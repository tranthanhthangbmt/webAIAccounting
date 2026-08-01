8-24 
Chương 8  Diễn giải kết quả phân tích dữ liệu 
Tương quan là thước đo hợp lệ để kiểm tra mối quan hệ tuyến tính giữa các biến trong 
dữ liệu và việc giải thích mối tương quan phải dựa trên hệ số tương quan. 
Phân tích tương quan là đáng tin cậy nếu các hệ số tương quan nhất quán và chính xác 
liên quan đến dữ liệu đang được phân tích. Trong ví dụ về kem và súp, mối tương quan là 
hợp lệ vì chúng tôi đang kiểm tra mối tương quan logic bằng cách sử dụng hệ số tương quan. Đó là 
đáng tin cậy nếu chúng ta tin rằng các hệ số tương quan là nhất quán và chính xác. 
Phân tích tương quan có thể được thực hiện bằng cách sử dụng dữ liệu Super Scooters: 
• Ban quản lý Super Scooters đang xem xét các chi phí tiếp thị có thể thay đổi và muốn 
để biết liệu có mối quan hệ giữa số tiền chi cho hoạt động tiếp thị đa dạng hay không 
(chiết khấu dành cho đại lý mua sản phẩm Super Scooters) và bán hàng 
khối lượng. 
• Ban quản lý lo ngại rằng họ đã chi 1,1 triệu USD cho hoạt động tiếp thị đa dạng vào năm 2024 và 
họ không chắc liệu chi tiêu đó có làm tăng doanh số bán hàng hay không. 
Hình minh họa 8.24 là bảng tổng hợp các hệ số tương quan về tổng doanh thu, doanh số bán hàng
ume, và chi phí tiếp thị thay đổi.
Hệ số tương quan giữa tiếp thị biến đổi và tổng doanh thu là 0,9650. Người phiên dịch-
của con số đó là có mối tương quan tích cực mạnh mẽ giữa tổng doanh thu và biến 
chi phí tiếp thị. Khi chi phí tiếp thị biến đổi tăng lên, tổng doanh thu cũng tăng theo. Ngoài ra còn có một sức mạnh 
mối tương quan giữa khối lượng bán hàng và tiếp thị biến đổi với hệ số tương quan là 0,77410. 
Mặc dù chúng tôi không thể chứng minh được mối quan hệ nhân quả nhưng chúng tôi có thể nói rằng dường như có mối tương quan tích cực mạnh mẽ 
giữa số tiền chi cho tiếp thị đa dạng và cả khối lượng bán hàng và tổng doanh thu.
Xác định mẫu
Phân tích xu hướng là một công cụ thống kê sử dụng dữ liệu lịch sử để xác định các mẫu. Nó có thể giải thích tại sao 
điều gì đó đang xảy ra. Đường xu hướng cho biết diễn biến chung hoặc xu hướng của dữ liệu và được 
được tạo bằng cách sử dụng các điểm dữ liệu lịch sử để ước tính một đường.3 Việc kiểm tra các xu hướng giúp phát hiện các mẫu 
và các mối quan hệ, có thể xác định các cơ hội hoặc mối đe dọa tiềm ẩn đối với doanh nghiệp. 
Cách tốt nhất để xác định xu hướng là vẽ biểu đồ dữ liệu theo thời gian. Hình minh họa 8.25 là một 
phân tích xu hướng chi phí nguyên vật liệu và doanh số bán hàng của Super Scooters trong những năm 2023–2025. 
MINH HỌA 8.24 
 
