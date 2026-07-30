## 2.4 Những Thước đo Mô tả Nào Giúp Chúng Ta Hiểu Dữ Liệu?

**MỤC TIÊU HỌC TẬP 4 (LEARNING OBJECTIVE 4)**
**Nhận diện các thước đo mô tả được sử dụng để thực hiện phân tích dữ liệu.**

Bạn đã học được cách xác định và trích xuất dữ liệu và một số phương pháp tiếp cận cơ bản để phân tích nó. Ở phần trước của khóa học, bạn cũng đã học được rằng có bốn loại phân tích dữ liệu:
- Phân tích Mô tả (Descriptive)
- Phân tích Chẩn đoán (Diagnostic)
- Phân tích Dự đoán (Predictive)
- Phân tích Kê toa (Prescriptive)

Hãy nhớ lại rằng phân tích mô tả giúp khám phá những gì đã hoặc đang xảy ra trong dữ liệu. Tại sao phân tích mô tả được coi là trọng tâm của phân tích dữ liệu? Không có sự hiểu biết cơ bản đó về dữ liệu, việc tiến tới các phương pháp phân tích dữ liệu phức tạp hơn là bất khả thi. Đôi khi phân tích mô tả là tất cả những gì cần thiết, nhưng thường thì phương pháp này là tiền thân cho các phân tích chẩn đoán, dự đoán, và kê toa. Kỹ năng phân tích dữ liệu cốt lõi cho phân tích mô tả là hiểu về thống kê mô tả (descriptive statistics) và phân tích tương quan (correlation analysis).

Thống kê mô tả khám phá các quan sát trung bình trong dữ liệu, hình dạng của dữ liệu và sự phân phối của dữ liệu. Ngoài ra, phân tích tương quan có thể chỉ ra các mối quan hệ trong dữ liệu. Cùng với nhau, các thống kê này cung cấp những hiểu biết sâu sắc về dữ liệu (data insights).

### Các thước đo vị trí (Measures of Location)
Các thước đo vị trí xác định quan sát trung bình (average), hoặc điển hình (typical), trong một tập dữ liệu.

#### Số Trung bình (Mean), Số Trung vị (Median), và Yếu vị (Mode)
Thước đo xu hướng tập trung (measure of central tendency) là một giá trị duy nhất mô tả một tập dữ liệu bằng cách xác định vị trí trung tâm trong tập dữ liệu đó. Có ba thước đo xu hướng tập trung:
- **Số Trung bình (Mean):** Tổng của tất cả các quan sát trong một tập dữ liệu chia cho tổng số lượng các quan sát.
- **Số Trung vị (Median):** Giá trị nằm ở giữa khi dữ liệu được sắp xếp từ nhỏ nhất đến lớn nhất.
- **Yếu vị (Mode):** Quan sát xuất hiện thường xuyên nhất.

Xác định mean và median là bước đầu tiên để hiểu dữ liệu trong phân tích mô tả. Hai thước đo này thường tương tự nhau, nhưng do mean có thể bị ảnh hưởng bởi các ngoại lệ (outliers - những giá trị cực đoan trong tập dữ liệu), nên có thể có một sự khác biệt lớn giữa chúng. Nếu có các ngoại lệ trong dữ liệu, thì median là đại diện tốt hơn cho giá trị trung tâm trong tập dữ liệu.

Mode hữu ích trong các tập dữ liệu có một lượng nhỏ các giá trị duy nhất. Ví dụ, một báo cáo tuổi nợ phải thu (accounts receivable aging report) có thể có các giá trị là 30, 60, và 90 ngày. Một mode của dữ liệu báo cáo tuổi nợ sẽ tiết lộ danh mục nào có nhiều quan sát nhất. Nếu có ít giá trị lặp lại, thì mode không phải là một thước đo hữu ích về xu hướng tập trung.

Excel được sử dụng ở đây để tính toán mean và median và diễn giải các kết quả, nhưng nhiều công cụ khác cũng có thể tính toán các giá trị mean và median. Trên thực tế, tất cả các phần mềm trực quan hóa dữ liệu đều có thể tính toán mean và median. Bất kể nó được tính toán như thế nào, có hai điều quan trọng:
- Hiểu cách tính toán các thước đo.
- Biết cách diễn giải kết quả.

