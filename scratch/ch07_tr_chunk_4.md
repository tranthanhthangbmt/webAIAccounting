7.2  Các mối quan hệ dữ liệu được hiển thị như thế nào để khám phá?  7-17
Không giống như biểu đồ cột, biểu đồ cột liên cụm sử dụng nhiều biến để so sánh
tư thế. Mặc dù biểu đồ cột được nhóm có thể so sánh giữa các mô hình nhưng nó cũng cung cấp 
sự so sánh trong một mô hình Ví dụ, sự so sánh trong Hình minh họa 7.20 là giữa 
số lượng đơn vị thực tế đã bán và số lượng đơn vị đã bán theo kế hoạch, đó là hai 
các biến trong vùng Giá trị:
• TotalActualUnits biểu thị tổng của tất cả các giá trị trong trườngActualUnits.
• TotalBudgetedUnits biểu thị tổng của tất cả các giá trị trong trường BudgetedUnits.
Khám phá và hiểu biết sâu sắc
Các biến bổ sung có thể được kéo vào ô Giá trị trong Hình minh họa 7.21. Ví dụ, 
phương sai, một biến được tính bằng chênh lệch giữa thực tế và dự toán 
đơn vị, có thể được thêm vào. Ngoài ra còn có ba biến danh nghĩa trong bộ dữ liệu này để bạn lựa chọn: 
quốc gia, loại hoặc mô hình.
Các loại hiểu biết sâu sắc khác nhau có thể được thu thập từ phân tích sai lệch, bao gồm cả khi 
kết quả cao hơn hoặc thuận lợi hơn dự kiến, thấp hơn hoặc kém thuận lợi hơn dự kiến, và 
nếu mục tiêu không hợp lý. Khi chúng tôi xác định được những hiểu biết này, bước tiếp theo có thể là khám phá
tìm ra những nguyên nhân có thể xảy ra, chẳng hạn như làm thế nào để đảo ngược những sai lệch bất lợi. Điều này đặc biệt hữu ích 
khi sự khác biệt là đáng kể.
Phương sai từ trước đến nay là công cụ có giá trị để kế toán viên chỉ ra các vấn đề 
cần được giải quyết:
• Sự thiếu hiệu quả như thiếu kinh nghiệm trong việc đàm phán giá cả, nhân viên không đủ trình độ, sử dụng lao động-
được giao nhiệm vụ sai, sử dụng nguồn lực chất lượng thấp hoặc đào tạo không đầy đủ.
• Những thay đổi bất ngờ như thay đổi về giá, hoặc nhu cầu giảm.
• Lập ngân sách kém.
Một cái nhìn sâu sắc có thể được thu thập từ Hình minh họa 7.20 là hầu hết các mô hình đều có ưu điểm
có thể có phương sai, nhưng một số (Pilot và Odyssey) có phương sai không thuận lợi. Một điều nữa là, 
ngoại trừ mẫu CR-V, hầu hết các phương sai đều không đáng kể.
Mẫu khám phá dữ liệu 4: Xếp hạng
Mối quan hệ dữ liệu xếp hạng (Minh họa 7.22) sắp xếp các giá trị của một biến một cách tuần tự 
dựa trên giá trị của biến thứ hai. Thứ hạng được xác định bởi một số chất lượng, chẳng hạn như chất lượng cao
est, thấp nhất, nhanh nhất, chậm nhất, như được xác định bởi biến thứ hai. Thứ hạng có thể được hiển thị trong 
thứ tự tăng dần hoặc giảm dần. Cũng có thể tính toán thứ hạng một cách rõ ràng.
MINH HỌA 7.22  Khám phá 
Cấu trúc dữ liệu xếp hạng 
Mối quan hệ
Xếp hạng làm gì.
Biến được sử dụng
để xếp hạng.
Biến
Biến
Trực quan hóa
Không có hình ảnh trực quan xếp hạng cụ thể, nhưng nhiều hình ảnh tích hợp thông tin xếp hạng, 
bao gồm bảng, biểu đồ thanh và biểu đồ cột. Hình minh họa 7.23 (B) thể hiện biểu đồ cột 
xếp hạng các mẫu xe của HNA (xếp hạng gì) dựa trên số xe bán ra trong giai đoạn 2021–2025

![ILLUSTRATION 7.23](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.23.png)

