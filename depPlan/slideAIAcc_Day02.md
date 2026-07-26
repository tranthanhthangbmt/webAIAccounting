# Kế hoạch Thiết kế và Làm lại Bộ Slide Bài giảng Buổi 2 (Chuẩn Beamer 16:9 - Học tập từ Môn Deep Learning)

**Thư mục mục tiêu:** `webAIAccounting/TaiLieu/slideAIAcc/`  
**Định dạng mới:** **LaTeX Beamer Widescreen 16:9** (`\documentclass[aspectratio=169]{beamer}`)  
**Theme & Colortheme:** `Madrid` theme, `default` color theme (được chuẩn hóa theo đúng môn `TaiLieu/slideDL`)  
**File nguồn nội dung:** `docs/buoi_02.md` (Tab Tiếng Việt - *Buổi 2: AI, Blockchain và Dữ liệu lớn trong Kinh tế - Tài chính*)  
**Thư mục hình ảnh:** `Figures/Buoi_02B/`  
**Thời lượng chuẩn đại học:** 3 Tiết học (135 Phút giảng dạy & thảo luận)  
**Quy mô dự kiến:** **48 Frames (Slides) chi tiết**

---

## 1. Goal Description (Mục tiêu Kỹ thuật & Sư phạm)

Tiếp nối sự thành công trong việc tạo slide bài giảng Buổi 1, chúng ta sẽ tiếp tục áp dụng chuẩn **Beamer hiện đại 16:9 (`Madrid` theme)** cho Buổi 2 của môn **"Trí tuệ Nhân tạo cho Kế toán"**:
- **Tương thích tuyệt đối với màn hình 16:9 hiện đại:** Hiển thị trang chiếu ngang rộng rãi, có thanh tiêu đề (`frametitle`), chân trang (`footline`) tự động đếm số trang (`Frame X / Y`) và hiển thị tên trường Đại học Đông Á.
- **Tự động hóa Mục lục & Đánh dấu Chương mục:** Bố cục bài giảng được chia làm **4 Sections**, sinh ra Mục lục Động (`\tableofcontents`) ngay sau trang bìa.
- **Tích hợp hình ảnh trọn vẹn bằng bố cục song song (`\begin{columns}`):**
  - Khai thác tối đa các hình ảnh chất lượng từ thư mục `Figures/Buoi_02B/` như biểu đồ Venn về Data Scientist (Figure 6.2), sơ đồ quan hệ AI-ML-DL (Figure 6.3), các bước mô hình hóa (Figure 6.7), và các biểu đồ Tradeoff Bias-Variance (Figure 6.9).
- **Phân bổ chương trình 3 tiết chuẩn đại học (135 phút):** 48 frames chuyên sâu cho sinh viên ngành kế toán tiếp thu toàn diện tri thức AI, Blockchain, Dữ liệu lớn và thảo luận tình huống.

---

## 2. User Review Required (Các điểm cần Thầy xác nhận)

> [!IMPORTANT]
> **Xác nhận Cấu trúc 4 Phân đoạn (Sections) cho Buổi 2:**  
> Tôi đã phân tách nội dung của Buổi 2 thành 4 phần chính tương ứng với 4 Section trong Beamer. Thầy vui lòng xem qua `Bố cục Phân chương Beamer` bên dưới để đảm bảo mạch kiến thức đi từ (1) Blockchain & Bitcoin -> (2) DeFi & NFT -> (3) Khoa học Dữ liệu & Big Data -> (4) Quy trình Khai phá Dữ liệu.

> [!WARNING]
> **Xác nhận Hình ảnh & Đồ thị minh họa:**  
> Buổi 2 có rất nhiều hình ảnh, bảng biểu trong `Figures/Buoi_02B/`. Tôi dự kiến sẽ chia cột 50:50 hoặc 60:40 để hiển thị hình ảnh ở cột phải và văn bản giải thích ở cột trái nhằm tối ưu hóa sự tập trung của sinh viên trên lớp.

---

## 3. Open Questions

