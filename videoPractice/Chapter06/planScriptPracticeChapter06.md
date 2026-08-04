# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 6

Tài liệu này là SOP (Quy trình thao tác chuẩn) để bám sát và xây dựng kịch bản (Script) quay video thực hành cho **Chương 6: Mô hình hóa Thông tin (Information Modeling)**.

## LƯU Ý ĐẶC BIỆT (YÊU CẦU CỦA NGƯỜI DÙNG)
- **Giới tính Giảng viên:** Nhân vật Người 1 (Giảng viên) là Nam. Xuyên suốt toàn bộ kịch bản, Sinh viên (Người 2) phải xưng hô là **"thầy"** (tuyệt đối không dùng "cô" hoặc "thầy/cô").

## 1. Mục tiêu cốt lõi
- Xây dựng một kịch bản thoại tương tác (Người 1 - Giảng viên, Người 2 - Sinh viên) đảm bảo khớp tuyệt đối 1:1 với **107 slides** của Chương 6.
- Làm nổi bật tư duy thiết kế hệ thống cơ sở dữ liệu: Cách thiết kế một Mô hình hóa Thông tin (Information Modeling), Sơ đồ Thực thể - Mối quan hệ (ERD), và quy tắc chuẩn hóa dữ liệu.

## 2. Nguyên liệu Đầu vào (Inputs)
Cần tập hợp các tài nguyên sau tại thư mục `videoPractice\Chapter06`:
1. **File mã nguồn Slide (`Slide_Practice_Ch06.tex`):** Lấy từ thư mục `TaiLieu/slidePractice`. Dùng để xuất chính xác 107 tiêu đề slide làm khung kịch bản.
2. **File PDF Slide (`Slide_Practice_Ch06.pdf`):** Cần copy sang `videoPractice\Chapter06` để đối chiếu hình ảnh biểu đồ ERD khi viết kịch bản.
3. **Tài liệu Textbook gốc:** Dùng để hiểu sâu hơn về các thuật ngữ như Entities, Attributes, Relationships, Cardinalities (1:1, 1:N, M:N).

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter06.txt`
- **Vị trí lưu trữ:** `webAIAccounting\videoPractice\Chapter06\`
- **Định dạng bắt buộc cho từng Slide (tổng cộng 107 mục):**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên (Thầy) - Giải thích khái niệm thực thể, bản số (cardinality)...]
  Người 2: [Lời thoại Sinh viên - Gọi "thầy", đặt câu hỏi về cách vẽ sơ đồ...]
  ```

## 4. Quy trình Thực hiện chi tiết cho Chương 6

### Bước 1: Khởi tạo
- Đảm bảo thư mục `webAIAccounting\videoPractice\Chapter06` đã được tạo.
- Copy file `Slide_Practice_Ch06.pdf` vào thư mục này.

### Bước 2: Bóc tách 107 Slides của Chương 6
Chương 6 dài 107 slides, đặc thù có rất nhiều sơ đồ (Diagrams). Kịch bản sẽ chia theo các luồng kiến thức:
- **Phần Khởi động:** Giới thiệu Mô hình hóa thông tin là gì? Tại sao kế toán cần biết thiết kế Database?
- **Phần Cốt lõi (ERD):** Giải phẫu các thành phần của Sơ đồ thực thể - mối quan hệ: Thực thể (Entities), Thuộc tính (Attributes), và Khóa (Keys).
- **Phần Nâng cao (Cardinalities):** Rèn luyện cách đọc và vẽ bản số: Một-Nhiều (1:M), Nhiều-Nhiều (M:N).
- **Phần Bài tập (BE, EX, PAC):** Rất nhiều bài tập vẽ sơ đồ và chuyển đổi từ sơ đồ sang cấu trúc bảng SQL.

### Bước 3: Nguyên tắc Viết Lời thoại đặc thù cho Chương 6
- **Giảng viên (Thầy):** Hóa thân thành một "Kiến trúc sư hệ thống" (System Architect). Giảng viên cần chỉ dẫn sinh viên cách nhìn vạn vật trong doanh nghiệp dưới dạng Thực thể (Khách hàng, Hóa đơn, Sản phẩm).
- **Sinh viên:** Phải thể hiện được sự khó khăn khi mới học vẽ sơ đồ ERD. Ví dụ: *"Thưa thầy, làm sao phân biệt được khi nào dùng mối quan hệ Một-Nhiều (1:M) và khi nào dùng Nhiều-Nhiều (M:N) ạ?"*. Sinh viên luôn luôn xưng hô là "thầy".
- **Kỹ thuật tự động hóa kịch bản:** Tiếp tục sử dụng Python script để parse 107 tiêu đề slide từ file `Slide_Practice_Ch06.tex`. Tích hợp xử lý tự động sinh thoại dựa trên keyword như "ERD", "Cardinality", "ILLUSTRATION".

### Bước 4: Kiểm thử (QA)
- **Kiểm tra xưng hô:** Đảm bảo 100% kịch bản dùng từ "thầy".
- **Kiểm tra độ chính xác của Slide:** Cần có đủ 107 slides (1:1). Các slide hình vẽ phải có câu thoại nhắc sinh viên nhìn vào màn hình.

## 5. Triển khai
Sử dụng kế hoạch này để viết file mã Python `extract_and_generate_ch06.py` nhằm mục đích bóc tách 107 tiêu đề từ `.tex` và tạo tự động `script_chapter06.txt`.
