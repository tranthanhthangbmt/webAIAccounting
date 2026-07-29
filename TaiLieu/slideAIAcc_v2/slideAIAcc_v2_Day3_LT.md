# KẾ HOẠCH SLIDE LÝ THUYẾT - DAY 3 (BUỔI 3)
**Tên bài:** AI HỖ TRỢ NHẬP LIỆU \& XỬ LÝ CHỨNG TỪ KẾ TOÁN
**Định hướng:** Chuyển đổi từ nhập liệu thủ công sang tự động hóa. Tích hợp kiến thức về Quy trình luân chuyển hóa đơn (Revenue Cycle) và Bảo mật dữ liệu (Confidentiality \& Privacy Controls).
**Cấu trúc:** 42 Slides.

**ĐỀ XUẤT NGUỒN ẢNH MINH HỌA:**
- **Lấy từ file DOCX/PDF:** Sơ đồ luân chuyển chứng từ (Revenue Cycle), các phương pháp bảo vệ quyền riêng tư (Privacy Controls).
- **Chụp ảnh màn hình (Screenshot):** Giao diện ChatGPT phân tích hóa đơn PDF, ứng dụng OCR quét hóa đơn đỏ.
- **Sinh ảnh bằng AI:** Robot AI đang đọc và quét hàng núi giấy tờ hóa đơn; Cỗ máy biến giấy tờ thành file Excel.

---

# PHẦN 1: TỔNG QUAN QUY TRÌNH CHỨNG TỪ \& NỖI ĐAU NHẬP LIỆU

## TRANG BÌA (Title Page)
- Tiêu đề chính: Trí tuệ Nhân tạo cho Kế toán
- Tiêu đề phụ: Buổi 3 - AI Hỗ trợ Nhập liệu \& Xử lý Chứng từ
- Tác giả: Đại học Đông Á
- *(🖼️ Ảnh minh họa: AI Generated - Một robot đang chiếu tia laser quét qua một tờ hóa đơn tài chính, biến nó thành các dòng code số).*

## Năng lực đạt được sau buổi học
- **Về Lý thuyết (LT):** Hiểu được quy trình luân chuyển chứng từ (Revenue Cycle) và cách công nghệ OCR/AI thay thế việc nhập liệu thủ công; Nhận thức rõ các rủi ro bảo mật (Confidentiality \& Privacy) khi chia sẻ dữ liệu kế toán với AI.
- **Về Thực hành (TH):** Biết cách sử dụng Prompt (như Provide formatting instructions) kết hợp ChatGPT/Copilot hoặc tính năng OCR của Excel để bóc tách dữ liệu từ hình ảnh/PDF hóa đơn thành định dạng bảng.
- **Về Tư duy nghề nghiệp:** Chuyển dịch từ tư duy "người nhập liệu" sang "người kiểm soát" (Reviewer), biết cách bảo vệ dữ liệu nhạy cảm của doanh nghiệp trước các công cụ AI công cộng.

## Khởi động (Ice-breaker)
- **Câu hỏi:** Bạn dành bao nhiêu phần trăm thời gian làm việc chỉ để gõ lại số liệu từ hóa đơn giấy vào phần mềm kế toán MISA/Excel?
- **Thực trạng:** Hơn 60\% thời gian của sinh viên kế toán mới ra trường là làm công việc "thợ gõ" (Data entry).

## Quy trình Bán hàng \& Thu tiền (The Revenue Cycle)
- Bất kỳ doanh nghiệp nào cũng có chu trình Doanh thu.
- Bắt đầu từ khi khách hàng đặt hàng $\rightarrow$ Giao hàng $\rightarrow$ Xuất hóa đơn $\rightarrow$ Thu tiền.
- Mỗi bước đều phát sinh một loại **Chứng từ (Document)**.

