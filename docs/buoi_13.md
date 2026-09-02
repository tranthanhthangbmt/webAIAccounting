# Buổi 13: Kỹ thuật Viết Prompt & Chiến lược Phân tích Dữ liệu Tài chính (SPARKS Framework)

<!-- tabs:start -->

#### ** 📚 Thuật ngữ & Khái niệm **

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Kính viễn vọng tiên đoán (Telescope Metaphor)</b></summary>
<br>

Hình ảnh ví von sự dịch chuyển của nghề kế toán. Kế toán không còn dùng "Gương chiếu hậu" để ghi chép dĩ vãng, mà dùng AI như "Kính viễn vọng" để soi chiếu, dự báo tương lai và cảnh báo rủi ro cho doanh nghiệp.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Nguyên lý "Rác đầu vào = Rác đầu ra" (Garbage in, Garbage out)</b></summary>
<br>

Nền tảng của Chiến lược dữ liệu. Dù AI có siêu việt đến đâu, nếu dữ liệu đầu vào (hóa đơn, chứng từ) bị sai lệch hoặc giả mạo, kết quả phân tích phun ra cũng chỉ là rác rưởi.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Phân tích Mô tả (Descriptive Analytics)</b></summary>
<br>

Trụ cột 1. Trả lời câu hỏi "Chuyện gì đã xảy ra?" (Ví dụ: Bảng tỷ số báo doanh thu tăng, lợi nhuận giảm). Nhược điểm là nó không cho biết TẠI SAO điều đó xảy ra.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Phân tích Chẩn đoán (Diagnostic Analytics)</b></summary>
<br>

Trụ cột 2. Trả lời câu hỏi "Tại sao điều đó xảy ra?" thông qua việc đào sâu vào dữ liệu (như xem lại băng quay chậm) để tìm nguyên nhân gốc rễ (ví dụ: đứt gãy chuỗi cung ứng làm tăng chi phí).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Phân tích Dự báo (Predictive Analytics)</b></summary>
<br>

Trụ cột 3. Trả lời câu hỏi "Chuyện gì sẽ xảy ra tiếp theo?". Dựa trên mô hình toán học hồi quy để dự báo tương lai (doanh thu, dòng tiền) bằng dữ liệu khoa học, không phải bằng tâm linh hay cảm tính.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Phân tích Đề xuất (Prescriptive Analytics)</b></summary>
<br>

Trụ cột 4 - Đỉnh cao nhất. Trả lời câu hỏi "Ta NÊN làm gì?". Hệ thống AI tự động tính toán và đề xuất bản đồ chiến lược tối ưu nhất (ví dụ: nên sản xuất bao nhiêu xe màu xanh/đỏ để tối đa lợi nhuận) cho Ban Giám đốc phê duyệt.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Kỹ thuật viết Prompt (Prompt Engineering)</b></summary>
<br>

Nghệ thuật và khoa học thiết kế câu lệnh để "sai bảo" và giao tiếp với AI. Nếu không có kỹ năng này, AI sẽ đoán mò và đưa ra kết quả vô dụng.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Chỉ định vai trò (Role-based Prompting)</b></summary>
<br>

Nguyên tắc vàng số 1. Thay vì ra lệnh chung chung, hãy yêu cầu AI "Đóng vai một Kế toán trưởng 15 năm kinh nghiệm về IFRS". Lập tức AI sẽ thay đổi giọng văn, độ sâu kỹ thuật và tính pháp lý cho hợp với vai diễn.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Cung cấp bối cảnh (Context Structuring)</b></summary>
<br>

Nguyên tắc vàng số 2. Phải nói rõ mục tiêu, loại hình công ty và định dạng dữ liệu rõ ràng (Bảng/Gạch đầu dòng). Ném một bãi chữ lộn xộn sẽ làm AI bị "tẩu hỏa nhập ma".

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Tư duy theo bước (Chain-of-Thought)</b></summary>
<br>

Nguyên tắc vàng số 3. Thêm thần chú "Hãy suy nghĩ từng bước một (step-by-step)". Kỹ thuật này khóa chặt logic của AI, ngăn cản nó nhảy cóc đoán mò kết quả, giúp giảm thiểu sai sót đáng kể trong các bài toán thuế lắt léo.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Hạn chế Toán học của LLM</b></summary>
<br>

