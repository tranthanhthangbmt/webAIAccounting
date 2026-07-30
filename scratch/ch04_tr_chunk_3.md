**MỤC TIÊU HỌC TẬP 3 (LEARNING OBJECTIVE 3)**
**Giải thích cách một chiến lược phân tích được thiết kế.**

Hãy xem xét hai câu hỏi sau khi thiết kế một chiến lược phân tích dữ liệu:
1. Chiến lược phân tích đã chọn có thể trả lời các câu hỏi mục tiêu cụ thể không?
2. Thang đo lường của dữ liệu có phù hợp với chiến lược phân tích đã chọn không?

Ở phần trước trong khóa học này, bạn đã học được có bốn loại mục tiêu phân tích dữ liệu: mô tả (descriptive), chẩn đoán (diagnostic), dự đoán (predictive), và đề xuất (prescriptive). Mỗi loại đặt ra những câu hỏi khác nhau về dữ liệu. Chúng ta thực hiện các phân tích để trả lời những câu hỏi đó. Phân tích cụ thể có thể được thực hiện trên dữ liệu bị ảnh hưởng bởi thang đo lường của dữ liệu. Tiếp theo, chúng ta tóm tắt những điều cần xem xét khi thiết kế các phân tích cho các dự án có mục tiêu mô tả và chẩn đoán.

### Thiết kế Các Phân tích để Mô tả và Chẩn đoán (Designing Analyses to Describe and Diagnose)

Bởi vì việc hiểu các hiện tượng được thu thập bởi dữ liệu là điều cần thiết, nhiều dự án phân tích dữ liệu bắt đầu bằng các phân tích mô tả. Phân tích chẩn đoán bao gồm nhiều phân tích giống như phân tích mô tả, nhưng trọng tâm là giải thích *tại sao* điều gì đó lại xảy ra. Vì nhiều loại phân tích có thể vừa là mô tả vừa là chẩn đoán, nên việc thảo luận hai chiến lược phân tích này cùng nhau là hợp lý.

Loại phân tích mô tả và chẩn đoán cụ thể được sử dụng phụ thuộc vào thang đo lường của dữ liệu. Ví dụ, việc tính toán quan sát trung vị (median observation) trong dữ liệu yêu cầu sử dụng các thước đo khoảng (interval) hoặc tỷ lệ (ratio). Hình minh họa 4.14 cho thấy một số chiến lược phân tích cho các mục tiêu mô tả và chẩn đoán (dấu tích (checkmarks) biểu thị các phân tích phù hợp, và dấu X biểu thị các phân tích không phù hợp cho thang đo lường đó).

![ILLUSTRATION 4.14](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.14.png)

![ILLUSTRATION 4.14B](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.14B.png)

**Các Chiến lược Phân tích Mô tả (Descriptive Analysis Strategies)**
Hãy nhớ lại rằng dữ liệu kế toán là dữ liệu định giá và giao dịch kinh tế lịch sử (historic economic transaction and valuation data). Các kế toán viên, nhà quản lý kinh doanh, và các cơ quan quản lý đều muốn biết thêm về những gì đã xảy ra và liệu dữ liệu báo hiệu tin tốt hay tin đáng lo ngại, vì vậy phân tích mô tả là chiến lược phân tích phổ biến nhất sử dụng dữ liệu kế toán. Nó hữu ích cho việc đánh giá hiệu suất của chiến lược vì nó cung cấp nhiều ý nghĩa và thông tin kinh doanh (business intelligence) hơn là chỉ nhìn vào, ví dụ, các tổng số được báo cáo trên báo cáo tài chính của một năm.

Hãy xem qua một ví dụ sử dụng tập dữ liệu các khoản phải thu của WeMakeIt Inc. để minh họa sức mạnh giải thích của phân tích mô tả ngay cả khi sử dụng dữ liệu định danh (categorical data). Hãy nhớ lại rằng mục tiêu của phân tích này là để tự tin hơn vào các tỷ lệ phần trăm được sử dụng cho ước tính nợ khó đòi. Kết quả phân tích mô tả ban đầu cho thấy sự gia tăng lớn về số lượng khách hàng có hóa đơn chưa thanh toán vào cuối năm 2025 so với cuối năm 2024. Phân tích này đã được thiết kế để trả lời hai câu hỏi mô tả:
- Câu hỏi mục tiêu 1: Có bao nhiêu khách hàng có hóa đơn chưa thanh toán vào cuối năm 2024?
- Câu hỏi mục tiêu 2: Có bao nhiêu khách hàng có hóa đơn chưa thanh toán vào cuối năm 2025?

