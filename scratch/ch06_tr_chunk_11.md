6-62  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
EX 6.11  (LO 2, 3)  Dữ liệu   Kế toán tài chính   Tạo mô hình thông tin cho dòng tiền 
Phân tích Valentina Turner sở hữu The Blue Ballroom, một phòng tập khiêu vũ ở Nevada. Cô ấy có một 
bảng tính ghi lại các khoản thu, chi từ đầu năm (2025). các 
cấu trúc của tập dữ liệu được hiển thị ở đây.
Chuyển tiềnLời khuyên
Số
Biên nhận tiền mặt
Bảng sự kiện
Bảng kích thước
Bảng sự kiện
Giải ngân
Số chứng từ
Số tiền
Ngày
ngân hàng
Số tiền
ngân hàng
Ngày
Tiền mặtGiải ngân
N
N
1
1
Mã Ngân Hàng
Tên ngân hàng
Số dư ban đầu
Tiền mặt
Chìa khóa
Cột
Cô ấy muốn sử dụng bảng tóm tắt ở đây để thể hiện dòng tiền tổng thể và dòng tiền 
cho mỗi tài khoản trong số ba tài khoản ngân hàng của cô ấy.
Fulton
MTB
PNC
23.009
89.012
44.099
Tên ngân hàng
Số dư ban đầu
953,34
2.116,00
2.408,04
$
$
$
Dòng vào
1.148,36
900,23
2.987,36
$
$
$
22.813,98
90.227,77
43.519,68
$
$
$
Tổng cộng
156.120 USD 5.477,38 USD 5.035,95 USD
156.561,43 USD
Dòng chảy ra
Số dư khách hàng
$ 
$ 
$ 
	 1. Tạo mô hình thông tin.
	 2. Tạo báo cáo.
EX 6.12  (LO 2, 3)  Dữ liệu   Kế toán quản lý   Tạo mô hình thông tin cho nhân viên 
Băng chuyền phân tích hiệu suất là một công ty khởi nghiệp về dịch vụ chia sẻ xe nhằm mục đích cạnh tranh với các công ty 
như Uber và Lyft ở Mỹ. Sử dụng nhiều quảng cáo địa phương, họ đã chạy một chương trình thí điểm trong thời gian đầu tiên 
cuối tuần của tháng Hai tại khu vực Seattle. Biểu đồ hiển thị dữ liệu họ đã thu thập.
Bảng sự kiện
Bảng kích thước
RideID
đi xe
N
1
tham gia
Chìa khóa
Cột
Thời gian ước tính
Thời gian thực tế
Số tiền
Mẹo
Đánh giá
Người lái xe
ID tài xế
Người lái xe
Tên tài xế
Từ điển dữ liệu cung cấp mô tả ngắn gọn cho từng trường.
đi xe
Tên
Mô tả
RideID
Một ID xác định duy nhất một chuyến đi.
Thời gian ước tính
Thời gian ước tính của chuyến đi tính bằng phút.
Thời gian thực tế
Thời gian thực tế của chuyến đi tính bằng phút.
Số tiền
Số tiền được trả cho chuyến đi.
Mẹo
Số tiền boa mà người lái xe nhận được khi đi xe.
(Tiếp theo)

Tên
Mô tả
Đánh giá
Đánh giá của khách hàng về chuyến đi theo thang điểm từ một đến năm, 
với năm là xuất sắc.
Người lái xe
ID của người lái xe.
Người lái xe
Tên
Mô tả
ID tài xế
Một ID xác định duy nhất một trình điều khiển.
Tên tài xế
Tên của người lái xe.
	 1. Giám đốc điều hành của Carousel yêu cầu bạn phát triển một mô hình thông tin giúp phân tích hiệu suất của tài xế.
mance. Phát triển ít nhất ba biện pháp.
	 2. Tiếp theo, tạo ít nhất hai báo cáo sử dụng mô hình thông tin bạn đã phát triển.
