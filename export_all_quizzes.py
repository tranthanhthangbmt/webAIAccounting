import os
import json
import re
import random
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Danh sách thông tin các buổi
SESSION_NAMES = {
    "Day01": "Buổi 1: What Accountants Need to Know",
    "Day02": "Buổi 2: AI and Blockchain in Finance",
    "Day03": "Buổi 3: Python for Finance & Data Science",
    "Day04": "Buổi 4: Algorithms and AI Concepts",
    "Day05": "Buổi 5: Data Analysis and Financial Modeling",
    "Day06": "Buổi 6: Machine Learning for Finance",
    "Day07": "Buổi 7: Deep Learning and Neural Networks",
    "Day08": "Buổi 8: Trí tuệ nhân tạo (AI) trong Kế toán",
    "Day09": "Buổi 9: Đạo đức kinh doanh và An toàn AI",
    "Day11": "Buổi 11: Chuẩn mực đạo đức Kế toán toàn cầu",
    "Day12": "Buổi 12: Thực hành AI nhận thức và AI tạo sinh",
    "Day13": "Buổi 13: Kỹ thuật Prompt & Phân tích dữ liệu (SPARKS)",
    "Day14": "Buổi 14: Phân tích Dữ liệu Chuyên sâu"
}

TYPE_VN = {
    "multiple_choice": "Trắc nghiệm",
    "ordering": "Sắp xếp thứ tự",
    "matching": "Ghép cặp",
    "fill_in_blanks": "Điền khuyết"
}