Một chiến lược dữ liệu và một chiến lược phân tích đã được phát triển:
- Chiến lược dữ liệu: Sử dụng biến định danh (categorical variable) là `CustomerNumber` để xác định các khách hàng có số dư chưa thanh toán.
- Chiến lược phân tích: Đếm và so sánh tần suất (frequency) của các mã khách hàng duy nhất có hóa đơn chưa thanh toán vào cuối năm 2024, và sau đó lặp lại phân tích cho cuối năm 2025. Lưu ý rằng cả đếm (count) và tần suất đều là các phân tích có thể được thực hiện trên dữ liệu định danh.

![ILLUSTRATION 4.15](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.15.png)

Kết quả chỉ ra rằng vào năm 2024 có 37 mã khách hàng duy nhất có hóa đơn chưa thanh toán, và vào năm 2025 có 52 mã khách hàng duy nhất có hóa đơn chưa thanh toán. Tiếp theo, chúng ta thảo luận về các chiến lược phân tích chẩn đoán.

**ÁP DỤNG TƯ DUY PHẢN BIỆN 4.5 (APPLYING CRITICAL THINKING 4.5): Hãy Cẩn thận Khi Giải thích Kết quả Ban đầu**
Ban đầu, bạn có thể kết luận rằng các khoản phải thu vào năm 2025 có khả năng rủi ro thu hồi cao hơn đơn giản là vì có nhiều khách hàng có hóa đơn chưa thanh toán trong năm 2025 hơn năm 2024. Tuy nhiên, đánh giá ban đầu này có thể bị ảnh hưởng bởi các giả định và định kiến (biases) nội bộ (Rủi ro - Risks):
- Sự gia tăng số lượng khách hàng có số dư chưa thanh toán trong năm 2025 có thể không phải là một kết quả tiêu cực, vì công ty đã phát triển và có thêm khách hàng mới vào năm 2025.
- Những kết quả này có thể thúc đẩy bạn đánh giá các giải thích thay thế và thực hiện các phân tích mới, chẳng hạn như xác định xem số lượng khách hàng năm 2025 có hóa đơn chưa thanh toán vào cuối năm có nhiều hóa đơn nợ trong năm 2025 hơn năm 2024 hay không, hoặc giá trị số dư chưa thanh toán của họ có cao hơn vào năm 2025 hay không, điều này có thể báo hiệu mối lo ngại về thanh khoản tiền mặt (cash liquidity). Kết quả này có liên quan chặt chẽ hơn đến rủi ro không thể thu hồi các khoản phải thu của công ty chúng ta (Các phương án thay thế - Alternatives).

**Các Chiến lược Phân tích Chẩn đoán (Diagnostic Analysis Strategies)**
Các chiến lược phân tích chẩn đoán có thể được so sánh với công việc thám tử. Các kế toán viên có thể sử dụng các chiến lược phân tích này để xác định và khám phá những nguyên nhân có khả năng nhất của các hiện tượng kế toán. Mặc dù cả hai chiến lược phân tích mô tả và chẩn đoán đều là các kỹ thuật mô tả, các chiến lược phân tích chẩn đoán cũng xác định những yếu tố nào đã gây ra doanh thu bán hàng thấp hơn hoặc chi phí cao hơn, chẳng hạn. Các chiến lược chẩn đoán luôn yêu cầu áp dụng các kỹ năng tư duy phản biện.

Các bên liên quan dựa vào các kế toán viên trong các lĩnh vực thực hành kế toán để chẩn đoán xem điều gì đang xảy ra và giải thích, thường bằng các thuật ngữ phi kế toán, lý do tại sao nó lại xảy ra. Ví dụ, các kế toán viên hệ thống (systems accountants) thường sử dụng dữ liệu phân tán lỗi (error dispersion data) để xác định các vấn đề về hiệu suất hệ thống hoặc dữ liệu hoạt động bất thường có thể chỉ ra sự truy cập trái phép của các bên.

