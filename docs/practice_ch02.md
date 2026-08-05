# Chương 2: Các Kỹ năng Phân tích Dữ liệu Nền tảng (Foundational Data Analysis Skills)

<!-- tabs:start -->
#### **Tiếng Việt**

## Tổng quan Chương (Chapter Preview)

Bạn sẽ làm việc với dữ liệu và phần mềm phân tích dữ liệu trong suốt sự nghiệp của mình, và một trong những công cụ phần mềm phổ biến nhất được sử dụng trong kế toán là Microsoft Excel. Như bạn sẽ thấy trong phần Professional Insight, khả năng sử dụng Microsoft Excel để thao tác trên các tập dữ liệu lớn là một tài sản to lớn đối với những kế toán viên chuyên nghiệp mới được tuyển dụng. Mặc dù các kỹ năng Microsoft Excel là quan trọng, nhưng phần mềm này không đủ mạnh để phân tích các tập dữ liệu cực kỳ lớn, vì vậy nó không phải là công cụ duy nhất được sử dụng để phân tích dữ liệu. Chương này giới thiệu một số kỹ năng mà bất kể sử dụng công nghệ nào, đều là nền tảng để thực hiện phân tích dữ liệu. Microsoft Excel được sử dụng để minh họa cho nhiều kỹ năng phân tích dữ liệu cốt lõi, nhưng các chương tiếp theo cũng sẽ giới thiệu các phần mềm phân tích dữ liệu như Power BI và Tableau. Sự kết hợp giữa hiểu biết cốt lõi về dữ liệu, trực quan hóa dữ liệu và các kỹ năng phân tích mô tả là nền tảng để thực hiện phân tích dữ liệu nâng cao hơn.

### Góc nhìn Chuyên gia (Professional Insight): Pivot Tables Có Thể Giúp Ích Như Thế Nào Trong Việc Hiểu Các Tập Dữ Liệu Lớn?
Josh, một sinh viên kế toán năm cuối, giải thích cách việc học Microsoft Excel đã giúp ích cho anh ấy trong kỳ thực tập.

"Nhiệm vụ đầu tiên của tôi là tạo một Excel PivotTable để thao tác với một tệp dữ liệu khổng lồ gồm khoảng 450.000 bản ghi. Tôi vừa nhận được chứng chỉ Microsoft Office Specialist Basic Excel khi bắt đầu kỳ thực tập tại PwC. Thật tuyệt vời khi được áp dụng những gì đã học ở trường vào thế giới kinh doanh. Trải nghiệm này đã mang lại cho tôi sự tự tin khi giao tiếp với cấp trên và giúp tôi xây dựng danh tiếng về sự đáng tin cậy tại công ty. Giám đốc phụ trách khách hàng của tôi đã hoàn toàn ấn tượng với công việc của tôi, và phó giám đốc (senior associate) của tôi đã rất ngạc nhiên khi tôi có thể tổng hợp một bảng dữ liệu toàn diện như vậy với rất ít kinh nghiệm."

---

## Lộ trình Chương (Chapter Roadmap)

**MỤC TIÊU HỌC TẬP (LEARNING OBJECTIVES)** | **CHỦ ĐỀ (TOPICS)** | **ỨNG DỤNG (APPLY IT)**
--- | --- | ---
**LO 2.1** Mô tả cách dữ liệu được lưu trữ trong và trích xuất từ các cơ sở dữ liệu quan hệ. | • Cơ sở dữ liệu quan hệ (Relational Databases)<br>• Kết nối các bảng (Joining Tables) | Xác định Khóa chính và Khóa ngoại (Identify Primary and Foreign Keys) *(Ví dụ: Hệ thống Thông tin Kế toán)*
**LO 2.2** Giải thích cách các hàm giúp trả lời các câu hỏi phân tích dữ liệu. | • Các Hàm Cơ bản cho Phân tích Dữ liệu<br>• Áp dụng các Hàm Cơ bản của Excel | Phân tích Các Giao dịch Bán hàng với Các Hàm Excel *(Ví dụ: Kế toán Tài chính và Kế toán Quản trị)*
**LO 2.3** Minh họa cách các pivot tables tổ chức và lọc dữ liệu. | • Sử dụng Pivot Tables<br>• Lọc Pivot Tables | Phân tích Bán hàng với Excel PivotTables *(Ví dụ: Kế toán Tài chính và Kế toán Quản trị)*
**LO 2.4** Nhận diện các thước đo mô tả được sử dụng để thực hiện phân tích dữ liệu. | • Các thước đo vị trí (Measures of Location)<br>• Các thước đo độ phân tán (Measures of Dispersion)<br>• Các thước đo hình dạng (Measures of Shape)<br>• Phân tích tương quan (Correlation Analysis) | Sử dụng Thống kê Mô tả để Kiểm toán Chi phí Bảo hành *(Ví dụ: Kiểm toán)*
**LO 2.5** Tóm tắt cách trực quan hóa dữ liệu khám phá và giải thích dữ liệu. | • Hiểu Các Tập Dữ Liệu Lớn<br>• Trực quan hóa và Khi nào nên Sử dụng chúng<br>• Trực quan hóa bằng Microsoft Excel | Phân tích Chi phí Sản phẩm bằng Trực quan hóa Dữ liệu *(Ví dụ: Kế toán Quản trị)*

> **Data** Thẻ Data xuất hiện trong chương khi dữ liệu cho một ví dụ, hình ảnh minh họa hoặc ứng dụng có sẵn trên nền tảng học tập trực tuyến của Wiley. Các phần mềm phân tích dữ liệu liên tục thay đổi, và có thể có những phiên bản mới hơn của phần mềm được đề cập trong chương này. Để biết thêm thông tin, hãy truy cập video đi kèm trên nền tảng học tập trực tuyến của Wiley.

---

## 2.1 Việc Hiểu Cách Lưu Trữ Dữ Liệu Giúp Trả Lời Các Câu Hỏi Như Thế Nào?

**MỤC TIÊU HỌC TẬP 1 (LEARNING OBJECTIVE 1)**
**Mô tả cách dữ liệu được lưu trữ trong và trích xuất từ các cơ sở dữ liệu quan hệ.**

Hiểu cách dữ liệu được lưu trữ là rất quan trọng đối với phân tích dữ liệu. Điều này là do loại phân tích có thể được thực hiện phụ thuộc vào dữ liệu đang được sử dụng, và việc xác định cũng như trích xuất dữ liệu chúng ta cần đòi hỏi phải biết cách nó được lưu trữ.

![ILLUSTRATION 2.2](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.2.png)

### Cơ sở dữ liệu quan hệ (Relational Databases)

Dữ liệu, bất kể loại hay định dạng, cần được lưu trữ ở đâu đó. Một cách để làm điều đó là lưu trữ trong một **cơ sở dữ liệu quan hệ (relational database)**, đó là một tập hợp các dữ liệu có liên quan logic với nhau có thể được truy xuất, thao tác và cập nhật để đáp ứng nhu cầu của người dùng. Hầu hết dữ liệu bạn sẽ làm việc trong sự nghiệp kế toán của mình sẽ đến từ các cơ sở dữ liệu quan hệ, nơi dữ liệu được lưu trữ trong các bảng (tables) riêng lẻ có thể được liên kết với nhau. Khi các bảng được liên kết, dữ liệu từ nhiều bảng có thể được truy cập.

Một bảng trong cơ sở dữ liệu quan hệ lưu trữ dữ liệu có giá trị liên quan đến một đối tượng được quan tâm, chẳng hạn như một nguồn lực doanh nghiệp (business resource), sự kiện (event), hoặc tác nhân (agent). Các bảng bao gồm các hàng (rows) và cột (columns):
- Mỗi hàng đại diện cho một bản ghi (record) hoặc một phiên bản của đối tượng trong bảng.
- Các cột phản ánh các **thuộc tính (attributes)**, đó là các trường dữ liệu (data fields) mô tả các khía cạnh khác nhau của các bản ghi (Hình minh họa 2.1).

**HÌNH MINH HỌA 2.1 (ILLUSTRATION 2.1) Các Yếu tố của Cơ sở dữ liệu, Các Ví dụ về Bảng và Thuộc tính**

![ILLUSTRATION 2.1](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.1.png)

Hình minh họa 2.2 (ILLUSTRATION 2.2) phía trên là góc nhìn cơ sở dữ liệu về bảng dữ liệu tài sản của một trường đại học, chứa dữ liệu về lượng tài sản tồn kho của trường.

Mỗi hàng trong bảng hiển thị một tài sản có thể nhận diện duy nhất. Các thuộc tính đi kèm với nó được sắp xếp trong mỗi cột dọc liệt kê bên dưới tên bảng:
- `AssetTagID`: Số thẻ nhận diện (Tag identification number)
- `AssetDescription`: Mô tả tài sản
- `CategoryID`: Số nhận diện danh mục
- `Amount`: Nguyên giá tài sản
- `AcquisitionDate`: Ngày mua tài sản

Bảng `AssetUsefulLife` chứa thông tin liên quan đến các danh mục tài sản. Mỗi hàng là một danh mục duy nhất, và các cột là các thuộc tính của danh mục đó:
- `CategoryID`: Số nhận diện cho mỗi danh mục tài sản
- `CategoryDescription`: Mô tả danh mục
- `UsefulLife`: Thời gian sử dụng hữu ích tính bằng năm của các tài sản trong mỗi danh mục

Có một biểu tượng chìa khóa bên cạnh thuộc tính `AssetTagID` trong bảng đầu tiên và `CategoryID` trong bảng thứ hai. Biểu tượng này xác định **khóa chính (primary key)**, đó là cột bắt buộc phải có một giá trị duy nhất cho mỗi hàng trong bảng. Trong bảng `UniversityAssetData`, mỗi tài sản được nhận diện duy nhất bởi cột khóa chính `AssetTagID`. Trong bảng `AssetUsefulLife`, khóa chính là `CategoryID`. Mỗi hàng trong bảng `AssetUsefulLife` sẽ có một số `CategoryID` duy nhất.

Để tính khấu hao cho tài sản, chúng ta cần thông tin về nguyên giá, thông tin về thời gian sử dụng hữu ích và tuổi của tài sản. Tuy nhiên, thông tin đó xuất hiện ở hai bảng khác nhau. Việc liên kết chúng yêu cầu một trường chung trong cả hai bảng:
- Trường `CategoryID` có ở cả hai bảng.
- `CategoryID` là cột khóa chính trong bảng `AssetUsefulLife`.
- Trong bảng `UniversityAssetData`, `CategoryID` là một **cột khóa ngoại (foreign key column)**. Một cột khóa ngoại chứa cùng một dữ liệu với khóa chính từ một bảng khác. Nó được lặp lại trong bảng thứ hai để các bảng có thể được liên kết trong mối quan hệ với nhau. Hình minh họa 2.3 cho thấy mối quan hệ liên kết hai bảng sử dụng thuộc tính `CategoryID`.

Tại sao điều này lại quan trọng? Việc liên kết các bảng tạo ra một mối quan hệ giúp bạn có thể lấy thông tin từ cả hai bảng và tạo các tính toán về khấu hao cho mọi tài sản trong bảng dữ liệu tài sản.

**HÌNH MINH HỌA 2.3 (ILLUSTRATION 2.3) Tạo Mối Quan Hệ Giữa Các Bảng**

![ILLUSTRATION 2.3](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.3.png)

### Kết nối các bảng (Joining Tables)

Khi các trường chung sử dụng khóa chính và khóa ngoại được xác định trên các bảng, bước tiếp theo là cho cơ sở dữ liệu biết cách liên kết các bảng để trích xuất dữ liệu:
- **Truy vấn (query)** là một yêu cầu hành động được đưa ra đối với cơ sở dữ liệu. Nó cung cấp cho máy tính các hướng dẫn để kết nối, thêm, cập nhật, xóa, truy xuất, hoặc thao tác với dữ liệu trong các bảng của nó. Các truy vấn có thể được tạo ra và sử dụng một lần hoặc lưu trữ để tái sử dụng sau này.
- Ngôn ngữ lệnh truy vấn tiêu chuẩn được sử dụng để quản lý cơ sở dữ liệu là **Ngôn ngữ Truy vấn Có cấu trúc (Structured Query Language - SQL)**. Việc viết mã SQL nằm ngoài phạm vi của chương này, nhưng may mắn thay, nhiều chương trình phần mềm có tích hợp sẵn các ứng dụng tự động tạo mã SQL cần thiết để truy vấn cơ sở dữ liệu.

Việc truy xuất tất cả các trường dữ liệu cần thiết để hoàn thành một tác vụ cụ thể đòi hỏi phải hiểu cách **kết nối (join)** các bảng dựa trên các cột mà chúng có điểm chung. Các bảng được liên kết bằng cách tạo một **lệnh join** kết hợp các hàng từ hai hoặc nhiều bảng dựa trên một cột liên quan giữa chúng. Các lệnh kết nối cũng được sử dụng trong các phần mềm trực quan hóa dữ liệu và các phần mềm phân tích dữ liệu khác khi có nhiều hơn một bảng dữ liệu đang được sử dụng trong một phân tích. (Chúng ta sẽ thảo luận chi tiết hơn về trực quan hóa dữ liệu ở phần cuối của chương này và trong các chương sau).

Các kiểu kết nối (joins) phổ biến nhất là **kết nối trong (inner)**, **kết nối trái (left)**, **kết nối phải (right)**, và **kết nối toàn bộ (full)**. Hình minh họa 2.4 tóm tắt các lệnh kết nối khác nhau và cung cấp một đại diện trực quan. Phần tô bóng xanh dương thể hiện kết quả của lệnh kết nối. Lưu ý rằng **giá trị null (null value)** không giống với giá trị bằng không (0). Một giá trị null là khi một giá trị bị ẩn, không được biết (unknown) hoặc bị thiếu (missing).

**HÌNH MINH HỌA 2.4 (ILLUSTRATION 2.4) Các Loại Kết nối (Types of Joins)**

![ILLUSTRATION 2.4](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.4.png)

Chúng ta có thể minh họa cách các kết nối này hoạt động bằng một ví dụ. Bikes R Us là một đại lý bán buôn xe đạp. Hình minh họa 2.5 cho thấy hai bảng từ cơ sở dữ liệu của họ:
- Bảng bên trái là bảng Khách hàng (`Customer`), và bảng Đơn hàng (`Order`) ở bên phải.
- `CustomerID` là khóa chính trong bảng Khách hàng.
- `OrderID` là khóa chính trong bảng Đơn hàng. `CustomerID` ở đây là một khóa ngoại.

**HÌNH MINH HỌA 2.5 (ILLUSTRATION 2.5) Các Bảng Cơ sở dữ liệu của Bikes R Us**

![ILLUSTRATION 2.5](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.5.png)

Một **kết nối trong (inner join)** trên hai bảng này sẽ tạo ra một bảng với toàn bộ dữ liệu từ cả hai bảng khớp với nhau trên trường `CustomerID` (Hình minh họa 2.6).

**HÌNH MINH HỌA 2.6 (ILLUSTRATION 2.6) Kết quả từ Inner Join cho Bikes R Us**

![ILLUSTRATION 2.6](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.6.png)

Inner join hiển thị thông tin khách hàng và đơn hàng cho mỗi khách hàng đã đặt một đơn hàng:
- Những kết quả này tiết lộ rằng khách hàng có `CustomerID = 1003`, Little Town Bike Stores, chưa thực hiện bất kỳ giao dịch mua nào.
- `OrderID 50016` không có trường hợp khớp nào trong bảng khách hàng với `CustomerID = 102`, do đó đơn hàng này không được phản ánh trong các bảng đã được kết nối.

Một **kết nối trái (left join)** trả về tất cả các hàng từ bảng bên trái và sẽ hiển thị bất kỳ dữ liệu khớp nào từ bảng bên phải. Nếu không có các hàng khớp trong bảng bên phải, thì các trường không có dữ liệu khớp sẽ mang giá trị null (Hình minh họa 2.7).

**HÌNH MINH HỌA 2.7 (ILLUSTRATION 2.7) Kết quả từ Left Join cho Bikes R Us**

![ILLUSTRATION 2.7](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.7.png)

Left join trong Hình minh họa 2.7 hiển thị tất cả các khách hàng từ bảng Customer và thông tin khớp từ bảng Order:
- `CustomerID = 1003` được liệt kê trong kết nối này, nhưng vì không có đơn hàng nào khớp, các kết quả cho các trường của đơn hàng là null.
- `OrderID = 50016` không được phản ánh trong kết quả của bảng đã kết nối. Không có `CustomerID = 102` nào trong bảng Customer, nên bản ghi đó không được đưa vào kết nối.

Một **kết nối phải (right join)** trả về tất cả các hàng từ bảng bên phải và sẽ hiển thị bất kỳ dữ liệu khớp nào từ bảng bên trái (Hình minh họa 2.8).

**HÌNH MINH HỌA 2.8 (ILLUSTRATION 2.8) Kết quả từ Right Join cho Bikes R Us**

