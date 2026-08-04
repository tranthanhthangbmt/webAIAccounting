chapter_title = 'Chuẩn bị Dữ liệu'
chapter_subtitle = 'Analysis: Data Preparation'

slides = [
    {
        "type": "title_slide",
    },
    {
        "type": "normal",
        "title": "Góc nhìn Chuyên gia (Professional Insight)",
        "content": r"""\begin{itemize}
    \item \textbf{Thực tế 80/20:} Chuẩn bị dữ liệu thường chiếm 80\% thời gian của một dự án phân tích dữ liệu, chỉ 20\% còn lại dành cho việc phân tích thực sự.
    \item \textbf{Rác vào - Rác ra (GIGO):} Dữ liệu không được chuẩn bị kỹ lưỡng sẽ dẫn đến kết quả phân tích sai lệch, bất kể mô hình học máy (Machine Learning) có phức tạp đến đâu.
    \item \textbf{Tầm quan trọng của ETL:} Quá trình Trích xuất (Extract), Chuyển đổi (Transform), và Tải (Load) là kỹ năng cốt lõi bắt buộc đối với một Kế toán viên trong kỷ nguyên số.
\end{itemize}""",
    },
    {
        "type": "normal",
        "title": "Lộ trình Chương (Chapter Roadmap)",
        "content": r"""\begin{itemize}
    \item \textbf{LO 5.1:} Định hình dữ liệu (Data Profiling).
    \item \textbf{LO 5.2:} Mô tả quá trình ETL.
    \item \textbf{LO 5.3:} Mẫu trích xuất dữ liệu.
    \item \textbf{LO 5.4:} Mẫu chuyển đổi cột (Column Transformation).
    \item \textbf{LO 5.5:} Mẫu chuyển đổi bảng (Table Transformation).
    \item \textbf{LO 5.6:} Mẫu chuyển đổi mô hình dữ liệu.
    \item \textbf{LO 5.7:} Mẫu tải dữ liệu.
\end{itemize}""",
    },
    {
        "type": "normal",
        "title": "5.1 Quá trình Định hình Dữ liệu (Data Profiling)",
        "content": r"""\begin{itemize}
    \item \textbf{Data Profiling là gì?} Là bước khảo sát đầu tiên để hiểu rõ dữ liệu trước khi xử lý. Giống như việc "khám sức khỏe tổng quát" cho dữ liệu.
    \item \textbf{Hai bước định hình chính:}
    \begin{itemize}
        \item \textit{Điều tra chất lượng (Investigate Quality):} Tìm các giá trị bị thiếu (Missing), bất thường (Anomalies), hoặc sai định dạng.
        \item \textit{Điều tra cấu trúc (Investigate Structure):} Hiểu cách các cột (trường) và hàng (bản ghi) được tổ chức.
    \end{itemize}
    \item \textbf{Quyết định \& Thông báo:} Khi phát hiện lỗi nghiêm trọng, cần quyết định loại bỏ/sửa chữa dữ liệu và thông báo cho các bên liên quan.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.1",
        "image": "ILLUSTRATION 5.1.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.1A",
        "image": "ILLUSTRATION 5.1A.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.2",
        "image": "ILLUSTRATION 5.2.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.3",
        "image": "ILLUSTRATION 5.3.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.4",
        "image": "ILLUSTRATION 5.4.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.5",
        "image": "ILLUSTRATION 5.5.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.6",
        "image": "ILLUSTRATION 5.6.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.7",
        "image": "ILLUSTRATION 5.7.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.8",
        "image": "ILLUSTRATION 5.8.png",
    },
    {
        "type": "normal",
        "title": "5.2 Mô tả quá trình ETL (Extract, Transform, Load)",
        "content": r"""\begin{itemize}
    \item \textbf{E - Extract (Trích xuất):} Kéo dữ liệu từ các hệ thống nguồn (ERP, CRM, Web). Dữ liệu này thường ở dạng thô và chưa sẵn sàng để phân tích.
    \item \textbf{T - Transform (Chuyển đổi):} Là khâu quan trọng nhất. Làm sạch, tính toán lại, định dạng lại để dữ liệu phù hợp với mô hình phân tích mục tiêu.
    \item \textbf{L - Load (Tải):} Đưa dữ liệu đã được làm sạch vào kho dữ liệu (Data Warehouse) hoặc phần mềm trực quan hóa (Power BI, Tableau).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.9",
        "image": "ILLUSTRATION 5.9.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.10",
        "image": "ILLUSTRATION 5.10.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.11",
        "image": "ILLUSTRATION 5.11.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.12",
        "image": "ILLUSTRATION 5.12.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.13A",
        "image": "ILLUSTRATION 5.13A.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.13B",
        "image": "ILLUSTRATION 5.13B.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.14",
        "image": "ILLUSTRATION 5.14.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.15",
        "image": "ILLUSTRATION 5.15.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.16",
        "image": "ILLUSTRATION 5.16.png",
    },
    {
        "type": "normal",
        "title": "5.3 Áp dụng các mẫu để Trích xuất Dữ liệu (Extraction Patterns)",
        "content": r"""\begin{itemize}
    \item \textbf{Mẫu trích xuất toàn bộ (Full Extraction):} 
    \begin{itemize}
        \item Rút toàn bộ dữ liệu từ nguồn ở mỗi lần thực hiện. Phù hợp với các bảng dữ liệu nhỏ (Ví dụ: Danh mục khách hàng).
    \end{itemize}
    \item \textbf{Mẫu trích xuất tăng dần (Incremental Extraction):}
    \begin{itemize}
        \item Chỉ trích xuất những dữ liệu mới được tạo hoặc bị thay đổi kể từ lần trích xuất cuối cùng. Giúp tiết kiệm băng thông và tài nguyên hệ thống (Ví dụ: Dữ liệu giao dịch bán hàng hàng ngày).
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.17",
        "image": "ILLUSTRATION 5.17.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.18",
        "image": "ILLUSTRATION 5.18.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.19",
        "image": "ILLUSTRATION 5.19.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.20",
        "image": "ILLUSTRATION 5.20.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.21",
        "image": "ILLUSTRATION 5.21.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.22",
        "image": "ILLUSTRATION 5.22.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.23",
        "image": "ILLUSTRATION 5.23.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.24",
        "image": "ILLUSTRATION 5.24.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.25",
        "image": "ILLUSTRATION 5.25.png",
    },
    {
        "type": "normal",
        "title": "5.4 Áp dụng mẫu để Chuyển đổi Cột (Column Transformation)",
        "content": r"""\begin{itemize}
    \item \textbf{1. Làm sạch (Cleaning):} Xóa khoảng trắng thừa (Trim), sửa lỗi chính tả.
    \item \textbf{2. Định dạng (Formatting):} Đổi định dạng tiền tệ (VND sang USD), định dạng ngày tháng (MM/DD/YYYY sang DD/MM/YYYY).
    \item \textbf{3. Tách cột (Splitting):} Tách cột "Họ và Tên" thành hai cột "Họ" và "Tên".
    \item \textbf{4. Ghép cột (Concatenating):} Nối "Mã vùng" và "Số điện thoại".
    \item \textbf{5. Rút trích (Extracting):} Lấy tên miền từ địa chỉ Email.
    \item \textbf{6. Tính toán (Calculated):} Cột "Thành tiền" = "Số lượng" $\times$ "Đơn giá".
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.26",
        "image": "ILLUSTRATION 5.26.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.27",
        "image": "ILLUSTRATION 5.27.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.28",
        "image": "ILLUSTRATION 5.28.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.29",
        "image": "ILLUSTRATION 5.29.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.30",
        "image": "ILLUSTRATION 5.30.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.32",
        "image": "ILLUSTRATION 5.32.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.33",
        "image": "ILLUSTRATION 5.33.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.34",
        "image": "ILLUSTRATION 5.34.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.35",
        "image": "ILLUSTRATION 5.35.png",
    },
    {
        "type": "normal",
        "title": "5.5 Áp dụng mẫu để Chuyển đổi Bảng (Table Transformation)",
        "content": r"""\begin{itemize}
    \item \textbf{1. Lọc (Filtering):} Giữ lại các hàng thỏa mãn điều kiện (Ví dụ: Chỉ lấy doanh thu $> 1000$ USD).
    \item \textbf{2. Sắp xếp (Sorting):} Sắp xếp bảng theo thứ tự (Ví dụ: Bán chạy nhất lên đầu).
    \item \textbf{3. Gộp bảng theo cột (Join/Merge):} Kết hợp bảng "Hóa đơn" và "Khách hàng" dựa trên khóa chung (Mã KH).
    \item \textbf{4. Nối bảng theo hàng (Append/Union):} Nối dữ liệu bán hàng tháng 1 và tháng 2 vào chung một bảng (Phải có cùng số lượng cột và kiểu dữ liệu).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.36",
        "image": "ILLUSTRATION 5.36.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.37",
        "image": "ILLUSTRATION 5.37.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.38",
        "image": "ILLUSTRATION 5.38.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.39",
        "image": "ILLUSTRATION 5.39.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.40",
        "image": "ILLUSTRATION 5.40.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.41",
        "image": "ILLUSTRATION 5.41.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.42",
        "image": "ILLUSTRATION 5.42.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.42_1",
        "image": "ILLUSTRATION 5.42_1.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.43",
        "image": "ILLUSTRATION 5.43.png",
    },
    {
        "type": "normal",
        "title": "5.6 Áp dụng mẫu để Chuyển đổi Mô hình (Model Transformation)",
        "content": r"""\begin{itemize}
    \item \textbf{Tổ chức Schema:} Từ nhiều bảng rời rạc, liên kết chúng lại thành một mô hình thống nhất để phân tích.
    \item \textbf{Star Schema (Mô hình Ngôi sao):} Gồm 1 Bảng Sự kiện (Fact Table) ở giữa chứa dữ liệu giao dịch, và các Bảng Danh mục (Dimension Tables) xung quanh. Tối ưu cho tốc độ truy vấn.
    \item \textbf{Snowflake Schema (Mô hình Bông tuyết):} Giống Star Schema nhưng các Bảng Danh mục được chuẩn hóa (chia nhỏ) tiếp. Tiết kiệm không gian lưu trữ nhưng làm chậm tốc độ phân tích.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.43_1",
        "image": "ILLUSTRATION 5.43_1.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.44",
        "image": "ILLUSTRATION 5.44.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.45",
        "image": "ILLUSTRATION 5.45.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.46",
        "image": "ILLUSTRATION 5.46.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.47",
        "image": "ILLUSTRATION 5.47.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.48",
        "image": "ILLUSTRATION 5.48.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.49",
        "image": "ILLUSTRATION 5.49.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.50",
        "image": "ILLUSTRATION 5.50.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.51",
        "image": "ILLUSTRATION 5.51.png",
    },
    {
        "type": "normal",
        "title": "5.7 Áp dụng mẫu cho vấn đề Tải Dữ liệu (Data Loading)",
        "content": r"""\begin{itemize}
    \item \textbf{Tải ban đầu (Initial Load):} Nạp toàn bộ dữ liệu lịch sử vào một Data Warehouse mới tinh. Thường tốn nhiều thời gian.
    \item \textbf{Tải tăng dần (Incremental Load):} Chỉ nạp những giao dịch mới phát sinh, chạy định kỳ hàng ngày/hàng giờ.
    \item \textbf{Tải làm mới (Full Refresh):} Xóa toàn bộ dữ liệu cũ và nạp lại toàn bộ dữ liệu mới. Chỉ dùng cho các bảng nhỏ và ít thay đổi.
    \item \textbf{Kiểm tra tính toàn vẹn (Integrity Checks):} Phải đảm bảo số dòng của bảng Nguồn (Source) khớp với bảng Đích (Destination) sau khi tải.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.52",
        "image": "ILLUSTRATION 5.52.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.53",
        "image": "ILLUSTRATION 5.53.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.54",
        "image": "ILLUSTRATION 5.54.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.55",
        "image": "ILLUSTRATION 5.55.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.56",
        "image": "ILLUSTRATION 5.56.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.57",
        "image": "ILLUSTRATION 5.57.png",
    },
    {
        "type": "normal",
        "title": "Các Tình huống Apply It",
        "content": r"""\begin{center}
    \Huge \textbf{Apply It}
\end{center}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.58",
        "image": "ILLUSTRATION 5.58.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.59",
        "image": "ILLUSTRATION 5.59.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.60",
        "image": "ILLUSTRATION 5.60.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.61",
        "image": "ILLUSTRATION 5.61.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 5.62",
        "image": "ILLUSTRATION 5.62.png",
    },
    {
        "type": "image",
        "title": "Apply It 5.1",
        "image": "Apply It 5.1.png",
    },
    {
        "type": "image",
        "title": "Apply It 5.2",
        "image": "Apply It 5.2.png",
    },
    {
        "type": "image",
        "title": "Apply It 5.3",
        "image": "Apply It 5.3.png",
    },
    {
        "type": "image",
        "title": "Apply It 5.5",
        "image": "Apply It 5.5.png",
    },
    {
        "type": "image",
        "title": "Apply It 5.6",
        "image": "Apply It 5.6.png",
    },
    {
        "type": "image",
        "title": "Apply It 5.7",
        "image": "Apply It 5.7.png",
    },
    {
        "type": "normal",
        "title": "Phần Bài tập Ngắn (Brief Exercises)",
        "content": r"""\begin{center}
    \Huge \textbf{Brief Exercises}
\end{center}""",
    },
    {
        "type": "double_image",
        "title": "BE 5.1 & BE 5.2",
        "image1": "BE 5.1.png",
        "image2": "BE 5.2.png",
    },
    {
        "type": "double_image",
        "title": "BE 5.3 & BE 5.4",
        "image1": "BE 5.3.png",
        "image2": "BE 5.4.png",
    },
    {
        "type": "double_image",
        "title": "BE 5.5 & BE 5.6",
        "image1": "BE 5.5.png",
        "image2": "BE 5.6.png",
    },
    {
        "type": "double_image",
        "title": "BE 5.13 & BE 5.15",
        "image1": "BE 5.13.png",
        "image2": "BE 5.15.png",
    },
    {
        "type": "image",
        "title": "BE 5.16",
        "image": "BE 5.16.png",
    },
    {
        "type": "normal",
        "title": "Phần Bài tập (Exercises)",
        "content": r"""\begin{center}
    \Huge \textbf{Exercises}
\end{center}""",
    },
    {
        "type": "double_image",
        "title": "EX 5.2 & EX 5.3",
        "image1": "EX 5.2.png",
        "image2": "EX 5.3.png",
    },
    {
        "type": "double_image",
        "title": "EX 5.6 & EX 5.7",
        "image1": "EX 5.6.png",
        "image2": "EX 5.7.png",
    },
    {
        "type": "image",
        "title": "EX 5.8",
        "image": "EX 5.8.png",
    },
    {
        "type": "normal",
        "title": "Tình Huống Ứng Dụng Chuyên Môn (PAC)",
        "content": r"""\begin{center}
    \Huge \textbf{Professional Application Cases (PAC)}
\end{center}""",
    },
    {
        "type": "double_image",
        "title": "PAC 5.1 & PAC 5.2",
        "image1": "PAC 5.1.png",
        "image2": "PAC 5.2.png",
    },
    {
        "type": "double_image",
        "title": "PAC 5.3 & PAC 5.4A",
        "image1": "PAC 5.3.png",
        "image2": "PAC 5.4A.png",
    },
    {
        "type": "double_image",
        "title": "PAC 5.4B & PAC 5.4A_1",
        "image1": "PAC 5.4B.png",
        "image2": "PAC 5.4A_1.png",
    },
    {
        "type": "normal",
        "title": "Tóm tắt Mục tiêu Học tập Chương 5",
        "content": r"""\begin{itemize}
    \item \textbf{LO 5.1:} Data Profiling giúp xác định "sức khỏe" dữ liệu trước khi xử lý.
    \item \textbf{LO 5.2:} Nắm vững vai trò của từng bước trong quá trình ETL.
    \item \textbf{LO 5.3 \& 5.7:} Sử dụng đúng mẫu Trích xuất (Full/Incremental) và mẫu Tải (Refresh/Incremental) để tối ưu hiệu suất.
    \item \textbf{LO 5.4 - 5.6:} Áp dụng thành thạo các kỹ thuật chuyển đổi Cột (Clean, Split), Bảng (Join, Append), và xây dựng Mô hình dữ liệu chuẩn (Star Schema).
\end{itemize}""",
    },
]
