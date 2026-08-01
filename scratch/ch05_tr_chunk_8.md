5-46  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Ôn tập và thực hành chương
Đánh giá mục tiêu học tập
❶  Giải thích quy trình lập hồ sơ dữ liệu.
Lập hồ sơ dữ liệu là quá trình điều tra chất lượng và cấu trúc dữ liệu
ture. Nó có ba phần:
•  Điều tra chất lượng dữ liệu: Xác định xem có bất thường nào trong 
dữ liệu. Nói cách khác, dữ liệu có bị bẩn không?
•  Điều tra cấu trúc dữ liệu: Cải thiện tổ chức của 
dữ liệu phục vụ cho mục đích phân tích. 
•  Quyết định và thông báo: Quyết định xem có nên giải quyết vấn đề hay không 
được xác định, chi phí để thực hiện việc đó và hậu quả của việc không 
giải quyết các vấn đề.
❷  Mô tả quá trình trích xuất-chuyển đổi-tải (ETL).
Trích xuất, chuyển đổi, tải (ETL) là một quá trình khắc phục các vấn đề về dữ liệu:
•  Quá trình trích xuất đang di chuyển dữ liệu đến khu vực tổ chức để chuyển đổi
mục đích hoạt động.
•  Chuyển đổi liên quan đến việc cải thiện dữ liệu trong ba giai đoạn phụ
các quá trình: làm sạch, tái cấu trúc và tích hợp.
•  Quá trình tải xảy ra khi dữ liệu được di chuyển đến khu vực nơi chúng 
sẽ được sử dụng để phân tích.
❸  Áp dụng các mẫu để trích xuất dữ liệu.
Các mẫu chuẩn bị dữ liệu là một công cụ mạnh mẽ cho dự án chuẩn bị dữ liệu
vân vân. Chúng giúp xác định các vấn đề về dữ liệu và cung cấp hướng dẫn để phát hiện 
và sửa chúng. Địa chỉ mẫu trích xuất dữ liệu:
• Việc truyền dữ liệu không đầy đủ.
• Việc truyền dữ liệu không chính xác.
❹  Áp dụng các mẫu để chuyển đổi các cột.
Phép biến đổi làm sạch dữ liệu bằng cách sửa các giá trị (chất lượng) và 
tái cấu trúc và tích hợp các cấu trúc dữ liệu để phân tích (cấu trúc
đúng vậy). Có thể tiến hành dần dần theo cột, bảng, mô hình 
cấp độ. 
Các mẫu chuyển đổi cột giải quyết các vấn đề về dữ liệu trong một cột duy nhất.
ừm. Địa chỉ mẫu cột định hướng cấu trúc:
• Các cột chứa dữ liệu không liên quan và không đáng tin cậy.
• Tên cột không chính xác và mơ hồ.
• Kiểu dữ liệu không chính xác.
• Cột kết hợp hoặc nhiều giá trị.
Địa chỉ mẫu cột hướng tới chất lượng: 
• Cột có dữ liệu không chính xác. 
• Dữ liệu không nhất quán trong các cột. 
• Cột có dữ liệu không đầy đủ.
• Cột có dữ liệu không hợp lệ.
❺  Áp dụng các mẫu để chuyển đổi bảng.
Các mẫu chuyển đổi bảng giải quyết các vấn đề về dữ liệu trong một 
cái bàn. Địa chỉ các mẫu bảng định hướng cấu trúc:
• Tên bảng không trực quan và mơ hồ.
• Các bảng không có khóa chính.
• Bảng có từ hai cột trở lên có nội dung chồng chéo.
Địa chỉ mẫu bảng định hướng chất lượng:
• Các giá trị không hợp lệ có thể được xác định bằng các quy tắc trong bảng.
❻  Áp dụng các mẫu để chuyển đổi mô hình.
Các mẫu chuyển đổi mô hình giải quyết các vấn đề về dữ liệu trên các bảng. 
Địa chỉ các mẫu mô hình hướng cấu trúc:
• Kết hợp các bảng có cấu trúc tương tự bằng phép hợp. Com-
các bảng bining có các đặc điểm khác nhau cho cùng một 
thực thể có sự hợp nhất.
• Tuân thủ các nguyên tắc mô hình hóa chiều.
Địa chỉ mẫu bảng định hướng chất lượng:
• Giá trị không hợp lệ có thể được xác định bằng quy tắc liên bảng.
❼  Áp dụng các mẫu cho các vấn đề tải dữ liệu.
Trích xuất và tải đều là các quá trình chuyển giao và do đó có 
các vấn đề dữ liệu tương tự:
• Việc truyền dữ liệu không đầy đủ.
• Việc truyền dữ liệu không chính xác.
Ngoài ra, khi dữ liệu đã được tải, điều quan trọng là:
• Kiểm tra xem mô hình dữ liệu có đầy đủ và chính xác không.
Hình minh họa 5.45 cung cấp cái nhìn tổng quan về 20 mẫu chuẩn bị dữ liệu. Cột đầu tiên 
hiển thị số nhận dạng để dễ tham khảo và mã ở cột thứ hai cho biết liệu 
một mẫu tập trung vào các giá trị (V) hoặc tái cấu trúc dữ liệu (S). Biểu đồ cũng bao gồm vấn đề dữ liệu và 
cách phát hiện và khắc phục.

