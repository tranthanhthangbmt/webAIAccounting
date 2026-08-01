5-64  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
BE 5,7  (LO 3, 4)  Bạn phải đối mặt với năm tình huống chuẩn bị dữ liệu khác nhau. Hãy ghép một vấn đề về chất lượng dữ liệu với từng vấn đề 
kịch bản. Mỗi vấn đề về chất lượng dữ liệu chỉ có thể được sử dụng một lần. 
	 Một.	 Tên cột không chính xác hoặc mơ hồ.
	 b.	 Tất cả các cột không có giá trị đơn.
	 c.	 Tất cả dữ liệu chưa được truyền chính xác.
	 d.	 Các cột không có kiểu dữ liệu chính xác.
	 đ.	 Tất cả dữ liệu chưa được chuyển giao.
#
Kịch bản
Vấn đề về chất lượng dữ liệu
1.
Grace đã nhận được tập dữ liệu có cột có tiêu đề ClientInfo. 
Mỗi bản ghi trong trường đó chứa địa chỉ gửi thư của khách hàng.
2.
Dữ liệu trong cột Doanh số là số tiền của 
giao dịch mua bán. Tuy nhiên, Quinn lưu ý rằng kiểu dữ liệu là 
được phân loại là ký tự chữ và số hoặc dữ liệu văn bản.
3.
Khi kiểm tra dữ liệu được chuyển từ hệ thống tính lương sang hệ thống 
kho dữ liệu, Molly nhận thấy rằng hồ sơ tiền lương của nhân viên chỉ 
bao gồm các nhân viên có họ bắt đầu từ A đến S.
4.
Barnes nhận được một bảng dữ liệu từ nhóm CNTT. Một trong những 
các cột chứa cả dữ liệu tên khách hàng và dữ liệu thời hạn thanh toán.
5.
Devon trích xuất dữ liệu từ bộ phận vận chuyển của công ty 
nhật ký. Ngoài dữ liệu lô hàng, nhật ký còn chứa thông tin tóm tắt 
số liệu thống kê như tổng số lượng vận chuyển. Khi kiểm tra 
dữ liệu được trích xuất, Devon lưu ý rằng tổng số lượng được vận chuyển 
vì dữ liệu được trích xuất không khớp với tổng số lượng được vận chuyển 
số trong nhật ký.
BE 5.8  (LO 3)  Dữ liệu   Bạn nhận được một tệp văn bản có thông tin đơn đặt hàng tháng 12. Trước bạn 
bắt đầu phân tích của bạn, sử dụng Power Query (Excel hoặc Power BI) để xác định xem dữ liệu đã được
được chuyển giao đầy đủ và chính xác. Tổng cộng 34 lần mua hàng với tổng chi phí trung bình cho mỗi sản phẩm (dòng đặt hàng) 
trong số 610,98 USD đã được thực hiện trong tháng 12. 
	 1. Đặt tên cho mẫu chuẩn bị mà bạn đã sử dụng để xác minh tất cả các giao dịch đã được chuyển và giải thích cách thực hiện 
bạn đã xác minh điều này.
	 2. Đặt tên cho mẫu chuẩn bị mà bạn đã sử dụng để xác minh rằng tất cả dữ liệu đã được truyền chính xác và giải thích 
cách bạn xác minh điều này.
BE 5.9  (LO 4)  Simply Salon Beautiful thu thập thông tin khách hàng và gán ID khách hàng duy nhất 
để theo dõi phần thưởng, giao dịch mua hàng và cuộc hẹn của khách hàng. 
ID khách hàngTên khách hàng
Emily Boyd
bỏng Artie
Mario Edwards Jr.
Javon Wims
Tierna Davidson
Sarah Gorden
Nữ
Nam
Nam
Nam
Nữ
Nữ
21/10/1978
21/9/2008
28/6/2906
4/1/2009
14/6/1982
22/7/1955
A283
$490,12
$48,01
$287,89
$476,45
$393,99
$593,07
1
0
1
1
0
1
A493
A393
B382
C494
C948
Giới TínhNgày Sinh
1
3
6
2
4
6
Phần thưởng
Số lượng
Cuộc hẹn đã lên lịch
Đối với mỗi cột, xác định loại dữ liệu thích hợp nhất. Mỗi loại dữ liệu có thể được sử dụng một lần, nhiều hơn 
một lần, hoặc không chút nào.
	 Một.	 Ngày
	 b.	 Ngày/Giờ
	 c.	 Số thập phân
	 d.	 Tỷ lệ phần trăm
	 đ.	 văn bản
	 f.	 thời gian
	 g.	 Toàn bộ số