#### Tính toán Các Thước đo Vị trí
Chúng ta sẽ sử dụng lại ví dụ về trường đại học để minh họa cách tính toán mean, median, và mode. Tuy nhiên, thay vì tài sản, chúng ta sẽ thực hiện phân tích mô tả về bảng lương của trường đại học.

> **Data** Hình minh họa 2.36 là một phần trích xuất từ tập dữ liệu bảng lương của trường đại học. Tập dữ liệu hiển thị cột chức danh nhân viên và mức lương hàng năm cho tất cả nhân viên của trường đại học (10.789 nhân viên).

Hai bước đầu tiên liên quan đến các hàm Excel:
1. Tính toán mean sử dụng hàm Excel `AVERAGE`. Công thức là `=AVERAGE(C2:C10790)`. Kết quả là $40,065.88.
2. Tính toán median sử dụng hàm Excel `MEDIAN`. Công thức là `=MEDIAN(C2:C10790)`. Kết quả là $28,276.00.

Việc so sánh hai thước đo cho thấy có một sự chênh lệch lớn giữa mức lương trung bình (mean) và mức lương trung vị (median) cho một nhân viên ($11,789.88). Điều gì có thể gây ra hiện tượng này? Hãy nhớ rằng, mean có thể bị ảnh hưởng bởi các ngoại lệ. Dữ liệu có thể được kiểm tra thêm để xác định xem có số tiền lương nào cực kỳ cao hoặc thấp hay không.
3. Cuối cùng, sử dụng tùy chọn bộ lọc (filter) của Excel trong tệp dữ liệu để lọc các mức lương từ cao nhất xuống thấp nhất.

Hình minh họa 2.37 hiển thị năm mức lương cao nhất và năm mức lương thấp nhất.

**HÌNH MINH HỌA 2.36 (ILLUSTRATION 2.36) Dữ liệu Bảng lương Đại học**

![ILLUSTRATION 2.36](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.36.png)

**HÌNH MINH HỌA 2.37 (ILLUSTRATION 2.37) Các Mức lương Đại học từ Cao nhất đến Thấp nhất**

![ILLUSTRATION 2.37](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.37.png)

Xét về mức lương mean cao hơn bao nhiêu so với median, rất có thể có nhiều mức lương ở số tiền thấp hơn là số tiền cao hơn. Chúng ta có thể hiểu rõ hơn về sự khác biệt giữa các mức lương mean và median bằng cách xem xét mức độ biến động (variation) trong dữ liệu.

### Các thước đo độ phân tán (Measures of Dispersion)
Trong ví dụ về tiền lương, đã có một sự khác biệt lớn giữa số tiền lương mean và median. **Các thước đo độ phân tán (measures of dispersion)**, mô tả mức độ biến động trong dữ liệu, có thể giúp tìm ra nguyên nhân của sự chênh lệch này. Dữ liệu bị dàn trải hay co cụm lại với nhau? Nói cách khác, khoảng cách từ tất cả các quan sát, hay các điểm dữ liệu, đến giá trị mean là bao xa?

#### Phương sai (Variance) và Độ lệch chuẩn (Standard Deviation)
Có hai thước đo độ phân tán được sử dụng rộng rãi:
- **Phương sai (Variance)** là trung bình bình phương khoảng cách giữa các điểm dữ liệu trong tập dữ liệu và giá trị mean.
- **Độ lệch chuẩn (Standard deviation)** là căn bậc hai của phương sai.

Mặc dù phương sai là cần thiết để tính toán độ lệch chuẩn, nhưng thông thường chỉ có độ lệch chuẩn được báo cáo vì nó dễ diễn giải hơn phương sai. Nó dễ hiểu hơn bởi vì nó có cùng đơn vị đo với mean. Trong ví dụ về bảng lương đại học, độ lệch chuẩn sẽ được tính bằng đô la của mức lương hàng năm.

#### Tính toán Các Thước đo Độ phân tán
> **Data** Các thước đo độ phân tán có thể được tính toán bằng cách sử dụng Microsoft Excel (Hình minh họa 2.38).

**HÌNH MINH HỌA 2.38 (ILLUSTRATION 2.38) Dữ liệu Bảng lương Đại học**

![ILLUSTRATION 2.38](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.38.png)

Một lần nữa, tính toán các thước đo này bằng cách thực hiện các phép tính trong Excel:
1. Tính phương sai sử dụng hàm Excel `VAR`. Công thức là `=VAR(C2:C10790)`. Kết quả là $1,939,797,496.92
2. Tiếp theo, tính độ lệch chuẩn sử dụng hàm Excel `STDEV`. Công thức là `=STDEV(C2:C10790)`. Kết quả là $44,043.13

