import os

def create_beamer_slide():
    tex_content = r"""\documentclass[aspectratio=169]{beamer}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{tabularx}

% Cấu hình giao diện Beamer
\usetheme{Madrid}
\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}[frame number]

\title[TTNT trong Kế toán - Buổi 6]{Trí tuệ Nhân tạo Ứng dụng trong Kế toán}
\subtitle{Buổi 6: AI trong Kiểm tra Gian lận \& Ổn định Tài chính Vĩ mô}
\author{Giảng viên: [Tên Giảng Viên]}
\institute{Đại học Đông Á}
\date{\today}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Nội dung Bài học}
    \tableofcontents
\end{frame}

% ==========================================
% SECTION 1: Kế toán Điều tra & Các công nghệ Cốt lõi
% ==========================================
\section{Kế toán Điều tra \& Các công nghệ Cốt lõi}

\begin{frame}{Sự bế tắc của Kiểm toán Truyền thống}
    \textbf{Sự trỗi dậy của AI trong Kế toán điều tra (Forensic Accounting):}
    \begin{itemize}
        \item Thời đại kỹ thuật số tạo ra khối lượng giao dịch khổng lồ mỗi ngày.
        \item Các phương pháp chọn mẫu thủ công đang bộc lộ quá nhiều điểm yếu.
        \item Quy trình thủ công tốn kém, độ trễ cao và phụ thuộc nhiều vào sai số chủ quan của con người.
    \end{itemize}
\end{frame}

\begin{frame}{Ẩn dụ: Bịt mắt mò kim đáy biển}
    \begin{exampleblock}{Kiểm toán thủ công}
        Việc chỉ chọn mẫu 5\% - 10\% để kiểm tra gian lận giống hệt như việc \textbf{"bịt mắt và đi mò kim dưới đáy biển"}. Kẻ gian lận tinh vi dễ dàng lách luật bằng cách xé nhỏ hóa đơn (Smurfing).
    \end{exampleblock}
    \vspace{0.3cm}
    \begin{alertblock}{Vị thám tử không bao giờ ngủ}
        AI đóng vai trò như một vị thám tử liên tục rà soát 100\% dân số dữ liệu 24/7. Nó đọc hàng triệu tài liệu trong một giây và đánh dấu sự liên kết giữa những manh mối nhỏ nhất.
    \end{alertblock}
\end{frame}

\begin{frame}{Sự chuyển dịch Mô hình Kế toán}
    \begin{itemize}
        \item \textbf{Mô hình cũ (Phản ứng hậu kiểm):} Phát hiện gian lận sau khi kỳ kế toán đã kết thúc, thiệt hại đã xảy ra và rất khó thu hồi tài sản.
        \item \textbf{Mô hình mới (Phòng ngừa chủ động - Proactive Prevention):} AI theo dõi dòng tiền ngay theo thời gian thực (real-time) và chặn đứng giao dịch trước khi tiền rời khỏi tài khoản.
    \end{itemize}
\end{frame}

\begin{frame}{So sánh: Phạm vi \& Thời gian Phát hiện}
    \begin{table}[]
        \centering
        \begin{tabularx}{\textwidth}{|l|X|X|}
        \hline
        \textbf{Tiêu chí} & \textbf{Phương pháp Truyền thống} & \textbf{Giải pháp AI/ML} \\ \hline
        \textbf{Phạm vi} & Chọn mẫu thống kê (5\% – 10\%). Bỏ lọt các gian lận tinh vi. & \textbf{Kiểm tra toàn phần (100\%)} liên tục 24/7. \\ \hline
        \textbf{Thời gian} & Kiểm tra hậu kỳ (sau khi kết thúc quý/năm). & \textbf{Phát hiện theo thời gian thực (Real-time)}. \\ \hline
        \end{tabularx}
        \caption{So sánh Phương pháp Kiểm tra Gian lận (Phần 1)}
    \end{table}
\end{frame}

\begin{frame}{So sánh: Quy tắc \& Loại Dữ liệu}
    \begin{table}[]
        \centering
        \begin{tabularx}{\textwidth}{|l|X|X|}
        \hline
        \textbf{Tiêu chí} & \textbf{Phương pháp Truyền thống} & \textbf{Giải pháp AI/ML} \\ \hline
        \textbf{Quy tắc} & Quy tắc tĩnh (VD: Hóa đơn > 50.000 USD). Rất dễ bị lách. & Học máy nhận diện \textbf{mô hình động (Dynamic Pattern)}. \\ \hline
        \textbf{Loại dữ liệu} & Chỉ xử lý số liệu có cấu trúc trên Excel, sổ cái. & Xử lý \textbf{cả dữ liệu phi cấu trúc} (Email, Hợp đồng) qua NLP. \\ \hline
        \textbf{Nguồn lực} & Mệt mỏi, tốn kém, dễ sai sót do chủ quan. & Tự động hóa, tập trung điều tra ca rủi ro cao. \\ \hline
        \end{tabularx}
        \caption{So sánh Phương pháp Kiểm tra Gian lận (Phần 2)}
    \end{table}
\end{frame}

\begin{frame}{Giảm thiểu Cảnh báo Giả (False Positives)}
    \begin{itemize}
        \item \textbf{Vấn đề của hệ thống cũ:} Các quy tắc cứng nhắc tạo ra quá nhiều cảnh báo giả, khiến kiểm toán viên bị "bội thực" cảnh báo và có xu hướng bỏ qua chúng.
        \item \textbf{Sức mạnh của AI:} Tự động học hỏi từ lịch sử giao dịch để phân biệt chính xác giữa một giao dịch lớn hợp lệ (do mở rộng kinh doanh) và một hành vi trục lợi.
        \item Hệ thống học hỏi liên tục giúp hệ thống thông minh hơn theo thời gian, nâng cao độ nhạy mà không tăng cảnh báo giả.
    \end{itemize}
\end{frame}

\begin{frame}{Các công nghệ AI cốt lõi trong Phát hiện Gian lận}
    Trí tuệ nhân tạo không chỉ là một khái niệm chung chung, mà là sự kết hợp của nhiều thuật toán tinh vi:
    \begin{enumerate}
        \item Học có giám sát (Supervised Learning).
        \item Học không giám sát (Unsupervised Learning - Anomaly Detection).
        \item Xử lý Ngôn ngữ Tự nhiên (NLP - Natural Language Processing).
        \item Phân tích Mạng lưới và Đồ thị (Graph Analytics).
    \end{enumerate}
\end{frame}

\begin{frame}{1. Học có giám sát (Supervised Learning)}
    \begin{itemize}
        \item Mô hình được huấn luyện trên các tập dữ liệu đã được con người \textbf{gán nhãn rõ ràng} (ví dụ: đâu là hóa đơn hợp lệ, đâu là hóa đơn gian lận).
        \item Thuật toán xây dựng một phương trình phân loại dựa trên những nhãn đã cho trước.
        \item \textbf{Ưu điểm:} Cực kỳ xuất sắc trong việc phát hiện các chiêu thức gian lận đã biết từ trước.
        \item \textbf{Nhược điểm:} Không thể phát hiện ra những mánh khóe hoàn toàn mới.
    \end{itemize}
\end{frame}

\begin{frame}{2. Học không giám sát (Unsupervised Learning)}
    \textbf{Phát hiện Bất thường (Anomaly Detection):}
    \begin{itemize}
        \item Không cần gán nhãn dữ liệu trước. Thuật toán tự động nhóm các giao dịch giống nhau lại thành cụm dựa trên thuộc tính tự nhiên.
        \item Bất kỳ giao dịch nào nằm chỏng chơ ngoài các cụm này (Outliers) sẽ bị cắm cờ cảnh báo (Flagged).
    \end{itemize}
    \vspace{0.3cm}
    \textit{Giải pháp này giúp tìm ra những lỗ hổng và thủ đoạn gian lận hoàn toàn mới (Unknown Unknowns) mà con người chưa từng lường trước.}
\end{frame}

\begin{frame}{3. Xử lý Ngôn ngữ Tự nhiên (NLP)}
    \begin{itemize}
        \item Dữ liệu kế toán không chỉ là những con số. Có đến 80\% dữ liệu doanh nghiệp là \textbf{phi cấu trúc} (Email, hợp đồng, báo cáo, tin nhắn).
        \item Thuật toán NLP có khả năng "đọc" và phân tích các văn bản phi cấu trúc này.
        \item Ứng dụng: Phân tích ngữ điệu (Sentiment Analysis) của biên bản cuộc họp, hợp đồng nhà thầu để tìm dấu hiệu thông đồng.
    \end{itemize}
\end{frame}

\begin{frame}{Ẩn dụ NLP: Che đậy kinh doanh bết bát}
    \begin{exampleblock}{Hành vi Quản trị Lợi nhuận (Earnings Management)}
        \begin{itemize}
            \item Khi công ty làm ăn thua lỗ, Ban giám đốc hiếm khi nói dối trắng trợn (vì sợ rủi ro pháp lý).
            \item Thay vào đó, họ dùng \textbf{ngôn từ thao túng}: Lạm dụng "thể bị động" để né tránh trách nhiệm.
            \item \textbf{Ví dụ:} Thay vì nói \textit{"Chúng tôi đã làm lỗ 5 tỷ"}, họ sẽ viết \textit{"Chi phí đã bị gia tăng do các yếu tố khách quan"}.
        \end{itemize}
    \end{exampleblock}
    $\Rightarrow$ NLP có thể đếm tự động tần suất sử dụng các từ ngữ né tránh này và cảnh báo cho Nhà đầu tư!
\end{frame}

\begin{frame}{4. Phân tích Đồ thị \& Mạng lưới (Graph Analytics)}
    \textbf{Khám phá mạng lưới Rửa tiền \& Sân sau:}
    \begin{itemize}
        \item AI tạo ra bản đồ trực quan hóa kết nối giữa hàng ngàn chủ tài khoản, địa chỉ IP truy cập, và số điện thoại.
        \item \textbf{Khám phá:} Dễ dàng nhận ra 5 công ty độc lập trên giấy tờ nhưng thực chất lại dùng chung một dải IP truy cập ngân hàng, hoặc chuyển tiền xoay vòng khép kín.
    \end{itemize}
\end{frame}

\begin{frame}{Case Study 1: Gian lận Thẻ Tín dụng \& Ngân hàng}
    \begin{itemize}
        \item \textbf{Thách thức:} Ngân hàng bán lẻ mất hàng triệu USD vì gian lận trực tuyến. Hệ thống cũ liên tục khóa nhầm thẻ của khách hàng hợp lệ (cảnh báo giả).
        \item \textbf{Giải pháp AI:} Triển khai \textbf{Học sâu (Deep Learning)} phân tích 200 biến số cùng lúc: GPS, thói quen chi tiêu, loại thiết bị, tốc độ gõ phím.
        \item \textbf{Kết quả:} Giảm 40\% cảnh báo giả, tăng 35\% khả năng chặn đứng giao dịch xấu, tiết kiệm 15 triệu USD trong năm đầu tiên.
    \end{itemize}
\end{frame}

\begin{frame}{Case Study 2: Gian lận Bảng lương (Payroll Fraud)}
    \begin{itemize}
        \item \textbf{Thách thức:} Tập đoàn 50.000 nhân viên trên 20 quốc gia bị thất thoát quỹ lương do tạo "nhân viên ma" (Ghost employees) và chấm công khống.
        \item Quy mô quá lớn khiến bộ phận nhân sự không thể nào rà soát thủ công từng hồ sơ.
        \item \textbf{Giải pháp AI:} Dùng Học máy không giám sát để phân nhóm toàn bộ dữ liệu trả lương trong 3 năm qua.
    \end{itemize}
\end{frame}

\begin{frame}{Nhận diện "Nhân viên ma" bằng Máy học}
    \begin{itemize}
        \item Thuật toán tự động đối chiếu chéo: mã số thuế, số tài khoản ngân hàng, địa chỉ nhà, và nhật ký quẹt thẻ ra vào cổng.
        \item \textbf{Kết quả:} Phát hiện ngay lập tức 45 tài khoản "nhân viên ma" dù tên khác nhau nhưng lại dùng chung số thẻ ngân hàng và có cùng một IP đăng nhập để điền timesheet.
        \item Tập đoàn thu hồi thành công 2.3 triệu USD bị biển thủ bởi các quản lý chi nhánh.
    \end{itemize}
\end{frame}

\begin{frame}{Case Study 3: Trục lợi Bảo hiểm (Insurance Claims)}
    \begin{itemize}
        \item \textbf{Thách thức:} Khách hàng làm giả hoặc thổi phồng hóa đơn y tế, hoặc dùng phần mềm chỉnh sửa ảnh để làm trầm trọng hóa vụ tai nạn xe hơi.
        \item \textbf{Giải pháp AI:} Tích hợp Computer Vision (Thị giác máy tính) để quét độ chân thực của ảnh hiện trường và NLP để đọc báo cáo giám định y tế.
        \item \textbf{Kết quả:} Rút ngắn thời gian duyệt hồ sơ hợp lệ từ 7 ngày xuống \textbf{10 phút}, chặn đứng 18\% yêu cầu bồi thường giả mạo.
    \end{itemize}
\end{frame}

% ==========================================
% SECTION 2: Chống Tham nhũng Công & Cuộc đua Thuật toán
% ==========================================
\section{Chống Tham nhũng Công \& Cuộc đua Thuật toán}

\begin{frame}{Chống Tham nhũng Khu vực Công}
    \begin{itemize}
        \item Khu vực công (mua sắm chính phủ, đấu thầu cơ sở hạ tầng) luôn là môi trường cực kỳ nhạy cảm và phức tạp.
        \item Hàng ngàn dự án tiêu tốn ngân sách khổng lồ mỗi năm.
        \item Chỉ kiểm tra sổ sách kế toán truyền thống là không đủ để phanh phui những đường dây tham nhũng được bọc lót tinh vi bằng giấy tờ hợp lệ.
    \end{itemize}
\end{frame}

\begin{frame}{Case Study 4: Bất thường trong Mua sắm Công}
    \begin{itemize}
        \item \textbf{Thách thức:} Cơ quan chính phủ cần kiểm toán hàng nghìn gói thầu. Có dấu hiệu \textbf{thông đồng (collusion)} và \textbf{chia nhỏ gói thầu} để lách luật.
        \item \textbf{Phát hiện của AI:} Chỉ lệch giá trị đấu thầu thì chưa chắc là tham nhũng. Hệ thống AI tập trung tìm kiếm các \textit{mô hình trao thầu lặp đi lặp lại}.
    \end{itemize}
\end{frame}

\begin{frame}{Chiêu trò Chia nhỏ Gói thầu (Smurfing trong Đấu thầu)}
    \begin{itemize}
        \item \textbf{Lách luật hạn mức:} Nếu quy định là trên 1 tỷ đồng phải đấu thầu công khai, kẻ gian sẽ chia nhỏ dự án thành 3 gói thầu giá 350 triệu đồng để được chỉ định thầu.
        \item \textbf{AI vào cuộc:} Tự động gom nhóm các gói thầu có cùng nội dung công việc, cùng địa điểm và thời gian triển khai sát nhau, được giao cho cùng một nhóm công ty gia đình.
        \item Cảnh báo đỏ ngay lập tức cho Ủy ban Kiểm tra.
    \end{itemize}
\end{frame}

\begin{frame}{Mạng lưới Thông đồng \& Tiền Lại quả (Kickbacks)}
    \begin{alertblock}{Chiêu trò của Nhà thầu}
        \begin{itemize}
            \item AI phát hiện ra quy luật: 4 công ty liên tục tham gia đấu thầu chung, và \textbf{thay phiên nhau trúng thầu} một cách nhịp nhàng.
            \item Giá trúng thầu luôn bám sát nút giá dự toán (chỉ thấp hơn 0.5\% - 1\%) nhưng lại cao hơn 30\% so với giá thị trường.
        \end{itemize}
    \end{alertblock}
    \vspace{0.2cm}
    $\Rightarrow$ Phanh phui đường dây thổi giá để ăn tiền "lại quả" (Kickbacks) giữa cán bộ thẩm định và nhà thầu. 8 cá nhân bị khởi tố!
\end{frame}

\begin{frame}{Đánh giá Rủi ro Văn hóa: Khung STPCM}
    \textbf{AI không chỉ quét con số, mà còn đánh giá cả "Văn hóa":}
    \begin{itemize}
        \item Mô hình kiểm toán mở rộng \textbf{STPCM}: 
            \begin{enumerate}
                \item Strategy (Chiến lược)
                \item Transaction (Giao dịch)
                \item Process (Quy trình)
                \item Culture (Văn hóa)
                \item Model (Mô hình)
            \end{enumerate}
        \item \textbf{Đánh giá Văn hóa (Culture) như thế nào?} Thông qua NLP, AI liên tục đọc tin nhắn chat nội bộ, email của doanh nghiệp.
    \end{itemize}
\end{frame}

\begin{frame}{Dấu hiệu Gian lận từ Giao tiếp Nội bộ}
    \begin{exampleblock}{Mầm mống của Gian lận}
        Nếu hệ thống nhận thấy một vị Giám đốc thường xuyên sử dụng các cụm từ:
        \begin{itemize}
            \item \textit{"Phải làm ngay, không được hỏi!"}
            \item \textit{"Đây là tài liệu tuyệt mật."}
            \item Hoặc liên tục \textbf{gửi email giao dịch vào lúc nửa đêm}.
        \end{itemize}
    \end{exampleblock}
    $\Rightarrow$ AI sẽ tự động chấm "Điểm rủi ro văn hóa" của phòng ban đó lên mức Đỏ, cảnh báo áp lực sai trái đang được tạo ra.
\end{frame}

\begin{frame}{Cuộc chạy đua Vũ trang Thuật toán}
    \begin{alertblock}{Vũ khí của Tội phạm Tài chính}
        \begin{itemize}
            \item Kế toán viên dùng AI để bắt gian lận, thì tội phạm cũng dùng **AI tạo sinh (GenAI)** để làm giả dữ liệu.
            \item Chúng dùng AI để tạo ra hàng ngàn giao dịch giả mạo, nhào nặn báo cáo tài chính sao cho qua mặt được các thuật toán thống kê thông thường.
        \end{itemize}
    \end{alertblock}
\end{frame}

\begin{frame}{Giải pháp Phòng thủ: Sự giao thoa ML \& NLP}
    \begin{itemize}
        \item Kẻ gian lận có thể làm giả những con số toán học hoàn hảo bằng AI...
        \item \textbf{Nhưng:} Việc dùng máy tính để giả mạo toàn bộ \textit{chuỗi logic giao tiếp email, ngôn ngữ văn bản tự nhiên, phong cách nói chuyện} cho khớp với số liệu tài chính trong thời gian dài là cực kỳ khó!
        \item AI của kiểm toán sẽ "bắt lỗi" từ chính sự bất đồng bộ giữa số liệu và ngữ cảnh văn bản.
    \end{itemize}
\end{frame}

\begin{frame}{Đào tạo Liên tục (Continuous Training)}
    \begin{itemize}
        \item Hệ thống chống gian lận không phải cài đặt một lần là xong.
        \item Kế toán viên phải liên tục nạp các chiêu thức lừa đảo mới (từ thị trường) vào mô hình.
        \item Quá trình này đòi hỏi một tư duy linh hoạt và sự am hiểu sâu sắc về vòng đời của dữ liệu.
    \end{itemize}
\end{frame}

\begin{frame}{Tái hiện Quy trình Khoa học Dữ liệu}
    \begin{columns}
        \column{0.4\textwidth}
        Đào tạo liên tục mô hình chống gian lận chính là Vòng đời Dự án Khoa học Dữ liệu:
        \begin{itemize}
            \item Thu thập chứng cứ mới.
            \item Làm sạch và Mô hình hóa.
            \item Đánh giá thuật toán.
            \item Triển khai giám sát 24/7.
        \end{itemize}
        
        \column{0.6\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_02B/Figure 6.4 Data science project lifecycle.jpeg}
            \caption{Vòng đời Dự án Khoa học Dữ liệu}
        \end{figure}
    \end{columns}
\end{frame}


% ==========================================
% SECTION 3: Ổn định Tài chính Vĩ mô & Kỷ nguyên XAI
% ==========================================
\section{Ổn định Tài chính Vĩ mô \& Kỷ nguyên XAI}

\begin{frame}{Sự Chuyển dịch Vĩ đại của Kế toán}
    \begin{block}{Từ Bác sĩ Pháp y...}
        Kiểm toán viên truyền thống giống như Bác sĩ Pháp y: Đi tìm nguyên nhân căn bệnh \textbf{sau khi} doanh nghiệp đã phá sản, tiền đã thất thoát.
    \end{block}
    \vspace{0.3cm}
    \begin{block}{...Sang Bác sĩ Y tế Dự phòng}
        Với AI, Kế toán viên tiến hóa thành Bác sĩ Dự phòng: Bắt bệnh, dự báo và \textbf{ngăn chặn} sự sụp đổ trước khi nó thực sự bùng phát.
    \end{block}
\end{frame}

\begin{frame}{Ổn định Tài chính Vĩ mô (Financial Stability)}
    \begin{itemize}
        \item Việc bắt được vài cá nhân tham nhũng trong công ty là tốt. Nhưng điều gì xảy ra nếu rủi ro đe dọa \textbf{toàn bộ hệ thống ngân hàng quốc gia}?
        \item Rủi ro lây lan (Contagion Effect) có thể nhấn chìm nền kinh tế.
        \item Ngân hàng Trung ương dùng GenAI để phân tích dữ liệu khổng lồ theo thời gian thực (Big Data) nhằm duy trì sự ổn định vĩ mô.
    \end{itemize}
\end{frame}

\begin{frame}{Ngăn chặn Bank Run qua App Điện thoại}
    \begin{itemize}
        \item Trong kỷ nguyên số, một cuộc rút tiền hàng loạt (Bank Run) không còn là cảnh người dân xếp hàng dài ngoài đường. 
        \item Nó diễn ra \textbf{âm thầm chỉ trong vài giờ} qua các ứng dụng Mobile Banking. Mạng xã hội thổi bùng sự hoảng loạn.
        \item Đợi đến báo cáo cuối tháng thì ngân hàng đã sập!
    \end{itemize}
\end{frame}

\begin{frame}{Giải pháp Ngăn chặn Bank Run bằng AI}
    \begin{itemize}
        \item AI được cấy trực tiếp vào hệ thống Core Banking của các ngân hàng thương mại.
        \item Theo dõi dòng thanh khoản theo từng phút, quét tin tức tiêu cực trên mạng xã hội.
        \item Cảnh báo ngay cho Ngân hàng Trung ương khi phát hiện sự sụt giảm tiền gửi đột biến, chặn đứng sự lây lan (Contagion) trước khi nó trở thành thảm họa.
    \end{itemize}
\end{frame}

\begin{frame}{Kiểm tra Sức chịu đựng (Stress Testing)}
    \begin{itemize}
        \item AI tạo ra hàng triệu kịch bản kinh tế khắc nghiệt (Ví dụ: Lạm phát tăng vọt + Đứt gãy chuỗi cung ứng toàn cầu).
        \item \textbf{Mục đích:} Đánh giá xem Bảng Cân đối Kế toán và Danh mục đầu tư của ngân hàng có chịu đựng nổi cú sốc đó hay không?
        \item Đảm bảo hệ thống ngân hàng luôn có đủ "tấm đệm vốn" an toàn.
    \end{itemize}
\end{frame}

\begin{frame}{Quản trị Quỹ Lương hưu \& Trợ lý Rô-bốt}
    \begin{itemize}
        \item \textbf{Vấn đề:} Hàng triệu hồ sơ hưu trí phức tạp, dễ bị trục lợi (báo tử muộn để lĩnh thêm tiền).
        \item \textbf{AI trong Quỹ Hưu trí:} Tự động thu thập dữ liệu người thụ hưởng, đối chiếu chéo với cơ sở dữ liệu quốc gia (khai sinh, khai tử).
        \item Cung cấp Trợ lý AI (Robo-advisors) giao tiếp 24/7 để tư vấn quyền lợi cho người lớn tuổi một cách thân thiện, chính xác.
    \end{itemize}
\end{frame}

\begin{frame}{Tương lai Kế toán: Có bị thay thế không?}
    \begin{alertblock}{Nỗi sợ hãi của Kế toán viên}
        Nhiều sinh viên lo sợ AI tự động hóa toàn bộ sổ sách sẽ cướp đi công việc của họ? Công nghệ AI Tạo sinh có thể tự hạch toán, tự lập báo cáo?
    \end{alertblock}
    \vspace{0.2cm}
    \begin{center}
        \Large \textbf{Sự thật: Kế toán viên không bị thay thế, mà họ phải TIẾN HÓA!}
    \end{center}
\end{frame}

\begin{frame}{Phi công điều khiển Siêu phi cơ AI}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item AI giải phóng kế toán khỏi việc gõ phím nhập liệu rườm rà.
            \item Kế toán viên hiện đại giống như những phi công: Bạn không cần trực tiếp chế tạo động cơ AI, nhưng bạn phải biết cách điều khiển bảng điều khiển khổng lồ này để vượt qua bão tố tài chính.
        \end{itemize}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_02B/Figure 6.2 Data scientist Venn diagram.jpeg}
            \caption{Giao thoa Năng lực mới}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Kỹ năng Sinh tồn 1: AI \& Data Literacy}
    \begin{itemize}
        \item \textbf{Hiểu biết về AI (AI Literacy):} Không cần code như kỹ sư phần mềm, nhưng phải hiểu dữ liệu được huấn luyện thế nào, đâu là thuật toán phân loại, đâu là NLP.
        \item \textbf{Làm chủ Dữ liệu (Data Management):} Biết một chút SQL hay Python để giao tiếp với hệ thống dữ liệu khổng lồ.
        \item Biết dùng Excel ngày xưa, tương đương với biết dùng Prompt AI và Python ngày nay!
    \end{itemize}
\end{frame}
    
\begin{frame}{Kỹ năng Sinh tồn 2: Tư duy Phản biện (Critical Thinking)}
    \begin{alertblock}{Tại sao lại cần Tư duy phản biện?}
        Vì AI hoàn toàn có thể Sai lầm! Máy móc chỉ đưa ra khuyến nghị dựa trên \textbf{xác suất thống kê}.
    \end{alertblock}
    \begin{itemize}
        \item Đôi khi AI đánh dấu một giao dịch là "gian lận" chỉ vì nó chưa từng thấy giao dịch đó trước đây.
        \item \textbf{Phán đoán nghề nghiệp:} Kế toán viên phải can thiệp để kết luận xem đó là hành vi phạm pháp, hay đơn giản là một chiến lược kinh doanh hoàn toàn mới của công ty.
    \end{itemize}
\end{frame}

\begin{frame}{Kỹ năng Sinh tồn 3: Đạo đức \& Minh bạch}
    \begin{itemize}
        \item Bảo mật dữ liệu nhạy cảm của khách hàng (Tuyệt đối không đẩy báo cáo tài chính mật lên ChatGPT hay các mô hình LLM công khai).
        \item Tránh những thiên lệch thuật toán (Algorithmic Bias) có thể dẫn đến phân biệt đối xử trong việc cấp tín dụng (do dữ liệu huấn luyện thiên vị chủng tộc, giới tính).
        \item Đảm bảo tuân thủ tiêu chuẩn an ninh thông tin ISO 27001.
    \end{itemize}
\end{frame}

\begin{frame}{Kỷ nguyên của Explainable AI (XAI)}
    \textbf{XAI - AI có khả năng giải thích (Trách nhiệm giải trình):}
    \begin{itemize}
        \item Nếu hệ thống AI từ chối duyệt khoản vay của một doanh nghiệp vừa và nhỏ, chúng ta không thể trả lời khách hàng rằng: \textit{"Vì phần mềm máy tính bảo thế!"}
        \item Kế toán viên phải dùng XAI để bóc trần "Hộp đen thuật toán", dịch kết quả đó thành ngôn ngữ kinh doanh: \textit{"Anh bị từ chối vì tỷ lệ đòn bẩy nợ quý 3 quá cao"}.
    \end{itemize}
\end{frame}

\begin{frame}{Suy ngẫm Cuối: AI điều hành Vĩ mô?}
    \begin{exampleblock}{Tương lai tự trị?}
        Liệu có một ngày, để loại bỏ hoàn toàn lòng tham và sự chậm trễ của con người, AI sẽ được cấp quyền \textbf{tự động điều chỉnh tỷ giá và lãi suất vĩ mô} ngay khi khủng hoảng chớm nở?
    \end{exampleblock}
\end{frame}

\begin{frame}{Đánh đổi giữa Tối ưu và Quyền Kiểm soát}
    \begin{itemize}
        \item Tự động chặn dòng tiền đầu cơ.
        \item Vô hiệu hóa khủng hoảng trước khi con người kịp chớp mắt.
        \item \textbf{Câu hỏi lớn:} Máy móc không hiểu được nỗi đau của sự sa thải hàng loạt. Chúng ta có sẵn sàng đánh đổi sự tối ưu tuyệt đối đó, để giao phó \textit{quyền kiểm soát sinh mệnh kinh tế} cho một cỗ máy vô cảm?
    \end{itemize}
\end{frame}

\begin{frame}{Tổng kết Bài học}
    \begin{itemize}
        \item AI biến kiểm toán từ chọn mẫu thụ động sang hệ thống phòng thủ toàn diện, phát hiện gian lận bằng Supervised, Unsupervised ML và NLP.
        \item Kế toán điều tra không chỉ soi số liệu, mà quét cả văn hóa độc hại ẩn sau những email công sở (Mô hình STPCM).
        \item Ở tầm vĩ mô, AI bảo vệ quốc gia khỏi Bank Run và khủng hoảng dây chuyền qua Stress Testing.
        \item \textbf{Tương lai:} Kế toán viên làm chủ XAI và Tư duy phản biện sẽ là những người dẫn dắt nền kinh tế số.
    \end{itemize}
\end{frame}

\begin{frame}
    \centering
    \Huge \textbf{Cảm ơn các bạn đã lắng nghe!}
    
    \vspace{0.5cm}
    \Large Hỏi \& Đáp
\end{frame}

\end{document}
"""
    output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "Slide_AIAcc_Day06.tex")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
        
    print(f"Generated {file_path}")

if __name__ == "__main__":
    create_beamer_slide()
