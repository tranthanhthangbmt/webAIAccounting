# Kế hoạch Tạo Bài tập Trắc nghiệm - Buổi 12

## 1. Mục tiêu
Thiết kế bộ 30 câu hỏi trắc nghiệm tương tác cho **Buổi 12: Thực hành AI Nhận thức và AI Tạo sinh trong Kế toán - Tài chính (Generative AI & Web-Enhanced ChatGPT)**. 

## 2. Các chủ đề trọng tâm (Theo `docs/buoi_12.md`)
- **Chương 1: Generative AI in Accounting:**
  - Định nghĩa và vai trò của GAI (Generative Artificial Intelligence).
  - Tự động hóa các tác vụ lặp đi lặp lại và giảm thiểu sai sót.
  - Phân tích dự báo (Predictive Analytics) trong kế toán.
  - Tầm quan trọng của Data Literacy và tư duy phê phán.
  - Các nghiên cứu điển hình (Case studies: doanh nghiệp nhỏ, công ty tư vấn, tập đoàn đa quốc gia).
- **Chương 12: Web-Enhanced ChatGPT & Custom GPTs:**
  - Cửa hàng GPT (GPT Store) và Khả năng tùy chỉnh GPT.
  - Tích hợp API và Actions vào các phần mềm kế toán.
  - Rủi ro về bảo mật dữ liệu, hiện tượng "ảo giác" (hallucination).
  - Ứng dụng thực tế: Chăm sóc khách hàng tài chính, đào tạo (tutoring).

## 3. Quy tắc cốt lõi về đáp án MCQ
- Các câu hỏi Multiple Choice: Nội dung (text) của lựa chọn được chỉ định là đúng (`correctAnswer`) **không được phép dài hơn** bất kỳ lựa chọn sai nào. Lý tưởng là ngắn hơn hoặc có độ dài tương đương, tránh việc lộ đáp án do người học nhìn ra lựa chọn dài nhất.

## 4. Các bước triển khai kỹ thuật
1. Khởi tạo thư mục `quizzes/Day12` bằng cách sao chép từ `quizzes/Day11`.
2. Tạo script Python `update_quiz_day12.py` định nghĩa mảng 30 câu hỏi chuẩn định dạng JSON, với 4 loại tương tác (Multiple choice, Matching, Fill-in-the-blanks, Ordering).
3. Chạy lệnh thực thi script trên để tiêm nội dung vào `index.html`.
4. Tìm đến cuối file `docs/buoi_12.md` (trước dòng `<!-- tabs:end -->`) để chèn thẻ `iframe` hiển thị Bài tập Trắc nghiệm cho người dùng.
5. Kiểm thử độ dài đáp án đúng của các câu MCQ thông qua file Python.
