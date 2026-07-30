# Chương 3: Động lực và Mục tiêu cho Phân tích Dữ liệu (Motivations and Objectives for Data Analysis)

<!-- tabs:start -->
#### **Tiếng Việt**

# Chương 3: Động lực và Mục tiêu cho Phân tích Dữ liệu (Motivations and Objectives for Data Analysis)

## Tổng quan Chương (Chapter Preview)

### Tài nguyên Dữ liệu Thực hành
Trong chương này, bạn sẽ sử dụng các bộ dữ liệu sau cho bài tập thực hành. Bạn có thể tải về để mở ra xem trước dữ liệu:
- 📥 **<a href="Datasets/Vendor_Payments.csv" download target="_blank"><strong>Vendor_Payments.csv</strong></a>**: Dữ liệu chi tiết các khoản thanh toán cho nhà cung cấp (sử dụng cho tạo Highlight Table).
- 📥 **<a href="Datasets/PCard_Spending.csv" download target="_blank"><strong>PCard_Spending.csv</strong></a>**: Dữ liệu giao dịch thẻ mua hàng (P-Card) của nhân viên.

Phân tích dữ liệu (Data analytics) là một lĩnh vực đang phát triển nhanh chóng và đầy thú vị, và có một nhu cầu lớn trong lĩnh vực này đối với các chuyên gia kế toán, những người có thể sử dụng các công cụ mới để phân tích một lượng lớn dữ liệu. Phân tích dữ liệu và trích xuất thông tin từ nó dẫn đến các quyết định sáng suốt, và các doanh nghiệp ngày nay mong muốn có được những người có những kỹ năng này.

Tuy nhiên, một dự án phân tích dữ liệu không bắt đầu bằng việc đi sâu ngay vào dữ liệu. Việc lập kế hoạch cho dự án, bao gồm hiểu được động lực (motivation) để thực hiện nó và phát triển các mục tiêu cụ thể của nó, cũng quan trọng không kém. Phân tích dữ liệu có thể tốn kém, phức tạp và mất thời gian. Một kế hoạch chi tiết liên kết động lực của dự án với mục tiêu và các câu hỏi trọng tâm của nó, giúp chúng ta chọn ra phương pháp phân tích tốt nhất. Nếu không có kế hoạch, chúng ta có thể bỏ sót những thông tin quan trọng hoặc các câu hỏi thiết yếu, điều này có thể làm cho quá trình phân tích kém hiệu quả hoặc thậm chí vô ích.

Giai đoạn đầu tiên của quy trình phân tích dữ liệu là lập kế hoạch. Nó bao gồm việc xác định động lực của dự án, từ đó giúp xác định mục tiêu. Mục tiêu của dự án thúc đẩy mọi thứ, từ các câu hỏi được đặt ra cho đến các lựa chọn phân tích mà chúng ta thực hiện để tìm ra câu trả lời cho chúng. Chương này xem xét mối liên hệ giữa việc hiểu tại sao dự án là cần thiết và việc phát triển một mục tiêu dự án có trọng tâm.

---

### Góc nhìn Chuyên gia (Professional Insight): Tại sao Động lực và Mục tiêu lại quan trọng đối với các Dự án Phân tích Dữ liệu?

Georgia sống cùng cha mẹ trong khi theo học lấy bằng cử nhân kế toán tại trường đại học địa phương. Ngay sau khi tốt nghiệp, cô đã hoàn thành một kỳ thực tập kiểm toán (auditing internship) trong mùa bận rộn. Cô sắp bước vào chương trình thạc sĩ kế toán trong học kỳ mùa thu.

"Vào ngày đầu tiên thực tập, tôi đã học được rằng các kế toán viên chuyên nghiệp tuân theo một quy trình mỗi khi họ làm việc trong một dự án phân tích dữ liệu. Đầu tiên, họ tìm hiểu động lực cho các dự án của mình, điều này sau đó sẽ ảnh hưởng đến các mục tiêu công việc cụ thể của họ. Khi họ xác định rõ ràng về động lực và mục tiêu của mình, họ có thể lên kế hoạch cho một chiến lược thành công cho các dự án phân tích dữ liệu của mình.

Tôi cũng học được rằng các kế toán viên chuyên nghiệp được thúc đẩy bởi nhiều thứ hơn là các mục tiêu nghề nghiệp cá nhân. Các kiểm toán viên muốn mang lại giá trị gia tăng cho các công ty và khách hàng của họ bằng cách đảm bảo với họ rằng các báo cáo tài chính (financial statements) là đáng tin cậy và chính xác. Suy cho cùng, thông tin tốt có nghĩa là thị trường vốn, các quyết định cho vay, mối quan hệ chính phủ và quan hệ đối tác kinh doanh tốt hơn.

Điều này đã giúp tôi nhận ra rằng tôi cũng được thúc đẩy bởi nhiều thứ hơn là chỉ có được một công việc tuyệt vời sau khi học đại học. Tôi muốn tạo ra sự khác biệt trên thế giới và tôi muốn tôn vinh sự chăm chỉ của cha mẹ tôi trong việc nuôi dạy tôi thành công. Việc nhận thức được động lực này của tôi đã giúp tôi cam kết hơn với mục tiêu và việc học của mình!"

---

## Lộ trình Chương (Chapter Roadmap)

**MỤC TIÊU HỌC TẬP (LEARNING OBJECTIVES)** | **CHỦ ĐỀ (TOPICS)** | **ỨNG DỤNG (APPLY IT)**
--- | --- | ---
**LO 3.1** Tóm tắt mối quan hệ giữa động lực, mục tiêu và các câu hỏi phân tích dữ liệu. | • Hiểu về Động lực (Understanding Motivation)<br>• Các Mục tiêu Rõ ràng Dẫn đến Các Câu hỏi Phân tích Dữ liệu Có trọng tâm | Liên kết Động lực với Mục tiêu (Ví dụ: Kiểm toán)
**LO 3.2** Trình bày cách phát triển các câu hỏi mô tả (descriptive questions). | • Phát triển Các Câu hỏi Mô tả<br>• Các Ví dụ Phân tích Mô tả (Descriptive Analyses Examples) | Mô tả Hành vi Mua hàng của Khách hàng (Ví dụ: Kế toán Tài chính)
**LO 3.3** Trình bày cách phát triển các câu hỏi chẩn đoán (diagnostic questions). | • Phát triển Các Câu hỏi Chẩn đoán<br>• Các Ví dụ Phân tích Chẩn đoán (Diagnostic Analyses Examples) | Xác định Rủi ro Sai sót Trọng yếu của Bán hàng (Ví dụ: Kiểm toán)
**LO 3.4** Trình bày cách phát triển các câu hỏi dự đoán (predictive questions). | • Phát triển Các Câu hỏi Dự đoán<br>• Các Ví dụ Phân tích Dự đoán (Predictive Analyses Examples) | Lên kế hoạch cho Phân tích Xu hướng Bán hàng (Ví dụ: Kế toán Quản trị)
**LO 3.5** Trình bày cách phát triển các câu hỏi đề xuất (prescriptive questions). | • Phát triển Các Câu hỏi Đề xuất<br>• Các Ví dụ Phân tích Đề xuất (Prescriptive Analyses Examples) | Đề xuất Tổ hợp Bán hàng Tối ưu (Ví dụ: Kế toán Quản trị)
**LO 3.6** Mô tả các động lực và mục tiêu cho phân tích dữ liệu trong thực tiễn nghề nghiệp. | • Hệ thống Thông tin Kế toán (Accounting Information Systems)<br>• Kiểm toán (Auditing)<br>• Kế toán Tài chính (Financial Accounting)<br>• Kế toán Quản trị (Managerial Accounting)<br>• Kế toán Thuế (Tax Accounting) | Nối các Động lực với Các Lĩnh vực Thực hành Nghề nghiệp

> **Data** Thẻ Data xuất hiện trong chương khi dữ liệu cho một ví dụ, hình ảnh minh họa hoặc ứng dụng có sẵn trên nền tảng học tập trực tuyến của Wiley. Phần mềm phân tích dữ liệu liên tục thay đổi và có thể có các phiên bản mới hơn của phần mềm được tham chiếu trong chương này. Để biết thêm thông tin, hãy truy cập video đi kèm trên nền tảng học tập trực tuyến của Wiley.

---

## 3.1 Động lực Thông tin đến Các Câu hỏi Phân tích Dữ liệu Dựa trên Mục tiêu Như thế nào?

**MỤC TIÊU HỌC TẬP 1 (LEARNING OBJECTIVE 1)**
**Tóm tắt mối quan hệ giữa động lực, mục tiêu và các câu hỏi phân tích dữ liệu.**

Sẽ dễ dàng hơn để duy trì sự tập trung vào mục tiêu của một nhiệm vụ khi chúng ta biết ngay từ đầu lý do tại sao chúng ta thực hiện nó. Việc hiểu động lực để thực hiện một phân tích và xác định mục tiêu của nó cũng giúp tạo ra các câu hỏi cụ thể, dựa trên mục tiêu (objective-based questions). Xét cho cùng, không thể nhận được câu trả lời đúng nếu chúng ta không biết nên hỏi điều gì.

### Hiểu về Động lực (Understanding Motivation)

Động lực trong phân tích dữ liệu trong kế toán là lý do mà phân tích được thực hiện. Chữ "tại sao" (why) đằng sau một dự án có thể thay đổi, nhưng các dự án phân tích dữ liệu thường được thúc đẩy bởi bốn động lực:
- **Cơ hội (Opportunity):** Đánh giá các cơ hội mới sẽ mang lại lợi ích cho tổ chức.
- **Các vấn đề chuyên môn (Professional issues):** Đánh giá các thay đổi do các luật, quy định mới hoặc các thay đổi trong thực tiễn kế toán.
- **Giải quyết vấn đề (Problem solving):** Giải quyết một vấn đề hoặc rắc rối mà tổ chức đang gặp phải.
- **Đánh giá quy trình và hiệu suất (Process and performance assessment):** Hiểu và cải thiện các quy trình và hiệu suất của tổ chức.

Hình minh họa 3.1 (Illustration 3.1) mô tả một số động lực phổ biến và bao gồm một ví dụ từ một công ty có tên là Super Scooters, công ty chuyên sản xuất và bán nhiều loại xe tay ga.

![ILLUSTRATION 3.1](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.1.png)

Trong mỗi ví dụ của Super Scooters, động lực của phân tích là để mô tả tiềm năng của tình huống, chẩn đoán (diagnose) các yếu tố nguyên nhân hoặc xác định sự thay đổi trong hoạt động, dự đoán (predict) doanh thu bán hàng hoặc thu nhập ròng, hoặc đề xuất (prescribe) quá trình hành động tốt nhất. Bất kể nguồn gốc của động lực là gì, các lựa chọn phân tích dữ liệu mà chúng ta đưa ra phụ thuộc vào những gì có thể thu được từ phân tích. Nếu những lợi ích tiềm năng của nó lớn hơn chi phí thực hiện, thì các bên liên quan (stakeholders) sẽ coi đó là một phân tích có giá trị.

### Các Mục tiêu Rõ ràng Dẫn đến Các Câu hỏi Phân tích Dữ liệu Có trọng tâm (Clear Objectives Lead to Focused Data Analysis Questions)

Bạn vừa học được rằng bốn động lực chung cho phân tích dữ liệu trong kế toán là các cơ hội, thay đổi quy định, giải quyết vấn đề và đánh giá hiệu suất và quy trình. Ví dụ, một công ty có một đơn vị kinh doanh hoạt động kém hiệu quả sẽ đánh giá hiệu suất của nó để hiểu tại sao. Một dự án phân tích dữ liệu thành công phụ thuộc vào một phát biểu cụ thể hơn, điều này sau đó sẽ thông tin cho các câu hỏi sẽ được đặt ra trong phân tích.

#### Xác định Mục tiêu (Determine the Objective)

Mục tiêu của một dự án phân tích dữ liệu tuân theo động lực một cách tự nhiên. Hãy quay lại động lực chung đó đối với phân tích dữ liệu, một đơn vị kinh doanh hoạt động kém hiệu quả:
- **Động lực:** Giải quyết vấn đề bằng cách đánh giá hiệu suất của đơn vị để khám phá lý do tại sao nó lại hoạt động kém hiệu quả.
- Việc cụ thể hơn là cần thiết vì hiệu suất kém có thể có một vài nguyên nhân.
- Bước đầu tiên là xác định rõ các lĩnh vực hiệu suất cần điều tra và trình bày rõ những cuộc điều tra đó nên đạt được điều gì.

Nói cách khác, điều quan trọng là phải làm rõ đích đến (goal) của phân tích dữ liệu.

Mọi dự án phân tích dữ liệu đều bắt đầu với việc thiết lập một mục tiêu (objective), đó chính là đích đến của dự án. Nó là một phát biểu chi tiết những gì dự án sẽ hoàn thành. Một ví dụ mới có thể minh họa cách xác định mục tiêu của một dự án. Omni Restaurants sở hữu các nhà hàng trên năm khu vực tại Hoa Kỳ. Thông tin tài chính cho năm hiện tại theo khu vực được thể hiện trong Hình minh họa 3.2.

Hình minh họa 3.2 cho thấy Omni đang thua lỗ ở một khu vực:
- **Động lực:** Họ lo ngại về những khoản lỗ ở Khu vực 1 (Region 1) và muốn hiểu điều gì đang thúc đẩy chúng.
- **Mục tiêu chung:** Loại bỏ những khoản lỗ tài chính đó.

![ILLUSTRATION 3.2](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.2.png)

Bây giờ chúng ta đã chuyển từ động lực sang mục tiêu. Nhưng mục tiêu là quá chung chung nên thật khó để quyết định nên bắt đầu phân tích từ đâu. Một mục tiêu cụ thể sẽ thu hẹp trọng tâm của phân tích. Trong trường hợp của Omni, chỉ có một khu vực đang gặp thua lỗ:
- **Mục tiêu cụ thể:** Xác định các yếu tố thúc đẩy những khoản lỗ trong Khu vực 1.

Sau khi mục tiêu đã rõ ràng và cụ thể, hãy hình thành các câu hỏi mà sẽ đạt được mục tiêu đó khi chúng được giải quyết.

![ILLUSTRATION 3.3](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.3.png)

#### Đặt câu hỏi một cách rõ ràng (Articulate Questions)

Việc đặt sai các câu hỏi sẽ dẫn đến những câu trả lời không giải quyết được mục tiêu. Các câu hỏi tốt là những câu hỏi rõ ràng, súc tích và có thể đo lường được (measurable). Vậy, các câu hỏi tốt được phát triển như thế nào? Đánh giá mỗi câu hỏi về việc liệu nó có giải quyết được mục tiêu hay không, có tập trung vào một vấn đề duy nhất hay không, có thể đo lường được không và liệu dữ liệu cần thiết để trả lời nó có sẵn hay không. Nếu câu hỏi không đáp ứng các tiêu chí này, hãy sửa đổi nó, chia nhỏ nó ra hoặc bỏ nó đi. Sử dụng lưu đồ trong Hình minh họa 3.3 để phát triển các câu hỏi phân tích dữ liệu cụ thể.

Phương pháp tư duy phản biện (critical thinking) đối với việc phát triển câu hỏi có thể giúp ích cho quá trình này. Hãy nhớ rằng việc tư duy phản biện khi thực hiện phân tích dữ liệu liên quan đến việc xem xét những người bị ảnh hưởng bởi phân tích, mục đích của nó, xem xét nhiều lựa chọn thay thế (alternatives) ở mỗi bước, kiểm soát rủi ro, thu thập thông tin hoặc kiến thức phù hợp, và phản ánh về các dự án trong quá khứ và hiện tại.

![ILLUSTRATION 3.4](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.4.png)

Super Scooters hiện đang ở năm thứ ba của hợp đồng với Lime, và họ không chắc chắn liệu họ đã đưa ra những quyết định sản xuất đúng đắn hay chưa. Doanh số dường như đang giảm ở một số mẫu mã, và chi phí thì đang tăng. Calvin và Lyla đã yêu cầu bạn giúp họ làm ba việc:
1. Hiểu được mẫu mã nào đang có doanh số giảm và tại sao.
2. Dự báo các chi phí bảo hành trong tương lai.
3. Xác định tổ hợp sản phẩm (product mix) có lợi nhuận cao nhất cho việc sản xuất.

Sử dụng khung tư duy phản biện, SPARKS, để xác định động lực, các mục tiêu và các câu hỏi phù hợp với phân tích mà Calvin và Lyla muốn bạn thực hiện. Hình minh họa 3.5 tóm tắt cách tư duy phản biện giúp đánh giá các động lực, mục tiêu và các câu hỏi.

*(1) Một công ty thuộc sở hữu tư nhân (privately held company) là công ty không bán cổ phiếu của họ trên các sàn giao dịch công cộng.*

#### Vai trò của Tư duy Phản biện (The Role of Critical Thinking)

Hãy sử dụng ví dụ Super Scooters để chứng minh tầm quan trọng của việc đánh giá một cách phản biện động lực, mục tiêu và các câu hỏi ở giai đoạn này của quy trình phân tích dữ liệu. Giả sử bạn là một kế toán viên cho công ty Super Scooters. Super Scooters là một công ty thuộc sở hữu tư nhân sản xuất ba mẫu xe tay ga có động cơ (hai mẫu điện và một mẫu chạy bằng xăng) và một mẫu xe tay ga không có động cơ (Hình minh họa 3.4).

![ILLUSTRATION 3.5](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.5.png)

---

## 3.2 Các Mục tiêu Mô tả (Descriptive Objectives) là gì?

**MỤC TIÊU HỌC TẬP 2 (LEARNING OBJECTIVE 2)**
**Trình bày cách phát triển các câu hỏi mô tả.**

Một dự án phân tích dữ liệu với mục tiêu hiểu về một thứ gì đó đang diễn ra ở hiện tại hoặc đã xảy ra đòi hỏi các câu hỏi mô tả (descriptive questions). Những loại câu hỏi này được trả lời bằng cách sử dụng phân tích mô tả (descriptive analytics). Các câu hỏi mô tả thường là những câu hỏi đầu tiên được đặt ra trong bất kỳ phân tích nào vì việc hiểu về dữ liệu là cần thiết trước khi bắt đầu các phân tích chuyên sâu hơn.

### Phát triển Các Câu hỏi Mô tả (Develop Descriptive Questions)

Các câu hỏi mô tả được thiết kế để hiểu rõ hơn về dữ liệu nhằm trả lời các câu hỏi kinh doanh. Để phát triển các câu hỏi mô tả tốt, đầu tiên hãy xác định mục tiêu của phân tích, sau đó chia nhỏ mục tiêu đó thành các câu hỏi. Hãy nhớ rằng, một câu hỏi tốt là một câu hỏi có liên quan đến mục tiêu, cụ thể, có thể đo lường được và có thể được trả lời bằng dữ liệu hiện có.

---

