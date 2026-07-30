## 2.2 Các Hàm Bảng Tính Phân Tích Lượng Lớn Dữ Liệu Như Thế Nào?

**MỤC TIÊU HỌC TẬP 2 (LEARNING OBJECTIVE 2)**
**Giải thích cách các hàm giúp trả lời các câu hỏi phân tích dữ liệu.**

Phân tích dữ liệu thường bao gồm việc thực hiện các tính toán như cộng tổng các số tiền, đếm các mục dữ liệu, và tính toán số trung bình. Các tính toán được sử dụng thường xuyên thường được tích hợp sẵn vào phần mềm phân tích dưới dạng các **hàm (functions)**, tức là các công thức được xác định trước để thực hiện các tính toán. Một ví dụ là hàm `SUM` trong Microsoft Excel giúp cộng một dải các số trong các hàng hoặc các cột.

Các hàm giúp cho việc phân tích nhanh chóng lượng lớn dữ liệu mà không cần phải viết các công thức phức tạp. Thực tế, một trong những thuộc tính mạnh mẽ nhất của Microsoft Excel là các hàm được tích hợp sẵn để thực hiện tính toán. Hãy nhớ rằng các hàm phổ biến nhất và logic đằng sau chúng cũng áp dụng cho các phần mềm khác ngoài Microsoft Excel. Ví dụ, các hàm có thể được sử dụng trong các công cụ phân tích và trực quan hóa như Power BI và Tableau. Hiểu cách các hàm này hoạt động, và quan trọng hơn, là khi nào nên sử dụng chúng, là một kỹ năng phân tích dữ liệu cốt lõi.

### Các Hàm Cơ bản cho Phân tích Dữ liệu (Basic Functions for Data Analysis)

Hình minh họa 2.11 mô tả một số hàm Excel cơ bản được sử dụng trong phân tích dữ liệu:
- Tên hàm xuất hiện ở cột đầu tiên.
- Cột thứ hai hiển thị đối số của hàm (function argument), đó là cú pháp cần thiết để gọi hàm cùng với dải (range) và tiêu chí (criteria) để áp dụng cho nó. Tất cả các hàm Excel bắt đầu bằng một dấu bằng (=), tiếp theo là loại hàm được thực hiện, và sau đó là dấu ngoặc đơn chỉ định các đối số cho hàm. Ví dụ, để tính tổng một cột số trong cột C từ hàng 2 đến hàng 245, hàm sẽ là: `=SUM(C2:C245)`.
- Cách hàm tính toán được mô tả trong cột thứ ba.

**HÌNH MINH HỌA 2.11 (ILLUSTRATION 2.11) Các Hàm Microsoft Excel Cơ Bản**

![ILLUSTRATION 2.11](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.11.png)

Quay trở lại với ví dụ về dữ liệu của trường đại học, Hình minh họa 2.12 hiển thị hộp đối số hàm cho hàm `COUNTIF` được sử dụng để xác định trường đại học sở hữu bao nhiêu máy bơm (pumps). Có hai tùy chọn nhập liệu để thực thi các hàm được minh họa:
- Nhập trực tiếp đối số hàm vào một ô trên bảng tính, hoặc
- Sử dụng hộp **Function Arguments** (Đối số hàm).

**HÌNH MINH HỌA 2.12 (ILLUSTRATION 2.12) Hộp Đối số Hàm COUNTIF của Dữ liệu Tài sản Đại học**

![ILLUSTRATION 2.12](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.12.png)

Để mở hộp thoại:
- Nhấp vào biểu tượng `fx` cạnh thanh công thức ô, nằm phía trên bảng tính (xem biểu tượng `fx` màu xanh lá cây trong Hình minh họa 2.13).
- Tiếp theo, hộp nhập liệu Function Arguments như trong Hình minh họa 2.12 sẽ xuất hiện trên màn hình.
- Điền dải ô (range) và tiêu chí (criteria), rồi chọn OK. Công thức cho hàm sau đó sẽ xuất hiện (Hình minh họa 2.13). Lưu ý rằng tiêu chí (trong ví dụ này là "Pump") phải được gõ trong dấu ngoặc kép. Điều này áp dụng cho bất kỳ tiêu chí nào không phải là một tham chiếu ô hoặc một con số.

**HÌNH MINH HỌA 2.13 (ILLUSTRATION 2.13) Tìm Biểu tượng Đối số Hàm**

![ILLUSTRATION 2.13](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.13.png)

Các hàm Excel này có thể giúp phân tích nhanh các tập dữ liệu, đặc biệt khi chúng rất lớn. Bây giờ hãy áp dụng các hàm này để trả lời các câu hỏi từ một tập dữ liệu về tài sản cố định.

### Áp dụng Các Hàm Cơ bản của Excel (Applying Excel Basic Functions)

> **Data** Chúng ta sẽ sử dụng tập dữ liệu tài sản của trường đại học (Hình minh họa 2.14) để minh họa cách các hàm có thể giúp hiểu dữ liệu.

**HÌNH MINH HỌA 2.14 (ILLUSTRATION 2.14) Dữ liệu Tài sản Đại học**

![ILLUSTRATION 2.14](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.14.png)

Tập dữ liệu được tạo ra từ tệp University Asset Data:
- Mỗi hàng trong tập dữ liệu đại diện cho một tài sản duy nhất thuộc sở hữu của trường đại học.
- Các cột đại diện cho các thuộc tính của mỗi tài sản.