Cột
Kiểu dữ liệu
Mã khách hàng
1.
Tên khách hàng
2.
Giới tính
3.
Ngày sinh
4.
Phần thưởng
5.
YTDDoanh số
6.
Số cuộc hẹn đã lên lịch
7.

Bài tập ngắn  5-65
BE 5.10  (LO 4)  Dữ liệu   Với dữ liệu được cung cấp, hãy sử dụng công cụ ETL để thực hiện các thao tác sau.
	 1. Sửa đổi kiểu dữ liệu cho cột CustomerId từ văn bản thành số nguyên. Có bao nhiêu bản ghi 
báo cáo lỗi sau sự thay đổi này?
	 2. Xác định số phần thưởng cao nhất mà khách hàng nhận được.
	 3. Xác định bất kỳ dữ liệu không chính xác nào trong cột Thời lượng cuộc hẹn.
BE 5.11  (LO 5)  Dữ liệu   Sếp của bạn đưa cho bạn một tệp văn bản chứa thông tin bán hàng bao gồm 
số tiền, chiết khấu và phiếu giảm giá. Một đoạn trích được hiển thị ở đây.
Hóa đơnKhông
6/1/2025
8/1/2025
9/1/2025
10/1/2025
10/1/2025
6/1/2025
7/1/2025
7/1/2025
8/1/2025
8/1/2025
1203
1208
1209
Tiền mặt
Tiền mặt
1210
1211
Tiền mặt
1212
10/1/2025
10/1/2025
11/1/2025
11/1/2025
$398
$354
$863
$944
0
2
0
5
5
2
0
0
0
0
5
10
0
2
25
0
5
25
0
0
10
5
2
0
0
0
5
15
23
144
233
17
101
224
301
24
144
1204
Tiền mặt
1206
1207
Tiền mặt
Ngày bán hàng
$621
$233
$539
$985
$320
$682
$477
$779
$742
$452
Số tiền Phiếu giảm giá Khách hàng
Dựa trên cuộc thảo luận với sếp, bạn tập hợp từ điển dữ liệu sau đây.
Tên
Mô tả
Hóa đơnKhông
Một mã duy nhất được cấp cho việc bán hàng Tín dụng mà hóa đơn được lập. Nhãn 
Tiền mặt được sử dụng để bán hàng bằng tiền mặt.
Ngày bán hàng
Ngày việc bán hàng xảy ra.
Số tiền
Số tiền mà khách hàng nợ trước khi giảm giá và phiếu giảm giá.
Giảm giá
Tỷ lệ chiết khấu được trao cho khách hàng.
Phiếu giảm giá
Một phiếu giảm giá trị giá một đô la do khách hàng cung cấp. Cần lưu ý rằng một 
phiếu giảm giá chỉ có thể được xem xét khi không áp dụng giảm giá.
Khách hàng
ID của khách hàng. Đối với bán hàng bằng tiền mặt, trường này được để trống. 
Liệt kê các mẫu chuyển đổi bảng (mẫu 11–14) có liên quan đến tập dữ liệu này và giải thích cách 
bạn sẽ áp dụng từng cái.
BE 5.12  (LO 5)  Người giám sát của bạn đã yêu cầu bạn hiểu rõ về doanh số bán hàng cũng như các khoản giảm giá và phiếu giảm giá được áp dụng 
cho họ. Họ đã cung cấp cho bạn một bảng tính để bạn phân tích. Đây là một đoạn trích của bảng tính đó:
0
32
1
0
0
45
0
0
1
10
Ngày bán hàng
$197
$4,680
$584
$997
$258
$113
$155
$423
$88
$250
21/10/2025
27/10/2025
28/10/2025
29/10/2025
30/10/2025
22/10/2025
23/10/2025
24/10/2025
25/10/2025
26/10/2026
Số tiền
0
2
0
1
2
2
0
12
10
3
Phiếu giảm giá
1
2
1
2
3
1
1
Đã được phê duyệt
	 1. Áp dụng mẫu chuẩn bị dữ liệu 11. Bảng có tiêu đề Số tiền & Chiết khấu. Đề xuất tên bảng 
