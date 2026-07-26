import os

def create_beamer_day13():
    content = r"""\documentclass[aspectratio=169,12pt]{beamer}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage{lmodern}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{multicol}
\usepackage{tikz}

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

% --- Title Page Info ---
\title[AI trong Kế toán - Buổi 13]{Kỹ thuật Viết Prompt, Khung SPARKS \& Phân tích Dữ liệu}
\subtitle{Prompt Engineering \& SPARKS Framework}
\author[Giảng viên]{Trí tuệ Nhân tạo cho Kế toán (AI in Accounting)}
\institute[Đại học]{Khoa Kế toán - Kiểm toán}
\date{Buổi học 13}

\begin{document}

% Slide 1: Title
\begin{frame}
    \titlepage
\end{frame}

% Slide 2: Mục tiêu
\begin{frame}{Mục tiêu Bài học (Learning Objectives)}
    \begin{itemize}
        \item \textbf{Chiến lược Dữ liệu:} Hiểu rõ 4 Trụ cột Phân tích qua lăng kính trận đấu thể thao.
        \item \textbf{Kỹ thuật Prompt:} Nắm vững nghệ thuật "giao tiếp" với AI (Prompt Engineering) cho nghiệp vụ Kế toán.
        \item \textbf{Khung Tư duy SPARKS:} Áp dụng phương pháp luận chuẩn hóa 6 bước vào dự án phân tích kế toán thực tế.
        \item \textbf{Nhận diện Rủi ro:} Cảnh giác với "Hộp đen", ảo giác số liệu và vấn đề đạo đức của AI.
    \end{itemize}
\end{frame}

% Slide 3: Agenda
\begin{frame}{Nội dung Chính (Agenda)}
    \tableofcontents
\end{frame}

% ==========================================
\section{Khởi động \& Sự dịch chuyển vĩ đại}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 5
\begin{frame}{Sự Dịch chuyển Vĩ đại của Nghề Kế toán}
    \begin{itemize}
        \item \textbf{Trước đây:} Kế toán chủ yếu cặm cụi ghi chép lịch sử, khóa sổ, đối chiếu. (Tư duy phản ứng).
        \item \textbf{Hiện nay \& Tương lai:} Sử dụng dữ liệu và AI để "kiến tạo tương lai".
        \item Không chỉ dọn dẹp quá khứ, mà còn dự báo và định hướng chiến lược.
    \end{itemize}
\end{frame}

% Slide 6
\begin{frame}{Kính viễn vọng Tiên đoán}
    \begin{quote}
        "Phân tích tài chính là một quá trình làm sạch, điều chỉnh và chuyển đổi dữ liệu thành những hiểu biết sâu sắc. Sự ra đời của AI đã biến quá trình này từ một \textbf{chiếc gương chiếu hậu} trở thành một \textbf{chiếc kính viễn vọng tiên đoán} mạnh mẽ."\\
        \vspace{0.2cm}
        -- \textbf{Wayne R. Landsman}, Moody’s Analytics
    \end{quote}
    \begin{itemize}
        \item AI phát hiện mô hình rủi ro tự động và đưa ra các cảnh báo trước thời hạn.
    \end{itemize}
\end{frame}


% ==========================================
\section{Chiến lược Dữ liệu \& 4 Trụ cột Phân tích}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 8
\begin{frame}{Nguyên lý Sinh tồn: Rác đầu vào = Rác đầu ra}
    \begin{itemize}
        \item Sở hữu các công cụ phân tích siêu phàm là rất tuyệt vời.
        \item Nhưng nếu nguyên liệu đầu vào có vấn đề thì sao? (Garbage In, Garbage Out).
        \item \textbf{Data Strategy (Chiến lược dữ liệu):} Bắt buộc phải có để phân loại và làm sạch dữ liệu trước khi nạp vào mô hình.
    \end{itemize}
\end{frame}

% Slide 9
\begin{frame}{Ẩn dụ: Trận đấu Thể thao Khắc nghiệt}
    \begin{itemize}
        \item Hãy coi hệ thống dữ liệu doanh nghiệp như một trận đấu thể thao.
        \item Có 4 mức độ (4 trụ cột) để chúng ta phân tích trận đấu này.
        \item Không thể nhảy cóc, phải bắt đầu từ nền tảng cơ bản nhất.
    \end{itemize}
\end{frame}

% Slide 10
\begin{frame}{Trụ cột 1: Phân tích Mô tả (Descriptive Analytics)}
    \begin{itemize}
        \item \textbf{Câu hỏi:} "Chuyện gì đã xảy ra?"
        \item \textbf{Ẩn dụ:} Việc này giống hệt như ngước nhìn lên \textbf{Bảng điểm điện tử} ở sân vận động.
        \item Cho ta biết tỷ số đang là bao nhiêu (Doanh thu tổng, Lợi nhuận quý này).
        \item \textit{Hạn chế:} Chỉ nhìn bảng điểm thì không biết tại sao đội nhà lại thua!
    \end{itemize}
\end{frame}

% Slide 11
\begin{frame}{Trụ cột 2: Phân tích Chẩn đoán (Diagnostic Analytics)}
    \begin{itemize}
        \item \textbf{Câu hỏi:} "Tại sao điều đó lại xảy ra?"
        \item \textbf{Ẩn dụ:} Giống như xem lại \textbf{Băng ghi hình quay chậm} từng pha bóng để tìm ra lỗ hổng phòng ngự.
        \item Bảng điểm báo Lợi nhuận giảm mạnh $\rightarrow$ Chẩn đoán chỉ ra thủ phạm là "Chi phí bảo trì máy móc đột ngột tăng vọt".
    \end{itemize}
\end{frame}

% Slide 12
\begin{frame}{Trụ cột 3: Phân tích Dự báo (Predictive Analytics)}
    \begin{itemize}
        \item \textbf{Câu hỏi:} "Chuyện gì sẽ xảy ra tiếp theo?"
        \item Sử dụng dữ liệu hiện tại để xây dựng các \textbf{mô hình toán học} (như Hồi quy tuyến tính).
        \item Không dự đoán bằng linh cảm!
        \item \textbf{Ví dụ Supercooters:} AI dự đoán doanh thu 2026 nếu sản lượng tăng 10\%, hoặc nếu chi phí bảo hành bất ngờ tăng vọt.
    \end{itemize}
\end{frame}

% Slide 13
\begin{frame}{Trụ cột 4: Phân tích Đề xuất (Prescriptive Analytics)}
    \begin{itemize}
        \item \textbf{Câu hỏi:} "Chúng ta nên làm gì?"
        \item Đây là \textbf{đỉnh cao thực sự} của phân tích (What-If analysis \& Tối ưu hóa).
        \item Hệ thống sẽ trả lời thẳng: Doanh nghiệp nên sản xuất bao nhiêu xe mỗi loại để \textbf{tối đa hóa biên lợi nhuận đóng góp} (Contribution Margin).
        \item Vẽ ra bản đồ chiến lược đi tốt nhất cho tổ chức.
    \end{itemize}
\end{frame}


% ==========================================
\section{Kỹ năng Sinh tồn: Kỹ thuật Viết Prompt}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 15
\begin{frame}{Prompt Engineering là gì?}
    \begin{itemize}
        \item Là "nghệ thuật và khoa học" thiết kế câu lệnh đầu vào để hướng dẫn AI (ChatGPT, Claude, Gemini).
        \item \textbf{Bản chất LLM:} AI không tự "nghĩ", nó chỉ dự đoán từ ngữ dựa trên xác suất ngữ cảnh.
        \item Không có bối cảnh chuẩn = Nhận lại những câu trả lời "rác".
    \end{itemize}
\end{frame}

% Slide 16
\begin{frame}{Nguyên tắc 1: Chỉ định vai trò (Role-based)}
    \begin{itemize}
        \item \textbf{Sai lầm:} "Hãy lập báo cáo chi phí." (Quá chung chung).
        \item \textbf{Chuẩn mực:} "Hãy đóng vai một Kế toán trưởng có 15 năm kinh nghiệm về chuẩn mực IFRS và VAS..."
        \item Gán vai trò giúp AI thiết lập đúng \textbf{giọng văn}, \textbf{độ sâu kỹ thuật} và \textbf{góc nhìn pháp lý}.
    \end{itemize}
\end{frame}

% Slide 17
\begin{frame}{Nguyên tắc 2: Cung cấp Bối cảnh \& Dữ liệu (Context \& Clarity)}
    \begin{itemize}
        \item Trình bày rõ ràng loại hình doanh nghiệp, mục tiêu kinh doanh.
        \item Dữ liệu đầu vào cần được định dạng theo cấu trúc bảng (Table) hoặc danh sách (Bullet points).
        \item Khung dữ liệu càng mạch lạc, AI giải quyết vấn đề càng sắc nét.
    \end{itemize}
\end{frame}

% Slide 18
\begin{frame}{Nguyên tắc 3: Tư duy theo Bước (Chain-of-Thought)}
    \begin{itemize}
        \item Các bài toán tài chính phức tạp (Ví dụ: tính thuế TNDN hoãn lại) rất dễ làm AI "nhầm lẫn".
        \item \textbf{Bí quyết:} Yêu cầu AI *"hãy suy nghĩ từng bước một (step-by-step) và giải thích quá trình tính toán"* trước khi đưa ra đáp án cuối cùng.
    \end{itemize}
\end{frame}

% Slide 19
\begin{frame}{Thực chiến 1: Phân tích Báo cáo Tài chính}
    \begin{itemize}
        \item \textbf{Prompt:} "\textit{Đóng vai một chuyên gia phân tích tài chính. Hãy phân tích bảng số liệu sau của Công ty A, tính toán hệ số thanh toán hiện hành, hệ số thanh toán nhanh. Sau đó đưa ra nhận xét chiến lược ngắn gọn trong đúng 3 gạch đầu dòng.}"
        \item \textbf{Kết quả:} Bạn nhận được một bản tóm tắt số liệu kèm phân tích khả năng thanh khoản cực kỳ chuyên nghiệp.
    \end{itemize}
\end{frame}

% Slide 20
\begin{frame}{Thực chiến 2: Rà soát Hóa đơn \& Thuế}
    \begin{itemize}
        \item \textbf{Prompt:} "\textit{Tôi có danh sách các giao dịch mua hàng dưới đây. Hãy lập bảng đối chiếu để xác định các khoản mục tiềm ẩn rủi ro về Thuế GTGT theo chuẩn mực hiện hành và đề xuất giải thích.}"
        \item \textbf{Kết quả:} Phát hiện điểm mù thuế mà kiểm toán viên con người dễ bỏ sót do áp lực thời gian.
    \end{itemize}
\end{frame}

% Slide 21
\begin{frame}{Sai lầm Chết người 1 \& 2}
    \begin{itemize}
        \item \textbf{1. Prompt quá chung chung:} Hỏi mơ hồ sẽ nhận lại lý thuyết suông.
        \item \textbf{2. Ảo tưởng khả năng làm Toán của AI:} LLM là mô hình ngôn ngữ (như học sinh giỏi Văn), không phải máy tính siêu bự. AI cộng trừ nhân chia những số lớn rất hay nhầm! Luôn phải kiểm tra lại công thức toán.
    \end{itemize}
\end{frame}

% Slide 22
\begin{frame}{Sai lầm Chết người 3: Rò rỉ Dữ liệu Nhạy cảm}
    \begin{itemize}
        \item \textbf{Tuyệt đối không:} Đưa tên thật của khách hàng, mã số thuế bí mật, số thẻ tín dụng lên các công cụ AI công cộng (như ChatGPT bản free).
        \item Hành động đó có thể vi phạm trắng trợn Luật bảo vệ quyền riêng tư (GDPR) và đẩy lãnh đạo công ty vào vòng lao lý.
    \end{itemize}
\end{frame}


% ==========================================
\section{Khởi động Dự án với Khung Tư duy SPARKS}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 24
\begin{frame}{Khung Tư duy SPARKS là gì?}
    \begin{itemize}
        \item \textbf{SPARKS Framework} là một quy trình làm việc chuẩn hóa, có tính hệ thống được thiết kế riêng cho Kế toán viên.
        \item Giúp triển khai các dự án Phân tích dữ liệu kế toán một cách khoa học, chuyên nghiệp, không bị bỏ sót các yếu tố rủi ro.
    \end{itemize}
\end{frame}

% Slide 25
\begin{frame}{Các bước S.P.A.}
    \begin{itemize}
        \item \textbf{S - State the Question (Xác định Câu hỏi):} Phân tích không bắt đầu từ dữ liệu, mà bắt đầu từ vấn đề kinh doanh. (Ví dụ: "Tại sao chi phí mua hàng Quý 4 tăng đột biến?").
        \item \textbf{P - Partition the Data (Phân chia \& Thu gọn):} Rút trích đúng các trường dữ liệu cần thiết từ hệ thống ERP khổng lồ (bỏ bớt thông tin thừa).
        \item \textbf{A - Analyze the Data (Thực hiện Phân tích):} Áp dụng 1 trong 4 trụ cột phân tích (Mô tả, Chẩn đoán, Dự báo, Đề xuất).
    \end{itemize}
\end{frame}

% Slide 26
\begin{frame}{Các bước R.K.S.}
    \begin{itemize}
        \item \textbf{R - Refine the Analysis (Tinh chỉnh Phân tích):} Chú ý các giá trị ngoại lai (Outliers). Một lỗi gõ dư số 0 của thư ký có thể làm sai bét toàn bộ mô hình.
        \item \textbf{K - Communicate the Insights (Truyền đạt):} Biến số liệu thô thành các Dashboards hoặc biểu đồ mạch lạc để sếp dễ chốt hạ.
        \item \textbf{S - Stop and Reflect (Dừng lại \& Suy ngẫm):} Rà soát xem thông tin đã thực sự trả lời được bài toán kinh doanh ban đầu chưa?
    \end{itemize}
\end{frame}

% Slide 27
\begin{frame}{Thực hành SPARKS: Tài khoản Phải trả (Accounts Payable)}
    \begin{itemize}
        \item \textbf{Bối cảnh:} Quản lý cơ sở dữ liệu hàng ngàn hóa đơn từ nhà cung cấp.
        \item \textbf{Các trường Dữ liệu (Data Dictionary):}
        \begin{itemize}
            \item \texttt{InvoiceNo, InvoiceAmount, InvoiceDate}
            \item \texttt{VendorID, VendorName}
            \item \texttt{QualityRating} (Đánh giá chất lượng 1-5)
            \item \texttt{PONo} (Số Purchase Order)
        \end{itemize}
    \end{itemize}
\end{frame}

% Slide 28
\begin{frame}{Case Study 1: Truy tìm Hóa đơn Bất thường}
    \begin{itemize}
        \item \textbf{S (Câu hỏi):} Có giao dịch nào bất thường (gian lận, sai sót) không?
        \item \textbf{A (Phân tích):} Vẽ \textbf{Biểu đồ phân tán (Scatter Plot)} với trục X (Ngày hóa đơn) và trục Y (Số tiền).
        \item \textbf{R (Tinh chỉnh):} Các điểm nằm tách biệt quá cao trên trục Y $\rightarrow$ Outliers cần kiểm tra lập tức (lỗi gõ phím hay gian lận?).
        \item \textbf{K (Truyền đạt):} Gửi báo cáo 5 hóa đơn cao bất thường cho Kế toán trưởng.
    \end{itemize}
\end{frame}

% Slide 29
\begin{frame}{Case Study 2: Chấm điểm Chất lượng Nhà cung cấp}
    \begin{itemize}
        \item \textbf{S (Câu hỏi):} Đối tác nào làm ăn tệ nhất?
        \item \textbf{P \& A:} Tính hàm trung bình (\texttt{AVERAGE}) của chỉ số \texttt{QualityRating} theo từng \texttt{VendorName}.
        \item \textbf{R (Tinh chỉnh):} Coi chừng! Nhà cung cấp A giao 1 đơn (điểm 5/5) so với NCC B giao 100 đơn (điểm 4.8/5) $\rightarrow$ Không thể chỉ nhìn điểm trung bình mà bỏ qua quy mô.
    \end{itemize}
\end{frame}


% ==========================================
\section{Bãi mìn Rủi ro: Hộp đen \& Đạo đức AI}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 31
\begin{frame}{Bơm AI vào Hệ thống: Động cơ vs. Bãi mìn}
    \begin{itemize}
        \item Khi chúng ta có Chiến lược dữ liệu chuẩn, việc tích hợp AI sẽ tạo ra một \textbf{Động cơ siêu tốc độ}.
        \item Nhưng đồng thời, nó cũng mở ra một \textbf{Bãi mìn rủi ro} chưa từng có.
    \end{itemize}
\end{frame}

% Slide 32
\begin{frame}{Rủi ro 1: Thảm họa Bảo mật}
    \begin{itemize}
        \item Nếu hệ thống thiếu mã hóa, hậu quả sẽ cực kỳ thảm khốc.
        \item \textbf{Ví dụ đau thương:} Vụ rò rỉ dữ liệu lịch sử của Equifax năm 2017. Thông tin tài chính của hàng triệu người bị phơi bày chỉ vì một lỗ hổng bảo mật không được vá.
    \end{itemize}
\end{frame}

% Slide 33
\begin{frame}{Khái niệm "Pháo đài Dữ liệu"}
    \begin{itemize}
        \item \textbf{Giải pháp:} Tuân thủ nghiêm ngặt chuẩn bảo mật GDPR (Châu Âu) hoặc CCPA (Mỹ).
        \item Các nền tảng AI doanh nghiệp (Enterprise) bọc dữ liệu trong một "pháo đài", không sử dụng để huấn luyện AI cộng đồng.
    \end{itemize}
\end{frame}

% Slide 34
\begin{frame}{Rủi ro 2: Hiện tượng Hộp đen (Black Box)}
    \begin{itemize}
        \item Máy tính quyết định quá nhanh, nhưng lại không thể "giải thích" vì sao nó làm thế!
        \item \textbf{Giao dịch Tần suất cao (HFT - High Frequency Trading):} Mua bán hàng ngàn cổ phiếu trong một tích tắc.
        \item \textbf{Lo ngại:} Không một kiểm toán viên nào biết bên trong cái hộp đen đó thuật toán đang tính toán cái gì. Có thể gây sụp đổ thị trường Flash Crash.
    \end{itemize}
\end{frame}

% Slide 35
\begin{frame}{Rủi ro 3: Đạo đức \& Sự thiên lệch (Bias)}
    \begin{itemize}
        \item Đây là nơi \textbf{Công nghệ va chạm với Triết học}.
        \item Bản chất AI không có lương tâm, nó chỉ tối ưu hóa "Hàm mục tiêu" được giao.
    \end{itemize}
\end{frame}

% Slide 36
\begin{frame}{Sự nhẫn tâm của Thuật toán}
    \begin{itemize}
        \item Nếu giao cho AI một quỹ đầu tư với mục tiêu duy nhất: "Tối đa hóa lợi nhuận tài chính".
        \item AI có thể mù quáng đổ hàng tỷ đô la vào \textbf{công ty nhiên liệu hóa thạch ô nhiễm} hoặc \textbf{sản xuất vũ khí}.
        \item Mặc kệ việc điều đó đi ngược lại hoàn toàn tiêu chuẩn ESG (Môi trường - Xã hội - Quản trị) của doanh nghiệp!
    \end{itemize}
\end{frame}

% Slide 37
\begin{frame}{Lỗi nằm ở AI hay Con người?}
    \begin{itemize}
        \item Bản thân công nghệ hay những đoạn mã code \textbf{không có lỗi}.
        \item Lỗi nằm ở khâu quản trị và thiết lập của con người.
        \item Chính con người đã mớm dữ liệu thiên lệch và viết ra hàm mục tiêu tàn nhẫn đó cho nó.
    \end{itemize}
\end{frame}

% Slide 38
\begin{frame}{Giải pháp Cốt lõi: Chiếc Phanh Khẩn cấp}
    \begin{itemize}
        \item Phải thiết lập cơ chế giám sát liên tục.
        \item \textbf{Nguyên tắc tối thượng:} Máy móc đưa ra thông tin và đề xuất, nhưng con người phải chịu trách nhiệm.
        \item Kế toán trưởng luôn phải giữ quyền "đạp phanh khẩn cấp" và chốt hạ quyết định.
    \end{itemize}
\end{frame}

% Slide 39
\begin{frame}{Định nghĩa lại Vai trò}
    \begin{itemize}
        \item Các bạn sinh viên sẽ không ra trường để làm thợ nhập liệu (Data Entry) nhàm chán.
        \item Các bạn sẽ trở thành những \textbf{Cố vấn Chiến lược (Strategic Advisors)}.
        \item Đọc hiểu mô hình, đánh giá rủi ro, và điều hướng chiến lược cho tổ chức.
    \end{itemize}
\end{frame}

% Slide 40
\begin{frame}{Câu hỏi Mở (Kích thích Tư duy)}
    \begin{center}
        \textit{"Nếu trong tương lai, AI đảm nhận trọn vẹn việc phân tích, dự báo với độ chính xác vượt xa con người... \\
        Thì giá trị không thể thay thế của một chuyên gia tài chính là gì?"}
    \end{center}
\end{frame}

% Slide 41
\begin{frame}{Đặc quyền của Con người}
    \begin{itemize}
        \item Giá trị thực sự không còn nằm ở kỹ năng cộng trừ nhân chia hay lập bảng tính Excel siêu phàm.
        \item Nó nằm ở \textbf{Trực giác Đạo đức} và \textbf{Sự thấu cảm triết học}.
        \item Những thứ vô hình mà không một dòng code nào có thể lập trình được.
    \end{itemize}
\end{frame}

% Slide 42
\begin{frame}{Tổng kết Bài học}
    \begin{itemize}
        \item \textbf{4 Trụ cột Phân tích:} Mô tả, Chẩn đoán, Dự báo, Đề xuất (Nhìn bảng điểm \& Xem lại băng hình).
        \item \textbf{Prompt Engineering:} Gán vai trò, cung cấp bối cảnh, tư duy theo bước. Cảnh giác với số học của AI.
        \item \textbf{SPARKS Framework:} 6 bước chuẩn hóa giải quyết dự án kế toán (VD: Tìm hóa đơn bất thường).
        \item \textbf{Quản trị Rủi ro:} Bảo mật (Equifax), Hiện tượng Hộp đen, và hàm mục tiêu vô đạo đức của thuật toán.
    \end{itemize}
\end{frame}

% Slide 43
\begin{frame}{Hỏi đáp (Q\&A)}
    \begin{center}
        \Large \textbf{Cảm ơn các bạn đã lắng nghe!}\\
        \vspace{1cm}
        Bạn có câu hỏi nào về Kỹ thuật Prompt, Khung SPARKS, hay vấn đề Đạo đức của AI trong ngành Tài chính không?
    \end{center}
\end{frame}

\end{document}
"""
    tex_path = os.path.join("TaiLieu", "slideAIAcc", "Slide_AIAcc_Day13.tex")
    os.makedirs(os.path.dirname(tex_path), exist_ok=True)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Generated {tex_path} successfully.")

if __name__ == '__main__':
    create_beamer_day13()
