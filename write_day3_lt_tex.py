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

\title[Buổi 3: Xử lý Chứng từ]{Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.3cm} \Large Buổi 3: AI Hỗ trợ Nhập liệu \& Xử lý Chứng từ}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

% SLIDE 1
\begin{frame}
    \titlepage
    \begin{center}
        \includegraphics[width=0.5\textwidth,height=2.5cm,keepaspectratio]{images/Day_03/bg_day3.png}
    \end{center}
\end{frame}

% SLIDE 2
\begin{frame}{Nội dung Chương trình}
    \tableofcontents
\end{frame}

% SLIDE 3
\begin{frame}{Khởi động (Ice-breaker)}
    \begin{center}
        \Large \textbf{Bạn dành bao nhiêu thời gian để gõ lại số liệu?}
    \end{center}
    \vspace{0.5cm}
    \begin{itemize}
        \item Thực trạng: Hơn 60\% thời gian của sinh viên kế toán mới ra trường là làm công việc "thợ gõ" (Data entry).
        \item Nhìn hóa đơn giấy $\rightarrow$ Gõ vào Excel $\rightarrow$ Gõ vào phần mềm kế toán.
        \item Đây là công việc nhàm chán, dễ sai sót và có nguy cơ bị thay thế cao nhất bởi AI.
    \end{itemize}
\end{frame}

\section{1. Quy trình Chứng từ \& Nỗi đau Nhập liệu}

% SLIDE 4
\begin{frame}{Quy trình Bán hàng \& Thu tiền (Revenue Cycle)}
    \begin{itemize}
        \item Bất kỳ doanh nghiệp nào cũng có chu trình Doanh thu.
        \item Bắt đầu từ khi khách hàng \textbf{Đặt hàng} $\rightarrow$ \textbf{Giao hàng} $\rightarrow$ \textbf{Xuất hóa đơn} $\rightarrow$ \textbf{Thu tiền}.
        \item Mỗi bước đều phát sinh một loại \textbf{Chứng từ (Document)}.
    \end{itemize}
\end{frame}

% SLIDE 5
\begin{frame}{Các loại chứng từ cốt lõi}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Đơn đặt hàng (Purchase Order):} Chốt số lượng, giá cả.
            \item \textbf{Phiếu xuất kho (Packing Slip):} Xác nhận hàng đã rời kho.
            \item \textbf{Hóa đơn giá trị gia tăng (Sales Invoice):} Ghi nhận doanh thu, thuế.
            \item \textbf{Giấy báo có (Remittance Advice):} Xác nhận tiền về tài khoản.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_03/revenue_cycle.png}
    \end{columns}
\end{frame}

% SLIDE 6
\begin{frame}{Luân chuyển chứng từ truyền thống}
    \begin{itemize}
        \item Kế toán viên phải thu thập bản cứng hoặc file PDF qua Zalo/Email.
        \item Mở file PDF/Ảnh ở một màn hình, màn hình kia mở phần mềm MISA/SAP.
        \item Nhìn bằng mắt, gõ lại từng con số: Mã số thuế, Tên công ty, Tiền trước thuế, Tiền thuế VAT...
    \end{itemize}
\end{frame}

% SLIDE 7
\begin{frame}{Rủi ro của phương pháp thủ công}
    \begin{itemize}
        \item \textbf{Sai sót con người (Human Error):} Gõ sai dấu phẩy (1,000,000 thành 100,000). Hậu quả: Báo cáo thuế sai, phạt chậm nộp.
        \item \textbf{Quá tải (Bottleneck):} Hóa đơn thường dồn về cuối tháng khiến kế toán phải OT liên tục.
        \item \textbf{Thất lạc dữ liệu:} Rách giấy, mờ mực, trôi tin nhắn Zalo.
    \end{itemize}
\end{frame}

% SLIDE 8
\begin{frame}{Nhu cầu Tự động hóa}
    \begin{itemize}
        \item Doanh nghiệp KHÔNG trả lương cho kế toán chỉ để "gõ máy".
        \item Kế toán hiện đại được trả lương để \textbf{Phân tích} và \textbf{Kiểm soát rủi ro}.
        \item \textbf{Giải pháp:} Giao việc đọc và nhập liệu chứng từ cho máy móc (AI \& OCR).
    \end{itemize}
