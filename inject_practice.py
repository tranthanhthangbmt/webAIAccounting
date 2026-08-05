import os
import re

practices = {
    '02': """
#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Đặc trưng của Big Data (Độ khó: Dễ)**
Dựa vào bài giảng về Big Data (Chương 1), hãy nêu 4 đặc tính (4Vs) của Dữ liệu lớn. Lấy ví dụ về "Velocity" (Tốc độ) trong dữ liệu kế toán của một công ty thương mại điện tử.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- 4Vs: Volume (Dung lượng), Velocity (Tốc độ), Variety (Đa dạng), Veracity (Độ tin cậy).
- Ví dụ "Velocity": Sàn TMĐT xử lý hàng triệu giao dịch mỗi giây vào dịp Black Friday. Hệ thống kế toán phải ghi nhận doanh thu và hàng tồn kho theo thời gian thực (Real-time) thay vì chờ cuối ngày khóa sổ.
</details>
<br>

**Bài tập 2: Nguyên lý Blockchain (Độ khó: Trung bình)**
Sổ cái phân tán (Distributed Ledger) của Blockchain giải quyết vấn đề "tin cậy" trong giao dịch tài chính như thế nào so với hệ thống sổ cái tập trung truyền thống?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Hệ thống tập trung: Dữ liệu nằm ở máy chủ trung tâm (ngân hàng), dễ bị hack hoặc sửa đổi đơn phương.
- Blockchain (Sổ cái phân tán): Mọi nút (node) trong mạng đều lưu bản sao sổ cái. Một giao dịch khi được xác nhận bằng cơ chế đồng thuận sẽ không thể bị xóa hoặc sửa chữa (Tính bất biến - Immutability). Điều này loại bỏ rủi ro gian lận đơn phương.
</details>
<br>

**Bài tập 3: AI kết hợp Blockchain (Độ khó: Khó)**
Theo textbook, sự kết hợp giữa AI và Blockchain tạo ra hợp đồng thông minh (Smart Contracts). Hãy thiết kế một quy trình thanh toán tự động ứng dụng Smart Contract cho dịch vụ logistics.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Cảm biến IoT trên xe tải theo dõi vị trí và nhiệt độ hàng hóa. Dữ liệu này (Variety) được AI phân tích liên tục.
- Smart Contract trên Blockchain quy định: "Nếu hàng hóa đến kho đúng giờ và nhiệt độ được duy trì dưới -5 độ C, tự động thanh toán 100% cước phí".
- Lợi ích: Tự động hóa kế toán công nợ và thanh toán, loại bỏ tranh chấp hợp đồng.
</details>
<br>
""",
    '03': """
#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Ứng dụng NLP trong Kế toán (Độ khó: Dễ)**
Giáo trình (Chương 1) đề cập đến Xử lý ngôn ngữ tự nhiên (NLP). Kế toán viên có thể dùng NLP để làm gì khi đối mặt với hàng ngàn hợp đồng thuê tài sản (Lease contracts)?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Kế toán viên sử dụng NLP để tự động đọc và trích xuất các điều khoản quan trọng (thời hạn thuê, lãi suất ngầm định, số tiền thanh toán định kỳ) từ văn bản hợp đồng phi cấu trúc, sau đó tự động phân loại theo chuẩn mực IFRS 16 thay vì nhập liệu thủ công.
</details>
<br>

**Bài tập 2: Machine Reasoning vs Machine Learning (Độ khó: Trung bình)**
Phân biệt giữa Machine Reasoning (Lập luận máy) và Machine Learning (Học máy) trong việc tự động hóa các bút toán.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Machine Reasoning: Dựa trên các quy tắc do con người thiết lập (Rule-based). Ví dụ: "NẾU hóa đơn chứa từ 'điện', GHI NHẬN vào chi phí tiện ích". Dễ giải thích nhưng kém linh hoạt.
- Machine Learning: Mô hình tự học từ dữ liệu lịch sử mà không cần lập trình quy tắc cụ thể. Nó có thể phân loại đúng các hóa đơn phức tạp chưa từng gặp trước đó.
</details>
<br>

**Bài tập 3: Rủi ro Đạo đức AI - Ethics (Độ khó: Khó)**
Dựa trên Chương 15 (Đạo đức AI): Nếu một hệ thống AI đánh giá rủi ro tín dụng từ chối khoản vay của một nhóm khách hàng do thiên kiến dữ liệu (Bias), ngân hàng phải đối mặt với rủi ro gì? Nêu giải pháp.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Rủi ro: Vi phạm pháp luật về chống phân biệt đối xử, tổn hại uy tín thương hiệu, và rủi ro pháp lý (kiện tụng).
- Giải pháp: Kế toán viên/Kiểm toán viên hệ thống cần yêu cầu sự minh bạch (Explainable AI - XAI), kiểm tra bộ dữ liệu huấn luyện để loại bỏ các thuộc tính nhạy cảm (giới tính, chủng tộc), và có cơ chế con người can thiệp (Human-in-the-loop).
</details>
<br>
""",
    '04': """
#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Phân khúc Khách hàng bằng Gom cụm (Độ khó: Dễ)**
Theo Chương 5, thuật toán Gom cụm (Clustering) giúp ích gì cho Kế toán quản trị trong việc phân khúc khách hàng (Market Segmentation) theo mức độ sinh lời?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Clustering là học không giám sát. Nó tự động nhóm khách hàng có chung đặc điểm (tần suất mua, giá trị đơn hàng, chi phí phục vụ) thành các cụm. 
- Kế toán quản trị dùng kết quả này để xác định nhóm khách hàng mang lại biên lợi nhuận cao nhất để tối ưu hóa ngân sách marketing.
</details>
<br>

**Bài tập 2: Dự báo sức khỏe tài chính bằng Classification (Độ khó: Trung bình)**
Phân loại (Classification) khác với Hồi quy (Regression) như thế nào khi áp dụng để dự báo sức khỏe tài chính (Chương 10)?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Hồi quy (Regression) dự đoán một giá trị liên tục. Ví dụ: Dự báo tỷ suất sinh lời trên tài sản (ROA) là 15.5%.
- Phân loại (Classification) dự đoán một danh mục rời rạc. Ví dụ: Phân loại tình trạng công ty là "Phá sản" (Default) hoặc "Khỏe mạnh" (Healthy).
</details>
<br>

**Bài tập 3: AI so với Mô hình Z-score truyền thống (Độ khó: Khó)**
Lợi thế của mạng nơ-ron nhân tạo (ANN) so với các mô hình thống kê phân tích phân biệt truyền thống (như Altman Z-score) khi dự báo nguy cơ phá sản.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Altman Z-score giả định mối quan hệ tuyến tính giữa các chỉ số tài chính. Tuy nhiên, rủi ro tài chính thực tế phức tạp và phi tuyến.
- Mạng nơ-ron (ANN) không cần giả định trước về sự phân phối dữ liệu, chúng tự tìm ra các mối quan hệ phi tuyến tính ẩn sâu giữa hàng ngàn biến số, mang lại độ chính xác dự báo cao hơn nhiều trong môi trường kinh tế biến động.
</details>
<br>
""",
    '05': """
#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Giảm thiểu bất định với Decision Trees (Độ khó: Dễ)**
Cây quyết định (Decision Trees) trong Chương 12 giúp Kế toán quản trị giảm thiểu sự bất định (Uncertainty) như thế nào khi lựa chọn dự án đầu tư?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Cây quyết định trực quan hóa mọi nhánh rủi ro có thể xảy ra của một dự án (thành công/thất bại).
- Bằng cách gán xác suất và dòng tiền (Payoffs) cho từng nút, kế toán tính được Giá trị kỳ vọng (Expected Value - EV) để ra quyết định dựa trên dữ liệu thay vì cảm tính.
</details>
<br>

**Bài tập 2: Phát triển Sản phẩm Mới và Capital Budgeting (Độ khó: Trung bình)**
Theo Chương 14, AI dự báo vòng đời sản phẩm (New Product Development) đóng góp gì cho việc lập ngân sách vốn (Capital Budgeting)?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- AI dự báo được nhu cầu thị trường và độ dài vòng đời sản phẩm chính xác hơn.
- Từ đó, kế toán dự phóng được chính xác hơn Dòng tiền trong tương lai (Cash flows), giúp tính NPV và IRR tin cậy hơn, tránh đầu tư vốn lớn vào các sản phẩm mau chóng lỗi thời.
</details>
<br>

**Bài tập 3: Hiện tượng Overfitting trong mô hình kinh doanh (Độ khó: Khó)**
Giải thích hiện tượng "Overfitting" (Học vẹt) trong mô hình học máy. Hậu quả của nó khi doanh nghiệp dùng mô hình này để ra quyết định là gì?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Overfitting xảy ra khi mô hình học quá mức các chi tiết và "nhiễu" của dữ liệu huấn luyện trong quá khứ, khiến nó hoạt động hoàn hảo trên dữ liệu cũ nhưng dự báo rất tệ đối với dữ liệu tương lai mới.
- Hậu quả: Dẫn đến quyết định sai lầm trầm trọng (ví dụ: mô hình dự báo doanh số quá lạc quan, dẫn đến sản xuất thừa hàng tồn kho).
</details>
<br>
""",
    '06': """
#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Phát hiện bất thường trong mua sắm công (Độ khó: Dễ)**
Theo Case study 4 (Chương 5) về chống tham nhũng khu vực công, AI có thể phát hiện điểm bất thường (Anomaly detection) nào trong hồ sơ dự thầu?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- AI phân tích các mạng lưới liên kết (Network analysis) giữa các công ty dự thầu, phát hiện trùng lặp địa chỉ IP, chung số điện thoại hoặc việc các công ty luân phiên nhau trúng thầu với mức giá chênh lệch cực nhỏ (dấu hiệu thông đồng/Bid rigging).
</details>
<br>

**Bài tập 2: AI trong hệ thống phòng chống rửa tiền (AML) (Độ khó: Trung bình)**
Hệ thống AML (Chống rửa tiền) truyền thống dựa trên các quy tắc (Rules-based) thường tạo ra lượng lớn "Cảnh báo giả" (False positives). AI giải quyết vấn đề này ra sao?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Rules-based AML cảnh báo bất kỳ giao dịch nào > 10.000 USD (gây quá tải vì nhiều giao dịch hợp pháp).
- AI (Machine Learning) học hành vi giao dịch trong quá khứ của khách hàng. Nó chỉ cảnh báo nếu giao dịch đó *bất thường so với lịch sử* của khách hàng, giúp giảm thiểu đáng kể False Positives và tiết kiệm chi phí điều tra.
</details>
<br>

**Bài tập 3: AI và Ổn định Kinh tế Vĩ mô (Độ khó: Khó)**
Theo Chương 1, phân tích cách AI thu thập dữ liệu để cảnh báo sớm rủi ro, qua đó duy trì sự ổn định tài chính (Financial Stability) của một quốc gia.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- AI không chỉ dựa vào BCTC của các ngân hàng. Nó thu thập dữ liệu vĩ mô thời gian thực (giá bất động sản, dòng vốn toàn cầu, tin tức Sentiment analysis) để mô phỏng (Stress testing) nguy cơ vỡ nợ dây chuyền (Contagion risk).
- Nhờ đó, Ngân hàng Trung ương có thể can thiệp bơm thanh khoản trước khi khủng hoảng xảy ra.
</details>
<br>
""",
    '07': """
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
""",
    '08': """
#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Chấm điểm tín dụng bằng Alternative Data (Độ khó: Dễ)**
Theo Chương 6, Mô hình AI chấm điểm tín dụng (Credit Scoring) sử dụng các nguồn dữ liệu phi truyền thống (Alternative data) nào so với ngân hàng truyền thống?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Ngân hàng truyền thống: Lịch sử vay nợ CIC, tài sản đảm bảo, BCTC.
- AI dùng Dữ liệu thay thế (Alternative Data): Lịch sử đóng tiền điện nước, thói quen mua sắm online, thanh toán tiền cước viễn thông, mạng xã hội. Giúp những người không có tài khoản ngân hàng (Unbanked) vẫn tiếp cận được tín dụng.
</details>
<br>

**Bài tập 2: Giao dịch Thuật toán - Algorithmic Trading (Độ khó: Trung bình)**
Giao dịch thuật toán do AI thực hiện mang lại lợi thế gì về tốc độ, và tiềm ẩn rủi ro thao túng cục bộ (Flash Crash) như thế nào?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Lợi thế: Thực hiện hàng nghìn lệnh mua bán trong phần nghìn giây (HFT - High Frequency Trading), kiếm lời từ sự chênh lệch giá cực nhỏ (Arbitrage) mà con người không thể làm.
- Rủi ro Flash Crash: Nếu nhiều thuật toán cùng phản ứng bán tháo với một tin tức giả mạo, giá cổ phiếu có thể sụp đổ gần bằng 0 trong vài phút trước khi con người kịp can thiệp.
</details>
<br>

**Bài tập 3: Thao túng thị trường (Spoofing) bằng AI (Độ khó: Khó)**
Theo Chương 4, nêu hình thức thao túng thị trường "Spoofing" (Đặt lệnh ảo) bằng AI. Kế toán/Kiểm toán viên cần công cụ gì để phát hiện?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Spoofing: AI đặt khối lượng lớn lệnh Mua để tạo cảm giác cầu thị trường cao (đẩy giá lên), nhưng hủy toàn bộ lệnh đó ngay trước khi khớp lệnh.
- Để phát hiện: Kiểm toán viên phải dùng chính AI phân tích Dữ liệu sổ lệnh (Order book data) cấp độ vi mô, nhận dạng tỷ lệ Hủy lệnh/Đặt lệnh bất thường (Order-to-trade ratio) vượt ngưỡng cho phép.
</details>
<br>
""",
    '09': """
#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Kế toán Tài sản mã hóa (Crypto Assets) (Độ khó: Dễ)**
Theo Chương 2, đặc điểm ẩn danh (Pseudonymity) của tiền mã hóa gây khó khăn gì cho kiểm toán viên khi xác minh tính hiện hữu của tài sản?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Do địa chỉ ví Crypto là ẩn danh (chỉ là chuỗi ký tự hash), kiểm toán viên rất khó chứng minh doanh nghiệp có thực sự nắm giữ Private Key của ví đó hay không, dẫn đến khó xác minh quyền sở hữu tài sản (Ownership & Existence).
</details>
<br>

**Bài tập 2: Robo-Advisors trong Tư vấn Tài chính (Độ khó: Trung bình)**
Dựa vào Chương 6, Cố vấn Robot (Robo-Advisors) xây dựng danh mục đầu tư cho khách hàng dựa trên những tiêu chí nào? Lợi thế lớn nhất của nó là gì?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Tiêu chí: Dựa trên độ tuổi, thu nhập, mục tiêu tài chính và khẩu vị rủi ro (Risk tolerance) được thu thập qua bảng khảo sát đầu vào.
- Lợi thế lớn nhất: Chi phí quản lý cực thấp, hoạt động 24/7, và tự động tái cân bằng danh mục (Rebalancing) không bị cảm xúc chi phối so với Broker con người.
</details>
<br>

**Bài tập 3: Đánh giá lại giá trị (Revaluation) đối với Crypto (Độ khó: Khó)**
Đánh giá rủi ro trong việc ghi nhận và đánh giá lại (Revaluation) đối với tài sản Crypto trên Bảng cân đối kế toán khi thị trường biến động mạnh.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Crypto có độ biến động (Volatility) cực lớn (có thể giảm 30% trong 1 ngày). Việc đánh giá lại giá trị hợp lý (Fair Value) vào cuối kỳ kế toán có thể gây ra những khoản lỗ chưa thực hiện (Unrealized losses) khổng lồ, làm biến dạng lợi nhuận và sức khỏe tài chính thực sự của doanh nghiệp hoạt động cốt lõi không thuộc ngành crypto.
</details>
<br>
""",
    '11': """
#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Phân biệt dữ liệu Structured vs Unstructured (Độ khó: Dễ)**
Theo Chương 2, hãy cho ví dụ về Dữ liệu có cấu trúc (Structured) và Dữ liệu phi cấu trúc (Unstructured) trong hệ thống tài chính của một doanh nghiệp.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Structured Data: Sổ cái kế toán, Bảng cân đối, số lượng hàng tồn kho (dữ liệu dạng bảng biểu, số liệu rõ ràng trong CSDL quan hệ).
- Unstructured Data: Email trao đổi của ban giám đốc, hình ảnh hóa đơn viết tay, đoạn ghi âm cuộc gọi của khách hàng đến phòng CSKH.
</details>
<br>

**Bài tập 2: Làm sạch dữ liệu - Data Cleansing (Độ khó: Trung bình)**
Làm sạch dữ liệu là bước tốn nhiều thời gian nhất (chiếm 80% thời gian phân tích). Nêu 3 lỗi dữ liệu phổ biến cần xử lý trước khi chạy mô hình phân tích rủi ro.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- 1. Missing values (Dữ liệu bị thiếu hoặc rỗng, ví dụ thiếu ngày sinh khách hàng).
- 2. Duplicates (Dữ liệu bị lặp lại nhiều lần do lỗi hệ thống).
- 3. Outliers (Dữ liệu ngoại lai phi lý, ví dụ tuổi = 999).
</details>
<br>

**Bài tập 3: Độ lệch chuẩn (Standard Deviation) trong đo lường rủi ro (Độ khó: Khó)**
Độ lệch chuẩn đo lường điều gì trong thống kê phân tích? Tại sao dữ liệu lợi nhuận tài chính có độ lệch chuẩn cao lại được coi là mang tính rủi ro nguy hiểm?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Độ lệch chuẩn đo lường mức độ phân tán của dữ liệu xung quanh giá trị trung bình.
- Lợi nhuận có độ lệch chuẩn cao nghĩa là nó dao động biên độ rất mạnh (tháng lãi lớn, tháng lỗ nặng). Sự biến động (Volatility) khó đoán định này chính là định nghĩa cốt lõi của Rủi ro tài chính.
</details>
<br>
""",
    '12': """
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
""",
    '13': """
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
""",
    '14': """
#### ** ✍️ Bài tập Luyện tập **

**Bài tập 1: Khám phá Dữ liệu - EDA (Độ khó: Dễ)**
Theo Chương 7, Phân tích Khám phá (Exploratory Data Analysis - EDA) khác biệt gì với Phân tích Kiểm định (Confirmatory Analysis) trước khi lập mô hình?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Phân tích Kiểm định (Confirmatory) là bạn có sẵn một giả thuyết (Ví dụ: "Quảng cáo FB làm tăng doanh thu") và bạn dùng thống kê để chứng minh nó.
- Khám phá Dữ liệu (EDA) là bạn "bơi" trong dữ liệu mà không có giả thuyết trước, dùng biểu đồ để tìm ra các xu hướng, điểm bất thường (outliers) hay mối tương quan ẩn giấu chưa ai biết.
</details>
<br>

**Bài tập 2: Lựa chọn Biểu đồ Thăm dò (Độ khó: Trung bình)**
Kể tên mô hình biểu đồ đồ thị thích hợp nhất để thể hiện: (1) Sự biến động doanh thu theo thời gian, và (2) Cơ cấu/Tỷ trọng nợ trên tổng tài sản.
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- (1) Thay đổi theo thời gian (Trend): Biểu đồ đường (Line chart) hoặc Biểu đồ miền (Area chart).
- (2) Tỷ trọng thành phần: Biểu đồ tròn (Pie chart) hoặc Biểu đồ dạng vòng (Donut chart), Cây thư mục (Treemap).
</details>
<br>

**Bài tập 3: Nghệ thuật Data Storytelling (Độ khó: Khó)**
Theo Chương 9, khi trình bày báo cáo phân tích AI cho Ban Giám đốc cấp cao (C-Suite), tại sao nguyên tắc "Kể chuyện dữ liệu" (Data Storytelling) lại quan trọng hơn việc trình bày các chỉ số thống kê kỹ thuật (như P-value, R-squared)?
<details>
<summary>💡 Gợi ý trả lời (Click để xem)</summary>

- Ban Giám đốc không quan tâm và thường không hiểu các thuật ngữ khoa học dữ liệu phức tạp. Họ chỉ quan tâm: Mô hình này giúp công ty kiếm thêm bao nhiêu tiền? Tiết kiệm bao nhiêu? Rủi ro là gì?
- Data Storytelling giúp dịch các con số kỹ thuật khô khan thành một câu chuyện kinh doanh có bối cảnh, cao trào và lời kêu gọi hành động (Actionable insights) dễ hiểu.
</details>
<br>
"""
}

base_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs"

for day, content in practices.items():
    file_path = os.path.join(base_dir, f"buoi_{day}.md")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    # Find the Trac Nghiem section
    trac_nghiem_pattern = r"(#### \*\* 📝 Bài tập Trắc nghiệm \*\*\n\n<iframe[^>]+></iframe>\n\n)(<!-- tabs:end -->)"
    
    match = re.search(trac_nghiem_pattern, file_content)
    if match:
        new_content = file_content[:match.end(1)] + content + match.group(2) + file_content[match.end(2):]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully injected into {day}")
    else:
        # Check if tabs:end is present
        end_pattern = r"(<!-- tabs:end -->)"
        match = re.search(end_pattern, file_content)
        if match:
            new_content = file_content[:match.start(1)] + content + match.group(1) + file_content[match.end(1):]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully injected into {day} (fallback method)")
        else:
            print(f"Could not find insertion point in {day}")
