# KẾ HOẠCH SLIDE THỰC HÀNH - DAY 1 (BUỔI 1)
**Tên bài:** THỰC HÀNH AI TẠO SINH (GAI) TRONG KẾ TOÁN & KỸ NĂNG PROMPT CƠ BẢN
**Định hướng:** Hands-on (Thực hành trực tiếp), Kế toán No-code, Phân tích tình huống.
**Nguồn dữ liệu:** *ChatGPT and AI for Accountants - Chapter 1: Generative Artificial Intelligence (GAI) in Accounting*

**ĐỀ XUẤT NGUỒN ẢNH MINH HỌA:**
- **Lấy từ file DOCX (Sách gốc):** Dùng Python giải nén thư mục `word/media` từ file DOCX tương ứng của sách thực hành để lấy các bảng biểu (như Bảng Tác động của AI lên kế toán).
- **Chụp ảnh màn hình (Screenshot):** Phần thực hành rất cần ảnh chụp màn hình giao diện của ChatGPT, QuickBooks Online, Xero, Tableau.
- **Sinh ảnh bằng AI:** Các slide về kỹ năng, tư duy, hoặc hình minh họa cho các Case Study (Quán cà phê, Công ty thiết kế).

---

# PHẦN 1: GIỚI THIỆU THỰC HÀNH & CÔNG CỤ CẦN CHUẨN BỊ

## TRANG BÌA (Title Page)
- Tiêu đề chính: Trí tuệ Nhân tạo cho Kế toán (Phần Thực Hành)
- Tiêu đề phụ: Buổi 1 - Ứng dụng GAI và Hướng dẫn Prompt cơ bản
- *(🖼️ Ảnh minh họa: Hình nền máy tính đang mở phần mềm kế toán và màn hình chat AI).*

## NỘI DUNG CHƯƠNG TRÌNH THỰC HÀNH
- 1. Điều kiện tiên quyết và Công cụ AI kế toán
- 2. Ứng dụng AI Tự động hóa \& Phân tích dự báo
- 3. Case Studies: Phân tích Bài toán thực tế
- 4. Kỹ năng sinh tồn \& Thực hành viết Prompt

## Khởi động (Ice-breaker)
- Trích dẫn Sam Altman: *"Nó chậm, nhiều lỗi, làm nhiều thứ chưa tốt, nhưng những chiếc máy tính đầu tiên cũng vậy."*
- Thông điệp: Đừng kỳ vọng AI hoàn hảo ngay lập tức, hãy học cách dùng nó từ bây giờ.

## Năng lực đạt được sau buổi học
- **Về Lý thuyết (LT):** Nắm vững nền tảng Hệ thống Thông tin Kế toán (AIS); Phân biệt rõ sự khác nhau giữa AI, Machine Learning và Deep Learning trong bối cảnh kế toán tài chính.
- **Về Thực hành (TH):** Có khả năng sử dụng các Generative AI (ChatGPT, Copilot, Gemini) để đóng vai (Role-play) hỗ trợ giải đáp các chuẩn mực kế toán cơ bản.
- **Về Tư duy nghề nghiệp:** Chấp nhận và thích nghi với sự thay đổi của nghề kế toán trong kỷ nguyên AI; Nhận thức AI là công cụ hỗ trợ (Copilot), không phải mối đe dọa thay thế hoàn toàn kế toán viên.

## Điều kiện tiên quyết (Prerequisites)
- Hạ tầng kỹ thuật (Technical infrastructure) không cần quá phức tạp nhưng phải đúng chuẩn.
- Gồm 3 khía cạnh: Trình duyệt web, Nền tảng AI, và Tư duy mở.

## Công cụ cần có: Phần mềm \& Tài khoản
- Trình duyệt web hiện đại: Chrome, Edge, Safari.
- Quyền truy cập Nền tảng AI: Đăng ký tài khoản OpenAI (ChatGPT) hoặc Google Gemini.
- *(🖼️ Ảnh minh họa: Screenshot trang đăng ký tài khoản ChatGPT).*

## Tư duy cần có: Sự tò mò trí tuệ (Intellectual Curiosity)
- Vượt qua rào cản kỹ thuật: Một tư duy cởi mở để khám phá, thử nghiệm (experiment) và thích nghi với cách xử lý dữ liệu mới.

## Hệ sinh thái Phần mềm Kế toán tích hợp AI
- Xử lý dữ liệu tự động: QuickBooks, Xero.
- Phân tích \& Báo cáo nâng cao: IBM Cognos Analytics, Tableau.
- Lưu trữ đám mây \& Bảo mật: AWS, Microsoft Azure.
- *(🖼️ Ảnh minh họa: Logo của QuickBooks, Xero, Tableau, AWS).*

---

# PHẦN 2: ỨNG DỤNG AI TỰ ĐỘNG HÓA & PHÂN TÍCH DỰ BÁO

