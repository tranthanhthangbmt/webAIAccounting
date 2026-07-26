import os

def create_beamer_day11():
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
\title[AI trong Kế toán - Buổi 11]{Kỹ năng Phân tích Dữ liệu Nền tảng\\(Foundational Data Analysis)}
\subtitle{Từ Cơ sở Dữ liệu đến Trực quan hóa}
\author[Giảng viên]{Trí tuệ Nhân tạo cho Kế toán (AI in Accounting)}
\institute[Đại học]{Khoa Kế toán - Kiểm toán}
\date{Buổi học 11}

\begin{document}

% Slide 1: Title
\begin{frame}
    \titlepage
\end{frame}

% Slide 2: Mục tiêu
\begin{frame}{Mục tiêu Bài học (Learning Objectives)}
    \begin{itemize}
        \item \textbf{Khái niệm cốt lõi:} Nắm vững cấu trúc Cơ sở Dữ liệu Quan hệ (Bảng, Khóa chính, Khóa ngoại).
        \item \textbf{SQL JOIN:} Hiểu cơ chế hoạt động của các lệnh kết nối bảng (Inner, Left, Right, Full Join).
        \item \textbf{Excel nâng cao:} Sử dụng các hàm có điều kiện (SUMIFS, COUNTIFS) và PivotTable.
        \item \textbf{Thống kê mô tả:} Phát hiện những bất thường ẩn sau giá trị trung bình (Mean).
        \item \textbf{Trực quan hóa:} Áp dụng đồ thị hiệu quả giữa hai giai đoạn: Khám phá và Giải thích.
    \end{itemize}
\end{frame}

% Slide 3: Agenda
\begin{frame}{Nội dung Chính (Agenda)}
    \tableofcontents
\end{frame}

% ==========================================
\section{Khởi động \& Ảo ảnh của Số Trung Bình}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 5
\begin{frame}{Tình huống Kiểm toán Thực tế}
    \textbf{Case Study: Super Scooters}
    \begin{itemize}
        \item Công ty sản xuất và cho thuê xe điện scooter.
        \item Trong báo cáo tài chính hàng tháng, chi phí bảo hành trung bình cho mỗi chiếc xe là \textbf{\$600}.
        \item Ngân sách dự kiến cho mỗi xe là \$650.
        \item \textbf{Câu hỏi:} Nhìn vào con số \$600, bạn thấy hệ thống hoạt động ổn định không? Có nên đóng hồ sơ kiểm toán?
    \end{itemize}
\end{frame}

% Slide 6
\begin{frame}{Ảo ảnh 600 USD: Con số "Hoàn hảo"}
    \begin{itemize}
        \item \textbf{Cái bẫy của con số trung bình:} Nó thường che giấu sự thật gai góc bên trong.
        \item Nếu chỉ nhìn vào báo cáo tổng hợp, mức \$600 rất an toàn.
        \item Nhưng trong ngành kiểm toán, chữ "Trung bình" (Mean) luôn tiềm ẩn rủi ro lớn.
        \item Nó có xu hướng "san bằng" mọi bất thường.
    \end{itemize}
\end{frame}

% Slide 7
\begin{frame}{Cú sốc đằng sau con số \$600}
    \textbf{Sự thật bị che giấu:}
    \begin{itemize}
        \item Khi đào sâu vào dữ liệu thô, chi phí thực tế không hề tụ lại quanh mức \$600.
        \item Nó trải rộng và tập trung ở hai mức:
        \begin{enumerate}
            \item Những lỗi nhỏ: Tốn khoảng \textbf{\$200}
            \item Những lỗi hệ thống nghiêm trọng: Tốn đúng \textbf{\$1.200}
        \end{enumerate}
        \item Có một dòng xe cụ thể đang liên tục ngốn \$1.200 chi phí sửa chữa!
        \item \textbf{Kết luận:} Con số \$600 chỉ là ảo ảnh toán học, không phản ánh một giao dịch thực tế nào.
    \end{itemize}
\end{frame}

% Slide 8
\begin{frame}{Hành trình Khám phá Dữ liệu}
    \begin{itemize}
        \item Làm thế nào để tóm gọn những "kẻ cắp tàng hình" đang bào mòn lợi nhuận?
        \item \textbf{Bước 1:} Trích xuất từ gốc rễ - Cơ sở dữ liệu quan hệ (Relational Database).
        \item \textbf{Bước 2:} Chế ngự dữ liệu khổng lồ bằng các hàm tính toán (Excel Functions).
        \item \textbf{Bước 3:} Phân tích đa chiều với PivotTable.
        \item \textbf{Bước 4:} Lật tẩy ảo ảnh bằng Thống kê mô tả (Descriptive Statistics) \& Trực quan hóa (Visualization).
    \end{itemize}
