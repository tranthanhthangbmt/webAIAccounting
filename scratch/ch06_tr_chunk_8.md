6-44  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
MINH HỌA 6.62  Tạo cột và thước đo
Trường
Lịch
nhân viên
chọn
“Thêm lựa chọn”
Hàng hóa
Mua hàng
bán hàng
nhà cung cấp
Tìm kiếm
Khách hàng
Chọn bảng
1
Biện pháp mới
Cột mới
2
chọn
“Biện pháp mới” Hoặc
“Cột mới”
BƯỚC 3: Vùng để nhập công thức tạo cột hoặc thước đo mới sẽ 
xuất hiện (Minh họa 6.63).
MINH HỌA 6.63  Nhập công thức
Chèn
Tập tin
1
Mới
đo lường
nhanh chóng
đo lường
Định dạng
Cấu trúc
Thuộc tính
Tính toán
Trang chủ
Trợ giúp
Công cụ bảng
Dụng cụ đo
Xem
Làm người mẫu
Tên
Đo lường
Bàn nhà
Khách hàng
Định dạng $%
Tự động
$
%
000
Danh mục dữ liệu Chưa được phân loại
Đo =
Nhập công thức
3
4
Cách đi qua
CÁCH 6.1 
Tạo cột và thước đo được tính toán bằng Power BI
Các cột và số đo được tính toán là các khối xây dựng của các mô hình thông tin. Ở đây, chúng tôi 
minh họa cách chúng có thể được chỉ định bằng Power BI.
Những gì bạn cần: Dữ liệu   Tệp dữ liệu How To 6.1.
BƯỚC 1: Trong ngăn Trường, chọn bảng mà bạn muốn thêm cột hoặc thước đo vào. 
Trong Hình minh họa 6.62, bảng Khách hàng được chọn.
BƯỚC 2: Bên cạnh tên bảng, nhấp vào Tùy chọn khác và chọn Biện pháp mới hoặc Mới 
Cột.
Làm thế nào để
BƯỚC 4: Nhập công thức. Ví dụ: nhập công thức sau để tạo thước đo 
xác định số lượng khách hàng:
SỐ KHÁCH HÀNG = COUNT(Khách hàng[CustomerID]).
Sau đó, nhấn phím Enter.

![ILLUSTRATION 6.63](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.63.png)

Cách đi qua  6-45
CÁCH 6.2 
Triển khai tập hợp được lọc bằng SQL
Các mẫu được thảo luận trong chương này không dành riêng cho một phần mềm hoặc ngôn ngữ nào. Ở đây, bạn có thể 
thực hành triển khai tính năng tổng hợp đã lọc bằng phần mềm cơ sở dữ liệu quan hệ (ví dụ: Microsoft 
Access) bằng Ngôn ngữ truy vấn có cấu trúc (SQL).
Những gì bạn cần: Dữ liệu   Tệp dữ liệu How To 6.2.
BƯỚC 1: Mở file bằng Microsoft Access và chọn tab Create trong Main Menu. 
Bấm vào Thiết kế Truy vấn trong nhóm Truy vấn của dải băng.
BƯỚC 2: Khi một dải băng mới xuất hiện trong nhóm Kết quả, hãy chọn Chế độ xem SQL.
BƯỚC 3: Nhập lệnh SQL như trong Hình minh họa 6.64.
MINH HỌA 6.64  Truy vấn SQL để xác định tổng doanh thu được tạo từ việc bán hàng sang Hoa Kỳ 
Khách hàng theo danh mục sản phẩm
Truy vấn: Tổng doanh thu từ khách hàng Mỹ theo danh mục sản phẩm
CHỌN Danh mục, SUM([SellPrice] * [Số lượng bán]) AS [TotalrevenueFromUSCustomers]
TỪ Hàng hóa INNER JOIN (Khách hàng INNER THAM GIA Bán hàng TRÊN Customer.CustomerID = Sales.Customer) 
TRÊN Hàng hóa.BatchID = Bán hàng.Hàng hóa
Ở ĐÂU Quốc gia=“US”
NHÓM THEO Danh mục
Mã mô tả chi tiết
Mã
Mô tả
SUM([Giá bán] * [Số lượng đã bán])
Tính tổng doanh thu được tạo ra từ 
bán hàng.
Ở ĐÂU Quốc gia="US"
Bộ lọc được xác định thông qua biểu thức Boolean. 
Chỉ doanh số bán hàng từ khách hàng Mỹ mới được xem xét.
NHÓM THEO Danh mục
Tổng doanh thu được chia theo danh mục. 
Có ba giá trị cho CATEGORY: 
Điện tử, Sân vườn và Văn phòng.
TỪ Hàng hóa INNER JOIN (Khách hàng INNER JOIN 
Doanh số TRÊN Khách hàng.CustomerID = Doanh số.Khách hàng)  
TRÊN Hàng hóa.BatchID = Bán hàng.Hàng hóa
Xác định các kết nối giữa các bảng và do đó 
đường dẫn hướng.
BƯỚC 4: Chọn Dấu chấm than (!) trong nhóm Kết quả của dải băng. Bảng hiển thị 
trong Minh họa 6.65, tóm tắt doanh thu được tạo ra từ việc bán hàng cho khách hàng Hoa Kỳ bằng 
(sản phẩm) danh mục sẽ xuất hiện.
MINH HỌA 6.65  Kết quả truy vấn
Điện tử
Danh mục
Tổng doanh thu từ khách hàng Mỹ
34.553
80.012
210.560
Vườn
văn phòng
Dữ liệu   Thẻ Dữ liệu xuất hiện khi dữ liệu cần thiết để trả lời một câu hỏi hoặc hoàn thành một câu hỏi. 
bài tập có sẵn trên nền tảng học tập trực tuyến của Wiley.

