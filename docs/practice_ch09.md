<!-- tabs:start -->
#### **Tiếng Việt**

# Chương 9: Truyền đạt Kết quả Phân tích Dữ liệu (Communicating Data Analysis Results)

> [!NOTE]
> **Dữ liệu thực hành Chương 9:**
> Để thực hành các bài tập trong chương này, bạn có thể tải về các bộ dữ liệu mô phỏng dưới đây. Bạn có thể tải về để mở ra xem trước dữ liệu:
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/SWI_SalesApprovals.csv" download target="_blank"><strong>SWI_SalesApprovals.csv</strong></a>** (EX 9.17)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/SuperScooters_Costs.csv" download target="_blank"><strong>SuperScooters_Costs.csv</strong></a>** (EX 9.18)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/HEH_B2B_Sales.csv" download target="_blank"><strong>HEH_B2B_Sales.csv</strong></a>** (EX 9.19)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/OneStopShop_ProductMix.csv" download target="_blank"><strong>OneStopShop_ProductMix.csv</strong></a>** (EX 9.20)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/MPL_ComputerUsage.csv" download target="_blank"><strong>MPL_ComputerUsage.csv</strong></a>** (PAC 9.1)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/MPL_Payroll.csv" download target="_blank"><strong>MPL_Payroll.csv</strong></a>** (PAC 9.2)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/MPL_Financials_10Y.csv" download target="_blank"><strong>MPL_Financials_10Y.csv</strong></a>** (PAC 9.3)
> - 📥 **<a href="TaiLieu/textbookForPractice/Data/MPL_PerformanceMetrics.csv" download target="_blank"><strong>MPL_PerformanceMetrics.csv</strong></a>** (PAC 9.4)

Truyền dữ liệu Xem trước chương Bước cuối cùng trong quy trình phân tích dữ liệu là giải thích kết quả phân tích của chúng tôi và những hàm ý. Cho dù mục tiêu là thông báo hay thuyết phục thì việc truyền đạt kết quả một cách hiệu quả là quan trọng. Nếu đối tượng mục tiêu không hiểu thông tin thì không thành vấn đề việc phân tích được thực hiện tốt như thế nào.

Kết quả phân tích dữ liệu có thể được truyền đạt thông qua các bản ghi nhớ, báo cáo hoặc thuyết trình, kể tên một số phương pháp Bất kể hình thức truyền thông nào, việc phân tích đều phải được hỗ trợ sử dụng trực quan hóa dữ liệu, câu chuyện dữ liệu hoặc trực quan hóa dữ liệu tương tác. Chương này tập trung về các phương pháp hay nhất cho các hình thức giao tiếp phân tích dữ liệu phổ biến mà bạn sẽ gặp trong sự nghiệp kế toán của bạn, bao gồm việc chuẩn bị trực quan hóa dữ liệu hiệu quả (cả tĩnh và liên hoạt động) và tạo các câu chuyện dữ liệu. Báo cáo Giai đoạn 3 Báo cáo Giai đoạn 3 giao tiếp tôi C Xác minh quá trình và kết quả Giải thích kết quả và của họ ý nghĩa Phiên dịch Phân tích Giai đoạn 2 Phân tích M ồ S A Hiểu lý do cho phân tích dữ liệu

1. Chuẩn bị dữ liệu

2. Xây dựng thông tin mô hình

3. Khám phá dữ liệu Xác định mục tiêu và cụ thể đặt câu hỏi phân tích sẽ câu trả lời Thiết kế dữ liệu và phân tích chiến lược Kế hoạch Giai đoạn 1 Chiến lược Mục tiêu Động lực

**Cái nhìn sâu sắc chuyên nghiệp:** Kiến thức trực quan hóa dữ liệu có thể Phân biệt bạn với đám đông? Jenna là sinh viên kế toán cao cấp vừa hoàn thành khóa thực tập kiểm toán tại một công ty lớn. công ty kế toán quốc tế. Một trong những điều rút ra được lớn nhất của tôi là mức độ giao tiếp chất lượng cao được công ty thực tập của tôi đánh giá cao. Điều này đặc biệt đúng khi nói đến giao tiếp ra kết quả phân tích dữ liệu. Tôi là thực tập sinh duy nhất của khách hàng kiểm toán có kinh nghiệm sử dụng trực quan hóa dữ liệu. phần mềm hoạt động. Tôi đã có thể tạo trực quan hóa dữ liệu cho bản trình bày mà nhóm chuẩn bị cho khách hàng. Kết quả là tôi được mời tham dự buổi thuyết trình. Việc tham gia vào cuộc họp với khách hàng cho phép tôi tương tác với đối tác trên kiểm toán. Tôi tin rằng nó thực sự đã giúp tôi nổi bật so với các thực tập sinh khác và là một trong những lý do tôi được mời làm việc toàn thời gian.

**Lộ trình chương**

MỤC TIÊU BÀI HỌC ÁP DỤNG NÓ

**LO 9.1   Giải thích cách dữ liệu**

câu chuyện truyền đạt dữ liệu qua đường hậu môn- kết quả ysis.

- Phát triển kiến thức dữ liệu

- Giao tiếp hiệu quả

- Kể một câu chuyện dữ liệu Kế toán giao tiếp Thông tin (Ví dụ: Tài chính Kế toán) LO 9.2 Tóm tắt các bước để tạo dữ liệu hiệu quả trực quan hóa.

- Xác minh dữ liệu

- Xem xét khán giả

- Xác định mục tiêu Kết hợp mục tiêu với Các loại trực quan (Ví dụ: Kiểm toán) LO 9.3 Mô tả đặc điểm cơ sở dữ liệu hiệu quả trực quan hóa.

- Sử dụng nguyên tắc nhận thức thị giác

- Xem xét các thuộc tính quan tâm trước

- Tránh lộn xộn

- Sử dụng các phương pháp hay nhất dành riêng cho hình ảnh hóa Đánh giá trực quan (Ví dụ: Quản lý Kế toán) LO 9.4 Nhận biết sai lệch trực quan hóa dữ liệu.

- Bỏ qua đường cơ sở

- Thao tác với trục Y

- Đi ngược lại quy ước

- Chọn lọc dữ liệu

- Sử dụng biểu đồ sai Xác định dữ liệu sai lệch Trực quan hóa (Ví dụ: Quản lý Kế toán) LO 9.5 Tạo tính tương tác trình bày trực quan hóa dữ liệu.

- Các phương pháp hay nhất cho bài thuyết trình trực tiếp

- Tạo trực quan hóa dữ liệu tương tác Tạo một tương tác Trực quan hóa (Ví dụ: Tài chính Kế toán) Dữ liệu Thẻ Dữ liệu xuất hiện trong chương khi dữ liệu cho một ví dụ, hình minh họa hoặc ứng dụng được có sẵn trên nền tảng học tập trực tuyến của Wiley. Phần mềm phân tích dữ liệu liên tục thay đổi và có thể có nhiều phiên bản phần mềm mới hơn. được đưa ra trong chương này. Để biết thêm thông tin, hãy truy cập video đi kèm trên nền tảng học tập trực tuyến của Wiley. Chương Lộ trình 9-1

Theo cách nói của Nhà kinh tế trưởng Hal Varian của Google, một “kỹ năng cực kỳ quan trọng”.1 Điều này đặc biệt quan trọng dành cho những kế toán viên thường xuyên truyền đạt kết quả phân tích dữ liệu cho nhiều bên liên quan. Phát triển kiến thức dữ liệu Việc truyền đạt hiệu quả những phát hiện này đòi hỏi kiến thức về dữ liệu, đó là khả năng hiểu rõ đứng và truyền đạt dữ liệu. Tại sao kiến ​​thức dữ liệu lại quan trọng đến vậy? Nghiên cứu trực quan hóa dữ liệu công ty phần mềm Qlik và công ty tư vấn Accenture nhận thấy rằng 63% nhân viên sử dụng dữ liệu đưa ra quyết định ít nhất mỗi tuần một lần.2 Hơn nữa, một nghiên cứu khác của công ty tư vấn McKinsey & Company nhận thấy rằng những công ty có nhân viên thường xuyên sử dụng dữ liệu trong quá trình ra quyết định có nhiều khả năng báo cáo mức tăng trưởng doanh thu hơn 10% trong ba năm qua.3 Dữ liệu Hãy sử dụng một ví dụ để minh họa khả năng hiểu biết về dữ liệu. Hãy tưởng tượng bạn là một nhân viên kế toán Huskie Motor Corporation (HMC).4 HMC là nhà sản xuất ô tô quốc tế sản xuất và bán ô tô tại 15 quốc gia. Các quốc gia được nhóm thành ba khu vực – Châu Âu, Bắc Mỹ và Nam Mỹ (Minh họa 9.1).

## 9.1  Chúng ta kể một câu chuyện dữ liệu như thế nào?

**MỤC TIÊU HỌC TẬP ➊**

Giải thích cách câu chuyện dữ liệu truyền đạt kết quả phân tích dữ liệu. 1McKinsey & Company, 2009. Hal Varian về việc Web thách thức các nhà quản lý như thế nào. https://www.mckinsey.com/ các ngành/công nghệ-truyền thông và viễn thông/thông tin chi tiết của chúng tôi/hal-varian-on-how-the-web-thách thức- người quản lý (truy cập vào tháng 7 năm 2022). 2Qlik và Accenture. 2020. Tác động của con người đối với kiến ​​thức dữ liệu. Dự án kiến ​​thức dữ liệu. https:// thedataliteracyproject.org/humanimpact (truy cập vào tháng 7 năm 2022). 4Ann C. Dzuranin, Johan Perols và Dana L. Hart, “Huskie Motor Corporation: Hình dung hiện tại và Dự đoán Tương lai,” Tạp chí Trường hợp Giáo dục IMA, Tập 11 Số 2, 2018, bit.ly/3qHsGS2. ©2022, Viện Kế toán Quản trị, www.imanet.org. Được sử dụng với sự cho phép. 3QuantamBlack AI của McKinsey, 2019. Hãy nắm bắt chúng nếu bạn có thể: những người dẫn đầu về dữ liệu và phân tích đã thu hút như thế nào phía trước. https://www.mckinsey.com/business-functions/quantumblack/our-insights/catch-them-if-you-can- cách các nhà lãnh đạo về dữ liệu và phân tích đã tiến lên phía trước (truy cập vào tháng 7 năm 2022).

**MINH HỌA 9.1 Huskie Tổng công ty ô tô (HMC) Hoạt động quốc tế Châu Âu Bắc Mỹ Nam Mỹ Pháp Canada Argentina nước Đức México Bôlivia Ba Lan Hoa Kỳ Brazil Tây Ban Nha Chilê Thụy Điển Colombia Vương quốc Anh Venezuela**

**MINH HỌA 9.2 Thương hiệu HMC và Người mẫu Thương hiệu apechete Jackson Tatra Người mẫu Chare tàn bạo Lợi thế đảo mấu chốt nở hoa Sỏi vĩ cầm Jespie Robin nổi loạn máy đo thời gian mùa hè Gỗ Người nói huyên thuyên HMC có ba nhãn hiệu xe và mỗi nhãn hiệu có năm mẫu xe riêng biệt (Minh họa 9.2).**

![ILLUSTRATION 9.2](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.2.png)

## 9.1  Chúng ta kể một câu chuyện dữ liệu như thế nào?  9-3

Bạn được yêu cầu chuẩn bị một bản phân tích về xu hướng bán hàng theo tháng của mỗi thương hiệu. Hình minh họa

## 9.3 cung cấp thông tin bán hàng theo nhãn hiệu cho từng tháng nhưng nó có thể hiện những gì bạn cần hiểu về xu hướng bán hàng?

**MINH HỌA 9.3 Tổng HMC Doanh số theo thương hiệu 2,4 triệu USD 4,3 triệu USD 6,5 triệu USD 0,2 triệu USD 1,2 triệu USD 2,2 triệu USD 3,4 triệu USD 0,2 triệu USD 2,5 triệu USD 1,2 triệu USD 4,6 triệu USD 2,3 triệu USD 2,3 triệu USD 1,2 triệu USD 2,4 triệu USD 1,2 triệu USD 2,4 triệu USD 1,2 triệu USD 2,6 triệu USD 1,7 triệu USD 2,7 triệu USD 1,6 triệu USD 2,2 triệu USD 1,4 triệu USD 2,5 triệu USD 2,8 triệu USD 3,7 triệu USD 1,3 triệu USD 2,0 triệu USD 2,9 triệu USD 3,2 triệu USD 3,7 triệu USD 3,5 triệu USD 3,2 triệu USD 2,9 triệu USD 1,9 triệu USD tháng Giêng tháng hai tháng ba tháng tư tháng 5 tháng sáu tháng bảy tháng Tám tháng chín tháng mười tháng mười một tháng mười hai apechete Xu hướng tổng doanh thu theo thương hiệu: 2024–2025 (triệu USD) Jackson Tatra Phân tích bảng này sẽ xác định tháng nào có doanh thu cao nhất và tháng nào có doanh thu cao nhất. thấp nhất. Việc chuẩn bị một biểu đồ đường cũng sẽ thực hiện được điều tương tự (Minh họa 9.4).**

**MINH HỌA 9.4 Tổng HMC Biểu đồ đường xu hướng bán hàng 3,0 triệu USD 3,5 triệu USD 4,0 triệu USD 4,5 triệu USD 5,0 triệu USD 5,5 triệu USD 6,0 triệu USD 6,5 triệu USD 7,0 triệu USD 2,0 triệu USD 2,5 triệu USD 1,0 triệu USD 1,5 triệu USD 0,0 triệu USD 0,5 triệu USD Tổng doanh thu Tháng Tổng doanh thu theo thương hiệu: 2024–2025 (Triệu đô la) tháng Giêng. Tháng Hai Tháng ba. Tháng Tư. tháng 5 Tháng Sáu. Tháng Bảy. Tháng 8 Tháng 9 Tháng 10 Tháng 11 Tháng mười hai Thương hiệu apechete Jackson Tatra Biểu đồ trong Hình 9.4 thể hiện rõ hơn xu hướng bán hàng: • Tháng 3 là tháng có lượng bán ra cao nhất và tháng 4 là tháng có lượng bán ra thấp nhất. • Doanh số bán hàng đạt đỉnh trở lại vào tháng 6 đối với thương hiệu Apechete và Jackson, sau đó chững lại đối với thương hiệu Apechete và Jackson. phần còn lại của năm. • Thương hiệu Tatra có doanh số tăng từ tháng 4 đến tháng 8. Mặc dù các số liệu trong Hình minh họa 9.3 có thể được sử dụng để xác định xu hướng bán hàng nhưng sẽ dễ dàng hơn để làm như vậy với Hình minh họa 9.4. Bởi vì kỹ năng hiểu biết về dữ liệu là cần thiết để lập kế hoạch thành công- Trong sự nghiệp, chương này xem xét kỹ năng hiểu biết về dữ liệu trong việc truyền đạt kết quả phân tích dữ liệu.**

![ILLUSTRATION 9.4](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.4.png)

Giao tiếp hiệu quả Bước cuối cùng trong quá trình phân tích dữ liệu là tóm tắt những phát hiện của dự án và trao đổi. giới thiệu chúng tới đối tượng mục tiêu. Điều này đòi hỏi phải giải thích ý nghĩa của dữ liệu bằng cách viết ghi nhớ hoặc báo cáo hoặc chuẩn bị bài thuyết trình giải thích kết quả phân tích dữ liệu rõ ràng và ngắn gọn. Điều này không dễ dàng và cần phải thực hành. Báo cáo kết quả một cách hiệu quả phân tích dữ liệu đòi hỏi phải có nhận thức về khán giả, tập trung vào thông điệp, đưa ra thông điệp trong ngữ cảnh và đảm bảo nó được trình bày rõ ràng dưới dạng một câu chuyện hấp dẫn. Hiểu khán giả Bạn đã bao giờ tham dự một buổi thuyết trình mà người thuyết trình không cung cấp đủ thông tin cơ bản thông tin để bạn hiểu chủ đề? Giống như bước vào một lớp vật lý nâng cao khi bạn chưa bao giờ tham gia một khóa học vật lý. Hiểu người mà chúng ta đang giao tiếp là rất quan trọng. Khán giả (hoặc người đọc) phải được cung cấp đủ thông tin cơ bản và giải thích. ý để theo dõi phần trình bày. ÁP DỤNG TƯ DUY PHIẾU 9.1: Xác định đối tượng Khi truyền đạt kết quả phân tích dữ liệu, việc xác định các bên liên quan của phân tích là một bước quan trọng đầu tiên. Họ là đối tượng mà bạn đang giao tiếp (Các bên liên quan):

- Các bên liên quan nội bộ có thể sẽ biết một số thông tin bạn đang truyền đạt.

- Khi giao tiếp với các bên liên quan bên ngoài, hãy cân nhắc thông tin nào họ sẽ tìm thấy nhiều nhất phù hợp và tập trung vào đó. Biết được khán giả bao gồm các bên liên quan bên trong hay bên ngoài sẽ có thể phát triển giao tiếp phù hợp và dễ hiểu. Trong ví dụ về HMC, nếu giao tiếp dành cho các bên liên quan nội bộ như quản lý công ty, có thể giả định một cách an toàn họ sẽ có kiến thức về nền tảng của công ty. Trong khi đó, nếu bài thuyết trình dành cho các bên liên quan bên ngoài như nhà đầu tư, nó nên bao gồm nhiều thông tin cơ bản hơn về công ty. Tập trung vào tin nhắn Kế toán rất thoải mái khi đọc và giải thích các con số nên dễ dàng chỉ tập trung vào các con số khi truyền đạt phân tích dữ liệu. Tuy nhiên, khán giả có thể tương tác nhiều hơn được thiết lập trong mối quan hệ giữa các con số và thông điệp. Ví dụ, nếu mục tiêu của việc phân tích là xác định xu hướng chi phí, đảm bảo thông tin liên lạc giải thích được xu hướng và không chỉ tập trung vào số lượng. Đặt nó trong bối cảnh Gợi ý thứ ba để giao tiếp hiệu quả là đưa dữ liệu vào bối cảnh hoặc quan điểm. Có hai khía cạnh đối với bối cảnh khi truyền đạt kết quả phân tích dữ liệu: 1. Bối cảnh của mục đích tổng thể của việc phân tích. Mục đích là để thông báo hoặc thuyết phục khán giả? 2. Bối cảnh của các phân tích riêng lẻ. Các phân tích có dựa trên tất cả dữ liệu của công ty hay không? chỉ một khoa thôi à? Số liệu được tính bằng đô la hay hàng triệu? Khi truyền đạt kết quả phân tích dữ liệu, hãy cung cấp cho khán giả thông tin họ cần để hiểu rõ. đứng vững bối cảnh của phân tích. Chúng ta sẽ thảo luận về các khía cạnh khác của bối cảnh trong suốt chương này. Phấn đấu cho sự rõ ràng Gợi ý thứ tư để truyền đạt phân tích dữ liệu hiệu quả là đảm bảo rằng cộng đồng tốt đẹp là dễ hiểu. Thực hiện điều này bằng cách giải thích rõ ràng dữ liệu và kết quả trong

## 9.1  Chúng ta kể một câu chuyện dữ liệu như thế nào?  9-5

tường thuật về giao tiếp và bao gồm cả hình ảnh trực quan hiệu quả. Gợi ý cuối cùng cho giao tiếp hiệu quả là thu hút khán giả bằng một câu chuyện đáng nhớ. Kể một câu chuyện dữ liệu Con người đã truyền đạt kiến thức và thông tin bằng cách sử dụng những câu chuyện trong hàng ngàn năm– chúng là một phần không thể thiếu trong giao tiếp của con người. Trên thực tế, tâm trí con người được kết nối để hấp thụ những câu chuyện. Nghiên cứu đã chỉ ra rằng khi chúng ta nghe hoặc đọc một câu chuyện, bộ não của chúng ta được kích hoạt. các phần cảm xúc của não tiết ra các chất hóa học để kích thích cảm giác kết nối, khen thưởng và sự công nhận.5 Nói cách khác, một câu chuyện tạo ra cả phản ứng về thể chất và cảm xúc. Nghiên cứu cũng đã chỉ ra rằng các sự kiện sẽ đáng nhớ hơn tới 22% khi chúng là một phần của câu chuyện.6 Vì vậy, cách kể chuyện có thể giúp truyền đạt kết quả phân tích dữ liệu như thế nào? Yếu tố câu chuyện dữ liệu Có ba yếu tố trong một câu chuyện dữ liệu – dữ liệu, tường thuật và hình ảnh (Minh họa 9.5). 5Tâm lý học ngày nay, 2011. Rutledge, P. Sức mạnh tâm lý của việc kể chuyện. https://www.psychologytoday. com/us/blog/ Positively-media/201101/the-psychological-power-storytelling (truy cập vào tháng 7 năm 2022). 6Forbes, 2015. Harrison, K. Một bài thuyết trình hay là về dữ liệu và câu chuyện. https://www.forbes.com/sites/ kateharrison/2015/01/20/a-good-trình bày-is-about-data-and-story/#1f9a2f54450f (truy cập vào tháng 7 năm 2022). 8Thermopylae Sciences and Technology, 2014. Con người xử lý dữ liệu trực quan tốt hơn. https://www.t-sciences. com/news/humans-process-visual-data-better (truy cập vào tháng 7 năm 2022).

**MINH HỌA 9.5 Các yếu tố của Kể chuyện hiệu quả dữ liệu Tường thuật Tường thuật Hình ảnh Hình ảnh dữ liệu Tường thuật dữ liệu dữ liệu Giải thích Khai sáng Hình ảnh Tường thuật Hình ảnh Tương tác Tác giả cuốn Kể chuyện bằng dữ liệu hiệu quả, Brent Dykes, mô tả cách các yếu tố này kết hợp để giải thích, khai sáng và thu hút khán giả:7 • Sự giao thoa giữa dữ liệu và tường thuật giải thích câu chuyện dữ liệu. Lời tường thuật của câu chuyện cung cấp bối cảnh và bình luận cần thiết để hiểu kết quả phân tích. Nó cung cấp cấu trúc cho dữ liệu và hướng dẫn người đọc hiểu ý nghĩa của việc phân tích. • Dữ liệu cũng kết hợp với hình ảnh để giúp người đọc hiểu rõ hơn. Trực quan hóa dữ liệu tiết lộ các mô hình hoặc xu hướng có thể không được chú ý nếu không có sự trợ giúp của trực quan- hóa. Trên thực tế, con người xử lý hình ảnh trực quan nhanh hơn 60.000 lần so với văn bản.8 • Cuối cùng, việc kết hợp tường thuật với hình ảnh sẽ thu hút khán giả vào câu chuyện. Một câu chuyện hay có thể thu hút sự chú ý của người đọc và tăng khả năng hành động. Ngoài việc bao gồm ba yếu tố này, một câu chuyện dữ liệu tốt phải được cấu trúc một cách hiệu quả. Cấu trúc câu chuyện dữ liệu Hầu hết các câu chuyện đều có cấu trúc tương tự nhau. Họ giới thiệu các nhân vật và dựng bối cảnh, sau đó là một loạt các sự kiện xây dựng đến thời điểm quan trọng nhất hoặc khí hậu nhất của câu chuyện. Theo đoạn cao trào của câu chuyện, phần còn lại của các sự kiện sẽ sáng tỏ cho đến khi xung đột được giải quyết và câu chuyện kết thúc. 7Đê, B. (2020). Kể chuyện hiệu quả: Cách thúc đẩy sự thay đổi bằng dữ liệu, tường thuật và hình ảnh. Hoboken, NJ: Wiley.**

![ILLUSTRATION 9.5](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.5.png)

Đi theo mạch kể chuyện được mô tả trong Hình minh họa 9.7 là một cách đơn giản và hiệu quả để cấu trúc một câu chuyện dữ liệu. Sau khi đã thiết lập được cấu trúc, các yếu tố của câu chuyện (dữ liệu, tường thuật, hình ảnh) có thể được áp dụng để làm cho câu chuyện dữ liệu trở nên sống động. Cấu trúc này được gọi là kim tự tháp Freytag, đôi khi còn được gọi là công trình kể chuyện cung (Minh họa 9.6). Kim tự tháp được phát triển bởi nhà viết kịch và tiểu thuyết gia người Đức Gustav Freytag để hiểu cấu trúc của kịch Hy Lạp và Shakespeare. Nó là một trong những được dạy nhiều nhất về cấu trúc kịch trên thế giới. 9Writers.com, 2020. Glatch, S. 5 yếu tố của cấu trúc kịch tính: hiểu về kim tự tháp Freytag. https:// writer.com/freytags-pyramid (truy cập vào tháng 7 năm 2022).

