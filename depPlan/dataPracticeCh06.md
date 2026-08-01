# Kế hoạch Tạo Dữ liệu Thực hành cho Chương 6: Information Modeling

Dựa trên nội dung tài liệu Thực hành 6 (Chương 6), dưới đây là kế hoạch chi tiết tạo các bộ dữ liệu (datasets) để hỗ trợ sinh viên thực hành các bài tập về Lập mô hình thông tin (Information Modeling):

## Các Bộ Dữ liệu sẽ được tạo

### 1. Dữ liệu Ruppetware (EX 6.8)
- **Mô tả:** Dữ liệu bán hàng của nhân viên để thực hành xây dựng mô hình tính toán tiền thưởng (Bonus). Mục tiêu năm 2025 được xác định dựa trên trung bình doanh số năm 2024 cộng thêm 5%.
- **Các trường dữ liệu:** `SalespersonID`, `SalespersonName`, `SalesAmount_2024`, `SalesAmount_2025`.
- **Định dạng:** CSV (`Ruppetware_Sales.csv`).

### 2. Dữ liệu Leno Transportation Service - LTS (EX 6.9)
- **Mô tả:** Bộ 3 bảng dữ liệu quản lý vận tải để thực hành mô hình hóa quan hệ (Relational Modeling) nhằm kiểm tra xe tải nào chở quá tải hoặc dưới tải.
- **Bảng Trucks (Xe tải):** `TruckID`, `MaxCapacity_kg`.
- **Bảng Pallets (Kiện hàng):** `PalletID`, `Weight_kg`.
- **Bảng Schedule (Lịch trình):** `ScheduleID`, `Date`, `TruckID`, `PalletID`.
- **Định dạng:** CSV (`LTS_Trucks.csv`, `LTS_Pallets.csv`, `LTS_Schedule.csv`).

### 3. Dữ liệu D*Tunes (PAC 6.1, PAC 6.2, PAC 6.3)
- **Mô tả:** Hệ thống quản lý trung tâm khiêu vũ (hoặc âm nhạc) phức tạp để thực hành lập mô hình tính toán khả năng sinh lời, phát hiện gian lận (học viên học thử miễn phí nhiều lần), và phân tích điểm hòa vốn cho các lớp nhóm.
- **Bảng Instructors (Giảng viên):** `InstructorID`, `InstructorName`, `HoursTaught`, `AwardsWon`, `NationalRecognition` (để phân loại: Học việc, Trung cấp, Cao cấp, Vô địch).
- **Bảng Sessions (Buổi học):** `SessionID`, `SessionType` (Starter, Private, Group, Friday Party), `InstructorID`, `Date`.
- **Bảng Registrations (Học viên & Đăng ký):** `RegistrationID`, `StudentID`, `StudentName`, `SessionID`, `FeePaid`.
- **Định dạng:** CSV (`DTunes_Instructors.csv`, `DTunes_Sessions.csv`, `DTunes_Registrations.csv`).

## Các Bước Thực Hiện
1. Sử dụng thư viện Python (`pandas`, `random`, `faker`) để tự động sinh các bộ dữ liệu đa dạng, đảm bảo có chứa các kịch bản thực tế (như xe tải vượt tải trọng, học viên học thử nhiều lần, lớp nhóm không đủ học sinh để hòa vốn).
2. Lưu các file CSV này vào thư mục `TaiLieu/textbookForPractice/Data/`.
3. Cập nhật file `docs/practice_ch06.md` ở phần đầu để chèn liên kết tải xuống dạng thẻ HTML `<a>` (có thuộc tính `download` để tránh lỗi 404 trên Docsify) như đã cấu hình thành công ở chương 5.
4. Chạy kiểm tra đường dẫn tải file trước khi nghiệm thu.
