8-34 
Chương 8  Diễn giải kết quả phân tích dữ liệu 
Ôn tập và thực hành chương
Đánh giá mục tiêu học tập
❶  So sánh cách diễn giải phân tích dữ liệu và dữ liệu 
thăm dò. 
Mặc dù việc khám phá và giải thích dữ liệu có vẻ giống nhau nhưng có 
sự khác biệt quan trọng:
•  Khám phá dữ liệu là quá trình phân tích dữ liệu để xác định 
liệu chúng ta có cần thực hiện các phân tích bổ sung hay không. Mục tiêu 
trong việc khám phá dữ liệu đang tiến đến mức chúng ta có đủ khả năng 
tự tin rằng chúng tôi hiểu những gì đang xảy ra trong dữ liệu. 
•  Diễn giải phân tích dữ liệu là quá trình đánh giá một kết quả phân tích 
để hiểu và giải thích ý nghĩa của nó. Những hiểu biết thu được từ 
giải thích dẫn đến quyết định kinh doanh tốt. 
❷  Áp dụng tư duy phê phán vào việc giải thích phân tích dữ liệu.
•  Hiểu biết về các bên liên quan giúp hiểu được các vấn đề
nội dung phân tích và ý nghĩa của kết quả. 
•  Xác định mục đích của việc phân tích sẽ duy trì sự tập trung vào mục đích của nó 
mục tiêu và tránh đi sai hướng trong việc diễn giải.
Áp dụng nó 8.5
Giải thích hồi quy 
Kết quả 
Dữ liệu   Kế toán quản trị   DHI muốn hiểu điều gì đang thúc đẩy tổng chi phí cho 
chuỗi khách sạn. Luciana cảm thấy chắc chắn rằng các biến số sau có ảnh hưởng lớn nhất đến chi phí:
• Tuổi của khách sạn
• Số lượng nhân viên bảo trì
• Tổng số giờ dọn phòng
• Tổng số phòng cho thuê 
Cô ấy đã yêu cầu bạn chuẩn bị mô hình hồi quy sử dụng các biến đó để dự đoán chi phí. Sau-
minh họa hạ thấp là kết quả của mô hình đó. 
Số giờ dọn phòng và số phòng được thuê theo địa điểm Mô hình hồi quy
Nhiều R
R vuông
Hình vuông R đã điều chỉnh
Lỗi chuẩn
Quan sát
ANOVA
0.7215151
0,520584
0.4714132
93901.466
44
df
SS
MS
F
3.73412E+11
3.43882E+11
Hồi quy
dư
Tổng cộng
4
39
43
7.17293E+11
9.3353E+10
8817485253
10.58724498
6.62556E-06
107148.5543
2.918679199
Đánh chặn
Cho thuê phòng
Giờ làm việc, dọn phòng
Tuổi
Nhân viên, Bảo trì
413314.47
11.015461
6.0934507
−3565.695
16762.392
1674.938087
6906.902129
5.531393108
−2.12885155
2.42690446
1.1016123
3.85739665
3.77412543
0,039637083
0,019949355
0.277382666
0,000534577
0,000418405
Ý nghĩa F
Hệ số lỗi chuẩn
t Thống kê
giá trị P
Thống kê hồi quy
GIẢI PHÁP
1. Bình phương R được điều chỉnh là 0,471, nghĩa là tiền thuê phòng, số giờ dọn phòng đã làm, tuổi 
của khách sạn và số lượng nhân viên bảo trì có thể chiếm 47,1% tổng chi phí. 
2. Mô hình có ý nghĩa – Ý nghĩa F nhỏ hơn 0,05 – vì vậy, tốt hơn là không có mô hình nào cả. 
3. Giá trị p của Số giờ làm việc, Công việc nội trợ lớn hơn 0,05 nên loại bỏ 
từ mô hình. 
1. Hình vuông R được điều chỉnh tiết lộ điều gì về mô hình?
2. Có mô hình thì tốt hơn là không có mô hình?
3. Có biến nào bạn muốn Luciana loại bỏ khỏi mô hình không? Tại sao?

![Apply It 8.5](../TaiLieu/textbookForPractice/Figures/Ch_08/Apply%20It%208.5.png)

