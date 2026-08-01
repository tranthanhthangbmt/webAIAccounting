5-0
 C H A PT E R 5 
 Phân tích: Dữ liệu 
Chuẩn bị 
 Xem trước chương 
 Cho đến giờ trong khóa học này, bạn đã học cách lập kế hoạch cho một dự án phân tích dữ liệu bằng cách trình bày rõ những gì 
thúc đẩy nó, xác định các mục tiêu của nó và thiết kế một chiến lược để hoàn thành nó một cách thành công. 
Bây giờ kế hoạch đã sẵn sàng, đã đến lúc chuyển sang giai đoạn phân tích dữ liệu. Có ba 
nhiệm vụ trong giai đoạn này: chuẩn bị dữ liệu, xây dựng mô hình thông tin và khám phá dữ liệu. 
Ở đây, chúng ta sẽ tập trung vào nhiệm vụ đầu tiên là chuẩn bị dữ liệu để phân tích. Việc chuẩn bị dữ liệu có thể 
hoạt động tốn nhiều thời gian nhất trong dự án phân tích dữ liệu. Bạn có thể chi tiêu hơn 75% số tiền 
tổng thời gian làm việc của dự án cho riêng nhiệm vụ này! Nhưng có lý do chính đáng cho việc này, vì việc chuẩn bị dữ liệu
hoạt động bao gồm nhiều hoạt động. Có hai yếu tố chính cần lưu ý khi chuẩn bị dữ liệu 
để phân tích:
 1. Chất lượng dữ liệu sẽ ảnh hưởng đến chất lượng của những hiểu biết sâu sắc và các quyết định dựa trên 
họ. Nói cách khác, dữ liệu xấu dẫn đến những quyết định sai lầm. 
 2. Cấu trúc của dữ liệu sẽ quyết định mức độ hiệu quả của chúng được phân tích.  
 Đầu tiên, chúng ta khám phá chi tiết hai quy trình chuẩn bị dữ liệu chính. Tiếp theo chương trình bày 
hai mươi mẫu trích xuất, chuyển đổi và tải dữ liệu mà bạn có thể sử dụng để chuẩn bị dữ liệu cho 
phân tích. 
Phân tích
kế hoạch
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
Phát hiện và sửa
vấn đề dữ liệu
Xác định và
tính toán 
có liên quan
thông tin
Khám phá thông tin chi tiết
thích hợp cho
ra quyết định
dữ liệu
Chuẩn bị 
Thông tin
Làm người mẫu
dữ liệu
Thăm dò

Chương Lộ trình  5-1
Cái nhìn sâu sắc chuyên nghiệp: Làm thế nào bạn có thể tiếp cận những thách thức của 
Chuẩn bị dữ liệu?
Bill là giám đốc bộ phận phân tích dữ liệu kiểm toán tại một trong những công ty kế toán công lớn.
Sau khi tốt nghiệp với bằng kế toán, tôi dần dần chuyển sang lĩnh vực phân tích dữ liệu của chúng tôi 
luyện tập. Tôi thích cách kế toán và công nghệ kết hợp với nhau trong hoạt động kiểm toán của chúng tôi-
và luôn có những cơ hội cũng như thách thức mới để giải quyết.
Một thách thức chính khi làm việc với dữ liệu tại một công ty kế toán công là khách hàng của chúng tôi 
có đủ hình dạng và kích cỡ, với các hệ thống ERP khác nhau, từ các hệ thống độc quyền truyền thống
hướng tới các hệ thống tích hợp dựa trên đám mây ngày càng hiện đại với các tính năng phức tạp 
khả năng báo cáo và phân tích. Điều này có nghĩa là độ sạch, chất lượng, hạt
độ trễ, khối lượng và cấu trúc của dữ liệu có thể thay đổi đáng kể. Điều này làm tăng 
tầm quan trọng của các giải pháp ETL (Extract-Transform-Load) để giúp các chuyên gia của chúng tôi 
trích xuất dữ liệu một cách hiệu quả từ hệ thống máy khách, chuyển đổi dữ liệu đó thành một dữ liệu chung 
định dạng và cuối cùng tải dữ liệu vào nền tảng phân tích của chúng tôi.
Để thành công, các chuyên gia dữ liệu tại công ty của tôi phải có khả năng hiểu và 
đánh giá dữ liệu của khách hàng để đảm bảo rằng chúng phù hợp và đáng tin cậy. Điều này bao gồm 
biết cách trò chuyện phù hợp với khách hàng, thường bao gồm cả việc đại diện
người gửi từ bộ phận CNTT của khách hàng và các chuyên gia trích xuất dữ liệu nội bộ của chúng tôi, 
để truyền đạt hiệu quả các yêu cầu dữ liệu của chúng tôi. Những kỹ năng bạn đang xây dựng 
trong chương này đều rất phù hợp với sự nghiệp thành công của nhà phân tích dữ liệu trong thời đại ngày nay. 
nghề kế toán công.
Lộ trình chương
MỤC TIÊU HỌC TẬP
CHỦ ĐỀ
ÁP DỤNG NÓ
 LO 5.1   Giải thích quy trình 
