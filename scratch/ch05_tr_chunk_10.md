5-58  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
14.  (LO 5)  Bạn đang kiểm tra các cột trong tập dữ liệu mà bạn đang phân tích. Các cột sau 
nằm trong tập dữ liệu.
ID tài sản khách sạn
Chứa một số nhận dạng duy nhất cho mỗi khách sạn.
Khách sạnTuổi
Khách sạn đã hoạt động được bao nhiêu năm kể từ khi khai trương.
Ngày khai trương
Ngày khách sạn khai trương.
Phòng có sẵn
Số phòng trong khách sạn.
Phòng đã thuê
Số phòng thuê trong năm.
Doanh thu
Số tiền thu được từ tiền thuê phòng trong năm.
Sau khi xem lại các tiêu đề và mô tả cột, bạn sẽ lưu ý điều nào sau đây? 
Một.	 Không có sự chồng chéo giữa các cột.
b.	 Có sự chồng chéo giữa HotelAge và Khai mạcDate.
c.	 Có sự dư thừa giữa RoomsAvailable và RoomsRented.
d.	 Có sự phụ thuộc giữa HotelAge và Khai mạcDate.
15.  (LO 5)  Hãy xem xét một tình huống trong đó quy tắc xác thực sau được áp dụng cho bảng Nhân viên 
hiển thị. 
HỢP LỆ =
NẾU NHÂN VIÊN.TUỔI < 24 VÀ NHÂN VIÊN.BẰNG ĐỘ = “ĐẠI HỌC”,
SAU ĐÓ “CÓ”,
KHÁC “KHÔNG”
nhân viên
Mã
Tuổi
Bằng cấp
1
23
Trường trung học
2
23
đại học
3
25
đại học
4
21
Phát biểu nào sau đây là sai?
Một.	 Giá trị của cột Hợp lệ cho nhân viên có mã “1” là “Không”. 
b.	 Giá trị của cột Hợp lệ cho nhân viên có mã “2” là “Không”. 
c.	 Giá trị của cột Hợp lệ cho nhân viên có mã “3” là “Không”. 
d.	 Giá trị của cột Hợp lệ cho nhân viên có mã “4” là “Không”. 
16.  (LO 6)  Mithali, một nhà phân tích tài chính, đang chuẩn bị dữ liệu để tham gia vào một dự án phân tích dữ liệu trước
xác định doanh thu cho giai đoạn tiếp theo dựa trên các cân nhắc về môi trường. Hiện cô đang xem xét lại 
các bảng để xác thực các quy tắc giữa các bảng về tính toàn vẹn tham chiếu. Điều nào sau đây đúng về tham chiếu 
tính chính trực?
Một.	 Trường khóa chính và khóa ngoài phải có cùng tên.
b.	 Khóa chính phải có một giá trị, nhưng khóa ngoại có thể có nhiều giá trị.
c.	 Các trường khóa chính và khóa ngoài có thể có các kiểu dữ liệu khác nhau.
d.	 Tất cả các giá trị trong khóa ngoại cũng phải tồn tại dưới dạng giá trị trong khóa chính tương ứng.
17.  (LO 6)  Skyline là công ty sưởi ấm và sửa ống nước quốc gia. Giám đốc tài chính của Skyline đang chuẩn bị cho nhân viên 
dữ liệu hiệu suất để phân tích thêm. Mẫu của bốn trong số các tập tin được hiển thị. Bạn sẽ đề xuất như thế nào 
kết hợp bốn tập tin này?
Tháng GiêngMua hàng
ID mua hàng
Ngày
Số tiền
nhân viên
14399
1/1/2025
1.432,24
  7
14400
1/1/2025
  799,99
14
14401
1/1/2025
320
12
14402
1/1/2025
  822,21
22