Cách đi qua  
8-35
•  Khi diễn giải một phân tích, hãy cân nhắc xem có lựa chọn thay thế nào không 
giải thích hoặc phân tích thay thế cần được tiến hành.
•  Xác định các rủi ro tiềm ẩn như rủi ro dữ liệu, rủi ro phân tích và 
rủi ro thiên vị. 
•  Mọi diễn giải phân tích đều yêu cầu kiến ​​thức cụ thể. Xác định-
trang bị những kiến thức cần thiết về kế toán, ngành và công nghệ
edge cung cấp cho chúng tôi các công cụ để diễn giải phân tích. 
•  Giải thích phân tích tương tự được thực hiện trước đây có thể 
áp dụng trong bối cảnh hiện nay. 
❸  Xác định xem kết quả phân tích dữ liệu có đáp ứng được yêu cầu 
câu hỏi và phù hợp với mục tiêu phân tích.
Câu trả lời cho một số câu hỏi cụ thể có thể hữu ích khi giải thích-
tiến hành phân tích dữ liệu:
•  Phương pháp và kết quả có hợp lý với kiến thức hiện tại không?
cạnh về chủ đề đang được phân tích? Liệu việc phân tích và 
giải thích có ý nghĩa? Xem xét liệu việc phân tích có 
ý nghĩa rõ ràng. Nó có giải quyết được mục tiêu hoặc câu hỏi được đặt ra không? 
Cũng hãy xem xét liệu cách giải thích có hợp lý hay không.
•  Đôi khi cần thêm thông tin hoặc phân tích trước khi đưa ra quyết định cuối cùng 
việc giải thích có thể được hoàn thành. Tránh những rủi ro như “những gì bạn 
xem là tất cả đều có” thành kiến hoặc thiên vị xác nhận. 
❹  Đánh giá tính giá trị và độ tin cậy của mô tả 
và kết quả phân tích dữ liệu chẩn đoán.
Phân tích mô tả xác định những gì đã xảy ra trong quá khứ, trong khi 
phân tích chẩn đoán điều tra lý do tại sao nó xảy ra.
•  Các kỹ thuật phân tích mô tả phổ biến bao gồm tần suất 
phân phối, lập bảng chéo, đo lường vị trí và đo lường
chắc chắn về sự phân tán. 
•  Các kỹ thuật phân tích chẩn đoán phổ biến bao gồm sự bất thường 
phát hiện, phân tích tương quan và phân tích xu hướng.
•  Phân tích dữ liệu có giá trị nếu nó đo lường được những gì nó được cho là
chắc chắn và thể hiện hiện thực. 
•  Phân tích dữ liệu là đáng tin cậy nếu các thước đo được sử dụng trong phân tích 
chính xác và nhất quán và dữ liệu được sử dụng là đáng tin cậy 
và đáng tin cậy.
❺  Đánh giá tính giá trị và độ tin cậy của các phương pháp dự đoán và 
kết quả phân tích dữ liệu theo quy định.
Phân tích dự đoán được sử dụng khi mục tiêu của phân tích là 
để dự đoán một kết quả trong tương lai. Phân tích theo quy định nhằm mục đích quy định 
những hành động mang lại kết quả tốt nhất trong tương lai.
•  Hồi quy tuyến tính là nền tảng cho hầu hết các mô hình dự đoán-
kỹ thuật ing. Hiệu lực của mô hình hồi quy được đánh giá 
bằng cách mô hình thể hiện hiện tượng tương tác tốt như thế nào
est. Độ tin cậy của mô hình được đánh giá bằng cách đánh giá 
thống kê hồi quy, thống kê mô hình và giá trị p của 
các hệ số. 
•  Các mô hình tối ưu hóa và phân tích giả định thường được sử dụng 
cho các phân tích mang tính quy tắc. Trong nghề kế toán, chuyện gì sẽ xảy ra? 
phân tích có thể giúp đánh giá một số lựa chọn (Phân tích kịch bản) hoặc 
để xác định một đầu vào cụ thể (Tìm kiếm mục tiêu). 
•  Bất kể công cụ nào được sử dụng để tạo phân tích giả định, hãy đánh giá 
giá trị bằng cách xác định xem mô hình có đang đo lường những gì nó hỗ trợ hay không
đặt ra để đo lường (giá trị) và các biện pháp đó là chính xác 
và nhất quán (độ tin cậy).
Đánh giá các điều khoản chính
Chính xác  8-17
Bình phương R đã điều chỉnh (R2)  8-28
Sự bất thường  8-22
Phân tích tương quan  8-23
Hệ số tương quan  8-23
Phân tích bảng chéo  8-19
Giải thích phân tích dữ liệu  8-2
Phân bổ tần số  8-18
Hồi quy tuyến tính  8-27
Trung bình  8-19
Trung vị  8-19
Chế độ  8-19
Ngoại lệ  8-20
Thống kê hồi quy  8-28
Độ tin cậy  8-17
Biểu đồ phân tán  8-20
Độ lệch chuẩn  8-21
Sai số chuẩn  8-28
Phân tích xu hướng  8-24
Đường xu hướng  8-24
Hiệu lực  8-17
phân tích điều gì sẽ xảy ra  8-31
Cách đi qua 
CÁCH 8.1 
Tạo phân phối tần số với Power BI
Hình minh họa 8.14 là sự phân bố tần số cho các mẫu xe Super Scooter khác nhau. Nó đã được tạo ra 
trong Excel, nhưng các công cụ khác, chẳng hạn như Power BI, cũng có thể tạo phân bố tần số. 
Những gì bạn cần:  Dữ liệu   Tệp dữ liệu How To 8.1.
BƯỚC 1: Trích xuất dữ liệu. Mở Power BI và chọn tab Home ở ngang trên cùng 
menu (Minh họa 8.37).
Làm cách nào để