Sai lầm chết người. LLM (như ChatGPT) bản chất là mô hình xử lý ngôn ngữ, rất giỏi văn nhưng lại kém toán. Bắt nó cộng trừ nhân chia số lớn rất dễ sai, kế toán viên luôn phải dùng máy tính kiểm tra lại.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Khung tư duy SPARKS</b></summary>
<br>

Quy trình làm việc 6 bước thiết kế riêng cho Kế toán viên để xử lý hàng triệu dòng dữ liệu mà không bị hoảng loạn.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">S - State the Question (Xác định câu hỏi)</b></summary>
<br>

Bước 1. Bắt đầu bằng một câu hỏi kinh doanh cốt lõi (VD: "Vì sao chi phí Quý 4 tăng?").

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">P - Partition (Cắt lớp dữ liệu)</b></summary>
<br>

Bước 2. Rút trích đúng các cột dữ liệu cần thiết để giải quyết câu hỏi, vứt bỏ râu ria thừa thãi.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">A - Analyze (Phân tích)</b></summary>
<br>

Bước 3. Áp dụng các thuật toán hoặc công cụ để phân tích mớ dữ liệu vừa cắt.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">R - Refine (Tinh chỉnh)</b></summary>
<br>

Bước 4. Đi tìm và xử lý các Ngoại lệ (Outliers) vô lý. (Đôi khi quy mô mẫu nhỏ làm bóp méo điểm trung bình, hoặc một lỗi gõ dư số 0 của thư ký làm nổ tung cả mô hình).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">K - Communicate (Giao tiếp/Trực quan hóa)</b></summary>
<br>

Bước 5. Vẽ Dashboard, biểu đồ trực quan để trình bày kết quả "kể chuyện dữ liệu" cho Sếp.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">S - Stop (Dừng lại)</b></summary>
<br>

Bước 6. Dừng lại, suy ngẫm và phản biện xem báo cáo này đã thực sự trả lời đúng câu hỏi Sếp giao ở Bước 1 hay chưa.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Pháo đài dữ liệu (Data Fortress)</b></summary>
<br>

Giải pháp an ninh mạng bắt buộc (tuân thủ GDPR). Cô lập dữ liệu tài chính nội bộ, xây tường lửa để chống lại thảm họa rò rỉ bảo mật như vụ hack Equifax.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Hiện tượng Hộp đen (Black Box)</b></summary>
<br>

Nỗi sợ hãi khi giao quyền cho AI (VD: Giao dịch cao tần). Máy móc tự đưa ra quyết định chốt lệnh nhưng không một con người nào hiểu được logic bên trong thuật toán là gì, có nguy cơ gây sụp đổ thị trường (Flash Crash).

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Hàm mục tiêu vô cảm (Objective Function)</b></summary>
<br>

Điểm giao thoa giữa Công nghệ và Triết học. AI không có lương tâm. Nếu hàm mục tiêu là "tối đa lợi nhuận", nó sẵn sàng chà đạp đạo đức (tài trợ phá hoại môi trường) để đạt được mục tiêu đó, vì lỗi nằm ở người lập trình.

</details>

<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Trực giác đạo đức & Thấu cảm triết học</b></summary>
<br>

Đặc quyền vô giá và vĩnh cửu của con người. Sự khác biệt lớn nhất giữa một Chuyên gia tài chính bằng xương bằng thịt và một cỗ máy AI siêu việt. Máy tính đề xuất, nhưng con người phải nắm giữ "chiếc phanh khẩn cấp" luân lý.

</details>



#### ** 🇬🇧 Tiếng Anh **

### 📄 Tài liệu PDF 1: Chương 6: Turbocharging Financial Analysis (Scott Dell)

<object data="textbook/Buoi_13A_Chương 6 (Turbocharging Financial Analysis).pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_13A_Chương 6 (Turbocharging Financial Analysis).pdf#view=FitH" target="_blank">Nhấn vào đây để tải tài liệu PDF 1</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_13A_Chương 6 (Turbocharging Financial Analysis).pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 1 (PDF)</a></p>

---

### 📄 Tài liệu PDF 2: Chương 3 & 4: Planning Data Strategies & SPARKS Framework

<object data="textbook/Buoi_13B_Chương 3 & 4 (Planning Data Strategies).pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/Buoi_13B_Chương 3 & 4 (Planning Data Strategies).pdf#view=FitH" target="_blank">Nhấn vào đây để tải tài liệu PDF 2</a>.</p>
</object>
<p style="text-align: right;"><a href="textbook/Buoi_13B_Chương 3 & 4 (Planning Data Strategies).pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu 2 (PDF)</a></p>


