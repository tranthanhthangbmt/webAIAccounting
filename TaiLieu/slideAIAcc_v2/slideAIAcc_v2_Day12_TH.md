---
theme: "default"
title: "Day 12 TH: Thực hành Đạo đức và Pháp lý khi ứng dụng AI"
author: "Giảng viên"
date: "2026"
---

# BUỔI 12: THỰC HÀNH ĐẠO ĐỨC KẾ TOÁN VÀ PHÁP LÝ KHI ỨNG DỤNG AI

## Năng lực đạt được sau buổi học
- **Xây dựng Quy tắc Ứng xử (Code of Conduct):** Biết cách soạn thảo và triển khai một Bộ quy tắc Ứng xử AI phù hợp với đặc thù của doanh nghiệp kế toán.
- **Ẩn danh hóa dữ liệu (Data Anonymization):** Sử dụng các công cụ AI và phần mềm (Power Query/Python) để làm sạch và ẩn danh hóa dữ liệu nhạy cảm trước khi đưa lên nền tảng đám mây (Cloud).
- **Kiểm định Thiên kiến:** Thực hành rà soát, phát hiện và xử lý các thiên kiến thuật toán trong các mô hình AI dự báo tài chính đơn giản.
- **Tuân thủ quy định:** Áp dụng nguyên tắc "Con người làm chủ" trong quy trình kiểm duyệt (validation) các báo cáo do AI sinh ra.

## Nội dung chương trình
1. Tổng quan về Thực hành AI có đạo đức trong kế toán.
2. Bài tập 1: Xây dựng Bộ quy tắc Ứng xử AI (AI Code of Conduct).
3. Bài tập 2: Kỹ thuật ẩn danh hóa dữ liệu (Anonymization Techniques).
4. Bài tập 3: Phát hiện và xử lý Thiên kiến Thuật toán (Bias Mitigation).
5. Thực hành đánh giá Rủi ro và Trách nhiệm pháp lý.
6. Tổng kết và Q&A.

---

# PHẦN 1: TỔNG QUAN VỀ THỰC HÀNH AI CÓ ĐẠO ĐỨC

## 1.1 Tình huống khởi động (Icebreaker)
- Hãy tưởng tượng bạn là Giám đốc Tài chính (CFO) của một công ty.
- Nhân viên của bạn đã đưa toàn bộ danh sách khách hàng và báo cáo lương chưa mã hóa lên ChatGPT để tóm tắt.
- Câu hỏi: Hệ lụy gì có thể xảy ra? Công ty sẽ phải đối mặt với những rủi ro pháp lý nào?

## 1.2 Tại sao cần Bộ quy tắc Ứng xử AI?
- AI không tự phân biệt được "đúng" hay "sai" về mặt đạo đức.
- Kế toán viên cần một kim chỉ nam rõ ràng để biết cái gì được phép và không được phép khi dùng AI.
- Giúp tổ chức quản trị rủi ro và tuân thủ các quy định bảo vệ dữ liệu hiện hành (ví dụ: GDPR, Luật An ninh mạng).

## 1.3 Mục tiêu của buổi thực hành
- Chuyển hóa các lý thuyết về Đạo đức và Pháp lý (từ buổi học trước) thành các quy trình thực tiễn (SOPs).
- Rèn luyện kỹ năng tự bảo vệ bản thân và khách hàng khi thao tác với dữ liệu nhạy cảm trên môi trường AI.

---

# PHẦN 2: BÀI TẬP 1 - XÂY DỰNG AI CODE OF CONDUCT

## 2.1 Yêu cầu Bài tập 1
- **Nhiệm vụ:** Viết một "Bản nháp Bộ quy tắc Ứng xử AI" cho một Công ty Dịch vụ Kế toán ABC.
- **Công cụ:** Sử dụng ChatGPT hoặc Claude để hỗ trợ soạn thảo, nhưng bạn phải là người tinh chỉnh và quyết định cấu trúc cuối cùng.
- **Thời gian:** 20 phút.

## 2.2 Các yếu tố bắt buộc trong Bộ quy tắc
- **Mục đích:** Tại sao công ty lại cần tài liệu này?
- **Phạm vi áp dụng:** Áp dụng cho những phần mềm AI nào? (Ví dụ: ChatGPT, Copilot, OCR AI).
- **Nguyên tắc cốt lõi:** Minh bạch (Transparency), Công bằng (Fairness), và Con người làm chủ (Human-in-the-loop).

## 2.3 Quy định về Bảo mật Dữ liệu
- Dữ liệu nào **tuyệt đối cấm** đưa vào các nền tảng AI công cộng (Public AI)?
- Quy trình phê duyệt trước khi sử dụng một công cụ AI mới là gì?
- Hình thức xử lý kỷ luật nếu nhân viên vi phạm quy định bảo mật.

