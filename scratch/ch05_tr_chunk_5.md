5-28  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Mẫu chuẩn bị dữ liệu 10: Giá trị không hợp lệ
Các quy tắc dành riêng cho miền xác định xem dữ liệu có được chấp nhận hay không có thể được tạo cho hầu hết các 
cột. Dữ liệu không đáp ứng được những mong đợi này được coi là không hợp lệ.
Tạo và áp dụng quy tắc xác thực
Đối với một số quy tắc xác thực, chúng tôi có thể dựa vào thông tin hồ sơ được tạo tự động 
bằng công cụ ETL. Đối với cột bắt buộc, không thể chứa giá trị null, số liệu thống kê 
về các giá trị null do công cụ ETL cung cấp có thể được sử dụng để xác thực. Tuy nhiên, trong hầu hết các trường hợp 
quy tắc xác thực phải được triển khai bằng ngôn ngữ kịch bản. Hình minh họa 5.28 cho thấy một số 
ví dụ về các quy tắc xác thực áp dụng cho trường hợp Beans. Cú pháp được sử dụng trong mã mẫu 
cột mang tính chung chung vì không sử dụng ngôn ngữ kịch bản cụ thể nào.
MINH HỌA 5.28  Thiết kế và triển khai các quy tắc xác thực
Mô tả
Mã mẫu
Số giờ thực tế cho một 
dịch vụ phải tích cực 
và không thể vượt quá 14.
THỰC TẾGIỜHỢP LÝ =
NẾU SERVICE.ACTUALTIME > 0 VÀ SERVICEACTUALTIME <= 14,
SAU ĐÓ “CÓ”,
KHÁC “KHÔNG”
Nhân viên tối thiểu 
giá là 150 USD và 
tỷ lệ nhân viên tối đa 
phải thấp hơn $500.
GIÁ TRỊ =
NẾU TỶ LỆ NHÂN VIÊN >= 150 VÀ TỶ LỆ NHÂN VIÊN < 500,
SAU ĐÓ “CÓ”,
KHÁC “KHÔNG”
Chức danh công việc hợp lệ là:  
{Người quản lý, Đối tác,  
Cấp cao, Giám đốc cấp cao,  
Nhân viên}.
JOBTITLEVALID =
NẾU NHÂN VIÊN.JOBTITLE TRONG {“ QUẢN LÝ”, “ĐỐI TÁC”, “CAO CẤP”, “SR. MANAGER”, “NHÂN VIÊN”},
SAU ĐÓ “CÓ”,
KHÁC “KHÔNG”
Sửa đổi giá trị không hợp lệ
Nếu xác định được một giá trị nghi vấn, hãy loại bỏ nguyên nhân gốc rễ, thay đổi giá trị trong nguồn, 
hoặc thay đổi giá trị trong cơ sở dữ liệu phân tích. Trong tập dữ liệu Beans, không có dữ liệu nào không hợp lệ 
được phát hiện.
Tóm tắt mẫu 10
vấn đề
Dữ liệu không hợp lệ có thể dẫn đến việc ra quyết định kém.
Phát hiện (Hồ sơ dữ liệu)
Tạo và áp dụng các quy tắc xác thực.
Đúng (ETL)
Sửa đổi các giá trị không hợp lệ.
Dữ liệu   Một trong những trợ lý của Shanice tại Stufan đã chuẩn bị bốn hồ sơ có tên Khách hàng, Mặt hàng, Bán hàng và 
Nhân viên bán hàng và đưa chúng cho bạn. Những tập tin này có một số vấn đề về dữ liệu. Xác định chúng bằng cách sử dụng col-
umn mô hình chuyển đổi trong phần này.
Đối với mỗi vấn đề về dữ liệu bạn xác định: 
1. Mô tả vấn đề. 
2. Xác định mẫu chuẩn bị dữ liệu bạn đã áp dụng để phát hiện sự cố. 
3. Giải thích cách bạn sẽ sửa nó.
Áp dụng nó 5.4
Sử dụng cột 
Chuyển đổi 
mẫu

