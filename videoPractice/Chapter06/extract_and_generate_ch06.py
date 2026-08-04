import re

tex_content = open('d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/slidePractice/Slide_Practice_Ch06.tex', encoding='utf-8').read()
frames = re.findall(r'\\begin\{frame\}(?:\[.*?\])?(?:\{(.*?)\})?', tex_content)
titles = [f if f else 'NO_TITLE' for f in frames]

print(f'Found {len(titles)} frames for Chapter 06')

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter06/script_chapter06.txt'
text = '''KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 6
Mô hình hóa Thông tin (Information Modeling)

=========================================
Người 1 (Giảng viên): Hướng dẫn, phân tích tư duy thiết kế hệ thống cơ sở dữ liệu.
Người 2 (Sinh viên): Tương tác, đặt câu hỏi về sơ đồ ERD (luôn xưng hô là "thầy").
=========================================
'''

for i, title in enumerate(titles):
    text += f'\nSlide {i+1}: {title.upper() if title != "NO_TITLE" else "TRANG BÌA"}\n'
    if i == 0:
        text += 'Người 1: Chào mừng các em đến với Chương 6. Hôm nay, chúng ta sẽ hóa thân thành những "Kiến trúc sư hệ thống" để học cách thiết kế cấu trúc Dữ liệu, hay còn gọi là Mô hình hóa thông tin.\n'
        text += 'Người 2: Dạ em chào thầy. Thưa thầy, phần này có phải là mình sẽ học cách vẽ các sơ đồ kết nối lằng nhằng giống như của dân IT không ạ?\n'
    elif i == len(titles) - 1:
        text += 'Người 1: Vậy là chúng ta đã hoàn thành xuất sắc Chương 6! Mô hình hóa thông tin là một kỹ năng khó nhưng cực kỳ đắt giá, giúp các em không chỉ xài dữ liệu mà còn biết cách "kiến tạo" ra cấu trúc dữ liệu cho công ty.\n'
        text += 'Người 2: Dạ vâng, hôm nay em đã phân biệt được rõ 1:M và M:N rồi ạ. Cảm ơn thầy rất nhiều, hẹn gặp lại thầy ở bài sau!\n'
    elif 'ILLUSTRATION' in title or 'Hình minh họa' in title or 'Apply It' in title or 'PAC' in title or 'BE' in title or 'EX' in title:
        text += 'Người 1: Mời các em quan sát kỹ hình minh họa Sơ đồ Thực thể - Mối quan hệ (ERD) trên slide này. Hãy chú ý đến các Thực thể (Entities) và Bản số (Cardinalities) của chúng.\n'
        text += 'Người 2: Dạ thưa thầy, khi nhìn trực tiếp vào sơ đồ ERD thế này, em dễ hình dung luồng kết nối dữ liệu hơn rất nhiều ạ.\n'
    else:
        text += f'Người 1: Ở slide này, chúng ta xem xét vấn đề: {title}. Đây là quy tắc chuẩn hóa dữ liệu bắt buộc để tránh trùng lặp.\n'
        text += 'Người 2: Vâng thưa thầy, em đang theo dõi và ghi chép rất cẩn thận phần lý thuyết này.\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done generating script_chapter06.txt!')
