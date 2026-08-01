6-20
CHƯƠNG 6 Phân tích: Mô hình hóa thông tin
 MINH HỌA 6.22 Mối quan hệ giữa các kích thước hàng hóa 
Thương hiệu
ID lô
N
1
1
1
N
N
N
N
N
N
Loại
Danh mục
 Các thuật toán trong Hình minh họa 6.23 cho thấy việc thực hiện các biện pháp để trả lời các câu hỏi
Các vấn đề về số lượng giao dịch, đại lý (ai) và tài nguyên (cái gì) rất đơn giản. 
Việc triển khai được thực hiện bằng cách tổng hợp-Đếm một cột. Công thức tương tự 
đã được sử dụng cho thước đo NumberOfCustomers ở phần trước của chương này. 
 MINH HỌA 6.23 Có bao nhiêu biện pháp cho mô hình thông tin của KLUB 
 Bảng: Nhà cung cấp 
Đo lường
Thuật toán
SốNhà Cung Cấp
COUNT(ID nhà cung cấp)
 Bảng: Doanh thu 
Đo lường
Thuật toán
Số lượng doanh số bán hàng
COUNT(InvoiceLineID)
 Bảng: Mua hàng 
Đo lường
Thuật toán
Số Lượng Mua Hàng
ĐẾM(ID lô)
 Bảng: Nhân viên 
Đo lường
Thuật toán
SốNhân Viên
COUNT(ID nhân viên)
 Bảng: Hàng hóa 
Đo lường
Thuật toán
SốĐợt
ĐẾM(ID lô)
 Khi đã sẵn sàng, các bộ lọc có thể được áp dụng cho các biện pháp. Ví dụ: các bảng mô tả các tác nhân 
(ai) thường chứa thông tin vị trí, do đó cũng có thể xác định số lượng 
Khách hàng KLUB sống ở California hoặc bất kỳ địa điểm nào khác. Mặt khác, các bảng 
mô tả tài nguyên (cái gì) thường chứa thông tin về các danh mục có thể được sử dụng làm hồ sơ
ters. Ví dụ: có thể xác định KLUB đã mua bao nhiêu lô điện tử.
 Phân tích
 Thước đo NumberOfCustomers có thể xác định mức độ phân bổ khách hàng tiềm năng 
trên khắp các quốc gia theo tỉnh ở Canada và tiểu bang ở Hoa Kỳ ( Minh họa 6.24 ). Nhấp vào một 
thanh trong biểu đồ cột sẽ lọc các tiểu bang/tỉnh trong bảng, do đó việc quản lý tại KLUB có thể 
chỉ chọn các tỉnh của Canada.

![ILLUSTRATION 6.24](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.24.png)

6.3  Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán?  6-21
MINH HỌA 6.24  Phân tích số lượng khách hàng
BẬT
BC
Kiểm soát chất lượng
AB
CA
TX
NY
FL
SK
IL
21.290
8,641
7.664
7.445
5.286
3,837
2.938
2.606
2.440
2,389
PA
MI
ôi
NJ
MA
GA
NC
VA
MO
2.127
1.979
1.880
1.474
1,472
1.380
1.375
1.172
1.098
WA
WI
TRONG
MN
MD
1.068
1.064
1.034
1.031
1,013
Số Lượng Khách Hàng
tiểu bang
50.151
49.849
Hoa Kỳ
Quốc gia
Số lượng
Khách hàng
Số lượng khách hàng
theo vị trí
CA
0
10.000
20.000
30.000
40.000
50.000
60.000
Mẫu mô hình thông tin 9: Tham gia | 
Giao dịch-Ai
Mối quan hệ tham gia mô tả ai tham gia vào một giao dịch (Minh họa 6.25).
MINH HỌA 6.25  Mối quan hệ tham gia
N
tham gia
tham gia
N
1
1
Bảng kích thước 
Bảng sự kiện
Đến/Từ
Ai?
Bên ngoài
đại lý
Giao dịch
Ai?
nội bộ
đại lý
Trong mô hình dữ liệu của KLUB có ba mối quan hệ tham gia:
• Từ bán hàng đến khách hàng (khách hàng là đại lý bên ngoài).
• Từ Bán hàng đến Nhân viên (nhân viên là đại lý nội bộ).
• Từ mua hàng đến nhà cung cấp (nhà cung cấp là đại lý bên ngoài).

![ILLUSTRATION 6.25](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.25.png)

