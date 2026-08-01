7-22  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
Để hiển thị chuỗi thời gian, hình ảnh trực quan yêu cầu đơn vị thời gian như phút, giờ, ngày hoặc 
tuần và một biến thay đổi theo thời gian. 
Trực quan hóa
Biểu đồ đường là cách hiển thị phổ biến nhất cho chuỗi thời gian, nhưng biểu đồ thanh, biểu đồ cột, 
biểu đồ vùng, biểu đồ thác nước và biểu đồ đường thu nhỏ cũng có thể được sử dụng. Hãy quay trở lại với Honda 
Ví dụ về Motors Bắc Mỹ (HNA). Hình minh họa 7.32 là biểu đồ dạng đường Power BI khám phá 
doanh số bán hàng của HNA thay đổi như thế nào trong giai đoạn 2021–2025. 
Mặc dù dữ liệu không chỉ ra yếu tố khác hoặc các yếu tố khác có thể là gì, nhưng chủ sở hữu lưu ý-
lưu ý rằng những ngôi nhà có nhiều cây cối, nhiều cây cối và góc nhà sẽ mất nhiều thời gian hơn để cắt cỏ. Điều này có nghĩa 
khó khăn hoặc phức tạp đó là một yếu tố khác ảnh hưởng đến thời gian và chi phí và quyết định 
mô hình nên được điều chỉnh để phản ánh điều này.
ÁP DỤNG TƯ duy phản biện 7.3: Đánh giá 
Giả định
Ví dụ về biểu đồ phân tán Buzz Cut cho thấy tư duy phản biện là một phần không thể thiếu của dữ liệu 
thăm dò:
• Các giả định không thực tế có thể dẫn đến những hiểu biết sâu sắc gây ra rủi ro đáng kể. Định giá thấp 
có thể dẫn đến thua lỗ (Rủi ro).
• Những hiểu biết sâu sắc này có thể ảnh hưởng tiêu cực đến tất cả các bên liên quan. Nếu có những yếu tố khác thúc đẩy 
đôi khi, nhân viên có thể bị đánh giá không công bằng và việc định giá thấp có thể có nghĩa là Buzz Cut 
không thể trả nợ cho chủ nợ (Stakeholders).
Mẫu khám phá dữ liệu 7: Chuỗi thời gian
Mối quan hệ dữ liệu chuỗi thời gian xác định giá trị của một biến tại các thời điểm liên tiếp 
(Minh họa 7.31).
MINH HỌA 7.31  Khám phá 
Cấu trúc cho dữ liệu chuỗi thời gian 
Mối quan hệ
danh nghĩa
Biến
Các giá trị này
biến được sử dụng để
so sánh chuỗi thời gian.
số
Biến
Biến
đang được phân tích.
Đơn vị thời gian được sử dụng
để phân tích.
Đơn vị thời gian
Biến

![ILLUSTRATION 7.32](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.32.png)

7.2  Các mối quan hệ dữ liệu được hiển thị như thế nào để khám phá?  7-23
MINH HỌA 7.32  Biểu đồ đường thể hiện những thay đổi về doanh số bán căn hộ của HNA trong giai đoạn 2021–2025
2021
2022
2023
2024
2025
0
1.000.000
2.041.879
2.225.138
2.000.000
3.000.000
Đơn vị đã bán
Thay đổi về số lượng căn đã bán: 2021‒2025
Năm
1.774.263
1.723.765
1.782.692
Nó được tạo trong Power BI bằng cách sử dụng năm làm đơn vị thời gian và tổng doanh số đơn vị làm số 
biến (Minh họa 7.33).
MINH HỌA 7.33  Tạo biểu đồ dạng đường trong Power BI
Trục
Năm
Truyền thuyết
Thêm trường dữ liệu ở đây
Giá trị
Đơn vị đã bán
Biến
đang được phân tích.
Đơn vị thời gian được sử dụng
để phân tích.
Đơn vị thời gian
Biến
số
Biến
Khám phá và hiểu biết sâu sắc
Tìm kiếm các xu hướng, chu kỳ và sự bất thường khi khám phá chuỗi thời gian:
• Xu hướng biểu thị hướng chung (lên hoặc xuống) trong đó một biến di chuyển 
theo thời gian.
• Chu kỳ biểu thị một mô hình thay đổi, có thể thay đổi về độ dài và cường độ theo thời gian. 
Tính thời vụ đề cập đến các chu kỳ trong năm có tính chất cố định.
• Sự bất thường là những biến động không có tính hệ thống, thường là ngắn hạn.
Chuỗi thời gian trong Hình minh họa 7.32 cho thấy xu hướng tăng mạnh về doanh số bán hàng của HNA bắt đầu từ 
từ năm 2023. Kéo và thả có thể khám phá xu hướng này chi tiết hơn bằng cách so sánh 
xu hướng ở Canada và Mỹ. Biểu đồ đường mới này (A) và cách nó được tạo ra (B) được hiển thị trong 
Minh họa 7.34. Biểu đồ này cho thấy một bức tranh rất khác: Doanh số bán hàng ở Mỹ không thay đổi và tốc độ tăng trưởng là 
kết quả của việc tăng doanh số bán hàng ở Canada. Những hiểu biết bổ sung có thể được tạo ra bằng cách so sánh 
xu hướng cho các đơn vị được bán theo mẫu hoặc loại.

