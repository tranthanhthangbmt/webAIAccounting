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

\title[Buổi 5 (TH): Excel \& AI]{Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.3cm} \Large Buổi 5 (Thực hành): Ứng dụng Excel \& AI (Prompt) để quét điểm bất thường (Outliers)}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

% SLIDE 1
\begin{frame}
    \titlepage
    \begin{center}
        \includegraphics[width=0.5\textwidth,height=2.5cm,keepaspectratio]{images/Day_05/bg_day5_th.png}
    \end{center}
\end{frame}

% SLIDE 2
\begin{frame}{Năng lực đạt được sau buổi học}
    \begin{itemize}
        \item \textbf{Về Lý thuyết (LT):} Củng cố tư duy phát hiện điểm bất thường (Outliers) trong dữ liệu.
        \item \textbf{Về Thực hành (TH):} Sử dụng thành thạo Conditional Formatting, Pivot Table trong Excel kết hợp với Prompt AI để thiết lập bẫy lỗi (red flags), quét sổ Nhật ký chung tìm hóa đơn chẵn, lệch ngày.
        \item \textbf{Về Tư duy nghề nghiệp:} Rèn luyện kỹ năng hoài nghi nghề nghiệp, biết cách kết hợp cảnh báo của AI với việc đối chiếu chứng từ gốc để đưa ra kết luận.
    \end{itemize}
\end{frame}

% SLIDE 3
\begin{frame}{Kịch bản thực hành (Case Study)}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{itemize}
            \item \textbf{Vai trò:} Bạn là một Kiểm toán viên nội bộ (Internal Auditor).
            \item \textbf{Nhiệm vụ:} Bạn được giao rà soát \textbf{5.000 dòng} Sổ Nhật ký chung của Công ty X trong năm tài chính vừa qua.
            \item \textbf{Công cụ:} Excel và ChatGPT / Copilot.
            \item \textbf{Mục tiêu:} Phát hiện nhanh các giao dịch có dấu hiệu gian lận.
        \end{itemize}
        \column{0.4\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_05/red_flags_table.png}
    \end{columns}
\end{frame}

% SLIDE 4
\begin{frame}{Các rủi ro (Red Flags) cần tìm kiếm}
    \begin{itemize}
        \item \textbf{Red Flag 1:} Giao dịch phát sinh vào ngày nghỉ (Thứ 7, Chủ Nhật) - Bất thường về thời gian.
        \item \textbf{Red Flag 2:} Giao dịch có số tiền tròn chẵn đến hàng triệu (Ví dụ: 10.000.000 VNĐ thay vì 10.125.000 VNĐ) - Dấu hiệu của hóa đơn khống hoặc chia nhỏ hóa đơn.
        \item \textbf{Red Flag 3:} Bút toán lệch sổ (Ví dụ Nợ $\neq$ Có).
        \item \textbf{Red Flag 4:} Mức chi tiêu của một nhân viên/phòng ban cao đột biến so với trung bình (Outlier cục bộ).
    \end{itemize}
\end{frame}

% SLIDE 5
\begin{frame}{Chuẩn bị file dữ liệu}
    \begin{itemize}
        \item \textbf{File thực hành:} \texttt{NhatKyChung\_Day05\_Raw.xlsx}
        \item File này chứa dữ liệu giả lập (Mock data) của một doanh nghiệp thương mại.
        \item Giảng viên đã "cài cắm" sẵn một số giao dịch lỗi và gian lận.
        \item \textit{Nhiệm vụ của bạn là dùng AI và Excel để "săn" được chúng càng nhanh càng tốt!}
    \end{itemize}
\end{frame}

\section{Ôn tập Excel cốt lõi cho Kế toán điều tra}