![ILLUSTRATION 2.8](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.8.png)

Right join trong Hình minh họa 2.8 hiển thị tất cả các đơn hàng từ bảng Order và bất kỳ khách hàng nào khớp từ bảng Customer:
- Không có bản ghi khách hàng nào khớp cho `CustomerID = 102`, vì vậy các trường từ bảng Customer sẽ có giá trị null cho bản ghi đó.
- Nếu không có hàng khớp trong bảng bên trái, thì các trường sẽ có giá trị null.

Một **kết nối toàn bộ (full join)** sẽ trả về tất cả các hàng từ cả hai bảng (Hình minh họa 2.9).

**HÌNH MINH HỌA 2.9 (ILLUSTRATION 2.9) Kết quả từ Full Join cho Bikes R Us**

![ILLUSTRATION 2.9](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.9.png)

Full join được hiển thị trong Hình minh họa 2.9 hiển thị toàn bộ các bản ghi từ cả hai bảng:
- Lưu ý các giá trị null đối với các trường của bảng Order cho `CustomerID = 1003` và các giá trị null đối với các trường của bảng Customer cho `OrderID = 50016`.
- Bất kỳ trường nào không có dữ liệu khớp sẽ có giá trị null.

Các kết nối (joins) là thiết yếu khi phân tích dữ liệu từ nhiều nguồn khác nhau. Hình minh họa 2.10 đưa ra các ví dụ về một số câu hỏi mà các kế toán viên có thể cần hỏi về dữ liệu và loại kết nối thích hợp sẽ giúp trả lời chúng.

**HÌNH MINH HỌA 2.10 (ILLUSTRATION 2.10) Các Câu hỏi Phân tích Dữ liệu Mẫu và Lệnh kết nối Phù hợp**

![ILLUSTRATION 2.10](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.10.png)

---

### Áp dụng (Apply It 2.1)
**Xác định Khóa chính và Khóa ngoại (Identify Primary and Foreign Keys)**

**Hệ thống Thông tin Kế toán (Accounting Information Systems)** Super Scooters, một nhà sản xuất xe tay ga có động cơ, vừa chuyển đổi sang một hệ thống cơ sở dữ liệu quan hệ. Bạn làm việc trong bộ phận hệ thống thông tin kế toán của công ty và đã và đang hỗ trợ việc chuyển đổi sang hệ thống cơ sở dữ liệu mới. Các bảng sau đây đã được thiết lập.

![Apply It 2.1](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.1.png)

**YÊU CẦU:**
1. Hãy cho biết khóa chính (primary key) của mỗi bảng.
2. Hãy chỉ ra các trường đóng vai trò là khóa ngoại (foreign key) và ghi rõ bảng mà khóa ngoại đó tham chiếu tới.

## 2.2 Các Hàm Bảng Tính Phân Tích Lượng Lớn Dữ Liệu Như Thế Nào?

**MỤC TIÊU HỌC TẬP 2 (LEARNING OBJECTIVE 2)**
**Giải thích cách các hàm giúp trả lời các câu hỏi phân tích dữ liệu.**

Phân tích dữ liệu thường bao gồm việc thực hiện các tính toán như cộng tổng các số tiền, đếm các mục dữ liệu, và tính toán số trung bình. Các tính toán được sử dụng thường xuyên thường được tích hợp sẵn vào phần mềm phân tích dưới dạng các **hàm (functions)**, tức là các công thức được xác định trước để thực hiện các tính toán. Một ví dụ là hàm `SUM` trong Microsoft Excel giúp cộng một dải các số trong các hàng hoặc các cột.

Các hàm giúp cho việc phân tích nhanh chóng lượng lớn dữ liệu mà không cần phải viết các công thức phức tạp. Thực tế, một trong những thuộc tính mạnh mẽ nhất của Microsoft Excel là các hàm được tích hợp sẵn để thực hiện tính toán. Hãy nhớ rằng các hàm phổ biến nhất và logic đằng sau chúng cũng áp dụng cho các phần mềm khác ngoài Microsoft Excel. Ví dụ, các hàm có thể được sử dụng trong các công cụ phân tích và trực quan hóa như Power BI và Tableau. Hiểu cách các hàm này hoạt động, và quan trọng hơn, là khi nào nên sử dụng chúng, là một kỹ năng phân tích dữ liệu cốt lõi.

### Các Hàm Cơ bản cho Phân tích Dữ liệu (Basic Functions for Data Analysis)

Hình minh họa 2.11 mô tả một số hàm Excel cơ bản được sử dụng trong phân tích dữ liệu:
- Tên hàm xuất hiện ở cột đầu tiên.
- Cột thứ hai hiển thị đối số của hàm (function argument), đó là cú pháp cần thiết để gọi hàm cùng với dải (range) và tiêu chí (criteria) để áp dụng cho nó. Tất cả các hàm Excel bắt đầu bằng một dấu bằng (=), tiếp theo là loại hàm được thực hiện, và sau đó là dấu ngoặc đơn chỉ định các đối số cho hàm. Ví dụ, để tính tổng một cột số trong cột C từ hàng 2 đến hàng 245, hàm sẽ là: `=SUM(C2:C245)`.
- Cách hàm tính toán được mô tả trong cột thứ ba.

**HÌNH MINH HỌA 2.11 (ILLUSTRATION 2.11) Các Hàm Microsoft Excel Cơ Bản**

![ILLUSTRATION 2.11](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.11.png)

Quay trở lại với ví dụ về dữ liệu của trường đại học, Hình minh họa 2.12 hiển thị hộp đối số hàm cho hàm `COUNTIF` được sử dụng để xác định trường đại học sở hữu bao nhiêu máy bơm (pumps). Có hai tùy chọn nhập liệu để thực thi các hàm được minh họa:
- Nhập trực tiếp đối số hàm vào một ô trên bảng tính, hoặc
- Sử dụng hộp **Function Arguments** (Đối số hàm).

**HÌNH MINH HỌA 2.12 (ILLUSTRATION 2.12) Hộp Đối số Hàm COUNTIF của Dữ liệu Tài sản Đại học**

![ILLUSTRATION 2.12](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.12.png)

Để mở hộp thoại:
- Nhấp vào biểu tượng `fx` cạnh thanh công thức ô, nằm phía trên bảng tính (xem biểu tượng `fx` màu xanh lá cây trong Hình minh họa 2.13).
- Tiếp theo, hộp nhập liệu Function Arguments như trong Hình minh họa 2.12 sẽ xuất hiện trên màn hình.
- Điền dải ô (range) và tiêu chí (criteria), rồi chọn OK. Công thức cho hàm sau đó sẽ xuất hiện (Hình minh họa 2.13). Lưu ý rằng tiêu chí (trong ví dụ này là "Pump") phải được gõ trong dấu ngoặc kép. Điều này áp dụng cho bất kỳ tiêu chí nào không phải là một tham chiếu ô hoặc một con số.

**HÌNH MINH HỌA 2.13 (ILLUSTRATION 2.13) Tìm Biểu tượng Đối số Hàm**

![ILLUSTRATION 2.13](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.13.png)

Các hàm Excel này có thể giúp phân tích nhanh các tập dữ liệu, đặc biệt khi chúng rất lớn. Bây giờ hãy áp dụng các hàm này để trả lời các câu hỏi từ một tập dữ liệu về tài sản cố định.

### Áp dụng Các Hàm Cơ bản của Excel (Applying Excel Basic Functions)

> **Data** Chúng ta sẽ sử dụng tập dữ liệu tài sản của trường đại học (Hình minh họa 2.14) để minh họa cách các hàm có thể giúp hiểu dữ liệu.

**HÌNH MINH HỌA 2.14 (ILLUSTRATION 2.14) Dữ liệu Tài sản Đại học**

![ILLUSTRATION 2.14](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.14.png)

Tập dữ liệu được tạo ra từ tệp University Asset Data:
- Mỗi hàng trong tập dữ liệu đại diện cho một tài sản duy nhất thuộc sở hữu của trường đại học.
- Các cột đại diện cho các thuộc tính của mỗi tài sản.

Có 13.127 hàng dữ liệu trong bảng tính này, nên việc quét chúng bằng mắt là không thể. Thay vào đó, hãy tận dụng các hàm Excel có sẵn. Tưởng tượng bạn chịu trách nhiệm xem xét các tài sản cố định cho trường đại học. Bạn có thể muốn đặt các câu hỏi được liệt kê trong Hình minh họa 2.15. Mỗi câu hỏi đều có thể được trả lời bằng một hàm Excel.

**HÌNH MINH HỌA 2.15 (ILLUSTRATION 2.15) Câu hỏi, Hàm và Câu trả lời Sử dụng Dữ liệu Tài sản Đại học**

![ILLUSTRATION 2.15](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.15.png)

Hình minh họa 2.15 sử dụng các hàm SUM, COUNTA, COUNTIF, SUMIF, và COUNTBLANK. Có thể sử dụng hàm SUMIFS hoặc COUNTIFS không?

Nếu câu hỏi là có bao nhiêu máy tính mà trường đại học đã mua vào năm 2023, thì hãy sử dụng hàm `COUNTIFS` vì có hai tiêu chí. Hãy nhớ rằng hàm `COUNTIFS` yêu cầu chỉ định dải ô để áp dụng cho tiêu chí đầu tiên (thiết bị máy tính). Tiêu chí tiếp theo là các giao dịch mua được thực hiện vào năm 2023, và dải ô sẽ là cột ghi ngày mua (dates acquired). Hình minh họa 2.16 hiển thị hộp Đối số Hàm cho hàm `COUNTIFS` và kết quả của nó.

**HÌNH MINH HỌA 2.16 (ILLUSTRATION 2.16) Các Đối số Hàm cho hàm COUNTIFS**

![ILLUSTRATION 2.16](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.16.png)

Hộp hàm tạo ra một công thức:
`=COUNTIFS(D2:D13127,"Computer Equipment",F2:F13127,">12/31/2022",F2:F13127,"<1/1/2024")`

Để chỉ lấy dữ liệu của năm 2023, tạo hai tiêu chí trong đối số hàm:
- Đầu tiên, ngày tháng phải lớn hơn 31 tháng 12 năm 2022 (Criteria2).
- Thứ hai, ngày tháng phải nhỏ hơn 1 tháng 1 năm 2024 (Criteria3).

Bằng cách bao gồm các tiêu chí đó trong đối số, chỉ những kết quả thuộc năm 2023 mới được hiển thị.

Các hàm cơ bản của Excel rất hữu ích để trả lời các câu hỏi có một câu trả lời duy nhất hoặc một câu trả lời với một chiều dữ liệu (dimension). **Các chiều dữ liệu (Dimensions)** là các biến hoặc các trường khác có thể được sử dụng để phân tích sâu (drill down) hoặc phân tách các thước đo phân tích. Nói cách khác, các chiều dữ liệu được sử dụng khi có một câu hỏi cụ thể về một khía cạnh cụ thể của dữ liệu.

Ví dụ, một câu hỏi về việc có bao nhiêu máy tính được mua trong năm 2023 chỉ có một chiều dữ liệu – máy tính trong năm 2023. Thế còn một câu hỏi có nhiều hơn một chiều dữ liệu thì sao? Sẽ ra sao nếu chúng ta muốn biết tổng chi phí cho mỗi danh mục tài sản thay vì chỉ riêng máy tính trong một năm cụ thể? Câu hỏi đó có nhiều hơn một chiều dữ liệu bởi vì nó liên quan đến mọi danh mục tài sản và tất cả các năm. Chúng ta sẽ thảo luận cách giải quyết các câu hỏi đa chiều trong phần tiếp theo.

---

### Áp dụng (Apply It 2.2)
**Phân tích Các Giao dịch Bán hàng với Các Hàm Excel (Analyze Sales Transactions with Excel Functions)**

**Kế toán Tài chính (Financial Accounting)** | **Kế toán Quản trị (Managerial Accounting)**

> **Data** Super Scooters sản xuất và bán bốn mẫu xe tay ga đứng: Celeritas, Captain, Lazer, và Kicks. Khách hàng của họ trải dài từ các công ty chia sẻ xe tay ga lớn đến các nhà bán lẻ nhỏ. Người giám sát của bạn đã đưa cho bạn (một kế toán viên của công ty) một danh sách các câu hỏi cần trả lời bằng cách sử dụng tập dữ liệu Super Scooters. Dưới đây là một phần của Các Giao dịch Bán hàng của Super Scooters cho các năm 2023–2025. Có 3.645 giao dịch trong cơ sở dữ liệu bán hàng.

Hãy giải thích hàm Microsoft Excel nào phù hợp nhất để trả lời các câu hỏi sau đây về dữ liệu bán hàng của Super Scooters.
1. Tổng doanh thu gộp (tính bằng đô la) là bao nhiêu?
2. Tổng doanh thu gộp (tính bằng đô la) cho năm 2023 là bao nhiêu?
3. Có bao nhiêu giao dịch bán hàng cho mẫu xe Lazer?
4. Doanh thu gộp trung bình cho mẫu xe Celeritas trong năm 2023 là bao nhiêu?
5. Có bao nhiêu chiếc mẫu xe Captain màu xanh lá (green) đã được bán?
6. Nếu Super Scooters muốn thêm một cột để chỉ ra liệu số ngày lưu bãi (days on the lot) có lớn hơn 50 ngày hay không, hàm nào sẽ phù hợp?

![Apply It 2.2](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.2.png)

## 2.3 Làm Thế Nào Chúng Ta Tổ Chức Các Tập Dữ Liệu Cho Phân Tích?

**MỤC TIÊU HỌC TẬP 3 (LEARNING OBJECTIVE 3)**
**Minh họa cách các pivot tables tổ chức và lọc dữ liệu.**

Bạn vừa học cách sử dụng các hàm để trả lời các câu hỏi với một chiều dữ liệu. Mặc dù bạn có thể sử dụng nhiều hàm để trả lời các câu hỏi liên quan đến nhiều chiều dữ liệu, nhưng sẽ hiệu quả hơn nếu trước tiên sử dụng một kỹ thuật tổ chức dữ liệu trên tập dữ liệu.

Tổ chức dữ liệu là quá trình sắp xếp lại dữ liệu để làm cho nó dễ hiểu hơn. **Pivot table** là một công cụ tóm tắt và sắp xếp lại các cột và hàng dữ liệu đã chọn trong một bảng tính, cơ sở dữ liệu, hoặc chương trình kinh doanh thông minh (business intelligence). Các Pivot tables có thể nhanh chóng sắp xếp lại dữ liệu để giúp trả lời nhiều câu hỏi kinh doanh quan trọng. Hãy nhớ lại từ phần góc nhìn chuyên gia mở đầu chương rằng Josh đã cần phải sử dụng một pivot table để tổ chức lại một bảng tính với 450.000 hàng dữ liệu. Thật khó tin rằng Josh có thể phân tích dữ liệu bảng tính một cách hiệu quả mà không cần đến pivot table.

Các ví dụ ở đây sử dụng Microsoft Excel để minh họa cách tạo và lọc một pivot table. (Lưu ý rằng các pivot table được tạo trong phần mềm này thường được dán nhãn là PivotTables). Mặc dù các minh họa sử dụng Excel PivotTables, các kỹ thuật này cũng được sử dụng trong các phần mềm phân tích dữ liệu khác. Ví dụ, chúng rất hữu ích khi tạo các biểu đồ trực quan. Bất kể bạn sử dụng công cụ phân tích dữ liệu nào, việc hiểu các chức năng cơ bản của việc tạo ra các pivot table hữu ích và cách lọc chúng là điều cần thiết.

### Sử dụng Pivot Tables

Vừa mạnh mẽ vừa dễ sử dụng, pivot table cũng là một trong những công cụ phổ biến nhất mà bạn sẽ sử dụng trong sự nghiệp kế toán của mình. Nó có năm thành phần chính:
1. **Các trường (Fields):** Các phần tử dữ liệu có sẵn để sử dụng trong pivot table.
2. **Các cột (Columns):** Khi một trường được chọn cho khu vực cột, chỉ những giá trị duy nhất của trường đó được liệt kê ngang qua phía trên cùng.
3. **Các hàng (Rows):** Khi một trường được chọn cho khu vực hàng, nó điền vào khu vực đó dưới dạng cột đầu tiên. Tất cả các giá trị hàng đều là các giá trị duy nhất và các giá trị trùng lặp bị loại bỏ.
4. **Các giá trị (Values):** Mỗi giá trị được giữ trong một ô của pivot table và hiển thị thông tin đã được tóm tắt. Ví dụ là tổng (sum), trung bình (average), hoặc đếm (count).
5. **Các bộ lọc (Filters):** Áp dụng một điều kiện giới hạn cho toàn bộ bảng.

Một khi bạn biết những điều cơ bản về việc tạo một pivot table trong Microsoft Excel, bạn có thể sử dụng công cụ này để trả lời các câu hỏi kế toán.

