# -*- coding: utf-8 -*-
"""
Builder for Paper 1:
Detecting Accounting Frauds in Publicly Traded U.S. Firms: A Machine Learning Approach
(Li, Yu, Zhang, Ke - ACML / Journal of Accounting Research)
"""

import os
from generate_day02_helpers import get_html_template

PAPERS_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day02_Extra\papers"

TITLE_VI = "Phát Hiện Gian Lận Kế Toán Tại Các Công Ty Đại Chúng Hoa Kỳ Bằng Tiếp Cận Học Máy & Dữ Liệu BCTC Thô"
TITLE_EN = "Detecting Accounting Frauds in Publicly Traded U.S. Firms: A Machine Learning Approach"
AUTHORS = "Bin Li (ĐH Vũ Hán), Julia Yu (Nanyang Business School, NTU), Jie Zhang (NTU), Bin Ke (ĐH Quốc gia Singapore - NUS)"
JOURNAL = "ACML / JMLR Workshop and Conference Proceedings (Mở rộng tại Journal of Accounting Research - JAR)"
DOI = "JMLR W&CP 45:173-188 / SSRN 2849013"
BADGE = "Paper 1 • JAR & ACML Landmark"

def build():
    # Markdown Content
    md_content = f"""# {TITLE_VI.upper()}
*({TITLE_EN})*

- **Tác giả:** {AUTHORS}
- **Tạp chí & Hội nghị:** {JOURNAL}
- **Định danh học thuật:** {DOI}
- **Cơ sở dữ liệu thực nghiệm:** Toàn bộ hồ sơ vi phạm AAERs từ Ủy ban Chứng khoán Hoa Kỳ (SEC) giai đoạn 1982–2010 (90.172 năm-công ty)

---

## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

Nghiên cứu này khảo sát cách thức các kỹ thuật học máy (*Machine Learning*) có thể hỗ trợ hiệu quả việc phát hiện gian lận kế toán tại các công ty đại chúng giao dịch trên thị trường chứng khoán Hoa Kỳ. Các công trình nghiên cứu trước đây thường bắt chước chuyên gia con người thông qua việc sử dụng các tỷ số tài chính (*financial ratios*) hoặc tỷ số phi tài chính làm biến đặc trưng cho mô hình. Chúng tôi tạo ra bước đột phá khác biệt hoàn toàn bằng cách **sử dụng trực tiếp các biến số kế toán thô (*raw accounting variables*)**, vốn có sẵn ngay trên báo cáo tài chính của doanh nghiệp, từ đó cho phép áp dụng nhanh chóng cho các công ty mới với chi phí rất thấp.

Bên cạnh đó, chúng tôi thu thập bộ dữ liệu gian lận kế toán toàn diện nhất về các công ty niêm yết Hoa Kỳ và gán nhãn từng năm-công ty (*firm-years*). Một đặc tính cốt lõi của bài toán này là **dữ liệu mất cân bằng cực đoan (*extremely imbalanced data*)**, trong đó số năm-công ty có hành vi gian lận chiếm tỷ lệ chưa tới 1% (chính xác là 0,7%). Thay vì sử dụng kỹ thuật lấy lại mẫu (*re-sampling*) làm sai lệch phân phối thực tế, chúng tôi giải quyết vấn đề bằng các kỹ thuật học máy thích nghi với dữ liệu mất cân bằng:
1. Mô hình Máy véctơ hỗ trợ có trọng số phạt lệch (*Biased-Penalty Support Vector Machine - BP-SVM*) tuyến tính và phi tuyến tính (Polynomial, RBF).
2. Các phương pháp học kết hợp (*Ensemble Methods*) tiên tiến như **EasyEnsemble** và **BalancedCascade**.

Kết quả thực nghiệm trên diện rộng chứng minh rằng phương pháp đề xuất đạt độ chính xác cân bằng (*Balanced Accuracy - BAC*) lên tới **77,53%**, vượt trội hoàn toàn so với các mô hình kinh điển như Logistic Regression (BAC chỉ đạt 60,00%) hay SVM-FK (BAC 69,74%). Hơn thế nữa, thuật toán có tốc độ tính toán cực nhanh, sẵn sàng triển khai trên quy mô lớn tại các cơ quan quản lý và các hãng kiểm toán.

**Từ khóa:** Phát hiện gian lận kế toán; Học máy; Biến số kế toán thô; Dữ liệu mất cân bằng; Biased-Penalty SVM; Phương pháp kết hợp (Ensemble Methods); AAERs; SEC.

---

## 1. GIỚI THIỆU & ĐỘNG LỰC NGHIÊN CỨU (INTRODUCTION)

Học máy đã và đang được ứng dụng mạnh mẽ trong lĩnh vực tài chính tính toán (*computational finance*). Trong đó, một trong những bài toán thách thức và có giá trị kinh tế lớn nhất là **phát hiện gian lận kế toán (*accounting fraud*)** tại các công ty niêm yết. Gian lận kế toán do những người nội bộ (các nhà quản lý cấp cao và cổ đông kiểm soát) thực hiện là vấn đề nhức nhối mang tính toàn cầu.

Nếu không được phát hiện và ngăn chặn kịp thời, gian lận sẽ gây ra những thảm họa kinh tế khổng lồ cho các bên liên quan trực tiếp (như các vụ bê bối lịch sử Enron, WorldCom). Gian lận cũng tác động tiêu cực gián tiếp tới các doanh nghiệp làm ăn liêm chính, vì các doanh nghiệp trung thực buộc phải cạnh tranh bất bình đẳng với các công ty gian dối để thu hút nguồn vốn khan hiếm của nhà đầu tư. Hơn thế nữa, do sự bất cân xứng thông tin (*information asymmetry*) giữa người nội bộ và thị trường, gian lận làm xói mòn nghiêm trọng niềm tin của công chúng vào hệ thống tài chính.

### Điểm Nghẽn Của Các Phương Pháp Truyền Thống:
Trong lịch sử nghiên cứu kế toán, giới học thuật và thực hành thường tin rằng: Để phát hiện gian lận, mô hình phải bắt chước hành vi của kiểm toán viên con người bằng cách tính toán các **tỷ số tài chính (*financial ratios*)**, chẳng hạn như:
- Mô hình M-Score của Beneish (1999) gồm 8 tỷ số tài chính.
- Mô hình F-Score của Dechow et al. (2011) gồm 11 tỷ số tài chính và biến dồn tích.

Tuy nhiên, việc phụ thuộc vào tỷ số tài chính bộc lộ 3 điểm yếu chí mạng:
1. **Thiên lệch chủ quan của con người (*Human Domain Bias*):** Tỷ số tài chính do con người tự nghĩ ra có thể bỏ sót những mối tương tác phi tuyến tính ngầm giữa các khoản mục số liệu thô.
2. **Chi phí tính toán và mất mát thông tin:** Khi doanh nghiệp không có đủ dữ liệu lịch sử hoặc có cấu trúc vốn đặc thù, việc tính tỷ số sẽ gặp lỗi chia cho 0 hoặc làm mất mát độ lớn thực tế (*magnitude*) của các giao dịch.
3. **Kẻ gian dễ dàng đối phó:** Những kẻ gian lận sành sỏi hoàn toàn hiểu rõ các tỷ số như ROA, Biên lợi nhuận gộp, hay Tỷ số thanh toán hiện hành, và họ sẽ chủ động dàn xếp các con số để "làm đẹp" đúng các chỉ số mà kiểm toán viên thường soi xét!

---

## 2. Ý TƯỞNG CỐT LÕI: SỬ DỤNG TRỰC TIẾP BIẾN KẾ TOÁN THÔ (RAW ACCOUNTING VARIABLES)

Thay vì chuyển đổi dữ liệu thành các tỷ số tài chính, nhóm nghiên cứu đề xuất **đưa trực tiếp 24 khoản mục kế toán thô** từ Bảng cân đối kế toán và Báo cáo kết quả hoạt động kinh doanh vào các thuật toán học máy hiện đại.

![Hình 1: Tổng quan hệ thống phát hiện gian lận đề xuất](figures_paper1/fig_p4_1.jpeg)
*Hình 1: Sơ đồ đối chiếu giữa tiếp cận truyền thống dựa trên tỷ số tài chính (phía trên) và tiếp cận đề xuất của nghiên cứu dựa trên dữ liệu kế toán thô kết hợp học thích nghi mất cân bằng (phía dưới).*

### Danh mục 24 biến kế toán thô trên BCTC:
1. `act`: Tài sản ngắn hạn (Current Assets - Total)
2. `ap`: Phải trả người bán (Accounts Payable - Trade)
3. `at`: Tổng tài sản (Assets - Total)
4. `ceq`: Vốn chủ sở hữu phổ thông (Common/Ordinary Equity - Total)
5. `che`: Tiền và tương đương tiền (Cash and Short-Term Investments)
6. `cogs`: Giá vốn hàng bán (Cost of Goods Sold)
7. `csho`: Khối lượng cổ phiếu lưu hành (Common Shares Outstanding)
8. `dlc`: Nợ ngắn hạn (Debt in Current Liabilities)
9. `dltt`: Nợ dài hạn (Long-Term Debt - Total)
10. `dp`: Khấu hao và hao mòn lũy kế (Depreciation and Amortization)
11. `ebit`: Lợi nhuận trước lãi vay và thuế (EBIT)
12. `invt`: Hàng tồn kho (Inventories - Total)
13. `ivao`: Đầu tư và tạm ứng dài hạn khác (Investment and Advances - Other)
14. `ivst`: Đầu tư ngắn hạn (Short-Term Investments - Total)
15. `lct`: Nợ ngắn hạn tổng cộng (Current Liabilities - Total)
16. `lt`: Tổng nợ phải trả (Liabilities - Total)
17. `ni`: Lợi nhuận ròng (Net Income/Loss)
18. `ppegt`: Nguyên giá tài sản cố định (Property, Plant and Equipment - Gross)
19. `ppent`: Giá trị còn lại TSCĐ (Property, Plant and Equipment - Net)
20. `pstk`: Cổ phiếu ưu đãi (Preferred/Preference Stock)
21. `re`: Lợi nhuận giữ lại chưa phân phối (Retained Earnings)
22. `rect`: Khoản phải thu khách hàng (Receivables - Total)
23. `sale`: Doanh thu thuần (Sales/Turnover - Net)
24. `xsga`: Chi phí bán hàng và quản lý doanh nghiệp (SG&A Expense)

---

## 3. CƠ SỞ DỮ LIỆU THỰC NGHIỆM AAERs (1982–2010)

Mẫu gian lận kế toán được trích xuất từ **Thông cáo Thực thi Kế toán và Kiểm toán (AAERs - Accounting and Auditing Enforcement Releases)** do SEC ban hành từ 17/05/1982 đến 01/09/2010.

| Tên Tập Dữ Liệu | Giai Đoạn | Tổng Số Năm-Công Ty | Số Năm Gian Lận (Tỷ lệ %) | Số Năm Không Gian Lận (%) | Số Lượng Biến Đặc Trưng |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **USRaw 0paired (Toàn bộ)** | 1991–2005 | 90.172 (100%) | 632 (0,70%) | 89.540 (99,30%) | 24 biến thô năm $t$ |
| - Mẫu huấn luyện (Train) | 1991–2002 | 72.456 (100%) | 514 (0,71%) | 71.942 (99,29%) | 24 biến thô |
| - Mẫu kiểm thử ngoài mẫu (Test) | 2003–2005 | 17.716 (100%) | 118 (0,67%) | 17.598 (99,33%) | 24 biến thô |
| **USRaw 1paired (Cặp 2 năm)** | 1991–2005 | 77.605 (100%) | 548 (0,62%) | 77.057 (99,38%) | 48 biến (năm $t$ và $t-1$) |
| - Mẫu huấn luyện (Train) | 1991–2002 | 61.662 (100%) | 438 (0,71%) | 61.224 (99,29%) | 48 biến |
| - Mẫu kiểm thử (Test) | 2003–2005 | 15.943 (100%) | 110 (0,67%) | 15.833 (99,33%) | 48 biến |
| **USRatio (Tỷ số tài chính)** | 1991–2005 | 88.875 (100%) | 693 (0,78%) | 88.182 (99,22%) | 11 tỷ số (Dechow 2011) |
| - Mẫu huấn luyện (Train) | 1991–2002 | 70.879 (100%) | 568 (0,80%) | 70.311 (99,20%) | 11 tỷ số |
| - Mẫu kiểm thử (Test) | 2003–2005 | 17.996 (100%) | 125 (0,69%) | 17.871 (99,31%) | 11 tỷ số |

> [!WARNING]
> **Thách thức mất cân bằng lớp cực đoan:** Số vụ gian lận chỉ chiếm **0,7%** tổng mẫu (tỷ lệ 1 vụ gian lận trên 140 công ty bình thường). Nếu một mô hình ngây thơ luôn dự đoán "Không gian lận", độ chính xác thuần túy (*Raw Accuracy*) vẫn đạt tới 99,3%, nhưng mô hình đó hoàn toàn vô giá trị vì bỏ sót 100% các công ty gian lận! Do đó, bắt buộc phải sử dụng **Balanced Accuracy (BAC)**:
> $$ \\text{{Balanced Accuracy (BAC)}} = \\frac{{\\text{{Sensitivity}} + \\text{{Specificity}}}}{{2}} $$

---

## 4. CÁC THUẬT TOÁN HỌC MÁY THÍCH NGHI MẤT CÂN BẰNG

### 4.1 Biased-Penalty Support Vector Machine (BP-SVM)
Để giải bài toán bất đối xứng chi phí, BP-SVM gán trọng số phạt $p$ lớn hơn nhiều cho các trường hợp phân loại nhầm lớp thiểu số (gian lận):
$$ \\min_{{\\mathbf{{w}}, b, \\boldsymbol{{\\xi}}}} \\frac{{1}}{{2}} \\|\\mathbf{{w}}\\|^2 + C \\left( p \\sum_{{i \\in \\text{{Frauds}}}} \\xi_i + \\sum_{{i \\in \\text{{Non-frauds}}}} \\xi_i \\right) $$
Trong thực nghiệm, tham số phạt tối ưu được tính bằng tỷ lệ mất cân bằng mẫu:
$$ p = \\frac{{N_{{\\text{{non-fraud}}}}}}{{N_{{\\text{{fraud}}}}}} = \\frac{{71.942}}{{514}} \\approx 139,96 $$

Các dạng nhân (kernel) được kiểm định:
- Tuyến tính (*Linear Kernel*): $\\kappa(\\mathbf{{x}}_i, \\mathbf{{x}}_j) = \\mathbf{{x}}_i^T \\mathbf{{x}}_j$
- Đa thức bậc 2 (*Polynomial Kernel degree 2*): $\\kappa(\\mathbf{{x}}_i, \\mathbf{{x}}_j) = (\\mathbf{{x}}_i^T \\mathbf{{x}}_j + 1)^2$
- Đa thức bậc 3 (*Polynomial Kernel degree 3*): $\\kappa(\\mathbf{{x}}_i, \\mathbf{{x}}_j) = (\\mathbf{{x}}_i^T \\mathbf{{x}}_j + 1)^3$
- Hàm bán kính cơ sở (*RBF Kernel*): $\\kappa(\\mathbf{{x}}_i, \\mathbf{{x}}_j) = \\exp(-\\gamma \\|\\mathbf{{x}}_i - \\mathbf{{x}}_j\\|^2)$

### 4.2 Phương Pháp Học Kết Hợp (Ensemble Learning: EasyEnsemble & BalancedCascade)
Thay vì chỉ huấn luyện một bộ phân loại duy nhất, EasyEnsemble và BalancedCascade khai thác sức mạnh của tập hợp $m_1$ bộ phân loại AdaBoost, mỗi bộ AdaBoost chứa $m_2$ cây quyết định (*Decision Trees*):
1. **EasyEnsemble:** Trích xuất ngẫu nhiên $m_1$ tập mẫu con cân bằng độc lập, huấn luyện $m_1$ bộ phân loại yếu và tổng hợp kết quả biểu quyết.
2. **BalancedCascade:** Học có giám sát theo tầng thác lũ. Sau mỗi vòng, loại bỏ các mẫu không gian lận đã được phân loại đúng với độ tin cậy cực cao, dồn toàn bộ năng lực học máy vào việc phân biệt các mẫu mập mờ, khó phân loại nhất.

---

## 5. KẾT QUẢ THỰC NGHIỆM ĐỊNH LƯỢNG (EMPIRICAL RESULTS)

Bảng dưới đây tổng hợp kết quả kiểm thử ngoài mẫu (*out-of-sample test*) giai đoạn 2003–2005 trên 17.716 năm-công ty:

| Bộ Dữ Liệu | Phương Pháp Thuật Toán | Sensitivity (%) (Bắt trúng gian lận) | Specificity (%) (Nhận diện công ty sạch) | Balanced Accuracy (BAC %) |
| :--- | :--- | :--- | :--- | :--- |
| **USRatio (11 tỷ số tài chính)** | Mô hình Logit (Dechow et al. 2011) | 64,00% | 55,99% | **60,00%** |
| **USRaw 1paired (48 biến)** | SVM-FK (Cecchini et al. 2010) | 65,45% | 74,03% | **69,74%** |
| **USRaw 0paired (24 biến thô)** | BP-SVM Tuyến tính (Linear) | 70,34% | 68,96% | **69,65%** |
| USRaw 0paired (24 biến thô) | BP-SVM Đa thức bậc 2 (Poly-2) | 71,19% | 72,28% | **71,73%** |
| USRaw 0paired (24 biến thô) | **BP-SVM Đa thức bậc 3 (Poly-3)** | **73,73%** | **72,83%** | **73,28%** |
| USRaw 0paired (24 biến thô) | BP-SVM Bán kính RBF | 71,19% | 74,22% | **72,70%** |
| **USRaw 0paired (24 biến thô)** | **EasyEnsemble (AdaBoost + Trees)** | **75,76%** | **77,10%** | **76,43%** |
| **USRaw 0paired (24 biến thô)** | **BalancedCascade (Cascade Ensemble)** | **72,54%** | **82,52%** | **77,53%** |

### 🔍 Những Phát Hiện Khoa Học Mang Tính Cách Mạng:
1. **Biến số kế toán thô vượt trội hơn tỷ số tài chính:** Khi cùng áp dụng mô hình máy học, việc dùng 24 biến thô mang lại BAC 69,65% – 77,53%, cao hơn vượt bậc so với việc dùng 11 tỷ số tài chính chọn lọc thủ công (chỉ đạt BAC 60,00%).
2. **Phi tuyến tính nắm giữ chìa khóa gian lận:** Kernel đa thức bậc 3 (Poly-3) đạt BAC 73,28%, cao hơn đáng kể so với kernel tuyến tính (69,65%). Điều này chứng minh hành vi che giấu gian lận tạo ra các mối tương tác phi tuyến tính phức tạp giữa các khoản mục tài sản, nợ và chi phí mà mô hình tuyến tính không thể nào phát hiện.
3. **Kỹ thuật Ensemble đạt đỉnh cao hiệu năng:** BalancedCascade đạt Balanced Accuracy cao nhất lịch sử nghiên cứu trên tập dữ liệu này: **77,53%**, đồng thời đẩy độ đặc hiệu Specificity lên tới **82,52%** (giảm thiểu tối đa tình trạng báo động giả cho kiểm toán viên).

---

## 6. ĐÚC KẾT CHO NGHỀ NGHIỆP KẾ TOÁN & KIỂM TOÁN

> [!TIP]
> **Bài học nghiệp vụ cho Kiểm toán viên:**
> - **Đừng chỉ nhìn vào các tỷ số quen thuộc:** Kẻ gian luôn chủ đích điều chỉnh số liệu để các chỉ số như ROE, Current Ratio, Gross Margin nằm trong "vùng an toàn". Khi kiểm toán, hãy đưa toàn bộ số liệu sổ sách thô vào thuật toán học máy phi tuyến tính để nhận diện các bất thường cấu trúc ngầm.
> - **Tối ưu hóa thời gian kiểm toán:** Với Specificity đạt 82,52%, mô hình BalancedCascade giúp loại bỏ hơn 80% các doanh nghiệp thực sự liêm chính, giúp hãng kiểm toán tập trung nguồn lực nhân sự cấp cao vào 20% các hồ sơ rủi ro cao nhất.

---

## 7. TÀI LIỆU THAM KHẢO CHÍNH (REFERENCES)

1. **Beneish, M. D. (1999).** The detection of earnings manipulation. *Financial Analysts Journal*, 55(5), 24–36.
2. **Dechow, P. M., Ge, W., Larson, C. R., & Sloan, R. G. (2011).** Predicting material accounting misstatements. *Contemporary Accounting Research*, 28(1), 17–82.
3. **Cecchini, M., Aytug, H., Koehler, G. J., & Pathak, P. (2010).** Making words work: Using financial text as a predictor of financial events. *Decision Support Systems*, 50(1), 164–175.
4. **Bao, Y., Ke, B., Li, B., Yu, Y. J., & Zhang, J. (2020).** Detecting accounting fraud in publicly traded U.S. firms using a machine learning approach. *Journal of Accounting Research*, 58(1), 199–235.
5. **Liu, X.-Y., & Zhou, Z.-H. (2013).** Ensemble methods for class imbalance learning. *Imbalanced Learning: Foundations, Algorithms, and Applications*, Wiley, 61–82.
"""

    md_path = os.path.join(PAPERS_DIR, "paper_1_Detecting_Accounting_Fraud_tiengviet.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Markdown: {os.path.basename(md_path)}")

    # Generate HTML
    sidebar_links = """
      <a href="#abstract" class="sidebar-link">Tóm Tắt Nghiên Cứu</a>
      <a href="#sec1" class="sidebar-link">1. Mở Đầu & Động Lực</a>
      <a href="#sec2" class="sidebar-link">2. Tiếp Cận Dữ Liệu BCTC Thô</a>
      <a href="#sec3" class="sidebar-link">3. CSDL Thực Nghiệm AAERs</a>
      <a href="#sec4" class="sidebar-link">4. Thuật Toán BP-SVM & Ensemble</a>
      <a href="#sec5" class="sidebar-link">5. Kết Quả Thực Nghiệm</a>
      <a href="#sec6" class="sidebar-link">6. Đúc Kết Nghiệp Vụ Kiểm Toán</a>
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
          Nghiên cứu này khảo sát cách thức các kỹ thuật học máy (<em>Machine Learning</em>) có thể hỗ trợ hiệu quả việc phát hiện gian lận kế toán tại các công ty đại chúng niêm yết trên thị trường chứng khoán Hoa Kỳ. Các công trình trước đây thường bắt chước chuyên gia con người thông qua việc sử dụng các tỷ số tài chính (<em>financial ratios</em>). Chúng tôi tạo ra bước đột phá bằng cách <strong>sử dụng trực tiếp các biến số kế toán thô (raw accounting variables)</strong> có sẵn ngay trên báo cáo tài chính của doanh nghiệp. Bên cạnh đó, chúng tôi thu thập bộ dữ liệu gian lận toàn diện nhất từ các thông cáo thực thi của SEC (AAERs). Để giải quyết bài toán <strong>mất cân bằng lớp cực đoan (gian lận dưới 1%)</strong>, chúng tôi ứng dụng các thuật toán chuyên biệt gồm Biased-Penalty Support Vector Machine (BP-SVM) và các mô hình học kết hợp (EasyEnsemble, BalancedCascade). Kết quả thực nghiệm ngoài mẫu khẳng định mô hình đề xuất đạt Balanced Accuracy lên tới <strong>77,53%</strong>, vượt trội hoàn toàn so với mô hình hồi quy Logit truyền thống (60,00%).
        </p>
        <div class="keywords-box">
          <strong>Từ khóa cốt lõi:</strong> Machine Learning; Accounting Fraud Detection; Raw Accounting Variables; Imbalanced Learning; Biased-Penalty SVM; Ensemble Methods; AAERs; Balanced Accuracy.
        </div>
      </section>

      <!-- Section 1 -->
      <section id="sec1">
        <h2 class="section-title"><span class="section-number">1</span> MỞ ĐẦU & ĐỘNG LỰC NGHIÊN CỨU</h2>
        <p>Học máy ngày càng khẳng định vai trò sống còn trong tài chính tính toán. Trong đó, việc phát hiện gian lận báo cáo tài chính (BCTC) do những người nội bộ (ban giám đốc điều hành, cổ đông kiểm soát) thực hiện là bài toán cấp bách nhất. Các vụ sụp đổ kinh hoàng như Enron, WorldCom cho thấy nếu không ngăn chặn kịp thời, gian lận sẽ xóa sổ hàng chục tỷ USD giá trị vốn hóa, tàn phá niềm tin nhà đầu tư và làm suy thoái thị trường vốn.</p>
        
        <div class="callout callout-warning">
          <div class="callout-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
              <line x1="12" y1="9" x2="12" y2="13"></line>
              <line x1="12" y1="17" x2="12.01" y2="17"></line>
            </svg>
            Hạn chế chí mạng của các mô hình dựa trên tỷ số tài chính (Financial Ratios)
          </div>
          <p style="margin-bottom:0;">Các mô hình kinh điển như Beneish M-Score (1999) hay Dechow F-Score (2011) dựa dẫm vào các tỷ số tài chính do con người chọn lọc chủ quan. Kẻ gian lận sành sỏi luôn nắm rõ các tỷ số này và chủ động "xào nấu" số liệu để tỷ số vẫn đẹp mắt. Hơn nữa, việc tính tỷ số làm triệt tiêu thông tin về độ lớn giao dịch thực tế và không phản ánh được các tương tác phi tuyến tính ngầm giữa các tài khoản.</p>
        </div>
      </section>

      <!-- Section 2 -->
      <section id="sec2">
        <h2 class="section-title"><span class="section-number">2</span> Ý TƯỞNG ĐỘT PHÁ: SỬ DỤNG TRỰC TIẾP BIẾN KẾ TOÁN THÔ</h2>
        <p>Thay vì tính toán các tỷ số tài chính trung gian, nhóm tác giả đưa trực tiếp <strong>24 biến số kế toán thô (Raw Accounting Variables)</strong> từ Bảng cân đối kế toán và Báo cáo kết quả hoạt động kinh doanh vào mô hình máy học.</p>

        <!-- Figure 1 -->
        <div class="figure-wrapper">
          <div class="figure-header">
            <span>KIẾN TRÚC HỆ THỐNG PHÁT HIỆN GIAN LẬN</span>
            <span class="figure-badge">Hình 1</span>
          </div>
          <div class="figure-img-container">
            <img src="figures_paper1/fig_p4_1.jpeg" alt="Hình 1: Sơ đồ hệ thống phát hiện gian lận" class="figure-img" />
          </div>
          <div class="figure-caption">
            <strong>Hình 1:</strong> Đối chiếu tiếp cận truyền thống (Traditional Approach) dựa trên tỷ số tài chính chọn lọc thủ công và tiếp cận đề xuất (Proposed Approach) nạp trực tiếp biến số kế toán thô vào thuật toán học thích nghi mất cân bằng lớp.
          </div>
        </div>

        <p>Hệ thống 24 biến số thô bao gồm: Tài sản ngắn hạn (<code>act</code>), Phải trả người bán (<code>ap</code>), Tổng tài sản (<code>at</code>), Vốn chủ sở hữu (<code>ceq</code>), Tiền & tương đương tiền (<code>che</code>), Giá vốn hàng bán (<code>cogs</code>), Nợ ngắn hạn (<code>dlc</code>), Nợ dài hạn (<code>dltt</code>), Khấu hao (<code>dp</code>), EBIT (<code>ebit</code>), Hàng tồn kho (<code>invt</code>), Lợi nhuận ròng (<code>ni</code>), Doanh thu thuần (<code>sale</code>), Chi phí bán hàng & QLDN (<code>xsga</code>)...</p>
      </section>

      <!-- Section 3 -->
      <section id="sec3">
        <h2 class="section-title"><span class="section-number">3</span> CƠ SỞ DỮ LIỆU THỰC NGHIỆM AAERs (SEC 1982–2010)</h2>
        <p>Nghiên cứu thu thập toàn bộ dữ liệu vi phạm kế toán chính thức từ <strong>Ủy ban Chứng khoán Hoa Kỳ (SEC)</strong> trong gần 30 năm, tạo nên bộ dữ liệu mẫu lớn nhất và khách quan nhất trong y văn kế toán tài chính.</p>

        <div class="table-container">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Tên Tập Dữ Liệu</th>
                <th>Giai Đoạn</th>
                <th>Tổng Số Năm-Công Ty</th>
                <th>Số Vụ Gian Lận (%)</th>
                <th>Số Mẫu Liêm Chính (%)</th>
                <th>Số Lượng Thuộc Tính</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>USRaw 0paired (Toàn bộ)</strong></td>
                <td>1991–2005</td>
                <td>90.172 (100%)</td>
                <td>632 (0,70%)</td>
                <td>89.540 (99,30%)</td>
                <td>24 biến kế toán thô</td>
              </tr>
              <tr>
                <td>• Mẫu huấn luyện (Train)</td>
                <td>1991–2002</td>
                <td>72.456 (100%)</td>
                <td>514 (0,71%)</td>
                <td>71.942 (99,29%)</td>
                <td>24 biến thô</td>
              </tr>
              <tr>
                <td>• Mẫu kiểm thử ngoài mẫu (Test)</td>
                <td>2003–2005</td>
                <td>17.716 (100%)</td>
                <td>118 (0,67%)</td>
                <td>17.598 (99,33%)</td>
                <td>24 biến thô</td>
              </tr>
              <tr>
                <td><strong>USRaw 1paired (Cặp 2 năm liên tiếp)</strong></td>
                <td>1991–2005</td>
                <td>77.605 (100%)</td>
                <td>548 (0,62%)</td>
                <td>77.057 (99,38%)</td>
                <td>48 biến (năm t và t-1)</td>
              </tr>
              <tr>
                <td><strong>USRatio (Tập 11 tỷ số tài chính)</strong></td>
                <td>1991–2005</td>
                <td>88.875 (100%)</td>
                <td>693 (0,78%)</td>
                <td>88.182 (99,22%)</td>
                <td>11 tỷ số (Dechow 2011)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Section 4 -->
      <section id="sec4">
        <h2 class="section-title"><span class="section-number">4</span> THUẬT TOÁN HỌC MÁY XỬ LÝ MẤT CÂN BẰNG LỚP CỰC ĐOAN</h2>
        <p>Vì tỷ lệ gian lận thực tế chỉ chiếm 0,7%, nếu dùng các thuật toán thông thường, mô hình sẽ bị "nghiêng" hẳn về việc đoán công ty không gian lận để đạt độ chính xác ảo. Tác giả áp dụng 2 nhóm phương pháp:</p>

        <h3 class="sub-section-title">4.1 Biased-Penalty Support Vector Machine (BP-SVM)</h3>
        <p>Mô hình BP-SVM nhân thêm hệ số phạt <em>p</em> cho các trường hợp bỏ lọt công ty gian lận, với hệ số phạt được tính theo đúng tỷ lệ mất cân bằng dữ liệu:</p>
        
        <div class="formula-box">
          min w, b, &xi; &nbsp; &frac12; ||w||&sup2; + C &times; [ p &Sigma;<sub>i &isin; Frauds</sub> &xi;<sub>i</sub> + &Sigma;<sub>j &isin; Non-frauds</sub> &xi;<sub>j</sub> ]<br>
          với tham số phạt: p = N<sub>non-fraud</sub> / N<sub>fraud</sub> = 71.942 / 514 &approx; 139,96
        </div>

        <h3 class="sub-section-title">4.2 Học kết hợp EasyEnsemble và BalancedCascade</h3>
        <p>Sử dụng tập hợp nhiều bộ phân loại AdaBoost và Cây quyết định (Decision Trees) trên các tập con cân bằng, giúp mô hình vừa học được quy luật chung của số đông vừa nhận diện chuẩn xác các mẫu gian lận tinh vi.</p>
      </section>

      <!-- Section 5 -->
      <section id="sec5">
        <h2 class="section-title"><span class="section-number">5</span> KẾT QUẢ THỰC NGHIỆM ĐỊNH LƯỢNG & ĐỐI CHIẾU</h2>
        <p>Kết quả kiểm thử trên 17.716 năm-công ty độc lập (giai đoạn 2003–2005) khẳng định tính ưu việt áp đảo của tiếp cận mới:</p>

        <div class="table-container">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Dữ Liệu</th>
                <th>Phương Pháp Thuật Toán</th>
                <th>Sensitivity (%) (Bắt gian lận)</th>
                <th>Specificity (%) (Đúng công ty sạch)</th>
                <th>Balanced Accuracy (BAC %)</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: rgba(239, 68, 68, 0.05);">
                <td><strong>USRatio (11 tỷ số)</strong></td>
                <td>Mô hình Logit (Dechow et al. 2011)</td>
                <td>64,00%</td>
                <td>55,99%</td>
                <td><strong>60,00%</strong></td>
              </tr>
              <tr>
                <td>USRaw 1paired</td>
                <td>SVM-FK (Cecchini et al. 2010)</td>
                <td>65,45%</td>
                <td>74,03%</td>
                <td>69,74%</td>
              </tr>
              <tr>
                <td>USRaw 0paired (24 biến thô)</td>
                <td>BP-SVM Tuyến tính (Linear)</td>
                <td>70,34%</td>
                <td>68,96%</td>
                <td>69,65%</td>
              </tr>
              <tr style="background: rgba(59, 130, 246, 0.05);">
                <td>USRaw 0paired (24 biến thô)</td>
                <td><strong>BP-SVM Đa thức bậc 3 (Poly-3)</strong></td>
                <td><strong>73,73%</strong></td>
                <td><strong>72,83%</strong></td>
                <td><strong>73,28%</strong></td>
              </tr>
              <tr style="background: rgba(16, 185, 129, 0.08); font-weight: 600;">
                <td><strong>USRaw 0paired (24 biến thô)</strong></td>
                <td><strong>BalancedCascade (Ensemble)</strong></td>
                <td><strong>72,54%</strong></td>
                <td><strong>82,52%</strong></td>
                <td><strong>77,53%</strong></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout callout-success">
          <div class="callout-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
              <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            Ý nghĩa của thành tựu BAC 77,53%:
          </div>
          <p style="margin-bottom:0;">Mô hình BalancedCascade trên dữ liệu thô không chỉ tăng tỷ lệ bắt trúng gian lận lên 72,54% mà quan trọng hơn, đã nâng độ đặc hiệu (Specificity) lên 82,52%. Điều này giải quyết nỗi đau lớn nhất của kiểm toán viên: <strong>giảm thiểu hơn 80% các báo động giả</strong>, giúp kiểm toán viên không bị ngập trong các cuộc điều tra vô ích.</p>
        </div>
      </section>

      <!-- Section 6 -->
      <section id="sec6">
        <h2 class="section-title"><span class="section-number">6</span> ĐÚC KẾT CHO NGHỀ NGHIỆP KẾ TOÁN & KIỂM TOÁN</h2>
        <ul>
          <li><strong>Xóa bỏ định kiến về tỷ số tài chính:</strong> Máy học có khả năng tự động khám phá các tương tác phi tuyến tính phức tạp giữa các số liệu kế toán thô mà mắt người không thể tự tạo ra bằng công thức chia tỷ lệ thông thường.</li>
          <li><strong>Sẵn sàng triển khai thực tiễn:</strong> Thời gian huấn luyện và phân loại của mô hình chỉ mất vài giây, cho phép các cơ quan như Ủy ban Chứng khoán, Kiểm toán Nhà nước hoặc các công ty kiểm toán Big 4 quét toàn bộ hàng nghìn công ty niêm yết ngay khi BCTC vừa được nộp.</li>
          <li><strong>Bảo vệ doanh nghiệp làm ăn chân chính:</strong> Ngăn chặn tình trạng cạnh tranh không lành mạnh do các công ty gian lận tạo ra nhằm thu hút vốn đầu tư sai lệch.</li>
        </ul>
      </section>

      <!-- Section 7 -->
      <section id="sec7">
        <h2 class="section-title"><span class="section-number">7</span> TÀI LIỆU THAM KHẢO CHÍNH (REFERENCES)</h2>
        <ul class="references-list">
          <li><strong>Beneish, M. D. (1999).</strong> The detection of earnings manipulation. <em>Financial Analysts Journal</em>, 55(5), 24–36.</li>
          <li><strong>Dechow, P. M., Ge, W., Larson, C. R., & Sloan, R. G. (2011).</strong> Predicting material accounting misstatements. <em>Contemporary Accounting Research</em>, 28(1), 17–82.</li>
          <li><strong>Cecchini, M., Aytug, H., Koehler, G. J., & Pathak, P. (2010).</strong> Making words work: Using financial text as a predictor of financial events. <em>Decision Support Systems</em>, 50(1), 164–175.</li>
          <li><strong>Bao, Y., Ke, B., Li, B., Yu, Y. J., & Zhang, J. (2020).</strong> Detecting accounting fraud in publicly traded U.S. firms using a machine learning approach. <em>Journal of Accounting Research</em>, 58(1), 199–235.</li>
          <li><strong>Liu, X.-Y., & Zhou, Z.-H. (2013).</strong> Ensemble methods for class imbalance learning. <em>Imbalanced Learning: Foundations, Algorithms, and Applications</em>, Wiley, 61–82.</li>
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
        active_paper_idx=1
    )

    html_path = os.path.join(PAPERS_DIR, "paper_1_Detecting_Accounting_Fraud_tiengviet.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated HTML: {os.path.basename(html_path)}")

if __name__ == "__main__":
    build()
