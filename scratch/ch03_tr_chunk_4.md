Giả sử Super Scooters đang lập ngân sách (budget) cho năm tới:
- Họ muốn dự đoán doanh thu cho năm 2026 với giả định khối lượng bán hàng tăng 10%.
- Họ cũng tin rằng chi phí bảo hành sẽ tăng 10%.
- Cuối cùng, họ đang xem xét việc ngừng sản xuất mẫu Celeritas và muốn biết liệu điều đó có làm thay đổi doanh thu dự đoán hay không.

Mục tiêu tổng thể của phân tích dữ liệu là gì? Super Scooters nên đặt ra những câu hỏi nào để đáp ứng mục tiêu đó?

Khi xác định các câu hỏi dự đoán, sẽ rất hữu ích nếu hỏi: "Tôi muốn làm gì với câu trả lời?" Hình minh họa 3.14 cho thấy mục tiêu tổng thể của việc dự đoán doanh thu cho năm 2026, câu hỏi ban đầu, cộng với các câu hỏi phụ cụ thể.

![ILLUSTRATION 3.14](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.14.png)

Cũng giống như tất cả các câu hỏi, các câu hỏi dự đoán nên liên quan đến mục tiêu, cụ thể, có thể đo lường được, và phải sử dụng dữ liệu và phân tích thích hợp để trả lời chúng.

### Các Ví dụ Phân tích Dự đoán (Predictive Analyses Examples)

Hai phân tích phổ biến trả lời các câu hỏi dự đoán là các đường xu hướng (trendlines) và phân tích hồi quy (regression analysis).*(2)*

*(2) Có nhiều phương pháp phân tích dự đoán khác, chẳng hạn như trí tuệ nhân tạo (artificial intelligence), nằm ngoài phạm vi của chương này.*

#### Đường xu hướng (Trendlines)

Các đường xu hướng cho thấy mối quan hệ chức năng cơ bản của dữ liệu:
- Một mối quan hệ chức năng (functional relationship) là tác động của một biến độc lập (independent variable) lên một biến phụ thuộc (dependent variable).
- Một hàm tuyến tính (linear function) cho thấy sự tăng hoặc giảm đều đặn trên phạm vi của biến độc lập.

Công cụ Trendline của Excel có thể giúp xác định xem dữ liệu có tuân theo một hàm tuyến tính hay không. Hãy nhớ rằng Super Scooters tin rằng chi phí bảo hành sẽ tăng 10%. Hơn nữa, chi phí bảo hành được cho là bị thúc đẩy bởi doanh số bán hàng.

![ILLUSTRATION 3.15](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.15.png)

Đường xu hướng hỗ trợ một mối quan hệ tuyến tính:
- Khi số tiền tổng doanh số tăng, chi phí bảo hành cũng tăng theo.
- Phương trình cho đường xu hướng được hiển thị trong biểu đồ (y = 0.0431x + 18.632, R² = 0.9064). 

Phương trình đó có thể được sử dụng để dự đoán chi phí bảo hành trong tương lai dựa trên doanh số dự kiến trong đó y là số tiền chi phí bảo hành và x là số tiền tổng doanh số. Ví dụ, nếu tổng doanh số là 2.000 đô la, thì chi phí bảo hành dự kiến sẽ là:
> (0.0431 × 2.000) + 18.632 = $104.83

Nếu chi phí bảo hành tăng 10% như dự kiến của Super Scooters, mô hình dự đoán có thể được điều chỉnh bằng cách tăng 0,0431 lên 10%. Tìm công cụ đường xu hướng Chart Elements trong Excel bằng cách nhấp vào biểu đồ và sau đó nhấp vào dấu cộng (Hình minh họa 3.16).

![ILLUSTRATION 3.16](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.16.png)

Hình minh họa 3.15 cho thấy một đường xu hướng được tạo trong Excel để xác định xem có mối quan hệ tuyến tính giữa doanh số bán hàng và chi phí bảo hành của Super Scooters hay không.

Lưu ý rằng việc nhấp vào dấu cộng ở trên cùng bên trái của biểu đồ bao gồm tùy chọn chọn Trendline, và sau đó là More Options (Hình minh họa 3.17).

![ILLUSTRATION 3.17](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.17.png)

