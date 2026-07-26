# Kế hoạch dịch thuật và tạo Web cho Buổi 6

## Yêu cầu
Dựa trên lộ trình `Lộ trình Giảng dạy AI trong Kế toán và Tài chính_v2.csv`, Buổi 6 có chủ đề: "AI trong tài chính công và quốc tế: Quản lý ngân sách, thu - chi công, phòng chống gian lận."

Tài liệu cần dịch bao gồm 2 phần:
1. Sách **ChatGPT and AI for Accountants**: Chương 5 (Case study 4: Tackling public sector corruption).
2. Sách **Generative AI in Finance**: Chương 1 (Preserving financial stability).

## Các bước thực hiện
1. **Tìm kiếm vị trí trang:** Viết script Python dùng `PyPDF2` để xác định trang bắt đầu và kết thúc của:
   - "Case study 4: Tackling public sector corruption" trong file `_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Scott_Dell_Mfon_Akpan.pdf`.
   - "Preserving financial stability" trong file `_OceanofPDF.com_Generative_AI_in_Finance_-_Pethuru_Raj_Chelliah.pdf`.
2. **Trích xuất văn bản:** Trích xuất văn bản từ các trang tương ứng và lưu thành các file `buoi6A_text_utf8.txt` và `buoi6B_text_utf8.txt`.
3. **Phân tách (Chunking):** Chia nhỏ mỗi file thành các chunk (khoảng 15000 ký tự) như `chunk6A_1.txt`, `chunk6B_1.txt`,...
4. **Dịch thuật:** Dịch các chunk tiếng Anh này sang tiếng Việt, lưu dưới dạng `chunk6A_1_vi.txt`,... 
   - Đảm bảo bám sát từ vựng gốc.
   - Thêm các tag hình ảnh `<!-- IMAGE_PLACEHOLDER: ... -->` tại những vị trí có biểu đồ, hình vẽ.
5. **Ghép file và Xuất HTML:**
   - Tạo file `build_html_day06.py`.
   - Đọc các chunk tiếng Anh và tiếng Việt.
   - Sử dụng `marked.js` để tạo trang `Buoi_06.html` có 2 tab (English / Tiếng Việt).
6. **Kiểm tra:** Xác minh trang HTML hiển thị chính xác.
