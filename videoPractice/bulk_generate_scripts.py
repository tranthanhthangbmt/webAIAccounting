import PyPDF2
import re
import json
import random
import os

pdf_files = {
    6: "Ch_06_Analysis_Data Preparation.pdf",
    7: "Ch_07_Analysis_Data Exploration.pdf",
    8: "Ch_08_Interpreting Data Analysis Results.pdf",
    9: "Ch_09_Interpreting Data Analysis Results.pdf",
    10: "Ch_10_Recent Data and Analyses Developments in Accounting.pdf"
}

base_path = "d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting"
pdf_dir = f"{base_path}/TaiLieu/textbookForPractice"
slide_dir = f"{base_path}/TaiLieu/slidePractice"
video_dir = f"{base_path}/videoPractice"

# Common templates
teacher_ill_templates = [
    'Chúng ta cùng phân tích {title} nhé. Trọng tâm của phần này là: "{snippet}". Các em hãy lưu ý cách áp dụng vào thực tế.',
    'Các em xem minh họa ở {title} trên slide. Đoạn này đề cập đến: "{snippet}". Rất sát với tình huống doanh nghiệp.',
    'Slide tiếp theo là một ví dụ thực tế qua {title}. Cụ thể: "{snippet}". Phân tích kỹ sẽ giúp các em hiểu sâu hơn.',
    'Nhìn vào {title}, chúng ta có thể rút ra điều gì? Tài liệu có ghi: "{snippet}". Đây là một điểm rất đáng chú ý.',
    'Mời các em quan sát {title}. Điểm cốt lõi ở đây là: "{snippet}".'
]

student_ill_templates = [
    'Dạ, ví dụ này làm em thấy rõ hơn hẳn ạ.',
    'Vâng thưa thầy, hình ảnh này giải thích rất trực quan dễ hiểu.',
    'Dạ, kết hợp lý thuyết với minh họa thực tế thế này rất hiệu quả ạ.',
    'Em đã nắm được ý chính của phần này rồi thưa thầy.',
    'Dạ, nhờ minh họa này mà các khái niệm trở nên gần gũi hơn rất nhiều ạ.'
]

teacher_ex_templates = [
    'Bây giờ chúng ta cùng xem bài tập {title}. Đề bài đưa ra tình huống: "{snippet}". Các em thử suy nghĩ xem nên giải quyết thế nào.',
    'Đến phần thực hành với {title}. Dữ kiện bài toán: "{snippet}". Các em hãy vận dụng những gì vừa học để xác định yêu cầu nhé.',
    'Thử sức với {title} xem sao. Khởi đầu là: "{snippet}". Cứ bám sát phương pháp luận chúng ta đã học.'
]

student_ex_templates = [
    'Em sẽ bám sát vào các thông tin trong đề bài này để phân loại và giải quyết ạ.',
    'Dạ vâng, em đang gạch dưới các từ khóa quan trọng để tìm hướng đi thưa thầy.',
    'Bài tập này rất thực tế ạ, em sẽ áp dụng kỹ thuật để làm ngay.'
]

normal_teacher = [
    'Ở nội dung "{title}", chúng ta cần đặc biệt lưu ý những điểm cốt lõi.',
    'Bước sang phần "{title}", đây là một khái niệm rất hay xuất hiện trong thực tế.',
    'Tiếp tục với phần "{title}", các em hãy xâu chuỗi với các kỹ năng đã học trước đó.',
    'Phần "{title}" này chính là mấu chốt quan trọng.',
    'Các em tập trung vào slide "{title}" nhé, đây là nền tảng rất quan trọng.'
]

normal_student = [
    'Vâng, em đang ghi chú lại các ý chính này rồi thưa thầy.',
    'Dạ, em đang theo dõi sát sao tiến trình bài giảng ạ.',
    'Vâng thưa thầy, phần này rất logic và dễ áp dụng.',
    'Dạ em hiểu rồi ạ, phần này rất quan trọng.',
    'Thưa thầy, em đã gạch chân những từ khóa cốt lõi rồi ạ.'
]

chap_intros = {
    6: 'Chào mừng các em đến với Chương 6. Chúng ta sẽ tiếp tục đào sâu vào Kỹ năng Chuẩn bị Dữ liệu (Data Preparation), một khâu không thể thiếu.',
    7: 'Chào mừng các em đến với Chương 7. Hôm nay chúng ta sẽ khám phá dữ liệu (Data Exploration) để tìm ra những insight giá trị.',
    8: 'Chào mừng các em đến với Chương 8. Phần này chúng ta sẽ học cách diễn dịch kết quả phân tích (Interpreting Results) để đưa ra quyết định.',
    9: 'Chào mừng các em đến với Chương 9. Tiếp tục chủ đề Diễn dịch Kết quả, chúng ta sẽ ứng dụng sâu hơn vào các bài toán kế toán thực tế.',
    10: 'Chào mừng các em đến với Chương 10. Đây là chương cuối cùng, giới thiệu về các xu hướng và công nghệ phân tích mới nhất trong Kế toán.'
}

chap_outros = {
    6: 'Vậy là chúng ta đã kết thúc Chương 6. Hy vọng các em đã nắm vững các kỹ thuật xử lý dữ liệu phức tạp.',
    7: 'Vậy là chúng ta đã kết thúc Chương 7. Khám phá dữ liệu là một nghệ thuật, hãy luyện tập thường xuyên nhé.',
    8: 'Vậy là chúng ta đã kết thúc Chương 8. Đọc hiểu kết quả phân tích là kỹ năng sống còn của kế toán viên hiện đại.',
    9: 'Vậy là chúng ta đã kết thúc Chương 9. Các em hãy ứng dụng ngay những kỹ năng này vào công việc thực tế.',
    10: 'Chúng ta đã đi đến cuối hành trình với Chương 10. Chúc các em vận dụng thành công các công cụ tiên tiến này vào sự nghiệp Kế toán của mình!'
}

