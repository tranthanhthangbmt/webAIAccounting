# Tài nguyên Thực hành (Practical Resources)

Trang này cung cấp các bộ dữ liệu và hướng dẫn phần mềm cần thiết để bạn thực hành các bài tập theo cuốn sách **"Data and Analytics in Accounting: An Integrated Approach"** (Ann C. Dzuranin).

---

## 1. Các phần mềm cần thiết (Software Requirements)
Để theo kịp nội dung thực hành của môn học, sinh viên cần cài đặt và làm quen với các công cụ sau:

- **Microsoft Excel (Trọng tâm chính):**
  - Cần kích hoạt công cụ **Power Query** (vào thẻ Data -> Get Data) để làm sạch dữ liệu (ETL).
  - Cần cài đặt Add-in **Data Analysis ToolPak** (vào File -> Options -> Add-ins) để thực hiện thống kê mô tả, Histogram, và Regression.
  - *Yêu cầu:* Excel 2016 trở lên hoặc Microsoft 365.

- **Tableau Public:**
  - Hoàn toàn miễn phí. Dùng để thực hành vẽ Dashboard tài chính và trực quan hóa dữ liệu (Data Visualization).
  - *Link tải:* [Tải Tableau Public](https://public.tableau.com/en-us/s/download)

- **Microsoft Power BI Desktop:**
  - Công cụ thay thế hoặc bổ trợ xuất sắc cho Excel trong việc lập Dashboard. Hoàn toàn miễn phí.
  - *Link tải:* [Tải Power BI Desktop](https://powerbi.microsoft.com/desktop/)

---

## 2. Các Bộ Dữ liệu Thực hành (Mock Datasets)

Dưới đây là các bộ dữ liệu mô phỏng (Mock Data) đã được chuẩn bị sẵn, bám sát các dự án thực tế trong giáo trình để bạn thực hành kỹ năng Kế toán - Dữ liệu. Hãy tải về và lưu vào một thư mục riêng biệt trên máy tính của bạn:

1. **Dự án Phân tích Lợi nhuận (Le Grind Coffee Distributors):**
   - *Mô tả:* Dữ liệu bán hàng chi tiết bao gồm Mã khách hàng, Phân loại khách hàng, Nguồn gốc cà phê, Doanh thu và Giá vốn hàng bán (COGS). Bộ dữ liệu này dùng để thực hành phân tích biên lợi nhuận gộp (Gross Margin Analysis) và làm quen với Pivot Table.
   - 📥 **[Tải file CSV: LeGrind_Raw.csv](../TaiLieu/Datasets/LeGrind_Raw.csv)**

2. **Dự án Dự báo và Mô hình hóa "What-if" (Super Scooters):**
   - *Mô tả:* Dữ liệu doanh số, giá bán lẻ, chi phí biến đổi, và chi phí cố định phân bổ theo từng tháng của các dòng xe Scooter. Dùng để thực hành mô hình hóa độ nhạy (Sensitivity Analysis) và dự báo lợi nhuận hoạt động (Operating Income).
   - 📥 **[Tải file CSV: SuperScooters_Case.csv](../TaiLieu/Datasets/SuperScooters_Case.csv)**

3. **Thực hành Làm sạch Dữ liệu (Dirty Data ETL):**
   - *Mô tả:* Một bộ dữ liệu bán hàng giả định chứa rất nhiều lỗi cố ý (Dirty Data) như: định dạng ngày tháng không đồng nhất, khoảng trắng thừa, trùng lặp mã đơn hàng, lỗi chính tả, sai kiểu dữ liệu... Bạn sẽ dùng Power Query hoặc XLOOKUP để dọn dẹp bộ dữ liệu này trước khi phân tích.
   - 📥 **[Tải file Excel: Sales_DirtyData.xlsx](../TaiLieu/Datasets/Sales_DirtyData.xlsx)**

---

## 3. Nguồn tài nguyên mở rộng (External Repositories)

Nếu bạn muốn rèn luyện thêm với các bộ dữ liệu khổng lồ (hàng triệu dòng), hãy tham khảo các nguồn mã nguồn mở sau:

- **Kaggle Datasets:** Tìm kiếm các từ khóa như "Financial Accounting Data" hoặc "Retail Store Sales Data" tại [Kaggle](https://www.kaggle.com/datasets).
- **Cộng đồng Tableau Public:** Lên thư viện của Tableau Public, tìm kiếm "CFO Dashboard" hoặc "Income Statement Dashboard", sau đó tải file workbook `.twbx` về để tham khảo cách các chuyên gia kết nối và vẽ biểu đồ dữ liệu kế toán.
