# Kế hoạch dịch thuật và tạo Web cho Buổi 8

## Yêu cầu
Dựa trên lộ trình `Lộ trình Giảng dạy AI trong Kế toán và Tài chính_v2.csv`, Buổi 8 có chủ đề: "AI trong tài chính ngân hàng và chứng khoán: Chấm điểm tín dụng, giao dịch thuật toán."

Tài liệu cần dịch bao gồm 2 phần từ 2 sách khác nhau:
1. **Generative Artificial Intelligence in Finance**: Chương 6 (Credit Scoring, Algorithmic Trading).
   - File gốc: `Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf`
2. **Fintech**: Phần AI Algorithmic Trading.
   - File gốc: `_OceanofPDF.com_Fintech_-_Pranay_Gupta.pdf`

## Các bước thực hiện
1. **Tìm kiếm vị trí trang:** Viết script Python dùng `PyMuPDF (fitz)` để xác định trang bắt đầu và kết thúc của:
   - "Chapter 6" (Phần Credit Scoring, Algorithmic Trading) trong sách Generative AI in Finance.
   - Phần "AI Algorithmic Trading" trong sách Fintech.
2. **Trích xuất văn bản:** Trích xuất văn bản từ các trang tương ứng và lưu thành các file `buoi8A_text_utf8.txt` và `buoi8B_text_utf8.txt`.
3. **Phân tách (Chunking):** Chia nhỏ mỗi file thành các chunk (khoảng 10000 - 15000 ký tự) như `chunk8A_1.txt`, `chunk8B_1.txt`,...
4. **Dịch thuật:** Dịch các chunk tiếng Anh này sang tiếng Việt, lưu dưới dạng `chunk8A_1_vi.txt`, `chunk8B_1_vi.txt`,... 
   - Đảm bảo bám sát từ vựng gốc (giữ lại từ chuyên ngành trong ngoặc đơn).
   - Thêm các tag hình ảnh `<!-- IMAGE_PLACEHOLDER: ... -->` tại những vị trí có biểu đồ, hình vẽ.
5. **Ghép file và Xuất HTML:**
   - Tạo file `build_html_day08.py`.
   - Đọc các chunk tiếng Anh và tiếng Việt.
   - Sử dụng `marked.js` để tạo trang `Buoi_08.html` có 2 tab (English / Tiếng Việt).
6. **Kiểm tra:** Xác minh trang HTML hiển thị chính xác và các tab hoạt động tốt.
