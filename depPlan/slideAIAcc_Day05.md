# Kế hoạch Xây dựng Slide Bài giảng Buổi 5

## 1. Thông tin chung
- **Học phần:** Trí tuệ Nhân tạo Ứng dụng trong Kế toán (AI in Accounting)
- **Buổi học:** Buổi 5
- **Chủ đề chính:** Quản trị Rủi ro Quyết định & Phát triển Sản phẩm Mới (Chương 12 & 14)
- **Tài liệu nguồn:** `docs/buoi_05.md`
- **Tài liệu bổ trợ:** `TaiLieu/script/audioScript_Day05.txt`
- **Số lượng Slide dự kiến:** ~45 slides
- **Thời lượng:** 3 tiết (135 phút)
- **Kiến trúc:** Beamer LaTeX, Aspect Ratio 16:9, Theme Madrid, tiếng Việt (T5 encoding).

## 2. Mục tiêu Bài giảng
1. Nắm vững rủi ro trong quản lý chuỗi cung ứng (Backorder, Bullwhip effect) và cách giải quyết bằng Dữ liệu.
2. Hiểu cơ chế thuật toán Random Forest, xử lý dữ liệu mất cân bằng (Downsampling), cách đánh giá (AUC ROC, Sensitivity, Specificity).
3. Phân biệt Tương quan và Nhân quả trong phân tích kinh doanh.
4. Nắm vững phương pháp Thử nghiệm A/B, kiểm định thống kê (ANOVA, Giả thuyết Không) trong phát triển sản phẩm mới.

## 3. Tích hợp Ẩn dụ từ Audio Script
Slide sẽ lồng ghép các câu chuyện/ẩn dụ thực tế để làm mềm hóa kiến thức kỹ thuật:
- **Hiệu ứng chiếc roi da:** Ví dụ cơn sốt giấy vệ sinh - Sự thổi phồng hoảng loạn qua từng khâu chuỗi cung ứng.
- **Rừng ngẫu nhiên (Subspace Sampling):** 100 bác sĩ hội chẩn một ca bệnh, bị giấu một phần xét nghiệm để ép tư duy độc lập thay vì chỉ nhìn vào triệu chứng rõ nhất.
- **Gian lận bài thi:** Mô hình học máy bị "lười biếng" khi gặp dữ liệu mất cân bằng, đánh lụi 100% để lấy điểm Accuracy cao. (Cần Downsampling).
- **AUC ROC:** Bản điểm chấm năng lực "đánh hơi trúng bệnh" (Độ nhạy) và "không báo động nhầm" (Độ đặc hiệu).
- **Tương quan giả tạo & Thiên kiến tự chọn:** Ăn kem và cháy rừng; Giao diện game màu xanh nước biển và game thủ VIP.
- **Giả thuyết Không (Null Hypothesis):** Gã giám khảo cực kỳ bảo thủ, khoanh tay bĩu môi nói "Chẳng có sự khác biệt nào cả, tất cả chỉ là do ăn may".

## 4. Cấu trúc chi tiết (3 Tiết học)

### Tiết 1: Bất định trong Chuỗi Cung ứng & Cây Quyết định (Slide 04 - 17)
- **Slide 04 - 06:** Đặt vấn đề: Sự bất định trong kinh doanh (Đứt gãy chuỗi cung ứng smartphone).
- **Slide 07 - 09:** Tình trạng Chậm giao hàng (Backorder) và Thảm họa "Hiệu ứng chiếc roi da" (Bullwhip effect - Ví dụ giấy vệ sinh).
- **Slide 10 - 11:** Khái niệm Tập dữ liệu mất cân bằng (Imbalanced data) trong đứt gãy chuỗi cung ứng.
- **Slide 12 - 14:** Học máy: Cây quyết định (Decision Tree). Cơ chế hoạt động dựa trên các biến phân loại.
- **Slide 15 - 16:** Tính toán Độ vẩn đục Gini (Gini Impurity). Tích hợp `Figure 12.3` và `Figure 12.5`.
- **Slide 17:** Điểm yếu chí mạng của Cây quyết định đơn lẻ (Nhạy cảm, dễ bị đánh lừa bởi dữ liệu huấn luyện).

### Tiết 2: Rừng ngẫu nhiên (Random Forest) & Đánh giá Mô hình (Slide 18 - 32)
- **Slide 18 - 19:** Giải pháp: Rừng ngẫu nhiên. Cơ chế Bootstrap Aggregation (Bagging).
- **Slide 20 - 22:** Lấy mẫu không gian con (Subspace Sampling) - Ẩn dụ "100 bác sĩ hội chẩn".
- **Slide 23 - 25:** Căn bệnh "lười biếng" của mô hình khi gặp dữ liệu mất cân bằng (Đoán bừa để lấy Accuracy cao).
- **Slide 26 - 28:** Phương pháp Lấy mẫu giảm (Downsampling) - Ép mô hình vào chân tường để học thật sự. Tích hợp `Figure 12.6`.
- **Slide 29 - 30:** Các chỉ số đánh giá mới: Độ nhạy (Sensitivity - Bắt đúng bệnh) và Độ đặc hiệu (Specificity - Không báo động nhầm).
- **Slide 31 - 32:** Bảng điểm thực sự: Đường cong ROC và chỉ số AUC. Vì sao Accuracy trở nên vô nghĩa?

### Tiết 3: Phát triển Sản phẩm Mới & Thử nghiệm A/B (Slide 33 - 45)
- **Slide 33 - 34:** Chuyển giao: Rủi ro nội bộ từ các quyết định chủ quan (Đổi tính năng, giao diện game mới).
- **Slide 35 - 37:** Cạm bẫy Thống kê: Tương quan giả tạo (Ăn kem - Cháy rừng) & Thiên kiến tự chọn (Màu xanh - Game thủ VIP).
- **Slide 38 - 39:** Thử nghiệm nhân quả: A/B Testing. Sức mạnh của Sự phân bổ ngẫu nhiên (Randomization) để triệt tiêu nhiễu.
- **Slide 40 - 41:** Giả thuyết Không (Null Hypothesis) - "Gã giám khảo bảo thủ".
- **Slide 42 - 44:** Phân tích Phương sai (ANOVA) và Kiểm định F (F-Test). Cân đo sự chênh lệch giữa các nhóm so với sự chênh lệch nội bộ.
- **Slide 45:** Sức mạnh của P-value (< 0.05) - Đánh bại sự hoài nghi và Ra quyết định tự tin.

## 5. Danh sách Hình ảnh (Figures) Cần Tích hợp
- `../Figures/Buoi_05A/Figure 12.1 Bullwhip Effect.jpeg`
- `../Figures/Buoi_05A/Figure 12.3 Gini Index Calculation.jpeg`
- `../Figures/Buoi_05A/Figure 12.5 Decision Tree Splits.jpeg`
- `../Figures/Buoi_05A/Figure 12.6 Data Imbalance.jpeg`
- Hình ảnh/Sơ đồ từ `Buoi_05B` (như quy trình phát triển sản phẩm).

## 6. Lộ trình Triển khai
1. Nhận phản hồi/phê duyệt từ User cho kế hoạch này.
2. Viết file `build_beamer_day05.py` tự động sinh mã LaTeX 16:9 Madrid.
3. Thực thi script, biên dịch qua `pdflatex` 2 lần.
4. Kiểm thử kết quả PDF và báo cáo.