#### Tạo một Microsoft Excel PivotTable
Thực hiện theo các bước sau:
1. Mở bảng tính chứa dữ liệu cần tóm tắt.
2. Nhấp vào bất kỳ ô nào trong dữ liệu (ví dụ: ô đầu tiên ở hàng A trong Hình minh họa 2.17).
3. Nhấp vào tùy chọn **Insert** trên thanh menu (ribbon) phía trên cùng.
4. Một hộp tùy chọn nhập liệu **PivotTable** sẽ xuất hiện ở trên cùng bên trái của màn hình (Hình minh họa 2.17).

**HÌNH MINH HỌA 2.17 (ILLUSTRATION 2.17) Bảng tính Excel Dữ liệu Tài sản Đại học**

![ILLUSTRATION 2.17](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.17.png)

Khi tùy chọn này được chọn, một hộp thoại mới sẽ mở ra có tên là **PivotTable from table or range** (Hình minh họa 2.18).
5. Đảm bảo rằng dải ô **Table/Range** trong hộp *Select a table or range* phản ánh toàn bộ dữ liệu cần bao gồm. (Hãy nhớ bao gồm cả các tiêu đề cột). Chọn **New Worksheet** và nhấp **OK** (Hình minh họa 2.18).

**HÌNH MINH HỌA 2.18 (ILLUSTRATION 2.18) Hộp thoại Tạo PivotTable của Excel**

![ILLUSTRATION 2.18](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.18.png)

6. Điều này sẽ mở ra một bảng tính mới. Một vùng làm việc **PivotTable** trống sẽ xuất hiện ở bên trái, và hộp **PivotTable Fields** dùng để tạo PivotTable sẽ nằm ở bên phải (Hình minh họa 2.19).

**HÌNH MINH HỌA 2.19 (ILLUSTRATION 2.19) Vùng làm việc PivotTable trống**

![ILLUSTRATION 2.19](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.19.png)

Sử dụng hộp PivotTable Fields để chọn những gì sẽ xuất hiện trong PivotTable. Kéo tên cột vào một trong các khu vực rows, columns, values, hoặc filters.

> **Data** Hãy sử dụng PivotTables để trả lời các câu hỏi dữ liệu về tài sản của trường đại học. Nếu bạn đang xác minh tổng chi phí cho mỗi danh mục tài sản, bạn có thể muốn trả lời các câu hỏi sau:
> - Câu hỏi 1: Tổng số dư cho các tài sản trong mỗi danh mục là bao nhiêu?
> - Câu hỏi 2: Tổng số lượng tài sản trong mỗi danh mục là bao nhiêu?

#### Tìm Tổng Số dư theo Danh mục
Trả lời câu hỏi đầu tiên bằng cách tìm tổng số dư theo danh mục.
1. Kéo `Category` vào khu vực **Rows**.
2. Kéo `Amount` vào khu vực **Values**. Khi đó, `Σ Values` trong khu vực Columns sẽ tự động được Excel tạo ra.
3. Excel sẽ điền các giá trị cho mỗi danh mục vào cột thứ hai của bảng tính.

Hình minh họa 2.20 hiển thị PivotTable kết quả.

**HÌNH MINH HỌA 2.20 (ILLUSTRATION 2.20) Excel PivotTable cho Câu hỏi 1: Tổng Số dư theo Danh mục là bao nhiêu?**

![ILLUSTRATION 2.20](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.20.png)

4. Excel sẽ mặc định tính tổng (sum) của giá trị đó. Có thể thay đổi loại thước đo bằng cách nhấp vào mũi tên chỉ xuống trong trường `Sum of Amount` và chọn thước đo mong muốn (Hình minh họa 2.21).

**HÌNH MINH HỌA 2.21 (ILLUSTRATION 2.21) Hộp thoại Value Field Settings của Excel PivotTable**

![ILLUSTRATION 2.21](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.21.png)

Một tính năng hữu ích khác của hộp thoại Value Field Settings là khả năng thay đổi định dạng số (number format) trong PivotTable.

#### Xác định Tổng số Lượng Tài sản
Để xác định tổng số lượng tài sản trong mỗi danh mục (Câu hỏi 2), sử dụng PivotTable Excel đầu tiên:
1. Kéo `AssetTagID` vào khu vực **Values**.
2. Nhấp vào mũi tên chỉ xuống, chọn **Value Field Settings**, và chọn **Count**.
   Dữ liệu có thể được tóm tắt bằng một số phép tính khác nhau. Câu hỏi yêu cầu về số lượng tài sản mỗi danh mục, nên chọn **Count**.
3. Excel điền vào cột tiếp theo của bảng với số lượng theo danh mục tài sản.

Kết quả được hiển thị trong Hình minh họa 2.22.

**HÌNH MINH HỌA 2.22 (ILLUSTRATION 2.22) Excel PivotTable cho Câu hỏi 2: Tổng Số lượng Tài sản trong Mỗi Danh mục là bao nhiêu?**

![ILLUSTRATION 2.22](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.22.png)

### Lọc Pivot Tables (Filtering Pivot Tables)
Một cách để tập trung vào một khía cạnh cụ thể của dữ liệu trong PivotTable là sử dụng một bộ lọc (filter). Áp dụng bộ lọc có nghĩa là chỉ những dữ liệu phù hợp với tiêu chí của nó mới được hiển thị. Có ba cách để lọc trong Excel:
- Áp dụng các tiêu chí lọc vào khu vực **Filter**.
- Sử dụng **AutoFilter** trong trường Row của PivotTable.
- Chèn một hoặc nhiều **slicers**.

> **Data** Việc trả lời câu hỏi dữ liệu tài sản thứ ba sẽ minh họa cho mỗi tùy chọn lọc:
> Câu hỏi 3: Tổng số tiền mua sắm theo danh mục được thực hiện vào năm 2022 là bao nhiêu?

#### Áp dụng Các Tiêu chí Lọc vào Hộp Filter Field
Để khám phá tổng số tiền mua sắm theo danh mục cho năm 2022, hãy tạo một PivotTable hiển thị các tài sản được mua trong năm 2022 theo danh mục:
1. Kéo `Category` vào Rows, và kéo `Amount` vào Values.
2. Trọng tâm là các tài sản được mua trong năm 2022, vì vậy hãy đưa `Years` vào khu vực **Filters**.
3. Từ `Years` ở cột đầu tiên và từ `ALL` ở cột thứ hai lúc này sẽ xuất hiện ở phần trên cùng của PivotTable.
4. Nhấp vào mũi tên chỉ xuống bên cạnh `ALL` sẽ tạo ra một hộp thả xuống để chọn các năm cần lọc (Hình minh họa 2.23).

**HÌNH MINH HỌA 2.23 (ILLUSTRATION 2.23) Cách Lọc trong một Excel PivotTable**

![ILLUSTRATION 2.23](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.23.png)

Hình minh họa 2.24 cho thấy kết quả của việc lọc các tài sản được mua vào năm 2022.

**HÌNH MINH HỌA 2.24 (ILLUSTRATION 2.24) PivotTable Trả lời cho Câu hỏi 3: Tổng Chi phí của Các Tài sản Được Mua trong năm 2022 là bao nhiêu?**

![ILLUSTRATION 2.24](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.24.png)

#### Sử dụng một Row Auto Filter
Các bộ lọc cũng có thể được tạo ra trong một Excel PivotTable với chức năng **Auto Filter** cho các hàng. Trong ví dụ này, câu hỏi là có bao nhiêu tiền đã được chi cho thiết bị máy tính (Computer Equipment) trong năm 2022.
1. Thay vì thêm một danh mục vào khu vực Filter, hãy nhấp vào mũi tên chỉ xuống ở **Row Labels** để hiển thị các lựa chọn lọc khác.
2. Hình minh họa 2.25 hiển thị hộp thả xuống xuất hiện sau đó. Tại đây, bỏ chọn tất cả và chỉ chọn các danh mục tài sản muốn lọc.

**HÌNH MINH HỌA 2.25 (ILLUSTRATION 2.25) Excel PivotTable để Lọc chỉ cho Thiết bị Máy tính**

![ILLUSTRATION 2.25](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.25.png)

3. Trong ví dụ này, chỉ có Thiết bị Máy tính (Computer Equipment) được chọn. PivotTable kết quả được hiển thị trong Hình minh họa 2.26.

**HÌNH MINH HỌA 2.26 (ILLUSTRATION 2.26) Excel PivotTable Hiển thị Riêng Thiết bị Máy tính Được mua trong năm 2022**

![ILLUSTRATION 2.26](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.26.png)

Tùy chọn auto filter nhanh chóng cô lập một mục cụ thể. Hai tùy chọn auto filter khác là **Label Filters** và **Value Filters**. Hình minh họa 2.27 cho thấy các tùy chọn khả dụng sau khi chọn Label Filters.

**HÌNH MINH HỌA 2.27 (ILLUSTRATION 2.27) Label Filters của Excel PivotTables**

![ILLUSTRATION 2.27](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.27.png)

Làm nổi bật và nhấp vào một trong các tùy chọn dưới Label Filters sẽ mở ra một hộp thoại để chèn tham số của bộ lọc. Ví dụ, chọn **Equals** và nhập "Computer Equipment" vào hộp thoại (Hình minh họa 2.28) sẽ đạt được kết quả giống như Hình minh họa 2.26.

**HÌNH MINH HỌA 2.28 (ILLUSTRATION 2.28) Hộp thoại Equals của Excel PivotTable Label Filter**

![ILLUSTRATION 2.28](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.28.png)

Điều gì sẽ xảy ra nếu mục tiêu là lọc dữ liệu sao cho chỉ năm danh mục tài sản đứng đầu xuất hiện?
1. Sử dụng **Value Filters** và chọn tùy chọn cho **Top 10...** (Hình minh họa 2.29).

**HÌNH MINH HỌA 2.29 (ILLUSTRATION 2.29) Các Tùy chọn Value Filter của PivotTable**

![ILLUSTRATION 2.29](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.29.png)

2. Một hộp thoại sẽ mở ra cho phép thay đổi bộ lọc thành trên cùng (top) hoặc dưới cùng (bottom) và số lượng mục cần hiển thị.
Trong Hình minh họa 2.30, "Top 5" theo "Sum of amount" đã được chọn.

**HÌNH MINH HỌA 2.30 (ILLUSTRATION 2.30) Hộp Nhập liệu PivotTable Value Filter Cho Các Giá trị Hàng đầu**

![ILLUSTRATION 2.30](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.30.png)

Excel PivotTable kết quả được hiển thị trong Hình minh họa 2.31.

**HÌNH MINH HỌA 2.31 (ILLUSTRATION 2.31) Kết quả của PivotTable Value Filter Cho 5 Số tiền Hàng đầu**

![ILLUSTRATION 2.31](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.31.png)

Thế còn việc lọc theo nhiều chiều dữ liệu cùng một lúc thì sao?

#### Sử dụng Các Slicers để Lọc Dữ liệu
Việc lọc đồng thời nhiều chiều dữ liệu thường được gọi là **slicing**, hoặc slice and dice, đây là quá trình chia nhỏ dữ liệu thành các phần nhỏ hơn hoặc kiểm tra nó từ nhiều góc nhìn khác nhau. **Slicers** là một công cụ phân tích phân tách các thước đo phân tích kết quả theo các chiều dữ liệu đã chọn. Tất cả các phần mềm phân tích dữ liệu đều có khả năng slicing:
- Microsoft Excel và Power BI sử dụng slicers.
- Trong Tableau, việc này được thực hiện thông qua các bộ lọc tương tác (interactive filters).

Trong tất cả các loại phần mềm, các slicer tùy chỉnh tương tác với một tập dữ liệu bằng cách cung cấp một hiển thị trực quan các bộ lọc khả dụng. Hình minh họa 2.32 chỉ ra nơi có thể tìm thấy tùy chọn thêm slicer trong Microsoft Excel.

**HÌNH MINH HỌA 2.32 (ILLUSTRATION 2.32) Thêm Slicers vào PivotTables**

![ILLUSTRATION 2.32](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.32.png)

1. Nhấp vào trong PivotTable và chọn **Insert Slicer** từ menu. Điều này sẽ mở một hộp với tất cả các trường của PivotTable.
2. Chọn các trường cho các slicers. Nếu mục tiêu là xác định số tiền đã chi cho mỗi danh mục tài sản theo năm, thì hãy slice dữ liệu theo danh mục tài sản và năm. Để làm điều này, hãy chọn `Category` và `AcquisitionDate`.

Hình minh họa 2.33 hiển thị các slicers kết quả. Một cái dành cho danh mục (Category) và cái kia dành cho năm (Years).

**HÌNH MINH HỌA 2.33 (ILLUSTRATION 2.33) Slicers của PivotTable Giúp Khám Phá Tổng Số tiền theo Danh mục và Năm**

![ILLUSTRATION 2.33](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.33.png)

Trong Hình minh họa 2.33, nhấp vào `Computer Equipment` trong slicer Category và `2022` trong slicer Years sẽ mang lại một PivotTable với tổng số thiết bị máy tính được mua trong năm 2022.

Slicers cũng có thể được thêm vào Power BI bằng cách chọn công cụ slicer trong **Visualizations** (Hình minh họa 2.34).

**HÌNH MINH HỌA 2.34 (ILLUSTRATION 2.34) Pivot Table Slicers Sử dụng PowerBI**

![ILLUSTRATION 2.34](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.34.png)

Tiếp theo, hãy chọn Category để tạo các slicer cho danh mục và lặp lại đối với các slicer AcquisitionDate. Hình minh họa 2.35 cho thấy kết quả.

**HÌNH MINH HỌA 2.35 (ILLUSTRATION 2.35) Các Slicers của Power BI cho Category và Year**

![ILLUSTRATION 2.35](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.35.png)

Bởi vì các chức năng của pivot table tóm tắt dữ liệu để tìm ra câu trả lời một cách nhanh chóng cho các câu hỏi của chúng ta, việc tạo ra các pivot table là một kỹ năng phân tích dữ liệu cốt lõi mà bạn sẽ sử dụng thường xuyên trong sự nghiệp của mình.

---

### Áp dụng (Apply It 2.3)
**Phân tích Bán hàng với Excel PivotTables (Analyze Sales with Excel PivotTables)**

> **Data** **Kế toán Tài chính** | **Kế toán Quản trị** Người giám sát của bạn tại Super Scooters đã yêu cầu bạn phân tích doanh số bán hàng cho năm 2025 và doanh thu cho tất cả các năm. Hãy tạo một Excel PivotTable để xác định những điều sau:
1. Tổng doanh thu gộp (tính bằng đô la) cho mỗi địa điểm (location) trong năm 2025 là bao nhiêu?
2. Doanh thu gộp trung bình cho mỗi mẫu xe trong năm 2025 là bao nhiêu?
3. Tổng doanh thu mỗi năm là bao nhiêu?

**GIẢI PHÁP (SOLUTION)**
1. Chọn (hoặc kéo) các trường: `Location` vào **Rows**, `Gross Sales` vào **Values**, và `Year` vào **Filters**. Trong bộ lọc năm, hãy chọn 2025.

![Apply It 2.3_1](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.3_1.png)

2. Đảm bảo rằng `Model` ở khu vực **Rows**, `Gross Sales` ở khu vực **Values**, và `Year` ở khu vực **Filters** (chọn 2025). Nhấp vào mũi tên chỉ xuống bên cạnh `Sum of Gross Sales` và chọn **Value Field Settings** để thay đổi từ Sum thành Average.

![Apply It 2.3_2](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.3_2.png)

3. Kéo trường `Year` vào khu vực **Rows** thay vì Filters. Xóa Model khỏi khu vực Rows và định dạng khu vực **Values** thành Sum.

![Apply It 2.3_3](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.3_3.png)

## 2.4 Những Thước đo Mô tả Nào Giúp Chúng Ta Hiểu Dữ Liệu?

**MỤC TIÊU HỌC TẬP 4 (LEARNING OBJECTIVE 4)**
**Nhận diện các thước đo mô tả được sử dụng để thực hiện phân tích dữ liệu.**

Bạn đã học được cách xác định và trích xuất dữ liệu và một số phương pháp tiếp cận cơ bản để phân tích nó. Ở phần trước của khóa học, bạn cũng đã học được rằng có bốn loại phân tích dữ liệu:
- Phân tích Mô tả (Descriptive)
- Phân tích Chẩn đoán (Diagnostic)
- Phân tích Dự đoán (Predictive)
- Phân tích Kê toa (Prescriptive)

Hãy nhớ lại rằng phân tích mô tả giúp khám phá những gì đã hoặc đang xảy ra trong dữ liệu. Tại sao phân tích mô tả được coi là trọng tâm của phân tích dữ liệu? Không có sự hiểu biết cơ bản đó về dữ liệu, việc tiến tới các phương pháp phân tích dữ liệu phức tạp hơn là bất khả thi. Đôi khi phân tích mô tả là tất cả những gì cần thiết, nhưng thường thì phương pháp này là tiền thân cho các phân tích chẩn đoán, dự đoán, và kê toa. Kỹ năng phân tích dữ liệu cốt lõi cho phân tích mô tả là hiểu về thống kê mô tả (descriptive statistics) và phân tích tương quan (correlation analysis).

