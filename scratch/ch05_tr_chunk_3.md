5-14  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Tải dữ liệu
Sau khi dữ liệu được làm sạch và chuyển đổi, chúng sẽ được tải vào phần mềm để phân tích. 
Tải dữ liệu là quá trình làm cho cơ sở dữ liệu phân tích có sẵn để sử dụng. phân tích 
cơ sở dữ liệu thường được đăng trên đám mây nơi chúng có thể được nhiều người dùng sử dụng đồng thời. 
Giống như trích xuất, một phần của việc truyền dữ liệu là xác thực xem tất cả các bản ghi đã được chuyển chưa 
và liệu chúng có được chuyển giao chính xác hay không.
Áp dụng nó 5.2
Kết hợp các bảng cho 
Phân tích
Giám đốc điều hành Stufan Shanice đề xuất tổ chức dữ liệu sản phẩm thành ba bảng riêng biệt, với một bảng dành cho 
từng loại sản phẩm. Cô ấy hỏi liệu có vấn đề gì khi kết hợp ba bảng để phân tích hay không. Làm thế nào 
bạn sẽ trả lời chứ?
BERL
DUCH
tháng 3
THO
TOU
Berlioz
nữ công tước
Marie
Thomas
Toulouse
Mã
Mô tả
23
44
34
19
32
QOH
quý tộc
CAPH
SNO
TINL
hộp thiếc
Thuyền trưởng Haddock
có tuyết
Tintin lớn
Tintin Nhỏ
Mã
Mô tả
14
22
23
44
QOH
tintin
BASHL
BASH
DOCL
TÀI LIỆU
DOPL
Rụt rè lớn
Rụt rè nhỏ
Tài liệu lớn
Tài liệu nhỏ
ngu ngốc lớn
DOPS
ngu ngốc nhỏ
GRUML Gắt gỏng Lớn
Nhỏ gắt gỏng
Hạnh phúc lớn
Hạnh Phúc Nhỏ
Hắt hơi lớn
Hắt hơi nhỏ
Bạch Tuyết Lớn
Bạch Tuyết Nhỏ
buồn ngủ lớn
buồn ngủ nhỏ
GRUMS
HAPL
HAPS
SLB
SNEL
SLS
SNES
TUYẾT
SNWS
Mã
Mô tả
người lùn
GIẢI PHÁP
• Ba bảng không thể được kết hợp bằng cách sử dụng phép hợp do cấu trúc bảng dành cho Người lùn 
bảng khác với cấu trúc bảng của bảng Aristocats và Tintin. QOH 
cột bị thiếu.
• Danh mục sản phẩm được xác định theo tên bảng và không thể sử dụng cho mục đích phân tích
tư thế. Một cột Danh mục cần được thêm vào mỗi bảng trong số ba bảng.
5.3  Những mẫu nào trích xuất dữ liệu?
MỤC TIÊU HỌC TẬP ➌
Áp dụng các mẫu để trích xuất dữ liệu.
Mỗi dự án phân tích dữ liệu đều có những thách thức chuẩn bị dữ liệu riêng. Mặc dù không có một chiếc nào, 
cách tiếp cận chung cho tất cả các dự án, một tập hợp các mẫu chuẩn bị dữ liệu có cấu trúc có thể giải quyết hầu hết 
những thách thức. Những mẫu này báo hiệu các vấn đề tiềm ẩn và cung cấp hướng dẫn để tìm ra chúng 
trong tập dữ liệu và sửa chúng. Mỗi mẫu xác định một vấn đề về dữ liệu, thảo luận cách giải quyết 
phát hiện nó bằng phương pháp định hình và giải thích một hoặc nhiều phương pháp ETL để sửa nó. nghĩ về 
các mẫu như một menu; bạn có thể chọn những cái phù hợp nhất với nhu cầu của bạn.

![Apply It 5.2](../TaiLieu/textbookForPractice/Figures/Ch_05/Apply%20It%205.2.png)

