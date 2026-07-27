# Buổi 4: AI trong Dự báo Kinh tế Vĩ mô và Phân tích Hành vi Người tiêu dùng

<!-- tabs:start -->

#### ** 🇬🇧 Tiếng Anh **

### 📄 Tài liệu PDF 1: Chương 5: Market Segmentation & AI Customer Analysis

<object data="textbook/Buoi_04A_Chương 5 (Market Segmentation...).pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_04A_Chương 5 (Market Segmentation...).pdf#view=FitH" target="_blank">Nhấn vào đây để tải tài liệu PDF 1</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_04A_Chương 5 (Market Segmentation...).pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 1 (PDF)</a></p>

---

### 📄 Tài liệu PDF 2: Chương 10: Forecasting Financial Health with AI

<object data="textbook/Buoi_04B_Chương 10 (Forecasting Financial Health...).pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_04B_Chương 10 (Forecasting Financial Health...).pdf#view=FitH" target="_blank">Nhấn vào đây để tải tài liệu PDF 2</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_04B_Chương 10 (Forecasting Financial Health...).pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 2 (PDF)</a></p>


#### ** 🇻🇳 Tiếng Việt **

# 5 PHÂN KHÚC THỊ TRƯỜNG BẰNG CÁC THUẬT TOÁN PHÂN CỤM (MARKET SEGMENTATION USING CLUSTERING ALGORITHMS)

5.1 Phân khúc Khách hàng (Segmenting Customers)
5.1.1 Cơ sở của việc Phân khúc (Basis of Segmentation)
5.2 Nhắm mục tiêu Khách hàng Tiềm năng (Targeting Potential Customers)
5.3 Định vị Sản phẩm trong Tâm trí Khách hàng (Positioning the Product in Customers’ Minds)
5.4 Phân khúc Dựa trên Dữ liệu (Data-Driven Segmentation)
5.4.1 Phân khúc theo Hành vi (Behavioral Segmentation)
5.4.2 Phân khúc Động (Dynamic Segmentation)
5.4.3 Vi phân khúc (Microsegments)
5.5 Các Thuật toán Phân cụm cho Phân khúc (Clustering Algorithms for Segmentation)
5.5.1 Mối quan hệ giữa Khoảng cách và Sự Tương đồng (The Relationship Between Distance and Similarity)
5.5.2 Thuật toán k-Means (The k-Means Algorithm)
5.5.3 Thuật toán k-Medoid (The k-Medoid Algorithm)
5.5.4 Sử dụng k-Means để Phân khúc Khách hàng
5.6 Thực hành bằng R: Phân khúc bằng k-Means và k-Medoid
5.7 Hiểu rõ Chương học

### MỤC TIÊU HỌC TẬP (LEARNING OBJECTIVES)
1. Hiểu về các khái niệm STP (Segmentation, Targeting, Positioning) trong tiếp thị.
2. Quyết định cách thức phân khúc khách hàng.
3. Tìm hiểu các cơ sở khác nhau của việc phân khúc.
4. Phân cụm (Cluster) để phân khúc khách hàng bằng thuật toán k-means và k-medoid.
5. Sử dụng k-means để tìm các phân khúc khách hàng mục tiêu.
6. Diễn giải kết quả của quá trình phân tích phân cụm.

## 5.1 PHÂN KHÚC KHÁCH HÀNG (SEGMENTING CUSTOMERS)

Vegan-Always là một nhà hàng mới mở ở Phoenix. Họ muốn gửi phiếu giảm giá (coupons) cho những khách hàng yêu thích đồ chay. Họ có nên gửi những phiếu giảm giá này cho tất cả cư dân của Phoenix không? Mặc dù có thể làm được, nhưng việc phân phối phiếu giảm giá rộng rãi như vậy không chỉ trở nên rất tốn kém mà không phải ai cũng sẽ quan tâm đến các món ăn của nhà hàng. Vì không phải tất cả khách hàng đều giống nhau hoặc có cùng sở thích, việc gửi cùng một thông điệp tiếp thị đến tất cả mọi người là không hiệu quả hoặc sinh lời. Chiến lược tốt nhất cho Vegan-Always là chia toàn bộ dân số Phoenix theo cách mà họ chỉ gửi phiếu giảm giá cho những người có khả năng sẽ ghé thăm nhà hàng. Một cách nhà hàng có thể làm điều này là sử dụng các yếu tố tâm lý học (psychographics) hoặc lối sống (lifestyle). Những người quan tâm nhiều hơn đến môi trường đã chuyển sang ăn chay và có thể sẽ quan tâm hơn đến một nhà hàng như vậy.

