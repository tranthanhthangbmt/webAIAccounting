# Kế hoạch Tạo Dữ liệu Thực hành cho Chương 5: Analysis: Data Preparation

Dựa trên nội dung tài liệu Thực hành 5 (Chương 5), dưới đây là kế hoạch chi tiết tạo các bộ dữ liệu (datasets) để hỗ trợ sinh viên thực hành các bài tập xử lý dữ liệu thực tế:

## Các Bộ Dữ liệu sẽ được tạo

### 1. Dữ liệu Hikko (EX 5.7)
- **Mô tả:** Dữ liệu doanh thu bán hàng theo quý và khu vực (US, Châu Âu, Châu Á) từ 2022 đến 2024. Dữ liệu này dùng để thực hành các kỹ thuật tái cấu trúc bảng (Pivot/Unpivot) nhằm đưa dữ liệu về dạng bảng dọc chuẩn hóa.
- **Các trường dữ liệu:** `Region`, `2022:Q1`, `2022:Q2`, `2022:Q3`, `2022:Q4`, `2023:Q1`... đến `2024:Q4`.
- **Định dạng:** CSV (`Hikko_Revenue_Data.csv`).

### 2. Dữ liệu Wilkinson (EX 5.8)
- **Mô tả:** Dữ liệu theo dõi thời gian làm việc (Time cards) của nhân viên xây dựng cho các dự án/tài sản khác nhau trong nhiều tuần.
- **Các trường dữ liệu:** `EmployeeID`, `EmployeeName`, `JobID`, `WeekNo`, `DayOfWeek`, `Date`, `HoursWorked`.
- **Định dạng:** CSV (`Wilkinson_Timecards.csv`).

### 3. Dữ liệu Vroomba (EX 5.11)
- **Mô tả:** Dữ liệu giao dịch bán hàng robot hút bụi. Dữ liệu này dùng để thực hành tạo và kiểm tra các quy tắc xác thực (Validation Rules) như: Giá bán, khách hàng phải thuộc danh sách nhà phân phối, doanh số đạt chỉ tiêu...
- **Các trường dữ liệu:** `TransactionID`, `SalespersonID`, `DistributorName`, `UnitsSold`, `UnitPrice`, `SaleDate`.
- **Định dạng:** CSV (`Vroomba_Sales.csv`).

### 4. Dữ liệu Fluffy (PAC 5.1, PAC 5.2, PAC 5.3)
- **Mô tả:** Công ty Fluffy có bộ dữ liệu phức tạp gồm Đơn đặt hàng (Sales Orders), Thu tiền (Cash Receipts) và Hồ sơ nhà cung cấp (Vendors) để làm sạch dữ liệu và phân tích chi phí tiêu chuẩn.
- **Dữ liệu SalesOrders:** `OrderNo`, `OrderDate`, `Amount`.
- **Dữ liệu CashReceipts:** `ReceiptNo`, `OrderNo`, `ReceiptDate`, `Amount`, `PaymentType`.
- **Dữ liệu Vendors/Costs:** `VendorID`, `VendorName`, `ServiceType`, `StandardCost`, `ActualCost`.
- **Định dạng:** CSV (`Fluffy_SalesOrders.csv`, `Fluffy_CashReceipts.csv`, `Fluffy_Vendors.csv`).

### 5. Dữ liệu HomePrinter & Creighton Group (EX 5.9, 5.10)
- **Mô tả:** Các tập dữ liệu mẫu cố tình chứa nhiều lỗi phổ biến (missing values, sai định dạng, outliers) để sinh viên lập hồ sơ dữ liệu (data profiling).
- **Định dạng:** CSV (`HomePrinter_Data.csv`, `Creighton_Payroll.csv`).

## Các Bước Thực Hiện
1. Sử dụng Python (`pandas`) để sinh các bộ dữ liệu này sao cho sát với các giá trị được mô tả trong bài tập.
2. Lưu các file này vào thư mục `TaiLieu/textbookForPractice/Data/` (hoặc thư mục dữ liệu tương ứng của dự án).
3. Cập nhật file `docs/practice_ch05.md` ở phần đầu để chèn liên kết tải xuống các tập dữ liệu này, tương tự như cách đã làm với các bài thực hành 1-4.
4. Chạy kiểm tra để đảm bảo người học có thể làm bài tập một cách chính xác dựa trên dữ liệu cung cấp.