![ILLUSTRATION 5.45](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.45.png)

Ôn tập mục tiêu học tập  5-47
MINH HỌA 5.45  Tổng quan về 
Mẫu chuẩn bị dữ liệu
Khai thác
Mã
Mã
vấn đề
Phát hiện (Hồ sơ dữ liệu)
Đúng (ETL)
1
V.
Tất cả dữ liệu không 
chuyển nhượng. 
So sánh số hàng.
Thêm các hàng còn thiếu.
2
V.
Dữ liệu không chính xác 
được chuyển giao.
So sánh số lượng kiểm soát
Sửa đổi các giá trị không chính xác. 
Chuyển đổi
Mã
Vấn đề về mã
Phát hiện (Hồ sơ dữ liệu)
Đúng (ETL)
Cột
3
S
Không liên quan hoặc không đáng tin cậy 
dữ liệu.
Quét trực quan các cột để tìm 
dữ liệu không liên quan và không đáng tin cậy. 
Xóa cột bằng 
dữ liệu không liên quan và không đáng tin cậy. 
4
S
Không chính xác hoặc mơ hồ 
dữ liệu.
Quét cột để tìm lỗi hoặc 
những cái tên mơ hồ. 
Đổi tên cột.
5
S
Các loại dữ liệu không chính xác.
Kiểm tra kiểu dữ liệu. 
Thay đổi kiểu dữ liệu.
6
S
Các cột không 
có giá trị đơn.
Xét các giá trị trong 
cột. 
Tách các cột tổng hợp.
Tạo một bảng riêng cho 
cột nhiều giá trị.
7
V.
Giá trị không chính xác.
Phát hiện các giá trị không chính xác với 
ngoại lệ. 
Sửa đổi các giá trị không chính xác. 
8
V.
Các giá trị không nhất quán
Xác định các giá trị không nhất quán 
Sửa đổi các giá trị không nhất quán. 
9
V.
Các giá trị không đầy đủ
Điều tra các giá trị null. 
Xóa các cột hoặc 
thay thế các giá trị null.
10
V.
Giá trị không hợp lệ.
Tạo và áp dụng xác thực 
quy luật. 
Sửa đổi các giá trị không hợp lệ. 
Bảng
11
S
Không chính xác hoặc mơ hồ 
tên bảng.
Quét trực quan bảng để tìm 
tên không chính xác hoặc mơ hồ. 
Đổi tên bảng. 
12
S
Thiếu khóa chính.
Xác định các bảng thiếu một 
khóa chính. 
Tạo khóa chính.
13
S
Cột dư thừa 
nội dung.
Thực hiện theo từng cột 
so sánh. 
Xóa phần thừa và 
dữ liệu phụ thuộc. 
14
V.
Đã phát hiện giá trị không hợp lệ 
với các quy tắc trong bảng.
Tạo và áp dụng nội bảng 
quy tắc xác nhận. 
Sửa đổi dữ liệu không hợp lệ.
người mẫu
15
S
Dữ liệu trải rộng trên các bảng. Xác định các bảng có điểm tương tự 
cấu trúc hoặc bảng mô tả 
đặc điểm khác nhau của 
cùng một thực thể. 
Liên kết hoặc hợp nhất các bảng. 
16
S
Tuân thủ 
mô hình chiều 
nguyên tắc. 
Phân tích mô hình dữ liệu 
tuân thủ kích thước 
nguyên tắc mô hình hóa. 
Tái cơ cấu mô hình như một ngôi sao/
lược đồ bông tuyết. 
17
V.
Đã phát hiện giá trị không hợp lệ 
với các quy tắc liên bảng.
Tạo và áp dụng liên bảng 
quy tắc xác nhận. 
Sửa đổi các quy tắc không hợp lệ. 
Đang tải
Mã
Vấn đề về mã
Phát hiện (Hồ sơ dữ liệu)
Đúng (ETL)
18
V.
Tải dữ liệu không đầy đủ. 
So sánh số hàng.
Thêm dữ liệu còn thiếu.
19
V.
Tải dữ liệu không chính xác. 
So sánh số lượng kiểm soát
Sửa đổi các giá trị không chính xác. 
20
S
Dữ liệu bị thiếu hoặc không chính xác 
các mối quan hệ. 
Điều tra tính đầy đủ 
và độ chính xác của dữ liệu 
mô hình.
Tạo, sửa đổi và xóa 
mối quan hệ 
Sửa đổi mô hình dữ liệu. 
Mẫu chuẩn bị dữ liệu

