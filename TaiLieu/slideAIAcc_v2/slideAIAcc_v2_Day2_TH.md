# KẾ HOẠCH SLIDE THỰC HÀNH - DAY 2 (BUỔI 2)
**Tên bài:** THỰC HÀNH CHUẨN HÓA DỮ LIỆU BẰNG POWER QUERY & EXCEL
**Định hướng:** Hands-on (Thực hành trực tiếp), No-code Data Transformation, Trải nghiệm dọn dẹp dữ liệu Kế toán thực tế.
**Nguồn dữ liệu:** *Blog Power Query, Power Query M Language, Apply It 2.1 & 2.2 (Foundational Data Analysis Skills)*

**ĐỀ XUẤT NGUỒN ẢNH MINH HỌA:**
- **Lấy từ file DOCX:** Lấy các bảng biểu từ bài tập Apply It 2.1 & 2.2 (Bảng Super Scooters).
- **Chụp ảnh màn hình (Screenshot):** Cực kỳ quan trọng để hướng dẫn sinh viên thao tác. Cần chụp giao diện Power Query Editor, nút Get Data, bảng Applied Steps.
- **Sinh ảnh bằng AI:** Sinh các ảnh minh họa trừu tượng (như cỗ máy xay dữ liệu, người kế toán lắp ráp các khối lego dữ liệu).

---

# PHẦN 1: GIỚI THIỆU THỰC HÀNH \& SỨC MẠNH CỦA POWER QUERY

## TRANG BÌA (Title Page)
- Tiêu đề chính: Trí tuệ Nhân tạo cho Kế toán (Phần Thực Hành)
- Tiêu đề phụ: Buổi 2 - Thực hành Chuẩn hóa dữ liệu với Power Query
- Tác giả: Đại học Đông Á
- *(🖼️ Ảnh minh họa: AI Generated - Giao diện dashboard hiện đại với biểu tượng phễu lọc dữ liệu).*

## Năng lực đạt được sau buổi học
- **Về Lý thuyết (LT):** Hiểu được nguyên lý hoạt động của Power Query trong việc kết nối, làm sạch và hợp nhất dữ liệu; Nắm bắt được logic của các phép Joins (Left, Right, Inner) trong thao tác gộp bảng.
- **Về Thực hành (TH):** Biết cách dùng tính năng cơ bản của Power Query và kết hợp ChatGPT để làm sạch một file dữ liệu "bẩn" (xóa cột thừa, tách/gộp chuỗi văn bản, chuyển đổi kiểu dữ liệu); Thực hiện thành công bài tập Case Study "Super Scooters" (Apply It 2.1 \& 2.2).
- **Về Tư duy nghề nghiệp:** Loại bỏ thói quen làm sạch dữ liệu thủ công, biết cách thiết lập các quy trình dọn dẹp dữ liệu tự động (Automated Data Transformation) để tiết kiệm thời gian cho Kế toán viên.

## Nỗi ám ảnh của Kế toán viên
- Có bao giờ bạn phải mất hàng giờ đồng hồ mỗi cuối tháng chỉ để:
  - Copy-paste dữ liệu từ 12 file Excel của 12 tháng lại với nhau?
  - Dò tìm lỗi VLOOKUP bị \#N/A vì khác định dạng?
  - Xóa thủ công hàng ngàn dòng trắng và khoảng cách thừa?

## Giải pháp mang tên Power Query
- **Power Query là gì?** Là một công cụ kết nối và chuẩn hóa dữ liệu siêu mạnh mẽ của Microsoft.
- Được ví như "Trợ lý dọn dẹp dữ liệu cá nhân" (Personal Data Assistant).
- **Đặc biệt:** Hoàn toàn KHÔNG cần biết code (No-code).

## Power Query nằm ở đâu?
- Được tích hợp sẵn hoàn toàn miễn phí.
- **Trong Excel:** Vào tab \texttt{Data} $\rightarrow$ Chọn \texttt{Get \& Transform Data}.
- **Trong Power BI Desktop:** Nút \texttt{Get Data} $\rightarrow$ \texttt{Transform Data}.
- *(🖼️ Ảnh minh họa: Screenshot vị trí nút bấm Get Data trên thanh Ribbon của Excel).*

