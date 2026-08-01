7-0
 C H A PT E R 7 
Phân tích: Dữ liệu 
Thăm dò 
 Xem trước chương 
 Cho đến nay trong giai đoạn phân tích của quá trình phân tích dữ liệu, bạn đã chuẩn bị dữ liệu, hoàn thành 
mô hình hóa thông tin và tạo ra một cơ sở dữ liệu phân tích. Bây giờ là lúc khám phá dữ liệu 
và thu thập những hiểu biết sâu sắc. Bước này điều tra dữ liệu để phát hiện những điểm bất thường, các mẫu mới và bất kỳ-
điều có thể cải thiện việc ra quyết định. Chương này sẽ giúp bạn phát triển những kỹ năng cần thiết 
để khám phá dữ liệu thành công, đó là một quá trình bao gồm việc đặt những câu hỏi phù hợp và 
xác định và khám phá các mối quan hệ dữ liệu để tìm ra những hiểu biết sâu sắc. Các mẫu được trình bày trong này 
chương này sẽ giúp bạn khám phá một cách hiệu quả và hiệu quả các tập dữ liệu bạn sẽ làm việc trong 
sự nghiệp của bạn. 
dữ liệu
Chuẩn bị 
Thông tin
Làm người mẫu
dữ liệu
Thăm dò 
Phân tích
Kế hoạch
Báo cáo
Giai đoạn 2
Giai đoạn 3
Giai đoạn 1
Phiên dịch
giao tiếp
Phân tích
Chiến lược
Mục tiêu
Động lực
Khám phá thông tin chi tiết
thích hợp cho
ra quyết định
Xác định và
tính toán
có liên quan
thông tin
Phát hiện và
dữ liệu chính xác
vấn đề

Cái nhìn sâu sắc chuyên nghiệp: Tại sao bạn nên biết cách khám phá dữ liệu?
Sau khi lấy bằng thạc sĩ kế toán, Yuqi gia nhập bộ phận phân tích dữ liệu của một công ty lớn. 
tổ chức tài chính.
Quá trình chuyển đổi sang nơi làm việc của tôi không phải là không có thách thức. Ở trường tôi được cho 
những vấn đề phức tạp mà tôi phải tìm ra những giải pháp tinh tế và tôi thực sự rất xuất sắc 
lúc đó. Tuy nhiên, khi tôi bắt đầu công việc của mình, không có câu hỏi nào được xác định rõ ràng. 
Ví dụ: nhóm dữ liệu tài chính liên tục yêu cầu chúng tôi cung cấp thông tin chi tiết mới. Điều gì có thể 
bạn nói với chúng tôi rằng chúng tôi chưa biết? Vì vậy, tôi cần học thêm các kỹ năng—đặc biệt là 
thăm dò dữ liệu. Tôi bắt đầu xem xét các tập dữ liệu từ nhiều góc độ khác nhau 
có thể. Tôi xem xét các xu hướng, sự phân bổ, nhóm dữ liệu theo những cách chưa ai làm được 
trước đây, tương quan với tất cả các loại biến số, tìm kiếm các giá trị ngoại lệ, v.v. Tôi phát triển-
đã vận hành một bộ kỹ năng khám phá dữ liệu độc đáo và trở nên giỏi về nó. Thành thật mà nói, tôi cảm thấy như mình 
đã trở thành một nhà nghiên cứu dữ liệu. Điều gì tiếp theo cho tôi? Sau khi làm điều này gần mười 
năm nữa, tôi dự định lấy bằng Tiến sĩ về khoa học dữ liệu.
Lộ trình chương
MỤC TIÊU HỌC TẬP
CHỦ ĐỀ
ÁP DỤNG NÓ
 LO 7.1  Mô tả quy trình  
của việc khám phá dữ liệu.
• Quá trình khám phá dữ liệu
• Khám phá dữ liệu bằng PivotTable
• Khám phá dữ liệu trên các công cụ
Khám phá dữ liệu với 
PivotTable
(Ví dụ: Quản lý 
Kế toán)
 LO 7.2  Khám phá nền tảng 
mối quan hệ dữ liệu thông qua 
trực quan hóa.
• Tám mô hình khám phá dữ liệu cơ bản 
Mối quan hệ
Hình dung từng phần thành toàn bộ 
Mối quan hệ với Excel
(Ví dụ: Quản lý 
Kế toán)
 LO 7.3  Khám phá dữ liệu bằng 
