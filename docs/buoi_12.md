# Buổi 12: Thực hành AI Nhận thức và AI Tạo sinh trong Kế toán - Tài chính (Generative AI & Web-Enhanced ChatGPT)

<!-- tabs:start -->

#### ** 📚 Thuật ngữ & Khái niệm **

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Ẩn dụ Kính chắn gió (Windshield Metaphor)</b></summary>
<br>

Hình ảnh ví von nghề kế toán cũ giống như việc lái xe chỉ nhìn vào kính chiếu hậu (cặm cụi ghi chép quá khứ). GenAI giúp gỡ bỏ màn đen, trang bị GPS để dự báo tương lai, giúp kế toán chuyển từ "Tư duy ghi chép" sang "Tư duy cố vấn".

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Trí tuệ Nhân tạo Tạo sinh (GenAI)</b></summary>
<br>

Thế hệ AI mới không chỉ biết tính toán cộng trừ như máy tính sơ khai, mà tiến hóa đến mức thấu hiểu ngôn ngữ, suy luận và sáng tạo ra nội dung mới.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Phần mềm Rule-based (Nếu-Thì)</b></summary>
<br>

Cỗ máy kế toán kiểu cũ, hoạt động như một cỗ máy "dò từ khóa" cứng nhắc. Chỉ cần hóa đơn sai một lỗi chính tả nhỏ, hệ thống sẽ báo lỗi đỏ chót và kẹt cứng.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Sự thấu hiểu ngữ nghĩa (Semantic Understanding)</b></summary>
<br>

Khả năng của Mạng Neural sâu phân tích hàng tỷ tham số để hiểu ý nghĩa thực sự của câu văn. Dù chứng từ có bị sai sót đánh máy, AI vẫn hiểu mục đích cốt lõi như một chuyên gia thuế lão làng.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Phân tích dự báo (Predictive Analytics)</b></summary>
<br>

Khả năng phân tích biến động (ví dụ: tỷ giá, dòng tiền) và hú còi báo động các nguy cơ thiếu hụt thanh khoản trong tương lai ngay theo thời gian thực thay vì đợi đến cuối quý.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Hiểu biết dữ liệu (Data Literacy)</b></summary>
<br>

Kỹ năng sinh tồn cốt lõi. Kế toán viên không cần biết viết code lập trình, nhưng bắt buộc phải hiểu cơ chế: máy nạp dữ liệu gì vào thì sẽ mớm ra kết quả gì, để kiểm soát và không bị thuật toán lừa.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Kể chuyện dữ liệu (Data Storytelling)</b></summary>
<br>

Năng lực diễn giải của con người, biến một bảng Dashboard chi chít biểu đồ vô tri thành một "câu chuyện kinh doanh" mạch lạc nhằm thuyết phục lãnh đạo chốt phương án chiến lược.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Mô hình ngôn ngữ lớn (LLMs)</b></summary>
<br>

Nền tảng cốt lõi của ChatGPT. Bản chất toán học của nó không phải là "suy nghĩ" như con người, mà chỉ là cố gắng "Đoán xác suất của từ tiếp theo" dựa trên kho dữ liệu khổng lồ nó được huấn luyện.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Ảo giác AI (Hallucination)</b></summary>
<br>

Hiện tượng vô cùng nguy hiểm khi AI tự tin bịa ra một điều khoản luật không có thật hoặc một con số ma, nhưng trình bày nó với một thái độ đĩnh đạc, cực kỳ thuyết phục.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Sự nhạy bén thương trường (Business Acumen)</b></summary>
<br>

Điểm yếu chí mạng của AI. AI giống như một cậu phụ việc siêu phàm nhưng non nớt về bối cảnh thực tế (ví dụ báo động sai một khoản chi khổng lồ thuộc về thương vụ sáp nhập đã được lên kế hoạch từ trước).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Tư duy phản biện (Critical Thinking)</b></summary>
<br>

Vũ khí tối thượng của kế toán viên. Luôn duy trì thái độ hoài nghi với kết quả máy tính đưa ra. (Kế toán viên là Bếp trưởng, AI là Phụ bếp. Trước pháp luật, Bếp trưởng là người ký duyệt và chịu trách nhiệm).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Dân chủ hóa AI (Democratization of AI)</b></summary>
<br>

Hiện tượng đột phá cho phép bất kỳ Kế toán viên nào cũng có thể tự xây dựng một con Bot AI riêng cho mình chỉ bằng cách trò chuyện bằng tiếng người mà không cần kỹ năng lập trình.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">GPT Store & Custom GPTs (GPT tùy chỉnh)</b></summary>
<br>

Cửa hàng ứng dụng để tải về các "Bộ não kỹ thuật số". Đặc biệt, Custom GPT cho phép doanh nghiệp nạp Sổ tay nội bộ vào để đào tạo một trợ lý AI mang tính cách và chuyên môn riêng biệt.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Cơ chế RAG (Truy xuất tăng cường)</b></summary>
<br>

"Khắc tinh" của Ảo giác AI. Kỹ thuật này khóa miệng AI lại, ép nó mỗi khi trả lời bắt buộc phải truy xuất vào đúng tài liệu nội bộ đã được doanh nghiệp cung cấp, triệt tiêu gần như hoàn toàn việc bịa chuyện.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Cửa sổ Ngữ cảnh (Context Window)</b></summary>
<br>

