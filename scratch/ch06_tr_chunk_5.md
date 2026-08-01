6-26  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
MINH HỌA 6.32  Bổ sung 
Các biện pháp cho dòng chảy của KLUB 
Mô hình thông tin
Bảng: Mua hàng
Đo lường
Thuật toán
Tổng số lượng đã mua 
SUM(Số lượng đã mua)
Bảng: Doanh thu
Đo lường
Thuật toán
Tổng Số Lượng Máy In Đã Bán
SUM(Số lượng bán) WHERE Loại = “Máy in”
Phân tích
Trong mô hình thông tin luồng KLUB, thước đo TotalQuantityBought trong bảng Mua hàng 
và thước đo Tổng số lượng bán trong bảng Doanh số tóm tắt các luồng vật chất, trong khi 
Thước đo Tổng chi phí trong bảng Mua hàng và thước đo Tổng doanh thu và Tổng giá vốn hàng bán trong bảng 
Bảng bán hàng tóm tắt các dòng tiền. Thương hiệu, Loại và Danh mục là các thứ nguyên tài nguyên.
Dữ liệu được mô tả bằng mối quan hệ dòng chảy có thể trả lời những câu hỏi nào? Minh họa 6.33 
trình bày một số nội dung có thể được phân tích bằng mô hình thông tin dòng chảy của KLUB.
MINH HỌA 6.33  Trả lời 
Câu hỏi với dòng chảy 
Mối quan hệ
Số lượng bán ra là bao nhiêu
giao dịch mỗi lô (MerchandiseID)?
Tổng chi phí mỗi đợt là bao nhiêu
(ID hàng hóa)?
Tổng doanh thu được tạo ra là bao nhiêu
mỗi lô (MerchandiseID)?
Tổng doanh thu được tạo ra là bao nhiêu
mỗi thương hiệu?
Tổng doanh thu được tạo ra là bao nhiêu
mỗi loại?
Tổng doanh thu được tạo ra là bao nhiêu
mỗi danh mục?
Tổng số máy in là bao nhiêu
(loại) đã bán?
Số lượng đơn vị được mua là bao nhiêu
mỗi lô (MerchandiseID)?
Số lượng đơn vị đã bán là bao nhiêu
mỗi lô (MerchandiseID)?
Số lượng mặt hàng đã bán là bao nhiêu
mỗi thương hiệu?
Số lượng mặt hàng đã bán là bao nhiêu
mỗi loại?
Số lượng mặt hàng đã bán là bao nhiêu
mỗi danh mục?
Sự đóng góp tương đối của mỗi
danh mục với tổng doanh thu được tạo ra?
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
Kích thước
Biện pháp
Tiếp theo, sử dụng mô hình thông tin của KLUB để khám phá hai câu hỏi được đặt ra trong phần này 
minh họa. 
• Câu hỏi ➐: Đóng góp tương đối của từng hạng mục (khía cạnh) vào Tổng-
Doanh thu (thước đo)? 
Trong Hình minh họa 6.34, thước đo Tổng Doanh thu trong bảng Doanh số được chia nhỏ thành 
thứ nguyên danh mục trong bảng Hàng hóa. Các lát biểu đồ hình tròn thể hiện tầm quan trọng tương đối
tính chất của từng thể loại. Biểu đồ hình tròn cho thấy KLUB tạo ra phần lớn doanh thu từ 
sản phẩm văn phòng.

![ILLUSTRATION 6.34](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.34.png)

