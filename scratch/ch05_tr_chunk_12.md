5-70  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
EX 5.3  (LO 1, 2, 3, 4, 5, 7)  Dữ liệu   Kế toán tài chính   Trích xuất, chuyển cột và bảng-
hình thành Là kế toán cho El Azteco, một nhà hàng ở Knoxville, TN, bạn được yêu cầu chuẩn bị 
dữ liệu để phân tích doanh số bán hàng của nhà hàng. Từ điển dữ liệu chi tiết dữ liệu được ghi lại cho mỗi lần bán hàng 
giao dịch.
Tên
Mô tả
ID
Một số xác định duy nhất việc bán hàng.
Ngày bán hàng
Ngày việc bán hàng xảy ra.
Số tiền
Số tiền mà khách hàng nợ trước khi giảm giá và phiếu giảm giá.
Giảm giá
Phần trăm chiết khấu dành cho khách hàng.
Lòng Trung ThànhGiảm Giá
Phần trăm chiết khấu dành cho khách hàng thân thiết được trao cho khách hàng.
Số trung thành 
Một con số duy nhất được trao cho khách hàng thân thiết. Chỉ có khách hàng 
đã đăng ký chương trình khách hàng thân thiết của El Azteco có thể được giảm giá cho khách hàng thân thiết.
Tất cả dữ liệu được ghi lại cho đến nay sẽ được cung cấp cho bạn dưới dạng tệp CSV. Dữ liệu cũng được hiển thị ở đây. Chú ý rằng hiện tại, 
tất cả dữ liệu được lưu trữ trong một cột. Hơn nữa, Fernando, chủ sở hữu của El Azteco, cho bạn biết rằng mức trung bình 
số tiền bán hàng cho đến nay là $ 212,1.
Thông Tin Bán Hàng 
1,1/6/2025,97,0,0
2,1/6/2025,113,2,3,49
3,1/6/2025,55,0,1,23
4,1/7/2025,423,2,0
5,1/7/2025,88,0,0
6,1/7/2025,250,3,5,53
7,1/8/2025,680,2,0
8,1/8/2025,58,0,0
9,1/8/2025,99,1,1
10,1/8/2025,258,2,0
A
Ví dụ về các câu hỏi bạn cần trả lời bằng cách sử dụng dữ liệu này bao gồm:
•  Số tiền thực tế phải trả cho mỗi lần bán là bao nhiêu?
•  Mức giảm giá trung bình cho mỗi lần bán là bao nhiêu?
•  Tổng mức chiết khấu dành cho khách hàng thân thiết là bao nhiêu?
Áp dụng các mẫu chuẩn bị dữ liệu cần thiết để chuẩn bị cơ sở dữ liệu phân tích giúp dễ dàng 
trả lời những câu hỏi này. Hãy đảm bảo xem xét các mô hình giúp phát hiện và khắc phục những điều không phù hợp.
dữ liệu liên tục và không hợp lệ. 
EX 5.4  (LO 4, 5, 7)  Kế toán quản trị   Áp dụng Nguyên tắc mô hình hóa theo chiều MEQ là 
một nhà sản xuất thiết bị y tế bán sản phẩm của họ ở Mỹ, Canada và một số nước châu Âu 
các nước. Tất cả việc bán hàng được thực hiện bởi nhân viên bán hàng. Với tư cách là kế toán viên của MEQ, bạn được yêu cầu thực hiện một công việc 
phân tích doanh số bán hàng của thực thể bạn bởi nhân viên bán hàng. Bạn sẽ tính toán các chỉ số hiệu suất chính (KPI) cho 
mỗi nhân viên bán hàng như một phần của đánh giá hiệu suất hàng năm của họ. Hiện tại, tất cả thông tin được lưu trữ trong một 
một bảng duy nhất (được đặt tên là Bán hàng) trong cơ sở dữ liệu quan hệ. Từ điển dữ liệu được đưa ra ở đây.
Tên
Mô tả
Địa chỉ
Địa chỉ của khách hàng.
Danh mục
Danh mục của một mặt hàng.
Mã C
Một mã nhận dạng duy nhất một khách hàng.
Tên C
Tên của khách hàng.
Ngày
Ngày bán hàng xảy ra.
Mô tả
Tên của một mặt hàng. 
DOH
Ngày một nhân viên bán hàng được thuê.
(Tiếp theo)

