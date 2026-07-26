import re

with open('docs/buoi_11.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Separate header and body
header_idx = text.find('#### ** 🇻🇳 Tiếng Việt (Bản dịch) **')
header_part = text[:header_idx + len('#### ** 🇻🇳 Tiếng Việt (Bản dịch) **')]
body_part = text[header_idx + len('#### ** 🇻🇳 Tiếng Việt (Bản dịch) **'):]
body_part = body_part.replace('<!-- tabs:end -->', '')

lines = body_part.split('\n')
cleaned_lines = []
for line in lines:
    s = line.strip()
    if not s:
        cleaned_lines.append('')
        continue
    # Remove OCR running page numbers like 2-0, 2-1, ..., 2-69
    if re.match(r'^2-\d+$', s):
        continue
    # Remove OCR running chapter headers
    if re.match(r'^CHƯƠNG\s*2\s+Kỹ\s+năng\s+phân\s+tích\s+dữ\s+liệu\s+cơ\s+bản$', s, re.IGNORECASE):
        continue
    # Remove --- Trang X ---
    if re.match(r'^---\s*Trang\s+\d+.*---$', s, re.IGNORECASE):
        continue
    if s == 'OceanofPDF.com':
        continue
    if s == '---':
        continue
    if s.isdigit() and len(s) <= 4:
        continue
    # Strip any existing headers from previous script runs to be 100% idempotent
    if (s.startswith('# PHẦN ') or
        re.match(r'^##\s+\d', s) or
        s.startswith('### *(Kỹ năng') or
        s.startswith('#### **❶') or
        s.startswith('#### **❷') or
        s.startswith('#### **❸') or
        s.startswith('#### **❹') or
        s.startswith('#### **❺') or
        s.startswith('### **MỤC TIÊU HỌC TẬP') or
        s.startswith('#### **EX ') or
        s.startswith('#### **PR ') or
        s.startswith('#### **PAC ') or
        s.startswith('#### **BE ') or
        s.startswith('#### **MINH HỌA ') or
        s.startswith('#### **CÁCH ') or
        re.match(r'^###\s+2\.4\.\d+', s) or
        re.match(r'^###\s+\*\*EX\s+2\.\d+', s) or
        re.match(r'^###\s+\*\*PR\s+2\.\d+', s) or
        re.match(r'^###\s+\*\*PAC\s+2\.\d+', s) or
        re.match(r'^###\s+\*\*BE\s+2\.\d+', s) or
        re.match(r'^####\s+\*\*BE\s+2\.\d+', s) or
        re.match(r'^####\s+\*\*EX\s+2\.\d+', s) or
        re.match(r'^####\s+\*\*PR\s+2\.\d+', s) or
        re.match(r'^####\s+\*\*PAC\s+2\.\d+', s)):
        continue
    cleaned_lines.append(s)

formatted_blocks = []
current_para = []

def flush_para():
    global current_para
    if not current_para:
        return
    text_para = ' '.join(current_para).strip()
    text_para = re.sub(r'\s+', ' ', text_para)
    if text_para:
        formatted_blocks.append(text_para)
    current_para = []

# Add Part I Header
formatted_blocks.append("# PHẦN I: TỔNG QUAN VÀ MỤC TIÊU HỌC TẬP (OVERVIEW & LEARNING OBJECTIVES)")
formatted_blocks.append("### *(Kỹ năng phân tích dữ liệu cơ bản - Basic Data Analytics Skills)*")

i = 0
in_html = False
html_block = []

inserted_part2 = False
inserted_part3 = False
inserted_part4 = False
inserted_part5 = False
inserted_part5_1 = False
inserted_part5_2 = False
inserted_part5_3 = False
inserted_part6 = False
inserted_part7 = False
inserted_part8 = False
inserted_part8_be = False
inserted_part8_ex = False
inserted_part8_pr = False
inserted_part8_pac = False

while i < len(cleaned_lines):
    s = cleaned_lines[i]
    if not s:
        if not in_html:
            flush_para()
        i += 1
        continue

    # Handle HTML blocks (<div ... </div>)
    if s.startswith('<div') or in_html:
        flush_para()
        in_html = True
        html_block.append(s)
        if s.endswith('</div>') or '</div>' in s:
            if html_block.count('<div') <= sum(1 for x in html_block if '</div>' in x):
                in_html = False
                formatted_blocks.append('\n'.join(html_block))
                html_block = []
        i += 1
        continue

    # Format Table of Contents LOs at beginning
    if re.match(r'^LO\s*2\.\d+.*', s) and not inserted_part2:
        flush_para()
        formatted_blocks.append(f"- **{s[:6]}**: {s[6:].strip()}")
        i += 1
        continue

    # Major Sections & Parts
    if ("2.1 Hiểu cách lưu trữ dữ liệu" in s or "2.1  Hiểu cách lưu trữ dữ liệu" in s) and not inserted_part2 and i < 300:
        flush_para()
        inserted_part2 = True
        formatted_blocks.append("---")
        formatted_blocks.append("# PHẦN II: CƠ SỞ DỮ LIỆU QUAN HỆ VÀ TRÍCH XUẤT DỮ LIỆU (RELATIONAL DATABASES & SQL - LO 2.1)")
        formatted_blocks.append("## 2.1 Khái niệm cơ sở dữ liệu quan hệ (Relational Database Concepts)")
        current_para.append(s)
        i += 1
        continue

    if ("2.2 Các hàm bảng tính" in s or "2.2  Các hàm bảng tính" in s) and not inserted_part3 and i < 1500:
        flush_para()
        inserted_part3 = True
        formatted_blocks.append("---")
        formatted_blocks.append("# PHẦN III: CÁC HÀM EXCEL CƠ BẢN TRONG PHÂN TÍCH DỮ LIỆU (EXCEL FUNCTIONS - LO 2.2)")
        formatted_blocks.append("## 2.2 Ứng dụng các hàm Excel cơ bản (Applying Basic Excel Functions)")
        current_para.append(s)
        i += 1
        continue

    if ("2.3 Chúng tôi tổ chức" in s or "2.3  Chúng tôi tổ chức" in s or "2.3 Chúng tôi sắp xếp" in s or "2.3  Chúng tôi sắp xếp" in s) and not inserted_part4 and i < 2500:
        flush_para()
        inserted_part4 = True
        formatted_blocks.append("---")
        formatted_blocks.append("# PHẦN IV: BẢNG TỔNG HỢP (PIVOTTABLE), SẮP XẾP VÀ LỌC DỮ LIỆU (PIVOTTABLES & FILTERING - LO 2.3)")
        formatted_blocks.append("## 2.3 Minh họa cách xoay bảng, sắp xếp và lọc dữ liệu (PivotTables, Sorting & Slicers)")
        current_para.append(s)
        i += 1
        continue

    if ("2.4 Biện pháp mô tả" in s or "2.4  Biện pháp mô tả" in s or "Các thước đo mô tả dữ liệu" in s) and not inserted_part5 and i < 3500:
        flush_para()
        inserted_part5 = True
        formatted_blocks.append("---")
        formatted_blocks.append("# PHẦN V: THỐNG KÊ MÔ TẢ TRONG PHÂN TÍCH DỮ LIỆU (DESCRIPTIVE STATISTICS - LO 2.4)")
        formatted_blocks.append("## 2.4 Các thước đo mô tả dữ liệu (Measures of Location, Spread, Shape & Correlation)")
        current_para.append(s)
        i += 1
        continue

    if s == "Tính toán số đo vị trí" and inserted_part5 and not inserted_part5_1:
        flush_para()
        inserted_part5_1 = True
        formatted_blocks.append("### 2.4.1 Các thước đo vị trí: Số trung bình, Trung vị và Yếu tố mốt (Measures of Location: Mean, Median & Mode)")
        i += 1
        continue

    if s == "Số đo hình dạng" and inserted_part5 and not inserted_part5_2:
        flush_para()
        inserted_part5_2 = True
        formatted_blocks.append("### 2.4.2 Thước đo hình dạng phân phối: Độ lệch (Measures of Shape: Skewness)")
        i += 1
        continue

    if s == "Phân tích tương quan" and inserted_part5 and not inserted_part5_3:
        flush_para()
        inserted_part5_3 = True
        formatted_blocks.append("### 2.4.3 Phân tích tương quan (Correlation Analysis)")
        i += 1
        continue

    if "Có hai loại trực quan hóa dữ liệu:" in s and not inserted_part6:
        flush_para()
        inserted_part6 = True
        formatted_blocks.append("---")
        formatted_blocks.append("# PHẦN VI: TRỰC QUAN HÓA DỮ LIỆU VÀ DASHBOARD (DATA VISUALIZATION & DASHBOARDS - LO 2.5)")
        formatted_blocks.append("## 2.5 Nguyên tắc và ứng dụng trực quan hóa dữ liệu (Data Visualization Best Practices & Tableau/Power BI)")
        current_para.append(s)
        i += 1
        continue

    if ("Ôn tập và thực hành chương" in s or "Đánh giá mục tiêu học tập" in s) and inserted_part6 and not inserted_part7:
        flush_para()
        inserted_part7 = True
        formatted_blocks.append("---")
        formatted_blocks.append("# PHẦN VII: TÓM TẮT CHƯƠNG VÀ HƯỚNG DẪN THỰC HÀNH (SUMMARY & HOW-TO GUIDES)")
        formatted_blocks.append("## 1. Tóm tắt các Mục tiêu Học tập (LO 2.1 - LO 2.5 Summary)")
        current_para.append(s)
        i += 1
        continue

    if "1. (LO 1) Một tập hợp các dữ liệu liên quan đến logic" in s and not inserted_part8:
        flush_para()
        inserted_part8 = True
        formatted_blocks.append("---")
        formatted_blocks.append("# PHẦN VIII: CÂU HỎI VÀ BÀI TẬP THỰC HÀNH (QUESTIONS & EXERCISES)")
        formatted_blocks.append("## 1. Câu hỏi trắc nghiệm (Multiple Choice Questions)")
        current_para.append(s)
        i += 1
        continue

    if ("BE 2.1" in s or "Bài tập ngắn gọn" in s) and inserted_part8 and not inserted_part8_be:
        flush_para()
        inserted_part8_be = True
        formatted_blocks.append("## 2. Bài tập ngắn gọn (Brief Exercises BE 2.1 – BE 2.14)")
        # Continue to handle BE 2.1 formatting below

    if re.match(r'^EX\s*2\.1\s.*', s) and not inserted_part8_ex:
        flush_para()
        inserted_part8_ex = True
        formatted_blocks.append("## 3. Bài tập thực hành (Exercises EX 2.1 – EX 2.10)")
        # Continue to handle EX 2.1 formatting below

    if re.match(r'^PR\s*2\.1\s.*', s) and not inserted_part8_pr:
        flush_para()
        inserted_part8_pr = True
        formatted_blocks.append("## 4. Bài tập vấn đề (Problems PR 2.1 – PR 2.4)")
        # Continue to handle PR 2.1 formatting below

    if re.match(r'^PAC\s*2\.1\s.*', s) and not inserted_part8_pac:
        flush_para()
        inserted_part8_pac = True
        formatted_blocks.append("## 5. Bài tập Kế toán & Phân tích (Accounting & Analytics PAC 2.1 – PAC 2.5)")
        # Continue to handle PAC 2.1 formatting below

    if s == "CÁCH 2.1" or s == "CÁCH 2.1 " or s.startswith("CÁCH 2.1"):
        flush_para()
        formatted_blocks.append("## 2. Hướng dẫn Thực hành 2.1: Tạo PivotTable và PivotChart (HOW TO 2.1)")
        i += 1
        continue

    if s == "CÁCH 2.2" or s == "CÁCH 2.2 " or s.startswith("CÁCH 2.2"):
        flush_para()
        formatted_blocks.append("## 3. Hướng dẫn Thực hành 2.2: Trực quan hóa với Tableau (HOW TO 2.2)")
        i += 1
        continue

    # Exercise IDs like BE 2.1, EX 2.1, PR 2.1, PAC 2.1
    if re.match(r'^(BE|EX|PR|PAC)\s*2\.\d+.*', s):
        flush_para()
        ex_text = s
        i += 1
        while i < len(cleaned_lines) and cleaned_lines[i] and not re.match(r'^(BE|EX|PR|PAC)\s*2\.\d+.*', cleaned_lines[i]) and not cleaned_lines[i].startswith('#') and not cleaned_lines[i].startswith('<div'):
            ex_text += " " + cleaned_lines[i]
            i += 1
        ex_text = re.sub(r'\s+', ' ', ex_text)
        formatted_blocks.append(f"#### **{ex_text[:80]}...**\n\n{ex_text}" if len(ex_text) > 80 else f"#### **{ex_text}**")
        continue

    # Captions (MINH HỌA 2.x or CÁCH 2.x)
    if re.match(r'^(MINH HỌA|CÁCH)\s*2\.\d+.*', s, re.IGNORECASE):
        flush_para()
        formatted_blocks.append(f"#### **{s}**")
        i += 1
        continue

    # Bullet lists starting with • or -
    if s.startswith('• ') or s.startswith('- '):
        flush_para()
        bullet_text = s[2:].strip()
        i += 1
        while i < len(cleaned_lines) and cleaned_lines[i] and not cleaned_lines[i].startswith('• ') and not cleaned_lines[i].startswith('- ') and not cleaned_lines[i].startswith('<div') and not cleaned_lines[i].startswith('#'):
            bullet_text += " " + cleaned_lines[i]
            i += 1
        bullet_text = re.sub(r'\s+', ' ', bullet_text)
        formatted_blocks.append(f"- {bullet_text}")
        continue

    # Numbered lists like 1. ..., 2. ...
    if re.match(r'^\d+\.\s+.*', s):
        flush_para()
        num_text = s
        i += 1
        while i < len(cleaned_lines) and cleaned_lines[i] and not re.match(r'^\d+\.\s+.*', cleaned_lines[i]) and not cleaned_lines[i].startswith('• ') and not cleaned_lines[i].startswith('<div') and not cleaned_lines[i].startswith('#'):
            num_text += " " + cleaned_lines[i]
            i += 1
        num_text = re.sub(r'\s+', ' ', num_text)
        formatted_blocks.append(f"- **{num_text}**" if len(num_text) < 80 else f"- {num_text}")
        continue

    current_para.append(s)
    i += 1

flush_para()

final_md = [header_part.strip(), ""]
for block in formatted_blocks:
    final_md.append(block)
    final_md.append("")
final_md.append("<!-- tabs:end -->")
final_md.append("")

with open('docs/buoi_11.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_md))

print("reformat_buoi_11.py completed! Block count:", len(formatted_blocks))