điều đó ít mơ hồ hơn.
	 2. Áp dụng mẫu chuẩn bị dữ liệu 12. Bảng có khóa chính không? Nếu không, hãy mô tả cách bạn 
sẽ tạo khóa chính cho bảng này.

5-66  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
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
James
lenk
Richards
Lozano
David
Petroni
kim cương
Sutherland
Đất sét
McCarthy
Kayne
Ivan
Mick
Juan
Gail
Ann
Shiela
Yvonne
Marcus
Molly
Houston
Texarcane
Chicago
Boston
Chicago
Houston
Boston
Chicago
Boston
Chicago
Nam
Nam
Nam
Nam
Nữ
Nữ
Nữ
Nữ
Nam
Nữ
1
3
5
4
7
1
3
4
5
1
27
35
39
37
40
27
35
37
39
27
3,521
3,811
2,901
3,477
3.420
1.709
2.331
3,871
1.942
3.665
Họ
ABC
Tên đầu tiên
ABC
Vị trí
ABC
Giới tính
ABC
Cấp độ
123
2024Giờ
123
Người đánh giáGiờ
123
BE 5.13  (LO 6)  Dữ liệu   Bạn được cung cấp hai tệp. Một tệp chứa thông tin nhân viên và tệp còn lại 
chứa thông tin hiệu suất của nhân viên. Đây là từ điển dữ liệu cho cả hai bảng.
Nhân viên (Thông tin nhân viên chung)
Tên
Mô tả
Họ
Họ của nhân viên.
Tên đầu tiên
Tên của một nhân viên.
Vị trí
Thành phố nơi nhân viên cư trú.
Giới tính
Giới tính của nhân viên.
Hiệu suất của nhân viên (Thông tin về hiệu suất của nhân viên)
Tên
Mô tả
Họ
Họ của nhân viên.
Tên đầu tiên
Tên của một nhân viên.
Cấp độ
Cấp độ của nhân viên với 1 là thấp nhất và 7 là cao nhất 
cao nhất.
2024Giờ
Số giờ một nhân viên đã làm việc vào năm 2024.
Tỷ lệ mỗi giờ
Mức lương theo giờ của một nhân viên.
Sử dụng mẫu chuẩn bị dữ liệu 15, kết hợp cả hai tệp để đạt được kết quả hiển thị ở đây.
BE 5,14  (LO 6)  Dữ liệu   HoneyBees là một nhà hàng cao cấp ở Bắc California. Họ vừa cài đặt 
hệ thống điểm bán hàng (POS) bên bàn trên mỗi bàn trong số 20 bàn của họ. Họ cung cấp cho bạn dữ liệu đầu tiên 
hai ngày sử dụng hệ thống mới. Từ điển dữ liệu mô tả dữ liệu được hệ thống POS thu thập 
vào cả hai ngày.
Từ điển dữ liệu ngày 1 của HoneyBees
Tên
Mô tả
Ngày
Ngày diễn ra giao dịch mua bán.
thời gian
Thời điểm diễn ra giao dịch mua bán.
Số tiền
Số tiền của giao dịch bán hàng.
Mẹo
Tiền boa nhận được theo phần trăm.
Khách hàng
Tên của khách hàng–tên trên thẻ tín dụng được sử dụng.
Máy chủ
Tên của máy chủ (nhân viên).
POS
Số POS–từ 1 đến 20–được sử dụng để ghi lại 
giao dịch mua bán.