![ILLUSTRATION 8.37](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.37.png)

8-36
CHƯƠNG 8 Diễn giải kết quả phân tích dữ liệu 
Tự động Lưu
Chia sẻ
Bình luận
Dán
Cắt
Sao chép
Trình vẽ định dạng
Tập tin
Làm người mẫu
Máy tính để bàn Power BI không có tiêu đề
Xem
Trợ giúp
Chèn
Trang chủ
Bảng nhớ tạm
Mới
đo lường
nhanh chóng
đo lường
Độ nhạy
Xuất bản
Chia sẻ
Máy tính
Chèn
Truy vấn
dữ liệu
X
+
Excel
Sổ làm việc
Điện B1
bộ dữ liệu
SQL
Máy chủ
Nhập
dữ liệu
Dữ liệu ngược
Gần đây
nguồn
Nhận
dữ liệu
+
A
Mới
Trực quan
văn bản
cái hộp
Thêm
hình ảnh
Làm mới
chuyển đổi
dữ liệu
Độ nhạy
Dán
Cắt
Sao chép
Trình vẽ định dạng
Bảng nhớ tạm
lúa mạch đen
Làm mới
Mới
đo lường
nhanh chóng
đo lường
Độ nhạy
Xuất bản
Chia sẻ
Máy tính
Độ nhạy
Điều hướng
Tùy chọn hiển thị
Bán hàng siêu xe tay ga_
2024−2025.xlsx [2]
Giao dịch bán hàng
2024–2025
Giao dịch mua bán 2024–2025
Trang 2
Số thứ tự
Năm
Số đơn đặt hàng bán hàng
người mẫu
Ngày bán
13684−2024
13684
2024
Celeritas
31/12/2024
13685−2024
13685
2024
Lazer
31/12/2024
13682−2024
13682
2024
thuyền trưởng
30/12/2024
13683−2024
13683
2024
Lazer
30/12/2024
13677−2024
13677
2024
Lazer
29/12/2024
13678−2024
13678
2024
Lazer
29/12/2024
13679−2024
13679
2024
Celeritas
29/12/2024
13680−2024
13680
2024
thuyền trưởng
29/12/2024
13681−2024
13681
2024
Celeritas
29/12/2024
13675−2024
13675
2024
Celeritas
28/12/2024
13676−2024
13676
2024
thuyền trưởng
28/12/2024
13671−2024
13671
2024
thuyền trưởng
27/12/2024
13672−2024
13672
2024
Lazer
27/12/2024
13673−2024
13673
2024
Lazer
27/12/2024
13674−2024
13674
2024
thuyền trưởng
27/12/2024
13668−2024
13668
2024
thuyền trưởng
26/12/2024
13669−2024
13669
2024
Celeritas
26/12/2024
13670−2024
13670
2024
cú đá
26/12/2024
13665−2024
13665
2024
Lazer
25/12/2024
Hủy bỏ
Tải
Chuyển đổi dữ liệu
! Dữ liệu trong bản xem trước đã bị cắt bớt do giới hạn kích thước
Trang 1
Hãy chắc chắn rằng bạn
đánh dấu vào ô
trước “Bán hàng
Giao dịch 2024−
2025.” Nếu bạn quên
bạn sẽ không có
tùy chọn “Tải”. 
GỢI Ý
1
2
MINH HỌA 8.37 Trích xuất và tải dữ liệu siêu xe tay ga
• Chọn biểu tượng Excel bên dưới. 
• Khi hộp thoại file mở ra, tìm đến file Excel Super Scooters và chọn Open
ở góc dưới bên phải. 
BƯỚC 2: Nạp dữ liệu (Minh họa 8.37). Từ cửa sổ Điều hướng của Power BI, cửa sổ này tự động
mở ra một cách tự nhiên sau khi nguồn dữ liệu được chọn, hãy chọn dữ liệu cho bài tập này: Giao dịch bán hàng
hành động 2023–2025. Tiếp theo nhấn Load ở dưới cùng bên phải để tải dữ liệu này lên.
BƯỚC 3: Chuyển đổi dữ liệu để tạo bảng tần số (Minh họa 8.38). Màn hình 
sẽ quay lại màn hình Power BI chính. Cột Trường sẽ ở phía bên phải của 
màn hình. 
• Nhấp vào mũi tên thả xuống bên cạnh Giao dịch bán hàng 2023–2025 để xem tất cả tên cột 
từ bảng tính. 
• Kéo các trường dữ liệu Model và Σ Order Number vào các khoảng trống được cung cấp ngay bên dưới 
Giá trị.
• Mỗi trường có một mũi tên xuống chỉ ra một menu các tùy chọn. Chọn mũi tên này cho Σ
Trường Số thứ tự và menu kéo xuống xuất hiện. 
• Chọn Đếm. Tên trường sẽ thay đổi thành Số lượng đơn hàng. 
• Bên trái là bảng kết quả gồm 4 mẫu Super Scooter, 
số lượng đơn đặt hàng và tổng cộng. Bạn có thể phóng to bảng mới đó để xem tất cả 
cột.

