# Buổi 5: AI trong Quản lý Chuỗi cung ứng và Phát triển Kinh tế Xanh, Bền vững

<div style="margin: 20px 0; padding: 15px; background-color: #f8f9fa; border-left: 4px solid #0056b3; border-radius: 4px;">
    <h4 style="margin-top: 0;">🎧 Nghe Bài Giảng (Audio)</h4>
    <audio controls style="width: 100%;">
        <source src="audio/AIAcc_Day_05_Random_Forests_AB_Testing_và_rủi_ro.m4a" type="audio/mp4">
        Trình duyệt của bạn không hỗ trợ thẻ audio.
    </audio>
</div>

<!-- tabs:start -->

#### ** 🇬🇧 Tiếng Anh (Bản gốc PDF) **

> Buổi học này bao gồm **2 tài liệu PDF gốc** từ giáo trình học phần (`textbook/`). Trình duyệt của bạn sẽ hiển thị nội dung từng tài liệu ở bên dưới.

### 📄 Tài liệu PDF 1: Chương 12: Managing Decision Uncertainty

<object data="textbook/Buoi_05A_Chương 12 (Managing Decision Uncertainty).pdf" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_05A_Chương 12 (Managing Decision Uncertainty).pdf" target="_blank">Nhấn vào đây để tải tài liệu PDF 1</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_05A_Chương 12 (Managing Decision Uncertainty).pdf" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 1 (PDF)</a></p>

---

### 📄 Tài liệu PDF 2: Chương 14: New Product Development & Financial Planning

<object data="textbook/Buoi_05B_Chương 14 (New Product Development).pdf" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_05B_Chương 14 (New Product Development).pdf" target="_blank">Nhấn vào đây để tải tài liệu PDF 2</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_05B_Chương 14 (New Product Development).pdf" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 2 (PDF)</a></p>


#### ** 🇻🇳 Tiếng Việt (Bản dịch) **

# 12 QUẢN LÝ SỰ KHÔNG CHẮC CHẮN TRONG RA QUYẾT ĐỊNH BẰNG RANDOM FORESTS (MANAGING DECISION UNCERTAINTY USING RANDOM FORESTS)

12.1 Ra quyết định Dưới sự Không chắc chắn (Decision-Making Under Uncertainty)
12.2 Các đặc điểm của Sự không chắc chắn trong Ra quyết định
12.3 Tình trạng Chậm giao hàng (Backorder) và Hệ quả của nó
12.4 Các Tùy chọn Học máy Hỗ trợ Ra quyết định Dưới sự Không chắc chắn
12.4.1 Các thành phần của Mô hình Cây Quyết định (Decision Tree Model)
12.4.2 Cây Phân loại (Classification Trees)
12.4.3 Ưu điểm, Nhược điểm và Cách Cải thiện Cây Phân loại
12.5 Rừng ngẫu nhiên (Random Forest)
12.6 Dự đoán Tình trạng Chậm giao hàng Bằng Random Forests (Backorder Prediction Using Random Forests)
12.6.1 Nhập và Chọn Dữ liệu
12.6.2 Sự mất cân bằng trong Dữ liệu
12.6.3 Tinh chỉnh Siêu tham số (Hyperparameter Tuning)
12.6.4 Kiểm tra Hiệu suất của Mô hình Random Forest
12.6.4.1 Giá trị Độ chính xác và ROC
12.6.4.2 Ma trận Nhầm lẫn (Confusion Matrix), Độ nhạy (Sensitivity) và Độ đặc hiệu (Specificity)
12.6.4.3 Vai trò của Việc Giảm mẫu (Downsampling)
12.7 Thông tin Kinh doanh và Tóm tắt
12.8 Thực hành bằng R: Dự đoán Tình trạng Chậm giao hàng
12.9 Hiểu rõ Chương học

### MỤC TIÊU HỌC TẬP (LEARNING OBJECTIVES)
1. Hiểu tầm quan trọng của các quyết định kinh doanh hiệu quả, dự báo nhu cầu.
2. Tìm hiểu việc ra quyết định dưới sự không chắc chắn.
3. Áp dụng mô hình cây quyết định để dự đoán các quyết định không chắc chắn.
4. Đánh giá các ưu điểm và hạn chế của mô hình cây.
5. Sử dụng cây quyết định tăng cường (boosted decision trees) để dự đoán quyết định lưu kho.

## 12.1 RA QUYẾT ĐỊNH DƯỚI SỰ KHÔNG CHẮC CHẮN (DECISION-MAKING UNDER UNCERTAINTY)

Ra quyết định dưới sự không chắc chắn đã được nghiên cứu như một chuỗi liên tục các quyết định được đưa ra khi thiếu thông tin hoặc thông tin chỉ có sẵn ở dạng xác suất (ví dụ: khả năng thành công là 80%). Hãy xem xét hai kịch bản sau đây để làm nổi bật sự không chắc chắn vốn có trong việc ra quyết định kinh doanh.

