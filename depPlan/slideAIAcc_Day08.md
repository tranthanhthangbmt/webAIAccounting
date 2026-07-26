# Kế hoạch Xây dựng Slide Bài giảng Buổi 8

## 1. Thông tin chung
- **Học phần:** Trí tuệ Nhân tạo Ứng dụng trong Kế toán (AI in Accounting)
- **Buổi học:** Buổi 8
- **Chủ đề chính:** AI trong Tài chính Ngân hàng và Thị trường Chứng khoán (Chấm điểm Tín dụng \& Giao dịch Thuật toán)
- **Tài liệu nguồn:** `docs/buoi_08.md` (Chương 4 \& Chương 6)
- **Tài liệu bổ trợ:** `TaiLieu/script/audioScript_Day08.txt`
- **Số lượng Slide dự kiến:** ~45 slides
- **Thời lượng:** 3 tiết (135 phút)
- **Kiến trúc:** Beamer LaTeX, Aspect Ratio 16:9, Theme Madrid, tiếng Việt (T5 encoding).

## 2. Mục tiêu Bài giảng
1. Nhận diện các hình thức gian lận trong Thương mại điện tử (Click Fraud, Credit Card Fraud, Document Fraud) và giải pháp phòng chống bằng học máy.
2. Hiểu được khái niệm "Dương tính giả" (False Positives) trong chấm điểm tín dụng và cách AI điều chỉnh trọng số linh hoạt (Baseline).
3. Đánh giá rủi ro của "Hộp đen" AI trong Giao dịch Thuật toán (Algorithmic Trading) qua sự kiện Flash Crash 2010.
4. Phân tích cuộc chiến Chống độc quyền (Antitrust) trong kỷ nguyên Big Tech: Hiệu ứng mạng, Sáp nhập tiêu diệt (Killer Acquisitions), và cái bẫy "Phúc lợi người tiêu dùng".
5. Mở rộng tư duy về vai trò của con người trong tương lai khi có sự xuất hiện của "Thẩm phán máy móc".

## 3. Tích hợp Ẩn dụ từ Audio Script
Slide sẽ lồng ghép các câu chuyện/ẩn dụ thực tế nhằm mang lại sự sinh động cho bài giảng:
- **Ẩn dụ Lượt nhấp ảo (Click Fraud):** Thuê hàng ngàn người giả vờ vào cửa hàng để làm mòn thảm, xài hao điện $\Rightarrow$ Cạn kiệt ngân sách quảng cáo.
- **Rừng ngẫu nhiên (Random Forest):** Trò chơi 20 câu hỏi nhanh như chớp. Cú di chuột tạo thành đường thẳng hoàn hảo đến mức phi tự nhiên (Bot vs Người thật).
- **Dương tính giả (False Positives):** Thảm họa bị khóa thẻ khi quẹt thẻ khách sạn ở Paris lúc 2h sáng do AI quá nhạy cảm. Cách mạng Nơ-ron tự động cập nhật "Đường cơ sở" (Baseline) nếu khách đã mua vé máy bay trước đó.
- **Dâu ông nọ cắm cằm bà kia:** Hóa đơn vật liệu xây dựng mang cấu trúc hành văn của... hóa đơn y tế (Phát hiện bằng OCR + NLP).
- **Flash Crash 2010:** Thị trường bốc hơi hàng nghìn điểm chỉ trong vài phút vì thuật toán tự chơi với thuật toán.
- **Vừa đá bóng vừa thổi còi:** Sàn giao dịch cấp công cụ AI cho người dùng nhưng lại thao túng để ưu tiên sàn. "Pump and Dump" (Bơm và xả) trong Crypto.
- **Đội bóng siêu giàu mua tiền đạo:** Chiến thuật Sáp nhập tiêu diệt (Killer Acquisitions) của Big Tech. Mua nhân tài giỏi nhất chỉ để cất ghế dự bị.
- **Lá chắn Quyền riêng tư:** Big Tech dùng "Quyền riêng tư" làm vỏ bọc để độc quyền dữ liệu (Vụ hiQ kiện LinkedIn).

