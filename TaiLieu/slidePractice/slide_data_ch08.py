chapter_title = 'Diễn giải Kết quả Phân tích Dữ liệu'
chapter_subtitle = 'Interpreting Data Analysis Results'

slides = [
    {
        "type": "title_slide",
    },
    {
        "type": "normal",
        "title": "Góc nhìn Chuyên gia (Professional Insight)",
        "content": r"""\begin{itemize}
    \item \textbf{Câu hỏi cốt lõi:} "Liệu kết quả phân tích này có hợp lý không?" (Do the Analysis Results Make Sense?)
    \item \textbf{Trách nhiệm của Kế toán viên:} Kế toán không chỉ tạo ra báo cáo mà còn phải \textit{diễn giải} ý nghĩa của những con số đó để tư vấn cho Ban Lãnh đạo.
    \item \textbf{Tư duy phản biện (Critical Thinking):} Đừng bao giờ tin tưởng tuyệt đối vào kết quả đầu ra của một thuật toán hay AI mà không có sự đánh giá, kiểm chứng từ con người.
\end{itemize}""",
    },
    {
        "type": "normal",
        "title": "Lộ trình Chương (Chapter Roadmap)",
        "content": r"""\begin{itemize}
    \item \textbf{LO 8.1:} Phân biệt Khám phá và Diễn giải.
    \item \textbf{LO 8.2:} Áp dụng Tư duy Phản biện trong Diễn giải (SPARK-S).
    \item \textbf{LO 8.3:} Đánh giá Sự phù hợp của Kết quả.
    \item \textbf{LO 8.4:} Đánh giá Phân tích Mô tả và Chẩn đoán.
    \item \textbf{LO 8.5:} Đánh giá Phân tích Dự đoán và Đề xuất.
\end{itemize}""",
    },
    {
        "type": "normal",
        "title": "8.1 Rút ra kết luận từ Phân tích dữ liệu",
        "content": r"""\begin{itemize}
    \item \textbf{Khám phá (Exploration):} Trả lời câu hỏi "Tôi đang nhìn thấy gì?" Mục tiêu là \textit{hiểu dữ liệu} (Understanding the data).
    \item \textbf{Diễn giải (Interpretation):} Trả lời câu hỏi "Điều này có ý nghĩa gì đối với doanh nghiệp?" Mục tiêu là \textit{hiểu kết quả phân tích} (Understanding the analysis).
    \item \textbf{Quá trình Diễn giải:} Đòi hỏi sự kết hợp giữa kiến thức chuyên môn kế toán, hiểu biết về bối cảnh kinh doanh và các nguyên tắc thống kê.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.1",
        "image": "ILLUSTRATION 8.1.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.2",
        "image": "ILLUSTRATION 8.2.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.3",
        "image": "ILLUSTRATION 8.3.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.4",
        "image": "ILLUSTRATION 8.4.png",
    },
    {
        "type": "normal",
        "title": "Từ Trực quan hóa đến Diễn giải",
        "content": r"""\begin{itemize}
    \item \textbf{Ví dụ:} Một biểu đồ doanh thu đang đi xuống.
    \item \textbf{Khám phá:} Phát hiện ra doanh thu tháng 10 giảm 15\% so với tháng 9.
    \item \textbf{Diễn giải:} Nguyên nhân là do gián đoạn chuỗi cung ứng hoặc thay đổi chính sách tín dụng? Hậu quả là dòng tiền tháng 11 sẽ bị thiếu hụt.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.5",
        "image": "ILLUSTRATION 8.5.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.6",
        "image": "ILLUSTRATION 8.6.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.7",
        "image": "ILLUSTRATION 8.7.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.8",
        "image": "ILLUSTRATION 8.8.png",
    },
    {
        "type": "normal",
        "title": "8.2 Ứng dụng Tư duy Phản biện (SPARK-S)",
        "content": r"""\begin{itemize}
    \item Tư duy phản biện giúp chúng ta không bị dẫn dắt bởi những dữ liệu sai lệch hoặc thiên kiến. Khung \textbf{SPARK-S}:
    \begin{itemize}
        \item \textbf{S - Stakeholders:} Ai bị ảnh hưởng bởi kết quả này?
        \item \textbf{P - Purpose:} Mục đích ban đầu của việc phân tích là gì?
        \item \textbf{A - Alternatives:} Có cách giải thích nào khác cho hiện tượng này không?
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.9",
        "image": "ILLUSTRATION 8.9.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.10",
        "image": "ILLUSTRATION 8.10.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.11",
        "image": "ILLUSTRATION 8.11.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.12",
        "image": "ILLUSTRATION 8.12.png",
    },
    {
        "type": "normal",
        "title": "Tư duy Phản biện (Tiếp theo)",
        "content": r"""\begin{itemize}
    \item \textbf{Khung SPARK-S (Tiếp):}
    \begin{itemize}
        \item \textbf{R - Risks \& Biases:} Phân tích này có gặp phải thiên kiến xác nhận (Confirmation Bias) hay rủi ro dữ liệu sai không?
        \item \textbf{K - Knowledge:} Chúng ta cần thêm thông tin gì để kết luận chắc chắn hơn?
        \item \textbf{S - Self-reflection:} Đánh giá lại bản thân trong quá trình phân tích.
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.13",
        "image": "ILLUSTRATION 8.13.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.14",
        "image": "ILLUSTRATION 8.14.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.15",
        "image": "ILLUSTRATION 8.15.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.16",
        "image": "ILLUSTRATION 8.16.png",
    },
    {
        "type": "normal",
        "title": "8.3 Đánh giá Sự phù hợp của Kết quả",
        "content": r"""\begin{itemize}
    \item \textbf{Câu hỏi chính:} Kết quả thu được có thực sự \textit{trả lời được câu hỏi kinh doanh} ban đầu không?
    \item \textbf{Đánh giá Dữ liệu (Data):} Dữ liệu có đủ sạch, đủ lớn và đại diện cho vấn đề không?
    \item \textbf{Đánh giá Phương pháp (Methods):} Mô hình thống kê hoặc biểu đồ được chọn có phù hợp với loại dữ liệu không?
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.17",
        "image": "ILLUSTRATION 8.17.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.18",
        "image": "ILLUSTRATION 8.18.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.19",
        "image": "ILLUSTRATION 8.19.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.20",
        "image": "ILLUSTRATION 8.20.png",
    },
    {
        "type": "normal",
        "title": "Kiểm tra và Bổ sung thông tin",
        "content": r"""\begin{itemize}
    \item \textbf{Kiểm tra Kết quả (Examine Results):} Các con số có ý nghĩa thực tế không? (Ví dụ: Tỷ suất lợi nhuận 500\% có thể là do lỗi dữ liệu hơn là thực tế).
    \item \textbf{Xác định thông tin cần thêm:} Có cần bổ sung dữ liệu phi tài chính (Non-financial data) để giải thích cho dữ liệu tài chính không?
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.21",
        "image": "ILLUSTRATION 8.21.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.22",
        "image": "ILLUSTRATION 8.22.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.23",
        "image": "ILLUSTRATION 8.23.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.24",
        "image": "ILLUSTRATION 8.24.png",
    },
    {
        "type": "normal",
        "title": "8.4 Đánh giá Phân tích Mô tả và Chẩn đoán",
        "content": r"""\begin{itemize}
    \item \textbf{Tính Hợp lệ (Validity):} Đo lường đúng thứ cần đo.
    \item \textbf{Độ Tin cậy (Reliability):} Tính nhất quán của kết quả khi lặp lại phân tích.
    \item \textbf{Phân tích Mô tả (Descriptive):} Đánh giá tính chính xác của các chỉ số tóm tắt (Tổng, Trung bình, Max, Min).
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.25",
        "image": "ILLUSTRATION 8.25.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.26",
        "image": "ILLUSTRATION 8.26.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.27",
        "image": "ILLUSTRATION 8.27.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.28",
        "image": "ILLUSTRATION 8.28.png",
    },
    {
        "type": "normal",
        "title": "Đánh giá Phân tích Chẩn đoán",
        "content": r"""\begin{itemize}
    \item \textbf{Phân tích Chẩn đoán (Diagnostic):} Giải thích "Tại sao điều đó xảy ra?"
    \item \textbf{Nhận diện Điểm dị biệt (Outliers):} Sử dụng biểu đồ phân tán (Scatterplot) hoặc Box-plot để tìm các giao dịch bất thường trong Kiểm toán.
    \item \textbf{Lưu ý:} Không phải Outlier nào cũng là gian lận, có thể do sai sót nhập liệu.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.29",
        "image": "ILLUSTRATION 8.29.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.30",
        "image": "ILLUSTRATION 8.30.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.31",
        "image": "ILLUSTRATION 8.31.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.32",
        "image": "ILLUSTRATION 8.32.png",
    },
    {
        "type": "normal",
        "title": "8.5 Đánh giá Phân tích Dự đoán và Đề xuất",
        "content": r"""\begin{itemize}
    \item \textbf{Phân tích Dự đoán (Predictive):} Sử dụng mô hình (như Hồi quy - Regression) để dự báo tương lai.
    \item \textbf{Đánh giá Mô hình:}
    \begin{itemize}
        \item Hệ số $R^2$ có đủ cao không?
        \item Mối quan hệ có ý nghĩa thống kê (p-value < 0.05) không?
        \item Cẩn thận với "Tương quan không có nghĩa là Nhân quả" (Correlation vs. Causation).
    \end{itemize}
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.32_1",
        "image": "ILLUSTRATION 8.32_1.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.33",
        "image": "ILLUSTRATION 8.33.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.34",
        "image": "ILLUSTRATION 8.34.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.35",
        "image": "ILLUSTRATION 8.35.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.36",
        "image": "ILLUSTRATION 8.36.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.37",
        "image": "ILLUSTRATION 8.37.png",
    },
    {
        "type": "normal",
        "title": "Đánh giá Phân tích Đề xuất",
        "content": r"""\begin{itemize}
    \item \textbf{Phân tích Đề xuất (Prescriptive):} Tối ưu hóa các nguồn lực để đạt kết quả tốt nhất.
    \item \textbf{Đánh giá Khả năng Thực thi:} Đề xuất của AI có khả thi trong điều kiện ngân sách và chính sách của công ty không?
    \item \textbf{Kết luận:} Con người luôn là chốt chặn cuối cùng trong quá trình ra quyết định tài chính.
\end{itemize}""",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.38",
        "image": "ILLUSTRATION 8.38.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.39",
        "image": "ILLUSTRATION 8.39.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.40",
        "image": "ILLUSTRATION 8.40.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.41",
        "image": "ILLUSTRATION 8.41.png",
    },
    {
        "type": "image",
        "title": "ILLUSTRATION 8.42",
        "image": "ILLUSTRATION 8.42.png",
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
        "title": "BE 8.3 & BE 8.4",
        "image1": "BE 8.3.png",
        "image2": "BE 8.4.png",
    },
    {
        "type": "double_image",
        "title": "BE 8.7 & BE 8.8",
        "image1": "BE 8.7.png",
        "image2": "BE 8.8.png",
    },
    {
        "type": "double_image",
        "title": "BE 8.9 & BE 8.10",
        "image1": "BE 8.9.png",
        "image2": "BE 8.10.png",
    },
    {
        "type": "image",
        "title": "BE 8.11",
        "image": "BE 8.11.png",
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
        "title": "EX 8.1 & EX 8.2",
        "image1": "EX 8.1.png",
        "image2": "EX 8.2.png",
    },
    {
        "type": "double_image",
        "title": "EX 8.4 & EX 8.5",
        "image1": "EX 8.4.png",
        "image2": "EX 8.5.png",
    },
    {
        "type": "double_image",
        "title": "EX 8.6 & EX 8.7",
        "image1": "EX 8.6.png",
        "image2": "EX 8.7.png",
    },
    {
        "type": "double_image",
        "title": "EX 8.8 & EX 8.9",
        "image1": "EX 8.8.png",
        "image2": "EX 8.9.png",
    },
    {
        "type": "double_image",
        "title": "EX 8.10 & EX 8.11",
        "image1": "EX 8.10.png",
        "image2": "EX 8.11.png",
    },
    {
        "type": "double_image",
        "title": "EX 8.12 & EX 8.13",
        "image1": "EX 8.12.png",
        "image2": "EX 8.13.png",
    },
    {
        "type": "double_image",
        "title": "EX 8.14 & EX 8.15",
        "image1": "EX 8.14.png",
        "image2": "EX 8.15.png",
    },
    {
        "type": "double_image",
        "title": "EX 8.16 & EX 8.17A",
        "image1": "EX 8.16.png",
        "image2": "EX 8.17A.png",
    },
    {
        "type": "double_image",
        "title": "EX 8.17B & EX 8.19",
        "image1": "EX 8.17B.png",
        "image2": "EX 8.19.png",
    },
    {
        "type": "image",
        "title": "EX 8.20",
        "image": "EX 8.20.png",
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
        "title": "PAC 8.1A & PAC 8.1b",
        "image1": "PAC 8.1A.png",
        "image2": "PAC 8.1b.png",
    },
    {
        "type": "double_image",
        "title": "PAC 8.1A_1 & PAC 8.2",
        "image1": "PAC 8.1A_1.png",
        "image2": "PAC 8.2.png",
    },
    {
        "type": "double_image",
        "title": "PAC 8.3 & PAC 8.4",
        "image1": "PAC 8.3.png",
        "image2": "PAC 8.4.png",
    },
    {
        "type": "normal",
        "title": "Trường hợp và Bổ trợ",
        "content": r"""\begin{center}
        \Huge \textbf{Tình huống Bổ trợ \& Dữ liệu} \\
        \vspace{0.5cm}
        \Large PR, ERD, Info
    \end{center}""",
    },
    {
        "type": "image",
        "title": "LO 2.4",
        "image": "LO 2.4.png",
    },
    {
        "type": "image",
        "title": "Infor 8.0",
        "image": "Infor 8.0.png",
    },
    {
        "type": "image",
        "title": "Ortho Inc 8.0",
        "image": "Ortho Inc 8.0.png",
    },
    {
        "type": "image",
        "title": "Apply It 8.1A",
        "image": "Apply It 8.1A.png",
    },
    {
        "type": "image",
        "title": "Apply It 8.1B",
        "image": "Apply It 8.1B.png",
    },
    {
        "type": "image",
        "title": "ERD 8.1A",
        "image": "ERD 8.1A.png",
    },
    {
        "type": "image",
        "title": "ERD 8.1B",
        "image": "ERD 8.1B.png",
    },
    {
        "type": "image",
        "title": "Ortho Inc 8.1",
        "image": "Ortho Inc 8.1.png",
    },
    {
        "type": "image",
        "title": "PR 8.1",
        "image": "PR 8.1.png",
    },
    {
        "type": "image",
        "title": "Apply It 8.1A_1",
        "image": "Apply It 8.1A_1.png",
    },
    {
        "type": "image",
        "title": "PR 8.2A",
        "image": "PR 8.2A.png",
    },
    {
        "type": "image",
        "title": "PR 8.2B",
        "image": "PR 8.2B.png",
    },
    {
        "type": "image",
        "title": "Apply It 8.3",
        "image": "Apply It 8.3.png",
    },
    {
        "type": "image",
        "title": "Apply It 8.4",
        "image": "Apply It 8.4.png",
    },
    {
        "type": "image",
        "title": "Apply It 8.5",
        "image": "Apply It 8.5.png",
    },
]
