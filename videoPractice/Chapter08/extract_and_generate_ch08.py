import re

tex_content = open('d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/slidePractice/Slide_Practice_Ch08.tex', encoding='utf-8').read()
frames = re.findall(r'\\begin\{frame\}(?:\[.*?\])?(?:\{(.*?)\})?', tex_content)
titles = [f if f else 'NO_TITLE' for f in frames]

print(f'Found {len(titles)} frames for Chapter 08')

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter08/script_chapter08.txt'
text = '''KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 8
Diễn giải Kết quả Phân tích Dữ liệu (Interpreting Data Analysis Results)

=========================================
Người 1 (Giảng viên): Hóa thân thành "Cố vấn chiến lược", hướng dẫn cách đọc các chỉ số thống kê và dịch thành ngôn ngữ kinh doanh.
Người 2 (Sinh viên): Tương tác, đặt câu hỏi ngây ngô dễ mắc bẫy (luôn xưng hô là "thầy").
=========================================
'''

for i, title in enumerate(titles):
    text += f'\nSlide {i+1}: {title.upper() if title != "NO_TITLE" else "TRANG BÌA"}\n'
    if i == 0:
        text += 'Người 1: Chào mừng các em đến với Chương 8. Nếu máy tính giúp chúng ta Phân tích, thì con người chúng ta phải làm nhiệm vụ Diễn giải. Đây là lúc các em không còn là những người đếm số (number-crunchers) nữa, mà trở thành những nhà cố vấn chiến lược!\n'
        text += 'Người 2: Dạ em chào thầy. Thưa thầy, phần này có phải là mình sẽ học cách "dịch" mấy con số phức tạp ra cho sếp hiểu không ạ?\n'
    elif i == len(titles) - 1:
        text += 'Người 1: Vậy là chúng ta đã hoàn thành Chương 8. Xin chúc mừng, các em đã biết cách tránh cái bẫy chết người "Tương quan là Nhân quả", và biết cách đánh giá một mô hình phân tích có thực sự hữu ích hay không.\n'
        text += 'Người 2: Dạ vâng, hôm nay em mới biết là không thể mang con số P-value thô cứng đi báo cáo sếp được. Cảm ơn thầy rất nhiều ạ! Hẹn gặp lại thầy ở chương sau!\n'
    elif 'ILLUSTRATION' in title or 'Hình minh họa' in title or 'Apply It' in title or 'PAC' in title or 'BE' in title or 'EX' in title:
        text += 'Người 1: Nhìn vào kết quả báo cáo thống kê này, các em thấy chỉ số P-value và R-squared đang nói lên điều gì? Chúng ta có nên tin tưởng vào mô hình này không?\n'
        text += 'Người 2: Thưa thầy, nếu chỉ nhìn thoáng qua thì có vẻ tốt, nhưng đối chiếu với thực tế kinh doanh thì có vẻ chúng ta đang bỏ sót một biến số ngoại sinh nào đó ạ!\n'
    else:
        text += f'Người 1: Ở slide này, chúng ta tiếp tục đi sâu vào khái niệm: {title}. Hãy luôn nhớ bẫy lớn nhất trong dữ liệu: Hai biến số tăng cùng nhau không có nghĩa là cái này gây ra cái kia (Correlation is not Causation).\n'
        text += 'Người 2: Vâng thưa thầy, em đã ghi chú đậm dòng chữ này vào sổ tay rồi ạ.\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done generating script_chapter08.txt!')
