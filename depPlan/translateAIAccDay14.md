# Kế hoạch dịch thuật và tạo Web cho Buổi 14

## Yêu cầu
Dựa trên lộ trình `Lộ trình Giảng dạy AI trong Kế toán và Tài chính_v2.csv`, Buổi 14 có chủ đề: "Phân tích dữ liệu chuyên sâu: Tìm điểm bất thường và truyền đạt kết quả kế toán."

Tài liệu cần dịch bao gồm:
1. **Data and Analytics in Accounting**: Chương 7 (Data Exploration) & Chương 9 (Communicating Results).
   - File gốc: `_OceanofPDF.com_Data_and_Analytics_in_Accounting_-_Ann_C_Dzuranin.pdf`

## Các bước thực hiện
1. **Tìm kiếm vị trí trang:** Viết script `find_page_day14.py` để xác định trang bắt đầu và kết thúc của:
   - "Chapter 7: Data Exploration" và "Chapter 9: Communicating Results" trong sách *Data and Analytics in Accounting*.
2. **Trích xuất văn bản:** Trích xuất văn bản từ các trang tương ứng bằng `extract_chunk_day14.py`.
3. **Phân tách (Chunking):** Chia nhỏ văn bản thành các chunk (khoảng 15000 ký tự) như `chunk14A_1.txt`, `chunk14A_2.txt`,...
4. **Dịch thuật chuyên sâu (Dựa trên phương pháp Chapter 12):**
   - Sử dụng script tự động (`translate_day14.py`) kết hợp với quy tắc bảo tồn từ khóa:
     > Yêu cầu nghiêm ngặt:
     > 1. **Tuyệt đối không bỏ sót:** Dịch thật chi tiết và bám sát nguyên bản.
     > 2. **Chèn vị trí hình ảnh chuẩn xác:** Dịch toàn bộ các tiêu đề hình/bảng. BẮT BUỘC chèn thẻ `<!-- IMAGE_PLACEHOLDER: [Tên hình] -->` ĐÚNG vị trí tương ứng trong văn bản gốc.
     > 3. **Bảo tồn thuật ngữ:** Giữ nguyên tên gốc của *Data Exploration*, *Data Storytelling*, *Communicating Results*, *Anomalies*...
     > 4. **Phân chia đoạn văn rõ ràng:** Tự động nhận diện và xuống dòng một cách hợp lý.
5. **Ghép file và Xuất HTML:**
   - Tạo file `build_html_day14.py` mô phỏng cấu trúc của `Buoi_02.html` (sử dụng thư viện `marked.js` ở client-side).
   - Đọc các chunk tiếng Anh và tiếng Việt.
   - Inject văn bản vào biến JavaScript bên trong file `Buoi_14.html` để render giao diện 2 tab (English / Tiếng Việt).
6. **Kiểm tra:** Xác minh trang HTML hiển thị chính xác.
