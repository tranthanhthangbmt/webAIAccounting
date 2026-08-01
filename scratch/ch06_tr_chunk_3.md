6-14  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
MINH HỌA 6.17  Nguyên tắc Một thước đo, Nhiều phân tích
Frazier, Theodore
Morris, Bonnie
Moncrief, Richard
Fisher, Rebecca
Thì là, Mary
Hải ly, Daniel
Vaughn, Anthony
Zebrowski, Connie
Uren, Harold
Người mới, Annie
Deaton, Andrew
Henderson, Teresa
Engel, Dexter
Nevius, Scott
Đen, Candice
Flynn, Casey
27.500 USD
$11,573
11.400 USD
$11,145
$10,975
10.200 USD
$9,960
$9,565
$9,385
8.750 USD
$8,515
$7,785
$6,825
$6,090
$5,884
5.700 USD
Tên
Tổng cộng
Doanh thu
Tổng doanh thu
Cắt theo: Khách hàng,
Trạng thái và (Sản phẩm)
Danh mục
Doanh thu
BẬT
BC
AB
CA
FL
Kiểm soát chất lượng
NY
TX
PA
GA
NJ
WI
MA
MS
MI
SK
CA
CA
CA
Hoa Kỳ
Hoa Kỳ
CA
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
CA
Tổng doanh thu
$621,633
$132,867
58.258
57.254
41.466
39.572
33,404
18.049
17.959
16.999
13.647
12.218
11.941
11.358
11.305
9,891
8,665
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
tiểu bang
Quốc gia
Doanh thu
văn phòng
Vườn
Điện tử
$431,308
132.300 USD
58.025
$
Danh mục
Doanh thu
ÁP DỤNG TƯ duy phản biện 6.2: Đánh giá thuật toán
Việc thực hiện một thuật toán (hoặc viết một chương trình) không phải là một môn khoa học chính xác. Thường có nhiều 
giải pháp phù hợp nhưng cũng có một số giải pháp chưa tốt. Tiêu chí quan trọng nhất của một chương trình tốt 
là đầu ra là chính xác. Nhưng nó cũng phải nhanh và điều này đặc biệt đúng với các tập dữ liệu lớn. 
Một thuật toán nên sử dụng ít bộ nhớ nhất có thể và có thể đọc được. (Các lựa chọn thay thế).
MINH HỌA 6.16  Đơn-
Đo lường tổng hợp để tạo 
Tổng số lượng đã bán, Tổng doanh thu, 
và Số lượng khách hàng 
Biện pháp
Bảng: Doanh thu
Đo lường
Thuật toán
Tổng số lượng đã bán
SUM(Số lượng đã bán)
Bảng: Doanh thu
Đo lường
Thuật toán
Tổngdoanh thu
SUM(Doanh thu)
Bảng: Khách hàng
Đo lường
Thuật toán
Số Lượng Khách Hàng
COUNT(ID khách hàng)
Các biện pháp này tính toán các tập hợp có thể được cắt theo nhiều cách. Báo cáo ở 
Hình minh họa 6.17 là một ví dụ về nguyên tắc một thước đo, nhiều phân tích này. 
Nó chia nhỏ doanh thu theo khách hàng, tiểu bang và danh mục sản phẩm. Còn nhiều nữa 
các loại phân tích có thể được thực hiện với TotalRevenue, bao gồm cả phân tích theo 
Trường AgeCategory mà chúng tôi đã tính toán (là một phân loại).
Hình minh họa 6.16 liệt kê ba thước đo này và thuật toán của chúng.

![ILLUSTRATION 6.17](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.17.png)

