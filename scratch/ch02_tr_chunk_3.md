## 2.3 Làm Thế Nào Chúng Ta Tổ Chức Các Tập Dữ Liệu Cho Phân Tích?

**MỤC TIÊU HỌC TẬP 3 (LEARNING OBJECTIVE 3)**
**Minh họa cách các pivot tables tổ chức và lọc dữ liệu.**

Bạn vừa học cách sử dụng các hàm để trả lời các câu hỏi với một chiều dữ liệu. Mặc dù bạn có thể sử dụng nhiều hàm để trả lời các câu hỏi liên quan đến nhiều chiều dữ liệu, nhưng sẽ hiệu quả hơn nếu trước tiên sử dụng một kỹ thuật tổ chức dữ liệu trên tập dữ liệu.

Tổ chức dữ liệu là quá trình sắp xếp lại dữ liệu để làm cho nó dễ hiểu hơn. **Pivot table** là một công cụ tóm tắt và sắp xếp lại các cột và hàng dữ liệu đã chọn trong một bảng tính, cơ sở dữ liệu, hoặc chương trình kinh doanh thông minh (business intelligence). Các Pivot tables có thể nhanh chóng sắp xếp lại dữ liệu để giúp trả lời nhiều câu hỏi kinh doanh quan trọng. Hãy nhớ lại từ phần góc nhìn chuyên gia mở đầu chương rằng Josh đã cần phải sử dụng một pivot table để tổ chức lại một bảng tính với 450.000 hàng dữ liệu. Thật khó tin rằng Josh có thể phân tích dữ liệu bảng tính một cách hiệu quả mà không cần đến pivot table.

Các ví dụ ở đây sử dụng Microsoft Excel để minh họa cách tạo và lọc một pivot table. (Lưu ý rằng các pivot table được tạo trong phần mềm này thường được dán nhãn là PivotTables). Mặc dù các minh họa sử dụng Excel PivotTables, các kỹ thuật này cũng được sử dụng trong các phần mềm phân tích dữ liệu khác. Ví dụ, chúng rất hữu ích khi tạo các biểu đồ trực quan. Bất kể bạn sử dụng công cụ phân tích dữ liệu nào, việc hiểu các chức năng cơ bản của việc tạo ra các pivot table hữu ích và cách lọc chúng là điều cần thiết.

### Sử dụng Pivot Tables

Vừa mạnh mẽ vừa dễ sử dụng, pivot table cũng là một trong những công cụ phổ biến nhất mà bạn sẽ sử dụng trong sự nghiệp kế toán của mình. Nó có năm thành phần chính:
1. **Các trường (Fields):** Các phần tử dữ liệu có sẵn để sử dụng trong pivot table.
2. **Các cột (Columns):** Khi một trường được chọn cho khu vực cột, chỉ những giá trị duy nhất của trường đó được liệt kê ngang qua phía trên cùng.
3. **Các hàng (Rows):** Khi một trường được chọn cho khu vực hàng, nó điền vào khu vực đó dưới dạng cột đầu tiên. Tất cả các giá trị hàng đều là các giá trị duy nhất và các giá trị trùng lặp bị loại bỏ.
4. **Các giá trị (Values):** Mỗi giá trị được giữ trong một ô của pivot table và hiển thị thông tin đã được tóm tắt. Ví dụ là tổng (sum), trung bình (average), hoặc đếm (count).
5. **Các bộ lọc (Filters):** Áp dụng một điều kiện giới hạn cho toàn bộ bảng.

Một khi bạn biết những điều cơ bản về việc tạo một pivot table trong Microsoft Excel, bạn có thể sử dụng công cụ này để trả lời các câu hỏi kế toán.

#### Tạo một Microsoft Excel PivotTable
Thực hiện theo các bước sau:
1. Mở bảng tính chứa dữ liệu cần tóm tắt.
2. Nhấp vào bất kỳ ô nào trong dữ liệu (ví dụ: ô đầu tiên ở hàng A trong Hình minh họa 2.17).
3. Nhấp vào tùy chọn **Insert** trên thanh menu (ribbon) phía trên cùng.
4. Một hộp tùy chọn nhập liệu **PivotTable** sẽ xuất hiện ở trên cùng bên trái của màn hình (Hình minh họa 2.17).