6-22  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
Ngoài ra còn có các loại mối quan hệ tham gia khác không xuất hiện trong tập dữ liệu KLUB:
• Biên lai tiền mặt cho khách hàng.
• Biên lai tiền mặt cho nhân viên.
• Giải ngân tiền mặt cho nhà cung cấp.
• Giải ngân tiền mặt cho nhân viên.
Bởi vì thông tin được thu thập bởi các mối quan hệ này là tương tự nhau nên các loại phân tích giống nhau 
áp dụng cho tất cả chúng.
Mô hình thông tin
Theo nguyên tắc mô hình hóa chiều, các biện pháp phải được phát triển để bán hàng 
giao dịch và được chia nhỏ theo thứ nguyên tác nhân, chẳng hạn như bảng khách hàng:
• Các biện pháp liên quan nào có thể được thực hiện đối với các giao dịch mà đại lý có thể chia nhỏ? Ảo tưởng-
minh họa 6.26 (A) cho thấy số lượng giao dịch là thước đo chính cho sự tham gia
mô hình thông tin mối quan hệ pates. Ví dụ: có bao nhiêu chuyến bay (giao dịch) 
một hãng hàng không lấy khách hàng (đại lý)?
• Những kích thước nào có thể được xác định cho các đại lý? Phân tích có thể được thực hiện cho từng cá nhân 
khách hàng, nhưng thông thường khách hàng được nhóm theo nhiều cách khác nhau cho mục đích phân tích, 
bao gồm theo vị trí, nhóm thành viên hoặc danh mục hiệu suất.
MINH HỌA 6.26  Mẫu mô hình thông tin cho mối quan hệ tham gia
Bảng sự kiện
1
tham gia
tham gia
1
N
N
Bảng kích thước
Ai?
đại lý
Kích thước đại lý
Kích thước tác nhân được tính toán
Giao dịch
Số lượng giao dịch
bán hàng
Số lượng doanh số bán hàng
Ai?
Khách hàng
Tên
tiểu bang
Quốc gia
TuổiThể loại
(A) Chung
(B) KLUB
Cột
Cột được tính toán
Đo lường
Để triển khai mô hình thông tin người tham gia, tạo ra các biện pháp và tính toán phù hợp
các cột được sắp xếp trong bảng Giao dịch (thực tế) và Tác nhân (thứ nguyên). Các biện pháp thực tế 
và các trường được tính toán sẽ tùy thuộc vào nhu cầu cụ thể của doanh nghiệp. Áp dụng minh họa 6.26 (B) 
mô hình tham gia vào mối quan hệ Bán hàng-Khách hàng của KLUB. Tính toán bổ sung

![ILLUSTRATION 6.26](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.26.png)

6.3  Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán?  6-23
các cột và thước đo tạo ra mô hình thông tin phong phú hơn và do đó phân tích phong phú hơn. các 
các thuật toán để triển khai thước đo NumberOfSales và trường được tính toán AgeCategory 
trong Hình minh họa 6.26 đã được thảo luận trước đó trong chương này.
Phân tích
KLUB có thể sử dụng mối quan hệ tham gia để trả lời một số câu hỏi bằng phân tích dữ liệu 
(Minh họa 6.27).
MINH HỌA 6.27  Trả lời 
Câu hỏi với người tham gia 
Mối quan hệ
Số lượng bán ra là bao nhiêu
giao dịch trên mỗi khách hàng (tên)?
1
Khách hàng (tên) là ai với
số lượng giao dịch bán hàng cao nhất?
2
Số lượng bán ra là bao nhiêu
giao dịch trên mỗi tiểu bang (khách hàng)?
3
Số lượng bán ra là bao nhiêu
giao dịch ở mỗi quốc gia (khách hàng)?
4
Số lượng bán ra là bao nhiêu
giao dịch theo từng nhóm tuổi?
5
Số lượng bán hàng của mỗi nhân viên là bao nhiêu
(tên)?
6
Nhân viên (tên) của công ty là ai?
số lượng giao dịch bán hàng cao nhất?
7
Khách hàng (tên) với ai
một số giao dịch ít nhất là hai?
8
Kích thước
Biện pháp
Tiếp theo, hãy sử dụng mô hình thông tin của KLUB để khám phá thêm hai câu hỏi được đặt ra 
trong hình minh họa 6.27.
• Câu hỏi ❷: Ai là khách hàng (tên, là một chiều) có mức độ hài lòng cao nhất? 
số lượng giao dịch bán hàng (đo lường)? 
Trong Hình minh họa 6.28 số lượng giao dịch bán hàng được chia theo tên khách hàng, 
và top 5 được hiển thị theo thứ tự giảm dần.
MINH HỌA 6.28  Số lượng giao dịch bán hàng trên mỗi khách hàng: Top 5
14
14
13
13
13
11
12
10
8
6
4
2
0
Funk, Viola
Alfonso, Henry
Reynold, Steven
5 khách hàng hàng đầu
5 khách hàng hàng đầu
Số
bán hàng
Rippy, Kevin
Morris, Bonnie

![ILLUSTRATION 6.28](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.28.png)