**MINH HỌA 9.6 Freytag's Kim tự tháp9 Triển lãm Hành động gia tăng hành động rơi Độ phân giải Kim tự tháp Freytag cao trào Kim tự tháp của Freytag có thể được áp dụng vào việc kể chuyện bằng dữ liệu bằng ví dụ về HMC: • Nhóm kiểm toán nhận được tin báo nặc danh rằng một trong những người quản lý mua hàng đã nhận được tiền lại quả từ các nhà cung cấp. • Nhóm đã chuẩn bị một bản phân tích điều tra hành vi gian lận lại quả có thể xảy ra trong giao dịch mua bộ phận ing. Họ đã xác định vị trí của hoạt động lại quả có thể xảy ra và nhân viên và nhà cung cấp có khả năng tham gia. Nếu bạn ở trong nhóm kiểm toán, bây giờ bạn đã sẵn sàng tạo một câu chuyện bằng cách sử dụng dữ liệu các phân tích được chuẩn bị trong quá trình kiểm toán của bộ phận mua hàng. Hình minh họa 9.7 cung cấp một ví dụ về cách áp dụng kim tự tháp Freytag vào một câu chuyện dữ liệu.**

**MINH HỌA 9.7 Cấu tạo của một câu chuyện dữ liệu Kim tự tháp Freytag Ứng dụng câu chuyện dữ liệu Ví dụ về phân tích phản ứng ngược Triển lãm Giới thiệu vấn đề hoặc vấn đề. Thảo luận ngắn gọn về thông tin cơ bản liên quan đến phân tích. Bao gồm chi tiết thú vị để thu hút sự chú ý của người đọc. Ví dụ: “Lừa đảo lại quả có xảy ra ở Phòng Mua hàng không? Dựa trên một mẹo ẩn danh, chúng tôi đã xem xét kỹ hơn việc mua hàng sở.” Hành động gia tăng Đối tượng phân tích là được khám phá ở mức độ sâu hơn. Trong phần này của câu chuyện, hãy bóc bỏ các lớp giật ngược một cách có phương pháp phân tích. cao trào Phát hiện chính hoặc cái nhìn sâu sắc là đã chia sẻ. Đây chính là “khoảnh khắc aha” của câu chuyện. Sau khi xây dựng vụ án ở phần trước, công bố nghi phạm (các) nhân viên và (các) nhà cung cấp. hành động rơi Chia sẻ giải pháp. Việc xác định một nhân viên và nhà cung cấp bị nghi ngờ không chứng minh được việc lại quả gian lận đã xảy ra. Tiếp theo, cung cấp thêm chi tiết và đề xuất về giao dịch cụ thể cần được điều tra thêm. Độ phân giải Kết thúc câu chuyện và đưa ra bước tiếp theo. Đưa ra đề xuất về các biện pháp kiểm soát nội bộ bổ sung để tránh hậu quả trong tương lai lừa đảo.**

![ILLUSTRATION 9.7](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.7.png)

## 9.1  Chúng ta kể một câu chuyện dữ liệu như thế nào?  9-7

Áp dụng nó

## 9.1 giao tiếp Kế toán Thông tin Dữ liệu Kế toán tài chính U.S. Outdoor Adventures là một công ty bán lẻ bán các chuyến du lịch cắm trại nguồn cung cấp ở Hoa Kỳ. Họ chuyên xây dựng các gói cắm trại với tất cả các vật dụng cần thiết. du khách sẽ cần cho chuyến phiêu lưu ngoài trời của họ. Công ty có ba loại sản phẩm: Cắm trại Thiết bị, mái chèo và lều. Khách hàng của Cuộc phiêu lưu ngoài trời ở Hoa Kỳ được phân loại thành các phân khúc: Con- Sumer, Công ty và Đại lý Du lịch. Danh sách sản phẩm, doanh số theo phân khúc và thông tin tài chính cho năm 2025 được cung cấp. (Lưu ý: các số liệu trong báo cáo tài chính năm 2025 có thể không cộng do làm tròn số.) Các sản phẩm phiêu lưu ngoài trời ở Hoa Kỳ được cung cấp Dụng cụ cắm trại mái chèo Lều Bếp cắm trại Thuyền Kayak Lều du lịch bụi Ghế Áo phao Mô hình trại căn cứ Bộ nấu ăn ván chèo Lều Núi - 4 Người Chốt mái chèo Northface subzero Bộ dụng cụ đánh lửa Bộ sơ cứu Bộ nấu siêu nhỏ Lò nướng di động propan Túi ngủ Thông tin tài chính về Cuộc phiêu lưu ngoài trời của Hoa Kỳ năm 2025 Dụng cụ cắm trại mái chèo Lều Tổng cộng bán hàng $321,964 $ 243,580 $ 538,526 $1,104,070 Giảm giá $ 34.170 $ 40.030 $ 96.864 $ 171.063 Doanh thu thuần $ 287,794 $ 203,550 $441,663 $ 933.006 Giá vốn hàng bán $114,903 $ 87.682 $193,681 $ 396.265 Chi phí vận chuyển $ 36.900 $ 31.066 $ 64.646 $ 132.611 Lợi nhuận $135,992 $ 84.802 $183,336 $ 404.130 Công ty muốn mở rộng kinh doanh ra quốc tế, nhưng họ phải tăng thêm vốn thật đáng để làm như vậy Nếu bạn được giao nhiệm vụ trình bày thông tin này cho một nhóm nhà đầu tư tiềm năng, mô tả lý do tại sao mỗi điều sau đây lại quan trọng cần xem xét và đưa ra ví dụ về mỗi điều liên quan đến Cuộc phiêu lưu ngoài trời của Hoa Kỳ.

1. Xác định đối tượng.

2. Tập trung vào thông điệp chứ không phải những con số

3. Đặt dữ liệu vào ngữ cảnh.

4. Làm cho nó dễ hiểu.

5. Tạo một câu chuyện đáng nhớ. Tổng cộng Đại lý du lịch Công ty Người tiêu dùng $512,711 $359,264 232.095 USD $1,104,070 Cuộc phiêu lưu ngoài trời ở Hoa Kỳ Doanh số năm 2025 theo phân khúc Phân đoạn Tổng doanh thu GIẢI PHÁP

1. Cung cấp đủ thông tin cơ bản và giải thích để khán giả có thể theo dõi bài thuyết trình. trong trường hợp này, các nhà đầu tư tiềm năng là khán giả. Họ có thể sẽ hiểu những con số nhưng có thể cần thêm thông tin cơ bản về doanh nghiệp.

2. Khán giả này có thể muốn biết các con số liên quan như thế nào đến thông điệp được truyền đi. xác định, đó là khả năng doanh nghiệp thành công trên phạm vi quốc tế.

3. Đầu tiên, đó là bối cảnh của mục tiêu tổng thể của việc phân tích, đó là thu hút đầu tư vào công ty. Ngoài ra còn có bối cảnh của các phân tích cá nhân. Chúng bao gồm khách hàng của công ty, sản phẩm họ bán và lợi nhuận hiện tại của họ. Cuối cùng, có bối cảnh công ty so sánh với các đối thủ cạnh tranh như thế nào.

4. Giải thích rõ ràng số liệu và kết quả. Làm cho việc giao tiếp trở nên dễ hiểu bằng cách sử dụng hiệu quả những hình dung trực quan. Trong ví dụ này, việc tạo các hình ảnh trực quan khác ngoài bảng có thể có ý nghĩa.

5. Thu hút khán giả bằng một câu chuyện dữ liệu giúp người đọc dễ nhớ kết quả hơn. Câu chuyện trong ví dụ này có thể tập trung vào thành công trước đây của Cuộc phiêu lưu ngoài trời ở Hoa Kỳ và cách đầu tư vào việc mở rộng quốc tế sẽ xây dựng dựa trên thành công đó.

![Apply It 9.1](../TaiLieu/textbookForPractice/Figures/Ch_09/Apply%20It%209.1.png)

## 9.2  Các bước tạo là gì

Trực quan hóa dữ liệu hiệu quả?

**MỤC TIÊU HỌC TẬP ➋**

Tóm tắt các bước để tạo trực quan hóa dữ liệu hiệu quả. Trực quan hóa dữ liệu là quá trình hiển thị dữ liệu để cung cấp ý nghĩa và hiểu biết sâu sắc cho khán giả. Một hình ảnh trực quan được thiết kế tốt sẽ truyền đạt kết quả phân tích một cách rõ ràng và một cách ngắn gọn. Hình minh họa 9.8 là hình ảnh trực quan mà Ford Motor Company sử dụng trong bài trình bày của họ kết quả quý 3 năm 2021 cho các nhà đầu tư.

**MINH HỌA 9.8 Ford Motor Trình bày thu nhập của công ty 272 Q2 2020 Q3 2020 Q4 2020 Q1 2021 Q2 2021 Q3 2021 651 Đơn vị bán buôn (000) EBIT ($B) 540 533 327 546 $10,9 $25,3 Doanh thu ($B) $22,0 $23,0 $15,0 $24,0 Q2 2020 Q3 2020 Q4 2020 Q1 2021 Q2 2021 Q3 2021 $(0,9) Q2 2020 Q3 2020 Q4 2020 Q1 2021 Q2 2021 Q3 2021 3,2 USD 1,1 USD $2,9 0,2 USD $2,4 Biên EBIT (%) (8,6)% Q2 2020 Q3 2020 Q4 2020 Q1 2021 Q2 2021 Q3 2021 12,6% 4,9% 12,8% 1,3% 10,1% Nguồn: Ford, Đánh giá thu nhập quý 3 năm 2021, ngày 27 tháng 10 năm 2021. Để tổng quan về hoạt động của Ford tại Bắc Mỹ, hình minh họa này là một ví dụ về một hình ảnh trực quan được thiết kế tốt. Nó tổng hợp thông tin về số lượng xe bán ra (đơn vị bán buôn), doanh thu được tạo ra từ việc bán hàng đó (doanh thu), thu nhập trước lãi vay và thuế trên doanh thu đó (EBIT) và tỷ suất lợi nhuận phần trăm của thu nhập trước lãi vay và thuế (Tỷ lệ ký quỹ EBIT%). Lưu ý sự khác biệt về màu sắc của dữ liệu quý thứ ba. Bằng cách sử dụng một cách khác màu sắc cho quý 3 năm 2021, mục tiêu của hình ảnh hóa (để truyền đạt kết quả quý 3 năm 2021) là rõ ràng ngay lập tức. Việc tạo các hình ảnh trực quan được thiết kế tốt như thế này bắt đầu bằng việc xác minh dữ liệu, xem xét đối tượng và xác định mục tiêu của việc phân tích.**

![ILLUSTRATION 9.8](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.8.png)

## 9.2  Các bước để tạo trực quan hóa dữ liệu hiệu quả là gì?  9-9

Xác minh dữ liệu Câu nói “rác vào, rác ra” có liên quan đến giao tiếp phân tích dữ liệu cũng như thực hiện phân tích dữ liệu. Dữ liệu không chính xác dẫn đến hình dung không chính xác. Để tránh điều này, dữ liệu phải có các thuộc tính về tính chính xác, đầy đủ, nhất quán, mới mẻ và kịp thời. Dữ liệu chính xác Dữ liệu chính xác không có sai sót. Họ đáng tin cậy và đại diện cho vấn đề hoặc vấn đề đang được hình dung. Hãy tưởng tượng việc chuẩn bị thông tin cho các cổ đông của HMC hư cấu công ty. Mục tiêu là cung cấp thông tin về doanh số hàng tháng trong năm 2025 cho mỗi thương hiệu. các dữ liệu được cung cấp trong Hình minh họa 9.9 đại diện cho hiệu suất bán hàng năm 2025 của Ape- thương hiệu Chet. Nếu dữ liệu được xác nhận là không có lỗi thì chúng cũng đáng tin cậy.

**MINH HỌA 9.9 HMC 2025 Hiệu suất bán hàng 0 10 20 30 40 50 60 70 80 tháng Giêng. Tháng Hai Tháng ba. Tháng Tư. tháng 5 Tháng Sáu. Tháng Bảy. Tháng 8 Tháng 9 Tháng 10 Tháng 11 Tháng mười hai bán hàng khối lượng Tháng Doanh số bán hàng theo thương hiệu‒2025 apechete Dữ liệu đầy đủ và nhất quán Dữ liệu hoàn chỉnh khi không có dữ liệu nào bị thiếu. Hình minh họa 9.9 cho thấy doanh số hàng tháng ừm, nhưng nó thiếu dữ liệu của tháng Tư. Sẽ là bất thường nếu chỉ có bốn lần bán hàng trong cả tháng, vì vậy bước tiếp theo là xác nhận xem dữ liệu đã đầy đủ hay chưa. Dữ liệu có nhất quán trong tất cả các thời kỳ không? Ví dụ: dữ liệu phải được định dạng theo thời gian được hiển thị. Tính nhất quán cũng liên quan đến các thuộc tính của dữ liệu. Nói cách khác, mức độ chi tiết cho từng khoảng thời gian được hiển thị có giống nhau không? Hình minh họa 9.10 là một ví dụ về dữ liệu không nhất quán trong hình ảnh trực quan. Việc trực quan hóa cho tổng doanh thu năm 2024 hiển thị tổng số trên thanh tính bằng nghìn và hình ảnh trực quan cho năm 2025 hiển thị tổng doanh thu tính bằng triệu. Điều này có thể gây nhầm lẫn cho những người xem không chú ý các ký hiệu.**

![ILLUSTRATION 9.9](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.9.png)

Dữ liệu mới và kịp thời Dữ liệu được coi là mới nếu chúng là dữ liệu mới nhất hiện có. Tránh sử dụng dữ liệu lỗi thời trong trực quan hóa. Hãy xem xét cách trình bày thu nhập trong Hình minh họa 9.8. Nếu Ford đã sử dụng dữ liệu từ quý thứ hai trong bài thuyết trình về quý thứ ba của họ, các nhà đầu tư sẽ không có lợi ích gì thông tin về kết quả quý 3. Dữ liệu được coi là kịp thời khi chúng có sẵn kịp thời để sử dụng cho việc trực quan hóa. Khi thiết kế hình ảnh trực quan, hãy đảm bảo rằng dữ liệu được nhắm mục tiêu có sẵn để hình ảnh trực quan- hóa là mới mẻ. Hãy xem xét khán giả Sau khi xác minh dữ liệu, hãy cân nhắc xem ai sẽ xem hình ảnh trực quan. Khán giả có thể là tách thành bốn loại (Minh họa 9.11).10

**MINH HỌA 9.10 Tổng HMC Doanh số theo thương hiệu: 2024 và 2025 Tổng doanh thu theo thương hiệu‒2024 Thương hiệu Thương hiệu Tổng doanh thu theo thương hiệu‒2025 2 triệu USD 0 triệu USD 4 triệu USD 6 triệu USD 8 triệu USD 10 triệu USD 12 triệu USD 14 triệu USD 16 triệu USD 18 triệu USD Tổng doanh thu Apechete Jackson Tatra $9,127.6K $16,697.2K $16,305.4K 2 triệu USD 0 triệu USD 4 triệu USD 6 triệu USD 8 triệu USD 10 triệu USD 12 triệu USD 14 triệu USD 16 triệu USD 18 triệu USD 20 triệu USD Tổng doanh thu Apechete Jackson Tatra 9,5 triệu USD 18,3 triệu USD 17,2 triệu USD 17,2 triệu USD 10Harvard Business Review, tháng 4 năm 2013. Stikeleather, J. Cách kể một câu chuyện bằng dữ liệu. https://hbr.org/2013/04/ cách kể một câu chuyện bằng dữ liệu (truy cập vào tháng 7 năm 2022).**

**MINH HỌA 9.11 Các loại Khán giả Danh mục Mô tả Họ muốn gì Người mới Chưa bao giờ gặp phải thông tin. Đủ chi tiết để đạt được sự hiểu biết. quản lý Có một số kiến thức về chủ đề này. Kết quả khả thi. chuyên gia Có kiến thức sâu sắc về chủ đề. Điều tra và khám phá. điều hành Có kiến thức sâu rộng, trình độ cao về chủ đề. Chỉ những hiểu biết quan trọng nhất. Khán giả mới làm quen Đối tượng mới làm quen, có thể là nội bộ hoặc bên ngoài tổ chức, cần có đủ sự hỗ trợ thông tin cơ bản để hiểu được kết quả. Một bản phân tích cho một khách hàng bên ngoài hoặc một khách hàng trước được gửi đến một bộ phận nội bộ không quen thuộc với chủ đề này đều sẽ có đối tượng mới làm quen. Hình minh họa 9.12 là một ví dụ về kiểu trực quan hóa có thể được sử dụng để giải thích việc bán hàng xu hướng cho khán giả mới làm quen.**

![ILLUSTRATION 9.12](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.12.png)

## 9.2  Các bước để tạo trực quan hóa dữ liệu hiệu quả là gì?  11-9

**MINH HỌA 9.12 Mẫu trực quan cho người mới khán giả 0,8 triệu USD 1,0 triệu USD 1,1 triệu USD 1,3 triệu USD 1,4 triệu USD 1,5 triệu USD 1,7 triệu USD 1,9 triệu USD 0,5 triệu USD 0,7 triệu USD 0,2 triệu USD 0,3 triệu USD 0,4 triệu USD 0,0 triệu USD 0,1 triệu USD Tổng của Tổng doanh thu Tháng Xu hướng bán hàng của thương hiệu Tatra‒2025 (Triệu đô la) tháng Giêng. Tháng Hai Tháng ba. Tháng Tư. tháng 5 Tháng Sáu. Tháng Bảy. Tháng 8 Tháng 9 Tháng 10 Tháng 11 Tháng mười hai 0,6 triệu USD 0,9 triệu USD 1,2 triệu USD 1,6 triệu USD 1,8 triệu USD tháng ba Tổng doanh thu: 1,8 triệu USD tháng Tám Tổng doanh thu: 1,8 triệu USD tháng tư Tổng doanh thu: 0,7 triệu USD tháng mười hai Tổng doanh thu: 1,0 triệu USD Hình ảnh trực quan được dán nhãn rõ ràng để hiển thị cho người xem những tháng có doanh thu cao nhất và thấp nhất. Đối tượng quản lý Khán giả quản lý thường có một số kiến thức về chủ đề này, vì vậy nền tảng chi tiết thông tin có thể không cần thiết. Tuy nhiên, đối tượng này đang tìm kiếm kết quả có thể hành động được, vì vậy trực quan hóa nên bao gồm các khuyến nghị cho các hành động dựa trên kết quả. Bảng điều khiển trong Hình minh họa 9.13 cũng truyền đạt tỷ suất lợi nhuận của nhà quản lý như phân tích tổng doanh thu và chi phí. ( Data How To 9.1 ở cuối chương giải thích cách tạo bảng điều khiển này trong Tableau.) Các bộ lọc về năm bán hàng và thương hiệu cho phép người quản lý tùy chỉnh- ize hình ảnh theo năm và thương hiệu. Nó cung cấp thông tin nhanh chóng, có thể hành động. Làm thế nào để**

**MINH HỌA 9.13 Mẫu bảng thông tin hiệu suất dành cho đối tượng quản lý Tổng doanh thu theo thương hiệu 5 triệu USD 0 triệu USD 10 triệu USD 15 triệu USD 20 triệu USD 25 triệu USD 30 triệu USD 35 triệu USD Tổng doanh thu Thương hiệu apechete Jackson Tatra 35,0 triệu USD 18,6 triệu USD 33,5 triệu USD 18,6 triệu USD 33,5 triệu USD Trang tổng quan về hiệu suất của đối tượng được quản lý Tỷ suất lợi nhuận theo thương hiệu apechete Jackson Tatra 20,4% 13,0% 5,6% 2024 2025 Năm bán Ngày apechete Jackson Tatra Thương hiệu Chi phí Phân tích chi phí 10 triệu USD 0 triệu USD 20 triệu USD 30 triệu USD 40 triệu USD 50 triệu USD Giá trị Tổng số vật liệu lao động Chi phí biến đổi Bộ lọc**

![ILLUSTRATION 9.13](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.13.png)

Hình minh họa này cung cấp thông tin chi tiết về tỷ suất lợi nhuận của từng mô hình cũng như ngang với tỷ suất lợi nhuận trung bình của tất cả các mẫu HMC. Những mô hình có biên lợi nhuận âm rượu gin được xác định rõ ràng bằng các thanh màu cam. Từ đây chuyên gia có thể xác định mô hình nào để điều tra thêm. Khán giả chuyên gia Bởi vì các chuyên gia đã có kiến thức sâu sắc về chủ đề phân tích nên loại hình này khán giả không cần thông tin cơ bản cơ bản. Thay vào đó, họ quan tâm đến khía cạnh điều tra của câu chuyện. Ví dụ, các chuyên gia sẽ quan tâm đến việc đào sâu hơn vào tỷ suất lợi nhuận cho HMC để xem liệu có mô hình cụ thể nào cần được nghiên cứu hay không hơn nữa. Hình minh họa 9.14 là hình ảnh trực quan dùng để phân tích tỷ suất lợi nhuận theo mô hình.

**MINH HỌA 9.14 Hình dung mẫu dành cho khán giả chuyên gia Tỷ suất lợi nhuận theo mô hình‒2025 người mẫu –5,5% trung bình 21,0% 25,1% 19,4% 6,1% 16,1% –30% –25% –20% –15% –10% –5% 0% 5% 10% 15% 20% 25% 30% 35% 40% Tỷ suất lợi nhuận trung bình Gỗ tàn bạo mấu chốt Lợi thế vĩ cầm đảo Jespie máy đo thời gian nở hoa Chare mùa hè Robin nổi loạn Sỏi Người nói huyên thuyên –25,3% –17,3% 11,8% 18,4% 11,7% 33,0% 31,4% 37,2% 28,9% Trung bình Tỷ suất lợi nhuận –37% 37% ÁP DỤNG TƯ DUY PHIẾU 9.2: Trao tặng cho khán giả Thông tin họ cần Rất dễ đánh mất sự chú ý của khán giả nếu thiếu kiến thức, thông tin nền tảng cần thiết để diễn giải và hiểu kết quả phân tích dữ liệu (Kiến thức): • Xem xét những thông tin nào là cần thiết để hiểu được thông điệp được truyền đạt. • Bao gồm thông tin cơ bản cần thiết để khán giả hiểu được phân tích. Đối với phân tích HMC được chuẩn bị trong Hình minh họa 9.15. khán giả là những nhà điều hành, vì vậy họ hiểu rõ cách sử dụng tỷ lệ đóng góp, tổng chi phí cố định và thu nhập trước thuế để quyết định có nên ngừng sản phẩm hay không. Vì vậy, họ không cần thông tin chi tiết về cách để giải thích những con số đó.**

![ILLUSTRATION 9.15](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.15.png)

## 9.2  Các bước để tạo trực quan hóa dữ liệu hiệu quả là gì?  13-9

