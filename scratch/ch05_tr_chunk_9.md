5-52  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
CÁCH 5.2 
Hợp nhất các bảng với Power Query
Trong trường hợp Beans, mục tiêu là tham gia các bảng Nhân viên và Nhân khẩu học nhân viên. Nếu cả hai 
các bảng có chung khóa chính nên việc nối hoặc hợp nhất rất đơn giản. Nhưng nhân viên
Bảng nhân khẩu học không có khóa chính và có vấn đề khớp giữa 
những cái tên. Hãy cùng khám phá cách giải quyết những vấn đề khác nhau này bằng Power Query.
Những gì bạn cần:  Dữ liệu   Tệp dữ liệu How To 5.2. 
BƯỚC 1: Nếu bạn đang sử dụng Excel, hãy mở tệp và nhấp vào tab Dữ liệu trong menu chính. chọn 
Lấy dữ liệu trong dải băng, sau đó khởi chạy Power Query Editor. Trong Power BI, hãy mở tệp và 
nhấp vào tab Trang chủ trong menu chính. Chọn Chuyển đổi dữ liệu.
	
Trong cả hai trường hợp, Power Query sẽ mở ra. Đảm bảo bạn đã kết nối với BeansEmployee-
Tệp dữ liệu. Tạo kết nối này bằng cách nhấp vào bánh xe bên cạnh Nguồn trong ngăn Các bước áp dụng. 
Trong Đường dẫn tệp, chỉ định vị trí đặt tập dữ liệu trên thiết bị của bạn. Nếu bạn không xác định điều này 
kết nối chính xác, bạn sẽ nhận được thông báo lỗi giống như trong Hình minh họa 5.57.
Làm thế nào để
Bấm vào Cấu hình cột dựa trên 1000 hàng, sau đó chọn Cấu hình cột dựa trên 
toàn bộ tập dữ liệu (Minh họa 5.55).
Cấu hình cột dựa trên 1000 hàng trên cùng
Cấu hình cột dựa trên toàn bộ tập dữ liệu
MINH HỌA 5.55  Sơ đồ cột 
Dựa trên toàn bộ tập dữ liệu
Số liệu thống kê trong Hình minh họa 5.56 sẽ xuất hiện. Điều này là kết quả của việc kiểm tra Cột 
tùy chọn hồ sơ. Trong số những thông tin khác, thông tin được cung cấp bao gồm số hàng và giá trị trung bình
số lượng kiểm soát độ tuổi.
Đếm
Thống kê cột
. . .
Lỗi
trống
khác biệt
duy nhất
NaN
số không
tối thiểu
Tối đa
trung bình
Độ lệch chuẩn
Thậm chí
Lẻ
4.632
0
0
4.632
4.632
0
0
1
4.632
2.316,5
1.337,28...
2.316
2.316
MINH HỌA 5.56  Sơ đồ cột
MINH HỌA 5.57  Kết nối sai với tập dữ liệu
Tập tin
Trang chủ
chuyển đổi
Thêm cột
Xem
Nguồn dữ liệu
Nguồn dữ liệu
Cài đặt
A
Z
Z
A
Sắp xếp
chuyển đổi
kết hợp
Truy vấn [2]
Cài đặt truy vấn
ĐẶC TÍNH
Tên
Tất cả tài sản
Truy vấn
Thuộc tính
Trình chỉnh sửa nâng cao
Quản lý
Làm mới
Xem trước
Tách
Cột
Nhóm
Bởi
Kiểu dữ liệu: Bất kỳ
Sử dụng hàng đầu tiên làm tiêu đề
1 2 Thay thế giá trị
Đóng
Đóng &
Tải
Quản lý
Thông số
Thông số
Nhập dữ liệu
Nguồn mới
Nguồn gần đây
Truy vấn mới
Giảm hàng
Giữ
Hàng
Xóa
Hàng
Quản lý cột
chọn
Cột
Xóa
Cột
Hợp nhất truy vấn
Nối các truy vấn
Kết hợp các tập tin
Nhân khẩu học của nhân viên...
!
Người lao động
!
DataSource.Error: Không thể tìm thấy tệp 'C:\Users\bigda\Dropbox\WILEY\BEANS\DA_CH 05_Apply It 5.2 BeansEmployeeData.xlsx'.
Chi tiết:
     C:\Users\bigda\Dropbox\WILEY\BEANS\DA_CH 05_Áp dụng nó 5.2 BeansEmployeeData.xlsx    