Trong kịch bản đầu tiên, một hãng hàng không lớn, được coi là công ty thống trị tại một trong những sân bay trung tâm của mình, đang phải đối mặt với một thách thức mới: sự gia nhập của một đối thủ cạnh tranh giá rẻ, không rườm rà. Họ phải quyết định xem có nên phản ứng với người mới tham gia (hành động) hay không làm gì cả (không hành động). Cả hai quyết định đều mang những sự không chắc chắn vốn có. Nếu họ quyết định thực hiện một hành động và giảm giá, sẽ có một số kết quả không chắc chắn. Thứ nhất, việc giảm giá có ngăn cản khách hàng đổ xô đến người mới tham gia hay không? Thứ hai, liệu nó thực sự làm tăng thị phần, hay sẽ làm xói mòn lợi nhuận? Thứ ba, liệu việc giảm giá có củng cố hình ảnh thương hiệu của hãng, hay sẽ bị coi là dấu hiệu của sự yếu kém? Thứ tư, các hành động như giảm giá đôi khi có thể dẫn đến cuộc chiến giá cả, điều này có thể gây tổn hại cho toàn bộ ngành. Thay vào đó, hãng hàng không có thể duy trì hiện trạng, nhưng sự không hành động này lại có những điều không chắc chắn riêng. Thứ nhất, có bao nhiêu khách hàng hiện tại có thể bị thuyết phục bởi mức giá thấp hơn hoặc các dịch vụ mới lạ của đối thủ cạnh tranh. Thứ hai, việc giữ nguyên hướng đi có thể được các cổ đông coi là một bước đi tự tin, thể hiện sức mạnh của thương hiệu, hoặc chỉ ra sự không sẵn lòng thích ứng với động lực thị trường đang thay đổi. Thứ ba, bằng cách không điều chỉnh theo động lực thị trường đang thay đổi, có khả năng mất đi các cơ hội mà người mới tham gia có thể khai thác. Thứ tư, liệu doanh nghiệp có thể phục hồi vị thế của mình nếu họ nhận ra quá muộn rằng cần phải có một phản ứng?

Trong kịch bản thứ hai, một nhà bán lẻ hàng điện tử...


thời gian sản phẩm vận chuyển từ nhà sản xuất đến nhà bán lẻ cũng có thể thấp hoặc cao. Biến kết quả là liệu sản phẩm có bị chậm giao hàng (backordered) hay không (có hoặc không). Mục tiêu của chúng ta là đưa ra một mô hình dự đoán đơn giản cho biết liệu một sản phẩm có bị chậm giao hay không dựa trên doanh số dự báo và thời gian vận chuyển. Dữ liệu được trình bày trong Bảng 12.1.

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_05A/Figure 12.1 Bullwhip Effect.jpeg" alt="Figure 12.1 Bullwhip Effect" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Figure 12.1 Bullwhip Effect</div>
</div>






| Doanh số dự báo (Forecasted sales) | Thời gian vận chuyển (Transit time) | Bị chậm giao (Backordered) |
|---|---|---|
| Thấp (Low) | Thấp (Low) | Không (No) |
| Cao (High) | Thấp (Low) | Có (Yes) |
| Thấp (Low) | Thấp (Low) | Không (No) |
| Cao (High) | Cao (High) | Có (Yes) |
| Thấp (Low) | Thấp (Low) | Có (Yes) |
| Cao (High) | Cao (High) | Không (No) |
| Cao (High) | Thấp (Low) | Có (Yes) |
| Thấp (Low) | Cao (High) | Không (No) |
| Cao (High) | Cao (High) | Có (Yes) |

Thách thức đầu tiên trong việc xây dựng cây phân loại (classification tree) là chọn một biến để phân chia nút gốc (root node) đầu tiên. Hãy xem xét Hình 12.3. Các vòng tròn tối đại diện cho khi sản phẩm bị chậm giao và các vòng tròn sáng đại diện cho khi nó không bị chậm giao. Chúng ta thấy rằng biến doanh số dự báo thực hiện phân loại liệu một sản phẩm có bị chậm giao hàng hay không tốt hơn. Trong nhóm dự báo thấp, ba trong số bốn điểm dữ liệu không bị chậm giao và trong nhóm dự báo cao, bốn trong số năm điểm dữ liệu bị chậm giao. Bằng trực giác, các nhóm dự báo cao và thấp có thể tách biệt các điểm dữ liệu bị chậm giao và không bị chậm giao hiệu quả hơn so với các nhóm thời gian vận chuyển cao và thấp. Nhưng đây chỉ là đánh giá trực quan. Làm thế nào chúng ta có thể định lượng xem biến nào là công cụ phân loại (classifier) tốt hơn? 

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_05A/Figure 12.3 Gini Index Calculation.jpeg" alt="Figure 12.3 Gini Index Calculation" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Figure 12.3 Gini Index Calculation</div>
</div>






