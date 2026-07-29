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

\title[Buổi 4: Thực hành Persona AI]{Thực hành Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.3cm} \Large Buổi 4: Thực hành Thiết lập Persona \& Trợ lý Kế toán AI}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

% SLIDE 1
\begin{frame}
    \titlepage
    \begin{center}
        \includegraphics[width=0.5\textwidth,height=2.5cm,keepaspectratio]{images/Day_04_TH/bg_day4_th.png}
    \end{center}
\end{frame}

% SLIDE 2
\begin{frame}{Nội dung Buổi thực hành}
    \tableofcontents
\end{frame}

% SLIDE 3
\begin{frame}{Trích dẫn truyền cảm hứng}
    \begin{quote}
        ``Trong thời đại AI, làm kế toán không chỉ là lướt qua các bảng tính sổ cái; mà là đón nhận và điều hướng làn sóng của cuộc cách mạng kỹ thuật số.''
    \end{quote}
    \vspace{0.5cm}
    \begin{flushright}
        -- \textit{Dr. Martijn van Otterlo, Đại học Tilburg}
    \end{flushright}
    \vspace{0.5cm}
    \textbf{Nhận định:} Kế toán sẽ không bị đào thải bởi AI. Chỉ những người không biết dùng AI mới bị đào thải.
\end{frame}

\section{1. Mục tiêu và Chuẩn bị (Setting the Stage)}

% SLIDE 4
\begin{frame}{Chuẩn bị Môi trường (Setting the stage)}
    \begin{itemize}
        \item \textbf{Công cụ cần có:}
        \begin{itemize}
            \item Trình duyệt Web hiện đại (Google Chrome hoặc Microsoft Edge).
            \item Tài khoản OpenAI (ChatGPT) hoặc Microsoft Copilot.
            \item Kết nối Internet ổn định.
        \end{itemize}
        \item \textbf{Tư duy:} Sẵn sàng giao tiếp với máy móc như một người đồng nghiệp.
    \end{itemize}
\end{frame}

% SLIDE 5
\begin{frame}{Tại sao AI cần có "Nhân dạng" (Persona)?}
    \begin{itemize}
        \item Khi bạn hỏi ChatGPT một câu bình thường, nó sẽ trả lời theo kiểu "Bách khoa toàn thư", rất chung chung và lan man.
        \item Trong kế toán, mỗi vị trí (Kế toán thuế, Kế toán trưởng, Kiểm toán viên) có cách tư duy và hệ quy chuẩn pháp lý khác nhau.
        \item \textbf{Kỹ thuật Persona (Đóng vai):} Buộc AI phải tư duy trong một giới hạn nghề nghiệp cụ thể và chuyên sâu.
    \end{itemize}
\end{frame}

\section{2. Kỹ thuật thiết lập Persona cho AI}

% SLIDE 6
\begin{frame}{Kỹ thuật Persona là gì?}
    Persona (Nhân dạng) là việc cung cấp cho AI một vai trò cụ thể trước khi giao việc.
    \vspace{0.3cm}
    \\ \textbf{Công thức Prompt Persona:}
    \begin{enumerate}
        \item \textbf{Đóng vai (Act as):} Bạn là ai?
        \item \textbf{Mục tiêu (Goal):} Bạn cần giải quyết vấn đề gì?
        \item \textbf{Bối cảnh (Context):} Quy định/Luật áp dụng là gì?
        \item \textbf{Định dạng (Format):} Trả kết quả dưới dạng nào (Bảng, gạch đầu dòng)?
    \end{enumerate}
\end{frame}

% SLIDE 7
\begin{frame}{Xây dựng Persona "Kế toán trưởng"}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Prompt Mẫu:} 
        \\ \textit{"Hãy đóng vai một Kế toán trưởng với 15 năm kinh nghiệm tại Việt Nam. Bạn nắm rất rõ Thông tư 200/2014/TT-BTC. Nhiệm vụ của bạn là kiểm tra các nghiệp vụ kế toán tôi đưa ra, chỉ ra lỗi sai (nếu có) và hướng dẫn định khoản. Hãy luôn trích dẫn cơ sở pháp lý."}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_04_TH/chatgpt_persona.png}
    \end{columns}
\end{frame}

% SLIDE 8
\begin{frame}{Hệ quả của việc dùng Persona}
    \begin{itemize}
        \item \textbf{Không có Persona:} AI trả lời ngắn gọn: \textit{Nợ 642, Có 111.} (Đúng nhưng thiếu chuyên môn).
        \item \textbf{Có Persona Kế toán trưởng:} AI sẽ phân tích: \textit{"Theo TT200, chi phí này phục vụ quản lý doanh nghiệp nên hạch toán vào TK 642. Nếu thanh toán bằng tiền mặt, ghi Có 111. Tuy nhiên, lưu ý hóa đơn trên 20 triệu đồng phải thanh toán không dùng tiền mặt để được khấu trừ thuế GTGT..."}
    \end{itemize}
