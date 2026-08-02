# Kế hoạch Kịch bản Bài giảng: Day 12 - Thực hành AI Nhận thức và AI Tạo sinh trong Kế toán

**Tệp đầu vào:** `Slide_AIAcc_Day12.tex` & Textbook "Data and Analytics in the Accounting Profession".
**Hình thức:** Hội thoại giảng dạy Socratic (Người 1: Giảng viên, Người 2: Sinh viên).
**Mục tiêu:** Cung cấp tư duy chiến lược khi ứng dụng Generative AI (GenAI) vào kế toán. Hiểu cơ chế phân tích ngữ nghĩa, nhận diện ảo giác AI (Hallucination), tận dụng RAG/GPT Store và bảo mật bằng Human-in-the-Loop (HITL).

## Dàn ý Chi tiết (Mapping Slide & Textbook)

### Mở đầu & Sự dịch chuyển cốt lõi (Slide 1 - 7)
- **Ẩn dụ Kính chắn gió:** Kế toán truyền thống giống như lái xe 120km/h trên cao tốc nhưng bịt kính trước, chỉ dùng "gương chiếu hậu" (nhìn vào dữ liệu quá khứ).
- **GenAI là GPS định vị:** Gỡ kính chắn gió, nhìn xuyên thấu thời gian thực.
- Kế toán không còn là "thợ ghi chép" mà trở thành "cố vấn chiến lược". AI đã tiến hóa từ chỗ tính toán (cộng trừ) sang nhận thức (hiểu ngôn ngữ).

### Phần 1: Cơ chế khác biệt của AI & Machine Learning (Slide 8 - 15)
- **Case Study thuế đa quốc gia (Global Tech Enterprises):** 
- **Phần mềm cũ (Rule-based):** Dò tìm từ khóa (Keyword matching). Hóa đơn sai 1 chữ là báo lỗi hệ thống, gây ách tắc.
- **GenAI:** Mạng Neural thấu hiểu ngữ nghĩa sâu sắc. Không dò từ mà phân tích logic y hệt con người.
- **Dự báo dòng tiền (Predictive):** Báo động thiếu thanh khoản trước cả tháng.
- **Kỹ năng sinh tồn mới:** Kế toán trưởng không cần học Code (Python), nhưng phải có Hiểu biết dữ liệu (Data Literacy) và kỹ năng kể chuyện kinh doanh (Data Storytelling).

### Phần 2: Tư duy phản biện & Ảo giác AI - Hallucination (Slide 16 - 23)
- **Nghịch lý niềm tin:** Máy móc vốn được tin là khách quan tuyệt đối. Nhưng với LLMs, tin 100% là tự sát.
- **Bản chất LLM:** Dự đoán từ tiếp theo xác suất cao nhất.
- **Ảo giác AI:** Khi máy "bịa" ra luật, số liệu không có thật nhưng văn phong cực kỳ tự tin.
- **Ẩn dụ Cậu Analyst siêu phàm:** Làm việc nhạy bén nhưng mù bối cảnh thực tế (la làng khoản chi bất thường nhưng không biết đó là dự án sáp nhập đã chốt).
- **Phụ bếp và Bếp trưởng:** AI sơ chế dữ liệu, kế toán viên là bếp trưởng nếm thử và chịu trách nhiệm pháp lý cuối cùng.

### Phần 3: Kỷ nguyên Cá nhân hóa với Cửa hàng GPT (Slide 24 - 31)
- **Dân chủ hóa AI:** Bất cứ kế toán nào cũng tạo được AI riêng (Custom GPT) bằng cách chat mà không cần code.
- **App Store vs GPT Store:** GPT Store cung cấp "những bộ não chuyên gia" thay vì phần mềm vô tri.
- **Cơ chế RAG (Khắc tinh của ảo giác):** Ném sổ tay quy định nội bộ vào, ép AI phải giở tài liệu ra đọc rồi mới được trả lời.
- **Context Window khổng lồ:** Nhớ dai toàn bộ bối cảnh chuỗi tác vụ phức tạp.

### Phần 4: Bảo mật Dữ liệu & Quản trị Rủi ro (Slide 32 - 38)
- **Thảm họa rò rỉ:** Chat kế hoạch mật cho AI dùng chung -> Trở thành mồi huấn luyện -> Bị đối thủ dùng AI tra cứu ra ngay.
- **Giải pháp:** Phiên bản AI Enterprise (Bong bóng cô lập dữ liệu tuyệt đối). Chuẩn SOC 2.
- **Quy tắc Vàng HITL (Human-in-the-Loop):** Tuyệt đối không cho AI chốt lệnh chuyển tiền, con người kiểm duyệt cuối.

### Phần 5: Tương lai Kiểm toán Liên tục & Tổng kết (Slide 39 - 45)
- Không phải tương lai 10 năm sau mà là sinh tồn hiện tại. 
- AI giúp kiểm toán liên tục (Continuous Auditing) tới mốc 1/1000 giây sau giao dịch.
- **Hệ thống tự chữa lành:** Bóp nghẹt gian lận từ trứng nước.
- **Tổng kết:** 4 bài học lớn về GenAI, GPT Store, HITL và Kiểm toán liên tục.
