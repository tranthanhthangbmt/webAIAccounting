# Kế hoạch Thiết kế và Xây dựng Bộ Slide Bài giảng Buổi 1 theo Chuẩn Beamer (Học tập từ TaiLieu/slideDL)

**Thư mục mục tiêu:** `webAIAccounting/TaiLieu/slideAIAcc/`  
**File định dạng mới:** LaTeX Beamer Widescreen 16:9 (`\documentclass[aspectratio=169]{beamer}`)  
**Theme & Color Theme:** `Madrid` theme, `default` colortheme (chuẩn tương tự `TaiLieu/slideDL`)  
**File nguồn nội dung:** `docs/buoi_01.md` (Tab Tiếng Việt - *Chương 1: Những điều Kế toán viên cần biết về AI*)  
**Thư mục hình ảnh:** `Figures/Buoi_01/`  
**Thời lượng chuẩn đại học:** 3 Tiết học (135 Phút giảng dạy & thảo luận)  
**Quy mô dự kiến:** **45 - 50 Frames (Slides) chi tiết**

---

## 1. Lý do Đổi mới & Ưu điểm vượt trội của Kiến trúc Beamer (16:9 Madrid)

Khác với kiến trúc cũ dùng `\documentclass{article}` + `aima2e-slides.sty` (thiết kế kiểu 4:3 cũ từ thập niên 1990/2000), việc áp dụng chuẩn **LaTeX Beamer 16:9 (`aspectratio=169`)** như môn Deep Learning (`TaiLieu/slideDL/Chapter01.tex`) mang lại các lợi ích tuyệt đối:
1. **Tỷ lệ khung hình hiện đại 16:9:** Phù hợp hoàn hảo với màn hình máy chiếu giảng đường đại học hiện đại và màn hình laptop sinh viên.
2. **Thanh điều hướng & Chân trang chuyên nghiệp (Madrid Theme):** Tự động hiển thị Tên bài giảng, Tên trường (*Đại học Đông Á*), ngày tháng và số thứ tự trang (`Frame X / Y`).
3. **Mục lục Động (`\tableofcontents`) & Phân chia Chương mục (`\section{...}`):** Giúp giảng viên và sinh viên luôn định vị được mình đang ở phần nào trong thời lượng 135 phút của buổi học.
4. **Trình bày Song song (`\begin{columns}`):**
   - Cho phép đặt nội dung giải thích lý thuyết bên trái (`\column{0.5\textwidth}`) và hình ảnh bên phải (`\column{0.5\textwidth}`).
   - Đặc biệt tối ưu để nhúng và phân tích 2 biểu đồ quan trọng:
     - `Figure 1.1 Relationship between AI, ML, and DL..PNG`
     - `Figure 1.2 Relationship between (big) data mining and AI..PNG`
5. **Độ ổn định tối đa:** Xử lý danh sách bằng `\begin{itemize}` và `\begin{enumerate}` chuẩn LaTeX, không bao giờ gặp lỗi ngắt dòng hay tràn trang không kiểm soát.

---

## 2. Bố cục Phân chương Tiết học (Sections & TOC)

Bộ slide Buổi 1 sẽ được cấu trúc thành **4 Sections chính**, tự động sinh ra Mục lục bài giảng:

```latex
\section{1. Khái quát về AI \& Lịch sử Chuyển đổi số Kế toán}
\section{2. Hệ sinh thái AI Cốt lõi \& Học máy trong Tài chính}
\section{3. NLP, Khai phá Dữ liệu, RPA \& API cho Kế toán}
\section{4. Công cụ Lập trình (Python/SQL) \& Lộ trình Kỹ năng}
```

### Tiết 1 (45 Phút - 15 Frames): Khái quát về AI & Lịch sử Chuyển đổi số Kế toán
- **Mục tiêu:** Nắm bắt bối cảnh kinh tế số, định nghĩa AI, phân biệt rạch ròi giữa Trí tuệ con người và Trí tuệ nhân tạo, điểm lại hành trình 5 giai đoạn lịch sử công nghệ của Kế toán viên.
- **Nội dung các slide:**
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

