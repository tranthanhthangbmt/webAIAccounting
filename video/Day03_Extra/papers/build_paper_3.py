# -*- coding: utf-8 -*-
"""
Builder for Paper 3:
Fake Invoices and Receipts in Accounting: Impacts and Mitigation in the Age of Gen-AI
(Thornton, Aljuaid, Chapman, Bhowmik - BMVC 2025 / Newcastle University & Sage PLC)
"""

import os
from generate_day03_helpers import get_html_template, PAPERS_DIR

TITLE_VI = "Hóa Đơn Và Biên Lai Giả Mạo Trong Kế Toán: Tác Động Nghiệp Vụ Và Giải Pháp Khắc Phục Bằng Thị Giác Máy Tính Trong Kỷ Nguyên AI Tạo Sinh (Gen-AI)"
TITLE_EN = "Fake Invoices and Receipts in Accounting: Impacts and Mitigation in the Age of gen-AI"
AUTHORS = "Philip Thornton, Lamyaa Aljuaid, Matthew W Chapman, Deepayan Bhowmik (Newcastle University & Sage PLC, UK)"
JOURNAL = "British Machine Vision Conference (BMVC 2025 Workshops - MAAAI / SRBS) & Newcastle University Repository"
DOI = "https://doi.org/10.57711/kgxg-9653 — BMVA Open Access"
BADGE = "Paper 3 • BMVC Landmark & Image Forensics (2025/2026)"

