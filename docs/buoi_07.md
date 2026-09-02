# Buổi 7: AI trong Tài chính Doanh nghiệp và Kiểm toán (Tự động hóa Kiểm soát Nội bộ & Phát hiện Gian lận)

<!-- tabs:start -->

#### ** 📚 Thuật ngữ & Khái niệm **

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Rủi ro tiềm tàng (Inherent Risk)</b></summary>
<br>

Là rủi ro tự nhiên sinh ra từ bản chất ngành nghề kinh doanh mà không có bất kỳ biện pháp bảo vệ nào. Ví dụ: Kinh doanh xăng dầu thì mặc định rủi ro cháy nổ là rất cao.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Rủi ro kiểm soát nội bộ (Internal Control Risk)</b></summary>
<br>

Rủi ro sinh ra khi hệ thống phòng thủ của công ty bị lủng, do Ban giám đốc quản lý kém, hoặc cố tình lách luật để tư lợi. Đây là mục tiêu tấn công chính của AI trong kiểm toán hiện đại.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Điểm yếu trọng yếu (Material Weaknesses)</b></summary>
<br>

Các lỗ hổng chết người trong hệ thống kiểm soát nội bộ, đủ lớn để khiến công ty sụp đổ (như Thomas Cook). Thách thức của kế toán là phải phát hiện ra lỗ hổng này bằng AI *trước cả khi* kỳ kiểm toán bắt đầu.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Môi trường kiểm soát (Control Environment)</b></summary>
<br>

Nền tảng cốt lõi của khung COSO, nó chính là "Văn hóa doanh nghiệp" và "Đạo đức của Ban giám đốc". Thứ vô hình này rất khó đo lường bằng phiếu khảo sát (vì nhân viên hay báo cáo láo) nhưng lại bị AI đọc vị dễ dàng.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Hệ thống Phòng thủ Chủ động (Proactive Defense System)</b></summary>
<br>

Chuyển dịch tư duy từ việc ghi chép quá khứ sang việc "cầm đèn chạy trước ô tô". AI giăng bẫy bắt lỗi kẻ gian lận ngay lúc chúng mới nhen nhóm ý định (giống phim Minority Report).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Nhiệt kế Đạo đức bằng NLP (Xử lý Ngôn ngữ Tự nhiên)</b></summary>
<br>

Công nghệ biến máy tính thành máy quét tâm lý. AI đọc lướt hàng vạn email lúc nửa đêm, tin nhắn nội bộ để đánh hơi "sự thay đổi thái độ", phát hiện các chỉ thị ngầm mang tính ép buộc của sếp.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Thuật toán TF-IDF (Tần suất thuật ngữ)</b></summary>
<br>

Một bộ đếm thông minh trong NLP. Nó cân đo đong đếm xem một từ vựng mờ ám có "sức nặng" bao nhiêu trong văn cảnh, giúp phân loại các báo cáo hoặc giao tiếp có chứa ý đồ thao túng.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Đánh giá Phong cách Quản lý (Management Philosophy)</b></summary>
<br>

AI sẽ dán nhãn xem văn hóa của Ban giám đốc là "Hợp tác" hay "Độc đoán" dựa trên từ vựng họ dùng. Một văn hóa sếp gào thét "Phải xong bằng mọi giá" sẽ bị AI đánh dấu Đỏ (rủi ro gian lận cao).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Quản trị Lợi nhuận (Earnings Management)</b></summary>
<br>

Một dạng tiểu xảo "hợp pháp" tinh vi. Sếp dùng thủ thuật kế toán để xào nấu lợi nhuận cho đẹp hồ sơ. AI vạch trần thủ đoạn này bằng cách phát hiện sự bất đồng bộ giữa giọng điệu hoảng loạn trong email nội bộ và giọng điệu hào nhoáng trên báo cáo cổ đông.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Đánh giá Chéo Đa chiều (Khung STOPSCAM)</b></summary>
<br>

Thuật toán không bao giờ kết tội vội vã. Nó đối chiếu giữa Hành vi (vừa bị giáng chức), Tâm lý (email thù hằn) và Thao tác (đăng nhập hệ thống) để quyết định có nên khóa tài khoản của nhân viên đó hay không.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Bất kiêm nhiệm (Segregation of Duties)</b></summary>
<br>

Nguyên tắc vàng trong kế toán (Người tạo hóa đơn thì không được phép Duyệt chi tiền). Tuy nhiên, kẻ gian dễ lách luật bằng cách mượn User của người khác.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Khai phá Quy trình (Process Mining)</b></summary>
<br>

Công nghệ cốt lõi thứ 2. Thuật toán này không nhìn vào con số trên sổ sách, mà nó lôi hệ thống máy chủ ra để vẽ lại chính xác 100% đường đi thực tế của quy trình phê duyệt xem có bị đi tắt, lách luật hay không.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Cái bóng Kỹ thuật số (Digital Shadow / Event Logs)</b></summary>
<br>

Nhật ký sự kiện lưu trên máy chủ (Ai đăng nhập? Bằng dải IP nào? Mấy giờ, mấy phút, mấy giây?). Kẻ gian có thể làm giả hóa đơn giấy, nhưng không thể xóa được cái bóng kỹ thuật số này trước con mắt của Process Mining.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Phân tích Dữ liệu vs Siêu Dữ liệu (Data-Centric vs Metadata-Centric)</b></summary>
<br>

Kiểm toán cũ chỉ nhìn Data (Tờ hóa đơn này giá bao nhiêu?). Kiểm toán AI nhìn vào Metadata (Ai là người duyệt tờ hóa đơn này trên máy tính 192.168.1.1 vào lúc 2 giờ sáng?).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Cảnh báo giả & Sự kiệt sức (False Positives & Alert Fatigue)</b></summary>
<br>

Mặt trái của giám sát bằng máy móc. Nếu máy móc cứ thấy đăng nhập 2h sáng là báo động (kể cả lúc đang khóa sổ kế toán hợp lệ), nhân viên sẽ bị kiệt sức vì báo động giả và bỏ mặc hệ thống.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Sự giao thoa Người và Máy (Human-in-the-loop)</b></summary>
<br>

Giải pháp cho Cảnh báo giả. Phán đoán nghề nghiệp của Kế toán viên sẽ đóng vai trò "dạy dỗ" (dán nhãn) cho máy tính biết phân biệt đâu là áp lực khóa sổ cuối năm, đâu là hành vi trộm cắp, để máy ngày càng khôn hơn.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Học không giám sát (Unsupervised Learning)</b></summary>
<br>

Tuyệt chiêu dùng để đi săn các mánh khóe lừa đảo hoàn toàn mới toanh mà giới giang hồ chưa từng dùng (Unknown Unknowns). Máy tự phân tích mà không cần con người dạy trước.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Thuật toán Phân cụm (Clustering)</b></summary>
<br>

Một kỹ thuật của Học không giám sát. Nó tự gom các hóa đơn thành ổ. Ví dụ: Kẻ gian lách ngưỡng phê duyệt 10,000 USD bằng cách xé nhỏ hóa đơn thành 9,999 USD. Phân cụm sẽ vẽ ra một cái "ổ nhền nhện" bất thường tại con số 9,999 đó để bắt thóp.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Mô hình Kim cương Gian lận (Fraud Diamond)</b></summary>
<br>

Phiên bản tiến hóa của Tam giác Gian lận. Gồm 4 yếu tố: Áp lực, Cơ hội, Sự biện minh, và Năng lực. AI được sinh ra để triệt tiêu viên kim cương này.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Góc Năng lực (Capability)</b></summary>
<br>

Mồi lửa châm ngòi. Để thực hiện vụ lừa đảo ngàn tỷ, kẻ đó phải am hiểu hệ thống, biết cách xóa dấu vết (thường là sếp lớn). Kẻ lừa đảo mà thiếu năng lực thì muốn ăn cắp cũng đành chịu chết.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Sự Biện minh (Rationalization)</b></summary>
<br>

Kẻ gian tự lừa dối bản thân bằng những lý lẽ: "Tôi chỉ mượn công ty tạm vài tỷ thôi", "Công ty nợ tôi món tiền này". NLP của AI sẽ phân tích văn bản để tìm ra sự xáo trộn tâm lý này.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Phân tích Mạng lưới Xã hội (Social Network Analysis)</b></summary>
<br>

Dùng AI để phân tích sự liên kết ngầm trong công ty (ai hay chat với ai nhất). Qua đó lật tẩy các nhóm quyền lực ngầm đang thâu tóm hệ thống, vượt mặt các cấu trúc phòng ban chính quy.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Gian lận lấy AI làm trung tâm (AI-centric fraud)</b></summary>
<br>

Tội phạm thời 4.0 dùng chính AI để làm giả số liệu, giả giọng nói CEO (Deepfake) để ra lệnh chuyển tiền. Ranh giới thật - giả bị xóa nhòa.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Rủi ro AI bị thao túng (Algorithm Manipulation)</b></summary>
<br>

Nỗi sợ tột cùng. Điều gì xảy ra nếu cỗ máy AI của công ty bị Ban giám đốc nạp mệnh lệnh ngầm: "Tối ưu báo cáo tài chính bằng mọi giá"? AI sẽ tự động sinh ra hàng vạn giao dịch ma với tốc độ ánh sáng để che giấu khoản lỗ.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Kiểm toán Thuật toán (Algorithm Auditing)</b></summary>
<br>

Kỹ năng tối thượng của Kế toán tương lai. Thay vì chỉ đi kiểm toán sổ sách của con người, kế toán viên sẽ phải "kiểm toán cỗ máy AI" để xem nó có bị cài cắm mã độc thiên vị hay tiếp tay cho gian lận hay không.

</details>



#### ** 🇬🇧 Tiếng Anh **

### 📄 Tài liệu PDF 1: Chương 9: Automating Internal Controls

<object data="textbook/Buoi_07A_Chương 9 (Automating Internal Controls).pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_07A_Chương 9 (Automating Internal Controls).pdf#view=FitH" target="_blank">Nhấn vào đây để tải tài liệu PDF 1</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_07A_Chương 9 (Automating Internal Controls).pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 1 (PDF)</a></p>

---

### 📄 Tài liệu PDF 2: Chương 12: Intelligent Automation of Fraud Detection

<object data="textbook/Buoi_07B_Chương 12 (Intelligent Automation of Fraud Detection).pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_07B_Chương 12 (Intelligent Automation of Fraud Detection).pdf#view=FitH" target="_blank">Nhấn vào đây để tải tài liệu PDF 2</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_07B_Chương 12 (Intelligent Automation of Fraud Detection).pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 2 (PDF)</a></p>


#### ** 🇻🇳 Tiếng Việt **

# 1. Đánh giá Kiểm soát Nội bộ Tự động (Automating Internal Controls Assessment)

## 1.1 Giới thiệu và Bối cảnh Thực tiễn (Introduction and Practical Context)

GẦN ĐÂY, PRICEWATERHOUSECOOPERS (PWC) đã dàn xếp hai vụ kiện sơ suất nghề nghiệp lớn thu hút nhiều sự chú ý ở Anh. Trong hai vụ án (MF Global và Taylor Bean & Whitaker), các cáo buộc chống lại PwC chỉ ra rằng các nguyên đơn kỳ vọng công ty kiểm toán sẽ vượt xa những xác nhận của ban quản lý (management assertions) và đưa cả việc ra quyết định của ban quản lý vào phạm vi kiểm toán. Một công ty khác, công ty du lịch Thomas Cook, cũng được PwC kiểm toán từ năm 2007 đến 2016. Từ năm 2017 cho đến khi Thomas Cook sụp đổ vào năm 2019, Ernst & Young (EY) đã tiếp quản với vai trò là công ty kiểm toán. Khi điều tra, người ta phát hiện ra rằng PwC đã cung cấp tư vấn thù lao cho Thomas Cook, và mặc dù cả hai công ty, PwC và EY, đều có thông tin về những vấn đề sâu sắc mà Thomas Cook đang phải đối mặt, cả hai đều đưa ra các báo cáo kiểm toán sạch (clean audit reports) cho Thomas Cook. Bình luận về những thất bại trong kiểm toán, Bob Moritz, chủ tịch toàn cầu của PwC, cho biết: “Kỳ vọng của thị trường cao hơn yêu cầu quy định. Khi những thất bại lớn xảy ra, đó không hẳn là một thất bại của kiểm toán. Các biện pháp kiểm soát có thể là phù hợp, nhưng sự tiếp nối của doanh nghiệp, vị thế tài chính và tính bền vững dài hạn của nó vẫn có thể bị nghi ngờ” (Kinder, 2019).

Liệu PwC và EY có thể đạt được những hiểu biết sâu sắc hơn về những điểm yếu trọng yếu trong kiểm soát nội bộ (material weaknesses in internal controls) của khách hàng, ngay cả trước khi một cuộc kiểm toán được bắt đầu?
Liệu PwC có thể phát triển những hiểu biết sâu sắc hơn về hoạt động kinh doanh của một công ty?
Làm thế nào để ban quản lý, hội đồng quản trị và ủy ban kiểm toán có thể nhận được sự đánh giá liên tục về các biện pháp kiểm soát kiểm toán?
Làm thế nào để nhận diện và giảm thiểu các rủi ro mới và đang nổi lên?
Kiểm toán có thể mở rộng phạm vi của mình mà không phát sinh thêm chi phí lớn hay không?

Câu trả lời cho những câu hỏi này và nhiều câu hỏi tương tự khác phụ thuộc rất nhiều vào chiến lược tự động hóa các kiểm soát nội bộ (automation strategy of internal controls). Trong chương này, chúng tôi phát triển một cách tiếp cận chiến lược toàn diện để tự động hóa việc đánh giá và kiểm toán các kiểm soát nội bộ.

## 1.2 Tự động hóa Đánh giá Kiểm soát Nội bộ (Automating Internal Controls Assessment)

Khác với rủi ro tiềm tàng (inherent risk), vốn được gắn liền với các lựa chọn chiến lược do công ty thực hiện dựa trên mô hình kinh doanh, ngành nghề,... rủi ro kiểm soát nội bộ (internal controls risk) là một hàm số của các hành động từ các nhóm quản lý và hội đồng quản trị. Năm 1993, Ủy ban của các Tổ chức Bảo trợ thuộc Ủy ban Treadway (Committee of Sponsoring Organizations of the Treadway Commission - COSO) đã trình bày một khuôn khổ, hiện đã trở thành tiêu chuẩn cho kiểm soát nội bộ. COSO định nghĩa kiểm soát nội bộ như sau (COSO, 2013):

