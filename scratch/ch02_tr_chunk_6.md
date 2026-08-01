## Ôn tập Chương và Thực hành (Chapter Review and Practice)

### Tóm tắt Mục tiêu Học tập (Learning Objectives Review)

❶ **Mô tả cách dữ liệu được lưu trữ trong và trích xuất từ các cơ sở dữ liệu quan hệ.**
Dữ liệu được sử dụng trong các phân tích dữ liệu kế toán thường được lưu trữ trong một cơ sở dữ liệu quan hệ (relational database). Việc truy xuất dữ liệu từ một cơ sở dữ liệu đòi hỏi phải hiểu cách các bảng trong một cơ sở dữ liệu quan hệ được cấu trúc:
- Dữ liệu được lưu trữ trong các bảng (tables), bao gồm các trường (fields) và các bản ghi (records). Các trường là các cột thể hiện các đặc điểm về mỗi bản ghi được lưu trữ trong các cột của tập dữ liệu. Các bản ghi là dữ liệu nằm trong các hàng đại diện cho các trường hợp của hiện tượng đang được ghi lại trong tập dữ liệu.
- Các bảng có một khóa chính (primary key), đây là một giá trị duy nhất cho mỗi hàng trong bảng. Thường thì một bảng sẽ có một khóa ngoại (foreign key). Khóa ngoại là một cột khóa chính được lặp lại từ một bảng khác. Các khóa ngoại giúp có thể kết nối (join) dữ liệu được lưu trữ ở các bảng khác nhau.
- Để phân tích dữ liệu được lưu trữ trong nhiều hơn một bảng, hãy kết nối dữ liệu từ nhiều bảng. Có các kết nối trong (inner joins), kết nối phải (right joins), kết nối trái (left joins), hoặc kết nối toàn bộ (full joins), mỗi loại truy xuất dữ liệu theo các cách khác nhau. Lệnh kết nối được chọn phải phù hợp với câu hỏi phân tích dữ liệu đang được đặt ra.

❷ **Giải thích cách các hàm giúp trả lời các câu hỏi phân tích dữ liệu.**
Phân tích dữ liệu bao gồm việc thực hiện các phép tính:
- Các hàm (functions) là các công thức được xác định trước để thực hiện các phép tính được sử dụng thường xuyên.
- Các hàm phổ biến nhất bao gồm AVERAGE, AVERAGEIF, AVERAGEIFS, COUNT, COUNTIF, COUNTIFS, SUM, SUMIF, và SUMIFS.

❸ **Minh họa cách các pivot tables tổ chức và lọc dữ liệu.**
Tổ chức dữ liệu là quá trình sắp xếp lại dữ liệu để làm cho nó dễ hiểu hơn hoặc để trả lời một câu hỏi cụ thể:
- Sắp xếp (Sort), lọc (filter), và cắt lớp (slice) là các công cụ phổ biến để tổ chức lại dữ liệu trong một bảng tính nhằm trả lời các câu hỏi.
- Pivot tables sắp xếp lại dữ liệu một cách hiệu quả trong một bảng tính để tạo ra các tóm tắt tùy chỉnh của các thông tin chính.

❹ **Nhận diện các thước đo mô tả được sử dụng để thực hiện phân tích dữ liệu.**
Các kỹ năng phân tích dữ liệu cốt lõi cho phân tích mô tả là thống kê mô tả và phân tích tương quan:
- Các thước đo vị trí (measures of location) bao gồm số trung bình (mean), số trung vị (median), và yếu vị (mode).
- Các thước đo phân phối (measures of distribution) bao gồm phương sai (variance) và độ lệch chuẩn (standard deviation).
- Các thước đo hình dạng (measures of shape) bao gồm độ lệch (skewness) và độ nhọn (kurtosis).
- Các thước đo tương quan (correlation measures) có thể giúp xác định các mối quan hệ giữa các dữ liệu. Sự tương quan cho các biến liên tục được đo bằng hệ số tương quan. Thước đo này là một giá trị số giữa −1 và +1. Giá trị càng gần với giá trị tuyệt đối của 1, thì sự tương quan càng mạnh.

