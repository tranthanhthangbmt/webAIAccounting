## Bài Tập Ngắn (Brief Exercises)

**BE 2.1 (LO 1) Kế toán Quản trị (Managerial Accounting)**
Bạn là một chuyên viên phân tích tài chính cho PizzaNow! Kiểm soát viên nội bộ của công ty muốn bạn thực hiện một phân tích sử dụng ba bảng trong cơ sở dữ liệu quan hệ (Employees, Customers, TakeOrder).
Đối với mỗi khoản mục sau, hãy xác định xem nó là một khóa chính (primary key), khóa ngoại (foreign key), hay không phải cả hai.
1. OrderNumber trong bảng TakeOrder
2. EmployeeID trong bảng TakeOrder
3. CustomerID trong bảng Customers
4. EmployeeID trong bảng Employees
5. Date trong bảng TakeOrder
6. ZipCode trong bảng Employees

**BE 2.2 (LO 1) Hệ thống Thông tin Kế toán (Accounting Information Systems)**
Dine At Home cung cấp dịch vụ giao đồ ăn tận nhà được đặt từ nhiều nhà hàng địa phương khác nhau. Bạn là người kết nối giữa bộ phận công nghệ thông tin và bộ phận kế toán của công ty. Bạn được yêu cầu giải thích mối quan hệ giữa ba bảng này cho nhóm kế toán. Các bảng (Customer1, Restaurant, Order) được lấy từ cơ sở dữ liệu của Dine At Home.
Đối với mỗi kịch bản, hãy xác định kết nối (join) mà bạn có khả năng sử dụng nhiều nhất để truy vấn dữ liệu. Mỗi loại kết nối có thể được sử dụng một lần, nhiều lần, hoặc không được sử dụng.
a. Left join
b. Right join
c. Inner join
d. Full join
1. Thực hiện một truy vấn để kết nối bảng Restaurant (bảng bên trái) và bảng Order (bảng bên phải), nhưng chỉ trả về các hàng từ cả hai bảng có giá trị khớp nhau.
2. Thực hiện một truy vấn để kết nối bảng Restaurant (bảng bên trái) và bảng Customer1 (bảng bên phải), và trả về tất cả các bản ghi từ bảng Restaurant, nhưng chỉ trả về các bản ghi khớp từ bảng Customer1.
3. Thực hiện một truy vấn để kết nối bảng Order (bảng bên trái) và bảng Customer1 (bảng bên phải), và trả về tất cả các bản ghi từ cả hai bảng. Khớp các bản ghi có thể khớp ở cả hai bảng.
4. Thực hiện một truy vấn để kết nối bảng Order (bảng bên trái) và bảng Customer1 (bảng bên phải), và chỉ trả về tất cả các bản ghi từ bảng Order và các bản ghi khớp từ bảng Customer1.
1. Xác định khóa chính (primary keys) và khóa ngoại (foreign keys) cho mỗi bảng.
2. Nếu bạn muốn biết tên của một khách hàng cho một đơn hàng cụ thể, bạn nên truy vấn các bảng nào?

**BE 2.3 (LO 1) Kế toán Tài chính (Financial Accounting)**
Giả sử bạn là một chuyên viên phân tích tài chính trong nhóm kiểm soát cho công ty phân phối của bạn. Bạn được yêu cầu xác định tất cả các mặt hàng tồn kho không có doanh số bán hàng trong năm qua:
- Nhóm IT đã cung cấp tệp dữ liệu hàng tồn kho hiện có (inventory on hand data file) và tệp dữ liệu doanh số mười hai tháng (twelve month sales data file).
- Bạn đã xác định bảng hàng tồn kho hiện có là bảng bên trái và bảng doanh số mười hai tháng là bảng bên phải.
Hãy xác định kết nối (join) phù hợp nhất cho hai bảng này để thực hiện phân tích của bạn. Tại sao kết nối này lại phù hợp nhất?

**BE 2.4 (LO 1) Kế toán Tài chính (Financial Accounting)**
Bạn là một chuyên viên phân tích tài chính cho Dine At Home và được yêu cầu phân tích dữ liệu trong ba bảng trên (Customer1, Restaurant, Order). 

**BE 2.5 (LO 2) > **Data** Kế toán Quản trị (Managerial Accounting)**
Kiểm soát viên tại ThisBigCity đã yêu cầu bạn thực hiện một bản phân tích về chi phí hoàn trả cho nhân viên (employee reimbursement expenses) của thành phố trong mười lăm năm qua. Nhóm IT đã cung cấp một bản tải xuống tất cả dữ liệu hoàn trả cho nhân viên kể từ năm 2005.
1. Sử dụng hàm AVERAGE. Số tiền hoàn trả trung bình được trả từ tháng 7 năm 2005 đến tháng 11 năm 2020 là bao nhiêu?
2. Sử dụng hàm AVERAGEIF. Số tiền hoàn trả trung bình được trả trong năm 2019 là bao nhiêu?
3. Sử dụng hàm AVERAGEIFS. Số tiền hoàn trả trung bình được trả trong sở cứu hỏa (fire department) trong năm 2019 là bao nhiêu?

