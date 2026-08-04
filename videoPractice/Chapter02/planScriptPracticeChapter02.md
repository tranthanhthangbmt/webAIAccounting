# Kế hoạch Xây dựng Kịch bản (Script) Bài giảng Thực hành - Chương 2

Tài liệu này đóng vai trò như một SOP (Quy trình thao tác chuẩn) để bám sát và xây dựng kịch bản (Script) quay video thực hành cho Chương 2, đảm bảo tính thống nhất về cấu trúc và văn phong đã được thiết lập từ Chương 1.

## 1. Mục tiêu cốt lõi
- Tạo ra một kịch bản quay video/thu âm chi tiết, bám sát các kỹ năng nền tảng trong phân tích dữ liệu (Cơ sở dữ liệu, Hàm Excel, Pivot Tables, Thống kê mô tả và Trực quan hóa).
- Hình thức thể hiện: Đối thoại tương tác sinh động giữa 2 nhân vật (Người 1: Giảng viên hướng dẫn và Người 2: Sinh viên thực hành).
- Yêu cầu tiên quyết: Kịch bản phải khớp 100% với số lượng slide trong file thuyết trình (Chương 2 có tổng cộng 45 slides).

## 2. Nguyên liệu Đầu vào (Inputs)
Để xây dựng kịch bản cho Chương 2, cần 3 tài nguyên sau:
1. **File mã nguồn Slide (`Slide_Practice_Ch02.tex`):** Lấy từ thư mục `TaiLieu/slidePractice`. Dùng để trích xuất 45 tiêu đề slide và cấu trúc nội dung.
2. **File PDF Slide (`Slide_Practice_Ch02.pdf`):** Cần copy từ thư mục tài liệu sang thư mục làm việc hiện tại (`videoPractice\Chapter02`) để tham chiếu hình ảnh, biểu đồ khi đọc thoại.
3. **Tài liệu Textbook gốc (`Ch_02_Foundational Data Analysis Skills.pdf`):** Lấy từ `TaiLieu/textbookForPractice`. Cung cấp bối cảnh chi tiết và lời khuyên của chuyên gia (ví dụ: "Josh's Insight" về Pivot Tables) để thêm vào thoại.

## 3. Tiêu chuẩn Đầu ra (Outputs)
- **Tên file:** `script_chapter02.txt`
- **Vị trí lưu trữ:** `webAIAccounting\videoPractice\Chapter02\`
- **Định dạng bắt buộc cho từng Slide (tổng cộng 45 mục):**
  ```text
  Slide [Số thứ tự]: [TIÊU ĐỀ SLIDE ĐƯỢC VIẾT HOA]
  Người 1: [Lời thoại Giảng viên - Giải thích khái niệm, hướng dẫn thao tác (VD: "Các em kéo trường Doanh thu vào ô Values...")]
  Người 2: [Lời thoại Sinh viên - Tương tác, đặt câu hỏi về các lỗi thường gặp hoặc đúc kết kiến thức]
  ```

## 4. Quy trình Thực hiện chi tiết cho Chương 2

### Bước 1: Khởi tạo
- Đảm bảo thư mục `webAIAccounting\videoPractice\Chapter02` đã được tạo.
- (Tùy chọn) Copy file `Slide_Practice_Ch02.pdf` vào thư mục này để đối chiếu.

### Bước 2: Bóc tách 45 Slides của Chương 2
- Quét qua file `.tex` để chia kịch bản thành các cụm nội dung chính:
  - **LO 2.1:** Lưu trữ & Cơ sở dữ liệu (Tables, Relationships, Keys).
  - **LO 2.2:** Hàm bảng tính (Excel functions như VLOOKUP, INDEX, MATCH).
  - **LO 2.3:** Pivot Tables (Cách kéo thả, phân tích đa chiều).
  - **LO 2.4:** Thống kê mô tả (Mean, Median, Mode).
  - **LO 2.5:** Trực quan hóa dữ liệu.
  - **Bài tập (BE, EX, PAC):** Chuyển hóa thành hội thoại hỏi đáp.

### Bước 3: Nguyên tắc Viết Lời thoại đặc thù cho Chương 2
Do Chương 2 mang tính "cầm tay chỉ việc" rất cao (liên quan đến Excel và Database), lời thoại cần thay đổi cho phù hợp:
- **Người 1 (Giảng viên):** Thay vì chỉ giảng đạo lý, cần dùng những từ ngữ mang tính hành động (Action-oriented) như: "Hãy nhìn vào cột A", "Khi các em gộp hai bảng này bằng khóa chính...", "Để ý hàm XLOOKUP khác VLOOKUP ở chỗ...".
- **Người 2 (Sinh viên):** Đóng vai trò là một người mới học, thường xuyên đặt những câu hỏi dễ sai lầm: "Thầy ơi, khóa ngoại (Foreign key) khác khóa chính ở đâu ạ?", "Em dùng Pivot Table nhưng số không khớp, em phải check lại chỗ nào ạ?".
- Các hình ảnh minh họa (ILLUSTRATION 2.X) phải được nhắc tên rõ ràng để người xem video dễ theo dõi.

### Bước 4: Kiểm thử (QA)
- **Kiểm tra số lượng:** Phải có đúng 45 mục "Slide X:" từ Slide 1 đến Slide 45.
- **Kiểm tra luồng thao tác:** Đọc lại các hướng dẫn về hàm Excel và Pivot Table xem đã dễ hiểu nếu chỉ nghe qua audio chưa. 

## 5. Triển khai
Sử dụng kế hoạch này để trực tiếp ra lệnh tạo file `script_chapter02.txt` ngay sau đây.