Bộ nhớ ngắn hạn siêu phàm của GenAI. Khả năng nhớ dai dẳng toàn bộ lịch sử hàng trăm trang tài liệu để đối chiếu chuỗi nghiệp vụ tài chính phức tạp mà không bị "nói câu sau quên câu trước".

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">AI Phiên bản Enterprise (Bong bóng kín)</b></summary>
<br>

Tiêu chuẩn bảo mật pháp lý bắt buộc (chứng chỉ SOC 2) dành cho doanh nghiệp tài chính. Dữ liệu nạp vào được cô lập, cấm nhà cung cấp AI đem đi huấn luyện, giúp ngăn chặn thảm họa rò rỉ bí mật chiến lược của công ty.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Mã hóa / Làm mờ dữ liệu (Data Masking)</b></summary>
<br>

Kỷ luật bắt buộc đối với nhân viên: luôn che giấu thông tin cá nhân khách hàng, số thẻ tín dụng trước khi nạp dữ liệu lên môi trường AI để tuân thủ các đạo luật bảo vệ quyền riêng tư (GDPR, CCPA).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Con người trong vòng lặp (HITL - Human-in-the-loop)</b></summary>
<br>

Quy tắc Vàng trong quản trị rủi ro tự động hóa. Không bao giờ cấp quyền cho AI tự động bấm nút "Chuyển tiền". Mọi luồng lệnh tài chính sinh ra từ AI bắt buộc phải chui qua khe cửa cuối cùng là cái nhấp chuột duyệt của con người.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Kiểm toán liên tục (Continuous Auditing)</b></summary>
<br>

Tương lai của ngành kiểm toán. AI sẽ bám đuôi từng giao dịch một cách thầm lặng và phát hiện lỗi sai chỉ trong 1 phần nghìn giây sau khi thao tác được thực hiện, thay vì phải gom chờ kiểm kê vào cuối quý.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Mạng lưới tự chữa lành (Self-Healing System)</b></summary>
<br>

Đích đến vĩ đại của hệ thống tài chính kỷ nguyên số, nơi thuật toán bóp nghẹt mọi mầm mống gian lận, bòn rút ngầm hay sai sót kế toán ngay từ trong trứng nước trước khi đồng tiền bẩn kịp lọt ra ngoài.

</details>



#### ** 🇬🇧 Tiếng Anh **

### 📄 Tài liệu PDF 1: Chương 1: Generative AI in Accounting (Scott Dell)

<object data="textbook/Buoi_12A_Chương 1 (Generative AI in Accounting).pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_12A_Chương 1 (Generative AI in Accounting).pdf#view=FitH" target="_blank">Nhấn vào đây để tải tài liệu PDF 1</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_12A_Chương 1 (Generative AI in Accounting).pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 1 (PDF)</a></p>

---

### 📄 Tài liệu PDF 2: Chương 12: Web-Enhanced ChatGPT & Custom GPTs

<object data="textbook/Buoi_12B_Chương 12 (Web-Enhanced ChatGPT).pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_12B_Chương 12 (Web-Enhanced ChatGPT).pdf#view=FitH" target="_blank">Nhấn vào đây để tải tài liệu PDF 2</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_12B_Chương 12 (Web-Enhanced ChatGPT).pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 2 (PDF)</a></p>


#### ** 🇻🇳 Tiếng Việt **

# CHƯƠNG 1: TRÍ TUỆ NHÂN TẠO SÁNG TẠO (GAI) TRONG KẾ TOÁN

> *"Nó chậm, nhiều lỗi, nó không làm tốt nhiều việc, nhưng những thứ đầu tiên cũng vậy: máy tính."*  
> – **Sam Altman**, Giám đốc điều hành và đồng sáng lập OpenAI

Lĩnh vực kế toán, theo truyền thống được coi là pháo đài của các quy trình thủ công và xử lý số lượng lớn, đang chứng kiến một cuộc cách mạng mang tính biến đổi – sự ra đời của **Trí tuệ nhân tạo sáng tạo (Generative Artificial Intelligence - GAI)**. Công nghệ đột phá này không chỉ là một công cụ mới trong kho vũ khí kế toán; nó thể hiện sự thay đổi mô hình trong cách xử lý, phân tích và sử dụng dữ liệu tài chính.

Trọng tâm của sự chuyển đổi này là khả năng GAI tự động hóa các tác vụ phức tạp, thu thập hiểu biết sâu sắc từ các bộ dữ liệu khổng lồ và nâng cao quá trình ra quyết định. Trong chương này, chúng ta bắt tay vào một hành trình khám phá các hoạt động phức tạp, ứng dụng và tác động sâu sắc của GAI trong lĩnh vực kế toán:
- Chúng ta bắt đầu bằng việc truy tìm nguồn gốc và sự phát triển của AI trong bối cảnh kế toán, cung cấp một góc nhìn lịch sử nêu bật những cột mốc quan trọng dẫn đến tình trạng hiện tại của AI.
- Khám phá các yêu cầu kỹ thuật để khai thác GAI trong kế toán, bao gồm phần cứng, phần mềm và cả tư duy cần thiết để tích hợp AI một cách hiệu quả vào quy trình công việc kế toán truyền thống.
- Hiểu cách GAI, đặc biệt là các công cụ như ChatGPT và Mô hình ngôn ngữ lớn (LLM), đang tạo nên làn sóng trong lĩnh vực kế toán.
- Đề cập đến những nỗi sợ hãi chung và quan niệm sai lầm về AI, đưa ra cái nhìn cân bằng về những lợi ích và hạn chế tiềm ẩn của nó.
- Khám phá vai trò của AI trong các lĩnh vực công cộng và riêng tư, cơ quan thuế, ý nghĩa đối với xã hội nói chung và các kỹ năng mà kế toán viên cần có để phát triển trong bối cảnh mới này.