## 2.4 Prompt mẫu để soạn thảo
- "Act as a Chief Compliance Officer in an accounting firm. Draft a concise 1-page AI Code of Conduct focusing on data privacy, human oversight, and algorithmic bias. Keep it professional but easy to understand for all accountants."

## 2.5 Thực hành soạn thảo
- Học viên tiến hành chạy prompt trên ChatGPT.
- So sánh kết quả AI sinh ra với yêu cầu thực tế của các doanh nghiệp kế toán Việt Nam.
- Điều chỉnh ngôn từ cho phù hợp với văn hóa công sở (Tone of voice).

## 2.6 Đánh giá chéo (Peer Review)
- Trình bày tóm tắt Bộ quy tắc của bạn trước lớp.
- Thảo luận: Điều khoản nào là khó tuân thủ nhất trong thực tế? Tại sao?

---

# PHẦN 3: BÀI TẬP 2 - ẨN DANH HÓA DỮ LIỆU (ANONYMIZATION)

## 3.1 Khái niệm Ẩn danh hóa Dữ liệu
- Ẩn danh hóa (Data Anonymization) là quá trình xóa bỏ hoặc sửa đổi các thông tin định danh cá nhân (PII) từ một bộ dữ liệu.
- Đảm bảo rằng không ai có thể truy nguyên dữ liệu đó thuộc về tổ chức hay cá nhân nào.

## 3.2 Các cấp độ làm sạch dữ liệu
- **Level 1 (Xóa bỏ):** Xóa hoàn toàn các cột chứa Tên, CMND/CCCD, Số điện thoại.
- **Level 2 (Mã hóa/Masking):** Thay thế tên "Nguyễn Văn A" thành "Khách hàng 001", hoặc chỉ giữ lại 4 số cuối của thẻ tín dụng.
- **Level 3 (Khái quát hóa/Generalization):** Thay vì để địa chỉ chính xác, chỉ để lại "Khu vực Miền Nam".

## 3.3 Yêu cầu Bài tập 2
- Cho một file Excel `Payroll_Data_Raw.xlsx` chứa danh sách lương nhân viên (Gồm: Họ tên, Email, Số TK Ngân hàng, Mức lương).
- **Nhiệm vụ:** Sử dụng tính năng Find & Replace hoặc Power Query để ẩn danh hóa hoàn toàn dữ liệu trước khi nhờ AI phân tích quỹ lương.

## 3.4 Thực hành bằng Power Query
- Bước 1: Load dữ liệu vào Power Query Editor.
- Bước 2: Chọn các cột PII (Họ tên, Email, Số TK).
- Bước 3: Sử dụng chức năng "Remove Columns" đối với dữ liệu không cần thiết.

## 3.5 Sử dụng hàm Hash (Nâng cao)
- Nếu cần theo dõi biến động lương của cùng một người qua các tháng mà không muốn lộ tên.
- Sử dụng hàm băm (Hashing) hoặc tạo một Index cột (ID_1, ID_2) để thay thế cho tên thật.

## 3.6 Sử dụng AI để rà soát dữ liệu PII
- Có thể viết một đoạn script Python đơn giản hoặc nhờ AI (nếu dùng trên môi trường Private) quét file để cảnh báo nếu còn sót dữ liệu cá nhân.
- Prompt: "Check this dataset schema and flag any columns that might contain Personally Identifiable Information (PII)." (Chỉ gửi Headers, không gửi Data).

## 3.7 Kiểm tra kết quả
- Đảm bảo file sau khi ẩn danh hóa vẫn giữ được tính toàn vẹn về mặt số liệu tài chính để AI có thể phân tích (ví dụ: tính trung bình, phân bổ).
- Rút ra bài học: "Đừng bao giờ gửi file raw lên Cloud".

---

# PHẦN 4: BÀI TẬP 3 - PHÁT HIỆN THIÊN KIẾN THUẬT TOÁN

## 4.1 Hiểu về Thiên kiến trong Dữ liệu Kế toán
- Thiên kiến (Bias) thường ẩn sâu trong dữ liệu lịch sử.
- Ví dụ: Một mô hình AI chấm điểm tín dụng có thể tự động từ chối khoản vay của các doanh nghiệp siêu nhỏ chỉ vì trong quá khứ, tỷ lệ nợ xấu của nhóm này (do ngoại cảnh) hơi cao.