Độ vẩn đục Gini (Gini impurity) cung cấp cho chúng ta một cách để làm điều này. Mỗi biến dự báo ở mỗi cấp độ là $1 - \text{(tỷ lệ điểm dữ liệu bị chậm giao = "Có")}^2 - \text{(tỷ lệ điểm dữ liệu bị chậm giao = "Không")}^2$. Các giá trị Gini impurity thấp hơn được ưu tiên so với các giá trị cao hơn. Hãy tìm hiểu cách tính chỉ số Gini (Gini index) cho ví dụ mà chúng ta đang làm việc.

Đối với doanh số dự báo như thể hiện trong Hình 12.3, chúng ta có năm điểm dữ liệu có dự báo doanh số cao và bốn điểm dữ liệu có dự báo doanh số thấp. Trong số năm điểm dữ liệu thuộc nhóm dự báo cao, có bốn điểm bị chậm giao và một điểm thì không. Tỷ lệ các mặt hàng bị chậm giao trong nhóm này là $4/5$ và tỷ lệ các mặt hàng không bị chậm giao là $1/5$. Gini impurity cho nhóm này là $1 - (4/5)^2 - (1/5)^2 = 0.32$. Trong số bốn điểm dữ liệu thuộc nhóm dự báo thấp, một mặt hàng bị chậm giao và ba mặt hàng thì không. Tỷ lệ các mặt hàng bị chậm giao trong nhóm này là $1/4$ và tỷ lệ các mặt hàng không bị chậm giao là $3/4$. Gini impurity cho nhóm này là $1 - (1/4)^2 - (3/4)^2 = 0.375$. Bây giờ chúng ta có thể tính toán Gini impurity có trọng số (weighted Gini impurity) cho doanh số dự báo. Vì có chín điểm dữ liệu, Gini impurity có trọng số cho nhóm dự báo cao sẽ là $5/9$, và đối với nhóm dự báo thấp, nó sẽ là $4/9$. Trung bình có trọng số sẽ là $(5/9)0.32 + (4/9)0.375 = 0.34$.

Tương tự, chúng ta có thể tính toán Gini impurity có trọng số cho biến thời gian vận chuyển (được mô tả trong Hình 12.4).

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_05A/Figure 12.4 Gini Impurity for Forecasted Sales and Transit Time.jpeg" alt="Figure 12.4 Gini Impurity for Forecasted Sales and Transit Time" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Figure 12.4 Gini Impurity for Forecasted Sales and Transit Time</div>
</div>






Chúng ta thấy rằng Gini impurity thấp hơn khi sử dụng doanh số dự báo; do đó, nó trở thành biến dùng để chia nút gốc (root node). Cây quyết định kết quả sẽ giống như Hình 12.5.

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_05A/Figure 12.5 Decision Tree Splits.jpeg" alt="Figure 12.5 Decision Tree Splits" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Figure 12.5 Decision Tree Splits</div>
</div>







biến kết quả (outcome variable) và thực tế là mức thiểu số (minority level) (khi sản phẩm bị chậm giao) quan trọng hơn đối với nhiệm vụ dự đoán, chúng ta cần ước tính độ nhạy (sensitivity) cũng như độ đặc hiệu (specificity) của dự đoán này.

### 12.6.4.2 Ma trận Nhầm lẫn (Confusion Matrix), Độ nhạy (Sensitivity) và Độ đặc hiệu (Specificity)
Một phần ôn tập nhanh từ Chương 9 về hồi quy logistic giải thích về ma trận nhầm lẫn. Hãy làm việc với ví dụ sau để hiểu quá trình tính toán độ nhạy và độ đặc hiệu.

| | Dự đoán (Prediction) | |
|---|---|---|
| **Sự thật (Truth)** | **Không (No)** | **Có (Yes)** |
| **Không (No)** | i | ii |
| **Có (Yes)** | iii | iv |

Dựa vào ma trận nhầm lẫn trong Bảng 12.4, độ nhạy và độ đặc hiệu như sau:
- Độ nhạy (Sensitivity) = $\frac{iv}{iii + iv}$
- Độ đặc hiệu (Specificity) = $\frac{i}{i + ii}$

