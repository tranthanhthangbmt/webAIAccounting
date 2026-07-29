# KẾ HOẠCH SLIDE THỰC HÀNH - DAY 07 (BUỔI 7)
**Tên bài:** Buổi 7 TH: Ứng dụng AI Hỗ trợ Lập Báo cáo và Dashboard

### Mở đầu
## Title: Buổi 7 TH: Ứng dụng AI Hỗ trợ Lập Báo cáo và Dashboard.
    - Thực hành: Xây dựng Thuyết minh BCTC & Interactive Performance Dashboard
    - Giảng viên: Đại học Đông Á
    - Môn học: Trí tuệ Nhân tạo cho Kế toán
## Năng lực đạt được sau buổi học.
    - **Về Kiến thức:** Nắm vững quy trình thiết kế Dashboard hiệu suất tương tác (Interactive Performance Dashboard) từ dữ liệu kế toán thô.
    - **Về Kỹ năng:** Sử dụng AI (ChatGPT/Claude) để tự động sinh dàn ý Thuyết minh BCTC; sử dụng Excel/PowerBI để làm sạch dữ liệu, tạo Pivot Table, Pivot Chart và ghép thành Dashboard hoàn chỉnh.
    - **Về Tư duy:** Rèn luyện khả năng "Data Storytelling" (Kể chuyện bằng dữ liệu) để trình bày thông tin tài chính một cách trực quan, dễ hiểu và dễ ra quyết định cho Ban giám đốc.
## Nội dung chương trình (Agenda).
    - 1. Dùng AI phác thảo Thuyết minh Báo cáo Tài chính.
    - 2. Giới thiệu bộ dữ liệu (Dataset) và mục tiêu thiết kế Dashboard.
    - 3. Làm sạch dữ liệu và tạo bảng tóm tắt (Pivot Tables).
    - 4. Xây dựng các biểu đồ tương tác (Pivot Charts).
    - 5. Hoàn thiện Interactive Performance Dashboard.
    - 6. Đánh giá và tích hợp AI Insights.

### Phần 1: Dùng AI phác thảo Thuyết minh Báo cáo Tài chính
## Tổng quan bài tập Thuyết minh BCTC.
    - Bối cảnh: Công ty giả định vừa khóa sổ kế toán, Ban giám đốc cần bản Thuyết minh BCTC nhanh.
    - Dữ liệu cung cấp: Bảng Cân đối kế toán và Báo cáo Kết quả Kinh doanh rút gọn (File Excel).
## Thiết lập Prompt cho AI.
    - Prompt đóng vai: "Bạn là một Kế toán trưởng dày dạn kinh nghiệm..."
    - Mục tiêu Prompt: Yêu cầu AI đọc số liệu và sinh ra Dàn ý (Outline) cho Thuyết minh BCTC chuẩn VAS.
## Thực thi và đánh giá kết quả từ AI.
    - Copy & Paste dữ liệu hoặc Upload file Excel lên công cụ AI.
    - Phân tích dàn ý do AI cung cấp (Đủ các phần: Đặc điểm hoạt động, Chính sách kế toán, Giải trình chi tiết chưa?).
## Yêu cầu AI phân tích biến động (Fluctuation Analysis).
    - Prompt tiếp theo: "Hãy phân tích và viết một đoạn giải trình về sự biến động của Doanh thu thuần và Giá vốn hàng bán năm nay so với năm trước."
## Tinh chỉnh giọng văn (Tone of Voice).
    - Kỹ thuật: Yêu cầu AI viết lại đoạn giải trình với văn phong trung lập, khách quan và chuyên nghiệp.
    - "Hãy sử dụng ngôn ngữ tài chính, tránh dùng các từ cảm xúc như 'tuyệt vời', 'tồi tệ'."
