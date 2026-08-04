# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 9

Tài liệu này là SOP (Quy trình thao tác chuẩn) để bám sát và xây dựng kịch bản (Script) quay video thực hành cho **Chương 9: Trình bày Kết quả Phân tích Dữ liệu (Presenting Data Analysis Results)**.

## LƯU Ý ĐẶC BIỆT (YÊU CẦU CỦA NGƯỜI DÙNG)
- **Giới tính Giảng viên:** Nhân vật Người 1 (Giảng viên) là Nam. Xuyên suốt toàn bộ kịch bản, Sinh viên (Người 2) phải xưng hô là **"thầy"** (tuyệt đối không dùng "cô" hoặc "thầy/cô").

## 1. Mục tiêu cốt lõi
- Xây dựng một kịch bản thoại tương tác (Người 1 - Giảng viên, Người 2 - Sinh viên) đảm bảo khớp tuyệt đối 1:1 với **106 slides** của Chương 9.
- Làm nổi bật kỹ năng "Trực quan hóa dữ liệu" (Data Visualization) và "Kể chuyện bằng dữ liệu" (Data Storytelling). Chuyển hóa số liệu thành các biểu đồ Dashboard trực quan để thuyết phục Ban Giám đốc.

## 2. Nguyên liệu Đầu vào (Inputs)
Cần tập hợp các tài nguyên sau tại thư mục `videoPractice\Chapter09`:
1. **File mã nguồn Slide (`Slide_Practice_Ch09.tex`):** Lấy từ thư mục `TaiLieu/slidePractice`. Dùng để xuất chính xác 106 tiêu đề slide làm khung kịch bản.
2. **File PDF Slide (`Slide_Practice_Ch09.pdf`):** Cần copy sang `videoPractice\Chapter09` để xem các định dạng biểu đồ (Bar chart, Pie chart, Line chart, Dashboard).
3. **Tài liệu Textbook gốc:** Dùng để nắm vững nguyên tắc thiết kế thị giác: Đơn giản hóa, chọn đúng loại biểu đồ, tránh sử dụng biểu đồ 3D gây nhiễu.

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter09.txt`
- **Vị trí lưu trữ:** `webAIAccounting\videoPractice\Chapter09\`
- **Định dạng bắt buộc cho từng Slide (tổng cộng 106 mục):**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên (Thầy) - Hướng dẫn cách chọn biểu đồ, mẹo kể chuyện...]
  Người 2: [Lời thoại Sinh viên - Gọi "thầy", thể hiện sự thích thú với các biểu đồ đẹp...]
  ```

## 4. Quy trình Thực hiện chi tiết cho Chương 9

### Bước 1: Khởi tạo
- Đảm bảo thư mục `webAIAccounting\videoPractice\Chapter09` đã được tạo.
- Copy file `Slide_Practice_Ch09.pdf` vào thư mục này.

### Bước 2: Bóc tách 106 Slides của Chương 9
Chương 9 (106 slides) là chương thiên về thẩm mỹ và trình bày, bao gồm:
- **Phần Khởi động:** Sức mạnh của trực quan hóa - "Một bức tranh đáng giá ngàn lời nói". 
- **Phần Cốt lõi (Chọn đúng biểu đồ):** Khi nào dùng Line chart (xu hướng), khi nào dùng Bar chart (so sánh), tại sao nên hạn chế Pie chart và tuyệt đối tránh 3D chart.
- **Phần Nâng cao (Data Storytelling):** Cách thiết kế một Dashboard hiệu quả, tập trung vào đối tượng khán giả (Audience-centric).
- **Phần Bài tập (BE, EX, PAC):** Chỉnh sửa các biểu đồ "xấu" thành biểu đồ "đẹp" và dễ hiểu.

### Bước 3: Nguyên tắc Viết Lời thoại đặc thù cho Chương 9
- **Giảng viên (Thầy):** Đóng vai trò là một "Chuyên gia Thuyết trình/Kể chuyện". Nhấn mạnh nguyên tắc: *"Đừng bắt sếp phải suy nghĩ khi nhìn biểu đồ"*. Nhắc nhở sinh viên tránh các lỗi trang trí màu mè thừa thãi (chartjunk).
- **Sinh viên:** Rất hào hứng vì phần này bắt mắt. Sinh viên xưng "thưa thầy". Sinh viên sẽ đặt câu hỏi về thẩm mỹ: *"Thưa thầy, làm sao để phối màu cho Dashboard nhìn chuyên nghiệp mà không bị chói mắt ạ?"*.
- **Kỹ thuật tự động hóa kịch bản:** Dùng Python script để bóc tách 106 tiêu đề slide từ file `Slide_Practice_Ch09.tex` thành kịch bản tự động.

### Bước 4: Kiểm thử (QA)
- **Kiểm tra xưng hô:** Đảm bảo 100% kịch bản dùng từ "thầy", loại bỏ hoàn toàn "cô" hay "thầy/cô".
- **Kiểm tra độ chính xác của Slide:** Cần có đủ 106 slides (1:1). Slide minh họa biểu đồ phải có câu thoại kêu gọi sinh viên nhìn lên màn hình.

## 5. Triển khai
Sử dụng kế hoạch này để viết file mã Python `extract_and_generate_ch09.py` nhằm mục đích bóc tách 106 tiêu đề từ `.tex` và tạo tự động `script_chapter09.txt`.