def clean_html(text):
    if not text:
        return ""
    text = re.sub(r'<span[^>]*class="blank-slot"[^>]*data-id="(\d+)"[^>]*>___(?:\(\d+\))?___</span>', r'___(\1)___', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def convert_question_to_mcq(q, q_idx):
    """
    Chuẩn hóa mọi loại câu hỏi (ordering, matching, fill_in_blanks, multiple_choice)
    thành dạng Trắc nghiệm 4 lựa chọn (A, B, C, D)
    """
    q_type = q.get("type", "multiple_choice")
    difficulty = q.get("difficulty", "Trung bình")
    explanation = clean_html(q.get("explanation", ""))
    
    # 1. TRẮC NGHIỆM ĐƠN (MULTIPLE CHOICE)
    if q_type == "multiple_choice":
        question_text = clean_html(q.get("question", ""))
        options_data = q.get("options", [])
        correct_ans_id = str(q.get("correctAnswer", "")).strip().lower()
        
        # Sắp xếp hoặc đọc options
        opt_dict = {}
        for opt in options_data:
            opt_id = str(opt.get("id", "")).strip().lower()
            opt_dict[opt_id] = clean_html(opt.get("text", ""))
        
        keys = ["a", "b", "c", "d"]
        options = {
            "A": opt_dict.get("a", ""),
            "B": opt_dict.get("b", ""),
            "C": opt_dict.get("c", ""),
            "D": opt_dict.get("d", "")
        }
        
        correct_letter = correct_ans_id.upper()
        if correct_letter not in ["A", "B", "C", "D"]:
            correct_letter = "A"
            
        return {
            "type_raw": q_type,
            "type_vn": TYPE_VN.get(q_type, q_type),
            "difficulty": difficulty,
            "question": question_text,
            "options": options,
            "correct": correct_letter,
            "explanation": explanation
        }

    # 2. SẮP XẾP THỨ TỰ (ORDERING)
    elif q_type == "ordering":
        prompt = clean_html(q.get("question", ""))
        items = q.get("items", [])
        correct_order = [str(x).strip() for x in q.get("correctOrder", [])]
        
        id_to_num = {str(item["id"]).strip(): f"({idx+1})" for idx, item in enumerate(items)}
        items_detail = "\n".join([f"  {id_to_num.get(str(item['id']).strip(), str(item['id']))} {clean_html(item['text'])}" for item in items])
        question_text = f"{prompt}\n{items_detail}\nThứ tự sắp xếp đúng là:"
        
        correct_seq = " ➔ ".join([id_to_num.get(cid, cid) for cid in correct_order])
        
        # Sinh 3 phương án sai
        all_cids = list(correct_order)
        distractors = []
        
        # Đảo ngược
        rev = list(reversed(all_cids))
        if rev != all_cids:
            distractors.append(" ➔ ".join([id_to_num.get(cid, cid) for cid in rev]))
            
        # Đổi chỗ 2 phần tử đầu
        if len(all_cids) >= 2:
            p2 = list(all_cids)
            p2[0], p2[1] = p2[1], p2[0]
            s = " ➔ ".join([id_to_num.get(cid, cid) for cid in p2])
            if s not in distractors and s != correct_seq:
                distractors.append(s)
                
        # Đổi chỗ 2 phần tử cuối
        if len(all_cids) >= 2:
            p3 = list(all_cids)
            p3[-1], p3[-2] = p3[-2], p3[-1]
            s = " ➔ ".join([id_to_num.get(cid, cid) for cid in p3])
            if s not in distractors and s != correct_seq:
                distractors.append(s)
                
        # Dịch chuyển vòng tròn
        p4 = all_cids[1:] + all_cids[:1]
        s = " ➔ ".join([id_to_num.get(cid, cid) for cid in p4])
        if s not in distractors and s != correct_seq:
            distractors.append(s)
            
        while len(distractors) < 3:
            distractors.append(f"Phương án thứ tự khác {len(distractors)+1}")
            
        distractors = distractors[:3]
        
        # Chọn vị trí ngẫu nhiên/xoay tua cho đáp án đúng
        pos_idx = q_idx % 4
        opts_list = list(distractors)
        opts_list.insert(pos_idx, correct_seq)
        
        letters = ["A", "B", "C", "D"]
        options = {letters[i]: opts_list[i] for i in range(4)}
        correct_letter = letters[pos_idx]
        
        return {
            "type_raw": q_type,
            "type_vn": TYPE_VN.get(q_type, q_type),
            "difficulty": difficulty,
            "question": question_text,
            "options": options,
            "correct": correct_letter,
            "explanation": explanation
        }

    # 3. GHÉP CẶP (MATCHING)
    elif q_type == "matching":
        prompt = clean_html(q.get("question", ""))
        left = q.get("left", [])
        right = q.get("right", [])
        correct_pairs = q.get("correctPairs", {})
        
        l_map = {str(item["id"]).strip(): f"{idx+1}" for idx, item in enumerate(left)}
        r_map = {str(item["id"]).strip(): chr(97+idx) for idx, item in enumerate(right)} # a, b, c...
        
        left_text = "\n".join([f"  ({l_map[str(item['id']).strip()]}) {clean_html(item['text'])}" for item in left])
        right_text = "\n".join([f"  ({r_map[str(item['id']).strip()]}) {clean_html(item['text'])}" for item in right])
        
        question_text = f"{prompt}\nCột 1:\n{left_text}\nCột 2:\n{right_text}\nPhương án ghép cặp đúng là:"
        
        pair_strs = []
        for l_id in left:
            lid_str = str(l_id["id"]).strip()
            rid_str = str(correct_pairs.get(lid_str, "")).strip()
            pair_strs.append(f"{l_map.get(lid_str, lid_str)}-{r_map.get(rid_str, rid_str)}")
        correct_str = ", ".join(pair_strs)
        
        # Sinh 3 phương án ghép sai
        distractors = []
        # Sai 1: Đảo ngược kết quả cột 2
        r_assigned = [r_map.get(str(correct_pairs.get(str(l["id"]).strip(), "")).strip(), "") for l in left]
        r_rev = list(reversed(r_assigned))
        s1 = ", ".join([f"{l_map[str(left[i]['id']).strip()]}-{r_rev[i]}" for i in range(len(left))])
        if s1 != correct_str:
            distractors.append(s1)
            
        # Sai 2: Dịch chuyển vòng
        r_shift = r_assigned[1:] + r_assigned[:1]
        s2 = ", ".join([f"{l_map[str(left[i]['id']).strip()]}-{r_shift[i]}" for i in range(len(left))])
        if s2 not in distractors and s2 != correct_str:
            distractors.append(s2)
            
        # Sai 3: Đổi chỗ 2 phần tử đầu
        if len(r_assigned) >= 2:
            r_swap = list(r_assigned)
            r_swap[0], r_swap[1] = r_swap[1], r_swap[0]
            s3 = ", ".join([f"{l_map[str(left[i]['id']).strip()]}-{r_swap[i]}" for i in range(len(left))])
            if s3 not in distractors and s3 != correct_str:
                distractors.append(s3)
                
        while len(distractors) < 3:
            distractors.append(f"Phương án ghép cặp khác {len(distractors)+1}")
            
        distractors = distractors[:3]
        
        pos_idx = (q_idx + 1) % 4
        opts_list = list(distractors)
        opts_list.insert(pos_idx, correct_str)
        
        letters = ["A", "B", "C", "D"]
        options = {letters[i]: opts_list[i] for i in range(4)}
        correct_letter = letters[pos_idx]
        
        return {
            "type_raw": q_type,
            "type_vn": TYPE_VN.get(q_type, q_type),
            "difficulty": difficulty,
            "question": question_text,
            "options": options,
            "correct": correct_letter,
            "explanation": explanation
        }

    # 4. ĐIỀN KHUYẾT (FILL IN BLANKS)
    elif q_type == "fill_in_blanks":
        prompt = clean_html(q.get("question", ""))
        body_text = clean_html(q.get("text", ""))
        words = q.get("words", [])
        correct_answers = q.get("correctAnswers", {})
        
        word_dict = {str(w["id"]).strip(): clean_html(w["text"]) for w in words}
        
        # Các chỗ trống theo thứ tự
        blank_slots = sorted(list(correct_answers.keys()), key=lambda x: int(x) if x.isdigit() else x)
        correct_words = [word_dict.get(str(correct_answers[slot]).strip(), "") for slot in blank_slots]
        correct_str = " ; ".join([f"({slot}) {w}" for slot, w in zip(blank_slots, correct_words)])
        
        question_text = f"{prompt}\n\"{body_text}\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:"
        
        # Sinh distractors
        all_word_texts = [clean_html(w["text"]) for w in words]
        distractors = []
        
        # Đảo ngược thứ tự từ
        if len(correct_words) > 1:
            rev_words = list(reversed(correct_words))
            s_rev = " ; ".join([f"({slot}) {w}" for slot, w in zip(blank_slots, rev_words)])
            if s_rev != correct_str:
                distractors.append(s_rev)
                
        # Sử dụng các từ gây nhiễu trong words
        extra_words = [w for w in all_word_texts if w not in correct_words]
        if extra_words:
            fake1 = []
            for i, slot in enumerate(blank_slots):
                fake1.append(f"({slot}) {extra_words[i % len(extra_words)]}")
            s_fake1 = " ; ".join(fake1)
            if s_fake1 not in distractors and s_fake1 != correct_str:
                distractors.append(s_fake1)
                
            fake2 = []
            for i, slot in enumerate(blank_slots):
                chosen = extra_words[(i+1) % len(extra_words)] if len(extra_words) > 1 else correct_words[(i+1)%len(correct_words)]
                fake2.append(f"({slot}) {chosen}")
            s_fake2 = " ; ".join(fake2)
            if s_fake2 not in distractors and s_fake2 != correct_str:
                distractors.append(s_fake2)
                
        while len(distractors) < 3:
            distractors.append(f"Phương án điền từ khác {len(distractors)+1}")
            
        distractors = distractors[:3]
        
        pos_idx = (q_idx + 2) % 4
        opts_list = list(distractors)
        opts_list.insert(pos_idx, correct_str)
        
        letters = ["A", "B", "C", "D"]
        options = {letters[i]: opts_list[i] for i in range(4)}
        correct_letter = letters[pos_idx]
        
        return {
            "type_raw": q_type,
            "type_vn": TYPE_VN.get(q_type, q_type),
            "difficulty": difficulty,
            "question": question_text,
            "options": options,
            "correct": correct_letter,
            "explanation": explanation
        }

    return None

def extract_all_questions():
    quizzes_dir = "quizzes"
    days = sorted([d for d in os.listdir(quizzes_dir) if os.path.isdir(os.path.join(quizzes_dir, d))])
    
    all_data = []
    global_idx = 1
    
    for day in days:
        html_path = os.path.join(quizzes_dir, day, "index.html")
        if not os.path.exists(html_path):
            continue
            
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        m = re.search(r'const questions\s*=\s*(\[[\s\S]*?\]);(?:\s*(?:let|const|var|function|\n\s*//|\n\s*let|\n\s*const))', content)
        if not m:
            print(f"Warning: Không tìm thấy questions trong {day}")
            continue
            
        qs = json.loads(m.group(1))
        session_title = SESSION_NAMES.get(day, day)
        
        for local_idx, q in enumerate(qs):
            mcq = convert_question_to_mcq(q, local_idx)
            if mcq:
                mcq["global_stt"] = global_idx
                mcq["session_key"] = day
                mcq["session_name"] = session_title
                mcq["local_stt"] = local_idx + 1
                all_data.append(mcq)
                global_idx += 1
                
    return all_data

def export_to_excel(all_questions, output_path):
    wb = openpyxl.Workbook()
    # Sheet 1: Master 390
    ws_all = wb.active
    ws_all.title = "Tất cả 390 câu hỏi"
    
    headers = [
        "STT Tổng", "Buổi học", "STT Buổi", "Dạng gốc", "Độ khó",
        "Nội dung câu hỏi", "Đáp án A", "Đáp án B", "Đáp án C", "Đáp án D",
        "Đáp án đúng", "Giải thích chi tiết"
    ]
    
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    left_align = Alignment(horizontal="left", vertical="top", wrap_text=True)
    border_thin = Side(border_style="thin", color="D9D9D9")
    box_border = Border(left=border_thin, right=border_thin, top=border_thin, bottom=border_thin)
    
    ws_all.append(headers)
    for col_idx in range(1, len(headers) + 1):
        cell = ws_all.cell(row=1, column=col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
    
    for q in all_questions:
        row = [
            q["global_stt"],
            q["session_name"],
            q["local_stt"],
            q["type_vn"],
            q["difficulty"],
            q["question"],
            q["options"]["A"],
            q["options"]["B"],
            q["options"]["C"],
            q["options"]["D"],
            q["correct"],
            q["explanation"]
        ]
        ws_all.append(row)
        current_row = ws_all.max_row
        for col_idx in range(1, len(row) + 1):
            cell = ws_all.cell(row=current_row, column=col_idx)
            cell.border = box_border
            if col_idx in [1, 3, 4, 5, 11]:
                cell.alignment = center_align
            else:
                cell.alignment = left_align
                
    # Sheet 2: 156 Pure MCQ
    ws_pure = wb.create_sheet(title="156 Trắc nghiệm thuần túy")
    ws_pure.append(headers)
    for col_idx in range(1, len(headers) + 1):
        cell = ws_pure.cell(row=1, column=col_idx)
        cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="276A3C", end_color="276A3C", fill_type="solid")
        cell.alignment = center_align
        
    pure_stt = 1
    for q in all_questions:
        if q["type_raw"] == "multiple_choice":
            row = [
                pure_stt,
                q["session_name"],
                q["local_stt"],
                q["type_vn"],
                q["difficulty"],
                q["question"],
                q["options"]["A"],
                q["options"]["B"],
                q["options"]["C"],
                q["options"]["D"],
                q["correct"],
                q["explanation"]
            ]
            ws_pure.append(row)
            current_row = ws_pure.max_row
            for col_idx in range(1, len(row) + 1):
                cell = ws_pure.cell(row=current_row, column=col_idx)
                cell.border = box_border
                if col_idx in [1, 3, 4, 5, 11]:
                    cell.alignment = center_align
                else:
                    cell.alignment = left_align
            pure_stt += 1
            
    # Auto-adjust column widths
    for sheet in [ws_all, ws_pure]:
        sheet.column_dimensions["A"].width = 10
        sheet.column_dimensions["B"].width = 25
        sheet.column_dimensions["C"].width = 10
        sheet.column_dimensions["D"].width = 14
        sheet.column_dimensions["E"].width = 12
        sheet.column_dimensions["F"].width = 45
        sheet.column_dimensions["G"].width = 28
        sheet.column_dimensions["H"].width = 28
        sheet.column_dimensions["I"].width = 28
        sheet.column_dimensions["J"].width = 28
        sheet.column_dimensions["K"].width = 12
        sheet.column_dimensions["L"].width = 35

    wb.save(output_path)
    print(f"Đã lưu Excel: {output_path}")

def export_to_quizizz_template(all_questions, output_path):
    """Template chuẩn Quizizz Excel"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Quizizz Questions"
    
    headers = [
        "Question Text", "Question Type", "Option 1", "Option 2", 
        "Option 3", "Option 4", "Option 5", "Correct Answer", "Time in seconds", "Image Link"
    ]
    ws.append(headers)
    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="8854D0", end_color="8854D0", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    correct_map = {"A": "1", "B": "2", "C": "3", "D": "4"}
    for q in all_questions:
        ans_num = correct_map.get(q["correct"], "1")
        row = [
            q["question"],
            "Multiple Choice",
            q["options"]["A"],
            q["options"]["B"],
            q["options"]["C"],
            q["options"]["D"],
            "", # Option 5
            ans_num,
            "45", # 45s mỗi câu
            ""
        ]
        ws.append(row)
        
    ws.column_dimensions["A"].width = 50
    ws.column_dimensions["B"].width = 16
    ws.column_dimensions["C"].width = 25
    ws.column_dimensions["D"].width = 25
    ws.column_dimensions["E"].width = 25
    ws.column_dimensions["F"].width = 25
    ws.column_dimensions["H"].width = 15
    ws.column_dimensions["I"].width = 15
    
    wb.save(output_path)
    print(f"Đã lưu Quizizz Excel: {output_path}")

def export_to_moodle_aiken(all_questions, output_path):
    """Chuẩn Aiken format cho Moodle / Canvas LMS"""
    with open(output_path, "w", encoding="utf-8") as f:
        for q in all_questions:
            # Aiken requires question text on lines, followed by A. B. C. D. then ANSWER: X
            q_clean = q["question"].replace("\n", " ")
            f.write(f"{q_clean}\n")
            f.write(f"A. {q['options']['A']}\n")
            f.write(f"B. {q['options']['B']}\n")
            f.write(f"C. {q['options']['C']}\n")
            f.write(f"D. {q['options']['D']}\n")
            f.write(f"ANSWER: {q['correct']}\n\n")
    print(f"Đã lưu Moodle Aiken (.txt): {output_path}")

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def export_to_word_docx(all_questions, output_path, title="NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM AI TRONG KẾ TOÁN"):
    doc = Document()
    
    # Cấu hình lề trang 2cm
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    # Tiêu đề
    p_uni = doc.add_paragraph()
    r_uni = p_uni.add_run("TRƯỜNG ĐẠI HỌC ĐÔNG Á\nKHOA KẾ TOÁN - TÀI CHÍNH")
    r_uni.font.name = "Times New Roman"
    r_uni.font.size = Pt(11)
    r_uni.font.bold = True
    p_uni.alignment = WD_ALIGN_PARAGRAPH.LEFT
    
    p_title = doc.add_paragraph()
    r_title = p_title.add_run(title.upper())
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(27, 73, 125)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run(f"Tổng số: {len(all_questions)} câu hỏi trắc nghiệm kèm đáp án và giải thích chi tiết\n(Định dạng tương thích 100% với Azota, Microsoft Forms, Google Forms và in đề thi)")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_paragraph().paragraph_format.space_after = Pt(10)
    
    current_session = ""
    for q in all_questions:
        if q["session_name"] != current_session:
            current_session = q["session_name"]
            p_sess = doc.add_paragraph()
            p_sess.paragraph_format.space_before = Pt(16)
            p_sess.paragraph_format.space_after = Pt(6)
            r_sess = p_sess.add_run(f"═══ {current_session.upper()} ═══")
            r_sess.font.name = "Times New Roman"
            r_sess.font.size = Pt(13)
            r_sess.font.bold = True
            r_sess.font.color.rgb = RGBColor(16, 52, 98)
            
        diff_raw = str(q.get("difficulty", "")).lower()
        if "dễ" in diff_raw:
            diff_code = "NB"
        elif "khó" in diff_raw and "rất" in diff_raw:
            diff_code = "VDC"
        elif "khó" in diff_raw:
            diff_code = "VD"
        else:
            diff_code = "TH"
            
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(6)
        p_q.paragraph_format.space_after = Pt(2)
        
        r_num = p_q.add_run(f"Câu {q['global_stt']} [{diff_code}]: ")
        r_num.font.name = "Times New Roman"
        r_num.font.bold = True
        r_num.font.size = Pt(11)
        r_num.font.color.rgb = RGBColor(20, 20, 20)
        
        r_qtext = p_q.add_run(q["question"])
        r_qtext.font.name = "Times New Roman"
        r_qtext.font.size = Pt(11)
        
        # Các phương án A, B, C, D (hoàn toàn đồng nhất font thường, màu đen)
        for letter in ["A", "B", "C", "D"]:
            p_opt = doc.add_paragraph()
            p_opt.paragraph_format.left_indent = Inches(0.25)
            p_opt.paragraph_format.space_before = Pt(1)
            p_opt.paragraph_format.space_after = Pt(1)
            
            is_correct = (letter == q["correct"])
            
            # Format chuẩn Azota: dấu sao trước chữ cái đáp án đúng (Azota tự động ẩn dấu * đối với thí sinh)
            prefix = f"*{letter}. " if is_correct else f"{letter}. "
            
            r_let = p_opt.add_run(prefix)
            r_let.font.name = "Times New Roman"
            r_let.font.size = Pt(11)
            r_let.font.bold = False
            r_let.font.underline = False
            r_let.font.color.rgb = RGBColor(0, 0, 0)
                
            r_opt_text = p_opt.add_run(q["options"][letter])
            r_opt_text.font.name = "Times New Roman"
            r_opt_text.font.size = Pt(11)
            r_opt_text.font.bold = False
            r_opt_text.font.underline = False
            r_opt_text.font.color.rgb = RGBColor(0, 0, 0)
                
        # Lời giải chi tiết
        if q["explanation"]:
            p_exp = doc.add_paragraph()
            p_exp.paragraph_format.left_indent = Inches(0.25)
            p_exp.paragraph_format.space_before = Pt(2)
            p_exp.paragraph_format.space_after = Pt(8)
            
            r_exp_title = p_exp.add_run("Lời giải: ")
            r_exp_title.font.name = "Times New Roman"
            r_exp_title.font.size = Pt(10)
            r_exp_title.font.italic = True
            r_exp_title.font.bold = True
            r_exp_title.font.color.rgb = RGBColor(120, 60, 0)
            
            r_exp = p_exp.add_run(q["explanation"])
            r_exp.font.name = "Times New Roman"
            r_exp.font.size = Pt(10)
            r_exp.font.italic = True
            r_exp.font.color.rgb = RGBColor(70, 70, 70)
            
    # BẢNG TỔNG HỢP ĐÁP ÁN CUỐI TÀI LIỆU (Chuẩn Azota & giáo viên kiểm tra)
    doc.add_page_break()
    p_ans_title = doc.add_paragraph()
    r_ans_title = p_ans_title.add_run("BẢNG TỔNG HỢP ĐÁP ÁN TRẮC NGHIỆM")
    r_ans_title.font.name = "Times New Roman"
    r_ans_title.font.size = Pt(14)
    r_ans_title.font.bold = True
    r_ans_title.font.color.rgb = RGBColor(27, 73, 125)
    p_ans_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Tạo bảng 10 cột đáp án
    num_cols = 10
    total_q = len(all_questions)
    num_rows = (total_q + num_cols - 1) // num_cols
    
    table = doc.add_table(rows=num_rows * 2, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'
    
    q_map = {q["global_stt"]: q["correct"] for q in all_questions}
    
    for r in range(num_rows):
        # Hàng câu hỏi
        for c in range(num_cols):
            q_num = r * num_cols + c + 1
            cell_header = table.cell(r * 2, c)
            set_cell_background(cell_header, "1F497D")
            p_h = cell_header.paragraphs[0]
            p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if q_num <= total_q:
                r_h = p_h.add_run(f"Câu {q_num}")
                r_h.font.bold = True
                r_h.font.size = Pt(9)
                r_h.font.color.rgb = RGBColor(255, 255, 255)
            else:
                p_h.add_run("")
                
        # Hàng đáp án
        for c in range(num_cols):
            q_num = r * num_cols + c + 1
            cell_ans = table.cell(r * 2 + 1, c)
            p_a = cell_ans.paragraphs[0]
            p_a.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if q_num <= total_q:
                r_a = p_a.add_run(q_map.get(q_num, ""))
                r_a.font.bold = True
                r_a.font.size = Pt(10)
                r_a.font.color.rgb = RGBColor(200, 0, 0)
            else:
                p_a.add_run("")
                
    doc.save(output_path)
    print(f"Đã lưu Word (.docx): {output_path}")

def export_by_session(all_questions, base_folder):
    """Xuất từng buổi riêng lẻ (Day01 -> Day14)"""
    sessions_folder = os.path.join(base_folder, "Tung_Buoi")
    os.makedirs(sessions_folder, exist_ok=True)
    
    from collections import defaultdict
    grouped = defaultdict(list)
    for q in all_questions:
        grouped[q["session_key"]].append(q)
        
    for s_key, s_qs in grouped.items():
        s_title = SESSION_NAMES.get(s_key, s_key)
        safe_name = s_title.replace(":", " -").replace("/", "-")
        
        # Word
        docx_path = os.path.join(sessions_folder, f"{safe_name}.docx")
        # Đánh lại STT từ 1..30 cho buổi đó
        session_qs_copy = []
        for idx, item in enumerate(s_qs):
            item_copy = dict(item)
            item_copy["global_stt"] = idx + 1
            session_qs_copy.append(item_copy)
        export_to_word_docx(session_qs_copy, docx_path, title=f"ĐỀ KIỂM TRA TRẮC NGHIỆM - {s_title}")
        
        # Excel
        xlsx_path = os.path.join(sessions_folder, f"{safe_name}.xlsx")
        export_to_excel(session_qs_copy, xlsx_path)
        
        # Aiken
        aiken_path = os.path.join(sessions_folder, f"{safe_name}_Aiken.txt")
        export_to_moodle_aiken(session_qs_copy, aiken_path)
        
    print(f"Đã xuất toàn bộ 13 buổi vào: {sessions_folder}")

def main():
    output_dir = "NganHangCauHoi_TracNghiem"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Đang trích xuất dữ liệu câu hỏi...")
    all_qs = extract_all_questions()
    print(f"Tổng số câu hỏi đã trích xuất: {len(all_qs)}")
    
    # 1. Excel Master
    excel_path = os.path.join(output_dir, "NganHang_390_CauHoi_AI_KeToan.xlsx")
    export_to_excel(all_qs, excel_path)
    
    # 2. Quizizz Excel Template
    quizizz_path = os.path.join(output_dir, "Quizizz_Template_390_CauHoi.xlsx")
    export_to_quizizz_template(all_qs, quizizz_path)
    
    # 3. Word Master (Chuẩn Azota / MS Forms)
    docx_path = os.path.join(output_dir, "NganHang_390_CauHoi_AI_KeToan.docx")
    export_to_word_docx(all_qs, docx_path)
    
    # 4. Moodle Aiken TXT
    aiken_path = os.path.join(output_dir, "Moodle_Aiken_390_CauHoi.txt")
    export_to_moodle_aiken(all_qs, aiken_path)
    
    # 5. JSON Master
    json_path = os.path.join(output_dir, "NganHang_390_CauHoi_AI_KeToan.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu JSON: {json_path}")
    
    # 6. Xuất từng buổi
    export_by_session(all_qs, output_dir)
    print("\nHOÀN TẤT XUẤT TOÀN BỘ CÂU HỎI TRẮC NGHIỆM!")

if __name__ == "__main__":
    main()
