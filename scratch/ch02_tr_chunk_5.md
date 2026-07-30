## 2.5 Trực quan hóa Được Sử dụng Như thế nào trong Phân tích Dữ liệu?

**MỤC TIÊU HỌC TẬP 5 (LEARNING OBJECTIVE 5)**
**Tóm tắt cách trực quan hóa dữ liệu khám phá và giải thích dữ liệu.**

Trực quan hóa dữ liệu (data visualization) là sự trình bày bằng đồ họa của dữ liệu và thông tin. Các doanh nghiệp đang ngày càng tập trung vào trực quan hóa dữ liệu do sự kết hợp của tính sẵn có của dữ liệu ngày càng tăng và các công cụ phần mềm dễ sử dụng. Trong môi trường làm việc ngày nay, các nhà tuyển dụng kỳ vọng sinh viên tốt nghiệp ngành kế toán biết cách sử dụng trực quan hóa dữ liệu để hiểu, giải thích, và truyền đạt các câu trả lời cho các câu hỏi về dữ liệu.

Có hai loại trực quan hóa dữ liệu:
- **Trực quan hóa dữ liệu khám phá (Exploratory data visualization)** sử dụng các công cụ và kỹ thuật trực quan hóa dữ liệu để khám phá dữ liệu nhằm tìm ra những hiểu biết sâu sắc (insights). Trực quan hóa dữ liệu khám phá giúp hiểu dữ liệu và xác định các mô hình ẩn bên dưới (underlying patterns), các xu hướng (trends), hoặc các điểm bất thường (anomalies).
- **Trực quan hóa dữ liệu giải thích (Explanatory data visualization)** sử dụng các công cụ và kỹ thuật trực quan hóa dữ liệu để truyền đạt kết quả của một phân tích. Nó được sử dụng để giải thích kết quả phân tích, chỉ ra các mối quan hệ trong dữ liệu, và truyền đạt các hiểu biết sâu sắc.

Khóa học này cuối cùng sẽ đề cập chi tiết hơn đến cả hai loại trên. Cuộc thảo luận này giới thiệu về cách các trực quan hóa giúp chúng ta hiểu các tập dữ liệu lớn, xác định các dạng trực quan hóa phổ biến và khi nào nên sử dụng chúng, cũng như giải thích cách tạo chúng trong Microsoft Excel. Nhiều chuyên gia kế toán thích các phần mềm trực quan hóa mạnh mẽ hơn như Power BI và Tableau bởi vì Microsoft Excel có khả năng trực quan hóa dữ liệu hạn chế. Tuy nhiên, việc tạo trực quan hóa trong Excel là một sự giới thiệu đơn giản và hiệu quả.

### Hiểu Các Tập Dữ Liệu Lớn (Making Sense of Large Data Sets)
Trực quan hóa rất mạnh mẽ bởi vì nó có thể nhanh chóng và hiệu quả tiết lộ các hiểu biết sâu sắc (insights) được chôn giấu trong dữ liệu thô. Hình minh họa 2.56 là một bảng tóm tắt doanh số bán hàng của một cửa hàng đồ điện tử cho các năm 2023–2025. Hãy so sánh bảng này với dạng trực quan hóa của nó trong biểu đồ cột.

**HÌNH MINH HỌA 2.56 (ILLUSTRATION 2.56) Trực quan hóa Dữ liệu Bán hàng**

![ILLUSTRATION 2.56](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.56.png)

Biểu đồ đồ thị doanh số bán hàng dễ diễn giải hơn:
- Rõ ràng ngay lập tức là các thiết bị gia dụng (appliances) và tivi (TVs) có doanh số bán hàng cao nhất trong cả ba năm, và chỉ có các thiết bị gia dụng mới có sự gia tăng doanh số trong năm 2025.
- Tất cả các danh mục sản phẩm khác đều có doanh số năm 2025 thấp hơn so với hai năm trước.

Mặc dù có thể đi đến cùng những kết luận đó bằng cách sử dụng bảng dữ liệu, nhưng nó không dễ dàng bằng việc phát hiện ra các sự khác biệt hoặc đưa ra các so sánh. Khả năng nhanh chóng nhìn thấy các mô hình và các mối quan hệ trong các tập dữ liệu lớn là lý do tại sao kỹ năng trực quan hóa dữ liệu lại quan trọng đến vậy.