---

## 1.1 Điều kiện tiên quyết (Prerequisites)

Việc tích hợp GAI vào lĩnh vực kế toán đòi hỏi phải có cơ sở hạ tầng kỹ thuật mạnh mẽ, bao gồm một loạt các công cụ và phần mềm được thiết kế để khai thác tiềm năng của AI. Công nghệ này tuy mạnh mẽ nhưng đòi hỏi phải có môi trường phù hợp để phát triển và phát huy hết khả năng của mình.

### 1. Các công cụ cơ bản cần thiết
- **Trình duyệt web hiện đại:** Bước đầu tiên để truy cập các công cụ AI như ChatGPT là thông qua trình duyệt web. Các trình duyệt hiện đại như Chrome, Edge, Firefox hoặc Safari rất cần thiết để tương tác liền mạch với nền tảng AI.
- **Truy cập nền tảng AI:** Việc đăng ký và truy cập vào các nền tảng AI như OpenAI là rất quan trọng. Trang web của OpenAI cung cấp quyền truy cập vào các phiên bản khác nhau của công cụ GAI, bao gồm các mô hình ChatGPT được sử dụng rộng rãi.
- **Sự tò mò trí tuệ (Intellectual Curiosity):** Ngoài các công cụ kỹ thuật, tư duy tò mò trí tuệ là nền tảng. Tương tác với công nghệ AI đòi hỏi sự cởi mở để khám phá, thử nghiệm và thích ứng với những phương thức xử lý và phân tích dữ liệu mới.

### 2. Phần mềm kế toán hỗ trợ AI
- **Công cụ xử lý dữ liệu tự động:** Phần mềm kế toán được tăng cường AI, chẳng hạn như QuickBooks với các tính năng AI, tự động hóa các công việc lặp đi lặp lại như nhập dữ liệu, phân loại và đối chiếu, giúp giảm đáng kể khối lượng công việc thủ công.
- **Phân tích và báo cáo nâng cao:** Phần mềm như Xero được tích hợp AI cung cấp khả năng phân tích dữ liệu nâng cao, cho phép kế toán viên rút ra những hiểu biết sâu sắc hơn từ dữ liệu tài chính, tạo báo cáo toàn diện và đưa ra lời khuyên chiến lược dựa trên các dự đoán dữ liệu.

### 3. Công cụ phân tích và Quản lý dữ liệu
- **Phân tích dự đoán (Predictive Analytics):** Các công cụ như IBM Cognos Analytics sử dụng AI để thực hiện phân tích dự đoán, cung cấp thông tin hướng tới tương lai rất quan trọng cho việc lập kế hoạch chiến lược và ra quyết định.
- **Trực quan hóa dữ liệu (Data Visualization):** Các công cụ được hỗ trợ bởi AI chẳng hạn như Tableau biến các bộ dữ liệu phức tạp thành biểu đồ dễ hiểu và có thể hành động.
- **Lưu trữ đám mây an toàn:** Các giải pháp lưu trữ đám mây như AWS hoặc Microsoft Azure trang bị AI mang lại sự an toàn và khả năng mở rộng để lưu trữ lượng lớn dữ liệu tài chính.
- **Bảo mật và tuân thủ dữ liệu:** Tích hợp AI đòi hỏi các giao thức bảo mật mạnh mẽ như mã hóa, truyền dữ liệu an toàn và tuân thủ các tiêu chuẩn bảo mật (GDPR, CCPA).

---

## 1.2 Đổi mới AI trong kế toán – Tính toán tự động và Phân tích dự đoán

Sự ra đời của AI trong kế toán đã đánh dấu một bước tiến đáng kể trong cách xử lý và phân tích dữ liệu tài chính. Trọng tâm của sự tiến bộ này là vai trò của AI trong việc tự động hóa các tính toán phức tạp và cung cấp phân tích dự đoán.

### 1. Tự động hóa các phép tính phức tạp
- **Hiệu quả và chính xác:** AI chuyển đổi cách tính toán kế toán truyền thống từ tốn thời gian và dễ sai sót sang hiệu quả và có độ chính xác cao. Các công cụ AI có thể xử lý các phép tính phức tạp như ước tính thuế, khấu hao và dự báo tài chính với tốc độ vượt trội.
- **Thuật toán thích ứng:** Hệ thống AI hiện đại trong phần mềm kế toán có thể thích ứng với những thay đổi của môi trường và quy định tài chính. Chúng liên tục học hỏi từ dữ liệu mới, đảm bảo tuân thủ luật thuế và chuẩn mực báo cáo.
- **Giảm sai sót:** Việc tự động hóa giúp giảm đáng kể nguy cơ lỗi con người, đảm bảo sự tuân thủ và tính chính xác trong báo cáo tài chính.