#### ** 🇻🇳 Tiếng Việt **

# PHẦN I: TĂNG CƯỜNG PHÂN TÍCH VÀ DỰ ĐOÁN TÀI CHÍNH VỚI AI (SCOTT DELL - CHƯƠNG 6)

> *"Phân tích tài chính là một quá trình làm sạch, điều chỉnh và chuyển đổi dữ liệu thành những hiểu biết sâu sắc có thể hành động. Sự ra đời của AI đã đưa quá trình này từ một tấm gương chiếu hậu trở thành một chiếc kính viễn vọng tiên đoán mạnh mẽ."*  
> – **Wayne R. Landsman**, Nhà khoa học trưởng về quyết định tại Moody’s Analytics

Phân tích tài chính là công cụ quan trọng đối với các doanh nghiệp và nhà đầu tư trong nền kinh tế năng động ngày nay, nơi được đặc trưng bởi những thay đổi nhanh chóng, sự không chắc chắn và sự kết nối toàn cầu phức tạp. Khả năng phân tích dữ liệu tài chính chính xác và dự đoán xu hướng tương lai tốt hơn không chỉ là lợi thế chiến lược mà còn là điều kiện cốt lõi để tồn tại và phát triển.

---

## 1.1 Vai trò biến đổi của AI trong Phân tích tài chính

Phân tích và dự báo tài chính đóng vai trò then chốt trong việc ra quyết định chiến lược kinh doanh và quản trị rủi ro:
- **Chuyển từ phân tích tĩnh sang động:** Trí tuệ nhân tạo (AI) giúp quá trình phân tích chuyển từ việc chỉ kiểm tra dữ liệu lịch sử ("gương chiếu hậu") sang việc dự báo thời gian thực và tự động nhận diện mô hình rủi ro tiềm ẩn ("kính viễn vọng tiên đoán").
- **Tối ưu hóa nguồn lực và cơ hội:** Bằng cách giải thích chính xác các bộ dữ liệu tài chính đa chiều, doanh nghiệp có thể xác định sớm các cơ hội sinh lời, phân bổ vốn hiệu quả hơn và nâng cao tính minh bạch cho nhà đầu tư.
- **Tăng cường sự linh hoạt:** Trong môi trường kinh tế biến động, hệ thống dự báo tài chính hỗ trợ AI giúp các tổ chức điều chỉnh quy trình kinh doanh kịp thời nhằm duy trì lợi thế cạnh tranh.

---

## 1.2 Các công cụ và ứng dụng AI trong Dự báo Tài chính

- **Phân tích xu hướng & Mô hình dự đoán:** Các thuật toán học máy (Machine Learning) kiểm tra dữ liệu dòng tiền, chu kỳ thu chi và mô hình vĩ mô để dự báo doanh thu và chi phí với độ chính xác cao vượt trội so với bảng tính truyền thống.
- **Phân tích tình cảm (Sentiment Analysis):** AI phân tích thông tin từ báo cáo thường niên, tin tức thị trường và đánh giá chuyên gia để nhận định xu hướng tâm lý thị trường, hỗ trợ đưa ra quyết định đầu tư phù hợp.
- **Trực quan hóa dữ liệu tự động:** Tự động tạo bảng điều khiển (Dashboards) tương tác, chuyển các bảng số liệu kế toán phức tạp thành các biểu đồ rõ ràng, hỗ trợ ban lãnh đạo ra quyết định tức thì.

#### Bảng 1.1 – Tóm tắt các ứng dụng AI trong Phân tích và Dự báo tài chính

| Lĩnh vực phân tích | Phương pháp truyền thống | Đột phá với Trí tuệ nhân tạo (AI) | Lợi ích đối với Kế toán viên |
| :--- | :--- | :--- | :--- |
| **Dự báo dòng tiền** | Dựa trên trung bình cộng lịch sử và giả định thủ công. | Sử dụng mô hình học máy phân tích dữ liệu đa biến thời gian thực. | Tăng độ chính xác dự báo, nhận diện sớm thâm hụt vốn. |
| **Phân tích rủi ro tín dụng** | Đánh giá qua chỉ số tĩnh và báo cáo tài chính quý/năm. | Phân tích liên tục hành vi thanh toán và tín hiệu thị trường. | Giảm tỷ lệ nợ xấu, tự động cảnh báo rủi ro khách hàng. |
| **Phân tích chi phí & Ngân sách** | Đối chiếu phương sai thủ công vào cuối kỳ kế toán. | Tự động phát hiện chi phí bất thường ngay tại thời điểm phát sinh. | Kiểm soát ngân sách chặt chẽ, tối ưu hóa chi phí vận hành. |