tích hợp nền tảng 
các mối quan hệ.
• Hai mẫu sử dụng một hình ảnh duy nhất
• Báo cáo sử dụng nhiều hình ảnh trực quan
Xây dựng một tương tác 
Báo cáo 
(Ví dụ: Quản lý 
Kế toán)
Dữ liệu   Thẻ Dữ liệu xuất hiện trong chương khi dữ liệu cho một ví dụ, hình minh họa hoặc ứng dụng được  
có sẵn trên nền tảng học tập trực tuyến của Wiley.
Phần mềm phân tích dữ liệu liên tục thay đổi và có thể có nhiều phiên bản phần mềm mới hơn.
được đưa ra trong chương này. Để biết thêm thông tin, hãy truy cập video đi kèm trên nền tảng học tập trực tuyến của Wiley. 
7.1  Khám phá dữ liệu là gì?
MỤC TIÊU HỌC TẬP ➊
Mô tả quá trình khám phá dữ liệu.
Trong chương về lập mô hình thông tin, bạn đã học cách thêm thông tin hữu ích cho 
phân tích vào cơ sở dữ liệu phân tích. Bây giờ bạn đã sẵn sàng để bắt đầu khám phá dữ liệu. Khám phá dữ liệu-
phân tích dữ liệu mang tính thăm dò, là quá trình khám phá nhằm tìm kiếm điều gì đó mới mẻ 
và trước đây chưa được biết đến. Điều này được thực hiện bằng cách tìm kiếm các mẫu, các giá trị ngoại lệ hoặc hơn thế nữa 
7.1  Khám phá dữ liệu là gì?  7-1

7-2  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
nói chung, để hiểu biết sâu sắc. Cái nhìn sâu sắc là một quan sát có thể ảnh hưởng đáng kể đến doanh nghiệp ' 
ra quyết định. Hãy nhớ rằng, các quyết định không dựa trên dữ liệu. Đúng hơn, các quyết định được thông báo 
bởi những hiểu biết sâu sắc được tạo ra từ dữ liệu.
Quá trình tạo ra những hiểu biết sâu sắc này là điểm phân biệt việc phân tích dữ liệu với những công việc đơn giản. 
hành vi báo cáo số Tính toán và trình bày tổng số tiền quyên góp 
mỗi năm đối với một tổ chức phi lợi nhuận đang báo cáo, nhưng nhận ra rằng có sự sụt giảm 
xu hướng quyên góp trong những năm qua và các nhà tài trợ ở các nhóm tuổi khác nhau cư xử khác nhau là 
là kết quả của việc khám phá dữ liệu. Mặc dù họ có thể chia sẻ một số công cụ nhưng điều cần thiết là phải phân biệt 
giữa khám phá dữ liệu, giải thích và báo cáo:
• Thăm dò: Khám phá những hiểu biết sâu sắc.
• Giải thích: Bối cảnh hóa và hiểu biết sâu sắc.
• Báo cáo: Truyền đạt những hiểu biết sâu sắc.
Giải thích và báo cáo được đề cập trong các chương riêng của họ. Bây giờ hãy tóm tắt 
quá trình khám phá dữ liệu.
Quá trình khám phá dữ liệu
Khám phá dữ liệu là một phần không thể thiếu trong công việc của kế toán viên hàng ngày. Họ tìm kiếm những hiểu biết sâu sắc, 
từ việc xác định liệu có những biến động theo mùa trong doanh số bán hàng hay không và liệu những biến động đó có 
ảnh hưởng đến kết quả kinh doanh, đến việc những thay đổi trong chính sách tín dụng ảnh hưởng như thế nào đến doanh số bán hàng và các tài khoản khó thu hồi 
phải thu. Đó là một quá trình gồm bốn bước để xác định các câu hỏi, xác định các mối quan hệ dữ liệu, 
khám phá các mối quan hệ dữ liệu và cuối cùng là tạo ra những hiểu biết sâu sắc (Minh họa 7.1).
MINH HỌA 7.1  Khám phá dữ liệu như một quá trình
Doanh số bán hàng có được cải thiện không?
1.774.263 1.723.765 1.782.692 2.041.879 2.225.138
2021
2022
2023
2024
2025
Xác định 
dữ liệu
Mối quan hệ
Khám phá
dữ liệu
Mối quan hệ
Tạo
Thông tin chi tiết
Xu hướng tăng
bắt đầu từ năm 2023
Xu hướng tăng
bắt đầu từ năm 2023
Chuỗi thời gian
Mô tả một cái gì đó như thế nào 
thay đổi theo thời gian. 
Đồng thời xác định 
mô hình thay đổi 
chẳng hạn như sự tăng trưởng,
biến động, suy giảm. 
Trực quan hóa
2021
0
1.000.000
2.000.000
3.000.000
2022
2023
Năm
2024
2025
2.225.138
2.041.879
1.782.692
1.723.765
1.774.263
Đơn vị đã bán
Thiết kế
Trục
Năm
Truyền thuyết
Thêm trường dữ liệu ở đây
Giá trị
Đơn vị đã bán
Xác định 
Câu hỏi

