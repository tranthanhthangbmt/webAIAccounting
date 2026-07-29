# Kế hoạch Bài giảng Lý thuyết - Day 05 (Phiên bản v2)

**Chủ đề:** AI PHÁT HIỆN SAI SÓT VÀ CHẨN ĐOÁN BẤT THƯỜNG KẾ TOÁN (Forensic Accounting & Outlier Detection)
## Năng lực đạt được sau buổi học
- **Về Lý thuyết (LT):** Hiểu được bản chất của sai sót/gian lận (Outliers) và cách AI (như LOF) tự động khoanh vùng rủi ro thay cho kiểm tra chọn mẫu.
- **Về Thực hành (TH):** Ứng dụng thành thạo Excel (Conditional Formatting) và Power BI kết hợp Prompt AI để quét Sổ Nhật ký chung, phát hiện nhanh các giao dịch đáng ngờ (sai lệch ngày tháng, số tiền chẵn...).
- **Về Tư duy nghề nghiệp:** Hình thành sự "hoài nghi nghề nghiệp", hiểu được giới hạn của AI (báo động giả) và trách nhiệm kiểm chứng của kế toán viên.
**Số lượng slide dự kiến:** 41 slide
---

## Phần 1: Kế toán điều tra và Sự can thiệp của AI (Slides 1 - 8)
## Tiêu đề: Trí tuệ Nhân tạo cho Kế toán - Buổi 5: AI Phát hiện sai sót \& Chẩn đoán bất thường.
## Mục tiêu bài học (Hiểu về Kế toán điều tra, Nhận diện Outlier, Ứng dụng AI phát hiện gian lận).
## Kế toán điều tra (Forensic Accounting) là gì? Khái niệm như những "Thám tử tài chính".
## Các loại gian lận phổ biến trong doanh nghiệp (Rút ruột công quỹ, Lạm dụng thẻ tín dụng công ty, Trốn thuế).
## Hậu quả của gian lận tài chính (Thống kê thiệt hại kinh tế toàn cầu hàng năm).
## Phương pháp rà soát thủ công truyền thống: Tốn thời gian, dễ bỏ sót.
## Vai trò của Machine Learning/AI trong Kế toán điều tra.
## Tự động hóa: Từ việc kiểm tra ngẫu nhiên (Sampling) sang kiểm tra toàn bộ 100% dữ liệu.

## Phần 2: Hiểu về "Điểm bất thường" (Outliers) (Slides 9 - 16)
## Điểm bất thường (Outliers) là gì?
## Sự khác biệt giữa Outliers (bất thường có ý nghĩa) và Noise (Nhiễu ngẫu nhiên).
## Tại sao Outlier lại quan trọng trong Kế toán? (Đó thường là dấu hiệu của sai sót hoặc gian lận).
## Ví dụ về Outlier: Một nhân viên thường xuyên chi tiêu tiếp khách 20 triệu/tháng bỗng dưng thanh toán hóa đơn 500 triệu.
## Phương pháp nhận diện toàn cục (Global Outlier Detection) - Phương pháp 3 độ lệch chuẩn (3SD Rule).
## Hạn chế của phương pháp toàn cục trong dữ liệu tài chính đa chiều.
## Khái niệm Phương pháp nhận diện cục bộ (Local Outlier Detection).
## Ưu điểm của nhận diện cục bộ: Tìm ra điểm bất thường so với "môi trường xung quanh" nó.

## Phần 3: Trực giác về thuật toán LOF (Local Outlier Factor) (Slides 17 - 25)
## Thuật toán LOF (Local Outlier Factor) là gì? Giải thích bằng trực giác (Không code).
## Ví dụ trực quan: Ngôi nhà trong thung lũng vs Ngôi nhà trên đỉnh núi.
## Định nghĩa "Hàng xóm" (Neighbors) trong dữ liệu kế toán (Ví dụ: Các giao dịch có tính chất tương đồng).
## Khoảng cách Reachability (Reachability Distance) - Đo lường bán kính vùng lân cận.
## Mật độ cục bộ (Local Reachability Density - LRD) - Nơi nào đông đúc, nơi nào thưa thớt?
## Cách AI tính toán chỉ số LOF để chấm điểm rủi ro cho từng giao dịch.
## Phân tích điểm số LOF: Điểm số cao cảnh báo rủi ro cao (Red Flag).
## Ứng dụng LOF vào phát hiện gian lận thẻ tín dụng doanh nghiệp.
## So sánh hiệu quả của LOF so với việc thiết lập luật (Rule-based) thông thường.

## Phần 4: Phát hiện gian lận với AI và No-code (Slides 26 - 34)
## Làm thế nào để áp dụng AI mà không cần viết code?
## Sử dụng các công cụ tích hợp sẵn AI: Excel (Analyze Data) và Power BI (Anomaly Detection).
## Quy trình chuẩn bị dữ liệu cho AI rà soát: Dọn dẹp dữ liệu (Data Cleansing).
## Cung cấp bối cảnh cho AI: Prompt hướng dẫn ChatGPT/Copilot tìm kiếm điểm bất thường.
## Case Study 1: Phát hiện giao dịch chia nhỏ (Smurfing) để né tránh hạn mức phê duyệt.
## Cách AI nhận diện mô hình (Pattern Recognition) của Smurfing.
## Case Study 2: Phát hiện hóa đơn ma (Phantom Vendors) bằng phân tích tài khoản ngân hàng trùng lặp.
## Case Study 3: Phát hiện chi tiêu ngoài giờ làm việc hoặc vào ngày nghỉ phép.
## Sự kết hợp giữa AI (cảnh báo) và Con người (điều tra và ra quyết định).

## Phần 5: Thách thức, Đạo đức và Tương lai (Slides 35 - 42)
## Những rào cản khi triển khai AI trong Kế toán điều tra (Dữ liệu không gán nhãn - Unlabeled data).
## Cạm bẫy của AI: Báo động giả (False Positives) gây lãng phí nguồn lực.
## Cạm bẫy của AI: Bỏ sót rủi ro (False Negatives) do kẻ gian lận liên tục thay đổi chiến thuật.
## Vấn đề bảo mật dữ liệu và quyền riêng tư khi đưa dữ liệu sổ cái lên nền tảng AI.
## Đạo đức nghề nghiệp: AI không có tính người, Kế toán viên phải là người đánh giá cuối cùng.
## Xu hướng tương lai: AI rà soát giao dịch theo thời gian thực (Real-time Auditing).
## Tóm tắt bài học: AI là chiếc radar mạnh mẽ, nhưng kế toán viên là người cầm lái.
## Q&A và Hướng dẫn thực hành buổi tiếp theo (Thực hành dùng Pivot Table \& AI tìm bất thường).
