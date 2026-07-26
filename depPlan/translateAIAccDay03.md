# Kế hoạch tự động dịch Buổi 3 (Đạo đức, rủi ro của AI & Các khái niệm cơ bản)

Theo lộ trình khóa học, **Buổi 3** bao gồm tài liệu từ 2 cuốn sách:
1. **Tài liệu 3A**: `Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf` (Chương 1 - Phần về Machine Learning, Deep Learning, NLP).
2. **Tài liệu 3B**: `Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...pdf` (Chương 15 - Ethics and Laws).

Dựa trên phương pháp của Chương 12 (như trong `depPlan/translateChapter12.md`) và quy trình đã áp dụng thành công cho Buổi 1 & Buổi 2, quy trình sẽ được tiến hành theo các bước sau:

## 1. Trích xuất văn bản (Text Extraction)
Hiện tại văn bản thô của Buổi 3 chưa có sẵn. Tôi sẽ tiến hành:
- Đọc 2 file PDF tương ứng từ thư mục `ebooks`.
- Trích xuất chính xác văn bản (OCR/text extraction) cho các chương yêu cầu (Chương 1 của Tài liệu 3A và Chương 15 của Tài liệu 3B).
- Lưu kết quả trích xuất vào các tệp `buoi3A_text_utf8.txt` và `buoi3B_text_utf8.txt`.

## 2. Phương pháp Phân chia tài liệu (Chunking & Tree of Thought)
- **Phân tích Tài liệu 3A (Chương 1)**: Xác định và cắt chính xác các phần về Machine Learning, Deep Learning và Natural Language Processing (NLP) thành các chunk (ví dụ: `chunk3A_1`, `chunk3A_2`...).
- **Phân tích Tài liệu 3B (Chương 15)**: Chia nội dung về "Ethics and Laws" (Đạo đức và Pháp luật) thành các chunk có kích thước phù hợp (từ 10-15 nghìn ký tự/chunk) để AI có thể dịch thuật với chất lượng cao nhất (ví dụ: `chunk3B_1`, `chunk3B_2`...).

## 3. Quy trình Dịch thuật & Định dạng (Translation & Formatting)
- **Prompt dịch thuật**: Đóng vai trò chuyên gia AI & Kế toán, dịch chi tiết 100% văn bản, không tóm tắt.
- **Bảo tồn thuật ngữ**: Giữ lại các thuật ngữ tiếng Anh gốc trong ngoặc đơn (ví dụ: *Machine Learning*, *Algorithmic Bias*).
- **Hình ảnh**: Thay thế tất cả các biểu đồ, hình ảnh bằng thẻ `<!-- IMAGE_PLACEHOLDER: [Tên hình/Bảng] -->` ở cả bản tiếng Anh và Tiếng Việt để dễ dàng bổ sung sau này.
- Lưu bản dịch vào các tệp tương ứng (`chunk3A_1_vi.txt`, `chunk3B_1_vi.txt`...).

## 4. Xuất file web (HTML Output)
Tôi sẽ tạo (hoặc cập nhật) mã Python `build_html_day03.py` để tự động tổng hợp tất cả các chunks. 
Đầu ra sẽ là file `Buoi_03.html` với cấu trúc:
- Tab 1: **English (Bản gốc)**
  - Nội dung Tài liệu 3A (Phần ML, DL, NLP)
  - Nội dung Tài liệu 3B (Chương 15: Ethics and Laws)
- Tab 2: **Tiếng Việt (Bản dịch)**
  - Bản dịch Tài liệu 3A
  - Bản dịch Tài liệu 3B

## 5. Kiểm tra (Verification Plan)
1. Đảm bảo trích xuất PDF thành công, không bị lỗi font chữ.
2. Dịch từng chunk mà không bị ngắt quãng hoặc sót ý.
3. Sinh file `Buoi_03.html`, kiểm tra tính năng tab và định dạng Markdown hiển thị chuẩn xác trên trình duyệt.
