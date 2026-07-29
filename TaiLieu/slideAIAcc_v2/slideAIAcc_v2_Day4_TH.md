# KẾ HOẠCH SLIDE THỰC HÀNH - DAY 4 (BUỔI 4)
**Tên bài:** THỰC HÀNH AI TRONG KẾ TOÁN CHI TIẾT - KỸ THUẬT PERSONA
**Định hướng:** Thực hành sử dụng ChatGPT/Copilot thông qua kỹ thuật thiết lập "Persona" (Đóng vai) để xử lý các công việc kế toán chi tiết: Định khoản, phân bổ chi phí, quản lý lịch trình và giao tiếp với khách hàng.
**Cấu trúc:** 32 Slides.

**ĐỀ XUẤT NGUỒN ẢNH MINH HỌA:**
- **Chụp ảnh màn hình (Screenshot):** Giao diện ChatGPT đóng vai Kế toán trưởng; Giao diện AI lên lịch trình (Scheduling); Prompt phân bổ chi phí.
- **Sinh ảnh bằng AI:** Hình ảnh một con robot đang mặc vest, đeo kính giống một vị Kế toán trưởng khó tính.

---

# PHẦN 1: MỤC TIÊU VÀ CHUẨN BỊ (SETTING THE STAGE)

## TRANG BÌA (Title Page)
- Tiêu đề chính: Thực hành Trí tuệ Nhân tạo cho Kế toán
- Tiêu đề phụ: Buổi 4 - Thực hành Thiết lập Persona \& Trợ lý Kế toán AI
- Tác giả: Đại học Đông Á
- *(🖼️ Ảnh minh họa: AI Generated - Một robot AI mặc vest, ngồi trước máy tính với bảng tính Excel và logo ChatGPT).*

## Năng lực đạt được sau buổi học
- **Về Lý thuyết (LT):** Củng cố kiến thức về nguyên lý kế toán và các bước trong chu trình kế toán để làm cơ sở đánh giá kết quả đầu ra của AI.
- **Về Thực hành (TH):** Thành thạo kỹ thuật thiết lập "Persona" (Đóng vai) cho AI; Biết cách sử dụng Prompt để yêu cầu AI định khoản các nghiệp vụ kinh tế phát sinh lộn xộn; Có khả năng đối chiếu và so sánh kết quả định khoản bằng AI với phương pháp thủ công.
- **Về Tư duy nghề nghiệp:** Nâng cao tư duy hoài nghi nghề nghiệp, không tin tưởng mù quáng vào kết quả của AI mà luôn có bước kiểm chứng (Cross-check) dựa trên nền tảng chuyên môn kế toán vững chắc.

## Trích dẫn truyền cảm hứng
- *"Trong thời đại AI, làm kế toán không chỉ là lướt qua các bảng tính sổ cái; mà là đón nhận và điều hướng làn sóng của cuộc cách mạng kỹ thuật số."*
- \textit{(Dr. Martijn van Otterlo - Đại học Tilburg)}
- Kế toán không bị đào thải, chỉ những người không biết dùng AI mới bị đào thải.

## Chuẩn bị môi trường (Setting the stage)
- **Công cụ cần có:** 
  - Trình duyệt Web hiện đại (Chrome/Edge).
  - Tài khoản OpenAI (ChatGPT) hoặc Microsoft Copilot.
  - Kết nối Internet ổn định.
- **Tư duy:** Sẵn sàng giao tiếp với máy móc như một người đồng nghiệp.

## Tại sao AI cần có "Nhân dạng" (Persona)?
- Khi bạn hỏi ChatGPT một câu bình thường, nó sẽ trả lời theo kiểu "Bách khoa toàn thư", rất chung chung.
- Trong kế toán, mỗi vị trí (Kế toán thuế, Kế toán trưởng, Kiểm toán viên) có cách tư duy và quy chuẩn pháp lý khác nhau.
- \textbf{Kỹ thuật Persona (Đóng vai):} Buộc AI phải tư duy trong giới hạn nghề nghiệp cụ thể.

---

# PHẦN 2: KỸ THUẬT THIẾT LẬP PERSONA CHO AI