6.2  Những mẫu nào triển khai thuật toán mô hình hóa thông tin?   6-15
Mẫu mô hình thông tin 6: Đã lọc 
Tổng hợp
Thường cần phải phân tích tổng hợp dựa trên các tập dữ liệu đã được lọc. Một ví dụ là phân tích 
tổng doanh thu được tạo ra từ việc bán hàng cho khách hàng Hoa Kỳ. Có nhiều cách khác nhau để thực hiện 
tập hợp được lọc. Phương pháp này thường phụ thuộc vào phần mềm đang được sử dụng.
• Trong Excel, sử dụng các hàm SUMIF, COUNTIF, AVERAGEIF, v.v..
• Trong SQL, sử dụng mệnh đề WHERE ( Data How To 6.2 trình bày cách triển khai một 
tổng hợp được lọc bằng SQL).
• Trong Power BI, tạo bộ lọc trong khung Bộ lọc hoặc sử dụng chức năng TÍNH TOÁN.
Hình minh họa 6.18 (A) là một ví dụ về tập hợp được lọc để xác định tổng 
doanh thu do KLUB tạo ra từ việc bán hàng cho khách hàng Hoa Kỳ. Hình minh họa 6.18 (B) tái tạo lại 
báo cáo từ Hình minh họa 6.17 sử dụng thước đo tổng doanh thu từ khách hàng Hoa Kỳ.
Mẫu mô hình thông tin 7: Đo lường 
Hệ thống phân cấp
Hệ thống phân cấp thước đo được sử dụng khi một thước đo mới, phức tạp hơn được tạo bằng cách sử dụng 
biện pháp. Trong thực tế, những vấn đề phức tạp đôi khi có thể được giải quyết bằng cách chia vấn đề thành 
các vấn đề nhỏ hơn, sau đó kết hợp các giải pháp khác nhau. Đặc biệt là hệ thống phân cấp đo lường 
hữu ích khi tính toán tỷ lệ và điểm chuẩn.
Bảng: Doanh thu
Đo lường
Thuật toán
Tổngdoanh thuTừUSKhách hàng
SUM(Doanh thu.Doanh thu)
WHERE Customer.Country = “US”
MINH HỌA 6.18  Tổng hợp được lọc để tính tổng doanh thu từ khách hàng Hoa Kỳ
(A)
Adams, Ramón
Alfonso, Henry
Cung thủ, Greg
Armstrong, Rita
Arnold, Charles
thợ làm bánh, Nancy
Bóng, Martha
Ngân hàng, Ingrid
Barnhart, Richard
Dơi, Andrea
Hải ly, Daniel
Bentley, nghiêm túc
Bernard, Caleb
Blocher, Harold
Bloss, John
1.160
4.965
2.150
300
710
1.030
320
1.465
885
1.680
10.200 USD
1.750
1,418
990
828
$
$
$
$
$
$
$
$
$
$
$
$
$
$
Tên
Tổng doanh thu
Từ khách hàng Mỹ
Tổng doanh thu
Từ khách hàng Mỹ
Cắt theo: Khách hàng,
Trạng thái và (Sản phẩm)
Danh mục
Tổng doanh thu
Từ Mỹ
Khách hàng
AK
AL
AR
AZ
CA
CO
CT
DC
DE
FL
GA
xin chào
ID
IL
TRONG
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Tổng doanh thu
Từ khách hàng Mỹ
$325,125
5.148
750
6.310
4.050
41.466
2.160
980
6.023
4.550
$39,572
13.647
113
1.520
4.715
5.217
$
$
$
$
$
$
$
$
$
$
$
$
$
$
tiểu bang
Quốc gia
Điện tử
Vườn
văn phòng
34.553
80.012
$
$
$ 210,560
Danh mục
Tổng doanh thu
Từ Mỹ
Khách hàng
Tổng doanh thu
Từ Mỹ
Khách hàng
(B)

![ILLUSTRATION 6.18](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.18.png)