EX 6.13  (LO 2, 3)  Dữ liệu   Kế toán tài chính   Tạo mô hình thông tin cho doanh thu 
Phân tích Jane Jones (JJ) vừa mở một xe bán đồ ăn nhỏ, Gourmet@5, trên Đại lộ số 5 ở Thành phố New York. 
Thực đơn rất đơn giản, bao gồm bánh mì kẹp thịt, xúc xích, chai nước và nhiều loại soda và kẹo. 
Cô ấy đưa cho bạn một bảng tính chứa tất cả các giao dịch trong tuần đầu tiên từ thứ Hai đến 
Chủ nhật. Sơ đồ cho thấy dữ liệu nào được thu thập.
Bảng sự kiện
Bảng kích thước
Mã hàng
Mặt hàng
N
1
Dòng chảy
(ra)
Chìa khóa
Cột
bán hàng
ID giao dịch
ngày
Mục
số lượng
Tên mặt hàng
Mặt hàngGiá
MụcDanh mục
Từ điển dữ liệu cung cấp mô tả ngắn gọn cho từng trường.
bán hàng
Tên
Mô tả
ID giao dịch
Một ID được sử dụng để xác định giao dịch.
ngày
Ngày trong tuần xảy ra giao dịch.
Mục
Mặt hàng bán cho khách hàng (mã số).
số lượng
Số lượng mặt hàng đã bán.
Mặt hàng
Tên
Mô tả
Mã hàng
Mã xác định duy nhất một loại sản phẩm.
Tên mặt hàng
Tên mặt hàng (loại sản phẩm).
Mặt hàngGiá
Giá của mặt hàng. Tất cả các mặt hàng đều có giá cố định.
MụcDanh mục
Danh mục của mặt hàng.
	 1. Phát triển mô hình thông tin giúp phân tích doanh số bán hàng trong tuần đầu tiên. Đặc biệt là chủ sở hữu 
quan tâm đến việc biết sản phẩm nào tạo ra nhiều doanh thu nhất.
	 2. Tạo ít nhất hai báo cáo bằng mô hình thông tin bạn đã tạo.
Bài tập  6-63

6-64  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
Dữ liệu EX 6.14  (LO 2, 3)  Tạo mô hình thông tin để phân tích hiệu suất của nhân viên 
Giuseppina's là một cửa hàng pizza nổi tiếng do gia đình sở hữu ở Bourbon, Missouri. Chủ cửa hàng có col-
đã đưa ra các thông tin sau về tất cả các đợt giao hàng vào ngày 14 tháng 2 năm 2025: số đơn hàng, tài xế, 
số tiền đặt hàng và số tiền tip mà tài xế nhận được. Chủ sở hữu muốn xếp hạng các trình điều khiển dựa trên 
hai tiêu chí:
•  Tổng số tiền tip nhận được.
•  Tỷ lệ phần trăm tiền boa trung bình nhận được.
	 1. Phát triển mô hình thông tin cho việc phân tích đó.
	 2. Sử dụng mô hình thông tin để tạo bảng cho mỗi thứ hạng hiển thị tên các tài xế.
Trường hợp ứng dụng chuyên nghiệp: D*Tunes
D*Tunes là một studio khiêu vũ ở Pocatello, Idaho. Chủ sở hữu studio đã thu thập dữ liệu liên quan đến 
doanh thu dạy học của studio vào tháng 1 năm 2025. Bạn đang thực tập với họ với vai trò kế toán. Chủ sở hữu có một 
loạt câu hỏi có thể được trả lời bằng cách sử dụng dữ liệu đã được cung cấp cho bạn. Bạn đã có rồi 
đã phát triển từ điển dữ liệu và mô hình dữ liệu cho tập dữ liệu.
Từ điển dữ liệu D*Tunes
Giảng viên
Tên cột
Mô tả trường
ID giảng viên
Một ID xác định duy nhất một người hướng dẫn.
Tên giảng viên
Tên của một người hướng dẫn.
Số Giờ Dạy
Số giờ một người hướng dẫn đã dạy cho D*Tunes.
SốGiải Thưởng
Số lượng giải thưởng địa phương và khu vực mà một giảng viên có được 
nhận được trong ba năm qua.
SốGiải ThưởngQuốc Gia
Số lượng sự công nhận quốc gia mà một người hướng dẫn đã nhận được.
Mức lương
Đối với nhân viên toàn thời gian, mức lương mà người hướng dẫn kiếm được.
Chức danh công việc
Chức danh của người hướng dẫn.
Lớp học
Tên cột
Mô tả trường
Mã lớp
Mã xác định duy nhất một lớp.
Mô tả lớp
Một mô tả ngắn gọn về lớp học.
Sinh viên
Tên cột
Mô tả trường
ID sinh viên
Một ID xác định duy nhất một học sinh.
Tên sinh viên
Tên của một học sinh.
Cấp độ
Trình độ kỹ năng của học sinh: 
B = Người mới bắt đầu 
Tôi = Trung cấp 
A = Nâng cao
Giới tính
Giới tính của học sinh.

