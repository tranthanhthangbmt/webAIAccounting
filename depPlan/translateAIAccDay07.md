# Kế hoạch dịch thuật và tạo Web cho Buổi 7

## Yêu cầu
Dựa trên lộ trình `Lộ trình Giảng dạy AI trong Kế toán và Tài chính_v2.csv`, Buổi 7 có chủ đề: "AI trong tài chính doanh nghiệp và kiểm toán: Tự động hóa kiểm soát nội bộ & Kế toán pháp y."

Tài liệu cần dịch bao gồm 2 phần từ 1 sách duy nhất (**Artificial Intelligence for Audit, Forensic Accounting, and Valuation**):
1. Chương 9 (Automating Internal Controls).
2. Chương 12 (Intelligent Automation of Fraud Detection).

File gốc: `_OceanofPDF.com_Artificial_Intelligence_for_Audit_Forensic_Accounting_and_Valuation_-_Al_Naqvi.pdf`

## Các bước thực hiện
1. **Tìm kiếm vị trí trang:** Viết script Python dùng `PyMuPDF (fitz)` để xác định trang bắt đầu và kết thúc của:
   - "Chapter 9: Automating Internal Controls".
   - "Chapter 12: Intelligent Automation of Fraud Detection".
2. **Trích xuất văn bản:** Trích xuất văn bản từ các trang tương ứng và lưu thành các file `buoi7A_text_utf8.txt` và `buoi7B_text_utf8.txt`.
3. **Phân tách (Chunking):** Chia nhỏ mỗi file thành các chunk (khoảng 15000 ký tự) như `chunk7A_1.txt`, `chunk7B_1.txt`,...
4. **Dịch thuật:** Dịch các chunk tiếng Anh này sang tiếng Việt, lưu dưới dạng `chunk7A_1_vi.txt`, `chunk7B_1_vi.txt`,... 
   - Đảm bảo bám sát từ vựng gốc (giữ lại từ chuyên ngành trong ngoặc đơn).
   - Thêm các tag hình ảnh `<!-- IMAGE_PLACEHOLDER: ... -->` tại những vị trí có biểu đồ, hình vẽ.
5. **Ghép file và Xuất HTML:**
   - Tạo file `build_html_day07.py`.
   - Đọc các chunk tiếng Anh và tiếng Việt.
   - Sử dụng `marked.js` để tạo trang `Buoi_07.html` có 2 tab (English / Tiếng Việt).
6. **Kiểm tra:** Xác minh trang HTML hiển thị chính xác.
