# KẾ HOẠCH SLIDE LÝ THUYẾT - DAY 1 (BUỔI 1)
**Tên bài:** TỔNG QUAN ỨNG DỤNG AI VÀ HỆ THỐNG THÔNG TIN TRONG KẾ TOÁN
**Định hướng:** Kế toán thực hành, No-code, góc nhìn người làm nghiệp vụ.

**ĐỀ XUẤT NGUỒN ẢNH MINH HỌA:**
1. **Lấy từ file DOCX (Sách gốc):** Do bản chất file `.docx` là một tệp nén ZIP, ta có thể dùng Python giải nén thư mục `word/media` để lấy toàn bộ biểu đồ, sơ đồ học thuật (như Sơ đồ AIS, Value Chain) giữ nguyên chất lượng gốc. Em có thể viết script tự động trích xuất toàn bộ ảnh này vào thư mục `images/Day_01/`.
2. **Sinh ảnh bằng AI / Dùng Vector (Bổ sung):** Đối với các slide khái niệm trừu tượng (như "Thiên nga đen", "Kế toán viên hiện đại"), em sẽ tạo mô tả lệnh (Prompt) để ta có thể dùng AI tạo ra các hình minh họa vector phong cách phẳng (Flat design) hoặc 3D giúp slide bớt khô khan hơn sách.

---

# PHẦN 1: GIỚI THIỆU & NỀN TẢNG HỆ THỐNG THÔNG TIN KẾ TOÁN (AIS)

## TRANG BÌA (Title Page)
- Tiêu đề chính: Trí tuệ Nhân tạo cho Kế toán
- Tiêu đề phụ: Buổi 1: Tổng quan Ứng dụng AI trong Kế toán
- Tác giả: Đại học Đông Á
- *(🖼️ Ảnh minh họa: Hình nền Abstract về công nghệ, kết nối dữ liệu tài chính - Lấy từ thư viện Vector/AI).*

## NỘI DUNG CHƯƠNG TRÌNH (Table of Contents)
- 1. Nền tảng Hệ thống Thông tin Kế toán (AIS)
- 2. Sự tiến hóa của Nghề Kế toán & Trí tuệ Nhân tạo
- 3. Ứng dụng Thực tiễn của AI trong Chu trình Kế toán
- 4. Tương lai với Generative AI (ChatGPT)

## Năng lực đạt được sau buổi học
- **Về Lý thuyết (LT):** Nắm vững nền tảng Hệ thống Thông tin Kế toán (AIS); Phân biệt rõ sự khác nhau giữa AI, Machine Learning và Deep Learning trong bối cảnh kế toán tài chính.
- **Về Thực hành (TH):** Có khả năng sử dụng các Generative AI (ChatGPT, Copilot, Gemini) để đóng vai (Role-play) hỗ trợ giải đáp các chuẩn mực kế toán cơ bản.
- **Về Tư duy nghề nghiệp:** Chấp nhận và thích nghi với sự thay đổi của nghề kế toán trong kỷ nguyên AI; Nhận thức AI là công cụ hỗ trợ (Copilot), không phải mối đe dọa thay thế hoàn toàn kế toán viên.

## Mở đầu - Câu chuyện kinh doanh (Case Study: S&S)
- Ví dụ thực tế về việc mở doanh nghiệp S&S. Các quyết định cần đưa ra: Định giá sản phẩm, quản lý dòng tiền, thuê nhân viên...
- *(🖼️ Ảnh minh họa: Ảnh chụp cửa hàng bán lẻ hoặc sơ đồ dòng tiền của S&S - Trích xuất từ DOCX Chapter 1 AIS).*

## Hệ thống (System) là gì?
- Định nghĩa: Tập hợp các phương pháp, quy trình để thực hiện một mục tiêu.
- Khái niệm Hệ thống con (Subsystem) và sự tương tác.
- Mục tiêu đồng nhất (Goal congruence) vs Xung đột mục tiêu (Goal conflict).
- *(🖼️ Ảnh minh họa: Sơ đồ bánh răng hoặc cấu trúc phân tầng Hệ thống lớn -> Hệ thống con).*

