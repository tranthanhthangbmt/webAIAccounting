---
theme: "default"
title: "Day 13-15 LT: Khung phân tích Dữ liệu MOSAIC"
author: "Giảng viên"
date: "2026"
---

# BUỔI 13-15: LÝ THUYẾT - DỰ ÁN CUỐI KỲ (KHÔNG CODE)

## Năng lực đạt được sau buổi học
- **Hiểu rõ Quy trình MOSAIC:** Nắm vững 6 bước cốt lõi trong phân tích dữ liệu kế toán: Motivation, Objective, Strategy, Analyze, Interpret, Communicate.
- **Tích hợp công cụ AI (No-Code):** Biết cách áp dụng các công cụ Generative AI (như ChatGPT, Copilot) vào từng bước của quy trình MOSAIC mà không cần viết code (Python/R/SQL).
- **Phát triển Tư duy Phân tích (Data Analytics Mindset):** Rèn luyện tư duy phản biện (Critical Thinking) để đặt câu hỏi đúng, chọn sai số đúng và diễn giải dữ liệu một cách logic.
- **Chuẩn bị cho Dự án Thực tế:** Tạo tiền đề vững chắc để thực hiện dự án cuối khóa (Capstone Project) về cải tiến quy trình kế toán.

## Nội dung chương trình
1. Tổng quan về Dự án Cuối kỳ & Quy trình MOSAIC.
2. Giai đoạn 1: Lập kế hoạch (Plan) - MOS (Motivation, Objective, Strategy).
3. Giai đoạn 2: Phân tích (Analyze) - A (Analyze).
4. Giai đoạn 3: Báo cáo (Report) - IC (Interpret, Communicate).
5. Tư duy Phân tích Dữ liệu & Kỹ năng Tư duy Phản biện (SPARKS).
6. Hướng dẫn Tích hợp AI (No-Code) vào quy trình.

---

# PHẦN 1: TỔNG QUAN VỀ MOSAIC

## 1.1 Khái niệm về Quy trình Phân tích Dữ liệu
- Phân tích dữ liệu không chỉ là sử dụng công cụ (Excel, AI) để xử lý số liệu.
- Đó là một **quy trình có hệ thống** nhằm biến dữ liệu thô (raw data) thành thông tin chi tiết (insights) để ra quyết định kinh doanh.
- Để đạt được hiệu quả, kế toán viên cần một khuôn khổ (framework) chuẩn mực.

## 1.2 MOSAIC là gì?
- **MOSAIC** là một quy trình gồm 6 bước được thiết kế riêng cho lĩnh vực kế toán:
  1. **M**otivation (Động lực/Lý do).
  2. **O**bjective (Mục tiêu).
  3. **S**trategy (Chiến lược).
  4. **A**nalyze (Phân tích).
  5. **I**nterpret (Diễn giải).
  6. **C**ommunicate (Giao tiếp/Báo cáo).

## 1.3 Tại sao sử dụng MOSAIC?
- Được xây dựng dựa trên đặc thù của ngành Kế toán - Tài chính (do Ann Dzuranin & Guido Geerts phát triển).
- Cung cấp cấu trúc logic để sinh viên không bị lạc lối khi đối mặt với một tập dữ liệu lớn.
- Dễ dàng kết hợp với các công cụ AI No-Code.

## 1.4 Ba Giai đoạn Cốt lõi của MOSAIC
- Quy trình 6 bước có thể được gộp thành 3 giai đoạn chính:
  - **Giai đoạn 1: Plan (Lập kế hoạch):** Gồm Motivation, Objective, Strategy. (Bước chuẩn bị quan trọng nhất).
  - **Giai đoạn 2: Analyze (Thực thi):** Tương đương với bước Analyze (xử lý, khám phá dữ liệu).
  - **Giai đoạn 3: Report (Báo cáo):** Gồm Interpret và Communicate (trình bày kết quả cho các bên liên quan).

---

# PHẦN 2: GIAI ĐOẠN 1 - LẬP KẾ HOẠCH (PLAN)

## 2.1 M - Motivation (Động lực)
- **Câu hỏi cốt lõi:** Vấn đề kinh doanh đang gặp phải là gì? Tại sao chúng ta cần phân tích tập dữ liệu này?
- **Ví dụ:** Lãnh đạo công ty phàn nàn rằng "Chi phí vận hành quý vừa qua tăng đột biến mà không rõ lý do". Động lực ở đây là tìm ra nguyên nhân gây tăng chi phí.
- **Vai trò của AI:** Dùng ChatGPT để thảo luận (brainstorming) và làm rõ vấn đề kinh doanh dựa trên mô tả sơ bộ.

## 2.2 O - Objective (Mục tiêu)
- **Câu hỏi cốt lõi:** Chúng ta cần đạt được kết quả cụ thể nào?
- Chuyển hóa động lực (Motivation) thành một câu hỏi phân tích (Data Question) hoặc một giả thuyết (Hypothesis) có thể đo lường được.
- **Ví dụ:** "Xác định các khoản mục chi phí nào đã tăng vượt mức 10% so với dự toán ngân sách trong quý 3."