Câu hỏi trắc nghiệm  5-59
N
N
N
1
1
1
1
N
Ngày
Bảng kích thước
Bảng sự kiện
Bảng kích thước
TuầnNgày
Tháng
Năm
Ngày
Mã nhân viên
Tên
Vị trí
nhân viên
ID nhà cung cấp
Tên
Danh bạ
nhà cung cấp
DòngMụcSố
nhân viên
Mục
Ngày mua
nhà cung cấp
ID mua hàng
số lượng
Giá
Mua hàng
Mã hàng
Mô tả
Mục
Nhân khẩu học nhân viên
ID
Tên
Ngày Sinh
14399
Ben Jespers
3/3/1975
14400
Bắc Thạch
17/7/1985
14401
Michael Rodman
20/5/1984
14402
Benita Alvarez
11/11/1979
Tiền lương nhân viên
ID
Lương theo giờ
14399
25
14400
38
14401
36
14402
45
Tháng HaiMua hàng
ID mua hàng
Ngày
Số tiền
nhân viên
15021
1/2/2025
123,89
  4
15022
1/2/2025
540,99
  1
15023
1/2/2025
183,12
14
15024
1/2/2025
744,41
21
một.	 Hợp nhất các giao dịch mua hàng tháng 1 và nhân khẩu học nhân viên và hợp nhất các giao dịch mua hàng tháng 2 và 
Tiền lương của nhân viên.
b.	 Liên minh Tháng GiêngMua hàng và Tháng HaiMua hàng và Công đoàn Nhân viênNhân khẩu học và 
Tiền lương của nhân viên.
c.	 Liên minh Tháng GiêngMua hàng và Tháng HaiMua hàng và hợp nhấtNhân khẩu học và 
Tiền lương của nhân viên.
d.	 Liên minh Tháng GiêngMua hàng và Nhân viênNhân khẩu học và hợp nhất Tháng HaiMua hàng và 
Tiền lương của nhân viên.
18.  (LO 6)  Điều nào sau đây sẽ dẫn đến việc chuyển đổi lược đồ ngôi sao này thành lược đồ bông tuyết?
Một.	 Tên nhân viên là trường kết hợp chứa cả họ và tên của nhân viên.
b.	 Đối với một số nhân viên, vị trí của họ không được biết đến.
c.	 Có thể có nhiều địa chỉ liên hệ cho một nhà cung cấp.
d.	 Ngày trong tuần, tháng và năm được sử dụng rộng rãi cho mục đích phân tích.