![ILLUSTRATION 7.1](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.1.png)

7.1  Khám phá dữ liệu là gì?  7-3
Xác định câu hỏi
Khám phá dữ liệu giúp trả lời các câu hỏi kế toán như liệu doanh thu và lợi nhuận có 
cải thiện, sản phẩm nào đáng được đầu tư, nợ xấu có được quản lý hợp lý hay không, và 
nhiều hơn nữa. Cơ sở dữ liệu phân tích phải cung cấp câu trả lời cho cả những vấn đề được dự kiến và không dự đoán trước. 
(không có kế hoạch) câu hỏi. Một khi câu hỏi đã được xác định, chẳng hạn như câu hỏi về việc liệu 
doanh số bán hàng đơn vị đang được cải thiện trong Hình minh họa 7.1 thì các mối quan hệ dữ liệu cơ bản có thể được 
được xác định.
Xác định mối quan hệ dữ liệu
Nếu chúng ta muốn biết liệu doanh số bán hàng có được cải thiện hay không và dữ liệu có sẵn cho thấy có sự thay đổi trong cả hai 
ngân sách tiếp thị và doanh số bán hàng, thì mối quan hệ giữa hai yếu tố đó 
có thể tạo ra những hiểu biết có giá trị. Mối quan hệ dữ liệu mô tả cách các phần tử dữ liệu (hoặc giá trị
ue) có liên quan với nhau. Nhưng trước khi có thể phân tích các khía cạnh của mối quan hệ dữ liệu, họ phải 
được xác định. Stephen few1, một chuyên gia về trực quan hóa dữ liệu, phân biệt tám nền tảng 
mối quan hệ dữ liệu:
• So sánh danh nghĩa
• Phân phối
• Độ lệch
• Xếp hạng
• Một phần đến toàn bộ
• Tương quan
• Chuỗi thời gian
• Không gian địa lý
Mối quan hệ dữ liệu được xác định trong Hình minh họa 7.1 là một chuỗi thời gian, mô tả cách 
một cái gì đó thay đổi theo thời gian và giúp xác định các mô hình thay đổi. Một mối quan hệ có 
được xác định, cho dù đó là mối quan hệ theo chuỗi thời gian hay một trong các mối quan hệ được kiểm tra 
ở phần sau của chương này, đã sẵn sàng để khám phá.
Khám phá mối quan hệ dữ liệu
Mặc dù có nhiều cách tiếp cận khác nhau để khám phá các mối quan hệ dữ liệu, việc trực quan hóa và thống kê
tics là phổ biến nhất. Khám phá bao gồm việc chọn trực quan hóa hoặc trực quan hóa 
phù hợp nhất để khám phá các mối quan hệ dữ liệu. Trong Hình minh họa 7.1, biểu đồ đường trực quan hóa 
chuỗi thời gian.
Hãy nhớ rằng cần có kiến ​​thức về công cụ cụ thể để tạo hình ảnh trực quan. cho 
Ví dụ: phân tích chuỗi thời gian đòi hỏi phải biết cách tạo biểu đồ dạng đường. Kinh doanh 
các phần mềm thông minh như Excel, Power BI và Tableau đều có những công cụ mạnh mẽ để hiển thị
xác định các mối quan hệ dữ liệu để khám phá. Biểu đồ đường trong Hình minh họa 7.1 được thiết kế bằng cách sử dụng 
Điện BI. Trong phần thiết kế của hình minh họa, trường trục đề cập đến đơn vị thời gian được sử dụng cho 
trục x trong biểu đồ và trường giá trị đề cập đến biến được sử dụng cho trục y.
Tạo thông tin chi tiết
Biểu đồ đường trong Hình minh họa 7.1 cho thấy xu hướng tăng doanh số bán căn hộ bắt đầu từ năm 2023. 
Việc khám phá sâu hơn cái nhìn sâu sắc này sẽ bao gồm việc khám phá nguồn gốc của sự tăng trưởng đó và liệu 
xu hướng tăng có thể được giải thích bởi các yếu tố khác. Trên thực tế, việc khám phá dữ liệu là một quá trình liên tục 
quá trình. Thông tin chi tiết tạo ra các câu hỏi mới, sau đó tạo ra nhiều thông tin chi tiết hơn. Những cái này 
các quan sát sau đó được diễn giải và truyền đạt tới các bên liên quan trong giai đoạn cuối của quá trình 
quá trình phân tích dữ liệu.
1Ít, Stephen. (2012). Cho tôi xem các con số: Thiết kế bảng và đồ thị để khai sáng. Đồi El Dorado, 
CA: Nhà xuất bản Analytics.