!
Đi đến lỗi
Nhân khẩu học nhân viên
?
Nguồn dữ liệu
Nguồn dữ liệu
Cài đặt
A
Z
Z
A
Sắp xếp
chuyển đổi
kết hợp
Tách
Cột
Nhóm
Bởi
Kiểu dữ liệu: Bất kỳ
Sử dụng hàng đầu tiên làm tiêu đề
1 2 Thay thế giá trị
Quản lý
Thông số
Thông số
Nhập dữ liệu
Nguồn mới
Nguồn gần đây
Truy vấn mới
Giảm hàng
Giữ
Hàng
Xóa
Hàng
Quản lý cột
chọn
Cột
Xóa
Cột
Hợp nhất truy vấn
Nối các truy vấn
Kết hợp các tập tin
Đóng
Đóng &
Tải

![ILLUSTRATION 5.57](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.57.png)

Cách đi qua  5-53
BƯỚC 2: Chọn bảng Nhân viên trong ngăn Truy vấn. Tiếp theo chọn tab Home trong Power 
Menu chính của Truy vấn và chọn Hợp nhất Truy vấn trong nhóm Kết hợp. 
BƯỚC 3: Chọn bảng Nhân khẩu học để kết hợp với bảng Nhân viên.
BƯỚC 4: Chọn FirstName và LastName trong cả hai bảng. Sử dụng Mẫu 6 để phân chia tên 
trong bảng Nhân viên hiện đã được đền đáp!
	
Hình minh họa 5.58 minh họa trực quan cách thực hiện các bước 3, 4 và 5.
MINH HỌA 5.58  Hợp nhất các bảng với Fuzzy Match
Hợp nhất
Chọn một bảng và các cột phù hợp để tạo bảng đã hợp nhất.
nhân viên
ID nhân viên
Tên 1
Họ 2
Chức danh công việc
tỷ lệ
Tình trạng hôn nhân
1
2
3
4
5
Kayne
Ivan
Mick
Juan
Gail
James
lenk
Richards
Lozano
David
nhân viên
Người quản lý
cao cấp
nhân viên
cao cấp
165
250
225
180
218
đã kết hôn
Độc thân
đã kết hôn
Độc thân
Nhân khẩu học nhân viên
Tên 1
Danh sách chứng nhận họ 2
Đại học
vô giá trị
vô giá trị
vô giá trị
Diego
Kim
Marcus
Gail
Shiela
Asare
bụi cây
Đất sét
David
kim cương
CPA
CPA, CMA, CFA
Đại học bang Grand Valley
Đại học Delaware
Đại học bang Michigan
Đại học Michigan
Đại học bang Michigan
Tham gia loại
Bên ngoài bên trái (tất cả từ thứ nhất, khớp từ thứ hai)
Sử dụng kết hợp mờ để thực hiện hợp nhất
Hủy bỏ
được rồi
4
4
3
Tùy chọn kết hợp mờ
Ngưỡng tương tự (tùy chọn)
0,4
tôi
tôi
Bỏ qua trường hợp
Khớp bằng cách kết hợp các phần văn bản
5
5
BƯỚC 5: Để giải quyết các vấn đề về dữ liệu do biệt hiệu, lỗi đánh máy và tên bị đảo ngược, hãy nhấp vào 
hộp kiểm Sử dụng kết hợp mờ để thực hiện hợp nhất. So khớp mờ là một thuật toán 
đo lường sự tương đồng giữa hai bộ giá trị. Ngưỡng tương tự xác định 
các giá trị cần phải giống nhau đến mức nào để chúng khớp với nhau. Để khớp hoàn toàn cả hai bộ ở đây, 
ngưỡng nên được hạ xuống 0,4. Nhấn OK để thực hiện việc ghép.
BƯỚC 6: Như minh họa trong Hình 5.59, một cột mới được thêm vào bảng Nhân viên 
là kết quả của việc hợp nhất: Nhân khẩu học nhân viên. Tất cả các giá trị trong cột này hiển thị 
Bảng làm giá trị. Tiếp theo, nhấp vào góc trên bên phải của cột: 
• Power Query sẽ cho phép bạn chọn bất kỳ cột nào từ bảng Nhân khẩu học nhân viên 
và thêm nó vào bảng Nhân viên. Bỏ chọn cột FirstName và LastName 
và giữ các cột Danh sách chứng nhận và Đại học. 
• Bỏ chọn Sử dụng tên cột gốc làm tiền tố. Thao tác này sẽ xóa Nhân viênDemo-
đồ họa từ tên cột Danh sách Chứng nhận và Trường Đại học.
Đến đây là bạn đã gộp thành công hai bảng thành một.
MINH HỌA 5.59  Chọn dữ liệu từ 
Bảng đã hợp nhất
Nhân khẩu học nhân viên
6
Bảng
Bảng
Bảng
Bảng
Bảng