## Kỹ thuật Persona là gì?
- Persona (Nhân dạng) là việc cung cấp cho AI một vai trò cụ thể trước khi giao việc.
- \textbf{Công thức Prompt Persona:}
  - *Đóng vai (Act as):* Bạn là ai?
  - *Mục tiêu (Goal):* Bạn cần giải quyết vấn đề gì?
  - *Bối cảnh (Context):* Quy định/Luật áp dụng là gì?
  - *Định dạng (Format):* Trả kết quả dưới dạng nào (Bảng, gạch đầu dòng)?

## Xây dựng Persona "Kế toán trưởng"
- \textbf{Prompt Mẫu:} *"Hãy đóng vai một Kế toán trưởng với 15 năm kinh nghiệm tại Việt Nam. Bạn nắm rất rõ Thông tư 200/2014/TT-BTC. Nhiệm vụ của bạn là kiểm tra các nghiệp vụ kế toán tôi đưa ra, chỉ ra lỗi sai (nếu có) và hướng dẫn định khoản chính xác. Hãy luôn trích dẫn cơ sở pháp lý (điều khoản) cho các quyết định của bạn."*

## Hệ quả của việc dùng Persona
- \textbf{Không có Persona:} AI trả lời ngắn gọn: Nợ 642, Có 111.
- \textbf{Có Persona Kế toán trưởng:} AI sẽ phân tích: *"Theo TT200, chi phí này phục vụ quản lý doanh nghiệp nên hạch toán vào TK 642. Nếu thanh toán bằng tiền mặt, ghi Có 111. Tuy nhiên, lưu ý hóa đơn trên 20 triệu đồng phải thanh toán không dùng tiền mặt để được khấu trừ thuế..."*
- Sự khác biệt là cực kỳ lớn!

---

# PHẦN 3: THỰC HÀNH 1 - AI LÀM "KẾ TOÁN THANH TOÁN"

## Tình huống Thực hành 1
- Công ty bạn vừa mua một phần mềm Kế toán trị giá 60.000.000đ (chưa gồm 10\% VAT), thanh toán bằng chuyển khoản. Thời gian sử dụng dự kiến là 3 năm.
- \textbf{Yêu cầu:} Dùng ChatGPT (đã thiết lập Persona Kế toán trưởng) để định khoản nghiệp vụ mua phần mềm và bút toán phân bổ tháng đầu tiên.

## Nhập Prompt cho Tình huống 1
- Cả lớp copy tình huống trên và dán vào ChatGPT.
- Quan sát cách AI xử lý \textbf{Tài khoản 242 (Chi phí trả trước)} thay vì đưa thẳng vào Chi phí trong kỳ.

## Đánh giá Kết quả của AI
- AI có chỉ ra được số tiền VAT là 6.000.000đ không?
- Phân bổ tháng đầu tiên: 60 triệu / (3 * 12 tháng) = 1.666.667đ.
- Bút toán phân bổ: Nợ TK 642 / Có TK 242 số tiền 1.666.667đ.
- *(🖼️ Ảnh minh họa: Ảnh chụp màn hình kết quả trả lời của ChatGPT).*

## Tình huống "Mẹo" (Trick Question)
- Thử kiểm tra AI bằng một nghiệp vụ sai luật.
- \textbf{Prompt:} *"Sếp tôi vừa dùng quỹ tiền mặt của công ty (TK 111) để mua một chiếc xe máy SH giá 100 triệu cho con gái sếp đi học. Hãy định khoản."*
- Xem AI "Kế toán trưởng" phản ứng thế nào với giao dịch không phục vụ mục đích kinh doanh!

## Xử lý Tình huống Mẹo
- AI chuẩn sẽ \textbf{từ chối} ghi nhận đây là tài sản công ty (TK 211).
- AI sẽ gợi ý hạch toán vào Phải thu khác (Nợ 1388) hoặc trừ vào Lương/Cổ tức của Giám đốc, vì đây là chi tiêu cá nhân, không được tính vào chi phí hợp lý.

---

# PHẦN 4: THỰC HÀNH 2 - PHÂN BỔ CHI PHÍ \& DỰ BÁO

