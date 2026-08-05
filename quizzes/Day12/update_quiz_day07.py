import re
import json

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Theo COSO (2013), có bao nhiêu thành phần chính trong hệ thống kiểm soát nội bộ?",
        "options": [
            { "id": "a", "text": "3 thành phần" },
            { "id": "b", "text": "5 thành phần" },
            { "id": "c", "text": "7 thành phần" },
            { "id": "d", "text": "17 thành phần" }
        ],
        "correctAnswer": "b",
        "explanation": "Kiểm soát nội bộ theo COSO gồm 5 thành phần: Môi trường kiểm soát, Đánh giá rủi ro, Hoạt động kiểm soát, Giám sát, Thông tin & Truyền thông."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Rủi ro kiểm soát nội bộ (Internal Controls Risk) khác với rủi ro tiềm tàng (Inherent Risk) ở điểm nào?",
        "options": [
            { "id": "a", "text": "Rủi ro kiểm soát phụ thuộc vào các quyết định quản lý của doanh nghiệp" },
            { "id": "b", "text": "Rủi ro kiểm soát luôn luôn không thể thay đổi hay quản lý được" },
            { "id": "c", "text": "Rủi ro kiểm soát chỉ liên quan đến các đối thủ cạnh tranh bên ngoài" },
            { "id": "d", "text": "Rủi ro kiểm soát phát sinh khi không có sự tồn tại của nhân viên" }
        ],
        "correctAnswer": "a",
        "explanation": "Rủi ro tiềm tàng gắn liền với ngành nghề kinh doanh, còn rủi ro kiểm soát là sản phẩm của cách ban quản lý thiết lập quy trình kiểm soát."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các loại rủi ro với định nghĩa của chúng:",
        "left": [
            { "id": "l1", "text": "Rủi ro tiềm tàng (Inherent Risk)" },
            { "id": "l2", "text": "Rủi ro kiểm soát (Control Risk)" },
            { "id": "l3", "text": "Rủi ro kiểm toán (Audit Risk)" }
        ],
        "right": [
            { "id": "r1", "text": "Rủi ro tồn tại tự nhiên khi chưa có bất kỳ biện pháp kiểm soát nào" },
            { "id": "r2", "text": "Rủi ro xảy ra do thiếu sót trong quy trình phòng ngừa của công ty" },
            { "id": "r3", "text": "Rủi ro tổng thể liên quan đến cả khả năng phát hiện của kiểm toán viên" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Audit Risk là hàm số của Inherent Risk, Control Risk, và Detection Risk."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp 4 Cấp độ Đánh giá Rủi ro Tự động từ ngoài vào trong:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Cấp độ 1: Từ ngoài vào trong (Dữ liệu công khai)" },
            { "id": "2", "text": "Cấp độ 2: Tập trung vào quy trình (Process centric)" },
            { "id": "3", "text": "Cấp độ 3: Rủi ro doanh nghiệp (Enterprise chuỗi giá trị)" },
            { "id": "4", "text": "Cấp độ 4: Quyết định kinh doanh (Business decisions)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Bốn cấp độ: Outside-in, Process centric, Enterprise, và Business decisions."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về Khai thác Quy trình (Process Mining):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Công nghệ Khai thác Quy trình (Process Mining) trích xuất <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> từ các hệ thống để kiểm tra dấu vết kiểm toán, xem ai đã truy cập hệ thống vào lúc nào. Điều này cho phép kiểm toán phân tích toàn bộ <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> dữ liệu thay vì chỉ chọn mẫu.",
        "words": [
            { "id": "w1", "text": "nhật ký sự kiện (event logs)" },
            { "id": "w2", "text": "tổng thể (population)" },
            { "id": "w3", "text": "biên bản giấy" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Process mining sử dụng log sự kiện (event logs) để phân tích 100% (toàn bộ tổng thể) thay vì lấy mẫu."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Trong đánh giá Môi trường Kiểm soát, phương pháp TF-IDF (Tần suất Thuật ngữ) được dùng để làm gì?",
        "options": [
            { "id": "a", "text": "Tính tần suất chữ ký của Giám đốc trên sổ cái" },
            { "id": "b", "text": "Xác định mức độ bao phủ của các quy định nội bộ" },
            { "id": "c", "text": "Tự động gửi email đòi nợ khách hàng" },
            { "id": "d", "text": "Quay video giám sát việc chấm công" }
        ],
        "correctAnswer": "b",
        "explanation": "TF-IDF phân tích các tài liệu chính sách và quy trình (NLP) để xem chúng có đề cập đủ đến các rủi ro cốt lõi không."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Hiệp hội ACFE chia gian lận thành 2 loại chính nào?",
        "options": [
            { "id": "a", "text": "Gian lận thẻ tín dụng và gian lận bảo hiểm" },
            { "id": "b", "text": "Gian lận nội bộ và gian lận bên ngoài" },
            { "id": "c", "text": "Tham nhũng và biển thủ tài sản" },
            { "id": "d", "text": "Sai sót vô ý và gian lận cố ý" }
        ],
        "correctAnswer": "b",
        "explanation": "ACFE phân chia thành gian lận từ bên trong (Internal fraud) và bên ngoài (External fraud)."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các mô hình quy trình với ý nghĩa thực tế:",
        "left": [
            { "id": "l1", "text": "Mô hình De jure (Theo quy chuẩn)" },
            { "id": "l2", "text": "Mô hình De facto (Trên thực tế)" },
            { "id": "l3", "text": "Bất đồng (Discrepancy)" }
        ],
        "right": [
            { "id": "r1", "text": "Mô tả cách làm việc chuẩn mực, mong muốn hoặc bắt buộc" },
            { "id": "r2", "text": "Cách quy trình thực sự đang diễn ra, kể cả những vi phạm" },
            { "id": "r3", "text": "Khoảng cách giữa lý thuyết và thực hành được AI phát hiện" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "De jure là chuẩn mực lý thuyết, De facto là những gì thực sự đang diễn ra. AI tìm sự khác biệt (Discrepancy) giữa hai mô hình này."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về Cây Gian lận (Fraud Tree):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Theo ACFE, gian lận nội bộ được chia làm ba nhánh lớn: Tham nhũng (Corruption), <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (Asset misappropriation), và Gian lận <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> (Financial statement fraud).",
        "words": [
            { "id": "w1", "text": "Biển thủ tài sản" },
            { "id": "w2", "text": "Báo cáo tài chính" },
            { "id": "w3", "text": "Thuế thu nhập" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "3 nhánh của Fraud Tree là: Corruption, Asset Misappropriation, và Financial Statement Fraud."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp 4 thành tố của Hình thoi Gian lận (Fraud Diamond) theo trình tự mô hình mở rộng:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Áp lực (Pressure/Motivation)" },
            { "id": "2", "text": "Cơ hội (Opportunity)" },
            { "id": "3", "text": "Sự biện minh (Rationalization)" },
            { "id": "4", "text": "Khả năng thực hiện (Capability)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Fraud Diamond thêm Capability vào 3 yếu tố gốc (Pressure, Opportunity, Rationalization)."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong Tam giác gian lận, AI phát hiện 'Cơ hội' (Opportunity) chủ yếu dựa vào việc đánh giá yếu tố nào?",
        "options": [
            { "id": "a", "text": "Giá cổ phiếu của các đối thủ trên sàn" },
            { "id": "b", "text": "Nhược điểm của hệ thống kiểm soát nội bộ" },
            { "id": "c", "text": "Tâm trạng buồn bực của nhân viên" },
            { "id": "d", "text": "Biến động của tỷ giá hối đoái quốc tế" }
        ],
        "correctAnswer": "b",
        "explanation": "Cơ hội cho gian lận được tạo ra khi có điểm yếu trong kiểm soát nội bộ (thiếu quy trình, văn hóa lỏng lẻo)."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Tự động hóa Đánh giá Kiểm soát Nội bộ trong kỷ nguyên AI kết hợp những công nghệ nào?",
        "options": [
            { "id": "a", "text": "Chỉ sử dụng máy tính bỏ túi (Calculator) và sổ tay" },
            { "id": "b", "text": "Chỉ dựa vào các bảng câu hỏi giấy được in sẵn" },
            { "id": "c", "text": "Khai thác quy trình, học máy và hệ chuyên gia" },
            { "id": "d", "text": "Máy fax, điện thoại cố định và băng từ lưu trữ" }
        ],
        "correctAnswer": "c",
        "explanation": "Chiến lược tự động hóa đòi hỏi Process mining, Machine learning, RPA, và Expert systems."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các loại phân tích Kiểm soát nội bộ với cách hoạt động:",
        "left": [
            { "id": "l1", "text": "Tập trung vào Dữ liệu (Data-centric)" },
            { "id": "l2", "text": "Tập trung vào Siêu dữ liệu (Metadata-centric)" },
            { "id": "l3", "text": "Dữ liệu + Siêu dữ liệu" }
        ],
        "right": [
            { "id": "r1", "text": "Kiểm tra ngân sách, dòng tiền và giao dịch kế toán thuần túy" },
            { "id": "r2", "text": "Kiểm tra nhật ký sự kiện, ai đăng nhập, lúc nào (Process Mining)" },
            { "id": "r3", "text": "Dùng học máy (ML) để phân loại bất thường từ nhật ký quy trình" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Data: Giao dịch kế toán. Metadata: Nhật ký truy cập hệ thống. Kết hợp cả 2: ML + Process Mining."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về rủi ro Biện minh (Rationalization):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Sự biện minh là sự tự lừa dối bản thân, nơi kẻ gian lận tự nhủ hành động sai trái là <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. AI sử dụng công nghệ phân tích <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> để dò tìm những mẫu giao tiếp bất thường trong email báo hiệu tâm lý này.",
        "words": [
            { "id": "w1", "text": "có thể chấp nhận được" },
            { "id": "w2", "text": "hành vi (behavior)" },
            { "id": "w3", "text": "hoàn toàn hợp pháp" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Sự biện minh coi gian lận là có thể chấp nhận được (ví dụ 'tôi chỉ mượn tạm'). AI phân tích hành vi để bắt mạch tâm lý này."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp 4 chữ cái đầu trong mô hình STOPSCAM của Viện Trí tuệ Nhân tạo Hoa Kỳ:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "S - Strategy (Chiến lược)" },
            { "id": "2", "text": "T - Transactions (Giao dịch)" },
            { "id": "3", "text": "O - Operations (Hoạt động)" },
            { "id": "4", "text": "P - Processes (Quy trình)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "STOPSCAM bắt đầu với S (Strategy), T (Transactions), O (Operations), P (Processes)."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Sự sụp đổ của công ty du lịch Thomas Cook (2019) cho thấy hạn chế gì của kiểm toán truyền thống?",
        "options": [
            { "id": "a", "text": "Kiểm toán viên không biết sử dụng phần mềm kế toán" },
            { "id": "b", "text": "Rủi ro kinh doanh không được đánh giá đúng mực" },
            { "id": "c", "text": "Họ quên thu thập hóa đơn bán hàng" },
            { "id": "d", "text": "Nhân viên công ty đã giả mạo chữ ký trên toàn bộ cổ phiếu" }
        ],
        "correctAnswer": "b",
        "explanation": "PwC và EY dù biết vấn đề rủi ro chiến lược kinh doanh của công ty nhưng vẫn ra báo cáo sạch (clean audit)."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các khía cạnh của COSO với ví dụ thực tiễn:",
        "left": [
            { "id": "l1", "text": "Mục tiêu: Tuân thủ luật pháp" },
            { "id": "l2", "text": "Mục tiêu: Báo cáo đáng tin cậy" },
            { "id": "l3", "text": "Môi trường kiểm soát" }
        ],
        "right": [
            { "id": "r1", "text": "Không trốn thuế và tuân thủ luật lao động" },
            { "id": "r2", "text": "Số liệu lợi nhuận đúng thực tế, không khai khống" },
            { "id": "r3", "text": "Văn hóa công ty, tính chính trực của Ban giám đốc" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Tuân thủ liên quan luật pháp. Báo cáo liên quan số liệu. Môi trường kiểm soát liên quan văn hóa."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Trong AI, khái niệm Human-in-the-loop đối với kiểm soát nội bộ nghĩa là gì?",
        "options": [
            { "id": "a", "text": "Chỉ có máy tính tự ra quyết định về các điểm yếu của hệ thống" },
            { "id": "b", "text": "Hệ thống AI không cần sự kiểm duyệt sau khi đã hoạt động" },
            { "id": "c", "text": "Con người luôn giám sát và kiểm duyệt các cảnh báo từ máy" },
            { "id": "d", "text": "Máy tính thay thế hoàn toàn mọi trách nhiệm của con người" }
        ],
        "correctAnswer": "c",
        "explanation": "Dù AI tự động hóa cao, quyết định và thẩm định cuối cùng vẫn cần sự đánh giá của Kế toán viên/Kiểm toán viên (Human-in-the-loop)."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ về hệ thống phát hiện gian lận tự động (IFFDI):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Kiểm soát nội bộ đóng vai trò là một <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để bảo vệ tài sản, tuy nhiên khi gian lận vẫn xảy ra, AI sẽ chuyển sang chức năng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> để khoanh vùng và phân tích lỗi.",
        "words": [
            { "id": "w1", "text": "bức tường lửa (firewall)" },
            { "id": "w2", "text": "phát hiện và điều tra" },
            { "id": "w3", "text": "công cụ tính thuế" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Kiểm soát nội bộ là phòng ngừa (bức tường lửa). Nếu thủng, chức năng điều tra (investigation) bằng AI sẽ tiếp quản."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Chữ 'C' trong mô hình STOPSCAM đại diện cho phân tích yếu tố nào?",
        "options": [
            { "id": "a", "text": "Chi phí kiểm toán thường niên của công ty khách hàng" },
            { "id": "b", "text": "Văn hóa công ty, ban quản trị và mạng lưới xã hội" },
            { "id": "c", "text": "Các thay đổi cấu trúc thuế thu nhập doanh nghiệp" },
            { "id": "d", "text": "Tỷ giá chuyển đổi ngoại tệ của thị trường" }
        ],
        "correctAnswer": "b",
        "explanation": "C = Culture (Văn hóa). Phân tích văn hóa công ty, sức ép từ CEO, độ tuân thủ của Ban giám đốc."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp 4 chữ cái cuối trong mô hình STOPSCAM:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "S - Statements (Báo cáo)" },
            { "id": "2", "text": "C - Culture (Văn hóa)" },
            { "id": "3", "text": "A - Attitudes (Thái độ)" },
            { "id": "4", "text": "M - Model (Mô hình)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "STOPSCAM: S (Statements), C (Culture), A (Attitude), M (Model)."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các thành phần Đánh giá Môi trường Kiểm soát với kỹ thuật AI:",
        "left": [
            { "id": "l1", "text": "Sự chính trực và Đạo đức" },
            { "id": "l2", "text": "Cấu trúc tổ chức & Quyền hạn" },
            { "id": "l3", "text": "Kiểm soát vật lý" }
        ],
        "right": [
            { "id": "r1", "text": "Dùng NLP phân tích từ ngữ trong MD&A và Biên bản họp" },
            { "id": "r2", "text": "Phân tích mạng lưới từ siêu dữ liệu Email nội bộ" },
            { "id": "r3", "text": "Phân tích Computer Vision (thị giác máy tính) từ camera" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Đạo đức thể hiện qua văn bản (NLP). Cấu trúc quyền lực thể hiện qua tần suất email. Kiểm soát vật lý dùng camera (Vision)."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Theo nghiên cứu của Simsek et al. (2018), họ đã làm gì với dữ liệu từ ngoài vào trong?",
        "options": [
            { "id": "a", "text": "Dự đoán giá cổ phiếu của các công ty công nghệ" },
            { "id": "b", "text": "Nhận diện rủi ro kiểm soát nội bộ từ báo cáo tài chính lịch sử" },
            { "id": "c", "text": "Phân loại các khoản lỗ tỷ giá hối đoái quốc tế" },
            { "id": "d", "text": "Gửi tự động bảng khảo sát rủi ro đến nhân viên" }
        ],
        "correctAnswer": "b",
        "explanation": "Nhóm nghiên cứu dùng tỷ số tài chính quá khứ để dự đoán MWIC (nhược điểm trọng yếu của kiểm soát nội bộ) với độ chính xác 70-80%."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về việc phân tích Quyền hạn (Authority):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong doanh nghiệp, <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> hệ thống (logs) từ các phần mềm ERP có thể chỉ ra việc phê duyệt có được thực hiện đúng người và đúng cấp độ hay không. Phân tích này là ứng dụng cốt lõi của <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "nhật ký truy cập" },
            { "id": "w2", "text": "khai thác quy trình" },
            { "id": "w3", "text": "sổ quỹ tiền mặt" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Nhật ký hệ thống (logs) được dùng trong Khai thác quy trình (Process Mining) để phân tích quyền hạn."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Quy trình ứng phó gian lận từ nhận diện đến quản lý:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Nhận diện điểm yếu của Kiểm soát nội bộ (Cơ hội gian lận)" },
            { "id": "2", "text": "Mô phỏng rủi ro (Risk Simulation) bằng công cụ AI" },
            { "id": "3", "text": "Giám sát tự động (Continuous Control Monitoring)" },
            { "id": "4", "text": "Đưa ra giải pháp khắc phục (Prescriptive remedies)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Nhận diện điểm yếu -> Mô phỏng tình huống -> Giám sát liên tục -> Báo cáo giải pháp."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Chữ T trong STOPSCAM là viết tắt của 'Transactions', nghĩa là AI sẽ kiểm tra gì?",
        "options": [
            { "id": "a", "text": "Hệ thống điện lạnh của doanh nghiệp" },
            { "id": "b", "text": "Toàn bộ dữ liệu giao dịch sổ cái (G/L) và bút toán" },
            { "id": "c", "text": "Danh sách nhân viên mới gia nhập công ty" },
            { "id": "d", "text": "Chiến lược tiếp thị sản phẩm mới" }
        ],
        "correctAnswer": "b",
        "explanation": "Transactions (giao dịch) liên quan đến kiểm tra dữ liệu bút toán nhật ký, sổ cái."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công nghệ AI với lĩnh vực kiểm soát rủi ro:",
        "left": [
            { "id": "l1", "text": "NLP (Xử lý Ngôn ngữ Tự nhiên)" },
            { "id": "l2", "text": "Computer Vision (Thị giác máy tính)" },
            { "id": "l3", "text": "Unsupervised ML (Học không giám sát)" }
        ],
        "right": [
            { "id": "r1", "text": "Phân tích thái độ qua nội dung Email/Biên bản họp" },
            { "id": "r2", "text": "Phân tích camera hành vi trộm cắp ở nhà kho" },
            { "id": "r3", "text": "Gom cụm phát hiện các hóa đơn thanh toán lạ" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "NLP phân tích chữ. Computer Vision phân tích video/ảnh. Unsupervised ML gom cụm dữ liệu giao dịch."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về Khả năng (Capability) trong gian lận:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Khả năng xảy ra gian lận lớn khi một cá nhân tin rằng họ có quyền lực hoặc năng lực để che giấu hành vi. AI đánh giá <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> của cá nhân này qua dữ liệu nhân sự (HR) và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> để xem họ có đủ sức thao túng hệ thống hay không.",
        "words": [
            { "id": "w1", "text": "mức độ trọng yếu (materiality)" },
            { "id": "w2", "text": "mạng lưới xã hội (social network)" },
            { "id": "w3", "text": "báo cáo tài chính" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Khả năng/quyền lực được phân tích thông qua tác động trọng yếu và mạng lưới quan hệ nội bộ của cá nhân."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp quá trình AI phát triển từ dữ liệu thô đến đề xuất hành động (Analytics):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Mô tả: AI thống kê điều gì đã xảy ra từ sổ kế toán" },
            { "id": "2", "text": "Dự đoán: AI dự đoán gian lận nào có thể xảy ra sắp tới" },
            { "id": "3", "text": "Đề xuất: AI tự động chặn tài khoản nghi ngờ (Prescriptive)" },
            { "id": "4", "text": "Giám sát: Kế toán viên đánh giá hiệu quả giải pháp AI" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Phân tích dữ liệu đi từ Descriptive -> Predictive -> Prescriptive -> Monitoring."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Theo nghiên cứu, việc ban quản lý tích cực sử dụng AI để tìm hiểu 'rủi ro mới nổi' (emergent risks) cho thấy điều gì?",
        "options": [
            { "id": "a", "text": "Sự yếu kém trong năng lực tài chính của nhân sự" },
            { "id": "b", "text": "Ban quản lý chủ động bảo vệ công ty trước sai sót" },
            { "id": "c", "text": "Công ty đang chuẩn bị hồ sơ đệ đơn phá sản" },
            { "id": "d", "text": "Sự lãng phí tiền bạc vào các phần mềm AI đắt đỏ" }
        ],
        "correctAnswer": "b",
        "explanation": "Khi ban quản lý chủ động dùng công nghệ phân tích rủi ro mới, đó là dấu hiệu của môi trường kiểm soát mạnh, chủ động ngăn ngừa lỗi."
    }
]

import os

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day07\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the title and headers
content = content.replace("Bài Tập Trắc Nghiệm Buổi 1", "Bài Tập Trắc Nghiệm Buổi 7")
content = content.replace("kiến thức của Buổi 1", "kiến thức của Buổi 7")
content = content.replace("tài liệu Buổi 1", "tài liệu Buổi 7")

# Replace the questions array
json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 07 quiz updated with 30 new questions.")
