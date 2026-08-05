import re
import json

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Ứng dụng AI giúp Kế toán Điều tra chuyển đổi từ mô hình phản ứng hậu kiểm sang mô hình nào?",
        "options": [
            { "id": "a", "text": "Phòng ngừa chủ động (Proactive Prevention)" },
            { "id": "b", "text": "Kiểm toán truyền thống dựa trên sổ sách giấy tờ" },
            { "id": "c", "text": "Hệ thống chuyên gia lập trình quy tắc thủ công" },
            { "id": "d", "text": "Lập báo cáo tài chính nội bộ thủ công hàng quý" }
        ],
        "correctAnswer": "a",
        "explanation": "AI giúp chuyển từ kiểm tra sau khi sự cố xảy ra sang phòng ngừa chủ động và theo thời gian thực."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Đâu là điểm yếu lớn nhất của phương pháp chọn mẫu thống kê truyền thống trong phát hiện gian lận?",
        "options": [
            { "id": "a", "text": "Cần quá nhiều phần mềm máy tính hiện đại để chạy" },
            { "id": "b", "text": "Nó bỏ lọt các giao dịch gian lận nằm ngoài mẫu kiểm toán" },
            { "id": "c", "text": "Nó phân tích 100% giao dịch khiến kế toán viên mệt mỏi" },
            { "id": "d", "text": "Hệ thống tự động đưa ra quá nhiều cảnh báo giả" }
        ],
        "correctAnswer": "b",
        "explanation": "Chọn mẫu thống kê thường chỉ kiểm tra 5-10% dữ liệu, kẻ gian lận dễ dàng lách qua bằng cách chia nhỏ giao dịch (Smurfing)."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các công nghệ AI với tính năng chính trong phát hiện gian lận:",
        "left": [
            { "id": "l1", "text": "Xử lý Ngôn ngữ Tự nhiên (NLP)" },
            { "id": "l2", "text": "Phân tích Mạng lưới (Graph Analysis)" },
            { "id": "l3", "text": "Học không giám sát (Unsupervised ML)" }
        ],
        "right": [
            { "id": "r1", "text": "Đọc hiểu email, hợp đồng và biên bản họp" },
            { "id": "r2", "text": "Trực quan hóa quan hệ giữa các tài khoản, IP, công ty sân sau" },
            { "id": "r3", "text": "Tự động gom cụm, tìm điểm ngoại lai mà không cần gán nhãn" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "NLP đọc văn bản. Graph vẽ sơ đồ mạng lưới quan hệ. Unsupervised ML tìm điểm bất thường từ dữ liệu thô."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp theo Lộ trình 7 Bước Triển khai AI trong Kế toán (4 bước đầu):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Đánh giá chiến lược và xác định nút thắt cổ chai" },
            { "id": "2", "text": "Chọn lựa công cụ AI phù hợp quy mô doanh nghiệp" },
            { "id": "3", "text": "Đào tạo nhân sự kỹ năng AI, xóa bỏ tâm lý e ngại" },
            { "id": "4", "text": "Triển khai thí điểm (Pilot) trên tác vụ lặp đi lặp lại" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Lộ trình: Đánh giá chiến lược -> Chọn công cụ -> Đào tạo nhân lực -> Triển khai Pilot."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ vào khái niệm phân tích dữ liệu gian lận:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Thay vì kiểm tra hậu kỳ (sau khi kết thúc kỳ kế toán), hệ thống AI phân tích toàn phần 100% dữ liệu theo <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, giúp phát hiện và ngăn chặn giao dịch bất thường nhằm giảm thiểu <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "thời gian thực (real-time)" },
            { "id": "w2", "text": "cảnh báo giả (false positives)" },
            { "id": "w3", "text": "chu kỳ hàng năm" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Real-time anomaly detection giúp cảnh báo ngay khi giao dịch xảy ra, đồng thời AI học cách giảm bớt cảnh báo giả (false positives)."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Hiện tượng 'ảo giác' (Hallucination) trong AI Tạo sinh (GenAI) mang lại rủi ro gì lớn nhất cho ngành kế toán?",
        "options": [
            { "id": "a", "text": "AI sinh ra thông tin, trích dẫn hoặc số liệu tài chính không có thật" },
            { "id": "b", "text": "Nó làm máy tính của kế toán viên tiêu thụ quá nhiều điện năng" },
            { "id": "c", "text": "Không thể kết nối với mạng nội bộ của doanh nghiệp" },
            { "id": "d", "text": "Luôn dự báo lạm phát sai lệch do lỗi phần cứng" }
        ],
        "correctAnswer": "a",
        "explanation": "Ảo giác của GenAI là hiện tượng nó tự bịa ra thông tin sai lệch trông có vẻ hợp lý, rất nguy hiểm nếu áp dụng vào BCTC."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Mô hình Học máy nào phù hợp nhất để nhận diện các chiêu thức gian lận ĐÃ BIẾT từ dữ liệu lịch sử?",
        "options": [
            { "id": "a", "text": "Học không giám sát (Unsupervised Learning)" },
            { "id": "b", "text": "Học có giám sát (Supervised Learning)" },
            { "id": "c", "text": "Hệ thống lưu trữ đám mây phân tán" },
            { "id": "d", "text": "Thuật toán K-Means Clustering" }
        ],
        "correctAnswer": "b",
        "explanation": "Học có giám sát dùng dữ liệu đã gán nhãn ('gian lận' / 'hợp lệ') để nhận diện lại các hành vi gian lận đã biết."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các thuật ngữ kỹ thuật dữ liệu tài chính với đặc điểm của chúng:",
        "left": [
            { "id": "l1", "text": "Underfitting (Độ lệch cao)" },
            { "id": "l2", "text": "Overfitting (Phương sai cao)" },
            { "id": "l3", "text": "Bias vs. Variance Tradeoff" }
        ],
        "right": [
            { "id": "r1", "text": "Mô hình quá đơn giản, không học được quy luật dữ liệu" },
            { "id": "r2", "text": "Mô hình quá phức tạp, học vẹt cả nhiễu của dữ liệu huấn luyện" },
            { "id": "r3", "text": "Quá trình tìm điểm cân bằng tối ưu giữa hai lỗi sai số trên" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Underfitting là Bias cao. Overfitting là Variance cao. Điểm cân bằng là Tradeoff."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ liên quan đến quá trình huấn luyện Học máy (Modeling Process):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Để đánh giá mô hình, tập dữ liệu được chia làm hai phần: Tập <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (thường chiếm 80%) để mô hình học quy luật và Tập <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> (thường 20%) dùng để đánh giá hiệu suất khách quan.",
        "words": [
            { "id": "w1", "text": "huấn luyện (Training set)" },
            { "id": "w2", "text": "kiểm tra (Test set)" },
            { "id": "w3", "text": "ngoại lai (Outliers)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Data luôn được chia Train (để học) và Test (để kiểm chứng)."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp Vòng đời Dự án Khoa học Dữ liệu trong Kiểm tra Gian lận (Data Science Lifecycle):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Hiểu bài toán nghiệp vụ (Xác định mục tiêu chống gian lận)" },
            { "id": "2", "text": "Đánh giá, làm sạch & Chuẩn bị dữ liệu (Data Preparation)" },
            { "id": "3", "text": "Mô hình hóa (Modeling) & Đánh giá hiệu suất thuật toán" },
            { "id": "4", "text": "Triển khai hệ thống (Deployment) vào giám sát thực tế" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Theo hình 6.4: Business Understanding -> Data Prep -> Modeling & Evaluation -> Deployment."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong Case Study 4, cơ quan nhà nước đã phát hiện 'Thông đồng đấu thầu' (Bid-rigging) thông qua thuật toán nào?",
        "options": [
            { "id": "a", "text": "Hồi quy tuyến tính đơn giản trên bảng tính Excel" },
            { "id": "b", "text": "Phân tích bất thường kết hợp phân tích mạng lưới (Graph Analytics)" },
            { "id": "c", "text": "Mạng nơ-ron nhân tạo thế hệ đầu từ thập niên 90" },
            { "id": "d", "text": "Học có giám sát dùng dữ liệu gian lận ngân hàng" }
        ],
        "correctAnswer": "b",
        "explanation": "AI phân tích bất thường và Graph Analytics theo dõi lịch sử nộp thầu của các công ty có liên quan (sân sau)."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Theo báo cáo, công nghệ Trí tuệ Nhân tạo đang tác động đến ngành Kế toán - Kiểm toán như thế nào?",
        "options": [
            { "id": "a", "text": "Loại bỏ hoàn toàn sự can thiệp và kiểm soát của con người" },
            { "id": "b", "text": "Thay thế phán đoán nghề nghiệp của kiểm toán viên" },
            { "id": "c", "text": "Tự động kiểm tra 100% dữ liệu, chuyển hướng sang kiểm toán liên tục" },
            { "id": "d", "text": "Làm chậm quá trình phát hành báo cáo tài chính cuối năm" }
        ],
        "correctAnswer": "c",
        "explanation": "AI tự động kiểm tra 100% dữ liệu giúp kiểm toán viên chuyển từ lấy mẫu sang Kiểm toán liên tục (Continuous Auditing)."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các cấp độ AI với định nghĩa trong Kế toán (Theo biểu đồ Venn):",
        "left": [
            { "id": "l1", "text": "Trí tuệ nhân tạo (AI)" },
            { "id": "l2", "text": "Học máy (ML)" },
            { "id": "l3", "text": "Học sâu (Deep Learning)" }
        ],
        "right": [
            { "id": "r1", "text": "Khái niệm rộng nhất về máy tính mô phỏng trí thông minh con người" },
            { "id": "r2", "text": "Máy tính sử dụng thuật toán thống kê để tự học từ dữ liệu tài chính" },
            { "id": "r3", "text": "Phân nhánh nâng cao dùng mạng nơ-ron nhiều lớp (nhận diện hình ảnh/chữ viết)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "AI là tập lớn nhất. ML là tập con của AI. DL là tập con của ML chuyên xử lý phức tạp bằng mạng nơ-ron."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về hệ thống phát hiện gian lận tiền lương (Payroll Fraud):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong Case Study Tập đoàn Đa quốc gia, AI sử dụng kỹ thuật phân cụm <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để đối chiếu chéo thông tin ngân hàng và mã số thuế, qua đó phát hiện các tài khoản <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> do quản lý chi nhánh cấu kết tạo ra.",
        "words": [
            { "id": "w1", "text": "không giám sát (Unsupervised)" },
            { "id": "w2", "text": "nhân viên ma (ghost employees)" },
            { "id": "w3", "text": "đám mây phân tán" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Sử dụng Unsupervised Learning để tìm các 'ghost employees' không có thật nhằm bòn rút tiền lương."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp quá trình Phát triển Hệ thống Big Data (Tech Stack):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Hệ thống ghi nhận dữ liệu từ các giao dịch thô (Data Sources)" },
            { "id": "2", "text": "Hệ thống truyền tải sự kiện trực tuyến (Ví dụ: Apache Kafka)" },
            { "id": "3", "text": "Hệ thống lưu trữ phân tán và xử lý đám mây (Hadoop/Spark)" },
            { "id": "4", "text": "Giao diện trực quan hóa dữ liệu cho Kế toán viên (Tableau/Power BI)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Tech stack flow: Nguồn dữ liệu -> Streaming/Kafka -> Data Lake/Hadoop -> Visualization BI tools."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong kinh tế vĩ mô, Ngân hàng Trung ương sử dụng AI để cảnh báo hiện tượng 'Rút tiền ồ ạt' (Bank Run) như thế nào?",
        "options": [
            { "id": "a", "text": "Từ chối mọi yêu cầu rút tiền của khách hàng cá nhân" },
            { "id": "b", "text": "Phân tích tự động các chỉ số thanh khoản, dòng tiền gửi và tỷ lệ nợ xấu" },
            { "id": "c", "text": "Xóa bỏ các hồ sơ vay vốn có rủi ro cao một cách thủ công" },
            { "id": "d", "text": "Chỉ dựa vào các tin đồn vô căn cứ trên báo chí truyền thông" }
        ],
        "correctAnswer": "b",
        "explanation": "AI quét hàng vạn chỉ tiêu báo cáo tuân thủ từ các ngân hàng để phát hiện sớm sụt giảm thanh khoản, ngăn chặn Bank Run."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các ứng dụng GenAI với lĩnh vực Kế toán cụ thể:",
        "left": [
            { "id": "l1", "text": "Kế toán Tài chính" },
            { "id": "l2", "text": "Kế toán Quản trị" },
            { "id": "l3", "text": "Tư vấn Thuế" }
        ],
        "right": [
            { "id": "r1", "text": "Tự động phân loại hóa đơn (OCR) và hạch toán" },
            { "id": "r2", "text": "Dự báo dòng tiền (Cash Flow) và phân tích phương sai" },
            { "id": "r3", "text": "Rà soát luật thuế, chuẩn bị tờ khai tối ưu hóa chi phí" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Tài chính -> hạch toán. Quản trị -> dự báo tương lai. Thuế -> chuẩn bị tờ khai."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Việc sử dụng công nghệ AI 'hộp đen' (Black-box) trong kiểm toán gặp trở ngại pháp lý gì lớn nhất?",
        "options": [
            { "id": "a", "text": "Không thể giải thích cho cơ quan pháp luật lý do AI đưa ra kết luận" },
            { "id": "b", "text": "Chi phí quá rẻ khiến hệ thống mất đi sự uy tín" },
            { "id": "c", "text": "Hộp đen không thể đọc được dữ liệu phi cấu trúc" },
            { "id": "d", "text": "Chỉ hoạt động được trên các máy tính siêu phân luồng" }
        ],
        "correctAnswer": "a",
        "explanation": "Black-box AI khó giải thích quy trình ra quyết định, gây khó khăn khi cần trình bày căn cứ khởi tố trước Tòa án."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ liên quan đến sự giám sát của con người đối với AI:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Mặc dù AI có thể tự động hóa hàng loạt quy trình kế toán, nguyên tắc <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> yêu cầu Kế toán viên phải luôn luôn kiểm duyệt và duy trì sự kiểm soát cuối cùng, kết hợp với <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> để ra quyết định.",
        "words": [
            { "id": "w1", "text": "Human-in-the-loop" },
            { "id": "w2", "text": "phán đoán nghề nghiệp" },
            { "id": "w3", "text": "làm sạch dữ liệu" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Nguyên tắc 'Người dùng trong vòng lặp' (Human-in-the-loop) nhấn mạnh vai trò quyết định cuối cùng vẫn thuộc về chuyên gia."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong Case Study 3 (Bảo hiểm), AI kết hợp NLP với Computer Vision để giải quyết vấn đề gì?",
        "options": [
            { "id": "a", "text": "Xác định xem nhân viên bảo hiểm có đi làm đúng giờ hay không" },
            { "id": "b", "text": "Đọc báo cáo giám định và phân tích ảnh hiện trường để tìm dấu hiệu chỉnh sửa" },
            { "id": "c", "text": "Phân tích giá cổ phiếu của các công ty bảo hiểm trên sàn chứng khoán" },
            { "id": "d", "text": "In hóa đơn bồi thường ra giấy một cách tự động" }
        ],
        "correctAnswer": "b",
        "explanation": "NLP đọc văn bản giám định và Computer Vision phân tích hình ảnh xem ảnh tai nạn có bị photoshop cắt ghép hay không."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp mức độ phức tạp từ thấp đến cao trong 3 trụ cột kỹ năng Kế toán viên hiện đại (Venn Diagram):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Kiến thức chuyên môn Kế toán / Tài chính cốt lõi" },
            { "id": "2", "text": "Sử dụng công cụ tính toán Thống kê và Excel trung cấp" },
            { "id": "3", "text": "Viết truy vấn SQL, Python để xử lý Dữ liệu lớn (Big Data)" },
            { "id": "4", "text": "Xây dựng và huấn luyện mô hình Học máy (Machine Learning)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Từ kiến thức kế toán nền tảng -> Thống kê Excel -> SQL/Python Big data -> ML modeling."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các Khung Kỹ năng Cần thiết trong thời đại AI (Bảng 2.2) với mức độ quan trọng:",
        "left": [
            { "id": "l1", "text": "Tư duy phản biện & Thẩm định (Kiểm chứng sai lệch)" },
            { "id": "l2", "text": "Kỹ thuật Prompt & Giao tiếp AI (SPARKS)" },
            { "id": "l3", "text": "Đạo đức & Tuân thủ Pháp lý (GDPR)" }
        ],
        "right": [
            { "id": "r1", "text": "Quan trọng nhất, bắt buộc để chặn ảo giác AI trước khi duyệt" },
            { "id": "r2", "text": "Kỹ năng cốt lõi giúp điều khiển và ra lệnh chính xác cho ChatGPT" },
            { "id": "r3", "text": "Rất cao, đảm bảo không vi phạm bảo mật dữ liệu khách hàng" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Phản biện là quan trọng nhất để tránh báo cáo sai. Prompt là công cụ giao tiếp hằng ngày. Tuân thủ GDPR bảo vệ quyền riêng tư."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Khái niệm 'Giải thích mô hình' (Explainable AI - XAI) có ý nghĩa gì trong kiểm toán?",
        "options": [
            { "id": "a", "text": "Mô hình giúp người dùng biết được lý do tại sao AI lại ra kết luận gian lận" },
            { "id": "b", "text": "Mô hình có thể tự động thuyết trình bằng giọng nói qua loa" },
            { "id": "c", "text": "Mô hình giấu kín thuật toán để bảo mật 100% trước đối thủ" },
            { "id": "d", "text": "AI không cần giải thích gì vì kết quả của nó luôn luôn đúng" }
        ],
        "correctAnswer": "a",
        "explanation": "Explainable AI (XAI) giúp mở 'hộp đen', làm rõ cách AI suy luận để có thể giải trình trước Tòa án hoặc cấp quản lý."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về rủi ro của AI Tạo sinh (GenAI):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong chính sách bảo mật doanh nghiệp, nhân viên kế toán tuyệt đối bị cấm đưa các số liệu tài chính <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> lên các công cụ AI công cộng (như ChatGPT bản miễn phí) để tránh rò rỉ <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "mật (confidential)" },
            { "id": "w2", "text": "sở hữu trí tuệ và bí mật kinh doanh" },
            { "id": "w3", "text": "đã công bố công khai" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Dữ liệu mật bị đưa lên AI công cộng có nguy cơ bị dùng làm dữ liệu huấn luyện, gây rò rỉ bí mật."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Trình tự khám phá bất thường trong Mua sắm công (Tackling bid-rigging):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Tập hợp hàng nghìn hồ sơ nộp thầu lịch sử" },
            { "id": "2", "text": "Sử dụng Graph Analytics vẽ bản đồ quan hệ (IP, email, cổ đông)" },
            { "id": "3", "text": "Phát hiện tần suất thắng thầu luân phiên và mức giá sát nút dự toán" },
            { "id": "4", "text": "Kết luận mạng lưới thông đồng thầu (collusion) và khởi tố" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Lấy hồ sơ -> Vẽ sơ đồ quan hệ -> Nhận diện mẫu luân phiên -> Kết luận có thông đồng."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Quá trình EDA (Exploratory Data Analysis) trong học máy dùng để làm gì?",
        "options": [
            { "id": "a", "text": "Đóng gói phần mềm để bán cho khách hàng" },
            { "id": "b", "text": "Thăm dò, vẽ biểu đồ để phát hiện giá trị ngoại lai trước khi huấn luyện" },
            { "id": "c", "text": "Thay thế nhân viên kế toán quản trị trong việc viết báo cáo" },
            { "id": "d", "text": "Chỉ dùng để cài đặt mật khẩu cho cơ sở dữ liệu" }
        ],
        "correctAnswer": "b",
        "explanation": "Khám phá dữ liệu (EDA) là bước chuẩn bị, vẽ biểu đồ để hiểu rõ phân phối dữ liệu, tìm lỗi/ngoại lai trước khi đưa vào ML."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công nghệ thập niên với đặc trưng phân tích gian lận:",
        "left": [
            { "id": "l1", "text": "Thập niên 1980s (Hệ thống chuyên gia)" },
            { "id": "l2", "text": "Thập niên 2000s (Học máy tiên tiến)" },
            { "id": "l3", "text": "Thập niên 2020s (AI Tạo sinh)" }
        ],
        "right": [
            { "id": "r1", "text": "Chỉ chạy quy tắc tĩnh (If-Then), không thể tự học" },
            { "id": "r2", "text": "Chấm điểm rủi ro tự động nhưng thường rơi vào dạng hộp đen khó giải thích" },
            { "id": "r3", "text": "Có thể đọc hiểu biên bản cuộc họp và tự động viết báo cáo điều tra" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "80s: Rule-based. 2000s: Machine Learning black-boxes. 2020s: LLMs, GenAI NLP."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về các thuật toán trong Case Study 4:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Để phát hiện nhóm công ty 'sân sau' thông đồng thổi phồng giá trúng thầu để nhận <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, cơ quan quản lý đã áp dụng hệ thống phát hiện <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "tiền hoa hồng (kickbacks)" },
            { "id": "w2", "text": "bất thường (Anomaly Detection)" },
            { "id": "w3", "text": "nhân viên ma" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Bid-riggers thổi giá lên 25-40% để nhận kickbacks. Anomaly Detection (AI) phát hiện quy luật này."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Trình tự kỹ thuật tạo Biến Mục Tiêu (Target Creation) trong giám sát gian lận:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Ghi nhận mọi giao dịch chuyển tiền trong quá khứ" },
            { "id": "2", "text": "Đánh dấu (Label) các giao dịch sạch là số 0" },
            { "id": "3", "text": "Đánh dấu các giao dịch gian lận/vỡ nợ là số 1" },
            { "id": "4", "text": "Nạp tập dữ liệu 0 và 1 này vào mô hình Học có giám sát (Supervised ML)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Thu thập data -> Đánh nhãn 0 (hợp lệ) -> Đánh nhãn 1 (gian lận) -> Train supervised ML."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong Kinh tế học Phát triển (Development Economics), AI và dữ liệu viễn thông được dùng để làm gì?",
        "options": [
            { "id": "a", "text": "Theo dõi nội dung tin nhắn cá nhân của người dân" },
            { "id": "b", "text": "Lập bản đồ nghèo đói (Poverty Mapping) để phân bổ phúc lợi minh bạch" },
            { "id": "c", "text": "Chặn hoàn toàn các kết nối 5G ở khu vực nông thôn" },
            { "id": "d", "text": "Điều chỉnh lãi suất ngân hàng thương mại hàng tuần" }
        ],
        "correctAnswer": "b",
        "explanation": "Dữ liệu vệ sinh dịch tễ, viễn thông và điện năng tiêu thụ giúp AI vẽ bản đồ nghèo đói để chính phủ hỗ trợ đúng người yếu thế."
    }
]

import os

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day06\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the title and headers
content = content.replace("Bài Tập Trắc Nghiệm Buổi 1", "Bài Tập Trắc Nghiệm Buổi 6")
content = content.replace("kiến thức của Buổi 1", "kiến thức của Buổi 6")
content = content.replace("tài liệu Buổi 1", "tài liệu Buổi 6")

# Replace the questions array
json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 06 quiz updated with 30 new questions.")
