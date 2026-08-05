# Lập kế hoạch: Thêm Tab Bài tập Trắc nghiệm (Interactive Quiz) cho Buổi 8

Theo đúng định hướng đã triển khai thành công từ Buổi 1 đến Buổi 7, tôi sẽ lập kế hoạch xây dựng bộ 30 câu hỏi trắc nghiệm tương tác cho Buổi 8. 

## Nguồn tài liệu tham khảo chính (Buổi 8)
Nội dung câu hỏi sẽ bám sát vào:
- **Slide bài giảng:** `TaiLieu/slideAIAcc/Slide_AIAcc_Day08.pdf` (và các nội dung liên quan trên trang).
- **Tài liệu đọc 1:** `textbook/Buoi_08A_Chương 6 (Credit Scoring, Algorithmic Trading)2. Phần AI Algorithmic Trading.pdf` (Sử dụng bản dịch tiếng Việt tương ứng trong `docs/buoi_08.md`).
- **Tài liệu đọc 2:** `textbook/Buoi_08B_Chuong_4_AI_Market_Manipulation_new.pdf` (Sử dụng bản dịch tiếng Việt tương ứng trong `docs/buoi_08.md`).

## Yêu cầu cốt lõi (Theo chỉ thị khắt khe từ người dùng)
- **Kiểm soát độ dài đáp án MCQ (Ưu tiên hàng đầu):** Đảm bảo tuyệt đối rằng trong tất cả các câu hỏi trắc nghiệm nhiều lựa chọn (MCQ), **đáp án đúng được thiết kế có độ dài ngang bằng hoặc ngắn hơn các đáp án sai**. Tuyệt đối không để xảy ra tình trạng "đáp án dài nhất là đáp án đúng".
- **Đa dạng hóa định dạng:** Tiếp tục duy trì hệ thống tương tác với 4 dạng câu hỏi:
  1. Trắc nghiệm truyền thống (MCQ)
  2. Kéo thả điền từ (Fill-in-the-blanks)
  3. Ghép nối thuật ngữ (Matching)
  4. Sắp xếp thứ tự quy trình (Ordering)

## Proposed Changes

Tôi sẽ triển khai hệ thống Quiz tĩnh cho Buổi 8 với các bước sau:

### Khởi tạo thư mục và file Quiz
#### [NEW] `quizzes/Day08/index.html`
- Nhân bản bộ khung giao diện chuẩn (HTML/CSS/JS) từ hệ thống trước.
- Đổi các tiêu đề thành "Buổi 8".
- Xây dựng và thực thi script Python (`update_quiz_day08.py`) để sinh tự động mã JSON chứa 30 câu hỏi mới và đưa vào file HTML.

### Cập nhật File Markdown
#### [MODIFY] `docs/buoi_08.md`
- Tôi sẽ đọc nội dung tệp `docs/buoi_08.md` để nắm bắt ngữ cảnh, từ đó soạn thảo hệ thống câu hỏi xoay quanh Giao dịch thuật toán (Algorithmic Trading) và Thao túng thị trường bằng AI (Market Manipulation).
- Bổ sung tab **📝 Bài tập Trắc nghiệm** vào đoạn cuối của file (ngay trước thẻ đóng tab `<!-- tabs:end -->`).
- Nhúng đoạn mã `iframe` trỏ đến trang HTML của Quiz.

## Verification Plan
1. Lưu giữ bản kế hoạch này vào tệp `depPlan/createQuizDay08.md`.
2. Trích xuất dữ liệu bài học thực tế từ `docs/buoi_08.md`.
3. Sinh và nhúng câu hỏi bằng Python, sau đó trực tiếp kiểm tra sự chênh lệch độ dài của các tùy chọn.
4. Mở giao diện `/#/docs/buoi_08`, chơi thử tab Bài tập Trắc nghiệm. Đảm bảo mọi thứ hoàn hảo trước khi báo cáo hoàn tất quy trình.