❺ **Tóm tắt cách trực quan hóa dữ liệu khám phá và giải thích dữ liệu.**
Trực quan hóa dữ liệu là một trong những lĩnh vực phát triển nhanh nhất của phân tích dữ liệu trong nghề kế toán:
- Trực quan hóa dữ liệu (Data visualization) là sự trình bày dữ liệu và thông tin bằng đồ họa. Trực quan hóa dữ liệu có thể giúp nhanh chóng hiểu được các tập dữ liệu lớn.
- Trực quan hóa dữ liệu khám phá (Exploratory data visualization) kiểm tra dữ liệu để phát hiện ra các mô hình (patterns), xu hướng (trends), hoặc điểm bất thường (anomalies). Trực quan hóa dữ liệu giải thích (Explanatory data visualization) sử dụng các công cụ và kỹ thuật trực quan hóa dữ liệu để truyền đạt kết quả phân tích dữ liệu.
- Lựa chọn đúng trực quan hóa là sự kết hợp giữa việc xem xét mục đích của phân tích và quyết định xem mục tiêu là để thể hiện sự cấu thành, các mối quan hệ, sự phân phối, các xu hướng, hay các so sánh.

---

### Ôn tập Thuật ngữ Chính (Key Terms Review)
- Các thuộc tính (Attributes)
- Dữ liệu phân loại (Categorical data)
- Hệ số độ nhọn (Coefficient of kurtosis - CK)
- Hệ số bất đối xứng (Coefficient of skewness - CS)
- Phân tích tương quan (Correlation analysis)
- Hệ số tương quan (Correlation coefficient)
- Tổ chức dữ liệu (Data organization)
- Trực quan hóa dữ liệu (Data visualization)
- Các chiều dữ liệu (Dimensions)
- Trực quan hóa dữ liệu giải thích (Explanatory data visualization)
- Trực quan hóa dữ liệu khám phá (Exploratory data visualization)
- Khóa ngoại (Foreign key)
- Phân phối tần số (Frequency distribution)
- Các hàm (Functions)
- Biểu đồ tần suất (Histogram)
- Kết nối (Join)
- Độ nhọn (Kurtosis)
- Số trung bình (Mean)
- Các thước đo xu hướng tập trung (Measures of central tendency)
- Các thước đo độ phân tán (Measures of dispersion)
- Các thước đo vị trí (Measures of location)
- Các thước đo hình dạng (Measures of shape)
- Số trung vị (Median)
- Yếu vị (Mode)
- Giá trị rỗng (Null value)
- Bảng tổng hợp (Pivot table)
- Khóa chính (Primary key)
- Truy vấn (Query)
- Cơ sở dữ liệu quan hệ (Relational database)
- Độ lệch/Bất đối xứng (Skewness)
- Bộ cắt lọc dữ liệu (Slicers)
- Cắt lớp dữ liệu (Slicing)
- Độ lệch chuẩn (Standard deviation)
- Ngôn ngữ Truy vấn Có cấu trúc (Structured Query Language - SQL)
- Bảng (Table)
- Phương sai (Variance)

---

### Các Bài Hướng dẫn Chi tiết (How To Walk-Throughs)

#### HOW TO 2.1
**Định dạng và Tùy chọn Show Values As trong PivotTables**

Các giá trị trong một Excel PivotTable có thể được định dạng bằng hộp thoại Value Field Settings.
**Những gì bạn cần:** > **Data** Tệp dữ liệu How To 2.1.

**BƯỚC 1:** Nhấp vào Number Format. Hộp thoại Format Cells giống như trong dải công cụ Home sẽ xuất hiện (Hình minh họa 2.64).

**HÌNH MINH HỌA 2.64 (ILLUSTRATION 2.64) Định dạng Các Giá trị trong một PivotTable**

![ILLUSTRATION 2.64](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.64.png)

**BƯỚC 2:** Bạn cũng có thể sử dụng tùy chọn **Show Values As** trong hộp thoại Value Field Settings để thêm một phép tính nhanh cho các giá trị:
- Nhấp vào Show Values As sẽ hiển thị một danh sách thả xuống gồm các phép tính được tích hợp sẵn.
- Hình minh họa 2.65 hiển thị các giá trị dưới dạng tỷ lệ phần trăm của tổng số (grand total).

**HÌNH MINH HỌA 2.65 (ILLUSTRATION 2.65) Các Tùy chọn Show Values As**

![ILLUSTRATION 2.65](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.65.png)

**BƯỚC 3:** Tổng Doanh thu (Sum of Revenue) có thể nhanh chóng được đổi thành Phần trăm của Tổng Doanh thu (Percent of Total Revenue) bằng cách chọn **% of Grand Total** trong hộp thoại (Hình minh họa 2.66).