Hãy sử dụng lại tập dữ liệu các khoản phải thu của WeMakeIt Inc., lần này là để minh họa phân tích chẩn đoán:
- Câu hỏi mục tiêu mới: Các khách hàng mua chịu quay lại (returning credit customers) có nhiều hóa đơn chưa thanh toán vào cuối năm 2025 hơn số hóa đơn chưa thanh toán của họ vào cuối năm 2024 không?
- Chiến lược dữ liệu: Một lần nữa, sử dụng tập dữ liệu cho các hóa đơn mở (open invoices) của các khoản phải thu cuối năm 2024 và 2025.
- Chiến lược phân tích: Nhóm dữ liệu theo `CustomerNumber` cho câu hỏi này.

Hình minh họa 4.15 (phần trước) đã báo cáo một phần kết quả của phân tích này.
Để trả lời câu hỏi này, chúng ta có thể chọn tạo một biến thứ bậc (ordinal variable) được tính toán mới (hãy nhớ rằng biến (variable) là một mục dữ liệu sẽ được sử dụng trong phân tích). Biến này sẽ nhóm các khách hàng mua chịu vào các khoảng tăng dần dựa trên số lượng hóa đơn mà họ chưa thanh toán vào cuối năm. Có một số lợi ích đối với chiến lược này:
- Việc thay đổi một biến liên tục (continuous variable) thành các khoảng thứ bậc (ordinal ranges) mang lại các phân nhóm có ý nghĩa hơn thay vì chỉ đếm số lượng hóa đơn chưa thanh toán trên mỗi khách hàng.
- Biến thứ bậc mới cho phép hiểu rõ hơn về kết quả tổng thể của tổng số hóa đơn chưa thanh toán.

Hãy tạo ba mức độ cho các hóa đơn chưa thanh toán: khoảng 1-3 hóa đơn, 4-6 hóa đơn, và 7-9 hóa đơn làm các mức độ biến thứ bậc mới. Hình minh họa 4.16 cung cấp hình ảnh trực quan về kết quả của chiến lược phân tích này. (Data: Mục How To 4.2 mô tả cách tạo lại hình ảnh trực quan này bằng một công cụ khác.)

![ILLUSTRATION 4.16](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.16.png)

Kết quả của phân tích thứ hai này cho thấy số lượng khách hàng có 4-6 và 7-9 hóa đơn chưa thanh toán đã giảm vào năm 2025 so với năm 2024. Tuy nhiên, có gần gấp đôi số khách hàng có 1-3 hóa đơn quá hạn vào năm 2025 so với năm 2024. Những kết quả này là tin tức hỗn hợp cho những lo ngại về rủi ro khả năng thu hồi các khoản phải thu trong tương lai.

Phát hiện bất ngờ này là một lời nhắc nhở tốt về tầm quan trọng của tư duy phản biện và sự cân nhắc kỹ lưỡng về kết quả phân tích ban đầu. Suy nghĩ phản biện khi diễn giải các kết quả phân tích liên quan đến việc đánh giá cả các chiến lược phân tích đã thực hiện và chưa thực hiện. Đặt câu hỏi hoài nghi (skeptically) về các chiến lược phân tích dữ liệu có thể mang lại những hiểu biết có giá trị, như phân tích cuối cùng này đã làm.

**ÁP DỤNG TƯ DUY PHẢN BIỆN 4.6 (APPLYING CRITICAL THINKING 4.6): Kiểm soát cho Các Rủi ro đối với Các Chiến lược Phân tích**
Tùy thuộc vào mục tiêu của dự án, các chiến lược phân tích có thể liên quan đến một sự kết hợp đa dạng các biến với các nguồn và thang đo lường khác nhau. Việc chỉ đơn giản là thêm các biến và sự phức tạp vào các lựa chọn phân tích mà không có sự biện minh (justification) có thể dẫn đến tình trạng quá tải thông tin, làm giảm khả năng phán đoán của bạn. Ví dụ, dự báo bán hàng có thể liên quan đến ít biến số hơn trong các ngành như nông nghiệp, vì nhu cầu thực phẩm ổn định hơn so với hàng không, vì du lịch mang tính tùy ý (discretionary) hơn.
Các thói quen giảm thiểu rủi ro chuyên nghiệp bao gồm (Rủi ro - Risks):
- Giữ cho việc phân tích đơn giản nhất có thể bằng cách đưa vào ít biến nhất nhưng lại phù hợp nhất.
- Tài liệu hóa từng bước, đặc biệt là các lợi ích và hạn chế của mỗi lựa chọn khi bạn phát triển, đánh giá và chọn một chiến lược phân tích (Các phương án thay thế - Alternatives).

