5-34  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Các mẫu chuyển đổi ở cấp mô hình tìm kiếm các vấn đề về dữ liệu trên các bảng, chẳng hạn như dữ liệu 
mô tả cùng một thực thể trải rộng trên nhiều bảng, mô hình dữ liệu có cấu trúc 
khó hiểu và các mô hình dữ liệu không hỗ trợ xử lý hiệu quả.
Mẫu chuẩn bị dữ liệu 15: Truyền bá dữ liệu  
Trên các bàn
Việc phân tích trở nên khó khăn hơn khi dữ liệu mô tả cùng một thực thể được trải rộng trên 
nhiều bảng. Hình minh họa 5.32 cho thấy hai tình huống có thể xảy ra.
	 1. Trong bảng (A) cả hai bảng, JanuarySales và FebSales, có cùng cấu trúc nhưng 
các hàng khác nhau. Đó là bảng bán hàng được hiển thị trong bảng (C) được chia theo chiều ngang. Câu hỏi về 
tổng số tiền bán hàng sẽ dễ trả lời hơn nếu tất cả dữ liệu nằm trong một bảng.
	 2. Trong bảng (B), hai bảng mô tả các đặc điểm khác nhau của cùng một thực thể–Sản phẩm. 
Một số thông tin về sản phẩm có ID 1 có trong bảng ProductDescriptions. Khác 
thông tin cho cùng một sản phẩm, ID = 1, nằm trong bảng ProductAccounting. Trong trường hợp này, 
đó là bảng sản phẩm được hiển thị trong bảng (D) được chia theo chiều dọc.
MINH HỌA 5.32  Kết hợp các bảng
189
190
191
Số
Ngày
Tháng GiêngBán Hàng
(A) Dữ liệu bán hàng hàng tháng
Trên các bàn
(C) Liên minh dữ liệu bán hàng hàng tháng
(D) Hợp nhất thông tin sản phẩm
(B) Thông tin sản phẩm
Trên các bàn
10/1/2025
15/1/2025
24/1/2025
$17,450
$ 23,890
19.001 USD
Số tiền
192
193
194
Ngày
Tháng haiBán hàng
9/2/2025
10/2/2025
14/2/2025
$ 25,451
$34,881
$7,282
195
23/2/2025
$13,209
Số tiền
189
190
191
Ngày
bán hàng
10/1/2025
15/1/2025
24/1/2025
$17,450
$ 23,890
19.001 USD
Số tiền
192
193
194
9/2/2025
10/2/2025
14/2/2025
$ 25,451
$34,881
$7,282
195
23/2/2025
$13,209
1
2
3
ID
Loại
Mô tả sản phẩm
Thú nhồi bông
Đài phát thanh
Quả bóng đá
Đồ chơi
Điện tử
Đồ chơi
Danh mục
1
2
3
ID
QOH 
Sản phẩmKế toán
84
133
354
1
2
3
ID
Loại
sản phẩm
Thú nhồi bông
Đài phát thanh
Quả bóng đá
Đồ chơi
điện tử
Đồ chơi
Danh mục
QOH 
84
133
354
Số
Số
5.6  Mô hình nào biến đổi mô hình?
MỤC TIÊU HỌC TẬP ❻
Áp dụng các mẫu để chuyển đổi mô hình.

![ILLUSTRATION 5.32](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.32.png)

