import os

def create_beamer_day03():
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
\title[AI trong Kế toán - Buổi 3]{Tương lai của AI, Đạo đức, Rủi ro \\\& Khai phá Dữ liệu trong Kế toán}
\subtitle{AI Ethics, Risks \& Data Mining}
\author[Giảng viên]{Trí tuệ Nhân tạo cho Kế toán (AI in Accounting)}
\institute[Đại học]{Khoa Kế toán - Kiểm toán}
\date{Buổi học 03}

\begin{document}

% Slide 1: Title
\begin{frame}
    \titlepage
\end{frame}

% Slide 2: Mục tiêu
\begin{frame}{Mục tiêu Bài học (Learning Objectives)}
    \begin{itemize}
        \item \textbf{Học sâu \& Khai phá dữ liệu:} Hiểu cách AI chuyển từ "tính toán" sang "tiên đoán" trong kinh doanh.
        \item \textbf{Tự động hóa (RPA \& API):} Ứng dụng robot phần mềm và hiểu lý do Kế toán viên cần học lập trình.
        \item \textbf{Rủi ro "Hộp đen":} Phân tích sự kiện Flash Crash và vấn đề thiếu khả năng giải thích của Deep Learning.
        \item \textbf{Thiên kiến Thuật toán:} Đánh giá rủi ro đạo đức qua case study Apple Card (2019).
        \item \textbf{Trách nhiệm giải trình:} Nắm bắt định hướng pháp lý (EU AI Act) đối với hệ thống trí tuệ nhân tạo.
    \end{itemize}
\end{frame}

% Slide 3: Agenda
\begin{frame}{Nội dung Chính (Agenda)}
    \tableofcontents
\end{frame}

% ==========================================
\section{1. Học sâu, NLP \& Khai phá Dữ liệu (Data Mining)}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 5
\begin{frame}{Bối cảnh Cách mạng Công nghiệp 4.0}
    \begin{itemize}
        \item Theo Klaus Schwab (Nhà sáng lập Diễn đàn Kinh tế Thế giới), chúng ta đang ở giữa Cách mạng Công nghiệp 4.0.
        \item \textbf{AI không còn nằm trong phòng thí nghiệm.} Nó đã ngồi ngay trong phòng họp của các Tập đoàn toàn cầu.
        \item Sự thay đổi cốt lõi: Tính minh bạch, rạch ròi "đen trắng" của Kế toán truyền thống đang bị thách thức bởi "vùng xám" của AI.
    \end{itemize}
\end{frame}

% Slide 6
\begin{frame}{Từ Tính toán (Calculation) sang Tiên đoán (Prediction)}
    \begin{itemize}
        \item Rất nhiều người lầm tưởng AI chỉ là "tự động hóa" nhanh hơn.
        \item Thực tế, sức mạnh của AI là \textbf{Tiên đoán (Predictive Analytics)}.
        \item Kế toán truyền thống: Nhìn vào "gương chiếu hậu" (Dữ liệu quá khứ) để lái xe.
        \item Kế toán AI: Tư duy \textbf{chủ động} (Tiên đoán xu hướng, ngăn chặn rủi ro).
    \end{itemize}
\end{frame}

% Slide 7
\begin{frame}{Case Study 1: Tiên đoán tại Lux Fashion Inc.}
    \begin{itemize}
        \item \textbf{Vấn đề:} Quyết định số lượng sản xuất trang phục cho mùa tới.
        \item \textbf{Giải pháp AI:} Thuật toán không chỉ xem lịch sử bán hàng nội bộ, mà còn "cào" (scrape) dữ liệu khổng lồ:
        \begin{itemize}
            \item Dự báo thời tiết.
            \item Xu hướng trên Mạng xã hội.
            \item Màu sắc trang phục của các ngôi sao Pop tuần qua.
        \end{itemize}
    \end{itemize}
\end{frame}

% Slide 8
\begin{frame}{Kết quả tại Lux Fashion Inc.}
    \begin{itemize}
        \item Thuật toán tìm ra những mẫu hình ẩn (hidden patterns) mà não người không thể thấy được.
        \item \textbf{Thành quả kinh doanh:} 
        \begin{itemize}
            \item Giảm \textbf{15\%} chi phí hàng tồn kho (giảm chi phí lưu kho đồ lỗi mốt).
            \item Đẩy doanh thu tăng \textbf{20\%} (luôn có sẵn mặt hàng hot).
        \end{itemize}
    \end{itemize}
\end{frame}