Bằng trực giác, độ nhạy là tỷ lệ dương tính thật (true positive rate) và thể hiện khả năng mô hình của chúng ta phân loại chính xác các sản phẩm bị chậm giao. Độ đặc hiệu là tỷ lệ âm tính thật (true negative rate) và đại diện cho khả năng mô hình của chúng ta phân loại chính xác các sản phẩm không bị chậm giao. Nếu độ nhạy của mô hình thấp, thì chúng ta sẽ không thể xác định trước các sản phẩm có khả năng bị chậm giao. Mặt khác, nếu độ đặc hiệu thấp, chúng ta sẽ kết thúc bằng việc đặt hàng quá mức (overordering) những sản phẩm ít có khả năng bị chậm giao. Đối với mô hình của chúng ta, độ nhạy là $\frac{83}{83+16} = 0.838$, và độ đặc hiệu là $\frac{329}{329+73} = 0.818$.

### 12.6.4.3 Vai trò của Việc Giảm mẫu (Downsampling)
Trong phân tích trước đó, chúng ta đã sử dụng kỹ thuật giảm mẫu (downsampling) để xử lý vấn đề mất cân bằng lớp (class imbalance). Phương pháp giảm mẫu này lấy mẫu các hàng từ dữ liệu huấn luyện theo cách mà mức đa số (tức là khi sản phẩm không bị chậm giao) được lấy mẫu ít hơn. Nhưng hãy kiểm tra xem kết quả sẽ thay đổi như thế nào nếu chúng ta không giảm mẫu. Các kết quả khi không sử dụng giảm mẫu được trình bày trong Bảng 12.5, cùng với ma trận nhầm lẫn trong Bảng 12.6.

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_05A/Figure 12.6 Data Imbalance.jpeg" alt="Figure 12.6 Data Imbalance" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Figure 12.6 Data Imbalance</div>
</div>






```R
.metric    .estimator .estimate .config
accuracy   binary     0.8602794 Preprocessor1_Model1
roc_auc    binary     0.9038896 Preprocessor1_Model1
```

| | Không (No) | Có (Yes) |
|---|---|---|
| **Không (No)** | 393 | 61 |
| **Có (Yes)** | 9 | 38 |

Chúng ta nhận thấy rằng cả độ chính xác (accuracy) và giá trị AUC đều cao và có thể so sánh được với phân tích trước đó khi chúng ta thực hiện giảm mẫu. Tuy nhiên, khi ước tính độ nhạy và độ đặc hiệu, chúng ta quan sát thấy một bức tranh rất khác. Nếu không giảm mẫu, độ nhạy là $\frac{38}{38+61} = 0.384$, và độ đặc hiệu là $\frac{393}{393+9} = 0.978$. Có sự sụt giảm lớn về độ nhạy từ 0.838 xuống 0.384 và sự gia tăng về độ đặc hiệu từ 0.818 lên 0.978. Điều này cho thấy trong trường hợp không có giảm mẫu, mô hình của chúng ta không thể xác định các sản phẩm cuối cùng sẽ bị chậm giao. Giảm mẫu giải quyết điểm yếu này và cái giá phải trả là sự sụt giảm về độ đặc hiệu. Giảm mẫu đảm bảo rằng không làm tổn hại đến giá trị AUC và độ chính xác, chúng ta có thể làm cho độ nhạy và độ đặc hiệu rất tương đồng nhau. Lưu ý rằng giảm mẫu chỉ là một trong nhiều phương pháp lấy mẫu con (subsampling) có sẵn trong các gói phân tích.

## 12.7 THÔNG TIN KINH DOANH VÀ TÓM TẮT (BUSINESS INSIGHTS AND SUMMARY)
Trong chương này, chúng ta đã xem xét tình trạng chậm giao hàng (backorders), một chủ đề lớn trong chuỗi cung ứng có thể gây ra nhiều vấn đề như sự không hài lòng của khách hàng.


mãn của khách hàng, doanh số bị mất và giảm uy tín thương hiệu. Chúng ta đã thảo luận về cách phân tích dữ liệu và các thuật toán học máy, đặc biệt là Random Forest, có thể giúp các tổ chức chủ động dự đoán và quản lý sự không chắc chắn này. Chúng ta đã khám phá các khái niệm như ma trận nhầm lẫn (confusion matrix), độ nhạy (sensitivity), độ đặc hiệu (specificity) và tầm quan trọng của việc xử lý dữ liệu mất cân bằng thông qua các kỹ thuật như giảm mẫu (downsampling).

## 12.8 THỰC HÀNH BẰNG R: DỰ ĐOÁN TÌNH TRẠNG CHẬM GIAO HÀNG
(Phần này bao gồm các đoạn mã R đã được trình bày trong các phần trước để dự đoán tình trạng chậm giao hàng bằng Random Forest, vui lòng xem mã nguồn trong sách).

## 12.9 HIỂU RÕ CHƯƠNG HỌC

