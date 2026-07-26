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
\usepackage{listings}
\usepackage{amsmath}

% Cấu hình giao diện Beamer
\usetheme{Madrid}
\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}[frame number]

% Cấu hình màu cho code
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}
\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}
\lstset{style=mystyle}

\title[TTNT trong Kế toán - Buổi 5]{Trí tuệ Nhân tạo Ứng dụng trong Kế toán}
\subtitle{Buổi 5: Quản trị Rủi ro Quyết định \& Phát triển Sản phẩm Mới}
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
% SECTION 1: Bất định trong Chuỗi Cung ứng & Cây Quyết định
% ==========================================
\section{Bất định trong Chuỗi Cung ứng \& Cây Quyết định}

\begin{frame}{Sự Bất định trong Kinh doanh}
    \textbf{Kế toán không chỉ là ghi chép quá khứ:}
    \begin{itemize}
        \item Báo cáo tài chính phản ánh những con số rõ ràng, rành mạch.
        \item Nhưng thế giới kinh doanh thực tế luôn biến động và \textit{bất định (uncertainty)}.
    \end{itemize}
    \vspace{0.3cm}
    \begin{block}{Tình huống: Đứt gãy nguồn cung Smartphone}
        Nửa đêm, một chuỗi bán lẻ công nghệ nhận được thông báo: Nguồn cung smartphone hot nhất mùa sẽ bị cắt giảm một nửa.
        \begin{itemize}
            \item Trả hàng và mất doanh thu?
            \item Hay tiếp tục nhận đơn (Backorder) và hứa giao sau?
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}{Tình trạng Chậm giao hàng (Backorder)}
    \textbf{Nhận đơn nhưng không có sẵn hàng:}
    \begin{itemize}
        \item Nghe có vẻ giống một chiến lược giữ chân khách hàng thông minh.
        \item Nhưng thực tế, nó là một \textbf{mồi lửa} châm ngòi cho sự sụp đổ niềm tin.
    \end{itemize}
    \vspace{0.3cm}
    \textbf{Hậu quả:}
    \begin{itemize}
        \item Người tiêu dùng trải qua cảm giác chực chờ sẽ hiếm khi quay lại mua sắm.
        \item Giữ được đơn hàng hôm nay, nhưng vĩnh viễn mất đi khách hàng đó trong tương lai.
    \end{itemize}
\end{frame}

\begin{frame}{Thảm họa: Hiệu ứng chiếc roi da (Bullwhip Effect)}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Cơn sốt giấy vệ sinh:}
        \begin{itemize}
            \item Một vài khách hàng mua dư (sự hoảng loạn nhỏ).
            \item Siêu thị thấy kệ trống $\Rightarrow$ Đặt \textbf{gấp đôi} từ nhà phân phối.
            \item Nhà phân phối tưởng nhu cầu bùng nổ $\Rightarrow$ Đặt \textbf{gấp bốn} từ nhà máy.
            \item Nhà máy sản xuất hết công suất $\Rightarrow$ Vài tháng sau \textbf{ế ẩm}.
        \end{itemize}
        \textit{Một tiếng thì thầm của khách hàng biến thành tiếng hét hoảng loạn ở cuối chuỗi cung ứng.}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_05A/Figure 12.1 Bullwhip Effect.jpeg}
            \caption{Hiệu ứng chiếc roi da}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Tập dữ liệu mất cân bằng (Imbalanced Data)}
    Để ngăn chặn "tiếng hét hoảng loạn", chúng ta cần \textbf{dự báo} chính xác khi nào thì tình trạng Backorder thực sự xảy ra.
    \vspace{0.3cm}
    \begin{block}{Thách thức Dữ liệu: Sự mất cân bằng}
        \begin{itemize}
            \item Có hàng triệu đơn hàng được giao trơn tru.
            \item Chỉ có vài trăm đơn hàng bị thiếu hụt.
            \item Tỷ lệ bình thường \textit{áp đảo hoàn toàn} sự bất thường.
        \end{itemize}
    \end{block}
    \textit{Khi đưa tập dữ liệu này vào mô hình thống kê truyền thống, chúng sẽ hoàn toàn vô dụng!}