### Ứng dụng 3.1 (Apply It 3.1)
**Liên kết Động lực với Mục tiêu (Link Motivation to Objectives)**

**Kiểm toán (Auditing)**
Đôi bạn thân Luanne và Maxine đã và đang làm các sản phẩm bánh nướng cho một người bạn sở hữu một quán cà phê địa phương. Những món bánh nướng ngon tuyệt của họ chẳng mấy chốc đã có nhiều người hâm mộ đến nỗi Luanne và Maxine phải thuê không gian bếp thương mại để theo kịp nhu cầu. Bây giờ, doanh nghiệp của họ, Best Bakes Bakery, cung cấp các sản phẩm bánh nướng cho nhiều quán cà phê và nhà hàng.

Họ muốn mở rộng hoạt động của mình sang các tiểu bang khác và đang tìm kiếm các nhà đầu tư tiềm năng. Họ tin rằng ý kiến của một CPA về báo cáo tài chính của họ sẽ giúp thuyết phục các nhà đầu tư đầu tư vào công ty của họ.

Các chủ sở hữu đã thuê công ty CPA của bạn để chuẩn bị một bản đánh giá (review) các báo cáo tài chính của họ. Best Bakes Bakery là doanh nghiệp kinh doanh tiệm bánh đầu tiên của công ty bạn, và bạn là kiểm toán viên độc lập (external auditor) được phân công tham gia hợp đồng này. Người giám sát của bạn yêu cầu bạn sử dụng phân tích dữ liệu cho việc đánh giá rủi ro (risk assessment):
- Bạn có dữ liệu báo cáo tài chính của ba năm qua và phải tính toán một số tỷ số (ratios) liên quan đến hoạt động của công ty.
- Người giám sát của bạn tin rằng phân tích sẽ xác định các lĩnh vực có rủi ro sai sót trọng yếu cao hơn tiềm ẩn.

**Yêu cầu:**
1. Hạng mục động lực nào áp dụng cho kịch bản này?
2. Những ai là các bên liên quan trong phân tích dữ liệu của bạn?
3. Mục tiêu phân tích của bạn là gì?

**GIẢI PHÁP (SOLUTION)**
1. Động lực là đánh giá quy trình và hiệu suất. Việc phân tích các tỷ số tài chính sẽ cung cấp thông tin liên quan đến việc đánh giá rủi ro về tiềm năng xảy ra các sai sót trọng yếu (material misstatements).
2. Bạn, công ty kiểm toán của bạn và khách hàng là những bên liên quan nội bộ. Các nhà đầu tư và chủ nợ của khách hàng là các bên liên quan bên ngoài.
3. Mục tiêu của phân tích là xác định rủi ro sai sót trọng yếu tiềm ẩn trong các báo cáo tài chính.


Hãy tiếp tục với ví dụ Super Scooters để minh họa. Hình minh họa 3.6 cung cấp thông tin tài chính cho các năm từ 2023 đến 2025.

![ILLUSTRATION 3.6](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.6.png)

Mặc dù doanh số (sales) và doanh thu thuần (net revenue) đã tăng lên, hai trong số các mẫu mã lại có doanh thu thuần sụt giảm (Hình minh họa 3.7).

![ILLUSTRATION 3.7](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.7.png)

Super Scooters muốn hiểu rõ sự sụt giảm doanh thu thuần của các mẫu Celeritas và Kicks. Họ nên đặt ra những câu hỏi gì cho dữ liệu? Những thước đo (measures) nào có thể được sử dụng để trả lời các câu hỏi đó?

![ILLUSTRATION 3.8](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.8.png)

Hãy chú ý xem tất cả các câu hỏi đều liên quan đến mục tiêu của phân tích như thế nào. Các câu hỏi ban đầu (initial questions) là ổn nhưng còn rộng. Các câu hỏi phụ (sub-questions) trong cột thứ hai sẽ thu hẹp trọng tâm. Hơn nữa, mỗi câu hỏi đều có thể đo lường được, như được chỉ ra bởi các thước đo ở cột cuối cùng. Một khi các câu hỏi mô tả chi tiết được phác thảo, đã đến lúc xác định dữ liệu và phương pháp phân tích cần thiết để trả lời chúng.

### Các Ví dụ Phân tích Mô tả (Descriptive Analyses Examples)

Các phân tích thường được sử dụng để trả lời các câu hỏi mô tả bao gồm các thước đo về tần suất (frequency), vị trí (location), độ phân tán (dispersion) và tỷ lệ phần trăm (percentages):
- Các thước đo **tần suất** giúp chúng ta hiểu các danh mục của dữ liệu.
- Các thước đo **vị trí** (trung bình, trung vị, yếu vị - mean, median, mode) cho thấy các quan sát trung bình trong một tập dữ liệu.
- Các thước đo **độ phân tán** (giá trị nhỏ nhất, giá trị lớn nhất, khoảng, phương sai, và độ lệch chuẩn - minimum, maximum, range, variance, standard deviation) cho thấy có bao nhiêu sự biến thiên giữa các quan sát trong tập dữ liệu.
- Các thước đo **thay đổi tỷ lệ phần trăm** (percentage change) so sánh kết quả với các kỳ trước và tỷ lệ phần trăm của tổng số.

> **Data** Hãy trình bày một ví dụ sử dụng các câu hỏi được xác định trong Hình minh họa 3.8.

Hình minh họa 3.8 cung cấp các ví dụ về cả các câu hỏi ban đầu và các câu hỏi phụ (nói cách khác, các câu hỏi chi tiết hơn).

Có thể khám phá xem tổng doanh số (gross sales) đã giảm đối với mẫu Celeritas hay chưa bằng cách sử dụng thước đo tổng doanh số. Có một số phân tích khác nhau có thể xác định xem tổng doanh số đã giảm hay chưa:
- Số tiền tổng doanh số (Gross sales dollars): thước đo tổng thể (total measure)
- Khối lượng bán hàng (Sales volume): thước đo tổng thể
- Giá bán bình quân một đơn vị (Average unit sales price)

Một bảng PivotTable trong Microsoft Excel được tạo với dữ liệu của Super Scooter chuẩn bị cho một phân tích mô tả cho câu hỏi này (Hình minh họa 3.9).

![ILLUSTRATION 3.9](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.9.png)

Dữ liệu bán hàng xác nhận rằng mẫu Celeritas và Kicks đều suy giảm từ năm 2024 đến năm 2025. Thú vị là, cả khối lượng bán hàng và giá trung bình đều giảm, vì vậy sự suy giảm là sự kết hợp của cả khối lượng và giá cả. Bước tiếp theo là trả lời câu hỏi phụ tiếp theo: Doanh số có giảm ở tất cả các địa điểm không?

Hình minh họa 3.10 cho thấy sự thay đổi trong số tiền tổng doanh số trung bình (average gross sales dollars), đây là một thước đo vị trí. Nó là kết quả của một phân tích mô tả trong Tableau cho thấy sự thay đổi trong tổng doanh số từ năm 2023 đến 2025 theo địa điểm cho mẫu Celeritas. Đây là một bảng đánh dấu (highlight table) trong đó màu tối hơn báo hiệu mức giảm lớn hơn. (**Data** Xem mục How To 3.1 ở cuối chương này để tìm hiểu cách tạo bảng này trong Tableau.)

![ILLUSTRATION 3.10](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.10.png)

Địa điểm Seattle có mức giảm tổng doanh số lớn nhất từ năm 2024 ở mức 140.206 đô la. Dallas có mức giảm lớn thứ hai ở mức 106.783 đô la. Tuy nhiên, rõ ràng là doanh số đã giảm ở tất cả các địa điểm. Bước tiếp theo là xác định lý do tại sao doanh số lại giảm, điều này sẽ yêu cầu phân tích chẩn đoán (diagnostic analytics).

---

