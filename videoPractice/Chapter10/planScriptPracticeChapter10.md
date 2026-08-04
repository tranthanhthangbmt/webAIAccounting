# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 10

Tài liệu này là SOP (Quy trình thao tác chuẩn) để bám sát và xây dựng kịch bản (Script) quay video thực hành cho **Chương 10: Các Xu hướng Dữ liệu và Phân tích Mới nhất trong Kế toán (Latest Trends in Accounting Data and Analytics)**.

## LƯU Ý ĐẶC BIỆT (YÊU CẦU CỦA NGƯỜI DÙNG)
- **Giới tính Giảng viên:** Nhân vật Người 1 (Giảng viên) là Nam. Xuyên suốt toàn bộ kịch bản, Sinh viên (Người 2) phải xưng hô là **"thầy"** (tuyệt đối không dùng "cô" hoặc "thầy/cô").

## 1. Mục tiêu cốt lõi
- Xây dựng một kịch bản thoại tương tác (Người 1 - Giảng viên, Người 2 - Sinh viên) đảm bảo khớp tuyệt đối 1:1 với **69 slides** của Chương 10.
- Đây là chương tổng kết mang tính thời sự, làm nổi bật tương lai của nghề kế toán dưới sự tác động của AI, RPA (Tự động hóa quy trình bằng Robot), Blockchain và Kiểm toán liên tục (Continuous Auditing).

## 2. Nguyên liệu Đầu vào (Inputs)
Cần tập hợp các tài nguyên sau tại thư mục `videoPractice\Chapter10`:
1. **File mã nguồn Slide (`Slide_Practice_Ch10.tex`):** Lấy từ thư mục `TaiLieu/slidePractice`. Dùng để xuất chính xác 69 tiêu đề slide làm khung kịch bản.
2. **File PDF Slide (`Slide_Practice_Ch10.pdf`):** Cần copy sang `videoPractice\Chapter10` để tham chiếu.
3. **Tài liệu Textbook gốc:** Dùng để nắm vững thuật ngữ về xu hướng (RPA, Smart Contracts, XBRL...).

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter10.txt`
- **Vị trí lưu trữ:** `webAIAccounting\videoPractice\Chapter10\`
- **Định dạng bắt buộc cho từng Slide (tổng cộng 69 mục):**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên (Thầy) - Truyền cảm hứng, định hướng nghề nghiệp tương lai...]
  Người 2: [Lời thoại Sinh viên - Gọi "thầy", thể hiện sự bất ngờ trước công nghệ và đặt câu hỏi về lộ trình...]
  ```

## 4. Quy trình Thực hiện chi tiết cho Chương 10

### Bước 1: Khởi tạo
- Đảm bảo thư mục `webAIAccounting\videoPractice\Chapter10` đã được tạo.
- Copy file `Slide_Practice_Ch10.pdf` vào thư mục này.

### Bước 2: Bóc tách 69 Slides của Chương 10
Chương 10 (69 slides) được xem là "phần chóp" của toàn bộ khóa học:
- **Phần Khởi động:** Nhìn lại hành trình từ Chương 1 đến 9. Mở ra cánh cửa về tương lai số.
- **Phần Cốt lõi (Công nghệ):** Phân tích sâu về AI, Học máy (Machine Learning), RPA thay thế các tác vụ lặp đi lặp lại.
- **Phần Nâng cao (Tác động tới nghề nghiệp):** Vai trò của Kế toán viên trong kỷ nguyên Blockchain và Smart Contracts (Hợp đồng thông minh).
- **Phần Bài tập (BE, EX, PAC):** Thực hành xử lý các tình huống đánh giá tác động công nghệ đối với doanh nghiệp.

### Bước 3: Nguyên tắc Viết Lời thoại đặc thù cho Chương 10
- **Giảng viên (Thầy):** Đóng vai trò là một "Người truyền cảm hứng" (Visionary/Mentor). Giảng viên đưa ra thông điệp: *"AI không cướp việc của kế toán viên, nhưng người kế toán biết dùng AI sẽ cướp việc của người không biết dùng"*.
- **Sinh viên:** Vừa lo lắng vừa háo hức. Sinh viên xưng "thưa thầy". Sinh viên sẽ đặt các câu hỏi lo ngại về tương lai nghề nghiệp: *"Thưa thầy, liệu Robot có thay thế hoàn toàn kế toán viên tụi em không ạ?"*.
- **Kỹ thuật tự động hóa kịch bản:** Dùng Python script để bóc tách 69 tiêu đề slide từ file `Slide_Practice_Ch10.tex` thành kịch bản tự động.

### Bước 4: Kiểm thử (QA)
- **Kiểm tra xưng hô:** Đảm bảo 100% kịch bản dùng từ "thầy", tuyệt đối không dùng "cô" hay "thầy/cô".
- **Kiểm tra độ chính xác của Slide:** Cần có đủ 69 slides (1:1).

## 5. Triển khai
Sử dụng kế hoạch này để viết file mã Python `extract_and_generate_ch10.py` nhằm mục đích bóc tách 69 tiêu đề từ `.tex` và tạo tự động `script_chapter10.txt`.
