# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 4

Tài liệu này là SOP (Quy trình thao tác chuẩn) để xây dựng kịch bản (Script) quay video thực hành cho **Chương 4: Lập Kế hoạch Dữ liệu và Chiến lược Phân tích (Data Planning and Analysis Strategy)**. 

## LƯU Ý ĐẶC BIỆT (YÊU CẦU CỦA NGƯỜI DÙNG)
- **Giới tính Giảng viên:** Nhân vật Người 1 (Giảng viên) là Nam. Xuyên suốt toàn bộ kịch bản, Sinh viên (Người 2) phải xưng hô là **"thầy"** (tuyệt đối không dùng "cô" hoặc "thầy/cô").

## 1. Mục tiêu cốt lõi
- Xây dựng một kịch bản thoại tương tác (Người 1 - Giảng viên, Người 2 - Sinh viên) đảm bảo khớp tuyệt đối 1:1 với **81 slides** của Chương 4.
- Tập trung làm nổi bật tư duy chiến lược trong việc chọn lọc dữ liệu: Không phải dữ liệu nào cũng dùng được, phải biết lập kế hoạch và thu thập đúng loại dữ liệu.

## 2. Nguyên liệu Đầu vào (Inputs)
Cần tập hợp 3 tài nguyên sau tại thư mục `videoPractice\Chapter04`:
1. **File mã nguồn Slide (`Slide_Practice_Ch04.tex`):** Lấy từ thư mục `TaiLieu/slidePractice`. Dùng để xuất chính xác 81 tiêu đề slide làm khung kịch bản.
2. **File PDF Slide (`Slide_Practice_Ch04.pdf`):** Cần copy sang `videoPractice\Chapter04` để tham chiếu hình ảnh.
3. **Tài liệu Textbook gốc (`Ch_04...pdf`):** Để bổ sung các kiến thức chuyên môn về Lập kế hoạch dữ liệu (Data Planning), các kỹ thuật trích xuất dữ liệu, định dạng file, v.v.

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter04.txt`
- **Vị trí lưu trữ:** `webAIAccounting\videoPractice\Chapter04\`
- **Định dạng bắt buộc cho từng Slide (tổng cộng 81 mục):**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên (Thầy) - Dẫn dắt, giải thích chiến lược dữ liệu...]
  Người 2: [Lời thoại Sinh viên - Phản hồi, gọi "thầy", đặt câu hỏi...]
  ```

## 4. Quy trình Thực hiện chi tiết cho Chương 4

### Bước 1: Khởi tạo và Gom dữ liệu
- Đảm bảo thư mục `webAIAccounting\videoPractice\Chapter04` đã được tạo.
- Copy file `Slide_Practice_Ch04.pdf` vào thư mục này để có cơ sở đối chiếu khi sinh kịch bản.

### Bước 2: Bóc tách 81 Slides của Chương 4
Chương 4 có 81 slides, thuộc mức độ vừa phải, chia thành các phần chính:
- **Phần Khởi động:** Giới thiệu tổng quan về việc Lập kế hoạch dữ liệu (Data Planning).
- **Phần Kiến thức cốt lõi:** Các thuộc tính của dữ liệu tốt (chất lượng, độ tin cậy, định dạng). So sánh các nguồn dữ liệu bên trong vs bên ngoài.
- **Phần Kỹ thuật/Thực hành:** Cách trích xuất dữ liệu, nhận diện các định dạng file (CSV, JSON, XML...), hiểu về Database schema.
- **Phần Bài tập (BE, EX, PAC):** Chuyển các bài kiểm tra thành hội thoại hỏi-đáp.

### Bước 3: Nguyên tắc Viết Lời thoại đặc thù cho Chương 4
- **Giảng viên (Thầy):** Văn phong điềm đạm, mang tính chất của một người tư vấn chiến lược. Nhấn mạnh vào việc "rác đầu vào thì rác đầu ra" (Garbage in, Garbage out) - dữ liệu tồi sẽ làm sai lệch mọi phân tích.
- **Sinh viên:** Thể hiện sự tôn trọng, luôn gọi là "thầy" hoặc "thưa thầy". Đặt các câu hỏi thiên về khâu chuẩn bị, ví dụ: "Thưa thầy, nếu dữ liệu công ty bị thiếu thì mình lấy dữ liệu bên ngoài ở đâu bù vào ạ?".
- **Tính liền mạch:** Do dùng công cụ script tự động tạo 1:1, phải đảm bảo các câu chuyển đoạn (chuyển từ slide lý thuyết sang slide hình ảnh minh họa) mượt mà và tự nhiên nhất.

### Bước 4: Kiểm thử (QA)
- **Kiểm tra xưng hô:** Quét toàn bộ file `script_chapter04.txt` để đảm bảo KHÔNG CÓ chữ "cô" hoặc "thầy/cô" nào bị lọt vào.
- **Kiểm tra số lượng:** Đảm bảo đúng 81 mục từ Slide 1 đến Slide 81. Tuyệt đối không gộp chung các slide ILLUSTRATION.

## 5. Triển khai
Sử dụng kế hoạch này kết hợp với script tự động `generate_script.py` đã áp dụng thành công ở Chương 3 (được điều chỉnh lại cho phù hợp với yêu cầu xưng hô và nội dung Chương 4) để tạo file script 1:1 hoàn chỉnh.
