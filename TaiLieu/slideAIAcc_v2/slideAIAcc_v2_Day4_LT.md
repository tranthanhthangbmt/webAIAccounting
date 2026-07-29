# KẾ HOẠCH SLIDE LÝ THUYẾT - DAY 4 (BUỔI 4)
**Tên bài:** ỨNG DỤNG AI XỬ LÝ CÔNG VIỆC KẾ TOÁN CHI TIẾT VÀ TỔNG HỢP
**Định hướng:** Chuyển đổi từ định khoản và ghi sổ thủ công sang tự động hóa với AI. Tích hợp lý thuyết về Tự động hóa Ghi sổ (AI-Enabled Bookkeeping) và Đối soát/Kiểm soát nội bộ tiền mặt (Cash & Internal Controls).
**Cấu trúc:** 42 Slides.

**ĐỀ XUẤT NGUỒN ẢNH MINH HỌA:**
- **Lấy từ file DOCX/PDF:** Sơ đồ chu trình kế toán (Accounting Cycle), Mô hình Tam giác gian lận (Fraud Triangle).
- **Chụp ảnh màn hình (Screenshot):** Giao diện AI gợi ý định khoản (Nợ/Có), giao diện đối soát ngân hàng tự động (Bank Reconciliation).
- **Sinh ảnh bằng AI:** Một bộ não AI đang phân loại hàng ngàn tờ giấy (chứng từ) vào các rổ khác nhau (tài khoản kế toán); Hình ảnh an ninh mạng bảo vệ két sắt tiền mặt.

---

# PHẦN 1: TỔNG QUAN KẾ TOÁN CHI TIẾT \& TỔNG HỢP

## TRANG BÌA (Title Page)
- Tiêu đề chính: Trí tuệ Nhân tạo cho Kế toán
- Tiêu đề phụ: Buổi 4 - Ứng dụng AI xử lý công việc KT Chi tiết \& Tổng hợp
- Tác giả: Đại học Đông Á
- *(🖼️ Ảnh minh họa: AI Generated - Một bộ não điện tử đang bay lơ lửng trên một quyển sổ cái truyền thống, các con số Nợ/Có phát sáng).*

## NỘI DUNG CHƯƠNG TRÌNH
- 1. Phân biệt Kế toán chi tiết (Bookkeeping) và Kế toán tổng hợp (Accounting).
- 2. Tự động hóa Định khoản và Phân loại tài khoản (Categorization).
- 3. AI trong Đối soát ngân hàng (Reconciliation).
- 4. Tập hợp chi phí \& Lập báo cáo tự động (Reporting).
- 5. Kiểm soát nội bộ trong chu trình Kế toán (Internal Controls).

## Khởi động (Ice-breaker)
- **Câu hỏi:** Điều gì khiến sinh viên kế toán sợ nhất khi làm bài tập Nguyên lý kế toán?
- **Đáp án:** Định khoản sai Nợ / Có và cuối kỳ Bảng Cân Đối Số Phát Sinh không cân!
- **Giải pháp:** Nếu máy tính có thể tự học cách ghi Nợ/Có thì sao?

## Bookkeeping vs Accounting
- **Bookkeeping (Ghi sổ / KT Chi tiết):** Là quá trình thu thập, ghi chép và phân loại các giao dịch tài chính hàng ngày. Mang tính chất lặp đi lặp lại.
- **Accounting (Kế toán Tổng hợp):** Là quá trình phân tích, diễn giải và lập báo cáo từ dữ liệu đã ghi sổ để ra quyết định. Mang tính chất tư duy chiến lược.

## Chu trình Kế toán (The Accounting Cycle)
1. Phân tích giao dịch.
2. Ghi nhật ký (Journalizing - Định khoản).
3. Chuyển sổ cái (Posting).
4. Lập bảng cân đối thử.
5. Thực hiện bút toán điều chỉnh.
6. Lập Báo cáo tài chính.
- *Nhận định:* Bước 1, 2, 3 mất nhiều thời gian nhất $\rightarrow$ Đây là mảnh đất màu mỡ cho AI.

