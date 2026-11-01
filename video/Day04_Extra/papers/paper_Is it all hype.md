---
# SLIDE 1
**PHÂN TÍCH CHUYÊN SÂU BÀI BÁO KHOA HỌC:**
*Is it all hype? ChatGPT's performance and disruptive potential in the accounting and auditing industries (Eulerich et al., 2024)*[cite: 42]

**Giảng viên:** TS. Trần Thành Thắng
**Lớp:** Kế toán - Buổi 12/15 (Phần 2)
**Trường:** Đại học Đông Á - Phân hiệu Đắk Lắk

---
# SLIDE 2
**MỤC TIÊU CỦA BÀI PHÂN TÍCH (ToT & CoT)**

- **Tree of Thoughts (Khám phá):** Đánh giá các ngưỡng năng lực khác nhau của AI qua từng phương pháp Prompting.
- **Chain of Thought (Suy luận):** Theo dõi chuỗi logic của nhóm nghiên cứu khi "dạy" AI thi Kế toán: Từ một cỗ máy học vẹt thành một chuyên gia biết dùng công cụ (Agents).
- **Mục tiêu cốt lõi:** Trả lời câu hỏi: Sự đe dọa của AI đối với nghề kế toán chỉ là "lời đồn thổi" (Hype) hay là "sự thật"?[cite: 42]

---
# SLIDE 3
**BỐI CẢNH: NỖI SỢ HÃI VÀ THỰC TẾ PHŨ PHÀNG**

- **Nỗi sợ (The Hype):** Báo cáo của McKinsey dự báo AI có thể thay thế 400 triệu lao động (15% toàn cầu) vào năm 2030, trong đó ngành kế toán/kiểm toán chịu tác động nặng nề[cite: 43]. 
- **Thực tế phũ phàng (The Reality):** Nghiên cứu ban đầu của Wood et al. (2023) chỉ ra ChatGPT 3.5 thi trượt thảm hại, chỉ đạt khoảng 50% điểm bài tập kế toán so với mức 75% của sinh viên[cite: 43]. 
- **Vấn đề đặt ra:** Liệu các mô hình mới hơn (GPT-4) và kỹ thuật Prompt tốt hơn có lật ngược được thế cờ?[cite: 43]

---
# SLIDE 4
**PHƯƠNG PHÁP LUẬN: BÀI KIỂM TRA KHẮC NGHIỆT NHẤT**

Nhóm tác giả đã cho ChatGPT làm các câu hỏi trắc nghiệm từ 4 kỳ thi chứng chỉ danh giá nhất ngành[cite: 42, 51]:
1. **CPA (Kế toán công chứng):** Gồm 4 phần (AUD, BEC, FAR, REG)[cite: 51].
2. **CMA (Kế toán quản trị):** Gồm 2 phần[cite: 51].
3. **CIA (Kiểm toán nội bộ):** Gồm 3 phần[cite: 51].
4. **EA (Đại lý thuế):** Gồm 3 phần[cite: 51].
*Lưu ý:* Loại bỏ các câu hỏi có hình ảnh đồ thị và bài tập tự luận[cite: 51].

---
# SLIDE 5
**QUY TRÌNH THỰC CHỨNG 4 BƯỚC (CHAIN OF THOUGHT)**

Nghiên cứu đo lường năng lực AI qua 4 cấp độ Prompting[cite: 44]:
- **Bước 1 (Baseline):** Dùng ChatGPT 3.5 (Zero-shot) để đối chiếu với nghiên cứu cũ[cite: 44].
- **Bước 2 (Model Upgrade):** Dùng ChatGPT 4.0 (Zero-shot) để xem sức mạnh phần cứng[cite: 44].
- **Bước 3 (Few-shot Training):** Dạy GPT-4.0 bằng cách cung cấp 10 ví dụ (10-shot) trước khi hỏi[cite: 44].
- **Bước 4 (ReAct - Agent):** Kết hợp Suy luận (Reasoning) và Hành động (Acting) - Cấp công cụ cho AI[cite: 44].