## 2.3 Phân loại Mục tiêu Phân tích
Có 4 loại phân tích chính:
1. **Descriptive (Mô tả):** Chuyện gì đã xảy ra? (Ví dụ: Báo cáo lợi nhuận năm ngoái).
2. **Diagnostic (Chẩn đoán):** Tại sao nó lại xảy ra? (Ví dụ: Tìm nguyên nhân chi phí tăng).
3. **Predictive (Dự báo):** Chuyện gì sẽ xảy ra? (Ví dụ: Dự báo dòng tiền tháng tới).
4. **Prescriptive (Đề xuất):** Chúng ta nên làm gì? (Ví dụ: Đề xuất phương án cắt giảm chi phí).

## 2.4 S - Strategy (Chiến lược)
- **Câu hỏi cốt lõi:** Chúng ta cần dữ liệu gì, và sẽ dùng phương pháp nào để phân tích?
- Xác định nguồn dữ liệu (ERP, Hóa đơn, File Excel).
- Đánh giá chất lượng dữ liệu (Data Quality).
- Chọn công cụ phân tích (Excel, Power BI, Advanced Data Analysis của AI).

## 2.5 Chiến lược Dữ liệu (Data Strategy)
- Xác định các trường dữ liệu (Fields/Columns) cần thiết.
- **Ví dụ:** Để phân tích chi phí, cần các cột: Mã tài khoản, Tên chi phí, Ngày phát sinh, Số tiền, Bộ phận chịu phí.
- **Vai trò của AI:** Yêu cầu AI (Copilot) lập danh sách các dữ liệu cần thu thập dựa trên mục tiêu phân tích.

---

# PHẦN 3: GIAI ĐOẠN 2 - PHÂN TÍCH (ANALYZE)

## 3.1 A - Analyze (Phân tích)
- Đây là giai đoạn thực thi các thao tác kỹ thuật trên dữ liệu.
- Trong kỷ nguyên AI No-code, bước này đã được tự động hóa phần lớn nhờ các tính năng Data Analytics tích hợp sẵn.
- **Các bước phụ:** Chuẩn bị dữ liệu (Prepare), Khám phá (Explore), và Xây dựng mô hình (Build Models).

## 3.2 Chuẩn bị Dữ liệu (Data Preparation)
- Chiếm đến 80% thời gian của một dự án phân tích.
- **Làm sạch (Cleaning):** Xử lý giá trị trống (Missing values), xóa dòng trùng lặp (Duplicates), sửa định dạng ngày tháng.
- **Chuẩn hóa (Transforming):** Đổi tên cột, tạo cột dữ liệu mới (ví dụ: Cột "Lợi nhuận" = "Doanh thu" - "Chi phí").
- Có thể dùng Power Query hoặc AI Prompt để xử lý nhanh chóng.

## 3.3 Khám phá Dữ liệu (Data Exploration)
- Sử dụng các thống kê mô tả (Descriptive Statistics) để nhìn nhận tổng quan: Trung bình (Mean), Trung vị (Median), Min, Max, Độ lệch chuẩn.
- Vẽ các biểu đồ cơ bản (Histogram, Boxplot) để tìm kiếm các điểm bất thường (Outliers).
- Phân tích tương quan (Correlation) để xem hai biến số có mối liên hệ với nhau không.

## 3.4 Ứng dụng AI trong Khám phá Dữ liệu
- Tải file dữ liệu lên ChatGPT (Advanced Data Analysis).
- Sử dụng Prompt: "Hãy thực hiện Exploratory Data Analysis (EDA) trên tập dữ liệu này và tóm tắt 3 xu hướng đáng chú ý nhất."
- AI sẽ tự động phân tích và trả về các biểu đồ cùng nhận xét sơ bộ.

## 3.5 Xây dựng Mô hình Thông tin (Build Models)
- Đối với phân tích nâng cao, có thể yêu cầu AI áp dụng các mô hình học máy cơ bản như Phân cụm (Clustering) hoặc Hồi quy (Regression).
- **Ví dụ (No-code):** Yêu cầu AI "Sử dụng mô hình hồi quy tuyến tính để dự báo doanh thu tháng 12 dựa trên dữ liệu lịch sử". Sinh viên không cần viết mã Python, AI sẽ tự làm.

---

# PHẦN 4: GIAI ĐOẠN 3 - BÁO CÁO (REPORT)

## 4.1 I - Interpret (Diễn giải)
- **Câu hỏi cốt lõi:** Các con số này có ý nghĩa gì đối với doanh nghiệp?
- Kết nối kết quả phân tích (Analyze) trở lại với Mục tiêu ban đầu (Objective).
- Không chỉ đưa ra kết quả toán học (Ví dụ: P-value < 0.05), mà phải dịch nó sang ngôn ngữ kinh doanh (Ví dụ: "Chiến dịch quảng cáo có tác động tích cực đến doanh số").

