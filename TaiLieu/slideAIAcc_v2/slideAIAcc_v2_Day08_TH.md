# KẾ HOẠCH SLIDE THỰC HÀNH - DAY 08 (BUỔI 8)
**Tên bài:** Buổi 8 TH: Phân tích Xu hướng và Dự báo Ngân sách với AI

### Mở đầu
## Title: Buổi 8 TH: Phân tích Xu hướng và Dự báo Ngân sách với AI.
    - Thực hành: Ứng dụng AI trong Kế toán Quản trị
    - Giảng viên: Đại học Đông Á
    - Môn học: Trí tuệ Nhân tạo cho Kế toán
## Năng lực đạt được sau buổi học.
    - **Về Kiến thức:** Nắm vững quy trình thiết lập bài toán dự báo trong Kế toán Quản trị, hiểu cách AI phân tích các chuỗi thời gian (time-series) từ dữ liệu doanh thu quá khứ.
    - **Về Kỹ năng:** Thành thạo việc thiết kế Prompt yêu cầu AI (ChatGPT) phân tích xu hướng (Trend Analysis), dự báo dòng tiền/doanh thu cho quý tiếp theo và lập các kịch bản Tốt/Xấu/Cơ sở.
    - **Về Tư duy:** Đánh giá tính khả thi và độ tin cậy của các con số dự báo do máy sinh ra. Ra quyết định kinh doanh dựa trên sự kết hợp giữa dữ liệu lịch sử và phán đoán chuyên gia.
## Nội dung chương trình (Agenda).
    - 1. Chuẩn bị Dữ liệu Doanh thu và Dòng tiền.
    - 2. Phân tích Xu hướng (Trend Analysis) với AI.
    - 3. Thực hành Dự báo Doanh thu cho Quý tiếp theo.
    - 4. Xây dựng Kịch bản Đa chiều (Scenario Planning).
    - 5. Trực quan hóa Báo cáo Quản trị.

### Phần 1: Chuẩn bị Dữ liệu Doanh thu và Dòng tiền
## Tổng quan Bài tập Thực hành.
    - Tình huống: Bạn là Kế toán Quản trị của Công ty ABC. Giám đốc yêu cầu bạn lập bản kế hoạch lợi nhuận cho Quý 1 năm tới.
    - Nhiệm vụ: Phân tích dữ liệu doanh thu và dòng tiền của 12 tháng qua để đưa ra dự báo.
## Nguồn dữ liệu (Dataset).
    - Giảng viên cung cấp: File Excel `Sales_CashFlow_12Months.csv`.
    - Các trường dữ liệu: Tháng, Dòng sản phẩm, Khối lượng bán, Giá bán, Chi phí biến đổi, Chi phí cố định, Dòng tiền thuần.
## Làm sạch và chuẩn hóa dữ liệu.
    - Mở file bằng Excel, kiểm tra xem có dòng dữ liệu nào trống (Missing values) hoặc bất thường không.
    - Định dạng cột Tháng thành dạng "Date", cột Số tiền thành dạng "Currency".
## Tải dữ liệu lên môi trường AI.
    - Sử dụng ChatGPT Plus (Advanced Data Analysis) hoặc Claude.
    - Click vào biểu tượng đính kèm (Attachment) để tải file CSV lên khung chat.
## Prompt cơ bản: Yêu cầu AI "Đọc hiểu" dữ liệu.
    - **Prompt:** "Tôi vừa tải lên file dữ liệu doanh thu và dòng tiền 12 tháng qua của công ty. Hãy đọc file, tóm tắt cấu trúc các cột và cho tôi biết tổng doanh thu của 12 tháng là bao nhiêu."
## Xác nhận tính chính xác (Data Validation).
    - So sánh tổng doanh thu AI vừa báo cáo với tổng hàm SUM trong Excel của bạn.
    - Đảm bảo AI đã hiểu đúng bối cảnh số liệu trước khi bắt đầu phân tích sâu hơn.