5-60  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Câu hỏi ôn tập
19.  (LO 7)  Hamza đang chuyển dữ liệu vào cơ sở dữ liệu phân tích để phân tích. Anh ấy nên bước những bước nào 
thực hiện để xác định xem tất cả các dữ liệu được chuyển giao?
Một.	 Xem lại các cột để biết quy ước đặt tên thích hợp.
b.	 Thiết lập các quy tắc xác thực dữ liệu và xác định dữ liệu nào không tuân thủ các quy tắc xác thực dữ liệu.
c.	 Kiểm tra các giá trị riêng biệt và phân tích tần số. 
d.	 So sánh số hàng của cơ sở dữ liệu phân tích với số hàng của tập dữ liệu trong công cụ ETL.
20.  (LO 7)  Bạn đang chuẩn bị bản phân tích cho một công ty giao đồ ăn tên là Dine At Home. Dùng bữa tại 
Home nhận đơn đặt hàng thực phẩm từ nhà hàng và giao cho khách hàng. Khách hàng có thể đặt hàng 
nhiều lần nhưng một đơn hàng chỉ dành cho một khách hàng. Nhà hàng có thể có nhiều đơn hàng, nhưng một đơn hàng thì 
chỉ dành cho một nhà hàng. Thông số kỹ thuật lượng số nào sau đây là không chính xác?
Nhà hàng
Nhà hàng
Đặt hàng
Đặt hàng
Đặt hàng
Đặt hàng
Khách hàng
Khách hàng
N
N
1
N
một.
b.
c.
d.
1.  (LO 1)  Mô tả việc chuẩn bị dữ liệu. Tại sao việc chuẩn bị dữ liệu là cần thiết trước khi phân tích dữ liệu?
2.  (LO 1)  Giả sử bạn đang chuẩn bị cơ sở dữ liệu phân tích. Bạn đã tải xuống dữ liệu thô từ thông tin-
hệ thống mation và hiện đang kiểm tra tính nhất quán của dữ liệu. Thảo luận về hai kỹ thuật lập hồ sơ mà bạn 
có thể sử dụng để xác định sự không nhất quán trong dữ liệu.
3.  (LO 2)  Xác định và mô tả ba quy trình con chuyển đổi dữ liệu.
4.  (LO 2)  So sánh và đối chiếu hai hình thức tích hợp dữ liệu: liên kết và kết hợp.
5.  (LO 2)  So khớp dữ liệu là gì và tại sao việc tích hợp dữ liệu lại là một thách thức?
6.  (LO 3)  Mô tả từ điển dữ liệu là gì và tại sao nó là một phần quan trọng trong phân tích dữ liệu. 
7.  (LO 3)  Thảo luận lý do tại sao cách tiếp cận dựa trên mẫu để chuẩn bị dữ liệu lại phù hợp cho phân tích dữ liệu 
dự án.
8.  (LO 3)  Thảo luận về các công cụ và tính năng có sẵn trong Microsoft Excel để đảm bảo việc truyền tải tất cả dữ liệu 
khi trích xuất dữ liệu.
9.  (LO 4)  So sánh và đối chiếu các kiểu dữ liệu số nguyên và văn bản. Bao gồm các biến như thế nào 
được ghi chú dưới dạng số nguyên và các biến được mã hóa dưới dạng văn bản được sử dụng trong phân tích dữ liệu. 
10.  (LO 4)  Thảo luận về sự khác biệt giữa cột tổng hợp và cột đa giá trị và đưa ra ý kiến 
ví dụ của mỗi cái. 
11.  (LO 4)  Mô tả các kỹ thuật lập hồ sơ để phát hiện các giá trị không nhất quán và giải thích cách sửa đổi
nếu các giá trị không nhất quán. Cho một ví dụ về một giá trị không nhất quán. 
12.  (LO 5)  Thảo luận về tầm quan trọng của việc giảm thiểu dữ liệu dư thừa giữa các cột trong bảng phân tích 
cơ sở dữ liệu.
13.  (LO 5)  Thảo luận tại sao việc xác minh sự hiện diện của khóa chính lại quan trọng. Giải thích cách xác định phần còn thiếu 
khóa chính và cách tạo khóa chính.
14.  (LO 6)  Mô tả mô hình hóa chiều và thảo luận tầm quan trọng của việc tuân thủ các quy định về chiều 
nguyên tắc mô hình hóa khi xây dựng cơ sở dữ liệu phân tích.
15.  (LO 6)  Sự khác biệt giữa hợp nhất và hợp nhất là gì? Cho ví dụ khi một công đoàn 
không thể sử dụng được 
16.  (LO 6)  Thảo luận về lợi ích của các cột có giá trị đơn và bảng phẳng để cắt dữ liệu.

Bài tập ngắn  5-61
17.  (LO 6)  Giải thích cách bạn phát hiện và khắc phục các vấn đề sau. 
vấn đề
Phát hiện 
Sửa chữa
Một bảng trong cơ sở dữ liệu phân tích của bạn không có khóa chính.
Một cột trong bảng tài sản cố định có cột ngày mua 
(DateAcquired) và tuổi tài sản (AssetAge). Tuổi đại diện 
tài sản đó đã được giữ trong bao lâu kể từ ngày mua.
Một bảng chứa thông tin nhà cung cấp được đặt tên là VINFO.
Dữ liệu không hợp lệ có thể đã được nhập vào một trong các bảng trong 
cơ sở dữ liệu.
18.  (LO 6)  Thảo luận về các mô hình chuyển đổi và nó khác với các cột chuyển đổi như thế nào. 
19.  (LO 7)  Thảo luận về tầm quan trọng của việc xác thực các mối quan hệ khi truyền dữ liệu từ công cụ ETL 
vào cơ sở dữ liệu phân tích.
20.  (LO 7)  Thảo luận tại sao việc đảm bảo truyền chính xác khi tải dữ liệu lại quan trọng. Cho một ví dụ về 
làm thế nào để xác định xem dữ liệu có chính xác hay không. 
Bài tập ngắn gọn
BE 5.1  (LO 1)  Kiểm toán   Bạn là nhân viên kiểm toán được phân công phụ trách kiểm toán Coleman Cable, Inc. bạn có 
được yêu cầu phát triển lược đồ sao để minh họa cấu trúc của mô hình dữ liệu phân tích cho hoạt động bán hàng của bạn 
phân tích. Cấp trên đã cung cấp cho bạn bản phác thảo đầu tiên của lược đồ sao. Nối mỗi điều sau đây 
tới vị trí thích hợp của nó trong lược đồ hình sao.
	 Một.	 Bảng kích thước
	 b.	 Bảng sự kiện
	 c.	 N
	 d.	 Đo lường
	 đ.	 Tổng số tiền đã mua
	 f.	 Nhân viên mua hàng