Hộp Format Trendline mở ra cho phép người dùng chọn các hàm số khác (exponential - số mũ, logarithmic - logarit, polynomial - đa thức, power - lũy thừa và moving average - trung bình động). Điều này có thể hữu ích nếu khuôn mẫu của dữ liệu dường như không phải là tuyến tính. Đồng thời, nhấp vào các hộp để hiển thị phương trình và R-square (R bình phương) trên biểu đồ. R-square là thước đo mức độ phù hợp của đường so với dữ liệu. Càng gần 1, độ phù hợp càng tốt. Đường xu hướng trong Hình minh họa 3.16 có R-square rất mạnh là 0,9064. Chúng ta sẽ thảo luận chi tiết hơn về R-square trong phần tiếp theo.

#### Hồi quy Tuyến tính (Linear Regression)

Mặc dù bạn có thể không chuẩn bị một mô hình dự đoán trong suốt sự nghiệp của mình, nhưng bạn có khả năng sẽ sử dụng các mô hình dự đoán hoặc cần diễn giải kết quả đầu ra của chúng. Hồi quy tuyến tính là một công cụ để xây dựng các mô hình toán học và thống kê nhằm giải thích mối quan hệ giữa một biến phụ thuộc và một hoặc nhiều biến độc lập.

Phân tích dự đoán xây dựng các mô hình để dự đoán hoặc hiểu rõ hơn về một hiện tượng. Để tìm ra những yếu tố nào ảnh hưởng đến chi phí bảo hành, chúng ta sẽ xây dựng một mô hình dự đoán chi phí bảo hành.

Việc xây dựng một mô hình đòi hỏi phải xác định các biến sẽ được đưa vào đó:
- Một biến (variable) là một trường dữ liệu được sử dụng để phân tích.
- Một biến phụ thuộc (dependent variable) là thước đo kết quả đầu ra (chi phí bảo hành).
- Các biến độc lập (independent variables) là các biến ảnh hưởng đến biến phụ thuộc (các biến cụ thể mà chúng ta tin rằng có ảnh hưởng đến chi phí bảo hành, chẳng hạn như doanh số bán hàng hoặc số lượng yêu cầu bảo hành).

Hồi quy tuyến tính đơn (simple linear regression) liên quan đến một biến độc lập duy nhất, trong khi hồi quy đa biến (multiple regression) liên quan đến hai hay nhiều biến độc lập. Mục tiêu của mô hình hồi quy là tìm phương trình của đường phù hợp nhất với dữ liệu.

Hãy kiểm tra kết quả đầu ra của một mô hình hồi quy để hiểu cách chúng giúp trả lời các câu hỏi. Là một kế toán viên tại Super Scooters, bạn đang cố gắng ước tính chi phí bảo trì (maintenance expense) cho các thiết bị máy móc vào năm tới. Bạn tin rằng các yếu tố dẫn dắt chi phí đối với chi phí bảo trì là số giờ thiết bị được sử dụng và số lượng yêu cầu sửa chữa. Các biến của mô hình hồi quy sẽ là:
- **Biến phụ thuộc:** Chi phí bảo trì
- **Biến độc lập:** Số giờ máy (machine hours) và số yêu cầu sửa chữa (repair requests)

Dữ liệu lịch sử từ 36 tháng trước đó sẽ được sử dụng để tạo mô hình hồi quy. Kết quả từ mô hình được hiển thị trong Hình minh họa 3.18.

![ILLUSTRATION 3.18](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.18.png)

Hồi quy trong Hình minh họa 3.18 được thực hiện bằng Microsoft Excel. Bản tóm tắt đầu ra được chia thành ba phần.

**Thống kê Hồi quy (Regression Statistics)**
Phần đầu tiên là thống kê hồi quy, hoặc các thước đo thống kê được sử dụng để đánh giá mô hình. Hình minh họa 3.19 cho thấy các số liệu thống kê hồi quy từ Hình minh họa 3.18, cùng với định nghĩa của thống kê và cách diễn giải đối với mô hình hồi quy của Super Scooters.

![ILLUSTRATION 3.19](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.19.png)

**Phân tích Phương sai (ANOVA)**
Phần tiếp theo của đầu ra hồi quy là ANOVA (phân tích phương sai). Hình minh họa 3.20 là phần ANOVA từ mô hình hồi quy.

Trong một hồi quy tuyến tính đa biến như thế này, ý nghĩa (significance) là một kiểm định giả thuyết (hypothesis test) xem liệu mô hình hồi quy có tốt hơn một mô hình không có biến độc lập nào hay không. Nói cách khác, liệu mô hình này có tốt hơn việc không có mô hình nào cả?

![ILLUSTRATION 3.20](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.20.png)

