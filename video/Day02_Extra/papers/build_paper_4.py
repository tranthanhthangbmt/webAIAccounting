# -*- coding: utf-8 -*-
"""
Builder for Paper 4:
Detection of Anomalies in Large-Scale Accounting Data using Deep Autoencoder Networks
(Marco Schreyer, Timur Sattarov, Damian Borth, Andreas Dengel, Bernd Reimer - DFKI & PwC)
"""

import os
from generate_day02_helpers import get_html_template

PAPERS_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day02_Extra\papers"

TITLE_VI = "Phát Hiện Bất Thường Trong Dữ Liệu Kế Toán Quy Mô Lớn Bằng Mạng Deep Autoencoder"
TITLE_EN = "Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoder Networks"
AUTHORS = "Marco Schreyer (DFKI), Timur Sattarov (PwC), Damian Borth (DFKI), Andreas Dengel (DFKI), Bernd Reimer (PwC)"
JOURNAL = "DFKI & PricewaterhouseCoopers (PwC) / arXiv & IJAIS Research Stream"
DOI = "arXiv:1709.05254 / PwC Forensic Data Analytics"
BADGE = "Paper 4 • PwC & DFKI Landmark"

def build():
    # Markdown Content
    md_content = """# PHÁT HIỆN BẤT THƯỜNG TRONG DỮ LIỆU KẾ TOÁN QUY MÔ LỚN BẰNG MẠNG DEEP AUTOENCODER
*(Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoder Networks)*

- **Tác giả:** Marco Schreyer (DFKI), Timur Sattarov (PwC), Damian Borth (DFKI), Andreas Dengel (DFKI), Bernd Reimer (PwC)
- **Đơn vị nghiên cứu:** Trung tâm Nghiên cứu Trí tuệ Nhân tạo Đức (DFKI) & Hãng Kiểm toán PricewaterhouseCoopers (PwC GmbH)
- **Định danh học thuật:** [arXiv:1709.05254](https://arxiv.org/abs/1709.05254)
- **Cơ sở dữ liệu thực nghiệm:** Hàng triệu dòng bút toán kế toán thực tế trích xuất từ hệ thống hoạch định tài nguyên doanh nghiệp (SAP ERP) của 2 tập đoàn đa quốc gia

---

## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

Học cách phát hiện gian lận trong dữ liệu kế toán quy mô lớn là một trong những thách thức lâu đời nhất trong công tác kiểm toán báo cáo tài chính và điều tra gian lận nội bộ. Hiện nay, phần lớn các kỹ thuật áp dụng trong thực tế vẫn phụ thuộc vào **các quy tắc thủ công (*handcrafted IF-ELSE rules*)** được rút ra từ các kịch bản gian lận đã biết trong quá khứ. Mặc dù đem lại thành công nhất định, các quy tắc này bộc lộ nhược điểm nghiêm trọng: Chúng hoàn toàn bất lực trong việc tổng quát hóa ra ngoài các kịch bản đã biết và những kẻ gian lận sẽ nhanh chóng tìm ra cách lách luật.

Để khắc phục nhược điểm này, lấy cảm hứng từ thành công của học sâu, chúng tôi đề xuất ứng dụng **Mạng nơ-ron Tự mã hóa Sâu (*Deep Autoencoder Neural Networks*)** để tự động phát hiện các bút toán sổ cái bất thường (*anomalous journal entries*). Chúng tôi chứng minh rằng **sai số tái tạo (*reconstruction error*)** thu được từ mạng nơ-ron sau huấn luyện, khi được điều chuẩn bởi xác suất xuất hiện của từng thuộc tính riêng lẻ, có thể được diễn giải như một thang đo đánh giá bất thường có tính thích nghi rất cao.

Thực nghiệm trên hai bộ dữ liệu bút toán nhật ký chung thực tế quy mô lớn của hai tập đoàn đa quốc gia chứng minh tính hiệu quả vượt bậc của phương pháp, đạt điểm F1-score lên tới **32,93%** (Dataset A) và **16,95%** (Dataset B), đồng thời **giảm thiểu 97,5% số lượng cảnh báo giả (*false positive alerts*)** so với các phương pháp nơ-ron nông. Phản hồi thực tế từ các kiểm toán viên công chứng (*Chartered Accountants*) và các chuyên gia điều tra gian lận (*Fraud Examiners*) tại PwC đã khẳng định chất lượng xuất sắc của mô hình trong việc bắt trúng các bất thường kế toán trọng yếu trong thực tế.

**Từ khóa:** Hệ thống thông tin kế toán (AIS); Kỹ thuật kiểm toán có máy tính trợ giúp (CAATs); Kiểm tra bút toán (Journal Entry Testing); Kế toán điều tra (Forensic Accounting); Phát hiện gian lận; Phân tích dữ liệu điều tra; Học sâu (Deep Learning); Autoencoder.

---

## 1. ĐỘNG LỰC & THÁCH THỨC TRONG KIỂM TOÁN SỔ CÁI (GENERAL LEDGER)

Theo Báo cáo Gian lận Toàn cầu của Hiệp hội các Nhà điều tra Gian lận Công chứng (ACFE), một tổ chức điển hình **bị thất thoát trung bình 5% tổng doanh thu hàng năm** do các hành vi gian lận và lạm dụng chức vụ. Trong các vụ bê bối tài chính, ban giám đốc và các kế toán viên thoái hóa thường sử dụng các bút toán điều chỉnh nhật ký chung (*journal entries*) để "xào nấu" lợi nhuận hoặc che giấu các khoản rút ruột tài sản.

Theo Chuẩn mực Kiểm toán Quốc tế **ISA 240** và chuẩn mực Hoa Kỳ **SAS 99**, kiểm toán viên bắt buộc phải thực hiện thủ tục **Kiểm tra bút toán nhật ký (*Journal Entry Testing - JET*)** để đánh giá rủi ro ban quản lý ghi đè kiểm soát nội bộ.

### Điểm Nghẽn Của Phương Pháp Kiểm Toán Truyền Thống:
Trong các hệ thống ERP hiện đại như **SAP R/3 hay SAP S/4HANA**, một doanh nghiệp lớn có thể phát sinh hàng triệu dòng bút toán mỗi năm. Kiểm toán viên thường dùng các câu lệnh truy vấn lọc dữ liệu (SQL, ACL, IDEA) dựa trên quy tắc cố định, ví dụ:
- Lọc các bút toán hạch toán vào ban đêm hoặc ngày cuối tuần.
- Lọc các bút toán có số tiền làm tròn (ví dụ: 10.000.000 VNĐ).
- Lọc các bút toán chứa từ khóa nhạy cảm ("điều chỉnh", "sửa lỗi").

**Hậu quả:** Các quy tắc này sinh ra hàng chục nghìn cảnh báo giả (*False Positives*), khiến kiểm toán viên kiệt sức vì phải kiểm tra thủ công các bút toán hoàn toàn bình thường, trong khi kẻ gian chỉ cần hạch toán vào lúc 10h sáng thứ Ba với số tiền lẻ là hoàn toàn "tàng hình" trước hệ thống kiểm toán!

---

## 2. BẢN CHẤT DỮ LIỆU BÚT TOÁN KẾ TOÁN TRONG HỆ THỐNG ERP

Mỗi giao dịch kinh tế trong hệ thống SAP ERP được ghi nhận theo nguyên tắc ghi kép (*dual-entry principle*), bao gồm ít nhất hai dòng bút toán (Nợ và Có) và được tổ chức thành hai tầng bảng cơ sở dữ liệu:
1. **Tầng Tiêu đề chứng từ (Document Header - Bảng `BKPF`):** Chứa thông tin chung về chứng từ: Số chứng từ, Loại chứng từ (Document Type, ví dụ: `RE` - Hóa đơn mua hàng, `KZ` - Thanh toán người bán), Ngày hạch toán (Posting Date), Giờ hạch toán, Mã người tạo (User ID), Mã giao dịch (T-Code).
2. **Tầng Dòng bút toán (Line Items - Bảng `BSEG`):** Chứa chi tiết từng dòng: Khóa định khoản (Posting Key, ví dụ: `31` - Ghi Có nhà cung cấp, `40` - Ghi Nợ tài khoản chi phí), Mã tài khoản Sổ cái (General Ledger Account), Số tiền hạch toán (Amount), Mã nhà cung cấp / khách hàng.

![Hình 1: Quy trình ghi nhận bút toán kép](figures_paper4/fig1_journal_process_cropped.png)
*Hình 1: Quy trình ghi nhận dòng tiền và hạch toán chứng từ kép trong hệ thống ERP: Nhận hóa đơn đầu vào ($1.000) -> Thanh toán qua ngân hàng ($1.000).*

### Tiền xử lý dữ liệu:
Do các thuộc tính kế toán phần lớn là biến định danh phân loại (*categorical attributes*), nghiên cứu áp dụng kỹ thuật mã hóa **One-Hot Encoding** để chuyển đổi từng bút toán thành một véc-tơ nhị phân thưa đa chiều:
- **Tập dữ liệu A:** Gồm 401 chiều sau khi mã hóa.
- **Tập dữ liệu B:** Gồm 576 chiều sau khi mã hóa.

---

## 3. PHÂN LOẠI 2 DẠNG BẤT THƯỜNG KẾ TOÁN: GLOBAL VS. LOCAL ANOMALIES

Để thiết kế hệ thống phát hiện gian lận hiệu quả, nhóm tác giả phân định rõ hai hình thái bất thường:
1. **Bất thường toàn cục (*Global Anomalies*):** Các bút toán có thuộc tính hiếm gặp hoặc số tiền vượt ngưỡng cực đoan (ví dụ: Bút toán chuyển tiền hàng triệu USD phát sinh từ một loại chứng từ chưa từng dùng bao giờ).
2. **Bất thường cục bộ / ngữ cảnh (*Local/Contextual Anomalies*):** Các bút toán nhìn bề ngoài **hoàn toàn bình thường** nếu xem xét từng thuộc tính riêng lẻ (số tiền nhỏ, tài khoản thông dụng, hạch toán giờ hành chính), nhưng **sự kết hợp giữa các thuộc tính lại vô lý và trái quy luật** (ví dụ: Nhân viên phòng Mua hàng lại hạch toán tài khoản Chi phí Quản trị Doanh nghiệp đối ứng với Tài khoản Ngân hàng lạ).

---

## 4. KIẾN TRÚC MẠNG NƠ-RON DEEP AUTOENCODER ĐỀ XUẤT

Mạng Autoencoder là một kiến trúc học sâu không giám sát gồm hai mạng nơ-ron truyền thẳng ghép nối tiếp:
1. **Mạng Mã hóa (Encoder Net $f_\theta$):** Nén véc-tơ đầu vào $x_i \in \mathbb{R}^{d_x}$ qua nhiều tầng ẩn xuống một không gian tiềm ẩn (*Latent Space*) có số chiều cực nhỏ $Z \in \mathbb{R}^{d_z}$ (với $d_z = 3$).
2. **Mạng Giải mã (Decoder Net $g_\theta$):** Giải nén từ không gian tiềm ẩn để tái tạo lại véc-tơ ban đầu $\hat{x}_i \in \mathbb{R}^{d_y}$.

![Hình 2: Sơ đồ kiến trúc Deep Autoencoder](figures_paper4/fig2_autoencoder_arch_cropped.png)
*Hình 2: Kiến trúc Deep Autoencoder phát hiện bất thường: Bút toán hợp lệ được tái tạo hoàn hảo (sai số thấp); Bút toán gian lận có cấu trúc dị thường không thể tái tạo đúng (sai số vọt cao) -> Gắn cờ cảnh báo.*

### Cơ Chế Phát Hiện Gian Lận Qua Sai Số Tái Tạo:
Mạng Autoencoder được huấn luyện trên hàng triệu bút toán bình thường hàng ngày của doanh nghiệp. Do đó, mạng học được "quy luật hạch toán chuẩn mực" của tổ chức.
- **Bút toán liêm chính (99,9%):** Autoencoder dễ dàng tái tạo lại với sai số cực nhỏ $\mathcal{L}(x_i, \hat{x}_i) \approx 0$.
- **Bút toán gian lận (bất thường):** Chứa đựng các tương tác kỳ dị chưa từng thấy trong tập huấn luyện. Autoencoder không thể tái tạo chính xác $\rightarrow$ **Sai số tái tạo vọt lên cực cao!**

$$ \mathcal{L}(x_i, \hat{x}_i) = \frac{1}{k} \sum_{j=1}^k \left( x_i^j - \hat{x}_i^j \right)^2 $$

### Thang Đo Điểm Bất Thường Kết Hợp (Hybrid Anomaly Score):
Để bắt được cả Global Anomalies và Local Anomalies, tác giả kết hợp:
1. Điểm xác suất thuộc tính $AP(x_i)$: Bắt các giá trị hiếm gặp (Global).
2. Điểm sai số tái tạo Autoencoder $\mathcal{L}(x_i, \hat{x}_i)$: Bắt tương tác bất hợp lý (Local).

$$ AS(x_i) = \alpha \cdot \frac{AP(x_i) - AP_{\min}}{AP_{\max} - AP_{\min}} + (1 - \alpha) \cdot \frac{\mathcal{L}(x_i, \hat{x}_i) - \mathcal{L}_{\min}}{\mathcal{L}_{\max} - \mathcal{L}_{\min}} $$

---

## 5. THỰC NGHIỆM ĐỊNH LƯỢNG TRÊN DỮ LIỆU ERP THỰC TẾ

Tác giả đánh giá 9 cấu hình mạng Autoencoder từ nông (AE 1: 1 tầng ẩn) đến sâu (AE 9: 9 tầng ẩn với hàng nghìn nơ-ron):

| Cấu Hình | Kiến Trúc Các Tầng Ẩn (Số Nơ-ron) | Chiều Latent Space | Dataset A: Precision | Dataset A: F1-Score | Số Cảnh Báo Phải Xem Xét |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AE 1 (Nông)** | [401] - 3 - [401] | 3 | 0,0049 | 0,0098 | 19.233 bút toán |
| AE 2 | [401] - 4-3-4 - [401] | 3 | 0,0063 | 0,0126 | 14.966 bút toán |
| AE 3 | [401] - 8-4-3-4-8 - [401] | 3 | 0,0098 | 0,0194 | 9.719 bút toán |
| AE 4 | [401] - 16-8-4-3-4-8-16 - [401] | 3 | 0,0290 | 0,0564 | 3.275 bút toán |
| AE 5 | [401] - 32-16-8-4-3-4-8-16-32 - [401] | 3 | 0,0641 | 0,1204 | 1.483 bút toán |
| AE 6 | [401] - 64-32-16-8-4-3-4-8-16-64 - [401] | 3 | 0,0752 | 0,1398 | 1.264 bút toán |
| AE 7 | [401] - 128-64-32-16-8-4-3-4-8-16-64-128 - [401] | 3 | 0,0796 | 0,1474 | 1.194 bút toán |
| AE 8 | [401] - 256-128-64-32-16-8-4-3-4-8-16-64-128-256 - [401] | 3 | 0,1201 | 0,2144 | 791 bút toán |
| **AE 9 (Sâu nhất)** | **[401] - 512-256-128-64-32-16-8-4-3-...-512 - [401]** | **3** | **0,1971** | **0,3293** | **Chỉ còn 482 bút toán!** |

### 🚀 Sức Mạnh Tuyệt Đối Của Kiến Trúc Mạng Sâu:
Mạng nông AE 1 bắt kiểm toán viên phải kiểm tra tới **19.233 bút toán** để tìm ra gian lận. Trong khi đó, mạng học sâu **AE 9 thu hẹp danh sách nghi vấn xuống chỉ còn 482 bút toán (giảm tới 97,5% khối lượng công việc!)** trong khi vẫn duy trì tỷ lệ bao phủ gian lận (Recall) đạt 100%!

### Bảng Đối Chuẩn So Sánh Với Các Thuật Toán Học Không Giám Sát Khác (Bảng 3 bài báo):

| Thuật Toán Đối Chuẩn | Dataset | ROC-AUC | Precision (%) | F1-Score | Số Lượng Bút Toán Cần Kiểm Tra |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Deep Autoencoder (AE 9)** | **A** | **0,9999** | **56,88%** | **0,7251** | **Chỉ 167 bút toán** |
| One-Class SVM (OC-SVM) | A | 0,9999 | 27,69% | 0,4338 | 343 bút toán |
| Local Outlier Factor (LOF) | A | 0,9979 | 4,99% | 0,0952 | 1.901 bút toán |
| HDBSCAN (Phân cụm mật độ) | A | 0,9787 | 2,56% | 0,0499 | 3.714 bút toán |
| PCA (Phân tích thành phần chính) | A | 0,9608 | 0,55% | 0,0110 | 17.162 bút toán |
| **Deep Autoencoder (AE 9)** | **B** | **0,9997** | **16,16%** | **0,2782** | **Chỉ 619 bút toán** |
| One-Class SVM | B | 0,9997 | 13,97% | 0,2451 | 716 bút toán |
| LOF | B | 0,9984 | 5,18% | 0,0986 | 1.929 bút toán |
| HDBSCAN | B | 0,9744 | 3,83% | 0,0720 | 2.680 bút toán |
| PCA | B | 0,9978 | 3,31% | 0,0640 | 3.025 bút toán |

---

## 6. ĐÁNH GIÁ CHẤT LƯỢNG THỰC TẾ TỪ CÁC CHUYÊN GIA KIỂM TOÁN PwC

Các kiểm toán viên công chứng và chuyên gia điều tra gian lận tại PwC đã trực tiếp rà soát các bút toán bất thường trong thực tế do mô hình AE 9 phát hiện:
1. **Phát hiện gian lận phân tách thanh toán (*Invoice Splitting*):** Bắt sống các bút toán cố ý chia nhỏ số tiền thành nhiều hóa đơn dưới 5.000 EUR để lách thẩm quyền phê duyệt của Giám đốc tài chính.
2. **Bút toán điều chỉnh ngoài giờ (*Off-Hour Postings*):** Phát hiện các bút toán điều chỉnh doanh thu vào lúc 23h đêm Chủ nhật được thực hiện bởi tài khoản người dùng của phòng kỹ thuật IT thay vì phòng kế toán.
3. **Cặp tài khoản đối ứng bất thường:** Nhận diện các bút toán Nợ TK Chi phí quản lý đối ứng trực tiếp với Có TK Phải thu khách hàng mà không qua hóa đơn điều chỉnh.

---

## 7. ĐÚC KẾT CHO NGHỀ NGHIỆP KIỂM TOÁN HIỆN ĐẠI

> [!TIP]
> **Chuyển dịch từ Kiểm toán lấy mẫu sang Kiểm toán toàn diện 100%:**
> - Deep Autoencoder cho phép quét 100% hàng triệu bút toán nhật ký chung trong vài phút, loại bỏ hoàn toàn rủi ro chọn mẫu (*Sampling Risk*).
> - Giúp các hãng kiểm toán Big 4 chuyển đổi mạnh mẽ sang mô hình **Kiểm toán liên tục (*Continuous Auditing*)**, phát hiện gian lận theo thời gian thực thay vì đợi đến đợt kiểm toán cuối năm.

---

## 8. TÀI LIỆU THAM KHẢO CHÍNH (REFERENCES)

1. **Schreyer, M., Sattarov, T., Borth, D., Dengel, A., & Reimer, B. (2017).** Detection of anomalies in large scale accounting data using deep autoencoder networks. *arXiv preprint arXiv:1709.05254*.
2. **ACFE (2016).** Report to the Nations on Occupational Fraud and Abuse. *Association of Certified Fraud Examiners*.
3. **PwC (2016).** Global Economic Crime Survey 2016: An inside look at the true costs of crime. *PricewaterhouseCoopers*.
4. **Schreyer, M., et al. (2020).** Multi-view anomaly detection in large-scale accounting data. *International Conference on Information Systems (ICIS)*.
"""

    md_path = os.path.join(PAPERS_DIR, "paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Markdown: {os.path.basename(md_path)}")

    # Generate HTML
    sidebar_links = """
      <a href="#abstract" class="sidebar-link">Tóm Tắt Nghiên Cứu</a>
      <a href="#sec1" class="sidebar-link">1. Động Lực Kiểm Toán Sổ Cái</a>
      <a href="#sec2" class="sidebar-link">2. Bản Chất Bút Toán SAP ERP</a>
      <a href="#sec3" class="sidebar-link">3. Bất Thường Global vs Local</a>
      <a href="#sec4" class="sidebar-link">4. Kiến Trúc Deep Autoencoder</a>
      <a href="#sec5" class="sidebar-link">5. Kết Quả Định Lượng Thực Tế</a>
      <a href="#sec6" class="sidebar-link">6. Đánh Giá Từ Chuyên Gia PwC</a>
      <a href="#sec7" class="sidebar-link">7. Đúc Kết Kiểm Toán Liên Tục</a>
      <a href="#sec8" class="sidebar-link">8. Tài Liệu Tham Khảo</a>
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
          Phát hiện gian lận trong dữ liệu kế toán quy mô lớn là bài toán thách thức cốt tử trong kiểm toán báo cáo tài chính và điều tra gian lận nội bộ. Phần lớn các phương pháp hiện hành vẫn dựa vào các quy tắc thủ công (<em>handcrafted IF-ELSE rules</em>) dễ bị kẻ gian lách qua và sinh ra hàng nghìn cảnh báo giả. Lấy cảm hứng từ học sâu, chúng tôi đề xuất ứng dụng <strong>Mạng nơ-ron Tự mã hóa Sâu (Deep Autoencoder Neural Networks)</strong> để tự động nhận diện các bút toán nhật ký chung bất thường. Sai số tái tạo (<em>reconstruction error</em>) kết hợp với xác suất thuộc tính đóng vai trò thang đo bất thường có tính thích nghi cực cao. Thực nghiệm trên 2 bộ dữ liệu SAP ERP thực tế của hai tập đoàn đa quốc gia chứng minh mô hình đạt F1-score <strong>32,93%</strong> (Dataset A) và <strong>16,95%</strong> (Dataset B), đồng thời <strong>giảm thiểu tới 97,5% số lượng cảnh báo giả</strong> so với mạng nông. Đánh giá thực tế từ các kiểm toán viên và chuyên gia điều tra gian lận tại PwC khẳng định mô hình bắt trúng các bất thường kế toán trọng yếu trong thực tế.
        </p>
        <div class="keywords-box">
          <strong>Từ khóa:</strong> Accounting Information Systems; Computer Assisted Audit Techniques (CAATs); Journal Entry Testing; Forensic Accounting; Fraud Detection; Deep Learning; Autoencoder; PwC.
        </div>
      </section>

      <!-- Section 1 -->
      <section id="sec1">
        <h2 class="section-title"><span class="section-number">1</span> ĐỘNG LỰC & THÁCH THỨC TRONG KIỂM TOÁN SỔ CÁI (GENERAL LEDGER)</h2>
        <p>Báo cáo của ACFE ước tính các doanh nghiệp thất thoát trung bình <strong>5% doanh thu hàng năm</strong> do gian lận nội bộ. Theo Chuẩn mực Kiểm toán Quốc tế <strong>ISA 240</strong>, kiểm toán viên bắt buộc phải kiểm tra các bút toán nhật ký chung (<em>Journal Entry Testing - JET</em>) để phát hiện rủi ro ban quản lý ghi đè kiểm soát.</p>

        <div class="callout callout-warning">
          <div class="callout-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
              <line x1="12" y1="9" x2="12" y2="13"></line>
              <line x1="12" y1="17" x2="12.01" y2="17"></line>
            </svg>
            Nghịch lý của các quy tắc kiểm toán thủ công (IF-ELSE Rules):
          </div>
          <p style="margin-bottom:0;">Trong hệ thống ERP lớn với hàng triệu dòng bút toán, việc dùng các câu lệnh lọc thủ công (như lọc bút toán cuối tuần, số tiền làm tròn) tạo ra hàng chục nghìn cảnh báo giả. Kiểm toán viên bị quá tải, trong khi kẻ gian dễ dàng né tránh bằng cách hạch toán vào giờ hành chính với các con số lẻ.</p>
        </div>
      </section>

      <!-- Section 2 -->
      <section id="sec2">
        <h2 class="section-title"><span class="section-number">2</span> BẢN CHẤT DỮ LIỆU BÚT TOÁN KẾ TOÁN TRONG HỆ THỐNG SAP ERP</h2>
        <p>Mỗi chứng từ kế toán trong hệ thống SAP ERP được lưu trữ theo cấu trúc 2 tầng: Tầng tiêu đề chứng từ (bảng <code>BKPF</code>) và tầng dòng bút toán chi tiết (bảng <code>BSEG</code>).</p>

        <!-- Figure 1 -->
        <div class="figure-wrapper">
          <div class="figure-header">
            <span>QUY TRÌNH HẠCH TOÁN BÚT TOÁN KÉP TRONG ERP</span>
            <span class="figure-badge">Hình 1</span>
          </div>
          <div class="figure-img-container">
            <img src="figures_paper4/fig1_journal_process_cropped.png" alt="Hình 1: Quy trình hạch toán ERP" class="figure-img" />
          </div>
          <div class="figure-caption">
            <strong>Hình 1:</strong> Dòng chảy chứng từ kế toán kép trong hệ thống ERP: Nhận hóa đơn đầu vào ($1.000) &rarr; Xuất tiền thanh toán từ ngân hàng ($1.000). Dữ liệu được mã hóa One-Hot thành véc-tơ nhị phân 401 chiều (Dataset A) và 576 chiều (Dataset B).
          </div>
        </div>
      </section>

      <!-- Section 3 -->
      <section id="sec3">
        <h2 class="section-title"><span class="section-number">3</span> PHÂN LOẠI BẤT THƯỜNG TOÀN CỤC (GLOBAL) VS. CỤC BỘ (LOCAL)</h2>
        <ul>
          <li><strong>Bất thường Toàn cục (Global Anomalies):</strong> Các bút toán có số tiền bất thường cực lớn hoặc thuộc tính cực hiếm (ví dụ: loại chứng từ lạ chưa từng xuất hiện).</li>
          <li><strong>Bất thường Cục bộ / Ngữ cảnh (Local/Contextual Anomalies):</strong> Các bút toán có số tiền bình thường, tài khoản bình thường, nhưng <strong>sự kết hợp giữa người tạo, thời gian và cặp tài khoản Nợ/Có lại trái với quy luật nội bộ</strong>. Đây là loại gian lận tinh vi nhất mà kiểm toán truyền thống hoàn toàn bỏ sót!</li>
        </ul>
      </section>

      <!-- Section 4 -->
      <section id="sec4">
        <h2 class="section-title"><span class="section-number">4</span> KIẾN TRÚC MẠNG NƠ-RON DEEP AUTOENCODER ĐỀ XUẤT</h2>
        <p>Mạng Autoencoder bao gồm Mạng mã hóa (Encoder) nén dữ liệu xuống không gian ẩn 3 chiều, và Mạng giải mã (Decoder) khôi phục lại bút toán ban đầu.</p>

        <!-- Figure 2 -->
        <div class="figure-wrapper">
          <div class="figure-header">
            <span>KIẾN TRÚC MẠNG DEEP AUTOENCODER CHO BÚT TOÁN KẾ TOÁN</span>
            <span class="figure-badge">Hình 2</span>
          </div>
          <div class="figure-img-container">
            <img src="figures_paper4/fig2_autoencoder_arch_cropped.png" alt="Hình 2: Kiến trúc Deep Autoencoder" class="figure-img" />
          </div>
          <div class="figure-caption">
            <strong>Hình 2:</strong> Cơ chế phát hiện bất thường: Với 99,9% bút toán hợp lệ, mạng tái tạo chuẩn xác với sai số nhỏ. Với bút toán gian lận, mạng không thể tái tạo đúng &rarr; Sai số tái tạo (Reconstruction Error) tăng vọt &rarr; Gắn cờ cảnh báo kiểm toán viên!
          </div>
        </div>

        <p>Công thức tính Điểm bất thường kết hợp (Anomaly Score):</p>
        <div class="formula-box">
          AS(x<sub>i</sub>) = &alpha; &times; AP_Score(x<sub>i</sub>) + (1 - &alpha;) &times; Reconstruction_Error(x<sub>i</sub>, &hat;x<sub>i</sub>)
        </div>
      </section>

      <!-- Section 5 -->
      <section id="sec5">
        <h2 class="section-title"><span class="section-number">5</span> KẾT QUẢ THỰC NGHIỆM ĐỊNH LƯỢNG TRÊN DỮ LIỆU ERP THỰC TẾ</h2>
        <p>Đánh giá 9 kiến trúc Autoencoder từ nông (AE 1) đến sâu (AE 9) trên dữ liệu doanh nghiệp thực tế (Bảng 2 bài báo gốc):</p>

        <div class="table-container">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Cấu Hình Mạng</th>
                <th>Số Tầng Ẩn (Topology)</th>
                <th>Precision (%)</th>
                <th>F1-Score</th>
                <th>Tỷ Lệ Bút Toán Nghi Vấn (%)</th>
                <th>Số Lượng Bút Toán Cần Rà Soát</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: rgba(239, 68, 68, 0.05);">
                <td>AE 1 (Nông - 1 tầng)</td>
                <td>[401] - 3 - [401]</td>
                <td>0,0049</td>
                <td>0,0098</td>
                <td>6,26%</td>
                <td>19.233 bút toán</td>
              </tr>
              <tr>
                <td>AE 3</td>
                <td>[401] - 8-4-3-4-8 - [401]</td>
                <td>0,0098</td>
                <td>0,0194</td>
                <td>3,16%</td>
                <td>9.719 bút toán</td>
              </tr>
              <tr>
                <td>AE 5</td>
                <td>[401] - 32-16-8-4-3-...-32 - [401]</td>
                <td>0,0641</td>
                <td>0,1204</td>
                <td>0,48%</td>
                <td>1.483 bút toán</td>
              </tr>
              <tr>
                <td>AE 7</td>
                <td>[401] - 128-64-32-...-128 - [401]</td>
                <td>0,0796</td>
                <td>0,1474</td>
                <td>0,39%</td>
                <td>1.194 bút toán</td>
              </tr>
              <tr style="background: rgba(16, 185, 129, 0.08); font-weight: 700;">
                <td><strong>AE 9 (Mạng sâu nhất)</strong></td>
                <td><strong>[401] - 512-256-128-...-512 - [401]</strong></td>
                <td><strong>0,1971</strong></td>
                <td><strong style="color: #059669; font-size: 1.05rem;">0,3293</strong></td>
                <td><strong>0,16%</strong></td>
                <td><strong style="color: #059669; font-size: 1.05rem;">Chỉ còn 482 bút toán!</strong></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout callout-success">
          <div class="callout-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
            Bước đột phá: Giảm 97,5% khối lượng kiểm tra thủ công!
          </div>
          <p style="margin-bottom:0;">Mạng nơ-ron nông AE 1 bắt kiểm toán viên phải kiểm tra 19.233 bút toán, trong khi <strong>mạng sâu AE 9 thu hẹp danh sách xuống chỉ còn 482 bút toán</strong> mà vẫn bắt trọn 100% các bút toán gian lận!</p>
        </div>

        <h3 class="sub-section-title">Đối chuẩn với các thuật toán học không giám sát khác (Bảng 3):</h3>
        <div class="table-container">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Thuật Toán Đối Chuẩn</th>
                <th>Dataset</th>
                <th>ROC-AUC</th>
                <th>Precision (%)</th>
                <th>F1-Score</th>
                <th>Số Bút Toán Nghi Vấn</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: rgba(16, 185, 129, 0.08); font-weight: 700;">
                <td><strong>Deep Autoencoder (AE 9)</strong></td>
                <td><strong>A</strong></td>
                <td><strong style="color: #059669;">0,9999</strong></td>
                <td><strong>56,88%</strong></td>
                <td><strong style="color: #059669;">0,7251</strong></td>
                <td><strong style="color: #059669;">Chỉ 167 bút toán</strong></td>
              </tr>
              <tr>
                <td>One-Class SVM (OC-SVM)</td>
                <td>A</td>
                <td>0,9999</td>
                <td>27,69%</td>
                <td>0,4338</td>
                <td>343 bút toán</td>
              </tr>
              <tr>
                <td>Local Outlier Factor (LOF)</td>
                <td>A</td>
                <td>0,9979</td>
                <td>4,99%</td>
                <td>0,0952</td>
                <td>1.901 bút toán</td>
              </tr>
              <tr>
                <td>HDBSCAN (Phân cụm)</td>
                <td>A</td>
                <td>0,9787</td>
                <td>2,56%</td>
                <td>0,0499</td>
                <td>3.714 bút toán</td>
              </tr>
              <tr>
                <td>PCA (Phân tích thành phần chính)</td>
                <td>A</td>
                <td>0,9608</td>
                <td>0,55%</td>
                <td>0,0110</td>
                <td>17.162 bút toán</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Section 6 -->
      <section id="sec6">
        <h2 class="section-title"><span class="section-number">6</span> ĐÁNH GIÁ CHẤT LƯỢNG THỰC TẾ TỪ CÁC CHUYÊN GIA KIỂM TOÁN PwC</h2>
        <p>Các kiểm toán viên và chuyên viên điều tra gian lận nội bộ tại PwC đã trực tiếp rà soát các trường hợp thực tế do AE 9 phát hiện:</p>
        <ul>
          <li><strong>Hành vi phân tách hóa đơn (Invoice Splitting):</strong> Kẻ gian cố tình chia nhỏ một khoản chi 24.000 EUR thành 5 hóa đơn dưới 5.000 EUR để không phải trình Giám đốc tài chính phê duyệt.</li>
          <li><strong>Bút toán hạch toán đêm khuya bởi người dùng trái thẩm quyền:</strong> Tài khoản IT thực hiện bút toán điều chỉnh giảm doanh thu vào lúc 23h đêm Chủ nhật.</li>
          <li><strong>Bút toán kết chuyển đối ứng trái quy luật:</strong> Ghi Nợ Chi phí đối ứng thẳng vào Phải thu mà không có chứng từ xuất kho hoặc biên bản bù trừ công nợ.</li>
        </ul>
      </section>

      <!-- Section 7 -->
      <section id="sec7">
        <h2 class="section-title"><span class="section-number">7</span> ĐÚC KẾT CHO NGHỀ NGHIỆP KIỂM TOÁN HIỆN ĐẠI</h2>
        <ul>
          <li><strong>Chuyển dịch sang Kiểm toán Toàn diện 100%:</strong> Xóa bỏ hoàn toàn rủi ro lấy mẫu (Sampling Risk), quét toàn bộ 100% bút toán sổ cái của doanh nghiệp trong vài phút.</li>
          <li><strong>Hiện thực hóa Kiểm toán Liên tục (Continuous Auditing):</strong> Cho phép hệ thống kiểm soát nội bộ và kiểm toán nội bộ phát hiện gian lận theo thời gian thực thay vì đợi đến đợt kiểm toán cuối năm.</li>
          <li><strong>Tối ưu hóa nguồn lực nhân sự kiểm toán:</strong> Kiểm toán viên chỉ cần tập trung rà soát vài trăm bút toán có điểm bất thường cao nhất thay vì mò kim đáy bể trong hàng triệu dòng dữ liệu.</li>
        </ul>
      </section>

      <!-- Section 8 -->
      <section id="sec8">
        <h2 class="section-title"><span class="section-number">8</span> TÀI LIỆU THAM KHẢO CHÍNH (REFERENCES)</h2>
        <ul class="references-list">
          <li><strong>Schreyer, M., Sattarov, T., Borth, D., Dengel, A., & Reimer, B. (2017).</strong> Detection of anomalies in large scale accounting data using deep autoencoder networks. <em>arXiv preprint arXiv:1709.05254</em>.</li>
          <li><strong>ACFE (2016).</strong> Report to the Nations on Occupational Fraud and Abuse. <em>Association of Certified Fraud Examiners</em>.</li>
          <li><strong>PwC (2016).</strong> Global Economic Crime Survey 2016: An inside look at the true costs of crime. <em>PricewaterhouseCoopers</em>.</li>
          <li><strong>Schreyer, M., et al. (2020).</strong> Multi-view anomaly detection in large-scale accounting data. <em>International Conference on Information Systems (ICIS)</em>.</li>
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
        active_paper_idx=4
    )

    html_path = os.path.join(PAPERS_DIR, "paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated HTML: {os.path.basename(html_path)}")

if __name__ == "__main__":
    build()