Thống kê mô tả khám phá các quan sát trung bình trong dữ liệu, hình dạng của dữ liệu và sự phân phối của dữ liệu. Ngoài ra, phân tích tương quan có thể chỉ ra các mối quan hệ trong dữ liệu. Cùng với nhau, các thống kê này cung cấp những hiểu biết sâu sắc về dữ liệu (data insights).

### Các thước đo vị trí (Measures of Location)
Các thước đo vị trí xác định quan sát trung bình (average), hoặc điển hình (typical), trong một tập dữ liệu.

#### Số Trung bình (Mean), Số Trung vị (Median), và Yếu vị (Mode)
Thước đo xu hướng tập trung (measure of central tendency) là một giá trị duy nhất mô tả một tập dữ liệu bằng cách xác định vị trí trung tâm trong tập dữ liệu đó. Có ba thước đo xu hướng tập trung:
- **Số Trung bình (Mean):** Tổng của tất cả các quan sát trong một tập dữ liệu chia cho tổng số lượng các quan sát.
- **Số Trung vị (Median):** Giá trị nằm ở giữa khi dữ liệu được sắp xếp từ nhỏ nhất đến lớn nhất.
- **Yếu vị (Mode):** Quan sát xuất hiện thường xuyên nhất.

Xác định mean và median là bước đầu tiên để hiểu dữ liệu trong phân tích mô tả. Hai thước đo này thường tương tự nhau, nhưng do mean có thể bị ảnh hưởng bởi các ngoại lệ (outliers - những giá trị cực đoan trong tập dữ liệu), nên có thể có một sự khác biệt lớn giữa chúng. Nếu có các ngoại lệ trong dữ liệu, thì median là đại diện tốt hơn cho giá trị trung tâm trong tập dữ liệu.

Mode hữu ích trong các tập dữ liệu có một lượng nhỏ các giá trị duy nhất. Ví dụ, một báo cáo tuổi nợ phải thu (accounts receivable aging report) có thể có các giá trị là 30, 60, và 90 ngày. Một mode của dữ liệu báo cáo tuổi nợ sẽ tiết lộ danh mục nào có nhiều quan sát nhất. Nếu có ít giá trị lặp lại, thì mode không phải là một thước đo hữu ích về xu hướng tập trung.

Excel được sử dụng ở đây để tính toán mean và median và diễn giải các kết quả, nhưng nhiều công cụ khác cũng có thể tính toán các giá trị mean và median. Trên thực tế, tất cả các phần mềm trực quan hóa dữ liệu đều có thể tính toán mean và median. Bất kể nó được tính toán như thế nào, có hai điều quan trọng:
- Hiểu cách tính toán các thước đo.
- Biết cách diễn giải kết quả.

#### Tính toán Các Thước đo Vị trí
Chúng ta sẽ sử dụng lại ví dụ về trường đại học để minh họa cách tính toán mean, median, và mode. Tuy nhiên, thay vì tài sản, chúng ta sẽ thực hiện phân tích mô tả về bảng lương của trường đại học.

> **Data** Hình minh họa 2.36 là một phần trích xuất từ tập dữ liệu bảng lương của trường đại học. Tập dữ liệu hiển thị cột chức danh nhân viên và mức lương hàng năm cho tất cả nhân viên của trường đại học (10.789 nhân viên).

Hai bước đầu tiên liên quan đến các hàm Excel:
1. Tính toán mean sử dụng hàm Excel `AVERAGE`. Công thức là `=AVERAGE(C2:C10790)`. Kết quả là $40,065.88.
2. Tính toán median sử dụng hàm Excel `MEDIAN`. Công thức là `=MEDIAN(C2:C10790)`. Kết quả là $28,276.00.

Việc so sánh hai thước đo cho thấy có một sự chênh lệch lớn giữa mức lương trung bình (mean) và mức lương trung vị (median) cho một nhân viên ($11,789.88). Điều gì có thể gây ra hiện tượng này? Hãy nhớ rằng, mean có thể bị ảnh hưởng bởi các ngoại lệ. Dữ liệu có thể được kiểm tra thêm để xác định xem có số tiền lương nào cực kỳ cao hoặc thấp hay không.
3. Cuối cùng, sử dụng tùy chọn bộ lọc (filter) của Excel trong tệp dữ liệu để lọc các mức lương từ cao nhất xuống thấp nhất.

Hình minh họa 2.37 hiển thị năm mức lương cao nhất và năm mức lương thấp nhất.

**HÌNH MINH HỌA 2.36 (ILLUSTRATION 2.36) Dữ liệu Bảng lương Đại học**

![ILLUSTRATION 2.36](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.36.png)

**HÌNH MINH HỌA 2.37 (ILLUSTRATION 2.37) Các Mức lương Đại học từ Cao nhất đến Thấp nhất**

![ILLUSTRATION 2.37](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.37.png)

Xét về mức lương mean cao hơn bao nhiêu so với median, rất có thể có nhiều mức lương ở số tiền thấp hơn là số tiền cao hơn. Chúng ta có thể hiểu rõ hơn về sự khác biệt giữa các mức lương mean và median bằng cách xem xét mức độ biến động (variation) trong dữ liệu.

### Các thước đo độ phân tán (Measures of Dispersion)
Trong ví dụ về tiền lương, đã có một sự khác biệt lớn giữa số tiền lương mean và median. **Các thước đo độ phân tán (measures of dispersion)**, mô tả mức độ biến động trong dữ liệu, có thể giúp tìm ra nguyên nhân của sự chênh lệch này. Dữ liệu bị dàn trải hay co cụm lại với nhau? Nói cách khác, khoảng cách từ tất cả các quan sát, hay các điểm dữ liệu, đến giá trị mean là bao xa?

#### Phương sai (Variance) và Độ lệch chuẩn (Standard Deviation)
Có hai thước đo độ phân tán được sử dụng rộng rãi:
- **Phương sai (Variance)** là trung bình bình phương khoảng cách giữa các điểm dữ liệu trong tập dữ liệu và giá trị mean.
- **Độ lệch chuẩn (Standard deviation)** là căn bậc hai của phương sai.

Mặc dù phương sai là cần thiết để tính toán độ lệch chuẩn, nhưng thông thường chỉ có độ lệch chuẩn được báo cáo vì nó dễ diễn giải hơn phương sai. Nó dễ hiểu hơn bởi vì nó có cùng đơn vị đo với mean. Trong ví dụ về bảng lương đại học, độ lệch chuẩn sẽ được tính bằng đô la của mức lương hàng năm.

#### Tính toán Các Thước đo Độ phân tán
> **Data** Các thước đo độ phân tán có thể được tính toán bằng cách sử dụng Microsoft Excel (Hình minh họa 2.38).

**HÌNH MINH HỌA 2.38 (ILLUSTRATION 2.38) Dữ liệu Bảng lương Đại học**

![ILLUSTRATION 2.38](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.38.png)

Một lần nữa, tính toán các thước đo này bằng cách thực hiện các phép tính trong Excel:
1. Tính phương sai sử dụng hàm Excel `VAR`. Công thức là `=VAR(C2:C10790)`. Kết quả là $1,939,797,496.92
2. Tiếp theo, tính độ lệch chuẩn sử dụng hàm Excel `STDEV`. Công thức là `=STDEV(C2:C10790)`. Kết quả là $44,043.13

Mặc dù không có sự diễn giải thực tế về con số phương sai, nhưng có sự diễn giải cho độ lệch chuẩn:
- Một độ lệch chuẩn thấp cho thấy các quan sát trong tập dữ liệu có xu hướng gần với giá trị mean của tập dữ liệu đó.
- Một độ lệch chuẩn cao cho thấy các giá trị dàn trải qua một phạm vi rộng hơn.

Trong ví dụ này, độ lệch chuẩn $44,043.14 chỉ ra rằng một quan sát, trong trường hợp này là tiền lương hàng năm của một nhân viên, trong tập dữ liệu có thể chênh lệch $44,043.14 so với mean. Nhớ lại rằng mean là $40,068.88, do đó $44,043.14 sẽ được coi là một độ lệch chuẩn cao.

Một cách khác để đánh giá độ phân tán là sử dụng một biểu đồ phân tán (scatterplot - hay còn gọi là scatter chart) để trực quan hóa dữ liệu (Hình minh họa 2.39).

**HÌNH MINH HỌA 2.39 (ILLUSTRATION 2.39) Biểu đồ phân tán Bảng lương Đại học**

![ILLUSTRATION 2.39](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.39.png)

Tiền lương phân tán rộng rãi giữa $0 và cao hơn một chút so với $450,000. Trực quan hóa dữ liệu này trùng khớp với độ lệch chuẩn lớn ở mức $44,043.14.

### Các thước đo hình dạng (Measures of Shape)
Ngoài việc hiểu về độ phân tán của dữ liệu, việc hiểu sự phân phối, hay hình dạng của nó cũng rất quan trọng. **Các thước đo hình dạng (Measures of shape)** mô tả sự phân phối của dữ liệu trong tập dữ liệu. Cách một tập dữ liệu được định hình có thể tiết lộ thước đo xu hướng tập trung tốt nhất nên được sử dụng, hoặc nó có thể hiển thị các mẫu hình trong dữ liệu.

#### Hệ số Bất đối xứng (Skewness) và Độ nhọn (Kurtosis)
Các tập dữ liệu thường có hình dạng đối xứng hoặc không đối xứng. Trong một phân phối đối xứng, mean, median, và mode đều bằng nhau và phân phối dữ liệu ở bên phải của mean giống hệt với dữ liệu ở bên trái của mean. Một phân phối đối xứng sẽ trông giống như một đường cong hình chuông (bell curve) trong một biểu đồ (Hình minh họa 2.40).

**HÌNH MINH HỌA 2.40 (ILLUSTRATION 2.40) Phân phối Đối xứng (Symmetrical Distribution)**

![ILLUSTRATION 2.40](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.40.png)

Hình dạng của phân phối có thể được xác định bằng cách vẽ biểu đồ dữ liệu hoặc bằng cách sử dụng hai thước đo thống kê. Thường thì cả hai đều phù hợp. Hai thước đo hình dạng là skewness (độ lệch/hệ số bất đối xứng) và kurtosis (độ nhọn).

**Skewness** mô tả sự thiếu đối xứng của dữ liệu:
- Các phân phối có đuôi kéo dài về bên phải của mean được coi là **lệch phải (positively skewed)**.
- Các phân phối có đuôi kéo dài về bên trái của mean là **lệch trái (negatively skewed)**.

**HÌNH MINH HỌA 2.41 (ILLUSTRATION 2.41) Các Ví dụ về Độ Lệch (Skewness)**

![ILLUSTRATION 2.41](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.41.png)

**Hệ số bất đối xứng (coefficient of skewness - CS)** đo lường độ lệch của một phân phối. Nếu CS là âm, thì dữ liệu lệch trái. Nếu CS là dương, dữ liệu lệch phải. Mức độ lệch có thể được diễn giải thông qua giá trị tuyệt đối của CS:
- |CS| > 1, mức độ lệch cao
- 0.5 ≤ |CS| ≤ 1, độ lệch vừa phải
- |CS| < 0.5, tương đối đối xứng

Tính hệ số bất đối xứng bằng cách sử dụng hàm Excel `=SKEW(data range)`. 
> **Data** Hình minh họa 2.42 hiển thị hàm Excel và kết quả sử dụng tệp dữ liệu bảng lương đại học. CS là dương 2.3, cho thấy dữ liệu có mức độ lệch cao và lệch về bên phải.

**HÌNH MINH HỌA 2.42 (ILLUSTRATION 2.42) Độ lệch (Skewness) và Độ nhọn (Kurtosis) của Dữ liệu Bảng lương Đại học**

![ILLUSTRATION 2.42](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.42.png)

**Kurtosis** đề cập đến mức độ nhọn (peaked) hoặc dẹt (flat) của biểu đồ tần suất dữ liệu. **Hệ số độ nhọn (coefficient of kurtosis - CK)** đo lường mức độ nhọn của một phân phối:
- Nếu CK lớn hơn 3, thì dữ liệu hơi nhọn với độ phân tán ít hơn.
- Nếu CK nhỏ hơn 3, dữ liệu hơi dẹt với mức độ phân tán rộng.

Hệ số độ nhọn có thể được tính trong Excel bằng cách sử dụng hàm `=KURT(data range)`.
Hình minh họa 2.42 cho thấy CK của dữ liệu lương đại học là 8.2. Điều này cho thấy dữ liệu rất nhọn với ít độ phân tán.

#### Các Phân phối Tần số (Frequency Distributions) và Biểu đồ Tần suất (Histograms)
Cùng với các thước đo CS và CK, hình dạng của phân phối có thể được trực quan hóa bằng hai thước đo khác:
- Một **phân phối tần số (frequency distribution)** là một đại diện của dữ liệu tóm tắt số lượng các quan sát trong một khoảng nhất định. Ví dụ, số lượng nhân viên theo các nhóm mức lương.
- Một **biểu đồ tần suất (histogram)** là một biểu đồ cột của một phân phối tần số, trong đó chiều cao của cột phản ánh tần số (frequency) trong khoảng đó. Ví dụ, chúng ta có thể muốn nhóm các mức lương theo từng số tiền $10,000, $20,000, và $30,000 rồi sau đó đếm xem có bao nhiêu nhân viên ở mỗi hạng mục.

Các thước đo này có thể được tạo trong các phần mềm trực quan hóa dữ liệu như Power BI, Tableau, và trong Microsoft Excel bằng cách sử dụng công cụ Analysis Toolpak. Analysis Toolpak là một tiện ích bổ sung (add-on) miễn phí cho Excel. Một khi được thêm vào, nó sẽ nằm dưới thẻ Data. Hình minh họa 2.43 hiển thị nơi để tìm công cụ Data Analysis và hộp thoại tương ứng mở ra sau khi nhấp vào Data Analysis.

**HÌNH MINH HỌA 2.43 (ILLUSTRATION 2.43) Công cụ Data Analysis của Excel**

![ILLUSTRATION 2.43](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.43.png)

1. Để chuẩn bị một biểu đồ histogram và phân phối tần số, hãy chọn **Histogram** và nhấp **OK**.
2. Một hộp thoại sẽ mở ra (Hình minh họa 2.44).
3. Có hai hộp đầu vào (input boxes):
   - **Input Range** là dữ liệu sẽ được trực quan hóa. Việc chọn tiêu đề cột và đánh dấu chọn hộp **Labels** là rất hữu ích để histogram được dán nhãn bằng tiêu đề của dữ liệu đang được trực quan hóa (Hình minh họa 2.44).
   - Hộp đầu vào tiếp theo là **Bin Range**, dùng để xác định các nhóm được sử dụng cho phân phối tần số và các cột histogram. Chúng phải được thiết lập trước khi mở hộp thoại. Tạo Bin Range bằng cách thiết lập một cột chứa các giá trị dùng để nhóm dữ liệu. Nhìn chung, các giá trị này nên ở các mức tăng bằng nhau và số lượng nhóm nên từ 5 đến 15.
4. Cuối cùng, chọn nơi kết quả sẽ được xuất ra. Hãy đảm bảo đánh dấu kiểm hộp **Chart Output** trước khi nhấp OK.

**HÌNH MINH HỌA 2.44 (ILLUSTRATION 2.44) Hộp thoại Histogram**

![ILLUSTRATION 2.44](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.44.png)

Làm thế nào bạn biết cần tạo bao nhiêu nhóm? Cách tốt nhất là thử nghiệm với dữ liệu để tìm ra một con số sẽ tạo ra một sự trực quan hóa hữu ích. Ví dụ, việc sử dụng ít nhóm hơn có nghĩa là độ rộng của các nhóm sẽ rộng hơn và trực quan hóa có thể cung cấp cái nhìn chi tiết kém hơn. Thường thì việc chia khoảng (giá trị lớn nhất – giá trị nhỏ nhất) cho số lượng nhóm bạn muốn hiển thị có thể là một điểm bắt đầu tốt.

> **Data** Các bước này có thể được sử dụng để tạo một histogram với tệp dữ liệu bảng lương đại học:
1. Mở bảng tính và tạo một cột cho các khoảng chia (bins).
2. Đầu tiên, xác định khoảng dữ liệu. Mức lương tối thiểu là $78.00 và mức lương tối đa là $468,675.00, cho thấy có một phạm vi dữ liệu rộng. Tạo 12 nhóm (bins), bắt đầu bằng $8,000 với khoảng tăng (increments) là $20,000 (Hình minh họa 2.45).

**HÌNH MINH HỌA 2.45 (ILLUSTRATION 2.45) Dữ liệu Bảng Lương, Các Bins, và Hộp thoại Histogram**

![ILLUSTRATION 2.45](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.45.png)