% SLIDE 6
\begin{frame}{Tại sao lại dùng Excel cho Kế toán điều tra?}
    \begin{itemize}
        \item Giao diện thân thuộc với mọi kế toán viên.
        \item Khả năng tùy biến cao, xử lý dữ liệu lớn.
        \item Dễ dàng kết hợp với các công thức được sinh ra từ AI.
        \item Các phiên bản Excel mới (Excel 365) đã được tích hợp sẵn Machine Learning (Analyze Data).
    \end{itemize}
\end{frame}

% SLIDE 7
\begin{frame}{Ôn tập 1: Data Formatting (Định dạng dữ liệu)}
    Trước khi phân tích, dữ liệu phải "Sạch" và "Chuẩn":
    \begin{itemize}
        \item \textbf{Cột Ngày tháng:} Chuyển về định dạng \textit{Short Date} (DD/MM/YYYY).
        \item \textbf{Cột Số tiền:} Chuyển về định dạng \textit{Number} hoặc \textit{Accounting} (Có dấu phẩy phân cách hàng nghìn).
        \item \textbf{Loại bỏ khoảng trắng (Trim):} Đảm bảo tên nhân viên hoặc mã tài khoản không có dấu cách thừa.
    \end{itemize}
\end{frame}

% SLIDE 8
\begin{frame}{Ôn tập 2: Conditional Formatting}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Định nghĩa:} Tính năng định dạng theo điều kiện giúp tự động đổi màu ô / hàng nếu thỏa mãn một quy tắc (Rule) nào đó.
            \item \textbf{Ứng dụng:} Đây là công cụ đắc lực nhất để làm nổi bật (Highlight) các Red Flags trong biển dữ liệu.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_05/excel_conditional_formatting.png}
    \end{columns}
\end{frame}

% SLIDE 9
\begin{frame}{Ôn tập 3: Hàm WEEKDAY()}
    \begin{itemize}
        \item \textbf{Cú pháp:} \texttt{=WEEKDAY(serial\_number, [return\_type])}
        \item \textbf{Chức năng:} Trả về thứ trong tuần của một ngày.
        \item Nếu \texttt{return\_type = 1} (hoặc bỏ trống): Chủ Nhật = 1, Thứ Hai = 2, ..., Thứ Bảy = 7.
        \item \textit{Suy luận logic:} Để bắt ngày cuối tuần, ta cần điều kiện: \texttt{WEEKDAY(Ngày) = 1} HOẶC \texttt{WEEKDAY(Ngày) = 7}.
    \end{itemize}
\end{frame}

% SLIDE 10
\begin{frame}{Ôn tập 4: Hàm MOD()}
    \begin{itemize}
        \item \textbf{Cú pháp:} \texttt{=MOD(number, divisor)}
        \item \textbf{Chức năng:} Trả về phần dư của phép chia.
        \item \textbf{Ứng dụng tìm số chẵn:} Để kiểm tra một số tiền có tròn chẵn hàng triệu hay không, ta chia nó cho 1.000.000.
        \item \textit{Ví dụ:} \texttt{=MOD(10000000, 1000000)} sẽ trả về \textbf{0}.
        \item \texttt{=MOD(10125000, 1000000)} sẽ trả về \textbf{125000}.
    \end{itemize}
\end{frame}

% SLIDE 11
\begin{frame}{Ôn tập 5: Pivot Table cơ bản}
    \begin{itemize}
        \item Pivot Table là bảng tổng hợp dữ liệu động.
        \item \textbf{Kế toán điều tra dùng Pivot Table để làm gì?}
        \begin{itemize}
            \item Nhóm các giao dịch theo \textit{Mã nhân viên} để xem ai có tổng chi tiêu cao nhất.
            \item Nhóm theo \textit{Nhà cung cấp} để đếm số lần phát sinh giao dịch (Tần suất).
            \item Nhóm theo \textit{Giờ/Tháng} để phát hiện xu hướng bất thường theo thời gian.
        \end{itemize}
    \end{itemize}
\end{frame}

