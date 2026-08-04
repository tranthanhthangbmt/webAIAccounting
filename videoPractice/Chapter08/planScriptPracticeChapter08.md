# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 8

Tài liệu này là SOP (Quy trình thao tác chuẩn) để bám sát và xây dựng kịch bản (Script) quay video thực hành cho **Chương 8: Diễn giải Kết quả Phân tích Dữ liệu (Interpreting Data Analysis Results)**.

## LƯU Ý ĐẶC BIỆT (YÊU CẦU CỦA NGƯỜI DÙNG)
- **Giới tính Giảng viên:** Nhân vật Người 1 (Giảng viên) là Nam. Xuyên suốt toàn bộ kịch bản, Sinh viên (Người 2) phải xưng hô là **"thầy"** (tuyệt đối không dùng "cô" hoặc "thầy/cô").

## 1. Mục tiêu cốt lõi
- Xây dựng một kịch bản thoại tương tác (Người 1 - Giảng viên, Người 2 - Sinh viên) đảm bảo khớp tuyệt đối 1:1 với **93 slides** của Chương 8.
- Làm nổi bật bước "Diễn giải" (Interpretation) - phần cốt lõi tạo ra giá trị cho doanh nghiệp. Chuyển hóa những con số thống kê vô hồn, những biểu đồ phức tạp thành các kết luận kinh doanh thực tiễn (Insights).

## 2. Nguyên liệu Đầu vào (Inputs)
Cần tập hợp các tài nguyên sau tại thư mục `videoPractice\Chapter08`:
1. **File mã nguồn Slide (`Slide_Practice_Ch08.tex`):** Lấy từ thư mục `TaiLieu/slidePractice`. Dùng để xuất chính xác 93 tiêu đề slide làm khung kịch bản.
2. **File PDF Slide (`Slide_Practice_Ch08.pdf`):** Cần copy sang `videoPractice\Chapter08` để nhìn hình ảnh và kết quả số liệu.
3. **Tài liệu Textbook gốc:** Dùng để hiểu sâu hơn về các khái niệm Correlation (Tương quan), Causation (Nhân quả), R-squared (Hệ số xác định), và P-value.

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter08.txt`
- **Vị trí lưu trữ:** `webAIAccounting\videoPractice\Chapter08\`
- **Định dạng bắt buộc cho từng Slide (tổng cộng 93 mục):**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên (Thầy) - Giải thích ý nghĩa con số, phân biệt tương quan và nhân quả...]
  Người 2: [Lời thoại Sinh viên - Gọi "thầy", thể hiện sự vỡ lẽ khi hiểu ý nghĩa thực sự của dữ liệu...]
  ```

## 4. Quy trình Thực hiện chi tiết cho Chương 8

### Bước 1: Khởi tạo
- Đảm bảo thư mục `webAIAccounting\videoPractice\Chapter08` đã được tạo.
- Copy file `Slide_Practice_Ch08.pdf` vào thư mục này.

### Bước 2: Bóc tách 93 Slides của Chương 8
Chương 8 (93 slides) có thể chia thành các nội dung chính:
- **Phần Khởi động:** Sự khác biệt giữa Phân tích (Analysis) và Diễn giải (Interpretation). Máy móc phân tích, con người diễn giải.
- **Phần Cốt lõi (Tương quan vs Nhân quả):** Nhấn mạnh bẫy lớn nhất của phân tích dữ liệu: "Tương quan không có nghĩa là Nhân quả" (Correlation is not Causation).
- **Phần Đánh giá Mô hình:** Hướng dẫn cách đọc các chỉ số thống kê quan trọng như R-squared, P-value, Error Rate để đánh giá xem mô hình có đáng tin cậy hay không.
- **Phần Bài tập (BE, EX, PAC):** Thực hành đọc hiểu các báo cáo kết quả từ phần mềm và rút ra kết luận.

### Bước 3: Nguyên tắc Viết Lời thoại đặc thù cho Chương 8
- **Giảng viên (Thầy):** Hóa thân thành một "Chuyên gia Cố vấn" (Consultant). Giảng viên không chỉ dạy cách tính toán, mà dạy cách "nói chuyện với sếp". Ví dụ: *"Nếu em báo cáo P-value với sếp, sếp sẽ đuổi em ra ngoài. Em phải nói là: Có 95% khả năng chiến dịch marketing này đã thực sự làm tăng doanh thu!"*.
- **Sinh viên:** Thể hiện sự giác ngộ. Sinh viên luôn xưng "thưa thầy". Sinh viên sẽ đặt các câu hỏi ngây ngô dễ mắc bẫy, ví dụ: *"Thầy ơi, biến A và biến B cùng tăng thì chứng tỏ A gây ra B phải không ạ?"*.
- **Kỹ thuật tự động hóa kịch bản:** Tiếp tục sử dụng Python script để parse 93 tiêu đề slide từ file `Slide_Practice_Ch08.tex`.

### Bước 4: Kiểm thử (QA)
- **Kiểm tra xưng hô:** Đảm bảo 100% kịch bản dùng từ "thầy", không dùng "cô" hay "thầy/cô".
- **Kiểm tra độ chính xác của Slide:** Cần có đủ 93 slides (1:1).

## 5. Triển khai
Sử dụng kế hoạch này để viết file mã Python `extract_and_generate_ch08.py` nhằm mục đích bóc tách 93 tiêu đề từ `.tex` và tạo tự động `script_chapter08.txt`.