5.3  Những mẫu nào trích xuất dữ liệu?  5-15
Dữ liệu   Hãy sử dụng một trường hợp để minh họa cách áp dụng các mẫu chuẩn bị dữ liệu trong thế giới thực 
kịch bản. Bạn cũng có thể sử dụng dữ liệu có sẵn để tự mình xử lý từng mẫu. 
Beans là một công ty kế toán ở Okemos, Michigan cung cấp dịch vụ kế toán và thuế. 
Petra, đối tác quản lý của họ, đã ưu tiên cải thiện việc phân tích các dịch vụ của họ trong 
năm mới. Petra không ngại thực hiện việc phân tích nhưng gặp khó khăn trong việc tích hợp các dữ liệu khác nhau 
nguồn. Hãy tưởng tượng bạn là một trong những nhân viên kế toán giúp chuẩn bị dữ liệu.
Bộ dữ liệu cho Beans bao gồm bốn bảng tính trong một tệp Excel (Minh họa 5.12). 
$
MINH HỌA 5.12  Bảng tính trong Tập dữ liệu Beans
Bảng tính
Mô tả
ClData
Thông tin về khách hàng của Beans.
nhân viên
Thông tin chung về nhân viên Beans.
E-Dem
Thông tin nhân khẩu học về nhân viên của Bean.
Dịch vụ
Thông tin về các dịch vụ được cung cấp trong khoảng thời gian từ tháng 1 đến tháng 7 năm 2025.
Bước đầu tiên là xác định dữ liệu có sẵn và tạo từ điển dữ liệu, biểu đồ 
cho biết dữ liệu nào có sẵn và chúng có thể được tìm thấy ở đâu. Một bản ghi từ điển dữ liệu khác nhau-
các mẩu thông tin cho từng trường, bao gồm tên, mô tả ngắn gọn về nội dung, dữ liệu 
loại, trường là khóa chính hay khóa ngoại và trường đó là bắt buộc hay tùy chọn.
Từ điển dữ liệu thường được gọi là siêu dữ liệu - đó là dữ liệu về dữ liệu. Nó được xây dựng dần dần 
trong suốt quá trình chuẩn bị dữ liệu, nhưng việc tạo tên cột và mô tả là một điều tốt 
điểm khởi đầu. Hình minh họa 5.13 cho thấy bản nháp đầu tiên của từ điển dữ liệu cho tập dữ liệu Beans. 
(Xem Minh họa 5.44 ở cuối chương để biết ví dụ về từ điển dữ liệu hoàn chỉnh.)
MINH HỌA 5.13  Từ điển dữ liệu Beans
ClData
Tên
Mô tả
ID
ID duy nhất của khách hàng.
Tên
Tên của khách hàng.
Tên ngành
Ngành công nghiệp của khách hàng.
nhân viên
Tên
Mô tả
ID
ID của nhân viên.
Tên
Tên của một nhân viên.
Chức danh
Chức danh công việc của một nhân viên.
tỷ lệ
Mức lương theo giờ của một nhân viên.
văn phòng
Văn phòng của một nhân viên.
MS
Tình trạng hôn nhân của một nhân viên.
E-Dem
Tên
Mô tả
đầu tiên
Tên của một nhân viên.
Cuối cùng
Họ của nhân viên.
Tuổi
Độ tuổi của nhân viên
Danh sách chứng chỉ
Danh sách các chứng chỉ của nhân viên.
Đại học
Trường đại học mà nhân viên đã nhận được bằng đại học.
(Tiếp theo)

![ILLUSTRATION 5.44](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.44.png)

