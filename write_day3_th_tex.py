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

\title[Thực hành Buổi 3]{Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.3cm} \Large Thực hành Buổi 3: AI Hỗ trợ Nhập liệu \& Đọc Chứng từ}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

% SLIDE 1
\begin{frame}
    \titlepage
    \begin{center}
        \includegraphics[width=0.5\textwidth,height=2.5cm,keepaspectratio]{images/Day_03_TH/bg_day3_th.png}
    \end{center}
\end{frame}

% SLIDE 2
\begin{frame}{Mục tiêu Buổi Thực hành}
    \begin{enumerate}
        \item Nắm vững kỹ thuật Prompt để giao tiếp với AI xử lý hóa đơn.
        \item Thực hành trích xuất dữ liệu từ Ảnh (Bill) và PDF (Hóa đơn VAT).
        \item Chuyển đổi dữ liệu thô thành định dạng Bảng (Excel/CSV).
        \item Áp dụng tư duy "Vibe Accounting" (Chỉ cần ra lệnh, AI tự làm).
    \end{enumerate}
\end{frame}

% SLIDE 3
\begin{frame}{Tư duy "Vibe Accounting"}
    \begin{itemize}
        \item \textbf{Vibe Coding:} Thuật ngữ IT chỉ việc lập trình viên không cần viết code, chỉ cần mô tả ý tưởng, AI sẽ tự viết code.
        \item \textbf{Vibe Accounting:} Kế toán không cần gõ phím cạch cạch nhập số!
        \item Chỉ cần tải hóa đơn lên và ra lệnh: \textit{"Lọc cho tôi số tiền thuế!"}, AI sẽ trả về kết quả.
    \end{itemize}
\end{frame}

% SLIDE 4
\begin{frame}{Công cụ sử dụng}
    \begin{itemize}
        \item \textbf{Microsoft Copilot:} Tích hợp sẵn trong trình duyệt Edge, miễn phí, xử lý ảnh và PDF rất tốt.
        \item \textbf{ChatGPT (Bản Free/Plus):} Phân tích dữ liệu cực mạnh.
        \item \textbf{Microsoft Excel / Google Sheets:} Để kiểm tra kết quả đầu ra.
    \end{itemize}
    \vspace{0.5cm}
    \begin{center}
        \textbf{Yêu cầu: Sinh viên mở sẵn trình duyệt và đăng nhập ChatGPT/Copilot.}
    \end{center}
\end{frame}

% SLIDE 5
\begin{frame}{Bộ dữ liệu thực hành (Dataset)}
    \begin{itemize}
        \item Lớp trưởng gửi link Google Drive chứa thư mục \textbf{Day3\_ChungTu}.
        \item \textbf{Bao gồm:}
        \begin{itemize}
            \item 2 ảnh chụp bill ăn uống (JPG).
            \item 2 ảnh chụp hóa đơn viết tay (PNG).
            \item 3 file hóa đơn điện tử (PDF).
        \end{itemize}
        \item Sinh viên tải toàn bộ về máy tính để chuẩn bị thực hành.
    \end{itemize}
\end{frame}

\section{1. Xử lý Hóa đơn Bán lẻ (Ảnh chụp)}

% SLIDE 6
\begin{frame}{Bài toán 1 - Thanh toán công tác phí}
    \begin{itemize}
        \item \textbf{Bối cảnh:} Nhân viên kinh doanh đi công tác về, đưa cho bạn một xấp ảnh chụp các bill ăn uống, taxi, tiếp khách.
        \item \textbf{Yêu cầu cũ:} Bạn phải căng mắt ra đọc từng bill, nhập vào Excel để làm Phiếu chi. Rất dễ sai sót và mất thời gian.
        \item \textbf{Mục tiêu:} Dùng AI để làm thay việc này trong 1 phút!
    \end{itemize}
\end{frame}

