# Kế hoạch Tạo Dữ liệu Thực hành cho Chương 10: Recent Data and Analyses Developments in Accounting (Những phát triển gần đây trong Phân tích Dữ liệu Kế toán)

Dựa trên nội dung tài liệu Thực hành 10 (Chương 10), dưới đây là kế hoạch chi tiết tạo các bộ dữ liệu (datasets) để hỗ trợ sinh viên thực hành về tự động hóa quy trình bằng công cụ (Alteryx, Excel Macros) và kiểm toán các khoản chi phí dự phòng:

## Các Bộ Dữ liệu sẽ được tạo

### 1. Dữ liệu Water Sports, Inc. (EX 10.7)
- **Mô tả:** Dữ liệu doanh thu và chi phí của các dòng sản phẩm thể thao dưới nước để thực hành sử dụng phần mềm Alteryx tự động lập Báo cáo kết quả hoạt động kinh doanh so sánh (Comparative Income Statement). Sinh viên sẽ tự động hóa việc tính Lợi nhuận gộp (Gross Profit) và Thu nhập ròng (Net Income).
- **Các trường dữ liệu:** `ProductLine`, `SalesRevenue`, `CostOfGoodsSold`, `SellingAndAdminExpenses`.
- **Định dạng:** CSV (`WaterSports_Financials.csv`).

### 2. Dữ liệu OneStopShop, Inc. (EX 10.8)
- **Mô tả:** Dữ liệu báo cáo thu nhập và bảng cân đối kế toán của 6 bộ phận kinh doanh độc lập (Lau sàn, Chăm sóc bãi cỏ, Kiểm soát dịch hại, Dọn dẹp hộ gia đình, Vệ sinh văn phòng, Sản phẩm ống nước) cho 2 năm hiện tại và năm trước. Dữ liệu này dùng để thực hành viết Excel Macro tính tự động 4 tỷ số tài chính (ROA, Tỷ suất lợi nhuận, Vòng quay tài sản, Tỷ lệ thanh toán hiện hành).
- **Các trường dữ liệu:** `Division`, `Year` (2024, 2025), `NetIncome`, `TotalRevenue`, `AverageTotalAssets`, `CurrentAssets`, `CurrentLiabilities`.
- **Định dạng:** CSV (`OneStopShop_Divisions.csv`).

### 3. Dữ liệu Trách nhiệm Bảo hành Máy tính (EX 10.12)
- **Mô tả:** Dữ liệu số dư sổ cái liên quan đến Chi phí bảo hành (Warranty Expense) và Trách nhiệm bảo hành (Warranty Liability) để sinh viên thực hành phân tích biến động (Textual Analysis/Audit Analysis) nhằm kiểm tra tuân thủ GAAP.
- **Các trường dữ liệu:** `AccountNumber`, `AccountDescription`, `Balance_2024`, `Balance_2025`.
- **Định dạng:** CSV (`ComputerMfg_Warranty.csv`).

## Các Bước Thực Hiện
1. Sử dụng Python (`pandas`, `random`, `faker`) để tự động sinh các bộ dữ liệu trên theo đúng logic kế toán (tài sản > nợ, doanh thu > chi phí, v.v.).
2. Lưu tất cả file CSV vào thư mục `TaiLieu/textbookForPractice/Data/`.
3. Cập nhật file `docs/practice_ch10.md` để chèn danh sách liên kết tải xuống dạng thẻ HTML `<a>` có thuộc tính `download` ở ngay phần đầu trang Thực hành.
4. Đảm bảo dữ liệu tạo ra phản ánh đúng ngữ cảnh của chương về Tự động hóa quy trình bằng Robot (RPA) và Kế toán tài chính.