Tương tự, nhân khẩu học (demographics) có thể là một cách khác để tìm các nhóm khách hàng phù hợp với nhà hàng. Quá trình chia thị trường thành các nhóm khách hàng có các đặc điểm tương đồng và chọn (các) nhóm phù hợp nhất để doanh nghiệp nhắm mục tiêu (target) được gọi là phân khúc thị trường (market segmentation).

Một cách để hình dung về phân khúc là xem nó như một sự thỏa hiệp giữa tiếp thị đại chúng (mass marketing - giả định rằng tất cả khách hàng đều giống nhau) và tùy chỉnh ở cấp độ cá nhân (individual-level customization - giả định rằng tất cả khách hàng đều là duy nhất). Thay vì nhắm mục tiêu vào từng khách hàng, việc phân khúc cho phép doanh nghiệp nhắm mục tiêu vào các nhóm khách hàng tương tự nhau trong cách họ phản hồi với sản phẩm. Trong các thị trường dựa trên dữ liệu (data-driven markets) hiện nay, việc phân khúc ở mức độ sâu hơn đã trở nên khả thi; do đó, vi phân khúc (microsegmenting) đang trở nên phổ biến. Ví dụ, dựa trên hành vi mua hàng trong quá khứ và sự tương đồng với các khách hàng khác, Amazon có khả năng tạo ra các vi phân khúc (microsegments) và đề xuất các sản phẩm rất cụ thể cho từng khách hàng của mình.

Bước đầu tiên trong phân khúc thị trường (market segmentation) là hiểu lý do tại sao khách hàng mua một sản phẩm. Sản phẩm đó mang lại những lợi ích gì mà khách hàng có thể quan tâm? Doanh nghiệp cần xác định tất cả các nhu cầu của khách hàng mà một sản phẩm hoặc dịch vụ có thể đáp ứng.


Thay vì cố gắng xác định phân khúc khách hàng có khả năng mua một thương hiệu nhất bằng một nghiên cứu dựa trên thái độ (ví dụ: khách hàng thích thương hiệu này đến mức nào?), một sản phẩm có thể được giới thiệu thông qua các mẫu nhỏ và hành vi mua hàng thực tế có thể được theo dõi. Ngoài ra, dựa trên dữ liệu bán hàng, các sản phẩm có thể được sửa đổi trong thời gian thực (real-time) dựa trên các tính năng mà khách hàng ưa thích nhất. Do đó, các thị trường dựa trên dữ liệu (data-driven markets) cho phép một vòng phản hồi (feedback loop) mà qua đó các doanh nghiệp có thể quan sát hoạt động mua hàng thực tế của khách hàng và tinh chỉnh các phân khúc thị trường (market segments).

### 5.4.2 Phân khúc Động (Dynamic Segmentation)
Một kết quả khác của dữ liệu phong phú về khách hàng cho phép doanh nghiệp liên tục cập nhật các phân khúc khách hàng của mình. Thay vì phân khúc tất cả khách hàng một lần và cho rằng sở thích của họ sẽ không thay đổi, phân khúc động (dynamic segmentation) giả định rằng sở thích sẽ thay đổi và liên tục cập nhật xem dịch vụ/sản phẩm nào sẽ được một phân khúc khách hàng cụ thể ưa thích nhất. Nhiều khía cạnh trong cuộc sống của một cá nhân có thể thay đổi. Ví dụ, một nhà sản xuất sô cô la không thể cho rằng chỉ vì một khách hàng đã mua sô cô la đen trong quá khứ thì họ sẽ tiếp tục làm như vậy. Nhu cầu cá nhân, gia đình hoặc sức khỏe của họ có thể thay đổi, khiến họ chuyển sang mua sô cô la không đường hoặc không có hạt. Phân khúc động tính đến khả năng sở thích của khách hàng thay đổi và do đó, phân khúc mà họ thuộc về không phải là tĩnh (static). Một lần nữa, điều quan trọng là các doanh nghiệp phải trau dồi khả năng sàng lọc qua lượng thông tin dồi dào có sẵn cho họ và sử dụng thông tin gần đây nhất, cho dù là hành vi hay thông tin khác, để phân khúc khách hàng.

### 5.4.3 Vi phân khúc (Microsegments)
Như đã đề cập trước đó, hiện nay đã có thể phục vụ các phân khúc khách hàng rất nhỏ bằng cách hiểu sâu sắc sở thích của họ và tùy chỉnh các sản phẩm cho phù hợp. Điều này cũng dẫn đến siêu cá nhân hóa (hyperpersonalization), nơi mỗi dịch vụ/sản phẩm nhắm mục tiêu duy nhất đến một khách hàng cụ thể dựa trên cả dữ liệu nhân khẩu học (demographic data) và dữ liệu hành vi (behavioral data) được thu thập về khách hàng đó. Chẳng hạn, các công ty bảo hiểm có thể bổ sung dữ liệu hiện có như tuổi, giới tính và danh mục sản phẩm hiện tại bằng hành vi trực tuyến như thời gian truy cập trên trang web của họ để phân khúc khách hàng tốt hơn và cung cấp cho khách hàng một sản phẩm được tùy chỉnh cao.