![ILLUSTRATION 5.28](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.28.png)

5.5  Những mẫu nào biến đổi bảng?  5-29
GIẢI PHÁP
Vấn đề 1:
1. Dữ liệu trong cột LoyaltyRating trong bảng Khách hàng không hữu ích cho việc phân tích 
mục đích.
2. Mẫu chuẩn bị dữ liệu 3: Dữ liệu không liên quan và không đáng tin cậy.
3. Xóa cột LoyaltyRating khỏi cơ sở dữ liệu phân tích.
Vấn đề 2:
1. Bảng Bán hàng có một cột có tiêu đề-SP không rõ ràng.
2. Mẫu chuẩn bị dữ liệu 4: Tên cột không chính xác và mơ hồ.
3. Thay thế SP viết tắt mơ hồ bằng SalesPerson.
Vấn đề 3:
1. Cột Trạng thái trong bảng Khách hàng chứa giá trị DN, giá trị này có thể không chính xác, 
không nhất quán và/hoặc không hợp lệ. 
2. Mẫu chuẩn bị dữ liệu 7, 8 và 10: Giá trị không chính xác, không nhất quán và không hợp lệ.
3. Thay thế giá trị DN bằng DE.
5.5  Những mẫu nào biến đổi 
Bàn?
MỤC TIÊU BÀI HỌC ➎
Áp dụng các mẫu để chuyển đổi bảng.
Các mẫu chuyển đổi ở cấp độ bảng tìm kiếm các vấn đề về dữ liệu trong một bảng duy nhất, chẳng hạn như ambig-
các bảng được đặt tên không rõ ràng, thiếu khóa chính và các cột chồng chéo. 
Mẫu chuẩn bị dữ liệu 11: Không trực quan và 
Tên bảng mơ hồ
Giống như tên cột, tên bảng là một phần của cả mô hình dữ liệu và từ vựng của tập dữ liệu, 
vì vậy chúng phải chính xác, trực quan và rõ ràng.
Quét bảng để tìm tên không chính xác hoặc mơ hồ
Việc kiểm tra nội dung của bảng và định nghĩa từ điển dữ liệu của nó có thể giúp xác định liệu 
cái tên phản ánh chính xác nội dung của nó. Quy tắc đặt tên bảng cũng giống như quy định 
để đặt tên cột. Chúng phải trực quan, tránh khoảng trắng, dấu gạch dưới và mã hóa đặc biệt:
• Ví dụ: sử dụng Biên nhận tiền mặt thay vì Biên nhận tiền mặt.
• Tránh mã hóa đặc biệt như DCustomer (D đề cập đến bảng thứ nguyên, nhưng không phải ai cũng 
sẽ hiểu điều đó).