## Nỗi đau của phương pháp truyền thống
- Dựa hoàn toàn vào trí nhớ và kinh nghiệm của kế toán viên để nhớ mã tài khoản (Vd: 156, 331, 642).
- Khối lượng giao dịch quá lớn dẫn đến dễ ghi nhầm, định khoản sai bản chất.
- Đối soát thủ công hàng ngàn dòng sao kê ngân hàng với sổ quỹ tiền mặt cực kỳ mệt mỏi.

## Giải pháp: AI-Enabled Bookkeeping
- Hệ thống AI có thể học từ hàng triệu giao dịch trong quá khứ để tự động dự đoán:
  - Giao dịch này thuộc mã tài khoản nào?
  - Bên Nợ ghi gì, bên Có ghi gì?
- Giúp kế toán tiết kiệm 80\% thời gian gõ phím và giảm thiểu 99\% sai sót cơ học.

---

# PHẦN 2: AI TỰ ĐỘNG HÓA PHÂN LOẠI \& ĐỊNH KHOẢN

## Data Entry Automation (Tự động hóa nhập liệu)
- Tiếp nối bài học Buổi 3 (OCR đọc hóa đơn).
- AI không chỉ dừng ở việc "Đọc chữ", mà nó lấy dữ liệu đó làm đầu vào cho bước tiếp theo: **Định khoản**.
- *(🖼️ Ảnh minh họa: Lưu đồ OCR $\rightarrow$ Database $\rightarrow$ Journal Entry).*

## Categorization Automation (Tự động Phân loại)
- Kế toán có hàng ngàn nghiệp vụ khác nhau.
- \textbf{Quy tắc cũ (Rule-based):} Nếu thấy chữ "Vinamilk" $\rightarrow$ Ghi vào Chi phí tiếp khách. Nhưng nếu mua sữa về làm bánh (Công ty Bánh kẹo) thì lại là Nguyên vật liệu!
- \textbf{AI thế hệ mới:} AI phân tích \textbf{Ngữ cảnh (Context)} để gợi ý mã tài khoản chính xác chứ không chỉ dựa vào từ khóa.

## Machine Learning trong Định khoản
- AI được "huấn luyện" (Train) dựa trên dữ liệu kế toán của chính công ty trong 5 năm qua.
- Nếu bạn thường xuyên định khoản tiền điện vào TK 6427 (Chi phí dịch vụ mua ngoài - QLDN), AI sẽ học được \textbf{Pattern (Quy luật)} đó.
- Lần sau có hóa đơn điện Điện lực EVN, AI tự động tạo bút toán: Nợ 6427 / Nợ 1331 / Có 331.

## Prompt Engineering để Định khoản (ChatGPT)
- Ngay cả khi không có phần mềm xịn, bạn có thể dùng ChatGPT làm "Trợ lý định khoản".
- \textbf{Prompt:} *"Bạn là Kế toán trưởng Việt Nam (TT200). Tôi vừa thanh toán tiền mua 5 máy tính bằng chuyển khoản, dùng cho phòng Giám đốc. Hãy định khoản giúp tôi."*
- \textbf{AI trả lời:} Nợ TK 211 (Tài sản cố định) / Nợ TK 133 / Có TK 112.

## Đào tạo AI bằng bộ luật nội bộ
- Mỗi doanh nghiệp có bộ tài khoản chi tiết khác nhau (Vd: 64271 là Tiền điện, 64272 là Tiền nước).
- Kế toán có thể tải (upload) Hệ thống tài khoản nội bộ lên AI và ra lệnh: *"Từ nay hãy định khoản dựa trên danh sách mã tài khoản này"*.

## Duyệt và Xác nhận (The Human Touch)
- Các phần mềm Kế toán tích hợp AI (như Xero, QuickBooks, MISA AMIS) không tự ý ghi sổ.
- Nó \textbf{Đề xuất (Suggest)} bút toán màu xanh lá cây.
- Kế toán viên chỉ việc lướt qua, thấy đúng thì bấm \textbf{"Duyệt (Approve)"}. Nhanh hơn gõ tay rất nhiều!

## Xử lý các nghiệp vụ phức tạp (Complex Transactions)
- Trả góp, phân bổ công cụ dụng cụ, khấu hao TSCĐ.
- AI có khả năng tự động tạo bảng phân bổ (Amortization Schedule) và tự động sinh bút toán Nợ/Có vào mỗi cuối tháng mà không cần con người can thiệp.