Bài tập  5-71
Tên
Mô tả
Id hóa đơn
ID xác định duy nhất một lần bán hàng.
Mã hàng
Mã xác định duy nhất một mặt hàng hoặc sản phẩm.
LiId
Một ID duy nhất được cấp cho mỗi mục hàng. Một đợt giảm giá có thể có nhiều dòng 
các mặt hàng. Một chi tiết đơn hàng chỉ định ID và mô tả của một mặt hàng, số lượng 
được bán và giá yêu cầu trên mỗi đơn vị.
Điều khoản thanh toán
Các điều khoản thanh toán áp dụng cho khách hàng.
Giá
Giá thanh toán cho một chi tiết đơn hàng như một phần của giao dịch bán hàng.
số lượng
Số lượng đã bán của một mục hàng như một phần của đợt giảm giá.
QOH
Số lượng hiện tại có sẵn cho một sản phẩm.
Vùng
Các khu vực khác nhau mà nhân viên bán hàng hoạt động. Mỗi vùng đều 
được giao cho đúng một nhân viên bán hàng.
Mã SP
Một mã xác định duy nhất một nhân viên bán hàng.
Tên Sp
Tên của người bán hàng.
	 1. Áp dụng nguyên tắc mô hình hóa thứ nguyên cho bảng Sales bằng cách tạo ngôi sao hoặc bông tuyết 
lược đồ. 
	 2. Liệt kê các mẫu bạn sẽ sử dụng để phát hiện và khắc phục các vấn đề về dữ liệu, đồng thời giải thích lý do bạn sử dụng 
từng mẫu. 
EX 5.5  (LO 6)  Dữ liệu   Kiểm tra   Kết hợp các bảng và xác định dữ liệu không hợp lệ Giả sử bạn là một 
nhà phân tích tài chính làm việc trong nhóm kiểm soát viên tại một công ty đại chúng. Bạn được yêu cầu chuẩn bị một 
cơ sở dữ liệu phân tích hiển thị tài sản cố định hợp nhất cho tổ chức của bạn. Cơ sở dữ liệu phân tích này 
sẽ được kiểm toán viên sử dụng để xác minh chi phí khấu hao và bởi người kiểm soát của bạn khi chúng được ghi nhận trước
so sánh các chú thích cuối trang của báo cáo tài chính. Công ty của bạn có địa điểm ở Hoa Kỳ và Mexico. 
Nhóm công nghệ của mỗi địa điểm đã cung cấp cho bạn một tệp dữ liệu chứa dữ liệu về tài sản cố định và 
khấu hao. Áp dụng các mẫu chuẩn bị dữ liệu thích hợp vào các tệp dữ liệu để tạo ra một báo cáo phân tích 
cơ sở dữ liệu giúp xác minh chi phí khấu hao năm 2025 và chi phí khấu hao lũy kế. 
Bạn có thể cho rằng tất cả dữ liệu đã được truyền chính xác.
EX 5.6  (LO 4)  Dữ liệu   Sử dụng các mẫu để phát hiện và khắc phục các vấn đề về dữ liệu Dunn Motors là một hãng Honda 
Đại lý tại Tallahassee, Fl. Họ giữ một danh sách tất cả các loại xe có sẵn cho nhân viên bán hàng trong chiếc xe đã qua sử dụng của họ 
khoa. Sau đây là mẫu danh sách và từ điển dữ liệu của bảng. 
3044
3045
3046
3047
3048
3049
3050
3051
3052
3053
12350
16990
9766
10889
22998
11150
24551
12990
17000
13500
ID
Accord-Đen-2017-*13,14,15*
Odyssey-White-2020-*4,7,11,12,17,*
Ridgeline-Đen-2012-*1,13*
Pilot-Trắng-2016-*7*
Accord-Đen-2018-*12,14,17*
CRV-Trắng-2019-*11,22,27*
Accord-Green-2012-*4,7*
Civic-Trắng-2015-*4,5,6*
Pilot-Red-2018-*1,7,11,18*
Civic-Gray-2017-*2,6,9,20*
Mã sản phẩm
Giá
Tên
Mô tả
ID
ID duy nhất của một chiếc ô tô.
Mã sản phẩm
Mã ô tô chứa các thông tin sau: mẫu xe, màu sắc, năm và danh sách 
các tính năng bổ sung (giữa **). Mỗi tính năng có mã nội bộ từ 1 đến 30.
Giá
Giá xe (trước khi thương lượng).
	 1. Mô tả các vấn đề về dữ liệu của bảng. 
	 2. Giải quyết những vấn đề này bằng cách chuyển đổi bảng.

