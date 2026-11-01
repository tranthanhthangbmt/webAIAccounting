---
# SLIDE 1
**PHÂN TÍCH CHUYÊN SÂU BÀI BÁO KHOA HỌC:**
*AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping (Kadir et al., 2025)*[cite: 74]

**Giảng viên:** TS. Trần Thành Thắng
**Lớp:** Kế toán - Buổi 12/15 (Phần Thực chứng)
**Trường:** Đại học Đông Á - Phân hiệu Đắk Lắk

---
# SLIDE 2
**MỤC TIÊU BÀI GIẢNG (ToT & CoT)**

- **Tree of Thoughts (Khám phá Giải pháp):** Đánh giá 3 nhánh công nghệ trong kiểm toán hiện đại (Quy tắc truyền thống vs. Học máy cổ điển vs. Mô hình ngôn ngữ lớn LLMs).
- **Chain of Thought (Suy luận Logic):** Bóc tách cách các nhà khoa học "kỹ thuật hóa" một LLM (vốn thiên về ngôn ngữ) thành một chuyên gia phát hiện gian lận tài chính thông qua Prompt Engineering[cite: 75].
- **Mục tiêu cốt lõi:** Sinh viên nắm được cách thiết kế "luồng công việc" (Workflow) kết hợp AI và con người[cite: 74].

---
# SLIDE 3
**THỰC TRẠNG: NỖI ĐAU CỦA KIỂM TOÁN VIÊN**

- **Bối cảnh:** Phát hiện các giao dịch bất thường (lỗi, gian lận, trốn thuế) là nhiệm vụ sống còn để bảo vệ tính toàn vẹn của BCTC[cite: 74].
- **Vấn đề của dữ liệu:** Bút toán kép (Journal Entry) chứa dữ liệu cực kỳ phức tạp: Số tiền (Numeric), Mã tài khoản (Categorical) và Diễn giải (Text)[cite: 74].
- **Sự quá tải:** Khối lượng dữ liệu khổng lồ khiến việc lấy mẫu thủ công dễ bỏ sót các sai phạm tinh vi (subtle irregularities)[cite: 74]. 

---
# SLIDE 4
**TREE OF THOUGHTS: 3 NHÁNH GIẢI QUYẾT BÀI TOÁN**

Để tìm ra gian lận, các công ty kiểm toán có 3 lựa chọn (Nhánh tư duy):
- **Nhánh 1 - Kiểm tra Bút toán truyền thống (JETs):** Dùng các bộ quy tắc (Rules) cứng nhắc.
- **Nhánh 2 - Machine Learning (Isolation Forest):** Thuật toán tự động cô lập các điểm dị biệt phi cấu trúc[cite: 74].
- **Nhánh 3 - Generative AI (LLMs):** Sử dụng các mô hình như LLaMA, Gemma, Mistral để đóng vai trò "Trợ lý kiểm toán" (AuditCopilot) đọc và hiểu bối cảnh[cite: 74, 76].

---
# SLIDE 5
**ĐÁNH GIÁ NHÁNH 1: SỰ THẤT BẠI CỦA JETs**

- **Cách hoạt động:** Lọc dữ liệu theo điều kiện (Ví dụ: Giao dịch vào cuối tuần, số tiền chẵn...).
- **Kết quả thực chứng (Tập dữ liệu 5.000 bút toán):** JET tìm được 45/50 lỗi (Recall: 0.90) nhưng lại tạo ra tới **942 cảnh báo sai (False Positives)**[cite: 76, 77].
- **Hệ lụy:** Kiểm toán viên bị "nhấn chìm" trong hàng nghìn cảnh báo giả, gây lãng phí thời gian và làm giảm độ nhạy bén nghề nghiệp[cite: 74].

---
# SLIDE 6
**ĐÁNH GIÁ NHÁNH 2: MACHINE LEARNING (ISOLATION FOREST)**