5-48
CHƯƠNG 5 Phân tích: Chuẩn bị dữ liệu
 Đánh giá các điều khoản chính
 Cơ sở dữ liệu phân tích 5-5 
 Số lượng 5-8 
 Cột tổ hợp 5-5 
 Đầu nối dữ liệu 5-10 
 Từ điển dữ liệu 5-15 
 Trích xuất dữ liệu 5-10 
 Tích hợp dữ liệu 5-13 
 Đang tải dữ liệu 5-14 
 Khớp dữ liệu 5-13 
 Mô hình dữ liệu 5-7 
 Chuẩn bị dữ liệu 5-2 
 Lập hồ sơ dữ liệu 5-2 
 Tái cấu trúc dữ liệu 5-13 
 Chuyển đổi dữ liệu 5-10 
 Kho dữ liệu 5-10 
 Kích thước 5-8 
 Dữ liệu bẩn 5-2 
 Trích xuất-chuyển đổi-tải (ETL) 5-10 
 Sự kiện 5-7 
Bàn phẳng 5-6 
Hợp nhất 5-13 
Cột đa giá trị 5-6 
Ngoại lệ 5-25 
 Tính toàn vẹn tham chiếu 5-39 
 Cột có giá trị đơn 5-5 
Cắt 5-5
Lược đồ bông tuyết 5-36 
 Lược đồ sao 5-7 
 Liên minh 5-13 
Quy tắc xác thực 5-3
 CÁCH 5.1 
Dữ liệu hồ sơ với Power Query 
 Power Query tích hợp các công cụ lập hồ sơ dữ liệu tuyệt vời. Hãy xem xét nó có thể giúp ích như thế nào với hàng 
số lượng, số lượng kiểm soát và thông tin phân phối. 
 Những gì bạn cần:
dữ liệu
Tệp dữ liệu How To 5.1. 
 BƯỚC 1: Trích xuất dữ liệu từ tệp dữ liệu. Có nhiều bước khác nhau để trích xuất dữ liệu từ 
Excel so với Power BI. Nếu bạn đang sử dụng Excel: 
• Trước tiên, hãy mở một sổ làm việc Trống và nhấp vào Dữ liệu > Từ Tệp > Từ Sổ làm việc Excel
(Minh họa 5.46).
Làm thế nào để
MINH HỌA 5.46 Trích xuất dữ liệu từ tệp Excel
Thuộc tính
Truy vấn & Trình kết nối
Chỉnh sửa liên kết
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
Công thức
Bố cục trang
Từ Excel
Nhập dữ liệu
sổ làm việc
Xem lại
Xem
Trợ giúp
Làm mới
Tất cả
Thuộc tính
Truy vấn & Trình kết nối
Chỉnh sửa liên kết
Từ văn bản/CSV
Từ Web
Từ Bảng/Phạm vi
Kết nối hiện có
Nguồn gần đây
Làm mới
Tất cả
Tất cả
Từ tập tin
Từ cơ sở dữ liệu 
Từ Azure
Từ sổ làm việc Excel
Từ văn bản/CSV
Từ XML
Từ JSON
X
JSON
Từ Power BI (Miền Bắc III...))
dữ liệu
1
2
3
H
Cách đi qua