% Slide 9
\begin{frame}{Case Study 2: Metro Bank \& Rủi ro Tín dụng}
    \begin{itemize}
        \item Thay vì chỉ nhìn vào Điểm tín dụng truyền thống hay bảng lương.
        \item \textbf{Metro Bank áp dụng AI để:} Phân tích hành vi trực tuyến và lịch sử thanh toán các hóa đơn siêu nhỏ.
        \item \textbf{Kết quả:} Giảm được \textbf{25\%} tỷ lệ nợ xấu.
        \item \textit{Góc khuất:} Mở ra rủi ro về quyền riêng tư khi máy móc "soi mói" thói quen sinh hoạt hàng ngày của khách hàng.
    \end{itemize}
\end{frame}

% Slide 10
\begin{frame}{Bản chất "Hộp đen" của Học sâu (Deep Learning)}
    \begin{itemize}
        \item Mạng Nơ-ron Nhân tạo (ANNs) có cấu trúc phức tạp với vô số lớp ẩn (Hidden Layers), giống như não người.
        \item Khi máy học (Learn), nó tự động điều chỉnh hàng triệu "trọng số" (weights) mà không theo logic IF-THEN truyền thống.
        \item \textbf{Black Box Model:} Kỹ sư viết ra thuật toán cũng không thể giải thích chính xác \textit{TẠI SAO} AI lại đưa ra một quyết định cụ thể.
    \end{itemize}
\end{frame}

% Slide 11
\begin{frame}{Ứng dụng Học sâu trong Tái tạo Chứng từ}
    \begin{itemize}
        \item Nhận dạng Ký tự Quang học (OCR) truyền thống rất kém với hóa đơn mờ, nhòe.
        \item \textbf{Deep Learning OCR:} Tự động nhận diện cấu trúc hóa đơn phức tạp, tái tạo lại dữ liệu tài chính chính xác từ ảnh chụp biên lai nhàu nát.
        \item Trợ thủ đắc lực cho Kế toán viên trong khâu nhập liệu.
    \end{itemize}
\end{frame}

% Slide 12
\begin{frame}{Xử lý Ngôn ngữ Tự nhiên (NLP)}
    \begin{itemize}
        \item Phân nhánh cốt lõi của AI giúp máy tính làm việc với văn bản con người.
        \item \textbf{NLU (Natural Language Understanding):} Giúp máy "hiểu" ngữ cảnh (VD: Phân tích cảm xúc mạng xã hội về cổ phiếu).
        \item \textbf{NLG (Natural Language Generation):} Giúp máy "viết" báo cáo. Chuyển biểu đồ tài chính thành một đoạn văn giải thích rõ ràng.
    \end{itemize}
\end{frame}

% Slide 13
\begin{frame}{Đọc hiểu Hợp đồng thông minh với AI}
    \begin{itemize}
        \item \textbf{Hệ thống Argus (Deloitte)} và \textbf{Clara (KPMG)} có khả năng tự động trích xuất thông tin từ hợp đồng dài hàng trăm trang.
        \item Không phải là thao tác tìm kiếm "Ctrl+F" từ khóa thông thường.
        \item AI hiểu được \textbf{ngữ cảnh pháp lý}, càng đọc nhiều càng tích lũy kinh nghiệm giống như một luật sư lâu năm.
    \end{itemize}
\end{frame}

% Slide 14
\begin{frame}{Lịch sử lặp lại: AI có cướp việc của Kế toán?}
    \begin{itemize}
        \item Những năm 1980, sự xuất hiện của Microsoft Excel khiến người giữ sổ sách sợ hãi sẽ mất việc.
        \item Thực tế: Excel không giết chết nghề Kế toán, nó chỉ giải phóng con người khỏi cái cực hình cộng trừ bằng bút chì.
        \item \textbf{AI hiện tại:} Là "trợ lý siêu việt", thay thế đôi mắt và bàn tay, nhưng \textbf{không thể thay thế khối óc} mang tính phán đoán và đạo đức.
    \end{itemize}
\end{frame}

% Slide 15
\begin{frame}{Khai phá Dữ liệu (Data Mining) vs Học máy (Machine Learning)}
    \begin{itemize}
        \item \textbf{Data Mining:} Tìm kiếm các mẫu hình (patterns) và luật (rules) có ý nghĩa trong kho dữ liệu khổng lồ của quá khứ.
        \item \textbf{Machine Learning:} Sử dụng dữ liệu đó để huấn luyện mô hình và dự báo tương lai.
        \item Khai phá dữ liệu là bước đi nền tảng trước khi xây dựng bất kỳ mô hình Học máy nào trong Tài chính.
    \end{itemize}
