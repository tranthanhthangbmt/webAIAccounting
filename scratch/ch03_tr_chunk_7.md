- Một mô hình bảng tính đánh giá những thay đổi và các sự kết hợp cụ thể của các yếu tố đầu vào và giả định của mô hình được gọi là phân tích what-if. Phân tích what-if là một cách dễ dàng để thay đổi các giá trị trong bảng tính và tính toán lại đầu ra.

**❻ Mô tả động lực và mục tiêu cho phân tích dữ liệu trong thực tiễn chuyên môn.**
Các lĩnh vực thực hành kế toán chuyên nghiệp chính có chung và cũng có những động lực duy nhất để thực hiện phân tích dữ liệu:
- Chuyên gia hệ thống thông tin kế toán có những động lực về quản trị, chiến lược, hoạt động, và tuân thủ.
- Kiểm toán viên có những động lực về tuân thủ chuyên môn, chất lượng, hãng kiểm toán (firm), và thị trường.
- Kế toán tài chính có những động lực từ cả các bên liên quan nội bộ và bên ngoài.
- Kế toán quản trị có những động lực về quản trị nội bộ, chiến lược, và hoạt động.
- Kế toán thuế có những động lực về tuân thủ chuyên môn, khách hàng, hãng kiểm toán (firm), và thị trường.

---

### Ôn tập Thuật ngữ Chính (Key Terms Review)
- Hệ số xác định (Coefficient of determination)
- Ràng buộc (Constraints)
- Hệ số tương quan (Correlation coefficient)
- Các biến quyết định (Decision variables)
- Biến phụ thuộc (Dependent variable)
- Các câu hỏi mô tả (Descriptive questions)
- Các câu hỏi chẩn đoán (Diagnostic questions)
- Mối quan hệ chức năng (Functional relationship)
- Các biến độc lập (Independent variables)
- Hàm tuyến tính (Linear function)
- Tối ưu hóa tuyến tính (Linear optimization)
- Hồi quy tuyến tính (Linear regression)
- Động lực (Motivation)
- Mục tiêu (Objective)
- Hàm mục tiêu (Objective function)
- Tối ưu hóa (Optimization)
- Các câu hỏi dự đoán (Predictive questions)
- Các câu hỏi đề xuất (Prescriptive questions)
- Thống kê hồi quy (Regression statistics)
- Biến (Variable)
- Phân tích What-if (What-if analysis)

---

### Hướng dẫn Thực hành (How To Walk-Throughs)

#### HOW TO 3.1: Tạo Bảng Đánh dấu (Highlight Table) trong Tableau
Bảng được hiển thị trong Hình minh họa 3.10 được tạo trong Tableau phiên bản 2021.1.2. Hãy tự tạo nó bằng cách làm theo các bước sau.
> **Những gì bạn cần:** **Data** File dữ liệu How To 3.1.

**BƯỚC 1:** Mở một worksheet (bảng tính) mới và kéo `Sold Date` vào Columns (Cột) và `Location` vào Rows (Hàng). Kéo `Gross Sales` vào vùng trống bên dưới số năm, hoặc vào biểu tượng Text trong phần Marks (Hình minh họa 3.37).

![ILLUSTRATION 3.37](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.37.png)

**BƯỚC 2:** Tạo một phép tính để tính toán sự thay đổi doanh số từ năm 2024 đến năm 2025. Bởi vì dữ liệu từ năm 2023 là không cần thiết và chúng ta chỉ quan tâm đến mẫu Celeritas, hãy tạo hai bộ lọc (filters). Đầu tiên, kéo `Model` vào hộp Filters. Điều này sẽ mở ra một hộp thoại (Hình minh họa 3.38).

![ILLUSTRATION 3.38](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.38.png)

Đánh dấu vào ô cho Celeritas và nhấp OK. Tiếp theo, kéo `Sold Date` vào Filter và chọn Years từ hộp thoại đầu vào (Hình minh họa 3.39).

![ILLUSTRATION 3.39](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.39.png)

Nhấp vào Next để xem các lựa chọn hộp thoại tiếp theo (Hình minh họa 3.40).

![ILLUSTRATION 3.40](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.40.png)

Chọn 2024 và 2025 rồi nhấp OK.

**BƯỚC 3:** Tạo phép tính. Việc nhấp vào mũi tên hướng xuống trong thẻ (pill) màu xanh lá cây cho Sum(Gross Sales) trong vùng Marks sẽ tạo ra một số tùy chọn (Hình minh họa 3.41).

![ILLUSTRATION 3.41](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.41.png)

Chọn tùy chọn Quick Table Calculation (Tính toán bảng nhanh), sau đó chọn Difference (Chênh lệch). Điều này sẽ thay đổi các cột trong bảng thành các mức chênh lệch (Hình minh họa 3.42).

