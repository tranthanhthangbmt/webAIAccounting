# Chương 4: Lập kế hoạch Dữ liệu và Chiến lược Phân tích (Planning Data and Analysis Strategies)

<!-- tabs:start -->
#### **Tiếng Việt**

## Tổng quan Chương (Chapter Preview)

Được trang bị với sự hiểu biết về các động lực và mục tiêu cho dự án phân tích dữ liệu và sau khi hình thành các câu hỏi mục tiêu cần thiết, đã đến lúc cho bước cuối cùng trong giai đoạn lập kế hoạch – thiết kế dữ liệu và các chiến lược phân tích (analysis strategies). Bạn sẽ sớm được kỳ vọng áp dụng kiến thức, khả năng tư duy và kỹ năng giải quyết vấn đề của mình để thiết kế một loạt các chiến lược dữ liệu và phân tích liên quan đến kế toán, kiểm toán và thuế. Chương này sẽ giúp bạn phát triển các kỹ năng cần thiết để lập các kế hoạch dự án phân tích dữ liệu hiệu quả.

*(Sơ đồ 3 Giai đoạn của Mô hình MOSAIC)*
- Giai đoạn 1: **Lập kế hoạch (Plan)**
  - Động lực (Motivation): Hiểu lý do của việc phân tích dữ liệu
  - Mục tiêu (Objective): Xác định mục tiêu và các câu hỏi cụ thể mà phân tích sẽ trả lời
  - Chiến lược (Strategy): Thiết kế dữ liệu và chiến lược phân tích
- Giai đoạn 2: **Phân tích (Analyze)**
  - Phân tích (Analysis): 1. Chuẩn bị dữ liệu, 2. Xây dựng các mô hình thông tin, 3. Khám phá dữ liệu
- Giai đoạn 3: **Báo cáo (Report)**
  - Diễn giải (Interpret): Giải thích các kết quả và ý nghĩa của chúng
  - Giao tiếp (Communicate): Xác minh quy trình và các kết quả

### Góc nhìn Chuyên gia (Professional Insight): Tại sao bạn nên lập Kế hoạch cho Dữ liệu và các Chiến lược Phân tích?

Taylor đã rất hào hứng khi bắt đầu sự nghiệp kiểm toán sau thời gian thực tập tại một công ty kế toán thuộc nhóm Big Four trong mùa bận rộn gần đây nhất.
Nhóm kiểm toán của tôi đã yêu cầu tôi tự thiết kế các chiến lược dữ liệu và phân tích của riêng mình và tài liệu hóa (document) từng bước tôi thực hiện. Mặc dù ban đầu tôi thiếu tự tin, nhưng tôi cảm thấy được hỗ trợ rất nhiều. Tôi đã học được rất nhiều điều, ngay cả khi tôi mắc sai lầm và phải chuyển hướng các chiến lược của mình.

Tôi đã thành công hơn khi hiểu được động lực và mục tiêu của các nhiệm vụ của mình. Tôi đã có thể hình thành những câu hỏi tốt hơn, từ đó dẫn đến những lựa chọn dữ liệu tốt hơn. Các thang đo lường (measurement scales) của dữ liệu tôi đã chọn cũng hướng tôi đến các phân tích phù hợp.

Nhiệm vụ đầu tiên của tôi là một phân tích mô tả. Tôi phải xác định xem số dư sổ chi tiết các khoản phải thu (accounts receivable subsidiary ledger) cuối năm và số dư sổ cái (general ledger) có khớp nhau không. Sau khi kiểm tra xem có bất kỳ hoạt động nào của khách hàng mua chịu (credit customer) bị loại trừ khỏi số dư các khoản phải thu trên sổ cái hay không, tôi đã tạo một báo cáo tuổi nợ của các khoản phải thu (accounts receivable aging report) liệt kê các số dư còn nợ (outstanding balances) của từng khách hàng từ sổ chi tiết. Tôi đã so sánh các khoản mục trong báo cáo tuổi nợ với các bút toán ghi sổ khoản phải thu trên sổ cái và ghi nhận từng khoản mục không khớp. Nếu không có khoản mục nào không khớp, số dư các khoản phải thu trên sổ cái đã được đối chiếu và xác minh thành công.

