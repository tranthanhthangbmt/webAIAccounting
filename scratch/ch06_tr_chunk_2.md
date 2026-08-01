6.1 Mô hình thông tin là gì? 6-7
được tạo ra bằng cách bán các vật dụng trong vườn ( cái gì ) cho khách hàng sống ở Texas ( ai ) trong năm 2023 
mùa xuân (khi nào)? 
 Khi phát triển các ngôi sao như thế này, điều quan trọng là phải xác định:
• Các biện pháp kế toán bị phá vỡ. 
• Các khía cạnh ai, cái gì và khi nào cho mục đích phân tích. 
 Chương này giải thích cách thực hiện cả hai.  Mô hình hóa thông tin là trung tâm của phân tích dữ liệu. 
Các mô hình thông tin phong phú, mạnh mẽ dẫn đến những phân tích phong phú và chắc chắn. Xây dựng các biện pháp và 
các kích thước phù hợp để phân tích đòi hỏi kỹ năng mã hóa. Nhưng một khi những biện pháp này và 
kích thước đã có sẵn, phần mềm, chẳng hạn như Power BI hoặc Tableau, giúp bạn dễ dàng thực hiện việc phân tích.
ysis. Dù bạn sử dụng phần mềm và ngôn ngữ nào, hãy đầu tư chút thời gian vào việc học cách viết mã. Nó 
sẽ trả hết!
 Áp dụng nó 6.1 
 Hoàn thành một ngôi sao 
Lược đồ 
Hệ thống thông tin kế toán
Kế toán tài chính
Ở nước ngoài là một cửa hàng ở King of 
Trung tâm mua sắm Prussia gần Philadelphia, PA chuyên bán vali và túi xách thời trang. Doanh số bán hàng thật ngoạn mục, nhưng 
ban quản lý tin rằng phân tích dữ liệu là chìa khóa để phát triển hơn nữa. Công ty đang trong quá trình 
xây dựng ứng dụng của họ và chủ sở hữu yêu cầu bạn giúp đỡ. 
 Hình minh họa hiển thị lược đồ hình sao trống cho các giao dịch nhận tiền mặt hoặc thanh toán được thực hiện 
bởi một khách hàng.
 Lược đồ sao nhận tiền mặt dự thảo 
N
N
tham gia
Xảy ra
tham gia
Dòng chảy chứng khoán
N
N
1
1
1
1
Bảng kích thước
Bảng sự kiện
Bảng kích thước
Đến/Từ
Ai?
?
Giao dịch
Biên nhận tiền mặt
Ai?
?
Khi?
?
Cái gì?
?
 Hoàn thành lược đồ hình sao bằng cách trả lời những câu hỏi này.
 1. Bạn sẽ sử dụng nhãn nào cho ai (bên ngoài và bên trong), cái gì và khi nào các bảng được 
được biểu thị bằng các ô trống có dấu chấm hỏi? 
 2. Nêu hai biện pháp liên quan để nhận tiền mặt. 
 3. Đối với cả hai biện pháp, hãy xác định một câu hỏi liên quan cho thấy biện pháp đó có thể được chia nhỏ như thế nào 
bởi thông tin trong các bảng ai, cái gì và khi nào. 
 GIẢI PHÁP 
 (Các giải pháp sẽ khác nhau. Sau đây là ví dụ.) 
 1. Who Table Bên ngoài: Khách hàng (Ai thực hiện thanh toán?) 
Ai ngồi bàn nội bộ: Nhân viên/Thu ngân. (Ai đang xử lý các khoản thanh toán của khách hàng?)

![Apply It 6.1](../TaiLieu/textbookForPractice/Figures/Ch_06/Apply%20It%206.1.png)

6-8  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
	
Bảng gì: Tài khoản (Thanh toán từ khách hàng sẽ làm tăng số dư của tài khoản. Tài khoản 
có thể là tiền mặt, ngân hàng, v.v.)
	
