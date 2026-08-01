5.4  Cột chuyển đổi mẫu nào?  5-21
	 1. Tên cột phải mô tả chính xác nội dung của cột.
	 2. Chúng phải trực quan đối với người kinh doanh.
	 3. Chỉ sử dụng những từ viết tắt phổ biến mà mọi người đều hiểu, chẳng hạn như YTD.
	 4. Loại bỏ dấu cách, dấu gạch dưới hoặc các ký hiệu khác. Ví dụ: sử dụng Tên khách hàng 
thay vì Customer_Name.
Đổi tên cột
Công cụ ETL giúp bạn dễ dàng khắc phục sự cố này bằng cách đổi tên cột. Minh họa 5.17 
cho biết cách đổi tên một cột trong Power Query. Đầu tiên, nhấp chuột phải vào cột ID trong 
Bảng ClData rồi chọn Đổi tên và nhập tên mới: “ClientID”. Lưu ý rằng một col-
thay đổi tên umn sẽ tự động lan truyền đến tất cả các công thức và báo cáo.
MINH HỌA 5.17  Sửa đổi tên cột
123 ID
Sao chép
Xóa
Xóa các cột khác
Cột trùng lặp
Thêm cột từ ví dụ...
Xóa trùng lặp
Xóa lỗi
Thay đổi loại
chuyển đổi
Thay thế các giá trị...
Thay thế lỗi...
Nhóm theo...
Điền vào
Bỏ xoay cột
Bỏ xoay các cột khác
Chỉ hủy xoay các cột đã chọn
Đổi tên...
Di chuyển
Đi sâu xuống
Thêm dưới dạng truy vấn mới 
1 2
Không phải tất cả các tên cột trong bộ dữ liệu Beans đều trực quan và dễ hiểu. Minh họa 5.18 
hiển thị một số thay đổi tên tiềm năng cho các cột. Lưu ý rằng, vì hai cột trong cùng một 
bảng không thể có cùng tên, Power Query tự động thay đổi cột ID thứ hai trong 
bảng Dịch vụ thành ID-1 khi tải dữ liệu.
MINH HỌA 5.18  Gợi ý tên cột  
cho đậu
ClData
ClData
nhân viên
nhân viên
E-Dem
E-Dem
E-Dem
Dịch vụ
Dịch vụ
ID khách hàng
Tên ngành
ID nhân viên
Chức danh công việc
Tên đầu tiên
Họ
Danh sách chứng nhận
Thời gian thực tế
ID dịch vụ
Dịch vụ
Dịch vụ
Dịch vụ
Thời gian dự toán
ID tác vụ
Tên nhiệm vụ
Bảng
Tên cột đã sửa đổi
ID
Tên ngành
ID
Chức danh
nhân viên
Tình trạng hôn nhân
MS
Đầu tiên
Cuối cùng
Danh sách chứng chỉ
Thời gian thực tế
ID
Thời gian dự kiến
ID-1
Nhiệm vụ
Tên cột

![ILLUSTRATION 5.18](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.18.png)