5-16  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Dịch vụ
Tên
Mô tả
ID
ID duy nhất cho dịch vụ được cung cấp.
Ngày
Ngày thực hiện dịch vụ.
Thời gian thực tế
Thời gian thực tế dành cho một dịch vụ được cung cấp.
Thời gian dự kiến
Thời gian dự kiến cho một dịch vụ được cung cấp.
ID
ID của nhiệm vụ được thực hiện.
Khu vực
Khu vực nhiệm vụ
Nhiệm vụ
Tên của nhiệm vụ được thực hiện.
ID nhân viên
ID của nhân viên thực hiện nhiệm vụ.
MINH HỌA 5.13  (Tiếp theo)
MINH HỌA 5.14  Đếm hàng cho bảng tính Excel
ngoại hối
Tự động Lưu
Oﬀ
khách hàng
nhân viên
Nhiệm vụ
Khu vực
ID
Thời gian dự toán
Thời gian thực tế
Ngày
1 
ID
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
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
Kế toán
5/1/2023
6/1/2023
6/1/2023
6/1/2023
6/1/2023
6/1/2023
6/1/2023
6/1/2023
6/1/2023
3,75
2,65
0,25
0,25
0,07
0,07
0,35
0,35
0,1
3,5
2,5
0,3
0,2
0,1
0,1
0,3
0,4
0,1
2
1
1
1
1
1
1
1
1
Xem lại
chuẩn bị
chuẩn bị
chuẩn bị
chuẩn bị
chuẩn bị
chuẩn bị
chuẩn bị
chuẩn bị
18
15
12
9
2
9
12
15
17
42
103
178
178
2
2
2
2
2
A
B
C
D
E
F
G
H
tôi
J
Dịch vụ
CLdate Nhân viên E-DEM
Thống kê sổ làm việc
Khóa mũ
Trung bình: 2316,5
Tổng: 10730028
Đếm: 4633
Số đếm: 4632
Tối thiểu: 1
Tối đa: 4632
Chọn “ID”
Cột
Trạng thái
thanh
Tổng số kiểm soát:
trung bình
Tổng số kiểm soát:
Tổng
Số lượng
Hàng
Bắt đầu từ từ điển dữ liệu trong Hình minh họa 5.13, chúng ta sẵn sàng chuẩn bị dữ liệu bằng cách áp dụng-
có hai mươi mẫu. Hai mẫu đầu tiên là các mẫu trích xuất để xác định xem tất cả dữ liệu đã được 
được trích xuất và liệu chúng có được chuyển chính xác hay không.
Mẫu chuẩn bị dữ liệu 1: Dữ liệu chưa đầy đủ 
Chuyển khoản
Quá trình trích xuất sẽ chuyển dữ liệu từ các tệp nguồn sang công cụ ETL để xử lý thêm. Một 
truyền dữ liệu không đầy đủ và dữ liệu bị thiếu dẫn đến kết quả không đáng tin cậy.
So sánh số hàng
So sánh số lượng hàng là một cách để kiểm tra tính đầy đủ. Làm việc với tập dữ liệu Beans, 
kiểm tra tính đầy đủ bằng cách so sánh số hàng của bảng tính Excel với số hàng tương ứng 
số hàng của bảng trong công cụ ETL. Hình minh họa 5.14 hiển thị bảng tính Service Excel. Khi nào 
cột ID được chọn, thanh trạng thái của Excel hiển thị có 4.632 hàng trong bảng tính.

![ILLUSTRATION 5.14](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.14.png)