**HÌNH MINH HỌA 2.17 (ILLUSTRATION 2.17) Bảng tính Excel Dữ liệu Tài sản Đại học**

![ILLUSTRATION 2.17](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.17.png)

Khi tùy chọn này được chọn, một hộp thoại mới sẽ mở ra có tên là **PivotTable from table or range** (Hình minh họa 2.18).
5. Đảm bảo rằng dải ô **Table/Range** trong hộp *Select a table or range* phản ánh toàn bộ dữ liệu cần bao gồm. (Hãy nhớ bao gồm cả các tiêu đề cột). Chọn **New Worksheet** và nhấp **OK** (Hình minh họa 2.18).

**HÌNH MINH HỌA 2.18 (ILLUSTRATION 2.18) Hộp thoại Tạo PivotTable của Excel**

![ILLUSTRATION 2.18](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.18.png)

6. Điều này sẽ mở ra một bảng tính mới. Một vùng làm việc **PivotTable** trống sẽ xuất hiện ở bên trái, và hộp **PivotTable Fields** dùng để tạo PivotTable sẽ nằm ở bên phải (Hình minh họa 2.19).

**HÌNH MINH HỌA 2.19 (ILLUSTRATION 2.19) Vùng làm việc PivotTable trống**

![ILLUSTRATION 2.19](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.19.png)

Sử dụng hộp PivotTable Fields để chọn những gì sẽ xuất hiện trong PivotTable. Kéo tên cột vào một trong các khu vực rows, columns, values, hoặc filters.

> **Data** Hãy sử dụng PivotTables để trả lời các câu hỏi dữ liệu về tài sản của trường đại học. Nếu bạn đang xác minh tổng chi phí cho mỗi danh mục tài sản, bạn có thể muốn trả lời các câu hỏi sau:
> - Câu hỏi 1: Tổng số dư cho các tài sản trong mỗi danh mục là bao nhiêu?
> - Câu hỏi 2: Tổng số lượng tài sản trong mỗi danh mục là bao nhiêu?

#### Tìm Tổng Số dư theo Danh mục
Trả lời câu hỏi đầu tiên bằng cách tìm tổng số dư theo danh mục.
1. Kéo `Category` vào khu vực **Rows**.
2. Kéo `Amount` vào khu vực **Values**. Khi đó, `Σ Values` trong khu vực Columns sẽ tự động được Excel tạo ra.
3. Excel sẽ điền các giá trị cho mỗi danh mục vào cột thứ hai của bảng tính.

Hình minh họa 2.20 hiển thị PivotTable kết quả.

**HÌNH MINH HỌA 2.20 (ILLUSTRATION 2.20) Excel PivotTable cho Câu hỏi 1: Tổng Số dư theo Danh mục là bao nhiêu?**

![ILLUSTRATION 2.20](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.20.png)

4. Excel sẽ mặc định tính tổng (sum) của giá trị đó. Có thể thay đổi loại thước đo bằng cách nhấp vào mũi tên chỉ xuống trong trường `Sum of Amount` và chọn thước đo mong muốn (Hình minh họa 2.21).

**HÌNH MINH HỌA 2.21 (ILLUSTRATION 2.21) Hộp thoại Value Field Settings của Excel PivotTable**

![ILLUSTRATION 2.21](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.21.png)

Một tính năng hữu ích khác của hộp thoại Value Field Settings là khả năng thay đổi định dạng số (number format) trong PivotTable.

