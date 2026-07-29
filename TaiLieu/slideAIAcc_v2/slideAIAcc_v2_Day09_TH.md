# KẾ HOẠCH SLIDE THỰC HÀNH - DAY 09 (BUỔI 9)
**Tên bài:** Buổi 9 TH: Đánh giá Rủi ro và Tự động hóa KSNB với AI

### Mở đầu
## Title: Buổi 9 TH: Đánh giá Rủi ro và Tự động hóa KSNB.
    - Thực hành: Tái thiết kế Quy trình Kiểm soát với ChatGPT
    - Giảng viên: Đại học Đông Á
    - Môn học: Trí tuệ Nhân tạo cho Kế toán
## Năng lực đạt được sau buổi học.
    - **Về Kiến thức:** Nhận diện được các lỗ hổng kiểm soát phổ biến (thiếu phân nhiệm, thiếu phê duyệt) trong một quy trình kinh doanh thực tế.
    - **Về Kỹ năng:** Sử dụng thành thạo Prompt (đóng vai chuyên gia COSO) để yêu cầu AI rà soát văn bản quy trình, phát hiện rủi ro và tự động phác thảo lưu đồ kiểm soát mới.
    - **Về Tư duy:** Rèn luyện sự hoài nghi nghề nghiệp (Professional Skepticism) khi đối chiếu kết quả của AI với chuẩn mực COSO, không phụ thuộc hoàn toàn vào máy móc.
## Nội dung Chương trình (Agenda).
    - 1. Chuẩn bị Case Study: Quy trình Mua hàng \& Thanh toán.
    - 2. Đóng vai Chuyên gia COSO (Persona Prompting).
    - 3. Ứng dụng AI phân tích Lỗ hổng (Gap Analysis).
    - 4. Yêu cầu AI đề xuất Quy trình Mới (Process Re-design).
    - 5. Trình bày và Thảo luận Kết quả.

### Phần 1: Chuẩn bị Case Study
## Giới thiệu Tình huống (Case Study).
    - Bạn là Kiểm toán viên Nội bộ mới được tuyển dụng tại Công ty ABC.
    - Giám đốc yêu cầu bạn rà soát lại "Quy trình Mua hàng và Thanh toán" hiện tại của công ty vì có nghi ngờ thất thoát.
## Đọc Quy trình hiện tại (As-Is Process).
    - Giảng viên cung cấp: File văn bản `Purchasing_Process_ABC.txt`.
    - Văn bản này dài khoảng 2 trang, mô tả cách thức nhân viên yêu cầu mua hàng, liên hệ NCC, nhận hàng và kế toán thanh toán.
## Nhận diện thủ công (Manual Check).
    - Đọc lướt qua văn bản. Bạn có thấy điểm nào vô lý không?
    - Ví dụ: "Nhân viên mua hàng có quyền tự duyệt chi dưới 10 triệu đồng".
## Hạn chế của việc rà soát thủ công.
    - Dễ bỏ sót lỗi nếu quy trình quá dài và phức tạp (hàng trăm trang SOP).
    - Khó đối chiếu đầy đủ với 5 thành phần của COSO 2013 cùng lúc.
## Giải pháp: Trợ lý Kiểm toán AI.
    - Ta sẽ sử dụng ChatGPT (hoặc Claude) để quét toàn bộ văn bản và trích xuất ra các rủi ro cốt lõi.

### Phần 2: Đóng vai Chuyên gia COSO
## Kỹ thuật Persona Prompting.
    - Nếu bạn chỉ hỏi "Tìm lỗi trong quy trình này", AI sẽ trả lời chung chung.
    - Cần ép AI "đóng vai" một chuyên gia có kiến thức sâu về KSNB.
## Khởi tạo Persona (Prompt 1).
    - **Prompt:** "Từ bây giờ, hãy đóng vai một Chuyên gia Kiểm soát Nội bộ cấp cao, am hiểu sâu sắc về Khuôn khổ COSO 2013 và kiểm toán tài chính."
## Xác nhận từ AI.
    - Đảm bảo AI đã hiểu vai trò của mình. AI sẽ phản hồi: "Tôi đã sẵn sàng. Vui lòng cung cấp quy trình bạn muốn đánh giá."
## Cung cấp Ngữ cảnh (Context).
    - Nhập đoạn văn bản mô tả quy trình công ty ABC vào chat.
    - Lưu ý: Xóa bỏ các thông tin nhạy cảm thật (Tên thật, số tài khoản) trước khi đưa lên AI.
## Lệnh đánh giá tổng thể (Prompt 2).
    - **Prompt:** "Dưới đây là quy trình mua hàng hiện tại. Dựa trên 5 thành phần của COSO 2013, hãy phân tích quy trình này."

### Phần 3: Ứng dụng AI phân tích Lỗ hổng
## Yêu cầu Tìm Lỗ hổng (Prompt 3).
    - **Prompt:** "Hãy liệt kê 3 lỗ hổng kiểm soát (Control Weaknesses) nguy hiểm nhất trong quy trình trên. Giải thích tại sao chúng lại nguy hiểm."
## Đọc hiểu Kết quả của AI.
    - Lỗ hổng 1: Thiếu sự Phân nhiệm (Segregation of Duties).
    - Người đề xuất mua hàng lại cũng chính là người nhận hàng và lập phiếu nhập kho.