## Các loại chứng từ cốt lõi trong Chu trình Doanh thu
- Đơn đặt hàng (Purchase Order).
- Phiếu xuất kho (Packing Slip / Delivery Note).
- Hóa đơn giá trị gia tăng (Sales Invoice).
- Giấy báo có của Ngân hàng (Remittance Advice).
- *(🖼️ Ảnh minh họa: Hình ảnh thực tế của 4 loại chứng từ trên).*

## Luân chuyển chứng từ truyền thống
- Kế toán viên phải thu thập bản cứng hoặc file PDF qua Zalo/Email.
- Mở file lên ở một màn hình, màn hình kia mở phần mềm MISA.
- Nhìn bằng mắt, gõ lại từng con số: Mã số thuế, Tên công ty, Tiền trước thuế, Tiền thuế VAT...

## Rủi ro của phương pháp thủ công
- **Sai sót con người (Human Error):** Gõ sai dấu phẩy thập phân (1,000,000 thành 100,000). Hậu quả: Báo cáo thuế sai, phạt chậm nộp.
- **Quá tải cuối tháng (Bottleneck):** Hóa đơn dồn về cuối tháng khiến kế toán phải OT (làm thêm giờ) liên tục.
- **Mất mát dữ liệu:** Rách giấy, mờ mực, trôi tin nhắn Zalo.

## Nhu cầu tự động hóa
- Doanh nghiệp không trả lương cho kế toán chỉ để "gõ máy".
- Doanh nghiệp trả lương cho kế toán để **Phân tích** và **Kiểm soát**.
- Giải pháp: Giao việc nhập liệu cho máy móc.

---

# PHẦN 2: CÔNG NGHỆ NHẬN DẠNG QUANG HỌC (OCR)

## OCR là gì? (Optical Character Recognition)
- \textbf{Định nghĩa:} Nhận dạng ký tự quang học.
- \textbf{Bản chất:} Chuyển đổi hình ảnh của văn bản (ảnh chụp, PDF scan) thành định dạng văn bản mà máy tính có thể hiểu và chỉnh sửa (như Word, Excel).

## Cơ chế hoạt động của OCR truyền thống
1. Quét hình ảnh (Image Acquisition).
2. Tiền xử lý (Pre-processing): Làm nét chữ, làm trắng nền.
3. Phân tích vùng (Zoning): Xác định đâu là vùng chứa chữ, đâu là logo.
4. Trích xuất ký tự (Character Extraction).

## Ứng dụng OCR trong Kế toán
- Chụp ảnh hóa đơn nhà hàng $\rightarrow$ Tự động trích xuất Tên nhà hàng, Ngày ăn, Tổng số tiền.
- Scan hàng loạt hóa đơn đầu vào $\rightarrow$ Đẩy thẳng vào phần mềm kế toán.
- *(🖼️ Ảnh minh họa: App điện thoại chụp hóa đơn).*

## Nhược điểm của OCR truyền thống
- Dựa trên \textbf{Luật (Rule-based)} và \textbf{Tọa độ (Template-based)}.
- Nếu nhà cung cấp đổi mẫu hóa đơn (Logo dời sang phải, Tên công ty tụt xuống dưới), OCR cũ sẽ đọc sai bét.
- Rất kém trong việc nhận dạng chữ viết tay hoặc hóa đơn bị nhàu nát, chụp mờ.

## Sự tiến hóa: OCR kết hợp AI (Intelligent Document Processing - IDP)
- AI vào cuộc! Thay vì học thuộc tọa độ, AI được huấn luyện (Machine Learning) để "Hiểu" hóa đơn.
- AI hiểu ngữ cảnh: "Số nằm cạnh chữ VAT 8\% chắc chắn là tiền thuế, dù nó nằm ở góc nào của tờ giấy".

---

# PHẦN 3: ỨNG DỤNG GENERATIVE AI ĐỂ XỬ LÝ CHỨNG TỪ

## Kỷ nguyên của Generative AI (ChatGPT/Copilot)
- Các mô hình ngôn ngữ lớn (LLMs) như GPT-4 hay Gemini hiện nay đều có khả năng \textbf{Thị giác máy tính (Computer Vision)}.
- Chúng không chỉ đọc chữ (OCR), mà còn hiểu logic của chứng từ kế toán!