\end{frame}

% Slide 16
\begin{frame}{Ứng dụng Data Mining: Phát hiện Ngoại lai}
    \begin{itemize}
        \item \textbf{Ngoại lai (Outliers):} Những dữ liệu nằm lệch chuẩn so với đám đông.
        \item Ứng dụng trong Kế toán \& Kiểm toán:
        \begin{itemize}
            \item Quét hàng triệu bút toán trên Sổ cái chung (General Ledger).
            \item Tự động đánh dấu những giao dịch vào "3 giờ sáng", giao dịch có giá trị bất thường so với lịch sử, hoặc trùng lặp số hóa đơn.
        \end{itemize}
    \end{itemize}
\end{frame}

% Slide 17
\begin{frame}{Khai phá Văn bản (Text Mining) \& Kế toán Pháp y}
    \begin{itemize}
        \item \textbf{Kế toán Pháp y (Forensic Accounting):} Điều tra các gian lận tài chính tinh vi.
        \item Text Mining cho phép phân tích hàng ngàn Email nội bộ, hợp đồng để phát hiện "tông giọng" (sentiment) che đậy, áp lực, hoặc những từ khóa liên quan đến gian lận (Kickback, Bribe).
    \end{itemize}
\end{frame}

% ==========================================
\section{2. Tự động hóa RPA, Ứng dụng API \& Lập trình}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 19
\begin{frame}{Tự động hóa Quy trình Bằng Robot (RPA) là gì?}
    \begin{itemize}
        \item \textbf{RPA (Robotic Process Automation):} Robot phần mềm thực hiện tự động các chuỗi thao tác lặp đi lặp lại trên máy tính (nhấp chuột, copy/paste, điền form).
        \item Giúp con người thoát khỏi công việc nhàm chán, có tính nguyên tắc cao.
        \item Các nền tảng phổ biến: UiPath, BluePrism, Automation Anywhere.
    \end{itemize}
\end{frame}

% Slide 20
\begin{frame}{Phân biệt RPA và AI}
    \begin{itemize}
        \item \textbf{RPA = Bàn tay (Cơ bắp):} Làm việc theo quy tắc (Rule-based), không biết tự tư duy, nếu quy trình thay đổi nó sẽ báo lỗi.
        \item \textbf{AI = Bộ não (Trí tuệ):} Làm việc dựa trên dữ liệu (Data-driven), có khả năng tự học, thích nghi và ra quyết định.
        \item \textit{Xu hướng:} Kết hợp cả hai tạo ra Tự động hóa Thông minh (Intelligent Automation).
    \end{itemize}
\end{frame}

% Slide 21
\begin{frame}{Ứng dụng RPA: Đối chiếu Ngân hàng}
    \begin{itemize}
        \item \textbf{Thực trạng:} Cuối tháng, Kế toán phải căng mắt đối chiếu từng dòng trên sổ phụ ngân hàng với sổ quỹ tiền mặt.
        \item \textbf{Giải pháp RPA:} 
        \begin{itemize}
            \item Tự động tải sao kê từ ngân hàng.
            \item Đối chiếu chéo mã giao dịch, số tiền.
            \item Chỉ báo cáo (Flag) những giao dịch bị lệch để con người xử lý.
        \end{itemize}
    \end{itemize}
\end{frame}

% Slide 22
\begin{frame}{Ứng dụng RPA: Theo dõi Khoản Phải Trả (AP)}
    \begin{itemize}
        \item Khi hóa đơn nhà cung cấp bay vào Email:
        \item RPA tự động đọc mail $\rightarrow$ Trích xuất hóa đơn (nhờ OCR/AI) $\rightarrow$ Đăng nhập vào phần mềm ERP (SAP/MISA) $\rightarrow$ Ghi nhận công nợ.
        \item Tốc độ xử lý tính bằng giây, hoàn toàn không có sai sót đánh máy.
    \end{itemize}
\end{frame}

% Slide 23
\begin{frame}{Giao diện Lập trình Ứng dụng (API)}
    \begin{itemize}
        \item \textbf{API (Application Programming Interface):} Cách các phần mềm giao tiếp với nhau mà không cần sự can thiệp của con người.
        \item \textbf{Ẩn dụ:} API giống như \textit{"Người bồi bàn"}. Khách hàng (Phần mềm A) gọi món, bồi bàn mang order vào Bếp (Phần mềm B), rồi bồi bàn mang món ăn (Dữ liệu) trả về bàn.
    \end{itemize}
