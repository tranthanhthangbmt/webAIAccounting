# KẾ HOẠCH SLIDE LÝ THUYẾT - DAY 2 (BUỔI 2)
**Tên bài:** NHẬN DIỆN & XỬ LÝ DỮ LIỆU KẾ TOÁN
**Định hướng:** Kế toán thực hành, Tư duy xử lý dữ liệu chuẩn hóa (Clean Data), Hiểu cấu trúc dữ liệu để sẵn sàng dùng AI.
**Nguồn dữ liệu:** *Data and Analytics in Accounting - Chapter 2: Foundational Data Analysis Skills*

**ĐỀ XUẤT NGUỒN ẢNH MINH HỌA:**
- **Lấy từ file DOCX (Sách gốc):** Dùng Python giải nén thư mục `word/media` để lấy sơ đồ Database, ảnh minh họa các loại Joins (Inner, Left, Right).
- **Chụp ảnh màn hình (Screenshot):** Bảng tính Excel lỗi (dữ liệu bẩn), giao diện Pivot Table cơ bản.
- **Sinh ảnh bằng AI:** Các slide concept trừu tượng (Dữ liệu bẩn vs Dữ liệu sạch, Người kế toán bơi trong biển dữ liệu).

---

# PHẦN 1: NHẬN DIỆN DỮ LIỆU TRONG KẾ TOÁN

## TRANG BÌA (Title Page)
- Tiêu đề chính: Trí tuệ Nhân tạo cho Kế toán
- Tiêu đề phụ: Buổi 2 - Nhận diện & Xử lý Dữ liệu Kế toán
- Tác giả: Đại học Đông Á
- *(🖼️ Ảnh minh họa: AI Generated - Luồng dữ liệu số nhị phân chuyển hóa thành biểu đồ tài chính)*

## Năng lực đạt được sau buổi học
- **Về Lý thuyết (LT):** Phân biệt được thế nào là Dữ liệu sạch (Clean Data) và Dữ liệu bẩn (Dirty Data); Hiểu nguyên lý cấu trúc cơ sở dữ liệu quan hệ (Relational Databases).
- **Về Thực hành (TH):** Áp dụng thành thạo các hàm cốt lõi và Pivot Tables trong Excel để tiền xử lý, làm sạch và tổng hợp dữ liệu chuẩn hóa, tạo nền tảng vững chắc để cấp cho hệ thống AI phân tích.
- **Về Tư duy nghề nghiệp:** Định hình tư duy "Garbage In, Garbage Out" (GIGO) - Nhận thức được dữ liệu kế toán sạch là điều kiện tiên quyết trước khi ứng dụng bất kỳ mô hình AI nào.

## Khởi động (Ice-breaker)
- Câu nói nổi tiếng: "Garbage in, garbage out" (GIGO) - Rác đầu vào thì rác đầu ra.
- AI dù thông minh đến đâu, nếu cấp cho nó dữ liệu sai lệch, nó sẽ đưa ra quyết định sai lầm.

## Tầm quan trọng của Dữ liệu trong Kế toán
- Kế toán không chỉ là "Ghi chép sổ sách" (Bookkeeping).
- Kế toán hiện đại là "Quản trị dữ liệu tài chính".
- Trước khi AI có thể phân tích, con người phải đảm bảo dữ liệu đã được cấu trúc đúng.

## Dữ liệu Sạch (Clean Data) là gì?
- Dữ liệu nguyên vẹn, chính xác, thống nhất về định dạng.
- Sẵn sàng để đưa vào phần mềm ERP hoặc hệ thống AI để phân tích ngay lập tức.
- *(🖼️ Ảnh minh họa: Bảng dữ liệu ngăn nắp, rõ ràng).*

## Dữ liệu Bẩn (Dirty Data) là gì?
- Là dữ liệu chứa lỗi, không nhất quán, thiếu sót hoặc định dạng sai.
- Chiếm đến 80% thời gian của Kế toán viên (chỉ để dọn dẹp số liệu cuối tháng).
- *(🖼️ Ảnh minh họa: Bảng dữ liệu lộn xộn, lỗi Font, định dạng ngày tháng lung tung).*