Mặc dù không có sự diễn giải thực tế về con số phương sai, nhưng có sự diễn giải cho độ lệch chuẩn:
- Một độ lệch chuẩn thấp cho thấy các quan sát trong tập dữ liệu có xu hướng gần với giá trị mean của tập dữ liệu đó.
- Một độ lệch chuẩn cao cho thấy các giá trị dàn trải qua một phạm vi rộng hơn.

Trong ví dụ này, độ lệch chuẩn $44,043.14 chỉ ra rằng một quan sát, trong trường hợp này là tiền lương hàng năm của một nhân viên, trong tập dữ liệu có thể chênh lệch $44,043.14 so với mean. Nhớ lại rằng mean là $40,068.88, do đó $44,043.14 sẽ được coi là một độ lệch chuẩn cao.

Một cách khác để đánh giá độ phân tán là sử dụng một biểu đồ phân tán (scatterplot - hay còn gọi là scatter chart) để trực quan hóa dữ liệu (Hình minh họa 2.39).

**HÌNH MINH HỌA 2.39 (ILLUSTRATION 2.39) Biểu đồ phân tán Bảng lương Đại học**

![ILLUSTRATION 2.39](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.39.png)

Tiền lương phân tán rộng rãi giữa $0 và cao hơn một chút so với $450,000. Trực quan hóa dữ liệu này trùng khớp với độ lệch chuẩn lớn ở mức $44,043.14.

### Các thước đo hình dạng (Measures of Shape)
Ngoài việc hiểu về độ phân tán của dữ liệu, việc hiểu sự phân phối, hay hình dạng của nó cũng rất quan trọng. **Các thước đo hình dạng (Measures of shape)** mô tả sự phân phối của dữ liệu trong tập dữ liệu. Cách một tập dữ liệu được định hình có thể tiết lộ thước đo xu hướng tập trung tốt nhất nên được sử dụng, hoặc nó có thể hiển thị các mẫu hình trong dữ liệu.

#### Hệ số Bất đối xứng (Skewness) và Độ nhọn (Kurtosis)
Các tập dữ liệu thường có hình dạng đối xứng hoặc không đối xứng. Trong một phân phối đối xứng, mean, median, và mode đều bằng nhau và phân phối dữ liệu ở bên phải của mean giống hệt với dữ liệu ở bên trái của mean. Một phân phối đối xứng sẽ trông giống như một đường cong hình chuông (bell curve) trong một biểu đồ (Hình minh họa 2.40).

**HÌNH MINH HỌA 2.40 (ILLUSTRATION 2.40) Phân phối Đối xứng (Symmetrical Distribution)**

![ILLUSTRATION 2.40](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.40.png)

Hình dạng của phân phối có thể được xác định bằng cách vẽ biểu đồ dữ liệu hoặc bằng cách sử dụng hai thước đo thống kê. Thường thì cả hai đều phù hợp. Hai thước đo hình dạng là skewness (độ lệch/hệ số bất đối xứng) và kurtosis (độ nhọn).

**Skewness** mô tả sự thiếu đối xứng của dữ liệu:
- Các phân phối có đuôi kéo dài về bên phải của mean được coi là **lệch phải (positively skewed)**.
- Các phân phối có đuôi kéo dài về bên trái của mean là **lệch trái (negatively skewed)**.

**HÌNH MINH HỌA 2.41 (ILLUSTRATION 2.41) Các Ví dụ về Độ Lệch (Skewness)**

![ILLUSTRATION 2.41](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.41.png)

**Hệ số bất đối xứng (coefficient of skewness - CS)** đo lường độ lệch của một phân phối. Nếu CS là âm, thì dữ liệu lệch trái. Nếu CS là dương, dữ liệu lệch phải. Mức độ lệch có thể được diễn giải thông qua giá trị tuyệt đối của CS:
- |CS| > 1, mức độ lệch cao
- 0.5 ≤ |CS| ≤ 1, độ lệch vừa phải
- |CS| < 0.5, tương đối đối xứng

Tính hệ số bất đối xứng bằng cách sử dụng hàm Excel `=SKEW(data range)`. 
> **Data** Hình minh họa 2.42 hiển thị hàm Excel và kết quả sử dụng tệp dữ liệu bảng lương đại học. CS là dương 2.3, cho thấy dữ liệu có mức độ lệch cao và lệch về bên phải.