6.3  Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán?  6-27
MINH HỌA 6.34  Tương đối 
Đóng góp của danh mục vào tổng số 
Doanh thu
văn phòng
431.308 (69,39%)
Điện tử
58.025 (9,33%)
Vườn
132.300 (21,28%)
Đóng góp vào tổng doanh thu
Bây giờ, hãy khám phá một câu hỏi khác. 
• Câu hỏi ⓭: Tổng số (số đo) của máy in (loại, là kích thước) là bao nhiêu? 
đã bán?
Hình minh họa 6.35 cho thấy tổng số lượng máy in đã bán và chia nhỏ con số đó 
theo thương hiệu bằng cách sử dụng biểu đồ cột. 
MINH HỌA 6.35  Tổng cộng 
Số lượng máy in đã bán
100
80
60
40
HP
99
74
Thương hiệu
Tổng số lượng
Máy in đã bán
Tổng số máy in đã bán
EPSON
20
0
Tổng số lượng
số máy in đã bán
Tổng số lượng
số máy in đã bán
173
Mẫu mô hình thông tin 11: Xảy ra | 
Giao dịch-Khi nào
Mối quan hệ xảy ra mô tả thời điểm một giao dịch diễn ra bằng cách kết nối nó với Calen-
bảng dar (Minh họa 6.36).
MINH HỌA 6.36  Xảy ra 
Mối quan hệ
Bảng sự kiện 
Xảy ra
N
1
Bảng kích thước
Khi nào?
Giao dịch
Lịch

![ILLUSTRATION 6.36](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.36.png)

6-28  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
Có hai mối quan hệ xảy ra trong mô hình dữ liệu của KLUB:
• Bán hàng cho Lịch.
• Mua hàng vào Lịch.
Có những mối quan hệ khác xảy ra không xuất hiện trong tập dữ liệu KLUB:
• Biên lai tiền mặt vào Lịch.
• Giải ngân tiền mặt vào Lịch.
Bởi vì thông tin được thu thập bởi các mối quan hệ này là tương tự nhau nên các loại phân tích giống nhau 
áp dụng cho tất cả chúng.
Mô hình thông tin
Theo nguyên tắc mô hình hóa chiều, các biện pháp phải được phát triển để truyền
hành động (chẳng hạn như Bán hàng) và được chia nhỏ theo thứ nguyên là một phần của bảng Lịch:
• Các biện pháp được phát triển trước đó cho các bảng Giao dịch, chẳng hạn như NumberOfSales, có thể 
cũng được sử dụng ở đây.
• Ngoài ngày, bảng Lịch còn chứa một chuỗi đơn vị thời gian làm thứ nguyên cho 
phân tích, bao gồm ngày trong tuần, số tuần, tháng, quý và năm. Bởi vì có 
chỉ có sáu tháng dữ liệu cho KLUB, các kích thước năm không liên quan.
Hình minh họa 6.37 (A) hiển thị mô hình thông tin chung cho các mối quan hệ xảy ra. Bảng điều khiển (B) 
của hình minh họa tương tự áp dụng mẫu này cho mối quan hệ Lịch bán hàng của KLUB. 
NumberOfSales có thể được phân tích theo ngày trong tuần, tháng và quý.
Bảng lịch chứa tất cả các ngày giữa ngày bắt đầu và ngày kết thúc. Phần mềm như 
Power BI giúp dễ dàng tạo bảng Lịch. Khi việc đó hoàn tất, các kích thước đơn vị thời gian như 
tháng, quý và năm có thể được thêm vào và sử dụng để phân tích. Việc tạo các kích thước này thường là 
dễ dàng. Một ví dụ về điều này là hàm năm của Excel, trả về thành phần năm của một ngày.
MINH HỌA 6.37  Thông tin 
Mô hình mẫu cho sự xuất hiện 
Mối quan hệ
Bảng sự kiện
1
Xảy ra
Xảy ra
1
N
N
Bảng kích thước
Khi nào?
Lịch
Ngày
Đơn vị thời gian
Khi nào?
Lịch
Ngày
TuầnNgày
Tháng
quý
bán hàng
Số lượng doanh số bán hàng
Giao dịch
Số lượng giao dịch
(A) Chung
(B) KLUB
Cột
Cột được tính toán
Đo lường
Phân tích
Hình minh họa 6.38 trình bày một số câu hỏi mẫu có thể được phân tích bằng cách sử dụng KLUB 
các mối quan hệ.