#### Xác định Tổng số Lượng Tài sản
Để xác định tổng số lượng tài sản trong mỗi danh mục (Câu hỏi 2), sử dụng PivotTable Excel đầu tiên:
1. Kéo `AssetTagID` vào khu vực **Values**.
2. Nhấp vào mũi tên chỉ xuống, chọn **Value Field Settings**, và chọn **Count**.
   Dữ liệu có thể được tóm tắt bằng một số phép tính khác nhau. Câu hỏi yêu cầu về số lượng tài sản mỗi danh mục, nên chọn **Count**.
3. Excel điền vào cột tiếp theo của bảng với số lượng theo danh mục tài sản.

Kết quả được hiển thị trong Hình minh họa 2.22.

**HÌNH MINH HỌA 2.22 (ILLUSTRATION 2.22) Excel PivotTable cho Câu hỏi 2: Tổng Số lượng Tài sản trong Mỗi Danh mục là bao nhiêu?**

![ILLUSTRATION 2.22](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.22.png)

### Lọc Pivot Tables (Filtering Pivot Tables)
Một cách để tập trung vào một khía cạnh cụ thể của dữ liệu trong PivotTable là sử dụng một bộ lọc (filter). Áp dụng bộ lọc có nghĩa là chỉ những dữ liệu phù hợp với tiêu chí của nó mới được hiển thị. Có ba cách để lọc trong Excel:
- Áp dụng các tiêu chí lọc vào khu vực **Filter**.
- Sử dụng **AutoFilter** trong trường Row của PivotTable.
- Chèn một hoặc nhiều **slicers**.

> **Data** Việc trả lời câu hỏi dữ liệu tài sản thứ ba sẽ minh họa cho mỗi tùy chọn lọc:
> Câu hỏi 3: Tổng số tiền mua sắm theo danh mục được thực hiện vào năm 2022 là bao nhiêu?

#### Áp dụng Các Tiêu chí Lọc vào Hộp Filter Field
Để khám phá tổng số tiền mua sắm theo danh mục cho năm 2022, hãy tạo một PivotTable hiển thị các tài sản được mua trong năm 2022 theo danh mục:
1. Kéo `Category` vào Rows, và kéo `Amount` vào Values.
2. Trọng tâm là các tài sản được mua trong năm 2022, vì vậy hãy đưa `Years` vào khu vực **Filters**.
3. Từ `Years` ở cột đầu tiên và từ `ALL` ở cột thứ hai lúc này sẽ xuất hiện ở phần trên cùng của PivotTable.
4. Nhấp vào mũi tên chỉ xuống bên cạnh `ALL` sẽ tạo ra một hộp thả xuống để chọn các năm cần lọc (Hình minh họa 2.23).

**HÌNH MINH HỌA 2.23 (ILLUSTRATION 2.23) Cách Lọc trong một Excel PivotTable**

![ILLUSTRATION 2.23](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.23.png)

Hình minh họa 2.24 cho thấy kết quả của việc lọc các tài sản được mua vào năm 2022.

**HÌNH MINH HỌA 2.24 (ILLUSTRATION 2.24) PivotTable Trả lời cho Câu hỏi 3: Tổng Chi phí của Các Tài sản Được Mua trong năm 2022 là bao nhiêu?**

![ILLUSTRATION 2.24](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.24.png)

#### Sử dụng một Row Auto Filter
Các bộ lọc cũng có thể được tạo ra trong một Excel PivotTable với chức năng **Auto Filter** cho các hàng. Trong ví dụ này, câu hỏi là có bao nhiêu tiền đã được chi cho thiết bị máy tính (Computer Equipment) trong năm 2022.
1. Thay vì thêm một danh mục vào khu vực Filter, hãy nhấp vào mũi tên chỉ xuống ở **Row Labels** để hiển thị các lựa chọn lọc khác.
2. Hình minh họa 2.25 hiển thị hộp thả xuống xuất hiện sau đó. Tại đây, bỏ chọn tất cả và chỉ chọn các danh mục tài sản muốn lọc.

**HÌNH MINH HỌA 2.25 (ILLUSTRATION 2.25) Excel PivotTable để Lọc chỉ cho Thiết bị Máy tính**

![ILLUSTRATION 2.25](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.25.png)

