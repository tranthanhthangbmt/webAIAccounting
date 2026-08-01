# Kế hoạch Tạo Dữ liệu Thực hành cho Chương 8: Interpreting Data Analysis Results (Diễn giải kết quả phân tích)

Dựa trên nội dung tài liệu Thực hành 8 (Chương 8), dưới đây là kế hoạch chi tiết tạo các bộ dữ liệu (datasets) để hỗ trợ sinh viên thực hành việc diễn giải các kết quả phân tích chẩn đoán, mô tả và dự đoán:

## Các Bộ Dữ liệu sẽ được tạo

### 1. Dữ liệu One Stop Shop (EX 8.14)
- **Mô tả:** Dữ liệu bán hàng theo quý từ năm 2022 đến 2025 để phân tích tính mùa vụ (Seasonality) thông qua phân tích chẩn đoán.
- **Các trường dữ liệu:** `Year`, `Quarter` (Q1, Q2, Q3, Q4), `SalesAmount`.
- **Định dạng:** CSV (`OneStopShop_Sales.csv`).

### 2. Dữ liệu U.S. Outdoor Adventures (EX 8.15, PR 8.1)
- **Mô tả:** Bộ dữ liệu chứa thông tin chi phí vận chuyển, phương thức vận chuyển và mức độ ưu tiên của đơn hàng (2022-2025). Dữ liệu này dùng để diễn giải phân tích mô tả.
- **Các trường dữ liệu:** `Year`, `Priority` (Critical, High, Medium, Low), `ShippingMode` (First class, Same day, Second class, Standard class), `ShipmentsCount`, `ShippingCost`.
- **Định dạng:** CSV (`OutdoorAdventures_Shipping.csv`).

### 3. Dữ liệu All Care Hospital (PR 8.2)
- **Mô tả:** Dữ liệu hoạt động của 2.000 bệnh viện trong hệ thống để thực hiện diễn giải phân tích dự đoán (Predictive Analysis) cho chi phí năm 2026.
- **Các trường dữ liệu:** `HospitalID`, `Admissions` (Số ca nhập viện), `Beds` (Số giường bệnh), `StaffingLevel` (Số lượng nhân viên), `TotalOperatingCost` (Tổng chi phí hoạt động).
- **Định dạng:** CSV (`AllCareHospital_Costs.csv`).

### 4. Dữ liệu Hệ thống Ortho Inc. (PAC 8.2, 8.3)
Bộ dữ liệu gồm 2 bảng để so sánh Đơn đặt hàng (Mua hàng) với Doanh số bán hàng và Báo cáo doanh thu theo bộ phận địa lý:
- **Ortho_Purchasing_Sales.csv (PAC 8.2):** Dữ liệu theo tháng (2022-2025) gồm `Date` (Tháng/Năm), `SalesAmount`, `PurchaseOrdersAmount`. (Phân tích xem bộ phận thu mua có mua dư thừa nguyên liệu hay không).
- **Ortho_Sales_By_State.csv (PAC 8.3):** Dữ liệu doanh thu bán hàng chi tiết theo các bang CA, FL, IL, NY, TX cho năm 2024 và 2025 để lập báo cáo phân khúc (Segment Reporting - ASC 606). Các trường: `Year`, `State`, `SalesRevenue`.

## Các Bước Thực Hiện
1. Sử dụng Python (`pandas`, `random`, `faker`) để tự động sinh các bộ dữ liệu trên theo đúng logic và các số liệu được gợi ý trong sách giáo khoa.
2. Lưu tất cả file CSV vào thư mục `TaiLieu/textbookForPractice/Data/`.
3. Cập nhật file `docs/practice_ch08.md` để chèn danh sách liên kết tải xuống dạng thẻ HTML `<a>` có thuộc tính `download` ở ngay phần đầu trang Thực hành.
4. Đảm bảo dữ liệu tính toán hợp lý để sinh viên có thể đưa ra các diễn giải (như mùa vụ bán hàng, chi phí vận chuyển tăng mạnh, thu mua nguyên liệu vượt ngưỡng doanh số).