\end{frame}

% ==========================================
\section{Cơ sở Dữ liệu Quan hệ \& Nghệ thuật Kết nối}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 10
\begin{frame}{Cơ sở dữ liệu quan hệ (Relational Database) là gì?}
    \begin{itemize}
        \item Là tập hợp các dữ liệu có liên quan về mặt logic.
        \item \textbf{Mục đích:} Lưu trữ, truy xuất và thao tác dữ liệu dễ dàng.
        \item Dữ liệu được lưu trữ trong các \textbf{bảng riêng lẻ (Tables)} thay vì một trang tính Excel khổng lồ duy nhất.
        \item Sức mạnh của chữ "Quan hệ" nằm ở cơ chế các bảng "nói chuyện" với nhau thông qua hệ thống \textbf{khóa (Keys)}.
    \end{itemize}
\end{frame}

% Slide 11
\begin{frame}{Thành phần cơ bản: Bảng, Hàng, Cột}
    \begin{itemize}
        \item \textbf{Hàng (Rows):} Đại diện cho một bản ghi (ví dụ: 1 giao dịch bán hàng).
        \item \textbf{Cột (Columns):} Phản ánh các thuộc tính của giao dịch đó (ví dụ: ngày tháng, số tiền).
    \end{itemize}
    \vspace{0.3cm}
    \begin{center}
        \includegraphics[height=4cm,keepaspectratio]{../../Figures/Buoi_11/ILLUSTRATION 2.1 Database Elements and Examples of Tables and Attributes.PNG}
    \end{center}
\end{frame}

% Slide 12
\begin{frame}{Khóa chính (Primary Key)}
    \begin{itemize}
        \item \textbf{Khái niệm:} Cột có giá trị \textbf{độc nhất} cho mỗi hàng trong bảng.
        \item \textbf{Vai trò:} Định danh cho bản ghi, không bao giờ có 2 hàng trùng khóa chính.
        \item \textbf{Ẩn dụ:} Nó giống như \textbf{Số Căn cước công dân} của mỗi người, độc nhất vô nhị.
    \end{itemize}
    \vspace{0.3cm}
    \begin{center}
        \includegraphics[height=4cm,keepaspectratio]{../../Figures/Buoi_11/Illustration 2.2 is the database view of a university’s asset data table that contains data for the inventory of its assets..PNG}
    \end{center}
\end{frame}

% Slide 13
\begin{frame}{Khóa ngoại (Foreign Key)}
    \begin{itemize}
        \item \textbf{Khái niệm:} Một cột trong bảng này chứa dữ liệu giống hệt khóa chính của bảng khác.
        \item \textbf{Vai trò:} Đóng vai trò như một \textbf{chiếc mỏ neo}, tạo đường dẫn liên kết giữa hai bảng.
        \item \textbf{Ẩn dụ:} Khi bạn điền số Căn cước vào tờ khai ngân hàng. Ngân hàng dùng số đó (khóa ngoại) truy xuất về dữ liệu dân cư để lấy họ tên, ngày sinh.
    \end{itemize}
\end{frame}

% Slide 14
\begin{frame}{Bài toán Dư thừa Thông tin}
    \begin{itemize}
        \item \textbf{Tại sao phải chia thành nhiều bảng?}
        \item \textbf{Ví dụ tính khấu hao:} Nếu ghi tỷ lệ khấu hao vào bảng Tài sản, mỗi khi nhập 1 máy tính mới, ta lại phải lặp lại thông tin đó hàng ngàn lần.
        \item \textbf{Giải pháp:} Lưu tuổi thọ \& tỷ lệ khấu hao ở \textbf{Bảng Danh mục Tài sản}. Lưu mã máy tính, ngày mua ở \textbf{Bảng Tài sản}.
        \item Dùng Khóa ngoại (CategoryID) để nối (Join) hai bảng lại.
    \end{itemize}
    \vspace{-0.2cm}
    \begin{center}
        \includegraphics[height=3cm,keepaspectratio]{../../Figures/Buoi_11/ILLUSTRATION 2.3 Creating a Relationship Between Tables.PNG}
    \end{center}