## Prompt Engineering (Kỹ thuật đặt câu lệnh) cho Hóa đơn
- Bạn có thể tải file PDF hóa đơn lên ChatGPT.
- **Prompt:** "Đây là hóa đơn mua hàng. Hãy đọc nó và trích xuất cho tôi các thông tin sau: Mã số thuế người bán, Tổng tiền trước thuế, Thuế VAT, Tổng thanh toán."

## Trích xuất ra định dạng Bảng (Table)
- Để tiện cho việc nhập liệu, ta yêu cầu AI trả về dưới dạng bảng.
- **Prompt:** "Hãy trình bày kết quả dưới dạng bảng có các cột: STT, Tên Hàng Hóa, Số Lượng, Đơn Giá, Thành Tiền. Bỏ qua các dòng trống."

## Xuất dữ liệu thẳng ra Excel/CSV
- Khả năng tuyệt vời của AI là tạo ra file.
- **Prompt:** "Hãy xuất kết quả trên thành một file CSV để tôi có thể mở bằng Excel."
- Kế toán chỉ cần tải file về và import thẳng vào phần mềm!

## So sánh đối chiếu chứng từ (3-Way Matching)
- Kế toán thường phải dò 3 tờ giấy: Đơn đặt hàng (PO) + Phiếu xuất kho + Hóa đơn xem có khớp số lượng và đơn giá không.
- **Giải pháp AI:** Tải cả 3 file lên ChatGPT.
- **Prompt:** "Hãy đối chiếu xem số lượng hàng giao thực tế có khớp với số lượng đặt hàng và số lượng xuất hóa đơn không. Chỉ ra các điểm sai lệch."

## Tiềm năng tự động hóa 100\% (RPA + AI)
- RPA (Robotic Process Automation): Các con bot tự động click chuột.
- Kết hợp RPA và AI:
  - Bot tự mở Email tải hóa đơn PDF về.
  - Bot đẩy PDF vào AI để đọc lấy số liệu.
  - Bot tự động mở phần mềm MISA, điền số liệu vào đúng ô và bấm Lưu.

## Ví dụ thực tế: Hệ thống tự động của các Big4
- PwC, Deloitte, EY, KPMG đều đã xây dựng các hệ thống AI nội bộ để tự động đọc hàng triệu chứng từ kiểm toán mỗi năm.
- Sinh viên kế toán cần làm quen với tư duy này để không bị đào thải.

---

# PHẦN 4: THỰC HÀNH TƯ DUY XỬ LÝ VỚI AI

## Case Study: Hóa đơn xăng dầu viết tay
- Lái xe mang về một xấp hóa đơn bán lẻ xăng dầu, chữ viết tay nguệch ngoạc.
- Nếu gõ tay: Mất 1 tiếng, dễ hoa mắt nhìn nhầm số.

## Giải quyết Case Study bằng ChatGPT
- Bước 1: Dùng điện thoại chụp lại xấp hóa đơn.
- Bước 2: Gửi ảnh vào app ChatGPT.
- Bước 3: Prompt "Nhận diện số tiền và ngày tháng trên các hóa đơn này, cộng tổng lại cho tôi."

## Kiểm chứng kết quả của AI (Human-in-the-loop)
- AI không hoàn hảo (Có thể bị Hallucination - Ảo giác).
- Nó có thể đọc nhầm số "8" thành số "3" nếu viết tay quá xấu.
- \textbf{Vai trò của Kế toán viên:} Không phải là người nhập liệu, mà là người \textbf{Duyệt (Review)} dữ liệu do AI làm ra.

## Nhận diện bất thường (Anomaly Detection)
- Cấp dữ liệu 1000 hóa đơn cho AI.
- Prompt: "Hãy tìm cho tôi những hóa đơn có ngày xuất vào Chủ Nhật hoặc ngày Lễ, hoặc có số tiền chiết khấu cao bất thường so với mức 5\% thông thường."
- AI sẽ quét trong 10 giây và lọc ra các hóa đơn đáng ngờ.

