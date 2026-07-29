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

\title[Buổi 2: Xử lý Dữ liệu]{Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.3cm} \Large Buổi 2: Nhận diện \& Xử lý Dữ liệu Kế toán}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

% SLIDE 1
\begin{frame}
    \titlepage
    \begin{center}
        \includegraphics[width=0.5\textwidth,height=2.5cm,keepaspectratio]{images/Day_02/bg_data.png}
    \end{center}
\end{frame}

% SLIDE 2
\begin{frame}{Nội dung Chương trình}
    \tableofcontents
\end{frame}

% SLIDE 3
\begin{frame}{Khởi động (Ice-breaker)}
    \begin{center}
        \Huge \textbf{"Garbage In, Garbage Out" (GIGO)}
    \end{center}
    \vspace{0.5cm}
    \textbf{Thông điệp:} \\
    AI dù thông minh đến đâu, nếu bạn cấp cho nó dữ liệu sai lệch (rác), nó sẽ đưa ra những quyết định tài chính sai lầm nghiêm trọng. \\
    Sự thành bại của AI nằm ở chất lượng dữ liệu đầu vào.
\end{frame}

% SLIDE 4
\begin{frame}{Tầm quan trọng của Dữ liệu trong Kế toán}
    \begin{itemize}
        \item Kế toán hiện đại không chỉ là "Ghi chép sổ sách" (Bookkeeping).
        \item Kế toán hiện đại chính là \textbf{"Quản trị dữ liệu tài chính"}.
        \item \textbf{Vai trò cốt lõi:} Trước khi AI có thể phân tích xu hướng dòng tiền hay phát hiện gian lận, con người phải đảm bảo dữ liệu đã được cấu trúc đúng.
    \end{itemize}
\end{frame}

\section{1. Dữ liệu Sạch (Clean Data) vs Dữ liệu Bẩn (Dirty Data)}

% SLIDE 5
\begin{frame}{Dữ liệu Sạch (Clean Data) là gì?}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Là dữ liệu nguyên vẹn, chính xác, thống nhất về định dạng.
            \item Không có ô trống vô lý, không bị trùng lặp.
            \item Sẵn sàng để đưa vào phần mềm ERP hoặc hệ thống AI để phân tích ngay lập tức.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02/clean_data.png}
    \end{columns}
\end{frame}

% SLIDE 6
\begin{frame}{Dữ liệu Bẩn (Dirty Data) là gì?}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Là dữ liệu chứa lỗi, không nhất quán, thiếu sót hoặc định dạng sai.
            \item Trớ trêu thay, việc xử lý dữ liệu bẩn chiếm đến \textbf{80\% thời gian} của Kế toán viên mỗi đợt chốt sổ cuối tháng.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02/dirty_data.png}
    \end{columns}
\end{frame}

% SLIDE 7
\begin{frame}{Các loại "Dữ liệu Bẩn" phổ biến (Phần 1)}
    \begin{itemize}
        \item \textbf{Sai định dạng (Formatting errors):} Cột Ngày tháng lộn xộn giữa \texttt{MM/DD/YYYY} (Mỹ) và \texttt{DD/MM/YYYY} (Việt Nam).
        \item \textbf{Khoảng trắng thừa (Leading/Trailing Spaces):} \\
        \textit{" Công ty A "} hoàn toàn khác với \textit{"Công ty A"}. \\
        Máy tính và AI sẽ hiểu đây là 2 đối tượng độc lập.
    \end{itemize}
\end{frame}

% SLIDE 8
\begin{frame}{Các loại "Dữ liệu Bẩn" phổ biến (Phần 2)}
    \begin{itemize}
        \item \textbf{Trùng lặp (Duplicates):} Cùng một khách hàng bị tạo thành 2 mã khách hàng (Customer ID) khác nhau do nhân viên sale gõ sai tên.
        \item \textbf{Giá trị rỗng (Null / Missing values):} Đơn hàng không có mã số thuế, thiếu mã vùng, thiếu số lượng.
    \end{itemize}
\end{frame}

% SLIDE 9
\begin{frame}{Hệ lụy của Dữ liệu Bẩn}
    \begin{itemize}
        \item \textbf{Lập báo cáo tài chính sai lệch:} Sai lệch công nợ, đánh giá sai hàng tồn kho.
        \item \textbf{Ra quyết định kinh doanh sai:} Ban giám đốc tưởng lãi nhưng thực chất lỗ.
        \item \textbf{Rủi ro tuân thủ (Compliance risks):} Phạt thuế do kê khai sai số liệu hóa đơn.
    \end{itemize}
