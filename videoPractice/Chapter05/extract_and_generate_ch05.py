import re

tex_content = open('d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/slidePractice/Slide_Practice_Ch05.tex', encoding='utf-8').read()
frames = re.findall(r'\\begin\{frame\}(?:\[.*?\])?(?:\{(.*?)\})?', tex_content)
titles = [f if f else 'NO_TITLE' for f in frames]

print(f'Found {len(titles)} frames for Chapter 05')

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter05/script_chapter05.txt'
text = '''KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 5
Chuẩn bị Dữ liệu (Data Preparation)

=========================================
Người 1 (Giảng viên): Hướng dẫn thực hành làm sạch, chuẩn hóa dữ liệu.
Người 2 (Sinh viên): Tương tác, đặt câu hỏi về các lỗi (luôn xưng hô là "thầy").
=========================================
'''

for i, title in enumerate(titles):
    text += f'\nSlide {i+1}: {title.upper() if title != "NO_TITLE" else "TRANG BÌA"}\n'
    if i == 0:
        text += 'Người 1: Chào mừng các em đến với Chương 5. Đây là phần "đổ mồ hôi" nhất nhưng lại quan trọng nhất của phân tích dữ liệu: Chuẩn bị và Làm sạch Dữ liệu. Quá trình này thường chiếm đến 80% thời gian của một dự án.\n'
        text += 'Người 2: Dạ em chào thầy. Thưa thầy, tại sao lại mất nhiều thời gian đến vậy ạ? Chẳng phải dữ liệu từ hệ thống xuất ra là dùng được luôn sao thầy?\n'
    elif i == len(titles) - 1:
        text += 'Người 1: Vậy là chúng ta đã kết thúc Chương 5. Làm sạch dữ liệu là một công việc đòi hỏi sự tỉ mỉ, kiên nhẫn và đôi khi khá "nhàm chán". Nhưng nhớ kỹ, dữ liệu sạch là nền tảng của mọi quyết định kinh doanh đúng đắn.\n'
        text += 'Người 2: Dạ vâng, bài học hôm nay rất thực tế. Cảm ơn thầy rất nhiều! Em sẽ mở file bài tập ra để thực hành xử lý các lỗi dữ liệu ngay ạ. Hẹn gặp lại thầy ở chương sau!\n'
    elif 'ILLUSTRATION' in title or 'Hình minh họa' in title or 'Apply It' in title or 'PAC' in title or 'BE' in title or 'EX' in title:
        text += 'Người 1: Mời các em quan sát kỹ hình minh họa và tình huống trên slide này. Hãy chú ý cách dữ liệu bị lỗi và cách chúng ta áp dụng các hàm để làm sạch nó.\n'
        text += 'Người 2: Dạ thưa thầy, khi nhìn trực tiếp vào cấu trúc lỗi như thế này, em dễ hình dung cách xử lý hơn hẳn ạ.\n'
    else:
        text += f'Người 1: Ở slide này, chúng ta xem xét kỹ năng: {title}. Nếu bỏ qua bước xử lý lỗi này, toàn bộ kết quả phân tích phía sau sẽ bị sai lệch hoàn toàn.\n'
        text += 'Người 2: Vâng thưa thầy, em đang theo dõi và ghi chép rất cẩn thận phần này.\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done generating script_chapter05.txt!')