Việc chọn thuật toán để thực hiện phân khúc cũng quan trọng không kém gì dữ liệu dành cho phân khúc. Nhiều lần chúng ta chỉ có các loại dữ liệu khác nhau về khách hàng mà không có thông tin về kết quả kinh doanh như doanh số bán hàng hoặc khách hàng đó có trung thành hay không. Tức là, dữ liệu có xu hướng không được gán nhãn (unlabeled). Bởi vì chúng ta không có bất kỳ nhãn kết quả nào, chúng ta không có khả năng so sánh hiệu suất của mô hình. Nhiệm vụ phổ biến nhất của học không giám sát (unsupervised learning) là phân tích khám phá (exploratory analysis), sử dụng các phương pháp trực quan hóa (đơn giản nhất là phân cụm - clustering) để kiểm tra dữ liệu và thu thập thông tin chi tiết.

Hãy xem qua các thuật toán thường được sử dụng cho phân khúc.

## 5.5 CÁC THUẬT TOÁN PHÂN CỤM CHO PHÂN KHÚC (CLUSTERING ALGORITHMS FOR SEGMENTATION)
Phân cụm (Clustering) thường được sử dụng để phân khúc khách hàng thành các nhóm có bộ nhu cầu tương tự nhau. Việc hiểu thuật toán k-Means và thuật toán k-Medoid rất hữu ích để hình dung quá trình phân cụm hoạt động như thế nào.

> 📸 **Hình ảnh**: Hình ảnh về Phân cụm hoặc Thị trường

### 5.5.1 Mối quan hệ giữa Khoảng cách và Sự Tương đồng (The Relationship Between Distance and Similarity)
Trong phân cụm, các đối tượng (ví dụ: khách hàng) được nhóm lại với nhau dựa trên khoảng cách của chúng trong một không gian đa chiều (multidimensional space). Nguyên tắc cơ bản là nếu hai khách hàng ở gần nhau trong không gian đặc trưng (feature space) của họ, họ sẽ có nhiều điểm tương đồng và do đó nên được nhóm vào cùng một cụm (cluster).

### 5.5.2 Thuật toán k-Means (The k-Means Algorithm)
Thuật toán k-Means là một trong những thuật toán học không giám sát (unsupervised learning) đơn giản và phổ biến nhất được sử dụng để giải quyết vấn đề phân cụm. Quy trình hoạt động bao gồm:
1. Xác định số lượng cụm $k$ (number of clusters).
2. Khởi tạo ngẫu nhiên các trung tâm cụm (centroids).
3. Gán mỗi điểm dữ liệu cho trung tâm cụm gần nhất.
4. Tính toán lại trung tâm của từng cụm dựa trên các điểm dữ liệu đã được gán.
5. Lặp lại bước 3 và 4 cho đến khi các trung tâm không thay đổi đáng kể.

### 5.5.3 Thuật toán k-Medoid (The k-Medoid Algorithm)
Tương tự như k-Means, nhưng thay vì sử dụng giá trị trung bình (mean) để làm trung tâm cụm, k-Medoid sử dụng một điểm dữ liệu thực tế (gọi là medoid) làm trung tâm. Điều này giúp thuật toán chống nhiễu (outliers) tốt hơn k-Means.







bởi vì không có nhiều giá trị ngoại lai (outliers) trong dữ liệu. Nếu số lượng các giá trị ngoại lai tăng lên, k-medoid sẽ đưa ra một giải pháp tốt hơn.

Do đó, chúng ta có thể kết luận phân tích phân cụm của mình bằng những hiểu biết sâu sắc sau đây. Khi muốn thực hiện phân khúc (segmentation), chúng ta có thể sử dụng thuật toán phân cụm như k-Means hoặc k-Medoid. Chúng ta sử dụng phân cụm vì dữ liệu của chúng ta không được gán nhãn (unlabeled), tức là chúng không có nhãn kết quả. Trong ví dụ, chúng ta thấy rằng khi số tiền chi tiêu (amount spent) và thời gian mua sắm (patronage duration) được sử dụng và chúng ta yêu cầu ba cụm, chúng ta có thể thu được các đặc điểm trung bình của khách hàng trong ba cụm đó. Sự khác biệt giữa các khách hàng này cho chúng ta biết doanh nghiệp có thể đưa ra các đề xuất sản phẩm hiệu quả như thế nào đối với khách hàng trong ba phân khúc này.

## 5.6 THỰC HÀNH BẰNG R: PHÂN KHÚC BẰNG K-MEANS VÀ K-MEDOID (IMPLEMENTATION USING R: SEGMENTATION USING K-MEANS AND K-MEDOID)

