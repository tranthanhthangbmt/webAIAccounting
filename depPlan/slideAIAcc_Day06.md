# Kế hoạch Xây dựng Slide Bài giảng Buổi 6

## 1. Thông tin chung
- **Học phần:** Trí tuệ Nhân tạo Ứng dụng trong Kế toán (AI in Accounting)
- **Buổi học:** Buổi 6
- **Chủ đề chính:** AI trong Tài chính Công và Tài chính Quốc tế (Phòng chống Gian lận & Ổn định Tài chính)
- **Tài liệu nguồn:** `docs/buoi_06.md` (Chương 5 & Chương 1 - Scott Dell)
- **Tài liệu bổ trợ:** `TaiLieu/script/audioScript_Day06.txt`
- **Số lượng Slide dự kiến:** ~45 slides
- **Thời lượng:** 3 tiết (135 phút)
- **Kiến trúc:** Beamer LaTeX, Aspect Ratio 16:9, Theme Madrid, tiếng Việt (T5 encoding).

## 2. Mục tiêu Bài giảng
1. Hiểu được sự chuyển dịch mô hình trong kế toán điều tra: từ "bác sĩ pháp y" (tìm nguyên nhân sau khi chết) sang "bác sĩ y tế dự phòng" (chủ động ngăn chặn).
2. Phân biệt được sự khác nhau giữa Học có giám sát, Học không giám sát (Anomaly Detection) và Xử lý ngôn ngữ tự nhiên (NLP) trong việc phát hiện gian lận và thông đồng.
3. Nắm được cách AI được sử dụng trong kiểm soát đấu thầu, phòng chống tham nhũng khu vực công.
4. Hiểu vai trò của AI trong việc duy trì ổn định kinh tế vĩ mô (chống lạm phát, ngăn chặn Bank Run, Stress testing).
5. Xác định được bộ kỹ năng mới của kế toán viên (Critical Thinking, Explainable AI - XAI) trong tương lai.

## 3. Tích hợp Ẩn dụ từ Audio Script
Slide sẽ lồng ghép các câu chuyện/ẩn dụ thực tế để làm mềm hóa kiến thức kỹ thuật:
- **Kế toán thủ công vs AI:** Giống như "Bịt mắt mò kim đáy biển" so với "Vị thám tử không bao giờ ngủ".
- **NLP & Quản trị Lợi nhuận:** Kẻ gian lận dùng "thể bị động" để che đậy làm ăn bết bát. AI quét email tìm văn hóa độc hại ("làm ngay", "tuyệt mật", "gửi lúc nửa đêm") qua mô hình STPCM.
- **Bác sĩ Y tế Dự phòng:** AI chuyển nghề kế toán từ việc làm pháp y (hậu kiểm) sang dự phòng khủng hoảng tài chính.
- **Cuộc chạy đua Vũ trang Thuật toán:** Tội phạm dùng AI tạo sinh để làm giả số liệu, nhưng AI của ta dùng NLP bắt lỗi "văn phong giao tiếp" phi logic.
- **Phi công lái Siêu phi cơ AI:** Kế toán viên không bị đào thải mà tiến hóa thành phi công điều khiển AI (cần Explainable AI - XAI để dịch hộp đen ra ngôn ngữ kinh doanh minh bạch).
- **Câu hỏi Đạo đức Vĩ mô:** Có nên để AI tự động điều hành lãi suất ngân hàng thay con người? Đánh đổi giữa hiệu suất tuyệt đối và quyền kiểm soát.

## 4. Cấu trúc chi tiết (3 Tiết học)

### Tiết 1: Kế toán Điều tra & Các công nghệ Cốt lõi (Slide 04 - 17)
- **Slide 04 - 06:** Đặt vấn đề: Sự bế tắc của Kế toán truyền thống. Ẩn dụ "Bịt mắt mò kim đáy biển" vs "Thám tử không bao giờ ngủ".
- **Slide 07 - 09:** Bảng so sánh 5 tiêu chí: Chọn mẫu (5%) vs Quét toàn bộ (100%), Độ trễ vs Real-time, Cảnh báo giả (False Positives).
- **Slide 10 - 11:** Các công nghệ AI cốt lõi: Học có giám sát (biết trước quy luật) vs Học không giám sát (Tìm "Unknown Unknowns" - Các bất thường chưa có tiền lệ).
- **Slide 12 - 14:** Công nghệ NLP (Xử lý ngôn ngữ tự nhiên) trong kế toán. Ví dụ: Dùng "thể bị động" che đậy lợi nhuận giảm; Phát hiện thao túng qua văn bản.
- **Slide 15 - 17:** Các Case Study Doanh nghiệp: (1) Thẻ tín dụng, (2) Nhân viên ma (Payroll Fraud), (3) Hồ sơ bồi thường bảo hiểm giả mạo bằng công nghệ chỉnh ảnh.

