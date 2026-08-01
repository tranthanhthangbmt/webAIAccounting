5.1  Lập hồ sơ dữ liệu là gì?  5-7
Hình minh họa 5.4 (B) hiển thị dữ liệu tương tự bằng cách sử dụng cấu trúc phẳng. Carlos, Elodie, Jane và Jim 
đã trở thành giá trị của cột Nhân viên bán hàng. Chúng có thể được sử dụng để lọc và hoạt động theo nhóm
ations. Bạn thích bảng ở ô (A) hay bảng ở ô (B) để trả lời một câu hỏi 
như “Jane và Jim đã bán được bao nhiêu chiếc Mustang?” Cấu trúc phẳng trong Hình minh họa 5.4 (B) 
giúp phân tích dễ dàng hơn vì chúng tôi có thể lọc theo nhân viên bán hàng và sau đó tính tổng các giá trị trong 
Cột Đơn vị đã bán.
Mô hình dữ liệu giúp phân tích dễ dàng hơn
Mô hình dữ liệu xác định cách các bảng khác nhau liên quan với nhau. Các mô hình dữ liệu phân tích nên 
dễ hiểu đối với người dùng doanh nghiệp như kế toán viên và máy tính có thể 
để xử lý chúng một cách hiệu quả. Cấu trúc được đề xuất cho các mô hình dữ liệu phân tích là 
lược đồ sao, có cả hai đặc điểm (Minh họa 5.5). Là đầu của Hình minh họa 5.5 
cho thấy, lược đồ hình sao bao gồm hai loại bảng, bảng sự kiện và bảng thứ nguyên, và 
mối quan hệ giữa chúng.
MINH HỌA 5.5  Lược đồ hình sao
ngày
Ngày trong tuần
Tháng
Năm
Ngày
ID nhân viên bán hàng
Tên đầu tiên
Họ
Sở
Tên
Nhân viên bán hàng
Bảng kích thước
Bảng sự kiện
Bảng kích thước
Mã sản phẩm
Tên
Mô tả
ID danh mục
Tên danh mục
Chi phí
sản phẩm
ID khách hàng
Tên
đường phố
Thành phố
Mã zip
tiểu bang
Email
Giới tính
Trạng thái
Nghề nghiệp
Địa chỉ
Khách hàng
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
Khách hàng
Nhân viên bán hàng
Hóa đơnKhông
Giá
số lượng
Số tiền
Dòng hóa đơnKhông
Tổng số lượng đã bán
Tổng doanh sốSố tiền
Tổng lợi nhuận
bán hàng
Chìa khóa
Cột
Cột được tính toán
Đo lường
Khóa ngoại
Mối quan hệ
Bảng sự kiện 
Trong bối cảnh kế toán, các sự kiện tương ứng với các giao dịch kinh doanh như 
như đơn đặt hàng, bán hàng, mua hàng và thanh toán. Bảng sự kiện ở giữa Hình minh họa 5.5 
chứa dữ liệu bán hàng. Dữ liệu trong bảng sự kiện được thu thập ở mức độ chi tiết cao để tránh 
áp đặt các ràng buộc bổ sung cho việc phân tích. (Mức độ chi tiết được gọi là hạt.) 
Trong Hình minh họa 5.5, hạt là một dòng hóa đơn, là một sản phẩm cụ thể được vận chuyển đến một địa điểm cụ thể. 
khách hàng, vào một ngày cụ thể và liên quan đến một nhân viên bán hàng cụ thể.

![ILLUSTRATION 5.5](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.5.png)

