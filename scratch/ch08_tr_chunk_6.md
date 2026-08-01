8.5  Độ giá trị và độ tin cậy được đánh giá như thế nào trong các phân tích dự đoán và phân tích theo quy định?  29-8
	 Hình minh họa 8.27 thể hiện thống kê hồi quy cho Hình minh họa 8.26: 
•  Bình phương R được điều chỉnh trong Hình minh họa 8.27 là 0,778. Chúng tôi giải thích rằng 77,8% 
tổng chi phí có thể được giải thích bằng số lượng đơn đặt hàng được xử lý và bằng 
khối lượng bán hàng.
•  Sai số chuẩn trong mô hình này là $1.337,16. Để xác định xem đây là một lớn hay 
một sai số chuẩn nhỏ, hãy so sánh nó với độ lệch chuẩn của biến phụ thuộc 
biến. Trong ví dụ này, so sánh sai số chuẩn với độ lệch chuẩn 
trong tổng chi phí. Hình minh họa 8.28 cung cấp giá trị trung bình và độ lệch chuẩn cho 
tổng chi phí.
•  Độ lệch chuẩn của $2.837,69 cao hơn sai số chuẩn của $1.337,16 trong 
mô hình hồi quy. Sai số chuẩn trong mô hình này sẽ được coi là một số-
nhỏ gì.
Phần tiếp theo của đầu ra tóm tắt hồi quy là đầu ra phân tích phương sai (ANOVA). 
Hình minh họa 8.29 là phần ANOVA từ mô hình hồi quy. ANOVA là một thử nghiệm cho 
Ý nghĩa của toàn bộ mô hình:
• Trong một hồi quy tuyến tính bội như thế này, mức ý nghĩa là phép kiểm tra xem liệu hồi quy có 
mô hình tốt hơn mô hình không có biến độc lập. Nói cách khác, là mô hình 
tốt hơn là không có mô hình nào cả? 
• Nói chung, một mô hình được coi là có ý nghĩa nếu thống kê F (Ý nghĩa F trong hình minh họa 
8,29) nhỏ hơn 0,05. 
MINH HỌA 8.28  Siêu 
Phòng thu mua xe tay ga 
Chi phí
Mua siêu xe tay ga
Chi phí bộ phận
2022 – 2024
Nghĩa là
Độ lệch chuẩn
$ 3,725,30
$ 2,837,69
MINH HỌA 8.29  ANOVA 
Thống kê hồi quy cho 
Chi phí bộ phận mua hàng
ANOVA
Chi phí của bộ phận mua hàng Kết quả ANOVA
dư
Hồi quy
Tổng cộng
df
21
2
23
SS
37547755.8
147659116.6
185206872.4
MS
1787988.371
73829558.29
F
41.29197
Ý nghĩa F
5.2812E-08
Vậy mô hình có quan trọng không? ANOVA trong Hình minh họa 8.29 có Ý nghĩa F là 
5.2812E-08. Ký hiệu “E-08” sau 5.2812 thể hiện ký hiệu khoa học, còn được gọi là 
ký hiệu hàm mũ. 5.28.12E-08 giống với 0,000000052812. Đây là một con số dưới đây 
0,05 nên mô hình có ý nghĩa. Nói cách khác, các biến độc lập có thể giải thích một số 
sự thay đổi của tổng chi phí, vì vậy tốt hơn là không có mô hình nào cả. 
Phần cuối cùng của kết quả tóm tắt hồi quy cung cấp thông tin để tạo ra 
phương trình dự đoán biến phụ thuộc. Nếu điều chỉnh R bình phương và sai số chuẩn 
có thể chấp nhận được và mô hình có ý nghĩa thì chúng ta có thể diễn giải phương trình của mô hình. 
Điểm chặn và các hệ số của mô hình thể hiện phương trình của đường thẳng tốt nhất 
phù hợp với dữ liệu. Thống kê quan trọng cần phân tích trong phần này là giá trị p cho mỗi thông số độc lập.
biến số vết lõm. Giống như thống kê F, giá trị p cung cấp một phép thử về ý nghĩa. Đó là một bài kiểm tra để 
liệu biến độc lập có cải thiện khả năng của mô hình trong việc dự đoán biến phụ thuộc hay không 
biến. Giá trị p từ 0,05 trở xuống được coi là đáng kể. 
Hãy sử dụng kết quả đầu ra trong Hình minh họa 8.30 để xác định mô hình dự đoán cho Super Scoot-
tổng chi phí của bộ phận mua hàng của người đó và sau đó giải thích các hệ số. Lưu ý rằng 
giá trị p cho tất cả các biến độc lập đáp ứng được kiểm định nhỏ hơn 0,05 và có-
đáng kể trước đây.