Khi đặt bảng: Lịch (Lịch chứa thông tin về ngày thanh toán 
đã được thực hiện.)
2. Thước đo 1: Tổng số giao dịch nhận tiền mặt.
	
Biện pháp 2: Tổng số tiền nhận được.
3. Biện pháp 1: Số lượng giao dịch (thước đo) nhận tiền mặt trong quý I 
2025 (khi nào) so sánh giữa các nhân viên (ai)?
	
Biện pháp 2: Xu hướng hàng tháng (thời điểm) đối với số tiền (thước đo) nhận được cho 
các tài khoản khác nhau (cái gì) và có bất kỳ biến động nào không?
6.2  Thông tin triển khai mẫu nào 
Thuật toán mô hình hóa? 
MỤC TIÊU HỌC TẬP ❷
Áp dụng các thuật toán mô hình hóa thông tin phổ biến.
Phần này trình bày bảy mẫu triển khai, mỗi mẫu đại diện cho một loại 
thuật toán. Bốn mẫu đầu tiên tạo các cột được tính toán, trong khi ba mẫu cuối cùng tạo ra số liệu
chắc chắn. (Cách thực hiện dữ liệu 6.1 ở cuối chương hướng dẫn cách tạo dữ liệu được tính toán 
cột và số đo bằng Power BI.) Chi tiết của từng mẫu được minh họa bằng 
Ví dụ và tập dữ liệu KLUB. Dữ liệu Tải xuống bộ dữ liệu có sẵn để tạo thông tin 
làm mẫu khi bạn đọc hết chương này.
Mẫu mô hình hóa thông tin 1: Trong bảng 
Tính toán số
Mẫu tính toán số trong bảng sẽ tạo một trường mới (cột được tính toán) 
từ một hoặc nhiều cột số hoặc các trường trong cùng một bảng. phép tính số học cơ bản
các phép cộng, trừ, nhân và chia có thể thực hiện được điều này. Một kỳ thi điển hình-
ple đang xác định tổng số tiền cho một dòng đơn hàng hoặc dòng hóa đơn bằng cách nhân giá 
và số lượng. Hình minh họa 6.7 (A) hướng dẫn cách tạo trường Doanh thu trong hoạt động bán hàng của KLUB 
MINH HỌA 6.7  Tính toán số học trong bảng để xác định doanh thu
1
2
3
4
5
1
1
1
2
2
8
9
16
19
20
12
4
1
40
40
223
223
223
80968
80968
5/1/23
5/1/23
5/1/23
6/1/23
6/1/23
7
7
7
635
635
Nhân viên khách hàng
BánGiá
Số lượng đã bán
Kết quả của thuật toán
BánGiá × Số lượngĐã bán
Doanh thu
Hàng hóa
Ngày
bán hàng
ID dòng hóa đơn
60
20
320
9
20
720
80
320
360
800
Bảng: Doanh thu
Cột được tính toán
Thuật toán
Doanh thu
BánGiá × Số lượngĐã bán
(A)
(B)

![ILLUSTRATION 6.7](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.7.png)