### Các dạng Trực quan hóa và Khi nào nên Sử dụng chúng
Có nhiều loại trực quan hóa khả dụng. Việc xác định xem nên sử dụng loại nào được dẫn dắt bởi loại dữ liệu có sẵn và điều bạn đang cố gắng thể hiện trong trực quan hóa. Trực quan hóa dữ liệu được đề cập chi tiết hơn trong các chương về phân tích, diễn giải và truyền thông, nhưng tiếp theo đây là một bản tóm tắt về một số dạng trực quan hóa phổ biến và cách để lựa chọn chúng.

#### Các Dạng Trực quan hóa Phổ biến (Common Visualizations)
**Dữ liệu phân loại (Categorical data)** là những dữ liệu được dán nhãn hoặc đặt tên có thể được sắp xếp thành các nhóm theo các đặc điểm cụ thể. Dữ liệu này không có giá trị định lượng. Dữ liệu phân loại được sử dụng trong các trực quan hóa để phác họa các nhóm dữ liệu. Trực quan hóa trong Hình minh họa 2.56 là một ví dụ sử dụng dữ liệu phân loại. Các loại sản phẩm là các nhóm giúp tóm tắt doanh số bán hàng. Cùng một trực quan hóa đó cũng bao gồm dữ liệu định lượng dưới dạng số tiền bán hàng. Việc kết hợp chúng lại với nhau chỉ ra mối quan hệ giữa các danh mục sản phẩm và doanh số bán hàng. Lưu ý rằng biểu đồ cũng có các năm. Các cột đại diện cho các năm 2023–2025.

Hãy luôn cân nhắc xem liệu dữ liệu đang được phân tích có thể được sử dụng trong một dạng trực quan hóa cụ thể hay không. Ví dụ, việc chỉ ra một mối quan hệ trong dữ liệu bằng cách sử dụng biểu đồ phân tán (scatterplot) đòi hỏi ít nhất một thước đo định lượng (quantitative measure). Việc thể hiện các xu hướng theo thời gian đòi hỏi một thước đo thời gian (ngày tháng) cộng với một thước đo định lượng.

Hình minh họa 2.57 liệt kê một số trực quan hóa dữ liệu phổ biến cùng với phần mô tả, các phương pháp hay nhất (best practices), và các loại dữ liệu cần thiết để tạo ra trực quan hóa.

**HÌNH MINH HỌA 2.57 (ILLUSTRATION 2.57) Các Trực quan hóa Dữ liệu Phổ biến**

![ILLUSTRATION 2.57](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.57.png)

Khi bạn phát triển các kỹ năng phân tích dữ liệu của mình, bạn sẽ làm việc với các tập dữ liệu lớn và sẽ cần sử dụng trực quan hóa dữ liệu để phân tích chúng và truyền đạt các phát hiện (findings). Bảng này có thể là một tài liệu tham khảo hữu ích khi bạn khám phá dữ liệu và truyền đạt các phát hiện của mình.

#### Lựa chọn Dạng Trực quan hóa (Choosing Visualizations)
Làm sao bạn biết trực quan hóa nào là tốt nhất cho một phân tích? Hãy bắt đầu bằng cách xem xét mục tiêu của dự án. Có một số mục tiêu phân tích phổ biến:
- Thể hiện sự cấu thành (Showing composition)
- Chỉ ra các mối quan hệ (Indicating relationships)
- Hiển thị các sự phân phối (Displaying distributions)
- Tìm kiếm các xu hướng (Finding trends)
- Thực hiện các so sánh (Making comparisons)

Hình minh họa 2.58 phân tích các lựa chọn trực quan hóa nếu mục tiêu là để thể hiện sự cấu thành, các mối quan hệ, hoặc các sự phân phối.
Hình minh họa 2.59 xác định các trực quan hóa hữu ích để hiển thị các xu hướng hoặc thực hiện các so sánh.

**HÌNH MINH HỌA 2.58 (ILLUSTRATION 2.58) Hướng dẫn về Các Trực quan hóa Thể hiện Sự Cấu thành, Mối Quan hệ, và Sự Phân phối**

