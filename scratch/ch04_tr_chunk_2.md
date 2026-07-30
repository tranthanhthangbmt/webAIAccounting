**MỤC TIÊU HỌC TẬP 2 (LEARNING OBJECTIVE 2)**
**Mô tả cách phát triển một chiến lược dữ liệu.**

Sẽ dễ dàng hơn để đưa ra những quyết định tốt hơn khi chúng ta có những thông tin cần thiết. Mỗi học kỳ, những sinh viên biết được mục tiêu giáo dục và nghề nghiệp của mình có thể chọn các khóa học chuẩn bị cho họ tốt nghiệp và bắt đầu sự nghiệp. Ví dụ, sinh viên chuyên ngành kế toán không cần phải học cùng các khóa học với sinh viên chuyên ngành giáo dục. Ý tưởng tương tự cũng áp dụng khi phát triển một chiến lược (strategy) để chọn dữ liệu trong phân tích dữ liệu. Một dự án phân tích dữ liệu thành công phụ thuộc vào việc lựa chọn dữ liệu phù hợp (relevant) và thích hợp (appropriate) cho mục tiêu của dự án, tôn trọng các đặc điểm và thang đo (measurement scales) của dữ liệu, và kiểm soát các rủi ro dữ liệu cố hữu (inherent data risks).

### Xác định Dữ liệu Phù hợp (Identify Appropriate Data)

Dữ liệu có thể được coi là phù hợp cho phân tích khi chúng có tính liên quan (relevant), có sẵn (available), và các đặc điểm phù hợp với các yêu cầu của phương pháp phân tích. Dữ liệu phù hợp có thể là dữ liệu nội bộ, bên ngoài, hoặc sự kết hợp của cả hai:
- **Dữ liệu nội bộ (Internal data):** được tạo ra bên trong tổ chức, chẳng hạn như dữ liệu bán hàng, dữ liệu mua hàng, dữ liệu hàng tồn kho, dữ liệu khách hàng, và dữ liệu nhà cung cấp. Dữ liệu nội bộ thường có thể dễ dàng được kiểm soát và xác minh hơn bởi một tổ chức.
- **Dữ liệu bên ngoài (External data):** được thu thập từ các nguồn bên ngoài tổ chức. Dữ liệu này có thể bao gồm dữ liệu thời tiết, dữ liệu địa lý, và dữ liệu đối thủ cạnh tranh có sẵn công khai. Việc sử dụng dữ liệu bên ngoài có phần rủi ro hơn vì chúng ta thường không thể biết dữ liệu có chính xác hoặc đầy đủ hay không. Tuy nhiên, dữ liệu bên ngoài có thể cung cấp những hiểu biết (insights) mà chỉ riêng dữ liệu nội bộ không thể cung cấp.

Sau khi xác định các lựa chọn dữ liệu có sẵn và phù hợp, các đặc điểm của các tập dữ liệu (data sets) khả thi cần được xác minh xem có phù hợp với phân tích đã lên kế hoạch hay không.

### Đánh giá Các Trường và Nguồn Dữ liệu (Evaluate Data Fields and Sources)

Một tập dữ liệu (data set) là một tập hợp các cột và hàng dữ liệu có sẵn để phân tích. Việc hiểu các đặc điểm của một tập dữ liệu là rất quan trọng vì, ví dụ, các thước đo và kiểm định thống kê thường yêu cầu các đặc điểm dữ liệu nhất định hoặc một lượng điểm dữ liệu tối thiểu. Việc vi phạm các yêu cầu về dữ liệu đối với các thước đo và kiểm định này có thể đe dọa đến tính chính xác (accuracy), độ tin cậy (reliability), và mức ý nghĩa (significance) của các kết quả phân tích.

Hãy sử dụng một ví dụ để đánh giá tác động mà dữ liệu có thể mang lại đối với phân tích. Hình minh họa 4.8 cho thấy tập dữ liệu hàng tồn kho của công ty sản xuất 3D WeMakeIt, Inc.

![ILLUSTRATION 4.8](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.8.png)

