# Kế hoạch Thiết kế và Làm lại Bộ Slide Bài giảng Buổi 1 (Chuẩn Beamer 16:9 - Học tập từ Môn Deep Learning)

**Thư mục mục tiêu:** `webAIAccounting/TaiLieu/slideAIAcc/`  
**Định dạng mới:** **LaTeX Beamer Widescreen 16:9** (`\documentclass[aspectratio=169]{beamer}`)  
**Theme & Colortheme:** `Madrid` theme, `default` color theme (được chuẩn hóa theo đúng môn `TaiLieu/slideDL`)  
**File nguồn nội dung:** `docs/buoi_01.md` (Tab Tiếng Việt - *Chương 1: Những điều Kế toán viên cần biết về AI*)  
**Thư mục hình ảnh:** `Figures/Buoi_01/`  
**Thời lượng chuẩn đại học:** 3 Tiết học (135 Phút giảng dạy & thảo luận)  
**Quy mô dự kiến:** **48 Frames (Slides) chi tiết**

---

## 1. Goal Description (Mục tiêu Kỹ thuật & Sư phạm)

Sau khi nghiên cứu cách làm slide của môn Deep Learning trong thư mục **`webAIAccounting/TaiLieu/slideDL`**, tôi đề xuất làm lại toàn bộ kế hoạch và kiến trúc slide cho Buổi 1 của môn **"Trí tuệ Nhân tạo cho Kế toán"** từ chuẩn cũ (`article` + `aima2e-slides.sty`) sang **chuẩn Beamer hiện đại 16:9 (`Madrid` theme)**:
- **Tương thích tuyệt đối với màn hình 16:9 hiện đại:** Hiển thị trang chiếu ngang rộng rãi, có thanh tiêu đề (`frametitle`), chân trang (`footline`) tự động đếm số trang (`Frame X / Y`) và hiển thị tên trường Đại học Đông Á.
- **Tự động hóa Mục lục & Đánh dấu Chương mục:** Bố cục bài giảng được chia làm **4 Sections**, sinh ra Mục lục Động (`\tableofcontents`) ngay sau trang bìa.
- **Tích hợp hình ảnh trọn vẹn bằng bố cục song song (`\begin{columns}`):**
  1. `Figure 1.1 Relationship between AI, ML, and DL..PNG` (Slide 23 - Sơ đồ bao hàm AI, ML, DL).
  2. `Figure 1.2 Relationship between (big) data mining and AI..PNG` (Slide 36 - Sơ đồ Big Data Mining và AI).
- **Phân bổ chương trình 3 tiết chuẩn đại học (135 phút):** 48 frames chuyên sâu cho sinh viên ngành kế toán tiếp thu toàn diện tri thức AI và thảo luận tình huống.

---

## 2. User Review Required (Các điểm cần Thầy xác nhận)

> [!IMPORTANT]
> **Xác nhận Kiến trúc Beamer 16:9 (`Madrid` Theme):**  
> Tôi đề xuất áp dụng kiến trúc chuẩn của môn Deep Learning (`TaiLieu/slideDL`):
> `\documentclass[aspectratio=169]{beamer}`  
> `\usetheme{Madrid}`  
> `\usecolortheme{default}`  
> Thầy có đồng ý sử dụng đúng kiến trúc chuẩn Beamer này cho toàn bộ môn AI cho Kế toán không?

> [!WARNING]
> **Xác nhận Thời lượng & Số lượng Slide (48 Frames / 135 Phút):**  
> Mỗi slide trong Beamer được tối ưu ngắn gọn, mạch lạc (3-5 gạch đầu dòng rõ ràng, kết hợp cột hình ảnh), thời lượng trung bình **2.8 phút / frame**, cực kỳ lý tưởng cho 3 tiết giảng đường đại học.

---

## 3. Open Questions

- Thầy có muốn đặt tên file kịch bản sinh mã mới là `build_beamer_day01.py` để phân biệt với script cũ không?
- Lệnh biên dịch chuẩn Beamer sẽ là: `pdflatex -synctex=1 -interaction=nonstopmode Slide_AIAcc_Day01.tex` chạy 2 lần trong thư mục `TaiLieu/slideAIAcc/` để tự động tạo Mục lục và số trang hoàn chỉnh.

---

## 4. Proposed Changes & Bố cục Phân chương Beamer (Sections & TOC)

