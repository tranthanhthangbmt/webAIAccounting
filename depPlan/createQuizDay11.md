# Kế hoạch Tạo Bài tập Trắc nghiệm - Buổi 11

## 1. Mục tiêu
Thiết kế bộ 30 câu hỏi trắc nghiệm tương tác cho **Buổi 11: Thực hành AI Phân tích Dữ liệu Cơ bản (Cơ sở Dữ liệu Quan hệ, SQL & Excel)**, dựa trên nội dung "Chương 2: Foundational Data Analysis Skills".

## 2. Các chủ đề trọng tâm (Theo `docs/buoi_11.md`)
- Cơ sở dữ liệu quan hệ (Relational Databases) và các khái niệm: Bảng, Hàng, Cột, Thuộc tính.
- Khóa chính (Primary Key) và Khóa ngoại (Foreign Key).
- Truy vấn cơ sở dữ liệu với SQL: Các loại liên kết như Inner Join, Left Join, Right Join, Full Join.
- Thao tác dữ liệu bằng Microsoft Excel (Các hàm phân tích cơ bản, Pivot Table).
- Thống kê mô tả (Descriptive Statistics): Thước đo Vị trí (Mean, Median), Phân tán (Variance, Range), Hình dạng, Tương quan.
- Khái niệm về Data Visualization (Trực quan hóa dữ liệu).

## 3. Quy tắc cốt lõi về đáp án MCQ
- Các câu hỏi Multiple Choice: Nội dung (text) của lựa chọn được chỉ định là đúng (`correctAnswer`) **không được phép dài hơn** bất kỳ lựa chọn sai nào. Lý tưởng là ngắn hơn hoặc có độ dài tương đương, tránh việc lộ đáp án do người học nhìn ra lựa chọn dài nhất.

## 4. Các bước triển khai kỹ thuật
1. Khởi tạo thư mục `quizzes/Day11` bằng cách sao chép từ `quizzes/Day09` (hoặc cấu trúc có sẵn).
2. Tạo script Python `update_quiz_day11.py` định nghĩa mảng 30 câu hỏi chuẩn định dạng JSON, với 4 loại tương tác (Multiple choice, Matching, Fill-in-the-blanks, Ordering).
3. Chạy lệnh thực thi script trên để tiêm nội dung vào `index.html`. Thay đổi các chuỗi "Bài Tập Trắc Nghiệm Buổi X" thành "Bài Tập Trắc Nghiệm Buổi 11".
4. Tìm đến cuối file `docs/buoi_11.md` (ngay trước dòng `<!-- tabs:end -->`) để chèn thẻ `iframe` hiển thị Bài tập Trắc nghiệm cho người dùng.
5. Kiểm thử độ dài đáp án đúng của các câu MCQ thông qua file Python.
