5-40  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Sửa đổi giá trị không hợp lệ
Nếu bạn đang giải quyết vụ Beans, bạn sẽ tham khảo ý kiến của Giám đốc điều hành để tìm hiểu xem liệu chính sách có phù hợp không. 
vi phạm, nhập dữ liệu không chính xác hoặc lý do khác gây ra lỗi. Một khi đã được xác định, 
vấn đề có thể được khắc phục bằng cách áp dụng biện pháp kiểm soát để tránh vi phạm chính sách thêm, khắc phục-
nhập các giá trị trong dữ liệu nguồn hoặc sửa các giá trị trong cơ sở dữ liệu phân tích.
Tóm tắt Mẫu 17
vấn đề
Dữ liệu không hợp lệ có thể dẫn đến việc ra quyết định kém.
Phát hiện (Hồ sơ dữ liệu)
Tạo và áp dụng các quy tắc xác thực giữa các bảng.
Đúng (ETL)
Sửa đổi các quy tắc không hợp lệ.
Áp dụng nó 5.6
Vẽ sơ đồ sao
Dữ liệu   Trợ lý của Shanice tại Stufan cung cấp cho bạn các phiên bản sửa đổi của Khách hàng, Mặt hàng, Bán hàng, 
và các tập tin Nhân viên bán hàng. Sử dụng dữ liệu trong các tệp này để vẽ lược đồ sao.
1. Vẽ các bảng khác nhau và các trường của chúng.
2. Dán nhãn cho mỗi bảng là sự kiện hoặc thứ nguyên và gắn nhãn cho mỗi bảng thứ nguyên là ai, khi nào hoặc cái gì.
3. Đặt bảng sự kiện ở giữa.
4. Hoàn thiện lược đồ hình sao bằng cách kết nối các bảng và xác định số lượng của chúng.
GIẢI PHÁP
Giao dịch
Cái gì?
Ai?
Ai?
Bảng kích thước
Bảng sự kiện
Bảng kích thước
N
N
N
1
1
1
Nhân viên bán hàng
ID nhân viên bán hàng
Tên
Thành phố
tiểu bang
Mục
Mã hàng
Mô tả
Danh mục
QOH
Khách hàng
Mã khách hàng
Tên
Thành phố
tiểu bang
bán hàng
Khách hàng
Nhân viên bán hàng
Mục
bán hàng
Giá
số lượng
Ngày
ID
1
4
2
3
Chìa khóa
Cột
Khóa ngoại

![Apply It 5.6](../TaiLieu/textbookForPractice/Figures/Ch_05/Apply%20It%205.6.png)

5.7  Mẫu nào áp dụng cho việc tải dữ liệu?  5-41
5.7  Áp dụng mẫu nào cho 
Đang tải dữ liệu?
MỤC TIÊU HỌC TẬP ❼
Áp dụng các mẫu cho các vấn đề tải dữ liệu.
Sau khi dữ liệu được làm sạch và chuyển đổi, đã đến lúc tải chúng vào phần mềm để phân tích.
chị ơi. Tải dữ liệu là quá trình làm cho cơ sở dữ liệu phân tích có sẵn để sử dụng. Vì cả hai 
trích xuất và tải là các quá trình truyền tải, chúng có những vấn đề tương tự khi nói đến 
tính đầy đủ và chính xác của dữ liệu được truyền. Điều quan trọng nữa là mô hình dữ liệu của 
cơ sở dữ liệu phân tích được xác thực - nghĩa là tất cả các mối quan hệ đã được xác định.
Mẫu chuẩn bị dữ liệu 18: Chưa hoàn chỉnh  
Đang tải dữ liệu
Đang tải sẽ di chuyển dữ liệu từ công cụ ETL sang cơ sở dữ liệu phân tích. Hình minh họa 5.40 cho thấy 
cách chuyển dữ liệu từ công cụ ETL, trong trường hợp này là Power Query, sang cơ sở dữ liệu phân tích.
Có ba lựa chọn: 
• Đóng và áp dụng: Đóng Power Query và áp dụng tất cả các phép biến đổi cho cơ sở dữ liệu phân tích.
• Áp dụng: Áp dụng tất cả các phép biến đổi cho cơ sở dữ liệu phân tích nhưng vẫn mở Power Query.
• Đóng: Đóng Power Query mà không áp dụng bất kỳ phép biến đổi nào cho cơ sở dữ liệu phân tích.
Nếu chúng ta chọn một trong hai tùy chọn đầu tiên thì điều quan trọng là phải xác nhận rằng tất cả dữ liệu đã được 
được chuyển giao. 
So sánh số hàng
Giống như Mẫu 1, số hàng cho cơ sở dữ liệu phân tích có thể được so sánh với số hàng 
của tập dữ liệu trong công cụ ETL. Công cụ ETL cũng sẽ đưa ra cảnh báo nếu có bất kỳ lỗi nào xảy ra khi 
các phép biến đổi được áp dụng cho cơ sở dữ liệu phân tích. 
Thêm hàng bị thiếu
Nếu các số không khớp, hãy xác định hàng nào không được chuyển và tại sao. Một khi đã xác định-
được xác nhận, hãy thêm các hàng còn thiếu vào cơ sở dữ liệu phân tích.
MINH HỌA 5.40  Phân tích ETL 
Chuyển cơ sở dữ liệu
Tập tin
Trang chủ
chuyển đổi
Gần đây
Nguồn
Nhập
dữ liệu
Mới
Nguồn
Đóng & Áp dụng
Đóng
Áp dụng
Đóng &
Áp dụng

