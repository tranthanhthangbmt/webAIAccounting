import re

tex_content = open('d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/slidePractice/Slide_Practice_Ch04.tex', encoding='utf-8').read()
frames = re.findall(r'\\begin\{frame\}(?:\[.*?\])?(?:\{(.*?)\})?', tex_content)
titles = [f if f else 'NO_TITLE' for f in frames]

print(f'Found {len(titles)} frames')

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter04/script_chapter04.txt'
text = '''KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 4
Lập Kế hoạch Dữ liệu và Chiến lược Phân tích

=========================================
Người 1 (Giảng viên): Hướng dẫn, phân tích tư duy chiến lược dữ liệu.
Người 2 (Sinh viên): Tương tác, đặt câu hỏi thực tế (luôn xưng hô là "thầy").
=========================================
'''

for i, title in enumerate(titles):
    text += f'\nSlide {i+1}: {title.upper() if title != "NO_TITLE" else "TRANG BÌA"}\n'
    if i == 0:
        text += 'Người 1: Chào mừng các em đến với Chương 4. Sau khi đã biết cách đặt câu hỏi phân tích, bước tiếp theo sống còn chính là Lập Kế hoạch Dữ liệu. Chúng ta không thể phân tích nếu không có nguyên liệu đầu vào.\n'
        text += 'Người 2: Dạ em chào thầy. Thưa thầy, phần này có giống với việc mình đi siêu thị mua nguyên liệu trước khi nấu ăn không ạ?\n'
    elif i == len(titles) - 1:
        text += 'Người 1: Vậy là chúng ta đã hoàn thành Chương 4. Kỹ năng lập kế hoạch dữ liệu sẽ là tiền đề vững chắc để các em bước vào phân tích thực sự.\n'
        text += 'Người 2: Dạ vâng, cảm ơn thầy rất nhiều! Em đã hiểu rõ tầm quan trọng của việc "chọn mặt gửi vàng" khi thu thập dữ liệu rồi ạ. Hẹn gặp lại thầy ở chương sau!\n'
    elif 'ILLUSTRATION' in title or 'Hình minh họa' in title or 'Apply It' in title or 'PAC' in title or 'BE' in title or 'EX' in title:
        text += 'Người 1: Mời các em quan sát bài tập và hình minh họa trên slide này để thấy rõ cách dữ liệu được cấu trúc trong thực tế.\n'
        text += 'Người 2: Dạ thưa thầy, hình ảnh này giúp em dễ hình dung hơn hẳn ạ.\n'
    else:
        text += f'Người 1: Ở slide này, chúng ta xem xét vấn đề: {title}. Lựa chọn dữ liệu sai lầm ở bước này sẽ làm sai lệch toàn bộ quy trình.\n'
        text += 'Người 2: Vâng thưa thầy, em đang theo dõi rất kỹ phần này.\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done!')