### Phần 2: Phân tích Xu hướng (Trend Analysis) với AI
## Tầm quan trọng của Phân tích Xu hướng.
    - Trước khi dự báo tương lai, ta phải hiểu quá khứ.
    - Nhận diện tính thời vụ (Seasonality): Các tháng nào doanh thu tăng đột biến?
## Thiết kế Prompt Phân tích Xu hướng.
    - **Prompt:** "Dựa trên dữ liệu 12 tháng qua, hãy phân tích xu hướng tăng/giảm doanh thu của từng dòng sản phẩm. Có yếu tố thời vụ nào được thể hiện không?"
## Khai thác Insight từ AI.
    - Yêu cầu AI chỉ ra nguyên nhân (Correlation) thay vì chỉ nêu con số.
    - Ví dụ: Tại sao Dòng tiền thuần tháng 8 lại âm dù doanh thu tăng? (Do tăng chi phí mua nguyên vật liệu dự trữ).
## Sử dụng AI để tính toán các Chỉ số biến động.
    - Yêu cầu AI tính Tốc độ tăng trưởng hàng tháng (MoM - Month over Month).
    - AI có thể tự động viết mã Python để xuất ra bảng tính MoM ngay trong khung chat.
## Kiểm chứng bằng Biểu đồ cơ bản.
    - Yêu cầu AI vẽ biểu đồ đường (Line chart) thể hiện sự thay đổi của Doanh thu và Chi phí trong 12 tháng.
## Đánh giá biểu đồ do AI sinh ra.
    - Biểu đồ có dễ hiểu không? Trục Y có bắt đầu từ 0 không?
    - Lưu biểu đồ này lại để đưa vào báo cáo quản trị cuối cùng.
## Nhận xét Phê phán.
    - Suy ngẫm: AI có nhận ra được các sự kiện bất thường (ví dụ: tháng 4 có chương trình khuyến mãi lớn) từ dữ liệu trống không?
    - Trả lời: Không, nếu bạn không cung cấp Context. $\Rightarrow$ Kế toán viên phải cung cấp Bối cảnh!

### Phần 3: Thực hành Dự báo Doanh thu (Forecasting)
## Từ Phân tích đến Dự báo.
    - Bước tiếp theo: Sử dụng dữ liệu quá khứ để ước tính doanh thu và dòng tiền cho 3 tháng tiếp theo (Quý 1 năm sau).
## Lựa chọn phương pháp Dự báo.
    - Trong ChatGPT, ta có thể yêu cầu AI sử dụng phương pháp Cân bằng động (Moving Average) hoặc Hồi quy tuyến tính (Linear Regression).
## Thiết kế Prompt Dự báo Cơ bản.
    - **Prompt:** "Hãy đóng vai Chuyên gia Kế toán Quản trị. Dựa vào xu hướng 12 tháng qua, hãy dự báo Doanh thu và Dòng tiền thuần cho 3 tháng tới. Trình bày dưới dạng bảng."
## Kỹ thuật Prompt nâng cao cho Dự báo.
    - Thêm các giả định (Assumptions) vào Prompt.
    - **Prompt:** "...Giả định rằng: Chi phí biến đổi sẽ tăng 5 phần trăm do lạm phát, và giá bán không thay đổi. Hãy tính lại dự báo lợi nhuận."
## Yêu cầu giải thích thuật toán.
    - Để tránh tình trạng "Hộp đen" (Black box), hãy hỏi AI: "Bạn đã sử dụng công thức hoặc phương pháp thống kê nào để tính ra con số của 3 tháng tới?"
## Kiểm tra tính hợp lý (Sanity Check).
    - Nếu AI dự báo doanh thu tháng 1 năm sau tăng vọt 200 phần trăm, bạn phải đặt câu hỏi "Tại sao?".
    - AI có thể nội suy sai do không hiểu tính chu kỳ hàng năm.