![ILLUSTRATION 5.59](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.59.png)

5-54  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
BƯỚC 7: Chỉ cần có bảng Nhân viên cho mục đích phân tích. Hình minh họa 5.60 cho thấy 
cách hướng dẫn Power Query không tải bảng. Nhấp chuột phải vào Nhân khẩu học nhân viên 
và bỏ chọn hộp kiểm trước Enable Load. Các bảng không được tải vào phần phân tích 
cơ sở dữ liệu được hiển thị in nghiêng. Lưu ý: Tùy chọn này chỉ có trong power BI, không có trong Excel
CÁCH 5.3 
Triển khai tính toàn vẹn tham chiếu với Microsoft Access
Để cải thiện chất lượng dữ liệu, tính toàn vẹn tham chiếu được triển khai tốt nhất ở cấp nhập dữ liệu. dữ liệu-
phần mềm cơ bản như Microsoft Access giúp việc này trở nên dễ dàng.
Những gì bạn cần:  Dữ liệu   Tệp How To 5.3. 
BƯỚC 1: Cơ sở dữ liệu Microsoft Access chứa các bảng Nhà cung cấp và Mua hàng: 
• Như minh họa trong hình 5.61, mối quan hệ giữa hai bảng được xác định giữa 
trường ID trong bảng Nhà cung cấp và trường Nhà cung cấp trong bảng Mua hàng. 
• Phần dưới của Hình minh họa 5.61 cho thấy khi tạo mối quan hệ này (bằng cách kéo 
trường nhà cung cấp vào bảng Mua hàng hoặc ngược lại), Microsoft Access cung cấp 
tùy chọn Thực thi tính toàn vẹn tham chiếu.
Làm thế nào để
MINH HỌA 5.60  Chọn các bảng không nên tải
Truy vấn [4]
khách hàng
Nhân khẩu học nhân viên
nhân viên
Dịch vụ
1
2
3
4
5
6
7
Kayne
Ivan
Sao chép
Dán
Xóa
Đổi tên
Kích hoạt tải
Đưa vào làm mới báo cáo
Tên đầu tiên
ABC
7
MINH HỌA 5.61  Thực thi 
Tính toàn vẹn tham chiếu với Microsoft 
Truy cập
Chỉnh sửa mối quan hệ
?
Bảng/Truy vấn:
Bảng/Truy vấn liên quan:
Thực thi tính toàn vẹn tham chiếu
Các trường liên quan đến cập nhật Cascade
Xếp tầng Xóa các bản ghi liên quan
Loại mối quan hệ:
Một-nhiều
nhà cung cấp
ID
Tên
Mua hàng
Mã
Ngày
nhà cung cấp
chọn
“Thực thi
tài liệu tham khảo
Chính trực”
Tùy chọn
Hủy bỏ
Tạo mới..
Tạo
Tham gia loại..

![ILLUSTRATION 5.61](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.61.png)

