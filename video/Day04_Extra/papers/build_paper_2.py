# -*- coding: utf-8 -*-
"""
Builder for Paper 2:
AuditCopilot: Leveraging Large Language Models for Fraud Detection in Double-Entry Bookkeeping
(Kadir, Vasu, Nair, Sonntag - DFKI, Oldenburg, Saarland & DATEV eG, 2025)
"""

import os
from generate_day04_helpers import get_html_template, PAPERS_DIR

TITLE_VI = "AuditCopilot: Khai Phóng Sức Mạnh Mô Hình Ngôn Ngữ Lớn Để Phát Hiện Gian Lận Trong Bút Toán Kép"
TITLE_EN = "AuditCopilot: Leveraging Large Language Models for Fraud Detection in Double-Entry Bookkeeping"
AUTHORS = "Md Abdul Kadir, Sai Suresh Macharla Vasu, Sidharth S. Nair, Daniel Sonntag (DFKI - German Research Center for Artificial Intelligence, Univ. of Oldenburg, Saarland Univ., cố vấn từ DATEV eG)"
JOURNAL = "DFKI Technical Report & Applied AI in Accounting (Đức) — Xuất bản Tháng 2/2025"
DOI = "Hỗ trợ tài trợ: Bộ Giáo dục & Nghiên cứu Liên bang Đức (BMBF 01IW24006) — Open Access CC BY 4.0"
BADGE = "Paper 2 • DFKI & DATEV Landmark (2025)"

