Hãy tiếp tục với ví dụ Super Scooters để minh họa. Hình minh họa 3.6 cung cấp thông tin tài chính cho các năm từ 2023 đến 2025.

![ILLUSTRATION 3.6](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.6.png)

Mặc dù doanh số (sales) và doanh thu thuần (net revenue) đã tăng lên, hai trong số các mẫu mã lại có doanh thu thuần sụt giảm (Hình minh họa 3.7).

![ILLUSTRATION 3.7](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.7.png)

Super Scooters muốn hiểu rõ sự sụt giảm doanh thu thuần của các mẫu Celeritas và Kicks. Họ nên đặt ra những câu hỏi gì cho dữ liệu? Những thước đo (measures) nào có thể được sử dụng để trả lời các câu hỏi đó?

![ILLUSTRATION 3.8](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.8.png)

Hãy chú ý xem tất cả các câu hỏi đều liên quan đến mục tiêu của phân tích như thế nào. Các câu hỏi ban đầu (initial questions) là ổn nhưng còn rộng. Các câu hỏi phụ (sub-questions) trong cột thứ hai sẽ thu hẹp trọng tâm. Hơn nữa, mỗi câu hỏi đều có thể đo lường được, như được chỉ ra bởi các thước đo ở cột cuối cùng. Một khi các câu hỏi mô tả chi tiết được phác thảo, đã đến lúc xác định dữ liệu và phương pháp phân tích cần thiết để trả lời chúng.

### Các Ví dụ Phân tích Mô tả (Descriptive Analyses Examples)

Các phân tích thường được sử dụng để trả lời các câu hỏi mô tả bao gồm các thước đo về tần suất (frequency), vị trí (location), độ phân tán (dispersion) và tỷ lệ phần trăm (percentages):
- Các thước đo **tần suất** giúp chúng ta hiểu các danh mục của dữ liệu.
- Các thước đo **vị trí** (trung bình, trung vị, yếu vị - mean, median, mode) cho thấy các quan sát trung bình trong một tập dữ liệu.
- Các thước đo **độ phân tán** (giá trị nhỏ nhất, giá trị lớn nhất, khoảng, phương sai, và độ lệch chuẩn - minimum, maximum, range, variance, standard deviation) cho thấy có bao nhiêu sự biến thiên giữa các quan sát trong tập dữ liệu.
- Các thước đo **thay đổi tỷ lệ phần trăm** (percentage change) so sánh kết quả với các kỳ trước và tỷ lệ phần trăm của tổng số.

> **Data** Hãy trình bày một ví dụ sử dụng các câu hỏi được xác định trong Hình minh họa 3.8.

Hình minh họa 3.8 cung cấp các ví dụ về cả các câu hỏi ban đầu và các câu hỏi phụ (nói cách khác, các câu hỏi chi tiết hơn).

Có thể khám phá xem tổng doanh số (gross sales) đã giảm đối với mẫu Celeritas hay chưa bằng cách sử dụng thước đo tổng doanh số. Có một số phân tích khác nhau có thể xác định xem tổng doanh số đã giảm hay chưa:
- Số tiền tổng doanh số (Gross sales dollars): thước đo tổng thể (total measure)
- Khối lượng bán hàng (Sales volume): thước đo tổng thể
- Giá bán bình quân một đơn vị (Average unit sales price)

Một bảng PivotTable trong Microsoft Excel được tạo với dữ liệu của Super Scooter chuẩn bị cho một phân tích mô tả cho câu hỏi này (Hình minh họa 3.9).

![ILLUSTRATION 3.9](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.9.png)

Dữ liệu bán hàng xác nhận rằng mẫu Celeritas và Kicks đều suy giảm từ năm 2024 đến năm 2025. Thú vị là, cả khối lượng bán hàng và giá trung bình đều giảm, vì vậy sự suy giảm là sự kết hợp của cả khối lượng và giá cả. Bước tiếp theo là trả lời câu hỏi phụ tiếp theo: Doanh số có giảm ở tất cả các địa điểm không?

Hình minh họa 3.10 cho thấy sự thay đổi trong số tiền tổng doanh số trung bình (average gross sales dollars), đây là một thước đo vị trí. Nó là kết quả của một phân tích mô tả trong Tableau cho thấy sự thay đổi trong tổng doanh số từ năm 2023 đến 2025 theo địa điểm cho mẫu Celeritas. Đây là một bảng đánh dấu (highlight table) trong đó màu tối hơn báo hiệu mức giảm lớn hơn. (**Data** Xem mục How To 3.1 ở cuối chương này để tìm hiểu cách tạo bảng này trong Tableau.)