## Các loại "Dữ liệu Bẩn" phổ biến (Phần 1)
- **Sai định dạng (Formatting errors):** Ngày tháng (MM/DD/YYYY lẫn lộn DD/MM/YYYY).
- **Khoảng trắng thừa (Leading/Trailing Spaces):** " Công ty A " khác với "Công ty A". Máy tính sẽ hiểu là 2 đối tượng khác nhau.

## Các loại "Dữ liệu Bẩn" phổ biến (Phần 2)
- **Trùng lặp (Duplicates):** Cùng một khách hàng bị tạo thành 2 mã khách hàng do lỗi đánh máy.
- **Giá trị rỗng (Null / Missing values):** Đơn hàng không có mã số thuế, thiếu mã vùng.

## Hệ lụy của Dữ liệu Bẩn
- Lập báo cáo tài chính sai lệch.
- Ra quyết định kinh doanh sai (Tưởng lãi nhưng thực chất lỗ).
- Rủi ro phạt thuế (Compliance risks).

## Vai trò của Kế toán viên trong kỷ nguyên AI
- Không cần tự tay dọn dẹp dữ liệu (AI có thể làm).
- Nhưng phải **Nhận diện** được dữ liệu đang bị bẩn ở đâu để ra "Lệnh" (Prompt) cho AI dọn dẹp.

---

# PHẦN 2: TỔ CHỨC & LƯU TRỮ DỮ LIỆU (RELATIONAL DATABASES)

## Làm sao để lưu trữ khối lượng dữ liệu khổng lồ?
- Excel rất tốt, nhưng không thể chứa hàng triệu giao dịch mỗi ngày.
- Giải pháp: Cơ sở dữ liệu quan hệ (Relational Database).
- Đa số phần mềm kế toán (MISA, SAP, Oracle) đều chạy trên nền tảng này.

## Khái niệm Relational Database
- Lưu trữ dữ liệu trong các **Bảng (Tables)** riêng biệt thay vì dồn chung vào một bảng khổng lồ.
- Các bảng được liên kết với nhau theo logic nghiệp vụ.
- *(🖼️ Ảnh minh họa: Sơ đồ các bảng liên kết - Trích từ sách gốc DOCX).*

## Thành phần của một Bảng (Table)
- **Dòng (Row / Record):** Đại diện cho 1 đối tượng duy nhất (VD: 1 khách hàng, 1 hóa đơn).
- **Cột (Column / Attribute):** Các thuộc tính mô tả (Mã KH, Tên KH, Địa chỉ).

## Primary Key (Khóa chính) là gì?
- Mã định danh độc nhất cho mỗi dòng trong bảng.
- Ví dụ: Mỗi người chỉ có 1 số CCCD. Trong kế toán: Mã Khách Hàng (CustomerID), Số Hóa Đơn (Invoice Number).
- Không bao giờ được phép trùng lặp hoặc để trống (Null).

## Foreign Key (Khóa ngoại) là gì?
- Là một cột trong bảng này, nhưng lại trỏ tới Primary Key của bảng khác.
- Dùng để **tạo liên kết (Relationship)** giữa các bảng.
- Vd: Cột CustomerID trong bảng "Hóa đơn" là Khóa ngoại trỏ về bảng "Khách hàng".

## Liên kết dữ liệu (Joins)
- Khi dữ liệu nằm ở nhiều bảng, ta dùng "Join" để kết hợp chúng lại phục vụ lập báo cáo.
- Bốn loại phổ biến: Inner Join, Left Join, Right Join, Full Join.
- *(🖼️ Ảnh minh họa: Các vòng tròn Venn biểu diễn Joins - Lấy từ DOCX).*

## Ứng dụng của Inner Join trong Kiểm toán
- **Định nghĩa:** Chỉ lấy các dòng có dữ liệu khớp ở cả 2 bảng.
- **Câu hỏi kế toán:** "Có nhân viên nào có số điện thoại trùng với số điện thoại của Nhà cung cấp không?" (Dấu hiệu gian lận).

