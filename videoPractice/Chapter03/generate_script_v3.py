import os
import json
import random

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter03/script_chapter03.txt'
titles_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter03/titles_ch03.txt'
pdf_context_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter03/pdf_context.json'

with open(pdf_context_path, 'r', encoding='utf-8') as f:
    pdf_context = json.load(f)

text = """KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 3
Động lực và Mục tiêu Phân tích Dữ liệu

=========================================
Người 1 (Giảng viên): Hướng dẫn, phân tích các động lực kinh doanh và case study.
Người 2 (Sinh viên): Tương tác, đặt câu hỏi thực tế. (Xưng hô "thầy")
=========================================

Slide 1: TRANG BÌA
Người 1: Chào mừng các em đến với Chương 3. Hôm nay chúng ta học cách biến dữ liệu thành giá trị thực tiễn bằng việc xác định đúng "Động lực" và "Mục tiêu".
Người 2: Dạ em chào thầy. Em rất tò mò làm sao để biết mình nên bắt đầu phân tích từ đâu khi đối mặt với một đống dữ liệu khổng lồ ạ?

Slide 2: GÓC NHÌN CHUYÊN GIA
Người 1: Câu hỏi của em chính là cốt lõi! Chuyên gia khuyên: "Đừng lao vào tính toán khi chưa biết sếp cần gì". Hãy luôn bắt đầu bằng một câu hỏi kinh doanh.
Người 2: Vâng, giống như trước khi xây nhà thì phải có bản thiết kế trước vậy.

Slide 3: LỘ TRÌNH CHƯƠNG
Người 1: Hôm nay chúng ta đi qua 6 phần. Từ việc định hình câu hỏi nhờ động lực, cho đến việc thiết lập các câu hỏi Mô tả, Chẩn đoán, Dự đoán và Đề xuất.

Slide 4: 3.1 ĐỘNG LỰC ĐỊNH HÌNH CÂU HỎI PHÂN TÍCH NHƯ THẾ NÀO?
Người 1: Động lực là những tác nhân từ bên trong (nội bộ) hoặc bên ngoài (thị trường, đối thủ) thôi thúc công ty phải hành động.
Người 2: Chẳng hạn doanh thu giảm, hay bị đối thủ cướp khách hàng chính là động lực phải không ạ?

Slide 5: MỤC TIÊU RÕ RÀNG
Người 1: Đúng thế. Từ động lực đó, ta thiết lập "Mục tiêu" (Objective) - tức là thứ ta muốn đạt được để giải quyết động lực kia.
Người 2: Nghĩa là nếu động lực là "doanh số giảm", thì mục tiêu sẽ là "tìm ra nguyên nhân giảm và đề xuất chiến lược tăng doanh số 10%".

Slide 6: XÁC ĐỊNH MỤC TIÊU
Người 1: Chuẩn! Mục tiêu phải thật cụ thể. Càng mơ hồ, em càng dễ đi lạc trong mớ dữ liệu.
Người 2: Dạ vâng, em ghi nhớ điều này.

Slide 7: KẾT NỐI ĐỘNG LỰC VỚI MỤC TIÊU
Người 1: Khi động lực rõ ràng, mục tiêu sẽ tự động sắc bén. Chúng kết nối trực tiếp với nhau tạo thành một mũi tên định hướng cho việc chọn phương pháp phân tích.
Người 2: Việc xác định động lực và mục tiêu đúng là la bàn trong phân tích dữ liệu ạ.
"""

with open(titles_path, 'r', encoding='utf-8') as f:
    titles = f.read().splitlines()

titles.append('Slide 123: KẾT THÚC')

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
    'Bài tập này rất thực tế ạ, em sẽ áp dụng mô hình phân tích để làm ngay.'
]

for i in range(7, len(titles)):
    if ': ' in titles[i]:
        slide_title = titles[i].split(': ', 1)[1]
    else:
        slide_title = titles[i]
        
    text += f'\nSlide {i+1}: {slide_title.upper()}\n'
    
    slide_key = slide_title.upper().strip()
    context = pdf_context.get(slide_key, "")
    
    snippet = ""
    if context:
        snippet = context[:150].replace('\n', ' ').strip()
        if len(context) > 150:
            snippet = snippet.rsplit(' ', 1)[0] + '...'
            
    # Format the slide title nicely (e.g. "ILLUSTRATION 3.1" -> "Minh họa 3.1", "BE 3.2" -> "Bài tập BE 3.2")
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
            text += f'Người 1: Chuyển sang phần {nice_title}, các em chú ý quan sát chi tiết trên màn hình nhé.\n'
            text += 'Người 2: Dạ vâng thưa thầy.\n'
            
    elif 'BE ' in slide_title or 'EX ' in slide_title or 'PAC ' in slide_title:
        if snippet:
            t_template = random.choice(teacher_ex_templates)
            s_template = random.choice(student_ex_templates)
            text += f'Người 1: {t_template.format(title=slide_title, snippet=snippet)}\n'
            text += f'Người 2: {s_template}\n'
        else:
            text += f'Người 1: Chúng ta cùng thực hành với {slide_title}. Các em hãy vận dụng kiến thức vừa học nhé.\n'
            text += 'Người 2: Vâng, em sẽ đọc kỹ đề và phân tích từ khóa thưa thầy.\n'
            
    elif i+1 == 123:
        text += 'Người 1: Phù! Một chương vô cùng đồ sộ với 123 slides đã hoàn thành. Các em đã nắm được linh hồn của phân tích dữ liệu: Luôn bắt đầu từ Động lực kinh doanh!\n'
        text += 'Người 2: Dạ vâng, hôm nay học tuy dài nhưng em thấy rất liền mạch và hệ thống. Em cảm ơn thầy! Hẹn gặp lại mọi người ở chương sau!\n'
    else:
        # Avoid robotic normal slide text too
        normal_teacher = [
            f'Người 1: Ở nội dung "{slide_title}", chúng ta cần đặc biệt lưu ý những điểm cốt lõi.',
            f'Người 1: Bước sang phần "{slide_title}", đây là một khái niệm rất hay xuất hiện trong thực tế.',
            f'Người 1: Tiếp tục với phần "{slide_title}", các em hãy xâu chuỗi với những gì đã học ở phần trước.'
        ]
        normal_student = [
            'Người 2: Vâng, em đang ghi chú lại các ý chính này rồi thưa thầy.',
            'Người 2: Dạ, em đang theo dõi sát sao tiến trình bài giảng ạ.',
            'Người 2: Vâng thưa thầy, phần này rất logic và dễ hiểu.'
        ]
        text += f'{random.choice(normal_teacher)}\n'
        text += f'{random.choice(normal_student)}\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Generated natural script_chapter03.txt successfully!")
