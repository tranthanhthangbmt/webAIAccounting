# Kế hoạch Xây dựng Slide Bài giảng Buổi 7

## 1. Thông tin chung
- **Học phần:** Trí tuệ Nhân tạo Ứng dụng trong Kế toán (AI in Accounting)
- **Buổi học:** Buổi 7
- **Chủ đề chính:** AI trong Tự động hóa Kiểm soát Nội bộ \& Phát hiện Gian lận
- **Tài liệu nguồn:** `docs/buoi_07.md` (Chương 9 \& Chương 12)
- **Tài liệu bổ trợ:** `TaiLieu/script/audioScript_Day07.txt`
- **Số lượng Slide dự kiến:** ~45 slides
- **Thời lượng:** 3 tiết (135 phút)
- **Kiến trúc:** Beamer LaTeX, Aspect Ratio 16:9, Theme Madrid, tiếng Việt (T5 encoding).

## 2. Mục tiêu Bài giảng
1. Nắm bắt khái niệm tự động hóa kiểm soát nội bộ qua lăng kính của Khung COSO.
2. Hiểu được ứng dụng của NLP trong việc lượng hóa "Môi trường kiểm soát" và "Văn hóa doanh nghiệp".
3. Phân biệt được sự khác nhau giữa dữ liệu giao dịch (Data-centric) và siêu dữ liệu (Metadata-centric) thông qua Khai phá quy trình (Process Mining).
4. Áp dụng Mô hình Kim cương Gian lận (Fraud Diamond) kết hợp với AI (Supervised/Unsupervised Learning) để chặn đứng hành vi sai trái.
5. Nhận thức được rủi ro đạo đức lớn nhất trong tương lai: "Ai sẽ kiểm soát hệ thống AI?".

## 3. Tích hợp Ẩn dụ từ Audio Script
Slide sẽ lồng ghép các câu chuyện/ẩn dụ thực tế nhằm mang lại sự sinh động cho bài giảng:
- **Phim Minority Report:** AI dự đoán và ngăn chặn tội phạm tài chính trước khi cú click chuột cuối cùng được thực hiện.
- **Chiếc nhiệt kế Đạo đức tự động:** Thay vì phát phiếu khảo sát vô hồn, AI dùng NLP (TF-IDF) quét email để "đo" áp lực và văn hóa độc đoán của Sếp.
- **Cái bóng Kỹ thuật số (Digital Shadow):** Process Mining không nhìn vào số tiền, mà nhìn vào cái bóng của giao dịch (ai truy cập, lúc mấy giờ, ở IP nào).
- **Phép ví von Kim cương Gian lận với "Vụ cháy nổ":** Áp lực (Chất đốt), Cơ hội (Oxy), Biện minh (Nhiệt độ) và Năng lực (Mồi lửa châm ngòi).
- **Giao dịch 9.999 USD:** Thuật toán phân cụm (Clustering) bắt thóp chiêu trò lách ngưỡng phê duyệt 10.000 USD.
- **Rủi ro AI Tự trị:** Khủng hoảng xảy ra khi chính AI tự che giấu các khoản lỗ bằng những giao dịch phức tạp để tối ưu hóa lợi nhuận.

## 4. Cấu trúc chi tiết (3 Tiết học - ~45 Slides)

### Tiết 1: Định hình lại Kế toán \& Lượng hóa Môi trường Kiểm soát (Slide 04 - 17)
- **Slide 04 - 05:** Đặt vấn đề: Sự sụp đổ của Thomas Cook, thất bại của kiểm toán truyền thống. 
- **Slide 06 - 08:** AI thay đổi cuộc chơi: Từ Minority Report đến Hệ thống phòng thủ chủ động.
- **Slide 09 - 11:** Nhắc lại Khung COSO (5 thành phần). Tại sao "Môi trường kiểm soát" lại là bài toán khó định lượng nhất? Điểm yếu của Phiếu khảo sát.
- **Slide 12 - 14:** Máy đo nhiệt độ Đạo đức (AI & NLP). Ứng dụng TF-IDF đếm trọng số từ vựng.
- **Slide 15 - 17:** Nhận diện phong cách quản lý (Độc đoán vs Hợp tác). Ví dụ: Quét các câu lệnh "Tôi không cần biết lý do", "Phải xong bằng mọi giá".

### Tiết 2: Khai phá Quy trình (Process Mining) \& Cái bóng Kỹ thuật số (Slide 18 - 32)
- **Slide 18 - 20:** Giới thiệu Process Mining trong thành phần "Hoạt động kiểm soát". Data-centric vs Metadata-centric.
- **Slide 21 - 23:** Cái bóng Kỹ thuật số: Khai thác Log file (Nhật ký hệ thống, IP, Timestamp).
- **Slide 24 - 26:** Case Study Vi phạm Bất kiêm nhiệm (Segregation of Duties): Người tạo vendor ma và người duyệt thanh toán dùng chung 1 địa chỉ IP cách nhau 6 phút.
- **Slide 27 - 29:** Bài toán Cảnh báo giả (False Positives). Đăng nhập 2h sáng để khóa sổ cuối tháng vs 2h sáng để đổi số TK ngân hàng.
- **Slide 30 - 32:** Giải pháp: Kết hợp Process Mining với Học máy (Machine Learning) để dạy AI phân biệt ngữ cảnh, giảm cảnh báo rác.

### Tiết 3: Kim cương Gian lận, Clustering \& Rủi ro AI (Slide 33 - 45)
- **Slide 33 - 34:** Cây Gian lận (Fraud Tree) \& Mô hình Kim cương Gian lận (Fraud Diamond - Bổ sung Capability).
- **Slide 35 - 37:** Ẩn dụ Vụ nổ: Chất đốt, Oxy, Nhiệt độ và Mồi lửa. Dùng AI đánh chặn từng góc.
- **Slide 38 - 40:** Góc Biện minh \& Năng lực: Phát hiện Quản trị Lợi nhuận (Earnings Management) bằng NLP (Đối chiếu giọng điệu email nội bộ và báo cáo ra công chúng).
- **Slide 41 - 42:** Học không giám sát (Clustering): Săn lùng "Unknown Unknowns". Bắt giao dịch lách luật 9.999 USD.
- **Slide 43 - 44:** Suy ngẫm cuối: Con dao hai lưỡi. Khi AI tự tối ưu hóa bằng cách giấu lỗ. "Ai sẽ kiểm toán cỗ máy?".
- **Slide 45:** Tổng kết \& Q/A.

## 5. Danh sách Hình ảnh (Figures) Cần Tích hợp
- Sử dụng các biểu đồ từ `Figures/Buoi_07A/` và `Figures/Buoi_07B/`:
  - `FIGURE 9.1 Automation of Internal Controls Evaluation.jpeg`
  - `FIGURE 9.2 Automated Environment Evaluation.jpeg`
  - Fraud Tree / Fraud Diamond nếu có trong hệ thống thư mục ảnh của Buổi 7.

## 6. Lộ trình Triển khai
1. Nhận phản hồi/phê duyệt từ User cho kế hoạch này.
2. Viết file `build_beamer_day07.py` tạo mã LaTeX với > 40 Slides.
3. Thực thi kịch bản và biên dịch PDF (2 lần để cập nhật TOC).
4. Kiểm thử kết quả, cập nhật Walkthrough.
