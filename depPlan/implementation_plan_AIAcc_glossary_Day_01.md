# Kế hoạch thiết kế Tab Thuật ngữ chuẩn hóa (Blueprint áp dụng từ Buổi 1)

Mục tiêu của kế hoạch này là đóng gói toàn bộ quy trình thiết kế, dọn dẹp và tiêm (inject) Tab "Thuật ngữ & Khái niệm cốt lõi" vào tài liệu bài giảng. Quy trình này đã được áp dụng thành công cho Buổi 1 (`AIAcc_glossaryDay_01.md` -> `docs/buoi_01.md`) và sẽ được dùng làm **Bản thiết kế mẫu (Blueprint) chuẩn** để triển khai tiếp cho Buổi 2 (`AIAcc_glossaryDay_02.md`) và các buổi sau.

## Các tiêu chuẩn bắt buộc đối với File nguồn (Glossary Source)

Trước khi chạy kịch bản tự động hóa, nội dung thuật ngữ cần được biên tập theo các tiêu chuẩn sau:
1. **Chuẩn học thuật:** Giải thích định nghĩa mang tính chuyên ngành, đi thẳng vào bản chất công nghệ.
2. **Gắn liền Nghiệp vụ:** Mỗi định nghĩa phải đi kèm với *Use case* (trường hợp ứng dụng) thực tế trong ngành Kế toán - Kiểm toán - Tài chính.
3. **Định dạng Markdown chuẩn:** Mỗi khái niệm phải tuân thủ nghiêm ngặt cú pháp danh sách (Bullet point):
   `*   **Tên thuật ngữ (Tiếng Anh - Viết tắt):** Nội dung giải thích...`
4. **Không chứa văn bản dư thừa:** Gỡ bỏ toàn bộ các câu hội thoại giao tiếp của AI (VD: "Tôi đã tổng hợp...", "Bạn hãy mở bảng Studio...").

## Kịch bản Tự động hóa (Python Script)

Với Buổi 1, script `rebuild_AIAcc_glossary_Day_01.py` đã thực hiện các bước xử lý kỹ thuật sau. Khi làm cho Buổi 2, bạn chỉ cần tạo bản sao (VD: `rebuild_AIAcc_glossary_Day_02.py`) và thay đổi đường dẫn file.

### 1. Dọn dẹp cấu trúc thô (Clean-up)
- Quét và xóa các dấu trích dẫn dạng `[cite: XXX]` bằng Regex: `r'(?:\\\\)*[ \t]*\[cite: \d+\]'`.
- Tự động dọn dẹp các heading phân nhóm (`### ...`) và các dải gạch ngang phân cách (`***`) để làm phẳng cấu trúc.

### 2. Giao diện Đóng/Mở Độc quyền (Exclusive Accordion) & Cuộn mượt (Smooth Scroll)
Thay vì nhóm chung các khái niệm, kịch bản dùng Regex để bóc tách từng Bullet point và bọc nó vào một khối HTML độc lập:
```html
<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)">
<summary><b style="font-size:1.2em">Tên thuật ngữ</b></summary>
<br>

Nội dung giải thích...

</details>
```
- **Exclusive Accordion:** Thuộc tính `name="glossary"` giúp đảm bảo tại một thời điểm chỉ có 1 khái niệm được mở (mở cái này sẽ tự đóng cái kia).
- **Smooth Scroll:** Sự kiện `onclick` kết hợp JavaScript giúp tự động đẩy khái niệm đang đọc lên vị trí cao nhất của màn hình, mang lại trải nghiệm UX tuyệt vời.

### 3. Xử lý Hình ảnh bằng thẻ `<span>` (Bảo toàn Markdown)
- Quét tìm định dạng hình ảnh Markdown (`![Alt](URL)`).
- Trích xuất thành thẻ `<img />` và chèn caption bằng thẻ nội tuyến **`<span>`** với đầy đủ CSS (in nghiêng, căn giữa) để danh sách không bị sập.

### 4. Xử lý Toán học (Tích hợp KaTeX)
- Chuyển đổi toàn bộ khối công thức `\\[ ... \\]` thành `$$ ... $$`.
- Chuyển đổi công thức nội tuyến `\\( ... \\)` thành `$ ... $`.
- Hỗ trợ multiline nhờ cờ `re.DOTALL`.

### 5. Tiêm (Inject) an toàn vào `docs/buoi_XX.md`
- Thuật toán quét file đích (`docs/buoi_01.md`, `docs/buoi_02.md`).
- Xóa bỏ Tab "Thuật ngữ" cũ nếu có (bằng Regex quét từ khóa `#### ** 📚 Thuật ngữ & Khái niệm **` đến `#### ** 🇬🇧 Tiếng Anh **`).
- **Tiêm Tab mới:** Chèn toàn bộ nội dung mới vừa sinh ra vào vị trí ngay trên tab `#### ** 🇬🇧 Tiếng Anh **`.
- **An toàn tuyệt đối:** Đảm bảo 100% các tab sẵn có (Tiếng Anh, Tiếng Việt, Slide, Video...) ở bên cạnh không bị mất hay thay đổi.

## Quy trình Thực thi (Verification Plan)

Khi bạn triển khai cho `AIAcc_glossaryDay_02.md`:
1. Chạy lệnh: `python rebuild_AIAcc_glossary_Day_02.py`
2. Tải lại trang web (Docsify / Live Server).
3. **Tiêu chí nghiệm thu:**
   - Tab "Thuật ngữ & Khái niệm" xuất hiện ngoài cùng bên trái.
   - Click vào một thuật ngữ bất kỳ: Các thuật ngữ khác tự thu gọn, thuật ngữ được click trượt mượt mà lên đầu trang.
   - Nội dung học thuật, chuyên nghiệp, hiển thị tốt công thức toán học và ảnh.