### Tiết 2 (45 Phút - 15 Frames): Hệ sinh thái AI Cốt lõi & Học máy trong Tài chính
- **Mục tiêu:** Hiểu sâu phân loại ANI/AGI, cơ chế Lập luận máy, Hệ chuyên gia thuế, cấu trúc AI - ML - DL và 4 phân lớp Học máy.
- **Nội dung các slide:**
  16. Phân loại Trí tuệ Nhân tạo: ANI (AI Hẹp) vs. AGI (AI Tổng quát)
  17. 3 Ứng dụng ANI trong Kế toán: OCR, Credit Risk Scoring, IFRS Chatbot
  18. Tầm nhìn AGI & Thách thức kiểm soát đạo đức kế toán (IFAC / AICPA)
  19. Lập luận máy (Machine Reasoning): Liên kết thuận (Forward) vs. Ngược (Backward)
  20. Hệ chuyên gia (Expert Systems): Cơ sở tri thức (`IF-THEN`) + Động cơ suy diễn
  21. Case Study Hệ chuyên gia: Tự động quyết toán thuế TNDN (Chi phí được trừ)
  22. Học máy (Machine Learning): Lập trình cổ điển (Rules + Data) vs. ML (Data + Answers = Rules)
  23. **[SLIDE SONG SONG - HÌNH 1.1]** Mối quan hệ giữa AI, ML và DL (`Figure 1.1 Relationship between AI, ML, and DL..PNG`)
  24. Phân tích Sơ đồ Figure 1.1 dưới góc độ Kế toán - Kiểm toán
  25. Học có giám sát (Supervised Learning): Bài toán Phân lớp & Hồi quy từ dữ liệu gán nhãn
  26. Ứng dụng Supervised ML: Phát hiện gian lận hóa đơn & Chấm điểm rủi ro nợ phải thu
  27. Học không giám sát (Unsupervised Learning): Phân cụm (Clustering) & Giảm chiều dữ liệu
  28. Ứng dụng Unsupervised ML: Phát hiện giao dịch bất thường trong Sổ Nhật ký chung (Outlier/Anomaly Detection)
  29. Học bán giám sát (Semi-supervised Learning): Bài toán gán nhãn 95% hóa đơn từ 5% mẫu kiểm toán
  30. Học tăng cường (Reinforcement Learning - RL): Thử & Sai, Quản trị dòng tiền động & Định giá động
  31. Học sâu (Deep Learning - DL): Mạng nơ-ron đa tầng xử lý ảnh hóa đơn & văn bản phi cấu trúc

### Tiết 3 (45 Phút - 16 Frames): NLP, Khai phá Dữ liệu, RPA & API cho Kế toán
- **Mục tiêu:** Nắm vững công nghệ xử lý chứng từ thông minh IDP, NLP, Khai phá dữ liệu lớn, RPA tiến hóa sang AI-RPA, API kế toán mở và lộ trình học lập trình.
- **Nội dung các slide:**
  32. Xử lý Chứng từ Thông minh (IDP) bằng Deep Learning OCR + ML
  33. Xử lý Ngôn ngữ Tự nhiên (NLP): Hiểu (NLU) & Sinh (NLG) ngôn ngữ kinh tế
  34. Ứng dụng NLP: Bóc tách hợp đồng IFRS 16 & Trợ lý ảo CFO Chatbot
  35. Khai phá Dữ liệu (Data Mining): Sàng lọc tri thức từ Data Warehouse
  36. **[SLIDE SONG SONG - HÌNH 1.2]** Big Data Mining và AI (`Figure 1.2 Relationship between (big) data mining and AI..PNG`)
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

## 3. Kiến trúc Kỹ thuật & Mã Mẫu Beamer (`build_beamer_day01.py`)

Script Python `build_beamer_day01.py` sẽ sinh file `Slide_AIAcc_Day01.tex` chuẩn Beamer như sau:

```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}
\usecolortheme{default}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{booktabs}

\setbeamertemplate{caption}[numbered]
\renewcommand{\figurename}{Hình}
\renewcommand{\thefigure}{1.\arabic{figure}}

\title[Buổi 1: AI & Nghề Kế toán]{Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.5cm} \Large Buổi 1: Những điều Kế toán viên cần biết về AI}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Nội dung Chương trình Buổi học (135 Phút)}
    \tableofcontents
\end{frame}

% ... CÁC SECTION VÀ FRAMES ...

\end{document}
```

---

## 4. Kế hoạch Triển khai (Next Steps sau khi Thầy đồng ý)

1. **Bước 1:** Viết kịch bản `build_beamer_day01.py` để tạo toàn bộ 48 frames chuẩn Beamer 16:9 vào file `TaiLieu/slideAIAcc/Slide_AIAcc_Day01.tex`.
2. **Bước 2:** Biên dịch file `Slide_AIAcc_Day01.tex` 2 lần bằng `pdflatex` để tạo `Slide_AIAcc_Day01.pdf`.
3. **Bước 3:** Kiểm tra số trang, mục lục, thanh điều hướng Madrid và chất lượng 2 hình ảnh `Figure 1.1` và `Figure 1.2`.
4. **Bước 4:** Cập nhật tài liệu tổng kết `walkthrough.md`.