Các cột riêng lẻ trong một tập dữ liệu được gọi là các trường (fields), và nếu nguồn dữ liệu là một cơ sở dữ liệu, các cột được gọi là các thuộc tính (attributes). Mỗi cột mô tả và thể hiện một đặc điểm, một mô tả, hoặc một khía cạnh độc nhất của hiện tượng được thu thập trong tập dữ liệu. Các hàng trong tập dữ liệu từ một cơ sở dữ liệu là các bản ghi (records), đại diện cho tập hợp các cột chứa những mô tả về một sự xuất hiện duy nhất cho mục đích của tập dữ liệu. Trong Hình minh họa 4.8, hàng được tô sáng chứa tất cả thông tin về mặt hàng tồn kho *Superhero Fantastic Four Mister Fantastic* – mã hàng tồn kho, mô tả, danh mục sản phẩm, đơn giá, và số lượng hàng đang có. Mặt hàng tồn kho này thuộc nhóm ProductCategory #3, cho thấy rằng đây là một mô hình siêu anh hùng.

Các bản ghi, hoặc hàng, trong tập dữ liệu hàng tồn kho này đại diện cho các sản phẩm khác nhau được sản xuất trong mỗi dòng sản phẩm. Các cột mô tả từng sản phẩm hàng tồn kho cho tập dữ liệu hàng tồn kho của WeMakeIt, Inc. được liệt kê trong Hình minh họa 4.9.

![ILLUSTRATION 4.9](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.9.png)

Ngoài việc hiểu nội dung của các trường dữ liệu trong cơ sở dữ liệu kế toán, việc xem xét nguồn (source) của dữ liệu là rất quan trọng vì chất lượng dữ liệu trong các trường ảnh hưởng đến chất lượng của phân tích. Dữ liệu được tạo ra bởi một bên thứ ba trên trang web, được nhập bộ bởi nhân viên, hay được tự động gán bởi máy tính? Dữ liệu có liên quan đến một danh mục, một thước đo, hay một phép tính? Ví dụ, trong dữ liệu hàng tồn kho của WeMakeIt, Inc. ở Hình minh họa 4.9, dữ liệu của trường `InventoryCode` có thể là các số tuần tự tự động được gán bởi hệ thống AIS mỗi khi một sản phẩm hàng tồn kho mới được thêm vào. Vì con người không tạo ra giá trị của trường đó khi một hàng mới được thêm vào, chúng ta có thể tự tin rằng dữ liệu `InventoryCode` luôn chính xác. Hình minh họa 4.10 tóm tắt các nguồn trường dữ liệu nội bộ điển hình thường được sử dụng bởi các kế toán viên.

![ILLUSTRATION 4.10](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.10.png)

Trong ví dụ về tập dữ liệu của WeMakeIt, Inc., dữ liệu của cả trường `InventoryCode` và `ProductCategory` đều là dữ liệu thô chưa đo lường (non-measured raw data) đã được định dạng dưới dạng số học (numeric) và rời rạc (discrete), có nghĩa là chúng không liên tục (non-continuous) và sẽ không bao giờ có các giá trị thập phân. Các trường này không thể được sử dụng trong phân tích cho các phép tính toán học vì chúng liên quan đến các mã định danh duy nhất cho các mặt hàng tồn kho và nhóm danh mục sản phẩm của chúng. Nguồn dữ liệu của trường `InventoryDescription` cũng là một trường dữ liệu thô chưa đo lường được định dạng dưới dạng trường văn bản (text field), không thể được sử dụng trong các phép tính số học trong quá trình phân tích.

Các nguồn cho các trường dữ liệu như `UnitCost` và `NumberOnHand` thì khác biệt vì chúng là dữ liệu số thô được đo lường (measured raw numeric data), có thể được sử dụng trong các phép tính toán học.

Cuối cùng, `UnitCost` và `NumberOnHand` có thể được nhân với nhau trong một biểu thức để tính toán một trường mới trong một truy vấn được gọi là `TotalCost`. Nguồn trường mới này là dữ liệu được tính toán (calculated data) mà cũng có tính số học và có khả năng được sử dụng trong nhiều phép tính toán học khác nhau trong kế toán.

Thang đo lường (measurement scale) của một trường dữ liệu đề cập đến loại thông tin do dữ liệu cung cấp. Thang đo lường dữ liệu nên được xem xét khi thiết kế chiến lược dữ liệu, vì chúng ảnh hưởng đến việc các phân tích nào có thể được thực hiện trên dữ liệu đó. Các thang đo lường dữ liệu được chia thành bốn nhóm: định danh (categorical), thứ bậc (ordinal), khoảng (interval), hoặc tỷ lệ (ratio) (Hình minh họa 4.11).