\end{frame}

% Slide 15
\begin{frame}{Truy xuất Dữ liệu: Ngôn ngữ SQL}
    \begin{itemize}
        \item \textbf{SQL (Structured Query Language):} Ngôn ngữ tiêu chuẩn để quản lý cơ sở dữ liệu.
        \item \textbf{Query (Truy vấn):} Yêu cầu hành động đối với cơ sở dữ liệu (Nối, Thêm, Cập nhật, Xóa).
        \item Khi dữ liệu nằm rải rác, SQL đóng vai trò thiết lập các lệnh \textbf{JOIN (Kết nối)} để lấy bức tranh toàn cảnh.
    \end{itemize}
\end{frame}

% Slide 16
\begin{frame}{Bốn Phương pháp Kết nối (JOIN)}
    \begin{center}
        \includegraphics[height=5cm,keepaspectratio]{../../Figures/Buoi_11/ILLUSTRATION 2.4 Types of Joins.PNG}
    \end{center}
    \begin{itemize}
        \item Inner Join, Left Join, Right Join, Full Join.
    \end{itemize}
\end{frame}

% Slide 17
\begin{frame}{Inner Join: Bức tranh "Sạch sẽ" nhưng Lừa dối}
    \begin{itemize}
        \item \textbf{Inner Join:} Chỉ trả về những hàng khớp nhau ở cả hai bảng.
        \item Ví dụ: Bảng A (Hóa đơn), Bảng B (Nhà cung cấp được duyệt).
        \item Kết quả: Trả về danh sách thanh toán cho nhà cung cấp hợp lệ. Trông rất sạch sẽ, hoàn hảo.
        \item \textbf{Nhược điểm:} Bỏ qua các hóa đơn thanh toán cho nhà cung cấp không có trong danh sách! Không phù hợp cho kiểm toán.
    \end{itemize}
    \vspace{-0.3cm}
    \begin{center}
        \includegraphics[height=3cm,keepaspectratio]{../../Figures/Buoi_11/ILLUSTRATION 2.6 Results from an Inner Join for Bikes R Us.PNG}
    \end{center}
\end{frame}

% Slide 18
\begin{frame}{Left Join trong Kiểm toán: Truy tìm "Kẻ cắp tàng hình"}
    \begin{itemize}
        \item \textbf{Left Join:} Giữ lại toàn bộ Bảng A (bên trái) và tìm dữ liệu tương ứng ở Bảng B (bên phải).
        \item Trong kiểm toán: Giữ lại toàn bộ \textbf{Hóa đơn chi tiền (A)}. Cố đắp thông tin \textbf{Nhà cung cấp (B)} vào.
        \item Điều gì xảy ra nếu Hóa đơn chi cho một "nhà cung cấp ma" không tồn tại ở Bảng B?
    \end{itemize}
\end{frame}

% Slide 19
\begin{frame}{Sự thật về giá trị NULL}
    \begin{itemize}
        \item Khi thông tin không khớp (Nhà cung cấp ma), hệ thống sẽ sinh ra giá trị \textbf{NULL} (rỗng).
        \item \textbf{Lưu ý:} NULL \textbf{không phải} là số Không (0).
        \item Số 0 là giá trị định lượng. NULL là khoảng trống không xác định.
        \item Nhìn thấy một loạt NULL ở cột nhà cung cấp? Báo động đỏ: Tiền đang bị tuồn ra ngoài hệ thống!
    \end{itemize}
    \vspace{-0.2cm}
    \begin{center}
        \includegraphics[height=2.5cm,keepaspectratio]{../../Figures/Buoi_11/ILLUSTRATION 2.7 Results from a Left Join for Bikes R Us.PNG}
    \end{center}
\end{frame}

% ==========================================
\section{Chế ngự Dữ liệu Khổng lồ với Các Hàm Tính toán}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 21
\begin{frame}{Từ SQL sang Excel: Bức tranh hàng trăm ngàn dòng}
    \begin{itemize}
        \item Sau khi trích xuất (Join) thành công, kết quả thường là một file Excel (hoặc CSV) khổng lồ chứa hàng trăm ngàn dòng.
        \item Lúc này, logic của cơ sở dữ liệu quan hệ hết tác dụng.
        \item Đây là lúc chúng ta phải "nhào nặn" dữ liệu bằng các công cụ tính toán và hàm (Functions).
    \end{itemize}
\end{frame}