Để phân tích và vẽ biểu đồ dữ liệu, chúng ta sẽ sử dụng hai gói (packages): `cluster` và `factoextra`. Sau khi nhập dữ liệu, chúng ta căn giữa và chia tỷ lệ nó (center and scale) bằng cách sử dụng hàm `scale()` với các tùy chọn `center = TRUE` và `scale = TRUE`; `center = TRUE` trừ giá trị trung bình cột của một biến khỏi các giá trị cột tương ứng của chúng, và `scale = TRUE` chia các cột (đã được căn giữa) của một biến cho độ lệch chuẩn (standard deviations) của chúng. Quá trình này chuyển đổi các giá trị của mỗi biến thành điểm $z$ (z scores) của chúng. Đây là một bước quan trọng trước khi phân tích cụm (cluster analysis) vì mỗi biến của một tập dữ liệu có thể được đo trên các thang đo khác nhau. Ví dụ, trong tập dữ liệu của chúng ta, thời gian khách hàng quen của cửa hàng được tính bằng tháng, nhưng số tiền chi tiêu được tính bằng đô la. Việc chia tỷ lệ (scaling) dữ liệu đảm bảo rằng không có sự biến dạng nào do sự khác biệt trong các thang đo được sử dụng giữa các biến.

Khi chúng ta đã đọc và chia tỷ lệ dữ liệu (`df`), mã thực tế để chạy k-Means khá đơn giản. Trong hàm `kmeans()`, `centers` chỉ định số lượng cụm ($k$), sau đó `nstart = 25` đặt 25 trung tâm (centroids) ngẫu nhiên ban đầu và chọn trung tâm tốt nhất. Giá trị `nstart` cao hơn mang lại giải pháp ổn định hơn, nhưng đối với các tập dữ liệu lớn hơn, điều này có thể tốn nhiều thời gian tính toán hơn.

```R
library(cluster)
library(factoextra)
 
set.seed(12345) # Thiết lập seed để có thể tái tạo kết quả
 
df <- read.csv(url("http://data.mishra.us/files/chapter_segmentation/segmentation_kmeans.csv"))
 
df <- scale(df, center = TRUE, scale = TRUE)
 
k_means <- kmeans(df, centers = 3, nstart = 25)
```

Đoạn mã sau giúp tạo Hình 5.4 bằng cách sử dụng hàm `fviz_cluster()`. Tùy chọn `repel = TRUE` ngăn các điểm dữ liệu tụ lại với nhau và giúp chúng dễ đọc hơn.

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_04A/Figure 5.4 k-Means Segmentation Plot.jpeg" alt="Figure 5.4 k-Means Segmentation Plot" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Figure 5.4 k-Means Segmentation Plot</div>
</div>




```R
fviz_cluster(k_means, data = df,
 repel = TRUE,
 main = "k-means segmentation plot"
)
```

Chúng ta cũng có thể in các trung tâm cụm (cluster centers) cho mỗi cụm trong số ba cụm, như chúng ta đã thấy trong Hình 5.4. Điều này rất hữu ích khi dữ liệu của chúng ta có nhiều hơn hai biến và việc vẽ biểu đồ các cụm trở nên khó khăn hơn. Bằng cách sử dụng các trung tâm cụm, chúng ta có thể đánh giá các đặc điểm trung bình của từng cụm. Nhất quán với biểu đồ, ở đây đầu ra của chúng ta cho thấy các thành viên của cụm 1 có thời gian mua sắm trung bình là -1.009 tháng và đã chi $1.383, trong khi các thành viên của cụm 2 có thời gian mua sắm là -1.006 tháng.

## 5.7 HIỂU RÕ CHƯƠNG HỌC (UNDERSTANDING THE CHAPTER)
- Phân khúc khách hàng là rất quan trọng để xác định chiến lược tiếp thị mục tiêu.
- Dữ liệu cung cấp cái nhìn sâu sắc về nhu cầu và hành vi.
- Các kỹ thuật phân cụm như k-Means giúp tự động hóa và định lượng các phân khúc này.


# 10 DỰ BÁO SỨC KHỎE TÀI CHÍNH CỦA MỘT DOANH NGHIỆP SỬ DỤNG HỒI QUY CÓ PHẠT (FORECASTING THE FINANCIAL HEALTH OF A BUSINESS USING PENALIZED REGRESSION)