5-8  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
MINH HỌA 5.6  Các biện pháp cắt lát theo kích thước
Tổng số tiền bán hàng là bao nhiêu (đô la)
cho một khách hàng cụ thể?
1
Tổng số tiền bán hàng là bao nhiêu (đô la)
cho tất cả khách hàng ở một tiểu bang cụ thể?
2
Tổng số lượng bán được của một
sản phẩm cụ thể?
3
Tháng nào có tổng số tiền cao nhất
số tiền bán hàng (đô la)?
4
Tổng số tiền bán hàng là bao nhiêu (đô la)
cho một sản phẩm cụ thể cho một sản phẩm cụ thể
khách hàng?
5
Doanh số bán hàng hàng tháng như thế nào?
tổng số lượng bán được cho một mặt hàng cụ thể
sản phẩm, dao động?
6
Người bán hàng với
tổng doanh thu cao nhất (đô la)
cho một sản phẩm cụ thể?
7
Tổng số lượng bán được của một
sản phẩm cụ thể trong một tháng cụ thể
ở một trạng thái cụ thể?
8
Kích thước
Biện pháp
Mặc dù số lượng hàng trong bảng chiều thường nhỏ nhưng chúng thường có nhiều 
cột. Bảng chiều Khách hàng trong Hình minh họa 5.5 có 10 cột nhưng không có thước đo. 
Trong thực tế, bảng thứ nguyên khách hàng thường có hơn 100 cột.
Mối quan hệ 
Các mối quan hệ, thành phần cuối cùng của mô hình dữ liệu, các bảng liên kết và được đại diện
bực bội bởi các dòng trong Hình minh họa 5.5. Tất cả các mối quan hệ trong lược đồ hình sao đều có quan hệ một-nhiều 
(1-N) mẫu số lượng. Lượng số là một ràng buộc xác định số lần một 
thể hiện của một thực thể có thể tham gia vào một mối quan hệ. Nó có thể nhận hai giá trị có thể là N hoặc 1:
• N: Một instance có thể tham gia nhiều lần vào mối quan hệ. Không có hạn chế.
• 1: Một instance chỉ có thể tham gia một lần vào mối quan hệ.
Mẫu số lượng 1-N cho mối quan hệ giữa một chiều và một bảng dữ kiện có thể được liên kết với nhau.
dự kiến như sau:
Mặc dù số lượng cột trong bảng dữ kiện nhìn chung là nhỏ nhưng chúng thường có nhiều 
hàng. Các công ty thường có hàng nghìn lượt bán hàng trong cùng một ngày, nếu không muốn nói là nhiều hơn – hãy nghĩ đến trực tuyến 
gã khổng lồ bán lẻ như Amazon. Các cột trong bảng thực tế cũng chủ yếu là định lượng và 
cụ thể hơn là phụ gia. Các giá trị trong các cột này có thể được tổng hợp hoặc nhóm lại dễ dàng 
cùng nhau làm biện pháp. Các thước đo này sau đó có thể được cắt bằng cách sử dụng các cột ở loại tiếp theo 
của các bảng.
Bảng kích thước 
Các kích thước cung cấp bối cảnh cho việc phân tích và mang lại ý nghĩa cho các sự kiện. 
Số tiền bán được 100 đô la không cung cấp nhiều thông tin. Doanh nghiệp muốn 
biết khi nào giao dịch bán hàng xảy ra, ai phải trả 100 đô la và hàng hóa gì. các 
Lược đồ hình sao trong Hình minh họa 5.5 có các bảng thứ nguyên cho ngày diễn ra bán hàng, sản phẩm 
đã bán, khách hàng và nhân viên bán hàng. Các cột trong bảng thứ nguyên là các biến 
có thể được kết hợp theo nhiều cách để cắt các thước đo. Hình minh họa 5.6 chứng minh 
tám câu hỏi có thể được trả lời bằng cách chia biện pháp bán hàng theo một hoặc nhiều khía cạnh
sions được thể hiện trong hình minh họa 5.5.

![ILLUSTRATION 5.6](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.6.png)