---

## 1.3 Nghiên cứu điển hình (Case Studies – Chương 6)

### 1. Phân tích tài chính trong ngành Bán lẻ (Retail Financial Analytics)
- **Bối cảnh:** Một chuỗi bán lẻ lớn đối mặt với thách thức trong việc lập dự báo nhu cầu hàng tồn kho và quản lý chi phí lưu kho theo mùa vụ.
- **Giải pháp AI:** Tích hợp công cụ phân tích dự đoán hỗ trợ AI để tra cứu mô hình bán hàng lịch sử, thời tiết và xu hướng tiêu dùng.
- **Kết quả:** Giảm 25% chi phí lưu kho và tối ưu hóa dòng tiền hoạt động nhờ dự báo chính xác nhu cầu vốn cho từng quý.

### 2. Dự báo thị trường Bất động sản và Tài sản dài hạn
- **Bối cảnh:** Một doanh nghiệp quản lý quỹ tài sản cần định giá và dự báo lợi nhuận đầu tư bất động sản trong giai đoạn biến động lãi suất.
- **Giải pháp AI:** Sử dụng mô hình hồi quy đa biến AI để theo dõi lãi suất ngân hàng, giá trị bất động sản khu vực và dòng tiền thuê.
- **Kết quả:** Giúp ban lãnh đạo ra quyết định giải ngân và thoái vốn với độ an toàn và tỷ suất sinh lời vượt kỳ vọng.

<br>
<hr>
<br>

# PHẦN II: KỸ THUẬT PROMPT TRONG KẾ TOÁN (SCOTT DELL - CHƯƠNG 13)

Kỹ thuật Prompt (Prompt Engineering) là nghệ thuật và khoa học thiết kế các câu lệnh đầu vào rõ ràng, có cấu trúc để hướng dẫn Mô hình ngôn ngữ lớn (LLMs như ChatGPT, Claude, Gemini) tạo ra kết quả đầu ra chính xác, chuyên nghiệp và có giá trị sử dụng cao nhất trong nghiệp vụ kế toán – tài chính.

---

## 2.1 Nguyên tắc xây dựng Prompt hiệu quả cho Kế toán viên

### 1. Chỉ định vai trò chuyên môn (Role-based Prompting)
- Luôn gán cho AI một vai trò cụ thể trong ngành nghề (ví dụ: *"Hãy đóng vai một Kế toán trưởng có 15 năm kinh nghiệm về chuẩn mực IFRS và VAS..."*).
- Giúp LLM thiết lập giọng văn, độ sâu kỹ thuật và góc nhìn chuẩn xác với yêu cầu nghề nghiệp.

### 2. Cung cấp bối cảnh và Dữ liệu rõ ràng (Context & Clarity)
- Cung cấp bối cảnh doanh nghiệp, loại hình kinh doanh và mục tiêu tài chính cụ thể.
- Định dạng dữ liệu đầu vào theo bảng hoặc danh sách mạch lạc để AI dễ dàng xử lý.

### 3. Phân chia tác vụ theo bước (Chain-of-Thought / Step-by-Step)
- Với các bài toán kế toán phức tạp (như phân bổ chi phí, tính thuế TNDN hoãn lại), hãy yêu cầu AI *re-check* từng bước tính toán trước khi đưa ra kết luận cuối cùng.

---

## 2.2 Các mẫu Prompt thực chiến trong Nghiệp vụ Kế toán

#### Bảng 2.1 – Bộ Prompt thực chiến chuyên nghiệp cho Kế toán viên

