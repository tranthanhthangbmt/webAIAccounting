<!-- tabs:start -->
#### **Tiếng Việt**

## 1.2 Các giai đoạn của Quy trình Phân tích Dữ liệu là gì? (What are the Stages of the Data Analysis Process?)

> **MỤC TIÊU HỌC TẬP 2 (LEARNING OBJECTIVE 2)**
> Mô tả các giai đoạn của quy trình phân tích dữ liệu.

Bất kể trong lĩnh vực kế toán nào, các kế toán viên đều tuân theo một quy trình phân tích dữ liệu bao gồm ba giai đoạn quan trọng như nhau (ILLUSTRATION 1.8).

![ILLUSTRATION 1.8](../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION%201.8.png)

Tuân theo một quy trình phân tích dữ liệu giúp đảm bảo rằng các phân tích dữ liệu được thực hiện một cách hiệu quả và có hiệu suất. Có những chương cụ thể dành riêng cho từng giai đoạn, nhưng ở đây chúng ta sử dụng một ví dụ ở mức độ tổng quan để giới thiệu quy trình này.

One Stop Shop (OSS) là một nhà phân phối bán buôn (Wholesale Distributor) cho các cửa hàng tiện lợi. Một nhà phân phối bán buôn mua sản phẩm từ các nhà cung cấp với số lượng lớn và sau đó bán các sản phẩm đó cho các nhà bán lẻ với giá cao hơn một chút, giữ lại phần chênh lệch làm lợi nhuận (Profit). Kể từ những khởi đầu khiêm tốn vào năm 1888 tại San Francisco, California với tư cách là một cửa hàng bách hóa, OSS đã phát triển thành một trong những nhà phân phối hàng tiêu dùng lớn nhất ở Bắc Mỹ. OSS có cùng mục tiêu ngày nay giống như hơn một trăm ba mươi năm trước - cung cấp cho khách hàng những hàng hóa chất lượng và dịch vụ nhanh chóng.

Ngày nay, OSS hoạt động tại Canada, Mexico và Hoa Kỳ. Công ty có 15 khu vực (5 khu vực ở mỗi quốc gia) và 30 trung tâm phân phối. OSS phân phối các sản phẩm thuộc các danh mục sau:
- Thức ăn trẻ em (Baby food)
- Đồ gia dụng (Household)
- Đồ uống (Beverages)
- Thịt (Meat)
- Ngũ cốc (Cereal)
- Văn phòng phẩm (Office supplies)
- Quần áo (Clothes)
- Chăm sóc cá nhân (Personal care)
- Mỹ phẩm (Cosmetics)
- Đồ ăn vặt (Snacks)
- Trái cây (Fruits)
- Rau quả (Vegetables)

Hãy tưởng tượng bạn là một kế toán viên tại OSS và người quản lý của bạn đã yêu cầu bạn sử dụng phân tích dữ liệu để đánh giá hiệu suất. Hãy áp dụng quy trình phân tích dữ liệu vào nhiệm vụ này.

### Giai đoạn 1: Lên kế hoạch (Stage 1: Plan)
Giai đoạn đầu tiên của quy trình phân tích dữ liệu là lập kế hoạch. Điều này bao gồm việc xác định động lực (Motivation) cho việc phân tích, xác định mục tiêu (Objective) và các câu hỏi cần trả lời, và vạch ra một chiến lược (Strategy) để thực hiện phân tích.

#### Hiểu rõ Động lực (Understand Motivation)
Động lực là lý do tại sao phân tích được thực hiện. Nó chính là chữ "tại sao" (why) chúng ta thực hiện phân tích. Chữ "tại sao" đằng sau một dự án có thể thay đổi từ việc tận dụng các cơ hội cho đến giải quyết các vấn đề, và nguồn gốc của nó có thể là bên ngoài hoặc bên nội bộ:
- **Động lực từ bên ngoài (External motivation):** Dự án bắt nguồn từ một yêu cầu hoặc đòi hỏi của một bên khác, chẳng hạn như các bên liên quan bên ngoài (External Stakeholders). Các bên liên quan bên ngoài này có thể là các nhà đầu tư (Investors), chủ nợ (Creditors), đối tác chuỗi cung ứng, cơ quan quản lý ngành hoặc các cơ quan chính phủ. Một ví dụ khác về động lực từ bên ngoài là khi một người nào đó trong tổ chức, nhưng ở một nhóm khác, giao dự án.
- **Động lực từ nội bộ (Internal motivation):** Dự án được thúc đẩy bởi mong muốn phục vụ khách hàng tốt hơn, hiểu rõ hơn về các hiện tượng để có được thông tin kinh doanh thông minh (Business Intelligence), hoặc để thực hiện các trách nhiệm công việc. Các dự án được thúc đẩy từ nội bộ khi lượng thông tin gia tăng thu được được tin là lớn hơn các chi phí tiềm tàng liên quan đến việc thực hiện các phân tích dữ liệu.

