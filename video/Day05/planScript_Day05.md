# Kế hoạch Kịch bản Bài giảng: Day 05 - Quản trị Rủi ro Quyết định & Phát triển Sản phẩm Mới

**Tệp đầu vào:** `Slide_AIAcc_Day05.tex` & Textbook "Data and Analytics in the Accounting Profession" (Chương 12 \& Chương 14).
**Hình thức:** Hội thoại giảng dạy Socratic (Người 1: Giảng viên, Người 2: Sinh viên).
**Mục tiêu:** Chuyển hóa các khái niệm như Dữ liệu mất cân bằng (Imbalanced Data), Rừng ngẫu nhiên (Random Forest) và Thử nghiệm A/B thành những câu chuyện dễ hiểu, ứng dụng vào quản trị rủi ro chuỗi cung ứng và quyết định kinh doanh.

## Dàn ý Chi tiết (Mapping Slide & Textbook)

### Phần 1: Bất định trong Chuỗi Cung ứng & Cây Quyết định (Slide 1 - 16)
- **Khởi động:** Giới thiệu bước chuyển đổi tư duy: Kế toán quản trị không chỉ ghi chép quá khứ mà phải kiểm soát sự "bất định" của tương lai.
- **Vấn đề Backorder \& Hiệu ứng roi da:** Tình huống đứt gãy nguồn cung smartphone. Hậu quả của trò chơi "Tam sao thất bản" trong chuỗi cung ứng (Cơn sốt giấy vệ sinh).
- **Tập dữ liệu mất cân bằng:** Tại sao thống kê truyền thống thất bại khi số ca giao hàng bình thường áp đảo hoàn toàn các ca đứt gãy.
- **Cây quyết định (Decision Tree):** Cách phân chia dữ liệu bằng Độ vẩn đục Gini. Sơ đồ rẽ nhánh. Điểm yếu chí mạng của cây quyết định đơn lẻ (sự nhạy cảm, dễ bị đánh lừa).

### Phần 2: Rừng ngẫu nhiên (Random Forest) & Đánh giá Mô hình (Slide 17 - 30)
- **Cơ chế 1: Bagging:** Bốc ngẫu nhiên dữ liệu tạo ra nhiều góc nhìn.
- **Cơ chế 2: Subspace Sampling:** Ẩn dụ "100 bác sĩ hội chẩn bị giấu bệnh án" để ép tư duy độc lập. Quyết định bằng Majority Vote (Bầu chọn số đông).
- **Căn bệnh lười biếng của mô hình:** Quy luật "khôn lỏi" khi mô hình gian lận đoán bừa.
- **Downsampling:** Cắt giảm dữ liệu nhóm bình thường để ép mô hình phải học thật sự.
- **Bảng điểm khắt khe:** Từ bỏ Accuracy, tập trung vào Độ nhạy (Sensitivity) và Độ đặc hiệu (Specificity). Đánh giá sức mạnh của đường cong ROC & AUC.

### Phần 3: Phát triển Sản phẩm Mới & Thử nghiệm A/B (Slide 31 - 49)
- **Sự chuyển giao:** Khi rủi ro đến từ quyết định chủ quan nội bộ (ví dụ: đổi giao diện game).
- **Tương quan vs. Nhân quả:** Cạm bẫy Tương quan giả tạo (Ăn kem và Cháy rừng) và Thiên kiến tự chọn (Self-Selection Bias - Người dùng chọn giao diện màu xanh).
- **Thử nghiệm A/B:** Phá vỡ bẫy bằng sự phân bổ ngẫu nhiên (Randomization) tước đi quyền tự chọn của khách hàng.
- **Gã giám khảo bảo thủ:** Giới thiệu Giả thuyết Không (Null Hypothesis).
- **ANOVA & F-Test:** So sánh biến động giữa các nhóm và nội bộ từng nhóm. Đập tan sự hoài nghi.
- **Giá trị P (P-value):** Điểm chốt hạ (P < 0.05) giúp ra quyết định đầu tư hàng triệu đô tự tin.
- **Lời kết:** Dữ liệu khách quan, không tự ái. Câu hỏi suy ngẫm về ranh giới giữa sự an toàn của thuật toán và sự sáng tạo điên rồ của con người.
