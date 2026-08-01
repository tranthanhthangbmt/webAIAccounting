6-32  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
MINH HỌA 6.45  Bổ sung 
Cột và số đo được tính toán 
dành cho Bán hàng Ai-Cái gì-Khi nào  
Lược đồ sao
Bảng: Doanh thu
Cột được tính toán
Thuật toán
Số lượng mục tiêu
Doanh số.Số lượng bán × Hàng hóa.Giá bán tối thiểu
Bảng: Doanh thu
Biện pháp
Thuật toán
Tổng số tiền mục tiêu
SUM(Số lượng mục tiêu)
Sự khác biệt
[Tổng doanh thu] − [TotalTargetAmount]
% chênh lệch
[Tổng doanh thu] / [Tổng số mục tiêu]
Phân tích
Lược đồ hình sao ai-làm-khi nào là một cấu trúc mạnh mẽ để phân tích dữ liệu kế toán. bất kỳ 
thước đo giao dịch trong bảng dữ kiện có thể được chia nhỏ theo bất kỳ sự kết hợp nào của các chiều (ai, 
cái gì và/hoặc khi nào), và những phân tích này có thể được định hình thông qua nhiều hình ảnh trực quan khác nhau.
MINH HỌA 6.44  Mô hình dữ liệu và thông tin cho Lược đồ ngôi sao bán hàng Ai làm gì khi nào
Bảng kích thước
Bảng sự kiện
Bảng kích thước
1
1
1
1
N
N
N
N
ID dòng hóa đơn
Khách hàng
Ngày
nhân viên
Hàng hóa
bán hàng
BánGiá
Số lượng đã bán
giá vốn
Doanh thu
Số lượng mục tiêu
CanadaHoa KỳTỷ lệdoanh thuTổngGiá vốn
Sự khác biệt
% chênh lệch
Số lượng doanh số bán hàng
Tổng COGS
Tổng số lượng đã bán
Tổngdoanh thu
Tổngdoanh thuTừKhách hàng Canada
Tổngdoanh thuTừUSKhách hàng
Tổng số tiền mục tiêu
bán hàng
ID lô
Thương hiệu
Danh mục
Mã
Hoa hồng
Mô tả
Giá bán tối thiểu
Loại
SốĐợt
Hàng hóa
ID khách hàng
Tuổi
Thành phố
Quốc gia
Tên đầu tiên
Giới tính
Họ
đường phố
tiểu bang
Điện thoại
Tiêu đề
Mã zip
Số Lượng Khách Hàng
Địa chỉ
TuổiThể loại
Khách hàng
ID nhân viên
Email
Tên đầu tiên
Giới tính
Họ
Ssn
SốNhân Viên
nhân viên
Ngày
TuầnNgày
Tháng
quý
Lịch
Chìa khóa
Cột
Cột được tính toán
Đo lường
Khóa ngoại
Mô hình thông tin mới

![ILLUSTRATION 6.45](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.45.png)