Tóm tắt hệ số tương quan 
dành cho siêu xe tay ga
Tương quan
hệ số
0,9650
0,7749
Tổng doanh thu
Khối lượng bán hàng
Phân tích 3Xu hướng cũng có thể được sử dụng như một phương pháp phân tích dự đoán. 
MINH HỌA 8.25  Phân tích xu hướng chi phí nguyên vật liệu và doanh số bán hàng của siêu xe tay ga 
bán hàng
khối lượng
$260K
$240K
$220K
$200K
$180K
$160K
$140K
$120K
$100K
$80K
$60K
$40K
$20K
$0K
0
200
400
600
800
1.000
1.200
1.400
1.600
1.800
2.000
2.200
2.400
2.600
2.800
3.000
3.200
3.400
3.600
Tháng ba.
2023
Tháng Sáu.
2023
Tháng 9
2023
Tháng mười hai
2023
Tháng ba.
2024
Tháng Sáu.
2024
Tháng 9
2024
Tháng mười hai
2024
Tháng mười hai
2025
Tháng ba.
2025
Tháng Sáu.
2025
Tháng 9 
2025
Chi phí vật liệu
Khối lượng bán hàng 
Vật liệu
Tháng mười hai
2022
Tháng và Năm
Xu hướng chi phí vật liệu và khối lượng bán hàng của siêu xe tay ga

![ILLUSTRATION 8.25](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.25.png)

8.4  Độ hiệu lực và độ tin cậy được xác định như thế nào trong các phân tích mô tả và chẩn đoán?  8-25
ÁP DỤNG TƯ duy phản biện 8.3: Diễn giải 
Phân tích chẩn đoán
Khi giải thích lý do tại sao điều gì đó xảy ra, hãy sử dụng phân tích chẩn đoán: 
• Kết quả phân tích chẩn đoán có thể được sử dụng để đưa ra những giải thích khác. Ví dụ như việc bán hàng 
xu hướng dường như xen kẽ với mức tăng và sau đó giảm vào quý tiếp theo. Có lẽ doanh số bán hàng 
các chương trình khuyến mãi đang thúc đẩy mô hình này (Các lựa chọn thay thế).
• Tìm kiếm các mối đe dọa tiềm ẩn đối với phân tích, chẳng hạn như các điểm bất thường. Có bất kỳ quan sát nào trong 
phân tích xu hướng bất thường hoặc bất ngờ (Rủi ro)? 
• Xem xét những gì cần thiết để hiểu các phân tích, chẳng hạn như phân tích tương quan và phân tích xu hướng 
phân tích (Kiến thức). 
Áp dụng nó 8.4 
Giải thích một  
Biểu đồ phân tán cho 
Ngoại lệ
Dữ liệu   Kiểm toán   Roberto Jimenez là giám đốc hoạt động của DHI. Anh ấy đã hỏi người liên
bộ phận kiểm toán cuối cùng để giúp anh ta thực hiện phân tích số giờ dọn phòng. Roberto muốn 
để biết các vị trí khác nhau đang hoạt động hiệu quả như thế nào. Bạn đã được cung cấp một biểu đồ phân tán 
hiển thị số giờ dọn phòng đã làm và số phòng thuê theo vị trí khách sạn. các 
đường xuyên qua biểu đồ là đường xu hướng biểu thị mối quan hệ tuyến tính giữa số giờ làm việc 
và thuê phòng. Lưu ý rằng những con số được liệt kê bên dưới dấu chấm là số vị trí khách sạn. Tất cả 
dữ liệu trong biểu đồ phân tán là những quan sát hợp lệ.
1. Xem lại biểu đồ phân tán, xác định các giá trị ngoại lệ tiềm năng và giải thích lý do tại sao bạn xác định chúng là các giá trị ngoại lệ. 
2. Đề xuất cách giải quyết các trường hợp ngoại lệ.   
Phân tích xu hướng được chuẩn bị bằng phần mềm trực quan hóa dữ liệu. Phân tích xu hướng cũng có thể 
được chuẩn bị trong Microsoft Excel bằng cách sử dụng công cụ đường xu hướng có sẵn khi dữ liệu được 
được biểu đồ. 
Super Scooters đang kiểm tra lý do tại sao chi phí nguyên liệu ngày càng tăng. Việc phân tích ở 
Hình minh họa 8.25 cho thấy khối lượng bán hàng và chi phí nguyên vật liệu thay đổi theo cùng một mô hình 
năm và cả hai đều tăng: 
• Điều hợp lý là khối lượng bán hàng tăng sẽ dẫn đến chi phí nguyên vật liệu tăng. Có sim-
ilar đỉnh và thung lũng trong dòng. Đây là một dấu hiệu cho thấy có thể có một mùa 
mẫu để bán hàng. 
• Các đường xu hướng trong phân tích (các đường thẳng nét đứt) cho thấy rằng mặc dù cả hai đường xu hướng 
dây chuyền ngày càng tăng, chi phí nguyên vật liệu ngày càng tăng với tốc độ cao hơn. 
Sau khi xem xét phân tích này, chúng ta có thể kết luận rằng chi phí nguyên vật liệu đang tăng lên do 
tăng khối lượng bán hàng.  
Việc phân tích khối lượng bán hàng và chi phí nguyên vật liệu này có giá trị vì nó sử dụng 
phương pháp để hiểu mối quan hệ giữa xu hướng bán hàng và chi phí. Các mea-
Những điều chắc chắn được sử dụng trong phân tích là chính xác và nhất quán, đồng thời dữ liệu đáng tin cậy và
xứng đáng nên phân tích cũng đáng tin cậy. Tuy nhiên, hiểu được tại sao chi phí nguyên vật liệu lại tăng 
với tốc độ nhanh hơn doanh số bán hàng sẽ yêu cầu điều tra nhiều hơn.