### Tiết 2: Chống Tham nhũng Công & Cuộc đua Thuật toán (Slide 18 - 32)
- **Slide 18 - 20:** Khu vực công: Nhạy cảm và phức tạp. Bối cảnh Case Study 4 (Chống tham nhũng Đấu thầu).
- **Slide 21 - 23:** Phân tích Đồ thị (Graph Analytics) phát hiện Mạng lưới thông đồng. Tỷ lệ sát giá dự toán & Quy luật trúng thầu luân phiên để ăn hoa hồng (Kickbacks).
- **Slide 24 - 26:** Khung STPCM. Đặc biệt: Đánh giá Rủi ro Văn hóa và Thái độ. Quét tin nhắn nội bộ: "Tuyệt mật", "Gửi lúc nửa đêm" là mầm mống gian lận.
- **Slide 27 - 29:** Cuộc chạy đua Vũ trang Thuật toán: Tội phạm dùng AI làm giả số liệu sổ sách cực kỳ hoàn hảo.
- **Slide 30 - 32:** Giải pháp chống trả: Kết hợp chéo Machine Learning và NLP. (Rất khó dùng AI để làm giả chuỗi logic giao tiếp email của con người trong thời gian dài).

### Tiết 3: Ổn định Tài chính Vĩ mô \& Kỷ nguyên Kế toán Mới (Slide 33 - 45)
- **Slide 33 - 34:** Sự chuyển dịch vĩ đại: Từ "Bác sĩ pháp y" (kiểm tra hậu kỳ) sang "Bác sĩ y tế dự phòng" (Ngăn chặn trước khủng hoảng).
- **Slide 35 - 37:** AI trong Ổn định Tài chính: Rút tiền ồ ạt qua App (Bank Run), Stress Testing (Mô phỏng đứt gãy chuỗi cung ứng & Lạm phát).
- **Slide 38 - 40:** Tương lai của nghề Kế toán: Không bị thay thế, nhưng phải tiến hóa. Trở thành "Phi công điều khiển siêu phi cơ AI".
- **Slide 41 - 43:** Kỹ năng sinh tồn: Tư duy phản biện (AI chỉ là xác suất) \& Explainable AI (XAI - Trách nhiệm giải trình hộp đen). Nếu máy từ chối khoản vay, kế toán phải giải thích được tại sao!
- **Slide 44 - 45:** Suy ngẫm cuối: Liệu một ngày AI có nên được cấp quyền "tự động tăng/giảm lãi suất vĩ mô"? Ranh giới giữa sự tối ưu tuyệt đối và quyền kiểm soát của nhân loại.

## 5. Danh sách Hình ảnh (Figures) Cần Tích hợp
*(Lưu ý: Dựa trên `docs/buoi_06.md`, một số hình ảnh từ `Figures/Buoi_02B` có thể được tái sử dụng để làm rõ các khái niệm về Vòng đời khoa học dữ liệu và Học máy nếu phù hợp với ngữ cảnh)*:
- Tái sử dụng `../Figures/Buoi_02B/Figure 6.4 Data science project lifecycle.jpeg` (Cho quy trình huấn luyện liên tục của AI chống gian lận).
- Có thể sử dụng bảng biểu (Tables) trực tiếp trong LaTeX để hiển thị các khung năng lực.

## 6. Lộ trình Triển khai
1. Nhận phản hồi/phê duyệt từ User cho kế hoạch này.
2. Viết file `build_beamer_day06.py` tự động sinh mã LaTeX 16:9 Madrid.
3. Thực thi script, biên dịch qua `pdflatex` 2 lần.
4. Kiểm thử kết quả PDF, báo cáo và cập nhật Walkthrough.