![ILLUSTRATION 5.40](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.40.png)

5-42  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Tóm tắt mẫu 18
vấn đề
Tất cả dữ liệu không được chuyển trong khi tải. 
Phát hiện (Hồ sơ dữ liệu)
So sánh số hàng.
Đúng (ETL)
Thêm dữ liệu còn thiếu.
Mẫu chuẩn bị dữ liệu 19: Dữ liệu không chính xác 
Đang tải
Ngay cả khi tất cả các hàng đã được chuyển, dữ liệu có thể chưa được chuyển đúng.
trực tiếp. Mẫu 19 giải quyết vấn đề tiềm ẩn này.
So sánh số tiền kiểm soát
Giống như Mẫu 2, một cách hiệu quả để xác thực việc truyền dữ liệu chính xác là so sánh các khoản tiền, 
mức trung bình hoặc bất kỳ số tiền kiểm soát nào khác.
Sửa đổi giá trị không chính xác
Nếu các số không khớp, hãy xác định dữ liệu nào được truyền không chính xác và dữ liệu nào 
gây ra vấn đề. Sau khi xác định được, hãy sửa đổi các giá trị được chuyển không chính xác trong thiết bị phân tích.
cơ sở dữ liệu ical.
Tóm tắt mẫu 19
vấn đề
Dữ liệu chính xác không được chuyển trong quá trình tải. 
Phát hiện (Hồ sơ dữ liệu)
So sánh số lượng kiểm soát
Đúng (ETL)
Sửa đổi các giá trị không chính xác.
Mẫu chuẩn bị dữ liệu 20: Thiếu hoặc không chính xác 
Mối quan hệ dữ liệu
Analytics phụ thuộc rất nhiều vào mô hình dữ liệu cơ bản. Liên quan đến dữ liệu bị thiếu hoặc được xác định không chính xác
nhiệm vụ làm cho việc phân tích trở nên khó khăn hoặc thậm chí là không thể, vì vậy tính đầy đủ và chính xác của 
mô hình dữ liệu phải được xác nhận sau khi tải.
Điều tra tính đầy đủ và chính xác của mô hình dữ liệu
Một mô hình dữ liệu đầy đủ và chính xác là một mô hình trong đó tất cả các mối quan hệ đều chính xác. 
Hình minh họa 5.41 cho thấy mô hình dữ liệu cuối cùng cho cơ sở dữ liệu phân tích Beans được tạo 
với Power Query. So sánh điều này với mô hình dữ liệu của bạn và xác định rằng không có mối quan hệ nào 
bị thiếu, không có mối quan hệ không cần thiết và tất cả các mối quan hệ đều được xác định chính xác. 
MINH HỌA 5.41  Mô hình dữ liệu Beans
Chứng chỉ
Chứng nhận
ID nhân viên
...
nhân viên
ID nhân viên
Tên đầu tiên
Chức danh công việc
Họ
Tình trạng hôn nhân
tỷ lệ
Đại học
...
Dịch vụ
Thời gian thực tế
Ngân sáchThời gian
khách hàng
Ngày
nhân viên
ID dịch vụ
Nhiệm vụ
...
Nhiệm vụ
Khu vực
ID tác vụ
Tên nhiệm vụ
...
khách hàng
ID khách hàng
Tên ngành
Tên
...
*
1
*
1
*
*
1
1

![ILLUSTRATION 5.41](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.41.png)