## Dữ liệu (Data) vs. Thông tin (Information)
- **Dữ liệu:** Các sự kiện thô được thu thập (VD: hóa đơn, số tiền).
- **Thông tin:** Dữ liệu đã được tổ chức, xử lý mang lại ý nghĩa (VD: Báo cáo doanh thu).
- *(🖼️ Ảnh minh họa: Biểu đồ chuyển đổi từ Data (Các khối lộn xộn) -> Processing -> Information (Biểu đồ, báo cáo) - Lấy từ DOCX Chapter 1 AIS).*

**SLIDE 7 & 8: 7 Đặc tính của Thông tin hữu ích**
- 1. Phù hợp 2. Đáng tin cậy 3. Đầy đủ 4. Kịp thời 5. Dễ hiểu 6. Có thể xác minh 7. Dễ tiếp cận.
- *(🖼️ Ảnh minh họa: Icon đồ họa đại diện cho từng đặc tính xếp thành vòng tròn).*

## Giá trị của Thông tin (Value of Information)
- Định nghĩa: Lợi ích của thông tin trừ đi Chi phí tạo ra nó.
- *(🖼️ Ảnh minh họa: Biểu đồ cán cân (Scale) giữa Chi phí (Thời gian/Tiền bạc) và Lợi ích (Quyết định tốt hơn) - Sinh bằng AI).*

## Hệ thống Thông tin Kế toán (AIS) là gì?
- Thành phần: Con người, Thủ tục, Dữ liệu, Phần mềm, Hạ tầng CNTT và Kiểm soát nội bộ.
- *(🖼️ Ảnh minh họa: Sơ đồ 6 thành phần của AIS kết nối với nhau - Trích xuất từ biểu đồ trong DOCX Chapter 1 AIS).*

---

# PHẦN 2: SỰ TIẾN HÓA CỦA NGHỀ KẾ TOÁN & TRÍ TUỆ NHÂN TẠO

## Sự chuyển dịch vai trò của Kế toán viên
- Từ Bookkeeper -> Data Analyst -> Strategic Advisor.
- *(🖼️ Ảnh minh họa: Hình ảnh tiến hóa (Evolution) từ người giữ sổ dùng giấy bút -> Kế toán viên dùng máy tính -> Kế toán viên đứng trước biểu đồ không gian AI - Sinh bằng AI).*

## Sức ép thay đổi - "Thiên nga đen" (Black Swan)
- Khái niệm Black Swan: Những sự kiện khó lường (VD: Covid-19).
- *(🖼️ Ảnh minh họa: Hình ảnh biểu tượng con Thiên Nga Đen trên biểu đồ chứng khoán đang lao dốc - Lấy từ mạng hoặc sinh bằng AI).*

**SLIDE 13 & 14: Lịch sử AI và Các "Mùa đông AI" (AI Winters)**
- Các cột mốc: 1950 -> 1956 -> Hiện tại.
- Lý do bùng nổ: Big Data, Cloud, GPU.
- *(🖼️ Ảnh minh họa: Biểu đồ dòng thời gian (Timeline) về lịch sử phát triển của AI - Trích xuất từ DOCX Chapter 1 What Accountants Need to Know).*

**SLIDE 15 & 16: Phân biệt AI, Học máy (ML) và Học sâu (Deep Learning)**
- Các khái niệm và 3 loại ML: Supervised, Unsupervised, Reinforcement.
- *(🖼️ Ảnh minh họa: Biểu đồ Venn (3 vòng tròn bao nhau) mô tả AI bao trùm ML, ML bao trùm Deep Learning - Rất phổ biến, trích từ sách DOCX).*

## Trí tuệ con người vs. Trí tuệ nhân tạo
- Sự bổ trợ: Xét đoán đạo đức vs Tốc độ xử lý khổng lồ.
- *(🖼️ Ảnh minh họa: Hình ảnh não người kết nối với bo mạch máy tính (Brain vs AI) hoặc Bảng Table so sánh).*

## Sự lầm tưởng "AI = Lập trình"
- Tư duy cũ: "Tôi là kế toán, tôi không biết code". Tư duy mới: Ứng dụng qua giao diện No-code.
- *(🖼️ Ảnh minh họa: Hình người đang dùng giao diện Chat (như ChatGPT) với dấu X gạch chéo màn hình toàn mã code lập trình).*

**SLIDE 19 & 20: AI đang thay thế phần nào công việc kế toán?**
- Công việc AI thay thế: Nhập liệu, khớp hóa đơn.
- Công việc AI KHÔNG thay thế: Đánh giá đạo đức, diễn giải chuẩn mực.
- *(🖼️ Ảnh minh họa: Bảng hoặc Sơ đồ cây phân loại các nhóm công việc AI làm tốt và kém).*