### Cấu trúc 4 Sections trong Mục lục Động (`\tableofcontents`)
```latex
\section{1. Khái quát về AI \& Lịch sử Chuyển đổi số Kế toán}
\section{2. Hệ sinh thái AI Cốt lõi \& Học máy trong Tài chính}
\section{3. NLP, Khai phá Dữ liệu, RPA \& API cho Kế toán}
\section{4. Công cụ Lập trình (Python/SQL) \& Lộ trình Kỹ năng}
```

### Tiết 1 (45 Phút - 15 Frames): Khái quát về AI & Lịch sử Chuyển đổi số Kế toán
- **Mục tiêu:** Nắm bắt bối cảnh kinh tế số, định nghĩa AI, phân biệt rạch ròi giữa Trí tuệ con người và Trí tuệ nhân tạo, điểm lại hành trình 5 giai đoạn lịch sử công nghệ của Kế toán viên.
- **Nội dung các frames:**
  1. Trang bìa (`\titlepage` - Trường Đại học Đông Á)
  2. Mục lục nội dung chương (`\tableofcontents`)
  3. Mục tiêu bài học (LO 1.1 đến LO 1.5)
  4. Bối cảnh bùng nổ dữ liệu phi cấu trúc trong Kế toán
  5. Định nghĩa Trí tuệ Nhân tạo (AI) trong tài chính
  6. Trí tuệ Con người (Trực giác, đạo đức, sáng tạo) vs. Trí tuệ Nhân tạo (Tốc độ, 24/7, big data)
  7. Bảng so sánh vùng năng lực Kế toán viên và máy móc
  8. Lịch sử AI từ 1950 (Phép thử Turing, Dartmouth) đến Kỷ nguyên Deep Learning
  9. Các "Mùa đông AI" (AI Winters) và lý do AI ngày nay phát triển bùng nổ
  10. Lịch sử Kế toán ứng dụng Công nghệ - Giai đoạn 1 (Bàn tính, Sổ giấy) & 2 (Mainframe, Excel 1985)
  11. Lịch sử Kế toán ứng dụng Công nghệ - Giai đoạn 3 (ERP - SAP/Oracle) & 4 (Cloud Accounting, RPA)
  12. Giai đoạn 5 - Kỷ nguyên AI & Chuyển dịch sang Kiểm toán Liên tục (Continuous Auditing)
  13. Thực trạng ứng dụng AI từ Big4 & AICPA (Tăng hiệu suất 40-60%)
  14. 3 tác vụ AI tiêu chuẩn: e-Invoice, Đối chiếu tự động, Phân tích chi phí
  15. Thảo luận: "AI có thay thế Kế toán viên?" (Cơ hội vs. Thách thức)

### Tiết 2 (45 Phút - 16 Frames): Hệ sinh thái AI Cốt lõi & Học máy trong Tài chính
- **Mục tiêu:** Hiểu sâu phân loại ANI/AGI, cơ chế Lập luận máy, Hệ chuyên gia thuế, cấu trúc AI - ML - DL và 4 phân lớp Học máy.
- **Nội dung các frames:**
  16. Phân loại Trí tuệ Nhân tạo: ANI (AI Hẹp) vs. AGI (AI Tổng quát)
  17. 3 Ứng dụng ANI trong Kế toán: OCR, Credit Risk Scoring, IFRS Chatbot
  18. Tầm nhìn AGI & Thách thức kiểm soát đạo đức kế toán (IFAC / AICPA)
  19. Lập luận máy (Machine Reasoning): Liên kết thuận (Forward) vs. Ngược (Backward)
  20. Hệ chuyên gia (Expert Systems): Cơ sở tri thức (`IF-THEN`) + Động cơ suy diễn
  21. Case Study Hệ chuyên gia: Tự động quyết toán thuế TNDN (Chi phí được trừ)
  22. Học máy (Machine Learning): Lập trình cổ điển (Rules + Data) vs. ML (Data + Answers = Rules)
  23. **[SLIDE SONG SONG - HÌNH 1.1]** Mối quan hệ giữa AI, ML và DL (`Figure 1.1 Relationship between AI, ML, and DL..PNG` đặt cột phải 0.45, giải thích cột trái 0.55)
  24. Phân tích Sơ đồ Figure 1.1 dưới góc độ Kế toán - Kiểm toán
  25. Học có giám sát (Supervised Learning): Bài toán Phân lớp & Hồi quy từ dữ liệu gán nhãn
  26. Ứng dụng Supervised ML: Phát hiện gian lận hóa đơn & Chấm điểm rủi ro nợ phải thu
  27. Học không giám sát (Unsupervised Learning): Phân cụm (Clustering) & Giảm chiều dữ liệu
  28. Ứng dụng Unsupervised ML: Phát hiện giao dịch bất thường trong Sổ Nhật ký chung (Outlier/Anomaly Detection)
  29. Học bán giám sát (Semi-supervised Learning): Bài toán gán nhãn 95% hóa đơn từ 5% mẫu kiểm toán
  30. Học tăng cường (Reinforcement Learning - RL): Thử & Sai, Quản trị dòng tiền động & Định giá động
  31. Học sâu (Deep Learning - DL): Mạng nơ-ron đa tầng xử lý ảnh hóa đơn & văn bản phi cấu trúc

