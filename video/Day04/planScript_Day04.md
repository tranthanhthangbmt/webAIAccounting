# Kế hoạch Kịch bản Bài giảng: Day 04 - Trí tuệ Nhân tạo Ứng dụng trong Kế toán

**Tệp đầu vào:** `Slide_AIAcc_Day04.tex` & Textbook "Data and Analytics in the Accounting Profession" (Chương 5 \& Chương 10).
**Hình thức:** Hội thoại giảng dạy Socratic (Người 1: Giảng viên, Người 2: Sinh viên).
**Mục tiêu:** Chuyển hóa các thuật toán AI phức tạp (k-Means, k-Medoid, LASSO Regression) thành các câu chuyện dễ hiểu, gắn liền với nghiệp vụ Phân tích Khách hàng và Đánh giá Rủi ro Phá sản. 

## Dàn ý Chi tiết (Mapping Slide & Textbook)

### Phần 1: Phân khúc Khách hàng & Học không giám sát (Slide 1 - 16)
- **Khởi động:** Giới thiệu bước ngoặt của Buổi 4: Chuyển từ lý thuyết sang thuật toán AI thực chiến (hands-on).
- **Vấn đề Marketing Đại trà:** Case study Nhà hàng Vegan-Always rải thảm voucher thất bại $\rightarrow$ Đặt ra nhu cầu tìm đúng tệp khách hàng.
- **Khái niệm Phân khúc \& Vi phân khúc:** Giải thích vi phân khúc (Microsegments) và phân khúc động (Real-time).
- **Học Không Giám Sát (Unsupervised Learning):** Giải mã sự đáng sợ của "Dữ liệu không nhãn" đối với con người.
- **Phân cụm (Clustering):** Khái niệm cốt lõi của Học không giám sát để tìm ra "cấu trúc ẩn" (hidden structure) bên trong mớ dữ liệu kế toán khổng lồ.

### Phần 2: Thuật toán k-Means, k-Medoid & Hệ số Silhouette (Slide 17 - 32)
- **Cơ chế Đo khoảng cách:** Giải thích khái niệm "Khoảng cách ngắn = Hành vi giống nhau".
- **Ví dụ Bữa tiệc khổng lồ:** Chuyển ngữ toán học toàn bộ vòng lặp của k-Means (Chọn $k$ cái bàn $\rightarrow$ Khách chạy lại gần bàn $\rightarrow$ Dời bàn $\rightarrow$ Lặp đến khi hội tụ).
- **Điểm yếu của k-Means:** Sự nhạy cảm với các Điểm ngoại lai (Outliers) - khách hàng mua số lượng quá lớn làm sai lệch trung bình cộng.
- **Giải pháp k-Medoid:** Dùng một "người thực" (Trưởng bàn) làm tâm cụm để chống nhiễu thay vì dùng "điểm ảo" (Trung bình cộng).
- **Hệ số Silhouette:** Công cụ chấm điểm để tìm số $k$ tối ưu (dựa trên Độ gắn kết bên trong và Độ tách biệt bên ngoài).
- **Ứng dụng Kế toán Quản trị:** Tối ưu hóa ROI khi tìm ra nhóm "Khách gắn bó lâu và chi nhiều tiền". Giới thiệu sơ lược code R chạy k-Means.

### Phần 3: Dự báo Phá sản, Đa cộng tuyến & Hồi quy LASSO (Slide 33 - 52)
- **Góc nhìn Quản trị rủi ro:** Chuyển từ việc tìm kiếm khách hàng sang bảo vệ sinh mệnh doanh nghiệp (Góc nhìn từ Ngân hàng UltraBank).
- **Chỉ số tài chính truyền thống:** Debt-to-Equity, Current Ratio...
- **Vấn đề Đa cộng tuyến (Multicollinearity):** Ví dụ trực quan "Lái xe bật 5 cái GPS cùng lúc". Các biến tương quan mạnh gây nhiễu và phá hủy mô hình Hồi quy cổ điển OLS. Hậu quả là Sai lầm Loại II.
- **Phát hiện đa cộng tuyến:** Sử dụng Correlation Plot và chỉ số VIF.
- **Thuật toán LASSO (Hồi quy có phạt):** Máy móc "trừng phạt" dữ liệu nhiễu bằng cách ép hệ số về 0 (Loại bỏ biến thừa). Tự động giữ lại các chỉ số cốt lõi mà kế toán không cần đoán mò.
- **Đánh giá bằng ROC AUC:** Giải nghĩa đường cong ROC và điểm AUC (AUC $\approx$ 0.8 là rất tốt).
- **Lời kết \& Tương lai nghề nghiệp:** Trực giác con người va chạm với thuật toán. Kế toán viên phải kiểm soát và diễn dịch AI chứ không phục tùng mù quáng. Hỏi \& Đáp.
