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

![LO 2.4](../TaiLieu/textbookForPractice/Figures/Ch_08/LO%202.4.png)

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