![Apply It 8.4](../TaiLieu/textbookForPractice/Figures/Ch_08/Apply%20It%208.4.png)

8-26 
Chương 8  Diễn giải kết quả phân tích dữ liệu 
GIẢI PHÁP
1. Có mối quan hệ tích cực giữa số giờ dọn phòng và giá thuê phòng. Như số-
Số lượng phòng thuê tăng lên và số giờ dọn phòng cũng tăng theo. Điều này có ý nghĩa 
vì phòng đã thuê phải được dọn dẹp. 
	
Có một số quan sát vị trí khách sạn nằm xa đường xu hướng hơn các quan sát khác. 
quan sát:  
• Vị trí 30 có số giờ dọn phòng cao nhất nhưng không phải là số phòng cao nhất 
cho thuê.
• Địa điểm 105 có số giờ dọn phòng thấp nhưng số lượng phòng cho thuê lại cao.
2. Khuyến nghị:
• Điều tra sâu hơn tại Địa điểm 30 để xác định nguyên nhân quản lý kém hiệu quả 
giờ.
• Điều tra sâu hơn về Địa điểm 105 để xác định tính hiệu quả có thể áp dụng cho ít hơn 
những địa điểm hiệu quả.
0
0
2
4
6
8
10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44
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
23
Số giờ đã làm việc,
dọn phòng
(Tính bằng nghìn) 
Giá thuê phòng (Tính theo nghìn)
Giờ dọn phòng đã làm việc và số phòng được thuê theo địa điểm
33
105
11
29
52
18
1
22
87
15 12
25
16
37
2
3
17
7
31
21
56
9
70
5
10
97
93
6 32
39
40
30
59
43