5.1  Lập hồ sơ dữ liệu là gì?  5-9
• 1: Với mỗi sự kiện, chỉ có một giá trị tương ứng trong mỗi bảng chiều. Đối với mỗi 
ví dụ của bảng Bán hàng (một dòng hoá đơn), có một ngày, sản phẩm, khách hàng và 
nhân viên bán hàng.
• N: Có thể có nhiều sự kiện cho mỗi chiều. Có thể bán nhiều hàng trong cùng một ngày 
và cùng một loại sản phẩm có thể được bán nhiều lần. Cả khách hàng và nhân viên bán hàng đều có thể 
tham gia vào nhiều giao dịch mua bán.
Quyết định và thông báo
Sau khi điều tra chất lượng và cấu trúc của dữ liệu, đã đến lúc thực hiện bước tiếp theo:
• Không tiến lên phía trước: Nếu dữ liệu không phù hợp, chẳng hạn như dữ liệu có chất lượng kém thì 
sử dụng dữ liệu để ra quyết định sẽ quá rủi ro. Tương tự, nếu cấu trúc dữ liệu là 
kém thì việc tái cơ cấu và xử lý dữ liệu có thể quá phức tạp và tốn kém về mặt kinh tế.
về mặt thực tế là không khả thi.
• Thiết kế lại hệ thống nguồn: Quyết định này thường được đưa ra do lỗi phát sinh 
của hệ thống nguồn cần được sửa chữa. Sau khi đã sửa, nguồn dữ liệu sẽ được cấu hình 
một lần nữa.
• Xác nhận sự phù hợp của dữ liệu cho việc phân tích và tiến về phía trước: Tiến về phía trước với 
dữ liệu đòi hỏi phải nhận thức được rủi ro. Nghĩa là, chúng ta có thể tiếp tục với dữ liệu bằng một 
nhận thức về các vấn đề về độ tin cậy tiềm ẩn và tác động của chúng tới các quyết định.
Nếu quyết định tiếp tục được đưa ra, bước tiếp theo trong quy trình sẽ được thông báo bởi bất kỳ ai. 
những vấn đề phải giải quyết.
Stufan là một cửa hàng nhỏ ở Gumboro, Delaware chuyên mua bán thú nhồi bông. Người sáng lập và CEO 
Shanice Parker muốn áp dụng phân tích dữ liệu để hiểu rõ hơn về hoạt động kinh doanh của mình. Để bắt đầu, cô ấy hỏi bạn 
công ty để giúp chuẩn bị dữ liệu cho việc phân tích.
Bảng này là mẫu dữ liệu sản phẩm của Stufan. Xác định ba vấn đề về chất lượng với dữ liệu.
BASHL
BASH
BERL
CAPH
DOCL
TÀI LIỆU
DOPL
DOPS
DUCH
Chú lùn to lớn rụt rè
Chú lùn nhỏ bé nhút nhát
Berlioz, quý tộc
Thuyền trưởng Haddock, Tintin
Doc lớn, người lùn
Doc Nhỏ, Người Lùn
Ngu Ngốc Lớn, Người Lùn
Nữ công tước, quý tộc
Ngốc Nghếch Nhỏ, Người Lùn
Mã
Mô tả
13
67
23
14
23
45
43
44
–3
QOH
GIẢI PHÁP
1.  Mô tả không phải là cột có một giá trị. Nó kết hợp “mô tả” và “danh mục”.
2.  Có một vấn đề về tính nhất quán: “Quý tộc” và “Quý tộc”.
3.  Có một vấn đề về tính hợp lệ: QOH (Số lượng có sẵn) không thể âm.
Áp dụng nó 5.1
Xác định chất lượng dữ liệu 
vấn đề

![Apply It 5.1](../TaiLieu/textbookForPractice/Figures/Ch_05/Apply%20It%205.1.png)

5-10  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
5.2  Việc trích xuất có ý nghĩa gì-
Dữ liệu tải chuyển đổi (ETL)?
MỤC TIÊU HỌC TẬP ➋
Mô tả quá trình trích xuất-chuyển đổi-tải (ETL).
Trong khi quá trình lập hồ sơ dữ liệu mà bạn vừa tìm hiểu phát hiện ra các vấn đề, thì hàm trích xuất-chuyển đổi-
quá trình tải (ETL) sẽ sửa chúng. Như Hình minh họa 5.7 cho thấy, quy trình ETL xây dựng một
cơ sở dữ liệu ly giải sử dụng một hoặc nhiều nguồn dữ liệu thô. 
MINH HỌA 5.7  Quy trình Trích xuất-Biến đổi-Tải (ETL)
Tải
phân tích
Cơ sở dữ liệu
Dữ liệu thô
Trích xuất
Vệ sinh
Tích hợp
Tái cơ cấu
chuyển đổi
E
T
L
Trích xuất dữ liệu 
Trích xuất dữ liệu, bao gồm việc truyền dữ liệu, là bước đầu tiên trong quy trình ETL:
• Dữ liệu nguồn được chuyển đến nền tảng nơi chúng sẽ được chuyển đổi. Nền tảng này là 
thông thường là kho dữ liệu, là phần mềm lưu trữ và phân tích các tập dữ liệu lớn. 
Power BI và Tableau là ví dụ về kho dữ liệu.
• Quá trình này cũng bao gồm việc xác thực dữ liệu hoặc xác nhận rằng dữ liệu đã được truyền 
một cách đầy đủ và chính xác.
Các công cụ ETL giúp dễ dàng trích xuất dữ liệu từ cơ sở dữ liệu, bảng tính, tệp văn bản và nhiều thứ khác 
nguồn dữ liệu bằng cách cung cấp các trình kết nối dữ liệu là các chương trình phần mềm trực quan được thiết kế 
để trích xuất dữ liệu. Hình minh họa 5.8 (A) hiển thị một số trình kết nối dữ liệu có sẵn trong Excel, 
trong khi bảng (B) thực hiện tương tự với Power BI.
Chuyển đổi dữ liệu 
Dữ liệu thô hiếm khi sẵn sàng để phân tích sau khi chúng được trích xuất. Chuyển đổi dữ liệu được cải thiện 
dữ liệu thô để phân tích thông qua việc làm sạch, tái cơ cấu và tích hợp.
Làm sạch dữ liệu
Dữ liệu có thể không chính xác, không hợp lệ, không nhất quán hoặc không đầy đủ. Làm sạch dữ liệu, một trong những việc quan trọng nhất 
khía cạnh quan trọng và tốn thời gian của việc chuyển đổi dữ liệu, còn được gọi là làm sạch dữ liệu-
ing hoặc chà dữ liệu. Nó liên quan đến việc thêm, sửa đổi và xóa dữ liệu:
• Trong trường hợp dữ liệu không đầy đủ, chẳng hạn như giao dịch bán hàng bị thiếu, dữ liệu có thể cần phải được 
đã thêm vào. Một chiến lược cụ thể để xử lý dữ liệu không đầy đủ là áp đặt, đó là khi 
giá trị ước tính được thay thế cho dữ liệu bị thiếu.

