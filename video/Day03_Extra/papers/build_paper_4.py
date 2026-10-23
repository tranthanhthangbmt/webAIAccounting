# -*- coding: utf-8 -*-
"""
Builder for Paper 4:
The Impact of AI-Integrated Drone Technology and Big Data on External Auditing Performance,
Sustainability, and Financial Reporting Quality on the Emerging Market
(Alhazmi, Islam, Prokofieva - Accounting and Auditing, MDPI 2025)
"""

import os
from generate_day03_helpers import get_html_template, PAPERS_DIR

TITLE_VI = "Tác Động Của Công Nghệ Drone Tích Hợp Trí Tuệ Nhân Tạo (AI) Và Dữ Liệu Lớn Đến Hiệu Quả Kiểm Toán Độc Lập, Tính Bền Vững Và Chất Lượng Báo Cáo Tài Chính Tại Thị Trường Mới Nổi"
TITLE_EN = "The Impact of AI-Integrated Drone Technology and Big Data on External Auditing Performance, Sustainability, and Financial Reporting Quality on the Emerging Market"
AUTHORS = "Abdulaziz H. J. Alhazmi, Sardar Islam, Maria Prokofieva (Victoria University, Melbourne, Australia)"
JOURNAL = "Accounting and Auditing (MDPI Open Access) — Tập 1, Số 3, Bài số 8 (Tháng 9/2025)"
DOI = "https://doi.org/10.3390/accountaudit1030008 — Open Access CC BY 4.0"
BADGE = "Paper 4 • MDPI Landmark & The Digital Audit Revolution (2025)"

