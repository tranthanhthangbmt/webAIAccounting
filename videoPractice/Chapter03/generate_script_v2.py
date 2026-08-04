import os
import json

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter03/script_chapter03.txt'
titles_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter03/titles_ch03.txt'
pdf_context_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter03/pdf_context.json'

with open(pdf_context_path, 'r', encoding='utf-8') as f:
    pdf_context = json.load(f)

text = """KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 3
Động lực và Mục tiêu Phân tích Dữ liệu

=========================================
Người 1 (Giảng viên): Hướng dẫn, phân tích các động lực kinh doanh và case study.
Người 2 (Sinh viên): Tương tác, đặt câu hỏi thực tế.
=========================================

Slide 1: TRANG BÌA
Người 1: Chào mừng các em đến với Chương 3. Hôm nay chúng ta học cách biến dữ liệu thành giá trị thực tiễn bằng việc xác định đúng "Động lực" và "Mục tiêu".
Người 2: Dạ em chào thầy/cô. Em rất tò mò làm sao để biết mình nên bắt đầu phân tích từ đâu khi đối mặt với một đống dữ liệu khổng lồ ạ?

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

for i in range(7, len(titles)):
    if ': ' in titles[i]:
        slide_title = titles[i].split(': ', 1)[1]
    else:
        slide_title = titles[i]
        
    text += f'\nSlide {i+1}: {slide_title.upper()}\n'
    
    # Check if we have context for this slide from the PDF
    slide_key = slide_title.upper().strip()
    context = pdf_context.get(slide_key, "")
    
    snippet = ""
    if context:
        snippet = context[:150].replace('\n', ' ').strip()
        if len(context) > 150:
            snippet = snippet.rsplit(' ', 1)[0] + '...'
            
    if 'ILLUSTRATION' in slide_title:
        if snippet:
            text += f'Người 1: Mời các em quan sát hình {slide_title}. Nội dung chính ở đây là: "{snippet}". Hãy xem cách nó được áp dụng vào thực tế.\n'
            text += 'Người 2: Dạ, khi kết hợp nội dung này với hình ảnh trực quan, em hiểu rõ ngữ cảnh hơn hẳn ạ.\n'
        else:
            text += 'Người 1: Mời các em quan sát hình minh họa trên slide này để thấy rõ ứng dụng thực tế.\n'
            text += 'Người 2: Dạ, hình ảnh trực quan giúp em dễ hình dung hơn hẳn ạ.\n'
    elif 'BE ' in slide_title or 'EX ' in slide_title or 'PAC ' in slide_title:
        if snippet:
            text += f'Người 1: Chúng ta cùng xem bài tập {slide_title}. Đề bài đề cập: "{snippet}". Các em hãy xác định loại câu hỏi phân tích phù hợp nhất.\n'
            text += 'Người 2: Em sẽ dựa vào các thông tin trong đề bài này để phân loại và giải quyết ạ.\n'
        else:
            text += 'Người 1: Chúng ta cùng xem bài tập này. Các em hãy xác định loại câu hỏi phân tích phù hợp nhất.\n'
            text += 'Người 2: Em sẽ dựa vào các từ khóa trong đề bài để phân loại và làm bài ạ.\n'
    elif i+1 == 123:
        text += 'Người 1: Phù! Một chương vô cùng đồ sộ với 123 slides đã hoàn thành. Các em đã nắm được linh hồn của phân tích dữ liệu: Luôn bắt đầu từ Động lực kinh doanh!\n'
        text += 'Người 2: Dạ vâng, hôm nay học tuy dài nhưng em thấy rất liền mạch và hệ thống. Em cảm ơn thầy/cô! Hẹn gặp lại mọi người ở chương sau!\n'
    else:
        text += f'Người 1: Ở slide này, chúng ta tiếp tục đi sâu vào khái niệm cốt lõi. {slide_title} đóng vai trò quan trọng trong việc thiết lập câu hỏi phân tích.\n'
        text += 'Người 2: Vâng, em đang theo dõi và đối chiếu với dữ liệu thực tế.\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Generated script_chapter03.txt successfully with specific PDF contexts!")
