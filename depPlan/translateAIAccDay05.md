# Kế hoạch Dịch thuật Tài liệu Buổi 5

## 1. Mục tiêu
- **Chủ đề:** AI trong quản lý kinh tế: Quản lý chuỗi cung ứng, ra quyết định dưới áp lực rủi ro.
- **Tài liệu nguồn:** `_OceanofPDF.com_Business_Analytics_Solving_Business_Problems_-_Arul_Mishra.pdf` (Chương 12 & Chương 14)
- **Yêu cầu:** Dịch sát nghĩa, chi tiết, chèn placeholder cho hình ảnh. Xuất ra file HTML song ngữ (2 tab: English, Tiếng Việt).

## 2. Các bước thực hiện
### Bước 1: Trích xuất nội dung văn bản (Text Extraction)
- Sử dụng thư viện `PyPDF2` (Python) để đọc tệp PDF.
- Xác định trang bắt đầu và kết thúc của:
  - **Chương 12 (Tài liệu 5A):** Managing Decision Uncertainty
  - **Chương 14 (Tài liệu 5B):** New Product Development
- Lưu nội dung thô (tiếng Anh) thành: `buoi5A_text_utf8.txt` và `buoi5B_text_utf8.txt`.

### Bước 2: Phân tách văn bản (Chunking)
- Do mỗi chương dài, chúng ta sẽ chia nhỏ các file gốc ra thành nhiều chunk nhỏ hơn (khoảng 15,000 - 20,000 ký tự mỗi chunk) để đảm bảo chất lượng dịch thuật.
  - `buoi5A_text_utf8.txt` -> `chunk5A_1.txt`, `chunk5A_2.txt`...
  - `buoi5B_text_utf8.txt` -> `chunk5B_1.txt`, `chunk5B_2.txt`...

### Bước 3: Dịch thuật (Translation)
- Dịch từng chunk một sang Tiếng Việt một cách tỉ mỉ.
- **Quy tắc dịch:**
  - Bám sát nghĩa gốc.
  - Giữ lại các thuật ngữ tiếng Anh gốc trong ngoặc đơn, ví dụ: "chuỗi cung ứng (supply chain)".
  - Chèn placeholder nếu có hình ảnh: `<!-- IMAGE_PLACEHOLDER: Hình ảnh mô tả... -->`.
- Lưu các tệp kết quả dịch: `chunk5A_1_vi.txt`, `chunk5A_2_vi.txt`...

### Bước 4: Lắp ráp & Xây dựng giao diện Web
- Tạo một kịch bản Python (`build_html_day05.py`) để ghép nội dung từ các file `chunk` và `chunk_vi`.
- Sử dụng CSS, Javascript và thư viện `marked.js` để render cấu trúc 2 Tab (English / Tiếng Việt).
- Tên tệp đầu ra: `Buoi_05.html`.

## 3. Thời gian dự kiến
- Xác định số trang & trích xuất PDF: ~3 phút.
- Phân tách văn bản (Chunking): ~1 phút.
- Dịch thuật chi tiết: ~5-10 phút (tùy vào độ dài của 2 chương).
- Đóng gói HTML: ~2 phút.
- **Tổng thời gian thực hiện:** Khoảng 15 phút sau khi triển khai.