---

# PHẦN 5: BẢO MẬT, QUYỀN RIÊNG TƯ \& KIỂM SOÁT

## Mặt trái của việc dùng AI xử lý chứng từ
- Khi tải Hóa đơn, Bảng lương, Hợp đồng lên ChatGPT, bạn đang đưa dữ liệu đi đâu?
- Các mô hình AI công cộng sẽ dùng dữ liệu của bạn để huấn luyện tiếp!
- Rủi ro lộ lọt bí mật kinh doanh (Confidentiality Risk).

## Confidentiality (Tính Bảo mật)
- \textbf{Định nghĩa:} Bảo vệ các tài sản trí tuệ và thông tin nhạy cảm của tổ chức (Kế hoạch kinh doanh, Báo cáo tài chính nội bộ, Danh sách khách hàng VIP).
- Nếu lộ ra ngoài, đối thủ cạnh tranh sẽ hưởng lợi.

## Privacy (Quyền riêng tư)
- \textbf{Định nghĩa:} Bảo vệ thông tin cá nhân (PII - Personally Identifiable Information) của khách hàng, nhân viên (CCCD, Số tài khoản ngân hàng, Lịch sử mua hàng).
- Pháp luật quy định rất nghiêm (GDPR, CCPA, Nghị định 13/2023/NĐ-CP của Việt Nam về Bảo vệ dữ liệu cá nhân).

## 4 Bước để Bảo vệ Dữ liệu theo chuẩn Quốc tế (Hình 12-1)
1. \textbf{Identify \& Classify:} Nhận diện và phân loại thông tin nào là Mật, thông tin nào là Phổ thông.
2. \textbf{Encryption:} Mã hóa dữ liệu (Đặc biệt quan trọng).
3. \textbf{Access Controls:} Kiểm soát truy cập (Ai được quyền xem, ai được quyền tải về).
4. \textbf{Training:} Đào tạo nhân viên (Tránh việc gửi nhầm mail, up nhầm file lên mạng).

## Phân loại dữ liệu trước khi đưa cho AI
- **Public (Công khai):** Thông tư, nghị định, chuẩn mực kế toán $\rightarrow$ Dùng ChatGPT công cộng vô tư.
- **Internal (Nội bộ):** Quy trình làm việc, mẫu biểu không chứa số liệu mật $\rightarrow$ Cẩn trọng.
- **Confidential/Restricted (Mật):** Hợp đồng M\&A, Bảng lương, Báo cáo doanh thu $\rightarrow$ \textbf{TUYỆT ĐỐI KHÔNG} tải lên ChatGPT miễn phí.

## Mã hóa dữ liệu (Encryption)
- Là phương pháp biến dữ liệu đọc được thành một chuỗi ký tự vô nghĩa (Ciphertext).
- Chỉ có người sở hữu "Chìa khóa" (Decryption Key) mới giải mã được.
- Bảo vệ dữ liệu trên đường truyền mạng (In transit) và dữ liệu lưu trữ trên máy (At rest).

## Giấu thông tin (Data Masking / Tokenization)
- Khi cần test hệ thống AI hoặc thuê lập trình viên ngoài.
- Dùng Data Masking để ẩn đi các dữ liệu nhạy cảm.
- Ví dụ: Số thẻ tín dụng \texttt{1234-5678-9012-3456} thành \texttt{XXXX-XXXX-XXXX-3456}.

## Enterprise AI (AI dành cho Doanh nghiệp)
- Để xử lý chứng từ mật, doanh nghiệp phải mua bản quyền \textbf{Enterprise AI} (Ví dụ: Microsoft Copilot for Microsoft 365, ChatGPT Enterprise).
- Cam kết của nhà cung cấp: "Chúng tôi KHÔNG sử dụng dữ liệu của bạn để huấn luyện mô hình. Dữ liệu của bạn được mã hóa hoàn toàn."