% SLIDE 7
\begin{frame}{Bước 1 - Tải ảnh lên AI}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Click vào nút đính kèm (Hình chiếc kẹp ghim hoặc dấu +) trên khung chat của ChatGPT/Copilot.
            \item Chọn file \texttt{Bill\_Taxi\_01.jpg}.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_03_TH/chatgpt_upload.png}
    \end{columns}
\end{frame}

% SLIDE 8
\begin{frame}{Bước 2 - Viết Prompt cơ bản}
    \begin{itemize}
        \item \textbf{Prompt 1:} \textit{"Hãy đọc hình ảnh này và cho tôi biết đây là hóa đơn gì, tổng số tiền là bao nhiêu?"}
        \item \textbf{Nhiệm vụ sinh viên:} Gõ prompt và quan sát tốc độ AI đọc ảnh (OCR).
        \item \textbf{Nhận xét:} AI đọc rất nhanh, nhưng dữ liệu trả về chỉ là dạng văn bản (text) thông thường, khó chèn vào Excel.
    \end{itemize}
\end{frame}

% SLIDE 9
\begin{frame}{Bước 3 - Viết Prompt có cấu trúc}
    \begin{itemize}
        \item Kế toán cần dữ liệu có cấu trúc để làm báo cáo.
        \item \textbf{Prompt 2:} \textit{"Bạn là một kế toán viên. Hãy đọc bill này và trích xuất thông tin theo định dạng sau: Tên đơn vị cung cấp | Ngày tháng | Nội dung chi | Số tiền."}
        \item Sinh viên thử lại và so sánh kết quả.
    \end{itemize}
\end{frame}

% SLIDE 10
\begin{frame}{Xử lý nhiều bill cùng lúc (Batch Processing)}
    \begin{itemize}
        \item Tải lên cùng lúc 3 file ảnh \texttt{Bill\_01}, \texttt{Bill\_02}, \texttt{Bill\_03}.
        \item \textbf{Prompt 3:} \textit{"Hãy đọc cả 3 hóa đơn này. Lập cho tôi một bảng tổng hợp gồm các cột: STT, Tên cửa hàng, Ngày, Số tiền. Cuối bảng tính tổng số tiền."}
        \item Đây chính là sức mạnh của AI: Xử lý hàng loạt tài liệu cùng lúc!
    \end{itemize}
\end{frame}

% SLIDE 11
\begin{frame}{Kiểm tra chéo (Human-in-the-loop)}
    \begin{itemize}
        \item \textbf{Nhiệm vụ sinh viên:} Đối chiếu kết quả AI trả về với ảnh gốc.
        \item \textbf{Câu hỏi thảo luận:} AI có đọc nhầm số "0" thành chữ "O", hay số "8" thành số "3" ở bill viết tay không?
        \item \textbf{Bài học cốt lõi:} AI là trợ lý, người chịu trách nhiệm cuối cùng vẫn là Kế toán viên. Luôn phải Review dữ liệu!
    \end{itemize}
\end{frame}

\section{2. Đọc Hóa đơn Điện tử (PDF)}

% SLIDE 12
\begin{frame}{Bài toán 2 - Hóa đơn GTGT (PDF)}
    \begin{itemize}
        \item \textbf{Bối cảnh:} Nhận được file PDF hóa đơn GTGT mua hàng từ nhà cung cấp (có vài chục mặt hàng).
        \item \textbf{Khó khăn:} Không thể copy/paste từng dòng từ PDF vào phần mềm MISA/Excel vì bảng sẽ bị vỡ nát, sai cột.
    \end{itemize}
\end{frame}

% SLIDE 13
\begin{frame}{Xử lý File PDF với AI}
    \begin{itemize}
        \item \textbf{Thao tác:} Upload file \texttt{HoaDon\_MuaHang\_01.pdf} lên ChatGPT.
        \item \textbf{Mẹo:} Nếu dùng bản miễn phí bị giới hạn tính năng upload, sinh viên có thể copy toàn bộ Text trong PDF (Ctrl+A, Ctrl+C) và dán thẳng vào cửa sổ chat.
    \end{itemize}
\end{frame}