---

# PHẦN 3: AI TRONG ĐỐI SOÁT VÀ TẬP HỢP CHI PHÍ

## Reconciliation Automation (Đối soát tự động)
- \textbf{Đối soát (Reconciliation):} Là quá trình so sánh số liệu giữa 2 nguồn độc lập (Ví dụ: Sổ quỹ công ty và Sao kê ngân hàng) để đảm bảo khớp nhau.
- \textbf{Thực trạng:} Mò mẫm từng dòng sao kê với sổ cái bằng thước kẻ và bút dạ quang.

## AI xử lý Sao kê Ngân hàng (Bank Reconciliation)
- AI-powered systems có thể so sánh hàng vạn giao dịch trong 3 giây.
- Nó ghép cặp (Match) theo: Ngày tháng, Số tiền, Mã giao dịch, Nội dung chuyển khoản.
- Tự động tick xanh các khoản đã khớp.

## Phát hiện Sai lệch (Discrepancy Identification)
- Nếu khách hàng chuyển 1.000.000đ nhưng trừ phí chuyển khoản 3.300đ $\rightarrow$ Tiền về tài khoản là 996.700đ.
- Kế toán truyền thống tìm "lòi mắt" không ra con số 1.000.000đ trên sao kê.
- \textbf{AI:} Nhận diện được khoản phí 3.300đ, tự động tách bút toán ghi nhận Chi phí tài chính (TK 635) để khớp sổ.

## Expense Management Automation (Quản lý chi phí)
- Nhân viên đi công tác dùng thẻ tín dụng công ty.
- AI kết nối thẳng với ngân hàng, tự động tải giao dịch về.
- Yêu cầu nhân viên chụp bill qua app điện thoại $\rightarrow$ AI đọc OCR $\rightarrow$ Tự động khớp bill với giao dịch quẹt thẻ $\rightarrow$ Tự động hạch toán chi phí.

## Tập hợp chi phí tính giá thành
- Kế toán sản xuất đau đầu nhất ở việc: Tập hợp chi phí NVL (621), Nhân công (622), Sản xuất chung (627).
- Dùng AI để phân bổ: Cung cấp cho AI tiêu thức phân bổ (theo giờ công máy, theo diện tích, theo nhân sự), AI tự động tính toán và tạo bút toán kết chuyển (TK 154).

## Dùng Prompt yêu cầu AI tính toán phân bổ
- \textbf{Prompt:} *"Tôi có chi phí điện tháng này là 50 triệu. Hãy lập bảng phân bổ chi phí này cho 3 phân xưởng A, B, C dựa trên tỷ lệ giờ máy hoạt động lần lượt là 200, 300, 500 giờ."*
- AI sẽ tính ra số tiền tương ứng cho từng phân xưởng ngay lập tức.

---

# PHẦN 4: LẬP BÁO CÁO CHI TIẾT \& TỔNG HỢP VỚI AI

## Reporting Automation (Báo cáo tự động)
- Báo cáo không chỉ là BCTC cuối năm, mà là Báo cáo quản trị (Management Reports) gửi cho Sếp hàng ngày.
- Báo cáo công nợ phải thu, phải trả, báo cáo dòng tiền (Cash Flow).

## Generative AI phân tích dữ liệu
- Bạn có một file Excel chứa 10.000 dòng Sổ Nhật ký chung.
- Khó khăn: Sếp hỏi *"Tháng này ta chi tiếp khách bao nhiêu tiền? Gấp đôi tháng trước không?"*
- Nếu tự làm: Mất 15 phút dùng Pivot Table.

## Dùng ChatGPT Advanced Data Analysis
- Tải file Excel Sổ Nhật ký chung lên ChatGPT.
- \textbf{Prompt:} *"Từ Sổ cái này, hãy tính tổng chi phí tiếp khách (TK 6428) trong tháng 3 và so sánh với tháng 2. Vẽ biểu đồ cột để minh họa."*
- AI sẽ tự code Python ngầm, đọc dữ liệu và vẽ biểu đồ trong 10 giây.