hồ sơ dữ liệu.
• Điều tra chất lượng dữ liệu
• Khảo sát cấu trúc dữ liệu
• Quyết định và thông báo
Xác định các vấn đề về chất lượng dữ liệu
 LO 5.2   Mô tả quá trình chiết xuất-
quá trình tải biến đổi (ETL).
• Trích xuất dữ liệu
• Chuyển đổi dữ liệu
• Tải dữ liệu
Kết hợp các bảng để phân tích
 LO 5.3   Áp dụng các mẫu để trích xuất 
dữ liệu.
• Hai mẫu trích xuất dữ liệu
Trích xuất dữ liệu bằng mẫu
 LO 5.4   Áp dụng các mẫu cho 
chuyển đổi cột
• Mẫu chuyển đổi tám cột
Sử dụng chuyển đổi cột 
mẫu
 LO 5.5   Áp dụng các mẫu cho 
chuyển đổi các bảng.
• Bốn mẫu chuyển đổi bảng
Chuyển đổi bảng với 
mẫu
 LO 5.6   Áp dụng các mẫu cho 
chuyển đổi các mô hình.
• Ba mô hình chuyển đổi mô hình
Vẽ sơ đồ sao
 LO 5.7   Áp dụng mẫu cho dữ liệu 
vấn đề tải.
• Ba kiểu tải dữ liệu
Đánh giá mối quan hệ 
Giữa các bàn
Dữ liệu   Thẻ Dữ liệu xuất hiện trong chương khi dữ liệu cho một ví dụ, hình minh họa hoặc ứng dụng được  
có sẵn trên nền tảng học tập trực tuyến của Wiley.
Phần mềm phân tích dữ liệu liên tục thay đổi và có thể có nhiều phiên bản phần mềm mới hơn.
được đưa ra trong chương này. Để biết thêm thông tin, hãy truy cập video đi kèm trên nền tảng học tập trực tuyến của Wiley.

5-2  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
5.1  Lập hồ sơ dữ liệu là gì?
MỤC TIÊU HỌC TẬP ➊
Giải thích quá trình lập hồ sơ dữ liệu.
Doanh nghiệp mất hàng tỷ USD mỗi năm do dữ liệu bẩn hoặc dữ liệu cung cấp không chính xác 
hoặc mô tả không đầy đủ về hoạt động kinh tế của một doanh nghiệp. Sử dụng dữ liệu bẩn có thể dẫn đến 
các vấn đề khác nhau, từ việc định giá không chính xác đến việc gửi hóa đơn tới nhầm khách hàng (hoặc không thu tiền 
chúng), đến mức không thể phát hiện gian lận. Chuẩn bị dữ liệu giúp tránh những vấn đề này và hơn thế nữa.
Chuẩn bị dữ liệu là quá trình lập hồ sơ, làm sạch, tái cấu trúc và tích hợp dữ liệu 
trước khi xử lý và phân tích. Nó giúp đảm bảo dữ liệu chất lượng cao và do đó cải thiện 
ra quyết định. Hồ sơ dữ liệu là quá trình điều tra chất lượng và cấu trúc dữ liệu. Nó 
có ba phần:
	 1. Điều tra chất lượng dữ liệu: Tìm kiếm những điểm bất thường trong dữ liệu. Tức là dữ liệu có bị bẩn không?
	 2. Điều tra cấu trúc dữ liệu: Tìm cách tốt nhất để sắp xếp dữ liệu và cải thiện 
