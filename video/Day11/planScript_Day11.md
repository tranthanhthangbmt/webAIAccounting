# Kế hoạch Kịch bản Bài giảng: Day 11 - Kỹ năng Phân tích Dữ liệu Nền tảng (Foundational Data Analysis)

**Tệp đầu vào:** `Slide_AIAcc_Day11.tex` & Textbook "Data and Analytics in the Accounting Profession".
**Hình thức:** Hội thoại giảng dạy Socratic (Người 1: Giảng viên, Người 2: Sinh viên).
**Mục tiêu:** Xây dựng tư duy phân tích dữ liệu cho kiểm toán viên, từ việc truy xuất cơ sở dữ liệu (SQL), xử lý bằng hàm Excel (SUMIFS), khám phá đa chiều (PivotTable), và vạch trần các bất thường (Thống kê mô tả & Trực quan hóa).

## Dàn ý Chi tiết (Mapping Slide & Textbook)

### Mở đầu & Ảo ảnh của Số Trung Bình (Slide 1 - 8)
- **Tình huống Super Scooters:** Chi phí bảo hành trung bình \$600 (dưới mức ngân sách \$650). Có an toàn không?
- **Lật tẩy ảo ảnh:** Số trung bình "san bằng" mọi thứ. Thực tế có 2 nhóm: lỗi nhỏ \$200 và lỗi nghiêm trọng \$1.200. Mức \$600 không đại diện cho giao dịch nào cả!
- **Hành trình khám phá:** Giới thiệu 4 bước từ SQL -> Excel -> PivotTable -> Thống kê mô tả/Trực quan hóa.

### Phần 1: Cơ sở Dữ liệu Quan hệ & Nghệ thuật Kết nối (Slide 9 - 19)
- **Cơ sở dữ liệu quan hệ (Relational Database):** Không phải 1 sheet Excel khổng lồ, mà chia thành nhiều Bảng (Tables).
- **Khóa chính (Primary Key):** Số định danh độc nhất (ẩn dụ: Số Căn cước công dân).
- **Khóa ngoại (Foreign Key):** Mỏ neo liên kết các bảng.
- **Tại sao phải tách bảng?** Giảm dư thừa dữ liệu (không phải nhập lại tỷ lệ khấu hao hàng ngàn lần).
- **SQL JOIN:** Cầu nối dữ liệu.
- **Inner Join vs Left Join:**
  - Inner Join: Chỉ lấy dữ liệu khớp 2 bên (Bỏ lọt hóa đơn ma).
  - Left Join: Lấy toàn bộ Hóa đơn (Bảng Trái), đắp Nhà cung cấp (Bảng Phải) vào. Nếu lòi ra giá trị NULL -> Phát hiện nhà cung cấp ma (kẻ cắp tàng hình).

### Phần 2: Chế ngự Dữ liệu Khổng lồ bằng Excel (Slide 20 - 26)
- **Giới hạn của hàm cơ bản:** SUM/COUNT không trả lời được các câu hỏi phức tạp đa chiều của Ban giám đốc.
- **Giải pháp - Hàm có điều kiện:** SUMIFS/COUNTIFS.
- **Ẩn dụ SUMIFS:** "Người bảo vệ khắt khe" cầm danh sách tiêu chí, duyệt từng dòng, chỉ cho qua nếu thỏa mãn ĐỒNG THỜI mọi điều kiện.
- **Nhược điểm:** Chỉ dùng được khi ta "biết rõ câu hỏi mình muốn đặt ra".

### Phần 3: Pivot Table & Tư duy Khám phá (Slide 27 - 32)
- **PivotTable:** Khi chưa biết hỏi gì, ta dùng Pivot để khám phá.
- **Cơ chế Kéo & Thả (Drag & Drop):** Xử lý hàng trăm ngàn dòng trong 10 giây.
- **5 Vùng cốt lõi:** Filters, Columns, Rows, Values.
- **Tương tác:** Tạo Dashboard với Slicers (Bộ lọc thời gian thực).
- **Cạm bẫy:** PivotTable lại đưa ra con số trung bình gọn gàng -> Lại rơi vào bẫy ảo ảnh ở đầu bài. Cần bước tiếp theo.

### Phần 4: Thống kê Mô tả & Vạch trần Sự thật (Slide 33 - 37)
- **Thống kê mô tả:** Không chỉ nhìn Mean. Phải xem Phương sai (Variance) và Độ lệch chuẩn (Std Dev).
- **Độ lệch (Skewness) & Độ nhọn (Kurtosis):** Hình dáng ngọn núi dữ liệu.
- **Lưng lạc đà (Bimodal):** Quay lại vụ Super Scooters. Đồ thị có 2 đỉnh (\$200 và \$1.200). \$600 nằm ở khoảng không vô nghĩa giữa 2 bướu lạc đà!
- **Độ lệch chuẩn (Radar an ninh):** Đóng vai trò thiết lập không phận an toàn. Giao dịch vượt ranh giới sẽ chớp đỏ báo hiệu Ngoại lệ (Outlier).

### Phần 5: Trực quan hóa Dữ liệu (Slide 38 - 44)
- **Giới hạn não bộ:** Đọc 500.000 dòng Excel gây "mù lòa nhận thức". Chuyển sang Vỏ não thị giác.
- **Scatter Plot (Biểu đồ phân tán):** Phát hiện Outlier trong tích tắc.
- **Hai giai đoạn:** Khám phá (lộn xộn như phòng thám tử) và Giải thích (gọn gàng, thuyết phục sếp).
- **Chọn đúng biểu đồ:** Bar chart (So sánh lớn nhỏ), Histogram (Xem hình dáng bướu lạc đà).
- **Tổng kết:** Đúc kết 4 vai trò của kiểm toán viên (Kiến trúc sư, Người điều phối, Thám tử, Nhà kể chuyện).