3. Trong ví dụ này, chỉ có Thiết bị Máy tính (Computer Equipment) được chọn. PivotTable kết quả được hiển thị trong Hình minh họa 2.26.

**HÌNH MINH HỌA 2.26 (ILLUSTRATION 2.26) Excel PivotTable Hiển thị Riêng Thiết bị Máy tính Được mua trong năm 2022**

![ILLUSTRATION 2.26](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.26.png)

Tùy chọn auto filter nhanh chóng cô lập một mục cụ thể. Hai tùy chọn auto filter khác là **Label Filters** và **Value Filters**. Hình minh họa 2.27 cho thấy các tùy chọn khả dụng sau khi chọn Label Filters.

**HÌNH MINH HỌA 2.27 (ILLUSTRATION 2.27) Label Filters của Excel PivotTables**

![ILLUSTRATION 2.27](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.27.png)

Làm nổi bật và nhấp vào một trong các tùy chọn dưới Label Filters sẽ mở ra một hộp thoại để chèn tham số của bộ lọc. Ví dụ, chọn **Equals** và nhập "Computer Equipment" vào hộp thoại (Hình minh họa 2.28) sẽ đạt được kết quả giống như Hình minh họa 2.26.

**HÌNH MINH HỌA 2.28 (ILLUSTRATION 2.28) Hộp thoại Equals của Excel PivotTable Label Filter**

![ILLUSTRATION 2.28](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.28.png)

Điều gì sẽ xảy ra nếu mục tiêu là lọc dữ liệu sao cho chỉ năm danh mục tài sản đứng đầu xuất hiện?
1. Sử dụng **Value Filters** và chọn tùy chọn cho **Top 10...** (Hình minh họa 2.29).

**HÌNH MINH HỌA 2.29 (ILLUSTRATION 2.29) Các Tùy chọn Value Filter của PivotTable**

![ILLUSTRATION 2.29](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.29.png)

2. Một hộp thoại sẽ mở ra cho phép thay đổi bộ lọc thành trên cùng (top) hoặc dưới cùng (bottom) và số lượng mục cần hiển thị.
Trong Hình minh họa 2.30, "Top 5" theo "Sum of amount" đã được chọn.

**HÌNH MINH HỌA 2.30 (ILLUSTRATION 2.30) Hộp Nhập liệu PivotTable Value Filter Cho Các Giá trị Hàng đầu**

![ILLUSTRATION 2.30](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.30.png)

Excel PivotTable kết quả được hiển thị trong Hình minh họa 2.31.

**HÌNH MINH HỌA 2.31 (ILLUSTRATION 2.31) Kết quả của PivotTable Value Filter Cho 5 Số tiền Hàng đầu**

![ILLUSTRATION 2.31](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.31.png)

Thế còn việc lọc theo nhiều chiều dữ liệu cùng một lúc thì sao?

#### Sử dụng Các Slicers để Lọc Dữ liệu
Việc lọc đồng thời nhiều chiều dữ liệu thường được gọi là **slicing**, hoặc slice and dice, đây là quá trình chia nhỏ dữ liệu thành các phần nhỏ hơn hoặc kiểm tra nó từ nhiều góc nhìn khác nhau. **Slicers** là một công cụ phân tích phân tách các thước đo phân tích kết quả theo các chiều dữ liệu đã chọn. Tất cả các phần mềm phân tích dữ liệu đều có khả năng slicing:
- Microsoft Excel và Power BI sử dụng slicers.
- Trong Tableau, việc này được thực hiện thông qua các bộ lọc tương tác (interactive filters).

Trong tất cả các loại phần mềm, các slicer tùy chỉnh tương tác với một tập dữ liệu bằng cách cung cấp một hiển thị trực quan các bộ lọc khả dụng. Hình minh họa 2.32 chỉ ra nơi có thể tìm thấy tùy chọn thêm slicer trong Microsoft Excel.