## Đọc hiểu Kết quả của AI (Tiếp).
    - Lỗ hổng 2: Thiếu bước Phê duyệt (Authorization).
    - Không có dấu kiểm duyệt của Kế toán trưởng trước khi chuyển tiền cho nhà cung cấp mới.
## Rủi ro Gian lận (Fraud Risk).
    - Yêu cầu AI chỉ ra kịch bản gian lận có thể xảy ra từ lỗ hổng 1.
    - (Nhân viên tự tạo nhà cung cấp "ma" và lập phiếu nhập kho khống để rút tiền).
## Đánh giá Rủi ro (Risk Matrix).
    - **Prompt:** "Hãy lập một bảng ma trận rủi ro (Risk Matrix) cho các lỗ hổng vừa tìm thấy, đánh giá mức độ Tác động (Impact) và Khả năng xảy ra (Likelihood)."
## Kiểm chứng chéo (Cross-check).
    - Sinh viên: Ma trận AI lập có hợp lý không? Lỗ hổng thiếu phê duyệt có thực sự là rủi ro "Cao" ở cả 2 mặt không?
## Hiện tượng Ảo giác (Hallucination).
    - Chú ý: Đôi khi AI tự bịa ra một bước không hề có trong văn bản (ví dụ: "Thủ quỹ không kiểm đếm" - trong khi quy trình mua hàng này chuyển khoản 100 phần trăm).

### Phần 4: Yêu cầu AI đề xuất Quy trình Mới
## Từ Bắt lỗi đến Kiến tạo.
    - Không chỉ tìm lỗi, Kế toán quản trị phải đưa ra giải pháp cải tiến (Process Re-design).
## Đề xuất Quy trình chuẩn COSO (Prompt 4).
    - **Prompt:** "Hãy thiết kế lại Quy trình mua hàng này để khắc phục toàn bộ các lỗ hổng trên, đảm bảo tính phân nhiệm nghiêm ngặt theo COSO 2013. Viết dưới dạng các bước (Step-by-step)."
## Phân tích Quy trình Mới.
    - Bước 1: Yêu cầu mua hàng $
ightarrow$ Bước 2: Phê duyệt (Trưởng bộ phận) $
ightarrow$ Bước 3: Đặt hàng (Phòng Mua hàng).
    - Bước 4: Nhận hàng (Thủ kho) $
ightarrow$ Bước 5: Thanh toán (Kế toán).
## Tự động hóa bằng AI (Prompt 5).
    - **Prompt:** "Trong quy trình mới này, bước nào có thể áp dụng AI (như OCR hoặc Machine Learning) để kiểm soát tự động? Gợi ý 2 ứng dụng."
## Ứng dụng Đối chiếu 3 chiều (3-Way Matching).
    - Khớp tự động: Đơn đặt hàng (PO) + Phiếu nhập kho (GRN) + Hóa đơn (Invoice).
## Biểu diễn Lưu đồ (Flowchart).
    - Kế toán thường dùng Visio/Draw.io để vẽ.
    - AI có thể viết mã Mermaid để vẽ lưu đồ tự động!
## Sử dụng mã Mermaid (Prompt 6).
    - **Prompt:** "Hãy viết mã Mermaid Diagram thể hiện quy trình mua hàng chuẩn COSO vừa thiết kế ở trên."
## Vẽ Lưu đồ với Mermaid.
    - Sinh viên copy đoạn code Mermaid từ ChatGPT.
    - Dán vào trình duyệt web `mermaid.live` để máy tự động sinh ra sơ đồ tư duy tuyệt đẹp.

### Phần 5: Trình bày và Thảo luận Kết quả
## Viết Báo cáo Kiểm toán Nội bộ.
    - Sau khi rà soát, bạn cần nộp báo cáo cho Ban giám đốc.
## Prompt tạo Báo cáo.
    - **Prompt:** "Dựa trên các phân tích nãy giờ, hãy viết một Báo cáo Kiểm toán Nội bộ (Audit Report) dài 300 chữ. Gồm 3 phần: Tóm tắt rủi ro hiện tại, Hậu quả có thể xảy ra, và Kiến nghị quy trình mới."
## Tính Chuyên nghiệp của Báo cáo.
    - Yêu cầu AI sử dụng văn phong học thuật, trang trọng (Professional/Formal tone).
## Bảo mật Dữ liệu khi dùng AI.
    - Thảo luận: Nếu công ty ABC là một tập đoàn niêm yết, việc đưa quy trình nội bộ lên ChatGPT có vi phạm tính bảo mật (Confidentiality) không?
## Giải pháp Bảo mật.
    - Xóa định danh (Anonymization).
    - Sử dụng AI doanh nghiệp (Enterprise AI) thay vì bản miễn phí.
## Bài học thực tế.
    - AI giúp Kiểm toán viên đi nhanh hơn từ việc "Tìm lỗi" đến việc "Thiết kế giải pháp". Tư duy hệ thống là chìa khóa.
## Bài tập về nhà & Q&A.
    - Bài tập: Dùng quy trình "Bán hàng và Thu tiền" (Giảng viên cấp). Hãy lặp lại quá trình dùng AI phân tích lỗ hổng và vẽ lưu đồ mới.
    - Kết thúc.