**HÌNH MINH HỌA 2.42 (ILLUSTRATION 2.42) Độ lệch (Skewness) và Độ nhọn (Kurtosis) của Dữ liệu Bảng lương Đại học**

![ILLUSTRATION 2.42](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.42.png)

**Kurtosis** đề cập đến mức độ nhọn (peaked) hoặc dẹt (flat) của biểu đồ tần suất dữ liệu. **Hệ số độ nhọn (coefficient of kurtosis - CK)** đo lường mức độ nhọn của một phân phối:
- Nếu CK lớn hơn 3, thì dữ liệu hơi nhọn với độ phân tán ít hơn.
- Nếu CK nhỏ hơn 3, dữ liệu hơi dẹt với mức độ phân tán rộng.

Hệ số độ nhọn có thể được tính trong Excel bằng cách sử dụng hàm `=KURT(data range)`.
Hình minh họa 2.42 cho thấy CK của dữ liệu lương đại học là 8.2. Điều này cho thấy dữ liệu rất nhọn với ít độ phân tán.

#### Các Phân phối Tần số (Frequency Distributions) và Biểu đồ Tần suất (Histograms)
Cùng với các thước đo CS và CK, hình dạng của phân phối có thể được trực quan hóa bằng hai thước đo khác:
- Một **phân phối tần số (frequency distribution)** là một đại diện của dữ liệu tóm tắt số lượng các quan sát trong một khoảng nhất định. Ví dụ, số lượng nhân viên theo các nhóm mức lương.
- Một **biểu đồ tần suất (histogram)** là một biểu đồ cột của một phân phối tần số, trong đó chiều cao của cột phản ánh tần số (frequency) trong khoảng đó. Ví dụ, chúng ta có thể muốn nhóm các mức lương theo từng số tiền $10,000, $20,000, và $30,000 rồi sau đó đếm xem có bao nhiêu nhân viên ở mỗi hạng mục.

Các thước đo này có thể được tạo trong các phần mềm trực quan hóa dữ liệu như Power BI, Tableau, và trong Microsoft Excel bằng cách sử dụng công cụ Analysis Toolpak. Analysis Toolpak là một tiện ích bổ sung (add-on) miễn phí cho Excel. Một khi được thêm vào, nó sẽ nằm dưới thẻ Data. Hình minh họa 2.43 hiển thị nơi để tìm công cụ Data Analysis và hộp thoại tương ứng mở ra sau khi nhấp vào Data Analysis.

**HÌNH MINH HỌA 2.43 (ILLUSTRATION 2.43) Công cụ Data Analysis của Excel**

![ILLUSTRATION 2.43](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.43.png)

1. Để chuẩn bị một biểu đồ histogram và phân phối tần số, hãy chọn **Histogram** và nhấp **OK**.
2. Một hộp thoại sẽ mở ra (Hình minh họa 2.44).
3. Có hai hộp đầu vào (input boxes):
   - **Input Range** là dữ liệu sẽ được trực quan hóa. Việc chọn tiêu đề cột và đánh dấu chọn hộp **Labels** là rất hữu ích để histogram được dán nhãn bằng tiêu đề của dữ liệu đang được trực quan hóa (Hình minh họa 2.44).
   - Hộp đầu vào tiếp theo là **Bin Range**, dùng để xác định các nhóm được sử dụng cho phân phối tần số và các cột histogram. Chúng phải được thiết lập trước khi mở hộp thoại. Tạo Bin Range bằng cách thiết lập một cột chứa các giá trị dùng để nhóm dữ liệu. Nhìn chung, các giá trị này nên ở các mức tăng bằng nhau và số lượng nhóm nên từ 5 đến 15.
4. Cuối cùng, chọn nơi kết quả sẽ được xuất ra. Hãy đảm bảo đánh dấu kiểm hộp **Chart Output** trước khi nhấp OK.

**HÌNH MINH HỌA 2.44 (ILLUSTRATION 2.44) Hộp thoại Histogram**

![ILLUSTRATION 2.44](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.44.png)

Làm thế nào bạn biết cần tạo bao nhiêu nhóm? Cách tốt nhất là thử nghiệm với dữ liệu để tìm ra một con số sẽ tạo ra một sự trực quan hóa hữu ích. Ví dụ, việc sử dụng ít nhóm hơn có nghĩa là độ rộng của các nhóm sẽ rộng hơn và trực quan hóa có thể cung cấp cái nhìn chi tiết kém hơn. Thường thì việc chia khoảng (giá trị lớn nhất – giá trị nhỏ nhất) cho số lượng nhóm bạn muốn hiển thị có thể là một điểm bắt đầu tốt.