6.3  Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán?  6-33
Các mô hình thông tin cho lược đồ sao Bán hàng và Mua hàng đã dần được 
được phát triển trong chương này khi chúng ta tạo ra các thước đo cần thiết và các cột tính toán. A 
Lược đồ hình sao ai-cái gì-khi nào là một cách hiệu quả để thực hiện phân tích vì nó có tính-
chỉ ra những gì cần chia nhỏ (thước đo) và cách chia nhỏ nó, đó là một phần giao nhau.
các kích thước. Lược đồ hình sao có thể được phát triển độc lập với phần mềm 
đã sử dụng. Hình minh họa 6.46 chỉ đưa ra một vài ví dụ về các câu hỏi có thể được phân tích bằng 
lược đồ ngôi sao bán hàng được hiển thị trong Hình minh họa 6.44.
MINH HỌA 6.46  Trả lời 
Câu hỏi với Ngôi sao bán hàng 
Lược đồ
Tổng số lượng bán được mỗi lần là bao nhiêu
thể loại (cái gì) vào cuối tuần
(ngày trong tuần) (khi) sang nữ (giới tính)
khách hàng sống ở Trung Đại Tây Dương
khu vực (tiểu bang) (ai)? 
So sánh tổng doanh thu được tạo ra
theo nhãn hiệu (cái gì), loại tuổi
và giới tính (ai)? 
So sánh % chênh lệch giữa
danh mục sản phẩm (cái gì) ―cái nào
danh mục vượt quá mong đợi về doanh thu
nhất?
1
Xác định % chênh lệch
nhân viên (tên) (ai) ―ai
là nhà đàm phán tốt hơn?
4
2
Xác định % chênh lệch
nhân viên (tên) (ai) trên khắp
danh mục (cái gì) ―ai nên bán cái gì?
5
3
Kích thước
Biện pháp
Tiếp theo, chúng ta khám phá hai trong số những câu hỏi này. 
• Câu hỏi ❶: Tổng số lượng bán ra (đo lường) theo chủng loại là bao nhiêu (kích thước nào) 
vào cuối tuần (ngày trong tuần) (khi chiều) đối với khách hàng nữ (giới tính) sống tại khu vực 
Khu vực giữa Đại Tây Dương (ai kích thước)?
Hình minh họa 6.47 cho thấy lược đồ sao ai-làm-khi nào có thể trả lời câu hỏi này như thế nào.
MINH HỌA 6.47  Lược đồ sao Ai-Làm-Khi nào để Phân tích Số lượng Đã bán
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
nhân viên
Giới tính
tiểu bang
Hàng hóa
Danh mục
Lịch
TuầnNgày
bán hàng
Tổng số lượng đã bán
Cột
Cột được tính toán
Đo lường

![ILLUSTRATION 6.47](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.47.png)

6-34  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
Đây là câu hỏi dạng truy vấn sử dụng bộ lọc, vì vậy bước tiếp theo là tạo thuật toán 
tích hợp các bộ lọc này (Minh họa 6.48).
MINH HỌA 6.48  Thực hiện Số lượng bán vào các ngày trong tuầnChoNữTrung Đại Tây DươngĐo lường khách hàng
Bảng: Doanh thu
Đo lường
Thuật toán
Số lượngBánCác ngày trong tuầnNữTrungAtlanticKhách hàng
SUM(Số lượng đã bán) 
WHERE Calendar.Weekday = 1 hoặc 7, VÀ 
  Khách hàng.Gender = “Nữ”, VÀ 
  Khách hàng.State = “PA” HOẶC “MD” HOẶC “DC” HOẶC “VA” HOẶC “WV” HOẶC “DE” HOẶC “NJ” HOẶC “NY” 
Cuối cùng, số được tạo bởi QuantSoldOnWeekdaysToFemaleMidAtlanticCustomers 
phải được cắt theo loại sản phẩm. Biểu đồ cột trong Hình minh họa 6.49 thể hiện sự cắt lát này.
MINH HỌA 6.49  So sánh chủng loại sản phẩm: Số lượng 
Bán cho khách hàng nữ vùng Trung Đại Tây Dương vào các ngày trong tuần 
200
150
100
50
0
250
Vườn
238
văn phòng
126
Danh mục
số lượng
đã bán
So sánh danh mục sản phẩm:
Ai, Cái gì, Khi nào
Điện tử
7
Tiếp theo, sử dụng mô hình thông tin để khám phá một câu hỏi khác. 
• Câu hỏi ❹: Xác định tỷ lệ % (thước đo) chênh lệch đối với nhân viên (tên, là ai 
chiều). 
Câu trả lời cho câu hỏi này có thể tiết lộ nhân viên nào là người đàm phán tốt hơn. Cái này 
là loại câu hỏi thăm dò. Hình minh họa 6.50 cho thấy ngôi sao who-what-when 
lược đồ trả lời câu hỏi này.

![ILLUSTRATION 6.50](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.50.png)

