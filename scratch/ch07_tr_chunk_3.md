7-12  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
được chọn bằng bộ lọc. Chúng ta có thể sử dụng nhiều thước đo (làm thế nào) để so sánh chúng, bao gồm cả tổng 
số giờ làm việc, tổng doanh thu được tạo ra, số lượng khách hàng, doanh thu trung bình trên mỗi khách hàng và 
thời gian phản hồi trung bình của khách hàng. Tất cả các biến này có thể được kéo vào khe biến số 
được gắn nhãn Giá trị. Đây là lý do tại sao bước lập mô hình thông tin lại quan trọng đối với việc khám phá dữ liệu – nó 
cho phép tạo các thước đo bổ sung mà sau này bạn có thể sử dụng trong phân tích.
Mẫu khám phá dữ liệu 2: Phân phối
Mối quan hệ dữ liệu phân phối (Minh họa 7.11) cho thấy các giá trị của một số 
biến được phân phối hoặc trải rộng bằng cách cung cấp giá trị thấp nhất, giá trị cao nhất, 
trung vị, phạm vi liên tứ phân vị, v.v.
MINH HỌA 7.11    Cấu trúc thăm dò cho một 
Mối quan hệ dữ liệu phân phối
So sánh nhiều
phân phối dựa trên
các giá trị của một
biến danh nghĩa.
số
Biến
Biến số
quyết định cái gì
lĩnh vực đang được khám phá.
danh nghĩa
Biến
Một kịch bản phổ biến, được hiển thị trong Hình minh họa 7.11, là tạo và so sánh nhiều bản phân phối
của cùng một biến số dựa trên các giá trị khác nhau của một biến danh nghĩa. các 
đường chấm chấm chỉ ra rằng một biến như vậy có giá trị cho việc khám phá, nhưng tùy chọn khi xác định
thiết lập mối quan hệ dữ liệu phân phối.
Trực quan hóa
Một số hình ảnh trực quan mô tả sự phân bố, bao gồm biểu đồ, biểu đồ violin và hộp-và-
biểu đồ râu (hoặc biểu đồ boxplot). Biểu đồ hình hộp và râu vừa mạnh mẽ vừa chi tiết, vì vậy 
chúng được sử dụng ở đây để minh họa trực quan cho mẫu này.
Hãy quay lại ví dụ về HNA. Dữ liệu Công ty có một bảng tính từ một trong 
các đại lý của nó ở New York. Họ muốn biết lợi nhuận thu được từ việc bán ô tô thay đổi như thế nào. 
Hình minh họa 7.12 tóm tắt dữ liệu bảng tính về số xe mà đại lý đã bán lần trước 
Tháng mười hai.
MINH HỌA 7.12    Cấu trúc dữ liệu của dữ liệu lợi nhuận đại lý
Tên trường
Mô tả
ID
ID nội bộ xác định chiếc xe.
người mẫu
Mẫu xe.
Lợi nhuận
Lợi nhuận thu được khi bán xe là giá bán trừ đi hóa đơn của đại lý. 
Điều này còn được gọi là lợi nhuận gộp trước.

![ILLUSTRATION 7.12](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.12.png)