% SLIDE 12
\begin{frame}{Checkpoint 1}
    \begin{center}
        \Large Hãy chắc chắn bạn đã nắm rõ các hàm: \\
        \textbf{WEEKDAY()}, \textbf{MOD()} và tính năng \textbf{Conditional Formatting}.
    \end{center}
    \vspace{0.5cm}
    Nếu bạn quên công thức, đừng lo lắng! Chúng ta sẽ dùng AI để viết chúng thay bạn.
\end{frame}

\section{Ứng dụng Prompt AI để xây dựng quy tắc quét lỗi}

% SLIDE 13
\begin{frame}{Tư duy Prompt Engineering cho Kế toán điều tra}
    Một Prompt (Câu lệnh) tốt để nhờ AI hỗ trợ Excel cần 3 yếu tố:
    \begin{enumerate}
        \item \textbf{Vai trò:} "Đóng vai chuyên gia dữ liệu Excel / Kiểm toán viên."
        \item \textbf{Bối cảnh \& Cấu trúc dữ liệu:} "Tôi có cột A là Ngày ghi sổ, cột B là Số tiền, dữ liệu bắt đầu từ dòng 2."
        \item \textbf{Mục tiêu:} "Viết cho tôi công thức Conditional Formatting để bôi đỏ toàn bộ dòng nếu số tiền chia hết cho 1 triệu."
    \end{enumerate}
\end{frame}

% SLIDE 14
\begin{frame}{Prompt 1: Bắt lỗi giao dịch ngày nghỉ}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Thực hành viết Prompt vào ChatGPT:} \\
        \textit{"Đóng vai một kế toán viên. Tôi đang dùng Excel. Cột C của tôi chứa Ngày ghi sổ (dữ liệu từ C2:C5000). Hãy viết cho tôi công thức dùng trong Conditional Formatting để làm nổi bật (bôi màu) các dòng có Ngày ghi sổ rơi vào Thứ Bảy hoặc Chủ Nhật."}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_05/chatgpt_excel_prompt.png}
    \end{columns}
\end{frame}

% SLIDE 15
\begin{frame}{Thực hành 1: Gắn công thức AI vào Excel}
    \begin{itemize}
        \item AI sẽ trả về một công thức dạng: \texttt{=OR(WEEKDAY(\$C2)=1, WEEKDAY(\$C2)=7)}
        \item \textbf{Thao tác:}
        \begin{enumerate}
            \item Bôi đen toàn bộ vùng dữ liệu (A2:F5000).
            \item Home $\rightarrow$ Conditional Formatting $\rightarrow$ New Rule.
            \item Chọn "Use a formula to determine which cells to format".
            \item Paste công thức AI cung cấp vào $\rightarrow$ Chọn Format (Fill màu Đỏ) $\rightarrow$ OK.
        \end{enumerate}
        \item \textit{Kết quả:} Toàn bộ các giao dịch lập vào cuối tuần sẽ sáng lên!
    \end{itemize}
\end{frame}

% SLIDE 16
\begin{frame}{Prompt 2: Tìm số tiền tròn chẵn bất thường (Smurfing)}
    \begin{itemize}
        \item Kẻ gian lận (hoặc nhân viên tạo hóa đơn khống) thường lười biếng và hay bịa ra các số tròn chẵn (Ví dụ: 5.000.000, 10.000.000).
        \item \textbf{Thực hành viết Prompt:} \\
        \textit{"Cột F của tôi là Số Tiền. Viết công thức Conditional Formatting để bôi màu các dòng có số tiền tròn chẵn đến hàng triệu (VD: 2.000.000, 15.000.000). Chú ý: bỏ qua các ô có giá trị bằng 0 hoặc rỗng."}
    \end{itemize}
\end{frame}