![ILLUSTRATION 6.65](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.65.png)

6-46  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
Câu hỏi trắc nghiệm
1.  (LO 1)  Câu nào sau đây là sai?
Một.	 Các cột được tính toán là trung tâm của phân tích dữ liệu. Sau khi tính toán, chúng có thể được cắt thành nhiều phần 
cách trong quá trình khám phá dữ liệu.
b.	 Một hệ thống phân cấp độ đo có thể được xây dựng bằng cách áp dụng các toán tử số học cho các độ đo hiện có, chẳng hạn như 
như phân chia các biện pháp hiện có.
c.	 Cột được tính toán là một phần tích hợp của bảng.
d.	 Các cột và số đo được tính toán đều được thực hiện bằng thuật toán.
2.  (LO 1)  Mô hình hóa thông tin là quá trình
một.	 xác định mối quan hệ giữa các bảng và các ràng buộc áp dụng cho chúng.
b.	 tạo ra kiến ​​thức bổ sung từ dữ liệu có liên quan cho mục đích phân tích.
c.	 tạo các lược đồ ngôi sao và/hoặc bông tuyết.
d.	 tạo cấu trúc dữ liệu giúp phân tích dễ dàng.
3.  (LO 1)  Điều nào sau đây không mô tả một thuật toán kế toán?
Một.	 Tính chi phí khấu hao theo phương pháp đường thẳng.
b.	 Tạo biểu đồ đường hiển thị những thay đổi về tỷ suất lợi nhuận ròng của tổ chức trong 5 năm qua 
năm.
c.	 Xác định tỷ suất lợi nhuận ròng năm ngoái.
d.	 Tính toán số lượng chi phí chung cần được phân bổ cho các loại sản phẩm khác nhau.
4.  (LO 1)  Giả sử một cửa hàng tạp hóa ghi lại thông tin sau cho mỗi giao dịch.
1
2
3
4
5
1/2/2025
1/2/2025
2/2/2025
2/2/2025
3/2/2025
Y
N
N
Y
N
1,44
0
2,89
1,35
1
144,17
35,80
$289,09
134,88
99,50
$
$
$
$
Lòng Trung ThànhGiảm Giá
lòng trung thành
Số tiền
Ngày
ID giao dịch
Mô hình thông tin bao gồm ba thước đo và một cột được tính toán. Điều nào sau đây là 
cột được tính?
	 Một.	 Tính toán chiết khấu lòng trung thành. Thành viên của chương trình khách hàng thân thiết được giảm giá 1% cho tất cả 
giao dịch.
	 b.	 Tính toán % giao dịch từ các thành viên của chương trình khách hàng thân thiết.
	 c.	 Tính toán tổng số tiền được tạo ra vào một ngày cụ thể.
	 d.	 Tính tổng số tiền chiết khấu dành cho khách hàng thân thiết được thanh toán vào một ngày cụ thể.
5.  (LO 1)  Lược đồ hình sao biểu thị cấu trúc dữ liệu giúp xác định số nào cần chia nhỏ 
(sự thật) và làm thế nào (cái gì, ai, khi nào) để phân tích chúng (các khía cạnh). Tình huống nào sau đây 
không phù hợp với cấu trúc như vậy?
Kịch bản
Sự kiện
Kích thước
cái gì
Ai
Khi nào
một.
Tổng doanh thu
Danh mục sản phẩm
Khách hàng
Tháng
b.
Tổng doanh thu
Vùng
c.
Tổng lợi nhuận
Loại sản phẩm
Vùng
Ngày trong tuần
d.
Tổng số lượng khách hàng
Vùng
đ.
Tổng số lượng bán hàng
Danh mục sản phẩm
Khách hàng
f.
Tổng số lượng bán hàng
Tháng
g.
Tổng chi phí
Loại sản phẩm