Chìa khóa
Cột
Khóa ngoại
Tên giảng viên
Chức danh công việc
SốGiải Thưởng
Số Giờ Dạy
SốGiải ThưởngQuốc Gia
Mức lương
Giảng viên
Mã lớp
Mô tả lớp
Lớp học
1
1
N
N
N
1
1
N
ID giảng viên
Tên sinh viên
Cấp độ
Giới tính
Sinh viên
ID sinh viên
tham gia
Bài học
sinh viên
lớp học
Người hướng dẫn
Ngày
Bài học
ID bài học
Bài học
Tên cột
Mô tả trường
ID bài học
Một ID xác định duy nhất một bài học.
Ngày
Ngày mà bài học diễn ra.
lớp học
Loại lớp học được dạy trong bài học này.
Người hướng dẫn
ID của người hướng dẫn dạy lớp này.
tham gia
Tên cột
Mô tả trường
Bài học
ID của bài học mà học sinh đã học.
sinh viên
ID của học sinh tham gia bài học.
Trường hợp ứng tuyển chuyên nghiệp: D*Tunes  6-65

6-66  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
PAC 6.1  Kế toán tài chính: Phân tích khả năng sinh lời của D*Tunes
Dữ liệu   Kế toán tài chính   D*Tunes có bốn loại người hướng dẫn:
• Người học việc.
•	 Trung cấp.
•	 Trình độ cao.
• Vô địch.
Các quy tắc sau đây được sử dụng để chỉ định người hướng dẫn vào danh mục của họ.
• Giáo viên dạy dưới 250 giờ là người học nghề.
• Giảng viên đã dạy trên 250 giờ được coi là trung cấp.
• Giảng viên trung cấp đã giành được ít nhất ba giải thưởng, từ danh sách được phê duyệt của địa phương và 
các giải đấu khu vực trong ba năm qua được coi là nâng cao.
• Những giảng viên đã được công nhận cấp quốc gia, từ danh sách các giải thưởng có uy tín cao, là những người có đẳng cấp-
được coi là nhà vô địch.
Lương của người hướng dẫn được xác định theo hạng mục của họ:
người học việc
Trung cấp
Nâng cao
Nhà vô địch
Danh mục
Tỷ lệ hàng giờ
45
65
85
$110
$
$
$
Tỷ lệ theo giờ này áp dụng cho bất kỳ lớp nào mà người hướng dẫn dạy: lớp bắt đầu, lớp riêng hoặc lớp. Ngoại lệ duy nhất-
Đó là các bữa tiệc tối thứ Sáu, trong đó người hướng dẫn được trả 250 USD. Cái giá mà sinh viên phải trả là 
mức lương theo giờ của người hướng dẫn cộng thêm $30. Vì vậy, đối với một giờ học với người học việc, sinh viên phải trả 75 USD. Đối với một 
một giờ học với một nhà vô địch, học sinh phải trả 140 USD. Tỷ lệ tiêu chuẩn cho bất kỳ buổi học nhóm nào (đu dây, 
cha-cha, v.v.) là $40 một người. Vé vào bữa tiệc thứ Sáu hàng tuần là 25 USD. Mỗi học sinh nhận được một 
bài học khai giảng miễn phí.
	 1. Phát triển mô hình thông tin cho phép bạn xác định lợi nhuận gộp của tháng trước. Khi nào 
tính toán lợi nhuận gộp, chi phí duy nhất cần xem xét là số tiền người chủ trả cho người hướng dẫn. Đừng 
bao gồm tiền lương trả cho nhân viên toàn thời gian. 
	 2. Tạo một báo cáo hiển thị tổng lợi nhuận gộp được tạo ra, lợi nhuận gộp được tạo ra trên mỗi lớp và tổng lợi nhuận gộp 
