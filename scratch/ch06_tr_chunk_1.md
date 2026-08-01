6-0
 C H A P T ÉP 6 
 Phân tích: Thông tin 
Làm người mẫu 
 Xem trước chương 
 Sau khi lập kế hoạch cho dự án và hoàn thành việc chuẩn bị dữ liệu, bạn có thể rất hào hứng 
cuối cùng khám phá dữ liệu và tạo ra những hiểu biết sâu sắc. Mặc dù dữ liệu có thể đã sẵn sàng để phân tích nhưng vẫn có 
vẫn còn thiếu một phần – thông tin cần thiết để thực hiện phân tích. Ví dụ, dữ liệu 
được lựa chọn và chuẩn bị cho việc phân tích có thể bao gồm một tập hợp các giao dịch nhưng không biết 
tổng doanh thu hoặc lợi nhuận được tạo ra, chúng không thể được phân tích để xác định sản phẩm nào 
có lãi. 
 
 Có hai nhiệm vụ lập mô hình thông tin quan trọng cần hoàn thành trước khi khám phá dữ liệu. 
Đầu tiên, bạn phải hiểu thông tin nào cần thiết để phân tích và dữ liệu nào cần thiết 
để tạo ra thông tin đó. Bạn đã làm điều này trong giai đoạn lập kế hoạch khi bạn phát triển một chiến lược 
để lựa chọn dữ liệu và phân tích tốt nhất để trả lời các câu hỏi kế toán. Nhiệm vụ thứ hai là xác định
đưa ra các biện pháp cụ thể mà bạn muốn sử dụng để phân tích dựa trên tập dữ liệu đã chuẩn bị, sau đó 
viết mã tạo ra thông tin này. 
 
 Mô hình hóa thông tin là một quá trình. Chương này sẽ giúp bạn phát triển các kỹ năng để làm điều đó 
thành công bằng cách cung cấp một danh mục các mẫu cho các cấu trúc mã hóa phổ biến và để xác định
thông tin được sử dụng trong phân tích kế toán. 
Phân tích
kế hoạch
Báo cáo
Giai đoạn 2
Giai đoạn 3
Giai đoạn 1
Phiên dịch
giao tiếp
Phân tích
Chiến lược
Mục tiêu
Động lực
Phát hiện và
dữ liệu chính xác
vấn đề
Xác định và
tính toán liên quan
thông tin
Khám phá thông tin chi tiết
thích hợp cho
ra quyết định
Thông tin
Làm người mẫu
dữ liệu
Thăm dò 
dữ liệu
Chuẩn bị

Cái nhìn sâu sắc chuyên nghiệp: Tại sao mô hình hóa thông tin lại quan trọng?
Sau khi lấy được bằng kế toán, Dan bắt đầu làm cố vấn thuế cho một trong những tập đoàn lớn. 
Bốn công ty kế toán đại chúng, nơi anh yêu thích dữ liệu và phân tích dữ liệu. Thêm 
Gần đây, anh ấy chuyển đến một tập đoàn viễn thông đa quốc gia nơi anh ấy làm việc ở vị trí chuyên viên dữ liệu. 
nhà phân tích.
Là một nhà phân tích dữ liệu, tôi phải linh hoạt. Tôi xử lý tập dữ liệu thô từ nhiều nguồn 
và tham gia rất nhiều vào ETL (trích xuất-chuyển đổi-tải). Tôi cũng khám phá dữ liệu để tổng hợp
đã thu thập thông tin chi tiết về các bên liên quan ở nhiều bộ phận và phát triển bảng thông tin. 
Liên tục đối mặt với những thử thách mới là điều tôi thực sự thích ở công việc của mình. Hai ngày 
trước đây, tôi đã xử lý dữ liệu phi cấu trúc (văn bản), hôm qua tôi đã viết mã một thuật toán mới-
rithm và hôm nay tôi đang làm việc trên một trang tổng quan trình bày một tập hợp các KPI có liên quan với nhau.
Mặc dù tôi dành phần lớn thời gian của mình cho ETL nhưng tôi nghĩ việc lập mô hình thông tin là trọng tâm của 
phân tích dữ liệu. Nó liên quan đến việc mã hóa các phép tính, kiểm tra xem chúng có đúng không và 
đảm bảo có sẵn thông tin cần thiết cho các trường hợp kinh doanh khác nhau. Cái này 
đó là nơi mà tấm bằng kế toán của tôi có ích vì tôi có thể hiểu được bối cảnh kinh doanh.
Lộ trình chương
MỤC TIÊU HỌC TẬP
CHỦ ĐỀ
ÁP DỤNG NÓ
 LO 6.1   Mô tả 