Quy trình phân tích các khoản phải thu của WeMakeIt, Inc., dù là mô tả hay chẩn đoán, đều liên quan đến một cách tiếp cận có thể được sử dụng cho hầu hết các chiến lược phân tích trong kế toán:
- Bắt đầu với một mục tiêu rõ ràng và các câu hỏi cụ thể cần được trả lời.
- Phát triển các phương án dữ liệu thay thế, đánh giá từng phương án dựa trên các yếu tố liên quan đến mục tiêu, và chọn chiến lược dữ liệu tốt nhất. Lọc tập dữ liệu xuống các biến và khoảng quan tâm cần thiết cho mục tiêu.
- Các chiến lược phân tích tốt nhất thường tạo ra các biến mới được tính toán trong cùng một hàng (within-row) cần thiết cho việc phân tích. Các biến được tính toán mới này có thể là các phân nhóm định danh, xếp hạng thứ bậc, số đo khoảng và biến tỷ lệ. Hãy nhớ rằng các phân nhóm phù hợp có thể giúp việc giải thích kết quả dễ dàng hơn.
- Tính toán bất kỳ số đo phân tích theo chiều dọc (vertical analysis measures) nào cần thiết, chẳng hạn như tổng số, tần suất, giá trị trung bình (averages), và các số đo phân tán (measures of dispersion) trên các hàng trong tập dữ liệu.
- Cuối cùng, các biến phân tích có thể được tương quan hoặc cắt lát (sliced) bởi các biến chiều (dimension variables) để thêm vào những hiểu biết sâu sắc từ việc phân tách (disaggregating) tổng số đo dọc.

Phân tích mô tả và chẩn đoán giúp hiểu rõ hơn những gì đã xảy ra và tại sao nó lại xảy ra. Điều gì sẽ xảy ra nếu mục tiêu là dự đoán một kết quả trong tương lai hoặc xác định chiến lược nào có thể đạt được một kết quả cụ thể? Trong những trường hợp đó, chúng ta cần sử dụng các phân tích dự đoán (predictive) hoặc đề xuất (prescriptive), được giải thích ở phần tiếp theo.

### Thiết kế Các Phân tích để Dự đoán và Đề xuất (Designing Analyses to Predict and Prescribe)

Các chiến lược phân tích dự đoán sử dụng dữ liệu lịch sử để tạo ra các mô hình ước tính một giá trị hoặc kết quả trong tương lai. Mặt khác, các chiến lược phân tích đề xuất giúp xác định phương án nào có khả năng tạo ra kết quả tốt nhất dựa trên mục tiêu đã cho. Các chiến lược phân tích dự đoán và đề xuất có thể xác định việc sử dụng nguồn lực một cách tốt nhất, cải thiện hiệu suất, dự đoán các phản ứng và biến động của thị trường, và tránh sự cố về quy trình:
- Các kế toán viên thường sử dụng các chiến lược phân tích này để đánh giá các lựa chọn lập kế hoạch thuế, các lựa chọn chiến lược tiếp thị và hoạt động, các lựa chọn tài trợ, các lựa chọn đầu tư, và các lựa chọn chiến lược rút lui (exit strategy).
- Các ngành công nghiệp có các mục tiêu phân tích này bao gồm các tổ chức cho vay muốn tránh những quyết định tín dụng tồi và các công ty bảo hiểm phải dự đoán thiên tai và sự bùng phát dịch bệnh để họ có thể điều chỉnh mô hình kinh doanh trước khi các cuộc khủng hoảng khiến doanh nghiệp của họ bị ảnh hưởng xảy ra.

Hình minh họa 4.17 tóm tắt các chiến lược phân tích dự đoán và đề xuất phổ biến nhất được sử dụng bởi các kế toán viên không liên quan đến các công cụ công nghệ tiên tiến. Dấu tích màu xanh lá cây cho biết các phân tích phù hợp, và dấu x màu đỏ cho biết các phân tích không phù hợp. Như hình minh họa cho thấy, không có nhiều mô hình dự đoán hoặc đề xuất cho các biến thang đo định danh và thứ bậc trừ khi chúng được sử dụng trong các mô hình mà các biến thang đo khoảng hoặc tỷ lệ được mong muốn cho việc dự đoán.