\end{frame}

\begin{frame}{Học Máy: Cây Quyết định (Decision Tree)}
    \begin{columns}
        \column{0.5\textwidth}
        Khắc tinh của những tập dữ liệu mất cân bằng chính là Học Máy, khởi đầu với \textbf{Cây Quyết định}.
        \begin{itemize}
            \item Một công cụ phân loại đơn giản.
            \item Dùng các biến số như \textit{Dự báo doanh số}, \textit{Thời gian vận chuyển} để rẽ nhánh.
            \item Đưa ra dự đoán: Hàng có bị thiếu (Yes) hay không (No).
        \end{itemize}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_05A/Figure 12.2 Components of a Decision Tree.jpeg}
            \caption{Cấu trúc Cây Quyết định}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Phân chia Nút gốc bằng Chỉ số Gini (Gini Impurity)}
    \begin{columns}
        \column{0.5\textwidth}
        Làm sao để biết biến nào phân loại tốt hơn?
        \begin{itemize}
            \item Tính \textbf{Độ vẩn đục Gini}. Giá trị càng thấp càng tốt.
            \item Ví dụ: Chia theo \textit{Doanh số dự báo} có tách được các đơn bị chậm giao tốt hơn không?
            \item Kết quả: Doanh số dự báo có chỉ số Gini thấp hơn (0.34) $\Rightarrow$ Chọn làm nút gốc.
        \end{itemize}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.85\textwidth]{../../Figures/Buoi_05A/Figure 12.3 Gini Index Calculation.jpeg}
            \caption{Tính toán Chỉ số Gini}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Kết quả: Sơ đồ Cây Phân loại}
    \begin{columns}
        \column{0.4\textwidth}
        \textbf{Phân tích Cây (Hình 12.5):}
        \begin{itemize}
            \item Nút gốc đầu tiên: Doanh số dự báo (Cao/Thấp).
            \item Rẽ nhánh tiếp theo: Thời gian vận chuyển (Cao/Thấp).
            \item Đến lá cuối cùng: Kết luận Có bị Backorder hay Không.
        \end{itemize}
        
        \column{0.6\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_05A/Figure 12.5 Decision Tree Splits.jpeg}
            \caption{Sơ đồ Cây Phân loại}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Điểm yếu chí mạng của Cây Quyết định đơn lẻ}
    \begin{alertblock}{Quá nhạy cảm và Dễ bị đánh lừa!}
        \begin{itemize}
            \item Cây quyết định đơn lẻ rất \textit{yếu ớt}.
            \item Thay đổi dữ liệu huấn luyện một chút xíu, cây sẽ mọc ra những nhánh hoàn toàn khác biệt.
            \item Dẫn đến dự báo sai lệch trầm trọng khi áp dụng vào thực tế.
        \end{itemize}
    \end{alertblock}
    \vspace{0.3cm}
    $\Rightarrow$ Cần một giải pháp mạnh mẽ hơn để khắc phục sự yếu ớt này.
\end{frame}

% ==========================================
% SECTION 2: Rừng ngẫu nhiên & Đánh giá Mô hình
% ==========================================
\section{Rừng ngẫu nhiên (Random Forest) \& Đánh giá Mô hình}