6-24  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
• Câu hỏi ❽: Khách hàng thường xuyên là ai? Nghĩa là, khách hàng là ai (tên, đó là 
một thứ nguyên) với số lượng giao dịch (số đo) ít nhất là hai? 
Hình minh họa 6.29 là một phần danh sách các khách hàng đã mua ít nhất hai lần từ KLUB.
MINH HỌA 6.29  Danh sách 
Khách hàng lặp lại
Funk, Viola
Alfonso, Henry
Reynold, Steven
Rippy, Kevin
Morris, Bonnie
Moore, Steven
Williams, Mary
Zebrowski, Connie
Garza, Jeffrey
Uren, Harold
Barnhart, Richard
Edens, Blaine
Jenkins, Toni
Phường, Jenny
Youngce, Stacey
14
13
13
13
11
9
9
9
8
8
7
7
7
7
7
Tên
Số lượng doanh số bán hàng
Mẫu mô hình thông tin 10: Dòng chảy | 
Giao dịch-Cái gì
Mối quan hệ dòng chảy mô tả những gì liên quan đến một giao dịch, chẳng hạn như hàng hóa và dịch vụ 
(Minh họa 6.30). Một giao dịch dẫn đến tăng hoặc giảm tài nguyên.
MINH HỌA 6.30  Dòng chảy 
Mối quan hệ
Bảng sự kiện
Dòng chảy
N
1
Bảng kích thước
Cái gì?
Tài nguyên
Giao dịch
Trong mô hình dữ liệu của KLUB có hai mối quan hệ luồng:
• Từ bán hàng đến hàng hóa.
• Từ mua hàng đến hàng hóa.
Ngoài ra còn có các loại mối quan hệ luồng khác không xuất hiện trong tập dữ liệu KLUB:
• Biên lai tiền mặt thành tiền mặt.
• Giải ngân tiền mặt thành tiền mặt.
Bởi vì thông tin được thu thập bởi các mối quan hệ này là tương tự nhau nên các loại phân tích giống nhau 
áp dụng cho tất cả chúng.
Mô hình thông tin
Bước đầu tiên là phát triển các thước đo cho các giao dịch, chẳng hạn như bán hàng, có thể bị phá vỡ. 
xuống theo các thứ nguyên là một phần của bảng Tài nguyên, chẳng hạn như hàng hóa. Đối với dòng chảy liên quan-
quan trọng, hãy xem xét các biện pháp tóm tắt các dòng vật chất và tiền tệ:
• Các dòng vật lý mô tả có bao nhiêu. Có bao nhiêu đơn vị đã được mua? Có bao nhiêu đơn vị 
đã được bán?
• Dòng tiền mô tả bao nhiêu? Giá trị của các đơn vị được bán là bao nhiêu và bằng cách nào 
chúng đã được bán được bao nhiêu?

![ILLUSTRATION 6.30](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.30.png)

6.3  Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán?  6-25
Ngoài ra, chúng ta có thể sử dụng số lượng giao dịch và số lượng tài nguyên đo lường được
chửi bới trước đó.
Hình minh họa 6.31 (A) hiển thị mô hình thông tin chung cho các mối quan hệ dòng chảy. bảng điều khiển 
(B) trong cùng một hình minh họa áp dụng mẫu này cho mối quan hệ luồng Bán-Hàng hóa của KLUB-
vận chuyển, dẫn đến bốn thước đo: NumberOfSales, TotalCOGS, TotalQuantitySold và 
Tổng doanh thu.
MINH HỌA 6.31  Mẫu mô hình thông tin cho mối quan hệ dòng chảy
Bảng sự kiện
1
Dòng chảy
Dòng chảy
1
N
N
Bảng kích thước
Cái gì?
Tài nguyên
Kích thước tài nguyên
Kích thước tài nguyên được tính toán
Cái gì?
ID hàng hóa
Thương hiệu
Loại
Danh mục
(A) Chung
(B) KLUB
Cột
Cột được tính toán
Đo lường
Hàng hóa
Số lượng doanh số bán hàng
Tổng COGS
Tổng số lượng đã bán
Tổngdoanh thu
bán hàng
Số lượng giao dịch
Tổng số lượng (Dòng chảy vật lý)
TotalDollarAmount(Tiền tệ)
Giao dịch
Việc thực hiện mô hình thông tin luồng liên quan đến việc tạo ra các biện pháp trong Giao dịch
bảng tion và tạo thứ nguyên Tài nguyên thông qua các thuật toán. Tất cả các kích thước trong Illustra-
điều 6.31 đã được đưa ra; nghĩa là, các tính toán bổ sung là không cần thiết. Làm thế nào để thực hiện các 
Các biện pháp NumberOfSales, TotalQuantitySold và TotalRevenue đã được thảo luận trước đó. Tổng-
COGS, thước đo trong bảng Doanh số, là tập hợp một cột tính tổng tất cả các giá trị trong 
cột COGS–SUM(COGS).
Có hai biện pháp bổ sung liên quan đến dòng chảy cần được thêm vào thông tin 
mô hình (Minh họa 6.32). Thước đo TotalQuantityBought sử dụng tổng hợp một cột
mẫu gation để xác định tổng số đơn vị được KLUB mua và nó được thêm vào Mua hàng 
cái bàn. Biện pháp TotalQuantityOfPrintersSold sử dụng mẫu tổng hợp được lọc để phát hiện
khai thác tổng số lượng máy in đã bán.

![ILLUSTRATION 6.32](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.32.png)