5.6  Mô hình nào biến đổi mô hình?  5-35
Xác định các bảng/bảng có cấu trúc tương tự mô tả sự khác nhau 
Đặc điểm của cùng một thực thể
Để xác định các bảng có cấu trúc tương tự, hãy tìm hai hoặc nhiều bảng có cùng cấu trúc. 
Các bảng này sẽ có cùng cột và dữ liệu tương tự. Một lựa chọn khác là tìm kiếm 
cho các bảng mô tả các đặc điểm khác nhau của cùng một thực thể. Trong trường hợp Đậu, Nhân viên 
và Nhân khẩu học nhân viên là những bảng như vậy. Mục đích là tạo ra một bảng duy nhất với tất cả các 
thông tin nhân viên.
Kết hợp các bảng
Hãy nhớ lại ở chương trước rằng việc kết hợp hai bảng có cấu trúc tương tự nhau được gọi là 
công đoàn. Trong Hình minh họa 5.32, bảng trong bảng (C) kết hợp hai bảng trong bảng (A). Kết hợp-
Việc kết hợp hai bảng có các đặc điểm khác nhau cho cùng một thực thể là sự hợp nhất hoặc sự kết hợp. cái bàn 
trong bảng (D) kết hợp hai bảng trong bảng (B). Đối với trường hợp Beans, cả Nhân viên và 
Các bảng Nhân khẩu học chứa thông tin nhân viên, vì vậy chúng phải được hợp nhất thành 
một bảng ( Dữ liệu Xem Cách thực hiện 5.2 để tìm hiểu cách hợp nhất các bảng này với Power Query.).
Hình minh họa 5.33 cho thấy cấu trúc của bảng kết hợp được đặt tên là Nhân viên.
Làm thế nào để
nhân viên
ID nhân viên
Tên đầu tiên
Họ
Chức danh công việc
tỷ lệ
Danh sách chứng nhận
Tình trạng hôn nhân
Đại học
MINH HỌA 5.33  
Bảng nhân viên kết hợp
Tóm tắt Mẫu 15
vấn đề
Dữ liệu của một thực thể được trải rộng trên nhiều bảng, 
làm phức tạp việc phân tích.
Phát hiện (Hồ sơ dữ liệu)
Xác định các bảng có cấu trúc tương tự hoặc các bảng mô tả 
những đặc điểm khác nhau của cùng một thực thể.
Đúng (ETL)
Liên kết hoặc hợp nhất các bảng.
Mẫu chuẩn bị dữ liệu 16: Mô hình dữ liệu không 
Tuân thủ các nguyên tắc của mô hình thứ nguyên
Mô hình hóa thứ nguyên là kỹ thuật tạo mô hình dữ liệu với các bảng dữ kiện được bao quanh bởi 
các bảng chiều. Các mô hình dữ liệu này, chẳng hạn như lược đồ hình sao, rất dễ hiểu và mang lại kết quả 
trong việc xử lý dữ liệu hiệu quả. 
Phân tích sự tuân thủ của mô hình dữ liệu với thứ nguyên 
Nguyên tắc làm mẫu
Sử dụng các nguyên tắc mô hình hóa thứ nguyên này bằng cách xác định các bảng thực tế và thứ nguyên 
và đảm bảo tất cả các trường thuộc về bảng chính xác. Trong bối cảnh kế toán, các bảng dữ kiện 
tương ứng với các giao dịch kinh doanh. Mặt khác, bảng kích thước mô tả ai 
tham gia vào các giao dịch, thời điểm giao dịch xảy ra và những gì đã được từ bỏ hoặc 
có được. (Chương về mô hình hóa thông tin thảo luận về ai, cái gì và khi nào phân tích 
giao dịch kế toán chi tiết hơn.)

![ILLUSTRATION 5.33](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.33.png)

5-36  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Hình minh họa 5.34 cấu trúc cơ sở dữ liệu phân tích hiện tại dưới dạng lược đồ sao. các 
Bảng dịch vụ là bảng thực tế, bảng Nhân viên là thứ nguyên ai và bảng Khách hàng là 
cũng là một chiều hướng ai.
MINH HỌA 5.34  Lược đồ hình sao đậu hiện tại
Ai?
Giao dịch
?
nhân viên
ID nhân viên
Tên đầu tiên
Họ
Chức danh công việc
tỷ lệ
Tình trạng hôn nhân
Danh sách chứng nhận
Đại học 
khách hàng
ID khách hàng
Tên
Tên ngành
Dịch vụ
N
N
1
1
ID dịch vụ
Ngày
Thời gian thực tế
Thời gian dự toán
Tên nhiệm vụ
ID tác vụ
Khu vực
Bảng kích thước
Bảng sự kiện
Bảng kích thước
Chìa khóa
Cột
Khóa ngoại
Ai?
Cái gì?
nhân viên
khách hàng
Lưu ý rằng thời điểm và kích thước nào dường như bị thiếu. Chỉ có trường Ngày trong 
bảng Dịch vụ và chúng tôi đã chọn không chỉ định thứ nguyên khi riêng biệt. Tuy nhiên, TaskId, 
Tên nhiệm vụ và Khu vực đều là những mô tả– Beans bán gì cho khách hàng của họ? Đó-
trước hết, một bảng thứ nguyên mới có tên Nhiệm vụ có thể được tạo. Hơn nữa, hãy nhớ lại từ Mẫu 6 rằng 
cột Danh sách chứng nhận trong bảng Nhân viên là cột có nhiều giá trị. Tạo một cái mới 
table biến nó thành một cột có giá trị đơn. Hình minh họa 5.35 cho thấy mô hình dữ liệu chúng ta 
muốn tạo ra.
Tạo một bảng riêng cho Chứng chỉ sẽ tạo ra một lược đồ bông tuyết. Trong tuyết-
lược đồ dạng vảy, thông tin về một thứ nguyên sẽ được trải rộng trên nhiều bảng. Lược đồ 
trong Minh họa 5.35 có thể được tạo bằng cách sử dụng Power Query làm công cụ ETL.

![ILLUSTRATION 5.35](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.35.png)

