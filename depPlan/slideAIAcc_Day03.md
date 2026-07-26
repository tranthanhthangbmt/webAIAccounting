# Kế hoạch Thiết kế và Làm lại Bộ Slide Bài giảng Buổi 3 (Chuẩn Beamer 16:9)

**Thư mục mục tiêu:** `webAIAccounting/TaiLieu/slideAIAcc/`  
**Định dạng thiết kế:** **LaTeX Beamer Widescreen 16:9** (`\documentclass[aspectratio=169]{beamer}`)  
**Theme \& Colortheme:** `Madrid` theme, `default` color theme (Kế thừa từ kiến trúc Buổi 1 và Buổi 2)  
**File nguồn nội dung:** `docs/buoi_03.md` (Tab Tiếng Việt - *Buổi 3: Tương lai của AI, Đạo đức, Rủi ro và Khai phá Dữ liệu trong Kế toán*)  
**Thư mục hình ảnh:** `Figures/Buoi_03B/` (Có chứa hình `image1.jpeg` - AI Ethics and Regulation in Finance)  
**Thời lượng chuẩn đại học:** 3 Tiết học (135 Phút giảng dạy & thảo luận)  
**Quy mô dự kiến:** **45-50 Frames (Slides) chi tiết**

---

## 1. Goal Description (Mục tiêu Kỹ thuật & Sư phạm)

Cấu trúc nội dung Buổi 3 tập trung vào hai mảng chính:
1. Chi tiết các công nghệ AI áp dụng trong kế toán (Học sâu, NLP, Data Mining, Text Mining, RPA, API).
2. Góc nhìn Đạo đức, Pháp luật và Rủi ro khi ứng dụng AI Tạo sinh vào hệ thống tài chính.

**Mục tiêu thiết kế Slide:**
- Tiếp tục tận dụng cấu trúc Beamer 16:9 để tạo không gian hiển thị văn bản rộng rãi.
- Chia toàn bộ nội dung thành **3 Sections chính**, tương ứng với 3 Tiết học trên lớp, giúp sinh viên không bị quá tải kiến thức.
- Tại phần Đạo đức, sẽ đưa ảnh `image1.jpeg` vào minh họa dưới dạng slide 2 cột (`\begin{columns}`) để nhấn mạnh vòng lặp Quy định & Đạo đức AI.
- Tăng cường thiết kế danh sách đa cấp (Bullet hanging indent) cho các ví dụ Case Studies từ ICICI Bank, HDFC, Paytm.

---

## 2. Bố cục Phân chương Beamer dự kiến (Sections \& TOC)

Để bài giảng đạt hiệu quả cao, tôi đã phân nhỏ 2 mục lớn trong Markdown thành 3 Sections giảng dạy:

### Mục lục Động (`\tableofcontents`)
```latex
\section{1. Học sâu, NLP \& Khai phá Dữ liệu (Data Mining) trong Kế toán}
\section{2. Tự động hóa RPA, Ứng dụng API \& Lập trình Kế toán}
\section{3. Đạo đức, Pháp luật \& Rủi ro AI Tạo sinh trong Tài chính}
```

### Tiết 1 (45 Phút - Khoảng 16 Frames): Học sâu, NLP & Khai phá Dữ liệu
- **Mục tiêu:** Sinh viên hiểu rõ Deep Learning hoạt động ra sao trong nhận dạng chứng từ, và cách NLP/Khai phá dữ liệu hỗ trợ công tác kiểm toán.
- **Nội dung chính:**
  1. Trang bìa & Mục lục.
  2. Mục tiêu bài học (LO 3.1 -> LO 3.5).
  3. Mạng Nơ-ron Nhân tạo (ANNs) và Học sâu (Deep Learning).
  4. Ứng dụng Học sâu trong Tái tạo Chứng từ (Ví dụ: EY quét hóa đơn OCR).
  5. Xử lý Ngôn ngữ Tự nhiên (NLP): Phân biệt NLU (Hiểu) và NLG (Tạo ngôn ngữ).
  6. Ví dụ NLG: Chuyển biểu đồ tài chính thành báo cáo văn bản.
  7. Khai phá Dữ liệu (Data Mining) vs Học máy (Sự khác biệt cốt lõi).
  8. Ứng dụng Data Mining: Phát hiện giao dịch ngoại lai (Outliers) trong Sổ cái chung.
  9. Khai phá Văn bản (Text Mining): Trích xuất khái niệm từ hợp đồng, email (Kế toán pháp y).