Kết quả từ hộp thoại histogram được trình bày trong Hình minh họa 2.46.

**HÌNH MINH HỌA 2.46 (ILLUSTRATION 2.46) Phân phối Tần số và Histogram Dữ liệu Bảng lương Đại học**

![ILLUSTRATION 2.46](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.46.png)

Histogram tiết lộ một số thông tin về hình dạng của tập dữ liệu, bao gồm việc hầu hết dữ liệu được nhóm lại trong khoảng từ $8,000 đến $48,000:
- Dữ liệu sau đó mỏng dần về bên phải. Điều này củng cố cho kết quả của các thước đo vị trí và hình dạng. Nhớ lại rằng median của dữ liệu là $28,276.00, và mean là $40,065.88. Dữ liệu đạt đỉnh tại giá trị mode.
- Dữ liệu sau đó kéo dài thành một đuôi về phía bên phải, điều này củng cố cho kết quả về hệ số bất đối xứng là một số dương 2.3.
- Cuối cùng, dữ liệu rất nhọn. Phần lớn (69%) nằm trong ba cột đầu tiên của histogram. Điều này hỗ trợ cho kết quả hệ số độ nhọn (kurtosis) là 8.2, chỉ ra rằng dữ liệu có độ nhọn cao và ít phân tán.

#### Các Công cụ Thống kê Mô tả
Bây giờ bạn đã học cách tính toán các thước đo vị trí, độ phân tán và hình dạng bằng cách sử dụng các hàm Excel đơn lẻ. Có một công cụ Excel khác, **Descriptive Statistics**, có thể tính toán tất cả các thước đo này cùng một lúc (Hình minh họa 2.47):
1. Chọn Descriptive Statistics từ danh sách Analysis Tools.
2. Sử dụng hộp thoại Descriptive Statistics để nhập vào phạm vi dữ liệu cần phân tích.
3. Khi phạm vi dữ liệu đã được nhập, chọn labels (nếu bạn đã chọn hàng có chứa tiêu đề cột), chọn nơi xuất kết quả, chọn Summary statistics, và nhấp OK.

**HÌNH MINH HỌA 2.47 (ILLUSTRATION 2.47) Công cụ và Hộp thoại Descriptive Statistics trong Excel**

![ILLUSTRATION 2.47](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.47.png)

Excel sau đó sẽ tính toán các thống kê mô tả và in kết quả trên một trang tính mới (Hình minh họa 2.48).

**HÌNH MINH HỌA 2.48 (ILLUSTRATION 2.48) Các Thống kê Mô tả về Dữ liệu Lương Đại học**

![ILLUSTRATION 2.48](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.48.png)

Các phần mềm thống kê thường có một tính năng tương tự để tính toán đồng thời nhiều số liệu thống kê mô tả. Dù chúng ta sử dụng nhiều hàm Excel riêng lẻ hoặc chỉ sử dụng một công cụ để tính toán, việc khám phá ra hình dạng của một tập dữ liệu giúp chúng ta hiểu dữ liệu tốt hơn. Còn có một thành phần quan trọng khác - đó là hiểu các mối quan hệ bên trong một tập dữ liệu.

### Phân tích Tương quan (Correlation Analysis)
Phân tích tương quan có thể khám phá các mối quan hệ trong dữ liệu bằng cách đo lường mối quan hệ tuyến tính giữa hai biến. Bước đầu tiên là hiểu cách các biến có tương quan với nhau, và bước thứ hai là thực hiện tính toán sự tương quan.

#### Diễn giải Các Hệ số Tương quan
Tương quan tuyến tính của các biến liên tục được đo lường bằng **hệ số tương quan (correlation coefficient)**, còn được gọi là Hệ số Tương quan Pearson (Pearson Product Moment Correlation Coefficient). Thước đo này là một giá trị số nằm giữa -1 và +1. Giá trị tuyệt đối của số càng cao thì sức mạnh của mối quan hệ càng lớn.

Một tương quan có thể là âm, bằng 0, hoặc dương (Hình minh họa 2.49):
- **Tương quan âm (negative correlation)** là một mối quan hệ nghịch đảo. Khi một biến tăng, biến kia sẽ giảm. Có một mối quan hệ âm giữa doanh số bán súp và nhiệt độ bởi vì khi nhiệt độ giảm thì doanh số bán súp lại tăng.
- **Không có tương quan (No correlation)** chỉ ra rằng không có mối quan hệ giữa các biến. Ví dụ, chúng ta sẽ không kỳ vọng nhiệt độ ngoài trời có bất kỳ tác động nào đến doanh số bán ngũ cốc.
- **Hệ số tương quan dương (positive correlation)** chỉ ra rằng khi một biến tăng, thì biến kia cũng tăng. Chúng ta kỳ vọng có một mối quan hệ dương giữa doanh số bán kem và nhiệt độ ngoài trời. Khi nhiệt độ tăng, doanh số bán kem cũng có xu hướng tăng theo.

**HÌNH MINH HỌA 2.49 (ILLUSTRATION 2.49) Các Ví dụ Về Tương quan**

![ILLUSTRATION 2.49](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.49.png)

Chúng ta cũng có thể xem xét mức độ mạnh yếu của một mối quan hệ. Hệ số tương quan càng cao, nằm giữa mức âm 1 và dương 1, thì mối tương quan càng mạnh. Hình minh họa 2.50 là một hướng dẫn để xác định xem một hệ số tương quan biểu thị một mối quan hệ yếu, vừa phải, hay mạnh.

**HÌNH MINH HỌA 2.50 (ILLUSTRATION 2.50) Diễn giải Các Hệ số Tương quan**

![ILLUSTRATION 2.50](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.50.png)

Hãy tưởng tượng bạn đang kiểm tra mối quan hệ giữa doanh số bán kem và nhiệt độ ngoài trời. Nếu hệ số tương quan của doanh số bán và nhiệt độ là dương 0.75, thì có một mối quan hệ dương mạnh mẽ giữa doanh số bán và nhiệt độ. Khi nhiệt độ tăng, doanh số bán kem tăng và ngược lại. (Hình minh họa 2.51)

**HÌNH MINH HỌA 2.51 (ILLUSTRATION 2.51) Ví dụ Về Tương quan Dương**

![ILLUSTRATION 2.51](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.51.png)

Giả sử thay vào đó chúng ta đang kiểm tra mối quan hệ giữa chi phí sưởi ấm và nhiệt độ, và hệ số tương quan là âm 0.70 (Hình minh họa 2.52).

**HÌNH MINH HỌA 2.52 (ILLUSTRATION 2.52) Ví dụ Về Tương quan Âm**

![ILLUSTRATION 2.52](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.52.png)

Trong trường hợp này, có một sự tương quan âm mạnh mẽ giữa chi phí sưởi ấm và nhiệt độ. Khi nhiệt độ giảm, chi phí sưởi ấm một ngôi nhà sẽ tăng và ngược lại.

#### Thực hiện Phân tích Tương quan
Tương quan có thể được đánh giá một cách trực quan bằng cách chuẩn bị một biểu đồ phân tán (scatterplot), giống như những biểu đồ trong Hình minh họa 2.49, và sau đó vẽ một đường. Điều này sẽ cho biết liệu có tồn tại sự tương quan hay không và liệu nó là dương hay âm.

Hệ số tương quan có thể được tính bằng tay với một công thức hoặc bằng phần mềm. Tất cả các phần mềm thống kê đều có thể tính toán một hệ số tương quan, bao gồm cả Microsoft Excel (được sử dụng trong ví dụ này). Bất kể phần mềm nào được sử dụng, việc giải thích kết quả đều giống nhau. Có hai cách để thực hiện phân tích tương quan trong Excel:
- Sử dụng hàm `CORREL`.
- Sử dụng tùy chọn Correlation trong công cụ Data Analysis.

Lợi ích của việc sử dụng tùy chọn Correlation trong công cụ Data Analysis là có thể tạo một bảng tương quan cho nhiều biến cùng lúc. 
> **Data** Chúng ta sử dụng dữ liệu bảng lương đại học để minh họa tùy chọn tương quan trong Excel và sau đó diễn giải kết quả.

Trong tab Salary Hours của tệp dữ liệu (Hình minh họa 2.53), hãy thực hiện một phân tích tương quan để xem có tương quan nào giữa mức lương hàng năm và số giờ làm việc hay không.

**HÌNH MINH HỌA 2.53 (ILLUSTRATION 2.53) Dữ liệu Lương và Giờ làm việc của Đại học**

![ILLUSTRATION 2.53](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.53.png)

Hình minh họa 2.54 hiển thị hộp thoại tương quan mở ra sau khi nhấp vào Correlation và chọn OK trong trình đơn thả xuống Data Analysis Tools. Input range trong hộp thoại chứa các cột đang được kiểm tra tương quan. Ví dụ này đang kiểm tra sự tương quan giữa cột G (Annual Salary) từ các hàng 1 – 10790, và cột H (Hours Worked) từ các hàng 1 – 10790.

**HÌNH MINH HỌA 2.54 (ILLUSTRATION 2.54) Công cụ Data Analysis và Hộp thoại Tương quan**

![ILLUSTRATION 2.54](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.54.png)

Hộp thoại trong Hình minh họa 2.54 hiển thị các dữ liệu đầu vào cần thiết để chạy phân tích tương quan. Kết quả của phân tích tương quan được trình bày trong Hình minh họa 2.55:
- Hệ số tương quan là 0.552.
- Có một sự tương quan dương vừa phải giữa mức lương hàng năm và số giờ làm việc.

Nói cách khác, khi số giờ làm việc tăng thì mức lương hàng năm cũng tăng theo.

**HÌNH MINH HỌA 2.55 (ILLUSTRATION 2.55) Phân tích Tương quan Lương Đại học**

![ILLUSTRATION 2.55](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.55.png)

Tại sao lại không có một mối tương quan mạnh mẽ hơn? Một mối tương quan mạnh giữa số giờ làm việc và mức lương hàng năm được trả dường như hợp lý. Tuy nhiên, nếu nhân viên được trả một mức lương cố định hàng năm thay vì trả theo giờ, thì điều đó sẽ làm giảm sự tương quan đối với số giờ.

Phân tích tương quan có thể giúp khám phá các mối quan hệ trong dữ liệu và hiểu được sức mạnh của chúng. Nhưng đừng bao giờ đưa ra giả định rằng một biến này là nguyên nhân làm thay đổi biến kia chỉ vì có sự tương quan giữa hai biến. Rất có thể tìm thấy sự tương quan giữa hai biến mà chẳng liên quan gì đến nhau. Đây là một **tương quan giả (spurious correlation)**, xảy ra khi có một mối quan hệ về mặt toán học nhưng lại không có logic giữa hai biến. Luôn luôn phải đảm bảo các mối tương quan đó là hợp lý (make sense) trước khi sử dụng chúng để đưa ra các quyết định.

---

### Áp dụng (Apply It 2.4)
**Sử dụng Thống kê Mô tả để Kiểm toán Chi phí Bảo hành (Use Descriptive Statistics to Audit Warranty Expense)**

> **Data** **Kiểm toán (Auditing)**
Là một kiểm toán viên độc lập (external auditor), bạn được giao phụ trách hợp đồng kiểm toán cho Super Scooters. Một trong những trách nhiệm của bạn là xem xét chi phí bảo hành (warranty expense). Như trong hình minh họa, chi phí bảo hành trung bình của Super Scooters đã tăng trong 3 năm qua.

![Apply It 2.4_1](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.4_1.png)

Để phân tích chi phí bảo hành, bạn quyết định sử dụng thống kê mô tả (descriptive statistics). Thực hiện các phân tích sau đây và diễn giải các kết quả của bạn.
1. Sử dụng tùy chọn Descriptive Statistics trong công cụ Data Analysis để tính toán các thống kê mô tả cho chi phí bảo hành từ 2023 đến 2025. Diễn giải các thước đo sau:
   - Mean (Số trung bình)
   - Median (Số trung vị)
   - Standard deviation (Độ lệch chuẩn)
   - Kurtosis (Độ nhọn)
   - Skewness (Độ lệch)
2. Thực hiện các thống kê mô tả cho chi phí bảo hành trong năm 2025. Diễn giải các thước đo sau:
   - Mean
   - Median
   - Kurtosis
   - Skewness
3. Chuẩn bị một biểu đồ histogram của Chi phí Bảo hành năm 2025 với các khoảng chia (bins) sau: 200, 400, 600, 800, 1000, 1200, và 1400.
   - Lập biểu đồ dữ liệu.
   - Hình dạng và sự phân phối trong histogram của bạn có hỗ trợ các thước đo về độ nhọn (kurtosis) và độ lệch (skewness) không?

**GIẢI PHÁP (SOLUTION)**
1. Các thống kê mô tả cho chi phí bảo hành từ 2023 đến 2025:

![Apply It 2.4_2](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.4_2.png)

*Diễn giải các thước đo (Measure Interpretation):*
**Thước đo** | **Kết quả** | **Diễn giải**
--- | --- | ---
**Mean** | Mức chi phí bảo hành trung bình cho giai đoạn 3 năm là $343.57. | Chi phí bảo hành trung bình cho tất cả 3,645 đơn hàng bán trong giai đoạn 3 năm là $343.57.
**Median** | Mức chi phí bảo hành trung vị cho giai đoạn 3 năm là $300.00. | Giá trị ở giữa của chi phí bảo hành trong giai đoạn 3 năm, khi xếp hạng chi phí bảo hành từ cao xuống thấp, là $300.
**Standard deviation** | Độ lệch chuẩn trong giai đoạn 3 năm là $244.90. | Đây là một độ lệch chuẩn cao khi so sánh với mean và median. Nó cho thấy một sự phân tán rộng trong các chi phí bảo hành.<br>Đối với bất kỳ lần bán hàng nào, chi phí bảo hành có thể tăng hoặc giảm + / − $244.90 so với giá trị mean.
**Kurtosis** | Hệ số độ nhọn là 1.54. | Giá trị này nhỏ hơn 3, chỉ ra rằng hình dạng của phân phối hơi dẹt với mức độ phân tán rộng.
**Skewness** | Hệ số bất đối xứng là một số dương 1.23. | Giá trị này lớn hơn 1, chỉ ra rằng dữ liệu đạt đỉnh ở quanh giá trị mean và sau đó kéo thành một đuôi sang bên phải.

2. Các thống kê mô tả cho chi phí bảo hành năm 2025:

![Apply It 2.4_3](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.4_3.png)

*Diễn giải các thước đo (Measure Interpretation):*
**Thước đo** | **Kết quả** | **Diễn giải**
--- | --- | ---
**Mean** | Mức chi phí bảo hành trung bình cho năm 2025 là $414.18. | Giá trị này cao hơn so với mức trung bình của ba năm được tìm thấy trong câu hỏi 1.
**Median** | Chi phí bảo hành trung vị cho năm 2025 là $330.00. | Giá trị này đại diện cho điểm chính giữa của sự phân phối nếu dữ liệu được sắp xếp từ thấp đến cao.
**Kurtosis** | Hệ số độ nhọn là 0.93. | Giá trị này nhỏ hơn 3, chỉ ra rằng hình dạng của phân phối có hơi dẹt với mức độ phân tán rộng.
**Skewness** | Hệ số bất đối xứng là số dương 1.18. | Giá trị này lớn hơn 1, chỉ ra rằng dữ liệu có đạt đỉnh xung quanh giá trị mean và sau đó đuôi kéo dài về bên phải.

3. Biểu đồ tần suất (Histogram):

![Apply It 2.4_4](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.4_4.png)

Đúng vậy, hệ số độ nhọn (kurtosis) chỉ ra một sự phân tán rộng. Chi phí bảo hành bị dàn trải từ $200 cho đến $1,200:
- Có ba đỉnh so với việc chỉ có một đỉnh nhọn duy nhất. Hệ số bất đối xứng (skewness) chỉ ra rằng dữ liệu đạt đỉnh ở xung quanh giá trị mean và sau đó có đuôi kéo về bên phải.
- Đỉnh cao nhất nằm ở quanh giá trị mean $414 và sau đó mỏng dần về bên phải.

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

## Câu Hỏi Trắc Nghiệm (Multiple Choice Questions)

1. (LO 1) Một tập hợp các dữ liệu có liên quan logic với nhau, có thể được truy xuất, thao tác và cập nhật để đáp ứng nhu cầu của người dùng được gọi là
a. bảng (table).
b. cơ sở dữ liệu quan hệ (relational database).
c. tập dữ liệu (data set).
d. kho dữ liệu (data warehouse).

2. (LO 1) Trong một bảng cơ sở dữ liệu quan hệ, một khóa chính (primary key)
a. không phải lúc nào cũng cần thiết.
b. giống như một khóa ngoại (foreign key).
c. là một giá trị duy nhất (unique value).
d. có thể được lặp lại trong bảng nếu cần.