8.5  Độ giá trị và độ tin cậy được đánh giá như thế nào trong các phân tích dự đoán và phân tích theo quy định?  27-8
8.5  Hiệu lực và độ tin cậy như thế nào 
Đánh giá trong dự đoán và quy định 
Phân tích?
MỤC TIÊU BÀI HỌC ➎
Đánh giá tính hợp lệ và độ tin cậy của kết quả phân tích dữ liệu dự đoán và quy định.
Như bạn đã biết, hai loại phân tích còn lại là phân tích dự đoán và phân tích theo quy định. 
Phần tiếp theo đề cập đến các loại phân tích trong những lĩnh vực này mà bạn có thể gặp phải trong 
sự nghiệp của bạn và cách xác định xem các phân tích có đáng tin cậy và hợp lệ hay không.
Phân tích dự đoán 
Có nhiều loại phân tích dự đoán, nhưng chúng đều có mục tiêu là dự đoán một 
kết quả trong tương lai. Trong nghề kế toán, phân tích dự báo phổ biến nhất là phân tích tuyến tính. 
hồi quy, là một công cụ để xây dựng các mô hình toán học và thống kê nhằm giải thích các 
mối quan hệ giữa một biến phụ thuộc và một hoặc nhiều biến độc lập. Kể cả nếu 
bạn không chuẩn bị các mô hình hồi quy tuyến tính trong sự nghiệp của mình, việc hiểu về hồi quy có thể giúp ích 
hiểu các mô hình dự đoán mà bạn gặp phải.  
Mô hình hóa mối quan hệ
Phân tích dự đoán xây dựng mô hình để giúp dự đoán hoặc hiểu rõ hơn về một hiện tượng. Xây dựng-
việc xây dựng một mô hình dự đoán chi phí cung ứng sẽ giúp hiểu được các yếu tố ảnh hưởng 
chi phí vật tư. Xây dựng mô hình này yêu cầu xác định các biến sẽ được đưa vào 
trong đó. 
Khi mô hình hồi quy hoàn tất, làm sao chúng ta biết liệu nó có hợp lệ hay không? Hãy nhớ rằng một 
phân tích có giá trị nếu nó đo lường được những gì cần đo lường và nếu nó cũng phản ánh được thực tế. 
Hãy xem xét các biến trong mô hình – chúng có hợp lý dựa trên mục tiêu của mô hình không? 
Ví dụ: khi đánh giá một mô hình kiểm tra tác động của nhiệt độ đến lợi ích
doanh số bán áo khoác, sẽ hợp lý nếu cả nhiệt độ và giá trung bình của áo khoác đều 
được đưa vào mô hình. Mô hình cũng có thể bao gồm cả tuyết rơi. Tuy nhiên, nếu mô hình bao gồm 
một biến số không có ý nghĩa, chẳng hạn như số lượng đồ bơi được bán, mẫu sẽ không được 
hợp lệ. Nó sẽ không đo lường những gì nó dự định đo lường. 
Bước tiếp theo là xác nhận mô hình là đáng tin cậy. Hãy nhớ lại rằng độ tin cậy có nghĩa là 
các biện pháp được sử dụng trong phân tích là chính xác và nhất quán và dữ liệu đáng tin cậy và 
đáng tin cậy. May mắn thay, có rất nhiều biện pháp thống kê trong phân tích hồi quy có thể 
được kiểm tra để xác định độ tin cậy. Các chương trước đã mô tả cách xây dựng hồi quy 
mô hình hóa và giải thích kết quả hồi quy. Ở đây, chúng tôi tập trung vào số liệu thống kê quan trọng và kết quả đầu ra 
giúp đánh giá và giải thích đầu ra của mô hình hồi quy. Hãy nhớ rằng nếu mô hình không 
hợp lệ, thì việc nó có đáng tin cậy hay không cũng không thành vấn đề. Một thước đo chính xác và nhất quán của mô hình 
không có nghĩa là mô hình đại diện cho thực tế. Vì vậy, bước đầu tiên để xác định xem mô hình có thay đổi hay không
khả năng logic là quan trọng. 
Độ tin cậy của mô hình hồi quy
Đánh giá độ tin cậy của phân tích hồi quy bằng cách xem xét số liệu thống kê của mô hình. Minh họa 
8.26 là đầu ra của mô hình hồi quy bội để dự đoán chi phí của bộ phận mua hàng 
dành cho siêu xe tay ga. Lưu ý rằng chi phí bộ phận mua hàng là những chi phí phát sinh