![ILLUSTRATION 5.46](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.46.png)

Cách đi qua 5-49
• Tiếp theo, chọn tệp Beans Excel và nhấp vào Nhập. Một hộp thoại Điều hướng sẽ mở ra. chọn 
bảng Dịch vụ và nhấp vào Tải (Minh họa 5.47).
 MINH HỌA 5.47 Chọn và tải bảng dịch vụ
Tùy chọn hiển thị
Điều hướng
Chọn nhiều mục
Ngày
Thời gian thực tế
Thời gian dự toán
ID_1
ID
ID
1/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
Khu vực
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
2
1
1
1
1
1
1
1
1
3,5
2,5
0,1
0,3
0,1
0,4
0,1
0,3
0,2
1
2
3
4
5
6
7
8
9
Dịch vụ
3,75
2,65
0,07
0,35
0,1
0,35
0,07
0,25
0,25
Dịch vụ
ClData
E-Dem
Đậu (1).xlsx [4]
nhân viên
Hủy bỏ
Chuyển đổi dữ liệu
Tải
Từ văn bản/CSV
Từ Web
Từ Bảng/Phạm vi
Kết nối hiện có
Nguồn gần đây
Tập tin
Trang chủ
Chèn
Bố cục trang
Công thức
dữ liệu
Làm mới
Tất cả
Có được thời gian
ID
3,5
2,5
0,1
0,3
0,1
0,4
0,1
0,3
0,2
0,5
0,5
0,1
0,7
0,1
Kết hợp truy vấn
Khởi chạy Trình soạn thảo Power Query...
Cài đặt nguồn dữ liệu...
Tùy chọn truy vấn
Từ tập tin
Từ cơ sở dữ liệu 
Từ Azure
Từ các nguồn khác
Từ dịch vụ trực tuyến
Từ Power BI (Miền Bắc III...)
Từ văn bản/CSV
Từ Web
Từ Bảng/Phạm vi
Kết nối hiện có
Nguồn gần đây
Làm mới
Tất cả
Tất cả
Nhận
dữ liệu
MINH HỌA 5.48 Mở Power Query
• Cuối cùng, nhấp vào tab Data và sau đó nhấp vào mũi tên xuống trong Get Data. Tiếp theo, bạn sẽ thấy 
tùy chọn để khởi chạy Power Query Editor. Bấm để mở Trình soạn thảo truy vấn (Minh họa 5.48).

![ILLUSTRATION 5.48](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.48.png)

5-50
CHƯƠNG 5 Phân tích: Chuẩn bị dữ liệu
Nếu bạn đang sử dụng Power BI: 
• Mở tệp Power BI mới và chọn Excel trong nhóm Dữ liệu. Hình minh họa 5.49 cho thấy 
Tab Trang chủ của Power BI, bao gồm nhóm Dữ liệu.
 MINH HỌA 5.49 Trích xuất dữ liệu từ tệp Excel
Nhận
dữ liệu
Tập tin
Làm người mẫu
Chèn
Xem
Trợ giúp
dữ liệu
Trang chủ
Power BI
bộ dữ liệu
SQL
Máy chủ
+
Nhập
dữ liệu
Gần đây
nguồn
Dán
Cắt
Sao chép
định dạng
họa sĩ
Excel
X
Dữ liệu ngược
dữ liệu
Power BI
bộ dữ liệu
SQL
Máy chủ
+
Nhập
dữ liệu
Gần đây
nguồn
Dữ liệu ngược
Bảng nhớ tạm
Nhận
dữ liệu
Dán
Cắt
Sao chép
định dạng
họa sĩ
Bảng nhớ tạm
• Tiếp theo, chọn file Beans Excel và nhấn Open. Một hộp thoại Điều hướng sẽ mở ra. chọn 
bảng Dịch vụ và nhấp vào Tải (Minh họa 5.50).
 MINH HỌA 5.50 Chọn và tải bảng dịch vụ