**HÌNH MINH HỌA 2.66 (ILLUSTRATION 2.66) Các Tùy chọn Show Values As**

![ILLUSTRATION 2.66](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.66.png)

---

#### HOW TO 2.2
**Tạo một Biểu đồ Cột (Bar Chart) Bằng Tableau**

Cùng một trực quan hóa từ Hình minh họa 2.63 có thể được tạo bằng cách sử dụng Tableau.
**Những gì bạn cần:** > **Data** Tệp dữ liệu How To 2.2.

![ILLUSTRATION 2.63](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.63.png)
![ILLUSTRATION 2.63_1](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.63_1.png)

**BƯỚC 1:** Thêm các trường cho trực quan hóa vào vùng làm việc (canvas):
- Mở tệp và nhấp vào **Sheet 1** ở dưới cùng của màn hình (Hình minh họa 2.67).
- Việc này sẽ mở ra một bảng tính mới cho một trực quan hóa. Nhấp vào trường cần trực quan hóa và kéo nó vào dòng column hoặc row:
   - Kéo `Sold Date` vào **Columns**, `Model` vào **Rows**, và `Gross Sales` vào **Text**.
   - Bạn cũng có thể kéo nó đến vị trí mong muốn trong vùng làm việc ở khu vực có nhãn *Drop field here*.

**HÌNH MINH HỌA 2.67 (ILLUSTRATION 2.67) Vùng làm việc Trực quan hóa của Tableau**

![ILLUSTRATION 2.67](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.67.png)

Hình minh họa 2.68 hiển thị kết quả khi `Year` được kéo vào Columns, `Model` vào Rows, và `Gross Sales` vào Text.

**HÌNH MINH HỌA 2.68 (ILLUSTRATION 2.68) Vùng làm việc Trực quan hóa Tableau: Bước 1**

![ILLUSTRATION 2.68](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.68.png)

**BƯỚC 2:** Tạo một biểu đồ thanh (bar chart). Chú ý rằng Tableau mặc định ở định dạng Table.
- Nhấp vào **Show Me** ở góc trên cùng bên phải của màn hình.
- Chọn biểu đồ cột xếp cạnh nhau (side-by-side column chart). Lưu ý rằng bất kỳ trực quan hóa nào được làm sáng (highlighted) đều có thể được chọn (Hình minh họa 2.69).

**HÌNH MINH HỌA 2.69 (ILLUSTRATION 2.69) Các Tùy chọn Show Me của Tableau**

![ILLUSTRATION 2.69](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.69.png)

Hình minh họa 2.70 là kết quả của việc chọn tùy chọn trực quan hóa biểu đồ cột.

**HÌNH MINH HỌA 2.70 (ILLUSTRATION 2.70) Trực quan hóa Bar Chart của Tableau**

![ILLUSTRATION 2.70](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.70.png)

**BƯỚC 3:** Đặt tiêu đề cho trực quan hóa:
- Nhấp đúp vào tiêu đề **Sheet 1** và chọn **Edit Title**.
- Đổi tiêu đề bằng cách gõ "Gross Sales by Model" (Hình minh họa 2.71).

**HÌNH MINH HỌA 2.71 (ILLUSTRATION 2.71) Tableau Bar Chart: Thêm một Tiêu đề**

![ILLUSTRATION 2.71](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.71.png)

**BƯỚC 4:** Định dạng trục (axis):
- Để định dạng trục Gross sales và đơn vị đô la tính bằng hàng ngàn (thousands), nhấp vào mũi tên chỉ xuống trong SUM (Gross Sales).
- Chọn **Format** và nhấp vào tab **Axis** (Hình minh họa 2.72).

**HÌNH MINH HỌA 2.72 (ILLUSTRATION 2.72) Tableau Bar Chart: Định dạng Trục**

![ILLUSTRATION 2.72](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.72.png)

**BƯỚC 5:** Đổi hiển thị tiền tệ (currency) thành hàng ngàn:
- Một khi ở trong hộp Format, chọn **Numbers** và **Currency (Custom)**.
- Chọn **Display Units** để đổi các con số được hiển thị thành hàng ngàn.
- Lưu ý, chúng ta cũng đã thay đổi số chữ số thập phân (decimal places) thành 0 (Hình minh họa 2.73).

**HÌNH MINH HỌA 2.73 (ILLUSTRATION 2.73) Tableau Bar Chart: Thay đổi Hiển thị Tiền tệ**

![ILLUSTRATION 2.73](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.73.png)
