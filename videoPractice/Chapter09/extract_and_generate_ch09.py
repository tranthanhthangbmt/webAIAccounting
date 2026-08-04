import re

tex_content = open('d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/slidePractice/Slide_Practice_Ch09.tex', encoding='utf-8').read()
frames = re.findall(r'\\begin\{frame\}(?:\[.*?\])?(?:\{(.*?)\})?', tex_content)
titles = [f if f else 'NO_TITLE' for f in frames]

print(f'Found {len(titles)} frames for Chapter 09')

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter09/script_chapter09.txt'
text = '''KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 9
Trình bày Kết quả Phân tích Dữ liệu (Data Visualization)

=========================================
Người 1 (Giảng viên): Hóa thân thành "Chuyên gia Thuyết trình", hướng dẫn cách kể chuyện bằng dữ liệu và thiết kế Dashboard.
Người 2 (Sinh viên): Hào hứng với biểu đồ đẹp, hỏi về tính thẩm mỹ (luôn xưng hô là "thầy").
=========================================
'''

for i, title in enumerate(titles):
    text += f'\nSlide {i+1}: {title.upper() if title != "NO_TITLE" else "TRANG BÌA"}\n'
    if i == 0:
        text += 'Người 1: Chào mừng các em đến với Chương 9. Đây là phần được mong chờ nhất: Trực quan hóa dữ liệu! Nguyên tắc tối thượng của chương này là: "Đừng bao giờ bắt sếp của em phải suy nghĩ khi nhìn vào biểu đồ".\n'
        text += 'Người 2: Dạ em chào thầy. Thưa thầy, phần này có phải là mình sẽ học cách làm ra các Dashboard báo cáo đẹp lung linh như trên mạng không ạ? Em rất thích phần này!\n'
    elif i == len(titles) - 1:
        text += 'Người 1: Vậy là chúng ta đã kết thúc Chương 9. Các em hãy nhớ, một biểu đồ đẹp không nằm ở chỗ nó có nhiều màu sắc hay hiệu ứng 3D phức tạp, mà nằm ở khả năng truyền đạt thông tin một cách nhanh và chính xác nhất.\n'
        text += 'Người 2: Dạ vâng, hôm nay em đã học được rất nhiều mẹo phối màu và chọn đúng biểu đồ. Cảm ơn thầy rất nhiều ạ! Hẹn gặp lại thầy ở chương cuối cùng!\n'
    elif 'ILLUSTRATION' in title or 'Hình minh họa' in title or 'Apply It' in title or 'PAC' in title or 'BE' in title or 'EX' in title:
        text += 'Người 1: Mời các em quan sát kỹ biểu đồ minh họa trên slide này. Hãy cho thầy biết, biểu đồ này đã tuân thủ đúng nguyên tắc tối giản chưa, hay đang bị "rác thị giác" (chartjunk)?\n'
        text += 'Người 2: Thưa thầy, theo em thì biểu đồ này nên bỏ đi các đường kẻ ngang mờ ở phía sau và không nên dùng hiệu ứng 3D, nhìn sẽ chuyên nghiệp hơn rất nhiều ạ!\n'
    else:
        text += f'Người 1: Ở slide này, chúng ta tiếp tục xem xét quy tắc: {title}. Lựa chọn đúng loại biểu đồ (Bar, Line hay Pie) sẽ quyết định toàn bộ sức mạnh của câu chuyện mà dữ liệu muốn kể.\n'
        text += 'Người 2: Vâng thưa thầy, em đang đối chiếu các quy tắc thiết kế này vào bài tập của mình ạ.\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done generating script_chapter09.txt!')