\end{frame}

\section{2. Công nghệ Nhận dạng Quang học (OCR)}

% SLIDE 9
\begin{frame}{OCR là gì? (Optical Character Recognition)}
    \begin{itemize}
        \item \textbf{Định nghĩa:} Nhận dạng ký tự quang học.
        \item \textbf{Bản chất:} Chuyển đổi hình ảnh (ảnh chụp, file PDF scan) thành định dạng văn bản mà máy tính có thể hiểu, copy và chỉnh sửa (như Word, Excel).
    \end{itemize}
\end{frame}

% SLIDE 10
\begin{frame}{Cơ chế hoạt động của OCR truyền thống}
    \begin{enumerate}
        \item \textbf{Quét hình ảnh (Image Acquisition):} Đưa hóa đơn vào máy scan.
        \item \textbf{Tiền xử lý (Pre-processing):} Phần mềm tự làm nét chữ, xóa bớt nhiễu nền.
        \item \textbf{Phân tích vùng (Zoning):} Xác định đâu là vùng chứa chữ, đâu là logo.
        \item \textbf{Trích xuất ký tự (Character Extraction):} So khớp từng nét chữ với bảng chữ cái.
    \end{enumerate}
\end{frame}

% SLIDE 11
\begin{frame}{Ứng dụng OCR trong Kế toán}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Chụp ảnh hóa đơn nhà hàng $\rightarrow$ OCR tự động trích xuất Tên nhà hàng, Ngày ăn, Tổng số tiền.
            \item Scan hàng loạt hóa đơn đầu vào $\rightarrow$ Đẩy thẳng dữ liệu vào phần mềm kế toán.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_03/ocr_app.png}
    \end{columns}
\end{frame}

% SLIDE 12
\begin{frame}{Nhược điểm của OCR truyền thống}
    \begin{itemize}
        \item Hoạt động dựa trên \textbf{Luật (Rule-based)} và \textbf{Tọa độ (Template-based)}.
        \item Nếu nhà cung cấp đổi mẫu hóa đơn (Logo dời sang phải, Tên công ty tụt xuống dưới), OCR cũ sẽ đọc sai dòng.
        \item Rất kém trong việc nhận dạng chữ viết tay hoặc hóa đơn bị nhàu nát, chụp mờ.
    \end{itemize}
\end{frame}

% SLIDE 13
\begin{frame}{Sự tiến hóa: OCR kết hợp AI (IDP)}
    \begin{itemize}
        \item \textbf{Intelligent Document Processing (IDP):} Khi AI được tích hợp vào OCR.
        \item Thay vì học thuộc tọa độ vị trí chữ, AI được huấn luyện để "Hiểu" hóa đơn.
        \item AI hiểu ngữ cảnh: \textit{"Con số nằm cạnh chữ VAT 8\% chắc chắn là tiền thuế, dù nó nằm ở bất kỳ góc nào của tờ giấy"}.
    \end{itemize}
\end{frame}

\section{3. Ứng dụng Generative AI Xử lý Chứng từ}

% SLIDE 14
\begin{frame}{Kỷ nguyên của Generative AI (ChatGPT/Copilot)}
    \begin{itemize}
        \item Các mô hình ngôn ngữ lớn (LLMs) như GPT-4 hay Gemini hiện nay đều có khả năng \textbf{Thị giác máy tính (Computer Vision)}.
        \item Chúng không chỉ "đọc" được chữ như OCR, mà còn hiểu sâu sắc về logic của chứng từ kế toán.
    \end{itemize}
\end{frame}

% SLIDE 15
\begin{frame}{Kỹ thuật Prompt để Phân tích Hóa đơn}
    \begin{columns}
        \column{0.5\textwidth}
        Bạn có thể tải thẳng file ảnh/PDF hóa đơn lên ChatGPT.
        \vspace{0.3cm}
        \\ \textbf{Prompt mẫu:} \\ \textit{"Đây là hóa đơn mua hàng. Hãy đọc nó và trích xuất cho tôi: Mã số thuế người bán, Tổng tiền trước thuế, Thuế VAT, Tổng thanh toán."}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_03/chatgpt_invoice.png}
    \end{columns}
\end{frame}