6.2  Những mẫu nào triển khai thuật toán mô hình hóa thông tin?   6-9
Sau khi được triển khai, trường Địa chỉ có thể được sử dụng để tạo bản đồ.
Bằng cách sử dụng các công thức tương tự, mô hình thông tin của KLUB có thể được mở rộng với các trường Tên cho 
cả bảng Khách hàng và Nhà cung cấp (Minh họa 6.9). Nếu bạn đang theo dõi quá trình xây dựng 
Mô hình thông tin của KLUB, đảm bảo tạo cả hai cột.
MINH HỌA 6.9  Tính toán văn bản trong bảng để xác định tên khách hàng và nhà cung cấp
Bảng: Khách hàng
Cột được tính toán
Thuật toán
Tên 
Họ & “ , ” & Tên
Bảng: Nhà cung cấp
Cột được tính toán
Thuật toán
Tên 
Họ & “ , ” & Tên
Mẫu mô hình hóa thông tin 3: Trong bảng 
Phân loại
Về bản chất, số lượng thuật toán phân loại có thể được áp dụng cho một tập dữ liệu là không giới hạn.
ited. Bạn có thể quen với việc phân loại chương trình khách hàng thân thiết theo cấp độ của các hãng hàng không (chẳng hạn như bạc, 
vàng, bạch kim), trong đó thuật toán xác định trạng thái của bạn dựa trên số dặm bay hoặc số tiền 
chi tiêu. Kỹ thuật thống kê về việc tạo nhóm dữ liệu là một ví dụ khác, trong đó các số được 
Mẫu mô hình hóa thông tin 2: Trong bảng 
Tính toán văn bản
Mẫu triển khai thứ hai cũng liên quan đến việc tạo một cột được tính toán mới từ một cột 
hoặc nhiều trường trong cùng một bảng. Tuy nhiên, thông tin trong cột mới được tạo từ 
các trường văn bản. Ví dụ: các phần thông tin vị trí khác nhau có thể được liên kết hoặc ghép nối
được ghi vào một địa chỉ để dịch vụ bản đồ như Bing Maps hoặc Google Maps có thể đọc được.
Hình minh họa 6.8 (A) hiển thị thuật toán tạo trường địa chỉ trong Khách hàng của KLUB 
cái bàn. (Ký hiệu dấu và biểu thị sự ghép nối.) Trường mới trong bảng Khách hàng 
trong Hình minh họa 6.8 (B) là kết quả của việc áp dụng phép tính này.
bảng có tính toán như vậy. Hình minh họa 6.7 (B) cho thấy kết quả: trường Doanh thu 
là một phần của bảng Bán hàng. Sau đó, chúng ta sẽ sử dụng trường Doanh thu làm khối xây dựng cho 
Đo lường tổng doanh thu.
MINH HỌA 6.8  Tính toán văn bản trong bảng để xác định địa chỉ khách hàng
1
2
3
4
5
3462 Phố MacLaren
2608 Ngõ nguyệt quế
4679 ngõ Byrd
Ổ đĩa 975 Armbrester
3251 đường St John
BẬT
TX
NM
CA
SK
K1P 5M7
79703
87102
90265
S4P 3Y2
Ottawa
thiết bị đầu cuối
Albuquerque
Malibu
Bruno
CA
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
CA
Mã zip
Quốc gia
Đường + Thành phố + Bang + Mã Zip + Quốc gia
Địa chỉ
tiểu bang
Thành phố
đường phố
ID khách hàng
3462 MacLaren Street,Ottawa,ON,K1P 5M7,CA
2608 Laurel Lane,Nhà ga,TX,79703,Hoa Kỳ
4679 Byrd Lane,Albuquerque,NM,87102,Hoa Kỳ
975 Armbrester Drive, Malibu, CA, 90265, Hoa Kỳ
3251 Phố St. John,Bruno,SK,S4P 3Y2,CA
Kết quả của thuật toán
(B)
Bảng: Khách hàng
Cột được tính toán
Thuật toán
Địa chỉ
Đường phố & “,” & Thành phố & “,” & Tiểu bang & “,” & Zip & “,” & Quốc gia
(A)

![ILLUSTRATION 6.9](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.9.png)