1. Tại sao tính chính xác (accuracy) không phải là số đo (metric) duy nhất hoặc tốt nhất để đánh giá mô hình học máy khi dữ liệu bị mất cân bằng (imbalanced)? Nêu ví dụ từ bài toán dự đoán chậm giao hàng.
2. Hãy xem xét một nhiệm vụ lập mô hình dự đoán liên quan đến bộ phân loại Random Forest. Giải thích vai trò và tầm quan trọng của việc sử dụng kiểm chứng chéo k-fold (k-fold CV) trong quá trình đánh giá mô hình.
3. Các quyết định được đưa ra khi thiếu một số thông tin được gọi là gì?
a. Quyết định rủi ro (Risky decisions)
b. Quyết định chắc chắn (Decisions under certainty)
c. Không thể đưa ra quyết định (No decision can be made)
d. Quyết định nhị phân (Binary decisions)
4. Trong các tùy chọn được cung cấp, đâu là đặc điểm của các quyết định được đưa ra trong sự không chắc chắn? (Chọn tất cả những phương án đúng.)
a. Cân nhắc rủi ro của việc ra quyết định với lợi ích của quyết định đó
b. Cân nhắc rủi ro so với chi phí của việc ra quyết định
c. Cân nhắc lợi ích của quyết định so với lợi nhuận từ bán hàng
d. Đánh giá các tùy chọn hiện có so với các tùy chọn mới
5. Câu nào sau đây đúng về hiệu ứng cái roi da (bullwhip effect)?
a. Nó xảy ra khi một thay đổi nhỏ về nhu cầu bị đánh giá quá cao, dẫn đến dư thừa nguồn cung.
b. Nó xảy ra khi một thay đổi nhỏ về nguồn cung bị đánh giá thấp.
c. Nó xảy ra khi cung cầu gặp nhau.
d. Nó xảy ra khi lạm phát khiến nhu cầu giảm.
6. Đối với cây quyết định, số đo (metric) nào được sử dụng để tìm biến nào là công cụ phân loại (classifier) tốt hơn?
a. Độ vẩn đục Gini (Gini impurity)
b. Hệ số xác định (Coefficient of determination)
c. Hệ số lạm phát phương sai (Variance inflation factor - VIF)
d. Hệ số tương quan đồng thế hệ (Cophenetic correlation coefficient)
7. Câu nào sau đây về bagging là sai?
a. Bagging là kết hợp bằng cách tái lấy mẫu (bootstrap aggregation).
b. Bagging bao gồm lấy mẫu có hoàn lại.
c. Bagging bao gồm lấy mẫu không hoàn lại.
d. Bagging giúp xây dựng các cây đa dạng.
8. Câu nào sau đây về việc giảm mẫu (downsampling) là sai?
a. Nó giải quyết vấn đề mất cân bằng dữ liệu.
b. Nó cho phép mô hình tìm hiểu tốt hơn các tính năng của lớp thiểu số.
c. Nó làm giảm nghiêm trọng độ chính xác của mô hình.
d. Nó làm giảm một chút độ đặc hiệu nhưng cải thiện đáng kể độ nhạy.
9. Giả sử chúng ta đang sử dụng cây quyết định để tìm ra (các) biến dự đoán nào có thể phân loại tốt hơn biến kết quả: liệu khách hàng có mua sản phẩm hay không. Cho các giá trị Gini impurity sau đối với ba biến dự đoán—Predictor A = 0.55, Predictor B = 0.24, và Predictor C = 0.76—lựa chọn nào sau đây sẽ được coi là bộ phân loại tối ưu cho quyết định mua/không mua?
a. Predictor A
b. Predictor B
c. Predictor C
d. Cả Predictor A và Predictor C

### CHÚ THÍCH (ENDNOTES)
(Các tài liệu tham khảo trong sách, ví dụ: bài viết của Heath và Amos Tversky về sự không chắc chắn, báo cáo kỹ thuật của IBM, các gói R như tidymodels, dplyr, ranger, themis, v.v.)

### MÔ TẢ CÁC HÌNH ẢNH (Descriptions of Images and Figures)
> 📸 **Hình ảnh**: Figure mô tả sự gia tăng nhu cầu khách hàng, nhà bán lẻ đặt hàng quá nhiều, sản xuất quá mức và nguồn cung (Bullwhip effect)
> 📸 **Hình ảnh**: Figure mô tả Doanh số Dự báo (Forecasted Sales) với các node Cao/Thấp
> 📸 **Hình ảnh**: Figure mô tả tính toán Chỉ số Gini
> 📸 **Hình ảnh**: Figure mô tả sơ đồ khối của Cây phân loại với Doanh số Dự báo và Thời gian vận chuyển


# 14 PHÁT TRIỂN SẢN PHẨM MỚI VỚI THỬ NGHIỆM A/B (NEW PRODUCT DEVELOPMENT WITH A/B TESTING)