3. (LO 1) Các bảng trong một cơ sở dữ liệu có thể nằm trong các yếu tố nào sau đây?
a. Tài sản, nợ phải trả, chi phí
b. Nguồn lực, chi phí, nhân viên
c. Doanh thu, sự kiện, tác nhân
d. Nguồn lực, sự kiện, tác nhân (Resources, events, agents)

4. (LO 1) Các cột trong một cơ sở dữ liệu phản ánh
a. các thuộc tính (attributes).
b. các sự kiện (events).
c. các nguồn lực (resources).
d. các tác nhân (agents).

5. (LO 1) Một yêu cầu dữ liệu từ một cơ sở dữ liệu nhằm lấy ra hoặc thao tác trên nó được gọi là
a. phân tích dữ liệu (data analysis).
b. một truy vấn (a query).
c. một câu hỏi (a question).
d. một kết nối (a join).

6. (LO 1) Khi thực hiện một phép kết nối (join) giữa hai bảng, nếu kết quả trả về là một giá trị rỗng (null value), điều đó chỉ ra rằng
a. giá trị bằng không.
b. phép kết nối không chính xác.
c. giá trị không tồn tại trong cơ sở dữ liệu.
d. một inner join đã được thực hiện.

7. (LO 1) Phép kết nối nào dẫn đến việc truy xuất tất cả các bản ghi từ bảng bên trái và các bản ghi khớp từ bảng bên phải?
a. Inner
b. Left
c. Right
d. Full

8. (LO 1) Phép kết nối nào trả về tất cả các hàng từ cả hai bảng có giá trị khớp nhau?
a. Inner
b. Left
c. Right
d. Full

9. (LO 1) Phép kết nối nào trả về tất cả các bản ghi từ bảng bên phải cũng như tất cả các bản ghi khớp từ bảng bên trái?
a. Inner
b. Left
c. Right
d. Full

10. (LO 1) Phép kết nối nào trả về tất cả các bản ghi khi có một sự khớp nhau trong cả bảng bên trái hoặc bên phải?
a. Inner
b. Left
c. Right
d. Full

11. (LO 2) Hàm nào sau đây trong Microsoft Excel trả về trung bình cộng (arithmetic mean) cho một dải hoặc mảng các con số?
a. AVERAGE
b. MEAN
c. AVERAGEIF
d. SUM

12. (LO 2) Hàm nào sau đây trong Microsoft Excel đếm số lượng ô được chỉ định bởi một tập hợp các tiêu chí cho trước?
a. COUNT
b. COUNTIF
c. COUNTIFS
d. COUNTA

13. (LO 2) Hàm này cộng các ô được chỉ định bởi một tập hợp các điều kiện hoặc tiêu chí cho trước.
a. SUM
b. SUMIF
c. SUMIFS
d. SUMPRODUCT

14. (LO 3) Hàm này cộng các ô được chỉ định bởi một điều kiện hoặc tiêu chí.
a. SUM
b. SUMIF
c. SUMIFS
d. SUMPRODUCT

15. (LO 3) Công cụ nào trong Microsoft Excel sẽ tổ chức lại dữ liệu bảng tính thành các bản tóm tắt tùy chỉnh của các thông tin quan trọng?
a. Sort
b. Filter
c. PivotTable
d. Developer

16. (LO 3) Một PivotTable hiển thị doanh số bán hàng theo loại sản phẩm, năm bán, và tổng số tiền bán hàng. Bạn chỉ muốn xem ba trong số 15 loại sản phẩm cụ thể. Cách tốt nhất để chỉ tập trung vào các loại sản phẩm cụ thể mà bạn quan tâm là sử dụng
a. hàm SORT.
b. hàm SUMIG.
c. một bộ lọc (filter).
d. cắt và dán (cut and paste).

17. (LO 3) Chức năng lọc tự động (Auto filter) trong một PivotTable có thể được truy cập bằng cách
a. sử dụng hộp lọc trong các trường PivotTable (PivotTable fields).
b. nhấp vào mũi tên thả xuống trong các nhãn hàng (row labels).
c. nhấp vào mũi tên thả xuống trong hộp bộ lọc (filter box).
d. kéo một trường vào hộp lọc trường.

18. (LO 3) Cắt lớp dữ liệu (Slicing) đề cập đến
a. loại bỏ các chữ số thập phân.
b. loại bỏ dữ liệu.
c. sắp xếp dữ liệu.
d. chia nhỏ dữ liệu thành các phần nhỏ hơn.

19. (LO 4) Tổng của tất cả các quan sát trong một tập dữ liệu chia cho tổng số các quan sát được gọi là
a. số trung bình (mean).
b. số trung vị (median).
c. yếu vị (mode).
d. khoảng (range).

20. (LO 4) Giá trị nằm ở giữa khi dữ liệu trong một tập dữ liệu được sắp xếp từ nhỏ nhất đến lớn nhất được gọi là
a. số trung bình (mean).
b. số trung vị (median).
c. yếu vị (mode).
d. khoảng (range).

21. (LO 4) Các thước đo độ phân tán (Measures of dispersion) cho thấy
a. xu hướng tập trung (central tendency).
b. hình dạng (shape).
c. sự biến thiên (variation).
d. vị trí (location).

22. (LO 4) Nếu hệ số bất đối xứng (coefficient of skewness) là -1.5, phân phối dữ liệu sẽ có
a. mức độ lệch cao và đuôi kéo về bên phải.
b. mức độ lệch cao và đuôi kéo về bên trái.
c. mức độ lệch vừa phải và đuôi kéo về bên phải.
d. mức độ lệch vừa phải và đuôi kéo về bên trái.

23. (LO 4) Một sự tương quan âm (negative correlation) có nghĩa là
a. khi một biến giảm, biến kia cũng giảm.
b. khi một biến tăng, biến kia cũng tăng.
c. khi một biến tăng, biến kia giảm.
d. khi một biến giảm, biến kia vẫn không thay đổi.

24. (LO 5) Những điều nào sau đây là lợi ích của trực quan hóa dữ liệu?
a. Trực quan hóa giúp hiểu nhanh các tập dữ liệu lớn.
b. Trực quan hóa dữ liệu có thể được sử dụng để khám phá dữ liệu.
c. Trực quan hóa dữ liệu có thể được sử dụng để giải thích phân tích dữ liệu.
d. Tất cả các điều trên đều là lợi ích của trực quan hóa dữ liệu.

25. (LO 5) Sử dụng trực quan hóa dữ liệu để xác định các mô hình ẩn bên dưới (underlying patterns) được coi là
a. trực quan hóa dữ liệu giải thích (explanatory data visualization).
b. trực quan hóa dữ liệu khám phá (exploratory data visualization).
c. phân tích đồ họa (graphical analysis).
d. phân tích từ trên xuống (top-down analysis).

26. (LO 5) Một trực quan hóa được sử dụng để thể hiện những thay đổi về khối lượng theo thời gian là một
a. biểu đồ vùng (area chart).
b. biểu đồ cột (bar chart).
c. biểu đồ đường (line graph).
d. biểu đồ tròn (pie chart).

27. (LO 5) Một trực quan hóa được sử dụng để minh họa các mối quan hệ đơn giản giữa các phần so với tổng thể là một
a. biểu đồ vùng (area chart).
b. biểu đồ cột (bar chart).
c. biểu đồ đường (line graph).
d. biểu đồ tròn (pie chart).

28. (LO 5) Một trực quan hóa được sử dụng để chỉ ra các phân phối tần số là một
a. biểu đồ tròn (pie chart).
b. biểu đồ đường (line chart).
c. biểu đồ tần suất (histogram chart).
d. biểu đồ bong bóng (bubble chart).

---

## Câu Hỏi Ôn Tập (Review Questions)

1. (LO 1) Hãy xác định và mô tả bốn loại kết nối (joins) có thể truy vấn một tập dữ liệu.

2. (LO 2) Đối với mỗi kịch bản, hãy nối ghép hàm Excel cơ bản tốt nhất có thể được sử dụng để giải quyết nó. Mỗi hàm có thể được sử dụng một lần, nhiều lần, hoặc không được sử dụng.
a. AVERAGE
b. AVERAGEIF
c. COUNT
d. COUNTIF
e. COUNTA
f. COUNTBLANK
g. SUM
h. SUMIF

**Kịch bản (Scenario)** | **Hàm (Function)**
--- | ---
1. Đếm số ô trong một tệp Excel có chứa số lượng hàng tồn kho. | 
2. Đếm số ô trong một tệp Excel có số lượng hàng tồn kho là 1.150 mặt hàng. | 
3. Tính trung bình cộng của số tiền hoa hồng trả cho nhân viên bán hàng trong quý 4. | 
4. Tính tổng doanh số bán hàng cho kỳ kế toán, được liệt kê ở cột K trong bảng tính Excel của bạn. | 
5. Tính tổng doanh số bán hàng cho kỳ kế toán chỉ dành riêng cho khách hàng số #4920. Số tiền doanh thu được liệt kê ở cột K trong bảng tính Excel của bạn và mã số khách hàng được liệt kê ở cột A trong bảng tính. | 
6. Đếm số lượng các mặt hàng tồn kho được liệt kê trên bảng tính nhưng không có số lượng hàng tồn kho. | 

3. (LO 2) Cung cấp một ví dụ về thời điểm bạn nên sử dụng hàm COUNTIFS.
4. (LO 2) Cung cấp một ví dụ về thời điểm bạn có thể sử dụng hàm COUNTBLANK.
5. (LO 3) Mô tả năm thành phần của một Excel PivotTable.
6. (LO 3) Mô tả cách một Excel PivotTable có thể được lọc (filtered).
7. (LO 4) Cung cấp một ví dụ về thời điểm mà số trung vị (median) của một phân phối có thể có ý nghĩa để diễn giải hơn là số trung bình (mean).
8. (LO 4) Định nghĩa độ lệch chuẩn (standard deviation) và cung cấp một ví dụ về cách diễn giải nó.
9. (LO 4) Định nghĩa tương quan âm (negative correlation) và tương quan dương (positive correlation). Cung cấp một ví dụ cho mỗi loại.
10. (LO 5) Mô tả trực quan hóa dữ liệu khám phá và trực quan hóa dữ liệu giải thích. Chúng giống nhau như thế nào? Chúng khác nhau ra sao?
11. (LO 5) Đối với mỗi kịch bản, hãy xác định xem bạn sẽ thực hiện trực quan hóa dữ liệu khám phá hay trực quan hóa dữ liệu giải thích.

**Kịch bản (Scenario)** | **Loại Trực quan hóa (Visualization Type)**
--- | ---
1. Người quản lý cung cấp cho bạn tất cả dữ liệu bán hàng theo dòng sản phẩm trong hai năm qua và yêu cầu bạn xác định các xu hướng bán hàng giữa các năm. | 
2. Bạn đã phân tích dữ liệu liên quan đến xu hướng bán hàng theo quốc gia trong ba năm qua và sẽ trình bày dữ liệu đó bằng cách sử dụng một tree map. | 
3. Quản lý cung cấp cho bạn tất cả các khoản thanh toán được trả cho các nhà cung cấp được chấp thuận trong sáu tháng qua và yêu cầu bạn xác định xem có bất kỳ khoản thanh toán nào nằm ngoài các số tiền thanh toán dự kiến hay không. | 
4. Quản lý cung cấp cho bạn một bản phân tích chi phí bảo trì trong năm và yêu cầu bạn chuẩn bị một biểu đồ tròn để minh họa các hạng mục chi phí. | 

12. (LO 5) Là một chuyên gia thuế cho một nhà bán lẻ trực tuyến, bạn được yêu cầu tạo một trực quan hóa biểu đồ đường mô tả sự gia tăng về số thuế bán hàng thu được và nộp đi trong mỗi tháng của năm nay so với năm ngoái. Bằng cách sử dụng các phương pháp hay nhất (best practices) của biểu đồ đường được trình bày trong chương, hãy mô tả cách bạn sẽ thiết lập trực quan hóa này. Xác định các điểm dữ liệu trên trục x, trục y, và các chuỗi dữ liệu.
13. (LO 5) Mô tả các phương pháp hay nhất đối với biểu đồ cột (bar charts) và biểu đồ vùng (area charts).
14. (LO 5) Bạn là một chuyên viên phân tích tài chính trong bộ phận hoạt động của một công ty sản xuất. Là một phần của các số liệu kiểm soát chất lượng, công ty của bạn theo dõi các chi phí làm lại (rework expenses) cho các hàng hóa không được sản xuất đạt tiêu chuẩn chất lượng. Quản lý của bạn đã yêu cầu bạn chuẩn bị một biểu đồ đường để minh họa xu hướng của chi phí làm lại theo danh mục mã lý do. Bạn lưu ý rằng có năm mã lý do khác nhau giải thích tại sao việc làm lại có thể được yêu cầu. Bằng cách sử dụng các phương pháp hay nhất được phác thảo trong chương này, hãy mô tả cách bạn sẽ thiết lập biểu đồ đường để phác họa các xu hướng chi phí làm lại theo danh mục.

## Bài Tập Ngắn (Brief Exercises)

**BE 2.1 (LO 1) Kế toán Quản trị (Managerial Accounting)**
Bạn là một chuyên viên phân tích tài chính cho PizzaNow! Kiểm soát viên nội bộ của công ty muốn bạn thực hiện một phân tích sử dụng ba bảng trong cơ sở dữ liệu quan hệ (Employees, Customers, TakeOrder).
Đối với mỗi khoản mục sau, hãy xác định xem nó là một khóa chính (primary key), khóa ngoại (foreign key), hay không phải cả hai.
1. OrderNumber trong bảng TakeOrder
2. EmployeeID trong bảng TakeOrder
3. CustomerID trong bảng Customers
4. EmployeeID trong bảng Employees
5. Date trong bảng TakeOrder
6. ZipCode trong bảng Employees

![BE 2.1](../TaiLieu/textbookForPractice/Figures/Ch_02/BE%202.1.png)
![BE 2.1_1](../TaiLieu/textbookForPractice/Figures/Ch_02/BE%202.1_1.png)

**BE 2.2 (LO 1) Hệ thống Thông tin Kế toán (Accounting Information Systems)**
Dine At Home cung cấp dịch vụ giao đồ ăn tận nhà được đặt từ nhiều nhà hàng địa phương khác nhau. Bạn là người kết nối giữa bộ phận công nghệ thông tin và bộ phận kế toán của công ty. Bạn được yêu cầu giải thích mối quan hệ giữa ba bảng này cho nhóm kế toán. Các bảng (Customer1, Restaurant, Order) được lấy từ cơ sở dữ liệu của Dine At Home.
Đối với mỗi kịch bản, hãy xác định kết nối (join) mà bạn có khả năng sử dụng nhiều nhất để truy vấn dữ liệu. Mỗi loại kết nối có thể được sử dụng một lần, nhiều lần, hoặc không được sử dụng.
a. Left join
b. Right join
c. Inner join
d. Full join
1. Thực hiện một truy vấn để kết nối bảng Restaurant (bảng bên trái) và bảng Order (bảng bên phải), nhưng chỉ trả về các hàng từ cả hai bảng có giá trị khớp nhau.
2. Thực hiện một truy vấn để kết nối bảng Restaurant (bảng bên trái) và bảng Customer1 (bảng bên phải), và trả về tất cả các bản ghi từ bảng Restaurant, nhưng chỉ trả về các bản ghi khớp từ bảng Customer1.
3. Thực hiện một truy vấn để kết nối bảng Order (bảng bên trái) và bảng Customer1 (bảng bên phải), và trả về tất cả các bản ghi từ cả hai bảng. Khớp các bản ghi có thể khớp ở cả hai bảng.
4. Thực hiện một truy vấn để kết nối bảng Order (bảng bên trái) và bảng Customer1 (bảng bên phải), và chỉ trả về tất cả các bản ghi từ bảng Order và các bản ghi khớp từ bảng Customer1.
1. Xác định khóa chính (primary keys) và khóa ngoại (foreign keys) cho mỗi bảng.
2. Nếu bạn muốn biết tên của một khách hàng cho một đơn hàng cụ thể, bạn nên truy vấn các bảng nào?

![BE 2.2](../TaiLieu/textbookForPractice/Figures/Ch_02/BE%202.2.png)
![BE 2.2_1](../TaiLieu/textbookForPractice/Figures/Ch_02/BE%202.2_1.png)

**BE 2.3 (LO 1) Kế toán Tài chính (Financial Accounting)**
Giả sử bạn là một chuyên viên phân tích tài chính trong nhóm kiểm soát cho công ty phân phối của bạn. Bạn được yêu cầu xác định tất cả các mặt hàng tồn kho không có doanh số bán hàng trong năm qua:
- Nhóm IT đã cung cấp tệp dữ liệu hàng tồn kho hiện có (inventory on hand data file) và tệp dữ liệu doanh số mười hai tháng (twelve month sales data file).
- Bạn đã xác định bảng hàng tồn kho hiện có là bảng bên trái và bảng doanh số mười hai tháng là bảng bên phải.
Hãy xác định kết nối (join) phù hợp nhất cho hai bảng này để thực hiện phân tích của bạn. Tại sao kết nối này lại phù hợp nhất?

