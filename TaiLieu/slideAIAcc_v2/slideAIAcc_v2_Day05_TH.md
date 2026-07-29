# Kế hoạch Bài giảng Thực hành - Day 05 TH (Phiên bản v2)

**Chủ đề:** THỰC HÀNH: ỨNG DỤNG EXCEL & AI (PROMPT) ĐỂ QUÉT NHẬT KÝ CHUNG VÀ TÌM ĐIỂM BẤT THƯỜNG (OUTLIERS)
## Năng lực đạt được sau buổi học
- **Về Lý thuyết (LT):** Ôn tập và củng cố tư duy phát hiện điểm bất thường (Outliers) trong kế toán điều tra.
- **Về Thực hành (TH):** Sinh viên sử dụng thành thạo Conditional Formatting, Pivot Table trong Excel kết hợp với Prompt AI (ChatGPT/Copilot) để thiết lập các bẫy lỗi (red flags), nhận diện hóa đơn chẵn, ngày nghỉ, lệch thời gian và đối tượng sai sót trên một tập dữ liệu giả lập (Nhật ký chung).
- **Về Tư duy nghề nghiệp:** Rèn luyện kỹ năng hoài nghi nghề nghiệp, không quá phụ thuộc vào máy móc, biết cách kết hợp cảnh báo của AI với kiểm tra chứng từ kế toán gốc.
**Số lượng slide dự kiến:** 34 slide
---

## Phần 1: Giới thiệu Bài thực hành và Chuẩn bị dữ liệu (Slides 1 - 5)
## Tiêu đề: Trí tuệ Nhân tạo cho Kế toán - Buổi 5 (Thực hành): Dùng Excel & AI quét điểm bất thường.
## Năng lực đạt được sau buổi học (Về Lý thuyết, Thực hành và Tư duy nghề nghiệp).
## Kịch bản thực hành (Case Study): Bạn là một Kiểm toán viên nội bộ, được giao nhiệm vụ rà soát 5.000 dòng Sổ Nhật ký chung của Công ty X trong năm tài chính vừa qua.
## Các rủi ro (Red Flags) cần tìm kiếm: Giao dịch ngày nghỉ, Số tiền chẵn bất thường, Bút toán lệch thời gian, Đối tượng bất thường.
## Chuẩn bị file dữ liệu: Giảng viên cung cấp file Excel `NhatKyChung_Day05_Raw.xlsx` (có chứa sẵn các lỗi cố ý).

## Phần 2: Ôn tập Excel cốt lõi cho Kế toán điều tra (Slides 6 - 12)
## Tại sao lại dùng Excel? (Công cụ mạnh mẽ, tích hợp tốt với AI, dễ tùy biến).
## Ôn tập 1: Data Formatting. Định dạng cột Ngày tháng (Short Date), Số tiền (Number/Accounting).
## Ôn tập 2: Conditional Formatting. Cách bôi màu các ô thỏa mãn điều kiện nhất định.
## Ôn tập 3: Hàm WEEKDAY() trong Excel. Cách trích xuất thứ trong tuần từ cột Ngày tháng (1 = Chủ nhật, 7 = Thứ bảy).
## Ôn tập 4: Hàm MOD() trong Excel. Cách kiểm tra số tiền tròn chẵn (Ví dụ: chia hết cho 1.000.000).
## Ôn tập 5: Pivot Table cơ bản. Nhóm các giao dịch theo bộ phận/nhân viên để xem tổng chi tiêu.
## Checkpoint 1: Đảm bảo sinh viên nắm vững các hàm này trước khi kết hợp với AI.

## Phần 3: Ứng dụng Prompt AI để xây dựng quy tắc quét lỗi (Slides 13 - 19)
## Tư duy Prompt Engineering cho kế toán điều tra: Cung cấp vai trò, dữ liệu mẫu, và mục tiêu rõ ràng.
## Prompt 1: Yêu cầu AI viết công thức Conditional Formatting. 
    *   *Ví dụ:* "Tôi có cột B là Ngày ghi sổ. Hãy viết công thức Excel để làm nổi bật các dòng rơi vào Thứ Bảy hoặc Chủ Nhật."
## Thực hành 1: Copy công thức AI cung cấp vào Excel $\rightarrow$ Xem kết quả các hóa đơn cuối tuần "báo đỏ".
## Prompt 2: Tìm số tiền tròn chẵn bất thường (Smurfing/Phantom Bills).
    *   *Ví dụ:* "Tôi muốn tìm các hóa đơn chi phí tiếp khách có số tiền chẵn đến hàng triệu (VD: 5.000.000). Cột D là số tiền. Viết công thức Conditional Formatting."
## Thực hành 2: Áp dụng công thức MOD vào dữ liệu.
## Prompt 3: Nhận diện bất thường cục bộ (Local Outliers) bằng Pivot Table.
    *   *Ví dụ:* "Hướng dẫn tôi cách dùng Pivot Table để tìm nhân viên có chi phí mua văn phòng phẩm cao gấp 3 lần mức trung bình của phòng ban."
## Thực hành 3: Tạo Pivot Table theo hướng dẫn của AI.

## Phần 4: Phân tích Nâng cao bằng Data Analysis (Analyze Data) (Slides 20 - 25)
## Giới thiệu tính năng "Analyze Data" (Tích hợp AI) trên Excel 365.
## Cách thức hoạt động: Excel tự động tìm các "mẫu" (patterns) và "điểm bất thường" (outliers) mà không cần viết công thức.
## Thực hành 4: Bôi đen Sổ Nhật ký chung $\rightarrow$ Chọn Analyze Data.
## Khám phá kết quả: Đọc các biểu đồ tự động (Ví dụ: "Chi phí vận chuyển cao bất thường vào tháng 9").
## Kết hợp ChatGPT Plus/Advanced Data Analysis: Upload file CSV Sổ Nhật ký chung.
## Prompt 4: "Hãy đóng vai kiểm toán viên. Dùng thuật toán phát hiện bất thường để quét file dữ liệu này và báo cáo top 10 giao dịch đáng ngờ nhất."

## Phần 5: Giải quyết tình huống và Lập báo cáo kiểm soát (Slides 26 - 31)
## Review kết quả quét: Có phải tất cả các "Red Flags" đều là gian lận? (False Positives).
## Bài tập nhóm: Mỗi nhóm sinh viên chọn ra 3 giao dịch bị "báo đỏ".
## Kỹ năng phỏng vấn/đối chiếu: Bạn sẽ yêu cầu những chứng từ gì để xác minh 3 giao dịch này? (Hóa đơn GTGT, Phiếu xuất kho, Lệnh chi...).
## Nếu phát hiện gian lận thật sự (VD: chia nhỏ hóa đơn để trốn ký duyệt), kế toán viên cần làm gì?
## Viết báo cáo tóm tắt: Trình bày bảng danh sách các giao dịch bất thường lên Ban Giám đốc (Sử dụng biểu đồ từ Pivot Table).
## Đánh giá độ hiệu quả của phương pháp AI + No-code so với làm thủ công.

## Phần 6: Tổng kết và Q&A (Slides 32 - 34)
## Tóm tắt kiến thức thực hành cốt lõi: Kết hợp Excel truyền thống và Prompt AI tạo ra sức mạnh vượt trội.
## Lưu ý về bảo mật: Không upload dữ liệu thật, chưa mã hóa (Unmasked data) lên ChatGPT công khai.
## Q&A - Hỏi đáp và Hướng dẫn nộp bài tập thực hành.