## AI hỗ trợ lập Báo cáo Dòng tiền (Statement of Cash Flows)
- Lập Báo cáo Lưu chuyển tiền tệ luôn là ác mộng của kế toán.
- AI có khả năng rà soát toàn bộ phát sinh đối ứng với nhóm tài khoản Tiền (111, 112) và tự động phân loại vào 3 luồng: HĐ Kinh doanh, HĐ Đầu tư, HĐ Tài chính.

## Lập Thuyết minh Báo cáo Tài chính
- Thuyết minh BCTC là văn bản dài dòng.
- \textbf{Giải pháp AI:} Cung cấp cho AI Bảng Cân Đối Kế Toán và Báo cáo Kết quả Kinh doanh.
- \textbf{Prompt:} *"Hãy viết bản dự thảo Thuyết minh báo cáo tài chính phần 'Sự biến động của Hàng tồn kho' dựa trên số liệu này."*

## Xây dựng Dashboard Quản trị trực quan
- AI kết hợp với Power BI hoặc Excel Copilot.
- Kế toán chỉ việc chat: *"Lập một Dashboard doanh thu theo chi nhánh và sản phẩm"*.
- Hệ thống tự động kéo thả tạo biểu đồ trực quan $\rightarrow$ Nâng tầm kế toán thành Chuyên viên phân tích dữ liệu (Data Analyst).

---

# PHẦN 5: KIỂM SOÁT NỘI BỘ VÀ QUẢN LÝ SAI SÓT (INTERNAL CONTROLS)

## Tại sao cần Kiểm soát Nội bộ?
- *Nhắc lại câu chuyện Enron \& WorldCom (Accounting Scandals).*
- Những công ty lớn sụp đổ vì Kế toán trưởng "nấu sổ" (Cooking the books).
- Kế toán không chỉ lo tính toán, mà còn phải thiết lập hệ thống bảo vệ tài sản công ty.

## Mô hình Tam giác Gian lận (Fraud Triangle)
- Gian lận tài chính xảy ra khi hội tụ 3 yếu tố:
  1. \textbf{Áp lực (Pressure/Motivation):} Nợ nần cá nhân, áp lực chỉ tiêu.
  2. \textbf{Cơ hội (Opportunity):} Quản lý lỏng lẻo, dễ rút tiền mà không ai biết.
  3. \textbf{Bao biện (Rationalization):} "Tôi chỉ mượn tạm, mai tôi trả".

## Trọng tâm của Kiểm soát Nội bộ
- Doanh nghiệp không thể kiểm soát "Áp lực" hay "Bao biện" của nhân viên.
- Doanh nghiệp chỉ có thể triệt tiêu \textbf{"Cơ hội (Opportunity)"}.
- \textbf{Công cụ triệt tiêu Cơ hội:} Hệ thống Kiểm soát Nội bộ (Internal Controls).

## 2 Mục tiêu cốt lõi của Internal Controls
1. \textbf{Bảo vệ Tài sản (Safeguard Assets):} Chống mất cắp, biển thủ tiền mặt, hàng tồn kho.
2. \textbf{Cải thiện tính chính xác \& độ tin cậy của Kế toán:} Đảm bảo BCTC không có sai sót trọng yếu.

## Đặc thù kiểm soát Tiền (Cash)
- Tiền là tài sản dễ bị đánh cắp nhất (Thanh khoản cao nhất).
- \textbf{Nguyên tắc Phân quyền (Separation of Duties):} 
  - Người giữ tiền (Thủ quỹ) \textbf{KHÔNG} được phép là người ghi sổ kế toán tiền (Kế toán thanh toán).
  - Một người ôm cả 2 việc = Rủi ro gian lận 99\%.

## AI củng cố Kiểm soát Nội bộ như thế nào?
- Khi áp dụng AI vào định khoản và đối soát, tính \textbf{Chính xác cơ học} được đẩy lên tối đa.
- Máy móc không biết "Cố tình gian lận" hay "Biển thủ".
- AI ghi log (nhật ký) mọi hành động: Giao dịch này do AI đề xuất, ai là người bấm duyệt? Lúc mấy giờ? $\rightarrow$ Dấu vết kiểm toán (Audit Trail) hoàn hảo.