các khái niệm nền tảng của 
mô hình hóa thông tin.
• Quá trình lập mô hình thông tin
• Cách tiếp cận có cấu trúc
Hoàn thành lược đồ sao 
(Ví dụ: Thông tin kế toán 
Hệ thống và Kế toán tài chính)
 LO 6.2   Áp dụng chung 
mô hình hóa thông tin 
thuật toán.
Bảy mẫu mô hình thông tin 
cho thuật toán
Sử dụng thuật toán để tính mạng 
Doanh thu 
(Ví dụ: Kế toán tài chính)
 LO 6.3   Phát triển và triển khai 
mô hình thông tin chung 
cấu trúc dữ liệu kế toán
Sáu mẫu mô hình hóa thông tin cho 
Cấu trúc dữ liệu kế toán phổ biến
Trả lời câu hỏi bằng một ngôi sao 
Lược đồ
(Ví dụ: Kế toán quản trị)
Dữ liệu   Thẻ Dữ liệu xuất hiện trong chương khi dữ liệu cho một ví dụ, hình minh họa hoặc ứng dụng được 
có sẵn trên nền tảng học tập trực tuyến của Wiley.
Phần mềm phân tích dữ liệu liên tục thay đổi và có thể có nhiều phiên bản phần mềm mới hơn.
được đưa ra trong chương này. Để biết thêm thông tin, hãy truy cập video đi kèm trên nền tảng học tập trực tuyến của Wiley. 
6.1  Mô hình thông tin là gì?
MỤC TIÊU HỌC TẬP ➊
Trình bày các khái niệm cơ bản của mô hình hóa thông tin.
Mô hình hóa thông tin là quá trình tạo ra kiến thức bổ sung từ dữ liệu có liên quan.
thích hợp cho mục đích phân tích. Tiếp theo, chúng ta xem xét việc này được thực hiện như thế nào trong bối cảnh kế toán.
6.1  Mô hình thông tin là gì?  6-1

6-2  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
Quá trình mô hình hóa thông tin
Trong mô hình hóa thông tin, dữ liệu là đầu vào. Chúng là những số liệu thô và sự kiện. Thuật toán 
là các tập lệnh chuyển đổi dữ liệu thành thông tin, là đầu ra của phép cộng
kiến thức thu được từ dữ liệu (Minh họa 6.1).
MINH HỌA 6.1  Quá trình mô hình hóa thông tin
Thuật toán
Thông tin
dữ liệu
chuyển đổi
đầu ra
đầu vào
Mô hình thông tin
Thuật toán là mối liên kết giữa đầu vào của sự kiện và đầu ra của thông tin hữu ích. Giữ 
hãy nhớ rằng dữ liệu (đầu vào) cho một ứng dụng cũng có thể là thông tin (đầu ra) cho ứng dụng khác 
ứng dụng. Một ví dụ là báo cáo tài chính là thông tin (đầu ra) cho hoạt động tài chính 
người chuẩn bị báo cáo nhưng họ là dữ liệu (đầu vào) cho các nhà phân tích tài chính.
Các thuật toán là công việc nội tại của kế toán viên. Những hướng dẫn này tính toán khấu hao
liên quan, chi phí, tỷ lệ tài chính, và nhiều hơn nữa. Chúng bao gồm từ đơn giản đến phức tạp và có thể được mã hóa 
với nhiều ngôn ngữ, bao gồm các hàm Excel, Biểu thức phân tích dữ liệu của Power BI 
(DAX) và ngôn ngữ lập trình Python. Trong chương này chúng ta sẽ dựa vào gen-
mô tả thực tế của các thuật toán.
Bảy cột đầu tiên trong Hình minh họa 6.2 là các trường dữ liệu. Chúng là những mô tả thực tế 
về các giao dịch bán hàng, chẳng hạn như số nhận dạng của giao dịch và ngày xảy ra. 
Trong kế toán, những mô tả này có thể bao gồm từ số an sinh xã hội của nhân viên đến 
tên các khách hàng đã thực hiện thanh toán. Hai cột cuối cùng trong Hình minh họa 6.2 
chứa thông tin đã được tính toán bằng thuật toán.
MINH HỌA 6.2  Dữ liệu, thông tin và thuật toán cho giao dịch bán hàng
Thông tin
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
3/1/2022
3/1/2022
3/1/2022
4/1/2022
4/1/2022
4/1/2022
4/1/2022
4/1/2022
4/1/2022
5/1/2022
825
$
$
$
$
2.500 USD
2.500 USD
1.250 USD
900
1.500 USD
1.500 USD
1.000 USD
900
500
825
$
$
$
$
$
2.400 USD
2.250 USD
$1,175
775
1.250 USD
1.350 USD
950
900
450
0
100
250
75
125
250
150
50
0
50
Máy rửa chén
Tủ lạnh
Tủ lạnh
Bếp nấu
Máy rửa chén
Bếp nấu
Lò nướng
Bếp nấu
Bếp nấu
Máy rửa chén
Jeremy
Jane
Molly
Whitney
Zuzu
Carmen
Ben
Lebron
Trisha
xuomin
Giảm giá
Khách hàng
Nhân viên bán hàng
Kích thước giao dịch
Số tiền
sản phẩm
Ngày
ID
Ed
Juana
Hakeem
Ed
Juana
Cindy
Hakeem
Juana
Hakeem
Cindy
S
M
M
M
S
M
M
S
S
S
NẾU số tiền ròng của một giao dịch nhỏ hơn 1.000 USD,
THÌ Kích thước giao dịch là S (nhỏ), 
KHÁC
    NẾU số tiền ròng của một giao dịch ít nhất là 1.000 USD nhưng nhỏ hơn 2.500 USD,
    THÌ Kích thước giao dịch là M (trung bình), 
    ELSE quy mô giao dịch là L (lớn). 