% SLIDE 14
\begin{frame}{Prompt trích xuất phần Header (Thông tin chung)}
    \begin{itemize}
        \item Bước đầu tiên là lấy thông tin chung của tờ hóa đơn.
        \item \textbf{Prompt 4:} \textit{"Hãy đọc hóa đơn này và liệt kê cho tôi: Ký hiệu hóa đơn, Số hóa đơn, Ngày lập, Mã số thuế người bán, Tên người bán."}
    \end{itemize}
\end{frame}

% SLIDE 15
\begin{frame}{Prompt trích xuất Chi tiết hàng hóa (Line Items)}
    \begin{itemize}
        \item Đây là phần tốn thời gian nhất của kế toán khi nhập liệu.
        \item \textbf{Prompt 5:} \textit{"Hãy lập một bảng chi tiết các mặt hàng trong hóa đơn này. Cột gồm: STT, Tên Hàng Hóa, ĐVT, Số lượng, Đơn giá, Thành tiền (Chưa VAT). Bỏ qua các dòng trống."}
    \end{itemize}
\end{frame}

% SLIDE 16
\begin{frame}{Ép kiểu dữ liệu (Data Formatting)}
    \begin{itemize}
        \item Kế toán ghét nhất AI trả về số tiền có chữ (Vd: 1.000.000VNĐ) vì không dùng hàm SUM() được.
        \item \textbf{Prompt 6 (Nâng cấp):} \textit{"Làm lại bảng trên. Lưu ý ở cột Số lượng, Đơn giá và Thành tiền, CHỈ in ra con số, KHÔNG chứa chữ 'VNĐ' hay ký hiệu tiền tệ, sử dụng dấu phẩy để phân cách hàng nghìn."}
    \end{itemize}
\end{frame}

% SLIDE 17
\begin{frame}{Kiểm tra tính toán (Math Check)}
    \begin{itemize}
        \item AI là mô hình ngôn ngữ, không phải máy tính bỏ túi. Đôi khi nó làm toán rất dở!
        \item \textbf{Nhiệm vụ sinh viên:} Lấy máy tính hoặc nhẩm lại xem cột (Số lượng $\times$ Đơn giá) có thực sự bằng cột Thành tiền mà AI vừa xuất ra không.
        \item Nếu sai $\rightarrow$ Báo cho AI biết lỗi sai để nó tự sửa.
    \end{itemize}
\end{frame}

\section{3. Chuyển đổi Dữ liệu sang Excel}

% SLIDE 18
\begin{frame}{Từ Chatbot ra Excel}
    \begin{itemize}
        \item Không ai để bảng dữ liệu quý giá nằm mãi trên cửa sổ ChatGPT. Ta phải mang nó về phần mềm kế toán.
        \item \textbf{Cách 1:} Copy \& Paste trực tiếp.
        \item \textbf{Cách 2:} Yêu cầu AI tạo file CSV/Excel để tải về.
    \end{itemize}
\end{frame}

% SLIDE 19
\begin{frame}{Cách 1 - Copy \& Paste chuẩn xác}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Bôi đen bảng trên ChatGPT, Copy (Ctrl+C).
            \item Mở Excel. Dùng tính năng \textbf{Paste Special $\rightarrow$ Text} (để không bị vỡ khung bảng và giữ nguyên định dạng số).
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_03_TH/excel_paste_special.png}
    \end{columns}
\end{frame}

% SLIDE 20
\begin{frame}{Cách 2 - Xuất file CSV (Khuyên dùng)}
    \begin{itemize}
        \item \textbf{Prompt 7:} \textit{"Hãy lưu bảng chi tiết hàng hóa vừa tạo thành một file định dạng .CSV để tôi tải về máy."}
        \item AI sẽ tạo ra một đường link Download. Click vào để tải file về.
    \end{itemize}
\end{frame}

