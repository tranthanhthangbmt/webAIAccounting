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

\title[Buổi 4: AI Chi tiết \& Tổng hợp]{Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.3cm} \Large Buổi 4: Ứng dụng AI xử lý công việc KT Chi tiết \& Tổng hợp}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

% SLIDE 1
\begin{frame}
    \titlepage
    \begin{center}
        \includegraphics[width=0.5\textwidth,height=2.5cm,keepaspectratio]{images/Day_04/bg_day4.png}
    \end{center}
\end{frame}

% SLIDE 2
\begin{frame}{Nội dung Chương trình}
    \tableofcontents
\end{frame}

% SLIDE 3
\begin{frame}{Khởi động (Ice-breaker)}
    \begin{center}
        \Large \textbf{Nỗi ám ảnh lớn nhất của sinh viên Kế toán?}
    \end{center}
    \vspace{0.5cm}
    \begin{itemize}
        \item Đó là định khoản sai Nợ / Có.
        \item Và cuối kỳ Bảng Cân Đối Số Phát Sinh không cân!
        \item \textbf{Tưởng tượng:} Nếu máy tính có thể tự học thuộc hàng ngàn tài khoản và tự động ghi Nợ/Có thay bạn thì sao?
    \end{itemize}
\end{frame}

\section{1. Tổng quan Kế toán Chi tiết \& Tổng hợp}

% SLIDE 4
\begin{frame}{Bookkeeping vs Accounting}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Bookkeeping (Kế toán chi tiết / Ghi sổ):}
        \begin{itemize}
            \item Quá trình thu thập, phân loại và ghi chép các giao dịch hàng ngày.
            \item Có tính chất lặp đi lặp lại.
        \end{itemize}
        \column{0.5\textwidth}
        \textbf{Accounting (Kế toán tổng hợp):}
        \begin{itemize}
            \item Quá trình phân tích, diễn giải và lập báo cáo từ dữ liệu đã ghi sổ.
            \item Đòi hỏi tư duy phân tích và ra quyết định.
        \end{itemize}
    \end{columns}
\end{frame}

% SLIDE 5
\begin{frame}{Chu trình Kế toán (The Accounting Cycle)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{enumerate}
            \item Phân tích giao dịch.
            \item Ghi nhật ký (Journalizing - Định khoản).
            \item Chuyển sổ cái (Posting).
            \item Lập Bảng cân đối thử.
            \item Bút toán điều chỉnh.
            \item Lập Báo cáo tài chính.
        \end{enumerate}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_04/accounting_cycle.png}
    \end{columns}
\end{frame}

% SLIDE 6
\begin{frame}{Nỗi đau của phương pháp truyền thống}
    \begin{itemize}
        \item Kế toán phải phụ thuộc vào trí nhớ để nhớ mã tài khoản (Vd: 156, 331, 642).
        \item Khối lượng giao dịch hàng ngày quá lớn dẫn đến dễ ghi nhầm, định khoản sai bản chất.
        \item Đối soát thủ công hàng ngàn dòng sao kê ngân hàng với sổ quỹ tiền mặt cực kỳ mệt mỏi.
    \end{itemize}
\end{frame}

% SLIDE 7
\begin{frame}{Giải pháp: AI-Enabled Bookkeeping}
    \begin{itemize}
        \item Trí tuệ nhân tạo có thể học từ hàng triệu giao dịch trong quá khứ để \textbf{tự động dự đoán}:
        \item \textit{Giao dịch này thuộc mã tài khoản nào?}
        \item \textit{Bên Nợ ghi gì, bên Có ghi gì?}
        \item Giúp kế toán tiết kiệm 80\% thời gian gõ phím và giảm thiểu gần như 100\% sai sót cơ học.
    \end{itemize}
\end{frame}

\section{2. AI Tự động hóa Phân loại \& Định khoản}