Số tiền – Giảm giá
Thuật toán cho NetAmount
Thuật toán cho kích thước giao dịch
dữ liệu
Số tiền ròng

![ILLUSTRATION 6.2](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.2.png)

6.1  Mô hình thông tin là gì?  6-3
Có hai loại trường thông tin:
• Trong Hình minh họa 6.2, cả NetAmount và TransactionSize đều là một cột được tính toán trong phần 
Bảng SalesTransactions vì một giá trị được tính cho mỗi ô trong các cột. Họ 
là những phần không thể thiếu của bảng.
• Loại trường thông tin thứ hai là thước đo, là tổng hợp hoặc tổng cộng 
có thể được sử dụng trong các báo cáo và do đó cho mục đích phân tích. Các biện pháp được tạo ra bởi thuật toán
nhịp điệu, nhưng chúng không phải là bộ phận không thể thiếu của một bảng.
Hai thước đo có thể được tính toán cho bảng trong Hình minh họa 6.2 là tổng số tiền ròng 
được tạo ra bởi doanh số bán hàng và số lượng giao dịch lớn. Các thuật toán cho các biện pháp này 
được thể hiện trong hình minh họa 6.3.
MINH HỌA 6.3  Thuật toán tính tổng số tiền ròng và số lượng giao dịch lớn
Đo lường 
Thuật toán
Tổng số tiền ròng 
Tổng tất cả các giá trị trong cột NetAmount.
Số lượng giao dịch lớn
Đếm số ô trong cột Kích thước giao dịch có 
giá trị “L.”
Các biện pháp là trung tâm của phân tích dữ liệu. Chúng có thể được tính toán và sau đó được cắt thành từng phần 
nhiều cách trong quá trình khám phá dữ liệu. Phần mềm phân tích dữ liệu, như Power BI và Tableau, 
giúp bạn dễ dàng tạo và cắt chúng.
Một cách tiếp cận có cấu trúc
Việc thực hiện phân tích dữ liệu đòi hỏi phải xác định các con số cần phân tích (đây là các
chắc chắn) và cách phân tích chúng (đây là các thứ nguyên hoặc các trường có thể cắt chúng). 
Chương này mô tả cách tiếp cận có cấu trúc để phát triển các mô hình thông tin kế toán bằng cách 
xác định các khía cạnh của ai, cái gì và khi nào trong các giao dịch để giúp kế toán có ý nghĩa 
của dữ liệu. Một thước đo như tổng doanh thu có thể được chia nhỏ theo các khía cạnh sau:
• Khách hàng (ai?).
• Loại sản phẩm (cái gì?).
• Năm (khi nào?).
Các kích thước như thế này và số đo mà chúng có thể cắt, thường được định cấu hình theo hình sao 
lược đồ. (Như bạn đã học trước đó trong khóa học này, lược đồ hình sao là cấu trúc dữ liệu được ưu tiên 
để phân tích dữ liệu.) Hãy sử dụng một ví dụ để giúp minh họa điều này. Dữ liệu   KLUB là một cửa hàng bán lẻ 
tọa lạc tại Interlochen, MI:
• Chủ sở hữu KLUB sử dụng kết nối kinh doanh ở các không gian bán lẻ khác nhau để đàm phán mua số lượng lớn
theo đuổi mức giá chiết khấu cao và ký chính sách không hoàn trả với tất cả các nhà cung cấp để cung cấp
sau đó giảm giá.
• Công ty bán các mặt hàng này với giá thấp hơn so với đối thủ cạnh tranh nhưng vẫn có giá trị
tỷ suất lợi nhuận tạm thời.
• Chủ sở hữu xử lý mọi cuộc đàm phán, hợp đồng và giao hàng với nhà cung cấp.
• Nhân viên bán hàng là nhà thầu được hưởng hoa hồng trên sản phẩm bán được.
Trang web của KLUB hiển thị các mặt hàng hiện có nhưng việc bán hàng chỉ được thực hiện trên 
điện thoại. Công ty thường xuyên gửi email tiếp thị tới danh sách 100.000 khách hàng tiềm năng. 
Khi khách hàng muốn mua thứ gì đó, họ gửi email cho công ty và nhân viên bán hàng liên hệ 
họ.
KLUB