14.1 Những đổi mới trên Thị trường (Innovations in the Marketplace)
14.2 Các Giai đoạn Phát triển Sản phẩm Mới
14.2.1 Hình thành Ý tưởng (Idea Generation)
14.2.2 Sàng lọc Ý tưởng (Idea Screening)
14.2.3 Phát triển và Thử nghiệm Khái niệm (Concept Development and Testing)
14.2.4 Phân tích Kinh doanh (Business Analysis)
14.2.5 Thiết kế và Phát triển Sản phẩm
14.2.6 Thử nghiệm Thị trường (Test Marketing)
14.2.7 Thương mại hóa (Commercialization)
14.2.8 Đánh giá và Kiểm soát (Evaluation and Control)
14.3 Tầm quan trọng của Thử nghiệm và Nghiên cứu Thị trường
14.3.1 Dành cho Đánh giá Thiết kế
14.3.2 Dành cho Tương tác Khách hàng trong Thế giới Đa kênh (Omnichannel)
14.3.3 Dành cho Tích hợp Phản hồi và Trải nghiệm Khách hàng
14.4 Sự phức tạp của Thử nghiệm A/B (The Intricacies of A/B Testing)
14.5 Sử dụng Thử nghiệm A/B để Thử nghiệm Nguyên mẫu Trò chơi (Gaming Prototypes)
14.5.1 Thiết kế Thử nghiệm (Experimental Design)
14.5.2 Phân tích Dữ liệu và Trình bày Kết quả
14.5.3 Kiểm định F (F Test)
14.5.4 Kiểm định Sự khác biệt Thống kê
14.6 Sử dụng Thử nghiệm A/B trong Phát triển Sản phẩm Mới
14.6.1 Thông tin chi tiết (Insights) Rút ra Từ Thử nghiệm A/B
14.7 Thực hành bằng R: Thử nghiệm A/B
14.8 Hiểu rõ Chương học

### MỤC TIÊU HỌC TẬP (LEARNING OBJECTIVES)
1. Giới thiệu sản phẩm mới trên thị trường.
2. Ghi nhớ các bước trong quy trình phát triển sản phẩm mới.
3. Hỗ trợ phát triển sản phẩm mới bằng học máy (machine learning).
4. Sử dụng thử nghiệm A/B để phát triển sản phẩm mới.
5. Giới thiệu một sản phẩm kỹ thuật số.

## 14.1 NHỮNG ĐỔI MỚI TRÊN THỊ TRƯỜNG (INNOVATIONS IN THE MARKETPLACE)

Chase đã giới thiệu thẻ tín dụng mới của mình, Chase Sapphire Reserve, vào năm 2016, cung cấp cho người dùng 100.000 điểm thưởng đăng ký cho năm đầu tiên và đưa Chase vượt mục tiêu doanh số hàng năm trong vài tuần đầu tiên. Sự nhiệt tình của những người thuộc thế hệ millennial khi sử dụng thẻ do số điểm miễn phí là một yếu tố chính tạo nên thành công của nó. Tuy nhiên, Chase cần nhìn xa hơn năm đầu tiên giới thiệu sản phẩm để đánh giá thẻ sẽ hoạt động như thế nào trong những năm tiếp theo sau khi hết ưu đãi khuyến mãi và phí hàng năm bắt đầu. Mặc dù phí hàng năm cao là $550, nó được coi là thẻ du lịch tốt nhất nhờ những đặc quyền mà nó mang lại—bao gồm cả quyền ra vào phòng chờ sân bay và tín dụng phí đăng ký cho Global Entry và TSA PreCheck. Đây là một ví dụ về việc ra mắt sản phẩm được thiết kế và triển khai tốt, và các chiến lược phù hợp đang giúp Chase duy trì thành công của mình.

Nintendo phát hành Switch vào năm 2017, bán được 2,74 triệu máy trong tháng đầu tiên. Thiết kế của nó cho phép chơi trò chơi cầm tay và bảng điều khiển (console) thu hút được lượng lớn người dùng. Các tựa game ra mắt, chẳng hạn như *The Legend of Zelda: Breath of the Wild*, đã thu hút sự chú ý của mọi người. Switch có giá cả cạnh tranh, và các tính năng như chơi trò chơi nhiều người chơi cục bộ và tính di động đã giúp nó đạt hiệu suất thành công trên thị trường.

Khái niệm về một sản phẩm đã phát triển trong thời đại kỹ thuật số. Những tiến bộ công nghệ về trí tuệ nhân tạo, điện toán đám mây, in 3D và mạng cảm biến không dây giờ đây đã giúp cho việc chế tạo các sản phẩm không có sự hiện diện vật lý nhưng tồn tại hoàn toàn trên web trở nên khả thi, chẳng hạn như ứng dụng theo dõi sức khỏe trên điện thoại thông minh và ứng dụng nhận dạng khuôn mặt để phát hiện gian lận; thậm chí trong ô tô, phần lớn việc lái xe được điều khiển bằng thuật toán, chẳng hạn như với xe tự lái...