## 4.2 Cẩn trọng với Sự thiên kiến trong Diễn giải
- **Thiên kiến xác nhận (Confirmation Bias):** Cố tình diễn giải dữ liệu theo hướng củng cố niềm tin đã có từ trước của bản thân.
- Tương quan không phải là Nhân quả (Correlation does not imply Causation).
- Dùng AI như một "Devil's Advocate" (Người phản biện): "Dựa trên kết quả này, có cách giải thích nào khác phản bác lại kết luận của tôi không?"

## 4.3 C - Communicate (Giao tiếp/Báo cáo)
- Trình bày kết quả và đề xuất hành động (Actionable Insights) cho các bên liên quan (Stakeholders - như Giám đốc, Cổ đông).
- Sử dụng **Trực quan hóa dữ liệu (Data Visualization):** Vẽ biểu đồ (Charts), lập bảng điều khiển (Dashboards).
- Nguyên tắc: "Keep It Simple". Người đọc báo cáo thường không có kiến thức sâu về kỹ thuật phân tích.

## 4.4 Kể chuyện bằng Dữ liệu (Data Storytelling)
- Báo cáo phải là một câu chuyện có logic: Bắt đầu từ Vấn đề (Motivation) -> Quá trình tìm kiếm (Analysis) -> Giải pháp (Insights).
- **Vai trò của AI:** Yêu cầu ChatGPT viết một dàn ý Thuyết minh báo cáo hoặc tạo ra các kịch bản trình bày (Pitch Script) phù hợp với đối tượng khán giả.

---

# PHẦN 5: TƯ DUY PHÂN TÍCH VÀ KỸ NĂNG PHẢN BIỆN (SPARKS)

## 5.1 Data Analytics Mindset
- Để thực hiện tốt MOSAIC, bạn cần một **Tư duy Phân tích Dữ liệu (Data Analytics Mindset)**.
- Đây là sự kết hợp của: Kỹ năng công nghệ, Khả năng đọc hiểu dữ liệu (Data Literacy), và Kỹ năng giao tiếp.
- Quan trọng nhất: **Tư duy Phản biện (Critical Thinking).**

## 5.2 Khung tư duy SPARKS
SPARKS là một bộ công cụ tư duy phản biện dành cho kế toán viên:
- **S**takeholders: Xác định các bên liên quan. Ai quan tâm đến kết quả này?
- **P**urpose: Xác định mục đích. Tại sao chúng ta lại thực hiện nhiệm vụ này?
- **A**lternatives: Xem xét các giải pháp thay thế. Còn cách giải quyết nào khác không?
- **R**isks: Đánh giá rủi ro (Rủi ro về dữ liệu sai, rủi ro mô hình).
- **K**nowledge: Xác định kiến thức cần thiết. Chúng ta đang thiếu thông tin gì?
- **S**elf-Reflection: Tự phản tỉnh. Đánh giá lại kết luận của chính mình để tránh thiên kiến.

## 5.3 Kết hợp MOSAIC và SPARKS
- SPARKS đóng vai trò như một bộ lọc "kiểm soát chất lượng" ở mỗi bước của MOSAIC.
- Ở giai đoạn Motivation: Dùng 'S' (Stakeholders) và 'P' (Purpose).
- Ở giai đoạn Strategy: Dùng 'A' (Alternatives) và 'R' (Risks).
- Ở giai đoạn Interpret: Dùng 'S' (Self-Reflection).

---

# KẾT LUẬN VÀ CHUYỂN TIẾP THỰC HÀNH

## 6.1 Tổng kết Lý thuyết MOSAIC
- MOSAIC (Motivation, Objective, Strategy, Analyze, Interpret, Communicate) là kim chỉ nam cho mọi dự án phân tích dữ liệu trong kế toán.
- Kết hợp với AI, quy trình này giúp tự động hóa khâu "Analyze", giải phóng thời gian để kế toán viên tập trung vào tư duy ở khâu "Plan" và "Report".

## 6.2 Định hướng Dự án Thực tế
- Các buổi thực hành tiếp theo (Day 13-15) sẽ là **Dự án Nhóm Cuối kỳ**.
- Bạn sẽ chọn một bộ dữ liệu kế toán thực tế (Sổ cái, Doanh thu, Chi phí, v.v.).
- Áp dụng toàn bộ quy trình MOSAIC kết hợp với kỹ thuật Prompt (đã học từ Buổi 1 đến 12) để tạo ra một báo cáo phân tích hoàn chỉnh mà không cần viết code.

## CẢM ƠN CÁC BẠN ĐÃ LẮNG NGHE!
- Kết thúc phần Lý thuyết MOSAIC.
- Sẵn sàng bước vào phần Hướng dẫn Thực hành Dự án!