- Script sinh mã cho Buổi 2 dự kiến sẽ mang tên `build_beamer_day02.py`.
- Tương tự như Buổi 1, sau khi Thầy duyệt kế hoạch này, tôi sẽ tiến hành viết Script sinh mã ngay lập tức.

---

## 4. Proposed Changes & Bố cục Phân chương Beamer (Sections & TOC)

### Cấu trúc 4 Sections trong Mục lục Động (`\tableofcontents`)
```latex
\section{1. Tiền mã hóa, Bitcoin \& Ứng dụng Blockchain trong Tài chính}
\section{2. Tài chính Phi tập trung (DeFi), NFT \& Vũ trụ Ảo (Metaverse)}
\section{3. Khoa học Dữ liệu \& Hệ sinh thái Dữ liệu Lớn (Big Data)}
\section{4. Quy trình Mô hình hóa \& Đánh giá Mô hình Học máy}
```

### Tiết 1 (45 Phút - 15 Frames): Tiền mã hóa, Bitcoin & Ứng dụng Blockchain
- **Mục tiêu:** Sinh viên hiểu bản chất của Bitcoin, hệ thống thanh toán điện tử ngang hàng, cách Tòa án Châu Âu (CJEU) nhìn nhận về tiền ảo, và cơ chế của mạng lưới Blockchain.
- **Nội dung các frames:**
  1. Trang bìa (`\titlepage` - Trường Đại học Đông Á)
  2. Mục lục nội dung chương (`\tableofcontents`)
  3. Mục tiêu bài học (LO 2.1 đến LO 2.5)
  4. Bitcoin: Hệ thống thanh toán điện tử mật mã
  5. Đặc tính phi tập trung (Decentralized) và Ngang hàng (Peer-to-peer)
  6. Bitcoin có phải là Tiền tệ hợp pháp? (Góc nhìn Pháp lý & CJEU)
  7. Lập luận của Tổng Biện lý: Phương tiện trao đổi vs. Công cụ lưu trữ giá trị
  8. Nghịch lý của Tiền mã hóa: Sự cần thiết của Trung gian Tài chính
  9. Tiền kỹ thuật số của Ngân hàng Trung ương (CBDC)
  10. Sổ cái Công khai Phân tán (Distributed Public Ledger) & Vai trò "Công chứng viên"
  11. Các rủi ro: Biến động giá (Volatility) và Thiếu cơ sở pháp lý
  12. Cuộc đua Tiền ảo: Litecoin, Ethereum, Zcash, Ripple
  13. Tính minh bạch & Có thể kiểm toán (Auditable) của Blockchain
  14. Chuỗi khối và AI trong Tài chính: Cặp bài trùng của tương lai
  15. Hợp đồng Thông minh (Smart Contracts) & Cố vấn Rô-bốt (Robo-advisors)

### Tiết 2 (45 Phút - 16 Frames): Tài chính Phi tập trung (DeFi), NFT & Vũ trụ Ảo (Metaverse)
- **Mục tiêu:** Sinh viên khám phá không gian tài chính mới (Metaverse, DeFi) và cách AI hỗ trợ việc định giá tài sản số, tự động hóa dịch vụ tài chính, và tạo nội dung NFT.
- **Nội dung các frames:**
  16. Giao dịch Thuật toán (Algorithmic Trading) do AI điều khiển
  17. Vũ trụ Ảo (Metaverse) trong Tài chính
  18. Bất động sản ảo, Nghệ thuật số & Mã thông báo (Tokens)
  19. Tài chính Phi tập trung (DeFi) trong Metaverse
  20. Fintech \& Ngân hàng Ảo (Virtual Banking)
  21. Tính tương tác (Interoperability) \& Bề mặt Tấn công mạng (Attack Surface)
  22. AI, Tài chính Phi tập trung (DeFi) \& Nghệ thuật NFT
  23. Vai trò của AI: Sáng tạo Nội dung \& Quản lý Đề xuất NFT
  24. Vấn đề Đạo đức \& Bản quyền trong Tác phẩm do AI tạo ra
  25. Giao thoa giữa DeFi và NFT: Sử dụng NFT làm Tài sản thế chấp
  26. Khoa học Dữ liệu (Data Science) - Bối cảnh & Sự thổi phồng
  27. **[SLIDE SONG SONG]** Biểu đồ Venn: Nhà Khoa học Dữ liệu (`Figure 6.2 Data scientist Venn diagram.jpeg`)
  28. Phân tích Kỹ năng: Toán học, Máy tính \& Chuyên môn Nghiệp vụ (Domain Expertise)
  29. Phân tích Dữ liệu (Data Analytics) vs. Khoa học Dữ liệu
  30. Trí tuệ Nhân tạo vs. Học máy vs. Học sâu
  31. **[SLIDE SONG SONG]** Biểu đồ Venn: AI, ML \& DL (`Figure 6.3 AI, machine learning, and deep learning Venn diagram.jpeg`)