Có 13.127 hàng dữ liệu trong bảng tính này, nên việc quét chúng bằng mắt là không thể. Thay vào đó, hãy tận dụng các hàm Excel có sẵn. Tưởng tượng bạn chịu trách nhiệm xem xét các tài sản cố định cho trường đại học. Bạn có thể muốn đặt các câu hỏi được liệt kê trong Hình minh họa 2.15. Mỗi câu hỏi đều có thể được trả lời bằng một hàm Excel.

**HÌNH MINH HỌA 2.15 (ILLUSTRATION 2.15) Câu hỏi, Hàm và Câu trả lời Sử dụng Dữ liệu Tài sản Đại học**

![ILLUSTRATION 2.15](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.15.png)

Hình minh họa 2.15 sử dụng các hàm SUM, COUNTA, COUNTIF, SUMIF, và COUNTBLANK. Có thể sử dụng hàm SUMIFS hoặc COUNTIFS không?

Nếu câu hỏi là có bao nhiêu máy tính mà trường đại học đã mua vào năm 2023, thì hãy sử dụng hàm `COUNTIFS` vì có hai tiêu chí. Hãy nhớ rằng hàm `COUNTIFS` yêu cầu chỉ định dải ô để áp dụng cho tiêu chí đầu tiên (thiết bị máy tính). Tiêu chí tiếp theo là các giao dịch mua được thực hiện vào năm 2023, và dải ô sẽ là cột ghi ngày mua (dates acquired). Hình minh họa 2.16 hiển thị hộp Đối số Hàm cho hàm `COUNTIFS` và kết quả của nó.

**HÌNH MINH HỌA 2.16 (ILLUSTRATION 2.16) Các Đối số Hàm cho hàm COUNTIFS**

![ILLUSTRATION 2.16](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.16.png)

Hộp hàm tạo ra một công thức:
`=COUNTIFS(D2:D13127,"Computer Equipment",F2:F13127,">12/31/2022",F2:F13127,"<1/1/2024")`

Để chỉ lấy dữ liệu của năm 2023, tạo hai tiêu chí trong đối số hàm:
- Đầu tiên, ngày tháng phải lớn hơn 31 tháng 12 năm 2022 (Criteria2).
- Thứ hai, ngày tháng phải nhỏ hơn 1 tháng 1 năm 2024 (Criteria3).

Bằng cách bao gồm các tiêu chí đó trong đối số, chỉ những kết quả thuộc năm 2023 mới được hiển thị.

Các hàm cơ bản của Excel rất hữu ích để trả lời các câu hỏi có một câu trả lời duy nhất hoặc một câu trả lời với một chiều dữ liệu (dimension). **Các chiều dữ liệu (Dimensions)** là các biến hoặc các trường khác có thể được sử dụng để phân tích sâu (drill down) hoặc phân tách các thước đo phân tích. Nói cách khác, các chiều dữ liệu được sử dụng khi có một câu hỏi cụ thể về một khía cạnh cụ thể của dữ liệu.

Ví dụ, một câu hỏi về việc có bao nhiêu máy tính được mua trong năm 2023 chỉ có một chiều dữ liệu – máy tính trong năm 2023. Thế còn một câu hỏi có nhiều hơn một chiều dữ liệu thì sao? Sẽ ra sao nếu chúng ta muốn biết tổng chi phí cho mỗi danh mục tài sản thay vì chỉ riêng máy tính trong một năm cụ thể? Câu hỏi đó có nhiều hơn một chiều dữ liệu bởi vì nó liên quan đến mọi danh mục tài sản và tất cả các năm. Chúng ta sẽ thảo luận cách giải quyết các câu hỏi đa chiều trong phần tiếp theo.

---

### Áp dụng (Apply It 2.2)
**Phân tích Các Giao dịch Bán hàng với Các Hàm Excel (Analyze Sales Transactions with Excel Functions)**

**Kế toán Tài chính (Financial Accounting)** | **Kế toán Quản trị (Managerial Accounting)**

> **Data** Super Scooters sản xuất và bán bốn mẫu xe tay ga đứng: Celeritas, Captain, Lazer, và Kicks. Khách hàng của họ trải dài từ các công ty chia sẻ xe tay ga lớn đến các nhà bán lẻ nhỏ. Người giám sát của bạn đã đưa cho bạn (một kế toán viên của công ty) một danh sách các câu hỏi cần trả lời bằng cách sử dụng tập dữ liệu Super Scooters. Dưới đây là một phần của Các Giao dịch Bán hàng của Super Scooters cho các năm 2023–2025. Có 3.645 giao dịch trong cơ sở dữ liệu bán hàng.

Hãy giải thích hàm Microsoft Excel nào phù hợp nhất để trả lời các câu hỏi sau đây về dữ liệu bán hàng của Super Scooters.
1. Tổng doanh thu gộp (tính bằng đô la) là bao nhiêu?
2. Tổng doanh thu gộp (tính bằng đô la) cho năm 2023 là bao nhiêu?
3. Có bao nhiêu giao dịch bán hàng cho mẫu xe Lazer?
4. Doanh thu gộp trung bình cho mẫu xe Celeritas trong năm 2023 là bao nhiêu?
5. Có bao nhiêu chiếc mẫu xe Captain màu xanh lá (green) đã được bán?
6. Nếu Super Scooters muốn thêm một cột để chỉ ra liệu số ngày lưu bãi (days on the lot) có lớn hơn 50 ngày hay không, hàm nào sẽ phù hợp?

![Apply It 2.2](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.2.png)
