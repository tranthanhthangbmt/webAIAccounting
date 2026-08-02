# Kế hoạch Kịch bản Bài giảng: Day 01 - Trí tuệ Nhân tạo cho Kế toán (AI in Accounting)

**Tệp đầu vào:** `Slide_AIAcc_Day01.tex` & Textbook "Data and Analytics in the Accounting Profession"
**Hình thức:** Hội thoại giảng dạy Socratic (Giảng viên gợi mở, Sinh viên phản biện).
**Mục tiêu:** Chuyển đổi các định nghĩa kỹ thuật thành ngôn ngữ nói tự nhiên, dễ hiểu cho Text-to-Speech; tích hợp case-study kế toán thực tế.

## Dàn ý Chi tiết (Mapping Slide & Textbook)

### Phần 1: Khởi động & Sự Chuyển dịch Vai trò của Kế toán (Slide 1 - 14)
- **Bối cảnh:** Dữ liệu phi cấu trúc bùng nổ, bảng tính Excel truyền thống chạm ngưỡng giới hạn. (Map với Textbook: Vai trò của dữ liệu trong nghề kế toán).
- **Phân tích AI vs. Con người:** Giảng viên đặt câu hỏi gợi mở về giới hạn của máy tính so với trực giác của con người (Socratic).
- **Tiến trình lịch sử:** Sinh viên thắc mắc về các "Mùa đông AI". Giảng viên giải thích nguyên nhân quá khứ (thiếu phần cứng/dữ liệu) và lý giải vì sao nay đã khác nhờ Cloud và e-Invoice.
- **Thực tiễn (Case study 1):** Sự dịch chuyển từ Kiểm toán định kỳ (Periodic Auditing) sang Kiểm toán liên tục (Continuous Auditing). Giới thiệu tự động hóa hóa đơn, đối chiếu ngân hàng.

### Phần 2: Hệ sinh thái AI Cốt lõi & Học máy trong Tài chính (Slide 15 - 31)
- **ANI vs AGI:** Phân biệt AI hẹp (nhận diện ảnh, chatbot thuế) và AI tổng quát. Sinh viên đặt câu hỏi về đạo đức (Nếu AI làm sai, ai đền bù?).
- **Từ Lập luận máy (Machine Reasoning) đến Học máy (Machine Learning):**
    - *Hệ chuyên gia (Expert Systems):* Ví dụ kiểm tra thuế bằng quy tắc IF-THEN (Luật thuế TNDN).
    - *Sự chuyển đổi (Machine Learning):* Không cần viết IF-THEN nữa, máy tự tìm quy luật. **(Kỹ năng: Chuyển hóa phương trình học máy thành ngôn ngữ nói: "Nạp dữ liệu hóa đơn + nhãn gian lận -> Máy tự đúc kết ra bộ lọc toán học").**
- **4 Mô hình Học máy (Kèm ví dụ nghiệp vụ Bắt buộc):**
    - *Supervised Learning:* Phát hiện gian lận hóa đơn (Fraud Detection), Chấm điểm tín dụng.
    - *Unsupervised Learning:* Tìm điểm dị biệt (Anomaly Detection) như bút toán ghi sổ lúc 3h sáng Chủ Nhật.
    - *Semi-supervised:* Tiết kiệm 80% công sức dán nhãn chứng từ.
    - *Reinforcement Learning:* Học qua thử/sai -> Quản trị dòng tiền động (Dynamic Cash Management).
- **Deep Learning (Học sâu):** Xử lý hình ảnh hóa đơn nhàu nát, file ghi âm.

### Phần 3: NLP, Khai phá Dữ liệu, RPA & API (Slide 32 - 43)
- **Tự động hóa thông minh (IDP & NLP):**
    - Sinh viên thắc mắc: Làm sao máy đọc được hợp đồng dài ngoằng?
    - Giảng viên giải thích NLP biến chữ thành "vectơ số học", từ đó "hiểu" ngữ cảnh.
    - *Case study 2:* Phân tích Hợp đồng thuê tài sản (IFRS 16).
- **Khai phá dữ liệu (Data Mining):** Tìm quy luật từ Big Data (Khai phá văn bản Báo cáo thường niên để dự báo giá cổ phiếu).
- **Tiến hóa RPA (Từ "Robot mù" đến AI-RPA):**
    - *Case study 3:* Quy trình đối chiếu 3 bên (3-Way Matching: Hóa đơn - Đơn mua hàng - Phiếu nhập kho). API truyền dữ liệu thẳng lên Cổng Thuế.

### Phần 4: Công cụ Lập trình & Lộ trình Thăng tiến (Slide 44 - 46)
- **Tại sao lại là Python & SQL?:** Giảng viên giải thích ưu điểm của Python (dễ đọc như tiếng Anh, thư viện Pandas xử lý nghìn file Excel trong nháy mắt).
- **Kết luận:** Kế toán viên biết dùng AI sẽ thay thế kế toán viên truyền thống. Giao nhiệm vụ cho buổi học tiếp theo.
