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

\title[Buổi 2: Thực hành Power Query]{Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.3cm} \Large Thực hành: Chuẩn hóa Dữ liệu bằng Power Query}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

% SLIDE 1
\begin{frame}
    \titlepage
    \begin{center}
        \includegraphics[width=0.5\textwidth,height=2.5cm,keepaspectratio]{images/Day_02_TH/bg_pq.png}
    \end{center}
\end{frame}

% SLIDE 2
\begin{frame}{Nội dung Chương trình Thực hành}
    \tableofcontents
\end{frame}

\section{1. Sức mạnh của Power Query}

% SLIDE 3
\begin{frame}{Nỗi ám ảnh của Kế toán viên}
    Có bao giờ bạn phải mất hàng giờ đồng hồ mỗi cuối tháng chỉ để:
    \begin{itemize}
        \item Copy-paste dữ liệu từ 12 file Excel của 12 tháng lại với nhau?
        \item Dò tìm lỗi VLOOKUP bị \texttt{\#N/A} vì khác định dạng?
        \item Xóa thủ công hàng ngàn dòng trắng và khoảng cách thừa do copy từ phần mềm ERP?
    \end{itemize}
\end{frame}

% SLIDE 4
\begin{frame}{Giải pháp mang tên Power Query}
    \begin{itemize}
        \item \textbf{Power Query là gì?} Là một công cụ kết nối và chuẩn hóa dữ liệu siêu mạnh mẽ của Microsoft.
        \item Được ví như "Trợ lý dọn dẹp dữ liệu cá nhân" (Personal Data Assistant).
        \item \textbf{Đặc biệt:} Hoàn toàn \textbf{KHÔNG} cần biết code (No-code Data Transformation).
    \end{itemize}
\end{frame}

% SLIDE 5
\begin{frame}{Power Query nằm ở đâu?}
    \begin{columns}
        \column{0.5\textwidth}
        Được tích hợp sẵn và hoàn toàn miễn phí.
        \begin{itemize}
            \item \textbf{Trong Excel:} Vào tab \texttt{Data} $\rightarrow$ Chọn nhóm \texttt{Get \& Transform Data}.
            \item \textbf{Trong Power BI Desktop:} Nút \texttt{Get Data} $\rightarrow$ \texttt{Transform Data}.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02_TH/get_data.png}
    \end{columns}
\end{frame}

% SLIDE 6
\begin{frame}{Giao diện Power Query Editor (Phần 1)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Ribbon (Thanh công cụ):} Chứa các tab \texttt{Home}, \texttt{Transform}, \texttt{Add Column}. Nơi thực hiện các phép thuật biến đổi.
            \item \textbf{Queries Pane (Cửa sổ Queries):} Nằm bên trái, quản lý danh sách các bảng dữ liệu đang được kết nối.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02_TH/pq_interface.png}
    \end{columns}
\end{frame}

% SLIDE 7
\begin{frame}{Giao diện Power Query Editor (Phần 2)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Data Preview:} Khu vực trung tâm hiển thị trực tiếp dữ liệu.
            \item \textbf{Applied Steps:} Khung bên phải - \textbf{Tính năng đáng giá nhất!} Ghi lại toàn bộ lịch sử thao tác giống như một cuốn băng ghi hình.
            \item Có thể \texttt{Undo} bất kỳ bước nào chỉ bằng 1 cú click (dấu \texttt{X}).
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02_TH/applied_steps.png}
    \end{columns}
\end{frame}

\section{2. Thao tác Dọn dẹp Cơ bản}

% SLIDE 8
\begin{frame}{Tại sao không làm trực tiếp trên Excel?}
    \begin{itemize}
        \item Khi sửa dữ liệu trực tiếp trên ô Excel, nếu lỡ làm sai sẽ rất khó khôi phục, và tháng sau phải làm lại từ đầu.
        \item \textbf{Power Query lưu lại quy trình (Applied Steps).} Tháng sau khi có data mới, chỉ cần bấm \texttt{Refresh}, dữ liệu mới sẽ tự động chạy qua phễu lọc cũ.
    \end{itemize}