10.1 Sức khỏe Tài chính của một Doanh nghiệp (Financial Health of a Business)
10.2 Tầm quan trọng của việc Dự báo Sức khỏe Tài chính của Doanh nghiệp
10.2.1 Ảnh hưởng của Việc vay mượn đối với Sức khỏe Tài chính
10.2.2 Tỷ lệ Nợ và Khả năng Vay mượn
10.3 Tầm quan trọng của việc Biết được Sức khỏe Tài chính đối với Người cho vay
10.3.1 Sức khỏe Tài chính Kém: Phá sản (Bankruptcy)
10.4 Tầm quan trọng của việc Biết Sức khỏe Tài chính của Doanh nghiệp đối với Nhà đầu tư
10.5 Dự báo Sức khỏe Tài chính (Forecasting Financial Health)
10.5.1 Các Chỉ số Tài chính (Financial Ratios)
10.6 Đa cộng tuyến (Multicollinearity)
10.6.1 Kiểm tra Đa cộng tuyến
10.7 Sử dụng Hồi quy có phạt (Penalized Regression) để Đánh giá Sức khỏe Tài chính
10.7.1 Dự đoán Sức khỏe Tài chính bằng LASSO (Predicting Financial Health Using LASSO)
10.7.2 Thông tin Kinh doanh và Các Ứng dụng Khác
10.8 Thực hành bằng R: Đánh giá Sức khỏe của một Doanh nghiệp
10.9 Phụ lục: Bảng Thuật ngữ Tài chính
10.10 Hiểu rõ Chương học

### MỤC TIÊU HỌC TẬP (LEARNING OBJECTIVES)
1. Đánh giá sức khỏe tài chính của một doanh nghiệp.
2. Hiểu được tầm quan trọng của việc dự báo phá sản (bankruptcy forecasting) đối với các nhà đầu tư, người cho vay và doanh nghiệp.
3. Sử dụng hồi quy có phạt (penalized regression) để dự báo sức khỏe tài chính.
4. Xác định đa cộng tuyến và lựa chọn đặc trưng (feature selection) bằng mô hình LASSO.

## 10.1 SỨC KHỎE TÀI CHÍNH CỦA MỘT DOANH NGHIỆP (FINANCIAL HEALTH OF A BUSINESS)

Trong bất kỳ công ty nào, bộ phận tài chính thực hiện các chức năng quan trọng là kiểm soát, lập kế hoạch, ra quyết định và đảm bảo tuân thủ quy định. Bộ phận này cung cấp một cái nhìn hồi tố về cách thức hoạt động của doanh nghiệp bằng cách xem xét nhiều báo cáo tài chính, bao gồm bảng cân đối kế toán, báo cáo kết quả hoạt động kinh doanh và báo cáo lưu chuyển tiền tệ để chỉ ra cho doanh nghiệp biết điểm mạnh và điểm yếu của mình nằm ở đâu. Nó cũng cung cấp một cái nhìn hướng tới tương lai quan trọng dưới dạng nhiều dự báo, bao gồm dự báo lưu chuyển tiền tệ, lập kế hoạch kịch bản (scenario planning) và phân tích độ nhạy (sensitivity analysis). Các mô hình dự báo (Forecasting models) rất thường được sử dụng trong tài chính để thông báo cho những người cho vay (lenders), bản thân doanh nghiệp và một số loại nhà đầu tư khác nhau về nơi họ cần đầu tư nguồn lực trong các khoảng thời gian tới. Những dự báo này cũng xem xét xếp hạng tín dụng, điều kiện thị trường và triển vọng kinh tế vĩ mô rộng lớn hơn. 

Doanh nghiệp nên đầu tư vào đâu? Nên tăng giá hay đưa ra các chương trình khuyến mãi? Liệu công ty có thể tăng lương cho nhân viên hay đã đến lúc cắt giảm chi phí? Liệu công ty có thể đầu tư vào một địa điểm mới hay một sản phẩm mới không? Quản lý tài chính cung cấp một cái nhìn tổng thể về sức khỏe tài chính của một công ty, giúp đưa ra các quyết định chiến lược trên nhiều phòng ban khác nhau. Do đó, dự báo tài chính giúp cung cấp cho ban lãnh đạo doanh nghiệp một bức tranh tổng thể để phát triển các chiến lược tránh tư duy cục bộ trong việc ra quyết định. Việc dự báo như vậy cũng giúp người cho vay xác định xem có nên cho vay hay không và giúp các doanh nghiệp đi vay xác định số tiền họ nên vay.

## 10.2 TẦM QUAN TRỌNG CỦA VIỆC DỰ BÁO SỨC KHỎE TÀI CHÍNH CỦA DOANH NGHIỆP

Các thực thể khác nhau trong công ty cần xác định sức khỏe tài chính của doanh nghiệp vì nó là thông tin đầu vào quan trọng trong các quyết định của họ. Các chủ sở hữu và ban quản lý cần biết doanh nghiệp đang thực hiện các chức năng chính của nó như thế nào để xác định lĩnh vực nào cần đầu tư thêm.