![ILLUSTRATION 4.17](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.17.png)

Cả hai chiến lược phân tích dự đoán và đề xuất thường sử dụng số liệu thống kê và các kỹ thuật lập mô hình tinh vi (sophisticated modeling techniques) cho các thuật toán của chúng:
- Các công cụ phổ biến cho việc này bao gồm hồi quy thống kê (statistical regression), phân tích chuỗi thời gian (time series analyses), khai phá và ánh xạ quy trình (process mining and mapping), phân tích văn bản (text analysis), mô hình trí tuệ nhân tạo (artificial intelligence models), khai phá dữ liệu (data mining), mô hình toán học (mathematical modeling), mô phỏng phức tạp (complex simulations), và mô hình phân tích độ nhạy giả định (what-if sensitivity analysis modeling).
- Những mô hình này tự đào tạo (train themselves) bằng cách tận dụng các mô hình (patterns), mối quan hệ, và cấu trúc trong dữ liệu hiện có để dự đoán chính xác các điều kiện và kết quả trong tương lai.

Chìa khóa để thiết kế các chiến lược dự đoán hoặc đề xuất là chọn dữ liệu sẽ có tiềm năng tốt nhất để thông tin cho các câu hỏi mục tiêu dự đoán hoặc đề xuất:
- Nếu mục tiêu là dự đoán chi phí bảo trì thiết bị sản xuất của năm tới, dữ liệu giúp giải thích số tiền dự kiến hoặc mức tăng hay giảm chi phí bảo trì là rất cần thiết. Nói cách khác, những biến nào thúc đẩy sự thay đổi trong chi phí bảo trì? Khi những biến đó được xác định, dữ liệu liên quan có thể được chọn và chuẩn bị để phân tích.
- Nếu chúng ta tin rằng mức độ sản xuất tác động đến chi phí bảo trì, thì hãy bao gồm một biến dữ liệu về số lượng sản phẩm được sản xuất, một thước đo cho các mức độ sản xuất phổ biến nhất, hoặc một thước đo xem mức sản xuất dự kiến sẽ tăng hay giảm so với mức hiện tại.

Giả sử các kiểm toán viên của WeMakeIt đang kiểm tra các giả định được sử dụng để tạo số dư trong tài khoản dự phòng nợ nghi ngờ của công ty. Các kiểm toán viên đã phát triển một mô hình bao gồm ba biến có thể tác động đến việc liệu các hóa đơn có được thu đúng hạn hay không. Mô hình dự đoán một hóa đơn có thể chưa thanh toán trong bao nhiêu ngày dựa trên số tiền hóa đơn, liệu họ là khách hàng mới (1) hay hiện tại (0), và khoảng thời gian tín dụng được cho phép trên hóa đơn của họ. Kết quả của mô hình hồi quy được cung cấp trong Hình minh họa 4.18.

![ILLUSTRATION 4.18](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.18.png)

Mô hình này cho thấy các biến này (số tiền hóa đơn, khách hàng mới hay hiện tại, và thời hạn tín dụng) giải thích khoảng 68% sự thay đổi trong số ngày chưa thanh toán của một khách hàng (adjusted R-square). Mô hình này có ý nghĩa thống kê với mức Significance F nhỏ hơn 0.05. Hệ số chặn (intercept) âm sẽ sửa các dự đoán của mô hình đi gần 8 ngày vì khách hàng hiếm khi thanh toán trong tuần đầu tiên khi họ được cung cấp một khoảng thời gian miễn lãi để thanh toán hóa đơn. Mức độ ý nghĩa (significance) của hệ số chặn chỉ ra rằng sự tồn tại đơn thuần của một thời hạn tín dụng là một biến tác động đến số ngày khách hàng cần để thanh toán hóa đơn của họ. Với mô hình này, các kiểm toán viên giờ đây có thể dự đoán rằng một khách hàng mới với hóa đơn $900 và thời hạn 60 ngày để thanh toán sẽ mất khoảng 16.5 ngày để thực hiện thanh toán của họ:
`−7.9617 + $900(0.0008) + 1(1.5350) + 60(0.3954) = 16.48 ngày`

