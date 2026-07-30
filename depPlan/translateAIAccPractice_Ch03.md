# Kế hoạch dịch thuật chi tiết: Chương 3 - Motivations and Objectives for Data Analysis

## 1. Mục tiêu và Tài liệu nguồn
- **Nguồn:** `TaiLieu/textbookForPractice/Ch_03_Motivations and Objectives for Data Analysis.pdf` (Tổng cộng: 64 trang).
- **Mục tiêu:** Dịch toàn bộ nội dung sang Tiếng Việt một cách cực kỳ chi tiết (không tóm tắt), đồng thời chèn các hình ảnh (`ILLUSTRATION x.x`, `EX x.x`, v.v.) đã được chuẩn bị sẵn vào đúng vị trí văn bản.
- **Đầu ra:** File Markdown `docs/practice_ch03.md` để đưa lên trang web (Docsify) và được liên kết trong menu `_sidebar.md`.

## 2. Phương pháp Phân chia (Chunking Strategy)
Cuốn sách có cấu trúc rõ ràng theo các mục tiêu học tập (Learning Objectives - LO). Do tài liệu dài 64 trang, việc đẩy toàn bộ vào AI cùng lúc sẽ bị giới hạn token và giảm chất lượng dịch. Tôi sẽ chia PDF thành 10 phần (Chunks) theo đúng quy chuẩn đã áp dụng cho Chương 1 và 2:

- **Chunk 1:** Phần mở đầu & LO 3.1 (Motivations for Data Analysis).
- **Chunk 2:** LO 3.2 (Descriptive Analysis Objectives).
- **Chunk 3:** LO 3.3 (Diagnostic Analysis Objectives).
- **Chunk 4:** LO 3.4 (Predictive Analysis Objectives).
- **Chunk 5:** LO 3.5 (Prescriptive Analysis Objectives).
- **Chunk 6:** LO 3.6 (Common Objectives in Professional Practice).
- **Chunk 7:** Chương đánh giá và Ôn tập (Chapter Review and Practice) bao gồm Tóm tắt chương và Thuật ngữ (LO 3.1 đến LO 3.6).
- **Chunk 8:** Bài tập ngắn (Brief Exercises). Yêu cầu **dịch chi tiết toàn bộ bài tập**, không tóm tắt.
- **Chunk 9:** Bài tập (Exercises). Yêu cầu **dịch chi tiết toàn bộ bài tập** và **chèn đầy đủ các hình ảnh** liên quan vào nội dung, không được bỏ sót.
- **Chunk 10:** Bài tập tổng hợp / Tình huống thực tế (Problems / Cases). Yêu cầu **dịch chi tiết toàn bộ** và **chèn đầy đủ các hình ảnh**.

## 3. Quy tắc Dịch thuật & Định dạng (Translation & Formatting Rules)
1. **Dịch thuật chuyên sâu:** Đóng vai trò là một Chuyên gia Kế toán và Phân tích Dữ liệu để dịch sát nghĩa, giữ nguyên cấu trúc đoạn văn của tác giả, tuyệt đối không được tự ý tóm tắt.
2. **Bảo tồn thuật ngữ:** Đối với các khái niệm chuyên ngành, phải giữ nguyên từ tiếng Anh gốc trong ngoặc đơn ở lần xuất hiện đầu tiên.
3. **Trình bày song ngữ (Top Dual Tabs):** Tài liệu sẽ được định dạng theo cấu trúc Tab của Docsify ở ngay phần trên cùng của trang.
   - Tab **Tiếng Việt** sẽ chứa toàn bộ nội dung đã dịch.
   - Tab **English** sẽ nhúng trực tiếp file PDF gốc.

## 4. Tích hợp Hình ảnh tự động (Image Integration)
Trong quá trình dịch, AI sẽ tự động thay thế bằng cú pháp hình ảnh Markdown, trỏ trực tiếp đến thư mục ảnh của Chương 3 (`TaiLieu/textbookForPractice/Figures/Ch_03/`):
- **Cú pháp:** `![Tên Hình Ảnh](../TaiLieu/textbookForPractice/Figures/Ch_03/Tên Hình Ảnh.png)`
- Bằng cách này, hình ảnh độ phân giải cao sẽ hiển thị ngay lập tức cùng với văn bản.

## 5. Các bước Thực thi (Execution Steps)
1. **Extract Text & Images:** Text đã được trích xuất (64 trang). Hình ảnh của Chương 3 đã có sẵn trong thư mục `Figures/Ch_03`.
2. **Chunk & Translate:** Tách text thô thành 10 file chunk (`ch03_chunk_1.txt` đến `ch03_chunk_10.txt`) và dịch lần lượt.
3. **Assemble:** Hợp nhất các bản dịch lại thành file `docs/practice_ch03.md`.
4. **Update Sidebar:** Cập nhật file `_sidebar.md` để thêm mục `Thực hành 3: Motivations and Objectives for Data Analysis` vào menu điều hướng.