5.3  Những mẫu nào trích xuất dữ liệu?  5-17
Tiếp theo, xác định số hàng cho bảng Dịch vụ trong công cụ ETL được sử dụng để trích xuất. Ảo tưởng-
Phiên bản 5.15 hiển thị thông tin đó như một phần của cấu hình cột ID trong Power Query. các 
các số trùng khớp cho biết tất cả các hàng đã được chuyển. Nếu các con số không khớp nhau, 
chúng ta phải xác định dữ liệu nào không được chuyển và nguyên nhân gây ra sự cố. Cho 
tính chất tuần tự của ID, phân tích khoảng cách có thể là một công cụ hữu ích để thực hiện việc này. Trong trường hợp này, có 
không có sự cố chuyển dữ liệu nào khi trích xuất dữ liệu từ tập dữ liệu Beans vào Power Query.
MINH HỌA 5.15  Đếm hàng với Power Query
Thống kê cột
Đếm
4.632
Lỗi
0
trống
0
khác biệt
4.632
duy nhất
4.632
NaN
0
số không
0
tối thiểu
1
Tối đa
4.632
trung bình
2.316,5
Độ lệch chuẩn
1.337,28...
Thậm chí
2.316
Lẻ
2.316
Số hàng
Tổng số kiểm soát:
trung bình
Thêm hàng bị thiếu
Nếu số lượng hàng không khớp, hãy thêm các hàng bị thiếu vào dữ liệu nguồn, bảng tính Dịch vụ 
trong tệp tập dữ liệu Beans hoặc vào tập dữ liệu của ETL.
Tóm tắt Mẫu 1
vấn đề
Tất cả dữ liệu không được chuyển.
Phát hiện (Hồ sơ dữ liệu)
So sánh số hàng.
Đúng (ETL)
Thêm các hàng còn thiếu.
Mẫu chuẩn bị dữ liệu 2: Dữ liệu không chính xác 
Chuyển khoản
Ngay cả khi tất cả các hàng đã được chuyển, dữ liệu có thể chưa được chuyển đúng.
trực tiếp. Điều này thường xảy ra do sự khác biệt về kiểu dữ liệu.
So sánh số tiền kiểm soát
Vấn đề này có thể được phát hiện bằng cách sử dụng số lượng kiểm soát. Trong tập dữ liệu Beans, so sánh giá trị trung bình 
trong bảng tính Excel (Minh họa 5.14) với cùng số cho bảng Dịch vụ trong bảng 
Công cụ ETL (Minh họa 5.15). Các số trùng khớp biểu thị sự chuyển giao chính xác các giá trị cho 
Cột ID trong bảng Dịch vụ. Các thử nghiệm tương tự có thể được thực hiện cho các cột khác.

![ILLUSTRATION 5.15](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.15.png)

5-18  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Sửa đổi giá trị không chính xác
Không có số lượng kiểm soát khác nhau khi lấy dữ liệu từ bảng tính Beans Excel-
trang tính vào Power Query. Nhưng nếu các con số không khớp nhau, bước tiếp theo là xác định xem số nào 
dữ liệu được truyền không chính xác và nguyên nhân gây ra sự cố. Sau khi được xác định, sự kết hợp
các giá trị được truyền trực tiếp trong tập dữ liệu của ETL có thể được sửa đổi.
Tóm tắt mẫu 2
vấn đề
Dữ liệu không được truyền chính xác.
Phát hiện (Hồ sơ dữ liệu)
So sánh số lượng kiểm soát
Đúng (ETL)
Sửa đổi các giá trị không chính xác.
Kiểm tra tính đầy đủ và chính xác của việc truyền dữ liệu là một hoạt động phổ biến đối với hoạt động kiểm toán.
tors. Khách hàng cung cấp dữ liệu qua email, chia sẻ đám mây, chuyển USB, v.v. 
số liệu thống kê được tạo ở phía người gửi và người nhận giúp phát hiện các vấn đề chuyển tiền.
Áp dụng nó 5.3
Trích xuất dữ liệu với 
mẫu
Dữ liệu   Shanice đưa cho bạn, một nhân viên kế toán làm việc cho Stufan, một tệp văn bản chứa các giao dịch bán hàng của Stufan.
thông tin. Cô ấy cũng cung cấp các thông tin sau:
•  Số lượng giao dịch: 28
•  Giá trung bình được tính: 25,32
1. Trích xuất dữ liệu bán hàng vào công cụ ETL của bạn.
2. Xác định xem tất cả các giao dịch có được chuyển đi hay không và liệu tất cả dữ liệu có được chuyển chính xác hay không.
GIẢI PHÁP
	 1. Đầu tiên, trích xuất dữ liệu vào Excel. Tiếp theo, mở trình soạn thảo Power Query và kiểm tra hồ sơ 
cho cột Giá.
Thống kê cột
Đếm
28
Lỗi
0
trống
0
khác biệt
8
duy nhất
4
NaN
0
số không
0
tối thiểu
10
Tối đa
40
trung bình
25.3214...
	 2. Như hình ảnh hiển thị, thông tin được cung cấp cho biết tất cả các giao dịch đã được chuyển–