\end{frame}

% SLIDE 10
\begin{frame}{Vai trò của Kế toán viên trong kỷ nguyên AI}
    \begin{itemize}
        \item Tin vui: Bạn không cần phải tự tay dọn dẹp hàng vạn dòng dữ liệu (AI và phần mềm có thể làm tự động).
        \item \textbf{Nhiệm vụ của bạn:} Phải \textbf{Nhận diện} được dữ liệu đang bị bẩn ở đâu, lỗi gì, để ra "Lệnh" (Prompt) cho AI dọn dẹp đúng chỗ.
    \end{itemize}
\end{frame}

\section{2. Tổ chức \& Lưu trữ Dữ liệu (Relational Databases)}

% SLIDE 11
\begin{frame}{Làm sao để lưu trữ khối lượng dữ liệu khổng lồ?}
    \begin{itemize}
        \item Excel rất tuyệt vời, nhưng không thể chứa hàng triệu giao dịch mỗi ngày một cách ổn định.
        \item \textbf{Giải pháp:} Cơ sở dữ liệu quan hệ (Relational Database).
        \item Đa số phần mềm kế toán hiện tại (MISA, SAP, Oracle) đều chạy ngầm trên nền tảng cơ sở dữ liệu này.
    \end{itemize}
\end{frame}

% SLIDE 12
\begin{frame}{Khái niệm Relational Database}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Lưu trữ dữ liệu trong các \textbf{Bảng (Tables)} riêng biệt thay vì dồn chung vào một file khổng lồ.
            \item Các bảng được liên kết với nhau theo logic nghiệp vụ chặt chẽ.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02/db_schema.png}
    \end{columns}
\end{frame}

% SLIDE 13
\begin{frame}{Thành phần của một Bảng (Table)}
    \begin{itemize}
        \item \textbf{Bảng (Table):} Đại diện cho một thực thể (VD: Bảng Khách hàng, Bảng Hóa đơn).
        \item \textbf{Dòng (Row / Record):} Đại diện cho 1 đối tượng duy nhất (VD: 1 khách hàng cụ thể).
        \item \textbf{Cột (Column / Attribute):} Các thuộc tính mô tả đối tượng (Mã KH, Tên KH, Địa chỉ).
    \end{itemize}
\end{frame}

% SLIDE 14
\begin{frame}{Khóa chính (Primary Key) là gì?}
    \begin{itemize}
        \item Là mã định danh độc nhất cho mỗi dòng trong bảng.
        \item \textbf{Ví dụ đời thực:} Mỗi người chỉ có 1 số CCCD.
        \item \textbf{Ví dụ kế toán:} Mã Khách Hàng (CustomerID), Số Hóa Đơn (Invoice Number).
        \item \textbf{Quy tắc:} Không bao giờ được phép trùng lặp (Duplicate) hoặc để trống (Null).
    \end{itemize}
\end{frame}

% SLIDE 15
\begin{frame}{Khóa ngoại (Foreign Key) là gì?}
    \begin{itemize}
        \item Là một cột trong bảng này, nhưng lại chứa dữ liệu trỏ tới \textbf{Primary Key} của bảng khác.
        \item Dùng để \textbf{tạo liên kết (Relationship)} giữa các bảng.
        \item \textbf{Ví dụ:} Cột \texttt{CustomerID} trong bảng "Hóa đơn" là Khóa ngoại trỏ về bảng "Khách hàng", cho biết hóa đơn này của ai.
    \end{itemize}
\end{frame}

% SLIDE 16
\begin{frame}{Liên kết dữ liệu (Joins)}
    \begin{columns}
        \column{0.5\textwidth}
        Khi dữ liệu nằm rải rác ở nhiều bảng, ta dùng thao tác \textbf{"Join"} để kết hợp chúng lại phục vụ việc lập báo cáo tổng hợp.
        \vspace{0.3cm}
        \\ Bốn loại phổ biến: Inner, Left, Right, Full.
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02/joins_venn.png}
    \end{columns}
\end{frame}

% SLIDE 17
\begin{frame}{Ứng dụng của Inner Join trong Kiểm toán}
    \begin{itemize}
        \item \textbf{Định nghĩa:} Chỉ lấy các dòng có dữ liệu khớp nhau ở cả 2 bảng.
        \item \textbf{Ứng dụng kế toán:} "Có nhân viên nào có số điện thoại cá nhân trùng với số điện thoại của Nhà cung cấp không?" (Tức là ghép bảng Nhân viên và bảng Nhà cung cấp).
        \item Dấu hiệu của gian lận lập công ty "sân sau".
    \end{itemize}