% SLIDE 16
\begin{frame}{Trích xuất ra định dạng Bảng (Table)}
    \begin{itemize}
        \item Để tiện cho việc nhập liệu, ta yêu cầu AI trả về dưới dạng bảng rõ ràng.
        \item \textbf{Prompt:} \textit{"Hãy trình bày kết quả dưới dạng bảng có các cột: STT, Tên Hàng Hóa, Số Lượng, Đơn Giá, Thành Tiền. Bỏ qua các dòng trống không chứa dữ liệu."}
    \end{itemize}
\end{frame}

% SLIDE 17
\begin{frame}{Xuất dữ liệu thẳng ra Excel/CSV}
    \begin{itemize}
        \item Khả năng tuyệt vời của các công cụ GenAI (như Advanced Data Analysis của GPT-4) là \textbf{tạo ra file tải về}.
        \item \textbf{Prompt:} \textit{"Hãy xuất kết quả bảng trên thành một file CSV để tôi có thể tải về và mở bằng Excel."}
        \item Kế toán chỉ cần tải file về và import thẳng vào MISA/SAP!
    \end{itemize}
\end{frame}

% SLIDE 18
\begin{frame}{So sánh đối chiếu chứng từ (3-Way Matching)}
    \begin{itemize}
        \item Kế toán thường phải dò 3 tờ giấy: Đơn đặt hàng (PO) + Phiếu xuất kho + Hóa đơn xem có khớp số lượng và đơn giá không. Rất mất thời gian.
        \item \textbf{Giải pháp AI:} Tải cả 3 file lên ChatGPT cùng lúc.
        \item \textbf{Prompt:} \textit{"Hãy đối chiếu xem số lượng hàng giao thực tế có khớp với số lượng đặt hàng và số lượng xuất hóa đơn không. Chỉ ra các điểm sai lệch."}
    \end{itemize}
\end{frame}

% SLIDE 19
\begin{frame}{Tự động hóa toàn trình (RPA + AI)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{RPA (Robotic Process Automation):} Các con bot tự động mô phỏng thao tác click chuột/gõ phím của con người.
            \item \textbf{Sự kết hợp hoàn hảo:} RPA làm tay chân, AI làm bộ não.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_03/rpa_bot.png}
    \end{columns}
\end{frame}

% SLIDE 20
\begin{frame}{Luồng tự động hóa 100\%}
    \begin{enumerate}
        \item Bot RPA tự động mở Email, tải hóa đơn PDF từ nhà cung cấp về.
        \item Bot đẩy PDF vào hệ thống AI để đọc lấy số liệu.
        \item AI trả về file Excel chuẩn.
        \item Bot RPA tự động mở phần mềm MISA, điền số liệu vào đúng ô và bấm Lưu. Kế toán chỉ việc... uống cà phê và duyệt!
    \end{enumerate}
\end{frame}

% SLIDE 21
\begin{frame}{Xu hướng của các hãng Kiểm toán lớn (Big4)}
    \begin{itemize}
        \item PwC, Deloitte, EY, KPMG đều đã xây dựng các hệ thống AI nội bộ để tự động đọc hàng triệu chứng từ kiểm toán mỗi năm.
        \item Công việc "vọc chứng từ" của thực tập sinh đang giảm dần.
        \item \textbf{Hệ quả:} Sinh viên kế toán cần trang bị tư duy ứng dụng AI để tạo ra giá trị phân tích, thay vì kỹ năng nhập liệu.
    \end{itemize}
\end{frame}

\section{4. Tư duy Phân tích với AI}

% SLIDE 22
\begin{frame}{Case Study: Hóa đơn xăng dầu viết tay}
    \begin{itemize}
        \item \textbf{Tình huống:} Lái xe mang về một xấp 50 hóa đơn bán lẻ xăng dầu, chữ viết tay nguệch ngoạc.
        \item \textbf{Cách cũ:} Kế toán mất 1-2 tiếng căng mắt ra gõ, rất dễ nhìn nhầm số.
        \item \textbf{Cách mới với AI:} Xem Slide tiếp theo!
    \end{itemize}
\end{frame}

