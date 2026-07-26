# Kế hoạch dịch thuật và tạo Web cho Buổi 13

## Yêu cầu
Dựa trên lộ trình `Lộ trình Giảng dạy AI trong Kế toán và Tài chính_v2.csv`, Buổi 13 có chủ đề: "Kỹ thuật Prompt & Khởi động Phân tích dữ liệu: Khung tư duy SPARKS."

Tài liệu cần dịch bao gồm 2 nguồn:
1. **ChatGPT and AI for Accountants**: Chương 6 (Turbocharging Financial Analysis).
   - File gốc: `_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Scott_Dell_Mfon_Akpan.pdf`
2. **Data and Analytics in Accounting**: Chương 3 & 4 (Planning Data Strategies).
   - File gốc: `_OceanofPDF.com_Data_and_Analytics_in_Accounting_-_Ann_C_Dzuranin.pdf`

## Các bước thực hiện
1. **Tìm kiếm vị trí trang:** Viết script `find_page_day13.py` để xác định trang bắt đầu và kết thúc của các chương thuộc hai quyển sách trên.
2. **Trích xuất văn bản:** Trích xuất văn bản từ các trang tương ứng bằng `extract_chunk_day13.py`.
   - Các chunk của sách 1 sẽ lưu thành `chunk13A_1.txt`,...
   - Các chunk của sách 2 sẽ lưu thành `chunk13B_1.txt`,...
3. **Phân tách (Chunking):** Chia nhỏ văn bản thành các chunk (khoảng 15000 ký tự).
4. **Dịch thuật chuyên sâu:**
   - Sử dụng script tự động (`translate_day13.py`) kết hợp với quy tắc bảo tồn từ khóa:
     > Yêu cầu nghiêm ngặt:
     > 1. **Tuyệt đối không bỏ sót:** Dịch thật chi tiết và bám sát nguyên bản.
     > 2. **Chèn vị trí hình ảnh chuẩn xác:** Dịch toàn bộ các tiêu đề hình/bảng. BẮT BUỘC chèn thẻ `<!-- IMAGE_PLACEHOLDER: [Tên hình] -->` ĐÚNG vị trí tương ứng trong văn bản gốc.
     > 3. **Bảo tồn thuật ngữ:** Giữ nguyên tên gốc của *SPARKS*, *Prompt*, *Data Strategies*, *Financial Analysis*...
     > 4. **Phân chia đoạn văn rõ ràng:** Tự động nhận diện và xuống dòng một cách hợp lý.
5. **Ghép file và Xuất HTML:**
   - Tạo file `build_html_day13.py` mô phỏng cấu trúc của `Buoi_02.html` (sử dụng thư viện `marked.js`).
   - Ghép toàn bộ chunk13A và chunk13B.
   - Inject văn bản vào biến JavaScript bên trong file `Buoi_13.html` để render giao diện 2 tab (English / Tiếng Việt).
6. **Kiểm tra:** Xác minh trang HTML hiển thị chính xác.