![ILLUSTRATION 5.8](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.8.png)

5.2 Dữ liệu trích xuất-chuyển đổi tải (ETL) có ý nghĩa gì? 5-11
• Việc sửa đổi dữ liệu là cần thiết khi giá trị hiện tại phải được thay thế bằng giá trị mới nếu 
dữ liệu không chính xác, không hợp lệ, không nhất quán hoặc không đầy đủ. Thay thế giá trị NY bằng NJ 
trong cột ghi lại trạng thái của khách hàng là một ví dụ về điều này.
• Xóa dữ liệu không liên quan để phân tích. Dữ liệu dư thừa, chẳng hạn như doanh số bán hàng trùng lặp 
giao dịch nên được loại bỏ. 
Nhận
dữ liệu
Từ văn bản/CSV
Từ Web
Từ Bảng/Phạm vi
Kết nối hiện có
Nguồn gần đây
Tập tin
Trang chủ
Chèn
Vẽ
Bố cục trang
Công thức
dữ liệu
Làm mới
Tất cả
Truy vấn & Conne
Từ tập tin
Từ cơ sở dữ liệu 
Từ Azure
Từ các nguồn khác
Kết hợp truy vấn
Khởi chạy Trình soạn thảo Power Query...
Cài đặt nguồn dữ liệu
Tùy chọn truy vấn
Từ văn bản/CSV
Từ Web
Từ Bảng/Phạm vi
Kết nối hiện có
Nguồn gần đây
Làm mới
Tất cả
Tất cả
Từ sổ làm việc
Từ văn bản/CSV
Từ XML
Từ JSON
Từ PDF
Từ thư mục
X
JSON
PDF
Excel
X
Nhận
dữ liệu
Power BI
bộ dữ liệu
SQL
Máy chủ
Gần đây
nguồn
Tập tin
Trang chủ
Chèn
Làm người mẫu
Xem
Trợ giúp
Bảng nhớ tạm
dữ liệu
Nhận dữ liệu
Tìm kiếm
Tất cả
Tất cả
Tập tin
Cơ sở dữ liệu
Nền tảng sức mạnh
Azure
Dịch vụ trực tuyến
Khác
Kết nối
Hủy bỏ
Trang 1
Từ dịch vụ trực tuyến
Dán
Cắt
Sao chép
Họa sĩ định dạng
& Conne
+
Nhập
dữ liệu
Excel
X
Power BI
bộ dữ liệu
SQL
Máy chủ
Gần đây
nguồn
dữ liệu
+
Nhập
dữ liệu
Excel
Văn bản/CSV
JSON
XML
Thư mục
PDF
thư mục SharePoint
Cơ sở dữ liệu máy chủ SQL
Cơ sở dữ liệu Dịch vụ Phân tích Máy chủ SQL
Truy cập cơ sở dữ liệu
Cơ sở dữ liệu Oracle
Cơ sở dữ liệu IBM Db2
IBM Netezza
Cơ sở dữ liệu IBM Informix (Beta)
Cơ sở dữ liệu MySQL
Cơ sở dữ liệu PostgreSQL
Ứng dụng mẫu
Đầu nối được chứng nhận
Để có cái nhìn tổng quan về tất cả Excel
trình kết nối dữ liệu, nhấp vào Dữ liệu
trong Menu chính, sau đó chọn
Nhận dữ liệu trong Ribbon.
Bảng nhớ tạm
Dán
Cắt
Sao chép
Họa sĩ định dạng
b
d
b
d
(A) Trình kết nối dữ liệu Excel
(B) Trình kết nối dữ liệu Power BI
Để có cái nhìn tổng quan về tất cả Quyền lực
trình kết nối dữ liệu của BI, hãy nhấp vào
Tab Trang chủ trong Menu Chính, sau đó
chọn Lấy dữ liệu trong Ribbon. 
 MINH HỌA 5.8 Trích xuất dữ liệu bằng Trình kết nối dữ liệu 
 MINH HỌA 5.9 Loại bỏ 