5-22  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Tóm tắt mẫu 4
vấn đề
Tên cột không chính xác hoặc mơ hồ làm cho nó 
khó hiểu và khó làm việc hơn với một tập dữ liệu.
Phát hiện (Hồ sơ dữ liệu)
Quét các cột để tìm tên không chính xác hoặc mơ hồ.
Đúng (ETL)
Đổi tên cột.
Mẫu chuẩn bị dữ liệu 5: Kiểu dữ liệu không chính xác
Xác minh các loại dữ liệu là một phần thiết yếu của việc chuẩn bị dữ liệu. Kiểu dữ liệu là một phần không thể thiếu của 
các định nghĩa cột vì chúng xác định những gì chúng ta có thể và không thể làm với dữ liệu trong một cột
ừm. Ví dụ: các toán tử như SUM và AVERAGE yêu cầu một số 
trường, nhưng các hàm thời gian và ngày yêu cầu một cột có kiểu dữ liệu ngày.
Kiểm tra kiểu dữ liệu
Các công cụ ETL tự động gán loại dữ liệu cho từng cột trong quá trình trích xuất, nhưng đôi khi 
phép gán không chính xác hoặc công cụ ETL không thể xác định loại dữ liệu. Hãy 
minh họa kịch bản cuối cùng bằng một ví dụ. Hình minh họa 5.19 (A) cho thấy mức chênh lệch thô
dữ liệu trang tính. Bảng điều khiển (B) hiển thị cùng một tập dữ liệu sau khi trích xuất trong Power Query. Chú ý rằng 
kiểu dữ liệu là ABC 
123, còn được gọi là kiểu dữ liệu Any. Nó chỉ ra rằng Power Query không thể 
xác định loại dữ liệu, có nghĩa là không thể thực hiện các phép tính trên dữ liệu trong 
cột.
MINH HỌA 5.19  Kiểm tra và thay đổi kiểu dữ liệu
A
A
B
6
ID
1
2
4
5
123 ID
Lỗi
Lỗi
1
2
4
5
6
1
2
3
4
5
6
7
ID
2 (28%)
Lỗi
Xóa lỗi
...
ABC
123 ID
A
B
1
2
4
5
6
(B) Dữ liệu được trích xuất
(C) Chuyển đổi kiểu dữ liệu:
Số nguyên
(D) Loại dữ liệu
Chuyển đổi: Văn bản
(A) Nguyên
Bảng tính
dữ liệu
Mã ABC
1
2
3
4
5
6
7
1
2
A
4
5
B
6
Thay đổi kiểu dữ liệu
Khắc phục sự cố này bằng cách thay đổi kiểu dữ liệu bằng công cụ ETL. Hình minh họa 5.20 cho thấy 
các kiểu dữ liệu khác nhau có sẵn trong Power Query. Hình minh họa 5.19 (C) cho thấy điều gì xảy ra nếu 
Số nguyên được chọn cho tập dữ liệu trong bảng (B). Lưu ý rằng một số giá trị được chuyển đổi 
trong khi các giá trị khác tạo ra lỗi. Điều này rất hữu ích vì việc kiểm tra lỗi sẽ được thực hiện 
một phần của việc chuẩn bị dữ liệu. Thanh màu đỏ cho biết có lỗi và nhấp vào nó sẽ hiển thị 
tỷ lệ lỗi (28%). Chúng cũng có thể được lọc ra, điều này rất hữu ích cho các tập dữ liệu lớn. 
Hình minh họa 5.19 (D) cho thấy điều gì xảy ra khi Kiểu Dữ liệu được chuyển đổi thành Văn bản. Các lỗi 
biến mất, nhưng những gì có thể làm với dữ liệu còn hạn chế.

![ILLUSTRATION 5.20](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.20.png)

5.4  Cột chuyển đổi mẫu nào?  5-23
MINH HỌA 5.20  Các kiểu dữ liệu Power Query
ABC
123
ID
1
2
3
4
5
6
7
1.2 Số thập phân
$ Số thập phân cố định
123 Số nguyên
% Phần Trăm
Ngày/Giờ
Ngày/Giờ/Múi giờ
Ngày
Thời lượng
ABC
văn bản
thời gian
Đúng/Sai
nhị phân
Sử dụng ngôn ngữ...
Không có vấn đề gì với các kiểu dữ liệu của Bean nên không cần thực hiện thay đổi nào. Tuy nhiên, hãy đảm bảo 
để thêm một cột vào từ điển dữ liệu để chỉ định các kiểu dữ liệu.
Tóm tắt mẫu 5
vấn đề
Loại dữ liệu không chính xác sẽ giới hạn những việc có thể làm 
với dữ liệu trong một cột.
Phát hiện (Hồ sơ dữ liệu)
Kiểm tra kiểu dữ liệu.
Đúng (ETL)
Thay đổi kiểu dữ liệu.
Mẫu chuẩn bị dữ liệu 6: Tổng hợp và 
Cột nhiều giá trị
Mỗi ô phải chứa một giá trị mô tả một đặc tính vì hai hoặc nhiều giá trị trong 
cùng một ô khiến việc phân tích trở nên khó khăn hơn. Hai tình huống cụ thể vi phạm nguyên tắc đơn 
quy tắc có giá trị và làm cho việc phân tích trở nên phức tạp hơn là các cột tổng hợp và cột đa giá trị.
Quét các cột tổng hợp và nhiều giá trị
Phương pháp tốt nhất để phát hiện các cột tổng hợp hoặc nhiều giá trị là quét trực quan. Kiểm tra 
tập dữ liệu Beans theo cách này sẽ tiết lộ:
• Cột Tên trong bảng Nhân viên trộn lẫn họ và tên của nhân viên. Trong khi 
đây có thể không phải là vấn đề từ góc độ phân tích mà là vấn đề khi so khớp 
chúng với các cột FirstName và LastName trong bảng E-Dem.
• Cột Danh sách Chứng nhận trong bảng E-Dem có nhiều giá trị.
Tái cấu trúc dữ liệu
Cách cấu trúc lại một cột phụ thuộc vào cột đó là cột tổng hợp hay cột có nhiều giá trị. 
Giải pháp cho cột tổng hợp là chia nó ra. Trong Power Query, bấm vào cột Tên. 
Sau đó chọn tab Trang chủ trong Menu chính. Bấm vào Tách cột trong ruy-băng và chọn 
Bằng dấu phân cách (Minh họa 5.21).