![ILLUSTRATION 3.10](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.10.png)

Địa điểm Seattle có mức giảm tổng doanh số lớn nhất từ năm 2024 ở mức 140.206 đô la. Dallas có mức giảm lớn thứ hai ở mức 106.783 đô la. Tuy nhiên, rõ ràng là doanh số đã giảm ở tất cả các địa điểm. Bước tiếp theo là xác định lý do tại sao doanh số lại giảm, điều này sẽ yêu cầu phân tích chẩn đoán (diagnostic analytics).

---

### Ứng dụng 3.2 (Apply It 3.2)
**Mô tả Hành vi Mua hàng của Khách hàng (Describe Customers' Buying Behavior)**

> **Data** **Kế toán Tài chính (Financial Accounting)** Best Bakes Bakery muốn hiểu rõ hơn về hành vi mua hàng của những khách hàng hàng đầu của họ. Bạn đã được cung cấp các giao dịch bán hàng cho các năm 2022 đến 2025. Một đoạn trích từ file (dữ liệu) theo sau.

![Apply It 3.2](../TaiLieu/textbookForPractice/Figures/Ch_03/Apply%20It%203.2.png)

**Yêu cầu:**
1. Mục tiêu của phân tích là gì?
2. Phát triển ba câu hỏi phù hợp với mục tiêu, và mô tả các thước đo (measures) cần thiết để trả lời các câu hỏi đó.
3. Bạn sẽ sử dụng những phân tích nào để trả lời những câu hỏi này?

**GIẢI PHÁP (SOLUTION)**
1. Mục tiêu của phân tích là xác định các khách hàng hàng đầu và đánh giá những sản phẩm họ mua.
2. 
| **Câu hỏi (Questions)** | **Thước đo (Measures)** |
| --- | --- |
| 1. Năm khách hàng hàng đầu là ai? | Tổng doanh số, khối lượng bán hàng, tỷ suất lợi nhuận (profit margin) |
| 2. Năm sản phẩm bán chạy nhất là gì? | Khối lượng bán hàng, tổng doanh số |
| 3. Khách hàng chi tiêu theo mô hình nào đối với năm khách hàng hàng đầu? | Khối lượng bán hàng, tổng doanh số |

3. Các phân tích cho ba câu hỏi:
   1. **Phân tích mô tả:** Năm khách hàng hàng đầu theo năm cho mỗi thước đo so với mức trung bình của tất cả các khách hàng.
   2. **Phân tích mô tả:** Năm sản phẩm bán chạy nhất theo năm cho mỗi thước đo so với mức trung bình của tất cả các sản phẩm.
   3. **Phân tích mô tả:** Phân tích cho thấy doanh số bán hàng theo tháng hoặc quý của mỗi năm cho năm khách hàng hàng đầu. Có thể sử dụng biểu đồ thanh (bar chart) hoặc biểu đồ đường (line chart).

---

## 3.3 Các Mục tiêu Chẩn đoán (Diagnostic Objectives) là gì?

**MỤC TIÊU HỌC TẬP 3 (LEARNING OBJECTIVE 3)**
**Trình bày cách phát triển các câu hỏi chẩn đoán.**

Khi chúng ta đã biết những gì đã xảy ra, bước tiếp theo là xác định tại sao. Các câu hỏi chẩn đoán (diagnostic questions) được xây dựng dựa trên các phân tích mô tả và khám phá thêm dữ liệu để tìm ra nguyên nhân của kết quả. Phân tích chẩn đoán (diagnostic analytics) thực hiện điều này bằng cách tìm kiếm các điểm bất thường (anomalies), các mối tương quan (correlations), các khuôn mẫu (patterns), hoặc các xu hướng (trends).

### Phát triển Các Câu hỏi Chẩn đoán (Develop Diagnostic Questions)

Các câu hỏi chẩn đoán xác định một vấn đề hoặc rắc rối để hiểu tại sao một kết quả lại xảy ra. Hình minh họa 3.11 cho thấy các câu hỏi chẩn đoán dựa trên kết quả phân tích mô tả doanh số bán hàng của Super Scooters ở phần trước.

![ILLUSTRATION 3.11](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.11.png)

Tại sao doanh số lại giảm, và cụ thể hơn, tại sao địa điểm Seattle lại có mức giảm lớn nhất? Các câu hỏi và câu hỏi phụ đào sâu hơn vào sự sụt giảm doanh số bằng cách hỏi về các điểm bất thường và các mô hình bất thường. Bây giờ, hãy xác định dữ liệu và các phân tích sẽ trả lời các câu hỏi này.
