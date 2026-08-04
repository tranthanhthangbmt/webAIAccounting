# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 5

Tài liệu này là SOP (Quy trình thao tác chuẩn) để xây dựng kịch bản (Script) quay video thực hành cho **Chương 5: Chuẩn bị Dữ liệu (Data Preparation)**.

## LƯU Ý ĐẶC BIỆT (YÊU CẦU CỦA NGƯỜI DÙNG)
- **Giới tính Giảng viên:** Nhân vật Người 1 (Giảng viên) là Nam. Xuyên suốt toàn bộ kịch bản, Sinh viên (Người 2) phải xưng hô là **"thầy"** (tuyệt đối không dùng "cô" hoặc "thầy/cô").

## 1. Mục tiêu cốt lõi
- Xây dựng một kịch bản thoại tương tác (Người 1 - Giảng viên, Người 2 - Sinh viên) đảm bảo khớp tuyệt đối 1:1 với **101 slides** của Chương 5.
- Làm nổi bật quy trình ETL (Extract, Transform, Load) và các kỹ năng làm sạch dữ liệu trong Excel/Database. Do đây là phần "đổ mồ hôi" nhất của phân tích dữ liệu (chiếm 80% thời gian), kịch bản cần mang tính chất thực hành sâu.

## 2. Nguyên liệu Đầu vào (Inputs)
Cần tập hợp các tài nguyên sau tại thư mục `videoPractice\Chapter05`:
1. **File mã nguồn Slide (`Slide_Practice_Ch05.tex`):** Lấy từ thư mục `TaiLieu/slidePractice`. Dùng để xuất chính xác 101 tiêu đề slide làm khung kịch bản.
2. **File PDF Slide (`Slide_Practice_Ch05.pdf`):** Cần copy sang `videoPractice\Chapter05` để đối chiếu trực quan.
3. **Tài liệu Textbook gốc:** Để tham chiếu các thuật ngữ như Missing values, Outliers, Data parsing, Data validation.

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter05.txt`
- **Vị trí lưu trữ:** `webAIAccounting\videoPractice\Chapter05\`
- **Định dạng bắt buộc cho từng Slide (tổng cộng 101 mục):**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên (Thầy) - Hướng dẫn làm sạch, chuẩn hóa dữ liệu...]
  Người 2: [Lời thoại Sinh viên - Gọi "thầy", đặt câu hỏi về các lỗi định dạng...]
  ```

## 4. Quy trình Thực hiện chi tiết cho Chương 5

### Bước 1: Khởi tạo
- Đảm bảo thư mục `webAIAccounting\videoPractice\Chapter05` đã được tạo.
- Copy file `Slide_Practice_Ch05.pdf` vào thư mục này.

### Bước 2: Bóc tách 101 Slides của Chương 5
Chương 5 có 101 slides, chia thành các phần chính:
- **Phần Khởi động:** Giới thiệu về quy trình ETL (Extract, Transform, Load) và tại sao phải mất đến 80% thời gian để làm sạch dữ liệu.
- **Phần Nhận diện Lỗi (Data Profiling):** Phân tích các loại lỗi phổ biến: dữ liệu bị thiếu (missing), dữ liệu ngoại lai (outliers), định dạng ngày tháng sai lệch, lỗi đánh máy.
- **Phần Xử lý (Data Cleaning & Formatting):** Hướng dẫn dùng các hàm Excel (TRIM, LEFT/RIGHT, VALUE, IFERROR) hoặc công cụ Power Query để xử lý.
- **Phần Bài tập (BE, EX, PAC):** Chuyển các tình huống kiểm tra thành hội thoại.

### Bước 3: Nguyên tắc Viết Lời thoại đặc thù cho Chương 5
- **Giảng viên (Thầy):** Hóa thân thành người có kinh nghiệm thực chiến xử lý dữ liệu. Nhấn mạnh sự kiên nhẫn. Các ví dụ đưa ra phải bám sát nỗi đau của dân kế toán (ví dụ: ngày tháng định dạng MM/DD vs DD/MM, lỗi Font chữ).
- **Sinh viên:** Luôn xưng hô "thưa thầy". Sinh viên thường tỏ ra bực bội hoặc ngạc nhiên khi thấy dữ liệu thực tế lại lộn xộn đến vậy. Ví dụ: "Thưa thầy, nếu có một ô bị trống (NULL) thì mình xóa nguyên cái dòng đó luôn hay điền số 0 vào ạ?".
- **Kỹ thuật tự động hóa kịch bản:** Tương tự Chương 3 và 4, sẽ dùng mã Python để parse tự động 1:1 từ mã nguồn `Slide_Practice_Ch05.tex` ra 101 mục kịch bản.

### Bước 4: Kiểm thử (QA)
- **Kiểm tra xưng hô:** Đảm bảo từ khóa "thầy" được dùng đồng nhất. Không có "cô" hay "thầy/cô".
- **Kiểm tra độ chính xác của Slide:** Cần có đủ 101 slides. Không gộp, không thiếu.

## 5. Triển khai
Tiến hành sử dụng script tự động để bóc tách 101 tiêu đề slide từ file LaTeX và sinh kịch bản `script_chapter05.txt`.
