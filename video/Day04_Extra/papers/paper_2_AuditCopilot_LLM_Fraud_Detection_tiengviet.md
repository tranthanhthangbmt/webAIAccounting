# AUDITCOPILOT: KHAI PHÓNG SỨC MẠNH MÔ HÌNH NGÔN NGỮ LỚN ĐỂ PHÁT HIỆN GIAN LẬN TRONG BÚT TOÁN KÉP
*(AuditCopilot: Leveraging Large Language Models for Fraud Detection in Double-Entry Bookkeeping)*

- **Tác giả:** Md Abdul Kadir, Sai Suresh Macharla Vasu, Sidharth S. Nair, Daniel Sonntag (DFKI - German Research Center for Artificial Intelligence, Univ. of Oldenburg, Saarland Univ., cố vấn từ DATEV eG)
- **Đơn vị nghiên cứu:** Trung tâm Nghiên cứu Trí tuệ Nhân tạo Đức (DFKI), Đại học Oldenburg, Đại học Saarland, với sự bảo trợ chuyên môn từ Tập đoàn Phần mềm Kế toán DATEV eG.
- **Tài trợ học thuật:** Bộ Giáo dục và Nghiên cứu Liên bang Đức (BMBF - Grant 01IW24006 & 16IS23064).
- **Tập dữ liệu thực nghiệm:** Bộ dữ liệu tổng hợp chuẩn mực gồm 5.000 bút toán kép (Gronewald et al., 2024) và Bộ dữ liệu ẩn danh thực tế từ đối tác kiểm toán doanh nghiệp tại Đức.
- **Slide bài giảng tương ứng:** Slide P3: AuditCopilot for Audit Fraud Detection (Buổi 12/15)

---

## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

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
