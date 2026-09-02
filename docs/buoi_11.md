# Buổi 11: Thực hành AI Phân tích Dữ liệu Cơ bản (Cơ sở Dữ liệu Quan hệ, SQL & Excel)

<!-- tabs:start -->

#### ** 📚 Thuật ngữ & Khái niệm **

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Cơ sở dữ liệu quan hệ (Relational Database)</b></summary>
<br>

Phương thức lưu trữ dữ liệu dưới dạng các "Bảng" (Tables) nhỏ lẻ, phân tán thay vì gộp chung vào một file Excel khổng lồ. Các bảng này có thể "nói chuyện" và nối lại với nhau bằng hệ thống Khóa để chống dư thừa thông tin.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Khóa chính (Primary Key)</b></summary>
<br>

Cột có giá trị ĐỘC NHẤT cho mỗi hàng. Nó giống hệt như Số Căn cước Công dân, dùng để định danh duy nhất một bản ghi giao dịch trong bảng.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Khóa ngoại (Foreign Key)</b></summary>
<br>

Chiếc mỏ neo nằm ở bảng này nhưng lại lấy dữ liệu từ Khóa chính của bảng khác để liên kết và truy xuất thông tin chéo giữa các bảng.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Lệnh JOIN (Kết nối)</b></summary>
<br>

Từ khóa quyền lực nhất trong ngôn ngữ SQL, dùng để gom các bảng dữ liệu bị băm nhỏ lại với nhau thành một bức tranh toàn cảnh.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Inner Join (Kết nối trong / Phép giao)</b></summary>
<br>

Phương pháp nối chỉ lấy những dòng khớp nhau ở cả Bảng Trái và Bảng Phải. Kết quả trả ra một danh sách sạch sẽ, hoàn hảo nhưng thường là một "cái bẫy" che giấu sự bất thường hoặc gian lận.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Left Join (Kết nối trái)</b></summary>
<br>

Phương pháp nối ép hệ thống giữ lại TOÀN BỘ dữ liệu ở Bảng Trái và cố gắng nhét thông tin Bảng Phải vào. Đây là kỹ thuật cốt lõi trong kiểm toán để truy tìm các "kẻ cắp tàng hình" (như chi tiền cho công ty ma).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Giá trị NULL (Rỗng)</b></summary>
<br>

Lỗ hổng đen ngòm sinh ra khi dùng Left Join mà không tìm thấy dữ liệu khớp. Nhớ kỹ: NULL không phải là số 0. Một đống NULL ở cột tên nhà cung cấp là bằng chứng thép cho thấy tiền đang bị tuồn ra ngoài hệ thống!

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Hàm có điều kiện (SUMIFS / COUNTIFS)</b></summary>
<br>

Đóng vai trò như "Người bảo vệ khắt khe" đi dọc qua hàng trăm ngàn dòng giao dịch, chỉ cho phép cộng hoặc đếm những dòng thỏa mãn ĐỒNG THỜI mọi tiêu chí đa chiều đã đặt ra.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Pivot Table (Bảng tổng hợp)</b></summary>
<br>

Vũ khí tối thượng khi bạn nhận được dữ liệu thô nhưng không biết phải đặt câu hỏi gì. Dùng giao diện Kéo và Thả (Drag & Drop) để biến hình và gom nhóm bãi chiến trường 500.000 dòng thành báo cáo gọn gàng trong 10 giây.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Slicers (Bộ lọc trực quan)</b></summary>
<br>

Biến báo cáo Pivot tĩnh thành một Bảng điều khiển tương tác (Interactive Dashboard), cho phép biểu đồ tự động nhảy số theo thời gian thực (real-time) khi thuyết trình.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Ảo ảnh Số trung bình (Mean)</b></summary>
<br>

Một cái bẫy chết người của kiểm toán viên. Nó có sức mạnh "san bằng" mọi sự bất thường để cho ra một con số đẹp đẽ, sạch sẽ, hoàn toàn che giấu những khoản chi phí/thất thoát đột biến khổng lồ.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Thống kê mô tả (Descriptive Statistics)</b></summary>
<br>

Hành động đưa dữ liệu lên "bàn mổ" để đo lường mức độ bất thường bằng Phương sai (Variance) và Độ lệch chuẩn (Standard Deviation) thay vì chỉ tin vào số trung bình.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Hình dáng phân bổ (Skewness & Kurtosis)</b></summary>
<br>

Đo lường xem "ngọn núi dữ liệu" đó méo về bên trái hay bên phải (Độ lệch), nhọn hoắt (tập trung) hay thấp tè trải dài (Độ nhọn) để đánh giá tính rủi ro.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Phân bổ Lưng lạc đà (Bimodal)</b></summary>
<br>

Hiện tượng đồ thị thực tế có 2 đỉnh tách biệt ở 2 thái cực, chứng minh rằng con số trung bình nằm lọt thỏm dưới "thung lũng" không đại diện cho bất kỳ giao dịch thực tế nào.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Độ lệch chuẩn (Radar an ninh)</b></summary>
<br>

Vạch ra vùng không phận an toàn chứa 99% giao dịch bình thường. Ngay khi có một khoản chi lọt ra ngoài vùng này, "Radar chớp đỏ" báo hiệu kiểm toán viên phải lao vào kiểm tra chứng từ ngay lập tức.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Ngoại lệ (Outlier)</b></summary>
<br>

Dấu chấm giao dịch đơn độc bay lơ lửng cách xa đám đông, bị phát hiện bởi Radar an ninh. Gian lận và sai sót trọng yếu thường nằm ở đó.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Sự mù lòa nhận thức (Cognitive Blindness)</b></summary>
<br>

Điểm yếu của não bộ khi cố nhìn vào bảng dữ liệu hàng trăm ngàn dòng chữ/số để tìm lỗi. Phải khắc phục bằng cách sử dụng sức mạnh của vỏ não thị giác (Trực quan hóa).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Biểu đồ phân tán (Scatter Plot)</b></summary>
<br>

Mỗi giao dịch biến thành một dấu chấm trên trục tọa độ. Giúp mắt người chỉ mất 0,1 giây để nhận ra ngay lập tức các Ngoại lệ (Outlier) bất thường.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Biểu đồ tần suất (Histogram)</b></summary>
<br>

Dùng để vẽ nên hình dáng ngọn núi dữ liệu, giúp phát hiện xem phân bổ đó có bị cắt làm đôi (như lưng con lạc đà) che giấu 2 xu hướng cực đoan hay không.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Khám phá (Exploratory) và Giải thích (Explanatory)</b></summary>
<br>

Hai triết lý vẽ đồ thị. Khám phá là lộn xộn, chi tiết để chính bạn tự tìm ra lỗi. Giải thích là cắt bỏ mọi râu ria, chỉ làm nổi bật thông điệp duy nhất để mang vào phòng họp trình chiếu cho Sếp.

</details>



#### ** 🇬🇧 Tiếng Anh **

### 📄 Chương 2: Foundational Data Analysis Skills (Ann C. Dzuranin)

<object data="textbook/Buoi_11_Chương 2 (Foundational Data Analysis Skills).pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_11_Chương 2 (Foundational Data Analysis Skills).pdf#view=FitH" target="_blank">Nhấn vào đây để tải tài liệu PDF gốc</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_11_Chương 2 (Foundational Data Analysis Skills).pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về tài liệu PDF (Bản gốc tiếng Anh)</a></p>


#### ** 🇻🇳 Tiếng Việt **

# PHẦN I: TỔNG QUAN VÀ MỤC TIÊU HỌC TẬP (OVERVIEW & LEARNING OBJECTIVES)

### *(Kỹ năng phân tích dữ liệu cơ bản - Basic Data Analytics Skills)*

C H A PT E R 2 Dữ liệu cơ bản Kỹ năng phân tích Xem trước chương Bạn sẽ làm việc với dữ liệu và phần mềm phân tích dữ liệu trong suốt sự nghiệp của mình và một trong những công cụ phần mềm phổ biến nhất được sử dụng trong kế toán là Microsoft Excel. Như bạn sẽ thấy trong Tính năng Professional Insight, khả năng sử dụng Microsoft Excel để thao tác với các tập dữ liệu lớn là một tài sản to lớn cho các kế toán viên chuyên nghiệp mới được tuyển dụng. Trong khi kỹ năng Microsoft Excel là quan trọng là phần mềm không đủ mạnh để phân tích các tập dữ liệu cực lớn, vì vậy nó không phải là công cụ duy nhất được sử dụng để phân tích dữ liệu. Chương này giới thiệu một số kỹ năng mà bất kể công nghệ được sử dụng là nền tảng để thực hiện phân tích dữ liệu. Microsoft Excel được sử dụng để thể hiện nhiều kỹ năng phân tích dữ liệu cốt lõi, nhưng các chương tiếp theo cũng giới thiệu phần mềm phân tích dữ liệu như Power BI và Tableau. Sự kết hợp của sự hiểu biết cốt lõi về dữ liệu, trực quan hóa dữ liệu và kỹ năng phân tích mô tả là nền tảng để thực hiện nhiều hơn phân tích dữ liệu nâng cao. Cái nhìn chuyên sâu về chuyên môn: Bảng Pivot có thể giúp hiểu được như thế nào Tập dữ liệu lớn? Josh, một sinh viên kế toán cấp cao, giải thích việc học Microsoft Excel đã giúp anh như thế nào trong công việc của mình. thực tập. Nhiệm vụ đầu tiên của tôi là tạo một PivotTable trong Excel để thao tác một tệp dữ liệu khổng lồ với khoảng 450.000 bản ghi. Tôi vừa nhận được Mic- Chứng chỉ Excel cơ bản của rosoft Office Specialist khi tôi bắt đầu thực tập tại PwC. Nó cảm thấy tuyệt vời khi áp dụng những gì tôi học được trên lớp vào thế giới kinh doanh. Kinh nghiệm này sự hữu ích đã giúp tôi tự tin khi giao tiếp với cấp trên và giúp tôi xây dựng danh tiếng về độ tin cậy tại công ty của tôi. Giám đốc của tôi về khách hàng là Thor- rất ấn tượng với công việc của tôi và cộng sự cấp cao của tôi rất ngạc nhiên rằng tôi có thể để tập hợp một bảng toàn diện như vậy với rất ít kinh nghiệm.

Lộ trình chương MỤC TIÊU HỌC TẬP CHỦ ĐỀ ÁP DỤNG NÓ LO 2.1 Mô tả cách thức xử lý dữ liệu được lưu trữ và trích xuất từ ​​ cơ sở dữ liệu quan hệ.

- Cơ sở dữ liệu quan hệ

- Nối các bàn Xác định chính và nước ngoài Phím (Ví dụ: Kế toán Hệ thống thông tin) LO 2.2 Giải thích cách thức hoạt động giúp trả lời phân tích dữ liệu câu hỏi.

- Các hàm cơ bản để phân tích dữ liệu

- Áp dụng các hàm cơ bản của Excel Phân tích giao dịch bán hàng với các hàm Excel (Ví dụ: Tài chính và Kế toán quản trị) LO 2.3 Minh họa cách xoay bảng sắp xếp và lọc dữ liệu.

- Sử dụng Bảng tổng hợp

- Lọc bảng tổng hợp Phân tích doanh số bán hàng bằng Excel PivotTable (Ví dụ: Tài chính và Kế toán quản trị) LO 2.4 Xác định mang tính mô tả các biện pháp được sử dụng để thực hiện dữ liệu phân tích.

- Biện pháp vị trí

- Biện pháp phân tán

- Số đo hình dạng

- Phân tích tương quan Sử dụng thống kê mô tả để Kiểm toán chi phí bảo hành (Ví dụ: Kiểm toán) LO 2.5 Tóm tắt dữ liệu như thế nào trực quan khám phá và giải thích dữ liệu.

- Hiểu các tập dữ liệu lớn

- Hình ảnh trực quan và thời điểm sử dụng chúng

---

# PHẦN II: CƠ SỞ DỮ LIỆU QUAN HỆ VÀ TRÍCH XUẤT DỮ LIỆU (RELATIONAL DATABASES & SQL - LO 2.1)

## 2.1 Khái niệm cơ sở dữ liệu quan hệ (Relational Database Concepts)

- Trực quan hóa Microsoft Excel Phân tích chi phí sản phẩm với Trực quan hóa dữ liệu (Ví dụ: Quản lý Kế toán) Dữ liệu Thẻ Dữ liệu xuất hiện trong chương khi có sẵn dữ liệu cho một ví dụ, hình minh họa hoặc ứng dụng trên nền tảng học tập trực tuyến của Wiley. Phần mềm phân tích dữ liệu liên tục thay đổi và có thể có nhiều phiên bản phần mềm mới hơn. được đưa ra trong chương này. Để biết thêm thông tin, hãy truy cập video đi kèm trên nền tảng học tập trực tuyến của Wiley. 2.1 Hiểu cách lưu trữ dữ liệu giúp trả lời các câu hỏi như thế nào? 2.1 Hiểu cách lưu trữ dữ liệu Trợ giúp Trả lời câu hỏi? MỤC TIÊU HỌC TẬP ➊ Mô tả cách dữ liệu được lưu trữ và trích xuất từ cơ sở dữ liệu quan hệ. Hiểu cách dữ liệu được lưu trữ là rất quan trọng để phân tích dữ liệu. Điều này là do loại phân tích có thể được thực hiện phụ thuộc vào dữ liệu được sử dụng cũng như việc xác định và trích xuất dữ liệu chúng ta cần đòi hỏi phải biết nó được lưu trữ như thế nào.

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/Illustration 2.2 is the database view of a university’s asset data table that contains data for the inventory of its assets..PNG" alt="Illustration 2.2 is the database view of a university’s asset data table that contains data for the inventory of its assets." style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">Illustration 2.2 is the database view of a university’s asset data table that contains data for the inventory of its assets.</div>

</div>

Cơ sở dữ liệu

Dữ liệu, bất kể loại hay định dạng nào, đều cần được lưu trữ ở đâu đó. Một cách để làm điều đó là trong cơ sở dữ liệu quan hệ, là tập hợp các dữ liệu có liên quan về mặt logic có thể được truy xuất, được thao tác và cập nhật để đáp ứng nhu cầu của người dùng. Hầu hết dữ liệu bạn sẽ làm việc với trong tài khoản của mình- sự nghiệp của bạn sẽ đến từ cơ sở dữ liệu quan hệ, nơi dữ liệu được lưu trữ trong các bảng riêng lẻ có thể được liên kết với nhau. Khi các bảng được liên kết, dữ liệu từ nhiều bảng có thể được truy cập. Một bảng trong cơ sở dữ liệu quan hệ lưu trữ dữ liệu có giá trị liên quan đến một đối tượng quan tâm, chẳng hạn như một nguồn lực kinh doanh, sự kiện hoặc đại lý. Bảng bao gồm các hàng và cột:

- Mỗi hàng đại diện cho một bản ghi hoặc một thể hiện của đối tượng của bảng.

- Các cột phản ánh các thuộc tính, là các trường dữ liệu mô tả các khía cạnh của hồ sơ (Minh họa 2.1).

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.1 Database Elements and Examples of Tables and Attributes.PNG" alt="ILLUSTRATION 2.1 Database Elements and Examples of Tables and Attributes" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.1 Database Elements and Examples of Tables and Attributes</div>

</div>

Các phần tử cơ sở dữ liệu Ví dụ về bảng Ví dụ về thuộc tính Tài nguyên: Có thể xác định được đối tượng có hiệu quả kinh tế giá trị cho đơn vị kinh doanh. Vật phẩm tồn kho

- Mã mặt hàng tồn kho con số

- Mô tả

- Chi phí

- Số lượng có sẵn Sự kiện: Một tổ chức hoạt động kinh doanh. Lệnh bán hàng

- Số đơn bán hàng

- Ngày lập đơn bán hàng

- ID khách hàng của người mua Đại lý: Đại diện cho người hoặc tổ chức về cái gì dữ liệu được thu thập. Nhân viên

- Mã số nhân viên

- Tên

- Địa chỉ

- Số điện thoại Hình minh họa 2.2 là khung nhìn cơ sở dữ liệu về bảng dữ liệu tài sản của một trường đại học chứa dữ liệu về việc kiểm kê tài sản của nó. Dữ liệu tài sản đại học ID thẻ nội dung Mô tả tài sản Số tiền ID danh mục Ngày mua lại Tài Sản Hữu ÍchCuộc Sống ID danh mục Thể loạiMô tả Hữu íchCuộc sống Khóa chính Khóa chính

2.1 Hiểu cách lưu trữ dữ liệu giúp trả lời các câu hỏi như thế nào? Mỗi hàng trong bảng hiển thị một nội dung có thể nhận dạng duy nhất. Các thuộc tính liên quan của nó là tổ chức được ghi trong mỗi cột dọc được liệt kê bên dưới tên bảng:

- AssetTagID: Số nhận dạng thẻ

- AssetDescription: Mô tả tài sản

- CategoryID: Số nhận dạng danh mục

- Số tiền: Nguyên giá tài sản

- AcquisitionDate: Ngày tài sản được mua Bảng AssetUsefulLife chứa thông tin liên quan đến danh mục nội dung. Mỗi hàng là một danh mục duy nhất và các cột là thuộc tính của danh mục đó:

- CategoryID: Mã số nhận dạng cho từng loại tài sản

- CategoryDescription: Mô tả danh mục

- Cuộc sống hữu ích: Thời gian hữu ích tính bằng năm của tài sản trong từng danh mục Có một ký hiệu cho khóa bên cạnh thuộc tính AssetTagID trong bảng đầu tiên và Catego- ryID trong bảng thứ hai. Ký hiệu này xác định khóa chính, là cột phải có một giá trị duy nhất cho mỗi hàng trong bảng. Trong bảng UniversityAssetData, mọi nội dung được xác định duy nhất bởi cột khóa chính AssetTagID. Trong AssetUsefulLife bảng, khóa chính là CategoryID. Mỗi hàng trong bảng AssetUsefulLife sẽ có một giá trị duy nhất Số ID danh mục. Để tính khấu hao tài sản, chúng ta cần thông tin về chi phí, thông tin về vòng đời hữu ích và tuổi của tài sản. Tuy nhiên, thông tin đó xuất hiện ở hai bảng khác nhau. Liên kết chúng yêu cầu một trường chung trong cả hai:

- Trường CategoryID có trong cả hai bảng.

- CategoryID là cột khóa chính trong bảng AssetUsefulLife.

- Trong bảng UniversityAssetData, CategoryID là cột khóa ngoại. Một khóa ngoại umn chứa dữ liệu giống như khóa chính của một bảng khác. Nó đã được lặp lại trong bảng thứ hai để các bảng có thể được liên kết trong mối quan hệ với nhau. Minh họa 2.3

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.3 Creating a Relationship Between Tables.PNG" alt="ILLUSTRATION 2.3 Creating a Relationship Between Tables" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.3 Creating a Relationship Between Tables</div>

</div>

hiển thị mối quan hệ liên kết hai bảng bằng thuộc tính CategoryID. Tại sao điều này lại quan trọng? Việc liên kết các bảng tạo ra một mối quan hệ cho phép kéo thông tin từ cả hai bảng và tạo các tính toán khấu hao cho mọi tài sản trong bảng dữ liệu tài sản. Dữ liệu tài sản đại học ID thẻ nội dung Mô tả tài sản Số tiền ID danh mục Ngày mua lại Tài Sản Hữu ÍchCuộc Sống ID danh mục Thể loạiMô tả Hữu íchCuộc sống Khóa chính Khóa chính Khóa ngoại

Mối quan hệ giữa các bảng

Tham gia các bảng Khi các trường chung sử dụng khóa chính và khóa ngoại được xác định trên các bảng, bước tiếp theo là cho cơ sở dữ liệu biết cách liên kết các bảng để trích xuất dữ liệu:

- Truy vấn là một yêu cầu hành động được thực hiện đối với cơ sở dữ liệu. Nó cung cấp các hướng dẫn máy tính để nối, thêm, cập nhật, xóa, truy xuất hoặc thao tác dữ liệu trong các bảng của nó. Truy vấn có thể được tạo và sử dụng một lần hoặc được lưu trữ để sử dụng lại sau này.

- Ngôn ngữ lệnh truy vấn tiêu chuẩn được sử dụng để quản lý cơ sở dữ liệu là Ngôn ngữ có cấu trúc Ngôn ngữ truy vấn (SQL). Viết mã SQL nằm ngoài phạm vi của chương này, nhưng đối với- May mắn thay, nhiều chương trình phần mềm có sẵn các ứng dụng tự động tạo Mã SQL cần thiết để truy vấn cơ sở dữ liệu. Truy xuất tất cả các trường dữ liệu cần thiết để hoàn thành một nhiệm vụ cụ thể đòi hỏi phải có sự hiểu biết cách nối các bảng dựa trên các cột mà chúng có chung. Các bảng được liên kết bằng cách tạo một phép nối kết hợp các hàng từ hai hoặc nhiều bảng dựa trên một cột có liên quan giữa chúng. Tham gia cũng được sử dụng trong phần mềm trực quan hóa và phần mềm phân tích dữ liệu khác khi có nhiều hơn một bảng dữ liệu được sử dụng trong phân tích. (Chúng tôi thảo luận về trực quan hóa dữ liệu chi tiết hơn ở cuối chương này và ở các chương sau.) Các phép nối phổ biến nhất là các phép nối trong, trái, phải và đầy đủ. Minh họa 2.4 tóm tắt-

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.4 Types of Joins.PNG" alt="ILLUSTRATION 2.4 Types of Joins" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.4 Types of Joins</div>

</div>

tăng cường các kết nối khác nhau và cung cấp một biểu diễn trực quan. Màu xanh tượng trưng cho kết quả của sự tham gia. Lưu ý rằng giá trị null không giống với giá trị 0. Một giá trị null là khi một giá trị không xác định hoặc bị thiếu.

Tham gia Mô tả Trình bày trực quan Nội tâm

- Chọn tất cả các hàng từ cả hai bảng bằng cách so khớp các giá trị.

- Kết quả sẽ không có giá trị null ở bất kỳ khóa nào cột. Bảng 1 Bảng 2 trái

- Trả về tất cả bản ghi từ bảng bên trái và bảng các bản ghi phù hợp từ bảng bên phải.

- Có thể có giá trị null nếu không có khớp giá trị ở bảng bên phải với bảng bên trái ghi lại. Bảng 2 Bảng 1 Đúng

- Trả về tất cả bản ghi từ bảng bên phải và các bản ghi trùng khớp từ bảng bên trái.

- Có thể trả về giá trị null nếu không có giá trị khớp ở bảng bên trái với bản ghi trong cái bàn bên phải. Bảng 1 Bảng 2 Đầy đủ

- Trả về tất cả các bản ghi khi có sự trùng khớp trong bảng bên trái hoặc bên phải.

- Giá trị rỗng có thể xuất hiện trong kết quả này nếu có không có bản ghi phù hợp giữa các bảng. Bảng 2 Bảng 1

2.1 Hiểu cách lưu trữ dữ liệu giúp trả lời các câu hỏi như thế nào? Chúng ta có thể minh họa cách các phép nối này hoạt động bằng một ví dụ. Bikes R Us là nhà bán buôn xe đạp đại lý. Hình minh họa 2.5 hiển thị hai bảng từ cơ sở dữ liệu của họ:

- Bảng bên trái là bảng Khách hàng, bảng Đơn hàng ở bên phải.

- CustomerID là khóa chính trong bảng Khách hàng.

- OrderID là khóa chính trong bảng Order. CustomerID là khóa ngoại. MINH HỌA 2.5 Bảng cơ sở dữ liệu của Bikes R Us

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.5 Bikes R Us Database Tables.PNG" alt="ILLUSTRATION 2.5 Bikes R Us Database Tables" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.5 Bikes R Us Database Tables</div>

</div>

Bảng khách hàng Quốc gia chu kỳ Vòng quay Cửa hàng xe đạp thị trấn nhỏ Creebo tắc kè Blunsom NY NC TX Cửa hàng ba môn phối hợp Nhẫn CA Tên công ty ID khách hàng Tên liên hệ tiểu bang 50012 50013 1/2/2025 2/2/2025 3/2/2025 $578,23 $982,99 1.563,32 USD 50014 50015 4/2/2025 300,12 USD 5/2/2025 $639,99 50016 Ngày đặt hàng ID đơn hàng Bảng đặt hàng Số tiền ID khách hàng Việc nối bên trong trên hai bảng này sẽ tạo ra một bảng có tất cả dữ liệu từ các bảng khớp trên trường CustomerID (Minh họa 2.6).

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.6 Results from an Inner Join for Bikes R Us.PNG" alt="ILLUSTRATION 2.6 Results from an Inner Join for Bikes R Us" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.6 Results from an Inner Join for Bikes R Us</div>

</div>

Tham gia nội bộ Quốc gia chu kỳ Quốc gia chu kỳ Vòng quay Creebo Creebo tắc kè NY NY NC Cửa hàng ba môn phối hợp Nhẫn CA Tên công ty ID khách hàng Tên liên hệ tiểu bang 50012 50013 1/2/2025 2/2/2025 3/2/2025 $578,23 $982,99 1.563,32 USD 50014 50015 4/2/2025 300,12 USD Ngày đặt hàng ID đơn hàng Số tiền Kết nối bên trong hiển thị thông tin khách hàng và đơn đặt hàng cho từng khách hàng có đã đặt hàng:

- Những kết quả này cho thấy khách hàng có CustomerID = 1003, Cửa hàng xe đạp Little Town, chưa thực hiện bất kỳ giao dịch mua hàng nào.

- OrderID 50016 không khớp trong bảng khách hàng với CustomerID = 102, vì vậy thứ tự đó không được phản ánh trong các bảng đã nối. Phép nối bên trái trả về tất cả các hàng từ bảng bên trái và sẽ hiển thị mọi dữ liệu khớp từ bảng bàn bên phải. Nếu không có hàng trùng khớp trong bảng bên phải thì các trường không khớp sẽ là null (Minh họa 2.7).

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.7 Results from a Left Join for Bikes R Us.PNG" alt="ILLUSTRATION 2.7 Results from a Left Join for Bikes R Us" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.7 Results from a Left Join for Bikes R Us</div>

</div>

tham gia Quốc gia chu kỳ Quốc gia chu kỳ Vòng quay Creebo Creebo tắc kè NY NY NC Cửa hàng xe đạp thị trấn nhỏ Blunsom TX Tên công ty ID khách hàng Tên liên hệ tiểu bang 50012 50013 1/2/2025 2/2/2025 KHÔNG CÓ $578,23 $982,99 KHÔNG CÓ KHÔNG CÓ KHÔNG CÓ ID khách hàng Cửa hàng ba môn phối hợp Nhẫn CA 3/2/2025 1.563,32 USD 50014 50015 4/2/2025 300,12 USD Ngày đặt hàng ID đơn hàng Số tiền

Phép nối đầy đủ được hiển thị trong Hình minh họa 2.9 hiển thị tất cả các bản ghi từ cả hai bảng:

- Lưu ý các giá trị null cho các trường trong bảng Đơn hàng cho CustomerID = 1003 và các giá trị null cho các trường bảng Khách hàng cho OrderID = 50016.

- Bất kỳ trường nào không khớp sẽ có giá trị null. Tham gia là cần thiết khi phân tích dữ liệu từ nhiều nguồn. Hình minh họa 2.10 cho thấy

ví dụ về một số câu hỏi mà kế toán viên có thể cần hỏi về dữ liệu và loại kết nối đó sẽ trả lời họ.

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.8 Results from a Right Join for Bikes R Us.PNG" alt="ILLUSTRATION 2.8 Results from a Right Join for Bikes R Us" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.8 Results from a Right Join for Bikes R Us</div>

</div>