ILLUSTRATION 1.9 là một phân tích về doanh số bán hàng và lợi nhuận trong bốn năm qua tại OSS.

![ILLUSTRATION 1.9](../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION%201.9.png)

Phân tích tiết lộ rằng tổng doanh số và tổng lợi nhuận tăng từ năm 2023 đến 2024, nhưng lại giảm từ năm 2024 đến 2025 với mức 9.4%. OSS lo ngại về sự sụt giảm này, do đó động lực của họ để thực hiện phân tích là muốn hiểu tại sao doanh thu lại giảm từ năm 2024 đến 2025. Loại động lực này được xem là động lực nội bộ. Một khi động lực cho việc phân tích dữ liệu được thiết lập, đây là lúc chuyển từ bức tranh toàn cảnh sang các mục tiêu cụ thể.

#### Xác định Mục tiêu (Determine the Objective)
Mọi dự án phân tích dữ liệu đều bắt đầu bằng việc thiết lập một mục tiêu, đó chính là đích đến của dự án. Một mục tiêu rõ ràng thu hẹp trọng tâm của phân tích, và các câu hỏi cụ thể hướng dẫn phân tích có thể được phát triển dựa trên mục tiêu đó.
Ví dụ, mục tiêu phân tích của OSS là xác định yếu tố nào đang thúc đẩy sự sụt giảm trong doanh số và lợi nhuận. Dựa trên điều đó, bạn có thể phát triển các câu hỏi cụ thể sau:
- Có phải chỉ có một danh mục sản phẩm duy nhất gặp phải sự sụt giảm về doanh số và lợi nhuận?
- Sự sụt giảm có diễn ra ở tất cả các quốc gia và khu vực không?

#### Thiết kế Chiến lược Dữ liệu và Phân tích (Design the Data and Analysis Strategy)
Phát triển một chiến lược cho dự án là bước cuối cùng trong giai đoạn lên kế hoạch. Có hai khía cạnh đối với điều này – xác định dữ liệu cần thiết để trả lời các câu hỏi và quyết định loại hình phân tích nào là phù hợp dựa trên cả dữ liệu và những câu hỏi đó.
Thiết kế chiến lược cho dữ liệu bao gồm việc xác định dữ liệu cụ thể cần thiết và biết cách truy cập nó. Có hai loại dữ liệu:
- **Dữ liệu nội bộ (Internal data):** Được tìm thấy bên trong tổ chức. Điều này bao gồm dữ liệu giao dịch, dữ liệu sổ cái chung, dữ liệu bán hàng, dữ liệu khách hàng, dữ liệu nhà cung cấp, các tài liệu nội bộ, và email nội bộ.
- **Dữ liệu bên ngoài (External data):** Được thu thập từ bên ngoài tổ chức. Các dữ liệu như thế này có thể đến từ mạng xã hội, các trang web, dữ liệu thời tiết, dữ liệu chính phủ, và bản đồ.

Hiểu được nguồn dữ liệu tiềm năng là rất quan trọng. Ví dụ, việc thực hiện phân tích về các khoản phải trả yêu cầu truy cập vào các nguồn dữ liệu nội bộ để lấy dữ liệu sổ cái chung và dữ liệu nhà cung cấp. Nếu một công ty bán đồ uống và mục tiêu phân tích là dự đoán doanh số bán sô-cô-la nóng, thì cả dữ liệu nội bộ (giao dịch) và dữ liệu bên ngoài (dữ liệu thời tiết) sẽ được sử dụng.

Về phần chiến lược phân tích, có bốn loại phương pháp phân tích dữ liệu, mỗi loại sẽ được thảo luận chi tiết trong các chương tương lai. ILLUSTRATION 1.10 cung cấp một số ví dụ ngắn gọn và định nghĩa cho chúng.

![ILLUSTRATION 1.10](../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION%201.10.png)