## Rolling Forecast (Dự báo Cuốn chiếu).
    - Thảo luận cách sử dụng template Prompt này để cập nhật dự báo mỗi tháng khi có dữ liệu mới.

### Phần 4: Xây dựng Kịch bản Đa chiều (Scenario Planning)
## Tại sao cần lập nhiều kịch bản?
    - Tương lai là bất định. Một bản kế hoạch tĩnh là không đủ.
    - Cần chuẩn bị cho các tình huống xấu nhất (Thiên nga đen) và tốt nhất.
## Khởi tạo 3 Kịch bản (3 Scenarios).
    - Kịch bản Cơ sở (Base Case): Giữ đà tăng trưởng như dự báo hiện tại.
    - Kịch bản Lạc quan (Best Case): Kinh tế phục hồi mạnh mẽ.
    - Kịch bản Bi quan (Worst Case): Chuỗi cung ứng đứt gãy.
## Thiết kế Prompt Mô phỏng Kịch bản.
    - **Prompt:** "Dựa trên bản dự báo vừa lập, hãy tạo thêm 2 kịch bản. Kịch bản Lạc quan: Sản lượng bán tăng 15 phần trăm. Kịch bản Bi quan: Khách hàng chậm trả tiền làm Dòng tiền vào giảm 20 phần trăm."
## Phân tích Độ nhạy (Sensitivity Analysis).
    - Xem xét tác động của từng biến số. Nếu giá nguyên vật liệu tăng 1 phần trăm, lợi nhuận ròng giảm bao nhiêu phần trăm?
    - AI làm rất tốt việc tính toán Độ nhạy này trong nháy mắt.
## Đề xuất Chiến lược Ứng phó (Mitigation Strategy).
    - Bước tạo ra giá trị cao nhất của Kế toán quản trị.
    - **Prompt:** "Với kịch bản Bi quan (dòng tiền âm vào tháng 2), hãy đề xuất 3 giải pháp tài chính để công ty không bị thiếu hụt thanh khoản."
## Đánh giá các lời khuyên từ AI.
    - Các đề xuất (như: Đàm phán kéo dài thời gian trả nợ, Bán nợ) có phù hợp với thực tế công ty không?
## Lưu trữ và cập nhật Kịch bản.
    - Hướng dẫn sinh viên cách lưu các Kịch bản này thành các Sheet riêng biệt trên Excel sau khi copy từ AI.

### Phần 5: Tổng kết và Trình bày Báo cáo Quản trị
## Đóng gói Báo cáo (Packaging the Report).
    - Kế toán không gửi những dòng chat thô của AI cho Ban giám đốc.
    - Cần tổng hợp: Bảng số liệu, Biểu đồ dự báo, và Đoạn tóm tắt (Executive Summary).
## Yêu cầu AI viết Executive Summary.
    - **Prompt:** "Dựa vào tất cả các phân tích và 3 kịch bản trên, hãy viết một bản Tóm tắt Quản trị (Executive Summary) dài 200 chữ để tôi trình bày trước Ban Giám đốc."
## Trình bày kết quả (Communicate Results).
    - Sử dụng kỹ thuật Data Storytelling (đã học ở buổi trước) để dẫn dắt câu chuyện từ Dữ liệu quá khứ -> Dự báo tương lai -> Đề xuất chiến lược.
## Bài học kinh nghiệm (Lessons Learned).
    - AI giải phóng kế toán khỏi việc lập công thức Excel phức tạp.
    - Khả năng tư duy chiến lược và đặt câu hỏi đúng (Prompting) quyết định chất lượng của bản ngân sách.
## Bài tập về nhà & Q&A.
    - Bài tập: Sinh viên tự điều chỉnh các giả định (lạm phát 10 phần trăm) và nộp lại báo cáo kịch bản bi quan.
    - Hỏi và Đáp cuối giờ.
