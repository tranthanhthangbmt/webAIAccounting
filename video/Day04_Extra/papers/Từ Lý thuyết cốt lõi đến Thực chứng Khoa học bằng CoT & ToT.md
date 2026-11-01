---
# SLIDE 1
**BUỔI 12: ỨNG DỤNG GENERATIVE AI TRONG KẾ TOÁN & KIỂM TOÁN**
*Từ Lý thuyết cốt lõi đến Thực chứng Khoa học bằng CoT & ToT*

**Giảng viên:** TS. Trần Thành Thắng
**Lớp:** Kế toán - Buổi 12/15
**Trường:** Đại học Đông Á - Phân hiệu Đắk Lắk

---
# SLIDE 2
**MỤC TIÊU BÀI HỌC (SCIENTIFIC METHOD)**

- **Khám phá không gian giải pháp (Tree of Thoughts - ToT):** Đánh giá đa chiều các phương pháp kiểm toán/kế toán: Truyền thống vs. Machine Learning cổ điển vs. Generative AI.
- **Suy luận logic tuần tự (Chain of Thought - CoT):** Hiểu cách các nhà khoa học "dạy" AI suy nghĩ từng bước để vượt qua điểm yếu về toán học và logic.
- **Thực chứng khoa học:** Áp dụng CoT và ToT vào phân tích 2 nghiên cứu mới nhất (2024-2025) về AI trong Kế toán & Kiểm toán.

---
# SLIDE 3
**TREE OF THOUGHTS (ToT) TRONG TỰ ĐỘNG HÓA KẾ TOÁN**

Để phát hiện sai sót/gian lận hoặc giải bài toán kế toán, chúng ta có 3 "nhánh" tư duy:
- **Nhánh 1: Quy tắc truyền thống (Rule-based/JETs):** Dùng điều kiện If/Else (ví dụ: giao dịch > 1 tỷ hoặc vào ngày nghỉ thì cảnh báo). Nhược điểm: Cứng nhắc, quá nhiều cảnh báo sai (False Positives).
- **Nhánh 2: AI Phân biệt (Machine Learning/Isolation Forest):** Thuật toán tìm điểm dị biệt. Ưu điểm: Ít cảnh báo sai hơn. Nhược điểm: Hộp đen, không giải thích được lý do bằng lời.
- **Nhánh 3: AI Tạo sinh (LLMs - ChatGPT/Claude):** Khả năng suy luận ngữ cảnh sâu. Nhược điểm: Dễ bị "ảo giác" hoặc tính toán sai nếu không có chiến lược Prompt đúng.

---
# SLIDE 4
**CHAIN OF THOUGHT (CoT): CÁCH "MỞ KHÓA" NHÁNH SỐ 3 (LLMs)**

Để LLM xử lý tốt nghiệp vụ Kế toán, ta không thể hỏi trực tiếp (Zero-shot) mà phải dẫn dắt AI suy luận từng bước (Chain of Thought):
1. **Phân tích bối cảnh:** Đọc dữ liệu đầu vào (Sổ cái, BCTC).
2. **Khai báo bộ quy tắc (RAG/Knowledge):** Cấp cho AI chuẩn mực kế toán (VAS/IFRS) hoặc luật thuế.
3. **Suy luận từng bước:** Bắt AI giải thích *tại sao* tính ra con số này trước khi đưa ra kết quả cuối.
4. **Cấp công cụ (Agents/ReAct):** Cho phép AI tự dùng máy tính (Calculator) để khắc phục lỗi cộng trừ.

---
# SLIDE 5
**TỪ LÝ THUYẾT ĐẾN THỰC TIỄN: 2 CASE STUDY KHOA HỌC**

Chúng ta sẽ áp dụng ToT và CoT để phân tích 2 bài báo đột phá:
- **Case 1: "Is it all hype?" (Eulerich & Wood, 2024)**[cite: 2] 
  *Câu hỏi:* LLM có thực sự vượt qua được các kỳ thi chứng chỉ Kế toán/Kiểm toán khắt khe nhất (CPA, CMA, CIA, EA) không?
- **Case 2: "AuditCopilot" (Kadir et al., 2025)**[cite: 34]
  *Câu hỏi:* LLM có thể thay thế thuật toán Machine Learning để phát hiện gian lận trong Bút toán kép (Double-Entry Bookkeeping) không?

