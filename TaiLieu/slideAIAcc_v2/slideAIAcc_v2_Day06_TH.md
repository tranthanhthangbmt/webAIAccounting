# KẾ HOẠCH SLIDE THỰC HÀNH - DAY 06 (BUỔI 6)
**Tên bài:** THỰC HÀNH: ỨNG DỤNG AI TRONG PHÂN TÍCH BÁO CÁO TÀI CHÍNH
**Định hướng:** Kế toán thực hành, No-code, sử dụng Advanced Data Analysis.

### Giới thiệu chung
## Title: Buổi 6 TH: Thực hành Phân tích Báo cáo Tài chính.
    - Giảng viên: Đại học Đông Á
    - Môn học: Trí tuệ Nhân tạo cho Kế toán
## Năng lực đạt được sau buổi học.
    - **Về Kiến thức:** Nắm bắt quy trình phân tích dữ liệu đa chiều (Data Cubes) và tỷ số tài chính.
    - **Về Kỹ năng:** Sử dụng ChatGPT (Advanced Data Analysis) để tính toán tự động và viết báo cáo đánh giá sức khỏe tài chính.
    - **Về Tư duy:** Hình thành tư duy đối chiếu, kiểm chứng kết quả do AI tạo ra (Double-check), không phụ thuộc mù quáng.
## Cấu trúc buổi thực hành (Agenda).
    - Chuẩn bị dữ liệu (Data Preparation).
    - Khởi tạo môi trường AI & Upload dữ liệu.
    - Thực thi Prompt tính toán Tỷ số tài chính.
    - Phân tích đa chiều (Pivot/Cubes) và trực quan hóa.
    - Báo cáo đánh giá và phản biện AI.

### Phần 1: Chuẩn bị Dữ liệu (Data Preparation)
## Giới thiệu bộ dữ liệu thực hành.
    - File Excel chứa Bảng Cân đối kế toán (Balance Sheet) và Báo cáo Kết quả Kinh doanh (Income Statement).
    - Dữ liệu thô của 1 công ty niêm yết trong 3 năm liên tiếp.
## Kiểm tra cấu trúc file Excel trước khi đưa vào AI.
    - Tại sao phải kiểm tra? Tránh lỗi "Garbage in, Garbage out".
    - Các cột cần có: Khoản mục, Mã số, Năm T, Năm T-1, Năm T-2.
## Làm sạch dữ liệu (Data Cleansing) cơ bản.
    - Xóa các dòng trống (Blank rows), cột thừa.
    - Bỏ các định dạng phức tạp (Merge cells) có thể làm AI bối rối.
## Chuẩn hóa tiêu đề cột (Headers).
    - Tiêu đề cột phải rõ ràng, ngắn gọn, nên dùng tiếng Anh hoặc tiếng Việt không dấu nếu công cụ AI dễ bị lỗi font.
    - Dòng đầu tiên (Row 1) phải là tên cột.
## Tầm quan trọng của định dạng số liệu (Number format).
    - Số tiền (VNĐ/USD) không được chứa ký tự chữ cái lẫn lộn.
    - Phân biệt dấu phẩy (,) và dấu chấm (.) tùy theo Locale của Excel.

### Phần 2: Khởi tạo môi trường AI \& Upload Dữ liệu
## Kích hoạt Advanced Data Analysis (ADA) trên ChatGPT.
    - Đăng nhập tài khoản ChatGPT.
    - Đảm bảo tính năng phân tích dữ liệu (Data Analyst) được bật.
## Thao tác Upload file an toàn.
    - Kéo thả file Excel vào khung chat.
    - Lưu ý bảo mật: Đổi tên công ty thực thành công ty giả định (Công ty ABC) để bảo vệ dữ liệu nội bộ.
## Prompt số 1 - Lệnh "Đọc hiểu" dữ liệu.
    - "Đóng vai chuyên gia phân tích tài chính. Hãy đọc file Excel đính kèm và tóm tắt cấu trúc dữ liệu của 2 sheet: Balance Sheet và Income Statement."
## Phân tích phản hồi đầu tiên của AI.
    - Kiểm tra xem AI có nhận diện đúng số dòng, số cột và các khoản mục chính không.
    - Nếu AI đọc sai (nhận nhầm header), cần nhắc nhở và sửa lỗi ngay.

### Phần 3: Thực thi Prompt Tính toán Tỷ số tài chính
## Prompt số 2 - Tính toán Nhóm Thanh khoản (Liquidity).
    - "Dựa trên dữ liệu, hãy tạo một bảng tính Tỷ số thanh toán hiện hành và Tỷ số thanh toán nhanh cho cả 3 năm."