![ILLUSTRATION 6.3](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.3.png)

6-4  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
Sau sáu tháng kinh doanh, người chủ tò mò muốn biết công ty sẽ đứng ở đâu? 
quan điểm bán hàng và lợi nhuận, đồng thời thuê bạn cung cấp một số thông tin chi tiết. Bạn được cung cấp compa-
dữ liệu có sẵn của ny. Tập dữ liệu rõ ràng và có cấu trúc dưới dạng lược đồ hình sao.
Từ mô hình dữ liệu đến mô hình thông tin
Hình minh họa 6.4 hiển thị lược đồ hai sao cho tập dữ liệu KLUB. Mô hình thông tin 
vẫn chưa được tạo ra.
MINH HỌA 6.4  Lược đồ sao mua và bán của KLUB
Bảng kích thước
Bảng sự kiện
Bảng kích thước
Hàng hóa
Lịch
Khách hàng
nhân viên
bán hàng
Lược đồ ngôi sao bán hàng
1
1
N
N
1
1
N
N
Bảng kích thước
Bảng sự kiện
Bảng kích thước
nhà cung cấp
Lịch
Hàng hóa
Mua hàng
Ngôi sao mua hàng
Lược đồ
1
1
N
N
1
N
Lược đồ hình sao là một mô hình dữ liệu. Mô hình dữ liệu hiển thị cấu trúc của tập dữ liệu. Nó cho thấy 
các khái niệm đang được mô tả, các bảng và các trường được sử dụng để mô tả các khái niệm. Một 
mô hình thông tin mở rộng mô hình dữ liệu vì nó cũng bao gồm các cột được tính toán và 
biện pháp. Nó có thông tin bổ sung được tính toán từ tập dữ liệu, có thể được sử dụng 
cho mục đích phân tích.
Hình minh họa 6.5 hiển thị lược đồ sao Bán hàng mở rộng với các tên trường như Thương hiệu, 
Quốc gia và Giới tính. Trong hình minh họa này, bảng dữ kiện mô tả các giao dịch bán hàng. những cánh đồng 
có dấu hỏi cho biết các cột và thước đo được tính toán của mô hình thông tin 
sẽ được phát triển trong chương này.

![ILLUSTRATION 6.5](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.5.png)

6.1  Mô hình thông tin là gì?  6-5
MINH HỌA 6.5  Lược đồ sao bán hàng mở rộng
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
?
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
?
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
Khách hàng
Ngày
nhân viên
Hàng hóa
?
?
?
?
?
bán hàng
Chìa khóa
Cột
Cột được tính toán
Đo lường
Khóa ngoại
?
?
?
ÁP DỤNG TƯ duy phê phán 6.1: Cùng dữ liệu, khác KPI
Các thước đo đưa vào các chỉ số hiệu suất chính (KPI), là những con số mà doanh nghiệp mong muốn 
để theo dõi và sau đó phân tích. Phát triển một mô hình thông tin đòi hỏi phải nói chuyện với những người khác nhau
ple trên toàn công ty của bạn:
• Những người bị ảnh hưởng bởi việc phân tích đều có thể muốn có KPI của riêng họ. Hãy xem xét 
dữ liệu bán hàng—người quản lý tiếp thị có thể quan tâm đến việc phân tích tỷ lệ rời bỏ, trong khi 
kế toán viên có thể quan tâm đến việc phân tích các khoản phải thu và chi phí nợ khó đòi. các 
cùng một dữ liệu đang được phân tích nhưng phải áp dụng các KPI khác nhau (Các bên liên quan).
• Một KPI có thể có ý nghĩa khác nhau đối với những người khác nhau. Điều gì sẽ xảy ra nếu bạn được yêu cầu phân tích lợi nhuận? 
ký quỹ? Đó là tỷ suất lợi nhuận gộp hay tỷ suất lợi nhuận ròng? Hãy chắc chắn rằng bạn hiểu 
thuật toán (Kiến thức)!
Tạo số đo và kích thước
Có hai mục tiêu để xây dựng mô hình thông tin cho lược đồ sao. Đầu tiên là tạo 
một tập hợp các thước đo phong phú cho bảng sự kiện. Hãy nhớ lại rằng trong lược đồ hình sao, các bảng sự kiện thường chứa 
giao dịch kinh doanh. Ví dụ, trong Hình minh họa 6.2 cột NetAmount đã được tạo

