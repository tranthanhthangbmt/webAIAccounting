6-56  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
BE 6,14  (LO 3)  Giả sử bạn muốn khám phá tổng doanh thu được tạo ra từ việc bán hàng từ cấp cao 
nhân viên bán hàng cho khách hàng Hoa Kỳ vào năm 2025 sẽ khác nhau giữa các danh mục sản phẩm. Nhân viên bán hàng được coi là cấp cao 
khi họ gắn bó với công ty ít nhất 10 năm sau ngày tuyển dụng. Hoàn thành lược đồ sao. 
Tên nhân viên
nhân viên
Tên bên cho thuê
Quốc gia
SốNgười Cho Thuê
Bên cho thuê
Bảng kích thước
Bảng sự kiện
tham gia
Dòng chảy
Xảy ra
tham gia
Bảng kích thước
ID máy bay
nhà sản xuất
Loại máy bay
Máy bay
Năm
Lịch
1
1
1
1
N
N
1
N
Số thuê
Cho ThuêKýNgày
Cho thuêNgày thành lập
Ngày chấm dứt hợp đồng thuê
Thời hạn thuê
Loại thuê
Số tiền thanh toán hàng năm
Tổng số tiền thuêSố tiền
Số lượng hợp đồng thuê
Tiền gốcSố tiền
nhân viên
Bên cho thuê
Ngày
Máy bay
Cho thuê
Chìa khóa
Cột
Cột được tính toán
Đo lường
Khóa ngoại
SốMáy Bay
Ngày
BE 6,15  (LO 3)  Địa Trung Hải là một hãng hàng không cỡ trung với các chuyến bay chủ yếu ở Châu Âu và Châu Phi. Họ 
thuê tất cả các máy bay của họ từ người cho thuê. Một phần của mô hình thông tin lược đồ sao của họ được hiển thị ở đây.
Bảng kích thước
Bảng sự kiện
tham gia
Dòng chảy
Xảy ra
tham gia
Bảng kích thước
1
1
1
1
N
N
N
N
Dòng hóa đơn
Cột
Cột được tính toán
Đo lường
Nhân viên bán hàng
Khách hàng
sản phẩm
Lịch

Bảng là từ điển dữ liệu cho mô hình thông tin này.
Tên
Mô tả
Tên nhân viên
Tên của nhân viên tại Địa Trung Hải chịu trách nhiệm về 
hợp đồng thuê.
Tên bên cho thuê
Người cho thuê máy bay.
Bên Cho ThuêĐất Nước
Nước của bên cho thuê.
SốNgười Cho Thuê
Tổng số bên cho thuê mà Mediterranean đã thuê máy bay.
Số thuê
ID của người thuê.
Cho ThuêKýNgày
Ngày hợp đồng thuê được ký kết.
Cho thuêNgày thành lập
Ngày bắt đầu hợp đồng thuê.
Ngày chấm dứt hợp đồng thuê
Ngày mà hợp đồng thuê kết thúc.
Tiền gốcSố tiền
Số tiền tài trợ bên thuê (Địa Trung Hải) đồng ý trả cho bên cho thuê.
Thời hạn thuê
Số năm một chiếc máy bay được thuê.
Loại thuê
Cho thuê ngắn hạn hoặc vận hành.
Cho thuê dài hạn hoặc tài chính.
Số tiền thanh toán hàng năm
Số tiền phải trả hàng năm cho hợp đồng thuê.
Tổng số tiền thuêSố tiền
Tổng số tiền cho tất cả các hợp đồng thuê.
Số lượng hợp đồng thuê
Tổng số hợp đồng thuê.
ID máy bay
ID duy nhất của máy bay.
nhà sản xuất
Người chế tạo máy bay—Boeing, Airbus hoặc Embraer.
Loại máy bay
Loại máy bay. Ví dụ: mô hình 787 (Boeing). 
SốMáy Bay
Tổng số máy bay được thuê.
Xác định ít nhất năm câu hỏi có thể được phân tích bắt đầu từ mô hình thông tin này.
Bài tập  6-57
Bài tập
EX 6.1  (LO 1)  Xác định mối quan hệ dữ liệu Đối với mỗi kịch bản được mô tả, hãy xác định mối quan hệ nào
mối quan hệ hoặc các mối quan hệ mà họ mô tả: tham gia, diễn ra hoặc xảy ra.
	 1. Thanh lý tài sản cố định.
	 2. Thanh toán bằng tiền mặt.
	 3. Lập báo cáo bán hàng hàng quý.
	 4. Trả lại hàng cho người bán.
	 5. Sản xuất ô tô điện theo yêu cầu.