---
# SLIDE 6
**BƯỚC 1: SỰ THẤT BẠI CỦA AI THẾ HỆ CŨ (GPT-3.5)**

- **Kết quả:** ChatGPT 3.5 **THI TRƯỢT 100%** các phần thi[cite: 42, 55].
- **Điểm số:** Điểm trung bình chỉ đạt 53.1%[cite: 42, 44]. 
- **Điểm yếu:** AI đặc biệt kém ở mảng Thuế cá nhân (EA - IND), chỉ đạt 37.3% (thấp hơn cả đoán mò)[cite: 55]. 
- **Nhận định:** Nếu chỉ dừng ở đây, AI hoàn toàn không có khả năng thay thế kế toán viên.

---
# SLIDE 7
**BƯỚC 2: CÚ NHẢY VỌT TỪ CÔNG NGHỆ LÕI (GPT-4)**

- **Thay đổi:** Nâng cấp thẳng lên mô hình ChatGPT 4 (tháng 3/2023)[cite: 43].
- **Kết quả:** Điểm trung bình tăng vọt thêm 16.5% (đạt 69.6%)[cite: 44, 55].
- **Thành tựu:** GPT-4 đã tự thi đỗ 5 phần thi, bao gồm **toàn bộ chứng chỉ Kiểm toán nội bộ (CIA)**[cite: 53, 55]. 
- Tuy nhiên, AI vẫn trượt các môn nặng về tính toán và chuẩn mực như Kế toán tài chính (FAR) và Thuế (EA)[cite: 55].

---
# SLIDE 8
**BƯỚC 3: SỨC MẠNH CỦA FEW-SHOT PROMPTING**

- **Thay đổi:** Áp dụng "10-Shot Training". Nhóm nghiên cứu đưa vào Prompt 10 câu hỏi mẫu kèm đáp án đúng để "khởi động" tư duy cho mô hình[cite: 44, 52].
- **Kết quả:** Điểm trung bình tăng thêm 6.6% (đạt 76.2%)[cite: 42, 56].
- **Thành tựu:** Nhờ học được từ ví dụ, AI đã thi đỗ thêm toàn bộ chứng chỉ **Kế toán quản trị (CMA)**[cite: 53, 56].

---
# SLIDE 9
**BƯỚC 4: GAME CHANGER - KIẾN TRÚC ReAct (AGENTS)**

- **Vấn đề cốt lõi:** LLMs là mô hình ngôn ngữ, nó "đoán chữ" chứ không biết "làm toán". Nó cộng trừ rất tệ[cite: 54].
- **Giải pháp ReAct (Reasoning + Acting):** 
  - Yêu cầu AI "suy nghĩ" các bước cần làm[cite: 66].
  - Cho phép AI dùng quyền **Web Search** (tìm luật/tỷ giá) và **Calculator** (máy tính bỏ túi để cộng trừ)[cite: 44, 52, 66].
- **Kết quả chấn động:** Điểm số tăng thêm 8.9%. Đạt trung bình **85.1%**[cite: 42, 57]. 

---
# SLIDE 10
**KẾT LUẬN VỀ NĂNG LỰC: AI ĐÃ "TỐT NGHIỆP"**

- Với kiến trúc ReAct, ChatGPT-4 **THI ĐỖ 100% CÁC CHỨNG CHỈ (CPA, CMA, CIA, EA)**[cite: 42, 57].
- Đáng chú ý: Năng lực giải quyết các câu hỏi "Vận dụng" (Application) tăng từ 62.3% (10-shot) lên 77.4% nhờ có Máy tính bỏ túi[cite: 58].
- **Trả lời câu hỏi nghiên cứu:** Không còn là "đồn thổi". ChatGPT thực sự có đủ năng lực chuyên môn để tạo ra sự phá bĩnh (disrupt) trong ngành kế toán/kiểm toán[cite: 42, 64].

---
# SLIDE 11
**TÁC ĐỘNG ĐẾN GIÁO DỤC KẾ TOÁN (EDUCATION)**