| Mục đích nghiệp vụ | Cấu trúc Prompt mẫu được khuyến nghị | Kết quả mong đợi từ LLM |
| :--- | :--- | :--- |
| **Phân tích Báo cáo Tài chính** | *"Đóng vai một chuyên gia phân tích tài chính. Hãy phân tích bảng số liệu sau của Công ty A, tính toán các chỉ số thanh khoản (Hệ số thanh toán hiện hành, nhanh) và đưa ra nhận xét chiến lược ngắn gọn trong 3 gạch đầu dòng."* | Bảng tính chỉ số tài chính kèm nhận xét đánh giá tình hình thanh khoản rõ ràng. |
| **Rà soát tuân thủ Hóa đơn & Thuế** | *"Tôi có danh sách các giao dịch mua hàng dưới đây. Hãy lập bảng đối chiếu để xác định các khoản mục tiềm ẩn rủi ro về thuế giá trị gia tăng (GTGT) theo chuẩn mực thuế hiện hành và đề xuất giải thích."* | Bảng phát hiện điểm rủi ro, trích dẫn lý do và biện pháp rà soát hồ sơ thanh toán. |
| **Soạn thảo Thư tư vấn Khách hàng** | *"Hãy soạn một bức thư chuyên nghiệp bằng tiếng Việt, gửi Ban Giám đốc Khách hàng B để tóm tắt các phát hiện kiểm toán nội bộ về quy trình kiểm soát chi phí bán hàng trong quý 3."* | Thư tư vấn chuyên nghiệp, đúng chuẩn mực văn phong công sở và mạch lạc. |

---

## 2.3 Những sai lầm cần tránh khi sử dụng Prompt
- **Prompt quá chung chung:** Nhập các câu hỏi mơ hồ như *"Làm thế nào để phân tích chi phí?"* sẽ tạo ra câu trả lời chung chung, thiếu thực tế.
- **Không kiểm chứng số liệu tính toán:** LLM có thể nhầm lẫn số học; kế toán viên luôn cần yêu cầu hiển thị công thức và đối chiếu lại số liệu cuối cùng.
- **Vi phạm bảo mật dữ liệu nhạy cảm:** Không đưa thông tin định danh khách hàng (tên thật, mã số thuế bí mật, số tài khoản) vào các nền tảng AI công cộng chưa được mã hóa.

<br>
<hr>
<br>

# PHẦN III: KHỞI ĐỘNG PHÂN TÍCH DỮ LIỆU VỚI KHUNG TƯ DUY SPARKS (RICHARDSON)

Khung tư duy **SPARKS** là một quy trình làm việc chuẩn hóa, có tính hệ thống được thiết kế riêng cho Kế toán viên để triển khai các dự án Phân tích dữ liệu kế toán (Data Analytics in Accounting) một cách khoa học, sâu sắc và thực tiễn.

---

## 3.1 Giải mã Khung tư duy SPARKS

- **S – State the Question (Xác định Câu hỏi):** Bắt đầu từ vấn đề kinh doanh hoặc tài chính cốt lõi. Chúng ta cần giải quyết câu hỏi gì? (Ví dụ: *"Tại sao chi phí mua hàng của nhà cung cấp X lại tăng đột biến trong Quý 4?"*).
- **P – Partition the Data (Phân chia & Thuật gọn Dữ liệu):** Xác định các nguồn dữ liệu cần thiết, tiến hành làm sạch, loại bỏ sai lệch và chọn lọc các biến số liên quan trong Hệ thống thông tin kế toán (AIS/ERP).
- **A – Analyze the Data (Thực hiện Phân tích):** Áp dụng kỹ thuật phân tích phù hợp (Mô tả, Chẩn đoán, Dự đoán hoặc Đề xuất) trên bộ dữ liệu đã được làm sạch.
- **R – Refine the Analysis (Tinh chỉnh & Kiểm định Phân tích):** Rà soát rủi ro phân tích, kiểm tra tính hợp lệ của các giả định tài chính và tinh chỉnh mô hình để đạt độ chính xác cao hơn.
- **K – Communicate the Insights (Truyền đạt Thông tin chi tiết):** Sử dụng các biểu đồ, bảng điều khiển (Dashboards) và báo cáo ngắn gọn để truyền tải phát hiện đến Ban Giám đốc hoặc các bên liên quan.
- **S – Stop and Reflect (Dừng lại & Suy ngẫm):** Đánh giá lại toàn bộ quy trình, xác định xem các thông tin đã trả lời trọn vẹn câu hỏi ban đầu chưa và áp dụng vào chiến lược kinh doanh.

---

## 3.2 Bốn mức độ Phân tích Dữ liệu Kế toán (4 Levels of Analytics)

#### Bảng 3.1 – Phân loại 4 mức độ Phân tích dữ liệu kế toán theo Richardson