8-28 
Chương 8  Diễn giải kết quả phân tích dữ liệu 
bởi bộ phận mua hàng để xử lý các đơn đặt hàng (bảng lương, hành chính và vượt mức)
đầu). Những chi phí này không giống như chi phí mua hàng. Mô hình này dựa trên lịch sử 
dữ liệu, được thu thập từ mỗi địa điểm sản xuất, về các biến được cho là có ảnh hưởng đến tổng
theo đuổi chi phí của bộ phận. 
MINH HỌA 8.27  Hồi quy 
Thống kê cho phòng mua hàng 
Chi phí
Thống kê hồi quy
Nhiều R
Hình vuông R đã điều chỉnh
R vuông
Quan sát
Lỗi chuẩn
0.892897453
0.777957848
0.797265861
24
1.337.156824
Trong mô hình này, tổng chi phí của bộ phận mua hàng là biến phụ thuộc và doanh thu 
khối lượng và số lượng đơn đặt hàng được xử lý là các biến độc lập. 
Phép hồi quy trong Hình minh họa 8.26 được thực hiện bằng Microsoft Excel. Tóm tắt 
Đầu ra được chia thành ba phần. Đầu tiên là thống kê hồi quy, là số liệu thống kê 
các biện pháp được sử dụng để đánh giá mô hình. Hình minh họa 8.27 cho thấy thống kê hồi quy từ 
Minh họa 8.26.
MINH HỌA 8.26  Mô hình hồi quy chi phí bộ phận mua siêu xe tay ga
Nhiều R
R vuông
Hình vuông R đã điều chỉnh
Lỗi chuẩn
Quan sát
ANOVA
0.892897453
0.797265861
0.777957848
1.337.156824
24
df
SS
MS
F
147659116.6
37547755.8
Hồi quy
dư
Tổng cộng
2
21
23
185206872.4
73829558.29
1787988.371
41.29196782
5.2812E-08
877.1183137
31.32217805
Đánh chặn
Số đơn đặt hàng
Khối lượng bán hàng
−994.5719771
180.0127037
1.191401172
0.351035522
3.393961854
−1.133908575
5.747132382
0,002736568
1.05165E-05
0.269611889
Ý nghĩa F
Hệ số lỗi chuẩn
t Thống kê
giá trị P
TÓM TẮT ĐẦU RA
Hồi quy chi phí bộ phận mua siêu xe tay ga
Thống kê hồi quy
Tất cả số liệu thống kê hồi quy cung cấp cái nhìn sâu sắc về mô hình hồi quy. Mỗi thống kê này
các vấn đề cơ bản đã được đề cập trong chương dành cho các kỹ năng phân tích dữ liệu cơ bản. Dưới đây là một số 
số liệu thống kê quan trọng nhất để đánh giá độ tin cậy của mô hình: 
• Bình phương R đã điều chỉnh (R2): Giải thích mức độ phù hợp của đường hồi quy với dữ liệu. các 
R2 được điều chỉnh là một thống kê điều chỉnh giá trị của R2 bằng cách kết hợp cỡ mẫu 
và số lượng biến độc lập. Nói chung, sử dụng R2 đã điều chỉnh để đánh giá 
mô hình hồi quy bội. R2 càng gần 1 thì độ phù hợp của hồi quy càng tốt 
dòng vào dữ liệu.
• Sai số chuẩn: Trong kết quả hồi quy của Excel, sai số chuẩn biểu thị độ biến thiên của 
các giá trị biến phụ thuộc được quan sát từ các giá trị được mô hình dự đoán. 
Nói cách khác, nó so sánh biến phụ thuộc thực tế với giá trị dự đoán mà 
mô hình cung cấp. Nếu dữ liệu được nhóm gần với đường hồi quy thì tiêu chuẩn 
lỗi sẽ nhỏ. Nếu dữ liệu phân tán nhiều hơn thì sai số chuẩn sẽ lớn hơn. A 
sai số chuẩn nhỏ là tối ưu.

![ILLUSTRATION 8.27](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.27.png)