\begin{frame}{Giải pháp đột phá: Rừng ngẫu nhiên (Random Forest)}
    \textbf{Thuật toán Rừng Ngẫu Nhiên} là tập hợp của hàng trăm cây quyết định. Nó giải quyết sự yếu ớt bằng 2 cơ chế:
    \vspace{0.3cm}
    \begin{block}{1. Bootstrap Aggregation (Bagging)}
        \begin{itemize}
            \item Thay vì đưa toàn bộ dữ liệu cho tất cả các cây cùng học.
            \item Thuật toán bốc \textbf{ngẫu nhiên một phần dữ liệu} (có hoàn lại) cho một cây, rồi bốc phần khác cho cây tiếp theo.
            \item Tạo ra sự đa dạng hóa góc nhìn.
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}{Cơ chế 2: Lấy mẫu không gian con (Subspace Sampling)}
    \begin{exampleblock}{Ẩn dụ: 100 Bác sĩ Hội chẩn}
        \begin{itemize}
            \item Nếu đưa cùng 1 bộ hồ sơ bệnh án cho 100 bác sĩ, họ đều có xu hướng chỉ nhìn vào triệu chứng rõ nhất (ví dụ: ho dữ dội) và ra \textit{cùng một kết luận}.
            \item \textbf{Giải pháp:} Cố tình \textit{giấu đi một vài kết quả xét nghiệm} (ví dụ: giấu X-Quang người này, giấu chỉ số huyết áp người kia).
            \item \textbf{Hiệu quả:} Ép các bác sĩ (cây quyết định) phải \textbf{suy nghĩ độc lập}, đào sâu tìm manh mối từ những triệu chứng mờ nhạt.
        \end{itemize}
    \end{exampleblock}
    Tập hợp quyết định độc lập của 100 bác sĩ $\Rightarrow$ \textbf{Sức mạnh của đám đông (Wisdom of the crowd)}.
\end{frame}

\begin{frame}{Căn bệnh "Lười biếng" của Mô hình}
    \textbf{Quay lại với Tập dữ liệu mất cân bằng:} (99\% giao hàng thành công, 1\% Backorder).
    \begin{itemize}
        \item Nếu để mô hình tự học, nó sẽ nhận ra một \textit{quy luật khôn lỏi}.
        \item Nó chỉ cần \textbf{đoán bừa} là "Không bao giờ thiếu hàng".
        \item Tỷ lệ chính xác (Accuracy) vẫn đạt \textbf{99\%}!
    \end{itemize}
    \vspace{0.3cm}
    \begin{alertblock}{Gian lận bài thi}
        Giống như việc đánh lụi toàn bộ một đáp án A để chắc chắn được 9 điểm, mà không cần học bài.
    \end{alertblock}
\end{frame}

\begin{frame}{Xử lý Lười biếng: Lấy mẫu giảm (Downsampling)}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Ép mô hình vào chân tường:}
        \begin{itemize}
            \item Thuật toán chủ động \textit{cắt bỏ bớt} lượng dữ liệu khổng lồ của nhóm giao hàng thành công.
            \item Ép tỷ lệ xuống sao cho nhóm bình thường chỉ nhỉnh hơn nhóm thiếu hụt một chút (khoảng 1.5 lần).
            \item Mô hình bị tước đi lợi thế, buộc phải thực sự học cách nhận diện đặc trưng của ca thiếu hụt.
        \end{itemize}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_05A/Figure 12.6 Data Imbalance.jpeg}
            \caption{Dữ liệu Mất cân bằng}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Các chỉ số đánh giá thực sự}
    Vì Accuracy đã trở nên vô nghĩa (do gian lận), chúng ta cần một "Bảng điểm" mới khắc nghiệt hơn.
    \begin{block}{1. Độ nhạy (Sensitivity - Tỷ lệ Dương tính Thật)}
        \begin{itemize}
            \item Khả năng \textbf{đánh hơi trúng phóc} những ca thực sự bị thiếu hụt hàng hóa.
            \item Nếu độ nhạy thấp = Bỏ lọt tội phạm / Bắt hụt bệnh.
        \end{itemize}
    \end{block}
    \begin{block}{2. Độ đặc hiệu (Specificity - Tỷ lệ Âm tính Thật)}
        \begin{itemize}
            \item Khả năng \textbf{không đưa ra báo động giả}.
            \item Nếu độ đặc hiệu thấp = Cảnh báo nhầm những đơn hàng đang giao suôn sẻ $\Rightarrow$ Mất chi phí dự phòng vô ích.
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}{Đường cong ROC \& Chỉ số AUC}
    \begin{itemize}
        \item \textbf{AUC ROC (Area Under the Receiver Operating Characteristic Curve):} Bảng điểm đánh giá từ 0 đến 1.
        \item Đánh giá đồng thời cả Độ nhạy và Độ đặc hiệu.
        \item \textbf{AUC càng gần 1:} Mô hình càng xuất sắc trong việc phân loại \textit{thực sự}, hoàn toàn loại bỏ yếu tố đoán bừa.
    \end{itemize}
    \vspace{0.3cm}
    \textit{Rừng ngẫu nhiên kết hợp Downsampling tạo ra mô hình có AUC cực kỳ ấn tượng, xử lý mượt mà hiện tượng nhiễu và đa cộng tuyến trong chuỗi cung ứng!}
