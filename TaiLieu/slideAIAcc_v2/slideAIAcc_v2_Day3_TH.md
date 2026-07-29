# KẾ HOẠCH SLIDE THỰC HÀNH - DAY 3 (BUỔI 3 TH)
**Tên bài:** THỰC HÀNH AI HỖ TRỢ NHẬP LIỆU \& ĐỌC CHỨNG TỪ (NO-CODE)
**Định hướng:** Chuyển hóa tư duy "AI-Assisted Coding" thành "AI-Assisted Accounting" (Kế toán No-Code). Hướng dẫn sinh viên dùng ChatGPT/Copilot như một trợ lý trích xuất dữ liệu, đọc hóa đơn và xuất file Excel.
**Cấu trúc:** 32 Slides.

**ĐỀ XUẤT NGUỒN ẢNH MINH HỌA:**
- **Ảnh thực tế:** Các mẫu hóa đơn đỏ (VAT), hóa đơn bán lẻ, bill nhà hàng, bill taxi.
- **Ảnh chụp màn hình (Screenshot):** Giao diện chat với ChatGPT/Copilot, cách upload file, kết quả trả về dạng bảng, cách tải file CSV/Excel.
- **Sinh ảnh AI:** Sinh viên kế toán đang vui vẻ uống trà trong khi màn hình máy tính tự động chạy số liệu.

---

# PHẦN 1: GIỚI THIỆU \& CHUẨN BỊ MÔI TRƯỜNG THỰC HÀNH

## TRANG BÌA (Title Page)
- Tiêu đề chính: Trí tuệ Nhân tạo cho Kế toán (Thực hành)
- Tiêu đề phụ: Buổi 3 - AI Hỗ trợ Nhập liệu \& Đọc Chứng từ
- Tác giả: Đại học Đông Á
- *(🖼️ Ảnh minh họa: Một màn hình máy tính chia đôi, một bên là hóa đơn giấy lộn xộn, một bên là bảng Excel gọn gàng).*

## Năng lực đạt được sau buổi học
- **Về Lý thuyết (LT):** Nắm vững chiến thuật "Provide formatting instructions" (chỉ định định dạng đầu ra) trong cẩm nang OpenAI Prompt Engineering Guide.
- **Về Thực hành (TH):** Biết cách tải hình ảnh/PDF hóa đơn lên ChatGPT hoặc dùng tính năng trích xuất dữ liệu hình ảnh của Excel để bóc tách thông tin (Tên công ty, MST, Số tiền, Ngày tháng) và xuất ra bảng; Biết cách Import dữ liệu Excel vào phần mềm Kế toán.
- **Về Tư duy nghề nghiệp:** Hình thành thói quen luôn kiểm tra chéo (Cross-check) độ chính xác của dữ liệu do AI xuất ra (Human-in-the-loop).

## Tư duy "Vibe Accounting" (Làm việc bằng cảm hứng)
- \textbf{Vibe Coding} là thuật ngữ giới lập trình dùng để chỉ việc: Bạn không cần viết code, chỉ cần mô tả ý tưởng, AI sẽ viết code.
- \textbf{Vibe Accounting:} Kế toán không cần gõ phím cạch cạch nhập số, chỉ cần tải hóa đơn lên và ra lệnh: *"Lọc cho tôi số tiền thuế!"*, AI sẽ trả về kết quả.

## Công cụ sử dụng trong buổi học
- \textbf{Microsoft Copilot:} Tích hợp sẵn trong trình duyệt Edge, miễn phí, xử lý ảnh và PDF rất tốt.
- \textbf{ChatGPT (Bản Free/Plus):} Phân tích dữ liệu (Advanced Data Analysis) cực mạnh.
- \textbf{Microsoft Excel / Google Sheets:} Để kiểm tra kết quả đầu ra.
- *(Giảng viên yêu cầu sinh viên mở sẵn trình duyệt và đăng nhập).*

## Bộ dữ liệu thực hành (Dataset)
- Lớp trưởng gửi link Google Drive chứa thư mục "Day3\_ChungTu".
- Bao gồm:
  - 2 ảnh chụp bill ăn uống (JPG).
  - 2 ảnh chụp hóa đơn viết tay (PNG).
  - 3 file hóa đơn điện tử (PDF).
- Sinh viên tải toàn bộ về máy.

---

# PHẦN 2: BÀI TẬP 1 - XỬ LÝ HÓA ĐƠN BÁN LẺ (ẢNH CHỤP)

## Bài toán 1 - Thanh toán công tác phí
- \textbf{Bối cảnh:} Nhân viên kinh doanh đi công tác về, ném cho bạn một xấp ảnh chụp các bill ăn uống, taxi, tiếp khách.
- \textbf{Yêu cầu cũ:} Bạn phải căng mắt ra đọc từng bill, nhập vào Excel để làm Phiếu chi.

## Bước 1 - Tải ảnh lên Copilot/ChatGPT
- Hướng dẫn thao tác đính kèm hình ảnh (Nút kẹp ghim / dấu +).
- Chọn file `Bill_Taxi_01.jpg`.
- *(🖼️ Ảnh minh họa: Ảnh chụp màn hình vị trí nút Upload trên ChatGPT).*