% SLIDE 8
\begin{frame}{Data Entry Automation (Tự động hóa Nhập liệu)}
    \begin{itemize}
        \item Tiếp nối bài học Buổi 3 (OCR đọc hóa đơn).
        \item AI không chỉ dừng ở việc "Đọc chữ", mà nó lấy dữ liệu số tiền và thông tin công ty đó làm đầu vào cho bước cực kỳ quan trọng: \textbf{Định khoản (Journalizing)}.
    \end{itemize}
\end{frame}

% SLIDE 9
\begin{frame}{Categorization Automation (Tự động Phân loại)}
    \begin{itemize}
        \item \textbf{Quy tắc cũ (Rule-based):} Nếu thấy chữ "Vinamilk" $\rightarrow$ Ghi vào Chi phí tiếp khách. Nhưng nếu là Công ty bánh kẹo mua sữa về làm bánh thì lại là Nguyên vật liệu!
        \item \textbf{AI thế hệ mới:} AI phân tích \textbf{Ngữ cảnh (Context)} của công ty để gợi ý mã tài khoản chính xác chứ không chỉ học vẹt từ khóa.
    \end{itemize}
\end{frame}

% SLIDE 10
\begin{frame}{Machine Learning trong Định khoản}
    \begin{itemize}
        \item AI được "huấn luyện" (Train) dựa trên dữ liệu kế toán của chính công ty bạn.
        \item Nếu bạn thường xuyên định khoản tiền điện vào TK 6427, AI sẽ học được \textbf{Quy luật (Pattern)} đó.
        \item Tháng sau, cứ có hóa đơn điện, AI tự động tạo bút toán: \textit{Nợ 6427 / Nợ 1331 / Có 331}.
    \end{itemize}
\end{frame}

% SLIDE 11
\begin{frame}{Prompt Engineering để Định khoản}
    \begin{columns}
        \column{0.5\textwidth}
        Dùng ChatGPT làm "Trợ lý định khoản".
        \vspace{0.3cm}
        \\ \textbf{Prompt:} \textit{"Bạn là Kế toán Việt Nam. Tôi vừa trả tiền mua 5 máy tính bằng chuyển khoản, dùng cho phòng Giám đốc. Hãy định khoản."}
        \\ \textbf{AI:} \textit{Nợ TK 211 / Nợ TK 133 / Có TK 112.}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_04/journal_entry.png}
    \end{columns}
\end{frame}

% SLIDE 12
\begin{frame}{Đào tạo AI bằng bộ luật nội bộ}
    \begin{itemize}
        \item Mỗi doanh nghiệp có bộ tài khoản chi tiết khác nhau (Vd: 64271 là Tiền điện, 64272 là Tiền nước).
        \item Bạn có thể upload Danh mục tài khoản (Chart of Accounts) lên ChatGPT và ra lệnh: \textit{"Từ nay hãy định khoản chi tiết dựa trên danh sách mã tài khoản này"}.
    \end{itemize}
\end{frame}

% SLIDE 13
\begin{frame}{Duyệt và Xác nhận (The Human Touch)}
    \begin{itemize}
        \item Các phần mềm Kế toán hiện đại (Xero, QuickBooks, MISA AMIS) có AI tích hợp sẽ không tự ý ghi sổ mù quáng.
        \item Nó sẽ \textbf{Đề xuất (Suggest)} bút toán định khoản.
        \item Kế toán viên chỉ việc kiểm tra lướt qua, thấy đúng thì bấm \textbf{"Duyệt (Approve)"}.
    \end{itemize}
\end{frame}

% SLIDE 14
\begin{frame}{Xử lý các nghiệp vụ phức tạp (Complex Transactions)}
    \begin{itemize}
        \item Các nghiệp vụ như: Phân bổ công cụ dụng cụ, Khấu hao TSCĐ, Trả góp.
        \item AI có khả năng tự động tạo Bảng phân bổ (Amortization Schedule) và tự động sinh bút toán Nợ/Có vào mỗi cuối tháng mà không cần con người nhắc nhở.
    \end{itemize}
\end{frame}

