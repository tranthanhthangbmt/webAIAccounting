# Chương 3: Động lực và Mục tiêu cho Phân tích Dữ liệu (Motivations and Objectives for Data Analysis)

## Tổng quan Chương (Chapter Preview)

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
