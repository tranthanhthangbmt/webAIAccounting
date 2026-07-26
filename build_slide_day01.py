# -*- coding: utf-8 -*-
"""
Script tự động sinh file LaTeX Slide_AIAcc_Day01.tex cho Buổi 1:
"Những điều Kế toán viên cần biết về AI" (48 slides, 3 tiết / 135 phút)
Tích hợp trọn vẹn Figure 1.1 và Figure 1.2 từ thư mục Figures/Buoi_01/.
"""

import os

def build_tex():
    tex_dir = "TaiLieu/slideAIAcc"
    os.makedirs(tex_dir, exist_ok=True)
    tex_path = os.path.join(tex_dir, "Slide_AIAcc_Day01.tex")

    header = r"""\documentclass{article}
\usepackage[T5]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{fleqn}
\usepackage{color}
\usepackage{graphicx}
\usepackage{aima-accounting-slides}

% Custom macros & dimensions for slide deck
\renewcommand{\heading}[1]{\clearpage\noindent\fbox{\fbox{\parbox[c]{\headingwidth}{\centering \rule[-0.5\fboxsep]{0em}{1em}\headingfont #1\vspace{0.2em}}}}\par\medskip}
\renewcommand{\thefigure}{1.\arabic{figure}}

\begin{document}

\begin{LARGE}

% SLIDE 01: TRANG BÌA
\titleslide{Trí tuệ Nhân tạo cho Kế toán}{Buổi 1: Những điều Kế toán viên cần biết về AI}

\sf

% SLIDE 02: NỘI DUNG CHƯƠNG TRÌNH
\heading{Nội dung Chương trình Buổi học (135 Phút)}

\blob \textbf{Tiết 1 (45 Phút): Khái quát về AI \& Lịch sử Chuyển đổi số Kế toán}
\subbull 1.1 Cuộc cách mạng AI trong nghề Kế toán - Kiểm toán
\subbull 1.2 Trí tuệ Nhân tạo (AI) là gì?
\subbull 1.3 - 1.4 Trí tuệ Con người vs. Trí tuệ Nhân tạo
\subbull 1.5 - 1.6 Lịch sử của AI (1950 - Nay) \& Các Mùa đông AI
\subbull 1.7 - 1.10 Lịch sử Kế toán ứng dụng Công nghệ \& Thực trạng hiện nay

\blob \textbf{Tiết 2 (45 Phút): Hệ sinh thái AI Cốt lõi \& Học máy trong Tài chính}
\subbull 2.1 - 2.3 Phân loại AI: Trí tuệ Nhân tạo Hẹp (ANI) vs. Tổng quát (AGI)
\subbull 2.4 - 2.6 Lập luận máy \& Hệ chuyên gia trong Tuân thủ Thuế
\subbull 2.7 - 2.9 Học máy (Machine Learning) \& Phân tích Sơ đồ Figure 1.1
\subbull 2.10 - 2.16 4 Mô hình Học máy trong Kế toán (Supervised, Unsupervised, Semi, RL)
\subbull 2.17 Học sâu (Deep Learning - DL)

\blob \textbf{Tiết 3 (45 Phút): NLP, Khai phá Dữ liệu, RPA, API \& Công cụ Lập trình}
\subbull 3.1 - 3.3 Ứng dụng DL OCR \& Xử lý Ngôn ngữ Tự nhiên (NLP)
\subbull 3.4 - 3.7 Khai phá Dữ liệu (Data Mining), Text Mining \& Figure 1.2
\subbull 3.8 - 3.10 Tự động hóa Quy trình bằng Robot (RPA) \& AI-RPA
\subbull 3.11 - 3.12 Giao diện Lập trình Ứng dụng (API) trong Kế toán Mở
\subbull 3.13 - 3.15 Các Ngôn ngữ Lập trình (Python, R, SQL) \& Lộ trình Kỹ năng

% SLIDE 03: MỤC TIÊU BÀI HỌC
\heading{Mục tiêu Bài học (Lesson Objectives - LO)}

\blob \textbf{LO 1.1 - Hiểu bản chất AI:} Nắm vững khái niệm Trí tuệ Nhân tạo trong tài chính, phân biệt rạch ròi giữa Trí tuệ con người, AI hẹp (ANI) và AI tổng quát (AGI).

\blob \textbf{LO 1.2 - Lịch sử \& Tiến hóa:} Hiểu hành trình phát triển của AI và 5 giai đoạn tiến hóa công nghệ của nghề Kế toán - Kiểm toán (từ bàn tính, Excel, ERP, Cloud đến AI).

\blob \textbf{LO 1.3 - Làm chủ Học máy \& Học sâu:} Giải thích được cơ chế hoạt động và ứng dụng tài chính của Học có giám sát, Học không giám sát, Học bán giám sát, Học tăng cường và Mạng nơ-ron Học sâu.

\blob \textbf{LO 1.4 - Tích hợp Hệ sinh thái Tự động hóa:} Phân tích sự kết hợp hiệu quả giữa Khai phá dữ liệu (Data Mining), NLP, RPA và API trong quy trình kế toán tự động hóa hiện đại.

\blob \textbf{LO 1.5 - Định hướng Công cụ \& Ngôn ngữ:} Hiểu lý do vì sao Python là "ngôn ngữ chung" của Kế toán viên kỷ nguyên số và xây dựng lộ trình nâng cấp năng lực bản thân.

% SLIDE 04
\heading{1.1 Cuộc cách mạng AI trong nghề Kế toán}

\blob \textbf{Bối cảnh Kinh tế Số:} Dữ liệu tài chính không còn là những con số tĩnh trên sổ sách, mà đã trở thành "tài sản chiến lược" lớn nhất của doanh nghiệp.

\blob \textbf{Sự bùng nổ Dữ liệu Phi cấu trúc:} Hơn 80\% dữ liệu doanh nghiệp hiện nay là phi cấu trúc (hợp đồng kinh tế, hóa đơn scan, email, âm thanh, hình ảnh).
\subbull Phương pháp kế toán thủ công không thể xử lý khối lượng dữ liệu khổng lồ này.

\blob \textbf{Yêu cầu Chuyển dịch Vai trò:} Kế toán viên đang bước qua giai đoạn từ "người ghi chép lịch sử" (Bookkeeper) sang "nhà phân tích và cố vấn chiến lược" (Strategic Business Advisor).
\subbull AI chính là đòn bẩy công nghệ cốt lõi thúc đẩy bước chuyển dịch lịch sử này.

% SLIDE 05
\heading{1.2 Trí tuệ Nhân tạo (AI) là gì?}

\blob \textbf{Định nghĩa phổ quát:} Trí tuệ Nhân tạo (Artificial Intelligence) là khả năng của máy móc hoặc phần mềm thực hiện các tác vụ đòi hỏi nhận thức và suy luận tương tự con người.

\blob \textbf{Góc nhìn Tài chính - Kế toán:} AI không phải là "phép thuật thần kỳ", mà bản chất là sự kết hợp của toán học, thống kê nâng cao và năng lực xử lý máy tính trên tập dữ liệu lớn.

\blob \textbf{3 Trụ cột cốt lõi của AI hiện đại:}
\subbull \textbf{1. Dữ liệu (Data):} Hàng triệu chứng từ kế toán, sổ nhật ký, lịch sử giao dịch.
\subbull \textbf{2. Thuật toán (Algorithms):} Mô hình toán học học hỏi từ dữ liệu để dự báo.
\subbull \textbf{3. Sức mạnh Điện toán (Computing Power):} Điện toán đám mây và vi xử lý GPU/TPU tốc độ cao.

% SLIDE 06
\heading{1.3 Trí tuệ Con người vs. Trí tuệ Nhân tạo (P1)}

\blob \textbf{Trí tuệ Con người (Human Intelligence):}
\subbull Sở hữu \textbf{trực giác nghề nghiệp}, năng lực đánh giá đạo đức và sự thấu hiểu bối cảnh kinh doanh.
\subbull Có khả năng giải quyết các tình huống "Thiên nga đen" (Black Swan) chưa từng có tiền lệ trong lịch sử số liệu.
\subbull Bị giới hạn bởi sinh học: Tốc độ tính toán chậm, dễ mệt mỏi, dễ sai sót khi lặp lại.

\blob \textbf{Trí tuệ Nhân tạo (Artificial Intelligence):}
\subbull Khả năng tính toán siêu tốc, xử lý hàng triệu hóa đơn chỉ trong vài giây với độ chính xác cao.
\subbull Hoạt động liên tục 24/7/365, không mệt mỏi, không bị ảnh hưởng bởi tâm lý hay cảm xúc.
\subbull Thiếu "ý thức" và "sự phán đoán đạo đức", hoàn toàn phụ thuộc vào chất lượng dữ liệu huấn luyện.

% SLIDE 07
\heading{1.4 Trí tuệ Con người vs. Trí tuệ Nhân tạo (P2)}

\blob \textbf{Bảng đối chiếu Vùng Năng lực trong Kế toán - Kiểm toán:}
\subbull \textbf{AI Vượt trội:} Đối chiếu công nợ nghìn dòng, phát hiện giao dịch bất thường thống kê, nhận diện dữ liệu hóa đơn (OCR), dự báo dòng tiền theo mô hình học máy.
\subbull \textbf{Con người Vượt trội:} Xét đoán kế toán (Accounting Estimates), giải thích sai lệch ngân sách cho HĐQT, thẩm định đạo đức chuẩn mực IFRS, thương thảo hợp đồng.

\blob \textbf{Kết luận Sư phạm:} AI và Con người là mối quan hệ \textbf{bổ trợ (Augmentation)}, không phải đối đầu. Máy móc xử lý dữ liệu quy mô lớn, Kế toán viên tập trung ra quyết định chiến lược.

% SLIDE 08
\heading{1.5 Lịch sử của Trí tuệ Nhân tạo (1950 - Nay)}

\blob \textbf{1950 - Phép thử Turing (Alan Turing):} Đặt nền móng triết học "Liệu máy móc có thể suy nghĩ?" qua bài kiểm tra khả năng giả lập giao tiếp con người.

\blob \textbf{1956 - Hội nghị Dartmouth:} Thuật ngữ "Artificial Intelligence" (Trí tuệ Nhân tạo) chính thức ra đời bởi John McCarthy và các nhà khoa học tiên phong.

\blob \textbf{1970 - 1980 - Kỷ nguyên Hệ chuyên gia (Expert Systems):} AI phát triển dựa trên luật suy diễn logic (Rule-based), ứng dụng đầu tiên trong chẩn đoán y khoa và thuế.

\blob \textbf{2010 - Hiện nay - Kỷ nguyên Học sâu \& Generative AI:} Sự bùng nổ của Mạng nơ-ron nhiều lớp (Deep Learning), Big Data và mô hình ngôn ngữ lớn (ChatGPT, Claude) làm thay đổi toàn diện ngành tài chính.

% SLIDE 09
\heading{1.6 Các "Mùa đông AI" \& Bài học Công nghệ}

\blob \textbf{Khái niệm "Mùa đông AI" (AI Winters):} Là những giai đoạn (khủng hoảng 1974-1980 và 1987-1993) khi sự ủng hộ và nguồn vốn nghiên cứu AI sụt giảm mạnh do không đạt được kỳ vọng thổi phồng.

\blob \textbf{Nguyên nhân trong quá khứ:}
\subbull Phần cứng máy tính quá yếu, bộ nhớ hạn chế.
\subbull Thiếu nguồn dữ liệu số hóa đủ lớn để huấn luyện mô hình.
\subbull Thuật toán lý thuyết chưa giải quyết được bài toán phi tuyến tính phức tạp.

\blob \textbf{Vì sao AI hiện đại không còn "Mùa đông"?:}
\subbull Dữ liệu kế toán - tài chính đã số hóa 100\% (Cloud ERP, e-Invoice).
\subbull Năng lực tính toán vi xử lý tăng cấp số nhân (Định luật Moore \& GPU computing).

% SLIDE 10
\heading{1.7 Lịch sử Kế toán ứng dụng Công nghệ (P1)}

\blob \textbf{Giai đoạn 1: Kỷ nguyên Thủ công \& Cơ học (Trước năm 1960)}
\subbull Công cụ chủ đạo: Bàn tính (Abacus), Sổ sách kế toán giấy (Paper Ledgers).
\subbull Đặc điểm: Tốc độ xử lý rất chậm, rủi ro sai sót tính toán thủ công cao, khó đối chiếu.

\blob \textbf{Giai đoạn 2: Kỷ nguyên Máy tính Mainframe \& Bảng tính Điện tử (1960 - 1980)}
\subbull Sự xuất hiện của phần mềm bảng tính ban đầu: VisiCalc (1979) và Lotus 1-2-3.
\subbull Bước ngoặt lịch sử: \textbf{Microsoft Excel (1985)} ra đời, chuẩn hóa hoàn toàn công việc tính toán, bảng cân đối kế toán và tự động hóa công thức trên máy tính cá nhân.

% SLIDE 11
\heading{1.8 Lịch sử Kế toán ứng dụng Công nghệ (P2)}

\blob \textbf{Giai đoạn 3: Kỷ nguyên Quản trị Nguồn lực Doanh nghiệp - ERP (1990 - 2000)}
\subbull Các hệ thống ERP lớn (SAP, Oracle) kết nối liên thông dữ liệu giữa Phân hệ Bán hàng, Mua hàng, Kho hàng, Tài sản cố định và Sổ cái (General Ledger).
\subbull Chấm dứt tình trạng "ốc đảo dữ liệu" (Data Silos) trong phòng Kế toán.

\blob \textbf{Giai đoạn 4: Kỷ nguyên Điện toán Đám mây \& RPA (2000 - 2015)}
\subbull Kế toán trên mây (Cloud Accounting: Xero, QuickBooks Online) cho phép truy cập tài chính mọi lúc mọi nơi.
\subbull Tự động hóa Quy trình bằng Robot (RPA) bắt đầu thay thế việc copy-paste thủ công.

% SLIDE 12
\heading{1.9 Kỷ nguyên Trí tuệ Nhân tạo trong Kế toán}

\blob \textbf{Giai đoạn 5: Kỷ nguyên AI \& Kiểm toán Liên tục (2015 - Hiện nay)}
\subbull AI được tích hợp sâu vào cốt lõi các phần mềm kế toán và hệ thống quản trị tài chính doanh nghiệp.

\blob \textbf{Sự chuyển dịch Mô hình Kiểm soát Tài chính:}
\subbull \textbf{Trước đây:} Kiểm toán định kỳ (Periodic Auditing - Hậu kiểm sau tháng/quý/năm).
\subbull \textbf{Hiện nay:} Kiểm toán liên tục (Continuous Auditing - Kiểm soát theo thời gian thực 24/7 nhờ thuật toán AI giám sát mọi bút toán).

\blob \textbf{Báo cáo Tài chính Động:} Xuất báo cáo tài chính ngay tại thời điểm yêu cầu với năng lực dự báo dòng tiền tương lai có xác suất cao.

% SLIDE 13
\heading{1.10 Thực trạng Kế toán viên sử dụng AI}

\blob \textbf{Số liệu Thực tiễn từ Khảo sát Big4 \& AICPA:}
\subbull Hơn 70\% doanh nghiệp kiểm toán lớn đã và đang triển khai các hệ thống AI trong kiểm tra hóa đơn và đánh giá rủi ro tín dụng.
\subbull Việc áp dụng AI giúp tiết kiệm trung bình 40\% - 60\% thời gian xử lý hồ sơ chứng từ.

\blob \textbf{3 Tác vụ AI đã trở thành Tiêu chuẩn ngành Kế toán:}
\subbull \textbf{1. Tự động xử lý Hóa đơn Điện tử (e-Invoice Processing):} Bóc tách dữ liệu không cần gõ phím.
\subbull \textbf{2. Đối chiếu Ngân hàng Tự động (Automated Reconciliation):} Khớp lệnh nghìn giao dịch trong vài giây.
\subbull \textbf{3. Phân tích Chi phí \& Phát hiện Ngoại lệ:} Cảnh báo các khoản chi sai định mức ngay lập tức.

% SLIDE 14
\heading{1.11 Thảo luận: AI có thay thế Kế toán viên?}

\blob \textbf{Câu hỏi Kinh điển:} "Liệu nghề Kế toán - Kiểm toán có biến mất trong tương lai vì sự phát triển của Trí tuệ Nhân tạo?"

\blob \textbf{Phân tích của Chuyên gia Tài chính:}
\subbull AI chỉ thay thế các \textbf{tác vụ lặp đi lặp lại} (Bookkeeping, nhập liệu, đối chiếu cơ bản).
\subbull AI KHÔNG THỂ thay thế tư duy xét đoán chuyên môn, trách nhiệm đạo đức giải trình và năng lực tư vấn chiến lược cho Giám đốc Tài chính (CFO).

\blob \textbf{Khẩu hiệu Hành động của Môn học:}
\subbull \emph{"AI sẽ không thay thế Kế toán viên, nhưng Kế toán viên biết làm chủ AI chắc chắn sẽ thay thế Kế toán viên truyền thống!"}

% SLIDE 15
\heading{2.1 Phân loại Trí tuệ Nhân tạo: ANI vs. AGI}

\blob \textbf{2 Cấp độ Nhận thức và Độ rộng Tác vụ của AI:}
\subbull \textbf{1. Trí tuệ Nhân tạo Hẹp (ANI - Artificial Narrow Intelligence):} AI được lập trình và huấn luyện chuyên biệt để làm tốt MỘT tác vụ duy nhất.
\subbull \textbf{2. Trí tuệ Nhân tạo Tổng quát (AGI - Artificial General Intelligence):} AI có khả năng nhận thức, tự suy luận và làm được mọi tác vụ trí tuệ như con người.

\blob \textbf{Trạng thái Ứng dụng Tài chính hiện tại:}
\subbull 100\% các hệ thống AI đang áp dụng trong ngành Kế toán - Kiểm toán - Ngân hàng ngày nay đều thuộc phân lớp \textbf{ANI (AI Hẹp)}.

% SLIDE 16
\heading{2.2 Trí tuệ Nhân tạo Hẹp (ANI) trong Kế toán}

\blob \textbf{Bản chất của ANI:} Siêu việt trong phạm vi nhỏ, nhưng hoàn toàn "mù tịt" nếu đưa ra khỏi lĩnh vực được huấn luyện.
\subbull Ví dụ: Mô hình AI đánh giá rủi ro tín dụng rất xuất sắc, nhưng không thể dùng mô hình đó để... đọc hiểu hợp đồng thuê tài sản.

\blob \textbf{3 Ví dụ ANI tiêu biểu trong ngành Kế toán:}
\subbull \textbf{1. AI-OCR:} Nhận diện ký tự và con số từ ảnh chụp hóa đơn GTGT.
\subbull \textbf{2. Credit Risk Scoring:} Thuật toán chấm điểm tín dụng khách hàng dựa trên lịch sử thanh toán.
\subbull \textbf{3. Chatbot Kế toán:} Trả lời tự động các quy định về Chuẩn mực IFRS 15 / IFRS 16.

% SLIDE 17
\heading{2.3 Trí tuệ Nhân tạo Tổng quát (AGI) \& Thách thức}

\blob \textbf{Tầm nhìn AGI trong tương lai:} Một "Kiểm toán viên máy móc" toàn năng có thể tự động đi tham quan nhà máy, nói chuyện với Giám đốc, phân tích sổ sách và tự đưa ra ý kiến kiểm toán.

\blob \textbf{Thách thức lớn về Đạo đức \& Kiểm soát (Value Alignment):}
\subbull Làm thế nào để đảm bảo AGI tuân thủ tuyệt đối Đạo đức Nghề nghiệp Kế toán (IFAC / AICPA)?
\subbull Ai sẽ là người chịu trách nhiệm pháp lý nếu AGI đưa ra quyết định sai sót gây thiệt hại hàng nghìn tỷ đồng?
\subbull Kế toán viên cần tham gia vào quá trình thiết kế ranh giới đạo đức cho AI ngay từ bây giờ.

% SLIDE 18
\heading{2.4 Lập luận máy (Machine Reasoning)}

\blob \textbf{Khái niệm Lập luận máy:} Là hệ thống AI biểu diễn tri thức dưới dạng các cấu trúc logic và sử dụng các thuật toán suy diễn để rút ra kết luận mới từ cơ sở dữ liệu hiện có.

\blob \textbf{2 Cơ chế Suy diễn cốt lõi trong Tài chính:}
\subbull \textbf{1. Liên kết Thuận (Forward Chaining):} Đi từ các sự kiện dữ liệu hiện có -> Áp dụng các luật kế toán -> Suy ra kết luận hạch toán cuối cùng.
\subbull \textbf{2. Liên kết Ngược (Backward Chaining):} Đi từ một giả thuyết kiểm toán (Ví dụ: "Hóa đơn này vi phạm luật thuế") -> Truy xuất ngược lại tìm dữ kiện chứng minh.

% SLIDE 19
\heading{2.5 Hệ chuyên gia (Expert Systems)}

\blob \textbf{Định nghĩa:} Hệ chuyên gia là một dạng AI sớm nhất và thành công nhất trong Kế toán, hoạt động bằng cách mô phỏng khả năng ra quyết định của một chuyên gia con người.

\blob \textbf{Cấu trúc 2 Thành phần Không thể tách rời:}
\subbull \textbf{1. Cơ sở Tri thức (Knowledge Base):} Tập hợp các chuẩn mực kế toán (VAS/IFRS), quy định Luật Thuế, chính sách tài chính được mã hóa dưới dạng \texttt{IF ... THEN ...}.
\subbull \textbf{2. Động cơ Suy diễn (Inference Engine):} Thuật toán quét số liệu chứng từ thực tế và áp dụng luật từ Cơ sở Tri thức để đưa ra chỉ dẫn.

% SLIDE 20
\heading{2.6 Ứng dụng Hệ chuyên gia trong Thuế \& Tuân thủ}

\blob \textbf{Case Study: Hệ thống Kiểm tra Chi phí Được trừ Thuế TNDN}

\blob \textbf{Chuỗi luật logic \texttt{IF - THEN} được mã hóa trong Hệ chuyên gia:}
\subbull \texttt{IF} Hóa đơn có đầy đủ thông tin hợp lệ \texttt{AND} Không nằm trong danh sách doanh nghiệp bỏ trốn...
\subbull \texttt{AND IF} Giá trị hóa đơn $\ge 20$ triệu VNĐ \texttt{THEN} Kiểm tra chứng từ thanh toán không dùng tiền mặt.
\subbull \texttt{IF} Có ủy nhiệm chi hợp lệ \texttt{THEN} Phê duyệt khoản chi phí được trừ.

\blob \textbf{Ưu điểm vượt trội:} Minh bạch tuyệt đối 100\%, có thể giải trình mọi bước suy diễn cho Đoàn thanh tra Thuế mà không bị "hộp đen" (Black Box).

% SLIDE 21
\heading{2.7 Học máy (Machine Learning - ML)}

\blob \textbf{Định nghĩa của Arthur Samuel (1959):} Học máy là lĩnh vực của Trí tuệ Nhân tạo cung cấp cho máy tính khả năng tự học hỏi từ dữ liệu mà không cần phải được lập trình tường minh từng quy tắc.

\blob \textbf{Sự khác biệt mang tính Cách mạng:}
\subbull \textbf{Lập trình Kế toán Truyền thống:} Con người nạp \texttt{[Dữ liệu Sổ sách]} + \texttt{[Quy tắc/Luật Hạch toán]} vào máy -> Máy tính ra \texttt{[Kết quả Báo cáo]}.
\subbull \textbf{Học máy (Machine Learning):} Con người nạp \texttt{[Dữ liệu Sổ sách]} + \texttt{[Kết quả/Nhãn Thực tế]} vào máy -> Máy tự học và tạo ra \texttt{[Quy luật Thuật toán]}.

% SLIDE 22
\heading{2.8 Sơ đồ Mối quan hệ: AI - ML - DL}

\begin{center}
\includegraphics[width=0.75\textwidth]{{../../Figures/Buoi_01/Figure 1.1 Relationship between AI, ML, and DL..PNG}}
\par\medskip
\textbf{Figure 1.1:} Mối quan hệ bao hàm giữa Trí tuệ Nhân tạo (AI), Học máy (ML) và Học sâu (DL).
\end{center}

% SLIDE 23
\heading{2.9 Phân tích Biểu đồ Figure 1.1}

\blob \textbf{Diễn giải Sơ đồ Euler dưới góc độ Kế toán - Kiểm toán:}
\subbull \textbf{1. Trí tuệ Nhân tạo (AI - Vòng lớn ngoài cùng):} Là toàn bộ lĩnh vực khoa học rộng lớn bao gồm mọi kỹ thuật giúp máy thông minh (bao gồm Hệ chuyên gia, RPA, Học máy).
\subbull \textbf{2. Học máy (ML - Vòng giữa):} Là một tập con thuộc AI, sử dụng các thuật toán thống kê tự học quy luật từ dữ liệu kế toán lịch sử.
\subbull \textbf{3. Học sâu (Deep Learning - DL - Vòng trong cùng):} Là một tập con thuộc ML, sử dụng Mạng nơ-ron nhân tạo đa tầng để xử lý dữ liệu phức tạp phi cấu trúc.
\subbull \emph{Quy tắc vàng: "Mọi Học sâu đều là Học máy, và mọi Học máy đều là Trí tuệ nhân tạo, nhưng điều ngược lại thì không đúng!"}

% SLIDE 24
\heading{2.10 Học có giám sát (Supervised Learning - P1)}

\blob \textbf{Cơ chế hoạt động:} Mô hình được huấn luyện trên tập dữ liệu đã có nhãn đích rõ ràng (Labeled Data). Kế toán viên đóng vai trò "người thầy" chỉ cho máy biết câu trả lời đúng.

\blob \textbf{2 Bài toán cốt lõi của Học có giám sát:}
\subbull \textbf{1. Bài toán Phân lớp (Classification):} Dự báo nhãn rời rạc theo từng nhóm (Ví dụ: `Gian lận` / `Hợp lệ` ; `Vỡ nợ` / `An toàn`).
\subbull \textbf{2. Bài toán Hồi quy (Regression):} Dự báo một giá trị số liên tục (Ví dụ: Dự báo Doanh thu quý tới là `150.5 Tỷ VNĐ`).

% SLIDE 25
\heading{2.11 Học có giám sát trong Kế toán (P2)}

\blob \textbf{Ứng dụng 1: Phát hiện Gian lận Hóa đơn (Fraud Detection)}
\subbull Huấn luyện mô hình trên 50,000 hóa đơn lịch sử (đã được Kiểm toán viên gán nhãn: `0 = Hợp lệ`, `1 = Gian lận`).
\subbull Khi hóa đơn mới xuất hiện, mô hình tự động chấm điểm xác suất gian lận để cảnh báo phòng Kế toán.

\blob \textbf{Ứng dụng 2: Chấm điểm Tín dụng Khách hàng (Credit Scoring)}
\subbull Dựa trên các chỉ số tài chính (hệ số thanh toán, lịch sử trả nợ), phân loại khách hàng có nợ phải thu vào nhóm `Rủi ro cao`, `Rủi ro trung bình`, hay `Rủi ro thấp`.

% SLIDE 26
\heading{2.12 Học không giám sát (Unsupervised - P1)}

\blob \textbf{Cơ chế hoạt động:} Thuật toán làm việc với tập dữ liệu hoàn toàn KHÔNG CÓ NHÃN (Unlabeled Data). Máy tính tự tìm kiếm mô hình, cấu trúc và sự tương đồng ngầm trong dữ liệu.

\blob \textbf{2 Kỹ thuật chủ đạo trong Phân tích Tài chính:}
\subbull \textbf{1. Phân cụm (Clustering - K-Means, DBSCAN):} Gom nhóm các giao dịch hoặc đối tượng tài chính có hành vi tương tự nhau.
\subbull \textbf{2. Giảm số chiều (Dimensionality Reduction - PCA):} Đơn giản hóa hàng trăm biến số tài chính xuống còn vài nhân tố chính mà không mất thông tin.

% SLIDE 27
\heading{2.13 Học không giám sát trong Kiểm toán (P2)}

\blob \textbf{Ứng dụng Đột phá: Phát hiện Giao dịch Bất thường (Anomaly Detection)}
\subbull Kiểm toán viên không thể biết trước hình thái của mọi hành vi gian lận mới.
\subbull Thuật toán Học không giám sát tự động phân cụm hàng triệu bút toán trong Sổ Nhật ký chung (General Ledger) và lập tức khoanh vùng các giao dịch "lạc loài" (Outliers):
\subbull \textbf{Ví dụ 1:} Bút toán chuyển tiền phát sinh lúc 3:00 sáng ngày Chủ Nhật.
\subbull \textbf{Ví dụ 2:} Hàng loạt giao dịch mua thiết bị có giá trị \texttt{19,990,000 VNĐ} (né ngưỡng phê duyệt 20 triệu).

% SLIDE 28
\heading{2.14 Học bán giám sát (Semi-supervised Learning)}

\blob \textbf{Bài toán Thực tế của Kế toán viên:}
\subbull Doanh nghiệp có 1,000,000 hóa đơn mỗi năm, nhưng Kế toán viên chỉ có đủ thời gian kiểm tra chi tiết và gán nhãn cho 50,000 hóa đơn (5\% dũ liệu).
\subbull 95\% dữ liệu còn lại là dữ liệu không nhãn.

\blob \textbf{Giải pháp Học bán giám sát:}
\subbull Mô hình học từ 5\% dữ liệu có nhãn để hiểu quy luật, sau đó lan truyền nhận thức sang 95\% dữ liệu không nhãn.
\subbull Tiết kiệm đến 80\% chi phí và công sức kiểm toán thủ công nhưng vẫn đạt độ chính xác rất cao.

% SLIDE 29
\heading{2.15 Học tăng cường (Reinforcement Learning - P1)}

\blob \textbf{Cơ chế hoạt động:} Tác nhân AI (Agent) tự học thông qua quá trình \textbf{Thử \& Sai (Trial and Error)} trong một môi trường động tương tự như chơi một trò chơi tài chính.

\blob \textbf{Hệ thống Phần thưởng \& Hình phạt (Reward System):}
\subbull Nếu quyết định tài chính đem lại lợi nhuận/giảm rủi ro -> Máy được nhận phần thưởng (+).
\subbull Nếu quyết định dẫn đến lỗ hoặc vi phạm ràng buộc -> Máy bị hình phạt (-).
\subbull Thuật toán tự động tối ưu hóa chiến lược hành động để đạt tổng phần thưởng kỳ vọng lớn nhất sau hàng triệu kịch bản mô phỏng.

% SLIDE 30
\heading{2.16 Học tăng cường trong Tài chính (P2)}

\blob \textbf{Ứng dụng 1 - Quản trị Dòng tiền Động (Dynamic Cash Management):}
\subbull Tác nhân RL tự động cân đối lượng tiền mặt giữ lại tại quỹ và số tiền đem gửi tiết kiệm ngắn hạn dựa trên biến động lãi suất hằng ngày.

\blob \textbf{Ứng dụng 2 - Chiến lược Định giá Động (Dynamic Pricing):}
\subbull Tự động điều chỉnh giá bán sản phẩm theo thời gian thực dựa trên nhu cầu thị trường, lượng hàng tồn kho và giá đối thủ, nhằm tối đa hóa biên lợi nhuận gộp.

% SLIDE 31
\heading{2.17 Học sâu (Deep Learning - DL)}

\blob \textbf{Cấu trúc Mạng Thần kinh Nhân tạo Đa tầng (Deep Neural Networks - DNN):}
\subbull Gồm các lớp Nơ-ron đầu vào (Input Layer), nhiều lớp ẩn (Hidden Layers) và lớp đầu ra (Output Layer).

\blob \textbf{Năng lực vượt trội với Dữ liệu Phi cấu trúc:}
\subbull Không cần con người làm bước "trích xuất đặc trưng thủ công" (Feature Engineering).
\subbull DL tự động nhận biết đường nét, chữ viết, ký hiệu trên hóa đơn chụp bị mờ, nghiêng, hoặc file ghi âm cuộc họp hội đồng quản trị.

% SLIDE 32
\heading{3.1 Ứng dụng DL: Tự động hóa Chứng từ (OCR + AI)}

\blob \textbf{Bước tiến từ OCR Truyền thống sang IDP (Intelligent Document Processing):}
\subbull OCR truyền thống chỉ chụp ảnh và đoán ký tự, dễ sai khi hóa đơn thay đổi biểu mẫu.
\subbull IDP ứng dụng Học sâu (Deep Learning) để \textbf{hiểu ngữ cảnh}: Biết đâu là Tên người bán, đâu là Mã số thuế, đâu là Tổng tiền VAT dù biểu mẫu mới gặp lần đầu.

\blob \textbf{Quy trình Hạch toán Tự động hoàn toàn:}
\subbull \texttt{[Ảnh Hóa đơn PDF]} -> \texttt{[DL-OCR trích xuất]} -> \texttt{[ML đối chiếu Đơn hàng PO]} -> \texttt{[Tự động tạo Bút toán trên Sổ cái]}.

% SLIDE 33
\heading{3.2 Xử lý Ngôn ngữ Tự nhiên (NLP - P1)}

\blob \textbf{Khái niệm NLP (Natural Language Processing):}
\subbull Là nhánh của AI chuyên giúp máy tính hiểu, diễn giải và sinh ra ngôn ngữ của con người dưới dạng văn bản hoặc giọng nói.

\blob \textbf{2 Phân hệ Cốt lõi của NLP:}
\subbull \textbf{1. Hiểu Ngôn ngữ Tự nhiên (NLU - Natural Language Understanding):} Phân tích ý nghĩa, ngữ pháp và cảm xúc của bài viết kinh tế.
\subbull \textbf{2. Sinh Ngôn ngữ Tự nhiên (NLG - Natural Language Generation):} Tự động soạn thảo văn bản giải trình tài chính mạch lạc như con người viết.

% SLIDE 34
\heading{3.3 NLP trong Kế toán - Kiểm toán (P2)}

\blob \textbf{Ứng dụng 1: Phân tích Hợp đồng Kinh tế (Contract Analysis)}
\subbull NLP tự động đọc hợp đồng thuê tài sản dài 50 trang, trích xuất chính xác các điều khoản về thời hạn, lãi suất, quyền mua lại để hạch toán đúng Chuẩn mực IFRS 16.

\blob \textbf{Ứng dụng 2: Trợ lý Ảo cho Giám đốc Tài chính (CFO Chatbot)}
\subbull CFO hỏi: "Doanh thu dòng sản phẩm A tháng này giảm vì sao?" -> NLP phân tích dữ liệu ERP và trả lời ngay lý do chi tiết bằng ngôn ngữ tự nhiên.

% SLIDE 35
\heading{3.4 Khai phá Dữ liệu (Data Mining)}

\blob \textbf{Định nghĩa Khai phá Dữ liệu:}
\subbull Là quá trình phân tích sâu các kho dữ liệu lớn (Data Warehouse) bằng công cụ toán học và AI để tìm ra các mẫu hình (Patterns), xu hướng ẩn và mối tương quan kinh tế.

\blob \textbf{Khác biệt với Thống kê Kế toán truyền thống:}
\subbull Thống kê truyền thống: "Đúng hay sai giả thuyết có sẵn?"
\subbull Khai phá dữ liệu: "Hãy khám phá xem dữ liệu đang ẩn chứa quy luật vàng nào mà Kế toán viên chưa từng nghĩ tới!"

% SLIDE 36
\heading{3.5 Sơ đồ: Big Data Mining và AI}

\begin{center}
\includegraphics[width=0.75\textwidth]{{../../Figures/Buoi_01/Figure 1.2 Relationship between (big) data mining and AI..PNG}}
\par\medskip
\textbf{Figure 1.2:} Mối quan hệ giữa Khai phá Dữ liệu lớn (Big Data Mining) và Trí tuệ Nhân tạo (AI).
\end{center}

% SLIDE 37
\heading{3.6 Phân tích Biểu đồ Figure 1.2}

\blob \textbf{Diễn giải Biểu đồ Figure 1.2 trong Kế toán Quản trị:}
\subbull \textbf{1. Dữ liệu lớn (Big Data):} Là mỏ quặng khổng lồ chứa hàng tỷ bản ghi giao dịch bán hàng, nhật ký hệ thống, dữ liệu thị trường.
\subbull \textbf{2. Khai phá Dữ liệu (Data Mining):} Là công nghệ sàng lọc quặng, trích xuất ra các mô hình (Models) có giá trị kinh tế cao.
\subbull \textbf{3. Trí tuệ Nhân tạo (AI):} Sử dụng các mô hình khai phá được để ra quyết định và tự động hóa tác vụ tài chính thời gian thực.

% SLIDE 38
\heading{3.7 Khai phá Văn bản (Text Mining)}

\blob \textbf{Khái niệm Khai phá Văn bản:}
\subbull Là kỹ thuật chuyên sâu của Data Mining nhằm trích xuất thông tin có giá trị từ dữ liệu văn bản phi cấu trúc (Text-based Data).

\blob \textbf{Ứng dụng trong Kế toán - Kiểm toán \& Đầu tư:}
\subbull \textbf{1. Phân tích Cảm xúc (Sentiment Analysis):} Đo lường tông giọng lạc quan hay bi quan của HĐQT trong Báo cáo Thường niên (Annual Reports) để dự báo giá cổ phiếu.
\subbull \textbf{2. Rà soát Pháp lý:} Quét tự động biên bản họp hội đồng thành viên để tìm cảnh báo rủi ro gian lận, kiện tụng tiềm ẩn.

% SLIDE 39
\heading{3.8 Tự động hóa Quy trình bằng Robot (RPA)}

\blob \textbf{Khái niệm RPA (Robotic Process Automation):}
\subbull Sử dụng "Robot phần mềm" để bắt chước các thao tác máy tính của con người trên giao diện người dùng (GUI) nhằm thực hiện các tác vụ lặp lại theo quy tắc.

\blob \textbf{Hành vi tiêu biểu của Robot RPA trong Kế toán:}
\subbull Tự động đăng nhập vào Cổng dịch vụ Ngân hàng -> Tải Sổ phụ ngân hàng hằng ngày -> Mở phần mềm Kế toán -> Nhập liệu đối chiếu số dư mà không cần con người bấm chuột.

% SLIDE 40
\heading{3.9 Tiến hóa: Từ RPA truyền thống đến AI-RPA}

\blob \textbf{RPA Truyền thống (Blind Robot - Robot mù):}
\subbull Hoạt động thuần túy theo quy tắc cố định (Rule-based: Cứ click vào tọa độ X, Y).
\subbull Gặp một hóa đơn đổi mẫu mã hay mạng internet lag nhẹ là Robot... treo hệ thống và báo lỗi.

\blob \textbf{AI-RPA (Intelligent Automation - Tự động hóa thông minh):}
\subbull Sự dung hợp giữa \textbf{RPA + AI (OCR + Machine Learning + NLP)}.
\subbull Robot không chỉ "click và paste", mà có năng lực HIỂU chứng từ, tự xử lý ngoại lệ và tự học biểu mẫu mới.

% SLIDE 41
\heading{3.10 Case Study RPA + AI trong Kế toán}

\blob \textbf{Quy trình Tự động hóa Kế toán Thanh toán (Accounts Payable - AP):}

\blob \textbf{Các bước tự động liên hoàn không chậm trễ:}
\subbull \textbf{Bước 1 (RPA):} Đúng 8:00 sáng, Robot tự tải 500 file hóa đơn PDF từ hòm thư điện tử của nhà cung cấp.
\subbull \textbf{Bước 2 (AI-IDP):} Học sâu đọc và bóc tách dữ liệu chi tiết từng dòng hóa đơn.
\subbull \textbf{Bước 3 (ML):} Thuật toán đối chiếu tự động 3 bên (3-Way Matching: Hóa đơn == Đơn mua hàng PO == Phiếu nhập kho GRN).
\subbull \textbf{Bước 4 (RPA):} Tự động lập lệnh chi trên hệ thống Ngân hàng cho các chứng từ khớp 100\%; chỉ báo cáo Kế toán viên các trường hợp lệch giá.

% SLIDE 42
\heading{3.11 Giao diện Lập trình Ứng dụng (API) \& AI (P1)}

\blob \textbf{Khái niệm API (Application Programming Interface):}
\subbull Là bộ quy ước giao tiếp chuẩn hóa cho phép các phần mềm và hệ thống máy tính khác nhau "trò chuyện" và chia sẻ dữ liệu trực tiếp với nhau.

\blob \textbf{Chấm dứt Kỷ nguyên Nhập liệu Thủ công:}
\subbull Kế toán viên không còn phải xuất file Excel từ hệ thống bán hàng (POS) rồi hì hục import/nhập lại vào phần mềm Kế toán. API đồng bộ dữ liệu ngay lập tức từng giây.

% SLIDE 43
\heading{3.12 Tích hợp API và AI trong Kế toán (P2)}

\blob \textbf{Hệ sinh thái Kế toán Mở (Open Accounting APIs):}
\subbull \textbf{1. Gọi API sang Mô hình AI:} Phần mềm kế toán khi tạo đơn bán hàng sẽ tự động gọi API sang mô hình AI trên đám mây để chấm điểm hạn mức tín dụng khách hàng trong 0.1 giây.
\subbull \textbf{2. API Thuế Điện tử:} Tự động truyền thẳng dữ liệu hóa đơn điện tử và Báo cáo quyết toán thuế lên Cổng thông tin Tổng cục Thuế với chữ ký số được mã hóa bảo mật.

% SLIDE 44
\heading{3.13 Ngôn ngữ Lập trình tốt nhất cho Kế toán viên}

\blob \textbf{3 "Vũ khí Công nghệ" vàng cho Kế toán viên hiện đại:}
\subbull \textbf{1. Python:} Ngôn ngữ số 1 toàn cầu cho AI, Học máy, Xử lý dữ liệu tài chính lớn và viết kịch bản tự động hóa Kế toán.
\subbull \textbf{2. R:} Ngôn ngữ cực mạnh trong Thống kê toán học chuyên sâu, kiểm định mô hình rủi ro và Kiểm toán phân tích.
\subbull \textbf{3. SQL (Structured Query Language):} Ngôn ngữ truy vấn cơ sở dữ liệu nền tảng, giúp Kế toán viên trực tiếp lấy số liệu từ kho dữ liệu ERP mà không cần nhờ IT.

% SLIDE 45
\heading{3.14 Vì sao Kế toán viên hiện đại chọn Python?}

\blob \textbf{4 Lý do Chiến lược khiến Python là "Ngôn ngữ chung":}
\subbull \textbf{1. Cú pháp cực kỳ trực quan:} Dễ đọc, dễ viết như tiếng Anh tự nhiên, học nhanh chóng ngay cả với sinh viên khối kinh tế - kế toán.
\subbull \textbf{2. Thư viện Kế toán/Tài chính vô địch:} \texttt{pandas} (bảng tính lớn), \texttt{scikit-learn} (học máy), \texttt{matplotlib/seaborn} (trực quan hóa).
\subbull \textbf{3. Tích hợp sâu với Excel \& ERP:} Tự động hóa xử lý hàng trăm file Excel trong 5 giây.
\subbull \textbf{4. Cộng đồng toàn cầu:} Hàng triệu kế toán viên lập trình hỗ trợ giải đáp mã nguồn mở.

% SLIDE 46
\heading{3.15 Lộ trình Nâng cấp Năng lực (Upskilling Roadmap)}

\blob \textbf{4 Bước Phát triển Năng lực AI cho Kế toán viên:}
\subbull \textbf{Bước 1 - Năng lực Dữ liệu (Data Literacy):} Rèn luyện tư duy số, hiểu cấu trúc bảng biểu và nguyên tắc bảo mật dữ liệu tài chính.
\subbull \textbf{Bước 2 - Làm chủ Công cụ Quản trị:} Thành thạo Excel nâng cao (Power Query, Power Pivot) và câu lệnh SQL cơ bản để truy xuất dữ liệu ERP.
\subbull \textbf{Bước 3 - Học lập trình Python Kế toán:} Viết script tự động hóa công việc thường nhật và phân tích dữ liệu thăm dò (EDA).
\subbull \textbf{Bước 4 - Triển khai AI \& RPA:} Tích hợp các mô hình Học máy, NLP và Trợ lý AI vào quy trình nghiệp vụ thực tế của doanh nghiệp.

% SLIDE 47
\heading{Bài tập Ôn tập Tình huống Buổi 1}

\blob \textbf{Đề bài Thực hành - Hãy chọn Công nghệ AI đúng:}
\subbull \emph{Hãy xác định công nghệ phù hợp nhất (\textbf{Supervised ML, Unsupervised ML, NLP, RPA, hay Expert System}) cho 4 bài toán sau:}
\subbull \textbf{Tình huống 1:} Tự động mở website ngân hàng, tải sổ phụ, copy số dư vào phần mềm kế toán vào 7:00 sáng mỗi ngày.
\subbull \textbf{Tình huống 2:} Phân tích 20,000 khách hàng để gom thành 4 nhóm có hành vi mua sắm và thanh toán giống nhau mà không biết trước nhóm nào.
\subbull \textbf{Tình huống 3:} Xây dựng hệ thống kiểm tra tự động xem một khoản vay ngân hàng có tuân thủ đúng định mức tỷ lệ nợ trên vốn theo Luật Thuế hay không.
\subbull \textbf{Tình huống 4:} Đọc file hợp đồng kinh tế PDF và cảnh báo các điều khoản vi phạm chuẩn mực kế toán IFRS 15.

% SLIDE 48
\heading{Tổng kết Buổi 1 \& Lời dặn dò Buổi 2}

\blob \textbf{5 Điểm Ghi nhớ Cốt lõi của Buổi 1:}
\subbull 1. AI không thay thế Kế toán viên; AI mở rộng năng lực và tầm ảnh hưởng của Kế toán viên.
\subbull 2. Phân biệt rõ Trí tuệ con người vs. AI Hẹp (ANI) vs. AI Tổng quát (AGI).
\subbull 3. Học máy (Supervised, Unsupervised, RL) \& Học sâu là động cơ chuyển đổi số tài chính.
\subbull 4. Data Mining, NLP, RPA và API kết hợp tạo nên hệ sinh thái tự động hóa trọn vẹn.
\subbull 5. Python và SQL là chìa khóa thăng tiến trong nghề Kế toán kỷ nguyên số.

\blob \textbf{Dặn dò chuẩn bị cho Buổi 2:}
\subbull Đọc trước tài liệu PDF trong thư mục \texttt{textbook} cho Buổi 2: \textbf{"AI and Finance, Big Data \& Blockchain"}.
\subbull Chuẩn bị câu hỏi thảo luận về cách Big Data và Blockchain thay đổi chứng từ kế toán.

\end{LARGE}
\end{document}
"""

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(header)
    print(f"Successfully generated {tex_path} with 48 academic slides.")

if __name__ == "__main__":
    build_tex()
