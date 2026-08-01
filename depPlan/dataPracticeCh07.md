# Kế hoạch Tạo Dữ liệu Thực hành cho Chương 7: Data Exploration (Khám phá dữ liệu)

Dựa trên nội dung tài liệu Thực hành 7 (Chương 7), dưới đây là kế hoạch chi tiết tạo các bộ dữ liệu (datasets) để hỗ trợ sinh viên thực hành các bài tập về Khám phá và Trực quan hóa dữ liệu:

## Các Bộ Dữ liệu sẽ được tạo

### 1. Dữ liệu Cook Autos (EX 7.7)
- **Mô tả:** Dữ liệu bán hàng (Thực tế vs Mục tiêu) của 3 nhân viên (Carlos, Arun, Shanice) cho 3 dòng xe (SUV, Sedan, Sports) năm 2025.
- **Các trường dữ liệu:** `Salesperson`, `CarType`, `Target_Sales`, `Actual_Sales`.
- **Định dạng:** CSV (`CookAutos_Sales.csv`).

### 2. Dữ liệu Wok and Dumpling (EX 7.8)
- **Mô tả:** Doanh thu bán hàng hàng ngày trong Quý 1 của 2 chi nhánh nhà hàng (Wok và Dumpling).
- **Các trường dữ liệu:** `Date`, `Restaurant_Branch`, `Daily_Sales`.
- **Định dạng:** CSV (`WokDumpling_Q1_Sales.csv`).

### 3. Dữ liệu Santorini Group (EX 7.9)
- **Mô tả:** Dữ liệu đặt phòng khách sạn của 5 nhân viên tham dự hội thảo, bao gồm tên khách sạn (Hilton, Marriott), giá phòng mỗi đêm và khoảng cách đến địa điểm hội thảo (để vẽ biểu đồ bong bóng).
- **Các trường dữ liệu:** `EmployeeName`, `Hotel`, `NightlyRate`, `DistanceToSeminar_miles`.
- **Định dạng:** CSV (`Santorini_Hotels.csv`).

### 4. Dữ liệu Rainbow Hotel (EX 7.14)
- **Mô tả:** Dữ liệu thống kê số lượng và loại khiếu nại của khách hàng trong tháng 1/2025. Thích hợp để vẽ biểu đồ Pareto.
- **Các trường dữ liệu:** `Complaint_ID`, `Date`, `Source` (Website, Call, Mail, ratemyhotel.com), `Category` (Phòng bẩn, Wifi kém, Chuột, Nhiệt độ, Phí bất ngờ, Nhân viên).
- **Định dạng:** CSV (`RainbowHotel_Complaints.csv`). (Dữ liệu sẽ được tạo dạng danh sách từng khiếu nại riêng biệt để sinh viên tự Pivot/Aggregate).

### 5. Dữ liệu Jumpers Grocery (EX 7.15)
- **Mô tả:** Dữ liệu doanh thu 5 năm của 2 siêu thị (NIndy, SIndy) theo 7 danh mục sản phẩm. Dùng để làm Bảng điều khiển tương tác (Interactive Dashboard).
- **Các trường dữ liệu:** `Year`, `Store`, `Category`, `SalesAmount`.
- **Định dạng:** CSV (`Jumpers_5Year_Sales.csv`).

### 6. Dữ liệu Hệ thống NoTable (PAC 7.2, 7.3, 7.4)
Hệ thống ERP của NoTable sẽ gồm 3 bảng phục vụ phân tích chi phí, quản lý công nợ và thuế:
- **NoTable_Production.csv (PAC 7.2):** `OrderID`, `DesignerName`, `Est_LaborCost`, `Act_LaborCost`, `Est_MaterialCost`, `Act_MaterialCost`. (Phân tích chênh lệch - Variance).
- **NoTable_SalesOrders.csv (PAC 7.3, 7.4):** `OrderID`, `CustomerID`, `OrderDate`, `Amount`, `PaymentDate`, `DeliveryState`. (Phân tích chiết khấu thanh toán sớm, phạt trả chậm và phân tích thuế chưa thu theo bang).
- **NoTable_Customers.csv (PAC 7.3):** `CustomerID`, `CustomerName`, `CreditRating`. 

## Các Bước Thực Hiện
1. Sử dụng Python (`pandas`, `random`, `faker`) để tự động sinh các bộ dữ liệu trên theo đúng logic và các số liệu mẫu được miêu tả trong sách giáo khoa.
2. Lưu tất cả file CSV vào thư mục `TaiLieu/textbookForPractice/Data/`.
3. Cập nhật file `docs/practice_ch07.md` để chèn danh sách liên kết tải xuống dạng thẻ HTML `<a>` có thuộc tính `download` ở ngay phần đầu trang Thực hành.
4. Nghiệm thu và kiểm tra các đường dẫn.
