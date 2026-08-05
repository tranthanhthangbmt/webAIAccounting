import re
import json
import os

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Gian lận nhấp chuột vào quảng cáo (Ad click fraud) nhằm mục đích gì trong chiến dịch kỹ thuật số?",
        "options": [
            { "id": "a", "text": "Thao túng phân tích quảng cáo và thu nhập PPC" },
            { "id": "b", "text": "Cải thiện trải nghiệm của khách hàng mua hàng" },
            { "id": "c", "text": "Làm cho hình ảnh sản phẩm trở nên đẹp đẽ hơn" },
            { "id": "d", "text": "Giảm lượng tiêu thụ điện năng của máy chủ web" }
        ],
        "correctAnswer": "a",
        "explanation": "Lừa đảo nhấp chuột vào quảng cáo thao túng mô hình PPC (Pay-per-click) để làm cạn kiệt ngân sách của đối thủ hoặc kiếm tiền bất chính."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Theo báo cáo, phương thức tấn công xếp chồng quảng cáo (Ad stacking) hoạt động như thế nào?",
        "options": [
            { "id": "a", "text": "Nhiều quảng cáo xếp lớp lên nhau trong một vị trí" },
            { "id": "b", "text": "Gửi hàng triệu email rác cho khách hàng cũ" },
            { "id": "c", "text": "Sao chép mã nguồn của trang web đối thủ" },
            { "id": "d", "text": "In nhiều tờ rơi quảng cáo ở định dạng giấy" }
        ],
        "correctAnswer": "a",
        "explanation": "Xếp chồng quảng cáo là khi nhiều quảng cáo được xếp lớp trong một vị trí duy nhất, người dùng chỉ thấy lớp trên cùng nhưng nhấp chuột đăng ký cho tất cả."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép nối các loại gian lận quảng cáo với đặc điểm của chúng:",
        "left": [
            { "id": "l1", "text": "Bot tự động" },
            { "id": "l2", "text": "Bấm vào trang trại (Click farm)" },
            { "id": "l3", "text": "Nhà xuất bản lừa đảo" }
        ],
        "right": [
            { "id": "r1", "text": "Tập lệnh được lập trình để mô phỏng con người" },
            { "id": "r2", "text": "Nhóm cá nhân nhấp chuột thủ công số lượng lớn" },
            { "id": "r3", "text": "Chủ trang web tự nhấp để tăng thu nhập giả tạo" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Bot dùng phần mềm, Click farm dùng sức người giá rẻ, Nhà xuất bản tự nhấp để kiếm tiền bất chính."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp quy trình ứng dụng AI trong bảo lãnh khoản vay (Loan Underwriting):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập dữ liệu mạng xã hội và thương mại điện tử" },
            { "id": "2", "text": "Phân tích mẫu hành vi và thông tin vị trí, giao dịch" },
            { "id": "3", "text": "Hệ thống AI tạo ra xác suất vỡ nợ của người nộp đơn" },
            { "id": "4", "text": "Chuyển khoản vay vào ví điện tử trong 15 phút" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quy trình bảo lãnh khoản vay bằng AI: Thu thập -> Phân tích hành vi -> Tính xác suất vỡ nợ -> Cấp vốn tự động."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về Giao dịch thuật toán bằng AI:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Khác với giao dịch định lượng truyền thống, AI có khả năng hoạt động như một <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> tham gia thị trường. Công cụ <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> giúp máy phân tích báo cáo tin tức để dự báo tâm lý quản lý.",
        "words": [
            { "id": "w1", "text": "đại lý độc lập" },
            { "id": "w2", "text": "NLP (Xử lý ngôn ngữ tự nhiên)" },
            { "id": "w3", "text": "kế toán viên phụ tá" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "AI trong trading hoạt động như đại lý độc lập, sử dụng NLP để phân tích tin tức và cảm xúc."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Học chuyển giao (Transfer learning) trong phát hiện gian lận mang lại lợi ích gì?",
        "options": [
            { "id": "a", "text": "Áp dụng mô hình gian lận này sang miền gian lận khác" },
            { "id": "b", "text": "Chuyển tiền của kẻ lừa đảo lại cho người bị hại" },
            { "id": "c", "text": "Đào tạo nhân viên mới qua các khóa học trực tuyến" },
            { "id": "d", "text": "Xóa toàn bộ các dữ liệu lịch sử để bảo mật hệ thống" }
        ],
        "correctAnswer": "a",
        "explanation": "Học chuyển giao (Transfer learning) là quá trình vận dụng kiến thức từ một miền (ví dụ gian lận thẻ tín dụng) để cải thiện mô hình phát hiện ở miền khác."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Công nghệ nào được dùng để trích xuất văn bản từ hình ảnh hóa đơn lừa đảo?",
        "options": [
            { "id": "a", "text": "Nhận dạng ký tự quang học (OCR)" },
            { "id": "b", "text": "Công cụ tìm kiếm thông tin" },
            { "id": "c", "text": "Máy chiếu slide bài giảng" },
            { "id": "d", "text": "Giao thức truyền tập tin mạng" }
        ],
        "correctAnswer": "a",
        "explanation": "OCR (Optical Character Recognition) được sử dụng để đọc chữ trên hình ảnh tài liệu."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các công nghệ với vai trò tương ứng trong phát hiện gian lận:",
        "left": [
            { "id": "l1", "text": "Xử lý Ngôn ngữ Tự nhiên (NLP)" },
            { "id": "l2", "text": "AI có thể giải thích (Explainable AI)" },
            { "id": "l3", "text": "Blockchain (DLT)" }
        ],
        "right": [
            { "id": "r1", "text": "Tìm kiếm lỗi ngữ pháp, bất thường từ ngữ trong hóa đơn" },
            { "id": "r2", "text": "Làm rõ quyết định hộp đen để tuân thủ quy định đạo đức" },
            { "id": "r3", "text": "Tạo sổ cái bất biến chống lại việc sửa đổi giao dịch" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "NLP phân tích văn bản, Explainable AI minh bạch hóa thuật toán, Blockchain tạo sổ cái bất biến."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về Cố vấn Robot (Robo-Advisors):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Cố vấn robot cung cấp dịch vụ đầu tư tài chính <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Mô hình lai kết hợp tư vấn truyền thống và robot được kỳ vọng sẽ trở thành <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> trên thị trường.",
        "words": [
            { "id": "w1", "text": "tự động dựa trên thuật toán" },
            { "id": "w2", "text": "người chiến thắng" },
            { "id": "w3", "text": "chiến lược lỗi thời" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Robo-advisors tự động hóa đầu tư, mô hình hybrid (lai) được dự báo là người chiến thắng."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp các bước Phân tích Tên miền chéo (Cross-domain Analysis) trong phát hiện gian lận:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập dữ liệu giao dịch nội bộ và hồ sơ khách hàng" },
            { "id": "2", "text": "Tích hợp với dữ liệu thị trường và chỉ số kinh tế vĩ mô" },
            { "id": "3", "text": "Sử dụng ML để tìm sự khác thường giữa các miền dữ liệu" },
            { "id": "4", "text": "Cảnh báo sớm gian lận mà không thể thấy ở từng miền lẻ" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Cross-domain kết hợp dữ liệu nhiều nguồn (nội bộ, vĩ mô) dùng ML để phát hiện dấu hiệu cảnh báo sớm."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Cuộc tấn công đối nghịch (Adversarial attacks) nhắm vào mô hình AI là gì?",
        "options": [
            { "id": "a", "text": "Thay đổi dữ liệu đầu vào để đánh lừa mô hình AI" },
            { "id": "b", "text": "Gửi email nặc danh tống tiền lãnh đạo doanh nghiệp" },
            { "id": "c", "text": "Làm quá tải máy chủ bằng các lệnh truy cập liên tục" },
            { "id": "d", "text": "Cắt đứt đường truyền cáp quang của tòa nhà máy chủ" }
        ],
        "correctAnswer": "a",
        "explanation": "Adversarial attacks cố tình thay đổi dữ liệu đầu vào một cách tinh vi để AI phân loại sai."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Generative AI (AI Tạo sinh) giúp gì trong việc giảm thiểu rủi ro gian lận?",
        "options": [
            { "id": "a", "text": "Sản xuất dữ liệu tổng hợp để đào tạo mô hình gian lận" },
            { "id": "b", "text": "In hóa đơn giả mạo để kiểm tra độ nhạy của nhân viên" },
            { "id": "c", "text": "Thiết kế logo mới cho hệ thống nhận diện thương hiệu" },
            { "id": "d", "text": "Đánh bóng hình ảnh công ty trên các phương tiện báo chí" }
        ],
        "correctAnswer": "a",
        "explanation": "Gian lận thực tế ('Thiên nga đen') rất hiếm, Generative AI tạo dữ liệu mô phỏng để huấn luyện hệ thống phòng thủ."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép nối các công nghệ với ví dụ thực tiễn trong tài chính:",
        "left": [
            { "id": "l1", "text": "Chatbots" },
            { "id": "l2", "text": "Hệ thống AI 'Quyền anh trắng' (White-boxing)" },
            { "id": "l3", "text": "Máy học (Machine Learning)" }
        ],
        "right": [
            { "id": "r1", "text": "Hỗ trợ khách hàng gọi taxi, chuyển tiền trên WeChat" },
            { "id": "r2", "text": "Phát hiện gian lận bằng cách tính toán điểm minh bạch" },
            { "id": "r3", "text": "Học từ dữ liệu giao dịch lịch sử để dự báo gian lận" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Chatbot để tương tác, White-boxing giúp minh bạch cách chấm điểm, ML dùng để học dữ liệu."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về sự thiên vị (Bias) trong mô hình AI:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Sự <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> trong dữ liệu đào tạo AI có thể dẫn đến kết quả không công bằng hoặc phân biệt đối xử. Để giải quyết, tổ chức cần thực hiện quá trình tiền xử lý dữ liệu và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> mô hình liên tục.",
        "words": [
            { "id": "w1", "text": "thiên vị (bias)" },
            { "id": "w2", "text": "hiệu chỉnh (calibration)" },
            { "id": "w3", "text": "tuyệt đối hóa" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Sự thiên vị (Bias) yêu cầu phải hiệu chuẩn và tiền xử lý dữ liệu (Calibration) liên tục."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp lịch sử phát triển của phát hiện gian lận tài chính:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Kiểm toán thủ công bằng sổ sách giấy tờ" },
            { "id": "2", "text": "Hệ thống chuyên gia dựa trên quy tắc (Rule-based)" },
            { "id": "3", "text": "Mô hình Học máy (Machine Learning) nhận diện tự động" },
            { "id": "4", "text": "Mô hình AI dự đoán và AI tạo sinh (Generative AI)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Từ thủ công -> Dựa trên quy tắc cố định -> ML thích ứng -> AI dự đoán/tạo sinh tiên tiến."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Tại sao hệ thống phát hiện gian lận dựa trên quy tắc (rule-based) lại bộc lộ nhiều điểm yếu hiện nay?",
        "options": [
            { "id": "a", "text": "Chúng không thể phát hiện các kiểu gian lận chưa từng có" },
            { "id": "b", "text": "Luôn yêu cầu phải có kết nối mạng Internet 5G" },
            { "id": "c", "text": "Nhân sự không biết lập trình các câu lệnh If-Else" },
            { "id": "d", "text": "Chi phí mua hệ thống máy chủ quá đắt đỏ và tốn kém" }
        ],
        "correctAnswer": "a",
        "explanation": "Hệ thống Rule-based không thể nhận diện các phương thức gian lận mới tinh vi (không nằm trong tập quy tắc đã biết)."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các quy định pháp lý (Regulatory compliance) với ý nghĩa:",
        "left": [
            { "id": "l1", "text": "AML" },
            { "id": "l2", "text": "KYC" },
            { "id": "l3", "text": "PCI DSS" }
        ],
        "right": [
            { "id": "r1", "text": "Các biện pháp phòng chống rửa tiền (Anti-Money Laundering)" },
            { "id": "r2", "text": "Quy tắc nhận biết khách hàng (Know Your Customer)" },
            { "id": "r3", "text": "Tiêu chuẩn bảo mật dữ liệu ngành thẻ thanh toán" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "AML = Anti-Money Laundering; KYC = Know Your Customer; PCI DSS = Payment Card Industry Data Security Standard."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Mô hình 'Thiên nga đen' (Black Swan) trong phát hiện gian lận ám chỉ điều gì?",
        "options": [
            { "id": "a", "text": "Sự kiện hiếm khi xảy ra nhưng gây tổn thất thảm khốc" },
            { "id": "b", "text": "Sự kiện thường xuyên xảy ra với mức thiệt hại siêu nhỏ" },
            { "id": "c", "text": "Hiện tượng khách hàng rút tiền đồng loạt khỏi ngân hàng" },
            { "id": "d", "text": "Thuật toán chuyên phát hiện các lỗi đánh máy tài liệu" }
        ],
        "correctAnswer": "a",
        "explanation": "Black Swan events (Thiên nga đen) là các sự kiện gian lận quy mô lớn, hiếm xảy ra nhưng thiệt hại khổng lồ."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ về rủi ro đạo đức trong AI:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong ngành tài chính, các tổ chức phải đảm bảo AI tuân thủ đạo đức, không phân biệt đối xử và <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Tính <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> là bắt buộc để người dùng hiểu được quá trình AI ra quyết định.",
        "words": [
            { "id": "w1", "text": "bảo mật quyền riêng tư" },
            { "id": "w2", "text": "minh bạch (transparency)" },
            { "id": "w3", "text": "phức tạp (complexity)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "AI phải bảo mật quyền riêng tư và đảm bảo tính minh bạch để có thể giải thích được."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong AI Algorithmic Trading, AI sử dụng dữ liệu phi cấu trúc nào để xác định xu hướng đầu tư?",
        "options": [
            { "id": "a", "text": "Tin tức, blog và mạng xã hội" },
            { "id": "b", "text": "Bảng cân đối kế toán nội bộ" },
            { "id": "c", "text": "Danh sách mã số thuế" },
            { "id": "d", "text": "Biên lai chi phí tiền điện" }
        ],
        "correctAnswer": "a",
        "explanation": "AI Trading phân tích dữ liệu phi cấu trúc như mạng xã hội, báo cáo tin tức để đoán tâm lý thị trường."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp quá trình AI phát hiện gian lận Thẻ Tín Dụng:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Ghi nhận dữ liệu thẻ (số tiền, địa điểm, thời gian)" },
            { "id": "2", "text": "Máy học đối chiếu với thói quen tiêu dùng lịch sử" },
            { "id": "3", "text": "Xác định sai lệch (VD: quẹt thẻ tại 2 quốc gia cùng lúc)" },
            { "id": "4", "text": "Cảnh báo và tự động khóa thẻ tạm thời" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quy trình: Thu thập -> Đối chiếu lịch sử -> Xác định sai lệch -> Đưa ra hành động cảnh báo."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các khái niệm kỹ thuật với ứng dụng tài chính:",
        "left": [
            { "id": "l1", "text": "Khả năng mở rộng (Scalability)" },
            { "id": "l2", "text": "Độ bền của mô hình (Robustness)" },
            { "id": "l3", "text": "False Positive (Dương tính giả)" }
        ],
        "right": [
            { "id": "r1", "text": "Xử lý khối lượng giao dịch cực lớn trong thời gian thực" },
            { "id": "r2", "text": "Phòng thủ trước các cuộc tấn công đối nghịch vào dữ liệu" },
            { "id": "r3", "text": "Nhận diện nhầm giao dịch hợp pháp thành gian lận" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Scalability là tốc độ/quy mô xử lý, Robustness là sự bền bỉ trước tấn công, False positive là khóa nhầm thẻ."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Sự khác biệt quan trọng giữa Robot-Advisor (cố vấn robot) và các nhà quản lý quỹ truyền thống là gì?",
        "options": [
            { "id": "a", "text": "Tự động phân bổ danh mục dựa trên thuật toán và dữ liệu" },
            { "id": "b", "text": "Robot-Advisor luôn cam kết sinh lời 100% không rủi ro" },
            { "id": "c", "text": "Hoạt động hoàn toàn bằng năng lượng mặt trời" },
            { "id": "d", "text": "Bỏ qua các nguyên tắc tính toán tài chính cơ bản" }
        ],
        "correctAnswer": "a",
        "explanation": "Robo-advisor sử dụng thuật toán phân bổ danh mục tự động và tiết kiệm chi phí nhân sự."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về tác dụng của AI trong Tuân thủ quy định (RegTech):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Hệ thống AI giám sát quy định có thể tự động kiểm tra <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> theo tiêu chuẩn KYC (Nhận biết khách hàng) và quét giao dịch để phát hiện dấu hiệu của việc <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "danh tính khách hàng" },
            { "id": "w2", "text": "rửa tiền (AML)" },
            { "id": "w3", "text": "thay đổi lãi suất" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "AI trong RegTech giúp định danh KYC và quét dấu hiệu rửa tiền AML."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp quá trình AI phân tích tài liệu phân phối trong Thương mại điện tử:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Nhận hình ảnh hóa đơn, lệnh vận chuyển từ hệ thống" },
            { "id": "2", "text": "Dùng OCR để trích xuất chữ và NLP để kiểm tra văn phong" },
            { "id": "3", "text": "Phát hiện độ lệch (VD: sai giá, sai số lượng) bằng ML" },
            { "id": "4", "text": "Chuyên viên con người đánh giá lại (Human-in-the-loop)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Thu hình ảnh -> OCR/NLP trích xuất -> Nhận diện sai lệch -> Con người xác minh."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Lĩnh vực Tài chính Ngân hàng sử dụng GRC để quản lý cái gì?",
        "options": [
            { "id": "a", "text": "Quản trị, Quản lý rủi ro và Tuân thủ (Governance, Risk, Compliance)" },
            { "id": "b", "text": "Tăng trưởng, Doanh thu và Chi phí (Growth, Revenue, Cost)" },
            { "id": "c", "text": "Giao tiếp, Đánh giá và Cạnh tranh" },
            { "id": "d", "text": "Khai thác vàng, Đọc sách và Ghi chép" }
        ],
        "correctAnswer": "a",
        "explanation": "GRC viết tắt của Governance, Risk management, and Compliance."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép cặp rủi ro và cách khắc phục khi sử dụng AI:",
        "left": [
            { "id": "l1", "text": "Dữ liệu huấn luyện bị định kiến (Bias)" },
            { "id": "l2", "text": "Vi phạm quyền riêng tư khách hàng" },
            { "id": "l3", "text": "Thuật toán hoạt động như 'hộp đen'" }
        ],
        "right": [
            { "id": "r1", "text": "Hiệu chỉnh dữ liệu để đảm bảo tính công bằng (Fairness)" },
            { "id": "r2", "text": "Mã hóa dữ liệu và tuân thủ chặt chẽ quyền riêng tư" },
            { "id": "r3", "text": "Sử dụng các mô hình AI có thể giải thích (Explainable AI)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Bias cần Fairness; Quyền riêng tư cần mã hóa; Hộp đen cần Explainable AI."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về khả năng tổng hợp dữ liệu của Generative AI:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Do gian lận là các sự kiện hiếm, Generative AI có thể được sử dụng trong mạng biệt lập để <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> dữ liệu mô phỏng. Việc này giúp cải thiện <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> của mô hình mà không cần chờ đợi gian lận thực xảy ra.",
        "words": [
            { "id": "w1", "text": "tạo ra (generate)" },
            { "id": "w2", "text": "độ nhạy bén (accuracy)" },
            { "id": "w3", "text": "xóa bỏ hoàn toàn" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Generative AI tạo dữ liệu giả lập để tăng độ nhạy bén cho bộ máy phát hiện gian lận."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp cấu trúc các chương trình tự động hóa tương tác tài chính từ đơn giản đến phức tạp:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Chatbot quy tắc quét từ khóa cơ bản (Rule-based Bot)" },
            { "id": "2", "text": "Chatbot sử dụng NLP hiểu ý định người dùng (NLP Bot)" },
            { "id": "3", "text": "Robo-advisor phân bổ danh mục đầu tư bán tự động" },
            { "id": "4", "text": "AI Algorithmic Trading độc lập ra quyết định mua bán" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Từ cấp thấp (rule chatbot) -> NLP chatbot -> Robo-advisor -> Thuật toán Trading siêu tốc."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Sự xuất hiện của 'Deep Learning' (Học sâu) mang lại bước tiến gì cho ngành ngân hàng?",
        "options": [
            { "id": "a", "text": "Xác định các cấu trúc mạng lưới ẩn, phức tạp của gian lận" },
            { "id": "b", "text": "Làm cho phần cứng máy tính trở nên nhẹ và rẻ tiền hơn" },
            { "id": "c", "text": "Giảm lượng dữ liệu cần thiết để kiểm toán doanh nghiệp" },
            { "id": "d", "text": "In sao kê ngân hàng nhanh hơn trên giấy A4" }
        ],
        "correctAnswer": "a",
        "explanation": "Học sâu (Deep Learning) sử dụng mạng nơ-ron giúp ngân hàng phát hiện các mẫu gian lận tinh vi, phức tạp."
    }
]

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day08\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Bài Tập Trắc Nghiệm Buổi 7", "Bài Tập Trắc Nghiệm Buổi 8")
content = content.replace("kiến thức của Buổi 7", "kiến thức của Buổi 8")
content = content.replace("tài liệu Buổi 7", "tài liệu Buổi 8")

json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 08 quiz updated with 30 new questions.")