## Information Rights Management (IRM)
- Phần mềm kiểm soát quyền thông tin.
- Dù file hóa đơn đã được gửi đi, kế toán trưởng vẫn có quyền giới hạn:
  - Chỉ cho phép xem, không cho in ấn (Print).
  - Cấm copy/paste.
  - Tự động hủy file (Revoke access) sau 7 ngày.

## Data Loss Prevention (DLP)
- Hệ thống phòng chống thất thoát dữ liệu.
- Hoạt động như một màng lọc: Nếu một nhân viên thử gửi email đính kèm file có chứa từ khóa "Bảng lương", hệ thống sẽ chặn email lại và cảnh báo quản lý.

## Digital Signatures (Chữ ký số)
- Chứng từ kế toán hiện đại không thể thiếu Chữ ký số.
- Chữ ký số không phải là ảnh chụp chữ ký tay dán vào PDF!
- Nó là một thuật toán mã hóa phức tạp chứng minh:
  1. Ai là người tạo ra văn bản này (Non-repudiation).
  2. Văn bản chưa hề bị chỉnh sửa kể từ khi ký (Integrity).

## Cách tạo Chữ ký số (Hashing)
- \textbf{Hàm băm (Hash):} Biến một văn bản dài thành một đoạn code ngắn duy nhất (Ví dụ độ dài 256 ký tự). Nếu sửa dù chỉ 1 dấu chấm trong văn bản, đoạn code Hash sẽ thay đổi hoàn toàn.
- Ký số = Mã hóa đoạn Hash đó bằng Khóa Bí Mật (Private Key) của giám đốc.

## Blockchain trong chứng từ (Khái niệm sơ lược)
- Blockchain có thể hiểu đơn giản là một cuốn sổ cái (Ledger) được nhân bản ra hàng ngàn máy tính.
- Khi một chứng từ hóa đơn được đưa lên Blockchain, nó không thể bị xóa bỏ, không thể bị sửa chữa (Immutability).
- Tạo ra niềm tin tuyệt đối trong kế toán.

## Quy trình chuẩn khi áp dụng AI vào Kế toán
1. Nhận chứng từ gốc.
2. Xóa/Ẩn thông tin định danh nhạy cảm cá nhân.
3. Cấp cho Enterprise AI để trích xuất dữ liệu.
4. Con người (Kế toán viên) kiểm tra lại kết quả.
5. Duyệt và lưu vào CSDL (có phân quyền Access Control).

## Trách nhiệm nghề nghiệp của Kế toán viên
- AI là trợ thủ, không phải người chịu trách nhiệm trước pháp luật.
- Nếu AI đọc sai số tiền thuế và bạn duyệt bấm nộp, cơ quan thuế sẽ phạt Doanh nghiệp (và truy trách nhiệm bạn), chứ không phạt OpenAI!

## Tóm tắt Buổi 3
- \textbf{Giá trị:} AI và OCR giải phóng kế toán khỏi công việc nhập liệu nhàm chán.
- \textbf{Kỹ năng:} Biết cách dùng Prompt để bắt AI đọc, trích xuất và đối chiếu chứng từ.
- \textbf{Tuân thủ:} Luôn cảnh giác với bảo mật dữ liệu, phân loại tài liệu mật và hiểu về cơ chế mã hóa.

## Chuẩn bị cho Buổi Thực hành
- Cài đặt sẵn Excel.
- Đăng ký tài khoản ChatGPT hoặc chuẩn bị Microsoft Copilot.
- Chuẩn bị các file ảnh, file PDF hóa đơn thực tế để thực hành đọc số liệu.

## Q\&A
- Cùng thảo luận: Nếu AI thay thế hoàn toàn việc nhập liệu, sinh viên kế toán mới ra trường nên làm gì để gia tăng giá trị bản thân trong mắt nhà tuyển dụng?