phân tích.
	 3. Quyết định và thông báo: Đưa ra quyết định về việc liệu có thể giải quyết được vấn đề hay không 
các vấn đề đã được xác định, chi phí để thực hiện việc đó là bao nhiêu và xem xét những hậu quả có thể xảy ra.
sẽ mất đi nếu vấn đề không được giải quyết.
Các quyết định được đưa ra trong giai đoạn cuối sẽ hướng dẫn quá trình trích xuất, chuyển đổi, tải (ETL) bằng cách 
xác định những gì cần phải thay đổi. Như Minh họa 5.1. cho thấy, việc chuẩn bị dữ liệu là một công việc liên tục
sự hợp tác giữa quá trình lập hồ sơ dữ liệu, là chủ đề của cuộc thảo luận này, 
và quy trình ETL, sẽ được đề cập tiếp theo. Hiện tại, hãy nhớ rằng việc lập hồ sơ dữ liệu sẽ phát hiện 
vấn đề về dữ liệu và ETL sửa chúng.
MINH HỌA 5.1  Dữ liệu 
Quá trình chuẩn bị
Quá trình chuẩn bị dữ liệu
Trích xuất-Chuyển đổi-Tải
Hồ sơ dữ liệu
Chất lượng dữ liệu
Cấu trúc dữ liệu
Thông báo
đúng
Phát hiện
Điều tra chất lượng dữ liệu
Khi thảo luận về “chất lượng” của dữ liệu mà chúng tôi làm việc cùng, chúng tôi đang đề cập đến tính phù hợp 
của việc sử dụng dữ liệu để ra quyết định. Đánh giá chất lượng dữ liệu xác định các giá trị thiếu sót trong 
tập dữ liệu, cho biết liệu có dữ liệu nào cần phải được làm sạch hay không. Có nhiều phương pháp khác nhau để 
đang làm điều này:
• Phương pháp dựa trên quy tắc là cách tiếp cận từ trên xuống. Một mối quan hệ hoặc quy tắc logic được xác định 
giữa các dữ liệu và được kiểm tra để xác định xem dữ liệu có phù hợp với nó hay không. Số quy định đó 
có thể được chỉ định là gần như không giới hạn. Ví dụ bao gồm:
•  Phân chia nhiệm vụ.
•  Số lượng hiện có không thể âm.
•  Người dưới 16 tuổi không được phép thuê ô tô.
•  Việc bán hàng chỉ có thể được thực hiện khi có đơn hàng hợp lệ.
• Phương pháp thăm dò và suy luận là phương pháp tiếp cận từ dưới lên. Mục tiêu là tìm 
những bất thường bằng cách kiểm tra dữ liệu từ nhiều khía cạnh khác nhau. Sắp xếp, tần suất

![ILLUSTRATION 5.1](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.1.png)

