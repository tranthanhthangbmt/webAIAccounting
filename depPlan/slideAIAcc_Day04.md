# Kế hoạch Thiết kế và Làm lại Bộ Slide Bài giảng Buổi 4 (Chuẩn Beamer 16:9)

**Thư mục mục tiêu:** `webAIAccounting/TaiLieu/slideAIAcc/`  
**Định dạng thiết kế:** **LaTeX Beamer Widescreen 16:9** (`\documentclass[aspectratio=169]{beamer}`)  
**Theme \& Colortheme:** `Madrid` theme, `default` color theme (Kế thừa từ kiến trúc Buổi 1, 2 và 3)  
**File nguồn nội dung:** 
- `docs/buoi_04.md` (Chương 5: Phân khúc thị trường \& Chương 10: Dự báo sức khỏe tài chính)
- `TaiLieu/script/audioScript_Day04.txt` (Dùng để lấy ví dụ chuyên sâu: Tiệc thực khách k-Means, 5 cái GPS nhiễu loạn cho Đa cộng tuyến).  
**Thư mục hình ảnh:** 
- `Figures/Buoi_04A/` (Hình 5.1 -> 5.7 về k-Means, k-Medoid, Phân khúc)
- `Figures/Buoi_04B/` (Hình 10.1 -> 10.4 về Đa cộng tuyến, ROC AUC)  
**Thời lượng chuẩn đại học:** 3 Tiết học (135 Phút giảng dạy \& thảo luận)  
**Quy mô dự kiến:** **45-50 Frames (Slides) chi tiết**

---

## 1. Goal Description (Mục tiêu Kỹ thuật \& Sư phạm)

Buổi 4 đánh dấu sự chuyển mình từ lý thuyết chung sang **các thuật toán thực chiến (hands-on algorithms)**:
1. **Phần 1 (Chương 5):** Học không giám sát (Unsupervised Learning). Ứng dụng phân cụm (Clustering) để phân khúc khách hàng tiềm năng. Điển hình là thuật toán **k-Means** và **k-Medoid**.
2. **Phần 2 (Chương 10):** Đánh giá sức khỏe tài chính và dự báo phá sản. Xử lý triệt để căn bệnh "Đa cộng tuyến" (Multicollinearity) của các chỉ số tài chính bằng **Hồi quy có phạt (Penalized Regression - mô hình LASSO)**.

**Mục tiêu thiết kế Slide:**
- Tiếp tục chia làm 3 Sections (mỗi Section tương ứng 1 tiết 45 phút).
- Tích hợp các câu chuyện/ví dụ sinh động từ Audio Script:
  - So sánh thuật toán k-Means với việc *sắp xếp bàn tiệc cho nhóm khách hàng (đo khoảng cách và dời tâm cụm liên tục)*.
  - So sánh Đa cộng tuyến (Multicollinearity) trong dữ liệu Kế toán với việc *lái xe mà có 5 cái GPS cùng gào thét chỉ đường gây nhiễu loạn*.
- Tận dụng tối đa các hình ảnh (Figure 5.4, 10.2, 10.4) bằng cách dùng code LaTeX `\begin{columns}` để chia slide thành 2 phần: chữ bên trái, hình bên phải.
- Có kèm theo trích đoạn code R minh họa ngắn gọn từ tài liệu (gói `cluster`, `factoextra`, `glmnet`).

---

## 2. Bố cục Phân chương Beamer dự kiến (Sections \& TOC)

### Mục lục Động (`\tableofcontents`)
```latex
\section{1. Phân khúc Khách hàng \& Học không giám sát (Unsupervised Learning)}
\section{2. Thuật toán k-Means, k-Medoid \& Hệ số Silhouette}
\section{3. Dự báo Phá sản, Đa cộng tuyến \& Hồi quy LASSO (Penalized Regression)}
```

### Tiết 1 (45 Phút - Khoảng 16 Frames): Phân khúc Khách hàng \& Học không giám sát
- **Mục tiêu:** Sinh viên hiểu vì sao không thể Marketing đại trà và hiểu bản chất của Học không giám sát (không có nhãn).
- **Nội dung chính:**
  1. Trang bìa \& Mục lục.
  2. Mục tiêu bài học (LO 4.1 -> 4.4).
  3. Case study dẫn nhập: Nhà hàng Vegan-Always tại Phoenix (Không phát Voucher đại trà).
  4. Khái niệm Phân khúc thị trường (Market Segmentation) \& Vi phân khúc (Microsegments).
  5. Phân khúc động (Dynamic Segmentation): Khách hàng hôm nay ăn sô-cô-la đen, ngày mai có thể đổi khẩu vị.
  6. **Khái niệm Học không giám sát:** Bộ dữ liệu hỗn độn, không có nhãn (Unlabeled Data).
  7. Mục đích của Học không giám sát: Tự động mò mẫm, tìm ra cấu trúc ẩn bằng Phân cụm (Clustering).

