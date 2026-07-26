# Kế hoạch tự động dịch Buổi 4 (AI trong kinh tế vĩ mô: Phân tích hành vi người tiêu dùng & Dự báo sức khỏe tài chính)

Theo lộ trình khóa học, **Buổi 4** bao gồm tài liệu từ cuốn sách sau:
**Tài liệu 4**: `_OceanofPDF.com_Business_Analytics_Solving_Business_Problems_-_Arul_Mishra.pdf`
- **Phần 4A**: Chương 5 (Market Segmentation...) - Hướng dẫn ứng dụng thuật toán phân cụm (k-Means, k-Medoid) để phân khúc khách hàng.
- **Phần 4B**: Chương 10 (Forecasting Financial Health...) - Sử dụng mô hình hồi quy (LASSO) để dự báo sức khỏe tài chính và phá sản.

Dựa trên phương pháp của Chương 12 (như trong `depPlan/translateChapter12.md`) và quy trình đã áp dụng thành công cho Buổi 1, 2, và 3, quy trình sẽ được tiến hành theo các bước sau:

## 1. Trích xuất văn bản (Text Extraction)
Hiện tại văn bản thô của Buổi 4 chưa có sẵn. Tôi sẽ tiến hành:
- Đọc file PDF `_OceanofPDF.com_Business_Analytics_Solving_Business_Problems_-_Arul_Mishra.pdf` từ thư mục `ebooks`.
- Tìm trang tương ứng của Chương 5 và Chương 10.
- Trích xuất chính xác văn bản (OCR/text extraction) cho các chương yêu cầu.
- Lưu kết quả trích xuất vào các tệp `buoi4A_text_utf8.txt` (Chương 5) và `buoi4B_text_utf8.txt` (Chương 10).

## 2. Phương pháp Phân chia tài liệu (Chunking & Tree of Thought)
- **Phân tích Tài liệu 4A (Chương 5)**: Chia nội dung Chương 5 thành các chunk có kích thước phù hợp (từ 10-15 nghìn ký tự/chunk) để AI có thể dịch thuật với chất lượng cao nhất (ví dụ: `chunk4A_1`, `chunk4A_2`...).
- **Phân tích Tài liệu 4B (Chương 10)**: Chia nội dung Chương 10 thành các chunk (ví dụ: `chunk4B_1`, `chunk4B_2`...).

## 3. Quy trình Dịch thuật & Định dạng (Translation & Formatting)
- **Prompt dịch thuật**: Đóng vai trò chuyên gia AI & Kế toán/Tài chính, dịch chi tiết 100% văn bản, không tóm tắt.
- **Bảo tồn thuật ngữ**: Giữ lại các thuật ngữ tiếng Anh gốc trong ngoặc đơn (ví dụ: *Market Segmentation*, *k-Means*, *k-Medoid*, *Forecasting*, *LASSO*).
- **Hình ảnh**: Thay thế tất cả các biểu đồ, hình ảnh, bảng biểu bằng thẻ `<!-- IMAGE_PLACEHOLDER: [Tên hình/Bảng] -->` ở cả bản tiếng Anh và Tiếng Việt để dễ dàng bổ sung sau này.
- Lưu bản dịch vào các tệp tương ứng (`chunk4A_1_vi.txt`, `chunk4B_1_vi.txt`...).

## 4. Xuất file web (HTML Output)
Tôi sẽ tạo (hoặc cập nhật) mã Python `build_html_day04.py` để tự động tổng hợp tất cả các chunks. 
Đầu ra sẽ là file `Buoi_04.html` với cấu trúc:
- Tab 1: **English (Bản gốc)**
  - Nội dung Tài liệu 4A (Chương 5: Market Segmentation...)
  - Nội dung Tài liệu 4B (Chương 10: Forecasting Financial Health...)
- Tab 2: **Tiếng Việt (Bản dịch)**
  - Bản dịch Tài liệu 4A
  - Bản dịch Tài liệu 4B

## 5. Kiểm tra (Verification Plan)
1. Đảm bảo trích xuất PDF thành công, không bị lỗi font chữ.
2. Dịch từng chunk mà không bị ngắt quãng hoặc sót ý.
3. Sinh file `Buoi_04.html`, kiểm tra tính năng tab và định dạng Markdown hiển thị chuẩn xác trên trình duyệt.