5.6  Mô hình nào biến đổi mô hình?  5-37
Cấu hình lại mô hình dữ liệu dưới dạng lược đồ hình sao/bông tuyết
Đầu tiên, tạo bảng Thứ nguyên nhiệm vụ để ghi lại các mô tả cho dịch vụ. 
Bước 1: 
Nhân đôi bảng Dịch vụ và đổi tên bản sao là “Task” (Minh họa 5.36). 
Đối với cả bảng Dịch vụ và Nhiệm vụ, chỉ giữ lại các cột được hiển thị trong Hình minh họa 5.35.
MINH HỌA 5.36  Bảng dịch vụ trùng lặp
ID dịch vụ
123
khách hàng
Nhân khẩu học của nhân viên...
nhân viên
Dịch vụ
Đóng
Nguồn dữ liệu
Cài đặt
Đóng &
Áp dụng
Nhập
dữ liệu
Mới
Nguồn
Gần đây
Nguồn
Nguồn dữ liệu
Quản lý
Thông số
Thông số
Truy vấn mới
Truy vấn [4]
1
2
3
4
Sao chép
Dán
Xóa
Đổi tên
Kích hoạt tải
Đưa vào làm mới báo cáo
Tài liệu tham khảo
trùng lặp
MINH HỌA 5.35  Lược đồ hình sao/bông tuyết lý tưởng của Beans
Giao dịch
Ai?
Ai?
Ai?
Cái gì?
N
N
1
1
N
1
N
1
Chứng chỉ
ID nhân viên
Chứng nhận
nhân viên
ID nhân viên
Tên đầu tiên
Họ
Chức danh công việc
tỷ lệ
Tình trạng hôn nhân
Đại học
khách hàng
ID khách hàng
Tên
Tên ngành
Nhiệm vụ
ID tác vụ
Khu vực
Tên nhiệm vụ
Dịch vụ
khách hàng
nhân viên
Nhiệm vụ
Ngày
Thời gian thực tế
Thời gian dự toán
ID dịch vụ
Bảng kích thước
Bảng sự kiện
Bảng kích thước
Chìa khóa
Cột
Khóa ngoại

![ILLUSTRATION 5.36](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.36.png)

5-38  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
MINH HỌA 5.37  Bảng kích thước nhiệm vụ
ID tác vụ
1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8
Kế toán
Kế toán
Kế toán
Kế toán
Thuế
Thuế
Thuế
Thuế
chuẩn bị
Xem lại
Quản trị viên
Khác
chuẩn bị
Xem lại
Quản trị viên
Khác
123
Tên nhiệm vụ
Khu vực
ABC
ABC
Đảm bảo giữ lại trường TaskID trong bảng Dịch vụ và đổi tên thành “Nhiệm vụ”. Dịch vụ 
bảng bây giờ đã được chia thành hai bảng. Dịch vụ là một bảng sự kiện và Nhiệm vụ là một bảng thứ nguyên. 
Bước 2: 
Xóa các hàng trùng lặp trong bảng Tác vụ bằng cách chọn tab Trang chủ trong Power 
Menu chính của truy vấn. Chọn Xóa hàng, sau đó chọn Xóa hàng trùng lặp. 
Bảng Nhiệm vụ bây giờ sẽ phản ánh bảng được hiển thị trong Hình minh họa 5.37. 
Thứ hai, giải quyết vấn đề về Danh sách chứng nhận, là một cột có nhiều giá trị trong 
Bảng nhân viên: 
Bước 1: 
Sử dụng quy trình tương tự như trước để tạo bảng CertificationList:
• Nhân đôi bảng Nhân viên và đặt tên cho bản sao là “Chứng chỉ”. 
• Loại bỏ cột CertificationList khỏi bảng Nhân viên. 
• Trong bảng Chứng chỉ mới, chỉ giữ lại ID nhân viên và Danh sách chứng chỉ 
cột. 
Bước 2: 
Chuyển đổi Danh sách chứng nhận từ cột nhiều giá trị thành cột có giá trị đơn 
cột: 
• Trong Power Query, tách cột Danh sách chứng nhận và chọn Mỗi lần xuất hiện của 
tùy chọn phân cách. 
• Bấm vào cột ID nhân viên và chọn Chuyển đổi trong menu chính.
• Cuối cùng, chọn Hủy xoay các cột trong dải băng và chọn Hủy xoay các cột khác 
(Minh họa 5.38). 
Bước 3: 
Trong bảng kết quả, hãy xóa cột Thuộc tính và thay đổi cột Giá trị 
đặt tên cho “Chứng chỉ”. Các chứng chỉ của nhân viên hiện được ghi lại dưới dạng một giá trị 
cột.
Điều này hoàn tất việc chuyển đổi tập dữ liệu của Bean thành lược đồ hình sao/bông tuyết.

![ILLUSTRATION 5.38](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.38.png)