\section{3. AI trong Đối soát và Tập hợp Chi phí}

% SLIDE 15
\begin{frame}{Reconciliation Automation (Đối soát tự động)}
    \begin{itemize}
        \item \textbf{Đối soát (Reconciliation):} Là quá trình so sánh số liệu giữa 2 nguồn (Ví dụ: Sổ quỹ công ty và Sao kê ngân hàng) để đảm bảo khớp nhau.
        \item \textbf{Thực trạng cũ:} Mò mẫm từng dòng sao kê với sổ cái bằng thước kẻ và bút dạ quang. Vô cùng tốn thời gian.
    \end{itemize}
\end{frame}

% SLIDE 16
\begin{frame}{AI xử lý Sao kê Ngân hàng (Bank Reconciliation)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item AI có thể so sánh hàng vạn giao dịch trong 3 giây.
            \item Nó tự động ghép cặp (Match) theo: Ngày tháng, Số tiền, Mã tham chiếu.
            \item Tự động đánh dấu tick các khoản đã khớp.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_04/bank_recon.png}
    \end{columns}
\end{frame}

% SLIDE 17
\begin{frame}{Phát hiện Sai lệch (Discrepancy Identification)}
    \begin{itemize}
        \item \textbf{Ví dụ:} Khách chuyển 1.000.000đ nhưng ngân hàng trừ phí 3.300đ $\rightarrow$ Sao kê báo nhận 996.700đ.
        \item Kế toán truyền thống tìm không ra số 1.000.000đ trên sao kê để gạch nợ.
        \item \textbf{AI:} Nhận diện ngay khoản phí 3.300đ, tự động tách bút toán \textit{Chi phí tài chính (TK 635)} để số liệu khớp nhau hoàn toàn!
    \end{itemize}
\end{frame}

% SLIDE 18
\begin{frame}{Expense Management (Quản lý chi phí)}
    \begin{itemize}
        \item Nhân viên đi công tác dùng thẻ công ty chi tiêu.
        \item Nhân viên chụp bill qua app $\rightarrow$ AI đọc bill (OCR) $\rightarrow$ Tự động khớp bill với giao dịch quẹt thẻ từ ngân hàng $\rightarrow$ Tự động định khoản chi phí công tác.
        \item Không còn cảnh cuối tháng chạy đi đòi từng tờ hóa đơn.
    \end{itemize}
\end{frame}

% SLIDE 19
\begin{frame}{Tập hợp chi phí tính giá thành}
    \begin{itemize}
        \item Kế toán sản xuất phải chia chi phí NVL (621), Nhân công (622), SX chung (627).
        \item Dùng AI để phân bổ: Cung cấp cho AI tiêu thức phân bổ (theo giờ công, diện tích), AI tự động tính toán và tạo bút toán kết chuyển sang TK 154.
    \end{itemize}
\end{frame}

% SLIDE 20
\begin{frame}{Dùng Prompt yêu cầu AI tính phân bổ}
    \begin{itemize}
        \item \textbf{Prompt:} \textit{"Tôi có chi phí điện tháng này là 50 triệu. Hãy lập bảng phân bổ chi phí này cho 3 phân xưởng A, B, C dựa trên tỷ lệ giờ máy hoạt động lần lượt là 200, 300, 500 giờ."}
        \item ChatGPT sẽ tính ra chính xác số tiền cho từng phân xưởng trong 1 giây.
    \end{itemize}
\end{frame}

\section{4. Lập Báo cáo Chi tiết \& Tổng hợp với AI}

% SLIDE 21
\begin{frame}{Reporting Automation (Báo cáo tự động)}
    \begin{itemize}
        \item Báo cáo không chỉ là BCTC cuối năm, mà là Báo cáo quản trị (Management Reports) gửi cho Sếp hàng ngày.
        \item AI giúp lập báo cáo công nợ phải thu, phải trả, báo cáo dòng tiền theo thời gian thực (Real-time).
    \end{itemize}
\end{frame}