## 4.2 Yêu cầu Bài tập 3
- Đọc một tình huống giả định (Case Study) về một hệ thống AI duyệt chi phí công tác tự động.
- Hệ thống liên tục từ chối các hóa đơn khách sạn của nhân viên nữ nhưng lại duyệt cho nhân viên nam với cùng mức chi phí.
- **Nhiệm vụ:** Đóng vai Kiểm toán viên Công nghệ, tìm ra nguyên nhân của sự thiên lệch này.

## 4.3 Phân tích nguyên nhân (Root Cause Analysis)
- Xem xét bộ dữ liệu huấn luyện (Training Data): Có thể dữ liệu lịch sử chủ yếu là của các lãnh đạo nam (đi công tác nhiều), dẫn đến AI "học" sai lệch.
- Xem xét biến số (Variables): Hệ thống có vô tình sử dụng "Giới tính" làm một biến quyết định không?

## 4.4 Thực hành khắc phục (Mitigation)
- Làm thế nào để sửa lỗi này?
- Bước 1: Loại bỏ biến "Giới tính" khỏi mô hình ra quyết định.
- Bước 2: Đảm bảo bộ dữ liệu huấn luyện cân bằng (Balanced Data) giữa các nhóm nhân viên.
- Bước 3: Đưa "Con người" vào vòng lặp (Human-in-the-loop) để duyệt lại các trường hợp bị AI từ chối.

## 4.5 Sử dụng công cụ kiểm định (Fairness Check)
- Giới thiệu ngắn gọn các công cụ như IBM AI Fairness 360 (Khái niệm).
- Đối với kế toán, cách tốt nhất là "Sample Testing": Lấy ngẫu nhiên 100 kết quả bị từ chối và tự kiểm tra tay để xem có quy luật phân biệt đối xử nào không.

---

# PHẦN 5: ĐÁNH GIÁ RỦI RO & TRÁCH NHIỆM PHÁP LÝ

## 5.1 Quy trình Đánh giá Rủi ro AI (AI Risk Assessment)
- Trước khi mua hoặc triển khai một phần mềm AI kế toán, cần lập bảng đánh giá rủi ro.
- Thực hành: Điền vào mẫu "Bảng kiểm (Checklist) Rủi ro AI".

## 5.2 Các tiêu chí trong Bảng kiểm
- Tính bảo mật: Dữ liệu được lưu trữ ở đâu? (Data Residency).
- Quyền sở hữu: Ai sở hữu dữ liệu đầu ra do AI tạo ra?
- Tính minh bạch: Vendor (nhà cung cấp) có giải thích được thuật toán của họ không?

## 5.3 Trách nhiệm pháp lý của Kế toán viên
- Thảo luận nhóm: Nếu phần mềm AI phân tích sai dẫn đến nộp sai thuế, Kế toán viên có thoát được trách nhiệm không?
- Kết luận: KHÔNG. "AI calculates, but humans sign". Kế toán viên chịu trách nhiệm cuối cùng.

## 5.4 Lập Kế hoạch Ứng phó Sự cố (Incident Response Plan)
- Khi phát hiện rò rỉ dữ liệu hoặc lỗi AI nghiêm trọng, cần làm gì đầu tiên?
- Các bước: Cách ly hệ thống AI -> Báo cáo cấp quản lý/IT -> Thông báo cho khách hàng (nếu cần thiết theo luật) -> Tìm nguyên nhân và khắc phục.

---

# PHẦN 6: TỔNG KẾT VÀ Q&A

## 6.1 Tổng kết Bài thực hành
- Bộ quy tắc ứng xử AI là lá chắn đầu tiên bảo vệ đạo đức nghề nghiệp.
- Kỹ năng Ẩn danh hóa dữ liệu (Data Anonymization) là bắt buộc đối với mọi kế toán viên hiện đại.
- Luôn giữ thái độ "Hoài nghi nghề nghiệp" (Professional Skepticism) trước mọi kết quả của AI để tránh thiên kiến.

## 6.2 Q&A (Hỏi đáp)
- Học viên đặt câu hỏi về các vướng mắc trong việc áp dụng AI an toàn.
- Thảo luận các tình huống thực tế tại doanh nghiệp của học viên.

## 6.3 Bài tập về nhà
- Hoàn thiện Bộ quy tắc Ứng xử AI của riêng bạn.
- Chuẩn bị một file dữ liệu (dummy data) và áp dụng các phương pháp ẩn danh hóa đã học để tạo ra một bộ dữ liệu sạch.

## CẢM ƠN CÁC BẠN ĐÃ THAM GIA!
- Kết thúc phần Thực hành Day 12.
- "Trở thành người sử dụng AI thông minh, đạo đức và tuân thủ pháp luật".