![ILLUSTRATION 2.58](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.58.png)

**HÌNH MINH HỌA 2.59 (ILLUSTRATION 2.59) Hướng dẫn về Các Trực quan hóa Thể hiện Các Xu hướng hoặc Các So sánh**

![ILLUSTRATION 2.59](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.59.png)

Bạn có thể sử dụng cả hai hướng dẫn trực quan hóa này, cùng với các mô tả và các phương pháp hay nhất trong Hình minh họa 2.57, để tạo ra trực quan hóa tốt nhất giải quyết mục đích của việc phân tích.

### Các Trực quan hóa của Microsoft Excel
Nhiều công cụ có thể tạo ra các trực quan hóa. Khóa học này tập trung vào bộ ba phần mềm: Tableau, Power BI, và Microsoft Excel, là những công cụ phổ biến nhất (nhưng chắc chắn không phải là duy nhất) được sử dụng trong kinh doanh ngày nay.

Microsoft Excel có thể tạo ra các trực quan hóa dữ liệu cơ bản. Các công cụ trực quan hóa trong Microsoft Excel nằm trong dải băng (ribbon) Insert (Hình minh họa 2.60).

**HÌNH MINH HỌA 2.60 (ILLUSTRATION 2.60) Chèn một Trực quan hóa trong Excel**

![ILLUSTRATION 2.60](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.60.png)

Để sử dụng công cụ Charts:
- Đánh dấu (highlight) dữ liệu cần vẽ biểu đồ.
- Chọn một biểu đồ cụ thể, hoặc nhấp vào **Recommended Charts** để xem các đề xuất.

Một biểu đồ cũng có thể được tạo ra từ một Excel PivotTable. Có thể tạo PivotTable trước hoặc tạo PivotTable và biểu đồ cùng lúc bằng cách sử dụng **PivotChart**. Hình minh họa 2.61 hiển thị hộp thoại khi Create PivotChart được chọn. Lưu ý rằng nó giống hệt hộp thoại PivotTable.

**HÌNH MINH HỌA 2.61 (ILLUSTRATION 2.61) Hộp thoại PivotChart**

![ILLUSTRATION 2.61](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.61.png)

> **Data** Ví dụ này sử dụng tệp dữ liệu Super Scooters để tạo đồng thời một PivotTable và PivotChart về doanh thu gộp theo năm và theo mẫu xe (Hình minh họa 2.62). Để làm điều này, hãy chọn:
- Trường `Model` cho Legend (Series).
- `Year` cho Axis (Categories).
- `Sum of Gross Sales` cho Values.

Hình minh họa 2.63 hiển thị PivotTable và PivotChart kết quả, đây là một biểu đồ thanh (bar chart) trong đó màu của các thanh đại diện cho các mẫu xe.

**HÌNH MINH HỌA 2.62 (ILLUSTRATION 2.62) Vùng làm việc PivotTable và PivotChart**

![ILLUSTRATION 2.62](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.62.png)

**HÌNH MINH HỌA 2.63 (ILLUSTRATION 2.63) PivotTable và PivotChart Đã hoàn thành của Super Scooters**

![ILLUSTRATION 2.63](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.63.png)

Trong suốt sự nghiệp kế toán của mình, bạn sẽ bắt gặp nhiều loại phần mềm trực quan hóa dữ liệu. Tuy nhiên, việc học cách sử dụng bất kỳ phần mềm nào trong số này cũng giúp chuẩn bị cho bạn sử dụng và tìm hiểu công nghệ mới.

---

### Áp dụng (Apply It 2.5)
**Phân tích Chi phí Sản phẩm với Trực quan hóa Dữ liệu (Analyze Product Costs with Data Visualization)**

**Kế toán Quản trị (Managerial Accounting)**
Kiểm soát viên tại Super Scooters đã yêu cầu bạn chuẩn bị một bản phân tích chi phí sản phẩm. Cụ thể, kiểm soát viên muốn có câu trả lời cho bốn câu hỏi sau:
1. Tổng chi phí cho mỗi mẫu xe mỗi năm là bao nhiêu?
2. Chi phí biến đổi nào là cao nhất?
3. Chi phí nhân công (labor), nguyên vật liệu (materials), và chi phí sản xuất chung (overhead costs) đang tăng hay giảm theo thời gian?
4. Liệu tổng chi phí có liên quan đến khối lượng bán hàng (sales volume) không?