% Slide 22
\begin{frame}{Hạn chế của Hàm Cơ bản}
    \begin{center}
        \includegraphics[height=3.5cm,keepaspectratio]{../../Figures/Buoi_11/ILLUSTRATION 2.11 Basic Microsoft Excel Functions.PNG}
    \end{center}
    \begin{itemize}
        \item Hàm \texttt{SUM} hay \texttt{COUNT} rất nhanh.
        \item Nhưng ban lãnh đạo hiếm khi hỏi những câu đơn giản như "Tổng tài sản là bao nhiêu?".
    \end{itemize}
\end{frame}

% Slide 23
\begin{frame}{Nhu cầu Phân tích Đa chiều (Multi-dimensional)}
    \begin{itemize}
        \item Sếp thường hỏi: "Tổng giá trị tài sản, \textbf{nhưng} chỉ tính danh mục thiết bị y tế, mua sau năm 2022, tại chi nhánh phía Nam."
        \item Một hàm SUM thông thường sẽ "bó tay".
        \item Nếu lọc thủ công rồi copy ra chỗ khác cộng lại: Mất thời gian, rủi ro sai sót (Human Error) cực lớn.
    \end{itemize}
\end{frame}

% Slide 24
\begin{frame}{Giải pháp: Các Hàm Có Điều Kiện}
    \begin{itemize}
        \item \textbf{SUMIF / COUNTIF:} Tính tổng / Đếm với 1 điều kiện.
        \item \textbf{SUMIFS / COUNTIFS:} Tính tổng / Đếm với nhiều điều kiện kết hợp.
        \item \textbf{Cơ chế hoạt động:} Cho phép xử lý ngay lập tức các truy vấn chứa nhiều điều kiện ràng buộc.
    \end{itemize}
\end{frame}

% Slide 25
\begin{frame}{Cơ chế của SUMIFS: "Người bảo vệ khắt khe"}
    \begin{itemize}
        \item \textbf{Ẩn dụ:} Hàm SUMIFS giống như một người bảo vệ kho dữ liệu, tay cầm danh sách tiêu chí khắt khe.
        \item \textbf{Cách duyệt:} Người bảo vệ đi dọc qua hàng trăm ngàn dòng, soi từng giao dịch.
        \item \textbf{Quyết định:} Chỉ những giao dịch thỏa mãn \textbf{đồng thời tất cả} điều kiện mới được phép qua cửa để cộng gộp vào tổng.
    \end{itemize}
    \begin{center}
        \includegraphics[height=2.5cm,keepaspectratio]{../../Figures/Buoi_11/ILLUSTRATION 2.12 University Asset Data COUNTIF Function Arguments Box.PNG}
    \end{center}
\end{frame}

% Slide 26
\begin{frame}{Sức mạnh \& Hạn chế của Các hàm Excel}
    \begin{itemize}
        \item \textbf{Sức mạnh:} Nhanh chóng, tự động hóa, độ chính xác cao. Trả lời ngay được các câu hỏi chi tiết.
        \item \textbf{Hạn chế:} Cơ chế đó chỉ hiệu quả khi chúng ta \textbf{biết chính xác câu hỏi mình muốn đặt ra}.
        \item Nếu sếp bảo: "Hãy cho tôi xem bức tranh tổng quan, tự tìm ra xu hướng xem!" - Không có điều kiện cụ thể để đưa vào hàm.
    \end{itemize}
\end{frame}


% ==========================================
\section{Pivot Table \& Tư duy Phân tích Khám phá}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 28
\begin{frame}{Vũ khí Tối thượng: PivotTable}
    \begin{itemize}
        \item Khi không có câu hỏi chi tiết, PivotTable là công cụ hoàn hảo.
        \item Không cần viết một dòng công thức nào cả.
        \item Khả năng thay đổi hình dạng dữ liệu nhanh chóng thông qua giao diện \textbf{Kéo - Thả (Drag \& Drop)}.
    \end{itemize}
\end{frame}

% Slide 29
\begin{frame}{Năm Vùng Cốt Lõi của PivotTable}
    \begin{itemize}
        \item \textbf{Filters:} Bộ lọc toàn cục cho bảng.
        \item \textbf{Columns:} Phân chia dữ liệu theo chiều ngang.
        \item \textbf{Rows:} Gom nhóm dữ liệu theo chiều dọc.
        \item \textbf{Values:} Thực hiện phép tính (Sum, Average, Count...).
    \end{itemize}
