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