\end{frame}

\section{3. Thực hành 1: AI làm "Kế toán thanh toán"}

% SLIDE 9
\begin{frame}{Tình huống Thực hành 1 (Định khoản)}
    \begin{itemize}
        \item Công ty bạn vừa mua một phần mềm Kế toán trị giá 60.000.000đ (chưa gồm 10\% VAT), thanh toán bằng chuyển khoản ngân hàng. 
        \item Thời gian phân bổ dự kiến là 3 năm.
        \item \textbf{Yêu cầu:} Dùng ChatGPT (đã thiết lập Persona Kế toán trưởng) để định khoản nghiệp vụ mua phần mềm và bút toán phân bổ tháng đầu tiên.
    \end{itemize}
\end{frame}

% SLIDE 10
\begin{frame}{Nhập Prompt cho Tình huống 1}
    \begin{itemize}
        \item Mở ChatGPT / Copilot.
        \item Copy đoạn Prompt Persona Kế toán trưởng và dán vào.
        \item Gửi tiếp nội dung nghiệp vụ mua phần mềm.
        \item Quan sát cách AI xử lý \textbf{Tài khoản 242 (Chi phí trả trước)} thay vì đưa thẳng vào Chi phí trong kỳ.
    \end{itemize}
\end{frame}

% SLIDE 11
\begin{frame}{Đánh giá Kết quả của AI}
    \begin{itemize}
        \item AI có chỉ ra được số tiền VAT là 6.000.000đ không?
        \item Phân bổ tháng đầu tiên: $60.000.000 / (3 \times 12) = 1.666.667$ đ.
        \item \textbf{Bút toán phân bổ:} Nợ TK 642 / Có TK 242 số tiền 1.666.667 đ.
        \item AI có trích dẫn đúng tài khoản theo TT200 không?
    \end{itemize}
\end{frame}

% SLIDE 12
\begin{frame}{Tình huống "Mẹo" (Trick Question)}
    Thử kiểm tra AI bằng một nghiệp vụ sai luật kế toán.
    \vspace{0.3cm}
    \\ \textbf{Prompt:} \textit{"Sếp tôi vừa dùng quỹ tiền mặt của công ty (TK 111) để mua một chiếc xe máy SH giá 100 triệu cho con gái sếp đi học. Hãy định khoản."}
    \vspace{0.3cm}
    \\ Xem AI "Kế toán trưởng" phản ứng thế nào với giao dịch không phục vụ mục đích kinh doanh!
\end{frame}

% SLIDE 13
\begin{frame}{Xử lý Tình huống Mẹo}
    \begin{itemize}
        \item AI chuẩn sẽ \textbf{từ chối} ghi nhận đây là tài sản công ty (TK 211) hay chi phí hợp lý.
        \item AI sẽ gợi ý hạch toán vào Phải thu khác (Nợ 1388) hoặc trừ vào Lương/Cổ tức của Giám đốc.
        \item Nếu AI vẫn cho ghi vào TK 211, bạn cần chỉnh lại Prompt Persona để AI "thuộc luật" hơn.
    \end{itemize}
\end{frame}

\section{4. Thực hành 2: Phân bổ chi phí \& Dự báo}

% SLIDE 14
\begin{frame}{AI trong Kế toán Quản trị}
    \begin{itemize}
        \item Kế toán quản trị cần các quyết định phân bổ chi phí (Cost Allocation) và dự báo (Financial Forecasting).
        \item Sự phức tạp nằm ở việc có quá nhiều biến số thay đổi và dữ liệu lớn.
    \end{itemize}
\end{frame}

% SLIDE 15
\begin{frame}{Tình huống Thực hành 2 (Phân bổ chi phí)}
    \begin{itemize}
        \item Doanh nghiệp sản xuất có hóa đơn tiền điện 120.000.000đ dùng chung cho 3 phân xưởng.
        \item Dữ liệu giờ máy hoạt động: Phân xưởng 1 (1.000 giờ), Phân xưởng 2 (1.500 giờ), Phân xưởng 3 (2.500 giờ).
        \item \textbf{Yêu cầu:} Đổi Persona AI thành "Kế toán Quản trị", yêu cầu lập bảng phân bổ tiền điện theo giờ máy hoạt động.
    \end{itemize}
\end{frame}