6-16  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
2Thước đo TotalRevenueFromUSCustomers giống với thước đo trong Hình minh họa 6.18.
Sau khi tạo NumberOfCustomers, TotalQuantitySold, TotalRevenue, TotalRevenue
FromUSCustomers, TotalRevenueFromCanadianCustomers và Canadian/USRevenueRatio 
biện pháp, mô hình thông tin của KLUB ngày càng phát triển (Minh họa 6.20). Hãy nhớ rằng, càng giàu có 
mô hình thông tin của bạn càng phong phú thì phân tích của bạn sẽ càng phong phú!
Hình minh họa 6.19 (A) trực quan hóa hệ thống phân cấp thước đo. Biện pháp đầu tiên, TotalRevenue-
FromCanadianCustomers, xác định tổng doanh thu do khách hàng của KLUB tạo ra trong 
Canada. Thước đo thứ hai, TotlRevenueFromUSCustomers, xác định tổng doanh thu 
được tạo ra bởi khách hàng Hoa Kỳ của KLUB. Biện pháp thứ ba sử dụng lại hai biện pháp đầu tiên để tính toán 
một tỷ lệ so sánh doanh thu của Canada với doanh thu của Hoa Kỳ, sử dụng doanh thu của Hoa Kỳ làm chuẩn.
Hình minh họa 6.19 (B) cho thấy khả năng triển khai hệ thống phân cấp khung nhìn. Dấu gạch chéo 
biểu tượng tượng trưng cho sự phân chia. Cuối cùng, Minh họa 6.19 (C) cho thấy một cách sử dụng Canada/
Đo lường tỷ lệ doanh thu của Hoa Kỳ. Đường màu đỏ là tỷ lệ có giá trị 1, biểu thị mức đóng góp bằng nhau 
vào doanh thu của cả hai nước. Với phân tích này, ban quản lý tại KLUB có thể thấy được điều đó 
Canada tạo ra nhiều doanh thu hơn một chút cho các sản phẩm văn phòng, phần lớn doanh thu cho Electron-
Các sản phẩm ics và Garden được sản xuất tại Hoa Kỳ.
MINH HỌA 6.19  Đo lường thứ bậc của người Canada/Hoa Kỳ Tỷ lệ doanh thu: Trực quan hóa và triển khai2
người Canada/
Tỷ lệ doanh thu của Hoa Kỳ
Đo lường thứ bậc
Tổngdoanh thu
TừUSKhách hàng
Tổngdoanh thu
TừKhách hàng Canada
(A)
Đo lường hệ thống phân cấp để tính toán thước đo tỷ lệ doanh thu của Canada/US
Bảng: Doanh thu
Biện pháp
Thuật toán
Tổngdoanh thuTừKhách hàng Canada
SUM(Doanh thu)
WHERE Customer.Country = “CA”
Tổngdoanh thuTừUSKhách hàng
SUM(Doanh thu)
WHERE Customer.Country = “US”
Tỷ lệ doanh thu Canada/Mỹ
Tổngdoanh thuFromCanadianCustomers / TotalRevenueFromUSCustomers
(B)
1,05
0,68
0,65
văn phòng
Điện tử
Danh mục
Vườn
0,0
0,2
0,4
Canada/Mỹ
Tỷ lệ doanh thu
So sánh tỷ lệ doanh thu
theo danh mục
0,6
0,8
1.0
1.2
(C)

![ILLUSTRATION 6.20](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.20.png)

6.2 Những mẫu nào triển khai các thuật toán mô hình hóa thông tin?  6-17
 MINH HỌA 6.20 Mô hình thông tin của KLUB được mở rộng bằng các biện pháp 
ID nhân viên
Email
Tên đầu tiên
Giới tính
Họ
Ssn
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
Vùng
Số lượng khách hàng
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
bán hàng
BánGiá
Số lượng đã bán
giá vốn
Doanh thu
bán hàng
ID dòng hóa đơn
Khách hàng
Ngày
Hàng hóa
nhân viên
Chìa khóa
Cột
Cột được tính toán
Đo lường
Khóa ngoại
Tỷ lệ doanh thu Canada/Mỹ
Tổng số lượng đã bán
Tổngdoanh thu
Tổngdoanh thuTừUSKhách hàng
Tổngdoanh thuTừKhách hàng Canada
Các biện pháp bổ sung vào
Mô hình thông tin
 Áp dụng nó 6.2 
 Sử dụng thuật toán 