% SLIDE 22
\begin{frame}{Generative AI Phân tích dữ liệu}
    \begin{itemize}
        \item Bạn có một file Excel chứa 10.000 dòng Sổ Nhật ký chung.
        \item Sếp hỏi: \textit{"Tháng này ta chi tiếp khách bao nhiêu tiền? Tăng hay giảm so với tháng trước?"}
        \item Làm tay (Pivot Table) sẽ mất 10-15 phút.
    \end{itemize}
\end{frame}

% SLIDE 23
\begin{frame}{Dùng ChatGPT Advanced Data Analysis}
    \begin{itemize}
        \item Upload file Excel Sổ Nhật ký chung lên ChatGPT.
        \item \textbf{Prompt:} \textit{"Hãy tính tổng chi phí tiếp khách (TK 6428) trong tháng 3, so sánh với tháng 2. Vẽ biểu đồ cột để minh họa."}
        \item AI sẽ tự động code Python ngầm, đọc dữ liệu và vẽ biểu đồ trả về ngay lập tức.
    \end{itemize}
\end{frame}

% SLIDE 24
\begin{frame}{AI hỗ trợ Lập Báo cáo Lưu chuyển Tiền tệ}
    \begin{itemize}
        \item Lập Cash Flow Statement luôn là nỗi sợ của kế toán.
        \item AI có khả năng rà soát toàn bộ phát sinh đối ứng với nhóm TK Tiền (111, 112).
        \item Từ đó AI tự động phân loại giao dịch vào 3 luồng: HĐ Kinh doanh, HĐ Đầu tư, HĐ Tài chính một cách chính xác.
    \end{itemize}
\end{frame}

% SLIDE 25
\begin{frame}{Lập Thuyết minh Báo cáo Tài chính}
    \begin{itemize}
        \item Thuyết minh BCTC là phần văn bản giải trình dài dòng.
        \item \textbf{Giải pháp:} Cung cấp Bảng Cân Đối Kế Toán cho AI.
        \item \textbf{Prompt:} \textit{"Hãy viết bản dự thảo Thuyết minh BCTC phần 'Sự biến động của Hàng tồn kho' dựa trên bảng số liệu tôi vừa tải lên."}
    \end{itemize}
\end{frame}

% SLIDE 26
\begin{frame}{Xây dựng Dashboard Quản trị trực quan}
    \begin{itemize}
        \item AI có thể kết hợp với Power BI hoặc Copilot trong Excel.
        \item Kế toán chỉ việc chat: \textit{"Lập một Dashboard thể hiện doanh thu theo từng chi nhánh"}.
        \item Hệ thống tự vẽ đồ thị trực quan, nâng tầm kế toán viên thành Chuyên viên phân tích dữ liệu (Data Analyst).
    \end{itemize}
\end{frame}

\section{5. Kiểm soát Nội bộ (Internal Controls)}

% SLIDE 27
\begin{frame}{Tại sao Kế toán cần Kiểm soát Nội bộ?}
    \begin{itemize}
        \item Những vụ bê bối kế toán lịch sử (Enron, WorldCom) sụp đổ vì dàn lãnh đạo cố tình "nấu sổ" (Cooking the books).
        \item Kế toán viên không chỉ lo tính toán, mà còn có trách nhiệm thiết lập hệ thống để \textbf{bảo vệ tài sản} công ty khỏi bị đánh cắp.
    \end{itemize}
\end{frame}

% SLIDE 28
\begin{frame}{Mô hình Tam giác Gian lận (Fraud Triangle)}
    \begin{columns}
        \column{0.5\textwidth}
        Gian lận tài chính xảy ra khi hội tụ 3 yếu tố:
        \begin{enumerate}
            \item \textbf{Áp lực (Pressure):} Nợ cá nhân, áp lực chỉ tiêu kinh doanh.
            \item \textbf{Cơ hội (Opportunity):} Quản lý lỏng lẻo.
            \item \textbf{Bao biện (Rationalization):} "Tôi chỉ mượn tạm vài ngày".
        \end{enumerate}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_04/fraud_triangle.png}
    \end{columns}