![ILLUSTRATION 6.38](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.38.png)

6.3  Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán?  6-29
MINH HỌA 6.38  Trả lời 
Câu hỏi với sự xuất hiện 
Mối quan hệ
Số lượng bán ra như thế nào
so sánh giao dịch giữa các ngày trong tuần?
Số lượng mua như thế nào
so sánh giao dịch giữa các ngày trong tuần?
1
2
Xu hướng về số lượng là gì
giao dịch bán hàng trong sáu tháng đầu tiên
tháng của năm 2023?
Số lượng bán ra như thế nào
giao dịch đầu tiên và
so sánh quý 2?
3
4
Kích thước
Biện pháp
Một lần nữa, chúng ta có thể sử dụng mô hình thông tin để khám phá hai trong số những câu hỏi này. Minh họa 
6.39 khám phá câu hỏi đầu tiên với mô hình thông tin xảy ra của KLUB. 
• Câu hỏi ❶: Làm thế nào để so sánh số lượng giao dịch bán hàng (đo lường) giữa các tuần-
ngày (kích thước)? 
Biểu đồ cột chia nhỏ số lượng giao dịch bán hàng theo ngày trong tuần.
MINH HỌA 6.39  So sánh 
Số lượng giao dịch bán hàng 
Xuyên suốt các ngày trong tuần
200
150
183
180
174
141
132
110
87
100
50
0
Thứ Sáu.
Thứ Hai.
Tuệ.
Thứ Tư.
Ngày trong tuần
Số
bán hàng
So sánh doanh số bán hàng trong tuần
Thu.
Đã ngồi.
Mặt trời.
Hình minh họa 6.40 khám phá một câu hỏi khác.
• Câu hỏi ❸: Xu hướng về số lượng giao dịch bán hàng (thước đo) trong thời gian 
sáu tháng đầu tiên (chiều) của năm 2023? 
Biểu đồ đường phân tích số lượng giao dịch bán hàng theo tháng và giúp xác định 
xu hướng.
MINH HỌA 6.40  Nhận dạng 
Xu hướng về số lượng bán hàng 
Giao dịch qua nhiều tháng
250
200
150
100
tháng Giêng.
88
110
137
140
264
268
Tháng Hai
Tháng ba.
Tháng
Số
bán hàng
Xu hướng bán hàng theo tháng
Tháng Tư.
tháng 5
Tháng Sáu.
50
300

![ILLUSTRATION 6.40](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.40.png)

6-30  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
Mẫu mô hình thông tin 12: Who-What-
Khi lược đồ sao
Trong khi các mẫu 9, 10 và 11 phân tích các khía cạnh ai, cái gì và khi nào của kế toán 
giao dịch, mẫu này tích hợp ba mối quan hệ này (Minh họa 6.41).
MINH HỌA 6.41  Mẫu lược đồ sao Ai-Làm-Khi nào
N
N
tham gia
Xảy ra
tham gia
Dòng chảy
N
N
1
1
1
1
Bảng kích thước
Bảng sự kiện
Bảng kích thước
Ai?
Bên ngoài
đại lý
Giao dịch
Ai?
nội bộ
đại lý
Khi nào?
Lịch
Cái gì?
Tài nguyên
Mô hình dữ liệu của KLUB tích hợp hai phiên bản của mẫu ai-làm-khi nào. Đầu tiên là 
để mua các mặt hàng, tức là mua hàng (Minh họa 6.42). Không có nhân viên 
thông tin để ghi lại việc mua hàng vì chủ sở hữu công ty giám sát việc mua lại
quá trình xử lý.
MINH HỌA 6.42  Mô hình lược đồ sao Who-What-When mua hàng
N
N
tham gia
Xảy ra
Dòng chảy
N
1
1
1
Bảng kích thước
Bảng sự kiện
Bảng kích thước
nhà cung cấp
Mua hàng
Lịch
cái gì
KLUB có
mua?
Khi nào
KLUB có
mua?
Từ ai
KLUB có
mua?
Hàng hóa