> **Data** Các bước này có thể được sử dụng để tạo một histogram với tệp dữ liệu bảng lương đại học:
1. Mở bảng tính và tạo một cột cho các khoảng chia (bins).
2. Đầu tiên, xác định khoảng dữ liệu. Mức lương tối thiểu là $78.00 và mức lương tối đa là $468,675.00, cho thấy có một phạm vi dữ liệu rộng. Tạo 12 nhóm (bins), bắt đầu bằng $8,000 với khoảng tăng (increments) là $20,000 (Hình minh họa 2.45).

**HÌNH MINH HỌA 2.45 (ILLUSTRATION 2.45) Dữ liệu Bảng Lương, Các Bins, và Hộp thoại Histogram**

![ILLUSTRATION 2.45](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.45.png)

Kết quả từ hộp thoại histogram được trình bày trong Hình minh họa 2.46.

**HÌNH MINH HỌA 2.46 (ILLUSTRATION 2.46) Phân phối Tần số và Histogram Dữ liệu Bảng lương Đại học**

![ILLUSTRATION 2.46](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.46.png)

Histogram tiết lộ một số thông tin về hình dạng của tập dữ liệu, bao gồm việc hầu hết dữ liệu được nhóm lại trong khoảng từ $8,000 đến $48,000:
- Dữ liệu sau đó mỏng dần về bên phải. Điều này củng cố cho kết quả của các thước đo vị trí và hình dạng. Nhớ lại rằng median của dữ liệu là $28,276.00, và mean là $40,065.88. Dữ liệu đạt đỉnh tại giá trị mode.
- Dữ liệu sau đó kéo dài thành một đuôi về phía bên phải, điều này củng cố cho kết quả về hệ số bất đối xứng là một số dương 2.3.
- Cuối cùng, dữ liệu rất nhọn. Phần lớn (69%) nằm trong ba cột đầu tiên của histogram. Điều này hỗ trợ cho kết quả hệ số độ nhọn (kurtosis) là 8.2, chỉ ra rằng dữ liệu có độ nhọn cao và ít phân tán.

#### Các Công cụ Thống kê Mô tả
Bây giờ bạn đã học cách tính toán các thước đo vị trí, độ phân tán và hình dạng bằng cách sử dụng các hàm Excel đơn lẻ. Có một công cụ Excel khác, **Descriptive Statistics**, có thể tính toán tất cả các thước đo này cùng một lúc (Hình minh họa 2.47):
1. Chọn Descriptive Statistics từ danh sách Analysis Tools.
2. Sử dụng hộp thoại Descriptive Statistics để nhập vào phạm vi dữ liệu cần phân tích.
3. Khi phạm vi dữ liệu đã được nhập, chọn labels (nếu bạn đã chọn hàng có chứa tiêu đề cột), chọn nơi xuất kết quả, chọn Summary statistics, và nhấp OK.

**HÌNH MINH HỌA 2.47 (ILLUSTRATION 2.47) Công cụ và Hộp thoại Descriptive Statistics trong Excel**

![ILLUSTRATION 2.47](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.47.png)

Excel sau đó sẽ tính toán các thống kê mô tả và in kết quả trên một trang tính mới (Hình minh họa 2.48).

**HÌNH MINH HỌA 2.48 (ILLUSTRATION 2.48) Các Thống kê Mô tả về Dữ liệu Lương Đại học**

![ILLUSTRATION 2.48](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.48.png)

Các phần mềm thống kê thường có một tính năng tương tự để tính toán đồng thời nhiều số liệu thống kê mô tả. Dù chúng ta sử dụng nhiều hàm Excel riêng lẻ hoặc chỉ sử dụng một công cụ để tính toán, việc khám phá ra hình dạng của một tập dữ liệu giúp chúng ta hiểu dữ liệu tốt hơn. Còn có một thành phần quan trọng khác - đó là hiểu các mối quan hệ bên trong một tập dữ liệu.

### Phân tích Tương quan (Correlation Analysis)
Phân tích tương quan có thể khám phá các mối quan hệ trong dữ liệu bằng cách đo lường mối quan hệ tuyến tính giữa hai biến. Bước đầu tiên là hiểu cách các biến có tương quan với nhau, và bước thứ hai là thực hiện tính toán sự tương quan.

