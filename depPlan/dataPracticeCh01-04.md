# Kế hoạch Tạo Dữ liệu Thực hành cho Chương 1-4

Dựa trên yêu cầu, tôi tiến hành tạo các bộ dữ liệu mô phỏng (mock datasets) tương ứng với các tình huống thực hành, bài tập và ví dụ được đề cập trong sách giáo khoa từ Chương 1 đến Chương 4.

## Các Bộ Dữ liệu sẽ được tạo

### 1. Chương 2 & 4: Sihrya's Beauty Salon / Supply Store
- **Mô tả:** Dữ liệu bán hàng chi tiết để phân tích khả năng sinh lời của sản phẩm.
- **Các trường dữ liệu (Fields):** `SaleReceiptNo`, `Saledate`, `InvCode`, `NoSold`, `InvDesc`, `InvPrice`, `InvCost`.
- **Định dạng:** CSV (`Sihryas_Beauty_Sales.csv`).

### 2. Chương 4: Automated Transportation, Inc. (ATI)
- **Mô tả:** Dữ liệu toàn diện về chu trình mua hàng (Order-to-Pay), thuế hải quan và đánh giá nhà cung cấp.
- **Các trường dữ liệu (Fields):** `InvoiceNO`, `InvoiceAmt`, `ShipDate`, `InvoiceDate`, `VendorID`, `VendorName`, `ProductID`, `UnitCost`, `ShipCost`, `FlatDuty`, `TariffAmt`, `ShipLocation`, `QualityRate`, `PaymentTerms`, `ShipTerms`, `PayAddress`, `PONumber`, `PODate`, `ReceivingNumber`, `ReceivingDate`, `QtyReceived`, `QtyPurchased`, `QtyInvoice`, `Approved`.
- **Định dạng:** CSV (`ATI_Purchases_Data.csv`).

### 3. Chương 3 & 4: P-Card Spending & Vendor Payments
- **Mô tả:** Dữ liệu chi tiêu thẻ P-Card của nhân viên và các khoản thanh toán cho nhà cung cấp (để thực hành PivotTable và phân tích chẩn đoán).
- **Các trường dữ liệu P-Card:** `EmployeeNumber`, `EmployeeName`, `TransactionDate`, `Vendor`, `TransactionAmount`.
- **Các trường dữ liệu Vendor Payments (EX 3.3):** `VendorName`, `PaymentDate`, `PaymentAmount`. (Bao gồm các nhà cung cấp cụ thể như 4-Star Hose & Supply, Aecom, WRG LLC...).
- **Định dạng:** CSV (`PCard_And_Vendor_Payments.csv`).

### 4. Chương 4: Cửa hàng đồ thú cưng (Pet Supply Store)
- **Mô tả:** Dữ liệu đơn đặt hàng và nhà cung cấp để thực hành chiến lược dữ liệu và đánh giá chất lượng (EX 4.4, EX 4.6).
- **Các trường dữ liệu (Fields):** `PONo`, `VendorID`, `VendorName`, `VendorQuality`, `VendorAddress`, `VendorCity`, `VendorState`, `VendorZip`, `VendorPayterms`, `PODate`, `POItemID`, `POItemDescription`, `ItemCost`, `ItemQty`.
- **Định dạng:** CSV (`Pet_Supply_Purchases.csv`).

### 5. Bổ sung cho Chương 1: Little Tots Daycare
- **Mô tả:** Bảng cân đối số phát sinh (Trial Balance) và dữ liệu tài chính cơ bản để lập Báo cáo tài chính.
- **Định dạng:** CSV (`LittleTots_Financials.csv`).

## Các Bước Thực Hiện
1. Viết script Python sinh dữ liệu bằng thư viện `Faker` và `pandas`.
2. Chạy script để xuất dữ liệu ra thư mục `TaiLieu/Datasets/`.
3. Cập nhật file `docs/thuchanh.md` để bổ sung mô tả và liên kết tải các bộ dữ liệu này.
4. Cập nhật `walkthrough.md`.