% SLIDE 17
\begin{frame}{Thực hành 2: Áp dụng công thức số chẵn}
    \begin{itemize}
        \item Cảnh giác với công thức AI: Bạn cần kiểm tra xem AI có dùng đúng hàm \texttt{MOD} không.
        \item Công thức chuẩn: \texttt{=AND(\$F2<>0, MOD(\$F2, 1000000)=0)}
        \item Lặp lại thao tác tạo New Rule trong Conditional Formatting với công thức này.
    \end{itemize}
\end{frame}

% SLIDE 18
\begin{frame}{Prompt 3: Nhận diện bất thường cục bộ với Pivot Table}
    \begin{itemize}
        \item \textbf{Vấn đề:} Làm sao biết nhân viên Nguyễn Văn A có chi phí tiếp khách bất thường hay không?
        \item \textbf{Prompt:} \\
        \textit{"Tôi có dữ liệu: Cột C (Tên nhân viên), Cột D (Loại chi phí), Cột E (Số tiền). Hãy hướng dẫn tôi từng bước cách tạo Pivot Table để tính tổng chi phí của từng nhân viên, sau đó làm sao để tìm ra nhân viên có chi phí cao vượt trội so với những người khác."}
    \end{itemize}
\end{frame}

% SLIDE 19
\begin{frame}{Thực hành 3: Phân tích kết quả Pivot Table}
    \begin{itemize}
        \item Theo hướng dẫn của AI, chèn Pivot Table.
        \item Kéo "Tên nhân viên" vào Rows, "Số tiền" vào Values.
        \item Dùng tính năng Sort (Sắp xếp) từ Lớn đến Nhỏ.
        \item Nếu Top 1 có giá trị cao gấp 5-10 lần Top 2 $\rightarrow$ Đó chính là một \textbf{Outlier} cần phải lôi hồ sơ ra kiểm tra ngay!
    \end{itemize}
\end{frame}

\section{Phân tích Nâng cao bằng Data Analysis (Analyze Data)}

% SLIDE 20
\begin{frame}{Giới thiệu tính năng "Analyze Data" (Tích hợp AI)}
    \begin{itemize}
        \item Dành cho các bạn dùng Microsoft 365 (hoặc Excel trên web).
        \item Analyze Data là công cụ Machine Learning được tích hợp thẳng vào Excel.
        \item Bạn không cần viết Pivot Table hay vẽ Chart. Trí tuệ nhân tạo sẽ "đọc" dữ liệu của bạn và tự động đưa ra các Insight (Gợi ý).
    \end{itemize}
\end{frame}

% SLIDE 21
\begin{frame}{Cách thức hoạt động của Analyze Data}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item AI tự động tìm các mô hình (Patterns) ẩn bên trong bộ dữ liệu.
            \item Tự động phát hiện Xu hướng (Trends) và Điểm bất thường (Outliers/Anomalies) trong chuỗi thời gian (Time-series).
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_05/excel_analyze_data.png}
    \end{columns}
\end{frame}

% SLIDE 22
\begin{frame}{Thực hành 4: Sử dụng Analyze Data}
    \begin{itemize}
        \item Bôi đen toàn bộ bảng dữ liệu Nhật ký chung.
        \item Vào tab \textbf{Home} $\rightarrow$ Nhấp vào \textbf{Analyze Data} (Ở góc trên bên phải).
        \item Một cửa sổ bên phải sẽ hiện ra với hàng loạt biểu đồ.
        \item Hãy lướt xem AI phát hiện được gì? (Ví dụ: "Tổng tiền cao khác thường vào ngày 15/08").
    \end{itemize}
\end{frame}

% SLIDE 23
\begin{frame}{Khám phá kết quả}
    \begin{itemize}
        \item Bạn có thể hỏi AI bằng ngôn ngữ tự nhiên ngay trong ô tìm kiếm của Analyze Data.
        \item Ví dụ (Tiếng Anh): \textit{"Show me total amount by department"} hoặc \textit{"Which date has the highest amount?"}
        \item AI sẽ tự động sinh ra Pivot Table trả lời cho bạn.
    \end{itemize}
