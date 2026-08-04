import re
import json
import random

tex_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/slidePractice/Slide_Practice_Ch05.tex'
output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter05/script_chapter05.txt'
pdf_context_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter05/pdf_context_ch05.json'

with open(pdf_context_path, 'r', encoding='utf-8') as f:
    pdf_context = json.load(f)

tex_content = open(tex_path, encoding='utf-8').read()
frames = re.findall(r'\\begin\{frame\}(?:\[.*?\])?(?:\{(.*?)\})?', tex_content)
titles = [f if f else 'NO_TITLE' for f in frames]

print(f'Found {len(titles)} frames for Chapter 05')

text = """KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 5
Chuẩn bị và Làm sạch Dữ liệu (Data Preparation)

=========================================
Người 1 (Giảng viên): Chuyên gia thực chiến, hướng dẫn kỹ thuật xử lý dữ liệu lỗi.
Người 2 (Sinh viên): Chăm chỉ, xưng "thầy", thích thú với các hàm xử lý dữ liệu.
=========================================
"""

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
    'Bài tập này rất thực tế ạ, em sẽ áp dụng kỹ thuật làm sạch dữ liệu để làm ngay.'
]

normal_teacher = [
    'Ở nội dung "{title}", chúng ta cần đặc biệt lưu ý những điểm cốt lõi về kỹ thuật chuẩn bị dữ liệu.',
    'Bước sang phần "{title}", đây là một khái niệm rất hay xuất hiện trong thực tế làm sạch dữ liệu.',
    'Tiếp tục với phần "{title}", các em hãy xâu chuỗi với các kỹ năng đã học trước đó.',
    'Phần "{title}" này chính là mấu chốt để tránh rủi ro dữ liệu rác (Garbage in).',
    'Các em tập trung vào slide "{title}" nhé, đây là nền tảng rất quan trọng khi trực tiếp thao tác với cơ sở dữ liệu.'
]

normal_student = [
    'Vâng, em đang ghi chú lại các ý chính này rồi thưa thầy.',
    'Dạ, em đang theo dõi sát sao tiến trình bài giảng ạ.',
    'Vâng thưa thầy, phần này rất logic và dễ áp dụng.',
    'Dạ em hiểu rồi, việc làm sạch cẩn thận giúp tránh sai số rất lớn.',
    'Thưa thầy, em đã gạch chân những từ khóa cốt lõi rồi ạ.'
]

for i, title in enumerate(titles):
    slide_title = title.strip()
    if slide_title == "NO_TITLE":
        slide_title = "TRANG BÌA"
        
    text += f'\nSlide {i+1}: {slide_title.upper()}\n'
    
    if i == 0:
        text += 'Người 1: Chào mừng các em đến với Chương 5. Đây là phần "đổ mồ hôi" nhất nhưng lại quan trọng nhất của phân tích dữ liệu: Chuẩn bị và Làm sạch Dữ liệu. Quá trình này thường chiếm đến 80% thời gian của một dự án.\n'
        text += 'Người 2: Dạ em chào thầy. Thưa thầy, tại sao lại mất nhiều thời gian đến vậy ạ? Chẳng phải dữ liệu từ hệ thống xuất ra là dùng được luôn sao thầy?\n'
        continue
    elif i == len(titles) - 1:
        text += 'Người 1: Vậy là chúng ta đã kết thúc Chương 5. Kỹ năng làm sạch và chuẩn bị dữ liệu chính là vũ khí mạnh nhất của một kế toán viên trong kỷ nguyên số.\n'
        text += 'Người 2: Dạ vâng, hôm nay em đã học được rất nhiều thủ thuật để dọn dẹp "dữ liệu rác". Cảm ơn thầy rất nhiều ạ!\n'
        continue

    slide_key = slide_title.upper().strip()
    context = pdf_context.get(slide_key, "")
    
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
            text += f'Người 1: {t_template.format(title=nice_title, snippet=snippet)}\n'
            text += f'Người 2: {s_template}\n'
        else:
            text += f'Người 1: Chuyển sang phần {nice_title}, các em chú ý quan sát cách xử lý lỗi trên màn hình nhé.\n'
            text += 'Người 2: Dạ vâng thưa thầy.\n'
            
    elif 'BE ' in slide_title or 'EX ' in slide_title or 'PAC ' in slide_title:
        if snippet:
            t_template = random.choice(teacher_ex_templates)
            s_template = random.choice(student_ex_templates)
            text += f'Người 1: {t_template.format(title=slide_title, snippet=snippet)}\n'
            text += f'Người 2: {s_template}\n'
        else:
            text += f'Người 1: Chúng ta cùng thực hành với {slide_title}. Các em hãy vận dụng kiến thức chuẩn bị dữ liệu vừa học nhé.\n'
            text += 'Người 2: Vâng, em sẽ đọc kỹ đề và phân tích từ khóa thưa thầy.\n'
            
    else:
        text += f'Người 1: {random.choice(normal_teacher).format(title=slide_title)}\n'
        text += f'Người 2: {random.choice(normal_student)}\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Generated natural script_chapter05.txt successfully with specific PDF contexts!")
