# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 7

Tài liệu này là SOP (Quy trình thao tác chuẩn) để bám sát và xây dựng kịch bản (Script) quay video thực hành cho **Chương 7: Khám phá Dữ liệu (Data Exploration)**.

## LƯU Ý ĐẶC BIỆT (YÊU CẦU CỦA NGƯỜI DÙNG)
- **Giới tính Giảng viên:** Nhân vật Người 1 (Giảng viên) là Nam. Xuyên suốt toàn bộ kịch bản, Sinh viên (Người 2) phải xưng hô là **"thầy"** (tuyệt đối không dùng "cô" hoặc "thầy/cô").

## 1. Mục tiêu cốt lõi
- Xây dựng một kịch bản thoại tương tác (Người 1 - Giảng viên, Người 2 - Sinh viên) đảm bảo khớp tuyệt đối 1:1 với **103 slides** của Chương 7.
- Làm nổi bật bước "Khám phá" (Exploration) trong phân tích dữ liệu, hướng dẫn sinh viên cách "đánh hơi" thấy những điểm bất thường (outliers), xu hướng (trends) thông qua các công cụ trực quan hóa sơ bộ trước khi chạy các mô hình phức tạp.

## 2. Nguyên liệu Đầu vào (Inputs)
Cần tập hợp các tài nguyên sau tại thư mục `videoPractice\Chapter07`:
1. **File mã nguồn Slide (`Slide_Practice_Ch07.tex`):** Lấy từ thư mục `TaiLieu/slidePractice`. Dùng để xuất chính xác 103 tiêu đề slide làm khung kịch bản.
2. **File PDF Slide (`Slide_Practice_Ch07.pdf`):** Cần copy sang `videoPractice\Chapter07` để đối chiếu hình ảnh.
3. **Tài liệu Textbook gốc:** Dùng để nắm vững các kỹ thuật Khám phá dữ liệu: Thống kê mô tả cơ bản, Histogram, Boxplot, Scatter Plot.

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter07.txt`
- **Vị trí lưu trữ:** `webAIAccounting\videoPractice\Chapter07\`
- **Định dạng bắt buộc cho từng Slide (tổng cộng 103 mục):**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên (Thầy) - Hướng dẫn cách phân tích phân phối dữ liệu, phát hiện ngoại lai...]
  Người 2: [Lời thoại Sinh viên - Gọi "thầy", đặt câu hỏi về ý nghĩa của các biểu đồ khám phá...]
  ```

## 4. Quy trình Thực hiện chi tiết cho Chương 7

### Bước 1: Khởi tạo
- Đảm bảo thư mục `webAIAccounting\videoPractice\Chapter07` đã được tạo.
- Copy file `Slide_Practice_Ch07.pdf` vào thư mục này.

### Bước 2: Bóc tách 103 Slides của Chương 7
Chương 7 (103 slides) tập trung vào giai đoạn khám phá, có thể chia thành các luồng:
- **Phần Khởi động:** Giới thiệu Data Exploration là gì? Khác gì với Data Cleaning (Chương 5) và Data Modeling (Chương 6)?
- **Phần Cốt lõi (Trực quan hóa Khám phá):** Các công cụ cốt lõi để "nhìn" dữ liệu: Histogram (Phân phối), Boxplot (Điểm dị biệt), Scatter Plot (Tương quan).
- **Phần Nâng cao (Phân tích Thống kê nhanh):** Đọc các chỉ số trung bình (Mean), trung vị (Median), độ lệch chuẩn (Standard Deviation) để hiểu bản chất tập dữ liệu.
- **Phần Bài tập (BE, EX, PAC):** Thực hành nhìn biểu đồ và đưa ra nhận định ban đầu.

### Bước 3: Nguyên tắc Viết Lời thoại đặc thù cho Chương 7
- **Giảng viên (Thầy):** Đóng vai trò là một "Thám tử dữ liệu". Lời thoại nên mang tính chất khơi gợi: *"Nhìn vào biểu đồ này, các em có thấy điểm gì bất thường không?", "Tại sao Trung bình lại lớn hơn Trung vị rất nhiều?"*.
- **Sinh viên:** Phải thể hiện sự ngạc nhiên khi phát hiện ra những sự thật ẩn giấu đằng sau những con số nhàm chán. Luôn xưng hô "thưa thầy". Ví dụ: *"Thưa thầy, điểm chấm tròn nằm tít trên cao của Boxplot kia có phải là giao dịch gian lận không ạ?"*.
- **Kỹ thuật tự động hóa kịch bản:** Tiếp tục sử dụng Python script để parse 103 tiêu đề slide từ file `Slide_Practice_Ch07.tex`. 

### Bước 4: Kiểm thử (QA)
- **Kiểm tra xưng hô:** Đảm bảo 100% kịch bản dùng từ "thầy", tuyệt đối không có "cô" hay "thầy/cô".
- **Kiểm tra độ chính xác của Slide:** Cần có đủ 103 slides (1:1). 

## 5. Triển khai
Sử dụng kế hoạch này để viết file mã Python `extract_and_generate_ch07.py` nhằm mục đích bóc tách 103 tiêu đề từ `.tex` và tạo tự động `script_chapter07.txt`.