---
# SLIDE 6
**BÀI BÁO 1: AI & CÁC KỲ THI KẾ TOÁN CHUYÊN NGHIỆP**
*Nghiên cứu của Eulerich, Wood et al. (2024)*[cite: 2]

- **Bối cảnh:** Báo chí thổi phồng (hype) rằng ChatGPT sẽ thay thế kế toán. Tuy nhiên, các nghiên cứu ban đầu cho thấy ChatGPT làm bài thi rất tệ[cite: 3].
- **Mục tiêu nghiên cứu:** Đánh giá lại năng lực thực sự của AI khi áp dụng các kỹ thuật Prompt tiên tiến nhất trên 4 kỳ thi: CPA (Kế toán công), CMA (Kế toán quản trị), CIA (Kiểm toán nội bộ) và EA (Đại lý thuế)[cite: 2, 4].

---
# SLIDE 7
**BÀI BÁO 1: SỰ THẤT BẠI CỦA ZERO-SHOT PROMPTING**

- **Bước thử đầu tiên (Nhánh ToT 1):** Cho ChatGPT 3.5 thi trực tiếp mà không hướng dẫn (Zero-shot)[cite: 4].
- **Kết quả:** ChatGPT 3.5 **THI TRƯỢT TẤT CẢ** các kỳ thi[cite: 2].
- **Chi tiết:** Điểm trung bình chỉ đạt **53.1%** (Dưới mức đỗ 70-75%)[cite: 14, 15]. Tệ nhất là mảng Thuế (EA) dành cho cá nhân chỉ đạt 37.3%[cite: 15].
- **Kết luận bước 1:** AI sơ khai chưa đủ kiến thức và khả năng tính toán để làm kế toán[cite: 2, 10].

---
# SLIDE 8
**BÀI BÁO 1: NÂNG CẤP MÔ HÌNH VÀ CHIẾN LƯỢC FEW-SHOT**

- **Nâng cấp 1: Dùng mô hình mạnh hơn (GPT-4).** Điểm số tăng mạnh thêm trung bình 16.5%[cite: 2]. GPT-4 đã thi đỗ chứng chỉ Kiểm toán nội bộ (CIA)[cite: 15].
- **Nâng cấp 2: Dùng 10-Shot Training.** Thay vì hỏi ngay, các nhà khoa học "dạy" AI bằng cách cung cấp 10 ví dụ mẫu trước khi hỏi[cite: 2].
- **Kết quả:** Điểm tăng thêm 6.6% nữa. Mô hình thi đỗ thêm chứng chỉ CMA[cite: 2, 16].
- *Vấn đề còn tồn đọng:* AI vẫn thi trượt môn Kế toán tài chính (CPA - FAR) và Thuế, do yếu toán học[cite: 16].

---
# SLIDE 9
**BÀI BÁO 1: BƯỚC ĐỘT PHÁ TỪ ReAct (REASONING & ACTING)**

- Để giải quyết triệt để điểm yếu tính toán, tác giả áp dụng **ReAct** - biến LLM thành một Agent (Đại lý hành động)[cite: 4, 26].
- **ReAct = Suy luận (Chain of Thought) + Hành động (Sử dụng công cụ).** 
- Thay vì tự nhẩm tính, ChatGPT được cấp quyền dùng **Máy tính bỏ túi (Calculator)** và **Tìm kiếm Web (Search)** để tra cứu tỷ giá/luật thuế[cite: 4, 26].
- **Kết quả chấn động:** Điểm số tăng thêm 8.9%. GPT-4 **THI ĐỖ 100% CÁC KỲ THI** (CPA, CMA, CIA, EA) với điểm trung bình **85.1%**[cite: 2, 17].

---
# SLIDE 10
**BÀI BÁO 1: BÀI HỌC RÚT RA CHO SINH VIÊN KẾ TOÁN**

- Khoảng cách giữa việc AI "vô dụng" (37%) và AI "xuất sắc" (85%) nằm ở **Kỹ năng Prompting (Few-shot, CoT, ReAct)**[cite: 15, 17].
- Ứng dụng thực tiễn: Khi các em dùng AI làm bài tập Thuế hoặc phân tích Báo cáo tài chính, tuyệt đối đừng để AI tự cộng trừ. Hãy viết Prompt yêu cầu AI suy luận công thức, sau đó tích hợp công cụ (Data Analysis/Calculator) để ra kết quả[cite: 12].