% SLIDE 23
\begin{frame}{Giải quyết Case Study bằng ChatGPT}
    \begin{itemize}
        \item \textbf{Bước 1:} Dùng điện thoại chụp lại toàn bộ xấp hóa đơn.
        \item \textbf{Bước 2:} Gửi ảnh vào app ChatGPT (hoặc Copilot).
        \item \textbf{Bước 3:} Dùng Prompt: \textit{"Hãy nhận diện số tiền và ngày tháng trên các hóa đơn viết tay này, lập thành bảng và cộng tổng lại cho tôi."}
        \item Xong trong 30 giây!
    \end{itemize}
\end{frame}

% SLIDE 24
\begin{frame}{Kiểm chứng kết quả (Human-in-the-loop)}
    \begin{itemize}
        \item \textbf{Cảnh báo:} AI không hoàn hảo. Nó có thể bị Hallucination (Ảo giác), đọc nhầm số "8" thành số "3" nếu chữ viết quá mờ hoặc xấu.
        \item \textbf{Nguyên tắc Human-in-the-loop (Con người trong vòng lặp):} AI là người thực thi, Kế toán là người \textbf{Kiểm duyệt (Review)}. Không bao giờ tin tưởng AI mù quáng 100\%.
    \end{itemize}
\end{frame}

% SLIDE 25
\begin{frame}{Nhận diện bất thường (Anomaly Detection)}
    AI không chỉ đọc, mà còn biết cảnh báo rủi ro!
    \begin{itemize}
        \item Cấp dữ liệu 1000 hóa đơn cho AI.
        \item \textbf{Prompt:} \textit{"Hãy tìm cho tôi những hóa đơn có ngày xuất vào Chủ Nhật hoặc ngày nghỉ Lễ, hoặc hóa đơn có số tiền chiết khấu cao bất thường."}
        \item AI sẽ rà quét trong 10 giây và lọc ra các hóa đơn đáng ngờ để kiểm toán viên xem xét.
    \end{itemize}
\end{frame}

\section{5. Bảo mật, Quyền riêng tư \& Kiểm soát}

% SLIDE 26
\begin{frame}{Mặt trái của việc dùng AI xử lý chứng từ}
    \begin{itemize}
        \item \textbf{Câu hỏi lớn:} Khi bạn tải Hóa đơn, Bảng lương, Hợp đồng lên ChatGPT miễn phí, bạn đang đưa dữ liệu đi đâu?
        \item Các mô hình AI công cộng sẽ mặc định dùng dữ liệu bạn tải lên để \textbf{huấn luyện tiếp (Train) mô hình của họ}.
        \item Rủi ro lộ lọt bí mật kinh doanh và thông tin cá nhân là cực kỳ nghiêm trọng.
    \end{itemize}
\end{frame}

% SLIDE 27
\begin{frame}{Confidentiality (Tính Bảo mật)}
    \begin{itemize}
        \item \textbf{Định nghĩa:} Bảo vệ các tài sản trí tuệ và thông tin nhạy cảm của tổ chức.
        \item \textbf{Ví dụ:} Kế hoạch kinh doanh, Báo cáo tài chính nội bộ, Danh sách khách hàng VIP, Bí mật công nghệ.
        \item Nếu lộ ra ngoài, đối thủ cạnh tranh sẽ hưởng lợi, công ty mất lợi thế.
    \end{itemize}
\end{frame}

% SLIDE 28
\begin{frame}{Privacy (Quyền riêng tư)}
    \begin{itemize}
        \item \textbf{Định nghĩa:} Bảo vệ thông tin cá nhân (PII - Personally Identifiable Information) của khách hàng và nhân viên.
        \item \textbf{Ví dụ:} Số thẻ CCCD, Số tài khoản ngân hàng, Lịch sử khám bệnh, Lịch sử mua hàng.
        \item Vi phạm quyền riêng tư có thể dẫn đến việc bị kiện và phạt rất nặng theo các luật định (GDPR Châu Âu, NĐ 13/2023/NĐ-CP của VN).
    \end{itemize}
\end{frame}

% SLIDE 29
\begin{frame}{4 Bước Bảo vệ Dữ liệu (Chuẩn Quốc tế)}
    \begin{enumerate}
        \item \textbf{Identify \& Classify:} Nhận diện và phân loại (Đâu là thông tin mật, đâu là phổ thông).
        \item \textbf{Encryption (Mã hóa):} Chìa khóa công nghệ quan trọng nhất.
        \item \textbf{Access Controls:} Kiểm soát quyền truy cập.
        \item \textbf{Training:} Đào tạo nhận thức cho nhân viên.
    \end{enumerate}