Nghiên cứu chỉ ra những thay đổi đang diễn ra ngay tại giảng đường:
- **Trợ giảng AI (TA-bots):** Một lớp học có bot AI giải đáp được 51,000 truy vấn sinh viên chỉ trong nửa học kỳ, tỷ lệ chính xác >95%, chi phí cực rẻ (200$/tháng)[cite: 59].
- **Chấm điểm & Phản hồi:** AI được thử nghiệm để tự động chấm điểm bài luận và giải đáp case study[cite: 59].
- **Sự chuyển dịch vai trò:** Giảng viên sẽ chuyển từ "người thuyết giảng" (sage-on-the-stage) sang "người hướng dẫn đồng hành" (guide-at-the-side)[cite: 61].

---
# SLIDE 12
**TÁC ĐỘNG ĐẾN THỰC TIỄN NGHỀ NGHIỆP (BUSINESS)**

Thực tế ứng dụng tại các tập đoàn lớn không thể chối cãi:
- **Big 4 hành động:** PwC đầu tư 1 tỷ USD, KPMG chi 2 tỷ USD, EY chi 1.5 tỷ USD vào các hệ thống AI nội bộ[cite: 43]. 
- **Ứng dụng cụ thể:** EY phát triển Chatbot tính lương (Intelligent Payroll Chatbot) để đọc hiểu phiếu lương và giảm >50% khối lượng công việc[cite: 62]. Bloomberg ra mắt BloombergGPT riêng cho dữ liệu tài chính[cite: 62].
- Theo khảo sát của KPMG, 65% công ty lớn đang ứng dụng AI vào báo cáo tài chính[cite: 62].

---
# SLIDE 13
**NHỮNG GIỚI HẠN CỦA AI VÀ CƠ HỘI CHO CON NGƯỜI**

Nghiên cứu này cũng thừa nhận giới hạn (Limitations) của AI:
1. **Chỉ "Biết" chứ chưa "Làm":** Việc AI đỗ bài thi trắc nghiệm không đồng nghĩa nó biết tự tay đóng sổ kế toán hay đối chiếu ngân hàng (Bank reconciliations) trên phần mềm ERP[cite: 65].
2. **Khả năng thị giác:** AI trong nghiên cứu chưa giải quyết được các câu hỏi chứa hình ảnh, sơ đồ phức tạp[cite: 51, 65].
3. **Ảo giác (Hallucination):** Dù dùng ReAct, AI vẫn có lúc giải thích sai (nhưng tỏ ra rất tự tin)[cite: 60].

---
# SLIDE 14
**TỔNG KẾT BÀI HỌC BUỔI 12**

- Sức mạnh của AI không nằm ở mô hình gốc (Zero-shot) mà nằm ở **Kỹ thuật viết Prompt (Few-shot) và Thiết kế luồng xử lý (Agents/ReAct)**.
- Kế toán viên tương lai không cần sợ mất việc, mà cần sợ việc **không biết cách giao việc cho AI**.
- Năng lực cốt lõi mới của nghề kế toán là: Phân tích nghiệp vụ, viết Prompt thiết lập tham số, và "kiểm toán" lại dữ liệu do AI tạo ra.

---
# SLIDE 15
**CÂU HỎI THẢO LUẬN & CASE STUDY CUỐI GIỜ**

*Từ nghiên cứu của Eulerich (2024), chúng ta thấy AI rất giỏi lý thuyết và lý luận, nhưng lại hay mắc lỗi toán học nếu không có công cụ bổ trợ.*

**Thảo luận (10 phút):**
Hãy tưởng tượng bạn đang phân tích báo cáo tỷ số tài chính (ROA, ROE) bằng ChatGPT bản miễn phí. Làm thế nào để bạn "đóng khung" (Prompt) yêu cầu để đảm bảo AI đưa ra nhận định đúng xu hướng mà không bị sai sót ở các phép chia số lớn? (Gợi ý: Hãy nghĩ đến phương pháp Chain of Thought).