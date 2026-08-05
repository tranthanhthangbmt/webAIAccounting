<!-- tabs:start -->
#### **Tiếng Việt**

# Chương 8: Diễn giải Kết quả Phân tích Dữ liệu (Interpreting Data Analysis Results)

> [!NOTE]
> **Dữ liệu thực hành Chương 8:**
> Để thực hành các bài tập trong chương này, bạn có thể tải về các bộ dữ liệu mô phỏng dưới đây. Bạn có thể tải về để mở ra xem trước dữ liệu:
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/OneStopShop_Sales.csv" download target="_blank"><strong>OneStopShop_Sales.csv</strong></a>** (EX 8.14)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/OutdoorAdventures_Shipping.csv" download target="_blank"><strong>OutdoorAdventures_Shipping.csv</strong></a>** (EX 8.15, PR 8.1)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/AllCareHospital_Costs.csv" download target="_blank"><strong>AllCareHospital_Costs.csv</strong></a>** (PR 8.2)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/Ortho_Purchasing_Sales.csv" download target="_blank"><strong>Ortho_Purchasing_Sales.csv</strong></a>** (PAC 8.2)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/Ortho_Sales_By_State.csv" download target="_blank"><strong>Ortho_Sales_By_State.csv</strong></a>** (PAC 8.3)

C h A P T ER 8 Phiên dịch dữ liệu Kết quả phân tích Xem trước chương Hành trình xây dựng kỹ năng phân tích dữ liệu của bạn tiếp tục trong chương này với trọng tâm là diễn giải kết quả phân tích dữ liệu. Bạn đã và đang phát triển tư duy phân tích dữ liệu của mình, xác định và phân tích động lực cho các dự án phân tích dữ liệu, học cách xác định các câu hỏi liên quan- dữ liệu, khái niệm và thiết kế các chiến lược phân tích dữ liệu. Bạn cũng đã học được những kỹ năng cần thiết để chuẩn bị dữ liệu để phân tích, xây dựng mô hình thông tin và khám phá dữ liệu. Bây giờ, nó là thời gian để diễn giải các kết quả phân tích để có thể truyền đạt cho các bên liên quan.

Ban đầu có vẻ như việc khám phá dữ liệu và giải thích dữ liệu là như nhau. Mặc dù một số khía cạnh tương tự nhau nhưng cũng có những khác biệt chính. Bước khám phá dữ liệu tập trung vào việc phân tích hơn là diễn giải. Giải thích kết quả phân tích dữ liệu là một bước quan trọng trong quá trình phân tích dữ liệu.

Sẽ có những lúc trong sự nghiệp của bạn, bạn phải diễn giải một bản phân tích dữ liệu đã được được chuẩn bị bởi người khác trong tổ chức, khách hàng, chủ nợ hoặc đối tác trong chuỗi cung ứng của bạn. Cái này chương tập trung vào việc diễn giải ý nghĩa của cả những phân tích cuối cùng và kết quả của bạn trước khi được so sánh bởi những người khác. Phân tích Kế hoạch Báo cáo M ồ S A tôi C Mục tiêu Chiến lược Phân tích Phiên dịch giao tiếp Động lực Hiểu lý do cho phân tích dữ liệu Xác minh quá trình và kết quả Giải thích kết quả và của họ ý nghĩa

1. Chuẩn bị dữ liệu

2. Xây dựng thông tin mô hình

3. Khám phá dữ liệu Xác định mục tiêu và cụ thể đặt câu hỏi phân tích sẽ câu trả lời Thiết kế dữ liệu và phân tích chiến lược Giai đoạn 2 Giai đoạn 3 Giai đoạn 1

**Lộ trình chương**

**Lộ trình chương**

**MỤC TIÊU HỌC TẬP**

CHỦ ĐỀ ÁP DỤNG NÓ

**LO 8.1   So sánh phân tích dữ liệu**

diễn giải và dữ liệu thăm dò.

- Giải thích phân tích dữ liệu so với dữ liệu Thăm dò

- Giải thích phân tích dữ liệu Giải thích doanh thu Trực quan hóa (Ví dụ: Tài chính Kế toán) LO 8.2 Áp dụng tư duy phản biện để giải thích phân tích dữ liệu.

- Các bên liên quan: Hiểu bối cảnh

- Mục đích: Xác định “Tại sao” của Phân tích

- Các giải pháp thay thế: Điều tra các cách giải thích khác

- Rủi ro: Xem xét dữ liệu, phân tích và thành kiến

- Kiến thức: Những điều chúng ta cần biết

- Tự suy ngẫm: Nghĩ về những bài học kinh nghiệm Đánh giá một phân tích chi phí (Ví dụ: Kiểm toán) LO 8.3 Xác định xem dữ liệu có kết quả phân tích trả lời đặt câu hỏi và phù hợp với mục tiêu của việc phân tích.

- Đánh giá dữ liệu và phương pháp

- Kiểm tra kết quả

- Xác định xem có thêm thông tin hoặc phân tích là cần thiết Giải thích Phân tích Hoàn tiền (Ví dụ: Quản lý Kế toán) LO 8.4 Đánh giá tính hợp lệ và độ tin cậy của việc mô tả và kết quả phân tích dữ liệu chẩn đoán.

- Phân tích mô tả

- Phân tích chẩn đoán Giải thích biểu đồ phân tán cho Ngoại lệ (Ví dụ: Kiểm toán) LO 8.5 Đánh giá tính hợp lệ và độ tin cậy của dự đoán và kết quả phân tích dữ liệu theo quy định.

- Phân tích dự đoán

- Phân tích theo quy định Giải thích kết quả hồi quy (Ví dụ: Quản lý Kế toán) Dữ liệu Thẻ Dữ liệu xuất hiện trong chương khi dữ liệu cho một ví dụ, hình minh họa hoặc ứng dụng được có sẵn trên nền tảng học tập trực tuyến của Wiley. Phần mềm phân tích dữ liệu liên tục thay đổi và có thể có nhiều phiên bản phần mềm mới hơn. được đưa ra trong chương này. Để biết thêm thông tin, hãy truy cập video đi kèm trên nền tảng học tập trực tuyến của Wiley. Cái nhìn sâu sắc chuyên nghiệp: Kết quả phân tích có hợp lý không? Megan, một kế toán thuế cấp cao, làm việc tại một trong mười công ty kế toán lớn nhất Hoa Kỳ. Khi tôi mới tốt nghiệp, công ty tôi làm việc đã thuê ngoài tất cả các báo cáo và phân tích thuế. sự chuẩn bị. Ngay lập tức tôi được yêu cầu phải xem xét các phân tích do người khác chuẩn bị. ple và giải thích những kết quả đó cho đối tác. Thật sự rất khó khăn khi đột nhiên ở trong một vai trò xem xét hơn là vai trò người chuẩn bị. Tôi biết cách kiểm tra các con số để xem chúng có đều đúng, nhưng việc diễn giải ý nghĩa của kết quả còn khó khăn hơn nhiều. Khi tôi chuyển sang vai trò cấp cao, tôi đã thấy tầm quan trọng của tư duy phản biện- thậm chí còn hơn thế nữa. Những nhân viên tôi yêu thích nhất khi làm việc cùng là những người xem xét kết quả của họ và hỏi câu hỏi. Họ không chỉ cho rằng vì các con số được nhập chính xác nên kết quả là đúng Bạn có thể kiểm tra tất cả các con số để xem chúng có đúng không, nhưng khi bạn thực hiện phân tích, bạn cần có khả năng xác định xem kết quả có hợp lý hay không. Nhân viên sau khi nhập chính xác tất cả dữ liệu vào phần mềm thuế và đã cân nhắc một bản phân tích nghĩa vụ thuế cho thấy nghĩa vụ thuế của khách hàng đã tăng lên. Làm thế nào- chưa bao giờ, điều này không có ý nghĩa gì vì khách hàng đó đã lỗ 100 nghìn đô la từ một lần hoạt động kinh doanh của họ. Vì vậy, nghĩa vụ thuế đáng lẽ phải giảm xuống. Khi tôi chỉ này, nhân viên trả lời: “Tôi quá chú ý đến chi tiết nên tôi hợp lý hóa kết quả thay vì đặt thêm câu hỏi.” Quay lại để đánh giá- ăn nếu điều gì đó có ý nghĩa là khó khăn. Khi còn là sinh viên, tôi đã không tập làm điều đó. tôi đã chỉ tập trung vào việc có được câu trả lời đúng và đạt điểm cao.

Chương 8 Diễn giải kết quả phân tích dữ liệu

## 8.1  Chúng ta rút ra kết luận như thế nào từ

Phân tích dữ liệu?

**MỤC TIÊU HỌC TẬP ➊**

So sánh việc giải thích phân tích dữ liệu và khám phá dữ liệu. Giải thích phân tích dữ liệu là quá trình đánh giá một phân tích để hiểu và giải thích ý nghĩa của nó. Tương tự như việc diễn giải dự báo thời tiết khi lập kế hoạch ngoài trời bên, những hiểu biết sâu sắc thu được từ việc giải thích phân tích dữ liệu giúp chúng tôi kinh doanh hiệu quả các quyết định. Giải thích phân tích dữ liệu và khám phá dữ liệu có vẻ rất giống nhau. Trên thực tế, bạn đang diễn giải ngay cả khi bạn đang khám phá dữ liệu. Giải thích phân tích dữ liệu so với dữ liệu Thăm dò Mục tiêu của việc khám phá dữ liệu là hiểu dữ liệu, trong khi việc diễn giải dữ liệu liên quan đến việc hiểu rõ đứng phân tích. Tuy nhiên, trọng tâm là điều tạo nên sự khác biệt giữa việc khám phá và diễn giải. Một ví dụ có thể minh họa sự khác biệt. Hãy tưởng tượng tiến hành kiểm toán các tài khoản nhận được. có thể. Khách hàng đã cấp cho nhóm kiểm toán quyền truy cập vào dữ liệu các khoản phải thu có sẵn. Một đoạn trích từ dữ liệu được thể hiện trong Hình minh họa 8.1. Bước đầu tiên là khám phá dữ liệu để hiểu rõ chịu đựng được. Hãy nhớ lại rằng khám phá dữ liệu là một quá trình gồm bốn bước:

1. Xác định các câu hỏi về dữ liệu.

2. Xác định các mối quan hệ dữ liệu.

3. Khám phá các mối quan hệ dữ liệu.

4. Tạo ra những hiểu biết sâu sắc. Dữ liệu có thể được khám phá để tính toán tổng số khoản phải thu theo danh mục lão hóa và dữ liệu và thông tin thanh toán có thể được sử dụng để xác định các mối quan hệ trong dữ liệu:

- Cột G thể hiện các tài khoản mà khách hàng không đồng ý với số tiền trên hóa đơn.

- Thăm dò: Liệu có mối liên hệ giữa các khoản phải thu đang bị tranh chấp và cách giải quyết quá hạn thanh toán là gì? ngoại hối B A C D E F G Trang 1 3 4 5 6 7 8 2466 2467 Tự động Lưu Oﬀ 1 2 2468 ID khách hàng không cần giấy tờNgày Số hóa đơn Ngày hóa đơn Trích đoạn cơ sở dữ liệu các khoản phải thu của khách hàng Ngày đến hạn Hóa đơnSố tiền Đang tranh chấp 611365 7900770 9231909 0379-NEVHP 8976-AMJEO 2820-XGXSB 9322-YCTQO 6627-ELFBK 5148-SYKLB 7050-KQLDO 9758-AIEIK 5/4/2025 2/3/2024 24/1/2024 5/4/2024 25/11/2024 27/8/2025 28/9/2024 22/4/2024 9888306 15752855 18104516 9989225541 9990243864 H Ngày giải quyết tôi Hóa đơn không cần giấy tờ Giấy điện tử điện tử điện tử Giấy Giấy Giấy điện tử 1/1/2025 25/1/2025 2/7/2025 9/2/2025 24/10/2024 25/1/2024 26/4/2024 3/7/2025 31/1/2025 24/02/2025 1/8/2025 11/3/2025 23/11/2024 24/2/2024 26/5/2024 2/8/2025 $55,94 $61,74 $65,88 $105,92 $72,27 $94,00 $53,16 $68,66 Không Có Không Không Có Có Không Không 14/1/2025 2/3/2025 7/7/2025 16/3/2025 27/11/2024 20/2/2024 17/5/2024 17/7/2025 MINH HỌA 8.1 Cơ sở dữ liệu các khoản phải thu

![ILLUSTRATION 8.1](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.1.png)

## 8.1  Chúng tôi rút ra kết luận từ phân tích dữ liệu bằng cách nào?

Một mối quan hệ thay thế cũng có thể được khám phá:

- Dữ liệu cột I cho biết khách hàng nhận hóa đơn điện tử hay hóa đơn giấy.

- Thăm dò: Hóa đơn giấy hay hóa đơn điện tử có mối quan hệ với thời gian thực hiện khách hàng phải trả? Những hiểu biết sâu sắc thu được từ việc phân tích các mối quan hệ có thể được sử dụng để ước tính những khoản không thể thu hồi được. tài khoản. Thực hiện nhiều phân tích thăm dò cuối cùng sẽ dẫn đến phân tích chính xác. giải thích rõ ràng các khoản phải thu và các khoản phải thu khó đòi. Bây giờ là lúc chuyển sang chế độ phiên dịch. Tại thời điểm này, chúng tôi hiểu dữ liệu, nhưng chúng ta phải hiểu ý nghĩa của các phân tích trong việc hỗ trợ các thử nghiệm kiểm toán của công ty tính đầy đủ và hợp lý của khoản dự phòng phải thu khó đòi. Giải thích phân tích dữ liệu xảy ra ở cuối quá trình khám phá dữ liệu. Chúng tôi chuyển từ khám phá để hiểu rõ hơn phiên dịch để chúng ta có thể đưa ra những quyết định sáng suốt. Giải thích phân tích dữ liệu Giải thích phân tích dữ liệu là quá trình xem xét một phân tích. Có hai bước, mỗi bước với những câu hỏi cụ thể cần được trả lời. Bước 1: Xác định xem phân tích có ý nghĩa hay không.

- Câu hỏi 1: Bản phân tích có trả lời được câu hỏi dự định và có phù hợp với bản gốc không? khách quan?

- Câu hỏi 2: Dữ liệu và phương pháp được sử dụng để thực hiện phân tích có chính xác không?

- Câu hỏi 3: Kết quả có hợp lý không, hay cần phân tích thêm? Bước 2: Xác minh rằng kết quả là hợp lệ và đáng tin cậy.

- Câu hỏi 4: Phân tích có đo lường được những gì nó dự định đo lường không?

- Câu hỏi 5: Kết quả có chính xác không? Các bước này có vẻ quen thuộc vì chúng phản ánh quá trình phân tích dữ liệu trước đó. chương. Khi diễn giải phân tích của chúng tôi, hai câu hỏi đầu tiên ở Bước 1 sẽ được trả lời trong các giai đoạn lập kế hoạch và phân tích của quy trình MOSAIC:

- Phân tích có trả lời được câu hỏi hoặc mục tiêu ban đầu của phân tích không? (Động lực và Mục tiêu)

- Dữ liệu có chính xác và phương pháp thích hợp được sử dụng để thực hiện phân tích không? (Chiến lược và Phân tích) Các câu hỏi còn lại từ cả hai bước sẽ được trả lời trong quá trình báo cáo. giai đoạn của quá trình phân tích dữ liệu (Giải thích). Tuy nhiên, nếu người khác chuẩn bị phân tích thì cần phải giải quyết từng câu hỏi cho cả hai bước. Chương này hoạt động thông qua năm câu hỏi với giả định rằng bản phân tích đã được người khác chuẩn bị. Hãy tiếp tục với ví dụ về các khoản phải thu. Trong quá trình kiểm toán, đoàn kiểm toán sẽ xem xét số dư các khoản phải thu để xác nhận hai điều: 1. Các khoản phải thu tồn tại và hợp pháp. 2. Số tiền phản ánh trên bảng cân đối kế toán bao gồm tất cả các khoản phải thu và được hoàn thành. Hiểu các khoản phải thu liên quan đến việc xem xét bản phân tích do khách hàng chuẩn bị, trong đó phải được giải thích. Hình minh họa 8.2, biểu đồ cột, là một ví dụ về khoản phải thu phân tích được gọi là báo cáo lão hóa các khoản phải thu. Biểu đồ chia tổng các khoản phải thu thành các loại dựa trên thời điểm các khoản phải thu đến hạn. Mỗi thanh trong biểu đồ đại diện cho tổng số khoản phải thu đến hạn của từng loại.