5.1  Lập hồ sơ dữ liệu là gì?  5-3
phân phối và phân tích ngoại lệ là những ví dụ về các kỹ thuật mạnh mẽ để khám phá 
mục đích. Cách tiếp cận từ dưới lên thứ hai, suy luận, là một phương pháp dựa trên máy tính 
thuật toán để xác định sự bất thường.
Các phương pháp khác nhau này xác định sự bất thường của dữ liệu, xảy ra khi dữ liệu không đáp ứng được yêu cầu. 
kỳ vọng về tính chính xác, giá trị, tính nhất quán và đầy đủ.
Tính đúng đắn
Dữ liệu mô tả sự thật về các thực thể, chẳng hạn như tên khách hàng, giá sản phẩm hoặc 
ngày của một giao dịch. Dữ liệu không chính xác khi giá trị được gán cho ký tự của thực thể-
istic là sai. Ví dụ: một khách hàng có thể sống ở New Jersey (NJ), nhưng New York (NY) lại là 
thay vào đó được ghi lại hoặc giá của sản phẩm là $252 nhưng được liệt kê là $225.
Dữ liệu không chính xác là điều phổ biến, như những ví dụ thực tế về trục trặc dữ liệu này cho thấy. Đối với 
doanh nghiệp có liên quan, lỗi dữ liệu có thể nghiêm trọng:
• Delta Airlines bán vé máy bay khứ hồi từ lục địa Mỹ tới Hawaii với giá chưa đến 7 USD. 
Trong một ví dụ tương tự, một khách hàng của United Airlines có thể mua vé khứ hồi hạng nhất.
vé chuyến đi từ Mỹ tới Hồng Kông chỉ với bảy dặm dành cho khách hàng thường xuyên.
• Một khách hàng đặt phòng khách sạn sang trọng ở Pasadena, California với giá 10 USD một đêm.
• Walmart bán máy chạy bộ với giá dưới 35 USD.
Có một số cách để phát hiện những lỗi như vậy. Khi định giá không chính xác, chẳng hạn như khi
vé máy bay đắt tiền được giảm giá sâu do có sai sót, sau đó giá tăng đột ngột 
nhu cầu có thể là một dấu hiệu của một vấn đề. Các kỹ thuật lập hồ sơ, chẳng hạn như khám phá các ngoại lệ, 
cũng có thể hữu ích. Dù thế nào đi nữa, hãy luôn suy nghĩ chín chắn về dữ liệu được phân tích và theo dõi. 
đối với những bất thường.
ÁP DỤNG TƯ duy phản biện 5.1: Đánh giá chất lượng dữ liệu
Việc sử dụng dữ liệu hợp lý sẽ loại bỏ những thành kiến và phỏng đoán trong quá trình ra quyết định. Sử dụng dữ liệu kém trong 
quá trình này làm tăng rủi ro. Vì vậy, điều quan trọng là phải đánh giá rủi ro liên quan đến dữ liệu kém hoàn hảo. 
Có hai đặc điểm cần xem xét (Rủi ro):
• Độ tin cậy: Dữ liệu được trích xuất từ hệ thống hoạch định nguồn lực doanh nghiệp (ERP) đã được 
chịu hàng trăm kiểm soát nội bộ đáng tin cậy hơn dữ liệu cảm tính được trích xuất 
từ Facebook.
• Tác động: Tương tự, tác động của việc tung ra dòng sản phẩm mới lớn hơn nhiều so với quyết định 
để đầu tư vào danh thiếp mới.
Tác động càng cao thì bạn càng sẵn sàng đầu tư vào việc cải thiện độ tin cậy của dữ liệu.
Đánh giá độ tin cậy và tác động của dữ liệu
Quyết định
tác động
Độ tin cậy của dữ liệu
Thấp
Cao
nhỏ
lớn
hiệu lực
Một phần không thể thiếu khác của việc lập hồ sơ dữ liệu là thiết kế các quy tắc xác thực. Những quy tắc này xác định giá trị
Những điều này được và không được chấp nhận và chúng có thể có nhiều hình dạng và hình thức. Ví dụ, một đơn đặt hàng 
phải xảy ra trước chuyến hàng hoặc địa chỉ email phải chứa ký hiệu @.

