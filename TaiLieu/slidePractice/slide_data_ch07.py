chapter_title = 'Khám phá Dữ liệu'
chapter_subtitle = 'Analysis: Data Exploration'

slides = [
    {
        "type": "title_slide",
    },
    {
        "type": "normal",
        "title": "Góc nhìn Chuyên gia (Professional Insight)",
        "content": r"""\begin{itemize}
    \item \textbf{Tầm quan trọng:} Khám phá dữ liệu là bước đầu tiên để "làm quen" với dữ liệu. Kế toán viên cần hiểu rõ dữ liệu của mình trước khi đưa ra bất kỳ kết luận hay báo cáo nào.
    \item \textbf{Trực giác Kế toán:} Kết hợp kinh nghiệm thực tiễn và kỹ năng phân tích để phát hiện ra các điểm bất thường, xu hướng hoặc insight tiềm ẩn.
    \item \textbf{Kể chuyện bằng dữ liệu (Data Storytelling):} Một biểu đồ trực quan tốt có giá trị hơn hàng ngàn con số trong bảng tính phức tạp.
\end{itemize}""",
    },
    {
        "type": "normal",
        "title": "Lộ trình Chương (Chapter Roadmap)",
        "content": r"""\begin{itemize}
    \item \textbf{LO 7.1:} Quy trình Khám phá Dữ liệu.
    \item \textbf{LO 7.2:} Khám phá Mối quan hệ Nền tảng qua 8 Mẫu Trực quan hóa.
    \item \textbf{LO 7.3:} Khám phá Dữ liệu bằng cách Tích hợp Mối quan hệ (Dashboards).
\end{itemize}""",
    },
    {
        "type": "normal",
        "title": "7.1 Khám phá Dữ liệu (Data Exploration) là gì?",
        "content": r"""\begin{itemize}
    \item \textbf{Định nghĩa:} Là quá trình phân tích dữ liệu ban đầu bằng các công cụ trực quan và thống kê để hiểu rõ đặc điểm, phát hiện xu hướng và kiểm tra các giả định.
    \item \textbf{Sự khác biệt:}
    \begin{itemize}
        \item \textbf{Khám phá (Exploration):} Tự do tìm kiếm insight (cho chính bạn).
        \item \textbf{Diễn giải (Interpretation):} Hiểu ý nghĩa của insight.
        \item \textbf{Báo cáo (Reporting):} Trình bày insight cho người khác (Management/Stakeholders).
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.1",
        "image": "ILLUSTRATION 7.1.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.2",
        "image": "ILLUSTRATION 7.2.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.3",
        "image": "ILLUSTRATION 7.3.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.4",
        "image": "ILLUSTRATION 7.4.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.5",
        "image": "ILLUSTRATION 7.5.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.6",
        "image": "ILLUSTRATION 7.6.png",
    },
    {
        "type": "normal",
        "title": "Quy trình Khám phá Dữ liệu",
        "content": r"""\begin{itemize}
    \item \textbf{Bước 1: Xác định Mục tiêu (Identify Objectives):} Bạn đang tìm kiếm điều gì?
    \item \textbf{Bước 2: Lựa chọn Biến (Select Variables):} Dữ liệu nào cần thiết?
    \item \textbf{Bước 3: Khám phá Trực quan (Visual Exploration):} Sử dụng biểu đồ.
    \item \textbf{Bước 4: Đánh giá \& Tinh chỉnh (Evaluate \& Refine):} Biểu đồ có ý nghĩa không? Có cần thay đổi không?
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.7",
        "image": "ILLUSTRATION 7.7.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.8",
        "image": "ILLUSTRATION 7.8.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.9",
        "image": "ILLUSTRATION 7.9.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.10",
        "image": "ILLUSTRATION 7.10.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.11",
        "image": "ILLUSTRATION 7.11.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.12",
        "image": "ILLUSTRATION 7.12.png",
    },
    {
        "type": "normal",
        "title": "Công cụ Khám phá Dữ liệu",
        "content": r"""\begin{itemize}
    \item \textbf{PivotTables trong Excel:} Công cụ cơ bản, nhanh chóng và phổ biến nhất để nhóm, tóm tắt và lọc dữ liệu.
    \item \textbf{Đa nền tảng (Across Tools):} Các công cụ BI hiện đại (Power BI, Tableau) cung cấp khả năng trực quan hóa mạnh mẽ hơn, hỗ trợ tương tác và xử lý dữ liệu lớn (Big Data).
    \item \textbf{Mục tiêu cốt lõi:} Tìm ra các \textit{Insights} ẩn giấu đằng sau những con số tài chính khô khan.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.13",
        "image": "ILLUSTRATION 7.13.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.14",
        "image": "ILLUSTRATION 7.14.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.15",
        "image": "ILLUSTRATION 7.15.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.16",
        "image": "ILLUSTRATION 7.16.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.17",
        "image": "ILLUSTRATION 7.17.png",
    },
    {
        "type": "normal",
        "title": "7.2 Mối quan hệ Nền tảng qua Trực quan hóa",
        "content": r"""\begin{itemize}
    \item \textbf{Mục đích:} Giúp não bộ con người nhanh chóng nhận diện quy luật (Pattern Recognition).
    \item \textbf{8 Mẫu Mối quan hệ Nền tảng (Eight Patterns):}
    \begin{enumerate}
        \item Phần-Toàn thể (Part-To-Whole)
        \item So sánh Cường độ (Magnitude)
        \item Chuỗi Thời gian (Time Series)
        \item Phân phối (Distribution)
        \item ... và 4 mẫu nâng cao khác.
    \end{enumerate}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.18",
        "image": "ILLUSTRATION 7.18.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.19",
        "image": "ILLUSTRATION 7.19.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.20",
        "image": "ILLUSTRATION 7.20.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.21",
        "image": "ILLUSTRATION 7.21.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.22",
        "image": "ILLUSTRATION 7.22.png",
    },
    {
        "type": "normal",
        "title": "Phân tích Các Mẫu Cơ bản",
        "content": r"""\begin{itemize}
    \item \textbf{Phần-Toàn thể (Part-To-Whole):} Biểu đồ tròn (Pie), Biểu đồ vành khăn (Donut), Treemap. Cho thấy tỷ trọng đóng góp (Ví dụ: Tỷ trọng doanh thu theo từng sản phẩm).
    \item \textbf{Cường độ (Magnitude):} Biểu đồ cột (Bar/Column). Dùng để so sánh trực diện kích thước, quy mô giữa các hạng mục.
    \item \textbf{Chuỗi Thời gian (Time Series):} Biểu đồ đường (Line). Thể hiện xu hướng biến động qua thời gian (Tháng, Quý, Năm).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.23",
        "image": "ILLUSTRATION 7.23.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.24",
        "image": "ILLUSTRATION 7.24.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.25",
        "image": "ILLUSTRATION 7.25.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.26",
        "image": "ILLUSTRATION 7.26.png",
    },
    {
        "type": "normal",
        "title": "Phân tích Các Mẫu Nâng cao",
        "content": r"""\begin{itemize}
    \item \textbf{Phân phối (Distribution):} Biểu đồ Histogram, Box-plot. Đánh giá sự phân tán của dữ liệu và phát hiện ngoại lai (Outliers).
    \item \textbf{Tương quan (Correlation):} Biểu đồ phân tán (Scatter plot). Kiểm tra mối liên hệ giữa hai biến (Ví dụ: Chi phí quảng cáo và Doanh thu).
    \item \textbf{Không gian/Địa lý (Spatial):} Bản đồ (Map). Hiển thị dữ liệu theo vị trí địa lý (Ví dụ: Doanh số theo Tỉnh/Thành phố).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.27",
        "image": "ILLUSTRATION 7.27.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.28",
        "image": "ILLUSTRATION 7.28.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.29",
        "image": "ILLUSTRATION 7.29.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.30",
        "image": "ILLUSTRATION 7.30.png",
    },
    {
        "type": "normal",
        "title": "Nguyên tắc Thiết kế Biểu đồ",
        "content": r"""\begin{itemize}
    \item \textbf{Giữ sự đơn giản (Keep it Simple):} Tránh lạm dụng 3D, bóng đổ hoặc màu sắc lòe loẹt gây xao nhãng (Chartjunk).
    \item \textbf{Rõ ràng (Clarity):} Trục tọa độ, nhãn dữ liệu (Data labels), và tiêu đề phải dễ đọc và mang tính mô tả.
    \item \textbf{Sử dụng Màu sắc có chủ ý:} Dùng màu đỏ cho sự giảm sút/rủi ro, màu xanh cho sự tăng trưởng.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.31",
        "image": "ILLUSTRATION 7.31.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.32",
        "image": "ILLUSTRATION 7.32.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.33",
        "image": "ILLUSTRATION 7.33.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.34",
        "image": "ILLUSTRATION 7.34.png",
    },
    {
        "type": "normal",
        "title": "7.3 Khám phá Dữ liệu Đa chiều (Tích hợp)",
        "content": r"""\begin{itemize}
    \item \textbf{Tích hợp Mối quan hệ:} Sử dụng kết hợp nhiều loại biểu đồ để có cái nhìn toàn diện hơn (Holistic view).
    \item \textbf{Hai mẫu trong một (Single Visualization):}
    \begin{itemize}
        \item Biểu đồ Đa trục (Dual-axis): So sánh hai chỉ số có thang đo khác nhau trên cùng một biểu đồ (ví dụ: Doanh thu - Cột, Tỷ suất LN - Đường).
        \item Biểu đồ Bong bóng (Bubble chart): Thể hiện 3 biến dữ liệu (Trục X, Trục Y, Độ lớn bong bóng).
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.35",
        "image": "ILLUSTRATION 7.35.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.36",
        "image": "ILLUSTRATION 7.36.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.37",
        "image": "ILLUSTRATION 7.37.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.38",
        "image": "ILLUSTRATION 7.38.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.39",
        "image": "ILLUSTRATION 7.39.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.40",
        "image": "ILLUSTRATION 7.40.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.41",
        "image": "ILLUSTRATION 7.41.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.42",
        "image": "ILLUSTRATION 7.42.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.43",
        "image": "ILLUSTRATION 7.43.png",
    },
    {
        "type": "normal",
        "title": "Bảng điều khiển (Dashboards)",
        "content": r"""\begin{itemize}
    \item \textbf{Dashboard là gì?} Là giao diện trực quan tổng hợp nhiều biểu đồ, chỉ số quan trọng (KPIs) trên cùng một màn hình.
    \item \textbf{Tính Tương tác (Interactivity):} Người dùng có thể click, lọc (Slicers), khoan sâu (Drill-down) để khám phá chi tiết (Ví dụ: Từ doanh thu Tổng Công ty khoan xuống từng Chi nhánh).
    \item \textbf{Giá trị Kế toán:} Giúp Ban Lãnh đạo ra quyết định nhanh chóng, dựa trên dữ liệu (Data-driven decision making).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.44",
        "image": "ILLUSTRATION 7.44.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.45",
        "image": "ILLUSTRATION 7.45.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.46",
        "image": "ILLUSTRATION 7.46.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.47",
        "image": "ILLUSTRATION 7.47.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.48",
        "image": "ILLUSTRATION 7.48.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.49",
        "image": "ILLUSTRATION 7.49.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.50",
        "image": "ILLUSTRATION 7.50.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.51",
        "image": "ILLUSTRATION 7.51.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 7.52",
        "image": "ILLUSTRATION 7.52.png",
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
        "title": "BE 7.6 & BE 7.7",
        "image1": "BE 7.6.png",
        "image2": "BE 7.7.png",
    },
    {
        "type": "double_image",
        "title": "BE 7.8 & BE 7.9",
        "image1": "BE 7.8.png",
        "image2": "BE 7.9.png",
    },
    {
        "type": "double_image",
        "title": "BE 7.10 & BE 7.11A",
        "image1": "BE 7.10.png",
        "image2": "BE 7.11A.png",
    },
    {
        "type": "double_image",
        "title": "BE 7.11B & BE 7.12A",
        "image1": "BE 7.11B.png",
        "image2": "BE 7.12A.png",
    },
    {
        "type": "image",
        "title": "BE 7.12B",
        "image": "BE 7.12B.png",
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
        "title": "EX 7.3 & EX 7.4",
        "image1": "EX 7.3.png",
        "image2": "EX 7.4.png",
    },
    {
        "type": "double_image",
        "title": "EX 7.5 & EX 7.6",
        "image1": "EX 7.5.png",
        "image2": "EX 7.6.png",
    },
    {
        "type": "double_image",
        "title": "EX 7.7 & EX 7.8",
        "image1": "EX 7.7.png",
        "image2": "EX 7.8.png",
    },
    {
        "type": "double_image",
        "title": "EX 7.9 & EX 7.10A",
        "image1": "EX 7.9.png",
        "image2": "EX 7.10A.png",
    },
    {
        "type": "double_image",
        "title": "EX 7.10B & EX 7.11",
        "image1": "EX 7.10B.png",
        "image2": "EX 7.11.png",
    },
    {
        "type": "double_image",
        "title": "EX 7.12 & EX 7.13",
        "image1": "EX 7.12.png",
        "image2": "EX 7.13.png",
    },
    {
        "type": "double_image",
        "title": "EX 7.14 & EX 7.15",
        "image1": "EX 7.14.png",
        "image2": "EX 7.15.png",
    },
    {
        "type": "image",
        "title": "LO 2.10",
        "image": "LO 2.10.png",
    },
    {
        "type": "image",
        "title": "LO 2.11",
        "image": "LO 2.11.png",
    },
    {
        "type": "image",
        "title": "LO 2.14",
        "image": "LO 2.14.png",
    },
    {
        "type": "image",
        "title": "LO 2.14_1",
        "image": "LO 2.14_1.png",
    },
    {
        "type": "image",
        "title": "LO 2.15",
        "image": "LO 2.15.png",
    },
    {
        "type": "image",
        "title": "LO 3.15",
        "image": "LO 3.15.png",
    },
    {
        "type": "image",
        "title": "LO 3.16",
        "image": "LO 3.16.png",
    },
    {
        "type": "image",
        "title": "LO 3.17",
        "image": "LO 3.17.png",
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
        "title": "LO 3.20A",
        "image": "LO 3.20A.png",
    },
    {
        "type": "image",
        "title": "LO 3.20B",
        "image": "LO 3.20B.png",
    },
    {
        "type": "image",
        "title": "LO 3.20C",
        "image": "LO 3.20C.png",
    },
    {
        "type": "image",
        "title": "LO 3.20A_1",
        "image": "LO 3.20A_1.png",
    },
    {
        "type": "image",
        "title": "LO 3.20A_2",
        "image": "LO 3.20A_2.png",
    },
    {
        "type": "image",
        "title": "Info 7.0",
        "image": "Info 7.0.png",
    },
    {
        "type": "image",
        "title": "Apply It 7.1A",
        "image": "Apply It 7.1A.png",
    },
    {
        "type": "image",
        "title": "Apply It 7.1B",
        "image": "Apply It 7.1B.png",
    },
    {
        "type": "image",
        "title": "Apply It 7.2",
        "image": "Apply It 7.2.png",
    },
    {
        "type": "image",
        "title": "Apply It 7.3A",
        "image": "Apply It 7.3A.png",
    },
    {
        "type": "image",
        "title": "Apply It 7.3B",
        "image": "Apply It 7.3B.png",
    },
    {
        "type": "image",
        "title": "Apply It 7.3A_1",
        "image": "Apply It 7.3A_1.png",
    },
    {
        "type": "image",
        "title": "Apply It 7.3A_2",
        "image": "Apply It 7.3A_2.png",
    },
    {
        "type": "image",
        "title": "NoTable 7.16",
        "image": "NoTable 7.16.png",
    },
]