6.3  Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán?  6-35
MINH HỌA 6.50  Lược đồ sao Ai làm gì khi nào để phân tích% sai lệch
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
Hàng hóa
Khách hàng
Lịch
nhân viên
Tên
bán hàng
% chênh lệch
Cột
Đo lường
MINH HỌA 6.51  So sánh 
Nhân viên dựa trên% chênh lệch
Gianni, Kobierski
Ngọc, Steeden
Arlyn, McCreery
Rosabel, Gabitus
Dalenna, Patillo
Valery, Bayles
Catherin, Tolliday
Sương mù, Coomer
Florella, McAllan
Hermina, Jeandillou
Padriac, phòng khách
Alyda, Greenhall
Tamra, Lambdin
Berti, Pridding
Loreen, Polye
Catharine, Laimable
Audie, Braniﬀ
Charlie, Libri
Clim, Orhtmann
Chancey, Donke
Aarika, bạch dương
Edik, Kiến thức
Silvain, MacTague
Sally, bão tuyết
Timmie, Brookzie
06/12
4,80
3,43
2,94
2,86
2,86
2,66
2,59
2,56
2,47
2,44
2,40
2,38
2,36
2,36
2,35
2,33
2,27
2,25
2,25
2,20
2.19
2.07
1,94
1,93
Tên nhân viên
% chênh lệch
Mẫu mô hình thông tin 13: Ngôi sao tích hợp 
Lược đồ
Hình minh họa 6.52 (A) cho thấy các ngôi sao ai-cái gì-khi nào được kết nối thông qua các tài nguyên. 
Nguồn lực được thu thập nhằm mục đích bán hoặc sử dụng chúng cho sản xuất, kiểm tra.
xin. Hình minh họa 6.52 (B) áp dụng mẫu cho KLUB. Vì KLUB mua hàng theo đợt 
Hình minh họa 6.51 chia thước đo % chênh lệch theo nhân viên (tên), cho thấy 
khả năng đàm phán của mỗi nhân viên. Để tạo ra những hiểu biết sâu sắc hơn, hãy sắp xếp phần trăm-
tuổi theo thứ tự giảm dần.

![ILLUSTRATION 6.52](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.52.png)

6-36  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
và bán chúng để kiếm lợi nhuận, các lược đồ sao Bán hàng và Mua hàng được kết nối thông qua 
bảng Hàng hóa.
MINH HỌA 6.52  Mẫu lược đồ hình sao tích hợp
Dòng chảy
trong
(A) Chung
(B) KLUB
Dòng chảy
ra ngoài
Dòng chảy
trong
Dòng chảy
ra ngoài
Mua hàng
Cái gì?
Tài nguyên
cái gì là
Đang là
Đã mua/bán?
Hàng hóa
Giao dịch
bán hàng
Giao dịch
Các ví dụ bổ sung về các ngôi sao tích hợp không thuộc bộ dữ liệu KLUB là:
• Từ các khoản thu từ tiền mặt đến các khoản giải ngân bằng tiền mặt.
• Mua lại tài sản cố định để khấu hao tài sản cố định.
Mô hình thông tin
Mẫu này mô tả dòng tài nguyên về mặt số lượng và giá trị. Nó giúp trả lời 
các câu hỏi về bao nhiêu tài nguyên đã được thu thập, dòng vốn vào là bao nhiêu, bao nhiêu 
còn hàng, bao nhiêu đã được sử dụng và sử dụng như thế nào (chẳng hạn như bán hàng). Hình minh họa 6.53 cung cấp một 
tổng quan về các khái niệm kế toán, mô hình thông tin, có thể bắt nguồn từ việc tích hợp 
Lược đồ sao Mua và Bán của KLUB như trong Hình minh họa 6.52.
MINH HỌA 6.53  Mô hình thông tin cho Lược đồ sao tích hợp của KLUB
Khái niệm/Lĩnh vực
Loại trường
Mô tả
Doanh thu
Cột được tính toán
Số tiền mà khách hàng phải trả cho 
mặt hàng đã bán.
giá vốn
Cột được tính toán
Số tiền mà KLUB thanh toán cho các mặt hàng 
họ đã bán.
Lợi nhuận
Cột được tính toán
Lợi nhuận KLUB kiếm được từ các mặt hàng họ bán.
Lợi nhuận ròng
Cột được tính toán
Lợi nhuận ròng KLUB kiếm được từ các mặt hàng đã bán 
sau khi trả tiền hoa hồng (chi phí bổ sung) cho 
nhân viên của họ (nhân viên bán hàng).
Tổngdoanh thu
Đo lường
Tổng doanh thu được tạo ra từ việc bán hàng.
Tổng COGS
Đo lường
Tổng số tiền mà KLUB thanh toán cho các mặt hàng mà họ 
đã bán.
Tổng lợi nhuận
Đo lường
Tổng lợi nhuận thu được từ việc bán hàng.
Tổng lợi nhuận ròng
Đo lường
Tổng lợi nhuận ròng được tạo ra từ việc bán hàng. 
Hoa hồng cho nhân viên được xem xét.
Tổng lợi nhuận ròng  
Ký quỹ
Đo lường
Tỷ suất lợi nhuận ròng tổng thể cho doanh thu của KLUB. 
Tổng lợi nhuận ròng/tổng ​​doanh thu.