## 4. Cấu trúc chi tiết (3 Tiết học - ~45 Slides)

### Tiết 1: Cuộc chiến Không gian Số \& Gian lận TMĐT (Slide 04 - 17)
- **Slide 04 - 05:** Đặt vấn đề: Thị trường chứng khoán đột ngột bốc hơi ngàn điểm vì cỗ máy hộp đen bí ẩn. AI: Từ Tấm khiên phòng thủ đến Vũ khí tấn công.
- **Slide 06 - 08:** Gian lận nhấp chuột (Click Fraud): Ẩn dụ khách hàng ảo làm mòn thảm. Nông trại nhấp chuột (Click farms).
- **Slide 09 - 11:** Nhận diện Bot vs Người: Sự hoàn hảo phi tự nhiên. AI sử dụng Cây quyết định (Decision Tree).
- **Slide 12 - 14:** Rừng ngẫu nhiên (Random Forest): Chặn đứng cú nhấp mờ ám (Giờ giấc, IP, Tốc độ chuột).
- **Slide 15 - 17:** Gian lận quản lý thẻ tín dụng (Credit Card Fraud): Xác lập Đường cơ sở (Baseline) từ thói quen cá nhân thay vì truy tìm kẻ xấu.

### Tiết 2: Dương tính giả, OCR + NLP \& Flash Crash (Slide 18 - 32)
- **Slide 18 - 20:** Bài toán hóc búa: Dương tính giả (False Positives) - Nỗi ác mộng bị khóa thẻ oan ở nước ngoài.
- **Slide 21 - 23:** Cân bằng trọng số của Mạng Nơ-ron (Neural Network). Khả năng hiểu bối cảnh (Ví dụ đã mua vé đi Pháp trước đó).
- **Slide 24 - 26:** Làm giả Chứng từ (Document Dispensation): Từng pixel hoàn hảo.
- **Slide 27 - 29:** Kết hợp OCR + NLP: Khi hóa đơn Xây dựng mang văn phong Y tế. Sự bất nhất về cấu trúc ngôn từ (Dấu vân tay giả mạo). Nguyên tắc Human-in-the-loop (Máy lọc, người chốt).
- **Slide 30 - 32:** Đổi vai: Từ Phòng thủ sang Tấn công. Giao dịch Thuật toán (Algorithmic Trading). Sự kiện Flash Crash 2010.

### Tiết 3: Big Tech, Chống độc quyền \& Thẩm phán Máy móc (Slide 33 - 45)
- **Slide 33 - 35:** Vấn đề đạo đức Fintech: Vừa đá bóng vừa thổi còi (Ví dụ Paytm/Zerodha).
- **Slide 36 - 37:** Crypto \& Bơm xả (Pump and Dump): Dùng Discord, Telegram. Học máy quét dòng tiền và ngôn ngữ để ngăn chặn.
- **Slide 38 - 39:** Sự trỗi dậy của Gatekeepers (Người gác cổng). Hiệu ứng mạng (Network Effects).
- **Slide 40 - 41:** Sáp nhập Tiêu diệt (Killer Acquisitions): Đội bóng giàu mua tiền đạo cất ghế dự bị.
- **Slide 42 - 43:** Lá chắn Quyền riêng tư (Vụ LinkedIn) \& Cái bẫy "Phúc lợi Người tiêu dùng" (Khi khách hàng chính là sản phẩm). Phong trào Right to Repair.
- **Slide 44:** Suy ngẫm viễn cảnh: Thẩm phán máy móc (Không cảm xúc). Vai trò của Kế toán/Kiểm toán viên ở đâu?
- **Slide 45:** Tổng kết \& Q/A.

## 5. Lộ trình Triển khai
1. Nhận phản hồi/phê duyệt từ User cho kế hoạch này.
2. Viết file `build_beamer_day08.py` tạo mã LaTeX với ~45 Slides.
3. Thực thi kịch bản và biên dịch PDF.
4. Kiểm thử kết quả, cập nhật Walkthrough.