6-10  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
được nhóm thành các số “thùng” nhỏ hơn, chẳng hạn như nhóm tuổi. Trên thực tế, việc phân loại là đa dạng
có mặt trong kế toán, chẳng hạn như phân loại các khoản phải thu theo độ tuổi để xác định nợ khó đòi 
chi phí.
Mẫu triển khai thứ ba được sử dụng khi phân loại được xác định dựa trên 
dữ liệu là một phần của cùng một bảng. Hầu hết các thuật toán phân loại đều dựa vào logic Boolean, vì vậy nó 
là cần thiết để hiểu các toán tử Boolean như các hàm AND, OR, NOT và IF cũng như cách 
để tạo ra chúng.
Với cả mã (A) và sơ đồ (B) Minh họa 6.10 cho thấy hàm IF có thể 
chia khách hàng thành hai loại: cấp dưới (đến 40 tuổi) và cấp cao (trên 40 tuổi). 
Hình minh họa 6.10 (C) là kết quả của việc áp dụng thuật toán này. Trường AgeCategory mới bây giờ là 
một phần của bảng Khách hàng.
MINH HỌA 6.10  Phân loại trong bảng Sử dụng hàm IF để xác định danh mục độ tuổi của khách hàng
Loại tuổi =
cao cấp
Loại tuổi =
Thiếu niên
Tuổi < =
40
1
2
3
4
5
25
22
68
71
54
Thiếu niên
Thiếu niên
cao cấp
cao cấp
cao cấp
ID khách hàng
Tuổi
TuổiThể loại
Kết quả của
Thuật toán
sai
đúng
Cột được tính toán
Thuật toán
Loại tuổi = Người cao tuổi
TuổiCategory = Junior
Tuổi <= 40
Bảng: Khách hàng
(C)
(A)
(B)
Sau khi triển khai, chúng ta có thể sử dụng trường AgeCategory để phân tích. Minh họa 6.11 
hiển thị tỷ lệ tương ứng của khách hàng cấp dưới và cấp cao của KLUB.
MINH HỌA 6.11  Biểu đồ hình tròn được tạo bằng trường AgeCategory
cao cấp
65.203 (65,2%)
Thiếu niên
34.797 (34,8%)
Tầm quan trọng tương đối của các loại tuổi
Mẫu mô hình hóa thông tin 4: Trên bảng 
Tính toán
Các phép tính cho mẫu này giống như ba mẫu đầu tiên–một cột mới được tạo từ tồn tại-
nhập dữ liệu bằng cách sử dụng số học, tính toán văn bản hoặc phân loại. Nhưng mô hình này khác với 
các mẫu trước đó vì dữ liệu từ các bảng khác nhau được sử dụng để tạo cột mới. Cái này 
có nghĩa là các bảng phải được liên kết. Việc này được thực hiện như thế nào tùy thuộc vào phần mềm đang được

![ILLUSTRATION 6.11](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.11.png)