5-72  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
EX 5.7  (LO 2, 5, 6)  Dữ liệu   Kế toán tài chính   Chuẩn bị dữ liệu để phân tích tài chính Hikko là một 
công ty công nghệ có trụ sở tại California với doanh số bán hàng ở ba khu vực: Mỹ, Châu Âu và Châu Á. Nó xuất bản-
đưa ra báo cáo sau đây về doanh thu hàng quý của mình. 
Khu vực 2022:Q1
2022:Q2 2022:Q3 2022:Q4 2023:Q1 2023:Q2 2023:Q3 2023:Q4 2024:Q1 2024:Q2 2024:Q3
2024:Q4
Hoa Kỳ
77.265.889
57.176.758
57.748.525 78.811.207 97.265.889 71.976.758 80.613.969 94.347.912 107.467.822 78.451.510 89.434.721
102.094.431
CHÂU ÂU
53.761.998
47,848,178
51.197.551 53.224.378 65.534.311 58.325.537 67.074.367 67.500.340
73.666.129 54.512.935 54.512.935
72.929.468
CHÂU Á
32,188,799
27.038.591
31.094.380 32.832.575 31.777.112 23.197.292 23.661.238 32.094.883
29.778.112 22.035.803
24.239.383
28,289,206
Bạn muốn so sánh doanh thu của Hikko giữa các khu vực, quý và năm. Bạn sẽ tổ chức lại như thế nào-
thu thập dữ liệu để thực hiện việc phân tích đó dễ dàng? 
EX 5.8  (LO 1, 4, 5, 6)  Dữ liệu   Kế toán quản lý   Chuẩn bị dữ liệu để phân tích chi phí Wilkinson, 
một người xây nhà sang trọng ở miền nam Nevada, sử dụng thẻ thời gian làm việc để theo dõi chi phí lao động cho các công việc khác nhau của mình. 
tài sản. Họ tạo ra các báo cáo hàng tuần. Các mẫu báo cáo tuần 1 và tuần 2 năm 2025 được hiển thị tại đây. 
3405
3406
3407
3408
1
1
13
25
1
1
1
1
ID
ERF007
ERF008
ERF007
IR68
Công việc của nhân viênKhông
WilkinsonTuần1
WilkinsonTuần 2
TuầnKhông
4
4
4
8
4
Thứ năm:
2/1/2025
8
8
8
Thứ Sáu:
3/1/2025
4
8
0
thứ bảy:
4/1/2025
4608
4609
4610
4611
25
13
13
1
2
2
2
2
ID
ERF008
ERF008
IR68
IR101
Công việcKhông
nhân viên
TuầnKhông
8
8
4
6
Thứ hai:
6/1/2025
8
8
8
Thứ ba:
7/1/2025
8
4
10
Thứ Tư:
8/1/2025
8
8
8
Thứ Năm:
9/1/2025
8
8
8
Thứ Sáu:
10/1/2025
4
4
4
thứ bảy:
11/1/2025
Bạn sẽ chuẩn bị dữ liệu của Wilkinson như thế nào cho mục đích phân tích chi phí lao động?
EX 5.9  (LO 4)  Dữ liệu   Phát hiện vấn đề về dữ liệu HomePrinter là nhà phân phối máy in laser và máy in phun cho 
văn phòng tại nhà. Bạn nhận được một tập dữ liệu mô tả các mẫu khác nhau mà họ mua (và bán) và 
Mua hàng tháng Giêng. Lập hồ sơ tập dữ liệu và xác định mọi vấn đề về dữ liệu.
EX 5.10  (LO 5)  Dữ liệu   Phát hiện các vấn đề về dữ liệu Creighton Group là một công ty kế toán nhỏ có 
hai mươi nhân viên. Họ theo dõi tiền lương, tiền thưởng và các thông tin khác của nhân viên trong một hệ thống dữ liệu 
tập tin. Lập hồ sơ tập dữ liệu này và xác định mọi vấn đề về dữ liệu.
EX 5.11  (LO 6)  Dữ liệu   Tạo và kiểm tra các quy tắc xác thực Vroomba sản xuất và bán các sản phẩm tiên tiến nhất
robot hút bụi nghệ thuật. Tất cả các đơn vị được bán với giá $ 279. Nhân viên bán hàng nhận được tiền thưởng lớn nếu họ bán được nhiều hơn 
1.000 đơn vị trong một tuần. Nhân viên bán hàng có thể bán hàng cho một danh sách khách hàng đã được phê duyệt trước.
tors, chỉ. Mỗi khách hàng (nhà phân phối) có một tên duy nhất. Họ cung cấp cho bạn một mẫu giao dịch bán hàng
hành động cho tuần ngày 6 tháng 1 năm 2025. Bạn sẽ kiểm tra quy tắc xác thực nào? Có giao dịch nào không 
yêu cầu điều tra thêm?
EX 5.12  (LO 5)  Dữ liệu   Xác định dữ liệu không nhất quán, không đầy đủ hoặc không hợp lệ Tội phỉ báng là một cách mới-
công ty chia sẻ. Họ tin rằng công việc của họ là chìa khóa thành công của họ. Họ theo dõi một phạm vi rộng 
nhiều thông tin nhân viên trong một ứng dụng đám mây tùy chỉnh. Vào ngày 1 tháng 1 năm 2025, họ cung cấp cho bạn 
mẫu thông tin nhân viên. Từ điển dữ liệu cho bảng Driver như sau.