lợi nhuận được tạo ra trên mỗi người hướng dẫn.
Kiểm toán PAC 6.2 : Phân tích gian lận tiềm ẩn
Chính sách của Data   Auditing   D*Tunes là khách hàng tiềm năng có thể có một bài học bắt đầu miễn phí. Làm thế nào-
bao giờ hết, người hướng dẫn vẫn được trả tiền cho những bài học này. Chủ sở hữu không muốn thay đổi chính sách này, nhưng dưới
cho rằng nó tạo cơ hội cho gian lận. Bạn được yêu cầu phân tích bốn câu hỏi sau đây.
Xây dựng mô hình thông tin để khám phá từng câu hỏi. Sau đó, tạo một báo cáo cho từng người trong số họ.
	 1. Chi phí của các bài học khởi đầu là bao nhiêu. Những khoản đầu tư nào đã được thực hiện cho đến nay?
	 2. Có học sinh nào đã học nhiều hơn một bài học nhập môn không?
	 3. Có giáo viên nào có số buổi học nhập môn cao bất thường không?
	 4. Tỷ lệ chuyển đổi là bao nhiêu? Tức là có bao nhiêu học sinh đăng ký tham gia khóa nhập môn cũng 
cuối cùng đã trả tiền cho một buổi học hay một bữa tiệc tối thứ sáu?
PAC 6.3  Kế toán quản lý: Tạo phân tích hòa vốn của các nhóm nhóm
Dữ liệu   Kế toán quản lý   Chính sách của D*Tunes là chỉ giữ các lớp nhóm khi có mạng 
doanh thu ít nhất là 150 USD sau khi trả tiền cho người hướng dẫn. Hiện nay, mức giá sinh viên phải trả cho lớp học nhóm 
là 40 đô la. Hãy khám phá hai câu hỏi sau đây.
	 1. Tạo mô hình thông tin để xác định số lượng học sinh cần thiết cho mỗi buổi học để hòa vốn, 
và bài học nào chưa đạt được mục tiêu đó.
	 2. Tạo một báo cáo cho biết lớp nào không đạt điểm hòa vốn. Những lớp học nào sẽ 
bạn đề nghị hủy bỏ?

Trường hợp tiếp theo của LeGrind: Xây dựng mô hình thông tin cho 
Tính lợi nhuận gộp
dữ liệu
Truy cập nền tảng học tập trực tuyến của Wiley để biết thông tin cơ bản về trường hợp, các câu hỏi, dữ liệu bổ sung và 
biết thêm chi tiết về vụ án đang tiếp tục. 
Trường hợp tiếp theo của LeGrind: Xây dựng mô hình thông tin để tính lợi nhuận gộp 6-67
 Kế toán thuế PAC 6.4: Xác định khoản khấu trừ cho nhân viên được trả lương 
dữ liệu
Kế toán thuế
Đối với hai nhân viên làm công ăn lương, D*Tunes phải giữ lại giấy tờ của người sử dụng lao động.
thuế FICA hàng tháng từ tiền lương của họ.  Thuế FICA là sự kết hợp giữa thuế An sinh xã hội và 
Thuế Medicare.  Thuế suất FICA năm 2025 là 7,65%, bao gồm thuế An sinh xã hội là 6,2% và Medicare 
thuế 1,45%. Chủ sở hữu không cần khấu trừ thuế An sinh xã hội đối với bất kỳ khoản thu nhập nào trên 168.900 USD. 
Vì vậy, hãng phim chỉ phải khấu trừ thuế Medicare đối với số tiền lương vượt quá số tiền này.  Tạo một thông tin-
mô hình sẽ cho phép bạn thiết kế một bảng tính tương tự như bảng tính được hiển thị sẽ giúp ích cho studio
xác định các khoản thanh toán thuế FICA cho mỗi tháng.
tháng Giêng
tháng hai
tháng ba
tháng tư
tháng 5
Mức lương
FICA%
An sinh xã hội%
% Medicare
An ninh xã hộiTối đa
200.000
0,0765
0,062
0,0145
168.900
tháng sáu
tháng bảy
tháng Tám
tháng chín
tháng mười
tháng mười một
tháng mười hai
1.275,00
1.275,00
1.275,00
1.275,00
1.275,00
1.275,00
1.275,00
1.275,00
1.275,00
1.275,00
380,13
241,67
Tháng
Khấu trừ