Hàng có Power Query 
Xóa
Hàng
A
Z
Z
A
Tách
Cột
Nhóm
Bởi
Xóa các hàng trên cùng
Xóa hàng dưới cùng
Xóa các hàng thay thế
+
Xóa trùng lặp
Xóa hàng trống
Xóa lỗi
 Các công cụ ETL cung cấp các chức năng tích hợp cho nhiều tác vụ làm sạch dữ liệu. Điều gì sẽ xảy ra nếu bạn muốn 
để xóa hàng khỏi bảng?  Hình minh họa 5.9 cho thấy Power Query, Excel và Power 
Công cụ ETL của BI có các lệnh xóa hàng trùng lặp, hàng trống hoặc hàng chứa 
lỗi. Các công cụ khác cung cấp các hoạt động tương tự.

![ILLUSTRATION 5.9](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.9.png)

5-12  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Còn việc thay thế các giá trị cụ thể thì sao? Hình minh họa 5.10 cho thấy cách Tìm và 
Tùy chọn thay thế có thể khắc phục sự cố không nhất quán.
MINH HỌA 5.10  Thay thế giá trị bằng Power Query
Thay thế giá trị
Giá trị cần tìm
Thay thế một giá trị bằng một giá trị khác trong các cột đã chọn.
M
Thay thế bằng
Nam
Tùy chọn nâng cao
Hủy bỏ
được rồi
ÁP DỤNG TƯ duy phê phán 5.3: Chọn phương pháp tốt nhất
Chuẩn bị dữ liệu không phải là một khoa học chính xác. Phán đoán là một phần quan trọng trong việc xây dựng một phương pháp phân tích.
cơ sở dữ liệu cal. Luôn xem xét các lựa chọn thay thế, kiểm tra điểm mạnh và điểm yếu của chúng và xếp hạng 
họ. Trong phần sau, bảng (A) và (B) biểu thị cùng một dữ liệu nhưng sắp xếp chúng khác nhau 
(Các lựa chọn thay thế):
• Trong bảng (B), danh mục trở thành thực thể riêng của nó và tên của danh mục chỉ được ghi lại một lần.
• Mặt khác, việc áp dụng mô hình dữ liệu ở bảng (A) có nghĩa là tên danh mục được lặp lại 
cho tất cả các sản phẩm cùng loại. Mô hình dữ liệu trong bảng (B) tiết kiệm không gian ở mức giá 
phức tạp, vì có một mối quan hệ bổ sung cần được xem xét trong quá trình 
phân tích.
Các mô hình dữ liệu thay thế cho cùng một tập dữ liệu
Hóa đơnKhông
Ngày
sản phẩm
bán hàng
(A)
(B)
N
1
N
1
N
1
Mã sản phẩm
Tên
Mô tả
ID danh mục
Tên danh mục
Chi phí
sản phẩm
Hóa đơnKhông
Ngày
sản phẩm
bán hàng
Mã sản phẩm
Tên
Mô tả
Danh mục
Chi phí
sản phẩm
ID danh mục
Tên danh mục
Danh mục
Nếu “M” đôi khi được dùng cho “Nam” và đôi khi từ “Nam” được dùng trong cột
umn cho giới tính trong tập dữ liệu thì tất cả giá trị M trong cột Giới tính có thể được thay thế bằng 
“Nam.” Sử dụng công cụ này sẽ nhanh chóng giải quyết dữ liệu không nhất quán bằng cách tìm giá trị không nhất quán
ues và thay thế chúng.