\end{frame}

% ==========================================
% SECTION 3: Phát triển Sản phẩm Mới & Thử nghiệm A/B
% ==========================================
\section{Phát triển Sản phẩm Mới \& Thử nghiệm A/B}

\begin{frame}{Chuyển giao: Sự Bất định từ Nội bộ}
    Rừng ngẫu nhiên là tấm khiên hoàn hảo bảo vệ doanh nghiệp khỏi thế giới bên ngoài (Bão lụt, đứt gãy Logistic).
    \vspace{0.3cm}
    \textbf{Nhưng nếu nguồn cơn sự hỗn loạn đến từ quyết định của Ban giám đốc?}
    \begin{itemize}
        \item Đổi hẳn cốt truyện của một tựa game?
        \item Tung ra một giao diện ứng dụng mới toanh?
    \end{itemize}
    \textit{Chúng ta không có dữ liệu lịch sử để dự báo cho một sản phẩm chưa từng tồn tại!}
    \vspace{0.3cm}
    $\Rightarrow$ Chuyển từ Dự báo (Predictive Modeling) sang \textbf{Thử nghiệm Nhân quả (Causal Experimentation)}.
\end{frame}

\begin{frame}{Cạm bẫy Thống kê: Tương quan Giả tạo}
    \begin{alertblock}{Sự khác biệt giữa Tương quan (Correlation) và Nhân quả (Causation)}
        Dữ liệu có thể cho thấy: \textit{Số lượng người ăn kem tăng lên cùng lúc với số vụ cháy rừng.}
    \end{alertblock}
    \begin{itemize}
        \item Cả hai biến cùng tăng (Tương quan toán học).
        \item Nhưng ăn kem \textbf{không gây ra} cháy rừng! (Nguyên nhân thực sự là mùa hè nhiệt độ cao).
        \item Nếu ra quyết định kinh doanh chỉ dựa trên tương quan bề mặt, doanh nghiệp đang ném tiền qua cửa sổ.
    \end{itemize}
\end{frame}

\begin{frame}{Thiên kiến Tự chọn (Self-Selection Bias)}
    \begin{exampleblock}{Ví dụ: Giao diện game màu Xanh nước biển}
        \begin{itemize}
            \item Dữ liệu cho thấy: Người dùng giao diện Xanh nước biển chi nhiều tiền mua vật phẩm hơn người dùng màu Đỏ.
            \item \textbf{Kết luận sai:} Màu xanh kích thích mua sắm $\Rightarrow$ Ép mọi người dùng màu xanh.
            \item \textbf{Sự thật:} Game cho phép người chơi \textit{tự chọn} màu. Vô tình, các game thủ VIP "bạo chi" lại có gu thẩm mỹ thích màu xanh.
            \item Màu xanh chỉ là dấu hiệu đi kèm, không có "ma lực" thôi miên khách hàng rút ví!
        \end{itemize}
    \end{exampleblock}
\end{frame}