5.7  Mẫu nào áp dụng cho việc tải dữ liệu?  5-43
Sửa đổi mô hình dữ liệu
Để thực hiện việc này trong Power BI, hãy chọn tab Trang chủ trong Menu chính và nhấp vào Quản lý mối quan hệ-
tàu trong dải băng. Cửa sổ như minh họa 5.42 sẽ xuất hiện. Chọn các nút ở 
ở cuối cửa sổ để tạo, chỉnh sửa hoặc xóa mối quan hệ.
MINH HỌA 5.42  Quản lý các mối quan hệ
Dịch vụ (Khách hàng)
Dịch vụ (Nhân viên)
Dịch vụ (Nhiệm vụ)
Khách hàng (ID khách hàng)
Nhân viên (ID nhân viên)
Nhiệm vụ (ID nhiệm vụ)
Từ: Bảng (Cột)
Giấy chứng nhận (ID nhân viên)
Mới...
Đến: Bảng (Cột)
Nhân viên (ID nhân viên)
Chỉnh sửa...
Xóa
Tự động phát hiện...
Đóng
Đang hoạt động
Quản lý mối quan hệ
Hình minh họa 5.43 cho thấy một số khía cạnh của mối quan hệ có thể được xác định:
• Các trường dữ liệu mà mối quan hệ được xác định giữa chúng.
• Các yếu tố áp dụng cho mối quan hệ.
• Hướng điều hướng dùng để tổng hợp dữ liệu.
MINH HỌA 5.43  Xác định các mối quan hệ
Chọn các bảng và cột có liên quan.
được rồi
Hủy bỏ
Hồng y
Chứng chỉ
2
3
3
CPA
CPA
CMA
ID nhân viên
Chứng nhận
nhân viên
1
2
3
Nhân viên
Người quản lý
cao cấp
ID nhân viên
Chức danh công việc
Kayne
Ivan
Mick
Tên đầu tiên
James
lenk
Richards
Họ
Đại học bang Michigan
Đại học Michigan
Đại học bang Wayne
Đại học
165
250
225
tỷ lệ
đã kết hôn
Độc thân
Tình trạng hôn nhân
Nhiều thành một (*:1)
Làm cho mối quan hệ này hoạt động
Giả sử tính toàn vẹn tham chiếu
Hướng lọc chéo
Độc thân
Áp dụng bộ lọc bảo mật theo cả hai hướng
Điều hướng
phương hướng
Các trường cho
mối quan hệ
độ nét
Hồng y
đặc điểm kỹ thuật
Chỉnh sửa mối quan hệ

![ILLUSTRATION 5.43](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.43.png)
![ILLUSTRATION 5.43_1](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.43_1.png)

5-44  CHƯƠNG 5  Phân tích: Chuẩn bị dữ liệu
Tóm tắt mẫu 20
vấn đề
Mối quan hệ dữ liệu bị thiếu hoặc được xác định không chính xác 
làm cho việc phân tích trở nên khó khăn hoặc thậm chí là không thể.
Phát hiện (Hồ sơ dữ liệu)
Kiểm tra tính đầy đủ và chính xác của 
mô hình dữ liệu.
Đúng (ETL)
Sửa đổi mô hình dữ liệu.
Quá trình chuyển đổi tập dữ liệu Beans và quá trình chuẩn bị cho phân tích hiện đã hoàn tất.
Hình minh họa 5.44 cho thấy từ điển dữ liệu đã sửa đổi cho cơ sở dữ liệu phân tích trong Illus-
tỷ lệ 5.41.
MINH HỌA 5.44  Từ điển dữ liệu sửa đổi Beans
Dịch vụ
Tên
Mô tả
Kiểu dữ liệu
Chìa khóa
bắt buộc
khách hàng
ID duy nhất của khách hàng.
số nguyên
nước ngoài
Có
nhân viên
ID duy nhất của nhân viên.
số nguyên
nước ngoài
Có
Nhiệm vụ
ID duy nhất của một nhiệm vụ.
số nguyên
nước ngoài
Có
ID dịch vụ
ID duy nhất của dịch vụ.
số nguyên
Chính
Có
Ngày
Ngày thực hiện dịch vụ.
Ngày
Có
Thời gian thực tế
Thời gian thực tế dành cho 
dịch vụ được cung cấp.
thập phân
Có
Thời gian dự toán
Thời gian dự kiến cho dịch vụ 
được cung cấp.
thập phân
Có
Nhiệm vụ
Tên
Mô tả
Kiểu dữ liệu
Chìa khóa
bắt buộc
ID tác vụ
ID duy nhất của một nhiệm vụ.
số nguyên
Chính
Có
Tên nhiệm vụ
Tên của một nhiệm vụ.
văn bản
Có
Khu vực
Khu vực của một nhiệm vụ.
văn bản
Có
khách hàng
Tên
Mô tả
Kiểu dữ liệu
Chìa khóa
bắt buộc
ID khách hàng
ID duy nhất của khách hàng.
số nguyên
Chính
Có
Tên
Tên của khách hàng.
văn bản
Có
Tên ngành
Ngành công nghiệp của khách hàng.
văn bản
Có
nhân viên
Tên
Mô tả
Kiểu dữ liệu
Chìa khóa
bắt buộc
ID nhân viên
ID duy nhất của nhân viên.
số nguyên
Chính
Có
Tên đầu tiên
Tên của một nhân viên.
văn bản
Có
Họ
Họ của nhân viên.
văn bản
Có
Chức danh công việc
Chức danh công việc của một nhân viên.
văn bản
Có
tỷ lệ
Mức giá tính theo giờ cho 
nhân viên.
số nguyên
Có
Tình trạng hôn nhân
Tình trạng hôn nhân của một nhân viên.
văn bản
Không
Đại học
Trường đại học từ đó 
nhân viên đã nhận được một 
bằng đại học.
văn bản
Không
Chứng nhận
Tên
Mô tả
Kiểu dữ liệu
Chìa khóa
bắt buộc
ID nhân viên
ID duy nhất của nhân viên.
số nguyên
nước ngoài
Có
Chứng nhận
Một chứng nhận đạt được bởi 
nhân viên.
văn bản
Có

