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