### 2. Cung cấp phân tích dự đoán
- **Dự báo và lập kế hoạch:** AI phân tích các mẫu dữ liệu lịch sử để dự đoán các kịch bản tài chính trong tương lai, giúp kế toán viên và lãnh đạo doanh nghiệp đưa ra những quyết định chiến lược sáng suốt.
- **Giải thích dữ liệu sâu sắc:** AI vượt xa việc xử lý dữ liệu đơn thuần; nó diễn giải dữ liệu để xác định xu hướng tài chính, rủi ro tiềm ẩn và cơ hội, hướng dẫn doanh nghiệp tối ưu hóa hiệu suất tài chính.
- **Tư vấn tài chính tùy chỉnh:** Thuật toán AI điều chỉnh phân tích theo nhu cầu kinh doanh cụ thể, mang lại lời khuyên tài chính được tùy chỉnh phù hợp với tình hình tài chính riêng của từng doanh nghiệp.

#### Bảng 1.1 – Tóm tắt tác động của AI đối với kế toán

| Khu vực tác động | Mô tả sự đổi mới của AI | Ảnh hưởng đến thực hành kế toán |
| :--- | :--- | :--- |
| **Xử lý dữ liệu tự động** | Thuật toán AI tự động hóa các tác vụ như nhập và phân loại dữ liệu, giảm bớt công sức thủ công. | Tăng hiệu quả, giảm sai sót, cho phép kế toán viên tập trung vào các nhiệm vụ tư vấn chiến lược cấp cao hơn. |
| **Phân tích dự đoán** | AI sử dụng dữ liệu lịch sử để dự đoán các kịch bản và xu hướng tài chính trong tương lai. | Tăng cường lập kế hoạch tài chính và ra quyết định chiến lược với những hiểu biết sâu sắc dựa trên dữ liệu. |
| **Nâng cao tuân thủ** | Hệ thống AI giám sát liên tục các giao dịch tài chính để đảm bảo tuân thủ quy định. | Cải thiện độ chính xác, giảm thiểu rủi ro vi phạm quy định và tránh các hình phạt. |
| **Nâng cao khả năng báo cáo** | Các công cụ AI phân tích dữ liệu tài chính và tạo ra các báo cáo toàn diện, đa chiều. | Cung cấp cái nhìn sâu sắc hơn và bức tranh tài chính rõ ràng hơn cho ban lãnh đạo và các bên liên quan. |
| **Tư vấn tài chính được cá nhân hóa** | AI tùy chỉnh lời khuyên tài chính dựa trên nhu cầu, đặc thù và kịch bản kinh doanh cụ thể. | Điều chỉnh chiến lược tài chính phù hợp với bối cảnh thực tế của doanh nghiệp, mang lại hiệu quả cao nhất. |

---

## 1.3 Nghiên cứu điển hình và Ứng dụng thực tế (Case Studies)

### 1. Quán cà phê Brewed Awakenings với QuickBooks Online (Doanh nghiệp nhỏ)
- **Thách thức:** Là một doanh nghiệp nhỏ với đội ngũ nhân viên hạn chế, việc quản lý tài chính, đặc biệt là lập kế hoạch và tuân thủ thuế, là một thách thức đáng kể.
- **Giải pháp AI:** Triển khai **QuickBooks Online**, sử dụng khả năng AI để theo dõi chi phí tự động, phân loại chi phí thông minh và đối chiếu giao dịch ngân hàng/thẻ tín dụng.
- **Kết quả:** Giảm thiểu lỗi nhập liệu thủ công, cung cấp thông tin dự báo dòng tiền và rủi ro tài chính, giúp chủ quán chuyển hướng thời gian tiết kiệm được sang phát triển kinh doanh và chăm sóc khách hàng.

### 2. Cityscape Consulting với Xero (Công ty tư vấn quy mô vừa và nhỏ)
- **Thách thức:** Quản lý ngân sách dự án, kế toán và tuân thủ thuế cho các dự án kiến trúc và thiết kế đô thị đổi mới.
- **Giải pháp AI:** Triển khai **Xero** với giao diện trực quan và tính năng tự động nhập giao dịch ngân hàng, phân loại chi phí thông minh và theo dõi dòng tiền theo thời gian thực.
- **Kết quả:** Phân tích dựa trên AI cung cấp thông tin dự báo dòng tiền và đưa ra đề xuất khấu trừ thuế, giúp hợp lý hóa quản lý ngân sách và cải thiện lợi nhuận dự án.

### 3. GlobalTech Enterprises với IBM Watson (Tập đoàn đa quốc gia)
- **Thách thức:** Quản lý tài chính ở nhiều quốc gia khác nhau, tuân thủ luật thuế đa dạng và xử lý khối lượng giao dịch liên công ty khổng lồ.
- **Giải pháp AI:** Tích hợp nền tảng AI tiên tiến **IBM Watson** để tự động hóa tuân thủ luật thuế quốc tế, lập mô hình tài chính dự đoán và xử lý các giao dịch xuyên biên giới.
- **Quản trị đạo đức và an ninh:** Đảm bảo tuân thủ tiêu chuẩn bảo mật GDPR/CCPA, thực hiện kiểm tra thường xuyên và loại bỏ thiên vị trong đánh giá rủi ro tín dụng và phát hiện gian lận.

---

## 1.4 Chuẩn bị cho một tương lai dựa trên AI trong kế toán

Việc tích hợp AI vào kế toán không chỉ đòi hỏi công nghệ mà còn đòi hỏi sự thay đổi về kỹ năng và đào tạo nhân sự.

