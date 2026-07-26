# Kế hoạch Xây dựng Slide Bài giảng - Buổi 11

## 1. Thông tin Chung
- **Môn học:** Trí tuệ Nhân tạo cho Kế toán (AI in Accounting)
- **Buổi học:** 11 - Kỹ năng Phân tích Dữ liệu Nền tảng (Foundational Data Analysis Skills)
- **Thời lượng:** 135 phút (3 tiết)
- **Số lượng Slide dự kiến:** 45 - 46 slides
- **Theme LaTeX:** Madrid, tỷ lệ 16:9
- **Nguồn tài liệu:** 
  - `docs/buoi_11.md` (Chương 2: Foundational Data Analysis Skills)
  - `TaiLieu/script/audioScript_Day11.txt` (Phép ẩn dụ, Case study thực tế)

## 2. Mục tiêu Bài học (Learning Objectives)
1. Nắm vững cấu trúc Cơ sở Dữ liệu Quan hệ (Bảng, Khóa chính, Khóa ngoại).
2. Hiểu cơ chế hoạt động của các lệnh SQL JOIN (đặc biệt là Left Join trong kiểm toán).
3. Sử dụng các hàm Excel có điều kiện (SUMIFS, COUNTIFS) và PivotTable để phân tích dữ liệu đa chiều.
4. Vận dụng Thống kê Mô tả để phát hiện những bất thường đằng sau giá trị trung bình.
5. Áp dụng trực quan hóa dữ liệu hiệu quả giữa hai giai đoạn: Khám phá và Giải thích.

## 3. Cấu trúc Kịch bản Chi tiết (Khoảng 46 Slides)

### Mở đầu (3 Slides)
1. **Title Slide:** Trí tuệ Nhân tạo cho Kế toán - Buổi 11: Kỹ năng Phân tích Dữ liệu Nền tảng.
2. **Mục tiêu Bài học:** 5 mục tiêu cốt lõi.
3. **Agenda:** Nội dung chính của bài giảng (5 phần).

### Phần 1: Khởi động & Ảo ảnh của Con số Trung bình (4 Slides)
*Dựa trên Case study Super Scooters trong audioScript*
4. **Tình huống Kiểm toán Thực tế:** Chi phí bảo hành trung bình của Super Scooters.
5. **Ảo ảnh 600 USD:** Một con số hoàn hảo trong vùng an toàn ngân sách?
6. **Cú sốc đằng sau con số:** Sự thật về 2 đỉnh chi phí (200 USD và 1.200 USD).
7. **Hành trình Dữ liệu:** Từ Cơ sở Dữ liệu -> Xử lý (Excel/Pivot) -> Thống kê & Trực quan hóa.

### Phần 2: Cơ sở Dữ liệu Quan hệ & Nghệ thuật Kết nối (10 Slides)
8. **Nguồn gốc Dữ liệu Doanh nghiệp:** Cơ sở dữ liệu quan hệ (Relational Database) là gì?
9. **Thành phần cơ bản:** Bảng (Table), Hàng (Row) và Cột (Column).
10. **Khóa chính (Primary Key):** "Căn cước công dân" của Dữ liệu.
11. **Khóa ngoại (Foreign Key):** Chiếc mỏ neo liên kết thông tin.
12. **Bài toán Dư thừa Thông tin:** Tại sao phải chia ra nhiều bảng? (Ví dụ: Khấu hao tài sản).
13. **Truy xuất Dữ liệu:** Vai trò của SQL trong việc kết nối các Bảng.
14. **Bốn phương pháp Kết nối (JOIN):** Inner, Left, Right, Full Join.
15. **Inner Join:** Chỉ lấy phần giao (Bức tranh hoàn hảo nhưng thiếu sót).
16. **Left Join trong Kiểm toán:** Tìm kiếm những "Kẻ cắp tàng hình".
17. **Sự thật về giá trị NULL:** NULL không phải là số 0 - Báo động nhà cung cấp ma.

### Phần 3: Chế ngự Dữ liệu Khổng lồ với Các Hàm Tính toán (8 Slides)
18. **Từ SQL sang Excel:** Đối mặt với bức tranh hàng trăm ngàn dòng.
19. **Hạn chế của các hàm cơ bản:** SUM và COUNT không đủ sức mạnh.
20. **Nhu cầu phân tích Đa chiều:** Khi Ban lãnh đạo đặt ra nhiều điều kiện khắt khe.
21. **Các hàm có điều kiện:** SUMIF, COUNTIF và SUMIFS.
22. **Cơ chế hoạt động của SUMIFS:** "Người bảo vệ kho dữ liệu khắt khe".
23. **Quy trình duyệt Giao dịch:** Soi từng giao dịch, thỏa mãn tất cả mới được qua.
24. **Ưu điểm:** Loại bỏ thao tác lọc thủ công, đảm bảo tính chính xác.
25. **Hạn chế:** Cần phải biết trước câu hỏi và điều kiện chính xác.