Câu hỏi trắc nghiệm  5-55
BƯỚC 2: Hình minh họa 5.62 minh họa điều gì sẽ xảy ra nếu bạn chọn tùy chọn này. Bảng điều khiển (A) 
hiển thị tất cả các nhà cung cấp hiện có. Bảng (B) hiển thị điều gì sẽ xảy ra nếu bạn cố gắng thêm một đối tượng không tồn tại 
nhà cung cấp—nhà cung cấp có ID 6—vào bảng Mua hàng. Access tạo ra lỗi ngăn cản bạn 
nhập vào nhà cung cấp không hợp lệ.
ID
Tên
Billy
namsun
Esmeralda
Cassius
Carol
1
2
3
4
5
Mã
Ngày
nhà cung cấp
Bấm để thêm
L122
2/1/2023
U18
3/1/2023
1
6
Truy cập Microsof
Bạn không thể thêm hoặc thay đổi bản ghi vì bản ghi liên quan được yêu cầu trong bảng 'Nhà cung cấp'.
!
được rồi
Trợ giúp
Nhập một không-
Nhà cung cấp hiện tại
Thông báo lỗi
Được tạo bởi
Truy cập
(A)
(B)
MINH HỌA 5.62  Nhập nhà cung cấp không hợp lệ
Dữ liệu   Thẻ Dữ liệu xuất hiện khi dữ liệu để trả lời một câu hỏi hoặc hoàn thành một bài tập 
có sẵn trên nền tảng học tập trực tuyến của Wiley. 
Câu hỏi trắc nghiệm
1.  (LO 1)  Thuật ngữ nào sau đây mô tả quá trình lập hồ sơ, làm sạch, tái cơ cấu và 
tích hợp dữ liệu trước khi xử lý và phân tích?
Một.	 Hồ sơ dữ liệu
b.	 Chuẩn bị dữ liệu
c.	 Truy vấn dữ liệu
d.	 Phân tích dữ liệu
2.  (LO 1)  Hao, nhà phân tích các khoản phải thu, đang xem xét hồ sơ khách hàng chính để sử dụng trong phân tích-
dự án ysis Anh ấy nhận thấy rằng trong trường Địa chỉ, trạng thái của một khách hàng được liệt kê là NM, trong khi một khách hàng khác 
Tiểu bang của khách hàng được liệt kê là New Mexico. Điều nào sau đây là đúng?
Một.	 Hao đã xác định một trường hợp dữ liệu không chính xác.
b.	 Hao đã xác định một trường hợp dữ liệu không hợp lệ.
c.	 Hao đã xác định được một trường hợp dữ liệu không nhất quán.
d.	 Hao đã xác định được một trường hợp dữ liệu không lớn.
3.  (LO 1)  Spencer, nhà phân tích tài chính tại một cửa hàng quần áo thể thao, đang chuẩn bị một hồ sơ tổng thể về tất cả các chuyên gia 
người phát ngôn thể thao của công ty. Dựa vào bảng để xác định khẳng định nào sau đây là đúng:
Người phát ngôn
Tên
thể thao
Bharat Arun, Bowling
Bharat Arun
Bowling
Ramakrishnan Sridhar, Fielding
Ramakrishnan Sridhar
Bảo vệ
Virat Kohli, Người dơi
Virat Kohli
Người đánh bóng
Rohit Sharma, Người dơi
Rohit Sharma
Người đánh bóng
một.	 Cột Người phát ngôn chứa dữ liệu không chính xác, trong khi cột Tên chứa dữ liệu không hợp lệ.
b.	 Người phát ngôn là cột có giá trị đơn, trong khi Tên là cột tổng hợp.
c.	 Người phát ngôn là một cột tổng hợp, trong khi Tên là cột có một giá trị.
d.	 Người phát ngôn đại diện cho một cột tổng hợp, trong khi Tên và Thể thao đại diện cho các cột được cắt lát.

![ILLUSTRATION 5.62](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.62.png)