**Rủi ro của Chiến lược Phân tích và Các Kiểm soát Đề xuất (Analysis Strategy Risks and Suggested Controls)**
Hai bước cuối cùng của một kế hoạch phân tích dữ liệu là xem xét các rủi ro cố hữu đối với dữ liệu và các chiến lược phân tích, đồng thời áp dụng các kiểm soát để giảm thiểu những rủi ro đó. Hình minh họa 4.19 nắm bắt các rủi ro phổ biến nhất mà kế toán viên phải đối mặt khi phân tích dữ liệu.

![ILLUSTRATION 4.19](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.19.png)

Việc xem xét các rủi ro này trong quá trình lập kế hoạch chiến lược phân tích và thêm các kiểm soát để giúp giảm thiểu chúng là rất quan trọng. Nếu không có các kiểm soát đó, chúng ta có nguy cơ chuẩn bị, diễn giải và báo cáo các kết quả phân tích không chính xác, có thể khiến bản thân hoặc các bên liên quan của chúng ta đưa ra những quyết định gây hại. Bây giờ chúng ta đã hoàn thành quy trình chọn dữ liệu tốt nhất và các chiến lược phân tích, hãy xem xét cách các kế toán viên thực hiện điều này trong thực hành chuyên môn.

---

### Áp dụng (Apply It 4.3)
**Tạo một Kế hoạch Dự án Phân tích Dữ liệu Dự đoán (Create a Predictive Data Analysis Project Plan)**

**Kế toán Tài chính** Tremendous Toys đã triển khai một cơ sở dữ liệu để nắm bắt các chi phí hàng tồn kho từ hoạt động sản xuất của họ mỗi tuần. Dữ liệu từ các trường dữ liệu sau đã được trích xuất, có ghi chú loại dữ liệu và thang đo lường của mỗi trường.

| Tên trường (Field Name) | Loại trường (Field Type) | Thang đo lường (Field Measurement Scale) |
| --- | --- | --- |
| `ProductionRunNumber` | Dữ liệu thô chưa đo lường | Định danh (Categorical - Nominal) |
| `ProductionRunDate` | Dữ liệu thô chưa đo lường | Khoảng (Interval) |
| `NumberOfToysinRun` | Dữ liệu thô đo lường | Tỷ lệ (Ratio) |
| `ToyIDNumber` | Dữ liệu thô chưa đo lường | Định danh (Categorical - Nominal) |
| `DirectMaterialsUsed` | Dữ liệu thô đo lường | Tỷ lệ (Ratio) |
| `DirectLaborUsed` | Dữ liệu thô đo lường | Tỷ lệ (Ratio) |
| `OverheadCostApplied` | Dữ liệu được tính toán | Tỷ lệ (Ratio) |
| `TotalRunCost` | Dữ liệu được tính toán | Tỷ lệ (Ratio) |
| `TotalUnitCost` | Dữ liệu được tính toán | Tỷ lệ (Ratio) |

Sử dụng dữ liệu sản xuất này, cũng như dữ liệu bán hàng về số lượng đồ chơi của mỗi loại được bán ra mỗi tháng trong ba năm qua, hãy tạo một kế hoạch dự án phân tích dữ liệu dự đoán để ước tính giá trị hàng tồn kho cuối năm của Tremendous Toy vào cuối năm tài chính tiếp theo. Kế hoạch dự án của bạn nên giải quyết những vấn đề sau:
1. Mục tiêu dự án và các câu hỏi cụ thể (Project objective and specific questions)
2. Chiến lược dữ liệu (Data strategy)
3. Chiến lược phân tích (Analysis strategy)
4. Rủi ro trong các chiến lược dữ liệu và phân tích (Risks in data and analysis strategies)
5. Các kiểm soát đối với các chiến lược dữ liệu và phân tích (Controls for data and analysis strategies)

**GIẢI PHÁP (SOLUTION)**
**1. Mục tiêu dự án (Project objective)**
Dự đoán chính xác giá trị hàng tồn kho của cuối năm tiếp theo.
**Các câu hỏi cụ thể (Specific questions)**
- Có bao nhiêu đơn vị sản phẩm được dự đoán sẽ có trong hàng tồn kho vào cuối năm tới?
- Đơn giá dự kiến cho mỗi loại đồ chơi vào cuối năm tới là bao nhiêu?

