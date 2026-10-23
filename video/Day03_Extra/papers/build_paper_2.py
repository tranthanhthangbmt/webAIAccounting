# -*- coding: utf-8 -*-
"""
Builder for Paper 2:
Automated Invoice Data Extraction: Using LLM and OCR
(Khanchandani et al. - arXiv 2026 & Framework Hyperautomation LUT 2026)
"""

import os
from generate_day03_helpers import get_html_template, PAPERS_DIR

TITLE_VI = "Trích Xuất Dữ Liệu Hóa Đơn Tự Động Bằng Mô Hình Ngôn Ngữ Lớn (LLM) Và Nhận Dạng Quang Học (OCR)"
TITLE_EN = "Automated Invoice Data Extraction: Using LLM and OCR"
AUTHORS = "Khushi Khanchandani, Advait Thakur, Akshita Shetty, Chaitravi Reddy, Ritisa Behera (K.J. Somaiya School of Engineering, Mumbai)"
JOURNAL = "Kho lưu trữ mở Cornell University — arXiv:2511.05547 [cs.CV] (Cập nhật 2026) & LUT University Repository"
DOI = "https://arxiv.org/abs/2511.05547 — Open Access Research"
BADGE = "Paper 2 • Multimodal Document AI & LLM (2026)"

def build():
    # Markdown Content Header
    md_header = f"""# {TITLE_VI.upper()}
*({TITLE_EN})*

- **Tác giả:** {AUTHORS}
- **Nguồn xuất bản:** {JOURNAL}
- **Định danh học thuật:** {DOI}
- **Khung thực tiễn đi kèm:** Mô hình Siêu tự động hóa (Hyperautomation) 5 tầng của Harshith Bhaskar (2026, LUT University)
- **Slide bài giảng tương ứng:** Slide P3: AI Trong Kế Toán & Kiểm Toán (LLM + OCR)

---

"""
    md_body = r"""## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

Trong hệ sinh thái doanh nghiệp hiện đại, hóa đơn mua hàng (*Purchase Invoices*) đến từ hàng ngàn nhà cung cấp toàn cầu với muôn vàn định dạng phi cấu trúc. Các phương pháp bóc tách truyền thống dựa trên mẫu biểu (*Template-based*) hoặc biểu thức chính quy (*Regex*) thường xuyên sụp đổ mỗi khi nhà cung cấp thay đổi thiết kế hoặc khi hóa đơn có bố cục phức tạp nhiều trang. 

Nghiên cứu này giới thiệu bước đột phá của thế hệ **Trí tuệ Nhân tạo Đa phương thức (Multimodal Document AI)**: Kết hợp công nghệ Nhận dạng Ký tự Quang học (**OCR**) với sức mạnh suy luận ngữ nghĩa của **Mô hình Ngôn ngữ Lớn (Large Language Models - LLMs)** và mô hình đồ thị cấu trúc bố cục (*Graph-based layout reasoning*). 

Kiến trúc đề xuất vận hành theo quy trình khép kín:
1. **Thu nhận và Nhận dạng đa phương thức:** Sử dụng OCR tiên tiến kết hợp trích xuất hộp giới hạn tọa độ không gian 2 chiều $(x, y, w, h)$.
2. **Khung trích xuất ngữ nghĩa thích ứng bằng LLM:** Áp dụng kỹ thuật Prompt chuyên biệt tài chính (*Few-shot prompting & Schema-constrained JSON generation*), cho phép LLM không chỉ "nhìn chữ" mà còn "hiểu sâu sắc ngữ cảnh kế toán" để phân định chính xác các trường dễ nhầm lẫn (như phân biệt giữa *Địa chỉ giao hàng* và *Địa chỉ xuất hóa đơn*, giữa *Số tài khoản ngân hàng thụ hưởng* và *Mã số thuế*).
3. **Liên kết Siêu tự động hóa (Hyperautomation) trong Kế toán Phải trả (AP):** Kết hợp với công nghệ Tự động hóa bằng Robot (RPA) để tự động thực hiện **Đối chiếu 3 bên (3-Way Matching)** giữa Hóa đơn, Đơn đặt hàng (PO) và Phiếu nhập kho (GRN) trước khi đẩy bút toán vào hệ thống ERP (SAP/Oracle/MISA).

Kết quả thực nghiệm khẳng định hệ thống đạt **F1-score 95,4%** trong kịch bản tổng quát hóa không cần mẫu (*Zero-shot / Few-shot Generalization*) trên các hóa đơn chưa từng gặp trong tập huấn luyện. Đặc biệt, thời gian chu kỳ xử lý hóa đơn giảm từ **9,15 ngày xuống chỉ còn dưới 1 phút**, tiết kiệm hàng trăm ngàn USD chi phí vận hành cho doanh nghiệp.

**Từ khóa:** Trích xuất hóa đơn tự động; Mô hình Ngôn ngữ Lớn (LLM); OCR; Siêu tự động hóa (Hyperautomation); Kế toán Phải trả (Accounts Payable); Đối chiếu 3 bên (3-Way Matching); RPA; Intelligent Document Processing (IDP).

---

## 1. GIỚI THIỆU & TẠI SAO PHẢI KẾT HỢP OCR VỚI LLM?

### 1.1. Sự Bế Tắc Của OCR Đơn Thuần Trong Xử Lý Văn Bản Kế Toán
OCR truyền thống chỉ làm được một nhiệm vụ duy nhất: chuyển đổi điểm ảnh (*pixels*) thành chuỗi ký tự thô (*text string*). Nhưng trong thực tế phòng kế toán:
- **Ký tự thô không có ngữ nghĩa:** OCR có thể đọc được chuỗi `0101234567`, nhưng nó hoàn toàn không biết đây là *Mã số thuế người bán*, *Mã số thuế người mua*, hay *Số điện thoại liên hệ*.
- **Cấu trúc bảng biểu phức tạp:** Một dòng hàng hóa đơn có thể bị rớt dòng thành 2–3 hàng văn bản (ví dụ tên mặt hàng quá dài). OCR truyền thống sẽ đọc lẫn lộn số lượng của dòng trên với đơn giá của dòng dưới.
- **Tính phi mẫu biểu (*Unseen Layouts*):** Doanh nghiệp không thể viết sẵn 1.000 mẫu biểu cấu hình (templates) cho 1.000 nhà cung cấp khác nhau, vì chỉ cần một nhà cung cấp đổi cỡ chữ hoặc thêm một cột chiết khấu là toàn bộ quy trình tự động hóa cũ bị tê liệt.

### 1.2. Sức Mạnh Đột Phá Của Mô Hình Ngôn Ngữ Lớn (LLMs)
Sự xuất hiện của LLM (như GPT-4, Llama-3, Mistral) mang lại năng lực suy luận ngữ cảnh vượt trội:
- **Hiểu cấu trúc kế toán:** LLM hiểu bản chất các thuật ngữ kế toán quốc tế và Việt Nam (VAT, Subtotal, Invoice No, Billing Address, Shipping Address).
- **Tự động chuẩn hóa dữ liệu:** Tự động chuẩn hóa các định dạng ngày tháng đa dạng (`12/05/2026`, `May 12, 2026`, `2026-05-12`) về một chuẩn duy nhất `YYYY-MM-DD`.
- **Xuất dữ liệu cấu trúc ép kiểu (*Strict JSON Schema*):** LLM có thể nhận văn bản thô từ OCR và định dạng lại chính xác thành JSON tuân thủ schema kế toán mà không bị lỗi cú pháp.

---

## 2. KIẾN TRÚC HỆ THỐNG ĐỀ XUẤT (SYSTEM ARCHITECTURE)

Hệ thống được thiết kế thành một chuỗi xử lý 4 giai đoạn logic và hiệu quả:

![Hình 1: Kiến trúc tổng thể hệ thống bóc tách hóa đơn bằng LLM và OCR](figures_paper_2/fig_p4_1.jpeg)
*Hình 1: Sơ đồ kiến trúc luồng dữ liệu — tích hợp Ingestion, OCR & Geometry Analysis, LLM Semantic Extraction, và ERP Accounting Integration.*

---

### 2.1. Giai Đoạn 1: Tiền Xử Lý Đa Định Dạng & Nhận Dạng Quang Học (OCR & Spatial Layout)
Hệ thống tiếp nhận mọi định dạng hóa đơn (file PDF điện tử, ảnh quét, ảnh chụp camera di động):
1. **Phân tích hình học 2D (Spatial Layout Parsing):** Sử dụng mạng nhận dạng văn bản trích xuất không chỉ nội dung chữ mà còn lưu trữ tọa độ không gian chính xác $(x_1, y_1, x_2, y_2)$ của từng từ và từng dòng.
2. **Khôi phục cấu trúc đọc tự nhiên (Reading Order Restoration):** Sắp xếp lại thứ tự các khối chữ theo quy tắc từ trên xuống dưới, từ trái sang phải, đảm bảo văn bản đưa vào LLM không bị đảo lộn dòng biểu.

![Hình 2: Phân tích hộp giới hạn và cấu trúc không gian của hóa đơn](figures_paper_2/fig_p5_1.jpeg)
*Hình 2: Trực quan hóa các hộp giới hạn (Bounding Boxes) phân chia các khối thông tin tiêu đề, thông tin đối tác và bảng kê hàng hóa.*

---

### 2.2. Giai Đoạn 2: Trích Xuất Ngữ Nghĩa Bằng Mô Hình Ngôn Ngữ Lớn (LLM Semantic Extraction)

Văn bản thô kèm thông tin vị trí được đưa vào mô hình ngôn ngữ thông qua kỹ thuật **Prompt Engineering chuyên biệt tài chính**:

```json
{
  "role": "system",
  "content": "Bạn là chuyên gia kế toán AI có nhiệm vụ trích xuất dữ liệu hóa đơn. Hãy phân tích văn bản OCR được cung cấp và trích xuất thành định dạng JSON hợp lệ theo Schema sau: {invoice_number, invoice_date, seller_name, seller_tax_id, buyer_name, buyer_tax_id, items: [{description, quantity, unit_price, line_total}], subtotal, vat_rate, vat_amount, total_amount}. Tuyệt đối không suy diễn, nếu không có hãy để giá trị null."
}
```

![Hình 3: Kết quả phân tích ngữ nghĩa và trích xuất bảng biểu](figures_paper_2/fig_p5_2.jpeg)
*Hình 3: Khả năng bóc tách chính xác từng dòng mặt hàng (Line Items) trong bảng chi tiết hóa đơn phức tạp.*

Nhờ cơ chế chú ý (*Self-Attention*), LLM dễ dàng liên kết từ khóa "Tổng cộng tiền thanh toán" ở cuối trang với con số nằm cách xa nó ở góc phải dưới cùng, vượt qua hoàn toàn rào cản chia cột của OCR truyền thống.

---

### 2.3. Giai Đoạn 3: Khung Siêu Tự Động Hóa 5 Tầng Trong Kế Toán Phải Trả (AP)
Theo nghiên cứu của Harshith Bhaskar (2026, LUT University) được tích hợp trong mô hình:

```
[Tầng 1: Thu thập Hóa đơn] -> Email Bot tự động tải hóa đơn từ hòm thư kế toán
         ↓
[Tầng 2: Thị giác máy tính IDP] -> OCR + Bóc tách cấu trúc bố cục
         ↓
[Tầng 3: LLM Trích xuất Ngữ nghĩa] -> Xuất dữ liệu JSON chuẩn hóa
         ↓
[Tầng 4: Quy tắc Nghiệp vụ & Đối chiếu 3 bên (3-Way Matching)]
         Đối chiếu: Hóa đơn == Đơn đặt hàng (PO) == Phiếu nhập kho (GRN)
         ↓
         ├── Khớp 100% ────> RPA tự động tạo Bút toán ghi sổ vào ERP (SAP/MISA)
         └── Lệch giá/số lượng ──> Chuyển Hàng đợi Phê duyệt (Human-in-the-Loop)
```

---

## 3. KẾT QUẢ THỰC NGHIỆM & SO SÁNH HIỆU NĂNG

### 3.1. So Sánh Hiệu Quả Trích Xuất Ngữ Nghĩa

So sánh giữa các thế hệ công nghệ xử lý hóa đơn:

| Công Nghệ Xử Lý | F1-Score Trên Hóa Đơn Chuẩn | F1-Score Trên Hóa Đơn Không Theo Mẫu (Unseen Layouts) | Khả Năng Xử Lý Đa Ngôn Ngữ |
| :--- | :---: | :---: | :---: |
| **OCR Cổ điển + Template Matching** | 82,4% | 38,1% *(Gần như hỏng hoàn toàn)* | Kém |
| **OCR + Rule-based / Regex** | 86,7% | 52,3% | Trung bình |
| **Deep Learning Vision (LayoutLMv3)** | 93,1% | 84,6% | Khá |
| **Phương Pháp Đề Xuất (LLM + OCR)** | **97,8%** | **95,4%** | **Xuất sắc (Tự thích nghi)** |

> [!TIP]
> **Điểm mấu chốt:** Với các hóa đơn hoàn toàn mới (*Unseen Layouts*), mô hình kết hợp LLM + OCR vẫn duy trì F1-score lên tới **95,4%**, chứng minh năng lực khái quát hóa phi thường của mô hình ngôn ngữ lớn trong việc hiểu ngôn ngữ tài chính.

---

### 3.2. Tác Động Rút Ngắn Thời Gian & Chi Phí Vận Hành Thực Tế

Theo số liệu đo lường thực tế tại doanh nghiệp ứng dụng khung Siêu tự động hóa (Bhaskar 2026):

| Tiêu Chí Đo Lường | Quy Trình Thủ Công Cũ | Ứng Dụng Siêu Tự Động Hóa (LLM + OCR + RPA) | Mức Độ Tối Ưu Hóa |
| :--- | :---: | :---: | :---: |
| **Thời gian chu kỳ xử lý hóa đơn** | **9,15 ngày** | **Dưới 1 phút** | Giảm **> 99%** |
| **Chi phí xử lý trung bình mỗi hóa đơn** | **12,50 USD** | **1,80 USD** | Tiết kiệm **85,6%** |
| **Tỷ lệ tự động hóa xuyên suốt (STP Rate)** | 0% | **82,5%** *(Tự động đẩy vào ERP không cần người chạm tay)* | Đột phá |
| **Tỷ lệ hóa đơn hưởng chiết khấu thanh toán sớm** | 35% | **96%** | Tăng mạnh thanh khoản |

---

## 4. BÀI HỌC NGHIỆP VỤ & KIỂM SOÁT ẢO GIÁC AI (HALLUCINATION RISK)

### 4.1. Nguy Cơ Ảo Giác Của LLM Trong Kế Toán
Một trong những lo ngại lớn nhất của Kiểm toán viên khi dùng LLM là hiện tượng **Ảo giác (Hallucination)** — mô hình tự "bịa" ra một con số hoặc ngày tháng không hề có trên hóa đơn.

### 4.2. Giải Pháp Kiểm Soát Kỹ Thuật (Mitigation Strategy)
1. **Ép Buộc Nhiệt Độ Bằng 0 (Temperature = 0.0):** Triệt tiêu tính sáng tạo của LLM, bắt buộc mô hình chỉ trích xuất dữ liệu có căn cứ.
2. **Khóa Ánh Xạ Chuỗi Ký Tự Gốc (Substring Verification):** Mọi giá trị số mà LLM trả về trong file JSON đều phải vượt qua bài kiểm tra: con số đó có tồn tại nguyên vẹn trong chuỗi văn bản do OCR đọc được hay không. Nếu không tìm thấy, hệ thống lập tức từ chối và cảnh báo nghi ngờ ảo giác.
3. **Bộ Lọc Đẳng Thức Nghiệp Vụ:** Tự động đối chiếu số học giữa đơn giá $\times$ số lượng = thành tiền trên từng dòng chi tiết.

---

## CÂU HỎI THẢO LUẬN CHO SINH VIÊN KẾ TOÁN

1. **Câu hỏi thảo luận 1:** *"Trong quy trình Đối chiếu 3 bên (3-Way Matching), nếu số lượng hàng trên Hóa đơn là 100 sản phẩm nhưng Phiếu nhập kho (GRN) chỉ ghi nhận 95 sản phẩm (5 sản phẩm bị vỡ hỏng trong quá trình vận chuyển), hệ thống AI-RPA nên xử lý thế nào? Kế toán viên cần can thiệp ở bước nào để thanh toán đúng công nợ thực tế?"*
2. **Câu hỏi thảo luận 2:** *"Tại sao việc giảm chu kỳ xử lý hóa đơn từ 9 ngày xuống 1 phút lại giúp Giám đốc Tài chính (CFO) đàm phán được mức chiết khấu thanh toán tốt hơn từ nhà cung cấp?"*

---
"""
    md_content = md_header + md_body

    # HTML Body Generation
    sidebar_links = """
      <a href="#abstract" class="sidebar-link active">Tóm tắt nghiên cứu</a>
      <a href="#sec1" class="sidebar-link">1. Giới thiệu & Tại sao cần LLM</a>
      <a href="#sec2" class="sidebar-link">2. Kiến trúc giải pháp LLM + OCR</a>
      <a href="#sec2-1" class="sidebar-link sub-link">2.1 Phân tích bố cục không gian</a>
      <a href="#sec2-2" class="sidebar-link sub-link">2.2 Trích xuất ngữ nghĩa bằng LLM</a>
      <a href="#sec2-3" class="sidebar-link sub-link">2.3 Khung Siêu tự động hóa 5 tầng</a>
      <a href="#sec3" class="sidebar-link">3. Kết quả thực nghiệm</a>
      <a href="#sec4" class="sidebar-link">4. Kiểm soát ảo giác AI (Hallucination)</a>
      <a href="#discussion" class="sidebar-link">Câu hỏi thảo luận trên lớp</a>
    """

    content_html = r"""
      <!-- Abstract Box -->
      <section id="abstract" class="abstract-box">
        <div class="abstract-heading">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
          </svg>
          Tóm Tắt Nghiên Cứu (Abstract)
        </div>
        <p class="abstract-text">
          Trong hệ sinh thái doanh nghiệp hiện đại, hóa đơn mua hàng (<em>Purchase Invoices</em>) đến từ hàng ngàn nhà cung cấp toàn cầu với muôn vàn định dạng phi cấu trúc. Các phương pháp bóc tách truyền thống dựa trên mẫu biểu (<em>Template-based</em>) hoặc biểu thức chính quy (<em>Regex</em>) thường xuyên sụp đổ mỗi khi nhà cung cấp thay đổi thiết kế hoặc khi hóa đơn có bố cục phức tạp nhiều trang.
        </p>
        <p class="abstract-text" style="margin-top: 1rem;">
          Nghiên cứu này giới thiệu bước đột phá của thế hệ <strong>Trí tuệ Nhân tạo Đa phương thức (Multimodal Document AI)</strong>: Kết hợp công nghệ Nhận dạng Ký tự Quang học (<strong>OCR</strong>) với sức mạnh suy luận ngữ nghĩa của <strong>Mô hình Ngôn ngữ Lớn (Large Language Models - LLMs)</strong> và mô hình phân tích cấu trúc hình học. Hệ thống áp dụng kỹ thuật Prompt Engineering tài chính có kiểm soát (Schema-constrained output), cho phép trích xuất chính xác các bảng kê chi tiết mặt hàng và tự động đối chiếu hóa đơn với Đơn đặt hàng (PO) và Phiếu nhập kho (GRN).
        </p>
        <p class="abstract-text" style="margin-top: 1rem;">
          Kết quả thực nghiệm khẳng định hệ thống đạt <strong>F1-score 95,4%</strong> trong kịch bản tổng quát hóa không cần mẫu (Zero-shot) trên các hóa đơn hoàn toàn mới. Ứng dụng thực tiễn trong Siêu tự động hóa (Hyperautomation) giúp rút ngắn chu kỳ xử lý hóa đơn từ <strong>9,15 ngày xuống dưới 1 phút</strong>, tiết kiệm hơn 85% chi phí xử lý kế toán công nợ.
        </p>
        <div class="keywords-box">
          <strong>Từ khóa:</strong> Trích xuất hóa đơn tự động; Mô hình Ngôn ngữ Lớn (LLM); OCR; Siêu tự động hóa (Hyperautomation); Kế toán Phải trả (Accounts Payable); Đối chiếu 3 bên (3-Way Matching); RPA; Intelligent Document Processing (IDP).
        </div>
      </section>

      <!-- Section 1 -->
      <section id="sec1">
        <h2 class="section-title">
          <span class="section-number">1</span>
          Giới Thiệu & Tại Sao Phải Kết Hợp OCR Với LLM?
        </h2>
        <p>
          Trong kỷ nguyên số, dữ liệu kế toán không chỉ nằm trong các bảng tính Excel ngăn nắp mà phân tán trong hàng triệu tài liệu bán cấu trúc và phi cấu trúc. Nhận dạng ký tự quang học (OCR) thông thường chỉ thực hiện việc "đọc chữ", nhưng không có năng lực "hiểu ngữ nghĩa":
        </p>
        <ul>
          <li><strong>Không phân biệt được vai trò thực thể:</strong> Khi đọc được chuỗi ký tự "Công ty TNHH ABC", OCR không thể tự biết đây là đơn vị bán hàng, đơn vị mua hàng hay đơn vị vận chuyển trung gian nếu không có con người cấu hình sẵn tọa độ.</li>
          <li><strong>Thất bại trước sự biến động mẫu biểu:</strong> Khi đối tác thay đổi vị trí ô thuế suất hoặc in hóa đơn theo khổ ngang thay vì khổ dọc, các kịch bản tự động hóa cũ hoàn toàn tê liệt.</li>
        </ul>

        <div class="callout callout-info">
          <div class="callout-title" style="color: #2563eb;">
            💡 Bước Chuyển Đổi Sang Multimodal Document AI
          </div>
          <p style="margin-bottom: 0;">
            Bằng cách tích hợp Mô hình Ngôn ngữ Lớn (LLM) vào chuỗi xử lý sau bước OCR, hệ thống sở hữu "bộ não" có khả năng đọc hiểu ngữ cảnh tài chính, tự động suy luận quan hệ giữa các trường thông tin và xuất ra định dạng JSON cấu trúc chuẩn mực mà không phụ thuộc vào bất kỳ mẫu biểu cố định nào.
          </p>
        </div>
      </section>

      <!-- Section 2 -->
      <section id="sec2">
        <h2 class="section-title">
          <span class="section-number">2</span>
          Kiến Trúc Hệ Thống Đề Xuất (System Architecture)
        </h2>
        <p>
          Quy trình bóc tách thông minh kết hợp LLM và OCR được tổ chức theo kiến trúc phân tầng hiện đại:
        </p>

        <div class="figure-wrapper">
          <div class="figure-img-container">
            <img src="figures_paper_2/fig_p4_1.jpeg" alt="Kiến trúc tổng thể hệ thống bóc tách hóa đơn LLM + OCR" />
          </div>
          <div class="figure-caption">
            <strong>Hình 1:</strong> Sơ đồ kiến trúc tổng thể — từ tiếp nhận tài liệu đa định dạng, phân tích tọa độ không gian 2D, suy luận ngữ nghĩa bằng LLM đến đẩy dữ liệu vào ERP.
          </div>
        </div>

        <h3 id="sec2-1" class="sub-section-title">2.1. Phân Tích Bố Cục Không Gian 2D (Spatial Layout Parsing)</h3>
        <p>
          Để cung cấp ngữ cảnh đầy đủ cho LLM, hệ thống trích xuất đồng thời cả nội dung văn bản và tọa độ hộp giới hạn (Bounding Boxes) của từng từ:
        </p>

        <div class="figure-wrapper">
          <div class="figure-img-container">
            <img src="figures_paper_2/fig_p5_1.jpeg" alt="Hộp giới hạn tọa độ không gian hóa đơn" />
          </div>
          <div class="figure-caption">
            <strong>Hình 2:</strong> Trực quan hóa các hộp giới hạn (Bounding Boxes) xác định vị trí tương đối giữa các trường thông tin trên hóa đơn.
          </div>
        </div>

        <h3 id="sec2-2" class="sub-section-title">2.2. Trích Xuất Ngữ Nghĩa Bằng LLM Chuyên Biệt Tài Chính</h3>
        <p>
          Hệ thống xây dựng các mẫu Prompt chuyên gia yêu cầu mô hình đóng vai trò Kiểm toán viên tài chính AI, bóc tách toàn diện các bảng kê hàng hóa phức tạp:
        </p>

        <div class="figure-wrapper">
          <div class="figure-img-container">
            <img src="figures_paper_2/fig_p5_2.jpeg" alt="Bóc tách chi tiết từng dòng mặt hàng" />
          </div>
          <div class="figure-caption">
            <strong>Hình 3:</strong> Khả năng bóc tách chính xác từng dòng mặt hàng (Line Items) trong bảng kê nhiều sản phẩm và tự động chuẩn hóa định dạng số tiền.
          </div>
        </div>

        <h3 id="sec2-3" class="sub-section-title">2.3. Khung Siêu Tự Động Hóa 5 Tầng Trong Kế Toán Phải Trả</h3>
        <p>
          Nghiên cứu kết hợp với mô hình thực tiễn của Harshith Bhaskar (2026, LUT University) để tạo nên chuỗi Siêu tự động hóa (Hyperautomation) khép kín:
        </p>
        <div class="callout callout-success">
          <div class="callout-title" style="color: #059669;">
            🤖 Quy Trình Đối Chiếu 3 Bên Tự Động (Automated 3-Way Matching)
          </div>
          <p style="margin-bottom: 0;">
            Sau khi LLM bóc tách xong hóa đơn thành JSON, Robot phần mềm (RPA) tự động truy vấn Đơn đặt hàng (Purchase Order - PO) và Phiếu nhập kho (Goods Receipt Note - GRN) trên hệ thống ERP để đối chiếu chéo: Số lượng mua == Số lượng nhập kho == Số lượng tính tiền trên hóa đơn; Đơn giá thỏa thuận == Đơn giá trên hóa đơn. Nếu khớp 100%, hệ thống tự động ghi nhận bút toán Nợ 156, 133 / Có 331 và lên lịch thanh toán mà không cần con người phê duyệt thủ công.
          </p>
        </div>
      </section>

      <!-- Section 3 -->
      <section id="sec3">
        <h2 class="section-title">
          <span class="section-number">3</span>
          Kết Quả Thực Nghiệm & So Sánh Hiệu Năng
        </h2>

        <h3 class="sub-section-title">3.1. Độ Chính Xác Trích Xuất Trên Hóa Đơn Không Theo Mẫu</h3>
        <div class="table-container">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Phương Pháp Công Nghệ</th>
                <th>F1-Score Mẫu Đã Biết</th>
                <th>F1-Score Mẫu Mới (Unseen Layouts)</th>
                <th>Khả Năng Thích Ứng</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>OCR Truyền thống + Template Cố định</td>
                <td>82,4%</td>
                <td>38,1%</td>
                <td>Kém (Hỏng khi đổi mẫu)</td>
              </tr>
              <tr>
                <td>OCR + Biểu thức chính quy (Regex)</td>
                <td>86,7%</td>
                <td>52,3%</td>
                <td>Trung bình</td>
              </tr>
              <tr>
                <td>Học sâu Thị giác (LayoutLMv3)</td>
                <td>93,1%</td>
                <td>84,6%</td>
                <td>Khá</td>
              </tr>
              <tr style="background: rgba(37, 99, 235, 0.08); font-weight: 700;">
                <td>Mô hình đề xuất (LLM + OCR)</td>
                <td><strong>97,8%</strong></td>
                <td><strong>95,4%</strong></td>
                <td><strong>Xuất sắc (Zero-shot)</strong></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3 class="sub-section-title">3.2. Hiệu Quả Tối Ưu Hóa Chi Phí & Chu Kỳ Thanh Toán</h3>
        <div class="table-container">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Chỉ Số Hiệu Năng Kế Toán</th>
                <th>Quy Trình Thủ Công</th>
                <th>Hệ Thống Siêu Tự Động Hóa</th>
                <th>Mức Độ Cải Thiện</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Thời gian xử lý chu kỳ hóa đơn</td>
                <td><strong>9,15 ngày</strong></td>
                <td><strong>&lt; 1 phút</strong></td>
                <td><span style="color: #10b981; font-weight: 700;">Nhanh hơn 99%</span></td>
              </tr>
              <tr>
                <td>Chi phí xử lý trung bình / hóa đơn</td>
                <td><strong>12,50 USD</strong></td>
                <td><strong>1,80 USD</strong></td>
                <td><span style="color: #10b981; font-weight: 700;">Tiết kiệm 85,6%</span></td>
              </tr>
              <tr>
                <td>Tỷ lệ xử lý thẳng tự động (STP Rate)</td>
                <td>0%</td>
                <td><strong>82,5%</strong></td>
                <td>Tự động hóa hoàn toàn</td>
              </tr>
              <tr>
                <td>Tỷ lệ nhận chiết khấu thanh toán sớm</td>
                <td>35%</td>
                <td><strong>96%</strong></td>
                <td>Tối ưu dòng tiền</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Section 4 -->
      <section id="sec4">
        <h2 class="section-title">
          <span class="section-number">4</span>
          Kiểm Soát Ảo Giác AI (Hallucination Risk)
        </h2>
        <p>
          Trong kiểm toán và kế toán, sai sót một con số có thể dẫn đến hậu quả pháp lý nghiêm trọng. Nhóm nghiên cứu đề xuất giải pháp 3 lớp chống ảo giác cho LLM:
        </p>
        <ol>
          <li><strong>Thiết lập Temperature = 0.0:</strong> Buộc mô hình triệt tiêu tính ngẫu nhiên, chỉ xuất ra các sự kiện thực tế có căn cứ.</li>
          <li><strong>Xác thực chuỗi con đối chiếu (Substring Verification):</strong> Mọi số tiền hay mã số thuế do LLM trích xuất bắt buộc phải tìm thấy chính xác trong chuỗi văn bản OCR thô ban đầu; nếu không tìm thấy, hệ thống lập tức từ chối và cảnh báo.</li>
          <li><strong>Kiểm tra chéo đẳng thức kế toán:</strong> Tự động tính lại đơn giá $\times$ số lượng để đối chiếu với thành tiền trên từng dòng.</li>
        </ol>
      </section>

      <!-- Discussion Questions -->
      <section id="discussion" style="margin-top: 3.5rem;">
        <div class="callout callout-success">
          <div class="callout-title" style="font-size: 1.1rem; color: #059669;">
            💬 CÂU HỎI THẢO LUẬN & TRANH BIỆN TRÊN LỚP (SEMINAR)
          </div>
          <ol style="margin-top: 0.75rem; margin-bottom: 0.5rem;">
            <li><strong>Câu hỏi 1 (Về kiểm soát nội bộ & 3-Way Matching):</strong> Khi hệ thống AI-RPA phát hiện hóa đơn có số tiền chênh lệch 50.000 VNĐ so với Đơn đặt hàng (PO) do phát sinh thêm phí bốc xếp ngoài hợp đồng, quy trình kiểm soát nội bộ của doanh nghiệp nên thiết kế như thế nào để vừa không làm nghẽn thanh toán vừa đảm bảo tính liêm chính của chi phí?</li>
            <li><strong>Câu hỏi 2 (Về hiệu quả dòng tiền):</strong> Tại sao việc rút ngắn thời gian xử lý hóa đơn từ 9 ngày xuống 1 phút lại giúp Giám đốc Tài chính (CFO) đàm phán được mức chiết khấu thanh toán tốt hơn từ nhà cung cấp? Hãy phân tích dưới góc độ chi phí cơ hội của vốn.</li>
          </ol>
        </div>
      </section>
    """

    # Generate HTML file
    html_out = get_html_template(
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

    html_file_path = os.path.join(PAPERS_DIR, "paper_2_Automated_Invoice_LLM_OCR_tiengviet.html")
    with open(html_file_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"Generated Paper 2 HTML: {html_file_path}")

    # Generate Markdown file
    md_file_path = os.path.join(PAPERS_DIR, "paper_2_Automated_Invoice_LLM_OCR_tiengviet.md")
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Paper 2 Markdown: {md_file_path}")

if __name__ == "__main__":
    build()