![ILLUSTRATION 4.11](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.11.png)

**Góc nhìn Chuyên gia 4.2 (Professional Insight 4.2): Làm thế nào để bạn chọn Dữ liệu Tài chính cho Phân tích?**

Jadon là sinh viên chuyên ngành kế toán và tài chính, một vận động viên thể thao của trường, và là chủ tịch của tổ chức sinh viên thế hệ đầu tiên trong trường. Trong quá trình thực tập, anh ấy nhận ra sự nghiệp của mình sẽ liên quan đến phân tích dữ liệu về thông tin trên báo cáo tài chính nhiều như thế nào.

Vào ngày đầu tiên của kỳ thực tập mùa hè, tôi được giao nhiệm vụ tính toán 10 tỷ số tài chính cho 5 công ty trong cùng một ngành trong 3 năm gần nhất. Tôi phải tự mình tìm cách lấy dữ liệu và thực hiện các phép tính. Tôi đã áp dụng kinh nghiệm thể thao của mình để củng cố sự tự tin bằng cách tạo ra một kế hoạch (game plan). Đầu tiên, tôi phải chọn và thiết lập công cụ phân tích của mình.

Tôi đã chọn Excel với Analysis ToolPak và tạo một biểu mẫu dữ liệu thô (raw data template) dựa trên các tổng số tôi sẽ cần cho các tỷ số trong bảng tính (worksheet) đầu tiên. Tôi đã sao chép nó 5 lần cho dữ liệu thô của mỗi công ty. Tôi đã tạo một bảng tính khác cho tất cả các tính toán tỷ số dưới dạng các hàng, và các công ty sẽ là các cột, được nhóm theo từng năm. Tôi đã sắp xếp các tỷ số thành các nhóm khả năng sinh lời (profitability), thanh khoản (liquidity), và khả năng thanh toán (solvency). Tôi đã nhập các công thức tỷ số liên kết quay lại (tied back) các ô trong bảng tính dữ liệu thô và ghi chép lại các bước của mình trên một trang khác để ghi nhớ những lựa chọn của mình.

Tiếp theo, tôi phải tìm xem nên lấy dữ liệu ở đâu. Tôi đã vào dữ liệu xBRL của SEC, tải thông tin báo cáo tài chính xuống và nhập những gì tôi cần vào Excel. Một lợi ích bất ngờ của việc có tất cả các tỷ số trong một trang là nó giúp dễ dàng tạo các hình ảnh trực quan (visualizations) về kết quả của tôi. Tôi đã rất ngạc nhiên trước sự rõ ràng về những công ty có hiệu suất hoạt động tốt nhất và tệ nhất qua các hình ảnh trực quan này. Tôi đã lưu tệp của mình và gửi email cho sếp.

Chúng ta sẽ thảo luận về cách các thang đo lường dữ liệu ảnh hưởng đến các lựa chọn chiến lược phân tích ở phần sau của chương này. Tiếp theo, hãy kiểm tra các rủi ro và các kiểm soát liên quan đến chiến lược dữ liệu của chúng ta.

### Xem xét Các Rủi ro của Chiến lược Dữ liệu và Thực hiện Các Kiểm soát (Consider Data Strategy Risks and Implement Controls)

Một lợi ích khác của việc tài liệu hóa chiến lược dữ liệu trong một kế hoạch dự án là việc xem xét từng lựa chọn có thể giúp xác định ba rủi ro dữ liệu phổ biến có thể ảnh hưởng đến tính hợp lệ, độ chính xác và độ tin cậy của một phân tích (Hình minh họa 4.12).

![ILLUSTRATION 4.12](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.12.png)

Rủi ro đầu tiên là việc một mẫu (sample) được trích xuất từ một tổng thể (population) dữ liệu lớn hơn lại là một đại diện kém cho tổng thể cơ bản đó. Ví dụ, việc lựa chọn ngẫu nhiên các viên bi có màu sắc khác nhau có thể không phải là một mẫu đại diện chính xác cho các đặc điểm của tổng thể các viên bi (Hình minh họa 4.13).

![ILLUSTRATION 4.13](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.13.png)

Đó là lý do tại sao việc thực hiện các kiểm tra về tính đại diện của mẫu có thể xác minh tính hợp lệ của nó hoặc phát hiện điểm yếu đáng kể của nó trong việc đại diện cho các tổng thể của những viên bi.