Bài tập ngắn  5-67
Từ điển dữ liệu ngày thứ 2 của HoneyBees
Tên
Mô tả
Ngày
Ngày giao dịch bán hàng xảy ra.
thời gian
Thời điểm diễn ra giao dịch mua bán.
Số tiền
Số tiền của giao dịch bán hàng.
Mẹo
Tiền boa nhận được theo phần trăm.
Máy chủ
Tên của máy chủ (nhân viên).
Khách hàng
Tên của khách hàng–tên trên thẻ tín dụng được sử dụng.
POS
Số POS–từ 1 đến 20–được sử dụng để ghi lại doanh số bán hàng 
giao dịch.
Kết hợp dữ liệu trong hai tệp cho mục đích phân tích. Tệp mới sẽ có 46 giao dịch. 
BE 5.15  (LO 6)  Bạn đang đánh giá một tập dữ liệu để xác định xem dữ liệu đó có hợp lệ hay không. Mô hình dữ liệu cho 
tập dữ liệu được hiển thị.
ID
Thời gian thực tế
Loại công việc
Tỷ lệ phương sai
Công việc
N
1
Mã
Thời gian dự toán
Loại công việc
VarianceRatio là thước đo và đây là công thức của nó: 
Tỷ lệ phương sai = (Thời gian thực tế – Thời gian dự toán) / Thời gian dự toán
Bạn lưu ý rằng thời gian dự kiến tối thiểu cho tất cả công việc là hai giờ. Nhóm của bạn thiết kế một số vali-
quy tắc ngày tháng, bao gồm quy tắc xác thực giữa các bảng sau:
NẾU BIẾN ĐỔI > 1 
SAU ĐÓ ĐỎ 
KHÁC LÀ XANH 
	 1. Chỉ định quy tắc xác thực theo cách dễ hiểu đối với người kinh doanh. 
	 2. Thảo luận xem điều gì có thể khiến công thức tạo ra giá trị màu đỏ.

5-68  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
BE 5,16  (LO 7)  Tin Fos, một công ty dịch vụ thông tin cỡ trung bình, đã nhận được một bộ dữ liệu từ một trong những công ty của họ. 
khách hàng. Họ đang cố gắng thiết kế các báo cáo phân tích nhưng kết quả lại trống hoặc sai. Đánh giá 
từ điển dữ liệu và mô hình dữ liệu sau đây để xác định hai vấn đề đang gây ra sự cố.
Từ điển dữ liệu
PurchaseOrder (Thông tin về đơn hàng đã đặt)
Tên
Mô tả
Số tiền
Số tiền phải trả cho nhà cung cấp.
Ngày
Ngày mà đơn hàng được đặt.
ID
ID duy nhất của đơn đặt hàng.
nhà cung cấp
ID của nhà cung cấp mà hàng hóa được mua.
Giao hàng (Thông tin về hàng hóa được giao)
Tên
Mô tả
Ngày
Ngày mà hàng hóa được giao.
Giao hàngKhông
ID duy nhất của lô hàng.
Mua hàngĐơn hàng
Số đơn đặt hàng liên quan đến việc giao hàng.
Nhà cung cấp (Thông tin về nhà cung cấp)
Tên
Mô tả
Địa chỉ
Địa chỉ của nhà cung cấp.
ID
ID duy nhất của nhà cung cấp.
Tên
Tên của nhà cung cấp.
Mô hình dữ liệu:
Mua hàngĐơn hàng
Ngày
ID
nhà cung cấp
1
1
Số tiền
nhà cung cấp
ID
Tên
Địa chỉ
Giao hàng tận nơi
Giao hàngKhông
Mua hàngĐơn hàng
Ngày
N
N
Mối quan hệ:
Đang hoạt động
Từ: Bảng (Cột)
Đến: Bảng (Cột)
Đơn đặt hàng (ID)
Nhà cung cấp (Tên)
Giao hàng (DeliveryNo)
Đơn đặt hàng (Nhà cung cấp)
Quản lý mối quan hệ