![ILLUSTRATION 6.53](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.53.png)

6.3  Những mẫu nào giúp phát triển và triển khai các mô hình thông tin kế toán?  6-37
Một lần nữa, có nhiều cách để triển khai mô hình thông tin nâng cao liên quan đến 
với các lược đồ sao tích hợp. Công thức cho các cột và số đo bổ sung là 
thể hiện ở hình minh họa 6.54.
MINH HỌA 6.54  Mở rộng 
Mô hình thông tin của KLUB
Bảng: Doanh thu
Cột được tính toán
Thuật toán
Lợi nhuận
Doanh thu − Giá vốn hàng bán
Lợi nhuận ròng
Doanh số.Lợi nhuận − (Doanh số.Doanh thu × (Hàng hóa.Hoa hồng)/100)
Bảng: Doanh thu
Đo lường
Thuật toán
Tổng lợi nhuận
TỔNG(Lợi nhuận)
Tổng lợi nhuận ròng
TỔNG(Lợi nhuận ròng)
Tổng lợi nhuận ròngBiên lợi nhuận
[Tổng lợi nhuận ròng] / [Tổng doanh thu]
Cột Lợi nhuận được triển khai bằng phép tính số trong bảng.
mẫu tation (Mẫu 1). Việc triển khai cột NetProfit phức tạp hơn, 
vì cần có thông tin từ cả bảng Bán hàng và bảng Hàng hóa. Đây là 
một ứng dụng của mẫu triển khai tính toán trên nhiều bảng (Mẫu 4).
Việc thực hiện các biện pháp TotalProfit và TotalNetProfit đều là những ứng dụng 
của mẫu triển khai tổng hợp một cột (Mẫu 5), tính tổng các giá trị 
của một cột được tính toán. Cuối cùng, thước đo TotalNetProfitMargin là một ứng dụng của 
đo lường mẫu triển khai phân cấp (Mẫu 7).
Mô hình thông tin có thể được mở rộng hơn nữa với các biện pháp cụ thể hơn. Để thi-
Chẳng hạn, chúng ta có thể tính toán tổng lợi nhuận thu được từ việc bán hàng điện tử ở Mỹ. 
việc thực hiện biện pháp này được thể hiện trong Hình minh họa 6.55, đây là một ứng dụng của 
mẫu triển khai tổng hợp được lọc (Mẫu 6).
MINH HỌA 6.55  
Thực hiện các 
Lợi nhuậnForUSEĐiện tửBán hàng 
Đo lường
Bảng: Doanh thu
Đo lường
Thuật toán
Lợi nhuậnDành cho SỬ DỤNGĐiện tửBán hàng
TotalProfit Trong đó Customer.Country = “US” AND
  Merchandise.Category = “Điện tử”
Phân tích
Mô hình thông tin mở rộng này có thể trả lời nhiều câu hỏi liên quan đến tài chính của KLUB.
tình hình thực tế (Minh họa 6.56).
MINH HỌA 6.56  Trả lời 
Câu hỏi với KLUB tích hợp 
Lược đồ sao
Tỷ suất lợi nhuận ròng tổng thể của
các loại sản phẩm khác nhau?
25 khách hàng (tên) có ai
tỷ suất lợi nhuận ròng cao nhất?
Hãng máy in nào, HP hay Epson,
có tỷ suất lợi nhuận cao nhất? 
1
2
3
Những nhân viên (tên) nào có
tạo ra ít nhất 1.000 USD lợi nhuận?
Các tỉnh (tiểu bang) của Canada xếp hạng như thế nào
dựa trên tổng lợi nhuận được tạo ra?
4
5
Xu hướng (tháng) của lợi nhuận là gì
được tạo ra bằng cách bán đồ điện tử 
(danh mục) cho khách hàng Hoa Kỳ (tiểu bang)?
6
Kích thước
Biện pháp

![ILLUSTRATION 6.56](../TaiLieu/textbookForPractice/Figures/Ch_06/ILLUSTRATION%206.56.png)