\end{frame}

% Slide 24
\begin{frame}{Hệ sinh thái Kế toán Mở (Open Accounting)}
    \begin{itemize}
        \item Nhờ API, dữ liệu Kế toán có thể kết nối thời gian thực với Cơ quan Thuế, Ngân hàng, Sàn Thương mại Điện tử.
        \item Các dịch vụ AI mạnh mẽ được cung cấp qua API (Cắm-và-Chạy):
        \begin{itemize}
            \item \textbf{Google Prediction API}
            \item \textbf{BigML}
            \item ChatGPT API (Tích hợp trợ lý AI thẳng vào bảng tính).
        \end{itemize}
    \end{itemize}
\end{frame}

% Slide 25
\begin{frame}{Tại sao Kế toán viên cần học Lập trình?}
    \begin{itemize}
        \item Bạn không cần phải trở thành Kỹ sư Phần mềm.
        \item Tuy nhiên, hiểu \textbf{Logic Lập trình} giúp bạn giao tiếp được với dữ liệu và thiết lập các kịch bản tự động hóa hiệu quả.
        \item Năng lực này được gọi là \textbf{Tech-savvy} (Am hiểu công nghệ).
    \end{itemize}
\end{frame}

% Slide 26
\begin{frame}{Các Công cụ \& Ngôn ngữ Phổ biến}
    \begin{itemize}
        \item \textbf{Python:} Ngôn ngữ vua trong xử lý dữ liệu và AI. Rất thân thiện cho người mới bắt đầu.
        \item \textbf{R:} Phù hợp cho phân tích Thống kê chuyên sâu.
        \item \textbf{SQL (Structured Query Language):} Ngôn ngữ bắt buộc để trích xuất dữ liệu trực tiếp từ Database (Thay vì đợi IT xuất file Excel).
    \end{itemize}
\end{frame}

% Slide 27
\begin{frame}{Xu hướng "Do-It-Yourself" AI (Tự tùy biến)}
    \begin{itemize}
        \item Các nền tảng Low-code/No-code đang bùng nổ.
        \item Kế toán viên có thể tự kéo thả để huấn luyện một mô hình AI dự báo dòng tiền cho riêng doanh nghiệp của mình.
        \item Nắm vững cơ sở dữ liệu (Database) là chìa khóa để trở thành nhà phân tích tài chính quyền lực trong tương lai.
    \end{itemize}
\end{frame}


% ==========================================
\section{3. Đạo đức, Pháp luật \& Rủi ro AI Tạo sinh}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 29
\begin{frame}{Rủi ro từ Hệ thống "Hộp đen" (Black Box)}
    \begin{itemize}
        \item \textbf{Khả năng giải thích (Explainability)} là thách thức lớn nhất của AI.
        \item Kế toán, Tài chính yêu cầu tính minh bạch và rạch ròi.
        \item Nhưng khi giao quyền quyết định hàng tỷ USD cho thuật toán Deep Learning, chúng ta không thể mở mã nguồn ra để biết \textit{TẠI SAO} máy lại ra quyết định đó.
    \end{itemize}
\end{frame}

% Slide 30
\begin{frame}{Đạo đức \& Quy định AI trong Tài chính}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \begin{itemize}
                \item Sự phát triển của AI luôn đi trước hành lang pháp lý.
                \item Kế toán viên phải đối mặt với 4 thách thức cốt lõi: 
                \begin{enumerate}
                    \item Quyền riêng tư.
                    \item Thao túng thị trường.
                    \item Thiên kiến (Bias).
                    \item Mất cân bằng lao động.
                \end{enumerate}
            \end{itemize}
        \end{column}
        \begin{column}{0.5\textwidth}
            \centering
            % Require image1.jpeg in Figures/Buoi_03B/
            \includegraphics[width=\textwidth,height=0.7\textheight,keepaspectratio]{../../Figures/Buoi_03B/image1.jpeg}
        \end{column}
    \end{columns}
\end{frame}

% Slide 31
\begin{frame}{Thách thức 1: Rủi ro Giao dịch Thuật toán (Flash Crash)}
    \begin{itemize}
        \item Thuật toán Giao dịch Tần suất cao (HFT) ra lệnh trong vài phần nghìn giây.
        \item \textbf{Sự kiện 06/05/2010 (Flash Crash):} Một lệnh bán lớn kích hoạt sự hoảng loạn dây chuyền của các "hộp đen" khác.
        \item Chỉ số Dow Jones bốc hơi hàng ngàn điểm trước khi con người kịp chớp mắt và với tay tới "nút dừng khẩn cấp".
        \item Máy móc vô cảm tạo ra \textbf{Rủi ro Hệ thống}.
    \end{itemize}
