import os

def create_beamer_slide():
    tex_content = r"""\documentclass[aspectratio=169]{beamer}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{xcolor}

% Cấu hình giao diện Beamer
\usetheme{Madrid}
\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}[frame number]

\title[TTNT trong Kế toán - Buổi 8]{Trí tuệ Nhân tạo Ứng dụng trong Kế toán}
\subtitle{Buổi 8: AI trong Tài chính Ngân hàng và Thị trường Chứng khoán}
\author{Giảng viên: [Tên Giảng Viên]}
\institute{Đại học Đông Á}
\date{\today}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Nội dung Bài học}
    \tableofcontents
\end{frame}

% ==========================================
% SECTION 1: Cuộc chiến Không gian Số & Gian lận TMĐT
% ==========================================
\section{Cuộc chiến Không gian Số \& Gian lận Thương mại Điện tử}

\begin{frame}{Khởi đầu: Thị trường bốc hơi ngàn điểm}
    \textbf{Tưởng tượng một viễn cảnh:}
    \begin{itemize}
        \item Toàn bộ thị trường chứng khoán đột ngột bốc hơi hàng ngàn điểm chỉ trong chớp mắt.
        \item Không có khủng hoảng kinh tế, không có chiến tranh, không có sự kiện chính trị chấn động.
        \item Nguyên nhân: Một cỗ máy tự động (Hộp đen bí ẩn) quyết định bán tháo hàng loạt mà không một ai kịp can thiệp.
    \end{itemize}
\end{frame}

\begin{frame}{Vụ Flash Crash 2010: Cơn ác mộng có thật}
    \begin{alertblock}{Flash Crash ngày 06/05/2010}
        Chỉ trong vài phút ngắn ngủi, chỉ số Dow Jones bốc hơi gần 1.000 điểm, thổi bay hàng nghìn tỷ đô la giá trị vốn hóa trước khi đột ngột phục hồi trở lại.
    \end{alertblock}
    Không có bất kỳ sự nhầm lẫn (Fat-finger error) nào của con người. Đó hoàn toàn là chuỗi phản ứng dây chuyền của \textbf{Giao dịch Tần suất cao (High-Frequency Trading)}.
\end{frame}

\begin{frame}{AI: Tấm khiên và Vũ khí}
    \textbf{Hai mặt của Trí tuệ Nhân tạo trong Tài chính:}
    \begin{itemize}
        \item \textbf{Mặt Sáng (Tấm khiên):} AI đóng vai trò bảo vệ túi tiền của chúng ta khỏi sự xâm nhập tinh vi (Thương mại điện tử, Ngân hàng).
        \item \textbf{Mặt Tối (Vũ khí):} AI đang bị các thế lực khổng lồ lợi dụng để thao túng toàn bộ nền kinh tế và bóp nghẹt sự cạnh tranh.
    \end{itemize}
\end{frame}

\begin{frame}{Gian lận Nhấp chuột (Click Fraud) là gì?}
    \begin{itemize}
        \item \textbf{Mô hình PPC (Pay-Per-Click):} Nhà quảng cáo trả tiền cho mỗi lượt nhấp chuột của người dùng vào quảng cáo kỹ thuật số của họ.
        \item \textbf{Gian lận Nhấp chuột:} Các hành vi thao túng giả mạo nhấp chuột để thu lợi bất chính hoặc làm cạn kiệt ngân sách đối thủ.
    \end{itemize}
\end{frame}

\begin{frame}{Ẩn dụ: Khách hàng Ảo làm mòn thảm}
    \begin{exampleblock}{Tấn công cửa hàng}
        Việc gian lận nhấp chuột giống như việc một đối thủ cạnh tranh \textbf{thuê hàng ngàn người giả vờ bước vào cửa hàng của bạn}.
    \end{exampleblock}
    \vspace{0.2cm}
    \begin{itemize}
        \item Họ đi dạo, vặn vòi nước, bật đèn, xài hao điện, làm mòn thảm.
        \item Kết quả: Chi phí vận hành của bạn tăng vọt, ngân sách cạn kiệt mà \textbf{doanh thu vẫn bằng 0}.
    \end{itemize}
\end{frame}

\begin{frame}{Động cơ của Kẻ tấn công}
    Các đối thủ cạnh tranh sử dụng Click Fraud để:
    \begin{enumerate}
        \item Đốt cháy ngân sách Marketing của bạn trong vài giờ.
        \item Đẩy quảng cáo của bạn khỏi trang tìm kiếm (hết tiền).
        \item Tự giành lấy vị trí hiển thị ưu tiên với chi phí thấp hơn.
    \end{enumerate}
\end{frame}

\begin{frame}{Bot Tự động và Nông trại Nhấp chuột}
    \textbf{Kẻ gian thực hiện bằng cách nào?}
    \begin{itemize}
        \item \textbf{Bot \& Script:} Các đoạn mã độc tự động chạy hàng triệu lượt click.
        \item \textbf{Nông trại Nhấp chuột (Click Farms):} Những khu vực giá lao động siêu rẻ, hàng trăm con người ngồi bấm điện thoại thủ công cả ngày để tạo tương tác giả.
        \item \textbf{Nhái nhấp chuột (Click Injection):} Tiêm mã độc vào smartphone của người dùng thật để tạo ra click ảo ẩn danh.
    \end{itemize}
\end{frame}

\begin{frame}{Sự Hoàn hảo Phi tự nhiên của Kẻ giả mạo}
    Nếu Bot được lập trình bắt chước con người, làm sao phát hiện?
    \begin{alertblock}{Đường thẳng hoàn hảo}
        Con người hiếm khi di chuột từ điểm A đến điểm B tạo thành một đường thẳng hoàn hảo. Độ nhiễu tự nhiên luôn tồn tại. Nếu tốc độ và quỹ đạo chuột \textbf{hoàn hảo đến mức phi tự nhiên}, đó chính là Bot!
    \end{alertblock}
\end{frame}

\begin{frame}{Học máy vào cuộc: Cây Quyết định (Decision Tree)}
    \begin{itemize}
        \item AI không nhìn vào 1 biến số đơn lẻ, nó sử dụng \textbf{Cây Quyết định}.
        \item Giống như trò chơi \textbf{20 câu hỏi} diễn ra trong một phần nghìn giây.
        \item Ví dụ: \textit{Thiết bị này đã từng mua hàng chưa? $\rightarrow$ Chưa $\rightarrow$ Giao dịch lúc 3h sáng? $\rightarrow$ Có $\rightarrow$ Tốc độ di chuột phi tự nhiên? $\rightarrow$ Có.}
    \end{itemize}
\end{frame}

\begin{frame}{Rừng Ngẫu nhiên (Random Forest)}
    \begin{itemize}
        \item Một kẻ gian có thể đánh lừa một cái cây quyết định bằng cách tạo ra độ nhiễu giả.
        \item Tuy nhiên, AI dùng \textbf{Random Forest (Rừng ngẫu nhiên)}: Chạy song song hàng ngàn cây quyết định khác nhau.
        \item Nó kiểm tra hàng ngàn tổ hợp hành vi: Vị trí địa lý, thời gian lưu trang, tốc độ cuộn chuột, lịch sử bộ nhớ cache...
    \end{itemize}
\end{frame}

\begin{frame}{Chặn đứng cú nhấp chuột mờ ám}
    \begin{itemize}
        \item Dựa vào quy luật xác suất khổng lồ, mọi sự bất thường sẽ bị lộ diện qua những tương quan vi tế nhất.
        \item Thuật toán sẽ \textbf{chặn đứng cú nhấp chuột đó} và loại bỏ nó khỏi hóa đơn tính tiền của nhà quảng cáo.
    \end{itemize}
\end{frame}

\begin{frame}{Quản lý Thẻ tín dụng (Credit Card Fraud)}
    \textbf{Từ ngân sách Quảng cáo đến Ví tiền thực sự:}
    \begin{itemize}
        \item Hàng triệu giao dịch thẻ diễn ra mỗi giây trên toàn cầu.
        \item Bài toán hóc búa: Làm sao AI phân biệt được đâu là \textbf{chủ thẻ đang mua sắm} và đâu là \textbf{tên trộm đang xài thẻ ăn cắp}?
    \end{itemize}
\end{frame}

\begin{frame}{Phương pháp Cốt lõi: Đường Cơ sở (Baseline)}
    \begin{alertblock}{AI không đi tìm kẻ xấu}
        AI không bắt đầu bằng việc quét khuôn mặt tội phạm. Thay vào đó, nó thiết lập \textbf{Đường Cơ sở (Baseline)} về hành vi bình thường của \textbf{chính chủ thẻ đó}.
    \end{alertblock}
\end{frame}

\begin{frame}{Học từ Thói quen Cá nhân}
    \textbf{Dữ liệu lịch sử chi tiết:}
    \begin{itemize}
        \item Bạn thường mua sắm ở khu vực nào?
        \item Loại hàng hóa ưa thích (Quần áo, Đồ công nghệ...)?
        \item Mức giá trung bình một lần quẹt thẻ là bao nhiêu?
        \item Thói quen mua vào khung giờ nào (Sáng hay tối muộn)?
    \end{itemize}
    \textit{Bất cứ sai lệch quá lớn nào so với Baseline đều bị cắm Cờ đỏ (Red Flag).}
\end{frame}

% ==========================================
% SECTION 2: Dương tính giả, OCR + NLP & Flash Crash
% ==========================================
\section{Dương tính giả, OCR + NLP \& Sự kiện Flash Crash}

\begin{frame}{Bài toán hóc búa: Dương tính giả (False Positives)}
    Hành vi của con người không cố định như máy móc!
    \begin{itemize}
        \item Cuối tuần bạn đột nhiên có hứng bay sang Paris du lịch và quẹt thẻ mua một chiếc túi xách đắt tiền.
        \item Nếu AI cứng nhắc, nó sẽ khóa ngay thẻ của bạn vì "Sai lệch hoàn toàn so với Baseline tại Việt Nam".
    \end{itemize}
\end{frame}

\begin{frame}{Nỗi ác mộng Khóa thẻ oan uổng}
    \begin{alertblock}{Ranh giới mong manh}
        Việc bị khóa thẻ lúc đang cố trả tiền phòng khách sạn ở một quốc gia xa lạ là một trải nghiệm tồi tệ. \textbf{Dương tính giả (False Positives)} làm suy giảm nghiêm trọng chất lượng dịch vụ của Ngân hàng.
    \end{alertblock}
\end{frame}

\begin{frame}{Mạng Nơ-ron và Cân bằng trọng số}
    \begin{itemize}
        \item \textbf{Cơ chế Học máy:} Cân bằng trọng số rủi ro (Weights).
        \item Nếu vị trí địa lý quẹt thẻ thay đổi từ Việt Nam sang Pháp \textbf{chỉ trong 2 tiếng} $\Rightarrow$ Vô lý về mặt vật lý (Trọng số rủi ro cực cao, 99\% là kẻ cắp thông tin thẻ).
    \end{itemize}
\end{frame}

\begin{frame}{AI Hiểu Bối cảnh: Giao dịch ở Paris là Hợp lệ!}
    \begin{exampleblock}{Cập nhật Baseline theo thời gian thực}
        Nếu hệ thống nhận thấy \textbf{cách đó vài tuần, chính chủ thẻ này đã thanh toán mua vé máy bay đi Pháp} $\Rightarrow$ Thuật toán tự động điều chỉnh đường cơ sở. Giao dịch tại Paris lúc này được xem là hợp lý và không bị khóa oan!
    \end{exampleblock}
\end{frame}

\begin{frame}{Làm giả Chứng từ (Document Dispensation)}
    \begin{itemize}
        \item Kẻ gian dùng phần mềm đồ họa tinh vi để chế tác hóa đơn, biên lai giả mạo hoàn hảo đến từng \textbf{pixel}.
        \item Mắt thường (Kiểm toán viên) kiểm tra hồ sơ giấy không thể phát hiện ra nét cắt ghép.
    \end{itemize}
\end{frame}

\begin{frame}{OCR: Chuyển Ảnh thành Văn bản}
    Bước 1: Sử dụng công nghệ \textbf{OCR (Optical Character Recognition)}
    \begin{itemize}
        \item Nhận dạng Ký tự Quang học.
        \item Quét toàn bộ hình ảnh tờ hóa đơn và số hóa nó thành văn bản thô (Text).
    \end{itemize}
    \textit{Nhưng OCR chỉ đọc chữ, nó không hiểu chữ đó có hợp lý hay không.}
\end{frame}

\begin{frame}{Phần Tinh túy: Xử lý Ngôn ngữ Tự nhiên (NLP)}
    Bước 2: Sử dụng \textbf{NLP (Natural Language Processing)}
    \begin{itemize}
        \item NLP soi vào tính Logic của ngôn từ thay vì độ phân giải của bức ảnh.
        \item AI phân tích ngữ nghĩa, cấu trúc và văn phong hành văn.
    \end{itemize}
\end{frame}

\begin{frame}{Ẩn dụ: Dâu ông nọ cắm cằm bà kia}
    \begin{exampleblock}{Sự bất nhất logic}
        Một tờ hóa đơn thanh toán tiền Vật liệu Xây dựng, nhưng thuật toán NLP lại phát hiện \textbf{cấu trúc ngữ pháp, cách sắp xếp chi phí lại mang hơi hướng của một... Hóa đơn Y tế!} (Vì kẻ gian lấy template y tế để chế tác).
    \end{exampleblock}
\end{frame}

\begin{frame}{Dấu Vân tay của Sự Giả mạo}
    \begin{itemize}
        \item Một nhà cung cấp luôn dùng một phong cách hành văn trong 5 năm, đột nhiên hóa đơn mới nhất lại dùng từ ngữ sai chính tả ở những chỗ vô lý.
        \item \textbf{Sự bất nhất về logic ngôn ngữ} chính là dấu vân tay tố cáo sự giả mạo, bất chấp hình ảnh có đẹp đến đâu.
    \end{itemize}
\end{frame}

\begin{frame}{Nguyên tắc "Human in the Loop"}
    \begin{alertblock}{Máy lọc, Con người chốt}
        Trong gian lận chứng từ, Máy móc KHÔNG được quyền tự động hủy hóa đơn. AI chỉ đóng vai trò \textbf{Siêu màng lọc}, khoanh vùng các hồ sơ khả nghi nhất. Một chuyên gia con người sẽ xem xét bối cảnh thực tế để đưa ra phán quyết cuối cùng.
    \end{alertblock}
\end{frame}

\begin{frame}{Đổi vai: Từ Phòng thủ sang Tấn công}
    \begin{itemize}
        \item Nếu AI có thể xử lý hàng triệu giao dịch, phân tích hàng ngàn điểm dữ liệu để chống gian lận...
        \item Chuyện gì xảy ra khi sức mạnh tính toán siêu phàm đó được dùng để \textbf{giao dịch kiếm lời}?
    \end{itemize}
\end{frame}

\begin{frame}{Giao dịch Thuật toán (Algorithmic Trading)}
    \begin{itemize}
        \item Thuật toán Mua/Bán cổ phiếu nhanh hơn cái chớp mắt.
        \item Hàng ngàn lệnh được tung ra thị trường chỉ trong vài phần nghìn giây.
        \item \textbf{Vấn đề:} Hộp đen (Black Box). Đôi khi ngay cả kỹ sư lập trình ra nó cũng không hiểu tại sao AI lại ra quyết định bán vào thời điểm đó.
    \end{itemize}
\end{frame}

\begin{frame}{Bản chất của Sự kiện Flash Crash 2010}
    \textbf{Phản ứng dây chuyền vô tri:}
    \begin{itemize}
        \item Một thuật toán phát hiện sự sụt giảm siêu nhỏ $\rightarrow$ Kích hoạt lệnh bán.
        \item Hàng trăm thuật toán từ các quỹ khác (được thiết lập giống nhau) phát hiện phe kia bán $\rightarrow$ Tự động hùa theo bán tháo.
        \item \textbf{Vòng lặp tử thần kéo giá xuống đáy.} Không có tư duy logic của con người để dừng lại và nói: "Công ty này vẫn tốt, đừng bán".
    \end{itemize}
\end{frame}

% ==========================================
% SECTION 3: Big Tech, Chống độc quyền & Thẩm phán Máy móc
% ==========================================
\section{Big Tech, Chống độc quyền \& Thẩm phán Máy móc}

\begin{frame}{Đạo đức trong Fintech}
    Các thị trường mới nổi (như Ấn Độ) đang tích hợp \textbf{AI Giao dịch độc quyền} vào ứng dụng (ví dụ: Paytm, Zerodha) để người dùng phổ thông cũng được xài AI tư vấn đầu tư.
\end{frame}

\begin{frame}{Vừa đá bóng vừa thổi còi}
    \begin{alertblock}{Xung đột lợi ích}
        Làm sao chứng minh được Cỗ máy AI (Hộp đen) tư vấn cho khách hàng mua mã cổ phiếu đó KHÔNG nhằm mục đích \textbf{ưu tiên lợi ích thanh khoản cho chính Sàn giao dịch}? Tính toàn vẹn của thị trường bị phá vỡ!
    \end{alertblock}
\end{frame}

\begin{frame}{Crypto \& Chiến dịch "Bơm và Xả" (Pump and Dump)}
    \begin{itemize}
        \item Nơi bất đối xứng thông tin là công cụ để trục lợi.
        \item Kẻ gian dùng Discord, Telegram, Twitter lan truyền tin đồn (Bơm - Pump) giá đồng Coin Vốn hóa thấp.
        \item Khi người chơi nhỏ lẻ FOMO đu đỉnh $\Rightarrow$ Chúng xả hàng (Dump) và rời đi.
    \end{itemize}
\end{frame}

\begin{frame}{Học máy rà quét Telegram \& Discord}
    \begin{itemize}
        \item Khối lượng tin nhắn lùa gà và giao dịch trên Blockchain là quá lớn đối với con người.
        \item AI (Machine Learning) phải rà quét ngôn ngữ theo thời gian thực kết hợp xem xét dòng tiền on-chain để phát hiện các \textbf{cụm thông tin bất thường}.
        \item $\Rightarrow$ Dùng thuật toán để chống lại sự thao túng của thuật toán khác!
    \end{itemize}
\end{frame}

\begin{frame}{Cuộc chiến Chống độc quyền (Antitrust) trong kỷ nguyên AI}
    Vậy ai là người nắm giữ những siêu thuật toán mạnh mẽ nhất để thao túng thị trường?
    \vspace{0.2cm}
    $\Rightarrow$ \textbf{Các tập đoàn công nghệ khổng lồ (Big Tech).}
\end{frame}

\begin{frame}{Người gác cổng (Gatekeepers)}
    \begin{itemize}
        \item Big Tech không cạnh tranh trong một thị trường có sẵn. Họ cạnh tranh để \textbf{sở hữu toàn bộ thị trường đó} và làm "Người gác cổng".
        \item \textbf{Hiệu ứng mạng (Network Effects):} Càng nhiều người dùng $\rightarrow$ AI học được nhiều dữ liệu $\rightarrow$ AI thông minh hơn $\rightarrow$ Dịch vụ tốt hơn $\rightarrow$ Thu hút thêm người dùng $\rightarrow$ Vòng lặp khép kín.
    \end{itemize}
\end{frame}

\begin{frame}{Sáp nhập Tiêu diệt (Killer Acquisitions)}
    Các Big Tech không để startup khởi nghiệp vươn lên thành đối thủ. Họ thâu tóm ngay từ trong trứng nước!
    \begin{exampleblock}{Ẩn dụ: Đội bóng Siêu giàu}
        Giống hệt như một đội bóng nhà giàu vung tiền mua tiền đạo xuất sắc nhất của đội đối thủ. Họ mua về \textbf{không phải để đá}, mà để \textbf{cất anh ta trên băng ghế dự bị mãi mãi}, đảm bảo đội bạn không có người sút tung lưới mình.
    \end{exampleblock}
\end{frame}

\begin{frame}{Vỏ bọc "Quyền riêng tư" (Vụ kiện LinkedIn)}
    \begin{itemize}
        \item Để lách luật chống độc quyền, các tập đoàn dùng cờ hiệu "Bảo vệ Quyền riêng tư" làm bình phong.
        \item \textbf{Vụ hiQ Labs kiện LinkedIn:} LinkedIn chặn hiQ thu thập dữ liệu hồ sơ công khai với lý do "Bảo vệ người dùng". 
        \item Sự thật bị cáo buộc: LinkedIn chặn để tự mình độc quyền mảng dịch vụ phân tích dữ liệu tuyển dụng.
    \end{itemize}
\end{frame}

\begin{frame}{Cái bẫy "Phúc lợi Người tiêu dùng"}
    \begin{itemize}
        \item Tòa án Tối cao Hoa Kỳ (nhiều thập kỷ qua) thường sử dụng thước đo \textbf{Phúc lợi Người tiêu dùng (Consumer Welfare)} để đánh giá Độc quyền. 
        \item Lập luận: Nếu giá dịch vụ không tăng (thậm chí Facebook, Google là MIỄN PHÍ), thì không có thiệt hại cho người dùng.
    \end{itemize}
\end{frame}

\begin{frame}{Khi Khách hàng chính là Sản phẩm}
    \begin{alertblock}{Lỗ hổng của Pháp luật}
        Dịch vụ miễn phí để đổi lấy dữ liệu! Sự dễ dãi này cho phép Big Tech tự do thiết kế lại cấu trúc thị trường. Khách hàng không mua sản phẩm, \textbf{khách hàng chính là sản phẩm}.
    \end{alertblock}
\end{frame}

\begin{frame}{Quyền được sửa chữa (Right to Repair)}
    \begin{itemize}
        \item Phong trào đòi quyền tự sửa chữa thiết bị chống lại thiết kế "phần cứng đóng" của Apple, John Deere...
        \item Đòi hỏi một luật pháp Ex-ante (quy định tiêu chuẩn công bằng từ đầu) thay vì Ex-post (chạy theo giải quyết hậu quả khi thị trường đã bị bóp méo).
    \end{itemize}
\end{frame}

\begin{frame}{Suy ngẫm Tương lai: Thẩm phán Máy móc}
    \textbf{Trí tuệ Nhân tạo Bậc cao (AGI):}
    \begin{itemize}
        \item Nếu AI tiến hóa thành \textbf{Thẩm phán Máy móc} - một thực thể diễn giải luật pháp tuyệt đối khách quan, không bị chi phối bởi lợi ích chính trị, tự động trừng phạt các siêu tập đoàn ngay khi có hành vi thao túng.
        \item \textbf{Câu hỏi lớn:} Khi máy móc trở thành luật sư và thẩm phán cho chính những cỗ máy khác, vai trò của những Chuyên gia Kế toán/Kiểm toán (Con người) sẽ nằm ở đâu?
    \end{itemize}
\end{frame}

\begin{frame}{Tổng kết bài học}
    \begin{enumerate}
        \item \textbf{TMĐT:} AI dùng Random Forest chặn Click ảo, dùng Baseline (Baseline) chống trộm Thẻ tín dụng, và OCR+NLP để lật tẩy Hóa đơn giả.
        \item \textbf{Tài chính:} Algorithmic Trading mang lại tốc độ nhưng là nguyên nhân của những đợt Flash Crash thảm họa.
        \item \textbf{Độc quyền:} Big Tech đang xây pháo đài dữ liệu khép kín thông qua Network Effects và Killer Acquisitions, dùng quyền riêng tư làm bình phong.
    \end{enumerate}
\end{frame}

\begin{frame}
    \centering
    \Huge \textbf{Cảm ơn các bạn đã lắng nghe!}
    
    \vspace{0.5cm}
    \Large Hỏi \& Đáp
\end{frame}

\end{document}
"""
    output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "Slide_AIAcc_Day08.tex")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
        
    print(f"Generated {file_path}")

if __name__ == "__main__":
    create_beamer_slide()