---

# PHẦN 3: ỨNG DỤNG THỰC TIỄN CỦA AI TRONG CHU TRÌNH KẾ TOÁN

## Các Chu trình Kinh doanh cơ bản (Business Processes)
- Revenue, Expenditure, Production, HR, Financing.
- *(🖼️ Ảnh minh họa: Sơ đồ luân chuyển thông tin giữa 5 chu trình kinh doanh cơ bản - Lấy nguyên bản từ DOCX Chapter 1 AIS).*

**SLIDE 22 đến 25: AI trong từng Chu trình (Doanh thu, Chi phí, Sản xuất, Tiền lương)**
- Dự báo doanh số, OCR đọc hóa đơn, so khớp 3 bên, chấm công thông minh.
- *(🖼️ Ảnh minh họa: Ở mỗi chu trình chèn 1 hình mô tả quy trình OCR hoặc quy trình Matching tự động hóa - Trích từ DOCX).*

**SLIDE 26 & 27: AI trong Kiểm soát nội bộ và Phát hiện gian lận**
- Phát hiện giao dịch ảo, chênh lệch bằng Machine Learning (Anomaly Detection).
- *(🖼️ Ảnh minh họa: Biểu đồ Scatter Plot phân tán, khoanh đỏ các điểm ngoại lai (Outliers) đại diện cho gian lận - Trích từ DOCX).*

## Lợi ích của AIS tích hợp AI
- Tốc độ, giảm chi phí, cải thiện dòng tiền.
- *(🖼️ Ảnh minh họa: Biểu đồ tăng trưởng (Upward trend) kết hợp icon AI).*

**SLIDE 29 & 30: AI trong Chuỗi giá trị (Value Chain)**
- Các hoạt động chính, AIS nối kết dữ liệu.
- *(🖼️ Ảnh minh họa: Sơ đồ Value Chain của Michael Porter truyền thống, đánh dấu phần System Support - Trích từ DOCX Chapter 1 AIS).*

---

# PHẦN 4: TƯƠNG LAI VỚI GENERATIVE AI (CHATGPT)

**SLIDE 31 & 32: Generative AI là gì? ChatGPT và Kế toán**
- AI có khả năng sáng tạo. Cơ hội và Thách thức (Hallucination).
- *(🖼️ Ảnh minh họa: Logo các mô hình GAI lớn như ChatGPT, Gemini, Copilot).*

## Khái niệm Prompt Engineering (Kỹ nghệ Gợi ý)
- Kỹ năng ra lệnh cho AI để được kết quả chính xác nhất.
- *(🖼️ Ảnh minh họa: Sơ đồ cấu trúc của một câu Prompt chuẩn: Role + Context + Task + Format).*

**SLIDE 34 đến 36: Ứng dụng ChatGPT (Soạn văn bản, Giải thích BCTC, Tra cứu)**
- Thực tiễn ứng dụng thay thế sức người.
- *(🖼️ Ảnh minh họa: Ảnh chụp màn hình (Screenshot) một đoạn hội thoại mẫu hỏi ChatGPT về giải thích BCTC).*

**SLIDE 37 & 38: Rủi ro, Đạo đức (Data Privacy, Bias, Human-in-the-loop)**
- Rủi ro bảo mật dữ liệu, thiên kiến và trách nhiệm giải trình.
- *(🖼️ Ảnh minh họa: Hình minh họa "Con người luôn ở trong quy trình" (Human-in-the-loop) - Con người duyệt lại kết quả từ máy tính).*

## 3 Kỹ năng Sinh tồn của Kế toán tương lai
- 1. Prompting 2. Fact-checking 3. Phân tích tham mưu.
- *(🖼️ Ảnh minh họa: Hình ảnh Kế toán viên siêu anh hùng hoặc Icon đại diện 3 kỹ năng).*

**SLIDE 40 & 41: Lời kết & Tổng kết bài học**
- Tóm tắt lại các mục tiêu đã đạt được.

## Giới thiệu Buổi Thực Hành & Q&A
- Cài đặt ChatGPT/Gemini, chuẩn bị cho bài tập thực hành.
- *(🖼️ Ảnh minh họa: Màn hình báo "Chuẩn bị vào Lab Thực Hành" kèm mã QR code link đến phần mềm).*