chọn? Tự chọn xảy ra nếu những người tham gia được phép chọn nhóm (hoặc phương pháp điều trị) mà họ muốn tham gia. Ví dụ, nếu chúng ta thiết kế một thử nghiệm A/B cho các trò chơi điện tử để tìm ra màu sắc nào của giao diện trực quan sống động hơn (ví dụ: xanh dương so với xanh lục) và để người tham gia chọn chơi bằng màu sắc họ muốn, thì thiết kế thử nghiệm không được ngẫu nhiên hóa vì chúng ta đang cho phép người tham gia tự chọn nhóm thử nghiệm của họ dựa trên sở thích về màu sắc.

## 14.5 SỬ DỤNG THỬ NGHIỆM A/B ĐỂ THỬ NGHIỆM NGUYÊN MẪU TRÒ CHƠI
Trong chương này, hãy sử dụng ví dụ về một công ty trò chơi điện tử. GameV đang làm việc trên một ý tưởng trò chơi mới mà các nhà thiết kế của họ tin rằng sẽ sống động và hấp dẫn hơn các trò chơi khác mà GameV hiện đã phát triển. Tuy nhiên, trước khi ra mắt trò chơi, các nhà thiết kế của GameV đã tạo ra một số nguyên mẫu (prototypes) của trò chơi để họ có thể tung ra phiên bản có khả năng giữ chân nhiều người chơi nhất. Từ dữ liệu trước đây trong ngành công nghiệp trò chơi, họ biết rằng mọi điểm tương tác (engagement) trong trò chơi đều dẫn đến việc người chơi sẽ quay lại. Ví dụ, nhiều người chơi không quay lại sau phiên đầu tiên do quá trình cài đặt bị lỗi hoặc do các tính năng trò chơi kém hấp dẫn. Do đó, GameV muốn sử dụng thử nghiệm A/B để đánh giá các tính năng cụ thể. Trò chơi cho phép người chơi kiếm thêm mạng (extra life) bằng cách thực hiện một số nhiệm vụ. GameV đã xác định ba mức độ khó: 25, 35 và 45. Họ muốn tìm xem mức độ khó nào dẫn đến sự tương tác (engagement) lớn hơn. Có khả năng nếu người chơi kiếm được một mạng sống bằng cách thực hiện một nhiệm vụ khó khăn, điều đó có thể dẫn đến việc họ cảm thấy gắn bó hơn. Ngoài ra, cũng có khả năng việc kiếm được một mạng sống bằng một nhiệm vụ khó khăn hơn sẽ khiến người chơi bỏ cuộc. Do đó, GameV muốn tìm xem mức độ khó nào thu hút nhiều người chơi hơn trong môi trường trò chơi này. Có thể nghĩ ba mức độ khó là thấp (low), trung bình (medium) và cao (high).

GameV tin rằng một số đo kết quả (outcome metric) tốt để tìm ra mức độ thành công của nguyên mẫu là thời gian người chơi dành để chơi. Vì trò chơi là một nguyên mẫu, người chơi chưa bao giờ chơi nó trước đây và thời gian họ chơi trò chơi sẽ giúp GameV xác định nguyên mẫu nào mang lại sự tương tác và sự nhập tâm (immersion) lớn nhất. Biến kết quả (outcome variable - không giống như trong Chương 7) có bản chất là liên tục (continuous). Do đó, chúng ta sẽ sử dụng kiểm định F (F test) để tìm ra mức độ khó nào dẫn đến mức độ nhập tâm cao nhất.

### 14.5.1 Thiết kế Thử nghiệm (Experimental Design)
GameV đã phát triển ba nguyên mẫu theo cách mà mỗi nguyên mẫu được thiết kế với một trong ba mức độ khó. Mỗi nguyên mẫu cung cấp các tính năng trò chơi độc đáo tương ứng với mức độ khó cụ thể của nó, mang đến cho người chơi nhiều trải nghiệm khác nhau. Trong thiết kế thử nghiệm, mức độ khó là yếu tố duy nhất khác biệt giữa ba nguyên mẫu, với các mức cụ thể được đặt ở 25, 35 và 45. Mọi tính năng khác của trò chơi đều giữ nguyên; chỉ các tính năng liên quan đến mức độ khó là khác nhau. Hơn nữa, việc phân bổ người chơi cho một trong ba nguyên mẫu là hoàn toàn ngẫu nhiên. Bằng cách thiết kế ngẫu nhiên hóa (randomization) vào quá trình thiết lập, GameV đảm bảo rằng mọi biến phụ (chẳng hạn như sở thích của người chơi, mức độ quen thuộc của họ với các trò chơi trước đây hoặc thời gian trong ngày) đều có cùng cơ hội tác động đến cả ba nguyên mẫu, có nghĩa là bất kỳ sự khác biệt nào về thời gian chơi giữa các nguyên mẫu đều có thể được gán một cách tự tin cho mức độ khó.