## Đột phá của AI trong Tính toán Kế toán
- AI không chỉ tính toán cộng trừ nhân chia, mà xử lý các kịch bản tài chính cực kỳ phức tạp.
- Tập trung vào 2 trụ cột: Tự động hóa tính toán \& Phân tích dự báo.

## Tự động hóa các tính toán phức tạp (Automating Calculations)
- Hiệu suất và chính xác (Efficiency \& Accuracy): Tự động tính thuế, khấu hao, dự phóng tài chính với tốc độ đáng kinh ngạc.
- Thuật toán thích ứng (Adaptive algorithms): AI liên tục học luật thuế mới, cập nhật chuẩn mực (IFRS/VAS) để tuân thủ.

## Giảm thiểu sai sót (Error Reduction)
- Tác động: Loại bỏ rủi ro do con người mệt mỏi, nhập sai số liệu. Đảm bảo tính tuân thủ pháp lý khắt khe.
- *(🖼️ Ảnh minh họa: Đồ thị so sánh tỷ lệ lỗi giữa nhập liệu thủ công và AI).*

## Khả năng Phân tích Dự báo (Predictive Analytics)
- Dự báo (Forecasting): Dựa trên dữ liệu lịch sử để vẽ ra các kịch bản dòng tiền tương lai.
- Hỗ trợ lãnh đạo ra quyết định chiến lược thay vì chỉ nhìn vào báo cáo quá khứ.

## Phân tích \& Diễn giải Dữ liệu (Insightful Data Interpretation)
- Không chỉ xử lý số liệu, AI "đọc vị" dữ liệu.
- Nhận diện xu hướng (Trends), phát hiện rủi ro tiềm ẩn (Risks) và chỉ ra cơ hội tối ưu hóa lợi nhuận.

## Lời khuyên Tài chính Cá nhân hóa (Personalized Advice)
- AI không đưa ra lời khuyên chung chung.
- Nó tùy chỉnh chiến lược dựa trên bối cảnh đặc thù của từng doanh nghiệp (ngành nghề, quy mô, tình trạng nợ).

---

# PHẦN 3: CASE STUDIES - BÀI TOÁN THỰC TẾ

## Tại sao cần Case Study?
- Học qua thực tiễn: Xem cách AI tháo gỡ khó khăn cho các quy mô doanh nghiệp khác nhau: Cửa hàng nhỏ, Công ty dịch vụ, Tập đoàn đa quốc gia.
- *(🖼️ Ảnh minh họa: Bảng "Impact of AI on accounting" (Tác động của AI) từ sách giáo khoa).*

## Case Study 1: Quán cà phê Brewed Awakenings
- **Bối cảnh:** Doanh nghiệp nhỏ, ít nhân sự, đau đầu vì quản lý chi phí, thuế và dòng tiền lẻ tẻ.
- **Giải pháp:** Sử dụng phần mềm QuickBooks Online tích hợp AI.
- *(🖼️ Ảnh minh họa: AI Generated - Quán cà phê nhộn nhịp).*

## Kết quả tại Brewed Awakenings
- Phân loại tự động chi phí (Categorization).
- Đồng bộ giao dịch ngân hàng theo thời gian thực (Bank Feeds).
- Dự báo dòng tiền \& Lập kế hoạch thuế chính xác. Chủ quán rảnh tay tập trung chăm sóc khách hàng.

## Case Study 2: Công ty tư vấn thiết kế Cityscape Consulting
- **Bối cảnh:** Công ty kiến trúc, tập trung vào dự án sáng tạo. Ngân sách dự án thay đổi liên tục, cần quản lý chi phí dự án sát sao.
- **Giải pháp:** Áp dụng Xero AI.
- *(🖼️ Ảnh minh họa: AI Generated - Văn phòng kiến trúc sư).*

## Kết quả tại Cityscape Consulting
- Theo dõi sức khỏe tài chính dự án (Real-time overview).
- Gợi ý cơ hội tiết kiệm chi phí và các khoản được khấu trừ thuế.
- Biến Xero thành "Giám đốc tài chính ảo" (Virtual CFO).

## Nhìn lại Doanh nghiệp vừa \& nhỏ (SMEs)
- AI đã san bằng sân chơi: Các doanh nghiệp nhỏ giờ đây có trong tay sức mạnh phân tích tài chính vốn chỉ dành cho các tập đoàn lớn có ngân sách hàng triệu USD.

## Case Study 3: Tập đoàn GlobalTech Enterprises
- **Bối cảnh:** Tập đoàn đa quốc gia, lượng dữ liệu khổng lồ, chi nhánh ở nhiều quốc gia với các luật thuế khác nhau (VAT, GST, State Tax).
- **Giải pháp:** Tích hợp IBM Watson (AI doanh nghiệp siêu lớn).
- *(🖼️ Ảnh minh họa: Hình ảnh quả địa cầu kết nối mạng lưới dữ liệu toàn cầu).*

