# Lập kế hoạch: Thêm Tab Bài tập Trắc nghiệm (Interactive Quiz) cho Buổi 4

Tiếp nối quy trình thành công của các buổi trước, tôi sẽ xây dựng hệ thống 30 câu hỏi trắc nghiệm tương tác cho Buổi 4 với chủ đề: **"Phân khúc Thị trường (Market Segmentation) và Dự báo Sức khỏe Tài chính (Forecasting Financial Health)"**. Toàn bộ nội dung sẽ được trích xuất bám sát vào các tài liệu của Buổi 4.

## Nguồn tài liệu tham khảo chính (Buổi 4)
1. **Slide bài giảng:** `TaiLieu/slideAIAcc/Slide_AIAcc_Day04.pdf` (tham chiếu nội dung từ file `.tex`).
2. **Tài liệu đọc 1:** `textbook/Buoi_04A_Chương 5 (Market Segmentation...).pdf` (sử dụng bản dịch tiếng Việt trong `docs/buoi_04.md`).
3. **Tài liệu đọc 2:** `textbook/Buoi_04B_Chương 10 (Forecasting Financial Health...).pdf` (sử dụng bản dịch tiếng Việt trong `docs/buoi_04.md`).

## Yêu cầu bổ sung từ người dùng
- Các câu hỏi dạng nhiều lựa chọn (MCQ) phải được thiết kế sao cho **độ dài của đáp án đúng không được dài hơn rõ rệt so với các đáp án sai**, tránh việc học viên dễ dàng đoán được đáp án dựa vào độ dài.

## Phạm vi kiến thức bao phủ
1. **Phân khúc thị trường (Market Segmentation):** Các khái niệm và phương pháp sử dụng công nghệ và AI để phân tích khách hàng.
2. **Dự báo sức khỏe tài chính (Forecasting Financial Health):** Các kỹ thuật dự báo (ví dụ: phân tích chuỗi thời gian, hồi quy), cách AI giúp đánh giá và dự báo tài chính.
3. **Ứng dụng thực tiễn:** Cách Kế toán viên có thể tận dụng các thuật toán máy học để đánh giá hiệu suất kinh doanh và rủi ro.

## Proposed Changes

Tôi sẽ tạo thư mục mới cho Buổi 4 và nhúng trang trắc nghiệm vào nội dung chính.

### Khởi tạo thư mục và file Quiz
#### [NEW] `quizzes/Day04/index.html`
- **Tái sử dụng hoàn toàn** bộ khung giao diện, thiết kế CSS hiện đại và logic Javascript từ các buổi trước nhằm đảm bảo tính đồng bộ, chạy mượt mà và nhẹ.
- Biên soạn **30 câu hỏi** mới, vẫn chia đủ 4 dạng như cũ:
  - **Trắc nghiệm nhiều lựa chọn (MCQ)**
  - **Ghép nối (Matching)**
  - **Sắp xếp thứ tự (Ordering)**
  - **Kéo thả điền từ (Fill-in-the-blanks)**

### Cập nhật File Markdown
#### [MODIFY] `docs/buoi_04.md`
Thêm tab mới vào cuối file, vị trí nằm ngay trước `<!-- tabs:end -->`:

```markdown
#### ** 📝 Bài tập Trắc nghiệm **

<iframe src="quizzes/Day04/index.html" style="width: 100%; min-height: 700px; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>
```

## Verification Plan
- Chạy script Python để tự động tạo và chèn nội dung 30 câu hỏi vào file `quizzes/Day04/index.html`.
- Lưu giữ cấu trúc kế hoạch này thành `depPlan/createQuizDay04.md` phục vụ việc truy xuất sau này.
- Mở URL `/#/docs/buoi_04` trên trình duyệt nội bộ, chuyển qua tab **Bài tập Trắc nghiệm** để kiểm tra giao diện, đảm bảo hiển thị đúng câu hỏi và tính năng tương tác không có lỗi.
