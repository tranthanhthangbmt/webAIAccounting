# Kế hoạch dịch thuật chi tiết: Chương 6 - Analysis: Information Modeling

## 1. Mục tiêu và Tài liệu nguồn
- **Nguồn:** `TaiLieu/textbookForPractice/Ch_06_Analysis_Data Preparation.pdf` (Tên file gốc trên máy, dự kiến nội dung nói về Information Modeling / Chuẩn bị & Mô hình dữ liệu).
- **Mục tiêu:** Dịch toàn bộ nội dung sang Tiếng Việt một cách cực kỳ chi tiết (không tóm tắt), đồng thời chèn các hình ảnh đã được chuẩn bị sẵn vào đúng vị trí văn bản.
- **Đầu ra:** File Markdown `docs/practice_ch06.md` để đưa lên trang web (Docsify) và được liên kết trong menu `_sidebar.md`.

## 2. Phương pháp Phân chia (Chunking Strategy)
Tài liệu sẽ được chia thành nhiều phần (chunks) dựa trên cấu trúc các mục tiêu học tập (LO) và các phần bài tập:
- **Chunk 1:** Phần mở đầu & LO 6.1
- **Chunk 2:** LO 6.2
- **Chunk 3:** LO 6.3
- **Chunk 4:** LO 6.4
- **Chunk 5:** LO 6.5 & 6.6
- **Chunk 6:** Chapter Review (Tóm tắt chương và Thuật ngữ).
- **Chunk 7:** Multiple Choice & Discussion Questions (Câu hỏi trắc nghiệm và Thảo luận).
- **Chunk 8:** Brief Exercises (Bài tập ngắn). Yêu cầu **dịch chi tiết toàn bộ bài tập**, không tóm tắt.
- **Chunk 9:** Exercises (Bài tập) - Phần 1. Yêu cầu **dịch chi tiết toàn bộ bài tập** và **chèn đầy đủ các hình ảnh** liên quan.
- **Chunk 10:** Exercises (Bài tập) - Phần 2.
- **Chunk 11:** Professional Application Cases (Bài tập tổng hợp / Tình huống thực tế). Yêu cầu **dịch chi tiết toàn bộ** và **chèn đầy đủ các hình ảnh**.

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
   <iframe src="TaiLieu/textbookForPractice/Ch_06_Analysis_Data%20Preparation.pdf" width="100%" height="800px"></iframe>
   <!-- tabs:end -->
   ```

## 4. Tích hợp Hình ảnh tự động (Image Integration)
Trong quá trình dịch, khi văn bản gốc có đề cập đến các hình ảnh hoặc biểu đồ, thay thế bằng cú pháp hình ảnh Markdown, trỏ trực tiếp đến thư mục ảnh:
- **Cú pháp:** `![Tên_Ảnh](../TaiLieu/textbookForPractice/Figures/Ch_06/Tên_Ảnh.png)`
- Nguồn hình ảnh: Lấy từ thư mục `TaiLieu/textbookForPractice/Figures/Ch_06` (đã có sẵn các file như `ILLUSTRATION 6.1.png`, `EX 6.10.png`, `BE 6.11.png`...).
- **Lưu ý quan trọng (Đã khắc phục từ Chương 5):** Không sử dụng định dạng Header `#### **...**` cho các dòng chứa chú thích ảnh hoặc tiêu đề bài tập phụ, thay vào đó chỉ dùng in đậm `**...**` để tránh xung đột làm vỡ Tab của Docsify.

## 5. Các bước Thực thi (Execution Steps)
1. **Extract Text:** Trích xuất text thô từ PDF, chia vào các file `scratch/ch06_chunk_*.txt`.
2. **Translate (Dịch):** Đẩy từng Chunk vào AI để dịch sang tiếng Việt và lưu kết quả vào `scratch/ch06_tr_chunk_*.md`.
3. **Assemble (Lắp ráp):** Hợp nhất các bản dịch lại thành file `docs/practice_ch06.md` thông qua script Python, tự động:
   - Xóa các artifact thừa (số trang, header rác của PDF).
   - Xử lý các tag in đậm cho các mục lục `LO 6.x` và `MINH HỌA/EX/BE`.
   - Giữ nguyên đánh số danh sách (`1. `, `2. `).
   - Chèn cú pháp hình ảnh `![...](../TaiLieu/...)` vào những nơi thích hợp.
4. **Update UI:** Cập nhật file `_sidebar.md` để gắn link hiển thị bài **Thực hành 6** lên thanh điều hướng của website.