Trường hợp ứng dụng chuyên nghiệp: Fluffy 5-73
 Tên 
 Mô tả 
 Số tài xế
 Số duy nhất của người lái xe phỉ báng. 
Ngày Sinh
 Sinh nhật của một tài xế.
 tiểu bang
 Tiểu bang nơi người lái xe sinh sống.
 NgàyGiấy phép lái xe
 Ngày người lái xe lấy được bằng lái xe.
 Xếp hạng trung bình
 Đánh giá trung bình của người lái xe, với 1 là mức tệ nhất có thể 
đánh giá và 5 là tốt nhất có thể. 
 Khách hàng
 Mã duy nhất gồm sáu chữ số được sử dụng để nhắn tin cho tài xế đón 
thông tin .
Lập hồ sơ cho tập dữ liệu này và xác định mọi vấn đề về dữ liệu không nhất quán, không đầy đủ hoặc không hợp lệ. 
 Dữ liệu EX 5.13 (LO 1, 4)
Chuẩn bị dữ liệu để phân tích Muffin House là một tiệm bánh công nghiệp ở 
Ogunquit, Maine. Họ sản xuất đồ nướng với số lượng lớn. Đối với mỗi lô, họ ghi lại một phạm vi 
thông tin. Một mẫu thông tin này được cung cấp trong một tệp dữ liệu. Từ điển dữ liệu cho lô 
bảng theo sau. 
BỘ
 Tên 
 Mô tả 
 ID 
 Xác định duy nhất một lô. 
 sản phẩm
 Sản phẩm là bánh nướng, sản xuất theo mẻ. 
 ước tính thông qua
 Thời gian thông lượng ước tính cho lô. Có bao nhiêu 