### Tiết 3 (45 Phút - 17 Frames): NLP, Khai phá Dữ liệu, RPA & API cho Kế toán
- **Mục tiêu:** Nắm vững công nghệ xử lý chứng từ thông minh IDP, NLP, Khai phá dữ liệu lớn, RPA tiến hóa sang AI-RPA, API kế toán mở và lộ trình học lập trình.
- **Nội dung các frames:**
  32. Xử lý Chứng từ Thông minh (IDP) bằng Deep Learning OCR + ML
  33. Xử lý Ngôn ngữ Tự nhiên (NLP): Hiểu (NLU) & Sinh (NLG) ngôn ngữ kinh tế
  34. Ứng dụng NLP: Bóc tách hợp đồng IFRS 16 & Trợ lý ảo CFO Chatbot
  35. Khai phá Dữ liệu (Data Mining): Sàng lọc tri thức từ Data Warehouse
  36. **[SLIDE SONG SONG - HÌNH 1.2]** Big Data Mining và AI (`Figure 1.2 Relationship between (big) data mining and AI..PNG` đặt cột phải 0.45, giải thích cột trái 0.55)
  37. Phân tích Biểu đồ Figure 1.2: Nhiên liệu (Big Data) -> Sàng lọc (Data Mining) -> Động cơ quyết định (AI)
  38. Khai phá Văn bản (Text Mining): Phân tích cảm xúc Báo cáo thường niên & Rà soát pháp lý
  39. Tự động hóa Quy trình bằng Robot (RPA): Robot phần mềm tự tải sao kê, đối chiếu công nợ
  40. Sự tiến hóa: Từ RPA truyền thống (Rule-based) đến AI-RPA (Intelligent Automation)
  41. Case Study AI-RPA trong Phòng Kế toán Thanh toán (Accounts Payable - AP)
  42. Giao diện Lập trình Ứng dụng (API): Chấm dứt kỷ nguyên nhập liệu thủ công giữa POS, Ngân hàng và Sổ cái
  43. Hệ sinh thái Kế toán Mở (Open Accounting APIs) & Kết nối Cổng Thuế điện tử
  44. 3 Ngôn ngữ Lập trình Vàng cho Kế toán viên: Python, R và SQL
  45. Vì sao Python là "Ngôn ngữ chung" của Kế toán hiện đại? (Pandas, Scikit-learn, Excel)
  46. Lộ trình Nâng cấp Năng lực 4 Bước (Upskilling Roadmap: Data Literacy -> Excel/SQL -> Python -> AI-RPA)
  47. Bài tập Tình huống Buổi 1: Lựa chọn công nghệ AI cho 4 bài toán doanh nghiệp
  48. Tổng kết Buổi 1 & Chuẩn bị bài đọc Buổi 2 (AI in Finance, Big Data & Blockchain)

---

## 5. Verification Plan (Kế hoạch Kiểm thử & Kiểm chứng)

### 1. Kiểm thử Biên dịch Tự động Beamer (Automated Beamer Build)
- Chạy lệnh biên dịch 2 lần trong thư mục `TaiLieu/slideAIAcc/` để cập nhật Mục lục (`.toc`) và số trang:
  ```bash
  pdflatex -synctex=1 -interaction=nonstopmode Slide_AIAcc_Day01.tex
  pdflatex -synctex=1 -interaction=nonstopmode Slide_AIAcc_Day01.tex
  ```
- Đảm bảo mã thoát thành công `Exit code 0`, không có lỗi phông chữ T5 hay lỗi mất hình ảnh.

### 2. Kiểm chứng Chất lượng Trực quan Beamer
- Kiểm tra thanh điều hướng dưới chân trang (`Madrid` theme) hiển thị rõ "Trí tuệ Nhân tạo cho Kế toán - Đại học Đông Á - Frame X / Y".
- Kiểm tra 2 trang chiếu song song (`\begin{columns}`) cho Figure 1.1 và Figure 1.2 hiển thị tỷ lệ đẹp mắt 55:45, không tràn viền.