**HÌNH MINH HỌA 2.32 (ILLUSTRATION 2.32) Thêm Slicers vào PivotTables**

![ILLUSTRATION 2.32](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.32.png)

1. Nhấp vào trong PivotTable và chọn **Insert Slicer** từ menu. Điều này sẽ mở một hộp với tất cả các trường của PivotTable.
2. Chọn các trường cho các slicers. Nếu mục tiêu là xác định số tiền đã chi cho mỗi danh mục tài sản theo năm, thì hãy slice dữ liệu theo danh mục tài sản và năm. Để làm điều này, hãy chọn `Category` và `AcquisitionDate`.

Hình minh họa 2.33 hiển thị các slicers kết quả. Một cái dành cho danh mục (Category) và cái kia dành cho năm (Years).

**HÌNH MINH HỌA 2.33 (ILLUSTRATION 2.33) Slicers của PivotTable Giúp Khám Phá Tổng Số tiền theo Danh mục và Năm**

![ILLUSTRATION 2.33](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.33.png)

Trong Hình minh họa 2.33, nhấp vào `Computer Equipment` trong slicer Category và `2022` trong slicer Years sẽ mang lại một PivotTable với tổng số thiết bị máy tính được mua trong năm 2022.

Slicers cũng có thể được thêm vào Power BI bằng cách chọn công cụ slicer trong **Visualizations** (Hình minh họa 2.34).

**HÌNH MINH HỌA 2.34 (ILLUSTRATION 2.34) Pivot Table Slicers Sử dụng PowerBI**

![ILLUSTRATION 2.34](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.34.png)

Tiếp theo, hãy chọn Category để tạo các slicer cho danh mục và lặp lại đối với các slicer AcquisitionDate. Hình minh họa 2.35 cho thấy kết quả.

**HÌNH MINH HỌA 2.35 (ILLUSTRATION 2.35) Các Slicers của Power BI cho Category và Year**

![ILLUSTRATION 2.35](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.35.png)

Bởi vì các chức năng của pivot table tóm tắt dữ liệu để tìm ra câu trả lời một cách nhanh chóng cho các câu hỏi của chúng ta, việc tạo ra các pivot table là một kỹ năng phân tích dữ liệu cốt lõi mà bạn sẽ sử dụng thường xuyên trong sự nghiệp của mình.

---

### Áp dụng (Apply It 2.3)
**Phân tích Bán hàng với Excel PivotTables (Analyze Sales with Excel PivotTables)**

> **Data** **Kế toán Tài chính** | **Kế toán Quản trị** Người giám sát của bạn tại Super Scooters đã yêu cầu bạn phân tích doanh số bán hàng cho năm 2025 và doanh thu cho tất cả các năm. Hãy tạo một Excel PivotTable để xác định những điều sau:
1. Tổng doanh thu gộp (tính bằng đô la) cho mỗi địa điểm (location) trong năm 2025 là bao nhiêu?
2. Doanh thu gộp trung bình cho mỗi mẫu xe trong năm 2025 là bao nhiêu?
3. Tổng doanh thu mỗi năm là bao nhiêu?

**GIẢI PHÁP (SOLUTION)**
1. Chọn (hoặc kéo) các trường: `Location` vào **Rows**, `Gross Sales` vào **Values**, và `Year` vào **Filters**. Trong bộ lọc năm, hãy chọn 2025.

![Apply It 2.3_1](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.3_1.png)

2. Đảm bảo rằng `Model` ở khu vực **Rows**, `Gross Sales` ở khu vực **Values**, và `Year` ở khu vực **Filters** (chọn 2025). Nhấp vào mũi tên chỉ xuống bên cạnh `Sum of Gross Sales` và chọn **Value Field Settings** để thay đổi từ Sum thành Average.

![Apply It 2.3_2](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.3_2.png)

3. Kéo trường `Year` vào khu vực **Rows** thay vì Filters. Xóa Model khỏi khu vực Rows và định dạng khu vực **Values** thành Sum.

![Apply It 2.3_3](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.3_3.png)