Bài tập  5-69
Bài tập
EX 5.1  (LO 1, 2, 4, 5)  Dữ liệu   Chuyển đổi dữ liệu cơ bản Bạn đang chạy phần mềm kế toán của riêng mình 
luyện tập. Khách hàng của bạn là các công ty vừa và nhỏ cần hỗ trợ xử lý giao dịch, 
kế toán, lập báo cáo tài chính. Khách hàng mới nhất của bạn, Healthy Pets, là một nhà bán lẻ đồ dùng cho thú cưng với mười 
các địa điểm trên toàn khu vực. Chủ sở hữu công ty đã cung cấp cho bạn dữ liệu về lòng trung thành của khách hàng. Mỗi cus-
tomer có thể tham gia chương trình khách hàng thân thiết để kiếm điểm khi mua hàng giảm giá.
	 1. Loại bỏ các mục khách hàng trùng lặp (Gợi ý: Có 11 bản ghi trong bảng gốc; bảng sạch 
chỉ nên bao gồm 9 bản ghi).
	 2. Thay thế các giá trị trong cột giới tính để các bản ghi có nhãn “M” được thay thế bằng Nam và 
các bản ghi có “F” được thay thế bằng Nữ.
	 3. Đổi tên cột Ngày thành DOB, (ngày sinh của khách hàng).
	 4. Chuyển đổi cột CustInfo thành hai cột có giá trị đơn. Dán nhãn một cột Tên và 
đường cột thứ hai.
EX 5.2  (LO 1, 2, 4, 6)  Dữ liệu   Chuyển đổi cột và mô hình Bạn là nhân viên kế toán cho Bar-
Gain, một thương hiệu nhượng quyền mua các mặt hàng trên khắp Bắc Mỹ, sửa chữa và làm sạch chúng, sau đó bán chúng 
với mức tăng đáng kể. Bạn đã được yêu cầu tạo cơ sở dữ liệu phân tích để hiểu việc mua hàng 
dự đoán về một dự án đánh giá chu kỳ kinh doanh và tính hiệu quả. Người giám sát của bạn đã cung cấp cho bạn ba 
Tệp CSV và tệp PDF có từ điển dữ liệu cho từng tệp. Áp dụng quy trình chuẩn bị dữ liệu thích hợp
terns vào ba tệp để tạo cơ sở dữ liệu phân tích nhất quán với cơ sở dữ liệu được hiển thị ở đây. 
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
US1
US2
US3
US4
US5
CAN1
CAN2
CAN3
CAN4
CAN5
Cohen, Sandra
Xám, Thứ Bảy
Leroy, Shanice
Tinh thần, Benita
Vương, CeCe
Chu, Jim
Coyle, Irene
Dabrowski, Elizbieta
Vua, Laura
Jackson, Kiara
scohen@vstores.com
thứ bảy-gray@Ibox.com
sleroy@google.com
bmor@hf.com
cece@cch.com
jzhu@outlook.com
Irene@coyle.com
ElzDab@gmail.com
LauraKing@fmh.com
kiaraj@ncn.com
ID
ABC
Tên
ABC
Email
ABC
2
1
1
5
1
1
1
1
2
2
nhà cung cấp
ABC
Giá
123
Loại
ABC
Ngày
số lượng
123
Danh mục
ABC
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
8992
8993
8994
8894
8896
8897
8897
8898
8898
8899
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
3/1/2025
3/1/2025
3/1/2025
3/1/2025
3/1/2025
Nồi cơm điện
Điện thoại
Nồi chiên
Thú nhồi bông
truyền hình
Thú nhồi bông
lò vi sóng
Tai nghe
Đồ trang sức
Máy in
Nhà bếp
Điện tử
Nhà bếp
Đồ chơi
Điện
Đồ chơi
Nhà bếp
Điện tử
Đồ chơi
Điện
$69
$113
$181
$14
$79
$67
$205
$45
$13
$199
US1
CAN3
CAN5
US2
CAN2
CAN1
US1
US4
CAN1
CAN3
Đặt hàngKhông
123
ID mục hàng
123
Mặc cảMua hàng
Mặc cảNhà cung cấp