để tính mạng 
Doanh thu 
Kế toán tài chính
Người chủ cửa hàng bán lẻ hành lý ở nước ngoài cung cấp cho bạn mô hình dữ liệu sau, 
trong đó hiển thị dữ liệu liên quan đến bán hàng mà Nước ngoài thu thập. Mỗi hàng trong bảng Bán hàng đại diện cho một 
dòng hoá đơn.
ID khách hàng
Tên
Mức độ trung thành
Khách hàng
ID sản phẩm
Danh mục sản phẩm
Mã khuyến mãi
Khuyến MãiGiảm Giá
sản phẩm
1
1
N
N
Khách hàng
sản phẩm
bán hàng
Giá
số lượng
bán hàng
Hóa đơnDòngSố
Chìa khóa
Cột
Khóa ngoại
 Một số sản phẩm có mã khuyến mãi và giảm giá khuyến mãi. Đối với sản phẩm không có khuyến mãi 
mã, mức giảm giá là 0. Ở nước ngoài có ba cấp độ trung thành: Cá, Đại bàng và Sư tử. Các khoản giảm giá được trao cho 
mỗi mức độ trung thành được hiển thị trong bảng.

![Apply It 6.2](../TaiLieu/textbookForPractice/Figures/Ch_06/Apply%20It%206.2.png)

6-18  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
6.3  Mô hình nào giúp phát triển và 
Thực hiện thông tin kế toán 
Người mẫu?
MỤC TIÊU HỌC TẬP ➌
Phát triển và triển khai các mô hình thông tin cho các cấu trúc dữ liệu kế toán chung.
Trước đó trong khóa học, bạn đã biết tầm quan trọng của việc áp dụng mô hình thứ nguyên cho 
dữ liệu kế toán. Việc tổ chức dữ liệu hợp lý theo những cách cụ thể giúp việc phân tích dễ dàng hơn. Thông tin-
mô hình hóa hoặc xác định và thực hiện các biện pháp và kích thước cũng được hưởng lợi từ 
có cấu trúc tương tự tại chỗ. Phần trước đề cập đến bảy mẫu phổ biến cho 
thực hiện các cột và số đo đã tính toán. Ở đây, chúng tôi trình bày thêm sáu mẫu giúp 
xác định các biện pháp để phân tích đặc điểm ai, cái gì và khi nào của các giao dịch kế toán.
cá
đại bàng
sư tử
0
3
5
Cấp độ
Giảm giá
Chủ sở hữu ở nước ngoài yêu cầu bạn tính tổng doanh thu thuần được tạo ra cho đến nay. Khi tính toán 
tổng doanh thu thuần, hãy nhớ xem xét cả chiết khấu dành cho khách hàng thân thiết và khuyến mãi. Giả sử rằng cả hai 
giảm giá được ghi lại dưới dạng phần trăm, ví dụ: 5%. Đối với mỗi điều sau đây, hãy chỉ ra (những) mẫu nào 
bạn đã áp dụng, sau đó hiển thị thuật toán của bạn.
1. Giảm giá lòng trung thành
2. Doanh thu thuần
3. Tổng doanh thu thuần
GIẢI PHÁP
1. Mẫu 2.
Thuật toán (cột tính toán): LoyaltyDiscount =
NẾU Cấp = “Cá” THÌ 0, ELSE
NẾU Cấp độ = “Đại bàng” THÌ 3, KHÁC 5
2. Mẫu 3 và Mẫu 4.
Thuật toán (cột tính toán): NetRevenue =
NẾU Khách hàng.LoyaltyDiscount > 0 và Product.PromotionDiscount > 0
SAU ĐÓ
Doanh số.Giá × Doanh số.Số lượng × (1 − ((Customer.LoyaltyDiscount / 100) + (Product.
Khuyến mãiGiảm giá/100)))
KHÁC
NẾU Customer.LoyaltyDiscount = 0 và Product.PromotionDiscount > 0
SAU ĐÓ Doanh số.Giá × Doanh số.Số lượng × (1 − Sản phẩm.Khuyến mãiGiảm giá/100)
KHÁC
NẾU Khách hàng.LoyaltyDiscount > 0 và Product.PromotionDiscount = 0
SAU ĐÓ Doanh số.Giá × Doanh số.Số lượng × (1 − Khách hàng.Giảm giá trung thành/100)
ELSE Doanh số.Giá × Doanh số.Số lượng
3. Mẫu 5. 
Thuật toán (đo lường): Tổng doanh thu ròng = SUM(Số tiền)

6.3 Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán? 6-19
 MINH HỌA 6.21 Có Bao Nhiêu Mẫu 