\end{frame}

% SLIDE 29
\begin{frame}{Trọng tâm của Internal Controls}
    \begin{itemize}
        \item Doanh nghiệp không thể kiểm soát "Áp lực" hay sự "Bao biện" trong đầu nhân viên.
        \item Doanh nghiệp chỉ có thể triệt tiêu \textbf{"Cơ hội"}.
        \item Công cụ để triệt tiêu cơ hội chính là \textbf{Hệ thống Kiểm soát Nội bộ (Internal Controls)}.
    \end{itemize}
\end{frame}

% SLIDE 30
\begin{frame}{2 Mục tiêu cốt lõi của Internal Controls}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{enumerate}
            \item \textbf{Bảo vệ Tài sản (Safeguard Assets):} Ngăn chặn mất cắp, biển thủ tiền mặt.
            \item \textbf{Cải thiện tính chính xác:} Đảm bảo BCTC đáng tin cậy.
        \end{enumerate}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_04/internal_controls.png}
    \end{columns}
\end{frame}

% SLIDE 31
\begin{frame}{Đặc thù kiểm soát Tiền (Cash)}
    \begin{itemize}
        \item Tiền là tài sản dễ bị đánh cắp nhất vì thanh khoản cao.
        \item \textbf{Nguyên tắc Phân quyền (Separation of Duties):} 
        \item Người giữ tiền mặt (Thủ quỹ) \textbf{KHÔNG} được phép đồng thời là người ghi sổ (Kế toán thanh toán).
        \item Nếu 1 người làm 2 việc = Rủi ro gian lận tiền rất lớn!
    \end{itemize}
\end{frame}

% SLIDE 32
\begin{frame}{AI củng cố Kiểm soát Nội bộ thế nào?}
    \begin{itemize}
        \item Máy móc không biết "Cố tình gian lận" hay "Biển thủ".
        \item \textbf{Audit Trail (Dấu vết kiểm toán):} AI ghi nhận mọi hành động: Giao dịch này do AI định khoản lúc mấy giờ, kế toán viên nào bấm duyệt.
        \item Sự minh bạch này giúp chống gian lận cực tốt.
    \end{itemize}
\end{frame}

% SLIDE 33
\begin{frame}{Rủi ro khi phụ thuộc vào AI (AI Risks)}
    \begin{itemize}
        \item \textbf{Automation Bias (Thành kiến Tự động hóa):} Kế toán viên quá tin tưởng vào AI, nhắm mắt duyệt (Approve) mọi bút toán mà không thèm kiểm tra.
        \item \textbf{Garbage In - Garbage Out:} Nếu AI học từ dữ liệu sai trong quá khứ, nó sẽ tự động hạch toán sai hàng loạt trong tương lai.
    \end{itemize}
\end{frame}

% SLIDE 34
\begin{frame}{Kiểm soát hệ thống AI}
    \begin{itemize}
        \item Kế toán trưởng phải lập quy trình rà soát ngẫu nhiên 5\% số lượng bút toán do AI làm.
        \item \textbf{Phân quyền AI:} AI không được phép tạo các bút toán nhạy cảm (như tính lương, phân chia lợi nhuận) mà không có chữ ký duyệt tay của Sếp.
    \end{itemize}
\end{frame}

% SLIDE 35
\begin{frame}{Continuous Auditing (Kiểm toán liên tục)}
    \begin{itemize}
        \item Nhờ AI xử lý số liệu Real-time, ta không cần đợi đến cuối tháng mới soát xét.
        \item AI sẽ quét Sổ cái hàng ngày và tự động gửi Cảnh báo (Alert): \textit{"Hôm nay có 3 bút toán chuyển tiền tỷ lệ bất thường, yêu cầu kiểm tra ngay"}.
    \end{itemize}
\end{frame}