## Double-check (Kiểm chứng chéo).
    - Sinh viên tự tính toán lại tỷ lệ phần trăm thay đổi của Doanh thu để so sánh với số liệu AI tự tính.
    - Tìm và chỉ ra lỗi "Ảo giác" (nếu có) của AI.

### Phần 2: Giới thiệu bộ dữ liệu và mục tiêu Dashboard
## Chuyển sang phần Báo cáo Quản trị (Dashboards).
    - Tại sao lại cần Dashboard? Để Ban Giám đốc nhìn nhận "Sức khỏe Doanh nghiệp" một cách trực quan nhất.
## Giới thiệu Bộ dữ liệu (Dataset).
    - Dữ liệu bán hàng và chi phí của công ty qua các năm, chi tiết tới từng tháng, từng dòng sản phẩm và từng khu vực.
    - Số lượng: Khoảng 2,000 dòng dữ liệu thô.
## Mục tiêu thiết kế Dashboard (Objective).
    - Thể hiện được Tổng doanh thu (Gross Sales).
    - Tỷ suất Lợi nhuận gộp (Profit Margin) theo từng Dòng sản phẩm (Brand).
    - Phân tích cấu trúc Chi phí (Cost Analysis).
## Lên ý tưởng (Wireframing).
    - Vẽ phác thảo cấu trúc Dashboard trên giấy hoặc bảng trắng.
    - Vị trí đặt biểu đồ: Biểu đồ quan trọng nhất đặt ở góc trên cùng bên trái.
## Bố cục màn hình (Screen Layout).
    - Chia màn hình Dashboard thành các phần: Tiêu đề, Vùng Bộ lọc (Filters), Vùng Biểu đồ chính, Vùng Biểu đồ phụ.

### Phần 3: Làm sạch dữ liệu và tạo bảng tóm tắt (Pivot Tables)
## Kiểm tra và làm sạch dữ liệu thô.
    - Xóa bỏ các dòng trống (Blank Rows).
    - Xử lý các giá trị lỗi (N/A, VALUE) và định dạng chuẩn (Currency, Date).
## Sử dụng AI để tìm lỗi dữ liệu.
    - Prompt: "Hãy kiểm tra xem cột 'Gross Sales' có chứa giá trị text nào không, hoặc có số âm bất thường không."
## Tạo Pivot Table 1: Doanh thu theo Dòng sản phẩm.
    - Insert > PivotTable.
    - Kéo 'Brand' vào Rows, 'Gross Sales' vào Values.
## Tạo Pivot Table 2: Tỷ suất lợi nhuận.
    - Tạo Calculated Field trong PivotTable (Profit = Gross Sales - Variable Costs).
    - Tính Profit Margin = Profit / Gross Sales.
## Tạo Pivot Table 3: Phân tích chi phí.
    - Kéo 'Labor' và 'Materials' vào để xem cấu trúc chi phí (Variable Costs).

### Phần 4: Xây dựng các biểu đồ tương tác (Pivot Charts)
## Vẽ biểu đồ Doanh thu (Gross Sales).
    - Chọn Pivot Table 1 -> Insert PivotChart -> Bar Chart.
    - Áp dụng nguyên tắc Gestalt: Sắp xếp các cột theo thứ tự giảm dần (Sort Z to A).
## Vẽ biểu đồ Tỷ suất Lợi nhuận (Profit Margin).
    - Chọn Pivot Table 2 -> Insert PivotChart -> Column Chart hoặc Line Chart.
    - Thêm một đường trung bình (Average Line) làm chuẩn (Benchmark).
## Vẽ biểu đồ Cấu trúc chi phí (Cost Analysis).
    - Chọn Pivot Table 3 -> Insert PivotChart -> Stacked Bar Chart.
    - Thể hiện sự đóng góp của chi phí nguyên vật liệu và nhân công vào tổng chi phí.
## Làm sạch biểu đồ (Decluttering).
    - Xóa bỏ các đường lưới (Gridlines) mờ nhat.
    - Ẩn các nút Field Buttons không cần thiết trên biểu đồ.
