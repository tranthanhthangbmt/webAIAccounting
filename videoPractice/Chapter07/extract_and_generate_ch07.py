import re

tex_content = open('d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/slidePractice/Slide_Practice_Ch07.tex', encoding='utf-8').read()
frames = re.findall(r'\\begin\{frame\}(?:\[.*?\])?(?:\{(.*?)\})?', tex_content)
titles = [f if f else 'NO_TITLE' for f in frames]

print(f'Found {len(titles)} frames for Chapter 07')

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter07/script_chapter07.txt'
text = '''KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 7
Khám phá Dữ liệu (Data Exploration)

=========================================
Người 1 (Giảng viên): Hóa thân thành "thám tử dữ liệu", khơi gợi sinh viên tìm kiếm ngoại lai (outliers) và xu hướng.
Người 2 (Sinh viên): Tương tác, đặt câu hỏi ngạc nhiên (luôn xưng hô là "thầy").
=========================================
'''

for i, title in enumerate(titles):
    text += f'\nSlide {i+1}: {title.upper() if title != "NO_TITLE" else "TRANG BÌA"}\n'
    if i == 0:
        text += 'Người 1: Chào mừng các em đến với Chương 7. Hôm nay, thầy trò chúng ta sẽ đóng vai những "thám tử dữ liệu". Sau khi làm sạch số liệu ở chương trước, giờ là lúc chúng ta quan sát, "đánh hơi" để tìm ra những sự thật đang ẩn giấu.\n'
        text += 'Người 2: Dạ em chào thầy. Thưa thầy, nghe như kiểu mình đang đi tìm thủ phạm trong phim hình sự vậy, em hào hứng quá ạ!\n'
    elif i == len(titles) - 1:
        text += 'Người 1: Vậy là chúng ta đã kết thúc Chương 7! Khám phá dữ liệu là bước đệm tuyệt vời để các em có cảm giác với con số trước khi chạy bất kỳ mô hình phân tích phức tạp nào.\n'
        text += 'Người 2: Dạ vâng, hôm nay em đã biết cách nhìn Histogram và Boxplot để "bắt tẩy" các điểm dị biệt rồi ạ. Cảm ơn thầy rất nhiều, hẹn gặp lại thầy ở bài sau!\n'
    elif 'ILLUSTRATION' in title or 'Hình minh họa' in title or 'Apply It' in title or 'PAC' in title or 'BE' in title or 'EX' in title:
        text += 'Người 1: Nhìn vào biểu đồ/bài tập này, các em có thấy điểm gì bất thường không? Hãy chú ý đến những điểm chấm nằm tách biệt hoàn toàn so với phần còn lại.\n'
        text += 'Người 2: Thưa thầy, có phải cái điểm nằm tít trên cao kia chính là một giao dịch ngoại lai (outlier) không ạ?\n'
    else:
        text += f'Người 1: Ở slide này, chúng ta xem xét vấn đề: {title}. Đây là kỹ thuật giúp chúng ta hiểu rõ bản chất phân phối của dữ liệu.\n'
        text += 'Người 2: Vâng thưa thầy, em đang theo dõi và đối chiếu xem tại sao Trung bình lại lệch so với Trung vị ạ.\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done generating script_chapter07.txt!')