## Giao diện Power Query Editor (Phần 1)
- **Ribbon (Thanh công cụ):** Chứa các tab \texttt{Home}, \texttt{Transform}, \texttt{Add Column}. Nơi thực hiện các phép thuật biến đổi.
- **Queries Pane (Cửa sổ Queries):** Nằm bên trái, quản lý danh sách các bảng dữ liệu đang được kết nối.
- *(🖼️ Ảnh minh họa: Screenshot tổng quan giao diện Power Query).*

## Giao diện Power Query Editor (Phần 2)
- **Data Preview (Xem trước dữ liệu):** Khu vực trung tâm hiển thị trực tiếp bảng dữ liệu đang xử lý.
- **Applied Steps (Các bước đã áp dụng):** Khung bên phải - \textbf{Tính năng đáng giá nhất!}. Ghi lại toàn bộ lịch sử thao tác giống như một cuốn băng ghi hình.
- Có thể hoàn tác (Undo) bất kỳ bước nào chỉ bằng 1 cú click (dấu \texttt{X}).

---

# PHẦN 2: CÁC THAO TÁC DỌN DẸP CƠ BẢN (BASIC TRANSFORMATIONS)

## Tại sao không làm trực tiếp trên Excel?
- Khi sửa dữ liệu trực tiếp trên ô Excel, nếu lỡ làm sai sẽ rất khó khôi phục, và tháng sau phải làm lại từ đầu.
- **Power Query lưu lại quy trình (Applied Steps).** Tháng sau chỉ cần bấm \texttt{Refresh}, dữ liệu mới sẽ tự động chạy qua phễu lọc cũ.

## Thao tác 1 - Xóa cột thừa (Removing Columns)
- Báo cáo kết xuất từ phần mềm thường kèm theo rất nhiều cột mã hệ thống không cần thiết cho kế toán.
- **Thực hành:** Nhấn chuột phải vào tiêu đề cột $\rightarrow$ \texttt{Remove}.
- Lợi ích: Làm nhẹ file, tăng tốc độ tính toán.

## Thao tác 2 - Đổi kiểu dữ liệu (Changing Data Types)
- Đây là nguyên nhân hàng đầu gây lỗi VLOOKUP! (Số hóa đơn lưu dạng Text vs lưu dạng Number).
- **Thực hành:** Click vào biểu tượng định dạng ở tiêu đề cột (ABC, 123, 📅) $\rightarrow$ Chọn \texttt{Whole Number}, \texttt{Text} hoặc \texttt{Date}.

## Thao tác 3 - Lọc các dòng bị lỗi (Filtering Rows)
- Loại bỏ các dòng tiêu đề rác của hệ thống hoặc các dòng trống.
- **Thực hành:** Bấm vào nút mũi tên trên tiêu đề cột $\rightarrow$ Bỏ chọn \texttt{(null)} hoặc \texttt{Blank}.
- Giống hệt Filter trong Excel nhưng quá trình này được lưu vĩnh viễn vào bộ máy tự động.

## Thao tác 4 - Thay thế giá trị (Replace Values)
- Giúp sửa các lỗi sai chính tả hàng loạt. (Ví dụ: "Hà nôi", "HN", "Ha Noi" $\rightarrow$ Sửa chung thành "Hà Nội").
- **Thực hành:** Chuột phải vào tiêu đề $\rightarrow$ \texttt{Replace Values} $\rightarrow$ Nhập \texttt{Value To Find} và \texttt{Replace With}.

## Thao tác 5 - Tách cột (Split Column)
- Ví dụ: Cột tên ghi là "Nguyễn Văn A - KT" cần tách riêng Tên và Phòng ban.
- **Thực hành:** Chọn \texttt{Split Column} $\rightarrow$ \texttt{By Delimiter} (Ký tự phân cách: dấu gạch ngang \texttt{-}).

## Thao tác 6 - Trim \& Clean
- Xóa khoảng trắng thừa (Leading/Trailing spaces) bằng \texttt{Trim}.
- Xóa các ký tự không in được bằng \texttt{Clean}.
- Đặc biệt hữu dụng với dữ liệu tải xuống từ hệ thống ngân hàng (Bank Statements).