7.2  Các mối quan hệ dữ liệu được hiển thị như thế nào để khám phá?  7-13
Hình minh họa 7.13 cho thấy mười hàng đầu tiên của tập dữ liệu.
MINH HỌA 7.13    Mười đầu tiên 
Hàng lợi nhuận của đại lý 
Tập dữ liệu. 
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
$ 2,125
$ 2,798
$ 2,144
$ 2,749
$1,810
$1,844
$4,446
$ 3,107
$1,912
$ 2,101
ID
Lợi nhuận
dân sự
CR-V
Odyssey
hiệp định
hiệp định
hiệp định
Odyssey
Phi công
dân sự
dân sự
người mẫu
MINH HỌA 7.14  Trực quan hóa 
mối quan hệ dữ liệu phân phối 
với biểu đồ hình hộp và râu
7.000 USD
6.000 USD
5.000 USD
4.000 USD
3.000 USD
2.000 USD
1.000 USD
8.000 USD
$0
Lợi nhuận
Phân phối lợi nhuận
người mẫu
Loại trung bình
Loại râu
Nghĩa là
Tứ phân vị 1
Tứ phân vị 3
Tối đa
tối thiểu
IQR
Râu trên
Râu dưới
trung vị
Bao gồm
Tối thiểu/Tối đa
2728
1963
2979
6960
340
1016
6960
340
2374
Hình minh họa 7.15 cho thấy cách tạo biểu đồ này trong Power BI. Power BI yêu cầu kéo-
đưa một trường vào khe Trục. Các giá trị cho trường này đại diện cho các điểm dữ liệu. Kéo một 
khóa chính vào vị trí này là một cách làm tốt vì tất cả các điểm dữ liệu và giá trị duy nhất của chúng đều được 
sau đó đại diện. Biểu đồ dạng hộp và râu tương tự cũng có thể được tạo trong Excel. (Dữ liệu Xem 
Làm thế nào để 7.1. ở cuối chương để tìm hiểu cách thực hiện việc này.)
Làm thế nào để
Như đã đề cập trước đó, việc tạo và so sánh nhiều phân phối của cùng một số 
biến dựa trên các giá trị khác nhau của một biến danh nghĩa là phổ biến trong loại phân tích này. 
Hình minh họa 7.16 cho thấy cách tạo biểu đồ với sự so sánh này bằng Power BI:
• Kéo Model vào ô Axis Category I.
• Sau đó, một bản phân phối riêng sẽ được tạo cho từng mô hình.
Hình minh họa 7.14 hiển thị biểu đồ hình hộp và râu cho trường Lợi nhuận. Đại diện vòng tròn màu đỏ-
bực bội với mức trung bình. Phần dưới cùng của hộp màu xanh lá cây là tứ phân vị đầu tiên và phần trên cùng của hộp màu cam 
hộp là tứ phân vị thứ ba. Trung vị là giao điểm giữa các hộp màu xanh lá cây và màu cam, 
và chiều dài của các hộp màu xanh lá cây và màu cam kết hợp là phạm vi liên vùng. Cuối cùng, 
hàng rào phía dưới mô tả giá trị tối thiểu, trong khi hàng rào phía trên mô tả giá trị tối đa. 
Trục
ID
Trục loại I
Thêm trường dữ liệu ở đây
Trục loại II
Thêm trường dữ liệu ở đây
Giá trị
Lợi nhuận
duy nhất
Mã định danh
Các điểm dữ liệu
đại diện trong
phân phối.
số
Biến
Biến số
xác định lĩnh vực nào
đang được khám phá.
MINH HỌA 7.15  Tạo một 
Biểu đồ hình hộp và râu trong Power BI

![ILLUSTRATION 7.16](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.16.png)

7-14  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
Hình minh họa 7.17 là biểu đồ kết quả.
Khám phá và hiểu biết sâu sắc
Kéo và thả các biến cũng hỗ trợ khám phá dữ liệu bằng mẫu này. Sử dụng 
cấu trúc thăm dò cho mối quan hệ dữ liệu phân phối, chúng ta có thể nhanh chóng kiểm tra sự phân bố
sự kết hợp của bất kỳ trường số nào trong tập dữ liệu và sử dụng bất kỳ trường danh nghĩa nào trong tập dữ liệu để so sánh 
phân phối dữ liệu.
Hình minh họa 7.14 cho thấy thông tin phân phối do Power BI cung cấp, bao gồm 
trung vị, giá trị trung bình, khoảng tứ phân vị (IQR), giá trị thấp nhất và giá trị cao nhất. Cái này 
giúp bạn có thể điều tra các ngoại lệ, độ lệch, v.v. Biểu đồ trong Hình minh họa 7.17 
cho phép so sánh nhiều hơn giữa các bản phân phối:
• Lợi nhuận của mô hình Ridgeline cao hơn các mô hình khác.
• Lợi nhuận của các mẫu CR-V và Pilot là như nhau, có nghĩa là có rất ít 
biến thể.
• Lợi nhuận của Odyssey và đặc biệt là dòng xe Civic được dàn trải hơn.
Trục
ID
người mẫu
Trục loại I
Trục loại II
Thêm trường dữ liệu ở đây
Giá trị
Lợi nhuận
duy nhất
Mã định danh
Các điểm dữ liệu
đại diện trong
phân phối.
danh nghĩa
Biến
Các giá trị của
biến danh nghĩa là
dùng để tạo nhiều
phân phối.
số
Biến
Biến số
xác định lĩnh vực nào
đang được khám phá.
MINH HỌA 7.16  Tạo 
Biểu đồ hình hộp và râu với 
Nhiều phân phối
hiệp định
dân sự
CR-V
Odyssey
Phi công
Đường sườn núi
$0
1.000 USD
2.000 USD
3.000 USD
4.000 USD
5.000 USD
6.000 USD
7.000 USD
8.000 USD
Lợi nhuận
người mẫu
Phân phối lợi nhuận theo mô hình
MINH HỌA 7.17  Song song 
Phân phối lợi nhuận cho xe HNA 
Người mẫu

![ILLUSTRATION 7.17](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.17.png)