\end{frame}

% Slide 30
\begin{frame}{Phép màu Kéo \& Thả: 10 Giây cho 450.000 dòng}
    \begin{itemize}
        \item Kéo trường \textit{Danh mục Tài sản} thả vào vùng \textbf{Rows}.
        \item Hệ thống quét 450.000 dòng, lập tức gom nhóm và hiển thị 5-10 dòng đại diện.
        \item Kéo tiếp trường \textit{Chi phí} vào vùng \textbf{Values}, nó tự động tính tổng theo từng danh mục.
        \item \textbf{Kết quả:} Từ đống hỗn độn thành báo cáo gọn gàng trong nháy mắt.
    \end{itemize}
\end{frame}

% Slide 31
\begin{frame}{Bảng điều khiển Tương tác (Interactive Dashboard)}
    \begin{itemize}
        \item PivotTable không chỉ tóm tắt mà còn cho phép \textbf{Drill-down} (phân tích sâu).
        \item Sử dụng \textbf{Slicers} (Bộ lọc trực quan).
        \item Khi click vào một năm cụ thể trên Slicer, toàn bộ bảng tóm tắt tự thay đổi số liệu theo thời gian thực.
        \item Báo cáo tĩnh trở thành một cỗ máy tương tác.
    \end{itemize}
\end{frame}

% Slide 32
\begin{frame}{Cạm bẫy của sự gọn gàng}
    \begin{itemize}
        \item Báo cáo PivotTable thường đưa ra các con số tổng hoặc trung bình rất "đẹp và sạch sẽ".
        \item \textbf{Vấn đề:} Sự sạch sẽ đó có thể là một cái bẫy.
        \item Con số tóm tắt có xu hướng san bằng mọi thứ, che giấu sự thật gai góc (như ví dụ \$600 bảo hành xe).
        \item Chúng ta cần bước tiếp theo: \textbf{Thống kê mô tả}.
    \end{itemize}
\end{frame}


% ==========================================
\section{Thống kê Mô tả \& Vạch trần Sự thật}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 34
\begin{frame}{Thống kê Mô tả (Descriptive Statistics)}
    \begin{itemize}
        \item Đưa dữ liệu lên "bàn mổ" để soi rọi bản chất.
        \item Đừng chỉ nhìn vào \textbf{Mean (Số trung bình)}. Số trung bình rất dễ bị bóp méo bởi dữ liệu ngoại lệ.
        \item Phải bổ sung các thước đo phân tán:
        \begin{itemize}
            \item \textbf{Phương sai (Variance)}
            \item \textbf{Độ lệch chuẩn (Standard Deviation)}
        \end{itemize}
    \end{itemize}
\end{frame}

% Slide 35
\begin{frame}{Hình dáng Phân bổ: Độ lệch \& Độ nhọn}
    \begin{itemize}
        \item \textbf{Độ lệch (Skewness):} Dữ liệu có xu hướng nghiêng về một phía (âm hoặc dương) hay đối xứng?
        \item \textbf{Độ nhọn (Kurtosis):} "Ngọn núi" dữ liệu nhọn hoắt (tập trung) hay thấp tè (trải dài)?
        \item Nếu chi phí bảo hành phần lớn là \$600, ngọn núi sẽ rất cao và nhọn ở giữa (Kurtosis cao), thể hiện sự ổn định.
    \end{itemize}
\end{frame}

% Slide 36
\begin{frame}{Lật tẩy Ảo ảnh 600 USD: Lưng Lạc đà (Bimodal)}
    \begin{itemize}
        \item Dữ liệu của Super Scooters không phải là một ngọn núi.
        \item Nó phân tán ra hai phía (\$200 và \$1.200) tạo thành đồ thị có 2 đỉnh (Bimodal Distribution).
        \item Giống như \textbf{lưng một con lạc đà có hai bướu}.
        \item Cái bướu thứ 2 ở mức \$1.200 là manh mối chỉ ra một linh kiện lỗi hệ thống.
        \item Số trung bình \$600 rơi vào khoảng không vô nghĩa giữa 2 bướu lạc đà!
    \end{itemize}
\end{frame}