EX 6.2  (LO 2)  Dữ liệu   Kế toán tài chính   Kế toán thuế   Xây dựng mô hình thông tin cho 
Báo cáo Doanh thu thuần và Đường cong thuế là một cửa hàng đồ nội thất được thiết kế theo yêu cầu. Họ cung cấp cho bạn một 
bảng tính chứa thông tin sau về doanh số bán hàng quý 1 năm 2025 của họ:
•  InvoiceNumber: Được sử dụng để xác định duy nhất các giao dịch bán hàng.
•  Số tiền: Tổng số tiền của một lần bán hàng.
•  Giảm giá: Khoản giảm giá, tính bằng đô la, được khấu trừ khỏi số tiền (bán hàng).
•  Thuế: Số tiền thuế, được xác định dưới dạng phần trăm, mà khách hàng phải trả trên số tiền bán hàng sau 
giảm giá đã được áp dụng.
	 1. Tạo một mô hình thông tin cho phép bạn xác định tổng doanh thu thuần và tổng thuế 
sẽ được Curves thu thập cho doanh số bán hàng Q1.
	 2. Sau khi đã có mô hình thông tin, hãy tạo báo cáo này.
$3,319,960
$136.463,17
Tổng doanh thu ròng
Tổng số thuế

6-58  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
EX 6.3  (LO 2)  Dữ liệu   Kế toán quản trị   Xây dựng mô hình thông tin cho tiêu chuẩn báo cáo 
Chi phí FonzieBikes là nhà sản xuất xe đạp và xe đẩy chuyên dụng của Canada. Các kỹ sư và kế toán của họ 
đã làm việc cùng nhau để xác định Bảng kê nguyên vật liệu (BoM) xác định những nguyên liệu thô nào cần thiết 
để tạo ra một thành phẩm (sản phẩm), bao nhiêu (số lượng) và chi phí (tiêu chuẩn) dự kiến cho mỗi sản phẩm đó là bao nhiêu. 
họ. Bạn được cấp một tập dữ liệu chứa mẫu dữ liệu BoM.
Xe ba bánh
Xe ba bánh
Xe ba bánh
Xe ba bánh
Xe đạp leo núi
Xe đạp leo núi
Xe đạp leo núi
Xe đạp leo núi
lỗi
lỗi
lỗi
lỗi
lỗi
lỗi
lỗi
Lốp xe ba bánh, mặt trước lớn
Khung xe ba bánh
lốp 4”
Bàn đạp xe ba bánh
Khung 18”
Bánh xe và lốp 26 inch
Tay cầm xe đạp leo núi
Hệ thống bánh răng
quả hạch
Bu lông
Đài phát thanh
Thân xe tải
Động cơ
Lốp ô tô
Sơn đen
1
1
1
2
1
2
2
1
2.500
2.750
1
1
1
4
40
96
150
64
28
213
34
44
81
0,01
0,01
111
430
1.015
69
2
$
$
$
$
$
$
$
$
$
$
$
$
$
$
$
Đã hoàn thành Nguyên liệu thô tốt
STDSố lượng STDChi phí
	 1. Tạo mô hình thông tin.
	 2. Sử dụng mô hình thông tin để tạo báo cáo hiển thị tổng chi phí tiêu chuẩn ước tính cho mỗi 