ngày
Ngày trong tuần
Tháng
Năm
Ngày
ID thư ký
Tên đầu tiên
Họ
Tên
Nhân viên mua hàng
Mã sản phẩm
Tên
Mô tả
Chi phí
sản phẩm
ID nhà cung cấp
Tên
Người liên hệ
đường phố
Thành phố
Mã zip
tiểu bang
Địa chỉ
nhà cung cấp
1
1
1
1
N
N
N
N
Ngày
sản phẩm
nhà cung cấp
Giá
số lượng
Số tiền
Tổng số lượng đã mua
Mua hàngĐơn hàngKhông
Mua hàng
3.
Chìa khóa
Cột
Cột được tính toán
Khóa ngoại
6.
4.
5.
1.
2.

5-62  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
BE 5.2  (LO 1)  Bạn là nhà phân tích tài chính được yêu cầu trình bày vấn đề với người quản lý của bạn về mối quan hệ giữa 
các bảng trong cơ sở dữ liệu phân tích của bạn. Đối với mỗi thông số kỹ thuật trong bốn mối quan hệ sau đây, hãy xác định các 
câu thích hợp nhất mô tả một trong những đặc điểm chính của nó.
Khách hàng
Kích thước
Bảng
Sự thật
Bảng
nhà cung cấp
nhân viên
nhân viên
bán hàng
Mua hàng
Đặt hàng
Thanh toán
1
N
1
N
1
N
1
N
1
2
3
4
	 một.	 Chỉ có một nhà cung cấp có thể được chỉ định để mua hàng.
	 b.	 Với mỗi một khách hàng có thể có nhiều lần bán hàng.
	 c.	 Cùng một nhân viên có thể đặt nhiều đơn hàng.
	 d.	 Có thể có nhiều khách hàng cho cùng một giao dịch mua bán – ví dụ: hai người mua một căn nhà.
	 đ.	 Chỉ có một nhân viên chịu trách nhiệm thanh toán.
BE 5.3  (LO 1)  Bạn đã được cung cấp một bảng dữ liệu chứa dữ liệu khách hàng được thu thập cho một cửa hàng bán lẻ 
chương trình khách hàng thân thiết của công ty. Sau đây là một đoạn trích của bảng dữ liệu đó. Xác định ít nhất ba dữ liệu 
vấn đề chất lượng.
Thông tin khách hàng
Giới tính
Ngày
Email
Steve Millier, 121 South Beach St
M
21/10/1978
Steve.miller
Sara Stevens, 435 Parker St
Nữ
21/9/2008
sara.stevens@mail.com
Libby Ralston, 812 Foster Ave
Nữ
28/6/2956
libby123@mail.com
Able Meyers, 902
Nam
4/1/2009
Smileyone@mail.com
Spring Stevens, 639 Bulldog Ct
Không tiết lộ
14/6/1982
sparkie.steven
Kevin Hogan, 3098 N. Tier St. Căn hộ 392
M
22/7/1955
doglover@mail.com
Libby Ralston, 812 Foster Ave
Nữ
Sara Stevens, 435 Parker St
Nữ
21/9/2008
sara.stevens@mail.com
Cooper Mazzu, 2342 Lincoln Way
Nam
17/4/1955
coop8623
Molly trắng
F
21/10/1977
molly.white.123@mail.com
Janet Jones, 909 Xa lộ 78
F
BE 5.4  (LO 2)  Hai bảng sau phải được tích hợp vào một bảng kết hợp. Bảng kết hợp 
phải bao gồm các trường sau cho mỗi bản ghi: Mô tả, QOH, Vị trí, Chi phí, Giá và Bán hàng. 
Xem lại từng bảng và xác định ba thách thức đối sánh dữ liệu.
Bảng A
Mô tả
QOH
Vị trí
Vòng cổ chó màu xanh
  5