#### Bảng 1.2 – Các kỹ năng và đào tạo cần thiết trong môi trường do AI điều khiển

| Kỹ năng / Đào tạo | Mô tả chi tiết | Tầm quan trọng đối với Kế toán viên |
| :--- | :--- | :--- |
| **Hiểu biết về dữ liệu (Data Literacy)** | Khả năng đọc, hiểu, quản lý và giao tiếp hiệu quả với dữ liệu tài chính. | Nền tảng cần thiết để điều hướng và tận dụng các nền tảng phân tích AI. |
| **Tư duy phê phán & Ra quyết định** | Kỹ năng phân tích sâu sắc để đánh giá thông tin, kết quả từ AI và đưa ra quyết định chiến lược. | Chìa khóa để diễn giải chính xác thông tin chi tiết từ AI cho các quyết định quản trị. |
| **Học tập liên tục & Phát triển chuyên môn** | Cam kết không ngừng học hỏi và cập nhật kiến thức về sự phát triển của công nghệ AI. | Cần thiết để luôn theo kịp các cải tiến công nghệ và quy định mới trong nghề nghiệp. |

---

## 1.5 Triển khai AI trong phòng kế toán

Để triển khai thành công các giải pháp AI vào bộ phận kế toán, tổ chức cần thực hiện theo một lộ trình chiến lược mạch lạc:
- **Đánh giá và lập kế hoạch chiến lược:** Đánh giá các quy trình hiện tại, xác định các lĩnh vực tối ưu để tích hợp AI và thiết lập các mục tiêu rõ ràng.
- **Chọn công cụ AI phù hợp:** Lựa chọn phần mềm và giải pháp AI phù hợp với nhu cầu cụ thể của doanh nghiệp và đánh giá kỹ lưỡng nhà cung cấp.
- **Đào tạo và phát triển kỹ năng:** Cung cấp đào tạo kỹ thuật, bồi dưỡng liên tục và xây dựng văn hóa học tập chủ động cho nhân viên.
- **Tích hợp theo từng giai đoạn:** Triển khai AI theo giai đoạn, bắt đầu với các nhiệm vụ đơn giản trước khi mở rộng sang các ứng dụng phức tạp hơn.
- **Hợp tác và giao tiếp:** Thúc đẩy sự hợp tác giữa bộ phận kế toán, CNTT và các phòng ban liên quan; duy trì giao tiếp minh bạch.
- **Giám sát và cải tiến liên tục:** Thường xuyên xem xét hiệu quả hoạt động, thu thập phản hồi và cải tiến lặp lại.
- **Quản trị và bảo mật dữ liệu:** Thiết lập chính sách quản trị dữ liệu mạnh mẽ, bảo vệ thông tin tài chính nhạy cảm và tuân thủ quy định pháp luật.

#### Bảng 1.3 – Tóm tắt chiến lược triển khai AI trong phòng kế toán

| Chiến lược | Hành động chính | Mục tiêu chiến lược |
| :--- | :--- | :--- |
| **1. Đánh giá chiến lược và lập kế hoạch** | Đánh giá quy trình hiện tại, xác định lĩnh vực tích hợp AI và thiết lập mục tiêu rõ ràng. | Xác định khu vực tối ưu để áp dụng AI và thiết lập các số liệu thành công. |
| **2. Lựa chọn công cụ AI phù hợp** | Chọn giải pháp AI phù hợp với nhu cầu cụ thể và đánh giá các nhà cung cấp. | Đảm bảo công cụ AI được chọn rất phù hợp và hiệu quả đối với nhu cầu bộ phận. |
| **3. Đào tạo và phát triển kỹ năng** | Cung cấp đào tạo kỹ thuật, bồi dưỡng liên tục và thúc đẩy văn hóa học tập. | Trang bị cho nhân viên những kỹ năng và kiến thức cần thiết để sử dụng AI hiệu quả. |
| **4. Tích hợp theo giai đoạn** | Tích hợp công cụ AI với hệ thống hiện có, triển khai theo từng giai đoạn cụ thể. | Đảm bảo tích hợp suôn sẻ không làm gián đoạn quy trình hiện tại, cho phép điều chỉnh. |
| **5. Hợp tác và giao tiếp** | Thúc đẩy sự hợp tác liên ngành và duy trì giao tiếp minh bạch giữa các bộ phận. | Đảm bảo tất cả các bên liên quan được liên kết và thông báo đầy đủ về tích hợp AI. |
| **6. Giám sát và cải tiến liên tục** | Thường xuyên xem xét hiệu suất, thu thập phản hồi và cải tiến lặp lại. | Tối ưu hóa việc sử dụng AI dựa trên hiệu suất thực tế và thích ứng với nhu cầu mới. |
| **7. Quản trị dữ liệu và bảo mật** | Thực hiện chính sách quản trị dữ liệu mạnh mẽ và biện pháp bảo mật cao cấp. | Bảo vệ dữ liệu tài chính nhạy cảm và đảm bảo tuân thủ quy định bảo vệ dữ liệu. |

---

## 1.6 Tóm tắt Chương 1

Sự ra đời của Trí tuệ nhân tạo sáng tạo (GAI) đang tái định hình toàn diện ngành kế toán. Từ tự động hóa các phép tính phức tạp đến cung cấp phân tích dự đoán chuyên sâu, AI giúp gia tăng hiệu quả, độ chính xác và cung cấp giá trị chiến lược cho doanh nghiệp. Kế toán viên trong kỷ nguyên mới cần chủ động trang bị tư duy dữ liệu, tư duy phê phán và duy trì việc học tập liên tục để tận dụng tối đa những cơ hội mà AI mang lại.

