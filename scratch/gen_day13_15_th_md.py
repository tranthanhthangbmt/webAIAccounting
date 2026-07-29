import os

markdown_content = """---
theme: "default"
title: "Day 13-15 TH: Thực hành Dự án Cuối kỳ (No-Code)"
author: "Giảng viên"
date: "2026"
---

# BUỔI 13-15: THỰC HÀNH DỰ ÁN CUỐI KỲ (CAPSTONE PROJECT)

## Năng lực đạt được sau dự án
- **Làm chủ quy trình:** Tự tin áp dụng toàn bộ 6 bước của quy trình MOSAIC vào bài toán kế toán thực tế.
- **Kỹ năng No-code AI:** Thành thạo việc kết hợp các prompt (câu lệnh AI) để làm sạch dữ liệu, định khoản, và phân tích số liệu mà không cần viết mã lập trình.
- **Tư duy Giải quyết Vấn đề:** Khả năng phát hiện sai sót (anomalies) trong dữ liệu kế toán thô (raw data) và đưa ra các đề xuất quản trị.
- **Kỹ năng Trình bày:** Trực quan hóa dữ liệu (Data Visualization) thành Dashboard và thuyết trình mạch lạc trước hội đồng.

## Nội dung chương trình
1. Giới thiệu Đề bài Dự án & Phân nhóm.
2. Giai đoạn 1 (Buổi 13): Lên kế hoạch (MOS) & Khám phá dữ liệu.
3. Giai đoạn 2 (Buổi 14): Phân tích & Xử lý số liệu bằng AI (Analyze).
4. Giai đoạn 3 (Buổi 15): Vẽ Dashboard & Báo cáo (Interpret & Communicate).
5. Kỹ năng Thuyết trình & Bảo vệ Dự án.
6. Tổng kết khóa học.

---

# PHẦN 1: GIỚI THIỆU ĐỀ BÀI DỰ ÁN (CAPSTONE)

## 1.1 Kịch bản Kinh doanh (Business Case)
- Bạn được tuyển dụng làm Chuyên viên Phân tích Dữ liệu Kế toán cho Công ty Thương mại ABC.
- Giám đốc giao cho bạn một tập dữ liệu thô (Raw Dataset) gồm 5.000 dòng giao dịch trong năm qua.
- Dữ liệu bao gồm: Sổ nhật ký chung, Hóa đơn mua/bán hàng, Bảng lương.

## 1.2 Vấn đề của Công ty ABC
- Lợi nhuận quý 4/2025 giảm mạnh (giảm 25% so với cùng kỳ).
- Nghi ngờ có một số khoản chi phí bất thường hoặc bị ghi nhận sai (gian lận/nhầm lẫn).
- Giám đốc yêu cầu một báo cáo minh bạch và chi tiết trong vòng 3 ngày làm việc (tương đương 3 buổi học).

## 1.3 Yêu cầu Đầu ra (Deliverables)
1. Một file Excel đã làm sạch và chuẩn hóa.
2. Bảng định khoản tự động bằng AI (có log kiểm chứng).
3. Một Dashboard động trên Excel (hoặc Power BI) thể hiện tình hình kinh doanh.
4. Một bản báo cáo quản trị (Executive Summary) dài 1 trang (A4) do AI hỗ trợ soạn thảo.
5. Một bài thuyết trình (Pitch) 10 phút trước hội đồng.

## 1.4 Quy định & Nguyên tắc (No-Code)
- **Công cụ cho phép:** Excel (Power Query, Pivot Table), ChatGPT (Advanced Data Analysis), Copilot, Claude.
- **Không yêu cầu:** Lập trình Python, R, hoặc SQL.
- **Bắt buộc:** Áp dụng khung tư duy SPARKS để phản biện kết quả của AI (Không tin mù quáng vào AI).

## 1.5 Lập nhóm và Phân vai
- Nhóm 3-4 thành viên. Phân vai:
  - **Trưởng nhóm (Project Manager):** Quản lý tiến độ, điều phối công việc.
  - **Chuyên gia AI Prompting:** Phụ trách giao tiếp với ChatGPT/Copilot.
  - **Chuyên viên Dữ liệu (Data Analyst):** Xử lý Power Query và vẽ biểu đồ.
  - **Chuyên viên Báo cáo:** Tổng hợp Interpret và chuẩn bị slide/thuyết trình.

---

# PHẦN 2: BUỔI 13 - LẬP KẾ HOẠCH & KHÁM PHÁ (MOS)

## 2.1 Bước M - Motivation (Động lực)
- Họp nhóm 15 phút đầu tiên: Xác định rõ vấn đề kinh doanh.
- Tại sao Ban Giám đốc lại lo lắng về Quý 4?
- Sử dụng SPARKS (Chữ S & P): Ai là người đọc báo cáo này? Mục đích cốt lõi là gì?

## 2.2 Bước O - Objective (Mục tiêu)
- Viết ra 3 Câu hỏi Phân tích Dữ liệu (Data Questions).
- Câu 1: (Descriptive) Xu hướng doanh thu và chi phí 12 tháng qua là gì?
- Câu 2: (Diagnostic) Khoản mục chi phí nào tăng đột biến nhất trong Q4?
- Câu 3: (Diagnostic) Có giao dịch nào vi phạm nguyên tắc kiểm soát nội bộ không?

## 2.3 Trợ lý AI - Tạo dàn ý phân tích
- **Thực hành Prompting:** Cùng AI lập chiến lược.
- "Đóng vai Chuyên gia Phân tích Tài chính. Tôi cần tìm nguyên nhân giảm lợi nhuận Q4 từ file Sổ cái 5000 dòng. Dựa trên 3 câu hỏi mục tiêu [Paste 3 câu ở trên], hãy gợi ý cho tôi các bước thao tác cụ thể trên Excel (Pivot, Chart)."

## 2.4 Bước S - Strategy (Chiến lược Dữ liệu)
- Tải file `ABC_Raw_Data_2025.xlsx` từ hệ thống lớp học.
- Đánh giá chất lượng dữ liệu: File có bao nhiêu cột? (Ví dụ: Ngày, Số chứng từ, Diễn giải, Tài khoản Nợ/Có, Số tiền).
- Lên danh sách các "căn bệnh" của dữ liệu: Lỗi font, ngày tháng sai chuẩn, ô bị bỏ trống.

## 2.5 Thực hành: Khám phá Dữ liệu Cơ bản
- Mở file Excel. Sử dụng Data Filter.
- Đếm số dòng trống (Blanks).
- Tính tổng (SUM) cột Số tiền để ghi nhận "Control Total" (Tổng đối chiếu) trước khi làm sạch.
- **Mẹo:** Nếu Control Total bị thay đổi sau khi làm sạch, bạn đã làm mất dữ liệu!

---

# PHẦN 3: BUỔI 14 - PHÂN TÍCH & XỬ LÝ SỐ LIỆU (ANALYZE)

## 3.1 Bước A - Làm sạch Dữ liệu (Data Cleaning)
- Khởi động Power Query Editor trong Excel.
- Loại bỏ các ký tự thừa (Trim), chuẩn hóa kiểu dữ liệu (Change Type) cho cột Ngày tháng và Số tiền.
- Thay thế lỗi (Replace Errors) bằng số 0 hoặc "N/A".

## 3.2 Khắc phục lỗi bằng AI
- Nếu gặp một chuỗi ký tự lạ (Ví dụ: "HĐ001-INV-2025"), cần tách số hóa đơn.
- **Prompt:** "Tôi có cột dữ liệu chứa chuỗi 'HĐ001-INV-2025' trong Excel. Tôi chỉ muốn lấy chữ '001'. Hãy cho tôi công thức Excel ngắn nhất để làm việc này."

## 3.3 Tự động Định khoản bằng AI
- Giả định file có 50 nghiệp vụ phát sinh mới chỉ có mô tả bằng chữ (Ví dụ: "Mua máy chiếu phòng họp").
- **Prompt:** "Đóng vai Kế toán trưởng (Thông tư 200). Định khoản Nợ/Có cho các nghiệp vụ sau và xuất kết quả dạng bảng: 1. Mua máy chiếu..., 2. Chi tiền mặt tiếp khách..."
- Dán (Paste) kết quả vào file Excel.

## 3.4 Phân tích Tìm kiếm Điểm bất thường (Outliers)
- Nhiệm vụ: Tìm ra các khoản chi sai quy định.
- Sử dụng tính năng "Analyze Data" (Tích hợp AI) trên Excel 365, hoặc upload file lên ChatGPT.
- **Prompt:** "Sử dụng thuật toán tìm kiếm điểm bất thường (Outlier Detection), hãy chỉ ra top 5 giao dịch có số tiền chi ra vượt quá 3 độ lệch chuẩn (Standard Deviations) so với trung bình tháng."

## 3.5 Phân tích Xu hướng (Trend Analysis)
- Tạo Pivot Table tổng hợp Doanh thu và Chi phí theo Tháng.
- Chèn (Insert) Line Chart.
- Quan sát tháng 10, 11, 12: Đường chi phí có vượt đường doanh thu không?
- Lập bảng Top 3 bộ phận tiêu tốn nhiều chi phí nhất Quý 4.

## 3.6 Đánh giá lại với SPARKS (Chữ R - Risks)
- Kiểm tra lại các kết luận của AI: Số liệu AI đưa ra có khớp với Pivot Table bạn tự làm không?
- Cảnh giác với "Ảo giác AI" (Hallucinations) khi phân tích số liệu tài chính lớn.

---

# PHẦN 4: BUỔI 15 - VẼ DASHBOARD & BÁO CÁO (INTERPRET & COMMUNICATE)

## 4.1 Bước I - Diễn giải Kết quả (Interpret)
- Thảo luận nhóm: Từ biểu đồ xu hướng và danh sách điểm bất thường, kết luận cuối cùng là gì?
- (Ví dụ: Lợi nhuận giảm do Bộ phận Marketing chi quá ngân sách 40% vào tháng 11, cộng thêm 2 khoản chi tiếp khách bị ghi trùng).
- Chuyển "Con số" thành "Nguyên nhân kinh doanh".

## 4.2 Bước C - Xây dựng Dashboard (Trực quan hóa)
- Tạo một Sheet mới đặt tên là "Dashboard".
- Tập hợp các Pivot Charts đã làm ở Buổi 14 về đây.
- Yêu cầu bắt buộc:
  - 1 Slicer lọc theo Quý/Tháng.
  - 1 Slicer lọc theo Phòng ban.
  - Biểu đồ so sánh Doanh thu - Chi phí.
  - Các KPI Cards (Tổng DT, Tổng CP, Lợi Nhuận).

## 4.3 Sử dụng AI viết Báo cáo Quản trị
- Ban Giám đốc không có thời gian xem toàn bộ file Excel.
- Hãy dùng ChatGPT soạn một Executive Summary.
- **Prompt:** "Đóng vai Giám đốc Tài chính. Dựa trên số liệu: Doanh thu Q4 giảm 10%, Chi phí Marketing tăng 40%, phát hiện 2 khoản chi trùng. Hãy viết một email báo cáo dài 300 chữ gửi CEO, nhấn mạnh vào rủi ro và đề xuất siết chặt kiểm soát."

## 4.4 Kỹ thuật "Kể chuyện bằng Dữ liệu"
- Khi thuyết trình, không đọc các con số vô hồn.
- Bắt đầu bằng bối cảnh (Context) -> Trình bày cao trào (Vấn đề Q4) -> Đưa ra giải pháp (Dựa trên dữ liệu).
- Sử dụng ngữ điệu tự tin, mắt hướng về Ban Giám đốc.

## 4.5 Thuyết trình (Presentation)
- Mỗi nhóm có 10 phút trình bày, 5 phút Q&A.
- Giảng viên (Đóng vai CEO) sẽ đặt các câu hỏi phản biện gắt gao (Ví dụ: "Làm sao em biết AI định khoản khoản này là đúng?").
- Điểm đánh giá: 40% kỹ thuật dữ liệu, 30% tư duy diễn giải (SPARKS), 30% kỹ năng thuyết trình.

---

# TỔNG KẾT KHÓA HỌC

## 5.1 Lời ngỏ từ Giảng viên
- Chúc mừng các bạn đã đi đến cuối hành trình "Trí tuệ nhân tạo cho Kế toán"!
- Qua 15 buổi, các bạn đã vượt qua vùng an toàn của một kế toán viên truyền thống.
- Các bạn không chỉ biết hạch toán, mà còn biết dùng AI để kiểm soát, phân tích và quản trị dữ liệu.

## 5.2 Thông điệp cốt lõi
- "AI sẽ không thay thế kế toán viên. Kế toán viên biết sử dụng AI sẽ thay thế kế toán viên không biết dùng AI."
- Kỹ năng No-code (Power Query, Prompting) là vũ khí lợi hại nhất của bạn trong 5 năm tới.

## 5.3 Định hướng tương lai
- Hãy tự xây dựng một "Thư viện Prompt" (Prompt Library) cho riêng mình.
- Tiếp tục theo dõi các bản cập nhật của ChatGPT, Copilot trong hệ sinh thái Tài chính.
- Khóa học kết thúc, nhưng hành trình chuyển đổi số của bạn chỉ mới bắt đầu!

## CHÚC CÁC BẠN THÀNH CÔNG RỰC RỠ!
- Cảm ơn các bạn đã đồng hành.
- Hẹn gặp lại ở những cột mốc vinh quang trong sự nghiệp!
"""

output_path = "TaiLieu/slideAIAcc_v2/slideAIAcc_v2_Day13-15_TH.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(f"Successfully generated {output_path}")