Loại phân tích phổ biến nhất và dễ hiểu nhất, **Phân tích mô tả (Descriptive analytics)**, tiết lộ điều gì đang diễn ra ở hiện tại hoặc điều gì đã xảy ra trong quá khứ. Chúng là loại phân tích đầu tiên được thực hiện để giúp hiểu dữ liệu. Tổng (Sum), đếm (Count), trung bình (Average), trung vị (Median), độ lệch chuẩn (Standard Deviation), và tỷ lệ (Proportions) là các ví dụ.

Thay vì chỉ cho chúng ta biết điều gì đã xảy ra, **Phân tích chẩn đoán (Diagnostic analytics)** tiết lộ tại sao một điều gì đó đã xảy ra. Các thông tin thu được từ phân tích mô tả về những gì đã xảy ra cho phép chúng ta đào sâu hơn để hiểu tại sao. Kết quả của những phân tích này cung cấp thông tin cho việc ra quyết định về các hành động trong tương lai. Ví dụ bao gồm việc phát hiện các dị biệt (Anomaly and Outlier Detection), phân tích xu hướng (Trend Analysis), và nhận dạng mẫu (Pattern Recognition).

**Phân tích dự đoán (Predictive analytics)** cũng giúp hiểu và dự đoán điều gì có thể xảy ra trong tương lai. Phân tích dự đoán sử dụng dữ liệu, các thuật toán thống kê, và học máy (Machine Learning) để xác định khả năng xảy ra của các kết quả trong tương lai dựa trên dữ liệu lịch sử. Mục tiêu là sử dụng những gì đã biết về quá khứ để đưa ra đánh giá tốt hơn về những gì có thể xảy ra trong tương lai. Dự báo (Forecasting), phân tích hồi quy (Regression Analysis), và phân tích chuỗi thời gian (Time-series Analysis) là một vài ví dụ.

Cuối cùng, **Phân tích đề xuất (Prescriptive analytics)** giúp xác định lộ trình hành động tốt nhất để đạt được mục tiêu trong một kịch bản nhất định. Những phân tích này vượt xa các phân tích mô tả và dự đoán bằng cách đề xuất một hoặc nhiều quá trình hành động có thể. Phân tích đề xuất bao gồm phân tích tối ưu hóa (Optimization) và phân tích giả định (What-if analyses).

ILLUSTRATION 1.11 tóm tắt giai đoạn lên kế hoạch cho OSS, bao gồm phương pháp phân tích dữ liệu nên được sử dụng để thực hiện các phân tích.

![ILLUSTRATION 1.11](../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION%201.11.png)

### Giai đoạn 2: Phân tích (Stage 2: Analyze)
Sau khi lập kế hoạch cẩn thận, đã đến lúc bắt đầu phân tích. Giai đoạn này bao gồm chuẩn bị dữ liệu (Data Preparation), xây dựng các mô hình thông tin (Building Information Models), và khám phá dữ liệu (Exploring Data). Từng phần sẽ được đề cập chi tiết ở phần sau của khóa học này, nhưng chúng được mô tả ngắn gọn ở đây và áp dụng cho kịch bản của OSS.

#### Chuẩn bị Dữ liệu (Prepare Data)
Dữ liệu có chất lượng tốt dẫn đến các phân tích có chất lượng tốt, vì vậy chuẩn bị dữ liệu cho việc phân tích là một bước rất quan trọng trong giai đoạn này. Quy trình này thường được gọi là Trích xuất-Chuyển đổi-Tải (ETL - Extract-Transform-Load).
- **Trích xuất (Extracting):** là quy trình truy xuất dữ liệu từ một nguồn. Điều này có thể là tải xuống một tệp Excel hoặc trích xuất dữ liệu từ cơ sở dữ liệu (Database) hoặc kho dữ liệu (Data Warehouse).
- **Chuyển đổi (Transforming):** diễn ra khi dữ liệu được làm sạch, tái cấu trúc và/hoặc tích hợp với dữ liệu khác trước khi sử dụng cho phân tích.
- **Tải (Loading):** là quy trình nhập dữ liệu đã được chuyển đổi vào phần mềm được sử dụng để phân tích. Có nhiều loại phần mềm phân tích có sẵn, bao gồm Excel, Power BI, và Tableau.

