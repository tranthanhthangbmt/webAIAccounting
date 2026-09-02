# Kế hoạch thiết kế Tab Thuật ngữ cho Buổi 2 (Dựa trên Blueprint Buổi 1)

Mục tiêu của kế hoạch này là áp dụng nghiêm ngặt **Bản thiết kế mẫu (Blueprint)** đã thống nhất từ Buổi 1 để xử lý file `depPlan/AIAcc_glossaryDay_02.md` và tiêm an toàn vào tài liệu `docs/buoi_02.md`. 

## User Review Required
Bạn vui lòng xem kỹ các đề xuất xử lý dưới đây. Trọng tâm của Buổi 2 là việc **biên tập lại (rewrite)** toàn bộ 17 thuật ngữ thô thành các định nghĩa học thuật chuẩn mực. Nếu bạn đồng ý, hãy nhấn **Proceed** để tôi tiến hành thực thi ngay lập tức.

## Proposed Changes

Tôi sẽ thực hiện các bước sau một cách tuần tự:

### 1. Chuẩn hóa & Dọn dẹp File nguồn (`AIAcc_glossaryDay_02.md`)
- **Xóa bỏ hội thoại thừa:** Xóa toàn bộ các câu dẫn dắt của AI như *"Tôi đã biên soạn và xuất bản thành công..."* hay *"Để tiếp nối Phần 1..."*.
- **Gỡ bỏ phân cấp Chương:** Xóa các tiêu đề dư thừa như `1. **Chương III: Phương Pháp Luận Khoa Học Dữ Liệu...**`.
- **Biên tập học thuật (Professional Rewrite):** Viết lại toàn bộ 17 thuật ngữ (như *Vòng đời Dự án Khoa học Dữ liệu, Độ chệch vs. Phương sai, Định danh Tài sản mã hóa, Nghịch lý McGinnis...*) theo văn phong từ điển bách khoa. Đảm bảo mọi khái niệm đều đính kèm một **Use case (Trường hợp ứng dụng)** trong Kế toán/Kiểm toán/Tài chính.
- **Chuẩn hóa cú pháp:** Đưa toàn bộ 17 thuật ngữ về định dạng bắt buộc của Blueprint:
  `*   **Tên thuật ngữ (Tiếng Anh - Viết tắt):** Nội dung giải thích...`

### 2. Khởi tạo Kịch bản Tự động hóa (`rebuild_AIAcc_glossary_Day_02.py`)
Tôi sẽ nhân bản và điều chỉnh kịch bản từ Buổi 1 để tạo file `rebuild_AIAcc_glossary_Day_02.py`:
- Trỏ đường dẫn đầu vào: `depPlan/AIAcc_glossaryDay_02.md`
- Trỏ đường dẫn đầu ra: `docs/buoi_02.md`
- **Kế thừa 100% logic:** 
  - Bóc tách từng thuật ngữ thành HTML `<details name="glossary">` để tạo hiệu ứng **Exclusive Accordion** (mở một tab sẽ đóng các tab khác).
  - Tích hợp JavaScript `onclick="setTimeout(() => this.scrollIntoView({behavior: 'smooth', block: 'start'}), 150)"` tạo hiệu ứng **Smooth Scroll**.
  - Xử lý toán học KaTeX (`$$...$$`) và hình ảnh Markdown sang `<img />` với thẻ `<span style="...">` caption.

### 3. Tiêm (Inject) an toàn vào `docs/buoi_02.md`
- Kịch bản sẽ tự động quét file `docs/buoi_02.md`.
- Xóa bỏ tab "Thuật ngữ" cũ (nếu có).
- Chèn trực tiếp khối HTML mới sinh ra vào ngay sát phía trên tab `#### ** 🇬🇧 Tiếng Anh **`.
- **Bảo toàn nguyên vẹn 100% các tab sẵn có.**

## Verification Plan

### Automated Tests
- Chạy thử nghiệm lệnh `python rebuild_AIAcc_glossary_Day_02.py`.
- Quan sát terminal xem log tiêm file báo cáo thành công.

### Manual Verification
- Bạn và tôi sẽ tải lại trang `buoi_02` trên trình duyệt Docsify.
- **Tiêu chí nghiệm thu:**
  1. Tab "Thuật ngữ & Khái niệm" đứng đầu tiên trong khối Tabs.
  2. Các định nghĩa hoàn toàn học thuật, không còn câu từ hội thoại.
  3. Click vào khái niệm bất kỳ -> Mở mượt mà, cuộn lên top, đóng các khái niệm khác.
  4. Các tab Tiếng Anh, Tiếng Việt... vẫn giữ nguyên nội dung.
