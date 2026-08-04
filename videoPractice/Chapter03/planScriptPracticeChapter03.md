# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 3

Tài liệu này là SOP (Quy trình thao tác chuẩn) để bám sát và xây dựng kịch bản (Script) quay video thực hành cho **Chương 3: Động lực và Mục tiêu Phân tích Dữ liệu (Motivations and Objectives for Data Analysis)**. Do số lượng slide của chương này rất lớn (123 slides), kế hoạch cần được thực hiện cực kỳ kỷ luật.

## 1. Mục tiêu cốt lõi
- Xây dựng một kịch bản thoại tương tác (Người 1 - Giảng viên, Người 2 - Sinh viên) trải dài suốt 123 slides mà không gây nhàm chán.
- Đảm bảo ánh xạ 1:1 tuyệt đối giữa số lượng slide và số mục kịch bản.
- Chú trọng giải thích rõ các "Động lực kinh doanh" đằng sau mỗi bài toán dữ liệu.

## 2. Nguyên liệu Đầu vào (Inputs)
Cần tập hợp 3 tài nguyên sau tại thư mục `videoPractice\Chapter03`:
1. **File mã nguồn Slide (`Slide_Practice_Ch03.tex`):** Lấy từ thư mục `TaiLieu/slidePractice`. Là cơ sở duy nhất để bóc tách chính xác 123 tiêu đề slide.
2. **File PDF Slide (`Slide_Practice_Ch03.pdf`):** Cần copy sang `videoPractice\Chapter03` để nhìn hình ảnh khi viết thoại.
3. **Tài liệu Textbook gốc (`Ch_03_Motivations and Objectives for Data Analysis.pdf`):** Cung cấp các case study thực tế hoặc framework về Động lực - Mục tiêu trong kinh doanh.

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter03.txt`
- **Vị trí lưu trữ:** `webAIAccounting\videoPractice\Chapter03\`
- **Định dạng bắt buộc cho từng Slide (tổng cộng 123 mục):**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên - Đặt vấn đề, giải thích động lực kinh doanh, hướng dẫn...]
  Người 2: [Lời thoại Sinh viên - Phản hồi, đặt câu hỏi làm rõ, tóm tắt ý...]
  ```

## 4. Quy trình Thực hiện chi tiết cho Chương 3

### Bước 1: Khởi tạo và Gom dữ liệu
- Đảm bảo thư mục `webAIAccounting\videoPractice\Chapter03` đã được tạo.
- Copy file `Slide_Practice_Ch03.pdf` vào thư mục này để đối chiếu.

### Bước 2: Bóc tách 123 Slides của Chương 3
Vì Chương 3 rất dài (123 slides), cần chia nhỏ kịch bản thành các chặng (milestones) để kiểm soát, ví dụ:
- **Chặng 1 (Slide 1-30):** Khởi động, giới thiệu các loại động lực (Motivations) từ bên trong và bên ngoài doanh nghiệp.
- **Chặng 2 (Slide 31-60):** Đi sâu vào các Mục tiêu (Objectives) và thiết lập câu hỏi phân tích (như framework SMART hay tương tự).
- **Chặng 3 (Slide 61-90):** Mối liên hệ giữa việc xác định đúng Động lực và chọn đúng phương pháp phân tích (Mô tả, Chẩn đoán...).
- **Chặng 4 (Slide 91-123):** Dành riêng cho phần Thực hành (Practice & Exercises, PAC).

### Bước 3: Nguyên tắc Viết Lời thoại đặc thù cho Chương 3
- **Tính kinh doanh (Business-oriented):** Chương này nặng về tư duy đặt câu hỏi kinh doanh. Lời thoại của Người 1 phải luôn xoay quanh "Tại sao sếp lại muốn báo cáo này?", "Công ty đang gặp khó khăn gì?". 
- **Nhịp độ (Pacing):** Vì số lượng slide lớn (123 trang), cần tránh các câu thoại lan man ở những slide chuyển tiếp (như trang tiêu đề, trang mục tiêu...). Lời thoại ở các slide này nên ngắn gọn, dứt khoát. Dành thời lượng để phân tích sâu vào các slide mang tính Case Study.
- **Người 2 (Sinh viên):** Nên đóng vai trò là một người hay tò mò về ứng dụng thực tế. Ví dụ: "Vậy nếu ban giám đốc không rõ họ muốn gì thì mình phải bắt đầu từ đâu hả thầy?".

### Bước 4: Kiểm thử (QA) Khắt khe
- **Kiểm tra số lượng:** Phải đếm chính xác có đủ 123 cụm "Slide X:" từ 1 đến 123. Tuyệt đối không được gộp slide hay bỏ sót.
- **Sự kiên nhẫn:** Đọc lại các đoạn chuyển giao giữa các chặng để xem có mượt mà hay không, đảm bảo duy trì được sự hứng thú của người học.

## 5. Triển khai
Sử dụng kế hoạch SOP này để tiến hành ra lệnh tạo file `script_chapter03.txt`. Do file script sẽ rất dài, AI có thể cần phải chia làm nhiều lần xuất dữ liệu hoặc phải đảm bảo sinh văn bản một cách liên tục không bị ngắt quãng.