## Bước 2 - Viết Prompt cơ bản
- \textbf{Prompt 1:} *"Hãy đọc hình ảnh này và cho tôi biết đây là hóa đơn gì, tổng số tiền là bao nhiêu?"*
- Sinh viên gõ prompt và quan sát tốc độ AI đọc ảnh (OCR).

## Bước 3 - Viết Prompt cấu trúc (Structured Prompt)
- Prompt 1 quá thô sơ. Kế toán cần dữ liệu có cấu trúc.
- \textbf{Prompt 2:} *"Bạn là một kế toán viên. Hãy đọc bill này và trích xuất thông tin theo định dạng sau: Tên đơn vị cung cấp | Ngày tháng | Nội dung chi | Số tiền."*

## Xử lý nhiều bill cùng lúc (Batch Processing)
- Tải lên cùng lúc 3 file ảnh `Bill_01`, `Bill_02`, `Bill_03`.
- \textbf{Prompt 3:} *"Hãy đọc cả 3 hóa đơn này. Lập cho tôi một bảng tổng hợp gồm các cột: STT, Tên cửa hàng, Ngày, Số tiền. Cuối bảng tính tổng số tiền."*

## Human-in-the-loop (Kiểm tra chéo)
- \textbf{Nhiệm vụ sinh viên:} Đối chiếu kết quả AI trả về với ảnh gốc.
- \textit{Câu hỏi thảo luận:} AI có đọc nhầm số "0" thành chữ "O", hay số "8" thành số "3" ở bill viết tay không?
- Rút ra bài học: Luôn phải review lại dữ liệu.

---

# PHẦN 3: BÀI TẬP 2 - ĐỌC HÓA ĐƠN ĐIỆN TỬ (PDF)