Tham gia ngay Quốc gia chu kỳ Quốc gia chu kỳ Vòng quay Creebo Creebo tắc kè NY NY NC Tên công ty ID khách hàng Tên liên hệ tiểu bang 50012 50013 1/2/2025 2/2/2025 $578,23 $982,99 KHÔNG CÓ ID khách hàng KHÔNG CÓ KHÔNG CÓ KHÔNG CÓ 5/2/2025 $639,99 50016 Cửa hàng ba môn phối hợp Nhẫn CA 3/2/2025 1.563,32 USD 50014 50015 4/2/2025 300,12 USD Ngày đặt hàng ID đơn hàng Số tiền Phép nối bên phải trong Hình minh họa 2.8 hiển thị tất cả các lệnh từ bảng Order và bất kỳ lệnh khớp nào khách hàng từ bảng Khách hàng:

- Không có bản ghi khách hàng phù hợp cho CustomerID = 102, do đó các trường từ Bảng khách hàng sẽ có giá trị null cho bản ghi đó.

- Nếu không có hàng nào phù hợp ở bảng bên trái thì các trường sẽ có giá trị null. Một phép nối đầy đủ sẽ trả về tất cả các hàng từ cả hai bảng (Minh họa 2.9).

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.9 Results from a Full Join for Bikes R Us.PNG" alt="ILLUSTRATION 2.9 Results from a Full Join for Bikes R Us" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.9 Results from a Full Join for Bikes R Us</div>

</div>

Tham gia đầy đủ Quốc gia chu kỳ Quốc gia chu kỳ Vòng quay Creebo Creebo tắc kè NY NY NC Tên công ty ID khách hàng Tên liên hệ tiểu bang 50012 50013 1/2/2025 2/2/2025 $578,23 $982,99 KHÔNG CÓ ID khách hàng KHÔNG CÓ KHÔNG CÓ KHÔNG CÓ 5/2/2025 $639,99 50016 Cửa hàng ba môn phối hợp Nhẫn CA 3/2/2025 1.563,32 USD 50014 KHÔNG CÓ Cửa hàng xe đạp thị trấn nhỏ Blunsom TX KHÔNG CÓ KHÔNG CÓ KHÔNG CÓ 50015 4/2/2025 300,12 USD Ngày đặt hàng ID đơn hàng Số tiền Phép nối bên trái trong Hình minh họa 2.7 hiển thị tất cả các khách hàng từ bảng Khách hàng và

thông tin trùng khớp từ bảng Đơn hàng:

- CustomerID = 1003 được liệt kê trong liên kết này, nhưng vì không có thứ tự phù hợp nên kết quả cho các trường đơn hàng là null.

- OrderID = 50016 không được phản ánh trong kết quả của bảng đã nối. Không có ID khách hàng = 102 trong bảng Khách hàng, do đó bản ghi đó không được chọn khi tham gia. Phép nối phải trả về tất cả các hàng từ bảng bên phải và sẽ hiển thị mọi dữ liệu khớp từ bảng bảng bên trái (Minh họa 2.8).

2.1 Hiểu cách lưu trữ dữ liệu giúp trả lời các câu hỏi như thế nào?

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.10 Sample Data Analysis Questions and Appropriate Join.PNG" alt="ILLUSTRATION 2.10 Sample Data Analysis Questions and Appropriate Join" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.10 Sample Data Analysis Questions and Appropriate Join</div>

</div>

Câu hỏi Tham gia Có hóa đơn nào của khách hàng mà không có biên lai không? Tham gia trái Có bất kỳ giao dịch nào được tính vào các tài khoản không tồn tại không? Tham gia trái Có bất kỳ séc trả lương nào được phát hành cho nhân viên giả mạo không? Tham gia trái Có khoản lợi nhuận bán hàng nào cho khách hàng không tồn tại không? Tham gia trái Có mặt hàng tồn kho nào chưa được bán không? (Bảng đơn hàng bên trái) Tham gia ngay Có khách hàng nào chưa mua hàng không? (Bảng đơn hàng bên trái) Tham gia ngay Có nhà cung cấp nào chưa được gửi đơn đặt hàng không? (Bảng Mua hàng ở bên trái) Tham gia ngay Có hóa đơn nhà cung cấp nào chưa được thanh toán không? (Bảng thanh toán bên trái) Tham gia ngay Có địa chỉ nhân viên nào khớp với địa chỉ nhà cung cấp không? Tham gia nội bộ Có số điện thoại của nhân viên nào khớp với số điện thoại của nhà cung cấp không? Tham gia nội bộ Việc bán hàng đã được thực hiện ở một khu vực cụ thể chưa? Tham gia nội bộ Áp dụng nó 2.1 Xác định chính và Khóa ngoại Hệ thống thông tin kế toán Super Scooters, nhà sản xuất xe tay ga có động cơ, vừa chuyển đổi sang hệ thống cơ sở dữ liệu quan hệ. Bạn làm việc trong lĩnh vực hệ thống thông tin kế toán của công ty và đã giúp chuyển đổi sang hệ thống cơ sở dữ liệu mới. Sau đây các bảng đã được thiết lập. Địa điểm Vị tríSố Vị tríMô tả Đơn đặt hàng bán hàng Bán hàngSố thứ tự Số đơn hàng người mẫu Ngày bán Doanh số bán hàng Màu sắc Vị tríSố Khu vựcSố tiểu bang Quốc gia Đơn VịBánGiá Số hạng mục Số khách hàng Mã Số Nhân Viên nhân viên Mã Số Nhân Viên Tên đầu tiên Họ Địa chỉ Thành phố tiểu bang Mã Zip Khu vựcSố Khách hàng Số khách hàng Tên khách hàng Địa chỉ khách hàng Khách HàngThành Phố Khách hàngTrạng thái Tên liên hệ Khách hàngZipCode Tên liên hệ Số điện thoại Khu vực Khu vựcSố Khu vựcMô tả Hàng tồn kho Số hạng mục MụcMô tả Màu sắc Số lượng trên tay Chi phí đặt hàng bán hàng Số đơn hàng Tiếp thị biến đổi Lao động Tổng sốBảo hành Tổng số khấu hao Thuế bán hàng Vật liệu Chi phí chung

GIẢI PHÁP Bảng Khóa chính Khóa ngoại Đơn đặt hàng bán hàng Bán hàngSố thứ tự Số đơn hàng Vị tríSố Khu vựcSố Số khách hàng Mã Số Nhân Viên Địa điểm Vị tríSố không có Vùng Khu vựcSố không có Hàng tồn kho Số hạng mục không có Chi phí đặt hàng bán hàng Số đơn hàng không có nhân viên Mã Số Nhân Viên Khu vựcSố Khách hàng Số khách hàng không có 2.2 Cách phân tích các hàm bảng tính Lượng dữ liệu lớn? MỤC TIÊU HỌC TẬP ➋ Giải thích cách các hàm giúp trả lời các câu hỏi phân tích dữ liệu. Phân tích dữ liệu thường bao gồm việc thực hiện các phép tính như cộng số lượng, đếm dữ liệu nhập và tính điểm trung bình. Các phép tính thường được sử dụng thường được tích hợp vào phần mềm phân tích kho dưới dạng hàm, là các công thức được xác định trước để thực hiện các phép tính. Một ví dụ là Hàm SUM trong Microsoft Excel có tác dụng cộng một dãy số theo hàng hoặc cột. Các chức năng giúp bạn có thể nhanh chóng phân tích lượng lớn dữ liệu mà không cần viết com. công thức phức tạp. Trên thực tế, một số thuộc tính mạnh mẽ nhất của Microsoft Excel là tính năng tích hợp sẵn. các hàm thực hiện tính toán. Hãy nhớ rằng các chức năng phổ biến nhất và logic đằng sau chúng cũng áp dụng cho các phần mềm khác ngoài Microsoft Excel. Ví dụ, các chức năng có thể được sử dụng trong các công cụ phân tích và trực quan hóa như Power BI và Tableau. Hiểu cách những điều này các hàm hoạt động và quan trọng hơn là khi nào nên sử dụng chúng là kỹ năng phân tích dữ liệu cốt lõi. Các hàm cơ bản để phân tích dữ liệu Hình minh họa 2.11 mô tả một số hàm Excel cơ bản dùng trong phân tích dữ liệu:

- Tên hàm xuất hiện ở cột đầu tiên.

- Cột thứ hai hiển thị đối số của hàm, đây là cú pháp cần thiết để gọi chức năng, phạm vi và tiêu chí để áp dụng cho nó. Tất cả các hàm Excel đều bắt đầu bằng một dấu bằng, theo sau là loại hàm đang được thực hiện và sau đó là dấu ngoặc đơn chỉ định các đối số cho hàm. Ví dụ: để tính tổng một cột số trong col- umn C và các hàng từ 2 đến 245, hàm sẽ là: =SUM(C2:C245).

- Việc tính toán hàm được mô tả ở cột thứ ba. Sếp của bạn yêu cầu bạn xác định tất cả các khóa chính và khóa ngoại cho các bảng trong cơ sở dữ liệu để các phép nối có thể được tạo ra. Đối với mỗi bảng, liệt kê khóa chính và bất kỳ khóa ngoại nào.

---

# PHẦN III: CÁC HÀM EXCEL CƠ BẢN TRONG PHÂN TÍCH DỮ LIỆU (EXCEL FUNCTIONS - LO 2.2)

## 2.2 Ứng dụng các hàm Excel cơ bản (Applying Basic Excel Functions)

2.2 Các hàm bảng tính phân tích lượng lớn dữ liệu như thế nào?

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.11 Basic Microsoft Excel Functions.PNG" alt="ILLUSTRATION 2.11 Basic Microsoft Excel Functions" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.11 Basic Microsoft Excel Functions</div>

</div>

chức năng Đối số hàm Tính toán hàm NẾU =IF(kiểm tra logic, giá trị nếu đúng, giá trị nếu sai) Trả về một giá trị nếu điều kiện đúng và một cái khác nếu nó sai. TRUNG BÌNH =TRUNG BÌNH(Phạm vi) Trả về giá trị trung bình số học của phạm vi, mảng hoặc số. TRUNG BÌNH =AVERAGEIF (Phạm vi, Tiêu chí, Phạm vi trung bình) Tìm giá trị trung bình số học của các ô được xác định bởi một điều kiện hoặc tiêu chí nhất định. TRUNG BÌNH =AVERAGEIFS(Phạm vi tổng, Phạm vi tiêu chí1, Tiêu chí1, Phạm vi tiêu chí2, Tiêu chí2) Tìm giá trị trung bình số học của các ô được xác định bởi một tập hợp các điều kiện hoặc tiêu chí nhất định. Phạm vi bổ sung, phạm vi tiêu chí và có thể thêm tiêu chí ĐẾM =COUNT(Phạm vi) Đếm số ô trong một phạm vi chứa số. QUẬN =COUNTIF(Phạm vi, Tiêu chí) Đếm số ô trong một phạm vi đáp ứng được các tiêu chí đã cho. QUẬN =COUNTIFS(Phạm vi 1, Tiêu chí1, Phạm vi2, Tiêu chí2) Đếm số ô được chỉ định bởi một bộ tiêu chí đã cho. Phạm vi bổ sung, phạm vi tiêu chí và có thể thêm tiêu chí QUẬN =COUNTA(Phạm vi) Đếm số ô chứa văn bản trong một phạm vi. QUỐC GIA =COUNTBLANK(Phạm vi) Đếm số ô trống trong một phạm vi. TỔNG =SUM(Phạm vi) Thêm các ô trong một phạm vi. SUMIF =SUMIF(Phạm vi, Tiêu chí, phạm vi tổng) Thêm các ô được chỉ định bởi một ô được chỉ định điều kiện hoặc tiêu chí. TÓM TẮT =SUMIFS(Phạm vi tổng, Phạm vi tiêu chí1, Tiêu chí1, Phạm vi tiêu chí2, Tiêu chí2) Thêm các ô được chỉ định bởi một tập hợp nhất định điều kiện hoặc tiêu chí. Phạm vi bổ sung, phạm vi tiêu chí và có thể thêm tiêu chí Quay lại ví dụ dữ liệu trường đại học, Hình minh họa 2.12 cho thấy hàm đối số

hộp bổ sung cho hàm COUNTIF dùng để xác định số lượng máy bơm mà trường đại học sở hữu. Có hai tùy chọn đầu vào để thực hiện các chức năng được minh họa:

- Nhập đối số hàm trực tiếp vào một ô trên bảng tính, hoặc

- sử dụng hộp Đối số hàm. MINH HỌA 2.12 Hộp đối số hàm COUNTIF dữ liệu tài sản của trường đại học

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.12 University Asset Data COUNTIF Function Arguments Box.PNG" alt="ILLUSTRATION 2.12 University Asset Data COUNTIF Function Arguments Box" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.12 University Asset Data COUNTIF Function Arguments Box</div>

</div>