A10
Cổ áo bác sĩ màu đỏ
  3
A11
Dây 7 inch chắc chắn 
Chì
10
B10
Dây 10 inch 
Chì chắc chắn - Xanh
  3
B10
Dây 10 inch 
Chì chắc chắn - Đen
  5
B10
Bảng B
Mô tả sản phẩm
Chi phí
Giá
bán hàng
Vòng cổ cho chó - Xanh dương
12,54
16,93
Y
Dây dẫn chắc chắn 7 inch
15,44
20,85
N
Vòng cổ chó đỏ
15,54
20,98
N
Dây 10 inch chắc chắn 
Chì - Bk
20,38
27,52
N
Dây 10 inch màu xanh lá cây 
Chì chắc chắn
28,34
38,26
Y

Bài tập ngắn  5-63
Bảng BE 5,5  (LO 2)  (A) và (B) thể hiện các mô hình dữ liệu thay thế cho cùng một tập dữ liệu. So sánh và 
đối chiếu hai mô hình.
ID
Tên
Địa chỉ
Nhóm
Tên nhóm
Khách hàng
(A)
(B)
1
N
1
1
N
ID nhóm
Tên nhóm
Nhóm
ID
Tên
Địa chỉ
Nhóm
Khách hàng
Hóa đơnKhông
Số tiền
Ngày
Khách hàng
bán hàng
N
Hóa đơnKhông
Số tiền
Ngày
Khách hàng
bán hàng
BE 5.6  (LO 3)  Kế toán thuế   Bạn đã được yêu cầu phát triển cơ sở dữ liệu phân tích để phân tích địa phương 
và thuế bán hàng liên bang so với thuế giá trị gia tăng. Một đoạn trích của bảng dữ liệu của bạn được trình bày.
Ngày bánID
25/5/2024
26/5/2024
27/5/2024
28/5/2024
29/5/2024
30/5/2024
Hoa Kỳ
Hoa Kỳ
MEX
MEX
CÓ THỂ
AUS
$197
$113
$155
$423
$88
$250
1001
0,0685
0,0685
0,16
0,16
0,05
0,1
1002
1003
1004
1005
1006
Bán hàngĐịa điểm bánSố tiền
0,02
0,02
Thuế bán hàng tại địa phương
VAT
Bạn đã bắt đầu quá trình và bây giờ đã sẵn sàng tạo từ điển dữ liệu. Đối với mỗi khoảng trống 
được đánh số trong bảng sau, hãy xác định câu hoặc thuật ngữ thích hợp để tạo thành 
từ điển dữ liệu. Mỗi thuật ngữ hoặc câu sẽ chỉ được sử dụng một lần.
	 Một.	 mã giảm giá
	 b.	 BánSố lượng
	 c.	 VAT
	 d.	 Thuế địa phương
	 đ.	 Tỷ lệ phần trăm thuế bán hàng liên bang được thu 
tại thời điểm bán hàng.
	 f.	 Địa điểm nơi việc bán hàng được thực hiện.
	 g.	 Ngày việc bán hàng được thực hiện.
Tên
Mô tả
1.
Mã định danh duy nhất cho mỗi lần bán hàng được thực hiện.
Ngày
2.
BánĐịa điểm
3.
4.
Tổng số tiền bán trước thuế.
5.
Phần trăm thuế địa phương thu được tại thời điểm bán hàng.
Thuế bán hàng
6.
7.
Tỷ lệ phần trăm thuế giá trị gia tăng phải thu liên quan đến việc bán hàng.