## AI trong Kế toán Quản trị
- Kế toán quản trị cần các quyết định phân bổ chi phí (Cost Allocation) và dự báo dòng tiền (Financial Forecasting).
- Sự phức tạp nằm ở việc có quá nhiều biến số thay đổi.

## Tình huống Thực hành 2 (Phân bổ chi phí)
- Doanh nghiệp sản xuất có hóa đơn tiền điện 120.000.000đ dùng chung cho 3 phân xưởng.
- Dữ liệu: Phân xưởng 1 (1.000 giờ máy), Phân xưởng 2 (1.500 giờ máy), Phân xưởng 3 (2.500 giờ máy).
- \textbf{Yêu cầu:} Đổi Persona AI thành "Kế toán Quản trị", yêu cầu lập bảng phân bổ tiền điện theo giờ máy hoạt động.

## Nhập Prompt \& Lấy kết quả
- \textbf{Prompt thêm:} *"Hãy trình bày kết quả dưới dạng Bảng (Table), bao gồm các cột: Tên Phân Xưởng, Giờ Máy, Tỷ lệ \%, Số tiền phân bổ."*
- AI không chỉ tính toán đúng mà còn format thành bảng rất đẹp, sẵn sàng copy vào Excel.

## Sự tiến hóa của Dự báo Tài chính (Financial Forecasting)
- Phương pháp cũ: Dựa vào Excel, kéo công thức xu hướng (Trendline). Rất thụ động.
- AI hiện đại (Deep Learning): Nhận diện mô hình, bất thường, và yếu tố bên ngoài.
- Chuyển từ "Dự báo tuyến tính" sang "Dự báo đa chiều".

## Tình huống Dự báo cơ bản với ChatGPT
- \textbf{Prompt:} *"Doanh thu 6 tháng đầu năm của công ty theo thứ tự là: 10, 12, 11, 15, 18, 20 tỷ. Ngân sách marketing hàng tháng là: 1, 1, 1.2, 1.5, 2, 2.5 tỷ. Tháng tới tôi dự định cắt giảm marketing còn 1 tỷ, hãy dự báo doanh thu tháng 7 và giải thích lý do."*

## Phân tích kết quả Dự báo của AI
- AI sẽ nhận thấy mối tương quan (Correlation) chặt chẽ giữa Ngân sách marketing và Doanh thu.
- AI sẽ cảnh báo sự sụt giảm doanh thu mạnh nếu cắt giảm marketing đột ngột, chứ không đơn thuần chỉ tính trung bình cộng như Excel.

---

# PHẦN 5: QUẢN LÝ QUAN HỆ KHÁCH HÀNG (CLIENT RELATIONSHIPS)

## Kế toán đâu chỉ có những con số?
- Quản lý công việc (Practice Management) đòi hỏi giao tiếp nhiều với đối tác, khách hàng, nhà cung cấp.
- Đặc biệt là các tình huống tế nhị: Đòi nợ, xin gia hạn nợ, giải thích sai sót hóa đơn.

## Nâng tầm quan hệ với AI
- Khách hàng mong muốn sự phản hồi tức thì, cá nhân hóa.
- NLP (Xử lý ngôn ngữ tự nhiên) giúp AI đọc hiểu sắc thái cảm xúc trong email của khách hàng (đang giận dữ, phàn nàn hay bình thường).
- AI có thể soạn thảo các email chuyên nghiệp, giữ vững mối quan hệ (Client Relationships).

## Thực hành 3 - Viết Email Khó (Drafting Emails)
- \textbf{Tình huống:} Một khách hàng VIP (Công ty XYZ) đã trễ hạn thanh toán 45 ngày số tiền 500 triệu. Bạn đã gọi điện 2 lần nhưng họ đều hứa lèo.
- \textbf{Yêu cầu:} Dùng ChatGPT soạn một email nhắc nợ. Yêu cầu văn phong: Lịch sự nhưng kiên quyết, đề cập đến việc sẽ tính lãi chậm trả nếu không thanh toán trong 3 ngày tới.