def build():
    # Markdown Content Header
    md_header = f"""# {TITLE_VI.upper()}
*({TITLE_EN})*

- **Tác giả:** {AUTHORS}
- **Đơn vị nghiên cứu:** Khoa Máy tính & Kỹ thuật — Đại học Newcastle và Tập đoàn Phần mềm Kế toán Sage PLC (Vương quốc Anh)
- **Hội thảo & Nguồn:** {JOURNAL}
- **Định danh học thuật:** {DOI}
- **Slide bài giảng tương ứng:** Slide P4: AI in Accounting & Auditing (Fake Invoices Gen-AI)

---

"""
    md_body = r"""## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

Sự bùng nổ vũ bão của Trí tuệ Nhân tạo Tạo sinh (**Generative AI - Gen-AI**), bao gồm các mô hình khuếch tán hình ảnh (*Diffusion Models*), Mạng đối nghịch tạo sinh (*GANs*) và các công cụ chỉnh sửa ảnh thông minh, đang tạo ra một mối đe dọa mang tính sinh tử đối với tính toàn vẹn của hệ thống kế toán và kiểm toán toàn cầu. Kẻ gian, nhân viên nội bộ bất lương hoặc các đường dây tội phạm có tổ chức giờ đây có thể tạo ra những hóa đơn, biên lai thanh toán giả mạo hoàn hảo — từ hóa đơn mua sắm tiếp khách, vé máy bay điện tử đến hóa đơn mua nguyên vật liệu trị giá hàng tỷ đồng — với độ chân thực về vết nhàu, bóng sáng, phông chữ và logo đến mức **mắt thường của kiểm toán viên con người hoàn toàn không thể nhận biết**.

Công trình nghiên cứu tiên phong này của Đại học Newcastle phối hợp với tập đoàn phần mềm kế toán quốc tế **Sage PLC**:
1. **Phân tích toàn diện tác động kinh tế và pháp lý:** Đánh giá các hình thức gian lận thanh toán khống chi phí công tác (*Expense Reimbursement Fraud*), gian lận hóa đơn bất hợp pháp để trốn thuế thu nhập doanh nghiệp, và gian lận quay vòng hoàn thuế GTGT (*VAT Carousel Fraud*).
2. **Giải phẫu cơ chế tạo giả của Gen-AI:** Làm rõ cách thức tội phạm sử dụng kỹ thuật cấy ghép ảnh (*Splicing*), xóa sửa số tiền (*Inpainting*), và sinh ảnh tổng hợp hoàn toàn (*Synthetic Generation*) để vượt qua các chốt kiểm soát nội bộ truyền thống.
3. **Đề xuất khung giải pháp Pháp y Hình ảnh số (Digital Image Forensics) dựa trên Thị giác Máy tính:**
   - **Phân tích mức độ lỗi nén (Error Level Analysis - ELA):** Phát hiện sự không đồng nhất trong tỷ lệ nén JPEG tại các vùng con số bị chỉnh sửa.
   - **Phân tích miền tần số (Frequency Domain & Wavelet Analysis):** Nhận diện các dấu vết can thiệp vi mô ở tần số cao mà mắt người không nhìn thấy.
   - **Kiểm định siêu dữ liệu (Metadata / EXIF Forensics):** Bóc tách lịch sử phần mềm chỉnh sửa và thiết bị tạo ảnh.
   - **Mạng Học sâu chuyên biệt (Deep Forgery Detection CNNs):** Huấn luyện mô hình nhận diện các dấu vết nhân tạo do AI tạo sinh để lại trên từng điểm ảnh (*pixel artifacts*).

Nghiên cứu cung cấp một lộ trình thực chiến để các nhà phát triển phần mềm kế toán (như Sage, SAP, MISA) và các hãng kiểm toán Big 4 tích hợp bộ lọc "Kính hiển vi số" vào quy trình kiểm soát nội bộ, bảo vệ doanh nghiệp trước làn sóng gian lận tài chính tinh vi thời đại AI.

**Từ khóa:** Hóa đơn giả mạo; Biên lai giả; AI tạo sinh (Gen-AI); Pháp y hình ảnh số (Image Forensics); Error Level Analysis (ELA); Kiểm toán gian lận; Kiểm soát nội bộ; Thị giác máy tính.

---

## 1. BỐI CẢNH: KHI MẮT THƯỜNG KIỂM TOÁN VIÊN BỊ "VÔ HIỆU HÓA"

Trong hơn một thế kỷ qua, nguyên tắc cơ bản của kiểm toán là **kiểm tra chứng từ gốc (Vouching)**: Kiểm toán viên xem xét hóa đơn, biên lai giấy hoặc bản chụp quét để đối chiếu với sổ sách kế toán. Nếu chứng từ có đầy đủ con dấu, chữ ký, ngày tháng hợp lý và hóa đơn nhìn "thật", giao dịch sẽ được chấp thuận.

Tuy nhiên, sự xuất hiện của AI tạo sinh đã làm sụp đổ hoàn toàn giả định này:
- **Thời kỳ tiền AI (Pre-AI):** Kẻ gian phải dùng kéo cắt dán số tiền, dùng bút xóa rồi photocopy lại. Những hóa đơn giả mạo này thường để lại dấu vết lem mực, phông chữ lệch hàng, hoặc đường viền cắt dán thô thiển mà một kế toán viên kinh nghiệm có thể phát hiện bằng mắt thường.
- **Thời kỳ Photoshop:** Kẻ gian dùng phần mềm chỉnh sửa ảnh để đổi con số. Mặc dù khó phát hiện hơn, nhưng nếu phóng to ảnh, kiểm toán viên vẫn có thể thấy pixel bị vỡ hoặc phông chữ bị méo.
- **Thời kỳ Gen-AI hiện nay (2025–2026):** Chỉ cần một câu lệnh prompt ngắn (ví dụ: *"Tạo một biên lai ăn tối nhà hàng 5 sao tại Hà Nội trị giá 15.800.000 VNĐ ngày 20/10/2025, có vết gấp giấy nhẹ và bóng đèn vàng"*), các mô hình AI tạo ra một bức ảnh hóa đơn hoàn hảo 100%. Phông chữ khớp hoàn toàn với ánh sáng môi trường, có độ nghiêng tự nhiên và vết bẩn giả như thật.

---

## 2. PHÂN TÍCH TÁC ĐỘNG NGHIỆP VỤ KẾ TOÁN & THUẾ (IMPACT ANALYSIS)

Bài báo phân loại 3 cấp độ thiệt hại nghiêm trọng của hóa đơn giả trong doanh nghiệp:

### 2.1. Cấp Độ Doanh Nghiệp: Gian Lận Chi Phí Thanh Toán Công Tác (T&E Expense Fraud)
Theo thống kê của Hiệp hội các Nhà Kiểm toán Gian lận Quốc tế (ACFE), gian lận chi phí chiếm tới **15% tổng số các vụ gian lận nội bộ doanh nghiệp**, với thời gian trung bình để phát hiện lên tới **18 tháng**. 
- Nhân viên công tác đi taxi hết 200.000 VNĐ nhưng dùng AI sửa ảnh biên lai thành 1.200.000 VNĐ để thanh toán khống.
- Tạo giả vé máy bay, hóa đơn khách sạn 5 sao dù thực tế ở nhà người quen.
- Doanh nghiệp mất mát hàng tỷ đồng quỹ tiền mặt mỗi năm mà không hề hay biết.

### 2.2. Cấp Độ Cơ Quan Thuế: Gian Lận Thuế TNDN & Hoàn Thuế GTGT
- Mua bán hóa đơn đầu vào giả để nâng khống giá vốn hàng bán (COGS), làm giảm lợi nhuận trước thuế nhằm trốn thuế TNDN.
- Gian lận hoàn thuế GTGT quay vòng (*VAT Carousel Fraud*): Sử dụng hóa đơn do AI tạo ra để hợp thức hóa hàng hóa ảo xuất khẩu, chiếm đoạt tiền hoàn thuế từ ngân sách nhà nước.

### 2.3. Cấp Độ Hãng Kiểm Toán Độc Lập: Rủi Ro Pháp Lý Khôn Lường
Nếu kiểm toán viên ký báo cáo kiểm toán chấp nhận toàn phần nhưng sau đó cơ quan công an phát hiện doanh nghiệp sử dụng hàng trăm tỷ hóa đơn đầu vào giả mạo:
- Hãng kiểm toán đối mặt với nguy cơ bị đình chỉ hoạt động, kiện tụng đòi bồi thường thiệt hại hàng triệu USD và đánh mất uy tín thương hiệu vĩnh viễn.

---

## 3. KHUNG GIẢI PHÁP THỊ GIÁC MÁY TÍNH & PHÁP Y HÌNH ẢNH (MITIGATION STRATEGIES)

Để chống lại AI tạo sinh, giải pháp duy nhất là **sử dụng chính Trí tuệ Nhân tạo và Thị giác máy tính như một chiếc "Kính hiển vi pháp y"**:

![Hình 1: Phân tích pháp y hình ảnh phát hiện vùng chỉnh sửa trên biên lai](figures_paper_3/fig_p7_1.jpeg)
*Hình 1: Trực quan hóa kết quả phân tích mức độ lỗi nén (ELA) và miền tần số trên hóa đơn bị chỉnh sửa số tiền.*

---

### 3.1. Kỹ Thuật 1: Phân Tích Mức Độ Sai Số Nén (Error Level Analysis - ELA)
Khi một bức ảnh được lưu dưới định dạng JPEG, toàn bộ ảnh được nén với một tỷ lệ suy hao (*lossy compression*) đồng nhất.
- Khi kẻ gian mở ảnh ra bằng Photoshop hoặc AI, chỉnh sửa con số `5` thành số `8`, rồi lưu lại: **Vùng con số mới được nén ít lần hơn so với phần còn lại của bức ảnh**.
- Thuật toán ELA cố tình nén lại bức ảnh ở chất lượng 95% và tính toán ma trận sai số pixel giữa hai phiên bản:
```
\Delta I(x, y) = |I_{original}(x, y) - I_{recompressed}(x, y)| \times S
```
(Trong đó $S$ là hệ số khuếch đại hiển thị, thường chọn $S = 20$).
- Kết quả: Vùng văn bản nguyên bản hiển thị màu xám tối đồng nhất, trong khi **con số bị sửa đổi sẽ phát sáng rực rỡ** trên màn hình phân tích ELA, vạch trần hành vi gian lận ngay lập tức!

---

### 3.2. Kỹ Thuật 2: Phân Tích Miền Tần Số Cao & Biến Đổi Wavelet

![Hình 2: Phân tích phổ tần số và dấu vết nhiễu vi mô của AI tạo sinh](figures_paper_3/fig_p8_1.jpeg)
*Hình 2: Dấu vết bất thường trong phổ tần số Fourier và nhiễu vi mô (PRNU) giữa hóa đơn do máy ảnh chụp thật và hóa đơn do AI tạo sinh.*

- Ảnh chụp từ máy ảnh/điện thoại thật luôn chứa mẫu nhiễu cảm biến quang học đặc thù (**PRNU - Photo-Response Non-Uniformity**), phân bố đều khắp bức ảnh như một "dấu vân tay phần cứng".
- Các hóa đơn do mô hình khuếch tán (Diffusion Models) tạo ra hoàn toàn không có nhiễu cảm biến thực này, hoặc có sự gián đoạn tần số cao tại đường biên chữ. Thuật toán biến đổi Wavelet 2D bóc tách các dải tần số cao $(HH, LH, HL)$ để phát hiện sự mất cân đối năng lượng điểm ảnh.

---

### 3.3. Kỹ Thuật 3: Mạng Học Sâu Phát Hiện Giả Mạo (Deep Learning Forgery Classifier)

![Hình 3: Khung phát hiện gian lận đa phương thức và ma trận nhầm lẫn](figures_paper_3/fig_p9_1.jpeg)
*Hình 3: Kiến trúc mạng nơ-ron tích hợp (ResNet/Vision Transformer) phân loại hóa đơn Thật vs. Giả mạo và ma trận kết quả thực nghiệm.*

Hệ thống kết hợp mạng tích chập sâu và Vision Transformer:
- Đầu vào: Ảnh hóa đơn RGB kết hợp bản đồ ELA và bản đồ phổ tần số.
- Đầu ra: Điểm số rủi ro gian lận (**Fraud Risk Score: 0% – 100%**) và khoanh vùng chính xác tọa độ các ô bị can thiệp.

---

## 4. KHUNG QUY TRÌNH KIỂM SOÁT NỘI BỘ THỜI KỶ NGUYÊN GEN-AI

Nghiên cứu của Đại học Newcastle & Sage đề xuất quy trình kiểm soát 4 bước tự động hóa:

```
[Nhân viên gửi ảnh Hóa đơn thanh toán]
                ↓
[Cổng Pháp y Thị giác máy tính (AI Forensics Gateway)]
  ├── Bước 1: Kiểm tra Siêu dữ liệu (EXIF / C2PA Metadata)
  ├── Bước 2: Chạy bộ lọc ELA & Phân tích tần số Wavelet
  └── Bước 3: Chấm điểm rủi ro bằng Deep Learning Model
                ↓
    ┌───────────┴───────────┐
    ↓                       ↓
Điểm rủi ro < 15%     Điểm rủi ro ≥ 15% (Nghi ngờ giả mạo)
    ↓                       ↓
Tự động chuyển duyệt  Khóa thanh toán tạm thời + Gửi Cảnh báo
chi tiền theo hạn mức  đến Trưởng phòng Kiểm soát Nội bộ kèm
                      ảnh nhiệt khoanh vùng số tiền bị sửa!
```

---

## CÂU HỎI THẢO LUẬN & TRANH BIỆN TRÊN LỚP (SEMINAR)

1. **Câu hỏi thảo luận 1 (Về kiểm soát nội bộ & Đạo đức nghề nghiệp):** *"Nếu nhân viên dùng AI tạo ra một hóa đơn tiếp khách giả trị giá 5.000.000 VNĐ cực kỳ giống thật để bù đắp cho những chi phí không tên không thể lấy hóa đơn, quy trình kiểm soát nội bộ truyền thống có phát hiện được không? Bạn đánh giá hành vi này dưới góc độ Chuẩn mực đạo đức nghề nghiệp kế toán như thế nào?"*
2. **Câu hỏi thảo luận 2 (Cuộc đua công nghệ):** *"Kẻ gian có thể dùng AI để 'lừa' lại bộ lọc ELA bằng cách thêm nhiễu giả vào ảnh không? Phía các công ty kiểm toán và cơ quan thuế cần làm gì để luôn đi trước tội phạm công nghệ một bước?"*

---
"""
    md_content = md_header + md_body

    # HTML Body Generation
    sidebar_links = """
      <a href="#abstract" class="sidebar-link active">Tóm tắt nghiên cứu</a>
      <a href="#sec1" class="sidebar-link">1. Bối cảnh & Đe dọa của Gen-AI</a>
      <a href="#sec2" class="sidebar-link">2. Phân tích tác động kế toán</a>
      <a href="#sec3" class="sidebar-link">3. Khung giải pháp Pháp y Hình ảnh</a>
      <a href="#sec3-1" class="sidebar-link sub-link">3.1 Phân tích lỗi nén ELA</a>
      <a href="#sec3-2" class="sidebar-link sub-link">3.2 Phân tích miền tần số Wavelet</a>
      <a href="#sec3-3" class="sidebar-link sub-link">3.3 Mô hình Học sâu bắt giả mạo</a>
      <a href="#sec4" class="sidebar-link">4. Quy trình kiểm soát nội bộ mới</a>
      <a href="#discussion" class="sidebar-link">Câu hỏi thảo luận trên lớp</a>
    """

    content_html = f"""
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
          Sự bùng nổ vũ bão của Trí tuệ Nhân tạo Tạo sinh (<strong>Generative AI - Gen-AI</strong>), bao gồm các mô hình khuếch tán hình ảnh (<em>Diffusion Models</em>), Mạng đối nghịch tạo sinh (<em>GANs</em>) và các công cụ chỉnh sửa ảnh thông minh, đang tạo ra một mối đe dọa mang tính sinh tử đối với tính toàn vẹn của hệ thống kế toán và kiểm toán toàn cầu. Kẻ gian, nhân viên nội bộ bất lương hoặc các đường dây tội phạm có tổ chức giờ đây có thể tạo ra những hóa đơn, biên lai thanh toán giả mạo hoàn hảo — từ hóa đơn mua sắm tiếp khách, vé máy bay điện tử đến hóa đơn mua nguyên vật liệu trị giá hàng tỷ đồng — với độ chân thực về vết nhàu, bóng sáng, phông chữ và logo đến mức <strong>mắt thường của kiểm toán viên con người hoàn toàn không thể nhận biết</strong>.
        </p>
        <p class="abstract-text" style="margin-top: 1rem;">
          Công trình nghiên cứu tiên phong này của Đại học Newcastle phối hợp với tập đoàn phần mềm kế toán quốc tế <strong>Sage PLC</strong> phân tích sâu sắc tác động kinh tế và cơ chế kỹ thuật của hiểm họa này, đồng thời đề xuất khung giải pháp <strong>Pháp y Hình ảnh số (Digital Image Forensics)</strong> dựa trên Thị giác Máy tính: (1) Phân tích mức độ lỗi nén (Error Level Analysis - ELA); (2) Phân tích miền tần số Wavelet nhận diện dấu vết vi mô của mô hình tạo sinh; và (3) Mạng Học sâu phân loại giả mạo tự động.
        </p>
        <p class="abstract-text" style="margin-top: 1rem;">
          Nghiên cứu cung cấp một lộ trình thực chiến giúp các nhà phát triển phần mềm kế toán và các hãng kiểm toán tích hợp "Kính hiển vi số" vào quy trình kiểm soát nội bộ, bảo vệ quỹ tiền mặt doanh nghiệp trước làn sóng gian lận tài chính thời đại AI.
        </p>
        <div class="keywords-box">
          <strong>Từ khóa:</strong> Hóa đơn giả mạo; Biên lai giả; AI tạo sinh (Gen-AI); Pháp y hình ảnh số (Image Forensics); Error Level Analysis (ELA); Kiểm toán gian lận; Kiểm soát nội bộ; Thị giác máy tính.
        </div>
      </section>

      <!-- Section 1 -->
      <section id="sec1">
        <h2 class="section-title">
          <span class="section-number">1</span>
          Bối Cảnh: Khi Mắt Thường Kiểm Toán Viên Bị "Vô Hiệu Hóa"
        </h2>
        <p>
          Trong suốt lịch sử kế toán kiểm toán truyền thống, phương thức kiểm tra chứng từ gốc (<em>Vouching</em>) dựa trên mắt nhìn của kiểm toán viên là bức tường lửa bảo vệ doanh nghiệp. Nếu một hóa đơn có đầy đủ chữ ký, con dấu, số tiền khớp với hợp đồng và nhìn không có dấu hiệu tẩy xóa cơ học, giao dịch sẽ được coi là hợp lệ.
        </p>
        <p>
          Tuy nhiên, AI tạo sinh đã làm thay đổi hoàn toàn cuộc chơi. Nếu như trước đây kẻ gian dùng Photoshop ghép số thì vẫn để lại đường viền răng cưa hoặc mất cân bằng sáng, thì hiện nay các mô hình Gen-AI (như Stable Diffusion inpainting) có thể thay thế một con số trên hóa đơn mà tự động tái tạo hoàn hảo từng hạt nhiễu, sợi giấy và độ mờ quang học. <strong>Mắt thường của con người đã chính thức trở nên bất lực!</strong>
        </p>

        <div class="callout callout-warning">
          <div class="callout-title" style="color: #d97706;">
            ⚠️ Tội Phạm Tài Chính Kỷ Nguyên Số Hóa
          </div>
          <p style="margin-bottom: 0;">
            Chỉ với một chiếc điện thoại di động và các website tạo biên lai giả mạo trực tuyến tích hợp AI, bất kỳ nhân viên nào cũng có thể "vẽ" ra một hóa đơn taxi hoặc ăn uống trị giá hàng chục triệu đồng trong chưa đầy 30 giây để thanh toán khống chi phí công tác.
          </p>
        </div>
      </section>

      <!-- Section 2 -->
      <section id="sec2">
        <h2 class="section-title">
          <span class="section-number">2</span>
          Phân Tích Tác Động Nghiệp Vụ Kế Toán & Thuế (Impact Analysis)
        </h2>
        <p>
          Bài báo của Thornton et al. chỉ rõ 3 cấp độ thiệt hại khổng lồ đối với nền kinh tế:
        </p>
        <ul>
          <li><strong>Thủng lưới quỹ tiền mặt doanh nghiệp:</strong> Gian lận thanh toán công tác (T&E Expense Fraud) làm bốc hơi từ 5% đến 15% ngân sách hoạt động của các công ty đa quốc gia.</li>
          <li><strong>Thất thu thuế và rủi ro hình sự:</strong> Việc sử dụng hóa đơn bất hợp pháp để trốn thuế TNDN và gian lận hoàn thuế GTGT quay vòng (VAT Carousel Fraud) khiến doanh nghiệp đối mặt với án phạt tiền tỷ và truy cứu trách nhiệm hình sự người đại diện pháp luật.</li>
          <li><strong>Khủng hoảng niềm tin kiểm toán:</strong> Kiểm toán viên độc lập không thể đưa ra ý kiến trung thực và hợp lý nếu bằng chứng kiểm toán được xây dựng trên nền tảng các hóa đơn giả mạo do AI tạo sinh.</li>
        </ul>
      </section>

      <!-- Section 3 -->
      <section id="sec3">
        <h2 class="section-title">
          <span class="section-number">3</span>
          Khung Giải Pháp Thị Giác Máy Tính & Pháp Y Hình Ảnh (Mitigation Strategies)
        </h2>
        <p>
          Để đối phó với kẻ gian dùng công nghệ cao, giải pháp duy nhất là sử dụng các công cụ <strong>Pháp y Hình ảnh số (Digital Image Forensics)</strong> dựa trên Computer Vision:
        </p>

        <div class="figure-wrapper">
          <div class="figure-img-container">
            <img src="figures_paper_3/fig_p7_1.jpeg" alt="Phân tích mức độ lỗi nén ELA trên hóa đơn" />
          </div>
          <div class="figure-caption">
            <strong>Hình 1:</strong> Phân tích mức độ lỗi nén (Error Level Analysis - ELA) — vùng con số bị chỉnh sửa bằng phần mềm đồ họa phát sáng rõ rệt so với nền giấy xám đồng nhất.
          </div>
        </div>

        <h3 id="sec3-1" class="sub-section-title">3.1. Phân Tích Mức Độ Sai Số Nén (Error Level Analysis - ELA)</h3>
        <p>
          Kỹ thuật ELA khai thác tính chất suy hao của chuẩn nén ảnh JPEG. Khi một hóa đơn được lưu nhiều lần, các pixel nguyên bản đạt trạng thái cân bằng nén tối màu. Nếu một con số mới được cấy ghép vào ảnh, vùng đó có chu kỳ nén ít hơn và sẽ <strong>phát sáng với mức năng lượng chênh lệch cao</strong> khi được tái nén ở chất lượng 95%:
        </p>
        <div class="math-block">
          \\Delta I(x, y) = |I_{{original}}(x, y) - I_{{recompressed}}(x, y)| \\times 20
        </div>

        <h3 id="sec3-2" class="sub-section-title">3.2. Phân Tích Miền Tần Số Wavelet & Dấu Vân Tay Cảm Biến (PRNU)</h3>
        <p>
          Mọi cảm biến camera vật lý đều để lại dấu vân tay nhiễu hạt siêu nhỏ không đồng đều (PRNU). AI tạo sinh tuy mô phỏng được hình ảnh mắt thấy nhưng hoàn toàn không thể tái tạo đúng quy luật phân bố năng lượng tần số cao của cảm biến quang học:
        </p>

        <div class="figure-wrapper">
          <div class="figure-img-container">
            <img src="figures_paper_3/fig_p8_1.jpeg" alt="Phân tích phổ tần số và dấu vết AI tạo sinh" />
          </div>
          <div class="figure-caption">
            <strong>Hình 2:</strong> Phân tích phổ tần số và dấu vết bất thường ở dải tần số cao của ảnh do mô hình khuếch tán sinh ra so với ảnh chụp thực tế.
          </div>
        </div>

        <h3 id="sec3-3" class="sub-section-title">3.3. Mô Hình Học Sâu Bắt Giả Mạo (Deep Learning Forgery Classifier)</h3>
        <p>
          Hệ thống tích hợp mạng ResNet và Vision Transformer để tự động trích xuất các đặc trưng vi mô của điểm ảnh, xuất ra điểm số rủi ro gian lận (Fraud Risk Score) từ 0% đến 100%:
        </p>

        <div class="figure-wrapper">
          <div class="figure-img-container">
            <img src="figures_paper_3/fig_p9_1.jpeg" alt="Khung phát hiện gian lận và ma trận nhầm lẫn" />
          </div>
          <div class="figure-caption">
            <strong>Hình 3:</strong> Kiến trúc mô hình học sâu phân loại hóa đơn Thật vs. Giả mạo và ma trận đánh giá hiệu năng đạt độ chính xác trên 96%.
          </div>
        </div>
      </section>

      <!-- Section 4 -->
      <section id="sec4">
        <h2 class="section-title">
          <span class="section-number">4</span>
          Quy Trình Kiểm Soát Nội Bộ Mới Cho Doanh Nghiệp
        </h2>
        <p>
          Thay vì để kế toán viên thanh toán "mù", doanh nghiệp cần thiết lập <strong>Cổng sàng lọc Pháp y AI tự động</strong>:
        </p>
        <div class="callout callout-info">
          <div class="callout-title" style="color: #2563eb;">
            🛡️ Bức Tường Lửa Kiểm Soát Nội Bộ 4 Bước
          </div>
          <ol style="margin-bottom: 0;">
            <li><strong>Thu thập:</strong> Nhân viên tải ảnh hóa đơn chi phí lên hệ thống phần mềm kế toán qua App di động.</li>
            <li><strong>Quét Pháp y tự động:</strong> Mô-đun Computer Vision lập tức chạy kiểm tra EXIF Metadata, thuật toán ELA và phân tích miền tần số trong 1,5 giây.</li>
            <li><strong>Phân luồng:</strong> Nếu điểm rủi ro &lt; 15%, hóa đơn được tự động chuyển sang luồng thanh toán thông thường.</li>
            <li><strong>Khóa cảnh báo:</strong> Nếu điểm rủi ro ≥ 15%, hệ thống lập tức khóa lệnh thanh toán, đồng thời gửi thông báo đỏ đến Kiểm toán nội bộ kèm ảnh nhiệt định vị chính xác vị trí con số bị làm giả!</li>
          </ol>
        </div>
      </section>

      <!-- Discussion Questions -->
      <section id="discussion" style="margin-top: 3.5rem;">
        <div class="callout callout-success">
          <div class="callout-title" style="font-size: 1.1rem; color: #059669;">
            💬 CÂU HỎI THẢO LUẬN & TRANH BIỆN TRÊN LỚP (SEMINAR)
          </div>
          <ol style="margin-top: 0.75rem; margin-bottom: 0.5rem;">
            <li><strong>Câu hỏi 1 (Tình huống đạo đức thực tế):</strong> Một nhân viên kinh doanh kỳ cựu mang về doanh thu hàng chục tỷ cho công ty nhưng bị phát hiện dùng AI tạo giả hóa đơn ăn tối 5 triệu đồng để thanh toán chi phí tiếp khách (với lý do quán ăn bình dân không xuất được hóa đơn đỏ). Nếu là Trưởng phòng Kiểm soát nội bộ, bạn sẽ xử lý tình huống này như thế nào?</li>
            <li><strong>Câu hỏi 2 (Pháp lý kiểm toán):</strong> Theo Chuẩn mực Kiểm toán Quốc tế (ISA 240) và Chuẩn mực Kiểm toán Việt Nam (VSA 240) về trách nhiệm của kiểm toán viên liên quan đến gian lận, nếu kiểm toán viên không sử dụng các công cụ công nghệ phân tích ảnh số và bỏ sót các hóa đơn giả mạo do Gen-AI tạo ra, kiểm toán viên có bị coi là thiếu sự thận trọng nghề nghiệp đúng mức (Professional Skepticism) hay không?</li>
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
        active_paper_idx=3
    )

    html_file_path = os.path.join(PAPERS_DIR, "paper_3_Fake_Invoices_Receipts_GenAI_tiengviet.html")
    with open(html_file_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"Generated Paper 3 HTML: {html_file_path}")

    # Generate Markdown file
    md_file_path = os.path.join(PAPERS_DIR, "paper_3_Fake_Invoices_Receipts_GenAI_tiengviet.md")
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Paper 3 Markdown: {md_file_path}")

if __name__ == "__main__":
    build()