% Slide 37
\begin{frame}{Độ Lệch Chuẩn: Hệ thống "Radar An ninh"}
    \begin{itemize}
        \item \textbf{Độ lệch chuẩn} đóng vai trò xác định ranh giới của sự bình thường.
        \item \textbf{Ẩn dụ Radar:} 99\% giao dịch nằm trong không phận an toàn sẽ bị radar bỏ qua.
        \item Ngay khi có một giao dịch vượt ranh giới độ lệch chuẩn, nó trở thành \textbf{Ngoại lệ (Outlier)}.
        \item Radar ngay lập tức nhấp nháy đỏ báo động cho kiểm toán viên.
    \end{itemize}
\end{frame}


% ==========================================
\section{Trực quan hóa Dữ liệu - Đôi mắt của AI}
% ==========================================
\begin{frame}
    \tableofcontents[currentsection]
\end{frame}

% Slide 39
\begin{frame}{Giới hạn của Não bộ}
    \begin{itemize}
        \item Não người không được thiết kế để đọc nửa triệu dòng văn bản.
        \item Cố tìm ra gian lận bằng cách cuộn Excel sẽ dẫn đến "mù lòa nhận thức".
        \item Trực quan hóa dữ liệu (Visualization) chuyển gánh nặng xử lý sang \textbf{vỏ não thị giác} - nơi chúng ta xử lý hình ảnh nhanh gấp vạn lần.
    \end{itemize}
\end{frame}

% Slide 40
\begin{frame}{Biểu đồ phân tán (Scatter Plot)}
    \begin{itemize}
        \item Mỗi giao dịch là một dấu chấm trên đồ thị.
        \item Mắt người ngay lập tức phát hiện ra một dấu chấm đơn độc, tách biệt so với đám đông (Outlier) chỉ trong \textit{tích tắc}.
        \item Đó là sức mạnh của trực quan hóa trong kiểm toán.
    \end{itemize}
\end{frame}

% Slide 41
\begin{frame}{Hai Giai đoạn: Khám phá \& Giải thích}
    \begin{itemize}
        \item \textbf{Khám phá (Exploratory):} Giống như \textit{bảng điều tra của thám tử}. Lộn xộn, thử nghiệm liên tục nhiều loại đồ thị để tự mình tìm ra xu hướng.
        \item \textbf{Giải thích (Explanatory):} Giống như \textit{bản trình chiếu trước Ban Giám đốc}. Gọn gàng, sắc nét, có mục tiêu rõ ràng để kể lại câu chuyện.
    \end{itemize}
\end{frame}

% Slide 42
\begin{frame}{Chọn đúng Biểu đồ (Choose the Right Chart)}
    \begin{itemize}
        \item \textbf{Bar Chart (Biểu đồ cột):} Xuất sắc để so sánh độ lớn (VD: doanh thu giữa các vùng).
        \item \textbf{Histogram (Biểu đồ tần suất):} Hoàn hảo để hiển thị \textit{hình dáng phân bổ} (để thấy được cái "lưng lạc đà").
        \item Chọn sai biểu đồ là bóp méo thông điệp dữ liệu!
    \end{itemize}
\end{frame}

% ==========================================
\section{Tổng kết \& Q\&A}
% ==========================================

% Slide 44
\begin{frame}{Tổng kết Buổi học}
    \begin{itemize}
        \item \textbf{Tư duy Kiến trúc sư:} Nắm bắt cơ chế khóa (Primary/Foreign Key) và lệnh SQL JOIN.
        \item \textbf{Người điều phối dữ liệu:} Sử dụng SUMIFS và PivotTable để nhào nặn thông tin, tạo dashboard đa chiều.
        \item \textbf{Thám tử kiểm toán:} Dùng thống kê mô tả (Kurtosis, Variance) để vượt qua ảo ảnh số trung bình.
        \item \textbf{Nhà kể chuyện:} Trực quan hóa dữ liệu để phát hiện ngoại lệ và thuyết phục ban giám đốc.
    \end{itemize}
\end{frame}

% Slide 45
\begin{frame}{Hỏi đáp (Q\&A)}
    \begin{center}
        \Large \textbf{Cảm ơn các bạn đã lắng nghe!}\\
        \vspace{1cm}
        Bạn có câu hỏi nào về Cơ sở dữ liệu, Excel Functions, PivotTable hay Thống kê mô tả không?
    \end{center}
\end{frame}

\end{document}
"""
    # Write tex file directly to correct location
    tex_path = os.path.join("TaiLieu", "slideAIAcc", "Slide_AIAcc_Day11.tex")
    os.makedirs(os.path.dirname(tex_path), exist_ok=True)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Generated {tex_path} successfully.")

if __name__ == '__main__':
    create_beamer_day11()