phải mất vài phút để hoàn thành lô. 
 hành động xuyên suốt
 Thời gian thông lượng thực tế cho lô. Bao nhiêu phút 
thực sự cần phải hoàn thành lô. 
 Số lượng ước tính
 Số lượng đơn vị bánh nướng ước tính sẽ được
do lô sản xuất. 
 Hành độngSố lượng
 Số lượng thực tế các đơn vị bánh nướng được sản xuất bởi 
lô. 
 Cơ sở vật chất
 Ghi lại cơ sở nào trong hai cơ sở A hoặc B đã sản xuất ra 
lô. 
 Giám sát viên
 Nhân viên giám sát lô hàng. 
Bạn sẽ thực hiện những thay đổi gì đối với tệp trước khi nó được sử dụng để phân tích? 
 Trường hợp ứng dụng chuyên nghiệp: Fluffy
Fluffy là một công ty đang phát triển nhanh chóng ở Bắc Dakota chuyên sản xuất và vận chuyển thú nhồi bông theo yêu cầu của khách hàng. 
tất cả năm mươi tiểu bang của Hoa Kỳ. Có một số tùy chọn để tùy chỉnh, từ việc khách hàng tự gửi 
thiết kế để gửi cho công ty một ý tưởng thiết kế sơ bộ để Fluffy phát triển và tạo ra. Trong khi kinh doanh 
đang diễn ra tốt đẹp, hệ thống thông tin của công ty là thảm họa và họ không thể thực hiện bất kỳ phân tích nào. 
Ưu tiên là tích hợp dữ liệu của họ vào cơ sở dữ liệu phân tích. Họ thuê công ty của bạn để giúp họ.

5-74  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
1
2
3
4
5
4326 Lochmere Lane, Groton, CT, 06340
1177 Phố Gore, Houston, TX, 77027
4457 Lonely Oak Drive, Di động, AL, 36603
3764 Phố Courtright, Fargo, ND, 58102 
2170 Metz Lane, Camden, NJ, 08102
Mã
Cửa hàng giảm giá
Lebron Jordan
Kho Duﬀy
Bob Dylan
Vải của Segher
Tên
Địa chỉ
Nhà cung cấp
1
2
3
4
5
Phillipps Circle 12, Fargo, ND, 58102
1012 Catherine Drive, St. Thomas, ND, 58276
2490 Đại lộ Findley, Hope, ND, 58046
3764 Phố Courtright, Fargo, ND, 58102
4000 Đại lộ Findley, Minot, ND, 58701
Mã
Joan Waddington
Matt Anthony
Elizabeth Petroni
Andrea Dylan
Jimmy John
Tên
Địa chỉ
Nhân viên
1
2
3
4
6
7
8
8
9
10
1
3
5
4
2
4
6
6
2
4
Số
Mua hàng
6/1/2025
23/1/2025
23/1/2025
30/1/2025
31/1/2025
7/1/2025
9/1/2025
14/1/2025
20/1/2025
21/1/2025
Ngày
$4,176
$1,597
$1,597
$3,433
$1,833
$660
$1,680
$4,703
$ 3,108
$ 2,263
Số lượng nhân viên
Sử dụng các mẫu chuẩn bị dữ liệu, xem xét dữ liệu mẫu và xác định ít nhất ba vấn đề. Ở đâu 
có thể áp dụng, hãy chỉ định mẫu bạn đã áp dụng để phát hiện và khắc phục sự cố.
PAC 5.2  Kế toán tài chính: Xác định và phân tích các khoản phải thu
Dữ liệu   Kế toán tài chính   Fluffy cho phép khách hàng của họ thanh toán theo từng đợt. trong hiện tại 
hệ thống, đơn đặt hàng và thanh toán được ghi vào hai tệp riêng biệt. Tệp SalesOrders ghi lại các 
số tiền khách hàng nợ Fluffy và các khoản thanh toán đã nhận được. Tệp Biên nhận tiền mặt 
ghi lại tất cả các khoản thanh toán nhận được. Mẫu của cả hai tập tin được hiển thị ở đây.
1
2
3,10
5
4
11
7,9,11
$838,46
100,03 USD
$245,67
3.632,16 USD
$386,90
$753,15
$194,80
$611,00
1.496,72 USD
$63,00
6/1/2025
7/1/2025
9/1/2025
13/1/2025
15/1/2025
20/1/2025
20/1/2025
23/1/2025
28/1/2025
25/1/2025
1
2
3
4
5
6
10
7
9
8
Đặt hàngKhông có ngày
Số tiền
Thanh toán
Đơn đặt hàng bán hàng
Tiền mặt
Thẻ tín dụng
Thẻ tín dụng
Kiểm tra
Tiền mặt
Kiểm tra
Kiểm tra
Kiểm tra
Kiểm tra
Kiểm tra
$838,46
100,3 USD
$150
$350
$386,9
200 USD
500 USD
$194,8
$403,15
$95,67
200 USD
6/1/2025
7/1/2025
9/1/2025
20/1/2025
24/1/2025
27/1/2025
27/1/2025
30/1/2025
31/1/2025
31/1/2025
30/1/2025
1
2
3
4
5
6
10
11
7
9
8
Biên nhận tiền mặtKhông
Ngày
Số tiền
Loại
Biên lai tiền mặt
Kiểm tra
	 1. Xác định và giải thích vấn đề chính trong tập dữ liệu. 
	 2. Mô tả cách bạn sắp xếp lại dữ liệu để có thể tính toán các khoản phải thu.