![ILLUSTRATION 8.38](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.38.png)

Cách đi qua  
8-37
MINH HỌA 8.38  Xây dựng bảng tần số
Giá trị
Giá trị
Giao dịch mua bán 20...
Giao dịch mua bán 20...
Màu sắc
Màu sắc
Đóng góp M...
Đóng góp M...
Quốc gia
Quốc gia
Số ngày tồn kho
Số ngày tồn kho
Tổng doanh thu
Tổng doanh thu
Lao động
Lao động
Vị trí
Vị trí
Vật liệu
Vật liệu
người mẫu
người mẫu
Số thứ tự
Số thứ tự
Chi phí chung
Chi phí chung
Doanh thu
Doanh thu
Đơn đặt hàng bán hàng số...
Đơn đặt hàng bán hàng số...
Thuế bán hàng
Thuế bán hàng
Báo cáo chéo
Báo cáo chéo
Oﬀ
Oﬀ
Khoan qua
Khoan qua
Trực quan hóa
Trực quan hóa
Trường
Trường
123
người mẫu
người mẫu
Số thứ tự
Số thứ tự
Tìm kiếm
Tìm kiếm
BƯỚC 4: Thêm cột bảng tần số tương đối bằng cách quay lại cột Trường và se-
chọn trường Số thứ tự. Kéo nó xuống bên dưới trường Số lượng đơn đặt hàng trong 
Cột trực quan hóa. 
• Chọn menu mũi tên kéo xuống cho trường Số đơn hàng mới và chọn Đếm. 
• Trong menu mũi tên kéo xuống, chọn Hiển thị giá trị dưới dạng. Chọn mũi tên bên phải để 
Phần trăm của Tổng số. 
• Bên trái màn hình sẽ hiển thị cột mới tỷ lệ phần trăm tổng doanh thu của từng sản phẩm 
mẫu xe tay ga và tổng thể (Minh họa 8.39). Một lần nữa, có thể cần phải phóng to 
bảng để xem cột mới.
MINH HỌA 8.39  Siêu phẩm cuối cùng 
Bảng tần số xe tay ga
người mẫu
thuyền trưởng
Celeritas
892
cú đá
Lazer
Tần số
1.010
456
Tổng doanh thu
3.645
1.287
24,47%
Tần số tương đối
27,71%
12,51%
100,00%
35,31%
• Cuối cùng, có thể đổi tên các cột thành “Tần suất” và “Tương đối”. 
Tần suất” bằng cách nhấp vào mũi tên xuống tương tự được sử dụng để chọn Đếm và thay vào đó chọn 
Đổi tên cho Visual này. 
Cũng có thể thực hiện phân phối tần suất bằng cách sử dụng PivotTable hoặc bằng cách sử dụng trực quan hóa dữ liệu.
phần mềm hoạt động. 
CÁCH 8.2 
Tính toán thống kê mô tả  
trong Microsoft Excel 
Để tạo Minh họa về doanh số bán hàng của Super Scooters trong Hình minh họa 8.18, hãy sử dụng Mô tả 
Tùy chọn thống kê trong Công cụ phân tích dữ liệu trong Microsoft Excel. 
Làm cách nào để