**MINH HỌA 9.15 Trực quan hóa mẫu cho một Đối tượng điều hành Phân tích khả năng sinh lời của Mortimer và Jespie: 2024–2025 ($800K) ($1,000K) ($600K) ($400K) ($200K) $0K $200K $400K $600K $800K 1.000 nghìn USD $1,200K $1,400K $1,600K $1,800K Ký quỹ đóng góp Tổng chi phí cố định Thu nhập trước thuế $950K $1,797K $937K $18K ($847K) 2.000 nghìn USD Hàng ngàn (bằng đô la Mỹ) Jespie Jespie máy đo thời gian máy đo thời gian máy đo thời gian Jespie ($919K) $950K $937K ($919K) máy đo thời gian Jespie Hình minh họa 9.15 cho thấy tỷ lệ đóng góp, tổng chi phí cố định và thu nhập trước thuế cho mỗi mô hình. Nếu quyết định được đưa ra là có nên ngừng các mô hình hay không, hình ảnh trực quan này truyền đạt thông tin liên quan đến quyết định đó. Cụ thể, nó cho thấy mức độ đóng góp Tuy nhiên, biên lợi nhuận sẽ bị mất và ảnh hưởng của chi phí cố định đến quyết định. Giám đốc điều hành sẽ cần xác định xem liệu chi phí cố định có thể tránh được hay không nếu ngừng sản xuất các mô hình này. ÁP DỤNG TƯ duy phản biện 9.3: Giải quyết mục tiêu Thông thường, bạn phải chuẩn bị nhiều hình ảnh trực quan trong quá trình thực hiện phân tích của mình. Khi nào bạn quyết định sử dụng hình ảnh nào trong bài thuyết trình, tập trung vào mục đích phân tích- chị (Mục đích). Điều này giúp loại trừ những hình ảnh không liên quan đến mục tiêu ban đầu của phân tích. Mục đích của phân tích HMC là đánh giá hiệu quả hoạt động của các thương hiệu khác nhau. Hãy tập trung vào mục tiêu đó trong khi chuẩn bị bài thuyết trình. Ví dụ, nếu mục đích là so sánh hiệu suất của năm danh mục, chọn biểu đồ cột thay vì khu vực biểu đồ. Xác định mục tiêu Khi dữ liệu được xác minh và đối tượng đã được xem xét, bước tiếp theo là hiểu mục tiêu của phân tích hoặc câu hỏi/vấn đề cần giải quyết trong hình ảnh trực quan. các mục tiêu của việc phân tích giúp xác định các loại trực quan phù hợp. Nó có thể là để hiển thị thành phần, mối quan hệ, phân phối, xu hướng hoặc so sánh dữ liệu (Minh họa 9.16). Đối tượng điều hành Khán giả bao gồm các giám đốc điều hành sẽ chỉ quan tâm đến những hiểu biết quan trọng nhất. Trước tiên hãy thảo luận về những hiểu biết quan trọng, sau đó thảo luận về sự hỗ trợ cho những hiểu biết đó. Hình minh họa 9.15 là một hình ảnh trực quan có thể được sử dụng khi giao tiếp với khán giả là các nhà điều hành, những người muốn biết thông tin chi tiết về hai mô hình có lợi nhuận thấp nhất là Mortimer và Jespie.**

![ILLUSTRATION 9.16](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.16.png)

Khi mục tiêu của giao tiếp phân tích dữ liệu được xác định, hãy chọn hình ảnh- sẽ truyền tải thông điệp tốt nhất. Hình minh họa 9.17 là cây quyết định để chọn một trực quan hóa nếu mục tiêu là hiển thị thành phần, mối quan hệ hoặc phân phối.

**MINH HỌA 9.17 Cây quyết định trực quan hóa để hiển thị thành phần, Mối quan hệ và phân phối Biểu đồ vùng Biểu đồ hình tròn Biểu đồ thanh xếp chồng Biểu đồ bong bóng biểu đồ phân tán Biểu đồ biểu đồ Biểu đồ đường biểu đồ phân tán Hiển thị thành phần Hiển thị sự phân phối Mục tiêu là gì của việc phân tích? Hiển thị mối quan hệ Hình minh họa 9.18 cung cấp hướng dẫn khi mục tiêu là thể hiện xu hướng hoặc so sánh.**

**MINH HỌA 9.18 Cây quyết định trực quan hóa cho Hiển thị xu hướng hoặc so sánh Biểu đồ đường Biểu đồ cột Biểu đồ thanh Biểu đồ cột Biểu đồ đường Biểu đồ cột Mục tiêu là gì của việc phân tích? Chỉ ra xu hướng So sánh Mặt hàng Theo thời gian**

**MINH HỌA 9.16 Mục tiêu trực quan Mục tiêu Giải thích Ví dụ Thành phần Hiển thị cách một phần của dữ liệu so sánh với tổng thể. Mỗi khu vực có bao nhiêu doanh thu đóng góp vào tổng doanh thu? Mối quan hệ Hiển thị cách dữ liệu có liên quan. Có mối liên hệ nào giữa máy giờ và chi phí bảo trì? Phân phối Tiết lộ cách dữ liệu được trải rộng hoặc được nhóm lại. Có những giao dịch nào có thể được coi là ngoại lệ? Xu hướng Hiển thị các mẫu trong dữ liệu. Có mô hình doanh thu theo mùa không? So sánh So sánh giá trị giữa các nhóm của dữ liệu. So sánh doanh thu năm 2024 đến năm 2025 theo sản phẩm?**

![ILLUSTRATION 9.18](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.18.png)

## 9.3  Đặc điểm của hình dung hiệu quả là gì?  9-15

Tiếp theo, chúng tôi thảo luận về các phương pháp hay nhất để tạo hình ảnh trực quan. Áp dụng nó

## 9.2 Kết hợp mục tiêu với Các loại trực quan Kiểm tra Bạn đã được chỉ định vào nhóm kiểm tra cho Cuộc phiêu lưu ngoài trời ở Hoa Kỳ. Bạn có trách nhiệm- có thể chuẩn bị trực quan hóa dữ liệu để truyền đạt kết quả của một số thử nghiệm kiểm toán. Sau đây là danh sách các phân tích đã được chuẩn bị cho cuộc kiểm toán. Ghép hình ảnh thích hợp- (các) hóa có thể được sử dụng cho mỗi phân tích. Lựa chọn phù hợp: Biểu đồ phân tán, biểu đồ cột, biểu đồ cột xếp chồng, biểu đồ đường, biểu đồ thanh Kiểm tra kiểm toán Hình dung có thể So sánh số lượng đã bán và số tiền đã thanh toán cho mỗi giao dịch mua bán. Doanh thu bán hàng theo quý, theo năm. Số lượng lều bán ra theo loại lều hiện nay năm và ba năm trước đó. Giảm giá được cung cấp cho mỗi giao dịch để xác định giảm giá bất thường. Doanh thu thực tế so với dự kiến. Thay đổi số dư tài khoản sổ cái chung. GIẢI PHÁP Kiểm tra kiểm toán Hình dung có thể So sánh số lượng và số lượng đã bán thanh toán cho mỗi giao dịch mua bán. biểu đồ phân tán Doanh thu bán hàng theo quý, theo năm. Biểu đồ cột hoặc biểu đồ cột xếp chồng Số lượng lều bán ra theo loại lều hiện nay năm và ba năm trước đó. Biểu đồ cột xếp chồng hoặc biểu đồ đường riêng biệt cho mỗi sản phẩm Giảm giá được cung cấp cho mỗi giao dịch để xác định giảm giá bất thường. biểu đồ phân tán Doanh thu thực tế so với dự kiến. Biểu đồ đường Thay đổi số dư tài khoản sổ cái chung. Biểu đồ thanh

## 9.3  Đặc điểm của

Hình dung hiệu quả?

**MỤC TIÊU HỌC TẬP ➌**

Mô tả các đặc điểm của trực quan hóa dữ liệu hiệu quả. Sau khi chọn loại trực quan hóa, bước tiếp theo là áp dụng các phương pháp hay nhất để đảm bảo nó hiệu quả.

![Apply It 9.2](../TaiLieu/textbookForPractice/Figures/Ch_09/Apply%20It%209.2.png)

Sử dụng nguyên tắc nhận thức trực quan Bộ não con người thích sự đơn giản và trật tự trong các hình ảnh trực quan vì nó ngăn cản chúng ta trở nên choáng ngợp với thông tin. Chúng ta có thể xử lý các mẫu đơn giản nhanh hơn so với com- mô hình phức tạp. Gestalt là một lĩnh vực tâm lý học là nền tảng cho nghiên cứu hiện đại của nhận thức. Nguyên tắc Gestalt của nhận thức thị giác mô tả cách con người đạt được ý nghĩa từ những kích thích xung quanh họ. Những nguyên tắc này giải quyết nhu cầu tự nhiên của con người là tìm kiếm đặt hàng. Chúng ta có thể tạo ra những hình ảnh trực quan hiệu quả bằng cách xem xét các nguyên tắc liên quan như tính chất, sự tương đồng, sự gần gũi và tiêu điểm. Tính liên tục Quy luật liên tục đề cập đến cách mọi người có xu hướng nhận thức bất kỳ đường nào là tiếp tục trong nó. hướng đã thiết lập và cách các đối tượng thẳng hàng với nhau được cảm nhận như một đường dẫn hoặc hình dạng. Chúng tôi theo dõi các đường, đường cong hoặc một chuỗi hình dạng để xác định xem có mối quan hệ nào không giữa các phần tử. Trực quan hóa dữ liệu hiệu quả sẽ sắp xếp các đối tượng trực quan thành một dòng để mô phỏng làm đơn giản hóa việc phân nhóm và so sánh. Hình minh họa 9.19 thể hiện tổng doanh thu theo mô hình bán hàng của HMC ở Vương quốc Anh. Các thanh trong biểu đồ này được sắp xếp theo thứ tự bảng chữ cái, một cách sắp xếp gây khó khăn cho người xem so sánh các mô hình. Ngược lại, Hình minh họa 9.20 cho thấy các thanh ở phía dưới đặt hàng theo tổng doanh thu. Hình minh họa 9.20 là biểu đồ dễ đọc hơn vì mắt người xem đi theo một con đường liên tục. Người xem có thể dễ dàng nhận ra đâu là sản phẩm bán chạy nhất và thấp nhất bán mô hình.

**MINH HỌA 9.19 Tổng doanh thu bởi Model-Vương quốc Anh Tổng doanh thu theo mẫu tại Vương quốc Anh: 2024–2025 $50K $0K $100K $150K $200K $250K $300K $350K $400K $450K Tổng bán hàng (ở Mỹ đô la) người mẫu Chare nở hoa mấu chốt Đảo Jespie mùa hè Robin**

**MINH HỌA 9.20 Tổng doanh thu theo Model Sắp xếp giảm dần Đặt hàng Tổng doanh thu theo mẫu tại Vương quốc Anh: 2024–2025 $50K $0K $100K $150K $200K $250K $300K $350K $400K $450K Tổng Doanh số bán hàng (ở Mỹ đô la) người mẫu mấu chốt Đảo Jespie Chare Robin nở hoa mùa hè**

![ILLUSTRATION 9.20](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.20.png)

## 9.3  Đặc điểm của hình dung hiệu quả là gì?  17-9

Sự tương đồng Quy luật tương đồng phát biểu rằng các yếu tố giống nhau có xu hướng được coi là một nhóm thống nhất. Những đồ vật giống nhau về màu sắc, hình dạng, kích thước hoặc vị trí gợi lên nhận thức rằng chúng thuộc về cùng một nhóm. Hình minh họa 9.21 là biểu đồ thanh thể hiện doanh số bán hàng theo quý của 4 xe ô tô HMC các mô hình. Biểu đồ này giúp bạn dễ dàng so sánh các thương hiệu trong từng quý nhưng lại khó để so sánh doanh số bán hàng của các thương hiệu riêng lẻ theo thời gian.

**MINH HỌA 9.21 Doanh thu hàng quý theo mẫu Tổng doanh số theo mẫu xe: 2024–2025 $0K $400K $600K $800K 1.000 nghìn USD $1,200K $1,400K $1,600K $1,800K Q1 Q2 Q3 Q4 Tổng bán hàng người mẫu $200K Gỗ vĩ cầm mấu chốt tàn bạo Gỗ vĩ cầm mấu chốt tàn bạo Gỗ vĩ cầm mấu chốt tàn bạo Gỗ vĩ cầm mấu chốt tàn bạo Nếu mục đích của hình ảnh trực quan là cung cấp sự so sánh về hiệu quả hoạt động của thương hiệu theo thời gian, thì các thương hiệu nên được nhóm lại với nhau như trong Hình minh họa 9.22.**

**MINH HỌA 9.22 Hàng quý Doanh số theo mẫu (Đã sửa đổi) Tổng doanh số theo mẫu xe: 2024–2025 $0K $400K $600K $800K 1.000 nghìn USD $1,200K $1,400K $1,600K $1,800K tàn bạo mấu chốt vĩ cầm Gỗ Tổng bán hàng người mẫu $200K mấu chốt tàn bạo vĩ cầm Gỗ Q4 Q3 Q2 Q1 Q4 Q3 Q2 Q1 Q4 Q3 Q2 Q1 Q4 Q3 Q2 Q1 Bây giờ chúng ta có thể so sánh hiệu suất thương hiệu hàng quý vì rất dễ nhận thấy việc phân nhóm theo thương hiệu. Sử dụng quy luật tương tự có thể giúp người xem xác định các nhóm mà đối tượng dữ liệu đã chơi thuộc về.**

![ILLUSTRATION 9.22](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.22.png)

Gần Quy luật tiệm cận phát biểu rằng mọi người sẽ cảm nhận được các yếu tố thị giác dựa trên mức độ gần gũi của nó. chúng được định vị với nhau. Mỗi điểm trong biểu đồ phân tán ở Hình minh họa 9.23 là một bán lẻ. Rõ ràng là có hai nhóm bán hàng:

1. Doanh thu từ 70.000 USD đến 85.000 USD.

2. Doanh thu từ 11.000 USD đến 55.000 USD. MINH HỌA 9.23 Tổng doanh thu theo giao dịch 90.000 USD 50.000 USD 60.000 USD 70.000 USD 80.000 USD 10.000 USD 20.000 USD 30.000 USD 40.000 USD $- Tổng số tiền bán: Giao dịch năm 2024 và 2025 Tổng bán hàng Giao dịch 1.000 2.500 500 2.000 0 1.500 3.000 Quy luật tiệm cận giúp người xem hiểu được một tập hợp dữ liệu lớn rất nhanh chóng. Tiêu điểm Quy luật tiêu điểm đề cập đến cách chúng ta chú ý hơn đến bất cứ điều gì nổi bật về mặt thị giác. Tiêu điểm có xu hướng là điểm khởi đầu cho người xem. Minh họa 9.21 và 9.22 là ví dụ về nguyên lý tiêu điểm Hãy tưởng tượng bạn đã chuẩn bị một bản phân tích về doanh số bán hàng của HMC trong Venezuela. Bạn bắt đầu bài thuyết trình của mình bằng cái nhìn tổng quan về doanh số bán hàng trên toàn Nam Mỹ các quốc gia được thể hiện trong Hình minh họa 9.24. MINH HỌA 9.24 Hiệu suất bán hàng ở Venezuela Tổng doanh thu ở Nam Mỹ: 2024–2025 Quốc gia $500K $0K 1.000 nghìn USD $1,500K 2.000 nghìn USD $2,500K $3,000K $3,500K $4,000K $4,500K Tổng doanh thu (bằng đô la Mỹ) Bôlivia Venezuela Argentina Colombia Brazil Chilê

![ILLUSTRATION 9.24](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.24.png)

## 9.3  Đặc điểm của hình dung hiệu quả là gì?  19-9

Hình minh họa 9.25 vẫn cung cấp thông tin về các quốc gia Nam Mỹ khác, nhưng việc sử dụng màu khác cho Venezuela sẽ tập trung sự chú ý của người xem vào quốc gia đó. Hãy xem xét các thuộc tính quan tâm Nguyên tắc Gestalt giúp tạo ra những hình ảnh trực quan dễ dàng được người xem tiếp thu. Nhưng làm sao chúng ta có thu hút được sự chú ý của họ không? Các nghiên cứu đã chỉ ra rằng ai đó sẽ quyết định trong vòng 3 đến 8 giây nên tiếp tục nhìn vào hình ảnh trực quan hay chuyển sự chú ý của họ sang thứ khác.11 Thuộc tính chú ý trước là những đặc tính trực quan mà chúng ta nhận thấy mà không nhận ra. Kích thước, màu sắc và vị trí là các thuộc tính được chú ý trước trong hình ảnh trực quan có thể hướng sự chú ý của khán giả. Kích thước Nếu các yếu tố của hình ảnh trực quan có kích thước khác nhau thì khán giả sẽ cho rằng những khác biệt về kích thước đó là quan trọng. Nói cách khác, quy mô tương đối sẽ được hiểu là tầm quan trọng tương đối. Điều này đúng ở cá nhân trực quan hóa cũng như trong bảng điều khiển. Hình minh họa 9.26 là một bảng thông tin được thiết kế để giúp ban quản lý giám sát việc bán hàng và doanh thu của thương hiệu của họ. Hình ảnh trực quan có cỡ chữ lớn nhất trong bảng điều khiển là Tỷ suất lợi nhuận theo thương hiệu. Bởi vì hình ảnh này lớn hơn những hình ảnh khác nên người xem sẽ tập trung vào nó trước khi xem tổng doanh thu và phân tích chi phí. Bạn đã tuân theo quy luật liên tục bằng cách sắp xếp các ô nhịp từ cao nhất đến thấp nhất. Tuy nhiên, bạn có thể cải thiện hình ảnh này bằng cách làm nổi bật quốc gia mà bạn muốn người xem nhìn thấy tập trung vào (Minh họa 9.25).

**MINH HỌA 9.25 Biểu đồ hiệu suất bán hàng có trọng tâm Tổng doanh thu ở Nam Mỹ: 2024–2025 $500K $0K 1.000 nghìn USD $1,500K 2.000 nghìn USD $2,500K $3,000K $3,500K $4,000K $4,500K Tổng doanh thu (bằng đô la Mỹ) Quốc gia Bôlivia Venezuela Argentina Colombia Brazil Chilê 11Knaflic Nussbaumer, C. (2015). Kể chuyện bằng dữ liệu. Hoboken, NJ: Wiley.**

![ILLUSTRATION 9.26](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.26.png)

Mặc dù kích thước tương đối của hình ảnh trực quan cho thấy tầm quan trọng của nó, nhưng kích thước của văn bản trong minh họa, so với văn bản khác, cũng sẽ cho thấy tầm quan trọng. Màu sắc Như bạn đã học trong phần thảo luận về các nguyên tắc Gestalt, màu sắc có thể khiến việc hình dung trở nên hiệu quả hơn. hiệu quả. Có ba cách để sử dụng màu sắc trong trực quan hóa:

1. Tuần tự: Màu sắc được sắp xếp từ thấp đến cao (Minh họa 9.27). MINH HỌA 9.26 Tỷ suất lợi nhuận theo Bảng điều khiển thương hiệu Tổng của Tổng bán hàng Thương hiệu Tổng doanh thu theo thương hiệu 5 triệu USD 0 triệu USD 10 triệu USD 15 triệu USD 20 triệu USD 25 triệu USD 30 triệu USD 35 triệu USD apechete Jackson Tatra 35,0 triệu USD 18,6 triệu USD 33,5 triệu USD Phân tích chi phí 10 triệu USD 0 triệu USD 20 triệu USD 30 triệu USD 40 triệu USD 50 triệu USD Giá trị chi phí Lao động Vật liệu Tổng cộng Chi phí biến đổi Tỷ suất lợi nhuận theo thương hiệu apechete Jackson Tatra 20,4% 13,0% 5,6% 2024 2025 apechete Jackson Năm bán Ngày Tatra Thương hiệu Trang tổng quan Bộ lọc MINH HỌA 9.27 Tuần tự Thang màu TỔNG (Tổng doanh thu) $66K $410K

2. Phân kỳ: Có hai màu tuần tự với điểm giữa trung tính (Minh họa 9.28). Loại thang đo này rất hữu ích trong việc hiển thị lãi và lỗ. MINH HỌA 9.28 Phân kỳ Thang màu –50,0% Tỷ lệ lợi nhuận 50,0%

3. Phân loại: Có màu sắc tương phản để so sánh riêng lẻ. Đây là một điều phổ biến sử dụng màu sắc khi so sánh các danh mục. Hình minh họa 9.29 cho thấy màu sắc tương phản như thế nào có thể được sử dụng trong biểu đồ cột.

![ILLUSTRATION 9.29](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.29.png)

## 9.3  Đặc điểm của hình dung hiệu quả là gì?  21-9

**MINH HỌA 9.29 Sử dụng màu phân loại trong biểu đồ cột ($1,000K) ($500K) $0K $500K 1.000 nghìn USD $1,500K 2.000 nghìn USD $2,500K $3,000K $3,500K $4,000K apechete Jackson Tatra Doanh thu thuần người mẫu Thu nhập trước thuế theo thương hiệu và mẫu mã‒2025 Chare đảo Sỏi Robin Summet Brutus mấu chốt vĩ cầm nổi loạn Gỗ Advn.. nở hoa Jespie Morti.. Rambl.. Màu sắc cũng có thể làm nổi bật hoặc cảnh báo khán giả tập trung vào điều gì đó cụ thể trong hình ảnh. alization. Hình minh họa 9.30 cho thấy việc sử dụng tính năng tô sáng. Hình ảnh trực quan giống hệt với Hình minh họa 9.29 nhưng phiên bản này chỉ nêu bật những thương hiệu bị lỗ ròng.**

**MINH HỌA 9.30 Sử dụng màu sắc để làm nổi bật ($1,000K) ($500K) $0K $500K 1.000 nghìn USD $1,500K 2.000 nghìn USD $2,500K $3,000K $3,500K $4,000K apechete Jackson Tatra Doanh thu thuần người mẫu Thu nhập trước thuế theo thương hiệu và mẫu mã‒2025 Chare đảo Sỏi Robin Summet Brutus mấu chốt vĩ cầm nổi loạn Gỗ Advan.. Bloom Jespie Morti.. Rambl..**

![ILLUSTRATION 9.30](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.30.png)

**MINH HỌA 9.31 Sử dụng màu sắc để cảnh báo người xem ($1,000K) ($500K) $0K $500K 1.000 nghìn USD $1,500K 2.000 nghìn USD $2,500K $3,000K $3,500K $4,000K apechete Jackson Tatra Doanh thu thuần người mẫu Thu nhập trước thuế theo thương hiệu và mẫu mã‒2025 Chare đảo Sỏi Robin Summet Brutus mấu chốt vĩ cầm nổi loạn Gỗ Advan.. Bloom Jespie Morti.. Rambl.. Doanh thu thuần –4 triệu USD 4 triệu USD Màu sắc gợi lên cảm xúc, vì vậy hãy chú ý đến tông màu mà màu sắc truyền tải. Ví dụ, màu đỏ gợi lên cảm giác cấp bách. Trong hình ảnh có thông tin tài chính, màu đỏ cũng là dấu hiệu có hiệu suất kém. Bằng cách nêu bật các mô hình có doanh thu thuần âm (Minh họa 9.31) người xem có thể nhanh chóng nhận thấy Crux, Jespie và Mortimer đang thua lỗ. Bất kể Theo tông màu của nó, màu sắc nên được sử dụng vừa nhất quán vừa tiết kiệm: • Nếu hình ảnh trực quan bao gồm màu sắc, các biến phải được biểu thị bằng cùng màu để tránh nhầm lẫn. • Diễn giải quá nhiều màu sắc có thể khiến khán giả choáng ngợp, vì vậy chỉ thêm những màu sắc tạo nên nó dễ dàng hơn để giải thích hình dung. Hình minh họa 9.32 trực quan hóa doanh thu thuần theo khu vực bằng cách sử dụng nhiều màu sắc theo hướng phân kỳ thang màu.**

**MINH HỌA 9.32 Trực quan hóa với quá nhiều màu sắc apechete Vùng Thu nhập trước thuế theo vùng $ 1,246,353 $ 2,013,345 $ 2,372,282 1.010.446 USD $963,145 $625,278 Jackson Tatra Châu Âu Bắc Mỹ Nam Mỹ Doanh thu thuần $124,690 3 triệu USD $ 2,719,779 136.006 USD $124,690 Làm nổi bật các thương hiệu bị lỗ ròng và làm mờ dần tất cả các thanh khác sẽ khuyến khích khán giả ngay lập tức tập trung vào các thanh tối hơn. Sử dụng màu sắc theo cách này cũng là một bài kiểm tra khác- ý nghĩa của việc áp dụng Luật đầu mối. Điều gì sẽ xảy ra nếu mục đích là thu hút sự chú ý của khán giả và cảnh báo họ về một vấn đề hoặc vấn đề? Hình minh họa 9.31 thay đổi màu sắc của các tổn thất trong Hình minh họa 9.30 để truyền tải một cảm giác cấp bách.**

![ILLUSTRATION 9.32](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.32.png)

## 9.3  Đặc điểm của hình dung hiệu quả là gì?  23-9