![ILLUSTRATION 8.30](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.30.png)

8-30
CHƯƠNG 8 Diễn giải kết quả phân tích dữ liệu 
Mô hình dự đoán sẽ bằng điểm chặn, cộng với các hệ số độc lập
biến dent, nhân với giá trị dự đoán cho các biến đó. Dựa trên hồi quy 
mô hình ở Hình minh họa 8.30, phương trình dự đoán tổng chi phí bộ phận mua hàng là:
($994,57) + $180,01 (số lượng đơn đặt hàng) + $1,19 (khối lượng bán hàng)
Hình minh họa 8.31 là cách tính tổng chi phí dự kiến nếu 12 đơn đặt hàng được thực hiện
ngừng hoạt động và 2.200 xe tay ga được bán.
ÁP DỤNG TƯ duy phê phán 8.4: Diễn giải dự đoán 
Phân tích
Nếu phân tích được diễn giải dự đoán một kết quả trong tương lai thì bạn sẽ diễn giải trước
phân tích định tính: 
• Trong ví dụ về chi phí bộ phận mua hàng của Super Scooters, mục đích của mô hình là 
hiểu rõ hơn và dự đoán chi phí của bộ phận (Mục đích). 
• Việc đưa ra dự đoán này đòi hỏi phải hiểu cách diễn giải phân tích hồi quy 
(Kiến thức). 
Số đơn đặt hàng
Đánh chặn
Khối lượng bán hàng
người mẫu
hệ số
Phòng mua hàng Chi phí dự kiến
$180,01
$ (994,57)
$1,19
Biến
Giá trị
12
1
2.200
3.786,66 USD
Dự đoán
2.160,15 USD
$ (994,57)
2.621,08 USD
MINH HỌA 8.31 Dự đoán 
Ví dụ mẫu
Cộng tích của từng hệ số biến độc lập và giá trị dự đoán của từng biến 
để ngăn chặn dự đoán tổng chi phí bộ phận mua hàng là 3.786,66 USD trong năm.
Mô hình có thể được hiểu như thế này:
• Phần chặn: Phần chặn không có ý nghĩa thực tế. Đó là kết quả của mô hình 
đại diện cho giá trị trung bình của phản hồi khi tất cả các biến độc lập đều bằng 0. Nó 
là nơi hàm phương trình đi qua trục y. 
• Số lượng Đơn đặt hàng: Mỗi đơn đặt hàng cộng thêm $180,01 vào tổng chi phí.
• Doanh số bán hàng: Với mỗi chiếc xe tay ga được bán thêm, chi phí bộ phận mua hàng sẽ tăng thêm 
$1,19.
Sử dụng mô hình như trong Hình minh họa 8.31 giúp doanh nghiệp dự đoán kết quả trong tương lai. các 
kết hợp việc đánh giá các biến có trong mô hình để xem liệu chúng có ý nghĩa và 
thì việc đánh giá số liệu thống kê của mô hình hồi quy sẽ giúp xác định xem mô hình có hợp lệ hay không 
và đáng tin cậy. 
MINH HỌA 8.30 Hồi quy 
Ví dụ mẫu
Số đơn đặt hàng
Đánh chặn
Khối lượng bán hàng
hệ số
180.0127
−994.572
1.1914012
Lỗi chuẩn
31.32217805
877.1183137
0.351035522
3.393961854
t Thống kê
5.747132382
0,002737
1.05E-05
−1.133908575
giá trị P
0,269612
Mô hình hồi quy phòng mua hàng 
Phân tích theo quy định
Phân tích theo quy định quy định những gì sẽ xảy ra để đạt được kết quả mong muốn. com nhất
Phân tích theo quy định trong kế toán là các mô hình phân tích giả định và tối ưu hóa. các