Thông thường, một mô hình được coi là có ý nghĩa nếu thống kê F (Significance F trong Hình minh họa 3.20) nhỏ hơn 0,05:
- Nếu F có ý nghĩa, thì mô hình có thể giải thích được một phần sự biến thiên của biến phụ thuộc. Nói cách khác, nó tốt hơn là không có mô hình nào cả.
- Phân tích ANOVA trong Hình minh họa 3.20 có Significance F là 2.05385E-23. Ký hiệu "E-23" sau 2.05385 đại diện cho ký hiệu khoa học, còn được gọi là ký hiệu số mũ (exponential notation). 2.05385E-23 giống với 0.0000000000000000000000205385. Rõ ràng nó là một số thấp hơn rất nhiều so với 0,05, vì vậy mô hình là có ý nghĩa (significant).

Nói cách khác, các biến độc lập có thể giải thích một phần sự thay đổi của tổng chi phí, do đó mô hình này tốt hơn là không có mô hình nào cả.

**Phương trình Hồi quy (Regression Equation)**
Phần cuối cùng của tóm tắt đầu ra hồi quy cung cấp thông tin để tạo ra phương trình dự đoán biến phụ thuộc:
- Điểm cắt (intercept) và các hệ số (coefficients) của mô hình biểu diễn phương trình của đường thẳng phù hợp nhất với dữ liệu.
- Thống kê chính cần phân tích trong phần này là p-value (giá trị p) cho mỗi biến độc lập. Giống như thống kê F, p-value cung cấp một kiểm định ý nghĩa. Trong trường hợp p-value, đó là kiểm định xem liệu biến độc lập có cải thiện khả năng của mô hình trong việc dự đoán tốt hơn biến phụ thuộc hay không. Một p-value từ 0,05 trở xuống thường được coi là có ý nghĩa (significant).

Hãy sử dụng đầu ra trong Hình minh họa 3.21 để xác định mô hình dự đoán cho chi phí bảo trì máy móc và diễn giải các hệ số.

![ILLUSTRATION 3.21](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.21.png)

Lưu ý rằng p-value cho các biến độc lập đáp ứng được kiểm định nhỏ hơn 0,05 và do đó có ý nghĩa. Mô hình dự đoán sẽ bằng điểm cắt cộng (hoặc trừ nếu số âm) các hệ số của các biến độc lập nhân với các giá trị dự đoán cho các biến đó. Dựa trên mô hình hồi quy trong Hình minh họa 3.21, phương trình để dự đoán tổng chi phí bộ phận mua hàng (purchasing department costs) là:
> $5,252.86 + $3.57 (số giờ máy) + $759.84 (số yêu cầu sửa chữa)

Việc tính toán tổng chi phí dự kiến nếu có 2.250 giờ máy trong một tháng và 8 yêu cầu sửa chữa được thể hiện trong Hình minh họa 3.22. Bắt đầu với điểm cắt và cộng thêm tích số của mỗi hệ số biến độc lập và giá trị dự đoán của biến đó để có được mức dự đoán là $19,364.08 của tổng chi phí bảo trì trong năm.

![ILLUSTRATION 3.22](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.22.png)

Mô hình có thể được diễn giải như sau:
- **Điểm cắt (Intercept):** Điểm cắt không phải lúc nào cũng có diễn giải thực tế. Đó là một kết quả của mô hình thể hiện mức trung bình cho phản ứng khi tất cả các biến độc lập bằng 0. Đó là nơi hàm số của phương trình cắt trục y. Tuy nhiên, ở đây điểm cắt thể hiện số tiền chi phí cố định tồn tại bất kể số giờ máy và yêu cầu sửa chữa.
- **Số giờ máy (Machine hours):** Mỗi giờ thiết bị máy móc được sử dụng làm tăng thêm 3,57 đô la vào tổng chi phí.
- **Yêu cầu sửa chữa (Repair requests):** Mỗi yêu cầu làm tăng thêm 759,84 đô la vào tổng chi phí.

Sử dụng một mô hình giống như trong Hình minh họa 3.22 giúp các doanh nghiệp dự đoán kết quả trong tương lai. (**Data** Xem mục How To 3.2 để tìm hiểu cách thực hiện hồi quy này trong Microsoft Excel.)

---

### Ứng dụng 3.4 (Apply It 3.4)
**Lên kế hoạch cho Phân tích Xu hướng Bán hàng (Plan a Sales Trend Analysis)**

