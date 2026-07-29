import os

tex_content = r"""\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}
\usecolortheme{default}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{booktabs}

\setbeamertemplate{caption}[numbered]
\renewcommand{\figurename}{Hình}

\title[Buổi 5: AI \& Forensic Accounting]{Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.3cm} \Large Buổi 5: AI Phát hiện sai sót \& Chẩn đoán bất thường}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

% SLIDE 1
\begin{frame}
    \titlepage
    \begin{center}
        \includegraphics[width=0.5\textwidth,height=2.5cm,keepaspectratio]{images/Day_05/bg_day5_lt.png}
    \end{center}
\end{frame}

% SLIDE 2
\begin{frame}{Năng lực đạt được sau buổi học}
    \begin{itemize}
        \item \textbf{Về Lý thuyết (LT):} Hiểu được bản chất của sai sót/gian lận (Outliers) và cách AI (như LOF) tự động khoanh vùng rủi ro thay cho kiểm tra chọn mẫu.
        \item \textbf{Về Thực hành (TH):} Ứng dụng thành thạo Excel (Conditional Formatting) và Power BI kết hợp Prompt AI để quét Sổ Nhật ký chung, phát hiện nhanh các giao dịch đáng ngờ.
        \item \textbf{Về Tư duy nghề nghiệp:} Hình thành sự "hoài nghi nghề nghiệp", hiểu được giới hạn của AI (báo động giả) và trách nhiệm kiểm chứng của kế toán viên.
    \end{itemize}
\end{frame}

% SLIDE 4
\begin{frame}{Nội dung bài học}
    \tableofcontents
\end{frame}

\section{1. Kế toán điều tra và Sự can thiệp của AI}

% SLIDE 5
\begin{frame}{Kế toán điều tra (Forensic Accounting) là gì?}
    \begin{itemize}
        \item \textbf{Định nghĩa:} Kế toán điều tra là công việc sử dụng các kỹ năng kế toán, kiểm toán và điều tra để kiểm tra tính hợp lệ của các giao dịch tài chính.
        \item Họ giống như những \textbf{"Thám tử tài chính"} (Financial Detectives).
        \item Mục đích: Tìm kiếm các bằng chứng về gian lận (Fraud) có thể sử dụng trước tòa án.
    \end{itemize}
\end{frame}

% SLIDE 6
\begin{frame}{Các loại gian lận phổ biến trong doanh nghiệp}
    \begin{itemize}
        \item Rút ruột công quỹ (Embezzlement).
        \item Lạm dụng thẻ tín dụng công ty (Corporate credit card fraud).
        \item Trốn thuế / Gian lận thuế (Tax Evasion).
        \item Khai khống doanh thu / Ẩn giấu nợ vay để làm đẹp BCTC.
        \item Rửa tiền (Money Laundering).
    \end{itemize}
\end{frame}

% SLIDE 7
\begin{frame}{Hậu quả của gian lận tài chính}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Mặc dù số lượng giao dịch gian lận chiếm tỷ lệ rất nhỏ so với tổng giao dịch hợp lệ.
            \item Nhưng chúng gây thiệt hại \textbf{hơn 5 nghìn tỷ USD} mỗi năm cho nền kinh tế toàn cầu.
            \item Tổn thất về uy tín, sụp đổ doanh nghiệp (VD: Enron, Wirecard).
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_05/fraud_stats.png}
    \end{columns}
\end{frame}

% SLIDE 8
\begin{frame}{Phương pháp rà soát thủ công truyền thống}
    \begin{itemize}
        \item \textbf{Quá khứ:} Kế toán viên/Kiểm toán viên phải dò từng chứng từ, hóa đơn giấy.
        \item \textbf{Hạn chế:}
        \begin{itemize}
            \item Tốn cực kỳ nhiều thời gian và nguồn lực.
            \item Chỉ có thể \textbf{chọn mẫu ngẫu nhiên} (Random Sampling), không thể kiểm tra 100\% sổ cái.
            \item Dễ bỏ sót các thủ đoạn gian lận tinh vi do con người dễ mệt mỏi.
        \end{itemize}
    \end{itemize}
\end{frame}

% SLIDE 9
\begin{frame}{Vai trò của Machine Learning/AI}
    \begin{itemize}
        \item \textbf{Tự động hóa hoàn toàn:} Chuyển từ kiểm tra chọn mẫu sang kiểm tra \textbf{toàn bộ 100\%} dữ liệu trong thời gian thực.
        \item Tốc độ: AI có thể xử lý hàng triệu dòng sổ cái chỉ trong vài giây.
        \item Khả năng học hỏi: AI học cách phân biệt giữa một giao dịch "bình thường" và một giao dịch "đáng ngờ" từ dữ liệu trong quá khứ hoặc cấu trúc dữ liệu hiện tại.
    \end{itemize}
\end{frame}

\section{2. Hiểu về "Điểm bất thường" (Outliers)}

% SLIDE 10
\begin{frame}{Điểm bất thường (Outliers) là gì?}
    \begin{itemize}
        \item \textbf{Định nghĩa:} Outliers là những quan sát (dữ liệu) khác biệt quá lớn so với các quan sát khác, gây ra sự nghi ngờ rằng chúng được tạo ra bởi một cơ chế hoàn toàn khác.
        \item Trong kế toán, một giao dịch Outlier không phải là lỗi ngẫu nhiên, mà nó có thể là \textbf{kết quả của một hành vi có chủ đích} (gian lận).
    \end{itemize}
\end{frame}

% SLIDE 11
\begin{frame}{Outliers vs Noise (Nhiễu)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Nhiễu (Noise):} Do sai sót ngẫu nhiên trong quá trình nhập liệu (VD: gõ dư một số 0). Thường không mang lại thông tin hữu ích và cần được làm sạch (Data processing).
            \item \textbf{Bất thường (Outliers):} Do quá trình phát sinh giao dịch bị thay đổi (VD: kẻ gian cố tình sửa số liệu). \textbf{Rất có giá trị} vì nó hé lộ bản chất của vấn đề.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_05/outlier_vs_noise.png}
    \end{columns}
\end{frame}

% SLIDE 12
\begin{frame}{Ví dụ về Outlier trong Kế toán}
    \textbf{Tình huống:}
    \begin{itemize}
        \item Một nhân viên bán hàng thường xuyên dùng thẻ tín dụng công ty để tiếp khách. 
        \item Các khoản chi tiêu trung bình luôn dao động từ 5 triệu đến 20 triệu VNĐ/tháng.
        \item Đột nhiên, tháng này có một hóa đơn quẹt thẻ tại Cửa hàng trang sức với số tiền \textbf{500 triệu VNĐ}.
    \end{itemize}
    $\rightarrow$ Đây là một Outlier điển hình cảnh báo rủi ro lạm dụng công quỹ.
\end{frame}

% SLIDE 13
\begin{frame}{Phương pháp nhận diện toàn cục (Global Outlier Detection)}
    \begin{itemize}
        \item \textbf{Quy tắc 3 độ lệch chuẩn (3SD Rule):} Trong phân phối chuẩn, bất kỳ dữ liệu nào nằm cách giá trị trung bình quá 3 lần độ lệch chuẩn đều bị coi là Outlier.
        \item Phương pháp này coi toàn bộ tập dữ liệu được sinh ra từ \textbf{cùng một quy luật} (Một cơ chế chung).
    \end{itemize}
\end{frame}

% SLIDE 14
\begin{frame}{Hạn chế của phương pháp toàn cục}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Kế toán là tập hợp của nhiều bộ phận (Sản xuất, Bán hàng, Quản lý). Mỗi bộ phận có quy luật chi tiêu khác nhau.
            \item Phương pháp toàn cục (Global) dễ bị sai số khi các điểm bất thường \textbf{tụ tập thành một đám} (Cluster), chúng sẽ tự che dấu nhau (Masking) và qua mặt hệ thống.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_05/global_vs_local.png}
    \end{columns}
\end{frame}

% SLIDE 15
\begin{frame}{Khái niệm Nhận diện cục bộ (Local Outlier Detection)}
    \begin{itemize}
        \item Giải pháp: Đánh giá một giao dịch có bất thường hay không \textbf{dựa vào những giao dịch tương tự xung quanh nó} (Neighborhood).
        \item Nếu một khoản chi phí tiếp khách bị xem là bất thường, không phải đem so với chi phí mua nguyên vật liệu, mà phải so với các khoản tiếp khách của chính phòng ban đó.
    \end{itemize}
\end{frame}

\section{3. Trực giác về thuật toán LOF (Local Outlier Factor)}

% SLIDE 16
\begin{frame}{LOF (Local Outlier Factor) là gì?}
    \begin{itemize}
        \item LOF là một thuật toán AI phổ biến giúp tìm ra các điểm bất thường mang tính cục bộ.
        \item Thay vì kết luận cứng nhắc "Có/Không", LOF chấm cho mỗi giao dịch một \textbf{Điểm số bất thường (LOF Score)}.
    \end{itemize}
\end{frame}

% SLIDE 17
\begin{frame}{Ví dụ trực quan về LOF (Ngôi nhà trong thung lũng)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Hãy tưởng tượng một thị trấn có 99 ngôi nhà nằm san sát nhau dưới \textbf{thung lũng}.
            \item Chỉ có 1 ngôi nhà duy nhất (Nhà gỗ) nằm biệt lập \textbf{trên đỉnh núi}.
            \item Bằng trực giác, Nhà gỗ là "Điểm bất thường" (Outlier) vì xung quanh nó rất \textbf{thưa thớt} (Mật độ thấp), trong khi các nhà dưới thung lũng rất \textbf{đông đúc} (Mật độ cao).
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_05/lof_intuition.png}
    \end{columns}
\end{frame}

% SLIDE 18
\begin{frame}{Khái niệm "Hàng xóm" (Neighbors)}
    \begin{itemize}
        \item Thuật toán LOF sẽ đếm một số lượng nhất định các "hàng xóm" gần nhất với điểm đang xét (Ví dụ: 5 điểm gần nhất).
        \item Trong dữ liệu kế toán: Hàng xóm của một "Hóa đơn mua thép" là các "Hóa đơn mua thép" khác có cùng nhà cung cấp, cùng thời gian hoặc cùng khối lượng.
    \end{itemize}
\end{frame}

% SLIDE 19
\begin{frame}{Bán kính vùng lân cận (Reachability Distance)}
    \begin{itemize}
        \item \textbf{Khoảng cách (Distance):} Là sự khác biệt giữa giá trị của hai giao dịch.
        \item \textbf{Bán kính (Reachability):} Được định nghĩa là khoảng cách từ điểm đang xét đến "người hàng xóm" xa nhất trong nhóm lân cận.
        \item Nếu các giao dịch tương đồng nhau, bán kính sẽ nhỏ. Nếu giao dịch bị cô lập, bán kính sẽ rất lớn.
    \end{itemize}
\end{frame}

% SLIDE 20
\begin{frame}{Mật độ cục bộ (Local Reachability Density - LRD)}
    \begin{itemize}
        \item \textbf{LRD} tỷ lệ nghịch với Bán kính. 
        \item Nếu Bán kính nhỏ $\rightarrow$ Các điểm nằm chen chúc nhau $\rightarrow$ Mật độ (LRD) \textbf{cao} (Giao dịch bình thường).
        \item Nếu Bán kính lớn $\rightarrow$ Các điểm nằm rời rạc $\rightarrow$ Mật độ (LRD) \textbf{thấp} (Giao dịch đáng ngờ).
    \end{itemize}
\end{frame}

% SLIDE 21
\begin{frame}{Chỉ số LOF (Local Outlier Factor)}
    \begin{itemize}
        \item Bước cuối cùng, AI sẽ so sánh \textbf{Mật độ (LRD) của chính điểm đó} với \textbf{Mật độ trung bình của các "hàng xóm"}.
        \item Nếu bạn sống ở nơi hoang vắng (Mật độ thấp), nhưng tất cả "hàng xóm" của bạn (dù ở xa) lại sống trong trung tâm thành phố (Mật độ cao) $\rightarrow$ Bạn chính là kẻ lạc loài (Outlier).
        \item LOF = Trung bình Mật độ hàng xóm / Mật độ của bạn.
    \end{itemize}
\end{frame}

% SLIDE 22
\begin{frame}{Đọc hiểu điểm số LOF (LOF Score)}
    \begin{itemize}
        \item \textbf{LOF $\approx$ 1:} Giao dịch bình thường, giống hệt các giao dịch xung quanh.
        \item \textbf{LOF > 1 (ví dụ 1.5, 2.0, 5.0):} Cảnh báo đỏ (Red Flag). Điểm càng cao, sự bất thường càng lớn, khả năng gian lận càng cao.
    \end{itemize}
\end{frame}

% SLIDE 23
\begin{frame}{Tại sao LOF lại xuất sắc hơn Rules-based?}
    \begin{itemize}
        \item \textbf{Rules-based (Kế toán truyền thống):} Thiết lập luật "Hóa đơn > 20 triệu thì kiểm tra". Kẻ gian sẽ lách luật bằng cách xuất hóa đơn 19.9 triệu.
        \item \textbf{AI với LOF:} Không quan tâm luật. Nó chỉ thấy một cụm cực nhiều hóa đơn 19.9 triệu là "khác biệt" so với mật độ phân phối thông thường của công ty, và báo động ngay lập tức.
    \end{itemize}
\end{frame}

\section{4. Phát hiện gian lận với AI và No-code}

% SLIDE 24
\begin{frame}{Dùng AI mà không cần viết code}
    \begin{itemize}
        \item Sinh viên kế toán không cần lập trình thuật toán LOF bằng Python hay R.
        \item Chúng ta sẽ ứng dụng trực tiếp các nền tảng có tích hợp sẵn AI: \textbf{Microsoft Excel (Analyze Data)} và \textbf{Power BI (Anomaly Detection)}.
    \end{itemize}
\end{frame}

% SLIDE 25
\begin{frame}{Quy trình rà soát dữ liệu bằng AI}
    \begin{enumerate}
        \item \textbf{Chuẩn bị:} Xuất sổ Nhật ký chung hoặc Sổ chi tiết từ phần mềm kế toán (MISA, FAST, SAP) ra Excel.
        \item \textbf{Làm sạch (Data Cleansing):} Định dạng lại cột Ngày tháng, Số tiền, Loại bỏ dòng trống.
        \item \textbf{Chạy AI:} Bật tính năng Anomaly Detection hoặc dùng ChatGPT/Copilot để quét mảng dữ liệu.
        \item \textbf{Xử lý cảnh báo:} Kế toán viên lấy chứng từ gốc của các khoản bị "báo đỏ" để kiểm tra thủ công.
    \end{enumerate}
\end{frame}

% SLIDE 26
\begin{frame}{Sức mạnh của Prompt trong rà soát (Copilot/ChatGPT)}
    \begin{itemize}
        \item Cung cấp bối cảnh là yếu tố quan trọng nhất.
        \item \textbf{Prompt chuẩn:} \textit{"Đóng vai một kiểm toán viên nội bộ. Hãy phân tích tập dữ liệu thẻ tín dụng này. Tìm và liệt kê các giao dịch thỏa mãn 1 trong các yếu tố: Xảy ra vào ngày cuối tuần, vượt 3 lần mức chi tiêu trung bình của cá nhân đó, hoặc có số tiền chẵn đến kỳ lạ (VD: 10.000.000 thay vì 10.150.000)."}
    \end{itemize}
\end{frame}

% SLIDE 27
\begin{frame}{Case Study 1: Gian lận chia nhỏ (Smurfing)}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Vấn đề:} 
        \begin{itemize}
            \item Chính sách: Chi > 50 triệu phải có chữ ký Giám đốc. 
            \item Kẻ gian chẻ nhỏ hóa đơn thành 49tr, 48tr, 45tr để Kế toán trưởng ký (Smurfing).
        \end{itemize}
        \textbf{AI Giải quyết:} 
        \begin{itemize}
            \item AI (LOF) sẽ thấy mật độ giao dịch ngay dưới mốc 50tr dày đặc bất thường.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_05/smurfing_diagram.png}
    \end{columns}
\end{frame}

% SLIDE 28
\begin{frame}{Case Study 2: Hóa đơn ma (Phantom Vendors)}
    \begin{itemize}
        \item \textbf{Kịch bản:} Nhân viên tạo một nhà cung cấp giả mạo, lấy tên gần giống đối tác thật (Cty ABC và Cty ABCs), nhưng tài khoản ngân hàng thụ hưởng lại là của người nhà nhân viên.
        \item \textbf{AI Giải quyết:} Dùng AI để tìm Outliers trong Master Data (Dữ liệu gốc). AI phát hiện 2 mã nhà cung cấp khác nhau nhưng có chung 1 tài khoản ngân hàng, hoặc 1 tài khoản nhà cung cấp trùng với số tài khoản trên bảng lương nhân viên!
    \end{itemize}
\end{frame}

% SLIDE 29
\begin{frame}{Case Study 3: Giao dịch không khớp thời gian}
    \begin{itemize}
        \item Kế toán thường hay kiểm tra "Số tiền" mà quên kiểm tra "Thời gian".
        \item AI có thể dễ dàng lọc ra (Red Flags):
        \begin{itemize}
            \item Phiếu chi tiền mặt lập vào lúc 22h00 đêm Chủ nhật.
            \item Nhân viên X đang nghỉ phép ở Đà Nẵng nhưng lại có phát sinh thanh toán quẹt thẻ tại Hà Nội.
        \end{itemize}
    \end{itemize}
\end{frame}

% SLIDE 30
\begin{frame}{Sự kết hợp: AI và Con người}
    \begin{itemize}
        \item AI \textbf{không thể} tự ra quyết định buộc tội một nhân viên.
        \item Chức năng của AI chỉ là \textbf{Khoanh vùng rủi ro} (Highlight Anomaly).
        \item Con người (Kế toán/Kiểm toán viên) phải kết hợp sự \textbf{Hoài nghi nghề nghiệp} để kiểm tra đối chiếu chứng từ gốc, phỏng vấn và đưa ra kết luận.
    \end{itemize}
\end{frame}

\section{5. Thách thức, Đạo đức và Tương lai}

% SLIDE 31
\begin{frame}{Thách thức 1: Dữ liệu không gán nhãn (Unlabeled Data)}
    \begin{itemize}
        \item Hầu hết sổ sách kế toán đều không có nhãn (không ai ghi chú sẵn giao dịch nào là gian lận để AI học).
        \item Buộc phải dùng Học không giám sát (Unsupervised Learning - như thuật toán LOF), độ chính xác sẽ phụ thuộc vào mức độ "nhiễu" của hệ thống sổ sách.
    \end{itemize}
\end{frame}

% SLIDE 32
\begin{frame}{Thách thức 2: Báo động giả (False Positives)}
    \begin{itemize}
        \item Đây là căn bệnh nan giải của AI.
        \item AI đánh dấu 100 giao dịch là gian lận, Kế toán kiểm tra mờ mắt phát hiện 99 giao dịch là hợp lệ (ví dụ: mua hàng sỉ cuối năm nên số tiền đột biến).
        \item Gây mệt mỏi, lãng phí nguồn lực và dẫn đến tâm lý "bỏ qua cảnh báo" của con người.
    \end{itemize}
\end{frame}

% SLIDE 33
\begin{frame}{Thách thức 3: Kẻ gian lận thích nghi (False Negatives)}
    \begin{itemize}
        \item Tội phạm tài chính rất thông minh. Khi biết công ty dùng AI bắt "Hóa đơn chẵn", chúng sẽ cố tình chèn số lẻ.
        \item Dẫn đến False Negatives (Bỏ lọt tội phạm).
        \item AI cần được huấn luyện và cập nhật liên tục để đối phó với chiến thuật mới.
    \end{itemize}
\end{frame}

% SLIDE 34
\begin{frame}{Bảo mật dữ liệu (Data Privacy)}
    \begin{itemize}
        \item Sổ cái (General Ledger) là bí mật kinh doanh cao nhất của doanh nghiệp.
        \item Tuyệt đối \textbf{không tải} toàn bộ sổ cái thô lên các nền tảng AI Public (ChatGPT bản miễn phí).
        \item Nên sử dụng các giải pháp AI bảo mật doanh nghiệp (Copilot for Enterprise, Private LLMs) hoặc ẩn danh hóa dữ liệu (xóa tên, xóa STK thật).
    \end{itemize}
\end{frame}

% SLIDE 35
\begin{frame}{Đạo đức nghề nghiệp}
    \begin{itemize}
        \item AI không có tính nhân văn, nó chỉ nhìn vào những con số khô khan.
        \item Nếu AI báo cáo sai, ai chịu trách nhiệm? Là kế toán viên!
        \item Không bao giờ được ủy quyền ra quyết định kỷ luật/tố cáo hoàn toàn cho máy móc mà thiếu xác minh của chuyên gia.
    \end{itemize}
\end{frame}

% SLIDE 36
\begin{frame}{Tương lai: Real-time Auditing (Kiểm toán thời gian thực)}
    \begin{itemize}
        \item Hiện nay: Kế toán ghi sổ, cuối năm Kiểm toán độc lập mới vào rà soát $\rightarrow$ Mất bò mới lo làm chuồng.
        \item Tương lai có AI: Hệ thống ERP tích hợp thuật toán LOF, mọi bút toán vừa Enter xong sẽ bị AI quét qua ngay lập tức. Gian lận bị chặn đứng ngay trong ngày.
    \end{itemize}
\end{frame}

% SLIDE 37
\begin{frame}{Tóm tắt bài học}
    \begin{itemize}
        \item \textbf{Gian lận} luôn để lại dấu vết dạng "Điểm bất thường" (Outliers).
        \item Phương pháp \textbf{nhận diện cục bộ} (như LOF) giúp tìm ra các giao dịch bất thường so với chính bộ phận của nó, khắc phục điểm yếu của quy luật cứng nhắc.
        \item \textbf{Sinh viên No-code} có thể dùng Excel, Power BI và ChatGPT để thực hiện các nghiệp vụ kế toán điều tra phức tạp.
        \item \textbf{AI là chiếc radar}, nhưng bạn (kế toán viên) mới là \textbf{người thuyền trưởng} đưa ra quyết định.
    \end{itemize}
\end{frame}

% SLIDE 38
\begin{frame}{Q \& A}
    \begin{center}
        \Huge \textbf{HỎI \& ĐÁP}
    \end{center}
    \vspace{0.5cm}
    \textit{Chuẩn bị cho Buổi Thực hành Day 05 TH:}
    \begin{itemize}
        \item Cài đặt Excel bản mới nhất.
        \item Ôn tập lại Conditional Formatting và Pivot Table.
        \item Chúng ta sẽ tự tay "bắt" các hóa đơn ma trên một tập dữ liệu giả lập.
    \end{itemize}
\end{frame}

\end{document}
"""

with open(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\Slide_AIAcc_v2_Day05_LT.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)
