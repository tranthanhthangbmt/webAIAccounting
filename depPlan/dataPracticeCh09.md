# Kế hoạch Tạo Dữ liệu Thực hành cho Chương 9: Communicating Data Analysis Results (Truyền đạt kết quả phân tích)

Dựa trên nội dung tài liệu Thực hành 9 (Chương 9), dưới đây là kế hoạch chi tiết tạo các bộ dữ liệu (datasets) để hỗ trợ sinh viên thực hành về trực quan hóa dữ liệu (Data Visualization), xây dựng bảng điều khiển (Dashboards), và kể chuyện bằng dữ liệu (Data Storytelling):

## Các Bộ Dữ liệu sẽ được tạo

### 1. Dữ liệu SWI Inc. (EX 9.17)
- **Mô tả:** Dữ liệu số lượng phê duyệt bán hàng và tổng doanh thu đã phê duyệt của 3 giám đốc bán hàng (Mary Ann Parola, Hamish Rundan, Shonie Oscebono) cho 4 khu vực. Dùng để sinh viên phát hiện và sửa các biểu đồ dễ gây hiểu lầm.
- **Các trường dữ liệu:** `SalesManager`, `Region`, `SalesApprovedCount`, `TotalRevenue`.
- **Định dạng:** CSV (`SWI_SalesApprovals.csv`).

### 2. Dữ liệu Super Scooters (EX 9.18)
- **Mô tả:** Dữ liệu chi phí sản xuất dòng xe Celeritas (nhân công, nguyên vật liệu, chi phí chung) theo tháng để sinh viên phát hiện các biểu đồ sai lệch về chi phí cố định và biến đổi.
- **Các trường dữ liệu:** `Month`, `Labor_Cost`, `Material_Cost`, `Overhead_Cost`, `TotalAllocated_Cost`.
- **Định dạng:** CSV (`SuperScooters_Costs.csv`).

### 3. Dữ liệu Phụ tùng Xe đạp HEH, Inc. (EX 9.19)
- **Mô tả:** Dữ liệu bán hàng B2B (doanh nghiệp với doanh nghiệp) cho một công ty bán phụ tùng xe đạp. Phục vụ cho việc tạo Dashboard bán hàng tương tác.
- **Các trường dữ liệu:** `Date`, `CustomerID`, `CustomerName`, `ProductCategory`, `SalesAmount`, `Region`.
- **Định dạng:** CSV (`HEH_B2B_Sales.csv`).

### 4. Dữ liệu One Stop Shop (EX 9.20)
- **Mô tả:** Dữ liệu xu hướng bán hàng và cơ cấu sản phẩm (12 loại hàng hóa như: Đồ trẻ em, Đồ uống, Ngũ cốc, Quần áo, Mỹ phẩm, v.v.) từ 2022 đến 2025. Dùng để sửa lại biểu đồ phân tích xu hướng do khách hàng làm sai.
- **Các trường dữ liệu:** `Year`, `ProductCategory`, `SalesPercentage`, `TotalSalesAmount`.
- **Định dạng:** CSV (`OneStopShop_ProductMix.csv`).

### 5. Dữ liệu Hệ thống Thư viện MPL (PAC 9.1, 9.2, 9.3, 9.4)
Bộ dữ liệu gồm 4 bảng bao quát hệ thống thư viện, phục vụ xây dựng báo cáo toàn diện và kể chuyện dữ liệu (Data Storytelling):
- **MPL_ComputerUsage.csv (PAC 9.1):** Sử dụng máy tính tại các chi nhánh. `Branch`, `ComputersAvailable`, `DailyAvgUsers`.
- **MPL_Payroll.csv (PAC 9.2):** Chi phí tiền lương. `EmployeeID`, `EmployeeName`, `Branch`, `Position`, `AnnualSalary`.
- **MPL_Financials_10Y.csv (PAC 9.3):** Phân tích doanh thu và chi phí 10 năm (2016-2025). `Year`, `TotalRevenue`, `TotalExpenses`.
- **MPL_PerformanceMetrics.csv (PAC 9.4):** Các chỉ số tài chính và phi tài chính theo tháng để làm Dashboard. `YearMonth`, `Branch`, `BooksBorrowed`, `Visitors`, `DonationsReceived`, `FinesCollected`.

## Các Bước Thực Hiện
1. Sử dụng Python (`pandas`, `random`, `faker`) để tự động sinh các bộ dữ liệu trên theo đúng logic và các số liệu được gợi ý trong sách giáo khoa.
2. Lưu tất cả file CSV vào thư mục `TaiLieu/textbookForPractice/Data/`.
3. Cập nhật file `docs/practice_ch09.md` để chèn danh sách liên kết tải xuống dạng thẻ HTML `<a>` có thuộc tính `download` ở ngay phần đầu trang Thực hành.
4. Đảm bảo dữ liệu được sinh ra cố ý có những cấu trúc phù hợp với mục tiêu "sửa lỗi trực quan hóa" (visualization errors) hoặc thiết kế "bảng điều khiển tương tác" (interactive dashboards) của Chương 9.