**BE 2.6 (LO 2) > **Data** Hệ thống Thông tin Kế toán (Accounting Information Systems)**
Là một kiểm toán viên nội bộ tại ThisBigCity, bạn đang kiểm tra các kiểm soát nội bộ (internal controls) đối với quy trình hoàn trả cho nhân viên của thành phố. Nhóm IT đã cung cấp bản tải xuống tất cả dữ liệu hoàn trả cho nhân viên kể từ năm 2005. Quản lý của bạn đề xuất thực hiện thống kê mô tả (descriptive statistics) trên tệp này để xác định xem bạn có dữ liệu tổng thể (population of data) đầy đủ hay không, và để bắt đầu quá trình xác định kích thước mẫu (sample size) cho việc kiểm tra kiểm soát nội bộ.
1. Sử dụng hàm COUNT. Có bao nhiêu khoản hoàn trả được thanh toán từ tháng 7 năm 2005 đến tháng 11 năm 2020?
2. Sử dụng hàm COUNTIF. Có bao nhiêu khoản hoàn trả được thanh toán trong năm 2019?
3. Sử dụng hàm COUNTIFS. Có bao nhiêu khoản hoàn trả được thanh toán trong năm 2019 cho lực lượng cứu hỏa (firefighters)?

**BE 2.7 (LO 3) > **Data** Kiểm toán (Auditing)**
Sử dụng PivotTables và dữ liệu có sẵn để trả lời các câu hỏi sau:
1. Khách hàng nào có số dư khoản phải thu (accounts receivable balance) cao nhất?
2. Khách hàng nào có số dư khoản phải thu cao nhất mà đã quá hạn (past due) trên 150 ngày?

**BE 2.8 (LO 3) > **Data** Kế toán Tài chính (Financial Accounting)**
Sử dụng PivotTables và dữ liệu có sẵn để trả lời các câu hỏi sau:
1. Tổng các khoản phải thu (accounts receivable) là bao nhiêu?
2. Tổng số theo từng khu vực (region) là bao nhiêu?

**BE 2.9 (LO 3) > **Data** Kế toán Tài chính (Financial Accounting), Kế toán Quản trị (Managerial Accounting)**
Sử dụng PivotTables và dữ liệu Super Scooters để trả lời các câu hỏi sau:
1. Tổng doanh thu gộp (gross sales) cho mỗi mẫu xe (model) theo từng năm là bao nhiêu?
2. Xe màu nào có khối lượng bán (sales volume) cao nhất trong năm 2023?
3. Tổng chi phí tiếp thị biến đổi (variable marketing expense) cho năm 2023 tính theo mẫu xe là bao nhiêu?

**BE 2.10 (LO 4) > **Data** Kế toán Quản trị (Managerial Accounting)**
Là một chuyên viên phân tích tài chính làm việc cho Animal Control Centers, bạn muốn hiểu về khoản tiền làm thêm giờ (overtime pay) trong năm 2025. Hãy tìm các thống kê sau đây cho tiền lương làm thêm giờ:
1. Số trung bình (Mean)
2. Số trung vị (Median)
3. Yếu vị (Mode)

**BE 2.11 (LO 4) > **Data** Kế toán Tài chính (Financial Accounting)**
Bạn đang chuẩn bị cuộc thảo luận và phân tích của ban giám đốc (MD&A) liên quan đến sở cứu hỏa của thành phố Chicago. Một trong những khoản chi phí quan trọng nhất của sở cứu hỏa là tiền làm thêm giờ. Do đó, bạn muốn hiểu dữ liệu làm thêm giờ trước khi viết bài MD&A.
1. Tính hệ số bất đối xứng (coefficient of skewness) cho tiền lương làm thêm giờ.
2. Tính hệ số độ nhọn (coefficient of kurtosis) cho tiền lương làm thêm giờ.
3. Chuẩn bị một biểu đồ tần suất (histogram) với các nhóm (groupings) sau: $500, $1,000, $2,000, $3,000, $4,000, $5,000, $6,000.

**BE 2.12 (LO 5) > **Data** Kế toán Tài chính (Financial Accounting)**
Công ty của bạn, Loans Are US, cung cấp các khoản vay cho các doanh nghiệp quy mô nhỏ đến vừa. Công ty có các văn phòng cho vay tại bốn khu vực. Bạn được yêu cầu chuẩn bị một trực quan hóa minh họa tổng số tiền cho vay theo khu vực và theo tuổi nợ (age of receivables). Hãy chuẩn bị một biểu đồ cột xếp chồng (stacked column chart) để làm điều này.

**BE 2.13 (LO 5) > **Data** Kế toán Tài chính (Financial Accounting)**
Loans Are US theo dõi xếp hạng tín dụng cho tất cả tài khoản của khách hàng. Bạn phải chuẩn bị một trực quan hóa minh họa tổng số các khoản vay dựa trên xếp hạng tín dụng. Hãy chuẩn bị một biểu đồ cột (bar chart) trực quan hóa số lượng tài khoản trong mỗi mức thuộc ba xếp hạng tín dụng: AAA, BBB, và CCC.

**BE 2.14 (LO 5) > **Data** Kế toán Tài chính (Financial Accounting)**
Cấp trên của bạn tại Loans Are US đã yêu cầu bạn chuẩn bị một trực quan hóa minh họa tổng số tiền tính bằng đô la của các khoản vay đã quá hạn thanh toán trên 150 ngày dựa theo xếp hạng tín dụng. Hãy chuẩn bị một biểu đồ cột trực quan hóa số lượng tài khoản trong mỗi mức thuộc ba xếp hạng tín dụng: AAA, BBB, và CCC.