5-30  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Đổi tên bảng
Để khắc phục sự cố này, hãy đổi tên bảng bằng công cụ ETL vì việc thay đổi tên sẽ tự động được thực hiện. 
được phổ biến tới tất cả các công thức. Đối với ví dụ về Đậu, hãy thực hiện hai thay đổi. Đầu tiên, thay thế ClData 
bằng Khách hàng và sau đó thay thế E-Dem bằng Nhân khẩu học nhân viên.
Tóm tắt mẫu 11
vấn đề
Tên bảng không chính xác hoặc mơ hồ làm cho nó 
khó hiểu và khó làm việc hơn với một tập dữ liệu.
Phát hiện (Hồ sơ dữ liệu)
Quét trực quan các bảng để tìm lỗi không chính xác hoặc mơ hồ 
những cái tên.
Đúng (ETL)
Đổi tên bảng.
Mẫu chuẩn bị dữ liệu 12: Thiếu khóa chính
Mẫu này tập trung vào các khóa chính. Các bảng là sự mô tả các thực thể và mỗi trường hợp của 
một thực thể phải được xác định duy nhất. Để là khóa chính, một cột phải có một khóa duy nhất 
giá trị cho mỗi trường hợp và không có giá trị null. Các khóa chính thường đã có sẵn khi 
dữ liệu được trích xuất từ cơ sở dữ liệu quan hệ. Tuy nhiên, khóa chính sẽ không được đặt đúng chỗ 
khi dữ liệu được trích xuất từ bảng tính, chẳng hạn như trong trường hợp Beans. Để thành lập một trường sơ cấp 
khóa, trường phải được chọn và cả hai quy tắc phải được xác thực.
Xác định các bảng bị thiếu khóa chính
Mỗi bảng cần ít nhất một cột—hoặc tổ hợp các cột—đáp ứng cả hai 
tiêu chí đã thảo luận trước đó. Các cột đáp ứng cả hai tiêu chí là khóa ứng viên và ETL 
công cụ có thể giúp xác định chúng. Cấu hình cột do Power Query cung cấp, lần đầu tiên được hiển thị trong 
Hình minh họa 5.15 và được lặp lại trong Hình minh họa 5.29, cung cấp thông tin cần thiết để 
xác định khóa ứng cử viên: 
• Giá trị của Empty phải bằng 0. 
• Các giá trị của Đếm, Khác biệt và Duy nhất phải giống nhau. Giá trị duy nhất là giá trị 
chỉ xảy ra một lần trong cột.
MINH HỌA 5.29  Cột 
Hồ sơ trong Power Query
Thống kê cột
Đếm
4.632
Lỗi
0
trống
0
khác biệt
4.632
duy nhất
4.632
NaN
0
số không
0
tối thiểu
1
Tối đa
4.632
trung bình
2.316,5
Độ lệch chuẩn
1.337,28...
Thậm chí
2.316
Lẻ
2.316
Tạo khóa chính
Bảng Nhân khẩu học không có khóa ứng viên. Chúng ta có thể kết hợp cái đầu tiên 
và họ vào cùng một trường (Tên), nhưng nhìn chung không nên sử dụng tên làm tên chính 
các khóa vì chúng hiếm khi là duy nhất. Đối với các tình huống như thế này, hãy tạo khóa nhân tạo, chẳng hạn như 
số. Như Hình minh họa 5.30 cho thấy, các công cụ ETL có thể giúp giải quyết vấn đề đó:

![ILLUSTRATION 5.30](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.30.png)

5.5  Những mẫu nào biến đổi bảng?  5-31
• Trong Power Query, nhấp vào Thêm cột trong Menu chính.
• Chọn Cột chỉ mục.
• Bấm Từ 1.
MINH HỌA 5.30  Tạo khóa chính
Trang chủ
chuyển đổi
Xem
Thêm cột
Chưa có tiêu đề - Trình soạn thảo Power Query
Tập tin
≠
123
Cột có điều kiện
Cột chỉ mục
cột intex
Truy vấn [5]
tùy chỉnh
Cột
Cột Từ
Ví dụ
ƒx 
ƒx 
Gọi tùy chỉnh
chức năng
chung
ABC ĐẦU TIÊN
Từ 0
Từ 1
Tùy chỉnh...
Trường hợp của tập dữ liệu Beans phức tạp hơn nên có một giải pháp thay thế, 
được trình bày với Mẫu 15. 
Tóm tắt Mẫu 12
vấn đề
Một số bảng không có khóa chính.
Phát hiện (Hồ sơ dữ liệu)
Xác định các bảng thiếu khóa chính.
Đúng (ETL)
Tạo khóa chính.
Mẫu chuẩn bị dữ liệu 13: Nội dung dư thừa 
Trên các cột
Mẫu này tìm kiếm những phần dư thừa tạo ra sự không nhất quán. Xảy ra mâu thuẫn dữ liệu 
khi cùng một dữ liệu được ghi lại nhiều lần và được thay đổi ở một nơi nhưng không phải ở nơi khác, 
chẳng hạn như địa chỉ email của khách hàng. Đây là hai tình huống trong đó có hai hoặc nhiều cột trong một 
bảng có thể có cùng nội dung:
• Khi có sự trùng lặp chẳng hạn như một địa chỉ chứa thông tin trạng thái và một địa chỉ riêng biệt 
trường trạng thái.
• Khi có sự phụ thuộc, tồn tại khi giá trị của một cột phụ thuộc vào 
các giá trị của một cột khác trong cùng một bảng. Giả sử cả tuổi và ngày sinh đều 
được ghi lại. Tuy nhiên, giá trị tuổi thay đổi khi thời gian trôi qua và dữ liệu sẽ trở nên 
không nhất quán. Vì vậy, thay vì chuyển tuổi từ nguồn dữ liệu, cần tính
được quản lý như một phần của cơ sở dữ liệu phân tích. 
Thực hiện so sánh theo cột
Việc thực hiện so sánh từng cột để tìm phần chồng chéo hoặc phần phụ thuộc sẽ phát hiện ra điều này 
vấn đề. Làm như vậy trong tập dữ liệu Beans sẽ cho thấy hiện tại không có nội dung dư thừa. 
Xóa các cột dư thừa và phụ thuộc
Những cột chứa thông tin dư thừa có thể bị xóa. Khi có sự phụ thuộc, 
xóa cột chứa giá trị phụ thuộc. Thay vào đó, hãy sử dụng công thức để tạo lại 
cột trong cơ sở dữ liệu phân tích.