#### Diễn giải Các Hệ số Tương quan
Tương quan tuyến tính của các biến liên tục được đo lường bằng **hệ số tương quan (correlation coefficient)**, còn được gọi là Hệ số Tương quan Pearson (Pearson Product Moment Correlation Coefficient). Thước đo này là một giá trị số nằm giữa -1 và +1. Giá trị tuyệt đối của số càng cao thì sức mạnh của mối quan hệ càng lớn.

Một tương quan có thể là âm, bằng 0, hoặc dương (Hình minh họa 2.49):
- **Tương quan âm (negative correlation)** là một mối quan hệ nghịch đảo. Khi một biến tăng, biến kia sẽ giảm. Có một mối quan hệ âm giữa doanh số bán súp và nhiệt độ bởi vì khi nhiệt độ giảm thì doanh số bán súp lại tăng.
- **Không có tương quan (No correlation)** chỉ ra rằng không có mối quan hệ giữa các biến. Ví dụ, chúng ta sẽ không kỳ vọng nhiệt độ ngoài trời có bất kỳ tác động nào đến doanh số bán ngũ cốc.
- **Hệ số tương quan dương (positive correlation)** chỉ ra rằng khi một biến tăng, thì biến kia cũng tăng. Chúng ta kỳ vọng có một mối quan hệ dương giữa doanh số bán kem và nhiệt độ ngoài trời. Khi nhiệt độ tăng, doanh số bán kem cũng có xu hướng tăng theo.

**HÌNH MINH HỌA 2.49 (ILLUSTRATION 2.49) Các Ví dụ Về Tương quan**

![ILLUSTRATION 2.49](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.49.png)

Chúng ta cũng có thể xem xét mức độ mạnh yếu của một mối quan hệ. Hệ số tương quan càng cao, nằm giữa mức âm 1 và dương 1, thì mối tương quan càng mạnh. Hình minh họa 2.50 là một hướng dẫn để xác định xem một hệ số tương quan biểu thị một mối quan hệ yếu, vừa phải, hay mạnh.

**HÌNH MINH HỌA 2.50 (ILLUSTRATION 2.50) Diễn giải Các Hệ số Tương quan**

![ILLUSTRATION 2.50](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.50.png)

Hãy tưởng tượng bạn đang kiểm tra mối quan hệ giữa doanh số bán kem và nhiệt độ ngoài trời. Nếu hệ số tương quan của doanh số bán và nhiệt độ là dương 0.75, thì có một mối quan hệ dương mạnh mẽ giữa doanh số bán và nhiệt độ. Khi nhiệt độ tăng, doanh số bán kem tăng và ngược lại. (Hình minh họa 2.51)

**HÌNH MINH HỌA 2.51 (ILLUSTRATION 2.51) Ví dụ Về Tương quan Dương**

![ILLUSTRATION 2.51](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.51.png)

Giả sử thay vào đó chúng ta đang kiểm tra mối quan hệ giữa chi phí sưởi ấm và nhiệt độ, và hệ số tương quan là âm 0.70 (Hình minh họa 2.52).

**HÌNH MINH HỌA 2.52 (ILLUSTRATION 2.52) Ví dụ Về Tương quan Âm**

![ILLUSTRATION 2.52](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.52.png)

Trong trường hợp này, có một sự tương quan âm mạnh mẽ giữa chi phí sưởi ấm và nhiệt độ. Khi nhiệt độ giảm, chi phí sưởi ấm một ngôi nhà sẽ tăng và ngược lại.

#### Thực hiện Phân tích Tương quan
Tương quan có thể được đánh giá một cách trực quan bằng cách chuẩn bị một biểu đồ phân tán (scatterplot), giống như những biểu đồ trong Hình minh họa 2.49, và sau đó vẽ một đường. Điều này sẽ cho biết liệu có tồn tại sự tương quan hay không và liệu nó là dương hay âm.

Hệ số tương quan có thể được tính bằng tay với một công thức hoặc bằng phần mềm. Tất cả các phần mềm thống kê đều có thể tính toán một hệ số tương quan, bao gồm cả Microsoft Excel (được sử dụng trong ví dụ này). Bất kể phần mềm nào được sử dụng, việc giải thích kết quả đều giống nhau. Có hai cách để thực hiện phân tích tương quan trong Excel:
- Sử dụng hàm `CORREL`.
- Sử dụng tùy chọn Correlation trong công cụ Data Analysis.