7-18  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
Khám phá và hiểu biết sâu sắc
Các mối quan hệ xếp hạng khác nhau có thể được khám phá bằng cách kéo và thả. Khách hàng có thể 
được xếp hạng dựa trên doanh số bán hàng hoặc độ tuổi của họ; nhân viên có thể được xếp hạng dựa trên 
lương hoặc thâm niên của họ. Các biện pháp, chẳng hạn như tổng số nợ tồn đọng ít nhất 60 ngày, có thể 
cũng được sử dụng để xếp hạng khách hàng. Thứ hạng có thể xác định, ví dụ, top 25 hoặc cuối cùng 
25 khách hàng dựa trên doanh thu. Biểu đồ cột trong Hình 7.23 cho biết thứ hạng của mô hình 
dựa trên số lượng sản phẩm bán ra trong giai đoạn 2021–2025. Civic là mẫu xe bán chạy nhất 
bởi Hiệp định.
Mẫu khám phá dữ liệu 5: Từng phần đến toàn bộ
Mối quan hệ dữ liệu một phần với toàn bộ (Minh họa 7.24) so sánh các bộ phận với tổng thể và hình thức 
các phần khác nhau so sánh với nhau như thế nào. Ví dụ, một tổ chức có thể tạo ra
đạt được doanh thu 100.000 đô la, đó là toàn bộ. Danh mục sản phẩm gia đình, văn phòng và sân vườn 
tạo ra lần lượt 30.000 USD (30 %), 50.000 USD (50%) và 20.000 USD (20%). Ba sản phẩm này 
danh mục đại diện cho các bộ phận.
MINH HỌA 7.24  Khám phá 
Cấu trúc cho một phần dữ liệu toàn bộ 
Mối quan hệ
Biến đó
xác định cách 
toàn bộ bị phá vỡ
theo từng phần.
Toàn bộ hoặc
số bị phá vỡ
xuống.
số
Biến
danh nghĩa
Biến
Hình dung từ phần đến toàn bộ sẽ xác định số là tổng thể và cách toàn bộ 
nên chia thành nhiều phần. 
(cách xếp hạng). Hình minh họa 7.23 (A) hiển thị mối quan hệ xếp hạng này được tạo cho PivotTable 
trong Excel.
  MINH HỌA 7.23    Tích hợp mối quan hệ dữ liệu xếp hạng vào biểu đồ cột
Biến được sử dụng
để xếp hạng.
Xếp hạng làm gì.
Biến
Biến
dân sự
hiệp định
CR-V
Odyssey
Phi công
Đường sườn núi
3.074.040
2.555.799
1.603.686
898.441
897.807
517.964
người mẫu
Tổng số căn đã bán
dân sự
hiệp định
CR-V
Odyssey
Phi công
Đường sườn núi
Các mô hình được xếp hạng theo tổng số đơn vị đã bán
(A) Tạo mối quan hệ xếp hạng cho PivotTable
(B) Tích hợp mối quan hệ xếp hạng với biểu đồ cột
500.000
0
1.000.000
1.500.000
2.000.000
2.500.000
3.000.000
3.500.000
2.555.799
1.603.686
517.964
3.074.040
898.441
897.807
Sắp xếp lớn nhất đến nhỏ nhất
ZA
AZ
Sắp xếp nhỏ nhất đến lớn nhất

![ILLUSTRATION 7.24](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.24.png)