### Phần 4: Pivot Table & Tư duy Phân tích Khám phá (7 Slides)
26. **Câu hỏi mở từ Sếp:** "Cho tôi xem bức tranh tổng quan thì sao?"
27. **Giải pháp tối thượng:** PivotTable - Không cần viết một dòng công thức.
28. **Năm vùng cốt lõi:** Filters, Columns, Rows, Values.
29. **Phép màu của Drag & Drop:** Kéo và thả để thiết kế báo cáo.
30. **Quy mô và Tốc độ:** Tóm tắt nửa triệu dòng thành báo cáo 10 dòng trong 10 giây.
31. **Bảng điều khiển Tương tác:** Sử dụng Drill-down và Slicers.
32. **Cạm bẫy của sự Gọn gàng:** PivotTable có thể che lấp những chi tiết bất thường.

### Phần 5: Thống kê Mô tả & Vạch trần Sự thật (7 Slides)
33. **Bước qua Ảo ảnh của Mean (Trung bình):** Tại sao Mean dễ bị bóp méo?
34. **Đo lường độ phân tán:** Phương sai (Variance) & Độ lệch chuẩn (Standard Deviation).
35. **Hình dáng phân bổ:** Độ lệch (Skewness) & Độ nhọn (Kurtosis).
36. **Ngọn núi hay Lưng lạc đà?** (Bi-modal distribution).
37. **Lật tẩy Ảo ảnh 600 USD:** Số trung bình nằm giữa 2 cái bướu của con lạc đà.
38. **Độ lệch chuẩn như một "Hệ thống Radar".**
39. **Cảnh báo Ngoại lệ (Outliers):** Nhấp nháy đỏ khi giao dịch vượt ranh giới an toàn.

### Phần 6: Trực quan hóa Dữ liệu - Đôi mắt của AI (5 Slides)
40. **Giới hạn của Não bộ:** Không thể đọc 500 ngàn dòng bằng mắt thường.
41. **Biểu đồ phân tán (Scatter Plot):** Chuyển gánh nặng sang vỏ não thị giác (Tìm điểm cô lập).
42. **Hai giai đoạn trực quan hóa:** Khám phá (Exploratory) vs. Giải thích (Explanatory).
43. **Bảng điều tra vs. Bản trình chiếu:** Từ lộn xộn, thử nghiệm đến thông điệp sắc nét.
44. **Chọn đúng Biểu đồ:** Đừng dùng nhầm Bar Chart cho Histogram.

### Tổng kết (2 Slides)
45. **Tổng kết bài học:** Hệ tư duy mới (Cơ sở dữ liệu -> Phân tích -> Trực quan hóa).
46. **Q&A:** Giải đáp thắc mắc.

## 4. Các "Ẩn dụ" (Metaphors) Nổi bật sẽ dùng trong Slide
- **Căn cước công dân & Mỏ neo:** Giải thích Khóa chính (Primary Key) và Khóa ngoại (Foreign Key).
- **Kẻ cắp tàng hình & Giá trị NULL:** Vai trò của Left Join để phát hiện nhà cung cấp ma.
- **Người bảo vệ khắt khe:** Chức năng của hàm SUMIFS duyệt qua các điều kiện lọc.
- **Lưng Lạc đà (Bimodal):** Minh họa dữ liệu phân bổ hai đỉnh, lật tẩy con số trung bình ảo.
- **Hệ thống Radar an ninh:** Vai trò của Độ lệch chuẩn trong việc phát hiện Ngoại lệ (Outliers).
- **Bảng điều tra của thám tử vs. Bản trình chiếu của sếp:** Hai giai đoạn trực quan hóa (Exploratory vs. Explanatory).

## 5. Các bước Tiếp theo (Next Steps)
- Dựa trên bản kế hoạch này, sinh file kịch bản tạo beamer: `build_beamer_day11.py`.
- Tích hợp nội dung, bullet points logic và code build LaTeX.
- Sinh ra file `Slide_AIAcc_Day11.pdf` đạt số lượng ~45 - 46 frames chuẩn xác.