Lợi ích của việc sử dụng tùy chọn Correlation trong công cụ Data Analysis là có thể tạo một bảng tương quan cho nhiều biến cùng lúc. 
> **Data** Chúng ta sử dụng dữ liệu bảng lương đại học để minh họa tùy chọn tương quan trong Excel và sau đó diễn giải kết quả.

Trong tab Salary Hours của tệp dữ liệu (Hình minh họa 2.53), hãy thực hiện một phân tích tương quan để xem có tương quan nào giữa mức lương hàng năm và số giờ làm việc hay không.

**HÌNH MINH HỌA 2.53 (ILLUSTRATION 2.53) Dữ liệu Lương và Giờ làm việc của Đại học**

![ILLUSTRATION 2.53](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.53.png)

Hình minh họa 2.54 hiển thị hộp thoại tương quan mở ra sau khi nhấp vào Correlation và chọn OK trong trình đơn thả xuống Data Analysis Tools. Input range trong hộp thoại chứa các cột đang được kiểm tra tương quan. Ví dụ này đang kiểm tra sự tương quan giữa cột G (Annual Salary) từ các hàng 1 – 10790, và cột H (Hours Worked) từ các hàng 1 – 10790.

**HÌNH MINH HỌA 2.54 (ILLUSTRATION 2.54) Công cụ Data Analysis và Hộp thoại Tương quan**

![ILLUSTRATION 2.54](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.54.png)

Hộp thoại trong Hình minh họa 2.54 hiển thị các dữ liệu đầu vào cần thiết để chạy phân tích tương quan. Kết quả của phân tích tương quan được trình bày trong Hình minh họa 2.55:
- Hệ số tương quan là 0.552.
- Có một sự tương quan dương vừa phải giữa mức lương hàng năm và số giờ làm việc.

Nói cách khác, khi số giờ làm việc tăng thì mức lương hàng năm cũng tăng theo.

**HÌNH MINH HỌA 2.55 (ILLUSTRATION 2.55) Phân tích Tương quan Lương Đại học**

![ILLUSTRATION 2.55](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.55.png)

Tại sao lại không có một mối tương quan mạnh mẽ hơn? Một mối tương quan mạnh giữa số giờ làm việc và mức lương hàng năm được trả dường như hợp lý. Tuy nhiên, nếu nhân viên được trả một mức lương cố định hàng năm thay vì trả theo giờ, thì điều đó sẽ làm giảm sự tương quan đối với số giờ.

Phân tích tương quan có thể giúp khám phá các mối quan hệ trong dữ liệu và hiểu được sức mạnh của chúng. Nhưng đừng bao giờ đưa ra giả định rằng một biến này là nguyên nhân làm thay đổi biến kia chỉ vì có sự tương quan giữa hai biến. Rất có thể tìm thấy sự tương quan giữa hai biến mà chẳng liên quan gì đến nhau. Đây là một **tương quan giả (spurious correlation)**, xảy ra khi có một mối quan hệ về mặt toán học nhưng lại không có logic giữa hai biến. Luôn luôn phải đảm bảo các mối tương quan đó là hợp lý (make sense) trước khi sử dụng chúng để đưa ra các quyết định.

---

### Áp dụng (Apply It 2.4)
**Sử dụng Thống kê Mô tả để Kiểm toán Chi phí Bảo hành (Use Descriptive Statistics to Audit Warranty Expense)**

> **Data** **Kiểm toán (Auditing)**
Là một kiểm toán viên độc lập (external auditor), bạn được giao phụ trách hợp đồng kiểm toán cho Super Scooters. Một trong những trách nhiệm của bạn là xem xét chi phí bảo hành (warranty expense). Như trong hình minh họa, chi phí bảo hành trung bình của Super Scooters đã tăng trong 3 năm qua.

![Apply It 2.4_1](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.4_1.png)

Để phân tích chi phí bảo hành, bạn quyết định sử dụng thống kê mô tả (descriptive statistics). Thực hiện các phân tích sau đây và diễn giải các kết quả của bạn.
1. Sử dụng tùy chọn Descriptive Statistics trong công cụ Data Analysis để tính toán các thống kê mô tả cho chi phí bảo hành từ 2023 đến 2025. Diễn giải các thước đo sau:
   - Mean (Số trung bình)
   - Median (Số trung vị)
   - Standard deviation (Độ lệch chuẩn)
   - Kurtosis (Độ nhọn)
   - Skewness (Độ lệch)