trong ba sản phẩm: xe ba bánh, xe đạp leo núi và xe buggy.
lỗi
Xe đạp leo núi
Xe ba bánh
Đã hoàn thànhTốt
Tổng chi phí tiêu chuẩn
1.964,50
450,00
366,00
$
$
$
EX 6.4  (LO 2)  Dữ liệu   Kế toán quản lý   Tạo báo cáo về Emory chi tiêu của khách sạn & 
Grant là một công ty kế toán khu vực ở miền đông nam Hoa Kỳ. Khi đi du lịch tới khách hàng, họ 
nhân viên có thể ở tại bất kỳ khách sạn Hilton hoặc Marriott nào. Bạn nhận được một bảng tính có tất cả tháng 2 năm 2025 
giao dịch khách sạn và số tiền phải trả cho mỗi lần lưu trú. Bạn được yêu cầu xây dựng một mô hình thông tin 
có thể xác định hai điều:
•  Số tiền chi tiêu cho các khách sạn Hilton, số tiền chi tiêu cho các khách sạn Marriott và số tiền chi tiêu cho 
khách sạn khác.
•  Tỷ lệ tương đối của Hilton, Marriott và các khách sạn khác trong chi phí lưu trú.
	 1. Phát triển mô hình thông tin.
	 2. Sau đó, tạo hai báo cáo sau:
Báo cáo 1: Số tiền chi tiêu cho mỗi chuỗi khách sạn.
Hilton
Marriott
Khác
Tổng cộng
khách sạn
Tổng số tiền đã chi
170.154,52
245.756,70
73.376,80
2.225,38
$
$
$
$

Báo cáo 2: Tỷ lệ chi phí lưu trú tương đối trên mỗi chuỗi khách sạn
EX 6.5  (LO 2)  Dữ liệu   Tạo mô hình thông tin để hỗ trợ quyết định tuyển dụng CreativeX là 
tuyển dụng giám đốc tài chính. Để được coi là đủ điều kiện, ứng viên phải đáp ứng ba tiêu chí sau:
•  Từ 30 đến 50 tuổi (>= 30 và <=50).
•  Chuyên môn về kiểm toán hoặc thuế, hoặc cả hai.
•  Hiện đang làm việc ở cấp độ 3 (quản lý) trở lên.
Công ty cung cấp cho bạn bảng tính chứa thông tin họ nhận được từ 
ứng viên.
Liz Smith
Jada Vaughn
Jenny Vương
Eric Kim
Harrison sương mù
ngôi sao George
Elton Seger
Isabella Fernande
Elise Jackson
Brenda Swif
Lindsay Lauper
Nicole Sardo
Cindy Raﬀerty
Greg Cuddy
Mateo Rodríguez
Caleb Cooke
Jane Harris
Debra Pollack
Sheldon Andrews
33
29
52
47
41
39
25
38
41
25
56
35
40
45
31
28
41
29
49
Y
Y
N
Y
N
Y
N
Y
Y
N
N
N
N
Y
N
Y
N
Y
Y
N
Y
N
Y
Y
N
N
N
Y
N
Y
N
N
N
Y
N
Y
N
Y
4
3
1
3
4
5
3
2
2
5
4
2
2
3
4
2
5
1
2
ứng viên
Kiểm toán
Thuế
Cấp độ
Tuổi
	 1. Tạo mô hình thông tin.
	 2. Sử dụng mô hình thông tin để tạo danh sách tên của các ứng viên đủ tiêu chuẩn.
EX 6.6  (LO 2)  Dữ liệu   Kế toán tài chính   Xây dựng mô hình thông tin cho mạng báo cáo 
Doanh thu Old Marine (OM) là nhà sản xuất quần áo ở Michigan. Bạn được cấp một bảng tính có thể
thu thập thông tin liên quan đến tất cả các đơn đặt hàng tháng 1 năm 2025. Nó có hai bảng tính:
•  Đơn đặt hàng: Đối với mỗi đơn hàng, một ID, ngày, số tiền và ID lô hàng duy nhất được cung cấp.
•  Lô hàng: Đối với mỗi lô hàng, một ID duy nhất, loại lô hàng, chi phí vận chuyển (Số tiền) và 
công ty vận chuyển được cung cấp.
Có hai loại vận chuyển:
•  Xuất xứ FOB (O): Khách hàng thanh toán chi phí vận chuyển.
•  Điểm đến FOB (D): Old Marine thanh toán chi phí vận chuyển.
Doanh thu ròng của một đơn hàng là số tiền của đơn hàng trừ đi chi phí vận chuyển do OM thanh toán.
	 1. Tạo mô hình thông tin cho phép bạn tạo tổng doanh thu thuần cho tháng 1 năm 2025 