5-32  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Tóm tắt mẫu 13
vấn đề
Nội dung dư thừa giữa các cột trong bảng 
có thể dẫn đến sự không nhất quán.
Phát hiện (Hồ sơ dữ liệu)
Thực hiện so sánh theo từng cột.
Đúng (ETL)
Xóa dữ liệu dư thừa và phụ thuộc.
Mẫu chuẩn bị dữ liệu 14: Tìm giá trị không hợp lệ 
với Quy tắc trong bảng
Mẫu 14 tương tự như Mẫu 10 ở chỗ nó cũng xác định các giá trị được chấp nhận cho một cột. Làm thế nào-
bao giờ hết, Mẫu 14 xác định tính hợp lệ của các giá trị của cột dựa trên các giá trị trong một hoặc 
nhiều cột khác trong cùng một bảng.
Tạo và áp dụng quy tắc xác thực trong bảng
Mục tiêu của quy tắc xác thực là xác định dữ liệu không hợp lệ. Việc tạo quy tắc xác thực yêu cầu 
kiến thức chuyên sâu về doanh nghiệp và chúng được triển khai bằng ngôn ngữ kịch bản. 
Hình minh họa 5.31 hiển thị quy tắc xác thực trong bảng cho trường hợp Beans. Các giá trị trong 
cột Tỷ lệ phụ thuộc vào các giá trị trong cột Vị trí công việc. Áp dụng xác thực này 
quy tắc đối với tập dữ liệu của Bean cho thấy tỷ lệ này quá thấp đối với năm nhân viên–Alex Messi, 
Thibaut Martens, Paulo Lukaku, Ed Diamond và Molly McCarthy.
MINH HỌA 5.31  Thiết kế và 
Triển khai nội bảng 
Quy tắc xác thực
MÔ TẢ
Tỷ lệ nhân viên của Beans được xác định theo vị trí công việc của họ. Bảng hiển thị mức tối thiểu 
và mức tối đa, tính bằng đô la, cho từng vị trí công việc.
Vị trí
>=
<
nhân viên
150
200
cao cấp
200
250
Người quản lý
250
300
Giám đốc cấp cao
300
350
Đối tác
350
500
MÃ MẪU
RATEVALIDBASEDONJOBTITLE =
NẾU NHÂN VIÊN.JOBTITLE = “Nhân viên” VÀ (NHÂN VIÊN.RATE >= 150 VÀ NHÂN VIÊN.RATE < 200), THÌ “CÓ”, ELSE,
NẾU NHÂN VIÊN.JOBTITLE = “Cấp cao” VÀ (NHÂN VIÊN.RATE >= 200 VÀ NHÂN VIÊN.RATE < 250), “CÓ”, ELSE,
NẾU NHÂN VIÊN.JOBTITLE = “Người quản lý” VÀ (NHÂN VIÊN.RATE >= 250 VÀ NHÂN VIÊN.RATE < 300), “CÓ”, ELSE,
NẾU NHÂN VIÊN.JOBTITLE = “Quản lý cấp cao” VÀ (EMPLOYEE.RATE >= EMPLOYEE.RATE < 350), “CÓ”, ELSE,
NẾU NHÂN VIÊN.JOBTITLE = “Đối tác” VÀ (NHÂN VIÊN.RATE >= 350 VÀ NHÂN VIÊN.RATE < 500), “CÓ”, ELSE,
“KHÔNG”
)