Do tải trọng nhận thức bổ sung được tạo ra bởi màu sắc nên việc diễn giải bảng sẽ dễ dàng hơn. khó khăn. Người xem phải giải thích các con số, vùng, nhãn hiệu và bảy màu sắc khác nhau để hiểu bảng. Mặt khác, thang độ dốc đơn màu trong Hình minh họa 9.33 giúp dễ dàng hơn để khán giả nhanh chóng nhận thấy Tatra ở Bắc Mỹ có doanh thu ròng cao nhất.

**MINH HỌA 9.33 Đã sửa đổi Trực quan hóa bằng cách sử dụng một màu Thang đo độ dốc apechete Vùng Thu nhập trước thuế theo vùng $ 1,246,353 $ 2,013,345 $ 2,372,282 1.010.446 USD $963,145 $625,278 Jackson Tatra Châu Âu Bắc Mỹ Nam Mỹ Thu nhập trước thuế $ 2,719,779 136.006 USD $124,690 $124,690 3 triệu USD Cuối cùng, hãy cân nhắc những người dùng bị mù màu khi tạo hình ảnh trực quan. Mù màu ảnh hưởng đến 8% nam giới và 0,5% phụ nữ. Bệnh mù màu phổ biến nhất là không có khả năng phân biệt nhuốm màu giữa các sắc thái màu đỏ và xanh lá cây, do đó tránh sử dụng màu đỏ và màu xanh lá cây trong cùng một hình dung. Vị trí Vị trí mục trong hình ảnh trực quan và bảng điều khiển rất quan trọng. Hầu hết mọi người bắt đầu xem một hình ảnh phân tích từ góc trên bên trái và sau đó quét theo chuyển động zig-zag qua toàn bộ hình ảnh- hóa (Minh họa 9.34). Hãy suy nghĩ về việc xem trực quan hóa trang tổng quan trong Hình minh họa 9,26. Bạn có thể đã bắt đầu bằng cách đọc tiêu đề “Tỷ suất lợi nhuận theo thương hiệu”. Vì vậy, hãy chắc chắn đặt thông tin quan trọng nhất ở phía trên bên trái của hình ảnh trực quan. Tiêu đề Cuối cùng, hãy thêm một tiêu đề thực tế và trung lập. Tránh sử dụng những từ mô tả không cần thiết. tiêu đề phải là một danh từ đại diện cho những gì được đo lường và khi nào. Trong Hình minh họa 9.31 tiêu đề đơn giản là: Thu nhập trước thuế theo Mô hình–2025. Thu nhập trước thuế đang được tính toán để người đọc biết phép đo là gì và khoảng thời gian. Hình minh họa 9.35 là một ví dụ về những việc không nên làm.**

**MINH HỌA 9.34 Làm thế nào Thông tin được xem trên màn hình hoặc Trang 1 2 3 4**

**MINH HỌA 9.35 Cách đặt tiêu đề sai cho một hình ảnh trực quan Chare ($1,000K) ($500K) $0K $500K 1.000 nghìn USD $1,500K 2.000 nghìn USD $2,500K $3,000K $3,500K $4,000K apechete Jackson Tatra đảo Sỏi Robin Summet Brutus mấu chốt vĩ cầm nổi loạn Gỗ Advan.. Bloom Jespie Morti.. Rambl.. Thu nhập trước thuế người mẫu So sánh hiệu suất mô hình**

![ILLUSTRATION 9.35](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.35.png)

Tiêu đề của hình ảnh không cung cấp cho người đọc sự mô tả rõ ràng về nội dung đang được đo. được đảm bảo (thu nhập trước thuế theo mô hình) hoặc khoảng thời gian được trình bày (2025). Một tiêu đề tốt hơn sẽ là: “Thu nhập trước thuế theo Mô hình–2025.” Tránh lộn xộn Sau khi xem xét các nguyên tắc về nhận thức và các đặc điểm chú ý trước, hãy xem xét sự kết hợp trực quan ter trong trực quan hóa. Sự lộn xộn là kẻ thù của một hình dung tốt. Càng lộn xộn thì hình dung, người xem càng khó hiểu được kết quả. Xóa mọi dữ liệu phi dữ liệu chi tiết liên quan từ trực quan hóa và kiểm tra thông tin dư thừa. Mục đích của Hình minh họa 9.36 thể hiện tổng doanh số bán hàng của từng mẫu xe được sản xuất dưới Thương hiệu Jackson và xác định mẫu bán chạy nhất.

**MINH HỌA 9.36 Hình dung chứa sự lộn xộn Thương hiệu Jackson: Tổng doanh thu theo mẫu người mẫu người mẫu 1.000.000 USD 1.500.000 USD 500.000 USD $0 2.000.000 USD 2.500.000 USD 3.000.000 USD tàn bạo 3.500.000 USD 4.000.000 USD 4.500.000 USD 5.000.000 USD 5.500.000 USD Tổng doanh thu nổi loạn mấu chốt vĩ cầm tàn bạo Gỗ mấu chốt vĩ cầm nổi loạn Gỗ Model: Crux Tổng doanh thu: $4,841,168 Người mẫu: Brutus Tổng doanh thu: $2,149,039 Các mẫu xe Jackson có tổng doanh thu của HMC: 2024–2025 Hình ảnh hiển thị doanh số bán hàng của các mẫu thương hiệu Jackson. Tuy nhiên, có rất nhiều yếu tố khiến người xem có thể bị choáng ngợp. Minh họa 9.37 sử dụng cùng dữ liệu nhưng loại bỏ những khía cạnh không cần thiết của việc hình dung.**

**MINH HỌA 9.37 Đã sửa đổi Trực quan hóa với sự lộn xộn Đã xóa Thương hiệu Jackson: Tổng doanh thu theo mẫu xe: 2024–2025 vĩ cầm Gỗ nổi loạn mấu chốt 4,8 triệu USD 4,6 triệu USD 3,9 triệu USD 3,2 triệu USD 2,1 triệu USD tàn bạo**

![ILLUSTRATION 9.37](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.37.png)

## 9.3  Đặc điểm của hình dung hiệu quả là gì?  25-9

Hãy nhớ lại rằng mục đích của việc trực quan hóa là cho thấy các mô hình khác nhau được thực hiện như thế nào. hình thành cho thương hiệu Jackson. Những thay đổi được tóm tắt trong Hình minh họa 9.38. Nền trong Hình minh họa 9.36 được tô màu xám, nhưng không cần thiết phải tô bóng nền của trực quan hóa. Điều đặc biệt quan trọng là tránh sử dụng nền đen- nền đen vì mặc dù trông có vẻ nổi bật nhưng nền đen có thể tạo ra màu sáng hơn và các từ có vẻ mờ đối với bất kỳ ai bị loạn thị. Theo Tổ chức Y tế Thế giới - (WHO), 43% dân số mắc chứng loạn thị, một tình trạng về thị giác có tật khúc xạ cản trở mắt tập trung ánh sáng đều vào võng mạc. Hình minh họa 9.39 là một danh sách kiểm tra, dựa trên các phương pháp hay nhất được thảo luận ở đây, để sử dụng khi đánh giá trực quan hóa dữ liệu của bạn.

**MINH HỌA 9.38 Tóm tắt: Trước và Sau khi Giảm Sự lộn xộn trực quan Hình ảnh lộn xộn Trực quan hóa đã sửa đổi Quá nhiều màu sắc không làm tăng thêm ý nghĩa của đồ thị vì các mô hình cũng được dán nhãn trực tiếp. Hình ảnh là một màu duy nhất. Nhãn trục được cung cấp, nhưng khán giả phải đoán số tiền chính xác. Dán nhãn trực tiếp cho từng thanh với doanh số bán hàng số lượng và loại bỏ trục. Khối lượng bán hàng nằm trong tiêu đề của biểu đồ, vì vậy loại bỏ tiêu đề trục. Hộp văn bản chú thích xác định sản phẩm bán chạy nhất mô hình. Sắp xếp dữ liệu từ cao nhất đến thấp nhất. Màu nền của biểu đồ là không cần thiết. Loại bỏ màu nền. Xóa đường lưới vì chúng ta đang loại bỏ trục và dán nhãn cho cột trực tiếp. Các mô hình được liệt kê theo thứ tự bảng chữ cái. có không có dấu hiệu nào cho thấy khán giả nên làm theo mô hình nào tập trung vào. Mô hình bán chạy nhất được nêu bật và những người khác có màu xám để thu hút sự chú ý đến nó.**

**MINH HỌA 9.39 Danh sách kiểm tra trực quan hóa dữ liệu 1. Dữ liệu đã được xác minh. 11. Đồ thị không có đường viền (giảm sự lộn xộn). 2. Trực quan hóa giải quyết mục tiêu hoặc câu hỏi đang được đề cập đến trong phân tích. 12. Dữ liệu được dán nhãn trực tiếp chứ không phải trong một chú giải riêng biệt. 3. Nó phù hợp với đối tượng mục tiêu. 13. Các nhãn dư thừa sẽ bị loại bỏ. 4. Loại hình ảnh phù hợp với dữ liệu và mức độ độ chính xác cần thiết. 14. Thang đo trục Y bắt đầu từ số 0. 5. Tiêu đề mô tả được căn trái ở góc trên bên trái. 15. Tỷ lệ là chính xác. 6. Phụ đề và/hoặc chú thích cung cấp thêm thông tin. 16. Dữ liệu được sắp xếp có chủ ý. 7. Những phát hiện hoặc kết luận quan trọng được nhấn mạnh. 17. Màn hình hiển thị không bị phiền nhiễu. 8. Kích thước văn bản được phân cấp và có thể đọc được. 18. Màu sắc được sử dụng một cách tiết kiệm và nhất quán. 9. Văn bản nằm ngang khi có thể. 19. Màu sắc dễ đọc đối với những người bị mù màu. 10. Đường lưới, nếu được sử dụng, sẽ bị tắt tiếng. 20. Dòng chảy không gian mang lại cảm giác trực quan cho người xem.**

![ILLUSTRATION 9.39](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.39.png)

Sử dụng các phương pháp hay nhất dành riêng cho hình ảnh Các phương pháp thực hành tốt nhất đã được thảo luận trước đây và những phương pháp được liệt kê trong Hình minh họa 9.39 là một phần thiết yếu điểm bắt đầu, nhưng cũng có những phương pháp thực hành tốt nhất dựa trên loại hình ảnh trực quan cần xem xét. Hình minh họa 9.40 là bản tóm tắt các phương pháp hay nhất để trực quan hóa dữ liệu phổ biến.

**MINH HỌA 9.40 Tốt nhất Thực hành theo loại trực quan Trực quan hóa Thực tiễn tốt nhất Biểu đồ khu vực**

- Không sử dụng nhiều hơn bốn loại để tránh nhầm lẫn và sự lộn xộn.

- Bắt đầu trục y ở điểm 0.

- Đặt dữ liệu có tính biến đổi cao lên trên cùng và dữ liệu có độ biến thiên thấp trên phần dưới cùng. Biểu đồ thanh

Biểu đồ cột

- Sử dụng thanh ngang nếu có nhiều hơn 7 danh mục hoặc danh mục dài nhãn.

- Sử dụng nhãn ngang để dễ đọc hơn.

- Thanh cách phù hợp và nhất quán.

- Sử dụng màu sắc một cách tiết kiệm hoặc làm điểm nhấn.

- Luôn có đường cơ sở bằng 0 (trục y bắt đầu từ 0).

- So sánh 2–7 danh mục theo cột dọc. Biểu đồ bong bóng

- Dán nhãn bong bóng và đảm bảo chúng có thể nhìn thấy được.

- Chia kích thước bong bóng theo diện tích chứ không phải theo đường kính.

- Không sử dụng bong bóng nếu chúng có kích thước tương tự nhau. Biểu đồ biểu đồ

- Sử dụng đường cơ sở bằng 0.

- Chọn số lượng thùng thích hợp:

- Thùng là các số đại diện cho các khoảng thời gian mà dữ liệu sẽ được nhóm lại.

- Các thùng xác định các nhóm được sử dụng để phân bổ tần số.

- Nói chung, nên bao gồm từ 5–15 thùng. Biểu đồ đường

- Thời gian chạy từ trái sang phải.

- Hãy nhất quán khi vẽ các mốc thời gian.

- Dùng nét liền, không chấm.

- Sử dụng đường cơ sở bằng 0.

- Không vẽ quá bốn dòng. Thay vào đó, hãy sử dụng nhiều biểu đồ. Biểu đồ hình tròn

- Có tác động mạnh mẽ nhất với các tập dữ liệu nhỏ.

- Sử dụng tốt nhất khi thể hiện sự khác biệt trong các nhóm dựa trên một biến.

- Đảm bảo dữ liệu thêm 100%.

- Giới hạn biểu đồ ở mức tối đa là năm đoạn.

- Bắt đầu phân đoạn đầu tiên ở vị trí 12 giờ. Biểu đồ thanh xếp chồng lên nhau

- Có thể theo chiều dọc hoặc chiều ngang.

- Thực hiện theo các phương pháp hay nhất tương tự như biểu đồ thanh.

- Dùng để hiển thị so sánh các thành phần phụ giữa các danh mục.

- Sử dụng tốt nhất khi không có quá nhiều thành phần phụ.

- Cân nhắc sử dụng thanh xếp chồng 100% để so sánh giữa thanh và các thành phần phụ dễ dàng hơn. (Tiếp theo) 9.3 Đặc điểm của hình dung hiệu quả là gì? 27-9 Áp dụng các phương pháp hay nhất cho từng hình dung cụ thể, các nguyên tắc nhận thức trực quan, và sử dụng một cách thích hợp các thuộc tính được chú ý trước sẽ giúp đảm bảo bạn đang tạo ra một tầm nhìn tốt. phân tích và truyền đạt kết quả một cách hiệu quả. Không làm như vậy có thể dẫn đến hình dung rằng gây hiểu lầm, đó là chủ đề của phần tiếp theo. Áp dụng nó 9.3 Đánh giá Trực quan hóa Dữ liệu Kế toán quản trị U.S. Outdoor Adventures đã chuẩn bị các hình ảnh trực quan sau đây- để giúp hiểu rõ hơn sản phẩm nào là sản phẩm bán chạy nhất của họ. Trực quan hóa Thực tiễn tốt nhất Biểu đồ phân tán

- Tập dữ liệu phải đi theo cặp với một biến độc lập (trục x) và một biến phụ thuộc (trục y).

- Sử dụng nếu thứ tự không liên quan–nếu không thì hãy sử dụng biểu đồ đường.

- Không sử dụng nếu chỉ có một vài dữ liệu hoặc nếu không có sự tương quan. Bản đồ cây

- Thích hợp khi việc so sánh chính xác không quan trọng.

- Sử dụng màu sắc tươi sáng, tương phản để dễ dàng xác định từng ô.

- Dán nhãn hộp bằng văn bản hoặc số. MINH HỌA 9.40 (Tiếp theo) Danh mục phụ bán hàng Lều du lịch bụi Mô hình trại căn cứ Bếp cắm trại Ghế Bộ nấu ăn Chốt Bộ dụng cụ đánh lửa Bộ sơ cứu Thuyền Kayak Áo phao Bộ nấu ăn siêu nhỏ Lều Núi - 4 Người Northface Subzero ván chèo mái chèo Lò nướng di động propan Túi ngủ Lều Núi - 4 Người Lều du lịch bụi ván chèo Nấu ăn vi mô Đơn vị mái chèo Áo phao Propane Bếp nướng di động Thuyền Kayak Bếp cắm trại Trại căn cứ người mẫu Bộ nấu ăn Northface Subzero 1. Thảo luận về tính hiệu quả của việc trực quan hóa này bằng cách sử dụng các phương pháp thực hành tốt nhất để trực quan hóa dữ liệu. 2. Sử dụng bộ dữ liệu Cuộc phiêu lưu ngoài trời của Hoa Kỳ để tạo hình ảnh trực quan được cải thiện.

## 9.4  Điều gì tạo nên trực quan hóa dữ liệu

Gây hiểu lầm?

**MỤC TIÊU HỌC TẬP ❹**

Nhận biết trực quan hóa dữ liệu gây hiểu lầm. GIẢI PHÁP

1. Một số vấn đề về trực quan hóa bao gồm:

- Tiêu đề không rõ ràng. Nó phải cụ thể hơn và bao gồm ngày tháng từ dữ liệu.

- Biểu đồ bong bóng không phải là lựa chọn đúng đắn. Có quá nhiều bong bóng và rất khó để giải thích mức độ khác biệt giữa các tiểu mục.

- Hình ảnh trực quan sử dụng quá nhiều màu sắc.

- Không có con số, quy mô nên doanh thu ở từng hạng mục không rõ ràng.

- Không rõ liệu hình ảnh hiển thị số tiền bán hàng hay số lượng bán hàng. 2. Hình ảnh gợi ý có tiêu đề rõ ràng và sắp xếp các sản phẩm từ bán chạy nhất đến thấp nhất. Thang đo được thể hiện rõ ràng là doanh thu thuần tính bằng nghìn đô la. $0K $50K $100K $150K $200K $250K $300K $350K $400K $450K $500K $550K $600K $650K Lều Núi - 4 Người Lều du lịch bụi Northface Subzero mái chèo Bộ nấu ăn Lò nướng di động propan Bộ nấu ăn siêu nhỏ Bếp cắm trại ván chèo Áo phao Chốt Bộ dụng cụ đánh lửa Ghế Túi ngủ Thuyền Kayak Bộ sơ cứu Mô hình trại căn cứ Doanh số theo danh mục phụ sản phẩm: 2022–2025 Doanh thu thuần (Tính bằng nghìn) Các phương pháp hay nhất về đạo đức và trực quan hóa dữ liệu được đan xen. Bởi vì sự hình dung có thể báo hiệu ảnh hưởng sâu sắc đến cách dữ liệu được sử dụng để đưa ra quyết định, thì có nghĩa vụ đạo đức là không đánh lừa người xem. Sử dụng các phương pháp hay nhất là bước đầu tiên để giảm thiểu rủi ro tạo ra

## 9.4  Điều gì khiến việc trực quan hóa dữ liệu gây hiểu lầm?  29-9

hiển thị dữ liệu sai lệch. Thứ hai là phát triển nhận thức về cách hình dung có thể đánh lừa để tránh mắc phải những sai lầm đó. Hình dung có thể gây hiểu lầm bằng cách bỏ qua cơ sở- đường thẳng, thao tác với trục y, chọn lọc dữ liệu, sử dụng sai loại biểu đồ và đi ngược lại các quy ước. Bỏ qua đường cơ sở Hình minh họa 9.41 là hình ảnh trực quan được đăng trên blog USA Today.

**MINH HỌA 9.41 Liên bang Chi tiêu phúc lợi: Bỏ qua Đường cơ sở Hơn 100 triệu người ở Hoa Kỳ hiện đang nhận được Một số hình thức phúc lợi liên bang 108.000.000 106.000.000 104.000.000 102.000.000 100.000.000 98.000.000 96.000.000 2009 Q1 2009 Q2 2009 Q3 2009 Q4 2010 Q1 2010 Q2 2010 Q3 2010 Q4 2011 Q1 2011 Q2 94.000.000 Số lượng người Mỹ Dữ liệu cho thấy có sự gia tăng đáng báo động trong chi tiêu phúc lợi liên bang. Tuy nhiên, để ý điểm khởi đầu là 94 triệu chứ không phải 0. Dữ liệu tương tự được trình bày trong Minh họa 9.42 với đường cơ sở bằng không.**

**MINH HỌA 9.42 Liên bang Chi tiêu phúc lợi: Đường cơ sở bằng 0 Q1 2009 Q2 2009 Q3 2009 Q4 2009 Q1 2010 Q2 2010 Q3 2010 Q4 2010 Q1 2011 Phúc lợi Liên bang nhận được ở Hoa Kỳ Số lượng người Mỹ Q2 2011 20.000.000 40.000.000 0 60.000.000 80.000.000 100.000.000 120.000.000 Bạn có nhận thấy sự khác biệt giữa hai hình ảnh trực quan không? Sự gia tăng chi tiêu phúc lợi có vẻ không kịch tính bằng. Luôn lập biểu đồ dữ liệu với đường cơ sở bằng 0 để tránh gây nhầm lẫn khán giả. Nguồn: Khảo sát điều tra dân số Hoa Kỳ / Bộ Thương mại Hoa Kỳ / Miền công cộng.**

![ILLUSTRATION 9.42](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.42.png)

Thao tác với trục Y Giống như việc bỏ qua đường cơ sở, việc thao tác tỷ lệ trên trục y có thể ảnh hưởng đến cách dữ liệu được hiển thị. được giải thích. Việc mở rộng hoặc nén tỷ lệ trên trục y có thể làm thay đổi dữ liệu dường như ít nhiều có ý nghĩa. Hình minh họa 9.43 là sự so sánh hai cách trực quan hóa bằng cách sử dụng cùng một dữ liệu.

**MINH HỌA 9.43 Thao tác với các ví dụ về trục Y $3,000K $2,800K $2,600K $2,400K $2,200K 2.000 nghìn USD $1,800K $1,600K $1,400K $1,200K 1.000 nghìn USD $800K $600K $400K $200K $0K Vật liệu Chi phí vật liệu: 2024–2025 Tháng 2024 2025 2026 $1,600K $1,500K $1,400K $1,300K $1,200K $1,100K 1.000 nghìn USD $800K $700K $900K $600K $500K $400K $300K $200K $100K $0K Vật liệu Chi phí vật liệu: 2024–2025 Tháng 2024 2025 2026 Chi phí vật liệu có vẻ biến động hơn nhiều trong biểu đồ bên phải. Nếu người chuẩn bị muốn để làm cho chi phí có vẻ ít biến động hơn, trục y có thể được điều khiển giống như biểu đồ bên trái bằng tăng quy mô tối đa. Đi ngược lại các công ước Tiêu chuẩn chung trong trực quan hóa dữ liệu là màu tối hơn biểu thị số cao hơn trong một màu. quy mô. Hình minh họa 9.44 cung cấp một ví dụ về điều gì sẽ xảy ra khi tiêu chuẩn đó bị vi phạm.**

**MINH HỌA 9.44 Ví dụ đi ngược lại quy ước Tỷ suất lợi nhuận theo mô hình (Gây hiểu lầm) Tỷ suất lợi nhuận theo mô hình (Chính xác) nở hoa 28,4% Lợi thế 37,6% mùa hè 32,9% máy đo thời gian –25,4% Jespie –17,5% nổi loạn 11,6% mấu chốt –5,0% Robin 16,1% Chare 24,9% Gỗ 31,6% tàn bạo 20,9% Sỏi 19,7% vĩ cầm 17,8% Lợi thế 37,6% mùa hè 32,9% Gỗ 31,6% Chare 24,9% nở hoa 28,4% máy đo thời gian –25,4% Jespie –17,5% nổi loạn 11,6% đảo 11,2% mấu chốt –5,0% Robin 16,1% Ramb -ler 5,9% Ramb -ler 5,9% tàn bạo 20,9% Sỏi 19,7% vĩ cầm 17,8% đảo 11,2%**

![ILLUSTRATION 9.44](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.44.png)

## 9.4  Điều gì khiến việc trực quan hóa dữ liệu gây hiểu lầm?  31-9

Nếu người xem không tập trung vào những con số trong hình ảnh, họ sẽ cho rằng Mortimer có tỷ suất lợi nhuận cao nhất theo bản đồ cây bên trái. Bản đồ cây ở bên phải tuân theo các quy ước chung về màu sắc và có thể thấy ngay rằng Mortimer có mức lợi nhuận thấp nhất. ÁP DỤNG TƯ duy phê phán 9.4: Xem xét trực quan hóa Rủi ro Khi tạo trực quan hóa dữ liệu, hãy nghĩ đến những rủi ro liên quan (Rủi ro):

- Người xem có thể không hiểu được hình ảnh.

- Hình ảnh không rõ ràng.