![ILLUSTRATION 8.31](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.31.png)

8.5  Độ giá trị và độ tin cậy được đánh giá như thế nào trong các phân tích dự đoán và phân tích theo quy định?  8-31
các quy tắc tương tự áp dụng cho các phương pháp phân tích khác cũng được áp dụng ở đây. Phân tích phải hợp lệ 
và đáng tin cậy. Vì mô hình quy định quy định hành động nên điều quan trọng là phải xác minh rằng đầu vào và 
kết quả đầu ra của mô hình là hợp lệ và đáng tin cậy để tránh đưa ra các quyết định kinh doanh sai lầm. 
Một mô hình bảng tính đánh giá những thay đổi về giá trị và giả định ảnh hưởng như thế nào đến 
kết quả được gọi là phân tích what-if. Phân tích giả định là một cách dễ dàng để thay đổi giá trị trong 
bảng tính và tính toán lại kết quả đầu ra.
Các công cụ Excel thường được sử dụng để phân tích điều gì xảy ra nếu bao gồm Trình quản lý Kịch bản và 
Tìm kiếm mục tiêu. (Các mô hình tối ưu hóa được thảo luận trong chương về động lực phân tích dữ liệu 
và mục tiêu.) Bất kể sử dụng công cụ nào, việc đánh giá tính hợp lệ và độ tin cậy của 
đầu ra mô hình là như nhau:
• Hiểu mô hình đang giải quyết vấn đề gì. 
• Xác định xem mô hình có đo lường được những gì nó cần đo lường hay không và trên thực tế, liệu nó có đo lường được không 
đại diện cho mục tiêu (tính hợp lệ). 
• Xem xét các thước đo mô hình để xác nhận tính chính xác và nhất quán (độ tin cậy).
Phân tích What-If: Trình quản lý kịch bản
Hãy xem xét phân tích kịch bản và đánh giá tính hợp lệ và độ tin cậy. Một điệu nhảy quốc tế 
công ty Ballet Nuevo đang biểu diễn ở Atlanta, Georgia. Họ có ba buổi biểu diễn 
đã lên lịch và đang xác định xem họ có nên thêm phần thứ tư hay không. Minh họa 8.32 cung cấp một tổng
mô hình mary.
MINH HỌA 8.32  Mô hình tài chính biểu diễn múa ba lê
ngoại hối
1
B
A
C
Trang 1
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
Ballet Nuevo-Phân tích kịch bản biểu diễn bổ sung
Phí rạp hát
Giá vé
Doanh số bán vé dự kiến
Chi phí nhượng bộ trung bình
mỗi người
Lợi nhuận
Doanh thu nhượng quyền
Doanh thu vé
% lợi nhuận nhượng quyền
Tỷ lệ lợi nhuận
18.000 USD
$ 31.250,00
$ 113.250,00
125.000 USD
$ 50,00
2.500
$ 25,00
50%
80%
Tự động Lưu
Oﬀ
mỗi người
Dự kiến doanh số bán vé và
chi tiêu ưu đãi
(thức ăn và đồ uống) bởi
người giữ vé
Phí rạp hát, dựa trên
về doanh thu bán vé, là chi phí
buộc tội công ty múa ba lê
từ nhà hát. Càng cao
việc bán vé, các
giảm phí rạp hát
Rạp chiếu phim mất 20%
về giá vé và
50% giá trị chiết khấu 
mọi người
Ballet Nuevo tin rằng có ba tình huống có thể xảy ra, được thể hiện trong Hình minh họa 8.33.
Doanh số bán vé dự kiến
Nhượng bộ chi tiêu
2.500
$ 25,00
18.000 USD
4.500
$40,00
10.000 USD
1.500
$10,00
$ 25.000,00
Phí rạp hát
Có khả năng
Mô hình phân tích kịch bản Ballet Nuevo
lạc quan
bi quan
MINH HỌA 8.33  
Buổi biểu diễn Ballet Nuevo 
kịch bản
Phân tích kịch bản được thực hiện bằng Trình quản lý kịch bản trong Microsoft Excel. Cảnh-
nario summary hiển thị kết quả khi các ô B3, B4, B5 (Minh họa 8.32) được đổi thành 
các giá trị được hiển thị trong Hình minh họa 8.33.