| Mức độ phân tích | Câu hỏi cốt lõi | Kỹ thuật & Công cụ kế toán sử dụng | Ví dụ thực tiễn trong Kế toán |
| :--- | :--- | :--- | :--- |
| **1. Phân tích Mô tả (Descriptive)** | *"Chuyện gì đã xảy ra?"* | Bảng tổng hợp (Pivot Tables), Thống kê mô tả (Sum, Mean, Median, Min, Max). | Tính tổng chi phí mua hàng theo từng nhà cung cấp trong năm tài chính. |
| **2. Phân tích Chẩn đoán (Diagnostic)** | *"Tại sao điều đó lại xảy ra?"* | Biểu đồ phân tán (Scatter plots), Phân tích phương sai (ANOVA), Đối chiếu kỳ trước. | Tìm nguyên nhân khiến tỷ lệ hàng lỗi của nhà cung cấp Y tăng cao trong tháng 8. |
| **3. Phân tích Dự đoán (Predictive)** | *"Điều gì có khả năng sẽ xảy ra?"* | Hồi quy tuyến tính (Linear Regression), Học máy, Mô hình chuỗi thời gian. | Dự báo số dư công nợ phải trả (Accounts Payable) trong hai quý tiếp theo. |
| **4. Phân tích Đề xuất (Prescriptive)** | *"Chúng ta nên làm gì?"* | Phân tích giả định (What-If Analysis), Tối ưu hóa mô hình, Đánh giá rủi ro chiến lược. | Đề xuất cơ cấu lại các điều khoản thanh toán để tận dụng chiết khấu thanh toán sớm. |

---

## 3.3 Bài tập Thực hành theo Mô hình SPARKS (SPARKS Practice)

Để làm quen với quy trình SPARKS, kế toán viên được rèn luyện trên bộ dữ liệu thực tế về **Thanh toán Nhà cung cấp (Accounts Payable - AP & Purchasing)** trong Hệ thống Thông tin Kế toán.

#### Bảng 3.2 – Từ điển Dữ liệu Cơ sở dữ liệu Mua hàng & Thanh toán (AP Data Dictionary)

| Nhãn trường dữ liệu | Tên trường hệ thống | Mô tả chi tiết trường dữ liệu |
| :--- | :--- | :--- |
| **Số hóa đơn** | `InvoiceNo` | Số hóa đơn duy nhất được thư ký AP nhập vào hệ thống từ hóa đơn của nhà cung cấp. |
| **Số tiền hóa đơn** | `InvoiceAmount` | Tổng số tiền thanh toán của hóa đơn (đơn vị: Đồng / USD). |
| **Ngày hóa đơn** | `InvoiceDate` | Ngày phát hành trên hóa đơn của nhà cung cấp. |
| **Mã nhà cung cấp** | `VendorID` | Mã định danh duy nhất của nhà cung cấp trong tập tin chính (Master file). |
| **Tên nhà cung cấp** | `VendorName` | Tên đầy đủ của đơn vị bán hàng / cung cấp dịch vụ. |
| **Mã sản phẩm** | `ProductID` | Mã nhận dạng hàng hóa / nguyên vật liệu được mua. |
| **Đơn giá mua** | `UnitCost` | Chi phí mua một đơn vị sản phẩm / hàng hóa. |
| **Chi phí vận chuyển** | `ShippingCost` | Cước phí vận chuyển phát sinh theo đơn hàng. |
| **Quốc gia vận chuyển** | `ShipLocation` | Vị trí quốc gia / khu vực nhận hàng. |
| **Đánh giá chất lượng** | `QualityRating` | Thang điểm đánh giá từ bộ phận nhận hàng (1 = Kém nhất đến 5 = Tuyệt vời). |
| **Điều khoản thanh toán** | `PaymentTerms` | Điều khoản tín dụng thương mại thỏa thuận với nhà cung cấp (ví dụ: `2/10 Net 30`). |
| **Số Đơn đặt hàng** | `PONo` | Số đơn đặt hàng (Purchase Order) tương ứng được lập bởi bộ phận Mua hàng. |

---