Đơn đặt hàng.
	 2. Sử dụng mô hình thông tin để tạo báo cáo hiển thị con số này.
Hilton
69,23%
Marriott
29,86%
Khác
0,91%
Bài tập  6-59

6-60  CHƯƠNG 6  Phân tích: Mô hình hóa thông tin
EX 6.7  (LO 2)  Dữ liệu   Kế toán tài chính   Xây dựng mô hình thông tin về tỷ suất lợi nhuận 
Phân tích Berok là một công ty đầu tư nhỏ muốn đầu tư vào một trong ba công ty sau:
các cửa hàng tạp hóa khác: Cửa hàng tạp hóa ABC, Cửa hàng tạp hóa lân cận hoặc Cửa hàng tạp hóa toàn cầu. Họ tập hợp một bảng tính 
với dữ liệu về doanh thu và lợi nhuận của mỗi công ty trong 5 năm qua. Một tỷ lệ quan trọng cho phân tích tài chính của họ 
là tỷ suất lợi nhuận.
	 1. Xây dựng mô hình thông tin tính tỷ suất lợi nhuận.
	 2. Sử dụng mô hình thông tin để tạo hai hình ảnh sau:
một.	 Tỷ suất lợi nhuận của từng năm trong 5 năm trước (2021-2025) của mỗi công ty trong số ba công ty:
Cửa hàng tạp hóa ABC
Cửa hàng tạp hóa lân cận
Cửa hàng tạp hóa toàn cầu
7,55%
6,83%
7,62%
Tên
2021
7,94%
6,76%
8,57%
2022
7,55%
7,02%
7,52%
7,14%
6,67%
8,27%
2023
2024
8,05%
6,78%
8,59%
2025
b.	 Tỷ suất lợi nhuận tính trên tổng doanh thu, lợi nhuận giai đoạn 2021-2025 của từng ngành 
ba công ty:
Cửa hàng tạp hóa ABC
Cửa hàng tạp hóa lân cận
Cửa hàng tạp hóa toàn cầu
7,65%
6,82%
8,08%
Tên
Tỷ suất lợi nhuận 2021–2025
EX 6.8  (LO 2)  Dữ liệu   Kế toán quản trị   Tạo mô hình thông tin để xác định 
Tiền thưởng cho nhân viên Ruppetware là một nhà sản xuất nhỏ các sản phẩm nhà bếp sáng tạo. Ngoài ra 
Với mức lương cố định, nhân viên bán hàng tại Ruppetware có thể kiếm được một khoản tiền thưởng đáng kể vào cuối năm. Đây là 
thuật toán xác định tiền thưởng cho năm 2025:
•  Số tiền bán hàng mục tiêu năm 2025 cho mỗi nhân viên bán hàng được xác định bằng cách cộng thêm 5% vào mức trung bình năm 2024 
số tiền bán hàng cho tất cả nhân viên bán hàng.
•  Chỉ những nhân viên bán hàng đạt được mục tiêu đó mới được xem xét nhận tiền thưởng. Độ lớn của tiền thưởng là 
xác định như sau:
•  Nếu vượt mục tiêu dưới 5%, tiền thưởng là 5.000 USD.
•  Nếu vượt mục tiêu ít nhất 5% nhưng dưới 10% thì tiền thưởng là 10.000 USD.
•  Nếu vượt mục tiêu ít nhất 10% thì tiền thưởng là 15.000 USD.
	 1. Tạo mô hình thông tin cần thiết cho việc phân tích đó.
	 2. Tạo danh sách hiển thị số tiền thưởng năm 2025 cho tất cả nhân viên bán hàng.