![ILLUSTRATION 5.21](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.21.png)

5-24
CHƯƠNG 5 Phân tích: Chuẩn bị dữ liệu
 MINH HỌA 5.21 Power Query | Cột Chia | thiết lập 
Đóng
Đóng &
Áp dụng
Mới
Nguồn
Gần đây
Nguồn
Nhập
dữ liệu
Truy vấn mới
Nguồn dữ liệu
Cài đặt
Nguồn dữ liệu..
Quản lý
Thông số
Thông số
Quản lý
Cột
Làm mới
Xem trước
A
Z
Z
A
Sắp xếp
Giảm
Hàng
Thuộc tính
Trình chỉnh sửa nâng cao
Quản lý
Tách
Cột
Nhóm
Bởi
E-DEM
nhân viên
Dữ liệu CL
Dịch vụ
Truy vấn [4]
ID nhân viên
123
Tên
ABC
Công việc
ABC
1
2
3
4
5
1
2
3
4
5
Kanya, James
Ivan, Lenk
Mick, Richards
Juan, Lozano
Gail, David
Nhân viên
Người quản lý
cao cấp
Nhân viên
cao cấp
Truy vấn
Tập tin
Trang chủ
chuyển đổi
Thêm cột
Công cụ
Trợ giúp
Xem
Theo dấu phân cách
Theo số lượng ký tự
Từ chữ thường sang chữ hoa
Từ chữ hoa sang chữ thường
Từ số đến không có chữ số
Bằng phi chữ số thành chữ số
Theo vị trí
Đóng
Đóng &
Áp dụng
Mới
Nguồn
Gần đây
Nguồn
Nhập
dữ liệu
Truy vấn mới
Nguồn dữ liệu
Cài đặt
Nguồn dữ liệu..
Quản lý
Thông số
Thông số
Quản lý
Cột
Làm mới
Xem trước
A
Z
Z
A
Sắp xếp
Giảm
Hàng
Thuộc tính
Trình chỉnh sửa nâng cao
Quản lý
Truy vấn
Loại dữ liệu: Văn bản
Sử dụng hàng đầu tiên
làm Tiêu đề
1 2 Thay thế giá trị
Nhóm
Bởi
Loại dữ liệu: Văn bản
Sử dụng hàng đầu tiên
làm Tiêu đề
1 2 Thay thế giá trị
 Cửa sổ như trong Hình 5.22 sẽ xuất hiện. Power Query đã được chọn Dấu phẩy
làm dấu phân cách và vì chỉ có một dấu phẩy cho mỗi tên nên việc tên nào không quan trọng 
trong số ba tùy chọn Split at được chọn. Trong ví dụ này, tùy chọn Dấu phân cách ngoài cùng bên trái là 
đã chọn. Sau khi tách, đổi tên Name.1 thành “FirstName” và Name.2 thành “LastName”. 
 Mặt khác, tính chất đa giá trị của cột CertificationList trong bảng E-Dem 
yêu cầu tạo một bảng mới. Nhưng vì dữ liệu nhân viên cần phải làm thêm nên nó khiến 
ý thức để làm điều đó sau này. Ví dụ này cho thấy bản chất không tuần tự của việc áp dụng các mẫu–
thứ tự áp dụng sẽ phụ thuộc vào từng dự án.  Các cột khác trong 
Tập dữ liệu Beans có giá trị đơn và mẫu này không áp dụng cho chúng. 
 Tóm tắt mẫu 6 
 vấn đề 
 Các cột không có giá trị đơn sẽ gây khó khăn cho việc phân tích. 
 Phát hiện (Hồ sơ dữ liệu) 
