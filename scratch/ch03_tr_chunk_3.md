### Các Ví dụ Phân tích Chẩn đoán (Diagnostic Analyses Examples)

Có bốn loại phân tích chẩn đoán phổ biến: phát hiện điểm bất thường (anomaly detection), tương quan (correlation), phát hiện khuôn mẫu (pattern detection), và phân tích xu hướng (trend analysis).

Sử dụng các câu hỏi của Super Scooters trong Hình minh họa 3.11, hãy kiểm tra các câu hỏi phụ sau:
1. Có những khuôn mẫu nhận diện được nào trong khối lượng bán hàng của mẫu Celeritas không?
2. Có những khuôn mẫu bất thường nào trong doanh số của mẫu Celeritas tại địa điểm Seattle không?

Biểu đồ đường (line charts) có thể xác định các khuôn mẫu bằng cách tiết lộ các mô hình lặp lại trong dữ liệu. Hình minh họa 3.12 cho thấy doanh số của Celeritas theo tháng của từng năm.

![ILLUSTRATION 3.12](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.12.png)

Các biểu đồ đường trong Hình minh họa 3.12 dường như không cho thấy một khuôn mẫu nào trong khối lượng bán hàng cho mẫu Celeritas. Tuy nhiên, biểu đồ đường này hiển thị tất cả các địa điểm, và các phân tích trước đó đã tiết lộ rằng địa điểm Seattle có sự sụt giảm doanh số của Celeritas.

Khuôn mẫu bán hàng trong các năm 2023 và 2025 chỉ ra rằng doanh số nhìn chung tăng từ quý đầu tiên đến quý thứ ba:
- Vào năm 2023 có một sự sụt giảm doanh số trong quý 4, nhưng năm 2024 và 2025 lại chứng kiến sự gia tăng trong doanh số quý 4.
- Tuy nhiên, doanh số năm 2025 thấp hơn doanh số năm 2024, và đã có một đợt sụt giảm lớn trong quý 3.

Để hiểu tại sao doanh số năm 2025 lại thấp hơn và tại sao lại có sự sụt giảm trong quý 3 năm 2025, chúng ta phải phân tích thêm khối lượng bán hàng theo địa điểm.

Hình minh họa 3.13 hiển thị một phân tích kiểm tra doanh số bán hàng hàng tháng của Celeritas tại địa điểm Seattle.

![ILLUSTRATION 3.13](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.13.png)

Biểu đồ cột về doanh số của Celeritas trong suốt năm 2025 cho thấy một điều và gợi ý một điều khác:
- Trong năm 2025 có một vài tháng không có doanh số.
- Đây có thể là một yếu tố góp phần vào sự sụt giảm trong tổng doanh số của Celeritas trong năm 2025.

Bước tiếp theo sẽ là hỏi ban quản lý xem điều gì đã xảy ra vào tháng 3 năm 2025 dẫn đến sáu tháng không có bất kỳ doanh số nào của mẫu Celeritas. Điều này cũng làm dấy lên các câu hỏi bổ sung cần điều tra:
- Có phải doanh số chỉ giảm ở địa điểm Seattle không?
- Mẫu Celeritas có phải là sản phẩm duy nhất có doanh số giảm không?

Quá trình điều tra này được gọi là phân tích dữ liệu khám phá (exploratory data analysis), mà bạn sẽ được học ở phần sau của khóa học này.

---

### Ứng dụng 3.3 (Apply It 3.3)
**Xác định Rủi ro Sai sót Trọng yếu của Bán hàng (Determine the Risk of Material Misstatement of Sales)**

> **Data** **Kiểm toán (Auditing)** Trong suốt cuộc kiểm toán báo cáo tài chính của Best Bakes Bakery, bạn được yêu cầu xác định xem có những thay đổi bất thường nào về doanh thu so với các năm trước có thể ảnh hưởng đến rủi ro sai sót trọng yếu hay không. Bạn đã được cung cấp một đoạn trích các giao dịch trong một file Excel để bạn biết được những dữ liệu nào có sẵn.

![Apply It 3.3](../TaiLieu/textbookForPractice/Figures/Ch_03/Apply%20It%203.3.png)

**Yêu cầu:**
1. Mục tiêu của phân tích là gì?
2. Phát triển ba câu hỏi phù hợp với mục tiêu, và nêu ra các thước đo cần thiết để trả lời chúng.
3. Bạn sẽ sử dụng những phân tích nào để trả lời ba câu hỏi này?

**GIẢI PHÁP (SOLUTION)**
1. Mục tiêu là phân tích các giao dịch từ năm 2022 đến năm 2025 đối với những thay đổi bất thường. Phân tích này sẽ cung cấp cho kiểm toán viên thông tin để xác định bản chất, thời gian và phạm vi của các thủ tục kiểm toán.
2. 
| **Câu hỏi (Questions)** | **Thước đo (Measures)** |
| --- | --- |
| 1. Có bất kỳ thay đổi bất thường nào trong tổng doanh thu qua các năm 2022–2025 không? | Tổng doanh số hàng quý |
| 2. Có bất kỳ thay đổi bất thường nào trong tổng doanh thu qua các năm theo địa điểm không? | Tổng doanh số hàng quý |
| 3. Có bất kỳ thay đổi bất thường nào trong doanh thu theo sản phẩm qua các năm không? | Khối lượng bán hàng theo sản phẩm |

3. Các phân tích điểm bất thường (anomaly), khuôn mẫu (pattern), và xu hướng (trend) có thể được chuẩn bị để trả lời các câu hỏi này.

---

## 3.4 Các Mục tiêu Dự đoán (Predictive Objectives) là gì?

**MỤC TIÊU HỌC TẬP 4 (LEARNING OBJECTIVE 4)**
**Trình bày cách phát triển các câu hỏi dự đoán.**

Cho đến nay, bạn đã học được cách phát triển các câu hỏi mô tả để tìm hiểu những gì đã xảy ra trong quá khứ và các câu hỏi chẩn đoán để hiểu lý do tại sao. Sẽ ra sao nếu bạn muốn biết những gì có thể xảy ra trong tương lai? Trong trường hợp này, bạn sẽ hỏi các câu hỏi dự đoán (predictive questions).

### Phát triển Các Câu hỏi Dự đoán (Develop Predictive Questions)

Khi đưa ra các quyết định cho vay, các ngân hàng sử dụng thông tin lịch sử về việc liệu một người đi vay tiềm năng có thanh toán các hóa đơn một cách nhất quán và đúng hạn hay không để dự đoán xem liệu họ có tiếp tục làm như vậy hay không. Theo cách tương tự, phân tích dự đoán (predictive analytics) sử dụng dữ liệu trong quá khứ và hiện tại để tạo ra các mô hình (models) để các doanh nghiệp có thể đưa ra các dự đoán.

Việc sử dụng phân tích dự đoán không phải là mới trong nghề kế toán, nhưng do sự sẵn có của dữ liệu và các công cụ phần mềm để thực hiện phân tích dự đoán đã gia tăng, nên việc thực hiện các phân tích này trong mọi lĩnh vực của kế toán cũng gia tăng theo:
- Kế toán tài chính có thể xác định các xu hướng trong doanh số bán hàng hoặc chi phí.
- Kế toán chi phí có thể dự đoán chi phí, lập các dự báo, và đánh giá các yếu tố dẫn dắt chi phí (cost drivers).
- Kiểm toán viên xác định các sai sót trọng yếu tiềm ẩn bằng cách sử dụng phân tích dự đoán.
- Kế toán thuế có thể sử dụng phân tích dự đoán cho việc lập kế hoạch thuế.