\end{frame}

% SLIDE 30
\begin{frame}{Phân loại dữ liệu trước khi dùng AI}
    \begin{itemize}
        \item \textbf{Public (Công khai):} Thông tư, nghị định, chuẩn mực kế toán $\rightarrow$ Được phép dùng ChatGPT công cộng để tóm tắt vô tư.
        \item \textbf{Internal (Nội bộ):} Mẫu biểu không chứa số liệu cụ thể $\rightarrow$ Cẩn trọng.
        \item \textbf{Confidential/Restricted (Mật):} Hợp đồng M\&A, Bảng lương, Báo cáo doanh thu $\rightarrow$ \textbf{TUYỆT ĐỐI KHÔNG} tải lên các bản AI miễn phí/công cộng.
    \end{itemize}
\end{frame}

% SLIDE 31
\begin{frame}{Mã hóa dữ liệu (Encryption)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Là phương pháp biến dữ liệu rõ (Plaintext) thành một chuỗi ký tự vô nghĩa (Ciphertext).
            \item Chỉ có người sở hữu "Chìa khóa" (Decryption Key) mới đọc được.
            \item Phải mã hóa dữ liệu cả trên đường truyền (In transit) và dữ liệu lưu trữ trong máy (At rest).
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_03/encryption.png}
    \end{columns}
\end{frame}

% SLIDE 32
\begin{frame}{Giấu thông tin (Data Masking / Tokenization)}
    \begin{itemize}
        \item Khi cần test hệ thống AI hoặc thuê lập trình viên bên ngoài.
        \item Dùng kỹ thuật Data Masking để ẩn đi/thay thế các dữ liệu nhạy cảm bằng chuỗi ký tự giả (Token) nhưng vẫn giữ nguyên định dạng.
        \item \textbf{Ví dụ:} Mã số thẻ tín dụng \texttt{1234-5678-9012-3456} sẽ được tự động đổi thành \texttt{XXXX-XXXX-XXXX-3456}.
    \end{itemize}
\end{frame}

% SLIDE 33
\begin{frame}{Giải pháp cho Doanh nghiệp: Enterprise AI}
    \begin{itemize}
        \item Để xử lý chứng từ mật, doanh nghiệp phải mua bản quyền \textbf{Enterprise AI} (Ví dụ: Microsoft Copilot for Microsoft 365, ChatGPT Enterprise).
        \item \textbf{Cam kết bảo mật:} "Chúng tôi KHÔNG sử dụng dữ liệu của bạn để huấn luyện mô hình. Dữ liệu của bạn được mã hóa và cách ly hoàn toàn."
    \end{itemize}
\end{frame}

% SLIDE 34
\begin{frame}{Information Rights Management (IRM)}
    \begin{itemize}
        \item Hệ thống kiểm soát quyền thông tin. Dù file hóa đơn/báo cáo đã được gửi cho đối tác, công ty vẫn giữ quyền kiểm soát:
        \item Cấm in ấn (Print), Cấm Copy/Paste văn bản.
        \item Hẹn giờ tự động hủy file (Revoke access) sau 7 ngày.
    \end{itemize}
\end{frame}

% SLIDE 35
\begin{frame}{Data Loss Prevention (DLP)}
    \begin{itemize}
        \item Hệ thống phòng chống thất thoát dữ liệu.
        \item Hoạt động như một màng lọc quét mọi email gửi ra ngoài:
        \item Nếu một nhân viên thử gửi email đính kèm file có chứa từ khóa nhạy cảm (như "Bảng lương", "Danh sách khách hàng"), hệ thống DLP sẽ lập tức chặn email lại và báo cho quản lý.
    \end{itemize}
\end{frame}

% SLIDE 36
\begin{frame}{Chữ ký số (Digital Signatures)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Kế toán hiện đại không thể sống thiếu Chữ ký số.
            \item Chữ ký số \textbf{KHÔNG PHẢI} là ảnh chụp chữ ký tay rồi dán vào PDF!
            \item Nó là một thuật toán toán học đảm bảo tính \textbf{Toàn vẹn (Integrity)} và \textbf{Chống chối bỏ (Non-repudiation)}.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_03/digital_signature.png}
    \end{columns}