% SLIDE 21
\begin{frame}{Sửa lỗi Font Tiếng Việt (UTF-8) khi mở CSV}
    \begin{itemize}
        \item \textbf{Lỗi phổ biến:} Mở file CSV bằng Excel bị lỗi font chữ Tiếng Việt loằng ngoằng.
        \item \textbf{Cách khắc phục chuẩn:}
        \begin{enumerate}
            \item Mở một file Excel trắng.
            \item Vào tab \textbf{Data} $\rightarrow$ Chọn \textbf{From Text/CSV}.
            \item Trỏ tới file vừa tải về. Ở mục \textit{File Origin}, chọn \textbf{65001: Unicode (UTF-8)}.
            \item Bấm Load để tải dữ liệu hoàn hảo.
        \end{enumerate}
    \end{itemize}
\end{frame}

% SLIDE 22
\begin{frame}{Thực hành độc lập}
    \begin{center}
        \Large \textbf{BÀI TẬP THỰC HÀNH CÁ NHÂN}
    \end{center}
    \vspace{0.3cm}
    \begin{itemize}
        \item Sinh viên tự áp dụng các Prompt từ đầu buổi để xử lý 2 file: \texttt{HoaDon\_MuaHang\_02.pdf} và \texttt{HoaDon\_MuaHang\_03.pdf}.
        \item \textbf{Đích đến:} Tạo ra 1 file Excel duy nhất tổng hợp chi tiết hàng hóa của cả 2 hóa đơn trên, định dạng số chuẩn, không lỗi font.
    \end{itemize}
\end{frame}

\section{4. Đối chiếu \& Tìm kiếm Bất thường}

% SLIDE 23
\begin{frame}{Bài toán 3 - Đối chiếu 3 chiều (3-Way Matching)}
    \begin{itemize}
        \item \textbf{Bối cảnh:} Kế toán cần kiểm tra xem Hóa đơn NCC gửi đến có khớp số lượng và đơn giá với Đơn đặt hàng (PO) mà công ty đã duyệt không.
        \item \textbf{Thực hành:} Tải lên 2 file \texttt{PO\_101.pdf} và \texttt{HoaDon\_101.pdf} cùng lúc.
    \end{itemize}
\end{frame}

% SLIDE 24
\begin{frame}{Kỹ thuật Prompt Đối chiếu}
    \begin{itemize}
        \item \textbf{Prompt 8:} \textit{"Tôi vừa tải lên Đơn đặt hàng và Hóa đơn của cùng 1 giao dịch. Hãy so sánh cột Số lượng và Đơn giá của từng mặt hàng giữa 2 file. Hãy lập bảng chỉ ra các mặt hàng có sự chênh lệch (nếu có)."}
        \item AI sẽ đối chiếu từng dòng và highlight các lỗi sai (ví dụ: Đặt 10 cái, nhưng xuất hóa đơn 12 cái).
    \end{itemize}
\end{frame}

% SLIDE 25
\begin{frame}{Bài toán 4 - Dò tìm rủi ro thuế}
    \begin{itemize}
        \item Tải lên file \texttt{DanhSach\_HoaDon\_Thang5.xlsx} (khoảng 50 dòng).
        \item \textbf{Prompt 9:} \textit{"Hãy đóng vai nhân viên kiểm tra thuế. Kiểm tra bảng kê mua vào này và tìm cho tôi: (1) Các hóa đơn có ngày xuất vào cuối tuần/ngày lễ; (2) Các hóa đơn có giá trị lớn hơn 20 triệu VNĐ nhưng chưa đánh dấu thanh toán chuyển khoản."}
    \end{itemize}
\end{frame}

% SLIDE 26
\begin{frame}{Xử lý dữ liệu bị khuyết thiếu (Missing Data)}
    \begin{itemize}
        \item Có những bill hóa đơn thực tế bị mất góc, rách mờ, hoặc đổ cà phê lên.
        \item \textbf{Prompt 10:} \textit{"Đọc hóa đơn này. Nếu thông tin nào bị mờ không thể đọc chắc chắn, tuyệt đối không tự bịa ra số liệu, hãy điền chữ '[CẦN KIỂM TRA LẠI]' vào ô đó."}
        \item Điều này giúp kế toán dễ dàng dùng chức năng Filter trong Excel để tìm và xử lý thủ công sau.
    \end{itemize}
