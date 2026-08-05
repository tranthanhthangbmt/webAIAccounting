# Lập kế hoạch: Thêm Tab Bài tập Trắc nghiệm (Interactive Quiz) cho Buổi 2

Dựa trên yêu cầu của bạn, hệ thống bài tập trắc nghiệm Buổi 2 ("AI, Blockchain và Dữ liệu lớn trong Kinh tế - Tài chính") sẽ được xây dựng gồm 30 câu hỏi. Toàn bộ nội dung kiến thức để soạn câu hỏi sẽ được trích xuất **chính xác và trực tiếp** từ các nguồn tài liệu của Buổi 2 như sau:

## Nguồn tài liệu tham khảo chính
1. **Slide bài giảng:** `TaiLieu/slideAIAcc/Slide_AIAcc_Day02.pdf` (dựa trên source .tex)
2. **Tài liệu đọc 1:** `textbook/Buoi_02A_Chương 1 (AI and Finance_Mục 1.2, 1.6, 1.7, 1.15) 2. Các phần về Big Data và Blockchain.pdf` (dựa trên bản dịch trong docs/buoi_02.md)
3. **Tài liệu đọc 2:** `textbook/Buoi_02B_Phần Big Data & Blockchain.pdf` (dựa trên bản dịch trong docs/buoi_02.md)

## Phạm vi kiến thức bao phủ (từ các nguồn trên)
1. **Bitcoin và Tiền tệ (Bitcoin as Money):** Các khái niệm về tiền ảo, blockchain, quan điểm pháp lý, CBDC, Litecoin, Ethereum, Zcash.
2. **Vũ trụ ảo trong Tài chính (Metaverse & DeFi):** Ngân hàng ảo, giao dịch thuật toán, tài sản kỹ thuật số.
3. **AI, DeFi, và NFTs:** Sự kết hợp giữa AI sáng tạo và bản quyền NFT. NFT làm tài sản thế chấp.
4. **Chuỗi khối và AI (Blockchain & AI):** Tính minh bạch, bảo mật, và hợp đồng thông minh.
5. **Khoa học Dữ liệu (Data Science) & Dữ liệu lớn (Big Data):** Mô hình Venn của Khoa học dữ liệu, Phân tích kinh doanh, và đặc trưng của Big Data.

## Proposed Changes

Tôi sẽ tạo một trang HTML tĩnh chứa 30 câu hỏi và nhúng nó vào file `docs/buoi_02.md`.

### Khởi tạo thư mục và file Quiz
#### [NEW] `quizzes/Day02/index.html`
- **Tái sử dụng hoàn toàn** bộ khung giao diện, thiết kế màu sắc (xanh dương/trắng) và mã điều khiển từ `quizzes/Day01/index.html` vì nó đã hoạt động rất ổn định và hiện đại.
- Biên soạn 30 câu hỏi mới dựa trên 3 file tài liệu đã nêu (gồm các dạng: MCQ, Ghép nối, Sắp xếp, Kéo thả điền từ).

### Cập nhật File Markdown
#### [MODIFY] `docs/buoi_02.md`
Thêm tab mới vào cuối file, ngay trước `<!-- tabs:end -->`:

```markdown
#### ** 📝 Bài tập Trắc nghiệm **

<iframe src="quizzes/Day02/index.html" style="width: 100%; min-height: 700px; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>
```

## Verification Plan
- Viết mã Python để tạo câu hỏi và nhúng vào `quizzes/Day02/index.html`.
- Tải lại trang web chính (`/#/docs/buoi_02`) và chuyển sang tab **Bài tập Trắc nghiệm**.
- Kiểm tra tính năng tương tác.