## Bài toán 2 - Hóa đơn GTGT
- \textbf{Bối cảnh:} Doanh nghiệp nhận được file PDF hóa đơn GTGT mua hàng từ nhà cung cấp (vài chục dòng hàng hóa).
- \textbf{Khó khăn:** Không thể copy/paste từng dòng vào phần mềm kế toán vì dễ lệch dòng.

## Xử lý File PDF với AI
- Hướng dẫn sinh viên upload file `HoaDon_MuaHang_01.pdf` lên ChatGPT.
- Giới hạn: Nếu dùng bản miễn phí, có thể copy toàn bộ Text trong PDF (Ctrl+A, Ctrl+C) và dán vào cửa sổ chat nếu không cho up file.

## Prompt trích xuất phần Header (Thông tin chung)
- \textbf{Prompt 4:} *"Hãy đọc hóa đơn này và liệt kê: Ký hiệu hóa đơn, Số hóa đơn, Ngày lập, Mã số thuế người bán, Tên người bán."*

## Prompt trích xuất Chi tiết hàng hóa (Line Items)
- Đây là phần tốn thời gian nhất của kế toán.
- \textbf{Prompt 5:} *"Hãy lập một bảng chi tiết các mặt hàng trong hóa đơn này. Cột gồm: STT, Tên Hàng Hóa, ĐVT, Số lượng, Đơn giá, Thành tiền (Chưa VAT)."*

## Ép kiểu dữ liệu (Data Formatting)
- Kế toán ghét nhất là AI trả về số tiền có chữ "VNĐ" dính liền (Vd: 1.000.000VNĐ) vì không tính toán được.
- \textbf{Prompt 6 (Nâng cấp):} *"Làm lại bảng trên. Lưu ý ở cột Số lượng, Đơn giá và Thành tiền, CHỈ in ra con số, không chứa chữ 'VNĐ' hay ký tự tiền tệ, sử dụng dấu phẩy để phân cách hàng nghìn."*

## Kiểm tra tính toán (Math Check)
- AI đôi khi làm toán dở!
- \textbf{Nhiệm vụ sinh viên:} Dùng máy tính bỏ túi hoặc nhẩm lại xem cột Số lượng x Đơn giá có thực sự bằng cột Thành tiền mà AI xuất ra không.
- Nếu sai $\rightarrow$ Dạy AI tính lại.

---

# PHẦN 4: CHUYỂN ĐỔI DỮ LIỆU SANG EXCEL

## Từ Chatbot ra Excel
- Không ai để bảng dữ liệu nằm trên ChatGPT. Phải mang nó về phần mềm.
- Cách 1: Copy \& Paste.
- Cách 2: Yêu cầu AI tạo file tải về.

## Cách 1 - Copy \& Paste chuẩn xác
- Sinh viên bôi đen bảng trên ChatGPT, mở Excel.
- Hướng dẫn dùng tính năng `Paste Special` $\rightarrow$ `Text` để không bị vỡ khung bảng.
- *(🖼️ Ảnh minh họa: Thao tác Paste Special trong Excel).*

## Cách 2 - Xuất file CSV (Khuyên dùng)
- \textbf{Prompt 7:} *"Hãy lưu bảng chi tiết hàng hóa vừa tạo thành một file định dạng .CSV để tôi tải về."*
- Click vào link tải file.

## Sửa lỗi Font Tiếng Việt khi mở CSV
- **Lỗi phổ biến:** Mở file CSV bằng Excel bị lỗi font chữ Tiếng Việt (Unicode UTF-8).
- **Cách khắc phục:**
  1. Mở Excel trắng.
  2. Vào Data $\rightarrow$ From Text/CSV.
  3. Ở mục File Origin, chọn `65001: Unicode (UTF-8)`.
  4. Bấm Load.

## Thực hành độc lập
- Sinh viên áp dụng kỹ năng từ đầu buổi đến giờ để xử lý file `HoaDon_MuaHang_02.pdf` và `HoaDon_MuaHang_03.pdf`.
- Đích đến: Tạo ra 1 file Excel duy nhất tổng hợp cả 2 hóa đơn.

---

# PHẦN 5: BÀI TẬP 3 - ĐỐI CHIẾU VÀ TÌM KIẾM BẤT THƯỜNG

## Bài toán 3 - 3-Way Matching
- \textbf{Bối cảnh:} Kế toán cần kiểm tra xem Hóa đơn có khớp với Đơn đặt hàng (PO) không.
- Tải lên 2 file: `PO_101.pdf` và `HoaDon_101.pdf`.

## Kỹ thuật Prompt Đối chiếu
- \textbf{Prompt 8:} *"Tôi vừa tải lên Đơn đặt hàng và Hóa đơn của cùng 1 giao dịch. Hãy so sánh cột Số lượng và Đơn giá của từng mặt hàng giữa 2 file. Hãy lập bảng chỉ ra các mặt hàng có sự chênh lệch (nếu có)."*
- Sinh viên quan sát AI đóng vai trò như một Kiểm toán viên nội bộ.

## Bài toán 4 - Dò tìm rủi ro thuế
- Tải lên file `DanhSach_HoaDon_Thang5.xlsx` (bảng kê mua vào, khoảng 50 dòng).
- \textbf{Prompt 9:} *"Hãy đóng vai nhân viên thuế. Kiểm tra bảng kê này và tìm cho tôi: 1. Hóa đơn có ngày xuất vào cuối tuần. 2. Hóa đơn có giá trị lớn hơn 20 triệu nhưng chưa đánh dấu thanh toán chuyển khoản."*

## Xử lý dữ liệu bị khuyết thiếu (Missing Data)
- Có những bill bị mất góc, rách mờ.
- \textbf{Prompt 10:} *"Đọc bill này. Nếu thông tin nào bị mờ không đọc được, hãy điền chữ '[CẦN KIỂM TRA LẠI]' vào ô đó."*
- Giúp kế toán dễ dàng filter trong Excel để xử lý sau.

---

# PHẦN 6: BẢO MẬT DỮ LIỆU THỰC TẾ

## Cảnh báo quan trọng khi thực hành
- Hôm nay chúng ta đang dùng các file chứng từ mẫu (Dummy data).
- \textbf{TUYỆT ĐỐI KHÔNG} dùng hóa đơn thật, hợp đồng thật của công ty để up lên ChatGPT bản miễn phí.
- Nhắc lại bài học Lý thuyết: Dữ liệu của bạn sẽ bị đem đi huấn luyện mô hình.

## Thiết lập quyền riêng tư trên ChatGPT
- Hướng dẫn sinh viên tắt tính năng lưu trữ lịch sử để bảo vệ dữ liệu.
- \textbf{Thao tác:} Settings $\rightarrow$ Data Controls $\rightarrow$ Tắt "Chat history \& training".
- *(🖼️ Ảnh minh họa: Màn hình cài đặt Data Controls của ChatGPT).*

## Xóa dữ liệu nhạy cảm (Sanitization) trước khi dùng AI
- Dùng công cụ bôi đen (Redact) trên PDF để che đi: Số tài khoản ngân hàng, Mã số CCCD của khách hàng trước khi tải lên AI.
- Đảm bảo tuân thủ quyền riêng tư (Privacy).

---

# PHẦN 7: TỔNG KẾT \& ĐÁNH GIÁ

## Báo cáo kết quả thực hành
- Sinh viên nộp lại file Excel cuối cùng lên hệ thống LMS.
- Chụp ảnh màn hình 1 câu Prompt hay nhất mà bạn đã sáng tạo ra để xử lý lỗi của AI.

## Ôn tập \& Rút kinh nghiệm
- \textbf{Ưu điểm:} Nhanh gấp 10 lần gõ tay, xuất bảng Excel đẹp.
- \textbf{Nhược điểm:} Thi thoảng AI bị "ngáo", tính toán sai, hoặc từ chối đọc file nếu file quá lớn.
- Kế toán viên phải luôn giữ vai trò người soát xét (Reviewer).

## Q\&A và Dặn dò
- Giải đáp thắc mắc về các lỗi file CSV, lỗi prompt không ra bảng.
- \textbf{Buổi sau (Day 4):} Chuyển sang dùng AI để phân tích nghiệp vụ kế toán chuyên sâu (Định khoản, tập hợp chi phí). Chuẩn bị ôn lại kiến thức Nguyên lý kế toán!