### Tiết 2 (45 Phút - Khoảng 15 Frames): Tự động hóa RPA, Ứng dụng API & Lập trình
- **Mục tiêu:** Nắm bắt công nghệ tự động hóa chu trình kế toán lặp đi lặp lại và cách thức phần mềm giao tiếp với nhau.
- **Nội dung chính:**
  1. Tự động hóa Quy trình Bằng Robot (RPA) là gì?
  2. RPA khác gì với AI? (RPA là tay chân, AI là bộ não).
  3. Ứng dụng RPA trong Kế toán: Đối chiếu ngân hàng, theo dõi khoản phải trả.
  4. Lợi ích: Tăng năng suất, giảm sai sót với các bot như UiPath, BluePrism.
  5. Giao diện Lập trình Ứng dụng (API): Khái niệm "Người phục vụ nhà hàng".
  6. Google Prediction API \& BigML trong hệ sinh thái Kế toán mở.
  7. Tại sao Kế toán viên cần học Lập trình? (Python, R, SQL).
  8. Tự tùy biến công nghệ AI (Do-it-yourself) cho doanh nghiệp.

### Tiết 3 (45 Phút - Khoảng 17 Frames): Đạo đức, Pháp luật & Rủi ro AI Tạo sinh
- **Mục tiêu:** Nâng cao nhận thức về rủi ro đạo đức, quyền riêng tư và thao túng thị trường khi áp dụng AI.
- **Nội dung chính:**
  1. Giới thiệu AI Tạo sinh (Generative AI) trong Tài chính.
  2. **[SLIDE SONG SONG]** Đạo đức và Quy định AI trong Tài chính (`Figure 15.1 - image1.jpeg`).
  3. Thách thức 1: Quyền riêng tư Dữ liệu (Vụ rò rỉ dữ liệu Equifax 2017).
  4. Thách thức 2: Giao dịch Thuật toán \& Sự kiện Flash Crash 2010.
  5. Thách thức 3: Lập hồ sơ Khách hàng (Customer Profiling) \& Vấn đề Xâm phạm cá nhân.
  6. Thách thức 4: Mất việc làm \& Bất bình đẳng kinh tế.
  7. Case Studies 1: Ngân hàng ICICI (Chatbot iPal \& Bảo mật).
  8. Case Studies 2: Paytm (Rủi ro thao túng thị trường bằng thuật toán).
  9. Case Studies 3: HDFC Bank (Thiên kiến - Bias trong chấm điểm tín dụng AI).
  10. Tổng kết bài học và Dặn dò.

---

## 3. User Review Required (Các điểm cần Thầy xác nhận)

> [!IMPORTANT]
> **Xác nhận Bố cục 3 Sections:**  
> Thay vì tuân theo đúng 2 phần lớn của sách gốc (có thể làm Tiết 1 quá dài), tôi đã bóc tách RPA, API và Ngôn ngữ lập trình thành một **Tiết học độc lập (Section 2)** để sinh viên khối Kế toán dễ hấp thụ mảng công nghệ phần mềm. Thầy vui lòng xem có hợp lý không?

> [!NOTE]
> **Về Hình ảnh (Figures):**  
> Trong thư mục `Figures/Buoi_03B/` hiện chỉ có duy nhất 1 ảnh `image1.jpeg` (Figure 15.1). Tôi sẽ tận dụng nó tối đa cho Section 3. Các Section khác sẽ tập trung thiết kế Text rõ ràng, mạch lạc, kết hợp bảng biểu tự vẽ bằng LaTeX nếu cần thiết.

---

## 4. Verification Plan (Kế hoạch Kiểm thử & Kiểm chứng)

Sau khi Thầy duyệt kế hoạch này, tôi sẽ tiến hành tạo Script `build_beamer_day03.py`:
- Thực hiện chạy `pdflatex` 2 lần tương tự Buổi 1 \& 2.
- Đảm bảo mã thoát `Exit code 0` và sinh ra `Slide_AIAcc_Day03.pdf` chuẩn xác.
- Kiểm tra trực quan xem hình `image1.jpeg` có hiển thị đẹp không bị mờ hay chèn chữ.