7.2  Các mối quan hệ dữ liệu được hiển thị như thế nào để khám phá?  7-19
Trực quan hóa
Nhiều hình ảnh trực quan có thể mô hình hóa các mối quan hệ từng phần với toàn bộ, bao gồm biểu đồ hình tròn, bánh rán 
biểu đồ, biểu đồ thanh xếp chồng, biểu đồ cột xếp chồng và sơ đồ dạng cây. Trong khi bản đồ cây được xem xét-
được coi là vượt trội trong việc mô tả các mối quan hệ từng phần với toàn bộ, ở đây chiếc bánh được sử dụng phổ biến hơn 
biểu đồ được hiển thị. Biểu đồ hình tròn trong Hình minh họa 7.25 cho thấy tầm quan trọng tương đối của từng 
Các mẫu xe của HNA là các bộ phận, xét về mặt tổng thể, là các đơn vị được bán trong thời gian 
Giai đoạn 2021–2025. Tầm quan trọng tương đối được thể hiện dưới dạng phần trăm hoặc phần trăm.
MINH HỌA 7.25  Trực quan hóa 
mối quan hệ dữ liệu một phần với toàn bộ 
Với biểu đồ hình tròn
Phân tích số căn bán theo mẫu: 2021–2025
dân sự
32,2%
Phi công
9,4%
Đường sườn núi
5,42%
hiệp định
26,77%
CR-V
16,8%
Odyssey
9,41%
Hình minh họa 7.26 cho thấy cách tạo biểu đồ hình tròn này bằng Power BI:
• Khe Giá trị xác định cái gì: Điều này đề cập đến số được chia nhỏ. Đây, nó 
là thước đo TotalUnitsSold.
• Khe Legend xác định cách thức: Điều này đề cập đến cách chia nhỏ tổng thể. Đây, đây là 
thực hiện theo mô hình. Đối với mỗi giá trị của mô hình, số lượng đơn vị bán được sẽ được tính toán, xác định
ing kích thước phần của nó trong chiếc bánh. Hình ảnh này hiển thị kích thước chia sẻ của nó dưới dạng phần trăm.
Khám phá và hiểu biết sâu sắc
Bất kỳ thước đo nào cũng có thể được kéo vào ô Giá trị (toàn bộ) trong Hình minh họa 7.26. Các biện pháp phù hợp 
cho các nhu cầu cụ thể cũng có thể được tạo ra, chẳng hạn như doanh số bán hàng trong tháng 7 cho khách hàng không ở Hoa Kỳ. Bất kỳ danh nghĩa nào 
biến có thể được kéo vào khe Legend (phần).
MINH HỌA 7.26  Tạo một 
Biểu đồ hình tròn trong Power BI
Truyền thuyết
người mẫu
Chi tiết
Thêm trường dữ liệu ở đây
Giá trị
Tổng số đơn vị đã bán
danh nghĩa
Biến
Biến đó
xác định cách 
toàn bộ bị phá vỡ
theo từng phần.
Toàn bộ hoặc
số bị phá vỡ
xuống.
số
Biến

![ILLUSTRATION 7.26](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.26.png)

7-20  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
Mối quan hệ từng phần với toàn bộ thường được sử dụng trong kế toán. Các ví dụ bao gồm break-
giảm chi phí trong nhiều hạng mục như chi phí hành chính, khấu hao,
chi phí quản lý và phân tích chi phí về nguyên vật liệu, nhân công và chi phí chung.
Biểu đồ hình tròn trong Hình minh họa 7.25 cho thấy mỗi mô hình đóng góp như thế nào, xét về mặt tương đối, vào 
tổng số căn bán được trong giai đoạn 2021–2025. Nó còn cho thấy rằng các mẫu xe Accord và Civic 
tổng cộng chiếm hơn 50% doanh số bán hàng. Thị phần của các mô hình khác, chẳng hạn như 
Ridgeline, tương đối nhỏ.
Mẫu khám phá dữ liệu 6: Tương quan
Mối quan hệ dữ liệu tương quan cho biết mức độ mà hai biến số thay đổi trong 
cùng hướng hoặc ngược chiều. Ví dụ: nếu chi phí tiếp thị cho một sản phẩm tăng lên, 
thì rất có thể doanh số bán sản phẩm tương tự cũng tăng lên. Có hai tính năng chính để 
cân nhắc với những mối quan hệ này. Đầu tiên là hướng:
• Hướng là dương nếu cả hai biến di chuyển cùng hướng.
• Hướng là âm nếu cả hai biến di chuyển theo hướng ngược nhau.
Đặc điểm thứ hai là sức mạnh của mối tương quan. Sức mạnh cho thấy mức độ tương phản
quan hệ giữa hai biến, từ không tương quan đến tương quan hoàn hảo. 
Hình minh họa 7.27 cho thấy cấu trúc thăm dò mối quan hệ dữ liệu tương quan giữa 
các biến số.
MINH HỌA 7.27  Khám phá 
Cấu trúc cho dữ liệu tương quan 
Mối quan hệ
số
Biến
số
Biến
Các biến
mà
dữ liệu tương quan
mối quan hệ là
đang được khám phá.
Trực quan hóa
Hình dung phổ biến nhất để khám phá mối tương quan là biểu đồ phân tán, cũng là 
được gọi là biểu đồ phân tán. Nó vẽ tọa độ cho hai biến cho mỗi điểm dữ liệu.
Hãy minh họa biểu đồ phân tán bằng ví dụ từ một công ty mới. Buzz Cut là một phong cảnh-
đang kinh doanh với hai chủ sở hữu. Những chủ doanh nghiệp nhỏ này liên tục phải đối mặt với những khó khăn về mặt chiến lược, 
các quyết định tài chính và hoạt động, chẳng hạn như ước tính giá cho tài sản. Dữ liệu Họ có một 
bảng tính chứa dữ liệu về kích thước và thời gian cắt trung bình, tính bằng phút, cho tất cả 
thuộc tính (Minh họa 7.28).
Dự toán giá là một quyết định quan trọng đối với tất cả các doanh nghiệp kinh doanh cảnh quan. Buzz Cut sử dụng
Mô hình quyết định hạ thấp để ước tính giá:
• Phải mất một phút để cắt 1.000 feet vuông và Buzz Cut tính phí một đô la mỗi phút 
($60 một giờ). Họ sẽ tính phí 50 USD cho việc cắt cỏ trên một khu đất rộng 50.000 foot vuông.
• Giá tối thiểu cho mỗi lần cắt là $25.
• Giảm giá được cung cấp cho lô lớn.
Tất cả giá được làm tròn: $25, $30, $35, v.v. Trong một số trường hợp, chủ sở hữu của Buzz Cut thương lượng 
với khách hàng. Các quyết định ước tính giá dựa trên hai giả định:
	 1. Kích thước của bãi cỏ quyết định thời gian cần thiết để cắt nó.
	 2. Thời gian quyết định chi phí và do đó quyết định giá cả.