Đếm: 28– và chúng đã được chuyển chính xác–Trung bình: 25,32.

![Apply It 5.3](../TaiLieu/textbookForPractice/Figures/Ch_05/Apply%20It%205.3.png)

5.4  Cột chuyển đổi mẫu nào?  5-19
5.4  Những mẫu nào biến đổi 
Cột?
MỤC TIÊU HỌC TẬP ❹
Áp dụng các mẫu để chuyển đổi cột.
Sau khi tất cả dữ liệu được chuyển sang công cụ ETL, đã đến lúc chuyển đổi chúng. Sự chuyển hóa có 
hai mục đích – làm sạch dữ liệu bằng cách sửa các giá trị và tái cấu trúc và tích hợp 
dữ liệu cho việc phân tích.
Cơ sở dữ liệu phân tích bao gồm một bộ bảng tích hợp, là mô hình dữ liệu, 
và mỗi bảng có nhiều cột. Điều này có nghĩa là các phép biến đổi có thể được thực hiện 
dần dần ở cấp độ cột, cấp độ bảng và cấp độ mô hình. Phần này tập trung vào việc chuyển
mô hình hình thành ở cấp độ cột. Các mẫu này tìm kiếm các vấn đề về dữ liệu trong một 
cột, chẳng hạn như tên không rõ ràng, vấn đề về kiểu dữ liệu và không chính xác, không nhất quán, không đầy đủ, 
hoặc các giá trị không hợp lệ.
Mẫu chuẩn bị dữ liệu 3: Không liên quan và  
Dữ liệu không đáng tin cậy
Dữ liệu không liên quan đến các quyết định sẽ làm tăng mô hình dữ liệu. Điều quan trọng là phải tránh sự tương tác
đưa dữ liệu không đáng tin cậy vào mô hình dữ liệu (hãy nhớ lại câu ngạn ngữ cũ, “rác vào, rác ra”). 
Hãy nhớ rằng việc loại trừ dữ liệu khỏi cơ sở dữ liệu phân tích không giống như xóa dữ liệu 
dữ liệu. Dữ liệu thô vẫn tồn tại và có thể được tích hợp nếu cần thiết.
Quét các cột để tìm dữ liệu không liên quan và không đáng tin cậy
Các cột không liên quan có thể được xác định chủ yếu bằng cách quét dữ liệu một cách trực quan. Từ điển dữ liệu
nary cũng có thể là một công cụ hữu ích. Ví dụ: bảng Nhân viên chứa thông tin liên quan đến-
các văn phòng. Bạn sẽ sử dụng dữ liệu trong cột này như thế nào để ra quyết định?
Quét dữ liệu cũng có thể xác định liệu một cột có chứa dữ liệu không đáng tin cậy hay không. trong 
Minh họa 5.16 (A), cột Tuổi trong bảng E-Dem trộn các giá trị null, số, ngày, 
và văn bản, điều này sẽ gây khó khăn cho việc tạo ra những hiểu biết đáng tin cậy. Hầu hết các công cụ ETL đều cung cấp 
số liệu thống kê về lỗi, giá trị null, v.v., có thể giúp xác định độ tin cậy của cột.  
( Dữ liệu Xem Cách 5.1 ở cuối chương để tìm hiểu cách sử dụng Power Query để lập cấu hình dữ liệu.) 
Xóa các cột có dữ liệu không liên quan hoặc không đáng tin cậy
Để khắc phục sự cố, hãy xóa các cột có dữ liệu không liên quan và không đáng tin cậy khỏi bản phân tích-
cơ sở dữ liệu ical. Hình minh họa 5.16 (B) cho thấy cách thực hiện điều này bằng Power Query. Chọn một cột, 
chẳng hạn như Tuổi, sau đó chọn Xóa Cột. Đối với tập dữ liệu Beans, cột không liên quan, 
Office và cột không đáng tin cậy, Tuổi, đã bị xóa.
Làm cách nào để