% SLIDE 16
\begin{frame}{Nhập Prompt \& Lấy kết quả}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Prompt thêm:} 
        \\ \textit{"Hãy trình bày kết quả dưới dạng Bảng (Table), bao gồm các cột: Tên Phân Xưởng, Giờ Máy, Tỷ lệ \%, Số tiền phân bổ."}
        \\ AI không chỉ tính toán đúng mà còn format thành bảng markdown rất đẹp, sẵn sàng copy vào Excel.
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_04_TH/cost_allocation.png}
    \end{columns}
\end{frame}

% SLIDE 17
\begin{frame}{Sự tiến hóa của Dự báo Tài chính}
    \begin{itemize}
        \item \textbf{Phương pháp cũ:} Dựa vào Excel, kéo công thức xu hướng (Trendline). Rất thụ động và tuyến tính.
        \item \textbf{AI hiện đại (Deep Learning):} Nhận diện mô hình, bất thường, và yếu tố bên ngoài. Chuyển từ "Dự báo tuyến tính" sang "Dự báo đa chiều".
    \end{itemize}
\end{frame}

% SLIDE 18
\begin{frame}{Tình huống Dự báo cơ bản với ChatGPT}
    \textbf{Prompt:}
    \vspace{0.2cm}
    \textit{"Doanh thu 6 tháng đầu năm của công ty lần lượt là: 10, 12, 11, 15, 18, 20 tỷ. 
    \\ Ngân sách marketing tương ứng là: 1, 1, 1.2, 1.5, 2, 2.5 tỷ. 
    \\ Tháng tới tôi dự định cắt giảm marketing còn 1 tỷ, hãy dự báo doanh thu tháng 7 và giải thích lý do."}
\end{frame}

% SLIDE 19
\begin{frame}{Phân tích kết quả Dự báo của AI}
    \begin{itemize}
        \item AI sẽ nhận thấy mối tương quan (Correlation) chặt chẽ giữa Ngân sách marketing và Doanh thu.
        \item AI sẽ cảnh báo sự sụt giảm doanh thu mạnh nếu cắt giảm marketing đột ngột, chứ không đơn thuần chỉ tính trung bình cộng như Excel.
    \end{itemize}
\end{frame}

\section{5. Quản lý Quan hệ Khách hàng (Client Relationships)}

% SLIDE 20
\begin{frame}{Kế toán đâu chỉ có những con số?}
    \begin{itemize}
        \item Quản lý công việc kế toán đòi hỏi giao tiếp nhiều với đối tác, khách hàng, nhà cung cấp.
        \item Đặc biệt là các tình huống tế nhị: Đòi nợ, xin gia hạn nợ, giải thích sai sót hóa đơn.
    \end{itemize}
\end{frame}

% SLIDE 21
\begin{frame}{Nâng tầm quan hệ với AI}
    \begin{itemize}
        \item Công nghệ NLP (Xử lý ngôn ngữ tự nhiên) giúp AI hiểu sắc thái cảm xúc trong email của khách hàng.
        \item AI có thể soạn thảo các email chuyên nghiệp, giúp giữ vững mối quan hệ (Client Relationships).
    \end{itemize}
\end{frame}

% SLIDE 22
\begin{frame}{Thực hành 3: Viết Email Khó}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Tình huống:} Khách VIP (Cty XYZ) trễ nợ 45 ngày số tiền 500 triệu. Đã gọi 2 lần nhưng hứa lèo.
        \vspace{0.2cm}
        \\ \textbf{Yêu cầu:} Dùng ChatGPT soạn một email nhắc nợ. Văn phong: Lịch sự nhưng kiên quyết, đề cập sẽ tính lãi chậm trả sau 3 ngày nữa.
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_04_TH/email_drafting.png}
    \end{columns}
\end{frame}

% SLIDE 23
\begin{frame}{Tùy chỉnh Email với Persona}
    \begin{itemize}
        \item Bạn có thể nói với ChatGPT: \textit{"Email này hơi gay gắt, hãy làm cho nó mềm mỏng hơn để không mất lòng khách hàng, thêm lời chúc sức khỏe vào đầu thư."}
        \item Khả năng tùy chỉnh ngôn từ (Tone \& Voice) của AI là không có giới hạn, giúp bạn gỡ rối các pha giao tiếp "đi vào lòng đất".
    \end{itemize}
\end{frame}

% SLIDE 24
\begin{frame}{AI trong Lên lịch trình (Scheduling)}
    \begin{itemize}
        \item Lên lịch họp thủ công qua email thường dẫn đến cảnh "gửi qua gửi lại 5 lần" mới chốt được giờ.
        \item Tương lai: AI tự quét lịch của hai bên và đề xuất khung giờ tối ưu nhất.
        \item Tiết kiệm thời gian (Time savings) là lợi ích lớn nhất của AI trong quản lý hành chính Kế toán.
    \end{itemize}
\end{frame}