**BE 2.4 (LO 1) Kế toán Tài chính (Financial Accounting)**
Bạn là một chuyên viên phân tích tài chính cho Dine At Home và được yêu cầu phân tích dữ liệu trong ba bảng trên (Customer1, Restaurant, Order). 

![BE 2.4](../TaiLieu/textbookForPractice/Figures/Ch_02/BE%202.4.png)
![BE 2.4_1](../TaiLieu/textbookForPractice/Figures/Ch_02/BE%202.4_1.png)

**BE 2.5 (LO 2) > **Data** Kế toán Quản trị (Managerial Accounting)**
Kiểm soát viên tại ThisBigCity đã yêu cầu bạn thực hiện một bản phân tích về chi phí hoàn trả cho nhân viên (employee reimbursement expenses) của thành phố trong mười lăm năm qua. Nhóm IT đã cung cấp một bản tải xuống tất cả dữ liệu hoàn trả cho nhân viên kể từ năm 2005.
1. Sử dụng hàm AVERAGE. Số tiền hoàn trả trung bình được trả từ tháng 7 năm 2005 đến tháng 11 năm 2020 là bao nhiêu?
2. Sử dụng hàm AVERAGEIF. Số tiền hoàn trả trung bình được trả trong năm 2019 là bao nhiêu?
3. Sử dụng hàm AVERAGEIFS. Số tiền hoàn trả trung bình được trả trong sở cứu hỏa (fire department) trong năm 2019 là bao nhiêu?

**BE 2.6 (LO 2) > **Data** Hệ thống Thông tin Kế toán (Accounting Information Systems)**
Là một kiểm toán viên nội bộ tại ThisBigCity, bạn đang kiểm tra các kiểm soát nội bộ (internal controls) đối với quy trình hoàn trả cho nhân viên của thành phố. Nhóm IT đã cung cấp bản tải xuống tất cả dữ liệu hoàn trả cho nhân viên kể từ năm 2005. Quản lý của bạn đề xuất thực hiện thống kê mô tả (descriptive statistics) trên tệp này để xác định xem bạn có dữ liệu tổng thể (population of data) đầy đủ hay không, và để bắt đầu quá trình xác định kích thước mẫu (sample size) cho việc kiểm tra kiểm soát nội bộ.
1. Sử dụng hàm COUNT. Có bao nhiêu khoản hoàn trả được thanh toán từ tháng 7 năm 2005 đến tháng 11 năm 2020?
2. Sử dụng hàm COUNTIF. Có bao nhiêu khoản hoàn trả được thanh toán trong năm 2019?
3. Sử dụng hàm COUNTIFS. Có bao nhiêu khoản hoàn trả được thanh toán trong năm 2019 cho lực lượng cứu hỏa (firefighters)?

**BE 2.7 (LO 3) > **Data** Kiểm toán (Auditing)**
Sử dụng PivotTables và dữ liệu có sẵn để trả lời các câu hỏi sau:
1. Khách hàng nào có số dư khoản phải thu (accounts receivable balance) cao nhất?
2. Khách hàng nào có số dư khoản phải thu cao nhất mà đã quá hạn (past due) trên 150 ngày?

**BE 2.8 (LO 3) > **Data** Kế toán Tài chính (Financial Accounting)**
Sử dụng PivotTables và dữ liệu có sẵn để trả lời các câu hỏi sau:
1. Tổng các khoản phải thu (accounts receivable) là bao nhiêu?
2. Tổng số theo từng khu vực (region) là bao nhiêu?

**BE 2.9 (LO 3) > **Data** Kế toán Tài chính (Financial Accounting), Kế toán Quản trị (Managerial Accounting)**
Sử dụng PivotTables và dữ liệu Super Scooters để trả lời các câu hỏi sau:
1. Tổng doanh thu gộp (gross sales) cho mỗi mẫu xe (model) theo từng năm là bao nhiêu?
2. Xe màu nào có khối lượng bán (sales volume) cao nhất trong năm 2023?
3. Tổng chi phí tiếp thị biến đổi (variable marketing expense) cho năm 2023 tính theo mẫu xe là bao nhiêu?

**BE 2.10 (LO 4) > **Data** Kế toán Quản trị (Managerial Accounting)**
Là một chuyên viên phân tích tài chính làm việc cho Animal Control Centers, bạn muốn hiểu về khoản tiền làm thêm giờ (overtime pay) trong năm 2025. Hãy tìm các thống kê sau đây cho tiền lương làm thêm giờ:
1. Số trung bình (Mean)
2. Số trung vị (Median)
3. Yếu vị (Mode)

**BE 2.11 (LO 4) > **Data** Kế toán Tài chính (Financial Accounting)**
Bạn đang chuẩn bị cuộc thảo luận và phân tích của ban giám đốc (MD&A) liên quan đến sở cứu hỏa của thành phố Chicago. Một trong những khoản chi phí quan trọng nhất của sở cứu hỏa là tiền làm thêm giờ. Do đó, bạn muốn hiểu dữ liệu làm thêm giờ trước khi viết bài MD&A.
1. Tính hệ số bất đối xứng (coefficient of skewness) cho tiền lương làm thêm giờ.
2. Tính hệ số độ nhọn (coefficient of kurtosis) cho tiền lương làm thêm giờ.
3. Chuẩn bị một biểu đồ tần suất (histogram) với các nhóm (groupings) sau: $500, $1,000, $2,000, $3,000, $4,000, $5,000, $6,000.

**BE 2.12 (LO 5) > **Data** Kế toán Tài chính (Financial Accounting)**
Công ty của bạn, Loans Are US, cung cấp các khoản vay cho các doanh nghiệp quy mô nhỏ đến vừa. Công ty có các văn phòng cho vay tại bốn khu vực. Bạn được yêu cầu chuẩn bị một trực quan hóa minh họa tổng số tiền cho vay theo khu vực và theo tuổi nợ (age of receivables). Hãy chuẩn bị một biểu đồ cột xếp chồng (stacked column chart) để làm điều này.

**BE 2.13 (LO 5) > **Data** Kế toán Tài chính (Financial Accounting)**
Loans Are US theo dõi xếp hạng tín dụng cho tất cả tài khoản của khách hàng. Bạn phải chuẩn bị một trực quan hóa minh họa tổng số các khoản vay dựa trên xếp hạng tín dụng. Hãy chuẩn bị một biểu đồ cột (bar chart) trực quan hóa số lượng tài khoản trong mỗi mức thuộc ba xếp hạng tín dụng: AAA, BBB, và CCC.

**BE 2.14 (LO 5) > **Data** Kế toán Tài chính (Financial Accounting)**
Cấp trên của bạn tại Loans Are US đã yêu cầu bạn chuẩn bị một trực quan hóa minh họa tổng số tiền tính bằng đô la của các khoản vay đã quá hạn thanh toán trên 150 ngày dựa theo xếp hạng tín dụng. Hãy chuẩn bị một biểu đồ cột trực quan hóa số lượng tài khoản trong mỗi mức thuộc ba xếp hạng tín dụng: AAA, BBB, và CCC.

## Bài Tập (Exercises)

**EX 2.1 (LO 1) Kiểm toán (Auditing)**
**Xác định Dữ liệu và Kết nối Cần thiết để Xác minh Dữ liệu (Identify Data and Joins Needed to Verify Data)**
Bạn là một kiểm toán viên nội bộ cho Way Cool Stuff. Bạn phải xác minh rằng không có nhân viên nào đồng thời là khách hàng. Các bảng dữ liệu của Way Cool Stuff (Locations, SalesOrders, Employee, Customer, Regions, Inventory, SalesOrderExpenses) được cung cấp trong cơ sở dữ liệu.
1. Bạn sẽ cần (các) bảng nào để có thể hoàn thành bài kiểm tra này?
2. Bạn sẽ sử dụng các trường nào để kết nối các bảng, nếu cần?
3. Bạn cần các trường nào từ (các) bảng để hoàn thành bài kiểm tra này?

![EX 2.1](../TaiLieu/textbookForPractice/Figures/Ch_02/EX%202.1.png)
![EX 2.1_1](../TaiLieu/textbookForPractice/Figures/Ch_02/EX%202.1_1.png)

**EX 2.2 (LO 1) Kế toán Tài chính (Financial Accounting)**
**Xác định Dữ liệu và Kết nối Cần thiết để Tóm tắt Dữ liệu (Identify Data and Joins Needed to Summarize Data)**
Bạn là một kế toán viên tài chính tại Way Cool Stuff đang tính toán thu nhập ròng (net income). Sử dụng các bảng cơ sở dữ liệu có sẵn của Way Cool Stuff được cung cấp.
1. Bạn cần (các) bảng nào để có thể thu thập dữ liệu cần thiết cho việc tính toán thu nhập ròng?
2. Bạn sẽ sử dụng các trường nào để kết nối các bảng?
3. Bạn sẽ cần các trường nào để tính thu nhập ròng?

![EX 2.2](../TaiLieu/textbookForPractice/Figures/Ch_02/EX%202.2.png)
![EX 2.2_1](../TaiLieu/textbookForPractice/Figures/Ch_02/EX%202.2_1.png)

**EX 2.3 (LO 1) Kế toán Quản trị (Managerial Accounting)**
**Áp dụng Kết nối để Trả lời Câu hỏi (Apply Joins to Answer Questions)**
Bạn đang phân tích doanh số bán hàng tại Way Cool Stuff theo khu vực cho các năm 2024 và 2025. Sử dụng các bảng cơ sở dữ liệu có sẵn.
1. Bạn cần (các) bảng nào để thu thập dữ liệu cần thiết nhằm phân tích doanh thu gộp (gross sales) theo khu vực cho năm 2024 và 2025?
2. Bạn sẽ sử dụng các trường nào để kết nối các bảng?
3. Bạn sẽ cần các trường nào để thực hiện phân tích của mình?

![EX 2.3](../TaiLieu/textbookForPractice/Figures/Ch_02/EX%202.3.png)
![EX 2.3_1](../TaiLieu/textbookForPractice/Figures/Ch_02/EX%202.3_1.png)

**EX 2.4 (LO 1) Kế toán Thuế (Tax Accounting)**
**Xác định Dữ liệu và Kết nối Cần thiết cho Việc Tuân thủ Thuế (Identify Data and Joins Needed for Tax Compliance)**
Bạn đang nộp tờ khai thuế bán hàng cấp bang của Way Cool Stuff cho tháng kết thúc vào ngày 31 tháng 12 năm 2025 đối với tất cả các địa điểm có thu thuế bán hàng. Sử dụng các bảng cơ sở dữ liệu có sẵn để trả lời các câu hỏi.
1. Bạn cần (các) bảng nào để có thể thu thập dữ liệu cần thiết cho việc tính toán khoản thuế bán hàng phải nộp cho tháng 12 năm 2025?
2. Bạn sẽ sử dụng các trường nào để kết nối các bảng?
3. Bạn sẽ cần các trường nào để thu thập thông tin cần thiết nhằm nộp thuế bán hàng năm 2025?

![EX 2.4](../TaiLieu/textbookForPractice/Figures/Ch_02/EX%202.4.png)
![EX 2.4_1](../TaiLieu/textbookForPractice/Figures/Ch_02/EX%202.4_1.png)

**EX 2.5 (LO 3) > **Data** Kế toán Quản trị (Managerial Accounting)**
**Áp dụng Bộ cắt lọc PivotTable của Excel (Apply Excel PivotTable Slicers)**
Cấp trên của bạn tại Best Bakes Bakery muốn bạn thực hiện một phân tích chi phí theo sản phẩm. Hãy tạo một Excel PivotTable hiển thị tất cả các sản phẩm, và tạo các bộ cắt lọc dữ liệu (slicers) để cung cấp các thông tin sau:
1. Tổng chi phí hàng tồn kho cho năm 2023.
2. Tổng chi phí hàng tồn kho cho bánh quế quế (cinnamon buns) từ năm 2022 đến 2025.
3. Tổng chi phí hàng tồn kho cho bánh quế quế trong năm 2023.
4. Tổng chi phí hàng tồn kho cho thành phố Thornton từ năm 2022 đến 2025.
5. Tổng chi phí hàng tồn kho cho bánh quy bơ (snickerdoodles) năm 2024 tại thành phố Brookfield.

**EX 2.6 (LO 4) > **Data** Kế toán Quản trị (Managerial Accounting)**
**Thống kê Mô tả (Descriptive Statistics)**
Bạn là một chuyên viên phân tích tài chính tại Animal Control Centers of America được giao nhiệm vụ tìm hiểu khoản tiền làm thêm giờ (overtime pay) trong năm. Nhóm IT của bạn đã cung cấp một tệp bao gồm số tiền làm thêm giờ của mỗi nhân viên mỗi tháng. Bảng tính này cũng bao gồm nhiệt độ trung bình hàng tháng. Hãy thực hiện một phân tích tương quan giữa số tiền làm thêm giờ phát sinh và nhiệt độ của mỗi tháng.
1. Hệ số tương quan giữa các biến số tiền (amount) và nhiệt độ (temperature) là bao nhiêu?
2. Mối tương quan giữa số tiền và nhiệt độ là mạnh, vừa phải, hay yếu? Giải thích câu trả lời của bạn.

**EX 2.7 (LO 4) > **Data** Kế toán Quản trị (Managerial Accounting)**
**Thống kê Mô tả (Descriptive Statistics)**
Giám đốc phát triển nhân sự tại Animal Control Centers đã yêu cầu bạn cung cấp một báo cáo tóm tắt về khoản tiền làm thêm giờ trong năm. Nhóm IT đã trích xuất dữ liệu từ cơ sở dữ liệu của công ty và cung cấp một tệp Excel. Cung cấp một báo cáo tóm tắt bằng cách thực hiện những điều sau:
1. Tạo các thống kê mô tả cho trường dữ liệu số tiền (Amount). Báo cáo kết quả thống kê mô tả:
- Số trung bình (Mean)
- Sai số chuẩn (Standard Error)
- Số trung vị (Median)
- Yếu vị (Mode)
- Độ lệch chuẩn (Standard Deviation)
- Phương sai mẫu (Sample Variance)
- Độ nhọn (Kurtosis)
- Độ lệch/Bất đối xứng (Skewness)
- Khoảng (Range)
- Giá trị nhỏ nhất (Minimum)
- Giá trị lớn nhất (Maximum)
- Tổng (Sum)
- Số lượng (Count)
2. Tạo một biểu đồ phân tán (scatterplot) của tiền lương làm thêm giờ. Trục x phải là tháng trong năm, và trục y là số tiền đô la của tiền làm thêm giờ đã trả.
3. Có bất kỳ điểm bất thường nào trên biểu đồ phân tán cần điều tra thêm không? Tại sao có hoặc tại sao không?

**EX 2.8 (LO 2, 5) > **Data** Kế toán Thuế (Tax Accounting)**
**Các Hàm Excel Cơ Bản và Trực quan hóa Biểu đồ Cột (Basic Excel Functions and Bar Chart Visualization)**
Bạn là một chuyên gia thuế được tổng kiểm toán của bang Wyoming yêu cầu cung cấp một báo cáo tóm tắt các tờ khai thuế đã nộp trong bang. Nhóm công nghệ thông tin đã cung cấp một tệp Excel có chứa dữ liệu về mã bưu chính của người nộp thuế, số lượng tờ khai, và các dữ liệu tờ khai thuế quan trọng khác.
1. Tình trạng nộp hồ sơ nào (filing status) có số tờ khai được nộp nhiều nhất? (Độc thân - Single, Chủ hộ - Head of Household, hoặc Kết hôn nộp chung - Married Filing Jointly)? Sử dụng một hàm Excel (không sử dụng PivotTable).
2. Tạo một trực quan hóa biểu đồ cột (column chart) thể hiện số lượng tờ khai thuế theo tình trạng nộp hồ sơ. Trục x nên bao gồm tình trạng nộp hồ sơ (single, MFJ, Head of Household), và trục y nên là số lượng tờ khai.