6-6  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
và sau đó được sử dụng để tạo thước đo TotalNetAmount, là thước đo tổng hợp. Tính toán 
các trường trong bảng thực tế thường được sử dụng làm khối xây dựng cho các biện pháp.
Mục tiêu thứ hai của việc xây dựng mô hình thông tin là tập hợp các kích thước phong phú có thể 
phá vỡ, hoặc cắt lát, các biện pháp theo nhiều cách. Các kích thước hữu ích trong Hình minh họa 6.5 bao gồm 
Giới tính, Bang, Quốc gia, Thương hiệu, Loại và Danh mục. Trong ví dụ KLUB, nó có thể hữu ích 
để so sánh lợi nhuận giữa các nhãn hiệu, loại, danh mục và quốc gia sản phẩm. Nhiều kích thước hơn 
có thể được tạo thông qua các cột được tính toán. Một ví dụ về thứ nguyên mà chúng tôi sẽ phát triển với 
các cột được tính toán cho ngôi sao Bán hàng của KLUB là AgeCategory, giúp phân biệt giữa cấp dưới 
và khách hàng cấp cao.
Bảng thứ nguyên có thể mô tả các đặc điểm cụ thể của giao dịch: ai đã tham gia, 
những gì liên quan và khi nào chúng xảy ra1:
• Bảng chiều mô tả các tác nhân tham gia vào các giao dịch là bảng who. 
Đại lý nội bộ là những nhân viên tham gia giao dịch. Các tác nhân bên ngoài, chẳng hạn 
với tư cách là khách hàng và nhà cung cấp, là các bên bên ngoài tổ chức có liên quan đến tài khoản-
giao dịch. Một mối quan hệ tham gia liên kết các đại lý với các giao dịch cụ thể.
• Bảng thứ nguyên mô tả các tài nguyên đã được từ bỏ hoặc có được như một phần 
của một giao dịch là một bảng gì. Trong ví dụ về KLUB, việc mua hàng làm tăng
giảm, trong khi doanh số bán hàng giảm. Mối quan hệ luồng liên kết các tài nguyên với các nguồn cụ thể 
giao dịch.
• Bảng thứ nguyên mô tả khi nào một giao dịch xảy ra là bảng khi nào. Những bảng như vậy 
thường có dạng bảng Lịch. Một mối quan hệ xảy ra liên kết lịch với 
giao dịch cụ thể.
Hình minh họa 6.6 là lược đồ sao Bán hàng của KLUB được gắn nhãn với thứ nguyên ai, cái gì và khi nào 
bảng và mối quan hệ của chúng.
1Các khía cạnh của ai-cái gì-khi nào của các giao dịch kế toán lần đầu tiên được ghi nhận ở McCarthy, William E. (1982) 
Mô hình kế toán REA: Khung tổng quát cho hệ thống kế toán trong môi trường dữ liệu dùng chung. 
Kiểm tra kế toán: 554-578.
N
N
tham gia
Xảy ra
tham gia
Dòng chảy
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
Khách hàng
Giao dịch
bán hàng
Ai? 
nhân viên
Khi nào? 
Lịch
Cái gì? 
Hàng hóa
MINH HỌA 6.6  Ngôi sao bán hàng với các bảng thứ nguyên Ai, Cái gì và Khi nào
Các ngôi sao giống như trong Hình minh họa 6.6 được thiết kế để phân tích kế toán. Họ 
giúp bạn dễ dàng trả lời các câu hỏi về giao dịch bao gồm ai, cái gì và khi nào
giật cơ. Ví dụ: một kế toán viên ở KLUB có thể hỏi: Doanh thu (thước đo) là bao nhiêu?

![ILLUSTRATION 6.6](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.6.png)