Kiểm tra các giá trị trong các cột. 
 Đúng (ETL) 
 Tách các cột kết hợp. 
 Tạo một bảng riêng cho các cột có nhiều giá trị. 
Mẫu chuẩn bị dữ liệu 7: Giá trị không chính xác
 Đôi khi giá trị sai được gán cho một trong các đặc điểm của thực thể. Việc chứng nhận cho 
một nhân viên có thể được ghi là CMA thay vì CPA, cả hai đều là chứng chỉ hợp lệ. 
Giá trị không chính xác có thể gây ra hậu quả nghiêm trọng, bao gồm cả lỗi vận chuyển và thanh toán. 
 MINH HỌA 5.22 Power Query | Cột Chia | 
Chọn dấu phân cách 
Chia cột theo dấu phân cách
Chỉ định dấu phân cách được sử dụng để phân chia cột văn bản.
Chọn hoặc nhập dấu phân cách
Chia tại
Dấu phẩy
?
Dấu phân cách ngoài cùng bên trái
Dấu phân cách ngoài cùng bên phải
Mỗi lần xuất hiện của dấu phân cách
Tùy chọn nâng cao

![ILLUSTRATION 5.22](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.22.png)

5.4  Cột chuyển đổi mẫu nào?  5-25
Phát hiện các giá trị không chính xác với các giá trị ngoại lệ
Dữ liệu không chính xác rất khó xác định trong nội dung của một cột, vì vậy nó rất hữu ích 
để tìm kiếm các giá trị ngoại lệ, nổi bật trong dữ liệu số. Nếu một sản phẩm có giá $19 
thay vào đó được ghi là 91 USD và hầu hết giá sản phẩm nằm trong khoảng từ 10 USD đến 30 USD, điều đó sẽ nổi bật. 
Một định nghĩa chính thức hơn cho giá trị ngoại lệ là giá trị lớn hơn 1,5 lần giá trị trung bình.
phạm vi ô bên dưới tứ phân vị đầu tiên hoặc trên tứ phân vị thứ ba.
Hãy lập cấu hình cột Thời gian thực tế trong bảng Dịch vụ. Minh họa 5.23 (A) hiển thị 
thống kê cấu hình cột được tạo bởi Power Query. Bảng (B) hiển thị các giá trị của 
Thời gian thực tế theo thứ tự giảm dần. Ba giá trị trên cùng trong cột (bảng (B)) là các giá trị ngoại lệ 
và rất có thể là sai. Ngoài ra, thời gian thực tế cho dịch vụ có ID “1325”, 25 giờ, là 
không hợp lệ. Chắc phải là 2,5 giờ.
MINH HỌA 5.23  Lập hồ sơ cho 
Dữ liệu không chính xác
Thống kê cột
Đếm
4.632
Lỗi
0
trống
0
khác biệt
190
duy nhất
48
NaN
0
số không
0
tối thiểu
0,05
Tối đa
25
trung bình
1.77672...
Độ lệch chuẩn
2.03039...
(B) Cột Thời gian Thực tế:
Giá trị theo thứ tự giảm dần
(A) Cột Thời gian Thực tế: Thống kê
1325
3277
4387
2828
2452
25
22,5
20
11.4
10:75
123 ID
1.2 Thời gian thực tế
Sửa đổi giá trị không chính xác
Khi một giá trị nghi vấn được xác định, có một vài lựa chọn. Đầu tiên là xác định các 
nguyên nhân gốc rễ của lỗi và loại bỏ nó. Người dùng có thể được cảnh báo rằng một ngoại lệ đang được nhập 
vào hệ thống. Điều này sẽ loại bỏ đáng kể các lỗi trong dữ liệu thô. Một lựa chọn khác là 
để sửa giá trị trong dữ liệu nguồn. Cuối cùng, giá trị có thể được hiệu chỉnh trong quá trình phân tích 
cơ sở dữ liệu, nhưng không có trong dữ liệu nguồn.
Hình minh họa 5.24 hiển thị các giá trị Thời gian thực được sửa đổi cho ví dụ về Beans.
Tóm tắt mẫu 7
vấn đề
Dữ liệu không chính xác có thể dẫn đến việc ra quyết định kém.
Phát hiện (Hồ sơ dữ liệu)
Phát hiện các giá trị không chính xác với các ngoại lệ.
Đúng (ETL)
Sửa đổi các giá trị không chính xác.
Mẫu chuẩn bị dữ liệu 8: Giá trị không nhất quán
Mẫu tiếp theo giải quyết vấn đề không nhất quán về dữ liệu, xảy ra khi hai hoặc nhiều đại diện khác nhau
sự phẫn nộ có cùng giá trị được trộn lẫn trong cùng một cột. Ví dụ, việc xác định 
tổng số tiền bán hàng tính bằng đô la cho khách hàng MI khi cả MI và Michigan đều được sử dụng làm giá trị 
có thể dẫn đến việc đánh giá thấp, từ đó có thể dẫn đến những quyết định sai lầm.
MINH HỌA 5.24  Sửa lỗi 
trường Thời gian thực tế trong Dịch vụ 
Bảng
1325
3277
4387
25
22,5
20
ID
Giá trị không chính xác
2,5
2,25
2
Giá trị đúng