\end{frame}

% SLIDE 9
\begin{frame}{Thao tác 1 - Xóa cột thừa (Removing Columns)}
    \begin{itemize}
        \item Báo cáo kết xuất từ phần mềm ERP thường kèm theo rất nhiều cột mã hệ thống không cần thiết cho kế toán.
        \item \textbf{Thực hành:} Nhấn chuột phải vào tiêu đề cột $\rightarrow$ Chọn \texttt{Remove}.
        \item \textbf{Lợi ích:} Làm nhẹ file, tăng tốc độ tính toán.
    \end{itemize}
\end{frame}

% SLIDE 10
\begin{frame}{Thao tác 2 - Đổi kiểu dữ liệu (Changing Data Types)}
    \begin{itemize}
        \item Đây là nguyên nhân hàng đầu gây lỗi VLOOKUP! (Vd: Số hóa đơn lưu dạng Text vs lưu dạng Number).
        \item \textbf{Thực hành:} Click vào biểu tượng định dạng ở góc trái tiêu đề cột (\texttt{ABC}, \texttt{123}, biểu tượng lịch).
        \item Chọn \texttt{Whole Number}, \texttt{Text} hoặc \texttt{Date} cho phù hợp.
    \end{itemize}
\end{frame}

% SLIDE 11
\begin{frame}{Thao tác 3 - Lọc các dòng bị lỗi (Filtering Rows)}
    \begin{itemize}
        \item Loại bỏ các dòng tiêu đề rác của hệ thống hoặc các dòng trống.
        \item \textbf{Thực hành:} Bấm vào nút mũi tên trên tiêu đề cột $\rightarrow$ Bỏ chọn \texttt{(null)} hoặc \texttt{Blank}.
        \item Giống hệt công cụ Filter trong Excel, nhưng quá trình này được lưu vĩnh viễn vào bộ máy tự động.
    \end{itemize}
\end{frame}

% SLIDE 12
\begin{frame}{Thao tác 4 - Thay thế giá trị (Replace Values)}
    \begin{itemize}
        \item Giúp sửa các lỗi sai chính tả hàng loạt. (Ví dụ: "Hà nôi", "HN", "Ha Noi" cần gộp chung thành "Hà Nội").
        \item \textbf{Thực hành:} Chuột phải vào tiêu đề cột $\rightarrow$ Chọn \texttt{Replace Values}.
        \item Nhập \texttt{Value To Find} (Giá trị cũ) và \texttt{Replace With} (Giá trị mới).
    \end{itemize}
\end{frame}

% SLIDE 13
\begin{frame}{Thao tác 5 - Tách cột (Split Column)}
    \begin{itemize}
        \item \textbf{Ví dụ:} Cột ghi là "Nguyễn Văn A - Kế toán" cần tách riêng Tên và Phòng ban.
        \item \textbf{Thực hành:} Chọn cột $\rightarrow$ Trên thanh Ribbon chọn \texttt{Split Column} $\rightarrow$ \texttt{By Delimiter}.
        \item Ký tự phân cách (Delimiter) ở đây là dấu gạch ngang \texttt{-}.
    \end{itemize}
\end{frame}

% SLIDE 14
\begin{frame}{Thao tác 6 - Trim \& Clean}
    \begin{itemize}
        \item \textbf{Trim:} Xóa khoảng trắng thừa (Leading/Trailing spaces) do người dùng lỡ bấm dấu cách.
        \item \textbf{Clean:} Xóa các ký tự không in được (non-printable characters).
        \item Đặc biệt hữu dụng với dữ liệu sao kê tải xuống từ hệ thống ngân hàng (Bank Statements).
    \end{itemize}
\end{frame}