## Rủi ro khi phụ thuộc vào AI (AI Risks)
- \textbf{Automation Bias (Thành kiến Tự động hóa):} Kế toán viên quá tin tưởng vào AI, nhắm mắt duyệt (Approve) hàng loạt mà không đọc.
- Nếu mô hình AI học từ dữ liệu sai trong quá khứ (Garbage In - Garbage Out), nó sẽ tự động hạch toán sai hàng loạt trong tương lai.

## Kiểm soát hệ thống AI
- Phải có quy trình đối chiếu mẫu định kỳ: Lấy ngẫu nhiên 5\% số lượng bút toán do AI tự làm ra để Kế toán trưởng rà soát tay.
- Giới hạn quyền hạn của AI: AI không được phép tạo bút toán trực tiếp đối với các nghiệp vụ nhạy cảm (Phân chia lợi nhuận, Tính lương).

## Continuous Auditing (Kiểm toán liên tục)
- Nhờ AI xử lý số liệu realtime, doanh nghiệp không cần đợi đến cuối tháng mới kiểm tra rủi ro.
- AI sẽ quét sổ cái hàng ngày và tự động gửi Cảnh báo (Alert): *"Hôm nay có 3 bút toán chuyển tiền tỷ lệ bất thường, yêu cầu kế toán trưởng kiểm tra"*.

## Tác động đến Tổ chức bộ máy Kế toán
- \textbf{Mô hình cũ (Hình tháp):} 1 Kế toán trưởng $\rightarrow$ 3 Kế toán tổng hợp $\rightarrow$ 10 Kế toán viên nhập liệu.
- \textbf{Mô hình mới với AI (Kim cương):} AI làm thay 80\% việc nhập liệu. Doanh nghiệp cần nhiều "Nhà phân tích dữ liệu kế toán" hơn là "Thợ gõ".

## Ứng dụng thực tế: Live Nation Entertainment
- Công ty tổ chức sự kiện âm nhạc lớn nhất thế giới (Bán 500 triệu vé/năm).
- Với lượng giao dịch khổng lồ, họ dùng Hệ thống thông tin và AI để giám sát dòng tiền, phân tích số vé bán và người vào cổng theo thời gian thực để chống thất thoát.
- *(Tham khảo từ Case Study trong sách Financial Accounting)*.

## Tư duy lại công việc định khoản
- Không cần phải "thuộc lòng" bộ mã tài khoản nữa.
- Cần "hiểu bản chất" của nghiệp vụ kinh tế để biết AI gợi ý như vậy là đúng hay sai.
- Chuyển từ Tư duy \textbf{Nhớ (Memorize)} sang Tư duy \textbf{Phân tích (Analyze)}.

## AI là trợ lý, không phải sếp của bạn!
- Bạn là người đặt ra câu lệnh (Prompt).
- Bạn là người cung cấp nguyên tắc kiểm soát.
- Kế toán viên nắm AI trong tay sẽ thay thế kế toán viên không biết dùng AI.

## Tóm tắt Buổi 4
- \textbf{Tự động hóa:} AI giải quyết triệt để khâu Ghi sổ (Bookkeeping), tự động phân loại Nợ/Có và đối soát ngân hàng.
- \textbf{Tổng hợp:} Dùng Prompt AI để tạo Báo cáo, vẽ biểu đồ và phân tích dữ liệu lớn.
- \textbf{Kiểm soát:} Cần củng cố Internal Controls để triệt tiêu cơ hội gian lận và kiểm soát lỗi hệ thống AI.

## Chuẩn bị cho Buổi Thực hành
- Yêu cầu ôn tập lại các nhóm tài khoản kế toán Việt Nam (TT200 / TT133).
- Cài đặt sẵn Excel.
- Chuẩn bị một file Excel chứa Bảng Cân đối Tài khoản (Trial Balance) để thực hành dùng AI phân tích số liệu.

## Q\&A
- Cùng thảo luận: Nếu AI tự động định khoản và đối soát ngân hàng khớp 100\%, liệu vị trí "Kế toán thanh toán" có biến mất trong tương lai gần?