MINH HỌA 7.28  Mười đầu tiên 
Các hàng của Kích thước Dữ liệu Thuộc tính 
Bảng tính thời gian
1
2
3
4
5
6
7
8
9
10
9
6
50
45
8
18
17
55
120
25
Tài sản
thời gian
4500
3000
50000
25000
4000
18000
21000
22000
100000
23000
Kích thước

![ILLUSTRATION 7.28](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.28.png)

7.2  Các mối quan hệ dữ liệu được hiển thị như thế nào để khám phá?  21-7
Giả định đầu tiên có thể được diễn đạt lại: “Có mối tương quan tích cực mạnh mẽ giữa bãi cỏ 
kích thước và thời gian: bãi cỏ càng lớn thì càng mất nhiều thời gian để cắt cỏ.”
Tương quan là mối quan hệ dữ liệu. Giả định có mối tương quan chặt chẽ và chiều hướng tích cực
các vấn đề liên quan đến mối quan hệ dữ liệu do Buzz Cut thực hiện. Biểu đồ phân tán trong Hình 7.29 
khám phá tính đúng đắn của những giả định này.
MINH HỌA 7.29  Biểu đồ phân tán 
Hiển thị mối tương quan giữa kích thước 
và Thời gian
0
0
20.000
40.000
60.000
80.000
100.000
20
40
60
80
100
120
140
thời gian
Kích thước bãi cỏ và mối tương quan thời gian
Kích thước
Biểu đồ phân tán này được tạo trong Power BI (Minh họa 7.30).
MINH HỌA 7.30  Tạo một 
Biểu đồ phân tán trong Power BI
Chi tiết
Tài sản
Thêm trường dữ liệu ở đây
Truyền thuyết
Trục X
Kích thước
Trục Y
thời gian
duy nhất
Mã định danh
Dữ liệu 
điểm đang được
đại diện.
số
Biến
số
Biến
các
biến
vì cái gì
sự tương quan
dữ liệu
mối quan hệ
đang được
đã khám phá.
Khám phá và hiểu biết sâu sắc
Biểu đồ phân tán được tạo bằng cách kéo và thả các biến số từ tập dữ liệu vào 
hai khu vực được thể hiện trong hình minh họa 7.30. Một số thông tin chi tiết có thể được thu thập sau khi biểu đồ phân tán được 
được tạo ra. Ví dụ, có một mối tương quan chặt chẽ và tích cực giữa kích thước bãi cỏ và thời gian. Ở đó 
cũng có hai thông tin chi tiết bổ sung:
	 1. Điểm dữ liệu có nền màu vàng hiển thị giá trị ngoại lệ. Nói chuyện với chủ sở hữu của Buzz 
Cut tiết lộ đây là kết quả của sự cố nhập dữ liệu. Phải mất 18 phút để cắt tài sản, 
nhưng “118 phút” đã được ghi lại.
	 2. Biểu đồ chỉ ra rằng có thể có những yếu tố khác ngoài kích thước ảnh hưởng đến thời gian. 
Các điểm dữ liệu có nền màu xanh lá cây trong Hình minh họa 7.29 biểu thị các thuộc tính 
có cùng kích thước nhưng yêu cầu lượng thời gian khác nhau, với thời gian khác nhau 
trong khoảng từ 17 đến 55 phút (bỏ qua giá trị ngoại lệ ở đây).

![ILLUSTRATION 7.30](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.30.png)