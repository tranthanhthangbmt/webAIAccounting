# Lập kế hoạch: Thêm Tab Bài tập Trắc nghiệm (Interactive Quiz) cho Buổi 6

Tiếp nối sự thành công của các buổi trước, tôi sẽ lập kế hoạch xây dựng bộ 30 câu hỏi trắc nghiệm tương tác cho Buổi 6. Toàn bộ nội dung sẽ được trích xuất bám sát vào tài liệu học tập của Buổi 6.

## Nguồn tài liệu tham khảo chính (Buổi 6)
- **Slide bài giảng:** `TaiLieu/slideAIAcc/Slide_AIAcc_Day06.pdf` (và source slide liên quan).
- **Tài liệu đọc 1:** `textbook/Buoi_06A_Chương 5 (Case study 4_ Tackling public sector corruption).pdf` (Sử dụng bản dịch trong `docs/buoi_06.md`).
- **Tài liệu đọc 2:** `textbook/Buoi_06B_2. Chương 1 (Preserving financial stability).pdf` (Sử dụng bản dịch trong `docs/buoi_06.md`).

## Yêu cầu cốt lõi (Theo yêu cầu từ người dùng)
- **Độ dài đáp án MCQ (Rất Quan Trọng):** Đảm bảo tuyệt đối rằng trong các câu hỏi trắc nghiệm nhiều lựa chọn (MCQ), **đáp án đúng có độ dài ngang bằng hoặc ngắn hơn các đáp án sai**. Điều này nhằm tránh tạo ra lỗ hổng giúp người trả lời "đoán mò" dựa vào cảm quan độ dài của đáp án.
- **Phân bổ dạng câu:** Duy trì bộ 30 câu hỏi đa dạng bao gồm:
  1. Trắc nghiệm (MCQ)
  2. Kéo thả điền từ (Fill-in-the-blanks)
  3. Ghép nối (Matching)
  4. Sắp xếp thứ tự (Ordering)

## Proposed Changes

Tôi sẽ thiết lập môi trường Quiz tương tự như các bài trước cho Buổi 6.

### Khởi tạo thư mục và file Quiz
#### [NEW] `quizzes/Day06/index.html`
- Sao chép bộ khung giao diện chuẩn từ các buổi trước.
- Cập nhật tiêu đề thành "Buổi 6".
- Viết và chạy script Python (`update_quiz_day06.py`) để sinh tự động mã JSON chứa 30 câu hỏi và nhúng vào tệp HTML này.

### Cập nhật File Markdown
#### [MODIFY] `docs/buoi_06.md`
- Tôi sẽ đọc tệp `docs/buoi_06.md` để lấy dữ liệu nội dung bài học.
- Chèn thêm tab **📝 Bài tập Trắc nghiệm** vào vị trí cuối tệp (ngay trước thẻ đóng tab `<!-- tabs:end -->`).
- Mã nhúng `iframe` sẽ trỏ tới giao diện của `quizzes/Day06/index.html`.

## Verification Plan
1. Lưu trữ bản kế hoạch này thành tệp `depPlan/createQuizDay06.md`.
2. Kiểm tra trực tiếp nội dung trong `docs/buoi_06.md` để lấy ngữ cảnh và dữ liệu.
3. Sinh câu hỏi và nhúng vào `quizzes/Day06`.
4. Mở trình duyệt tại `/#/docs/buoi_06`, trực tiếp chơi thử vài câu (đặc biệt chú ý độ dài các câu hỏi MCQ) để kiểm tra chất lượng trước khi báo cáo hoàn thành.