Rủi ro thứ hai là khả năng đưa các điểm dữ liệu bất thường (unusual data points) vào một phân tích. Các điểm dữ liệu ngoại lai (outlier data points) là các điểm dữ liệu bất thường so với phần còn lại của dữ liệu trong một điểm hoạt động (trục x hoặc biến độc lập), chẳng hạn như số lượng đơn vị sản xuất, hoặc một mức giá trị kinh tế bất thường (trục y hoặc biến phụ thuộc), chẳng hạn như tổng chi phí hoặc tổng doanh thu. Kiểm soát tốt nhất để xác định các ngoại lai là trực quan hóa dữ liệu trên một đồ thị để kiểm tra xem liệu thước đo đó có khác biệt quá nhiều so với phần dữ liệu còn lại hay không. Các ngoại lai được xác định có thể được đo lường lại (nếu có thể) hoặc bị loại bỏ bằng một quy tắc logic và được tài liệu hóa (documented rule).

Rủi ro dữ liệu cuối cùng là một loạt các lỗi dữ liệu, hay dữ liệu rác (dirty data), có thể gây ra vấn đề cho việc phân tích dữ liệu. Dữ liệu rác bao gồm các dữ liệu bị thiếu, không hợp lệ, trùng lặp và được định dạng sai. Ví dụ, các đơn đặt hàng (purchase orders), hóa đơn, hoặc séc (checks) do công ty viết ra phải được ghi nhận theo thứ tự liên tiếp, không có số bị thiếu hoặc hai chứng từ có cùng một mã số nhận dạng. Các kiểm soát luôn phải kiểm tra dữ liệu rác trước khi tiến hành phân tích. Dữ liệu có thể được đối chiếu với các chứng từ nguồn, hoặc nếu không thể, được kiểm tra tính hợp lý (tested for reasonableness). Việc kiểm tra tính hợp lý có thể bao gồm việc kiểm tra các số thứ tự bị thiếu, số bị trùng lặp, hoặc xác minh xem dữ liệu có định dạng dự kiến hay các ký tự được chấp nhận hay không.

Khi dữ liệu đã được lựa chọn, đánh giá, và bất kỳ rủi ro nào được xác định và kiểm soát, bước tiếp theo là phát triển một chiến lược phân tích phù hợp với mục tiêu của dự án.

---

### Áp dụng (Apply It 4.2)
**Xác định Đặc điểm Dữ liệu (Identify Data Characteristics)**

**Hệ thống Thông tin Kế toán** Tremendous Toys gần đây đã phát triển một cơ sở dữ liệu để nắm bắt các chi phí tồn kho từ quá trình sản xuất của họ mỗi tuần. 
Dữ liệu đã được trích xuất từ các trường dữ liệu sau:

Hoàn thành bảng ba cột bằng cách điền thêm loại và thang đo lường của mỗi trường dữ liệu.

**GIẢI PHÁP (SOLUTION)**

| Tên trường (Field Name) | Loại trường (Field Type) | Thang đo lường (Field Measurement Scale) |
| --- | --- | --- |
| `ProductionRunNumber` | Dữ liệu thô chưa đo lường (Non-measured raw data) | Định danh (Categorical - Nominal) |
| `ProductionRunDate` | Dữ liệu thô chưa đo lường (Non-measured raw data) | Khoảng (Interval) |
| `NumberOfToysinRun` | Dữ liệu thô đo lường (Measured raw data) | Tỷ lệ (Ratio) |
| `ToyIDNumber` | Dữ liệu thô chưa đo lường (Non-measured raw data) | Định danh (Categorical - Nominal) |
| `DirectMaterialsUsed` | Dữ liệu thô đo lường (Measured raw data) | Tỷ lệ (Ratio) |
| `DirectLaborUsed` | Dữ liệu thô đo lường (Measured raw data) | Tỷ lệ (Ratio) |
| `OverheadCostApplied` | Dữ liệu được tính toán (Calculated data) | Tỷ lệ (Ratio) |
| `TotalRunCost` | Dữ liệu được tính toán (Calculated data) | Tỷ lệ (Ratio) |
| `TotalUnitCost` | Dữ liệu được tính toán (Calculated data) | Tỷ lệ (Ratio) |
