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

\title[TTNT trong Kế toán - Buổi 4]{Trí tuệ Nhân tạo Ứng dụng trong Kế toán}
\subtitle{Buổi 4: Phân khúc Thị trường \& Dự báo Sức khỏe Tài chính}
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
% SECTION 1: Phân khúc Khách hàng & Học không giám sát
% ==========================================
\section{Phân khúc Khách hàng \& Học không giám sát}

\begin{frame}{Mục tiêu \& Bối cảnh Bài học}
    \textbf{Chuyển mình từ Lý thuyết sang Thuật toán thực chiến:}
    \begin{itemize}
        \item \textbf{Phần 1:} Áp dụng Học không giám sát (Unsupervised Learning) để phân cụm \& tìm kiếm khách hàng tiềm năng.
        \item \textbf{Phần 2:} Áp dụng Hồi quy có phạt (Penalized Regression) để dự báo sức khỏe tài chính.
    \end{itemize}
    \vspace{0.5cm}
    \begin{block}{Case Study: Nhà hàng Vegan-Always tại Phoenix}
        Mới khai trương nhà hàng chay. Họ có nên phát phiếu giảm giá (voucher) cho \textit{tất cả} cư dân trong thành phố không?
        \begin{itemize}
            \item Lãng phí chi phí marketing.
            \item Gửi nhầm thông điệp cho người không có nhu cầu (ví dụ: người chỉ thích ăn thịt).
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}{Khái niệm Phân khúc Thị trường}
    \textbf{Phân khúc Thị trường (Market Segmentation)} là gì?
    \begin{itemize}
        \item Chia thị trường thành các nhóm khách hàng có đặc điểm tương đồng.
        \item Nhắm mục tiêu (Target) vào nhóm phù hợp nhất thay vì "tiếp thị đại chúng" (mass marketing).
    \end{itemize}
    \vspace{0.3cm}
    \textbf{Sự phát triển nhờ Dữ liệu \& AI:}
    \begin{itemize}
        \item \textbf{Vi phân khúc (Microsegments):} Tùy chỉnh ở cấp độ cực nhỏ nhờ dữ liệu hành vi (Amazon, Netflix).
        \item \textbf{Phân khúc Động (Dynamic Segmentation):} Sở thích thay đổi theo thời gian.
        \begin{itemize}
            \item \textit{Ví dụ:} Khách hàng từng mua sô-cô-la đen, giờ chuyển sang loại không đường vì lý do sức khỏe.
        \end{itemize}
    \end{itemize}
\end{frame}

\begin{frame}{Học Không giám sát (Unsupervised Learning) là gì?}
    Khi dữ liệu khách hàng không có sẵn nhãn (Unlabeled Data), làm sao để phân nhóm?
    \begin{itemize}
        \item Chúng ta chỉ có các "con số thô": Tuổi tác, thu nhập, thời gian duyệt web, số tiền chi tiêu.
        \item \textbf{Không có nhãn:} Không có cột nào ghi sẵn "Khách hàng mua" hay "Khách hàng bỏ đi".
    \end{itemize}
    \vspace{0.3cm}
    \begin{block}{Sứ mệnh của Học Không giám sát}
        Tự động "mò mẫm" trong đống dữ liệu hỗn độn để tìm ra \textbf{cấu trúc ẩn}. Thuật toán tiêu biểu nhất để làm việc này là \textbf{Phân cụm (Clustering)}.
    \end{block}
\end{frame}

% ==========================================
% SECTION 2: Thuật toán k-Means, k-Medoid & Hệ số Silhouette
% ==========================================
\section{Thuật toán k-Means, k-Medoid \& Hệ số Silhouette}

\begin{frame}{Thuật toán k-Means: Cơ chế Đo khoảng cách}
    \textbf{Mối quan hệ giữa Khoảng cách và Sự tương đồng:}
    \begin{itemize}
        \item Nếu coi mỗi khách hàng là một điểm trên trục tọa độ đa chiều.
        \item Khoảng cách giữa 2 điểm càng ngắn $\Rightarrow$ Hành vi tiêu dùng càng giống nhau.
    \end{itemize}
    \vspace{0.3cm}
    \begin{exampleblock}{Ví dụ: Bữa tiệc lộn xộn (k-Means Intuition)}
        \begin{enumerate}
            \item Chọn số lượng bàn tiệc ($k$). Đặt $k$ chiếc bàn ngẫu nhiên giữa phòng.
            \item \textbf{Gán điểm:} Khách tự động chạy đến chiếc bàn \textit{gần nhất}.
            \item \textbf{Cập nhật tâm:} Chiếc bàn lúc này bị lệch, người tổ chức phải khiêng bàn dời vào \textit{chính giữa} nhóm khách.
            \item Một số khách ở rìa thấy bàn khác gần hơn lại chạy sang nhóm khác $\Rightarrow$ Tiếp tục dời bàn.
            \item Lặp lại đến khi \textbf{không ai chuyển bàn nữa (Hội tụ)}.
        \end{enumerate}
    \end{exampleblock}
\end{frame}