PAC 5.3  Kế toán quản lý: Phân tích chi phí
Dữ liệu   Kế toán quản trị   Phân tích chi phí là cực kỳ quan trọng đối với Fluffy. Ngoài việc sản xuất-
nhập thú nhồi bông và cung cấp dịch vụ vận chuyển tiêu chuẩn, họ cũng cung cấp một loạt các dịch vụ khác, chẳng hạn như 
chuyển phát nhanh, đóng gói và thiết kế. Trên thực tế, bất kỳ dịch vụ nào mà khách hàng yêu cầu sẽ được xem xét bởi 
Lông mượt. Khi công ty thuê ngoài một dịch vụ, chẳng hạn như chuyển phát nhanh, khách hàng chỉ cần thanh toán 
số tiền được tính cho Fluffy. Fluffy có mức đánh giá tiêu chuẩn cho mọi thứ được sản xuất nội bộ, thú nhồi bông 
động vật, thiết kế và đóng gói. 
0
154
0
0
0
0
0
0
252
0
0
0
225
0
0
150
0
0
0
0
0
0
50
125
0
25
250
125
10
35
0
0
35
1010
1011
1012
1013
1014
1015
1019
1020
1016
1018
1017
38
0
50
57
49
44
62
75
0
60
66
700
280
1.590
906
142
1.728
664
208
296
800
778
Không
Giá:100 Tiêu chuẩn Vận chuyển:0 Chuyển phát nhanhVận chuyển:0 Đóng gói:25 Thiết kế:50
Kiểm tra PAC 5.1 : Xác định các vấn đề về dữ liệu
Kiểm toán   Bạn được cấp quyền truy cập vào hồ sơ nhà cung cấp, giao dịch mua hàng và nhân viên của Fluffy. Các mẫu của ba 
tập tin xuất hiện ở đây.

Trường hợp tiếp theo của Le Grind: Sử dụng các mẫu chuẩn bị dữ liệu để làm sạch và cấu trúc dữ liệu cho mục đích phân tích 5-75
 Tệp dữ liệu mẫu cho thấy cách họ hiện ghi lại thông tin về chi phí và mức tăng giá. Để thi-
