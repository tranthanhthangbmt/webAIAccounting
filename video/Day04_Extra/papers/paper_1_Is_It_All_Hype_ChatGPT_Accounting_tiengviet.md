# IS IT ALL HYPE? ĐÁNH GIÁ NĂNG LỰC THỰC TẾ VÀ TIỀM NĂNG ĐỘT PHÁ CỦA CHATGPT TRONG NGÀNH KẾ TOÁN VÀ KIỂM TOÁN
*(Is it all hype? ChatGPT's performance and disruptive potential in the accounting and auditing industries)*

- **Tác giả:** Marc Eulerich (Univ. of Duisburg-Essen), Aida Sanatizadeh, Hamid Vakilzadeh, David A. Wood (Brigham Young University - BYU)
- **Tạp chí:** Review of Accounting Studies (Springer Nature) — Tập 29, Số 3, Trang 2318–2349 (Tháng 6/2024)
- **Định danh học thuật & Giấy phép:** [https://doi.org/10.1007/s11142-024-09833-9 — Open Access CC BY 4.0](https://doi.org/10.1007/s11142-024-09833-9 — Open Access CC BY 4.0)
- **Bộ đề kiểm tra thực nghiệm:** 12 phần thi trắc nghiệm từ 4 kỳ thi chứng chỉ danh giá nhất thế giới: CPA (AUD, BEC, FAR, REG), CMA (2 phần), CIA (3 phần), EA (3 phần thuế IRS).
- **Slide bài giảng tương ứng:** Slide P2: Is it all hype? ChatGPT in Accounting (Buổi 12/15)

---

## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

ChatGPT liên tục xuất hiện trên các phương tiện truyền thông đại chúng với nhiều dự báo về những xáo trộn và đột phá to lớn, đặc biệt trong các lĩnh vực kế toán và kiểm toán. Tuy nhiên, các nghiên cứu ban đầu trên phiên bản ChatGPT-3.5 lại chứng minh năng lực tương đối yếu kém của mô hình này trong các bài kiểm tra kế toán sinh viên (Wood et al., 2023). 

Trong nghiên cứu thực chứng này, chúng tôi kiểm định năng lực của mô hình thế hệ mới hơn – **ChatGPT-4** – kết hợp với các kỹ thuật tinh chỉnh prompt tiên tiến trên ngân hàng câu hỏi sát hạch của **4 kỳ thi chứng chỉ hành nghề danh giá nhất ngành Kế toán - Kiểm toán**:
1. **CPA (Certified Public Accountant - Kế toán Công chứng Hoa Kỳ)**
2. **CMA (Certified Management Accountant - Kế toán Quản trị Hoa Kỳ)**
3. **CIA (Certified Internal Auditor - Kiểm toán Nội bộ Quốc tế)**
4. **EA (Enrolled Agent - Đại lý Thuế Liên bang Hoa Kỳ / IRS)**

Quy trình thực nghiệm được triển khai tuần tự qua 4 cấp độ:
1. **Thiết lập đường cơ sở (Baseline):** Sử dụng ChatGPT-3.5 (Zero-shot) – kết quả thi trượt 100% tất cả các môn với điểm trung bình chỉ đạt 53.1%.
2. **Nâng cấp mô hình lõi (Model Upgrade):** Chuyển sang ChatGPT-4 (Zero-shot) – điểm số tăng thêm 16.5% đạt 69.6%, tự đỗ toàn bộ chứng chỉ Kiểm toán Nội bộ (CIA).
3. **Huấn luyện ngữ cảnh qua ví dụ (Few-shot Training):** Cung cấp 10 ví dụ mẫu (10-shot) – điểm số tăng thêm 6.6% đạt 76.2%, đỗ thêm toàn bộ chứng chỉ Kế toán Quản trị (CMA).
4. **Kiến trúc Tác nhân Thông minh (ReAct - Reasoning + Acting):** Kết hợp khả năng suy luận từng bước với quyền sử dụng công cụ Máy tính bỏ túi (Calculator) và Tìm kiếm Web (Web Search) – điểm số tăng vọt thêm 8.9% đạt trung bình **85.1%**, **THI ĐỖ 100% TOÀN BỘ CÁC KỲ THI CHỨNG CHỈ NGHỀ NGHIỆP**!

Nghiên cứu khẳng định dứt khoát: **Tiềm năng đột phá của ChatGPT trong ngành kế toán - kiểm toán hoàn toàn không phải là lời đồn thổi (hype)**. Công nghệ AI tạo sinh đã thực sự đạt đến ngưỡng năng lực chuyên môn để thay đổi cơ bản cách giảng dạy kế toán trong trường đại học cũng như quy trình tác nghiệp tại các công ty kiểm toán và doanh nghiệp toàn cầu.

---

## 1. GIỚI THIỆU & ĐỘNG LỰC NGHIÊN CỨU (INTRODUCTION)

Một nghiên cứu nổi tiếng của Viện Nghiên cứu Toàn cầu McKinsey ước tính rằng đến năm 2030, Trí tuệ nhân tạo (AI) có thể thay thế hoặc làm xáo trộn tới 15% lực lượng lao động toàn cầu (tương đương 400 triệu lao động), và các nghề nghiệp liên quan đến kế toán - kiểm toán chịu tác động đặc biệt nặng nề (Manyika & Sneader, 2018).

Sự ra mắt của ChatGPT vào tháng 11/2022 – một mô hình ngôn ngữ lớn (LLM) phát triển bởi OpenAI – đã làm bùng nổ trở lại các cuộc tranh luận về việc AI sẽ định hình lại nghề kế toán như thế nào. Tuy nhiên, một công trình nghiên cứu quy mô toàn cầu của Giáo sư David A. Wood cùng 327 đồng tác giả tại 186 trường đại học (Wood et al., 2023) đã chỉ ra rằng ChatGPT-3.5 chỉ đạt trung bình 50.9% trong các bài tập kế toán của sinh viên đại học, thua xa mức điểm trung bình 75.3% của sinh viên người thật.

Nhiều chuyên gia và giảng viên kế toán vội vàng đi đến kết luận rằng: *"ChatGPT chỉ là lời đồn thổi quá đà (overhype), nó giỏi văn vẻ nhưng bất lực trước những bài toán tính toán và chuẩn mực kế toán khắt khe"*.

Tuy nhiên, sự tiến hóa của công nghệ trí tuệ nhân tạo không diễn ra tuyến tính. Việc ra mắt mô hình GPT-4 vào tháng 3/2023 và sự trỗi dậy của các kỹ thuật Prompt Engineering hiện đại (Few-shot, ReAct Agent) đòi hỏi giới học thuật phải thực hiện một đánh giá thực chứng toàn diện, khách quan và khắt khe hơn. Đó chính là động lực thôi thúc chúng tôi thực hiện nghiên cứu này.

---

## 2. PHƯƠNG PHÁP NGHIÊN CỨU & BỘ DỮ LIỆU ĐỀ THI (METHODOLOGY)

Để đo lường năng lực chuyên môn thực tế, chúng tôi không dùng các bài tập lớp học thông thường mà chọn lọc ngẫu nhiên các câu hỏi trắc nghiệm từ ngân hàng đề thi chính thức của 4 kỳ thi chứng chỉ danh giá nhất thế giới (gồm 12 phần thi riêng biệt):

| Ký hiệu Kỳ thi | Tên Chứng chỉ | Các Phần thi Thành phần (Sections) | Ngưỡng Điểm Đạt Quy ước |
| :--- | :--- | :--- | :--- |
| **CPA** | Kế toán Công chứng Hoa Kỳ | **AUD** (Kiểm toán & Xác nhận)<br>**BEC** (Môi trường & Khái niệm Kinh doanh)<br>**FAR** (Báo cáo & Kế toán Tài chính)<br>**REG** (Luật thuế & Quy định) | **75%** |
| **CMA** | Kế toán Quản trị Hoa Kỳ | **Part 1** (Lập kế hoạch tài chính, Hiệu suất, Kiểm soát)<br>**Part 2** (Quản trị tài chính chiến lược) | **75%** |
| **CIA** | Kiểm toán Nội bộ Quốc tế | **Part 1** (Kiểm toán nội bộ căn bản)<br>**Part 2** (Thực hành kiểm toán nội bộ)<br>**Part 3** (Kiến thức kinh doanh cho kiểm toán) | **75%** |
| **EA** | Đại lý Thuế Liên bang Hoa Kỳ (IRS) | **BUS** (Thuế doanh nghiệp)<br>**IND** (Thuế thu nhập cá nhân)<br>**RPP** (Đại diện, Thực hành & Thủ tục thuế) | **70%** *(hoặc quy đổi thang 105/130)* |

*Ghi chú:* Nhằm đảm bảo tính khách quan và tập trung vào năng lực ngôn ngữ - suy luận, các câu hỏi chứa đồ thị hình ảnh phức tạp và các bài luận dài được loại trừ khỏi phạm vi nghiên cứu này.

---

## 3. QUY TRÌNH THỰC CHỨNG 4 BƯỚC (CHAIN OF THOUGHT)

Nghiên cứu thiết kế một chuỗi 4 bước thực nghiệm (Chain of Thought framework) để cô lập tác động của từng yếu tố kỹ thuật:

```
[Bước 1: Baseline]      -->  ChatGPT-3.5 (Zero-shot)         --> ĐTB: 53.1% (Trượt 100%)
[Bước 2: Model Upgrade] -->  ChatGPT-4.0 (Zero-shot)         --> ĐTB: 69.6% (+16.5%, Đỗ CIA)
[Bước 3: Few-shot]      -->  ChatGPT-4.0 (10-shot Training)  --> ĐTB: 76.2% (+6.6%, Đỗ CMA)
[Bước 4: ReAct Agent]   -->  ChatGPT-4.0 + Calculator + Web  --> ĐTB: 85.1% (+8.9%, ĐỖ 100% CẢ 4 KỲ THI)
```

### Chi tiết Vòng lặp ReAct (Reasoning + Acting)
LLMs về bản chất là mạng nơ-ron dự báo xác suất của từ tiếp theo (Next Token Prediction), không được trang bị bộ xử lý số học ALU (Arithmetic Logic Unit). Khi phải nhân chia các số lớn hoặc tính thuế luỹ tiến, mô hình thường tự nhẩm tính dẫn đến lỗi số học (arithmetic errors).

Kiến trúc ReAct (Yao et al., 2022) kết nối LLM với môi trường bên ngoài thông qua thư viện LangChain:
1. **Thought (Suy nghĩ):** AI phân tích đề bài và lên kế hoạch từng bước: *"Để tính tỷ số ROA, trước tiên cần xác định Lợi nhuận sau thuế và Tổng tài sản bình quân, sau đó thực hiện phép chia"*.
2. **Action (Hành động):** Khi gặp phép tính số học, AI không tự tính mà gọi công cụ **Calculator** (chạy bằng mã Python chính xác 100%). Khi gặp văn bản thuế hoặc tỷ giá, nó gọi công cụ **Web Search**.
3. **Observation (Quan sát):** Công cụ trả về kết quả số học tuyệt đối chuẩn xác.
4. **Final Answer (Kết luận):** AI tổng hợp số liệu vào lập luận và đưa ra phương án đúng.

---

## 4. KẾT QUẢ THỰC NGHIỆM ĐỊNH LƯỢNG (EMPIRICAL RESULTS)

### Bảng 2: So sánh ChatGPT-3.5 và ChatGPT-4 ở chế độ Zero-Shot
*(Số liệu thể hiện tỷ lệ % câu trả lời đúng trên từng phần thi)*

| Kỳ thi | Phần thi | ChatGPT-3.5 | ChatGPT-4 | Mức Tăng | Kết quả GPT-4 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **CPA** | AUD (Kiểm toán) | 57.4% | **82.1%** | +24.7% | **ĐỖ (Pass)** |
| | BEC (Kinh doanh) | 59.4% | 69.7% | +10.3% | Trượt (Fail) |
| | FAR (Kế toán tài chính) | 40.6% | 49.8% | +9.2% | Trượt (Fail) |
| | REG (Luật thuế) | 46.2% | 69.4% | +23.2% | Trượt (Fail) |
| | *Trung bình CPA* | *50.9%* | *67.8%* | *+16.9%* | *Trượt (Fail)* |
| **CMA** | Part 1 | 58.3% | 69.0% | +10.7% | Trượt (Fail) |
| | Part 2 | 48.3% | 62.7% | +14.4% | Trượt (Fail) |
| | *Trung bình CMA* | *53.3%* | *65.9%* | *+12.6%* | *Trượt (Fail)* |
| **CIA** | Part 1 | 58.0% | **75.3%** | +17.3% | **ĐỖ (Pass)** |
| | Part 2 | 60.7% | **76.0%** | +15.3% | **ĐỖ (Pass)** |
| | Part 3 | 68.0% | **78.0%** | +10.0% | **ĐỖ (Pass)** |
| | *Trung bình CIA* | *62.2%* | ***76.4%*** | *+14.2%* | ***ĐỖ TRỌN VẸN*** |
| **EA** | BUS (Thuế DN) | 40.7% | 64.7% | +24.0% | Trượt (Fail) |
| | IND (Thuế cá nhân) | 37.3% | 59.3% | +22.0% | Trượt (Fail) |
| | RPP (Quy trình thuế) | 59.3% | **80.7%** | +21.4% | **ĐỖ (Pass)** |
| | *Trung bình EA* | *45.8%* | *68.2%* | *+22.5%* | *Trượt (Fail)* |
| **TỔNG** | **Điểm Trung Bình Toàn Bộ** | **53.1%** | **69.6%** | **+16.5%** | **Đỗ 5/12 phần** |

> **Nhận xét quan trọng:** Ở Bước 1, ChatGPT-3.5 trượt 100% các môn. Nhưng khi nâng cấp lên GPT-4 ở Bước 2, AI đã tự động thi đỗ trọn vẹn chứng chỉ Kiểm toán Nội bộ CIA và môn Kiểm toán CPA AUD nhờ năng lực đọc hiểu ngôn ngữ chuẩn mực vượt trội. Tuy nhiên, các môn nặng tính toán như CPA FAR (49.8%) và EA IND (59.3%) vẫn thi trượt.

---

### Bảng 4: Bước ngoặt ReAct Agent (ChatGPT-4 + 10-shot + ReAct)

| Kỳ thi | Phần thi | Không có ReAct (10-shot) | Kích hoạt ReAct | Mức Tăng | Kết quả ReAct |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **CPA** | AUD | 87.5% | **91.5%** | +4.0% | **ĐỖ (Xuất sắc)** |
| | BEC | 74.5% | **85.7%** | +11.2% | **ĐỖ (Pass)** |
| | FAR | 64.5% | **78.0%** | **+13.5%** | **ĐỖ (Pass)** |
| | REG | 71.0% | **82.0%** | +11.0% | **ĐỖ (Pass)** |
| | *Trung bình CPA* | *74.4%* | ***84.3%*** | *+9.9%* | ***ĐỖ 100% CPA*** |
| **CMA** | Part 1 | 72.7% | **84.7%** | +12.0% | **ĐỖ (Pass)** |
| | Part 2 | 71.3% | **88.5%** | **+17.2%** | **ĐỖ (Pass)** |
| | *Trung bình CMA* | *72.0%* | ***86.6%*** | *+14.6%* | ***ĐỖ 100% CMA*** |
| **CIA** | Part 1 | 83.3% | **86.0%** | +2.7% | **ĐỖ (Pass)** |
| | Part 2 | 83.3% | **87.3%** | +4.0% | **ĐỖ (Pass)** |
| | Part 3 | 82.7% | **83.4%** | +0.7% | **ĐỖ (Pass)** |
| | *Trung bình CIA* | *83.1%* | ***85.5%*** | *+2.4%* | ***ĐỖ 100% CIA*** |
| **EA** | BUS | 71.3% | **82.0%** | +10.7% | **ĐỖ (Pass)** |
| | IND | 66.7% | **78.2%** | **+11.5%** | **ĐỖ (Pass)** |
| | RPP | 88.0% | **91.3%** | +3.3% | **ĐỖ (Pass)** |
| | *Trung bình EA* | *75.3%* | ***83.8%*** | *+8.5%* | ***ĐỖ 100% EA*** |
| **TỔNG** | **ĐIỂM TRUNG BÌNH TOÀN BỘ** | **76.2%** | ***85.1%*** | **+8.9%** | ***ĐỖ 100% CẢ 4 KỲ THI*** |

---

### Bảng 5: Phân tích theo Bản chất Câu hỏi (Application vs. Remembering & Understanding)

| Loại Câu hỏi | GPT-3.5 Zero-shot | GPT-4 Zero-shot | GPT-4 10-shot | GPT-4 ReAct | Mức Tăng nhờ ReAct |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Vận dụng chuyên môn (Application)** | 40.9% | 54.9% | 62.3% | **77.4%** | **+15.1%** |
| **Ghi nhớ & Hiểu biết (Remembering & Understanding)** | 60.8% | 79.8% | 85.3% | **90.6%** | +5.4% |

> **Phát hiện cốt lõi:** Việc trang bị công cụ máy tính (ReAct) tạo ra tác động bùng nổ nhất vào các câu hỏi dạng **Vận dụng chuyên môn (Application)**, tăng vọt thêm 15.1% (từ 62.3% lên 77.4%). Điều này chứng minh AI không chỉ biết nhắc lại định nghĩa mà hoàn toàn có khả năng xử lý các bài toán kế toán thực tế khi được trang bị đúng công cụ bổ trợ!

---

## 5. TÁC ĐỘNG ĐẾN GIÁO DỤC VÀ THỰC TIỄN NGHỀ NGHIỆP

### 5.1. Tác động đến Giáo dục Kế toán (Education)
Nghiên cứu của Eulerich et al. ghi nhận những thay đổi mang tính cách mạng ngay tại các giảng đường đại học:
1. **Trợ giảng AI chuyên biệt (TA-bots):** Tại trường của một tác giả, một Chatbot AI được huấn luyện trên giáo trình và đề cương môn Hệ thống thông tin kế toán đã giải đáp hơn 51,000 thắc mắc của sinh viên chỉ trong nửa học kỳ, đạt độ chính xác >95% với chi phí vận hành chưa đầy 200 USD/tháng.
2. **Chấm điểm tự động và phản hồi tức thì:** Giảng viên sử dụng LLM để chấm bài luận kế toán, phân tích các case study và đưa ra lời nhận xét mang tính xây dựng cho từng sinh viên trong vài giây.
3. **Chuyển dịch vai trò người Thầy:** Giảng viên chuyển từ *"Người thuyết giảng độc thoại trên bục giảng"* (*sage-on-the-stage*) sang *"Người cố vấn, định hướng đồng hành bên cạnh sinh viên"* (*guide-at-the-side*).

### 5.2. Tác động đến Thực tiễn Doanh nghiệp & Big 4 (Business)
Các hãng kiểm toán hàng đầu thế giới đang chi hàng tỷ USD để tích hợp LLMs vào quy trình tác nghiệp:
- **PwC:** Đầu tư 1 tỷ USD vào các sáng kiến Generative AI và hợp tác chiến lược mở rộng với Microsoft/OpenAI.
- **KPMG:** Công bố gói đầu tư 2 tỷ USD vào trí tuệ nhân tạo và đám mây toàn cầu.
- **EY:** Đầu tư 1.5 tỷ USD, xây dựng nền tảng EY.ai và ra mắt Chatbot Bảng lương Thông minh (*Intelligent Payroll Chatbot*), giúp giảm hơn 50% khối lượng công việc trả lời thắc mắc phiếu lương thủ công.
- **Bloomberg:** Phát triển *BloombergGPT* (mô hình 50 tỷ tham số) huấn luyện chuyên biệt trên dữ liệu tài chính.
- **Khảo sát của KPMG:** 65% lãnh đạo các doanh nghiệp quy mô lớn khẳng định họ đã hoặc đang tích hợp AI vào quy trình lập Báo cáo Tài chính và Kiểm toán!

---

## 6. NHỮNG GIỚI HẠN CỐT TỬ CỦA AI VÀ CƠ HỘI CHO CON NGƯỜI

Nghiên cứu của Eulerich et al. (2024) không cổ vũ cho sự lạc quan tếu mà thẳng thắn chỉ ra 3 ranh giới giới hạn của AI:
1. **Khoảng cách giữa "Biết" và "Làm" (Knowing vs. Doing):** Việc AI đỗ 100% câu trắc nghiệm trên giấy không có nghĩa nó biết tự tay đăng nhập vào phần mềm ERP SAP hay Oracle, xử lý những hóa đơn mua hàng nhàu nát hay đối chiếu các tài khoản ngân hàng thực tế phức tạp.
2. **Hạn chế thị giác và dữ liệu phi cấu trúc:** Nghiên cứu phải loại bỏ các câu hỏi chứa biểu đồ, sơ đồ luồng chứng từ. AI hiện nay vẫn gặp khó khăn lớn khi tiếp nhận các chứng từ thực tế scan mờ, bản vẽ nghiệm thu công trình xây dựng.
3. **Ảo giác tự tin (Confident Hallucination):** Dù có ReAct, LLMs đôi khi vẫn có thể đưa ra câu trả lời sai luật với một giọng điệu vô cùng tự tin và trôi chảy. Nếu kế toán viên nhắm mắt tin tưởng mà không kiểm toán chéo, rủi ro pháp lý sẽ cực kỳ khôn lường.

### Cơ hội vàng cho Sinh viên Kế toán - Kiểm toán
Con người không cần cạnh tranh với AI về tốc độ tính toán hay trí nhớ văn bản. Giá trị độc tôn của người làm kế toán - kiểm toán nằm ở:
- **Tư duy hoài nghi nghề nghiệp (Professional Skepticism);**
- **Năng lực phán đoán đạo đức và chiến lược kinh doanh;**
- **Trách nhiệm pháp lý cao nhất trước pháp luật và xã hội.**

---

## 7. KẾT LUẬN & KHUYẾN NGHỊ

Nghiên cứu của Eulerich, Sanatizadeh, Vakilzadeh và Wood (2024) đưa ra câu trả lời đanh thép: **Sự đột phá của ChatGPT trong ngành kế toán - kiểm toán KHÔNG HỀ LÀ ĐỒN THỔI!**

Khi kết hợp đúng đắn giữa mô hình nền tảng mạnh mẽ (GPT-4), kỹ thuật huấn luyện qua ví dụ (Few-shot) và kiến trúc tác nhân cấp công cụ (ReAct Agent), AI đã vượt qua ranh giới của một cỗ máy trò chuyện để trở thành một chuyên gia phân tích nghiệp vụ đạt chuẩn kiểm toán viên quốc tế. 

Thành công trong tương lai thuộc về những kế toán viên biết làm chủ kỹ thuật Prompt, biết chỉ huy các tác nhân AI và biết "kiểm toán lại kết quả của AI" để phục vụ cho các quyết định quản trị chiến lược của doanh nghiệp!
