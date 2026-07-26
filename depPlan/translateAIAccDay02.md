# Kế hoạch tự động dịch Buổi 2 (AI and Finance, Big Data & Blockchain)

Theo yêu cầu, **Buổi 2** bao gồm 2 tài liệu PDF khá dài:
1. `Buoi_02A_Chương 1 (AI and Finance_Mục 1.2, 1.6, 1.7, 1.15) 2. Các phần về Big Data và Blockchain.pdf` (68 trang)
2. `Buoi_02B_Phần Big Data & Blockchain.pdf` (59 trang)

Dựa trên phương pháp của Chương 12 (như trong `depPlan/translateChapter12.md`), quy trình sẽ được tiến hành theo các bước chia nhỏ (chunking), dịch thuật chi tiết qua AI, và tự động tạo trang Web có 2 tab (English / Tiếng Việt).

## 1. Phương pháp Phân chia tài liệu (Chunking & Tree of Thought)
Vì tổng dung lượng 2 tài liệu rất lớn, tôi sẽ thiết lập kế hoạch bóc tách như sau:

### Phân tích Tài liệu 2A:
- Sử dụng mã Python (PyPDF2) đọc toàn bộ 68 trang.
- Dùng Regex / AI để cắt chính xác các phần:
  - **Chunk A1**: Mục 1.2
  - **Chunk A2**: Mục 1.6
  - **Chunk A3**: Mục 1.7
  - **Chunk A4**: Mục 1.15
- Bỏ qua các mục không được yêu cầu để tiết kiệm thời gian và tối ưu nội dung.

### Phân tích Tài liệu 2B:
- Chia 59 trang thành các Chunk nhỏ (khoảng 3-5 trang/chunk) dựa trên Heading/Chương của tài liệu.
- Dự kiến chia thành 10-15 Chunks.

## 2. Quy trình Dịch thuật & Định dạng (Translation & Formatting)
- **Prompt dịch thuật**: Đóng vai trò chuyên gia AI & Kế toán, dịch chi tiết 100% văn bản, không tóm tắt.
- **Bảo tồn thuật ngữ**: Giữ lại các thuật ngữ tiếng Anh gốc trong ngoặc đơn (ví dụ: *Blockchain*, *Big Data Analytics*).
- **Hình ảnh**: Thay thế tất cả các biểu đồ, hình ảnh bằng thẻ `<!-- IMAGE_PLACEHOLDER: [Tên hình] -->` ở cả bản tiếng Anh và Tiếng Việt.

## 3. Xuất file web (HTML Output)
Tôi sẽ tạo mã Python `build_buoi2_html.py` để tự động tổng hợp tất cả các chunks. 
Đầu ra sẽ là file `Buoi_02.html` với cấu trúc:
- Tab 1: **English (Bản gốc)**
  - Nội dung Tài liệu 2A (các mục chọn lọc)
  - Nội dung Tài liệu 2B
- Tab 2: **Tiếng Việt (Bản dịch)**
  - Bản dịch Tài liệu 2A
  - Bản dịch Tài liệu 2B

## 4. Kiểm tra (Verification Plan)
1. Trích xuất text từ PDF thành công và đảm bảo đủ các mục yêu cầu.
2. Dịch từng chunk và lưu vào các file tạm (`chunkA1_vi.txt`, `chunkB1_vi.txt`...).
3. Sinh file `Buoi_02.html`, mở kiểm tra tính năng tab và định dạng Markdown (tiêu đề, in đậm, danh sách).
