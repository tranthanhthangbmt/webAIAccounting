# Kế hoạch Kịch bản Bài giảng: Day 13 - Kỹ thuật Viết Prompt, Khung SPARKS & Phân tích Dữ liệu

**Tệp đầu vào:** `Slide_AIAcc_Day13.tex` & Textbook "Data and Analytics in the Accounting Profession".
**Hình thức:** Hội thoại giảng dạy Socratic (Người 1: Giảng viên, Người 2: Sinh viên).
**Mục tiêu:** Cung cấp tư duy và công cụ phân tích từ 4 trụ cột, nghệ thuật viết lệnh Prompt chuẩn xác cho LLMs, ứng dụng khung quy trình SPARKS, và cảnh giác trước bãi mìn đạo đức của AI.

## Dàn ý Chi tiết (Mapping Slide & Textbook)

### Mở đầu & Sự dịch chuyển vĩ đại (Slide 1 - 6)
- **Sự chuyển đổi:** Kế toán chuyển từ dọn dẹp quá khứ sang kiến tạo tương lai.
- **Kính viễn vọng tiên đoán:** Khái niệm của Wayne R. Landsman, AI biến việc phân tích từ "gương chiếu hậu" thành "kính viễn vọng" nhìn trước rủi ro.

### Phần 1: Chiến lược Dữ liệu & 4 Trụ cột Phân tích (Slide 7 - 13)
- **Rác đầu vào = Rác đầu ra (GIGO):** Công cụ mạnh đến đâu cũng chết nếu dữ liệu dơ.
- **Ẩn dụ Sân vận động:**
  - **Mô tả (Descriptive):** Nhìn bảng tỷ số (Biết chuyện gì xảy ra: Doanh thu).
  - **Chẩn đoán (Diagnostic):** Xem lại băng ghi hình quay chậm (Tại sao lợi nhuận rớt: Do chi phí máy móc).
  - **Dự báo (Predictive):** Mô hình toán học đoán tỷ số tương lai (Nếu tăng 10% sản lượng).
  - **Đề xuất (Prescriptive):** Đỉnh cao tối ưu hóa (Nên xếp đội hình, sản xuất bao nhiêu xe để tối đa biên lợi nhuận).

### Phần 2: Kỹ năng Sinh tồn: Kỹ thuật Viết Prompt (Slide 14 - 22)
- **Prompt Engineering:** Nghệ thuật giao tiếp với AI. Không nhập bối cảnh = nhận kết quả rác.
- **3 Nguyên tắc Vàng:**
  - Role-based (Gán vai chuyên gia).
  - Context & Clarity (Cung cấp bối cảnh, định dạng bảng).
  - Chain-of-Thought (Ép AI suy nghĩ từng bước để chống lỗi sai logic).
- **Thực chiến:** Báo cáo tài chính & Thuế.
- **3 Sai lầm chết người:** Hỏi chung chung, Tin AI làm toán giỏi (rất hay sai cộng trừ), Rò rỉ dữ liệu nhạy cảm (GDPR).

### Phần 3: Khởi động Dự án với Khung Tư duy SPARKS (Slide 23 - 29)
- **SPARKS:** Quy trình chuẩn cho kế toán.
  - **S (State):** Hỏi đúng trọng tâm kinh doanh (Đừng cắm đầu vào dữ liệu ngay).
  - **P (Partition):** Trích xuất đúng vùng dữ liệu (Lọc).
  - **A (Analyze):** Phân tích 1 trong 4 trụ cột.
  - **R (Refine):** Tinh chỉnh (Cảnh giác với Outliers, ví dụ lỗi dư số 0).
  - **K (Communicate):** Truyền đạt (Vẽ Dashboard).
  - **S (Stop):** Suy ngẫm chốt lại vấn đề.
- **Thực hành Accounts Payable:** Tìm hóa đơn bất thường qua Scatter Plot. Chấm điểm nhà cung cấp (Cẩn thận số lượng đơn hàng quá ít làm bóp méo trung bình).

### Phần 4: Bãi mìn Rủi ro: Hộp đen & Đạo đức AI (Slide 30 - 43)
- **Động cơ vs Bãi mìn:** AI siêu tốc nhưng đầy rủi ro.
- **Rủi ro Bảo mật:** Bài học vụ Equifax (2017). Giải pháp Pháo đài dữ liệu.
- **Rủi ro Hộp đen (Black Box):** Giao dịch cao tần (HFT) ra quyết định vô hình gây sụp đổ thị trường.
- **Đạo đức AI (Bias):** Sự tàn nhẫn của thuật toán (Tối ưu lợi nhuận = Đổ tiền vào công ty vũ khí/ô nhiễm, đi ngược ESG).
- **Trách nhiệm của con người:** AI không có lỗi, người lập trình "hàm mục tiêu" mới có lỗi.
- **Chiếc phanh khẩn cấp:** Kế toán viên là người nắm chiếc phanh cuối cùng.
- **Đặc quyền con người:** Không phải cộng trừ nhân chia, mà là "Trực giác đạo đức" và "Thấu cảm triết học". Kế toán viên là Đối tác Chiến lược!