% SLIDE 15
\begin{frame}{Giới thiệu ngôn ngữ M (M Code)}
    \begin{itemize}
        \item Các thao tác "kéo thả" của bạn thực chất được Power Query tự động dịch thành ngôn ngữ lập trình gọi là "M" (hiển thị ở Formula Bar).
        \item Bạn \textbf{KHÔNG} cần biết code M để dùng Power Query.
        \item Tuy nhiên, nếu biết M, bạn có thể chỉnh sửa sâu hơn và thực hiện các biến đổi phức tạp mà giao diện không hỗ trợ.
    \end{itemize}
\end{frame}

\section{3. Hợp nhất Dữ liệu (Append \& Merge)}

% SLIDE 16
\begin{frame}{Nghệ thuật Hợp nhất dữ liệu}
    Trong thực tế, dữ liệu không bao giờ nằm sẵn trong 1 bảng đẹp đẽ duy nhất. Chúng ta có 2 phương pháp ghép bảng:
    \begin{itemize}
        \item Hợp nhất theo chiều dọc: \textbf{Append Queries} (Nối dữ liệu lên nhau).
        \item Hợp nhất theo chiều ngang: \textbf{Merge Queries} (Móc nối dữ liệu bằng mã chung).
    \end{itemize}
\end{frame}

% SLIDE 17
\begin{frame}{Gộp bảng theo chiều dọc (Append Queries)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Bài toán:} Kế toán có 12 file Excel (từ tháng 1 đến 12). Cần gộp thành 1 bảng duy nhất.
            \item \textbf{Giải pháp:} Dùng \texttt{Append Queries}. Các file có cùng cấu trúc cột sẽ tự động xếp chồng lên nhau như Lego.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02_TH/append_queries.png}
    \end{columns}
\end{frame}

% SLIDE 18
\begin{frame}{Lợi ích cực lớn của Append Queries}
    \begin{itemize}
        \item \textbf{So với Copy-Paste thủ công:} Nếu tháng sau có thêm file "Tháng 13" hoặc "Tháng 14".
        \item Bạn chỉ cần quăng file mới vào chung thư mục, bấm \texttt{Refresh} trong file tổng.
        \item Dữ liệu tự động cập nhật báo cáo ngay lập tức!
    \end{itemize}
\end{frame}

% SLIDE 19
\begin{frame}{Gộp bảng theo chiều ngang (Merge Queries)}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Bản nâng cấp hoàn hảo của hàm VLOOKUP.
            \item \textbf{Bài toán:} Bạn có bảng Hóa Đơn chứa \texttt{CustomerID}, cần mang \texttt{CustomerName} từ bảng Khách Hàng vào.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02_TH/merge_queries.png}
    \end{columns}
\end{frame}

% SLIDE 20
\begin{frame}{Cách thực hiện Merge Queries}
    \begin{itemize}
        \item Trên Ribbon chọn \texttt{Merge Queries}.
        \item Chọn bảng \textbf{A} (Hóa đơn) và bảng \textbf{B} (Khách hàng).
        \item \textbf{Bước cực kỳ quan trọng:} Click chọn cột \textbf{Khóa ngoại (Foreign Key)} và \textbf{Khóa chính (Primary Key)} khớp nhau giữa 2 bảng.
    \end{itemize}
\end{frame}

% SLIDE 21
\begin{frame}{Tại sao Merge lại "ăn đứt" VLOOKUP?}
    \begin{itemize}
        \item Hàm VLOOKUP rất nặng, làm file Excel bị đơ/treo nếu có hàng trăm ngàn dòng.
        \item VLOOKUP luôn bắt buộc tìm từ trái sang phải.
        \item \textbf{Merge Queries:} Xử lý ngầm, siêu nhẹ, không tốn bất kỳ ô Excel nào để tính toán, tốc độ cực nhanh và linh hoạt.
    \end{itemize}
\end{frame}