bán hàng
Khách hàng
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
babyliss
Heimvision
Terzani
Herman Miller
Uline
Cổng trước
CrafsMan
cối xay búa
Người bán hàng
Westcott
BLP
SAR
JFL
HMO
UOD
FRGH
CRAS
HAMC
LƯU Ý
WSC
chuyên nghiệp
Bình minh 14X
2090 chuyên nghiệp
Vũ trụ lưng cao
400 Điều Chỉnh
Phí bảo hiểm 50
4920
Hộp đựng 5 ram
Bìa cứng
cái kéo
Điện tử
Điện tử
Điện tử
văn phòng
văn phòng
Vườn
Vườn
văn phòng
văn phòng
văn phòng
Máy Sấy Tóc
Đồng hồ báo thức
Đèn sàn
Bàn Văn Phòng
Ghế văn phòng
Nhà Vườn
Máy rải
Giấy
Sổ tay
Công cụ văn phòng
Mô tả
Loại
Mã
Danh mục
Thương hiệu
ID lô
Chung
KLUB
Hàng hóa
Bảng
Tài nguyên
Giao dịch
đại lý
Có bao nhiêu hàng
trong bảng?
Có bao nhiêu lô?
Hàng hóa
bán hàng
Khách hàng
 Trong ví dụ về KLUB, chúng ta có thể tạo số đo “có bao nhiêu” cho: 
• Nguồn lực: Hàng hóa. 
• Giao dịch: Mua bán. 
• Đại lý: Khách hàng, nhà cung cấp và nhân viên. 
 Mô hình thông tin
 Những biện pháp này có thể được chia nhỏ hơn nữa. Sử dụng tập dữ liệu KLUB, chúng ta có thể khám phá các câu hỏi-
như sau bằng cách áp dụng các biện pháp này cho các giao dịch, ai và bảng nào:
• Giao dịch: Có bao nhiêu lần bán hàng và bao nhiêu lần mua hàng? 
• Đại lý (Ai): KLUB có bao nhiêu khách hàng, bao nhiêu nhân viên và bằng cách nào 
họ làm việc với nhiều nhà cung cấp? Cũng có thể đi sâu hơn để tìm ra cách 
nhiều khách hàng hoặc nhà cung cấp mà KLUB có ở mỗi quốc gia, mỗi tiểu bang hoặc mỗi tỉnh. 
• Tài nguyên (Cái gì): KLUB có bao nhiêu sản phẩm? Khi đó có thể tìm thấy 
số lượng sản phẩm theo nhãn hiệu, theo loại sản phẩm và theo danh mục sản phẩm. 
 Khi trả lời các câu hỏi về tác nhân và nguồn lực, chúng ta có thể phân tích mối quan hệ giữa 
các thứ nguyên trong cùng một bảng, chẳng hạn như số lượng khách hàng của một tiểu bang hoặc tỉnh, hoặc 
số loại sản phẩm cho mỗi loại.  Hình minh họa 6.22 cho thấy một số kích thước trong 
Bảng hàng hóa có liên quan. Hãy nhớ các số lượng N-1 cho mối quan hệ giữa 
ID lô và nhãn hiệu:
• 1: Một nhãn hiệu được chỉ định cho một lô. 
• N: Có thể có nhiều lô cùng nhãn hiệu. 
Mẫu mô hình hóa thông tin 8: Bao nhiêu
 Các bảng thường mô tả các khái niệm như khách hàng, nhà cung cấp, doanh số bán hàng và sản phẩm. Cái vỗ nhẹ tiếp theo-
tern tạo ra thước đo đếm số hàng hoặc số thể hiện của một khái niệm trong một 
cái bàn. Mẫu này có thể đếm tài nguyên, giao dịch và tác nhân, nghĩa là nó có thể được sử dụng 
cho cả bảng thực tế (giao dịch) và bảng thứ nguyên (tài nguyên và tác nhân). 
 Ví dụ minh họa 6.21 xác định số hàng trong Hàng hóa 
bảng hiển thị số lượng lô KLUB đã mua.

![ILLUSTRATION 6.22](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.22.png)