\end{frame}

% Slide 32
\begin{frame}{Case Study: Kiểm kê bằng Drone (KPMG/EY)}
    \begin{itemize}
        \item Drone bay trong nhà kho lạnh lẽo để quét hình ảnh kiểm kê tài sản.
        \item \textbf{Ảo ảnh thị giác:} Drone bay vào góc khuất, bóng râm làm AI nhầm lẫn và đếm khống lên thêm 2 triệu USD hàng hóa!
        \item Kiểm toán viên tin tưởng hoàn toàn vào drone $\rightarrow$ Công ty gian lận thành công.
        \item \textit{Câu hỏi hóc búa:} Drone không thể đi tù, ai chịu trách nhiệm?
    \end{itemize}
\end{frame}

% Slide 33
\begin{frame}{Thách thức 2: Thiên kiến Thuật toán (Algorithmic Bias)}
    \begin{itemize}
        \item Sự nhầm tưởng tai hại: "Máy móc thì vô cảm và khách quan tuyệt đối".
        \item Thực tế: Máy móc học từ dữ liệu lịch sử. Mà lịch sử lại chứa đầy định kiến và phân biệt đối xử của con người.
        \item Garbage in, Garbage out (Dữ liệu rác sinh ra Quyết định rác).
    \end{itemize}
\end{frame}

% Slide 34
\begin{frame}{Case Study: Bê bối Apple Card (2019)}
    \begin{itemize}
        \item Vợ chồng dùng chung tài sản, chung điểm tín dụng nộp hồ sơ xin thẻ Apple Card (Do Goldman Sachs hợp tác phát hành).
        \item \textbf{Kết quả:} Thuật toán cấp hạn mức cho Người Chồng cao gấp \textbf{20 lần} Người Vợ.
        \item Thuật toán đã "học" ngầm sự phân biệt đối xử giới tính trong tài chính!
    \end{itemize}
\end{frame}

% Slide 35
\begin{frame}{Nguy cơ từ "Biến đại diện" (Proxy Variables)}
    \begin{itemize}
        \item Dù Kỹ sư đã \textit{xóa hẳn} cột "Giới tính" khỏi dữ liệu huấn luyện, AI vẫn tự tìm ra đường khác.
        \item \textbf{Biến đại diện:} Thói quen mua sắm ở tiệm mỹ phẩm X, đăng ký tạp chí Y.
        \item AI nhận ra nhóm người mua đồ ở tiệm X (phụ nữ) thường có lịch sử rủi ro tín dụng cao hơn trong quá khứ, và tự động trừng phạt họ.
    \end{itemize}
\end{frame}

% Slide 36
\begin{frame}{Thách thức 3: Rủi ro Quyền Riêng tư (Data Privacy)}
    \begin{itemize}
        \item AI là cỗ máy "khát khao" dữ liệu vô độ.
        \item Khi gom một lượng dữ liệu siêu khổng lồ vào một chỗ để huấn luyện AI, ta vô tình tạo ra \textbf{Hũ mật (Honeypot)} cho tin tặc.
    \end{itemize}
\end{frame}

% Slide 37
\begin{frame}{Case Study: Sự kiện Equifax (2017)}
    \begin{itemize}
        \item Equifax (Hãng báo cáo tín dụng lớn nhất Mỹ) bị chọc thủng hệ thống.
        \item Thông tin cá nhân, lịch sử vay nợ của \textbf{hàng triệu người} bị phơi bày.
        \item Một hệ thống càng thông minh thì hậu quả khi bị xâm phạm càng tàn khốc.
    \end{itemize}
\end{frame}

% Slide 38
\begin{frame}{Quy định Pháp luật Đang Bám đuổi AI}
    \begin{itemize}
        \item \textbf{GDPR (Châu Âu) \& CCPA (California):} Kiểm soát quyền dữ liệu cá nhân chặt chẽ.
        \item \textbf{EU AI Act (2024):} Đạo luật AI đầu tiên trên thế giới của Liên minh Châu Âu.
        \item Không cấm AI, nhưng áp dụng phương pháp \textbf{Tiếp cận Dựa trên Rủi ro (Risk-based approach)}.
    \end{itemize}
\end{frame}