6.  (LO 2)  Bạn không đồng ý với nhận định nào sau đây về thuật toán?
Một.	 Biểu thức Boolean là một phần không thể thiếu của các thuật toán phân loại.
b.	 Phân tích dựa trên dữ liệu từ nhiều bảng phụ thuộc rất nhiều vào các mối quan hệ được xác định chính xác 
giữa các bảng.
c.	 Hệ thống phân cấp thước đo xác định mối quan hệ giữa các thước đo từ hai bảng khác nhau.
d.	 TỔNG, TRUNG BÌNH và COUNT là các phép toán thường được sử dụng để xác định số đo.
7.  Khi áp dụng thuật toán phân loại sau cho tập dữ liệu, khách hàng nào trong số bốn khách hàng 
(CustomerID) được gán giá trị B?
Thuật toán
IF ((Tuổi < 30 VÀ Chương trình khách hàng thân thiết = “Có”) HOẶC (Doanh số > 10.000 VÀ Số vấn đề = 0))
SAU ĐÓ “A”
KHÁC “B”
Tập dữ liệu
1
2
3
4
ID khách hàng
Kinsun
Barbara
Jon
Gabriella
32
29
29
25
Có
Không
Có
Có
$
$
$
$
13,833
15.000
15.000
20.000
0
2
2
0
Tên
Chương trình trung thành theo độ tuổi
bán hàng
Số Vấn Đề
một.	 1
b.	 2
c.	 3
d.	 4
8.  (LO 2)  Phép tính nào sau đây không phải là phép tính văn bản trong bảng?
Một.	 Kết hợp hai trường văn bản, chẳng hạn như kết hợp tên John và họ Doe của khách hàng, 
kết quả là John Doe.
b.	 Thay thế một số ký tự trong trường văn bản, chẳng hạn như thay thế “str” bằng “đường phố” trong địa chỉ 
lĩnh vực.
c.	 Trích xuất chuỗi con cho trường văn bản. Ví dụ trích xuất mã vùng 302 từ điện thoại 
số 302-200-5731.
d.	 Đếm số lượng ô khác nhau trong một trường văn bản. Ví dụ: đếm các giá trị khác nhau 
trong lĩnh vực Quốc gia.
9.  (LO 2)  Khi áp dụng thuật toán sau cho tập dữ liệu, cách triển khai nào sau đây 
mẫu được sử dụng?
Thuật toán
LOẠI GIÁ =
NẾU Giá < 25.000 THÌ “HẤP DẪN” KHÁC
NẾU Giá >= 25.000 VÀ GIÁ < 50.000 THÌ “TẦM TRUNG” KHÁC
“CAO CẤP”
Tập dữ liệu
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
ID sản phẩm
Giá
Bọ cánh cứng VW
Honda Phi Công
BMW X7
Chevrolet Cru..
Mercedes ML
Ford Explorer
Honda Civic
Chevrolet Tah..
Jeep Wrangler
Maserati Leva..
2019
2018
2019
2019
2017
2019
2017
2016
2007
2020
$14,322
25.119
50.432
11.654
29.750
32,881
9,811
42.889
9.999
69.922
$
$
$
$
$
$
$
$
$
Mô tả
Năm
một.	 Tính toán số trong bảng
b.	 Tính toán văn bản trong bảng
c.	 Phân loại trong bảng
d.	 Tổng hợp được lọc
Câu hỏi trắc nghiệm  6-47