def build():
    # 1. MARKDOWN CONTENT
    md_header = f"""# {TITLE_VI.upper()}
*({TITLE_EN})*

- **Tác giả:** {AUTHORS}
- **Đơn vị nghiên cứu:** Trung tâm Nghiên cứu Trí tuệ Nhân tạo Đức (DFKI), Đại học Oldenburg, Đại học Saarland, với sự bảo trợ chuyên môn từ Tập đoàn Phần mềm Kế toán DATEV eG.
- **Tài trợ học thuật:** Bộ Giáo dục và Nghiên cứu Liên bang Đức (BMBF - Grant 01IW24006 & 16IS23064).
- **Tập dữ liệu thực nghiệm:** Bộ dữ liệu tổng hợp chuẩn mực gồm 5.000 bút toán kép (Gronewald et al., 2024) và Bộ dữ liệu ẩn danh thực tế từ đối tác kiểm toán doanh nghiệp tại Đức.
- **Slide bài giảng tương ứng:** Slide P3: AuditCopilot for Audit Fraud Detection (Buổi 12/15)

---

"""
    md_body = """## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

Các kiểm toán viên tài chính và cơ quan thuế trên toàn thế giới phụ thuộc rất lớn vào các thử nghiệm kiểm tra bút toán nhật ký (**Journal Entry Tests - JETs**) để phát hiện các giao dịch bất thường trong sổ cái kế toán. Tuy nhiên, các phương pháp dựa trên quy tắc truyền thống này tạo ra **số lượng cảnh báo giả (False Positives) khổng lồ**, nhấn chìm kiểm toán viên trong biển thông tin nhiễu và dễ dàng bỏ lọt các sai phạm tinh vi (*subtle irregularities*).

Trong công trình nghiên cứu tiên phong này, chúng tôi phát triển hệ thống **AuditCopilot** – một framework ứng dụng các Mô hình Ngôn ngữ Lớn (LLMs) mã nguồn mở hàng đầu (Mistral, LLaMA, Gemma) để tự động phát hiện gian lận và sai lệch bất thường trong hệ thống **Bút toán kép (Double-Entry Bookkeeping)**.

Nhằm bảo mật tuyệt đối dữ liệu tài chính tối mật của doanh nghiệp và tuân thủ các quy định khắt khe của Luật Bảo vệ Dữ liệu (GDPR), AuditCopilot vận hành hoàn toàn trên các **mô hình trọng số mở cục bộ (On-Premise / Open-weight LLMs)**, không gửi bất kỳ byte dữ liệu nào ra các dịch vụ điện toán đám mây công cộng.

Bằng việc kết hợp kiến trúc Chuỗi tư duy (Chain of Thought), **bơm bối cảnh thống kê toàn cục (Global Context Injection)** và **thiết kế mô hình lai (Hybrid AI: kết hợp Isolation Forest với LLM)**, mô hình **Mistral 8B** đạt được kết quả đột phá chưa từng có:
- **Độ nhạy (Recall):** Đạt **0.98** (phát hiện chính xác 48/50 vụ gian lận thực tế).
- **Cảnh báo sai (False Positives):** Giảm ngoạn mục từ **942 (của JETs)** và **169 (của Machine Learning cổ điển)** xuống mức kỷ lục: **CHỈ CÒN 12 GIAO DỊCH!**
- **Độ chính xác (Precision):** Đạt **0.90** (90%), F1-Score đạt **0.94**.
- **Tính giải thích (Explainability):** Tự động sinh ra các đoạn giải trình nghiệp vụ bằng ngôn ngữ tự nhiên làm bằng chứng kiểm toán sơ bộ, giúp tiết kiệm hàng tuần làm việc điều tra hồ sơ.

---

## 1. BỐI CẢNH & NỖI ĐAU CỦA KIỂM TOÁN VIÊN (PROBLEM STATEMENT)

Trong kiểm toán Báo cáo tài chính, phát hiện các giao dịch bất thường (*anomalies*) — bao gồm sai sót vô tình, gian lận cố ý (*fraud*) và thủ thuật trốn thuế — là nhiệm vụ sống còn để bảo đảm tính trung thực và hợp lý của số liệu kế toán.

Tuy nhiên, kiểm toán viên phải đối mặt với hai thách thức khổng lồ:

### 1.1. Bản chất Đa thể thức của Dữ liệu Bút toán kép (Heterogeneous Data)
Một dòng bút toán trong sổ nhật ký chung không đơn thuần là một con số, mà tích hợp 4 loại dữ liệu dị biệt:
1. **Dữ liệu Số (Numeric):** Số tiền Nợ, Số tiền Có, thuế suất GTGT, số dư tài khoản.
2. **Dữ liệu Định danh / Phân loại (Categorical):** Mã số tài khoản kế toán, mã đối tượng pháp nhân, mã người nhập liệu (User ID), cờ Nợ/Có (Debit/Credit flags).
3. **Dữ liệu Thời gian (Temporal):** Ngày chứng từ, ngày ghi sổ, mốc thời gian hệ thống ghi nhận giao dịch.
4. **Dữ liệu Văn bản Tự do (Unstructured Narrative):** Phần diễn giải nội dung nghiệp vụ kinh tế phát sinh.

### 1.2. Sự Quá tải Dữ liệu & Sự Bất lực của Chọn mẫu Thủ công
Một doanh nghiệp quy mô vừa mỗi năm phát sinh từ vài trăm nghìn đến hàng triệu dòng bút toán. Phương pháp kiểm toán truyền thống là rút mẫu ngẫu nhiên vài trăm chứng từ. Phương pháp này hoàn toàn bất lực trước những thủ đoạn biển thủ được ngụy trang tinh vi: chia nhỏ khoản chi dưới hạn mức phê duyệt, hạch toán vào các tài khoản ít bị soi xét, hoặc thao túng các bút toán điều chỉnh vào ngày nghỉ cuối tuần.

---

## 2. TREE OF THOUGHTS: SO SÁNH 3 THẾ HỆ CÔNG NGHỆ

Để giải quyết bài toán, các nhà nghiên cứu tại DFKI đặt lên bàn cân 3 nhánh công nghệ:

### Nhánh 1: Kiểm tra Bút toán theo Quy tắc truyền thống (Journal Entry Tests - JETs)
- **Cách thức:** Sử dụng các truy vấn lọc điều kiện cứng nhắc (ví dụ: giao dịch vào thứ Bảy/Chủ nhật, số tiền chẵn, giao dịch ngoài giờ hành chính).
- **Kết quả thực chứng (Tập 5.000 bút toán):** Bắt được 45/50 lỗi (Recall: 0.90), nhưng tạo ra tới **942 CẢNH BÁO GIẢ (False Positives)**! Precision chỉ đạt 0.53.
- **Hệ lụy:** Kiểm toán viên rơi vào trạng thái kiệt quệ tinh thần (*Alert Fatigue*), mất hàng trăm giờ làm việc cho các giao dịch hợp lệ và mất tập trung vào các gian lận thực sự nguy hiểm.

### Nhánh 2: Học máy Cổ điển (Machine Learning Baseline - Isolation Forest)
- **Cách thức:** Thuật toán phân nhánh cây nhị phân không giám sát, tự động cô lập các điểm dữ liệu dị biệt nằm xa các cụm giao dịch bình thường.
- **Kết quả thực chứng:** Tìm được 49/50 lỗi (Recall: 0.98), số lượng cảnh báo giả giảm mạnh từ 942 xuống còn **169 trường hợp** (Precision: 0.61, F1: 0.68).
- **Điểm nghẽn cố hữu:** Bản chất "Hộp đen" (*Black Box*) và mù ngữ cảnh. Thuật toán chỉ xuất ra điểm số rủi ro toán học (ví dụ: *Anomaly Score = 0.89*) nhưng câm lặng hoàn toàn, không thể giải thích bằng ngôn ngữ con người lý do vi phạm nguyên tắc kế toán gì.

### Nhánh 3: AI Tạo sinh & Mô hình Ngôn ngữ Lớn Cục bộ (AuditCopilot với LLMs)
- **Đề xuất:** Khai phóng năng lực đọc hiểu ngữ cảnh nghiệp vụ sâu sắc của LLMs để vừa phát hiện dị biệt tinh vi, vừa giải trình rõ ràng bằng văn bản.
- **Giải bài toán bảo mật dữ liệu (Data Privacy):** Nghiên cứu cấm tuyệt đối việc tải sổ cái lên các API đám mây thương mại đóng kín (như ChatGPT của OpenAI) do vi phạm luật bảo mật và chuẩn mực đạo đức. Thay vào đó, AuditCopilot vận hành trên các **Mô hình Trọng số Mở (Open-weight LLMs)** như Mistral 8B, Gemma 7B, LLaMA 3.1 8B được triển khai nội bộ (*On-Premise Server*).

---

## 3. KIẾN TRÚC AUDITCOPILOT & KỸ THUẬT PROMPT TUNING

Thay vì huấn luyện lại toàn bộ mô hình (Fine-tuning rất tốn kém), nhóm nghiên cứu áp dụng kỹ thuật **Prompt Tuning** tinh vi với cấu trúc JSON chuẩn gồm 4 khối logic:
1. **Vai trò Chuyên gia (Role):** Bạn là chuyên gia kiểm toán tài chính hàng đầu chuyên về JET và phát hiện gian lận.
2. **Bối cảnh Toàn cục (Global Context):** Mean, Median, Phân vị thứ 95/99 của số tiền, hành vi giao dịch của User.
3. **Bộ 7 Tiêu chí Nhận diện Gian lận:** Số tiền bất thường, thiên lệch số tròn, hành vi người dùng dị thường, thời gian bất thường, mẫu hình tài khoản đối ứng lạ, điểm ngoại lai thống kê, vi phạm logic kinh doanh.
4. **Gợi ý từ Machine Learning (ML Hint):** Điểm số dị biệt từ thuật toán Isolation Forest.
5. **Đầu ra Ép buộc (Strict Output Schema):** Trả về JSON chuẩn với 3 trường: anomaly (0/1), confidence (0.0-1.0), explanation (lời giải thích chi tiết).

---

## 4. HAI ĐỘT PHÁ KỸ THUẬT CỐT LÕI

### Đột phá 1: Tiêm Bối cảnh Thống kê Toàn cục (Global Context Injection)
- Nếu chỉ đưa 1 dòng bút toán (ví dụ: chi phí 100 triệu), AI không thể biết 100 triệu là lớn hay nhỏ đối với công ty này.
- Nhóm nghiên cứu tính toán trước các chỉ số thống kê của toàn bộ sổ cái (Mean, Median, Phân vị 95th/99th, Min-Max, lịch sử hành vi của User) và đưa vào đầu Prompt. Nhờ đó, AI có hệ quy chiếu toàn diện như một Kiểm toán viên trưởng!

### Đột phá 2: Kiến trúc Trí tuệ Nhân tạo Lai (Hybrid AI: ML + LLM)
- Thuật toán Machine Learning (Isolation Forest) chạy trước để quét nhanh ma trận số liệu và gán nhãn rủi ro.
- Kết quả rủi ro này được đưa vào Prompt làm "Gợi ý" (*Hint*) cho LLM. LLM đóng vai trò "Thẩm phán tối cao" đọc gợi ý, kết hợp với phần diễn giải văn bản và quy tắc nghiệp vụ để đưa ra phán quyết cuối cùng và viết lời giải thích.

---

## 5. KẾT QUẢ THỰC NGHIỆM ĐỘT PHÁ (BẢNG 1 TỪ BÀI BÁO)

Thử nghiệm trên tập dữ liệu tổng hợp 5.000 bút toán (với 50 vụ gian lận thực tế):

| Nhóm Phương pháp | Mô hình / Thuật toán | Precision (Độ chính xác) | Recall (Độ nhạy) | F1-Score | Số lỗi bắt đúng (TP) | Cảnh báo SAI (FP) | Bỏ sót lỗi (FN) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Truyền thống** | Traditional JET | 0.53 | 0.90 | 0.50 | 45 | **942** | 5 |
| **Machine Learning** | Isolation Forest | 0.61 | 0.98 | 0.68 | 49 | **169** | 1 |
| **LLMs (AuditCopilot)**| Gemma 2B | 0.53 | 0.92 | 0.53 | 46 | 685 | 4 |
| | Gemma 7B | 0.71 | **0.99** | 0.79 | 50 | 68 | 0 |
| | LLaMA 3.1 8B | 0.67 | 0.88 | 0.73 | 44 | 78 | 6 |
| | **Mistral 8B** | **0.90** | **0.98** | **0.94** | **49** | **12 (Kỷ lục)** | **1** |
| | Mistral Small 22B | 0.53 | 0.92 | 0.52 | 46 | 711 | 4 |
| | GPT-5-mini (Cloud) | 0.55 | 0.95 | 0.56 | 48 | 466 | 2 |

> **Phát hiện quan trọng nhất:** Mô hình **Mistral 8B** đạt được sự hoàn hảo vượt bậc: Bắt được 49/50 vụ gian lận (Recall 0.98), số lượng cảnh báo giả giảm kinh hoàng từ **942 của JETs xuống CHỈ CÒN 12 GIAO DỊCH**, đẩy Precision lên **90%** và F1 đạt **0.94**!

---

## 6. PHÂN TÍCH BÓC TÁCH (ABLATION STUDY - BẢNG 2 TỪ BÀI BÁO)

Để chứng minh khoa học tính tất yếu của từng thành phần trong Prompt:

| Biến thể Prompt | Mô hình | Precision | Recall | Cảnh báo Sai (FP) | Bỏ sót Lỗi (FN) | Kết luận rút ra |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **AuditCopilot (Đầy đủ)** | Gemma 7B | **89%** | 78% | **32** | 73 | Điểm cân bằng tối ưu |
| **Bỏ Isolation Forest (w/o IF)** | Gemma 7B | **14%** | 90% | **1.973** *(tăng 60 lần)* | 34 | **ML là "Mỏ neo" giữ vững Precision** |
| **Bỏ cả Thống kê & IF** | Gemma 2B | **7%** | **7%** | 290 | **306** *(sót trầm trọng)* | **Thống kê là "Ngọn hải đăng" giữ Recall** |

---

## 7. GIÁ TRỊ TỐI THƯỢNG: TÍNH GIẢI THÍCH (EXPLAINABILITY)

Khác với Machine Learning chỉ xuất ra điểm số vô hồn, AuditCopilot cung cấp một trường `"explanation"` bằng văn bản tự nhiên:

> *"Bút toán này bất thường (anomaly = 1) vì nhân viên tài vụ A có lịch sử giao dịch rất thấp (trung bình 3 triệu/tháng) nhưng bỗng nhiên duyệt một bút toán chi phí tư vấn lên tới 350 triệu đồng (vượt ngưỡng phân vị 99th của toàn công ty) vào lúc 23h45 đêm Chủ nhật sang một tài khoản đối ứng chưa từng phát sinh giao dịch trong 12 tháng qua."*

Lời giải thích này đóng vai trò như một bản **Hồ sơ kiểm toán sơ bộ**, giúp kiểm toán viên tiết kiệm hàng tuần làm việc điều tra và có đủ luận cứ xác thực để chất vấn đối tượng nghi vấn ngay lập tức!

---

## 8. GIỚI HẠN & NGUYÊN TẮC QUẢN TRỊ NGHỀ NGHIỆP

Nghiên cứu của Kadir et al. (2025) khuyến cáo 3 ranh giới sống còn:
1. **Nguy cơ Prompt Injection qua trường diễn giải:** Kẻ gian có thể cố tình chèn văn bản gian dối để đánh lừa LLM bỏ qua cảnh báo.
2. **Tâm lý ỷ lại tự động hóa (Automation Bias):** Kiểm toán viên trẻ có thể tin tưởng mù quáng vào lời giải thích trôi chảy của AI mà lười biếng kiểm tra chứng từ gốc.
3. **AuditCopilot CHỈ LÀ CÔNG CỤ HỖ TRỢ QUYẾT ĐỊNH (Decision-Support Tool):** Tuyệt đối không được để AI tự ý ký báo cáo kiểm toán. Kiểm toán viên con người luôn là chốt chặn cuối cùng chịu trách nhiệm pháp lý (*Human-in-the-loop*).
"""
    md_content = md_header + md_body

    # 2. HTML CONTENT
    content_html = """
    <h2>Tóm Tắt Nghiên Cứu (Abstract)</h2>
    <p>Các kiểm toán viên tài chính và cơ quan thuế trên toàn thế giới phụ thuộc rất lớn vào các thử nghiệm kiểm tra bút toán nhật ký (<strong>Journal Entry Tests - JETs</strong>) để phát hiện các giao dịch bất thường trong sổ cái kế toán. Tuy nhiên, các phương pháp dựa trên quy tắc truyền thống này tạo ra <strong>số lượng cảnh báo giả (False Positives) khổng lồ</strong>, nhấn chìm kiểm toán viên trong biển thông tin nhiễu và dễ dàng bỏ lọt các sai phạm tinh vi.</p>

    <p>Trong công trình nghiên cứu tiên phong này công bố năm 2025, nhóm tác giả từ Trung tâm Nghiên cứu Trí tuệ Nhân tạo Đức (DFKI) và Đại học Oldenburg, với sự bảo trợ của Tập đoàn phần mềm kế toán DATEV eG, đã phát triển hệ thống <strong>AuditCopilot</strong> &mdash; một framework ứng dụng các Mô hình Ngôn ngữ Lớn (LLMs) mã nguồn mở hàng đầu để tự động phát hiện gian lận và sai lệch bất thường trong hệ thống <strong>Bút toán kép (Double-Entry Bookkeeping)</strong>.</p>

    <div class="callout callout-success">
      <div class="callout-icon">⚡</div>
      <div>
        <strong>Kỷ Lục Thực Chứng:</strong> Với mô hình nguồn mở <strong>Mistral 8B</strong> triển khai cục bộ (Local On-Premise), AuditCopilot đạt độ nhạy phát hiện gian lận <strong>0.98</strong> (49/50 vụ gian lận), và cắt giảm số lượng cảnh báo giả từ <strong>942 của JETs xuống CHỈ CÒN 12 GIAO DỊCH</strong>! Độ chính xác Precision đạt đỉnh <strong>0.90</strong> và F1 đạt <strong>0.94</strong>!
      </div>
    </div>

    <h2>1. Bối Cảnh & Nỗi Đau Của Kiểm Toán Viên</h2>
    <p>Dữ liệu Bút toán kép (Journal Entries - JEs) mang bản chất đa thể thức cực kỳ phức tạp:</p>
    <ul>
      <li><strong>Dữ liệu Số:</strong> Số tiền Nợ, Có, thuế suất, số dư tài khoản.</li>
      <li><strong>Dữ liệu Phân loại:</strong> Mã tài khoản, mã khách hàng/nhà cung cấp, User ID người lập biểu.</li>
      <li><strong>Dữ liệu Thời gian:</strong> Ngày ghi sổ, ngày chứng từ, giờ giao dịch.</li>
      <li><strong>Dữ liệu Văn bản Tự do:</strong> Diễn giải nghiệp vụ kinh tế phát sinh.</li>
    </ul>
    <p>Một doanh nghiệp phát sinh hàng triệu dòng bút toán mỗi năm. Việc chọn mẫu thủ công vài trăm chứng từ chẳng khác nào "mò kim đáy bể", khiến các sai phạm tinh vi rất dễ bị bỏ sót.</p>

    <h2>2. Tree of Thoughts: So Sánh 3 Thế Hệ Công Nghệ</h2>
    <table>
      <thead>
        <tr>
          <th>Thế hệ công nghệ</th>
          <th>Cơ chế hoạt động</th>
          <th>Ưu điểm</th>
          <th>Nhược điểm chí mạng</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Nhánh 1: Quy tắc JETs</strong></td>
          <td>Truy vấn SQL/ACL theo quy tắc tĩnh (cuối tuần, ngoài giờ, số chẵn)</td>
          <td>Đơn giản, dễ giải trình cho chuẩn mực</td>
          <td><span style="color:#f43f5e;font-weight:700">942 cảnh báo giả / 5.000 bút toán</span> &mdash; Gây tê liệt kiểm toán viên (Alert Fatigue)</td>
        </tr>
        <tr>
          <td><strong>Nhánh 2: Học máy Cổ điển (Isolation Forest)</strong></td>
          <td>Phân nhánh cây cô lập điểm dị biệt phi cấu trúc</td>
          <td>Cảnh báo giả giảm xuống 169, Recall đạt 0.98</td>
          <td><span style="color:#f43f5e;font-weight:700">Hộp đen (Black Box)</span> &mdash; Chỉ xuất ra điểm số vô hồn, không giải thích lý do</td>
        </tr>
        <tr>
          <td><strong>Nhánh 3: AuditCopilot (LLMs)</strong></td>
          <td>Prompt Tuning kết hợp Bối cảnh thống kê & gợi ý ML</td>
          <td><span style="color:#10b981;font-weight:700">Cảnh báo giả chỉ còn 12</span>, sinh lời giải thích bằng tiếng tự nhiên</td>
          <td>Cần hạ tầng máy chủ cục bộ (On-Premise) để bảo mật dữ liệu khách hàng</td>
        </tr>
      </tbody>
    </table>

    <div class="figure-box">
      <img src="figures_paper_2/page_7.png" alt="Cấu trúc Prompt AuditCopilot" />
      <div class="figure-caption">Hình 1: Cấu trúc Prompt Tuning chuẩn của AuditCopilot với bộ 7 tiêu chí nhận diện gian lận và bối cảnh thống kê toàn cục</div>
    </div>

    <h2>3. Kiến Trúc AuditCopilot & Hai Bí Quyết Kỹ Thuật</h2>
    
    <div class="callout callout-info">
      <div class="callout-icon">🧠</div>
      <div>
        <strong>Bí quyết 1: Tiêm Bối cảnh Thống kê Toàn cục (Global Context):</strong>
        <p style="margin:6px 0 0">Đưa Mean, Median, Phân vị 95th/99th, Min-Max và thống kê thói quen User vào Prompt. Giúp AI có hệ quy chiếu toàn diện để đánh giá quy mô giao dịch giống hệt một Kiểm toán viên trưởng.</p>
      </div>
    </div>

    <div class="callout callout-warning">
      <div class="callout-icon">🤝</div>
      <div>
        <strong>Bí quyết 2: Kiến trúc Trí tuệ Nhân tạo Lai (Hybrid AI):</strong>
        <p style="margin:6px 0 0">Không vứt bỏ Machine Learning! Cho Isolation Forest quét nhanh số liệu rồi nhúng cờ rủi ro làm "Gợi ý" (Hint) cho LLM. ML giải quyết tốc độ tính toán số học, còn LLM giải quyết khả năng đọc hiểu ngữ cảnh và diễn giải nghiệp vụ!</p>
      </div>
    </div>

    <h2>4. Bảng Kết Quả Thực Nghiệm Đột Phá (Table 1 từ Bài Báo)</h2>
    <table>
      <thead>
        <tr>
          <th>Nhóm</th>
          <th>Phương pháp</th>
          <th>Precision</th>
          <th>Recall</th>
          <th>F1-Score</th>
          <th>Bắt đúng (TP)</th>
          <th>Cảnh báo SAI (FP)</th>
          <th>Bỏ sót (FN)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Truyền thống</td>
          <td>Traditional JET</td>
          <td>0.53</td>
          <td>0.90</td>
          <td>0.50</td>
          <td>45</td>
          <td><span style="color:#f43f5e;font-weight:700">942</span></td>
          <td>5</td>
        </tr>
        <tr>
          <td>Machine Learning</td>
          <td>Isolation Forest</td>
          <td>0.61</td>
          <td>0.98</td>
          <td>0.68</td>
          <td>49</td>
          <td>169</td>
          <td>1</td>
        </tr>
        <tr>
          <td rowspan="4"><strong>AuditCopilot (LLMs)</strong></td>
          <td>Gemma 2B</td>
          <td>0.53</td>
          <td>0.92</td>
          <td>0.53</td>
          <td>46</td>
          <td>685</td>
          <td>4</td>
        </tr>
        <tr>
          <td>Gemma 7B</td>
          <td>0.71</td>
          <td><strong>0.99</strong></td>
          <td>0.79</td>
          <td>50</td>
          <td>68</td>
          <td>0</td>
        </tr>
        <tr>
          <td>LLaMA 3.1 8B</td>
          <td>0.67</td>
          <td>0.88</td>
          <td>0.73</td>
          <td>44</td>
          <td>78</td>
          <td>6</td>
        </tr>
        <tr style="background:rgba(16,185,129,0.15);font-weight:800">
          <td><strong>Mistral 8B</strong></td>
          <td><span style="color:#10b981">0.90</span></td>
          <td><span style="color:#10b981">0.98</span></td>
          <td><span style="color:#10b981">0.94</span></td>
          <td>49</td>
          <td><span style="color:#10b981;font-size:1.1rem">12 (KỶ LỤC)</span></td>
          <td>1</td>
        </tr>
        <tr>
          <td>Thương mại Cloud</td>
          <td>GPT-5-mini</td>
          <td>0.55</td>
          <td>0.95</td>
          <td>0.56</td>
          <td>48</td>
          <td>466</td>
          <td>2</td>
        </tr>
      </tbody>
    </table>

    <div class="figure-box">
      <img src="figures_paper_2/page_4.png" alt="Bảng số liệu Table 1 và Table 2" />
      <div class="figure-caption">Hình 2: Bảng kết quả thực nghiệm chi tiết và kiểm định bóc tách (Ablation Study) từ công bố gốc của DFKI (2025)</div>
    </div>

    <h2>5. Nghiên Cứu Bóc Tách (Ablation Study - Table 2)</h2>
    <p>Khi các tác giả cố tình tháo dỡ từng thành phần ra khỏi Prompt:</p>
    <ul>
      <li><strong>Tháo bỏ Isolation Forest (w/o IF):</strong> Số lượng cảnh báo sai của Gemma 7B bùng nổ từ 32 lên <strong>1.973 giao dịch (tăng gấp hơn 60 lần)</strong>, Precision rớt thảm hại từ 89% xuống 14%. &rarr; <em>ML chính là "chiếc mỏ neo" giữ vững độ chính xác Precision!</em></li>
      <li><strong>Tháo bỏ cả Thống kê toàn cục & IF (w/o Stats, IF):</strong> Tỷ lệ Recall sụp đổ, Gemma 2B bỏ sót tới <strong>306 vụ gian lận</strong>. &rarr; <em>Thống kê chính là "ngọn hải đăng" giữ vững độ nhạy Recall!</em></li>
    </ul>

    <h2>6. Giá Trị Tối Thượng: Tính Giải Thích (Explainability)</h2>
    <blockquote>
      "Giao dịch này bị đánh dấu bất thường (anomaly = 1) vì nhân viên tài vụ A có lịch sử giao dịch rất thấp (trung bình 3 triệu/tháng) nhưng bỗng nhiên duyệt một bút toán chi phí tư vấn lên tới 350 triệu đồng (vượt ngưỡng phân vị 99th của toàn công ty) vào lúc 23h45 đêm Chủ nhật sang một tài khoản đối ứng chưa từng phát sinh giao dịch trong 12 tháng qua."
    </blockquote>
    <p>Đoạn văn bản giải trình tự nhiên này trở thành bằng chứng kiểm toán sơ bộ có giá trị pháp lý, giúp kiểm toán viên tiết kiệm hàng tuần lễ đối soát thủ công.</p>

    <h2>7. Giới Hạn & Quản Trị Nghề Nghiệp (Governance)</h2>
    <div class="callout callout-danger">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>Nguyên tắc Quản trị Bắt buộc:</strong>
        <p style="margin:6px 0 0">AuditCopilot là công cụ hỗ trợ ra quyết định (Decision-Support Tool). Nghiêm cấm để AI tự ý ký duyệt Báo cáo kiểm toán. Kiểm toán viên con người luôn là chốt chặn cuối cùng chịu trách nhiệm pháp lý cao nhất (Human-in-the-loop)!</p>
      </div>
    </div>
    """

    full_html = get_html_template(
        title=TITLE_VI,
        title_en=TITLE_EN,
        authors=AUTHORS,
        journal=JOURNAL,
        doi=DOI,
        badge=BADGE,
        content_html=content_html,
        active_paper_idx=2
    )

    # Write files
    md_path = os.path.join(PAPERS_DIR, "paper_2_AuditCopilot_LLM_Fraud_Detection_tiengviet.md")
    html_path = os.path.join(PAPERS_DIR, "paper_2_AuditCopilot_LLM_Fraud_Detection_tiengviet.html")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Paper 2 generated successfully: MD ({len(md_content)} bytes), HTML ({len(full_html)} bytes)")

if __name__ == "__main__":
    build()