- **Cách hoạt động:** Thuật toán tự nhóm các giao dịch bình thường và "cô lập" các giao dịch có hành vi lạ (clustering/isolation)[cite: 74].
- **Kết quả thực chứng:** Tìm được 49/50 lỗi (Recall: 0.98), số lượng cảnh báo sai giảm mạnh chỉ còn **169 (False Positives)**[cite: 76, 77].
- **Hạn chế:** Các mô hình ML truyền thống này thiếu "khả năng hiểu ngữ cảnh" (contextual understanding)[cite: 75]. Chúng chỉ báo "Đây là lỗi" nhưng không thể giải thích bằng lời "Tại sao lỗi?" cho kiểm toán viên[cite: 75].

---
# SLIDE 7
**NHÁNH 3: GIẢI PHÁP LLM & VẤN ĐỀ BẢO MẬT**

- **Đề xuất:** Dùng LLM thay thế/hỗ trợ các phương pháp cũ[cite: 74].
- **Vấn đề Bảo mật (Privacy):** Dữ liệu kế toán là bí mật doanh nghiệp. Việc gửi sổ cái lên ChatGPT (OpenAI) là rủi ro cực lớn[cite: 76, 77].
- **Giải pháp của nghiên cứu:** Sử dụng các mô hình mã nguồn mở (Open-weight LLMs) như LLaMA (Meta), Gemma (Google), Mistral để chạy cục bộ (local), đảm bảo tuyệt đối tính bảo mật dữ liệu khách hàng[cite: 74, 76].

---
# SLIDE 8
**CHAIN OF THOUGHT: KIẾN TRÚC "AUDIT COPILOT"**

Thay vì huấn luyện lại toàn bộ AI (Rất tốn kém), nhóm nghiên cứu dùng kỹ thuật **Prompt Tuning** để điều khiển hành vi của LLM[cite: 75]. 
*Cấu trúc Prompt chuẩn JSON gồm:*
1. **Vai trò:** "Bạn là chuyên gia kiểm toán..."[cite: 80]
2. **Tiêu chí:** 7 dấu hiệu gian lận (Tiền lớn bất thường, làm ngoài giờ, tài khoản lạ...)[cite: 80]
3. **Đầu vào:** Chi tiết 1 dòng bút toán (Ngày, ID, Tiền, Thuế...)[cite: 75, 80]
4. **Đầu ra ép buộc:** Định dạng strict JSON `{"anomaly": 0/1, "explanation": "..."}`[cite: 80].

---
# SLIDE 9
**BÍ QUYẾT 1: CUNG CẤP "BỐI CẢNH TOÀN CỤC" (CONTEXT)**

- *Suy luận logic (CoT):* Nếu chỉ đưa cho AI 1 giao dịch 100 triệu, nó không biết là to hay nhỏ.
- *Giải pháp:* Nhóm nghiên cứu "bơm" thêm các thông số Thống kê toàn cục (Statistics) vào Prompt:
  - Giá trị Trung bình (Mean), Trung vị (Median)[cite: 80].
  - Điểm phân vị thứ 95 (95th percentile)[cite: 80].
  - Tần suất hoạt động của User đó (User behavior)[cite: 80].
- Nhờ vậy, AI có hệ quy chiếu để đánh giá giống hệt tư duy của con người[cite: 75].

---
# SLIDE 10
**BÍ QUYẾT 2: SỨC MẠNH LAI (HYBRID AI)**

- Không vứt bỏ thuật toán cũ, AuditCopilot tích hợp thẳng kết quả của **Isolation Forest** vào Prompt làm "Gợi ý" (Hint) cho LLM[cite: 75, 80].
- *Luồng tư duy:* Thuật toán ML làm nhiệm vụ cày xới số liệu thô -> Đưa ra chỉ số nghi ngờ -> LLM đọc chỉ số đó kết hợp với bối cảnh tài khoản để đưa ra phán quyết cuối cùng và viết lời giải thích[cite: 75].