% SLIDE 36
\begin{frame}{Tác động đến Tổ chức bộ máy Kế toán}
    \begin{itemize}
        \item \textbf{Mô hình cũ (Hình tháp):} 1 Kế toán trưởng $\rightarrow$ 3 Kế toán tổng hợp $\rightarrow$ 10 Kế toán viên nhập liệu.
        \item \textbf{Mô hình mới với AI (Kim cương):} AI làm thay việc nhập liệu (Bookkeeping). Doanh nghiệp cần những \textbf{Nhà phân tích dữ liệu kế toán} hơn là "Thợ gõ".
    \end{itemize}
\end{frame}

% SLIDE 37
\begin{frame}{Ứng dụng thực tế: Live Nation Entertainment}
    \begin{itemize}
        \item Live Nation là công ty tổ chức sự kiện âm nhạc lớn (Bán 500 triệu vé/năm).
        \item Lượng giao dịch tiền mặt và trực tuyến khổng lồ, rất dễ bị gian lận.
        \item Họ dùng Hệ thống thông tin và AI để giám sát dòng tiền, đối chiếu số vé bán và số người vào cổng theo thời gian thực để triệt tiêu gian lận!
    \end{itemize}
\end{frame}

% SLIDE 38
\begin{frame}{Tư duy lại công việc Định khoản}
    \begin{center}
        \Large Chuyển từ Tư duy \textbf{Nhớ (Memorize)} sang Tư duy \textbf{Phân tích (Analyze)}.
    \end{center}
    \vspace{0.5cm}
    \begin{itemize}
        \item Tương lai bạn không cần "thuộc lòng" mã tài khoản.
        \item Bạn cần "hiểu bản chất" của nghiệp vụ kinh tế để biết AI đang gợi ý định khoản đúng hay sai.
    \end{itemize}
\end{frame}

% SLIDE 39
\begin{frame}{AI là trợ lý, không phải Sếp của bạn!}
    \begin{itemize}
        \item Bạn là người đặt ra câu lệnh (Prompt).
        \item Bạn là người thiết lập nguyên tắc Kiểm soát Nội bộ.
        \item AI sẽ không thay thế kế toán. Nhưng Kế toán viên biết dùng AI sẽ thay thế người không biết dùng AI.
    \end{itemize}
\end{frame}

% SLIDE 40
\begin{frame}{Tóm tắt Buổi 4}
    \begin{itemize}
        \item \textbf{Bookkeeping:} AI tự động hóa phân loại, định khoản Nợ/Có và đối soát sao kê.
        \item \textbf{Accounting:} Dùng Prompt AI để tính toán phân bổ chi phí, lập Báo cáo quản trị, vẽ biểu đồ.
        \item \textbf{Internal Controls:} Củng cố kiểm soát nội bộ để loại bỏ "Cơ hội" trong Tam giác gian lận, đồng thời kiểm soát chính hệ thống AI (Automation Bias).
    \end{itemize}
\end{frame}

% SLIDE 41
\begin{frame}{Chuẩn bị cho Buổi Thực hành}
    \begin{itemize}
        \item Yêu cầu ôn tập lại các nhóm Tài khoản Kế toán (TT200 / TT133).
        \item Cài đặt sẵn Excel, chuẩn bị đăng nhập ChatGPT/Copilot.
        \item Chuẩn bị file Sổ Nhật ký chung để thực hành dùng AI tự động phân tích và định khoản.
    \end{itemize}
\end{frame}

% SLIDE 42
\begin{frame}{Kết thúc}
    \begin{center}
        \Huge \textbf{Q \& A}
    \end{center}
    \vspace{0.5cm}
    \textbf{Thảo luận:}
    \begin{itemize}
        \item Nếu AI tự động định khoản và đối soát ngân hàng khớp 100\%, liệu vị trí "Kế toán thanh toán" có biến mất hoàn toàn trong 5 năm tới?
    \end{itemize}
\end{frame}

\end{document}
"""

with open(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\Slide_AIAcc_v2_Day04_LT.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)