5.6 Những mẫu nào biến đổi mô hình? 5-39
 Tóm tắt Mẫu 16 
 vấn đề 
 Các mô hình dữ liệu không có cấu trúc theo 
nguyên tắc của mô hình chiều thường 
khó phân tích hơn. 
 Phát hiện (Hồ sơ dữ liệu) 
 Phân tích sự tuân thủ của mô hình dữ liệu với 
nguyên tắc mô hình hóa chiều. 
 Đúng (ETL) 
 Cấu hình lại mô hình dữ liệu dưới dạng ngôi sao/bông tuyết 
lược đồ. 
Mẫu khám phá dữ liệu 17: Tìm giá trị không hợp lệ 
với Luật liên bàn
 Các mẫu 10, 14 và 17 tương tự nhau vì chúng xác định các giá trị được chấp nhận cho một cột. 
Tuy nhiên, Mẫu 17 xác định tính hợp lệ của các giá trị của cột dựa trên các giá trị trong một 
hoặc nhiều bảng khác. Một ví dụ về quy tắc xác thực giữa các bảng được sử dụng rộng rãi là quy tắc tham chiếu 
tính toàn vẹn, đề cập đến thực tế là tất cả các giá trị trong khóa ngoại cũng phải tồn tại dưới dạng giá trị trong 
khóa chính tương ứng. ( Data How To 5.3 ở cuối chương giải thích cách 
triển khai tính toàn vẹn tham chiếu với Microsoft Access.) 
 Tạo và áp dụng quy tắc xác thực giữa các bảng
 Quy tắc xác thực giữa các bảng xác định dữ liệu không hợp lệ. Sự sáng tạo của họ đòi hỏi kiến thức chuyên sâu 
của doanh nghiệp.  Hình minh họa 5.39 cho thấy một ví dụ về áp dụng quy tắc xác thực giữa các bảng
đến vụ Beans. Nó là một phần của bảng Dịch vụ và nó chỉ định rằng chỉ những người quản lý, sr. người đàn ông-
người lớn tuổi và các đối tác có thể xem xét sự tham gia. Quy tắc đã phát hiện ra rằng dịch vụ 3971 là 
được đánh giá bởi một cấp cao và một nhân viên đã đánh giá dịch vụ 4193. 
Làm thế nào để
 MINH HỌA 5.39 Thiết kế và triển khai quy tắc xác thực giữa các bảng 
 Mô tả 
 Mã mẫu 
 Chỉ có người quản lý, sr. người quản lý, 
và các đối tác có thể xem xét một 
sự đính hôn. 
KHÔNG QUYỀN = 
 IF TASK.TASKNAME = “ĐÁNH GIÁ” VÀ 
  NHÂN VIÊN[JOBTITLE] TRONG {“MANAGER”, “SR. MANAGER”, “PARTNER”}, 
 SAU ĐÓ "Được", 
 KHÁC “Vấn đề”
MINH HỌA 5.38 Cột không xoay
Tập tin
Trang chủ
chuyển đổi
Thêm cột
Xem
Công cụ
Trợ giúp
Bảng
Nhóm
Bởi
Sử dụng hàng đầu tiên
làm Tiêu đề
1
2
Chuyển đổi
Hàng đảo ngược
Đếm hàng
Cột bất kỳ
Loại dữ liệu: Số nguyên
Phát hiện loại ngày
Đổi tên
?
1 2Thay thế giá trị
Điền vào
Cột xoay
Truy vấn [6]
Nhiệm vụ
Nhân khẩu học nhân viên
nhân viên
Dịch vụ
khách hàng
Chứng chỉ
ID nhân viên
123
Danh sách chứng nhận.1
ABC
Danh sách chứng nhận.2
ABC
Danh sách chứng nhận.3
ABC
Danh sách chứng nhận.4
ABC
1
2
3
4
5
6
7
CPA
1
2
3
4
5
6
7
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
CMA
CMA
CFA
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
vô giá trị
CPA
CPA
CPA
điều hòa không khí
Bỏ xoay cột
abc
ABC
123
Bỏ xoay cột
Bỏ xoay cột
Bỏ xoay các cột khác
Chỉ hủy xoay các cột đã chọn
Hợp nhất các cột
Phân tích cú pháp
Trích xuất
Bảng
Nhóm
Bởi
Sử dụng hàng đầu tiên
làm Tiêu đề
1
2
Chuyển đổi
Hàng đảo ngược
Đếm hàng
Cột bất kỳ
Loại dữ liệu: Số nguyên
Phát hiện loại ngày
Đổi tên
?
1 2Thay thế giá trị
Điền vào
Cột xoay
abc
ABC
123
ot cột
Hợp nhất các cột
Phân tích cú pháp
Trích xuất

![ILLUSTRATION 5.39](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.39.png)