![ILLUSTRATION 5.10](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.10.png)

5.2  Dữ liệu trích xuất-chuyển đổi-tải (ETL) có ý nghĩa gì?  5-13
Tích hợp dữ liệu
Hầu hết các dự án phân tích dữ liệu đều liên quan đến nhiều bảng, thường từ các nguồn dữ liệu khác nhau. 
phải được tích hợp trước khi thực hiện phân tích. Tích hợp dữ liệu là quá trình kết nối 
dữ liệu liên quan. Có hai hình thức tích hợp đặc biệt:
• Liên kết hai bảng bằng cách xác định mối quan hệ giữa chúng. Các mối quan hệ được tạo ra 
sử dụng khóa chính và khóa ngoại. Các khía cạnh khác của mối quan hệ phải được chỉ định là 
hồng y.
• Việc kết hợp hai hoặc nhiều bảng sẽ hợp nhất thông tin về cùng một thực thể. Các bảng có thể được 
kết hợp hai cách. Một liên kết kết hợp các bảng khác nhau có cùng cấu trúc dữ liệu. các 
kết quả là một bảng có nhiều hàng hơn. Hãy nhớ lại chương phân tích dữ liệu cơ bản rằng một 
nối hoặc hợp nhất, kết hợp các thành phần dữ liệu hoặc cột từ các bảng khác nhau. Kết quả là một 
bảng có nhiều cột hơn. 
Một thách thức cụ thể đối với việc tích hợp là việc so khớp dữ liệu, một quá trình so sánh dữ liệu và xác định
mỏ cho dù chúng mô tả cùng một thực thể. Hãy xem xét hai bộ dữ liệu khách hàng được hiển thị trong 
Minh họa 5.11. Hình minh họa 5.11 (A) chứa thông tin tài chính và bảng (B) chứa 
thông tin nhân khẩu học về khách hàng. Làm thế nào chúng ta có thể điều hòa hoặc phù hợp với khách hàng? 
tên? Các vấn đề cụ thể cần giải quyết bao gồm:
• Biệt danh: Jen Pollack so với Jenny Pollack.
• Lỗi đánh máy: Carlos Panetta so với Carlos Paretta.
• Tên đảo ngược: Margarita David so với David Margo.
Bảng (C) hiển thị bảng đã hợp nhất. Hầu hết các công cụ ETL đều cung cấp hỗ trợ nâng cao cho việc khớp dữ liệu.
Tái cấu trúc dữ liệu
Dữ liệu sạch không nhất thiết phải được cấu trúc theo cách giúp việc phân tích trở nên dễ dàng và hiệu quả. dữ liệu 
tái cấu trúc, còn được gọi là sắp xếp dữ liệu hoặc trộn dữ liệu, không thay đổi dữ liệu 
giá trị, nhưng nó thay đổi cách tổ chức dữ liệu.
Các công cụ ETL cung cấp nhiều kỹ thuật khác nhau để giúp việc tái cấu trúc dễ dàng hơn:
• Thêm và xóa cột.
• Đổi tên cột và bảng.
• Tách và gộp các cột.
• Tách và kết hợp các bảng.
• Chuyển đổi và hủy xoay bảng.
MINH HỌA 5.11  Vấn đề khớp dữ liệu
Ann trắng
Carlos Panetta
Jen Pollack
Margarita David
William McCarthy
B
A
B
C
A
Tên
Trạng thái
3
5
3
1
5
Giảm giá
(C) Bảng khách hàng đã hợp nhất
F
M
F
M
M
Giới tính
28
44
57
22
38
Tuổi
William McCarthy
Margarita David
Ann trắng
Carlos Panetta
Jen Pollack
A
C
B
A
B
Tên
Trạng thái
5
1
3
5
3
Giảm giá
(A) Bảng khách hàng:
Thông tin tài chính
Carlos Paretta
David Margo
Jenny Pollack
Bill McCarthy
Ann trắng
M
M
F
M
F
Tên
Giới tính
44
22
57
38
28
Tuổi
(B) Bảng khách hàng:
Thông tin nhân khẩu học

![ILLUSTRATION 5.11](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.11.png)