---

## 1.7 Câu hỏi ôn tập Chương 1 (Hỏi & Đáp)

1. **AI đang tự động hóa các phép tính kế toán phức tạp một cách hiệu quả và chính xác như thế nào?**  
   - *Trả lời:* Các thuật toán AI xử lý dữ liệu tài chính lớn trong nhiều kịch bản (thuế, khấu hao, dự báo) với độ chính xác cao, loại bỏ lỗi thủ công và thích ứng tự động với luật thuế mới.
2. **Ý nghĩa đạo đức và bảo mật dữ liệu của việc sử dụng AI trong kế toán là gì?**  
   - *Trả lời:* Tổ chức cần áp dụng các chính sách quản trị dữ liệu nghiêm ngặt, tuân thủ các quy định bảo mật (GDPR, CCPA), minh bạch hóa quy trình ra quyết định của thuật toán và loại bỏ thiên vị dữ liệu.
3. **Các kỹ năng quan trọng nhất mà kế toán viên cần phát triển trong môi trường AI là gì?**  
   - *Trả lời:* Hiểu biết về dữ liệu (Data Literacy), tư duy phản biện (Critical Thinking) để kiểm chứng đề xuất từ AI, và tư duy không ngừng học tập, cập nhật kiến thức công nghệ.

<br>
<hr>
<br>

# CHƯƠNG 12: TÍNH NĂNG CỬA HÀNG GPT TRONG CHATGPT (THE GPT STORE FEATURE IN CHATGPT)

> *"Mọi người ghét tìm kiếm."*  
> – **Sam Altman**

Giới thiệu các mô hình máy biến áp tạo sinh (GPTs - Generative Pre-trained Transformers) tùy chỉnh và dễ tiếp cận trong ChatGPT đã cách mạng hóa lĩnh vực trí tuệ nhân tạo đàm thoại. Các GPT tùy chỉnh này đã thay thế cơ chế plugin trước đây của GPT-4, nâng cao khả năng tương tác, tính chuyên môn hóa và tự động hóa các tác vụ phức tạp theo ngữ cảnh cụ thể của từng chuyên ngành, đặc biệt là trong tài chính và kế toán.

Cửa hàng GPT (GPT Store), có sẵn cho người dùng ChatGPT, tạo điều kiện khám phá và sử dụng hàng ngàn giải pháp AI tùy chỉnh được chia sẻ bởi cộng đồng toàn cầu và các chuyên gia, cung cấp một hệ sinh thái vô cùng phong phú cho công việc kế toán nghiệp vụ.

---

## 12.1 Những đổi mới của GPT trong ChatGPT

- **Khả năng tùy biến chuyên sâu (Deep Customization):** Người dùng có thể cung cấp dữ liệu riêng, tệp hướng dẫn nghiệp vụ và quy trình cụ thể để tạo ra một GPT am hiểu chính xác nghiệp vụ kế toán của doanh nghiệp.
- **Tích hợp hành động và API (Actions & APIs):** Các GPT tùy chỉnh có thể kết nối với cơ sở dữ liệu bên ngoài, hệ thống kế toán đám mây hoặc phần mềm CRM thông qua API để thực hiện các tác vụ tự động.
- **Hỗ trợ đa phương tiện nâng cao:** Khả năng xử lý tệp PDF tài chính, biểu đồ trang tính (Excel/CSV), hình ảnh và dữ liệu văn bản chỉ trong một phiên làm việc hợp nhất.

---

## 12.2 Những thách thức trong việc áp dụng GPT tùy chỉnh

- **Bảo mật và Quyền riêng tư dữ liệu:** Khi tải lên các tệp dữ liệu tài chính nhạy cảm hoặc tài liệu nội bộ để huấn luyện GPT, tổ chức phải kiểm soát chặt chẽ quyền sở hữu dữ liệu và đảm bảo không bị rò rỉ ra ngoài.
- **Quản lý chất lượng và Kiểm chứng thông tin:** Mặc dù GPT rất thông minh, hiện tượng "ảo giác" (hallucination) vẫn có thể xảy ra. Kế toán viên phải luôn áp dụng tư duy chuyên môn để thẩm định lại các con số và tham chiếu luật định.
- **Đào tạo và Thích ứng của nhân viên:** Nhu cầu đào tạo nhân sự sử dụng thành thạo các prompt chuyên nghiệp và quy trình làm việc với GPT tùy chỉnh đòi hỏi sự đầu tư về thời gian và nỗ lực từ ban lãnh đạo.

---

## 12.3 Nghiên cứu điển hình – GPT đang hoạt động (Case Studies)

### 1. Nâng cao dịch vụ khách hàng trong Tài chính – Kế toán
- **Ứng dụng:** Các công ty dịch vụ kế toán triển khai GPT tùy chỉnh đóng vai trò "Trợ lý hỗ trợ khách hàng 24/7", tự động giải đáp các thắc mắc về quy trình hóa đơn, thời hạn nộp báo cáo thuế và các thủ tục chuẩn mực kế toán cơ bản.
- **Kết quả:** Tiết kiệm thời gian cho tư vấn viên chuyên nghiệp, tăng tốc độ phản hồi khách hàng lên đáng kể.