5-4  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Tính hợp lệ và tính đúng đắn đôi khi bị nhầm lẫn. Hãy tưởng tượng rằng một doanh nghiệp vận chuyển 
các mặt hàng chỉ dành cho các bang miền Trung Tây: IL, IN, IA, KS, MI, MN, MO, NE, ND, OH, SD và WI. đây 
là một số tình huống:
• Hàng hóa được vận chuyển đến Ohio (OH), và OH được nhập làm giá trị cho trường trạng thái trong ô 
hệ thống. Giá trị vừa hợp lệ vừa chính xác.
• Ai đó vô tình ghi Minnesota (MN) là điểm đến của lô hàng 
đã đến Michigan (MI). Giá trị được nhập là hợp lệ (MN là trạng thái được chấp nhận) nhưng không chính xác.
• Doanh nghiệp nhận được đơn đặt hàng từ một khách hàng ở Pennsylvania (PA), và hàng hóa được 
được vận chuyển. PA được nhập vào hệ thống dưới dạng trạng thái. Trong khi hệ thống sẽ xem xét giá trị 
không hợp lệ thì đúng (PA là trạng thái đúng nhưng công ty không được bán hàng ở đó).
• Đơn hàng tương tự từ khách hàng ở PA được nhận và hàng sẽ được chuyển đến đó. 
NA–Không áp dụng–được nhập vào hệ thống dưới dạng trạng thái. Trong trường hợp này, giá trị được nhập 
vừa không hợp lệ vừa không chính xác.
Giá trị không chính xác có nghĩa là giá trị được gán sai và giá trị không hợp lệ có nghĩa là không chính xác.
giá trị chấp nhận được được ấn định.
tính nhất quán
Ngoài việc chính xác và hợp lệ, dữ liệu phải nhất quán. Dữ liệu không nhất quán xảy ra 
khi cùng một đặc tính được biểu diễn theo nhiều cách. Sử dụng cả MI và Michigan để 
tham chiếu đến cùng một trạng thái sẽ tạo ra sự không nhất quán về dữ liệu. Sử dụng mgr, mngr và manager để 
mô tả cùng một vị trí công việc sẽ làm như vậy. Những mâu thuẫn này tạo ra những thách thức 
trong quá trình phân tích. Ví dụ: sẽ khó xác định tổng doanh thu của mỗi bang nếu có 
là những tổng số riêng biệt cho MI và Michigan.
Làm thế nào chúng ta có thể xác định được những mâu thuẫn như thế này? Đây là hai kỹ thuật lập hồ sơ: 
• Tạo một danh sách với tất cả các giá trị riêng biệt, sau đó sắp xếp và xem xét. Các giá trị không nhất quán của mgr, 
mngr và người quản lý có thể sẽ được chú ý ngay lập tức.
• Xây dựng bảng tần số hoặc bảng đếm số lần một giá trị xuất hiện. Giá trị với 
tần số thấp có thể cho thấy dữ liệu không nhất quán.
Tính đầy đủ
Dữ liệu chính xác, hợp lệ và nhất quán chỉ chính xác nếu chúng cũng đầy đủ, vì không
dữ liệu hoàn chỉnh có thể dẫn đến những hiểu biết sai lệch. Dữ liệu có thể không đầy đủ theo hai cách.
Trường hợp còn thiếu là khi một khái niệm đã xuất hiện nhưng không được ghi lại, chẳng hạn như khi hàng hóa 
đã được bán nhưng giao dịch bán hàng không được ghi nhận. Một trường hợp bị thiếu chẳng hạn như thiếu 
giao dịch bán hàng có thể được xác định bằng phân tích chênh lệch. Nếu có một số thứ tự cho mỗi 
hóa đơn bán hàng thì việc thiếu số có thể cho thấy việc bán hàng đã xảy ra nhưng không được ghi lại.
Giá trị bị thiếu xảy ra khi giao dịch được ghi lại nhưng chúng tôi không có thông tin 
cho tất cả các đặc điểm. Kết quả là các ô trống. Điều này có thể xảy ra nếu một khách hàng được ghi lại, 
nhưng hồ sơ không bao gồm địa chỉ email của khách hàng. Thuật ngữ null thường chỉ ra 
một giá trị bị thiếu hoặc không xác định. Điều quan trọng là phải đánh giá xem thông tin còn thiếu ảnh hưởng như thế nào 
ra quyết định.
Điều tra cấu trúc dữ liệu
Cùng với chất lượng của chúng, dữ liệu được điều tra để đánh giá liệu chúng có được cấu trúc theo cách 
giúp việc phân tích dữ liệu trở nên dễ dàng và hiệu quả.
Mô tả rõ ràng
Trong quá trình khám phá và diễn giải dữ liệu, tên cột trong bảng sẽ trở thành các biến. Chúng tôi 
áp dụng các phép toán, chẳng hạn như tính tổng, cho chúng và sử dụng chúng như một phần của việc trực quan hóa
các biểu đồ, chẳng hạn như biểu đồ hình tròn. Tuy nhiên, các cột được đặt tên kém khiến việc phát triển trở nên phức tạp

