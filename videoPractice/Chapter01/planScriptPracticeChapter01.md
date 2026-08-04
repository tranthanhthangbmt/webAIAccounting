# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 1

Tài liệu này mô tả chi tiết phương pháp luận, cấu trúc và quy trình từng bước đã được sử dụng để tạo ra kịch bản quay video (Script) cho bài giảng thực hành Chương 1. Đây sẽ là bản mẫu chuẩn (template) để áp dụng đồng loạt cho các chương tiếp theo.

## 1. Mục tiêu cốt lõi
- Tạo ra một kịch bản quay video/thu âm chi tiết, sinh động, dễ hiểu nhằm phục vụ sinh viên thực hành.
- Hình thức thể hiện: Đối thoại tương tác giữa 2 nhân vật (Người 1: Giảng viên và Người 2: Sinh viên).
- Yêu cầu tiên quyết: Kịch bản phải khớp 100% với nội dung và cấu trúc của slide thuyết trình (1 slide tương ứng với 1 đoạn kịch bản).

## 2. Nguyên liệu Đầu vào (Inputs)
Để xây dựng kịch bản, cần thu thập đủ 3 tài nguyên sau:
1. **File mã nguồn Slide (`.tex`):** Ví dụ `Slide_Practice_Ch01.tex`. Cần file này để đếm chính xác số lượng thẻ `\begin{frame}`, từ đó đảm bảo không bỏ sót bất kỳ slide nào. Nó cũng cung cấp chính xác Text và Tiêu đề có trên slide.
2. **File PDF Slide (`.pdf`):** Ví dụ `Slide_Practice_Ch01.pdf`. Cần copy từ thư mục tài liệu sang thư mục làm việc (`videoPractice\Chapter01`) để phục vụ việc tham chiếu hình ảnh trong lúc đọc kịch bản.
3. **Tài liệu Textbook gốc:** Ví dụ `Ch_01_Data and Analytics in the Accounting Profession.pdf`. Cung cấp bối cảnh, câu chuyện thực tế (như ví dụ về công cụ Alteryx, số liệu phân tích) để đưa vào lời thoại của Giảng viên.

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter01.txt` (hoặc tương ứng theo chương).
- **Vị trí lưu trữ:** Nằm trong thư mục riêng của từng chương (VD: `webAIAccounting\videoPractice\Chapter01\`).
- **Định dạng bắt buộc:**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên - Dẫn dắt, giải thích, đặt câu hỏi gợi mở...]
  Người 2: [Lời thoại Sinh viên - Tương tác, trả lời, thể hiện sự ngạc nhiên hoặc đúc kết vấn đề...]
  ```

## 4. Quy trình Thực hiện (4 Bước)

### Bước 1: Khởi tạo và Gom nhóm dữ liệu
- Tạo thư mục riêng cho chương đang làm (VD: `Chapter01`).
- Copy file PDF slide vào thư mục vừa tạo.

### Bước 2: Bóc tách Cấu trúc Slide
- Mở file `.tex` của chương tương ứng.
- Liệt kê toàn bộ các slide theo thứ tự từ trang bìa đến trang kết thúc.
- Xác định rõ tính chất của từng slide (Lý thuyết, Hình ảnh minh họa, Bảng điều khiển, Bài tập BE/EX, hay Case Study PAC).

### Bước 3: Viết Lời thoại (Scripting)
Xây dựng lời thoại linh hoạt theo từng loại Slide:
- **Slide Khái niệm / Mở đầu:** "Người 1" dùng ngôn ngữ đời thường để đặt vấn đề. "Người 2" đưa ra những thắc mắc phổ biến của người đi làm/sinh viên để "Người 1" giải đáp.
- **Slide Hình ảnh / Bảng biểu (Dashboards):** "Người 1" phải chỉ đích danh chi tiết trên hình (VD: "Các em nhìn vào cột màu cam...", "Nhìn vào góc dưới màn hình..."). Điều này giúp người xem video biết mắt mình nên tập trung vào đâu.
- **Slide Mô hình (MOSAIC, SPARKS):** Chuyển hóa các gạch đầu dòng khô khan thành các câu kể chuyện có logic nhân quả.
- **Slide Bài tập (Brief Exercises, Exercises, PAC):** Biến thành mô hình Hỏi - Đáp. "Người 1" đóng vai trò người ra đề, tóm tắt tình huống. "Người 2" đưa ra đáp án và giải thích ngắn gọn lý do vì sao lại chọn đáp án đó.

### Bước 4: Kiểm thử và Rà soát (QA)
- **Kiểm tra số lượng:** Đếm tổng số mục "Slide X:" trong kịch bản. So sánh với tổng số lệnh `\begin{frame}` trong file `.tex`. Phải bằng nhau tuyệt đối (VD: Chương 1 có đúng 46 slides).
- **Kiểm tra văn phong:** Đọc nhẩm lại kịch bản để xem ngôn từ có tự nhiên không (Văn nói). Đảm bảo câu thoại không quá dài, ngắt nghỉ hợp lý.

## 5. Kế hoạch Triển khai cho các Chương tiếp theo
Sử dụng chính tài liệu `.md` này như một "SOP (Standard Operating Procedure)". Khi có yêu cầu làm script cho Chương 2, Chương 3..., tác nhân AI hoặc người dùng chỉ cần:
1. Tạo folder tương ứng.
2. Nạp file `.tex` của chương đó.
3. Đếm số lượng slide.
4. Triển khai viết script theo đúng format quy định ở phần 3 và phương pháp ở phần 4.