5.5  Những mẫu nào biến đổi bảng?  5-33
Sửa đổi giá trị không hợp lệ
Tại Beans, việc sửa đổi tỷ lệ nhân viên hoặc chính sách tỷ lệ cần có sự chấp thuận của Giám đốc điều hành, vì vậy 
không thể thay đổi tỷ giá cho đến khi được phê duyệt.
Áp dụng nó 5.5
Chuyển đổi bảng 
với các mẫu
Tại Stufan, Giám đốc điều hành Shanice băn khoăn liệu có thể tích hợp thông tin bán hàng và mua hàng hay không?
cơ sở để phân tích. Thông tin mua hàng hiện được ghi lại trong một bảng tính Excel có tiêu đề PTS, một 
mẫu trong số đó được hiển thị.
ngoại hối
1
B
C
D
E
A
PTS
2
3
4
5
6
7
8
9
hóa đơn
2
2
1
1
5
4
3
4
Giá
10
7
20
15
9
25
20
20
số lượng
10
10
10
10
10
10
10
10
nhà cung cấp
BIC
BIC
DITV
DITV
KÍCH THÍCH
DELT
STWS
DELT
Mục
TINL
TUYẾT
DOCL
TÀI LIỆU
TINL
TUYẾT
DUCH
GRUML
Tự động Lưu
Oﬀ
Sử dụng các mẫu chuyển đổi bảng để xác định hai vấn đề về dữ liệu trong tệp PTS. 
1. Đầu tiên, hãy mô tả vấn đề dữ liệu. 
2. Tiếp theo, xác định mẫu khám phá dữ liệu mà bạn có thể áp dụng để phát hiện nó. 
3. Cuối cùng, giải thích cách bạn khắc phục vấn đề. 
GIẢI PHÁP
Vấn đề 1:
1. Tên hiện tại của bảng tính/bảng không rõ ràng. PTS là viết tắt của Giao dịch mua hàng, 
nhưng điều đó không rõ ràng từ tiêu đề. 
2. Sử dụng Mẫu khám phá dữ liệu 11: Tên bảng không trực quan và mơ hồ.
3. Đổi tên bảng tính “Mua hàng”.
Vấn đề 2:
1. Bảng hiện không có khóa chính và không có cột nào chứa giá trị duy nhất
ue. Mỗi hàng trong bảng đại diện cho một dòng hoá đơn. Hai hàng đầu tiên trong bảng thể hiện 
hai chi tiết đơn hàng cho hóa đơn 1, một chi tiết đơn hàng cho mặt hàng DOCL và một chi tiết đơn hàng khác cho mặt hàng DOCS.
2. Sử dụng Mẫu khám phá dữ liệu 12: Thiếu khóa chính.
3. Tạo khóa nhân tạo bao gồm các số liên tiếp duy nhất. 
Tóm tắt mẫu 14
vấn đề
Dữ liệu không hợp lệ có thể dẫn đến việc ra quyết định kém.
Phát hiện (Hồ sơ dữ liệu)
Tạo và áp dụng các quy tắc xác thực trong bảng.
Đúng (ETL)
Sửa đổi các giá trị không hợp lệ.

![Apply It 5.5](../TaiLieu/textbookForPractice/Figures/Ch_05/Apply%20It%205.5.png)