xin vui lòng, đối với Đơn hàng số 1010:
• Chi phí để bán được sản phẩm là $350. Giá họ đưa ra là 700 USD. Như được chỉ ra bởi col-
ừm, đánh dấu trên thú nhồi bông là 100%. 
• Không có cộng thêm phí vận chuyển hoặc chuyển phát nhanh. 
• Lãi suất đóng gói là 25%. Chi phí đóng gói cho Đơn hàng số 1010 là 40 USD. Có mức chênh lệch 25% 
($10) và khách hàng trả $50 ($40 + $10.) 
• Tổng chi phí cho Đơn hàng 1010 là $350 (thú nhồi bông) + $38 (vận chuyển tiêu chuẩn) + $40 (đóng gói) 
= $428. Mức tăng giá cho cùng một đơn hàng là $350 (thú nhồi bông) + $10 (đóng gói) = $360. Tổng cộng 
giá mà khách hàng phải trả là $788. 
 Fluffy muốn sử dụng dữ liệu của họ để trả lời các câu hỏi như:
• Tổng doanh thu được tạo ra là bao nhiêu? 
• Cơ cấu chi phí tổng thể của các đơn đặt hàng dựa trên các dịch vụ được cung cấp là gì? 
• Các dịch vụ bổ sung ảnh hưởng đến tỷ suất lợi nhuận tổng thể như thế nào? 
 Bạn sẽ cơ cấu lại dữ liệu như thế nào để giúp trả lời những câu hỏi này thông qua phân tích dễ dàng hơn? 
Kế toán thuế PAC 5.4: Xác thực số tiền thuế bán hàng
Kế toán thuế
Hiện tại, nhân viên bán hàng của Fluffy chịu trách nhiệm tạo và gửi đơn hàng tới khách hàng.
tomer. Tất cả nhân viên bán hàng đều có quyền truy cập vào tệp Excel chứa thuế suất bán hàng cho từng tiểu bang. Họ 
sử dụng thông tin đó để xác định thuế bán hàng của đơn hàng theo cách thủ công và nhập vào hệ thống kế toán. 
Connecticut
Delaware
Hawaii
Kentucky
bang Maryland
Michigan
Đảo Rhode
6:35
không áp dụng
4.17
6
6
6
7
tiểu bang
Thuế suất bán hàng
Thuế suất bán hàng
 Vào cuối mỗi tuần, hệ thống kế toán của Fluffy tạo ra một danh sách tất cả các đơn hàng được gọi là Đơn đặt hàng bán hàng. Như 
Kế toán của Fluffy, bạn phải thu thuế bán hàng và nộp cho các tiểu bang hiện hành. Bạn phải kiểm tra xem 
số tiền thuế bán hàng là chính xác. Tiếp theo là một mẫu có mười đơn đặt hàng từ tệp đơn đặt hàng bán hàng.
KY
RI
CT
RI
MD
xin chào
xin chào
DE
MI
MD
1
2
3
4
5
6
10
7
9
8
$47,46
$12,03
$14,67
$144,16
$ 21,90
30,15 USD
$7,80
0,00 USD
$84,72
$8,00
$791
$88
$231
$3,488
$365
$723
$611
$55
$187
$1,412
Đặt hàngKhông
Số tiền bán hàngTrạng thái thuế
Đơn đặt hàng bán hàng
 Sẽ rất hữu ích nếu bạn có thể kết hợp thông tin trong cả hai bảng để tự động tính thuế bán hàng
mỗi đơn hàng và so sánh thông tin thuế theo tiểu bang. Có bất kỳ vấn đề dữ liệu nào có thể ngăn chặn điều này không? 
Liệt kê các mẫu bạn đã sử dụng để xác định vấn đề.
Trường hợp tiếp theo của Le Grind: Sử dụng các mẫu chuẩn bị dữ liệu để làm sạch và cấu trúc dữ liệu 
cho mục đích phân tích
dữ liệu
Truy cập nền tảng học tập trực tuyến của Wiley để biết thông tin cơ bản về trường hợp, các câu hỏi, dữ liệu bổ sung và 
biết thêm chi tiết về vụ án đang tiếp tục.