### Tiết 2 (45 Phút - Khoảng 18 Frames): Thuật toán k-Means, k-Medoid \& Hệ số Silhouette
- **Mục tiêu:** Đi sâu vào cơ chế toán học của việc đo khoảng cách, dời tâm cụm và lập trình R cơ bản.
- **Nội dung chính:**
  1. Mối quan hệ giữa Khoảng cách và Sự Tương đồng (Khoảng cách ngắn = Hành vi giống nhau).
  2. \textbf{[Ví dụ Audio Script]} Bữa tiệc lộn xộn \& Thuật toán k-Means: Đặt k cái bàn $\rightarrow$ Khách xúm lại $\rightarrow$ Dời bàn vào trung tâm $\rightarrow$ Lặp lại đến khi ổn định.
  3. Cấu trúc lặp của k-Means: Gán điểm (Assign) $\rightarrow$ Cập nhật tâm (Update Centroid).
  4. Hạn chế của k-Means: Dễ bị nhiễu (Outliers).
  5. Giải pháp k-Medoid: Dùng điểm dữ liệu thực tế làm tâm thay vì giá trị trung bình.
  6. **Câu hỏi:** Làm sao biết k bằng bao nhiêu? $\rightarrow$ Giới thiệu Hệ số Silhouette (Đánh giá độ chặt chẽ của cụm).
  7. Ứng dụng Kế toán: Nhóm 1 (Gắn bó lâu nhưng chi ít) vs Nhóm 2 (Gắn bó lâu, chi nhiều).
  8. Code R cơ bản: `kmeans(df, centers = 3, nstart = 25)`.
  9. \textbf{[Slide 2 cột]} Biểu đồ k-Means Segmentation Plot (Figure 5.4).

### Tiết 3 (45 Phút - Khoảng 16 Frames): Dự báo Phá sản, Đa cộng tuyến \& Hồi quy LASSO
- **Mục tiêu:** Áp dụng AI để bảo vệ sức khỏe tài chính doanh nghiệp; khắc phục điểm yếu của Hồi quy cổ điển.
- **Nội dung chính:**
  1. Tầm quan trọng của Dự báo sức khỏe tài chính (Góc nhìn của Người cho vay như Ngân hàng Altra).
  2. Các chỉ số tài chính phổ biến: Nợ/Vốn chủ sở hữu, Tỷ lệ thanh toán hiện hành.
  3. Vấn đề "Đa cộng tuyến" (Multicollinearity) là gì?
  4. \textbf{[Ví dụ Audio Script]} 5 chiếc máy GPS: Đa cộng tuyến giống như 5 chiếc GPS cùng chỉ đường gây nhiễu loạn cho OLS truyền thống.
  5. \textbf{[Slide 2 cột]} Biểu đồ tương quan (Figure 10.2). Phát hiện tỷ lệ có tương quan $> 0.9$.
  6. Hậu quả của Đa cộng tuyến: Tăng sai số chuẩn, báo động nhầm (Dương tính giả).
  7. **Giải pháp AI:** Hồi quy có phạt (Penalized Regression) $\rightarrow$ Mô hình LASSO.
  8. Cách LASSO trừng phạt dữ liệu: Ép các hệ số (Beta) của biến gây nhiễu về đúng bằng 0 (Tự động lựa chọn biến).
  9. Đánh giá Mô hình: Đường cong AUC ROC (Tỷ lệ True Positive vs False Positive).
  10. \textbf{[Slide 2 cột]} Đồ thị AUC ROC Curve (Figure 10.4) đạt mức 0.8.
  11. \textbf{Tổng kết:} Sự va chạm giữa "Trực giác Kế toán trưởng 20 năm" và "Thuật toán Big Data". Ai sẽ thắng?

---

## 3. User Review Required (Các điểm cần Thầy xác nhận)

> [!IMPORTANT]
> **Về việc tích hợp Audio Script:**  
> Tôi đã đọc kỹ `TaiLieu/script/audioScript_Day04.txt` và rút ra 2 ví dụ cực kỳ sư phạm: (1) Sắp xếp bàn tiệc cho k-Means, (2) Lái xe với 5 máy GPS cho Đa cộng tuyến. Tôi sẽ đưa các ví dụ hình tượng này vào các slide text để Giảng viên dễ diễn giải trên lớp. Thầy thấy cách tiếp cận này ổn chứ?

> [!NOTE]
> **Về Code R trong Slide:**  
> Vì màn hình máy chiếu có hạn, tôi sẽ chỉ cắt trích đoạn code R cốt lõi (ví dụ hàm `kmeans()` và hàm dựng mô hình LASSO `cv.glmnet`) vào slide để minh họa, không đưa toàn bộ data preprocessing dài dòng vào slide để tránh loãng nội dung.

---

## 4. Verification Plan (Kế hoạch Kiểm thử \& Kiểm chứng)

- Sau khi Thầy duyệt kế hoạch, tôi sẽ tạo `build_beamer_day04.py`.
- Tự động lấy các đường dẫn hình ảnh từ `../../Figures/Buoi_04A/` và `../../Figures/Buoi_04B/`.
- Thực thi `pdflatex` 2 lần và kiểm tra mã thoát (Exit code 0).
- Tạo báo cáo cập nhật tiến độ vào `walkthrough.md`.