### Bài tập 1: Phân tích các giao dịch Hóa đơn Mua hàng bất thường
- **S – Question:** Có xuất hiện các hóa đơn mua hàng với giá trị bất thường (quá lớn hoặc phát sinh ngoài giờ) trong kỳ kế toán không?
- **P – Partition:** Trích xuất trường `InvoiceDate`, `InvoiceAmount`, `VendorName` từ cơ sở dữ liệu.
- **A – Analyze:** Thực hiện phân tích chẩn đoán bằng cách vẽ **Biểu đồ phân tán (Scatter Plot)** với trục X là `InvoiceDate` và trục Y là `InvoiceAmount`.
- **R – Refine:** Kiểm tra các điểm giá trị ngoại lai (Outliers); rà soát xem có sự trùng lặp số hóa đơn hoặc sai sót gõ nhầm số liệu từ thư ký AP hay không.
- **K – Communicate:** Trình bày biểu đồ phân tán kèm danh sách 5 hóa đơn cao bất thường cho Kế toán trưởng rà soát.

---

### Bài tập 2: Phân tích Chất lượng Nhà cung cấp theo Thời gian
- **S – Question:** Nhà cung cấp nào có chỉ số đánh giá chất lượng trung bình (`QualityRating`) thấp nhất và xu hướng chất lượng của họ biến động thế nào?
- **P – Partition:** Lọc dữ liệu theo `VendorName`, `QualityRating`, `ShipDate`.
- **A – Analyze:** Tính hàm trung bình (`AVERAGE`) chỉ số `QualityRating` của từng nhà cung cấp và lập bảng xếp hạng.
- **R – Refine:** Đánh giá độ tin cậy của mẫu dữ liệu (nhà cung cấp chỉ cung cấp 1 đơn hàng so với nhà cung cấp cung cấp 50 đơn hàng).
- **K – Communicate:** Tạo biểu đồ cột thể hiện điểm chất lượng của Top 5 nhà cung cấp tốt nhất và 3 nhà cung cấp cần khuyến nghị thay thế.

---

### Bài tập 3: Phân tích Quy mô Mua hàng theo Quốc gia / Khu vực
- **S – Question:** Tổng kim ngạch mua hàng và số lượng đơn đặt hàng được phân bổ như thế nào giữa các quốc gia nhà cung cấp?
- **P – Partition:** Sử dụng bảng tổng hợp `ShipLocation`, `InvoiceAmount`, `PONo`.
- **A – Analyze:** Dùng **Pivot Table** kéo trường `ShipLocation` vào hàng (Rows), tính tổng `SUM(InvoiceAmount)` và đếm số lượng `COUNT(PONo)`.
- **R – Refine:** Rà soát ảnh hưởng của tỷ giá hối đoái đối với các nhà cung cấp nước ngoài.
- **K – Communicate:** Xây dựng biểu đồ tròn (Pie Chart) thể hiện tỷ trọng chi phí mua hàng toàn cầu.

<br>
<hr>
<br>

# PHẦN IV: TÓM TẮT VÀ CÂU HỎI ÔN TẬP BÀI HỌC

## 4.1 Tóm tắt tổng quan Buổi 13
Buổi 13 là sự giao thoa hoàn hảo giữa công nghệ hiện đại (**Kỹ thuật Prompt & AI trong Phân tích tài chính**) và phương pháp luận chuyên sâu (**Khung tư duy SPARKS**):
1. **AI và Dự báo Tài chính:** Trí tuệ nhân tạo chuyển đổi vai trò kế toán từ "ghi chép lịch sử" sang "dự báo chiến lược thời gian thực", nâng cao độ chính xác và khả năng quản trị rủi ro.
2. **Kỹ thuật Prompt:** Làm chủ Prompt Engineering (chỉ định vai trò, cung cấp bối cảnh, tư duy theo bước) là kỹ năng bắt buộc để khai thác hiệu quả các LLM trong nghiệp vụ tài chính – kế toán.
3. **Khung tư duy SPARKS:** Là kim chỉ nam giúp kế toán viên triển khai các dự án phân tích dữ liệu từ bước đặt câu hỏi (`State`), xử lý dữ liệu (`Partition`, `Analyze`), kiểm chứng rủi ro (`Refine`) đến truyền đạt báo cáo quản trị (`Communicate`, `Stop & Reflect`).

---

## 4.2 Câu hỏi ôn tập và Thảo luận nghiệp vụ (Hỏi & Đáp)

