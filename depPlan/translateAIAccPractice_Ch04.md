# Kế hoạch dịch thuật chi tiết: Chương 4 - Planning Data Analyses

## 1. Mục tiêu và Tài liệu nguồn
- **Nguồn:** `TaiLieu/textbookForPractice/Ch_04_Planning Data and.pdf` (Tổng cộng: 60 trang).
- **Mục tiêu:** Dịch toàn bộ nội dung sang Tiếng Việt một cách cực kỳ chi tiết (không tóm tắt), đồng thời chèn các hình ảnh đã được chuẩn bị sẵn vào đúng vị trí văn bản.
- **Đầu ra:** File Markdown `docs/practice_ch04.md` để đưa lên trang web (Docsify) và được liên kết trong menu `_sidebar.md`.

## 2. Phương pháp Phân chia (Chunking Strategy)
Cuốn sách có cấu trúc rõ ràng theo các mục tiêu học tập (Learning Objectives - LO). Do tài liệu dài 60 trang, việc đẩy toàn bộ vào AI cùng lúc sẽ bị giới hạn token và giảm chất lượng dịch. Tôi sẽ chia PDF thành 10 phần (Chunks) dựa theo các heading chính:

- **Chunk 1:** Phần mở đầu & LO 4.1 (Identify the components of...).
- **Chunk 2:** LO 4.2 (Describe how to develop a...).
- **Chunk 3:** LO 4.3 (Explain how an analysis...).
- **Chunk 4:** LO 4.4 (Summarize data and...).
- **Chunk 5:** Chapter Review (Tóm tắt chương và Thuật ngữ).
- **Chunk 6:** Multiple Choice & Discussion Questions (Câu hỏi trắc nghiệm và Thảo luận).
- **Chunk 7:** Brief Exercises (Bài tập ngắn). Yêu cầu **dịch chi tiết toàn bộ bài tập**, không tóm tắt.
- **Chunk 8:** Exercises (Bài tập) - Phần 1. Yêu cầu **dịch chi tiết toàn bộ bài tập** và **chèn đầy đủ các hình ảnh** liên quan.
- **Chunk 9:** Exercises (Bài tập) - Phần 2.
- **Chunk 10:** Professional Application Cases (Bài tập tổng hợp / Tình huống thực tế). Yêu cầu **dịch chi tiết toàn bộ** và **chèn đầy đủ các hình ảnh**.

## 3. Quy tắc Dịch thuật & Định dạng (Translation & Formatting Rules)
1. **Dịch thuật chuyên sâu:** Đóng vai trò là một Chuyên gia Kế toán và Khoa học Dữ liệu để dịch sát nghĩa, giữ nguyên cấu trúc đoạn văn của tác giả, tuyệt đối không được tự ý tóm tắt.
2. **Bảo tồn thuật ngữ:** Đối với các khái niệm chuyên ngành Kế toán (Accounting) hoặc Phân tích (Analytics), phải giữ nguyên từ tiếng Anh gốc trong ngoặc đơn ở lần xuất hiện đầu tiên.
3. **Trình bày song ngữ (Top Dual Tabs):** Tài liệu sẽ được định dạng theo cấu trúc Tab của Docsify, nhưng chỉ có MỘT khối Tab duy nhất nằm ở trên cùng của trang.
   - Tab **Tiếng Việt** sẽ chứa toàn bộ nội dung đã dịch của tất cả các phần (chunks).
   - Tab **English** sẽ nhúng trực tiếp file PDF gốc của chương.
   ```markdown
   <!-- tabs:start -->
   #### **Tiếng Việt**
   [Toàn bộ nội dung dịch của chương]
   #### **English**
   <iframe src="TaiLieu/textbookForPractice/Ch_04_Planning%20Data%20and.pdf" width="100%" height="800px"></iframe>
   <!-- tabs:end -->
   ```

## 4. Tích hợp Hình ảnh tự động (Image Integration)
Trong quá trình dịch, khi văn bản gốc có đề cập đến các hình ảnh hoặc biểu đồ, thay thế bằng cú pháp hình ảnh Markdown, trỏ trực tiếp đến thư mục ảnh:
- **Cú pháp:** `![Tên_Ảnh](../TaiLieu/textbookForPractice/Figures/Ch_04/Tên_Ảnh.png)`
- Trước khi dịch, cần trích xuất và đổi tên ảnh dựa trên nội dung PDF bằng OCR nếu ảnh chưa có tên chuẩn xác.

## 5. Các bước Thực thi (Execution Steps)
1. **Extract Images & Rename:** Đảm bảo tất cả các hình ảnh trong `Figures/Ch_04` được đặt tên chuẩn xác.
2. **Extract Text & Chunk:** Dùng Python phân tách text thô từ 60 trang PDF thành 10 files (chunks).
3. **Translate:** Đẩy từng Chunk vào mô hình AI để dịch chi tiết với các ràng buộc về thuật ngữ và hình ảnh như trên.
4. **Assemble:** Hợp nhất các bản dịch lại thành file `docs/practice_ch04.md`.
5. **Update UI:** Cập nhật file `_sidebar.md` và `walkthrough.md`.
