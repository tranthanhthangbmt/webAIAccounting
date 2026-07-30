# Kế hoạch dịch thuật chi tiết: Chương 2 - Foundational Data Analysis Skills

## 1. Mục tiêu và Tài liệu nguồn
- **Nguồn:** `TaiLieu/textbookForPractice/Ch_02_Foundational Data Analysis Skills.pdf` (Tổng cộng: 70 trang).
- **Mục tiêu:** Dịch toàn bộ nội dung sang Tiếng Việt một cách cực kỳ chi tiết (không tóm tắt), đồng thời chèn các hình ảnh đã được chuẩn bị sẵn (trong `Figures/Ch_02/`) vào đúng vị trí văn bản.
- **Đầu ra:** File Markdown `docs/practice_ch02.md` để đưa lên trang web (Docsify) và được liên kết trong menu `_sidebar.md`.

## 2. Phương pháp Phân chia (Chunking Strategy)
Cuốn sách có cấu trúc rõ ràng theo 5 mục tiêu học tập (LO 2.1 - LO 2.5). Do tài liệu dài 70 trang, tôi sẽ chia PDF thành 10 phần (Chunks) tuân thủ đúng quy chuẩn đã thống nhất từ Chương 1:

- **Chunk 1:** Phần mở đầu & LO 2.1 (Relational Databases, Joining Tables).
- **Chunk 2:** LO 2.2 (Basic Functions for Data Analysis).
- **Chunk 3:** LO 2.3 (Using Pivot Tables, Filtering Pivot Tables).
- **Chunk 4:** LO 2.4 (Descriptive measures, Correlation Analysis).
- **Chunk 5:** LO 2.5 (Data visualization).
- **Chunk 6:** Chương đánh giá và Ôn tập (Chapter Review and Practice) bao gồm Tóm tắt chương và Thuật ngữ (LO 2-1 đến LO 2-5).
- **Chunk 7:** Câu hỏi trắc nghiệm và Thảo luận (Multiple Choice & Discussion Questions).
- **Chunk 8:** Bài tập ngắn (Brief Exercises). Yêu cầu **dịch chi tiết toàn bộ bài tập**, không tóm tắt.
- **Chunk 9:** Bài tập (Exercises). Yêu cầu **dịch chi tiết toàn bộ bài tập** và **chèn đầy đủ các hình ảnh** liên quan vào nội dung, không được bỏ sót.
- **Chunk 10:** Bài tập tổng hợp / Tình huống thực tế (Problems / Cases). Yêu cầu **dịch chi tiết toàn bộ** và **chèn đầy đủ các hình ảnh**.

## 3. Quy tắc Dịch thuật & Định dạng (Translation & Formatting Rules)
1. **Dịch thuật chuyên sâu:** Đóng vai trò là một Chuyên gia Kế toán và Phân tích Dữ liệu để dịch sát nghĩa, giữ nguyên cấu trúc đoạn văn của tác giả, tuyệt đối không được tự ý tóm tắt.
2. **Bảo tồn thuật ngữ:** Đối với các khái niệm chuyên ngành, phải giữ nguyên từ tiếng Anh gốc trong ngoặc đơn ở lần xuất hiện đầu tiên.
3. **Trình bày song ngữ (Top Dual Tabs):** Có MỘT khối Tab duy nhất nằm ở trên cùng của trang:
   - Tab **Tiếng Việt** chứa toàn bộ nội dung đã dịch của tất cả các phần.
   - Tab **English** nhúng trực tiếp file PDF gốc.
   ```markdown
   <!-- tabs:start -->
   #### **Tiếng Việt**
   [Toàn bộ nội dung dịch của chương 2]
   #### **English**
   <object data="../TaiLieu/textbookForPractice/Ch_02_Foundational Data Analysis Skills.pdf" type="application/pdf" width="100%" height="800px"><p>Trình duyệt của bạn không hỗ trợ xem PDF trực tiếp.</p></object>
   <!-- tabs:end -->
   ```

## 4. Tích hợp Hình ảnh tự động (Image Integration)
Trong quá trình dịch, AI sẽ tự động thay thế các tham chiếu đến hình ảnh bằng cú pháp Markdown trỏ đến thư mục đã đổi tên.
- **Cú pháp minh họa:** `![ILLUSTRATION 2.1](../TaiLieu/textbookForPractice/Figures/Ch_02/ILLUSTRATION%202.1.png)` hoặc `![BE 2.1](../TaiLieu/textbookForPractice/Figures/Ch_02/BE%202.1.png)`

## 5. Các bước Thực thi (Execution Steps)
1. **Extract Text:** Dùng Python (PyMuPDF) để trích xuất text thô từ 70 trang PDF.
2. **Chunk & Translate:** Đẩy từng Chunk vào AI để dịch với các ràng buộc trên.
3. **Assemble:** Hợp nhất các bản dịch lại thành file `docs/practice_ch02.md`.
4. **Update Sidebar:** Cập nhật file `_sidebar.md` để thêm mục `Thực hành: Chương 2` vào menu điều hướng.