các nhà đầu tư, một cách tối ưu, có thể mua một cổ phần lớn để có tiếng nói lớn hơn trong các hoạt động của công ty. Vốn cổ phần tư nhân (Private equity) là một kiểu nhà đầu tư như vậy. Các công ty cổ phần tư nhân thường có xu hướng đầu tư vào các doanh nghiệp có tiềm năng chưa được hiện thực hóa nhưng đang gặp khó khăn về tài chính, có thể là do nợ cao; làm cho chúng phát triển nhanh chóng; và—nếu (như dự đoán) doanh nghiệp thực sự có tiềm năng chưa được hiện thực hóa—gặt hái những lợi ích.

Do đó, điều quan trọng đối với doanh nghiệp, người cho vay và nhà đầu tư là phải xác định chính xác liệu một doanh nghiệp có tiềm năng phát triển hay liệu quỹ đạo khó khăn tài chính có khả năng tiếp tục hay không. Một toàn bộ lĩnh vực trong tài chính được dành riêng cho việc tìm hiểu và dự đoán những biến số nào có thể được sử dụng để dự đoán liệu một doanh nghiệp sẽ gặp khó khăn tài chính hay, trong trường hợp cực đoan, là phá sản.

## 10.5 DỰ BÁO SỨC KHỎE TÀI CHÍNH (FORECASTING FINANCIAL HEALTH)

Một số biến dự báo (predictors) đã được xem xét có thể giúp dự đoán mức độ tín nhiệm. Hãy tìm hiểu điều này bằng cách sử dụng một ví dụ từ góc độ của một người cho vay như ngân hàng. Khi một doanh nghiệp tiếp cận ngân hàng để yêu cầu vay vốn, ngân hàng có khả năng sẽ sử dụng một số tiêu chí để trước tiên xác định sức khỏe tài chính của doanh nghiệp và sau đó quyết định xem có nên cho vay hay không. Giả sử ngân hàng muốn xác định các biến có thể giúp họ đánh giá sức khỏe tài chính của doanh nghiệp. Cũng giả sử rằng ngân hàng đang thận trọng trong ước tính của mình và định nghĩa mức độ tín nhiệm (creditworthiness) dựa trên tình trạng khó khăn tài chính trong tương lai hoặc khả năng phá sản (bankruptcy). Ngân hàng có thể tập trung vào các biến dự báo tài chính cũng như phi tài chính, nhưng nhiều khi những người cho vay thích xem xét các biến dự báo tài chính để hiểu được sức khỏe tài chính của một doanh nghiệp.

### 10.5.1 Các Chỉ số Tài chính (Financial Ratios)
Các doanh nghiệp báo cáo một số chỉ số tài chính (financial ratios) giúp người cho vay đánh giá sức khỏe tài chính của họ, chẳng hạn như tỷ lệ nợ trên vốn chủ sở hữu (debt-equity ratio), tỷ lệ thanh toán hiện hành (current ratio), tỷ lệ thu nhập (earnings ratio) và tỷ lệ hoạt động (operating ratio). Những tỷ lệ này thường có sẵn trên bảng cân đối kế toán của báo cáo tài chính của một doanh nghiệp. Vui lòng xem định nghĩa chi tiết của những tỷ lệ này trong bảng thuật ngữ được cung cấp trong Phần 10.9 của chương này.

Đối với bất kỳ loại dự báo nào, các doanh nghiệp có xu hướng sử dụng một quy trình lựa chọn biến (variable selection) để phân loại các biến có liên quan khỏi các biến không liên quan. Nếu một doanh nghiệp biết biến nào là có liên quan, họ chỉ có thể sử dụng các biến đó trong các mô hình dự báo của mình. Một lý do khác cho việc lựa chọn biến là để cải thiện độ chính xác của các dự đoán; dự đoán tốt hơn dẫn đến những sai lầm ít tốn kém hơn. Tương tự, khi dự đoán sức khỏe tài chính, điều quan trọng là phải thực hiện lựa chọn biến để tìm ra các biến dự báo (predictors) có liên quan để sử dụng trong các mô hình dự đoán.

Hơn nữa, nhiều biến dự báo tài chính có xu hướng tương quan với nhau (correlated), một số trong đó tương quan khá cao; điều này khiến một số biến dự báo có vẻ quan trọng (significant) khi thực tế không phải vậy—tức là, sự hiện diện của các biến dự báo cộng tuyến (collinear predictors) dẫn đến các dự đoán không chính xác. Hãy tìm hiểu xem đa cộng tuyến (multicollinearity) là gì.

## 10.6 ĐA CỘNG TUYẾN (MULTICOLLINEARITY)

