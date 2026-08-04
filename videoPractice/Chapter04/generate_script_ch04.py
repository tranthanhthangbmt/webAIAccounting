import os
import sys

sys.path.insert(0, 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/slidePractice')
import slide_data_ch04

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter04/script_chapter04.txt'

text = """KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 4
Lập Kế hoạch Dữ liệu và Chiến lược Phân tích

=========================================
Người 1 (Giảng viên): Hướng dẫn, phân tích tư duy chiến lược dữ liệu.
Người 2 (Sinh viên): Tương tác, đặt câu hỏi thực tế (luôn xưng hô là "thầy").
=========================================

Slide 1: TRANG BÌA
Người 1: Chào mừng các em đến với Chương 4. Sau khi đã biết cách đặt câu hỏi phân tích, bước tiếp theo sống còn chính là Lập Kế hoạch Dữ liệu. Chúng ta không thể phân tích nếu không có nguyên liệu đầu vào.
Người 2: Dạ em chào thầy. Thưa thầy, phần này có giống với việc mình đi siêu thị mua nguyên liệu trước khi nấu ăn không ạ?

Slide 2: GÓC NHÌN CHUYÊN GIA
Người 1: Chính xác! Như chuyên gia đã nói: "Dữ liệu rác đầu vào thì kết quả rác đầu ra" (Garbage in, Garbage out). Việc chọn đúng dữ liệu quyết định 90% sự thành bại của dự án.
Người 2: Vâng, em rất thấm thía câu nói này. Phân tích hay đến mấy mà dữ liệu sai thì vứt đi hết ạ.

Slide 3: LỘ TRÌNH CHƯƠNG
Người 1: Hôm nay chúng ta sẽ đi qua các phần: Nhận diện dữ liệu chất lượng, Phân biệt dữ liệu nội bộ và bên ngoài, và đặc biệt là cách trích xuất dữ liệu từ nhiều nguồn khác nhau.
Người 2: Dạ thưa thầy, em đã sẵn sàng ghi chép phần trích xuất dữ liệu rồi ạ.
"""

titles = [s.get('title', 'NO_TITLE') for s in slide_data_ch04.slides]

# Assuming there might be a mismatch or exactly 80 titles in data, let's pad or adapt to reach up to 81
# Slide_Practice_Ch04.tex had 81 frames. The titles in py file might be slightly fewer if title slide is not there, or end slide is hardcoded.
# We will just iterate over whatever is in `titles` and append the end slide.

for i in range(3, len(titles)):
    slide_title = titles[i]
    text += f'\nSlide {i+1}: {slide_title.upper()}\n'
    if 'ILLUSTRATION' in slide_title or 'Hình minh họa' in slide_title:
        text += 'Người 1: Mời các em quan sát hình minh họa trên slide này để thấy rõ cách dữ liệu được cấu trúc.\n'
        text += 'Người 2: Dạ, hình ảnh này giúp em dễ hình dung hơn hẳn ạ.\n'
    elif 'BE ' in slide_title or 'EX ' in slide_title or 'PAC ' in slide_title or 'Bài tập' in slide_title:
        text += 'Người 1: Nào, chúng ta cùng áp dụng vào bài tập này. Các em hãy xác định nguồn và loại dữ liệu cần thiết.\n'
        text += 'Người 2: Thưa thầy, em sẽ dựa vào yêu cầu kinh doanh để xác định xem cần dữ liệu nội bộ hay bên ngoài ạ.\n'
    else:
        text += f'Người 1: Ở slide này, chúng ta xem xét vấn đề: {slide_title}. Lựa chọn dữ liệu sai lầm ở bước này sẽ làm sai lệch toàn bộ quy trình.\n'
        text += 'Người 2: Vâng thưa thầy, em đang theo dõi rất kỹ phần này.\n'

if len(titles) < 81:
    text += f'\nSlide {len(titles)+1}: KẾT THÚC\n'
    text += 'Người 1: Vậy là chúng ta đã hoàn thành Chương 4. Kỹ năng lập kế hoạch dữ liệu sẽ là tiền đề vững chắc để các em bước vào phân tích thực sự.\n'
    text += 'Người 2: Dạ vâng, cảm ơn thầy rất nhiều! Em đã hiểu rõ tầm quan trọng của việc "chọn mặt gửi vàng" khi thu thập dữ liệu rồi ạ. Hẹn gặp lại thầy ở chương sau!\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Generated script_chapter04.txt successfully with {len(titles)+1} slides!")