2. Thực hiện các thống kê mô tả cho chi phí bảo hành trong năm 2025. Diễn giải các thước đo sau:
   - Mean
   - Median
   - Kurtosis
   - Skewness
3. Chuẩn bị một biểu đồ histogram của Chi phí Bảo hành năm 2025 với các khoảng chia (bins) sau: 200, 400, 600, 800, 1000, 1200, và 1400.
   - Lập biểu đồ dữ liệu.
   - Hình dạng và sự phân phối trong histogram của bạn có hỗ trợ các thước đo về độ nhọn (kurtosis) và độ lệch (skewness) không?

**GIẢI PHÁP (SOLUTION)**
1. Các thống kê mô tả cho chi phí bảo hành từ 2023 đến 2025:

![Apply It 2.4_2](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.4_2.png)

*Diễn giải các thước đo (Measure Interpretation):*
**Thước đo** | **Kết quả** | **Diễn giải**
--- | --- | ---
**Mean** | Mức chi phí bảo hành trung bình cho giai đoạn 3 năm là $343.57. | Chi phí bảo hành trung bình cho tất cả 3,645 đơn hàng bán trong giai đoạn 3 năm là $343.57.
**Median** | Mức chi phí bảo hành trung vị cho giai đoạn 3 năm là $300.00. | Giá trị ở giữa của chi phí bảo hành trong giai đoạn 3 năm, khi xếp hạng chi phí bảo hành từ cao xuống thấp, là $300.
**Standard deviation** | Độ lệch chuẩn trong giai đoạn 3 năm là $244.90. | Đây là một độ lệch chuẩn cao khi so sánh với mean và median. Nó cho thấy một sự phân tán rộng trong các chi phí bảo hành.<br>Đối với bất kỳ lần bán hàng nào, chi phí bảo hành có thể tăng hoặc giảm + / − $244.90 so với giá trị mean.
**Kurtosis** | Hệ số độ nhọn là 1.54. | Giá trị này nhỏ hơn 3, chỉ ra rằng hình dạng của phân phối hơi dẹt với mức độ phân tán rộng.
**Skewness** | Hệ số bất đối xứng là một số dương 1.23. | Giá trị này lớn hơn 1, chỉ ra rằng dữ liệu đạt đỉnh ở quanh giá trị mean và sau đó kéo thành một đuôi sang bên phải.

2. Các thống kê mô tả cho chi phí bảo hành năm 2025:

![Apply It 2.4_3](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.4_3.png)

*Diễn giải các thước đo (Measure Interpretation):*
**Thước đo** | **Kết quả** | **Diễn giải**
--- | --- | ---
**Mean** | Mức chi phí bảo hành trung bình cho năm 2025 là $414.18. | Giá trị này cao hơn so với mức trung bình của ba năm được tìm thấy trong câu hỏi 1.
**Median** | Chi phí bảo hành trung vị cho năm 2025 là $330.00. | Giá trị này đại diện cho điểm chính giữa của sự phân phối nếu dữ liệu được sắp xếp từ thấp đến cao.
**Kurtosis** | Hệ số độ nhọn là 0.93. | Giá trị này nhỏ hơn 3, chỉ ra rằng hình dạng của phân phối có hơi dẹt với mức độ phân tán rộng.
**Skewness** | Hệ số bất đối xứng là số dương 1.18. | Giá trị này lớn hơn 1, chỉ ra rằng dữ liệu có đạt đỉnh xung quanh giá trị mean và sau đó đuôi kéo dài về bên phải.

3. Biểu đồ tần suất (Histogram):

![Apply It 2.4_4](../TaiLieu/textbookForPractice/Figures/Ch_02/Apply%20It%202.4_4.png)

Đúng vậy, hệ số độ nhọn (kurtosis) chỉ ra một sự phân tán rộng. Chi phí bảo hành bị dàn trải từ $200 cho đến $1,200:
- Có ba đỉnh so với việc chỉ có một đỉnh nhọn duy nhất. Hệ số bất đối xứng (skewness) chỉ ra rằng dữ liệu đạt đỉnh ở xung quanh giá trị mean và sau đó có đuôi kéo về bên phải.
- Đỉnh cao nhất nằm ở quanh giá trị mean $414 và sau đó mỏng dần về bên phải.