Kiểm soát nội bộ là một quy trình, chịu tác động bởi hội đồng quản trị, ban quản lý và các nhân sự khác của một thực thể, được thiết kế để cung cấp sự đảm bảo hợp lý liên quan đến việc đạt được các mục tiêu trong ba hạng mục sau:
1. Độ tin cậy của việc lập báo cáo tài chính (Reliability of financial reporting).
2. Tính hiệu quả và hiệu suất của các hoạt động (Effectiveness and efficiency of operations).
3. Tuân thủ các luật pháp và quy định hiện hành (Compliance with applicable laws and regulations).

Tiêu chuẩn COSO dựa trên ba mục tiêu – tính hiệu quả và hiệu suất của các hoạt động, lập báo cáo tài chính đáng tin cậy, và tuân thủ các luật và quy định. Điều này có nghĩa là các biện pháp kiểm soát tồn tại để đạt được ba mục tiêu này. Mục tiêu đầu tiên về tính hiệu quả và hiệu suất của các hoạt động dựa trên các mục tiêu doanh nghiệp do hội đồng quản trị và các nhóm lãnh đạo cấp cao xác định, và cấu thành các mục tiêu chính mà công ty phải đạt được để thực hiện chiến lược của mình. Mục tiêu thứ hai về báo cáo tài chính đáng tin cậy dựa trên các xác nhận do công ty đưa ra và các số liệu cùng những thông tin công bố về hiệu quả tài chính của công ty. Mục tiêu thứ ba nhằm đảm bảo rằng công ty tuân thủ các luật và quy định áp dụng cho doanh nghiệp và ngành nghề của mình.

Đối với mỗi mục tiêu, các kiểm soát nội bộ được xây dựng với năm thành phần sau: (1) môi trường kiểm soát (control environment), (2) đánh giá rủi ro (risk assessment), (3) hoạt động kiểm soát (control activities), (4) giám sát (monitoring), và (5) thông tin và truyền thông (information and communication). Mỗi thành phần được hỗ trợ bởi các nguyên tắc và, tính đến năm 2013, có 17 nguyên tắc là một phần của khuôn khổ này.

Tại thời điểm này, cần lưu ý rằng tự động hóa kiểm toán có thể được xem như sự kết hợp giữa việc thu thập bằng chứng dựa trên công cụ (tool-driven) (nơi các kiểm toán viên không dựa vào bất kỳ thông tin nào do con người cung cấp) và dựa trên con người (human-based). Các bên được kiểm toán (auditees) cung cấp thông tin dưới dạng các yêu cầu dữ liệu, quyền truy cập vào các hệ thống và thông tin, và các phản hồi cho các yêu cầu thông tin cụ thể dưới dạng báo cáo, hỏi đáp, biểu mẫu,... Các công cụ tự động không dựa vào thông tin do con người cung cấp mà thay vào đó chúng truy cập trực tiếp vào bằng chứng từ nguồn như dữ liệu, cơ sở dữ liệu và các ứng dụng. Việc thu thập bằng chứng dựa trên con người phụ thuộc vào các cuộc khảo sát và bảng câu hỏi. Trí tuệ nhân tạo (AI) có vai trò trong cả hai lĩnh vực và mặc dù chương này chủ yếu tập trung vào các công cụ, việc tự động hóa các khảo sát và bảng câu hỏi tập trung vào con người liên quan đến khả năng tạo ra và phân tích các khảo sát và bảng câu hỏi. Chúng ta sẽ đề cập đến các khảo sát và bảng câu hỏi của con người trong một chương tiếp theo.

Các nghiên cứu trước đây sử dụng các phương pháp AI của kỹ thuật phân cụm dựa trên bản đồ tự tổ chức (self-organizing maps - SOMs) đã gợi ý rằng các kiểm soát nội bộ hình thành nên một mạng lưới các năng lực phức tạp, nơi một công ty có thể có một hoặc nhiều thành phần mạnh (ví dụ: các hoạt động kiểm soát và giám sát) nhưng không phải trong tất cả các lĩnh vực. Hơn nữa, các công ty có thể có các thành phần mạnh cho một mục tiêu nhưng không phải là cho cả ba (Länsiluoto et al., 2016). Nhắc lại rằng có ba mục tiêu: tính hiệu quả và hiệu suất của các hoạt động, báo cáo tài chính đáng tin cậy, và tuân thủ các luật và quy định. Để thiết kế một hệ thống tự động, chiến lược của chúng ta cần bao gồm tất cả ba mục tiêu COSO và năm thành phần liên quan.

Khi thiết kế một hệ thống kiểm soát nội bộ tự động, chiến lược tổng thể của chúng ta như sau:
- Tiếp cận vấn đề như là sự tương tác tích hợp của nhiều tác nhân khác nhau (cả tất định - deterministic và ngẫu nhiên - stochastic).
- Sử dụng nhiều công nghệ khác nhau, bao gồm khai thác quy trình (process mining), học máy (machine learning), RPA (Tự động hóa quy trình bằng robot) và hệ chuyên gia (expert systems).
- Kiểm tra những điểm yếu của kiểm soát nội bộ đã bám rễ vào trong thiết kế của công ty khách hàng, từ đó tạo ra một môi trường chín muồi cho các sai sót và gian lận, và để dự đoán liệu một hoạt động gian lận có đang diễn ra hay không.
- Sử dụng hệ thống kiểm soát nội bộ tích hợp để thực hiện đánh giá liên tục.
- Áp dụng hệ thống kiểm soát nội bộ tích hợp để tạo ra một đánh giá toàn diện (tức là phân tích toàn bộ tổng thể thay vì một mẫu).
- Phát triển và mở rộng hệ thống cùng với doanh nghiệp.

Đánh giá rủi ro tự động (Automated risk assessment) bao gồm ba lĩnh vực: đánh giá rủi ro kiểm toán, đánh giá rủi ro tiềm tàng (inherent risk), và đánh giá kiểm soát nội bộ. Rủi ro kiểm toán là một hàm số của rủi ro tiềm tàng, rủi ro kiểm soát, và rủi ro phát hiện (detection risk). Trong chương trước, chúng ta đã đề cập đến rủi ro tiềm tàng. Rủi ro tiềm tàng là rủi ro tồn tại khi không có bất kỳ kiểm soát nội bộ nào. Rủi ro kiểm soát nội bộ xảy ra khi một công ty không có các kiểm soát nội bộ phù hợp để quản lý và kiểm soát các rủi ro tiềm tàng. Việc thiếu vắng các biện pháp kiểm soát có thể là do các thông lệ (practices) hoặc thiết kế của công ty. Điều đó có thể xảy ra một cách có chủ ý hoặc vô ý. Kiểm soát nội bộ có thể bị lẩn tránh, vô hiệu hóa (overridden) hoặc bỏ qua khi ban quản lý tham gia vào gian lận. Do đó, trong khi rủi ro tiềm tàng đã được gắn liền trong bản chất của kinh doanh, rủi ro kiểm soát nội bộ lại rất nhiều khả năng là sản phẩm của cách thức mà một công ty được quản lý. Khi các kiểm toán viên quan sát thấy các lỗ hổng trong kiểm soát nội bộ, họ được cho là phải tăng cường các thủ tục cơ bản (substantive procedures) để làm giảm hoặc giảm thiểu cơ hội xảy ra sai sót.

Như được minh họa trong Hình 9.1, để tự động hóa việc đánh giá kiểm soát nội bộ, chúng ta tuân theo mô hình COSO và chia nó thành năm lĩnh vực năng lực: đánh giá môi trường tự động (automated environment evaluation), đánh giá rủi ro tự động (automated risk assessment), đánh giá hoạt động kiểm soát tự động (automated control activities assessment), đánh giá giám sát tự động (automated monitoring assessment) và đánh giá thông tin và truyền thông tự động (automated information and communications evaluation). Mỗi một lĩnh vực này được tự động hóa bằng các tác nhân khác nhau, làm việc một cách phối hợp và hợp tác để đạt được sự tự động hóa hoàn toàn.

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_07A/FIGURE 9.1 Automation of Internal Controls Evaluation.jpeg" alt="FIGURE 9.1 Automation of Internal Controls Evaluation" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Hình 9.1: Tự động hóa Đánh giá Kiểm soát Nội bộ (FIGURE 9.1 Automation of Internal Controls Evaluation)</div>
</div>

## 1.3 Môi trường Kiểm soát Tự động (Automated Control Environment)

Các nguyên tắc của môi trường kiểm soát (Hình 9.2) là:

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_07A/FIGURE 9.2 Automated Environment Evaluation.jpeg" alt="FIGURE 9.2 Automated Environment Evaluation" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Hình 9.2: Đánh giá Môi trường Kiểm soát Tự động (FIGURE 9.2 Automated Environment Evaluation)</div>
</div>

- Tổ chức thể hiện cam kết đối với sự chính trực và các giá trị đạo đức.

- Hội đồng quản trị thể hiện sự độc lập với ban quản lý và thực hiện vai trò giám sát đối với sự phát triển và hoạt động của kiểm soát nội bộ.
- Ban quản lý thiết lập, với sự giám sát của hội đồng quản trị, các cấu trúc, các tuyến báo cáo (reporting lines) cùng với các quyền hạn và trách nhiệm phù hợp trong việc theo đuổi các mục tiêu.
- Tổ chức thể hiện cam kết trong việc thu hút, phát triển và giữ chân những cá nhân có năng lực phù hợp với các mục tiêu.
- Tổ chức quy trách nhiệm (holds accountable) cho các cá nhân về những trách nhiệm kiểm soát nội bộ của họ trong việc theo đuổi các mục tiêu.

Đánh giá môi trường của kiểm soát là một cuộc điều tra về các mô hình giá trị và hành động của con người. Ví dụ, từ "tổ chức" trong nguyên tắc đầu tiên ngụ ý rằng có một hoặc nhiều con người thể hiện cam kết đối với sự chính trực và các giá trị đạo đức. Cam kết là một cấu trúc nhận thức (cognitive construct) và biểu hiện thông qua các giao tiếp và hành động của con người. Vào thời điểm này, chúng ta chưa có công nghệ đáng tin cậy để quan sát những gì diễn ra trong tâm trí của mọi người, nhưng chúng ta có thể quan sát các mô hình về con người và hành vi con người, vốn có thể cung cấp cho chúng ta thông tin về các cấu trúc tinh thần hoặc nhận thức của họ. Chẳng hạn, lời nói, cách chọn từ, cử chỉ và ngôn ngữ cơ thể (bao gồm cả thông tin sinh lý) có thể cung cấp cho chúng ta những manh mối về các cấu trúc nhận thức. Những điều này có thể là chung chung – hoặc cụ thể đối với một miền/lĩnh vực (domain). Ví dụ, một đánh giá chung có thể tiết lộ tính cách của một người và có thể được phân loại là hung hăng (aggressive) so với thụ động (passive). Một đánh giá cụ thể sẽ tìm kiếm trong lời nói (bằng miệng, bằng văn bản) về các giá trị.

Do đó, thiết kế một hệ thống để đánh giá môi trường kiểm soát sẽ bao gồm:
- Một tác nhân đo lường các cấu trúc nhận thức của các đội ngũ quản lý (giá trị, đạo đức, tính cách, sự chính trực, và những khía cạnh khác).
- Một tác nhân đo lường các cấu trúc nhận thức của các đội ngũ quản lý và hội đồng quản trị dành riêng cho cấu trúc nhiệm vụ (ví dụ: các giá trị hoặc các loại tính cách để hoạt động trong một thách thức cụ thể đối với một công ty hoặc cho một mục tiêu cụ thể của việc lập báo cáo tài chính).
- Một tác nhân xác định xem hội đồng quản trị có đảm nhận trách nhiệm giám sát, các cấu trúc, trách nhiệm và quyền hạn hay không.
- Một tác nhân xác định sự tách biệt của Hội đồng quản trị với đội ngũ quản lý, và thực hiện quyền giám sát đối với sự phát triển và hoạt động của kiểm soát nội bộ.
- Một tác nhân đo lường và cung cấp phản hồi về cam kết của công ty trong việc thu hút, phát triển và giữ chân các cá nhân có năng lực.
- Một tác nhân đánh giá trách nhiệm giải trình (accountability).

Các tác nhân trên, một khi được đào tạo, sẽ hình thành nên hệ thống môi trường kiểm soát tích hợp.

Sự Chính trực, Đạo đức, Tính cách, và Các Giá trị (Integrity, Ethics, Personality, and Values)
Hệ thống này đã được giải thích trong chương tiền lập kế hoạch kiểm toán. Chúng ta sẽ xem xét lại nó ở đây từ góc độ của một hệ thống nội bộ (trái ngược với bên ngoài). Kiểm toán viên có quyền truy cập vào nhiều tài liệu nội bộ hơn đáng kể so với việc phân tích một công ty từ bên ngoài. Trong thế giới ngày nay, hình ảnh, giọng nói, và dữ liệu video cũng có thể được yêu cầu và thu thập. Phiên bản cốt lõi của hệ thống này là xử lý ngôn ngữ tự nhiên, phân tích các giao tiếp bằng văn bản của đội ngũ quản lý và các thành viên hội đồng quản trị để tìm kiếm những từ ngữ biểu thị sự chính trực, đạo đức, giá trị và tính cách. Như đã đề cập trước đó, phương pháp này đã được triển khai để nghiên cứu rủi ro gian lận từ các mô hình ngôn ngữ học và thanh nhạc của các cuộc gọi thu nhập (Throckmorton et al., 2015) cũng như từ các tài liệu (Phần Thảo luận và Phân tích của Ban quản lý (MD&A) của Mẫu 10-K) (Humpherys et al., 2011). Tác nhân này dự kiến sẽ đánh giá lượng thông tin giao tiếp của ban quản lý và hội đồng quản trị được áp dụng cho các giá trị và đạo đức là bao nhiêu. Các tài liệu đầu vào được sử dụng cho các phân tích này có thể bao gồm các báo cáo, tin nhắn, biên bản họp hội đồng quản trị, email và các giao tiếp khác. Bằng cách sử dụng những điều đó làm đầu vào, một công cụ phân loại (classification engine) được triển khai, dựa trên từ ngữ, để đánh giá sự hiện diện, độ sâu và tần suất của các cuộc thảo luận liên quan đến đạo đức và sự chính trực trong quy trình hoạt động kinh doanh thông thường.