Đối với mỗi câu hỏi:
- Hãy xác định một dạng trực quan hóa phù hợp và giải thích lý do của bạn.
- Liệt kê các phương pháp hay nhất (best practices) cho dạng trực quan hóa đó.
- Xác định loại dữ liệu cần thiết cho trực quan hóa.

**GIẢI PHÁP (SOLUTION)**

1. Một biểu đồ vùng (area chart) là lựa chọn tốt nhất bởi vì nó thể hiện những thay đổi về khối lượng theo thời gian. Đối với câu hỏi này, nó sẽ hiển thị những thay đổi về tổng chi phí theo thời gian.
   *Phương pháp hay nhất (Best Practices):*
   - Không sử dụng cho dữ liệu có nhiều hơn 4 danh mục để tránh nhầm lẫn và lộn xộn. Ở đây có bốn mẫu xe, do đó yêu cầu này được đáp ứng.
   - Bắt đầu trục y ở số không hoặc cao hơn.
   - Đặt dữ liệu có độ biến động cao ở trên cùng và dữ liệu có độ biến động thấp ở dưới cùng.
   *Dữ liệu (Data):*
   - Trường ngày tháng (sử dụng năm)
   - Ít nhất một thước đo định lượng (sử dụng tổng chi phí)
2. Một biểu đồ cột/thanh (bar chart) là trực quan hóa phù hợp nhất vì nó so sánh các phần với tổng thể, làm nổi bật các danh mục, hoặc hiển thị những thay đổi theo thời gian.
   *Phương pháp hay nhất (Best Practices):*
   - So sánh hai đến bảy danh mục bằng các thanh dọc.
   - Sử dụng các thanh ngang nếu có nhiều hơn bảy danh mục hoặc nhãn danh mục quá dài.
   - Sử dụng các nhãn ngang để dễ đọc hơn.
   - Khoảng cách giữa các thanh (space bars) phải phù hợp và nhất quán.
   - Sử dụng màu sắc một cách tiết kiệm hoặc như một điểm nhấn.
   - Luôn có một đường cơ sở là số không (zero baseline).
   *Dữ liệu (Data):*
   - Một hoặc nhiều danh mục (chi phí nhân công, nguyên vật liệu, chi phí sản xuất chung)
   - Một hoặc nhiều thước đo định lượng (chi phí)
3. Một biểu đồ đường (line chart) là phù hợp bởi vì nó hiển thị một hoặc nhiều chuỗi dữ liệu và cho phép sử dụng nhiều chuỗi dữ liệu và điểm dữ liệu.
   *Phương pháp hay nhất (Best Practices):*
   - Thời gian chạy từ trái sang phải.
   - Cần nhất quán khi vẽ các điểm thời gian.
   - Sử dụng các đường nét liền (solid lines), không dùng nét đứt.
   - Sử dụng một đường cơ sở bằng không.
   - Không vẽ nhiều hơn bốn đường trên cùng một đồ thị. Thay vào đó, hãy sử dụng nhiều biểu đồ.
   *Dữ liệu (Data):*
   - Một trường ngày tháng
   - 0 hoặc nhiều danh mục
   - Một hoặc nhiều thước đo định lượng
4. Một biểu đồ phân tán (scatterplot) là phù hợp nhất để xem xét liệu có mối tương quan giữa khối lượng bán hàng và tổng chi phí hay không.
   *Phương pháp hay nhất (Best Practices):*
   - Tập dữ liệu nên đi theo cặp với một biến độc lập (independent variable - trục x) và một biến phụ thuộc (dependent variable - trục y).
   - Sử dụng nếu thứ tự không liên quan – nếu không hãy sử dụng một biểu đồ đường.
   - Không sử dụng nếu chỉ có một vài phần dữ liệu hoặc nếu không có sự tương quan.
   *Dữ liệu (Data):*
   - 0 hoặc nhiều danh mục
   - Một hoặc nhiều thước đo định lượng (khối lượng bán hàng và tổng chi phí)
