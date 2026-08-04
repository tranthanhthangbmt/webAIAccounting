chapter_title = 'Mô hình hóa Thông tin'
chapter_subtitle = 'Analysis: Information Modeling'

slides = [
    {
        "type": "title_slide",
    },
    {
        "type": "normal",
        "title": "Góc nhìn Chuyên gia (Professional Insight)",
        "content": r"""\begin{itemize}
    \item \textbf{Mô hình hóa Thông tin:} Không chỉ đơn giản là việc liên kết các bảng dữ liệu, mà là nghệ thuật cấu trúc hóa dữ liệu để trả lời chính xác các câu hỏi kinh doanh.
    \item \textbf{Khả năng mở rộng (Scalability):} Một mô hình dữ liệu tốt (ví dụ: Star Schema) cho phép báo cáo chạy nhanh hơn, dễ bảo trì hơn và hạn chế rủi ro sai lệch dữ liệu.
    \item \textbf{Tư duy Hệ thống:} Kế toán viên hiện đại cần tư duy giống như một Data Architect để xây dựng nền tảng vững chắc cho mọi phân tích phía sau.
\end{itemize}""",
    },
    {
        "type": "normal",
        "title": "Lộ trình Chương (Chapter Roadmap)",
        "content": r"""\begin{itemize}
    \item \textbf{LO 6.1:} Khái niệm Nền tảng của Mô hình hóa Thông tin.
    \item \textbf{LO 6.2:} Áp dụng Các Thuật toán Mô hình hóa Thông tin (7 Mẫu cơ bản).
    \item \textbf{LO 6.3:} Sáu Mẫu Mô hình hóa cho Cấu trúc Dữ liệu Kế toán (Star Schema).
\end{itemize}""",
    },
    {
        "type": "normal",
        "title": "6.1 Mô hình hóa Thông tin là gì?",
        "content": r"""\begin{itemize}
    \item \textbf{Định nghĩa:} Là quá trình cấu trúc và sắp xếp lại dữ liệu thô thành thông tin có ý nghĩa thông qua các thuật toán và mối quan hệ giữa các bảng.
    \item \textbf{Quy trình Mô hình hóa (The Information Modeling Process):} Chuyển từ Dữ liệu (Data) $\rightarrow$ Thuật toán (Algorithms) $\rightarrow$ Thông tin (Information).
    \item \textbf{Mục tiêu:} Đảm bảo tính toàn vẹn, tính nhất quán và dễ dàng truy xuất thông tin phục vụ cho Bảng điều khiển (Dashboards) và Báo cáo.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.1",
        "image": "ILLUSTRATION 6.1.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.2",
        "image": "ILLUSTRATION 6.2.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.3",
        "image": "ILLUSTRATION 6.3.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.4",
        "image": "ILLUSTRATION 6.4.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.5",
        "image": "ILLUSTRATION 6.5.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.6",
        "image": "ILLUSTRATION 6.6.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.7",
        "image": "ILLUSTRATION 6.7.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.8",
        "image": "ILLUSTRATION 6.8.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.9",
        "image": "ILLUSTRATION 6.9.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.10",
        "image": "ILLUSTRATION 6.10.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.11",
        "image": "ILLUSTRATION 6.11.png",
    },
    {
        "type": "normal",
        "title": "Thuật toán và Phương pháp tiếp cận",
        "content": r"""\begin{itemize}
    \item \textbf{Thuật toán (Algorithms):} Là tập hợp các quy tắc tính toán (ví dụ: Tính biên lợi nhuận = Doanh thu - Giá vốn).
    \item \textbf{Phương pháp tiếp cận có cấu trúc (Structured Approach):} 
    \begin{itemize}
        \item Hiểu rõ yêu cầu đầu ra (Output).
        \item Xác định dữ liệu đầu vào (Input).
        \item Xây dựng các bước xử lý logic (Processing).
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.12",
        "image": "ILLUSTRATION 6.12.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.13",
        "image": "ILLUSTRATION 6.13.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.14",
        "image": "ILLUSTRATION 6.14.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.15",
        "image": "ILLUSTRATION 6.15.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.16",
        "image": "ILLUSTRATION 6.16.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.17",
        "image": "ILLUSTRATION 6.17.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.18",
        "image": "ILLUSTRATION 6.18.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.19",
        "image": "ILLUSTRATION 6.19.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.20",
        "image": "ILLUSTRATION 6.20.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.21",
        "image": "ILLUSTRATION 6.21.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.22",
        "image": "ILLUSTRATION 6.22.png",
    },
    {
        "type": "normal",
        "title": "6.2 Bảy Mẫu Thuật toán Mô hình hóa Thông tin",
        "content": r"""\begin{itemize}
    \item \textbf{Mẫu 1 - Tính toán Cơ bản:} Cộng, trừ, nhân, chia (ví dụ: Tổng Doanh thu).
    \item \textbf{Mẫu 2 - Logic và Điều kiện (Logic/Conditional):} Hàm IF, CASE WHEN (ví dụ: Phân loại Nợ xấu nếu quá hạn 90 ngày).
    \item \textbf{Mẫu 3 - Xử lý Văn bản (Text):} Nối chuỗi, tách chuỗi, làm sạch văn bản (ví dụ: Tách Mã Vùng từ Số Điện thoại).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.23",
        "image": "ILLUSTRATION 6.23.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.24",
        "image": "ILLUSTRATION 6.24.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.25",
        "image": "ILLUSTRATION 6.25.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.26",
        "image": "ILLUSTRATION 6.26.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.27",
        "image": "ILLUSTRATION 6.27.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.28",
        "image": "ILLUSTRATION 6.28.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.29",
        "image": "ILLUSTRATION 6.29.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.30",
        "image": "ILLUSTRATION 6.30.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.31",
        "image": "ILLUSTRATION 6.31.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.32",
        "image": "ILLUSTRATION 6.32.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.33",
        "image": "ILLUSTRATION 6.33.png",
    },
    {
        "type": "normal",
        "title": "Các Mẫu Thuật toán tiếp theo",
        "content": r"""\begin{itemize}
    \item \textbf{Mẫu 4 - Thời gian (Date/Time):} Trích xuất Tháng, Năm, Quý (ví dụ: Doanh thu theo Quý).
    \item \textbf{Mẫu 5 - Hàm Tài chính (Financial):} Tính PV, FV, NPV, IRR.
    \item \textbf{Mẫu 6 - Tỷ suất (Ratios):} Tính ROA, ROE, Current Ratio.
    \item \textbf{Mẫu 7 - Hàm Phức hợp (Complex/Nested):} Kết hợp nhiều hàm với nhau.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.34",
        "image": "ILLUSTRATION 6.34.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.35",
        "image": "ILLUSTRATION 6.35.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.36",
        "image": "ILLUSTRATION 6.36.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.37",
        "image": "ILLUSTRATION 6.37.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.38",
        "image": "ILLUSTRATION 6.38.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.39",
        "image": "ILLUSTRATION 6.39.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.40",
        "image": "ILLUSTRATION 6.40.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.41",
        "image": "ILLUSTRATION 6.41.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.42",
        "image": "ILLUSTRATION 6.42.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.43",
        "image": "ILLUSTRATION 6.43.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.44",
        "image": "ILLUSTRATION 6.44.png",
    },
    {
        "type": "normal",
        "title": "6.3 Sáu Mẫu Cấu trúc Dữ liệu Kế toán",
        "content": r"""\begin{itemize}
    \item \textbf{Mẫu 1 - Hệ thống Tài khoản (Chart of Accounts):} Bảng danh mục cốt lõi của mọi hệ thống kế toán.
    \item \textbf{Mẫu 2 - Dữ liệu Giao dịch (Transactions):} Bảng Fact chứa các bút toán nhật ký (Sổ cái).
    \item \textbf{Mẫu 3 - Danh mục Thực thể (Entity/Master Data):} Khách hàng, Nhà cung cấp, Sản phẩm, Nhân viên.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.45",
        "image": "ILLUSTRATION 6.45.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.46",
        "image": "ILLUSTRATION 6.46.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.47",
        "image": "ILLUSTRATION 6.47.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.48",
        "image": "ILLUSTRATION 6.48.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.49",
        "image": "ILLUSTRATION 6.49.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.50",
        "image": "ILLUSTRATION 6.50.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.51",
        "image": "ILLUSTRATION 6.51.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.52",
        "image": "ILLUSTRATION 6.52.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.53",
        "image": "ILLUSTRATION 6.53.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.54",
        "image": "ILLUSTRATION 6.54.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.55",
        "image": "ILLUSTRATION 6.55.png",
    },
    {
        "type": "normal",
        "title": "Cấu trúc Dữ liệu (Tiếp theo)",
        "content": r"""\begin{itemize}
    \item \textbf{Mẫu 4 - Ngân sách so với Thực tế (Budget vs Actual):} Kết nối bảng kế hoạch và bảng thực tế để phân tích chênh lệch (Variance Analysis).
    \item \textbf{Mẫu 5 - Bảng Thời gian (Time Dimension):} Cực kỳ quan trọng để phân tích xu hướng (Time Intelligence) trong Power BI / Tableau.
    \item \textbf{Mẫu 6 - Sổ cái và Sổ chi tiết (General \& Subsidiary Ledgers):} Mối quan hệ 1-N (One-to-Many) giữa Sổ cái tổng hợp và các Sổ chi tiết (Phải thu, Phải trả, Hàng tồn kho).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.56",
        "image": "ILLUSTRATION 6.56.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.57",
        "image": "ILLUSTRATION 6.57.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.58",
        "image": "ILLUSTRATION 6.58.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.59",
        "image": "ILLUSTRATION 6.59.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.60",
        "image": "ILLUSTRATION 6.60.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.61A",
        "image": "ILLUSTRATION 6.61A.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.61B",
        "image": "ILLUSTRATION 6.61B.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.62",
        "image": "ILLUSTRATION 6.62.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.63",
        "image": "ILLUSTRATION 6.63.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.64",
        "image": "ILLUSTRATION 6.64.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 6.65",
        "image": "ILLUSTRATION 6.65.png",
    },
    {
        "type": "normal",
        "title": "Bài tập Ngắn (Brief Exercises)",
        "content": r"""\begin{center}
    \Huge \textbf{Phần Bài tập Ngắn} \\
    \vspace{0.5cm}
    \Large Brief Exercises (BE)
\end{center}""",
    },
    {
        "type": "double_image",
        "title": "BE 6.5 & BE 6.11",
        "image1": "BE 6.5.png",
        "image2": "BE 6.11.png",
    },
    {
        "type": "double_image",
        "title": "BE 6.12 & BE 6.14",
        "image1": "BE 6.12.png",
        "image2": "BE 6.14.png",
    },
    {
        "type": "image",
        "title": "BE 6.15",
        "image": "BE 6.15.png",
    },
    {
        "type": "normal",
        "title": "Bài tập (Exercises)",
        "content": r"""\begin{center}
    \Huge \textbf{Phần Bài tập} \\
    \vspace{0.5cm}
    \Large Exercises (EX)
\end{center}""",
    },
    {
        "type": "double_image",
        "title": "EX 6.2 & EX 6.3",
        "image1": "EX 6.2.png",
        "image2": "EX 6.3.png",
    },
    {
        "type": "double_image",
        "title": "EX 6.4A & EX 6.4B",
        "image1": "EX 6.4A.png",
        "image2": "EX 6.4B.png",
    },
    {
        "type": "double_image",
        "title": "EX 6.5 & EX 6.5_1",
        "image1": "EX 6.5.png",
        "image2": "EX 6.5_1.png",
    },
    {
        "type": "double_image",
        "title": "EX 6.7A & EX 6.7B",
        "image1": "EX 6.7A.png",
        "image2": "EX 6.7B.png",
    },
    {
        "type": "double_image",
        "title": "EX 6.9 & EX 6.10",
        "image1": "EX 6.9.png",
        "image2": "EX 6.10.png",
    },
    {
        "type": "double_image",
        "title": "EX 6.11A & EX 6.11B",
        "image1": "EX 6.11A.png",
        "image2": "EX 6.11B.png",
    },
    {
        "type": "double_image",
        "title": "EX 6.12 & EX 6.13A",
        "image1": "EX 6.12.png",
        "image2": "EX 6.13A.png",
    },
    {
        "type": "image",
        "title": "EX 6.13B",
        "image": "EX 6.13B.png",
    },
    {
        "type": "normal",
        "title": "Tình huống Ứng dụng (PAC)",
        "content": r"""\begin{center}
    \Huge \textbf{Tình huống Ứng dụng Chuyên môn} \\
    \vspace{0.5cm}
    \Large Professional Application Cases (PAC)
\end{center}""",
    },
    {
        "type": "double_image",
        "title": "PAC 6.1 & PAC 6.4",
        "image1": "PAC 6.1.png",
        "image2": "PAC 6.4.png",
    },
    {
        "type": "image",
        "title": "LO 1.4",
        "image": "LO 1.4.png",
    },
    {
        "type": "image",
        "title": "LO 1.5",
        "image": "LO 1.5.png",
    },
    {
        "type": "image",
        "title": "LO 1.7",
        "image": "LO 1.7.png",
    },
    {
        "type": "image",
        "title": "LO 1.9",
        "image": "LO 1.9.png",
    },
    {
        "type": "image",
        "title": "LO 3.13",
        "image": "LO 3.13.png",
    },
    {
        "type": "image",
        "title": "LO 3.17",
        "image": "LO 3.17.png",
    },
    {
        "type": "image",
        "title": "LO 3.17_1",
        "image": "LO 3.17_1.png",
    },
    {
        "type": "image",
        "title": "LO 3.18",
        "image": "LO 3.18.png",
    },
    {
        "type": "image",
        "title": "LO 3.19",
        "image": "LO 3.19.png",
    },
    {
        "type": "image",
        "title": "LO 3.21",
        "image": "LO 3.21.png",
    },
    {
        "type": "image",
        "title": "DTunes data dictionary 6.0",
        "image": "DTunes data dictionary 6.0.png",
    },
    {
        "type": "image",
        "title": "Fig 6.0",
        "image": "Fig 6.0.png",
    },
    {
        "type": "image",
        "title": "Apply It 6.1",
        "image": "Apply It 6.1.png",
    },
    {
        "type": "image",
        "title": "DTunes data dictionary 6.1",
        "image": "DTunes data dictionary 6.1.png",
    },
    {
        "type": "image",
        "title": "Apply It 6.2",
        "image": "Apply It 6.2.png",
    },
    {
        "type": "image",
        "title": "Apply It 6.3",
        "image": "Apply It 6.3.png",
    },
]