![ILLUSTRATION 5.24](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.24.png)

5-26  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Xác định các giá trị không nhất quán
Hai kỹ thuật định hình rất hữu ích để phát hiện các giá trị không nhất quán:
• Các giá trị riêng biệt: Quét trực quan các giá trị riêng biệt của một cột là một cách hiệu quả để 
xác định dữ liệu không nhất quán
• Tần số: Các giá trị có tần số thấp có thể cho thấy dữ liệu không nhất quán.
Hình minh họa 5.25 (A) hiển thị các giá trị riêng biệt cho cột JobTitle trong bảng Nhân viên. 
Thông tin này có sẵn cho tất cả các cột trong Power Query. Hình minh họa cho thấy rằng 
Giám đốc cấp cao được đại diện không nhất quán. Tần số thấp cũng có thể chỉ ra lỗi chính tả 
dẫn đến sự không nhất quán. Như bảng (B) hiển thị, tần số của Sr Manager là 1. Giá trị 
phân phối được hiển thị trong bảng (B) là một phần của cấu hình cột trong Power Query. Một cột khác 
với vấn đề mâu thuẫn trong tập dữ liệu Beans là University.
Sửa đổi các giá trị không nhất quán
Sửa dữ liệu không nhất quán bằng cách xác định nguyên nhân gốc rễ và loại bỏ nó hoặc sửa đổi 
các giá trị trong dữ liệu nguồn hoặc cơ sở dữ liệu phân tích. Khi sửa đổi các giá trị, 
đầu tiên hãy xác định nên giữ lại cách trình bày nào. Đối với cột JobTitle, giữ nguyên Manager. các 
những thay đổi trong Hình minh họa 5.26 đã được thực hiện đối với cột Đại học. 
Hầu hết phần mềm ETL, bao gồm Power Query, đều cung cấp các công cụ tìm và thay thế để sửa đổi giá trị.
Tóm tắt mẫu 8
vấn đề
Dữ liệu không nhất quán có thể dẫn đến việc ra quyết định kém.
Phát hiện (Hồ sơ dữ liệu)
Xác định các giá trị không nhất quán
Đúng (ETL)
Sửa đổi các giá trị không nhất quán.
Mẫu chuẩn bị dữ liệu 9: Giá trị không đầy đủ
Mẫu này giải quyết tình trạng không đầy đủ có thể khiến dữ liệu không thể sử dụng được và không đáng tin cậy. cho 
Ví dụ: không có địa chỉ của khách hàng, doanh nghiệp không thể gửi tài liệu tiếp thị cho họ. 
Ý nghĩa khác nhau của giá trị null cũng có thể dẫn đến dữ liệu không đáng tin cậy.
MINH HỌA 5.25  Lập hồ sơ cho dữ liệu không nhất quán
(B) Cột Chức danh: Tần suất
Đếm
Lỗi
trống
khác biệt
duy nhất
Chuỗi trống
tối thiểu
Tối đa
24
0
0
6
1
0
Quản lý...
Nhân viên
Thống kê cột
...
...
cao cấp
Nhân viên
Người quản lý
Đối tác
Giám đốc cấp cao
Giám đốc cấp cao
Phân phối giá trị
123
1
ID nhân viên
ABC
Tên đầu tiên
ABC
Họ
(A) Cột Chức danh: Giá trị riêng biệt
Họ
ABC
Sắp xếp giảm dần
ZA
Xóa sắp xếp
Xóa bộ lọc
Xóa trống
AZ
Sắp xếp tăng dần
Bộ lọc văn bản
Tìm kiếm
(Chọn tất cả) 
Người quản lý
Giám đốc cấp cao
Giám đốc cấp cao
Đối tác
cao cấp
Nhân viên
được rồi
Hủy bỏ
ABC
ABC
Chức danh công việc
Chức danh công việc
MSU
Ừm
Đại học bang Michigan
Đại học Michigan
Giá trị hiện tại
Giá trị mới
MINH HỌA 5.26  Thay đổi 
để giải quyết sự không nhất quán trong 
cột đại học

