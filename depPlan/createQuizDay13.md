# Kế hoạch Tạo Bài tập Trắc nghiệm - Buổi 13

## 1. Mục tiêu
Thiết kế bộ 30 câu hỏi trắc nghiệm tương tác cho **Buổi 13: Kỹ thuật Viết Prompt & Chiến lược Phân tích Dữ liệu Tài chính (SPARKS Framework)**. 

## 2. Các chủ đề trọng tâm (Theo `docs/buoi_13.md`)
- **Phần I: Tăng cường Phân tích Tài chính với AI:**
  - Chuyển đổi từ phân tích tĩnh (lịch sử) sang phân tích động (dự báo tương lai).
  - Các ứng dụng AI trong dự báo dòng tiền, phân tích rủi ro tín dụng.
  - Phân tích tình cảm (Sentiment Analysis).
- **Phần II: Kỹ thuật Prompt trong Kế toán:**
  - Chỉ định vai trò (Role-based Prompting).
  - Cung cấp bối cảnh và dữ liệu rõ ràng.
  - Phân chia tác vụ theo bước (Step-by-step / Chain-of-Thought).
  - Những sai lầm cần tránh (Prompt chung chung, vi phạm bảo mật).
- **Phần III: Khung tư duy SPARKS:**
  - Ý nghĩa các chữ cái trong SPARKS: State (Xác định câu hỏi), Partition (Phân chia), Analyze (Phân tích), Refine (Tinh chỉnh), Communicate (Truyền đạt), Stop (Suy ngẫm).
  - 4 mức độ phân tích dữ liệu: Mô tả (Descriptive), Chẩn đoán (Diagnostic), Dự đoán (Predictive), Đề xuất (Prescriptive).
  - Từ điển dữ liệu AP (Accounts Payable) và thực hành phân tích.

## 3. Quy tắc cốt lõi về đáp án MCQ
- Các câu hỏi Multiple Choice: Nội dung (text) của lựa chọn được chỉ định là đúng (`correctAnswer`) **không được phép dài hơn** bất kỳ lựa chọn sai nào. Lý tưởng là ngắn hơn hoặc có độ dài tương đương, tránh việc lộ đáp án do người học nhìn ra lựa chọn dài nhất.

## 4. Các bước triển khai kỹ thuật
1. Khởi tạo thư mục `quizzes/Day13` bằng cách sao chép từ `quizzes/Day12`.
2. Tạo script Python `update_quiz_day13.py` định nghĩa mảng 30 câu hỏi chuẩn định dạng JSON, với 4 loại tương tác (Multiple choice, Matching, Fill-in-the-blanks, Ordering).
3. Chạy lệnh thực thi script trên để tiêm nội dung vào `index.html`.
4. Tìm đến cuối file `docs/buoi_13.md` (trước dòng `<!-- tabs:end -->`) để chèn thẻ `iframe` hiển thị Bài tập Trắc nghiệm cho người dùng.
5. Kiểm thử độ dài đáp án đúng của các câu MCQ thông qua file Python.