### Ứng dụng 3.2 (Apply It 3.2)
**Mô tả Hành vi Mua hàng của Khách hàng (Describe Customers' Buying Behavior)**

> **Data** **Kế toán Tài chính (Financial Accounting)** Best Bakes Bakery muốn hiểu rõ hơn về hành vi mua hàng của những khách hàng hàng đầu của họ. Bạn đã được cung cấp các giao dịch bán hàng cho các năm 2022 đến 2025. Một đoạn trích từ file (dữ liệu) theo sau.

![Apply It 3.2](../TaiLieu/textbookForPractice/Figures/Ch_03/Apply%20It%203.2.png)

**Yêu cầu:**
1. Mục tiêu của phân tích là gì?
2. Phát triển ba câu hỏi phù hợp với mục tiêu, và mô tả các thước đo (measures) cần thiết để trả lời các câu hỏi đó.
3. Bạn sẽ sử dụng những phân tích nào để trả lời những câu hỏi này?

**GIẢI PHÁP (SOLUTION)**
1. Mục tiêu của phân tích là xác định các khách hàng hàng đầu và đánh giá những sản phẩm họ mua.
2. 
| **Câu hỏi (Questions)** | **Thước đo (Measures)** |
| --- | --- |
| 1. Năm khách hàng hàng đầu là ai? | Tổng doanh số, khối lượng bán hàng, tỷ suất lợi nhuận (profit margin) |
| 2. Năm sản phẩm bán chạy nhất là gì? | Khối lượng bán hàng, tổng doanh số |
| 3. Khách hàng chi tiêu theo mô hình nào đối với năm khách hàng hàng đầu? | Khối lượng bán hàng, tổng doanh số |

3. Các phân tích cho ba câu hỏi:
   1. **Phân tích mô tả:** Năm khách hàng hàng đầu theo năm cho mỗi thước đo so với mức trung bình của tất cả các khách hàng.
   2. **Phân tích mô tả:** Năm sản phẩm bán chạy nhất theo năm cho mỗi thước đo so với mức trung bình của tất cả các sản phẩm.
   3. **Phân tích mô tả:** Phân tích cho thấy doanh số bán hàng theo tháng hoặc quý của mỗi năm cho năm khách hàng hàng đầu. Có thể sử dụng biểu đồ thanh (bar chart) hoặc biểu đồ đường (line chart).

---

## 3.3 Các Mục tiêu Chẩn đoán (Diagnostic Objectives) là gì?

**MỤC TIÊU HỌC TẬP 3 (LEARNING OBJECTIVE 3)**
**Trình bày cách phát triển các câu hỏi chẩn đoán.**

Khi chúng ta đã biết những gì đã xảy ra, bước tiếp theo là xác định tại sao. Các câu hỏi chẩn đoán (diagnostic questions) được xây dựng dựa trên các phân tích mô tả và khám phá thêm dữ liệu để tìm ra nguyên nhân của kết quả. Phân tích chẩn đoán (diagnostic analytics) thực hiện điều này bằng cách tìm kiếm các điểm bất thường (anomalies), các mối tương quan (correlations), các khuôn mẫu (patterns), hoặc các xu hướng (trends).

### Phát triển Các Câu hỏi Chẩn đoán (Develop Diagnostic Questions)

Các câu hỏi chẩn đoán xác định một vấn đề hoặc rắc rối để hiểu tại sao một kết quả lại xảy ra. Hình minh họa 3.11 cho thấy các câu hỏi chẩn đoán dựa trên kết quả phân tích mô tả doanh số bán hàng của Super Scooters ở phần trước.

![ILLUSTRATION 3.11](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.11.png)

Tại sao doanh số lại giảm, và cụ thể hơn, tại sao địa điểm Seattle lại có mức giảm lớn nhất? Các câu hỏi và câu hỏi phụ đào sâu hơn vào sự sụt giảm doanh số bằng cách hỏi về các điểm bất thường và các mô hình bất thường. Bây giờ, hãy xác định dữ liệu và các phân tích sẽ trả lời các câu hỏi này.


### Các Ví dụ Phân tích Chẩn đoán (Diagnostic Analyses Examples)

Có bốn loại phân tích chẩn đoán phổ biến: phát hiện điểm bất thường (anomaly detection), tương quan (correlation), phát hiện khuôn mẫu (pattern detection), và phân tích xu hướng (trend analysis).

Sử dụng các câu hỏi của Super Scooters trong Hình minh họa 3.11, hãy kiểm tra các câu hỏi phụ sau:
1. Có những khuôn mẫu nhận diện được nào trong khối lượng bán hàng của mẫu Celeritas không?
2. Có những khuôn mẫu bất thường nào trong doanh số của mẫu Celeritas tại địa điểm Seattle không?

Biểu đồ đường (line charts) có thể xác định các khuôn mẫu bằng cách tiết lộ các mô hình lặp lại trong dữ liệu. Hình minh họa 3.12 cho thấy doanh số của Celeritas theo tháng của từng năm.

![ILLUSTRATION 3.12](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.12.png)

Các biểu đồ đường trong Hình minh họa 3.12 dường như không cho thấy một khuôn mẫu nào trong khối lượng bán hàng cho mẫu Celeritas. Tuy nhiên, biểu đồ đường này hiển thị tất cả các địa điểm, và các phân tích trước đó đã tiết lộ rằng địa điểm Seattle có sự sụt giảm doanh số của Celeritas.

Khuôn mẫu bán hàng trong các năm 2023 và 2025 chỉ ra rằng doanh số nhìn chung tăng từ quý đầu tiên đến quý thứ ba:
- Vào năm 2023 có một sự sụt giảm doanh số trong quý 4, nhưng năm 2024 và 2025 lại chứng kiến sự gia tăng trong doanh số quý 4.
- Tuy nhiên, doanh số năm 2025 thấp hơn doanh số năm 2024, và đã có một đợt sụt giảm lớn trong quý 3.

Để hiểu tại sao doanh số năm 2025 lại thấp hơn và tại sao lại có sự sụt giảm trong quý 3 năm 2025, chúng ta phải phân tích thêm khối lượng bán hàng theo địa điểm.

Hình minh họa 3.13 hiển thị một phân tích kiểm tra doanh số bán hàng hàng tháng của Celeritas tại địa điểm Seattle.

![ILLUSTRATION 3.13](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.13.png)

Biểu đồ cột về doanh số của Celeritas trong suốt năm 2025 cho thấy một điều và gợi ý một điều khác:
- Trong năm 2025 có một vài tháng không có doanh số.
- Đây có thể là một yếu tố góp phần vào sự sụt giảm trong tổng doanh số của Celeritas trong năm 2025.

Bước tiếp theo sẽ là hỏi ban quản lý xem điều gì đã xảy ra vào tháng 3 năm 2025 dẫn đến sáu tháng không có bất kỳ doanh số nào của mẫu Celeritas. Điều này cũng làm dấy lên các câu hỏi bổ sung cần điều tra:
- Có phải doanh số chỉ giảm ở địa điểm Seattle không?
- Mẫu Celeritas có phải là sản phẩm duy nhất có doanh số giảm không?

Quá trình điều tra này được gọi là phân tích dữ liệu khám phá (exploratory data analysis), mà bạn sẽ được học ở phần sau của khóa học này.

---

### Ứng dụng 3.3 (Apply It 3.3)
**Xác định Rủi ro Sai sót Trọng yếu của Bán hàng (Determine the Risk of Material Misstatement of Sales)**

> **Data** **Kiểm toán (Auditing)** Trong suốt cuộc kiểm toán báo cáo tài chính của Best Bakes Bakery, bạn được yêu cầu xác định xem có những thay đổi bất thường nào về doanh thu so với các năm trước có thể ảnh hưởng đến rủi ro sai sót trọng yếu hay không. Bạn đã được cung cấp một đoạn trích các giao dịch trong một file Excel để bạn biết được những dữ liệu nào có sẵn.

![Apply It 3.3](../TaiLieu/textbookForPractice/Figures/Ch_03/Apply%20It%203.3.png)

**Yêu cầu:**
1. Mục tiêu của phân tích là gì?
2. Phát triển ba câu hỏi phù hợp với mục tiêu, và nêu ra các thước đo cần thiết để trả lời chúng.
3. Bạn sẽ sử dụng những phân tích nào để trả lời ba câu hỏi này?

**GIẢI PHÁP (SOLUTION)**
1. Mục tiêu là phân tích các giao dịch từ năm 2022 đến năm 2025 đối với những thay đổi bất thường. Phân tích này sẽ cung cấp cho kiểm toán viên thông tin để xác định bản chất, thời gian và phạm vi của các thủ tục kiểm toán.
2. 
| **Câu hỏi (Questions)** | **Thước đo (Measures)** |
| --- | --- |
| 1. Có bất kỳ thay đổi bất thường nào trong tổng doanh thu qua các năm 2022–2025 không? | Tổng doanh số hàng quý |
| 2. Có bất kỳ thay đổi bất thường nào trong tổng doanh thu qua các năm theo địa điểm không? | Tổng doanh số hàng quý |
| 3. Có bất kỳ thay đổi bất thường nào trong doanh thu theo sản phẩm qua các năm không? | Khối lượng bán hàng theo sản phẩm |

3. Các phân tích điểm bất thường (anomaly), khuôn mẫu (pattern), và xu hướng (trend) có thể được chuẩn bị để trả lời các câu hỏi này.

---

## 3.4 Các Mục tiêu Dự đoán (Predictive Objectives) là gì?

**MỤC TIÊU HỌC TẬP 4 (LEARNING OBJECTIVE 4)**
**Trình bày cách phát triển các câu hỏi dự đoán.**

Cho đến nay, bạn đã học được cách phát triển các câu hỏi mô tả để tìm hiểu những gì đã xảy ra trong quá khứ và các câu hỏi chẩn đoán để hiểu lý do tại sao. Sẽ ra sao nếu bạn muốn biết những gì có thể xảy ra trong tương lai? Trong trường hợp này, bạn sẽ hỏi các câu hỏi dự đoán (predictive questions).

### Phát triển Các Câu hỏi Dự đoán (Develop Predictive Questions)

Khi đưa ra các quyết định cho vay, các ngân hàng sử dụng thông tin lịch sử về việc liệu một người đi vay tiềm năng có thanh toán các hóa đơn một cách nhất quán và đúng hạn hay không để dự đoán xem liệu họ có tiếp tục làm như vậy hay không. Theo cách tương tự, phân tích dự đoán (predictive analytics) sử dụng dữ liệu trong quá khứ và hiện tại để tạo ra các mô hình (models) để các doanh nghiệp có thể đưa ra các dự đoán.

Việc sử dụng phân tích dự đoán không phải là mới trong nghề kế toán, nhưng do sự sẵn có của dữ liệu và các công cụ phần mềm để thực hiện phân tích dự đoán đã gia tăng, nên việc thực hiện các phân tích này trong mọi lĩnh vực của kế toán cũng gia tăng theo:
- Kế toán tài chính có thể xác định các xu hướng trong doanh số bán hàng hoặc chi phí.
- Kế toán chi phí có thể dự đoán chi phí, lập các dự báo, và đánh giá các yếu tố dẫn dắt chi phí (cost drivers).
- Kiểm toán viên xác định các sai sót trọng yếu tiềm ẩn bằng cách sử dụng phân tích dự đoán.
- Kế toán thuế có thể sử dụng phân tích dự đoán cho việc lập kế hoạch thuế.


Giả sử Super Scooters đang lập ngân sách (budget) cho năm tới:
- Họ muốn dự đoán doanh thu cho năm 2026 với giả định khối lượng bán hàng tăng 10%.
- Họ cũng tin rằng chi phí bảo hành sẽ tăng 10%.
- Cuối cùng, họ đang xem xét việc ngừng sản xuất mẫu Celeritas và muốn biết liệu điều đó có làm thay đổi doanh thu dự đoán hay không.

Mục tiêu tổng thể của phân tích dữ liệu là gì? Super Scooters nên đặt ra những câu hỏi nào để đáp ứng mục tiêu đó?

Khi xác định các câu hỏi dự đoán, sẽ rất hữu ích nếu hỏi: "Tôi muốn làm gì với câu trả lời?" Hình minh họa 3.14 cho thấy mục tiêu tổng thể của việc dự đoán doanh thu cho năm 2026, câu hỏi ban đầu, cộng với các câu hỏi phụ cụ thể.

![ILLUSTRATION 3.14](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.14.png)

Cũng giống như tất cả các câu hỏi, các câu hỏi dự đoán nên liên quan đến mục tiêu, cụ thể, có thể đo lường được, và phải sử dụng dữ liệu và phân tích thích hợp để trả lời chúng.

### Các Ví dụ Phân tích Dự đoán (Predictive Analyses Examples)

Hai phân tích phổ biến trả lời các câu hỏi dự đoán là các đường xu hướng (trendlines) và phân tích hồi quy (regression analysis).*(2)*

*(2) Có nhiều phương pháp phân tích dự đoán khác, chẳng hạn như trí tuệ nhân tạo (artificial intelligence), nằm ngoài phạm vi của chương này.*

#### Đường xu hướng (Trendlines)

Các đường xu hướng cho thấy mối quan hệ chức năng cơ bản của dữ liệu:
- Một mối quan hệ chức năng (functional relationship) là tác động của một biến độc lập (independent variable) lên một biến phụ thuộc (dependent variable).
- Một hàm tuyến tính (linear function) cho thấy sự tăng hoặc giảm đều đặn trên phạm vi của biến độc lập.

Công cụ Trendline của Excel có thể giúp xác định xem dữ liệu có tuân theo một hàm tuyến tính hay không. Hãy nhớ rằng Super Scooters tin rằng chi phí bảo hành sẽ tăng 10%. Hơn nữa, chi phí bảo hành được cho là bị thúc đẩy bởi doanh số bán hàng.

![ILLUSTRATION 3.15](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.15.png)

Đường xu hướng hỗ trợ một mối quan hệ tuyến tính:
- Khi số tiền tổng doanh số tăng, chi phí bảo hành cũng tăng theo.
- Phương trình cho đường xu hướng được hiển thị trong biểu đồ (y = 0.0431x + 18.632, R² = 0.9064). 

Phương trình đó có thể được sử dụng để dự đoán chi phí bảo hành trong tương lai dựa trên doanh số dự kiến trong đó y là số tiền chi phí bảo hành và x là số tiền tổng doanh số. Ví dụ, nếu tổng doanh số là 2.000 đô la, thì chi phí bảo hành dự kiến sẽ là:
> (0.0431 × 2.000) + 18.632 = $104.83

Nếu chi phí bảo hành tăng 10% như dự kiến của Super Scooters, mô hình dự đoán có thể được điều chỉnh bằng cách tăng 0,0431 lên 10%. Tìm công cụ đường xu hướng Chart Elements trong Excel bằng cách nhấp vào biểu đồ và sau đó nhấp vào dấu cộng (Hình minh họa 3.16).

![ILLUSTRATION 3.16](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.16.png)

Hình minh họa 3.15 cho thấy một đường xu hướng được tạo trong Excel để xác định xem có mối quan hệ tuyến tính giữa doanh số bán hàng và chi phí bảo hành của Super Scooters hay không.

Lưu ý rằng việc nhấp vào dấu cộng ở trên cùng bên trái của biểu đồ bao gồm tùy chọn chọn Trendline, và sau đó là More Options (Hình minh họa 3.17).

![ILLUSTRATION 3.17](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.17.png)

Hộp Format Trendline mở ra cho phép người dùng chọn các hàm số khác (exponential - số mũ, logarithmic - logarit, polynomial - đa thức, power - lũy thừa và moving average - trung bình động). Điều này có thể hữu ích nếu khuôn mẫu của dữ liệu dường như không phải là tuyến tính. Đồng thời, nhấp vào các hộp để hiển thị phương trình và R-square (R bình phương) trên biểu đồ. R-square là thước đo mức độ phù hợp của đường so với dữ liệu. Càng gần 1, độ phù hợp càng tốt. Đường xu hướng trong Hình minh họa 3.16 có R-square rất mạnh là 0,9064. Chúng ta sẽ thảo luận chi tiết hơn về R-square trong phần tiếp theo.

#### Hồi quy Tuyến tính (Linear Regression)

Mặc dù bạn có thể không chuẩn bị một mô hình dự đoán trong suốt sự nghiệp của mình, nhưng bạn có khả năng sẽ sử dụng các mô hình dự đoán hoặc cần diễn giải kết quả đầu ra của chúng. Hồi quy tuyến tính là một công cụ để xây dựng các mô hình toán học và thống kê nhằm giải thích mối quan hệ giữa một biến phụ thuộc và một hoặc nhiều biến độc lập.

Phân tích dự đoán xây dựng các mô hình để dự đoán hoặc hiểu rõ hơn về một hiện tượng. Để tìm ra những yếu tố nào ảnh hưởng đến chi phí bảo hành, chúng ta sẽ xây dựng một mô hình dự đoán chi phí bảo hành.

Việc xây dựng một mô hình đòi hỏi phải xác định các biến sẽ được đưa vào đó:
- Một biến (variable) là một trường dữ liệu được sử dụng để phân tích.
- Một biến phụ thuộc (dependent variable) là thước đo kết quả đầu ra (chi phí bảo hành).
- Các biến độc lập (independent variables) là các biến ảnh hưởng đến biến phụ thuộc (các biến cụ thể mà chúng ta tin rằng có ảnh hưởng đến chi phí bảo hành, chẳng hạn như doanh số bán hàng hoặc số lượng yêu cầu bảo hành).

Hồi quy tuyến tính đơn (simple linear regression) liên quan đến một biến độc lập duy nhất, trong khi hồi quy đa biến (multiple regression) liên quan đến hai hay nhiều biến độc lập. Mục tiêu của mô hình hồi quy là tìm phương trình của đường phù hợp nhất với dữ liệu.

Hãy kiểm tra kết quả đầu ra của một mô hình hồi quy để hiểu cách chúng giúp trả lời các câu hỏi. Là một kế toán viên tại Super Scooters, bạn đang cố gắng ước tính chi phí bảo trì (maintenance expense) cho các thiết bị máy móc vào năm tới. Bạn tin rằng các yếu tố dẫn dắt chi phí đối với chi phí bảo trì là số giờ thiết bị được sử dụng và số lượng yêu cầu sửa chữa. Các biến của mô hình hồi quy sẽ là:
- **Biến phụ thuộc:** Chi phí bảo trì
- **Biến độc lập:** Số giờ máy (machine hours) và số yêu cầu sửa chữa (repair requests)

Dữ liệu lịch sử từ 36 tháng trước đó sẽ được sử dụng để tạo mô hình hồi quy. Kết quả từ mô hình được hiển thị trong Hình minh họa 3.18.

![ILLUSTRATION 3.18](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.18.png)

Hồi quy trong Hình minh họa 3.18 được thực hiện bằng Microsoft Excel. Bản tóm tắt đầu ra được chia thành ba phần.

**Thống kê Hồi quy (Regression Statistics)**
Phần đầu tiên là thống kê hồi quy, hoặc các thước đo thống kê được sử dụng để đánh giá mô hình. Hình minh họa 3.19 cho thấy các số liệu thống kê hồi quy từ Hình minh họa 3.18, cùng với định nghĩa của thống kê và cách diễn giải đối với mô hình hồi quy của Super Scooters.

![ILLUSTRATION 3.19](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.19.png)

**Phân tích Phương sai (ANOVA)**
Phần tiếp theo của đầu ra hồi quy là ANOVA (phân tích phương sai). Hình minh họa 3.20 là phần ANOVA từ mô hình hồi quy.

Trong một hồi quy tuyến tính đa biến như thế này, ý nghĩa (significance) là một kiểm định giả thuyết (hypothesis test) xem liệu mô hình hồi quy có tốt hơn một mô hình không có biến độc lập nào hay không. Nói cách khác, liệu mô hình này có tốt hơn việc không có mô hình nào cả?

![ILLUSTRATION 3.20](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.20.png)

Thông thường, một mô hình được coi là có ý nghĩa nếu thống kê F (Significance F trong Hình minh họa 3.20) nhỏ hơn 0,05:
- Nếu F có ý nghĩa, thì mô hình có thể giải thích được một phần sự biến thiên của biến phụ thuộc. Nói cách khác, nó tốt hơn là không có mô hình nào cả.
- Phân tích ANOVA trong Hình minh họa 3.20 có Significance F là 2.05385E-23. Ký hiệu "E-23" sau 2.05385 đại diện cho ký hiệu khoa học, còn được gọi là ký hiệu số mũ (exponential notation). 2.05385E-23 giống với 0.0000000000000000000000205385. Rõ ràng nó là một số thấp hơn rất nhiều so với 0,05, vì vậy mô hình là có ý nghĩa (significant).

Nói cách khác, các biến độc lập có thể giải thích một phần sự thay đổi của tổng chi phí, do đó mô hình này tốt hơn là không có mô hình nào cả.

**Phương trình Hồi quy (Regression Equation)**
Phần cuối cùng của tóm tắt đầu ra hồi quy cung cấp thông tin để tạo ra phương trình dự đoán biến phụ thuộc:
- Điểm cắt (intercept) và các hệ số (coefficients) của mô hình biểu diễn phương trình của đường thẳng phù hợp nhất với dữ liệu.
- Thống kê chính cần phân tích trong phần này là p-value (giá trị p) cho mỗi biến độc lập. Giống như thống kê F, p-value cung cấp một kiểm định ý nghĩa. Trong trường hợp p-value, đó là kiểm định xem liệu biến độc lập có cải thiện khả năng của mô hình trong việc dự đoán tốt hơn biến phụ thuộc hay không. Một p-value từ 0,05 trở xuống thường được coi là có ý nghĩa (significant).

Hãy sử dụng đầu ra trong Hình minh họa 3.21 để xác định mô hình dự đoán cho chi phí bảo trì máy móc và diễn giải các hệ số.

![ILLUSTRATION 3.21](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.21.png)

Lưu ý rằng p-value cho các biến độc lập đáp ứng được kiểm định nhỏ hơn 0,05 và do đó có ý nghĩa. Mô hình dự đoán sẽ bằng điểm cắt cộng (hoặc trừ nếu số âm) các hệ số của các biến độc lập nhân với các giá trị dự đoán cho các biến đó. Dựa trên mô hình hồi quy trong Hình minh họa 3.21, phương trình để dự đoán tổng chi phí bộ phận mua hàng (purchasing department costs) là:
> $5,252.86 + $3.57 (số giờ máy) + $759.84 (số yêu cầu sửa chữa)

Việc tính toán tổng chi phí dự kiến nếu có 2.250 giờ máy trong một tháng và 8 yêu cầu sửa chữa được thể hiện trong Hình minh họa 3.22. Bắt đầu với điểm cắt và cộng thêm tích số của mỗi hệ số biến độc lập và giá trị dự đoán của biến đó để có được mức dự đoán là $19,364.08 của tổng chi phí bảo trì trong năm.

![ILLUSTRATION 3.22](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.22.png)

Mô hình có thể được diễn giải như sau:
- **Điểm cắt (Intercept):** Điểm cắt không phải lúc nào cũng có diễn giải thực tế. Đó là một kết quả của mô hình thể hiện mức trung bình cho phản ứng khi tất cả các biến độc lập bằng 0. Đó là nơi hàm số của phương trình cắt trục y. Tuy nhiên, ở đây điểm cắt thể hiện số tiền chi phí cố định tồn tại bất kể số giờ máy và yêu cầu sửa chữa.
- **Số giờ máy (Machine hours):** Mỗi giờ thiết bị máy móc được sử dụng làm tăng thêm 3,57 đô la vào tổng chi phí.
- **Yêu cầu sửa chữa (Repair requests):** Mỗi yêu cầu làm tăng thêm 759,84 đô la vào tổng chi phí.

Sử dụng một mô hình giống như trong Hình minh họa 3.22 giúp các doanh nghiệp dự đoán kết quả trong tương lai. (**Data** Xem mục How To 3.2 để tìm hiểu cách thực hiện hồi quy này trong Microsoft Excel.)

---

### Ứng dụng 3.4 (Apply It 3.4)
**Lên kế hoạch cho Phân tích Xu hướng Bán hàng (Plan a Sales Trend Analysis)**

> **Data** **Kế toán Quản trị (Managerial Accounting)** Là một kế toán viên quản trị cho Best Bakes Bakery, bạn đang chuẩn bị một bản phân tích các xu hướng bán hàng để giúp lập ngân sách hoạt động năm 2026. Bạn đã được cung cấp các giao dịch bán hàng cho các năm 2022–2025. Sau đây là một đoạn trích từ file.

![Apply It 3.4](../TaiLieu/textbookForPractice/Figures/Ch_03/Apply%20It%203.4.png)

**GIẢI PHÁP (SOLUTION)**
1. Mục tiêu của phân tích là dự đoán doanh số cho ngân sách hoạt động năm tới.
2. 
| **Câu hỏi (Questions)** | **Thước đo (Measures)** |
| --- | --- |
| Doanh số bán hàng có xu hướng như thế nào từ 2022 đến 2025? | Khối lượng bán hàng, giá bán trung bình |
| Doanh số bán hàng theo sản phẩm có xu hướng như thế nào từ 2022 đến 2025? | Khối lượng bán hàng, giá bán trung bình |
| Doanh số bán hàng theo địa điểm có xu hướng như thế nào từ 2022 đến 2025? | Khối lượng bán hàng, giá bán trung bình |

3. Phân tích đường xu hướng (Trendline analysis) sẽ cung cấp một ước tính về xu hướng bán hàng mà sau đó có thể được áp dụng cho ngân sách năm 2026.

---

## 3.5 Các Mục tiêu Đề xuất (Prescriptive Objectives) là gì?

**MỤC TIÊU HỌC TẬP 5 (LEARNING OBJECTIVE 5)**
**Trình bày cách phát triển các câu hỏi đề xuất.**

Bạn đã học về các câu hỏi giúp mô tả những gì đã xảy ra, điều tra nguyên nhân tại sao, và dự báo những gì sẽ xảy ra tiếp theo. Tiếp theo, hãy kiểm tra các câu hỏi mà chúng ta đặt ra khi muốn biết những gì nên xảy ra.

### Phát triển Các Câu hỏi Đề xuất (Develop Prescriptive Questions)

Các mục tiêu đề xuất (prescriptive objectives) được xây dựng dựa trên các mô tả về hiện tại và các dự đoán về tương lai để xác định hành động tốt nhất. Các câu hỏi đề xuất điều tra cách làm thế nào để tận dụng các cơ hội trong tương lai hoặc giảm nhẹ kết quả rủi ro trong tương lai. Các phân tích chỉ định những hành động cần thiết để đạt được các kết quả mong muốn.

Trong ví dụ về Super Scooters, chúng ta đã trả lời câu hỏi dự đoán trước đó về chi phí bảo hành cho năm 2026. Bây giờ, chúng ta có thể giải quyết phân tích thứ ba do Super Scooters yêu cầu – quyết định cần sản xuất bao nhiêu đơn vị của mỗi mẫu để đạt được mục tiêu doanh thu năm 2026. Bước đầu tiên là đặt rõ ràng các câu hỏi.

Hình minh họa 3.23 bắt đầu với mục tiêu xác định tổ hợp sản phẩm có lợi nhuận cao nhất:
- Câu hỏi ban đầu thì cụ thể hơn. Nên sản xuất và bán bao nhiêu xe tay ga để tối đa hóa số dư đảm phí (contribution margin)?
- Tiếp theo, đào sâu hơn bằng cách hỏi về các ràng buộc tiềm ẩn (potential constraints) nên được đưa vào mô hình tối ưu hóa và nên sản xuất bao nhiêu đơn vị của mỗi mẫu.

![ILLUSTRATION 3.23](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.23.png)

Các phân tích đề xuất được thực hiện với các phương pháp phân tích và dữ liệu cụ thể.

### Các Ví dụ Phân tích Đề xuất (Prescriptive Analyses Examples)

Hai phương pháp phân tích phổ biến nhất được sử dụng để trả lời các câu hỏi đề xuất là các mô hình tối ưu hóa (optimization models) và phân tích "what-if" (what-if analyses).

#### Tối ưu hóa Tuyến tính (Linear Optimization)

Tối ưu hóa (optimization) là quá trình lựa chọn các giá trị của các biến số sao cho giảm thiểu hoặc tối đa hóa một đại lượng quan tâm nào đó. Mô hình hóa tối ưu (optimization modeling) giúp các nhà quản lý phân bổ các nguồn lực hiệu quả hơn.


hiệu quả hơn và đưa ra các quyết định về chi phí/lợi nhuận. Mô hình tối ưu hóa phổ biến nhất được sử dụng trong kế toán là tối ưu hóa tuyến tính. Trong tối ưu hóa tuyến tính, mô hình bao gồm:
- **Các biến quyết định (Decision variables):** Các giá trị chưa biết mà mô hình tìm cách xác định.
- **Hàm mục tiêu (Objective function):** Phương trình toán học mô tả mục tiêu đầu ra cần giảm thiểu hoặc tối đa hóa.
- **Các ràng buộc (Constraints):** Các giới hạn, yêu cầu, hoặc các hạn chế khác phải được áp dụng cho bất kỳ giải pháp nào, chẳng hạn như các ràng buộc về nhu cầu, vật liệu hoặc lao động.

Đầu ra từ một mô hình tối ưu hóa tuyến tính sẽ hiển thị giải pháp tối ưu.

Ban quản lý của Super Scooters đã quyết định tiếp tục sản xuất cả hai mẫu Celeritas và Kicks trong ít nhất một năm nữa. Họ muốn biết nên sản xuất bao nhiêu đơn vị của mỗi mẫu để tối đa hóa số dư đảm phí (contribution margin). Họ đã dự báo nhu cầu cho mỗi mẫu:
- Captain: 18.000 chiếc.
- Celeritas: 10.000 chiếc.
- Kicks: 7.000 chiếc.
- Lazer: 24.000 chiếc.

Vì muốn tránh lượng hàng tồn kho dư thừa, họ không muốn sản xuất nhiều hơn mức họ dự kiến bán được. Ngoài ra cũng có một giới hạn về số giờ máy (machine hours) có sẵn trong năm.

Hình minh họa 3.24 cho thấy thông tin cần thiết để tạo một mô hình tối ưu hóa cho Super Scooters.

![ILLUSTRATION 3.24](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.24.png)

Chương trình tối ưu hóa tuyến tính sẽ sử dụng dữ liệu này để giải quyết số lượng tối ưu của mỗi mẫu cần được sản xuất, trong đó số dư đảm phí (hàm mục tiêu) được tối đa hóa tùy thuộc vào các ràng buộc. Lưu ý rằng chúng ta đã bắt đầu với một con số 1 tùy ý trong các ô số lượng đơn vị được sản xuất. Con số này cũng có thể là số 0 khi bắt đầu; tuy nhiên, việc sử dụng số 1 giúp chúng ta có thể xác nhận các công thức. Tính năng tối ưu hóa tuyến tính có sẵn trong Microsoft Excel Solver có thể minh họa cách hoạt động của các mô hình tối ưu hóa. Chương trình Solver được truy cập thông qua tab Data trên thanh công cụ ribbon (Hình minh họa 3.25).

![ILLUSTRATION 3.25](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.25.png)

Nhấp vào Solver sẽ mở ra một hộp thoại để nhập ô hàm mục tiêu, ô biến quyết định và tạo bất kỳ ràng buộc nào có liên quan. Hình minh họa 3.26 là hộp thoại Solver được sử dụng để tạo chương trình tối ưu hóa cho Super Scooters.

![ILLUSTRATION 3.26](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.26.png)

Khi tất cả các ràng buộc đã được nhập vào, hãy đánh dấu vào ô để đảm bảo kết quả của Solver không bị âm (chúng ta không thể "hủy sản xuất" một sản phẩm) và chọn Phương pháp giải (Solving Method) là Simplex LP, vì đây là một tối ưu hóa tuyến tính. Nhấp vào Solve sẽ tạo ra hộp thoại như trong Hình minh họa 3.27.

![ILLUSTRATION 3.27](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.27.png)

Hộp thoại này cho thấy Solver đã tìm thấy một giải pháp tối ưu thỏa mãn các ràng buộc. Lựa chọn mặc định là Keep Solver Solution (Giữ giải pháp của Solver). Nếu nút (radio button) này được chọn, bảng tính sẽ phản ánh số tiền mới của biến quyết định và số dư đảm phí tối ưu (Hình minh họa 3.28). Ngoài ra còn có sự lựa chọn để tạo ra ba báo cáo. Chọn báo cáo Answer (Câu trả lời) và nhấp OK.

![ILLUSTRATION 3.28](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.28.png)

Hình minh họa 3.29 là báo cáo Answer. Phần đầu tiên của báo cáo cho thấy giá trị ban đầu của hàm mục tiêu và sau đó là giá trị cuối cùng khi đạt được giải pháp tối ưu. Trong trường hợp này, sản lượng tối ưu sẽ là 18.000 xe tay ga Captain, 5.520 xe Celeritas, 7.000 xe Kicks, và 24.000 xe Lazer.

![ILLUSTRATION 3.29](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.29.png)

Phần giữa của báo cáo (Các ô Biến - Variable Cells) cho thấy giá trị cuối cùng của các biến quyết định (Hình minh họa 3.30). Nó cho thấy số lượng xe tay ga mỗi mẫu mà Super Scooters nên bán để đạt được mức số dư đảm phí tối đa.

![ILLUSTRATION 3.30](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.30.png)

Cuối cùng, phần cuối của báo cáo cho thấy mức độ sử dụng các ràng buộc trong giải pháp tối ưu (Hình minh họa 3.31). Cột Status (Trạng thái) chỉ ra liệu ràng buộc có bị ràng buộc chặt (binding) hay không bị ràng buộc (not binding). Nói cách khác, việc sản xuất thêm là không thể nếu không có sự gia tăng trong mức giới hạn của ràng buộc đó. Số lượng hiển thị trong cột Slack đại diện cho số lượng của ràng buộc còn lại sau giải pháp tối ưu.

![ILLUSTRATION 3.31](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.31.png)

Vì số giờ máy là có hạn, mô hình tối ưu đưa ra cách tốt nhất để sử dụng những giờ đó nhằm tối đa hóa số dư đảm phí là sản xuất tất cả những gì Super Scooters có thể bán cho các mẫu Captain, Kicks và Lazer và sản xuất ít hơn 4.480 chiếc so với nhu cầu của mẫu Celeritas. Bất kỳ sự kết hợp nào khác sẽ dẫn đến số dư đảm phí thấp hơn so với mô hình tối ưu.

#### Phân tích What-if (What-if Analyses)

Một mô hình bảng tính đánh giá những thay đổi và các tổ hợp cụ thể của các đầu vào và giả định của mô hình được gọi là phân tích what-if. Phân tích what-if là một cách dễ dàng để thay đổi các giá trị trong bảng tính và tính toán lại các đầu ra. Microsoft Excel có ba công cụ được tích hợp trong tab Data ở dưới mục What-if Analyses. Hai trong số các công cụ này – Scenario Manager (Quản lý kịch bản) và Goal Seek (Tìm kiếm mục tiêu) – là những công cụ hữu ích để tạo điều kiện cho các phân tích what-if. Chúng ta sẽ thảo luận về từng công cụ trong một chương sau, nhưng đây là một lời giải thích ngắn gọn:
- **Scenario Manager** trong Excel cho phép thay đổi hoặc thay thế các giá trị đầu vào cho nhiều ô (tối đa 32). Do đó, kết quả của các giá trị đầu vào hoặc các kịch bản khác nhau có thể được xem xét cùng một lúc.
- **Goal Seek** được sử dụng khi kết quả mong muốn đã được biết trước nhưng giá trị đầu vào để đạt được kết quả đó thì chưa. Goal Seek bị giới hạn vì nó chỉ có thể sử dụng một biến đầu vào. Nếu phân tích đang được thực hiện yêu cầu nhiều hơn một biến thay đổi, thì một mô hình tối ưu hóa sử dụng Excel Solver là cần thiết. Ví dụ, mô hình tối ưu hóa của Super Scooters có nhiều hơn một biến vì cần phải xem xét các ràng buộc về nhu cầu và số giờ máy.

---

### Ứng dụng 3.5 (Apply It 3.5)
**Đề xuất Tổ hợp Bán hàng Tối ưu (Prescribe Optimal Sales Mix)**

> **Data** **Kế toán Quản trị (Managerial Accounting)** Bạn là một kế toán viên quản trị cho Best Bakes Bakery và được yêu cầu chuẩn bị một bản phân tích để xác định tổ hợp sản phẩm (mix of products) tối ưu nhằm tối đa hóa lợi nhuận. Bạn đã được cung cấp các giao dịch bán hàng cho các năm 2022–2025. Bên cạnh dữ liệu bán hàng trước đó, bạn biết rằng có một số ràng buộc về nguồn lực (chẳng hạn như vật tư hoặc giờ lao động) nên được đưa vào phân tích.

**Yêu cầu:**
1. Mục tiêu của phân tích là gì?
2. Phát triển ba câu hỏi phù hợp với mục tiêu.
3. Bạn sẽ sử dụng những phân tích nào để trả lời ba câu hỏi này?

**GIẢI PHÁP (SOLUTION)**
1. Mục tiêu là xác định tổ hợp bán hàng (sales mix) tối ưu của các sản phẩm dựa trên các nguồn lực có sẵn.
2. Ba câu hỏi:
   - Các ràng buộc về nguồn lực nào nên được đưa vào quyết định?
   - Yêu cầu về nguồn lực cho mỗi sản phẩm là gì?
   - Lợi nhuận dự kiến cho mỗi sản phẩm là bao nhiêu?
3. Tối ưu hóa tuyến tính có thể được sử dụng để xác định sự kết hợp tốt nhất của các sản phẩm để đạt được lợi nhuận tối đa.

---

## 3.6 Động lực và Mục tiêu Phân tích Dữ liệu trong Thực tiễn Nghề nghiệp là gì?

**MỤC TIÊU HỌC TẬP 6 (LEARNING OBJECTIVE 6)**
**Mô tả các động lực và mục tiêu cho phân tích dữ liệu trong thực tiễn nghề nghiệp.**

Trong khi các phương pháp phân tích – mô tả, chẩn đoán, dự đoán và đề xuất – là giống nhau trên các lĩnh vực kế toán, mục tiêu của dự án và những gì thúc đẩy chúng có thể khác nhau do có nhiều mục đích và các bên liên quan khác nhau. Trong kiểm toán, các bên liên quan phần lớn là từ bên ngoài (ví dụ: các cổ đông, các cơ quan quản lý), trong khi các bên liên quan trong kế toán quản trị chủ yếu là từ nội bộ (ví dụ: ban quản lý, nhân viên). Quan điểm của họ giúp xác định mục tiêu và phát triển các câu hỏi tốt.


#### Kiểm toán (Auditing)

Các kiểm toán viên thực hiện phân tích dữ liệu để xác minh thông tin trên báo cáo tài chính không bị sai sót trọng yếu. Mục đích của họ là cung cấp một ý kiến chuyên môn về việc liệu các báo cáo tài chính có cung cấp thông tin đáng tin cậy, chính xác cho các bên liên quan chính của khách hàng, bao gồm các chủ sở hữu công ty, các nhà đầu tư và chủ nợ trên thị trường vốn và các tổ chức tài chính hay không.

#### Hệ thống Thông tin Kế toán (Accounting Information Systems - AIS)

Động lực cho phân tích dữ liệu trong hệ thống thông tin kế toán (AIS) có thể rất đa dạng về phạm vi. Hình minh họa 3.32 tóm tắt các động lực, mục tiêu và câu hỏi điển hình cho phân tích dữ liệu AIS.

![ILLUSTRATION 3.32](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.32.png)

Mặc dù danh sách các câu hỏi trong Hình minh họa 3.32 chưa phải là đầy đủ, nhưng các câu hỏi này là một điểm khởi đầu để tiến hành phân tích nhằm giải quyết chúng.

**ÁP DỤNG TƯ DUY PHẢN BIỆN 3.1: Hiểu Các bên liên quan của AIS (APPLYING CRITICAL THINKING 3.1: Understand AIS Stakeholders)**
Việc hiểu động lực của các bên liên quan giúp xác định chính xác mục tiêu của các phân tích. Các bên liên quan trong các dự án phân tích dữ liệu AIS có thể là nội bộ hoặc bên ngoài tổ chức (Các bên liên quan - Stakeholders):
- Các bên liên quan nội bộ bao gồm giám đốc tài chính (CFO), kiểm toán viên nội bộ, các nhà quản lý, giám đốc thông tin (CIO) và nhân viên. Họ muốn hiểu và cải thiện các quy trình, vì vậy các mục tiêu tập trung vào các khía cạnh cụ thể của các quy trình nội bộ và cách cải thiện chúng.
- Các bên liên quan bên ngoài có thể bao gồm các nhà đầu tư, kiểm toán viên độc lập, khách hàng và nhà cung cấp. Những bên liên quan này bị thúc đẩy bởi việc tăng lợi tức đầu tư (return on investment), do đó, những dự án có tiềm năng mang lại lợi tức đầu tư cao nhất thường được ưu tiên.

Hình minh họa 3.33 bao gồm các ví dụ về động lực, mục tiêu và câu hỏi trong phân tích dữ liệu kiểm toán.

![ILLUSTRATION 3.33](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.33.png)

Lưu ý rằng động lực xác định một khía cạnh cụ thể của cuộc kiểm toán. Mục tiêu nêu rõ đích đến của phân tích. Cột thứ ba trong hình minh họa cung cấp một ví dụ về một câu hỏi cụ thể mà kiểm toán viên có thể giải quyết bằng phân tích. Phân tích kiểm toán được sử dụng để thực hiện đánh giá rủi ro (risk assessment), thủ tục phân tích cơ bản (substantive analytical procedures) và thực hiện các thử nghiệm chi tiết (tests of detail).

**ÁP DỤNG TƯ DUY PHẢN BIỆN 3.2: Thu thập Kiến thức Kiểm toán và Tránh các Thiên kiến (APPLYING CRITICAL THINKING 3.2: Acquire Auditing Knowledge and Avoid Biases)**
Các kiểm toán viên thu thập và áp dụng một số loại thông tin nhất định khi thực hiện phân tích dữ liệu kiểm toán (Kiến thức - Knowledge):
- Ngành nghề, hệ thống quản trị, chính sách và quy trình của khách hàng.
- Các chuẩn mực kế toán và kiểm toán có liên quan, cùng các quy định của SEC.
- Đánh giá rủi ro và các kỹ thuật thống kê, lấy mẫu.

Các kiểm toán viên có thể bị thiên kiến (biased) khi họ đưa ra các giả định về những gì họ mong đợi tìm thấy trong một hợp đồng kiểm toán. Họ phải luôn cảnh giác và hoài nghi về tất cả những thông tin mà họ được cung cấp (Rủi ro - Risks).

#### Kế toán Tài chính (Financial Accounting)

Có một số động lực điển hình cho các kế toán viên tài chính khi thực hiện phân tích dữ liệu:
- Đảm bảo các giao dịch kinh tế, thay đổi giá trị và các bút toán khóa sổ (period closing entries) đã được hệ thống kế toán ghi nhận hợp lý, được định giá ở tài khoản phù hợp và vào đúng kỳ kế toán.
- Dự đoán lợi nhuận thuần (net income) và dòng tiền (cash flows) trong tương lai cho ban quản lý cấp cao.
- Xác định, đánh giá và đảm bảo các nguồn vốn thay thế.

![ILLUSTRATION 3.34](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.34.png)

#### Kế toán Quản trị (Managerial Accounting)

Các kế toán viên quản trị thực hiện phân tích dữ liệu để cải thiện việc ra quyết định của ban quản lý và hiệu suất hoạt động.

Hình minh họa 3.35 cho thấy một số động lực, mục tiêu và câu hỏi điển hình cho các dự án mà kế toán viên quản trị thực hiện.

**ÁP DỤNG TƯ DUY PHẢN BIỆN 3.3: Xem xét Các phương pháp thay thế (APPLYING CRITICAL THINKING 3.3: Consider Alternative Methods)**
Nếu mục tiêu của phân tích là dự đoán thu nhập trong tương lai, thì kế toán viên quản trị có thể sử dụng phân tích hồi quy, đường xu hướng hoặc phân tích what-if. Hãy luôn chọn phương pháp có thể trả lời các câu hỏi một cách hiệu quả và hiệu suất nhất (Các phương án thay thế - Alternatives).

![ILLUSTRATION 3.35](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.35.png)

Hình minh họa 3.34 cho thấy các ví dụ về mục tiêu đối với những động lực này và các câu hỏi có thể giải quyết chúng.

#### Kế toán Thuế (Tax Accounting)

Kế toán thuế thực hiện phân tích dữ liệu để nâng cao chất lượng các lời khuyên và quyết định chuyên môn của họ, cũng như để đáp ứng các yêu cầu tuân thủ cho tổ chức hoặc khách hàng của họ. Các động lực điển hình cho phân tích thuế bao gồm:
- Thực hiện nghiên cứu thuế.
- Thiết kế các kế hoạch thuế.
- Tính toán chính xác nghĩa vụ thuế và hoàn thành các tờ khai thuế (tax returns) tương ứng.

Hình minh họa 3.36 tóm tắt các ví dụ về các mục tiêu liên quan đến những động lực này và một số câu hỏi cụ thể.

![ILLUSTRATION 3.36](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.36.png)

Mặc dù các động lực chung trong phân tích thuế có thể tương tự nhau, nhưng các mục tiêu và câu hỏi sẽ cụ thể cho từng khách hàng cá nhân. Ví dụ, lập kế hoạch thuế là một động lực phổ biến, nhưng khách hàng có thể có các mục tiêu khác nhau đối với kế hoạch thuế của họ, chẳng hạn như tiết kiệm để nghỉ hưu hoặc lập kế hoạch di sản. Mục tiêu của khách hàng sẽ quyết định loại phân tích được thực hiện.

Như chương này đã nhấn mạnh, các chuyên gia kế toán ngày càng thực hiện phân tích dữ liệu nhiều hơn để cung cấp giá trị cho các tổ chức và khách hàng của họ. Dù cho sự nghiệp của bạn đi đến đâu, việc tư duy phản biện về những gì đang thúc đẩy một dự án sẽ giúp bạn đặt ra những câu hỏi phân tích dữ liệu dựa trên mục tiêu tốt nhất để đạt được các đích đến của mình. Đây là hai bước đầu tiên của các dự án phân tích dữ liệu thành công trên mọi lĩnh vực thực hành nghề nghiệp.

---

### Ứng dụng 3.6 (Apply It 3.6)
**Nối các Động lực với Các Lĩnh vực Thực hành Nghề nghiệp (Match Motivations to Professional Practice Areas)**

> Hãy nối ít nhất một chữ viết tắt của lĩnh vực thực hành chuyên môn với các động lực sau đây để thực hiện phân tích dữ liệu.
a. Hệ thống thông tin kế toán (Accounting information systems - AIS)
b. Kiểm toán (Auditing)
c. Kế toán Tài chính (Financial Accounting)
d. Kế toán Quản trị (Managerial Accounting)
e. Kế toán Thuế (Tax Accounting)

**Câu hỏi:**
- Thực hiện nghiên cứu thuế.
- Đầu tư vào các công nghệ mới.
- Thực hiện các thủ tục phân tích đối với các biến động trong số dư tài khoản và trên các nhóm giao dịch.
- Đảm bảo tất cả các giao dịch kinh tế đã được ghi nhận.
- Đầu tư vào các công cụ kinh doanh thông minh (business intelligence tools).
- Gia tăng bảo mật cho các tài sản AIS, bao gồm cả dữ liệu.
- Đổi mới trong các quy trình hoạt động, do con người hay máy tính, để gia tăng tính hiệu quả của quy trình.
- Thiết kế các kế hoạch thuế có thể bảo vệ được (defendable tax plans).
- Tìm hiểu xem liệu tất cả các bút toán điều chỉnh vào cuối kỳ đã được ghi nhận chưa.
- Cải thiện hiệu suất hệ thống, chẳng hạn như thời gian xử lý và tính khả dụng.
- Đánh giá và kiểm tra hệ thống kiểm soát nội bộ.
- Gia tăng bảo mật cho các tài sản AIS, bao gồm cả dữ liệu.
- Tính toán nghĩa vụ thuế và hoàn thành các tờ khai thuế.
- Thực hiện kiểm kê hàng tồn kho vật chất và đếm tài sản cố định vào cuối năm tài chính.
- Kiểm tra tài liệu để xác định xem số dư tài khoản có được hỗ trợ (chứng minh) không.

**GIẢI PHÁP (SOLUTION)**
| **Động lực (Motivation)** | **Lĩnh vực Thực hành (Practice Area)** |
| --- | --- |
| Thực hiện nghiên cứu thuế. | Kế toán thuế |
| Đầu tư vào các công nghệ mới. | AIS |
| Thực hiện các thủ tục phân tích đối với các biến động trong số dư tài khoản và trên các nhóm giao dịch. | Kiểm toán |
| Đảm bảo tất cả các giao dịch kinh tế đã được ghi nhận. | Kế toán tài chính |
| Đầu tư vào các công cụ kinh doanh thông minh. | AIS |
| Gia tăng bảo mật cho các tài sản AIS, bao gồm cả dữ liệu. | AIS |
| Đổi mới trong các quy trình hoạt động, do con người hay máy tính, để gia tăng tính hiệu quả của quy trình. | Kế toán quản trị |
| Thiết kế các kế hoạch thuế có thể bảo vệ được. | Kế toán thuế |
| Tìm hiểu xem liệu tất cả các bút toán điều chỉnh vào cuối kỳ đã được ghi nhận chưa. | Kế toán tài chính |
| Cải thiện hiệu suất hệ thống, chẳng hạn như thời gian xử lý và tính khả dụng. | AIS |
| Đánh giá và kiểm tra hệ thống kiểm soát nội bộ. | Kiểm toán |
| Gia tăng bảo mật cho các tài sản AIS, bao gồm cả dữ liệu. | AIS |
| Tính toán nghĩa vụ thuế và hoàn thành các tờ khai thuế. | Kế toán thuế |
| Thực hiện kiểm kê hàng tồn kho vật chất và đếm tài sản cố định vào cuối năm tài chính. | Kế toán tài chính |
| Kiểm tra tài liệu để xác định xem số dư tài khoản có được hỗ trợ (chứng minh) không. | Kiểm toán |

---

## Đánh giá và Thực hành Chương (Chapter Review and Practice)

### Ôn tập Mục tiêu Học tập (Learning Objectives Review)

**❶ Tóm tắt mối quan hệ giữa động lực, mục tiêu và các câu hỏi phân tích dữ liệu.**
Kế toán viên thường thực hiện phân tích dữ liệu vì bốn lý do:
- Các cơ hội trong tổ chức của họ và trên thị trường.
- Các vấn đề chuyên môn và các yêu cầu từ luật pháp và quy định.
- Giải quyết vấn đề trong tổ chức của họ hoặc cho khách hàng.
- Đánh giá hiệu suất và quy trình đối với công việc của chính họ, hoặc công việc được thực hiện trong tổ chức của họ.

Đầu tiên, xác định mục tiêu, đó là đích đến của phân tích dữ liệu. Sau đó, phát triển các câu hỏi được thiết kế để đạt được đích đến của dự án. Các câu hỏi phân tích dữ liệu có thể được đánh giá dựa trên tính rõ ràng, súc tích và có thể đo lường được:
- Câu trả lời có giải quyết được mục tiêu của phân tích không?
- Câu hỏi có đề cập đến một chủ đề duy nhất không? Nếu không, hãy chia nó thành các câu hỏi phụ.
- Câu hỏi có đo lường được không?
- Các dữ liệu cần thiết để trả lời câu hỏi có sẵn không?

Nếu câu trả lời cho bất kỳ câu hỏi nào trong số này là không, thì hãy sửa đổi câu hỏi hoặc loại bỏ nó.

Sáu khía cạnh của tư duy phản biện có thể giúp chúng ta suy nghĩ về những gì đang thúc đẩy các phân tích dữ liệu và cách phát triển các mục tiêu cũng như câu hỏi:
- Việc hiểu các bên liên quan và góc nhìn của họ giúp xác định động lực của dự án và phát triển các mục tiêu và câu hỏi cụ thể.
- Việc tư duy phản biện thông qua mục đích của phân tích dữ liệu hỗ trợ chuyển từ mục tiêu sang các câu hỏi cụ thể.
- Việc xem xét nhiều phương pháp phân tích thay thế làm tăng khả năng chọn ra phương án tốt nhất cho mục đích.
- Việc nhận thức được các rủi ro tiềm ẩn giúp chúng ta có thể giảm thiểu chúng khi đánh giá động lực, xác định mục tiêu và phát triển câu hỏi.
- Việc cân nhắc những kiến thức nào là cần thiết để hoàn thành dự án thành công bao gồm xác nhận rằng chúng ta đã có kiến thức đó hoặc thực hiện thêm nghiên cứu.
- Việc hiểu tại sao chúng ta thực hiện phân tích dữ liệu cho phép chúng ta vận dụng kinh nghiệm đó vào các bối cảnh và nhiệm vụ phân tích dữ liệu trong tương lai. Xem xét những kinh nghiệm trong quá khứ có thể đẩy nhanh quá trình xác định mục tiêu và phát triển câu hỏi.

**❷ Trình bày cách phát triển các câu hỏi mô tả.**
Các câu hỏi mô tả tập trung vào việc hiểu những gì đang xảy ra ở hiện tại hoặc những gì đã xảy ra trong quá khứ. Chúng được phát triển bằng cách xác định mục tiêu của phân tích và sau đó thiết lập các câu hỏi phụ để thu hẹp trọng tâm. Bước tiếp theo là xác định dữ liệu và phương pháp phân tích để trả lời những câu hỏi đó. Các phương pháp mô tả phổ biến:
- Các thước đo tần suất giúp hiểu các danh mục dữ liệu.
- Các thước đo vị trí (trung bình, trung vị, yếu vị) tiết lộ các quan sát trung bình trong tập dữ liệu.
- Các thước đo độ phân tán (tối thiểu, tối đa, khoảng, phương sai, và độ lệch chuẩn) chỉ ra mức độ thay đổi giữa các quan sát trong tập dữ liệu.
- Các thước đo thay đổi phần trăm cho thấy các khoản tăng và giảm theo tỷ lệ phần trăm so với các kỳ trước và tỷ lệ phần trăm so với tổng số.

**❸ Trình bày cách phát triển các câu hỏi chẩn đoán.**
Các câu hỏi chẩn đoán được xây dựng dựa trên những gì đã học được trong phân tích mô tả và khám phá dữ liệu để tìm nguyên nhân của kết quả. Phân tích chẩn đoán xác định lý do tại sao một kết quả lại xảy ra bằng cách tìm kiếm các điểm bất thường, mối tương quan, khuôn mẫu hoặc xu hướng. Các phân tích chẩn đoán phổ biến:
- Phát hiện điểm bất thường: Biểu đồ phân tán (Scatterplots), biểu đồ thanh (bar charts).
- Tương quan (tuyến tính): Biểu đồ phân tán, tương quan.
- Phát hiện khuôn mẫu: Biểu đồ đường (Line graphs), biểu đồ thanh.
- Phân tích xu hướng: Biểu đồ thanh, biểu đồ đường, đường xu hướng.

**❹ Trình bày cách phát triển các câu hỏi dự đoán.**
Phân tích dự đoán sử dụng dữ liệu quá khứ và hiện tại để dự báo và tạo ra các mô hình (models) nhằm giúp doanh nghiệp đưa ra các dự đoán về tương lai. Việc gia tăng sự sẵn có của dữ liệu và các công cụ phần mềm để thực hiện phân tích dự đoán có nghĩa là nó hiện được sử dụng trong mọi lĩnh vực của kế toán. Để xác định một câu hỏi dự đoán, hãy tự hỏi, "Tôi muốn làm gì với câu trả lời?" Các phân tích phổ biến được sử dụng để trả lời câu hỏi dự đoán:
- Đường xu hướng (Trendlines): Thể hiện các mối quan hệ chức năng cơ bản của dữ liệu.
- Phân tích hồi quy (Regression analysis): Hồi quy tuyến tính xây dựng các mô hình toán học và thống kê để giải thích mối quan hệ giữa một biến phụ thuộc và một hoặc nhiều biến độc lập.

**❺ Trình bày cách phát triển các câu hỏi đề xuất.**
Các mục tiêu đề xuất được xây dựng dựa trên các dự đoán về tương lai và mô tả về hiện tại để xác định quá trình hành động tốt nhất. Các mục tiêu của phân tích đề xuất tập trung vào những gì nên xảy ra. Có hai phương pháp phân tích đề xuất phổ biến:
- Tối ưu hóa (Optimization) là quá trình chọn các giá trị của các biến số giúp tối thiểu hóa hoặc tối đa hóa một lượng cần quan tâm nào đó. Mô hình tối ưu hóa giúp các nhà quản lý phân bổ nguồn lực hiệu quả hơn và ra các quyết định chi phí/lợi nhuận.


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


### Các Câu hỏi Trắc nghiệm (Multiple Choice Questions)

1. **(LO 1)** Động lực trong phân tích dữ liệu kế toán là gì?
   a. Lý do tại sao phân tích đang được thực hiện.
   b. Việc giải thích kết quả của phân tích.
   c. Chỉ dựa trên các yếu tố bên ngoài phân tích.
   d. Chỉ dựa trên việc liệu sự nghiệp của bạn có được hưởng lợi từ việc thực hiện phân tích hay không.

2. **(LO 1)** Một nguồn động lực cho các phân tích dữ liệu trong kế toán liên quan đến cơ hội. Điều nào sau đây là một ví dụ về nguồn động lực từ cơ hội?
   a. Mong muốn sự thành công trong tương lai trên con đường sự nghiệp của bạn.
   b. Xem xét liệu có nên mở rộng sản xuất một sản phẩm mới ra mắt hay không.
   c. Đảm bảo tuân thủ theo tuyên bố mới nhất của FASB.
   d. Xem xét lý do tại sao khối lượng bán hàng của công ty giảm trong một khoảng thời gian.

3. **(LO 1)** Động lực của kế toán viên để thực hiện các phân tích dữ liệu có thể bắt nguồn từ đâu?
   a. Các cơ hội trên thị trường hoặc trong tổ chức.
   b. Những thay đổi trong luật pháp, quy định và các quy tắc nghề nghiệp.
   c. Những dấu hiệu cho thấy có một vấn đề cần được giải quyết.
   d. Cần thực hiện đánh giá các quy trình hoặc hiệu suất.
   e. Bất kỳ điều nào trong số này đều có thể kích hoạt động lực thực hiện phân tích dữ liệu.

4. **(LO 1)** Suy nghĩ phản biện (critical thinking) thông qua động lực để thực hiện các phân tích dữ liệu bao gồm việc xem xét
   a. Các bên liên quan, mục đích, các phương án thay thế, rủi ro, kiến thức và sự tự phản ánh.
   b. Các bên liên quan và mục đích.
   c. Các bên liên quan, mục đích, quản lý rủi ro và các phương án thay thế.
   d. Các bên liên quan, tiếp thu kiến thức, các phương án thay thế và sự tự phản ánh.
   e. Các bên liên quan, quản lý rủi ro, các phương án thay thế và sự tự phản ánh.

5. **(LO 1)** Các phân tích về các bên liên quan và góc nhìn của họ giúp suy nghĩ phản biện về động lực để thực hiện phân tích dữ liệu bởi vì
   a. Nó nhắc nhở bạn ai là người trả lương cho bạn.
   b. Một số người có thể ở bên ngoài tổ chức của bạn.
   c. Việc xem xét các góc nhìn của các bên liên quan giúp xác định mục tiêu và phát triển các câu hỏi tốt.
   d. Các bên liên quan nội bộ không bao giờ nên được xem xét.
   e. Tất cả những điều này là lý do để xem xét các bên liên quan trong quá trình suy nghĩ phản biện của bạn.

6. **(LO 1)** Xem xét một cách phản biện mục đích của việc thực hiện các phân tích dữ liệu
   a. Giúp chúng ta tập trung vào lý do tại sao một thứ gì đó được thực hiện hoặc tạo ra.
   b. Cung cấp dữ liệu miễn phí cho các phân tích.
   c. Tiết lộ các quan điểm của các bên liên quan.
   d. Giúp tránh những thành kiến và giả định.
   e. Không điều nào trong số này liệt kê những lợi ích của suy nghĩ phản biện đối với việc xem xét mục đích của các phân tích dữ liệu.

7. **(LO 1)** Việc thực hiện các phân tích dữ liệu phù hợp nhất sẽ có nhiều khả năng xảy ra hơn nếu bạn suy nghĩ phản biện về các vấn đề bằng cách
   a. Sử dụng biểu đồ thanh (bar charts) từ kết quả hoạt động của năm ngoái.
   b. Bắt đầu với các kết quả mà bạn muốn đạt được.
   c. Trả tiền cho những người khác để giúp bạn.
   d. Tiếp thu và áp dụng kiến thức mới.
   e. Không có cách nào trong số này giúp bạn thực hiện phân tích dữ liệu tốt hơn.

8. **(LO 1)** Suy nghĩ một cách phản biện về những rủi ro đối với góc nhìn của bạn khi xác định động lực thực hiện phân tích dữ liệu giúp bạn giảm thiểu
   a. Lỗi do những thành kiến.
   b. Lỗi do thiếu kinh nghiệm.
   c. Lỗi do những giả định của bạn.
   d. Những kết luận sai lầm từ các lỗi hoặc thiếu sót trong dữ liệu của bạn.
   e. Tất cả những điều này là những lợi ích của việc xem xét những rủi ro đối với các lựa chọn phân tích dữ liệu của bạn.

9. **(LO 1)** Việc xem xét nhiều phương pháp phân tích thay thế (alternative methods) giúp bạn
   a. Đi theo phương án thay thế đầu tiên xuất hiện trong đầu.
   b. Chọn tùy chọn tốt nhất cho mục đích của dự án.
   c. Chọn phương án thay thế có chi phí tăng thêm cao nhất.
   d. Chọn phương án thay thế có khả năng mang lại kết quả cung cấp thông tin thấp nhất.

10. **(LO 2)** Nếu mục tiêu của phân tích dữ liệu là hiểu những gì đang xảy ra ở hiện tại hoặc đã xảy ra trong quá khứ, thì bạn đang hỏi loại câu hỏi nào?
    a. Mô tả (Descriptive)
    b. Chẩn đoán (Diagnostic)
    c. Dự đoán (Predictive)
    d. Đề xuất (Prescriptive)

11. **(LO 2)** Khi bạn đã trình bày rõ ràng một câu hỏi mô tả, loại phân tích nào là cần thiết để hiểu sự phân tán của dữ liệu?
    a. Trung vị (Median)
    b. Tần suất (Frequency)
    c. Độ lệch chuẩn (Standard deviation)
    d. Thay đổi phần trăm (Percent change)

12. **(LO 2)** Giả sử bạn dự định thực hiện phân tích mô tả về chi phí bảo trì của đơn vị mình. Phân tích nào sau đây sẽ giúp hiểu rõ các danh mục chi phí bảo trì?
    a. Tạo một bảng phân phối tần suất dựa trên các danh mục chi phí bảo trì.
    b. Tính chi phí bảo trì trung bình (mean) và trung vị (median) cho kỳ kế toán.
    c. Xây dựng một mô hình hồi quy sử dụng số giờ lao động làm yếu tố dự đoán chi phí bảo trì.
    d. Tính phần trăm thay đổi của chi phí bảo trì so với năm trước.
    e. Không có phân tích nào trong số này được coi là phân tích mô tả dùng để hiểu các danh mục chi phí bảo trì.

13. **(LO 3)** Câu hỏi "Điều gì đang dẫn đến sự gia tăng trong chi phí nhân công?" là loại câu hỏi nào?
    a. Mô tả (Descriptive)
    b. Chẩn đoán (Diagnostic)
    c. Dự đoán (Predictive)
    d. Đề xuất (Prescriptive)

14. **(LO 3)** Câu hỏi phụ "Có bất kỳ giao dịch bán hàng bất thường nào trong năm 2023 không?" gắn liền nhất với mục tiêu phân tích dữ liệu nào sau đây?
    a. Số tiền bán hàng trung bình bằng đô la trong năm 2023 là bao nhiêu?
    b. Yếu tố dự báo tốt nhất về việc tăng doanh thu cho các kỳ tương lai là gì?
    c. Tại sao doanh số lại giảm trong năm 2023?
    d. Số tiền bán hàng tối thiểu và tối đa bằng đô la trong năm 2023 là bao nhiêu?

15. **(LO 4)** Câu hỏi "Doanh thu năm tới sẽ là bao nhiêu nếu chúng ta tăng doanh số bán hàng lên 10%?" là loại câu hỏi nào?
    a. Mô tả (Descriptive)
    b. Chẩn đoán (Diagnostic)
    c. Dự đoán (Predictive)
    d. Đề xuất (Prescriptive)

16. **(LO 4)** Câu hỏi nào sau đây là câu hỏi được hỏi trong phân tích dự đoán?
    a. Có những thay đổi bất thường nào trong tổng doanh thu từ năm 2021 đến 2024 không?
    b. Số tiền bán hàng trung bình cho các khách hàng trực tuyến mỗi năm là bao nhiêu?
    c. Doanh thu sẽ bị ảnh hưởng như thế nào nếu chúng ta giảm 5% chi phí biến đổi (variable costs)?
    d. Bao nhiêu doanh thu được phân loại là doanh thu từ doanh nghiệp đến doanh nghiệp (business-to-business)?

17. **(LO 5)** Câu hỏi "Mỗi tháng chúng ta nên mua bao nhiêu đơn vị sản phẩm để tối thiểu hóa chi phí lưu trữ hàng tồn kho nhưng vẫn đáp ứng được nhu cầu?" là loại câu hỏi nào?
    a. Mô tả (Descriptive)
    b. Chẩn đoán (Diagnostic)
    c. Dự đoán (Predictive)
    d. Đề xuất (Prescriptive)

18. **(LO 5)** Trong một mô hình tối ưu hóa, điều gì đang được xác định?
    a. Các ràng buộc (Constraints)
    b. Các biến quyết định (Decision variables)
    c. Hàm mục tiêu (Objective function)
    d. Số lượng cần sản xuất

19. **(LO 6)** Các kế toán viên AIS có khả năng cao nhất được tạo động lực để thực hiện phân tích dữ liệu cho các cơ hội nào sau đây?
    a. Các công nghệ mới có thể cung cấp việc tiết kiệm chi phí cho các quy trình hoạt động.
    b. Các khách hàng mới trên thị trường.
    c. Sự luân chuyển vị trí trong bộ phận lãnh đạo cơ quan quản lý.
    d. Những thay đổi đối với các công bố trên thuyết minh (footnote disclosures) theo yêu cầu của các nguyên tắc kế toán được chấp nhận chung.
    e. Những thay đổi trong các quy tắc thuế.

20. **(LO 6)** Động lực để thực hiện các phân tích dữ liệu của các kiểm toán viên sẽ cao đối với tình huống nào sau đây?
    a. Đánh giá tính hiệu quả của các kiểm soát nội bộ trong hệ thống kế toán của khách hàng họ.
    b. Đánh giá tính đầy đủ của số dư một tài khoản trên bảng cân đối kế toán hoặc báo cáo kết quả hoạt động kinh doanh của khách hàng.
    c. Xem xét rủi ro sai sót trọng yếu trong việc lập kế hoạch hợp đồng (engagement planning).
    d. Tổng hợp và phân tích các biến chính trong một hợp đồng thông minh (smart contract) để đánh giá xem liệu khách hàng có ghi nhận các khoản nợ thuê tài sản của họ theo quy định của GAAP hay không.
    e. Tất cả đều là những ví dụ về các tình huống mà kiểm toán viên có động lực thực hiện các phân tích dữ liệu.

21. **(LO 6)** Các kế toán tài chính sẽ có khả năng cao nhất được tạo động lực thực hiện các phân tích dữ liệu cho tình huống nào sau đây?
    a. Những thay đổi đối với đội ngũ quản lý.
    b. Những đối thủ cạnh tranh mới trên thị trường.
    c. Xác định và hỗ trợ (chứng minh) các giả định và ước tính cho các bút toán điều chỉnh cuối kỳ.
    d. Những thay đổi về thuế suất áp dụng cho tổ chức của họ.
    e. Không có điều nào trong số này sẽ thúc đẩy các phân tích dữ liệu bởi các kế toán tài chính.

22. **(LO 6)** Các kế toán viên quản trị sẽ có khả năng cao nhất được tạo động lực để thực hiện các phân tích dữ liệu cho tình huống nào sau đây?
    a. Những thay đổi về mã luật thuế (tax code).
    b. Những thay đổi trong các quy tắc công bố thuyết minh báo cáo tài chính.
    c. Những thay đổi đối với các quy định về báo cáo của Ủy ban Chứng khoán và Giao dịch (SEC).
    d. Những thay đổi đối với các chiến lược, hiệu suất và chi phí nguồn lực của tổ chức họ.
    e. Không có điều nào trong số này sẽ thúc đẩy các phân tích dữ liệu bởi các kế toán viên quản trị.

---

### Các Câu hỏi Ôn tập (Review Questions)

1. **(LO 1)** Thảo luận về các động lực sau đây đối với các phân tích dữ liệu trong kế toán bằng cách đưa ra một ví dụ cho mỗi động lực:
   1. Các cơ hội
   2. Các vấn đề chuyên môn và các yêu cầu
   3. Giải quyết vấn đề
   4. Đánh giá quy trình và hiệu suất

2. **(LO 1, 6)** So sánh và đối chiếu các xem xét chuyên môn và các yêu cầu tạo động lực cho các kế toán tài chính và kế toán quản trị thực hiện các phân tích dữ liệu.

3. **(LO 2, 4)** Giả sử bạn là một nhà phân tích tài chính tại một thực thể không đại chúng (non-public entity). Người giám sát của bạn đã yêu cầu bạn tính toán và phân tích các tỷ số khả năng thanh toán nợ trong 5 năm qua. Bạn lưu ý rằng có một số bên liên quan gắn với bản phân tích này, bao gồm người quản lý của bạn và ngân hàng đang nắm giữ khoản nợ của thực thể. Hãy đưa ra một ví dụ về việc làm thế nào hai bên liên quan này có thể bị tác động theo những cách khác nhau bởi các kết quả phân tích dữ liệu của bạn.

4. **(LO 1, 4)** Là một kiểm toán viên được phân công kiểm toán một công ty đại chúng trong ngành sản xuất, bạn được yêu cầu phân tích hàng tồn kho của công ty để hiểu các loại sản phẩm trong kho và cơ cấu nguyên vật liệu, sản phẩm dở dang và thành phẩm. Bạn nhận được file hàng tồn kho hiện có từ bộ phận công nghệ thông tin. Hãy xác định những kiến thức bạn có thể cần phải tiếp thu hoặc áp dụng cho phân tích này, điều có thể đóng góp vào động lực thực hiện nó của bạn.

5. **(LO 2)** Giả sử bạn đang thực hiện phân tích mô tả về dữ liệu hoàn trả chi phí cho nhân viên của công ty bạn trong năm tài chính hiện tại so với năm tài chính trước đó. Đưa ra một ví dụ về câu hỏi ban đầu liên quan đến phân tích này.

6. **(LO 2)** Là một kiểm toán viên làm việc trong nhóm kiểm toán nội bộ, bạn được yêu cầu thực hiện phân tích mô tả về các lần thử đăng nhập của nhân viên trong giờ làm việc và ngoài giờ làm việc. Mục tiêu của bạn là hiểu xem liệu số lượng các lần thử đăng nhập thất bại đã tăng hay giảm. Câu hỏi ban đầu của bạn là "Các nỗ lực đăng nhập có tăng lên không?" Đưa ra một ví dụ về một câu hỏi phụ có thể giải quyết mục tiêu và câu hỏi ban đầu cho phân tích mô tả đó.

7. **(LO 3)** Giải thích cách các kế toán viên có thể sử dụng phân tích chẩn đoán để xác định lý do tại sao một kết quả đã xảy ra.

8. **(LO 3)** Giám đốc tài chính (controller) công ty đã yêu cầu bạn thực hiện phân tích chẩn đoán về doanh số sản phẩm của công ty để hiểu tại sao doanh số tăng so với năm trước. Câu hỏi ban đầu của bạn là "Điều gì đang thúc đẩy khối lượng bán hàng tăng?" Xác định hai câu hỏi phụ cần xem xét khi bạn lập kế hoạch cho phân tích của mình.

9. **(LO 2, 4)** Mô tả sự khác biệt giữa các mục tiêu dự đoán và mục tiêu mô tả trong phân tích kế toán.

10. **(LO 4)** Định nghĩa các thuật ngữ biến phụ thuộc và biến độc lập. Các biến này được sử dụng như thế nào trong phân tích dự đoán?

11. **(LO 5)** Định nghĩa và giải thích về tối ưu hóa và phân tích what-if. Tại sao hai loại phân tích này được coi là phân tích đề xuất?

12. **(LO 5)** Giả sử bạn là một nhà phân tích tài chính làm việc cho một công ty sản xuất. Công ty của bạn sản xuất và bán nhiều loại linh kiện cho xe điều khiển từ xa cao cấp. Danh mục sản phẩm của bạn bao gồm ba sản phẩm phổ biến:
    - Bánh răng kim loại (Metal Gear)
    - Mô-men xoắn cao 330 (High-Torque 330)
    - Mô-men xoắn cao 400 (High-Torque 400)
    Giám đốc tài chính (controller) của bạn đã yêu cầu bạn xác định tổ hợp sản phẩm mang lại lợi nhuận cao nhất. Cung cấp một ví dụ về một câu hỏi ban đầu và câu hỏi phụ có thể định hướng cho kế hoạch phân tích của bạn.

13. **(LO 6)** Là một kế toán viên hệ thống thông tin kế toán (AIS), hãy xác định các bên liên quan chính mà bạn ưu tiên khi thực hiện các phân tích dữ liệu.

14. **(LO 6)** Những động lực chính của kiểm toán viên độc lập (external auditors) để thực hiện các phân tích dữ liệu là gì?

15. **(LO 6)** Giám đốc tài chính của bạn đã yêu cầu bạn chuẩn bị các bút toán điều chỉnh cho quá trình khóa sổ cuối tháng. Hãy thảo luận tại sao một kế toán báo cáo tài chính có thể tham gia vào phân tích dữ liệu khi họ chuẩn bị các bút toán điều chỉnh.

16. **(LO 6)** Các kế toán thuế thường xem xét các phương án thay thế khi quyết định liệu họ có động lực thực hiện các phân tích dữ liệu hay không. Thảo luận về một số phương án thay thế có thể cải thiện các quyết định của họ.

---

### Các Bài tập Ngắn (Brief Exercises)

**BE 3.1 (LO 1)** Ghép các sự kiện sau đây với loại động lực thực hiện phân tích dữ liệu tương ứng.
a. Sự gia tăng chi phí đáng kể
b. Các thành tựu hàng năm
c. Chuyên môn ngành mới
d. Chuẩn mực mới cho hợp đồng thuê tài sản (leases)
- 1. Cơ hội
- 2. Quy định hoặc luật pháp
- 3. Vấn đề
- 4. Đánh giá quy trình hoặc hiệu suất

**BE 3.2 (LO 1–6) Hệ thống Thông tin Kế toán** Giả sử bạn là một chuyên gia hệ thống thông tin kế toán được giao nhiệm vụ thực hiện một số phân tích liên quan đến các biện pháp kiểm soát bảo mật thông tin của công ty bạn. Hãy ghép loại phân tích với tình huống động lực tương ứng (các loại phân tích có thể được sử dụng nhiều lần).
a. Phân tích mô tả
b. Phân tích chẩn đoán
c. Phân tích dự đoán
d. Phân tích đề xuất
- 1. Phân tích số lần đăng nhập thất bại trung bình (mean), trung vị (median) và yếu vị (mode) sau khi công ty thay đổi các yêu cầu về mật khẩu để hiểu liệu lợi ích của các yêu cầu mật khẩu nâng cao có lớn hơn chi phí hay không.
- 2. Phân tích mối tương quan giữa số lượng nỗ lực lừa đảo (phishing) được báo cáo và sự tham gia của nhân viên vào các khóa đào tạo an ninh mạng để xác định xem việc đào tạo có liên quan đến việc báo cáo các hành vi lừa đảo hay không.
- 3. Phân tích các xu hướng về số lần đăng nhập thất bại theo thời gian để xác định xem nhân viên có tuân thủ chính sách của công ty về thông tin xác thực đăng nhập hay không.
- 4. Thực hiện phân tích hồi quy tuyến tính để xem xét khả năng xảy ra các vụ vi phạm bảo mật thông tin trong tương lai dựa trên các biến độc lập là số tiền đã chi tiêu cho hoạt động đào tạo an ninh mạng và phần mềm mã hóa.
- 5. Thực hiện phân tích what-if để xác định số tiền chi tiêu phù hợp cần thiết nhằm đáp ứng các mục tiêu về bảo mật thông tin của thực thể.

**BE 3.3 (LO 1, 6)** Nối nguồn động lực cho các phân tích dữ liệu trong kế toán chuyên nghiệp với tình huống thích hợp. Mỗi nguồn có thể được sử dụng một lần, nhiều lần hoặc không được sử dụng.
a. Cơ hội
b. Đánh giá quy trình và hiệu suất
c. Những thay đổi về quy định
d. Giải quyết vấn đề
- 1. Bạn là một kế toán thuế làm việc tại một công ty đa quốc gia lớn. Ban giám đốc điều hành đang cố gắng quyết định quốc gia tốt nhất để mở rộng hoạt động. Bạn được giao nhiệm vụ xác định các biến độc lập và thực hiện phân tích hồi quy để dự đoán doanh thu tiềm năng từ việc mở rộng này.
- 2. Công ty của bạn có một số chỉ số đo lường hiệu suất chính (KPI) gắn với quy trình sản xuất của nó – đặc biệt là kiểm soát chất lượng. Bạn được giao nhiệm vụ thực hiện một phân tích để xác định xem các tiêu chuẩn kiểm soát chất lượng có được ghi chép chính xác trong hệ thống thông tin hay không.
- 3. Bạn là một kiểm toán viên độc lập làm việc với một khách hàng sản xuất thuộc loại công ty đại chúng. Bạn đã được yêu cầu kiểm tra tính hiệu quả hoạt động của các kiểm soát nội bộ liên quan đến sự tuân thủ của nhóm mua hàng đối với quy định kiểm soát nội bộ rằng mọi đơn đặt hàng mua (purchase orders) trên 10.000 đô la đều phải được người giám sát mua hàng phê duyệt.
- 4. Bạn là một nhà phân tích tài chính làm việc cho một công ty phân phối các sản phẩm tiêu dùng tới các nhà bán lẻ trên khắp Hoa Kỳ. Bạn phải tìm hiểu lý do tại sao doanh số của sản phẩm thường phổ biến nhất từ trước đến nay của bạn, lò nướng điện (electric grill), lại bị sụt giảm.

**BE 3.4 (LO 2, 6) Kiểm toán** Là một trưởng nhóm kiểm toán (audit senior), bạn đã yêu cầu thực tập sinh của mình thực hiện một phân tích mô tả về các chi phí bảo trì của công ty trong thời kỳ kiểm toán. Bạn nhắc nhở thực tập sinh rằng trước tiên họ phải xác định mục đích của phân tích và sau đó chia nó thành các câu hỏi. Thực tập sinh đang lo lắng và tự hỏi làm thế nào họ biết được liệu họ đã phát triển được một câu hỏi mô tả tốt hay chưa. Hãy điền vào chỗ trống để hoàn thành một phản hồi cho mối bận tâm của thực tập sinh. Mỗi thuật ngữ có thể được sử dụng một lần, nhiều lần, hoặc không được sử dụng.
> Ngân hàng từ: mục tiêu (objective), cụ thể (specific), có sẵn (available), khát vọng (aspirational), chính xác (accurate), đáng kể (considerable), độc quyền (exclusive), mơ hồ (ambiguous)

Một câu hỏi tốt là một câu hỏi liên quan đến ___________, mang tính ___________, có thể đo lường được, và có thể được trả lời bằng những dữ liệu ___________.

**BE 3.5 (LO 2) Kế toán Tài chính** Bạn là một kế toán tài chính làm việc cho thành phố. Giám đốc tài chính (controller) của bạn muốn hiểu rõ hơn về các khoản thanh toán cho nhà cung cấp (vendor payments) được thực hiện bởi thành phố. Bạn đã tải xuống file thanh toán cho nhà cung cấp của các năm tài chính 2024 và 2025 từ cơ sở dữ liệu của thành phố. Một đoạn trích của dữ liệu đó đã được cung cấp (xem sách giáo khoa).
1. Mục tiêu của phân tích là gì?
2. Phát triển ba câu hỏi phù hợp với mục tiêu, và xác định các thước đo nào bạn sẽ sử dụng để trả lời các câu hỏi đó.
3. Bạn sẽ sử dụng những phân tích nào để trả lời ba câu hỏi này?

**BE 3.6 (LO 2, 6) Kế toán Quản trị** Hãy ghép phân tích phù hợp có thể được sử dụng để trả lời các câu hỏi mô tả hoặc các câu hỏi phụ. Mỗi lựa chọn phân tích có thể được sử dụng một lần, nhiều lần hoặc không được sử dụng.
a. Lọc dữ liệu để chỉ phân tích cái máy đang quan tâm và sử dụng hàm maximum.
b. Sử dụng các hàm minimum và maximum để xác định số lượng đơn vị được sản xuất ít nhất và nhiều nhất.
c. Lọc dữ liệu để chỉ phân tích đơn vị sản phẩm đang quan tâm và cái máy đang quan tâm và tính số đơn vị sản phẩm trung bình (mean) được sản xuất cho mỗi ca.
d. Tạo một phương trình tuyến tính để ước tính số giờ máy cần thiết để sản xuất một đơn vị sản phẩm.
e. Sử dụng tính năng mô hình tối ưu hóa trong Excel để xác định số lượng đơn vị sản phẩm tối đa có thể được sản xuất với hạn chế về thời gian trong ca làm việc.
f. Tạo một bảng phân phối tần suất để phân loại các danh mục sản phẩm.
- 1. Có bao nhiêu đơn vị đã được sản xuất cho mỗi danh mục sản phẩm trong cơ sở sản xuất?
- 2. Số đơn vị trung bình do máy #1.065 sản xuất trong ca 1, ca 2 và ca 3 là bao nhiêu?
- 3. Số đơn vị lớn nhất mà máy #1.810 đã sản xuất là bao nhiêu?
- 4. Khoảng phân tán (range) của các đơn vị được sản xuất trong kỳ là bao nhiêu?

**BE 3.7 (LO 3) Kiểm toán** Bạn là một kiểm toán viên nội bộ tại một công ty sản xuất và bán xe hơi điều khiển từ xa. Bạn đã được yêu cầu thực hiện một phân tích để xem liệu có những khoản mua hàng bất thường từ các nhà cung cấp trong kỳ hay không. Nhóm công nghệ thông tin của bạn đã cung cấp cho bạn một file giao dịch chứa tất cả các giao dịch mua được thực hiện trong kỳ. Một đoạn trích của file đã được cung cấp (xem sách giáo khoa).
1. Mục tiêu của phân tích là gì?
2. Phát triển ba câu hỏi phù hợp với mục tiêu.
3. Bạn sẽ sử dụng những phân tích nào để trả lời ba câu hỏi này?

**BE 3.8 (LO 3) Kiểm toán** Là một kiểm toán viên cho một công ty tư nhân, senior (kiểm toán viên chính) của bạn đã yêu cầu bạn kiểm tra số lượng hàng bán bị trả lại (sales returns) của khách hàng trong vòng 30 ngày đầu tiên sau thời điểm khóa sổ cuối năm. Phân tích mô tả đã tiết lộ hàng bán bị trả lại giảm mạnh so với năm trước. Hơn nữa, bạn lưu ý rằng mức giảm lớn nhất liên quan đến hàng bán bị trả lại là ở khu vực Tây Bắc (northwest region). Bạn phải thực hiện các phân tích chẩn đoán để hiểu lý do tại sao lại có sự sụt giảm ở khoản mục hàng bán bị trả lại này.
Dưới đây là dàn ý của mục tiêu phân tích dữ liệu, câu hỏi ban đầu, câu hỏi phụ, và các thước đo khả thi. Hoàn thành dàn ý bằng cách ghép câu phát biểu thích hợp vào ô trống tương ứng (xem sách giáo khoa). Các lựa chọn câu phát biểu có thể được dùng một lần, nhiều lần, hoặc không dùng.
a. Điều gì đang dẫn đến việc giảm hàng bán bị trả lại?
b. Có các khuôn mẫu bất thường nào trong hàng bán bị trả lại ở khu vực Tây Bắc đối với các dòng sản phẩm nhất định không?
c. Tạo một phân tích xu hướng hiển thị các khoản hoàn trả theo ngày cho mỗi dòng sản phẩm trong năm hiện tại so với năm trước.
d. Lọc dữ liệu để cô lập các khoản hàng bán bị trả lại ở khu vực Tây Bắc và xem xét tổng số tiền trả lại, khoản tiền trả lại trung bình và số lượng trả lại.
e. Tạo một mô hình tối ưu hóa để xác định số lượng hàng bán bị trả lại thích hợp nhất với các ràng buộc về doanh số và số lượng được sản xuất.
f. Tính độ lệch chuẩn của doanh thu và so sánh với độ lệch chuẩn của các chi phí nhân viên trong kỳ.
g. Tính tổng chi tiêu của công ty vào các dịch vụ khách hàng để xác định xem liệu hàng bán bị trả lại có liên quan đến chất lượng sản xuất hay không.

**BE 3.9 (LO 4)** Ghép nối các phân tích với các mô tả của chúng. Mỗi thuật ngữ có thể được sử dụng một lần, nhiều lần, hoặc không được sử dụng.
a. Biến độc lập (Independent variable)
b. Hàm tuyến tính (Linear function)
c. Thống kê hồi quy (Regression statistics)
d. Hệ số tương quan (Correlation coefficient)
e. Biến phụ thuộc (Dependent variable)
f. Adjusted R² (R² điều chỉnh)
- 1. Các thước đo thống kê được dùng để đánh giá mô hình hồi quy.
- 2. Biến đầu ra trong một mô hình hồi quy.
- 3. Biến hay các biến ảnh hưởng đến biến đầu ra.
- 4. Loại quan hệ này cho thấy mức tăng hoặc giảm đều đặn trên toàn bộ phạm vi của biến độc lập.
- 5. Số liệu thống kê này đo lường sức mạnh của mối quan hệ giữa biến phụ thuộc và biến độc lập.
- 6. Số liệu thống kê này giải thích độ phù hợp của đường hồi quy so với dữ liệu.

**BE 3.10 (LO 4)** Mục tiêu là thực hiện các phân tích dự đoán. Đối với mỗi câu hỏi ban đầu hoặc câu hỏi phụ sau đây, hãy xác định biến độc lập và biến phụ thuộc.
1. Doanh thu sẽ thay đổi bao nhiêu với mức tăng 15% trong khối lượng bán hàng?
2. Doanh thu sẽ tăng bao nhiêu với mức tăng 10% trong khối lượng sản xuất?
3. Các chi phí bảo trì sẽ thay đổi bao nhiêu nếu chúng ta tăng khối lượng sản xuất lên 5%?
4. Khi tình trạng thất nghiệp tăng, thì khối lượng bán hàng sẽ giảm đi bao nhiêu?
5. Khi số lượng nhân viên tăng, các chi phí an ninh thông tin sẽ tăng bao nhiêu?

**BE 3.11 (LO 4, 6) Hệ thống Thông tin Kế toán** Giả sử bạn là một kế toán viên thuộc hệ thống thông tin kế toán được yêu cầu xem xét sự thành công trong chương trình đào tạo an ninh mạng của công ty bạn. Bạn đã thu thập dữ liệu về số giờ đào tạo an ninh mạng được cung cấp hàng tháng cho nhân viên và số lượng các mối đe dọa không gian mạng đã được báo cáo. Bạn đã tạo ra một biểu đồ đường xu hướng (xem sách giáo khoa). Sử dụng thông tin được cung cấp trong biểu đồ đường và phương trình để trả lời các câu hỏi sau:
1. Nếu công ty cung cấp 9 giờ đào tạo trên không gian mạng trong một khoảng thời gian, số lượng các mối đe dọa không gian mạng (cybersecurity threats) được báo cáo bởi nhân viên là bao nhiêu?
2. Nếu công ty cung cấp 35 giờ đào tạo trên không gian mạng trong một khoảng thời gian, số lượng các mối đe dọa không gian mạng được báo cáo bởi nhân viên là bao nhiêu?

**BE 3.12 (LO 5)** Nối các thuật ngữ thích hợp với mỗi định nghĩa. Các thuật ngữ có thể được dùng một lần, nhiều lần, hoặc không được dùng.
a. Các ràng buộc (Constraints)
b. Hàm mục tiêu (Objective function)
c. Biến quyết định (Decision variable)
d. Tối ưu hóa (Optimization)
e. Hồi quy tuyến tính (Linear regression)
f. Biến phụ thuộc (Dependent variable)
g. Biến độc lập (Independent variable)
- 1. Quá trình chọn lựa các giá trị của các biến làm giảm thiểu hoặc tối đa hóa một đại lượng quan tâm nào đó.
- 2. Các giá trị chưa biết mà một mô hình tìm cách để xác định.
- 3. Phương trình toán học mô tả đầu ra mục tiêu mà chúng ta tìm cách giảm thiểu hoặc tối đa hóa.
- 4. Những hạn chế, yêu cầu, hoặc các giới hạn khác phải được áp dụng lên bất kỳ giải pháp nào.

**BE 3.13 (LO 5, 6) Kế toán Quản trị** Là một kế toán viên quản trị cho một công ty sản xuất, bạn được yêu cầu xác định số lượng đơn vị tối ưu phải được sản xuất để tối đa hóa số dư đảm phí (contribution margin - CM) của công ty. Công ty của bạn sản xuất bốn loại đơn vị khác nhau: Standard widgets, Blue flying widgets, Red swimming widgets, Yellow hopping widgets. Để thực hiện phân tích đề xuất, người quản lý của bạn đã xây dựng một bảng tính (spreadsheet) cho bạn để chạy chức năng Microsoft Excel Solver (xem sách giáo khoa).
1. Biến quyết định (decision variable) trong mô hình là gì?
2. Các ràng buộc (constraints) trong mô hình là gì?
3. Hàm mục tiêu (objective function) là gì?

**BE 3.14 (LO 5, 6) Kế toán Tài chính** Công ty tư nhân của bạn muốn mở rộng và phát triển một dòng sản phẩm mới; tuy nhiên, sự tăng trưởng đó đòi hỏi cần gia tăng vốn và đầu tư vào tài sản vật chất, con người, và nguyên vật liệu. Bạn được yêu cầu xem xét chiến lược phù hợp nhất để thu hút được số vốn cần thiết. Bạn đã tình nguyện tham gia vào phân tích dữ liệu để cung cấp góc nhìn sâu sắc cho cuộc thảo luận.
1. Mục tiêu của phân tích là gì?
2. Phát triển hai câu hỏi phù hợp với phân tích.
3. Bạn sẽ sử dụng những phân tích nào để trả lời cho từng câu hỏi?

**BE 3.15 (LO 6)** Hãy xác định xem liệu người có chuyên môn đã phát triển một câu hỏi có thể đo lường được và cụ thể, thích hợp cho lĩnh vực thực hành (practice area) đó hay chưa.
1. Một kiểm toán viên báo cáo tài chính hỏi: "Giá trị kỳ vọng của việc khách hàng phát hành cổ phiếu dựa trên giá thị trường hiện tại là bao nhiêu?"
2. Một kế toán viên thuộc hệ thống thông tin kế toán hỏi: "Công ty nên sản xuất bao nhiêu đơn vị sản phẩm để tối ưu hóa số dư đảm phí của công ty?"
3. Một kế toán thuế đặt ra câu hỏi: "Dựa trên tờ khai thuế năm ngoái, những thay đổi trong luật thuế năm nay sẽ ảnh hưởng như thế nào đến nghĩa vụ thuế của khách hàng?"
4. Một kế toán viên quản trị xem xét "Những sản phẩm nào sử dụng số lượng nguyên vật liệu thô cao nhất trong sản xuất?"
5. Một kế toán tài chính tự hỏi "Số tiền theo đô la của các khoản phải thu nào được phân loại trong mục chưa thanh toán quá 90 ngày?"

**BE 3.16 (LO 6)** Ghép mỗi phát biểu với lĩnh vực thực hành nghề nghiệp kế toán phù hợp nhất. Mỗi lĩnh vực thực hành nghề nghiệp kế toán có thể được sử dụng một lần, nhiều lần, hoặc không được sử dụng.
a. Hệ thống thông tin kế toán
b. Kế toán tài chính
c. Kế toán quản trị
d. Kiểm toán
e. Kế toán thuế
- 1. Simone và nhóm công nghệ thông tin đang điều tra khả năng đầu tư vào các công nghệ mới.
- 2. Chung muốn cải thiện hiệu suất hệ thống thông tin của công ty và đang đánh giá thời gian xử lý để chuẩn bị các báo cáo quản lý cuối tháng.
- 3. Christine muốn xác định các giao dịch bán hàng bất thường có thể đã góp phần vào sự gia tăng bất ngờ trong doanh thu của khách hàng so với năm ngoái.
- 4. Daniel hiện đang sử dụng tính năng Scenario Manager trong Excel để xác định lãi suất, điều khoản thanh toán, và thời hạn của khoản vay để đánh giá các chiến lược yêu cầu vốn khác nhau.
- 5. Ellis đang phân tích việc tính toán nghĩa vụ thuế của một khách hàng để xác định xem liệu có các chi phí nào chưa được gộp vào khoản khấu trừ một cách hợp lý hay không.
- 6. Pierre hiện đang kiểm tra mối quan hệ giữa số giờ máy và chi phí bảo trì để dự đoán về những thay đổi trong việc sản xuất.
- 7. Mica đang thực hiện phân tích hồi quy để ước tính doanh thu hàng tháng dự kiến cho một khách hàng bán lẻ. Sau đó, anh sẽ so sánh doanh thu hàng tháng dự kiến với số tiền được ghi nhận của khách hàng.

---

### Các Bài tập (Exercises)

**EX 3.1 (LO 2, 6) Kế toán Tài chính - Phân tích các Thước đo (Analysis of Measures)** Là giám đốc tài chính (controller) công ty cho một công ty cung cấp hàng sản xuất sợi, bạn được yêu cầu kiểm tra doanh số bán hàng cho từng khách hàng trong tháng 6 năm 2025. Bạn đã đánh giá các mục tiêu và câu hỏi trong phân tích của mình một cách phản biện và lập tài liệu về chúng (xem bảng trong sách). Sử dụng dữ liệu có sẵn để thực hiện các phân tích được đề xuất trong phần "Các Thước đo Khả thi" của kế hoạch phân tích.

**EX 3.2 (LO 2, 6) Kế toán Quản trị - Phân tích các Thước đo** Công ty của bạn sản xuất sợi chất lượng cao để bán tại các cửa hàng thủ công, cửa hàng đồ sợi và các cửa hàng chuyên biệt trên toàn quốc. Cụ thể, cơ sở của bạn sản xuất sợi len merino với nhiều màu sắc và với hai mức trọng lượng: chunky (dày) và DK weight. Người quản lý sản phẩm muốn hiểu những khác biệt về số lượng sản xuất theo từng sản phẩm giữa năm 2025 và 2024 trong kỳ sản xuất tháng Bảy, và đã cung cấp cho bạn dữ liệu sản xuất đối với một số sản phẩm được chọn. Hãy sử dụng bảng tính (spreadsheet) để xác định dữ liệu có sẵn và hoàn thành những điều sau:
1. Mục tiêu của phân tích là gì?
2. Có hai câu hỏi ban đầu nào bạn có thể hỏi về dữ liệu?
3. Tạo một biểu đồ cột (column chart) mô tả số lượng sản xuất theo `ProductDescription` và `Year`.
4. Tính toán và xác định một số thước đo mô tả:
   a. Tính số lượng sản xuất trung bình (`Average ProductionQuantity`) theo `ProductDescription` trong năm 2024 so với năm 2025.
   b. Xác định số lượng đơn vị sản phẩm được sản xuất thấp nhất theo `ProductDescription` trong năm 2024 so với năm 2025.
   c. Xác định số lượng đơn vị sản phẩm được sản xuất cao nhất theo `ProductDescription` trong năm 2024 so với năm 2025.

**EX 3.3 (LO 2, 6) Kế toán Tài chính - Bảng đánh dấu (Highlight Table) trên Tableau** 
> 📥 **Dữ liệu thực hành:** Tải file <a href="Datasets/Vendor_Payments.csv" download target="_blank"><strong>Vendor_Payments.csv</strong></a> để thực hiện bài tập này.

Giám đốc tài chính của bạn muốn hiểu rõ hơn những thay đổi trong các khoản thanh toán cụ thể cho nhà cung cấp từ năm 2024 đến năm 2025 được thực hiện bởi thành phố nơi bạn làm việc. Vị giám đốc tài chính này đặc biệt quan tâm đến việc hiểu những khoản thanh toán được thực hiện cho các nhà cung cấp sau: 4-Star Hose & Supply, Aecom Technical Services Inc., WRG LLC, Winston Water Cooler Ltd., và Zoetis Inc. Bạn đã tải file các khoản thanh toán cho nhà cung cấp về và tải nó lên Tableau để phân tích. Hãy tạo một Bảng Đánh dấu (Highlight table) trong Tableau để xác định những thay đổi trong các khoản thanh toán cho 5 nhà cung cấp này trong khoảng thời gian từ năm 2024 đến năm 2025.

**EX 3.4 (LO 2, 6) Hệ thống Thông tin Kế toán - Phân tích các Thước đo** Là một phần trong chương trình an ninh mạng mới của công ty bạn, mỗi nhân viên đều phải tham gia một khóa đào tạo hằng năm. Các khóa đào tạo này được thực hiện thông qua nhiều hình thức (trực tiếp, học trực tuyến đồng bộ - online synchronous, và trực tuyến không đồng bộ - online asynchronous). Bạn và nhóm của bạn đã theo dõi các chi phí đào tạo hàng tháng cũng như số lượng các mối đe dọa không gian mạng do nhân viên báo cáo. Nhân viên có thể báo cáo về các mối đe dọa an ninh mạng chẳng hạn như các nỗ lực lừa đảo (phishing), hoặc các chuyên gia CNTT có thể báo cáo về các mối đe dọa thông qua việc kiểm tra các báo cáo đăng nhập hàng tháng. Bạn được yêu cầu điều tra các chi phí đào tạo an ninh mạng trong giai đoạn từ tháng 1 năm 2023 đến hết tháng 12 năm 2025.
Xem xét và hoàn thành bảng bằng cách xác định các câu hỏi phụ và những thước đo khả thi được dùng để giải quyết các câu hỏi phụ mà bạn đã xác định (xem sách giáo khoa). Sau đó, hãy tiến hành thực hiện các phân tích mô tả bằng cách sử dụng file dữ liệu được cung cấp.

**EX 3.5 (LO 3, 6) Kiểm toán - Các Thước đo Chẩn đoán** Giả sử bạn là nhân viên kiểm toán được phân công thực hiện việc kiểm toán báo cáo tài chính của một khách hàng là một công ty tư nhân thuộc lĩnh vực phân phối cho năm tài chính kết thúc vào ngày 31 tháng 12 năm 2025. Khách hàng này không sản xuất các mặt hàng mà mua về thành phẩm và bán cho nhiều nhà bán lẻ khác nhau. Senior (Kiểm toán viên chính) của nhóm kiểm toán đã yêu cầu bạn thực hiện các thủ tục phân tích đối với các khoản hàng bán bị trả lại. Phân tích mô tả của bạn đã phát hiện ra rằng hàng bán bị trả lại đã gia tăng với tư cách là một phần trăm của doanh thu. Sử dụng bảng tính để thực hiện các yêu cầu sau đây:
1. Tính tổng số tiền bằng đô la của doanh số bán hàng, tổng số tiền trả lại, số lượng bán hàng, và số lượng trả lại cho mỗi năm 2024 và 2025.
2. Tính phần trăm thay đổi trong số tiền bằng đô la của doanh thu, số tiền trả lại, số lượng bán hàng, và số lượng trả lại từ năm 2024 đến năm 2025.
3. Tạo một biểu đồ phân tán (scatterplot) trong đó số tiền bằng đô la của doanh số bán hàng nằm trên trục x và các khoản hàng bán bị trả lại nằm trên trục y.
4. Những tháng nào trong năm 2025 có số lượng hàng bán bị trả lại mà bạn có thể coi là những điểm bất thường (anomalies)?

**EX 3.6 (LO 3, 6) Kế toán Quản trị - Phân tích Xu hướng với Biểu đồ Đường (Trend Analysis with Line Graphs)** Bạn là một thực tập sinh tại một công ty sản xuất, và giám đốc tài chính (controller) công ty của bạn đã biết việc bạn hoàn thành một khóa học phân tích dữ liệu chuyên sâu về kế toán. Vị giám đốc này đã thực hiện xong các phân tích mô tả cơ bản đối với doanh số bán hàng của công ty cho tháng 6 năm 2025 nhưng muốn hiểu lý do tại sao doanh số lại tăng thêm 5.14%. Sử dụng bộ dữ liệu để hoàn thành các yêu cầu sau:
1. Câu hỏi ban đầu cho phân tích này là gì?
2. Xác định hai câu hỏi phụ cho phân tích.
3. Xác định các thước đo (measures) tiềm năng mà bạn có thể tính toán để trả lời cho hai câu hỏi phụ này.
4. Tạo một biểu đồ đường hiển thị xu hướng doanh số trong tháng Sáu của năm 2024 so với năm 2025.
5. Tạo một biểu đồ cột hiển thị doanh số bán cho mỗi khách hàng trong tháng 6 năm 2024 so với tháng 6 năm 2025.


**EX 3.7 (LO 3, 6) Kế toán Tài chính - Phân tích Xu hướng và Tương quan (Trend and Correlation Analysis)** Giám đốc tài chính (controller) công ty đã yêu cầu nhóm phân tích các khoản phải thu (accounts receivable) và báo cáo tuổi nợ (aging) của các khoản phải thu so với năm trước. Phân tích mô tả của bạn chỉ ra rằng các khoản phải thu đã tăng so với năm trước, trong khi doanh số bán hàng vẫn giữ nguyên. Do bạn là thực tập sinh trong công việc này, các đồng nghiệp của bạn đã yêu cầu bạn xem xét các câu hỏi phân tích chẩn đoán mà bạn phải hỏi để lập kế hoạch cho phân tích của mình. Bạn đã được cung cấp từ điển dữ liệu (data dictionary). (Xem sách để biết chi tiết từ điển dữ liệu).
Hãy hoàn thành các câu hỏi mục tiêu chẩn đoán trong bảng sau:
- Mục tiêu: Hiểu lý do tại sao các khoản phải thu tăng so với năm trước.
- Câu hỏi ban đầu: ...
- Câu hỏi phụ: 1. ..., 2. ..., 3. ...
- Các thước đo khả thi: ...

**EX 3.8 (LO 3, 6) Hệ thống Thông tin Kế toán - Phân tích Xu hướng và Tương quan** Bạn và nhóm của bạn đã theo dõi số lượng các mối đe dọa không gian mạng (cybersecurity threats) do nhân viên báo cáo. Nhân viên có thể báo cáo các mối đe dọa an ninh mạng chẳng hạn như các nỗ lực lừa đảo (phishing), và các chuyên gia CNTT có thể báo cáo các mối đe dọa thông qua việc kiểm tra báo cáo đăng nhập hàng tháng.
Phân tích mô tả ban đầu của bạn đã phát hiện ra rằng trong ba năm qua, có 313 sự cố không gian mạng đã được báo cáo. Có 73 báo cáo trong năm 2023, 111 báo cáo trong năm 2024 và 129 báo cáo trong năm 2025. Người quản lý của bạn muốn hiểu lý do tại sao số lượng báo cáo sự cố mạng lại tăng lên. Bạn đã bắt đầu xác định các câu hỏi ban đầu, các câu hỏi phụ và những thước đo khả thi cho phân tích của mình trong bảng sau (xem sách giáo khoa).
- 4. Hãy thực hiện các phân tích khả thi.

**EX 3.9 (LO 4, 6) Hệ thống Thông tin Kế toán - Đường xu hướng (Trendlines)** Giám đốc tài chính của bạn đã yêu cầu bạn chứng minh mối quan hệ giữa chi phí đào tạo an ninh mạng và số lượng các mối đe dọa không gian mạng hợp lệ (valid cybersecurity threats) do nhân viên báo cáo. Bạn đã thu thập dữ liệu hàng tháng báo cáo chi phí đào tạo an ninh mạng hàng tháng và số lượng các mối đe dọa không gian mạng hợp lệ do nhân viên báo cáo. Hãy tạo một biểu đồ đường (line graph) cho thấy mối quan hệ giữa hai biến này. Bao gồm đường xu hướng (trendline), phương trình, và R-bình phương (R-square) của phân tích của bạn.

**EX 3.10 (LO 5, 6) Kiểm toán - Thủ tục Phân tích (Analytical Procedures) cho Hàng bán bị trả lại** Bạn là thực tập sinh kiểm toán cho kỳ kiểm toán báo cáo tài chính năm kết thúc vào ngày 31 tháng 12 năm 2025 của một công ty tư nhân. Kiểm toán viên chính (audit senior) của bạn rất vui mừng vì bạn vừa hoàn thành một khóa học phân tích dữ liệu kế toán và muốn bạn sử dụng kiến thức về phân tích dự đoán để phát triển một dự tính về khoản hàng bán bị trả lại dựa trên khối lượng bán hàng nhằm thực hiện các thủ tục phân tích. Bạn đã tham gia vào quá trình suy nghĩ phản biện (critical thinking) và phát triển một phần của bảng (xem sách giáo khoa). Hoàn thành bảng.
2. Thực hiện phân tích hồi quy để dự đoán giá trị bằng đô la của khoản hàng bán bị trả lại bằng cách sử dụng khối lượng bán hàng.
3. Viết phương trình hồi quy.
4. R² cho mô hình hồi quy là bao nhiêu?

**EX 3.11 (LO 5, 6) Kế toán Tài chính - Ước tính Chi phí Bảo hành cho các khoản Dự thu/Dự chi (Accruals)** Là một kế toán tài chính cho một công ty sản xuất widget đại chúng, bạn được cung cấp một file dữ liệu và được yêu cầu tính toán cũng như ghi nhận các bút toán điều chỉnh cuối tháng. Bạn phải tính số tiền chi phí bảo hành cho tháng 1 năm 2025.
1. Thực hiện phân tích hồi quy để dự đoán chi phí bảo hành bằng cách sử dụng khối lượng bán hàng.
2. Viết phương trình hồi quy.
3. Bạn vừa thực hiện một truy vấn hệ thống thông tin kế toán của công ty và xác định rằng khối lượng bán hàng tháng 1 năm 2026 là 10.385. Hãy viết bút toán nhật ký (journal entry) để ghi nhận chi phí bảo hành.

**EX 3.12 (LO 5, 6) Kế toán Quản trị - Phân tích Xu hướng** Bạn là nhà phân tích tài chính hỗ trợ công tác kiểm soát tại một công ty tư nhân chuyên sản xuất đĩa giấy, khay và các sản phẩm giấy dùng một lần khác. Công ty thuộc sở hữu của một nhóm đầu tư vốn cổ phần tư nhân (private equity - PE). Hội đồng quản trị PE quan tâm đến việc tiết kiệm chi phí và xác định tính hiệu quả trong các quy trình của công ty. Bạn đã thu thập dữ liệu hàng tháng về số lần thay khuôn cắt (die-cut changes) và chi phí bảo trì hàng tháng. Mục tiêu là dự đoán chi phí của các chi phí bảo trì cho kỳ tiếp theo.
1. Chạy phân tích hồi quy sử dụng số lần thay khuôn cắt để dự đoán chi phí bảo trì.
2. Viết phương trình hồi quy.
3. Nếu công ty dự kiến có 650 lần thay khuôn cắt trong tháng 1 năm 2024, thì chi phí bảo trì dự kiến của công ty là bao nhiêu?

**EX 3.13 (LO 4, 6) Kiểm toán - Phân tích Dự đoán** Công ty CPA Kahn & Williams là kiểm toán viên độc lập cho Super Scooters. Nhóm kiểm toán đang thực hiện các thủ tục thử nghiệm cơ bản (substantive procedures) về doanh thu và thiết kế một thử nghiệm sử dụng các phân tích dự đoán để đánh giá tính hợp lý của doanh thu được ghi nhận của Super Scooters. Mục tiêu là đánh giá tính hợp lý của doanh thu đã ghi nhận. Câu hỏi ban đầu là: Doanh thu hàng tháng được báo cáo có khác biệt đáng kể so với doanh thu hàng tháng được dự đoán từ mô hình hồi quy của nhóm kiểm toán không? Mô hình của nhóm dựa trên dữ liệu hàng tháng của 3 năm trước. Hơn nữa, nhóm tin rằng doanh thu bị chi phối bởi khối lượng bán hàng và giá bán trung bình của scooter được bán trong tháng. Nhóm đã quyết định rằng bất kỳ sự khác biệt nào giữa doanh thu dự đoán và doanh thu thực tế lớn hơn sai số chuẩn (standard error) (tính bằng đô la tuyệt đối), thì cần phải điều tra thêm. (Xem sách để biết tóm tắt đầu ra - SUMMARY OUTPUT).
1. Biến phụ thuộc (y range) trong mô hình là gì?
2. Biến độc lập (x range) trong mô hình là gì?
3. Phương trình hồi quy cho mô hình này là gì?

**EX 3.14 (LO 5, 6) Kế toán Quản trị - Tối ưu hóa** Quản đốc sản xuất của bạn đã yêu cầu bạn xác định số lượng mặt hàng cần sản xuất để tối đa hóa số dư đảm phí (contribution margin) của công ty trong kỳ. Công ty của bạn có 4 sản phẩm: Standard widgets, Blue flying widgets, Red swimming widgets, Yellow hopping widgets. Bạn đã tạo một bảng tính nêu sơ lược về nhu cầu, số giờ máy trên mỗi đơn vị sản phẩm, số dư đảm phí trên mỗi đơn vị và tổng số giờ máy. Sử dụng tính năng Microsoft Solver để xác định số lượng đơn vị cần sản xuất cho mỗi sản phẩm và số dư đảm phí tối đa.

**EX 3.15 (LO 5) Kế toán Quản trị - Sử dụng Tối ưu hóa Tuyến tính để Xác định Tổ hợp Sản phẩm và Lợi nhuận (Determine Product Mix and Profit)** Bạn và các bạn cùng phòng đại học mở một doanh nghiệp thiết kế và thủ công các loại dây dắt chó và mèo có biểu trưng (logo) và màu sắc của trường đại học bạn. Bạn đã quyết định cung cấp các loại dây dắt với 3 độ dài: 6, 8 và 12 feet.
Hơn nữa, bạn có hai loại dây dắt: "tiêu chuẩn" (standard) hoặc "trang trí" (decorative). Mặc dù dây dắt trang trí tốn nhiều thời gian hơn để tạo ra, nhưng chúng có biên lợi nhuận gộp lớn trên mỗi sản phẩm. Tuy nhiên, dây dắt tiêu chuẩn lại có nhu cầu cao hơn. Bạn và hai người bạn cùng phòng đã sắp xếp một lịch trình để có thể khớp mọi thứ vào tuần của các bạn - lịch trình này bao gồm các lớp học, các sự kiện xã hội và thời gian làm thủ công. Vì bạn đang đăng ký khóa học phân tích dữ liệu trong kế toán, bạn đã tình nguyện tính toán xem nên sản xuất bao nhiêu dây dắt mỗi loại hàng tuần dựa trên nhu cầu, lợi nhuận gộp cho mỗi sản phẩm và ràng buộc về giờ làm việc.
1. Thực hiện tối ưu hóa tuyến tính bằng Excel Solver.
2. Bạn và hai người bạn cùng phòng nên sản xuất bao nhiêu đơn vị mỗi loại mỗi tuần?
3. Tổng lợi nhuận gộp bạn mong đợi kiếm được dựa trên số lượng dây dắt chó sản xuất hàng tuần là bao nhiêu?
4. Có ràng buộc nào được xác định trong báo cáo câu trả lời là không ràng buộc (non-binding) không?

**EX 3.16 (LO 4, 5) Xây dựng Bảng tính và Xác định Các ràng buộc** Cùng với các bạn cùng phòng ở đại học, bạn đang mở một doanh nghiệp để làm các loại mũ, áo phông và tất trang trí có màu sắc của trường bạn. Bạn đã quyết định bắt đầu với năm sản phẩm cốt lõi: Decorative ball cap, Decorative "GO Team" t-shirt, Decorative "Defense Wins Championships" t-shirt, Decorative socks, Decorative knee-high socks.
Là một phần trong kế hoạch kinh doanh của bạn, bạn muốn tính toán tổng số lượng của từng sản phẩm sẽ tạo ra mỗi tuần. Bạn dự định sử dụng Microsoft Solver để xác định số lượng tối đa các đơn vị sản phẩm cần sản xuất trong giới hạn các ràng buộc của bạn. Bạn muốn tối đa hóa lợi nhuận của công ty với ràng buộc về số giờ làm việc cho mỗi người. Bảng (xem sách giáo khoa) phác thảo lợi nhuận gộp và số giờ làm thủ công cho mỗi sản phẩm.
Ngoài ra, bạn và các bạn cùng phòng đã cam kết làm việc theo số giờ sau đây mỗi tuần: Bạn: 20; Bạn cùng phòng 1: 20; Bạn cùng phòng 2: 15; Bạn cùng phòng 3: 10.
1. Xây dựng một bảng tính mô hình tối ưu hóa tuyến tính.
2. Tính tổng số lượng đơn vị cho từng sản phẩm nên được sản xuất mỗi tuần.
3. Tổng lợi nhuận gộp dự kiến kiếm được dựa trên sản xuất hàng tuần là bao nhiêu?
4. Có ràng buộc nào được xác định trong báo cáo câu trả lời là không ràng buộc không?

**EX 3.17 (LO 5, 6) Kế toán Quản trị - Tối ưu hóa Tuyến tính** Tiana’s Jewel Design, Inc. thiết kế và sản xuất đồ trang sức kim loại sản xuất hàng loạt và đồ trang sức mạ bạc thiết kế tùy chỉnh. Hiện tại, chủ sở hữu thiết kế và sản xuất ba dòng trang sức tùy chỉnh (custom jewelry): dây chuyền (necklaces), vòng tay (bracelets) và hoa tai (earrings) (các biến quyết định). Số dư đảm phí và yêu cầu về nguồn lực cho mỗi sản phẩm được cung cấp (xem bảng trong sách).
Họ muốn tối đa hóa số dư đảm phí (hàm mục tiêu). Tuy nhiên, chủ sở hữu có những ràng buộc sau:
- Hợp đồng sản xuất ít nhất 10 đôi khuyên tai tùy chỉnh một tháng.
- Họ có thể bán toàn bộ dây chuyền tùy chỉnh và khuyên tai tùy chỉnh được sản xuất ra.
- Nhu cầu đối với vòng tay tùy chỉnh chỉ là 30 cái một tháng.
- Mỗi tháng có thể mua được 800 ounce mạ bạc.
- Hai nhà thiết kế làm việc với tổng số là 120 giờ một tháng.
- Ước tính có sẵn 80 giờ gia công mỗi tháng.
1. Sử dụng Microsoft Excel Solver để tạo mô hình tối ưu hóa tuyến tính.
2. Cần sản xuất bao nhiêu sản phẩm mỗi loại để tối đa hóa số dư đảm phí?
3. Có ràng buộc nào bị giới hạn (binding) không?
4. Dựa trên kết quả đầu ra từ báo cáo câu trả lời, bạn sẽ đưa ra lời khuyên gì cho chủ sở hữu?

---

### Tình huống Ứng dụng Chuyên môn: Công ty Dịch vụ Chăm sóc Sức khỏe (Healthcare Service Company)

Kindred Healthcare là một công ty dịch vụ chăm sóc sức khỏe sau cấp tính chuyên vận hành dịch vụ chăm sóc phục hồi chức năng và chăm sóc cấp tính dài hạn trên khắp Hoa Kỳ. Các bệnh viện của Kindred cung cấp cùng một chế độ chăm sóc chuyên sâu mà bệnh nhân sẽ nhận được tại bệnh viện truyền thống, nhưng cho một giai đoạn phục hồi kéo dài. Dữ liệu được sử dụng trong tình huống này dựa trên dữ liệu thực tế từ Cổng Thông tin Dữ liệu Mở của Bộ Y tế và Dịch vụ Nhân sinh bang California.
Kindred có 13 bệnh viện chăm sóc cấp tính dài hạn ở California: Baldwin Park, Riverside, Brea, Sacramento, La Mirada, San Diego, Los Angeles, San Francisco Bay Area, Ontario, South Bay, Paramount, Westminster, Rancho.
Các địa điểm bệnh viện ở California được hợp nhất vào các báo cáo tài chính được kiểm toán bởi kiểm toán viên độc lập và cung cấp cho hội đồng quản trị, các nhà đầu tư chính của công ty và các tổ chức tài chính đã cấp các khoản vay ngân hàng. Báo cáo kết quả hoạt động kinh doanh (income statement) trong ba năm trước được cung cấp (xem bảng trong sách).
Các báo cáo tài chính được lập dựa trên số tiền hằng năm từ mỗi địa điểm ở California. Thực thể hợp nhất đã cung cấp một file dữ liệu bao gồm dữ liệu hàng năm theo địa điểm cho nhiều trường dữ liệu khác nhau.


**PAC 3.1 Kiểm toán: Phát triển Mục tiêu và Câu hỏi cho Kế hoạch Kiểm toán**
**Dữ liệu | Kiểm toán** Bạn là nhân viên năm thứ hai tại một công ty kế toán công được phân công thực hiện hợp đồng với Bệnh viện Kindred, đây là một hợp đồng mới của công ty. Bạn đã được yêu cầu thực hiện phân tích mô tả, phân tích chẩn đoán và phân tích dự đoán cho nhóm kiểm toán của mình.
Senior (kiểm toán viên chính) cung cấp cho bạn một file Excel bao gồm tổng doanh thu bệnh nhân theo địa điểm bệnh viện từ năm 2013 đến 2019. Senior yêu cầu bạn thực hiện phân tích dữ liệu khám phá và phác thảo một kế hoạch kiểm toán, bạn nhận ra việc này tương tự như phác thảo mục tiêu, câu hỏi ban đầu và câu hỏi phụ cho phân tích dữ liệu. Trước khi có thể khám phá đầy đủ dữ liệu, bạn phải hiểu được dữ liệu, vì vậy bạn bắt đầu với các số liệu thống kê mô tả. Hoàn thành bảng trong sách.
7. Thực hiện phân tích có khả năng như được mô tả cho mỗi thước đo.

**PAC 3.2 Kế toán Quản trị: Đánh giá Chi phí Nhân công và Năng suất**
**Dữ liệu | Kế toán Quản trị** Giả sử bạn là kế toán viên quản trị cho nhóm hợp nhất ở California của Bệnh viện Kindred. Giám đốc điều hành đã yêu cầu bạn phân tích dữ liệu hàng năm gắn liền với lao động của bệnh viện. Cụ thể, giám đốc điều hành quan tâm đến các biến số (xem từ điển dữ liệu trong sách).
Hoàn thành bảng trong sách.
7. Sử dụng dữ liệu để tính toán các thước đo.

**PAC 3.3 Kế toán Tài chính: Hiểu Doanh thu Bệnh nhân (Patient Revenue)**
**Dữ liệu | Kế toán Tài chính** Bạn là một nhà phân tích tài chính làm việc cho nhóm giám đốc tài chính (controller's group) chi nhánh California của nhóm Bệnh viện Kindred. Giám đốc tài chính của bạn đã nhấn mạnh thực tế là tổng doanh thu (gross revenue) bao gồm cả doanh thu nội trú (inpatient revenue) và doanh thu ngoại trú (outpatient revenue). Tuy nhiên, chỉ có một cơ sở – Bệnh viện Kindred-Rancho – có doanh thu ngoại trú. Do đó, giám đốc tài chính muốn hiểu đầy đủ về doanh thu nội trú theo cơ sở cho năm 2019. Cụ thể, bạn được yêu cầu hiểu về số tiền bằng đô la của doanh thu nội trú do mỗi cơ sở đóng góp trong năm 2019 và cách doanh thu nội trú đã thay đổi so với năm 2018. Cuối cùng, giám đốc tài chính đang lập dự báo tài chính cho doanh thu nội trú cho năm 2020 và muốn hiểu dữ liệu việc sử dụng (utilization data) có thể đóng góp vào việc tạo ra dự báo này. Để làm hài lòng giám đốc tài chính của công ty bạn, bạn đang lập kế hoạch phân tích của mình và đã bắt đầu bảng (xem bảng trong sách). Giám đốc tài chính cũng đã cung cấp cho bạn một từ điển dữ liệu liên quan đến phân tích này.
Hoàn thành bảng phân tích mô tả, chẩn đoán, và dự đoán (xem sách giáo khoa).
7. Sử dụng dữ liệu có sẵn để tính toán các thước đo.

**PAC 3.4 Kế toán Thuế: Đánh giá Dữ liệu Tờ khai Thuế của Tổ chức Phi lợi nhuận và Tổ chức Vì lợi nhuận**
**Dữ liệu | Kế toán Thuế** Với tư cách là một kế toán thuế tại Kindred, bạn đã được yêu cầu phân tích dữ liệu bệnh viện phi lợi nhuận (non-profit) và bệnh viện vì lợi nhuận (for-profit). Bệnh viện Kindred có ba bệnh viện ở California là các tổ chức được miễn thuế (tax exempt organizations). Ba bệnh viện này phải được tách khỏi các bệnh viện vì lợi nhuận cho các mục đích thuế. Ngoài ra, bạn cũng được yêu cầu phân tích một tập hợp mẫu hồ sơ khai thuế phi lợi nhuận và so sánh các hồ sơ đó với các số tiền mà các bệnh viện phi lợi nhuận của Kindred đã kê khai cho năm 2019. Các biến và định nghĩa dữ liệu cho cả hai file được đưa vào các bảng trong sách.
Hoàn thành bảng.
11. Sử dụng dữ liệu để tính toán các thước đo.

---

### Tình huống Tiếp diễn (Continuing Case) Le Grind: Động lực và các Câu hỏi Cụ thể để Phân tích Lợi nhuận gộp (Gross Profit)

**Dữ liệu**
Hãy truy cập nền tảng học tập trực tuyến của Wiley để biết thông tin cơ sở về tình huống, các câu hỏi bổ sung, dữ liệu và nhiều chi tiết hơn về tình huống tiếp diễn này.


#### **English**
<iframe src="TaiLieu/textbookForPractice/Ch_03_Motivations%20and%20Objectives%20for%20Data%20Analysis.pdf" width="100%" height="800px"></iframe>

<!-- tabs:end -->