Một cách khác phức tạp hơn, là lấy dữ liệu từ các giao tiếp của những nhà lãnh đạo thuộc một công ty đã tham gia vào gian lận và nghiên cứu các mô hình diễn đạt của họ so với các mô hình của những công ty đã cung cấp lợi nhuận thích đáng và đáp ứng được các nghĩa vụ ủy thác (fiduciary obligations).

Hội đồng Quản trị (Board of Directors)
Các tài liệu và email của hội đồng quản trị, bao gồm các biên bản từ các cuộc họp của ủy ban kiểm toán, được phân tích để xác định sự hiện diện của các cuộc thảo luận, hướng dẫn, chỉ thị và sự tham chiếu tới đạo đức, giá trị và tính chính trực. Điều tương tự có thể được thực hiện để đánh giá các tham chiếu tới các kiểm soát nội bộ. Điều này bộc lộ những trường hợp mà các tham chiếu về kiểm soát nội bộ đã được đưa ra. Phân tích email cũng bộc lộ luồng giao tiếp, quyền hạn và bản chất của mối quan hệ trong tổ chức.
Các đặc điểm (features) được sử dụng cho email có thể bao gồm siêu dữ liệu (metadata) của email, số lượng email, tiêu đề, văn bản, có hay không có tệp đính kèm, email đã được ký, được chuyển tiếp, được trả lời, cc, blind copy (bcc) và các đặc điểm khác liên quan đến tần suất của các email.

Triết lý Quản lý và Phong cách Điều hành (Management Philosophy and Operating Style)
Chúng ta đã đề cập ngắn gọn về lĩnh vực này trong một chương trước nơi mô hình của chúng ta dựa trên dữ liệu bên ngoài. Ở đây, chúng ta sử dụng dữ liệu nội bộ để đánh giá triết lý quản lý và phong cách điều hành. Một lần nữa, xử lý ngôn ngữ tự nhiên có thể mang lại cho chúng ta một sự khởi đầu tuyệt vời để hiểu về triết lý quản lý và phong cách điều hành.
Triết lý và phong cách quản lý có thể được quan sát bởi ngôn ngữ do đội ngũ quản lý sử dụng, các mạng lưới xã hội bên trong tổ chức và văn hóa công ty. Các tệp tin Nhân sự (HR files), tài liệu tòa án và các trang web như Glassdoor cung cấp dữ liệu tuyệt vời cho việc lập mô hình. Sử dụng học máy (machine learning), mục tiêu của bạn là huấn luyện thuật toán của mình để phân loại văn hóa của một công ty thành các lớp khác nhau. Điều này có thể được xem như một bài toán về việc phân loại đội ngũ quản lý vào các nhóm (buckets) khác nhau gồm các phong cách điều hành, triết lý quản lý và mô hình quản lý. Ví dụ: bạn có thể xác định xem phong cách quản lý là độc đoán (authoritarian) hay hợp tác (collaborative), khép kín so với cởi mở, tập trung vào sự ủy quyền (delegation centric) so với dựa trên sự trao quyền (empowerment based). Hành vi của nhân viên trong các tổ chức có thể được dự đoán bằng cách triển khai học máy và khai thác dữ liệu từ các thông tin văn bản như email (Straub et al., 2016).

Cấu trúc Tổ chức (Organizational Structure)
Sự đánh giá về cấu trúc tổ chức đến từ nhiều góc độ. Khả năng phân tích được xây dựng một cách có hệ thống bằng cách phân lớp những phần sau đây...

Các năng lực (capabilities):
- Trình phân tích cấu trúc tổ chức (The analyzer for organizational structure): tiện ích này xem xét các mô tả công việc của tổ chức và phân loại nhân viên vào các vai trò cụ thể liên quan đến kiểm soát nội bộ. Dữ liệu được khai thác là các mô tả công việc, tên phòng ban, nhân sự, chức danh, v.v. Một phân tích riêng biệt về tổ chức cũng có thể chỉ ra các luồng quyền lực, sức ảnh hưởng và các liên kết xã hội phi chính thức (Fire và Puzis, 2016).
- Trình phân tích cũng xem xét biểu đồ tổ chức so với cấu trúc quyền hạn thực tế. Cấu trúc quyền hạn theo biểu đồ được thể hiện trên các sơ đồ tổ chức và phụ thuộc vào các mối quan hệ báo cáo. Cấu trúc quyền hạn thực tế được xác định dựa trên việc phân tích các mạng lưới xã hội từ email, tin nhắn văn bản và các thông tin khác. Hệ thống phân cấp xã hội (social hierarchy) có thể được xác định từ học máy bằng cách phân tích các email (Rowe et al., 2007).

Năng lực Lập báo cáo Tài chính (Financial Reporting Competencies)
Các năng lực lập báo cáo tài chính có thể có được thông qua việc thấu hiểu nền tảng học vấn, kinh nghiệm và loại hình giáo dục.
Tập dữ liệu huấn luyện (training data set) cho năng lực bao gồm dữ liệu HR (nhân sự) điển hình, cũng như dữ liệu từ sơ yếu lý lịch, LinkedIn và dữ liệu mạng xã hội khác. Nó cũng bao gồm dữ liệu từ số lượng ấn phẩm của người đó, sự tham gia vào các hội nhóm chuyên môn khác nhau, các khóa đào tạo và chứng chỉ.
Artifact (tạo tác/công cụ) này có thể được thiết kế theo hai cách. Cách tiếp cận đầu tiên là sử dụng dữ liệu HR từ một tập dữ liệu lớn hơn (có thể bao gồm dữ liệu từ nhiều công ty) và để một con người gán nhãn (labels) cho dữ liệu. Nhãn trong trường hợp này sẽ được áp dụng để tìm hiểu các mức độ năng lực cho một vị trí. Các yếu tố như số năm làm việc, nền tảng học vấn, kinh nghiệm, v.v., sẽ là tập dữ liệu đầu vào. Thông tin có giá trị có thể được trích xuất từ sơ yếu lý lịch (Reza và Zaman, 2017). Biến 'y' hoặc biến đầu ra sẽ là có năng lực (competent) so với không có năng lực (incompetent) cho một công việc nhất định.
Artifact thứ hai và thú vị hơn sử dụng tập dữ liệu của các biến đầu vào bao gồm kinh nghiệm, số năm làm việc, nền tảng giáo dục từ một tập dữ liệu thực tế về các vụ gian lận và thất bại ở vị trí đó. Tuy nhiên, dù rất thú vị, sẽ rất khó để tái tạo lại một tập dữ liệu cho các mục đích huấn luyện vì sẽ rất khó để chỉ ra chính xác trách nhiệm cho một thất bại.

Quyền hạn và Trách nhiệm (Authority and Responsibility)
Quyền hạn và trách nhiệm được đánh giá bằng cách sử dụng các công nghệ tự động hóa thông minh khác nhau. Chúng ta đang cố gắng đánh giá xem ban quản lý có giao phó trách nhiệm về kiểm soát nội bộ một cách thích hợp hay không và các nhân viên có được trao cho các biện pháp kiểm soát và quyền hạn phù hợp để đảm bảo rằng các kiểm soát nội bộ được thực thi và hoạt động hiệu quả hay không. Có nhiều cách để đánh giá điều đó từ khía cạnh học máy.
Cách đầu tiên là có một tác nhân sử dụng dữ liệu nguồn nhân lực để hiểu về các trách nhiệm công việc. Việc thu thập dữ liệu cũng có thể mở rộng đến các biểu mẫu đánh giá và xem xét nhân viên hàng năm, thường chứa đựng các tài khoản chi tiết hơn về công việc thực tế mà nhân viên đảm nhận. Ngoài ra, email và các giao tiếp cũng có thể được sử dụng làm dữ liệu đầu vào. Mô hình sử dụng xử lý ngôn ngữ tự nhiên (natural language processing) để đánh giá xem, dựa trên vai trò của cá nhân, cấu trúc trách nhiệm của anh ấy hoặc cô ấy có bao gồm các tham chiếu đến các kiểm soát nội bộ đặc thù của vị trí hay không. Lưu ý rằng trong bài đánh giá này, chúng ta chỉ đang đánh giá môi trường chứ không phải các hoạt động. Do đó, trọng tâm của chúng ta vẫn là nghiên cứu môi trường của tổ chức.
Trong khi trách nhiệm được đánh giá bằng cách sử dụng phương pháp trên, phân tích quyền hạn lại là một vấn đề hoàn toàn khác. Quyền hạn biểu hiện trong việc cho phép một người quản lý hoặc nhân viên hành xử đúng mực, không áp đặt những ràng buộc không phù hợp hoặc không cần thiết, đảm bảo với nhân viên rằng sẽ không có hậu quả tiêu cực nào khi nhân viên nộp khiếu nại hoặc trở thành người thổi còi (whistleblower - người tố giác).
Quyền hạn là hàm số của việc có thể hành động theo những gì mà một người đã được giao phó trách nhiệm. Trong các hệ thống doanh nghiệp, quyền truy cập được cung cấp cho các cá nhân bởi một quy trình làm việc (workflow) có ghi lại người đã ủy quyền truy cập. Các nhật ký (logs) từ hệ thống đó có thể cho thấy liệu việc ủy quyền có đang được thực hiện ở cấp độ phù hợp hay không và có được thực hiện bởi người có thẩm quyền thực hiện việc đó, hay bởi một người ở cấp cao hơn trong tổ chức, hay bởi nhiều hơn một người.
Văn hóa có thể cung cấp một đại diện gián tiếp cho việc đánh giá quyền hạn. Những nhà lãnh đạo độc đoán (authoritative) hơn sẽ ít có xu hướng cho phép mọi người hoạt động độc lập, ngay cả khi nói đến một vai trò quan trọng như kiểm soát nội bộ. Cuối cùng, các email nội bộ, ghi chú cuộc họp và giao tiếp cung cấp dữ liệu tuyệt vời để đánh giá mức độ quyền hạn mà các nhân viên chủ chốt đang có. Trong các thiết lập nâng cao, cả video và lời nói đều có thể được sử dụng để nghiên cứu các động lực văn hóa của một công ty. Để đạt được mức độ tự động hóa đó, khai thác quy trình (process mining) và học máy được sử dụng, và các ứng dụng của chúng sẽ được giải thích ở phần sau trong chương này.

Chính sách và Thực tiễn Nguồn nhân lực (Human Resource Policies and Practices)
Các tập dữ liệu lớn luôn có sẵn và có thể được khai thác trong lĩnh vực nguồn nhân lực (Jia et al., 2018). Mục tiêu của đánh giá môi trường kiểm soát liên quan đến HR là xác định xem phòng ban này có nhận thức được các khái niệm cơ bản về phân chia nhiệm vụ (separation of duties), các kiểm soát nội bộ và việc tuyển dụng đúng nhân tài để giảm thiểu rủi ro hay không. Các chính sách và thực tiễn của HR có thể được phân tích bằng cách sử dụng xử lý ngôn ngữ tự nhiên và việc sử dụng các thuật ngữ chính (phân chia nhiệm vụ, v.v.) có thể được đánh giá để phát triển sự hiểu biết sâu sắc về các năng lực của HR.
Các khái niệm tương tự, như đã thảo luận ở trên, được áp dụng để xác định khả năng và đóng góp của bộ phận HR trong việc hỗ trợ các kiểm soát nội bộ mạnh mẽ hơn.

## 1.4 Đánh giá Rủi ro Tự động (Automated Risk Assessment)
Đánh giá rủi ro tự động đã được đề cập toàn diện trong chương trước từ góc độ rủi ro tiềm tàng (inherent risk). Chúng ta nhận thấy rằng có ít nhất bốn phương pháp tự động để khám phá rủi ro trong một tổ chức. Phương pháp đầu tiên tập trung vào việc xác định và quản lý rủi ro cụ thể theo tài khoản (account) và theo xác nhận (assertion). Ba phương pháp còn lại, kế toán ngầm/song song (shadow/parallel accounting), các mục tiêu chiến lược và học sâu (deep learning), có thể được sử dụng cho bất kỳ loại hình phát triển năng lực quản lý rủi ro nào. Trên thực tế, trong trường hợp của chúng ta, khuôn khổ COSO yêu cầu ban quản lý phải hiểu về các rủi ro từ góc độ đạt được các mục tiêu của công ty. Khuôn khổ COSO 2013 phác thảo bốn nguyên tắc đánh giá rủi ro:
1. Tổ chức chỉ định các mục tiêu với sự rõ ràng đầy đủ để cho phép việc xác định và đánh giá các rủi ro liên quan đến các mục tiêu đó.
2. Tổ chức nhận diện rủi ro đối với việc đạt được các mục tiêu của mình trên toàn thực thể và phân tích các rủi ro làm cơ sở để xác định cách thức quản lý những rủi ro đó.
3. Tổ chức cân nhắc tới khả năng xảy ra gian lận trong việc đánh giá rủi ro đối với quá trình đạt được các mục tiêu.
4. Tổ chức nhận diện và đánh giá những thay đổi có thể tác động đáng kể đến hệ thống kiểm soát nội bộ.

Trong chương này, chúng tôi sẽ mở rộng mô hình được trình bày trong phần đánh giá rủi ro tiềm tàng và bao gồm cả việc đánh giá rủi ro từ góc nhìn của kiểm soát nội bộ, đồng thời giới thiệu khái niệm đánh giá rủi ro dựa trên sự kiện (event-based risk assessment).
Quá trình này bao gồm bốn cấp độ tự động hóa:
Cấp độ 1: Từ ngoài vào trong (Outside-in) – Nắm được ý tưởng chung về những điểm yếu trọng yếu tiềm ẩn trong kiểm soát nội bộ (MWIC) bằng cách sử dụng thông tin công khai có sẵn. Điều này mang lại cho các kiểm toán viên cảm nhận về mức độ rủi ro mà tình huống của khách hàng có thể xảy ra.
Cấp độ 2: Tập trung vào quy trình (Process centric) – Hiểu về mối quan hệ rủi ro giữa các quy trình và các biện pháp kiểm soát.
Cấp độ 3: Doanh nghiệp (Enterprise) – Phát triển những hiểu biết sâu sắc hơn vào chuỗi giá trị và quy trình kinh doanh của tổ chức. Điều này tương tự như các khuôn khổ phân tích rủi ro dựa trên doanh nghiệp (enterprise-based risk analysis frameworks).
Cấp độ 4: Quyết định kinh doanh (Business decisions) – Kiểm toán viên không coi đây là một phần công việc của họ; tuy nhiên, như tình huống nghiên cứu mở đầu về việc PwC dàn xếp hai vụ kiện cho thấy, đang có một phong trào ngày càng tăng nhằm đặt trách nhiệm đó lên vai các kiểm toán viên. Lý do đằng sau điều đó rất rõ ràng. Những hệ quả kinh tế từ các quyết định và mục tiêu của ban quản lý chảy qua các hệ thống tài chính, và các bên liên quan (stakeholders) kỳ vọng kiểm toán viên hiểu và đánh giá được những thực tế kinh doanh đó. Các hậu quả từ những quyết định kinh doanh của ban quản lý cũng có thể trở thành các yếu tố động lực để tiến hành gian lận. Trong những trường hợp khác, các quyết định của ban quản lý tác động đến các dòng tiền trong tương lai và chi phí vốn của công ty, do đó tác động đến việc định giá nhiều tài sản ngắn hạn (current assets).