\begin{frame}{Từ k-Means đến k-Medoid}
    \textbf{Điểm yếu của k-Means:}
    \begin{itemize}
        \item Tâm cụm (Centroid) được tính bằng \textit{giá trị trung bình (mean)}.
        \item Rất dễ bị nhiễu bởi các điểm ngoại lai (Outliers). Một khách hàng tỷ phú có thể kéo lệch toàn bộ tâm cụm.
    \end{itemize}
    \vspace{0.5cm}
    \textbf{Giải pháp: Thuật toán k-Medoid}
    \begin{itemize}
        \item Thay vì dùng trung bình, k-Medoid sử dụng một \textbf{điểm dữ liệu thực tế} (gọi là medoid) làm tâm.
        \item Chống nhiễu (Robust) tốt hơn nhiều so với k-Means trong dữ liệu Kế toán - Tài chính (vốn hay có số liệu đột biến).
    \end{itemize}
\end{frame}

\begin{frame}{Làm sao biết $k$ bằng bao nhiêu? (Hệ số Silhouette)}
    Thuật toán không tự biết nên chia thành 2, 3 hay 5 cụm. Chúng ta cần thước đo.
    \begin{block}{Hệ số Silhouette (Silhouette Width)}
        Chấm điểm dựa trên 2 tiêu chí:
        \begin{enumerate}
            \item \textbf{Độ gắn kết (Cohesion):} Các điểm trong cùng một cụm phải rất gần nhau.
            \item \textbf{Độ tách biệt (Separation):} Các cụm phải nằm cách xa nhau.
        \end{enumerate}
    \end{block}
    \begin{itemize}
        \item Điểm số Silhouette dao động từ -1 đến 1.
        \item Điểm số càng gần 1 chứng tỏ cấu trúc cụm rất chặt chẽ và lý tưởng.
    \end{itemize}
\end{frame}

\begin{frame}[fragile]{Thực hành R: Ứng dụng k-Means trong Phân khúc}
    Giả sử 2 biến: \textit{Số tiền chi tiêu} và \textit{Thời gian gắn bó}.
    \begin{lstlisting}[language=R]
library(cluster)
library(factoextra)

# Chuan hoa du lieu ve Z-score de dong nhat thang do
df <- scale(df, center = TRUE, scale = TRUE)

# Chay thuat toan k-Means voi k=3
k_means <- kmeans(df, centers = 3, nstart = 25)

# Ve bieu do hinh anh
fviz_cluster(k_means, data = df, repel = TRUE, 
             main = "k-means segmentation plot")
    \end{lstlisting}
    \textit{Kết quả kinh doanh:} Cụm 1 (Gắn bó lâu nhưng chi ít) vs Cụm 2 (Gắn bó lâu và chi tiêu nhiều $\rightarrow$ Khách hàng Vàng).
\end{frame}

\begin{frame}{Kết quả Trực quan: Biểu đồ k-Means}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Phân tích Biểu đồ (Hình 5.4):}
        \begin{itemize}
            \item Dữ liệu đã được gán vào 3 cụm riêng biệt.
            \item Mỗi màu sắc/hình dạng đại diện cho một phân khúc khách hàng.
            \item Doanh nghiệp nhìn vào đây để quyết định chiến lược Marketing riêng cho từng nhóm, tối ưu hóa ROI.
        \end{itemize}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_04A/Figure 5.4 k-Means Segmentation Plot.jpeg}
            \caption{k-Means Segmentation Plot}
        \end{figure}
    \end{columns}
\end{frame}

% ==========================================
% SECTION 3: Dự báo Phá sản, Đa cộng tuyến & Hồi quy LASSO
% ==========================================
\section{Dự báo Phá sản, Đa cộng tuyến \& Hồi quy LASSO}

\begin{frame}{Bảo vệ Sinh mệnh Doanh nghiệp: Dự báo Phá sản}
    Tìm khách hàng để tăng doanh thu là chưa đủ, nếu doanh nghiệp đang "chảy máu" từ bên trong.
    \begin{itemize}
        \item \textbf{Góc nhìn của Người cho vay (Ví dụ: Ngân hàng Altra):} 
        \item Cần đánh giá \textit{Sức khỏe Tài chính} trước khi duyệt khoản vay.
        \item Ngân hàng dùng hàng loạt các \textbf{Chỉ số tài chính}:
        \begin{itemize}
            \item Tỷ lệ nợ/Vốn chủ sở hữu (Debt-to-Equity Ratio).
            \item Tỷ lệ thanh toán hiện hành (Current Ratio).
            \item Tỷ lệ hoạt động (Operating Ratio).
        \end{itemize}
    \end{itemize}
    \vspace{0.3cm}
    \textit{Tuy nhiên, sử dụng hàng chục tỷ lệ tài chính cùng lúc lại sinh ra một "căn bệnh" nguy hiểm trong Thống kê.}
\end{frame}