\end{frame}

% SLIDE 24
\begin{frame}{Sử dụng Advanced Data Analysis (ChatGPT Plus)}
    \begin{itemize}
        \item Nếu bạn có bản quyền ChatGPT Plus, bạn có thể tải thẳng file \texttt{.csv} hoặc \texttt{.xlsx} lên ChatGPT.
        \item ChatGPT có thể chạy ngôn ngữ lập trình Python ngầm bên dưới để phân tích độ lệch chuẩn (Z-score) hoặc thuật toán Isolation Forest/LOF một cách tự động.
    \end{itemize}
\end{frame}

% SLIDE 25
\begin{frame}{Prompt 4: Tự động hóa hoàn toàn với ChatGPT}
    \begin{itemize}
        \item \textbf{Thực hành:} Tải file \texttt{NhatKyChung\_Day05.csv} lên.
        \item \textbf{Prompt:} \\
        \textit{"Đây là Sổ Nhật ký chung của công ty tôi. Hãy đóng vai một Kiểm toán viên CNTT (IT Auditor). Sử dụng Python để quét file này, tính điểm Z-score cho cột Số tiền và tìm ra Top 5 giao dịch bất thường nhất. Liệt kê chúng dưới dạng bảng và giải thích tại sao bạn lại nghi ngờ chúng."}
    \end{itemize}
\end{frame}

\section{Giải quyết tình huống và Lập báo cáo kiểm soát}

% SLIDE 26
\begin{frame}{Review kết quả: Báo động giả (False Positives)}
    \begin{itemize}
        \item Các dòng bị bôi đỏ (Red flags) đã hiện ra. 
        \item Liệu 100\% chúng đều là gian lận?
        \item \textbf{KHÔNG!} Có thể có những khoản chi hợp lệ nhưng ngẫu nhiên trùng khớp điều kiện (Ví dụ: mua máy tính đúng giá chẵn 20.000.000 VNĐ, hoặc chuyển khoản cho đối tác vào sáng Thứ 7).
    \end{itemize}
\end{frame}

% SLIDE 27
\begin{frame}{Bài tập nhóm: Phân tích giao dịch "Báo đỏ"}
    \begin{itemize}
        \item \textbf{Yêu cầu:} Các nhóm hãy dùng tính năng Filter (Lọc) trong Excel để chỉ hiện những dòng bị bôi màu (Filter by Color).
        \item Chọn ra \textbf{3 giao dịch} mà bạn cho là đáng ngờ nhất.
        \item Thảo luận nhóm: Lý do tại sao bạn nghi ngờ? Giao dịch này vi phạm quy tắc kiểm soát nội bộ nào?
    \end{itemize}
\end{frame}

% SLIDE 28
\begin{frame}{Kỹ năng đối chiếu chứng từ (Vouching)}
    \begin{itemize}
        \item Kế toán viên phải làm gì tiếp theo? $\rightarrow$ Đi tìm \textbf{Bằng chứng kế toán}.
        \item Để xác minh 3 giao dịch trên, bạn sẽ yêu cầu phòng kế toán cung cấp hồ sơ gì?
        \begin{itemize}
            \item Hóa đơn đỏ (Hóa đơn điện tử).
            \item Ủy nhiệm chi / Sổ phụ ngân hàng.
            \item Hợp đồng kinh tế / Biên bản bàn giao.
            \item Chữ ký phê duyệt của Giám đốc.
        \end{itemize}
    \end{itemize}
\end{frame}

% SLIDE 29
\begin{frame}{Cách xử lý khi phát hiện gian lận}
    Nếu phát hiện gian lận thật sự (VD: Cố tình chẻ nhỏ hóa đơn làm 3 lần để né mức trần phê duyệt của Giám đốc tài chính):
    \begin{itemize}
        \item Tuyệt đối \textbf{bảo mật} thông tin, không làm "rút dây động rừng".
        \item Báo cáo trực tiếp (Bằng văn bản) cho Trưởng ban kiểm soát / Giám đốc.
        \item Không bao giờ để AI tự ra quyết định buộc tội thay con người.
    \end{itemize}