for ch, pdf_name in pdf_files.items():
    print(f"Processing Chapter {ch}...")
    ch_str = f"{ch:02d}"
    ch_dir = f"{video_dir}/Chapter{ch_str}"
    os.makedirs(ch_dir, exist_ok=True)
    
    # 1. Extract PDF
    pdf_path = f"{pdf_dir}/{pdf_name}"
    results = {}
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        text = re.sub(r'\n+', ' ', text)
        patterns = [
            r'(ILLUSTRATION ' + str(ch) + r'\.\d+[A-Z]?)(.*?)(?=ILLUSTRATION|BE ' + str(ch) + r'|EX ' + str(ch) + r'|PAC ' + str(ch) + r'|$)',
            r'(BE ' + str(ch) + r'\.\d+)(.*?)(?=ILLUSTRATION|BE ' + str(ch) + r'|EX ' + str(ch) + r'|PAC ' + str(ch) + r'|$)',
            r'(EX ' + str(ch) + r'\.\d+)(.*?)(?=ILLUSTRATION|BE ' + str(ch) + r'|EX ' + str(ch) + r'|PAC ' + str(ch) + r'|$)',
            r'(PAC ' + str(ch) + r'\.\d+)(.*?)(?=ILLUSTRATION|BE ' + str(ch) + r'|EX ' + str(ch) + r'|PAC ' + str(ch) + r'|$)'
        ]
        for pat in patterns:
            matches = re.findall(pat, text, re.IGNORECASE)
            for match in matches:
                title = match[0].upper()
                content = match[1].strip()[:500]
                if title not in results:
                    results[title] = content
        print(f"  -> Extracted {len(results)} items from PDF.")
    else:
        print(f"  -> PDF {pdf_path} not found.")

    # 2. Parse Tex and Generate Script
    tex_path = f"{slide_dir}/Slide_Practice_Ch{ch_str}.tex"
    if not os.path.exists(tex_path):
        print(f"  -> TEX {tex_path} not found. Skipping chapter {ch}.")
        continue
        
    tex_content = open(tex_path, encoding='utf-8').read()
    frames = re.findall(r'\\begin\{frame\}(?:\[.*?\])?(?:\{(.*?)\})?', tex_content)
    titles = [f if f else 'NO_TITLE' for f in frames]
    print(f"  -> Found {len(titles)} frames.")
    
    script_content = f"KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG {ch}\n"
    script_content += "=========================================\n"
    script_content += "Người 1 (Giảng viên): Chuyên gia phân tích dữ liệu kế toán.\n"
    script_content += "Người 2 (Sinh viên): Chăm chỉ, xưng \"thầy\", tương tác thực tế.\n"
    script_content += "=========================================\n"
    
    for i, slide_title in enumerate(titles):
        slide_title = slide_title.strip()
        if slide_title == "NO_TITLE":
            slide_title = "TRANG BÌA"
            
        script_content += f'\nSlide {i+1}: {slide_title.upper()}\n'
        
        if i == 0:
            script_content += f"Người 1: {chap_intros[ch]}\n"
            script_content += "Người 2: Dạ em chào thầy. Em đã sẵn sàng cho bài học hôm nay ạ.\n"
            continue
        elif i == len(titles) - 1:
            script_content += f"Người 1: {chap_outros[ch]}\n"
            script_content += "Người 2: Dạ vâng, em cảm ơn thầy rất nhiều ạ!\n"
            continue
            
        slide_key = slide_title.upper().strip()
        context = results.get(slide_key, "")
        
        snippet = ""
        if context:
            snippet = context[:150].replace('\n', ' ').strip()
            if len(context) > 150:
                snippet = snippet.rsplit(' ', 1)[0] + '...'
                
        nice_title = slide_title
        if 'ILLUSTRATION' in slide_title:
            nice_title = slide_title.replace('ILLUSTRATION', 'Minh họa')
        
        if 'ILLUSTRATION' in slide_title:
            if snippet:
                t_template = random.choice(teacher_ill_templates)
                s_template = random.choice(student_ill_templates)
                script_content += f'Người 1: {t_template.format(title=nice_title, snippet=snippet)}\n'
                script_content += f'Người 2: {s_template}\n'
            else:
                script_content += f'Người 1: Chuyển sang phần {nice_title}, các em chú ý quan sát chi tiết trên màn hình nhé.\n'
                script_content += 'Người 2: Dạ vâng thưa thầy.\n'
        elif 'BE ' in slide_title or 'EX ' in slide_title or 'PAC ' in slide_title:
            if snippet:
                t_template = random.choice(teacher_ex_templates)
                s_template = random.choice(student_ex_templates)
                script_content += f'Người 1: {t_template.format(title=slide_title, snippet=snippet)}\n'
                script_content += f'Người 2: {s_template}\n'
            else:
                script_content += f'Người 1: Chúng ta cùng thực hành với {slide_title}. Các em hãy vận dụng kiến thức vừa học nhé.\n'
                script_content += 'Người 2: Vâng, em sẽ đọc kỹ đề và phân tích từ khóa thưa thầy.\n'
        else:
            script_content += f'Người 1: {random.choice(normal_teacher).format(title=slide_title)}\n'
            script_content += f'Người 2: {random.choice(normal_student)}\n'
            
    output_path = f"{ch_dir}/script_chapter{ch_str}.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
        
    print(f"  -> Generated {output_path}")

print("All done!")