Cộng tuyến (Collinearity) xảy ra khi hai biến dự báo (predictor variables) có tương quan cao. Đa cộng tuyến (Multicollinearity) xảy ra khi có sự tương quan mạnh giữa nhiều biến độc lập. Mặc dù nó không làm giảm khả năng dự đoán của tổng thể mô hình, nhưng nó dẫn đến các ước tính không đáng tin cậy cho các hệ số (coefficients) của các biến dự báo cụ thể. Hồi quy LASSO (LASSO regression) thường được sử dụng để giải quyết vấn đề này vì khả năng lựa chọn đặc trưng (feature selection) của nó, loại bỏ các biến không cần thiết.


gần đây ngân hàng cũng nhận ra rằng các chỉ số (ratios) bao gồm các biến hoạt động (operating variables) như doanh số bán hàng (sales) cũng đáng được xem xét khi dự báo sức khỏe tài chính của một doanh nghiệp. Do đó, ngân hàng đã thu thập dữ liệu chứa 16 tỷ lệ khác nhau của 665 doanh nghiệp có sức khỏe tài chính tốt so với kém. Số liệu trong dữ liệu để đánh giá sức khỏe tài chính là liệu một doanh nghiệp có bị phá sản hay không. Dữ liệu chứa thông tin về một số chỉ số tài chính như tỷ lệ nợ trên vốn chủ sở hữu (debt–equity ratio), tỷ lệ thanh toán hiện hành (current ratio) và tỷ lệ hoạt động (operating ratio) đối với các doanh nghiệp đã hoặc chưa phá sản. Tương tự như những người cho vay khác, Ngân hàng Altra cũng sử dụng dữ liệu về các tỷ lệ này để xây dựng một mô hình có thể giúp đưa ra các dự đoán về sức khỏe tài chính của các doanh nghiệp mà ngân hàng đang xem xét có nên cho vay hay không. Ngân hàng Altra cũng muốn xác định liệu một số tỷ lệ có phải là biến dự báo tốt hơn những tỷ lệ khác hay không; do đó, việc có dữ liệu kèm theo nhãn về việc một doanh nghiệp có bị phá sản hay không là rất hữu ích trong việc xây dựng mô hình. (Dữ liệu được sử dụng trong ví dụ này là giả định.)

Dữ liệu có 16 chỉ số tài chính sau đây, một số trong đó là chỉ số hoạt động, chỉ số tiếp thị hoặc chỉ số kế toán:

- current_ratio_1 = tài sản lưu động / nợ ngắn hạn
- earning_ratio_1 = EBIT (thu nhập trước lãi vay và thuế) / tổng tài sản
- debt_equity_ratio_1 = giá trị sổ sách của vốn chủ sở hữu / tổng nợ phải trả
- accounting_ratio_1 = tổng tài sản / tổng nợ phải trả
- operating_ratio_1 = (hàng tồn kho * 365) / doanh thu
- marketing_ratio_1 = lợi nhuận ròng / doanh thu
- operating_ratio_2 = lợi nhuận từ hoạt động kinh doanh / chi phí tài chính
- marketing_ratio_2 = (tổng nợ phải trả − tiền mặt) / doanh thu
- current_ratio_2 = (tài sản lưu động − hàng tồn kho) / nợ dài hạn
- current_ratio_3 = (tài sản lưu động − hàng tồn kho − khoản phải thu) / nợ ngắn hạn
- operating_ratio_3 = lợi nhuận từ hoạt động kinh doanh / doanh thu
- current_ratio_4 = (tài sản lưu động − hàng tồn kho) / nợ ngắn hạn
- earning_ratio_2 = EBITDA (thu nhập trước lãi vay, thuế, khấu hao và khấu hao vô hình—tức là [lợi nhuận từ hoạt động kinh doanh − khấu hao] / tổng tài sản)
- current_ratio_5 = tài sản lưu động / tổng nợ phải trả
- debt_equity_ratio_2 = nợ dài hạn / vốn chủ sở hữu
- operating_ratio_4 = tổng chi phí / tổng doanh thu

Sử dụng dữ liệu này, chúng ta có thể bắt đầu thực hiện một số thử nghiệm và sau đó xây dựng mô hình. Thử nghiệm đầu tiên chúng ta sẽ tiến hành là kiểm tra xem dữ liệu có bao gồm các biến dự báo cộng tuyến hay không (tức là, liệu có tồn tại sự tương quan cao, cả tích cực hoặc tiêu cực, giữa một số trong 16 biến dự báo hay không). Chúng ta thu được một biểu đồ tương quan như thể hiện trong Hình 10.2. Đúng như kỳ vọng đối với các chỉ số tài chính, biểu đồ cho thấy khá nhiều tỷ lệ có tương quan hơn 0.5 với nhau. Ví dụ, `marketing_ratio_1` và `earnings_ratio_2` có tương quan −0.97 với nhau.

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_04B/Figure 10.2 Correlation Plot.jpeg" alt="Figure 10.2 Correlation Plot" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Figure 10.2 Correlation Plot</div>
</div>