\end{frame}

% SLIDE 18
\begin{frame}{Ứng dụng của Left / Right Join}
    \begin{itemize}
        \item \textbf{Định nghĩa Left Join:} Lấy toàn bộ dữ liệu bảng Trái, và ghép phần khớp của bảng Phải (phần không khớp sẽ báo \texttt{Null}).
        \item \textbf{Ứng dụng kế toán:} "Có hóa đơn mua hàng nào chưa được thanh toán không?" 
        \item Ghép bảng Hóa đơn (Trái) với bảng Thanh toán (Phải). Bất kỳ hóa đơn nào hiển thị Null ở cột thanh toán nghĩa là đang nợ.
    \end{itemize}
\end{frame}

\section{3. Các hàm cốt lõi \& Tư duy chuẩn hóa}

% SLIDE 19
\begin{frame}{Từ lý thuyết đến thực hành (Functions)}
    \begin{itemize}
        \item Database thường dành cho hệ thống lớn. 
        \item Trong thực tế làm việc hàng ngày tại các SME, Excel/Google Sheets vẫn là vua.
        \item Kế toán viên cần nắm vững tư duy sử dụng \textbf{Hàm (Functions)} để biến dữ liệu bẩn thành sạch một cách tự động.
    \end{itemize}
\end{frame}

% SLIDE 20
\begin{frame}{Hàm xử lý văn bản (Text Functions)}
    Giúp khắc phục ngay lập tức các lỗi do con người nhập liệu sai quy cách:
    \begin{itemize}
        \item \textbf{TRIM():} Cắt bỏ mọi khoảng trắng thừa vô lý ở đầu/cuối chuỗi.
        \item \textbf{UPPER():} Viết hoa toàn bộ chữ cái (chuẩn hóa Mã Khách Hàng).
        \item \textbf{PROPER():} Viết hoa chữ cái đầu tiên (chuẩn hóa Tên Công ty, Tên người).
    \end{itemize}
\end{frame}

% SLIDE 21
\begin{frame}{Hàm Logic (Logical Functions)}
    Dùng để rẽ nhánh, phân loại và chấm điểm dữ liệu tự động.
    \begin{itemize}
        \item \textbf{IF():} Cấu trúc điều kiện kinh điển. Nếu [Điều kiện] đúng thì trả về [A], sai thì trả về [B].
        \item \textbf{Ví dụ:} \texttt{IF(Doanh thu > 1 tỷ, "Khách VIP", "Khách thường")}
    \end{itemize}
\end{frame}

% SLIDE 22
\begin{frame}{Kết hợp AND / OR}
    Đánh giá nhiều điều kiện phức tạp cùng một lúc.
    \begin{itemize}
        \item \textbf{Ví dụ cảnh báo nợ xấu:} 
        \item \texttt{IF(AND(Nợ > 90 ngày, Chưa có cam kết trả), "Rủi ro cao", "Bình thường")}
    \end{itemize}
\end{frame}

% SLIDE 23
\begin{frame}{Hàm tra cứu (Lookup Functions)}
    \begin{columns}
        \column{0.5\textwidth}
        Tra cứu và ghép nối dữ liệu từ các bảng khác nhau. (Đóng vai trò giống như thao tác JOIN trong CSDL).
        \vspace{0.3cm}
        \\ \textbf{VLOOKUP():} Phổ biến nhất nhưng dễ lỗi (chỉ tìm từ trái sang phải).
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02/vlookup.png}
    \end{columns}
\end{frame}