> **Data** **Kế toán Quản trị (Managerial Accounting)** Là một kế toán viên quản trị cho Best Bakes Bakery, bạn đang chuẩn bị một bản phân tích các xu hướng bán hàng để giúp lập ngân sách hoạt động năm 2026. Bạn đã được cung cấp các giao dịch bán hàng cho các năm 2022–2025. Sau đây là một đoạn trích từ file.

![Apply It 3.4](../TaiLieu/textbookForPractice/Figures/Ch_03/Apply%20It%203.4.png)

**GIẢI PHÁP (SOLUTION)**
1. Mục tiêu của phân tích là dự đoán doanh số cho ngân sách hoạt động năm tới.
2. 
| **Câu hỏi (Questions)** | **Thước đo (Measures)** |
| --- | --- |
| Doanh số bán hàng có xu hướng như thế nào từ 2022 đến 2025? | Khối lượng bán hàng, giá bán trung bình |
| Doanh số bán hàng theo sản phẩm có xu hướng như thế nào từ 2022 đến 2025? | Khối lượng bán hàng, giá bán trung bình |
| Doanh số bán hàng theo địa điểm có xu hướng như thế nào từ 2022 đến 2025? | Khối lượng bán hàng, giá bán trung bình |

3. Phân tích đường xu hướng (Trendline analysis) sẽ cung cấp một ước tính về xu hướng bán hàng mà sau đó có thể được áp dụng cho ngân sách năm 2026.

---

## 3.5 Các Mục tiêu Đề xuất (Prescriptive Objectives) là gì?

**MỤC TIÊU HỌC TẬP 5 (LEARNING OBJECTIVE 5)**
**Trình bày cách phát triển các câu hỏi đề xuất.**

Bạn đã học về các câu hỏi giúp mô tả những gì đã xảy ra, điều tra nguyên nhân tại sao, và dự báo những gì sẽ xảy ra tiếp theo. Tiếp theo, hãy kiểm tra các câu hỏi mà chúng ta đặt ra khi muốn biết những gì nên xảy ra.

### Phát triển Các Câu hỏi Đề xuất (Develop Prescriptive Questions)

Các mục tiêu đề xuất (prescriptive objectives) được xây dựng dựa trên các mô tả về hiện tại và các dự đoán về tương lai để xác định hành động tốt nhất. Các câu hỏi đề xuất điều tra cách làm thế nào để tận dụng các cơ hội trong tương lai hoặc giảm nhẹ kết quả rủi ro trong tương lai. Các phân tích chỉ định những hành động cần thiết để đạt được các kết quả mong muốn.

Trong ví dụ về Super Scooters, chúng ta đã trả lời câu hỏi dự đoán trước đó về chi phí bảo hành cho năm 2026. Bây giờ, chúng ta có thể giải quyết phân tích thứ ba do Super Scooters yêu cầu – quyết định cần sản xuất bao nhiêu đơn vị của mỗi mẫu để đạt được mục tiêu doanh thu năm 2026. Bước đầu tiên là đặt rõ ràng các câu hỏi.

Hình minh họa 3.23 bắt đầu với mục tiêu xác định tổ hợp sản phẩm có lợi nhuận cao nhất:
- Câu hỏi ban đầu thì cụ thể hơn. Nên sản xuất và bán bao nhiêu xe tay ga để tối đa hóa số dư đảm phí (contribution margin)?
- Tiếp theo, đào sâu hơn bằng cách hỏi về các ràng buộc tiềm ẩn (potential constraints) nên được đưa vào mô hình tối ưu hóa và nên sản xuất bao nhiêu đơn vị của mỗi mẫu.

![ILLUSTRATION 3.23](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.23.png)

Các phân tích đề xuất được thực hiện với các phương pháp phân tích và dữ liệu cụ thể.

### Các Ví dụ Phân tích Đề xuất (Prescriptive Analyses Examples)

Hai phương pháp phân tích phổ biến nhất được sử dụng để trả lời các câu hỏi đề xuất là các mô hình tối ưu hóa (optimization models) và phân tích "what-if" (what-if analyses).

#### Tối ưu hóa Tuyến tính (Linear Optimization)

Tối ưu hóa (optimization) là quá trình lựa chọn các giá trị của các biến số sao cho giảm thiểu hoặc tối đa hóa một đại lượng quan tâm nào đó. Mô hình hóa tối ưu (optimization modeling) giúp các nhà quản lý phân bổ các nguồn lực hiệu quả hơn.