---
# SLIDE 11
**BÀI BÁO 2: AI TRONG BÚT TOÁN KÉP (DOUBLE-ENTRY)**
*Nghiên cứu của Kadir, Vaso, Nair & Sonntag (2025)*[cite: 34]

- **Bài toán:** Các Kiểm toán viên cần tìm các giao dịch bất thường (gian lận, trốn thuế) trong hàng triệu dòng bút toán[cite: 34].
- Khám phá ToT - Các cách tiếp cận hiện tại:
  - **Rule-based (JETs):** Cảnh báo quá nhiều (False Positives) khiến kiểm toán viên quá tải[cite: 34].
  - **Machine Learning (Isolation Forest):** Tìm đúng dị biệt nhưng không biết giải thích "Tại sao nó bất thường?"[cite: 34].

---
# SLIDE 12
**BÀI BÁO 2: SỰ KÉM HIỆU QUẢ CỦA CÔNG CỤ TRUYỀN THỐNG**

Thực chứng trên tập dữ liệu tổng hợp (Synthetic Dataset) có 5.000 giao dịch (chỉ có 50 giao dịch gian lận thực sự)[cite: 35, 36]:
- **Công cụ JET (Quy tắc truyền thống):** Tìm được 45/50 lỗi, nhưng lại báo động nhầm tới **942 giao dịch bình thường** (False Positives)[cite: 37].
- **Thuật toán Isolation Forest:** Tìm được 49/50 lỗi, báo động nhầm giảm xuống còn **169 giao dịch**[cite: 37].
- *Nỗi đau của Kiểm toán viên:* Họ vẫn phải tự đọc tay 169 giao dịch này để tự tìm ra nguyên nhân[cite: 34].

---
# SLIDE 13
**BÀI BÁO 2: GIẢI PHÁP "AUDIT COPILOT" TỪ LLMs**

Nhóm tác giả thiết kế một hệ thống Prompt (AuditCopilot) kết hợp cả 3 yếu tố[cite: 35, 40]:
1. **Dữ liệu giao dịch:** Ngày tháng, tài khoản, số tiền, người thực hiện[cite: 34].
2. **Context (Bối cảnh thống kê):** Cung cấp cho LLM thông tin về số dư trung bình, bách phân vị thứ 95/99 để AI có hệ quy chiếu[cite: 35, 40].
3. **Gợi ý từ Machine Learning:** Cung cấp điểm số của thuật toán Isolation Forest vào Prompt cho LLM[cite: 35, 40].
Yêu cầu LLM trả về JSON: Có gian lận không? (0/1) + **Lời giải thích tự nhiên.**[cite: 35, 40]

---
# SLIDE 14
**BÀI BÁO 2: KẾT QUẢ CỦA SỰ KẾT HỢP (HYBRID AI)**

- Khi dùng mô hình LLM mở (Mistral-8B) với prompt AuditCopilot, AI đã đạt kết quả đỉnh cao[cite: 36]:
- **Báo động nhầm (False Positives) giảm kỷ lục: Từ 942 (của JET) xuống chỉ còn 12 giao dịch!**[cite: 37]
- **Tỷ lệ phát hiện (Recall):** 98% (tìm ra gần như mọi gian lận)[cite: 37].
- Đặc biệt: AI tự động viết ra **lời giải thích** (Explanation) cho từng bút toán nghi ngờ, giúp Kiểm toán viên tiết kiệm hàng tuần làm việc[cite: 35, 40].

---
# SLIDE 15
**TỔNG KẾT BUỔI 12 & CÂU HỎI THẢO LUẬN**

1. **Tổng kết:** 
   - AI chỉ là công cụ. Nó yếu hay mạnh phụ thuộc vào **cấu trúc tư duy (CoT)** và **quy trình cấp quyền (Agents/ReAct)** mà người dùng tạo ra cho nó.
   - LLMs không thay thế phương pháp thống kê cổ điển, mà kết hợp với chúng (AuditCopilot) để tối ưu hóa nghề kiểm toán.
2. **Thảo luận (5 phút):** 
   - *Theo các bạn, nếu một hệ thống như AuditCopilot giải thích sai (Ảo giác AI) về một bút toán, ai sẽ là người chịu trách nhiệm pháp lý trước pháp luật: Kiểm toán viên, công ty phần mềm, hay công ty được kiểm toán?*