# Kế hoạch dịch thuật chi tiết: Chương 1 - Data and Analytics in the Accounting Profession

## 1. Mục tiêu và Tài liệu nguồn
- **Nguồn:** `TaiLieu/textbookForPractice/Ch_01_Data and Analytics in the Accounting Profession.pdf` (Tổng cộng: 42 trang).
- **Mục tiêu:** Dịch toàn bộ nội dung sang Tiếng Việt một cách cực kỳ chi tiết (không tóm tắt), đồng thời chèn các hình ảnh (`ILLUSTRATION x.x`) đã được chuẩn bị sẵn vào đúng vị trí văn bản.
- **Đầu ra:** File Markdown `docs/practice_ch01.md` để đưa lên trang web (Docsify) và được liên kết trong menu `_sidebar.md`.

## 2. Phương pháp Phân chia (Chunking Strategy)
Cuốn sách có cấu trúc rõ ràng theo các mục tiêu học tập (Learning Objectives - LO). Do tài liệu dài 42 trang, việc đẩy toàn bộ vào AI cùng lúc sẽ bị giới hạn token và giảm chất lượng dịch. Tôi sẽ chia PDF thành 7-8 phần (Chunks) dựa theo các heading chính:

- **Chunk 1:** Phần mở đầu & LO 1-1 (Văn hóa dựa trên dữ liệu trong kế toán).
- **Chunk 2:** LO 1-2 (Vai trò của dữ liệu và phân tích trong kế toán).
- **Chunk 3:** LO 1-3 (Bộ kỹ năng phân tích dữ liệu cần thiết cho kế toán viên).
- **Chunk 4:** LO 1-4 (Mô hình vòng đời dữ liệu - Data Lifecycle).
- **Chunk 5:** LO 1-5 (Các sáng kiến dữ liệu và chiến lược).
- **Chunk 6:** Chương đánh giá và Ôn tập (Chapter Review and Practice) bao gồm Tóm tắt chương và Thuật ngữ (LO 1-1 đến LO 1-4).
- **Chunk 7:** Câu hỏi trắc nghiệm và Thảo luận (Multiple Choice & Discussion Questions).
- **Chunk 8:** Bài tập ngắn (Brief Exercises). Yêu cầu **dịch chi tiết toàn bộ bài tập**, không tóm tắt.
- **Chunk 9:** Bài tập (Exercises). Yêu cầu **dịch chi tiết toàn bộ bài tập** và **chèn đầy đủ các hình ảnh** liên quan vào nội dung, không được bỏ sót để đảm bảo sinh viên có thể tự thực hành.
- **Chunk 10:** Bài tập tổng hợp / Tình huống thực tế (Problems / Cases). Yêu cầu **dịch chi tiết toàn bộ** và **chèn đầy đủ các hình ảnh**.

*(Lưu ý: Cấu trúc phân chia này (Chunk 1-10) và yêu cầu dịch chi tiết bài tập, chèn ảnh đầy đủ sẽ được áp dụng làm quy chuẩn bắt buộc cho cả Chương 2 và tất cả các chương thực hành sau này).*
## 3. Quy tắc Dịch thuật & Định dạng (Translation & Formatting Rules)
1. **Dịch thuật chuyên sâu:** Đóng vai trò là một Chuyên gia Kế toán và Khoa học Dữ liệu để dịch sát nghĩa, giữ nguyên cấu trúc đoạn văn của tác giả, tuyệt đối không được tự ý tóm tắt.
2. **Bảo tồn thuật ngữ:** Đối với các khái niệm chuyên ngành Kế toán (Accounting) hoặc Phân tích (Analytics), phải giữ nguyên từ tiếng Anh gốc trong ngoặc đơn ở lần xuất hiện đầu tiên.
   - *Ví dụ:* Kế toán quản trị (Management Accounting), Vòng đời dữ liệu (Data Lifecycle).
3. **Trình bày song ngữ (Top Dual Tabs):** Tài liệu sẽ được định dạng theo cấu trúc Tab của Docsify, nhưng chỉ có MỘT khối Tab duy nhất nằm ở trên cùng của trang.
   - Tab **Tiếng Việt** sẽ chứa toàn bộ nội dung đã dịch của tất cả các phần (chunks).
   - Tab **English** sẽ nhúng trực tiếp file PDF gốc của chương đó để sinh viên có thể xem bản gốc có độ phân giải cao.
   ```markdown
   <!-- tabs:start -->
   #### **Tiếng Việt**
   [Toàn bộ nội dung dịch của chương]
   #### **English**
   <object data="../TaiLieu/textbookForPractice/Ch_01_Data and Analytics in the Accounting Profession.pdf" type="application/pdf" width="100%" height="800px"><p>Trình duyệt của bạn không hỗ trợ xem PDF trực tiếp.</p></object>
   <!-- tabs:end -->
   ```

## 4. Tích hợp Hình ảnh tự động (Image Integration)
Trong quá trình dịch, khi văn bản gốc có đề cập đến các hình ảnh hoặc biểu đồ (ví dụ: *Illustration 1.1*, *BE 1.6*), AI sẽ tự động thay thế bằng cú pháp hình ảnh Markdown, trỏ trực tiếp đến thư mục ảnh đã được bóc tách và đổi tên bằng OCR trước đó:
- **Cú pháp:** `![ILLUSTRATION 1.1](../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION%201.1.png)`
- Bằng cách này, khi sinh viên đọc trên Web, hình ảnh độ phân giải cao sẽ hiển thị ngay lập tức cùng với văn bản.

## 5. Các bước Thực thi (Execution Steps)
1. **Extract Text:** Dùng Python (PyMuPDF) để trích xuất text thô từ toàn bộ 42 trang PDF.
2. **Chunk & Translate:** Đẩy từng Chunk vào AI để dịch với các ràng buộc về thuật ngữ và hình ảnh như trên.
3. **Assemble:** Hợp nhất các bản dịch lại thành file `docs/practice_ch01.md`.
4. **Update Sidebar:** Cập nhật file `_sidebar.md` để thêm mục `Thực hành: Chương 1` vào menu điều hướng.