**2. Chiến lược dữ liệu (Data strategy)**
- Dữ liệu từ hồ sơ sản xuất của ba năm qua của Tremendous Toys sẽ được trích xuất và chuẩn bị để phân tích về chi phí nguyên vật liệu, chi phí nhân công và chi phí sản xuất chung.
- Dữ liệu đơn vị bán hàng theo loại đồ chơi trong ba năm qua sẽ được trích xuất, làm sạch các lỗi dữ liệu bị thiếu, trùng lặp và dữ liệu ngoại lai, đồng thời được tổng hợp (aggregated) theo tháng. Điều này dẫn đến 36 điểm dữ liệu cho doanh số bán đơn vị hàng tháng của từng loại đồ chơi.
- Cần tạo một biến được tính toán cho chi phí trung bình hàng tháng của mỗi loại đồ chơi bằng cách sử dụng các trường `NumberOfToysinRun` và `TotalRunCost`. Trước tiên, dữ liệu này phải được tổng hợp theo tháng. Sau đó, đối với mỗi đồ chơi trong mỗi tháng, tổng chi phí sản xuất hàng tháng phải được chia cho tổng số đồ chơi được sản xuất để tính chi phí đồ chơi trung bình mỗi tháng cho từng loại đồ chơi. Kết quả sẽ là 36 điểm dữ liệu cho chi phí trung bình hàng tháng đối với mỗi loại đồ chơi.

**3. Chiến lược phân tích (Analysis strategy)**
- Doanh số bán hàng tháng 12 tính bằng đơn vị có thể được ước tính bằng cách chạy mô hình hồi quy trên doanh số đơn vị của từng tháng.
- Một biến được tính toán phải được tạo cho các đơn vị hàng tồn kho cuối kỳ của mỗi tháng đối với từng loại đồ chơi, tạo ra 36 điểm dữ liệu cho mỗi đồ chơi. Công thức của biến này là: đơn vị tồn kho đầu kỳ + số đồ chơi sản xuất hàng tháng − số đơn vị bán ra hàng tháng. (Bạn có thể giả định rằng doanh nghiệp này bắt đầu từ ba năm trước với không có hàng tồn kho đầu kỳ.)
- Lượng hàng tồn kho cuối kỳ của tháng 12 tính bằng đơn vị có thể được ước tính bằng cách chạy mô hình hồi quy trên các đơn vị hàng tồn kho cuối mỗi tháng đối với từng loại đồ chơi.
- Đơn giá trung bình của đồ chơi cuối tháng 12 có thể được ước tính bằng cách chạy hồi quy trên chi phí trung bình mỗi tháng trên một đồ chơi.
- Để tính tổng giá trị hàng tồn kho cuối tháng 12, số đơn vị hàng tồn kho cuối tháng 12 của mỗi đồ chơi cần được nhân với chi phí trung bình ước tính của tháng 12 tương ứng. Sau đó, các tổng chi phí này cho mỗi đồ chơi phải được cộng lại để ra tổng giá trị hàng tồn kho cuối tháng 12.

**4. Rủi ro của chiến lược dữ liệu (Risks to data strategy)**
Có thể có dữ liệu bị thiếu, trùng lặp hoặc sai sót trong các trường được chọn để phân tích.

**Rủi ro của chiến lược phân tích (Risks to analysis strategy)**
- Chi phí có thể đã thay đổi trong suốt ba năm qua do tính mùa vụ, sự thay đổi của nhà cung cấp và lạm phát.
- Các phép tính toán có thể chứa lỗi.

**5. Kiểm soát chiến lược dữ liệu (Data strategy controls)**
Thực hiện các bài kiểm tra làm sạch dữ liệu để tìm và sửa các dữ liệu bị thiếu, trùng lặp và các lỗi dẫn đến các điểm dữ liệu ngoại lai.

**Kiểm soát chiến lược phân tích (Analysis strategy controls)**
- So sánh đơn giá và doanh số mỗi tháng để xác định xem có yếu tố lạm phát, tính mùa vụ, hoặc các thay đổi khác xảy ra hay không. Nếu phát hiện sự thay đổi về dữ liệu, nguyên nhân và tính vĩnh viễn (permanence) của chúng nên được xác minh bằng cách nói chuyện với những nhân viên biết câu trả lời.
- Mỗi phép tính được thực hiện nên được xác minh, cũng như các phép tính trung bình.
- Các phân tích hồi quy có thể được xác minh bằng cách tạo các hình ảnh trực quan cho 36 điểm dữ liệu hàng tháng (3 năm) và kiểm tra bằng mắt xem có phù hợp với các ước tính hồi quy hay không.