### Tiết 3 (45 Phút - 17 Frames): Khoa học Dữ liệu, Big Data & Quy trình Mô hình hóa
- **Mục tiêu:** Sinh viên hiểu sâu về Vòng đời dự án Dữ liệu, 4 chữ V của Big Data, Ngăn xếp Công nghệ, các bước Phân tích khám phá (EDA) và Đánh giá hiệu suất Mô hình.
- **Nội dung các frames:**
  32. Những gì KHÔNG phải là Khoa học Dữ liệu?
  33. Dữ liệu lớn (Big Data) là gì?
  34. Đặc trưng 4 Chữ V của Big Data (Volume, Velocity, Variety, Veracity)
  35. **[SLIDE SONG SONG]** Vòng đời Dự án Khoa học Dữ liệu (`Figure 6.4 Data science project lifecycle.jpeg`)
  36. Bước 1: Định nghĩa Vấn đề (Ví dụ: Nợ quá hạn Khoản vay)
  37. **[SLIDE SONG SONG]** Bảng Phân loại Dữ liệu: Cấu trúc vs Phi Cấu trúc (`Table 6.1`)
  38. Các cấp độ của Dữ liệu (Granularity)
  39. Bước 3: Chuẩn bị Dữ liệu \& Kiểm tra Chất lượng (Data Quality Checks)
  40. Phân tích Dữ liệu Khám phá (EDA) \& Biến Mục tiêu
  41. Phân loại Bài toán Học máy: Có giám sát vs. Không giám sát
  42. Lựa chọn Mô hình (Hồi quy tuyến tính, Logistic, SVM)
  43. **[SLIDE SONG SONG]** Quy trình Mô hình hóa (`Figure 6.7 The modeling process.jpeg` - Huấn luyện, Xác thực, Kiểm thử)
  44. Phân tích Lỗi (Error Analysis): Độ lệch (Bias) và Phương sai (Variance)
  45. **[SLIDE SONG SONG]** Hiểu về Bias và Variance (`Figure 6.8 Understanding bias and variance.jpeg`)
  46. Ngăn xếp Công nghệ Dữ liệu lớn: Đưa dữ liệu vào (Kafka, Flume) \& Lưu trữ (Data Warehouse, Data Lake - Hadoop HDFS)
  47. Bài tập Tình huống Buổi 2: Xử lý dữ liệu nợ quá hạn
  48. Tổng kết Buổi 2 \& Dặn dò

---

## 5. Verification Plan (Kế hoạch Kiểm thử & Kiểm chứng)

### 1. Kiểm thử Biên dịch Tự động Beamer (Automated Beamer Build)
- Chạy lệnh biên dịch 2 lần trong thư mục `TaiLieu/slideAIAcc/` đối với file kịch bản của Buổi 2 (sau khi được tạo):
  ```bash
  pdflatex -synctex=1 -interaction=nonstopmode Slide_AIAcc_Day02.tex
  pdflatex -synctex=1 -interaction=nonstopmode Slide_AIAcc_Day02.tex
  ```
- Đảm bảo mã thoát thành công `Exit code 0`.

### 2. Kiểm chứng Chất lượng Trực quan Beamer
- Kiểm tra các slide song song chứa ảnh chụp từ `Figures/Buoi_02B/` (các sơ đồ Venn, quá trình Modeling, Bias-Variance) hiển thị rõ ràng, đúng tỷ lệ và không bị tràn khung chữ.
