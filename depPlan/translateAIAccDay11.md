# Kế hoạch dịch thuật và tạo Web cho Buổi 11

## Yêu cầu
Dựa trên lộ trình `Lộ trình Giảng dạy AI trong Kế toán và Tài chính_v2.csv`, Buổi 11 có chủ đề: "Thực hành nền tảng dữ liệu kế toán: Cấu trúc cơ sở dữ liệu và công cụ trực quan hóa (Excel, Power BI, Tableau)."

Tài liệu cần dịch bao gồm:
1. **Data and Analytics in Accounting**: Chương 2 (Foundational Data Analysis Skills).
   - File gốc: `_OceanofPDF.com_Data_and_Analytics_in_Accounting_-_Ann_C_Dzuranin.pdf`

## Các bước thực hiện
1. **Tìm kiếm vị trí trang:** Viết script Python dùng `PyMuPDF (fitz)` hoặc `PyPDF2` để xác định trang bắt đầu và kết thúc của:
   - "Chapter 2: Foundational Data Analysis Skills" trong sách *Data and Analytics in Accounting*.
2. **Trích xuất văn bản:** Trích xuất văn bản từ các trang tương ứng và lưu thành file `buoi11A_text_utf8.txt`.
3. **Phân tách (Chunking):** Chia nhỏ file thành các chunk (khoảng 10000 - 15000 ký tự) như `chunk11A_1.txt`, `chunk11A_2.txt`,...
4. **Dịch thuật chuyên sâu (Dựa trên phương pháp Chapter 12):**
   - Sử dụng Prompt chuyên sâu sau đây cho từng chunk để đảm bảo chất lượng dịch thuật tốt nhất.
   - **Mẫu Prompt (Dành cho AI):**
     > Đóng vai: Bạn là một chuyên gia dịch thuật tài liệu học thuật chuyên sâu về Tài chính, Kế toán và Phân tích Dữ liệu (Data Analytics).
     > Nhiệm vụ: Hãy dịch phần văn bản thuộc [Tên phần/Chunk] của tài liệu sang tiếng Việt.
     > Yêu cầu nghiêm ngặt:
     > 1. **Tuyệt đối không bỏ sót:** Dịch thật chi tiết và bám sát nguyên bản. Không được tự ý tóm tắt, cắt xén bất kỳ câu chữ, ý nghĩa hay chi tiết nào.
     > 2. **Chèn vị trí hình ảnh chuẩn xác:** Dịch toàn bộ các tiêu đề, chú thích của hình ảnh/bảng biểu. BẮT BUỘC chèn thẻ `<!-- IMAGE_PLACEHOLDER: [Tên hình/Bảng - Mô tả ngắn bằng tiếng Việt] -->` ĐÚNG vị trí tương ứng trong văn bản gốc để tôi bổ sung hình ảnh sau này.
     > 3. **Bảo tồn thuật ngữ:** Giữ nguyên các định dạng công thức, mã code (nếu có). Với các thuật ngữ học thuật quan trọng, hãy để từ tiếng Anh gốc trong ngoặc đơn sau bản dịch tiếng Việt (ví dụ: cơ sở dữ liệu quan hệ (*Relational Databases*), trực quan hóa dữ liệu (*Data Visualization*), *Power BI*, *Tableau*, *Excel*) để người đọc dễ đối chiếu.
     > 4. **Phân chia đoạn văn rõ ràng:** Tự động nhận diện và xuống dòng một cách hợp lý để tách biệt các luận điểm. Không để một đoạn văn quá dài gây mỏi mắt. Bôi đậm (**bold**) các từ khóa quan trọng, các khái niệm mới hoặc tiêu đề để dễ theo dõi.
     > 5. **Văn phong:** Sử dụng văn phong mạch lạc, chuẩn ngôn ngữ sách giáo trình đại học, dễ hiểu nhưng vẫn đảm bảo tính chuyên ngành.
   - Kết quả dịch được lưu dưới dạng `chunk11A_1_vi.txt`, `chunk11A_2_vi.txt`,...
5. **Ghép file và Xuất HTML:**
   - Tạo file `build_html_day11.py`.
   - Đọc các chunk tiếng Anh và tiếng Việt.
   - Sử dụng `marked.js` (hoặc module python `markdown`) để tạo trang `Buoi_11.html` có 2 tab (English / Tiếng Việt).
6. **Kiểm tra:** Xác minh trang HTML hiển thị chính xác và các tab hoạt động tốt.