### 2. Dạy kèm và Đào tạo nội bộ (Educational Tutoring)
- **Ứng dụng:** Xây dựng GPT gia sư cho các chuyên viên kế toán thực tập hoặc chuẩn bị thi chứng chỉ nghề nghiệp (CPA, ACCA), cung cấp giải thích chi tiết các chuẩn mực kế toán phức tạp.
- **Kết quả:** Tạo ra trải nghiệm học tập được cá nhân hóa và thích ứng với tốc độ tiếp thu của từng học viên.

### 3. Tự động hóa văn bản pháp luật và Hợp đồng tài chính
- **Ứng dụng:** Sử dụng GPT tùy chỉnh để tóm tắt các điều khoản hợp đồng kinh tế, rà soát các điểm rủi ro tài chính và kiểm tra sự phù hợp với quy định pháp luật.
- **Kết quả:** Giảm thời gian rà soát hồ sơ từ vài giờ xuống còn vài phút với độ chính xác cao.

### 4. Dịch thuật thời gian thực cho Báo cáo tài chính đa ngôn ngữ
- **Ứng dụng:** Hỗ trợ dịch thuật chuyên ngành chính xác giữa tiếng Anh, tiếng Việt và các ngôn ngữ khác cho báo cáo tài chính quốc tế (IFRS).

---

## 12.4 Xu hướng và Dự đoán trong tương lai về công nghệ GPT tùy chỉnh

#### Bảng 12.1 – Xu hướng và dự đoán trong tương lai về công nghệ GPT tùy chỉnh

| Xu hướng | Mô tả chi tiết | Tác động đối với doanh nghiệp |
| :--- | :--- | :--- |
| **Tích hợp rộng rãi trong dịch vụ khách hàng** | GPT được sử dụng để xử lý các câu hỏi phức tạp về kế toán và tư vấn nghiệp vụ một cách tự chủ. | Cải thiện hiệu quả, cá nhân hóa tương tác khách hàng và giảm chi phí vận hành thường xuyên. |
| **Trợ lý ảo thông minh nâng cao** | GPT được giao quyền quản lý các quy trình làm việc toàn diện với mức độ tự chủ lớn hơn (Agentic workflows). | Tăng năng suất vượt trội, hỗ trợ chuyên môn sâu cho chuyên gia kế toán và tài chính. |
| **Mở rộng sáng tạo nội dung đa phương tiện** | Khả năng tạo ra các báo cáo tổng hợp, biểu đồ trực quan hóa và bài diễn giải tài chính phong phú. | Nâng cao chất lượng báo cáo quản trị và giao tiếp tài chính trong doanh nghiệp. |
| **Quy trình đào tạo và tùy chỉnh hợp lý hóa** | Giao diện không cần viết mã (No-code) giúp việc tạo và tinh chỉnh các GPT chuyên biệt trở nên dễ dàng hơn bao giờ hết. | Giảm rào cản kỹ thuật, cho phép kế toán viên không rành lập trình tự xây dựng công cụ AI cho riêng mình. |
| **Trải nghiệm học tập thích ứng cá nhân hóa** | Giáo dục và bồi dưỡng nghiệp vụ kế toán được cá nhân hóa sâu sắc bằng các trợ lý học tập AI. | Nâng cao năng lực nhân sự liên tục, đáp ứng yêu cầu thay đổi nhanh chóng của thị trường. |

---

## 12.5 Chuẩn bị cho một tương lai được định hướng bởi GPT

Để thích ứng và làm chủ công nghệ GPT tùy chỉnh, cá nhân và tổ chức cần tuân thủ các bước hành động chiến lược:

#### Bảng 12.2 – Chuẩn bị cho tương lai được định hướng bởi GPT

| Chiến lược | Mục hành động chính | Mục tiêu chiến lược |
| :--- | :--- | :--- |
| **1. Cập nhật thông tin về phát triển AI** | Đăng ký các bản tin AI, ấn phẩm chuyên ngành và tham dự các hội thảo, hội nghị về AI trong Kế toán. | Luôn nắm bắt xu hướng công nghệ mới nhất để định hướng chiến lược dài hạn cho đơn vị. |
| **2. Đầu tư vào giáo dục & nâng cao kỹ năng** | Tham gia các khóa học chuyên sâu về ứng dụng AI, Prompt Engineering và quản trị giải pháp GPT. | Nâng cao năng lực chuyên môn để ứng dụng hiệu quả công cụ AI vào công việc hàng ngày. |
| **3. Cân nhắc đạo đức & tuân thủ quy định** | Xây dựng bộ quy tắc sử dụng AI có trách nhiệm, bảo mật dữ liệu khách hàng và tuân thủ pháp luật. | Đảm bảo sử dụng AI an toàn, minh bạch, duy trì niềm tin nghề nghiệp với các bên liên quan. |
| **4. Lập kế hoạch tích hợp chiến lược** | Xác định rõ các nghiệp vụ kế toán có thể tối ưu bằng GPT và lập lộ trình triển khai rõ ràng. | Hợp lý hóa việc áp dụng AI, tối đa hóa giá trị mang lại trên quy mô toàn bộ tổ chức. |
| **5. Nuôi dưỡng văn hóa đổi mới** | Khuyến khích sự thử nghiệm, đóng góp sáng kiến và chia sẻ công cụ AI tốt trong nội bộ nhóm. | Thúc đẩy môi trường làm việc chủ động, năng động và kiên cường trước sự thay đổi của công nghệ. |