7-4  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
Khám phá dữ liệu với PivotTable
Khám phá dữ liệu điều tra dữ liệu từ các góc độ khác nhau để thu thập thông tin chi tiết. Một công cụ được sử dụng rộng rãi 
vì đây là PivotTable Excel. Bạn đã học trong chương kỹ năng phân tích dữ liệu cơ bản 
rằng PivotTable có thể nhanh chóng sắp xếp lại dữ liệu để giúp trả lời các câu hỏi kinh doanh quan trọng. 
Ở đây, chúng tôi minh họa các yếu tố chính của việc khám phá dữ liệu bằng cách sử dụng PivotTable.
Dữ liệu Bộ dữ liệu trong Hình minh họa 7.2 (A) tóm tắt doanh số bán hàng của Honda Motors North 
Châu Mỹ (HNA) trong giai đoạn 2021–2025 trong bảng tổng hợp chéo.2 Minh họa 7.2 (B) cho thấy 
dữ liệu giống như một bảng phẳng.3 Hãy nhớ lại rằng đối với phân tích dữ liệu, các bảng phẳng được ưa thích hơn các bảng chéo
bảng lập bảng vì tiêu đề cột trong bảng phẳng không chứa giá trị dữ liệu hữu ích 
cho mục đích phân tích. Bảng phẳng trong Hình minh họa 7.2 (B) sẽ được sử dụng để xây dựng PivotTable.
ÁP DỤNG TƯ duy phản biện 7.1: Suy nghĩ chín chắn trong quá trình 
Khám phá dữ liệu
Tư duy phản biện là một phần không thể thiếu trong quá trình khám phá dữ liệu:
• Khám phá đòi hỏi sự hiểu biết sâu sắc về các mối quan hệ dữ liệu, cách chúng được trình bày và 
những hiểu biết sâu sắc mà họ có thể tạo ra. Ví dụ: nhiều hình ảnh trực quan có thể trình bày và khám phá 
chuỗi thời gian, bao gồm biểu đồ vùng, biểu đồ cột, biểu đồ đường, biểu đồ thu nhỏ và thác nước 
biểu đồ. Bạn phải biết nên sử dụng biểu đồ nào khi nào. Khi khám phá chuỗi thời gian, bạn đang tìm kiếm 
cho các xu hướng, chu kỳ và sự bất thường (Kiến thức).
• Khám phá dữ liệu thường dựa trên mẫu. Bạn sẽ tìm kiếm những khuôn mẫu và cấu trúc mà bạn có
được khắc phục trước đây và phát triển hơn nữa mà bạn có thể tận dụng trong các phân tích trong tương lai. Một ví dụ là 
phá vỡ các xu hướng để hiểu rõ hơn lý do thay đổi. Nếu có xu hướng tăng 
về số lượng bán ra, điều này có đúng với tất cả sản phẩm và khu vực (Tự phản ánh) không?
2Tập dữ liệu là hư cấu.
3Minh họa 7.2 (A) hiển thị tập dữ liệu đầy đủ. Hình minh họa 7.2 (B) hiển thị một phần tập dữ liệu; 10 hàng đầu tiên của 
bàn phẳng.
MINH HỌA 7.2  Bộ dữ liệu HNA
Quốc gia
dân sự
dân sự
hiệp định
CR-V
Phi công
hiệp định
CR-V
Phi công
Odyssey
Đường sườn núi
Hoa Kỳ
Canada
Canada
Canada
Canada
Canada
Canada
Odyssey
Đường sườn núi
Xe tải nhỏ
xe tải
320981
243192
175883
140444
188664
58322
230887
195232
135423
40998
25229
19008
301882
245998
160886 190001
142980
167123
55897
56889
242998
200872
129809 126592
35672
39811
7761
31887
292331
231441
139441
150872
275667
210665
26981
42001
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
Hoa Kỳ
người mẫu
xe sedan
xe sedan
xe sedan
SUV
SUV
xe sedan
SUV
SUV
Xe tải nhỏ
xe tải
Loại
2021
2022
2023
220877
55899
114119
43125
291002
309885
142917
150881
381998
253988
22099
55089
2024
252019
54891
98077
47329
255423
344771
125090
139009
480871
319755
19822
88081
2025
   
