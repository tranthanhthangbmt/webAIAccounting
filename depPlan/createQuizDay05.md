# Lập kế hoạch: Thêm Tab Bài tập Trắc nghiệm (Interactive Quiz) cho Buổi 5

Kế thừa toàn bộ cấu trúc và kinh nghiệm từ Buổi 1 đến Buổi 4, tôi sẽ lập kế hoạch xây dựng hệ thống 30 câu hỏi trắc nghiệm tương tác cho Buổi 5. Nội dung sẽ được trích xuất hoàn toàn dựa trên các tài liệu giảng dạy của Buổi 5 (từ slide và các chương textbook tương ứng).

## Nguồn tài liệu tham khảo chính (Buổi 5)
- **Slide bài giảng:** `TaiLieu/slideAIAcc/Slide_AIAcc_Day05.pdf` (và source `.tex`).
- **Tài liệu đọc 1:** `textbook/Buoi_05A_Chương 12 (Managing Decision Uncertainty).pdf` (sử dụng bản dịch tiếng Việt trong `docs/buoi_05.md`).
- **Tài liệu đọc 2:** `textbook/Buoi_05B_Chương 14 (New Product Development).pdf` (sử dụng bản dịch tiếng Việt trong `docs/buoi_05.md`).

## Yêu cầu cốt lõi (Theo yêu cầu từ người dùng)
- **Độ dài đáp án MCQ:** Đảm bảo chặt chẽ rằng trong các câu hỏi trắc nghiệm nhiều lựa chọn (MCQ), **đáp án đúng không được dài hơn rõ rệt so với các đáp án sai**. Điều này ngăn học viên sử dụng "mẹo" nhìn độ dài để đoán đáp án.
- **Phân bổ dạng câu:** Duy trì 30 câu hỏi trải đều qua 4 định dạng tương tác: 
  1. Trắc nghiệm (MCQ)
  2. Kéo thả điền từ (Fill-in-the-blanks)
  3. Ghép nối (Matching)
  4. Sắp xếp thứ tự (Ordering)

## Proposed Changes

Tôi sẽ tạo và tích hợp môi trường Quiz tĩnh cho Buổi 5.

### Khởi tạo thư mục và file Quiz
#### [NEW] `quizzes/Day05/index.html`
- Sao chép và tái sử dụng bộ khung (HTML/CSS/JS) đã được tối ưu hóa từ Buổi 4 sang Buổi 5.
- Cập nhật tiêu đề và các nhãn hiển thị thành "Buổi 5".
- Chạy một script Python (ví dụ: `update_quiz_day05.py`) để trộn và chèn tự động 30 câu hỏi mới vào file này.

### Cập nhật File Markdown
#### [MODIFY] `docs/buoi_05.md`
- Tôi sẽ kiểm tra file `docs/buoi_05.md`.
- Chèn thêm tab **📝 Bài tập Trắc nghiệm** vào cuối file, ngay trước vị trí đóng tab `<!-- tabs:end -->`.
- Mã nhúng `iframe` sẽ trỏ tới `quizzes/Day05/index.html`.

## Verification Plan
1. Lưu trữ bản kế hoạch này thành `depPlan/createQuizDay05.md`.
2. Truy xuất nội dung `docs/buoi_05.md` để lập danh sách câu hỏi.
3. Sinh và nhúng câu hỏi.
4. Mở trang web tại `/#/docs/buoi_05`, tự tay kiểm tra tab mới, chơi thử vài câu (đặc biệt là xem xét kỹ độ dài của các câu MCQ) để đảm bảo chất lượng trước khi báo cáo kết quả.