![ILLUSTRATION 5.44](../TaiLieu/textbookForPractice/Figures/Ch_05/ILLUSTRATION%205.44.png)

5.7  Mẫu nào áp dụng cho việc tải dữ liệu?  5-45
Áp dụng nó 5.7
Đánh giá 
Mối quan hệ 
Giữa các bàn
Hai hình minh họa sau đây thể hiện mối quan hệ hiện tại giữa bảng Bán hàng và Khách hàng 
cho tập dữ liệu Stufan. Có hai vấn đề có thể làm sai lệch đáng kể mọi phân tích liên quan đến 
mối quan hệ này. Xác định chúng và mô tả lý do tại sao chúng là vấn đề.
Chọn các bảng và cột có liên quan.
Hồng y
Chỉnh sửa mối quan hệ
Mã khách hàng
Khách hàng
bán hàng
Tên
Thành phố
tiểu bang
1
2
3
1
2
3
1
30
30
20
1
2
Cruella De Vil
Sẹo LeRoi
Winnie Pooh
Orlando
Phượng hoàng
Wilmington
AZ
DE
FL
ID
bán hàng
Mục
Giá
số lượng
Khách hàng
Nhân viên bán hàng
Ngày
DOCL
GRUML
SNES
10
1
1
6
10
20
111223333
111223333
vô giá trị
Thứ Sáu, ngày 21 tháng 2 năm 2025
Thứ Sáu, ngày 21 tháng 2 năm 2025
Thứ Bảy, ngày 22 tháng 2 năm 2025
Một chọi một (1:1)
Cả hai
Làm cho mối quan hệ này hoạt động
Giả sử tính toàn vẹn tham chiếu
Hướng lọc chéo
được rồi
Hủy bỏ
1
1
…
Khách hàng
Thành phố
Tên
tiểu bang
Mã khách hàng
Thu gọn
Thu gọn
…
bán hàng
Ngày
ID
Mục
Giá
số lượng
∑
∑
∑
∑
∑
bán hàng
Nhân viên bán hàng
Khách hàng
GIẢI PHÁP
1. Mối quan hệ được xác định giữa các trường sai: Mã khách hàng và ID. ID là một chuỗi
số hiệu được gán cho mỗi hàng trong bảng Bán hàng. Kết quả là, khách hàng sai là 
được phân công bán hàng. Mối quan hệ lẽ ra phải được xác định giữa 
Trường Mã khách hàng trong bảng Khách hàng và trường Khách hàng trong bảng Bán hàng.
2. Mẫu số lượng 1-N được mong đợi cho mối quan hệ giữa bảng thứ nguyên (khách hàng) 
và một bảng thực tế (bán hàng). Khách hàng có thể thực hiện nhiều lần bán hàng nhưng chỉ có một khách hàng được xác định cụ thể
cụ thể cho mỗi lần bán hàng.

![Apply It 5.7](../TaiLieu/textbookForPractice/Figures/Ch_05/Apply%20It%205.7.png)