6.2  Những mẫu nào triển khai thuật toán mô hình hóa thông tin?   6-11
đã sử dụng. Excel sử dụng hàm VLOOKUP, trong cơ sở dữ liệu quan hệ, việc này được thực hiện bằng phép nối và trong DAX thì 
được thực hiện bằng hàm LIÊN QUAN. Bất kể phần mềm nào, đều có nhiều 
Các câu hỏi cần cân nhắc khi liên kết các bảng:
• Có mối quan hệ được xác định chính xác giữa các bảng không?
• Bản chất của mối quan hệ là gì và nên xem xét loại liên kết nào?
• Những số lượng nào áp dụng cho mối quan hệ: 1-1, 1-N, N-1, hay N-N? Ví dụ, tính toán
các vấn đề trở nên phức tạp hơn khi điều hướng mối quan hệ 1-N.
Hãy sử dụng một ví dụ về phép tính trên nhiều bảng để minh họa một số vấn đề này. thu hồi 
KLUB mua sản phẩm theo đợt:
• Giá mua hoặc giá thành mỗi đơn vị trong một đợt được ghi vào bảng Mua hàng.
• Doanh thu của mặt hàng bán được xác định bằng cách nhân Giá bán và Số lượng đã bán 
các trường trong bảng Doanh số, dẫn đến trường Doanh thu (là cột được tính toán) 
đã thảo luận trước đó.
• Chi phí phù hợp được xác định bằng cách nhân Giá Mua trong bảng Mua với 
Số lượng được bán trong bảng Bán hàng.
Hình minh họa 6.12 là thuật toán tính giá vốn hàng bán (COGS). Vì dữ liệu từ 
các bảng khác nhau được sử dụng, tên bảng hiện được đưa vào thuật toán dưới dạng TableName.Field-
Tên. Ví dụ: Sales.QuantitySold đề cập đến trường Số lượng đã bán trong bảng Doanh số.
MINH HỌA 6.12  Tính toán theo bảng để xác định giá vốn hàng bán
Bảng: Doanh thu
Cột được tính toán
Thuật toán
giá vốn
Doanh số.Số lượng đã bán × Số lần mua.Giá mua
Hình minh họa 6.13 là mô hình dữ liệu mà việc triển khai cột COGS dựa vào.
MINH HỌA 6.13  COGS khi tính toán trên nhiều bảng
Số lượng bán được của một
sản phẩm cụ thể như
một phần của việc bán hàng cụ thể
(Dòng hóa đơn)
bán hàng
N
1
Thu gọn
Khách hàng
∑
nhân viên
∑
Hàng hóa
ID dòng hóa đơn
∑
Số lượng đã bán
∑
bán hàng
∑
BánGiá
∑
Ngày
Doanh thu
∑
ID lô
Mua hàng
MuaGiá
Ngày
∑
Số lượng đã mua
nhà cung cấp
∑
∑
Thu gọn
ID lô
Hàng hóa
Thương hiệu
Danh mục
Mã
Hoa hồng
Mô tả
Giá bán tối thiểu
Loại
Thu gọn
1
1
Giá phù hợp
đã trả (Chi phí) cho
mặt hàng đã bán
Các giá trị trong cột COGS trong bảng Doanh số được tính bằng cách nhân Quan-
trường titySold trong bảng Bán hàng theo trường Giá Mua tương ứng trong bảng Mua hàng. 
Các giá trị tương ứng được xác định bằng cách tuân theo các mối quan hệ, được gọi là

![ILLUSTRATION 6.13](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.13.png)

6-12  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
MINH HỌA 6.14  Biểu đồ cột được tạo bằng các trường giá vốn hàng bán và doanh thu
Điện tử
Vườn
văn phòng
$0
100.000 USD
So sánh doanh thu và giá vốn hàng bán
Trên các danh mục sản phẩm
200.000 USD
300.000 USD
400.000 USD
giá vốn
Doanh thu
500.000 USD
26.598
58.025
50.149
132.300
146.090
431.308
Việc áp dụng bốn mẫu triển khai đầu tiên đã mở rộng lược đồ sao Bán hàng của KLUB 
(Minh họa 6.15) với các cột được tính như sau:
• Địa chỉ (Khách hàng)
• AgeCategory (Khách hàng)
• COGS (Doanh thu)
• Tên (Khách hàng)
• Doanh thu (Doanh thu)
Ngoài ra, trường được tính toán Tên đã được thêm vào bảng Nhà cung cấp trong ngôi sao Mua hàng của KLUB 
lược đồ. 
đường dẫn hướng. Dưới đây là một số đặc điểm của quá trình điều hướng để thực hiện 
công thức này:
• Đường màu xanh biểu thị đường dẫn điều hướng trong Hình minh họa 6.13. Lĩnh vực Hàng hóa tại 
bảng Bán hàng được liên kết với trường BatchID trong bảng Hàng hóa dựa trên kết quả khớp 
các giá trị. Một mối quan hệ tương tự được tạo ra giữa trường BatchID trong Hàng hóa 
bảng và trường BatchID trong bảng Mua hàng. Nếu KLUB bán máy sấy tóc cho khách hàng
tomer, đường dẫn điều hướng sẽ tiết lộ nó thuộc về lô nào và do đó chúng thuộc về ai 
mua nó, khi nào và với giá bao nhiêu (chi phí).
• Đường dẫn điều hướng có số lượng 1-1. Có một mặt hàng hàng hóa (Merchan-
dise) trên mỗi dòng hóa đơn (Bán hàng) và một lần mua hàng (Mua hàng) cho một mặt hàng hàng hóa 
(Hàng hóa).
• Không có vấn đề gì khi tham gia. Có chính xác một mặt hàng cho mỗi dòng hóa đơn và có 
chính xác là một lần mua cho mỗi hàng hóa.
Sau khi triển khai, trường COGS có thể được sử dụng để phân tích. Tạo biểu đồ cột theo cụm
được kết hợp với trường COGS trong Hình minh họa 6.14 có thể được ban quản lý KLUB sử dụng để so sánh 
doanh thu và giá vốn hàng bán trên ba loại sản phẩm: điện tử, sân vườn và văn phòng.

