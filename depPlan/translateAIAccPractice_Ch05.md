# Kế hoạch dịch thuật chi tiết: Chương 5 - Data Preparation

## 1. Mục tiêu và Tài liệu nguồn
- **Nguồn:** `TaiLieu/textbookForPractice/Ch_05_Analysis_ Data Preparation.pdf` (Tổng cộng: 76 trang).
- **Mục tiêu:** Dịch toàn bộ nội dung sang Tiếng Việt một cách cực kỳ chi tiết (không tóm tắt), đồng thời chèn các hình ảnh đã được chuẩn bị sẵn vào đúng vị trí văn bản.
- **Đầu ra:** File Markdown `docs/practice_ch05.md` để đưa lên trang web (Docsify) và được liên kết trong menu `_sidebar.md`.

## 2. Phương pháp Phân chia (Chunking Strategy)
Do tài liệu khá dài (76 trang), việc đưa toàn bộ nội dung vào AI cùng lúc sẽ gây quá tải token và làm giảm chất lượng dịch thuật. Tài liệu sẽ được chia thành 12 phần (chunks) dựa trên cấu trúc các mục tiêu học tập (LO) và các phần bài tập:

- **Chunk 1:** Phần mở đầu & LO 5.1
- **Chunk 2:** LO 5.2
- **Chunk 3:** LO 5.3
- **Chunk 4:** LO 5.4
- **Chunk 5:** LO 5.5
- **Chunk 6:** LO 5.6 (Nếu có)
- **Chunk 7:** Chapter Review (Tóm tắt chương và Thuật ngữ).
- **Chunk 8:** Multiple Choice & Discussion Questions (Câu hỏi trắc nghiệm và Thảo luận).
- **Chunk 9:** Brief Exercises (Bài tập ngắn). Yêu cầu **dịch chi tiết toàn bộ bài tập**, không tóm tắt.
- **Chunk 10:** Exercises (Bài tập) - Phần 1. Yêu cầu **dịch chi tiết toàn bộ bài tập** và **chèn đầy đủ các hình ảnh** liên quan.
- **Chunk 11:** Exercises (Bài tập) - Phần 2.
- **Chunk 12:** Professional Application Cases (Bài tập tổng hợp / Tình huống thực tế). Yêu cầu **dịch chi tiết toàn bộ** và **chèn đầy đủ các hình ảnh**.

## 3. Quy tắc Dịch thuật & Định dạng (Translation & Formatting Rules)
1. **Dịch thuật chuyên sâu:** Đóng vai trò là một Chuyên gia Kế toán và Khoa học Dữ liệu để dịch sát nghĩa, giữ nguyên cấu trúc đoạn văn của tác giả, tuyệt đối không được tự ý tóm tắt.
2. **Bảo tồn thuật ngữ:** Đối với các khái niệm chuyên ngành Kế toán (Accounting) hoặc Phân tích (Analytics) cũng như các hàm công nghệ (như SQL, Excel), phải giữ nguyên từ tiếng Anh gốc trong ngoặc đơn ở lần xuất hiện đầu tiên.
3. **Trình bày song ngữ (Top Dual Tabs):** Tài liệu sẽ được định dạng theo cấu trúc Tab của Docsify, với một khối Tab duy nhất nằm ở trên cùng của trang.
   - Tab **Tiếng Việt** sẽ chứa toàn bộ nội dung đã dịch của tất cả các phần (chunks).
   - Tab **English** sẽ nhúng trực tiếp file PDF gốc của chương.
   ```markdown
   <!-- tabs:start -->
   #### **Tiếng Việt**
   [Toàn bộ nội dung dịch của chương]
   #### **English**
   <iframe src="TaiLieu/textbookForPractice/Ch_05_Analysis_%20Data%20Preparation.pdf" width="100%" height="800px"></iframe>
   <!-- tabs:end -->
   ```

## 4. Tích hợp Hình ảnh tự động (Image Integration)
Trong quá trình dịch, khi văn bản gốc có đề cập đến các hình ảnh hoặc biểu đồ, thay thế bằng cú pháp hình ảnh Markdown, trỏ trực tiếp đến thư mục ảnh:
- **Cú pháp:** `![Tên_Ảnh](../TaiLieu/textbookForPractice/Figures/Ch_05/Tên_Ảnh.png)`
- Nguồn hình ảnh: Lấy từ thư mục `TaiLieu/textbookForPractice/Figures/Ch_05` (có khoảng 94 ảnh đã được giải nén sẵn với định dạng tên như `ILLUSTRATION 5.1.png`, `BE 5.1.png`, v.v.). Script `update_practice_images.py` sẽ được sử dụng để tự động inject link ảnh vào đúng vị trí sau khi dịch.

## 5. Các bước Thực thi (Execution Steps)
1. **Extract Text:** Chạy script Python (ví dụ: `extract_ch05.py`) để trích xuất text thô từ 76 trang PDF, chia đều vào các file `ch05_chunk_*.txt`.
2. **Translate (Dịch):** Đẩy từng Chunk vào AI để dịch sang tiếng Việt và lưu kết quả vào `ch05_tr_chunk_*.md`.
3. **Inject Images:** Sử dụng script để quét và tự động chèn các image link `![...](../TaiLieu/...)` vào file dịch tương ứng dựa trên keyword.
4. **Assemble:** Hợp nhất các bản dịch lại thành file `docs/practice_ch05.md` thông qua script `assemble_practice_ch05.py`.
5. **Update UI:** Cập nhật file `_sidebar.md` để gắn link hiển thị bài Thực hành 5 lên thanh điều hướng của website.