Cấp độ 1: Phân tích Từ ngoài vào trong (Outside-In Analysis)
Một nhóm nghiên cứu muốn khám phá xem liệu có thể nhận diện các điểm yếu trọng yếu trong kiểm soát nội bộ từ việc sử dụng các dữ liệu bên ngoài công khai hay không (Simsek et al., 2018). Nhìn vào các công ty khác nhau đã thông báo về sự yếu kém trọng yếu trong các kiểm soát nội bộ, nhóm đã xác định được dữ liệu tài chính từ báo cáo tài chính lịch sử một năm trước khi công bố. Sử dụng dữ liệu đó – dữ liệu bao gồm các tỷ số tài chính như vòng quay tổng tài sản, khả năng sinh lời, cường độ vốn, quy mô, tỷ số thanh toán hiện hành (current ratio) và hiệu quả hoạt động – nhóm nghiên cứu đã cố gắng dự đoán những điểm yếu của kiểm soát nội bộ. Sau khi áp dụng nhiều phương pháp khác nhau, nhóm đã đạt được độ chính xác 70 đến 80% trong các kết quả. Điều này có nghĩa là nhóm đã có thể dự đoán, với độ chính xác hợp lý, rằng các điểm yếu trọng yếu tồn tại trong các kiểm soát nội bộ chỉ bằng cách sử dụng dữ liệu tài chính lịch sử. Một artifact tương tự có thể được triển khai để nhận diện những điểm yếu như vậy trong các công ty.
Thực tế là, dựa trên các tiến bộ công nghệ ngày nay, sức mạnh dự đoán của một artifact như vậy có thể được tăng cường đáng kể bằng cách bổ sung thêm các đặc điểm và sử dụng môi trường học sâu (deep learning environment).

Cấp độ 2: Tập trung vào Quy trình (Process Centric)
Khi tiến xa hơn phân tích Cấp độ 1, chúng ta có thể đi sâu hơn một cấp để xác định xem liệu các quy trình cốt lõi trong một công ty có mang rủi ro lớn hơn hay không. Đánh giá này là một hàm số của dữ liệu đặc trưng thu được từ hồ sơ lịch sử của những vấn đề trong kiểm soát nội bộ. Ví dụ, một tập dữ liệu chứa các ví dụ về những sai sót trước đây hoặc sự tiết lộ điểm yếu của kiểm soát nội bộ có thể được sử dụng để xác định sự hiện diện của MWIC phân theo ngành nghề, công ty, và loại hình quy trình. Có ít nhất hai loại phương pháp học máy có thể được triển khai để phát triển các hiểu biết về MWIC tập trung vào quy trình.
Cách tiếp cận đầu tiên tương tự như của Simsek et al., được thảo luận ở phần trước, ngoại trừ việc thay vì sử dụng dữ liệu hiệu quả hoạt động và tài chính làm đặc trưng đầu vào, chúng ta sử dụng ngành nghề, loại hình công ty, mô tả mô hình kinh doanh và các quy trình để hiểu được khả năng xảy ra của MWIC.
Cách tiếp cận thứ hai vay mượn từ các phương pháp được phát triển trong việc nghiên cứu lỗi con người ở các vụ tai nạn. Nghiên cứu về lỗi con người trong các tai nạn đã có tài liệu tham khảo đáng kể. Năm 1998, Hollnagel là tác giả của một cuốn sách có tựa đề Phương pháp Phân tích Lỗi và Độ tin cậy Nhận thức (Cognitive Reliability and Error Analysis Method - Hollnagel, 1998). Trong cuốn sách đó, ông đã phát triển ba hệ thống phân loại. Thứ nhất là sự phân loại về công nghệ, trong đó ông chỉ ra những vấn đề có thể gây ảnh hưởng đến máy móc (ví dụ: lỗi thiết bị, lỗi quy trình, lỗi giao diện). Phân loại thứ hai là của "con người", ám chỉ các vấn đề nhận thức có thể gây khó khăn cho con người (ví dụ: lập kế hoạch, thực thi, trí nhớ, diễn giải, quan sát). Hệ thống phân loại thứ ba là của tổ chức, bao gồm các điểm yếu trong một tổ chức (ví dụ: đào tạo, điều kiện làm việc). Hollnagel đã trình bày một Phương pháp Phân tích Lỗi và Độ tin cậy Nhận thức (CREAM), qua đó chuyển sự tập trung từ các đặc điểm của nhiệm vụ và một xác suất có giả thuyết về lỗi nhân tạo sang nguyên tắc rằng bối cảnh chính là động lực thúc đẩy Độ tin cậy Con người (Human Reliability) (R. Moura et al., 2015). Moura, Beer, Patelli, Lewis và Knoll đã xác định được tầm quan trọng của nguyên tắc này và phát triển mở rộng trên đó để sử dụng một tập dữ liệu tai nạn lớn, áp dụng kỹ thuật phân cụm (không giám sát - unsupervised) để phân loại dữ liệu nhằm khám phá ra các nguyên nhân khác nhau gây ra tai nạn. Họ đã sử dụng bản đồ tự tổ chức (self-organizing maps - SOMs) để phân cụm và phân loại dữ liệu (Moura et al., 2015; Moura et al., 2017). Kỹ thuật SOM cũng cho phép xem dữ liệu đa chiều dưới dạng biểu diễn hai chiều (Kohonen, 2013).
Tương tự như những gì Moura, Beer, Patelli, Lewis, và Knoll (2015) đã làm, SOM/Phân cụm (Clustering) có thể được áp dụng để thấu hiểu các động lực dẫn đến MWIC.

Cấp độ 3: Mối quan hệ Rủi ro Doanh nghiệp và Chuỗi Giá trị (Value Chain and Enterprise Risk Relationships)
Chúng ta đã đề cập đến quy trình quản lý rủi ro ở Chương 7. Bằng cách hiểu về các mối quan hệ chuỗi giá trị và rủi ro lấy doanh nghiệp làm trung tâm (enterprise-centric risk), chúng ta phát triển được những cái nhìn sâu sắc về những vấn đề tiềm ẩn có thể phát sinh trong những tình huống có sự tham gia của các bên bên ngoài (ví dụ: bán hàng và thu mua). Việc phát triển những hiểu biết đó giúp mang lại cho các kiểm toán viên một ý tưởng về nguy cơ giảm sút giá trị của các tài sản (ví dụ: việc biết được thông tin một khách hàng lớn đang bị phá sản sẽ tác động lên khoản Phải thu khách hàng - AR đang được nắm giữ bởi công ty khách hàng).
Quy trình quản lý rủi ro doanh nghiệp (enterprise risk management process) bao gồm các quy trình sau: nhận diện rủi ro, phát triển tiêu chí đánh giá, đánh giá rủi ro, đánh giá sự tương tác của các rủi ro, ưu tiên các rủi ro và ứng phó với rủi ro (Curtis và Carey, 2012). Việc sử dụng AI trong quy trình quản lý rủi ro sẽ tự động hóa luồng quy trình làm việc của việc quản lý rủi ro.

Cấp độ 4: Phân tích các Quyết định Kinh doanh (Business Decisions Analysis)
Lĩnh vực phân tích rủi ro này đóng vai trò sống còn trong việc cải thiện chất lượng kiểm toán và giúp phát triển một góc nhìn sâu sắc hơn, tinh tế hơn cho các kiểm toán viên. Sự tự động hóa trong trường hợp này tuân theo phương pháp tiếp cận tiêu chuẩn trong việc hiểu rõ rủi ro doanh nghiệp. Đã có các phương pháp và cách tiếp cận được thiết lập sẵn cho việc nhận diện, đo lường và quản lý các rủi ro doanh nghiệp.