\begin{frame}{Giải pháp: Thử nghiệm A/B (A/B Testing)}
    \begin{columns}
        \column{0.5\textwidth}
        Yếu tố sống còn của A/B Test là \textbf{Sự Phân bổ Ngẫu nhiên (Randomization)}.
        \begin{itemize}
            \item Tước đi quyền "tự chọn" của người dùng.
            \item Ném ngẫu nhiên 50\% người dùng vào màu Xanh, 50\% vào màu Đỏ.
            \item Cào bằng mọi yếu tố nhiễu (Người giàu, người nghèo chia đều 2 bên).
        \end{itemize}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_05B/Figure 14.1 New Product Development Process.jpeg}
            \caption{Quy trình Phát triển Sản phẩm}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Kiểm định Thống kê: Giả thuyết Không}
    Công ty Game tạo ra 3 nguyên mẫu (Mức độ khó: Dễ - Trung bình - Khó) để xem người chơi gắn bó với bản nào lâu nhất.
    \begin{block}{Giả thuyết Không (Null Hypothesis)}
        \begin{itemize}
            \item Tưởng tượng Giả thuyết Không là một \textbf{gã giám khảo cực kỳ bảo thủ}.
            \item Hắn khoanh tay bĩu môi nói: \textit{"Chẳng có mức độ khó nào tạo ra khác biệt. Mọi biến động thời gian chơi chỉ là do ăn may ngẫu nhiên!"}
        \end{itemize}
    \end{block}
    Nhiệm vụ của phân tích dữ liệu là phải đập tan sự hoài nghi của gã giám khảo này.
\end{frame}

\begin{frame}{Phân tích Phương sai (ANOVA) \& Kiểm định F}
    Không dùng Test thông thường (sẽ gây báo động nhầm - False Positive). Ta dùng \textbf{ANOVA (Phân tích Phương sai) và F-Test}.
    \vspace{0.3cm}
    F-Test đặt 2 thứ lên bàn cân:
    \begin{enumerate}
        \item \textbf{Sự khác biệt giữa các nhóm:} Do tác động của Mức độ khó Game.
        \item \textbf{Sự khác biệt bên trong nội bộ nhóm:} Do cá tính người chơi (Người rảnh rỗi vs Người bận rộn).
    \end{enumerate}
    $\Rightarrow$ Nếu sự khác biệt giữa các nhóm \textit{lấn át hoàn toàn} nhiễu loạn nội bộ, hệ thống sẽ kết luận: Sự chênh lệch là có thật!
\end{frame}

\begin{frame}{Sức mạnh của Giá trị P (P-value)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Kết quả trả về một con số quyền lực: \textbf{P-value}.
            \item Nếu \textbf{P-value < 0.05}: Xác suất để "gã giám khảo bảo thủ" đúng đã rơi xuống dưới 5\%.
            \item Ta đủ cơ sở khoa học để bác bỏ Giả thuyết Không.
            \item Quyết định kinh doanh không còn là cãi vã trong phòng họp, mà tự tin tung ra phiên bản chiến thắng!
        \end{itemize}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_05B/Figure 14.2 A Boxplot of Time Spent With Different Prototypes.jpeg}
            \caption{So sánh Thời gian tương tác (Boxplot)}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Tổng kết Buổi học}
    \textbf{Trí tuệ Nhân tạo \& Thống kê - Tấm khiên bảo vệ doanh nghiệp:}
    \begin{itemize}
        \item \textbf{Rừng ngẫu nhiên:} Lung sục nguy cơ đứt gãy chuỗi cung ứng mờ nhạt nhất.
        \item \textbf{Thử nghiệm A/B:} Dập tắt sự hoài nghi và cảm tính của Ban giám đốc.
        \item AI không thay thế con người vạch ra tầm nhìn, nhưng cung cấp nền tảng thực chứng để những ý tưởng đó không trở thành canh bạc mù quáng.
    \end{itemize}
    \vspace{0.5cm}
    \begin{center}
        \Large Liệu rủi ro bằng Không có triệt tiêu sự sáng tạo? Đó là câu hỏi mở cho thế hệ Kế toán chiến lược!
    \end{center}
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
    file_path = os.path.join(output_dir, "Slide_AIAcc_Day05.tex")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
        
    print(f"Generated {file_path}")

if __name__ == "__main__":
    create_beamer_slide()