![ILLUSTRATION 7.34](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.34.png)

7-24  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
MINH HỌA 7.34  Đơn vị phân tích xu hướng được bán theo quốc gia
0
500.000
646.777
1.127.486
648.999
1.074.766
721.717
1.060.975
1.000.000
1.500.000
Đơn vị
đã bán
Hoa Kỳ Vs. Xu hướng bán hàng của Canada: 2021‒2025 
(A) Phân tích xu hướng:
Đơn vị được bán theo quốc gia
(B) Tạo biểu đồ đường
với nhiều chuỗi thời gian
Năm
2021
2022
2023
2024
2025
870.418
1.171.461
1.053.935
1.171.203
Trục
Năm
Giá trị
Đơn vị đã bán
Biến
đang được phân tích.
Đơn vị thời gian được sử dụng
để phân tích.
Đơn vị thời gian
Biến
số
Biến
danh nghĩa
Biến
Các giá trị này
biến được sử dụng để
so sánh chuỗi thời gian.
Truyền thuyết
Quốc gia
Hoa Kỳ
Canada
Mẫu khám phá dữ liệu 8: Không gian địa lý
Trong mối quan hệ dữ liệu không gian địa lý, các giá trị số được gán cho các vị trí và được mã hóa thông qua 
tô màu hoặc tạo bóng và kích thước của bong bóng trong hình ảnh trực quan (Minh họa 7.35).
Mã hóa
Tô màu
Kích thước
Vị trí để
mà số lượng
biến được áp dụng.
Vị trí
Biến
Định lượng
biến dùng để
mục đích phân tích.
số
Biến
MINH HỌA 7.35  Khám phá 
Cấu trúc dữ liệu không gian địa lý 
Mối quan hệ

![ILLUSTRATION 7.35](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.35.png)