![ILLUSTRATION 6.15](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.15.png)

6.2  Những mẫu nào triển khai thuật toán mô hình hóa thông tin?   6-13
MINH HỌA 6.15  Mô hình thông tin của KLUB được mở rộng bằng các cột được tính toán
ID nhân viên
Email
Tên đầu tiên
Giới tính
Họ
Sssn
nhân viên
ID khách hàng
Tuổi
Thành phố
Quốc gia
Tên đầu tiên
Giới tính
Họ
đường phố
tiểu bang
Điện thoại
Tiêu đề
Mã zip
Địa chỉ
TuổiThể loại
Tên
Khách hàng
Bảng kích thước
Bảng sự kiện
Bảng kích thước
ID lô
Thương hiệu
Danh mục
Mã
Hoa hồng
Mô tả
Giá bán tối thiểu
Loại
Hàng hóa
Ngày
Lịch
1
1
1
1
N
N
N
N
ID dòng hóa đơn
bán hàng
BánGiá
Số lượng đã bán
giá vốn
Doanh thu
bán hàng
Khách hàng
Ngày
nhân viên
Hàng hóa
Chìa khóa
Cột
Cột được tính toán
Đo lường
Khóa ngoại
Đã thêm cột tính toán
đến mô hình thông tin
Mẫu mô hình thông tin 5: Cột đơn 
Tổng hợp
Mẫu tổng hợp một cột là mẫu đầu tiên tập trung vào các thước đo, như bạn có 
đã học, là trái tim của phân tích dữ liệu. Các biện pháp tính toán các tập hợp có thể được cắt lát hoặc 
bị phá vỡ, theo nhiều cách.
Ở dạng đơn giản nhất, thước đo áp dụng một phép toán cho tất cả các giá trị của một 
cột đơn. Các thao tác có thể được áp dụng bao gồm các hàm tổng hợp như SUM, 
TRUNG BÌNH, ĐẾM, MIN và MAX. Mỗi hàm này tạo ra một giá trị duy nhất. cho 
hầu hết các ứng dụng, các thước đo một cột chiếm một phần quan trọng trong thông tin 
mô hình. Một số điều khác về hàm tổng hợp:
• Ngoại trừ các hàm tổng hợp đếm, hầu hết đều yêu cầu kiểu dữ liệu số.
• Đảm bảo hiểu cách các hàm tổng hợp xử lý các giá trị cụ thể, chẳng hạn như null, 
vì điều này có thể khác nhau tùy thuộc vào nền tảng triển khai.
Có thể tạo ba thước đo bằng cách sử dụng tập hợp một cột cho tập dữ liệu của KLUB: 
	 1. TotalQuantitySold: Tính tổng số đơn vị (tổng hợp) được KLUB bán theo 
sử dụng hàm SUM để cộng tất cả các giá trị trong trường Số lượng đã bán trong bảng Doanh số.
	 2. TotalRevenue: Tính toán tổng doanh thu (tổng hợp) do KLUB tạo ra cho đến nay. thông báo 
rằng hàm tổng hợp SUM sử dụng trường được tính Doanh thu làm đối số.
	 3. NumberOfCustomers: Tính số lượng khách hàng của KLUB (tổng hợp) theo count-
nhập tất cả các ô trong trường CustomerID của bảng Khách hàng không trống. Bởi vì 
CustomerID là khóa chính, không có ô trống và tất cả các hàng trong bảng đang được 
được tính.