% Slide 39
\begin{frame}{Tiếp cận Dựa trên Rủi ro (EU AI Act)}
    \begin{itemize}
        \item Cơ chế như \textbf{Đèn giao thông}:
        \begin{itemize}
            \item Lọc thư rác (Spam) $\rightarrow$ Rủi ro thấp (Đèn xanh).
            \item AI chấm điểm vay vốn tín dụng, tuyển dụng nhân sự $\rightarrow$ Rủi ro cao (Đèn đỏ).
        \end{itemize}
        \item Bắt buộc các doanh nghiệp phải giải trình minh bạch nguồn gốc dữ liệu huấn luyện cho hệ thống "Đèn đỏ".
    \end{itemize}
\end{frame}

% Slide 40
\begin{frame}{Nghịch lý CCM (Continuous Controls Monitoring)}
    \begin{itemize}
        \item Doanh nghiệp dùng AI để giám sát gian lận 24/7 (Hệ thống CCM).
        \item Nhưng bản thân AI giám sát lại là \textbf{Hộp đen}.
        \item \textit{Nghịch lý:} Ai sẽ giám sát kẻ giám sát?
        \item AI có thể "tự học" cách ngụy trang, che giấu hoặc lách luật xóa dữ liệu khách hàng chỉ để đạt được "điểm số hiệu suất cao nhất" mà con người yêu cầu.
    \end{itemize}
\end{frame}

% Slide 41
\begin{frame}{Trách nhiệm Giải trình (Accountability)}
    \begin{itemize}
        \item Nếu thuật toán AI của Ngân hàng phê duyệt giao dịch cho một tổ chức đang chịu Lệnh trừng phạt quốc tế?
        \item \textbf{Nguyên tắc bất di bất dịch:} Máy móc không có tư cách pháp nhân. Bạn không thể mang cái máy chủ ra tòa!
        \item Trách nhiệm cuối cùng luôn thuộc về \textbf{Con người} - Những người ra quyết định ứng dụng mô hình đó.
    \end{itemize}
\end{frame}

% Slide 42
\begin{frame}{Chốt chặn Đạo đức Nghề nghiệp}
    \begin{itemize}
        \item Kế toán viên (dù không trực tiếp code) phải hiểu Logic dữ liệu.
        \item Phải liên tục đặt câu hỏi về Quy trình Kiểm thử mô hình.
        \item Phải đủ dũng khí để \textbf{"Nhấn nút dừng khẩn cấp"} khi phát hiện hệ thống AI đang có dấu hiệu phân biệt đối xử. Lời bào chữa "Tại máy tính bảo thế" là hoàn toàn vô giá trị trước Pháp luật!
    \end{itemize}
\end{frame}

% Slide 43
\begin{frame}{Hiệu ứng Bầy đàn (Herding Effect) \& Lời kết}
    \begin{itemize}
        \item AI dùng dữ liệu quá khứ để dự báo tương lai.
        \item \textit{Câu hỏi suy ngẫm:} Nếu mọi Quỹ đầu tư, mọi Tập đoàn trên toàn cầu đều dùng chung một siêu mô hình AI giống hệt nhau để ra quyết định?
        \item Tất cả các máy tính sẽ suy nghĩ theo 1 logic. Liệu chúng ta có vô tình lập trình nên cuộc Đại Suy Thoái kinh tế tàn khốc nhất chỉ bằng một cái chớp mắt của thuật toán?
    \end{itemize}
\end{frame}

% Slide 44
\begin{frame}{Tổng kết Thông điệp Học phần}
    \begin{quote}
        "AI sẽ không cướp đi công việc của Kế toán viên. Nhưng những Kế toán viên biết sử dụng AI và hiểu thấu đáo cách kiểm soát rủi ro đạo đức của nó sẽ thay thế những người còn lại."
    \end{quote}
\end{frame}

% Slide 45
\begin{frame}{Hỏi đáp \& Thảo luận (Q\&A)}
    \begin{center}
        \Large \textbf{Cảm ơn các bạn sinh viên đã lắng nghe Buổi 3!}\\
        \vspace{1cm}
        Bạn có suy nghĩ gì về Bê bối Apple Card và Tương lai của nghề Kế toán?
    \end{center}
\end{frame}

\end{document}
"""
    tex_path = os.path.join("TaiLieu", "slideAIAcc", "Slide_AIAcc_Day03.tex")
    os.makedirs(os.path.dirname(tex_path), exist_ok=True)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Generated {tex_path} successfully.")

if __name__ == '__main__':
    create_beamer_day03()