1. **Sự khác biệt chính giữa Phân tích tài chính truyền thống và Phân tích tài chính hỗ trợ AI là gì?**  
   - *Trả lời:* Phân tích truyền thống chủ yếu mang tính tĩnh, phụ thuộc vào kiểm tra bảng tính lịch sử ("gương chiếu hậu"). Trong khi đó, AI thực hiện xử lý dữ liệu thời gian thực, phát hiện mẫu tự động và cung cấp mô hình dự đoán chính xác cho các kịch bản tương lai ("kính viễn vọng tiên đoán").
2. **Tại sao Kỹ thuật Prompt (Prompt Engineering) lại được coi là kỹ năng cốt lõi của Kế toán viên thời đại 4.0?**  
   - *Trả lời:* LLM hoạt động theo cơ chế xác suất ngữ cảnh; nếu không có câu lệnh đầu vào rõ ràng, có vai trò chuyên môn và phân đoạn bước xử lý chuẩn xác, kết quả AI tạo ra có thể sai lệch hoặc thiếu độ sâu pháp lý/tài chính. Prompt Engineering giúp kế toán viên làm chủ và chuẩn hóa chất lượng đầu ra của AI.
3. **Trong khung tư duy SPARKS, bước nào thường dễ bị bỏ qua nhất nhưng lại quyết định thành công của một báo cáo quản trị kế toán?**  
   - *Trả lời:* Bước **R – Refine the Analysis (Tinh chỉnh phân tích)** và **K – Communicate the Insights (Truyền đạt thông tin)**. Việc không kiểm chứng rủi ro ngoại lai (Outliers) có thể dẫn đến kết luận sai; trong khi việc trình bày biểu đồ phức tạp, khó hiểu sẽ khiến Ban Giám đốc không thể ra quyết định hành động kịp thời.

#### ** 🎬 Video **

<iframe src="video/Day13/index.html?v=1785919941" style="width: 100%; aspect-ratio: 16/9; max-height: 75vh; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>

#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slideAIAcc/Slide_AIAcc_Day13.pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day13.pdf#view=FitH" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day13.pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

#### ** 📝 Bài tập Trắc nghiệm **

<iframe src="quizzes/Day13/index.html?v=1785919941" style="width: 100%; min-height: 700px; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>


#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Bốn cấp độ Phân tích dữ liệu (Độ khó: Dễ)**
Kể tên 4 cấp độ phân tích dữ liệu từ thấp đến cao (Chương 6). Việc hệ thống AI gợi ý ban giám đốc "Nên phân bổ ngân sách marketing vào khu vực nào để tối đa hóa doanh thu" thuộc cấp độ phân tích nào?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- 4 Cấp độ: Descriptive (Mô tả) -> Diagnostic (Chẩn đoán) -> Predictive (Dự đoán) -> Prescriptive (Đề xuất/Chỉ định).
- Việc AI "gợi ý hành động tối ưu hóa ngân sách" thuộc mức độ cao nhất: **Prescriptive Analytics**.
</details>
<br>

**Bài tập 2: Áp dụng Khung tư duy SPARKS (Độ khó: Trung bình)**
Chương 6 giới thiệu Khung tư duy phân tích SPARKS. Chữ "S" (Stakeholders) và "P" (Purpose) quan trọng như thế nào trước khi bắt tay vào code các mô hình dữ liệu?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Nếu không hiểu ai là người dùng cuối (Stakeholders) và mục tiêu kinh doanh cốt lõi (Purpose), kế toán viên có thể phân tích ra những mô hình toán học rất phức tạp, độ chính xác cao nhưng hoàn toàn vô dụng vì không giải quyết đúng "nỗi đau" thực tế của doanh nghiệp.
</details>
<br>

**Bài tập 3: Chiến lược Dữ liệu - Data Strategy (Độ khó: Khó)**
Dựa trên Chương 3 & 4, Kiến trúc dữ liệu (Data Architecture) đóng vai trò gì trong một Chiến lược Dữ liệu tổng thể? Tại sao không có Data Architecture thì ứng dụng AI sẽ thất bại?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Data Architecture (Kiến trúc dữ liệu) quy định cách dữ liệu được thu thập, tổ chức, lưu trữ và luân chuyển (Data Pipelines) trong toàn công ty.
- AI cần dữ liệu lớn, liên tục và sạch. Nếu kiến trúc dữ liệu yếu kém (dữ liệu nằm rời rạc ở các phòng ban/Silos), AI sẽ không có nguyên liệu đầu vào để học, dẫn đến "Garbage in, Garbage out" (GIGO) làm dự án đổ vỡ.
</details>
<br>
<!-- tabs:end -->