![ILLUSTRATION 8.2](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.2.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Phân tích này có thể là một trong nhiều phân tích mà nhóm kiểm toán phải giải thích. Nó giúp kiểm toán viên hiểu mối quan hệ giữa tổng các khoản phải thu và sự phân tích về cách thức phần lớn trong số đó đã quá hạn và trong bao lâu. Hãy tưởng tượng nhóm kiểm toán đang kiểm tra xem liệu việc định giá khoản dự phòng phải thu khó đòi có tài khoản là phù hợp. Khách hàng đã cung cấp hình ảnh trực quan trong Hình minh họa 8.3.

**MINH HỌA 8.2 Tài khoản Phân tích lão hóa các khoản phải thu Phân tích các khoản phải thu $0- 50.000 USD 100.000 USD 150.000 USD 200.000 USD 250.000 USD 300.000 USD 350.000 USD 400.000 USD 450.000 USD 0 30 60 90 Trên 90 Số ngày chưa thanh toán**

**MINH HỌA 8.3 Tài khoản Tuổi phải thu và phần trăm của Tài khoản không thể thu hồi 0 10 20 30 40 50 60 70 80% Số dư các khoản phải thu và Phần trăm không thể thu thập được $0- 50.000 USD 100.000 USD 150.000 USD 200.000 USD 250.000 USD 300.000 USD 350.000 USD 400.000 USD 450.000 USD 0 30 60 90 Trên 90 72% 37% 8% 5% 3% Số ngày chưa thanh toán Số dư tài khoản phải thu Phần trăm không thể thu thập được Một số điểm quan trọng về hình dung này: • Đây là biểu đồ trục kép, giúp minh họa mối quan hệ giữa các biến với thang đo khác nhau. • Ví dụ này kiểm tra tổng số tiền các khoản phải thu trong mỗi trong năm loại tuổi thọ và tỷ lệ phần trăm của các khoản phải thu đó không thể thu thập được. • Trục trái thể hiện số lượng các khoản phải thu bằng đô la Mỹ. Trục bên phải là tỷ lệ các khoản phải thu không thể thu hồi được. • Bao gồm cả hai biến trong hình ảnh hóa sẽ hiển thị tổng số khoản phải thu theo thời hạn loại và bao nhiêu phần trăm trong số các khoản phải thu đó được coi là không thể thu hồi được.**

![ILLUSTRATION 8.3](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.3.png)

## 8.1  Chúng tôi rút ra kết luận từ phân tích dữ liệu bằng cách nào?

Hãy nhớ lại khóa học kế toán tài chính đầu tiên của bạn rằng khoản dự phòng cho các khoản nợ khó đòi tài khoản là ước tính các khoản phải thu không thể thu hồi được. Số tiền này sau đó sẽ được khấu trừ từ số dư các khoản phải thu được báo cáo trên bảng cân đối kế toán của công ty. Nhóm kiểm toán đã yêu cầu khách hàng cung cấp thông tin liên quan đến tuổi của hiện tại số dư các khoản phải thu (báo cáo tuổi nợ các khoản phải thu) và ước tính bao nhiêu phần trăm- tuổi của số dư là không thể thu hồi được. Bây giờ là lúc diễn giải phân tích mà khách hàng có được cung cấp. Một trong những kỹ năng được đánh giá cao nhất của kế toán viên là khả năng độc lập và người đánh giá hoài nghi về thông tin tài chính. Hình minh họa

## 8.4 là một ví dụ ngắn gọn về dữ liệu phân tích diễn giải hình ảnh ở Hình minh họa 8.3. Mỗi bước được trình bày chi tiết hơn trong suốt chương.

Quá trình phiên dịch

Ví dụ: Giải thích hình minh họa 8.23 học tập Mục tiêu Bước 1: Xác định xem phân tích có ý nghĩa hay không.

1. Việc phân tích trả lời dự định đặt câu hỏi và phù hợp với mục tiêu ban đầu?

- Câu hỏi đặt ra là liệu khoản dự phòng cho các khoản phải thu khó đòi có hợp lý hay không. Phân tích này tiết lộ một số hiểu biết sâu sắc, nhưng cần thêm thông tin.

- Ví dụ: chúng tôi không biết số dư trong khoản dự phòng phải thu khó đòi. LỘ 3 2. Dữ liệu có chính xác không và các phương pháp được sử dụng để thực hiện phân tích? Dữ liệu:

- Để đưa ra nhận định này, hãy kiểm tra dữ liệu để xác nhận đúng các khoản phải thu dữ liệu được sử dụng trong phân tích.

- Xác nhận rằng dữ liệu được sử dụng để tính toán số phần trăm không thể thu được là chính xác đúng. LỘ 3 Phương pháp:

- Phân tích mang tính chất mô tả. Tổng số các khoản phải thu đến hạn ngày được cung cấp ở trục bên trái và phần trăm không thể thu thập được minh họa bằng một gọi ra từng phần trăm theo danh mục. Xác định xem đây có phải là cách phù hợp nhất không phương pháp.

- Vì mục tiêu là xác định xem việc định giá có hợp lý hay không nên có thể so sánh về khoản dự phòng cho các tài khoản nghi ngờ trong 5 năm qua số dư phải thu sẽ phù hợp hơn. LỘ 3 3. Là kết quả hợp lý, hoặc hơn thế nữa phân tích cần thiết?

- Để đưa ra đánh giá này, hãy so sánh thông tin trong phân tích với thông tin được biết về các khoản phải thu của khách hàng. Nếu tổng số phù hợp với báo cáo tài chính các báo cáo và ước tính về các tài khoản khó đòi thì việc phân tích sẽ được thực hiện hợp lý.

- Chúng ta cũng có thể đánh giá xem việc hình dung có hợp lý hay không. Ví dụ, hầu hết các khoản phải thu phải nằm trong danh mục dưới 30 ngày và các khoản phải thu rất có thể không thể thu được sẽ thuộc loại trễ hoặc hơn 90 ngày. LỘ 3 Bước 2: Xác minh kết quả là hợp lệ và đáng tin cậy. 4. Việc phân tích đo lường những gì đã được dự định? Hiệu lực đề cập đến mức độ phân tích thể hiện thực tế:

- Trong ví dụ này, hãy xác định xem hình ảnh trực quan có thể hiện sự phân tích về dự phòng cho việc định giá các tài khoản nghi ngờ. LỘ 4 và LÔ 5 5. Là kết quả chính xác? Độ chính xác có nghĩa là các thước đo được sử dụng trong phân tích là chính xác và không có sai lầm:

- Các thước đo được sử dụng trong hình dung là số dư tài khoản, số ngày chưa thanh toán, và tính toán phần trăm tài khoản không thể thu hồi được. Tất cả đều đúng biện pháp.

- Xác nhận số tiền là chính xác bằng cách so sánh các khoản phải thu với số tiền trên báo cáo tài chính. LỘ 4 và LÔ 5 MINH HỌA 8.4 Tổng quan về diễn giải phân tích dữ liệu

![ILLUSTRATION 8.4](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.4.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Áp dụng nó

## 8.1 Giải thích doanh thu Trực quan hóa Dữ liệu Kế toán tài chính Denton Hospitality, Inc. (DHI) là một chuỗi khách sạn ở phía Tây Nam Hoa Kỳ. Dante Garcia bắt đầu chuỗi khách sạn ở Denton, Texas vào năm 1968 với một khách sạn. Kể từ khi sau đó, chuỗi đã phát triển lên 48 khách sạn ở 4 bang. Dante nghỉ hưu năm 2002 và được kế nhiệm làm Giám đốc điều hành bởi con gái của ông, Luciana. Các khách sạn của DHI thuộc phân khúc lưu trú bình dân. Bất động sản ở Colorado, Oklahoma, New Mexico và Texas. Một khách sạn kinh tế điển hình có trung bình 84 phòng, mặc dù DHI khách sạn trung bình 117 phòng. Tòa nhà có tổng giám đốc, nhân viên lễ tân gồm 6 người, một quản gia trưởng, 7 quản gia và một nhân viên bảo trì. Ngoại trừ tổng giám đốc, nhân viên được trả lương theo giờ và số giờ được chỉ định của họ thay đổi tùy theo nhu cầu. Tóm tắt của DHI hiệu quả tài chính được cung cấp. Tổng cộng Số lượng Khách sạn tiểu bang $8,491,172 $ 6,972,316 5 7 5 31 Doanh thu 2024 Doanh thu 2025 Lợi nhuận 2024 CO NM được rồi TX $6,223,433 $62,907,543 48 $41,220,622 $8,414,229 $6,942,074 $ 6,156,051 $61,584,276 $ 40,071,922 $4,025,218 $ 3,701,428 $ 3,178,742 $ 29,226,377 $18,320,989 Lợi nhuận 2025 $ 3,862,043 $ 3,582,689 $ 2,928,290 $ 26,921,198 $16,548,176 Tóm tắt kết quả tài chính của DHI DHI muốn biết so sánh doanh thu giữa các bang như thế nào và doanh thu đang tăng hay giảm. Luciana đã yêu cầu bạn giải thích phân tích này.

1. Liệt kê các câu hỏi bạn sẽ hỏi để diễn giải phân tích này và đưa ra câu trả lời.

2. Đây là phân tích dữ liệu thăm dò hay diễn giải phân tích dữ liệu? tiểu bang Doanh thu 2024 2025 $0 CO $7,0$6,9 $6,2 $6,2 $41,2 $40,1 NM được rồi TX $5 $10 $15 Denton Hospitality, Inc. ‒ Doanh thu theo tiểu bang $20 $25 $30 $35 $40 $45 8,5 USD 8,4 USD GIẢI PHÁP

1. Phân tích có trả lời được câu hỏi và phù hợp với mục tiêu không? Vâng:

- Câu hỏi đặt ra là so sánh thu nhập của các tiểu bang như thế nào và liệu thu nhập có tăng lên hay không.

- Biểu đồ thể hiện doanh thu theo tiểu bang và so sánh với năm trước.

## 8.2  Mối quan hệ giữa tư duy phản biện và diễn giải phân tích dữ liệu là gì?  8-7

## 8.2  Mối quan hệ là gì

Giữa Tư duy phản biện và dữ liệu Giải thích phân tích?

**MỤC TIÊU HỌC TẬP ➋**

Áp dụng tư duy phản biện vào việc giải thích phân tích dữ liệu. Trong phần mở đầu chương, Megan đã thảo luận về tầm quan trọng của tư duy phản biện trong phân tích dữ liệu. Suy nghĩ sâu sắc về phân tích giúp diễn giải kết quả và tránh bị “. . . quá bị mắc kẹt chi tiết hơn để tôi hợp lý hóa kết quả thay vì đặt thêm câu hỏi.” Áp dụng một khuôn khổ tư duy phản biện đối với phân tích được diễn giải đảm bảo rằng chúng ta nhất quán suy nghĩ chín chắn về mọi phân tích. Hãy sử dụng tư duy phê phán để diễn giải bản phân tích dữ liệu do người khác chuẩn bị. Người đàn ông- Công ty sản xuất Super Scooters sản xuất bốn mẫu xe tay ga:

- Model Captain và Lazer là xe máy điện.

- Mẫu Kicks không được cấp điện.

- Celeritas là xe tay ga chạy bằng xăng. Dữ liệu và phương pháp được sử dụng để thực hiện phân tích có chính xác không? Vâng:

- DHI quan tâm đến hiệu quả doanh thu. Biểu đồ này bao gồm doanh thu.

- DHI cũng muốn biết hiệu quả hoạt động của từng bang và liệu doanh thu có tăng lên hay không. Thanh này biểu đồ hiển thị thông tin đó bằng cách nhóm doanh thu theo tiểu bang và hiển thị năm hiện tại so với năm trước. Kết quả có hợp lý không? Có lẽ:

- Cần khẳng định sự hiểu biết về DHI và doanh thu của họ để đưa ra quyết định cuối cùng quyết định về tính hợp lý.

- Biểu đồ thanh hiển thị có bao nhiêu khách sạn ở mỗi tiểu bang. Có vẻ hợp lý đó Texas có doanh thu cao nhất vì khoảng 65% tổng số khách sạn nằm ở Texas. Phân tích có hợp lệ không? Tức là nó có đo lường được những gì nó định đo lường không? Có lẽ:

- Các kết quả có vẻ hợp lý vì phân tích đã đo lường được những gì dự kiến– thu theo từng bang và so sánh với năm trước. Phân tích có chính xác (đáng tin cậy) không? Có lẽ:

- Cần nhiều nghiên cứu hơn để so sánh kết quả với báo cáo tài chính để đảm bảo tất cả doanh thu được trình bày và phân tích là chính xác. 2. Vì DHI yêu cầu giải thích kết quả phân tích nên có vẻ hợp lý rằng đây là một giải thích. Nếu nhiệm vụ diễn giải phân tích này để xác định các phân tích bổ sung có thể được thực hiện dựa trên kết quả, nó có thể được coi là mang tính thăm dò.

Chương 8 Diễn giải kết quả phân tích dữ liệu Super Scooters đã được hưởng lợi từ sự gia tăng của hệ thống chia sẻ xe tay ga ở các thành phố lớn. Giống như chia sẻ xe đạp, hệ thống chia sẻ xe tay ga là dịch vụ cung cấp xe tay ga cho những chuyến đi ngắn hạn. cho thuê. Thị trường xe máy điện toàn cầu ước tính đạt 34,7 tỷ USD vào năm 202

## 8.1 Các công ty như Lime và Bird đang mua số lượng lớn xe máy điện vì thị trường chia sẻ xe tay ga mở rộng. Super Scooters tin rằng đã đến lúc phải di chuyển chỉ sản xuất xe máy điện để có khả năng tăng doanh số bán hàng cho các công ty như Lime và Chim. Hãy tưởng tượng bạn là một nhân viên kế toán, là thành viên của một nhóm đang đánh giá xem có nên tiếp tục sản xuất mẫu xe ga ga Celeritas. Hãy áp dụng các yếu tố của tư duy phản biện (Minh họa 8.5) cho ví dụ này. 1https://www.grandviewresearch.com/industry-analysis/electric-scooters-market

**MINH HỌA 8.5 TIA LỬA Khung tư duy phản biện Mục đích Rủi ro Tự- Sự phản ánh Kiến thức Các bên liên quan Lựa chọn thay thế Phiên dịch**

**MINH HỌA 8.6 Siêu Xe tay ga bên trong và bên ngoài Các bên liên quan Các bên liên quan nội bộ Các bên liên quan bên ngoài • Người quản lý siêu xe tay ga • Nhân viên siêu xe tay ga • Nhà đầu tư • Chủ nợ Các bên liên quan: Hiểu bối cảnh Trước khi diễn giải phân tích do nhóm tiếp thị Celeritas cung cấp, hãy xem xét ai các bên liên quan đều có mặt trong quyết định này. Xác định các bên liên quan (Minh họa 8.6) cung cấp cái nhìn sâu sắc về tình huống mà phân tích dữ liệu được tạo ra. Kiến thức này có thể giúp giải thích kết quả.**

![ILLUSTRATION 8.6](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.6.png)

## 8.2  Mối quan hệ giữa tư duy phản biện và diễn giải phân tích dữ liệu là gì?  8-9

Không xác định được các bên liên quan có nghĩa là có khả năng diễn giải kết quả từ quan điểm sai lầm. Trong ví dụ này, nếu bạn không nghĩ đến chủ nợ của Super Scooters, bạn có thể không xem xét tác động của việc loại bỏ xe tay ga Celeritas đối với khả năng của công ty trả các khoản vay hiện tại của họ. Mục đích: Xác định “Tại sao” của Phân tích Ngoài việc nhận ra các bên liên quan, hãy xác định mục đích của việc phân tích. Thật dễ dàng hãy quên điều này đi và bắt đầu phiên dịch ngay lập tức. Hãy cẩn thận để không rơi vào cái bẫy này! Chúng tôi không thể diễn giải đầy đủ một phân tích cho đến khi chúng ta biết mục đích của nó. Trong ví dụ này, Super Scooters đang xem xét loại bỏ xe tay ga Celeritas. các Đội ngũ tiếp thị của Celeritas đã chuẩn bị bản phân tích doanh số bán hàng trong bốn năm qua và dự báo cho năm 2026. Phần tô bóng của đường biểu thị dự báo năm 2026. Mục đích của việc phân tích là để hiểu xu hướng bán hàng của bốn mẫu xe tay ga chạy bằng điện mà Super Scooters hiện đang sản xuất và bán. Bỏ qua mục đích có thể có nghĩa là diễn giải phân tích không chính xác. Nếu bạn không biết mục đích của việc phân tích trong Hình minh họa 8.7 là để đánh giá mô hình Celeritas, bạn có thể lãng phí thời gian đánh giá một mô hình khác.

**MINH HỌA 8.7 Dự báo siêu xe ga Lazer 0 1.000 2.000 cú đá 0 1.000 2.000 Celeritas người mẫu 0 1.000 2.000 thuyền trưởng Dự báo siêu xe tay ga năm 2026 - Khối lượng bán hàng (Chiếc) 0 1.000 2.000 Tháng 11 2026 tháng 5 2026 tháng 5 2023 tháng 5 2024 tháng 5 2025 Tháng 11 2025 Tháng 11 2022 Tháng 11 2023 Tháng 11 2024 Các lựa chọn thay thế: Điều tra các cách giải thích khác Luôn cân nhắc xem có cách nào khác để xem kết quả phân tích hay không. Ngoài ra, xem xét liệu có phương pháp thay thế nào để tiến hành phân tích chưa được giải quyết hay không. Cuối cùng, quyết định xem có cần phân tích thêm hay không. Suy nghĩ về những lựa chọn thay thế khác nhau này sẽ giúp xác định xem liệu phân tích phù hợp nhất có được sử dụng hay không, điều này có thể làm tăng độ tin cậy khi diễn giải kết quả.**

![ILLUSTRATION 8.7](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.7.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Trong ví dụ về Super Scooters, các cách hiểu khác có thể bao gồm:

- Các giả định về phân tích xu hướng không bao gồm tác động tiềm ẩn đến doanh số bán hàng của phương thức khác những người khác nếu Celeritas bị loại bỏ.

- Các giả định về phân tích xu hướng có thể quá mạnh mẽ.

- Chỉ phân tích xu hướng thì không đủ thông tin để làm cơ sở cho quyết định giữ hoặc thả chiếc xe tay ga Celeritas.

- Mô hình Kicks có hiệu suất kém nhất. Có lẽ mô hình đó nên được đánh giá để loại bỏ thay vì Celeritas. Rủi ro: Xem xét dữ liệu, phân tích và sai lệch Kiểm tra tất cả các khía cạnh của phân tích để xác định rủi ro tiềm ẩn. Điều này bắt đầu với dữ liệu và mở rộng đến những thành kiến tiềm tàng – của cả chúng ta và của các bên liên quan. Hỏi nhất định các câu hỏi có thể giúp đánh giá những rủi ro tiềm ẩn này. Hình minh họa 8.8 liệt kê các rủi ro, câu hỏi có thể được yêu cầu đánh giá chúng và áp dụng ví dụ về Siêu xe tay ga. Hãy ghi nhớ rằng nếu bạn là người chuẩn bị phân tích thì bạn đã giải quyết được một số vấn đề những vấn đề này. Rủi ro tiềm ẩn Câu hỏi Ví dụ về siêu xe tay ga dữ liệu

- Tính đầy đủ: Là sự phân tích thiếu dữ liệu liên quan?

- Độ chính xác: Dữ liệu có được sử dụng trong phân tích đúng không?

- Tính kịp thời: Dữ liệu có được sử dụng trong phân tích mới nhất có sẵn?

- Kiểm soát nội bộ: Đã kiểm soát nội bộ thích hợp trong nơi để đảm bảo dữ liệu được sử dụng là đúng không?

- Một số dữ liệu bán hàng không được bao gồm hoặc có thể không chính xác.

- Dữ liệu bắt đầu vào năm 2022 và tiếp tục đến năm 2026, vì vậy chúng xuất hiện kịp thời. Phân tích

- Phương pháp: Là phương pháp đúng được sử dụng để thực hiện phân tích?

- Dữ liệu: Phân tích có sử dụng đúng không dữ liệu?

- Mục đích: Phân tích đã trả lời câu hỏi?

- Mục đích của việc phân tích là để hiểu việc bán hàng xu hướng dành cho Super Scooter các mô hình.

- Việc phân tích sử dụng doanh thu số tiền từ năm 2022 đến năm 2025, vì vậy nó cho thấy doanh số bán hàng như thế nào xu hướng.

- Nguy cơ sử dụng sai cách ước tính dự báo năm 2026 số liệu cần được xem xét. thiên vị

- Thành kiến dữ liệu: Có phải tất cả đều cần thiết và dữ liệu thích hợp có trong phân tích?

- Thành kiến của người chuẩn bị: Người chuẩn bị có có bất kỳ thành kiến ​​tiềm ẩn nào có thể đã ảnh hưởng đến việc chuẩn bị phân tích?

- Thành kiến của người đánh giá: Người đánh giá có (bạn) có bất kỳ thành kiến nào có thể ảnh hưởng đến việc giải thích các kết quả?

- Dữ liệu có thể bị sai lệch nếu phân tích không bao gồm tất cả các dữ liệu bán hàng có sẵn.

- Người chuẩn bị có thể là thiên vị để cung cấp một tích cực phân tích nếu họ không muốn để loại bỏ Celeritas mô hình.

- Người đánh giá có thể bị thiên vị ủng hộ việc loại bỏ Celeritas hoặc ủng hộ việc giữ mô hình Celeritas MINH HỌA 8.8 Câu hỏi giúp xác định rủi ro

![ILLUSTRATION 8.8](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.8.png)

## 8.2  Mối quan hệ giữa tư duy phản biện và diễn giải phân tích dữ liệu là gì?  8-11

Kiến thức: Những điều chúng ta cần biết Để giải thích bất kỳ phân tích nào, hãy xác định kiến thức cần thiết để hiểu nó. Chúng tôi có thể không có nền tảng hoặc kinh nghiệm chính xác, do đó việc xác định mức độ hiểu biết cần thiết sẽ tiết lộ liệu chúng tôi có cần thực hiện nghiên cứu bổ sung hay không. Sẽ rất hữu ích khi hỏi những câu hỏi sau:

- Kiến thức kế toán cụ thể có cần thiết không?

- Kiến thức về ngành có hữu ích không?

- Kiến thức công nghệ có quan trọng để diễn giải kết quả phân tích không?

- Nghiên cứu bổ sung có cần thiết hay chúng ta nên tìm kiếm sự giúp đỡ của chuyên gia? Những loại kiến thức nào cần thiết để diễn giải chiến lược của nhóm tiếp thị Celeritas phân tích?

- Kiến thức kế toán: Hiểu được dự báo doanh thu đòi hỏi phải biết doanh thu doanh thu và cách tính toán dự báo. Để xác định xem có nên ngừng sử dụng Mô hình Celeritas, sự hiểu biết về chi phí, phân tích lợi nhuận theo khối lượng chi phí và cách thực hiện hình thành một phân tích giữ hoặc thả là cần thiết.

- Kiến thức ngành: Super Scooters hoạt động trong lĩnh vực ô tô và vận tải ngành công nghiệp, vì vậy bạn sẽ cần thông tin về ngành sản xuất khí đốt- xe máy điện và xe máy điện. Tìm hiểu về chuỗi cung ứng cho sản xuất xe tay ga và xe điện, cũng như các đối thủ cạnh tranh trong lĩnh vực sản xuất xe tay ga sản xuất, cũng sẽ rất quan trọng.

- Kiến thức công nghệ: Trong ví dụ này, hình ảnh trực quan thể hiện doanh thu và doanh số bán hàng dự báo cho mô hình Celeritas (Minh họa 8.7). Hiểu cách hình dung này được tạo ra sẽ rất hữu ích vì kiến thức về phần mềm sẽ giúp bạn đánh giá tốt hơn sự trực quan hóa.

- Kiến thức khác: Nếu bạn cần có kiến thức về kế toán, ngành hoặc kỹ thuật, hãy làm nghiên cứu bổ sung và/hoặc yêu cầu sự giúp đỡ của người có kiến thức đó. Tự suy ngẫm: Nghĩ về những bài học đã học Mỗi dự án phân tích dữ liệu nên bao gồm việc phản ánh các bài học rút ra từ các phân tích trước đó được thực hiện hoặc giải thích. Chúng ta cũng có thể học hỏi từ việc phân tích dữ liệu hiện tại đang được thực hiện hoặc giải thích và áp dụng điều đó cho các dự án phân tích dữ liệu trong tương lai. Suy ngẫm về những kinh nghiệm trước đây giúp chúng ta thực hiện các diễn giải một cách nhanh chóng, kỹ lưỡng và chính xác. Trong ví dụ về Siêu xe tay ga, hãy suy ngẫm về những phân tích khác mà bạn đã thực hiện có thể tương tự. Bạn có thực hiện bất kỳ phân tích giữ hoặc bỏ nào trong các khóa học đại học của mình không? Bạn đã phân tích doanh số chưa phân tích xu hướng trước đó? Nếu vậy, làm thế nào bạn có thể áp dụng những kinh nghiệm đó vào cách giải thích này? Áp dụng nó 8.2 Đánh giá chi phí Phân tích Kiểm toán Giám đốc điều hành của Denton Hospitality, Inc. (DHI) Luciana Garcia lo ngại về chi phí ngày càng tăng tại một số khách sạn và đã yêu cầu bộ phận kiểm toán nội bộ đánh giá những khách sạn nào có tăng chi phí trong hai năm qua. Với tư cách là kiểm toán viên nội bộ của DHI, người quản lý của bạn đã yêu cầu bạn chuẩn bị và giải thích bản phân tích chi phí của khách sạn trong hai năm qua và xác định các địa điểm với mức tăng cao nhất. Liệt kê từng yếu tố tư duy phản biện và xác định cách bạn áp dụng nó vào ví dụ này. GIẢI PHÁP Yếu tố tư duy phản biện Ví dụ Các bên liên quan Nội bộ: Bộ phận mua hàng, quản lý khách sạn Bên ngoài: Chủ nợ, nhà cung cấp Chương 8 Diễn giải kết quả phân tích dữ liệu 8.3 Làm sao chúng tôi biết được phân tích Hợp lý không? MỤC TIÊU HỌC TẬP ➌ Xác định xem kết quả phân tích dữ liệu có trả lời được câu hỏi và phù hợp với mục tiêu của phân tích. Hãy nhớ lại rằng bước đầu tiên trong việc giải thích dữ liệu là xác định xem phân tích đó có hợp lý hay không. Đây có vẻ là một câu hỏi hiển nhiên nhưng lại là một câu hỏi thường bị bỏ qua. Nó thậm chí còn hơn thế nữa quan trọng khi cố gắng hiểu một phân tích về một cái gì đó không quen thuộc. Về mặt dữ liệu phân tích, hỏi xem phân tích có “có ý nghĩa” hay không có nghĩa là xác nhận phân tích có ý nghĩa rõ ràng ý nghĩa. Sử dụng kỹ năng tư duy phê phán, xác định xem phân tích có trả lời được câu hỏi dự định hay không và phù hợp với mục tiêu, nếu dữ liệu và phương pháp chính xác được sử dụng và nếu cả hai kết quả đều đạt được hợp lý và đầy đủ cho mục đích của dự án. Đánh giá dữ liệu và phương pháp Các câu hỏi chúng ta có thể đặt ra để xác định xem phân tích có hợp lý hay không bao gồm việc suy nghĩ về cách thức chúng tôi đã nhận được kết quả:

- Dữ liệu được sử dụng trong phân tích có hợp lý với câu hỏi/mục tiêu phân tích không?

- Phương pháp phân tích có hợp lý với câu hỏi/mục tiêu phân tích không? Mục đích Đánh giá chi phí theo địa điểm của khách sạn và xác định chi phí nào các địa điểm đã có sự gia tăng. Lựa chọn thay thế Có thể có những phân tích thay thế có thể hoặc nên hãy chuẩn bị sẵn sàng. Cũng có thể có những cách giải thích khác nhau tại sao chi phí lại tăng lên. Ví dụ, tăng công suất phòng khách sạn có thể thúc đẩy sự gia tăng ở khách sạn chi phí. Rủi ro Dữ liệu có thể bị thiếu hoặc không chính xác. Một phân tích có thể là giải thích sai. Kiến thức Kiến thức về công ty và ngành nghề, khách sạn chi phí, việc chuẩn bị và giải thích dữ liệu phân tích là cần thiết. Tự phản ánh Có thể có những phân tích chi phí từ các dự án trước đó có thể áp dụng cho cái này Hãy xem xét liệu bạn có thể áp dụng những gì đã học được trong dự án này vào tương lai dự án.

## 8.3  Làm sao chúng tôi biết phân tích đó có ý nghĩa?

Hình minh họa 8.9 là một phân tích được thiết kế để chỉ ra liệu chi phí lao động của Super Scooters trong Char- Lotte, vị trí NC tăng lên khi doanh số bán hàng tăng lên. Dữ liệu được sử dụng trong phân tích có hợp lý với câu hỏi/mục tiêu của phân tích không?

- Số liệu sử dụng trong biểu đồ này là chi phí nhân công và doanh số bán hàng. Sử dụng là hợp lý hai thước đo này vì chúng ta muốn biết liệu chúng có liên quan với nhau hay không. Nói cách khác, làm cả hai các biện pháp di chuyển theo cùng một hướng? Phương pháp phân tích có hợp lý với câu hỏi/mục tiêu phân tích không?

- Biểu đồ trục kép so sánh hai thước đo khác nhau trong một biểu đồ. Số chi phí lao động số tiền ($50 nghìn–$250 nghìn) lớn hơn nhiều so với số lượng bán ra (1.000– 4.000). Nếu sử dụng biểu đồ cột liên cụm (Minh họa 8.10) để thay thế, khối lượng bán hàng thanh sẽ quá nhỏ để phân biệt một mối quan hệ. 250.000 USD 200.000 USD 150.000 USD 100.000 USD 50.000 USD 1.609 2,871 3.743 $0 2022 0 1.000 1.500 500 2.000 2.500 3.000 3.500 4.000 bán hàng khối lượng Lao động Chi phí 2023 2024 Charlotte, NC Khối lượng bán hàng và chi phí lao động Năm Chi phí lao động Tổng khối lượng bán hàng MINH HỌA 8.9 Biểu đồ trục kép về khối lượng bán hàng và chi phí nhân công MINH HỌA 8.10 Phân cụm Biểu đồ cột về khối lượng bán hàng và Chi phí lao động 250.000 USD 200.000 USD 150.000 USD 100.000 USD $69,834 $146,024 $205,673 50.000 USD $0 2022 2023 2024 Charlotte, NC Khối lượng bán hàng và chi phí lao động bán hàng khối lượng Chi phí lao động theo năm Chi phí lao động Tổng khối lượng bán hàng

![ILLUSTRATION 8.9](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.9.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Kiểm tra kết quả Ngoài ra còn có những câu hỏi đánh giá tính hợp lý của bản thân kết quả:

- Kết quả phân tích có hợp lý với những gì đã biết về chủ đề đang được đã phân tích? • Super Scooters sản xuất xe tay ga mà họ bán. Điều đó có ý nghĩa như số số lượng xe tay ga được bán tăng lên, họ sẽ cần sản xuất nhiều xe tay ga hơn. Tăng sự ủng hộ lao động sẽ dẫn đến tăng lao động.

- Ý nghĩa của việc phân tích có hợp lý dựa trên những gì đã biết về chủ đề này không? đang được phân tích? • Ý nghĩa là nếu Super Scooters tiếp tục tăng doanh số thì họ sẽ đã tăng chi phí lao động.

- Phân tích có giải quyết được nhu cầu/mối quan tâm của các bên liên quan không? • Mối quan tâm chung là liệu doanh số bán hàng và chi phí lao động tại Charlotte có tăng hay không vị trí có liên quan. Các bên liên quan bao gồm việc quản lý Super Scooters và nhân viên ở các địa điểm Charlotte. Phân tích này sẽ giúp họ hiểu rõ hơn mối quan hệ giữa khối lượng bán hàng và chi phí lao động. Nếu câu trả lời cho bất kỳ câu hỏi nào trong số này là “không” thì có thể là có nhiều hơn hoặc có sự khác biệt. phân tích sâu hơn là cần thiết trước khi kết quả có thể được giải thích. ÁP DỤNG TƯ duy phản biện 8.1: Hỏi xem liệu Phân tích có có ý nghĩa Lưu ý mối quan hệ giữa những câu hỏi này và cuộc thảo luận trước đây về việc áp dụng tư duy phê phán. Để trả lời những câu hỏi này, bạn cần biết:

- Ai bị ảnh hưởng bởi việc phân tích (Các bên liên quan).

- Lý do thực hiện phân tích (Mục đích).

- Kết quả có hợp lý dựa trên những gì bạn biết (Kiến thức) hay không.

- Liệu bạn có thể áp dụng kinh nghiệm hoặc kiến thức trong quá khứ vào bối cảnh hiện tại hay không và liệu những gì bạn việc học bây giờ có thể được tận dụng trong các phân tích trong tương lai (Tự suy ngẫm). Xác định xem có thêm thông tin hoặc phân tích là cần thiết Ngay cả khi sự giải thích có ý nghĩa, đôi khi có thêm thông tin hoặc phân tích bổ sung- ses vẫn cần thiết để trả lời kỹ lưỡng câu hỏi. Thật dễ dàng để tin rằng chúng ta có thông tin cần thiết để quyết định một quá trình hành động. Đây là một thành kiến phổ biến của con người Nhà tâm lý học đoạt giải Nobel Daniel Kahneman gọi “những gì bạn thấy là tất cả”. có “sự thiên vị”. Sự thiên vị này có thể đặc biệt mạnh mẽ nếu việc phân tích dữ liệu hỗ trợ các ý tưởng định sẵn hoặc kết luận về câu hỏi. Kế toán viên phải là người đánh giá thông tin một cách hoài nghi, vì vậy chúng ta phải xem xét kỹ lưỡng các phân tích dữ liệu để đảm bảo chúng cung cấp đủ thông tin và hỗ trợ. cảng để đưa ra quyết định sáng suốt. Có nhiều thành kiến hơn cần lưu ý khi diễn giải các phân tích dữ liệu:

- Thiên kiến xác nhận: Người thực hiện phân tích muốn chứng minh một yếu tố tiền định- giả định được khai thác, vì vậy họ tìm kiếm dữ liệu hỗ trợ niềm tin hiện có của họ. người đó

## 8.3  Làm sao chúng tôi biết phân tích đó có ý nghĩa?

diễn giải phân tích cũng có thể có sai lệch này. Nhận thức được tiềm năng của người chuẩn bị những thành kiến thiên vị, cũng như của chính chúng ta, có thể giúp giảm thiểu những thành kiến xác nhận.

- Sai lệch lựa chọn: Sai lệch này xảy ra khi dữ liệu được sử dụng trong phân tích được chọn chủ đề. một cách tích cực. Sai lệch lựa chọn là mối lo ngại nếu phân tích được diễn giải dựa trên mẫu của dữ liệu chứ không phải toàn bộ dân số. Một ví dụ là khi phân tích doanh thu giao dịch dựa trên một mẫu giao dịch chứ không phải trên tất cả các giao dịch. Nếu mẫu không đại diện tốt cho toàn bộ tổng thể thì kết quả sẽ là thiên vị. Tiếp tục với ví dụ về Siêu xe tay ga, cần phải phân tích thêm trước khi đưa ra quyết định giữ hay bỏ. Hãy tưởng tượng rằng bạn yêu cầu thêm thông tin về chi phí và được phân tích ở Hình minh họa 8.11. (Giả sử bạn đã xác định rằng phân tích có ý nghĩa.) Phân tích này cung cấp một số thông tin chi phí quan trọng, nhưng bạn có cần thêm không? Biến chi phí sẽ bị loại bỏ nếu mô hình Celeritas bị loại bỏ, nhưng chi phí cố định thì sao? Hỏi cho thông tin đó là tốt. Đừng cho rằng việc phân tích doanh thu và chi phí biến đổi là tất cả những gì cần thiết để quyết định xem có nên loại bỏ mô hình Celeritas hay không. Ngoài ra còn có khả năng xảy ra sai lệch lựa chọn và sai lệch xác nhận. Hãy xem xét một số câu hỏi để tìm kiếm thiên hướng lựa chọn:

- Người chuẩn bị phân tích doanh thu và chi phí biến đổi có sử dụng tất cả thông tin có sẵn không, hay họ chỉ chọn một mẫu thông tin đó?

- Nếu là mẫu, mẫu có đại diện cho toàn bộ doanh thu và chi phí biến đổi không? Để giảm thiểu khả năng xảy ra sai lệch xác nhận, hãy xem xét quan điểm của bạn về các phân tích. Việc giải thích có được tiếp cận với tinh thần cởi mở hay bạn đã thiên về hay phản đối việc loại bỏ mô hình Celeritas? MINH HỌA 8.11 Biến Chi phí theo mẫu xe Super Scooter 2.600.000 USD thuyền trưởng Celeritas cú đá Lazer 2.400.000 USD 2.200.000 USD 2.000.000 USD 1.800.000 USD 1.600.000 USD 1.400.000 USD 1.200.000 USD 1.000.000 USD 800.000 USD 600.000 USD 400.000 USD 200.000 USD $0 2022 2023 2024 Tổng chi phí biến đổi theo mô hình Tổng biến Chi phí Áp dụng nó 8.3 Giải thích khoản tiền hoàn lại Phân tích Dữ liệu Kế toán quản trị Luciana tại DHI lo ngại về số tiền hoàn lại được đưa ra tới khách hàng. Cô ấy đã yêu cầu bạn nói chuyện với người quản lý khu vực khách sạn để hiểu rõ hơn và sau đó giải thích một phân tích do nhân viên khác chuẩn bị để xác định loại vị trí có mức độ cao nhất số tiền hoàn lại. Sau khi nói chuyện với người quản lý khu vực khách sạn, bạn biết được:

- Nhân viên lễ tân có thể hoàn tiền cho khách của khách sạn mà không cần sự chấp thuận của bộ phận chung người quản lý.

![ILLUSTRATION 8.11](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.11.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Biểu đồ trục kép về hoàn tiền DHI và khiếu nại của khách $0 0,00 USD $10,00 $20,00 $30,00 $40,00 $50,00 $60,00 20.000 USD Sân bay Xa lộ Liên tiểu bang Tàu điện ngầm/thị trấn ngoại ô thành thị 40.000 USD 60.000 USD 80.000 USD 100.000 USD 120.000 USD 140.000 USD 160.000 USD Loại vị trí Tổng cộng Hoàn tiền Tiền hoàn lại trung bình mỗi Khiếu nại Tổng số tiền hoàn lại Số tiền hoàn lại trung bình cho mỗi khiếu nại

- Người quản lý khu vực cho rằng số lượng khiếu nại của khách có liên quan chặt chẽ đến tổng số tiền hoàn lại tiền. Nếu có nhiều khiếu nại của khách, tổng số khiếu nại có thể sẽ cao hơn hoàn lại tiền. GIẢI PHÁP 1. Dữ liệu có vẻ hợp lý. Mục đích là hiểu được khiếu nại của khách và hoàn tiền. Cả hai của những mục đó được đưa vào phân tích. Số tiền hoàn lại trung bình cho mỗi khiếu nại thể hiện số tiền hoàn lại số tiền trên cơ sở mỗi khiếu nại. 2. Mục tiêu là xác định loại địa điểm có số tiền hoàn lại cao nhất. Việc phân tích hiển thị tổng số tiền hoàn lại trên một trục bằng cách sử dụng các thanh cho số tiền hoàn lại của từng địa điểm.

Phân tích cũng cho thấy số tiền hoàn lại trung bình cho mỗi khiếu nại là một đường có số tiền hoàn lại trung bình cho mỗi khiếu nại. khiếu nại ở trục bên phải. Đây là cách hợp lý để đánh giá mối quan hệ giữa khiếu nại và hoàn tiền vì việc sử dụng số tiền hoàn lại trung bình cho mỗi khiếu nại sẽ giúp xem xét từng vị trí dựa trên hiệu suất của nó hơn là kích thước.

3. Các nhà quản lý khu vực tin chắc rằng số lượng khiếu nại có liên quan đến tổng số số tiền hoàn lại. Phân tích cho thấy số tiền hoàn lại trung bình là cao nhất đối với sân bay các địa điểm mặc dù các địa điểm ngoại ô có tổng số cao hơn.

4. Tổng số tiền hoàn lại ở các khu vực ngoại ô cao hơn nhiều, nên có vẻ như họ sẽ có số lượng khiếu nại cao nhất. Tuy nhiên, nếu có nhiều khách sạn hơn trong danh mục đó, thì cũng có thể là nguyên nhân dẫn đến tổng số khiếu nại. Bằng cách sử dụng số tiền hoàn lại trung bình cho mỗi khiếu nại, chúng ta có thể thấy rằng các địa điểm ở sân bay đang hoàn lại tiền rất cao cho khách mặc dù tổng số tiền số tiền hoàn lại không cao như các địa điểm ngoại thành.

5. Phân tích đáp ứng được nhu cầu của các bên liên quan ở một mức độ nào đó. Phân tích là một phần của câu đố này.

6. Có, cần phân tích thêm. Để chắc chắn rằng chúng tôi đã giải quyết vấn đề với các bên liên quan, hơn nữa phân tích là cần thiết để giải quyết mối lo ngại về việc khách sạn hoàn lại quá nhiều tiền.

1. Dữ liệu được sử dụng trong phân tích có hợp lý không?

2. Phân tích có hợp lý không?

3. Kết quả phân tích có hợp lý dựa trên những gì bạn biết về chủ đề đang được phân tích không?

4. Ý nghĩa của việc phân tích có hợp lý không dựa trên những gì bạn biết về chủ đề đang được đề cập? đã phân tích?

5. Bản phân tích có giải quyết được nhu cầu và mối quan tâm của các bên liên quan không?

6. Có cần phân tích thêm không? Nếu có, bạn muốn xem những phân tích nào trước khi đưa ra quyết định?

## 8.4  Độ hiệu lực và độ tin cậy được xác định như thế nào trong các phân tích mô tả và chẩn đoán?  8-17

## 8.4  Hiệu lực và độ tin cậy như thế nào

Xác định trong mô tả và Phân tích chẩn đoán?

**MỤC TIÊU HỌC TẬP ➍**

Đánh giá tính hợp lệ và độ tin cậy của kết quả phân tích dữ liệu mô tả và chẩn đoán. Khi đã thấy rõ rằng phân tích có ý nghĩa thì kết quả có thể được đánh giá về tính giá trị và độ tin cậy. Nếu kết quả không hợp lệ thì việc phân tích có “tốt” đến đâu cũng không thành vấn đề. Đôi khi rất dễ bị đánh lừa bởi các phân tích dữ liệu vì chúng ta coi chúng theo mệnh giá. thu hồi ví dụ ở đầu chương. Nhân viên kế toán thuế của Megan đã kiểm tra các con số và cho rằng phân tích đó là đúng. Tuy nhiên, kết quả phân tích là sự gia tăng thuế trách nhiệm pháp lý khi lẽ ra nó phải được giảm bớt. Nhân viên kế toán lẽ ra phải có nhiều hơn thế hoài nghi về phân tích và cho rằng một khoản lỗ lớn đáng lẽ phải gây ra sự sụt giảm trong nghĩa vụ thuế. Đầu tiên, giá trị hợp lệ và đáng tin cậy có nghĩa là gì trong bối cảnh phân tích dữ liệu?

- Đánh giá giá trị của một phân tích dữ liệu bao gồm việc xác nhận rằng nó đo lường những gì nó được cho là để đo lường và thể hiện thực tế.

- Độ tin cậy có nghĩa là dữ liệu được sử dụng đáng tin cậy và các thước đo được sử dụng trong phân tích là nhất quán và chính xác. Trong bối cảnh này, chính xác có nghĩa là các biện pháp được sử dụng trong phân tích là chính xác và không có sai sót. Trong sự nghiệp của mình, bạn sẽ giải thích tính hợp lệ và độ tin cậy của các loại phân tích khác nhau- ses. Hình minh họa 8.12 tóm tắt các loại phân tích phổ biến nhất trong bốn lĩnh vực phân tích. MINH HỌA 8.12 Tóm tắt Phân tích theo Khu vực Phân tích Phân tích dữ liệu được phân loại theo mục đích Tần số Phân phối chéo lập bảng Các biện pháp Vị trí Các biện pháp phân tán sự bất thường Phát hiện Tương quan Phân tích Xu hướng Phân tích tuyến tính Hồi quy Dự đoán Thuật toán Tối ưu hóa Người mẫu Chuyện gì xảy ra nếu Phân tích mô tả Phân tích Chẩn đoán Phân tích Dự đoán Phân tích mang tính quy định Phân tích Phần này xem xét các loại phân tích phổ biến nhất được sử dụng trong mô tả và chẩn đoán. phân tích hoài cổ, cách xác định các biện pháp thích hợp cho từng loại và cách xác định nếu kết quả là hợp lệ.

![ILLUSTRATION 8.12](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.12.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Phân tích mô tả Phân tích mô tả giúp hiểu rõ hơn về dữ liệu làm nền tảng cho việc phân tích giả vờ. Để đánh giá tính giá trị và độ tin cậy của các phân tích, hãy đảm bảo sử dụng đúng phương pháp và rằng dữ liệu là chính xác. Hình minh họa 8.13 là bản tóm tắt các phân tích mô tả hợp lý dựa trên về mục tiêu của việc phân tích. Để phân tích có giá trị, phương pháp phải phù hợp với mục tiêu tive. Trong một phân tích đáng tin cậy, các biện pháp được sử dụng là chính xác và nhất quán. Mục tiêu Câu hỏi mẫu Phân tích hợp lệ Tìm hiểu các loại dữ liệu. Loại sản phẩm nào đang bán nhất? Đơn vị kinh doanh nào có doanh thu cao nhất? Phân phối tần số biểu đồ Tóm tắt theo danh mục và các danh mục phụ. Sản phẩm nào đang bán nhất ở mỗi vùng? bao nhiêu tổng chi phí hàng năm theo doanh nghiệp đơn vị? Lập bảng chéo phân tích Xác định trung bình quan sát trong dữ liệu. Trách nhiệm thuế trung bình đối với mỗi đơn vị kinh doanh? Trung bình (nếu không có ngoại lệ) trung vị Đánh giá sự phân bố của dữ liệu. Các chi phí trong từng đơn vị kinh doanh của công ty trung bình? Độ lệch chuẩn

**MINH HỌA 8.13 Mô tả Mục tiêu, câu hỏi và giá trị Phân tích HÌNH ẢNH 8.15 Siêu Tần suất mẫu xe tay ga Biểu đồ phân phối 1.400 1.200 1.000 800 600 400 200 0 thuyền trưởng Celeritas cú đá Lazer Tần số người mẫu Biểu đồ phân bổ tần suất mẫu xe siêu xe tay ga Hiểu danh mục dữ liệu Việc nhóm dữ liệu thành các danh mục đôi khi là một phần của quá trình phân tích. Một ví dụ là khi mục tiêu là để hiểu doanh số bán hàng theo sản phẩm. Nếu việc phân tích dựa trên các nhóm hoặc danh mục dữ liệu thì một kết quả hợp lệ phân tích sẽ là phân bố tần số hoặc phân tích bảng chéo. Sự phân bổ tần suất cho biết số lần một điều gì đó đã xảy ra trong một nhóm hoặc khoảng. Ví dụ trong Hình minh họa 8.14 được chuẩn bị bằng Super Scooters tập dữ liệu. ( Data How To 8.1 ở cuối chương hướng dẫn cách tạo hình ảnh này trong Power BI.) Cột tần suất báo cáo đơn hàng bán từng mẫu xe trong năm 2023–2025. các cột tần số tương đối cho biết tỷ lệ phần trăm của tổng số đơn đặt hàng cho từng mẫu.**

**MINH HỌA 8.14 Siêu Tần suất mẫu xe tay ga Phân phối người mẫu thuyền trưởng Celeritas 892 cú đá Lazer Tần số 1.010 456 Tổng doanh thu 3.645 1.287 24,5% Tần số tương đối 27,7% 12,5% 100,0% 35,3% Làm thế nào để Đôi khi các phân tích phân bổ tần suất ở dạng biểu đồ (Minh họa 8.15).**

![ILLUSTRATION 8.15](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.15.png)

## 8.4  Hiệu lực và độ tin cậy được xác định như thế nào trong phân tích mô tả và phân tích chẩn đoán?  8-19

Lưu ý rằng phân tích bảng chéo không nhất thiết phải ở dạng bảng. Minh họa 8.17 là biểu đồ cột của bảng trong Hình minh họa 8.16. Tóm tắt theo danh mục dữ liệu Giả sử mục tiêu là biết số lượng đơn hàng mỗi năm, từ 2023 đến 2025, bằng mô hình xe tay ga. Phân tích bảng chéo sẽ trả lời câu hỏi đó. Một điều cấm kỵ chéo- phân tích quan sát cho thấy số lượng quan sát trong một tập dữ liệu cho các danh mục con khác nhau (Minh họa 8.16).

**MINH HỌA 8.16 Siêu Phân tích bảng chéo xe tay ga Đơn đặt hàng theo mẫu thuyền trưởng Celeritas cú đá Lazer Tổng cộng Số lượng đơn đặt hàng người mẫu Năm 317 2025 369 88 1.337 563 248 2023 244 261 960 207 327 2024 397 107 1.348 517 892 Tổng cộng 1.010 456 3.645 1.287**

**MINH HỌA 8.17 Siêu Phân tích bảng chéo xe tay ga Biểu đồ cột 0 thuyền trưởng Celeritas cú đá Lazer 100 200 244 248 207 300 400 500 600 397 327 317 107 88 517 2023 2025 2024 Số lượng đơn đặt hàng mỗi năm Đơn đặt hàng Người mẫu 563 261 369 Chúng ta có thể diễn giải điều gì từ những phân tích này? Đầu tiên, Lazer là mẫu bán chạy nhất, chiếm 35,3% tổng sản lượng bán ra (Minh họa 8.14). Thứ hai, Lazer là phương tiện duy nhất mô hình cho thấy sự gia tăng về sản lượng bán hàng mỗi năm từ 2023 đến 2025 (Minh họa 8.17). Những phân tích này có hợp lệ và đáng tin cậy không? Vì mục tiêu là phân tích khối lượng bán hàng theo mô hình, thì phân bố tần số và phân tích bảng chéo là những phương pháp hợp lệ để sử dụng. Độ tin cậy sẽ được xác định bằng cách xác nhận tổng số đồng ý với khối lượng bán hàng thực tế trong hồ sơ tài chính. Xác định một quan sát trung bình trong dữ liệu Đôi khi câu hỏi phân tích không phải về nhóm hoặc loại dữ liệu mà thay vào đó là hỏi về mức trung bình trong dữ liệu. Ngoài tần suất và bảng chéo, các biện pháp đo lường vị trí được sử dụng trong phân tích mô tả. Khi đánh giá tính giá trị và độ tin cậy của một phân tích bao gồm các thước đo về vị trí, đảm bảo rằng thước đo chính xác đang được sử dụng. Các thước đo vị trí bao gồm các thước đo trung bình, trung vị và mode thể hiện mức trung bình. độ tuổi hoặc quan sát điển hình trong tập dữ liệu: • Giá trị trung bình: Tổng của tất cả các quan sát trong một tập dữ liệu chia cho tổng số quan sát. • Median: Giá trị ở giữa khi dữ liệu được sắp xếp từ nhỏ nhất đến lớn nhất. • Chế độ: Quan sát xảy ra thường xuyên nhất.**

![ILLUSTRATION 8.17](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.17.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Cả ba thước đo đều là thước đo hợp lệ về vị trí, nhưng trong những điều kiện khác nhau, một số thước đo những xu hướng trung tâm chắc chắn sẽ phù hợp hơn những xu hướng khác. Ví dụ: giá trị trung bình có thể bị ảnh hưởng bởi các giá trị cực trị trong dữ liệu, trong khi giá trị trung bình bị ảnh hưởng bởi không bị ảnh hưởng bởi các loại giá trị này, là những giá trị ngoại lệ. Có hai phương pháp để xác định nếu có các ngoại lệ trong tập dữ liệu:

- Tìm kiếm sự khác biệt lớn giữa giá trị trung bình và trung vị.

- Vẽ biểu đồ dữ liệu để xác định trực quan xem có ngoại lệ hay không. Hãy bắt đầu bằng cách kiểm tra giá trị trung bình và trung vị. Hình minh họa 8.18 cho thấy trạng thái mô tả số liệu thống kê về số lượng bán hàng hàng tháng của Super Scooters. ( Dữ liệu Cách thực hiện 8.2 minh họa cách để tạo các số liệu thống kê này trong Microsoft Excel.) Doanh số bán hàng trung bình hàng tháng là 2.132 và khối lượng bán hàng trung bình hàng tháng là 1.879. Số trung bình lớn hơn nhiều so với số trung vị. Nhưng chúng tôi biết rằng nếu chúng ta đang tìm kiếm vị trí trung tâm của tập dữ liệu thì trung vị sẽ ở ngay trong giữa. Sự khác biệt lớn này là một dấu hiệu tốt cho thấy có những giá trị cực trị trong tập dữ liệu. MINH HỌA 8.19 Sơ đồ phân tán của Super Scooters’ Khối lượng bán hàng 8,421 7.810 0 1.000 22 tháng 8 23 tháng 3 23 tháng 10 24 tháng 4 24 tháng 11 25 tháng 5 25 tháng 12 2.000 3.000 4.000 5.000 6.000 7.000 8.000 9.000 Khối lượng bán hàng Siêu xe tay ga, Inc. Khối lượng bán hàng hàng tháng Độ lệch Nghĩa là trung vị Lỗi chuẩn Độ lệch chuẩn Chế độ Kurtosis Phương sai mẫu Phạm vi 2,73 2.132,39 1.879,00 275,34 1.652,02 #Không áp dụng 8,82 2.729.183,96 8.050,00 Đếm tối thiểu Tổng Tối đa 36:00 371,00 76.766,00 8.421,00 MINH HỌA 8.18 Mô tả Thống kê doanh số bán siêu xe tay ga khối lượng Làm thế nào để Bây giờ hãy thử phương pháp thứ hai. Một biểu đồ phân tán cho thấy mối quan hệ giữa hai số biến cal. Mỗi quan sát trong tập dữ liệu được vẽ dưới dạng một điểm có tọa độ liên quan đến giá trị của hai biến cho quan sát đó. Hình minh họa 8.19 là biểu đồ phân tán về doanh số hàng tháng của Super Scooters từ năm 2023 đến 2025. Mỗi giao dịch mua bán được biểu thị bằng dấu chấm. Hãy chú ý các dấu chấm có nhãn 8,421 và 7,810. Những quan sát này nằm ngoài hầu hết số tiền hàng tháng. Những tháng đó đang tăng lên ý nghĩa. Khi đánh giá các thước đo về vị trí, hãy ghi nhớ tác động tiềm ẩn của các yếu tố ngoại lai đối với kết quả. Nếu bạn chịu trách nhiệm lập ngân sách bán hàng cho Super Scooters thì bạn có thể lựa chọn giữa việc sử dụng khối lượng bán hàng trung bình hoặc trung bình từ năm trước vào ngân sách

![ILLUSTRATION 8.19](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.19.png)

## 8.4  Độ hiệu lực và độ tin cậy được xác định như thế nào trong các phân tích mô tả và chẩn đoán?  21-8

2Hãy nhớ rằng đây là một ví dụ rất đơn giản về việc chuẩn bị ngân sách. Ngân sách bán hàng bao gồm hơn chỉ ước tính số tiền giao dịch bán hàng duy nhất, đặc biệt nếu có nhiều sản phẩm và địa điểm. Tuy nhiên, nguy cơ sử dụng sai biện pháp vẫn là một mối lo ngại chính đáng.

**MINH HỌA 8.20 Ước tính Doanh số bán hàng sử dụng doanh số trung bình so với doanh số trung bình khối lượng Doanh số ước tính dựa trên khối lượng bán hàng trung bình Chênh lệch giữa khối lượng bán hàng ước tính = 3.036 Doanh số ước tính dựa trên khối lượng bán hàng trung bình 2.132 × 12 tháng = 25.584 1.879 × 12 tháng = 22.548 Tóm lại, khi đánh giá tính giá trị và độ tin cậy của một phân tích bao gồm các số đo chắc chắn về vị trí, xác nhận biện pháp chính xác đang được sử dụng. Nếu sử dụng đúng biện pháp thì kết quả là hợp lệ. Trong Hình minh họa 8.20, sử dụng giá trị trung bình thay vì trung vị để ước tính khối lượng bán hàng của bạn đời sẽ không hợp lệ vì sự khác biệt giữa giá trị trung bình và trung vị doanh số bán hàng hàng tháng. Việc sử dụng khối lượng bán hàng trung bình sẽ làm tăng ước tính do các giá trị ngoại lệ khối lượng bán hàng cao hơn trong dữ liệu. Đó không phải là một ước tính ngân sách đáng tin cậy. Đánh giá sự phân phối dữ liệu Loại phân tích mô tả cuối cùng được thảo luận ở đây là các biện pháp phân tán. phân tán đề cập đến mức độ biến đổi của dữ liệu. Dữ liệu có được trải rộng ra hay chúng nhỏ gọn? trong nói cách khác, tất cả các quan sát (điểm dữ liệu) cách nhau bao xa so với giá trị trung bình? Hai nhất Các thước đo độ phân tán được sử dụng rộng rãi là phương sai và độ lệch chuẩn. Độ lệch chuẩn cho thấy mức độ phân tán của dữ liệu so với giá trị trung bình. Nó ở trong cùng đơn vị với giá trị trung bình. Độ lệch chuẩn có thể giúp xác định giá trị và độ tin cậy của một phân tích. Hình minh họa 8.21 hiển thị danh sách thống kê mô tả về doanh số bán hàng của Super Scooters ừm. Độ lệch chuẩn được đánh dấu. cho ngân sách sản xuất năm tới. (Tham khảo Hình minh họa 8.18 để tính giá trị trung bình và trung bình cho số liệu thống kê mô tả của Super Scooters.) Hình minh họa 8.20 tóm tắt hai lựa chọn. Sử dụng giá trị trung bình làm thước đo trung bình độ tuổi của nhu cầu sản xuất bán hàng hàng tháng phóng đại nhu cầu sản xuất.2 Có một sự khác biệt- khoảng 3.036 (13%) giữa hai lựa chọn. Sẽ rất khó để giải thích với sếp của bạn tiếp theo năm tại sao bạn lại giảm 13% so với sản lượng dự kiến!**

**MINH HỌA 8.21 Mô tả Thống kê doanh số bán siêu xe tay ga khối lượng Siêu xe tay ga, Inc. Khối lượng bán hàng hàng tháng Độ lệch Nghĩa là trung bình Lỗi chuẩn Độ lệch chuẩn Chế độ Kurtosis Phương sai mẫu Phạm vi 2,73 2.132,39 1.879,00 275,34 1.652,02 #N/A 8,82 2.729.183,96 8.050,00 Đếm tối thiểu Tổng Tối đa 36:00 371,00 76.766,00 8.421,00 Trong ví dụ này, số lượng bán hàng trung bình hàng tháng là 2.132,39. tiêu chuẩn độ lệch là 1.652,02. Vì vậy, khoảng cách trung bình giữa một lần quan sát (trong trường hợp này là doanh số bán hàng) số tiền ume) và giá trị trung bình là 1.652,02. Độ lệch chuẩn có thể chỉ ra mối quan hệ của các điểm dữ liệu tionship có nghĩa là: • Độ lệch chuẩn thấp cho thấy các điểm dữ liệu có xu hướng gần với giá trị trung bình. • Độ lệch chuẩn cao cho thấy các điểm dữ liệu được trải rộng trên một phạm vi rộng các giá trị.**

![ILLUSTRATION 8.21](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.21.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Số tiền 1.652,02 có vẻ là độ lệch chuẩn cao hay thấp cho doanh số bán hàng? ừm? Xét rằng độ lệch chuẩn là khoảng 77% giá trị trung bình, có vẻ như độ lệch cao. Xem lại biểu đồ phân tán trong Hình minh họa 8.19 để xác định trực quan xem có nhiều quan sát (điểm dữ liệu) cách xa giá trị trung bình 2.132,39. Biểu đồ phân tán hiển thị dữ liệu điểm cao hơn nhiều so với mức trung bình. Kết hợp lại với nhau, phân tích mô tả giúp chúng ta hiểu rõ hơn về dữ liệu cơ bản trong quá trình phân tích. ysis đang được giải thích. Đánh giá tính giá trị và độ tin cậy của các phân tích liên quan đến việc đảm bảo tính chính xác phương pháp trực tràng được sử dụng và dữ liệu là chính xác. Phân phối tần số và bảng chéo có thể giúp nhóm dữ liệu thành các danh mục có ý nghĩa. Các thước đo về vị trí có thể cho thấy mức trung bình quan sát trông giống như hoặc nếu có các ngoại lệ, trong khi các thước đo độ phân tán cho thấy sự phân bố của dữ liệu làm nền tảng cho việc phân tích. ÁP DỤNG TƯ DUY PHIẾU 8.2: Đánh giá độ tin cậy và hiệu lực Có vẻ như bạn không áp dụng các kỹ năng tư duy phản biện khi đánh giá độ tin cậy và giá trị của phân tích mô tả, nhưng bạn đang suy nghĩ chín chắn trước khi bắt đầu:

- Bạn phải xác định lý do đằng sau việc phân tích để quyết định xem đó có phải là một câu hỏi cần thực hiện hay không. được trả lời bằng phân tích mô tả (Mục đích).

- Sau đó, bạn xác định thông tin cần thiết để diễn giải kết quả phân tích. Bạn có cần biết không làm thế nào để giải thích sự phân bố tần số? Bảng chéo? Biện pháp xác định vị trí? Các biện pháp phân tán? Bạn có kiến ​​thức đó (Kiến thức) chưa?

- Bạn có thể áp dụng kinh nghiệm với những diễn giải phân tích trước đây vào bối cảnh hiện tại (Tự suy ngẫm). Phân tích chẩn đoán Nếu mục tiêu của việc phân tích là hiểu tại sao điều gì đó lại xảy ra thì bạn sẽ giải thích các phân tích chẩn đoán. Hình minh họa 8.22 cung cấp một số đối tượng chẩn đoán phổ biến. những ý kiến và phân tích có thể được sử dụng. Mục tiêu Câu hỏi mẫu Phân tích hợp lệ Tìm sự bất thường trong tập dữ liệu. Có giao dịch doanh thu không khác nhau hoặc cao đáng ngờ? biểu đồ phân tán ô hộp Kiểm tra các mối quan hệ trong dữ liệu. Có mối quan hệ nào không giữa bảo trì chi phí và thiết bị giờ? biểu đồ phân tán Hệ số tương quan Xác định các mẫu trong tập dữ liệu. Có bán hàng theo mùa không hình mẫu? Biểu đồ thanh Biểu đồ cột Biểu đồ đường Đường xu hướng MINH HỌA 8.22 Chẩn đoán Mục tiêu, câu hỏi và giá trị Phân tích Tìm điểm bất thường Đánh giá tính hợp lệ và độ tin cậy bao gồm việc xác định bất kỳ sự bất thường tiềm ẩn nào trong dữ liệu. Một sự bất thường là một quan sát trong tập dữ liệu sai lệch so với mức bình thường hoặc dự kiến.

![ILLUSTRATION 8.22](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.22.png)

## 8.4  Hiệu lực và độ tin cậy được xác định như thế nào trong phân tích mô tả và phân tích chẩn đoán?  8-23

Xác định sự bất thường là một thủ tục phân tích chẩn đoán phổ biến. Một sự bất thường có thể có vẻ giống như một ngoại lệ, được thảo luận trong phần phân tích mô tả. Tuy nhiên, có một số sự khác biệt chính:

- Ngoại lệ: Đây là một quan sát hợp lý nằm ở khoảng cách bất thường so với các giá trị khác trong dữ liệu. Ví dụ, tại các cửa hàng bán lẻ doanh số bán hàng trong những ngày nghỉ lễ cao hơn nhiều so với trong mùa hè. Số tiền bán được cao trong tháng 12 có thể là một ngoại lệ, ở chỗ nó rất lớn. cao hơn các tháng khác, nhưng điều đó là hợp lý vì doanh số bán hàng dự kiến sẽ cao hơn vào tháng 12.

- Bất thường: Đây là một quan sát không chính đáng. Những quan sát bất hợp pháp có thể sai xảy ra hoặc những sự việc bất thường mà chúng ta không mong đợi gặp lại. Những quan sát này có thể là những ngoại lệ được xác định là bất hợp pháp, do đó là một sự bất thường. Một ví dụ về điều này là nếu chi phí vật tư cao hơn đáng kể trong một tháng do ghi nhật ký sai. Việc phát hiện những điều bất thường có thể là mục đích của việc phân tích, chẳng hạn như khi tìm kiếm những điều bất thường. liên minh các giao dịch lớn trong một cuộc kiểm toán khi nghi ngờ có gian lận. Tuy nhiên, việc phát hiện sự bất thường cũng có thể là ngoài ý muốn. Hãy nhớ lại rằng Hình minh họa 8.19 đã xác định hai trường hợp ngoại lệ tiềm năng – khối lượng bán hàng của 8.421 và 7.810. Số tiền này lớn hơn nhiều so với số tiền khối lượng hàng tháng khác mà xảy ra trong giai đoạn 2022-2025. Tại sao số lượng bán ra lại cao như vậy? Đây là một ví dụ về phát hiện bất thường Hai điểm này có thể là những quan sát chính đáng (ngoại lệ), hoặc bất hợp pháp (dị thường). Bước tiếp theo trong việc diễn giải là xác định lý do khiến khối lượng giao dịch hàng tháng cao. số lượng và điều tra các bất thường tiềm ẩn khác trong dữ liệu. Đầu tiên, kiểm tra tất cả số tiền trên 1.500 và xác định xem chúng có chính xác không. Nếu đúng thì điều tra lý do tiềm năng cho khối lượng cao. Kiểm tra mối quan hệ dữ liệu Một phần của việc hiểu dữ liệu là biết dữ liệu có liên quan như thế nào. Phân tích tương quan cho thấy mối quan hệ trong dữ liệu bằng cách đo lường mối quan hệ tuyến tính giữa hai biến. Nếu Mục tiêu của việc phân tích là xác định độ mạnh của mối quan hệ giữa các đối tượng quan tâm (các biến), thì phân tích tương quan sẽ phù hợp. Đánh giá giá trị và độ tin cậy của một phân tích tương quan đòi hỏi phải biết cách diễn giải hệ số tương quan. Tương quan tuyến tính được đo bằng hệ số tương quan, cũng biết có Pear- son hệ số tương quan sản phẩm-thời điểm. Số đo này là một giá trị số trong khoảng -1 và +1. Con số tuyệt đối càng cao thì sức mạnh của mối quan hệ càng lớn. Một vị trí hệ số tương quan tive chỉ ra rằng khi một biến tăng thì biến kia cũng tăng. Có một mối quan hệ tích cực giữa doanh số bán kem và nhiệt độ ngoài trời, ví dụ: xin. Khi nhiệt độ tăng, doanh số bán kem cũng có xu hướng tăng. Một mối tương quan tiêu cực là một mối quan hệ nghịch đảo. Khi một biến tăng lên thì biến kia giảm và ngược lại. Hãy xem xét việc bán súp. Có mối quan hệ tiêu cực giữa súp bán hàng và nhiệt độ. Khi nhiệt độ giảm, doanh số bán súp tăng lên. Minh họa 8.23 là hướng dẫn diễn giải giá trị của hệ số tương quan. MINH HỌA 8.23

Giải thích mối tương quan hệ số −0,70 −0,50 −0,30 Mối quan hệ tuyến tính tiêu cực vừa phải Mối quan hệ tuyến tính tiêu cực yếu 0 Không có mối quan hệ tuyến tính Chính xác −1 +0,50 +0,70 Chính xác +1 +0,30 Mối quan hệ tuyến tính phủ định hoàn hảo Mối quan hệ tuyến tính tiêu cực mạnh mẽ Mối quan hệ tuyến tính tích cực mạnh mẽ Một mối quan hệ tuyến tính tích cực hoàn hảo Mối quan hệ tuyến tính tích cực yếu Một mối quan hệ tuyến tính tích cực vừa phải Phiên dịch Tương quan r

![ILLUSTRATION 8.23](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.23.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Tương quan là thước đo hợp lệ để kiểm tra mối quan hệ tuyến tính giữa các biến trong dữ liệu và việc giải thích mối tương quan phải dựa trên hệ số tương quan. Phân tích tương quan là đáng tin cậy nếu các hệ số tương quan nhất quán và chính xác liên quan đến dữ liệu đang được phân tích. Trong ví dụ về kem và súp, mối tương quan là hợp lệ vì chúng tôi đang kiểm tra mối tương quan logic bằng cách sử dụng hệ số tương quan. Đó là đáng tin cậy nếu chúng ta tin rằng các hệ số tương quan là nhất quán và chính xác. Phân tích tương quan có thể được thực hiện bằng cách sử dụng dữ liệu Super Scooters:

- Ban quản lý Super Scooters đang xem xét các chi phí tiếp thị có thể thay đổi và muốn để biết liệu có mối quan hệ giữa số tiền chi cho hoạt động tiếp thị đa dạng hay không (chiết khấu dành cho đại lý mua sản phẩm Super Scooters) và bán hàng khối lượng.

- Ban quản lý lo ngại rằng họ đã chi 1,1 triệu USD cho hoạt động tiếp thị đa dạng vào năm 2024 và họ không chắc liệu chi tiêu đó có làm tăng doanh số bán hàng hay không. Hình minh họa 8.24 là bảng tổng hợp các hệ số tương quan về tổng doanh thu, doanh số bán hàng ume, và chi phí tiếp thị thay đổi. Hệ số tương quan giữa tiếp thị biến đổi và tổng doanh thu là 0,9650. Người phiên dịch- của con số đó là có mối tương quan tích cực mạnh mẽ giữa tổng doanh thu và biến chi phí tiếp thị. Khi chi phí tiếp thị biến đổi tăng lên, tổng doanh thu cũng tăng theo. Ngoài ra còn có một sức mạnh mối tương quan giữa khối lượng bán hàng và tiếp thị biến đổi với hệ số tương quan là 0,77410. Mặc dù chúng tôi không thể chứng minh được mối quan hệ nhân quả nhưng chúng tôi có thể nói rằng dường như có mối tương quan tích cực mạnh mẽ giữa số tiền chi cho tiếp thị đa dạng và cả khối lượng bán hàng và tổng doanh thu. Xác định mẫu Phân tích xu hướng là một công cụ thống kê sử dụng dữ liệu lịch sử để xác định các mẫu. Nó có thể giải thích tại sao điều gì đó đang xảy ra. Đường xu hướng cho biết diễn biến chung hoặc xu hướng của dữ liệu và được được tạo bằng cách sử dụng các điểm dữ liệu lịch sử để ước tính một đường.3 Việc kiểm tra các xu hướng giúp phát hiện các mẫu và các mối quan hệ, có thể xác định các cơ hội hoặc mối đe dọa tiềm ẩn đối với doanh nghiệp. Cách tốt nhất để xác định xu hướng là vẽ biểu đồ dữ liệu theo thời gian. Hình minh họa 8.25 là một phân tích xu hướng chi phí nguyên vật liệu và doanh số bán hàng của Super Scooters trong những năm 2023–2025. MINH HỌA 8.24

Tóm tắt hệ số tương quan dành cho siêu xe tay ga Tương quan hệ số 0,9650 0,7749 Tổng doanh thu Khối lượng bán hàng Phân tích 3Xu hướng cũng có thể được sử dụng như một phương pháp phân tích dự đoán.

**MINH HỌA 8.25 Phân tích xu hướng chi phí nguyên vật liệu và doanh số bán hàng của siêu xe tay ga bán hàng khối lượng $260K $240K $220K $200K $180K $160K $140K $120K $100K $80K $60K $40K $20K $0K 0 200 400 600 800 1.000 1.200 1.400 1.600 1.800 2.000 2.200 2.400 2.600 2.800 3.000 3.200 3.400 3.600 Tháng ba. 2023 Tháng Sáu. 2023 Tháng 9 2023 Tháng mười hai 2023 Tháng ba. 2024 Tháng Sáu. 2024 Tháng 9 2024 Tháng mười hai 2024 Tháng mười hai 2025 Tháng ba. 2025 Tháng Sáu. 2025 Tháng 9 2025 Chi phí vật liệu Khối lượng bán hàng Vật liệu Tháng mười hai 2022 Tháng và Năm Xu hướng chi phí vật liệu và khối lượng bán hàng của siêu xe tay ga**

![ILLUSTRATION 8.25](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.25.png)

## 8.4  Độ hiệu lực và độ tin cậy được xác định như thế nào trong các phân tích mô tả và chẩn đoán?  8-25

ÁP DỤNG TƯ duy phản biện 8.3: Diễn giải Phân tích chẩn đoán Khi giải thích lý do tại sao điều gì đó xảy ra, hãy sử dụng phân tích chẩn đoán:

- Kết quả phân tích chẩn đoán có thể được sử dụng để đưa ra những giải thích khác. Ví dụ như việc bán hàng xu hướng dường như xen kẽ với mức tăng và sau đó giảm vào quý tiếp theo. Có lẽ doanh số bán hàng các chương trình khuyến mãi đang thúc đẩy mô hình này (Các lựa chọn thay thế).

- Tìm kiếm các mối đe dọa tiềm ẩn đối với phân tích, chẳng hạn như các điểm bất thường. Có bất kỳ quan sát nào trong phân tích xu hướng bất thường hoặc bất ngờ (Rủi ro)?

- Xem xét những gì cần thiết để hiểu các phân tích, chẳng hạn như phân tích tương quan và phân tích xu hướng phân tích (Kiến thức). Áp dụng nó 8.4 Giải thích một Biểu đồ phân tán cho Ngoại lệ Dữ liệu Kiểm toán Roberto Jimenez là giám đốc hoạt động của DHI. Anh ấy đã hỏi người liên bộ phận kiểm toán cuối cùng để giúp anh ta thực hiện phân tích số giờ dọn phòng. Roberto muốn để biết các vị trí khác nhau đang hoạt động hiệu quả như thế nào. Bạn đã được cung cấp một biểu đồ phân tán hiển thị số giờ dọn phòng đã làm và số phòng thuê theo vị trí khách sạn. các đường xuyên qua biểu đồ là đường xu hướng biểu thị mối quan hệ tuyến tính giữa số giờ làm việc và thuê phòng. Lưu ý rằng những con số được liệt kê bên dưới dấu chấm là số vị trí khách sạn. Tất cả dữ liệu trong biểu đồ phân tán là những quan sát hợp lệ. 1. Xem lại biểu đồ phân tán, xác định các giá trị ngoại lệ tiềm năng và giải thích lý do tại sao bạn xác định chúng là các giá trị ngoại lệ. 2. Đề xuất cách giải quyết các trường hợp ngoại lệ. Phân tích xu hướng được chuẩn bị bằng phần mềm trực quan hóa dữ liệu. Phân tích xu hướng cũng có thể được chuẩn bị trong Microsoft Excel bằng cách sử dụng công cụ đường xu hướng có sẵn khi dữ liệu được được biểu đồ. Super Scooters đang kiểm tra lý do tại sao chi phí nguyên liệu ngày càng tăng. Việc phân tích ở Hình minh họa 8.25 cho thấy khối lượng bán hàng và chi phí nguyên vật liệu thay đổi theo cùng một mô hình năm và cả hai đều tăng:

- Điều hợp lý là khối lượng bán hàng tăng sẽ dẫn đến chi phí nguyên vật liệu tăng. Có sim- ilar đỉnh và thung lũng trong dòng. Đây là một dấu hiệu cho thấy có thể có một mùa mẫu để bán hàng.

- Các đường xu hướng trong phân tích (các đường thẳng nét đứt) cho thấy rằng mặc dù cả hai đường xu hướng dây chuyền ngày càng tăng, chi phí nguyên vật liệu ngày càng tăng với tốc độ cao hơn. Sau khi xem xét phân tích này, chúng ta có thể kết luận rằng chi phí nguyên vật liệu đang tăng lên do tăng khối lượng bán hàng. Việc phân tích khối lượng bán hàng và chi phí nguyên vật liệu này có giá trị vì nó sử dụng phương pháp để hiểu mối quan hệ giữa xu hướng bán hàng và chi phí. Các mea- Những điều chắc chắn được sử dụng trong phân tích là chính xác và nhất quán, đồng thời dữ liệu đáng tin cậy và xứng đáng nên phân tích cũng đáng tin cậy. Tuy nhiên, hiểu được tại sao chi phí nguyên vật liệu lại tăng với tốc độ nhanh hơn doanh số bán hàng sẽ yêu cầu điều tra nhiều hơn.

![Apply It 8.4](../TaiLieu/textbookForPractice/Figures/Ch_08/Apply%20It%208.4.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu GIẢI PHÁP

1. Có mối quan hệ tích cực giữa số giờ dọn phòng và giá thuê phòng. Như số- Số lượng phòng thuê tăng lên và số giờ dọn phòng cũng tăng theo. Điều này có ý nghĩa vì phòng đã thuê phải được dọn dẹp.

Có một số quan sát vị trí khách sạn nằm xa đường xu hướng hơn các quan sát khác. quan sát:

- Vị trí 30 có số giờ dọn phòng cao nhất nhưng không phải là số phòng cao nhất cho thuê.

- Địa điểm 105 có số giờ dọn phòng thấp nhưng số lượng phòng cho thuê lại cao. 2. Khuyến nghị:

- Điều tra sâu hơn tại Địa điểm 30 để xác định nguyên nhân quản lý kém hiệu quả giờ.

- Điều tra sâu hơn về Địa điểm 105 để xác định tính hiệu quả có thể áp dụng cho ít hơn những địa điểm hiệu quả. 0 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 Số giờ đã làm việc, dọn phòng (Tính bằng nghìn) Giá thuê phòng (Tính theo nghìn) Giờ dọn phòng đã làm việc và số phòng được thuê theo địa điểm 33 105 11 29 52 18 1 22 87 15 12 25 16 37 2 3 17 7 31 21 56 9 70 5 10 97 93 6 32 39 40 30 59 43

## 8.5  Độ giá trị và độ tin cậy được đánh giá như thế nào trong các phân tích dự đoán và phân tích theo quy định?  27-8

## 8.5  Hiệu lực và độ tin cậy như thế nào

Đánh giá trong dự đoán và quy định Phân tích? MỤC TIÊU BÀI HỌC ➎ Đánh giá tính hợp lệ và độ tin cậy của kết quả phân tích dữ liệu dự đoán và quy định. Như bạn đã biết, hai loại phân tích còn lại là phân tích dự đoán và phân tích theo quy định. Phần tiếp theo đề cập đến các loại phân tích trong những lĩnh vực này mà bạn có thể gặp phải trong sự nghiệp của bạn và cách xác định xem các phân tích có đáng tin cậy và hợp lệ hay không. Phân tích dự đoán Có nhiều loại phân tích dự đoán, nhưng chúng đều có mục tiêu là dự đoán một kết quả trong tương lai. Trong nghề kế toán, phân tích dự báo phổ biến nhất là phân tích tuyến tính. hồi quy, là một công cụ để xây dựng các mô hình toán học và thống kê nhằm giải thích các mối quan hệ giữa một biến phụ thuộc và một hoặc nhiều biến độc lập. Kể cả nếu bạn không chuẩn bị các mô hình hồi quy tuyến tính trong sự nghiệp của mình, việc hiểu về hồi quy có thể giúp ích hiểu các mô hình dự đoán mà bạn gặp phải. Mô hình hóa mối quan hệ Phân tích dự đoán xây dựng mô hình để giúp dự đoán hoặc hiểu rõ hơn về một hiện tượng. Xây dựng- việc xây dựng một mô hình dự đoán chi phí cung ứng sẽ giúp hiểu được các yếu tố ảnh hưởng chi phí vật tư. Xây dựng mô hình này yêu cầu xác định các biến sẽ được đưa vào trong đó. Khi mô hình hồi quy hoàn tất, làm sao chúng ta biết liệu nó có hợp lệ hay không? Hãy nhớ rằng một phân tích có giá trị nếu nó đo lường được những gì cần đo lường và nếu nó cũng phản ánh được thực tế. Hãy xem xét các biến trong mô hình – chúng có hợp lý dựa trên mục tiêu của mô hình không? Ví dụ: khi đánh giá một mô hình kiểm tra tác động của nhiệt độ đến lợi ích doanh số bán áo khoác, sẽ hợp lý nếu cả nhiệt độ và giá trung bình của áo khoác đều được đưa vào mô hình. Mô hình cũng có thể bao gồm cả tuyết rơi. Tuy nhiên, nếu mô hình bao gồm một biến số không có ý nghĩa, chẳng hạn như số lượng đồ bơi được bán, mẫu sẽ không được hợp lệ. Nó sẽ không đo lường những gì nó dự định đo lường. Bước tiếp theo là xác nhận mô hình là đáng tin cậy. Hãy nhớ lại rằng độ tin cậy có nghĩa là các biện pháp được sử dụng trong phân tích là chính xác và nhất quán và dữ liệu đáng tin cậy và đáng tin cậy. May mắn thay, có rất nhiều biện pháp thống kê trong phân tích hồi quy có thể được kiểm tra để xác định độ tin cậy. Các chương trước đã mô tả cách xây dựng hồi quy mô hình hóa và giải thích kết quả hồi quy. Ở đây, chúng tôi tập trung vào số liệu thống kê quan trọng và kết quả đầu ra giúp đánh giá và giải thích đầu ra của mô hình hồi quy. Hãy nhớ rằng nếu mô hình không hợp lệ, thì việc nó có đáng tin cậy hay không cũng không thành vấn đề. Một thước đo chính xác và nhất quán của mô hình không có nghĩa là mô hình đại diện cho thực tế. Vì vậy, bước đầu tiên để xác định xem mô hình có thay đổi hay không khả năng logic là quan trọng. Độ tin cậy của mô hình hồi quy Đánh giá độ tin cậy của phân tích hồi quy bằng cách xem xét số liệu thống kê của mô hình. Minh họa

## 8.26 là đầu ra của mô hình hồi quy bội để dự đoán chi phí của bộ phận mua hàng

dành cho siêu xe tay ga. Lưu ý rằng chi phí bộ phận mua hàng là những chi phí phát sinh

Chương 8 Diễn giải kết quả phân tích dữ liệu bởi bộ phận mua hàng để xử lý các đơn đặt hàng (bảng lương, hành chính và vượt mức) đầu). Những chi phí này không giống như chi phí mua hàng. Mô hình này dựa trên lịch sử dữ liệu, được thu thập từ mỗi địa điểm sản xuất, về các biến được cho là có ảnh hưởng đến tổng theo đuổi chi phí của bộ phận.

**MINH HỌA 8.27 Hồi quy Thống kê cho phòng mua hàng Chi phí Thống kê hồi quy Nhiều R Hình vuông R đã điều chỉnh R vuông Quan sát Lỗi chuẩn 0.892897453 0.777957848 0.797265861 24 1.337.156824 Trong mô hình này, tổng chi phí của bộ phận mua hàng là biến phụ thuộc và doanh thu khối lượng và số lượng đơn đặt hàng được xử lý là các biến độc lập. Phép hồi quy trong Hình minh họa 8.26 được thực hiện bằng Microsoft Excel. Tóm tắt Đầu ra được chia thành ba phần. Đầu tiên là thống kê hồi quy, là số liệu thống kê các biện pháp được sử dụng để đánh giá mô hình. Hình minh họa 8.27 cho thấy thống kê hồi quy từ**

**Minh họa 8.26.**

**MINH HỌA 8.26 Mô hình hồi quy chi phí bộ phận mua siêu xe tay ga Nhiều R R vuông Hình vuông R đã điều chỉnh Lỗi chuẩn Quan sát ANOVA 0.892897453 0.797265861 0.777957848 1.337.156824 24 df SS MS F 147659116.6 37547755.8 Hồi quy dư Tổng cộng 2 21 23 185206872.4 73829558.29 1787988.371 41.29196782 5.2812E-08 877.1183137 31.32217805 Đánh chặn Số đơn đặt hàng Khối lượng bán hàng −994.5719771 180.0127037 1.191401172 0.351035522 3.393961854 −1.133908575 5.747132382 0,002736568 1.05165E-05 0.269611889 Ý nghĩa F Hệ số lỗi chuẩn t Thống kê giá trị P TÓM TẮT ĐẦU RA Hồi quy chi phí bộ phận mua siêu xe tay ga Thống kê hồi quy Tất cả số liệu thống kê hồi quy cung cấp cái nhìn sâu sắc về mô hình hồi quy. Mỗi thống kê này các vấn đề cơ bản đã được đề cập trong chương dành cho các kỹ năng phân tích dữ liệu cơ bản. Dưới đây là một số số liệu thống kê quan trọng nhất để đánh giá độ tin cậy của mô hình: • Bình phương R đã điều chỉnh (R2): Giải thích mức độ phù hợp của đường hồi quy với dữ liệu. các R2 được điều chỉnh là một thống kê điều chỉnh giá trị của R2 bằng cách kết hợp cỡ mẫu và số lượng biến độc lập. Nói chung, sử dụng R2 đã điều chỉnh để đánh giá mô hình hồi quy bội. R2 càng gần 1 thì độ phù hợp của hồi quy càng tốt dòng vào dữ liệu. • Sai số chuẩn: Trong kết quả hồi quy của Excel, sai số chuẩn biểu thị độ biến thiên của các giá trị biến phụ thuộc được quan sát từ các giá trị được mô hình dự đoán. Nói cách khác, nó so sánh biến phụ thuộc thực tế với giá trị dự đoán mà mô hình cung cấp. Nếu dữ liệu được nhóm gần với đường hồi quy thì tiêu chuẩn lỗi sẽ nhỏ. Nếu dữ liệu phân tán nhiều hơn thì sai số chuẩn sẽ lớn hơn. A sai số chuẩn nhỏ là tối ưu.**

![ILLUSTRATION 8.27](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.27.png)

## 8.5  Độ giá trị và độ tin cậy được đánh giá như thế nào trong các phân tích dự đoán và phân tích theo quy định?  29-8

Hình minh họa 8.27 thể hiện thống kê hồi quy cho Hình minh họa 8.26: • Bình phương R được điều chỉnh trong Hình minh họa 8.27 là 0,778. Chúng tôi giải thích rằng 77,8% tổng chi phí có thể được giải thích bằng số lượng đơn đặt hàng được xử lý và bằng khối lượng bán hàng. • Sai số chuẩn trong mô hình này là $1.337,16. Để xác định xem đây là một lớn hay một sai số chuẩn nhỏ, hãy so sánh nó với độ lệch chuẩn của biến phụ thuộc biến. Trong ví dụ này, so sánh sai số chuẩn với độ lệch chuẩn trong tổng chi phí. Hình minh họa 8.28 cung cấp giá trị trung bình và độ lệch chuẩn cho tổng chi phí. • Độ lệch chuẩn của $2.837,69 cao hơn sai số chuẩn của $1.337,16 trong mô hình hồi quy. Sai số chuẩn trong mô hình này sẽ được coi là một số- nhỏ gì. Phần tiếp theo của đầu ra tóm tắt hồi quy là đầu ra phân tích phương sai (ANOVA). Hình minh họa 8.29 là phần ANOVA từ mô hình hồi quy. ANOVA là một thử nghiệm cho Ý nghĩa của toàn bộ mô hình:

- Trong một hồi quy tuyến tính bội như thế này, mức ý nghĩa là phép kiểm tra xem liệu hồi quy có mô hình tốt hơn mô hình không có biến độc lập. Nói cách khác, là mô hình tốt hơn là không có mô hình nào cả?

- Nói chung, một mô hình được coi là có ý nghĩa nếu thống kê F (Ý nghĩa F trong hình minh họa 8,29) nhỏ hơn 0,05. MINH HỌA 8.28 Siêu Phòng thu mua xe tay ga Chi phí Mua siêu xe tay ga Chi phí bộ phận 2022 – 2024 Nghĩa là Độ lệch chuẩn $ 3,725,30 $ 2,837,69 MINH HỌA 8.29 ANOVA Thống kê hồi quy cho Chi phí bộ phận mua hàng ANOVA Chi phí của bộ phận mua hàng Kết quả ANOVA dư Hồi quy Tổng cộng df 21 2 23 SS 37547755.8 147659116.6 185206872.4 MS 1787988.371 73829558.29 F 41.29197 Ý nghĩa F 5.2812E-08 Vậy mô hình có quan trọng không? ANOVA trong Hình minh họa 8.29 có Ý nghĩa F là 5.2812E-08. Ký hiệu “E-08” sau 5.2812 thể hiện ký hiệu khoa học, còn được gọi là ký hiệu hàm mũ. 5.28.12E-08 giống với 0,000000052812. Đây là một con số dưới đây 0,05 nên mô hình có ý nghĩa. Nói cách khác, các biến độc lập có thể giải thích một số sự thay đổi của tổng chi phí, vì vậy tốt hơn là không có mô hình nào cả. Phần cuối cùng của kết quả tóm tắt hồi quy cung cấp thông tin để tạo ra phương trình dự đoán biến phụ thuộc. Nếu điều chỉnh R bình phương và sai số chuẩn có thể chấp nhận được và mô hình có ý nghĩa thì chúng ta có thể diễn giải phương trình của mô hình. Điểm chặn và các hệ số của mô hình thể hiện phương trình của đường thẳng tốt nhất phù hợp với dữ liệu. Thống kê quan trọng cần phân tích trong phần này là giá trị p cho mỗi thông số độc lập. biến số vết lõm. Giống như thống kê F, giá trị p cung cấp một phép thử về ý nghĩa. Đó là một bài kiểm tra để liệu biến độc lập có cải thiện khả năng của mô hình trong việc dự đoán biến phụ thuộc hay không biến. Giá trị p từ 0,05 trở xuống được coi là đáng kể. Hãy sử dụng kết quả đầu ra trong Hình minh họa 8.30 để xác định mô hình dự đoán cho Super Scoot- tổng chi phí của bộ phận mua hàng của người đó và sau đó giải thích các hệ số. Lưu ý rằng giá trị p cho tất cả các biến độc lập đáp ứng được kiểm định nhỏ hơn 0,05 và có- đáng kể trước đây.

![ILLUSTRATION 8.30](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.30.png)

CHƯƠNG 8 Diễn giải kết quả phân tích dữ liệu Mô hình dự đoán sẽ bằng điểm chặn, cộng với các hệ số độc lập biến dent, nhân với giá trị dự đoán cho các biến đó. Dựa trên hồi quy mô hình ở Hình minh họa 8.30, phương trình dự đoán tổng chi phí bộ phận mua hàng là: ($994,57) + $180,01 (số lượng đơn đặt hàng) + $1,19 (khối lượng bán hàng) Hình minh họa 8.31 là cách tính tổng chi phí dự kiến nếu 12 đơn đặt hàng được thực hiện ngừng hoạt động và 2.200 xe tay ga được bán. ÁP DỤNG TƯ duy phê phán 8.4: Diễn giải dự đoán Phân tích Nếu phân tích được diễn giải dự đoán một kết quả trong tương lai thì bạn sẽ diễn giải trước phân tích định tính:

- Trong ví dụ về chi phí bộ phận mua hàng của Super Scooters, mục đích của mô hình là hiểu rõ hơn và dự đoán chi phí của bộ phận (Mục đích).

- Việc đưa ra dự đoán này đòi hỏi phải hiểu cách diễn giải phân tích hồi quy (Kiến thức). Số đơn đặt hàng Đánh chặn Khối lượng bán hàng người mẫu hệ số Phòng mua hàng Chi phí dự kiến $180,01 $ (994,57) $1,19 Biến Giá trị 12 1 2.200 3.786,66 USD Dự đoán 2.160,15 USD $ (994,57) 2.621,08 USD MINH HỌA 8.31 Dự đoán Ví dụ mẫu Cộng tích của từng hệ số biến độc lập và giá trị dự đoán của từng biến để ngăn chặn dự đoán tổng chi phí bộ phận mua hàng là 3.786,66 USD trong năm. Mô hình có thể được hiểu như thế này:

- Phần chặn: Phần chặn không có ý nghĩa thực tế. Đó là kết quả của mô hình đại diện cho giá trị trung bình của phản hồi khi tất cả các biến độc lập đều bằng 0. Nó là nơi hàm phương trình đi qua trục y.

- Số lượng Đơn đặt hàng: Mỗi đơn đặt hàng cộng thêm $180,01 vào tổng chi phí.

- Doanh số bán hàng: Với mỗi chiếc xe tay ga được bán thêm, chi phí bộ phận mua hàng sẽ tăng thêm $1,19. Sử dụng mô hình như trong Hình minh họa 8.31 giúp doanh nghiệp dự đoán kết quả trong tương lai. các kết hợp việc đánh giá các biến có trong mô hình để xem liệu chúng có ý nghĩa và thì việc đánh giá số liệu thống kê của mô hình hồi quy sẽ giúp xác định xem mô hình có hợp lệ hay không và đáng tin cậy. MINH HỌA 8.30 Hồi quy Ví dụ mẫu Số đơn đặt hàng Đánh chặn Khối lượng bán hàng hệ số 180.0127 −994.572 1.1914012 Lỗi chuẩn 31.32217805 877.1183137 0.351035522 3.393961854 t Thống kê 5.747132382 0,002737 1.05E-05 −1.133908575 giá trị P 0,269612 Mô hình hồi quy phòng mua hàng Phân tích theo quy định Phân tích theo quy định quy định những gì sẽ xảy ra để đạt được kết quả mong muốn. com nhất Phân tích theo quy định trong kế toán là các mô hình phân tích giả định và tối ưu hóa. các

![ILLUSTRATION 8.31](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.31.png)

## 8.5  Độ giá trị và độ tin cậy được đánh giá như thế nào trong các phân tích dự đoán và phân tích theo quy định?  8-31

các quy tắc tương tự áp dụng cho các phương pháp phân tích khác cũng được áp dụng ở đây. Phân tích phải hợp lệ và đáng tin cậy. Vì mô hình quy định quy định hành động nên điều quan trọng là phải xác minh rằng đầu vào và kết quả đầu ra của mô hình là hợp lệ và đáng tin cậy để tránh đưa ra các quyết định kinh doanh sai lầm. Một mô hình bảng tính đánh giá những thay đổi về giá trị và giả định ảnh hưởng như thế nào đến kết quả được gọi là phân tích what-if. Phân tích giả định là một cách dễ dàng để thay đổi giá trị trong bảng tính và tính toán lại kết quả đầu ra. Các công cụ Excel thường được sử dụng để phân tích điều gì xảy ra nếu bao gồm Trình quản lý Kịch bản và Tìm kiếm mục tiêu. (Các mô hình tối ưu hóa được thảo luận trong chương về động lực phân tích dữ liệu và mục tiêu.) Bất kể sử dụng công cụ nào, việc đánh giá tính hợp lệ và độ tin cậy của đầu ra mô hình là như nhau:

- Hiểu mô hình đang giải quyết vấn đề gì.

- Xác định xem mô hình có đo lường được những gì nó cần đo lường hay không và trên thực tế, liệu nó có đo lường được không đại diện cho mục tiêu (tính hợp lệ).

- Xem xét các thước đo mô hình để xác nhận tính chính xác và nhất quán (độ tin cậy). Phân tích What-If: Trình quản lý kịch bản Hãy xem xét phân tích kịch bản và đánh giá tính hợp lệ và độ tin cậy. Một điệu nhảy quốc tế công ty Ballet Nuevo đang biểu diễn ở Atlanta, Georgia. Họ có ba buổi biểu diễn đã lên lịch và đang xác định xem họ có nên thêm phần thứ tư hay không. Minh họa 8.32 cung cấp một tổng mô hình mary. MINH HỌA 8.32 Mô hình tài chính biểu diễn múa ba lê ngoại hối 1 B A C Trang 1 2 3 4 5 6 7 8 9 10 11 12 13 Ballet Nuevo-Phân tích kịch bản biểu diễn bổ sung Phí rạp hát Giá vé Doanh số bán vé dự kiến Chi phí nhượng bộ trung bình mỗi người Lợi nhuận Doanh thu nhượng quyền Doanh thu vé % lợi nhuận nhượng quyền Tỷ lệ lợi nhuận 18.000 USD $ 31.250,00 $ 113.250,00 125.000 USD $ 50,00 2.500 $ 25,00 50% 80% Tự động Lưu Oﬀ mỗi người Dự kiến doanh số bán vé và chi tiêu ưu đãi (thức ăn và đồ uống) bởi người giữ vé Phí rạp hát, dựa trên về doanh thu bán vé, là chi phí buộc tội công ty múa ba lê từ nhà hát. Càng cao việc bán vé, các giảm phí rạp hát Rạp chiếu phim mất 20% về giá vé và 50% giá trị chiết khấu mọi người Ballet Nuevo tin rằng có ba tình huống có thể xảy ra, được thể hiện trong Hình minh họa 8.33. Doanh số bán vé dự kiến Nhượng bộ chi tiêu 2.500 $ 25,00 18.000 USD 4.500 $40,00 10.000 USD 1.500 $10,00 $ 25.000,00 Phí rạp hát Có khả năng Mô hình phân tích kịch bản Ballet Nuevo lạc quan bi quan MINH HỌA 8.33 Buổi biểu diễn Ballet Nuevo kịch bản Phân tích kịch bản được thực hiện bằng Trình quản lý kịch bản trong Microsoft Excel. Cảnh- nario summary hiển thị kết quả khi các ô B3, B4, B5 (Minh họa 8.32) được đổi thành các giá trị được hiển thị trong Hình minh họa 8.33.

![ILLUSTRATION 8.33](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.33.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu $B$3 Kết quả phân tích kịch bản Ballet Nuevo $B$4 $B$5 $ 25,00 18.000 USD $B$13 $ 113.250,00 $40,00 10.000 USD 260.000 USD $10,00 $ 25.000,00 $ 42.500,00 $ 25,00 18.000 USD $ 113.250,00 Ô kết quả Thay đổi ô 2.500 4.500 1.500 2.500 Giá trị hiện tại Tóm tắt kịch bản lạc quan bi quan Có khả năng

**MINH HỌA 8.34 Phân tích kịch bản Ballet Nuevo**

**MINH HỌA 8.35 Giá vé và lợi nhuận mục tiêu – Tìm kiếm mục tiêu ngoại hối 1 B A C D C Trang 1 2 3 4 5 6 7 8 9 10 11 12 13 Ballet Nuevo ‒ Tìm kiếm mục tiêu lợi nhuận Doanh số bán vé dự kiến Chi phí nhượng bộ trung bình Phí rạp hát Doanh thu nhượng quyền Lợi nhuận Doanh thu vé Giá vé % lợi nhuận nhượng quyền Tỷ lệ lợi nhuận 2.500 mọi người Mỗi người Mỗi người $ 25,00 18.000 USD 125.000 USD $ 31.250,00 $ 113.250,00 $ 50,00 50% 80% Tự động Lưu Oﬀ được rồi Hủy bỏ Tìm kiếm mục tiêu Đặt ô: $B$13 Để giá trị: 150000 Bằng cách thay đổi ô: $B$6 ? Cách giải thích của phân tích này là ngay cả trong kịch bản bi quan Ballet Nuevo sẽ kiếm được lợi nhuận trên một hiệu suất bổ sung. Làm thế nào để chúng ta biết phân tích này là hợp lệ và đáng tin cậy? Ballet Nuevo muốn đánh giá sự khác biệt- các kịch bản bán vé và ưu đãi để xác định xem liệu chúng có nên bổ sung thêm một buổi biểu diễn hay không. Phân tích kịch bản là một phương pháp hợp lệ để sử dụng cho loại phân tích này và mô hình này đại diện cho ba những khả năng thực tế. Về độ tin cậy của mô hình, điều đó có thể được xác nhận bằng cách xác minh lợi nhuận tính toán là chính xác và các giả định là thực tế (giá vé, mua hàng giảm giá, và chi phí rạp hát). Nếu dữ liệu đầu vào của mô hình chính xác và nhất quán thì mô hình đó đáng tin cậy. Phân tích What-If: Tìm kiếm mục tiêu Một công cụ khác để thực hiện phân tích giả định là Goal Seek: • Tìm kiếm mục tiêu được sử dụng nếu kết quả mong muốn đã được biết nhưng giá trị đầu vào để đạt được kết quả đó kết quả là không. • Mục tiêu Tìm kiếm bị hạn chế vì nó chỉ có thể sử dụng một biến đầu vào. Nếu việc phân tích được thực hiện theo được hình thành đòi hỏi nhiều hơn một biến để thay đổi, sau đó một mô hình tối ưu hóa sử dụng Excel Solver sẽ là cần thiết. Trong ví dụ trước, Ballet Nuevo muốn phân tích so sánh các loại vé khác nhau và kịch bản bán hàng nhượng quyền để xác định xem họ có nên thêm một buổi biểu diễn hay không. Điều gì sẽ xảy ra nếu một phần bổ sung buổi biểu diễn không thể thực hiện được do rạp hát còn trống, và thay vào đó, Ballet Nuevo phải xem xét làm thế nào để đặt giá vé để đạt được lợi nhuận mục tiêu cụ thể? • Ballet Nuevo đã xác định họ cần lợi nhuận 150.000 USD từ buổi biểu diễn của mình. • Hiện tại giá vé là $50 và họ dự đoán sẽ có 2.500 vé được bán dựa trên số liệu cuối cùng buổi biểu diễn của năm Hình minh họa 8.35 hiển thị thông tin tài chính của Ballet Nuevo và hộp Goal Seek xuất hiện sau khi nhấp vào tab Dữ liệu trong Excel và chọn Phân tích What-If và Tìm kiếm mục tiêu. Kết quả phân tích được thể hiện ở Hình minh họa 8.34.**

![ILLUSTRATION 8.35](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.35.png)

## 8.5  Độ giá trị và độ tin cậy được đánh giá như thế nào trong các phân tích dự đoán và phân tích theo quy định?  8-33

- Ô Set thể hiện phép tính lợi nhuận tại ô B13 trong bảng tính Excel.

- Hãy chú ý số tiền lãi hiện tại là $113,250. Lợi nhuận mong muốn là 150.000 USD, do đó giá trị đó đã được nhập vào hộp giá trị To.

- Biến đang được thao tác là giá vé, do đó ô tham chiếu giá vé (B6) đã được nhập vào hộp Bằng cách thay đổi ô. Sau khi người dùng nhấn OK, Excel sẽ tính giá vé cần thiết để đáp ứng lợi nhuận mục tiêu 150.000 USD. Hình minh họa 8.36 là giải pháp được tạo ra bởi Excel. Để đạt được mục tiêu lợi nhuận với giá 150.000 USD, Ballet Nuevo phải tính phí 68,38 USD mỗi vé. Để đánh giá độ tin cậy và giá trị của mô hình tìm kiếm mục tiêu, hãy xác định xem mô hình đó có phù hợp không? đảm bảo những gì nó cần đo lường (độ tin cậy) và liệu nó có đại diện cho thực tế của câu hỏi hay không ý nghĩa/mục tiêu (tính hợp lệ):

- Trong mô hình này, xác nhận việc tính toán lợi nhuận là chính xác.

- Ngoài ra, hãy xác định xem mô hình có trả lời được câu hỏi Ballet Nuevo giá bao nhiêu không nên tính phí trên mỗi vé để đạt được lợi nhuận 150.000 USD và nếu vé đề xuất của người mẫu giá là thực tế. Nếu 68,38 USD là không thực tế cho một vé xem buổi biểu diễn thì Ballet Nuevo phải xem xét những cách khác để đạt được mục tiêu lợi nhuận. MINH HỌA 8.36 Giá vé và Lợi nhuận mục tiêu – Tìm kiếm mục tiêu Giải pháp ngoại hối 1 B A C Trang 1 2 3 4 5 6 7 8 9 10 11 12 13 Ballet Nuevo ‒ Tìm kiếm mục tiêu lợi nhuận Doanh số bán vé dự kiến Chi phí nhượng bộ trung bình Phí rạp hát Doanh thu nhượng quyền Lợi nhuận Doanh thu vé Giá vé % lợi nhuận nhượng quyền Tỷ lệ lợi nhuận 2.500 mọi người Mỗi người Mỗi người $ 25,00 18.000 USD 170.937,50 USD $ 31.250,00 150.000 USD $68,38 50% 80% Tự động Lưu Oﬀ ÁP DỤNG TƯ DUY PHIẾU 8.5: Diễn giải theo quy tắc Phân tích Sử dụng các yếu tố của tư duy phê phán khi diễn giải một mô hình quy định:

- Biết ai sẽ sử dụng dự đoán giúp xác định xem mô hình có giải quyết được mối quan ngại và vấn đề của họ hay không chắc chắn rằng nó đại diện cho thực tế (Các bên liên quan).

- Cần phải hiểu lý do tại sao việc phân tích được thực hiện để đánh giá xem liệu biến thể có có thể có ý nghĩa (Mục đích).

- Biết cách diễn giải các phân tích hồi quy và đánh giá các mô hình tối ưu hóa là cần thiết để giải thích chúng (Kiến thức).

![ILLUSTRATION 8.36](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.36.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu Ôn tập và thực hành chương Đánh giá mục tiêu học tập ❶ So sánh cách diễn giải phân tích dữ liệu và dữ liệu thăm dò. Mặc dù việc khám phá và giải thích dữ liệu có vẻ giống nhau nhưng có sự khác biệt quan trọng: • Khám phá dữ liệu là quá trình phân tích dữ liệu để xác định liệu chúng ta có cần thực hiện các phân tích bổ sung hay không. Mục tiêu trong việc khám phá dữ liệu đang tiến đến mức chúng ta có đủ khả năng tự tin rằng chúng tôi hiểu những gì đang xảy ra trong dữ liệu. • Diễn giải phân tích dữ liệu là quá trình đánh giá một kết quả phân tích để hiểu và giải thích ý nghĩa của nó. Những hiểu biết thu được từ giải thích dẫn đến quyết định kinh doanh tốt. ❷ Áp dụng tư duy phê phán vào việc giải thích phân tích dữ liệu. • Hiểu biết về các bên liên quan giúp hiểu được các vấn đề nội dung phân tích và ý nghĩa của kết quả. • Xác định mục đích của việc phân tích sẽ duy trì sự tập trung vào mục đích của nó mục tiêu và tránh đi sai hướng trong việc diễn giải. Áp dụng nó

## 8.5 Giải thích hồi quy Kết quả Dữ liệu Kế toán quản trị DHI muốn hiểu điều gì đang thúc đẩy tổng chi phí cho chuỗi khách sạn. Luciana cảm thấy chắc chắn rằng các biến số sau có ảnh hưởng lớn nhất đến chi phí:

- Tuổi của khách sạn

- Số lượng nhân viên bảo trì

- Tổng số giờ dọn phòng

- Tổng số phòng cho thuê Cô ấy đã yêu cầu bạn chuẩn bị mô hình hồi quy sử dụng các biến đó để dự đoán chi phí. Sau- minh họa hạ thấp là kết quả của mô hình đó. Số giờ dọn phòng và số phòng được thuê theo địa điểm Mô hình hồi quy Nhiều R R vuông Hình vuông R đã điều chỉnh Lỗi chuẩn Quan sát ANOVA 0.7215151 0,520584 0.4714132 93901.466 44 df SS MS F 3.73412E+11 3.43882E+11 Hồi quy dư Tổng cộng 4 39 43 7.17293E+11 9.3353E+10 8817485253 10.58724498 6.62556E-06 107148.5543 2.918679199 Đánh chặn Cho thuê phòng Giờ làm việc, dọn phòng Tuổi Nhân viên, Bảo trì 413314.47 11.015461 6.0934507 −3565.695 16762.392 1674.938087 6906.902129 5.531393108 −2.12885155 2.42690446 1.1016123 3.85739665 3.77412543 0,039637083 0,019949355 0.277382666 0,000534577 0,000418405 Ý nghĩa F Hệ số lỗi chuẩn t Thống kê giá trị P Thống kê hồi quy GIẢI PHÁP 1. Bình phương R được điều chỉnh là 0,471, nghĩa là tiền thuê phòng, số giờ dọn phòng đã làm, tuổi của khách sạn và số lượng nhân viên bảo trì có thể chiếm 47,1% tổng chi phí. 2. Mô hình có ý nghĩa – Ý nghĩa F nhỏ hơn 0,05 – vì vậy, tốt hơn là không có mô hình nào cả. 3. Giá trị p của Số giờ làm việc, Công việc nội trợ lớn hơn 0,05 nên loại bỏ từ mô hình. 1. Hình vuông R được điều chỉnh tiết lộ điều gì về mô hình? 2. Có mô hình thì tốt hơn là không có mô hình? 3. Có biến nào bạn muốn Luciana loại bỏ khỏi mô hình không? Tại sao?

![Apply It 8.5](../TaiLieu/textbookForPractice/Figures/Ch_08/Apply%20It%208.5.png)

Cách đi qua • Khi diễn giải một phân tích, hãy cân nhắc xem có lựa chọn thay thế nào không giải thích hoặc phân tích thay thế cần được tiến hành. • Xác định các rủi ro tiềm ẩn như rủi ro dữ liệu, rủi ro phân tích và rủi ro thiên vị. • Mọi diễn giải phân tích đều yêu cầu kiến ​​thức cụ thể. Xác định- trang bị những kiến thức cần thiết về kế toán, ngành và công nghệ edge cung cấp cho chúng tôi các công cụ để diễn giải phân tích. • Giải thích phân tích tương tự được thực hiện trước đây có thể áp dụng trong bối cảnh hiện nay. ❸ Xác định xem kết quả phân tích dữ liệu có đáp ứng được yêu cầu câu hỏi và phù hợp với mục tiêu phân tích. Câu trả lời cho một số câu hỏi cụ thể có thể hữu ích khi giải thích- tiến hành phân tích dữ liệu: • Phương pháp và kết quả có hợp lý với kiến thức hiện tại không? cạnh về chủ đề đang được phân tích? Liệu việc phân tích và giải thích có ý nghĩa? Xem xét liệu việc phân tích có ý nghĩa rõ ràng. Nó có giải quyết được mục tiêu hoặc câu hỏi được đặt ra không? Cũng hãy xem xét liệu cách giải thích có hợp lý hay không. • Đôi khi cần thêm thông tin hoặc phân tích trước khi đưa ra quyết định cuối cùng việc giải thích có thể được hoàn thành. Tránh những rủi ro như “những gì bạn xem là tất cả đều có” thành kiến hoặc thiên vị xác nhận. ❹ Đánh giá tính giá trị và độ tin cậy của mô tả và kết quả phân tích dữ liệu chẩn đoán. Phân tích mô tả xác định những gì đã xảy ra trong quá khứ, trong khi phân tích chẩn đoán điều tra lý do tại sao nó xảy ra. • Các kỹ thuật phân tích mô tả phổ biến bao gồm tần suất phân phối, lập bảng chéo, đo lường vị trí và đo lường chắc chắn về sự phân tán. • Các kỹ thuật phân tích chẩn đoán phổ biến bao gồm sự bất thường phát hiện, phân tích tương quan và phân tích xu hướng. • Phân tích dữ liệu có giá trị nếu nó đo lường được những gì nó được cho là chắc chắn và thể hiện hiện thực. • Phân tích dữ liệu là đáng tin cậy nếu các thước đo được sử dụng trong phân tích chính xác và nhất quán và dữ liệu được sử dụng là đáng tin cậy và đáng tin cậy. ❺ Đánh giá tính giá trị và độ tin cậy của các phương pháp dự đoán và kết quả phân tích dữ liệu theo quy định. Phân tích dự đoán được sử dụng khi mục tiêu của phân tích là để dự đoán một kết quả trong tương lai. Phân tích theo quy định nhằm mục đích quy định những hành động mang lại kết quả tốt nhất trong tương lai. • Hồi quy tuyến tính là nền tảng cho hầu hết các mô hình dự đoán- kỹ thuật ing. Hiệu lực của mô hình hồi quy được đánh giá bằng cách mô hình thể hiện hiện tượng tương tác tốt như thế nào est. Độ tin cậy của mô hình được đánh giá bằng cách đánh giá thống kê hồi quy, thống kê mô hình và giá trị p của các hệ số. • Các mô hình tối ưu hóa và phân tích giả định thường được sử dụng cho các phân tích mang tính quy tắc. Trong nghề kế toán, chuyện gì sẽ xảy ra? phân tích có thể giúp đánh giá một số lựa chọn (Phân tích kịch bản) hoặc để xác định một đầu vào cụ thể (Tìm kiếm mục tiêu). • Bất kể công cụ nào được sử dụng để tạo phân tích giả định, hãy đánh giá giá trị bằng cách xác định xem mô hình có đang đo lường những gì nó hỗ trợ hay không đặt ra để đo lường (giá trị) và các biện pháp đó là chính xác và nhất quán (độ tin cậy). Đánh giá các điều khoản chính Chính xác 8-17 Bình phương R đã điều chỉnh (R2) 8-28 Sự bất thường 8-22 Phân tích tương quan 8-23 Hệ số tương quan 8-23 Phân tích bảng chéo 8-19 Giải thích phân tích dữ liệu 8-2 Phân bổ tần số 8-18 Hồi quy tuyến tính 8-27 Trung bình 8-19 Trung vị 8-19 Chế độ 8-19 Ngoại lệ 8-20 Thống kê hồi quy 8-28 Độ tin cậy 8-17 Biểu đồ phân tán 8-20 Độ lệch chuẩn 8-21 Sai số chuẩn 8-28 Phân tích xu hướng 8-24 Đường xu hướng 8-24 Hiệu lực 8-17 phân tích điều gì sẽ xảy ra 8-31 Cách đi qua CÁCH

## 8.1 Tạo phân phối tần số với Power BI Hình minh họa 8.14 là sự phân bố tần số cho các mẫu xe Super Scooter khác nhau. Nó đã được tạo ra trong Excel, nhưng các công cụ khác, chẳng hạn như Power BI, cũng có thể tạo phân bố tần số. Những gì bạn cần: Dữ liệu Tệp dữ liệu How To 8.1. BƯỚC 1: Trích xuất dữ liệu. Mở Power BI và chọn tab Home ở ngang trên cùng menu (Minh họa 8.37). Làm cách nào để

![ILLUSTRATION 8.37](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.37.png)

CHƯƠNG 8 Diễn giải kết quả phân tích dữ liệu Tự động Lưu Chia sẻ Bình luận Dán Cắt Sao chép Trình vẽ định dạng Tập tin Làm người mẫu Máy tính để bàn Power BI không có tiêu đề Xem Trợ giúp Chèn Trang chủ Bảng nhớ tạm Mới đo lường nhanh chóng đo lường Độ nhạy Xuất bản Chia sẻ Máy tính Chèn Truy vấn dữ liệu X + Excel Sổ làm việc Điện B1 bộ dữ liệu SQL Máy chủ Nhập dữ liệu Dữ liệu ngược Gần đây nguồn Nhận dữ liệu + A Mới Trực quan văn bản cái hộp Thêm hình ảnh Làm mới chuyển đổi dữ liệu Độ nhạy Dán Cắt Sao chép Trình vẽ định dạng Bảng nhớ tạm lúa mạch đen Làm mới Mới đo lường nhanh chóng đo lường Độ nhạy Xuất bản Chia sẻ Máy tính Độ nhạy Điều hướng Tùy chọn hiển thị Bán hàng siêu xe tay ga_ 2024−2025.xlsx [2] Giao dịch bán hàng 2024–2025 Giao dịch mua bán 2024–2025 Trang 2 Số thứ tự Năm Số đơn đặt hàng bán hàng người mẫu Ngày bán 13684−2024 13684 2024 Celeritas 31/12/2024 13685−2024 13685 2024 Lazer 31/12/2024 13682−2024 13682 2024 thuyền trưởng 30/12/2024 13683−2024 13683 2024 Lazer 30/12/2024 13677−2024 13677 2024 Lazer 29/12/2024 13678−2024 13678 2024 Lazer 29/12/2024 13679−2024 13679 2024 Celeritas 29/12/2024 13680−2024 13680 2024 thuyền trưởng 29/12/2024 13681−2024 13681 2024 Celeritas 29/12/2024 13675−2024 13675 2024 Celeritas 28/12/2024 13676−2024 13676 2024 thuyền trưởng 28/12/2024 13671−2024 13671 2024 thuyền trưởng 27/12/2024 13672−2024 13672 2024 Lazer 27/12/2024 13673−2024 13673 2024 Lazer 27/12/2024 13674−2024 13674 2024 thuyền trưởng 27/12/2024 13668−2024 13668 2024 thuyền trưởng 26/12/2024 13669−2024 13669 2024 Celeritas 26/12/2024 13670−2024 13670 2024 cú đá 26/12/2024 13665−2024 13665 2024 Lazer 25/12/2024 Hủy bỏ Tải Chuyển đổi dữ liệu ! Dữ liệu trong bản xem trước đã bị cắt bớt do giới hạn kích thước Trang 1 Hãy chắc chắn rằng bạn đánh dấu vào ô trước “Bán hàng Giao dịch 2024− 2025.” Nếu bạn quên bạn sẽ không có tùy chọn “Tải”. GỢI Ý 1 2

**MINH HỌA 8.37 Trích xuất và tải dữ liệu siêu xe tay ga • Chọn biểu tượng Excel bên dưới. • Khi hộp thoại file mở ra, tìm đến file Excel Super Scooters và chọn Open ở góc dưới bên phải. BƯỚC 2: Nạp dữ liệu (Minh họa 8.37). Từ cửa sổ Điều hướng của Power BI, cửa sổ này tự động mở ra một cách tự nhiên sau khi nguồn dữ liệu được chọn, hãy chọn dữ liệu cho bài tập này: Giao dịch bán hàng hành động 2023–2025. Tiếp theo nhấn Load ở dưới cùng bên phải để tải dữ liệu này lên. BƯỚC 3: Chuyển đổi dữ liệu để tạo bảng tần số (Minh họa 8.38). Màn hình sẽ quay lại màn hình Power BI chính. Cột Trường sẽ ở phía bên phải của màn hình. • Nhấp vào mũi tên thả xuống bên cạnh Giao dịch bán hàng 2023–2025 để xem tất cả tên cột từ bảng tính. • Kéo các trường dữ liệu Model và Σ Order Number vào các khoảng trống được cung cấp ngay bên dưới Giá trị. • Mỗi trường có một mũi tên xuống chỉ ra một menu các tùy chọn. Chọn mũi tên này cho Σ Trường Số thứ tự và menu kéo xuống xuất hiện. • Chọn Đếm. Tên trường sẽ thay đổi thành Số lượng đơn hàng. • Bên trái là bảng kết quả gồm 4 mẫu Super Scooter, số lượng đơn đặt hàng và tổng cộng. Bạn có thể phóng to bảng mới đó để xem tất cả cột.**

![ILLUSTRATION 8.38](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.38.png)

Cách đi qua

**MINH HỌA 8.38 Xây dựng bảng tần số Giá trị Giá trị Giao dịch mua bán 20... Giao dịch mua bán 20... Màu sắc Màu sắc Đóng góp M... Đóng góp M... Quốc gia Quốc gia Số ngày tồn kho Số ngày tồn kho Tổng doanh thu Tổng doanh thu Lao động Lao động Vị trí Vị trí Vật liệu Vật liệu người mẫu người mẫu Số thứ tự Số thứ tự Chi phí chung Chi phí chung Doanh thu Doanh thu Đơn đặt hàng bán hàng số... Đơn đặt hàng bán hàng số... Thuế bán hàng Thuế bán hàng Báo cáo chéo Báo cáo chéo Oﬀ Oﬀ Khoan qua Khoan qua Trực quan hóa Trực quan hóa Trường Trường 123 người mẫu người mẫu Số thứ tự Số thứ tự Tìm kiếm Tìm kiếm BƯỚC 4: Thêm cột bảng tần số tương đối bằng cách quay lại cột Trường và se- chọn trường Số thứ tự. Kéo nó xuống bên dưới trường Số lượng đơn đặt hàng trong Cột trực quan hóa. • Chọn menu mũi tên kéo xuống cho trường Số đơn hàng mới và chọn Đếm. • Trong menu mũi tên kéo xuống, chọn Hiển thị giá trị dưới dạng. Chọn mũi tên bên phải để Phần trăm của Tổng số. • Bên trái màn hình sẽ hiển thị cột mới tỷ lệ phần trăm tổng doanh thu của từng sản phẩm mẫu xe tay ga và tổng thể (Minh họa 8.39). Một lần nữa, có thể cần phải phóng to bảng để xem cột mới.**

**MINH HỌA 8.39 Siêu phẩm cuối cùng Bảng tần số xe tay ga người mẫu thuyền trưởng Celeritas 892 cú đá Lazer Tần số 1.010 456 Tổng doanh thu 3.645 1.287 24,47% Tần số tương đối 27,71% 12,51% 100,00% 35,31% • Cuối cùng, có thể đổi tên các cột thành “Tần suất” và “Tương đối”. Tần suất” bằng cách nhấp vào mũi tên xuống tương tự được sử dụng để chọn Đếm và thay vào đó chọn Đổi tên cho Visual này. Cũng có thể thực hiện phân phối tần suất bằng cách sử dụng PivotTable hoặc bằng cách sử dụng trực quan hóa dữ liệu. phần mềm hoạt động. CÁCH 8.2 Tính toán thống kê mô tả trong Microsoft Excel Để tạo Minh họa về doanh số bán hàng của Super Scooters trong Hình minh họa 8.18, hãy sử dụng Mô tả Tùy chọn thống kê trong Công cụ phân tích dữ liệu trong Microsoft Excel. Làm cách nào để**

![ILLUSTRATION 8.39](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.39.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu được rồi Hủy bỏ Trợ giúp Phân tích dữ liệu Công cụ phân tích ? Anova: Yếu tố đơn lẻ Anova: Hai yếu tố với sự nhân rộng Anova: Hai yếu tố không cần nhân rộng Tương quan Hiệp phương sai Thống kê mô tả Làm mịn theo cấp số nhân F-Test Hai mẫu cho phương sai Phân tích Fourier biểu đồ

**MINH HỌA 8.41 Phân tích Hộp thoại Công cụ được rồi Hủy bỏ Trợ giúp Thống kê mô tả đầu vào Cột Hàng Phạm vi đầu vào: Được nhóm theo: Tùy chọn đầu ra Phạm vi đầu ra: Sổ làm việc mới Lớp bảng tính mới: Thống kê tóm tắt Mức độ tin cậy cho giá trị trung bình: Kth nhỏ nhất: Lớn thứ K: $B$1:$B$37 1 95 % 1 ? Nhãn ở hàng đầu tiên 3 4**

**MINH HỌA 8.42 Mô tả Hộp thống kê**

**MINH HỌA 8.40 Siêu Dữ liệu xe tay ga Tự động Lưu tập tin Bố cục trang Công thức Xem lại Chèn Trang chủ ngoại hối 1 Tháng/ Năm 23 tháng 1 23 tháng 2 23 tháng 3 154 182 126 bán hàng khối lượng A B C D Trang 1 2 3 4 E dữ liệu 1 F13 Bảng nhớ tạm Hoàn tác Phông chữ Dán Calibri A A 11 B tôi bạn A Những gì bạn cần: Dữ liệu Tệp dữ liệu How To 8.2. BƯỚC 1: Mở bảng tính bằng cách nhấp vào Dữ liệu trên thanh công cụ. (Minh họa 8.40). BƯỚC 2: Chọn Thống kê mô tả (Minh họa 8.41). BƯỚC 3: Trong hộp Thống kê mô tả, chỉ định phạm vi đầu vào (Minh họa 8.42).**

![ILLUSTRATION 8.42](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.42.png)

Câu hỏi trắc nghiệm • Phạm vi đầu vào là dữ liệu được sử dụng để tính toán thống kê mô tả. Trong ví dụ này nó là cột B • Bắt đầu với tiêu đề cột và cuộn xuống cuối tập dữ liệu. (Gợi ý: bấm vào ô tiêu đề và giữ Shift, Ctrl và mũi tên xuống bàn phím sẽ nắm bắt tất cả dữ liệu trong cột đó.) BƯỚC 4: Tạo đầu ra thống kê bằng cách nhấp vào Nhãn và Thống kê Tóm tắt. Chọn Phạm vi đầu ra và chọn một ô trong bảng tính hiện tại để có kết quả hoặc bấm vào Mới Worksheet và Excel sẽ đưa kết quả vào một bảng tính mới (Minh họa 8.42). Câu hỏi trắc nghiệm

1. (LO 1) Diễn giải kết quả phân tích dữ liệu là quá trình một. đánh giá một phân tích để hiểu và giải thích ý nghĩa của nó. b. thực hiện các thủ tục phân tích mô tả để hiểu rõ hơn đứng dữ liệu. c. khám phá dữ liệu để hiểu rõ hơn các mối quan hệ. d. chuyển đổi dữ liệu để cho phép phân tích.

2. (LO 1) Câu nào sau đây không phải là câu hỏi được giải quyết trong dữ liệu giải thích kết quả phân tích? Một. Dữ liệu có được sử dụng chính xác để thực hiện phân tích không? b. Công nghệ có được sử dụng đúng để thực hiện phân tích không? c. Phân tích có thiên vị không? d. Các phương pháp phân tích thích hợp có được sử dụng không?

3. (LO 1) Nếu người chuẩn bị phân tích bỏ qua các quan sát thì họ không nghĩ rằng quyết định này quan trọng, đây sẽ là một ví dụ về một. làm sạch dữ liệu. b. phương pháp phân tích sai. c. quyết định gian lận. d. thiên lệch lựa chọn.

4. (LO 1) Một trong những khía cạnh được đánh giá cao nhất của kế toán viên là khả năng đến một. là những người đánh giá độc lập và hoài nghi về thông tin tài chính. b. thực hiện các phép tính khó. c. xác định nhân viên có hành vi gian lận. d. nhớ thông tin tài chính.

5. (LO 2) Để diễn giải đầy đủ kết quả phân tích dữ liệu, một. xác định người đã chuẩn bị phân tích. b. xác định mục đích của việc phân tích. c. tự mình chuẩn bị phân tích. d. có tất cả kiến ​​thức cần thiết để hiểu được việc phân tích.

6. (LO 2) Khi diễn giải kết quả phân tích dữ liệu, một. chỉ xem xét các bên liên quan nội bộ bị ảnh hưởng bởi kết quả. b. các bên liên quan không liên quan đến việc giải thích. c. chỉ xem xét các bên liên quan bên ngoài bị ảnh hưởng bởi kết quả. d. xem xét các bên liên quan bên trong và bên ngoài có khả năng bị ảnh hưởng bởi kết quả.

7. (LO 2) Kết quả phân tích dữ liệu không bao gồm dữ liệu gần đây nhất dữ liệu là một ví dụ về loại rủi ro nào? Một. Phương pháp sai phân tích b. Người chuẩn bị thiên vị c. Tính kịp thời d. Tính đầy đủ

8. (LO 2) Khi diễn giải kết quả phân tích dữ liệu, điều nào sau đây- việc hạ thấp có thể là một rủi ro phân tích tiềm ẩn? Một. Phương pháp sai b. Thiếu dữ liệu liên quan c. Xu hướng dữ liệu d. Kiểm soát nội bộ

9. (LO 2) Quá trình suy nghĩ về những trải nghiệm trong quá khứ có thể ảnh hưởng như thế nào được áp dụng cho việc giải thích phân tích dữ liệu hiện tại là khía cạnh nào của tư duy phê phán? Một. Nhận dạng các bên liên quan b. Lựa chọn thay thế c. Tự phản ánh d. Mục đích

10. (LO 3) Một phân tích được chuẩn bị để hỗ trợ một niềm tin đã được xác định trước là một ví dụ về một. thiên lệch lựa chọn. b. gian lận. c. thiên kiến ​​xác nhận. d. ảnh hưởng đến sự thiên vị.

11. (LO 3) Điều nào sau đây mô tả quá trình xác định- xem kết quả phân tích có hợp lý với mục đích dự kiến hay không câu hỏi hoặc mục đích phân tích? Một. Có ý nghĩa b. Kiểm tra tổng số c. Phân tích thống kê d. Chuẩn bị dữ liệu trực quan hóa

12. (LO 3) Nếu câu trả lời cho câu hỏi “Phân tích có đề cập đến nhu cầu/mối quan tâm của các bên liên quan?” là không thì một. bạn phải thực hiện lại phân tích tương tự để xem liệu bạn có nhận được kết quả khác hay không. b. nó có thể sẽ được chấp nhận nếu các con số là chính xác. c. có thể các bên liên quan đã không hiểu được vấn đề. d. có thể cần phải thực hiện một phân tích khác trước khi bạn có thể giải thích kết quả.

13. (LO 3) Khi so sánh hai biến có số đo khác nhau- cân tâm lý một. biểu đồ cột nhóm là tốt nhất để so sánh trực quan các biến. b. biểu đồ thanh nhóm là tốt nhất để so sánh trực quan các biến. c. biểu đồ trục kép là cách tốt nhất để so sánh trực quan các biến. d. biểu đồ đường là tốt nhất để so sánh trực quan các biến. Dữ liệu Thẻ Dữ liệu xuất hiện khi dữ liệu cần thiết để trả lời một câu hỏi hoặc hoàn thành một câu hỏi. bài tập có sẵn trên nền tảng học tập trực tuyến của Wiley.

![ILLUSTRATION 8.42](../TaiLieu/textbookForPractice/Figures/Ch_08/ILLUSTRATION%208.42.png)

Chương 8 Diễn giải kết quả phân tích dữ liệu

14. (LO 4) Khi đánh giá độ tin cậy của kết quả phân tích dữ liệu, đánh giá xem liệu một. các biện pháp được sử dụng là chính xác và nhất quán. b. các biện pháp được sử dụng đo lường những gì họ phải làm. c. dữ liệu được sử dụng kịp thời. d. dữ liệu được sử dụng là hợp lý.

15. (LO 4) Một phân tích thích hợp để xác định số lần một sự kiện đã xảy ra sẽ là một. thước đo vị trí. b. thước đo độ phân tán. c. một sự phân bố tần số d. tối ưu hóa tuyến tính.

16. (LO 4) Sự bất thường là một. luôn là một ngoại lệ. b. một quan sát đi chệch khỏi những gì bình thường hoặc mong đợi. c. luôn bị loại bỏ. d. một dấu hiệu của sự gian lận.

17. (LO 4) Khi kiểm tra mối quan hệ giữa hai biến, nếu một biến tăng khi biến kia giảm mối quan hệ là một. một mối tương quan tích cực. b. một mối tương quan tiêu cực. c. không tương quan. d. tương quan hoàn hảo.

18. (LO 4) Nếu mục tiêu là sử dụng dữ liệu lịch sử để xác định các mẫu, phân tích nào tốt nhất để sử dụng? Một. Tối ưu hóa tuyến tính b. Phân phối tần số c. Phân tích xu hướng d. Hồi quy tuyến tính

19. (LO 5) Phân tích nào sau đây có thể dự đoán tương lai kết quả? Một. Độ lệch chuẩn b. Tối ưu hóa tuyến tính c. Phân tích bảng chéo d. Hồi quy tuyến tính

20. (LO 5) Mục tiêu của phân tích dự đoán là xây dựng một mô hình một. có thể giúp dự đoán hoặc hiểu rõ hơn một hiện tượng trong đó bạn quan tâm. b. có thể được thực hiện bằng phần mềm thống kê. c. có thể xác định tần suất xảy ra một hiện tượng trong quá khứ. d. không quá phức tạp.

21. (LO 5) Đánh giá độ tin cậy của phân tích hồi quy bao gồm một. so sánh giá trị trung bình và trung vị của biến phụ thuộc. b. đảm bảo mô hình trả lời câu hỏi hoặc mục đích của sự phân tích. c. xem xét số liệu thống kê của mô hình. d. bằng cách sử dụng kịch bản what-if.

22. (LO 5) Trong mô hình hồi quy được chuẩn bị để dự đoán doanh thu, sau đây là cách giải thích đúng về R bình phương đã điều chỉnh là 0,85? Một. Doanh thu sẽ tăng 85% trong năm tới. b. Các biến độc lập trong mô hình có thể giải thích được 85% sự thay đổi về doanh thu. c. Biến phụ thuộc trong mô hình có thể giải thích được 85% sự thay đổi của các biến độc lập. d. Bình phương R được điều chỉnh là một con số quá nhỏ để chúng tôi có thể dựa vào trên mô hình.

23. (LO 5) Một mô hình bảng tính cho phép đánh giá mức độ thay đổi các giá trị và giả định ảnh hưởng đến kết quả được gọi là một. phương trình hồi quy. b. mô hình tối ưu tuyến tính. c. mô hình dự đoán tốt nhất d. phân tích chuyện gì xảy ra nếu.

24. (LO 5) Công cụ nào là tốt nhất khi biết được kết quả mong muốn, nhưng không phải giá trị đầu vào cho một biến sẽ đạt được kết quả đó? Một. Tìm kiếm mục tiêu b. Trình quản lý kịch bản c. Hồi quy tuyến tính d. Phân tích dữ liệu Câu hỏi ôn tập

1. (LO 1) So sánh và đối chiếu việc khám phá dữ liệu với diễn giải phân tích dữ liệu.

2. (LO 1) Thảo luận về hai bước tổng thể trong quá trình diễn giải phân tích dữ liệu.

3. (LO 2) Khi áp dụng mô hình tư duy phản biện SPARKS để diễn giải các phân tích dữ liệu, làm thế nào xác định các bên liên quan giúp giải thích phân tích đó?

Câu hỏi ôn tập Đảm nhận vai trò của người chuẩn bị cho sự quán tưởng này.

1. Các bên liên quan là ai?

2. Mục đích của việc phân tích là gì?

3. Bạn cần có kiến ​​thức áp dụng nào để chuẩn bị cho việc hình dung này? Sau đó, đảm nhận vai trò người xem lại hình ảnh trực quan này và trả lời những câu sau:

4. Những rủi ro khi diễn giải hình dung này là gì?

5. Có thể rút ra kết luận gì từ hình dung?

5. (LO 2) Giải thích tại sao việc xác định và đánh giá các cách giải thích kết quả khác lại quan trọng.

6. (LO 3) Thảo luận ý nghĩa của việc hỏi “phân tích có hợp lý không?”

7. (LO 3) Những câu hỏi nào nên được đặt ra khi đánh giá dữ liệu và phương pháp phân tích?

8. (LO 3) Những câu hỏi nào nên được đặt ra khi đánh giá kết quả phân tích?

9. (LO 4) Giải thích ý nghĩa của độ tin cậy và giá trị trong bối cảnh diễn giải phân tích dữ liệu.

10. (LO 4) Giải thích sự khác biệt giữa điểm bất thường và điểm ngoại lệ.

11. (LO 5) Thảo luận cách đánh giá tính hợp lệ của mô hình hồi quy.

12. (LO 5) Giải thích cách sử dụng bình phương R đã điều chỉnh để đánh giá độ tin cậy của mô hình hồi quy.

13. (LO 5) Giải thích cách diễn giải liệu một biến độc lập trong mô hình hồi quy có phải là biến phụ thuộc hay không thước đo khả thi của biến phụ thuộc. (a) Tổng doanh số bán hàng bao gồm doanh số bán hàng hóa, lợi nhuận ròng dự kiến từ cửa hàng và các kênh kỹ thuật số của chúng tôi, cũng như vỡ thẻ gif. (b) Quý 4 và cả năm 2017 lần lượt có 14 tuần và 53 tuần, so với 13 tuần và 52 tuần trong các khoảng thời gian có thể so sánh được trình bày. (c) Bắt đầu từ quý 1 năm 2018, chúng tôi đã áp dụng các chuẩn mực kế toán mới để ghi nhận doanh thu, tiền thuê nhà và lương hưu. Chúng tôi đang trình bày một số kết quả của kỳ trước trên cơ sở phù hợp với các tiêu chuẩn mới và phù hợp với cách trình bày của kỳ hiện tại. Chúng tôi đã cung cấp thêm thông tin về tác động của chính sách mới Chuẩn mực kế toán về thông tin tài chính đã báo cáo trước đây theo Mẫu 8-K nộp ngày 11/5/2018. (d) Doanh thu năm 2015 bao gồm 3,815 triệu USD liên quan đến hoạt động kinh doanh dược phẩm và phòng khám trước đây của chúng tôi mà Target đã bán cho CVS vào tháng 12 năm 2015. −8,0 1Q 2Q 3Q Tổng doanh thu (a): Phần trăm thay đổi so với năm trước 4Q Năm −4,0 0,0 4.0 8,0 12.0 16.0 20,0 24.0 28,0 Phần trăm 2016(c)(d) 2017(b)(c) 2018 2019 2020 3,5 % 11,3 % (1,1)% 5,1 % – % 10,0 % 1,8 % 5,7 % 1,4 % 4,7 % 7,0 % 24,8 % 1,6 % 3,6 % Năm tài chính 2020 2019 2018 2017 (b) (c) 2016 (c) (d) 1Q 2Q 3Q 4Q 3,7 % 3,4 % (5,8)% 3,6 % Năm Nguồn: Báo cáo tài chính hợp nhất của Target được nộp cho Ủy ban Chứng khoán và Giao dịch Hoa Kỳ Public Domain.

4. (LO 2) Hình ảnh trực quan sau đây đã được công bố trên trang web Quan hệ nhà đầu tư mục tiêu.

Chương 8 Diễn giải kết quả phân tích dữ liệu 0 10.000 20.000 30.000 40.000 50.000 60.000 2025 70.000 80.000 90.000 100.000 110.000 Công trình công cộng - Tiện ích Sở Thành phố Boulder 2025 Tài khoản phải trả theo Sở Công trình công cộng - Dịch vụ hỗ trợ Công trình công cộng - Giao thông Công viên và Giải trí Không gian mở & Công viên trên núi NA Dịch vụ con người Sức sống cộng đồng Tài chính cảnh sát Thư viện Công nghệ thông tin Nhà ở lửa Toàn quốc / Toàn thành phố Sáng kiến khí hậu Nghệ thuật PW-Phát triển Văn phòng Quản lý Thành phố quy hoạch Số tiền giao dịch ($ tính bằng triệu) Bài tập ngắn gọn

1. Câu hỏi ban đầu để phân tích là “Bộ phận nào có số tiền chi tiêu cao nhất trong năm 2025?” Phân tích có trả lời được câu hỏi này không? Tại sao hoặc tại sao không?

2. Dựa trên thông tin từ người chuẩn bị phân tích, dữ liệu được sử dụng trong phân tích có chính xác không? tại sao hoặc tại sao không?

3. Thông tin nào trong tuyên bố của người chuẩn bị phân tích cho phép bạn kết luận rằng kết quả của phân tích có chính xác không? BE 8.1 (LO 1) Mặc dù việc khám phá dữ liệu và giải thích dữ liệu có liên quan đến quá trình phân tích dữ liệu, có sự khác biệt giữa hai hoạt động này. Khám phá dữ liệu là hiểu biết ________, trong khi diễn giải dữ liệu là hiểu _____________. BE 8.2 (LO 1) Có các bước trong quá trình xem xét bản phân tích. Câu hỏi đầu tiên hỏi liệu việc phân tích có tạo ra ý nghĩa, và câu thứ hai hỏi liệu kết quả phân tích có phải là ________ và _____________ hay không. BE 8.3 (LO 1) Kế toán tài chính Bạn là nhà phân tích tài chính làm việc cho thành phố Boulder, Col- orado. Người quản lý của bạn đã yêu cầu bạn xem lại phân tích tài khoản phải trả do các tài khoản chuẩn bị bộ phận phải trả. Người chuẩn bị phân tích đã nói với bạn rằng phân tích nhằm xác định Boulder nào, Sở thành phố Colorado có mức chi tiêu bằng đô la Mỹ cao nhất trong năm 2025. phân tích được chuẩn bị bằng cách sử dụng tất cả dữ liệu giao dịch trong năm 2025 cho mọi bộ phận. Người chuẩn bị cũng xác minh rằng tổng số tiền đã đồng ý với chi tiết đơn hàng thích hợp cho các khoản chi trong sổ cái chung, và rằng không có giao dịch nội bộ công ty nào cần loại bỏ.

Bài tập ngắn gọn

**BE 8.4 (LO 2) Kế toán tài chính Kế toán quản trị Là nhà phân tích tài chính cấp cao tại Super Scooters, bạn đã nhận được biểu đồ sau từ một nhà phân tích tài chính trong bộ phận của bạn. Người đàn ông của bạn- ager muốn biết số lượng sản phẩm phải bán cho mỗi mẫu trước khi nó có lãi. 0 thuyền trưởng Celeritas cú đá Lazer 500 100 Đơn vị người mẫu 806 1.024 607 430 1,452 1.116 1.500 2.000 2023 2024 2025 Số lượng hòa vốn cho mỗi mẫu và năm 553 858 1,807 392 377 333 Người lập biểu đồ cho bạn biết rằng tổng giá bán, chi phí biến đổi và tổng chi phí cố định đã được rút ra từ hệ thống thông tin kế toán và số tiền đã được thống nhất vào sổ cái. Họ đã sử dụng công thức điểm hòa vốn từ kỳ thi CPA để tính điểm hòa vốn theo đơn vị cho từng mô hình. 1. Kế toán và những kiến thức khác sẽ giúp ích gì bạn cần phải có được hoặc nộp đơn để được phê duyệt giải thích rõ ràng biểu đồ đã chuẩn bị hoặc tuyên bố của người chuẩn bị? 2. Các bên liên quan trong phân tích này là ai? 3. Mục đích của việc phân tích là gì và nó có tác dụng gì? biểu đồ trả lời câu hỏi do bạn đặt ra người quản lý? BE 8,5 (LO 2) Khi xem xét các rủi ro có thể xảy ra khi phân tích dữ liệu, hãy luôn đặt câu hỏi về việc phân tích. Hãy ghép từng loại rủi ro với câu hỏi giải quyết nó. Mỗi cái được sử dụng một lần, nhiều lần hoặc không sử dụng chút nào. Một. Rủi ro dữ liệu tiềm ẩn b. Rủi ro phân tích tiềm ẩn c. Rủi ro sai lệch tiềm ẩn d. Rủi ro trực quan tiềm ẩn đ. Rủi ro người dùng tiềm ẩn Câu hỏi Loại rủi ro được giải quyết 1. Người chuẩn bị có bất kỳ sai lệch tiềm ẩn nào có thể ảnh hưởng đến việc chuẩn bị phân tích không? 2. Dữ liệu được sử dụng trong phân tích có phải là dữ liệu mới nhất không? 3. Tất cả các dữ liệu cần thiết và phù hợp có được đưa vào phân tích không? 4. Các biện pháp kiểm soát nội bộ phù hợp có được áp dụng để đảm bảo dữ liệu được sử dụng là chính xác không? 5. Phương pháp phân tích có được sử dụng đúng không? 6. Bản phân tích có thiếu dữ liệu liên quan không? 7. Phân tích có đáp ứng được mục tiêu ban đầu và trả lời được câu hỏi không?**

**BE 8.6 (LO 3) Hãy ghép từng câu với độ lệch thích hợp cần lưu ý khi diễn giải dữ liệu phân tích- vâng. Chọn từ các thành kiến ​​sau đây. Mỗi cái có thể được sử dụng một lần hoặc nhiều lần. Một. Sự thiên vị xác nhận b. Xu hướng lựa chọn Tuyên bố Loại thiên vị 1. Người thực hiện phân tích muốn chứng minh một giả định đã được xác định trước. 2. Người thực hiện phân tích lựa chọn dữ liệu một cách chủ quan. 3. Người diễn giải phân tích muốn chứng minh một giả định đã được xác định trước. 4. Người diễn giải phân tích tập trung vào các kết quả hỗ trợ cho giả định hiện có. 5. Người diễn giải phân tích chỉ xem xét một mẫu dữ liệu chứ không phải toàn bộ dân số. 6. Người diễn giải bản phân tích bỏ qua các khía cạnh của bản phân tích mâu thuẫn với những gì hiện có giả định. Chương 8 Diễn giải kết quả phân tích dữ liệu**

**BE 8.7 (LO 3) Kiểm toán Roberto là giám đốc điều hành của Denton Hospitality Co. Anh ấy đã nhờ bạn để giải thích việc phân tích các khiếu nại của khách. Kiểm toán nội bộ đã cung cấp các phân tích và thông tin sau: “Chúng tôi đã chuẩn bị một biểu đồ trục kép để thể hiện mối quan hệ giữa khiếu nại của khách hàng và sự hài lòng của khách hàng. phe phái. Trục x hiển thị thuộc tính của khách sạn. Trục y bên trái là số lượng khiếu nại và trục y bên phải là điểm hài lòng của khách hàng. Đường ngang trên biểu đồ là điểm hài lòng của khách hàng đối với từng khách sạn tài sản. Có mối tương quan chặt chẽ giữa điểm hài lòng của khách hàng và khiếu nại của khách hàng.” 0 2 4 6 8 10 0 100 200 300 400 500 600 Khiếu nại Khách hàng Sự hài lòng Điểm 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 Điểm hài lòng của khách hàng và khiếu nại của khách Khiếu nại Điểm hài lòng của khách hàng 1. Roberto muốn biết liệu khách có- khiếu nại có liên quan đến chi phí bảo trì. Liệu hình ảnh và thông tin có hỗ trợ do bộ phận kiểm toán nội bộ cung cấp có ý nghĩa với câu hỏi của Roberto? Tại sao hoặc tại sao không? 2. Roberto muốn biết liệu có mối tương quan thống kê giữa khách hàng điểm hài lòng và khiếu nại của khách. là phân tích đủ để trả lời câu hỏi này- chuyện? Tại sao hoặc tại sao không? 3. Roberto muốn trình bày một mô tả trực quan về mối quan hệ giữa nhu cầu khách hàng điểm yếu và khiếu nại của khách như một phần của bài thuyết trình trước hội đồng. Là sự phân tích phương pháp hợp lý? Tại sao hoặc tại sao không? BE 8,8 (LO 4) Kiểm toán Bạn là kiểm toán viên bên ngoài cho các Cửa hàng Phiêu lưu Ngoài trời ở Hoa Kỳ. Thống kê của bạn- Nhóm phân tích cal đã cung cấp bảng thống kê mô tả về doanh số bán hàng của công ty từ năm 2022 đến năm 2025. Cửa hàng phiêu lưu ngoài trời ở Hoa Kỳ Bán hàng 2022‒2025 Nghĩa là trung vị Chế độ Độ lệch chuẩn Phạm vi tối thiểu Tối đa Đếm 229,86 54,49 12,96 623,25 22.638,04 0,44 22.638,48 9.994,00 Người chuẩn bị bản phân tích đã nói với bạn rằng họ đã sử dụng tất cả dữ liệu giao dịch bán hàng và thống nhất tổng doanh số bán hàng trong tập tin vào chi tiết đơn hàng bán hàng trong sổ cái chung. Lưu ý rằng có sự khác biệt lớn giữa giá trị trung bình và giá trị trung bình trong tập dữ liệu bán hàng. Sự khác biệt lớn giữa giá trị trung bình và trung vị gợi ý điều gì về các giao dịch bán hàng của các Cửa hàng Phiêu lưu Ngoài trời ở Hoa Kỳ từ năm 2022 đến năm 2025? BE 8,9 (LO 4) Kế toán tài chính Service King, Inc. là dịch vụ làm sạch thương mại và chăm sóc cỏ công ty. Người quản lý của bạn muốn hiểu liệu có mối quan hệ giữa kết quả của một cuộc khảo sát mức độ hài lòng của khách hàng và các biện pháp thực hiện chính của từng đội vệ sinh. Điểm hài lòng của khách hàng Khiếu nại của khách hàng hàng năm Số phút sử dụng tại chỗ ở Số lượng nhân viên –0.826124807 Tương quan: Khách hàng Điểm hài lòng 1 0.938922087 0.681057818 Người chuẩn bị phân tích tương quan đã cung cấp các định nghĩa dữ liệu: • Điểm hài lòng của khách hàng: Điểm từ khảo sát khách hàng. • Khiếu nại của Khách hàng Hàng năm: Số lượng khiếu nại của khách hàng được gửi mỗi năm. • Số phút dành cho chỗ ở: Số phút mà mỗi đội dọn dẹp dành để dọn dẹp chỗ ở. • Số lượng nhân viên: Số lượng nhân viên được phân công làm công việc dọn dẹp tại cơ sở.**

Bài tập ngắn gọn Sử dụng thông tin này để nối câu trả lời thích hợp cho mỗi câu hỏi. Phản hồi có thể được sử dụng một lần, nhiều hơn một lần, hoặc không hề. Một. Hệ số tương quan dương. b. Hệ số tương quan âm. c. Có mối tương quan tích cực mạnh mẽ giữa các biến. d. Có mối tương quan nghịch mạnh mẽ giữa các biến. đ. Có mối tương quan tích cực vừa phải giữa các biến. f. Có mối tương quan nghịch vừa phải giữa các biến. g. Không có mối quan hệ giữa các biến. Câu hỏi Trả lời

1. Mối quan hệ nghịch đảo giữa hai biến có ý nghĩa gì?

2. Bạn giải thích hệ số tương quan hàng năm như thế nào? khiếu nại của khách hàng và điểm hài lòng của khách hàng?

3. Bạn giải thích hệ số tương quan của số phút dành cho cơ sở kinh doanh và điểm hài lòng của khách hàng?

4. Bạn giải thích hệ số tương quan của số lượng nhân viên và điểm hài lòng của khách hàng? BE 8.10 (LO 5) Kế toán quản lý Khách hàng của bạn, All Care Hospital, cần hiểu chi phí yếu tố quyết định tổng chi phí bệnh viện của họ. Nhóm của bạn đã chạy phân tích hồi quy dựa trên thông tin đầu vào từ bệnh viện. thưa giám đốc tài chính. Phương trình hồi quy như sau: Chi phí bệnh viện = ($39.702) + $564 (Giường) + $0,65 (Khám ngoại trú) + $26,76 (Sinh con) Kết quả tóm tắt Thống kê hồi quy Nhiều R Hình vuông R đã điều chỉnh R vuông Quan sát Lỗi chuẩn 0.87254918 0.76098337 0.76134208 2.000 158.773.661 BE 8.11 (LO 5) Kế toán thuế Một điều cần cân nhắc khi lập kế hoạch thuế là hiểu biết và lập kế hoạch số tiền doanh thu thuần mà một công ty mong đợi trong năm tới. Nhóm của bạn đã tạo một phân tích giả định để dự đoán doanh thu thuần của Super Scooters trong năm tới. Dựa trên số liệu năm hiện tại, nhóm đã thực hiện ba phân tích độ nhạy: • Trường hợp tốt nhất: Họ kỳ vọng doanh số bán hàng sẽ tăng 10%. • Tình huống có thể xảy ra: Họ kỳ vọng doanh số bán hàng sẽ tăng 5%. • Trường hợp xấu nhất: Họ kỳ vọng doanh số bán hàng sẽ giảm 7%. Việc tính toán doanh thu thuần hiện tại như sau. Chi phí biến đổi là 47% doanh thu và Super Scooters kỳ vọng chi phí biến đổi sẽ ổn định trong năm tới.

1. Xác định các biến độc lập trong hồi quy mô hình.

2. Xác định biến phụ thuộc trong mô hình hồi quy.

3. Xác định thống kê hồi quy cho biết mức độ tốt các biến độc lập của mô hình giải thích sự phụ thuộc biến số vết lõm.

4. Chi phí bệnh viện chênh lệch bao nhiêu phần trăm giường bệnh, sinh nở và thăm khám ngoại trú giải thích? Tổng doanh thu Tổng chi phí biến đổi Ký quỹ đóng góp Tổng chi phí cố định Doanh thu thuần 5.722.777 2025 $12,165,162 $ $ $ $ 6.442.385 4.745.563 1.696.822 Doanh thu thuần Trường hợp tốt nhất $12,165,162 $ $ $ $ 6.008.916 6.156.246 1.696.822 trường hợp có thể xảy ra 4.459.424 $12,165,162 $ $ $ $ 5.837.232 6.327.930 1.696.822 4.631.108 $12,165,162 $ $ $ $ 6.123.371 6.041.791 1.696.822 4.344.969 Trường hợp xấu nhất Tổng doanh thu Tổng chi phí biến đổi Ký quỹ đóng góp Tổng chi phí cố định Doanh thu thuần Phân tích chuyện gì xảy ra nếu

1. Bạn cần có kiến thức gì để hiểu được các tình huống tốt nhất, có thể xảy ra và trường hợp xấu nhất? narios nên được giải thích?

2. Giả sử mục tiêu của việc phân tích là ước tính thuế bán hàng cho năm tới. Liệu có ích gì không? phân tích điều gì sẽ xảy ra nếu cung cấp thông tin thích hợp để bắt đầu ước tính của bạn?

Chương 8 Diễn giải kết quả phân tích dữ liệu Bài tập

**EX 8.1 (LO 1) Kiểm toán Hệ thống thông tin kế toán Giải thích và đánh giá dữ liệu Trực quan Phân tích sau đây được chuẩn bị để đánh giá chi phí kinh doanh cho thành phố Boul- der, CO. Bạn làm việc cho bộ phận kiểm toán nội bộ của thành phố. Người quản lý của bạn đã yêu cầu bạn xem lại một phân tích đánh giá việc hoàn trả chi phí kinh doanh cho các sở, ban ngành của thành phố. $0 2.000 USD $2,571 con người Dịch vụ cảnh sát Không gian mở & Núi Công viên Phòng ban Chi phí Thành phố của người quản lý văn phòng Công trình công cộng- Tiện ích lửa $2,694 $4,645 $5,425 $6,533 $12,671 4.000 USD 6.000 USD 8.000 USD 10.000 USD 12.000 USD 14.000 USD Chi phí kinh doanh - Sáu bộ phận hàng đầu Trả lời năm câu hỏi giải thích dữ liệu để xác định xem việc phân tích và trực quan hóa có hợp lý hay không và liệu chúng có hợp lệ và đáng tin cậy hay không.**

**EX 8.2 (LO 1) Kiểm toán Hệ thống thông tin kế toán Giải thích và đánh giá dữ liệu Hình dung Một mẹo ẩn danh đã được gọi đến đường dây nóng gian lận của thành phố với cáo buộc rằng các hợp đồng đang bị hủy bỏ. được trao mà không có quy trình đấu thầu phù hợp. Một phân tích đã được chuẩn bị để xác định mười nhà cung cấp hàng đầu dors để quá trình đấu thầu cho các nhà cung cấp đó có thể được xem xét lại. Dữ liệu được sử dụng là tất cả các khoản phải trả cho năm hiện tại. Các nhà cung cấp có số lượng giao dịch cao nhất được xác định là nhà cung cấp hàng đầu. Pera Năng lượng Xcel Ngân hàng JP Morgan Chase, Na Đối tác nhà ở Boulder Ngân hàng Mỹ Ameresco, Inc. Điểm thuận lợi Công ty TNHH Xây dựng Fransen-Pittman Công ty Quyền sở hữu Quốc gia Fidelity Công ty bảo hiểm sức khỏe và nhân thọ Cigna Tên nhà cung cấp Mười nhà cung cấp hàng đầu 0 1 2 3 4 5 6 7 8 9 10 11 0 100 200 300 400 500 600 Số tiền giao dịch (tính bằng triệu) Số lượng giao dịch Trả lời năm câu hỏi giải thích dữ liệu để xác định xem phân tích có hợp lý và có giá trị và đáng tin cậy hay không.**

Bài tập

**EX 8.3 (LO 2) Hệ thống thông tin kế toán Đánh giá trực quan hóa dữ liệu Chuyển đến tab- leau Gallery và tìm kiếm chủ đề kế toán. Chọn một hình ảnh trực quan và phân tích nó bằng cách sử dụng khuôn khổ tư duy phê phán. 1. Các bên liên quan là ai? 2. Mục đích phân tích là gì? 3. Có cách giải thích hoặc phân tích nào khác không? 4. Có rủi ro nào cần được xem xét không? 5. Người chuẩn bị cần kiến thức gì và phiên dịch viên cần nắm rõ kiến thức gì? đứng phân tích? 6. Bạn có thể sử dụng kinh nghiệm trước đây của mình hoặc áp dụng kinh nghiệm này vào các phân tích trong tương lai như thế nào?**

**EX 8.4 (LO 2) Kế toán tài chính Diễn giải các phân tích các khoản phải thu Giả sử bạn là một nhà phân tích tài chính làm việc trong nhóm kiểm soát viên tại Super Scooters. Bạn đã được yêu cầu phân tích các khoản phải thu và đã chuẩn bị bảng lão hóa sau đây. Các thanh thể hiện tổng tài khoản nhận được khả năng cân bằng. Dưới 30 Giá trị Khách hàng C1036 $40K 0K $40K 0K $40K 0K $40K 0K $40K 0K $40K 0K $40K 0K $40K 0K 0 $10,840 $23,562 $763 $23,038 $17,635 0 $7,184 0 0 0 0 0 0 0 0 0 0 $31,046 $32,229 $32,478 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 $40K 0K C1282 C1423 C1671 C2036 C2274 C3168 C9591 C9917 31 đến 60 61 đến 90 Ngày 91 đến 180 Hơn 180... Siêu xe tay ga, Inc. Bảng lão hóa các khoản phải thu 1. Các bên liên quan là ai? 2. Mục đích của việc phân tích là gì? 3. Có cách giải thích hoặc phân tích nào khác không? 4. Có rủi ro nào cần được xem xét không? 5. Người chuẩn bị cần kiến thức gì và phiên dịch viên cần hiểu kiến thức gì? đứng phân tích? 6. Bạn có thể sử dụng kinh nghiệm trước đây của mình hoặc áp dụng kinh nghiệm này vào các phân tích trong tương lai như thế nào thông qua tự phản ánh?**

Chương 8 Diễn giải kết quả phân tích dữ liệu

**EX 8.5 (LO 2) Kế toán tài chính Giải thích trực quan hóa dòng tiền Bạn làm việc với tư cách là chuyên gia tài chính nhà phân tích trong nhóm báo cáo tài chính tại Walmart, một công ty bán lẻ đại chúng lớn. Bạn đã được yêu cầu diễn giải bản phân tích dòng tiền của công ty so với đối thủ cạnh tranh và bạn đã được cung cấp hình dung sau đây. –$15 –$13,172 –$2,138 –$3,653 –$2,783 –$994 –$1,811 –$684 –$661 –$292 $943 $2,537 $26,557 Tập đoàn Walmart Tập đoàn mục tiêu Công ty Kroger Công ty TNHH Loblaw Thị trường thực phẩm nguyên chất –$13,031 $5,828 $3,775 –$10 –$5 $0 $5 Giá trị (K) $10 $15 $20 $25 $30 Dòng tiền Dòng tiền hoạt động Dòng tiền đầu tư Dòng tiền tài trợ 1. Các bên liên quan là ai? 2. Mục đích phân tích là gì? 3. Có cách giải thích hoặc phân tích nào khác không? 4. Có rủi ro nào cần được xem xét không? 5. Người chuẩn bị cần có kiến thức gì và phiên dịch viên cần có kiến thức gì hiểu phân tích? 6. Bạn có thể sử dụng kinh nghiệm trước đây của mình như thế nào hoặc áp dụng kinh nghiệm này vào các phân tích trong tương lai thông qua sự tự suy nghĩ?**

**EX 8.6 (LO 3) Dữ liệu Kế toán tài chính Giải thích tính hợp lý của phân tích dữ liệu theo là nhà phân tích tài chính tại Best Bakes Bakery, bạn thường được giao nhiệm vụ tiến hành và đánh giá dữ liệu cho việc ra quyết định. Chủ sở hữu Best Bakes đã yêu cầu bạn xác định năm khách hàng hàng đầu của họ. Bạn mỗi- đã hình thành bản phân tích tỷ suất lợi nhuận theo khách hàng và chuẩn bị hình ảnh trực quan sau đây bằng cách sử dụng Best Nướng tập tin dữ liệu. 2021 Tên giám sát Tỷ suất lợi nhuận theo khách hàng 21,98% 45,15% 45,83% 44,85% 42,77% 48,84% 2022 2023 2024 Quán cà phê chim xanh Nhà hàng bơ AM Eatery Quán cà phê nấu ăn tại nhà kem Krispy 39,14% 49,21% 45,51% 47,28% 48,17% 31,18% 50,90% 53,04% 55,14% 47,92% 21,98% 56,82% 48,44% 46,52% 44,31% 50,02% Quán cà phê Creole của Lucile Nhà hàng Gà Đỏ.. Túi núi đá.. 41,04% 45,32% 49,44% 50,38% 47,82% 40,91% 50,02% 40,53% 47,41% 47,11% 42,23% 41,69% Báo lại buổi sáng Eatery Trung tâm thành phố xi-rô Cà phê Ziggi Trung bình Tỷ suất lợi nhuận 56,82% 42,60% 47,37% 43,61% 56,57% 33,27% 43,47% 38,71% Bài tập 1. Dữ liệu được sử dụng trong phân tích có hợp lý với câu hỏi/mục tiêu phân tích không? 2. Phương pháp phân tích có hợp lý với câu hỏi/mục tiêu phân tích không? 3. Kết quả phân tích có hợp lý dựa trên những gì bạn biết về chủ đề đang được phân tích không? 4. Ý nghĩa của việc phân tích có hợp lý không dựa trên những gì bạn biết về chủ đề đang được đề cập? đã phân tích? 5. Bản phân tích có giải quyết được nhu cầu/mối quan tâm của các bên liên quan không?**

**EX 8.7 (LO 3) Kiểm toán Hệ thống thông tin kế toán Giải thích tính hợp lý của Phân tích dữ liệu mục nhật ký Bạn là cộng tác viên kiểm toán chịu trách nhiệm kiểm toán các mục nhật ký cho một khách hàng của công ty đại chúng. Một phần của thủ tục kiểm toán là phân tích hoạt động ghi nhật ký để xác định bất kỳ hoạt động bất thường nào. Bạn đã chuẩn bị bản phân tích sau đây về hoạt động ghi nhật ký. Nó cho thấy tổng số tiền đô la, số tiền trung bình và tổng số mục nhật ký được thực hiện tự động bởi hệ thống kế toán và được thực hiện bởi ba nhân viên chủ chốt tại khách hàng của bạn. $0 200.000 USD 400.000 USD 600.000 USD 800.000 USD 1.000.000 USD 1.200.000 USD 1.400.000 USD 1.600.000 USD 1.800.000 USD 0 500 1.000 1.500 2.000 2.500 3.000 3.500 1.500 3.000 tạp chí Bài dự thi nhân viên 1.200 10 500 tự động Phân tích mục nhật ký - Theo nhân viên Patel Trần Smith Jones Số tiền ghi nhật ký trung bình Tổng số tất cả các mục tạp chí đã đăng Tổng số mục tạp chí 1. Dữ liệu được sử dụng trong phân tích có hợp lý với câu hỏi/mục tiêu phân tích không? 2. Phương pháp phân tích có hợp lý với câu hỏi/mục tiêu phân tích không? 3. Kết quả phân tích có hợp lý dựa trên những gì bạn biết về chủ đề đang được phân tích không? 4. Ý nghĩa của việc phân tích có hợp lý không dựa trên những gì bạn biết về chủ đề đang được đề cập? đã phân tích? 5. Phân tích có giải quyết được câu hỏi/mục tiêu của phân tích không?**

Chương 8 Diễn giải kết quả phân tích dữ liệu

**EX 8.8 (LO 3) Kế toán quản trị Giải thích tính hợp lý của dự báo doanh thu Phân tích Super Scooters đang xem xét loại bỏ mẫu xe tay ga Celeritas và mở rộng cung cấp xe tay ga chạy bằng điện để tận dụng nhu cầu thị trường đang thay đổi. Bạn đã có được thông tin sau thông tin hạ thấp: • Thị trường xe máy điện đang phát triển nhanh chóng do sự gia tăng các chương trình chia sẻ xe máy. • Celeritas là chiếc xe tay ga chạy bằng xăng duy nhất mà Super Scooters sản xuất. • Các mẫu Lazer và Captain là xe tay ga chạy bằng điện, trong khi mẫu Kicks là xe sản xuất xe tay ga đồng minh. Nhóm phân tích của bạn đã chuẩn bị hình ảnh trực quan này để góp phần vào quá trình ra quyết định. Lazer 0 1.000 Tháng 11 2022 tháng 5 2023 tháng 5 2024 Tháng 11 2023 Tháng 11 2024 tháng 5 2025 Tháng 11 2025 tháng 5 2026 Tháng 11 2026 2.000 cú đá 0 1.000 2.000 Celeritas 0 1.000 2.000 người mẫu thuyền trưởng 0 1.000 2.000 Dự báo siêu xe tay ga năm 2026 - Khối lượng bán hàng (Chiếc) Tháng và Năm 1. Dữ liệu được sử dụng trong phân tích có hợp lý không đưa ra câu hỏi/mục tiêu của phân tích? 2. Phương pháp phân tích có hợp lý không? câu hỏi/mục tiêu của việc phân tích? 3. Kết quả phân tích có hợp lý không đưa ra những gì bạn biết về chủ đề này đã phân tích? 4. Ý nghĩa của việc phân tích có phải là lý do- có thể đưa ra những gì bạn biết về chủ đề này đang được phân tích? 5. Phân tích có giải quyết được nhu cầu/mối quan tâm không của các bên liên quan?**

**EX 8.9 (LO 3) Dữ liệu Kế toán tài chính Kế toán quản trị Đánh giá Phân tích dữ liệu về Bán hàng Với tư cách là nhà phân tích tài chính cho Super Scooters, bạn phải đánh giá phân tích sau đây được chuẩn bị bởi nhóm phân tích dữ liệu sử dụng bộ dữ liệu Super Scooters. Phân tích báo cáo tổng số tiền bán hàng cho từng mẫu mà công ty bán ra. Dựa trên phân tích, có vẻ như Captain là người được yêu thích nhất mô hình và Kicks là mô hình ít phổ biến nhất. thuyền trưởng Celeritas cú đá Lazer Tổng cộng người mẫu Tổng Tổng bán hàng $4,792,338 $12,324,133 $ 1,108,183 $ 27,147,407 $8,922,753 1. Phân tích có xác nhận nhiều nhất và ít nhất không mô hình phổ biến? Tại sao hoặc tại sao không? 2. Bạn có nghĩ cần phân tích thêm không? 3. Nếu có, bạn sẽ phân tích thêm những gì muốn xem trước khi quyết định mô hình nào là phổ biến nhất?**

Bài tập

**EX 8.10 (LO 3) Dữ liệu Kế toán quản trị Đánh giá Quản lý phân tích xu hướng bán hàng tại Công ty Phiêu lưu Ngoài trời Hoa Kỳ muốn hiểu khu vực nào đang hoạt động tốt nhất và liệu có xu hướng bán hàng qua các năm trong khu vực. Nhóm của bạn đã phân tích doanh số bán hàng và chuẩn bị một báo cáo trực quan hóa bằng cách sử dụng tệp Tableau của Công ty Phiêu lưu Ngoài trời Hoa Kỳ. 2022 Vùng Doanh số khu vực hàng năm $156,332 $102,874 $103,838 $128,680 $103,846 $147,883 2023 2024 2025 miền Trung Đông miền Nam Tây $71,301 $139,766 $180,529 $147,429 $93,539 $186,976 $213,239 $147,098 $122,977 $250,633 $0 300.000 USD 1. Phân tích có giải quyết được mục tiêu không? tại sao hoặc tại sao không? 2. Bạn có nghĩ cần phân tích thêm không? 3. Nếu có, bạn sẽ phân tích thêm những gì muốn xem trước khi quyết định khu vực nào hoạt động tốt nhất?**

**EX 8.11 (LO 4) Kế toán quản trị Giải thích phân tích tương quan All Care Hospital sẽ muốn hiểu rõ hơn về các yếu tố chi phí của tổng chi phí. Bước đầu tiên họ đã chuẩn bị một mối tương quan phân tích để xác định các yếu tố có tương quan với tổng chi phí. Trình điều khiển chi phí Giường Ngoại trú Lượt truy cập Sinh Gen Med / Phẫu thuật hay không Tổng cộng chi phí Giường 1 Thăm khám ngoại trú 0.61584604 1 Sinh 0.66665244 0.496333644 1 Gen Med / Phẫu thuật hay không 0.25764602 0.322183655 0.359453 1 Tổng chi phí 0.77739236 0.782692108 0,62695 0.249571064 1 Giải thích mối tương quan: 1. Thăm khám ngoại trú và tổng chi phí 2. Số giường và tổng chi phí 3. Số giường và số ca sinh**

**EX 8.12 (LO 4) Kế toán tài chính Diễn giải số liệu thống kê mô tả Bạn là nhà phân tích tài chính tại chuỗi khách sạn Denton Hospitality. Bạn đã được yêu cầu cung cấp sự hiểu biết tốt hơn về lợi nhuận của họ từ năm vừa qua. Nhóm phân tích dữ liệu của bạn đã chuẩn bị hai bản phân tích. Đầu tiên là một biểu đồ phân tán hiển thị tổng lợi nhuận hàng năm cho mỗi khách sạn. Thứ hai là phân tích thống kê mô tả về lợi nhuận trong năm qua. $0 200.000 USD 400.000 USD 600.000 USD 800.000 USD 1.000.000 USD 1.200.000 USD 1.400.000 USD –$200,000 –$400,000 Lợi nhuận hàng năm theo khách sạn Cho thuê phòng hàng năm Lợi nhuận 10K 0 20K 30K 40K 50K 60K Lợi nhuận Nghĩa là trung bình Lỗi chuẩn Đếm Chế độ Độ lệch chuẩn Phương sai mẫu Kurtosis Độ lệch Phạm vi tối thiểu Tối đa Tổng 309.049,66 95.511.689.341,06 0,07 0,00 1.472.109,00 (224.305,00) 1.247.804,00 26.289.170,25 547.691,05 553.868,00 44.607,48 48:00 #N/A 1. Giải thích số liệu thống kê mô tả sau: một. Nghĩa là b. trung bình c. Độ lệch chuẩn 2. Biểu đồ phân tán có hỗ trợ giải thích của bạn về số liệu thống kê mô tả không? Tại sao hoặc tại sao không?**

Chương 8 Diễn giải kết quả phân tích dữ liệu

**EX 8.13 (LO 4) Dữ liệu Kế toán tài chính Kế toán quản trị Diễn giải Mô tả Phân tích Bạn là nhà phân tích tài chính của One Stop Shop, một nhà phân phối bán buôn các sản phẩm tiêu dùng. uct đến các cửa hàng tiện lợi. Công ty hoạt động ở Canada, Mexico và Hoa Kỳ. Cửa hàng một cửa có hai kênh bán hàng: • Bán hàng trực tuyến được thực hiện thông qua trang web One Stop Shop. • Bán hàng ngoại tuyến được thực hiện trực tiếp với đại diện bán hàng của One Stop Shop. One Stop Shop muốn đánh giá liệu họ có nên chuyển sang chỉ bán hàng trực tuyến hay không. Họ tin điều này sẽ tiết kiệm được một khoản tiền đáng kể vì họ sẽ không cần nhiều đại diện bán hàng và sẽ không phải trả hoa hồng bán hàng. Sau đây là bản phân tích do One Stop Shop chuẩn bị bằng cách sử dụng One Tập dữ liệu Stop Shop. Canada Ngoại tuyến trực tuyến Tổng cộng Nhãn hàng Tổng của Tổng số bán hàng 392.731.724 USD $788,914,146 $ 396,182,421 México $710,979,369 Ngoại tuyến 400.360.732 USD trực tuyến $ 310,618,637 Hoa Kỳ $ 1,452,693,443 Ngoại tuyến $720,489,036 trực tuyến $732,204,407 $ 2,952,586,958 1. Bảng tổng hợp cung cấp thông tin gì cho One Stop Shop? 2. One Stop Shop nên xem xét những phân tích bổ sung nào?**

**EX 8.14 (LO 4) Kế toán tài chính Kế toán quản trị Giải thích Phân tích chẩn đoán- ics Đội ngũ quản lý tại One Stop Shop muốn biết liệu doanh số bán hàng có theo mùa hay không. các nhóm phân tích dữ liệu đã chuẩn bị hình dung sau đây. Q1 $0 50.000.000 USD 100.000.000 USD 150.000.000 USD 200.000.000 USD 250.000.000 USD Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 2022 2023 2024 2025 Tổng doanh thu Năm Tổng cộng 1. Phân tích có giải quyết được mục tiêu không? Tại sao hoặc tại sao không? 2. Những phân tích bổ sung nào có thể được thực hiện để xác định mô hình bán hàng?**

Bài tập

**EX 8.15 (LO 4) Dữ liệu Kiểm toán Diễn giải Phân tích mô tả Nhóm phân tích dữ liệu của bạn có cho bạn, một kiểm toán viên bên ngoài đang kiểm tra các giao dịch bán hàng cho các cửa hàng Outdoor Adventure ở Hoa Kỳ, một bản phân tích bao gồm độ lệch chuẩn cho doanh số bán hàng từ năm 2022 đến năm 2025. Họ cũng cung cấp cho bạn một biểu đồ bán hàng phân tán.**

Thống kê mô tả Bán hàng 2022 – 2025 Đếm Nghĩa là Chế độ trung vị Phương sai mẫu Độ lệch chuẩn Tối đa tối thiểu 9.994,00 229,86 12,96 54,49 388.434,46 623,25 22.638,48 0,44 5.000 USD $0 10.000 USD 15.000 USD 20.000 USD 25.000 USD 0 1.000 2.000 3.000 4.000 5.000 6.000 7.000 8.000 9.000 10.000 Giao dịch bán hàng phiêu lưu ngoài trời ở Hoa Kỳ 2022―2025 bán hàng (tính bằng nghìn) Giao dịch $22,638.48 Người chuẩn bị bản phân tích đã sử dụng tất cả dữ liệu giao dịch bán hàng và thống nhất tổng doanh số bán hàng trong hồ sơ của họ cho mục hàng bán hàng trong sổ cái chung.

1. Giải thích phương sai và độ lệch chuẩn về doanh số bán hàng của Cửa hàng Phiêu lưu Ngoài trời ở Hoa Kỳ.

2. Biểu đồ phân tán có hỗ trợ cho lời giải thích của bạn không độ lệch chuẩn? Tại sao hoặc tại sao không?

3. Sử dụng tệp dữ liệu được cung cấp để tạo lại phân tích. EX 8.16 (LO 5) Kế toán tài chính Kế toán quản trị Diễn giải phân tích hồi quy- sis Denton Hospitality Inc. đã thuê công ty tư vấn của bạn để đánh giá và quản lý dòng tiền. cụ thể- Cụ thể, bạn đã được yêu cầu xây dựng một mô hình hợp lệ và đáng tin cậy để dự đoán tổng chi phí để ban quản lý có thể quản lý dòng tiền tốt hơn. Bạn và nhóm của bạn đã chuẩn bị hồi quy sau đây. Nhiều R R vuông Hình vuông R đã điều chỉnh Lỗi chuẩn Quan sát ANOVA 0.810435721 0.656806059 0.62160668 79.448.54158 44 df SS MS F 4,71E+11 2,46E+11 Hồi quy dư Tổng cộng 4 39 43 7.17E+11 1,18E+11 6.31E+09 18.65959 1.211E–08 121071.9 587.7595 Đánh chặn Số phòng Số giờ đã làm việc, GM Giờ làm việc, dọn phòng Giờ làm việc, Lễ tân (131.136,43) 2.670,21 29h30 52.01 13:41 9.270823 18.93043 2.747581 4.683324 2.862522 3.160299 −1,08313 4.543032 0,003044 0,009043 0,006728 5,23E−05 0.285403 Ý nghĩa F Hệ số lỗi chuẩn t Thống kê giá trị P TÓM TẮT ĐẦU RA Hospitality, Inc – Mô hình dự đoán tổng chi phí Thống kê hồi quy

1. Giải thích số liệu thống kê hồi quy.

2. Giải thích liệu mô hình có ý nghĩa hay không.

3. Các hệ số của mô hình là gì?

4. Các biến sử dụng trong mô hình có tạo ra ý nghĩa? Tại sao hoặc tại sao không?

5. Xác định các biến khác có thể cải thiện mô hình.

6. Sử dụng mô hình để dự đoán chi phí cho một khách sạn với các đặc điểm sau: • Khai trương vào năm 1975 • 150 phòng • 9.200 giờ làm việc – Quầy lễ tân • 1.500 giờ làm việc – GM • 12.100 giờ làm việc – Dọn phòng • Địa điểm = Sân bay Chương 8 Diễn giải kết quả phân tích dữ liệu EX 8.17 (LO 5) Dữ liệu Kế toán quản lý Diễn giải Phân tích độ nhạy Super Scooters là chuẩn bị dự báo doanh thu cho năm tiếp theo. Dựa trên dữ liệu của năm hiện tại, bạn đã thực hiện ba độ nhạy phân tích: • Trường hợp tốt nhất: Chi phí biến đổi sẽ giảm 5%. • Kịch bản có thể xảy ra: Chi phí biến đổi sẽ tăng 2%, • Trường hợp xấu nhất: Biến sẽ tăng 7%. Việc tính toán doanh thu thuần hiện tại được cung cấp. Tổng doanh thu Tổng chi phí biến đổi Ký quỹ đóng góp Tổng chi phí cố định Doanh thu thuần 5.722.777 2025 $12,165,162 $ $ $ $ 6.442.385 4.745.563 1.696.822 Phân tích trường hợp tốt nhất, trường hợp có thể xảy ra và trường hợp xấu nhất được cung cấp. Super Scooters kỳ vọng doanh số duy trì ổn định trong năm tới. Trường hợp tốt nhất $12,165,162 $ $ $ $ 6.008.916 6.156.246 1.696.822 trường hợp có thể xảy ra 4.459.424 $12,165,162 $ $ $ $ 5.837.232 6.327.930 1.696.822 4.631.108 $12,165,162 $ $ $ $ 6.123.371 6.041.791 1.696.822 4.344.969 Trường hợp xấu nhất Tổng doanh thu Tổng chi phí biến đổi Ký quỹ đóng góp Tổng chi phí cố định Doanh thu thuần Tạo lại phân tích what-if và trả lời các câu hỏi:

1. Câu hỏi/mục tiêu của việc phân tích là gì?

2. Mô hình có đo lường được những gì nó được cho là không để đo?

3. Các thước đo của mô hình có chính xác và không? nhất quán? EX 8.18 (LO 5) Dữ liệu Kế toán quản lý Diễn giải Phân tích tìm kiếm mục tiêu Ngoài trời Hoa Kỳ Adventure Sales đã yêu cầu nhóm kế toán của bạn xác định doanh số hòa vốn cho sản phẩm lều của họ. Nhóm đã thảo luận các phương pháp tiềm năng để ước tính doanh thu hòa vốn và xác định rằng Goal Seek là phương pháp hiệu quả nhất. Đội ngũ bán hàng đã cung cấp cho bạn thông tin về giá cả và chi phí: • Giá bán = $70 • Chi phí biến đổi trên mỗi đơn vị = $25 • Chi phí cố định = 10.000 USD Với mô hình bảng tính được sử dụng để tính toán lợi nhuận bằng cách sử dụng dữ liệu này, hãy sử dụng Goal Seek để trả lời các câu hỏi sau: hạ thấp câu hỏi.

1. Số lượng đơn vị hòa vốn là bao nhiêu cần thiết?

2. US Outdoor Adven- bán để kiếm được lợi nhuận 100.000 USD?

3. Bạn sẽ xác minh tính hợp lệ và độ tin cậy bằng cách nào? khả năng của mô hình và kết quả của mô hình? EX 8.19 (LO 5) Dữ liệu Kế toán tài chính Diễn giải Phân tích dự đoán Bạn là một chuyên gia tài chính nhà phân tích tại Best Bakes Bakery. Người quản lý của bạn đã yêu cầu bạn xây dựng một mô hình để dự đoán doanh số bán hàng cho năm 2026 bằng cách sử dụng dữ liệu bán hàng từ năm 2022 đến năm 2025. Sau đây là phương trình đường xu hướng sử dụng các biến tổng doanh thu trong USD và tháng bán. Tổng doanh thu = $74.739,90 – ($1,56 × Tháng bán hàng). Thống kê mô hình bao gồm: R bình phương = 0,0487 giá trị p là 0,1406 Phương trình đường xu hướng được sử dụng để phát triển hình dung sau. Tháng và năm bán hàng đang diễn ra trục x và tổng doanh thu nằm trên trục y.

Bài tập 20.000 USD 19.000 USD 18.000 USD 17.000 USD 16.000 USD 15.000 USD 14.000 USD 13.000 USD 12.000 USD 11.000 USD 10.000 USD 9.000 USD 8.000 USD 7.000 USD 6.000 USD 5.000 USD 4.000 USD 3.000 USD 2.000 USD 1.000 USD $0 Tháng mười hai 2021 Tổng bán hàng Tháng Tư. Tháng 8 2022 Tháng mười hai Tháng Tư. Tháng 8 2023 Tháng mười hai Tháng Tư. Tháng 8 2024 Tháng mười hai Tháng mười hai Tháng Tư. Tháng 8 2025 Xu hướng bán hàng bánh nướng tốt nhất Kiểm tra phân tích trong tệp dữ liệu được cung cấp và diễn giải phân tích xu hướng bán hàng.

1. Câu hỏi/mục tiêu của việc phân tích là gì?

2. Mô hình và hình ảnh trực quan có cung cấp đủ thông tin để giải quyết vấn đề đó không?

3. Các biến của mô hình có hợp lệ không? EX 8.20 (LO 5) Kế toán tài chính Kế toán quản trị Diễn giải phân tích hồi quy- sis Bạn được yêu cầu xây dựng một mô hình để dự đoán doanh thu tại U.S. Outdoor Adventures. Ban quản lý tin rằng khu vực, tỷ lệ chiết khấu và số tiền chiết khấu là những yếu tố dự báo tốt về doanh số bán hàng. Bạn đã sử dụng dữ liệu trong tệp hồi quy để chuẩn bị phân tích hồi quy sau. Nhiều R 0,6260322 0.3919164 0.391612 486.1264 9994 221.75141 12.60104565 17.5978578 2.7291E-68 –438.73427 2.4154052 1521272575 2360352937 3881625512 9988 9993 304254515 1287.47445 0,00 236318.876 0.1232541 –17.727807 18.590415 24.64841598 0,030141825 15.12802917 14.84929891 15.9032368 –17.799694 80.1346697 0,0081474 –1.1938481 1.16897054 8.4529E-70 0,00 0.99349955 0.23256576 0.2424434 5 R vuông Hình vuông R đã điều chỉnh Lỗi chuẩn Quan sát ANOVA dư Hồi quy Tổng cộng Đánh chặn Giảm giá Giảm giá $ Vùng Tây Vùng Đông Vùng Miền Trung TÓM TẮT ĐẦU RA Thống kê hồi quy hệ số df SS MS F Ý nghĩa F Lỗi chuẩn t Thống kê giá trị P

1. Giải thích số liệu thống kê hồi quy.

2. Mô hình có ý nghĩa không? Tại sao hoặc tại sao không?

3. Các hệ số của mô hình là gì?

4. Các biến sử dụng trong mô hình có tạo ra ý nghĩa? Tại sao hoặc tại sao không?

5. Xác định các biến khác có thể cải thiện mô hình.

6. Dựa trên mô hình này, dự đoán là gì? bán khi tỷ lệ chiết khấu là 20%, bán hàng ở khu vực phía tây và giảm giá số tiền đô la là 100?

Chương 8 Diễn giải kết quả phân tích dữ liệu Vấn đề

**PR 8.1 (LO 1) Dữ liệu Kế toán tài chính Diễn giải Quản lý phân tích mô tả tại U.S. Outdoor Adventures đang đánh giá chính sách vận chuyển của họ tới khách hàng. Hiện nay công ty đang cung cấp miễn phí vận chuyển, nhưng họ đang xem xét tính phí vận chuyển cho khách hàng. Ban quản lý muốn đặt cược- ter hiểu chi phí vận chuyển đang thay đổi như thế nào và liệu có mối quan hệ giữa loại tàu- phương thức ping và mức độ ưu tiên thứ tự. Sản phẩm được vận chuyển ở hạng nhất, cùng ngày, hạng hai hoặc hạng tiêu chuẩn. Phương pháp của việc vận chuyển do khách hàng quyết định nhưng thường liên quan đến mức độ ưu tiên của đơn hàng. Các hạng mục ưu tiên là quan trọng, thấp, cao hoặc trung bình. Nhóm phân tích dữ liệu đã cung cấp các phân tích mô tả sau đây, chỉ ra rằng tổng số tàu chi phí ping tăng từ năm 2022 lên năm 2025. Họ cũng chuẩn bị phân bổ tần suất số lượng các lô hàng theo mức độ ưu tiên và phương thức vận chuyển cho các năm 2022, 2023, 2024 và 2025 cộng lại. Hạng nhất Cùng ngày hạng hai Hạng nhất Cùng ngày hạng hai Lớp tiêu chuẩn Hạng nhất Cùng ngày hạng hai Lớp tiêu chuẩn Lớp tiêu chuẩn 912 116 495 432 703 273 744 340 154 289 1.349 Tổng cộng 2025 2024 2023 2022 49.769,30 50.198,57 60.925,19 77.280,73 $ 238.173,79 Tổng cộng 9,994 Năm Tổng chi phí vận chuyển Chi phí vận chuyển mỗi năm Số lượng lô hàng 783 Quan trọng 3.069 432 5.710 4.187 Cao Thấp Trung bình Ưu tiên và Chế độ vận chuyển $ $ $ $ Số lượng lô hàng theo Chế độ vận chuyển 1. Xác định những điều sau đây: một. Các bên liên quan là ai? b. Mục đích của việc phân tích là gì? c. Có những cách giải thích khác hoặc phân tích? d. Có bất kỳ rủi ro nào cần phải có được xem xét? đ. Người chuẩn bị cần có kiến thức gì và người phiên dịch có kiến thức gì cần hiểu phân tích? f. Bạn có thể sử dụng kinh nghiệm trước đây của mình như thế nào hoặc áp dụng kinh nghiệm này vào các phân tích trong tương lai thông qua sự tự suy nghĩ? 2. Dữ liệu được sử dụng trong phân tích có hợp lý với câu hỏi/mục tiêu phân tích không? 3. Phương pháp phân tích có hợp lý với câu hỏi/mục tiêu phân tích không? 4. Kết quả phân tích có hợp lý với những gì đã biết về đối tượng đang được phân tích không? 5. Ý nghĩa của việc phân tích có hợp lý không dựa trên những gì bạn biết về chủ đề đang được đề cập? đã phân tích? 6. Bản phân tích có giải quyết được nhu cầu/mối quan tâm của các bên liên quan không? 7. Chuẩn bị một phân tích mô tả bổ sung để giúp Cuộc phiêu lưu ngoài trời của Hoa Kỳ hiểu được chi phí liên quan đến từng phương thức vận chuyển. Giải thích phân tích của bạn.**

**PR 8.2 (LO 1, 2, 3, 5) Dữ liệu Kế toán tài chính Kế toán quản trị Diễn giải dự đoán- tive Analysiss All Care Hospital, nơi điều hành 2.000 bệnh viện ở Hoa Kỳ, đang chuẩn bị ngân sách hoạt động của họ cho năm 2026. Ban quản lý điều hành muốn hiểu các yếu tố thúc đẩy tổng chi phí. Là thành viên của nhóm phân tích dữ liệu ở phòng kế toán, bạn được yêu cầu chuẩn bị và giải thích các phân tích dữ liệu nhằm cung cấp cho ban quản lý thông tin về toàn bộ bệnh viện chi phí.**

Vấn đề Nhóm phân tích dữ liệu đã cung cấp các phân tích mô tả tóm tắt số lượng bệnh viện ở mỗi vùng và tổng chi phí bệnh viện theo vùng. Vào năm 2025, tổng chi phí cho Tất cả các Bệnh viện Chăm sóc là $386,8 triệu. Họ cũng cung cấp cho bạn tệp dữ liệu thô. Số lượng bệnh viện Vùng Tổng cộng Tây Bắc Trung Bộ Đông Bắc Trung Bộ Trung Đại Tây Dương Đông Nam Trung Bộ nước Anh mới Núi Nam Đại Tây Dương Thái Bình Dương Tây Nam Trung Bộ 214 262 168 136 100 160 252 259 449 2.000 Vùng Tổng chi phí theo khu vực-2025 $52,941,169 $19,037,967 $60,506,505 $26,438,517 Đông Bắc Trung Bộ Đông Nam Trung Bộ Trung Đại Tây Dương Núi 19 triệu 71 triệu $25,634,270 $71,210,066 $57,893,598 nước Anh mới Thái Bình Dương Nam Đại Tây Dương $26,015,206 $47,082,098 Tây Bắc Trung Bộ Tây Nam Trung Bộ Tổng chi phí Theo ban quản lý, các biến sau đây là yếu tố dự báo tổng chi phí bệnh viện: nhập viện, điều tra dân số, thăm khám ngoại trú, sinh nở, chi phí tiền lương, nhân sự và có sinh con hay không. các nhóm phân tích đã chuẩn bị một mô hình hồi quy sử dụng các biến đó với kết quả đầu ra như sau. Nhiều R 0.982051941 0.964426014 0.964301005 61360.99522 2000 –4191.07786 2275.171 –1.84209 0,06561006 6.013726131 –57.72122789 2.03E+14 7,5E+12 2.11E+14 1992 1999 2.9E+13 7714.85352 0 3,77E+09 –0,019727175 –9.977260409 1.804388653 30.9359429 –5932.874462 2.697418 3329.682 0.387068 19.55346 0,009985 1.656594 0,036122 15.5366 –2.95197 –1.97573 –6.02276 49.95226 11.46872 –1.78181 1.8108E-51 0,00319445 0,04832264 2.0367E-09 0,00000000 1.5657E-29 0,07493183 –8653.042868 5.254624717 –96.06861315 –0.039308781 –13.22609855 1.733547274 25.64588566 –12462.8985 270.8871 6.772828 –19.3738 –0,00015 –6.72842 1.87523 36.226 597.1496 –8653.04 5.254625 –96.0686 –0,03931 –13.2261 1.733547 25.64589 –12462.9 270.8871 6.772828 –19.3738 –0,00015 –6.72842 1.87523 36.226 597.1496 7 R vuông Hình vuông R đã điều chỉnh Lỗi chuẩn Quan sát ANOVA dư Hồi quy Tổng cộng Đánh chặn tuyển sinh điều tra dân số Thăm khám ngoại trú Sinh Chi phí tiền lương nhân sự Sinh hay không TÓM TẮT ĐẦU RA Thống kê hồi quy hệ số df SS MS F Ý nghĩa F Lỗi chuẩn t Thống kê giá trị P Thấp hơn 95% Trên 95% Thấp hơn 95% Trên 95%

1. Xác định những điều sau đây: một. Các bên liên quan là ai? b. Mục đích của việc phân tích là gì? c. Có những cách giải thích khác hoặc phân tích? d. Có bất kỳ rủi ro nào cần được xem xét? đ. Người chuẩn bị cần có kiến thức gì và người phiên dịch có kiến thức gì cần hiểu phân tích? f. Bạn có thể sử dụng kinh nghiệm trước đây của mình như thế nào hoặc áp dụng kinh nghiệm này vào các phân tích trong tương lai?

2. Sử dụng Kết quả Tóm tắt cho các mục sau: một. Giải thích số liệu thống kê hồi quy. b. Mô hình có ý nghĩa không? Tại sao hoặc tại sao không? c. Xác định các hệ số của mô hình. d. Các biến được sử dụng trong mô hình có làm ý nghĩa? Tại sao hoặc tại sao không? đ. Xác định các biến khác có thể cải thiện mô hình.

3. Chuẩn bị mô hình hồi quy dự đoán tổng chi phí sử dụng các biến: nhập viện, ngoại trú thăm viếng, sinh nở và nhân sự. Một. Mẫu này có tốt hơn mẫu trước không người mẫu? b. Giải thích số liệu thống kê hồi quy và các hệ số của mô hình.

CHƯƠNG 8 Diễn giải kết quả phân tích dữ liệu Trường hợp ứng dụng chuyên nghiệp: Ortho Inc. Data Ortho Inc. là nhà sản xuất thiết bị y tế có trụ sở tại San Diego, California. Công ty ủng hộ sản xuất và bán các thiết bị cấy ghép thay thế đầu gối được sản xuất theo yêu cầu:

- Đây là một công ty tư nhân và nộp báo cáo tài chính dựa trên GAAP của Hoa Kỳ cho ngân hàng của mình như một phần các hợp đồng nợ của nó.

- Ban giám đốc rất quan tâm và tiếp tục nhấn mạnh tầm quan trọng của việc thiết kế tốt và kiểm soát nội bộ hiệu quả.

- Ortho là một tổ chức phi tập trung, có 5 địa điểm sản xuất và bán hàng trên khắp Hoa Kỳ Các bang sử dụng tổng cộng 28 giám đốc sản phẩm và 29 giám đốc bán hàng. Mỗi trang web hoạt động độc lập và chịu trách nhiệm thu mua nguyên liệu thô, sản xuất và bán hàng thành phẩm trong khu vực địa lý của mình. Người quản lý bán hàng duy trì khách hàng của riêng họ mối quan hệ, trong khi người quản lý sản phẩm giám sát mức tồn kho và đặt hàng nguyên liệu thô cần thiết.

- Silicon và thạch cao được sử dụng để làm khuôn cho tất cả các sản phẩm thay thế đầu gối của công ty. các vật liệu đổ vào khuôn khác nhau tùy theo sản phẩm – một số là kim loại, một số là nhựa và một số là gốm sứ. Công ty đã đầu tư đáng kể vào việc phát triển và duy trì hệ thống thông tin của mình hệ thống thu thập và báo cáo dữ liệu đầy đủ và chính xác. Ban quản lý công ty sử dụng dữ liệu được thu thập trong hệ thống thông tin để tạo báo cáo và hỗ trợ ra quyết định. Từ điển dữ liệu bao gồm dữ liệu phù hợp nhất được sử dụng bởi ban quản lý, kế toán viên, kiểm toán viên và các chuyên gia khác. BẢNG SẢN PHẨM Tên Khóa chính Định nghĩa Danh mục sản phẩm Cấy ghép đầu gối liên tục sản phẩm ✓ Mã nhận dạng mặt hàng sản phẩm Mô tả sản phẩm Mô tả sản phẩm Lưu ý: Bảng Product Master chứa thông tin về các sản phẩm khác nhau được bán bởi Ortho. Từ điển dữ liệu BẢNG CHẤT LIỆU Tên Khóa chính Định nghĩa Danh mục vật liệu Nguyên liệu thô ghi rõ liên tục Chất liệu ✓ Mã định danh vật liệu Chất liệuMô tả Mô tả vật liệu Lưu ý: Bảng Material Master chứa thông tin về các nguyên liệu thô khác nhau được Ortho mua. BẢNG GIAO DỊCH Tên Khóa chính Định nghĩa Loại chuyển đổi ✓ Cho biết loại giao dịch (O cho đơn hàng và S cho bán hàng) Chuyển số ✓ Mã nhận dạng cho đơn đặt hàng và bán hàng Mã trang web Trang web giao dịch (một trong năm địa điểm) Người quản lý Nhân viên liên quan đến giao dịch ID thực thể Nhà cung cấp/Khách hàng liên quan đến giao dịch số lượng Số lượng giao dịch Trường hợp ứng dụng chuyên nghiệp: Ortho Inc. Đơn vị Đơn vị giao dịch (lb hoặc kg đối với đơn hàng, ea đối với doanh số bán hàng) Đơn vịGiá Giá mỗi đơn vị Chuyển đổi ngày Ngày đặt hàng mua/bán Ngày hoàn thành Ngày giao/nhận (bán hàng/đơn hàng) Mục Nguyên liệu được mua hoặc sản phẩm được bán Tạo bởi Nguồn dữ liệu (ví dụ: lô hàng ngày) Tổng phụ Tổng giao dịch trước thuế (Đơn giá * Số lượng) Thuế Số tiền thuế Lưu ý: Bảng Giao dịch chứa sự kết hợp của các giao dịch đơn đặt hàng, đơn đặt hàng và giao dịch bán hàng trả lại BẢNG TRANG WEB Tên Khóa chính Định nghĩa Mã trang web ✓ Được xác định cho các trang web của công ty (năm chữ viết tắt của tiểu bang) Tên trang web Tên của trang web (tiểu bang) Lưu ý: Bảng Site chứa tên của từng site, là tên của tiểu bang nơi đặt site đó. BẢNG NHÂN VIÊN Tên Khóa chính Mô tả ID nhân viên ✓ Mã định danh nhân viên Tên đầu tiên Họ tên nhân viên Họ Họ của nhân viên Mã trang web Địa điểm công ty được xác định (tiểu bang) Vị trí Vị trí nhân viên Phê duyệt đơn hàng Thẩm quyền phê duyệt đơn đặt hàng của nhân viên Lưu ý: Bảng Nhân viên chính chứa thông tin về nhân viên liên quan đến đơn đặt hàng và đơn đặt hàng. theo đuổi các giao dịch đặt hàng, ví dụ: người quản lý sản phẩm và bán hàng. BẢNG THỰC THỂ Tên Khóa chính Mô tả ID thực thể ✓ Mã định danh thực thể (nhà cung cấp/khách hàng/Ortho, Inc.) Mã trang web Cho biết trang Ortho nào mà thực thể được liên kết với Tên thực thể Tên công ty thực thể Tên liên hệ Tên liên hệ của thực thể Tên liên hệ Họ liên hệ của thực thể Điện thoại Điện thoại thực thể Email Email thực thể Địa chỉ đường phố Địa chỉ đường phố của thực thể Thành phố Thành phố thực thể tiểu bang Trạng thái thực thể Mã zip Mã zip thực thể Loại thực thể Loại thực thể (“S” dành cho khách hàng và “O” dành cho nhà cung cấp)

Chương 8 Diễn giải kết quả phân tích dữ liệu Sơ đồ mối quan hệ thực thể (ERD) Bậc thầy sản phẩm sản phẩm Danh mục vật liệu Chất liệuMô tả Danh mục sản phẩm Mô tả sản phẩm Bậc thầy vật chất Trang web Mã trang web Tên trang web Thạc sĩ nhân viên ID nhân viên Tên đầu tiên Họ Mã trang web Vị trí Phê duyệt đơn hàng Chủ thể thực thể ID thực thể Mã trang web Tên thực thể Tên liên hệ Tên liên hệ Điện thoại Email Địa chỉ đường phố Thành phố tiểu bang Mã zip Loại thực thể Giao dịch Loại chuyển đổi Chuyển số Mã trang web Người quản lý ID thực thể số lượng Đơn vị Đơn vịGiá Chuyển đổi ngày Ngày hoàn thành Mục Tạo bởi Tổng phụ Thuế 1 1 1 N N N 1 1 N Chất liệu (Lưu ý: ERD cho biết bảng nào sẽ tham gia và cột nào sẽ sử dụng trong các liên kết.) Sơ đồ mối quan hệ thực thể (ERD) hiển thị mối quan hệ giữa các bảng trong thông tin hệ thống. Báo cáo thu nhập so sánh thể hiện thu nhập cho năm 2024 và 2025. Báo cáo thu nhập so sánh của Ortho Inc. Báo cáo thu nhập so sánh $ tính bằng triệu 2024 (đã kiểm toán) 2025 (chưa được kiểm toán) Doanh thu thuần $913 $854 Chi phí bán hàng 579 542 Lợi nhuận gộp 334 312 Nghiên cứu và phát triển 57 59 Bán hàng, tổng hợp và hành chính 191 196 Phí thu hồi, trừ số tiền bảo hiểm 5 5 Khấu hao tài sản vô hình 3 2 Tổng chi phí hoạt động 256 262 Thu nhập hoạt động 78 50 Thu nhập khác (chi phí), ròng 1 2 Thu nhập trước thuế thu nhập 79 52 Thuế thu nhập 11 8 Thu nhập ròng $ 68 $ 44

Trường hợp ứng dụng chuyên nghiệp: Ortho Inc. Kiểm tra PAC 8.1 : Giải thích phân tích mô tả và chẩn đoán Dữ liệu Kiểm toán Bạn thuộc nhóm kiểm toán bên ngoài kiểm toán báo cáo tài chính của Ortho kể từ và cho năm kết thúc ngày 31 tháng 12 năm 2025:

- Lưu ý rằng số tiền trình bày trong báo cáo thu nhập so sánh cho năm 2024 đã được kiểm toán, trong khi số tiền được trình bày cho năm 2025 chưa được kiểm toán.

- Cho năm kết thúc ngày 31 tháng 12 năm 2024, công ty kiểm toán của bạn đã đưa ra ý kiến chấp nhận toàn phần về tình hình tài chính báo cáo chính thức và lưu ý rằng kiểm soát nội bộ của công ty đối với báo cáo tài chính là phù hợp. được thiết kế riêng và vận hành hiệu quả. Bạn đã được yêu cầu xem xét rủi ro có sai sót trọng yếu liên quan đến doanh thu thuần. Cụ thể, chuyên gia kiểm toán của bạn đã yêu cầu bạn giải thích các phân tích mô tả được cung cấp bởi phân tích dữ liệu của công ty bạn đội. Đầu ra Tableau được cung cấp. Tổng cộng 2024 Số lượng riêng biệt của tổng phụ TR TR Chuyển ngày Phân phối tần suất bán hàng Tổng phụ TR Sản phẩmMô tả sản phẩm 4.196 4.378 7.217 9,567 20,457 4.153 9,714 20.331 4.306 16.526 2025 2024 2025 Đầu gối gốm trên gốm Đầu gối bằng kim loại và Polyethylene liên kết ngang Đầu gối kim loại và nhựa Đầu gối kim loại trên kim loại (Cobalt chrome) Đầu gối kim loại trên kim loại (Thép không gỉ) Đầu gối kim loại trên kim loại (Titan) 7.208 60.424 853.505.611 60.102 16.760 113,844,112 103.546.449 185.198.302 106.320.616 145.197.885 199.398.247 107.545.175 198.397.781 116.722.920 220.828.360 116.040.741 153.572.138 913,107,114 1. Xem xét tính hợp lệ của đầu ra Tableau được cung cấp bởi công nghệ thông tin của bạn đội. Là bảng phân bố tần suất bán hàng phân tích hợp lệ và đáng tin cậy? Tại sao hoặc tại sao không? 2. So sánh cơ cấu doanh số bán hàng từ năm 2025 đến năm 2024. Kết hợp bán hàng góp phần như thế nào vào việc xem xét- đánh giá rủi ro có sai sót trọng yếu? 3. Trong quá trình thẩm vấn với phó chủ tịch bán hàng, nhóm tương tác của bạn đã biết được rằng khách hàng lớn nhất chỉ mua kim loại- các sản phẩm đầu gối bằng kim loại, và những sản phẩm này các cuộc rượt đuổi chiếm khoảng 35% tổng số việc bán các sản phẩm này. Khách hàng này có những sửa đổi đáng kể được yêu cầu gần đây hợp đồng đặt hàng và điều khoản tín dụng của họ vì lo ngại có thể phá sản. Làm thế nào thông tin này có thể kết hợp với bảng phân bố tần suất bán hàng, con- giảm thiểu rủi ro có sai sót trọng yếu? 4. Nhóm công nghệ đã cung cấp một số thông tin terplot doanh số bán hàng cho đầu gối kim loại trên kim loại (cobalt chrome) sản phẩm cho tháng Tháng Mười. Nhóm công nghệ đã xác định fied một số điểm trên sơ đồ. Giải thích Liệu mỗi điểm được xác định trên sơ đồ sẽ cần điều tra thêm, hoặc nếu chúng nên được bao gồm trong chất bình thường thử nghiệm tích cực để bán hàng. Tổng số giao dịch bán hàng 80.000 USD 60.000 USD 40.000 USD 20.000 USD $(20.000) $(40.000) $(60.000) $(80.000) Ngày 27 tháng 9 Ngày 02 tháng 10 Ngày 07 tháng 10 Ngày 12 tháng 10 Ngày 17 tháng 10 2025 Ngày 22 tháng 10 Ngày 27 tháng 10 Ngày 01 tháng 11 Ngày 06 tháng 11 $− 1 3 2 5. Sử dụng bộ dữ liệu Ortho, Inc để tạo phần bổ sung phân tích mô tả mang tính chủ quan. Xem xét việc tạo phân tích bảng chéo về doanh số bán hàng theo sản phẩm mô tả và/hoặc bán hàng theo mã trang web. Những cái này thống kê mô tả cung cấp cái nhìn sâu sắc về doanh thu thuần của công ty trong năm được kiểm toán. Mô tả phân tích của bạn và giải thích kết quả.

Chương 8 Diễn giải kết quả phân tích dữ liệu

**PAC 8.2 Kế toán quản lý: Giải thích phân tích chẩn đoán Dữ liệu Kế toán quản trị Bạn được giao nhiệm vụ tìm hiểu mối quan hệ giữa đơn đặt hàng và đơn đặt hàng để thu mua nguyên vật liệu. Hiện nay, các cơ sở sản xuất đều chịu trách nhiệm về mọi giao dịch mua hàng. Lợi ích của tổ chức phi tập trung này là các trang web có thể nhanh chóng đáp ứng những thay đổi về nhu cầu sản xuất. Nhược điểm là việc tìm nguồn cung ứng cho việc mua hàng không được phối hợp chặt chẽ. được đặt giữa các trang web. Có lo ngại rằng bộ phận mua hàng của một số trang web đã mua nhiều nguyên liệu hơn mức cần thiết. Người quản lý của bạn đã yêu cầu bạn phân tích việc mua hàng so với doanh số bán hàng. Bạn đã chuẩn bị những thứ sau phân tích. 2022 2023 2024 2025 Tháng Giêng. Tháng Tư. Tháng Bảy. Tháng Mười. Tháng Giêng. Tháng Tư. Tháng Bảy. Tháng Mười. Tháng Giêng. Tháng Tư. Tháng Bảy. Tháng Mười. Tháng Giêng. Tháng Tư. Tháng Bảy. Tháng Mười. 20.000.000 USD 40.000.000 USD 60.000.000 USD 80.000.000 USD 100.000.000 USD Đơn đặt hàng Đơn đặt hàng bán hàng Công ty Ortho Đơn đặt hàng bán hàng Vs. Đơn đặt hàng Đơn đặt hàng Mối tương quan giữa mua hàng và bán hàng Công ty Ortho Đơn đặt hàng bán hàng Đơn đặt hàng 1 0.750363942 1 Đơn đặt hàng bán hàng 1. Những phân tích này giúp đánh giá như thế nào nếu các cơ sở đang mua nhiều nguyên liệu thô hơn họ cần? 2. Liệt kê một số phân tích bổ sung có thể áp dụng hữu ích. 3. Tạo các phân tích bổ sung và giải thích kết quả.**

**PAC 8.3 Kế toán tài chính: Diễn giải phân tích mô tả Dữ liệu Kế toán tài chính Kiểm soát viên tại Ortho Inc. đã yêu cầu bạn hiểu yêu cầu- Các quy định của ASC 606 Ghi nhận doanh thu liên quan đến việc tiết lộ dữ liệu bán hàng theo địa lý hoặc sản phẩm các hạng mục. Bạn đã chuẩn bị phân tích bảng chéo cho năm 2025 và 2024 làm điểm khởi đầu cho giai đoạn tiền cắt giảm việc tiết lộ. Tổng cộng 2025 Trang web 164.530.136,81 174.888.045,18 172.934.662,11 183.493.309,15 175.041.416,59 193.364.104,19 188.249.027,51 2024 sự khác biệt CA FL IL NY TX 174.872.628,25 853.505.610,67 913.082.519,55 163.660.289,73 175.554.510,70 18.963.172,34 –1.953.383,07 168.788,34 59.576.908,88 29.703.814,46 12.694.516,81 1. Ai là bên liên quan chính của phân tích? 2. Bạn cần cung cấp những kiến thức gì một sự giải thích hợp lý của mô tả phân tích? 3. Phân tích này có đủ cho báo cáo bộ phận không? hay bạn sẽ cần phân tích bổ sung? 4. Tạo các phân tích bổ sung về kết quả theo năm.**

Trường hợp tiếp theo của Le Grind: Xác minh và giải thích phân tích lợi nhuận gộp Kế toán thuế PAC 8.4: Giải thích phân tích mô tả và chẩn đoán dữ liệu Kế toán thuế Ban quản lý của Ortho muốn xác định các cơ hội tiềm năng về chi phí tiết kiệm. Một khía cạnh của chi phí mua hàng mà ban quản lý chưa xem xét là thuế doanh thu phải trả trên mua hàng. Ban quản lý đã yêu cầu phân tích thuế bán hàng được thanh toán theo địa điểm. Với tư cách là nhân viên kế toán thuế Ortho, bạn đã chuẩn bị bản phân tích xu hướng sau đây về thuế bán hàng được thanh toán theo địa điểm. $0 0,00 1,00 2,00 3,00 4 giờ 00 5 giờ 00 6 giờ 00 7 giờ 00 8 giờ 00 9 giờ 00 10,00% California Florida Illinois New York Texas 50.000.000 USD 100.000.000 USD 150.000.000 USD 200.000.000 USD 250.000.000 USD 300.000.000 USD 350.000.000 USD 400.000.000 USD 8,68% 7,50% 8,80% 8,52% 8,19% Ortho Inc. - Phân tích thuế bán hàng Thuế suất trong Phần trăm Thuế ở Hàng ngàn tiểu bang Mua hàng Thuế bán hàng đã nộp Thuế suất

1. Chuẩn bị phần diễn giải kết quả phân tích.

2. Phân tích này đã đầy đủ chưa hay bạn sẽ cần phân tích bổ sung?

3. Tạo các phân tích bổ sung về kết quả theo năm. Trường hợp tiếp theo của Le Grind: Xác minh và diễn giải tổng Phân tích lợi nhuận dữ liệu Truy cập nền tảng học tập trực tuyến của Wiley để biết thêm câu hỏi, dữ liệu và biết thêm thông tin chi tiết về vụ việc tiếp tục.

#### **English**
<iframe src="TaiLieu/textbookForPractice/Ch_08_Interpreting%20Data%20Analysis%20Results.pdf" width="100%" height="800px"></iframe>

#### ** 🎬 Video **

<iframe src="videoPractice/Chapter08/index.html" style="width: 100%; aspect-ratio: 16/9; max-height: 75vh; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>

#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slidePractice/Slide_Practice_Ch08.pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slidePractice/Slide_Practice_Ch08.pdf#view=FitH" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slidePractice/Slide_Practice_Ch08.pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

<!-- tabs:end -->