![ILLUSTRATION 8.33](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.33.png)

8-32 
Chương 8  Diễn giải kết quả phân tích dữ liệu 
$B$3
Kết quả phân tích kịch bản Ballet Nuevo
$B$4
$B$5
$ 25,00
18.000 USD
$B$13
$ 113.250,00
$40,00
10.000 USD
260.000 USD
$10,00
$ 25.000,00
$ 42.500,00
$ 25,00
18.000 USD
$ 113.250,00
Ô kết quả
Thay đổi ô
2.500
4.500
1.500
2.500
Giá trị hiện tại
Tóm tắt kịch bản
lạc quan
bi quan
Có khả năng
MINH HỌA 8.34  
Phân tích kịch bản Ballet Nuevo
MINH HỌA 8.35  Giá vé và lợi nhuận mục tiêu – Tìm kiếm mục tiêu
ngoại hối
1
B
A
C
D
C
Trang 1
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
Ballet Nuevo ‒ Tìm kiếm mục tiêu lợi nhuận
Doanh số bán vé dự kiến
Chi phí nhượng bộ trung bình
Phí rạp hát
Doanh thu nhượng quyền
Lợi nhuận
Doanh thu vé
Giá vé
% lợi nhuận nhượng quyền
Tỷ lệ lợi nhuận
2.500
mọi người
Mỗi người
Mỗi người
$ 25,00
18.000 USD
125.000 USD
$ 31.250,00
$ 113.250,00
$ 50,00
50%
80%
Tự động Lưu
Oﬀ
được rồi
Hủy bỏ
Tìm kiếm mục tiêu
Đặt ô:
$B$13
Để giá trị:
150000
Bằng cách thay đổi ô:
$B$6
?
Cách giải thích của phân tích này là ngay cả trong kịch bản bi quan Ballet Nuevo 
sẽ kiếm được lợi nhuận trên một hiệu suất bổ sung. 
Làm thế nào để chúng ta biết phân tích này là hợp lệ và đáng tin cậy? Ballet Nuevo muốn đánh giá sự khác biệt-
các kịch bản bán vé và ưu đãi để xác định xem liệu chúng có nên bổ sung thêm một buổi biểu diễn hay không. 
Phân tích kịch bản là một phương pháp hợp lệ để sử dụng cho loại phân tích này và mô hình này đại diện cho ba 
những khả năng thực tế. Về độ tin cậy của mô hình, điều đó có thể được xác nhận bằng cách xác minh lợi nhuận 
tính toán là chính xác và các giả định là thực tế (giá vé, mua hàng giảm giá, và 
chi phí rạp hát). Nếu dữ liệu đầu vào của mô hình chính xác và nhất quán thì mô hình đó đáng tin cậy. 
Phân tích What-If: Tìm kiếm mục tiêu
Một công cụ khác để thực hiện phân tích giả định là Goal Seek:  
• Tìm kiếm mục tiêu được sử dụng nếu kết quả mong muốn đã được biết nhưng giá trị đầu vào để đạt được kết quả đó 
kết quả là không. 
• Mục tiêu Tìm kiếm bị hạn chế vì nó chỉ có thể sử dụng một biến đầu vào. Nếu việc phân tích được thực hiện theo
được hình thành đòi hỏi nhiều hơn một biến để thay đổi, sau đó một mô hình tối ưu hóa sử dụng 
Excel Solver sẽ là cần thiết.
Trong ví dụ trước, Ballet Nuevo muốn phân tích so sánh các loại vé khác nhau và 
kịch bản bán hàng nhượng quyền để xác định xem họ có nên thêm một buổi biểu diễn hay không. Điều gì sẽ xảy ra nếu một phần bổ sung
buổi biểu diễn không thể thực hiện được do rạp hát còn trống, và thay vào đó, Ballet Nuevo phải 
xem xét làm thế nào để đặt giá vé để đạt được lợi nhuận mục tiêu cụ thể? 
• Ballet Nuevo đã xác định họ cần lợi nhuận 150.000 USD từ buổi biểu diễn của mình. 
• Hiện tại giá vé là $50 và họ dự đoán sẽ có 2.500 vé được bán dựa trên số liệu cuối cùng 
buổi biểu diễn của năm 
Hình minh họa 8.35 hiển thị thông tin tài chính của Ballet Nuevo và hộp Goal Seek 
xuất hiện sau khi nhấp vào tab Dữ liệu trong Excel và chọn Phân tích What-If và Tìm kiếm mục tiêu. 
Kết quả phân tích được thể hiện ở Hình minh họa 8.34.

