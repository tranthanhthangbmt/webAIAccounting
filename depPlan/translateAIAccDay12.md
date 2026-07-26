# Kế hoạch dịch thuật và tạo Web cho Buổi 12

## Yêu cầu
Dựa trên lộ trình `Lộ trình Giảng dạy AI trong Kế toán và Tài chính_v2.csv`, Buổi 12 có chủ đề: "Thực hành AI nhận thức và AI tạo sinh: Ứng dụng Generative AI hỗ trợ kế toán."

Tài liệu cần dịch bao gồm:
1. **ChatGPT and AI for Accountants**: Chương 1 (Generative AI in Accounting) & Chương 12 (Web-Enhanced ChatGPT).
   - File gốc: `_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Lila_Fretz.pdf`

## Các bước thực hiện
1. **Tìm kiếm vị trí trang:** Viết script `find_page_day12.py` để xác định trang bắt đầu và kết thúc của:
   - "Chapter 1" và "Chapter 12" trong sách *ChatGPT and AI for Accountants*.
2. **Trích xuất văn bản:** Trích xuất văn bản từ các trang tương ứng bằng `extract_chunk_day12.py`.
3. **Phân tách (Chunking):** Chia nhỏ văn bản thành các chunk (khoảng 15000 ký tự) như `chunk12A_1.txt`, `chunk12A_2.txt`,...
4. **Dịch thuật chuyên sâu (Dựa trên phương pháp Chapter 12):**
   - Sử dụng script tự động (`translate_day12.py`) kết hợp với quy tắc bảo tồn từ khóa:
     > Đóng vai: Bạn là một chuyên gia dịch thuật tài liệu học thuật chuyên sâu về Tài chính, Kế toán và AI.
     > Yêu cầu nghiêm ngặt:
     > 1. **Tuyệt đối không bỏ sót:** Dịch thật chi tiết và bám sát nguyên bản.
     > 2. **Chèn vị trí hình ảnh chuẩn xác:** Dịch toàn bộ các tiêu đề hình/bảng. BẮT BUỘC chèn thẻ `<!-- IMAGE_PLACEHOLDER: [Tên hình] -->` ĐÚNG vị trí tương ứng trong văn bản gốc.
     > 3. **Bảo tồn thuật ngữ:** Giữ nguyên tên gốc của *ChatGPT*, *Generative AI*, *Prompt*, *Plugins*...
     > 4. **Phân chia đoạn văn rõ ràng:** Tự động nhận diện và xuống dòng một cách hợp lý.
5. **Ghép file và Xuất HTML:**
   - Tạo file `build_html_day12.py` dựa trên cách làm của `build_html_day02.py` (sử dụng thư viện `marked.js` ở client-side thay vì render sẵn).
   - Đọc các chunk tiếng Anh và tiếng Việt.
   - Inject văn bản vào biến JavaScript bên trong file `Buoi_12.html` để render giao diện 2 tab (English / Tiếng Việt).
6. **Kiểm tra:** Xác minh trang HTML hiển thị chính xác.