Thiết kế Công nghệ (Technology Design)
Trước khi trình bày các phương pháp luận để đạt được mục tiêu đó, điều quan trọng là phải hiểu được hai loại dữ liệu then chốt cho việc thực hiện phân tích hoạt động kiểm soát. Đầu tiên là dữ liệu giao dịch (transactional data). Đây là dạng dữ liệu thông thường chúng ta dùng để tiến hành phân tích và bao gồm dữ liệu từ các cơ sở dữ liệu như bán hàng, kế toán và thu mua. Loại dữ liệu thứ hai, được gọi là siêu dữ liệu (metadata), là dữ liệu nói về dữ liệu – ví dụ như dữ liệu nhật ký máy tính (computer's log) về các giao dịch. Siêu dữ liệu ghi lại những thứ như ai là người truy cập hệ thống, khi nào một bút toán được nhập, hay những thay đổi nào đã diễn ra.
Việc soát xét các hoạt động kiểm soát dựa trên ba loại hình phân tích: tập trung vào dữ liệu (data-centric), tập trung vào siêu dữ liệu (metadata-centric) và tập trung vào cả dữ liệu cộng siêu dữ liệu. Để đánh giá cao sức mạnh của tự động hóa, điều quan trọng là phải nhận ra rằng việc đánh giá tự động các hoạt động kiểm soát gắn chặt trực tiếp vào việc đánh giá rủi ro đã được thực hiện ở phần trước, cũng như các thủ tục kiểm toán thực tế. Mặc dù chúng ta đã trình bày mô hình tự động hóa kiểm toán tổng thể như một mô hình tuyến tính, nhưng máy móc, không giống như con người, không cần đến các điểm nút chuyển đổi quy trình (process transition nodes) và thay vào đó nó có thể thực hiện đồng thời tất cả các quy trình.

Phân tích tập trung vào Siêu dữ liệu (Metadata-Centric Analysis)
Phân tích cụ thể theo quy trình đang là một lĩnh vực ngày càng phát triển của tự động hóa kiểm toán. Sự ra đời của công nghệ khai thác quy trình (process-mining technology) là một bước chuyển mình mang tính biến đổi đối với việc thực hiện đánh giá rủi ro bằng cách sử dụng dữ liệu nhật ký sự kiện (event log data). Các phương pháp phân tích được áp dụng để trích xuất những cái nhìn sâu sắc từ dữ liệu nhật ký nhằm hiểu được các mô hình liên quan đến kiểm toán. Dữ liệu trích xuất từ nhật ký sự kiện bao gồm thông tin về hệ thống nào đã được truy cập, khi nào và bởi ai. Điều này được biết đến dưới dạng thông tin về hoạt động, định tuyến (routing) và nguồn lực (resource). Khai thác quy trình là hình thức khai thác dữ liệu dựa trên các quy tắc.
Thông tin này được dùng để nắm bắt bằng chứng kiểm toán nhằm quyết định các yếu tố như:

- Liệu hệ thống có được truy cập bởi những người được ủy quyền làm việc đó hay không?
- Liệu hệ thống có được truy cập vào những thời điểm bất thường hoặc gần sát kỳ khóa sổ hay không?
- Liệu hệ thống có được truy cập với tần suất cao hơn vào một số khoảng thời gian nhất định hay không?
- Có hai hay nhiều hệ thống đang được truy cập bởi một người mà trách nhiệm của người đó không cho phép anh ta/cô ta làm vậy do yêu cầu phân chia nhiệm vụ (separation of duties) hay không?
- Các hệ thống có được truy cập bởi một nhóm người có số giờ truy cập hệ thống trùng khớp nhau, tuy nhiên, họ thường không truy cập các hệ thống cùng một lúc hay không?

Trong công trình nghiên cứu ấn tượng của mình, Jans et al. (2013) đã đưa ra lập luận mạnh mẽ cho việc sử dụng khai thác quy trình (process mining) trong kiểm toán và biện luận cho tiềm năng tạo ra giá trị của việc sử dụng khai thác quy trình. Họ đã trình bày bốn đặc điểm (attributes) chính sau đây của khai thác quy trình:
1. Khai thác quy trình phân tích toàn bộ tổng thể dữ liệu chứ không chỉ một mẫu (sample).
2. Yếu tố cốt lõi là dữ liệu đó bao gồm siêu dữ liệu (meta-data) – dữ liệu được nhập một cách độc lập với các hành động của bên được kiểm toán (auditee) – và không chỉ là dữ liệu do bên được kiểm toán nhập vào.
3. Khai thác quy trình cho phép kiểm toán viên có một cách thức hiệu quả hơn trong việc triển khai mô hình rủi ro kiểm toán bằng cách cung cấp những phương thức hiệu quả để thực hiện các thử nghiệm walk-through bắt buộc của quy trình và tiến hành các thủ tục phân tích.
4. Khai thác quy trình cho phép kiểm toán viên tiến hành những phân tích mà không thể thực hiện được bằng các công cụ kiểm toán hiện có, chẳng hạn như khám phá ra các cách thức mà các quy trình kinh doanh thực sự đang được thực hiện trên thực tế, và xác định các mối quan hệ xã hội giữa các cá nhân.

Khai thác quy trình có thể được sử dụng để xác định các quy trình từ đầu đến cuối – mang lại cái nhìn toàn diện về cách thức một quy trình di chuyển qua các hệ thống của công ty và vạch ra dấu vết kiểm toán (audit trail). Van der Aalst et al. (2010) phác thảo các khả năng của khai thác quy trình như là có khả năng cung cấp nguồn gốc kinh doanh (business provenance) bằng cách đảm bảo tính truy xuất nguồn gốc (traceability), phát hiện quy trình thông qua việc xác định các mô hình thường xuyên lặp lại, và có khả năng so sánh một mô hình định sẵn (a priori model) với các nhật ký sự kiện (event logs) và ngược lại.

Phân tích tập trung vào Dữ liệu (Data-Centric Analysis)
Phân tích kiểm soát nội bộ tập trung vào dữ liệu đề cập đến việc phân tích dữ liệu giao dịch để đánh giá các kiểm soát nội bộ và để thực hiện các thử nghiệm và thủ tục cơ bản thực tế. Dữ liệu này bao gồm những dữ liệu nằm trong các hệ thống kế toán và trở thành nguồn thông tin được sử dụng để xây dựng các báo cáo tài chính do ban quản lý cung cấp. Đây là các phân tích chung, chẳng hạn như ngân sách, báo cáo, kinh doanh thông minh (business intelligence), phân tích kinh doanh (business analytics) và các báo cáo thông tin quản lý khác. Trong các cấu trúc kiểm soát do con người dẫn dắt, các báo cáo này chính là huyết mạch của việc ra quyết định.
Trong một thế giới tự động, một số quá trình ra quyết định đó sẽ không còn được thực hiện bởi con người. Phần lớn nội dung này sẽ được thảo luận ở chương tiếp theo. Tuy nhiên, đối với chương này, điều quan trọng là phải xem xét rằng một hệ thống tài chính vi tính hóa được tạo thành từ dữ liệu giao dịch, các quy trình và cấu trúc cơ sở, và con người – người nhập dữ liệu hoặc đưa ra quyết định bên ngoài hệ thống. Những quyết định này có thể là về cách thức xử lý một giao dịch, hoặc đối chiếu cái gì/như thế nào, hay ghi nhận một bút toán ra sao. Tuy nhiên, trong khi việc ra quyết định của con người có thể được xem là ở bên ngoài hệ thống, do nó diễn ra trong tâm trí con người, thì những quyết định đó lại tác động đến những gì xảy ra trong hệ thống tài chính vi tính hóa. Chúng ta, những con người, vừa là một phần của hệ thống vừa tồn tại bên ngoài nó. Khi tiến bước cùng cuộc cách mạng AI, chúng ta có thể cần phải suy nghĩ khác đi về việc xem những gì diễn ra trong tâm trí con người là bên ngoài hệ thống và thay vào đó đưa những suy nghĩ, quyết định và khung nhận thức (cognitive frameworks) đó trở thành một phần của hệ thống. Việc mở rộng khái niệm hệ thống này xảy ra khi các khuôn khổ nhận thức và quá trình ra quyết định được chuyển giao từ tâm trí con người và nhúng (embedded) vào hệ thống tài chính.

Dữ liệu + Siêu dữ liệu (Data + Metadata)
Việc bổ sung học máy (machine learning) vào khai thác quy trình (process mining) là một sự đổi mới to lớn đối với kiểm toán. Khi được kết hợp lại, cả hai có thể tạo ra kiểm toán liên tục, tự động và tích hợp. Sáu năm sau khi đề xuất việc sử dụng khai thác quy trình, Jans cùng một tác giả khác đã đề xuất sử dụng học máy đi kèm với khai thác quy trình (Jans và Hosseinpour, 2019). Ý tưởng về học máy xuất phát từ thực tế là quá trình khai thác quy trình tạo ra một số lượng vô cùng lớn các ngoại lệ (exceptions). Các ngoại lệ này sau đó được con người diễn giải và đánh dấu là "đáng quan tâm" (of interest) và "không đáng quan tâm" (not of interest). Các ngoại lệ cung cấp một nguồn dữ liệu học tập khổng lồ, đến mức máy tính có thể học cách phân loại đầu ra của dữ liệu khai thác quy trình. Trên thực tế, dữ liệu được phân loại bởi con người cung cấp một tập hợp các ví dụ hoàn hảo cần thiết để dạy cho máy móc cách nhận diện các mô hình tốt (good) so với không thể chấp nhận được (unacceptable). Bằng cách sử dụng các thuật toán phân loại, máy tính có thể nhận diện các mô hình và khái quát hóa sự học hỏi của nó để nhận ra các mô hình bất thường vốn chưa từng được biết đến trước đó.

## 1.5 Các Hoạt động Kiểm soát Tự động (Control Activities)
Không giống như đánh giá môi trường kiểm soát tập trung vào các yếu tố thụ động của kiểm soát nội bộ, hoạt động kiểm soát (control activities) tập trung vào các hành động và hoạt động liên quan đến việc đảm bảo rằng các biện pháp kiểm soát nội bộ được thực thi, và các chỉ thị của hội đồng quản trị và ban quản lý về kiểm soát nội bộ được tuân thủ. Mục tiêu của việc đánh giá các hoạt động kiểm soát (McNally, 2013) là nhằm đảm bảo rằng tổ chức:
- Lựa chọn và phát triển các hoạt động kiểm soát.
- Lựa chọn và phát triển các kiểm soát chung đối với công nghệ.
- Triển khai các chính sách và quy trình.

Mục tiêu của tự động hóa thông minh (intelligent automation) là tự động hóa việc đánh giá mức độ đạt được của ba mục tiêu nêu trên một cách tự động.

Lựa chọn và Phát triển các Hoạt động Kiểm soát (Selects and Develops Control Activities)
Việc lựa chọn và phát triển các hoạt động kiểm soát là một hàm số của các rủi ro đã được nhận diện. Mỗi rủi ro trọng yếu đều yêu cầu phải có các biện pháp kiểm soát sao cho mục tiêu tổng thể là đảm bảo rủi ro có sai sót trọng yếu đối với tất cả các xác nhận liên quan (relevant assertions) được quản lý hiệu quả. Về một vài phương diện, các kiểm soát đóng vai trò phòng ngừa. Các gian lận và sai sót nên được phát hiện và sửa chữa trước khi chúng xâm nhập vào hệ thống tài chính.
Việc lựa chọn và phát triển các biện pháp kiểm soát có thể được xem như thiết lập một liên kết giữa mỗi rủi ro trọng yếu và quy trình phòng ngừa được thiết kế để ngăn chặn gian lận và sai sót đi vào hệ thống tài chính. Quy trình phòng ngừa này bao gồm các hoạt động được nhúng (embedded) vào trong các luồng công việc (workflows) và các quy trình kinh doanh. Ví dụ, tuyển dụng đúng người, thiết lập sự phân chia nhiệm vụ, xây dựng các hạn mức về quy mô giao dịch, thực thi việc phê duyệt trong luồng công việc, và giới hạn quyền truy cập vào các hệ thống là một số hoạt động then chốt được thực hiện.
Trong bối cảnh hiện đại hóa kiểm toán, có hai cách để xác định liệu ban quản lý có đang tích cực lựa chọn, phát triển các biện pháp kiểm soát và do đó tích cực tham gia vào các hoạt động kiểm soát hay không.
Cách thứ nhất là thông qua bằng chứng trực tiếp thu được để phản hồi lại sự đánh giá về các rủi ro đã biết (known risks). Bằng chứng này không dựa trên các bảng câu hỏi mà được thu thập trực tiếp (như đã thảo luận ở phần trước) và nó cho thấy liệu ban quản lý đã làm tốt việc chuẩn bị cho tổ chức ngăn chặn những sai sót trọng yếu và gian lận không thể lọt vào hệ thống kế toán hay chưa.
Cách thứ hai là tìm hiểu về năng lực và sự chuẩn bị của ban quản lý đối với các rủi ro mới nổi (emergent risks) chưa biết hoặc chưa được lường trước, vốn có thể phát sinh nhanh chóng và dẫn đến một sự kiện trọng yếu. Vì trọng tâm của kiểm toán viên chủ yếu nằm ở thông tin lịch sử, người ta có thể đặt câu hỏi về sự cần thiết của việc đưa điều này vào đánh giá. Lý do cho điều đó rất đơn giản. Thậm chí nếu chúng ta bỏ qua các lợi ích trực tiếp cho việc đánh giá tiềm năng (potential) so với đánh giá tập trung vào rủi ro đã biết, thì thực tế là việc ban quản lý tham gia vào tìm hiểu các rủi ro tiềm tàng tự bản thân nó đã là một dấu hiệu cho thấy ban quản lý đang hành xử có trách nhiệm và chủ động trong phản ứng phòng ngừa.
Mô hình này ngụ ý thiết lập một mô hình nhạy cảm với ngữ cảnh (context-sensitive model) cung cấp mối quan hệ giữa các rủi ro và các quy trình phản ứng phòng ngừa. Trong nhiều trường hợp, sẽ có những điểm tương đồng giữa các cách tiếp cận và rủi ro khác nhau. Rủi ro về xác nhận (assertion risk) có thể kêu gọi một sự phân chia nhiệm vụ chức năng cụ thể – chẳng hạn, trong các khoản phải trả (accounts payable), mua sắm và nhận hàng – bất kể đó là công ty nào. Trong các trường hợp khác, các rủi ro có thể đòi hỏi các phản ứng phòng ngừa mới, tùy chỉnh hoặc sáng tạo. Hầu hết hoạt động kiểm toán vận hành với các mô hình hiện có, cái mà van der Aalst et al. gọi là các mô hình theo quy chuẩn (de jure models), vốn "mô tả một cách thức làm việc mong muốn hoặc bắt buộc", ngược lại với các mô hình thực tế (de facto models) "nhằm mục đích mô tả thực tế với những vi phạm tiềm ẩn về các ranh giới được định nghĩa trong các mô hình de jure" (van der Aalst et al., 2011, 2010). Do đó, chúng ta có thể giả định rằng mô hình de jure là kết quả từ việc nhận thức được điều gì hiệu quả và điều gì không hiệu quả. Trong trường hợp này, chúng xuất phát từ kiến thức của kiểm toán viên về một biện pháp kiểm soát phòng ngừa nhất định là một sự giảm thiểu hiệu quả đối với một rủi ro cụ thể nhất định. Điều này ngụ ý rằng một bản thể luận (ontology) về rủi ro và các biện pháp phòng ngừa có thể được tạo ra, điều vốn về cơ bản có thể được chuyển hóa thành một tập hợp các quy tắc có thể được gọi ra hoặc dùng để kiểm tra đối chiếu cho một cuộc kiểm toán.

Tự động hóa lấy học máy làm trung tâm cho việc tự động hóa các hoạt động kiểm soát đề cập đến hai ứng dụng:
1. Ứng dụng nghiên cứu các mô hình rủi ro mới và đề xuất các chiến lược giảm thiểu rủi ro. Đây có thể là sự kết hợp của cả các cách tiếp cận không giám sát (phân cụm - clustering) và có giám sát (phân loại - classification). Nhiệm vụ của ứng dụng này là cập nhật các mô hình de jure hiện có. Cho dù việc cập nhật đó diễn ra thông qua học tập hay cập nhật các quy tắc hiện có, thì việc nhận dạng mô hình phản ứng-rủi ro (risk-response patterns recognition) vẫn là năng lực cốt lõi cần thiết để đề xuất và phát triển các hoạt động kiểm soát hiệu quả nhằm đối phó với các mô hình rủi ro mới nổi.
2. Ứng dụng tích hợp sự học hỏi ở trên và so sánh nó với các tình huống de facto (thực tế). Điều này được thực hiện từ sự kết hợp của phân tích “siêu dữ liệu + dữ liệu”, như đã thảo luận ở phần trước. Van der Aalst et al. đã làm rõ khái niệm đó khi họ nói: “Có khả năng thúc đẩy một mô hình de facto lên thành một mô hình de jure. Một sự so sánh cho thấy quá trình thực thi quy trình thực tế không nhất quán với mô hình tiền tồn tại (preexisting model) tiêu chuẩn có thể thúc đẩy việc cập nhật mô hình de jure” (van der Aalst et al., 2010). Những gì học máy làm là khám phá sự mâu thuẫn giữa mô hình de jure và mô hình de facto và sau đó nếu nó thấy mô hình de facto hiệu quả hơn, nó sẽ cập nhật mô hình de jure. Sự học hỏi có thể diễn ra từ ít nhất ba nguồn: (1) dữ liệu lịch sử từ các cuộc kiểm toán trước đây; (2) cơ sở kiến thức do kiểm toán viên (con người) cung cấp, nơi kiểm toán viên đưa ra các ví dụ về một phản ứng hiệu quả; và (3) hệ thống được thiết kế với một trình phê bình (critic) có thể mô phỏng các kịch bản rủi ro và phê bình các chiến lược được sử dụng để ngăn ngừa, chống lại các rủi ro dưới góc độ một cấu trúc mục tiêu. Thiết kế này nhìn chung sẽ yêu cầu việc sử dụng học tăng cường (reinforcement learning).

Lựa chọn và Phát triển Các Biện pháp Kiểm soát đối với Công nghệ (Selects and Develops Controls Over Technology)
Các hoạt động kiểm soát liên quan đến công nghệ đã được đề cập bởi van der Aalst et al. (2011), trong đó họ đề xuất khái niệm về một hệ thống giám sát (oversight system) được tạo ra để giám sát một hệ thống khác. Họ đã làm rõ rằng một biện pháp kiểm soát là “một tác vụ tự động trong hệ thống thông tin nhằm mục đích ngăn chặn sự vi phạm các quy tắc kinh doanh nhất định. Các biện pháp kiểm soát này liên quan chặt chẽ đến chức năng của hệ thống thông tin” và sau đó cảnh báo rằng “thường thì các quy tắc kinh doanh mang tính chung chung (tức là không bị ràng buộc vào một bối cảnh kinh doanh cụ thể)”.
Quá trình ban quản lý triển khai các biện pháp kiểm soát đối với công nghệ thông tin đang đạt được nhờ việc giám sát kiểm soát liên tục (continuous controls monitoring - CCM). CCM là một tập hợp các công cụ chuyên trích xuất dữ liệu từ cơ sở dữ liệu và quét tìm sự phân chia nhiệm vụ, các quyền hạn (authorizations), các sự vi phạm, lỗi, điểm bất thường, hạn mức về quy mô của giao dịch, v.v. Các biện pháp kiểm soát này được nhúng bên trong công nghệ.
Các kiểm soát truy cập công nghệ cũng là những cân nhắc quan trọng. Sự phân chia nhiệm vụ có thể được xác định chắc chắn từ các báo cáo về việc ai đã đăng nhập vào hệ thống. Việc đảm bảo rằng chỉ những người được ủy quyền truy cập hệ thống mới có thể truy cập được là điều thiết yếu để thiết lập một môi trường kiểm soát tốt hơn.
Sự xuất hiện của AI sẽ có ba tác động quan trọng đến lĩnh vực này. Thứ nhất, hai loại phân tích – dự đoán (predictive) và đề xuất (prescriptive) – được bổ sung vào bộ phát hiện điểm bất thường dựa trên quy tắc có tính tất định (deterministic) của CCM. Điều này có nghĩa là hệ thống không chỉ phân tích dữ liệu từ cơ sở dữ liệu, mà nó còn sử dụng dữ liệu để tìm hiểu về các sự vi phạm và do đó dự đoán chúng cũng như đưa ra các giải pháp khắc phục (prescriptive remedies) để chống lại các mối đe dọa. Tác động thứ hai là những lượng dữ liệu lớn hơn đáng kể có thể được xử lý và triển khai trong kiến trúc lấy học sâu (deep learning) làm trung tâm. Điều này cho phép phát hiện các gian lận và sai sót vốn không dễ bị phát hiện. Thứ ba, sự ra đời của AI sẽ dẫn đến việc thiết kế lại hoạt động kiểm soát và làm suy yếu các kiểm soát hiện có. Các hệ thống thông minh được triển khai không chỉ bởi những người đang cố gắng bảo vệ một công ty, mà còn bởi những kẻ không có ý định tốt đẹp. Điều này có nghĩa là các biện pháp kiểm soát thông minh sẽ trở nên cần thiết.
Hãy xem xét thực tế rằng các hệ thống giao dịch (có tính tất định) của chúng ta đang là một nguồn đáng lo ngại đối với chúng ta từ góc độ kiểm soát – hãy tưởng tượng đến sự xuất hiện của các cỗ máy thông minh trong tổ chức của chúng ta. Làm thế nào để chúng ta có thể quản lý và kiểm soát chúng? Sự ra đời của AI sẽ còn làm trầm trọng thêm vấn đề về kiểm soát. Chủ đề này được đề cập trong Chương 18 của cuốn sách này.

Triển khai các Chính sách và Quy trình (Deploys Policies and Procedures)
Các chính sách và quy trình được quét và sử dụng xử lý ngôn ngữ tự nhiên để phân tích nhằm xác định xem chúng có tuân thủ các loại rủi ro được xác định cho công ty khách hàng hay không. Chẳng hạn, tần suất của các từ khóa có thể phân loại tài liệu vào các lĩnh vực kiểm soát khác nhau và xác định xem liệu có sự bao phủ (coverage) thích hợp cho từng lĩnh vực kiểm soát hay không. Ví dụ: bằng cách sử dụng phương pháp Tần suất Thuật ngữ – Tần suất Tài liệu Nghịch đảo (Term Frequency - Inverse Document Frequency - TF-IDF), các tài liệu có thể được phân tích và phân loại dựa trên mức độ quan trọng và mức độ bao phủ.

Ví dụ: TF-IDF là gì? Tần suất Thuật ngữ – Tần suất Tài liệu Nghịch đảo (Term Frequency - Inverse Document Frequency)
TF-IDF là một phương pháp xử lý ngôn ngữ tự nhiên dựa trên việc tính toán tần suất của các từ ngữ. Nó gồm hai phần, phần TF (Tần suất thuật ngữ) và phần IDF (Tần suất tài liệu nghịch đảo). Trong phần TF, thuật toán tính số lần một thuật ngữ được sử dụng trong một tài liệu. Ví dụ, nếu bạn đang phân tích một tài liệu liên quan đến các chính sách và quy trình, bạn có thể biết được rằng các từ "Sự phân chia" (Separation) và "Nhiệm vụ" (Duties) được sử dụng tương ứng 34 và 28 lần. Nếu tài liệu dài tổng cộng 1000 từ, tần suất từ sẽ được tính bằng 34 chia cho 1000 đối với từ "Sự phân chia" và 28 chia cho 1000 đối với từ "Nhiệm vụ". Điều này mang lại một ước tính về số lần mỗi thuật ngữ được sử dụng trong một tài liệu và có thể cung cấp một cảm nhận về mức độ quan trọng của thuật ngữ đó trong tài liệu. Trong phần IDF, chúng ta tính toán tần suất tài liệu nghịch đảo bằng cách lấy toàn bộ kho ngữ liệu (tất cả các tài liệu) và xác định xem có bao nhiêu tài liệu đã sử dụng thuật ngữ này nói chung. Nó được tính toán bằng cách lấy log cơ số 2 của tổng số lượng tài liệu chia cho số lượng tài liệu trong đó thuật ngữ được sử dụng. Giả sử có 50 tài liệu tạo nên chính sách và quy trình, và các thuật ngữ "Sự phân chia" và "Nhiệm vụ" xuất hiện trong 12 và 32 tài liệu, thì log của 50/12 và 50/32 tương ứng sẽ cho chúng ta tần suất tài liệu nghịch đảo. Sau đó, TF-IDF được tính bằng cách nhân TF với IDF. Bằng cách sử dụng phương pháp này, chúng ta có thể xác định mức độ liên quan của các tài liệu đối với những chủ đề khác nhau. Một khi các giá trị TF-IDF được xác định, chúng ta cũng có thể tính toán những điểm tương đồng giữa các tài liệu. Ví dụ: chúng ta có thể ước tính tài liệu nào tập trung vào Sự phân chia Nhiệm vụ – các biện pháp kiểm soát nội bộ liên quan.

Các Biện pháp Kiểm soát Vật lý và Dữ liệu do Máy tạo ra (Physical Controls and Machine-Generated Data)
Các biện pháp kiểm soát vật lý là cần thiết để bảo vệ một số loại tài sản nhất định. Trước đây, các biện pháp kiểm soát truy cập vật lý bị giới hạn ở việc lắp đặt camera và ổ khóa. Cùng với những tiến bộ của AI, giờ đây chúng ta có cơ hội tạo ra những cải tiến đáng kể trong các biện pháp kiểm soát vật lý. Cơ hội này nằm ở việc đánh giá tự động đầu vào video để đánh giá xem việc sử dụng tài sản đó có tuân theo mục đích sử dụng dự kiến hay không. Nguồn cấp dữ liệu video (video feed) có thể được phân tích để phát hiện tình trạng sử dụng sai mục đích, trộm cắp và hành vi phá hoại tài sản một cách cố ý. Bên cạnh video, các dữ liệu Internet Vạn vật (IoT) khác cũng có thể được phân tích để xác định các biện pháp kiểm soát đối với sản xuất, hàng tồn kho, nhà kho, v.v. Tương tự, dữ liệu từ xe tải có thể được phân tích về dặm đường (travel miles), bảo trì và mô hình sử dụng đội xe.

## 1.6 Giám sát Tự động (Automated Monitoring)
Giám sát (Monitoring) đề cập đến việc ban quản lý thực hiện giám sát các hoạt động kiểm soát nội bộ một cách liên tục. Các chuẩn mực yêu cầu đội ngũ quản lý phải:
- Tiến hành các đánh giá liên tục và/hoặc đánh giá riêng biệt.
- Đánh giá và truyền đạt các khiếm khuyết (deficiencies): Mục tiêu của việc đánh giá là đảm bảo rằng ban quản lý tích cực lãnh đạo, quản lý và tham gia vào việc lập báo cáo. Trong một hệ thống tự động, chức năng giám sát tự động được nhúng vào bên trong máy móc. Trong các giai đoạn đầu của tự động hóa, người ta kỳ vọng rằng con người và máy móc sẽ chia sẻ trách nhiệm giám sát, nhưng khi công nghệ tiến lên, trách nhiệm này sẽ chuyển sang cho máy móc.
- Các kiểm soát tự động cung cấp thông tin về máy móc: Kiểm toán viên sẽ muốn xem bằng chứng cho thấy các kiểm soát tự động đang cung cấp bằng chứng về các hoạt động giám sát.
- Mô phỏng rủi ro (Risk simulation): Các kiểm toán viên có thể mô phỏng rủi ro trong một môi trường và quan sát hiệu suất của các biện pháp kiểm soát.
- Trình phê bình (Critic): Xác định xem có tồn tại một trình phê bình giúp tự động phê bình hiệu suất của các biện pháp kiểm soát giám sát hay không.
- Phân tích khoảng cách quy trình kinh doanh (Business process gap analysis): Thực hiện các kiểm tra tự động đối với phân tích khoảng cách của quy trình kinh doanh.
- Ngân sách, phương sai, và thẻ điểm (Budgets, variance, and scorecards).

## 1.7 Thông tin và Truyền thông (Information and Communications)
Các nguyên tắc hướng dẫn của COSO về thông tin và truyền thông nhấn mạnh rằng một tổ chức phải:
- Có được hoặc tạo ra, và sử dụng các thông tin chất lượng có liên quan để hỗ trợ chức năng của kiểm soát nội bộ.
- Truyền đạt thông tin nội bộ, bao gồm các mục tiêu và trách nhiệm đối với kiểm soát nội bộ, cần thiết để hỗ trợ kiểm soát nội bộ.
- Giao tiếp với các bên bên ngoài về kiểm soát nội bộ.
Mục tiêu của hệ thống thông tin và truyền thông kiểm soát nội bộ tự động là liên tục thu thập và tổng hợp các thông tin có thể hành động được (actionable information) về kiểm soát nội bộ, sau đó phổ biến nó cho cả các bên bên trong và bên ngoài.

Các phần trước đã đề cập đến một số artifact có thể được triển khai để tự động hóa kiểm soát nội bộ. Những artifact này sẽ cung cấp thông tin về trạng thái của chính chúng cũng như về các hoạt động của chúng. Ví dụ, tính năng tự quản trị (self-governance) có thể được tích hợp vào artifact và có thể báo cáo về các yếu tố như:
- Quy trình kinh doanh (Business process)
- Chi tiết giao dịch (Transaction details)
- Các sự kiện khác (Other events)
- Nguồn gốc dữ liệu (Data lineage)
Các báo cáo được tạo ra từ những yếu tố này có thể được gửi đến tất cả các bên liên quan và một quy trình báo cáo leo thang (escalation workflow) có thể được thiết kế.

## 1.8 Rủi ro Kiểm soát và Các Bước Tiếp theo (Control Risk and Next Steps)
Kế hoạch kiểm toán của chúng ta bắt đầu bằng việc sử dụng sâu rộng thông tin về công ty từ các nguồn bên ngoài nhằm phát triển một phân tích rủi ro tốt. Trong một số trường hợp, phân tích bên ngoài (từ ngoài vào trong) sẽ phơi bày những lĩnh vực rủi ro một cách rõ ràng như một chiếc đèn pin rọi sáng vào một điểm đáng quan tâm trong phòng tối. Trong những trường hợp khác, chúng sẽ mài giũa bản năng của chúng ta và khiến chúng ta nhận thức rõ hơn về những gì đang chờ đợi ở phía trước trong một hợp đồng dịch vụ (engagement).
Từ phương pháp từ ngoài vào trong, chúng ta chuyển sang dữ liệu và hệ thống nội bộ của một công ty. Cách tiếp cận của chúng ta trở nên có tính thâm nhập và sâu sắc hơn. Chúng ta đã xuyên thủng những bức bình phong che khuất và giành được quyền truy cập trực tiếp vào dữ liệu. Chính từ thời điểm đó, chúng ta bắt đầu đạt được sự tự tin vào khả năng giám sát và đánh giá các biện pháp kiểm soát một cách thông minh và liên tục.
Với sự hiểu biết thấu đáo về các rủi ro tiềm tàng (inherent risks) và rủi ro kiểm soát (control risks), các kiểm toán viên có thể đánh giá trọng tâm và mức độ của các thử nghiệm cơ bản (substantive procedures). Chúng tôi thảo luận về việc thu thập bằng chứng trực tiếp từ các tài khoản và thử nghiệm cơ bản trong chương tiếp theo.

Các Điểm Chính (Key Points)
- Thử nghiệm kiểm soát nội bộ là một trong những mục tiêu quan trọng nhất của một cuộc kiểm toán. Trong khi rủi ro tiềm tàng (inherent risk) thường là không thể kiểm soát được và là hàm số của mô hình kinh doanh của một công ty cùng nhiều thứ khác, thì rủi ro kiểm soát (control risk) lại có thể và nên được quản lý.
- Rủi ro kiểm soát bao gồm năm loại hình tự động hóa: môi trường kiểm soát tự động (automated controls environment), đánh giá rủi ro tự động (automated risk assessment), đánh giá hoạt động kiểm soát tự động (automated control activities assessment), đánh giá giám sát tự động (automated monitoring assessment), và đánh giá thông tin và truyền thông tự động (automation information and communications evaluation).
- Một kế hoạch tự động hóa kiểm toán phải giải quyết được tất cả các lĩnh vực này.

## 1.9 Tài liệu Tham khảo (References - Chương 9)
(Nội dung các tài liệu tham khảo được giữ nguyên theo bản gốc)
COSO (2013) Internal Control – Integrated Framework. [online]. Available from: https://www.coso.org/Documents/990025P-Executive-Summary-final-may20.pdf.
Curtis, P. and Carey, M. (2012) Risk assessment in practice. COSO. coso.org.
...
(Các tài liệu tham khảo khác như Fire và Puzis, Hollnagel, Humpherys, Jans, v.v.)

# 2. Tự động hóa Thông minh trong Phát hiện Gian lận (Intelligent Automation of Fraud Detection)

## 2.1 Khái niệm và Vai trò của Phát hiện Gian lận Thông minh (IFFDI Introduction)

CHÚNG TA ĐỀ CẬP ĐẾN CÁC SAI SÓT VÀ GIAN LẬN LIÊN QUAN ĐẾN KIỂM TOÁN xuyên suốt cuốn sách này; tuy nhiên, chương này dành riêng cho việc điều tra và phát hiện gian lận tài chính thông minh (intelligent financial fraud detection and investigation - IFFDI) sử dụng trí tuệ nhân tạo (AI). Môi trường kiểm soát nội bộ đóng vai trò như một bức tường lửa (firewall) để bảo vệ chống lại gian lận. Việc phòng ngừa khác với phát hiện và việc phát hiện thì khác với điều tra. Phát hiện ngụ ý việc chủ động tìm kiếm để khám phá, tìm ra, vạch trần hoặc phơi bày gian lận. Việc điều tra bắt đầu một khi có một mức độ nghi ngờ hợp lý phát triển về khả năng một vụ gian lận đang diễn ra. Trong chương này, chúng ta sẽ đề cập đến cả phát hiện và điều tra.
Khi triển khai các khả năng phát hiện gian lận của mình, bạn sẽ giải quyết các câu hỏi như:
- Làm thế nào để phân bổ các năng lực giữa việc phòng ngừa, phát hiện và điều tra? Những công nghệ nào cần triển khai cho mỗi lĩnh vực?
- Khi nào và sử dụng các công nghệ tất định (deterministic) so với ngẫu nhiên (stochastic) cho mục đích gì?
- Những phương pháp, mô hình, hay kỹ thuật nào bạn nên sử dụng?
- Làm thế nào để bạn thiết kế và cấu trúc hệ thống IFFDI của mình?
- Làm thế nào để bảo vệ công ty của bạn khỏi gian lận lấy AI làm trung tâm (AI-centric fraud)?

## 2.2 Phát hiện Gian lận và Cây Gian lận (Detecting Fraud and The Fraud Tree)
Gian lận xảy ra khi những sự trình bày sai lệch (misrepresentations) trọng yếu về các dữ kiện được thực hiện một cách có chủ ý và chúng dẫn đến tổn thất cho một hoặc nhiều nạn nhân. Hiệp hội các Giám định viên Gian lận Công chứng (Association of Certified Fraud Examiners - ACFE) phân loại gian lận chống lại một công ty thành hai loại: nội bộ và bên ngoài (ACFE, n.d.). Gian lận nội bộ (Internal fraud), còn được gọi là gian lận nghề nghiệp (occupational fraud), được ACFE định nghĩa là "việc sử dụng nghề nghiệp của một người để làm giàu cá nhân thông qua việc cố ý lạm dụng hoặc biển thủ các nguồn lực hoặc tài sản của tổ chức tuyển dụng". Gian lận nội bộ được thực hiện bởi các nhà quản lý, nhân viên, chủ sở hữu, hoặc các thành viên hội đồng quản trị của một công ty. Ngược lại, gian lận bên ngoài (External fraud) được thực hiện bởi các bên bên ngoài công ty, ví dụ như khách hàng, nhà cung cấp, đối tác.
ACFE phân loại gian lận nội bộ thành ba lĩnh vực: tham nhũng (corruption), biển thủ tài sản (asset misappropriation) và gian lận báo cáo tài chính (financial statement fraud). ACFE đã phát triển một sự thể hiện mạnh mẽ và toàn diện về gian lận nội bộ. Được biết đến với tên gọi Cây Gian lận (Fraud Tree) (Hình 12.1), nó bao hàm các danh mục con và các phân lớp khác nhau của gian lận nội bộ.

<div style="text-align: center; margin: 20px auto;">
    <img src="../Figures/Buoi_07B/FIGURE 12.1 The Fraud Tree.jpeg" alt="FIGURE 12.1 The Fraud Tree" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">Hình 12.1: Cây Gian lận ACFE (FIGURE 12.1 The Fraud Tree)</div>
</div>

Gian lận có thể xảy ra ở bất kỳ điểm nào trong một tổ chức. Ví dụ, nó có thể xảy ra ở cấp độ nhân viên, ở cấp độ hội đồng quản trị, hoặc trên toàn bộ chuỗi giá trị thông qua sự hợp tác giữa các đối tác và thậm chí cả các đối thủ cạnh tranh. Việc phát hiện gian lận là một trong những công việc phức tạp nhất. Việc bảo vệ một công ty khỏi bất kỳ sự gian lận tiềm ẩn nào có thể rất tốn kém và do đó các chi phí của IFFDI cần phải được xem xét.
Đừng quên rằng trong nhiều trường hợp, các nhà quản lý sành sỏi thường hoạt động trên ranh giới của luật pháp và mặc dù về mặt kỹ thuật, các báo cáo và tiết lộ (disclosures) có thể không bị đánh giá là những sự trình bày sai lệch dưới góc độ pháp lý, nhưng động cơ cơ bản cho các quyết định kinh doanh có thể là vì tư lợi. Chẳng hạn, ban quản lý của một tổ chức phi lợi nhuận triển khai một hội đồng quản trị thân thiện với CEO và với sự chấp thuận của hội đồng quản trị, họ bắt đầu thực hiện các khoản đầu tư theo cách thức mà CEO có ý định hưởng lợi cá nhân trong tương lai. Những tình huống như vậy khiến việc phát hiện gian lận trở nên cực kỳ khó khăn.

## 2.3 Các Yếu tố của Gian lận và Tam giác Gian lận (Elements of Fraud)
Vào những năm 1950, Donald Cressey đã trình bày lý thuyết tam giác gian lận (fraud triangle theory), trong đó xác định ba yếu tố của gian lận là áp lực (pressure), cơ hội (opportunity) và sự biện minh (rationalization) (Cressey, 1953). Một yếu tố thứ tư là khả năng (capability) sau đó đã được thêm vào và mô hình đã chuyển từ một hình tam giác sang một hình thoi (diamond) (Wolfe và Hermanson, 2004; Mansor, 2015). Khi chúng ta nghĩ về tự động hóa thông minh, các yếu tố thiết kế của chúng ta trước hết phải bắt đầu bằng việc phân tích các yếu tố của gian lận và xây dựng các năng lực xoay quanh chúng.

Áp lực hoặc Động lực (Pressure or Motivation)
Việc phát hiện từ sớm (preemptive detection) về động lực có thể tiến một bước dài trong việc phát hiện và ngăn ngừa gian lận. Động lực có thể là bất cứ thứ gì từ các tình huống cá nhân cho đến công việc. Ở cấp độ cá nhân, đó có thể là khi một người đang đối mặt với những khó khăn tài chính và do đó quyết định tham gia vào một vụ gian lận. Ở cấp độ ban quản lý, đó có thể là áp lực phải báo cáo những con số thu nhập nhất định (earnings numbers) theo như định hướng đã được đưa ra. Các công nghệ xác định động lực được triển khai để đánh giá các tình huống có thể thúc đẩy một người hoặc một đội ngũ quản lý phạm tội gian lận. Chúng thường liên quan đến việc hiểu các động lực học tình huống (situational dynamics) để dự đoán khả năng xảy ra gian lận.

Cơ hội (Opportunity)
Cơ hội cho gian lận được dựa trên những điểm yếu của kiểm soát nội bộ. Một môi trường thiếu các biện pháp kiểm soát hoặc có một nền văn hóa thúc đẩy sự cẩu thả có thể là một mảnh đất màu mỡ cho gian lận. Các cơ hội được nhận diện và khai thác bởi các cá nhân và các nhóm quản lý. Công nghệ đánh giá cơ hội gian lận được triển khai để đánh giá những điểm yếu trong kiểm soát cũng như việc xây dựng mô hình văn hóa và hành vi nhằm đánh giá mức độ nghiêm túc và mong muốn của ban quản lý và hội đồng quản trị trong việc triển khai các kiểm soát nội bộ.

Sự biện minh (Rationalization)
Sự biện minh là sự bào chữa mà một cá nhân hoặc một nhóm đưa ra cho hành vi gian lận. Đây là một yếu tố tự lừa dối bản thân, nơi các nhóm và cá nhân tự nhủ rằng việc tham gia vào hành vi gian lận là có thể chấp nhận được vì những lý do này nọ. Lời bào chữa có thể là đây chỉ là việc làm một lần, hoặc rằng họ chỉ đang mượn tiền, hoặc rằng họ đã bị từ chối sự đền bù xứng đáng và do đó việc ăn cắp là quyền của họ. Công nghệ phát hiện sự biện minh bao gồm các hệ thống được triển khai để thực hiện phân tích hành vi của các cá nhân và các nhóm.

Khả năng (Capability)
Khả năng là khi một người hoặc một nhóm tin rằng họ có năng lực (capability) để thoát khỏi việc thực hiện vụ gian lận, không bị bắt và thực hiện trót lọt nó. Công nghệ phát hiện khả năng cũng được sử dụng để đánh giá mức độ trọng yếu (materiality) của tác động mà một người, cỗ máy hoặc đội nhóm có thể gây ra.
AI đã được sử dụng để chống lại gian lận bằng cách xây dựng các năng lực phù hợp với tam giác gian lận trong thực tế. Ví dụ, Lin et al. (2015) đã sử dụng Hồi quy Logistic (Logistic Regression), Cây Quyết định (Decision Trees), Cây Phân loại và Hồi quy (Classification and Regression Trees - CART), và Mạng Nơ-ron Nhân tạo (Artificial Neural Networks - ANNs) để nghiên cứu ba khía cạnh của tam giác gian lận.

## 2.4 Phát hiện Gian lận Đặc thù theo Lĩnh vực (Domain-Specific Fraud Detection)
FBI phân loại các hành vi gian lận tài chính vào các lĩnh vực khác nhau như gian lận chứng khoán, gian lận thẻ tín dụng, gian lận báo cáo tài chính, gian lận bảo hiểm và các gian lận doanh nghiệp khác. Một cách để tiếp cận thiết kế của bạn là xem xét từng miền lĩnh vực cụ thể (domain area) mà bạn phải đối mặt với mức độ phơi nhiễm trọng yếu (material exposure). Điều này có nghĩa là các giải pháp chuyên biệt cần được phát triển trong những lĩnh vực cụ thể đó.
Có nhiều nghiên cứu đáng kể về việc sử dụng tự động hóa thông minh cho phát hiện gian lận đặc thù theo lĩnh vực (Ngai et al., 2011; West and Bhattacharya, 2016).

## 2.5 Mô hình STOPSCAM trong Phát hiện Gian lận (STOPSCAM Framework)
Viện Trí tuệ Nhân tạo Hoa Kỳ (American Institute of Artificial Intelligence) đã phát triển một mô hình được gọi là STOPSCAM. Mô hình này mở rộng dựa trên mô hình đặc thù theo lĩnh vực và các yếu tố gian lận để phát triển sự phân loại mở rộng về gian lận theo các lĩnh vực năng lực hoặc các bộ phát hiện (detectors) tập trung vào việc xây dựng và triển khai các năng lực thông minh. STOPSCAM là từ viết tắt của Strategy (Chiến lược), Transactions (Giao dịch), Operations (Hoạt động), Processes (Quy trình), Statements (Báo cáo/Tuyên bố), Culture (Văn hóa), Attitudes (Thái độ), và Model (Mô hình).

- **S - Chiến lược (Strategy)**: Công cụ chiến lược phân tích chiến lược của một công ty để thu thập những hiểu biết sâu sắc (key insights) nhằm nắm bắt các tín hiệu về những thay đổi đáng kể hoặc sự dai dẳng trong chiến lược của một công ty. Sự thay đổi đột ngột hoặc bất ngờ trong chiến lược, sự miễn cưỡng thay đổi chiến lược khi hiển nhiên là chiến lược đó không hiệu quả, sự nổi lên của một đối thủ cạnh tranh mới, sự thay đổi về công nghệ, rủi ro phá sản, và các khái niệm chiến lược khác đều được ghi nhận và phân tích. Các thay đổi về chiến lược cũng bao gồm các thương vụ sáp nhập, mua lại và các sự kiện tài trợ (financing events) lớn. Phân tích chiến lược tự động được thực hiện thông qua việc phân tích các báo cáo của chuyên gia phân tích, các thông cáo báo chí của công ty, cũng như các tin tức và ý kiến khác về một công ty.

- **T - Các giao dịch (Transactions)**: Phân tích ở cấp độ giao dịch đạt được bằng cách triển khai các hệ thống quét các chi tiết ở mức độ giao dịch. Ví dụ, các bút toán nhật ký, Sổ cái (G/L), kiểm tra các tài liệu hỗ trợ, và các ứng dụng tương tự khác của công nghệ trong kiểm toán tự động tạo thành đường cơ sở (baseline) cho kiểm toán liên tục ở cấp độ giao dịch với sự tập trung rõ ràng vào việc phát hiện điểm bất thường tập trung vào gian lận. Mục tiêu chính trong phân tích giao dịch là phát hiện bất thường (anomaly detection).

- **O - Các hoạt động (Operations)**: Đánh giá gian lận ở cấp độ hoạt động (Operational-level) được thực hiện bằng cách đánh giá dấu chân hoạt động (operational footprint) của một công ty và bao gồm cả chuỗi giá trị của công ty theo cả hai hướng. Điều này có nghĩa là bao gồm các nhà cung cấp và đối tác (ví dụ: các đối tác kênh) và khách hàng để phân tích tiềm năng xảy ra gian lận. Trong nhiều trường hợp, sự tương tác hoặc các cấu trúc giữa các đối tác, công ty con, khách hàng và nhà cung cấp cho thấy sự hiện diện của gian lận.

- **P - Các quy trình (Processes)**: Đánh giá gian lận tập trung vào quy trình tập trung vào việc hiểu các mô hình quy trình có tính bất thường. Các mô hình này có thể dựa trên các mô hình giao dịch, hoặc việc những người truy cập hệ thống một cách bất thường, hoặc các thời điểm truy cập hệ thống không hợp lý. Các công nghệ khai thác quy trình, cùng với học máy, được sử dụng để đánh giá điều này.

- **S - Báo cáo/Tuyên bố (Statements)**: Phân tích báo cáo (Statement analysis) được thực hiện bởi các bên bên ngoài, nơi các báo cáo tài chính được công bố công khai được phân tích để xác định sự tồn tại của gian lận. Điều này có thể dựa trên việc phân tích văn bản hoặc dữ liệu phi cấu trúc khác từ các báo cáo thường niên, hoặc các phân tích tỷ số tài chính, hoặc bằng cách phân tích các giao tiếp khác của công ty, chẳng hạn như cuộc gọi thu nhập (earnings call).

- **C - Văn hóa (Culture)**: Phân tích tự động ở cấp độ tổ chức tập trung vào việc thấu hiểu văn hóa, ban quản lý, các mối quan hệ báo cáo, các mạng lưới xã hội, hội đồng quản trị và các yếu tố tương tự khác. Nhiều yếu tố như vậy cung cấp thông tin về gian lận tiềm ẩn. Chẳng hạn, một CEO độc đoán hoặc quá hung hăng cùng với một hội đồng quản trị phục tùng có thể tạo ra một môi trường chín muồi cho gian lận.

- **A - Thái độ (Attitude)**: Thái độ là sự phân tích hành vi của đội ngũ quản lý và các thành viên hội đồng quản trị. Đây là một phần quan trọng của quá trình phân tích. Bằng cách sử dụng hình ảnh, video, văn bản, và các sự kết hợp khác cùng dữ liệu sẵn có, tự động hóa thông minh được sử dụng để tạo ra hồ sơ (profile) của các cá nhân và các mạng lưới xã hội. Các mạng lưới xã hội có thể tồn tại bên trong hoặc bên ngoài công ty. Chúng có thể tồn tại giữa các thành viên ban quản lý hoặc thành viên hội đồng quản trị và các giám đốc điều hành nhất định. Chúng được hình thành từ những mối quan tâm chung và dưới khía cạnh động lực học cấu trúc (structural dynamics), các mô hình ảnh hưởng có thể hoàn toàn khác với những gì được thể hiện trên các sơ đồ tổ chức của doanh nghiệp. Việc hiểu được những mô hình đó có thể làm sáng tỏ về cách thức gian lận có thể hình thành và ai có thể liên quan đến nó.

- **M - Mô hình (Model)**: Mô hình kinh doanh của một công ty là trung tâm của các chiến lược và quy trình của nó. Những thay đổi trong mô hình kinh doanh có thể biểu thị một số điều – bao gồm việc mở ra những cơ hội cho gian lận. Các công nghệ được sử dụng để phân tích các mô hình kinh doanh bao gồm việc lập bản đồ quy trình kinh doanh (business process mapping) bằng cách sử dụng học máy (Evermann et al., 2017). Sự trỗi dậy của AI trong kinh doanh cũng sẽ cho phép các doanh nghiệp triển khai các mô hình kinh doanh mới (Ehret và Wirtz, 2017).

## 2.6 Các Công nghệ và Mô hình AI trong Phát hiện Gian lận (Technologies and Models)
Ngai et al. (2011) đã thực hiện nghiên cứu tài liệu và chỉ ra rằng một loạt các phương pháp đang được sử dụng trong việc phát hiện gian lận. Họ đã phát triển một mô hình trong đó đầu tiên họ vạch ra các hạng mục gian lận rộng lớn như gian lận bảo hiểm, gian lận chứng khoán và hàng hóa, gian lận ngân hàng, và gian lận tài chính khác. Sau đó, họ tiếp tục phân loại dựa trên các hoạt động gian lận như rửa tiền (money laundering). Và từ khía cạnh giải pháp, họ chia các giải pháp khai thác dữ liệu thành phân loại (classification), phân cụm (clustering), phát hiện điểm ngoại lệ (outlier detection), dự đoán (prediction), hồi quy (regression) và trực quan hóa (visualization).
Gần đây hơn, một nhóm các nhà nghiên cứu khác cũng đã thực hiện một cuộc khảo sát sâu rộng về phát hiện gian lận (West và Bhattacharya, 2016). Họ cũng vậy, trước tiên họ tiến hành phân loại theo các lớp gian lận (ví dụ: bảo hiểm, báo cáo tài chính, v.v.). Tuy nhiên, họ đã điều tra một số phương pháp, bao gồm mạng nơ-ron, logistic, máy véc-tơ hỗ trợ (support-vector machine), cây quyết định, thuật toán di truyền (genetic algorithms), mạng niềm tin Bayesian (Bayesian belief network), khai thác quy trình, hệ miễn dịch nhân tạo (artificial immune system) và các phương pháp lai (hybrid methods). Cuộc khảo sát sâu rộng của họ tiết lộ rằng một sự đa dạng của các phương pháp đang được sử dụng trong tự động hóa thông minh.
Một cuộc khảo sát tài liệu thứ ba đã sử dụng một cách tiếp cận tương tự như những người khác; tuy nhiên, các nhà nghiên cứu này chia các kỹ thuật học máy thành các nhóm lớn gồm có giám sát (supervised), không giám sát (unsupervised) và bán giám sát (semi-supervised). Họ cũng đưa ra các ví dụ về những thách thức trong việc triển khai một số giải pháp và kỹ thuật giải quyết những vấn đề đó (Abdallah et al., 2016).
Nghiên cứu trên rất hữu ích để tìm hiểu về các phương pháp AI khác nhau đang được sử dụng trong nhiều loại lĩnh vực kinh doanh. Như chúng tôi đã thảo luận xuyên suốt cuốn sách này, cách tiếp cận điểm giải pháp (point solution approach) là không đủ nếu bạn muốn xây dựng một công ty kế toán pháp y hoặc kiểm toán kỷ nguyên hiện đại. Các công cụ phải làm việc cùng nhau để tạo thành một hệ sinh thái, trong đó các tác nhân (agents) khác nhau có thể làm việc cùng nhau để hoàn thành công việc.

## 2.7 Cách tiếp cận Thực tiễn của Chúng tôi (Our Approach)
Chúng tôi đã tiếp cận việc phát hiện gian lận không chỉ từ góc độ của lĩnh vực vấn đề (nghĩa là hạng mục gian lận > hoạt động gian lận > giải pháp) mà còn bằng cách đưa vào một lớp phân loại (class layer) cho việc triển khai giải pháp trong các lĩnh vực kinh doanh thực tiễn (tức là các tác nhân STOPSCAM). Các tác nhân STOPSCAM có thể được triển khai trong nhiều lĩnh vực khác nhau để phát hiện gian lận một cách toàn diện. Việc xây dựng một hệ thống phát hiện gian lận toàn diện đòi hỏi phải pha trộn bốn công nghệ chính là khai thác quy trình, tự động hóa quy trình bằng robot (robotic process automation), hệ chuyên gia (expert systems) và học máy (machine learning). Bên trong học máy tồn tại nhiều loại mô hình khác nhau và một số mô hình tốt hơn những mô hình khác đối với một số loại mô hình nhất định.
Chiến lược, tổ chức, văn hóa, thái độ và mô hình kinh doanh được tự động hóa bằng các thuật toán lập mô hình xã hội, hành vi, các quy trình lấy lý thuyết trò chơi làm trung tâm. Việc phát hiện gian lận giao dịch và báo cáo tài chính được tự động hóa bằng cách sử dụng phát hiện điểm bất thường, khai thác quy trình và hành vi.

Các Mô hình Có Giám sát trong Phát hiện Gian lận (Supervised Models in Fraud Detection)
Các kỹ thuật học có giám sát được triển khai trong phát hiện bất thường, các mô hình xã hội và hành vi. Cả hồi quy và phân loại đều có thể hỗ trợ trong việc phát hiện gian lận. Vì các kỹ thuật có giám sát dựa trên các ví dụ đã biết nên chúng dễ diễn giải hơn. Vấn đề chính của việc sử dụng học có giám sát là chúng ta thường (và may mắn thay) có nhiều ví dụ về các giao dịch không có gian lận hơn là các giao dịch gian lận. Do đó, việc dạy cho thuật toán trở nên khó khăn hơn khi, giả sử, đối với mỗi một ngàn ví dụ về giao dịch sạch (clean), thì mới cung cấp một ví dụ về một giao dịch gian lận. Có những kỹ thuật có thể được áp dụng để cân bằng các ví dụ. Chẳng hạn, một cách là đưa vào các ví dụ tổng hợp (synthetic - nhân tạo) về hành vi bất thường. Hạn chế thứ hai là dữ liệu cần được gán nhãn (labeling) và trừ khi dữ liệu đang được lấy ra từ các hệ thống nơi cả giá trị đầu vào và giá trị mục tiêu đầu ra đều có sẵn cho bài toán cụ thể đang được giải quyết, nếu không chúng ta có thể phải dựa vào việc gán nhãn dữ liệu tập trung vào con người (human-centric). Hãy nhớ lại rằng gán nhãn có nghĩa là cung cấp giá trị đầu ra mục tiêu cho mỗi véc-tơ đầu vào. Đó có thể trở thành một dự án khá tốn công sức.

Naïve Bayes, máy véc-tơ hỗ trợ (support-vector machines), k-láng giềng gần nhất (k-nearest neighbors), cây quyết định (decision trees), hồi quy logistic (logistic regression), học sâu (deep learning) và mạng nơ-ron nhân tạo (artificial neural networks) được sử dụng để tạo ra các artifact thông minh cho nhiều ứng dụng phát hiện gian lận khác nhau đã được vạch ra trong mô hình STOPSCAM.

Các Kỹ thuật Không Giám sát (Unsupervised Techniques)
Các kỹ thuật không giám sát được sử dụng trong việc phát hiện điểm bất thường, bao gồm trong các giao dịch, báo cáo và các quy trình. Chúng bao gồm các phương pháp phân cụm như k-means, các phương pháp giảm chiều dữ liệu (dimensionality reduction methods), dựa trên không gian con (subspace based) và dựa trên phân loại (classifier based) (Goldstein và Uchida, 2016). Mục tiêu ở đây là nhận diện các mô hình mà chúng ta không biết là chúng có tồn tại. Khi dữ liệu đang được phân tích phân cụm trong nhiều phân khúc khác nhau, nó tiết lộ sự hiện diện của các mô hình khác nhau. Một ví dụ về điều đó sẽ là sử dụng các kỹ thuật không giám sát để nhận diện phát hiện gian lận trong các vụ gian lận thẻ tín dụng.

Các Điểm Chính (Key Points)
- Phát hiện gian lận (Fraud detection) và phòng ngừa gian lận (fraud prevention) là khác nhau.
- Tự động hóa phát hiện gian lận tài chính được thực hiện thông qua việc điều tra và phát hiện gian lận tài chính thông minh (intelligent financial fraud detection and investigation).
- Phương pháp tiếp cận chung cho việc thiết kế tự động hóa thông minh phát hiện gian lận bao gồm việc thấu hiểu các hạng mục gian lận rộng lớn (ngân hàng, bảo hiểm, chăm sóc sức khỏe, v.v.), xác định các hoạt động bên trong những hạng mục đó, và sau đó triển khai các giải pháp dựa trên học máy bao gồm các phương pháp có giám sát, không giám sát, bán giám sát và các phương pháp khác.
- Từ góc độ phân loại giải pháp, chúng tôi đề xuất phát triển các giải pháp xoay quanh phương pháp STOPSCAM.

## 2.8 Tài liệu Tham khảo (References - Chương 12)
(Nội dung các tài liệu tham khảo được giữ nguyên theo bản gốc)
Abdallah, A., Maarof, M. A., and Zainal, A. (2016) Fraud detection system: A survey. Journal of Network and Computer Applications, 68 (C): 90–113.
ACFE (n.d.) Association of Certified Fraud Examiners. Available from: https://www.acfe.com/fraud-101.aspx.
Cressey, D. R. (1953) Other People's Money: A Study of the Social Psychology of Embezzlement. Glencoe, IL: Free press.
Ehret, M. and Wirtz, J. (2017) Unlocking value from machines: Business models and the industrial internet of things. Journal of Marketing Management, 33 (1–2): 111–130.
Evermann, J., Rehse, J. R., and Fettke, P. (2017) Predicting process behaviour using deep learning. Decision Support Systems, 100: 129–140.
Goldstein, M. & Uchida, S. (2016) A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data. PLoS ONE, 11 (4): 1–31.
Lin, C., Chiu, A., Yan, S, and Yen, D. C. (2015) Detecting the financial statement fraud: The analysis of the differences between data mining techniques and experts' judgments. Knowledge-Based Systems, 89: 459–470.
Mansor, R. A. N. (2015) Forensic accounting and fraud risk factors: The influence of fraud diamond theory. The American Journal of Innovative Research and Applied Sciences, 7 (28), 186–192.
Ngai, E. W. T., Hu, Y., Wong, Y. H., Chen, Y., and Sun, X. (2011) The application of data mining techniques in financial fraud detection: A classification framework and an academic review of literature. Decision Support Systems, 50 (3): 559–569.
West, J. and Bhattacharya, M. (2016) Intelligent financial fraud detection: A comprehensive review. Computers and Security, 57: 47–66.
Wolfe, D. T. and Hermanson, D. R. (2004) The Fraud diamond: Considering the four elements of fraud: Certified public accountant. The CPA Journal, 74 (12): 38–42.

#### ** 🎬 Video **

<iframe src="video/Day07/index.html?v=1785919941" style="width: 100%; aspect-ratio: 16/9; max-height: 75vh; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>

#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slideAIAcc/Slide_AIAcc_Day07.pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day07.pdf#view=FitH" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day07.pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

#### ** 📝 Bài tập Trắc nghiệm **

<iframe src="quizzes/Day07/index.html?v=1785919941" style="width: 100%; min-height: 700px; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>


#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: RPA và AI trong kiểm soát chứng từ (Độ khó: Dễ)**
Phân biệt RPA (Robotic Process Automation) và AI. Đâu là công cụ phù hợp để trích xuất dữ liệu từ các hóa đơn có định dạng hoàn toàn khác nhau của hàng trăm nhà cung cấp?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- RPA là "cơ bắp", hoạt động theo quy tắc cố định (Click vào tọa độ X, copy ô Y). RPA sẽ thất bại nếu định dạng hóa đơn thay đổi.
- AI (đặc biệt là Machine Learning / OCR kết hợp NLP) là "bộ não". Nó có khả năng tự hiểu ngữ cảnh và bóc tách đúng số tiền, mã số thuế dù các hóa đơn có form khác nhau.
</details>
<br>

**Bài tập 2: Kiểm toán Liên tục - Continuous Auditing (Độ khó: Trung bình)**
Theo Chương 9, khái niệm "Kiểm toán liên tục" bằng AI thay đổi quy trình kiểm toán truyền thống như thế nào?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Truyền thống: Kiểm toán dựa trên mẫu (Sampling) và thực hiện sau khi kết thúc niên độ. Kẻ gian lận có đủ thời gian che giấu.
- Continuous Auditing (CA): AI kết nối trực tiếp vào ERP, kiểm tra 100% giao dịch ngay khi chúng phát sinh theo thời gian thực (Real-time). Bất kỳ giao dịch đáng ngờ nào cũng bị cờ đỏ (Red-flag) tức thời.
</details>
<br>

**Bài tập 3: Unsupervised Learning phát hiện gian lận mới (Độ khó: Khó)**
Theo Chương 12, phân tích cách Học không giám sát (Unsupervised Learning) phát hiện một mẫu giao dịch gian lận hoàn toàn mới chưa từng có trong lịch sử (Zero-day fraud).
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Mô hình có giám sát (Supervised) chỉ phát hiện được các kiểu gian lận đã được gán nhãn trong quá khứ.
- Unsupervised Learning không cần nhãn. Nó chỉ tìm kiếm "điểm dị biệt" (Anomaly). Bất cứ giao dịch nào lệch xa khỏi cụm hành vi thông thường của đám đông (Ví dụ: Chuyển tiền lúc 3h sáng từ IP nước ngoài) đều bị cô lập thành bất thường, kể cả khi chiêu thức này chưa từng xuất hiện.
</details>
<br>
<!-- tabs:end -->