![ILLUSTRATION 8.35](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.35.png)

8.5  Độ giá trị và độ tin cậy được đánh giá như thế nào trong các phân tích dự đoán và phân tích theo quy định?  8-33
• Ô Set thể hiện phép tính lợi nhuận tại ô B13 trong bảng tính Excel. 
• Hãy chú ý số tiền lãi hiện tại là $113,250. Lợi nhuận mong muốn là 150.000 USD, do đó giá trị đó 
đã được nhập vào hộp giá trị To. 
• Biến đang được thao tác là giá vé, do đó ô tham chiếu giá vé 
(B6) đã được nhập vào hộp Bằng cách thay đổi ô.
Sau khi người dùng nhấn OK, Excel sẽ tính giá vé cần thiết để đáp ứng lợi nhuận 
mục tiêu 150.000 USD. Hình minh họa 8.36 là giải pháp được tạo ra bởi Excel. Để đạt được mục tiêu lợi nhuận 
với giá 150.000 USD, Ballet Nuevo phải tính phí 68,38 USD mỗi vé. 
Để đánh giá độ tin cậy và giá trị của mô hình tìm kiếm mục tiêu, hãy xác định xem mô hình đó có phù hợp không?
đảm bảo những gì nó cần đo lường (độ tin cậy) và liệu nó có đại diện cho thực tế của câu hỏi hay không
ý nghĩa/mục tiêu (tính hợp lệ):  
• Trong mô hình này, xác nhận việc tính toán lợi nhuận là chính xác. 
• Ngoài ra, hãy xác định xem mô hình có trả lời được câu hỏi Ballet Nuevo giá bao nhiêu không 
nên tính phí trên mỗi vé để đạt được lợi nhuận 150.000 USD và nếu vé đề xuất của người mẫu 
giá là thực tế. Nếu 68,38 USD là không thực tế cho một vé xem buổi biểu diễn thì Ballet Nuevo 
phải xem xét những cách khác để đạt được mục tiêu lợi nhuận. 
MINH HỌA 8.36  Giá vé 
và Lợi nhuận mục tiêu – Tìm kiếm mục tiêu 
Giải pháp
ngoại hối
1
B
A
C
Trang 1
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
Ballet Nuevo ‒ Tìm kiếm mục tiêu lợi nhuận
Doanh số bán vé dự kiến
Chi phí nhượng bộ trung bình
Phí rạp hát
Doanh thu nhượng quyền
Lợi nhuận
Doanh thu vé
Giá vé
% lợi nhuận nhượng quyền
Tỷ lệ lợi nhuận
2.500
mọi người
Mỗi người
Mỗi người
$ 25,00
18.000 USD
170.937,50 USD
$ 31.250,00
150.000 USD
$68,38
50%
80%
Tự động Lưu
Oﬀ
ÁP DỤNG TƯ DUY PHIẾU 8.5: Diễn giải theo quy tắc 
Phân tích
Sử dụng các yếu tố của tư duy phê phán khi diễn giải một mô hình quy định:  
• Biết ai sẽ sử dụng dự đoán giúp xác định xem mô hình có giải quyết được mối quan ngại và vấn đề của họ hay không
chắc chắn rằng nó đại diện cho thực tế (Các bên liên quan). 
• Cần phải hiểu lý do tại sao việc phân tích được thực hiện để đánh giá xem liệu biến thể có
có thể có ý nghĩa (Mục đích). 
• Biết cách diễn giải các phân tích hồi quy và đánh giá các mô hình tối ưu hóa là cần thiết để 
giải thích chúng (Kiến thức).

![ILLUSTRATION 8.36](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.36.png)