EX 6.9  (LO 2)  Dữ liệu   Kế toán quản lý   Xây dựng mô hình thông tin cho tải trọng xe tải 
Quản lý Dịch vụ vận tải Leno (LTS) là một công ty vận tải tổng hợp báo cáo hàng ngày 
lập kế hoạch liên kết các xe tải có sẵn với các pallet cần vận chuyển trong ngày. Tất cả các phương tiện vận chuyển đều 
địa phương. Họ lưu giữ dữ liệu của mình trong ba bảng tính:
•  Bảng tính Xe tải chứa danh sách tất cả các xe tải hiện có. Đối với mỗi xe tải, LTS ghi lại một ID duy nhất 
và trọng lượng tối đa mà nó có thể chở được (tải trọng xe tải).
•  Bảng tính Pallet chứa danh sách tất cả các pallet phải vận chuyển trong một ngày nhất định. Đối với mỗi 
pallet, LTS ghi lại một ID duy nhất và tổng trọng lượng của hàng hóa hiện có trên đó. Trọng lượng pallet là 
tính bằng kilôgam (lưu ý, 1 Kilôgam = 2,20462 pound).
•  Bảng Lịch trình chứa lịch trình hàng ngày và do đó xác định những pallet nào phải được 
chất lên xe tải nào.
Sử dụng ba bảng tính, LTS yêu cầu bạn tạo một mô hình thông tin cho phép họ khám phá 
hai câu hỏi sau:
•  Có vượt quá trọng lượng tối đa của bất kỳ xe tải nào không?
•  Xe tải nào có tải trọng dưới 75%?

Bài tập  6-61
	 1. Tạo mô hình thông tin.
	 2. Sau khi đã có mô hình thông tin, hãy sử dụng mô hình đó để tạo bảng cung cấp danh sách tất cả các xe tải 
dự định đi chơi hôm nay. Đối với mỗi xe tải, hiển thị ID, trọng lượng tối đa, trọng lượng theo lịch trình, 
và tải theo lịch trình của nó. Sử dụng nền đỏ cho xe tải vượt quá trọng lượng tối đa và 
nền màu vàng dành cho xe tải có tải trọng dưới 75%. Báo cáo sẽ trông như sau:
1
2
3
4
5
6
7
10.000
25.000
15.000
20.000
20.000
25.000
15.000
TruckID Trọng lượng tối đa
7.826,40
25.974,83
11.794,72
16.997,62
8.267,33
19.246,33
4.078,55
Tổng trọng lượng
0,78
1.04
0,79
0,85
0,41
0,77
0,27
Tải
EX 6.10  (LO 2)  Dữ liệu   Kế toán tài chính   Tạo mô hình thông tin để hiển thị 401K 
Đóng góp Maurer and Cook là một công ty kế toán nhỏ ở trung tâm thành phố Reno, Nevada. Họ cung cấp 
để phù hợp với 0,75 đô la trên mỗi đô la đóng góp 401K của nhân viên của họ sau khi phân loại 
lịch trình hiển thị ở đây.
Số năm làm việc
Lịch trình trao quyền
0
0%
1
0%
2
20%
3
40%
4
60%
5
80%
6
100%
Đối tác quản lý đưa cho bạn một bảng tính Excel có tên của tất cả nhân viên, số năm công tác của họ.
phó và tổng đóng góp của nhân viên. 
	 1. Phát triển mô hình thông tin. 
	 2. Tạo một báo cáo hiển thị tổng số tiền đóng góp 401k của mỗi nhân viên. 
David Maurer
Mike Cook
Bernard Espinosa
Susan Hoover
Jamal Coleman
Elzbieta Jacek
Gail Wolcott
Billy Houston
Carlos Martinez
Amy mùa đông
705.047,00
638.946,00
438.663,75
437.302,25
321.413,75
234.108,00
78.167,25
50.912,40
37.590,80
30.483,70
nhân viên
Tổng số tiền đóng góp