## Giới thiệu ngôn ngữ M (M Code)
- Dành cho người muốn tìm hiểu sâu.
- Các thao tác kéo thả của bạn thực chất được Power Query tự động dịch thành ngôn ngữ lập trình "M" (Formula Bar).
- Bạn **KHÔNG** cần biết code M, nhưng nếu biết, bạn có thể chỉnh sửa sâu hơn.

---

# PHẦN 3: HỢP NHẤT DỮ LIỆU (APPEND \& MERGE)

## Nghệ thuật Hợp nhất dữ liệu
- Trong thực tế, dữ liệu không bao giờ nằm sẵn trong 1 bảng đẹp đẽ.
- Hợp nhất theo chiều dọc: **Append Queries**.
- Hợp nhất theo chiều ngang: **Merge Queries**.

## Gộp bảng theo chiều dọc (Append Queries)
- **Bài toán:** Kế toán có 12 file Excel (từ tháng 1 đến tháng 12). Cần gộp thành 1 bảng duy nhất để làm báo cáo năm.
- **Giải pháp Power Query:** Dùng \texttt{Append Queries}. Các file có cùng cấu trúc cột sẽ tự động xếp chồng lên nhau.
- *(🖼️ Ảnh minh họa: AI Generated - Hai khối lego xếp chồng lên nhau).*

## Lợi ích cực lớn của Append
- So với Copy-Paste thủ công: Nếu tháng sau có thêm file "Tháng 13", chỉ cần quăng file vào thư mục và bấm \texttt{Refresh}, dữ liệu tự cập nhật báo cáo!

## Gộp bảng theo chiều ngang (Merge Queries)
- Bản nâng cấp hoàn hảo của VLOOKUP.
- **Bài toán:** Bạn có bảng Hóa Đơn chứa \texttt{CustomerID}, và bảng Khách Hàng chứa \texttt{CustomerName}. Cần mang tên KH vào bảng Hóa Đơn.
- *(🖼️ Ảnh minh họa: AI Generated - Hai bảng dữ liệu móc nối với nhau qua chiếc ổ khóa).*

## Cách thực hiện Merge Queries
- Chọn \texttt{Merge Queries}.
- Chọn bảng A và bảng B.
- **Bước quan trọng nhất:** Click chọn cột \textbf{Khóa ngoại (Foreign Key)} và \textbf{Khóa chính (Primary Key)} khớp nhau giữa 2 bảng.

## Tại sao Merge lại "ăn đứt" Vlookup?
- VLOOKUP rất nặng, làm file Excel bị treo nếu có hàng trăm ngàn dòng.
- VLOOKUP chỉ tìm từ trái sang phải.
- Merge Queries xử lý ngầm, siêu nhẹ, không tốn ô Excel để tính toán, tốc độ cực nhanh.

## Pivot \& Unpivot (Xoay và Bỏ xoay dữ liệu)
- Dữ liệu bị trình bày sai cấu trúc (Các tháng nằm ngang thành từng cột thay vì nằm dọc).
- **Thực hành:** Dùng lệnh \texttt{Unpivot Columns} để đưa các cột tháng về chuẩn 1 cột "Thuộc tính" và 1 cột "Giá trị". Sẵn sàng làm Pivot Table!

---

# PHẦN 4: LAB - THỰC HÀNH KẾ TOÁN (APPLY IT)

## LAB 1: Case Study - Super Scooters
- **Bối cảnh:** Hãng sản xuất xe scooter "Super Scooters" vừa chuyển đổi hệ thống Database.
- Hệ thống chia thành 4 bảng: Locations, SalesOrders, Employee, Customer.
- *(🖼️ Ảnh minh họa: Bảng dữ liệu của Super Scooters từ sách gốc).*

## Nhiệm vụ LAB 1
- Xác định \textbf{Primary Key} (Khóa chính) của từng bảng.
- Xác định \textbf{Foreign Key} (Khóa ngoại) kết nối bảng SalesOrders với bảng Customer.

## Phân tích LAB 1 - Bảng Locations \& Employee
- \textbf{Locations Table:}
  - Primary Key: \texttt{LocationNumber} (Không thể trùng lặp).
- \textbf{Employee Table:}
  - Primary Key: \texttt{EmployeeNumber}.