---

## 12.6 Tóm tắt Chương 12

Cửa hàng GPT (GPT Store) và công nghệ GPT tùy chỉnh trong ChatGPT đánh dấu một mốc phát triển nhảy vọt trong công nghệ trợ lý ảo nghiệp vụ. Đối với ngành kế toán – tài chính, khả năng cá nhân hóa chuyên sâu giúp kế toán viên tự xây dựng các "trợ lý nghiệp vụ riêng" cho từng tác vụ như rà soát chuẩn mực, tóm tắt hợp đồng hay hỗ trợ khách hàng. Mặc dù cần chú trọng quản trị bảo mật dữ liệu và kiểm chứng độ chính xác, tiềm năng đổi mới mà GPT mang lại là vô cùng to lớn.

---

## 12.7 Câu hỏi ôn tập Chương 12 (Hỏi & Đáp)

1. **Cửa hàng GPT (GPT Store) mang lại lợi ích đặc biệt gì cho các kế toán viên so với việc chỉ sử dụng mô hình ChatGPT chung?**  
   - *Trả lời:* Cho phép kế toán viên tìm kiếm hoặc tự xây dựng các trợ lý AI được cá nhân hóa sâu sắc với dữ liệu, quy trình và chuẩn mực riêng của doanh nghiệp, giúp tăng độ chính xác và chuyên môn hóa cao cho công việc.
2. **Những rủi ro bảo mật nào cần quan tâm khi sử dụng GPT tùy chỉnh với dữ liệu tài chính doanh nghiệp?**  
   - *Trả lời:* Rủi ro tải lên dữ liệu tài chính bảo mật hoặc thông tin nhận dạng cá nhân (PII) mà không có chính sách kiểm soát quyền sở hữu dữ liệu phù hợp; cần đảm bảo tắt chế độ chia sẻ dữ liệu huấn luyện và tuân thủ tiêu chuẩn bảo mật.
3. **Làm thế nào để doanh nghiệp xây dựng một văn hóa ứng dụng GPT an toàn và hiệu quả trong phòng kế toán?**  
   - *Trả lời:* Ban hành hướng dẫn sử dụng AI minh bạch, tổ chức đào tạo prompt chuyên nghiệp, chia sẻ các mẫu GPT hiệu quả nội bộ và thực hiện kiểm tra thường xuyên tính chính xác của các kết quả đầu ra.

#### ** 🎬 Video **

<iframe src="video/Day12/index.html?v=1785919941" style="width: 100%; aspect-ratio: 16/9; max-height: 75vh; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>

#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slideAIAcc/Slide_AIAcc_Day12.pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day12.pdf#view=FitH" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day12.pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

#### ** 📝 Bài tập Trắc nghiệm **

<iframe src="quizzes/Day12/index.html?v=1785919941" style="width: 100%; min-height: 700px; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>


#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Sự khác biệt của Generative AI (Độ khó: Dễ)**
Generative AI (như ChatGPT - Chương 12) khác biệt như thế nào so với AI truyền thống (Predictive/Analytical AI) trong khả năng xử lý nghiệp vụ?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Predictive AI: Chuyên phân tích dữ liệu lịch sử để dự báo xu hướng (Dự báo phá sản, dự báo giá).
- Generative AI: Có khả năng SÁNG TẠO nội dung mới (viết email, dịch văn bản, sinh mã code, tạo báo cáo phân tích tài chính) dựa trên dữ liệu đầu vào.
</details>
<br>

**Bài tập 2: Hiện tượng "Hallucinations" (Ảo giác AI) (Độ khó: Trung bình)**
Theo Chương 12, khi sử dụng ChatGPT để phân tích báo cáo tài chính, hiện tượng "Hallucinations" là gì? Cho ví dụ về hậu quả của nó.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Hallucination (Ảo giác) là việc AI tự tin đưa ra câu trả lời hoàn toàn sai sự thật và tự bịa đặt thông tin.
- Ví dụ hậu quả: ChatGPT có thể tự bịa ra một chuẩn mực IFRS không tồn tại hoặc trích dẫn các số liệu tài chính giả mạo để lý giải cho biến động lợi nhuận, khiến kế toán viên lập BCTC sai lệch pháp lý.
</details>
<br>

**Bài tập 3: Cấu trúc Prompt Kế toán hiệu quả (Độ khó: Khó)**
Dựa trên kiến thức về Web-Enhanced ChatGPT, hãy viết một "Prompt" (Câu lệnh) hoàn chỉnh theo cấu trúc 4 phần (Vai trò, Bối cảnh, Nhiệm vụ, Định dạng) để yêu cầu AI tóm tắt tình hình tài chính.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- **Vai trò:** Đóng vai là Giám đốc Tài chính (CFO) chuyên nghiệp.
- **Bối cảnh:** Đối mặt với báo cáo Q3 giảm lợi nhuận do chi phí nguyên vật liệu tăng.
- **Nhiệm vụ:** Tóm tắt báo cáo tài chính đính kèm, tìm ra 3 nguyên nhân cốt lõi làm tăng chi phí.
- **Định dạng:** Trình bày bằng gạch đầu dòng ngắn gọn, không quá 300 chữ, dùng tông giọng trang trọng.
</details>
<br>
<!-- tabs:end -->