![ILLUSTRATION 5.26](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.26.png)

5.4  Cột chuyển đổi mẫu nào?  5-27
Có một số khía cạnh của sự không hoàn thiện đáng để khám phá:
• Có nên cho phép giá trị null không, và nếu không thì có giá trị nào không?
• Nếu cho phép giá trị null thì bao nhiêu phần trăm giá trị là null? Nếu tỷ lệ phần trăm là 
cao, có nên tải cột không?
• Các giá trị không đầy đủ được biểu diễn như thế nào: giá trị rỗng hoặc một mã cụ thể? Là những đại diện 
nhất quán?
Điều tra giá trị Null
Các công cụ ETL tiết lộ, trên cơ sở từng cột, tỷ lệ phần trăm của các giá trị null. Sử dụng nguồn điện 
Truy vấn, Hình minh họa 5.27 hiển thị thông tin này cho cột Trạng thái hôn nhân trong 
Bảng nhân viên. Thông tin này hữu ích theo nhiều cách:
• Đối với mỗi cột, hãy quyết định xem có cho phép giá trị null hay không. Khóa chính không thể chứa 
giá trị null. Ngoài ra, cột Tỷ lệ trong bảng Nhân viên không thể chứa bất kỳ giá trị null nào 
bởi vì nó được sử dụng để xác định mức phí mà khách hàng phải trả. Tỷ lệ phần trăm cho thấy 
liệu đây có phải là trường hợp không.
• Tỷ lệ phần trăm cao hoặc cao hơn dự kiến ​​có thể khiến cột không thể sử dụng được.
Điều quan trọng nữa là phải phân tích xem tính không đầy đủ được thể hiện như thế nào và điều này ảnh hưởng như thế nào đến 
độ tin cậy của dữ liệu. Giá trị null trong cột MaritalStatus có ý nghĩa gì? Đây có phải là một 
cách khác để nói rằng một nhân viên còn độc thân, hay chúng ta không biết hôn nhân của nhân viên đó 
trạng thái?
Xóa trống
Tình trạng hôn nhân
16 (67%)
hợp lệ
0 (0%)
Lỗi
đã kết hôn
Độc thân
Độc thân
đã kết hôn
Độc thân
vô giá trị
vô giá trị
vô giá trị
vô giá trị
đã kết hôn
đã kết hôn
Tình trạng hôn nhân
ABC
8 (33%)
trống
MINH HỌA 5.27  
Hồ sơ không đầy đủ
Xóa cột hoặc thay thế giá trị null
Kịch bản điều chỉnh phụ thuộc vào tình hình. Nếu giá trị null không được phép nhưng chúng 
tồn tại thì chúng nên được thay thế. Nếu số lượng giá trị null quá cao không còn hữu ích thì 
xóa cột khỏi cơ sở dữ liệu phân tích. Nếu có sự không thống nhất trong việc trình bày 
thiếu các giá trị, thiết kế một lược đồ nhất quán và sửa các giá trị theo lược đồ đó. cho 
cột Tình trạng hôn nhân, các giá trị có thể là Đã kết hôn, Độc thân và để trống. Giá trị trống cho biết 
rằng các giá trị chưa được biết. 
Tóm tắt mẫu 9
vấn đề
Sự không đầy đủ có thể làm cho dữ liệu không thể sử dụng được và 
không đáng tin cậy và dẫn đến việc ra quyết định kém.
Phát hiện (Hồ sơ dữ liệu)
Điều tra các giá trị null.
Đúng (ETL)
Xóa cột hoặc thay thế các giá trị null.

![ILLUSTRATION 5.27](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.27.png)