- Hình ảnh gây hiểu lầm. Đối với việc hình dung HMC trong Hình minh họa 9.44, nếu bạn không xem xét rủi ro khi tạo ra một hình dung sai lệch, bạn có thể không nhận ra rằng quy ước về màu sắc là sai lệch. Chọn lọc dữ liệu Chỉ bao gồm một số điểm dữ liệu trong hình ảnh trực quan cũng có thể tạo ra ấn tượng sai lầm về dữ liệu. Hình minh họa 9.45 là một ví dụ về điều gì xảy ra khi dữ liệu được sử dụng có chọn lọc. MINH HỌA 9.45 Có chọn lọc Chọn ví dụ dữ liệu 45 triệu USD 50 triệu USD 5 triệu USD 10 triệu USD 15 triệu USD 20 triệu USD 25 triệu USD 30 triệu USD 35 triệu USD 40 triệu USD 0 triệu USD Tổng doanh thu Tổng doanh thu: 2024–2025 (Gây hiểu lầm) Tổng doanh thu: 2024–2025 (Chính xác) Năm bán ngày 2024 2025 $7,000K $500K 1.000 nghìn USD $1,500K 2.000 nghìn USD $2,500K $3,000K $3,500K $4,000K $4,500K $5,000K $5,500K $6,000K $6,500K $0K Tổng doanh thu Tháng 2024 2025 2026 Biểu đồ bên trái thể hiện tổng doanh thu của năm 2024 và năm 2025, trong khi biểu đồ bên phải lô đất bán hàng cho mỗi tháng. Lưu ý rằng biểu đồ bên trái tạo ra ấn tượng rằng doanh số bán hàng đã tăng dần. Tuy nhiên, như biểu đồ bên phải cho thấy, có rất nhiều sự thay đổi trong doanh số bán hàng hàng tháng. Sử dụng sai loại biểu đồ Đôi khi việc chọn sai loại biểu đồ có thể gây khó khăn cho việc diễn giải dữ liệu và dẫn đến gây nhầm lẫn cho người xem. Hình ảnh trực quan không phù hợp với loại dữ liệu hoặc kết quả phân tích được báo cáo khiến khán giả khó hiểu được thông điệp.

![ILLUSTRATION 9.45](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.45.png)

Nếu mục tiêu là hiển thị sự so sánh về hiệu quả hoạt động của từng thương hiệu theo năm thì biểu đồ thanh là một lựa chọn tốt hơn. Không giống như biểu đồ hình tròn, biểu đồ thanh giúp bạn dễ dàng xác định xem số tiền có tăng hoặc giảm. Điều này là do mắt người khó diễn giải tỷ lệ và những thay đổi về tỷ lệ trong biểu đồ hình tròn.

**MINH HỌA 9.46 Sử dụng Ví dụ về loại biểu đồ sai So sánh doanh số thương hiệu (Chính xác) apechete Jackson Tatra 2 triệu USD 0 triệu USD 4 triệu USD 6 triệu USD 8 triệu USD 10 triệu USD 12 triệu USD 14 triệu USD 16 triệu USD 18 triệu USD Tổng doanh thu Năm 2024 2025 2024 2025 2024 2025 So sánh doanh số thương hiệu (Gây hiểu lầm) apechete Tatra apechete Tatra 2024 Jackson Jackson 2025 Áp dụng nó 9.4 Xác định gây hiểu lầm Trực quan hóa dữ liệu Dữ liệu Kế toán quản lý Bạn là kế toán quản lý cho Cuộc phiêu lưu ngoài trời ở Hoa Kỳ xem xét các phân tích dữ liệu do ai đó trong bộ phận của bạn chuẩn bị. Đối với mỗi hình dung, hãy xác định xem nó có gây hiểu lầm hay không và sửa chữa những chỗ gây hiểu lầm. 1. Tỷ suất lợi nhuận theo phân khúc 35,0% 37,0% 38,0% 37,5% 38,5% 40,0% 39,5% 39,0% 40,5% 41,0% 41,5% Người tiêu dùng Công ty Đại lý du lịch Lợi nhuận trung bình Ký quỹ 36,5% 36,0% 35,5% 2025 2024 2023 2022 2025 2024 2023 2022 Năm 2025 2024 2023 2022 Hãy xem xét hai hình dung trong Hình minh họa 9.46.**

![ILLUSTRATION 9.46](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.46.png)

## 9.4  Điều gì khiến việc trực quan hóa dữ liệu gây hiểu lầm?  9-33

2. So sánh doanh số hàng năm theo sản phẩm $100K $300K $400K $450K $350K Dụng cụ cắm trại mái chèo Lều Doanh thu thuần $250K $200K $150K 2025 2024 2023 2022 2025 2024 2023 2022 Năm 2025 2024 2023 2022 3. Chi phí vận chuyển Hạng nhất Ưu tiên đặt hàng Chi phí vận chuyển theo mức độ ưu tiên đặt hàng và phương thức vận chuyển $5,505 $16,132 $13,215 $ 2,664 $13,516 $ 2,611 Cùng ngày hạng hai Quan trọng Cao Trung bình Thấp $7,687 $1,654 $8,898 $5,220 Lớp tiêu chuẩn $13,881 $41,628 $1,654 $41,628 4. $18K $20K $22K $24K $26K $28K $30K $32K $34K $14K $16K $6K $4K $12K $10K $8K $0K $2K vận chuyển Chi phí Năm đặt hàng Ngày Chi phí vận chuyển trong ngày 2022 2023 2024 2025

GIẢI PHÁP

1. Điều này gây hiểu nhầm vì đường cơ sở không bằng 0. Hình dung đã sửa: Tỷ suất lợi nhuận theo phân khúc 0,0% 40,0% 30,0% 20,0% 10,0% Người tiêu dùng Công ty Đại lý du lịch Lợi nhuận trung bình Ký quỹ 2025 2024 2023 2022 2025 2024 2023 2022 Năm 2025 2024 2023 2022

2. Điều này gây hiểu nhầm vì đường cơ sở không bằng 0. Hình dung đã sửa: So sánh doanh số hàng năm theo sản phẩm $0K $400K $450K $350K $300K Dụng cụ cắm trại mái chèo Lều Doanh thu ròng $250K $150K $200K $100K $50K 2025 2024 2023 2022 2025 2024 2023 2022 Năm 2025 2024 2023 2022

3. Hình ảnh này gây hiểu nhầm vì nó đi ngược lại quy ước bằng cách đảo ngược thang màu. Hình dung đã sửa: Chi phí vận chuyển Hạng nhất Ưu tiên đặt hàng Chi phí vận chuyển theo phương thức và mức độ ưu tiên đặt hàng: 2024–2025 $5,505 $16,132 $13,215 $ 2,664 $13,516 $ 2,611 Cùng ngày hạng hai Quan trọng Cao Trung bình Thấp $7,687 $1,654 $8,898 Lớp tiêu chuẩn $1,654 $41,628 $5,220 $13,881 $41,628

## 9.5  Dữ liệu được sử dụng như thế nào trong các bài thuyết trình trực tiếp?  9-35

4. Điều này gây hiểu nhầm vì trục y đã bị thao túng. Hình dung đã sửa: $18K $20K $16K $14K $12K $10K $8K $6K $4K $2K $0K Chi phí vận chuyển Chi phí vận chuyển trong ngày Năm đặt hàng Ngày 2022 2023 2024 2025 9.5 Dữ liệu được sử dụng như thế nào trong Live Thuyết trình? MỤC TIÊU HỌC TẬP ❺ Tạo một bản trình bày trực quan hóa dữ liệu tương tác. Bởi vì kế toán viên thường được yêu cầu trình bày các câu chuyện dữ liệu nên kỹ năng giao tiếp bằng lời nói là rất cần thiết. cần thiết cho một sự nghiệp thành công. Kết quả phân tích dữ liệu thường được truyền đạt thông qua một bài thuyết trình trực tiếp tới khán giả dự định, trực tiếp hoặc trong một cuộc họp ảo. Những cái này các bài thuyết trình thường bao gồm trực quan hóa dữ liệu tương tác. Các phương pháp hay nhất cho bản trình bày trực tiếp Dù trình bày trước khán giả trực tiếp hay ảo, bài thuyết trình phải rõ ràng và hấp dẫn. Không có gì tệ hơn việc chuẩn bị một bản phân tích dữ liệu tuyệt vời và sau đó trình bày nó cho một tổ chức độc lập. khán giả yêu quý. Tác giả kinh doanh Joel Schwartzberg đưa ra bảy cách thực hành tốt nhất để làm theo khi trình bày phân tích dữ liệu:12

1. Đảm bảo khán giả có thể xem dữ liệu. Một hình ảnh trực quan trông đẹp trên màn hình có thể quá nhỏ để người ở cuối phòng có thể nhìn thấy.

2. Tập trung vào các điểm mà dữ liệu minh họa bằng cách giải thích ý nghĩa của việc phân tích dữ liệu. Nêu các sự kiện mà không chỉ ra cách họ kể câu chuyện sẽ khiến khán giả bối rối. 12Harvard Business Review, 2020. Schwartzberg, J. Trình bày dữ liệu của bạn như một chuyên gia. https://hbr.org/2020/02/ trình bày dữ liệu của bạn như-a-pro (truy cập vào tháng 7 năm 2022).

3. Chia sẻ một điểm chính trên mỗi biểu đồ để tránh quá nhiều chi tiết. Thay vì hiển thị một số hình ảnh trực quan, chỉ chia sẻ những hình ảnh hỗ trợ câu chuyện dữ liệu.

4. Dán nhãn các thành phần biểu đồ một cách rõ ràng. Hãy xem lại chúng và hỏi: “Nếu tôi nhìn thấy điều này lần đầu tiên thời gian, liệu tôi có hiểu được không?”

5. Làm nổi bật trực quan điểm “a-ha”, hay cái nhìn sâu sắc hoặc khám phá, trong câu chuyện. Quà tặng thông minh- ers giải thích sự liên quan của khoảnh khắc “a-ha” bằng cả lời nói và điểm nhấn trực quan trong biểu đồ hoặc đồ thị.

6. Tiêu đề slide sẽ củng cố quan điểm của dữ liệu. Tránh những tiêu đề chung chung và chọn những tiêu đề đó khán giả sẽ chú ý và ghi nhớ.

7. Trình bày trước khán giả bằng cách nhìn vào họ chứ không phải đọc từ bản trình bày slide. Việc thu hút khán giả đòi hỏi phải kết nối với họ và cách tốt nhất để làm điều đó là bằng cách tập trung vào chúng hơn là các slide. Làm theo bảy cách thực hành tốt nhất này sẽ giúp tạo ra một bài thuyết trình hiệu quả. Tuy nhiên, Công việc không dừng lại ở đó, vì một bài thuyết trình hiệu quả đòi hỏi phải lập kế hoạch và thực hành. Tạo trực quan hóa dữ liệu tương tác Một cách mạnh mẽ để truyền đạt kết quả phân tích dữ liệu trong bản trình bày trực tiếp là mời khán giả khám phá cách trình bày dữ liệu. Trực quan hóa dữ liệu tương tác là một trực quan hóa cho phép người dùng khám phá, thao tác và tương tác với các biểu diễn đồ họa. các dữ liệu. Chúng giúp kết nối người thuyết trình với khán giả bằng cách đi sâu vào nội dung dữ liệu dựa trên nhu cầu của khán giả. Điều này cho phép người trình bày trả lời nhanh chóng mọi câu hỏi từ khán giả. Bên cạnh việc làm theo các phương pháp hay nhất để tạo trực quan hóa dữ liệu và kể một câu chuyện bằng dữ liệu, trực quan hóa dữ liệu tương tác sẽ cung cấp một cách dễ dàng và trực quan cho người dùng để tương tác với dữ liệu. Hãy xem xét sự hình dung trong Hình minh họa 9.47, đó là một dấu gạch ngang- bảng phản ánh tổng doanh thu và tỷ suất lợi nhuận theo nhãn hiệu xe được bán bởi Huskie Motor Tổng công ty (HMC). MINH HỌA 9.47 Bảng điều khiển tĩnh về tổng doanh thu và tỷ suất lợi nhuận Tỷ suất lợi nhuận theo thương hiệu 2024 2025 2024 2025 6,2% 5,0% Jackson Tatra 2024 0,00 0,10 0,20 0,25 2025 20,6% 20,2% apechete trung bình Tỷ suất lợi nhuận 0,05 0,15 13,2% 12,7% 13,2% 12,7% 19,5 triệu USD 27,4 triệu USD 12,8 triệu USD 9,7 triệu USD 12,6 triệu USD 5,0 triệu USD Vùng Châu Âu miền Nam Mỹ miền Bắc Mỹ 2025 2024 Tổng doanh thu theo khu vực Tổng doanh thu 5,0 triệu USD 27,4 triệu USD Tổng doanh thu theo thương hiệu apechete Jackson Tatra 2025 2024 2025 2024 2025 2024 5 triệu USD 15 triệu USD 16,7 triệu USD 9,1 triệu USD 9,5 triệu USD 16,3 triệu USD 17,2 triệu USD Tổng bán hàng 20 triệu USD 10 triệu USD 0 triệu USD 18,3 triệu USD

![ILLUSTRATION 9.47](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.47.png)

## 9.5  Dữ liệu được sử dụng như thế nào trong các bài thuyết trình trực tiếp?  9-37

Trực quan hóa tĩnh này không có chức năng tìm hiểu sâu hơn về dữ liệu. Điều gì sẽ xảy ra nếu, trong khi trình bày bài phân tích này, Giám đốc điều hành của HMC hỏi mô hình này hoạt động như thế nào? Lợi thế được thực hiện? Một hình ảnh trực quan tương tác sẽ giúp bạn có thể trả lời các câu hỏi Câu hỏi của CEO nhanh chóng. Làm thế nào để chúng ta làm cho hình ảnh trực quan có tính tương tác? Phổ biến nhất phương pháp là thêm bộ lọc cho phép lọc thông tin cụ thể. Tương tác tốt nhất trực quan hóa cho phép người dùng xem thông tin chi tiết. Việc thêm bộ lọc vào bảng thông tin trong Hình minh họa 9.47 làm cho bảng thông tin có tính tương tác, cho phép người dùng xem thông tin tương tự ở cấp độ chi tiết hơn – theo khu vực và mô hình (Minh họa 9.48).

**MINH HỌA 9.48 Bảng điều khiển tương tác về tổng doanh thu và tỷ suất lợi nhuận Tỷ suất lợi nhuận theo thương hiệu 2024 2025 Tatra –0,4 0,0 trung bình Lợi nhuận Ký quỹ –0,1 –0,2 –0,3 –25,6% –25,3% –25,6% –25,3% Châu Âu Bắc Mỹ Nam Mỹ Vùng Lợi thế nở hoa mùa hè Gỗ Robin nổi loạn Người nói huyên thuyên Sỏi máy đo thời gian Jespie đảo vĩ cầm mấu chốt Chare tàn bạo người mẫu 1,9 triệu USD 1,8 triệu USD Vùng miền Bắc Mỹ 2025 2024 Tổng doanh thu theo khu vực Tổng doanh thu 1,8 triệu USD 1,9 triệu USD Tổng doanh thu theo thương hiệu Tatra 2025 2024 0 triệu USD 1 triệu USD 1,9 triệu USD Tổng bán hàng 2 triệu USD 1,8 triệu USD Người dùng Hình minh họa 9.48 có thể chọn khu vực và kiểu xe ô tô và xem tất cả dữ liệu hoặc bất kỳ sự kết hợp nào của dữ liệu. Trong hình minh họa này, người dùng đã chọn Bắc Mỹ vùng có thể và mô hình Mortimer. Họ có thể nhanh chóng xem mô hình đó hoạt động như thế nào vào năm 2024 và 2025. ( Data How To 9.2 minh họa cách tạo bảng điều khiển tương tác trong Tableau.) Lợi ích của trực quan hóa dữ liệu tương tác là nó cho phép tương tác với dữ liệu. Một trực quan hóa tương tác giúp người dùng: • Nhanh chóng xác định xu hướng. • Xác định các mối quan hệ một cách hiệu quả. • Cung cấp cách kể chuyện bằng dữ liệu hữu ích. • Đơn giản hóa dữ liệu phức tạp. Hãy nhớ rằng trực quan hóa dữ liệu tương tác không giới hạn ở các bài thuyết trình trực tiếp. trong Nói chung, hình ảnh càng có tính tương tác cao thì người dùng sẽ càng tương tác nhiều hơn bất kể phương tiện truyền thông. Làm cách nào để**

![ILLUSTRATION 9.48](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.48.png)

Áp dụng nó

## 9.5 Tạo một tương tác Trực quan hóa Kế toán tài chính Với tư cách là nhân viên kế toán tài chính tại U.S. Outdoor Adventures, bạn đã chuẩn bị một phân tích doanh thu thuần theo loại sản phẩm. Là một phần của việc trình bày kết quả, bạn đã chuẩn bị trực quan sau: Doanh thu thuần theo danh mục sản phẩm $460K $480K $440K $420K $400K $380K $360K $340K $320K $300K $280K $240K $260K $220K Dụng cụ cắm trại mái chèo Lều Doanh thu thuần $200K $180K $120K $140K $160K $174K $207K $288K $139K $138K $173K $204K $305K $329K $400K $442K $159K $174K $207K $288K $139K $138K $173K $204K $305K $329K $400K $442K $159K $60K $80K $100K $40K $20K $0K 2025 2024 2023 2022 2025 2024 2023 2022 Năm 2025 2024 2023 2022 Trong quá trình trình bày bản phân tích cho nhóm kế toán, bạn đã được hỏi về doanh số bán hàng. cho một sản phẩm cụ thể (Bộ nấu ăn siêu nhỏ) trong danh mục sản phẩm Dụng cụ cắm trại cho năm 2024 ở California. Liệt kê những gì nên có trong hình ảnh này để làm cho nó có tính tương tác để bạn có thể trả lời các câu hỏi câu hỏi đặt ra trong buổi thuyết trình. GIẢI PHÁP Để tạo hình ảnh trực quan mang tính tương tác, hãy xác định những khía cạnh nào của hình ảnh mà người dùng sẽ quan tâm đến việc thay đổi. Trong ví dụ này, một bộ lọc là cần thiết để xem một phần phụ cụ thể như thế nào danh mục sản phẩm đang hoạt động. Để trả lời nhanh các câu hỏi về bán hàng trong một lĩnh vực cụ thể trạng thái, một bộ lọc cho trạng thái cũng là cần thiết. Bạn cũng nên có một bộ lọc cho sản phẩm danh mục để trả lời các câu hỏi về toàn bộ danh mục cũng như các danh mục phụ cụ thể. ÁP DỤNG TƯ duy phản biện 9.5: Lập kế hoạch tốt nhất Trình bày Việc tạo trực quan hóa dữ liệu cho bản trình bày cần có kế hoạch. Một phần của kế hoạch đó nên bao gồm việc xem xét các cách khác nhau để trình bày những phát hiện của bạn cũng như các hình ảnh thay thế có thể có. Alizations (Các lựa chọn thay thế):

- Hãy cởi mở về hình dung để bạn xem xét tất cả các lựa chọn có thể và tạo ra bài thuyết trình tốt nhất.

- Ví dụ: khi chuẩn bị trình bày bảng điều khiển HMC, hãy xem xét khả năng tương tác trực quan hóa trực quan so với tĩnh mở ra cơ hội cho một bài thuyết trình mạnh mẽ hơn.

Đánh giá mục tiêu học tập 9-39 Ôn tập và thực hành chương Đánh giá mục tiêu học tập ❶ Giải thích cách câu chuyện dữ liệu truyền đạt thông tin phân tích- kết quả nhé chị. Bước cuối cùng trong phân tích dữ liệu là tóm tắt các phát hiện và đánh giá. truyền đạt chúng đến đối tượng mục tiêu: • Kiến thức dữ liệu là khả năng hiểu dữ liệu và giao tiếp nghĩa của chúng một cách rõ ràng và chính xác. • Truyền đạt kết quả phân tích dữ liệu một cách hiệu quả bằng cách hiểu khán giả, tập trung vào thông điệp hơn là những con số, cung cấp bối cảnh cho dữ liệu, làm cho nó dễ hiểu kết quả và kể một câu chuyện dữ liệu. • Câu chuyện dữ liệu bao gồm ba yếu tố: dữ liệu, tường thuật và hình ảnh. Câu chuyện dữ liệu hiệu quả có cấu trúc cụ thể. Đầu tiên, vấn đề hoặc vấn đề được giới thiệu và tìm hiểu. Tiếp theo, cái nhìn sâu sắc chính là được xác định và một giải pháp được chia sẻ. Phần cuối của câu chuyện là một kết luận bao gồm các bước tiếp theo. ❷ Tóm tắt các bước tạo data hiệu quả trực quan hóa. Có ba bước cần làm theo trước khi tạo dữ liệu hiệu quả trực quan hóa: • Xác minh dữ liệu: Đảm bảo dữ liệu chính xác, đầy đủ, nhất quán lều, tươi, và kịp thời. • Hãy xem xét khán giả: Ai sẽ xem hình ảnh trực quan? Xem xét khán giả cần gì để họ tương tác và hiểu sự trực quan. $0K $15K $16K $14K $13K $12K $11K $10K $9K $8K $7K $6K $5K $4K $3K $2K $3K $2K $4K $14K $1K Doanh thu thuần 2025 2024 2023 2022 Dụng cụ cắm trại $3K $2K $4K $14K Alabama Arizona Indiana Illinois Idaho Gruzia Florida Quận Column.. Delaware Connecticut Colorado California Arkansas tiểu bang Dụng cụ cắm trại mái chèo Lều Danh mục Lều du lịch bụi Mô hình trại căn cứ Bếp cắm trại Ghế Chốt Bộ nấu ăn Bộ dụng cụ đánh lửa Bộ sơ cứu Áo phao Thuyền Kayak Bộ nấu ăn siêu nhỏ Lều Núi - 4 Người Northface Subzero Danh mục phụ Năm

❹ Nhận biết hình ảnh trực quan hóa dữ liệu gây hiểu lầm. Đạo đức và trực quan hóa dữ liệu được đan xen. Điều quan trọng là phải có thể xác định những hình dung sai lệch và không tạo ra chúng. các Những cách hình dung phổ biến gây hiểu lầm bao gồm: • Bỏ qua đường cơ sở: Điều này xảy ra khi đường cơ sở không bắt đầu từ số 0 và do đó tạo ấn tượng rằng những thay đổi kịch tính hơn. • Thao tác với trục y: Tăng hoặc giảm phạm vi trục có thể thay đổi nhận thức về dữ liệu. • Đi ngược lại các quy ước: Các quy ước về màu sắc khác thường có thể gây- cầu chì và đánh lừa khán giả. • Chọn lọc dữ liệu: Bỏ qua các điểm dữ liệu để thay đổi nhận thức về xu hướng trong dữ liệu có thể gây hiểu nhầm. • Sử dụng sai loại biểu đồ: Chọn hình ảnh trực quan không phù hợp không dễ dàng giải thích được dựa trên dữ liệu. ❺ Tạo bản trình bày trực quan hóa dữ liệu mang tính tương tác. Một cách phổ biến để truyền đạt kết quả phân tích dữ liệu là bằng miệng trình bày tới đối tượng mục tiêu: • Có một số cách thực hành nhất định khi thuyết trình: • Đảm bảo khán giả có thể xem dữ liệu. • Giải thích ý nghĩa của dữ liệu. • Chia sẻ một điểm trên mỗi biểu đồ. • Ghi nhãn trực quan một cách rõ ràng. • Làm nổi bật những hiểu biết hoặc khám phá quan trọng. • Các slide sẽ củng cố quan điểm của dữ liệu. • Nhìn vào khán giả chứ không phải vào slide của bạn. • Tạo trực quan hóa dữ liệu mang tính tương tác cho phép người xem khám phá, thao tác và tương tác với các biểu diễn đồ họa của dữ liệu. • Xác định mục tiêu: Là mục tiêu thể hiện thành phần, mối liên hệ quan hệ, phân phối, xu hướng hay so sánh? Chọn hình ảnh phù hợp với mục tiêu của dự án. ❸ Mô tả các đặc điểm của một dữ liệu hiệu quả trực quan hóa. Sau khi chọn hình ảnh trực quan, hãy làm theo các phương pháp hay nhất để đảm bảo nó truyền đạt kết quả một cách hiệu quả. Hãy xem xét các nguyên tắc của nhận thức trực quan: • Tính liên tục: Hình dung trực quan hiệu quả sẽ sắp xếp các đối tượng trực quan theo một dòng để đơn giản hóa việc nhóm và so sánh. • Sự tương đồng: Các vật phẩm giống nhau về màu sắc, hình dạng, kích thước hoặc vị trí gợi lên nhận thức rằng họ thuộc cùng một nhóm. • Sự gần gũi: Mọi người cảm nhận các yếu tố thị giác có liên quan như thế nào chúng được định vị chặt chẽ với nhau. • Tiêu điểm: Người xem hình ảnh trực quan sẽ chú ý hơn liên quan đến bất cứ điều gì nổi bật một cách trực quan. Các thuộc tính được chú ý trước là các thuộc tính trực quan mà chúng ta nhận thấy mà không cần thực tế. kích thước nó: • Kích thước: Kích thước tương đối được hiểu là tầm quan trọng tương đối. • Màu sắc: Sử dụng màu sắc một cách tiết kiệm và nhất quán. • Vị trí: Mọi người thường bắt đầu ở góc trên cùng bên trái của hình ảnh- ization và sau đó quét nó theo chuyển động zig-zag. Đặt thông tin quan trọng- ở phía trên bên trái của hình ảnh trực quan. • Tiêu đề: Chúng phải thực tế và trung lập. Tránh sử dụng không cần thiết những từ ngữ miêu tả văn bản. Tiêu đề nên bao gồm một danh từ đại diện bực bội với những gì đã được đo lường và khi nào. Tránh hình ảnh lộn xộn: • Xóa mọi chi tiết không liên quan đến dữ liệu khỏi hình ảnh trực quan. • Loại bỏ thông tin dư thừa. Đánh giá các điều khoản chính Bối cảnh 9-4 Kiến thức dữ liệu 9-2 Trực quan hóa dữ liệu 9-8 Nguyên tắc Gestalt của nhận thức thị giác 9-16 Trực quan hóa dữ liệu tương tác 9-36 Định luật liên tục 9-16 Định luật tiêu điểm 9-18 Định luật tiệm cận 9-18 Luật tương tự 9-17 Thuộc tính quan tâm 9-19