## Đọc kết quả Tỷ số Thanh khoản.
    - So sánh kết quả AI trả về với công thức chuẩn.
    - Kiểm tra xem AI lấy số liệu "Tài sản ngắn hạn" ở dòng nào.
## Prompt số 3 - Tính toán Nhóm Đòn bẩy (Solvency).
    - "Tiếp tục tính Tỷ số Nợ / Vốn chủ sở hữu (D/E) và Tỷ số Nợ / Tổng tài sản cho 3 năm."
## Đọc kết quả Tỷ số Đòn bẩy.
    - Phân tích rủi ro từ con số AI đưa ra.
    - Xác minh AI có cộng đúng tổng nợ (Nợ ngắn + Nợ dài) hay không.
## Prompt số 4 - Tính toán Nhóm Sinh lời (Profitability).
    - "Hãy tính ROA, ROE và Biên lợi nhuận gộp. Trình bày dưới dạng bảng so sánh."
## Đọc kết quả Tỷ số Sinh lời.
    - AI thường tính ROA bằng Tổng tài sản cuối kỳ hay Bình quân? (Yêu cầu AI giải thích công thức nó đã dùng).
## Prompt nâng cao - Mô hình DuPont.
    - "Sử dụng dữ liệu hiện có, hãy phân tách ROE của năm gần nhất theo Mô hình DuPont 3 nhân tố."
## Phân tích kết quả DuPont do AI xuất ra.
    - Nhìn vào 3 nhân tố (Biên lợi nhuận ròng, Vòng quay TS, Đòn bẩy).
    - Nguyên nhân nào làm thay đổi ROE?

### Phần 4: Phân tích Đa chiều (Từ Spreadsheet sang Data Cubes)
## Giới thiệu khái niệm Data Cubes cơ bản.
    - Vượt ra khỏi bảng 2 chiều (Dòng x Cột).
    - Thêm các chiều phân tích (Dimension): Thời gian, Chi nhánh, Dòng sản phẩm.
## Data Cubes trong AI.
    - Khác với Excel Pivot Table phải kéo thả thủ công.
    - AI có thể tạo các lát cắt dữ liệu (Slice and Dice) bằng mã Python ngầm định.
## Prompt số 5 - Tạo Data Cubes giả lập.
    - "Hãy nhóm doanh thu và chi phí theo từng quý (nếu có dữ liệu) và so sánh sự tăng trưởng (YoY)."
## Trực quan hóa dữ liệu (Data Visualization).
    - Yêu cầu AI: "Hãy vẽ biểu đồ cột thể hiện sự biến động của Doanh thu thuần và Lợi nhuận sau thuế trong 3 năm."
## Trực quan hóa cấu trúc vốn.
    - Yêu cầu AI: "Vẽ biểu đồ tròn (Pie chart) thể hiện cơ cấu Nợ và Vốn chủ sở hữu của năm mới nhất."
## Trực quan hóa xu hướng tỷ số.
    - Yêu cầu AI: "Vẽ biểu đồ đường (Line chart) mô tả xu hướng của ROA và ROE, thêm đường trung bình ngành (giả định là 10%)."

### Phần 5: Báo cáo Đánh giá và Phản biện AI
## Prompt Tổng hợp - Viết báo cáo Sức khỏe tài chính.
    - "Dựa trên tất cả các tỷ số đã tính, hãy viết một đoạn nhận xét 300 chữ đánh giá sức khỏe tài chính của công ty. Nêu rõ 2 điểm mạnh và 2 rủi ro."
## Đánh giá Báo cáo của AI.
    - Báo cáo có logic không? Các nhận định có khớp với số liệu không?
    - Phát hiện những lời "sáo rỗng" hoặc "ảo giác" của AI.
## Phản biện lại AI.
    - Kỹ năng quan trọng: Yêu cầu AI giải thích "Tại sao bạn kết luận rủi ro thanh khoản cao khi Tỷ số hiện hành là 1.5?".
    - Xem AI giải thích các giả định của nó.
## Kết xuất kết quả cuối cùng.
    - Hướng dẫn sinh viên copy/paste báo cáo và biểu đồ từ ChatGPT vào Word/PowerPoint để hoàn thiện bài tập nhóm.
## Tổng kết buổi thực hành.
    - Điểm lại các lệnh Prompt hiệu quả nhất đã sử dụng.
    - Nhắc nhở: AI chỉ là công cụ hỗ trợ tính toán nhanh, linh hồn của bài phân tích vẫn là tư duy tài chính của người làm kế toán.
## Q&A - Giải đáp thắc mắc.
    - Sinh viên đặt câu hỏi về các lỗi gặp phải khi thực thi Prompt.
    - Bài tập về nhà: Tự tải BCTC của 1 công ty khác (VNM, FPT) và thực hiện quy trình tương tự.