5-56  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
4.  (LO 1)  Phát biểu nào sau đây về lược đồ sao là sai?
Một.	 Bảng sự kiện thể hiện các giao dịch kinh doanh.
b.	 So với bảng dữ kiện, bảng thứ nguyên thường có ít phiên bản hơn và nhiều cột hơn.
c.	 Để làm cho việc cắt dữ liệu dễ dàng hơn, hầu hết các thước đo được xác định như một phần của bảng thứ nguyên.
d.	 Bảng thứ nguyên được sử dụng để phân tích cái gì, khi nào và ai.
đ.	 Hạt đại diện cho mức độ chi tiết của một bảng dữ kiện.
5.  (LO 2)  Câu nào sau đây về chuyển đổi dữ liệu là đúng?
1. Chuyển đổi dữ liệu có ba quy trình con: làm sạch, tái cấu trúc và tích hợp.
2. Việc dọn dẹp nhằm mục đích khắc phục những bất thường về dữ liệu.
3. Tái cấu trúc không thay đổi bất kỳ dữ liệu nào mà chỉ thay đổi cách chúng được tổ chức.
4. Tích hợp liên kết dữ liệu với nhau bằng cách xác định mối quan hệ.
Một.	 1 và 2
b.	 1 và 3
c.	 1, 2 và 4
d.	 1, 2, 3 và 4
6.  (LO 2)  Làm sạch dữ liệu có thể bao gồm việc thêm, sửa đổi và xóa dữ liệu. Trong trường hợp nào sau đây 
Ví dụ: Việc sửa đổi dữ liệu có cần thiết không?
Một.	 Tệp đơn đặt hàng bị thiếu một tháng đơn đặt hàng.
b.	 Bạn đang chuẩn bị phân tích xem có bao nhiêu đơn đặt hàng lớn hơn 500 USD. Tập tin bạn 
đang làm việc có một hàng vào đầu mỗi tháng mới với tên tháng được liệt kê trong 
cột ngày tháng. Không có dữ liệu nào khác trong hàng có tên tháng.
c.	 Trong khi kiểm tra dữ liệu đơn đặt hàng, bạn lưu ý rằng tên nhà cung cấp, địa chỉ đường phố, thành phố 
và trạng thái được liệt kê trong các cột riêng biệt. Trong một số trường hợp, cột trạng thái hiển thị tên trạng thái, 
trong các trường hợp khác, chữ viết tắt của tiểu bang được hiển thị. 
d.	 Trong quá trình phân tích các đơn đặt hàng, bạn lưu ý rằng một số đơn đặt hàng bao gồm nhà cung cấp 
số điện thoại. 
7.  (LO 3)  Việc xác thực việc truyền dữ liệu được thực hiện bằng cách so sánh dữ liệu nguồn với dữ liệu trong công cụ ETL. 
Phát biểu nào sau đây về truyền dữ liệu là sai?
Một.	 Số lượng hàng giúp xác thực tính đầy đủ của việc truyền dữ liệu.
b.	 Phân tích khoảng cách trình tự giúp xác thực tính đầy đủ của việc truyền dữ liệu.
c.	 So sánh mức trung bình của một trường số giúp xác thực tính chính xác của việc truyền dữ liệu.
d.	 Việc so sánh các tiêu đề cột giúp xác thực tính đầy đủ và chính xác.
đ.	 So sánh tổng các trường số giúp xác thực tính chính xác của việc truyền dữ liệu.
8.  (LO 3)  Bạn đang chuẩn bị phân tích các nhà cung cấp và đơn đặt hàng và đã chuyển dữ liệu từ 
hệ thống ERP cho tất cả các đơn đặt hàng trong năm qua và dữ liệu cho tất cả các nhà cung cấp. Bạn đã ủng hộ
được cung cấp các thông tin sau về dữ liệu:
1
Tổng số đơn đặt hàng
15.786
2
Tổng số đơn đặt hàng
$1,567,679
3
Số lượng đơn đặt hàng trung bình
99,31 USD
4
Tổng số nhà cung cấp
672
Thông tin nào có liên quan để đảm bảo chuyển tất cả dữ liệu?
Một.	 1 và 2
b.	 2 và 3
c.	 1 và 4
d.	 1, 2, 3 và 4
9.  (LO 4)  Lizelle là nhà phân tích tài chính đang chuẩn bị cơ sở dữ liệu phân tích để phân tích dữ liệu sản xuất 
để xác định các quy trình hiệu quả nhất. Cô ấy hiện đang xác định những dữ liệu không liên quan và không đáng tin cậy trong 
các cột trong một bảng. Câu trả lời nào sau đây là phù hợp nhất khi cô ấy xác định 
dữ liệu không liên quan hoặc không đáng tin cậy?
Một.	 Xóa cột có dữ liệu không liên quan hoặc không đáng tin cậy.
b.	 Từ bỏ dự án vì dữ liệu không hợp lệ và không thể phân tích được.
c.	 Bỏ xoay cột để dữ liệu được tách thành các trường riêng biệt.
d.	 Đặt dữ liệu có liên quan, không liên quan, đáng tin cậy và không đáng tin cậy vào các cột riêng biệt.