biến kết quả (outcome variable). Ví dụ, nếu chúng ta có một thiết kế thử nghiệm với ba yếu tố (factors) và mỗi yếu tố có hai cấp độ (levels), thì phương trình mô hình sẽ bao gồm ba hiệu ứng chính, ba tương tác hai yếu tố và một tương tác ba yếu tố, chỉ ra rằng thiết kế thử nghiệm nên bao gồm 2 * 2 * 2 = 8 nhóm. Giả sử cỡ mẫu là 50 người tham gia mỗi nhóm, chúng ta sẽ cần một mẫu gồm 400 người tham gia.

## 14.7 THỰC HÀNH BẰNG R: THỬ NGHIỆM A/B
(Phần này bao gồm các đoạn mã R đã được trình bày để kiểm tra tính chuẩn xác (Shapiro-Wilk), tính đồng nhất phương sai (Levene's test), Welch's ANOVA, và bài kiểm tra hậu hoc Games-Howell, vui lòng xem mã nguồn trong sách).

## 14.8 HIỂU RÕ CHƯƠNG HỌC

1. Sự khác biệt giữa kiểm tra nhân quả (causal testing) và kiểm tra tương quan (correlational testing) là gì? Thử nghiệm A/B là nhân quả hay tương quan?
2. Sự khác biệt giữa giả thuyết không (null hypothesis) và giả thuyết thay thế (alternate hypothesis) trong một thử nghiệm A/B là gì?
3. Mục đích chính của một thử nghiệm A/B là gì?
a. Để so sánh hai thiết kế quảng cáo khác nhau
b. Để xác định hiệu quả của một sự can thiệp giữa các nhóm
c. Để kiểm tra hiệu quả của một loại thuốc mới
d. Để tìm mối tương quan giữa các biến
4. Kiểm định thống kê nào bạn sẽ sử dụng để so sánh giá trị trung bình của ba hoặc nhiều nhóm?
a. Kiểm định t (t test)
b. Kiểm định F (F test)
c. Kiểm định chi bình phương (chi-square test)
d. Tương quan Pearson (Pearson correlation)
5. Giả thuyết không (null hypothesis) trong một thử nghiệm A/B là gì?
a. Có sự khác biệt đáng kể giữa các nhóm.
b. Không có sự khác biệt đáng kể giữa các nhóm.
c. Sự can thiệp gây ra sự khác biệt quan sát được.
d. Sự khác biệt được quan sát là do ngẫu nhiên.
6. Ưu điểm chính của việc sử dụng Welch's ANOVA so với kiểm định F tiêu chuẩn (ANOVA) là gì?
a. Nó mạnh hơn khi các phương sai bằng nhau.
b. Nó ít nhạy cảm hơn với các phương sai không bằng nhau.
c. Nó có tỷ lệ lỗi Loại I cao hơn.
d. Nó yêu cầu ít giả định hơn.
7. Khi nào bạn nên sử dụng kiểm tra hậu định (post hoc test) sau kiểm định F (ANOVA)?
a. Khi giả thuyết không bị bác bỏ
b. Khi giả thuyết không không bị bác bỏ
c. Luôn luôn sau kiểm định F
d. Chỉ khi kích thước mẫu không bằng nhau
8. Trong tình huống nào bạn sẽ chọn sử dụng Welch's ANOVA thay vì kiểm định F tiêu chuẩn?
a. Khi dữ liệu được phân phối chuẩn
b. Khi các phương sai trong mỗi nhóm bằng nhau
c. Khi phương sai trong mỗi nhóm không bằng nhau
d. Khi các nhóm bị phụ thuộc

### CHÚ THÍCH (ENDNOTES)
(Các tài liệu tham khảo trong sách, ví dụ: bài viết đánh giá thẻ Chase Sapphire Reserve, bài báo về Welch's t-Test, các gói R như rstatix, dplyr, ggplot2, v.v.)

### MÔ TẢ CÁC HÌNH ẢNH (Descriptions of Images and Figures)
> 📸 **Hình ảnh**: Figure mô tả sơ đồ 8 bước trong Quy trình phát triển sản phẩm mới
> 📸 **Hình ảnh**: Figure mô tả đồ thị hộp (boxplot) thời gian chơi theo từng điều kiện nguyên mẫu




#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slideAIAcc/Slide_AIAcc_Day05.pdf" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day05.pdf" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day05.pdf" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

<!-- tabs:end -->