6-48  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
10.  (LO 2)  Phát biểu nào sau đây về các mẫu mã hóa là không chính xác?
Một.	 Các tỷ lệ thường được thực hiện dưới dạng hệ thống phân cấp thước đo.
b.	 Các phép tính trên nhiều bảng dựa chủ yếu vào việc khớp các giá trị khóa chính và khóa ngoài.
c.	 Tập hợp (số đo) một cột tạo ra một giá trị số ít.
d.	 Thông thường, cùng một công thức kết hợp các phép tính số và văn bản.
11.  (LO 3)  Có bao nhiêu mẫu phù hợp nhất với loại bảng nào?
Một.	 Các bảng sự thật.
b.	 Các bảng kích thước.
c.	 Bảng thực tế và kích thước.
d.	 Không phải bảng thực tế cũng như bảng thứ nguyên.
12.  (LO 3)  Phát biểu nào sau đây về mô hình hóa các chiều là không chính xác? 
Một.	 Mô hình hóa thứ nguyên nhằm mục đích tạo ra các cấu trúc dữ liệu giúp phân tích dữ liệu dễ dàng hơn.
b.	 Kích thước có thể được sử dụng cho mục đích lọc.
c.	 Các cột được tính toán có thể hoạt động như các thứ nguyên.
d.	 Có bao nhiêu thước đo chỉ có thể được chỉ định cho các bảng kích thước.
13.  (LO 3)  Sơ đồ là một phần của lược đồ hình sao mô tả quy trình sản xuất.
Bảng sự kiện
N
1
Bảng kích thước
Đã hoàn thành Tốt
Sản xuất
Bạn mô tả bản chất của mối quan hệ giữa sản xuất và thành phẩm như thế nào? 
Một.	 Một mối quan hệ tham gia.
b.	 Một mối quan hệ xảy ra.
c.	 Mối quan hệ dòng chảy dẫn đến sự sụt giảm hoặc dòng chảy của hàng hóa thành phẩm. 
d.	 Một mối quan hệ dòng chảy dẫn đến sự gia tăng hoặc dòng hàng hóa thành phẩm. 
14.  (LO 3)  Câu hỏi nào sau đây không dựa vào mối quan hệ tham gia?
Một.	 Nhà cung cấp nào đưa ra mức giá thấp nhất cho một sản phẩm cụ thể?
b.	 Tổng số đơn vị bán được cho mỗi loại sản phẩm là bao nhiêu?
c.	 Với mỗi loại sản phẩm, khách hàng mua số lượng nhiều nhất trong năm qua là ai?
d.	 Nhân viên nào có tỷ lệ hoàn vốn kém nhất?
15.  (LO 3)  Câu hỏi nào sau đây không dựa vào mối quan hệ dòng chảy?
Một.	 John, một nhân viên kế toán, đã thực hiện bao nhiêu khoản thanh toán trong tháng 1?
b.	 Chúng ta đã sản xuất được bao nhiêu đơn vị trong tháng 1?
c.	 Bao nhiêu tiền đã được gửi vào tài khoản ngân hàng Fulton vào tháng 1?
d.	 Khách hàng nào mua nhiều sản phẩm điện tử nhất?
16.  (LO 3)  Ai-cái gì-khi các ngôi sao được kết nối thông qua
một.	 giao dịch (ví dụ: bán hàng).
b.	 nguồn lực (ví dụ: thành phẩm).
c.	 đại lý nội bộ (ví dụ: nhân viên).
d.	 đại lý bên ngoài (ví dụ: khách hàng).

17.  (LO 3)  Biểu đồ cột này được tạo bởi một nhà sản xuất ô tô.
2.000.000 USD
2.500.000 USD
2.001.001 USD
$998,177
$567,112
1.500.000 USD
1.000.000 USD
500.000 USD
$0
xe sedan
SUV
Danh mục
bán hàng
Thể thao
Mô tả nào chính xác nhất về thông tin kế toán được ghi lại trong biểu đồ này?
Một.	 Doanh thu trung bình được tạo ra theo danh mục.
b.	 Tổng doanh thu được tạo ra.
c.	 Mỗi danh mục đã tạo ra bao nhiêu doanh thu (dòng vào).
d.	 Mỗi danh mục đã tạo ra bao nhiêu doanh thu (dòng chi).
18.  (LO 3)  Phân tích nào sau đây không thể được khám phá bằng mô hình thông tin này?
ID nhân viên
SốNhân Viên
nhân viên
ID khách hàng
Tuổi
Thành phố
Quốc gia
Tên
Giới tính
Tiêu đề
Vùng
Số Lượng Khách Hàng
Khách hàng
Bảng kích thước
Bảng sự kiện
Bảng kích thước
ID sản phẩm
Danh mục
SốSản Phẩm
sản phẩm
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
Ngày đặt hàng
sản phẩm
Khách hàng
nhân viên
Đặt hàng
Giá
số lượng
Số tiền
Tổng số tiền
Tổng số lượng
Đặt hàng
ID dòng đơn hàng
Chìa khóa
Cột
Cột được tính toán
Đo lường
Khóa ngoại
Tên
Chức danh công việc
Giới tính
một.	 Số lượng sản phẩm khác nhau đặt hàng theo khu vực.
b.	 Tổng số lượng khách hàng nữ đặt hàng từ nhân viên nữ.
c.	 Thay đổi hàng tháng về số lượng đặt hàng.
d.	 Sự đóng góp tương đối của từng khu vực vào tổng số lượng đặt hàng.
đ.	 Ba khách hàng hàng đầu ở mỗi tiểu bang dựa trên số tiền đặt hàng.
Câu hỏi trắc nghiệm  6-49