% SLIDE 24
\begin{frame}{Kỷ nguyên mới với XLOOKUP}
    \begin{itemize}
        \item Microsoft đã ra mắt \textbf{XLOOKUP} để khắc phục mọi nhược điểm của VLOOKUP.
        \item Tìm kiếm hai chiều (trái-phải, trên-dưới).
        \item Tự động xử lý lỗi \texttt{\#N/A} (Giá trị Null) rất gọn gàng.
        \item Lời khuyên: Hãy dần chuyển sang dùng XLOOKUP trong kế toán hiện đại.
    \end{itemize}
\end{frame}

% SLIDE 25
\begin{frame}{Tư duy làm việc với hàm trong thời đại AI}
    \begin{center}
        \Large \textbf{Bạn KHÔNG cần thuộc lòng cú pháp!}
    \end{center}
    \vspace{0.5cm}
    \begin{itemize}
        \item Đừng cố nhớ vị trí các dấu phẩy, ngoặc đơn.
        \item \textbf{Chỉ cần biết:} "Bài toán này NÊN dùng hàm loại gì".
        \item Sau đó dùng AI (ChatGPT, Excel Copilot): \textit{"Viết cho tôi hàm tra cứu mã khách hàng từ Sheet 1 sang Sheet 2 dựa vào Mã số thuế."}
    \end{itemize}
\end{frame}

\section{4. Tổng hợp dữ liệu (Pivot Tables)}

% SLIDE 26
\begin{frame}{Vấn đề của Bảng dữ liệu phẳng (Flat Table)}
    \begin{itemize}
        \item Bạn có 1 file Excel xuất từ phần mềm ra chứa \textbf{450.000 dòng} chi tiết bán hàng.
        \item Sếp yêu cầu: \textit{"Báo cáo ngay tổng doanh thu theo từng chi nhánh trong năm nay."}
        \item Nếu dùng hàm SUMIF, file sẽ bị treo vì khối lượng tính toán quá nặng.
    \end{itemize}
\end{frame}

% SLIDE 27
\begin{frame}{Giải pháp: Pivot Table}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Công cụ mạnh mẽ nhất trong Excel để tóm tắt, nhóm (group) và tính toán dữ liệu khổng lồ.
            \item Thao tác hoàn toàn bằng \textbf{kéo thả (Drag \& Drop)}.
            \item Không cần viết bất kỳ dòng lệnh nào. Tốc độ xử lý trong tích tắc.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02/pivot_table.png}
    \end{columns}
\end{frame}

% SLIDE 28
\begin{frame}{Cơ chế hoạt động của Pivot Table}
    \begin{itemize}
        \item \textbf{Pivot (Trục xoay):} Cung cấp khả năng xoay các góc nhìn dữ liệu (View) một cách linh hoạt.
        \item Từ một danh sách chi tiết dài dằng dặc, biến thành một bảng tổng hợp gọn gàng 2 chiều.
    \end{itemize}
\end{frame}

% SLIDE 29
\begin{frame}{Các thành phần cấu tạo nên Pivot Table}
    \begin{itemize}
        \item \textbf{Rows (Dòng):} Gom nhóm dữ liệu theo hàng (Vd: Tên khu vực, Chi nhánh).
        \item \textbf{Columns (Cột):} Tách dữ liệu theo cột (Vd: Theo từng Quý, Tháng).
        \item \textbf{Values (Giá trị):} Các phép tính toán (Vd: \texttt{SUM} Tổng doanh thu, \texttt{COUNT} Số lượng đơn).
        \item \textbf{Filters (Bộ lọc):} Lọc loại bỏ dữ liệu không cần thiết.
    \end{itemize}
\end{frame}

% SLIDE 30
\begin{frame}{Bộ lọc động (Slicers)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Slicers:} Là bảng điều khiển trực quan dạng nút bấm.
            \item Giúp người dùng (hoặc Sếp) tự bấm để lọc báo cáo mà không cần biết dùng Excel.
            \item Nâng tầm báo cáo từ dạng tĩnh sang dạng tương tác (Interactive).
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02/slicer.png}
    \end{columns}
\end{frame}

% SLIDE 31
\begin{frame}{Ứng dụng Pivot Table trong Kế toán}
    \begin{itemize}
        \item Lên bảng Cân đối phát sinh tự động từ file Nhật ký chung.
        \item Lập Báo cáo Tuổi nợ (Aging report) theo các mốc 30-60-90 ngày.
        \item Phân tích chi phí phát sinh theo từng phòng ban/dự án để kiểm soát ngân sách.
    \end{itemize}
\end{frame}

% SLIDE 32
\begin{frame}{AI và Pivot Table}
    \begin{itemize}
        \item Sự ra đời của Copilot for Excel đã thay đổi cuộc chơi.
        \item Người dùng không cần tự kéo thả các trường (Fields).
        \item Chỉ cần Prompt: \textit{"Show me total sales by region in a pivot table."} - AI sẽ tự dựng bảng Pivot tức thì.
    \end{itemize}
\end{frame}

\section{5. Thống kê mô tả \& Trực quan hóa}

% SLIDE 33
\begin{frame}{Từ Dữ liệu đến Insights}
    \begin{center}
        \Large Dữ liệu thô $\rightarrow$ Làm sạch $\rightarrow$ Phân tích $\rightarrow$ \textbf{Insights (Sự thấu hiểu)}
    \end{center}
    \vspace{0.5cm}
    Bước đầu tiên của phân tích chính là sử dụng \textbf{Thống kê mô tả (Descriptive Statistics)} để tóm tắt các đặc điểm của tập dữ liệu.