\end{frame}

% SLIDE 37
\begin{frame}{Cơ chế của Chữ ký số (Hashing)}
    \begin{itemize}
        \item \textbf{Hàm băm (Hash):} Biến một tờ hóa đơn PDF thành một đoạn code ngắn duy nhất (Ví dụ độ dài 256 ký tự). 
        \item Nếu ai đó sửa dù chỉ 1 dấu chấm (hoặc sửa số tiền từ 1 triệu thành 9 triệu) trong file PDF đó, đoạn code Hash sẽ thay đổi hoàn toàn $\rightarrow$ Chữ ký số báo vô hiệu!
        \item \textbf{Ký số = } Mã hóa đoạn Hash đó bằng Khóa Bí Mật (Private Key) của Giám đốc.
    \end{itemize}
\end{frame}

% SLIDE 38
\begin{frame}{Blockchain trong Kế toán (Khái niệm sơ lược)}
    \begin{itemize}
        \item Blockchain có thể hiểu đơn giản là một cuốn sổ cái (Ledger) được nhân bản ra hàng ngàn máy tính.
        \item Khi một chứng từ hóa đơn được ký số và đưa lên Blockchain, nó không thể bị xóa bỏ, không thể bị sửa chữa (Immutability).
        \item \textbf{Tương lai:} Mọi giao dịch kế toán sẽ minh bạch và không thể gian lận.
    \end{itemize}
\end{frame}

% SLIDE 39
\begin{frame}{Quy trình chuẩn khi áp dụng AI vào Kế toán}
    \begin{enumerate}
        \item Nhận chứng từ gốc.
        \item Xóa/Ẩn thông tin định danh nhạy cảm cá nhân (Data Masking).
        \item Cấp cho Enterprise AI để đọc và trích xuất dữ liệu.
        \item Con người (Kế toán viên) kiểm tra chéo (Review) lại kết quả của AI.
        \item Ký số, duyệt và lưu vào Cơ sở dữ liệu nội bộ (có phân quyền Access Control).
    \end{enumerate}
\end{frame}

% SLIDE 40
\begin{frame}{Trách nhiệm nghề nghiệp của Kế toán viên}
    \begin{center}
        \Large \textbf{AI là trợ thủ, không phải người chịu trách nhiệm trước pháp luật.}
    \end{center}
    \vspace{0.5cm}
    \begin{itemize}
        \item Nếu AI đọc sai số tiền thuế và bạn nhắm mắt duyệt bấm nộp...
        \item Cơ quan thuế sẽ phạt Doanh nghiệp (và sếp sẽ truy trách nhiệm bạn), chứ pháp luật không phạt OpenAI hay Microsoft!
    \end{itemize}
\end{frame}

% SLIDE 41
\begin{frame}{Tóm tắt Buổi 3}
    \begin{itemize}
        \item \textbf{Giá trị:} Công nghệ OCR và GenAI giải phóng kế toán khỏi công việc nhập liệu nhàm chán (Data Entry).
        \item \textbf{Kỹ năng mới:} Biết dùng Prompt để yêu cầu AI đọc, trích xuất (thành bảng/CSV) và đối chiếu chứng từ.
        \item \textbf{Tuân thủ:} Luôn cảnh giác với bảo mật, không up dữ liệu mật lên AI công cộng, hiểu rõ vai trò của Mã hóa và Chữ ký số.
    \end{itemize}
\end{frame}

% SLIDE 42
\begin{frame}{Kết thúc \& Chuẩn bị cho Buổi Thực hành}
    \begin{center}
        \Huge \textbf{Q \& A}
    \end{center}
    \vspace{0.5cm}
    \textbf{Yêu cầu buổi sau:}
    \begin{itemize}
        \item Các bạn chuẩn bị sẵn các file ảnh chụp hóa đơn (đi ăn uống, mua sắm) để mang vào thực hành dùng AI tự động đọc và xuất ra Excel nhé!
    \end{itemize}
\end{frame}

\end{document}
"""

with open(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\Slide_AIAcc_v2_Day03_LT.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)