![ILLUSTRATION 3.42](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.42.png)

**BƯỚC 4:** Để tạo bảng đánh dấu trong đó các màu tối hơn đại diện cho các số lớn hơn, hãy chọn loại biểu đồ đó từ các tùy chọn Show Me (Hiển thị cho tôi) ở góc trên cùng bên phải (Hình minh họa 3.43).

![ILLUSTRATION 3.43](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.43.png)

Bây giờ bảng sẽ trông giống như bảng trong Hình minh họa 3.44.

![ILLUSTRATION 3.44](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.44.png)

**BƯỚC 5:** Để chỉ hiển thị cột cho năm 2025, nhấp chuột phải vào 2024 trong cột và chọn Hide (Ẩn) (Hình minh họa 3.45).

![ILLUSTRATION 3.45](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.45.png)

Nhấp vào Hide chứ không phải Exclude. (Việc chọn Exclude - Loại trừ có nghĩa là phép tính sẽ không còn hoạt động nữa vì dữ liệu năm 2024 sẽ bị xóa).

**BƯỚC 6:** Sắp xếp các địa điểm theo thứ tự từ mức sụt giảm lớn nhất đến mức sụt giảm nhỏ nhất. Để làm điều đó, hãy nhấp vào 2025 ở đầu cột. Hộp sẽ xuất hiện như trong Hình minh họa 3.46.

![ILLUSTRATION 3.46](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.46.png)

Nhấp vào biểu tượng sắp xếp hiển thị thanh nhỏ nhất ở trên cùng. Sau đó, dữ liệu sẽ được sắp xếp từ số nhỏ nhất đến số lớn nhất (Hình minh họa 3.47).

![ILLUSTRATION 3.47](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.47.png)

**BƯỚC 7:** Định dạng cột chênh lệch thành đô la chẵn (whole dollars) bằng cách nhấp vào thẻ (pill) màu xanh lá cây Sum(Gross Sale) trong vùng Marks và chọn Format (Định dạng) (Hình minh họa 3.48).

![ILLUSTRATION 3.48](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.48.png)

Ở đây, định dạng mặc định có thể được đổi sang tiền tệ (currency).

**BƯỚC 8:** Tạo tiêu đề cho bảng trực quan hóa. Theo mặc định, Tableau sẽ đặt tên cho bảng trực quan hóa theo số sheet. Để thay đổi điều đó, nhấp chuột phải vào khu vực tiêu đề của sheet và sau đó chọn Edit Title (Chỉnh sửa Tiêu đề) (Hình minh họa 3.49).

![ILLUSTRATION 3.49](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.49.png)

Nhập tiêu đề vào ô xuất hiện (Hình minh họa 3.50).

![ILLUSTRATION 3.50](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.50.png)

---

#### HOW TO 3.2: Thực hiện Hồi quy (Regression) trong Microsoft Excel
Hình minh họa 3.18 là quy trình hồi quy được thực hiện trong Excel. Bạn có thể tạo nó bằng cách làm theo các bước sau.
> **Những gì bạn cần:** **Data** File dữ liệu How To 3.2.

**BƯỚC 1:** Công cụ Data Analysis trong thanh công cụ Data (Dữ liệu) có tùy chọn cho hồi quy (regression). Hình minh họa 3.51 hiển thị hộp thoại mở ra khi Data Analysis được chọn.

![ILLUSTRATION 3.51](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.51.png)

**BƯỚC 2:** Nhấp vào Regression, sau đó nhấp OK. Một hộp thoại Regression sẽ xuất hiện (Hình minh họa 3.52).

![ILLUSTRATION 3.52](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.52.png)

**BƯỚC 3:** `Input Y Range` dành cho biến phụ thuộc. Biến phụ thuộc là những gì sẽ được dự đoán. Trong ví dụ này, đó là cột D, Chi phí Bảo trì (Maintenance Expenses) (`$D$1:$D$37`). `Input X Range` dành cho các biến độc lập. Trong ví dụ này, có hai biến độc lập – Số Giờ Máy (Machine Hours) và Số Yêu cầu Bảo trì (Maintenance Requests) (`$B$1:$C$37`).
Chọn Labels (Nhãn) nếu hàng đầu tiên của dữ liệu là tiêu đề cột (hàng 1). Trong ví dụ này, kết quả sẽ nằm trong một trang tính (worksheet) mới. Cuối cùng, chọn Residuals, Standardized Residuals, Residual Plots và Normal Probability Plots. Các tùy chọn sai số (residuals) này sẽ được sử dụng để đánh giá các giả định hồi quy.

**BƯỚC 4:** Nhấp OK để xem kết quả hồi quy (Hình minh họa 3.53).

![ILLUSTRATION 3.53](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.53.png)
