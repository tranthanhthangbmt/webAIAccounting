# -*- coding: utf-8 -*-
"""
Builder for Paper 2:
Financial Distress and Earnings Prediction using Deep Learning
(Yongliang Sun - Procedia Computer Science, Elsevier, 2024)
"""

import os
from generate_day02_helpers import get_html_template

PAPERS_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day02_Extra\papers"

TITLE_VI = "Dự Báo Kiệt Quệ Tài Chính Doanh Nghiệp Dựa Trên Mô Hình Học Sâu (Deep Autoencoder & Phân Loại)"
TITLE_EN = "Financial Distress and Earnings Prediction using Deep Learning"
AUTHORS = "Yongliang Sun (Dongying Vocational Institute, Trung Quốc)"
JOURNAL = "Procedia Computer Science 243 (2024) 1069–1078, Elsevier"
DOI = "10.1016/j.procs.2024.09.127"
BADGE = "Paper 2 • Elsevier Procedia 2024"

def build():
    # Markdown Content
    md_content = """# DỰ BÁO KIỆT QUỆ TÀI CHÍNH DOANH NGHIỆP DỰA TRÊN MÔ HÌNH HỌC SÂU (DEEP AUTOENCODER & PHÂN LOẠI)
*(Financial Distress and Earnings Prediction using Deep Learning)*

- **Tác giả:** Yongliang Sun (Dongying Vocational Institute, Trung Quốc)
- **Tạp chí xuất bản:** Procedia Computer Science 243 (2024) 1069–1078, Elsevier
- **Định danh DOI:** [10.1016/j.procs.2024.09.127](https://doi.org/10.1016/j.procs.2024.09.127)
- **Mẫu thực nghiệm:** 465 công ty niêm yết cổ phiếu hạng A tại sàn Thượng Hải & Thâm Quyến (2001–2018) bị cảnh báo đặc biệt (ST) và 2.325 công ty đối chứng Non-ST

---

## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

Để giải quyết triệt để hạn chế của các mô hình dự báo truyền thống trong việc mô tả nguyên nhân và cơ chế dẫn đến khủng hoảng tài chính doanh nghiệp, bài báo này ứng dụng **mô hình học sâu (*Deep Learning*)** đa tầng nhằm nâng cao hiệu quả dự báo kiệt quệ tài chính (*Financial Distress*). Nghiên cứu lựa chọn 465 công ty niêm yết cổ phiếu hạng A (ngành phi tài chính) tại sàn Thượng Hải và Thâm Quyến từ năm 2001 đến năm 2018 bị đưa vào diện cảnh báo đặc biệt (*Special Treatment - ST*) lần đầu do tình trạng tài chính bất thường, cùng 2.325 công ty đối chứng không bị ST (*Non-ST*).

Một hệ thống 23 chỉ số tài chính toàn diện thuộc 5 khía cạnh cốt lõi (Khả năng thanh toán, Năng lực hoạt động, Năng lực sinh lời, Tiềm năng phát triển và Lưu chuyển tiền tệ) được xây dựng. Mô hình học sâu kết hợp giữa **học đặc trưng phi giám sát (*Unsupervised Feature Learning*) qua 4 tầng mã hóa (Encoder)** và **tầng phân loại (*Classifier*) có giám sát** được tối ưu hóa bằng thuật toán lan truyền ngược (BP). Kết quả kiểm thử ngoài mẫu cho thấy mô hình học sâu đạt **độ chính xác tổng thể 78,33%** và đặc biệt đạt **độ chính xác dự báo các công ty lâm vào kiệt quệ (ST) lên tới 82,00%**, vượt trội hơn hẳn mô hình Hồi quy Logistic (71,00%) và mô hình Mạng nơ-ron nhân tạo truyền thống (69,67%).

**Từ khóa:** Học sâu (Deep Learning); Công ty niêm yết; Dự báo kiệt quệ tài chính; Cảnh báo đặc biệt (ST); Mạng nơ-ron đa tầng (Deep Neural Network).

---

## 1. ĐẶT VẤN ĐỀ & BỐI CẢNH NGHIÊN CỨU

Doanh nghiệp luôn phải đối mặt với vô vàn rủi ro trong quá trình vận hành, trong đó **rủi ro tài chính (*financial risk*)** là loại rủi ro nguy hiểm và tất yếu nhất. Một khi doanh nghiệp rơi vào khủng hoảng tài chính, nó sẽ gây ra tổn thất nặng nề cho các cổ đông, nhà đầu tư, chủ nợ, người lao động và làm lung lay tính ổn định của thị trường vốn.

Trong thực tế, tình trạng kiệt quệ tài chính không diễn ra sau một đêm, mà hầu hết các công ty đều trải qua một **quá trình suy thoái dần dần (*gradual deterioration*)**. Do đó, nếu có thể kịp thời nhận diện các tín hiệu cảnh báo suy thoái từ sớm (trước 2–3 năm), ban quản trị doanh nghiệp sẽ có cơ hội tái cấu trúc dòng tiền, ngân hàng có thể kiểm soát rủi ro tín dụng và kiểm toán viên có thể đưa ra ý kiến cảnh báo phù hợp về giả định hoạt động liên tục (*going concern*).

### Hạn Chế Của Các Mô Hình Kinh Điển (Beaver, Altman, Ohlson):
- Các mô hình phân tích biệt thức (Altman Z-Score) và hồi quy Logit (Ohlson O-Score) dựa trên giả định quan hệ tuyến tính giữa các biến số.
- Khi các tỷ số tài chính bị méo mó do biến động chu kỳ hoặc do hành vi làm đẹp sổ sách, các mô hình thống kê truyền thống dễ bị sai lệch dấu hồi quy và bỏ sót các doanh nghiệp đang trên bờ vực phá sản.

---

## 2. KIẾN TRÚC MÔ HÌNH HỌC SÂU ĐA TẦNG (DEEP LEARNING ARCHITECTURE)

Mô hình được thiết kế theo cấu trúc gồm hai giai đoạn:
1. **Giai đoạn học đặc trưng không giám sát (*Feature Learning*):** Ánh xạ véc-tơ 23 chỉ số tài chính đa chiều qua chuỗi 4 tầng ẩn Encoder (Encoder 1, Encoder 2, Encoder 3, Encoder 4) để nén dữ liệu và tự động trích xuất các mối quan hệ phi tuyến ngầm.
2. **Giai đoạn phân loại có giám sát (*Supervised Classification*):** Đưa véc-tơ đặc trưng nén vào tầng phân loại đầu ra để dự đoán xác suất công ty bị ST (nhãn 1) hoặc Non-ST (nhãn 0).

![Hình 1: Kiến trúc mô hình Học sâu](figures_paper2/fig1_model_arch_cropped.png)
*Hình 1: Kiến trúc mô hình học sâu dự báo kiệt quệ tài chính gồm Tầng đầu vào (23 chỉ số), các tầng mã hóa ẩn (Encoder 1 -> Encoder 4) và Tầng phân loại đầu ra.*

### Công thức ánh xạ tầng ẩn:
Tập huấn luyện $D = \{(x_1, y_1), (x_2, y_2), \dots, (x_m, y_m)\}$, với $x_i \in \mathbb{R}^{23}$ và $y_i \in \{0, 1\}$. Đầu ra của tầng ẩn thứ nhất:
$$ F_1^p = f\left( \sum_{i=1}^d \omega_i^p x_i + b_p \right) $$
Trong đó $f(\cdot)$ là hàm kích hoạt phi tuyến tính, $\omega$ là ma trận trọng số, $b$ là độ lệch bias. Quá trình tối ưu hóa giảm thiểu hàm mất mát sai số toàn phương trung bình (MSE) qua thuật toán lan truyền ngược.

---

## 3. HỆ THỐNG 23 CHỈ TIÊU TÀI CHÍNH TOÀN DIỆN

Sau khi sàng lọc và loại bỏ các biến số thiếu hụt dữ liệu, hệ thống 23 chỉ số tài chính được hoàn thiện thuộc 5 trụ cột:

| STT | Trụ Cột Tài Chính | Mã Chỉ Số | Tên Chỉ Số Tài Chính | Ý Nghĩa Kinh Tế |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Khả năng thanh toán** | `X1` | Tỷ số thanh toán hiện hành (Current Ratio) | Đo lường khả năng trang trải nợ ngắn hạn |
| 2 | | `X2` | Tỷ số thanh toán nhanh (Quick Ratio) | Khả năng thanh toán tức thời không tính tồn kho |
| 3 | | `X3` | Tỷ số nợ trên tổng tài sản (Debt to Assets) | Mức độ đòn bẩy tài chính và rủi ro vỡ nợ |
| 4 | | `X4` | Tỷ số nợ trên vốn CSH (Debt to Equity) | Cơ cấu tài trợ vốn của doanh nghiệp |
| 5 | | `X5` | Vốn lưu động trên tổng tài sản | Đệm thanh khoản ngắn hạn |
| 6 | **Năng lực hoạt động** | `X6` | Vòng quay khoản phải thu (Receivables Turnover) | Hiệu quả thu hồi công nợ bán hàng |
| 7 | | `X7` | Vòng quay hàng tồn kho (Inventory Turnover) | Tốc độ giải phóng hàng hóa trong kho |
| 8 | | `X8` | Vòng quay vốn lưu động | Hiệu quả luân chuyển tài sản ngắn hạn |
| 9 | | `X9` | Vòng quay tài sản cố định | Mức độ khai thác máy móc nhà xưởng |
| 10 | | `X10` | Vòng quay tổng tài sản (Total Assets Turnover) | Năng lực tạo doanh thu từ toàn bộ tài sản |
| 11 | **Năng lực sinh lời** | `X11` | Tỷ suất lợi nhuận trên tài sản (ROA) | Khả năng sinh lời của toàn bộ tài sản |
| 12 | | `X12` | Tỷ suất sinh lời trên vốn CSH (ROE) | Hiệu quả sử dụng vốn của cổ đông |
| 13 | | `X13` | Tỷ suất lợi nhuận gộp (Gross Margin) | Sức mạnh định giá và kiểm soát giá vốn |
| 14 | | `X14` | Biên lợi nhuận hoạt động | Hiệu quả từ hoạt động kinh doanh cốt lõi |
| 15 | | `X15` | Tỷ suất lợi nhuận trên tổng chi phí | Khả năng kiểm soát chi phí hoạt động |
| 16 | **Tiềm năng phát triển** | `X16` | Tốc độ tăng trưởng doanh thu thuần | Tiềm năng mở rộng thị phần |
| 17 | | `X17` | Tốc độ tăng trưởng lợi nhuận hoạt động | Động lực gia tăng lợi nhuận cốt lõi |
| 18 | | `X18` | Tốc độ tăng trưởng tổng tài sản | Tốc độ mở rộng quy mô doanh nghiệp |
| 19 | | `X19` | Tốc độ tăng trưởng vốn chủ sở hữu | Năng lực tích lũy tái đầu tư |
| 20 | | `X20` | Tốc độ tăng trưởng EPS | Lợi ích gia tăng trên mỗi cổ phần |
| 21 | **Lưu chuyển tiền tệ** | `X21` | Dòng tiền thuần từ HĐKD trên tổng tài sản | Chất lượng dòng tiền từ hoạt động chính |
| 22 | | `X22` | Dòng tiền HĐKD trên nợ phải trả | Năng lực trả nợ bằng tiền thật |
| 23 | | `X23` | Dòng tiền HĐKD trên doanh thu thuần | Khả năng biến doanh thu thành tiền mặt |

---

## 4. DỮ LIỆU THỰC NGHIỆM & QUY TRÌNH HUẤN LUYỆN

- **Mẫu ST:** 465 công ty phi tài chính tại sàn Thượng Hải & Thâm Quyến giai đoạn 2001–2018 bị đưa vào diện ST lần đầu (chứng minh tình trạng lỗ liên tiếp hoặc vốn CSH âm).
- **Mẫu Non-ST:** 2.325 công ty không bị ST trong toàn bộ chu kỳ nghiên cứu (tỷ lệ ghép mẫu 1:5 tương đồng về ngành nghề và quy mô).
- **Mẫu kiểm thử ngoài mẫu (Test Set):** 300 công ty (50 công ty ST và 250 công ty Non-ST) hoàn toàn độc lập, lấy số liệu tại thời điểm **T-3 (trước khi bị ST đúng 3 năm)** để kiểm chứng năng lực cảnh báo sớm.

![Hình 2 & 3: Quá trình huấn luyện tham số](figures_paper2/fig2_3_training_rmse.png)
*Hình 2 & 3: Đường cong hội tụ sai số RMSE qua các vòng huấn luyện (epochs) của mạng học sâu. Mô hình đạt trạng thái ổn định tối ưu sau 400 epochs.*

---

## 5. KẾT QUẢ THỰC NGHIỆM & ĐỐI CHIẾU SO SÁNH ĐA MÔ HÌNH

### Bảng So Sánh Hiệu Năng Dự Báo Giữa 3 Mô Hình (Bảng 8 trong bài báo gốc):
Kết quả kiểm tra tại thời điểm T-3 trên 300 công ty mẫu thử nghiệm độc lập:

| Mô Hình Đánh Giá | Nhóm Doanh Nghiệp | Dự Báo Đúng | Dự Báo Sai | Độ Chính Xác (%) |
| :--- | :--- | :--- | :--- | :--- |
| **Mô hình Học Sâu (Deep Learning)** | **Công ty Non-ST** (250 công ty) | **194** | 56 | **77,60%** |
| | **Công ty ST (Kiệt quệ)** (50 công ty) | **41** | 9 | **82,00%** |
| | **Tổng thể mô hình** (300 công ty) | **235** | 65 | **78,33%** |
| **Mô hình Hồi quy Logistic** | Công ty Non-ST (250 công ty) | 176 | 74 | 70,40% |
| | Công ty ST (Kiệt quệ) (50 công ty) | 37 | 13 | 74,00% |
| | Tổng thể mô hình (300 công ty) | 213 | 87 | 71,00% |
| **Mô hình Mạng BP Neural Network** | Công ty Non-ST (250 công ty) | 174 | 76 | 69,60% |
| | Công ty ST (Kiệt quệ) (50 công ty) | 35 | 15 | 70,00% |
| | Tổng thể mô hình (300 công ty) | 209 | 91 | 69,67% |

### 📊 Phân Tích Ý Nghĩa Kết Quả:
1. **Độ chính xác vượt trội:** Mô hình Học sâu đạt độ chính xác chung **78,33%**, cao hơn mô hình Logistic **+7,33%** và cao hơn mạng BP nơ-ron nông **+8,66%**.
2. **Khả năng bắt trúng doanh nghiệp sắp phá sản:** Đối với các công ty sắp bị cảnh báo ST, Học sâu nhận diện chính xác **82,00%** (bắt đúng 41/50 công ty), trong khi Logistic chỉ đạt 74,00% và BP-ANN chỉ đạt 70,00%. Điều này giảm thiểu nguy cơ bỏ sót doanh nghiệp kiệt quệ xuống mức rất thấp (chỉ bỏ sót 9 công ty).
3. **Cảnh báo sớm trước 3 năm (T-3):** Việc mô hình đạt độ chính xác hơn 82% tại thời điểm 3 năm trước khi biến cố ST chính thức diễn ra chứng minh rằng các tầng Encoder đã tự động học được "quỹ đạo suy thoái" tiềm ẩn từ các chỉ số tài chính kết hợp.

---

## 6. Ý NGHĨA ỨNG DỤNG CHO KIỂM TOÁN VIÊN & KẾ TOÁN QUẢN TRỊ

> [!IMPORTANT]
> **Đóng góp thiết thực cho công tác Kiểm toán & Quản trị rủi ro:**
> - **Đánh giá Khả năng Hoạt động Liên tục (Going Concern):** Theo chuẩn mực kiểm toán quốc tế ISA 570, kiểm toán viên có trách nhiệm thu thập đầy đủ bằng chứng thích hợp về tính hợp lý của giả định hoạt động liên tục. Mô hình Học sâu đóng vai trò công cụ hỗ trợ định lượng khách quan, đưa ra cảnh báo sớm trước 3 năm với độ tin cậy 82%.
> - **Cảnh báo sớm cho Kế toán Quản trị:** Giúp CFO và Ban Giám đốc chủ động cắt giảm chi phí, thu hồi công nợ và cơ cấu lại các khoản nợ vay trước khi doanh nghiệp rơi vào tình trạng mất thanh khoản hoàn toàn.

---

## 7. TÀI LIỆU THAM KHẢO CHÍNH (REFERENCES)

1. **Beaver, W. H. (1966).** Financial ratios as predictors of failure. *Journal of Accounting Research*, 4, 71–111.
2. **Altman, E. I. (1968).** Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. *The Journal of Finance*, 23(4), 589–609.
3. **Ohlson, J. A. (1980).** Financial ratios and the probabilistic prediction of bankruptcy. *Journal of Accounting Research*, 18(1), 109–131.
4. **Sun, Y. (2024).** Financial distress prediction based on deep learning model. *Procedia Computer Science*, 243, 1069–1078.
"""

    md_path = os.path.join(PAPERS_DIR, "paper_2_Financial_Distress_Prediction_tiengviet.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Markdown: {os.path.basename(md_path)}")

    # Generate HTML
    sidebar_links = """
      <a href="#abstract" class="sidebar-link">Tóm Tắt Nghiên Cứu</a>
      <a href="#sec1" class="sidebar-link">1. Đặt Vấn Đề & Bối Cảnh</a>
      <a href="#sec2" class="sidebar-link">2. Kiến Trúc Mô Hình Học Sâu</a>
      <a href="#sec3" class="sidebar-link">3. Hệ Thống 23 Chỉ Số Tài Chính</a>
      <a href="#sec4" class="sidebar-link">4. Dữ Liệu Thực Nghiệm (ST)</a>
      <a href="#sec5" class="sidebar-link">5. Kết Quả Định Lượng So Sánh</a>
      <a href="#sec6" class="sidebar-link">6. Đúc Kết Cho Kiểm Toán Viên</a>
      <a href="#sec7" class="sidebar-link">7. Tài Liệu Tham Khảo</a>
    """

    content_html = f"""
      <!-- Abstract Box -->
      <section id="abstract" class="abstract-box">
        <div class="abstract-heading">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
          </svg>
          TÓM TẮT NGHIÊN CỨU (ABSTRACT)
        </div>
        <p class="abstract-text">
          Nhằm giải quyết hạn chế của các mô hình truyền thống trong việc mô tả nguyên nhân khủng hoảng tài chính, nghiên cứu này ứng dụng <strong>mô hình học sâu (Deep Learning)</strong> đa tầng để nâng cao hiệu quả dự báo kiệt quệ tài chính (<em>Financial Distress</em>). Nghiên cứu lựa chọn 465 công ty niêm yết cổ phiếu hạng A tại sàn Thượng Hải & Thâm Quyến (2001–2018) bị cảnh báo đặc biệt (<em>Special Treatment - ST</em>) lần đầu, cùng 2.325 công ty đối chứng Non-ST. Hệ thống 23 chỉ số tài chính được xây dựng trên 5 khía cạnh cốt lõi. Mô hình kết hợp 4 tầng ẩn Encoder để học đặc trưng phi giám sát và tầng phân loại có giám sát. Kết quả kiểm nghiệm tại thời điểm <strong>T-3 (trước biến cố 3 năm)</strong> khẳng định mô hình học sâu đạt <strong>độ chính xác chung 78,33%</strong> và độ chính xác dự báo công ty kiệt quệ lên tới <strong>82,00%</strong>, vượt trội so với Hồi quy Logistic (71,00%) và Mạng BP nơ-ron truyền thống (69,67%).
        </p>
        <div class="keywords-box">
          <strong>Từ khóa:</strong> Deep Learning; Listed Company; Prediction of Financial Distress; Special Treatment (ST); Autoencoder; Backpropagation.
        </div>
      </section>

      <!-- Section 1 -->
      <section id="sec1">
        <h2 class="section-title"><span class="section-number">1</span> ĐẶT VẤN ĐỀ & BỐI CẢNH NGHIÊN CỨU</h2>
        <p>Doanh nghiệp trong nền kinh tế thị trường cạnh tranh khốc liệt luôn đối mặt với nhiều rủi ro, trong đó <strong>rủi ro tài chính</strong> là rủi ro mang tính sống còn. Khi một doanh nghiệp rơi vào khủng hoảng tài chính, nó sẽ kéo theo tổn thất to lớn cho các nhà đầu tư, chủ nợ, hệ thống ngân hàng và làm giảm sút tính ổn định của thị trường chứng khoán.</p>
        
        <p>Phần lớn các doanh nghiệp không sụp đổ đột ngột mà trải qua một <em>quá trình suy thoái tài chính tích tụ dần dần</em>. Do đó, việc xây dựng mô hình cảnh báo sớm có khả năng "bắt bệnh" trước 3 năm giúp nhà quản trị kịp thời xoay chuyển tình thế, đồng thời hỗ trợ kiểm toán viên đưa ra phán đoán chính xác về tính hoạt động liên tục (Going Concern).</p>

        <div class="callout callout-info">
          <div class="callout-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="16" x2="12" y2="12"></line>
              <line x1="12" y1="8" x2="12.01" y2="8"></line>
            </svg>
            Khái niệm Công ty ST (Special Treatment):
          </div>
          <p style="margin-bottom:0;">Tại thị trường chứng khoán Trung Quốc, quy chế Cảnh báo đặc biệt (ST) được áp dụng bắt buộc đối với các công ty niêm yết có tình trạng tài chính bất thường (ví dụ: lỗ ròng 2 năm liên tiếp hoặc vốn chủ sở hữu thấp hơn vốn điều lệ). Đây là chỉ báo thực nghiệm chuẩn mực nhất cho tình trạng kiệt quệ tài chính trước khi doanh nghiệp bị hủy niêm yết hoặc phá sản.</p>
        </div>
      </section>

      <!-- Section 2 -->
      <section id="sec2">
        <h2 class="section-title"><span class="section-number">2</span> KIẾN TRÚC MÔ HÌNH HỌC SÂU ĐA TẦNG</h2>
        <p>Mô hình được cấu trúc thành hệ thống đa cấp: Tầng đầu vào tiếp nhận 23 chỉ tiêu tài chính, đi qua 4 tầng ẩn Encoder để nén và học đặc trưng không giám sát, sau đó chuyển sang tầng phân loại đầu ra:</p>

        <!-- Figure 1 -->
        <div class="figure-wrapper">
          <div class="figure-header">
            <span>KIẾN TRÚC MẠNG NƠ-RON HỌC SÂU DỰ BÁO TÀI CHÍNH</span>
            <span class="figure-badge">Hình 1</span>
          </div>
          <div class="figure-img-container">
            <img src="figures_paper2/fig1_model_arch_cropped.png" alt="Hình 1: Kiến trúc mô hình Học sâu" class="figure-img" />
          </div>
          <div class="figure-caption">
            <strong>Hình 1:</strong> Luồng xử lý của mô hình: Dữ liệu tài chính 23 chiều &rarr; Encoder 1 &rarr; Encoder 2 &rarr; Encoder 3 &rarr; Encoder 4 &rarr; Classifier &rarr; Dự đoán nhị phân (ST / Non-ST).
          </div>
        </div>

        <p>Công thức biểu diễn toán học tại mỗi tầng ẩn $p$:</p>
        <div class="formula-box">
          F<sub>1</sub><sup>p</sup> = f( &Sigma;<sub>i=1..d</sub> &omega;<sub>i</sub><sup>p</sup> x<sub>i</sub> + b<sub>p</sub> )
        </div>
        <p>Trong đó $\omega$ là ma trận trọng số liên kết, $b$ là độ lệch bias, $f(\cdot)$ là hàm kích hoạt phi tuyến tính. Quá trình học sử dụng thuật toán lan truyền ngược (Backpropagation) để liên tục điều chỉnh trọng số nhằm giảm thiểu sai số bình phương trung bình (MSE).</p>
      </section>

      <!-- Section 3 -->
      <section id="sec3">
        <h2 class="section-title"><span class="section-number">3</span> HỆ THỐNG 23 CHỈ SỐ TÀI CHÍNH TUYỂN CHỌN</h2>
        <p>Nghiên cứu xây dựng một ma trận chỉ số tài chính toàn diện bao quát 5 khía cạnh sức khỏe của doanh nghiệp:</p>

        <div class="table-container">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Trụ Cột Tài Chính</th>
                <th>Mã</th>
                <th>Chỉ Số Tài Chính</th>
                <th>Ý Nghĩa Nghiệp Vụ Kế Toán</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td rowspan="5"><strong>1. Khả năng thanh toán</strong></td>
                <td><code>X1</code></td>
                <td>Tỷ số thanh toán hiện hành</td>
                <td>Đo lường năng lực trang trải nợ ngắn hạn bằng tài sản ngắn hạn</td>
              </tr>
              <tr>
                <td><code>X2</code></td>
                <td>Tỷ số thanh toán nhanh</td>
                <td>Đo khả năng thanh toán tức thời, loại trừ tồn kho kém thanh khoản</td>
              </tr>
              <tr>
                <td><code>X3</code></td>
                <td>Tỷ số nợ trên tổng tài sản</td>
                <td>Mức độ sử dụng đòn bẩy tài chính và gánh nặng nợ vay</td>
              </tr>
              <tr>
                <td><code>X4</code></td>
                <td>Tỷ số nợ trên vốn chủ sở hữu</td>
                <td>Cơ cấu nguồn vốn và mức độ rủi ro đối với vốn chủ</td>
              </tr>
              <tr>
                <td><code>X5</code></td>
                <td>Vốn lưu động trên tổng tài sản</td>
                <td>Quy mô đệm thanh khoản ngắn hạn trong cơ cấu tài sản</td>
              </tr>
              <tr>
                <td rowspan="5"><strong>2. Năng lực hoạt động</strong></td>
                <td><code>X6</code></td>
                <td>Vòng quay khoản phải thu</td>
                <td>Tốc độ thu hồi nợ và rủi ro phát sinh nợ khó đòi</td>
              </tr>
              <tr>
                <td><code>X7</code></td>
                <td>Vòng quay hàng tồn kho</td>
                <td>Hiệu quả giải phóng hàng tồn và nguy cơ ứ đọng vốn</td>
              </tr>
              <tr>
                <td><code>X8</code></td>
                <td>Vòng quay vốn lưu động</td>
                <td>Tốc độ luân chuyển của vốn ngắn hạn</td>
              </tr>
              <tr>
                <td><code>X9</code></td>
                <td>Vòng quay tài sản cố định</td>
                <td>Năng suất khai thác nhà xưởng, máy móc thiết bị</td>
              </tr>
              <tr>
                <td><code>X10</code></td>
                <td>Vòng quay tổng tài sản</td>
                <td>Hiệu suất tạo doanh thu từ toàn bộ tài sản doanh nghiệp</td>
              </tr>
              <tr>
                <td rowspan="5"><strong>3. Năng lực sinh lời</strong></td>
                <td><code>X11</code></td>
                <td>Tỷ suất sinh lời trên tài sản (ROA)</td>
                <td>Hiệu quả sinh lời của 1 đồng tài sản đầu tư</td>
              </tr>
              <tr>
                <td><code>X12</code></td>
                <td>Tỷ suất sinh lời trên vốn CSH (ROE)</td>
                <td>Lợi nhuận tạo ra cho các cổ đông</td>
              </tr>
              <tr>
                <td><code>X13</code></td>
                <td>Biên lợi nhuận gộp</td>
                <td>Sức mạnh cạnh tranh giá bán và quản trị giá vốn</td>
              </tr>
              <tr>
                <td><code>X14</code></td>
                <td>Biên lợi nhuận hoạt động</td>
                <td>Hiệu quả sinh lời từ hoạt động kinh doanh cốt lõi</td>
              </tr>
              <tr>
                <td><code>X15</code></td>
                <td>Lợi nhuận trên tổng chi phí</td>
                <td>Khả năng tạo thặng dư trên mỗi đồng chi phí bỏ ra</td>
              </tr>
              <tr>
                <td rowspan="5"><strong>4. Tiềm năng phát triển</strong></td>
                <td><code>X16</code></td>
                <td>Tăng trưởng doanh thu thuần</td>
                <td>Tốc độ mở rộng quy mô thị trường</td>
              </tr>
              <tr>
                <td><code>X17</code></td>
                <td>Tăng trưởng lợi nhuận hoạt động</td>
                <td>Động lực gia tăng lợi nhuận bền vững</td>
              </tr>
              <tr>
                <td><code>X18</code></td>
                <td>Tăng trưởng tổng tài sản</td>
                <td>Mức độ mở rộng đầu tư tài sản của doanh nghiệp</td>
              </tr>
              <tr>
                <td><code>X19</code></td>
                <td>Tăng trưởng vốn chủ sở hữu</td>
                <td>Khả năng tự tài trợ và bảo toàn vốn</td>
              </tr>
              <tr>
                <td><code>X20</code></td>
                <td>Tăng trưởng thu nhập mỗi cổ phần (EPS)</td>
                <td>Gia tăng giá trị đầu tư cho cổ đông</td>
              </tr>
              <tr>
                <td rowspan="3"><strong>5. Lưu chuyển tiền tệ</strong></td>
                <td><code>X21</code></td>
                <td>Dòng tiền thuần HĐKD / Tổng tài sản</td>
                <td>Chất lượng dòng tiền tạo ra từ tài sản thực tế</td>
              </tr>
              <tr>
                <td><code>X22</code></td>
                <td>Dòng tiền thuần HĐKD / Tổng nợ</td>
                <td>Năng lực trả nợ bằng tiền mặt từ hoạt động kinh doanh</td>
              </tr>
              <tr>
                <td><code>X23</code></td>
                <td>Dòng tiền thuần HĐKD / Doanh thu</td>
                <td>Mức độ chuyển hóa doanh thu sổ sách thành tiền mặt</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Section 4 -->
      <section id="sec4">
        <h2 class="section-title"><span class="section-number">4</span> DỮ LIỆU THỰC NGHIỆM & QUÁ TRÌNH HUẤN LUYỆN</h2>
        <p>Mẫu nghiên cứu gồm 465 công ty ST và 2.325 công ty Non-ST ghép cặp theo tỷ lệ 1:5. Mẫu kiểm thử độc lập gồm 300 công ty (50 ST, 250 Non-ST) được trích xuất dữ liệu tại <strong>năm T-3</strong> (tức 3 năm trước khi bị cảnh báo).</p>

        <!-- Figures 2 & 3 -->
        <div class="figure-wrapper">
          <div class="figure-header">
            <span>QUÁ TRÌNH HỘI TỤ SAI SỐ HUẤN LUYỆN (RMSE)</span>
            <span class="figure-badge">Hình 2 & 3</span>
          </div>
          <div class="figure-img-container">
            <img src="figures_paper2/fig2_3_training_rmse.png" alt="Hình 2 & 3: Quá trình huấn luyện mô hình" class="figure-img" />
          </div>
          <div class="figure-caption">
            <strong>Hình 2 & 3:</strong> Sai số bình phương trung bình (RMSE) của mô hình học sâu qua các vòng huấn luyện (epochs). Sai số giảm dốc nhanh chóng và hội tụ ổn định sau 400 epochs.
          </div>
        </div>
      </section>

      <!-- Section 5 -->
      <section id="sec5">
        <h2 class="section-title"><span class="section-number">5</span> KẾT QUẢ THỰC NGHIỆM ĐỊNH LƯỢNG & ĐỐI CHIẾU SO SÁNH</h2>
        <p>Bảng đối chiếu kết quả dự báo ngoài mẫu giữa 3 mô hình trên 300 công ty kiểm thử tại thời điểm T-3 (Bảng 8 bài báo gốc):</p>

        <div class="table-container">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Phương Pháp Dự Báo</th>
                <th>Phân Nhóm Doanh Nghiệp</th>
                <th>Số Mẫu Đúng</th>
                <th>Số Mẫu Sai</th>
                <th>Độ Chính Xác (%)</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: rgba(16, 185, 129, 0.08); font-weight: 600;">
                <td rowspan="3"><strong>Mô hình Học Sâu (Deep Learning)</strong></td>
                <td>Công ty Non-ST (250 công ty)</td>
                <td>194</td>
                <td>56</td>
                <td><strong>77,60%</strong></td>
              </tr>
              <tr style="background: rgba(16, 185, 129, 0.08); font-weight: 600;">
                <td><strong>Công ty ST (Kiệt quệ) (50 công ty)</strong></td>
                <td><strong>41</strong></td>
                <td><strong>9</strong></td>
                <td><strong style="color: #059669; font-size: 1.05rem;">82,00%</strong></td>
              </tr>
              <tr style="background: rgba(16, 185, 129, 0.12); font-weight: 700;">
                <td><strong>Tổng thể mô hình (300 công ty)</strong></td>
                <td><strong>235</strong></td>
                <td><strong>65</strong></td>
                <td><strong style="color: #059669; font-size: 1.05rem;">78,33%</strong></td>
              </tr>
              <tr>
                <td rowspan="3">Mô hình Hồi quy Logistic</td>
                <td>Công ty Non-ST (250 công ty)</td>
                <td>176</td>
                <td>74</td>
                <td>70,40%</td>
              </tr>
              <tr>
                <td>Công ty ST (Kiệt quệ) (50 công ty)</td>
                <td>37</td>
                <td>13</td>
                <td>74,00%</td>
              </tr>
              <tr style="font-weight: 600;">
                <td>Tổng thể mô hình (300 công ty)</td>
                <td>213</td>
                <td>87</td>
                <td>71,00%</td>
              </tr>
              <tr>
                <td rowspan="3">Mô hình Mạng BP Neural Network</td>
                <td>Công ty Non-ST (250 công ty)</td>
                <td>174</td>
                <td>76</td>
                <td>69,60%</td>
              </tr>
              <tr>
                <td>Công ty ST (Kiệt quệ) (50 công ty)</td>
                <td>35</td>
                <td>15</td>
                <td>70,00%</td>
              </tr>
              <tr style="font-weight: 600;">
                <td>Tổng thể mô hình (300 công ty)</td>
                <td>209</td>
                <td>91</td>
                <td>69,67%</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout callout-success">
          <div class="callout-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
            Điểm sáng vượt bậc của Học Sâu:
          </div>
          <p style="margin-bottom:0;">Trong khi mô hình Hồi quy Logistic chỉ đạt độ chính xác 74% và mạng BP nơ-ron truyền thống chỉ đạt 70% đối với nhóm công ty kiệt quệ, <strong>mô hình Học Sâu đạt tới 82,00%</strong>. Nhờ có 4 tầng ẩn Encoder nén và tái trích xuất đặc trưng, mô hình đã "nhìn thấu" các biểu hiện suy thoái tiềm ẩn từ trước 3 năm, giảm tỷ lệ bỏ sót công ty rủi ro xuống chỉ còn 18%.</p>
        </div>
      </section>

      <!-- Section 6 -->
      <section id="sec6">
        <h2 class="section-title"><span class="section-number">6</span> ĐÚC KẾT CHO NGHỀ NGHIỆP KIỂM TOÁN & KẾ TOÁN QUẢN TRỊ</h2>
        <ul>
          <li><strong>Hỗ trợ chuẩn mực ISA 570 (Hoạt động liên tục):</strong> Cung cấp bằng chứng kiểm toán định lượng vững chắc giúp kiểm toán viên đưa ra ý kiến chấp nhận từng phần hoặc từ chối đưa ra ý kiến khi phát hiện nguy cơ kiệt quệ tài chính.</li>
          <li><strong>Hệ thống cảnh báo sớm cho CFO:</strong> Giúp các giám đốc tài chính phát hiện sớm các dấu hiệu suy giảm thanh khoản và sinh lời từ 3 năm trước khi khủng hoảng bùng phát để kịp thời tái cấu trúc vốn.</li>
          <li><strong>Đánh giá rủi ro cấp tín dụng ngân hàng:</strong> Giúp các tổ chức tín dụng sàng lọc hồ sơ vay vốn, thiết lập lãi suất rủi ro và yêu cầu tài sản bảo đảm phù hợp.</li>
        </ul>
      </section>

      <!-- Section 7 -->
      <section id="sec7">
        <h2 class="section-title"><span class="section-number">7</span> TÀI LIỆU THAM KHẢO CHÍNH (REFERENCES)</h2>
        <ul class="references-list">
          <li><strong>Beaver, W. H. (1966).</strong> Financial ratios as predictors of failure. <em>Journal of Accounting Research</em>, 4, 71–111.</li>
          <li><strong>Altman, E. I. (1968).</strong> Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. <em>The Journal of Finance</em>, 23(4), 589–609.</li>
          <li><strong>Ohlson, J. A. (1980).</strong> Financial ratios and the probabilistic prediction of bankruptcy. <em>Journal of Accounting Research</em>, 18(1), 109–131.</li>
          <li><strong>Sun, Y. (2024).</strong> Financial distress prediction based on deep learning model. <em>Procedia Computer Science</em>, 243, 1069–1078.</li>
        </ul>
      </section>
    """

    full_html = get_html_template(
        title=TITLE_VI,
        title_en=TITLE_EN,
        authors=AUTHORS,
        journal=JOURNAL,
        doi=DOI,
        badge=BADGE,
        sidebar_links=sidebar_links,
        content_html=content_html,
        active_paper_idx=2
    )

    html_path = os.path.join(PAPERS_DIR, "paper_2_Financial_Distress_Prediction_tiengviet.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated HTML: {os.path.basename(html_path)}")

if __name__ == "__main__":
    build()