\end{frame}

% SLIDE 34
\begin{frame}{Các đại lượng đo lường vị trí (Location)}
    \begin{itemize}
        \item \textbf{Mean (Trung bình):} Dễ tính nhưng dễ bị nhiễu bởi các giá trị ngoại lai cực lớn/nhỏ (Outliers).
        \item \textbf{Median (Trung vị):} Phản ánh con số thực tế "nằm giữa" tập dữ liệu.
        \item \textbf{Ứng dụng thực tế:} Khi báo cáo mức lương, người ta hay dùng Lương trung vị thay vì trung bình để tránh bị kéo lệch bởi mức lương quá cao của CEO.
    \end{itemize}
\end{frame}

% SLIDE 35
\begin{frame}{Đo lường độ phân tán (Dispersion)}
    \begin{itemize}
        \item \textbf{Variance (Phương sai) \& Standard Deviation (Độ lệch chuẩn).}
        \item Đo lường mức độ rủi ro hoặc biến động của dữ liệu.
        \item \textbf{Ứng dụng trong Kế toán quản trị:} Phân tích độ lệch của chi phí sản xuất thực tế so với định mức dự toán ban đầu. Chi phí càng dao động mạnh, rủi ro càng cao.
    \end{itemize}
\end{frame}

% SLIDE 36
\begin{frame}{Vì sao cần Trực quan hóa dữ liệu? (Data Visualization)}
    \begin{itemize}
        \item Não bộ con người xử lý hình ảnh \textbf{nhanh hơn 60.000 lần} so với văn bản và các dãy số.
        \item Đừng bắt Sếp đọc 1 ma trận số liệu Excel! 
        \item Biểu đồ giúp Ban giám đốc "nhìn" thấy ngay vấn đề (trend giảm sút, chi phí tăng vọt) chỉ trong vài giây.
    \end{itemize}
\end{frame}

% SLIDE 37
\begin{frame}{Lựa chọn Biểu đồ phù hợp (Phần 1)}
    \begin{itemize}
        \item \textbf{Biểu đồ Cột (Bar/Column Chart):} So sánh giá trị tuyệt đối giữa các hạng mục. VD: So sánh Doanh thu các chi nhánh.
        \item \textbf{Biểu đồ Tròn (Pie Chart):} Thể hiện tỷ trọng (100\%). VD: Cơ cấu chi phí sản xuất. \textbf{Lưu ý:} Không dùng Pie Chart khi có quá nhiều mẩu nhỏ vụn vặt.
    \end{itemize}
\end{frame}

% SLIDE 38
\begin{frame}{Lựa chọn Biểu đồ phù hợp (Phần 2)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Biểu đồ Đường (Line Chart):} Thể hiện xu hướng theo dòng thời gian (Biến động dòng tiền 12 tháng).
            \item \textbf{Biểu đồ Phân tán (Scatter Plot):} Tìm mối tương quan giữa 2 biến số (VD: Chi phí quảng cáo và Doanh số bán hàng).
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02/chart_comparison.png}
    \end{columns}
\end{frame}

% SLIDE 39
\begin{frame}{Công cụ Trực quan hóa dữ liệu hiện đại}
    \begin{itemize}
        \item Excel cơ bản vẫn hỗ trợ tốt.
        \item Nâng cao hơn, các nền tảng như \textbf{Tableau} hoặc \textbf{Power BI} đang trở thành kỹ năng bắt buộc cho Kế toán quản trị.
        \item Tích hợp biểu đồ trực tiếp vào các \textbf{Dashboard} (Bảng điều khiển) cập nhật thời gian thực.
    \end{itemize}
\end{frame}

% SLIDE 40
\begin{frame}{Tổng kết Buổi 2}
    \begin{itemize}
        \item \textbf{Nền tảng:} Hiểu về Dữ liệu sạch \& Cấu trúc Relational Database.
        \item \textbf{Công cụ:} Nắm bắt tư duy dùng Hàm \& Pivot Table để dọn dẹp, tổng hợp dữ liệu.
        \item \textbf{Báo cáo:} Dùng Thống kê mô tả và Biểu đồ để kể câu chuyện tài chính (Data Storytelling).
    \end{itemize}
    \vspace{0.5cm}
    \begin{center}
        \textbf{Tiền đề quan trọng:} \\ Dữ liệu phải SẠCH thì các buổi sau ứng dụng AI mới CHÍNH XÁC!
    \end{center}
\end{frame}

\end{document}
"""

with open(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\Slide_AIAcc_v2_Day02_LT.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)
