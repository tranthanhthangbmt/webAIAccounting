chapter_title = "CHƯƠNG 10"
chapter_subtitle = "Các Xu hướng Dữ liệu và Phân tích Mới nhất trong Kế toán"
slides = [
    {
        "type": "title_slide",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.1",
        "image": "ILLUSTRATION 10.1.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.2",
        "image": "ILLUSTRATION 10.2.png",
    },
    {
        "type": "normal",
        "title": "Chương 10: Các Xu hướng Dữ liệu và Phân tích Mới nhất",
        "content": r"""\begin{itemize}
    \item \textbf{Mục tiêu:} Khám phá tác động của công nghệ và phân tích dữ liệu tiên tiến đối với nghề kế toán.
    \item \textbf{Trọng tâm:} Hiểu các đặc tính của Big Data và sự chuyển dịch của các công nghệ lõi.
    \item \textbf{Cấu trúc:} Dữ liệu lớn (Big Data), Sự phát triển của công nghệ, Ứng dụng vào các lĩnh vực kế toán.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.3",
        "image": "ILLUSTRATION 10.3.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.4",
        "image": "ILLUSTRATION 10.4.png",
    },
    {
        "type": "normal",
        "title": "10.1 Đặc điểm của Dữ liệu lớn (5V của Big Data)",
        "content": r"""\begin{itemize}
    \item Sự bùng nổ dữ liệu yêu cầu thay đổi trong phương pháp phân tích.
    \item Mô hình 5V giải thích bản chất đa chiều của Dữ liệu lớn:
    \begin{itemize}
        \item Volume (Khối lượng)
        \item Variety (Đa dạng)
        \item Velocity (Tốc độ)
        \item Veracity (Tính xác thực)
        \item Value (Giá trị)
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.5",
        "image": "ILLUSTRATION 10.5.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.6",
        "image": "ILLUSTRATION 10.6.png",
    },
    {
        "type": "normal",
        "title": "Volume (Khối lượng) & Variety (Đa dạng)",
        "content": r"""\begin{itemize}
    \item \textbf{Volume:} Lượng dữ liệu vượt ra khỏi khả năng xử lý của Excel hoặc SQL thông thường. Được tính bằng Terabyte, Petabyte,...
    \item \textbf{Variety:}
    \begin{itemize}
        \item Dữ liệu có cấu trúc (Bảng tính, CSDL)
        \item Dữ liệu bán cấu trúc (XML, JSON, XBRL)
        \item Dữ liệu phi cấu trúc (Văn bản, Hình ảnh, Âm thanh) chiếm đến 80\% tổng lượng dữ liệu hiện nay.
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.7",
        "image": "ILLUSTRATION 10.7.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.8",
        "image": "ILLUSTRATION 10.8.png",
    },
    {
        "type": "normal",
        "title": "Velocity (Tốc độ) & Veracity (Tính xác thực)",
        "content": r"""\begin{itemize}
    \item \textbf{Velocity:} Tốc độ sinh ra và luân chuyển của dữ liệu. Doanh nghiệp cần xử lý dữ liệu theo thời gian thực (Real-time).
    \item \textbf{Veracity:} Mức độ đáng tin cậy. Dữ liệu từ mạng xã hội có thể bị nhiễu và sai lệch (bias), dẫn đến rủi ro ra quyết định sai lầm.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.9",
        "image": "ILLUSTRATION 10.9.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.10",
        "image": "ILLUSTRATION 10.10.png",
    },
    {
        "type": "normal",
        "title": "Value (Giá trị)",
        "content": r"""\begin{itemize}
    \item \textbf{Value:} Tất cả 4V trước đều vô nghĩa nếu không thể trích xuất ra insight có giá trị (Value) cho doanh nghiệp.
    \item Đối với kế toán, Value thể hiện ở khả năng:
    \begin{itemize}
        \item Dự báo dòng tiền chính xác hơn.
        \item Nhận diện gian lận nhanh hơn.
        \item Tiết kiệm chi phí vận hành.
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.11",
        "image": "ILLUSTRATION 10.11.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.12",
        "image": "ILLUSTRATION 10.12.png",
    },
    {
        "type": "normal",
        "title": "Đạo đức Dữ liệu (Data Ethics)",
        "content": r"""\begin{itemize}
    \item \textbf{Quyền riêng tư (Privacy):} Bảo mật thông tin nhận dạng cá nhân (PII) trong quá trình phân tích.
    \item \textbf{Tính minh bạch (Transparency):} Người dùng cần biết thuật toán AI đưa ra quyết định dựa trên điều gì.
    \item \textbf{Thiên lệch (Bias):} Dữ liệu lịch sử mang định kiến sẽ dạy cho AI đưa ra những quyết định phân biệt đối xử.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.13",
        "image": "ILLUSTRATION 10.13.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.14",
        "image": "ILLUSTRATION 10.14.png",
    },
    {
        "type": "normal",
        "title": "10.2 Công Nghệ Thay Đổi Phân Tích Dữ Liệu",
        "content": r"""\begin{itemize}
    \item \textbf{Value Creation (Mục tiêu tạo giá trị):} Công nghệ không chỉ để lưu trữ mà phải tự động hóa, phân tích sâu và cung cấp dự đoán.
    \item Sự hội tụ của Cloud Computing, AI và Blockchain đang tái định hình cách bộ phận Kế toán làm việc hàng ngày.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.15",
        "image": "ILLUSTRATION 10.15.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.16",
        "image": "ILLUSTRATION 10.16.png",
    },
    {
        "type": "normal",
        "title": "Khai phá Dữ liệu & Hợp đồng Thông minh",
        "content": r"""\begin{itemize}
    \item \textbf{Khai phá Dữ liệu (Data Mining):} Ứng dụng thống kê và học máy để tìm kiếm mô hình (pattern) ẩn trong cơ sở dữ liệu lớn.
    \item \textbf{Hợp đồng Thông minh (Smart Contracts):} Code chạy trên blockchain tự động thực thi các điều khoản hợp đồng khi điều kiện được thỏa mãn (VD: tự động thanh toán khi hàng được giao).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.17",
        "image": "ILLUSTRATION 10.17.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.18",
        "image": "ILLUSTRATION 10.18.png",
    },
    {
        "type": "normal",
        "title": "Tự Động Hóa Quy Trình Bằng Robot (RPA)",
        "content": r"""\begin{itemize}
    \item \textbf{RPA (Robotic Process Automation):} Sử dụng phần mềm (bot) để tự động hóa các tác vụ lặp đi lặp lại có quy tắc cố định (VD: nhập liệu hóa đơn, đối chiếu ngân hàng).
    \item \textbf{Lợi ích:} Giảm thiểu lỗi sai (human error), giải phóng nhân sự kế toán cho công việc phân tích.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.19",
        "image": "ILLUSTRATION 10.19.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.20",
        "image": "ILLUSTRATION 10.20.png",
    },
    {
        "type": "normal",
        "title": "Khai Phá Quy Trình (Process Mining)",
        "content": r"""\begin{itemize}
    \item \textbf{Process Mining:} Kỹ thuật phân tích nhật ký sự kiện (event logs) từ hệ thống (ERP) để phát hiện quy trình thực tế diễn ra như thế nào.
    \item \textbf{Ứng dụng:} Tìm ra các điểm nghẽn (bottleneck) trong quy trình phê duyệt tài chính, hoặc các bước thừa thãi gây lãng phí.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.21",
        "image": "ILLUSTRATION 10.21.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.22",
        "image": "ILLUSTRATION 10.22.png",
    },
    {
        "type": "normal",
        "title": "Kiểm Toán Liên Tục (Continuous Auditing)",
        "content": r"""\begin{itemize}
    \item \textbf{Khái niệm:} Tự động hóa quá trình giám sát giao dịch tài chính liên tục theo thời gian thực.
    \item \textbf{Cách hoạt động:} Hệ thống cài đặt các ngưỡng báo động (alarms). Bất cứ giao dịch nào vi phạm rule (VD: giao dịch trong ngày nghỉ) sẽ bị đánh dấu ngay lập tức.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.23",
        "image": "ILLUSTRATION 10.23.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.24",
        "image": "ILLUSTRATION 10.24.png",
    },
    {
        "type": "normal",
        "title": "Phân Tích Văn Bản (Textual Analysis)",
        "content": r"""\begin{itemize}
    \item \textbf{Textual Analysis:} Sử dụng NLP (Xử lý ngôn ngữ tự nhiên) để trích xuất thông tin từ tài liệu phi cấu trúc (Báo cáo thường niên 10-K, Biên bản họp).
    \item \textbf{Phân tích cảm xúc (Sentiment Analysis):} Đo lường tông giọng lạc quan hay bi quan của Ban giám đốc để dự báo hiệu quả tương lai.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.25",
        "image": "ILLUSTRATION 10.25.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.26",
        "image": "ILLUSTRATION 10.26.png",
    },
    {
        "type": "normal",
        "title": "Trí Tuệ Nhân Tạo (AI) & Công Nghệ Nhận Thức",
        "content": r"""\begin{itemize}
    \item \textbf{Công nghệ nhận thức (Cognitive Technologies):} Giúp phần mềm có khả năng nhìn (Computer Vision), nghe, đọc và đưa ra quyết định như con người.
    \item \textbf{Machine Learning (Học máy):} Thuật toán có khả năng tự cải thiện theo thời gian mà không cần lập trình lại tường minh (VD: Nhận diện chứng từ giả).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.27",
        "image": "ILLUSTRATION 10.27.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.28",
        "image": "ILLUSTRATION 10.28.png",
    },
    {
        "type": "normal",
        "title": "10.3 Công Nghệ Gia Tăng Giá Trị Kế Toán",
        "content": r"""\begin{itemize}
    \item Sự thay đổi diễn ra ở tất cả các lĩnh vực cốt lõi của ngành:
    \begin{itemize}
        \item Hệ thống Thông tin Kế toán (AIS)
        \item Kiểm toán (Auditing)
        \item Kế toán Tài chính (Financial Accounting)
        \item Kế toán Quản trị (Managerial Accounting)
        \item Kế toán Thuế (Tax Accounting)
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.29",
        "image": "ILLUSTRATION 10.29.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.30",
        "image": "ILLUSTRATION 10.30.png",
    },
    {
        "type": "normal",
        "title": "Hệ thống Thông tin Kế toán (AIS)",
        "content": r"""\begin{itemize}
    \item Hệ thống ERP hiện đại (như SAP, Oracle) đã tích hợp sẵn AI.
    \item \textbf{Vai trò của Kế toán:} Trở thành người giám sát, đảm bảo chất lượng dữ liệu đầu vào và thiết lập các rule chuẩn cho RPA tự động chạy.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.31",
        "image": "ILLUSTRATION 10.31.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.32",
        "image": "ILLUSTRATION 10.32.png",
    },
    {
        "type": "normal",
        "title": "Kiểm toán (Auditing)",
        "content": r"""\begin{itemize}
    \item Không còn kiểm tra chọn mẫu. Phân tích dữ liệu cho phép kiểm tra 100\% tổng thể dữ liệu giao dịch.
    \item Nhận diện rủi ro chủ động bằng học máy thay vì phản ứng thụ động sau khi kỳ kế toán kết thúc.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.33",
        "image": "ILLUSTRATION 10.33.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.34",
        "image": "ILLUSTRATION 10.34.png",
    },
    {
        "type": "normal",
        "title": "Kế toán Tài chính",
        "content": r"""\begin{itemize}
    \item Phân tích văn bản trên hàng ngàn BCTC 10-K của đối thủ trong vài giây để đưa ra báo cáo so sánh.
    \item Hỗ trợ lập BCTC chuẩn XBRL tự động và phát hiện bất thường trước khi nộp lên Ủy ban Chứng khoán.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.35A",
        "image": "ILLUSTRATION 10.35A.png",
    },
    {
        "type": "normal",
        "title": "Kế toán Quản trị",
        "content": r"""\begin{itemize}
    \item Thay vì chỉ nhìn vào quá khứ (Descriptive), Kế toán Quản trị chuyển sang Dự báo (Predictive) và Đề xuất (Prescriptive).
    \item Ứng dụng Process Mining để tối ưu hóa chi phí vận hành chuỗi cung ứng.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.35B",
        "image": "ILLUSTRATION 10.35B.png",
    },
    {
        "type": "normal",
        "title": "Kế toán Thuế",
        "content": r"""\begin{itemize}
    \item RPA tự động điền tờ khai và đối chiếu quy định pháp luật thay đổi liên tục.
    \item Phân tích rủi ro hồ sơ bị thanh tra thuế để doanh nghiệp có phương án giải trình sớm.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.36",
        "image": "ILLUSTRATION 10.36.png",
    },
    {
        "type": "normal",
        "title": "Tổng Kết Chương 10",
        "content": r"""\begin{itemize}
    \item Nghề kế toán không biến mất, mà sẽ chuyển dịch lên cấp độ cao hơn.
    \item Công việc chân tay, lặp lại sẽ do RPA và AI đảm nhiệm.
    \item Kế toán viên cần trở thành những \textbf{Data Analyst} và \textbf{Strategic Advisor} thực thụ.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 10.37",
        "image": "ILLUSTRATION 10.37.png",
    },
    {
        "type": "image",
        "title": "Intro 10.0",
        "image": "Intro 10.0.png",
    },
    {
        "type": "image",
        "title": "Apply It 10.1",
        "image": "Apply It 10.1.png",
    },
    {
        "type": "image",
        "title": "Apply It 10.2",
        "image": "Apply It 10.2.png",
    },
    {
        "type": "image",
        "title": "HowTo 10.2",
        "image": "HowTo 10.2.png",
    },
    {
        "type": "image",
        "title": "Adventure Sports 10.13",
        "image": "Adventure Sports 10.13.png",
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
        "type": "image",
        "title": "BE 10.5",
        "image": "BE 10.5.png",
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
        "title": "EX 10.3 & EX 10.12",
        "image1": "EX 10.3.png",
        "image2": "EX 10.12.png",
    },
]
