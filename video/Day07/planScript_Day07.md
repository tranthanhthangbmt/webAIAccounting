# Kế hoạch Kịch bản Bài giảng: Day 07 - AI trong Tự động hóa Kiểm soát Nội bộ & Phát hiện Gian lận

**Tệp đầu vào:** `Slide_AIAcc_Day07.tex` & Textbook "Data and Analytics in the Accounting Profession" (Chương 9).
**Hình thức:** Hội thoại giảng dạy Socratic (Người 1: Giảng viên, Người 2: Sinh viên).
**Mục tiêu:** Giải thích cách Trí tuệ Nhân tạo và Khai phá Quy trình (Process Mining) định hình lại hệ thống Kiểm soát Nội bộ (COSO). Chuyển hóa các khái niệm trừu tượng (Văn hóa doanh nghiệp, Kim cương gian lận) thành các ví dụ có thể đo lường bằng AI.

## Dàn ý Chi tiết (Mapping Slide & Textbook)

### Phần 1: Định hình Kế toán & Lượng hóa Môi trường Kiểm soát (Slide 1 - 16)
- **Bối cảnh Khủng hoảng:** Sự sụp đổ của Thomas Cook, và việc Báo cáo kiểm toán "Sạch" không còn đủ sức bảo vệ doanh nghiệp.
- **Phòng thủ Chủ động:** Ẩn dụ từ phim *Minority Report* - Đánh hơi gian lận trước khi tiền rời đi.
- **Rủi ro Kiểm soát (Khung COSO):** Bài toán khó nhất là làm sao đo lường thứ vô hình như "Môi trường kiểm soát" (Văn hóa doanh nghiệp).
- **Hạn chế của Phiếu khảo sát:** Văn hóa "Báo cáo láo" - cấp dưới chỉ chọn đáp án sếp muốn thấy.
- **Giải pháp AI (NLP):** Dùng NLP để quét email nội bộ, phân tích từ vựng bằng thuật toán TF-IDF để đo lường "Áp lực ngầm" và phong cách quản lý độc đoán. Biến AI thành "Nhiệt kế đạo đức".

### Phần 2: Khai phá Quy trình & Cái bóng Kỹ thuật số (Slide 17 - 27)
- **Chuyển đổi góc nhìn:** Từ Data-Centric (Tìm số tiền mất) sang Metadata-Centric (Tìm lỗ hổng quy trình bằng Siêu dữ liệu).
- **Cái bóng kỹ thuật số (Digital Shadow):** Bám theo dấu vết hệ thống (Ai đăng nhập? IP nào? Mấy giờ?).
- **Vấn đề Bất kiêm nhiệm (Segregation of Duties):** Cách gian lận thực tế khi một người dùng tài khoản cấp dưới để lách luật "2 chữ ký".
- **Case Study (6 Phút Gian Lận):** Process Mining bóc trần sự thật khi 2 tài khoản khác nhau nhưng duyệt tiền trên cùng 1 địa chỉ IP chỉ cách nhau 6 phút.
- **Bài toán Cảnh báo giả (False Positives):** Sự khác biệt giữa Kế toán đăng nhập 2h sáng để khóa sổ (hợp lệ) và đăng nhập 2h sáng để sửa số tài khoản (gian lận). Cần Human-in-the-loop (Chuyên gia dán nhãn cho AI).

### Phần 3: Kim cương Gian lận, Clustering & Rủi ro AI (Slide 28 - 42)
- **Kim cương Gian lận (Fraud Diamond):** Sự bổ sung của yếu tố "Năng lực" (Capability) vào Tam giác Gian lận truyền thống. 
- **Ẩn dụ Cháy nổ:** Áp lực = Chất đốt, Cơ hội = Oxy, Biện minh = Nhiệt độ. Năng lực = Mồi lửa châm ngòi.
- **Quản trị Lợi nhuận (Earnings Management):** Xào xáo số liệu hợp pháp nhưng sai lệch bản chất. NLP phát hiện bằng cách đối chiếu độ tự tin trong Báo cáo cổ đông với sự hoảng loạn trong Email nội bộ.
- **Học Không Giám Sát (Clustering):** Gom cụm để tìm "Unknown Unknowns". Case study 9.999 USD để lách luật (Quy định duyệt thầu 10.000 USD).
- **Đánh giá Chéo Đa chiều:** Hệ thống tự động khóa quyền truy cập của nhân viên có dấu hiệu thù hằn.
- **Rủi ro Tương lai:** Con dao hai lưỡi khi chính hệ thống AI bị thao túng để che giấu các khoản lỗ bằng giao dịch cao tần phi nhân loại. Lời cảnh tỉnh cho nghề Kiểm toán Thuật toán.