Quốc gia
hiệp định
dân sự
dân sự
dân sự
dân sự
hiệp định
hiệp định
hiệp định
hiệp định
dân sự
Canada
Canada
Canada
Canada
Canada
2021
2022
2023
2024
2025
2021
2022
2023
2024
2025
195232
200872
210665
253988
319755
230887
242998
275667
381998
480871
Canada
Canada
Canada
Canada
Canada
người mẫu
xe sedan
xe sedan
xe sedan
xe sedan
xe sedan
xe sedan
xe sedan
xe sedan
xe sedan
xe sedan
Loại
Năm
Đơn vị đã bán
  	
(A) Cấu trúc bảng chéo của tập dữ liệu HNA	
(B) Cấu trúc phẳng của tập dữ liệu HNA
Hình minh họa 7.3 (A) là một PivotTable được tạo bằng Excel sử dụng tập dữ liệu HNA. Nó liệt kê 
Các mẫu xe của HNA theo thứ tự giảm dần về tổng số chiếc đã bán. Hình minh họa 7.3 (B) cho thấy cách 
PivotTable trong bảng A được tạo bằng hộp thoại Trường PivotTable, đây là công cụ của Excel 
để xác định nội dung của PivotTable.

![ILLUSTRATION 7.3](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.3.png)

7.1  Khám phá dữ liệu là gì?  7-5
Năm thành phần được sử dụng để khám phá dữ liệu với PivotTable là trường, giá trị, hàng, 
cột và bộ lọc (Minh họa 7.3 (B)).
Trường
Khu vực Trường liệt kê tất cả các thành phần dữ liệu có sẵn cho mục đích khám phá. Chúng có thể được kéo 
và chuyển sang các khu vực khác để xây dựng mối quan hệ dữ liệu và lọc dữ liệu. Trong hình minh họa 7.3, 
Các trường Model và UnitsSold được sử dụng để khám phá.
Giá trị
Vùng Giá trị trong Hình minh họa 7.3 (B) biểu thị số hoặc các số cần phân tích. Nó có thể 
được sử dụng để khám phá dữ liệu theo những cách khác nhau:
• Kéo và thả bất kỳ trường nào vào vùng Giá trị và áp dụng các phép toán như 
trung bình, đếm hoặc tính tổng của nó.
• Tạo các trường tính toán.
Ví dụ về các giá trị liên quan đến kế toán có thể được phân tích bao gồm tổng doanh thu, doanh thu thuần
enue, thuế, chi phí, lợi nhuận, v.v. Đối với HNA, các giá trị trong trường UnitsSold được tính tổng, 
tạo ra tổng số căn bán được trong giai đoạn 2021–2025.
Hàng và Cột
Trong Hình minh họa 7.3 (B), trường Model đã được kéo vào khu vực Rows nên bảng sẽ 
tính toán và hiển thị tổng số đơn vị được bán cho mỗi mô hình. Cột TotalUnitsSold trong Hình minh họa 
7.3 (A) sau đó có thể được sắp xếp và định dạng.
Khi trường Quốc gia được thêm vào khu vực Cột trong Hình minh họa 7.3 (B), kết quả 
bảng chéo (Minh họa 7.4) cho thấy tổng số đơn vị bán được trên mỗi mẫu, được biểu thị bằng 
các hàng và mỗi quốc gia, được biểu thị bằng các cột.
  Tổng số đơn vị đã bán
Odyssey
CR-V
hiệp định
Đường sườn núi
Phi công
dân sự
3.074.040
2.555.799
1.603.686
898.441
897.807
517.964
9.547.737
Người mẫu
Tổng số đơn vị đã bán
         
Trường PivotTable
Chọn các trường để thêm vào báo cáo:
Quốc gia
người mẫu
Loại
Năm
Đơn vị đã bán
Thêm bàn..
Kéo các trường giữa các khu vực bên dưới:
Bộ lọc
Cột
Tìm kiếm
Hàng
Trì hoãn cập nhật bố cục
Giá trị
∑
người mẫu
Tổng số đơn vị đã bán
cập nhật
  (A) PivotTable: Tổng số đơn vị được bán trên mỗi mô hình4	
   (B) Tạo PivotTable
4Một số định dạng nhỏ đã được áp dụng.
MINH HỌA 7.3  Excel 
PivotTable và PivotTable 
Hộp thoại

![ILLUSTRATION 7.4](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.4.png)