## Tùy chỉnh Email với Persona
- Bạn có thể nói với ChatGPT: *"Email này hơi gay gắt, hãy làm cho nó mềm mỏng hơn một chút để không mất lòng khách hàng, thêm lời chúc sức khỏe vào đầu thư."*
- Khả năng tùy chỉnh ngôn từ (Tone \& Voice) của AI là không có giới hạn.

## AI trong Lên lịch trình (Scheduling)
- Một trợ lý AI có thể tích hợp vào Calendar để tự động xếp lịch họp.
- Loại bỏ cảnh gửi qua gửi lại 5 cái email chỉ để chốt giờ họp.
- "Tiết kiệm thời gian (Time savings) là lợi ích lớn nhất của AI trong quản lý hành chính Kế toán."

---

# PHẦN 6: KIỂM SOÁT VÀ SOÁT XÉT (INTERNAL CONTROLS IN PRACTICE)

## AI trong vai trò Kiểm soát viên (Auditor)
- Thiết lập Persona mới: "Kiểm toán viên Nội bộ".
- Nhiệm vụ: Phát hiện điểm bất thường (Anomaly detection) trong tập dữ liệu.

## Thực hành 4 - Tìm điểm bất thường
- Giáo viên cung cấp một đoạn trích Sổ quỹ Tiền mặt (dạng text/bảng).
- Trong đó cài cắm 1 giao dịch: *Ngày Chủ nhật, 10:00 Tối - Rút tiền mặt 50 triệu - Nội dung: Tạm ứng cho Giám đốc.*
- \textbf{Yêu cầu sinh viên:} Đưa đoạn dữ liệu này cho ChatGPT và hỏi *"Có rủi ro kiểm soát nội bộ nào trong các giao dịch này không?"*

## Nhận diện Cờ đỏ (Red Flags)
- AI sẽ lập tức báo cờ đỏ (Red Flag):
  1. Giao dịch rút tiền mặt số lượng lớn vào ngày nghỉ (Chủ nhật).
  2. Giao dịch diễn ra ngoài giờ hành chính (10:00 Tối).
  3. Quỹ tiền mặt không hoạt động giờ đó $\rightarrow$ Rủi ro biển thủ hoặc ghi khống.

## Tổng kết sức mạnh của Persona
- Không có AI giỏi nhất, chỉ có người viết Prompt giỏi nhất.
- Bằng cách thay đổi Persona (Kế toán thanh toán $\rightarrow$ Kế toán quản trị $\rightarrow$ Kiểm toán viên), bạn biến ChatGPT thành một \textbf{Phòng Kế toán ảo} với đầy đủ nhân sự.

## Rủi ro bảo mật dữ liệu (Data Privacy)
- \textbf{CẢNH BÁO ĐỎ:} Tuyệt đối KHÔNG đưa thông tin thật của khách hàng, số tài khoản thật, tên thật của công ty lên ChatGPT bản miễn phí.
- AI sẽ dùng dữ liệu đó để huấn luyện mô hình (Training). Hãy luôn ẩn danh hóa dữ liệu (Anonymize data) trước khi dùng AI.

## Bài tập về nhà (Assignment)
- Dùng ChatGPT (Persona Kế toán trưởng) định khoản một danh sách gồm 10 nghiệp vụ kinh tế phát sinh phức tạp (Giáo viên cung cấp).
- Xuất kết quả ra file Excel và nộp lại trên hệ thống trường.

## Tóm tắt Buổi Thực hành
- \textbf{Persona:} Chìa khóa để mở khóa tư duy chuyên ngành của AI.
- \textbf{Định khoản \& Phân bổ:} AI tính toán nhanh và format bảng biểu đẹp mắt.
- \textbf{Giao tiếp:} AI là trợ thủ đắc lực soạn email, xử lý khủng hoảng truyền thông với khách hàng.

## Q\&A \& Hỗ trợ
- Sinh viên gặp lỗi khi Prompt?
- AI trả lời sai (Hallucination)? \textit{Cách khắc phục: Cung cấp thêm Context (Thông tư, luật) vào Prompt để nắn lại tư duy của AI.}
- Chúc các bạn làm chủ "Phòng kế toán ảo" của riêng mình!
