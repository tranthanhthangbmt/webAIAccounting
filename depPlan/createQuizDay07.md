# Lập kế hoạch: Thêm Tab Bài tập Trắc nghiệm (Interactive Quiz) cho Buổi 7

Tiếp tục quy trình đồng bộ như các buổi học trước, tôi sẽ lập kế hoạch xây dựng bộ 30 câu hỏi trắc nghiệm tương tác cho Buổi 7. 

## Nguồn tài liệu tham khảo chính (Buổi 7)
- **Slide bài giảng:** `TaiLieu/slideAIAcc/Slide_AIAcc_Day07.pdf` (và các tài nguyên liên quan).
- **Tài liệu đọc 1:** `textbook/Buoi_07A_Chương 9 (Automating Internal Controls).pdf` (Sử dụng bản dịch trong `docs/buoi_07.md`).
- **Tài liệu đọc 2:** `textbook/Buoi_07B_Chương 12 (Intelligent Automation of Fraud Detection).pdf` (Sử dụng bản dịch trong `docs/buoi_07.md`).

## Yêu cầu cốt lõi (Theo chỉ thị khắt khe từ người dùng)
- **Kiểm soát độ dài đáp án MCQ (Quan trọng nhất):** Đảm bảo tuyệt đối rằng trong tất cả các câu hỏi trắc nghiệm nhiều lựa chọn (MCQ), **đáp án đúng có độ dài ngang bằng hoặc ngắn hơn các đáp án sai**. Điều này nhằm ngăn chặn tình trạng học viên phát hiện đáp án đúng thông qua độ dài của câu chữ.
- **Đa dạng hóa định dạng:** Duy trì cấu trúc 30 câu hỏi với 4 dạng tương tác:
  1. Trắc nghiệm truyền thống (MCQ)
  2. Kéo thả điền từ (Fill-in-the-blanks)
  3. Ghép nối (Matching)
  4. Sắp xếp thứ tự (Ordering)

## Proposed Changes

Tôi sẽ triển khai hệ thống Quiz tĩnh tương tự cho Buổi 7.

### Khởi tạo thư mục và file Quiz
#### [NEW] `quizzes/Day07/index.html`
- Nhân bản bộ khung giao diện chuẩn (HTML/CSS/JS) từ Buổi 1.
- Chỉnh sửa tiêu đề thành "Buổi 7".
- Xây dựng và thực thi script Python (`update_quiz_day07.py`) để sinh tự động mã JSON chứa 30 câu hỏi mới và đưa vào file HTML.

### Cập nhật File Markdown
#### [MODIFY] `docs/buoi_07.md`
- Tôi sẽ quét nội dung tệp `docs/buoi_07.md` để lấy nguồn tạo câu hỏi.
- Bổ sung tab **📝 Bài tập Trắc nghiệm** vào đoạn cuối của file (trước khi đóng tab `<!-- tabs:end -->`).
- Nhúng `iframe` để hiển thị trang HTML chứa câu hỏi trắc nghiệm.

## Verification Plan
1. Lưu giữ bản kế hoạch này vào tệp `depPlan/createQuizDay07.md`.
2. Truy vấn dữ liệu thực tế từ `docs/buoi_07.md` để soạn 30 câu hỏi sát với bài giảng.
3. Sinh câu hỏi bằng Python và kiểm tra độ dài các tùy chọn.
4. Mở giao diện `/#/docs/buoi_07`, trực tiếp kiểm tra hiển thị và chức năng của tab Bài tập Trắc nghiệm. Đảm bảo mọi thứ hoàn hảo trước khi báo cáo kết quả.