## Tối ưu hóa Tiêu đề và Nhãn dữ liệu (Labels).
    - Đổi tên biểu đồ thành các thông điệp có ý nghĩa (VD: "Sản phẩm A đang dẫn đầu Doanh thu").
    - Thêm Data Labels trực tiếp lên các cột thay vì dùng trục Y quá dày đặc.
## Ứng dụng màu sắc (Color Application).
    - Dùng nguyên tắc Tiền chú ý (Preattentive attributes).
    - Tô màu Đỏ cho sản phẩm có Tỷ suất lợi nhuận âm, màu Xanh/Xám cho các sản phẩm còn lại.

### Phần 5: Hoàn thiện Interactive Performance Dashboard
## Khởi tạo Trang tính Dashboard (Dashboard Sheet).
    - Mở một Sheet mới, tắt Gridlines (View > Bỏ chọn Gridlines) để làm nền trắng.
    - Cut và Paste các biểu đồ từ các Sheet chứa Pivot Table sang Sheet Dashboard.
## Chèn Bộ lọc Tương tác (Slicers).
    - Chọn một biểu đồ -> Insert > Slicer.
    - Chọn các trường để lọc: 'Năm' (Year) và 'Khu vực' (Region).
## Chèn Timeline (Tùy chọn).
    - Insert > Timeline (dành riêng cho dữ liệu ngày tháng).
    - Cho phép lướt chọn dữ liệu theo Tháng/Quý/Năm nhanh chóng.
## Kết nối Slicer với nhiều biểu đồ (Report Connections).
    - Click chuột phải vào Slicer -> Report Connections.
    - Tích chọn tất cả các Pivot Tables có liên quan.
## Trải nghiệm tính Tương tác (Interactivity).
    - Thử click chọn Năm 2024 trên Slicer -> Quan sát toàn bộ biểu đồ tự động cập nhật.
    - Giải thích lợi ích: Giúp Ban giám đốc tự do "Drill-down" dữ liệu mà không cần kế toán vẽ lại biểu đồ.

### Phần 6: Đánh giá và tích hợp AI Insights
## Phân tích Dashboard bằng AI.
    - Cắt màn hình (Screenshot) Dashboard vừa tạo, dán vào ChatGPT (Vision).
    - Prompt: "Dựa vào hình ảnh Dashboard này, hãy tóm tắt 3 điểm nổi bật nhất về hiệu suất kinh doanh năm 2024."
## Tự động hóa Insight (NLG - Natural Language Generation).
    - Hướng dẫn dùng một số hàm Excel cơ bản ghép chuỗi (CONCATENATE) để tự động sinh ra một câu tóm tắt ngay trên Dashboard.
    - Ví dụ: ="Doanh thu cao nhất năm thuộc về " & [Hàm lấy tên sản phẩm].
## Tránh bẫy biểu đồ sai lệch (Misleading Traps).
    - Sinh viên tự kiểm tra chéo (Peer-review) Dashboard của bạn học.
    - Trục Y có bắt đầu từ 0 chưa? Màu sắc có nhất quán không? (Ví dụ: Sản phẩm A phải cùng 1 màu trên tất cả biểu đồ).
## Tổng kết buổi thực hành.
    - AI là công cụ sinh nội dung (Thuyết minh BCTC) và đọc hiểu kết quả (Dashboard Insights).
    - Kỹ năng tạo Dashboard là kỹ năng "kể chuyện" bằng số liệu giúp Kế toán viên nâng cao giá trị bản thân (từ Bookkeeper lên Advisor).
## Q&A - Giải đáp thắc mắc.
    - Hỗ trợ các sinh viên bị lỗi khi Report Connections hoặc lỗi Format biểu đồ.
    - Giao bài tập: Tự tùy biến Dashboard với màu sắc theo bộ nhận diện thương hiệu (Brand Guideline) của trường Đại học Đông Á.