## Ứng dụng của Left / Right Join
- **Định nghĩa:** Lấy toàn bộ dữ liệu 1 bảng, và ghép phần khớp của bảng kia (phần không khớp sẽ báo Null).
- **Câu hỏi kế toán:** "Có hóa đơn mua hàng nào chưa được thanh toán không?" (Ghép bảng Hóa đơn và bảng Thanh toán).

---

# PHẦN 3: HÀM CƠ BẢN & TƯ DUY CHUẨN HÓA

## Từ lý thuyết đến thực hành (Functions)
- Trong thực tế SME, Excel vẫn là vua.
- Cần nắm vững tư duy sử dụng Hàm (Functions) để biến dữ liệu bẩn thành sạch.

## Hàm xử lý văn bản (Text Functions)
- Tác dụng: Khắc phục lỗi con người nhập liệu sai quy cách.
- **TRIM():** Cắt bỏ các khoảng trắng thừa.
- **UPPER() / PROPER():** In hoa toàn bộ hoặc in hoa chữ cái đầu. Đưa tên Công ty về chuẩn.

## Hàm Logic (Logical Functions)
- Tác dụng: Giúp rẽ nhánh, phân loại dữ liệu tự động.
- **IF():** Nếu [Điều kiện] đúng thì [A], sai thì [B].
- Vd: IF(Doanh thu > 1 tỷ, "Khách VIP", "Khách thường").

## Kết hợp AND / OR
- Đánh giá nhiều điều kiện cùng lúc.
- Vd: Cảnh báo nợ xấu (Nợ > 90 ngày) AND (Chưa có cam kết trả).

## Hàm tra cứu (Lookup Functions)
- Tác dụng: Tìm kiếm và ghép nối dữ liệu từ các bảng khác nhau (Tương đương việc Join trong Database).
- **VLOOKUP():** Tra cứu dọc. Rất phổ biến nhưng dễ lỗi.
- *(🖼️ Ảnh minh họa: Screenshot dùng Vlookup tìm Tên Hàng hóa từ Mã Hàng hóa).*

## Kỷ nguyên mới với XLOOKUP
- XLOOKUP khắc phục nhược điểm của Vlookup: Tìm kiếm hai chiều, tự động xử lý lỗi #N/A (báo giá trị Null).
- Nên ưu tiên dùng XLOOKUP trong kế toán hiện đại.

## Tư duy làm việc với hàm trong thời đại AI
- Kế toán không cần thuộc lòng cú pháp hàm phức tạp.
- Chỉ cần biết **"Nên dùng hàm loại gì"**. AI (ChatGPT/Copilot) sẽ viết cú pháp hàm chính xác cho bạn.

---

# PHẦN 4: TỔNG HỢP DỮ LIỆU (PIVOT TABLES)

## Vấn đề của Bảng dữ liệu phẳng (Flat Table)
- Bạn có 1 file Excel 450.000 dòng lịch sử giao dịch.
- Xếp yêu cầu: "Báo cáo ngay tổng doanh thu theo từng chi nhánh trong năm nay."
- Dùng hàm SUMIF sẽ rất lâu và nặng máy.

## Giải pháp: Pivot Table
- Công cụ mạnh mẽ nhất trong Excel để tóm tắt, nhóm (group) và tính toán dữ liệu khổng lồ chỉ bằng thao tác kéo thả (Drag \& Drop).
- Không cần viết bất kỳ dòng lệnh nào.

## Cơ chế hoạt động của Pivot Table
- Biến đổi dữ liệu chi tiết thành báo cáo tổng hợp.
- Thay đổi cấu trúc góc nhìn (Xoay - Pivot) dữ liệu tức thì.
- *(🖼️ Ảnh minh họa: Giao diện Fields của Pivot Table - Lấy từ DOCX/Screenshot).*

## Các thành phần của Pivot Table
- **Rows (Dòng):** Nhóm theo tiêu chí (Vd: Tên khu vực).
- **Columns (Cột):** Tách theo tiêu chí phụ (Vd: Từng quý).
- **Values (Giá trị):** Tính toán (SUM, COUNT, AVERAGE).