\end{frame}

\section{5. Bảo mật Dữ liệu Thực tế}

% SLIDE 27
\begin{frame}{Cảnh báo quan trọng khi thực hành}
    \begin{center}
        \Large \textcolor{red}{\textbf{CẢNH BÁO BẢO MẬT}}
    \end{center}
    \vspace{0.3cm}
    \begin{itemize}
        \item Hôm nay chúng ta đang dùng các file chứng từ mẫu (Dummy data).
        \item Khi đi làm thực tế, \textbf{TUYỆT ĐỐI KHÔNG} dùng hóa đơn thật, hợp đồng thật của công ty để up lên ChatGPT bản miễn phí.
        \item Dữ liệu của công ty bạn sẽ bị đưa vào máy chủ để huấn luyện AI công cộng!
    \end{itemize}
\end{frame}

% SLIDE 28
\begin{frame}{Thiết lập Quyền riêng tư trên ChatGPT}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Hướng dẫn tắt tính năng lưu trữ lịch sử để bảo vệ dữ liệu phần nào.
            \item \textbf{Thao tác:} Vào \texttt{Settings} $\rightarrow$ \texttt{Data Controls} $\rightarrow$ Tắt mục \textbf{"Chat history \& training"}.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_03_TH/chatgpt_data_controls.png}
    \end{columns}
\end{frame}

% SLIDE 29
\begin{frame}{Xóa dữ liệu nhạy cảm (Sanitization)}
    \begin{itemize}
        \item Trước khi phải dùng AI (nếu công ty chưa mua bản Enterprise):
        \item Hãy dùng tính năng \textbf{Redact (Bôi đen)} trên PDF để che đi các thông tin nhạy cảm.
        \item \textbf{Ví dụ cần che:} Số tài khoản ngân hàng, Mã số CCCD, Tên cá nhân khách hàng, Mật khẩu.
    \end{itemize}
\end{frame}

\section{6. Tổng kết \& Đánh giá}

% SLIDE 30
\begin{frame}{Báo cáo kết quả thực hành}
    \begin{itemize}
        \item \textbf{Nhiệm vụ 1:} Sinh viên nộp lại file Excel tổng hợp (của phần Bài tập 2) lên hệ thống LMS.
        \item \textbf{Nhiệm vụ 2:} Chụp ảnh màn hình 1 câu Prompt hay nhất mà bạn đã sáng tạo ra để "sửa lưng" AI trong buổi hôm nay.
    \end{itemize}
\end{frame}

% SLIDE 31
\begin{frame}{Ôn tập \& Rút kinh nghiệm}
    \begin{itemize}
        \item \textbf{Ưu điểm:} Nhanh gấp 10 lần gõ tay, xuất bảng Excel đẹp, giảm thiểu OT.
        \item \textbf{Nhược điểm:} Thi thoảng AI bị "ngáo" (Hallucination), tính toán sai cộng trừ nhân chia, từ chối đọc file nếu quá dài.
        \item \textbf{Khẳng định:} Kế toán viên phải luôn giữ vai trò người soát xét (Reviewer). Bạn là người ra quyết định cuối cùng!
    \end{itemize}
\end{frame}

% SLIDE 32
\begin{frame}{Kết thúc}
    \begin{center}
        \Huge \textbf{Q \& A}
    \end{center}
    \vspace{0.5cm}
    \textbf{Dặn dò cho Buổi 4:}
    \begin{itemize}
        \item Chúng ta sẽ chuyển sang dùng AI để phân tích nghiệp vụ kế toán chuyên sâu (Định khoản, Tập hợp chi phí).
        \item Yêu cầu sinh viên về ôn lại kiến thức \textbf{Nguyên lý kế toán} (Nợ / Có).
    \end{itemize}
\end{frame}

\end{document}
"""

with open(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\Slide_AIAcc_v2_Day03_TH.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)