\section{6. Kiểm soát và Soát xét (Internal Controls)}

% SLIDE 25
\begin{frame}{AI trong vai trò Kiểm soát viên}
    \begin{itemize}
        \item Thiết lập Persona mới: "Kiểm toán viên Nội bộ".
        \item \textbf{Nhiệm vụ:} Phát hiện điểm bất thường (Anomaly detection) trong tập dữ liệu để ngăn chặn gian lận.
    \end{itemize}
\end{frame}

% SLIDE 26
\begin{frame}{Thực hành 4: Tìm điểm bất thường}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Tình huống:} Trong sổ quỹ tiền mặt (TK 111) có một đoạn giao dịch:
        \vspace{0.2cm}
        \textit{"Ngày Chủ nhật, 10:00 Tối - Rút tiền mặt 50 triệu - Nội dung: Tạm ứng cho Giám đốc."}
        \vspace{0.2cm}
        \\ \textbf{Yêu cầu:} Đưa đoạn dữ liệu này cho ChatGPT và hỏi \textit{"Có rủi ro kiểm soát nội bộ nào không?"}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_04_TH/anomaly_detection.png}
    \end{columns}
\end{frame}

% SLIDE 27
\begin{frame}{Nhận diện Cờ đỏ (Red Flags)}
    AI sẽ lập tức báo cờ đỏ (Red Flag):
    \begin{enumerate}
        \item Rút tiền mặt số lượng lớn vào ngày nghỉ (Chủ nhật).
        \item Giao dịch ngoài giờ hành chính (10:00 Tối).
        \item Tại sao lại "tạm ứng" tiền mặt vào giờ mà công ty không hoạt động?
    \end{enumerate}
    $\rightarrow$ Rủi ro biển thủ, ghi khống chứng từ để lấy tiền mặt.
\end{frame}

% SLIDE 28
\begin{frame}{Tổng kết sức mạnh của Persona}
    \begin{itemize}
        \item Không có AI giỏi nhất, chỉ có người viết Prompt giỏi nhất.
        \item Bằng cách thay đổi Persona (Kế toán thanh toán $\rightarrow$ Kế toán quản trị $\rightarrow$ Kiểm toán viên), bạn biến ChatGPT thành một \textbf{Phòng Kế toán ảo} với đầy đủ nhân sự.
    \end{itemize}
\end{frame}

% SLIDE 29
\begin{frame}{Rủi ro bảo mật dữ liệu (Data Privacy)}
    \begin{center}
        \Huge \textbf{CẢNH BÁO ĐỎ}
    \end{center}
    \vspace{0.3cm}
    \begin{itemize}
        \item Tuyệt đối \textbf{KHÔNG} đưa thông tin thật của khách hàng, số tài khoản ngân hàng thật, tên thật của công ty lên ChatGPT bản miễn phí.
        \item AI sẽ dùng dữ liệu đó để huấn luyện mô hình. Hãy luôn ẩn danh hóa dữ liệu (Anonymize data) trước khi dùng AI.
    \end{itemize}
\end{frame}

% SLIDE 30
\begin{frame}{Bài tập về nhà (Assignment)}
    \begin{itemize}
        \item Dùng ChatGPT (Persona Kế toán trưởng) định khoản một danh sách gồm 10 nghiệp vụ kinh tế phát sinh phức tạp.
        \item Yêu cầu AI xuất kết quả ra dạng Bảng.
        \item Copy Bảng đó dán vào Excel và nộp lại trên hệ thống E-learning của trường.
    \end{itemize}
\end{frame}

% SLIDE 31
\begin{frame}{Tóm tắt Buổi Thực hành}
    \begin{itemize}
        \item \textbf{Persona:} Chìa khóa để mở khóa tư duy chuyên ngành của AI.
        \item \textbf{Định khoản \& Phân bổ:} AI tính toán nhanh, trích dẫn đúng luật và format bảng biểu đẹp mắt.
        \item \textbf{Giao tiếp:} AI là trợ thủ đắc lực soạn thảo email, xử lý các tình huống khó nhằn với khách hàng.
    \end{itemize}
\end{frame}

% SLIDE 32
\begin{frame}{Kết thúc}
    \begin{center}
        \Huge \textbf{Q \& A}
    \end{center}
    \vspace{0.5cm}
    \textbf{Kinh nghiệm xử lý khi AI trả lời sai (Hallucination):}
    \begin{itemize}
        \item Hãy cung cấp thêm Context (Ví dụ: Trích dẫn một điều khoản trong Thông tư 200) và yêu cầu AI đọc lại điều khoản đó trước khi định khoản.
    \end{itemize}
\end{frame}

\end{document}
"""

with open(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\Slide_AIAcc_v2_Day04_TH.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)