Câu hỏi trắc nghiệm  5-57
10.  (LO 4)  Hofflak là một công ty xây dựng lớn ở Tây Bắc Hoa Kỳ. Hệ thống ERP của họ theo dõi 
toàn bộ tài sản của họ. Từ điển dữ liệu cho bảng tài sản trông như sau:
Tài sản
Tên
Mô tả
ID
ID duy nhất của một nội dung.
Mô tả
Mô tả của một tài sản.
Danh mục tài sản
Danh mục của một tài sản.
Giá
Giá phải trả cho tài sản.
Salvam
Giá trị sổ sách ước tính của tài sản vào cuối thời gian sử dụng hữu ích của nó.
Ước tínhTuổi thọ
Tuổi thọ ước tính của một tài sản.
Phương thức Dpr
Phương pháp khấu hao áp dụng cho tài sản.
Bạn sẽ thay đổi tên cột nào cho mục đích phân tích dữ liệu?
Một.	 ID, Salvam, DprMethod
b.	 ID, Giá, Thời gian tồn tại ước tính, Phương thức Dpr
c.	 Giá, Salvam, Thời gian ước tính, DprMethod
d.	 Danh mục tài sản, Giá
đ.	 Salvam, Thời gian sống ước tính, DprMethod
f.	 Ước tínhthời gian tồn tại, DprMethod
11.  (LO 4)  Để cơ cấu lại cột tổng hợp, bạn nên
một.	 loại bỏ dữ liệu cột không cần thiết.
b.	 chia dữ liệu cột thành các cột riêng biệt.
c.	 tạo một bảng riêng.
d.	 di chuyển cột sang bảng khác. 
12.  (LO 4)  Courtier là một cửa hàng bán đồ xa xỉ cao cấp chuyên thiết kế và sản xuất đồng hồ và trang sức 
và bán chúng trên toàn thế giới. Bảng này cung cấp một mẫu nhỏ thông tin khách hàng mà họ theo dõi. Họ 
có một chương trình khách hàng thân thiết rất đơn giản. Khách hàng đạt được trạng thái “kim cương” nếu họ mua nhiều hơn 
Sản phẩm trị giá 10.000.000 USD, trạng thái "vàng" nếu họ đã mua với giá hơn 1.000.000 USD và trạng thái "không" 
nếu họ mua ít hơn 1.000.000 USD.
Khách hàng
Mã
Trạng thái trung thành
Quốc gia
1
kim cương
Hoa Kỳ
2
Vàng
Ý
3
không áp dụng
Hoa Kỳ
4
Vàng
Dựa trên thông tin được cung cấp cho bạn, bạn sẽ mô tả các vấn đề của tập dữ liệu này như thế nào?
Một.	 Không đúng, không nhất quán, không đầy đủ, không hợp lệ
b.	 Không nhất quán, không đầy đủ, không hợp lệ
c.	 Không nhất quán, không hợp lệ
d.	 Không đầy đủ, không hợp lệ
13.  (LO 5)  Câu nào sau đây đúng về việc thiết lập khóa chính trong bảng?
Một.	 Khóa chính phải sử dụng cùng tiêu đề cột trong tất cả các bảng liên quan.
b.	 Khóa chính phải có một giá trị duy nhất cho mỗi hàng và không có giá trị null.
c.	 Khóa chính và khóa ngoại là những thông tin giống hệt nhau được lặp lại trong cùng một bảng.
d.	 Nếu một bảng không có khóa chính thì nó không thể được đưa vào cơ sở dữ liệu phân tích.