% SLIDE 22
\begin{frame}{Pivot \& Unpivot (Xoay và Bỏ xoay dữ liệu)}
    \begin{itemize}
        \item Thường gặp khi dữ liệu bị trình bày sai cấu trúc (Các tháng nằm ngang thành từng cột thay vì nằm dọc).
        \item \textbf{Thực hành:} Quét các cột tháng, dùng lệnh \texttt{Unpivot Columns}.
        \item Kết quả: Trả về chuẩn 1 cột "Thuộc tính" (Tháng) và 1 cột "Giá trị" (Doanh thu). Sẵn sàng làm Pivot Table!
    \end{itemize}
\end{frame}

\section{4. LAB - Thực hành (Apply It)}

% SLIDE 23
\begin{frame}{LAB 1: Case Study - Super Scooters}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Bối cảnh:} Hãng sản xuất xe "Super Scooters" chia Database thành 4 bảng: Locations, SalesOrders, Employee, Customer.
            \item \textbf{Nhiệm vụ:} Nhận diện cấu trúc liên kết.
        \end{itemize}
        \column{0.5\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{images/Day_02_TH/super_scooters.png}
    \end{columns}
\end{frame}

% SLIDE 24
\begin{frame}{Phân tích LAB 1 - Tìm Primary Key}
    Xác định \textbf{Primary Key} (Khóa chính) không được trùng lặp của các bảng:
    \begin{itemize}
        \item \textbf{Bảng Locations:} \texttt{LocationNumber}
        \item \textbf{Bảng Employee:} \texttt{EmployeeNumber}
        \item \textbf{Bảng Customer:} \texttt{CustomerNumber}
        \item \textbf{Bảng SalesOrders:} \texttt{SalesOrderNumber}
    \end{itemize}
\end{frame}

% SLIDE 25
\begin{frame}{Phân tích LAB 1 - Tìm Foreign Key}
    Bảng trung tâm \textbf{SalesOrders} cần nối với các bảng vệ tinh thông qua các \textbf{Foreign Keys} (Khóa ngoại) nào?
    \begin{itemize}
        \item Chứa \texttt{ItemNumber} (Nối với bảng Hàng hóa).
        \item Chứa \texttt{CustomerNumber} (Nối với bảng Khách hàng).
        \item Chứa \texttt{EmployeeNumber} (Nối với bảng Nhân viên bán hàng).
    \end{itemize}
\end{frame}

% SLIDE 26
\begin{frame}{LAB 2: Xử lý Hóa đơn Bán hàng thực tế}
    \begin{itemize}
        \item \textbf{Tình huống:} Kế toán được gửi một file "Báo cáo bán hàng thô".
        \item \textbf{Vấn đề 1:} Cột "Tên Khách Hàng" bị dính mã số ở đằng sau (VD: \textit{Nguyễn Văn A - KH001}).
        \item \textbf{Vấn đề 2:} Cột "Doanh thu" đang bị hiểu nhầm là định dạng Text (ABC) nên không tính tổng được.
    \end{itemize}
\end{frame}

% SLIDE 27
\begin{frame}{Live Demo - Giải quyết LAB 2}
    Cùng thực hành trực tiếp:
    \begin{enumerate}
        \item Import dữ liệu vào Power Query (\texttt{Get Data}).
        \item Dùng \texttt{Split Column by Delimiter} (Dấu \texttt{-}) để tách cột Tên và Mã khách hàng.
        \item Nhấn vào tiêu đề cột Doanh thu, đổi Data Type sang \texttt{Decimal Number}.
        \item Chọn \texttt{Close \& Load} để xuất bảng sạch ra Excel.
    \end{enumerate}
\end{frame}

% SLIDE 28
\begin{frame}{Tham số hóa (Parameters) nâng cao}
    \begin{itemize}
        \item Giúp truy vấn có tính \textbf{Động (Dynamic)}.
        \item \textbf{Ví dụ:} Thay vì tạo bộ lọc cố định là "Năm 2025", ta tạo một Parameter tên là "Năm Báo Cáo".
        \item Tháng sau, người dùng chỉ cần nhập số "2026", toàn bộ luồng xử lý tự động chạy lại cho năm mới.
    \end{itemize}
\end{frame}

% SLIDE 29
\begin{frame}{Load to Data Model (Mô hình Dữ liệu)}
    Sau khi Clean dữ liệu xong, ta xuất kết quả ra đâu?
    \begin{itemize}
        \item \textbf{Table:} Xuất ra sheet Excel bình thường (Sẽ bị lỗi nếu file có trên 1 triệu dòng).
        \item \textbf{Only Create Connection \& Add to Data Model:} Lưu ngầm trong bộ nhớ RAM, dùng để tạo Pivot Table trực tiếp. Rất mượt mà dù file có hàng chục triệu dòng!
    \end{itemize}
\end{frame}

\section{5. Tổng kết \& Bài tập}

% SLIDE 30
\begin{frame}{Best Practices khi dùng Power Query}
    \begin{itemize}
        \item \textbf{Đặt tên chuẩn:} Đổi tên Queries (Bảng) cho có ý nghĩa thay vì để mặc định \texttt{Table1}, \texttt{Table2} (VD: \texttt{tbl\_DanhSachKhachHang}).
        \item \textbf{Ghi chú (Document):} Ghi chú các bước thao tác phức tạp trong ô \texttt{Properties} của Applied Steps để người sau đọc còn hiểu.
        \item \textbf{Kiểm thử (Test):} Thường xuyên kiểm tra lại các bước truy vấn trước khi Load.
    \end{itemize}
\end{frame}

% SLIDE 31
\begin{frame}{Tổng kết Kiến thức Buổi Thực Hành}
    \begin{itemize}
        \item Power Query là công cụ tự động hóa quá trình chuẩn hóa (Clean) và biến đổi (Transform) dữ liệu số 1 của Microsoft.
        \item Thay thế hoàn hảo cho các thao tác Copy-paste thủ công và VLOOKUP nặng nề.
        \item Cửa sổ \textbf{Applied Steps} giúp bạn xây dựng một "Nhà máy tự động dọn rác dữ liệu".
    \end{itemize}
\end{frame}

% SLIDE 32
\begin{frame}{Hỏi \& Đáp (Q\&A)}
    \begin{itemize}
        \item \textbf{Q: Power Query có tốn phí không?} \\ 
        $\rightarrow$ A: Không, tích hợp sẵn trong Excel 2016 trở lên.
        \item \textbf{Q: Macbook có dùng được Power Query không?} \\ 
        $\rightarrow$ A: Có, Excel for Mac hiện đã hỗ trợ Power Query (dù giao diện hơi khác Windows).
    \end{itemize}
\end{frame}

% SLIDE 33
\begin{frame}{Bài tập về nhà}
    \begin{itemize}
        \item Nhận file dữ liệu \texttt{Sales\_DirtyData.xlsx} từ giảng viên.
        \item \textbf{Nhiệm vụ bằng Power Query:}
        \begin{enumerate}
            \item Loại bỏ các dòng trống ở phần tiêu đề (Filter).
            \item Sử dụng \texttt{Capitalize Each Word} để viết hoa chuẩn tên khách hàng.
            \item \texttt{Close \& Load to} dạng Pivot Table Report để tổng hợp doanh thu theo khách hàng.
        \end{enumerate}
    \end{itemize}
\end{frame}

% SLIDE 34
\begin{frame}
    \begin{center}
        \Huge \textbf{Thank You!}
        
        \vspace{1cm}
        \Large Hãy thực hành ngay trên máy tính của bạn, vì "Thực hành là cách duy nhất để làm chủ Dữ liệu".
    \end{center}
\end{frame}

\end{document}
"""

with open(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\Slide_AIAcc_v2_Day02_TH.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)
