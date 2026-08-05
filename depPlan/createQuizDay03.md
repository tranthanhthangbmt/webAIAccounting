# Lập kế hoạch: Thêm Tab Bài tập Trắc nghiệm (Interactive Quiz) cho Buổi 3

Dựa trên sự thành công của quy trình làm Buổi 2, tôi sẽ lập kế hoạch xây dựng bộ 30 câu hỏi trắc nghiệm tương tác cho Buổi 3 với nội dung tập trung vào: **"Machine Reasoning, ML, DL, NLP, cùng Đạo đức và Pháp luật trong Generative AI"**. Toàn bộ kiến thức sẽ được lấy chính xác từ các tài liệu học tập của Buổi 3.

## Nguồn tài liệu tham khảo chính (Buổi 3)
1. **Slide bài giảng:** `TaiLieu/slideAIAcc/Slide_AIAcc_Day03.pdf` (dựa trên source .tex và slide PDF)
2. **Tài liệu đọc 1:** `textbook/Buoi_03A_Chương 1 (Machine Reasoning, ML, DL, NLP).pdf` (dựa trên bản dịch trong docs/buoi_03.md)
3. **Tài liệu đọc 2:** `textbook/Buoi_03B_2. Chương 15 (Ethics and Laws_ Governing Generative AI’s Role...).pdf` (dựa trên bản dịch trong docs/buoi_03.md)

## Phạm vi kiến thức bao phủ
1. **Machine Reasoning:** Khả năng lập luận của máy móc, các hệ chuyên gia (Expert systems).
2. **Machine Learning (ML) & Deep Learning (DL):** Khái niệm, cách máy tính học từ dữ liệu, cấu trúc mạng nơ-ron sâu.
3. **Natural Language Processing (NLP):** Xử lý ngôn ngữ tự nhiên, phân tích cảm xúc, chatbot.
4. **Ethics (Đạo đức):** Các vấn đề đạo đức liên quan đến Trí tuệ nhân tạo tạo sinh (Generative AI), thiên kiến thuật toán (bias).
5. **Laws (Pháp luật):** Khuôn khổ pháp lý, quyền tác giả (copyright) đối với tác phẩm do AI tạo ra, quyền riêng tư và bảo vệ dữ liệu.

## Proposed Changes

Tôi sẽ tạo trang HTML tĩnh mới chứa 30 câu hỏi và nhúng vào `docs/buoi_03.md`.

### Khởi tạo thư mục và file Quiz
#### [NEW] `quizzes/Day03/index.html`
- **Tái sử dụng hoàn toàn** bộ khung giao diện, CSS và JS từ `quizzes/Day01` (và `Day02`).
- Biên soạn 30 câu hỏi mới tập trung vào kiến thức Buổi 3, gồm đầy đủ 4 dạng:
  - **Trắc nghiệm nhiều lựa chọn (MCQ)**
  - **Ghép nối (Matching)**
  - **Sắp xếp thứ tự (Ordering)**
  - **Kéo thả điền từ (Fill-in-the-blanks)**

### Cập nhật File Markdown
#### [MODIFY] `docs/buoi_03.md`
Thêm tab mới vào cuối file, ngay trước `<!-- tabs:end -->`:

```markdown
#### ** 📝 Bài tập Trắc nghiệm **

<iframe src="quizzes/Day03/index.html" style="width: 100%; min-height: 700px; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>
```

## Verification Plan
- Chạy script Python (ví dụ: `update_quiz_day03.py`) để tự động nhúng 30 câu hỏi vào file `index.html`.
- Lưu bản kế hoạch này thành `depPlan/createQuizDay03.md` để lưu trữ.
- Tải lại trang web (`/#/docs/buoi_03`), kiểm tra tab **Bài tập Trắc nghiệm** đảm bảo không có lỗi hiển thị và tất cả các tính năng tương tác (như kéo thả, ghép nối) hoạt động tốt.