Cách đi qua 9-41 Cách đi qua CÁCH

## 9.1 Tạo Bảng điều khiển trong Tableau Bảng thông tin trong Hình minh họa 9.13 được tạo bằng phần mềm trực quan hóa Tableau. Hãy làm theo các bước sau để tự tạo nó. Những gì bạn cần: dữ liệu Tệp dữ liệu How To 9.1. BƯỚC 1: Mở sổ làm việc để tìm ba hình ảnh trực quan đã được tạo: tỷ suất lợi nhuận theo thương hiệu, tổng doanh thu theo thương hiệu và phân tích chi phí. BƯỚC 2: Mở bảng tính bảng điều khiển bằng cách chọn Bảng điều khiển trên thanh công cụ chính hoặc bằng cách nhấp vào biểu tượng bảng điều khiển bên cạnh các bảng tính ( Minh họa 9.49 ). Làm thế nào để

**MINH HỌA 9.49 Hoạt cảnh Tùy chọn bảng điều khiển trong Thanh công cụ Tập tin dữ liệu Bảng tính Câu chuyện Phân tích Bản đồ định dạng Máy chủ Cửa sổ Trợ giúp Tableau - Bảng điều khiển Cách thực hiện- 11-1 + II + Trang tổng quan Tập tin dữ liệu Bảng tính Câu chuyện Phân tích Bản đồ định dạng Máy chủ Cửa sổ Trợ giúp + II + 2 BƯỚC 3: Trong bảng tính bảng điều khiển, nhấp và kéo bất kỳ hình ảnh trực quan nào được liệt kê bên dưới Các tờ giấy vào hộp Thả tờ giấy vào đây . BƯỚC 4: Trong phần Đối tượng bên trái, chọn Nổi (Xem Minh họa 9.50). Manu- đồng minh xác định vị trí và kích thước các hình ảnh trực quan.**

**MINH HỌA 9.50 Hoạt cảnh Canvas trang tổng quan lát gạch Nổi Hiển thị tiêu đề trang tổng quan Tập tin dữ liệu Bảng tính Câu chuyện Phân tích Bản đồ định dạng Máy chủ Cửa sổ Trợ giúp Trang tổng quan Tableau-DA_1e_Chapter 09 - Cách thực hiện 9.1 - Sổ làm việc đóng gói Tableau + II + Nguồn dữ liệu Biên lợi nhuận theo thương hiệu Tổng doanh thu theo phân tích chi phí thương hiệu Bảng điều khiển 1 + + + Tập tin dữ liệu Bảng tính Câu chuyện Phân tích Bản đồ định dạng Máy chủ Cửa sổ Trợ giúp Trang tổng quan Tableau-DA_1e_Chapter 09 - Cách thực hiện 9.1 - Sổ làm việc đóng gói Tableau Trang tổng quan Bố cục Mặc định Điện thoại Kích thước Trang tính Xem trước thiết bị Tỷ suất lợi nhuận theo thương hiệu Tổng doanh thu theo thương hiệu Phân tích chi phí Đối tượng ngang Dọc văn bản Hình ảnh Trang web trống Điều hướng Tải xuống Tiện ích mở rộng Hỏi dữ liệu A Trình duyệt máy tính để bàn (1000 × 800) Thả tờ giấy vào đây 3 4**

![ILLUSTRATION 9.50](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.50.png)

CHƯƠNG 9 Truyền đạt kết quả phân tích dữ liệu BƯỚC 5: Tạo lại bảng điều khiển được hiển thị trong Hình minh họa 9.13 bằng cách thả các hình ảnh trực quan vào bảng điều khiển. ( Minh họa 9.51 ) BƯỚC 6: Di chuyển các hình ảnh trực quan xung quanh bảng điều khiển bằng cách nhấp vào hình ảnh và đang kéo nó. Nó có thể được thay đổi kích thước bằng cách nhấp vào hình ảnh và sau đó di chuột ở góc. ( Minh họa 9.51 )

**MINH HỌA 9.51 Trực quan hóa Di chuyển và Định cỡ Bảng điều khiển Trang tổng quan Bố cục Mặc định Điện thoại Kích thước Trang tính Xem trước thiết bị Tỷ suất lợi nhuận theo thương hiệu Tổng doanh thu theo thương hiệu Phân tích chi phí Đối tượng ngang Dọc văn bản Hình ảnh Trang web trống Điều hướng Tải xuống Tiện ích mở rộng Hỏi dữ liệu A lát gạch Nổi Hiển thị tiêu đề trang tổng quan Tập tin dữ liệu Bảng tính Câu chuyện Phân tích Bản đồ định dạng Máy chủ Cửa sổ Trợ giúp Trang tổng quan Tableau-DA_1e_Chapter 09 - Cách thực hiện 9.1 - Sổ làm việc đóng gói Tableau + II Trình duyệt máy tính để bàn (1000 × 800) + Tập tin dữ liệu Bảng tính Câu chuyện Phân tích Bản đồ định dạng Máy chủ Cửa sổ Trợ giúp Trang tổng quan Tableau-DA_1e_Chapter 09 - Cách thực hiện 9.1 - Sổ làm việc đóng gói Tableau Toàn bộ chế độ xem Tỷ suất lợi nhuận theo thương hiệu apechete Jackson Tatra 20,4% 13,0% 5,6% 5,6% 20,4% Trung bình Lợi nhuận tháng 3.. 10 triệu USD 0 triệu USD 20 triệu USD 30 triệu USD 40 triệu USD Apechete Jackson Tatra 18,6 triệu USD 35,0 triệu USD 33,5 triệu USD Tổng doanh thu theo thương hiệu Tổng của Tổng doanh thu 6 5 Lao động Vật liệu Tổng cộng Biến Chi phí Phân tích chi phí 20 triệu USD 0 triệu USD 40 triệu USD 60 triệu USD Giá trị CÁCH 9.2 Tạo Bảng điều khiển tương tác trong Tableau Bảng điều khiển tương tác trong Hình 9.48 được tạo bằng phần mềm trực quan Hoạt cảnh. Thực hiện theo các bước sau để tạo ra nó. Những gì bạn cần: dữ liệu Tệp dữ liệu How To 9.2. BƯỚC 1: Mở sổ làm việc. Có ba hình ảnh trực quan đã được tạo: tổng doanh thu theo khu vực, tổng doanh thu theo thương hiệu và tỷ suất lợi nhuận theo thương hiệu. BƯỚC 2: Trong mỗi hình ảnh trực quan, hãy xác nhận có bộ lọc cho mô hình và khu vực. Điều này sẽ cho phép bạn lọc đến mức độ chi tiết thấp nhất trong bảng thông tin ( Minh họa 9.52 ) . Làm cách nào để**

![ILLUSTRATION 9.52](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.52.png)

Cách đi qua 9-43