Trong ví dụ OSS, công ty đã trích xuất một tệp chứa hàng nghìn giao dịch và một tệp chứa các số hiệu và tên khu vực. Cả hai tệp phải được chuẩn bị cho phân tích. Bước đầu tiên là xác định xem dữ liệu có cần được làm sạch hay không. Quy trình rà soát dữ liệu để tìm ra các vấn đề có thể xảy ra được gọi là lập hồ sơ dữ liệu (Data Profiling). Để xác minh tất cả dữ liệu đã được trích xuất, bạn có thể so sánh số lượng hàng (Row Counts) của dữ liệu đã trích xuất với tổng số hàng đáng lẽ phải có trong dữ liệu.
Để đảm bảo dữ liệu được chuyển đi một cách chính xác, hãy so sánh các số tiền được chuyển với các số tiền đối chiếu kiểm soát (Control Amounts). Dữ liệu của OSS có thể được chuẩn bị như thế này:
- Trích xuất: So sánh dữ liệu với tổng doanh số và con số doanh thu được cung cấp để chắc chắn tất cả các giao dịch đều có mặt ở đó.
- Chuyển đổi: Tích hợp tệp giao dịch với tệp Excel khu vực của OSS để lấy tên khu vực phục vụ cho việc phân tích theo khu vực.
- Tải: Khi đã được làm sạch và chuyển đổi, các tệp có thể được tải vào phần mềm phân tích.

Khi dữ liệu đã được tải, quá trình phân tích có thể bắt đầu bằng việc xây dựng các mô hình thông tin và khám phá dữ liệu.

#### Xây dựng Mô hình Thông tin (Build Information Models)
Lập mô hình thông tin là việc tạo ra thông tin cần thiết cho mục đích phân tích, bắt đầu từ dữ liệu thu thập được. Ví dụ là các tính toán như thu nhập ròng (Net Income), biên lợi nhuận (Profit Margin), tổng tài sản, hoặc thậm chí là điểm hòa vốn (Break-even Point) tính bằng đô la doanh thu.
Hãy xây dựng mô hình thông tin sử dụng ví dụ OSS để chẩn đoán xem có phải một hay nhiều sản phẩm hoặc khu vực đang thúc đẩy sự sụt giảm trong lợi nhuận hay không. Để phân tích lợi nhuận theo sản phẩm và khu vực, sử dụng dữ liệu OSS đã được làm sạch và chuyển đổi:
- Tạo một mô hình tính toán biên lợi nhuận theo sản phẩm và khu vực.
- Tạo một mô hình tính toán tỷ lệ biên lợi nhuận (Profit Margin Ratio).

ILLUSTRATION 1.12 là một phân tích lợi nhuận theo quốc gia.

![ILLUSTRATION 1.12](../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION%201.12.png)

Nó cho thấy lợi nhuận chỉ đang sụt giảm ở Canada và Mexico. Khám phá sâu hơn có thể xác định các khu vực cụ thể tại Canada và Mexico đang đóng góp vào sự sụt giảm đó.

#### Khám phá Dữ liệu (Explore Data)
Mục tiêu cốt lõi của phân tích dữ liệu là khám phá dữ liệu để xác định các mẫu hình (Patterns), xu hướng (Trends), hoặc các quan sát bất thường (Unusual Observations). Việc khám phá dữ liệu cho phép chúng ta phát hiện, đặt câu hỏi, và điều tra các mối quan hệ dữ liệu để thực thi thành công các mục tiêu phân tích dữ liệu. Tập dữ liệu tổng hợp của OSS và dữ liệu được tạo ra bởi phân tích biên lợi nhuận có thể được khám phá để tìm các mối quan hệ, các mẫu hình, hoặc các thông tin sâu sắc giúp giải thích tại sao lợi nhuận đã giảm từ năm 2024 xuống 2025. Doanh số là động lực chính của lợi nhuận, vì vậy dữ liệu bán hàng cho Canada và Mexico có thể được khám phá để tìm kiếm thông tin sâu sắc. ILLUSTRATION 1.13 là một phân tích doanh số theo quốc gia và khu vực cho Canada và Mexico.

![ILLUSTRATION 1.13](../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION%201.13.png)

Phân tích này cho thấy có nhiều khu vực ở cả hai quốc gia nơi doanh số đang suy giảm.

### Giai đoạn 3: Báo cáo (Stage 3: Report)
Mục tiêu của giai đoạn này là xác định xem các phân tích có đáp ứng được các mục tiêu của dự án hay không và sau đó chia sẻ kết quả. Giải thích các phân tích và truyền đạt kết quả là một giai đoạn rất quan trọng – một phân tích tuyệt vời nhưng không đáp ứng được mục tiêu của dự án thì cũng vô ích. Hơn nữa, nếu kết quả không được truyền đạt một cách hiệu quả, thì các phân tích và khuyến nghị không thể được đưa ra hành động.