Bản xem trước được tải xuống vào Thứ Tư, ngày 9 tháng 3 năm 2022
Tùy chọn hiển thị
Điều hướng
Dịch vụ
Đậu.xlsx [4]
Dịch vụ
ClData
E-Dem
nhân viên
Ngày
Thời gian thực tế
Thời gian dự toán
ID_1
ID
ID
Khu vực
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Thuế
Kế toán
Thuế
Kế toán
Kế toán
Kế toán
Kế toán
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
11
12
13
14
15
16
17
18
19
20
21
22
1/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
2/1/2025
3,75
2,65
0,07
0,35
0,1
0,35
0,07
0,25
0,25
0,75
0,75
0,1
0,75
0,1
0,25
0,07
0,35
0,07
0,07
0,35
3,95
4
3,5
2,5
0,1
0,3
0,1
0,4
0,1
0,3
0,2
0,5
0,5
0,1
0,7
0,1
0,2
0,1
0,4
0,1
0,1
0,5
3,8
2,8
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
2
1
1
1
1
1
1
1
1
2
8
1
8
1
1
1
1
4
1
1
1
2
Tải
Chuyển đổi dữ liệu
Hủy bỏ

![ILLUSTRATION 5.50](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.50.png)

Cách thực hiện bước 5-51
• Cuối cùng, nhấp vào Chuyển đổi dữ liệu trong nhóm Truy vấn của tab Trang chủ để khởi chạy Power 
Truy vấn (Minh họa 5.51). 
Các bước còn lại giống hệt đối với Excel và Power BI. 
 BƯỚC 2: Nhấp vào tab Xem trong menu chính ( Minh họa 5.52 ). Chọn chất lượng cột, 
Phân phối cột và cấu hình cột.
 MINH HỌA 5.51 Mở Power Query
Nhận
dữ liệu
Tập tin
Trang chủ
Làm người mẫu
Chèn
Xem
Trợ giúp
Bảng nhớ tạm
Làm mới
chuyển đổi
dữ liệu
dữ liệu
Excel
X
Power BI
bộ dữ liệu
SQL
Máy chủ
+
Nhập
dữ liệu
Gần đây
nguồn
Power BI
Dán
Cắt
Sao chép
định dạng
họa sĩ
Nhận
dữ liệu
Bảng nhớ tạm
dữ liệu
Excel
X
Power BI
bộ dữ liệu
SQL
Máy chủ
+
Nhập
dữ liệu
Gần đây
nguồn
Dán
Cắt
Sao chép
định dạng
họa sĩ
Làm mới
1
 MINH HỌA 5.52 Tùy chọn cấu hình cột 
Truy vấn
Cài đặt
Thanh công thức
Cách đơn
Chất lượng cột
Hiển thị khoảng trắng
Hồ sơ cột
Phân phối cột
Đi tới
Cột
Cột
Nâng cao
Biên tập viên
Nâng cao
Truy vấn
phụ thuộc
phụ thuộc
Luôn cho phép
Thông số
Xem trước dữ liệu
Bố cục
Tập tin
Trang chủ
chuyển đổi
Thêm cột
Công cụ
Trợ giúp
Xem
Truy vấn
Cài đặt
Thanh công thức
Bố cục
Đi tới
Cột
Cột
Nâng cao
Biên tập viên
Nâng cao
Truy vấn
phụ thuộc
phụ thuộc
Luôn cho phép
Thông số
2
Hình minh họa 5.53 cho thấy Power Query hiện hiển thị thông tin hồ sơ chi tiết cho từng 
cột. Phần trăm hợp lệ, lỗi và phần trăm trống xuất hiện khi chất lượng Cột được kiểm tra. các 
phân phối tần số xuất hiện khi bạn kiểm tra phân phối Cột. 
 MINH HỌA 5.53 Chất lượng cột và thông tin phân phối
hợp lệ
Lỗi
trống
100%
0%
0%
hợp lệ
Lỗi
trống
100%
0%
0%
hợp lệ
Lỗi
trống
100%
0%
0%
1000 khác biệt, 1000 độc đáo
45 khác biệt, 5 độc đáo
103 khác biệt, 38 độc đáo
1.2 Thời gian thực tế
Ngày
ID
123
3
 BƯỚC 3: Chọn cột ID. Khi góc dưới cùng bên trái của cửa sổ Power Query hiển thị
 (Minh họa 5.54), cấu hình cột hiện dựa trên 1000 hàng trên cùng.
 MINH HỌA 5.54 Cấu hình cột dựa trên mẫu
10 CỘT, 999+ HÀNG Cấu hình cột dựa trên 1000 hàng trên cùng

![ILLUSTRATION 5.54](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.54.png)