**MINH HỌA 9.52 Xác nhận Bộ lọc cho Khu vực và Mô hình Màu sắc Chi tiết Kích thước Nhãn Cột Hàng Điểm hình vuông Trang Bộ lọc Chú giải công cụ Khu vực: Châu Âu Model: Lợi thế SUM(Tổng doanh thu.. SUM(Tổng doanh thu.. NĂM(Ngày bán) Vùng 2 0,5 triệu USD 0,2 triệu USD Vùng Tổng doanh thu theo khu vực Châu Âu Châu Âu 2025 2024 BƯỚC 3: Làm theo hướng dẫn trong Cách thực hiện 9.1 để kéo cả ba hình ảnh trực quan vào dấu gạch ngang- canvas và định dạng bảng để phản chiếu bảng điều khiển trong Hình minh họa 9.48. BƯỚC 4: Để liên kết các trang tính trong bảng điều khiển để các bộ lọc sẽ áp dụng cho từng trang tính, hãy nhấp vào Danh sách bộ lọc. Chọn tùy chọn Áp dụng cho bảng tính và sau đó chọn bảng tính ( Minh họa 9.53 ).**

**MINH HỌA 9.53 Quan điểm của Bảng điều khiển sau Danh sách bộ lọc Mũi tên xuống được chọn người mẫu (Tất cả) Lợi thế nở hoa tàn bạo Chare mấu chốt vĩ cầm đảo Jespie máy đo thời gian Sỏi Người nói huyên thuyên nổi loạn Tất cả đều sử dụng nguồn dữ liệu liên quan Tất cả đều sử dụng nguồn dữ liệu này Bảng tính được chọn... Chỉ có bảng tính này... Tất cả đều sử dụng nguồn dữ liệu liên quan Tất cả đều sử dụng nguồn dữ liệu này Các bảng tính được chọn... Chỉ bảng tính này Chỉnh sửa bộ lọc... Định dạng bộ lọc và đặt điều khiển.. Áp dụng cho bảng tính Tùy chỉnh Tiêu đề Chỉnh sửa tiêu đề... Giá trị đơn (danh sách) Giá trị đơn (thả xuống) Giá trị đơn (thanh trượt) Nhiều giá trị (danh sách) Nhiều giá trị (thả xuống) Nhiều giá trị (danh sách tùy chỉnh) Trận đấu ký tự đại diện Chỉ những giá trị liên quan Tất cả giá trị trong cơ sở dữ liệu Bao gồm các giá trị Loại trừ giá trị Nổi Lệnh thả nổi Bỏ chọn Xóa khỏi Trang tổng quan Đổi tên mục bảng điều khiển... Thêm nút Hiển thị/Ẩn (Tất cả) Châu Âu Bắc Mỹ Vùng 4 Lọc danh sách mũi tên xuống Tỷ suất lợi nhuận theo thương hiệu: 2024–2025 2024 2025 2024 2025 6,2% 5,0% Jackson Tatra 0,00 0,10 0,20 0,25 trung bình Tỷ suất lợi nhuận 0,05 0,15 13,2% 12,7% 13,2% 12,7% Tổng doanh thu theo thương hiệu: 2024–2025 apechete Jackson Tatra 2025 2024 2025 2024 2025 2024 5 triệu USD 15 triệu USD 16,7 triệu USD 9,1 triệu USD 9,5 triệu USD 16,3 triệu USD 17,2 triệu USD Tổng bán hàng 20 triệu USD 10 triệu USD 0 triệu USD 18,3 triệu USD**

![ILLUSTRATION 9.48](../TaiLieu/textbookForPractice/Figures/Ch_09/ILLUSTRATION%209.48.png)

CHƯƠNG 9 Truyền đạt kết quả phân tích dữ liệu BƯỚC 5: Nhấp vào từng hình ảnh trong bảng điều khiển và tạo bộ lọc bằng cách chọn biểu tượng bộ lọc. Tỷ suất lợi nhuận theo thương hiệu: 2024–2025 2024 2025 2024 2025 Jackson Tatra 2024 0,0 0,2 2025 20,6% 20,2% apechete trung bình Tỷ suất lợi nhuận 0,1 0,3 13,2% 12,7% 13,2% 12,7% 6,2% 5,0% 6,2% 5,0% người mẫu (Tất cả) Lợi thế nở hoa tàn bạo Chare mấu chốt vĩ cầm đảo Jespie máy đo thời gian Sỏi Người nói huyên thuyên nổi loạn (Tất cả) Châu Âu Bắc Mỹ Vùng 5 19,5 triệu USD 27,4 triệu USD 12,8 triệu USD 9,7 triệu USD 12,6 triệu USD 5,0 triệu USD Vùng Châu Âu Châu Âu miền Nam Mỹ miền Bắc Mỹ 2025 2024 Tổng doanh thu theo khu vực Tổng doanh thu 5,0 triệu USD 27,4 triệu USD Tổng doanh thu theo thương hiệu: 2024–2025 apechete Jackson Tatra 2025 2024 2025 2024 2025 2024 5 triệu USD 15 triệu USD 16,7 triệu USD 9,1 triệu USD 9,5 triệu USD 16,3 triệu USD 17,2 triệu USD Tổng bán hàng 20 triệu USD 10 triệu USD 0 triệu USD 18,3 triệu USD Điều đó sẽ cho phép nhấp vào một hình ảnh và áp dụng lựa chọn cho tất cả chúng. Ví dụ, nhấp vào 12,6 triệu đô la ở Châu Âu 2025 có nghĩa là tất cả hình ảnh sẽ chỉ hiển thị Châu Âu 2025 kết quả. ( Minh họa 9.54 )

**MINH HỌA 9.54 Bảng điều khiển tương tác Tỷ suất lợi nhuận theo thương hiệu: 2024–2025 2025 2025 9,3% Jackson Tatra 0,0 0,2 0,3 2025 21,3% apechete trung bình Lợi nhuận Ký quỹ 0,1 13,5% người mẫu (Tất cả) Lợi thế nở hoa tàn bạo Chare mấu chốt vĩ cầm đảo Jespie máy đo thời gian Sỏi Người nói huyên thuyên nổi loạn (Tất cả) Châu Âu Bắc Mỹ Vùng Tổng doanh thu theo thương hiệu: 2024–2025 Apechete Jackson Tatra 2025 2025 2025 0 triệu USD 3,7 triệu USD 1,7 triệu USD Tổng bán hàng 8 triệu USD 4 triệu USD 6 triệu USD 2 triệu USD 19,5 triệu USD 27,4 triệu USD 12,8 triệu USD 9,7 triệu USD 12,6 triệu USD 5,0 triệu USD Vùng Châu Âu Châu Âu miền Nam Mỹ miền Bắc Mỹ 2025 2024 Tổng doanh thu theo khu vực Tổng doanh thu 5,0 triệu USD 27,4 triệu USD 27,4 triệu USD 9,7 triệu USD 5,0 triệu USD 19,5 triệu USD 12,8 triệu USD 7,3 triệu USD**

Câu hỏi trắc nghiệm 9-45 Câu hỏi trắc nghiệm

1. (LO 1) Khả năng đọc, ghi và giao tiếp dữ liệu trong ngữ cảnh được/được gọi là một. kỹ năng giao tiếp dữ liệu. b. truyền thông dữ liệu hiệu quả. c. kiến thức dữ liệu. d. kỹ năng kể chuyện dữ liệu.

2. (LO 1) Dara đã chuẩn bị phân tích dữ liệu về lợi nhuận theo sản phẩm cho năm hiện tại cho công ty của cô ấy. Cô ấy cảm thấy điều đó cũng quan trọng đối với cho thấy lợi nhuận năm nay so với những năm trước như thế nào. Đây là một ví dụ về một. đặt phân tích vào bối cảnh. b. hiểu khán giả. c. tạo nên một câu chuyện đáng nhớ. d. một phân tích thành phần.

3. (LO 1) Sara là kế toán tài chính cho một công ty bán lẻ. được yêu cầu thực hiện phân tích doanh số bán hàng trong 5 năm qua để chuẩn bị một báo cáo dự báo bán hàng. Công ty đang tìm kiếm thêm nhà đầu tư để họ có thể mở rộng hoạt động của mình. Người giám sát của Sara đã yêu cầu cô ấy chuẩn bị trước soạn thảo một báo cáo sẽ được trao cho các nhà đầu tư tiềm năng. Các nhà đầu tư sẽ được coi là ____________ của báo cáo. Một. các bên liên quan b. người chuẩn bị c. người mua d. cơ quan quản lý

4. (LO 1) Marcus là nhân viên kế toán tài chính cho một phần mềm máy tính công ty. Ông được yêu cầu thực hiện phân tích dòng tiền trong quá khứ 5 năm và chuẩn bị dự báo doanh thu. Công ty đang tìm kiếm thêm nhà đầu tư để mở rộng hoạt động. Marcus’ Người quản lý đã yêu cầu anh ta chuẩn bị một báo cáo sẽ được gửi cho các nhà đầu tư tiềm năng. Nếu các nhà đầu tư có thành kiến với loại hình mềm sản phẩm công ty bán, Marcus nên coi sự thiên vị này là một (n) một. thay thế quan trọng. b. sự kiện không thể kiểm soát được. c. rủi ro. d. kết quả tiêu cực.

5. (LO 1) Sự kết hợp giữa tường thuật và dữ liệu __________ câu chuyện. Một. giải thích b. soi sáng c. đính hôn. tiến hóa

6. (LO 1) Lột bỏ các lớp phân tích trong dữ liệu một cách có phương pháp câu chuyện là phần __________ của câu chuyện. Một. sự trình bày b. hành động gia tăng c. đỉnh điểm d. hành động rơi

7. (LO 2) Một __________ được thiết kế tốt sẽ truyền đạt kết quả của một cuộc phân tích- ysis một cách rõ ràng và ngắn gọn. Một. phân tích b. trực quan hóa dữ liệu c. thống kê d. báo cáo

8. (LO 2) A(n) __________ khán giả chủ yếu quan tâm đến kết quả khả thi. Một. người mới vào nghề b. quản lý c. chuyên gia d. điều hành

9. (LO 2) Biểu đồ vùng được sử dụng tốt nhất cho mục đích nào sau đây mục tiêu? Một. Đang hiển thị thành phần. b. Hiển thị các mối quan hệ. c. Hiển thị phân phối. d. Hiển thị so sánh

10. (LO 2) Biểu đồ phân tán được sử dụng tốt nhất cho trường hợp nào sau đây mục tiêu? Một. Đang hiển thị thành phần. b. Hiển thị các mối quan hệ. c. Chỉ ra xu hướng. d. Hiển thị so sánh

11. (LO 2) Jamie đang chuẩn bị hình dung để hiển thị kết quả phân tích xu hướng bán hàng. Jamie có dữ liệu về doanh số bán hàng mỗi tháng từ tất cả các khu vực của công ty. Tất cả dữ liệu bán hàng được báo cáo toàn bộ đô la ngoại trừ khu vực phía đông. Khu vực phía đông báo cáo doanh số bán hàng trong 1000- cát. Đây là ví dụ về loại thuộc tính xác minh dữ liệu nào? Một. Độ chính xác b. Tính đầy đủ c. tính nhất quán d. Độ tươi

12. (LO 3) Một ví dụ về thuộc tính quan tâm trước là một. sự lộn xộn. b. sự chính xác. c. tính kịp thời. d. màu sắc.

13. (LO 3) Nếu có 9 danh mục trong biểu đồ cột, thì danh mục nào trong số đó sau đây sẽ cải thiện khả năng trực quan hóa và làm cho nó dễ dàng hơn người đọc giải thích? Một. Sử dụng thanh dọc. b. Sử dụng thanh ngang. c. Sử dụng 9 màu khác nhau để phân biệt các loại. d. Sử dụng nhãn dọc để phù hợp với tất cả các mô tả danh mục trong đồ thị.

14. (LO 3) Khi thể hiện mối tương quan giữa hai biến, biểu đồ nào phù hợp nhất để sử dụng? Một. Bản đồ cây b. Biểu đồ thanh xếp chồng c. Biểu đồ bong bóng d. biểu đồ phân tán Dữ liệu Thẻ Dữ liệu xuất hiện khi dữ liệu cần thiết để trả lời một câu hỏi hoặc hoàn thành một câu hỏi. bài tập có sẵn trên nền tảng học tập trực tuyến của Wiley.

15. (LO 4) Xác định cách hình dung sau đây có thể gây hiểu nhầm. Pizza bán chạy nhất‒Quý 2 năm 2025 2.000 USD $2,800 3.200 USD 3.600 USD 4.400 USD 4.000 USD Phô mai xúc xích pepperoni ăn chay Tổng doanh số 2.400 USD tháng tư tháng 5 tháng sáu tháng tư tháng 5 tháng sáu tháng tư tháng 5 tháng sáu Năm một. Có quá nhiều màu sắc. b. Dữ liệu đã bị thao túng. c. Trục không bắt đầu từ số 0. d. Loại trực quan sai đã được sử dụng.

16. (LO 4) Hình ảnh trực quan sau đây được chuẩn bị để cho phép người xem so sánh số lượng bán hàng theo loại sản phẩm dành cho xe tải Pizza My Heart Food. Tên sản phẩm thịt bò bánh mì que Phô mai Cánh gà món ăn sâu tiếng Hawaii Người yêu thịt nấm xúc xích pepperoni xúc xích Bít tết tối cao ăn chay Pizza trắng Hình dung này có thể gây hiểu nhầm như thế nào? Một. Không có đường cơ sở. b. Dữ liệu đã được chọn lọc. c. Loại trực quan sai đã được sử dụng. d. Thang màu đi ngược lại với quy ước.

17. (LO 4) Hình ảnh trực quan sau đây được chuẩn bị cho bảng thông tin quản lý để theo dõi lợi nhuận lề. Tỷ suất lợi nhuận theo thương hiệu‒2025 apechete Jackson Tatra 20,4% 13,0% 5,6% Hình dung này có thể gây hiểu nhầm như thế nào? Một. Không có đường cơ sở. b. Dữ liệu đã được chọn lọc. c. Loại trực quan sai đã được sử dụng. d. Thang màu đi ngược lại với quy ước. Bài tập ngắn 9-47

18. (LO 5) Cách nào sau đây không phải là cách tốt nhất để chuẩn bị trình bày kết quả phân tích dữ liệu? Một. Tiêu đề slide phải chung chung để mọi người có thể hiểu được tiêu đề. b. Chỉ nên có một điểm chính trên mỗi biểu đồ để tránh quá mức làm choáng ngợp khán giả. c. Làm nổi bật trực quan điểm “a-ha” hoặc cái nhìn sâu sắc. d. Đảm bảo khán giả có thể nhìn thấy dữ liệu.

19. (LO 5) Trực quan hóa tĩnh một. cho phép người dùng tìm hiểu sâu hơn về phân tích. b. phù hợp nhất cho các bài thuyết trình trực tiếp. c. không cho phép người dùng tìm hiểu sâu hơn về phân tích. d. không thể được sử dụng trong một câu chuyện dữ liệu.

20. (LO 5) Hình ảnh trực quan cho phép người dùng khám phá và thao tác- mô phỏng dữ liệu là một. trực quan hóa dữ liệu tương tác. b. cần thiết cho tất cả các bài thuyết trình trực tiếp. c. không được khuyến khích cho một bài thuyết trình trực tiếp. d. chỉ được sử dụng trong bảng điều khiển. Câu hỏi ôn tập

1. (LO 1) Liệt kê và thảo luận từng đề xuất để truyền đạt hiệu quả hướng tới khán giả của bạn.

2. (LO 1) "đưa dữ liệu vào ngữ cảnh" nghĩa là gì?

3. (LO 1) Hãy tưởng tượng bạn đang trình bày một bản phân tích dữ liệu cho thấy xu hướng chi phí trong ba năm qua. Bạn đã tìm thấy một khu vực đã có sự tăng vọt đáng kể về chi phí lao động trong năm thứ hai của phân tích. Sau khi phân tích sâu hơn, bạn đã xác định được một vị trí cụ thể đang trả mức lương cao hơn nhiều so với các địa điểm khác trong cùng khu vực. Thảo luận cách bạn xây dựng câu chuyện dữ liệu cho những phân tích này. Bao gồm các yếu tố của một câu chuyện dữ liệu hiệu quả.

4. (LO 1) Thảo luận tại sao câu chuyện dữ liệu là một cách hiệu quả để truyền đạt đưa ra kết quả phân tích dữ liệu.

5. (LO 2) Thảo luận tại sao việc xác minh dữ liệu của bạn trước khi bắt đầu lại quan trọng cắt giảm giao tiếp phân tích dữ liệu của bạn.

6. (LO 2) So sánh và đối chiếu cách giao tiếp với người mới bắt đầu kiểm tra ence so với khán giả điều hành.

7. (LO 2) So sánh và đối chiếu giao tiếp với quản lý khán giả so với khán giả chuyên gia.

8. (LO 2) Thảo luận cách bảng thông tin có thể giúp truyền đạt dữ liệu phân tích kết quả ysis cho người quản lý.

9. (LO 2) Thảo luận xem mục tiêu của phân tích có thể giúp ngăn chặn như thế nào khai thác loại trực quan nên được sử dụng.

10. (LO 3) Thảo luận cách áp dụng định luật liên tục cho dữ liệu trực quan hóa.

11. (LO 3) Thảo luận cách áp dụng luật tương tự cho dữ liệu trực quan hóa.

12. (LO 3) Thảo luận cách áp dụng định luật tiệm cận cho dữ liệu trực quan hóa.

13. (LO 3) Thảo luận cách áp dụng định luật tiêu điểm cho dữ liệu trực quan hóa.

14. (LO 3) Thuộc tính cẩn thận là gì và tại sao chúng lại quan trọng khi chuẩn bị hình dung?

15. (LO 4) Hãy cho một ví dụ về cách điều khiển trục y có thể làm cho hình dung bị sai lệch.

16. (LO 4) Về việc tạo hình ảnh trực quan, hãy thảo luận về những gì đang diễn ra chống lại các quy ước có nghĩa là và đưa ra một ví dụ.

17. (LO 4) Thảo luận tại sao việc bỏ qua đường cơ sở trong hình ảnh trực quan có thể gây hiểu lầm.

18. (LO 5) So sánh và đối chiếu trực quan hóa tĩnh với tương tác những hình dung trực quan.

19. (LO 5) Thảo luận về lợi ích của việc sử dụng trực quan hóa dữ liệu tương tác và đưa ra ví dụ về cách trực quan hóa dữ liệu tương tác có thể được sử dụng trong một bài thuyết trình trực tiếp.

20. (LO 5) Thảo luận các phương pháp hay nhất để trình bày kết quả phân tích dữ liệu tới khán giả trực tiếp. BE 9.1 (LO 1) Kế toán tài chính Công ty của bạn đang xem xét một số cơ hội đầu tư. Bạn đã thu thập dữ liệu về các khoản đầu tư và chuẩn bị phân tích rủi ro. Hãy giải thích tại sao mỗi Sau đây là những điều quan trọng cần cân nhắc khi bạn bắt đầu chuẩn bị truyền đạt thông tin về phân tích rủi ro:

1. Hiểu khán giả.

2. Tập trung vào thông điệp.

3. Đặt dữ liệu vào ngữ cảnh.

4. Làm cho nó dễ hiểu.

5. Tạo một câu chuyện đáng nhớ. Bài tập ngắn gọn

**BE 9.2 (LO 1) Kế toán thuế U.S. Outdoor Adventures lo ngại về việc tuân thủ thuế bán hàng. Giám đốc sở thuế đã yêu cầu bạn phân tích doanh thu của công ty trong năm nay và thuế doanh thu đáng lẽ phải được thu thập. Bạn đã thực hiện phân tích và đang chuẩn bị truyền đạt ý kiến của mình kết quả cho giám đốc. Mô tả cách áp dụng từng điều sau đây vào việc trình bày kết quả của bạn trước giám đốc thuế. 1. Hiểu khán giả. 2. Tập trung vào thông điệp. 3. Đặt dữ liệu vào ngữ cảnh. 4. Làm cho nó dễ hiểu. 5. Tạo một câu chuyện đáng nhớ.**

**BE 9.3 (LO 1) Kiểm toán Bạn là kiểm toán viên đã thực hiện phân tích giao dịch mua hàng của khách hàng của bạn giao dịch thẻ (P-card). Mục tiêu của việc phân tích là kiểm tra các biện pháp kiểm soát của khách hàng đối với sử dụng thẻ mua hàng của nhân viên. Bạn đã sử dụng tất cả dữ liệu giao dịch thẻ P trong năm được kiểm toán để đánh giá các biện pháp kiểm soát sau: • Nhân viên chưa vượt quá hạn mức chi tiêu cho mỗi giao dịch. • Nhân viên chưa vượt quá hạn mức chi tiêu hàng tháng. • Tất cả các giao dịch mua đều được ghi lại kèm theo mô tả. • Tất cả các giao dịch mua đều có sự chấp thuận của người giám sát. Trong quá trình phân tích, bạn phát hiện ra có một số vi phạm chính sách, nhưng nhìn chung chúng đều vi phạm quy mô nhỏ và có sự tham gia của nhiều nhân viên/giám sát khác nhau. Tuy nhiên, một nhân viên và người giám sát đã rất lo lắng. vi phạm nghiêm trọng. Sau khi phân tích sâu hơn, bạn có thể xác định một kiểu chi tiêu đáng ngờ. sử dụng Kim tự tháp của Freytag để phác thảo cách bạn kể câu chuyện này. BE 9,4 (LO 2) Kế toán tài chính Công ty của bạn đang xem xét một số cơ hội đầu tư. Bạn đã thu thập dữ liệu về các khoản đầu tư và chuẩn bị phân tích rủi ro. Kiến thức của bạn sẽ là gì? khán giả cần hiểu được việc truyền đạt kết quả của bạn? BE 9,5 (LO2) Kiểm toán Kế toán tài chính Kế toán quản trị Hãy ghép từng câu sau- giảm xuống mức hình dung tốt nhất. Các lựa chọn hiển thị có thể được sử dụng một lần, nhiều lần hoặc không sử dụng chút nào. Một. Biểu đồ thanh b. Biểu đồ đường c. Biểu đồ thanh xếp chồng d. biểu đồ phân tán đ. Biểu đồ bong bóng Mục đích Trực quan hóa 1. Hiển thị sự phân bổ giá cho một mặt hàng cụ thể sản phẩm. 2. Thể hiện thành phần tổng chi phí. 3. Hãy thể hiện mối quan hệ giữa nhiệt độ và doanh số bán súp tại một nhà hàng. 4. Hiển thị xu hướng bán hàng theo thời gian. 5. Thể hiện sự phân bổ doanh số theo quốc gia. 6. Hiển thị so sánh doanh số theo năm. BE 9,6 (LO 3) Dữ liệu Kế toán tài chính Kế toán quản trị Sử dụng dữ liệu có sẵn, tạo một biểu đồ đường cho thấy xu hướng trả lương làm thêm giờ trong năm. Hãy chắc chắn làm theo các phương pháp hay nhất cho tạo biểu đồ đường. BE 9,7 (LO 3) Dữ liệu Kế toán tài chính Tạo biểu đồ cột so sánh doanh số sản phẩm năm 2024 và năm 2025 cho các thành phố sau: Denver, Loveland, Lafayette và Brookfield. Hãy chắc chắn để làm theo tốt nhất thực hành để tạo biểu đồ.**

Bài tập ngắn 9-49 BE 9,8 (LO 2, 3) Dữ liệu Kế toán tài chính Kế toán thuế Hình ảnh sau đây là chuẩn bị truyền đạt phân tích về việc hoàn trả của nhân viên cho nhân viên thành phố. Khán giả dành cho trực quan hóa là nhóm kiểm toán nội bộ. Mục tiêu là xác định các phòng ban có hiệu quả cao nhất số tiền hoàn trả cho nhân viên trong các năm 2022 đến 2025. 50.000 USD $0 100.000 USD 150.000 USD 200.000 USD 250.000 USD 300.000 USD 2022 2023 Năm 2024 2025 Sở Xây dựng Sở Y tế Sở Giao thông vận tải Chicago Văn phòng thông tin khẩn cấp Cục quản lý nước

1. Xác định những điều chỉnh/cải tiến có thể có cho việc hình dung này.

2. Chuẩn bị một hình dung đã chỉnh sửa. BE 9.9 (LO 3) Kiểm toán Kế toán tài chính Kế toán quản trị Hình ảnh sau đây- Việc phân tích đã được chuẩn bị để thể hiện lợi nhuận theo mùa của một tiệm bánh trong năm trước. Lợi nhuận theo mùa 1.000 USD 2.000 USD 3.000 USD 4.000 USD 5.000 USD 6.000 USD 7.000 USD 8.000 USD $- 9.000 USD Tháng Hai Tháng ba. Tháng Tư. tháng 5 Tháng Sáu. Tháng Bảy. Tháng 8 Tháng 10

1. Xác định những điều chỉnh/cải tiến có thể cần được xem xét để cải thiện hình ảnh trực quan.

2. Thảo luận tại sao những cải tiến được đề xuất của bạn là cần thiết.

**BE 9.10 (LO 3, 4) Dữ liệu Kế toán tài chính Một chuỗi khách sạn đã chuẩn bị một hình ảnh trực quan hiển thị tăng trưởng doanh thu từ năm 2022 đến năm 2025. Đối tượng xem trực quan là các nhà đầu tư tiềm năng. Tổng cộng 1.660.000.000 USD 1.680.000.000 USD 1.700.000.000 USD 1.640.000.000 USD 1.720.000.000 USD 1.740.000.000 USD 1.780.000.000 USD 1.760.000.000 USD 1.800.000.000 USD 1.820.000.000 USD 2022 2023 2024 2025 1. Xác định và thảo luận về bất kỳ yếu tố nào có thể gây nhầm lẫn cho việc hình dung. 2. Xác định xem có bất kỳ vi phạm nào đối với các phương pháp hay nhất hay không. 3. Chuẩn bị một hình dung đã chỉnh sửa.**

**BE 9.11 (LO 4) Dữ liệu Kế toán tài chính Bạn là kế toán viên thành phố đang phân tích việc trả lương làm thêm giờ cho sở cứu hỏa. Xem lại hình ảnh trực quan do người khác trong bộ phận của bạn chuẩn bị. Tháng Làm thêm giờ $0 1 2 3 4 5 6 7 8 9 10 11 12 2.000.000 USD 4.000.000 USD 6.000.000 USD 8.000.000 USD 10.000.000 USD 12.000.000 USD 14.000.000 USD 16.000.000 USD 18.000.000 USD 20.000.000 USD 1. Thảo luận xem việc hình dung có gây nhầm lẫn hay không và nếu có thì bằng cách nào? 2. Chuẩn bị một hình dung đã chỉnh sửa.**

Bài tập ngắn 9-51

**BE 9.12 (LO 4) Dữ liệu Kế toán tài chính Kế toán quản lý Cuộc phiêu lưu ngoài trời ở Hoa Kỳ đã yêu cầu phân tích doanh số bán hàng cho năm 2024 và 2025. Mục tiêu của phân tích là so sánh doanh số bán hàng từ 2024 đến 2025 và xác định xem có loại sản phẩm nào đang tăng hay giảm hay không. Phân tích sau đây đã được chuẩn bị cho đội ngũ quản lý. So sánh doanh số hàng năm theo sản phẩm Dụng cụ cắm trại Lều mái chèo 2024 2025 Dụng cụ cắm trại Lều mái chèo 1. Việc trực quan hóa dữ liệu này có phù hợp với phân tích này không? Thảo luận tại sao nó phù hợp hoặc không phù hợp. 2. Chuẩn bị một hình dung khác. Giải thích tại sao hình dung của bạn phù hợp hơn.**

**BE 9.13 (LO 5) Dữ liệu Kế toán quản lý Hình ảnh trực quan sau đây được chuẩn bị cho Huskie Tập đoàn ô tô để phân tích các kênh bán hàng. HMC muốn hiểu rõ hơn về lợi nhuận của nhân viên, chính phủ và các phương án thanh toán mua hàng (tiền mặt, tài trợ hoặc cho thuê). Thu nhập trước thuế: Mua hàng của nhân viên và chính phủ (2) Tatra Jackson apechete Chính phủ Tatra Jackson apechete Nhân viên/ Đối tác Chương trình $0K Thương hiệu Trần bán hàng.. –$600K–$500K–$400K–$300K–$200K–$100K $100K $200K $300K $400K $500K $600K $700K $800K $900K $1.000K Thu nhập trước thuế Thu nhập trước thuế –$1K $1K 1. Đề xuất cách thức trực quan hóa này có thể mang tính tương tác. 2. Tạo hình ảnh tương tác mà bạn đề xuất.**

**BE 9.14 (LO 2, 5) Dữ liệu Kiểm toán Kế toán tài chính Kế toán quản trị Sau đây- trực quan hóa đã được chuẩn bị để giúp Denton Hospitality phân tích lợi nhuận theo vị trí khách sạn. Mỗi dấu chấm trên biểu đồ phân tán thể hiện một vị trí khách sạn riêng lẻ. Khán giả của buổi thuyết trình sẽ là các chuyên gia. 1.400.000 USD 600.000 USD 800.000 USD 1.000.000 USD 1.200.000 USD –$200,000 0 200.000 USD 400.000 USD –$400,000 Lợi nhuận 20 50 10 40 0 30 60 1. Dựa trên khán giả là chuyên gia, bạn sẽ thay đổi hoặc nâng cao điều gì cho buổi thuyết trình trực tiếp? 2. Chuẩn bị biểu đồ phân tán đã hiệu chỉnh dựa trên đề xuất của bạn.**

**BE 9.15 (LO 5) Dữ liệu Kế toán tài chính Kế toán quản trị Hình ảnh sau đây- đã được chuẩn bị cho Cuộc phiêu lưu ngoài trời ở Hoa Kỳ để giúp họ phân tích doanh số bán hàng. Doanh thu thuần theo danh mục sản phẩm: 2022–2025 $460K $480K $440K $420K $400K $380K $360K $340K $320K $300K $280K $240K $260K $220K Dụng cụ cắm trại mái chèo Lều Doanh thu thuần $200K $180K $120K $140K $160K $174K $207K $288K $139K $138K $173K $204K $305K $329K $400K $442K $159K $174K $207K $288K $139K $138K $173K $204K $305K $329K $400K $442K $159K $60K $80K $100K $40K $20K $0K 2025 2024 2023 2022 2025 2024 2023 2022 Năm 2025 2024 2023 2022 Xác định các cách làm cho hình ảnh trực quan này mang tính tương tác để người dùng có thể đi sâu vào và xem các phương pháp khác nhau như thế nào. sản phẩm đang hoạt động. Sau đó, tạo hình ảnh trực quan. Bài tập**

**EX 9.1 (LO 1, 2, 3, 5) Dữ liệu Kế toán quản lý Tạo hình ảnh trực quan để phân tích doanh số và Profitability Super Scooters là một công ty sản xuất và bán bốn loại xe tay ga khác nhau: Thuyền trưởng, Celeritas, Kicks và Lazer. Bạn là kế toán tại Super Scooters và CEO đã yêu cầu phân tích doanh thu và lợi nhuận của các mô hình trong ba năm qua. 1. Chuẩn bị phân tích doanh thu và lợi nhuận. Thực hiện theo các phương pháp hay nhất được nêu trong chương. 2. Thảo luận cách bạn có thể làm cho các phân tích trở nên hấp dẫn đối với khán giả mà bạn đang trình bày.**

**EX 9.2 (LO 2, 3, 5) Dữ liệu Kế toán thuế Sử dụng hình ảnh trực quan để phân tích chi phí được khấu trừ Bạn là nhân viên kế toán thuế cho Ace Software, một công ty phần mềm máy tính, được giao nhiệm vụ thực hiện một công việc phân tích chi phí giải trí của doanh nghiệp. Theo luật thuế hiện hành, bữa ăn công tác được khấu trừ 50% ible. Chi phí giải trí (golf, vé sự kiện thể thao, v.v.) không được khấu trừ. 1. Chuẩn bị một hình ảnh tóm tắt chi tiêu cho việc giải trí. Thực hiện theo các phương pháp hay nhất được nêu trong chương. 2. Thiết kế trực quan hóa tương tác cho phép phân tích ở cấp độ nhân viên.**

**EX 9.3 (LO 2, 3) Dữ liệu Kế toán quản lý Tạo trực quan hóa để phân tích biến Chi phí Super Scooters sản xuất và bán bốn loại xe tay ga khác nhau: Captain, Celeritas, Kicks và Lazer. Bạn được yêu cầu thực hiện phân tích chi phí biến đổi theo mẫu mã và năm. 1. Chuẩn bị trực quan hóa dữ liệu giải thích về chi phí biến đổi. Bạn có thể sử dụng Excel, PowerBI hoặc Tableau để chuẩn bị các hình ảnh trực quan. Hãy chắc chắn làm theo tất cả các thực hành tốt nhất.**

Bài tập 9-53

2. Thảo luận cách bạn truyền đạt phân tích của mình tới từng đối tượng sau: • Người mới • Chuyên gia • Quản lý • Điều hành EX 9.4 (LO 1, 2, 3) Dữ liệu Kiểm toán Sử dụng Trực quan hóa để Phân tích Xu hướng Doanh thu Bạn là một kiểm toán viên cho công ty kế toán Banes, Kent và Williams. Là một phần của quá trình kiểm tra Super Scooters, bạn đã được yêu cầu tạo một hình ảnh trực quan để hiển thị phân tích xu hướng về doanh thu bán hàng. Mục tiêu của phân tích là để xác định xem có bất kỳ thay đổi bất thường nào về doanh số bán hàng so với những năm trước hoặc các xu hướng khác hay không có thể ảnh hưởng đến rủi ro có sai sót trọng yếu.

1. Chuẩn bị một bản trực quan có thể phân tích những thay đổi trong doanh số và xu hướng bán hàng.

2. Thảo luận tại sao những hình ảnh trực quan bạn chọn là phù hợp.

3. Thảo luận cách bạn truyền đạt phân tích của mình tới từng đối tượng sau: • Người mới • Chuyên gia • Quản lý • Điều hành EX 9.5 (LO 3) Dữ liệu Kế toán tài chính Tạo trực quan hóa để phân tích dữ liệu bảng lương Thực hiện phân tích tiền làm thêm giờ được trả theo bộ phận và tháng cho thành phố Chicago. Sử dụng trực quan phần mềm để tạo trực quan hiển thị như sau:

1. Các bộ phận có tổng số giờ làm thêm cao nhất.

2. Xu hướng làm thêm hàng tháng của bộ phận có tổng số giờ làm thêm cao nhất.

3. Những nhân viên có tổng số giờ làm thêm cao nhất trong năm ở bộ phận có tổng số giờ làm thêm cao nhất số tiền làm thêm giờ. EX 9.6 (LO 5) Dữ liệu Kế toán tài chính Tạo trực quan hóa tương tác Ngoài trời Hoa Kỳ Adventures muốn sử dụng bảng điều khiển tương tác để đánh giá doanh số và lợi nhuận của sản phẩm. Xem lại trực quan hóa tĩnh trong một trong các tệp Excel, PowerBI hoặc Tableau do bộ phận kế toán chuẩn bị tại Cuộc phiêu lưu ngoài trời của Hoa Kỳ. Chuyển đổi trực quan hóa tĩnh thành trực quan hóa tương tác để quản lý- ment có thể sử dụng để theo dõi lợi nhuận của sản phẩm theo danh mục phụ và vị trí. EX 9.7 (LO 1, 2, 3) Dữ liệu Kế toán quản lý Tạo hình ảnh trực quan để đưa ra quyết định Bạn là nhà phân tích tài chính làm việc trong nhóm vận hành tại Super Scooters. Nhóm điều hành là liên nằm trong xu hướng bán hàng của các mẫu xe tay ga. Cụ thể, họ muốn hiểu tổng doanh thu theo mô hình và khối lượng bán hàng theo mẫu mã để xác định những mẫu mã nào đang tăng lên theo các thước đo này. Những cái cao đó những người mẫu hoạt động tốt sẽ nhận được nhiều phân bổ đô la tiếp thị hơn.

1. Phân tích số tiền bán hàng, khối lượng bán hàng và khối lượng bán hàng theo mô hình trong ba năm qua. hiện tại trực quan hóa để truyền đạt kết quả cho nhóm điều hành. Bạn sẽ cần nhiều hơn một hình ảnh Alization để tạo ra một câu chuyện thích hợp cho đội ngũ điều hành.

2. Sử dụng kim tự tháp Freytag để kể câu chuyện. Đưa ra các khuyến nghị cho đội ngũ điều hành về việc phân bổ đô la tiếp thị cho các mô hình có hiệu suất cao. EX 9.8 (LO 2, 3) Dữ liệu Kế toán tài chính Tạo hình ảnh trực quan để mô tả bảo hành Expenses High-End Hubs (HEH) là một đơn vị tư nhân sản xuất và bán các bộ phận bánh xe đạp. Khách hàng chính của họ là các nhà sản xuất xe đạp leo núi cao cấp. Bộ điều khiển đã yêu cầu bạn hiểu lợi nhuận bảo hành năm nay so với năm ngoái. Mục tiêu của bạn là xác định các mô hình và bộ phận những con số có vấn đề về bảo hành trong năm hiện tại và để xác định các giả định để sử dụng trong bảo hành tính lũy kế cuối năm. Chuẩn bị hình ảnh mô tả về lợi nhuận bảo hành so với doanh số bán hàng theo mô hình cho năm nay và năm ngoái. EX 9.9 (LO 1, 2, 3) Dữ liệu Kiểm toán Truyền đạt rủi ro có sai sót trọng yếu bằng cách sử dụng Hình dung Bạn là kiểm toán viên cho công ty kế toán Banes, Kent và Williams. Là một phần của cuộc kiểm toán của Super Scooters, bạn phải tạo hình ảnh trực quan để truyền đạt xu hướng doanh thu bán hàng theo từng mẫu xe. Mục tiêu của việc phân tích là truyền đạt những thay đổi trong xu hướng bán hàng từ năm trước để thông báo cho bạn xem xét rủi ro có sai sót trọng yếu liên quan đến việc ghi nhận doanh thu cho cuộc kiểm toán năm hiện tại.

1. Tạo hình ảnh trực quan để hiển thị tổng doanh thu hàng năm theo địa điểm.

2. Tạo hình ảnh trực quan để hiển thị tổng doanh thu hàng năm theo mô hình và địa điểm.

3. Sử dụng kim tự tháp của Freytag để kể câu chuyện về từng hình ảnh trực quan và cách nó có thể cung cấp thông tin cho quá trình kiểm tra Siêu xe tay ga. Hãy nhớ rằng đối tượng của bạn đối với những hình ảnh và câu chuyện này là nhóm kiểm tra và các hồ sơ kiểm toán.

**EX 9.10 (LO 1, 2) Kế toán tài chính Kế toán quản trị Tạo câu chuyện dựa trên Khán giả Bạn là nhà phân tích tài chính của SWI, Inc. SWI là nhà sản xuất và phân phối các thiết bị vi mô chip và bộ vi xử lý. Công ty bán sản phẩm của mình cho khách hàng ở một số quốc gia và khu vực bao gồm Úc, Liên minh Châu Âu, Bắc Mỹ và Nam Mỹ. Bạn đã chuẩn bị hồ sơ bảng hạ thấp và trực quan hóa hiển thị doanh số bán hàng ở từng khu vực khác nhau vào năm 2024 so với năm 2025. Úc Liên minh châu Âu Bắc Mỹ Nam Mỹ $ 1,417,584 $ 1,252,712 $1,239,689 $ 1,515,744 Vị trí 2024 Bán hàng theo địa điểm $ 1,134,785 $ 1,376,503 $1,624,719 $ 1,742,311 2025 Tổng cộng $ 5,425,729 $ 5,878,318 Ngày bán Địa điểm/Ngày bán Bán hàng theo địa điểm $0K $1,600K $1,515,444 $1,742,311 $1,624,719 $1,252,712 $1,376,503 $1,417,584 $1,134,785 $1,239,689 $1,515,744 $1,742,311 $1,624,719 $1,252,712 $1,376,503 $1,417,584 $1,134,785 $1,239,689 2.000 nghìn USD $1,800K $1,400K $1,200K Nam Mỹ Bắc Mỹ Liên minh châu Âu Úc Tổng Doanh thu $1,000K $600K $800K $400K $200K 2025 2024 2025 2024 2025 2024 2025 2024 Năm Với hình ảnh trực quan và bảng biểu, hãy sử dụng kim tự tháp Freytag để kể câu chuyện về doanh số bán hàng của công ty bạn bằng cách quốc gia từ góc độ của một nhà điều hành đang thảo luận về kết quả thực hiện cuộc gọi của nhà đầu tư. Sau đó, hãy kể cho câu chuyện từ quan điểm của một nhà điều hành đưa ra quyết định quản lý về hiệu suất bán hàng.**

Bài tập 9-55

**EX 9.11 (LO 2, 3, 4) Dữ liệu Kiểm toán Đánh giá tài liệu phân tích dữ liệu Giả sử bạn là một nhân viên kiểm toán cấp cao phụ trách hợp đồng với SWI, Inc. SWI là công ty đại chúng sản xuất và phân phối tôn vinh vi mạch và bộ vi xử lý trên phạm vi quốc tế. Nhân viên nhóm đính hôn của bạn đã chuẩn bị một một loạt hình ảnh trực quan để xác định mức độ thử nghiệm cần được thực hiện ở từng khu vực theo mô hình. Cụ thể, nhóm tham gia cần hiểu rõ các khu vực và mô hình có sự thay đổi lớn nhất trong năm trước. Tổng doanh thu Tổng doanh thu theo năm Doanh số theo mẫu mã, khu vực và năm Năm bán.. người mẫu 500K Vi1×7 Vi1×9 Mitoxi1×4 Mitoxi1×7 1.000K 0K 1.500K 2.000K 2.500K 3.000K 4.000K 3.500K 4.500K 2024 2025 5.000K 5.500K 2024 2025 Năm bán ngày Úc Liên minh châu Âu Bắc Mỹ Nam Mỹ Vị trí 1. Cung cấp nhận xét đánh giá để cải thiện trang tổng quan. Xác định các hình ảnh trực quan gây hiểu lầm và cung cấp phản hồi để nâng cao hiệu quả tổng thể của việc trực quan hóa. 2. Chuẩn bị hình ảnh trực quan trên trang tổng quan để truyền đạt sự khác biệt về doanh số bán hàng theo khu vực theo mẫu mã.**

**EX 9.12 (LO 3) Dữ liệu Kế toán tài chính Tạo trực quan hóa để phân tích dữ liệu bảng lương Thực hiện phân tích mức lương được trả theo bộ phận và tháng cho thành phố Chicago. Sử dụng trực quan phần mềm để tạo trực quan hiển thị như sau: 1. Bộ phận có tổng mức lương dành cho nhân viên toàn thời gian cao nhất trong 3 bộ phận. 2. Năm phòng ban có số lượng nhân viên đông nhất. 3. 10 tổng lương cao nhất theo chức danh công việc.**

**EX 9.13 (LO 5) Dữ liệu Kế toán quản lý Tạo trực quan hóa tương tác Ngoài trời Hoa Kỳ Adventures muốn sử dụng bảng điều khiển tương tác để đánh giá chi phí sản phẩm và vận chuyển. Xem lại tĩnh trực quan hóa bằng một trong các tệp Excel, PowerBI hoặc Tableau do bộ phận kế toán quản lý chuẩn bị. tâm trí. Chuyển đổi trực quan hóa tĩnh thành trực quan hóa tương tác để ban quản lý có thể giám sát chi phí sản phẩm theo danh mục phụ và vị trí cũng như chi phí vận chuyển theo danh mục phụ, địa điểm và phương thức vận chuyển.**

**EX 9.14 (LO 2, 3) Dữ liệu Kiểm toán Sử dụng hình ảnh trực quan để truyền đạt tạp chí bất thường Bài viết HEH, Inc. là một công ty tư nhân có lịch cuối năm. Bạn là nhân viên kiểm toán được giao nhiệm vụ hợp đồng và chuyên gia kiểm toán của bạn đã yêu cầu bạn phân tích các giao dịch sổ cái chung trong năm hiện tại và xác định bất kỳ khoản mục bất thường nào có thể đã được ghi lại. Tạo hình ảnh trực quan minh họa các mục nhật ký bất thường. Ví dụ, hãy xem xét những điều sau đây: 1. Nhật ký được ghi vào ngày thứ Bảy. 2. Mục nhật ký trong đó mục ghi nhớ có điều chỉnh từ. 3. Các mục nhật ký trong đó mục ghi nhớ có từ “plug”.**

**EX 9.15 (LO 2, 3) Dữ liệu Hệ thống thông tin kế toán Sử dụng hình ảnh trực quan để truyền đạt cate Nhật ký phân tích kết quả Bạn là nhân viên kế toán hệ thống thông tin tại công ty của bạn, TBARk, một công ty công ty bán lẻ nhỏ bán cả trực tuyến và tại các cửa hàng truyền thống. Hàng quý, nhóm của bạn kiểm tra phân tích nhật ký của nhân viên để đảm bảo tuân thủ chính sách của công ty. Các chính sách chính tại công ty bao gồm: 1. Nhân viên chỉ nên đăng nhập vào một hệ thống POS tại một thời điểm. 2. Nhân viên phải đăng xuất khi không sử dụng hệ thống POS để bán hàng cho khách hàng. 3. Nhân viên công ty và văn phòng hỗ trợ không nên đăng nhập vào hệ thống POS. Bạn sẽ thông báo kết quả của mình cho người quản lý nhóm của bạn, một chuyên gia về thông tin kế toán. hệ thống quản lý, điều khiển và phân tích nhật ký. Chuẩn bị hình ảnh trực quan để kiểm tra từng chính sách bằng cách sử dụng tốt nhất thực tiễn để truyền đạt kết quả phân tích của bạn về từng chính sách.**

**EX 9.16 (LO 3, 4) Dữ liệu Kế toán tài chính Xác định hình ảnh hóa dữ liệu gây hiểu lầm mà bạn là nhà phân tích tài chính của Adventure Sports and Outdoors, một công ty bán lẻ chuyên bán thuyền, phụ kiện chèo thuyền và thiết bị an toàn. Nhóm mua hàng của bạn đang xem xét các hợp đồng với nhà cung cấp chính. Mục đích nhóm theo đuổi đã thực hiện các phân tích liên quan đến số tiền chi tiêu với mỗi nhà cung cấp và đã đưa ra kết luận về hành vi mua hàng. Phân tích của nhóm mua hàng sau đây và kết luận đã được trình bày cho bạn. Tên nhà cung cấp Bertram Hiệu suất cao... An toàn đầu tiên Wow Sports, Inc. Người săn cá voi ở Boston MasterCraf Nút thắt SGT Wakesurf, Inc. Số lượng hóa đơn hóa đơn TTL Số lượng hóa đơn theo nhà cung cấp Tên nhà cung cấp Chi phí hóa đơn theo nhà cung cấp Tên nhà cung cấp 0 Bertram Boston... CaoP... Thầy... An toàn... SGT Kn... Wakesu... Ôi S... Bertram Boston... CaoP... Thầy... An toàn... SGT Kn... Wakesu... Ôi S... 10 20 –10 30 40 50 60 70 90 80 100 110 120 130 5K 10K 15K 20K 25K 30K 35K 40K 50K 45K 55K 60K 65K 70K 1. Xác định các yếu tố gây hiểu lầm hoặc không hiệu quả trong những hình dung này. 2. Chuẩn bị hình ảnh trực quan thể hiện chính xác hơn hoạt động mua hàng của từng nhà cung cấp. Bài tập 9-57**

**EX 9.17 (LO 4) Dữ liệu Hệ thống thông tin kế toán Xác định hình ảnh trực quan gây hiểu lầm trong Kiểm tra kiểm soát Bạn là nhân viên kế toán hệ thống thông tin kế toán tại SWI Inc. Nhóm của bạn là đánh giá các biện pháp kiểm soát công nghệ thông tin liên quan đến quy trình phê duyệt bán hàng cho năm 2025. Kiểm soát quy trình phê duyệt bán hàng của SWI được thiết kế như sau: • Tất cả doanh số bán hàng trên $10.000 và doanh số bán hàng có sửa đổi đối với điều khoản bán hàng chung phải được phê duyệt bởi người quản lý bán hàng được chỉ định. • Có ba giám đốc bán hàng tại SWI: Mary Ann Parola quản lý thị trường Úc và Nam Mỹ khu vực, Hamish Rundan quản lý các khu vực Bắc Mỹ và Shonie Oscenbono quản lý khu vực Liên minh Châu Âu. Nhân viên kế toán AIS của bạn đã chuẩn bị các hình ảnh trực quan sau đây để truyền đạt hiệu quả hoạt động- tính chất của việc kiểm soát. Không 2 5 0 10 20 30 40 50 60 70 80 90 100 110 120 130 Mary Ann Parola Mary Ann Parola Shonie Oscebono Hamish Rundan Không Không Không 88 98 88 122 8 3 Vị trí/Bán hàng được phê duyệt Úc Liên minh Châu Âu Bắc Mỹ Nam Mỹ Số lượng Tổng doanh thu Kiểm soát phê duyệt bán hàng Xem lại hình ảnh trực quan cùng với dữ liệu: 1. Xác định các trường hợp trong đó hình ảnh trực quan không truyền đạt kết luận một cách thích hợp. 2. Chuẩn bị hình ảnh đã chỉnh sửa**

**EX 9.18 (LO 4) Kế toán quản trị Xác định những hình ảnh trực quan gây hiểu lầm Với tư cách là chuyên gia tài chính cấp cao nhà phân tích tại Super Scooters, nhóm của bạn đang chuẩn bị cho buổi thuyết trình với một nhóm sinh viên để giáo dục họ về chi phí biến đổi trong quá trình sản xuất. Bạn đã nhận được sự chấp thuận từ người điều hành nhóm chia sẻ dữ liệu công ty, nhưng bạn biết rằng đây là đối tượng mới làm quen. Nhân viên của bạn đã chuẩn bị hình ảnh trực quan sau đây để truyền đạt xu hướng lao động, vật chất, chi phí chung và tổng chi phí được phân bổ liên quan đến việc sản xuất và bán mẫu Celeritas. Lao động $500K 1.000 nghìn USD $1,500K 2.000 nghìn USD Vật liệu Chi phí chung Tổng số được phân bổ Chi phí cố định Chi phí thay đổi thuyền trưởng người mẫu Giá trị thuyền trưởng Xem lại hình ảnh trực quan do nhân viên của bạn chuẩn bị và giải thích cách nó có thể được cải thiện để trình bày. tiếp cận khán giả mới làm quen.**

**EX 9.19 (LO 5) Dữ liệu Kế toán tài chính Xây dựng trình bày trực quan hóa dữ liệu tương tác- Bán hàng HEH, Inc. bán phụ tùng xe đạp B2B, nghĩa là họ chủ yếu bán cho các công ty sản xuất và lắp ráp xe đạp. Tạo hai hình ảnh trực quan bán hàng và bảng thông tin tương tác điều đó sẽ cho phép bạn trình bày phân tích của mình với người quản lý bán hàng của công ty. Nhớ sử dụng tốt nhất thực tiễn trong việc tạo hình ảnh trực quan và tạo trang tổng quan tương tác.**

**EX 9.20 (LO 2, 3, 4) Dữ liệu Kiểm toán Đánh giá bản phân tích do khách hàng chuẩn bị về xu hướng bán hàng này là năm đầu tiên công ty của bạn thực hiện kiểm toán One Stop Shop. Nhóm đang thực hiện các phân tích để đạt được hiểu biết sâu sắc vị thế của khách hàng và ngành. One Stop Shop cung cấp cho nhóm của bạn bản phân tích về doanh số bán hàng của họ xu hướng và kết hợp sản phẩm từ năm 2022 đến năm 2025. 2022 160 triệu USD 165 triệu USD 170 triệu USD 175 triệu USD 180 triệu USD 185 triệu USD 190 triệu USD 195 triệu USD 2025 Phân tích xu hướng bán hàng: 2022–2025 Tổng lợi nhuận Cơ cấu doanh số sản phẩm: 2022–2025 Loại sản phẩm Mô tả Thức ăn trẻ em Đồ uống ngũ cốc Quần áo Mỹ phẩm trái cây hộ gia đình Thịt Vật tư văn phòng Chăm sóc cá nhân Đồ ăn nhẹ Rau củ 9,4% 27,7% 21,9% 2022 0,3% 16,4% 0,4% 4,3% 13,8% 22,5% 6,3% 3,8% 14,8% 0,4% 21,8% 2024 13,3% 21,2% 4,5% 2,3% 15,0% 0,3% 27,2% 2025 23,0% 14,4% 23,5% 15,2% 2023 0,4% 5,5% 3,1% 1. Đánh giá các hình ảnh trực quan do khách hàng cung cấp và xác định các vấn đề hoặc vấn đề tiềm ẩn với trực quan hóa. 2. Tạo hình ảnh trực quan hiệu quả hơn. Vấn đề Pueblo Hospitality, Inc. (PHI) vận hành chuỗi 48 khách sạn ở một số bang. Stephanie Putnam là chủ tịch và giám đốc điều hành của PHI. Các khách sạn của PHI nằm trong phân khúc lưu trú bình dân. Một nền kinh tế điển hình khách sạn lưu trú có trung bình 84 phòng, mặc dù khách sạn của PHI có trung bình 117 phòng. Tài sản có nhân viên bởi một tổng giám đốc, nhân viên lễ tân gồm 6 người, một quản gia trưởng, 7 quản gia và một nhân viên bảo trì. công nhân tài chính. Ngoại trừ tổng giám đốc, nhân viên được trả lương theo giờ và số giờ được phân công của họ khác nhau dựa trên nhu cầu.**

Trường hợp đăng ký chuyên nghiệp: Thư viện công cộng Madison 9-59 PHI sử dụng các tiêu chuẩn hiệu suất sau. Đo lường Mục tiêu Doanh thu trên mỗi phòng trống (RevPAR) Tăng 2% so với năm trước Sự hài lòng của khách hàng 7,5 Năng suất dọn phòng 30 phút mỗi phòng Điểm kiểm tra 7,0 Dữ liệu PR 9.1 (LO 1, 3, 5) Kế toán tài chính Tạo một câu chuyện dữ liệu để phân tích lợi nhuận phân tích doanh thu trên mỗi phòng có sẵn (RevPAR). Phân tích của bạn phải bao gồm doanh thu, lợi nhuận, trung bình doanh thu trên mỗi phòng sẵn có và doanh thu trung bình của đối thủ cạnh tranh trên mỗi phòng sẵn có. Chuẩn bị dữ liệu tương tác hình ảnh để trình bày với CEO. Dữ liệu PR 9.2 (LO 1, 2, 3, 5) Kế toán quản trị Tạo Bảng điều khiển cho Quản lý Đối tượng Chuẩn bị bản phân tích về hiệu suất của PHI cho từng mục tiêu hiệu suất. Tạo một dấu gạch ngang- hội đồng quản trị sẽ hữu ích cho việc quản lý để theo dõi hiệu suất. Đảm bảo rằng bảng điều khiển cho phép các nhà quản lý để xem các khách sạn riêng lẻ đang hoạt động như thế nào cũng như hiệu suất tổng thể của công ty. Dữ liệu PR 9.3 (LO 1, 2, 3, 5) Kiểm toán Tạo hình ảnh trực quan để đánh giá rủi ro doanh thu Bạn đã được giao cho nhóm kiểm toán để kiểm toán Pueblo Hospitality. Người quản lý của bạn đã yêu cầu bạn sử dụng hình ảnh hóa dữ liệu để hiểu rõ hơn về doanh thu. Cụ thể, bạn đã được yêu cầu đánh giá mối quan hệ giữa số phòng thuê và doanh thu và xác định những bất thường mô hình hoặc quan sát.

1. Lập bản phân tích đánh giá doanh thu năm nay so với năm trước.

2. Chuẩn bị bản phân tích cho thấy các ngoại lệ tiềm ẩn theo ID thuộc tính.

3. Chuẩn bị một câu chuyện dữ liệu kèm theo những hình ảnh trực quan của bạn để cung cấp cho người quản lý và thảo luận về kết quả của bạn. Trường hợp ứng dụng chuyên nghiệp: Thư viện công cộng Madison Thư viện Công cộng Madison (MPL) là một cơ quan của Thành phố Madison, Wisconsin. Sứ mệnh của thư viện là để “cung cấp quyền truy cập miễn phí và công bằng vào các trải nghiệm văn hóa và giáo dục”. Tầm nhìn của nó là trở thành “nơi để học hỏi, chia sẻ và sáng tạo”. Thư viện được điều hành bởi một ban giám đốc gồm chín thành viên được thị trưởng Madison bổ nhiệm với nhiệm kỳ ba năm. Ban thư viện làm việc với thị trưởng, thư viện nhân viên và Hội đồng chung Madison để lập kế hoạch, tài trợ và triển khai dịch vụ thư viện công cộng ở Madison. Thư viện được hỗ trợ tài chính bởi thành phố Madison và Quỹ Thư viện Công cộng Madison. chuyện. Quỹ này thúc đẩy và hỗ trợ các cơ sở, dịch vụ và chương trình thư viện công cộng của Madison. Hội đồng quản trị của nó bao gồm 30 thành viên. Các sáng kiến của Hội đồng quản trị bao gồm tăng quà tặng hạn chế, cải thiện gây quỹ, xây dựng sự hợp tác chiến lược để tài trợ cho sự đổi mới và các nhu cầu cấp thiết, đồng thời hỗ trợ chủng tộc công bằng và hòa nhập vào các hoạt động của thư viện và tổ chức thông qua tài trợ, nhân viên và thành lập hội đồng quản trị. Thư viện bao gồm tám địa điểm. Địa điểm thư viện Alicia Ashman miền Trung táo gai Nhìn ra hồ đồng cỏ Pinney Sequoya Nam Madison 733 N Đường High Point 201 W Mifflin St 2707 E Đại lộ Washington 2845 N. Đại lộ Sherman 5726 Đường Raymond Đường 516 Cottage Grove 4340 Đại lộ Tokay 222 S Park St Địa chỉ đường phố Madison Madison WI Madison Madison Madison Madison Madison Madison Thành phố 53717 53703 53704 53704 53711 53716 53711 53713 Mã Zip WI WI WI WI WI WI WI tiểu bang Tên thư viện

MPL hoạt động như một tổ chức phi lợi nhuận. Sau đây là thông tin tài chính của bốn năm trước. Thông tin tài chính thư viện Chiếm đoạt Thư viện Thành phố Madison Dịch vụ hợp đồng của hệ thống thư viện trung tâm phía Nam Dịch vụ theo hợp đồng của Hệ thống Thư viện Quận Dane Dịch vụ hợp đồng LINK tài trợ Khác Tiền phạt và lệ phí Tài trợ Tiền lương và phúc lợi Thư viện Sách, Phương tiện và Cơ sở dữ liệu: Dịch vụ theo hợp đồng của Hệ thống Thư viện Quận Dane Cơ sở vật chất Nợ Hưu trí Vật tư và tài sản vốn LINKcat Hoạt động máy tính trực tuyến Dịch vụ đã mua, Khác Dòng vào ròng/(Dòng tiền ra) 13.026.440 1.040.746 1.537.180 1.227.112 2.826.376 482.606 623.845 541.895 $ $ $ $ $ $ $ $ 21.306.200 $ (624.450) $ 12.659.647 1.039.586 1.515.114 2.648.112 497.976 609.444 745.755 12.352.852 1.000.816 1.456.628 2.745.463 390.440 611.337 578.811 $ $ $ $ $ $ $ 11.474.221 1.046.644 1.357.358 2.720.545 330,283 592.158 604.312 $ $ $ $ $ $ $ $ $ $ $ $ $ $ 19.715.634 19.136.347 $ 18.125.521 $ $ (470.320) 101.275 $ (107.047) $ $ Năm kết thúc ngày 31 tháng 12 Doanh thu thư viện 2024 2023 2022 2025 Chi phí thư viện 395.478 17.703.566 1.144.935 404.255 335.984 602.994 74.538 20.000 337.246 – – – 17.779.030 454.290 383,403 149.459 121.886 20.000 337.361 16.915.564 454.255 395.421 1.010.390 104.631 20.000 356.336 16.288.835 454.255 404.399 370.254 124.395 20.000 $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ 19.245.314 19.237.622 18.018.474 $ $ $ $ $ $ $ $ $ $ $ 20.681.750 $ Thông tin tài chính này cho thấy thư viện đã phải chịu sự gia tăng dòng tiền ra ròng trong hai năm vừa qua. năm. Hội đồng MPL lo ngại rằng nếu luồng tiền ra ròng tiếp tục, các thư viện sẽ phải giảm dịch vụ cộng đồng. Sau đây là danh sách các số liệu có thể được sử dụng để đánh giá hiệu suất MPL. Thanh toán Thanh toán kỹ thuật số Sử dụng Internet Đăng ký thẻ thư viện Nhân viên thư viện Công dụng phòng họp Tham dự chương trình (mọi lứa tuổi) lượt truy cập 3,454,156 462.416 227.370 15.544 137 22.714 107.447 1.779.552 2025 3.575.215 382.068 247.129 12.154 135 22.278 136.303 1.911.287 2024 3.800.000 289.309 635.363 13.245 128 20.782 110.744 2.170.000 2022 3.698.903 564.787 11.775 131 23.010 134.666 1.965.014 2023 Số liệu:

**PAC 9.1 Hệ thống thông tin kế toán: Trực quan hóa việc sử dụng hệ thống máy tính Dữ liệu Hệ thống thông tin kế toán MPL đã chứng kiến ​​sự gia tăng việc sử dụng máy tính trong thời gian qua hai năm. Họ muốn đảm bảo rằng họ đang cung cấp máy tính cho các chi nhánh với nhiều khả năng sử dụng nhất và giảm số lượng máy tính tại các chi nhánh có mức sử dụng thấp hơn. Sử dụng dữ liệu sử dụng máy tính MPL để chuẩn bị một hình ảnh trực quan tương tác nhằm giúp bộ phận hệ thống thông tin kế toán đánh giá việc sử dụng máy tính và công nghệ theo chi nhánh. Kiểm toán PAC 9.2 : Trình bày phân tích chi phí tiền lương bằng câu chuyện dữ liệu Dữ liệu Kiểm toán Với tư cách là thành viên của nhóm kiểm toán đang kiểm tra chi phí tiền lương của MPL, bạn đã thu thập được danh sách tên nhân viên hiện tại và số tiền lương. Chuẩn bị một phân tích mô tả về chi phí tiền lương sử dụng trực quan hóa dữ liệu. Tóm tắt những phát hiện của bạn trong một câu chuyện dữ liệu.**

**PAC 9.3 Kế toán tài chính: Trực quan hóa phân tích doanh thu và chi phí Dữ liệu Kế toán tài chính Bạn được yêu cầu chuẩn bị bản phân tích doanh thu và chi phí từ năm 2016 đến năm 2025. Sử dụng dữ liệu tài chính MPL để chuẩn bị các hình ảnh trực quan có thể hiển thị cho bạn người quản lý.**

**PAC 9.4 Kế toán quản lý: Xây dựng bảng điều khiển hiệu suất tương tác Dữ liệu Kế toán quản trị Bạn đã được yêu cầu chuẩn bị một bảng điều khiển cho phép con người- để xem cả số liệu tài chính và phi tài chính cho hệ thống thư viện. Sử dụng dữ liệu quản lý để chuẩn bị một bảng điều khiển.**

Trường hợp tiếp theo của Le Grind: Truyền đạt kết quả và đề xuất cho phân tích lợi nhuận gộp Trường hợp tiếp theo của Le Grind: Truyền đạt kết quả và khuyến nghị cho tổng Phân tích lợi nhuận dữ liệu Truy cập nền tảng học tập trực tuyến của Wiley để biết thông tin cơ bản về trường hợp, các câu hỏi, dữ liệu bổ sung và biết thêm chi tiết về vụ án đang tiếp tục.

#### **English**
<iframe src="TaiLieu/textbookForPractice/Ch_09_Interpreting%20Data%20Analysis%20Results.pdf" width="100%" height="800px"></iframe>
<!-- tabs:end -->