## Sức mạnh của IBM Watson tại GlobalTech
- Tự động hóa tuân thủ thuế quốc tế (Automated international compliance).
- Mô hình hóa tài chính dự báo toàn cầu (Predictive financial modeling) đối phó với tỷ giá, lạm phát.
- Xử lý mượt mà hàng triệu hóa đơn liên công ty (Inter-company transfers).

## Bài toán Đạo đức \& Bảo mật tại Tập đoàn lớn
- Rủi ro lớn nhất: Lộ lọt dữ liệu nhạy cảm.
- Giải pháp: IBM Watson tuân thủ nghiêm ngặt GDPR (Châu Âu) và CCPA (Mỹ).
- Kiểm toán liên tục (Continuous Audits) đối với chính hệ thống AI.

## Tính công bằng của AI (Bias and Fairness)
- AI phải minh bạch (Transparency).
- Đảm bảo AI không mang định kiến khi chấm điểm tín dụng hoặc phê duyệt nhà cung cấp.

---

# PHẦN 4: CHUẨN BỊ KỸ NĂNG & HƯỚNG DẪN PROMPT CƠ BẢN

## Chuẩn bị cho Tương lai AI (Future-proofing)
- "Máy móc không thay thế con người, nhưng người dùng máy móc sẽ thay thế người không dùng máy."
- 5 Kỹ năng cốt lõi Kế toán viên cần trang bị ngay hôm nay.
- *(🖼️ Ảnh minh họa: 5 mảnh ghép Puzzle tạo nên chân dung Kế toán viên thời 4.0).*

## Kỹ năng 1: Hiểu biết về AI (AI Literacy)
- Không cần biết lập trình thuật toán, nhưng phải hiểu cách AI hoạt động cơ bản (Input -> Blackbox -> Output).
- Hiểu được các khái niệm Học máy (Machine Learning) để biết AI có thể làm gì và không làm được gì.

## Kỹ năng 2: Năng lực Quản lý Dữ liệu (Data Proficiency)
- Đảm bảo nguồn dữ liệu sạch (Data Quality).
- Kỹ năng diễn giải đầu ra của AI (Data Interpretation) để biến báo cáo khô khan thành chiến lược hành động.

## Kỹ năng 3: Am hiểu Công nghệ \& Phần mềm (Software Familiarity)
- Nắm bắt giao diện và luồng làm việc của các ERP tích hợp AI (QuickBooks, Xero).
- Tính thích ứng (Adaptability) cao khi giao diện phần mềm cập nhật liên tục.

## Kỹ năng 4: Tư duy Phản biện \& Chiến lược (Critical Thinking)
- AI đưa ra số liệu, con người ra Quyết định.
- Kỹ năng tra vấn lại số liệu của AI (Fact-checking) để tránh lỗi "ảo giác" (Hallucination).
- Chuyển dịch từ người lập báo cáo sang vị thế Cố vấn chiến lược (Strategic Advisory).

## Kỹ năng 5: Học tập suốt đời (Continuous Learning)
- Công nghệ AI thay đổi từng ngày. Kiến thức hôm nay có thể lỗi thời vào tháng sau.
- Tham gia các hội thảo, khóa học về FinTech \& AI liên tục.

## LAB 1: Khởi động với ChatGPT (Prompting 101)
- **Nhiệm vụ:** Đăng nhập ChatGPT/Gemini.
- **Thực hành viết Prompt cơ bản:** "Hãy đóng vai một chuyên gia Kế toán, giải thích cho tôi khái niệm Khấu hao theo đường thẳng bằng ngôn ngữ đơn giản cho người không chuyên."
- *(🖼️ Ảnh minh họa: Chụp màn hình thao tác nhập Prompt).*

## LAB 2: Xử lý tình huống Kế toán
- **Nhiệm vụ:** Viết một email nhắc nợ.
- **Thử nghiệm:** 
  1. Viết Prompt chung chung: "Viết email đòi nợ." -> Xem kết quả (Thường cộc lốc).
  2. Viết Prompt tối ưu: "Đóng vai Kế toán công nợ, viết 1 email lịch sự nhưng kiên quyết đòi khoản nợ 50 triệu đã quá hạn 30 ngày từ công ty XYZ. Văn phong chuyên nghiệp." -> Xem kết quả khác biệt.

## Tổng kết Buổi Thực hành
- Công cụ phần mềm (QuickBooks, Xero, IBM Watson) đang định hình lại cách kế toán vận hành từ SME đến Tập đoàn.
- Hành trang mang về: 5 Kỹ năng sinh tồn \& Kỹ thuật đặt câu lệnh (Prompting) đầu tiên.

## Q\&A \& Hướng dẫn Tự học
- Trả lời thắc mắc của sinh viên trong quá trình tạo tài khoản.
- Giao bài tập về nhà: Tạo một kịch bản Prompt cho ChatGPT để tóm tắt một đoạn thông tư thuế dài 3 trang.