![ILLUSTRATION 8.39](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.39.png)

8-38 
Chương 8  Diễn giải kết quả phân tích dữ liệu 
được rồi
Hủy bỏ
Trợ giúp
Phân tích dữ liệu
Công cụ phân tích
?
Anova: Yếu tố đơn lẻ
Anova: Hai yếu tố với sự nhân rộng
Anova: Hai yếu tố không cần nhân rộng
Tương quan
Hiệp phương sai
Thống kê mô tả
Làm mịn theo cấp số nhân
F-Test Hai mẫu cho phương sai
Phân tích Fourier
biểu đồ
MINH HỌA 8.41  Phân tích 
Hộp thoại Công cụ
được rồi
Hủy bỏ
Trợ giúp
Thống kê mô tả
đầu vào
Cột
Hàng
Phạm vi đầu vào:
Được nhóm theo:
Tùy chọn đầu ra
Phạm vi đầu ra:
Sổ làm việc mới
Lớp bảng tính mới:
Thống kê tóm tắt
Mức độ tin cậy cho giá trị trung bình:
Kth nhỏ nhất:
Lớn thứ K:
$B$1:$B$37
1
95
%
1
?
Nhãn ở hàng đầu tiên
3
4
MINH HỌA 8.42  Mô tả 
Hộp thống kê
MINH HỌA 8.40  Siêu 
Dữ liệu xe tay ga 
Tự động Lưu
tập tin
Bố cục trang
Công thức
Xem lại
Chèn
Trang chủ
ngoại hối
1
Tháng/
Năm
23 tháng 1
23 tháng 2
23 tháng 3
154
182
126
bán hàng
khối lượng
A
B
C
D
Trang 1
2
3
4
E
dữ liệu
1
F13
Bảng nhớ tạm
Hoàn tác
Phông chữ
Dán
Calibri
A
A
11
B
tôi
bạn
A
Những gì bạn cần: Dữ liệu Tệp dữ liệu How To 8.2.
BƯỚC 1: Mở bảng tính bằng cách nhấp vào Dữ liệu trên thanh công cụ. (Minh họa 8.40). 
BƯỚC 2: Chọn Thống kê mô tả (Minh họa 8.41).
BƯỚC 3: Trong hộp Thống kê mô tả, chỉ định phạm vi đầu vào (Minh họa 8.42).

![ILLUSTRATION 8.42](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.42.png)