Sau đó, tôi đã thiết kế một chiến lược phân tích chẩn đoán (diagnostic analysis strategy) để xác định xem hoạt động phải thu nào đã gây ra bất kỳ khoản mục không khớp nào mà tôi tìm thấy. Chiến lược của tôi bắt đầu bằng việc thu thập tài liệu quy trình các khoản phải thu của khách hàng (client's accounts receivable process documentation). Đối với mỗi khoản mục không khớp, tôi xác định quy trình nào đã gây ra việc các khoản mục đó được đưa vào cả hai sổ. Việc ghi chép lại công việc đã giúp tôi giải thích những gì, như thế nào, và tại sao tôi lại thực hiện từng bước. Hồ sơ này sẽ hữu ích khi chúng tôi lặp lại việc xác minh này trong cuộc kiểm toán năm tới. Việc tự thiết kế các chiến lược dữ liệu và phân tích của riêng mình đã giúp tôi có được những kỹ năng liên quan và sự tự tin để bắt đầu sự nghiệp kiểm toán của mình.

---

## Lộ trình Chương (Chapter Roadmap)

| **MỤC TIÊU HỌC TẬP (LEARNING OBJECTIVES)** | **CHỦ ĐỀ (TOPICS)** | **ỨNG DỤNG (APPLY IT)** |
| --- | --- | --- |
| **LO 4.1** Xác định các thành phần của một kế hoạch dự án phân tích dữ liệu. | • Tạo một Kế hoạch Dự án Phân tích Dữ liệu<br>• Mẫu Kế hoạch Dự án Phân tích Dữ liệu | Xây dựng một Kế hoạch Dự án cho Chi phí Hàng tồn kho *(Ví dụ: Kế toán Tài chính)* |
| **LO 4.2** Mô tả cách phát triển một chiến lược dữ liệu. | • Xác định Dữ liệu Phù hợp<br>• Đánh giá Các Trường và Nguồn Dữ liệu<br>• Xem xét Các Rủi ro của Chiến lược Dữ liệu và Thực hiện Các Kiểm soát | Xác định Đặc điểm Dữ liệu *(Ví dụ: Hệ thống Thông tin Kế toán)* |
| **LO 4.3** Giải thích cách một chiến lược phân tích được thiết kế. | • Thiết kế Các Phân tích để Mô tả và Chẩn đoán<br>• Thiết kế Các Phân tích để Dự đoán và Đề xuất | Tạo một Kế hoạch Dự án Phân tích Dữ liệu Dự đoán *(Ví dụ: Kế toán Tài chính)* |
| **LO 4.4** Tóm tắt dữ liệu và các chiến lược phân tích trong các lĩnh vực thực hành chuyên môn. | • Hệ thống Thông tin Kế toán<br>• Kiểm toán<br>• Kế toán Tài chính<br>• Kế toán Quản trị<br>• Kế toán Thuế | Ghép nối Các Chiến lược với Các Lĩnh vực Thực hành Chuyên môn |

> **Data** Thẻ Data xuất hiện trong chương khi dữ liệu cho một ví dụ, hình ảnh minh họa hoặc ứng dụng có sẵn trên nền tảng học tập trực tuyến của Wiley.
> Các phần mềm phân tích dữ liệu liên tục thay đổi, và có thể có những phiên bản mới hơn của phần mềm được đề cập trong chương này. Để biết thêm thông tin, hãy truy cập video đi kèm trên nền tảng học tập trực tuyến của Wiley.

---

## 4.1 Các Kế toán viên Thiết kế Các Dự án Phân tích Dữ liệu Như Thế Nào?

**MỤC TIÊU HỌC TẬP 1 (LEARNING OBJECTIVE 1)**
**Xác định các thành phần của một kế hoạch dự án phân tích dữ liệu.**

Hãy nhớ lại rằng bước đầu tiên trong việc lập kế hoạch cho một dự án phân tích dữ liệu là hiểu được động lực (motivations) cho dự án, chẳng hạn như xác định vấn đề, đánh giá các mô hình và cơ hội, đo lường hiệu suất và tuân thủ quy định. Việc xem xét góc nhìn của các bên liên quan (stakeholders) chính của dự án là một phần quan trọng của sự hiểu biết đó. Tiếp theo, việc suy nghĩ phản biện về mục đích của dự án giúp xác định mục tiêu và làm rõ các câu hỏi cụ thể của dự án. Các mục tiêu và câu hỏi chung có thể được nhóm theo việc kết quả phân tích có mô tả (describe), chẩn đoán (diagnose) hay dự đoán (predict) một kết quả hay không, hoặc liệu kết quả phân tích có nên đưa ra các đề xuất (prescribe) chiến lược tương lai cho tổ chức hay không.

Bước cuối cùng của giai đoạn lập kế hoạch dự án phân tích dữ liệu là thiết kế một kế hoạch chuyên nghiệp cho dự án phân tích dữ liệu. Tư duy phản biện tiếp tục đóng một vai trò quan trọng, từ việc lựa chọn một chiến lược cho dữ liệu và phân tích, đến việc xác định các rủi ro cố hữu (inherent risks) cho cả hai và nhúng các kiểm soát nội bộ (internal controls) để giảm thiểu chúng. Kế hoạch chiến lược dữ liệu và phân tích là một bản thiết kế (blueprint) có tổ chức và có chủ đích cho dự án. Nó cũng cho phép một người khác ngoài người tạo ra nó thực hiện phân tích, điều này có thể giải phóng các kế toán viên để thực hiện các dịch vụ có giá trị khác với chuyên môn về kinh doanh và quy định của họ.

### Tạo một Kế hoạch Dự án Phân tích Dữ liệu (Create a Data Analysis Project Plan)

Nhiều người trong chúng ta sử dụng các công cụ lập kế hoạch mỗi ngày, chẳng hạn như dựa vào các ứng dụng điều hướng để lên kế hoạch cho thời gian di chuyển và cách đi đến các điểm đến mới. Các công cụ lập kế hoạch làm cho các nhiệm vụ hiệu quả hơn (efficient) và kết quả đem lại hiệu lực hơn (effective). Chúng cũng thường cung cấp những lời giải thích hợp lý cho sự cần thiết của các bước nhất định hoặc tại sao chúng nên được thực hiện theo một trình tự cụ thể.

Chương này tóm tắt một công cụ cho việc lập kế hoạch dự án phân tích dữ liệu mang lại những lợi ích tương tự cho các kế toán viên (Hình minh họa 4.1). Trình tự của các thành phần là có chủ đích:

- **Bước 1: Tập trung vào mục tiêu (Focus on the objective):**
  Luôn ghi nhớ mục tiêu và các câu hỏi cụ thể của dự án để chọn dữ liệu tốt nhất và các chiến lược phân tích nhằm hoàn thành mục tiêu và trả lời các câu hỏi đó. Việc đơn giản là nhớ đặt câu hỏi xem các quyết định về chiến lược dữ liệu và phân tích được đề xuất của kế hoạch liên quan như thế nào đến mục tiêu sẽ giúp chúng ta đưa ra những lựa chọn tốt hơn.
- **Bước 2: Chọn một chiến lược dữ liệu (Select a data strategy):**
  Sử dụng tư duy phản biện để phát triển và xếp hạng một số lựa chọn dữ liệu thay thế. Điều này đảm bảo rằng chúng ta chọn phương án dữ liệu phù hợp nhất cho mục tiêu.
- **Bước 3: Chọn một chiến lược phân tích (Select an analysis strategy):**
  Sử dụng những gì đã học được từ việc lựa chọn chiến lược dữ liệu và áp dụng quy trình phát triển cũng như xếp hạng đó cho các lựa chọn phân tích thay thế. Tuân theo bước này làm tăng khả năng chọn được phương án phân tích tốt nhất.
- **Bước 4: Xem xét rủi ro (Consider risks):**
  Việc xem xét và ưu tiên các rủi ro nghiêm trọng đối với cả chiến lược dữ liệu và phân tích cho thấy cách những rủi ro này có thể tạo ra các kết quả sai lệch và không hợp lệ (invalid).

![ILLUSTRATION 4.1](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.1.png)

- **Bước 5: Nhúng các kiểm soát (Embed controls):**
  Việc thiết kế và thực hiện các kiểm soát ngăn ngừa (preventative controls) và phát hiện (detective controls) vào quy trình phân tích dẫn đến kết quả chính xác, hợp lệ và đáng tin cậy.

Một kế hoạch phân tích dữ liệu làm tăng khả năng kết quả phân tích mô tả chính xác những gì đã xảy ra, chẩn đoán lý do tại sao nó xảy ra, dự đoán những gì có khả năng xảy ra, hoặc đề xuất hướng đi tốt nhất trong tương lai. Khi kế hoạch dự án hoàn tất, giai đoạn lập kế hoạch quy trình phân tích dữ liệu cũng hoàn thành, và đã đến lúc chuyển sang giai đoạn phân tích. Chương tiếp theo mô tả cách chuẩn bị dữ liệu đúng cách để phân tích. Nhưng trước tiên, hãy thực hành sử dụng công cụ lập kế hoạch dự án này trong bối cảnh kế toán.

### Mẫu Kế hoạch Dự án Phân tích Dữ liệu (Sample Data Analysis Project Plan)

Hãy tưởng tượng bạn là một kế toán tài chính cho WeMakeIt, Inc., một tập đoàn in 3D do nhân viên sở hữu (employee-owned) ở Phoenix, Arizona. Họ bán các mô hình siêu anh hùng (superhero figurines), dụng cụ xưởng cơ khí, và chân tay giả y tế (medical prostheses) được sản xuất bằng công nghệ in 3D. Được thành lập cách đây năm năm bởi một sinh viên đại học địa phương, Marisabel Cordoba, WeMakeIt, Inc. đã phát triển nhanh chóng để lấp đầy công suất sản xuất của họ và duy trì quy mô ổn định trong ba năm qua.

**Bước 1: Tập trung vào Mục tiêu (Focus on the Objective)**

Dự án trong ví dụ này là ước tính các khoản nợ khó đòi (bad debts) trong số dư các khoản phải thu cuối năm 2025. Kết quả sẽ là ước tính giá trị cho bút toán điều chỉnh cuối năm 2025, với việc ghi nợ vào chi phí nợ khó đòi (bad debts expense) và ghi có vào tài khoản đối ứng tài sản (contra-asset) là dự phòng phải thu khó đòi (allowance for uncollectible accounts).

**ÁP DỤNG TƯ DUY PHẢN BIỆN 4.1 (APPLYING CRITICAL THINKING 4.1): Ước tính Nợ khó đòi**
Phương pháp tính theo số dư các khoản phải thu cuối kỳ của U.S. GAAP yêu cầu những điều sau:
- Số dư các khoản phải thu cuối năm có thể được xem xét một cách tổng thể hoặc chia theo các tổng nhóm tuổi nợ (age group subtotals). Quy tắc nhóm tuổi nợ đối với các công ty sản xuất thường là nợ dưới 30 ngày, 30 đến 60 ngày, và nợ quá hạn trên 60 ngày, nhưng các quy tắc này khác nhau tùy theo từng ngành.
- Việc xem xét hướng dẫn của cơ quan quản lý, thực tiễn ngành, chính sách và quy trình kinh doanh, và các tỷ lệ ước tính nợ khó đòi trong quá khứ là cách tiếp cận chuyên môn để lựa chọn tỷ lệ ước tính nợ khó đòi. Thông thường, khi tuổi của các khoản phải thu tăng lên, tỷ lệ không thể thu hồi được áp dụng cho độ tuổi đó cũng tăng theo (Kiến thức - Knowledge).

Giả định các điều sau đây cho ví dụ này:
- Công ty cung cấp cho các khách hàng mua chịu các điều khoản thanh toán là 30 ngày.
- Số dư các khoản phải thu cuối năm 2025 trong sổ cái là $83,734.30.
- Dự phòng phải thu khó đòi chưa điều chỉnh cuối năm 2025 có số dư có (credit balance) là $3,000.
- WeMakeIt, Inc. đã quyết định sử dụng phần trăm của phương pháp các khoản phải thu cuối năm để ước tính chi phí nợ khó đòi mỗi năm. Họ đã ủy quyền (authorized) giả định nợ khó đòi là 2% cho các hóa đơn quá hạn 30 đến 60 ngày và 30% cho các hóa đơn quá hạn trên 60 ngày.

Dự án phân tích dữ liệu này có mục tiêu và các câu hỏi liên quan như sau:
- **Mục tiêu:** Ước tính chính xác khoản nợ khó đòi trong số dư các khoản phải thu cuối năm theo đúng quy định của U.S. GAAP.
- **Các câu hỏi cụ thể:**
  1. Ước tính hợp lý về các khoản phải thu không thể thu hồi trong số các khoản phải thu còn nợ (outstanding accounts receivables) cuối năm 2025 là bao nhiêu?
  2. Số tiền nào nên được sử dụng trong bút toán điều chỉnh chi phí nợ khó đòi (bad debts expense)?

Với mục tiêu đã được xác định và các câu hỏi đã được làm rõ, đã đến lúc phát triển chiến lược dữ liệu.

**Bước 2: Chọn Chiến lược Dữ liệu (Select the Data Strategy)**

Hãy phát triển một vài lựa chọn dữ liệu thay thế (data alternatives) có thể giúp trả lời câu hỏi mục tiêu. Sau đó, để chọn phương án dữ liệu hữu ích nhất cho kế hoạch dự án, hãy xác định các yếu tố bạn muốn sử dụng để xếp hạng các lựa chọn này, và gán giá trị cho các yếu tố của từng lựa chọn. Phương án chiến lược dữ liệu tốt nhất là phương án có đánh giá tổng thể về yếu tố cao nhất.

**ÁP DỤNG TƯ DUY PHẢN BIỆN 4.2 (APPLYING CRITICAL THINKING 4.2): Xem xét Các Góc nhìn Khác nhau**
Giá trị thuần có thể thực hiện được (net realizable value) của các khoản phải thu (các khoản phải thu trừ đi dự phòng phải thu khó đòi) được báo cáo trên bảng cân đối kế toán như một tài sản ngắn hạn (current asset). Chi phí nợ khó đòi làm giảm thu nhập ròng (net income) được báo cáo trên báo cáo kết quả hoạt động kinh doanh (income statement). Hãy nhớ rằng các bên có quan điểm rất khác nhau sử dụng thông tin này để ra quyết định (Các bên liên quan - Stakeholders):
- Các chủ nợ (Creditors), những người muốn được hoàn trả tiền, quan tâm đến tính thanh khoản (liquidity) của các tài sản.
- Các cổ đông (Shareholders), những người dự đoán giá trị cổ phiếu tương lai cũng như kỳ vọng cổ tức, phải hiểu được dòng tiền vào (cash inflows) dự kiến trong tương lai từ các hoạt động kinh doanh.
- Các nhà quản lý (Managers) muốn kiếm được tiền thưởng (bonuses), khoản này được xác định bởi sự tăng trưởng về thu nhập ròng và tổng tài sản. Sự thay đổi trong dự phòng phải thu khó đòi sẽ ảnh hưởng đến cả hai số tiền này.

Có một vài lựa chọn chiến lược dữ liệu có thể được xem xét độc lập hoặc kết hợp cho dự án này:
- Tất cả các hóa đơn bán chịu và dữ liệu thu tiền thuộc về kỳ kế toán.
- Tất cả các hóa đơn chưa thanh toán (outstanding invoices) có trong số dư các khoản phải thu cuối năm.
- Số dư tài khoản đã điều chỉnh cuối năm trước và số dư tài khoản chưa điều chỉnh cuối năm nay trong dự phòng phải thu khó đòi.
- Tổng các khoản xóa nợ phải thu (accounts receivable write-offs) của năm hiện tại.
- Các tỷ lệ phần trăm ước tính nợ khó đòi đã được ủy quyền cho các danh mục tuổi nợ phải thu.

Hãy nhớ lại rằng câu hỏi mục tiêu của dự án phân tích này yêu cầu một ước tính hợp lý về các khoản phải thu khó đòi cuối năm. Vì WeMakeIt, Inc. sử dụng phương pháp tỷ lệ phần trăm các khoản phải thu cuối năm theo GAAP với ba danh mục tuổi nợ điển hình cho các công ty sản xuất, nên dữ liệu hữu ích nhất khi xem xét các mục tiêu sẽ bao gồm:
- Các hóa đơn chưa thanh toán trong số dư các khoản phải thu cuối năm.
- Số dư tài khoản dự phòng phải thu khó đòi chưa điều chỉnh của năm nay.
- Các tỷ lệ ước tính nợ khó đòi đã được ủy quyền cho từng nhóm tuổi nợ của khoản phải thu.

**ÁP DỤNG TƯ DUY PHẢN BIỆN 4.3 (APPLYING CRITICAL THINKING 4.3): Chọn Chiến lược Dữ liệu Phù hợp với Mục tiêu của Bạn**
Cả chiến lược dữ liệu và chiến lược phân tích đều được cải thiện khi chúng được phát triển, đánh giá và xếp hạng bởi các giá trị yếu tố (factor values) được đặt ra cho mỗi chiến lược dữ liệu tiềm năng:
- Các yếu tố định giá mức độ liên quan của dữ liệu, chẳng hạn như số tiền dự kiến thu được trong tương lai, các sai số ước tính trước đó, và rủi ro không thể thu hồi dự kiến nên được sử dụng để chọn chiến lược dữ liệu tốt nhất cho kế hoạch phân tích của WeMakeIt, Inc. (Các phương án thay thế - Alternatives).
- Việc sử dụng dữ liệu từ các hóa đơn chưa thanh toán, dự phòng phải thu khó đòi chưa điều chỉnh, và các tỷ lệ ước tính nợ khó đòi đã được ủy quyền là lựa chọn tốt nhất cho phân tích của WeMakeIt, Inc. Những lựa chọn dữ liệu này phù hợp nhất với mục tiêu của phân tích, đó là tính toán một ước tính hợp lý cho các khoản phải thu khó đòi cuối năm (Mục đích - Purpose).
- Ví dụ về mặt cá nhân, nếu mục tiêu của bạn là ăn mặc thành công cho một cuộc phỏng vấn, thì bạn có thể phát triển, đánh giá và xếp hạng các lựa chọn về việc mặc thứ gì đó bạn đã có, mượn từ một người bạn, hoặc mua một bộ đồ mới để mặc đi phỏng vấn. Việc sử dụng quần áo bạn đã có sẽ xếp hạng cao hơn việc mua quần áo mới nếu bạn xếp hạng các lựa chọn dựa trên các yếu tố chi phí và thời gian thấp nhất.

**Bước 3: Chọn Chiến lược Phân tích (Select the Analysis Strategy)**

Đối với bất kỳ kế hoạch dự án nào, việc chọn chiến lược phân tích tốt nhất liên quan đến việc xem xét và đánh giá một vài phương án phân tích có thể có trong các câu hỏi mục tiêu và chiến lược đã được chọn cho dữ liệu. Các phương án phân tích trong ví dụ về ước tính nợ khó đòi này liên quan đến các phương pháp khác nhau để xác định tuổi của một hóa đơn chưa thanh toán:
- Số ngày chưa thanh toán (Days outstanding) tính từ ngày hóa đơn trở về sau.
- Số ngày chưa thanh toán tính từ ngày đáo hạn (due date) trở về sau.

Phương án phân tích đầu tiên được ưu tiên hơn vì chính sách của WeMakeIt, Inc. là cho phép khách hàng thanh toán hóa đơn trong vòng 30 ngày và vì họ chỉ ước tính nợ khó đòi khi hóa đơn đã quá ngày đáo hạn, tương đương với hoặc nhiều hơn 30 ngày chưa thanh toán.
Do đó, câu hỏi đầu tiên (ước tính hợp lý về các khoản phải thu không thể thu hồi trong số dư phải thu cuối năm 2025 là bao nhiêu) sẽ được trả lời bằng cách tính tổng giá trị nợ khó đòi ước tính của từng nhóm tuổi nợ. Đây là một thước đo ước tính phần không thể thu hồi của số dư các khoản phải thu cuối năm (Hình minh họa 4.2). (Data: Xem mục How To 4.1 ở cuối chương để tìm hiểu cách tính toán các con số trong hình minh họa này.)

![ILLUSTRATION 4.2](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.2.png)

Câu hỏi thứ hai (giá trị nào nên được sử dụng trong bút toán điều chỉnh cuối năm cho chi phí nợ khó đòi) sẽ được trả lời khi tổng số $10,366.89 này bị trừ đi số dư dự phòng phải thu khó đòi chưa điều chỉnh cuối năm ($3,000). Giá trị được tính toán chính là giá trị cho bút toán điều chỉnh (adjusting journal entry) cuối năm, ghi nợ vào chi phí nợ khó đòi và ghi có vào dự phòng phải thu khó đòi:
| | Ghi Nợ (Debit) | Ghi Có (Credit) |
|---|---|---|
| Chi phí nợ khó đòi (Bad debts expense) | $7,366.89 | |
| Dự phòng phải thu khó đòi (Allowance for uncollectible accounts) | | $7,366.89 |

Việc tăng số dư chưa điều chỉnh $3,000 của tài khoản dự phòng thêm $7,366.89 sẽ dẫn đến số dư đã điều chỉnh là $10,366.89, bằng với số tiền không thể thu hồi ước tính trong các khoản phải thu vào cuối năm 2025. Hình minh họa 4.3 tóm tắt ba bước đầu tiên của kế hoạch dự án này.

![ILLUSTRATION 4.3](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.3.png)

Hai bước cuối cùng là xem xét các rủi ro và kiểm soát đối với cả chiến lược dữ liệu và chiến lược phân tích. Đầu tiên, chúng ta sẽ đánh giá các rủi ro và kiểm soát của chiến lược dữ liệu, và sau đó là các rủi ro và kiểm soát của chiến lược phân tích.

**Bước 4 và 5: Rủi ro và Kiểm soát Chiến lược Dữ liệu (Data Strategy Risks and Controls)**

Trong khi các tổ chức đầu tư vào các quy trình và kiểm soát được thiết kế để thu thập dữ liệu kế toán một cách chính xác, thì các cơ sở dữ liệu kế toán chắc chắn sẽ có một số vấn đề về dữ liệu. Trong ví dụ này, dữ liệu bao gồm các hóa đơn chưa thanh toán của các khoản phải thu cuối năm 2025 và các tỷ lệ ước tính nợ khó đòi đã được ủy quyền. Có thể có một số rủi ro khi sử dụng dữ liệu các khoản phải thu này:
- Bỏ sót hóa đơn hoặc ghi sai hóa đơn vào sổ cái hoặc sổ chi tiết.
- Lỗi trong trường ngày đến hạn hóa đơn (due date fields) hoặc tổng số tiền hóa đơn.
- Các lỗi được tạo ra khi dữ liệu được trích xuất từ hệ thống AIS vào công cụ phân tích.

**ÁP DỤNG TƯ DUY PHẢN BIỆN 4.4 (APPLYING CRITICAL THINKING 4.4): Các mối đe dọa đối với Chiến lược Dữ liệu**
Rủi ro dữ liệu có thể ảnh hưởng đến độ chính xác và tính hợp lệ của kết quả phân tích. Những rủi ro này phải được đánh giá để có thể bổ sung các kiểm soát thích hợp vào kế hoạch dự án. Rủi ro chiến lược dữ liệu có thể bao gồm (Rủi ro - Risks):
- Dữ liệu rác (Dirty data) như dữ liệu không đầy đủ, dữ liệu không chính xác, và các trường dữ liệu được định dạng sai.
- Dữ liệu không liên quan đến mục tiêu của dự án.
- Dữ liệu không đủ để phân tích đáng tin cậy.
- Dữ liệu là một mẫu không mang tính đại diện (unrepresentative sample) cho tổng thể cơ bản.
- Lỗi trong các ước tính và giả định của ban quản lý về dữ liệu.

Các rủi ro dữ liệu này có thể được kiểm soát bằng cách so sánh dữ liệu được trích xuất với chứng từ hóa đơn gốc và chứng từ thu tiền. Các rủi ro có thể có liên quan đến các ước tính của ban quản lý về tỷ lệ phần trăm nợ khó đòi bao gồm sự thiên lệch của con người (human bias) được nhúng trong các tỷ lệ nợ khó đòi được ủy quyền, sự thay đổi trong hành vi thanh toán của khách hàng, và sự thay đổi trong quy trình kinh doanh đối với việc phê duyệt khách hàng mua chịu và các thực tiễn thu tiền.

![Applying critical thinking 4.4](../TaiLieu/textbookForPractice/Figures/Ch_04/Applying%20critical%20thinking%204.4.png)

Một cách để kiểm soát những rủi ro này là hỏi các nhà quản lý tài chính, bán hàng và phải thu xem có sự thay đổi nào đối với cơ sở khách hàng, điều kiện thị trường, hoặc các chính sách và thủ tục kinh doanh về phê duyệt tín dụng, xóa nợ, hay chính sách thu tiền trong năm hay không. Kiến thức này có thể xác nhận tỷ lệ nợ khó đòi hiện tại hoặc thúc đẩy việc điều chỉnh chúng.

Một kiểm soát khác để đánh giá các rủi ro trong các ước tính và giả định của ban quản lý là so sánh dữ liệu hiện tại với dữ liệu năm trước. Việc đánh giá sự gia tăng về số ngày chưa thanh toán trung vị (median number of days outstanding) và số lượng khách hàng mới so với khách hàng cũ trong từng nhóm tuổi có thể đưa ra những hiểu biết sâu sắc (insights) về tính hợp lý của các tỷ lệ ước tính nợ khó đòi.

Để minh họa, hãy tưởng tượng bạn đang tự hỏi liệu tỷ lệ nợ khó đòi 30% đối với các hóa đơn chưa thanh toán hơn 60 ngày có phải là một giả định hợp lý của ban quản lý trong năm 2025 hay không. Hình minh họa 4.4 cho thấy số ngày chưa thanh toán trung vị trong nhóm quá hạn trên 60 ngày đã tăng lên vào năm 2025.

![ILLUSTRATION 4.4](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.4.png)

Ngoài ra, bạn có thể tự hỏi liệu sự gia tăng này là do các khách hàng mới gây ra hay không, vì thói quen thanh toán của khách hàng mới thường không chắc chắn hơn khách hàng tiếp tục sử dụng dịch vụ (returning customers). Hình minh họa 4.5 cho thấy nhóm tuổi nợ trên 60 ngày có nhiều hóa đơn chưa thanh toán từ các khách hàng mới.

![ILLUSTRATION 4.5](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.5.png)

Kết quả của các bài kiểm tra kiểm soát này chỉ ra rằng nếu tỷ lệ nợ khó đòi năm 2024 cho nhóm tuổi này được sử dụng vào năm 2025, nó có thể không đo lường chính xác các khoản nợ khó đòi dự kiến trong số dư các khoản phải thu năm 2025. Những hình ảnh trực quan này cho thấy việc thực hiện các kiểm soát, chẳng hạn như kiểm tra tính hợp lý của dữ liệu (data reasonableness tests), trước khi thực hiện một phân tích có thể mang lại thông tin kinh doanh và chuyên môn tốt hơn.

**Bước 4 và 5: Rủi ro và Kiểm soát Chiến lược Phân tích (Analysis Strategy Risks and Controls)**

Các rủi ro phân tích phổ biến bao gồm sai sót trong việc thao tác dữ liệu (data manipulation), tính toán, hoặc khi sử dụng công nghệ, cũng như thành kiến con người và các vi phạm đạo đức khi sử dụng dữ liệu nhạy cảm. Dưới đây là một số ví dụ về rủi ro phân tích khi ước tính các khoản nợ khó đòi:
- Các sai sót trong việc phân loại nhóm tuổi nợ và tính toán tổng tuổi nợ.
- Áp dụng sai tỷ lệ ước tính nợ khó đòi đối với tổng của từng nhóm tuổi nợ.
- Tính sai tổng số tiền nợ khó đòi ước tính từ các nhóm tuổi nợ.
- Những nhầm lẫn trong việc tính toán giá trị dùng cho chi phí nợ khó đòi.

Việc xác minh tính chính xác của các phân loại nhóm tuổi nợ và của từng phép tính tổng cũng như phép nhân được thực hiện trên các khoản mục dữ liệu và các khoản tổng cộng của nhóm tuổi sẽ giúp kiểm soát những rủi ro này.

Một biện pháp kiểm soát khác là sử dụng tư duy thông thường (common sense) khi xem xét các kết quả về mức độ hợp lý (reasonableness). Hình minh họa 4.6 sử dụng một ví dụ từ nhóm ước tính tuổi nợ 30-60 ngày để cho thấy cách một bài kiểm tra theo tư duy thông thường có thể giúp phát hiện các sai sót lớn. Tổng các khoản phải thu chưa thanh toán của nhóm tuổi nợ đó là $20,441.46, và tỷ lệ không thể thu hồi đối với nhóm đó là 2%. Giá trị không thể thu hồi ước tính cho nhóm đó được tính bằng tích của hai con số trên, dẫn đến kết quả là $408.83. Biện pháp kiểm soát này đã giúp xác minh tính toán của chúng ta.

![ILLUSTRATION 4.6](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.6.png)

Thiết kế kế hoạch dự án cho ví dụ này hiện đã hoàn tất (Hình minh họa 4.7).

![ILLUSTRATION 4.7](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.7.png)

Tiếp theo, chúng ta sẽ đi sâu hơn vào cách phát triển cả hai loại chiến lược dữ liệu và chiến lược phân tích.

---

### Áp dụng (Apply It 4.1)
**Xây dựng Kế hoạch Dự án cho Chi phí Hàng tồn kho (Build a Project Plan for Inventory Costs)**

**Kế toán Tài chính** Tremendous Toys, công ty được thành lập bởi Elisabeth Hess và có trụ sở tại Wisconsin, chuyên sản xuất và bán đồ chơi trực tuyến với hình dáng các con vật độc đáo. Công ty có hơn một triệu đô la doanh thu bán hàng và lượng người theo dõi đông đảo cả trong nước và quốc tế. Ngân hàng đầu tư bảo lãnh (underwriting) cho đợt phát hành cổ phiếu lần đầu ra công chúng (IPO) sắp tới yêu cầu Elisabeth lập bản định giá hàng tồn kho cuối năm theo chuẩn U.S. GAAP.

Elisabeth đã lưu giữ các ghi chép rất tỉ mỉ, được sắp xếp theo các danh mục chi phí kinh doanh, như được liệt kê dưới đây. Cô ấy biết nguyên liệu nào đã được sử dụng để tạo ra từng món đồ chơi, nhân viên nào làm ra nó, và mất bao lâu để hoàn thành. Cô ấy cũng ghi lại số lượng và loại đồ chơi được sản xuất mỗi tháng. Tuy nhiên, cô ấy chưa bao giờ phân bổ chi phí (assigned costs) cho các mặt hàng tồn kho của mình.

| **Nguyên vật liệu (Materials)** | **Nhân công (Labor)** | **Chi phí chung (Overhead)** |
| --- | --- | --- |
| Nhựa cho máy in 3D (Plastic for 3D printers) | Thời gian làm việc của công nhân sản xuất (Production workers’ time) | Chi phí máy in 3D (3D printer costs) |
| Gỗ (Wood) | Mức lương của công nhân sản xuất (Production workers’ pay rate) | Chi phí dụng cụ sản xuất (Production tools costs) |
| Nhựa cây/Nhựa tổng hợp (Resin) | | Chi phí máy tính (thiết bị ngoại vi và internet) (Computer costs) |
| Sợi và vải (Fiber and fabric) | | Chi phí vận chuyển (Shipping costs) |
| Sơn, vec-ni và thuốc nhuộm (Paints, varnishes, and dyes) | | Tiền thuê xưởng, tiện ích và kho bãi (Factory rent, utilities, and storage) |
| Quần áo đồ chơi (Toy clothing) | | Vật tư sản xuất (Production supplies) |
| Keo dán và epoxy (Glues and epoxies) | | Thuế và phí pháp lý (Tax and legal fees) |
| Phụ kiện lấp lánh (Bling and other accessories) | | Đóng góp từ thiện (Donations to charities) |
| Mắt và các bộ phận cơ thể (Eyes and body parts) | | Chi phí quảng cáo (Advertising costs) |

Hãy lập một kế hoạch dự án phân tích dữ liệu để giúp Elisabeth xây dựng các chi phí có thể được ghi nhận vào hàng tồn kho (inventoriable costs) của cô ấy. Hãy sử dụng cấu trúc sau đây cho câu trả lời của bạn:
1. Mục tiêu dự án và câu hỏi cụ thể (Project objective and specific question)
2. Chiến lược dữ liệu (Data strategy)
3. Chiến lược phân tích (Analysis strategy)
4. Rủi ro của chiến lược dữ liệu và chiến lược phân tích (Data and analysis strategy risks)
5. Các biện pháp kiểm soát của chiến lược dữ liệu và chiến lược phân tích (Data and analysis strategy controls)

**GIẢI PHÁP (SOLUTION)**
**1. Mục tiêu dự án (Project objective)**
Chuẩn bị bản định giá toàn bộ chi phí (full costing valuation) tuân thủ U.S. GAAP cho hàng tồn kho hiện tại của Tremendous Toys.
**Câu hỏi cụ thể (Specific question)**
Giá trị hàng tồn kho cuối năm theo U.S. GAAP là bao nhiêu?

**2. Chiến lược dữ liệu (Data strategy)**
- Thu thập tất cả các chi phí và số lượng tiêu hao nguyên liệu thô (raw measures of consumption) của các nguồn lực liên quan đến sản xuất (nguyên vật liệu trực tiếp, nhân công trực tiếp, và chi phí sản xuất chung) trong ba năm qua.
- Thu thập các hồ sơ về số lượng sản phẩm được sản xuất cho mỗi tháng tương ứng với dữ liệu chi phí đã nhận.
- Kiểm kê hiện vật (physical count) đối với hàng tồn kho hiện tại theo sản phẩm.

**3. Chiến lược phân tích (Analysis strategy)**
- Tổng hợp dữ liệu chi phí theo số lượng mô hình đồ chơi sản xuất hàng tháng.
- Ước tính sự thay đổi chi phí (cost behavior) bằng cách sử dụng hồi quy (regression) để tìm ra biến phí (variable costs) trên mỗi mô hình và tổng định phí sản xuất (total fixed production costs) mỗi tháng.
- Áp dụng kết quả để định giá hàng tồn kho cuối năm.

**4. Rủi ro của chiến lược dữ liệu (Risks to data strategy)**
- Thiếu dữ liệu.
- Việc bao gồm cả các chi phí cá nhân (personal expenses).
- Chi phí nguyên vật liệu và chi phí nhân công có thể không mang tính đại diện cho chi phí thay thế thực tế (true replacement costs) của chi phí nguyên vật liệu và nhân công trong tương lai.
- Khả năng có thành kiến (potential bias) trong việc tối thiểu hóa thông tin chi phí để làm cho công ty có vẻ có lợi nhuận cao hơn.

**Rủi ro của chiến lược phân tích (Risks to analysis strategy)**
- Việc lấy trung bình chi phí của tất cả các mô hình có thể không chính xác nếu chi phí thực tế của các mô hình khác nhau có sự khác biệt đáng kể.
- Hồi quy có thể không có sức mạnh giải thích cao (R-square).
- Chi phí có thể có sự khác biệt theo tính mùa vụ (seasonality differences) (do sự khan hiếm nguyên vật liệu hoặc chi phí làm nóng và làm mát).
- Công thức tính chi phí có thể cần được tính lại hằng năm để phản ánh những thay đổi của chi phí.

**5. Kiểm soát chiến lược dữ liệu (Data strategy controls)**
- Phỏng vấn Elisabeth bằng một danh sách các chi phí hàng tồn kho điển hình để phát hiện những chi phí bị bỏ sót.
- Hỏi về xu hướng mùa vụ hoặc kinh tế của nguyên vật liệu, nhân công và chi phí sản xuất chung, đồng thời sử dụng mức trung bình của điểm cao nhất và điểm thấp nhất.

**Kiểm soát chiến lược phân tích (Analysis strategy controls)**
- Sử dụng các xu hướng trung vị (median tendencies) thay vì trung bình (means).
- Chạy các mô hình độ nhạy (sensitivity models) với các giá trị chi phí thay thế tương lai để nhận diện các rủi ro tiềm tàng trong các ước tính chi phí sản phẩm cuối cùng và khả năng thiên lệch dữ liệu.


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


**MỤC TIÊU HỌC TẬP 4 (LEARNING OBJECTIVE 4)**
**Tóm tắt dữ liệu và các chiến lược phân tích trong các lĩnh vực thực hành chuyên môn.**

Là bước cuối cùng của giai đoạn lập kế hoạch phân tích dữ liệu, các chuyên gia kế toán trong nhiều lĩnh vực thực hành thiết kế dữ liệu và các chiến lược phân tích dựa trên mục tiêu dự án của họ. Tại đây, chúng tôi đưa ra các ví dụ về các chiến lược dữ liệu và phân tích phổ biến cho các lĩnh vực thực hành chuyên môn về hệ thống thông tin kế toán (accounting information systems - AIS), kiểm toán (auditing), kế toán tài chính (financial accounting), kế toán quản trị (managerial accounting), và kế toán thuế (tax accounting).

### Hệ thống Thông tin Kế toán (Accounting Information Systems)

Bởi vì hệ thống thông tin kế toán của công ty tham gia vào việc lập kế hoạch, thực thi, kiểm soát và báo cáo các hoạt động của doanh nghiệp, các dự án phân tích dữ liệu trong lĩnh vực này thường liên quan đến dữ liệu và kiến thức liên ngành (interdisciplinary data and knowledge). Mục tiêu của các dự án này có thể có phạm vi từ việc chỉ tác động đến một hoặc hai nhân viên cho đến liên quan đến hầu hết toàn bộ tổ chức. Cả bốn loại mục tiêu phân tích (mô tả, chẩn đoán, dự đoán và đề xuất) đều thường được sử dụng.

Các phân tích dữ liệu AIS thường phân tích dữ liệu CNTT hoạt động với các mức độ toàn vẹn dữ liệu (data integrity) và tài liệu kiểm soát khác nhau. Dữ liệu kế toán truyền thống hơn thường được phân tích với dữ liệu định danh (categorical) và dữ liệu thứ bậc (ordinal) mang tính định tính (qualitative):
- Số lượng các phiếu hỗ trợ (help tickets) và sự cố.
- Số lượng lỗi và thời gian trễ (delay times).
- Các vấn đề đăng nhập.
- Mức độ hài lòng với hệ thống và hài lòng với dịch vụ CNTT.

Ví dụ, Hình minh họa 4.20 là một ví dụ về hình ảnh trực quan (visualization) số lượng các yêu cầu dịch vụ (service requests) hàng tháng liên quan đến hệ thống thông tin kế toán của một công ty. Mục tiêu là xác định xem có bao nhiêu tháng và những tháng nào có số lượng yêu cầu dịch vụ vượt quá công suất (capacity) 90 yêu cầu của đội ngũ nhân viên CNTT.

![ILLUSTRATION 4.20](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.20.png)

Các dự án phân tích dữ liệu AIS cũng có thể chọn các chiến lược dữ liệu sử dụng dữ liệu khoảng (interval) và tỷ lệ (ratio) mang tính định lượng (quantitative):
- Các chi phí như cài đặt và cập nhật thiết bị, phần mềm, và chi phí nhân công CNTT.
- Biến động ngân sách (budget variances) cho bất kỳ chi phí nào trong số này.

Điều quan trọng là chọn dữ liệu nắm bắt được hiệu suất, lỗ hổng (vulnerabilities), và các lỗi của hệ thống AIS. Ví dụ, để phân tích hiệu suất, chúng ta có thể phân tích số lượng email rác (dữ liệu tỷ lệ) trước và sau khi đầu tư vào tường lửa (firewall) mới.

Các kế toán viên thiết kế chiến lược phân tích cho các dự án AIS tập trung vào việc gia tăng lợi thế cạnh tranh và cải thiện hoạt động của tổ chức. Họ thường sử dụng số liệu thống kê để hiểu họ nên tập trung vào thành phần nào của hệ thống kế toán. Tính hình thức toán học (mathematical formality) của các công cụ thống kê có thể giúp thuyết phục ban quản lý thực hiện các khoản đầu tư cần thiết.

Có những rủi ro liên quan đến sự lựa chọn dữ liệu và lựa chọn phân tích AIS. Một số rủi ro chiến lược và quan trọng phổ biến cùng với các kiểm soát được đề xuất đối với dữ liệu và phân tích AIS được liệt kê trong Hình minh họa 4.21.

![ILLUSTRATION 4.21](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.21.png)

### Kiểm toán (Auditing)

Sự phản đối của các kiểm toán viên đối với sự thay đổi trong quá khứ, do rủi ro kiện tụng cao (high litigation risks) và sự xem xét của Ủy ban Giám sát Kế toán Công ty Đại chúng (Public Accounting Oversight Board - PCAOB) đối với các quy trình kiểm toán, đang dần biến mất khi các công nghệ mới giúp họ thực hiện các cuộc kiểm toán có chất lượng cao hơn, rủi ro thấp hơn và hiệu quả hơn. Các công ty kiểm toán đang ngày càng đầu tư nhiều hơn vào công nghệ và những cách thức mới để sử dụng chúng. Họ đang tổ chức lại để cung cấp các dịch vụ mới nhằm mang lại nhiều thông tin kinh doanh và giá trị kinh tế hơn cho khách hàng của mình.

Các kiểm toán viên sử dụng số liệu thống kê để xác định rủi ro đối với số dư tài khoản và các giao dịch bất thường, đặc biệt là trong các bút toán nhật ký liên quan đến các ước tính và giả định. Họ thường làm việc với các loại nguồn dữ liệu khác nhau, từ tài liệu quy trình, bút toán nhật ký, sổ cái và sổ chi tiết, bảng cân đối số phát sinh (trial balances), đến các tỷ số tài chính. Kiểm toán viên sử dụng các chiến lược phân tích để:
- Các mô-đun kiểm toán liên tục (Continuous auditing modules) để kiểm tra các quần thể dữ liệu lớn thay vì lấy mẫu kiểm tra với những rủi ro suy diễn (inference risks).
- Tự động nhận diện dữ liệu rác, các giao dịch bất thường, và các bất thường về mô hình để giảm thiểu rủi ro kiểm toán và rủi ro gian lận tốt hơn.
- Kiểm tra các kiểm soát nội bộ của toàn bộ chu trình giao dịch bằng khai phá quy trình (process mining) và truy xuất dòng chảy từ mua hàng đến thanh toán, việc sử dụng thẻ tín dụng mua hàng (P-cards) và tài liệu tiền lương. Kiểm tra chu trình doanh thu từ khâu đặt hàng đến khâu thu tiền.
- Sử dụng Tự động hóa quy trình bằng robot (Robotic Process Automation - RPA) để loại bỏ yếu tố con người (và thường không nhất quán) trong các nhiệm vụ kiểm toán lặp đi lặp lại, giải phóng kiểm toán viên để họ tập trung vào các lĩnh vực đòi hỏi tư duy phản biện và những phán đoán sâu sắc. (Các ứng dụng RPA và lợi ích đối với kế toán viên sẽ được giải thích trong chương đề cập đến các bước phát triển của dữ liệu và phân tích trong kế toán).
- Kiểm tra các giả thuyết về hàng tồn kho và tài sản cố định thông qua việc lấy mẫu, kiểm tra thống kê, và các suy diễn (inferences) cho tổng thể của những tài sản này.

Hình minh họa 4.22 là một ví dụ về việc kiểm toán viên sử dụng chiến lược phân tích khai phá quy trình (process mining) để tìm hiểu xem liệu tất cả các khoản mua hàng có tuân theo đúng quy trình từ yêu cầu mua hàng (requisition) đến ghi nhận hóa đơn mua hàng hay không. Hình ảnh trực quan chỉ ra rằng số lượng mua hàng nhiều hơn dự kiến (308 lần mua hàng) đã bỏ qua bước quy trình yêu cầu mua hàng được ủy quyền cũng như các bước xác nhận đơn hàng, nhận hàng và hóa đơn của nhà cung cấp được ủy quyền. Những sự sai lệch so với quy trình được ủy quyền này là điều đáng lo ngại đối với một kiểm toán viên. Các ô màu xanh lam chỉ ra những vị trí mà quy trình cho phép đơn đặt hàng lọt vào mà không có yêu cầu mua hàng và để cho các đơn đặt hàng đi ra mà không qua các bước bắt buộc tiếp theo. Một kiểm toán viên sau đó sẽ muốn theo dõi các ngoại lệ (exceptions) đối với quy trình được ủy quyền này.

![ILLUSTRATION 4.22](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.22.png)

Bất kể các chiến lược dữ liệu và phân tích được sử dụng là gì, kiểm toán viên phải xác định các rủi ro và các kiểm soát cần thiết để đảm bảo họ có thể dựa vào (rely on) kết quả phân tích của mình (Hình minh họa 4.23).

![ILLUSTRATION 4.23](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.23.png)

### Kế toán Tài chính (Financial Accounting)

Kế toán tài chính chịu trách nhiệm chính trong việc thu thập, ghi chép, xử lý, lưu trữ, và báo cáo thông tin kế toán. Sự chính xác, sự kỹ lưỡng và tài liệu hóa là những yếu tố thiết yếu. Dữ liệu kế toán mà họ sử dụng để phân tích vừa được hướng dẫn vừa bị hạn chế bởi các quy tắc kế toán và sự tuân thủ các cơ quan chính phủ. Do các thang đo lường của các biến mà họ cần cho việc phân tích, kế toán tài chính có thể phải biến đổi dữ liệu (transform data) tùy thuộc vào các câu hỏi mục tiêu của họ. Các dữ liệu này thường bao gồm dữ liệu định danh, khoảng và tỷ lệ.

Mục đích của chiến lược phân tích dữ liệu có thể là mô tả và chẩn đoán dựa trên các quy tắc và quy định về kế toán tài chính tương ứng:
- Bản chất (Nature), thời gian (timing), và tính ủy quyền của các giao dịch (và chẩn đoán các vấn đề) được ghi nợ vào mỗi tài khoản.
- Hiệu quả và những điểm yếu của kiểm soát nội bộ.
- Tính đầy đủ và hợp lý của các bút toán điều chỉnh vào cuối kỳ.

Các kế toán tài chính cũng sử dụng các chiến lược phân tích được thiết kế cho các mục tiêu dự đoán và đề xuất liên quan đến kết quả tài chính cho các nhà quản lý và thành viên hội đồng quản trị. Một ví dụ là việc ước tính thông tin bổ sung sẽ được trình bày cùng với báo cáo tài chính của họ, chẳng hạn như:
- Xếp hạng các nguồn vốn (capital sources) thay thế và chi phí vốn (costs of capital) theo mức độ thuận lợi.
- Thu nhập ròng và dòng tiền trong tương lai từ các hoạt động kinh doanh, đầu tư, và tài trợ.
- Tác động của các chiến lược mới lên báo cáo tài chính.
- Chi phí dự kiến trong tương lai liên quan đến nợ tiềm tàng (contingent liabilities), chi phí lương hưu, các đơn vị kinh doanh mới hoặc việc ngừng hoạt động của các đơn vị kinh doanh.

Các kế toán tài chính sử dụng thống kê để xác định các cơ hội và vấn đề liên quan đến khả năng sinh lời, thanh khoản, và định giá doanh nghiệp. Họ phân tích các mã ngành định danh từ các nhóm tài sản đầu tư định danh của khách hàng – giữ đến ngày đáo hạn, kinh doanh, và sẵn sàng để bán – để đảm bảo rủi ro đa dạng hóa (diversification risks) và các chiến lược nắm giữ (holding strategies) như mong muốn.

Hình minh họa 4.24 là một biểu đồ thác nước (waterfall chart) cho thấy kết quả phân tích của một dự án với mục tiêu hiểu rõ hơn về dòng tiền thuần hàng tháng của một tổ chức theo từng tháng. Biểu đồ thác nước là một hình ảnh trực quan hữu ích để hiển thị các thành phần tích cực và tiêu cực của một sự thay đổi.

![ILLUSTRATION 4.24](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.24.png)

Hình ảnh trực quan thác nước này cho thấy sự thay đổi của dòng tiền đối với mỗi tháng. Ví dụ, trong tháng Hai, dòng tiền đã tăng thêm $2,350 nhưng sau đó lại giảm $900 trong tháng Ba. Giá trị ròng của tất cả các thay đổi hàng tháng khớp với tổng số (total). Giống như các kế toán viên khác, kế toán tài chính phải xác định các rủi ro tiềm ẩn trong chiến lược dữ liệu và phân tích của họ (Hình minh họa 4.25).

![ILLUSTRATION 4.25](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.25.png)

### Kế toán Quản trị (Managerial Accounting)

Các kế toán quản trị gia tăng giá trị cho tổ chức của họ thông qua các chiến lược phân tích dữ liệu khác nhau. Mục đích của hầu hết các phân tích dữ liệu trong kế toán quản trị là cải thiện việc lập kế hoạch, kiểm soát hoạt động (operational control), và ra quyết định để hỗ trợ sứ mệnh và các chiến lược của tổ chức. Loại phân tích dữ liệu này có giá trị trong việc cải thiện sự lựa chọn, thực thi và đánh giá chiến lược của tổ chức. Những loại phân tích này cũng có thể dẫn đến các quyết định trao cho nhân viên nhiều quyền truy cập vào thông tin hơn, từ đó cải thiện hiệu suất, và cuối cùng là cải thiện văn hóa và hoạt động của tổ chức.

Kế toán quản trị chuẩn bị các chiến lược phân tích, cả cho các mục tiêu thường xuyên và ad hoc (chỉ dùng một lần) cho từng bộ phận chức năng của tổ chức. Các chiến lược này sử dụng dữ liệu qua các thang đo lường để mô tả, chẩn đoán, dự đoán, và đề xuất các tác động chiến lược:
- Xác định những lĩnh vực mà sự đổi mới trong cơ cấu tổ chức, chính sách và quy trình kinh doanh sẽ tăng cường tính hiệu quả (efficiencies), ví dụ như để giảm bớt các bước không tạo thêm giá trị (non-value-added steps) và sự chậm trễ.
- Xác định những lĩnh vực mà sự đổi mới trong quan hệ đối tác kinh doanh, hoạt động, và kiểm soát nội bộ sẽ làm tăng tính hiệu lực (effectiveness).
- Tăng cường lợi thế cạnh tranh thông qua nhiều cơ hội thông tin kinh doanh mới.
- Cải thiện việc tuân thủ với tất cả các quy định về mặt pháp lý và quy định.

Kế toán quản trị có thể thực hiện phân tích dữ liệu để xác định những lợi ích tiềm năng đối với quy trình kinh doanh và kiểm soát nội bộ của việc tự động hóa quy trình từ yêu cầu mua hàng đến hóa đơn của nhà cung cấp (xem Hình minh họa 4.22). Việc tự động hóa có thể buộc tất cả các phòng ban phải tuân theo quy trình kinh doanh đã được ủy quyền thay vì đi đường vòng. Việc xác định rủi ro đối với dữ liệu và phân tích được sử dụng trong kế toán quản trị là rất quan trọng để đảm bảo kết quả phân tích chính xác và đáng tin cậy (Hình minh họa 4.26).

**ÁP DỤNG TƯ DUY PHẢN BIỆN 4.7 (APPLYING CRITICAL THINKING 4.7): Sử dụng Đa ngành trong Kế toán Quản trị**
Cơ sở kiến thức mà các kế toán quản trị cần là rất rộng, liên quan đến nhiều ngành (multiple disciplines). Ví dụ, để giảm chi phí vận hành nhà máy, kế toán quản trị phải hiểu được kỹ thuật (engineering) của các máy móc sản xuất và biết cách tạo ra các mô hình thống kê đáng tin cậy cho sản xuất trong tương lai (Kiến thức - Knowledge):
- Các khái niệm kế toán và kinh tế
- Hành vi tổ chức (Organizational behavior)
- Quản trị vận hành (Operations management)
- Các công cụ công nghệ
- Các chuyên ngành phân tích định lượng (Quantitative analyses disciplines)

![ILLUSTRATION 4.26](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.26.png)

### Kế toán Thuế (Tax Accounting)

Nhờ vào phân tích dữ liệu, các kế toán thuế có nhiều thông tin hơn cho các dịch vụ tuân thủ và lập kế hoạch thuế của mình, điều này giúp cải thiện những phán đoán và cách họ lập hồ sơ bảo vệ quan điểm của mình trước khách hàng cũng như các cơ quan quản lý. Các cuộc khảo sát gần đây cho thấy hơn 58% các kế toán thuế đang sử dụng dữ liệu và các chiến lược phân tích cho nhiều lĩnh vực trong thực hành chuyên môn của họ, bao gồm:
- Thuế bán hàng, thuế sử dụng và thuế địa phương (SALT).
- Thuế giá trị gia tăng (VAT).
- Thuế hàng hóa và dịch vụ (GST).
- Thuế hải quan (Customs duties).
- Định giá chuyển nhượng (Transfer pricing) và các giao dịch nội bộ công ty (intercompany transactions).
- Tuân thủ thuế.
- Dự phòng thuế (Tax provisions).

Có lẽ tác động lớn nhất của các chiến lược phân tích dữ liệu đối với thực hành thuế là sự chuyển dịch khỏi sự phụ thuộc vào dữ liệu lịch sử và hướng tới góc nhìn cung cấp dịch vụ gia tăng giá trị, hướng tới tương lai (forward-looking) bằng cách sử dụng các chiến lược phân tích dự đoán và đề xuất. Các ví dụ về các phân tích dự đoán và đề xuất này bao gồm việc sử dụng mô hình dữ liệu phức tạp để đánh giá các phương án quyết định và vị thế (position alternatives), giúp cải thiện giá trị và độ chính xác của lời khuyên. Hình minh họa 4.27 là một bảng điều khiển động (live dashboard) cho thấy chi phí y tế năm hiện tại so với mức cần thiết đối với khoản khấu trừ từng khoản (itemized deductions) cho năm khách hàng cá nhân của họ. Điều này sẽ giúp kế toán thuế cung cấp lời khuyên cho những khách hàng này.

**ÁP DỤNG TƯ DUY PHẢN BIỆN 4.8 (APPLYING CRITICAL THINKING 4.8): Tư duy Phản biện trong Kế toán Thuế**
- Các kế toán thuế cân nhắc đến khách hàng, cơ quan thuế, và các đối tác công ty thuế của họ khi lên kế hoạch cho các phân tích dữ liệu khác nhau. Mỗi bên liên quan này có thể có những mục tiêu và ưu tiên khác nhau. Ví dụ, khách hàng có thể ưu tiên việc tối thiểu hóa nghĩa vụ thuế của họ, do đó đó sẽ là mục tiêu của các dịch vụ lập kế hoạch thuế của bạn (Các bên liên quan - Stakeholders).
- Các kỹ năng nghiên cứu và phân tích vững chắc là rất cần thiết, chẳng hạn như khi thực hiện nghiên cứu thuế, phát triển chiến lược thuế, và ước tính nghĩa vụ thuế. Ví dụ, luật tiểu bang khác với luật quốc gia và quốc tế đối với mỗi loại hạng mục thuế (Kiến thức - Knowledge).
- Khách hàng, cả cá nhân và tổ chức, có thể có động cơ để bỏ sót các khoản doanh thu chịu thuế và đưa vào các khoản chi phí không liên quan và không phù hợp. Những rủi ro dữ liệu này cần được kiểm soát, có lẽ bằng các câu hỏi phỏng vấn cũng như xác minh các hồ sơ được cung cấp thông qua các bài kiểm tra gián tiếp về tính hợp lý (Rủi ro - Risks).

Một ví dụ khác là việc truy vấn tinh vi dữ liệu kế toán của khách hàng để nhận diện tốt hơn các cơ hội, chẳng hạn như khi nào nên mua hoặc bán tài sản, và hiểu được các quyết định hoạt động thúc đẩy nghĩa vụ thuế.

![ILLUSTRATION 4.27](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.27.png)

![ILLUSTRATION 4.28](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.28.png)

---

### Áp dụng (Apply It 4.4)
**Ghép nối Các Chiến lược với Các Lĩnh vực Thực hành Chuyên môn (Match Strategies with Professional Practice Areas)**

Đối với mỗi mục tiêu phân tích và dữ liệu dưới đây:
1. Xác định thang đo lường dữ liệu sẽ được sử dụng.
2. Xác định một lĩnh vực thực hành có khả năng thực hiện phân tích đó.

Một số lựa chọn có nhiều hơn một câu trả lời đúng cho cả (1) và (2), nhưng hãy chỉ nhập một câu trả lời đúng cho mỗi mục.
**Các Thang đo lường Dữ liệu:** định danh (categorical), thứ bậc (ordinal), khoảng (interval), tỷ lệ (ratio)
**Các Lĩnh vực Thực hành:** Hệ thống thông tin kế toán, Kiểm toán, Kế toán tài chính, Kế toán quản trị, Kế toán thuế

**GIẢI PHÁP (SOLUTION)**

| Mục tiêu (Objective) | Thang đo lường (Measurement Scale) | Lĩnh vực thực hành (Practice Area) |
| --- | --- | --- |
| Lập báo cáo tuổi nợ của các hóa đơn chưa thanh toán cuối năm của khoản phải thu dựa trên số ngày quá hạn. | Khoảng (Interval) | Kế toán tài chính và quản trị |
| Dự đoán tiết kiệm chi phí và tăng năng suất từ các khoản đầu tư AIS mới. | Tỷ lệ (Ratio) | Kế toán quản trị |
| Tạo kế hoạch lấy mẫu phân tầng theo giá trị đô la (dollar value stratified sampling) cho các tài khoản tài sản đầu tư. | Khoảng (Interval) | Kiểm toán |
| Đánh giá các sự cố bảo mật máy chủ web theo loại sự cố. | Định danh (Categorical) | Hệ thống thông tin kế toán |
| Đề xuất mức tăng doanh thu sản phẩm theo từng sản phẩm từ các chiến dịch tiếp thị. | Tỷ lệ (Ratio) | Kế toán quản trị |
| Dự đoán dòng tiền tương lai từ các hoạt động kinh doanh. | Tỷ lệ (Ratio) | Kế toán quản trị |
| Tính toán những cải tiến quy trình trước và sau từ các khoản đầu tư hệ thống. | Khoảng (Interval) | Hệ thống thông tin kế toán |
| Kiểm tra các chiến lược lập kế hoạch thuế khác nhau bằng cách đánh giá số tiền tiết kiệm được trong tương lai. | Tỷ lệ (Ratio) | Kế toán thuế |
| Ước tính số lượng hàng tồn kho vào cuối năm bằng cách lấy mẫu một vài cửa hàng và thực hiện suy diễn (inferences) trên tổng thể. | Tỷ lệ (Ratio) | Kiểm toán |
| Kiểm tra các phê duyệt và tài liệu cho việc ủy quyền giao dịch. | Định danh (Categorical) | Kế toán tài chính |

Việc xác định rủi ro và đảm bảo có sẵn các kiểm soát thích hợp để giảm thiểu rủi ro cũng rất quan trọng.


**Ôn tập và Thực hành Chương (Chapter Review and Practice)**
**Ôn tập Các Mục tiêu Học tập (Learning Objectives Review)**

❶ **Xác định các thành phần của một kế hoạch dự án phân tích dữ liệu.**
Một kế hoạch dự án phân tích dữ liệu là một bản thiết kế (blueprint) để tuân theo cho dự án. Việc sử dụng một công cụ lập kế hoạch có thể giúp chọn ra dữ liệu và các chiến lược phân tích tốt nhất cho các mục tiêu của dự án. Có năm bước:
- **Bước 1:** Tập trung vào mục tiêu của dự án và các câu hỏi cụ thể cần được trả lời.
- **Bước 2:** Quyết định những dữ liệu nào là cần thiết để trả lời các câu hỏi, phát triển các phương án thay thế, đánh giá và xếp hạng phương án tốt nhất.
- **Bước 3:** Xem xét các phương pháp có sẵn để thực hiện phân tích và xếp hạng các phương án thay thế. Đánh giá và chọn tùy chọn chiến lược tốt nhất.
- **Bước 4 và 5:** Xem xét các rủi ro quan trọng cố hữu đối với cả chiến lược dữ liệu và chiến lược phân tích.
- **Bước 4 và 5:** Tích hợp các kiểm soát để giảm thiểu những rủi ro này trong chiến lược dữ liệu và chiến lược phân tích.

❷ **Mô tả cách phát triển một chiến lược dữ liệu.**
Một dự án thành công phụ thuộc vào việc sử dụng dữ liệu phù hợp và đánh giá các đặc điểm của nó. Việc xem xét tác động tiềm ẩn của dữ liệu lên phân tích và bất kỳ rủi ro nào giúp dễ dàng chọn ra dữ liệu phù hợp nhất cho các mục tiêu của dự án:
- Bước đầu tiên là chọn dữ liệu phù hợp nhất. Dữ liệu phù hợp là dữ liệu có sẵn và liên quan đến các câu hỏi mục tiêu phân tích dữ liệu.
- Các thang đo lường của dữ liệu cũng phải phù hợp để sử dụng với phương pháp phân tích dữ liệu đã chọn, vì không phải tất cả các phân tích đều hợp lệ cho mọi thang đo. Dữ liệu có thể có các thang đo định danh (categorical), khoảng (interval), thứ bậc (ordinal), hoặc tỷ lệ (ratio).
- Dữ liệu có thể là nội bộ (internal - được tạo ra bên trong tổ chức), bên ngoài (external - thu được từ một nguồn bên ngoài tổ chức), hoặc kết hợp cả hai. Dữ liệu có thể là các số đo thô (raw measures) hoặc dữ liệu thô chưa đo lường (assigned non-measures), và cũng có thể là các trường được tính toán (calculated fields).
- Xem xét các rủi ro tiềm ẩn liên quan đến dữ liệu được chọn để phân tích và đưa ra các kiểm soát để giảm thiểu những rủi ro đó. Ba rủi ro dữ liệu phổ biến (và các kiểm soát) bao gồm: mẫu không mang tính đại diện (non-representative samples - xác minh tính đại diện của mẫu), các điểm dữ liệu ngoại lai (outlier data points - xác định các điểm ngoại lai và sau đó biện minh hoặc loại bỏ), và dữ liệu rác (dirty data - xác minh tính toàn vẹn của tập dữ liệu và làm sạch).

❸ **Giải thích cách một chiến lược phân tích được thiết kế.**
Có hai điều cần xem xét khi thiết kế một chiến lược phân tích dữ liệu: (1) các câu hỏi mục tiêu và (2) thang đo lường của dữ liệu. Có bốn mục tiêu phân tích dữ liệu: mô tả (descriptive), chẩn đoán (diagnostic), dự đoán (predictive), hoặc đề xuất (prescriptive). Các câu hỏi chúng ta thiết kế dựa trên mục tiêu:
- Khi thiết kế bất kỳ loại phân tích nào, phân tích phù hợp phụ thuộc vào thang đo lường của dữ liệu. Các phương pháp phân tích mô tả và chẩn đoán điển hình bao gồm số đo xu hướng trung tâm (measure of central tendency - giá trị trung bình, trung vị), phân phối tần suất (frequency distributions), số đo độ phân tán dữ liệu (measures of data dispersion - ví dụ: khoảng, các tứ phân vị, độ lệch chuẩn), hình ảnh trực quan (visualizations), sự tương quan (correlation), và các phép tính toán (ví dụ: tổng số, phần trăm thay đổi).
- Các phân tích điển hình được sử dụng cho phân tích dự đoán và đề xuất bao gồm đường xu hướng (trendlines), phân tích hồi quy (regression analysis), các mô hình tối ưu hóa (optimization models), và phân tích độ nhạy giả định (what-if analyses).
- Có nhiều rủi ro phổ biến cố hữu trong các phân tích mô tả, chẩn đoán, dự đoán, và đề xuất có thể được xác định và kiểm soát. Một số rủi ro này bao gồm việc thực hiện phân tích với dữ liệu rác, hoặc phân tích không phù hợp với các thang đo của biến, sử dụng mẫu quá nhỏ, hoặc mẫu không mang tính đại diện, hoặc đưa vào (hoặc bỏ sót) các biến khỏi phân tích.

❹ **Tóm tắt dữ liệu và các chiến lược phân tích trong các lĩnh vực thực hành chuyên môn.**
Mỗi lĩnh vực thực hành chuyên môn kế toán lập kế hoạch dữ liệu và các chiến lược phân tích khác nhau cho những mục tiêu khác nhau, sử dụng dữ liệu với nhiều thang đo lường để mô tả, chẩn đoán, dự đoán, và đề xuất kết quả cho các bên liên quan và mục tiêu của họ. Các rủi ro cố hữu trong các lựa chọn dữ liệu và phân tích của họ, cũng như các kiểm soát mà họ thực hiện là một chức năng từ vai trò, trách nhiệm, và mục tiêu dự án của họ:
- Các chuyên gia hệ thống thông tin kế toán lập kế hoạch dữ liệu và chiến lược phân tích cho các mục tiêu quản trị AIS, đánh giá và lập kế hoạch chiến lược, hiệu suất hoạt động, và tuân thủ. Các dự án của họ thường liên quan đến chức năng quy trình kinh doanh, thông tin kinh doanh, và các mục đích an ninh mạng.
- Các kiểm toán viên lập kế hoạch dữ liệu và phân tích có các mục tiêu về chất lượng kiểm toán và tuân thủ quy trình kiểm toán chuyên nghiệp để xác minh tính đại diện của các số dư báo cáo tài chính của khách hàng hoặc hệ thống kế toán của tổ chức họ. Các kiểm toán viên độc lập (external auditors) có thêm các rủi ro dữ liệu khi sử dụng dữ liệu đã được khách hàng của họ thu thập và trích xuất, thường là không thể xác minh tính đầy đủ hoặc chính xác của dữ liệu.
- Kế toán tài chính tập trung vào sự tuân thủ quy định liên quan đến các mục tiêu thu thập, ghi chép, xử lý, lưu trữ, và báo cáo giao dịch.
- Kế toán quản trị có nhiều mục tiêu quản trị nội bộ, chiến lược, tài trợ, đầu tư, và hoạt động đối với dữ liệu và các kế hoạch phân tích của họ.
- Kế toán thuế tập trung vào cả việc tuân thủ và các cơ hội lập kế hoạch thuế hướng tới tương lai để phục vụ khách hàng và tổ chức bằng các kế hoạch chiến lược phân tích dữ liệu của họ. Tương tự như các kiểm toán viên độc lập, các kế toán thuế thường phải sử dụng các tập dữ liệu do khách hàng của họ chuẩn bị, điều này có thể có rủi ro cao hơn về sự không chính xác và không đầy đủ.

**Ôn tập Các Thuật ngữ Chính (Key Terms Review)**
- Các thuộc tính (Attributes) 4-12
- Dữ liệu được tính toán (Calculated data) 4-14
- Tập dữ liệu (Data set) 4-12
- Dữ liệu rác (Dirty data) 4-16
- Các trường (Fields) 4-12
- Dữ liệu số thô đo lường (Measured raw numeric data) 4-13
- Thang đo lường (Measurement scale) 4-14
- Dữ liệu thô chưa đo lường (Non-measured raw data) 4-13
- Các bản ghi (Records) 4-12
- Biến (Variable) 4-20

---

**CÁCH LÀM (HOW TO) 4.1**
**Tính toán Ước tính Nợ khó đòi Cuối năm Sử dụng Excel (Calculate Year-End Bad Debts Estimation Using Excel)**
Các số liệu hiển thị trong bảng ở Hình minh họa 4.2 được tính toán bằng Excel. Hãy nhớ lại một vài dữ kiện về ví dụ này:
- WeMakeIt, Inc. ước tính rằng 2% của các khoản phải thu quá hạn từ 30 đến 60 ngày sẽ không thể thu hồi, và 30% của các khoản phải thu quá hạn lớn hơn 60 ngày sẽ không thể thu hồi.
- Số dư chưa điều chỉnh của tài khoản dự phòng các khoản phải thu khó đòi cuối năm 2025 là $3,000.

**Bạn Cần Gì:** Dữ liệu: Tệp dữ liệu How To 4.1.

**BƯỚC 1:** Chọn toàn bộ tập dữ liệu, nhưng không chọn các nhãn (labels), và sắp xếp dữ liệu hóa đơn chưa thanh toán theo ngày hóa đơn. Tùy chọn `Sort` xuất hiện trong tab `Data`. (Hình minh họa 4.29)

![ILLUSTRATION 4.29](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.29.png)

**BƯỚC 2:** Tạo một cột mới ở bên phải của dữ liệu cho ngày cuối năm là 12/31/2025:
- Thêm một tên nhãn cho cột này ở hàng 1: “Analysis Date.”
- Ở hàng 2, nhập “12/31/2025” và sao chép ngày này xuống hàng dữ liệu cuối cùng. Việc này có thể được thực hiện dễ dàng bằng cách nhấp vào góc dưới cùng của ô đã nhập “12/31/2025” và kéo con trỏ xuống hàng dữ liệu cuối cùng (Hình minh họa 4.30).

![ILLUSTRATION 4.30](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.30.png)

**BƯỚC 3:** Tạo một cột mới ở bên phải của cột ngày 12/31/2025:
- Thêm một tên nhãn cho cột này ở hàng 1: “Days Outstanding.”
- Tính số ngày quá hạn bằng cách tạo một công thức trong ô G2, công thức này trừ ngày hóa đơn (Ô C2) khỏi ô ngày 12/31/2025 (F2) của `Analysis Date`. Công thức là `=F2-C2`.
- Sao chép công thức này qua tất cả các hàng dữ liệu trong Cột G. Việc sao chép có thể được thực hiện bằng cách nhấp vào góc dưới cùng của ô đã nhập công thức và kéo xuống hàng dữ liệu cuối cùng, (Hình minh họa 4.31).

![ILLUSTRATION 4.31](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.31.png)

**BƯỚC 4:** Chọn các tiêu đề trường dữ liệu và các hàng dữ liệu rồi tạo một `PivotTable`. Tùy chọn này nằm trong menu `Insert` trên Excel (Hình minh họa 4.32).

![ILLUSTRATION 4.32](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.32.png)

Chọn `New Worksheet`. Màn hình của bạn sẽ tự động chuyển sang trang tính mới. Đặt tên cho bảng này là “BadDebts2025.” Tên xuất hiện ở trên cùng bên trái màn hình của bạn.

**BƯỚC 5:** Chọn bất kỳ vị trí nào trong PivotTable để `PivotTable Fields` xuất hiện ở bên phải màn hình của bạn:
- Kéo `Invoice Amount` vào vùng `Values`.
- Kéo `Days Outstanding` vào `Rows`. Giải pháp PivotTable mới sẽ xuất hiện (Hình minh họa 4.33).

![ILLUSTRATION 4.33](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.33.png)

**BƯỚC 6:** Tiếp theo, chọn bất kỳ hàng nào trong cột `Days Outstanding`:
- Nhấp chuột phải và chọn `Group`.
- Trong hộp thoại mở ra (Hình minh họa 4.34), nhập số không (0) vào điểm bắt đầu (Starting at), 60 vào điểm kết thúc (Ending at), và sau đó nhập 30 cho tùy chọn `By`. Chọn `OK`.

![ILLUSTRATION 4.34](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.34.png)

Bây giờ PivotTable đã trở thành ba hàng cho ba danh mục độ tuổi mong muốn, với các tổng phụ (subtotals) đã được tính toán cho cột `Sum of InvoiceAmount`. Định dạng cột Sum dưới dạng tiền tệ (currency) (Hình minh họa 4.35). Định dạng các số tiền dưới dạng tiền tệ.

**BƯỚC 7:** Trong ô bên phải của tiêu đề `SumofInvoiceAmount`, nhập “Estimation %.” Trong ô bên phải tiếp theo, nhập “$ Uncollectible.” Điều chỉnh độ rộng cột:
- Trong ô bên phải của `$ 20,441.46`, nhập “0.02,” và trong ô bên dưới nhập “0.3” cho các tỷ lệ phần trăm không thể thu hồi.
- Định dạng cột `$ Uncollectible` dưới dạng tiền tệ.

**BƯỚC 8:** Trong các ô bên phải của mỗi tỷ lệ phần trăm này, nhập các công thức sau bằng cách sử dụng tham chiếu ô:
- Đối với nhóm 30-60 ngày, công thức là: `=(nhấp vào ô chứa 20441.46)*(nhấp vào ô chứa 0.02)`
- Và đối với nhóm >60 ngày: `=(nhấp vào ô chứa 33193.55)*(nhấp vào ô chứa 0.3)`
- Một ví dụ về công thức và các tổng số kết quả được hiển thị trong Hình minh họa 4.36. Thêm một đường gạch chân vào ô chứa công thức cuối cùng.

![ILLUSTRATION 4.35](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.35.png)

![ILLUSTRATION 4.36](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.36.png)

**BƯỚC 9:** Nhập công thức tính tổng (sum) trong ô tiếp theo (D7 trong ví dụ giải pháp này):
`=sum(D5:D6)`
Tổng này là số dư có cuối năm đã điều chỉnh mong muốn của tài khoản dự phòng các khoản phải thu khó đòi. Tổng này là $10,366.89 (cũng được hiển thị trong Hình minh họa 4.37).

**BƯỚC 10:** So sánh số dư tài khoản dự phòng chưa điều chỉnh năm 2025, là số dư có $3,000, với số dư cuối kỳ mong muốn đã tính toán để tính số tiền cần thiết cho bút toán điều chỉnh nhằm đảm bảo tài khoản dự phòng các khoản phải thu khó đòi có số dư có mong muốn đó:
- Nhập số dư chưa điều chỉnh vào ô D8 và công thức tính toán vào ô D10 (Hình minh họa 4.37): `=D7-D8`
- Bây giờ bạn đã sẵn sàng để thực hiện bút toán điều chỉnh của mình:
Nợ Chi phí nợ khó đòi 7,366.89
Có Dự phòng các khoản phải thu khó đòi 7,366.89

![ILLUSTRATION 4.37](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.37.png)

---

**CÁCH LÀM (HOW TO) 4.2**
**Tạo Biểu đồ Cột Tần suất trong Power BI (Create a Frequency Bar Chart in Power BI)**
Hình minh họa 4.16 có thể được tạo lại trong Power BI bằng cách phân tích các hóa đơn chưa thanh toán trong các khoản phải thu theo khách hàng và tạo một hình ảnh trực quan hiển thị số lượng hóa đơn chưa thanh toán thuộc nợ của các khách hàng duy nhất vào cuối năm 2024 và 2025 theo ba nhóm: 1-3 hóa đơn, 4-6 hóa đơn, và 7-9 hóa đơn.

**Bạn Sẽ Cần Gì:** Dữ liệu: Tệp dữ liệu How To 4.2.

**BƯỚC 1:** Tải tập dữ liệu lên Power BI:
- Mở Power BI và Chọn `Get Data`.
- Chọn `Import data from Excel` và chọn Excel Worksheet.
- Điều hướng đến tệp tập dữ liệu đã lưu và mở nó.

![ILLUSTRATION 4.38](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.38.png)

Khi cửa sổ `Navigator` mở ra, chọn `Sheet 1` của tệp được liệt kê ở bên trái, sau đó chọn `Load` (Hình minh họa 4.38).
- Xác minh việc nhập này bằng cách nhấp đúp vào biểu tượng bảng dữ liệu ở phía bên trái màn hình. Nhìn vào góc dưới cùng bên trái để xác minh rằng bạn đã tải thành công toàn bộ 201 bản ghi của tập dữ liệu (Hình minh họa 4.39).

![ILLUSTRATION 4.39](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.39.png)

**BƯỚC 2:** Chọn cột `AnalysisDate`.
- Trong menu bên dưới `Column Tools`, kéo các tùy chọn Format Field xuống và chọn tùy chọn cuối cùng “2001 (yyyy)” (Hình minh họa 4.40).
- Xác minh trường ngày phân tích đã thay đổi để hiển thị năm 2024 và 2025.

![ILLUSTRATION 4.40](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.40.png)

**BƯỚC 3:** Chọn cột `CustID` bằng cách nhấp vào tiêu đề cột. Nhấp chuột phải và chọn `Edit Query` (Hình minh họa 4.41).

![ILLUSTRATION 4.41](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.41.png)

- Điều này sẽ mở cửa sổ Power Query Editor. Trong cửa sổ này, cột `CustID` cũng sẽ được chọn.
- Chọn `Group By` từ menu trên cùng, và nó sẽ mở ra.
- Chọn `Advanced`. Ngay bên dưới trường `CustID` bạn sẽ thấy nút `Add grouping`. Chọn nút này để thêm một nhóm thứ hai cho trường `AnalysisDate`. Sau đó, bên dưới hộp phân nhóm mới, trong hộp `New column name`, nhập “CountInvoices” (không nhập dấu ngoặc kép).
- Trong menu thả xuống của phần `Operation`, chọn `Count Distinct Rows` và chọn `OK`. Đóng và Áp dụng (Close and Apply) Power Query Editor (Hình minh họa 4.42).

![ILLUSTRATION 4.42](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.42.png)

**BƯỚC 4:** Chọn cột `Count Invoices`. Chọn `Data Groups` từ cột trên cùng, sau đó chọn `New Data Group` (Hình minh họa 4.43).

![ILLUSTRATION 4.43](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.43.png)

Hình minh họa 4.43 hiển thị hộp thoại mở ra sau khi bạn chọn Data Groups:
- Trong hộp thoại, chọn `List` (không phải bins) cho `Group Type`.
- Dưới mục `Ungrouped values`, giữ phím shift để chọn các giá trị 1, 2, và 3.
- Chọn `Group`. Nhấp đúp vào nhóm mới xuất hiện trên cửa sổ bên phải và đổi nhãn thành “1-3”.
- Chọn nhóm `Other`, và di chuyển sang phía không được phân nhóm ở bên trái. Chọn 4 và 5 cùng nhau bằng cách một lần nữa giữ phím shift. Chọn `Group` và di chuyển sang cửa sổ bên phải. Nhấp đúp vào nhãn cho trường này, và nhập “4-6” (tình cờ là không có khách hàng nào có sáu hóa đơn chưa thanh toán, nhưng khoảng này vẫn sẽ là 4-6).
- Một lần nữa, chọn `Other` và di chuyển đến cửa sổ `Ungrouped values`. Chọn 7, 8, và 9 bằng cách giữ phím shift và chọn `Group`.
- Quay lại bên phải và nhấp đúp vào nhãn cho nhóm này. Đổi nó thành “7-9.” Chọn `OK`. (Hình minh họa 4.44).

![ILLUSTRATION 4.44](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.44.png)

**BƯỚC 5:** Bây giờ bạn đã sẵn sàng để tạo hình ảnh trực quan của mình:
- Chọn biểu tượng vẽ biểu đồ ở bên trái màn hình.
- Chọn cả ba biến trong danh sách `Fields` của bạn.

Trong ô `Visualizations`, `Count Invoices (groups)` nên nằm trong vùng `axis`. Bạn có thể cần di chuyển trường `AnalysisDate` lên trường `Legend` bằng cách kéo nó. Trường `Count Invoices` nên nằm trong vùng `Values` (Hình minh họa 4.45).

![ILLUSTRATION 4.45](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.45.png)

Hình ảnh trực quan của bạn đã hoàn tất (Hình minh họa 4.46)!

![ILLUSTRATION 4.46](../TaiLieu/textbookForPractice/Figures/Ch_04/ILLUSTRATION%204.46.png)


**Câu hỏi Trắc nghiệm (Multiple Choice Questions)**

1. **(LO 1)** Điềunào sau đây không phải là mục tiêu của các chiến lược phân tích dữ liệu?
a. Thu thập dữ liệu.
b. Mô tả dữ liệu.
c. Chẩn đoán dữ liệu.
d. Dự đoán một giá trị tương lai của dữ liệu.
e. Đề xuất tác động của một chiến lược cụ thể lên giá trị tương lai của dữ liệu.

2. **(LO 1)** Các mục tiêu chẩn đoán trong các chiến lược phân tích dữ liệu liên quan đến điều nào sau đây?
a. Tìm kiếm sự độc lập hoàn toàn của các biến.
b. Tìm kiếm tính nhân quả (causality) trong các biến hồi quy.
c. Tìm kiếm nơi để đổ lỗi cho kết quả hoạt động kém.
d. Tìm kiếm các mối liên hệ (associations) giữa các biến dữ liệu.
e. Dự đoán kết quả tương lai sẽ là gì trong dữ liệu.

3. **(LO 1)** Các thành phần của một kế hoạch chiến lược phân tích dữ liệu hiệu quả xem xét từng điều sau đây, ngoại trừ
a. các kiểm soát phân tích.
b. các rủi ro phân tích.
c. các mục tiêu phân tích.
d. độ phức tạp của phân tích.

4. **(LO 1)** Câu hỏi cụ thể nào sau đây mô tả mục tiêu phân tích mô tả đối với số dư các khoản phải thu vào cuối năm?
a. Có bao nhiêu hóa đơn của năm hiện tại đã được thu tiền trong năm?
b. Tổng của tất cả doanh thu bán hàng, bán bằng tiền mặt và bán chịu, trong năm là bao nhiêu?
c. Có bao nhiêu nhân viên bán hàng đã được tuyển dụng tại Thành phố New York trong năm nay?
d. Số ngày tồn kho trung bình cho mỗi dòng sản phẩm của bạn là bao nhiêu?
e. Có bao nhiêu hóa đơn mở (chưa thanh toán) vào cuối năm đã quá hạn?

5. **(LO 1)** Bạn được yêu cầu thực hiện phân tích dự đoán số dư các khoản phải trả vào cuối năm. Nguồn dữ liệu nào sau đây là tốt nhất để phân tích cho mục tiêu này?
a. Danh sách các nhà cung cấp mới được ủy quyền trong năm.
b. Các hóa đơn mở của nhà cung cấp đề cập đến các giao dịch mua hàng đã được nhận.
c. Danh sách các séc đã thanh toán cho các nhà cung cấp khoản phải trả trong năm.
d. Danh sách các đơn đặt hàng được phát hành trong tháng 12.
e. Không có nguồn dữ liệu nào trong số này là hữu ích để dự đoán số dư cuối năm của các khoản phải trả.

6. **(LO 1)** Giả sử bạn được yêu cầu ước tính số tiền của các khoản phải thu không thể thu hồi vào cuối năm. Điều nào sau đây không phải là một rủi ro phân tích cần xem xét khi ước tính nợ khó đòi của các khoản phải thu vào cuối năm?
a. Số lượng nhân viên bán hàng toàn thời gian được báo cáo không chính xác.
b. Việc tính toán số ngày quá hạn (days outstanding) không chính xác.
c. Công ty đã thay đổi chính sách thu tiền đối với một số khách hàng nhất định.
d. Có những khách hàng mới không được đưa vào phân tích các khoản phải thu theo độ tuổi (aged receivables).
e. Có những sai sót toán học trong việc tính tổng các khoản phải thu.

7. **(LO 1)** Phản ứng nào sau đây là phù hợp đối với rủi ro dữ liệu khi mẫu được chọn để phân tích không phù hợp?
a. Thêm các biến bị thiếu để xem những thay đổi về sức mạnh giải thích.
b. Kiểm tra dạng phân phối mẫu cho các giả định kiểm định thống kê.
c. Xác minh tính đại diện của mẫu của bạn.
d. Giải thích quy tắc được sử dụng để loại bỏ dữ liệu ngoại lai.
e. Biết điểm dữ liệu ngoại lai của bạn.

8. **(LO 1)** Suy nghĩ phản biện thấu đáo về các rủi ro đối với một chiến lược phân tích dữ liệu trong quá trình lập kế hoạch sẽ giúp tránh được
a. các định kiến (biases) trong lựa chọn dữ liệu.
b. các sai sót phán đoán do thiếu kinh nghiệm.
c. các sai sót diễn giải từ các tập dữ liệu rác.
d. các ứng dụng không chính xác của các kiểm định thống kê.
e. Tất cả những điều này đều là những chi phí có thể xảy ra do không xem xét đến các rủi ro đối với các lựa chọn phân tích dữ liệu.

9. **(LO 1)** Một chiến lược phân tích dữ liệu có nhiều khả năng thành công hơn nếu bạn suy nghĩ phản biện về
a. các phân tích do các đối thủ cạnh tranh của bạn thực hiện.
b. các kết quả mà bạn muốn đạt được.
c. dữ liệu sẽ thông tin tốt nhất cho các câu hỏi của bạn.
d. các mục tiêu của bạn cho việc phân tích.
e. Không có điều nào trong số này giúp bạn thực hiện lập kế hoạch chiến lược phân tích dữ liệu tốt hơn.

10. **(LO 2)** Thuật ngữ nào sau đây đề cập đến nội dung của một hàng trong tập dữ liệu?
a. Trường dữ liệu (Data field).
b. Thuộc tính (Attribute).
c. Lần xuất hiện duy nhất của bản ghi dữ liệu (Single occurrence of the data record).
d. Tất cả những thuật ngữ này đều định nghĩa một hàng dữ liệu trong một tập dữ liệu.

11. **(LO 2)** Thuật ngữ nào sau đây có thể đề cập đến tên của một cột trong tập dữ liệu hóa đơn bán hàng?
a. Invoice 3570.
b. Khách hàng ở Orlando, Florida.
c. CustomerState.
d. BankStatementDate.
(Data: Thẻ Data xuất hiện khi dữ liệu cần thiết để trả lời câu hỏi hoặc hoàn thành bài tập có sẵn trên nền tảng học tập trực tuyến của Wiley).

12. **(LO 2)** Điều nào sau đây là ví dụ về kiến thức mà bạn có thể cần thu thập để lập kế hoạch chiến lược phân tích dữ liệu?
a. Phân tích này phù hợp với các thang đo lường dữ liệu của bạn.
b. Hiểu rõ về những định kiến (biases) của bạn.
c. Xác định các bên liên quan chính.
d. Các nguồn lực phân tích có sẵn cho khoản thù lao của bạn.
e. Sự tương quan giữa khoản thù lao với kết quả.

13. **(LO 2)** Thang đo lường dữ liệu nào sau đây không thể được sử dụng trong việc thiết kế chiến lược phân tích dữ liệu của bạn?
a. Dữ liệu tối ưu (Optimal data)
b. Dữ liệu thứ bậc (Ordinal data)
c. Dữ liệu khoảng (Interval data)
d. Dữ liệu tỷ lệ (Ratio data)
e. Tất cả những thang đo trên đều là thang đo lường dữ liệu.

14. **(LO 2)** Thang đo lường dữ liệu nào sau đây cho phép phép nhân các điểm dữ liệu có ý nghĩa?
a. Dữ liệu khoảng (Interval data)
b. Dữ liệu định danh (Categorical data)
c. Dữ liệu thứ bậc (Ordinal data)
d. Dữ liệu tỷ lệ (Ratio data)
e. Dữ liệu nhóm (Group data)

15. **(LO 3)** Các phân tích mô tả bao gồm số đo xu hướng trung tâm trung vị (median) phù hợp với thang đo lường dữ liệu nào?
a. Định danh (Categorical)
b. Thứ bậc (Ordinal)
c. Danh nghĩa (Nominal)
d. Khoảng (Interval)
e. Tất cả các thang đo lường này đều hỗ trợ số đo xu hướng trung tâm trung vị.

16. **(LO 3)** Các phân tích chẩn đoán bao gồm các số đo phân tán dữ liệu như phương sai (variance) và độ lệch chuẩn (standard deviation) phù hợp với thang đo lường dữ liệu nào?
a. Định danh (Categorical)
b. Thứ bậc (Ordinal)
c. Tỷ lệ (Ratio)
d. Danh nghĩa (Nominal)
e. Tất cả các thang đo lường đều phù hợp cho phân tích phương sai.

17. **(LO 3)** Hình ảnh trực quan bằng biểu đồ thanh (Bar chart) phù hợp với dữ liệu có thang đo lường nào?
a. Định danh (Categorical)
b. Thứ bậc (Ordinal)
c. Tỷ lệ (Ratio)
d. Danh nghĩa (Nominal)
e. Tất cả các thang đo lường đều phù hợp cho biểu đồ thanh.

18. **(LO 3)** Câu hỏi mục tiêu nào sau đây phản ánh mục đích chẩn đoán (diagnostic) đối với số dư các khoản phải thu cuối năm?
a. Có bao nhiêu hóa đơn chưa thanh toán (outstanding invoices) trong số dư các khoản phải thu cuối năm?
b. Giá trị của số dư các khoản phải thu cuối năm là bao nhiêu?
c. Có phải các khách hàng mới đang gây ra sự gia tăng của các hóa đơn chưa thanh toán trong số dư các khoản phải thu cuối năm so với năm ngoái không?
d. Giá trị trung vị (median value) cho các hóa đơn chưa thanh toán trong số dư các khoản phải thu cuối năm là bao nhiêu?
e. Hóa đơn nào đã quá hạn lâu nhất trong số dư các khoản phải thu cuối năm?

19. **(LO 3)** Các phân tích dự đoán và đề xuất bao gồm việc tạo ra các hình ảnh trực quan đường xu hướng (trendline) phù hợp với thang đo lường dữ liệu nào?
a. Định danh (Categorical)
b. Thứ bậc (Ordinal)
c. Danh nghĩa (Nominal)
d. Khoảng (Interval)
e. Tất cả các thang đo lường này đều hỗ trợ sử dụng hình ảnh trực quan đường xu hướng.

20. **(LO 2, LO 3)** Chiến lược phân tích nào trong số những chiến lược này liên quan đến các thang đo lường dữ liệu định danh (categorical) và tỷ lệ (ratio)?
a. Đối chiếu số dư sổ chi tiết (subsidiary ledger) với số dư sổ cái (general ledger).
b. Lịch trình khấu hao cho tất cả các tài sản bất động sản.
c. Các loại nguồn vốn nào có chi phí vốn cao nhất.
d. Các thay đổi đối với thuế suất áp dụng cho tổ chức của họ.

21. **(LO 4)** Kế toán quản trị sẽ có khả năng cao nhất lập kế hoạch phân tích dữ liệu khi điều nào sau đây xảy ra?
a. Những thay đổi về thuế suất.
b. Việc loại bỏ các yêu cầu công bố thông tin (footnote disclosure) trên báo cáo tài chính.
c. Những thay đổi đối với trang web của Ủy ban Chứng khoán và Giao dịch (Securities and Exchange Commission).
d. Những thay đổi đối với hiệu suất của tổ chức họ.

22. **(LO 4)** Kế toán viên AIS (Hệ thống Thông tin Kế toán) sẽ có khả năng cao nhất thiết kế một chiến lược phân tích dữ liệu cho cơ hội nào sau đây?
a. Các công nghệ mới có thể cung cấp việc tiết kiệm chi phí cho các quy trình hoạt động.
b. Các khách hàng mới trên thị trường.
c. Sự thay đổi trong ban lãnh đạo của cơ quan quản lý.
d. Những thay đổi đối với các công bố thông tin được yêu cầu bởi các nguyên tắc kế toán được chấp nhận chung.
e. Những thay đổi trong các quy định thuế.

23. **(LO 4)** Kiểm toán viên lập kế hoạch chiến lược phân tích dữ liệu cho những tình huống nào sau đây?
a. Đánh giá tính hiệu quả của các kiểm soát nội bộ trong hệ thống kế toán của khách hàng họ.
b. Đánh giá tính đại diện của một số dư tài khoản trên bảng cân đối kế toán hoặc báo cáo kết quả hoạt động kinh doanh của khách hàng họ.
c. Xem xét rủi ro liên quan đến việc cung cấp ý kiến kiểm toán (audit opinion) cho một khách hàng.
d. Điều tra xem liệu các giả định của khách hàng trong việc ghi nhận nợ thuê tài sản của họ có nhất quán với các công ty khác trong ngành của họ hay không.
e. Tất cả những điều này đều là các ví dụ về những tình huống mà kiểm toán viên lập kế hoạch cho các chiến lược phân tích dữ liệu của họ.

24. **(LO 4)** Kế toán tài chính sẽ có khả năng cao nhất lập kế hoạch các chiến lược phân tích dữ liệu cho điều nào sau đây?
a. Những thay đổi đối với ban quản lý.
b. Các đối thủ cạnh tranh mới trên thị trường.


**Bài tập Ngắn (Brief Exercises)**
**Câu hỏi Ôn tập (Review Questions)**

1. **(LO 1)** Mô tả năm thành phần trong một kế hoạch dự án phân tích dữ liệu.
2. **(LO 1)** Thảo luận lý do tại sao các chuyên gia kế toán lại cần tập trung vào mục tiêu và các câu hỏi để tạo ra các phương án thay thế về dữ liệu và phân tích.
3. **(LO 1)** Mô tả các rủi ro về dữ liệu và phân tích nên được xem xét khi lập kế hoạch một dự án phân tích dữ liệu.
4. **(LO 2)** Định nghĩa và mô tả bốn thang đo lường được sử dụng làm các biến dữ liệu kế toán.
5. **(LO 2)** Giải thích việc lựa chọn một số trường dữ liệu nhất định có thể không phù hợp cho kế hoạch dự án của bạn như thế nào.
6. **(LO 2)** Cung cấp các ví dụ về hai rủi ro dữ liệu phổ biến và một kiểm soát cho mỗi rủi ro có thể giảm thiểu rủi ro đó.
7. **(LO 3)** Thảo luận lý do tại sao việc biết thang đo lường của các biến được sử dụng trong phân tích lại quan trọng khi quyết định có nên thiết kế một chiến lược phân tích dữ liệu mô tả, chẩn đoán, dự đoán hay đề xuất.
8. **(LO 3)** Thảo luận lý do tại sao việc khớp (match) loại phân tích được thực hiện với thang đo lường của dữ liệu lại quan trọng.
9. **(LO 3)** Giải thích một chiến lược phân tích xu hướng (trend analyses), và đưa ra một ví dụ về cách một kế toán viên có thể phân tích doanh thu bán hàng bằng cách sử dụng phân tích xu hướng.
10. **(LO 4)** Giả sử bạn là một kế toán viên hệ thống đang làm việc trong nhóm hệ thống thông tin kế toán tại công ty của bạn. Bạn đã được yêu cầu thực hiện phân tích dữ liệu để phân tích số lượng email rác truyền đến nhân viên trước và sau khi công ty đầu tư vào tường lửa (firewall) mới. Thảo luận về các rủi ro dữ liệu và xác định các kiểm soát liên quan để giảm thiểu các rủi ro đó trong phân tích của bạn.
11. **(LO 4)** Giả sử bạn là một kiểm toán viên đang làm việc để kiểm tra các kiểm soát nội bộ liên quan đến việc sử dụng thẻ tín dụng mua hàng (p-card) tại một công ty. Bạn có các trường dữ liệu sau:
- EmployeeNumber
- EmployeeName
- P-cardTransactionDate
- P-cardTransaction vendor
- P-cardTransactionAmount
Mô tả một chiến lược phân tích mô tả mà bạn có thể thực hiện bằng cách sử dụng chiến lược dữ liệu của số tiền giao dịch p-card (P-cardTransactionAmount) và bất kỳ một trong các trường dữ liệu khác.
12. **(LO 4)** Giả sử bạn là một kế toán thuế đang đánh giá hồ sơ tài chính của một cá nhân về việc tuân thủ thuế liên bang của họ. Các rủi ro dữ liệu nào nên được xem xét?

---

**Bài tập Ngắn (Brief Exercises)**

**BE 4.1 (LO 1)** Đặt các thành phần của kế hoạch dự án phân tích dữ liệu theo đúng thứ tự tuần tự, bắt đầu với số 1 cho bước đầu tiên.
___ a. Tích hợp các kiểm soát (Embed controls).
___ b. Xác định mục tiêu dự án và các câu hỏi cụ thể.
___ c. Thiết kế chiến lược dữ liệu.
___ d. Xem xét rủi ro.
___ e. Thiết kế chiến lược phân tích.

**BE 4.2 (LO 1)** Đặt các bước tạo chiến lược dữ liệu theo đúng thứ tự, bắt đầu với số 1 cho bước đầu tiên.
___ a. Chọn và định giá trị (value) các yếu tố để xếp hạng các phương án thay thế dữ liệu.
___ b. Đánh giá xếp hạng phương án dữ liệu và chọn chiến lược dữ liệu tốt nhất.
___ c. Dựa trên mục tiêu, phát triển một vài phương án dữ liệu thay thế.
___ d. Trích xuất, làm sạch, và biến đổi các trường dữ liệu để chuẩn bị dữ liệu cho việc phân tích.

**BE 4.3 (LO 1)** **Kế toán Tài chính** Đối với mỗi điều sau đây, hãy liệt kê yếu tố tư duy phản biện nào liên quan rõ ràng nhất (S = Các bên liên quan (Stakeholders); P = Mục đích (Purpose); A = Các phương án thay thế (Alternatives); R = Rủi ro (Risks); K = Kiến thức (Knowledge)):
___ 1. Biết được quy trình định giá nào sẽ sử dụng cho U.S. GAAP.
___ 2. Xem xét tác động của các kết quả phân tích.
___ 3. Cơ sở cho sự phù hợp của các lựa chọn dữ liệu của bạn.
___ 4. Không chỉ đi theo ý tưởng đầu tiên mà bạn nghĩ đến cho dữ liệu và phân tích của mình.
___ 5. Thực hiện một phân tích không phù hợp với thang đo lường dữ liệu của bạn.

**BE 4.4 (LO 2)** Ghép thang đo lường dữ liệu có thể được sử dụng với từng ví dụ.
Các thang đo lường có thể được sử dụng một lần, nhiều lần hoặc không được sử dụng.
a. Định danh (Categorical)
b. Thứ bậc (Ordinal)
c. Khoảng (Interval)
d. Tỷ lệ (Ratio)

| Ví dụ (Example) | Thang đo lường (Measurement Scale) |
| --- | --- |
| 1. Xếp hạng khảo sát khách hàng. | |
| 2. Số hiệu tài khoản trong hệ thống tài khoản (chart of accounts). | |
| 3. Các bang hoặc khu vực của một quốc gia. | |
| 4. Giá trị sổ sách của tài sản có thể khấu hao. | |
| 5. Ngày giao dịch, chẳng hạn như ngày giao hàng. | |
| 6. Điểm tín dụng của những người nộp đơn xin vay vốn. | |
| 7. Trường VendorID. | |
| 8. Doanh thu bán hàng. | |
| 9. Trọng lượng cố định của các hộp sản phẩm được vận chuyển. | |
| 10. Loại sản phẩm trong kho siêu thị, chẳng hạn như nông sản, thức ăn cho thú cưng, thịt, và thực phẩm đông lạnh. | |

**BE 4.5 (LO 2)** **Kiểm toán** Giả sử bạn là một kiểm toán viên chính chịu trách nhiệm giám sát thực tập sinh năm nay về một dự án phân tích dữ liệu liên quan đến việc mua hàng của khách hàng. Bạn đã cung cấp cho thực tập sinh một tập dữ liệu và yêu cầu thực tập sinh xem xét tập dữ liệu đó và chuẩn bị thảo luận. Dưới đây là phần trích đoạn của dữ liệu.

| PONo | VendID | VendorName | Vendor Quality | Vendor Payterms | PODate | PO ItemNo | ItemCost | ItemQty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2001 | 783 | Pep N Supply | 3 | 1/10 net 30 | 12/1/2023 | 23568 | 41.99 | 12 |
| 2002 | 783 | Pep N Supply | 3 | 1/10 net 30 | 12/2/2023 | 23567 | 31.99 | 12 |
| 2003 | 784 | Playtime Toys | 4 | 1/15 net 30 | | 32425 | 15.99 | 11 |
| 2004 | 784 | Playtime Toys | 4 | 1/15 net 30 | 12/4/2023 | 32426 | 15.99 | 10 |
| 2005 | 784 | Playtime Toys | 4 | 1/15 net 30 | 12/5/2023 | 32427 | 15.99 | 25 |
| 2006 | 258 | Snappy Supplies | 5 | net 45 | 12/6/2023 | 11246 | 3.25 | 26 |
| 2007 | 153 | | 2 | 2/10 net 60 | 12/7/2023 | 11258 | 333.25 | 35 |
| 153 | Production | | 2 | 2/10 net 60 | 12/8/2023 | 11259 | 6.75 | 45 |
| 2009 | 783 | Pep N Supply | 3 | 1/10 net 30 | 12/9/2023 | 23566 | 22.99 | 100 |

1. Thực tập sinh phát biểu, "Khi xem xét tập dữ liệu, tôi phân loại VendorID là một nguồn dữ liệu thô đo lường (measured raw data)." Hãy giải thích tại sao VendorID nên được coi là dữ liệu thô chưa đo lường (non-measured raw data).
2. Thực tập sinh phát biểu, "Trường dữ liệu VendorQuality (chất lượng nhà cung cấp) phải được coi là dữ liệu tỷ lệ (ratio data) vì chúng ta có thể phân tích nó như một biến trong phân tích của mình." Hãy giải thích tại sao trường dữ liệu VendorQuality không nên được coi là dữ liệu tỷ lệ.
3. Thực tập sinh nói, "Các trường dữ liệu ItemCost (chi phí mặt hàng) và ItemQty (số lượng mặt hàng) có thể được kết hợp để tạo ra một trường dữ liệu được tính toán (calculated data field)." Hãy giải thích tại sao điều này là đúng.
4. Dựa trên việc bạn xem xét trích đoạn tập dữ liệu, bạn mong đợi thực tập sinh sẽ xác định được những rủi ro dữ liệu nào?
5. Giả sử bạn yêu cầu thực tập sinh xác minh tính chính xác của số Đơn đặt hàng (PO) 2006. Thực tập sinh sẽ xem xét những gì để xác định xem dữ liệu trong cơ sở dữ liệu có chính xác không?

**BE 4.6 (LO 2)** Đối với mỗi trường dữ liệu sau đây, hãy xác định xem trường dữ liệu đó là trường dữ liệu thô đo lường (measured raw data - MRD), trường dữ liệu thô chưa đo lường (non-measured raw data - NRD), hay là trường được tính toán (calculated field - CAL).
___ 1. ProductIdentificationCode (Mã nhận diện sản phẩm)
___ 2. UnitCost (Đơn giá) cho mỗi mặt hàng tồn kho
___ 3. TotalCost (Tổng chi phí)
___ 4. GrossProfit (Lợi nhuận gộp)
___ 5. ProductCategory (Danh mục sản phẩm)
___ 6. NumberOnHand (Số lượng tồn kho) trong kho của mỗi sản phẩm

**BE 4.7 (LO 3)** Xác định mục tiêu của từng chiến lược phân tích sau đây là mô tả (describe), chẩn đoán (diagnose), dự đoán (predict), hay đề xuất (prescribe).

| Chiến lược (Strategy) | Mục tiêu (Objective) |
| --- | --- |
| 1. Lập báo cáo tuổi nợ cho các hóa đơn chưa thanh toán cuối năm của khoản phải thu dựa trên số ngày quá hạn để hiểu được điều gì đang xảy ra với các khoản phải thu. | |
| 2. Ước tính số tiền tiết kiệm chi phí và tăng năng suất từ các khoản đầu tư AIS mới. | |
| 3. Tạo kế hoạch lấy mẫu phân tầng theo giá trị đô la (dollar value stratified sampling) cho các tài khoản tài sản đầu tư. | |
| 4. Đếm và xếp hạng các sự cố bảo mật máy chủ web theo tuần. | |
| 5. Ước tính mức tăng doanh thu sản phẩm theo từng sản phẩm từ các chiến dịch tiếp thị. | |
| 6. Ước tính dòng tiền trong tương lai từ chiến lược tiếp tục hoạt động kinh doanh hiện tại. | |
| 7. Tính toán việc giảm chi phí trước - sau từ các khoản đầu tư hệ thống. | |
| 8. Kiểm tra các chiến lược lập kế hoạch thuế khác nhau bằng cách đánh giá số tiền mặt tiết kiệm được trong tương lai. | |
| 9. Ước tính số lượng hàng tồn kho vào cuối năm bằng cách lấy mẫu một số ít cửa hàng và đưa ra các suy diễn (inferences) về tổng thể. | |
| 10. Đếm tần suất các đơn đặt hàng chưa được thực hiện hoặc mới được thực hiện một phần để có thể giải quyết chúng. | |

**BE 4.8 (LO 3)** Đối với mỗi cấu trúc dữ liệu và phân tích được liệt kê cho các mục tiêu mô tả và chẩn đoán, hãy cho biết liệu phân tích có thể được thực hiện hay không bằng cách chọn "Có" (Yes) hoặc "Không" (No).
___ 1. Việc tính toán mode trên dữ liệu định danh (categorical data).
___ 2. Độ phân tán phương sai của dữ liệu thứ bậc (ordinal data).
___ 3. Việc tính toán trung vị (median) trên dữ liệu khoảng (interval data).
___ 4. Các phân phối tần suất tích lũy (Cumulative frequency distributions) trên dữ liệu định danh.
___ 5. Một hình ảnh trực quan về các xu hướng của dữ liệu định danh.
___ 6. Các tương quan bảng chéo (Cross tabulation correlations) của dữ liệu tỷ lệ (ratio data).

**BE 4.9 (LO 3)** Đối với mỗi cấu trúc dữ liệu và phân tích được liệt kê cho các mục tiêu dự đoán và đề xuất, hãy cho biết liệu phân tích có thể được thực hiện hay không bằng cách chọn "Có" hoặc "Không".
___ 1. Đường xu hướng (Trendlines) trên dữ liệu định danh (categorical data).
___ 2. Phân tích hồi quy (Regression analysis) trên dữ liệu thứ bậc (ordinal data).
___ 3. Mô hình tối ưu hóa (Optimization modeling) trên dữ liệu khoảng (interval data).
___ 4. Phân tích hồi quy trên dữ liệu định danh.
___ 5. Phân tích độ nhạy giả định (What-if analysis) trên dữ liệu tỷ lệ (ratio data).
___ 6. Đường xu hướng trên dữ liệu tỷ lệ.

**BE 4.10 (LO 4)** **Kiểm toán** Đối với mỗi chiến lược dữ liệu sau đây được sử dụng bởi các kiểm toán viên, hãy cung cấp ít nhất một rủi ro nên được kiểm soát để có thể tin cậy vào kết quả phân tích.
1. Lấy mẫu các giao dịch của khách hàng theo quy mô của các giao dịch tác động đến một tài khoản.
2. So sánh các ước tính và giả định được sử dụng bởi ban quản lý năm nay so với năm ngoái.
3. Yêu cầu xác nhận cho tất cả số dư tài khoản ngân hàng, khoản phải thu, và khoản phải trả vào cuối năm.

**BE 4.11 (LO 4)** **Hệ thống Thông tin Kế toán** Đối với mỗi chiến lược phân tích sau đây dành cho các dự án AIS, hãy xác định xem mục tiêu của dự án là mô tả/chẩn đoán (D) hay dự đoán/đề xuất (P):

| Chiến lược (Strategy) | Mục tiêu (Objective) |
| --- | --- |
| 1. Tính toán lượng thời gian trung bình mà mỗi phòng ban trong chu trình doanh thu dành ra để thực hiện chức năng của mình trên mỗi đơn hàng. | |
| 2. Tính toán lượng chi phí tiết kiệm được dự kiến từ việc chuyển sang công nghệ RFID (nhận dạng qua tần số vô tuyến) để nhận diện, định giá và tính chi phí hàng tồn kho. | |
| 3. Ước tính hệ thống AIS sẽ cần bao nhiêu không gian máy chủ nếu doanh thu bán hàng tăng 10% mỗi năm trong năm năm tới. | |
| 4. Phát hiện những thời điểm nào trong ngày và thông qua kênh nào mà sự truy cập trái phép vào mô-đun quản lý quan hệ khách hàng đang xảy ra. | |

**BE 4.12 (LO 4)** **Kế toán Tài chính** Giả sử bạn là một kế toán tài chính được giao nhiệm vụ chọn ra phương án tài trợ thay thế tốt nhất cho tổ chức của bạn. Đề xuất một chiến lược dữ liệu và một chiến lược phân tích cho mục tiêu này.


**Bài tập (Exercises)**

**EX 4.1 (LO 1) Ghép nối Các Thành phần Kế hoạch Dự án (Match Project Plan Components)** Hãy ghép thành phần kế hoạch dự án phân tích dữ liệu với từng phát biểu sau:
a. Các mục tiêu và câu hỏi của dự án
b. Chiến lược dữ liệu
c. Chiến lược phân tích
d. Các rủi ro quan trọng
e. Các kiểm soát được tích hợp
___ 1. Xác minh các giá trị dữ liệu về tính hợp lý.
___ 2. Định dạng dữ liệu phải được biến đổi trước khi phân tích.
___ 3. Dự đoán khối lượng bán hàng của năm tới.
___ 4. Dữ liệu khối lượng bán hàng.
___ 5. Sử dụng phân tích hồi quy để dự đoán khối lượng bán hàng của năm tới.
___ 6. Chẩn đoán nguyên nhân gây ra sự vượt chi phí (cost overruns) trong quy trình sản xuất.
___ 7. Sử dụng các thang đo khác nhau trên trục y và trục x trên các hình ảnh trực quan.

**EX 4.2 (LO 1) Kế toán Quản trị | Kế toán Tài chính | Thiết kế Chiến lược Dữ liệu và Chiến lược Phân tích (Design a Data Strategy and an Analysis Strategy)** Giả sử động lực của bạn để thực hiện phân tích dữ liệu là nhằm tối đa hóa doanh thu bán hàng. Các câu hỏi mục tiêu cụ thể của bạn là để xác định xem khối lượng bán hàng đang tăng, ổn định, hay đang giảm đối với từng dòng sản phẩm của công ty bạn trong năm nay so với năm ngoái. Hãy mô tả một chiến lược dữ liệu và chiến lược phân tích khả thi cho mục tiêu này.

**EX 4.3 (LO 1) Kế toán Quản trị | Hệ thống Thông tin Kế toán | Ghép nối Lựa chọn Chiến lược Dữ liệu (Match Data Strategy Choices)** Ghép từng mục tiêu với các lựa chọn dữ liệu sau.
a. Dữ liệu chi phí nhân công
b. Dữ liệu đợt sản xuất (Production run)
c. Dữ liệu chiến lược tiếp thị trong quá khứ
d. Dữ liệu khảo sát sự hài lòng với dịch vụ CNTT
e. Dữ liệu bán hàng trực tuyến
f. Dữ liệu hợp đồng bán hàng
___ 1. Điều gì đang gây ra biến động lớn trong việc sử dụng nguyên vật liệu sản xuất của chúng ta?
___ 2. Chiến lược tiếp thị nào có khả năng nhất sẽ làm tăng thị phần của chúng ta?
___ 3. Chúng ta có đang tuân thủ các quy trình của U.S. GAAP đối với việc ghi nhận doanh thu hay không?
___ 4. Dòng sản phẩm nào của chúng ta có thể được bán trực tuyến cũng như bán tại cửa hàng?
___ 5. Sự thay đổi (turnover) nhân viên CNTT của chúng ta có ảnh hưởng đến dịch vụ của họ đối với các bộ phận chức năng khác hay không?
___ 6. Chi phí tiền lương của chúng ta có đang tăng lên không?

**EX 4.4 (LO 2) Kế toán Quản trị | Thiết kế Các Chiến lược Dữ liệu (Design Data Strategies)** 
> 📥 **Dữ liệu thực hành:** Tải file [Pet_Supply_Purchases.csv](../TaiLieu/Datasets/Pet_Supply_Purchases.csv) để xem mẫu dữ liệu.

Sau đây là danh sách các trường có sẵn trong một tập dữ liệu từ một cửa hàng đồ dùng cho thú cưng.

| Trường dữ liệu (Data Field) | Mô tả (Description) |
| --- | --- |
| 1. PONo | Số Đơn đặt hàng được gán duy nhất |
| 2. VendorID | Mã nhà cung cấp được gán duy nhất |
| 3. VendorName | Tên nhà cung cấp |
| 4. VendorQuality | Đánh giá chất lượng từ 1 - 6, trong đó 1 = kém và 6 = xuất sắc |
| 5. VendorAddress | Tên đường và địa chỉ gửi thư của bưu điện Hoa Kỳ |
| 6. VendorCity | Thành phố của địa chỉ gửi thư |
| 7. VendorState | Bang của địa chỉ gửi thư |
| 8. VendorZip | Mã zip của địa chỉ gửi thư |
| 9. VendorPayterms | Các điều khoản thanh toán được đàm phán với nhà cung cấp |
| 10. PODate | Ngày Đơn đặt hàng |
| 11. POItemID | Số mặt hàng có thể nhận dạng duy nhất |
| 12. POItemDescription | Mô tả về mặt hàng |
| 13. ItemCost | Chi phí của mặt hàng tồn kho theo các điều khoản được đàm phán với nhà cung cấp |
| 14. ItemQty | Tổng số lượng mặt hàng đã mua |

Đối với mỗi mục tiêu sau (a, b, c), hãy xác định các trường dữ liệu tối thiểu (1-14) bạn sẽ chọn cho chiến lược dữ liệu của mình:
a. Mục tiêu của bạn là giảm lượng khí thải carbon từ các giao dịch mua hàng của mình, vì vậy bạn muốn xác định nhà cung cấp nào đã vận chuyển các đơn hàng mua của bạn qua chặng đường dài nhất (most miles) trong năm ngoái.
b. Mục tiêu của bạn là xác định xem các mặt hàng tồn kho nào có mức tăng chi phí lớn nhất trong năm năm qua.
c. Mục tiêu của bạn là xác định năm nhà cung cấp mà bạn đã thực hiện việc mua hàng có giá trị cao nhất trong năm ngoái.

**EX 4.5 (LO 2) Chuẩn bị một Kế hoạch Dự án (Prepare a Project Plan)** Bạn sẽ tốt nghiệp chương trình đại học trong một tháng tới. Mục tiêu của bạn là ứng tuyển thành công vào cả các công việc chuyên môn và các trường sau đại học (graduate school). Trong hồ sơ ứng tuyển của mình, bạn muốn thể hiện điểm số của mình đã cải thiện như thế nào khi bạn chuyển từ các khóa học giáo dục đại cương (general education courses) sang các khóa học chuyên ngành. Mô tả chiến lược dữ liệu, chiến lược phân tích của bạn, và ba rủi ro có thể xảy ra mà bạn cần kiểm soát bằng cách cung cấp các gợi ý kiểm soát.

**EX 4.6 (LO 2) Kế toán Quản trị | Các Rủi ro và Kiểm soát Chiến lược Dữ liệu (Data Strategy Risks and Controls)** Giả sử mục tiêu phân tích dữ liệu của bạn là nhằm giảm thiểu lượng khí thải carbon từ các giao dịch mua hàng của bạn từ các nhà cung cấp. Chiến lược phân tích của bạn là xác định nhà cung cấp nào đã vận chuyển các đơn mua hàng của bạn với quãng đường dài nhất trong năm qua. Bạn đã chọn các trường dữ liệu sau cho chiến lược dữ liệu của mình.

| Trường dữ liệu (Data Field) | Mô tả (Description) |
| --- | --- |
| PONo | Số Đơn đặt hàng được gán duy nhất |
| VendorID | Mã nhà cung cấp được gán duy nhất |
| VendorName | Tên nhà cung cấp |
| VendorAddress | Tên đường và địa chỉ gửi thư của bưu điện Hoa Kỳ |
| VendorCity | Thành phố của địa chỉ gửi thư |
| VendorState | Bang của địa chỉ gửi thư |
| VendorZip | Mã zip của địa chỉ gửi thư |
| PODate | Ngày Đơn đặt hàng |

Xác định ba rủi ro dữ liệu và các kiểm soát dữ liệu mà bạn có thể sử dụng cho những rủi ro đó.

**EX 4.7 (LO 3) Kiểm toán | Kế toán Quản trị | Chuẩn bị một Kế hoạch Dự án (Prepare a Project Plan)** Bạn là một kiểm toán viên nội bộ đang làm việc với bộ phận bán hàng thiết bị hoạt động ngoài trời (outdoor gear sales department) của công ty bạn để nghĩ ra một chiến lược mới về hoa hồng bán hàng nhằm khuyến khích lợi nhuận cao hơn so với chiến lược hoa hồng cố định (flat commission) hiện tại của bạn. Mô tả một chiến lược dữ liệu, một chiến lược phân tích và ba rủi ro có thể xảy ra mà bạn cần kiểm soát bằng cách cung cấp các gợi ý kiểm soát.

**EX 4.8 (LO 3) Kế toán Quản trị | Chuẩn bị một Kế hoạch Dự án (Prepare a Project Plan)** 
> 📥 **Dữ liệu thực hành:** Tải file [Sihryas_Beauty_Sales.csv](../TaiLieu/Datasets/Sihryas_Beauty_Sales.csv) để thực hiện bài tập này.

Bạn là một kế toán quản trị cho Cửa hàng Đồ dùng Làm đẹp Sihrya's. Bạn đã được yêu cầu dự đoán tỷ suất lợi nhuận trên biến phí (contribution margin) của năm tới. Dưới đây là một mẫu dữ liệu có sẵn cho phân tích của bạn.

| Nhãn trường (Field Label) | Tên trường trong cơ sở dữ liệu (Field Name in Database) |
| --- | --- |
| Receipt Number (Số Biên lai) | SaleReceiptNo |
| Sales Date (Ngày Bán hàng) | Saledate |
| Inventory Code (Mã Hàng tồn kho) | InvCode |
| Number Sold (Số lượng Bán ra) | NoSold |
| Inventory Description (Mô tả Hàng tồn kho) | InvDesc |
| Inventory Price (Giá Hàng tồn kho) | InvPrice |
| Inventory Cost (Chi phí Hàng tồn kho) | InvCost |

Mô tả một chiến lược dữ liệu, một chiến lược phân tích, và ba rủi ro có thể xảy ra mà bạn cần kiểm soát bằng cách cung cấp các gợi ý kiểm soát.

**EX 4.9 (LO 3) Kế toán Tài chính | Kế toán Quản trị | Chuẩn bị một Kế hoạch Dự án (Prepare a Project Plan)** Bạn làm việc với tư cách là một nhà phân tích tài chính cho một chuỗi cửa hàng cà phê lớn, chẳng hạn như Starbucks. Mục tiêu của bạn là chẩn đoán xem những cửa hàng nào có doanh số đang tăng. Chiến lược dữ liệu của bạn là sử dụng dữ liệu hàng tháng về doanh thu cửa hàng từ hai năm qua. Hãy thiết kế một chiến lược phân tích, bao gồm những rủi ro bạn nên xem xét và các kiểm soát nào sẽ giúp giảm thiểu những rủi ro đó.

**EX 4.10 (LO 1-4) Kiểm toán | Hệ thống Thông tin Kế toán | Chuẩn bị một Kế hoạch Dự án (Prepare a Project Plan)** Bạn đang làm việc trong nhóm hệ thống thông tin kế toán tại công ty của bạn. Bạn đã được yêu cầu đánh giá các kiểm soát nội bộ liên quan đến việc xác thực (authentication) người dùng vào hệ thống thông tin. Người quản lý của bạn đã yêu cầu bạn thực hiện một phân tích mô tả về các nỗ lực đăng nhập thất bại. Người quản lý của bạn đã cung cấp cho bạn mục tiêu phân tích và câu hỏi. Sử dụng biểu đồ, hãy ghi lại tài liệu các lựa chọn dữ liệu và phân tích cũng như rủi ro và kiểm soát đối với từng lựa chọn.

| Mục tiêu và Các Câu hỏi (Objective and Questions) | Các Chiến lược Dữ liệu và Phân tích (Data and Analysis Strategies) | Các Rủi ro (Risks) | Các Kiểm soát (Controls) |
| --- | --- | --- | --- |
| **Mục tiêu:** Đánh giá các kiểm soát nội bộ liên quan đến xác thực người dùng<br>**Câu hỏi:** Trung bình, trung vị, độ lệch chuẩn, và phân phối của các nỗ lực đăng nhập thất bại trong năm hiện tại là bao nhiêu? | 1. Dữ liệu:<br>2. Phân tích: | 3. Dữ liệu:<br>4. Phân tích: | 5. Dữ liệu:<br>6. Phân tích: |


**EX 4.11 (LO 1-4) Kế toán Tài chính | Kế toán Quản trị | Chuẩn bị một Kế hoạch Dự án (Prepare a Project Plan)** 
> 📥 **Dữ liệu thực hành:** Tải file [Sihryas_Beauty_Sales.csv](../TaiLieu/Datasets/Sihryas_Beauty_Sales.csv) để thực hiện bài tập này.

Bạn là một nhà phân tích tài chính tại Tiệm làm đẹp Sihrya's. Chủ sở hữu công ty đã yêu cầu bạn thực hiện các phân tích dữ liệu để hiểu về các sản phẩm đóng góp vào khả năng sinh lời của cửa hàng bán lẻ của tiệm. Chủ sở hữu đã cung cấp cho bạn một từ điển dữ liệu (data dictionary), được trình bày ở đây, mô tả dữ liệu mà bạn có thể xem xét sử dụng trong phân tích của mình.

| Nhãn trường (Field Label) | Tên trường trong cơ sở dữ liệu (Field Name in Database) | Mô tả trường (Field Description) |
| --- | --- | --- |
| Số Biên lai (Receipt Number) | ReceiptNo | Số biên lai được gán bởi POS, nhận dạng duy nhất mỗi giao dịch bán hàng. |
| Ngày Bán hàng (Sales Date) | SaleDate | Ngày bán hàng theo POS. |
| Mã Hàng tồn kho (Inventory Code) | InvCode | Số nhận dạng hàng tồn kho duy nhất cho mỗi sản phẩm trong cửa hàng bán lẻ của tiệm. |
| Số lượng Bán ra (Number Sold) | NoSold | Số lượng mặt hàng đã bán. |
| Mô tả Hàng tồn kho (Inventory Description) | InvDesc | Mô tả về mặt hàng tồn kho. |
| Giá Hàng tồn kho (Inventory Price) | InvPrice | Giá bán gộp của mặt hàng tồn kho. |
| Chi phí Hàng tồn kho (Inventory Cost) | InvCost | Chi phí bình quân gia quyền của mặt hàng tồn kho. |

1. Nêu rõ mục tiêu của chủ sở hữu đối với dự án phân tích dữ liệu của bạn.
2. Giả sử câu hỏi phân tích của bạn là nhằm xác định các sản phẩm có lợi nhuận gộp (gross profit) cao nhất. Hãy xác định các trường dữ liệu mà bạn nên đưa vào phân tích của mình. Xác định các lựa chọn phân tích dữ liệu để trả lời câu hỏi phân tích này.
3. Xác định các rủi ro và các lựa chọn kiểm soát liên quan đến câu hỏi phân tích.

**EX 4.12 (LO 1-4) Dữ liệu | Kế toán Quản trị | Chọn một Chiến lược Dữ liệu và Thực hiện Phân tích (Select a Data Strategy and Perform an Analysis)** 
> 📥 **Dữ liệu thực hành:** Tải file [Pet_Supply_Purchases.csv](../TaiLieu/Datasets/Pet_Supply_Purchases.csv) để thực hiện bài tập này.

Bạn là một kế toán quản trị làm việc tại một công ty bán lẻ đồ chăm sóc thú cưng có nhiều địa điểm. Người giám sát của bạn đã yêu cầu bạn so sánh số tiền mua hàng từ mỗi nhà cung cấp trong tháng 12 năm 2024 so với tháng 12 năm 2025. Sau khi thảo luận với người giám sát, bạn đã xác định được những điều sau:
**Mục tiêu:** So sánh tổng mức mua hàng theo nhà cung cấp trong tháng 12 năm 2024 và tháng 12 năm 2025.
**Câu hỏi:** Trong năm 2024 và 2025, công ty đã mua hàng nhiều nhất (tính bằng đô la) từ những nhà cung cấp nào?
**Dữ liệu:** Bạn có quyền truy cập vào các dữ liệu sau.

| Trường dữ liệu (Data Field) | Mô tả (Description) |
| --- | --- |
| PONo | Số Đơn đặt hàng được gán duy nhất. |
| VendorID | Mã nhà cung cấp được gán duy nhất. |
| VendorName | Tên nhà cung cấp. |
| VendorQuality | Đánh giá chất lượng từ 1 - 6, trong đó 1 = kém và 6 = xuất sắc. |
| VendorAddress | Tên đường và địa chỉ gửi thư của bưu điện Hoa Kỳ. |
| VendorCity | Thành phố của địa chỉ gửi thư. |
| VendorState | Bang của địa chỉ gửi thư. |
| VendorZip | Mã zip của địa chỉ gửi thư. |
| VendorPayterms | Các điều khoản thanh toán được đàm phán với nhà cung cấp. |
| PODate | Ngày Đơn đặt hàng. |
| POItemID | Số mặt hàng có thể nhận dạng duy nhất. |
| POItemDescription | Mô tả về mặt hàng. |
| ItemCost | Chi phí của mặt hàng theo các điều khoản được đàm phán với nhà cung cấp. |
| ItemQty | Tổng số lượng mặt hàng đã mua. |

1. Những mục dữ liệu nào bạn sẽ sử dụng trong chiến lược dữ liệu của mình?
2. Thiết kế một chiến lược phân tích để xác định (các) nhà cung cấp mà công ty có số tiền mua hàng cao hơn vào năm 2025 so với năm 2024.
3. Thực hiện phân tích theo chiến lược phân tích của bạn. Xác định các nhà cung cấp mà công ty có số tiền mua hàng cao hơn vào năm 2025 so với năm 2024.

---

**Các Bài tập Tình huống (Problems)**

**PR 4.1 (LO 1- 4) Dữ liệu | Kiểm toán | Kế toán Quản trị | Hoàn thành Kế hoạch Dự án (Complete Project Plan)** 
> 📥 **Dữ liệu thực hành:** Tải file [PCard_Spending.csv](../TaiLieu/Datasets/PCard_Spending.csv) để thực hiện bài tập này.

Bạn làm việc trong nhóm kiểm toán nội bộ của tổ chức mình và người giám sát của bạn đã yêu cầu bạn phân tích dữ liệu về thẻ p-card. Mục tiêu của phân tích là để hiểu được việc chi tiêu qua thẻ p-card trong năm hiện tại. Các câu hỏi liên quan đến mục tiêu bao gồm:
- Ba nhà cung cấp nào mà công ty chi nhiều tiền nhất bằng thẻ p-card?
- Nhân viên nào chi số tiền cao nhất bằng thẻ p-card?
Xem xét dữ liệu và hoàn thành biểu đồ để lập hồ sơ các lựa chọn chiến lược dữ liệu và phân tích của bạn.

| Mục tiêu và Các Câu hỏi (Objective and Questions) | Các Chiến lược Dữ liệu và Phân tích (Data and Analysis Strategies) | Các Rủi ro (Risks) | Các Kiểm soát (Controls) |
| --- | --- | --- | --- |
| **Mục tiêu:** Hiểu việc chi tiêu thẻ p-card trong năm hiện tại.<br>**Các Câu hỏi:**<br>• Ba nhà cung cấp nào mà Công ty chi nhiều tiền nhất bằng thẻ p-card?<br>• Nhân viên nào chi số tiền cao nhất bằng thẻ p-card? | **Dữ liệu:** Sử dụng dữ liệu được cung cấp trong tệp Excel.<br>**Phân tích:** Sử dụng Excel để tạo PivotTable cho phép phân nhóm dữ liệu chi tiêu p-card theo nhà cung cấp và sắp xếp theo nhà cung cấp có mức chi tiêu cao nhất.<br>Sử dụng Excel để tạo PivotTable nhằm phân nhóm số tiền chi tiêu p-card theo nhân viên và sắp xếp theo số tiền cao nhất theo từng nhân viên. | 1. Dữ liệu:<br>2. Phân tích: | 3. Dữ liệu:<br>4. Phân tích: |

5. Thực hiện các phân tích được đề xuất trong biểu đồ. Tóm tắt kết quả của bạn.

**PR 4.2 (LO 1, 2, 3) Dữ liệu | Kế toán Tài chính | Kế toán Quản trị | Hoàn thành Bước 2 và 3 của Kế hoạch Dự án và Thực hiện Phân tích (Complete Steps 2 and 3 of a Project Plan and Perform Analysis).** 
> 📥 **Dữ liệu thực hành:** Tải file [Sihryas_Beauty_Sales.csv](../TaiLieu/Datasets/Sihryas_Beauty_Sales.csv) để thực hiện bài tập này.

Bạn là một nhà phân tích tài chính tại Tiệm làm đẹp Sihrya's. Chủ sở hữu đã yêu cầu bạn thực hiện các phân tích dữ liệu để hiểu về các sản phẩm đóng góp vào khả năng sinh lời của cửa hàng bán lẻ của tiệm. Chủ sở hữu đã đưa cho bạn một từ điển dữ liệu (data dictionary), được trình bày ở đây, mô tả dữ liệu mà bạn có thể xem xét sử dụng trong phân tích của mình.

| Nhãn trường (Field Label) | Tên trường trong cơ sở dữ liệu (Field Name in Database) | Mô tả trường (Field Description) |
| --- | --- | --- |
| Số Biên lai (Receipt Number) | ReceiptNo | Số biên lai được gán bởi POS, nhận dạng duy nhất mỗi giao dịch bán hàng. |
| Ngày Bán hàng (Sales Date) | SaleDate | Ngày bán hàng theo POS. |
| Mã Hàng tồn kho (Inventory Code) | InvCode | Số nhận dạng hàng tồn kho duy nhất cho mỗi sản phẩm trong cửa hàng bán lẻ của tiệm. |
| Số lượng Bán ra (Number Sold) | NoSold | Số lượng mặt hàng đã bán. |
| Mô tả Hàng tồn kho (Inventory Description) | InvDesc | Mô tả về mặt hàng tồn kho. |
| Giá Hàng tồn kho (Inventory Price) | InvPrice | Giá bán gộp của mặt hàng tồn kho. |
| Chi phí Hàng tồn kho (Inventory Cost) | InvCost | Chi phí bình quân gia quyền của mặt hàng tồn kho. |

Giả sử mục tiêu phân tích của bạn là xác định các sản phẩm đóng góp nhiều nhất vào khả năng sinh lời của cửa hàng bán lẻ của tiệm. Các câu hỏi cụ thể của bạn là: Những sản phẩm nào có số lượng bán ra cao nhất? Những sản phẩm nào có biên lợi nhuận gộp dương (positive gross profit margin)? Hãy sử dụng thông tin được cung cấp để trả lời các câu hỏi sau:
1. Xác định các trường dữ liệu cần đưa vào chiến lược dữ liệu của bạn.
2. Xác định một chiến lược dữ liệu có thể được sử dụng để trả lời các câu hỏi mục tiêu.
3. Xác định một chiến lược phân tích có thể được sử dụng để trả lời các câu hỏi mục tiêu.
4. Xem xét dữ liệu được cung cấp để thực hiện phân tích. Sau khi thực hiện phân tích, hãy xác định hai sản phẩm hàng đầu đóng góp vào khả năng sinh lời của tiệm.


**Bài tập Tình huống Ứng dụng Chuyên môn (Professional Application Case): Automated Transportation, Inc. (ATI)**

**PR 4.3 (LO 1-4) Dữ liệu | Kế toán Quản trị | Hoàn thành Kế hoạch Dự án và Thực hiện Phân tích (Complete the Project Plan and Perform the Analysis)** Là một nhà phân tích tài chính tại một công ty trong ngành nhà hàng khách sạn, bạn đã được yêu cầu thiết kế một chiến lược phân tích dữ liệu để hiểu các yếu tố ảnh hưởng đến đánh giá chất lượng (quality rating) của khách. Nhóm của bạn đã thực hiện một cuộc khảo sát những khách lưu trú tại các cơ sở của bạn trong tháng 6. Nhóm cơ sở dữ liệu đã liên kết các phản hồi khảo sát về đánh giá chất lượng của kỳ lưu trú với địa điểm của khách, ngày nhận phòng và trả phòng, và số tiền chi tiêu. Họ chỉ ra rằng họ chỉ bao gồm dữ liệu liên quan đến các cuộc khảo sát được hoàn thành từ ngày 1 tháng 9 đến ngày 10 tháng 9.
1. Các thang đo lường dữ liệu nào được bao gồm trong các trường dữ liệu có nhãn Location (Địa điểm), QualityRating (Đánh giá Chất lượng), và SpendingAmount (Số tiền Chi tiêu)?
2. Xem xét tập dữ liệu, xác định các rủi ro dữ liệu hiện có trong tập dữ liệu, và đề xuất các kiểm soát cho những rủi ro này.
3. Giả sử một thành viên trong nhóm của bạn đề xuất rằng bạn sử dụng dữ liệu để dự đoán đánh giá chất lượng cho các kỳ lưu trú trong tương lai. Để thực hiện phân tích dự đoán này, bạn sẽ phải sử dụng dữ liệu đánh giá chất lượng trong một chiến lược phân tích dự đoán. Bạn sẽ trả lời như thế nào với thành viên trong nhóm của mình về tính phù hợp của việc sử dụng loại phân tích này?
4. Sử dụng tập dữ liệu này để thiết kế và thực hiện một chiến lược dữ liệu và chiến lược phân tích ban đầu, khác biệt để thỏa mãn câu hỏi mục tiêu. Lập tài liệu về chiến lược dữ liệu, chiến lược phân tích, rủi ro, và các kiểm soát của bạn, sau đó trình bày kết quả phân tích của bạn.

**PR 4.4 (LO 1-4) Dữ liệu | Kế toán Thuế | Hoàn thành Kế hoạch Dự án và Thực hiện Phân tích (Complete the Project Plan and Perform the Analysis)**
Beautiful Bites là một chuỗi tiệm bánh tọa lạc tại Colorado. Các chủ sở hữu của chuỗi cam kết với các giá trị bền vững xã hội và muốn tập trung hoạt động từ thiện của họ vào các thành phố (municipalities) nơi họ đang thu được nhiều thuế bán hàng (sales tax) nhất. Mục tiêu của phân tích dữ liệu là xác định xem hầu hết khách hàng của họ sống ở đâu. Câu hỏi cụ thể là: Hầu hết khách hàng của chúng ta cư trú tại những cộng đồng nào?
1. Chuẩn bị kế hoạch dự án phân tích dữ liệu.
2. Thực hiện phân tích và tóm tắt kết quả.

---

**Bài tập Tình huống Ứng dụng Chuyên môn: Automated Transportation, Inc. (ATI)**
> 📥 **Dữ liệu thực hành:** Tải file [ATI_Purchases_Data.csv](../TaiLieu/Datasets/ATI_Purchases_Data.csv) để thực hiện bài tập này.
Automated Transportation, Inc. là một nhà sản xuất cỡ trung bình chuyên về xe ô tô, thuyền và máy bay không người lái điều khiển từ xa. Công ty được thành lập cách đây 5 năm khi hai anh em quyết định chế tạo và bán xe điều khiển từ xa cho những người đam mê. Khi công ty phát triển, họ đã mở rộng các sản phẩm cung cấp của mình để bao gồm xe ô tô, thuyền, và máy bay không người lái điều khiển từ xa. Hai anh em đóng vai trò là chủ tịch và CEO của công ty, và hiện họ có hơn 70 nhân viên.
Họ có hai nhóm khách hàng chính: những người có sở thích (hobbyists) và các doanh nghiệp quan tâm đến việc kết hợp máy bay không người lái vào quy trình kinh doanh và chuỗi cung ứng của họ. Hai cơ sở khách hàng này cung cấp nhiều cơ hội phát triển. Ban quản lý coi trọng kiểm soát nội bộ, nhưng vì họ bận rộn điều hành công ty nên họ đã tuyển dụng nhân sự kế toán để giúp thiết kế các quy trình, chính sách, và kiểm soát nội bộ của công ty:
- Công ty không bắt buộc phải có báo cáo về kiểm soát nội bộ và kiểm toán viên độc lập không bắt buộc phải chứng thực (attest) về các kiểm soát nội bộ của công ty.
- Tuy nhiên, chủ sở hữu muốn chắc chắn rằng nhân viên công ty đang thiết kế và tuân theo các chính sách sẽ giúp họ duy trì các hoạt động hiệu lực và hiệu quả.
- Các chủ sở hữu cũng rất dựa vào dữ liệu (data-driven) và đưa ra nhiều quyết định kinh doanh của họ chỉ sau khi xem xét dữ liệu được thu thập và phân tích.
Sau đây là phần trích đoạn từ từ điển dữ liệu do nhân viên hệ thống thông tin của công ty và các kế toán viên hệ thống thông tin kế toán thiết kế.

| Nhãn trường Dữ liệu (Data Field Label) | Tên trường trong cơ sở dữ liệu (Field Name in Database) | Mô tả trường (Field Description) |
| --- | --- | --- |
| Số hóa đơn (Invoice number) | InvoiceNO | Số hóa đơn, được nhân viên kế toán công nợ (AP clerk) gõ thủ công vào AIS từ hóa đơn giấy do nhà cung cấp gửi qua đường bưu điện cho công ty. |
| Số tiền hóa đơn (Invoice amount) | InvoiceAmt | Số tiền của hóa đơn, được nhân viên kế toán công nợ gõ thủ công vào AIS từ hóa đơn giấy do nhà cung cấp gửi cho công ty. |
| Ngày giao hàng (Shipment date) | ShipDate | Ngày sản phẩm được chuyển đi từ địa điểm giao hàng. |
| Ngày hóa đơn (Invoice date) | InvoiceDate | Ngày của hóa đơn, được nhân viên kế toán công nợ gõ thủ công vào AIS từ hóa đơn giấy do nhà cung cấp gửi cho công ty. |
| Số nhận dạng nhà cung cấp (Vendor identification number) | VendorID | Số nhận dạng nhà cung cấp duy nhất. |
| Tên nhà cung cấp (Vendor name) | VendorName | Tên của nhà cung cấp. |
| Sản phẩm đã mua (Product purchased) | ProductID | Mã sản phẩm cho sản phẩm đã mua từ nhà cung cấp. Mã sản phẩm này nhất quán với danh mục từ nhà cung cấp. |
| Chi phí đơn vị (Unit cost) | UnitCost | Chi phí cho mỗi đơn vị sản phẩm đã mua từ nhà cung cấp. |
| Chi phí vận chuyển (Shipping cost) | ShipCost | Tổng chi phí vận chuyển. |
| Thuế hải quan cố định (Flat duty) | FlatDuty | Mức thuế quan cố định áp dụng cho mặt hàng phải chịu thuế. |
| Thuế quan (Tariff) | TariffAmt | Tổng số tiền thuế quan áp dụng cho hàng hóa được vận chuyển. |
| Địa điểm giao hàng (Shipping location) | ShipLocation | Quốc gia mà hàng hóa được gửi từ đó. |
| Đánh giá Chất lượng Nhận hàng (Receiving Quality rating) | QualityRate | Đây là đánh giá chất lượng được nhóm nhận hàng nhập vào AIS khi họ nhận hàng. Thang điểm là 1 = kém đến 5 = chất lượng xuất sắc. Nhóm nhận hàng đánh giá lô hàng về bao bì, chất lượng vật liệu, và tổng thể việc giao hàng. |
| Điều khoản thanh toán (Payment terms) | PaymentTerms | Các điều khoản thanh toán đã thỏa thuận với nhà cung cấp. Các điều khoản này được quản lý mua hàng đàm phán và được người giám sát mua hàng nhập vào tệp thông tin gốc (master file) của nhà cung cấp. |
| Điều khoản vận chuyển (Shipping terms) | ShipTerms | Các điều khoản vận chuyển - thường là FOB điểm đến (FOB destination) hoặc FOB điểm đi (FOB shipping). |
| Địa chỉ thanh toán (Payment address) | PayAddress | Địa chỉ của nhà cung cấp nơi khoản thanh toán sẽ được gửi qua bưu điện. |
| Số Đơn đặt hàng (Purchase order number) | PONumber | Số nhận dạng duy nhất được gán cho mỗi Đơn đặt hàng do công ty phát hành. |
| Ngày Đơn đặt hàng (Purchase order date) | PODate | Ngày Đơn đặt hàng được phát hành bởi công ty. |
| Số báo cáo nhận hàng (Receiving report number) | ReceivingNumber | Số nhận dạng duy nhất được gán cho mỗi báo cáo nhận hàng do bộ phận nhận hàng của công ty tạo ra. |
| Ngày báo cáo nhận hàng (Receiving report date) | ReceivingDate | Ngày sản phẩm được bộ phận nhận hàng của công ty nhận được. |
| Số lượng đã nhận (Quantity received) | QtyReceived | Tổng số lượng các mặt hàng đã nhận được. |
| Số lượng đã mua (Quantity purchased) | QtyPurchased | Tổng số lượng các mặt hàng trên Đơn đặt hàng. |
| Số lượng trên hóa đơn (Invoiced quantity) | QtyInvoice | Tổng số lượng các mặt hàng trên hóa đơn, số lượng này được nhân viên kế toán công nợ (AP clerk) gõ thủ công vào AIS từ hóa đơn giấy do nhà cung cấp gửi qua bưu điện. |
| Phê duyệt của Thủ quỹ (Treasurer Approval) | Approved | Tên viết tắt của Thủ quỹ cho biết sự chấp thuận của họ nếu hóa đơn lớn hơn $10,000. |

**PAC 4.1 Hệ thống Thông tin Kế toán: Đánh giá Kiểm soát Nội bộ của AIS (Evaluate AIS Internal Controls)**
**Hệ thống Thông tin Kế toán** Là một kế toán viên hệ thống thông tin, chủ sở hữu đã yêu cầu bạn thiết kế các kiểm soát nội bộ liên quan đến hệ thống thanh toán cho nhà cung cấp của công ty. Hãy nhớ lại từ khóa học hệ thống thông tin kế toán của bạn rằng có một số kiểm soát quan trọng trong chu trình từ đặt hàng đến thanh toán (order-to-pay cycle), bao gồm việc phê duyệt các giao dịch mua, và phê duyệt hóa đơn của nhà cung cấp. Bạn đã triển khai các kiểm soát sau:
- Nhân viên kế toán chuẩn bị một gói chứng từ thanh toán (voucher package) bao gồm phiếu chi (disbursement voucher), hóa đơn của nhà cung cấp, Đơn đặt hàng, và chứng từ nhận hàng cho mỗi khoản thanh toán được thực hiện.
- Các hóa đơn có khoản thanh toán vượt quá $10,000 có cấp phê duyệt thứ hai, được ghi chú trong hệ thống thông tin bằng chữ cái viết tắt tên của thủ quỹ.
Bạn muốn kiểm tra tính hữu hiệu của hoạt động (operational effectiveness) của kiểm soát này bằng cách phân tích dữ liệu được hệ thống thông tin kế toán thu thập trong quá trình này. Giả sử mục tiêu phân tích của bạn là để hiểu xem liệu kiểm soát nội bộ có đang hoạt động theo đúng thiết kế hay không. Hãy thiết kế chiến lược phân tích dữ liệu của bạn để giải quyết mục tiêu này. Đảm bảo cung cấp tài liệu cho các thành phần sau:
1. Câu hỏi mà phân tích dữ liệu của bạn nên giải quyết là gì?
2. Sử dụng từ điển dữ liệu, bạn nên yêu cầu các trường dữ liệu thô đo lường và dữ liệu thô chưa đo lường nào?
3. Bạn sẽ đưa ra những lựa chọn phân tích nào để phân tích dữ liệu? Cụ thể, bạn sẽ tạo những trường dữ liệu được tính toán nào trong phân tích của mình?
4. Các rủi ro dữ liệu đối với chiến lược phân tích dữ liệu của bạn là gì?
5. Các rủi ro phân tích trong chiến lược của bạn là gì?
6. Bạn nên đưa vào các kiểm soát nào trong các chiến lược dữ liệu và phân tích của mình để giảm thiểu những rủi ro mà bạn đã vạch ra?

**PAC 4.2 Kiểm toán: Chọn lọc Các Giao dịch Mua hàng Lớn và Bất thường (Select Large and Unusual Purchases)**
**Dữ liệu | Kiểm toán** Bạn là một nhân viên năm thứ hai làm việc tại một công ty kế toán công được phân công thực hiện hợp đồng dịch vụ ATI, đây là một hợp đồng dịch vụ mới của công ty. Trưởng nhóm kiểm toán (audit senior) của bạn đã cung cấp cho bạn một tệp giao dịch chứa tất cả các khoản thanh toán của công ty cho các nhà cung cấp trong tháng Một. Bạn được yêu cầu xác định xem công ty có ghi nhận chính xác thông tin hóa đơn hay không bằng cách thiết kế một chiến lược phân tích dữ liệu để chọn ra các giao dịch mua hàng để kiểm tra thêm. Trưởng nhóm của bạn yêu cầu bạn xác định các giao dịch có thể nằm ngoài hành vi mua hàng thông thường. Do đó, bạn phải thực hiện các phân tích mô tả. Trưởng nhóm của bạn đã cung cấp cho bạn kế hoạch phân tích dữ liệu một phần (partial) này.
Hãy hoàn thành biểu đồ bằng cách xác định rủi ro và các kiểm soát liên quan đối với các lựa chọn dữ liệu và phân tích được xác định trong kế hoạch phân tích dữ liệu.

| Mục tiêu và Các Câu hỏi (Objective and Questions) | Các Chiến lược Dữ liệu và Phân tích (Data and Analysis Strategies) | Các Rủi ro (Risks) | Các Kiểm soát (Controls) |
| --- | --- | --- | --- |
| **Mục tiêu:** Xác định các giao dịch mua hàng để kiểm tra thêm.<br>**Các Câu hỏi:** Có các giao dịch mua hàng nào có thể được coi là bất thường (anomalies) không? | **Chiến lược dữ liệu:** InvoiceNo, InvoiceDate, QtyInvoice, InvoiceAmt, VendorID, VendorDescription<br>**Chiến lược phân tích:** Thực hiện các số liệu thống kê mô tả để hiểu tổng số tiền và số lượng các giao dịch mua hàng được thực hiện với từng nhà cung cấp.<br>Thực hiện các số liệu thống kê chẩn đoán và tạo một biểu đồ phân tán (scatterplot) trong đó InvoiceDate nằm trên trục X và InvoiceAmount nằm trên trục Y để xác định bất kỳ khoản mua hàng ngoại lai (outlier) nào. | 1. Dữ liệu:<br>2. Phân tích: | 3. Dữ liệu:<br>4. Phân tích: |

5. Thực hiện phân tích thống kê mô tả để xác định tổng số tiền bằng đô la và số lượng các giao dịch mua hàng đã thực hiện đối với mỗi nhà cung cấp.
6. Sử dụng tập dữ liệu được cung cấp để thực hiện phân tích thống kê chẩn đoán nhằm tạo một biểu đồ phân tán (scatterplot) trong đó InvoiceDate nằm trên trục X và InvoiceAmt nằm trên trục Y để xác định các giao dịch mua ngoại lai (outlier purchases).

**PAC 4.3 Kế toán Tài chính: Lên kế hoạch Xác định Các Nhà cung cấp Có Mức Hoạt động Cao (Plan to Identify High Activity Vendors)**
**Kế toán Tài chính** Chủ sở hữu công ty muốn biết nhóm mua hàng đang sử dụng những nhà cung cấp nào và họ đang trả bao nhiêu cho mỗi nhà cung cấp để đàm phán các điều khoản hợp đồng tốt hơn với các nhà cung cấp thường xuyên. Bạn đang thực hiện phân tích dữ liệu để xác định các nhà cung cấp được sử dụng nhiều nhất. Trả lời từng câu hỏi liên quan đến phân tích dữ liệu của bạn.
1. Câu hỏi mà phân tích dữ liệu của bạn nên giải quyết là gì?
2. Sử dụng từ điển dữ liệu, bạn nên yêu cầu những trường dữ liệu thô đo lường và dữ liệu thô chưa đo lường nào?
3. Bạn sẽ đưa ra những lựa chọn phân tích nào để phân tích dữ liệu? Hãy cụ thể, bạn sẽ tạo những trường dữ liệu được tính toán nào trong phân tích của mình?
4. Các rủi ro dữ liệu đối với chiến lược phân tích dữ liệu của bạn là gì?
5. Các rủi ro phân tích trong chiến lược của bạn là gì?
6. Bạn nên bao gồm những kiểm soát nào trong phân tích của mình để giảm thiểu những rủi ro mà bạn đã vạch ra?

**PAC 4.4 Kế toán Quản trị: Xếp hạng Chất lượng Nhà cung cấp (Rank Vendor Quality)**
**Dữ liệu | Kế toán Quản trị** Vì công ty đang phát triển rất nhanh, các chủ sở hữu muốn chắc chắn rằng họ đang hợp tác với đúng nhà cung cấp về nguyên vật liệu thô. Họ đã yêu cầu nhóm nhận hàng đưa ra đánh giá cho mỗi lần nhận hàng để lập tài liệu về chất lượng bao bì, vật liệu về mặt ngoại quan, và tổng thể việc giao hàng. Đối với mỗi lần nhận hàng, nhóm nhận hàng ghi chép lại một mức đánh giá chất lượng trong hệ thống thông tin kế toán. Chủ sở hữu đã yêu cầu bạn xác định xem mức đánh giá chất lượng của nhà cung cấp đã thay đổi như thế nào kể từ đầu năm. Người quản lý của bạn đã thiết kế một phần chiến lược phân tích dữ liệu sau đây. Hoàn thành biểu đồ và ghi lại các rủi ro và các kiểm soát liên quan đối với các phân tích của bạn.

| Mục tiêu và Các Câu hỏi (Objective and Questions) | Các Chiến lược Dữ liệu và Phân tích (Data and Analysis Strategies) | Các Rủi ro (Risks) | Các Kiểm soát (Controls) |
| --- | --- | --- | --- |
| **Mục tiêu:** Hiểu đánh giá chất lượng của các khoản mua hàng.<br>**Các Câu hỏi:**<br>Đánh giá chất lượng trung bình của từng nhà cung cấp là bao nhiêu?<br>Đánh giá chất lượng cao nhất và thấp nhất theo nhà cung cấp là gì?<br>Đánh giá chất lượng theo nhà cung cấp đã thay đổi như thế nào qua thời gian? | **Chiến lược dữ liệu:** VendorID, VendorName, ReceivingNo, ReceivingDate, QualityRate<br>**Chiến lược phân tích:**<br>Tính `QualityRating` trung bình theo `VendorName`.<br>Tính `QualityRating` tối thiểu và tối đa theo `VendorName`.<br>Trực quan hóa xem `QualityRating` theo `VendorName` đã thay đổi như thế nào qua thời gian. | 1. Dữ liệu:<br>2. Phân tích: | 3. Dữ liệu:<br>4. Phân tích: |

5. Thực hiện các phân tích được đề xuất trong kế hoạch dự án phân tích dữ liệu.

**PAC 4.5 Kế toán Thuế: Lên kế hoạch Phân tích Chi phí Thuế quan Quốc tế (Plan International Duty Cost Analysis)**
**Kế toán Thuế** Các chủ sở hữu muốn hiểu tổng số tiền thuế hải quan (customs duty) bằng đô la mà họ sẽ nợ chính phủ Hoa Kỳ trong năm. Họ đã yêu cầu bạn thực hiện phân tích mô tả để hiểu các giao dịch mua hàng từ các nhà cung cấp tại mỗi quốc gia. Công ty của bạn thực hiện mua hàng từ các nhà cung cấp tại một số quốc gia, chẳng hạn như Trung Quốc, Mexico, Hoa Kỳ, Nhật Bản, Nam Phi, Israel, Hy Lạp, và Ai Cập. Bạn và nhóm của bạn đã thiết kế một chiến lược phân tích dữ liệu. Bạn đã được yêu cầu xem xét các rủi ro và các kiểm soát liên quan trong quá trình phát triển chiến lược đó. Hãy hoàn thành biểu đồ sau.

| Mục tiêu và Các Câu hỏi (Objective and Questions) | Các Chiến lược Dữ liệu và Phân tích (Data and Analysis Strategies) | Các Rủi ro (Risks) | Các Kiểm soát (Controls) |
| --- | --- | --- | --- |
| **Mục tiêu:** Hiểu các giao dịch mua hàng được thực hiện từ mỗi quốc gia.<br>**Các Câu hỏi:** Số tiền mua hàng từ mỗi quốc gia là bao nhiêu?<br>Có bao nhiêu giao dịch mua hàng đã được thực hiện từ các nhà cung cấp ở mỗi quốc gia? | **Chiến lược dữ liệu:** ShipLocation, InvoiceAmt, FlatDuty, TariffAmt, PONumber<br>**Chiến lược phân tích:**<br>Sử dụng một bảng pivot để đặt `ShipLocation` vào các hàng (rows) và tổng (sum) của `InvoiceAmt` vào các giá trị (values).<br>Sử dụng một bảng pivot để đặt `ShipLocation` vào các hàng và đếm (count) `PONumber` vào các giá trị. | 1. Dữ liệu:<br>2. Phân tích: | 3. Dữ liệu:<br>4. Phân tích: |

---

**Trường hợp Xuyên suốt Le Grind (Le Grind Continuing Case): Thiết kế Kế hoạch Phân tích Dữ liệu để Mô tả và Chẩn đoán Thay đổi về Biên Lợi nhuận Gộp (Design a Data Analysis Plan for Describing and Diagnosing Gross Margin Changes)**
**Dữ liệu (Data)**
Hãy truy cập nền tảng học tập trực tuyến của Wiley để xem bối cảnh tình huống, các câu hỏi bổ sung, dữ liệu, và thông tin chi tiết hơn về tình huống xuyên suốt này.



#### **English**

<embed src="../TaiLieu/textbookForPractice/Ch_04_Planning Data and.pdf" type="application/pdf" width="100%" height="800px" />

<!-- tabs:end -->
