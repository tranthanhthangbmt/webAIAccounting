# Kế hoạch Tạo Bài tập Trắc nghiệm - Buổi 9

## 1. Mục tiêu
Thiết kế bộ 30 câu hỏi trắc nghiệm tương tác cho **Buổi 9: AI trong Tài chính Cá nhân và Thị trường Tài sản Số (Crypto Assets & Robo-Advisors)**. 

## 2. Các chủ đề trọng tâm (Theo `docs/buoi_09.md`)
- Tiền điện tử (Cryptoassets) và biến động thị trường tài chính.
- Khái niệm về Số hóa (Digitalization) và Toàn cầu hóa tài chính.
- Sự đối lập giữa Tập trung hóa (Centralization) và Phân quyền (Decentralization).
- Ứng dụng Tài chính Phi tập trung (DeFi).
- Tiền kỹ thuật số của Ngân hàng Trung ương (CBDC).
- Cố vấn Robot (Robo-Advisors) trong ngành dịch vụ tài chính cá nhân.

## 3. Quy tắc cốt lõi về đáp án MCQ
- Các câu hỏi Multiple Choice: Nội dung (text) của lựa chọn được chỉ định là đúng (`correctAnswer`) **không được phép dài hơn** bất kỳ lựa chọn sai nào. Lý tưởng là ngắn hơn hoặc có độ dài tương đương.

## 4. Các bước triển khai kỹ thuật
1. Khởi tạo thư mục `quizzes/Day09` bằng cách sao chép từ `quizzes/Day08`.
2. Tạo script Python `update_quiz_day09.py` định nghĩa mảng 30 câu hỏi chuẩn định dạng JSON, với 4 loại tương tác (Multiple choice, Matching, Fill-in-the-blanks, Ordering).
3. Chạy lệnh thực thi script trên để tiêm nội dung vào `index.html`.
4. Tìm đến cuối file `docs/buoi_09.md` (trước dòng `<!-- tabs:end -->`) để chèn thẻ `iframe` hiển thị Bài tập Trắc nghiệm cho người dùng.
5. Kiểm thử độ dài đáp án đúng của các câu MCQ thông qua trang web cục bộ.