![ILLUSTRATION 5.16](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.16.png)

5-20
CHƯƠNG 5 Phân tích: Chuẩn bị dữ liệu
 Tóm tắt Mẫu 3 
vấn đề
 Dữ liệu không liên quan làm phồng tập dữ liệu. Dữ liệu không đáng tin cậy tăng lên 
nguy cơ đưa ra những quyết định sai lầm. 
Phát hiện (Hồ sơ dữ liệu)
Quét trực quan các cột để tìm dữ liệu không liên quan và không đáng tin cậy. 
Đúng (ETL)
 Xóa các cột có dữ liệu không liên quan hoặc không đáng tin cậy. 
Mẫu chuẩn bị dữ liệu 4: Không chính xác và 
Tên cột mơ hồ
 Tên cột trở thành các biến trong quá trình khám phá và giải thích dữ liệu. Tên của họ là 
quan trọng vì những người khác có thể sử dụng cơ sở dữ liệu phân tích. Về cơ bản, tên cột 
trở thành một phần từ vựng của cơ sở dữ liệu. Hãy nhớ lại rằng đối tác quản lý của Beans muốn thực hiện 
các phân tích cần thiết nhưng gặp khó khăn với việc chuẩn bị dữ liệu. Tên cột đúng, 
trực quan và rõ ràng giúp người khác sử dụng cơ sở dữ liệu và khám phá dữ liệu dễ dàng hơn. 
 Quét các cột để tìm tên không chính xác hoặc mơ hồ
 Quét trực quan nội dung của một cột và định nghĩa từ điển dữ liệu của nó có thể tiết lộ liệu 
tên cột phản ánh chính xác nội dung của nó. Dưới đây là bốn quy tắc đặt tên cột:
 MINH HỌA 5.16 Phát hiện và sửa dữ liệu không đáng tin cậy 
Đóng &
Áp dụng
Tập tin
Trang chủ Chuyển đổi Thêm cột
Công cụ
Trợ giúp
Xem
?
Đóng
Mới
Nguồn
Gần đây
Nguồn
Nhập
dữ liệu
Truy vấn mới
Nguồn dữ liệu
Cài đặt
Nguồn dữ liệu
Quản lý
Thông số
Thông số
Làm mới
Xem trước
Trình chỉnh sửa nâng cao
Quản lý
Thuộc tính
Truy vấn
E-DEM
NHÂN VIÊN
Dữ liệu CL
DỊCH VỤ
Truy vấn [4]
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
John
Diego
Kim
Marcus
Gail
Shiela
Ed
Kayne
Sara
Ivan
Federer
Asare
bụi cây
Đất sét
David
kim cương
kim cương
James
Lý
lenk
ba mươi hai
??
??
34
vô giá trị
45
1998
55
22
CPA
CPA, CMA, CFA
CPA
CPA
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
Đại học Michigan
Đại học bang Grand Valley
Đại học Delaware
MSU
Ừm
Đại học bang Michigan
MSU
Đại học bang Michigan
Đại học bang Michigan
Đại học Michigan
Đầu tiên
ABC
Cuối cùng
ABC
Tuổi
ABC
123
Danh sách chứng nhận
ABC
Đại học
ABC
(B) Xóa cột có dữ liệu không đáng tin cậy 
Tuổi
45
1998
ba mươi hai
55
34
22
??
51
??
2/9/1998
(A) Cột có
Dữ liệu không đáng tin cậy 
Quản lý cột
chọn
Cột
Xóa
Cột
Giảm
Hàng
Đóng &
Áp dụng
Đóng
Mới
Nguồn
Gần đây
Nguồn
Nhập
dữ liệu
Truy vấn mới
Nguồn dữ liệu
Cài đặt
Nguồn dữ liệu
Quản lý
Thông số
Thông số
Làm mới
Xem trước
Trình chỉnh sửa nâng cao
Quản lý
Thuộc tính
Truy vấn
Quản lý 
chọn
Cột
Giảm
Hàng