#### Diễn giải Kết quả (Interpret Results)
Diễn giải phân tích dữ liệu là quy trình xem xét các phân tích để chắc chắn rằng chúng hợp lý (Make Sense) dựa trên mục tiêu của dự án và kết quả là hợp lệ (Valid) và đáng tin cậy (Reliable). Hãy tưởng tượng rằng bạn hoặc một người nào đó khác đã chuẩn bị phân tích lợi nhuận cho OSS như được hiển thị trong ILLUSTRATION 1.12. Nhắc lại rằng mục tiêu của OSS là xác định cái gì đang thúc đẩy sự giảm sút lợi nhuận từ 2024 đến 2025. Phân tích này có đáp ứng mục tiêu đó không?
- Đây là một khởi đầu tốt. Hình ảnh trực quan trong ILLUSTRATION 1.12 cho thấy Canada và Mexico có sự sụt giảm về lợi nhuận, trong khi Hoa Kỳ có một sự gia tăng nhỏ về lợi nhuận.
- Tuy nhiên, việc phân tích chưa hoàn thành. Bước tiếp theo là đào sâu hơn vào các sự sụt giảm đó để tìm ra tại sao Canada và Mexico lại có mức suy giảm lớn như vậy.

#### Truyền đạt Kết quả (Communicate Results)
Kết quả của một dự án phân tích dữ liệu có thể được truyền đạt bằng lời nói, bằng hình ảnh, hoặc bằng văn bản. Thông thường, giao tiếp phân tích dữ liệu sẽ bao gồm các trực quan hóa dữ liệu (ILLUSTRATION 1.12 và 1.13). Truyền đạt kết quả cũng có thể bao gồm các bảng điều khiển (ILLUSTRATION 1.14).

![ILLUSTRATION 1.14](../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION%201.14.png)

Bảng điều khiển trong ILLUSTRATION 1.14 truyền đạt những thay đổi về lợi nhuận tới ban quản lý của OSS:
- Phần trăm thay đổi trong lợi nhuận theo từng quốc gia so với năm trước (2024-2025).
- Tổng lợi nhuận theo quốc gia (2022-2025).
- Lợi nhuận của mỗi quốc gia đã thay đổi như thế nào so với năm trước.
Ban quản lý có thể sử dụng phân tích này để theo dõi lợi nhuận. Ví dụ, dường như lợi nhuận của OSS đã giảm ở tất cả các sản phẩm ngoại trừ ngũ cốc, quần áo, văn phòng phẩm và chăm sóc cá nhân. Giống như các bước khác trong quy trình phân tích dữ liệu, việc truyền đạt kết quả cũng sẽ được thảo luận chi tiết hơn trong khóa học sau.

### MOSAIC: Kết hợp tất cả lại với nhau (Putting it All Together)
Được tạo ra bằng cách sắp xếp các mảnh gạch vụn với nhiều màu sắc khác nhau thành các mẫu hình (Patterns), các bức tranh khảm (Mosaics) là các loại hình nghệ thuật thị giác gợi lên ý nghĩa và cảm xúc. Để dễ dàng ghi nhớ các bước trong quy trình phân tích dữ liệu, hãy tưởng tượng việc sử dụng dữ liệu để tạo ra một bức tranh khảm sẽ kể một câu chuyện. Giống như các nghệ sĩ sử dụng các quy trình sáng tạo và logic để tiết lộ ý nghĩa về thế giới xung quanh họ thông qua nghệ thuật, các kế toán viên sử dụng phân tích dữ liệu để diễn giải ý nghĩa của dữ liệu và tiết lộ những thông tin kinh doanh sâu sắc để giúp các tổ chức đạt được mục tiêu của họ. ILLUSTRATION 1.15 cung cấp một biểu diễn trực quan của quy trình phân tích dữ liệu MOSAIC.

![ILLUSTRATION 1.15](../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION%201.15.png)

Khóa học này sẽ bao gồm từng khía cạnh của MOSAIC.

#### **English**
*Nội dung tiếng Anh gốc sẽ được giữ lại trong quá trình hợp nhất tài liệu...*
<!-- tabs:end -->
