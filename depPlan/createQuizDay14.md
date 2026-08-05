# Kế hoạch Tạo Bài tập Trắc nghiệm - Buổi 14

## 1. Mục tiêu
Thiết kế bộ 30 câu hỏi trắc nghiệm tương tác cho **Buổi 14: Phân tích Dữ liệu Kế toán Chuyên sâu (Khám phá Dữ liệu & Trực quan hóa Kết quả)**. 

## 2. Các chủ đề trọng tâm (Theo `docs/buoi_14.md`)
- **Phần I: Khám phá Dữ liệu (Data Exploration):**
  - Exploratory Data Analysis (EDA) vs. Confirmatory Analysis.
  - Quy trình 4 bước khám phá dữ liệu.
  - Cấu trúc PivotTable (Fields, Rows, Columns, Values, Filters).
  - 6 kỹ thuật PivotTable cốt lõi trong kế toán.
  - 5 Mô hình Mối quan hệ Dữ liệu (Nominal, Distribution, Deviation, Ranking, Part-to-Whole).
- **Phần II: Truyền đạt Kết quả (Communicating Results):**
  - Nguyên tắc Data Storytelling (Kể chuyện bằng dữ liệu).
  - Các lỗi thường gặp khi trình bày bảng biểu (Clutter, Misleading axis).

## 3. Quy tắc cốt lõi về đáp án MCQ
- Các câu hỏi Multiple Choice: Nội dung (text) của lựa chọn được chỉ định là đúng (`correctAnswer`) **không được phép dài hơn** bất kỳ lựa chọn sai nào. Lý tưởng là ngắn hơn hoặc có độ dài tương đương, tránh việc lộ đáp án do người học nhìn ra lựa chọn dài nhất.

## 4. Các bước triển khai kỹ thuật
1. Khởi tạo thư mục `quizzes/Day14` bằng cách sao chép từ `quizzes/Day13`.
2. Tạo script Python `update_quiz_day14.py` định nghĩa mảng 30 câu hỏi chuẩn định dạng JSON, với 4 loại tương tác (Multiple choice, Matching, Fill-in-the-blanks, Ordering).
3. Chạy lệnh thực thi script trên để tiêm nội dung vào `index.html`.
4. Tìm đến cuối file `docs/buoi_14.md` (trước dòng `<!-- tabs:end -->`) để chèn thẻ `iframe` hiển thị Bài tập Trắc nghiệm cho người dùng.
5. Kiểm thử độ dài đáp án đúng của các câu MCQ thông qua file Python.