7.2  Các mối quan hệ dữ liệu được hiển thị như thế nào để khám phá?  7-15
Có thể cần phải khám phá dữ liệu nhiều hơn để hiểu rõ hơn về nguồn gốc của biến thể. 
Nguyên nhân có thể là do giá cao hơn cho một mẫu cụ thể, số lượng tùy chọn 
có sẵn cho một mô hình cụ thể, kỹ năng đàm phán của nhân viên bán hàng hoặc khuyến mãi bán hàng, 
chẳng hạn.
Phân tích phân phối có nhiều ứng dụng, bao gồm phân tích lương thưởng của nhân viên.
chuyện. Để hiểu tiền lương được phân phối như thế nào, phân tích phân phối có thể được sử dụng để trả lời 
những câu hỏi sau:
• Lương có bị lệch phải không? Mức lương cao hơn có dàn trải hơn không?
• So sánh mức lương giữa các phòng ban như thế nào?
• Việc phân bổ thù lao của một tổ chức như thế nào so với việc phân bổ cho 
các tổ chức khác?
Mẫu khám phá dữ liệu 3: Độ lệch
Mối quan hệ dữ liệu sai lệch cho thấy một tập hợp các giá trị thực tế lệch khỏi tham chiếu của chúng như thế nào.
các giá trị xác thực, là các giá trị được dự toán hoặc dự báo. Các mối quan hệ sai lệch là mọi-
kế toán ở đâu. Phân tích phương sai là một ví dụ điển hình, chẳng hạn như sự khác biệt giữa 
chi phí thực tế và tiêu chuẩn. Cấu trúc thăm dò các mối quan hệ sai lệch được thể hiện trong 
Hình minh họa 7.18 chứa biến được so sánh và các biến được sử dụng để kết hợp
mục đích của parison – thực tế, mục tiêu và độ lệch.
MINH HỌA 7.18  Khám phá 
Cấu trúc cho dữ liệu sai lệch 
Mối quan hệ
danh nghĩa
Biến
số
Biến:
Độ lệch
Làm thế nào
so sánh là
đang được thực hiện.
Cái gì đang được
so sánh.
số
Biến:
Mục tiêu
số
Biến:
thực tế
Trực quan hóa
Biểu đồ thanh và cột được nhóm lại (được sử dụng trong ví dụ sau), thước đo, biểu đồ dấu đầu dòng, 
và nhiều hơn nữa có thể được sử dụng để phân tích độ lệch. Hãy tưởng tượng rằng HNA muốn khám phá 
liệu mỗi mẫu xe có đáp ứng được kỳ vọng về doanh số bán hàng hay không. Dữ liệu Công ty có một cái khác

![ILLUSTRATION 7.18](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.18.png)

7-16  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
MINH HỌA 7.19  Doanh số đơn vị dự toán của HNA-2025
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Canada
Canada
Canada
Canada
xe sedan
xe sedan
SUV
SUV
Xe tải nhỏ
xe tải
xe sedan
SUV
xe sedan
SUV
Quốc gia
Loại
dân sự
hiệp định
CR-V
Phi công
Odyssey
Đường sườn núi
dân sự
CR-V
hiệp định
Phi công
Canada
Canada
xe tải
Xe tải nhỏ
255423
344771
252019
125090
139009
54891
480871
98077
319755
47329
88081
19822
300000
350000
25000
160000
145000
55000
425000
110000
275000
45000
65000
30000
Đường sườn núi
Odyssey
người mẫu
Đơn vị ngân sách
Đơn vị thực tế
Tập dữ liệu này được dùng để tạo biểu đồ cột theo nhóm trong Hình minh họa 7.20 với Power BI.
MINH HỌA 7.21  Tạo 
Biểu đồ cột được nhóm trong 
Power BI
Trục
người mẫu
Truyền thuyết
Thêm trường dữ liệu ở đây
Giá trị
Tổng sốĐơn vị thực tế
Tổng số đơn vị dự toán
So sánh thế nào
đang được thực hiện.
danh nghĩa
Biến
Cái gì đang được
so sánh.
số
Biến:
Mục tiêu
số
Biến:
thực tế
664.526
625.000
736.294
725.000
350.096
135.000
172.419
205.000
158.831
175.000
142.972
120.000
Tổng số đơn vị thực tế
Tổng số đơn vị dự toán
100.000
0
200.000 300.000 400.000 500.000 600.000 700.000
hiệp định
dân sự
CR-V
Phi công
Odyssey
Đường sườn núi
người mẫu
Phân tích phương sai: Doanh số bán hàng thực tế so với ngân sách
MINH HỌA 7.20  Trực quan hóa 
mối quan hệ dữ liệu sai lệch với 
Biểu đồ cột nhóm
Hình minh họa 7.21 cho thấy biểu đồ được tạo ra như thế nào.
tập dữ liệu bao gồm cả doanh số bán hàng thực tế và ngân sách cho giai đoạn 2025 
(Minh họa 7.19).

![ILLUSTRATION 7.21](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.21.png)