## Bộ lọc (Filtering \& Slicers)
- **Filters:** Lọc báo cáo để chỉ xem một phần dữ liệu (VD: Chỉ xem Khách hàng Doanh nghiệp, bỏ qua Cá nhân).
- **Slicers:** Bảng điều khiển trực quan giúp sếp tự bấm để lọc báo cáo mà không cần biết dùng Excel.
- *(🖼️ Ảnh minh họa: Slicer tương tác trực quan).*

## Ứng dụng Pivot Table trong Kế toán
- Lên bảng Cân đối phát sinh từ Nhật ký chung.
- Báo cáo Tuổi nợ (Aging report).
- Phân tích chi phí theo từng phòng ban/dự án.

## AI và Pivot Table
- Các phần mềm hiện nay (Excel Copilot) có thể tự động tạo ra các Pivot Table phù hợp chỉ qua một câu lệnh tiếng Anh.
- "Show me total sales by region in a pivot table."

---

# PHẦN 5: THỐNG KÊ MÔ TẢ & TRỰC QUAN HÓA

## Phân tích Dữ liệu là gì?
- Dữ liệu thô -> Xử lý (Sạch) -> Phân tích -> Thông tin chi tiết (Insights).
- Bước đầu tiên của phân tích là Thống kê mô tả (Descriptive Statistics).

## Các đại lượng đo lường vị trí (Location)
- **Mean (Trung bình):** Bị nhiễu bởi các giá trị ngoại lai cực lớn/nhỏ.
- **Median (Trung vị):** Phản ánh con số thực tế "nằm giữa".
- Ứng dụng: Xác định mức lương trung vị của nhân viên thay vì trung bình.

## Đo lường độ phân tán (Dispersion)
- **Variance \& Standard Deviation (Phương sai \& Độ lệch chuẩn).**
- Đo lường mức độ rủi ro hoặc biến động.
- Ứng dụng: Phân tích độ lệch của chi phí bảo hành thực tế so với định mức dự toán.

## Vì sao cần Trực quan hóa dữ liệu? (Data Visualization)
- Não bộ con người xử lý hình ảnh nhanh hơn 60.000 lần so với văn bản và các dãy số.
- Giúp Ban giám đốc "nhìn" thấy vấn đề trong vài giây.
- *(🖼️ Ảnh minh họa: Bảng số liệu nhàm chán vs Biểu đồ trực quan sinh động).*

## Lựa chọn Biểu đồ phù hợp (Phần 1)
- **Biểu đồ Cột (Bar/Column Chart):** So sánh giá trị giữa các hạng mục (Doanh thu các chi nhánh).
- **Biểu đồ Tròn (Pie Chart):** Thể hiện tỷ trọng (Cơ cấu chi phí sản xuất). Không dùng khi có quá nhiều mẩu nhỏ.

## Lựa chọn Biểu đồ phù hợp (Phần 2)
- **Biểu đồ Đường (Line Chart):** Thể hiện xu hướng theo thời gian (Biến động doanh số 12 tháng).
- **Biểu đồ Phân tán (Scatter Plot):** Tìm mối tương quan (Correlation) giữa 2 biến số (Ví dụ: Chi phí quảng cáo và Doanh số bán hàng).

## Trực quan hóa dữ liệu trong thực tiễn
- Các nền tảng như Tableau, Power BI đang trở thành kỹ năng bắt buộc cho Kế toán quản trị.
- Tích hợp biểu đồ trực tiếp vào Dashboard thời gian thực.

## Tổng kết Buổi 2
- Nền tảng: Hiểu về Relational Database.
- Công cụ: Dùng Hàm & Pivot Table để dọn dẹp, tổng hợp dữ liệu.
- Báo cáo: Dùng Thống kê mô tả và Biểu đồ để kể câu chuyện tài chính (Data Storytelling).
- **Tiền đề quan trọng:** Dữ liệu chuẩn thì các buổi sau dùng AI mới chính xác!
