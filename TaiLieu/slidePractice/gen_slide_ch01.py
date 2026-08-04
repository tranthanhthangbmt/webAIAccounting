import os

out_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slidePractice\Slide_Practice_Ch01.tex"

latex_content = r"""\documentclass[aspectratio=169,12pt]{beamer}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage{lmodern}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{multicol}
\usepackage{tikz}
\usepackage{xcolor}

\usetheme{Madrid}
\usefonttheme{professionalfonts}

% --- Custom Colors & Settings ---
\definecolor{UBrandBlue}{RGB}{0, 71, 155}
\definecolor{UBrandGold}{RGB}{255, 184, 28}
\setbeamercolor{palette primary}{bg=UBrandBlue,fg=white}
\setbeamercolor{palette secondary}{bg=UBrandGold,fg=black}
\setbeamercolor{palette tertiary}{bg=UBrandBlue!80!black,fg=white}
\setbeamercolor{title}{bg=UBrandBlue,fg=white}
\setbeamercolor{item}{fg=UBrandBlue}

\title[Thực hành - Chương 1]{Dữ liệu và Phân tích trong Nghề Kế toán}
\subtitle{Data and Analytics in the Accounting Profession}
\author[Giảng viên]{Trí tuệ Nhân tạo cho Kế toán (AI in Accounting)}
\institute[Đại học]{Khoa Kế toán - Kiểm toán}
\date{Bài giảng Thực hành 01}

\begin{document}

% Slide 1: Title
\begin{frame}
    \titlepage
\end{frame}

% Slide 2: Mục tiêu
\begin{frame}{Tổng quan Chương (Chapter Preview)}
    \begin{itemize}
        \item \textbf{Sự thay đổi về dữ liệu và công nghệ} đang tác động mạnh mẽ đến vai trò của kế toán viên trong mọi lĩnh vực.
        \item \textbf{Kế toán viên tương lai} phải là:
        \begin{itemize}
            \item Chuyên gia linh hoạt, sáng tạo, am hiểu dữ liệu và công nghệ.
            \item Người giải quyết vấn đề (Problem-solvers) có tư duy phản biện.
        \end{itemize}
        \item \textbf{Góc nhìn chuyên gia}: 
        \begin{itemize}
            \item \textit{"Công nghệ không thay thế kế toán viên; nó tăng cường sự thành thạo kỹ thuật của họ..."} - KPMG.
            \item \textit{"Kỹ năng giải quyết vấn đề là thiết yếu... Nhà tuyển dụng tìm kiếm những người có khả năng suy nghĩ phân tích..."} - Deloitte.
        \end{itemize}
    \end{itemize}
\end{frame}

% Slide 3: Roadmap
\begin{frame}{Bản đồ Chương (Chapter Roadmap)}
    \begin{itemize}
        \item \textbf{LO 1.1:} Tóm tắt cách những tiến bộ về dữ liệu và công nghệ đang tác động đến các chuyên gia kế toán.
        \item \textbf{LO 1.2:} Mô tả các giai đoạn của quy trình phân tích dữ liệu (Data Analysis Process).
        \item \textbf{LO 1.3:} Xác định các kỹ năng cần thiết để thực hiện phân tích dữ liệu.
        \item \textbf{LO 1.4:} Giải thích cách áp dụng tư duy phân tích dữ liệu (Data Analytics Mindset) vào quy trình phân tích dữ liệu.
    \end{itemize}
\end{frame}

% --- Mục tiêu 1.1 ---
\begin{frame}{1.1 Dữ liệu và Phân tích đang Chuyển đổi Nghề Kế toán}
    \begin{itemize}
        \item Kế toán viên hiện nay có thể hoàn thành các chức năng kế toán lặp đi lặp lại chỉ trong một phần nhỏ thời gian so với trước đây.
        \item Tập trung vào các hoạt động mang lại \textbf{giá trị gia tăng}: 
        \begin{itemize}
            \item Đánh giá các kiểm soát.
            \item Cung cấp thông tin chi tiết về tài chính.
            \item Thực hiện các phân tích để hỗ trợ ra quyết định kinh doanh.
        \end{itemize}
        \item \textbf{Sự thay đổi của các kỳ thi}: CPA, CMA hiện nay đều bao gồm môn học về "Công nghệ và Phân tích dữ liệu".
    \end{itemize}
\end{frame}

\begin{frame}{Dữ liệu và Công nghệ (Data and Technology)}
    \begin{itemize}
        \item \textbf{Dữ liệu (Data):} Là những con số và sự kiện thô.
        \item \textbf{Thông tin (Information):} Là kiến thức thu được từ dữ liệu (sau khi áp dụng công nghệ).
        \item \textbf{Phân tích dữ liệu (Data Analytics):} Là quá trình phân tích dữ liệu thô để trả lời câu hỏi và cung cấp Insight.
        \item \textbf{Kinh doanh Thông minh Tự phục vụ (SSBI):}
        \begin{itemize}
            \item Cung cấp khả năng xử lý dữ liệu mở rộng: Chuẩn bị, Phân tích, Báo cáo.
            \item Dễ sử dụng, không yêu cầu bằng cấp khoa học máy tính!
            \item Ví dụ: Alteryx, Power BI, Tableau, Excel.
        \end{itemize}
    \end{itemize}
\end{frame}

\begin{frame}{Ví dụ SSBI (Alteryx Workflow)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.1.png}
        \caption{Alteryx cho phép thiết kế các luồng công việc: Nhập, Làm sạch, Lọc và Xuất.}
    \end{figure}
\end{frame}

\begin{frame}{Hiệu năng của SSBI (Alteryx Run Time)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.2.png}
        \caption{Chỉ mất 0.5 giây để nhập, làm sạch, lọc và xuất hơn 2.000 hàng dữ liệu.}
    \end{figure}
\end{frame}

\begin{frame}{Tác động đến Kiểm toán (Auditing)}
    \begin{itemize}
        \item \textbf{Mở rộng phạm vi:} Vượt ra ngoài việc thử nghiệm lấy mẫu (Sample-based Testing), tiến tới phân tích toàn bộ quần thể dữ liệu.
        \item \textbf{Phát hiện bất thường:} Xem xét toàn bộ tập dữ liệu để xác định ngoại lệ và điểm dị biệt.
        \item Cả kiểm toán viên nội bộ và độc lập đều sử dụng phân tích để \textbf{Đánh giá rủi ro} và thực hiện \textbf{Thủ tục cơ bản}.
    \end{itemize}
\end{frame}

\begin{frame}{Trực quan hóa Dữ liệu trong Kiểm toán (1/2)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.3.png}
        \caption{Phân tích Đánh giá Rủi ro sổ cái chung.}
    \end{figure}
\end{frame}

\begin{frame}{Trực quan hóa Dữ liệu trong Kiểm toán (2/2)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.4.png}
        \caption{So sánh doanh thu kỳ vọng và thực tế.}
    \end{figure}
\end{frame}

\begin{frame}{Tác động đến Kế toán Tài chính & Quản trị}
    \begin{itemize}
        \item \textbf{Kế toán Tài chính:}
        \begin{itemize}
            \item Sử dụng phần mềm tự động hóa (RPA, SSBI) cho các bút toán, lập báo cáo.
            \item Tạo các \textbf{Bảng điều khiển (Dashboards)} tài chính.
        \end{itemize}
        \item \textbf{Kế toán Quản trị:}
        \begin{itemize}
            \item Xác định rủi ro, cải thiện ngân sách và dự báo.
            \item Sử dụng Bảng tô sáng (Highlight Table) để xác định hiệu suất cao/thấp.
        \end{itemize}
    \end{itemize}
\end{frame}

\begin{frame}{Bảng điều khiển Kế toán Tài chính}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.5.png}
        \caption{Giám sát hiệu suất tài chính tổng thể.}
    \end{figure}
\end{frame}

\begin{frame}{Bảng điều khiển Kế toán Quản trị}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.6.png}
        \caption{Bảng tô sáng (Top) và Phân tích Tỷ suất lợi nhuận (Bottom).}
    \end{figure}
\end{frame}

\begin{frame}{Tác động đến Kế toán Thuế}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.6\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.7.png}
        \caption{Bảng điều khiển thuế theo dõi vị thế thuế của tổ chức.}
    \end{figure}
    \small
    Sử dụng dữ liệu để phân tích tính hiệu quả về thuế và hỗ trợ tuân thủ.
\end{frame}

% --- Mục tiêu 1.2 ---
\begin{frame}{1.2 Các Giai đoạn của Quy trình Phân tích Dữ liệu}
    \begin{figure}[h]
        \centering
        \includegraphics[width=\textwidth]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.8.png}
        \caption{3 Giai đoạn: Lên kế hoạch (Plan) -> Phân tích (Analyze) -> Báo cáo (Report).}
    \end{figure}
\end{frame}

\begin{frame}{Giai đoạn 1: Lên kế hoạch (Plan)}
    \begin{itemize}
        \item \textbf{Hiểu rõ Động lực:} Động lực từ bên ngoài hoặc nội bộ (vd: Muốn hiểu tại sao doanh thu lại giảm từ năm 2024 đến 2025).
        \item \textbf{Xác định Mục tiêu:} Thiết lập đích đến và phát triển các câu hỏi cụ thể (vd: Giảm ở sản phẩm nào, khu vực nào?).
        \item \textbf{Thiết kế Chiến lược:}
        \begin{itemize}
            \item Nguồn dữ liệu: Dữ liệu nội bộ vs. Dữ liệu bên ngoài.
            \item Phương pháp phân tích: Mô tả, Chẩn đoán, Dự đoán, Đề xuất.
        \end{itemize}
    \end{itemize}
\end{frame}

\begin{frame}{Hiểu rõ Động lực (Phân tích Doanh số OSS)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.9.png}
        \caption{Tổng doanh số giảm 9.4\% từ 2024 đến 2025 $\rightarrow$ Động lực nội bộ.}
    \end{figure}
\end{frame}

\begin{frame}{Bốn phương pháp phân tích dữ liệu}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.10.png}
        \caption{Mô tả (Điều gì đã xảy ra), Chẩn đoán (Tại sao), Dự đoán (Tương lai), Đề xuất (Hành động).}
    \end{figure}
\end{frame}

\begin{frame}{Giai đoạn 2: Phân tích (Analyze)}
    \begin{itemize}
        \item \textbf{Chuẩn bị Dữ liệu (ETL):}
        \begin{itemize}
            \item \textbf{Trích xuất (Extracting):} Lấy dữ liệu từ nguồn.
            \item \textbf{Chuyển đổi (Transforming):} Làm sạch, lập hồ sơ dữ liệu (Data Profiling).
            \item \textbf{Tải (Loading):} Đưa vào công cụ (Excel, Tableau...).
        \end{itemize}
        \item \textbf{Xây dựng Mô hình Thông tin:} Tính toán các KPI (vd: Biên lợi nhuận).
        \item \textbf{Khám phá Dữ liệu (Explore Data):} Xác định mẫu hình, xu hướng, bất thường.
    \end{itemize}
\end{frame}

\begin{frame}{Mô hình Thông tin: Phân tích Lợi nhuận theo Quốc gia}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.12.png}
        \caption{Lợi nhuận đang sụt giảm ở Canada và Mexico.}
    \end{figure}
\end{frame}

\begin{frame}{Khám phá Dữ liệu: Lợi nhuận Khu vực}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.13.png}
        \caption{Nhiều khu vực ở Canada và Mexico có doanh số suy giảm.}
    \end{figure}
\end{frame}

\begin{frame}{Giai đoạn 3: Báo cáo (Report)}
    \begin{itemize}
        \item \textbf{Diễn giải Kết quả (Interpret Results):}
        \begin{itemize}
            \item Xem xét lại các phân tích xem chúng có hợp lý và giải quyết được mục tiêu hay chưa.
            \item Kết quả có hợp lệ và đáng tin cậy không?
        \end{itemize}
        \item \textbf{Truyền đạt Kết quả (Communicate Results):}
        \begin{itemize}
            \item Giao tiếp bằng lời, văn bản, hoặc hình ảnh (Dashboard).
            \item Để ra quyết định hành động.
        \end{itemize}
    \end{itemize}
\end{frame}

\begin{frame}{Bảng điều khiển truyền đạt thông tin (Dashboard)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.14.png}
        \caption{Dashboard so sánh phần trăm thay đổi lợi nhuận và doanh thu.}
    \end{figure}
\end{frame}

\begin{frame}{MOSAIC: Kết hợp tất cả lại với nhau}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.15.png}
        \caption{Quy trình MOSAIC trong Phân tích dữ liệu.}
    \end{figure}
\end{frame}

% --- Mục tiêu 1.3 ---
\begin{frame}{1.3 Tư duy Phân tích Dữ liệu là gì?}
    \begin{itemize}
        \item \textbf{Tư duy phân tích dữ liệu:} Thói quen nghề nghiệp của việc suy nghĩ phản biện xuyên suốt toàn bộ quá trình phân tích.
        \item Các kỹ năng cốt lõi cần phát triển:
        \begin{itemize}
            \item \textbf{Tư duy Phản biện (Critical Thinking)}
            \item \textbf{Sự am hiểu Dữ liệu (Data Literacy)}
            \item \textbf{Kỹ năng Công nghệ (Technology Skills)}
            \item \textbf{Kỹ năng Giao tiếp (Communication Skills)}
        \end{itemize}
        \item Luôn hỏi "Tại sao?", cởi mở học công nghệ mới.
    \end{itemize}
\end{frame}

\begin{frame}{Kỹ năng Công nghệ \& Giao tiếp (Khảo sát)}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \begin{figure}[h]
                \centering
                \includegraphics[width=\textwidth]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.16.png}
                \caption{Kỹ năng Công nghệ}
            \end{figure}
        \end{column}
        \begin{column}{0.5\textwidth}
            \begin{figure}[h]
                \centering
                \includegraphics[width=\textwidth]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.17.png}
                \caption{Kỹ năng Mềm (Giao tiếp \& Phản biện)}
            \end{figure}
        \end{column}
    \end{columns}
\end{frame}

% --- Mục tiêu 1.4 ---
\begin{frame}{1.4 Áp dụng Tư duy Phân tích Dữ liệu (SPARKS)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.18.png}
        \caption{6 Yếu tố của tư duy phản biện (Stakeholders, Purpose, Alternatives, Risks, Knowledge, Self-reflection).}
    \end{figure}
\end{frame}

\begin{frame}{S - Stakeholders (Các bên liên quan)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.19.png}
        \caption{Nội bộ (Nhân viên, Quản lý) và Bên ngoài (Nhà đầu tư, Đối tác).}
    \end{figure}
\end{frame}

\begin{frame}{R - Risks (Đánh giá Rủi ro)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.20.png}
        \caption{Rủi ro từ Dữ liệu, Phân tích, Giả định, Định kiến.}
    \end{figure}
\end{frame}

\begin{frame}{Tổng hợp SPARKS}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.65\textheight]{../TaiLieu/textbookForPractice/Figures/Ch_01/ILLUSTRATION 1.21.png}
        \caption{Bộ công cụ Tư duy Phản biện SPARKS.}
    \end{figure}
\end{frame}

% --- Phần Bài tập Thực hành ---
\begin{frame}{Đánh giá và Thực hành Chương}
    \begin{center}
        \Large \textbf{Phần Bài tập Thực hành (Practice \& Exercises)}
    \end{center}
\end{frame}

\begin{frame}{Bài tập Ngắn (Brief Exercises)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/BE 1.1.png}
    \end{figure}
\end{frame}

\begin{frame}{Bài tập Ngắn (Brief Exercises - Tiếp)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/BE 1.1_1.png}
    \end{figure}
\end{frame}

\begin{frame}{Bài tập Ngắn (Brief Exercises - Tiếp)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/BE 1.6.png}
    \end{figure}
\end{frame}

\begin{frame}{Bài tập (Exercises - EX 1.3)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/EX 1.3.png}
    \end{figure}
\end{frame}

\begin{frame}{Bài tập (Exercises - EX 1.4)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/EX 1.4.png}
    \end{figure}
\end{frame}

\begin{frame}{Bài tập (Exercises - EX 1.5)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/EX 1.5.png}
    \end{figure}
\end{frame}

\begin{frame}{Bài tập (Exercises - EX 1.6)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/EX 1.6.png}
    \end{figure}
\end{frame}

\begin{frame}{Bài tập (Exercises - EX 1.7)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/EX_1.7.png}
    \end{figure}
\end{frame}

% --- Tình huống Ứng dụng Chuyên môn ---
\begin{frame}{Tình huống Ứng dụng Chuyên môn (PAC)}
    \begin{center}
        \Large \textbf{Little Tots Daycare}
    \end{center}
\end{frame}

\begin{frame}{Dữ liệu Tình huống 1}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/PAC_1.png}
    \end{figure}
\end{frame}

\begin{frame}{Dữ liệu Tình huống 2}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/PAC_2.png}
    \end{figure}
\end{frame}

\begin{frame}{Phân tích Tình huống (PAC 1.1)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/PAC 1.1.png}
    \end{figure}
\end{frame}

\begin{frame}{Phân tích Tình huống (PAC 1.3)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/PAC 1.3.png}
    \end{figure}
\end{frame}

\begin{frame}{Phân tích Tình huống (PAC 1.4)}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{../TaiLieu/textbookForPractice/Figures/Ch_01/PAC 1.4.png}
    \end{figure}
\end{frame}

\begin{frame}{Kết thúc}
    \begin{center}
        \Huge \textbf{Hỏi \& Đáp} \\
        \vspace{1cm}
        \Large Cảm ơn các bạn đã lắng nghe!
    \end{center}
\end{frame}

\end{document}
"""

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(latex_content)
    
print("Created Slide_Practice_Ch01.tex successfully.")