\end{frame}

% SLIDE 30
\begin{frame}{Lập Báo cáo Kiểm toán (Audit Report)}
    \begin{itemize}
        \item Cuối ngày làm việc, bạn phải nộp một báo cáo cho Sếp.
        \item \textbf{Nội dung:} 
        \begin{itemize}
            \item Tổng số giao dịch đã quét (VD: 5.000).
            \item Số lượng giao dịch bị nghi ngờ (VD: 45).
            \item Các loại rủi ro được phát hiện (Chi tiết theo biểu đồ Pivot Chart).
            \item Khuyến nghị hành động tiếp theo.
        \end{itemize}
    \end{itemize}
\end{frame}

% SLIDE 31
\begin{frame}{Đánh giá hiệu quả công nghệ}
    \begin{itemize}
        \item Hãy thử tưởng tượng: Nếu bạn phải dò 5.000 dòng này bằng mắt thường, bạn sẽ mất bao lâu? (Vài tuần?).
        \item Nhờ kết hợp Excel + AI Prompt, chúng ta đã làm xong việc của 1 tuần chỉ trong vòng \textbf{1 buổi học}.
        \item Đây chính là sức mạnh của No-code Accounting!
    \end{itemize}
\end{frame}

\section{Tổng kết và Q\&A}

% SLIDE 32
\begin{frame}{Tóm tắt kiến thức thực hành cốt lõi}
    \begin{itemize}
        \item \textbf{Outliers (Bất thường):} Là dấu vết để lại của tội phạm kinh tế.
        \item \textbf{Conditional Formatting + Hàm Logic (WEEKDAY, MOD):} Là công cụ quét rủi ro cực nhanh.
        \item \textbf{Prompt AI:} Giúp sinh viên kế toán không cần học thuộc công thức, chỉ cần có TƯ DUY tìm kiếm.
        \item \textbf{Analyze Data / Advanced Data Analysis:} AI tự động quét và phân tích điểm bất thường mức độ cao.
    \end{itemize}
\end{frame}

% SLIDE 33
\begin{frame}{Cảnh báo Bảo mật Dữ liệu (Data Privacy)}
    \begin{center}
        \Huge \textbf{STOP!}
    \end{center}
    \vspace{0.5cm}
    \begin{itemize}
        \item \textbf{TUYỆT ĐỐI KHÔNG} tải (upload) dữ liệu sổ sách \textbf{THẬT} của công ty bạn (có tên khách hàng, mã số thuế thực) lên ChatGPT bản miễn phí.
        \item AI có thể thu thập dữ liệu này để huấn luyện, gây lộ bí mật kinh doanh.
        \item Luôn phải "Mã hóa" (Masking) dữ liệu trước khi dùng AI trên đám mây, hoặc sử dụng hệ thống AI nội bộ (Private LLMs).
    \end{itemize}
\end{frame}

% SLIDE 34
\begin{frame}{Q \& A và Nộp bài}
    \begin{center}
        \Huge \textbf{HỎI \& ĐÁP}
    \end{center}
    \vspace{0.5cm}
    \textit{Hướng dẫn nộp bài:}
    \begin{itemize}
        \item Lưu file Excel \texttt{NhatKyChung\_Day05\_[MSSV].xlsx} đã có Conditional Formatting.
        \item Lưu kết quả phân tích Pivot Table vào Sheet 2.
        \item Nộp lên hệ thống LMS của trường trước 23:59 hôm nay.
    \end{itemize}
\end{frame}

\end{document}
"""

with open(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\Slide_AIAcc_v2_Day05_TH.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)