**EX 2.9 (LO 2, 4, 5) > **Data** Kế toán Quản trị (Managerial Accounting)**
**PivotTables, Thống kê Mô tả, và Trực quan hóa (PivotTables, Descriptive Statistics, and Visualizations)**
Bạn là một kế toán viên quản trị đang chuẩn bị phân tích doanh số bán hàng theo phân khúc. U.S. Outdoor Adventures có ba phân khúc: tiêu dùng (consumer), bán lẻ (retail), và công ty du lịch (travel company). Phân khúc tiêu dùng bao gồm doanh số bán hàng được thực hiện cho các khách hàng cá nhân thông qua trang web của U.S. Outdoor Adventures. Phân khúc bán lẻ là các đợt bán hàng cho các cửa hàng bán lẻ. Phân khúc công ty du lịch là các đợt bán hàng cho các công ty du lịch tổ chức và điều hành các chuyến đi cắm trại.
1. Tạo một Excel PivotTable tóm tắt doanh số bán hàng theo phân khúc từ 2022 đến 2025. Hiển thị từng phân khúc và tổng doanh số theo năm.
2. Tạo một biểu đồ cột (bar chart) cho doanh số bán hàng theo phân khúc từ 2022 đến 2025. Những phân khúc nào đang tăng lên, và những phân khúc nào đang giảm đi?
3. Tạo một PivotTable để phân tích doanh số bán hàng trung bình theo phân khúc từ 2022 đến 2025. Hiển thị từng phân khúc và doanh số trung bình theo năm.
4. Tạo một biểu đồ đường (line chart) cho doanh số bán hàng trung bình theo phân khúc từ 2022 đến 2025. Doanh số trung bình đang tăng hay giảm từ năm 2024 sang năm 2025?
5. Đi Sâu Hơn (Dig Deeper): Xem xét sự biến động trong doanh số bán hàng theo phân khúc bằng cách sử dụng một PivotTable và biểu đồ đường có hiển thị độ lệch chuẩn (standard deviation). Phân khúc nào có sự biến động nhiều nhất trong doanh số? Làm thế nào bạn xác định được câu trả lời của mình?

**EX 2.10 (LO 2, 5) > **Data** Kiểm toán (Auditing)**
**Pivot Tables và Biểu Đồ Đường (Pivot Tables and Line Graphs)**
Bạn đang tham gia vào cuộc kiểm toán báo cáo tài chính của Công ty U.S. Outdoor Adventure cho năm kết thúc vào ngày 31 tháng 12 năm 2023. Trưởng nhóm của bạn đã yêu cầu bạn tìm hiểu dữ liệu bán hàng và xác định các khách hàng trọng yếu để thực hiện kiểm tra chi tiết. Khách hàng đã cung cấp dữ liệu bán hàng. Theo sổ cái chung (general ledger), tổng doanh số cho các năm kết thúc 2025 và 2024 lần lượt là $273,323 và $269,196.
1. Tạo một Excel PivotTable thể hiện tổng doanh số bán hàng theo năm bằng cách sử dụng biến `ShipDate`. Xác minh xem tổng doanh số được báo cáo cho năm có khớp với số dư sổ cái của khách hàng như đã được trình bày hay không.
2. Tạo một PivotTable trình bày doanh số bán hàng cho năm 2024 và 2025 theo danh mục sản phẩm.
3. Sử dụng các phương pháp hay nhất được phác thảo trong Hình minh họa 2.57, tạo một biểu đồ đường chỉ ra doanh số cho năm 2024 và 2025 theo danh mục. Trục x phải bao gồm các năm 2024 và 2025, và trục y phải có số tiền đô la doanh thu. Nên có ba đường, mỗi đường cho một danh mục bán hàng: đồ cắm trại (camping gear), mái chèo (paddles), và lều (tents).
4. Đi Sâu Hơn (Dig Deeper): Sửa đổi biểu đồ đường để trục x có thông tin doanh thu hàng quý cho năm 2024 so với 2025 đối với từng danh mục bán hàng.

## Bài Toán (Problems)

**PR 2.1 (LO 3) > **Data** Kiểm toán (Auditing)**
**Áp dụng Lọc trong PivotTables (Applying Filtering in PivotTables)**
Công ty của bạn đã được thuê để thực hiện một cuộc kiểm toán cho Best Bakes Bakery. Bạn phải thực hiện một phân tích lợi nhuận theo khách hàng để xác định xem có bất kỳ thay đổi bất thường nào không.
1. Tạo một Excel PivotTable hiển thị tất cả các khách hàng và lợi nhuận cho năm 2024 ở một cột và năm 2025 ở một cột khác.
2. Sử dụng Value Field Settings để hiển thị phần trăm chênh lệch so với năm 2024.
3. Có bao nhiêu khách hàng có tỷ lệ phần trăm thay đổi lợi nhuận lớn hơn +/− 30% so với năm trước?

**PR 2.2 (LO 2, 4) > **Data** Kiểm toán (Auditing)**
**Các Hàm Excel và Thống kê Mô tả (Excel Functions and Descriptive Statistics)**
Bạn là một kiểm toán viên đang thực hiện cuộc kiểm toán báo cáo tài chính của ThisBigCity được yêu cầu thực hiện các thủ tục phân tích để hiểu các chi phí hoàn trả của thành phố cho năm kết thúc vào ngày 31 tháng 12 năm 2025. Khách hàng đã cung cấp một bản tải xuống tất cả dữ liệu hoàn trả cho nhân viên kể từ năm 2010. Để trả lời các câu hỏi sau, hãy sử dụng các hàm Excel, không sử dụng PivotTables.
1. Tổng số tiền đô la hoàn trả được thanh toán trong năm 2025 là bao nhiêu?
2. Tính tổng số tiền đô la hoàn trả được thanh toán trong năm 2025 cho các phòng ban sau đây.
- Department of Buildings
- Department of Health
- Department of Water Management
3. Số trung bình (mean), số trung vị (median), và yếu vị (mode) của số tiền hoàn trả trong năm 2025 là bao nhiêu?
4. Độ lệch chuẩn (standard deviation) của số tiền hoàn trả trong năm 2025 là bao nhiêu?
5. Tạo một biểu đồ phân tán (scatterplot) mô tả số tiền hoàn trả trong năm 2025. Trên trục x, hiển thị ngày tháng, và trên trục y, hiển thị số tiền. Phạm vi trục y nên từ $−500 đến $3,500.
6. Sử dụng các số liệu thống kê mô tả sau và biểu đồ phân tán để xác định bất kỳ điểm bất thường nào trong các khoản hoàn trả của thành phố trong năm 2025: Mean, Median, Mode, Standard deviation.
7. Đi Sâu Hơn (Dig Deeper): Mở rộng các phân tích này để bao gồm một cuộc thảo luận về số tiền hoàn trả theo phòng ban (department) hoặc theo chức danh công việc (job title).

![PR 2.2](../TaiLieu/textbookForPractice/Figures/Ch_02/PR%202.2.png)

**PR 2.3 (LO 2, 5) > **Data** Kiểm toán (Auditing)**
**Các Hàm Excel Cơ Bản và Biểu Đồ Tròn (Basic Excel Functions and Pie Chart)**
Bạn là một kiểm toán viên được phân công kiểm toán báo cáo tài chính của Outdoor Adventure Company cho năm kết thúc vào ngày 31 tháng 12 năm 2025. Trưởng nhóm của bạn muốn hiểu dữ liệu bán hàng và xác định các khách hàng trọng yếu để thực hiện kiểm tra chi tiết. Tổng doanh số bán hàng cho năm kết thúc ngày 31 tháng 12 năm 2025, theo sổ cái của công ty là $273,323. (Lưu ý: doanh thu được ghi nhận khi sản phẩm được vận chuyển cho khách hàng.) Sử dụng tệp Excel do khách hàng cung cấp, hãy thực hiện những việc sau:
1. Xác minh rằng tập dữ liệu đã đầy đủ bằng cách tính tổng cột doanh số và đối chiếu với số liệu doanh số được ghi lại trong sổ cái chung (general ledger) của khách hàng. Viết một câu chỉ ra rằng bạn đã đối chiếu số tiền bán hàng khớp với số tiền trong sổ cái chung của khách hàng.
2. Bằng cách sử dụng các phương pháp hay nhất (best practices) được nêu trong Hình minh họa 2.57, hãy tạo một biểu đồ tròn mô tả doanh số bán hàng theo khu vực cho năm 2025 và xác định khu vực có doanh số cao nhất. Biểu đồ tròn có phải là hình ảnh tốt nhất cho câu hỏi này không? Tại sao có hoặc tại sao không?
3. Đi Sâu Hơn (Dig Deeper): Phân tích tập dữ liệu để hiểu các khách hàng lớn nhất của công ty. Trình bày phân tích của bạn dưới dạng một trực quan hóa.

**PR 2.4 (LO 2, 5) > **Data** Kế toán Tài chính, Kế toán Quản trị**
**PivotTables và Biểu đồ Cột (PivotTables and Bar Charts)**
Bạn là một kế toán viên cho U.S. Outdoor Adventures đang chuẩn bị một bản phân tích doanh số cho báo cáo phân tích doanh số nội bộ hàng tháng.
1. Tạo một Excel PivotTable để xác định xem liệu có mô hình doanh số hàng tháng nào cho tổng doanh số hoặc từ năm 2024 đến năm 2025 hay không. Định dạng PivotTable để các số tiền doanh số ở dạng tiền tệ với không chữ số thập phân (zero decimal places).
2. Tạo một biểu đồ cột (bar chart) doanh thu hàng tháng từ 2024 đến 2025. Biểu đồ này có giúp xác định liệu có mô hình doanh số bán hàng hàng tháng hay không? Tại sao có hoặc tại sao không?
3. Đi Sâu Hơn (Dig Deeper): Tạo một PivotTable và một biểu đồ đường (line chart) để minh họa các mô hình doanh số hàng tháng theo danh mục sản phẩm trong các năm 2024 và 2025. Biểu đồ đường tiết lộ điều gì về các mô hình doanh số danh mục sản phẩm?

---

## Tình Huống Ứng Dụng Chuyên Môn (Professional Application Case): Pizza My Heart Food Truck, Inc.

Năm 2020 Sal Simonelli bắt đầu Pizza My Heart Food Truck, Inc. với một công thức gia truyền cũ và một chiếc xe tải bán thức ăn ở Fort Lauderdale, Florida. Pizza My Heart phục vụ mười một loại bánh pizza, cũng như bánh mì que và cánh gà. Họ hoạt động tại các nhà máy bia địa phương ở khu vực Fort Lauderdale và Orlando. Năm 2021 Sal mua một chiếc xe bán thức ăn thứ hai do con trai ông là Franco, điều hành ở Orlando, FL.

Sal và Franco tin rằng công việc kinh doanh của họ đang hoạt động tốt và đang xem xét việc mở rộng sang các thành phố khác của Florida. Dưới đây là báo cáo kết quả hoạt động kinh doanh của hai năm qua.

- Doanh nghiệp đang hoạt động thua lỗ vào năm 2024. Điều này phần lớn là do chi phí khởi nghiệp của chiếc xe tải thứ hai và bởi vì Sal và Franco vẫn đang tìm kiếm các địa điểm tốt nhất ở Fort Lauderdale và Orlando cho các xe tải của họ.
- Công ty bắt đầu có lãi vào năm 2025. Doanh thu gần như tăng gấp đôi đối với xe tải ở Fort Lauderdale và tăng hơn gấp đôi đối với xe tải ở Orlando.
- Cùng với sự gia tăng nhanh chóng về doanh số bán hàng, Sal và Franco cần một cách tốt hơn để ghi nhận dữ liệu tài chính và phi tài chính của họ.

Họ đã thuê công ty kế toán DGJ, LLC để tạo ra một cơ sở dữ liệu cho họ. Các trường trong mỗi bảng được hiển thị trong sơ đồ. Khóa chính (primary keys) được nhận diện bằng biểu tượng một chiếc chìa khóa đứng trước tên trường.

**PAC 2.1 Hệ thống Thông tin Kế toán (Accounting Information Systems): Hiểu Cấu trúc Cơ sở dữ liệu Quan hệ**
Bạn là một kế toán viên tại công ty kế toán DGJ, công ty đang giúp Pizza My Heart tạo ra một cơ sở dữ liệu quan hệ cho doanh nghiệp của họ. Bạn đã tạo ra các bảng như trên. Bây giờ, bạn phải tạo các kết nối (joins) giữa các bảng. Xác định các trường sẽ tạo ra một kết nối giữa các bảng (Sales và Customer, Sales và Employee, v.v.). Xem xét mỗi câu hỏi (Ví dụ: Có nhà cung cấp nào chưa thực hiện mua hàng không?), và liệt kê các bảng và các trường cần thiết để trả lời chúng. Chỉ ra xem liệu kết nối đó nên là một left, right, hay inner join.

**PAC 2.2 Kiểm toán (Auditing): Tạo Các Phân tích cho Tính trọn vẹn của Tiền (Completeness of Cash)**
> **Data** Bạn là một kiểm toán viên trong đợt kiểm toán Pizza My Heart, được phân công kiểm toán tiền mặt (cash). Sử dụng các tệp dữ liệu phiếu thu tiền mặt (cash receipts) và tiền gửi ngân hàng (bank deposit) để hoàn thành các phân tích như là một phần trong việc kiểm toán tiền mặt cho quý đầu tiên. Sử dụng các pivot tables khi có thể áp dụng.
1. Tóm tắt doanh thu hàng ngày, doanh thu tiền mặt hàng ngày, và doanh thu thẻ tín dụng hàng ngày cho Xe tải 1 (Truck 1).
2. Tóm tắt các khoản tiền gửi hàng ngày của Xe tải 1.
3. Chuẩn bị một bản đối chiếu giữa các khoản thu hàng ngày và các khoản tiền gửi hàng ngày. Sau đó, xác định xem liệu có bất kỳ đợt bán hàng hàng ngày nào không khớp với khoản tiền gửi hàng ngày hay không.

**PAC 2.3 Kế toán Tài chính (Financial Accounting): Tạo Các Phân tích Doanh thu (Analyses of Sales)**
> **Data** Bạn đang chuẩn bị kết quả bán hàng quý đầu tiên cho Pizza My Heart.
1. Tạo một PivotTable tóm tắt doanh thu theo Xe tải 1 (Truck 1) và hiển thị tổng doanh thu cho mỗi tháng trong quý đầu tiên (Tháng Giêng, Tháng Hai, Tháng Ba).
2. Tạo một PivotTable tóm tắt doanh số bán hàng theo sản phẩm cho quý đầu tiên của Xe tải 1. Sắp xếp dữ liệu từ doanh số bán hàng cao nhất đến doanh số thấp nhất.

**PAC 2.4 Kế toán Quản trị (Managerial Accounting): Tạo Các Phân tích để Hiểu Chi phí trên mỗi Sản phẩm**
> **Data** Bạn là một kế toán viên quản trị được yêu cầu chuẩn bị một bản phân tích chi phí. Sử dụng tệp dữ liệu mua hàng (purchases) để trả lời các câu hỏi bằng PivotTables:
1. Trung bình của tổng chi phí trên mỗi nguyên liệu thô là bao nhiêu?
2. Chi phí trung bình trên mỗi nguyên liệu thô theo nhà cung cấp là bao nhiêu?
3. Có nhà cung cấp nào đang tính phí cao hơn chi phí trung bình cho các nguyên liệu không?

**PAC 2.5 Kế toán Thuế (Tax Accounting): Tạo Các Phân tích Lập kế hoạch Mở rộng (Plan for Expansion)**
> **Data** Pizza My Heart đang cân nhắc việc mua một chiếc xe tải bán thức ăn khác, và bang Florida có thu thuế bán hàng (sales tax) trên doanh thu từ xe bán thức ăn. Sal muốn chọn một địa điểm tốt nhất, không chỉ để bán hàng mà còn xét về thuế bán hàng. Sử dụng các tệp dữ liệu về dân số Florida và thuế bán hàng theo thành phố để tạo ra một trực quan hóa cho thấy những thành phố nào có dân số đông nhất và tỷ suất thuế tương ứng.
1. Top 10 thành phố đông dân nhất ở Florida là gì?
2. Sử dụng PivotTable để xác định 10 thành phố có mức thuế suất thấp nhất.
3. Pizza My Heart đang xem xét Tallahassee như một thành phố tiềm năng cho một chiếc xe tải mới. Sal ước tính rằng doanh số trong năm đầu tiên sẽ là $150,000. Tiền thuế bán hàng sẽ được thu là bao nhiêu?

---

## Tình huống Tiếp tục Le Grind (Le Grind Continuing Case)

**Sử dụng Thống kê Mô tả để Phân tích Hoạt động Bán hàng Qua Ba Năm Đầu Hoạt Động Kinh Doanh**

> **Data** Truy cập nền tảng học tập trực tuyến của Wiley để biết bối cảnh tình huống, các câu hỏi bổ sung, dữ liệu và nhiều thông tin chi tiết hơn về tình huống tiếp tục này.

#### **English**

<object data="../TaiLieu/textbookForPractice/Ch_02_Foundational Data Analysis Skills.pdf" type="application/pdf" width="100%" height="800px"><p>Trình duyệt của bạn không hỗ trợ xem PDF trực tiếp. Vui lòng tải xuống tệp PDF tại <a href="../TaiLieu/textbookForPractice/Ch_02_Foundational Data Analysis Skills.pdf">đây</a>.</p></object>


#### ** 🎬 Video **

<iframe src="videoPractice/Chapter02/index.html?v=1785919941" style="width: 100%; aspect-ratio: 16/9; max-height: 75vh; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>

#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slidePractice/Slide_Practice_Ch02.pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slidePractice/Slide_Practice_Ch02.pdf#view=FitH" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slidePractice/Slide_Practice_Ch02.pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

<!-- tabs:end -->