---
# SLIDE 11
**KẾT QUẢ ĐỘT PHÁ (MÔ HÌNH MISTRAL-8B)**

Thử nghiệm trên tập dữ liệu tổng hợp mang lại kết quả chấn động[cite: 77]:
- **Phát hiện đúng (Recall):** 0.98 (Tìm ra 48/50 lỗi, chỉ sót 2)[cite: 77].
- **Cảnh báo sai (False Positives):** Giảm từ 942 (của JET) và 169 (của ML) xuống mức kỷ lục: **Chỉ còn 12 giao dịch!**[cite: 76, 77].
- **Độ chính xác (Precision):** Đạt 0.90, cao nhất trong tất cả các phương pháp thử nghiệm[cite: 76, 77].

---
# SLIDE 12
**TẠI SAO NÓ HOẠT ĐỘNG? (ABLATION STUDY)**

Nghiên cứu bóc tách (Ablation) chứng minh tầm quan trọng của thiết kế Prompt[cite: 76]:
1. **Nếu bỏ Isolation Forest ra khỏi Prompt:** Số cảnh báo sai (FP) tăng vọt (Ví dụ Gemma-7B tăng từ 32 lên 1973 lỗi giả)[cite: 76, 77]. -> *ML giúp giữ độ chính xác (Precision).*
2. **Nếu bỏ Số liệu thống kê (Statistics) ra khỏi Prompt:** LLM bị "mù", bỏ lót lỗi trầm trọng (Gemma-2B sót tới 306 lỗi)[cite: 76, 77]. -> *Thống kê giúp duy trì độ phủ (Recall).*

---
# SLIDE 13
**GIÁ TRỊ TỐI THƯỢNG: TÍNH GIẢI THÍCH (EXPLAINABILITY)**

- Khác với hộp đen của Machine Learning, LLM cung cấp một trường `"explanation"` bằng ngôn ngữ tự nhiên[cite: 74, 80].
- Thay vì chỉ hiện cảnh báo đỏ, hệ thống trả về: *"Giao dịch này bất thường (1) vì nhân viên A có lịch sử giao dịch rất thấp nhưng lại duyệt bút toán nằm ở bách phân vị thứ 99 ngoài giờ hành chính."*
- Giúp Kế toán trưởng/Kiểm toán viên tiết kiệm hàng tuần làm việc để lập hồ sơ kiểm toán[cite: 74, 75].

---
# SLIDE 14
**GIỚI HẠN & CẢNH BÁO NGHỀ NGHIỆP (LIMITATIONS)**

- **Ảo giác (Hallucinations) & Bias:** LLM vẫn có thể bịa ra lý do không có thật nếu thiết lập sai thông số (Temperature)[cite: 75, 77].
- **Sự phụ thuộc (Automation Bias):** Kiểm toán viên có thể sinh ra tâm lý ỷ lại, tin tưởng tuyệt đối vào lời giải thích nghe "rất bùi tai" của AI[cite: 77].
- **Governance (Quản trị):** AuditCopilot chỉ là công cụ hỗ trợ quyết định (Decision-support), không bao giờ được phép tự ra quyết định cuối cùng thay con người[cite: 77].

---
# SLIDE 15
**TỔNG KẾT & CÂU HỎI THẢO LUẬN**

- **Tổng kết:** Generative AI không giết chết Kế toán, mà các Kế toán viên biết thiết kế luồng (Workflow/Prompt) kết hợp giữa ML cổ điển và LLMs sẽ thay thế những người làm thủ công (JET).
- **Thảo luận cuối khóa (10 phút):**
  *Trong vai trò là một Kiểm toán viên nội bộ tương lai, nếu một phần mềm AI (như AuditCopilot) được công ty bạn mua về, bạn sẽ đề xuất quy trình "Kiểm tra chéo" (Human-in-the-loop) như thế nào để đảm bảo AI không che giấu các gian lận tinh vi do chính giám đốc tài chính chỉ đạo?*