\begin{frame}{Căn bệnh "Đa cộng tuyến" (Multicollinearity)}
    \begin{block}{Hiện tượng Đa cộng tuyến là gì?}
        Xảy ra khi các biến độc lập (predictors) có \textbf{tương quan cực kỳ chặt chẽ} với nhau. Thông tin bị lặp lại.
    \end{block}
    \begin{exampleblock}{Ví dụ: Lái xe với 5 chiếc GPS}
        \begin{itemize}
            \item Đa cộng tuyến giống như việc bạn lái xe và bật 5 chiếc GPS cùng lúc.
            \item Chúng gào thét chỉ đường, chỉ khác nhau một xíu. Thay vì đến đích, sự nhiễu loạn làm bạn hoảng loạn và đâm xe.
            \item \textbf{Hậu quả với Hồi quy cổ điển (OLS):} Sai số chuẩn tăng vọt, bỏ qua cảnh báo nguy hiểm thực sự (Sai lầm loại II).
        \end{itemize}
    \end{exampleblock}
\end{frame}

\begin{frame}{Phát hiện Đa cộng tuyến qua Biểu đồ Tương quan}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Phân tích Biểu đồ (Hình 10.2):}
        \begin{itemize}
            \item Có những chỉ số tài chính tương quan tới $> 0.9$ (ví dụ: marketing\_ratio\_1 và earning\_ratio\_2).
            \item Hệ số VIF (Variance Inflation Factor) của một số tỷ lệ lên tới \textbf{600} (Đa cộng tuyến ở mức thảm họa).
        \end{itemize}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_04B/Figure 10.2 Correlation Plot.jpeg}
            \caption{Ma trận tương quan các chỉ số tài chính}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Giải pháp AI: Hồi quy có phạt \& Mô hình LASSO}
    \textbf{Thuật toán LASSO (Least Absolute Shrinkage and Selection Operator)}
    \begin{itemize}
        \item Không dùng OLS cổ điển nữa. Chuyển sang \textbf{Hồi quy có phạt (Penalized Regression)}.
        \item \textbf{Cơ chế Trừng phạt ($\lambda$):} 
        \begin{itemize}
            \item Thuật toán ép các hệ số ($\beta$) của những biến không quan trọng (hoặc gây nhiễu) nhỏ dần.
            \item Đỉnh cao của LASSO: Ép các hệ số đó về \textbf{đúng bằng 0}.
        \end{itemize}
        \item \textbf{Tự động Lựa chọn Biến (Variable Selection):} 
        \begin{itemize}
            \item Ngân hàng đo 16 tỷ số. LASSO "thanh trừng" 4 tỷ số gây nhiễu (ép về 0), chỉ giữ lại 12 tỷ số thực sự cốt lõi để dự báo.
        \end{itemize}
    \end{itemize}
\end{frame}

\begin{frame}{Đánh giá Mô hình: Đường cong AUC ROC}
    Làm sao Ngân hàng biết mô hình dự báo phá sản đủ tốt để giao tiền?
    \begin{block}{Đường cong ROC \& Hệ số AUC}
        \begin{itemize}
            \item Trục Y: \textbf{True Positive (Đoán đúng phá sản)}.
            \item Trục X: \textbf{False Positive (Báo động nhầm)}.
            \item \textbf{AUC = 0.5:} Đoán bừa (như tung đồng xu).
            \item \textbf{AUC = 1.0:} Hoàn hảo tuyệt đối.
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}{Kết quả Đánh giá Mô hình LASSO}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Phân tích Biểu đồ (Hình 10.4):}
        \begin{itemize}
            \item Mô hình LASSO đạt \textbf{AUC $\approx$ 0.8}.
            \item Khá ấn tượng! Ngân hàng hoàn toàn tự tin nhập số liệu của công ty mới vào. 
            \item Kết quả xuất ra: 0 (Sắp phá sản, từ chối vay) hoặc 1 (An toàn, duyệt vay).
        \end{itemize}
        
        \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.9\textwidth]{../../Figures/Buoi_04B/Figure 10.4 AUC ROC Curve.jpeg}
            \caption{Đường cong AUC ROC (0.8)}
        \end{figure}
    \end{columns}
\end{frame}

\begin{frame}{Tổng kết: Sự va chạm giữa Con người \& Máy móc}
    \textbf{Tương lai của ngành Kế toán - Tài chính:}
    \begin{itemize}
        \item \textbf{Hôm nay:} AI đã chứng minh khả năng dẹp bỏ nhiễu loạn (LASSO) và gom nhóm khách hàng xuất sắc (k-Means) từ \textit{Big Data}.
        \item \textbf{Câu hỏi Mở:} Nếu dự báo của mô hình LASSO mâu thuẫn hoàn toàn với trực giác của một Kế toán trưởng có 20 năm kinh nghiệm. Chúng ta nên nghe ai?
        \item Tương lai không phải là \textit{phục tùng AI}, mà Kế toán viên phải học cách \textbf{diễn dịch, tranh luận và kiểm soát} các thuật toán này.
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
    file_path = os.path.join(output_dir, "Slide_AIAcc_Day04.tex")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
        
    print(f"Generated {file_path}")

if __name__ == "__main__":
    create_beamer_slide()