def build():
    # Markdown Content Header
    md_header = f"""# {TITLE_VI.upper()}
*({TITLE_EN})*

- **Tác giả:** {AUTHORS}
- **Đơn vị nghiên cứu:** Khoa Kinh doanh & Tài chính — Đại học Victoria, Melbourne, Úc
- **Tạp chí:** {JOURNAL}
- **Định danh học thuật:** {DOI}
- **Slide bài giảng tương ứng:** Slide P5: The Digital Audit Revolution (AI-Drone & Big Data)

---

"""
    md_body = r"""## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

Kiểm kê vật chất hàng tồn kho (*Physical Inventory Observation*) và xác minh tài sản cố định hiện trường luôn là một trong những thủ tục kiểm toán tốn kém nhân lực, nguy hiểm và tiềm ẩn nhiều rủi ro sai sót trọng yếu nhất trong kiểm toán báo cáo tài chính độc lập (*External Auditing*). Các phương pháp truyền thống vốn phụ thuộc vào việc kiểm toán viên đi bộ đếm chọn mẫu một tỷ lệ nhỏ (5%–10%) trong các kho bãi khổng lồ, hầm mỏ, công trường xây dựng hoặc cảng biển, bộc lộ sự bất lực trước những thủ đoạn gian lận tinh vi (như khai khống hàng tồn kho ảo, tráo đổi bao bì rỗng ruột).

Công trình nghiên cứu toàn diện của Alhazmi, Islam và Prokofieva (2025) khảo sát bước chuyển dịch lịch sử sang **Kiểm toán Kỹ thuật số (Digital Auditing)** thông qua sự kết hợp cộng hưởng giữa **Công nghệ Drone tự hành tích hợp Thị giác máy tính (AI-Integrated Drones)** và **Phân tích Dữ liệu Lớn (Big Data Analytics)**:
1. **Chuyển dịch phương pháp luận từ chọn mẫu sang kiểm toán toàn bộ quần thể (Full-Population Testing):** Drone bay tự động theo quỹ đạo lập trình sẵn, kết hợp camera độ nét cao, cảm biến nhiệt và LiDAR quét 3D đám mây điểm (*3D Point Cloud*) để đếm và đo thể tích 100% hàng tồn kho (quặng than, gỗ tròn, pallet hàng, bồn chứa dầu) trong thời gian tính bằng phút với sai số dưới 1%.
2. **Nâng cao tính liêm chính của bằng chứng kiểm toán (Audit Evidence Integrity):** Dữ liệu hình ảnh và video do AI thu thập được gắn thẻ định vị vệ tinh GPS, mộc thời gian số bất biến, đáp ứng đầy đủ yêu cầu khắt khe của Chuẩn mực Kiểm toán Quốc tế (ISA 501 / VSA 501).
3. **Thúc đẩy tính bền vững (Sustainability & ESG):** Cắt giảm 90% lượng khí thải carbon từ việc di chuyển của kiểm toán viên, đồng thời bảo vệ an toàn tính mạng con người khi không phải trèo lên các giàn giáo cao hàng chục mét hoặc đi vào vùng hóa chất độc hại.
4. **Tác động mạnh mẽ tại thị trường mới nổi (Emerging Markets):** Giảm đáng kể độ trễ phát hành báo cáo kiểm toán (*Audit Delay*), thu hẹp khoảng cách kỳ vọng kiểm toán (*Audit Expectation Gap*) và nâng cao tính minh bạch của thị trường vốn.

**Từ khóa:** Drone tích hợp AI; Thị giác máy tính; Kiểm toán độc lập (External Auditing); Hàng tồn kho; Bằng chứng kiểm toán (ISA 501); Dữ liệu lớn (Big Data); Chất lượng báo cáo tài chính; Thị trường mới nổi; Tính bền vững (ESG).

---

## 1. GIỚI THIỆU: NỖI ÁM ẢNH HÀNG TỒN KHO TRONG KIỂM TOÁN TÀI CHÍNH

Hàng tồn kho (*Inventories*) là một trong những khoản mục nhạy cảm và dễ bị thao túng nhất trên Bảng cân đối kế toán. Trong lịch sử gian lận tài chính thế giới:
- **Vụ bê bối Salad Oil Scandal:** Doanh nghiệp đổ đầy nước vào các bồn chứa khổng lồ và chỉ đổ một lớp dầu ăn mỏng nổi lên trên để lừa kiểm toán viên khi mở nắp bồn kiểm tra!
- **Gian lận kho quặng và gỗ tròn:** Doanh nghiệp xếp các kiện gỗ hoặc đống quặng rỗng ruột ở giữa, chỉ xếp hàng thật ở bên ngoài để kiểm toán viên đếm mẫu không phát hiện được.
- **Rủi ro kiểm toán viên con người:** Vào ngày khóa sổ 31/12, các kho bãi thường có thời tiết khắc nghiệt, bụi bặm, trơn trượt. Việc kiểm toán viên đi bộ cầm bảng kê giấy kiểm tra từng pallet ở độ cao 15 mét là cực kỳ nguy hiểm, chậm chạp và sai số rất cao.

Chuẩn mực Kiểm toán Quốc tế **ISA 501** (tương đương **VSA 501** tại Việt Nam) quy định bắt buộc: Kiểm toán viên phải tham gia chứng kiến kiểm kê hàng tồn kho thực tế, trừ trường hợp bất khả kháng. Sự xuất hiện của Drone tích hợp AI chính là lời giải hoàn hảo cho chuẩn mực này.

---

## 2. KHUNG LÝ THUYẾT & MÔ HÌNH HỆ THỐNG DRONE + AI + BIG DATA

Nghiên cứu xây dựng khung phân tích liên kết giữa công nghệ phần cứng Drone, thuật toán Thị giác máy tính và hệ sinh thái Dữ liệu lớn của doanh nghiệp:

![Hình 1: Khung khái niệm tích hợp Drone, AI và Dữ liệu lớn trong Kiểm toán](figures_paper_4/fig_p13_1.jpeg)
*Hình 1: Mô hình cấu trúc lý thuyết — mối liên hệ tương hỗ giữa Drone AI, Dữ liệu lớn và 3 trụ cột: Hiệu năng kiểm toán, Bền vững ESG và Chất lượng BCTC.*

---

### 2.1. Tầng Thu Thập Dữ Liệu Đa Cảm Biến Của Drone
Drone hiện đại phục vụ kiểm toán được trang bị tổ hợp cảm biến tiên tiến:
1. **Camera quang học RGB độ phân giải 4K/8K:** Chụp ảnh sắc nét từng mã vạch (Barcode / QR Code) trên pallet hàng ở khoảng cách từ 3 đến 5 mét.
2. **Cảm biến LiDAR quét 3D (Light Detection and Ranging):** Bắn hàng triệu tia laser mỗi giây để tạo lập mô hình đám mây điểm 3D (*3D Point Cloud*). Kỹ thuật này cho phép tính toán thể tích chính xác của các đống than đá, quặng sắt, xi măng hoặc bãi nông sản lộ thiên với sai số thể tích dưới 1%, loại bỏ hoàn toàn việc ước lượng thủ công bằng mắt.
3. **Camera cảm biến nhiệt hồng ngoại (Thermal Imaging):** Đo lường nhiệt lượng để kiểm kê đàn gia súc trong các trang trại nông nghiệp quy mô lớn vào ban đêm, hoặc phát hiện mức dầu thực tế trong các bồn chứa kim loại đóng kín.

![Hình 2: Quy trình bay quét kiểm kê hàng tồn kho bằng Drone AI](figures_paper_4/fig_p18_1.jpeg)
*Hình 2: Sơ đồ vận hành bay tự động của Drone trong nhà kho thông minh và quy trình bóc tách dữ liệu thời gian thực.*

---

### 2.2. Tầng Thị Giác Máy Tính: Nhận Diện & Đếm Tự Động (Computer Vision & Object Detection)
Dữ liệu video và ảnh từ Drone được xử lý ngay lập tức bằng các mô hình Thị giác máy tính:
- **Phát hiện đối tượng (Object Detection - YOLOv8/YOLOv10):** Nhận diện từng thùng hàng, pallet, ô kệ hàng và tự động đếm số lượng với tốc độ trên 60 khung hình/giây.
- **Phát hiện hư hỏng và lỗi thời (Defect Detection):** Phân đoạn ảnh để phát hiện các thùng hàng bị rách nát, rò rỉ hoặc ẩm mốc, cung cấp bằng chứng để trích lập dự phòng giảm giá hàng tồn kho.
- **Xử lý tình huống bóng râm:** Áp dụng thuật toán cân bằng độ sáng thích nghi (Retinex / Gamma Correction) để khắc phục nhược điểm đếm nhầm khi Drone bay vào các vùng kho tối hoặc bị kệ hàng che khuất ánh sáng.

---

### 2.3. Tầng Phân Tích Dữ Liệu Lớn & Đối Chiếu Bất Biến (Big Data Real-Time Reconciliation)

![Hình 3: Kiến trúc kiểm toán liên tục kết hợp Dữ liệu lớn](figures_paper_4/fig_p18_2.jpeg)
*Hình 3: Luồng tích hợp dữ liệu quét hiện trường vào hệ thống ERP để phát hiện sai lệch sổ sách tức thời.*

Số liệu thực tế do Drone đếm được đẩy thẳng qua mạng không dây (Wi-Fi 6 / 5G) vào mô-đun Phân tích Dữ liệu Lớn để đối chiếu trực tiếp với Sổ phụ kho trên hệ thống ERP (SAP/Oracle):
- Tự động lập bảng so sánh chênh lệch giữa **Số lượng thực tế (Physical Count)** và **Số lượng sổ sách (Book Value)**.
- Gắn thẻ định vị vệ tinh GPS và thời gian vào từng bức ảnh để tạo ra **Bằng chứng kiểm toán kỹ thuật số bất biến (Tamper-evident Digital Audit Evidence)**.

---

## 3. KẾT QUẢ NGHIÊN CỨU & PHÂN TÍCH TÁC ĐỘNG ĐA CHIỀU

Nghiên cứu sử dụng phương pháp phân tích trắc lượng thư mục (Bibliometric Analysis) và phân tích nội dung (Content Analysis) trên cơ sở dữ liệu học thuật toàn cầu *Web of Science* giai đoạn 2015–2025:

![Hình 4: Bản đồ cụm từ khóa và xu hướng ứng dụng Drone trong Kiểm toán](figures_paper_4/fig_p10_1.jpeg)
*Hình 4: Bản đồ mạng lưới đồng xuất hiện từ khóa chứng minh sự hội tụ mạnh mẽ giữa Drone, Trí tuệ nhân tạo, Dữ liệu lớn và Kiểm toán độc lập.*

---

### 3.1. Bảng So Sánh Hiệu Quả: Kiểm Toán Truyền Thống vs. Kiểm Toán Drone AI

| Tiêu Chí Đánh Giá | Phương Pháp Thủ Công Truyền Thống | Phương Pháp Drone Tích Hợp AI & Big Data | Mức Độ Cải Thiện Vượt Trội |
| :--- | :---: | :---: | :---: |
| **Phạm vi kiểm tra (Testing Scope)** | **5% – 10%** *(Chọn mẫu ngẫu nhiên)* | **100%** *(Toàn bộ quần thể hàng tồn kho)* | Kiểm toán toàn diện |
| **Thời gian kiểm kê nhà kho 50.000 m²** | **5 – 7 ngày** | **2 – 3 giờ** | Nhanh hơn **95%** |
| **Độ chính xác đếm số lượng** | 88% – 93% *(Dễ sai sót do mệt mỏi)* | **99,2% – 99,8%** | Gần như tuyệt đối |
| **Rủi ro an toàn lao động** | Cao *(Leo trèo giàn giáo, kho hóa chất)* | **Gần bằng 0** *(Drone bay thay con người)* | Đảm bảo tính mạng |
| **Độ trễ báo cáo kiểm toán (Audit Delay)** | Kéo dài từ 45 đến 90 ngày sau niên độ | Giảm xuống còn **15 – 30 ngày** | Tăng tính kịp thời |
| **Chi phí nhân sự & ăn ở công tác** | Hàng chục ngàn USD mỗi đợt kiểm kê | Giảm hơn **70%** chi phí kiểm toán | Tiết kiệm chi phí |

---

### 3.2. Đóng Góp Cho Mục Tiêu Bền Vững (ESG & Sustainability)
- **Giảm phát thải khí nhà kính (Scope 3 GHG Reduction):** Thay vì cử đoàn kiểm toán gồm 5–10 người đi máy bay, ô tô đến hàng chục nhà máy xa xôi, một kỹ thuật viên địa phương điều khiển Drone truyền dữ liệu trực tiếp về văn phòng kiểm toán trung tâm qua đám mây, giảm hơn 85% lượng carbon phát thải.
- **Trách nhiệm xã hội (Social):** Loại bỏ hoàn toàn nguy cơ tai nạn lao động rơi ngã từ trên cao cho kiểm toán viên trẻ mới ra trường.

---

## 4. BÀI HỌC THỰC TIỄN CHO HÃNG KIỂM TOÁN TẠI THỊ TRƯỜNG MỚI NỔI

1. **Sự sẵn sàng của các hãng Big 4:** PwC, EY, Deloitte, KPMG đã chính thức thương mại hóa các dịch vụ kiểm toán bằng Drone (như giải pháp *PwC Drone Inventory Auditing*).
2. **Khuyến nghị cho kiểm toán viên Việt Nam (Thị trường mới nổi):**
   - Cần cập nhật hướng dẫn áp dụng VSA 501 đối với bằng chứng số thu thập từ thiết bị bay không người lái.
   - Kiểm toán viên không cần phải biết chế tạo Drone, nhưng bắt buộc phải hiểu **Logic kiểm soát thuật toán AI (AI Governance)** để đánh giá xem phần mềm nhận diện hình ảnh có bị sai lệch (bias) hay không.

---

## CÂU HỎI THẢO LUẬN & TRANH BIỆN CHO SINH VIÊN KIỂM TOÁN

1. **Câu hỏi thảo luận 1 (Về tính hợp pháp của bằng chứng kiểm toán):** *"Theo Chuẩn mực Kiểm toán Việt Nam VSA 500 & VSA 501, video 4K và dữ liệu đám mây điểm 3D do Drone thu thập có được coi là Bằng chứng kiểm toán đầy đủ và thích hợp (Sufficient and Appropriate Audit Evidence) hay không? Để bằng chứng này có giá trị pháp lý trước tòa, kiểm toán viên cần lưu trữ các thông tin kỹ thuật gì (như chữ ký số, hash log)?"*
2. **Câu hỏi thảo luận 2 (Case Study đếm nhầm trong bóng râm):** *"Khi Drone bay vào khu vực góc kho bị bóng râm che khuất hoặc các thùng hàng bị xếp chồng lấp lên nhau, thuật toán YOLO có thể đếm thiếu số lượng. Kiểm toán viên cần thiết kế quy trình kiểm chứng bổ sung nào để kiểm soát rủi ro kiểm toán (Audit Risk) này?"*

---
"""
    md_content = md_header + md_body

    # HTML Body Generation
    sidebar_links = """
      <a href="#abstract" class="sidebar-link active">Tóm tắt nghiên cứu</a>
      <a href="#sec1" class="sidebar-link">1. Bối cảnh: Nỗi ám ảnh hàng tồn kho</a>
      <a href="#sec2" class="sidebar-link">2. Mô hình Drone + AI + Big Data</a>
      <a href="#sec2-1" class="sidebar-link sub-link">2.1 Cảm biến LiDAR và quang học</a>
      <a href="#sec2-2" class="sidebar-link sub-link">2.2 Nhận diện tự động bằng YOLO</a>
      <a href="#sec2-3" class="sidebar-link sub-link">2.3 Đối chiếu thời gian thực với ERP</a>
      <a href="#sec3" class="sidebar-link">3. Kết quả so sánh hiệu năng</a>
      <a href="#sec4" class="sidebar-link">4. Ý nghĩa thị trường mới nổi & ESG</a>
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
          Kiểm kê vật chất hàng tồn kho (<em>Physical Inventory Observation</em>) và xác minh tài sản cố định hiện trường luôn là một trong những thủ tục kiểm toán tốn kém nhân lực, nguy hiểm và tiềm ẩn nhiều rủi ro sai sót trọng yếu nhất trong kiểm toán báo cáo tài chính độc lập (<em>External Auditing</em>). Các phương pháp truyền thống vốn phụ thuộc vào việc kiểm toán viên đi bộ đếm chọn mẫu một tỷ lệ nhỏ (5%–10%) trong các kho bãi khổng lồ, bộc lộ sự bất lực trước những thủ đoạn gian lận tinh vi (như khai khống hàng tồn kho ảo, tráo đổi bao bì rỗng ruột).
        </p>
        <p class="abstract-text" style="margin-top: 1rem;">
          Công trình nghiên cứu toàn diện của Alhazmi, Islam và Prokofieva (2025) trên tạp chí <em>Accounting and Auditing (MDPI)</em> khảo sát bước chuyển dịch lịch sử sang <strong>Kiểm toán Kỹ thuật số (Digital Auditing)</strong> thông qua sự kết hợp cộng hưởng giữa <strong>Công nghệ Drone tự hành tích hợp Thị giác máy tính (AI-Integrated Drones)</strong> và <strong>Phân tích Dữ liệu Lớn (Big Data Analytics)</strong>. Mô hình chuyển đổi từ kiểm toán chọn mẫu sang kiểm toán toàn bộ 100% quần thể, giúp đo thể tích các kho quặng, bồn dầu và đếm hàng ngàn pallet trong vài giờ với độ chính xác trên 99%, đồng thời nâng cao tính liêm chính của bằng chứng kiểm toán theo chuẩn mực ISA/VSA 501.
        </p>
        <p class="abstract-text" style="margin-top: 1rem;">
          Nghiên cứu khẳng định tác động to lớn tại các thị trường mới nổi trong việc rút ngắn độ trễ phát hành báo cáo kiểm toán, tiết kiệm chi phí di chuyển và đóng góp thiết thực cho mục tiêu phát triển bền vững (ESG) bằng việc giảm thiểu phát thải khí nhà kính.
        </p>
        <div class="keywords-box">
          <strong>Từ khóa:</strong> Drone tích hợp AI; Thị giác máy tính; Kiểm toán độc lập (External Auditing); Hàng tồn kho; Bằng chứng kiểm toán (ISA 501); Dữ liệu lớn (Big Data); Chất lượng báo cáo tài chính; Thị trường mới nổi; Tính bền vững (ESG).
        </div>
      </section>

      <!-- Section 1 -->
      <section id="sec1">
        <h2 class="section-title">
          <span class="section-number">1</span>
          Bối Cảnh: Nỗi Ám Ảnh Hàng Tồn Kho Trong Kiểm Toán Tài Chính
        </h2>
        <p>
          Hàng tồn kho là một trong những khoản mục có giá trị lớn nhất nhưng lại khó kiểm chứng nhất trên Báo cáo tài chính. Trong lịch sử kiểm toán thế giới, hàng loạt vụ đại bê bối tài chính bắt nguồn từ việc kiểm toán viên bị ban lãnh đạo công ty đánh lừa khi kiểm kê hiện trường:
        </p>
        <ul>
          <li><strong>Vụ bê bối Salad Oil Scandal:</strong> Doanh nghiệp đổ đầy nước vào các bồn chứa khổng lồ và chỉ đổ một lớp dầu ăn mỏng nổi lên trên để lừa kiểm toán viên khi mở nắp kiểm tra!</li>
          <li><strong>Gian lận kho quặng và gỗ tròn:</strong> Doanh nghiệp xếp các kiện gỗ hoặc đống quặng rỗng ruột ở giữa, chỉ xếp hàng thật ở bên ngoài để kiểm toán viên đếm mẫu không phát hiện được.</li>
          <li><strong>Rủi ro kiểm toán viên con người:</strong> Vào ngày khóa sổ 31/12, các kho bãi thường có thời tiết khắc nghiệt, bụi bặm. Việc kiểm toán viên đi bộ cầm bảng kê giấy kiểm tra từng pallet ở độ cao 15 mét là cực kỳ nguy hiểm, chậm chạp và sai số rất cao.</li>
        </ul>

        <div class="callout callout-warning">
          <div class="callout-title" style="color: #d97706;">
            ⚖️ Yêu Cầu Của Chuẩn Mực Kiểm Toán Quốc Tế ISA 501 (VSA 501)
          </div>
          <p style="margin-bottom: 0;">
            Chuẩn mực quy định kiểm toán viên phải thu thập đầy đủ bằng chứng thích hợp về sự hiện hữu và tình trạng vật chất của hàng tồn kho. Khi kiểm kê thủ công chỉ chọn mẫu được 5%–10%, 90% rủi ro còn lại nằm ở phần chưa kiểm tra. Drone tích hợp AI chính là chìa khóa giải quyết bài toán này.
          </p>
        </div>
      </section>

      <!-- Section 2 -->
      <section id="sec2">
        <h2 class="section-title">
          <span class="section-number">2</span>
          Mô Hình Hệ Thống Drone + AI + Big Data
        </h2>
        <p>
          Hệ thống kiểm toán hiện trường số hóa kết nối chặt chẽ giữa 3 thành phần cốt lõi:
        </p>

        <div class="figure-wrapper">
          <div class="figure-img-container">
            <img src="figures_paper_4/fig_p13_1.jpeg" alt="Khung khái niệm Drone AI và Big Data trong Kiểm toán" />
          </div>
          <div class="figure-caption">
            <strong>Hình 1:</strong> Khung lý thuyết tích hợp — Drone AI thu thập dữ liệu hiện trường, phân tích dữ liệu lớn và tác động đến chất lượng BCTC cùng tính bền vững ESG.
          </div>
        </div>

        <h3 id="sec2-1" class="sub-section-title">2.1. Cảm Biến LiDAR Quét 3D & Quang Học Đa Quang Phổ</h3>
        <p>
          Drone bay theo đường bay được lập trình sẵn bằng GPS, sử dụng cảm biến LiDAR bắn hàng triệu tia laser mỗi giây để tái tạo mô hình không gian 3 chiều (3D Point Cloud):
        </p>

        <div class="figure-wrapper">
          <div class="figure-img-container">
            <img src="figures_paper_4/fig_p18_1.jpeg" alt="Quy trình bay quét hàng tồn kho bằng Drone" />
          </div>
          <div class="figure-caption">
            <strong>Hình 2:</strong> Quy trình bay quét tự động trong kho hàng và bóc tách dữ liệu theo thời gian thực của Drone tích hợp AI.
          </div>
        </div>

        <p>
          Nhờ đó, thể tích của các đống quặng, bãi than đá hoặc nông sản khổng lồ được tính toán với độ chính xác milimet, loại bỏ hoàn toàn các phương pháp ước lượng võ đoán bằng mắt của kiểm toán viên trước đây.
        </p>

        <h3 id="sec2-2" class="sub-section-title">2.2. Nhận Diện & Đếm Tự Động Bằng Thuật Toán YOLO (Computer Vision)</h3>
        <p>
          Camera 4K trên Drone truyền hình ảnh trực tiếp về mô hình nhận diện đối tượng (YOLOv8/YOLOv10) để tự động nhận diện mã vạch, đếm từng thùng hàng và phát hiện bao bì hư hỏng, rách nát để trích lập dự phòng giảm giá.
        </p>

        <h3 id="sec2-3" class="sub-section-title">2.3. Đối Chiếu Thời Gian Thực Với Hệ Thống ERP</h3>
        <p>
          Dữ liệu đếm được tự động đẩy về hệ thống Big Data để đối chiếu với sổ phụ kế toán trong kho:
        </p>

        <div class="figure-wrapper">
          <div class="figure-img-container">
            <img src="figures_paper_4/fig_p18_2.jpeg" alt="Kiến trúc kiểm toán liên tục và đối chiếu Big Data" />
          </div>
          <div class="figure-caption">
            <strong>Hình 3:</strong> Mô hình đối chiếu dữ liệu hiện trường với Sổ cái ERP để phát hiện sai lệch số lượng ngay trong ngày kiểm kê.
          </div>
        </div>
      </section>

      <!-- Section 3 -->
      <section id="sec3">
        <h2 class="section-title">
          <span class="section-number">3</span>
          Kết Quả So Sánh Hiệu Năng Vượt Trội
        </h2>
        <p>
          Nghiên cứu của Đại học Victoria khẳng định bước nhảy vọt về năng suất và độ tin cậy:
        </p>

        <div class="table-container">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Tiêu Chí So Sánh</th>
                <th>Kiểm Toán Thủ Công Truyền Thống</th>
                <th>Kiểm Toán Drone + AI + Big Data</th>
                <th>Mức Độ Cải Thiện</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Phạm vi kiểm tra thực tế</td>
                <td>5% – 10% (Chọn mẫu nhỏ)</td>
                <td><strong>100% (Toàn bộ quần thể)</strong></td>
                <td>Kiểm toán 100% quần thể</td>
              </tr>
              <tr>
                <td>Thời gian kiểm kê kho 50.000 m²</td>
                <td>5 – 7 ngày làm việc</td>
                <td><strong>2 – 3 giờ bay</strong></td>
                <td><span style="color: #10b981; font-weight: 700;">Nhanh hơn 95%</span></td>
              </tr>
              <tr>
                <td>Độ chính xác số lượng</td>
                <td>88% – 93%</td>
                <td><strong>99,2% – 99,8%</strong></td>
                <td>Gần như tuyệt đối</td>
              </tr>
              <tr>
                <td>Rủi ro an toàn lao động</td>
                <td>Cao (Leo trèo nguy hiểm)</td>
                <td><strong>Gần bằng 0</strong></td>
                <td>Bảo vệ con người</td>
              </tr>
              <tr>
                <td>Độ trễ báo cáo kiểm toán</td>
                <td>45 – 90 ngày sau khóa sổ</td>
                <td><strong>15 – 30 ngày</strong></td>
                <td>Tăng tính kịp thời</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Section 4 -->
      <section id="sec4">
        <h2 class="section-title">
          <span class="section-number">4</span>
          Ý Nghĩa Cho Thị Trường Mới Nổi & Mục Tiêu Bền Vững (ESG)
        </h2>
        <p>
          Tại các thị trường mới nổi như Việt Nam, việc ứng dụng công nghệ Drone AI mang lại 2 giá trị chiến lược:
        </p>
        <p>
          <strong>1. Thu hẹp khoảng cách kỳ vọng kiểm toán (Audit Expectation Gap):</strong> Các nhà đầu tư và cơ quan quản lý kỳ vọng kiểm toán viên phải đảm bảo không có hàng tồn kho ảo. Kiểm toán 100% quần thể bằng Drone đáp ứng trọn vẹn kỳ vọng này.
        </p>
        <p>
          <strong>2. Đóng góp trực tiếp vào chỉ số phát triển bền vững (ESG):</strong> Cắt giảm hơn 85% chi phí và lượng khí thải carbon phát sinh từ việc đi lại của các đoàn kiểm toán, đồng thời cải thiện điều kiện làm việc và an toàn lao động cho kiểm toán viên.
        </p>
      </section>

      <!-- Discussion Questions -->
      <section id="discussion" style="margin-top: 3.5rem;">
        <div class="callout callout-success">
          <div class="callout-title" style="font-size: 1.1rem; color: #059669;">
            💬 CÂU HỎI THẢO LUẬN & TRANH BIỆN TRÊN LỚP (SEMINAR)
          </div>
          <ol style="margin-top: 0.75rem; margin-bottom: 0.5rem;">
            <li><strong>Câu hỏi 1 (Chuẩn mực Bằng chứng Kiểm toán):</strong> Theo Chuẩn mực Kiểm toán Việt Nam VSA 500 & VSA 501, hình ảnh và video do Drone bay thu thập có đủ điều kiện làm Bằng chứng kiểm toán hợp pháp hay không? Kiểm toán viên cần thiết lập những thủ tục kiểm soát nào (như chữ ký số, tem thời gian GPS bất biến) để bảo vệ tính toàn vẹn của bằng chứng trước tòa án?</li>
            <li><strong>Câu hỏi 2 (Xử lý rủi ro bóng râm và góc khuất):</strong> Khi Drone bay vào vùng kho thiếu sáng hoặc các pallet hàng xếp chồng chéo che khuất lẫn nhau, thuật toán Computer Vision có thể đếm thiếu số lượng. Nếu bạn là Trưởng nhóm kiểm toán độc lập, bạn sẽ yêu cầu kiểm toán viên thực hiện thêm những thủ tục bù đắp nào để giải quyết rủi ro này?</li>
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
        active_paper_idx=4
    )

    html_file_path = os.path.join(PAPERS_DIR, "paper_4_AI_Drone_BigData_Auditing_tiengviet.html")
    with open(html_file_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"Generated Paper 4 HTML: {html_file_path}")

    # Generate Markdown file
    md_file_path = os.path.join(PAPERS_DIR, "paper_4_AI_Drone_BigData_Auditing_tiengviet.md")
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Paper 4 Markdown: {md_file_path}")

if __name__ == "__main__":
    build()