5.1  Lập hồ sơ dữ liệu là gì?  5-5
mô hình thông tin và tiến hành phân tích. Tên cột cũng phải chính xác, trực quan, 
và rõ ràng vì chúng là một phần của cơ sở dữ liệu phân tích, có thể có nhiều 
người dùng. Cơ sở dữ liệu phân tích là tập dữ liệu tích hợp được sử dụng cho mục đích phân tích. Unambig-
những mô tả khó hiểu nên được ưu tiên khi phát triển cơ sở dữ liệu phân tích. Đây là một số 
ví dụ về tiêu đề cột chính xác và rõ ràng:
• Cột tuổi phải chứa các số (ví dụ: 32) chứ không phải ngày (ví dụ: 2/6/1990).
• ID khách hàng mang tính mô tả nhiều hơn ID.
• Sinh nhật dễ hiểu hơn sinh nhật.
MINH HỌA 5.2  Cột tổng hợp và cột giá trị đơn
Cole, Lakeisha, NA
López, Alejandro, CPA
Key, Kim, NA
David, Julie, CPA
Malone, Moses, NA
Buslepp, Bill, CPA
Despontin, Marc, CPA
Kaminski, Ivanka, NA
Tên
(A) Tổng hợp
Cột
Cole, Lakeisha 
López, Alejandro
Chìa khóa, Kim
David, Julie
Malone, Moses
Buslepp, Bill
Potoms, Keme, NA
Potoms, Keme
Despontin, Marc
Kaminski, Ivanka
NA
CPA
NA
CPA
NA
CPA
NA
NA
CPA
Tên
Chứng nhận
(B) Giá trị đơn
Cột
ÁP DỤNG TƯ DUY PHIẾU 5.2: Tạo sự sẻ chia, 
Từ vựng dễ hiểu
Tạo từ vựng dùng chung yêu cầu xác định ai sẽ sử dụng cơ sở dữ liệu phân tích 
(Các bên liên quan):
• Nếu bạn chuẩn bị dữ liệu cho người khác thì hãy đảm bảo rằng bạn tạo từ vựng cho cột và 
tên bảng dễ hiểu và dễ làm việc.
• Ví dụ: các nhà khoa học dữ liệu thường sử dụng các tên bảng như DCustomer và 
FSales với D và F đề cập đến một số loại bảng nhất định. Tuy nhiên, những thuật ngữ như vậy có thể gây nhầm lẫn
gửi đến các bên liên quan khác không phải là nhà khoa học dữ liệu!
Cấu trúc bảng giúp phân tích dễ dàng hơn
Phân tích bao gồm tổng hợp hoặc nhóm dữ liệu và sau đó kiểm tra chúng từ các nguồn khác nhau. 
quan điểm về nhiều mặt. Điều này được gọi là cắt lát. Đây là một ví dụ về việc cắt giảm hoạt động bán hàng
dữ liệu hành động cho một doanh nghiệp có doanh số bán hàng ở nhiều khu vực: 
• Tổng hợp: Tính tổng số tiền bán hàng.
• Lát: Chia nhỏ tổng số theo khu vực để kiểm tra doanh số khu vực chi tiết hơn.
Một số cấu trúc dữ liệu phù hợp tốt cho các quy trình tổng hợp và cắt lát này, trong khi các cấu trúc khác thì phù hợp hơn. 
thì không, vì vậy việc học các phương pháp hay nhất để cấu trúc dữ liệu là rất quan trọng. Hai cách thực hành tốt nhất phổ biến là 
cột có giá trị đơn và bảng phẳng.
Cột có giá trị đơn 
Với mục đích phân tích, mỗi ô phải chứa một giá trị 
mô tả một đặc điểm Nghĩa là, mỗi cột phải có một giá trị. Hai hoặc nhiều hơn 
các giá trị trong cùng một ô khiến việc phân tích trở nên khó khăn hơn. Đây là hai kịch bản mà 
vi phạm quy tắc một giá trị.
Cột tổng hợp kết hợp các giá trị cho hai hoặc nhiều đặc điểm. Tên col-
umn trong Hình minh họa 5.2 (A) kết hợp các đặc điểm họ, tên và chứng nhận. 
Bạn muốn tập dữ liệu nào hơn nếu cần tạo danh sách với tất cả nhân viên có 
Bảng điều khiển CPA (A) hay (B)? Mặc dù dữ liệu giống hệt nhau cho cả hai tập dữ liệu, nhưng bảng (B) giúp việc này dễ dàng hơn 
để trả lời câu hỏi này