Tiếp theo, chúng ta có thể kiểm tra đa cộng tuyến (multicollinearity) bằng cách sử dụng VIF cho từng biến dự báo.
```R
## current_ratio_1 debt_equity_ratio_1 accounting_ratio_1 operating_ratio
## 4.565160        614.931070          624.345
```


rằng nó đã thu hẹp các tham số $\beta$ của 4 biến dự báo về 0 và do đó, đã chọn 12 từ 16 biến dự báo ban đầu.

```R
(best.lambda <- cv.binomial$lambda.min)
## [1] 8.837698e-05

y4 <- coef(cv.binomial, s="lambda.min", exact=FALSE)
print(y4)
## 17 x 1 sparse Matrix of class "dgCMatrix"
##                                                            s1
## (Intercept)                     1.346913e+01
## current_ratio_1                     9.231917e-02
## debt_equity_ratio_1                     1.297786e+01
## accounting_ratio_1 -1.416379e+01
## operating_ratio_1                    .
## marketing.ratio_1                     3.031253e+00
## operating_ratio_2                     3.493792e-03
## marketing_ratio_2                    .
## current_ratio_2 -1.985339e-05
## current_ratio_3                     2.416489e+00
## operating_ratio_3 -4.810050e+00
## current_ratio_4 -2.503380e+00
## earning_ratio_1                     4.965877e-01
## earning_ratio_2                    .
## current_ratio_5                     7.127187e-01
## debt_equity_ratio_2                    .
## operating_ratio_4                     9.021487e-03
```

Chúng ta đã huấn luyện mô hình hồi quy có phạt (penalized regression model) của mình. Nhưng phần quan trọng là xem nó có thể được sử dụng tốt như thế nào trong dự đoán. Bây giờ chúng ta sử dụng mô hình đã được huấn luyện với giá trị tối ưu của $\lambda$ và đánh giá xem nó hoạt động như thế nào trên một tập dữ liệu kiểm tra riêng biệt (test dataset).

```R
test_predictors <- testData[,c(1:16)]
test_predictors <- data.matrix(test_predictors)
pred = predict(cv.binomial, newx = test_predictors,
 type = "response",s ="lambda.min")
pred <- prediction(pred, testData$class)
 
perf <- performance(pred,"tpr","fpr")
auc_ROCR<- performance(pred,measure ="auc")
```

Chúng ta lại sử dụng đường cong AUC ROC để kiểm tra dự đoán của mô hình LASSO trên tập dữ liệu kiểm tra. Điều này được tính toán (và vẽ biểu đồ) dưới dạng tỷ lệ giữa dương tính giả (false positives) trên trục x và dương tính thật (true positives) trên trục y. Các giá trị AUC cao hơn cho thấy dự đoán mô hình tốt hơn. Hình 10.4 vẽ đường cong này.

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_04B/Figure 10.4 AUC ROC Curve.jpeg" alt="Figure 10.4 AUC ROC Curve" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Figure 10.4 AUC ROC Curve</div>
</div>







```R
plot(perf,colorize=FALSE, col="black") # plot ROC curve
lines(c(0,1),c(0,1),col = "gray", lty = 4 )
text(1,0.15,labels=paste("AUC = ", round(auc_ROCR@y.values[[1]],
 digits=2), sep=""),adj=1)
```

Sử dụng mô hình đã được huấn luyện, bây giờ chúng ta có thể sử dụng nó để dự đoán xem một doanh nghiệp có phá sản hay không. Nếu chúng ta cung cấp giá trị của 16 chỉ số tài chính của một doanh nghiệp mới cho mô hình, nó sẽ cung cấp dự đoán là 0 (sẽ phá sản) hoặc 1 (sẽ không phá sản).

Chúng ta nhập dữ liệu này dưới dạng `new_data`. Vì đối với `glmnet`, dữ liệu phải ở dạng ma trận, chúng ta chuyển đổi nó thành một ma trận có một hàng (`nrow = 1`) và 16 cột (`ncol = 16`).

## 10.9 Phụ lục: Bảng Thuật ngữ Tài chính
Bao gồm các định nghĩa về tỷ lệ nợ trên vốn chủ sở hữu, tỷ lệ thanh toán hiện hành, tỷ lệ thu nhập và tỷ lệ hoạt động.

## 10.10 Hiểu rõ Chương học (UNDERSTANDING THE CHAPTER)
- Sự ảnh hưởng của việc vay mượn đối với sức khỏe tài chính.
- Việc dự báo phá sản là quan trọng đối với nhà đầu tư và chủ nợ.
- Đa cộng tuyến làm nhiễu mô hình, có thể được giải quyết thông qua phương pháp LASSO.




#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slideAIAcc/Slide_AIAcc_Day04.pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day04.pdf#view=FitH" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day04.pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

<!-- tabs:end -->