## Phân tích LAB 1 - Bảng SalesOrders
- \textbf{SalesOrders Table:}
  - Primary Key: \texttt{SalesOrderNumber} (Mỗi đơn hàng có mã duy nhất).
  - Foreign Keys: \texttt{ItemNumber}, \texttt{CustomerNumber}, \texttt{EmployeeNumber}, \texttt{LocationNumber}. 
  - (Các khóa ngoại này giúp truy xuất thông tin từ các bảng vệ tinh).

## LAB 2: Xử lý Hóa đơn Bán hàng
- **Tình huống:** Kế toán được gửi một file dữ liệu "Báo cáo bán hàng thô". Cột "Tên Khách Hàng" vừa có tên, vừa có mã số ở đằng sau (Nguyễn Văn A - KH001). Cột "Doanh thu" bị định dạng là Text.
- **Yêu cầu:** Hãy làm sạch nó.

## Các bước giải quyết LAB 2 (Live Demo)
1. Import dữ liệu vào Power Query (Get Data).
2. Dùng \texttt{Split Column by Delimiter} (-) để tách cột Tên và Mã khách hàng.
3. Chọn cột Doanh thu, đổi Data Type sang \texttt{Decimal Number}.
4. Close \& Load để xuất bảng sạch ra Excel.

## Kỹ năng tạo tham số (Parameters) nâng cao
- Giúp truy vấn có tính động (Dynamic).
- Vd: Thay vì tạo bộ lọc cố định "Năm 2025", ta tạo Parameter "Năm". Người dùng có thể nhập số "2026" và toàn bộ luồng xử lý tự động đổi theo năm mới.

## Load to Data Model (Mô hình Dữ liệu)
- Sau khi Clean dữ liệu, ta xuất ra đâu?
- \textbf{Tùy chọn 1 (Table):} Xuất ra bảng Excel bình thường (Nặng máy nếu quá 1 triệu dòng).
- \textbf{Tùy chọn 2 (Create Connection Only \& Add to Data Model):} Lưu ngầm trong bộ nhớ, dùng để tạo Pivot Table trực tiếp, xử lý mượt mà hàng triệu dòng!

## Best Practices (Thực hành tốt nhất) khi dùng Power Query
- Đặt tên Queries (Bảng) có ý nghĩa (Vd: \texttt{tbl\_DanhSachKhachHang}).
- Ghi chú các bước thao tác phức tạp (Chuột phải vào Applied Step $\rightarrow$ \texttt{Properties} $\rightarrow$ \texttt{Description}).
- Thường xuyên kiểm tra lại các bước (Test Your Queries) trước khi Load.

---

# PHẦN 5: TỔNG KẾT \& Q\&A

## Tổng kết Kiến thức Buổi Thực Hành
- Power Query là công cụ tự động hóa quá trình chuẩn hóa (Clean) và biến đổi (Transform) dữ liệu No-code số 1 hiện nay.
- Thay thế hoàn hảo cho các thao tác Copy-paste, VLOOKUP nặng nề.
- Applied Steps giúp bạn xây dựng **"Nhà máy tự động dọn rác"**. Lần sau chỉ việc bấm Refresh!

## Hỏi \& Đáp (Q\&A)
- Các câu hỏi thường gặp:
  - "Power Query có tốn phí không?" $\rightarrow$ Không, tích hợp sẵn trong Excel 2016 trở lên.
  - "Macbook có dùng được Power Query không?" $\rightarrow$ Có, Excel for Mac hiện đã hỗ trợ Power Query (dù giao diện hơi khác Windows).

## Bài tập về nhà
- Nhận file dữ liệu "Sales\_DirtyData.xlsx" từ giảng viên.
- Hãy dùng Power Query để:
  1. Loại bỏ các dòng trống.
  2. Viết hoa chuẩn chữ cái đầu tên khách hàng.
  3. Load ra một Pivot Table báo cáo tổng doanh thu theo khách hàng.

## Kết thúc Buổi 2
- \begin{center} \Huge \textbf{Thank You!} \end{center}
- Hãy thực hành ngay trên máy tính của bạn, vì "Thực hành là cách duy nhất để làm chủ Dữ liệu".