![ILLUSTRATION 5.2](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.2.png)

5-6  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Bàn phẳng 
Một cách thực hành tốt nhất khác để cấu trúc dữ liệu là sử dụng bảng phẳng, trong đó
tiêu đề umn không chứa các giá trị dữ liệu hữu ích cho mục đích phân tích. Để phân tích dữ liệu, phẳng 
cấu trúc bảng được ưu tiên hơn các bảng chéo
Hình minh họa 5.4 (A) cho thấy một bảng chéo thể hiện mối quan hệ giữa 
hai biến số của mẫu xe và nhân viên bán hàng:
• Cột đầu tiên là giá trị của các mẫu xe khác nhau: Focus, Mustang, Escape, 
và Nhà thám hiểm.
• Tiêu đề cột ở hàng trên cùng hiển thị các giá trị dành cho nhân viên bán hàng.
• Ô mặt cắt ngang cho biết nhân viên bán hàng đã bán được bao nhiêu sản phẩm của một mẫu cụ thể. 
Nhân viên bán hàng Elodie đã bán được 5 chiếc xe Focus.
Bảng chéo có những hạn chế để phân tích. Các tên trong đầu cột bảng điều khiển (A)-
ers là ví dụ về các giá trị dữ liệu hữu ích cho việc phân tích dữ liệu. Tiêu đề cột không thể được sử dụng cho 
lọc hoặc hoạt động theo nhóm.
MINH HỌA 5.4  Cấu trúc bảng chéo so với cấu trúc bảng phẳng
Tập trung
Mustang
Thoát hiểm
Nhà thám hiểm
Tập trung
Mustang
Thoát hiểm
Nhà thám hiểm
Tập trung
Mustang
Thoát hiểm
Nhà thám hiểm
Tập trung
Mustang
Thoát hiểm
Nhà thám hiểm
4
3
2
1
5
3
0
1
0
2
1
2
0
1
4
2
người mẫu
Đơn vị đã bán
Carlos
Carlos
Carlos
Carlos
Elodie
Elodie
Elodie
Jane
Elodie
Jane
Jane
Jane
Jim
Jim
Jim
Jim
Nhân viên bán hàng
(B) Bằng phẳng
(A) Bảng chéo
Tập trung
Mustang
Thoát hiểm
Nhà thám hiểm
4
3
2
1
Carlos
5
3
0
0
Elodie
1
2
1
2
0
1
4
2
Jane
Jim
MINH HỌA 5.3  Cột nhiều giá trị và cột đơn giá trị
Cole, Lakeisha 
López, Alejandro
López, Alejandro
Chìa khóa, Kim
David, Julie
David, Julie
David, Julie
Malone, Moses
Buslepp, Bill
CISA
CISA
CPA
CMA
CISA
CMA
CPA
CMA
CPA
Buslepp, Bill
Potoms, Keme
Despontin, Marc
Kaminski, Ivanka
Kaminski, Ivanka
CPA
CMA
CPA
CISA
CMA
Tên
Chứng chỉ
(B) Giá trị đơn
Cột
Cole, Lakeisha 
López, Alejandro
Chìa khóa, Kim
David, Julie
Malone, Moses
Buslepp, Bill
Potoms, Keme
Despontin, Marc
Kaminski, Ivanka
CISA
CPA, CISA
CMA
CPA, CMA, CISA
CPA
CPA, CMA
CMA
CMA, CISA
CPA
Tên
Chứng chỉ
(A) Đa giá trị
Cột
Trong một cột có nhiều giá trị, một ô chứa nhiều giá trị có cùng đặc tính. các 
Cột Chứng chỉ trong Hình minh họa 5.3 (A) liệt kê tất cả các chứng chỉ cho một nhân viên. Một lần nữa, 
bạn muốn tập dữ liệu nào hơn nếu bạn cần tạo danh sách với tất cả nhân viên có 
bảng điều khiển CPA (A) hay (B)? Mặc dù dữ liệu giống hệt nhau cho cả hai bộ dữ liệu nhưng sẽ dễ trả lời hơn 
câu hỏi này với cột có giá trị đơn trong bảng (B).

![ILLUSTRATION 5.4](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.4.png)