Phạm vi Tiêu chí = {"BƠM";"BONDER";"HỆ THỐNG Tưới tiêu";"DRI... = "Máy bơm" B2:B13127 "Bơm" = 92 Đối số hàm QUẬN Đếm số ô trong một phạm vi thỏa mãn điều kiện đã cho. Phạm vi là phạm vi ô mà bạn muốn đếm các ô không trống. ? Kết quả công thức = 92 Trợ giúp về chức năng này Hủy bỏ được rồi

Để mở:

- Bấm vào fx bên cạnh công thức ô, phía trên bảng tính (xem fx màu xanh lá cây trong hình minh họa 2.13).

- Tiếp theo, hộp nhập Đối số hàm trong Hình minh họa 2.12 xuất hiện trên màn hình.

- Điền vào phạm vi và tiêu chí rồi chọn OK. Công thức của hàm sau đó xuất hiện (Minh họa 2.13). Lưu ý rằng tiêu chí (trong ví dụ này là “Bơm”) phải được nhập theo nguyên tắc

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.13 Finding the Function Arguments Symbol.PNG" alt="ILLUSTRATION 2.13 Finding the Function Arguments Symbol" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.13 Finding the Function Arguments Symbol</div>

</div>

các khẩu phần. Điều này đúng với mọi tiêu chí không phải là tham chiếu ô hoặc số.

Biểu tượng đối số hàm =COUNTIF(B2:B13127,"Bơm") ngoại hối Công thức Các hàm Excel này có thể giúp phân tích nhanh các tập dữ liệu, đặc biệt khi chúng rất phức tạp. lớn. Bây giờ hãy áp dụng các hàm này để trả lời các câu hỏi từ tập dữ liệu về tài sản cố định.

Dữ liệu Chúng tôi sẽ sử dụng bộ dữ liệu tài sản của trường đại học (Minh họa 2.14) để minh họa cách hoạt động

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.14 University Asset Data.PNG" alt="ILLUSTRATION 2.14 University Asset Data" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.14 University Asset Data</div>

</div>

tions có thể giúp làm cho dữ liệu có ý nghĩa.

ngoại hối B A C D E F Trang 1 13126 13127 Tự động Lưu Oﬀ ID thẻ nội dung Mô tả tài sản ID danh mục Dữ liệu tài sản của trường đại học Danh mục Số tiền Ngày mua lại U000009 U000010 U000015 U000016 U102879 U204391 Máy bơm Bonder Hệ thống thủy lợi khoan Máy chủ Lò nướng Thiết bị thí nghiệm Thiết bị thí nghiệm Máy móc nông nghiệp và nông nghiệp Máy móc nông nghiệp và nông nghiệp Thiết bị máy tính Thiết bị chuẩn bị và phục vụ thực phẩm $7,826.00 28.628,01 USD $17,068.00 $ 28.344,00 53.008,90 USD 7.255,53 USD 2/9/2021 11/9/2021 29/9/2020 27/10/2019 9/10/2021 6/5/2023 Tập dữ liệu được tạo từ tệp Dữ liệu tài sản của trường đại học:

- Mỗi hàng trong tập dữ liệu đại diện cho một tài sản duy nhất thuộc sở hữu của trường đại học.

- Các cột thể hiện thuộc tính của từng nội dung. Có 13.127 hàng dữ liệu trong bảng tính này, vì vậy việc quét chúng một cách trực quan là không thể. có thể. Thay vào đó, hãy tận dụng các hàm Excel có sẵn. Hãy tưởng tượng bạn chịu trách nhiệm để xem xét tài sản cố định cho trường đại học. Bạn có thể muốn hỏi những câu hỏi được liệt kê trong Minh họa 2.15. Mỗi câu hỏi có thể được trả lời bằng cách sử dụng hàm Excel.

<div style="text-align: center; margin: 20px auto;">
<img src="../Figures/Buoi_11/ILLUSTRATION 2.15 Questions, Functions, and Answers Using University Asset Data.PNG" alt="ILLUSTRATION 2.15 Questions, Functions, and Answers Using University Asset Data" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
<div style="color: #666; font-style: italic; font-size: 0.9em;">ILLUSTRATION 2.15 Questions, Functions, and Answers Using University Asset Data</div>

</div>

2.2 Các hàm bảng tính phân tích lượng lớn dữ liệu như thế nào?

Câu hỏi chức năng Trả lời Tổng chi phí cố định là bao nhiêu tài sản? =SUM(E2:E13127) $225.069.282,74 Có bao nhiêu tài sản cố định trường đại học có tổng cộng? =COUNTA(A2:A13127) 13.126 Có bao nhiêu tài sản mua lại sau năm 2022? =COUNTIF(F2:F13127,”>31/12/2022”) 1.388 Tổng giá trị tài sản là gì mua lại sau năm 2022? =SUMIF(F2:F13127,”>31/12/2022”,E2:E13127) $27.653.067,52 Có bất kỳ mô tả nào bị thiếu không? =COUNTBLANK(D2:D13127) Hình minh họa 2.15 sử dụng hàm SUM, COUNTA, COUNTIF, SUMIF và COUNTBLANK ý kiến. SUMIFS hoặc COUNTIFS có thể được sử dụng không? Nếu câu hỏi là trường đại học đã mua bao nhiêu máy tính vào năm 2023 thì hãy sử dụng Hàm COUNTIFS vì có hai tiêu chí. Hãy nhớ lại rằng hàm COUNTIFS yêu cầu chỉ định phạm vi ô áp dụng cho tiêu chí đầu tiên (thiết bị máy tính). Tiêu chí tiếp theo là các giao dịch mua được thực hiện vào năm 2023 và phạm vi sẽ là cột có ngày mua. Minh họa- Phần 2.16 hiển thị hộp Đối số hàm cho hàm COUNTIFS và kết quả.

Tiêu chí_range1 = {“Thiết bị thí nghiệm”;”Labora D2:D13127 = 283 Đối số hàm QUẬN Đếm số ô được chỉ định bởi một tập hợp các điều kiện hoặc tiêu chí nhất định. Criteria_range4: là phạm vi ô bạn muốn đánh giá cho điều kiện cụ thể. ? Kết quả công thức = 283 Trợ giúp về chức năng này Tiêu chí1 Tiêu chí_range2 = “Thiết bị máy tính” = {44441;44450;44103;43765;44446;4446 “Thiết bị máy tính” F2:F13127 Tiêu chí2 = “> 31/12/2022” “> 31/12/2022” Tiêu chí_range3 Tiêu chí3 = {44441;44450;44103;43765;44446;4446 = “< 1/1/2024” F2:F13127 “< 1/1/2024” Tiêu chí_range4 = tham khảo Hủy bỏ được rồi Hộp chức năng tạo ra một công thức: =COUNTIFS(D2:D13127,”Thiết bị máy tính”,F2:F13127,”>31/12/2022”, F2:F13127,”<1/1/2024”) Để chỉ truy xuất dữ liệu năm 2023, hãy tạo hai tiêu chí trong đối số hàm:

- Đầu tiên, ngày phải lớn hơn ngày 31 tháng 12 năm 2022 (Tiêu chí2).

- Thứ hai, ngày phải nhỏ hơn ngày 1 tháng 1 năm 2024 (Tiêu chí3).

Bằng cách đưa các tiêu chí đó vào đối số, chỉ kết quả của năm 2023 mới được hiển thị. Các hàm Excel cơ bản rất hữu ích khi trả lời các câu hỏi bằng một câu trả lời duy nhất hoặc một câu trả lời. trả lời với một chiều. Thứ nguyên là các biến hoặc các trường khác có thể được sử dụng để đi sâu hoặc phân chia các biện pháp phân tích. Nói cách khác, kích thước được sử dụng khi có một câu hỏi cụ thể về một khía cạnh cụ thể của dữ liệu. Ví dụ: câu hỏi về số lượng máy tính được mua vào năm 2023 chỉ có một máy tính-thứ nguyên vào năm 2023. Còn một câu hỏi có nhiều thứ nguyên thì sao? cái gì nếu chúng ta muốn biết tổng chi phí cho từng loại tài sản thay vì chỉ máy tính trong một năm cụ thể? Câu hỏi đó có nhiều hơn một chiều vì nó liên quan đến mọi tài sản loại và tất cả các năm. Tiếp theo chúng ta sẽ thảo luận cách giải quyết các câu hỏi đa chiều. Áp dụng nó 2.2 Phân tích doanh số bán hàng Giao dịch với Hàm Excel Dữ liệu Kế toán tài chính Kế toán quản lý Super Scooters sản xuất và bán bốn mẫu xe tay ga đứng: Celeritas, Captain, Lazer và Kicks. Khách hàng của họ bao gồm từ lớn công ty chia sẻ xe tay ga cho đến các nhà bán lẻ nhỏ. Người giám sát của bạn đã giao cho bạn một nhân viên kế toán cho công ty pany, danh sách các câu hỏi cần trả lời bằng cách sử dụng bộ dữ liệu Super Scooters. Phần tiếp theo là một phần của Super Giao dịch bán xe tay ga trong giai đoạn 2023–2025. Có 3.645 giao dịch trong cơ sở dữ liệu bán hàng. Giải thích những hàm Microsoft Excel nào phù hợp nhất để trả lời các câu hỏi sau về Dữ liệu bán hàng của Super Scooters.

- **1. Tổng doanh số bán hàng là bao nhiêu?**

- **2. Tổng doanh thu năm 2023 là bao nhiêu?**

- **3. Có bao nhiêu giao dịch bán hàng đối với mô hình Lazer?**

- **4. Tổng doanh thu trung bình của mẫu Celeritas vào năm 2023 là bao nhiêu?**

- **5. Đã bán được bao nhiêu mẫu Captain màu xanh lá cây?**

- 6. Nếu Super Scooters muốn thêm một cột cho biết số ngày trên lô có lớn hơn không 50 ngày, chức năng nào sẽ phù hợp? GIẢI PHÁP

- **1. TỔNG**

- **2. SUMIF**

- **3. ĐếmIF 4.IFS trung bình**

- **5. ĐếmIFS**

- 6. NẾU ngoại hối B C D A E F G H tôi J Trang 1 Số đơn hàng người mẫu Ngày bán Doanh số bán hàng Số ngàyTrong khoĐơn vịbánGiá Tổng doanh thu 13684 13685 13682 13683 10957 10960 31/12/2025 31/12/2025 30/12/2025 30/12/2025 22/12/2023 31/12/2023 $ 342,00 $414,00 $679,00 $376,00 $330 $357 $6,840 8.280 USD $13,580 $14,288 $5,940 $12,495 Celeritas Lazer thuyền trưởng Lazer Lazer Lazer Màu sắc Vị trí tiểu bang màu vàng Màu xanh màu xanh lá cây màu xanh lá cây màu vàng màu đỏ Dallas Seattle Seattle Miami Phượng hoàng Phượng hoàng TX WA WA FL AZ AZ Tự động Lưu Oﬀ

---

# PHẦN IV: BẢNG TỔNG HỢP (PIVOTTABLE), SẮP XẾP VÀ LỌC DỮ LIỆU (PIVOTTABLES & FILTERING - LO 2.3)

## 2.3 Minh họa cách xoay bảng, sắp xếp và lọc dữ liệu (PivotTables, Sorting & Slicers)

2.3 Chúng tôi tổ chức các tập dữ liệu để phân tích như thế nào? 2.3 Chúng tôi tổ chức các tập dữ liệu như thế nào để phân tích? MỤC TIÊU HỌC TẬP ➌ Minh họa cách tổ chức và lọc dữ liệu của bảng tổng hợp. Bạn vừa học cách sử dụng các hàm để trả lời các câu hỏi có một chiều. Mặc dù bạn có thể sử dụng một số hàm để trả lời các câu hỏi liên quan đến nhiều chiều, sẽ hiệu quả hơn nếu trước tiên sử dụng kỹ thuật tổ chức dữ liệu trên tập dữ liệu. Tổ chức dữ liệu là quá trình sắp xếp lại dữ liệu để dễ hiểu hơn. A bảng tổng hợp là công cụ tóm tắt và sắp xếp lại các cột và hàng dữ liệu đã chọn trong một bảng tính, cơ sở dữ liệu hoặc chương trình kinh doanh thông minh. Bảng tổng hợp có thể sắp xếp lại dữ liệu nhanh chóng

để giúp trả lời nhiều câu hỏi kinh doanh quan trọng. Nhớ lại lời nói mở đầu chương hiểu biết chuyên sâu mà Josh cần sử dụng để sắp xếp lại bảng tính với 450.000 hàng dữ liệu. Josh khó có thể phân tích dữ liệu bảng tính một cách hiệu quả nếu không có bảng tổng hợp. Các ví dụ ở đây sử dụng Microsoft Excel để minh họa cách tạo và lọc một trục cái bàn. (Lưu ý rằng các bảng tổng hợp được tạo trong phần mềm này thường được gắn nhãn là PivotTable.) Mặc dù phần trình diễn sử dụng Excel PivotTable nhưng những kỹ thuật này cũng được sử dụng trong các phần mềm phân tích dữ liệu. Ví dụ: chúng rất hữu ích khi tạo hình ảnh trực quan. Dù thế nào đi nữa công cụ phân tích dữ liệu bạn sử dụng, hiểu chức năng cơ bản của việc tạo các bảng tổng hợp hữu ích và cách lọc chúng là điều cần thiết. Sử dụng bảng tổng hợp Vừa mạnh mẽ vừa dễ sử dụng, bảng tổng hợp cũng là một trong những công cụ phổ biến nhất mà bạn sẽ sử dụng trong sự nghiệp kế toán của bạn. Nó có năm thành phần chính:

- **1. Trường: Các thành phần dữ liệu có sẵn để sử dụng trong bảng tổng hợp.**

- 2. Cột: Khi một trường được chọn cho vùng cột, chỉ các giá trị duy nhất của trường được liệt kê ở trên cùng.

- 3. Hàng: Khi một trường được chọn cho vùng hàng, trường đó sẽ được điền làm cột đầu tiên. Tất cả hàng giá trị là giá trị duy nhất và các giá trị trùng lặp sẽ bị loại bỏ.

- 4. Giá trị: Mỗi giá trị được giữ trong một ô của bảng tổng hợp và hiển thị thông tin tóm tắt. Ví dụ như tổng, trung bình hoặc đếm.

- 5. Bộ lọc: Áp dụng hạn chế cho toàn bộ bảng. Khi bạn biết những điều cơ bản về tạo bảng tổng hợp trong Microsoft Excel, bạn có thể sử dụng công cụ này để giải đáp thắc mắc kế toán. Tạo một PivotTable Microsoft Excel Thực hiện theo các bước sau:

- **1. Mở bảng tính có dữ liệu cần tóm tắt.**

- 2. Nhấp vào bất kỳ ô nào trong dữ liệu (ô đầu tiên ở hàng A trong Hình minh họa 2.17).

- **3. Nhấp vào tùy chọn Chèn trên dải băng menu trên cùng.**

- 4. Tùy chọn hộp nhập PivotTable sẽ xuất hiện ở phía trên bên trái màn hình (Minh họa 2.17).

Tự động Lưu Bảng Bàn ngoại hối A2 B A D E F ID thẻ nội dung Mô tả tài sản C ID danh mục Danh mục Số tiền 28.628,01 USD $ 28.344,00 $ 33,573,00 $13,720.00 13.552,65 USD $17,068.00 $7,826.00 Ngày mua lại Trang 1 Biểu tượng + Khuyến nghị- sửa chữa Biểu đồ Hình ảnh Hình dạng Mô hình 3D Minh họa SmartArt Ảnh chụp màn hình Nhận phần bổ trợ Tiện ích bổ sung của tôi Phần bổ trợ Biểu đồ Xoay bản đồ Biểu đồ Đường lấp lánh Cột Dòng Thắng/ Mất mát 3D Bản đồ Chuyến tham quan tập tin Trang chủ Chèn Bố cục trang Công thức dữ liệu Xem lại Xem Nhà phát triển Trợ giúp Power Pivot Tab mới U000009 Khuyến nghị- sửa chữa PivotTable Bảng Biểu tượng + Khuyến nghị- sửa chữa Biểu đồ Hình ảnh Hình dạng Mô hình 3D Minh họa SmartArt Ảnh chụp màn hình Nhận phần bổ trợ Tiện ích bổ sung của tôi Phần bổ trợ Biểu đồ Xoay bản đồ Biểu đồ Đường lấp lánh Cột Dòng Thắng/ Mất mát 3D Bản đồ Chuyến tham quan Khuyến nghị- sửa chữa PivotTable Xoay vòng Bảng Thiết bị thí nghiệm Thiết bị thí nghiệm Thiết bị thí nghiệm Máy móc nông nghiệp và nông nghiệp Máy móc nông nghiệp và nông nghiệp Thiết bị liên lạc, nghe nhìn, báo động và tín hiệu Thiết bị thí nghiệm Máy bơm Máy bơm Bonder Hệ thống thủy lợi khoan Máy quay video Hệ thống siêu âm U000010 U000015 U000016 U000018 U000020 U000022 U000009 4/9/2015 13/9/2015 1/10/2015 29/10/2015 9/9/2015 24/9/2015 9/9/2015

Bảng tính Excel dữ liệu tài sản của trường đại học Khi tùy chọn này được chọn, một hộp thoại mới sẽ mở ra có tên PivotTable từ bảng hoặc phạm vi ( Minh họa 2.18 ).

- 5. Đảm bảo Bảng/Phạm vi trong hộp Chọn bảng hoặc phạm vi phản ánh tất cả dữ liệu cần thiết. được bao gồm. (Hãy nhớ bao gồm các tiêu đề cột.) Chọn Bảng tính mới và nhấn OK (Minh họa 2.18). PivotTable từ bảng hoặc phạm vi Bảng/Phạm vi: Chọn một bảng hoặc dải ô ? Hủy bỏ được rồi Bảng tính mới Bảng tính hiện có Vị trí: ‘Dữ liệu kiểm kê của trường đại học’!$A$1:$F$13127 Chọn nơi bạn muốn đặt báo cáo PivotTable Chọn xem bạn có muốn phân tích nhiều bảng không Thêm dữ liệu này vào Mô hình Dữ liệu MINH HỌA 2.18 Hộp thoại Tạo PivotTable trong Excel

- 6. Thao tác này sẽ mở một bảng tính mới. Một khung vẽ PivotTable trống sẽ xuất hiện ở bên trái và Hộp Trường PivotTable tạo PivotTable sẽ ở bên phải (Hình minh họa 2.19).

2.3 Chúng tôi tổ chức các tập dữ liệu để phân tích như thế nào? ngoại hối A B C D E Xoay Q1 & Q2 Tự động Lưu Oﬀ Trường PivotTable Chọn các trường để thêm vào báo cáo: ID thẻ nội dung Mô tả tài sản ID danh mục Danh mục Số tiền Ngày mua lại Khu Năm Thêm bàn.. Kéo các trường giữa các khu vực bên dưới: Bộ lọc Cột Tìm kiếm Hàng Trì hoãn cập nhật bố cục Giá trị ∑ cập nhật PivotTable1 Để xây dựng một báo cáo, hãy chọn các trường từ Danh sách trường PivotTable

Canvas PivotTable trống Sử dụng hộp Trường PivotTable để chọn nội dung sẽ xuất hiện trong PivotTable. Kéo cột đặt tên cho hàng, cột, giá trị hoặc bộ lọc. Dữ liệu Hãy sử dụng PivotTable để trả lời các câu hỏi về dữ liệu về dữ liệu tài sản của trường đại học. Nếu bạn đang xác minh tổng chi phí cho từng loại tài sản, bạn có thể muốn trả lời câu hỏi những câu hỏi sau:

- Câu 1: Tổng số dư tài sản theo từng loại là bao nhiêu?

- Câu hỏi 2: Tổng số tài sản ở mỗi loại là bao nhiêu? Tìm Tổng số dư theo Danh mục Trả lời câu hỏi đầu tiên bằng cách tìm tổng số dư theo danh mục. 1. Kéo Danh mục vào khu vực Hàng. 2. Kéo Số tiền vào vùng Giá trị. Sau đó, các giá trị Σ trong Cột sẽ được tự động tạo ra được xử lý bằng Excel. 3. Excel sẽ điền các giá trị cho từng danh mục vào cột thứ hai của bảng tính.

Hình minh họa 2.20 hiển thị kết quả PivotTable. Câu hỏi 1 Nhãn hàng Máy móc nông nghiệp và nông nghiệp $ 3,838,203,58 129.924,35 USD 1.047.971,77 USD $ 2,458,319,00 4.242.923,45 USD 1.210.703,93 USD 3.060.781,37 USD 2.287.996,49 USD 2.449.781,57 USD 1.270.121,50 USD 6.467.000,41 USD Tổng cộng $ 225.069.282,74 1.587.495,45 USD $ 1.865.573,30 43.294.238,92 USD 147.343.867,13 USD $18,033.00 $51,825.00 $90,332.00 $47,239.00 $88,248.00 530.673,88 USD 278.233,02 USD 650.212,23 USD 146.953,15 USD 102.458,55 USD $ 279.665,97 230.506,72 USD Thiết bị nghệ thuật Thiết bị thể thao và giải trí Thuyền, động cơ thuyền và thiết bị hàng hải Thiết bị vệ sinh và bảo trì Thiết bị liên lạc, nghe nhìn, báo động và tín hiệu Thiết bị máy tính Thiết bị vẽ và khảo sát Thiết Bị Điện Thiết bị điện tử Thiết bị chuẩn bị và phục vụ thực phẩm Nội Thất Và Nội Thất Dụng cụ cầm tay và điện (Di động) Thiết bị công nghiệp, cửa hàng và xây dựng Thiết bị thí nghiệm Thiết bị xử lý vật liệu Thiết bị y tế Thiết bị khác Phương tiện cơ giới và thiết bị vận tải Nhạc cụ Máy văn phòng và kinh doanh và vật tư không tiêu hao Thiết bị kiểm soát đỗ xe Thiết bị chụp ảnh Thiết bị cấp nước, sưởi ấm, điều hòa không khí và thông gió Thiết bị cảnh sát, chữa cháy và an toàn Thiết bị in ấn và đóng sách Thiết bị điện lạnh Tổng số tiền

theo danh mục?

Kéo các trường giữa được rồi Hủy bỏ Cài đặt trường giá trị Bộ lọc Hàng Di chuyển lên Di chuyển xuống Di chuyển đến cuối Chuyển đến phần đầu Di chuyển đến Bộ lọc Báo cáo Di chuyển đến nhãn hàng Di chuyển đến nhãn cột Di chuyển đến giá trị ∑ Xóa trường Cài đặt trường giá trị... Tên nguồn: AssetTagID Tên tùy chỉnh: Tóm tắt các giá trị theo Chọn loại phép tính mà bạn muốn sử dụng để tóm tắt dữ liệu trường đã chọn Tổng trung bình Tối đa tối thiểu sản phẩm Định dạng số Tóm tắt trường giá trị bằng ? Số lượng AssetTagID Đếm Hiển thị giá trị dưới dạng tôi Danh mục Trì hoãn cập nhật bố cục Số lượng tài sản_T... cập nhật

- 4. Excel sẽ mặc định tính tổng của giá trị. Loại phép đo có thể được thay đổi bằng cách nhấp vào mũi tên xuống trong trường Tổng số tiền và chọn số đo mong muốn (Minh họa 2.21).

2.3 Chúng tôi tổ chức các tập dữ liệu để phân tích như thế nào? Một tính năng hữu ích khác của hộp thoại Cài đặt Trường Giá trị là khả năng thay đổi số- định dạng ber trong PivotTable. ( Cách thực hiện dữ liệu 2.1 ở cuối chương này giải thích về Hiển thị Khả năng định giá bằng các tính toán dựng sẵn.) Xác định tổng số tài sản Để xác định tổng số tài sản trong mỗi danh mục (Câu hỏi 2), hãy sử dụng hàm Excel đầu tiên PivotTable:

- **1. Kéo AssetTagID vào vùng Giá trị.**

- **2. Nhấp vào mũi tên xuống, chọn Cài đặt trường giá trị và chọn Đếm.**

Dữ liệu có thể được tóm tắt bằng một số tính toán khác nhau. Câu hỏi hỏi về số lượng nội dung cho mỗi danh mục, vì vậy hãy chọn Đếm.

- 3. Excel điền vào cột bảng tiếp theo số lượng theo danh mục tài sản. Kết quả được thể hiện ở hình minh họa 2.22. Câu hỏi 1 Câu hỏi 2 Trường PivotTable Nhãn hàng Số lượng AssetTagID Máy móc nông nghiệp và nông nghiệp $ 3,838,203,58 Chọn các trường để thêm vào báo cáo ID thẻ nội dung Mô tả tài sản ID danh mục Danh mục Danh mục Số tiền Ngày mua lại Khu Năm Thêm bàn.. Kéo các trường giữa các khu vực bên dưới: Bộ lọc Cột 129.924,35 USD 1.047.971,77 USD $ 2,458,319,00 4.242.923,45 USD 1.210.703,93 USD 3.060.781,37 USD 2.287.996,49 USD 2.449.781,57 USD 1.270.121,50 USD 6.467.000,41 USD Tổng cộng $ 225.069.282,74 13126 1.587.495,45 USD $ 1.865.573,30 43.294.238,92 USD 147.343.867,13 USD $18,033.00 $51,825.00 $90,332.00 $47,239.00 $88,248.00 530.673,88 USD 278.233,02 USD 650.212,23 USD 146.953,15 USD 102.458,55 USD $ 279.665,97 230.506,72 USD Thiết bị nghệ thuật Thiết bị thể thao và giải trí Thuyền, động cơ thuyền và thiết bị hàng hải Thiết bị vệ sinh và bảo trì Thông tin liên lạc, Nghe nhìn, Báo động, và thiết bị tín hiệu Thiết bị máy tính Thiết bị vẽ và khảo sát Thiết Bị Điện Thiết bị điện tử Thiết bị chuẩn bị và phục vụ thực phẩm Nội Thất Và Nội Thất Dụng cụ cầm tay và điện (Di động) Thiết bị công nghiệp, cửa hàng và xây dựng Thiết bị thí nghiệm Thiết bị xử lý vật liệu Thiết bị y tế Thiết bị khác Phương tiện cơ giới và thiết bị vận tải Nhạc cụ Máy móc văn phòng và kinh doanh và Vật tư không tiêu hao Thiết bị kiểm soát đỗ xe Thiết bị chụp ảnh Hệ thống nước, sưởi ấm, điều hòa không khí, và thiết bị thông gió Thiết bị cảnh sát, chữa cháy và an toàn Thiết bị in ấn và đóng sách Thiết bị điện lạnh Tổng số tiền Tìm kiếm Hàng Trì hoãn cập nhật bố cục Giá trị ∑ Giá trị Tổng số tiền Số lượng AssetTagID ∑ cập nhật MINH HỌA 2.22 Bảng tổng hợp Excel cho câu hỏi 2: Tổng số tài sản trong mỗi danh mục là bao nhiêu? Làm cách nào để

Một cách để tập trung vào một khía cạnh cụ thể của dữ liệu trong PivotTable là sử dụng bộ lọc. Áp dụng một bộ lọc có nghĩa là chỉ những dữ liệu phù hợp với tiêu chí của nó mới được hiển thị. Có ba cách để lọc trong Excel:

- Áp dụng tiêu chí lọc cho vùng trường Lọc.

- Sử dụng Bộ lọc Tự động trong trường Hàng của PivotTable.

- Chèn một hoặc nhiều máy thái. Dữ liệu Trả lời câu hỏi dữ liệu nội dung thứ ba sẽ hiển thị từng tùy chọn lọc: Câu 3: Tổng số lượng mua hàng theo danh mục thực hiện trong năm 2022 là bao nhiêu? Áp dụng tiêu chí lọc cho hộp trường bộ lọc Để khám phá tổng số lượng mua hàng theo danh mục trong năm 2022, hãy tạo PivotTable hiển thị tài sản được mua vào năm 2022 theo danh mục: 1. Kéo Danh mục vào Hàng và kéo Số lượng vào Giá trị. 2. Trọng tâm là tài sản được mua vào năm 2022, vì vậy hãy đưa Năm vào khu vực Bộ lọc. 3. Từ Năm ở cột đầu tiên và từ ALL ở cột thứ hai bây giờ sẽ xuất hiện ở đầu PivotTable. 4. Nhấp vào mũi tên xuống bên cạnh TẤT CẢ kết quả trong hộp thả xuống để chọn năm cần lọc (Minh họa 2.23). Tổng số tiền Câu hỏi 1 Nhãn hàng Năm Máy móc nông nghiệp và nông nghiệp Tổng cộng Thiết bị thể thao và giải trí Thuyền, động cơ thuyền và thiết bị hàng hải Thiết bị liên lạc, nghe nhìn, báo động và tín hiệu Thiết bị máy tính Thiết bị chuẩn bị và phục vụ thực phẩm Nội Thất Và Nội Thất Dụng cụ cầm tay và điện (Di động) Thiết bị công nghiệp, cửa hàng và xây dựng Thiết bị thí nghiệm Thiết bị xử lý vật liệu Thiết bị y tế Thiết bị khác Phương tiện cơ giới và thiết bị vận tải Máy văn phòng và kinh doanh và vật tư không tiêu hao Thiết bị kiểm soát đỗ xe Thiết bị in ấn và đóng sách Thiết bị điện lạnh TẤT CẢ $258.409.17 188.366,29 USD 389.043,31 USD 20.869.919,66 USD 103.113,50 USD $8,045.00 $89,889.00 $ 23.274,20 Chọn nhiều mục được rồi Hủy bỏ Tìm kiếm Kéo các trường giữa các khu vực bên dưới: Bộ lọc Cột Năm Danh mục Tổng số tiền Hàng Giá trị ∑ Trì hoãn cập nhật bố cục cập nhật Thiết bị vệ sinh và bảo trì MINH HỌA 2.23 Cách lọc trong PivotTable Excel Hình minh họa 2.24 cho thấy kết quả lọc tài sản được mua vào năm 2022.

2.3 Chúng tôi tổ chức các tập dữ liệu để phân tích như thế nào?

Trả lời câu hỏi 3: Thế nào là Tổng nguyên giá tài sản mua vào 2022? Tổng số tiền Nhãn hàng Năm Máy móc nông nghiệp và nông nghiệp Tổng cộng Thiết bị thể thao và giải trí Thuyền, động cơ thuyền và thiết bị hàng hải Thiết bị vệ sinh và bảo trì Thiết bị liên lạc, nghe nhìn, báo động và tín hiệu Thiết bị máy tính Thiết bị chuẩn bị và phục vụ thực phẩm Nội Thất Và Nội Thất Dụng cụ cầm tay và điện (Di động) Thiết bị công nghiệp, cửa hàng và xây dựng Thiết bị thí nghiệm Thiết bị xử lý vật liệu Thiết bị y tế Thiết bị khác Phương tiện cơ giới và thiết bị vận tải Máy văn phòng và kinh doanh và vật tư không tiêu hao Thiết bị kiểm soát đỗ xe Thiết bị in ấn và đóng sách Thiết bị điện lạnh $258.409.17 514.343,81 USD $ 144.999,00 108.637,41 USD 234.398,94 USD 523.934,69 USD 8.141.730,27 USD 77.915,86 USD 64.795,95 USD $ 49.665,00 117.352,04 USD 9.825.228,22 USD $6,778.00 188.366,29 USD 389.043,31 USD 20.869.919,66 USD 103.113,50 USD $8,045.00 $89,889.00 $ 23.274,20 Tổng số tiền Sử dụng Bộ lọc tự động hàng Bộ lọc cũng có thể được tạo trong PivotTable Excel bằng chức năng Lọc tự động cho các hàng. trong Trong ví dụ này, câu hỏi đặt ra là chi bao nhiêu cho thiết bị máy tính vào năm 2022.

- 1. Thay vì thêm một danh mục vào vùng Bộ lọc, hãy nhấp vào mũi tên xuống trong Nhãn Hàng để tiết lộ các lựa chọn lọc khác.

- 2. Hình minh họa 2.25 hiển thị hộp thả xuống sau đó xuất hiện. Tại đây chọn các danh mục của nội dung cần lọc. ngoại hối A B Trang 1 Tự động Lưu Oﬀ Nhãn hàng Năm Máy móc nông nghiệp và nông nghiệp Tổng cộng Thiết bị thể thao và giải trí Thuyền, động cơ thuyền và thiết bị hàng hải Thiết bị vệ sinh và bảo trì Thiết bị liên lạc, nghe nhìn, báo động và tín hiệu Thiết bị máy tính Thiết bị chuẩn bị và phục vụ thực phẩm Nội Thất Và Nội Thất Dụng cụ cầm tay và điện (Di động) Thiết bị công nghiệp, cửa hàng và xây dựng Thiết bị thí nghiệm Thiết bị xử lý vật liệu Thiết bị y tế Thiết bị khác Phương tiện cơ giới và thiết bị vận tải Máy văn phòng và kinh doanh và vật tư không tiêu hao Thiết bị kiểm soát đỗ xe Thiết bị in ấn và đóng sách Thiết bị điện lạnh $258.409.17 514.343,81 USD $ 144.999,00 108.637,41 USD 234.398,94 USD 523.934,69 USD 8.141.730,27 USD 77.915,86 USD 64.795,95 USD $ 49.665,00 117.352,04 USD 9.825.228,22 USD $6,778.00 188.366,29 USD 389.043,31 USD 20.869.919,66 USD 103.113,50 USD $8,045.00 $89,889.00 $ 23.274,20 Tổng số tiền Sắp xếp từ A đến Z Tùy chọn sắp xếp khác... Xóa bộ lọc khỏi “Danh mục” Bộ lọc nhãn Bộ lọc giá trị Sắp xếp Z đến A AZ ZA Tìm kiếm (Chọn tất cả) Máy nông nghiệp và trang trại Thiết bị nghệ thuật Phương trình thể thao và giải trí Thuyền, Động Cơ Thuyền và Tháng Ba Vệ sinh và bảo trì E Truyền thông, nghe nhìn Thiết bị máy tính được rồi Hủy bỏ MINH HỌA 2.25 Excel PivotTable để lọc cho máy tính Chỉ thiết bị

- 3. Trong ví dụ này, chỉ chọn Thiết bị Máy tính. PivotTable thu được là thể hiện ở hình minh họa 2.26 MINH HỌA 2.26 Excel PivotTable Chỉ hiển thị thiết bị máy tính Đã mua vào năm 2022 8.141.730,27 USD 8.141.730,27 USD Tổng cộng Nhãn hàng Tổng số tiền Thiết bị máy tính Năm Tùy chọn bộ lọc tự động nhanh chóng tách biệt một mục cụ thể. Hai bộ lọc tự động nữa là Nhãn Bộ lọc và Bộ lọc giá trị. Hình minh họa 2.27 thể hiện các tùy chọn có sẵn sau khi chọn Label Bộ lọc. MINH HỌA 2.27 Bộ lọc nhãn PivotTable trong Excel Sắp xếp từ A đến Z Tùy chọn sắp xếp khác... Xóa bộ lọc khỏi “Danh mục” Bộ lọc giá trị Sắp xếp Z đến A AZ ZA Tìm kiếm (Chọn tất cả) Máy nông nghiệp và trang trại Thiết bị nghệ thuật Phương trình thể thao và giải trí Thuyền, Động Cơ Thuyền và Tháng Ba Vệ sinh và bảo trì E Truyền thông, nghe nhìn Thiết bị máy tính được rồi Hủy bỏ Xóa bộ lọc Bằng... Không bằng... Bắt đầu với... Không bắt đầu bằng... Không kết thúc bằng... Chứa... Không chứa... Lớn Hơn... Lớn hơn hoặc bằng... Ít hơn... Nhỏ hơn hoặc bằng... Giữa... Không Giữa... Kết thúc bằng... Bộ lọc nhãn Đánh dấu và nhấp vào một trong các tùy chọn trong Bộ lọc Nhãn sẽ mở ra một hộp thoại để chèn tham số của bộ lọc. Ví dụ: chọn Bằng và nhập “Máy tính Equipment” trong hộp thoại (Minh họa 2.28) đạt được kết quả tương tự như Minh họa 2.26.

2.3 Chúng tôi sắp xếp các tập dữ liệu để phân tích như thế nào?

Bộ lọc nhãn (Danh mục) Hiển thị các mục có nhãn Sử dụng? để đại diện cho bất kỳ ký tự đơn nào bằng Thiết bị máy tính Sử dụng * để đại diện cho bất kỳ chuỗi ký tự nào Hủy bỏ được rồi ? Điều gì sẽ xảy ra nếu mục tiêu là lọc dữ liệu để chỉ xuất hiện 5 danh mục nội dung hàng đầu?

- 1. Sử dụng Bộ lọc Giá trị và chọn tùy chọn Top 10… (Minh họa 2.29). Sắp xếp từ A đến Z Tùy chọn sắp xếp khác... Xóa bộ lọc khỏi “Danh mục” Sắp xếp Z đến A AZ ZA Tìm kiếm (Chọn tất cả) Máy nông nghiệp và trang trại Thiết bị nghệ thuật Phương trình thể thao và giải trí Thuyền, Động Cơ Thuyền và Tháng Ba Vệ sinh và bảo trì E Truyền thông, nghe nhìn Thiết bị máy tính được rồi Hủy bỏ Xóa bộ lọc Bằng... Không bằng... Lớn Hơn... Lớn hơn hoặc bằng... Ít hơn... Nhỏ hơn hoặc bằng... Giữa... Không Giữa... Top 10... Bộ lọc nhãn Bộ lọc giá trị MINH HỌA 2.29 Tùy chọn bộ lọc giá trị PivotTable

- 2. Một hộp thoại sẽ mở ra cho phép thay đổi bộ lọc lên trên hoặc dưới và số lượng các mục để hiển thị. Trong Hình minh họa 2.30, “Top 5” theo “Tổng số tiền” đã được chọn. Bộ lọc Top 10 (Danh mục) Hiển thị hàng đầu Mặt hàng Tổng số tiền bởi Hủy bỏ được rồi ? MINH HỌA 2.30 Bộ lọc giá trị PivotTable cho hộp nhập giá trị hàng đầu

Kết quả PivotTable Excel được hiển thị trong Hình minh họa 2.31. 514.343,81 USD 523.934,69 USD 8.141.730,27 USD 9.825.228,22 USD 389.043,31 USD $ 19.394.280,30 Tổng cộng Nhãn hàng Máy móc nông nghiệp và nông nghiệp Tổng số tiền Năm Thiết bị liên lạc, nghe nhìn, báo động và tín hiệu Thiết bị máy tính Thiết bị thí nghiệm Thiết bị điện lạnh

Còn việc lọc nhiều thứ nguyên cùng một lúc thì sao? Sử dụng Slicers để lọc dữ liệu Việc lọc đồng thời nhiều chiều thường được gọi là cắt hoặc cắt và xúc xắc, đó là quá trình chia nhỏ dữ liệu thành các phần nhỏ hơn hoặc kiểm tra nó từ quan điểm khác nhau. Máy cắt là một công cụ phân tích giúp phân tách các thước đo phân tích kết quả theo các kích thước đã chọn. Tất cả các phần mềm phân tích dữ liệu đều có khả năng cắt:

- Microsoft Excel và Power BI sử dụng slicer.

- Trong Tableau, việc này được thực hiện bằng các bộ lọc tương tác. Trong tất cả các loại phần mềm, slicer tùy chỉnh sự tương tác với tập dữ liệu bằng cách cung cấp màn hình trực quan. chơi các bộ lọc có sẵn. Hình minh họa 2.32 cho thấy nơi có thể tìm thấy tùy chọn thêm slicer trong Microsoft Excel. Xem Nhà phát triển Trợ giúp Power Pivot nhào lộn dữ liệu Lọc Làm mới Thay đổi dữ liệu Nguồn Chèn Máy thái Chèn Dòng thời gian Lọc Kết nối ngoại hối ngoại hối B A C D E F $ 3,838,203,58 $80,333.00 3.060.781,37 USD 1.210.703,93 USD 278.233,02 USD $51,825.00 $18,033.00 43.294.238,92 USD 4.242.923,45 USD $ 2,458,319,00 530.673,88 USD 1.047.971,77 USD 129.924,35 USD Tổng số tiền ID thẻ nội dung Mô tả tài sản ID danh mục Danh mục Số tiền Ngày mua lại Khu Năm ? được rồi Hủy bỏ Xem lại dữ liệu Làm mới Thay đổi dữ liệu Nguồn Lọc Kết nối Chèn máy cắt MINH HỌA 2.32 Thêm Slicer vào PivotTable

2.3 Chúng tôi sắp xếp các tập dữ liệu để phân tích như thế nào?

- 1. Nhấp vào PivotTable và chọn Insert Slicer từ menu. Điều này sẽ mở một hộp với tất cả các trường PivotTable.

- 2. Chọn các trường cho slicer. Nếu mục tiêu là xác định số tiền đã được chi cho mỗi danh mục tài sản theo năm, sau đó chia nhỏ dữ liệu theo danh mục tài sản và năm. Để thực hiện việc này, hãy chọn Danh mục và Ngày mua lại. Hình minh họa 2.33 cho thấy kết quả slicer. Một cái dành cho danh mục và cái còn lại dành cho năm. ngoại hối A B C D Trang 1 Tự động Lưu Oﬀ Danh mục Năm 8.141.730,27 USD 8.141.730,27 USD Tổng cộng Nhãn hàng Tổng số tiền Thiết bị máy tính Nông nghiệp và trang trại Thể thao và Giải trí Thuyền, động cơ thuyền và Vệ sinh và bảo trì Truyền Thông, Âm Thanh Thiết bị máy tính Chuẩn bị thức ăn và Nội thất và Nội thất MINH HỌA 2.33 Bộ cắt PivotTable Tìm tổng số tiền theo danh mục và năm Trong Hình minh họa 2.33, nhấp vào Thiết bị Máy tính trong bộ cắt Danh mục và 2022 trong phần Bộ cắt theo năm tạo ra một PivotTable với tổng số thiết bị máy tính được mua vào năm 2022. Có thể thêm bộ cắt vào Power BI bằng cách chọn công cụ bộ cắt trong Trực quan hóa ( Minh họa- câu 2.34). R Py Giá trị Báo cáo chéo Giữ tất cả các bộ lọc Khoan qua Oﬀ Bật Trường Trực quan hóa Bộ lọc Trang 1 Ngày mua lại Số tiền Mô tả tài sản ID thẻ nội dung Danh mục ID danh mục Năm Thêm trường dữ liệu ở đây Thêm trường dữ liệu ở đây Thêm trường dữ liệu ở đây Tìm kiếm Bộ lọc trên hình ảnh này Bộ lọc trên trang này Bộ lọc trên tất cả các trang Số tiền là (Tất cả) là (Tất cả) Danh mục Danh mục Số tiền Thêm các trường thông tin chi tiết tại đây Tìm kiếm ngoại hối R Py MINH HỌA 2.34 Bảng tổng hợp Máy cắt sử dụng PowerBI

Tiếp theo, chọn Danh mục để tạo bộ cắt danh mục và lặp lại cho bộ cắt AcquisitionDate. Hình minh họa 2.35 cho thấy kết quả. tập tin Làm người mẫu Xem Trợ giúp Chèn Trang chủ ngoại hối A C B Trang 1 Danh mục Tổng cộng 8.141.730,27 USD Thiết bị máy tính 8.141.730,27 USD Số tiền Chọn nhiều mục được rồi Hủy bỏ Năm Chọn nhiều mục được rồi Hủy bỏ Danh mục Thiết bị chuẩn bị và phục vụ thực phẩm Đăng nhập Thiết bị máy tính Thông tin liên lạc, nghe nhìn, báo động Thiết bị vệ sinh và bảo trì Thuyền, động cơ thuyền và thiết bị hàng hải Thiết bị thể thao và giải trí Máy móc nông nghiệp và nông nghiệp

Bởi vì các hàm bảng tổng hợp tóm tắt dữ liệu để nhanh chóng tìm ra câu trả lời cho các câu hỏi của chúng ta, tạo bảng tổng hợp là kỹ năng phân tích dữ liệu cốt lõi mà bạn sẽ sử dụng thường xuyên trong sự nghiệp của mình. Áp dụng nó 2.3 Phân tích doanh số bán hàng với Bảng tổng hợp Excel dữ liệu Kế toán tài chính Kế toán quản lý Người giám sát của bạn tại Super Scooters có yêu cầu bạn phân tích doanh thu năm 2025 và doanh thu tất cả các năm. Tạo một PivotTable Excel để xác định sau đây:

- **1. Tổng doanh thu của từng địa điểm vào năm 2025 là bao nhiêu?**

- **2. Tổng doanh thu trung bình của mỗi mẫu xe vào năm 2025 là bao nhiêu?**

- **3. Tổng doanh thu mỗi năm là bao nhiêu? GIẢI PHÁP**

- 1. Chọn (hoặc kéo) các trường: Vị trí cho Hàng , Tổng doanh thu cho Giá trị và Năm cho Bộ lọc . Trong năm lọc chọn 2025. Nhãn hàng Tổng doanh thu gộp Boston Charlotte Chicago Dallas Miami Phượng hoàng Thành phố Salt Lake Seattle $ 1.433.578,00 $ 1.653.506,00 $ 1.624.719,00 $ 1.134.785,00 $ 1.606.576,00 $ 1.376.503,00 $ 1.593.184,00 $ 1.742.311,00 $ 12.165.162,00 Tổng cộng Năm

- 2. Bắt đầu bằng cách kéo các trường: Mô hình vào Hàng, Tổng doanh thu vào Giá trị và Năm vào Bộ lọc. Thay đổi Tổng doanh thu thành Trung bình bằng cách mở Cài đặt trường giá trị và chọn Trung bình. Trong bộ lọc năm, chọn 2025. Nhãn hàng Tổng doanh thu trung bình thuyền trưởng Celeritas cú đá Lazer 15.855,84 USD 4.977,54 USD 2.760,45 USD 7.981,45 USD 9.098,85 USD Tổng cộng Năm

---

# PHẦN V: THỐNG KÊ MÔ TẢ TRONG PHÂN TÍCH DỮ LIỆU (DESCRIPTIVE STATISTICS - LO 2.4)

## 2.4 Các thước đo mô tả dữ liệu (Measures of Location, Spread, Shape & Correlation)

- 3. Chọn các trường sau: Năm thành hàng, Doanh thu thành giá trị. Năm Tổng doanh thu 1.827.384,78 USD $ 4.086.546,19 $ 4.745.563,32 10.659.494,29 USD Tổng cộng 2.4 Biện pháp mô tả nào giúp chúng tôi Hiểu dữ liệu? MỤC TIÊU HỌC TẬP ➍ Xác định các biện pháp mô tả được sử dụng để thực hiện phân tích dữ liệu. Bạn đã học cách xác định và truy xuất dữ liệu cũng như một số phương pháp cơ bản để phân tích dữ liệu. Trước đó trong khóa học, bạn cũng đã biết rằng có bốn loại phân tích dữ liệu:

- Miêu tả

- Chẩn đoán

- Dự đoán

- Có tính chất kê đơn Hãy nhớ rằng phân tích mô tả giúp tiết lộ những gì đã xảy ra hoặc hiện đang xảy ra trong dữ liệu. Tại sao phân tích mô tả được coi là trọng tâm của phân tích dữ liệu? Không có điều đó hiểu biết cơ bản về dữ liệu, tiến tới các phương pháp phân tích dữ liệu phức tạp hơn là không thể được. Đôi khi những phân tích mang tính mô tả là tất cả những gì cần thiết, nhưng thường thì điều này phương pháp này là tiền thân cho các phân tích chẩn đoán, dự đoán và kê đơn. Dữ liệu cốt lõi kỹ năng phân tích cho phân tích mô tả là hiểu thống kê mô tả và mối tương quan phân tích.

Thống kê mô tả cho thấy những quan sát trung bình trong dữ liệu, hình dạng của dữ liệu. và phân phối dữ liệu. Ngoài ra, phân tích tương quan có thể chỉ ra mối quan hệ trong dữ liệu. Cùng với nhau, những số liệu thống kê này cung cấp những hiểu biết sâu sắc về dữ liệu. Các biện pháp vị trí Các phép đo vị trí xác định mức quan sát trung bình hoặc điển hình trong tập dữ liệu. Giá trị trung bình, trung vị và chế độ Thước đo xu hướng trung tâm là một giá trị duy nhất mô tả một tập hợp dữ liệu bằng cách xác định vị trí trung tâm trong tập dữ liệu đó. Có ba thước đo về xu hướng trung tâm:

- Giá trị trung bình: Tổng của tất cả các quan sát trong một tập dữ liệu chia cho tổng số quan sát.

- Median: Giá trị ở giữa khi dữ liệu được sắp xếp từ nhỏ nhất đến lớn nhất.

- Chế độ: Quan sát xảy ra thường xuyên nhất. Xác định giá trị trung bình và trung vị là bước đầu tiên để hiểu dữ liệu trong quá trình mô tả phân tích. Hai thước đo này thường giống nhau nhưng do giá trị trung bình có thể bị ảnh hưởng bởi lies (giá trị cực trị trong tập dữ liệu), có thể có sự khác biệt lớn giữa chúng. Nếu có là các giá trị ngoại lệ trong dữ liệu thì giá trị trung vị sẽ thể hiện tốt hơn giá trị trung tâm trong dữ liệu tập dữ liệu. Chế độ rất hữu ích trong các tập dữ liệu có số lượng nhỏ các giá trị duy nhất. Ví dụ, một báo cáo tuổi nợ phải thu có thể có giá trị 30, 60 và 90 ngày. Một chế độ lão hóa dữ liệu báo cáo sẽ tiết lộ danh mục nào có nhiều quan sát nhất. Nếu có ít lần lặp lại giá trị, thì chế độ không phải là thước đo hữu ích cho xu hướng trung tâm. Excel được sử dụng ở đây để tính giá trị trung bình và trung vị cũng như giải thích kết quả, nhưng nhiều công cụ có thể tính giá trị trung bình và trung vị. Trên thực tế, tất cả các phần mềm trực quan hóa dữ liệu đều có thể tính toán trung bình và trung vị. Bất kể nó được tính toán như thế nào, có hai điều quan trọng:

- Hiểu cách tính số đo.

- Biết cách diễn giải kết quả. Tính toán số đo vị trí Chúng ta sẽ sử dụng lại ví dụ ở trường đại học để minh họa cách tính giá trị trung bình, trung vị, và chế độ. Tuy nhiên, thay vì tài sản, chúng tôi sẽ thực hiện phân tích mô tả về trường đại học. bảng lương. Dữ liệu Hình minh họa 2.36 là một đoạn trích từ bộ dữ liệu bảng lương của trường đại học. Bộ dữ liệu hiển thị cột chức danh nhân viên và mức lương hàng năm cho tất cả nhân viên trường đại học (10,789 nhân viên).

ngoại hối B C Trang 1 10790 10791 Điều phối viên chương trình học giả nổi tiếng học giả nổi tiếng Quản trị mạng giáo sư 10789 Phó giáo sư $ 94.626,00 $141,939.00 Trợ lý giáo sư $87,454.00 $48,874.00 $ 23,998,00 $ 59.196,00 $ 57.633,00 Tiêu đề Lương hàng năm Tự động Lưu Oﬀ Dữ liệu bảng lương của trường đại học Hai bước đầu tiên liên quan đến các hàm Excel:

- 1. Tính giá trị trung bình bằng hàm AVERAGE trong Excel. Công thức là =AVERAGE (C2:C10790). Kết quả là $40,065.88.

- 2. Tính số trung vị bằng hàm MEDIAN trong Excel. Công thức là =MEDIAN (C2:C10790). Kết quả là $28,276.00. So sánh hai thước đo cho thấy sự khác biệt lớn giữa giá trị trung bình và giá trị trung vị lương hàng năm cho một nhân viên ($11.789,88). Điều gì có thể gây ra điều này? Hãy nhớ rằng, có nghĩa là có thể bị ảnh hưởng bởi các ngoại lệ. Dữ liệu có thể được kiểm tra thêm để xác định xem có mức độ cực kỳ cao hay không hoặc mức lương thấp.

- 3. Cuối cùng, sử dụng tùy chọn bộ lọc Excel trong tệp dữ liệu để lọc mức lương từ cao nhất đến thấp nhất. Hình minh họa 2.37 cho thấy 5 mức lương cao nhất và 5 mức lương thấp nhất. MINH HỌA 2.36 Đại học Dữ liệu tiền lương MINH HỌA 2.37 Đại học Mức lương cao nhất đến thấp nhất ngoại hối A B Trang 1 giáo sư giáo sư giáo sư giáo sư $ 426.091,00 $ 425.000,00 $ 406.909,00 $ 397.118,00 giáo sư $468,675.00 Mã Số Nhân Viên Bộ lọc hàng đầu: Năm mức lương đại học hàng đầu Bộ lọc dưới cùng: Năm mức lương đại học dưới cùng Tiêu đề C Lương hàng năm Tự động Lưu Oﬀ ngoại hối A B Trang 1 Trợ lý nghiên cứu sau đại học Trợ lý tốt nghiệp Trợ lý tốt nghiệp giáo sư $159,00 $152,00 $123,00 Nghệ sĩ đồ họa xuất bản $172,00 Mã Số Nhân Viên Tiêu đề C Lương hàng năm Tự động Lưu Oﬀ $78,00 C2 C6 $ 468.675,00 Có sự khác biệt lớn giữa mức lương cao nhất nhân viên và thấp nhất nhân viên được trả lương $78,00

Do mức lương trung bình cao hơn bao nhiêu so với mức lương trung vị, nên có khả năng mức lương thấp hơn so với mức lương cao hơn. Chúng ta có thể hiểu rõ hơn sự khác biệt sự khác biệt giữa số tiền lương trung bình và trung vị bằng cách xem xét mức độ biến động trong dữ liệu. Các biện pháp phân tán Trong ví dụ về tiền lương, có sự khác biệt lớn giữa mức trung bình và mức trung bình hàng năm. số tiền lương. Các phép đo độ phân tán, mô tả mức độ biến đổi trong dữ liệu, có thể giúp tìm ra nguyên nhân của sự chênh lệch này. Dữ liệu có được trải rộng ra hay chúng nhỏ gọn? trong nói cách khác, tất cả các quan sát hoặc điểm dữ liệu cách nhau bao xa so với giá trị trung bình? Phương sai và độ lệch chuẩn Có hai biện pháp phân tán được sử dụng rộng rãi:

- Phương sai là khoảng cách bình phương trung bình giữa các điểm dữ liệu trong tập dữ liệu và giá trị trung bình.

- Độ lệch chuẩn là căn bậc hai của phương sai. Mặc dù phương sai là cần thiết để tính độ lệch chuẩn nhưng thông thường chỉ có độ lệch chuẩn được sử dụng. được báo cáo đồng minh vì nó dễ diễn giải hơn phương sai. Nó dễ hiểu hơn vì nó có cùng đơn vị với giá trị trung bình. Trong ví dụ về bảng lương của trường đại học, độ lệch chuẩn sẽ bằng đô la tiền lương hàng năm. Tính toán độ phân tán Dữ liệu Các phép đo độ phân tán có thể được tính toán bằng Microsoft Excel (Minh họa 2.38). MINH HỌA 2.38 Đại học Dữ liệu tiền lương ngoại hối B C Trang 1 10790 10791 10792 10793 Điều phối viên chương trình học giả nổi tiếng học giả nổi tiếng Quản trị mạng giáo sư 10789 Phó giáo sư $ 94.626,00 $141,939.00 Trợ lý giáo sư $87,454.00 $48,874.00 $ 23,998,00 $ 59.196,00 Độ lệch chuẩn Phương sai =VAR(C2:C10790) =STDEV(C2:C10790) $ 57.633,00 Tiêu đề Lương hàng năm Tự động Lưu Oﬀ Dữ liệu bảng lương của trường đại học Một lần nữa, hãy tính toán các số đo này bằng cách thực hiện các phép tính trong Excel: 1. Tính phương sai bằng hàm VAR trong Excel. Công thức là =VAR(C2:C10790). Kết quả là $1.939.797.496,92 2. Tiếp theo, tính độ lệch chuẩn bằng hàm STDEV trong Excel. Công thức là =STDEV(C2:C10790). Kết quả là $44,043.13 Mặc dù không có cách giải thích thực tế về số phương sai, nhưng có tiêu chuẩn độ lệch:

- Độ lệch chuẩn thấp cho thấy các quan sát trong tập dữ liệu có xu hướng gần với trung bình của tập dữ liệu.

- Độ lệch chuẩn cao cho thấy các giá trị được trải rộng trên một phạm vi rộng hơn.

Trong ví dụ này, độ lệch chuẩn là 44.043,14 USD chỉ ra rằng một quan sát, trong trường hợp này Mức lương hàng năm của một nhân viên trong tập dữ liệu có thể thay đổi 44.043,14 USD so với mức trung bình. thu hồi rằng giá trị trung bình là 40.068,88 USD, vì vậy 44.043,14 USD sẽ được coi là độ lệch chuẩn cao. Một cách khác để đánh giá độ phân tán là sử dụng biểu đồ phân tán (còn gọi là biểu đồ phân tán) để trực quan hóa dữ liệu (Minh họa 2.39).

Biểu đồ phân tán bảng lương $0 50.000 USD 2.000 4.000 6.000 Mã số nhân viên 8.000 10.000 12.000 100.000 USD 150.000 USD 200.000 USD 250.000 USD 300.000 USD 350.000 USD 400.000 USD 450.000 USD 500.000 USD Lương hàng năm Bảng lương đại học Mức lương được phân bổ rộng rãi trong khoảng từ 0 USD đến hơn 450.000 USD một chút. Sự hình dung này của dữ liệu trùng khớp với độ lệch chuẩn lớn là 44.043,14 USD Số đo hình dạng Bên cạnh việc hiểu sự phân tán của dữ liệu, điều quan trọng là phải hiểu sự phân tán của nó. sự vận động hoặc hình dạng. Các thước đo hình dạng mô tả sự phân bố của dữ liệu trong tập dữ liệu. Làm thế nào một tập dữ liệu được định hình có thể tiết lộ thước đo tốt nhất về xu hướng sử dụng trung tâm hoặc nó có thể hiển thị các mẫu trong dữ liệu. Độ lệch và Kurtosis Các tập dữ liệu có hình dạng đối xứng hoặc không đối xứng. Trong phân bố đối xứng, giá trị trung bình, trung vị và mốt bằng nhau và phân bổ dữ liệu ở bên phải của gương trung bình dữ liệu ở bên trái của giá trị trung bình. Một phân bố đối xứng sẽ trông giống như một đường cong hình chuông đồ thị (Minh họa 2.40).

Phân phối đối xứng Trung bình/Trung bình/Chế độ Hình dạng của phân bố có thể được xác định bằng cách vẽ đồ thị dữ liệu hoặc bằng cách sử dụng hai biện pháp thực tế. Thông thường, cả hai đều phù hợp. Hai thước đo hình dạng là độ lệch và độ nhọn. Skewness mô tả sự thiếu tính đối xứng của dữ liệu:

- Phân phối ở bên phải giá trị trung bình được coi là có độ lệch dương.

- Phân phối ở bên trái giá trị trung bình bị lệch âm.

Hệ số độ lệch (CS) đo độ lệch của phân phối. Nếu CS là âm thì dữ liệu sẽ bị lệch sang bên trái (đuôi về bên trái). Nếu CS dương, dữ liệu là lệch phải (đuôi lệch sang phải). Mức độ sai lệch có thể được giải thích bằng giá trị tuyệt đối giá trị của CS:

- |CS| > 1, độ lệch cao

- 0,5 ≤ |CS| ≥ 1, độ lệch vừa phải

- |CS| < 0,5, tính đối xứng tương đối Tính hệ số độ lệch bằng hàm Excel =SKEW(phạm vi dữ liệu). dữ liệu Hình minh họa 2.42 thể hiện hàm và kết quả Excel sử dụng file dữ liệu bảng lương của trường đại học. CS là dương 2,3, cho thấy dữ liệu có mức độ sai lệch cao và sai lệch so với đúng. MINH HỌA 2.41 Độ lệch Ví dụ Độ lệch dương đối xứng Phân phối Độ lệch âm Chế độ trung vị Nghĩa là Trung bình/Trung bình/Chế độ Chế độ trung vị Nghĩa là MINH HỌA 2.42 Độ lệch và Kurtosis của dữ liệu bảng lương đại học chức năng Đo lường =SKEW(C2:C10790) =KURT(C2:C10790) kết quả CS CK 2.3 8.2 Kurtosis đề cập đến mức độ đỉnh hoặc phẳng của biểu đồ dữ liệu. Hệ số Kur- tosis (CK) đo mức độ nhọn của phân phối:

- Nếu CK lớn hơn 3 thì dữ liệu có phần đạt đỉnh với độ phân tán ít hơn.

- Nếu CK nhỏ hơn 3, dữ liệu có phần ổn định với mức độ phân tán rộng. Hệ số nhọn có thể được tính trong Excel bằng hàm =KURT(phạm vi dữ liệu). Hình minh họa 2.42 cho thấy CK của dữ liệu tiền lương của trường đại học là 8,2. Điều này cho thấy dữ liệu được đạt cực đại với độ phân tán ít hơn. Phân phối tần số và biểu đồ Cùng với các thước đo CS và CK, hình dạng của phân phối có thể được hình dung bằng hai các biện pháp khác:

- Phân bố tần số là sự biểu diễn dữ liệu tóm tắt số của các quan sát trong một khoảng thời gian nhất định. Ví dụ: số lượng nhân viên theo mức lương các nhóm đô la.

- Biểu đồ là biểu đồ thanh phân bố tần số trong đó chiều cao của thanh phản ánh tần số trong khoảng. Ví dụ: chúng ta có thể muốn nhóm tiền lương theo số tiền đô la là 10.000 đô la, 20.000 đô la và 30.000 đô la và sau đó đếm xem có bao nhiêu nhân viên nằm trong mỗi loại. Các biện pháp này có thể được tạo trong phần mềm trực quan hóa dữ liệu như Power BI, Tableau và trong Microsoft Excel bằng cách sử dụng Analysis Toolpak. Analysis Toolpak là một tiện ích bổ sung miễn phí dành cho Excel. Sau khi thêm, nó sẽ nằm trong tab Dữ liệu. Hình minh họa 2.43 cho thấy nơi tìm Dữ liệu Công cụ phân tích và hộp tương ứng sẽ mở ra sau khi nhấp vào Phân tích dữ liệu. Hình minh họa 2.41 cho thấy sự phân bố lệch dương, đối xứng và lệch âm.

Xem lại Xem Nhà phát triển Trợ giúp Power Pivot Tab mới Chia sẻ Chia sẻ ngoại hối A B Trang 1 Tự động Lưu Oﬀ được rồi Hủy bỏ Trợ giúp Phân tích dữ liệu Công cụ phân tích ? Anova: Hai yếu tố với sự nhân rộng Anova: Hai yếu tố không cần nhân rộng Tương quan Hiệp phương sai Thống kê mô tả Làm mịn theo cấp số nhân F-Test Hai mẫu cho phương sai Phân tích Fourier biểu đồ Đường trung bình động Phân tích Phân tích Truy vấn & Kết nối Truy vấn & Kết nối Chỉnh sửa liên kết Thuộc tính Làm mới Tất cả Nhắn tin tới Cột Công cụ dữ liệu Địa lý chứng khoán Kiểu dữ liệu Tab mới Sắp xếp Lọc Xóa Đăng ký lại Nâng cao Sắp xếp & Lọc dữ liệu dữ liệu Phân tích Bộ giải Phân tích Phân tích Phân tích Truy vấn & Kết nối Truy vấn & Kết nối Chỉnh sửa liên kết Thuộc tính Làm mới Tất cả Nhắn tin tới Cột Công cụ dữ liệu Địa lý chứng khoán Kiểu dữ liệu Tab mới Sắp xếp Lọc Xóa Đăng ký lại Nâng cao bụng Quảng cáo bụng Sắp xếp & Lọc Bộ giải

- **1. Để chuẩn bị biểu đồ và phân bổ tần số, hãy chọn Biểu đồ và nhấp vào OK .**

- **2. Một hộp thoại mở ra ( Minh họa 2.44 ).**

- **3. Có hai ô nhập liệu:**

- Phạm vi đầu vào là dữ liệu sẽ được hiển thị. Sẽ rất hữu ích khi chọn cột tiêu đề và chọn hộp Nhãn để biểu đồ được gắn nhãn với tiêu đề của dữ liệu được hình dung (Minh họa 2.44 ).

- Ô nhập tiếp theo là Bin Range , xác định các nhóm được sử dụng cho tần số thanh phân phối và biểu đồ. Những điều này phải được thiết lập trước khi mở hộp thoại hộp. Tạo Phạm vi Bin bằng cách thiết lập một cột chứa các giá trị trong đó dữ liệu nên được nhóm lại. Nói chung, các giá trị phải có mức tăng bằng nhau và số- số lượng nhóm nên từ năm đến mười lăm. 4. Cuối cùng, chọn nơi xuất dữ liệu. Hãy chắc chắn kiểm tra hộp Đầu ra biểu đồ trước khi nhấn OK. MINH HỌA 2.44 Biểu đồ Hộp thoại được rồi Hủy bỏ Trợ giúp biểu đồ đầu vào Phạm vi đầu vào: Phạm vi thùng: Tùy chọn đầu ra Phạm vi đầu ra: Sổ làm việc mới Lớp bảng tính mới: Pareto (biểu đồ được sắp xếp) Phần trăm tích lũy Đầu ra biểu đồ ? Nhãn

Làm thế nào để bạn biết có bao nhiêu nhóm để tạo? Cách tốt nhất là thử nghiệm với dữ liệu để tìm số sẽ tạo ra một hình ảnh trực quan hữu ích. Ví dụ: sử dụng ít nhóm hơn có nghĩa là độ rộng của nhóm sẽ rộng hơn và hình ảnh trực quan có thể cung cấp cái nhìn sâu sắc ít chi tiết hơn. Việc chia phạm vi (quan sát tối đa - quan sát tối thiểu) thường hữu ích cho số nhóm bạn muốn hiển thị làm điểm bắt đầu. Dữ liệu Bạn có thể sử dụng các bước này để tạo biểu đồ với tệp dữ liệu bảng lương của trường đại học:

- **1. Mở bảng tính và tạo cột cho các thùng.**

- 2. Đầu tiên, hãy xác định phạm vi dữ liệu. Mức lương tối thiểu là $78,00 và mức lương tối đa mức lương là $468.675,00, cho thấy có rất nhiều dữ liệu. Tạo 12 thùng, bắt đầu bằng 8.000 USD với số gia tăng 20.000 USD (Minh họa 2.45). MINH HỌA 2.45 Dữ liệu tiền lương, Hộp thoại Thùng và Biểu đồ ngoại hối B C Trang 1 10789 10790 Điều phối viên chương trình học giả nổi tiếng học giả nổi tiếng Quản trị mạng giáo sư Phó giáo sư $ 94.626,00 $141,939.00 Trợ lý giáo sư $87,454.00 $48,874.00 Điều phối viên chương trình sinh viên $ 42.630,00 giáo sư $113,736.00 giáo sư $ 2.170,00 giáo sư $ 115.228,00 Trợ lý nghiên cứu $ 6.700,00 Trợ lý nghiên cứu $ 6.700,00 Trợ lý nghiên cứu $ 20.100,00 28.000 48.000 68.000 88.000 108.000 128.000 148.000 168.000 188.000 208.000 228.000 giáo sư $ 119.900,00 $ 23,998,00 $ 59.196,00 $ 57.633,00 8.000 Tiêu đề Lương hàng năm E D Thùng Tự động Lưu Oﬀ Hộp thoại Dữ liệu Bảng lương, Thùng và Biểu đồ được rồi Hủy bỏ Trợ giúp biểu đồ đầu vào Phạm vi đầu vào: Phạm vi thùng: Tùy chọn đầu ra Phạm vi đầu ra: Sổ làm việc mới Lớp bảng tính mới: Pareto (biểu đồ được sắp xếp) Phần trăm tích lũy Đầu ra biểu đồ ? Nhãn $C$1:$C$10790 $E$4:$E$15 Kết quả từ hộp thoại biểu đồ được trình bày trong Hình minh họa 2.46.

2,873 biểu đồ Thùng lương (tính bằng nghìn) Tần số 2.169 1.241 2,504 $8K 1.000 1.500 2.000 2.500 3.000 3.500 28K 48K 68K 88K 108K 128K 148K 168K 188K 208K 228K Thêm 8.000 28.000 48.000 68.000 88.000 108.000 128.000 148.000 168.000 188.000 208.000 228.000 Thêm 2,504 2,873 2.169 1.241 23,21% 26,63% 20,10% 11,50% 6,98% 4,32% 2,46% 1,50% 0,95% 0,67% 0,77% 0,37% 0,55% Thùng Tần số % tần số Biểu đồ hiển thị một số thông tin về hình dạng của tập dữ liệu, bao gồm cả thông tin đó hầu hết dữ liệu được nhóm trong khoảng từ 8.000 đến 48.000 USD:

- Dữ liệu sau đó sẽ di chuyển sang bên phải. Điều này hỗ trợ kết quả của các phép đo vị trí và hình dạng. Hãy nhớ lại giá trị trung bình của dữ liệu là $28.276,00 và giá trị trung bình là $40.065,88. các dữ liệu đạt đỉnh ở chế độ này.

- Sau đó, dữ liệu sẽ chuyển sang bên phải, hỗ trợ cho kết quả về hệ số lệch tính tích cực 2.3.

- Cuối cùng, dữ liệu đạt đỉnh cao. Phần lớn (69%) nằm trong ba thanh đầu tiên trên biểu đồ. Điều này hỗ trợ kết quả cho hệ số nhọn là 8,2 cho thấy dữ liệu đạt đỉnh cao với độ phân tán ít hơn. Công cụ thống kê mô tả Bây giờ bạn đã học cách tính các số đo vị trí, độ phân tán và hình dạng bằng cách sử dụng sin- gle các hàm Excel. Có một công cụ Excel khác, Thống kê mô tả, tính toán tất cả những điều này. biện pháp ngay lập tức (Minh họa 2.47): 1. Chọn Thống kê mô tả từ danh sách Công cụ phân tích. 2. Sử dụng hộp thoại Thống kê mô tả để nhập phạm vi dữ liệu cần phân tích. 3. Sau khi nhập phạm vi dữ liệu, hãy chọn nhãn (nếu bạn chọn hàng có tiêu đề cột), chọn nơi đầu ra sẽ đi, chọn Thống kê tóm tắt và nhấp vào OK. MINH HỌA 2.47 Mô tả Công cụ và hộp thoại thống kê Excel hộp được rồi Hủy bỏ Trợ giúp Phân tích dữ liệu Công cụ phân tích ? Anova: Yếu tố đơn lẻ Anova: Hai yếu tố với sự nhân rộng Anova: Hai yếu tố không cần nhân rộng Tương quan hiệp phương sai Thống kê mô tả Làm mịn theo cấp số nhân F-Test Hai mẫu cho phương sai Phân tích Fourier biểu đồ Lưu ý rằng Thùng và Tần số được tạo bởi Excel khi biểu đồ được tạo. Cột cho % Tần suất là được tính bằng cách chia Tần suất cho mỗi thùng cho tổng số quan sát (10.789).

được rồi Hủy bỏ Trợ giúp Thống kê mô tả đầu vào Cột Hàng Phạm vi đầu vào: Được nhóm theo: Tùy chọn đầu ra Phạm vi đầu ra: Sổ làm việc mới Lớp bảng tính mới: Thống kê tóm tắt Mức độ tin cậy cho giá trị trung bình: Kth nhỏ nhất: Lớn thứ K: $C$1:$C$10790 % ? Nhãn ở hàng đầu tiên

Sau đó, Excel sẽ tính toán số liệu thống kê mô tả và in kết quả trên một công việc mới- tờ (Minh họa 2.48).

Thống kê mô tả dữ liệu tiền lương Nghĩa là Lỗi chuẩn trung vị Chế độ Độ lệch chuẩn Phương sai mẫu Kurtosis Độ lệch Phạm vi tối thiểu Tối đa Tổng Đếm 40.065,88 USD $424,02 $ 28,276,00 $ 3,269,00 44.043,13 USD 1.939.797.496,92 USD $8,19 $ 2,30 $ 468.597,00 $78,00 $ 468.675,00 $ 432.270.823,00 10.789,00 Lương hàng năm Các gói phần mềm thống kê thường có tính năng tương tự để tính toán nhiều mô tả. thống kê tích cực cùng một lúc. Cho dù chúng ta sử dụng nhiều hàm Excel đơn lẻ hay chỉ một hàm để tính toán nó, việc làm rõ hình dạng của tập dữ liệu giúp chúng ta hiểu rõ hơn về dữ liệu. Ngoài ra còn có một thành phần quan trọng khác – hiểu các mối quan hệ trong một tập dữ liệu. Phân tích tương quan Phân tích tương quan có thể tiết lộ mối quan hệ trong dữ liệu bằng cách đo lường mối quan hệ tuyến tính giữa hai biến. Bước đầu tiên là hiểu các biến số có mối tương quan như thế nào và bước thứ hai liên quan đến việc tính toán mối tương quan. Giải thích các hệ số tương quan Tương quan tuyến tính của các biến liên tục được đo bằng hệ số tương quan, còn được gọi là Hệ số tương quan thời điểm sản phẩm Pearson. Thước đo này là một con số giá trị giữa −1 và +1. Số tuyệt đối càng cao thì sức mạnh của mối quan hệ.

Mối tương quan có thể âm, bằng 0 hoặc dương (Minh họa 2.49):

- Tương quan âm là mối quan hệ nghịch đảo. Khi một biến tăng lên thì biến kia giảm đi. Có mối quan hệ nghịch biến giữa doanh số bán súp và nhiệt độ vì khi nhiệt độ giảm, doanh số bán súp tăng lên.

- Không có mối tương quan cho thấy không có mối quan hệ giữa các biến. Chúng tôi sẽ không mong đợi Ví dụ: nhiệt độ ngoài trời có tác động đến việc bán ngũ cốc.

- Hệ số tương quan dương chỉ ra rằng khi một biến tăng thì biến khác. Chúng tôi mong đợi một mối quan hệ tích cực giữa doanh số bán kem và nhiệt độ cửa. Khi nhiệt độ tăng, doanh số bán kem cũng có xu hướng tăng. MINH HỌA 2.49 Tương quan Ví dụ Nhiệt độ bán súp ngũ cốc Bán kem tiêu cực số không tích cực Chúng ta cũng có thể xem xét sức mạnh của một mối quan hệ. Hệ số tương quan càng cao thì giữa số âm 1 và số 1 dương thì mối tương quan càng mạnh. Hình minh họa 2.50 là hướng dẫn để xác định xem hệ số tương quan cho thấy mối quan hệ yếu, trung bình hay mạnh. MINH HỌA 2.50 Phiên dịch Hệ số tương quan −0,70 −0,50 −0,30 Mối quan hệ tuyến tính tiêu cực vừa phải Mối quan hệ tuyến tính tiêu cực yếu Không có mối quan hệ tuyến tính Chính xác −1 +0,50 +0,70 Chính xác +1 +0,30 Mối quan hệ tuyến tính phủ định hoàn hảo Mối quan hệ tuyến tính tiêu cực mạnh mẽ Mối quan hệ tuyến tính tích cực mạnh mẽ Một mối quan hệ tuyến tính tích cực hoàn hảo Mối quan hệ tuyến tính tích cực yếu Một mối quan hệ tuyến tính tích cực vừa phải Phiên dịch Tương quan r Hãy tưởng tượng xem xét mối quan hệ giữa doanh số bán kem và nhiệt độ ngoài trời. ture. Nếu hệ số tương quan giữa doanh số bán hàng và nhiệt độ là dương 0,75 thì có mối quan hệ tích cực mạnh mẽ giữa doanh số bán hàng và nhiệt độ. Khi nhiệt độ tăng lên, doanh số bán nước đá kem tăng lên và ngược lại. (Minh họa 2.51) MINH HỌA 2.51 Tích cực Ví dụ tương quan Nhiệt độ tăng Hệ số tương quan của kem Bán hàng và Nhiệt độ Doanh số tăng $

$ Chi phí sưởi ấm tăng Nhiệt độ giảm Hệ số tương quan của hệ thống sưởi Chi phí và nhiệt độ

Ví dụ tương quan

Dữ liệu về lương và giờ ngoại hối F G Trang 1 10789 10790 Điều phối viên chương trình học giả nổi tiếng học giả nổi tiếng Quản trị mạng giáo sư Phó giáo sư $ 94.626,00 $141,939.00 Trợ lý giáo sư $87,454.00 $48,874.00 Điều phối viên chương trình sinh viên $ 42.630,00 1.530 2.040 2.040 $ 23,998,00 $ 59.196,00 387,6 $ 57.633,00 2.040 Tiêu đề Lương hàng năm H Giờ Đã Làm Việc Tự động Lưu Oﬀ Dữ liệu về lương và giờ của trường đại học Hình 2.54 hiển thị hộp thoại tương quan mở ra sau khi nhấn vào Correlation và chọn OK trong menu thả xuống Công cụ phân tích dữ liệu. Phạm vi đầu vào trong hộp thoại Trong trường hợp này, có mối tương quan nghịch mạnh mẽ giữa chi phí sưởi ấm và nhiệt độ. Khi nhiệt độ giảm, chi phí sưởi ấm trong nhà tăng lên và ngược lại. Thực hiện phân tích tương quan Mối tương quan có thể được đánh giá một cách trực quan bằng cách chuẩn bị một biểu đồ phân tán, giống như trong Hình minh họa 2.49, rồi vẽ một đường. Điều này sẽ cho biết liệu mối tương quan có tồn tại hay không và nó là tích cực hay tiêu cực. Hệ số tương quan có thể được tính bằng tay bằng công thức hoặc bằng phần mềm. Tất cả phần mềm thống kê có thể tính toán hệ số tương quan, bao gồm cả Microsoft Excel, được sử dụng trong ví dụ này. Bất kể phần mềm được sử dụng là gì, việc giải thích kết quả là giống nhau. Có hai cách để thực hiện phân tích tương quan trong Excel:

- Sử dụng hàm CORREL.

- Sử dụng tùy chọn Tương quan trong công cụ Phân tích Dữ liệu. Lợi ích của việc sử dụng tùy chọn Tương quan trong công cụ Phân tích Dữ liệu là bảng tương quan vì có thể tạo nhiều biến cùng một lúc. Dữ liệu Chúng tôi sử dụng khoản thanh toán của trường đại học- cuộn dữ liệu để minh họa tùy chọn tương quan trong Excel và sau đó diễn giải kết quả. Trong tab Số giờ trả lương trong tệp dữ liệu (Minh họa 2.53), thực hiện phân tích tương quan để xem liệu có mối tương quan giữa mức lương hàng năm và số giờ làm việc hay không. Thay vào đó, giả sử chúng ta đang kiểm tra mối quan hệ giữa chi phí sưởi ấm và nhiệt độ. ture và hệ số tương quan là âm 0,70 (Minh họa 2.52)

hộp chứa các cột đang được kiểm tra sự tương quan. Ví dụ này đang kiểm tra mối tương quan giữa cột G (Lương hàng năm) hàng 1 – 10790 và cột H (Số giờ làm việc) hàng 1 – 10790.

Công cụ phân tích và mối tương quan Hộp thoại được rồi Hủy bỏ Trợ giúp Phân tích dữ liệu Công cụ phân tích ? Anova: Yếu tố đơn lẻ Anova: Hai yếu tố với sự nhân rộng Anova: Hai yếu tố không cần nhân rộng Tương quan Hiệp phương sai Thống kê mô tả Làm mịn theo cấp số nhân F-Test Hai mẫu cho phương sai Phân tích Fourier biểu đồ được rồi Hủy bỏ Trợ giúp Tương quan đầu vào Cột Hàng Phạm vi đầu vào: Được nhóm theo: Tùy chọn đầu ra Phạm vi đầu ra: Sổ làm việc mới Lớp bảng tính mới: $G$1:$H$10790 $J$3 ? Nhãn ở hàng đầu tiên Hộp thoại trong Hình minh họa 2.54 hiển thị các đầu vào cần thiết để chạy phân tích tương quan. ysis. Kết quả phân tích tương quan được thể hiện ở Hình minh họa 2.55:

- Hệ số tương quan là 0,552.

- Có mối tương quan dương giữa mức lương hàng năm và số giờ làm việc. Nói cách khác, khi số giờ làm việc tăng thì mức lương hàng năm cũng tăng. MINH HỌA 2.55 Đại học Phân tích tương quan tiền lương Lương hàng năm 0,552 Số giờ đã làm việc Lương hàng năm Số giờ đã làm việc Tại sao không có mối tương quan mạnh mẽ hơn? Mối tương quan chặt chẽ giữa số giờ làm việc và số tiền lương hàng năm được trả có vẻ hợp lý. Tuy nhiên, nếu nhân viên được trả lương mức lương cố định hàng năm thay vì theo giờ sẽ làm giảm mối tương quan với số giờ. Phân tích tương quan có thể giúp khám phá các mối quan hệ trong dữ liệu và hiểu được chúng sức mạnh. Nhưng đừng bao giờ cho rằng một biến gây ra sự thay đổi ở biến kia vì có mối tương quan giữa hai. Có thể tìm thấy mối tương quan giữa hai biến có không có gì liên quan đến nhau Đây là mối tương quan giả, xảy ra khi có mối quan hệ toán học, nhưng không phải là logic, giữa hai biến. Luôn đảm bảo sự tương quan những điều này có ý nghĩa trước khi sử dụng nó để đưa ra quyết định.

Áp dụng nó 2.4 Sử dụng mô tả Thống kê để kiểm toán Chi phí bảo hành Dữ liệu Kiểm toán Với tư cách là kiểm toán viên bên ngoài, bạn đã được chỉ định tham gia hợp đồng kiểm toán cho Super Xe tay ga. Một trong những trách nhiệm của bạn là xem xét chi phí bảo hành. Như hình minh họa cho thấy, trung bình chi phí bảo hành cho Super Scooters đã tăng lên trong ba năm qua. $0 $50 100 USD $150 $200 $250 $300 $350 $400 $450 Chi phí bảo hành trung bình trung bình Bảo hành chi phí Năm Để phân tích chi phí bảo hành, bạn đã quyết định sử dụng số liệu thống kê mô tả. Thực hiện như sau phân tích và giải thích kết quả của bạn.

- 1. Sử dụng tùy chọn Thống kê mô tả trong công cụ Phân tích dữ liệu để tính toán thống kê mô tả. chính sách chi phí bảo hành từ năm 2023 đến năm 2025. Giải thích các biện pháp sau: • Trung bình • Trung vị • Độ lệch chuẩn • Kurtosis • Độ lệch

- 2. Thống kê mô tả chi phí bảo hành năm 2025. Giải thích các biện pháp sau: • Trung bình • Trung bình • Kurtosis • Độ lệch

- 3. Lập biểu đồ Chi phí bảo hành năm 2025 với các thùng sau: 200, 400, 600, 800, 1000, 1200 và 1.400. • Lập biểu đồ dữ liệu. • Hình dạng và sự phân bố biểu đồ của bạn có hỗ trợ độ nhọn và độ lệch không biện pháp?

GIẢI PHÁP

- **1. Thống kê mô tả chi phí bảo hành giai đoạn 2023 - 2025:**

343,57 4.06 244,90 59.977,92 1,54 1,23 1,493 1.500 1.252.326 3.645 Nghĩa là Lỗi chuẩn trung vị Chế độ Độ lệch chuẩn Phương sai mẫu Kurtosis Độ lệch Phạm vi tối thiểu Tối đa Tổng Đếm Tổng số bảo hành

Đo lường giải thích: Đo lường kết quả Phiên dịch Nghĩa là Chi phí bảo hành trung bình cho trong thời gian 3 năm là $343,57. Chi phí bảo hành trung bình cho toàn bộ 3.645 sản phẩm bán ra trong thời gian 3 năm là $343,57. trung vị Chi phí bảo hành trung bình cho thời hạn 3 năm là $300,00. Giá trị trung bình của chi phí bảo hành cho thời hạn 3 năm, khi xếp hạng bảo hành chi phí từ cao đến thấp là 300$. Tiêu chuẩn sự lệch lạc Độ lệch chuẩn trên trong thời gian 3 năm là $244,90. Đây là độ lệch chuẩn cao so với đến số trung bình và số trung vị. Nó biểu thị một phạm vi rộng phân tán chi phí bảo hành. Đối với bất kỳ lần bán hàng nào, chi phí bảo hành có thể bằng + hoặc − $244,90 so với giá trị trung bình. Kurtosis Hệ số kurtosis là 1,54. Giá trị này nhỏ hơn 3, biểu thị rằng hình dạng của sự phân phối có phần bằng phẳng với một mức độ phân tán rộng. Độ lệch Hệ số độ lệch là dương 1,23. Giá trị này lớn hơn 1, chứng tỏ rằng đỉnh dữ liệu xung quanh giá trị trung bình và sau đó đuôi lệch sang bên phải.

- 2. Thống kê mô tả chi phí bảo hành năm 2025: 414,18 7.551634 276,13 76.245,34 0,93 1.18 1.460 1.500 553.759 1.337 Nghĩa là Lỗi chuẩn trung vị Chế độ Độ lệch chuẩn Phương sai mẫu Kurtosis Độ lệch Phạm vi tối thiểu Tối đa Tổng Đếm Tổng số bảo hành–2025

Đo lường giải thích: Đo lường kết quả Phiên dịch Nghĩa là Chi phí bảo hành trung bình cho Năm 2025 là $414,18. Con số này cao hơn mức trung bình ba năm tìm thấy ở câu hỏi 1. trung vị Chi phí bảo hành trung bình cho Năm 2025 là $330,00. Điều này thể hiện chính xác phần giữa của phân phối nếu dữ liệu được sắp xếp từ thấp nhất đến cao nhất. Kurtosis Hệ số kurtosis là 0,93. Con số này nhỏ hơn ba, cho thấy rằng hình dạng của sự phân bố hơi bằng phẳng với mức độ phân tán rộng. Độ lệch Hệ số độ lệch là dương 1,18. Giá trị này lớn hơn một, biểu thị dữ liệu đạt đỉnh xung quanh giá trị trung bình và sau đó tắt dần bên phải.

- 3. Biểu đồ: Thùng Tần số 1.000 1.200 1.400 Thêm biểu đồ Có, độ nhọn biểu thị sự phân tán rộng. Chi phí bảo hành được trải đều từ 200 USD đến 1.200 USD:

- Có ba đỉnh và một đỉnh cao. Độ lệch biểu thị các đỉnh dữ liệu xung quanh trung bình và sau đó đuôi sang bên phải.

---

# PHẦN VI: TRỰC QUAN HÓA DỮ LIỆU VÀ DASHBOARD (DATA VISUALIZATION & DASHBOARDS - LO 2.5)

## 2.5 Nguyên tắc và ứng dụng trực quan hóa dữ liệu (Data Visualization Best Practices & Tableau/Power BI)

Có hai loại trực quan hóa dữ liệu:

- Trực quan hóa dữ liệu thăm dò sử dụng các công cụ và kỹ thuật trực quan hóa dữ liệu để khám phá dữ liệu để tìm hiểu sâu sắc. Trực quan hóa dữ liệu thăm dò giúp hiểu dữ liệu và xác định xác định các mô hình, xu hướng hoặc sự bất thường cơ bản.

- Trực quan hóa dữ liệu giải thích sử dụng các công cụ và kỹ thuật trực quan hóa dữ liệu để giao tiếp truyền đạt kết quả phân tích. Nó được sử dụng để giải thích kết quả phân tích, chỉ ra các mối quan hệ trong dữ liệu và truyền đạt những hiểu biết sâu sắc. Khóa học này cuối cùng sẽ bao gồm cả hai chi tiết hơn. Cuộc thảo luận này giới thiệu cách trực quan các thuật toán phân tích có ý nghĩa đối với các tập dữ liệu lớn, xác định các hình ảnh trực quan phổ biến và khi nào nên sử dụng chúng và giải thích cách tạo chúng trong Microsoft Excel. Nhiều chuyên gia kế toán thích phần mềm trực quan hóa mạnh mẽ hơn như Power BI và Tableau vì Microsoft Excel có khả năng hiển thị dữ liệu hạn chế. Tuy nhiên, việc tạo trực quan hóa trong Excel là một giới thiệu hiệu quả và đơn giản. Tạo cảm giác về các tập dữ liệu lớn Hình dung có tác dụng mạnh mẽ vì nó có thể tiết lộ nhanh chóng và hiệu quả những hiểu biết ẩn giấu trong những thông tin thô sơ. dữ liệu. Hình minh họa 2.56 là bảng tổng hợp doanh thu của một cửa hàng điện máy qua các năm 2023–2025. So sánh bảng với hình ảnh trực quan của nó trong biểu đồ cột. MINH HỌA 2.56 Trực quan hóa Dữ liệu bán hàng Thiết bị gia dụng Máy ảnh Máy tính Phụ kiện máy tính TV Tổng cộng $627,417,576 $ 931,975,979 $ 589,356,617 $ 1,255,786,672 4.760.213.442 USD $ 434,358,182 $ 1,355,676,598 Doanh thu hàng năm Danh mục sản phẩm năm tài chính 2024 Tổng cộng Năm tài chính 2023 $ 217,276,947 $ 434,363,120 327.140.700 USD $ 216,412,502 $ 432,403,786 $ 217,491,906 $ 323,513,274 $ 215,524,232 $ 434,187,852 1.625.075.446 USD $ 486,955,296 năm tài chính 2025 $192,648,723 281.322.005 USD $157,419,883 $ 389,195,034 1.507.540.941 USD 1.627.597.055$ 200.000.000 USD 100.000.000 USD 300.000.000 USD 400.000.000 USD 500.000.000 USD 600.000.000 USD Thiết bị gia dụng Máy ảnh Máy tính Máy tính Phụ kiện TV Doanh thu hàng năm sản phẩm Năm tài chính 2023 năm tài chính 2024 năm tài chính 2025 Biểu đồ doanh số dễ diễn giải hơn:

- Có thể thấy ngay rằng thiết bị gia dụng và TV có doanh số bán hàng cao nhất trong cả ba năm, và chỉ có thiết bị gia dụng có doanh số bán hàng tăng vào năm 2025.

- Tất cả các danh mục sản phẩm khác đều có doanh số năm 2025 thấp hơn hai năm trước đó.

Mặc dù có thể đi đến kết luận tương tự bằng cách sử dụng bảng nhưng việc phát hiện không dễ dàng sự khác biệt hoặc so sánh. Khả năng nhìn thấy nhanh các mô hình và mối quan hệ trong các tập dữ liệu lớn là lý do tại sao kỹ năng trực quan hóa dữ liệu lại quan trọng đến vậy.

Hình dung và thời điểm sử dụng chúng Có rất nhiều loại trực quan có sẵn. Việc xác định sử dụng cái nào được thúc đẩy bởi loại dữ liệu có sẵn và những gì bạn đang cố gắng hiển thị trong hình ảnh trực quan. Trực quan hóa dữ liệu được đề cập chi tiết hơn trong các chương phân tích, giải thích và truyền thông, nhưng tiếp theo là bản tóm tắt một số hình ảnh trực quan phổ biến và cách chọn chúng. Hình dung chung Dữ liệu phân loại là dữ liệu được dán nhãn hoặc đặt tên có thể được sắp xếp thành các nhóm theo đặc điểm. đặc điểm cific. Dữ liệu không có giá trị định lượng. Dữ liệu phân loại được sử dụng trong trực quan hóa để mô tả các nhóm dữ liệu. Hình dung trong Hình 2.56 là một ví dụ sử dụng dữ liệu phân loại. Các loại sản phẩm là các nhóm tóm tắt doanh số bán hàng. giống nhau trực quan hóa cũng bao gồm dữ liệu định lượng dưới dạng số tiền bán hàng. Đặt chúng cùng nhau thể hiện mối quan hệ giữa chủng loại sản phẩm và doanh số bán hàng. Cũng chú ý đến biểu đồ có nhiều năm. Các thanh đại diện cho các năm 2023–2025. Luôn xem xét liệu dữ liệu đang được phân tích có thể được sử dụng theo một cách trực quan cụ thể hay không. chuyện. Ví dụ: việc hiển thị mối quan hệ trong dữ liệu bằng biểu đồ phân tán yêu cầu ít nhất một thước đo định lượng. Hiển thị xu hướng theo thời gian đòi hỏi thước đo thời gian (ngày) cộng với số lượng biện pháp chuẩn độ. Hình minh họa 2.57 liệt kê một số cách trực quan hóa dữ liệu phổ biến cùng với mô tả, tốt nhất thực tiễn và các loại dữ liệu cần thiết để tạo trực quan hóa.

Trực quan hóa sử dụng Thực tiễn tốt nhất Dữ liệu cần thiết Biểu đồ khu vực Biểu thị những thay đổi trong khối lượng theo thời gian.

- Không sử dụng nếu dữ liệu có nhiều hơn bốn loại tránh nhầm lẫn, lộn xộn.

- Bắt đầu trục y ở mức 0 hoặc cao hơn.

- Đặt dữ liệu có tính biến đổi cao lên trên cùng và dữ liệu có mức độ thay đổi thấp sự biến thiên ở phía dưới.

- Trường ngày.

- Ít nhất một định lượng đo lường. Thanh và cột Biểu đồ So sánh các bộ phận với một toàn bộ, làm nổi bật danh mục hoặc hiển thị thay đổi theo thời gian.

- So sánh từ hai đến bảy loại bằng thanh dọc.

- Sử dụng thanh ngang nếu có nhiều hơn bảy danh mục hoặc nhãn danh mục dài.

- Sử dụng nhãn ngang để dễ đọc.

- Thanh dấu cách nên được sử dụng hợp lý và một cách nhất quán.

- Sử dụng màu sắc một cách tiết kiệm hoặc làm điểm nhấn.

- Luôn có đường cơ sở bằng 0.

- Thanh ngang: (thanh biểu đồ) bằng không hoặc nhiều hơn danh mục, một hoặc nhiều biện pháp.

- Thanh dọc: (cột biểu đồ) một hoặc nhiều danh mục, một hoặc nhiều các biện pháp định lượng. Biểu đồ bong bóng So sánh độc lập những giá trị có sự khác biệt khoảng trống hoặc ngoại lệ.

- Dán nhãn bong bóng và đảm bảo chúng có thể nhìn thấy được.

- Chia kích thước bong bóng theo diện tích chứ không phải theo đường kính.

- Không sử dụng bong bóng nếu chúng có kích thước tương tự nhau.

- Một hoặc nhiều danh mục.

- Một hoặc nhiều định lượng biện pháp. Biểu đồ biểu đồ Hiển thị tần số phân phối.

- Sử dụng đường cơ sở bằng 0.

- Chọn số lượng thùng thích hợp:

- Thùng là những con số đại diện cho khoảng thời gian dữ liệu nào sẽ được nhóm lại.

- Các thùng xác định các nhóm được sử dụng cho tần số phân phối.

- Sử dụng từ 5 đến 15 thùng.

- Dữ liệu số (Tiếp theo)

Trực quan hóa sử dụng Thực tiễn tốt nhất Dữ liệu cần thiết Biểu đồ đường Hiển thị một hoặc nhiều chuỗi dữ liệu. Cho phép việc sử dụng nhiều dữ liệu chuỗi và điểm dữ liệu.

- Thời gian chạy từ trái sang phải.

- Hãy nhất quán vẽ các mốc thời gian.

- Dùng nét liền, không chấm.

- Sử dụng đường cơ sở bằng 0.

- Không vẽ quá bốn dòng. Sử dụng nhiều biểu đồ thay vào đó.

- Đường liên tục yêu cầu một ngày, không hoặc nhiều hơn các danh mục và một hoặc nhiều hơn về số lượng đo lường. Biểu đồ hình tròn Minh họa phần đơn giản các mối quan hệ tổng thể. Không phù hợp để làm những so sánh chính xác

- Có tác động mạnh mẽ nhất với các tập dữ liệu nhỏ.

- Tốt nhất để thể hiện sự khác biệt trong các nhóm dựa trên một biến.

- Đảm bảo dữ liệu cộng lại lên tới 100%.

- Giới hạn tối đa năm phân đoạn.

- Bắt đầu phân đoạn đầu tiên ở vị trí 12 giờ.

- Một hoặc nhiều danh mục.

- Một hoặc hai định lượng biện pháp. Biểu đồ thanh xếp chồng lên nhau So sánh nhiều phần- các mối quan hệ tổng thể.

- Có thể theo chiều dọc hoặc chiều ngang.

- Thực hiện theo các phương pháp hay nhất tương tự như biểu đồ thanh.

- Một hoặc nhiều danh mục.

- Một hoặc nhiều định lượng biện pháp. biểu đồ phân tán (Biểu đồ phân tán) Làm nổi bật mối tương quan và phân phối lớn lượng dữ liệu.

- Tập dữ liệu phải đi theo cặp với một tập dữ liệu độc lập biến (trục x) và biến phụ thuộc (trục y).

- Sử dụng nếu thứ tự không liên quan – nếu không thì sử dụng một dòng đồ thị.

- Không sử dụng nếu chỉ có một vài dữ liệu hoặc nếu không có sự tương quan.

- Không hoặc nhiều danh mục.

- Một hoặc nhiều định lượng biện pháp. Bản đồ cây

Hình dung một phần-to- toàn bộ mối quan hệ giữa nhiều hạng mục.

- Thích hợp khi không thể so sánh chính xác quan trọng.

- Sử dụng màu sắc tươi sáng, tương phản để mỗi hộp dễ dàng được xác định.

- Dán nhãn hộp bằng văn bản hoặc số.

- Một hoặc nhiều danh mục.

- Một hoặc hai định lượng biện pháp. MINH HỌA 2.57 (Tiếp theo) Khi bạn phát triển kỹ năng phân tích dữ liệu của mình, bạn sẽ làm việc với các tập hợp dữ liệu lớn và sẽ cần sử dụng trực quan hóa dữ liệu để phân tích chúng và truyền đạt các phát hiện. Biểu đồ này có thể là tài liệu tham khảo hữu ích khi bạn khám phá dữ liệu và truyền đạt những phát hiện của mình. Chọn hình ảnh trực quan Làm thế nào để bạn biết hình ảnh nào là tốt nhất cho phân tích? Bắt đầu bằng việc xem xét mục tiêu của dự án. Có một số mục tiêu phân tích chung:

- Hiển thị bố cục

- Biểu thị mối quan hệ

- Hiển thị phân phối

- Tìm kiếm xu hướng

- So sánh

Hình minh họa 2.58 chia nhỏ các lựa chọn trực quan nếu mục tiêu là thể hiện bố cục, mối liên hệ quyền sở hữu hoặc phân phối. Hình minh họa 2.59 xác định các hình ảnh trực quan hữu ích để hiển thị xu hướng hoặc thực hiện so sánh.

Hướng dẫn hiển thị trực quan Xu hướng hoặc so sánh Biểu đồ đường Biểu đồ cột Biểu đồ thanh Biểu đồ cột Biểu đồ đường Biểu đồ cột Mục tiêu là gì của việc phân tích? Chỉ ra xu hướng So sánh Mặt hàng Theo thời gian Bạn có thể sử dụng cả hướng dẫn trực quan, cùng với các mô tả và cách thực hành tốt nhất trong Hình minh họa 2.57, nhằm tạo ra hình ảnh trực quan tốt nhất nhằm giải quyết mục đích phân tích. Trực quan hóa Microsoft Excel Nhiều công cụ có thể tạo ra hình ảnh trực quan. Khóa học này tập trung vào bộ ba phần mềm, Tableau, Power BI và Microsoft Excel, là những công cụ phổ biến nhất (nhưng chắc chắn không phải duy nhất) được sử dụng trong kinh doanh ngày hôm nay.

Hướng dẫn trực quan hóa hiển thị Thành phần, mối quan hệ và Phân phối Biểu đồ vùng Biểu đồ hình tròn Biểu đồ thanh xếp chồng Biểu đồ bong bóng Biểu đồ tán xạ Biểu đồ biểu đồ Biểu đồ đường Biểu đồ tán xạ Hiển thị thành phần Hiển thị mối quan hệ Hiển thị sự phân phối Mục tiêu là gì của việc phân tích?

Microsoft Excel có thể tạo trực quan hóa dữ liệu cơ bản. Các công cụ trực quan trong Microsoft Excel nằm trong ribbon Insert (Minh họa 2.60)

Trực quan hóa trong Excel Được đề xuất Biểu đồ Biểu đồ Bản đồ Biểu đồ Pivot Thêm- trong Bố cục trang Công thức dữ liệu Xem lại Xem Chèn phát triển Để sử dụng công cụ Biểu đồ:

- Đánh dấu dữ liệu vào biểu đồ.

- Chọn một biểu đồ cụ thể hoặc nhấp vào Biểu đồ được đề xuất để xem các đề xuất. Biểu đồ cũng có thể được tạo từ PivotTable Excel. Hãy tạo PivotTable trước hoặc tạo PivotTable và biểu đồ cùng lúc bằng cách sử dụng PivotChart. Hình minh họa 2.61 cho thấy hộp thoại khi chọn Tạo PivotChart. Lưu ý rằng nó giống với PivotTable hộp thoại. MINH HỌA 2.61 PivotChart Hộp thoại được rồi Hủy bỏ Chọn kết nối... Tên kết nối: Tạo PivotChart Chọn dữ liệu bạn muốn phân tích Chọn nơi bạn muốn đặt PivotChart Chọn xem bạn có muốn phân tích nhiều bảng không Bảng tính hiện có Sử dụng Mô hình Dữ liệu của sổ làm việc này Bảng tính mới Vị trí: Chọn một bảng hoặc dải ô Sử dụng nguồn dữ liệu ngoài Bảng/Phạm vi: Thêm dữ liệu này vào Mô hình Dữ liệu 'Giao dịch bán hàng'!$A$1:$Z$3646 ? Dữ liệu Ví dụ này sử dụng tệp dữ liệu Super Scooters để tạo PivotTable và Piv- otBiểu đồ tổng doanh thu theo năm và theo model (Minh họa 2.62). Để thực hiện việc này, hãy chọn:

- Trường Model cho Legend (Series).

- Năm dành cho Trục (Danh mục).

- Tổng doanh thu gộp theo giá trị. Hình minh họa 2.63 hiển thị PivotTable và PivotChart thu được, là biểu đồ thanh ở dạng màu thanh đại diện cho các mô hình.

ngoại hối A B C D E F G H tôi J K Trang 1 Tự động Lưu Oﬀ Trường PivotTable Chọn các trường để thêm vào báo cáo: Số thứ tự Năm Số đơn đặt hàng bán hàng người mẫu Ngày bán Khối lượng bán hàng Màu sắc Vị trí tiểu bang Quốc gia Số ngày tồn kho Đơn giá bán Tổng doanh thu Tiếp thị biến đổi Tìm kiếm PivotTable7 Để xây dựng một báo cáo, hãy chọn các trường từ Danh sách trường PivotTable Để xây dựng PivotChart, hãy chọn các trường từ PivotChart ngoại hối A B C D E F G tờ Tự động Lưu Oﬀ Trường PivotTable Chọn các trường để thêm vào báo cáo Số thứ tự Năm Số đơn đặt hàng bán hàng người mẫu Ngày bán Khối lượng bán hàng Màu sắc Kéo các trường giữa các khu vực bên dưới: Bộ lọc Cột người mẫu Tìm kiếm Hàng Trì hoãn cập nhật bố cục Giá trị ∑ cập nhật Tổng doanh thu gộp Năm Tổng doanh thu gộp Nhãn hàng Nhãn cột thuyền trưởng Celeritas cú đá Lazer Tổng cộng Tổng cộng $ 1,893,384 $ 4,578,593 $ 5,850,804 $12,322,781 $ 1,132,873 $ 2,081,584 $ 1,577,881 $4,792,338 $ 585,415 $ 279,848 $ 242,920 $ 1,108,183 862.887 USD $ 3,566,309 $4,493,557 $8,922,753 $4,474,559 $10,506,334 $12,165,162 $ 27,146,055 thuyền trưởng $0 1.000.000 USD 2.000.000 USD 3.000.000 USD 4.000.000 USD 5.000.000 USD 6.000.000 USD 7.000.000 USD Celeritas cú đá Lazer người mẫu Tổng doanh thu gộp Năm

Trong sự nghiệp kế toán của mình, bạn sẽ gặp nhiều loại phần mềm trực quan hóa dữ liệu. các chương trình kho. Tuy nhiên, việc học cách sử dụng bất kỳ chương trình phần mềm nào sẽ giúp chuẩn bị bạn sử dụng và học hỏi công nghệ mới. ( Dữ liệu Cách thực hiện 2.2 là phần hướng dẫn cách tạo biểu đồ thanh sử dụng Tableau.) Áp dụng nó 2.5 Phân tích sản phẩm Chi phí với dữ liệu Trực quan hóa Kế toán quản lý Người quản lý tại Super Scooters đã yêu cầu bạn chuẩn bị một bản phân tích về chi phí sản phẩm. Cụ thể, bộ điều khiển muốn có câu trả lời cho bốn câu hỏi:

- **1. Tổng chi phí cho mỗi mô hình mỗi năm là bao nhiêu?**

- **2. Chi phí biến đổi nào cao nhất?**

- **3. Chi phí nhân công, vật liệu và chi phí chung tăng hay giảm theo thời gian?**

- 4. Tổng chi phí có liên quan đến khối lượng bán hàng không? Đối với mỗi câu hỏi:

- Xác định một hình dung thích hợp và giải thích lý do của bạn.

- Liệt kê các cách thực hành tốt nhất cho việc trực quan hóa.

- Xác định loại dữ liệu cần thiết cho việc trực quan hóa. GIẢI PHÁP 1. Biểu đồ vùng là lựa chọn tốt nhất vì nó thể hiện những thay đổi về khối lượng theo thời gian. Vì điều này câu hỏi, nó sẽ cho thấy những thay đổi trong tổng chi phí theo thời gian.

Thực tiễn tốt nhất: • Không sử dụng dữ liệu có nhiều hơn bốn loại để tránh nhầm lẫn và lộn xộn. Ở đó có bốn mô hình, vì vậy yêu cầu này được đáp ứng. • Bắt đầu trục y ở mức 0 hoặc cao hơn. • Đặt dữ liệu có độ biến thiên cao ở trên cùng và dữ liệu có độ biến thiên thấp ở phía dưới.

Dữ liệu: • Trường ngày (năm sử dụng) • Ít nhất một thước đo định lượng (sử dụng tổng chi phí)

- 2. Biểu đồ thanh là cách trực quan thích hợp nhất vì nó so sánh các bộ phận với tổng thể, cao cấp. danh mục đèn hoặc hiển thị các thay đổi theo thời gian.

Thực tiễn tốt nhất: • So sánh hai đến bảy danh mục bằng các thanh dọc. • Sử dụng thanh ngang nếu có nhiều hơn bảy danh mục hoặc nhãn danh mục dài. • Sử dụng nhãn ngang để dễ đọc hơn. • Thanh cách phù hợp và nhất quán. • Sử dụng màu sắc một cách tiết kiệm hoặc làm điểm nhấn. • Luôn có đường cơ sở bằng 0.

Dữ liệu: • Một hoặc nhiều danh mục (chi phí nhân công, vật liệu, chi phí chung) • Một hoặc nhiều thước đo định lượng (chi phí)

- 3. Biểu đồ đường thích hợp vì nó hiển thị một hoặc nhiều chuỗi dữ liệu và cho phép sử dụng của nhiều chuỗi dữ liệu và điểm dữ liệu.

Thực tiễn tốt nhất: • Thời gian chạy từ trái sang phải. • Hãy nhất quán trong việc vẽ các điểm thời gian. • Sử dụng đường nét liền, không chấm. • Sử dụng đường cơ sở bằng 0. • Không vẽ nhiều hơn bốn dòng. Thay vào đó, hãy sử dụng nhiều biểu đồ. Làm cách nào để

---

# PHẦN VII: TÓM TẮT CHƯƠNG VÀ HƯỚNG DẪN THỰC HÀNH (SUMMARY & HOW-TO GUIDES)

## 1. Tóm tắt các Mục tiêu Học tập (LO 2.1 - LO 2.5 Summary)

- Các thước đo hình dạng bao gồm độ lệch và độ nhọn. • Các thước đo tương quan có thể giúp xác định mối quan hệ giữa các dữ liệu. Mối tương quan của các biến liên tục được đo bằng cách sử dụng hệ số tương quan. Thước đo này là một giá trị số giữa −1 và +1. Giá trị càng gần giá trị tuyệt đối của 1 thì mối tương quan mạnh hơn. Ôn tập và thực hành chương Đánh giá mục tiêu học tập

Dữ liệu: • Các dòng liên tục cần một ngày, không hoặc nhiều danh mục và một hoặc nhiều định lượng biện pháp. • Đối với câu hỏi này, có nhiều năm, ba loại chi phí và chi phí của những chi phí đó.

- 4. Biểu đồ phân tán là lựa chọn tốt nhất vì nó làm nổi bật mối tương quan và phân bổ của lượng dữ liệu.

Thực tiễn tốt nhất: • Tập dữ liệu phải đi theo cặp với một biến độc lập (trục x) và một biến phụ thuộc (trục y). • Chỉ sử dụng nếu thứ tự không liên quan, nếu không hãy sử dụng biểu đồ đường. • Tránh nếu chỉ có một vài dữ liệu hoặc nếu không có mối tương quan.

Dữ liệu: • Không hoặc nhiều danh mục • Một hoặc nhiều thước đo định lượng

Cách đi qua Tên nguồn: Doanh thu Cài đặt trường giá trị ? Tên tùy chỉnh: Tổng doanh thu Tóm tắt trường giá trị bằng sản phẩm Đếm số StdDev StdDevp Var Varp được rồi Hủy bỏ Chọn kiểu tính toán mà bạn muốn sử dụng để tóm tắt dữ liệu từ trường đã chọn Định dạng ô ? được rồi Hủy bỏ Thể loại: Số Các định dạng kế toán sắp xếp các ký hiệu tiền tệ và dấu thập phân trong một cột. Vị trí thập phân: Biểu tượng: $4.089.159,47 $ Tóm tắt các giá trị theo Hiển thị giá trị dưới dạng mẫu chung Số Tiền tệ Kế toán Ngày thời gian Tỷ lệ phần trăm Phân số khoa học văn bản Đặc biệt tùy chỉnh Định dạng số

giải thích dữ liệu. Trực quan hóa dữ liệu là một trong những lĩnh vực phân tích dữ liệu phát triển nhanh nhất trong nghề kế toán: • Trực quan hóa dữ liệu là cách trình bày dữ liệu bằng đồ họa và thông tin. Trực quan hóa dữ liệu có thể giúp nhanh chóng hiểu được dữ liệu lớn bộ dữ liệu. • Trực quan hóa dữ liệu thăm dò kiểm tra dữ liệu để phát hiện ra các chim nhạn biển, xu hướng hoặc sự bất thường. Sử dụng trực quan hóa dữ liệu giải thích các công cụ và kỹ thuật trực quan hóa dữ liệu để truyền đạt thông tin kết quả phân tích dữ liệu. • Việc lựa chọn hình ảnh trực quan phù hợp là sự kết hợp của việc xem xét mục đích của việc phân tích và quyết định liệu mục tiêu có phải là để thể hiện thành phần, mối quan hệ, phân phối, xu hướng hoặc so sánh.

Định dạng và hiển thị giá trị dưới dạng tùy chọn trong PivotTable Các giá trị trong Excel PivotTable có thể được định dạng bằng hộp thoại Cài đặt Trường Giá trị. Những gì bạn cần: Dữ liệu Tệp dữ liệu How To 2.1. BƯỚC 1: Nhấp vào Định dạng số. Hộp thoại Format Cells tương tự có sẵn trong công cụ Home ribbon sẽ xuất hiện (Minh họa 2.64). Làm thế nào để Thuộc tính 2-2 Dữ liệu phân loại 2-42 Hệ số nhọn (CK) 2-30 Hệ số độ lệch (CS) 2-30 Phân tích tương quan 2-34 Hệ số tương quan 2-34 Tổ chức dữ liệu 2-13 Cắt lát 2-22 Trực quan hóa dữ liệu 2-40 Kích thước 2-12 Trực quan hóa dữ liệu giải thích 2-41 Trực quan hóa dữ liệu thăm dò 2-41 Khóa ngoại 2-3 Phân bố tần số 2-30 Chức năng 2-8 Biểu đồ 2-30 Tham gia 2-4 Kurtosis 2-30 Trung bình 2-26 Đo lường xu hướng trung tâm 2-26 Biện pháp phân tán 2-28 Thước đo vị trí 2-26 Số đo hình dạng 2-29 Trung bình 2-26 Chế độ 2-26 Giá trị null 2-4 Bảng tổng hợp 2-13 Khóa chính 2-3 Truy vấn 2-4 Cơ sở dữ liệu quan hệ 2-2 Độ lệch 2-29 Máy thái 2-22 Độ lệch chuẩn 2-28 Ngôn ngữ truy vấn có cấu trúc (SQL) 2-4 Bảng 2-2 Phương sai 2-28 Đánh giá các điều khoản chính Cách đi qua

BƯỚC 2: Cũng có thể sử dụng tùy chọn Hiển thị giá trị dưới dạng trong Cài đặt trường giá trị hộp thoại để thêm tính toán nhanh các giá trị:

- Nhấp vào Hiển thị giá trị dưới dạng sẽ hiển thị danh sách thả xuống các phép tính tích hợp.

- Hình minh họa 2.65 hiển thị các giá trị dưới dạng phần trăm của tổng số. Nhãn hàng Tổng doanh thu 1.827.384,78 USD $ 4.086.546,19 $ 4.745.563,32 10.659.494,29 USD Tổng cộng Nhãn hàng Tổng doanh thu 17,14% 38,34% 44,52% 100,00% Tổng cộng Bảng tổng hợp này hiển thị ba năm doanh thu Bảng tổng hợp này hiển thị cùng một dữ liệu nhưng theo tỷ lệ phần trăm tổng doanh thu MINH HỌA 2.65 Hiển thị giá trị dưới dạng tùy chọn BƯỚC 3: Tổng Doanh thu có thể nhanh chóng được thay đổi thành Phần trăm Tổng Doanh thu bằng cách chọn % của Tổng cộng trong hộp thoại (Minh họa 2.66). CÁCH 2.2 Tạo biểu đồ thanh bằng Tableau Hình dung tương tự từ Hình minh họa 2.63 có thể được tạo bằng Tableau. Những gì bạn cần: Dữ liệu Tệp dữ liệu How To 2.2. Làm thế nào để MINH HỌA 2.66 Hiển thị giá trị dưới dạng tùy chọn Tóm tắt các giá trị theo Tên nguồn: Doanh thu Cài đặt trường giá trị ? Tên tùy chỉnh: Tổng doanh thu Hiển thị các giá trị dưới dạng Không tính toán Hiển thị giá trị dưới dạng Không tính toán % của Tổng cộng % tổng số cột % tổng số hàng % của % tổng số hàng gốc được rồi Hủy bỏ Định dạng số

Cách đi qua

Dữ liệu tệp Tableau - Siêu xe tay ga Cách làm 2.2 Bảng tính Bảng thông tin Phân tích Câu chuyện Định dạng Bản đồ Trợ giúp Cửa sổ Máy chủ Màu sắc Quốc gia, tiểu bang Quốc gia ABC ABC ABC ABC Giao dịch mua bán (Siêu... dữ liệu Bàn tiểu bang Vị trí Mô hình ABC Số thứ tự Số đơn đặt hàng bán hàng Ngày bán Năm Kích thước Danh sách các bảng. Trong tập tin này chỉ có một. Biện pháp Đo tên Vĩ độ (được tạo) Ký quỹ đóng góp Số ngày tồn kho Tổng doanh thu Lao động Vật liệu Chi phí chung Doanh thu Thuế bán hàng Thuế suất bán hàng Khối lượng bán hàng Tổng chi phí cố định được phân bổ Tổng khấu hao Tổng chi phí cố định Tổng chi phí biến đổi Tổng số bảo hành Đơn giá bán Tiếp thị biến đổi Tổng chi phí Kinh độ (được tạo) Giao dịch bán hàng (Đếm) Đo giá trị Thả lĩnh vực ở đây tự động T T Màu sắc Chú giải công cụ chi tiết Kích thước văn bản Cột Tờ 1 Hàng Phân tích Bộ lọc Trang Điểm Tìm kiếm Tất cả các trường phía trên dòng là các kích thước được xem xét. Tất cả các trường bên dưới dòng là biện pháp. Các biện pháp liên tục các trường số. Kích thước là những trường không phải là thước đo. BƯỚC 1: Thêm các trường để trực quan hóa vào khung vẽ:

- Mở file và nhấn vào Sheet 1 dọc cuối màn hình (Minh họa 2.67).

- Thao tác này sẽ mở một bảng tính mới để hiển thị. Bấm vào trường để hình dung và kéo nó vào cột hoặc dòng hàng: • Kéo Ngày bán vào Cột, Mô hình vào Hàng và Tổng doanh thu vào Văn bản. • Bạn cũng có thể kéo nó đến vị trí mong muốn trong khung vẽ ở khu vực có nhãn Trường thả ở đây.

tự động T T SUM(Tổng doanh thu) T Màu sắc Chi tiết Chú giải công cụ Kích thước văn bản Tổng doanh thu theo mẫu thuyền trưởng Celeritas cú đá Lazer $ 1,893,384 $ 1,132,873 $ 585,415 862.887 USD người mẫu Ngày bán $4,570,481 $ 2,081,584 $ 279,848 $ 3,566,309 $ 5,850,804 $ 1,577,881 $ 242,920 $4,493,557 Năm(Ngày bán) người mẫu Cột Hàng Bộ lọc Trang Điểm Bước 2: Tạo biểu đồ thanh. Lưu ý Tableau được mặc định ở định dạng Bảng.

- Bấm vào Hiển thị cho tôi ở góc trên bên phải màn hình.

- Chọn biểu đồ cột cạnh nhau. Lưu ý rằng bất kỳ hình ảnh trực quan nào được đánh dấu đều có thể được chọn (Hình minh họa 2.69). MINH HỌA 2.69 Tableau Hiển thị cho tôi các tùy chọn 123 456 321 654 654 321 456 123 123 456 321 654 654 321 Biện pháp Kích thước Đối với các dòng (rời rạc) hãy thử 1 ngày 0 hoặc hơn 1 hoặc nhiều hơn Cho tôi xem Những hình ảnh trực quan chuyển sang màu xám cho biết bạn làm không có thích hợp dữ liệu cho sự trực quan hóa đó Hình minh họa 2.68 cho thấy kết quả khi kéo Year vào Columns, Model thành Rows, và Tổng doanh thu cho văn bản .

Cách đi qua BƯỚC 3: Đặt tiêu đề cho hình ảnh trực quan:

- Click đúp vào tiêu đề Sheet 1 và chọn Edit Title.

- Thay đổi tiêu đề bằng cách gõ “Tổng doanh thu theo mẫu” (Minh họa 2.71). Hình minh họa 2.70 là kết quả của việc chọn tùy chọn trực quan hóa biểu đồ thanh cột. MINH HỌA 2.70 Tableau Bar Trực quan hóa biểu đồ Tổng bán hàng $6,000K thuyền trưởng Celeritas Cú đá Mẫu/Ngày bán Tổng doanh thu theo mẫu Lazer $5,500K $5,000K $4,500K $4,000K $3,500K $3,000K $2,500K $1,500K 2.000 nghìn USD 1.000 nghìn USD $500K $0K Định dạng SUM(Tổng doanh thu) tự động T T Màu sắc Chú giải công cụ chi tiết Kích thước văn bản Cột Tờ 1 Hàng A Trường Trục Phông chữ: Bóng: Mặc định Bọ ve: quy mô Chỉnh sửa tiêu đề... Đặt lại tiêu đề Ẩn tiêu đề Định dạng tiêu đề... ngăn Bộ lọc Trang Điểm MINH HỌA 2.71 Tableau Bar Biểu đồ: Thêm tiêu đề BƯỚC 4: Định dạng trục:

- Để định dạng trục Tổng doanh thu và đô la theo đơn vị nghìn, hãy nhấp vào mũi tên xuống trong TỔNG (Tổng doanh thu).

- Chọn Format và nhấn vào Axis Tab (Minh họa 2.72).

BƯỚC 5: Thay đổi hiển thị tiền tệ thành hàng nghìn:

- Khi ở trong hộp Định dạng, hãy chọn Số và Tiền tệ (Tùy chỉnh).

- Chọn Đơn vị hiển thị để thay đổi số được hiển thị theo hàng nghìn.

- Lưu ý, chúng ta cũng đã thay đổi chữ số thập phân thành 0 (Minh họa 2.73). Tổng doanh thu E Mẫu/Ngày bán $5,500K $6,000K $5,000K $4,500K $4,000K $3,500K Cột Hàng người mẫu SUM(Tổng doanh thu) NĂM(Ngày bán) Lọc... Hiển thị bộ lọc Định dạng... Hiển thị tiêu đề Đưa vào chú giải công cụ Kích thước Thuộc tính Đo (tổng) rời rạc liên tục Chỉnh sửa trong Kệ Thêm bảng tính... Tính bảng nhanh Xóa MINH HỌA 2.72 Tableau Bar Biểu đồ: Định dạng trục Định dạng SUM(Tổng doanh thu) Cột Hàng Tổng doanh thu Trục A Trường Sách Tableau.. Bóng: Bọ ve: Căn chỉnh: Số: Mặc định quy mô $6,000K $5,500K thanh Màu sắc Kích thước Nhãn $5,000K 2.000 nghìn USD T tự động Số (Tiêu chuẩn) Số (Tùy chỉnh) Tiền tệ (Tiêu chuẩn) Tiền tệ (Tùy chỉnh) khoa học Tỷ lệ phần trăm tùy chỉnh Tiền tệ (Tùy chỉnh) Vị trí thập phân: Đơn vị hiển thị: Tiền tố/Hậu tố: $ Bao gồm dấu phân cách hàng nghìn Giá trị âm: ($1,234) Hàng ngàn (K) $123K ngăn Điểm Phông chữ: Trang Bộ lọc MINH HỌA 2.73 Tableau Bar Biểu đồ: Thay đổi hiển thị tiền tệ

---

# PHẦN VIII: CÂU HỎI VÀ BÀI TẬP THỰC HÀNH (QUESTIONS & EXERCISES)

## 1. Câu hỏi trắc nghiệm (Multiple Choice Questions)

- 1. (LO 1) Một tập hợp các dữ liệu liên quan đến logic có thể được truy xuất, được thao tác và cập nhật để đáp ứng nhu cầu của người dùng được gọi là một. bàn. b. cơ sở dữ liệu quan hệ. c. tập dữ liệu. d. kho dữ liệu.

- 2. (LO 1) Trong bảng cơ sở dữ liệu quan hệ, khóa chính một. không phải lúc nào cũng cần thiết. b. giống như khóa ngoại. c. là một giá trị duy nhất. d. có thể được lặp lại trong bảng nếu cần thiết.

- 3. (LO 1) Các bảng trong cơ sở dữ liệu có thể thuộc loại nào sau đây phần tử? Một. Tài sản, nợ phải trả, chi phí b. Nguồn lực, chi phí, nhân viên c. Doanh thu, sự kiện, đại lý d. Tài nguyên, sự kiện, đại lý

- 4. (LO 1) Các cột trong cơ sở dữ liệu phản ánh một. thuộc tính. b. sự kiện. c. tài nguyên. d. đại lý.

- 5. (LO 1) Yêu cầu dữ liệu từ cơ sở dữ liệu để truy xuất hoặc thao túng nó được gọi là một. phân tích dữ liệu. b. một truy vấn. c. một câu hỏi. d. một sự tham gia.

- 6. (LO 1) Khi thực hiện nối giữa hai bảng, nếu giá trị null được trả về, điều đó cho thấy một. một giá trị bằng không. b. sự tham gia không chính xác. c. một giá trị không tồn tại trong cơ sở dữ liệu. d. một sự tham gia bên trong đã được thực hiện.

- 7. (LO 1) Một phép nối dẫn đến việc truy xuất tất cả các bản ghi từ bên trái bảng và các bản ghi trùng khớp từ bảng bên phải là loại tham gia? Một. Nội tâm b. trái c. Đúng d. Đầy đủ

- 8. (LO 1) Một phép nối trả về tất cả các hàng từ cả hai bảng có giá trị phù hợp là loại tham gia nào? Một. Nội tâm b. trái c. Đúng d. Đầy đủ

- 9. (LO 1) Một phép nối trả về tất cả các bản ghi từ bảng bên phải dưới dạng cũng như tất cả các bản ghi trùng khớp từ bảng bên trái là loại nào tham gia? Một. Nội tâm b. trái c. Đúng d. Đầy đủ

- 10. (LO 1) Một phép nối trả về tất cả các bản ghi khi có sự trùng khớp trong bảng bên trái hoặc bên phải là loại tham gia nào? Một. Nội tâm b. trái c. Đúng d. Đầy đủ

- 11. (LO 2) Hàm Microsoft Excel nào sau đây trả về giá trị trung bình số học của một dãy hoặc mảng số? Một. TRUNG BÌNH b. Ý NGHĨA c. TRUNG BÌNH d. TỔNG

- 12. (LO 2) Hàm Microsoft Excel nào sau đây được tính số lượng ô được chỉ định bởi một bộ tiêu chí nhất định? Một. ĐẾM b. QUẬN c. QUẬN d. QUẬN

- 13. (LO 2) Hàm này thêm các ô được chỉ định bởi một tập hợp các điều kiện nhất định các điều kiện hoặc tiêu chí. Một. TỔNG b. SUMIF c. TÓM TẮT d. TỔNG HỢP SẢN PHẨM

- 14. (LO 3) Hàm này thêm các ô được chỉ định bởi một điều kiện hoặc tiêu chí. Một. TỔNG b. SUMIF c. TÓM TẮT d. TỔNG HỢP SẢN PHẨM

- 15. (LO 3) Công cụ nào trong Microsoft Excel sẽ sắp xếp lại bảng tính dữ liệu thành các bản tóm tắt tùy chỉnh về thông tin chính? Một. Sắp xếp b. Lọc c. bảng tổng hợp d. Nhà phát triển

- 16. (LO 3) PivotTable hiển thị doanh số theo loại sản phẩm, năm bán hàng, và tổng số tiền bán ra. Bạn chỉ muốn nhìn thấy ba trong số 15 loại sản phẩm cụ thể. Cách tốt nhất là chỉ tập trung vào loại sản phẩm cụ thể mà bạn quan tâm là sử dụng một. hàm SORT. b. hàm SUMIG. c. một bộ lọc. d. cắt và dán.

- 17. (LO 3) Chức năng lọc tự động trong PivotTable có thể được truy cập bằng một. bằng cách sử dụng hộp bộ lọc trong các trường PivotTable. b. nhấp vào mũi tên thả xuống trong nhãn hàng. c. nhấp vào mũi tên thả xuống trong hộp bộ lọc. d. kéo một trường vào hộp lọc trường.

- 18. (LO 3) Cắt lát đề cập đến một. loại bỏ số thập phân. b. loại bỏ dữ liệu. c. sắp xếp dữ liệu. d. chia nhỏ dữ liệu thành các phần nhỏ hơn. Dữ liệu Thẻ Dữ liệu xuất hiện khi dữ liệu cần thiết để trả lời một câu hỏi hoặc hoàn thành một câu hỏi. bài tập có sẵn trên nền tảng học tập trực tuyến của Wiley.

- **1. (LO 1) Xác định và mô tả bốn loại kết nối có thể truy vấn một tập dữ liệu.**

- 2. (LO 2) Đối với mỗi tình huống, hãy ghép hàm Excel cơ bản tốt nhất phù hợp với có thể được sử dụng để giải quyết nó. Mỗi chức năng có thể được sử dụng một lần, nhiều hơn hơn một lần, hoặc không hề. Một. TRUNG BÌNH b. TRUNG BÌNH c. ĐẾM d. QUẬN đ. QUẬN f. QUỐC GIA g. TỔNG h. SUMIF Kịch bản chức năng

- **1. Đếm số lượng ô trong một tệp Excel có hàng tồn kho số lượng.**

- **2. Đếm số lượng ô trong một Tệp Excel có hàng tồn kho số lượng 1.150 mặt hàng**

- 3. Tính trung bình số học của số tiền hoa hồng trả cho việc bán hàng nhân sự trong quý IV.

- 19. (LO 4) Tổng của tất cả các quan sát trong một tập dữ liệu chia cho tổng số quan sát được gọi là một. nghĩa là. b. trung vị. c. cách thức. d. phạm vi.

- 20. (LO 4) Giá trị ở giữa khi dữ liệu trong tập dữ liệu được sắp xếp từ nhỏ nhất đến lớn nhất được gọi là một. nghĩa là. b. trung vị. c. cách thức. d. phạm vi.

- 21. (LO 4) Các biện pháp phân tán cho thấy một. xu hướng trung tâm b. hình dạng. c. biến thể. d. vị trí.

- 22. (LO 4) Nếu hệ số sai lệch là -1,5 thì phân bố dữ liệu sẽ có một một. độ lệch cao và đuôi lệch về bên phải. b. độ lệch cao và đuôi lệch về bên trái. c. độ lệch vừa phải và đuôi bên phải. d. độ lệch vừa phải và đuôi lệch về bên trái.

- 23. (LO 4) Tương quan âm có nghĩa là một. khi một biến giảm thì biến kia giảm. b. khi một biến tăng thì biến kia tăng.

c. khi một biến tăng thì biến kia giảm. d. khi một biến giảm thì biến kia không đổi.

- 24. (LO 5) Lợi ích nào sau đây của việc trực quan hóa dữ liệu? Một. Trực quan hóa giúp hiểu nhanh các tập dữ liệu lớn. b. Trực quan hóa dữ liệu có thể được sử dụng để khám phá dữ liệu. c. Trực quan hóa dữ liệu có thể được sử dụng để giải thích phân tích dữ liệu. d. Tất cả những điều này đều là lợi ích của việc trực quan hóa dữ liệu.

- 25. (LO 5) Sử dụng trực quan hóa dữ liệu để xác định các mẫu cơ bản là xem xét một. trực quan hóa dữ liệu giải thích. b. trực quan hóa dữ liệu thăm dò. c. phân tích đồ họa. d. phân tích từ trên xuống.

- 26. (LO 5) Hình ảnh trực quan được sử dụng để thể hiện những thay đổi về âm lượng trong thời gian là một/một một. biểu đồ khu vực. b. biểu đồ thanh. c. đồ thị đường. d. biểu đồ tròn.

- 27. (LO 5) Hình ảnh trực quan được sử dụng để minh họa từng phần đơn giản cho toàn bộ các mối quan hệ là a/an một. biểu đồ khu vực. b. biểu đồ thanh. c. đồ thị đường. d. biểu đồ tròn.

- 28. (LO 5) Hình ảnh trực quan được sử dụng để hiển thị phân bố tần số là một/một một. biểu đồ tròn. b. biểu đồ đường. c. biểu đồ biểu đồ. d. biểu đồ bong bóng. Kịch bản chức năng

- 4. Tính tổng doanh số bán hàng khoảng thời gian được liệt kê trong cột K của bảng tính Excel của bạn.

- 5. Tính tổng doanh số bán hàng thời gian chỉ dành cho khách hàng #4920. Số tiền bán hàng được liệt kê trong cột K trong bảng tính Excel của bạn và mã số khách hàng được liệt kê trong cột A của bảng tính Excel của bạn.

- 6. Đếm số lượng hàng tồn kho các mục được liệt kê trên bảng tính không có số lượng hàng tồn kho.

- **3. (LO 2) Đưa ra ví dụ về thời điểm bạn nên sử dụng COUNTIFS chức năng.**

- **4. (LO 2) Hãy cho ví dụ về trường hợp bạn có thể sử dụng COUNTBLANK chức năng.**

- **5. (LO 3) Mô tả năm thành phần của PivotTable Excel.**

- **6. (LO 3) Mô tả cách lọc một PivotTable trong Excel.**

- 7. (LO 4) Cung cấp một ví dụ về trường hợp trung vị của một phân bố có thể có ý nghĩa hơn để giải thích hơn là ý nghĩa.

- **8. (LO 4) Xác định độ lệch chuẩn và đưa ra ví dụ về cách giải thích nó.**

- 9. (LO 4) Xác định tương quan âm và tương quan dương. ủng hộ- vid một ví dụ của mỗi.

- 10. (LO 5) Mô tả trực quan hóa dữ liệu khám phá và giải thích trực quan hóa dữ liệu. Chúng giống nhau thế nào? Chúng khác nhau như thế nào?

- 11. (LO 5) Đối với mỗi tình huống, hãy xác định xem bạn có thực hiện trực quan hóa dữ liệu thăm dò hoặc trực quan hóa dữ liệu giải thích. Kịch bản Loại trực quan

- 1. Người quản lý của bạn cung cấp cho bạn tất cả dữ liệu bán hàng theo dòng sản phẩm hai năm qua và yêu cầu bạn xác định xu hướng bán hàng giữa các năm.

- 2. Bạn đã phân tích dữ liệu liên quan đến xu hướng bán hàng theo quốc gia trong quá khứ ba năm và sẽ trình bày dữ liệu đó sử dụng bản đồ cây.

- 3. Người quản lý của bạn cung cấp cho bạn tất cả các khoản thanh toán được thực hiện để được phê duyệt nhà cung cấp trong sáu tháng qua và yêu cầu bạn xác định xem có bất kỳ khoản thanh toán nào được thực hiện hay không ngoài số tiền thanh toán dự kiến.

- 4. Người quản lý của bạn cung cấp cho bạn phân tích chi phí bảo trì năm và yêu cầu bạn chuẩn bị một chiếc bánh biểu đồ để minh họa các loại chi phí.

- 12. (LO 5) Là chuyên gia thuế cho một nhà bán lẻ trực tuyến, bạn đã từng được yêu cầu tạo một biểu đồ trực quan mô tả sự gia tăng thuế doanh thu được thu và nộp mỗi tháng trong năm nay so với năm ngoái. Sử dụng các phương pháp hay nhất về biểu đồ đường được nêu trong chương, mô tả cách bạn sẽ thiết lập trực quan hóa. Xác định dữ liệu các điểm trên trục x, trục y và chuỗi dữ liệu.

- **13. (LO 5) Mô tả các phương pháp hay nhất cho biểu đồ thanh và biểu đồ vùng.**

## 2. Bài tập ngắn gọn (Brief Exercises BE 2.1 – BE 2.14)

- 14. (LO 5) Bạn là nhà phân tích tài chính trong bộ phận hoạt động của một công ty sản xuất. Là một phần của số liệu kiểm soát chất lượng, công ty theo dõi chi phí làm lại hàng hóa chưa được sản xuất được đảm bảo đáp ứng các tiêu chuẩn chất lượng. Người quản lý của bạn đã yêu cầu bạn làm trước vẽ biểu đồ đường minh họa xu hướng chi phí làm lại theo lý do hạng mục mã. Bạn lưu ý rằng có năm mã lý do khác nhau cho tại sao có thể phải làm lại. Sử dụng các phương pháp hay nhất được nêu trong phần này chương, hãy mô tả cách bạn thiết lập biểu đồ đường để mô tả việc làm lại xu hướng chi phí theo danh mục. Bài tập ngắn gọn Nhân viên ID nhân viên Họ Tên đầu tiên Ngày sinh Ngày tuyển dụng Mức lương (theo giờ) Chức danh công việc Địa chỉ đường phố Thành phố tiểu bang Mã Zip Số điện thoại Khách hàng ID khách hàng Họ Tên đầu tiên Địa chỉ đường phố Thành phố Mã Zip tiểu bang Số điện thoại Nhận đơn hàng Số đơn hàng ID khách hàng ID nhân viên Ghi chú Ngày thời gian BE 2.1 (LO 1) Kế toán quản lý Bạn là nhà phân tích tài chính cho PizzaNow! Công ty lừa đảo troller muốn bạn thực hiện phân tích bằng ba bảng trong cơ sở dữ liệu quan hệ. Đối với mỗi mục, hãy xác định xem đó là khóa chính, khóa ngoại hay không.

- **1. OrderNumber trong bảng TakeOrder**

- **2. ID nhân viên trong bảng TakeOrder**

- **3. CustomerID trong bảng Khách hàng**

- **4. ID nhân viên trong bảng Nhân viên**

- **5. Ngày trong bảng TakeOrder**

- **6. ZipCode trong bảng Nhân viên**

- **1. Xác định khóa chính và khóa ngoại cho mỗi bảng.**

- 2. Nếu bạn muốn biết tên khách hàng cho một đơn hàng cụ thể, bạn nên truy vấn bảng nào? BE 2.3 (LO 1) Kế toán tài chính Giả sử bạn là nhà phân tích tài chính trong nhóm kiểm soát viên cho công ty phân phối của bạn. Bạn đã được yêu cầu xác định tất cả các mặt hàng tồn kho chưa có doanh số bán hàng trong năm qua: • Nhóm CNTT đã cung cấp tệp dữ liệu tồn kho hiện có và tệp dữ liệu bán hàng 12 tháng. • Bạn đã xác định hàng tồn kho trên bàn sẵn có là bảng bên trái và bảng bán hàng 12 tháng như bảng bên phải. Xác định phép nối thích hợp nhất cho hai bảng này để thực hiện phân tích của bạn. Tại sao cái này tham gia nhiều nhất thích hợp? BE 2.4 (LO 1) Kế toán tài chính Bạn là nhà phân tích tài chính của Dine At Home, người đã từng được yêu cầu phân tích dữ liệu trong ba bảng sau. Khách hàng1 ID khách hàng Tên đầu tiên Họ Điện thoại Trang web Địa chỉ Thành phố tiểu bang Mã Zip Nhà hàng Nhà hàngSố Tên nhà hàng đường phố Thành phố tiểu bang Mã zip Tên chủ sở hữu Tên chủ sở hữu Điện thoại Trang web Đặt hàng Số đơn hàng Nhà hàngSố Ngày đặt hàng Số lượng đặt hàng ID khách hàng Khách hàng1 ID khách hàng Tên đầu tiên Họ Điện thoại Trang web Địa chỉ Thành phố tiểu bang Mã Zip Nhà hàng Nhà hàngSố Tên nhà hàng đường phố Thành phố tiểu bang Mã zip Tên chủ sở hữu Tên chủ sở hữu Điện thoại Trang web Đặt hàng Số đơn hàng Nhà hàngSố Ngày đặt hàng Số lượng đặt hàng ID khách hàng BE 2.2 (LO 1) Hệ thống thông tin kế toán Dine At Home cung cấp dịch vụ giao bữa ăn tận nhà đặt hàng từ nhiều nhà hàng địa phương khác nhau. Bạn là người liên lạc giữa bộ phận công nghệ thông tin của công ty nhóm ogy và nhóm kế toán. Bạn được yêu cầu giải thích mối quan hệ giữa các bảng này với nhóm kế toán. Các bảng được lấy từ cơ sở dữ liệu Dine At Home. Đối với mỗi kịch bản, hãy xác định phép nối mà bạn có nhiều khả năng sử dụng nhất để truy vấn dữ liệu. Mỗi kiểu nối có thể được sử dụng một lần, nhiều lần hoặc không sử dụng lần nào. Một. Tham gia trái b. Tham gia ngay c. Tham gia nội bộ d. Tham gia đầy đủ

- 1. Thực hiện truy vấn để nối bảng Nhà hàng (bảng bên trái) và bảng Đơn hàng (bảng bên phải), nhưng chỉ trả về các hàng từ cả hai bảng có giá trị khớp nhau.

- 2. Thực hiện truy vấn để nối bảng Nhà hàng (bảng bên trái) và bảng Khách hàng1 (bảng bên phải), và trả về tất cả các bản ghi từ bảng Nhà hàng, nhưng chỉ những bản ghi phù hợp từ Khách hàng1 cái bàn.

- 3. Thực hiện truy vấn để nối bảng Order (bảng bên trái) và bảng Customer1 (bảng bên phải) và trả về tất cả các bản ghi từ cả hai bảng. Ghép các bản ghi có thể khớp trong cả hai bảng.

- 4. Thực hiện truy vấn để nối bảng Order (bảng bên trái) và bảng Customer1 (bảng bên phải) và chỉ trả về tất cả các bản ghi từ bảng Order và các bản ghi trùng khớp từ bảng Customer1. BE 2.5 (LO 2) Dữ liệu Kế toán quản lý Người kiểm soát tại ThisBigCity đã yêu cầu bạn thực hiện- phân tích về chi phí hoàn trả cho nhân viên của thành phố trong mười lăm năm qua. Nhóm CNTT đã cung cấp bản tải xuống tất cả dữ liệu hoàn trả cho nhân viên kể từ năm 2005.

- 1. Sử dụng hàm TRUNG BÌNH. Số tiền hoàn trả trung bình được trả từ tháng 7 năm 2005 đến Tháng 11 năm 2020?

- 2. Sử dụng hàm AVERAGEIF. Số tiền hoàn trả trung bình được trả trong năm 2019 là bao nhiêu?

- 3. Sử dụng hàm AVERAGEIFS. Số tiền hoàn trả trung bình được trả trong vụ cháy là bao nhiêu bộ phận trong năm 2019? BE 2.6 (LO 2) Dữ liệu Hệ thống thông tin kế toán Với tư cách là kiểm toán viên nội bộ tại ThisBigCity, bạn kiểm tra các biện pháp kiểm soát nội bộ đối với quy trình bồi hoàn cho nhân viên của thành phố. Nhóm CNTT đã cung cấp tải xuống tất cả dữ liệu về khoản hoàn trả của nhân viên kể từ năm 2005. Người quản lý của bạn đã đề xuất thực hiện thống kê mô tả trên tệp này để xác định xem bạn có tập hợp dữ liệu hoàn chỉnh hay không và để bắt đầu quá trình xác định cỡ mẫu để thử nghiệm kiểm soát nội bộ.

- 1. Sử dụng hàm COUNT. Có bao nhiêu khoản hoàn trả đã được trả từ tháng 7 năm 2005 đến tháng 11 năm 2020?

- **2. Sử dụng hàm COUNTIF. Có bao nhiêu khoản hoàn trả được trả trong năm 2019?**

- 3. Sử dụng hàm COUNTIFS. Có bao nhiêu khoản bồi hoàn đã được trả trong năm 2019 cho lính cứu hỏa? BE 2.7 (LO 3) Dữ liệu Kiểm tra Sử dụng PivotTable và dữ liệu có sẵn để trả lời các câu hỏi sau:

- **1. Khách hàng nào có số dư nợ phải thu cao nhất?**

- 2. Khách hàng nào có số dư nợ phải thu quá hạn trên 150 ngày cao nhất? BE 2.8 (LO 3) Dữ liệu Kế toán tài chính Sử dụngPivotTables và dữ liệu có sẵn để trả lời câu hỏi những câu hỏi sau:

- **1. Tổng số khoản phải thu là bao nhiêu?**

- 2. Tổng số theo khu vực là bao nhiêu? BE 2.9 (LO 3) Dữ liệu Kế toán tài chính Kế toán quản lý Sử dụng PivotTable và Dữ liệu Super Scooters để trả lời các câu hỏi sau:

- **1. Tổng doanh thu của từng mẫu xe tay ga theo năm là bao nhiêu?**

- **2. Xe ga màu nào có doanh số cao nhất năm 2023?**

- 3. Tổng chi phí tiếp thị biến đổi cho năm 2023 theo mô hình là bao nhiêu? BE 2.10 (LO 4) Dữ liệu Kế toán quản lý Là nhà phân tích tài chính làm việc cho Animal Con- Trung tâm kiểm soát, bạn muốn hiểu mức lương làm thêm giờ trong năm 2025. Tìm số liệu thống kê sau cho lương làm thêm giờ:

- **1. Ý nghĩa**

- **2. Trung vị**

- 3. Chế độ BE 2.11 (LO 4) Dữ liệu Kế toán tài chính Bạn đang chuẩn bị cuộc thảo luận của ban quản lý và phân tích (MD&A) liên quan đến sở cứu hỏa thành phố Chicago. Một trong những khoản chi quan trọng nhất đối với sở cứu hỏa là làm thêm giờ. Vì vậy, bạn muốn hiểu rõ dữ liệu làm thêm giờ trước khi viết MD & A.

- **1. Tính hệ số sai lệch khi trả lương làm thêm giờ.**

- **2. Tính hệ số nhọn khi trả lương làm thêm giờ.**

- 3. Chuẩn bị biểu đồ với các nhóm sau: $500, $1.000, $2.000, $3.000, $4.000, $5.000, $6.000. BE 2.12 (LO 5) Dữ liệu Kế toán tài chính Công ty của bạn, Loans Are US, cung cấp các khoản vay cho các doanh nghiệp nhỏ đến các doanh nghiệp có quy mô vừa. Công ty có văn phòng cho vay ở bốn khu vực. Bạn được yêu cầu chuẩn bị một trực quan minh họa tổng số tiền cho vay theo khu vực và theo độ tuổi khoản phải thu. Chuẩn bị một biểu đồ cột xếp chồng thực hiện điều này. BE 2.13 (LO 5) Dữ liệu Loans Are US theo dõi xếp hạng tín dụng cho tất cả tài khoản khách hàng. Bạn phải chuẩn bị một hình ảnh trực quan minh họa tổng số khoản vay theo xếp hạng tín dụng. Chuẩn bị một biểu đồ thanh trực quan xác định số lượng tài khoản ở từng mức xếp hạng tín dụng: AAA, BBB và CCC. BE 2.14 (LO 5) Dữ liệu Người giám sát của bạn tại Loans Are US đã yêu cầu bạn chuẩn bị một hình ảnh trực quan minh họa tổng số tiền của các khoản vay quá hạn trên 150 ngày theo xếp hạng tín dụng. Chuẩn bị một thanh biểu đồ trực quan hóa số lượng tài khoản ở mỗi trong số ba xếp hạng tín dụng: AAA, BBB và CCC. Bài tập ngắn gọn

## 3. Bài tập thực hành (Exercises EX 2.1 – EX 2.10)

### EX 2.1 (LO 1) Kiểm tra Xác định dữ liệu và các kết nối cần thiết để xác minh dữ ...

EX 2.1 (LO 1) Kiểm tra Xác định dữ liệu và các kết nối cần thiết để xác minh dữ liệu Bạn là kiểm toán viên nội bộ tor cho Way Cool Stuff. Bạn phải xác minh rằng không có nhân viên nào cũng là khách hàng. Các bảng sau đây nằm trong cơ sở dữ liệu. Địa điểm Vị tríSố Vị tríMô tả Đơn đặt hàng bán hàng Bán hàngSố thứ tự Số đơn hàng người mẫu Ngày bán Doanh số bán hàng Màu sắc Vị trí Vùng tiểu bang Quốc gia Đơn VịBánGiá Số khách hàng Mã Số Nhân Viên nhân viên Mã Số Nhân Viên Tên đầu tiên Họ Địa chỉ Thành phố tiểu bang Mã Zip Khu vựcSố Khách hàng Số khách hàng Tên khách hàng Địa chỉ khách hàng Khách HàngThành Phố Khách hàngTrạng thái Tên liên hệ Khách hàngZipCode Tên liên hệ Số điện thoại Khu vực Khu vựcSố Khu vựcMô tả Hàng tồn kho Số hạng mục MụcMô tả Màu sắc Số lượng trên tay Chi phí đặt hàng bán hàng Số đơn hàng Tiếp thị biến đổi Lao động Tổng sốBảo hành Tổng số khấu hao Thuế bán hàng Vật liệu Chi phí chung 1. Bạn cần có (những) bảng nào để hoàn thành bài kiểm tra này? 2. Bạn sẽ sử dụng trường nào để nối các bảng nếu cần? 3. Bạn cần những trường nào trong (các) bảng để hoàn thành bài kiểm tra này?

### EX 2.2 (LO 1) Kế toán tài chính Xác định dữ liệu và kết hợp cần thiết để tóm tắt...

EX 2.2 (LO 1) Kế toán tài chính Xác định dữ liệu và kết hợp cần thiết để tóm tắt dữ liệu mà bạn là kế toán tài chính tại Way Cool Stuff tính toán thu nhập ròng. Sau đây là các bảng cơ sở dữ liệu có sẵn cho Way Cool Stuff. Địa điểm Vị tríSố Vị tríMô tả Đơn đặt hàng bán hàng Bán hàngSố thứ tự Số đơn hàng người mẫu Ngày bán Doanh số bán hàng Màu sắc Vị trí Vùng tiểu bang Quốc gia Đơn VịBánGiá Số khách hàng Mã Số Nhân Viên nhân viên Mã Số Nhân Viên Tên đầu tiên Họ Địa chỉ Thành phố tiểu bang Mã Zip Khu vựcSố Khách hàng Số khách hàng Tên khách hàng Địa chỉ khách hàng Khách HàngThành Phố Khách hàngTrạng thái Tên liên hệ Khách hàngZipCode Tên liên hệ Số điện thoại Khu vực Khu vựcSố Khu vựcMô tả Hàng tồn kho Số hạng mục MụcMô tả Màu sắc Số lượng trên tay Chi phí đặt hàng bán hàng Số đơn hàng Tiếp thị biến đổi Lao động Tổng sốBảo hành Tổng số khấu hao Thuế bán hàng Vật liệu Chi phí chung 1. Bạn cần (những) bảng nào để có thể thu thập dữ liệu cần thiết để tính thu nhập ròng? 2. Bạn sẽ sử dụng trường nào để nối các bảng? 3. Bạn cần những lĩnh vực nào để tính thu nhập ròng?

### EX 2.3 (LO 1) Kế toán quản lý Đăng ký tham gia để trả lời câu hỏi Bạn đang phân ...

EX 2.3 (LO 1) Kế toán quản lý Đăng ký tham gia để trả lời câu hỏi Bạn đang phân tích doanh số bán hàng tại Way Cool Stuff theo khu vực trong các năm 2024 và 2025. Có sẵn các bảng cơ sở dữ liệu sau. Địa điểm Vị tríSố Vị tríMô tả Đơn đặt hàng bán hàng Bán hàngSố thứ tự Số đơn hàng người mẫu Ngày bán Doanh số bán hàng Màu sắc Vị trí Khu vựcSố tiểu bang Quốc gia Đơn VịBánGiá Số khách hàng Mã Số Nhân Viên nhân viên Mã Số Nhân Viên Tên đầu tiên Họ Địa chỉ Thành phố tiểu bang Mã Zip Khu vựcSố Khách hàng Số khách hàng Tên khách hàng Địa chỉ khách hàng Khách HàngThành Phố Khách hàngTrạng thái Tên liên hệ Khách hàngZipCode Tên liên hệ Số điện thoại Khu vực Khu vựcSố Tên vùng Hàng tồn kho Số hạng mục MụcMô tả Màu sắc Số lượng trên tay Chi phí đặt hàng bán hàng Số đơn hàng Tiếp thị biến đổi Lao động Tổng sốBảo hành Tổng số khấu hao Thuế bán hàng Vật liệu Chi phí chung 1. Bạn cần (những) bảng nào để thu thập dữ liệu cần thiết để phân tích tổng doanh thu theo khu vực cho năm 2024 và 2025? 2. Bạn sẽ sử dụng trường nào để nối các bảng? 3. Bạn sẽ cần những lĩnh vực nào để thực hiện phân tích của mình?

### EX 2.4 (LO 1) Kế toán thuế Xác định dữ liệu và các kết nối cần thiết để tuân thủ...

EX 2.4 (LO 1) Kế toán thuế Xác định dữ liệu và các kết nối cần thiết để tuân thủ thuế Bạn được điền Tờ khai thuế bán hàng tiểu bang của ing Way Cool Stuff vào cuối tháng ngày 31 tháng 12 năm 2025 cho tất cả các địa điểm ở thuế bán hàng nào đã được thu. Sử dụng các bảng cơ sở dữ liệu có sẵn để trả lời các câu hỏi. 1. Bạn cần (những) bảng nào để có thể thu thập dữ liệu cần thiết để tính toán nộp thuế bán hàng cho Tháng 12 năm 2025? 2. Bạn sẽ sử dụng trường nào để nối các bảng? 3. Bạn cần thu thập thông tin cần thiết để nộp thuế bán hàng năm 2025 ở những trường nào?

### EX 2.5 (LO 3) Dữ liệu Kế toán quản lý Áp dụng Bộ cắt Excel PivotTable Người giám...

EX 2.5 (LO 3) Dữ liệu Kế toán quản lý Áp dụng Bộ cắt Excel PivotTable Người giám sát của bạn tại Best Bakes Bakery muốn bạn thực hiện phân tích chi phí theo sản phẩm. Tạo một PivotTa- ble hiển thị tất cả các sản phẩm và tạo bộ cắt để cung cấp thông tin sau: 1. Tổng chi phí tồn kho năm 2023. 2. Tổng chi phí tồn kho bánh quế giai đoạn 2022 - 2025. 3. Tổng chi phí tồn kho bánh quế năm 2023. 4. Tổng chi phí tồn kho của thành phố Thornton từ năm 2022 đến năm 2025. 5. Tổng chi phí tồn kho cho snickerdoodles vào năm 2024 tại thành phố Brookfield.

### EX 2.6 (LO 4) Dữ liệu Kế toán quản lý Thống kê mô tả Bạn là nhà phân tích tài ch...

EX 2.6 (LO 4) Dữ liệu Kế toán quản lý Thống kê mô tả Bạn là nhà phân tích tài chính tại Trung tâm Kiểm soát Động vật Hoa Kỳ được giao nhiệm vụ tìm hiểu mức lương làm thêm giờ trong năm. của bạn Nhóm CNTT đã cung cấp một tệp bao gồm tiền lương làm thêm giờ cho mỗi nhân viên mỗi tháng. Bảng tính cũng bao gồm nhiệt độ trung bình hàng tháng. Thực hiện phân tích mối tương quan giữa lượng vượt quá thời gian phát sinh và nhiệt độ cho mỗi tháng. 1. Hệ số tương quan của các biến số lượng và nhiệt độ là gì? 2. Mối tương quan giữa lượng và nhiệt độ mạnh, trung bình hay yếu? Giải thích câu trả lời của bạn. Địa điểm Vị tríSố Vị tríMô tả Đơn đặt hàng bán hàng Bán hàngSố thứ tự Số đơn hàng người mẫu Ngày bán Doanh số bán hàng Màu sắc Vị trí Vùng tiểu bang Quốc gia Đơn VịBánGiá Số khách hàng Mã Số Nhân Viên nhân viên Mã Số Nhân Viên Tên đầu tiên Họ Địa chỉ Thành phố tiểu bang Mã Zip Khu vựcSố Khách hàng Số khách hàng Tên khách hàng Địa chỉ khách hàng Khách HàngThành Phố Khách hàngTrạng thái Tên liên hệ Khách hàngZipCode Tên liên hệ Số điện thoại Khu vực Khu vựcSố Khu vựcMô tả Hàng tồn kho Số hạng mục MụcMô tả Màu sắc Số lượng trên tay Chi phí đặt hàng bán hàng Số đơn hàng Tiếp thị biến đổi Lao động Tổng sốBảo hành Tổng số khấu hao Thuế bán hàng Vật liệu Chi phí chung

### EX 2.7 (LO 4) Dữ liệu Kế toán quản trị Thống kê mô tả Sự phát triển con người ch...

EX 2.7 (LO 4) Dữ liệu Kế toán quản trị Thống kê mô tả Sự phát triển con người chủ yếu viên chức tại Trung tâm Kiểm soát Động vật đã yêu cầu bạn cung cấp báo cáo tóm tắt về tiền lương làm thêm giờ trong năm. Nhóm CNTT trích xuất dữ liệu từ cơ sở dữ liệu của công ty và cung cấp tệp Excel. Cung cấp một bản tóm tắt báo cáo bằng cách thực hiện như sau: 1. Tạo số liệu thống kê mô tả cho trường dữ liệu Số tiền. Báo cáo kết quả thống kê mô tả: • Trung bình • Lỗi tiêu chuẩn • Trung bình • Chế độ • Độ lệch chuẩn • Phương sai mẫu • Kurtosis • Độ lệch • Phạm vi • Tối thiểu • Tối đa • Tổng • Đếm 2. Tạo biểu đồ phân tán về lương làm thêm giờ. Trục x phải là tháng trong năm và trục y là số tiền làm thêm giờ được trả bằng đô la. 3. Có điểm bất thường nào trên biểu đồ phân tán cần điều tra thêm không? Tại sao hoặc tại sao không?

### EX 2.8 (LO 2, 5) Dữ liệu Kế toán thuế Các hàm Excel cơ bản và Trực quan hóa biểu...

EX 2.8 (LO 2, 5) Dữ liệu Kế toán thuế Các hàm Excel cơ bản và Trực quan hóa biểu đồ thanh Bạn là một chuyên gia về thuế được tổng kiểm soát viên bang Wyoming yêu cầu cung cấp bản tóm tắt báo cáo. các tờ khai thuế đang được nộp trong tiểu bang. Nhóm công nghệ thông tin đã cung cấp file Excel có chứa dữ liệu liên quan đến mã zip của người nộp đơn, số tờ khai và dữ liệu khai thuế quan trọng khác. 1. Tình trạng nộp đơn nào có nhiều tờ khai được nộp nhiều nhất? (Độc thân, Chủ hộ, hoặc Kết hôn nộp hồ sơ chung)? Sử dụng hàm Excel (không phải PivotTable). 2. Tạo trực quan hóa biểu đồ cột hiển thị số tờ khai thuế theo trạng thái nộp hồ sơ. Trục x phải bao gồm tình trạng nộp đơn (độc thân, MFJ, Chủ hộ) và trục y phải là số lượng lợi nhuận.

### EX 2.9 (LO 2, 4, 5) Dữ liệu Kế toán quản lý PivotTable, Thống kê mô tả và Trực q...

EX 2.9 (LO 2, 4, 5) Dữ liệu Kế toán quản lý PivotTable, Thống kê mô tả và Trực quan hóa Bạn là một kế toán viên quản lý đang chuẩn bị phân tích doanh số bán hàng theo phân khúc. Hoa Kỳ ngoài trời Adventures có ba phân khúc: người tiêu dùng, bán lẻ và công ty du lịch. Phân khúc người tiêu dùng bao gồm doanh số bán hàng được thực hiện cho khách hàng cá nhân thông qua trang web Cuộc phiêu lưu ngoài trời của Hoa Kỳ. Phân khúc bán lẻ là những doanh số bán hàng được thực hiện cho các cửa hàng bán lẻ. Mảng công ty du lịch là doanh số bán hàng được thực hiện cho các công ty du lịch tổ chức và tổ chức các chuyến cắm trại. 1. Tạo PivotTable Excel tổng hợp doanh số bán hàng theo phân khúc từ năm 2022 đến năm 2025. Hiển thị từng phân khúc và tổng doanh thu theo năm. 2. Tạo biểu đồ thanh về doanh số bán hàng theo phân khúc từ năm 2022 đến năm 2025. Phân khúc nào đang tăng trưởng và phân khúc nào đang giảm? 3. Tạo PivotTable để phân tích doanh thu trung bình theo phân khúc từ năm 2022 đến năm 2025. Hiển thị từng phân khúc và doanh số bình quân theo năm. 4. Lập biểu đồ đường về doanh thu trung bình theo phân khúc từ năm 2022 đến năm 2025. Doanh thu trung bình đang tăng hay giảm dần từ năm 2024 đến năm 2025? 5. Tìm hiểu sâu hơn: Kiểm tra sự thay đổi về doanh số bán hàng theo phân khúc bằng cách sử dụng PivotTable và biểu đồ đường để phân biệt chơi độ lệch chuẩn. Phân khúc nào có sự biến động lớn nhất về doanh số bán hàng? Làm thế nào bạn xác định được câu trả lời của bạn?

### EX 2.10 (LO 2, 5) Dữ liệu Kiểm tra Bảng tổng hợp và biểu đồ đường Bạn đang làm v...

EX 2.10 (LO 2, 5) Dữ liệu Kiểm tra Bảng tổng hợp và biểu đồ đường Bạn đang làm việc ở Hoa Kỳ- Kiểm toán báo cáo tài chính của Công ty Adventure Door cho năm kết thúc vào ngày 31 tháng 12 năm 2023. Cấp cao của bạn đã yêu cầu bạn hiểu dữ liệu bán hàng và xác định những khách hàng quan trọng để thực hiện chi tiết thử nghiệm. Khách hàng đã cung cấp dữ liệu bán hàng. Theo sổ cái tổng hợp, tổng doanh thu trong năm vào cuối năm 2025 và 2024 lần lượt là 273.323 USD và 269.196 USD. 1. Tạo PivotTable Excel mô tả tổng doanh số theo năm bằng cách sử dụng biến ShipDate. Xác minh tổng doanh thu được báo cáo trong năm phù hợp với số dư sổ cái chung của khách hàng như đã trình bày. 2. Tạo PivotTable trình bày doanh số năm 2024 và 2025 theo danh mục sản phẩm. 3. Sử dụng các phương pháp hay nhất được nêu trong Hình minh họa 2.57, tạo biểu đồ đường thể hiện doanh số bán hàng cho năm 2024 và 2025 theo hạng mục. Trục x phải bao gồm các năm 2024 và 2025 và trục y phải có số tiền bán hàng bằng đô la. Nên có ba dòng, một dòng cho mỗi danh mục bán hàng, dụng cụ cắm trại, mái chèo và lều. 4. Đào sâu hơn: Sửa đổi biểu đồ đường để trục x có thông tin doanh số hàng quý của năm 2024 so với năm 2025 cho từng loại hình bán hàng.

Vấn đề

## 4. Bài tập vấn đề (Problems PR 2.1 – PR 2.4)

### PR 2.1 (LO 3) Dữ liệu Kiểm toán Áp dụng lọc trong PivotTable Công ty của bạn đã ...

PR 2.1 (LO 3) Dữ liệu Kiểm toán Áp dụng lọc trong PivotTable Công ty của bạn đã được thuê để thực hiện- thực hiện kiểm toán cho Best Bakes Bakery. Bạn phải thực hiện phân tích lợi nhuận theo khách hàng để xác định xem liệu có những thay đổi bất thường. 1. Tạo một PivotTable Excel hiển thị tất cả khách hàng và lợi nhuận cho năm 2024 trong một cột và năm 2025 trong một cột khác. 2. Sử dụng Cài đặt trường giá trị để hiển thị phần trăm chênh lệch so với năm 2024. 3. Có bao nhiêu khách hàng có phần trăm thay đổi về lợi nhuận lớn hơn +/− 30% so với trước đó? năm?

### PR 2.2 (LO 2, 4) Dữ liệu Kiểm toán Hàm Excel và Thống kê mô tả Bạn là kiểm toán ...

PR 2.2 (LO 2, 4) Dữ liệu Kiểm toán Hàm Excel và Thống kê mô tả Bạn là kiểm toán viên làm việc trong cuộc kiểm toán báo cáo tài chính của ThisBigCity được yêu cầu thực hiện các thủ tục phân tích để hiểu rõ chịu các chi phí hoàn trả của thành phố cho năm kết thúc vào ngày 31 tháng 12 năm 2025. Khách hàng đã cung cấp một tải xuống tất cả dữ liệu về khoản hoàn trả của nhân viên kể từ năm 2010. Để trả lời các câu hỏi sau, hãy sử dụng Excel hàm chứ không phải PivotTable. 1. Tổng số tiền hoàn trả được trả vào năm 2025 là bao nhiêu? 2. Tính tổng số tiền hoàn trả được trả vào năm 2025 cho các bộ phận sau. Sở hoàn trả thanh toán vào năm 2025 Sở Xây dựng Sở Y tế Cục quản lý nước 3. Mức trung bình, trung vị và phương thức của số tiền hoàn trả vào năm 2025 là gì? 4. Độ lệch chuẩn của số tiền hoàn trả vào năm 2025 là bao nhiêu? 5. Tạo biểu đồ phân tán mô tả số tiền hoàn trả vào năm 2025. Trên trục x, hiển thị ngày, và trên trục y, hiển thị số tiền. Phạm vi trục y phải nằm trong khoảng từ $−500 đến $3.500. 6. Sử dụng số liệu thống kê mô tả sau đây và biểu đồ phân tán để xác định bất kỳ điểm bất thường nào trong thành phố hoàn trả trong năm 2025. • Trung bình • Trung bình • Chế độ • Độ lệch chuẩn 7. Tìm hiểu sâu hơn: Mở rộng các phân tích này để bao gồm phần thảo luận về số tiền hoàn trả theo từng đơn vị khởi hành. chức danh hoặc theo chức danh công việc.

### PR 2.3 (LO 2, 5) Dữ liệu Kiểm toán Các hàm Excel cơ bản và Biểu đồ hình tròn Bạn...

PR 2.3 (LO 2, 5) Dữ liệu Kiểm toán Các hàm Excel cơ bản và Biểu đồ hình tròn Bạn là kiểm toán viên được chỉ định tới cuộc kiểm toán báo cáo tài chính của Công ty Phiêu lưu Ngoài trời cho năm kết thúc vào ngày 31 tháng 12 năm 2025. cấp cao muốn hiểu dữ liệu bán hàng và xác định những khách hàng quan trọng để thực hiện chi tiết thử nghiệm. Tổng doanh thu cho năm kết thúc vào ngày 31 tháng 12 năm 2025, theo sổ cái chung của công ty, là $273,323. (Lưu ý: doanh số bán hàng được ghi nhận khi sản phẩm được giao cho khách hàng.) Sử dụng client-pro- vided Excel, hãy thực hiện như sau: 1. Xác minh bộ dữ liệu đã đầy đủ bằng cách tổng hợp cột doanh số và thống nhất với số liệu doanh số đã ghi trong sổ cái chung của khách hàng. Viết một câu cho biết bạn đã đồng ý số tiền bán hàng cho số tiền trong sổ cái chung của khách hàng. 2. Sử dụng các phương pháp hay nhất được nêu trong Hình minh họa 2.57, tạo biểu đồ hình tròn mô tả doanh số bán hàng theo khu vực cho năm 2025 và xác định khu vực có doanh thu lớn nhất. Biểu đồ hình tròn có phải là hình ảnh trực quan tốt nhất cho câu hỏi này không? Tại sao hoặc tại sao không? 3. Đào sâu hơn: Phân tích tập dữ liệu để hiểu những khách hàng lớn nhất của công ty. Trình bày của bạn phân tích dưới dạng trực quan. Vấn đề

Dữ liệu PR 2.4 (LO 2, 5) Kế toán tài chính quản lý Kế toán PivotTable và thanh Biểu đồ Bạn là nhân viên kế toán của U.S. Outdoor Adventures đang chuẩn bị phân tích doanh số bán hàng hàng tháng Báo cáo phân tích bán hàng nội bộ.

- 1. Tạo một PivotTable Excel để xác định xem có mô hình bán hàng hàng tháng cho tổng doanh số bán hàng hay từ năm 2024 đến

- 2025. Định dạng PivotTable để số tiền bán hàng được tính bằng đơn vị tiền tệ không có chữ số thập phân.

- 2. Tạo biểu đồ thanh về doanh số hàng tháng từ năm 2024 đến năm 2025. Biểu đồ này có giúp xác định xem có doanh thu hàng tháng không? mô hình bán hàng? Tại sao hoặc tại sao không?

- 3. Tìm hiểu sâu hơn: Tạo PivotTable và biểu đồ dạng đường để minh họa mô hình bán hàng hàng tháng theo sản phẩm danh mục vào năm 2024 và 2025. Biểu đồ đường tiết lộ điều gì về mô hình bán hàng của danh mục sản phẩm? Trường hợp ứng dụng chuyên nghiệp: Pizza My Heart Food Truck, Inc. Năm 2020, Sal Simonelli thành lập Pizza My Heart Food Truck, Inc. với công thức gia đình cũ và một món ăn xe tải ở Fort Lauderdale, Florida. Pizza My Heart phục vụ 11 loại pizza cũng như bánh mì que và cánh gà. Họ hoạt động tại các nhà máy bia địa phương ở khu vực Fort Lauderdale và Orlando. Vào năm 2021 Sal mua chiếc xe tải bán đồ ăn thứ hai mà con trai ông, Franco, điều hành ở Orlando, FL. Sal và Franco tin rằng công việc kinh doanh của họ đang tiến triển tốt và đang xem xét mở rộng sang các thành phố khác ở Florida. Đây là báo cáo thu nhập trong hai năm qua. BÁO CÁO KINH DOANH CỦA PIZZA MY HEART 2024 VÀ 2025 Doanh thu Xe tải 1 $151,200 $333,396 Xe tải 2 100.800 USD $222,264 Tổng doanh thu 252.000 USD $555,660 Chi phí và chi phí Giá vốn hàng bán $138,600 $305,613 Tiếp thị 2.000 USD 2.000 USD Tiền lương $133,890 $155,600 Các chi phí khác 3.500 USD 4.000 USD Tổng chi phí và chi phí $277,990 $467,213 EBITDA ($25,990) $88,447 Khấu hao - Xe tải $43,750 $43,750 EBIT ($69,740) $44,697 Lãi suất - Vay mua xe tải $25,856 $ 20,506 Thu nhập trước thuế ($95,596) $ 24,191 Chi phí thuế thu nhập $0 $0 Thu nhập ròng ($95,596) $ 24,191 Lỗ ròng hoạt động chuyển tiếp ($95,596) ($71,405)

- Doanh nghiệp hoạt động thua lỗ vào năm 2024. Điều này phần lớn là do chi phí khởi nghiệp của năm thứ hai xe tải và vì Sal và Franco vẫn đang tìm kiếm những địa điểm tốt nhất ở Fort Lauderdale và Orlando cho xe tải của họ.

- Công ty bắt đầu có lãi vào năm 2025. Doanh số bán xe tải Fort Lauderdale và tăng hơn gấp đôi cho chiếc xe tải Orlando.

- Với doanh số bán hàng tăng nhanh, Sal và Franco cần một cách tốt hơn để nắm bắt tài chính và dữ liệu phi tài chính.

Trường hợp ứng dụng chuyên nghiệp: Pizza My Heart Food Truck, Inc. xe tải Số xe tải Vị tríSố Vị tríThành phố Vị tríTiểu bang Vị tríMã Zip Khách hàng ID khách hàng Thẻ Người Mua Thường Xuyên Tên khách hàng Họ của khách hàng Nhân viên ID nhân viên Tên đầu tiên Họ Xã HộiAn NinhSố Email Địa chỉ Giới tính Thành phố tiểu bang Số điện thoại Nhà cung cấp ID nhà cung cấp Tên công ty Số điện thoại Email Tên liên hệ Địa chỉ Tên liên hệ Thành phố tiểu bang Mã vùng Thực đơn Số sản phẩm Mô tả Danh sáchGiá Chi phí tiêu chuẩn Nguyên liệu thô ID thành phần Thành phầnMô tả Tiền mặt Số tài khoản ngân hàng Mô tả tài khoản Tên ngân hàng Địa chỉ ngân hàng Ngân HàngThành Phố Ngân hàngNhà nước Ngân hàngZipcode Mua hàng Số biên nhận ID nhà cung cấp ID thành phần Chi phí Số lượng đã mua Ngày mua ID nhân viên Tiền gửi Số tiền gửi Số tài khoản ngân hàng Ngày gửi tiền Số tiền ID nhân viên bán hàng ID đơn hàng Số sản phẩm số lượng Số xe tải Ngày bán hàng thời gian ID nhân viên ID khách hàng Nhận thanh toán Số biên nhận ID đơn hàng Tiền mặtSố tiền ID khách hàng Ngày nhận Thẻ tín dụngSố tiền Họ thuê công ty kế toán DGJ, LLC để tạo cơ sở dữ liệu cho họ. Các trường trong mỗi bảng là thể hiện trong sơ đồ. Khóa chính được xác định bằng ký hiệu khóa trước tên trường. Cơ sở dữ liệu về Pizza Trái tim tôi

## 5. Bài tập Kế toán & Phân tích (Accounting & Analytics PAC 2.1 – PAC 2.5)

### PAC 2.1 Hệ thống thông tin kế toán: Hiểu cấu trúc cơ sở dữ liệu quan hệ Hệ thống...

PAC 2.1 Hệ thống thông tin kế toán: Hiểu cấu trúc cơ sở dữ liệu quan hệ Hệ thống thông tin kế toán Bạn là kế toán viên tại công ty kế toán DGJ, đó là sự trợ giúp- ing Pizza My Heart tạo cơ sở dữ liệu quan hệ cho hoạt động kinh doanh của họ. Bạn đã tạo các bảng được hiển thị trước đó. Bây giờ, bạn phải tạo các kết nối giữa các bảng. Xác định các trường sẽ tạo liên kết giữa các bảng sau. Bàn Trường Bán hàng và khách hàng 1. Bán hàng và nhân viên 2. Bán hàng và xe tải 3. Bán hàng và Thực đơn 4. Nhân viên và mua hàng 5. Tiền gửi và tiền mặt 6. Mua hàng và nguyên liệu thô 7. Mua hàng và nhà cung cấp 8.

Hãy xem xét từng câu hỏi sau đây và liệt kê các bảng và trường cần thiết để trả lời chúng. Cho biết liệu phép nối nên là phép nối trái, phải hay nối trong. Câu hỏi Bảng Trường Loại tham gia

- **9. Có nhà cung cấp nào chưa mua hàng không?**

- **10. Địa chỉ của nhân viên có khớp với địa chỉ của nhà cung cấp không?**

- **11. Tổng doanh thu theo từng món trong thực đơn là bao nhiêu?**

- **12. Tổng doanh số bán hàng bằng xe tải là bao nhiêu?**

- 13. Có giao dịch mua hàng nào được thực hiện từ các nhà cung cấp không nằm trong Bàn của nhà cung cấp? Kiểm toán PAC 2.2 : Tạo phân tích về tính đầy đủ của tiền mặt Dữ liệu Kiểm toán Bạn là kiểm toán viên trong cuộc kiểm toán Pizza My Heart, người được giao nhiệm vụ kiểm toán tiền mặt.

Sử dụng các tệp dữ liệu biên lai tiền mặt và tiền gửi ngân hàng để hoàn thành các phân tích sau đây như một phần của cuộc kiểm toán của bạn tiền mặt trong quý đầu tiên. Sử dụng bảng tổng hợp nếu có.

- 1. Tổng hợp doanh số bán hàng hàng ngày, doanh số bán tiền mặt hàng ngày và doanh số thẻ tín dụng hàng ngày của Xe tải 1.

- **2. Tổng hợp tiền gửi hàng ngày bằng Xe tải 1.**

- 3. Lập bảng đối chiếu số tiền thu hàng ngày với tiền gửi hàng ngày. Sau đó, xác định xem có bất kỳ doanh số bán hàng không phù hợp với tiền gửi hàng ngày. PAC 2.3 Kế toán tài chính: Tạo phân tích bán hàng Dữ liệu Kế toán tài chính Bạn đang chuẩn bị kết quả bán hàng quý đầu tiên cho Pizza My Heart.

- 1. Tạo PivotTable tóm tắt doanh số bán hàng theo Xe tải 1 và hiển thị tổng doanh số bán hàng từng tháng trong quý 1 (tháng 1, tháng 2, tháng 3).

- 2. Tạo PivotTable tóm tắt doanh số bán hàng theo sản phẩm trong quý đầu tiên cho Xe tải 1. Sắp xếp dữ liệu từ doanh số cao nhất đến doanh số thấp nhất. PAC 2.4 Kế toán quản lý: Tạo phân tích để hiểu chi phí trên mỗi sản phẩm Dữ liệu Kế toán quản trị Bạn là một kế toán viên quản lý được yêu cầu chuẩn bị một bản phân tích về chi phí. Sử dụng tệp dữ liệu mua hàng để trả lời các câu hỏi sau bằng PivotTable:

- 1. Tổng chi phí trung bình cho mỗi thành phần nguyên liệu thô là bao nhiêu? (Gợi ý: lấy tổng chi phí, không xét đơn vị).

- 2. Chi phí trung bình cho mỗi thành phần nguyên liệu thô của nhà cung cấp là bao nhiêu? (Gợi ý: Tạo hai phép tính PivotTable quan hệ. Chi phí trên mỗi đơn vị đo lường = Tổng chi phí/(Kích thước * Số lượng) và Chi phí trên mỗi đơn vị = Tổng chi phí/Tổng cộng Số lượng)

- **3. Có nhà cung cấp nào đang tính phí nguyên liệu cao hơn mức trung bình không?**

Trường hợp tiếp theo của Le Grind: Sử dụng số liệu thống kê mô tả để phân tích hoạt động bán hàng trong ba năm đầu kinh doanh Kế toán thuế PAC 2.5: Tạo phân tích để lập kế hoạch mở rộng dữ liệu Kế toán thuế Pizza My Heart đang cân nhắc việc mua một chiếc xe bán đồ ăn khác và Florida tính thuế doanh thu đối với việc bán xe bán đồ ăn. Sal muốn chọn vị trí tốt nhất, không chỉ để bán hàng mà còn cho thuế bán hàng. Sử dụng dân số Florida và thuế bán hàng theo tệp dữ liệu thành phố để tạo hình ảnh trực quan cho thấy thành phố nào có dân số đông nhất và thành phố nào cũng hiển thị mức thuế theo thành phố.

- **1. Mười thành phố đông dân nhất ở Florida là gì?**

- **2. Sử dụng PivotTable để xác định các thành phố có 10 mức thuế suất thấp nhất.**

- 3. Pizza My Heart đang coi Tallahassee là thành phố tiềm năng cho loại xe tải mới. Sal ước tính doanh thu trong năm đầu tiên sẽ là 150.000 USD. Thuế bán hàng sẽ được thu là bao nhiêu? Trường hợp tiếp theo của Le Grind: Sử dụng thống kê mô tả để phân tích Hoạt động bán hàng trong ba năm đầu kinh doanh dữ liệu Truy cập nền tảng học tập trực tuyến của Wiley để biết thông tin cơ bản về trường hợp, các câu hỏi, dữ liệu bổ sung và biết thêm chi tiết về vụ án đang tiếp tục.

#### ** 🎬 Video **

<iframe src="video/Day11/index.html?v=1785919941" style="width: 100%; aspect-ratio: 16/9; max-height: 75vh; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>

#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slideAIAcc/Slide_AIAcc_Day11.pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day11.pdf#view=FitH" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day11.pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

#### ** 📝 Bài tập Trắc nghiệm **

<iframe src="quizzes/Day11/index.html?v=1785919941" style="width: 100%; min-height: 700px; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>


#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Phân biệt dữ liệu Structured vs Unstructured (Độ khó: Dễ)**
Theo Chương 2, hãy cho ví dụ về Dữ liệu có cấu trúc (Structured) và Dữ liệu phi cấu trúc (Unstructured) trong hệ thống tài chính của một doanh nghiệp.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Structured Data: Sổ cái kế toán, Bảng cân đối, số lượng hàng tồn kho (dữ liệu dạng bảng biểu, số liệu rõ ràng trong CSDL quan hệ).
- Unstructured Data: Email trao đổi của ban giám đốc, hình ảnh hóa đơn viết tay, đoạn ghi âm cuộc gọi của khách hàng đến phòng CSKH.
</details>
<br>

**Bài tập 2: Làm sạch dữ liệu - Data Cleansing (Độ khó: Trung bình)**
Làm sạch dữ liệu là bước tốn nhiều thời gian nhất (chiếm 80% thời gian phân tích). Nêu 3 lỗi dữ liệu phổ biến cần xử lý trước khi chạy mô hình phân tích rủi ro.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- 1. Missing values (Dữ liệu bị thiếu hoặc rỗng, ví dụ thiếu ngày sinh khách hàng).
- 2. Duplicates (Dữ liệu bị lặp lại nhiều lần do lỗi hệ thống).
- 3. Outliers (Dữ liệu ngoại lai phi lý, ví dụ tuổi = 999).
</details>
<br>

**Bài tập 3: Độ lệch chuẩn (Standard Deviation) trong đo lường rủi ro (Độ khó: Khó)**
Độ lệch chuẩn đo lường điều gì trong thống kê phân tích? Tại sao dữ liệu lợi nhuận tài chính có độ lệch chuẩn cao lại được coi là mang tính rủi ro nguy hiểm?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Độ lệch chuẩn đo lường mức độ phân tán của dữ liệu xung quanh giá trị trung bình.
- Lợi nhuận có độ lệch chuẩn cao nghĩa là nó dao động biên độ rất mạnh (tháng lãi lớn, tháng lỗ nặng). Sự biến động (Volatility) khó đoán định này chính là định nghĩa cốt lõi của Rủi ro tài chính.
</details>
<br>
<!-- tabs:end -->
