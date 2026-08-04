import re

tex_content = open('d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/slidePractice/Slide_Practice_Ch10.tex', encoding='utf-8').read()
frames = re.findall(r'\\begin\{frame\}(?:\[.*?\])?(?:\{(.*?)\})?', tex_content)
titles = [f if f else 'NO_TITLE' for f in frames]

print(f'Found {len(titles)} frames for Chapter 10')

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter10/script_chapter10.txt'
text = '''KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 10
Các Xu hướng Dữ liệu và Phân tích Mới nhất trong Kế toán (Latest Trends in Accounting Data and Analytics)

=========================================
Người 1 (Giảng viên): Đóng vai "Người truyền cảm hứng" (Mentor), định hướng tương lai nghề nghiệp.
Người 2 (Sinh viên): Vừa lo lắng vừa háo hức về tương lai, luôn tôn trọng (luôn xưng hô là "thầy").
=========================================
'''

for i, title in enumerate(titles):
    text += f'\nSlide {i+1}: {title.upper() if title != "NO_TITLE" else "TRANG BÌA"}\n'
    if i == 0:
        text += 'Người 1: Chào mừng các em đến với Chương 10 - chương cuối cùng của hành trình! Hôm nay chúng ta không chỉ nói về kỹ thuật, mà sẽ nói về TƯƠNG LAI. Kỷ nguyên của AI, RPA và Blockchain đang gõ cửa ngành Kế toán.\n'
        text += 'Người 2: Dạ em chào thầy. Thưa thầy, em vừa háo hức vừa hơi lo sợ. Liệu robot có thay thế hoàn toàn công việc của kế toán viên tụi em trong tương lai không ạ?\n'
    elif i == len(titles) - 1:
        text += 'Người 1: Vậy là chúng ta đã kết thúc Chương 10 và toàn bộ khóa học! Các em hãy luôn nhớ câu nói này của thầy: "AI không cướp việc của kế toán viên, nhưng người kế toán biết dùng AI sẽ cướp việc của người không biết dùng". Hãy luôn học hỏi và tiến về phía trước!\n'
        text += 'Người 2: Dạ vâng! Câu nói của thầy đã truyền cho em một động lực rất lớn. Giờ thì em đã hoàn toàn tự tin ứng dụng AI vào công việc kế toán rồi ạ. Em cảm ơn thầy vì một khóa học tuyệt vời!\n'
    elif 'ILLUSTRATION' in title or 'Hình minh họa' in title or 'Apply It' in title or 'PAC' in title or 'BE' in title or 'EX' in title:
        text += 'Người 1: Nhìn vào bức tranh/tình huống trên slide này, các em thấy hệ thống đang tự động hóa quy trình như thế nào? Đây chính là sức mạnh của RPA đấy.\n'
        text += 'Người 2: Thưa thầy, nhìn cách máy móc tự đối chiếu hóa đơn mà em thấy "sốc" luôn ạ. Vậy phần việc còn lại của chúng ta sẽ chuyển sang kiểm duyệt và phân tích đúng không thầy?\n'
    else:
        text += f'Người 1: Ở slide này, chúng ta bàn về khái niệm cốt lõi: {title}. Công nghệ này sinh ra là để làm công cụ đắc lực cho các em, giải phóng các em khỏi những công việc lặp đi lặp lại.\n'
        text += 'Người 2: Vâng thưa thầy, em đã hiểu rõ bản chất công cụ này rồi ạ. Em đang ghi chép lại các từ khóa quan trọng.\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done generating script_chapter10.txt!')