7.2  Các mối quan hệ dữ liệu được hiển thị như thế nào để khám phá?  7-25
Trực quan hóa
Các mối quan hệ không gian địa lý được xác định bằng bản đồ:
• Bản đồ hợp âm sử dụng cường độ màu để thể hiện các giá trị dữ liệu. Trong hình minh họa 7.36, màu sắc 
cường độ khác biệt giữa thuế suất bán hàng trung bình của tiểu bang và địa phương đối với 
tiểu bang Hoa Kỳ. Trong bản đồ này, trạng thái là biến vị trí, thuế suất là biến số và 
mã hóa dựa trên cường độ màu.
• Bản đồ ký hiệu tỷ lệ sử dụng các ký hiệu—thường là bong bóng/vòng tròn—và kích thước của 
biểu tượng đại diện cho giá trị dữ liệu. Biểu tượng càng lớn thì giá trị càng cao. Một doanh nghiệp 
có thể tạo một bản đồ hiển thị tổng doanh thu (biến số) trên mỗi thành phố (vị trí 
biến) cho một trạng thái cụ thể. Bong bóng đại diện cho thành phố càng lớn thì giá trị càng cao 
doanh thu của thành phố đó.
MINH HỌA 7.36  Bản đồ Choropleth về thuế suất 
MA
6,25%
#35
CT
6,35%
#33
RI
7,00%
#24
NJ
6,60%
#30
DE
MD
6,00%
#38
DC
6,00%
(#38)
Hạ xuống
Cao hơn
Thuế suất bán hàng trung bình của tiểu bang và địa phương kết hợp
NH
6
VT
6,24%
#36
Thuế bán hàng ở tiểu bang của bạn cao đến mức nào?
Thuế suất bán hàng trung bình của tiểu bang và địa phương kết hợp, tháng 1 năm 2021
WA
9,23%
#4
MT
ID
6,03%
#37
ND
6,96%
#27
MN
7,46%
#17
TÔI
5,50%
#42
MI
6,00%
#38
WI
5,43%
#43
HOẶC
SD
6,40%
#32
NY
8,52%
#10
WY
5,33%
#44
IA
6,94%
#28
ĐB
6,94%
#29
IL
8,82%
#7
PA
6,34% #34
CA
8,68%
#9
UT
7,19%
#21
NV
8,23%
#13
ôi
7,23%
#20
TRONG
7,00%
#24
CO
7,72%
#16
WV
6,50%
#31
MO
8,25%
#12
KS
8,69%
#8
VA
5,73%
#41
KY
6,00% #38
AZ
8,40%
#11
được rồi
8,95%
#6
NM
7,83%
#15
TN
9,55% #1
NC
6,98% #26
TX
8,19%
#14
AR
9,51%
#3
SC
7,46%
#18
AL
9,22%
#5
GA
7,32%
#19
MS
7,07%
#23
LA
9,52% #2
FL
7,08%
#22
xin chào
4,44%
#45
AK
1,76%
#46
Nguồn: Janelle Cammenga, Thuế suất bán hàng của Tiểu bang và Địa phương, năm 2021, Tổ chức Thuế. Có sẵn tại https://files.taxfoundation.org/ 
20210106094117/Tiểu bang và địa phương-Sales-Tax-Rates-2021.pdf
Khám phá và hiểu biết sâu sắc
Giống như các mối quan hệ dữ liệu khác, việc khám phá các mối quan hệ không gian địa lý phụ thuộc vào việc kéo 
và đánh rơi. Lựa chọn địa điểm được giới hạn ở địa chỉ, thành phố, tiểu bang hoặc tỉnh và quốc gia.
thử và thông tin vị trí phải được định dạng sao cho dịch vụ bản đồ, Google Maps hoặc 
Ví dụ, Bing Maps có thể nhận ra nó.

![ILLUSTRATION 7.36](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.36.png)

7-26  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
Áp dụng nó 7.2
Hình dung từng phần-
Toàn bộ mối quan hệ 
với Excel
Dữ liệu   Kế toán quản trị   Giám đốc điều hành tại Happy Colors cần hiểu tầm quan trọng tương đối
về các loại sản phẩm khác nhau của công ty, sơn chất lượng Thấp, Cao và Cao cấp, xét về mặt 
tổng số đơn vị hoặc số lon đang được sản xuất. Hoàn thành ba bước sau để thực hiện phân tích này:
1. Xác định mối quan hệ dữ liệu nào làm cơ sở cho câu hỏi này.
2. Xác định và tạo hình ảnh trực quan có thể khám phá mối quan hệ dữ liệu.
3. Mô tả những hiểu biết sâu sắc được tạo ra bởi hình ảnh.
GIẢI PHÁP
1. Mối quan hệ từng phần với toàn bộ đang được khám phá.
2. Một số hình ảnh trực quan có thể được sử dụng để khám phá các mối quan hệ từng phần với toàn bộ, bao gồm biểu đồ hình tròn, 
biểu đồ bánh rán, biểu đồ thanh xếp chồng, biểu đồ cột xếp chồng và biểu đồ dạng cây. Hình minh họa 
hiển thị biểu đồ hình tròn (A) và hộp thoại của Excel PivotTable được sử dụng để tạo biểu đồ đó (B).
Mối quan hệ từng phần với toàn bộ với biểu đồ hình tròn
Trường PivotTable
Chọn các trường để thêm vào báo cáo:
Tìm kiếm
Kéo các trường giữa các khu vực bên dưới:
Bộ lọc
Cột
Hàng
Giá trị
∑
Tổng số căn đã bán
sản phẩm
(A)
(B)
ID
Tháng
nhân viên
sản phẩm
SốCác Mặt Hàng Bị Lỗi
Tổng cộng
Chi phí
Thêm bàn...
Loại sản phẩm Chia sẻ
Toàn bộ hoặc
số bị phá vỡ
xuống.
Biến đó
xác định cách
toàn bộ bị phá vỡ
theo từng phần.
Cao
40%
Thấp
51%
Cao cấp
9%
3. Biểu đồ hình tròn cho thấy hơn một nửa sản lượng là dành cho lon thuộc loại sản phẩm Thấp, 
trong khi lon Premium có thị phần tương đối nhỏ - dưới 10%.
Mặt khác, nhiều biến số có thể được sử dụng để khám phá. Một bản đồ 
được tạo cho ví dụ về HNA có thể hiển thị tổng doanh thu được tạo ra trên mỗi đại lý và việc sử dụng 
cường độ màu để mã hóa. Bản đồ đó có thể hiển thị tỷ lệ doanh số bán xe mới so với xe cũ, 
đây là chỉ số hiệu suất chính (KPI) quan trọng đối với các đại lý ô tô và sử dụng quy mô cho 
mục đích mã hóa.

![Apply It 7.2](../TaiLieu/textbookForPractice/Figures/Ch_07/Apply%20It%207.2.png)