![ILLUSTRATION 6.42](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.42.png)

6.3  Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán?  6-31
Thứ hai là để bán các mặt hàng hoặc bán hàng (Minh họa 6.43).
MINH HỌA 6.43  Mẫu lược đồ hình sao Ai làm gì khi nào bán hàng
N
N
tham gia
Xảy ra
tham gia
Dòng chảy
N
N
1
1
1
1
Bảng kích thước
Bảng sự kiện
Bảng kích thước
Khách hàng
bán hàng
Ai
Bán?
nhân viên
Lịch
cái gì
KLUB có
bán?
Khi nào
KLUB có
bán?
Gửi ai
KLUB có
bán?
Hàng hóa
Mô hình thông tin
Hãy nhớ lại rằng mô hình dữ liệu chứa tất cả các trường, trong khi mô hình thông tin cũng chứa
cột culate và các biện pháp được tạo ra cho mục đích phân tích. Các mô hình thông tin có thể 
mở rộng tùy theo nhu cầu cụ thể của doanh nghiệp. Hình minh họa 6.44 là mô hình dữ liệu và thông tin
mô hình kết hợp cho lược đồ sao Bán hàng của KLUB. 
Để tạo mô hình thông tin phong phú hơn cho KLUB, chúng tôi đã thêm một cột được tính toán bổ sung 
được gọi là TargetAmount, cũng như ba thước đo bổ sung là TotalTargetAmount, Sự khác biệt, 
và Tỷ lệ khác biệt so với lược đồ sao Bán hàng: 
• Đối với mỗi đợt, KLUB có mức giá mục tiêu tối thiểu cho mỗi đơn vị được gọi là Giá bán tối thiểu.
• Biện pháp chênh lệch xác định sự khác biệt giữa giá thực tế được tính cho 
khách hàng và mức giá mục tiêu.
• % chênh lệch là kết quả của việc chia giá bán cho giá mục tiêu. Nó biểu thị bằng cái gì 
phần trăm giá mục tiêu tối thiểu bị vượt quá.
Trong số những biện pháp khác, những biện pháp này có thể được sử dụng để phân tích kỹ năng đàm phán của KLUB. 
nhân viên bán hàng. Hình minh họa 6.45 thể hiện công thức tạo cột tính toán mới 
(TargetAmount) và các thước đo (TotalTargetAmount, Chênh lệch và Chênh lệch%).
Cột được tính toán và số đo xác định các thông tin cụ thể:
• Cột TargetAmount xác định số tiền cho một dòng hoá đơn nếu 
giá bán tối thiểu đã được tính cho khách hàng. Thuật toán của nó tuân theo Mẫu 4: 
Tính toán xuyên bảng.
• Thước đo TotalTargetAmount xác định tổng số tiền KLUB sẽ có 
nhận được nếu công ty đã tính giá mục tiêu cho toàn bộ doanh số bán hàng của mình. Thuật toán của nó tuân theo
mức thấp Mẫu 5: Tập hợp một cột.
• Thước đo chênh lệch xác định sự khác biệt giữa tổng doanh thu và tổng 
số tiền mục tiêu. Ký hiệu “-” tượng trưng cho phép trừ. Đây là sự tổng hợp có thể 
cắt lát theo nhiều cách. Thuật toán của nó tuân theo Mẫu 7: Phân cấp đo lường.
• Thước đo % Chênh lệch so sánh doanh thu thực tế với doanh thu mục tiêu theo tỷ lệ
phần trăm. Thuật toán của nó cũng tuân theo Mẫu 7: Phân cấp đo lường.

![ILLUSTRATION 6.45](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.45.png)