import re
import json

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Mạng nơ-ron nhân tạo (ANNs) thường được sử dụng cho mục đích gì?",
        "options": [
            { "id": "a", "text": "Phân tích báo cáo tài chính thủ công" },
            { "id": "b", "text": "Nhận dạng mẫu (pattern recognition) như nhận dạng khuôn mặt và giọng nói" },
            { "id": "c", "text": "In ấn tài liệu" },
            { "id": "d", "text": "Chỉ dùng để gửi email tự động" }
        ],
        "correctAnswer": "b",
        "explanation": "ANNs thường được sử dụng cho nhận dạng mẫu như nhận dạng khuôn mặt trong hình ảnh và video, nhận dạng giọng nói, mạng xã hội, v.v."
    },
    # 2. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp quá trình hoạt động của Xử lý Ngôn ngữ Tự nhiên (NLP) khi Siri trả lời câu hỏi về thời tiết:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Người dùng đặt câu hỏi: 'Này Siri, thời tiết thế nào?'" },
            { "id": "2", "text": "NLU (Hiểu ngôn ngữ tự nhiên) giúp Siri hiểu yêu cầu của người dùng" },
            { "id": "3", "text": "Siri tìm kiếm thông tin thời tiết trên Internet" },
            { "id": "4", "text": "NLG (Tạo ngôn ngữ tự nhiên) chuyển dữ liệu thời tiết thành câu trả lời bằng giọng nói để phản hồi người dùng" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "NLP gồm hai phần: NLU (để máy tính hiểu người) và NLG (để máy tính nói lại cho người hiểu)."
    },
    # 3. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép nối các khái niệm về xử lý dữ liệu và ngôn ngữ với định nghĩa của chúng:",
        "left": [
            { "id": "l1", "text": "NLU (Hiểu ngôn ngữ tự nhiên)" },
            { "id": "l2", "text": "NLG (Tạo ngôn ngữ tự nhiên)" },
            { "id": "l3", "text": "Text mining (Khai phá văn bản)" }
        ],
        "right": [
            { "id": "r1", "text": "Cho phép máy tính hiểu các hướng dẫn được cung cấp bằng ngôn ngữ của con người" },
            { "id": "r2", "text": "Chuyển đổi dữ liệu và kết quả thành mô tả bằng lời nói mà con người có thể hiểu được" },
            { "id": "r3", "text": "Trích xuất thông tin từ các nguồn văn bản phi cấu trúc (email, pdf) để khám phá mẫu/chủ đề" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "NLU là máy hiểu người, NLG là máy giao tiếp với người, Text mining là trích xuất insight từ tài liệu văn bản."
    },
    # 4. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ thích hợp nói về sự khác biệt giữa Khai phá dữ liệu và Học máy (theo Bernard Marr):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Khai phá dữ liệu tìm kiếm các mẫu đã tồn tại trong <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, trong khi học máy cố gắng dự đoán các kết quả trong tương lai. Khai phá dữ liệu dựa vào sự can thiệp của <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> trong suốt quá trình, trong khi phần lớn quá trình học tập với học máy là tự động.",
        "words": [
            { "id": "w1", "text": "dữ liệu lịch sử (historical data)" },
            { "id": "w2", "text": "con người" },
            { "id": "w3", "text": "thuật toán" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Khai phá dữ liệu phân tích dữ liệu lịch sử và cần nhiều sự can thiệp phân tích của con người hơn học máy tự động."
    },
    # 5. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Nhà nghiên cứu Sophia Sun (2019) đã thúc đẩy việc sử dụng học sâu (DL) trong kiểm toán vào 2 lĩnh vực chính nào?",
        "options": [
            { "id": "a", "text": "Kiểm kê kho bãi và tính lương" },
            { "id": "b", "text": "Xác định thông tin (từ dữ liệu văn bản, hình ảnh, âm thanh) và hỗ trợ đánh giá (ra quyết định)" },
            { "id": "c", "text": "Thiết kế website và quảng cáo trên mạng xã hội" },
            { "id": "d", "text": "Tự động hóa hoàn toàn việc sa thải nhân viên" }
        ],
        "correctAnswer": "b",
        "explanation": "Sun (2019) thúc đẩy việc sử dụng học sâu để hỗ trợ ra quyết định kiểm toán trong hai lĩnh vực chính: xác định thông tin và hỗ trợ đánh giá."
    },
    # 6. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "RPA (Tự động hóa quy trình bằng robot) rất phù hợp với loại công việc nào?",
        "options": [
            { "id": "a", "text": "Các công việc mang tính sáng tạo cao, thay đổi liên tục" },
            { "id": "b", "text": "Các tác vụ có khối lượng lớn, lặp đi lặp lại thường do con người thực hiện (vd: đối chiếu ngân hàng, xử lý hóa đơn)" },
            { "id": "c", "text": "Các công việc cần sự đồng cảm và thấu hiểu tâm lý khách hàng" },
            { "id": "d", "text": "Khám phá các mô hình dữ liệu chưa từng được biết đến" }
        ],
        "correctAnswer": "b",
        "explanation": "RPA là một ứng dụng phần mềm tự động hóa các quy trình kinh doanh bằng cách lặp lại các hành động của con người, rất phù hợp cho các tác vụ lặp đi lặp lại."
    },
    # 7. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công cụ / nền tảng với chức năng / đặc điểm của chúng:",
        "left": [
            { "id": "l1", "text": "TPU (Bộ xử lý tensor)" },
            { "id": "l2", "text": "API (Giao diện lập trình ứng dụng)" },
            { "id": "l3", "text": "UiPath, Automation Anywhere" }
        ],
        "right": [
            { "id": "r1", "text": "Mạch chuyên dụng do Google phát triển để tăng tốc độ xử lý cho ứng dụng AI/ML" },
            { "id": "r2", "text": "Đóng vai trò như 'người đưa tin', cho phép các phần mềm và nền tảng khác nhau giao tiếp với nhau" },
            { "id": "r3", "text": "Các nhà cung cấp phần mềm hàng đầu trong lĩnh vực tự động hóa RPA" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "TPU tăng tốc AI. API kết nối phần mềm. UiPath là phần mềm RPA phổ biến."
    },
    # 8. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp quy trình khai phá văn bản (Text mining) được mô tả trong tài liệu:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập các nguồn văn bản phi cấu trúc (ví dụ: hợp đồng, email, bài đăng MXH)" },
            { "id": "2", "text": "Áp đặt cấu trúc (structure) lên các nguồn dữ liệu văn bản phi cấu trúc này" },
            { "id": "3", "text": "Sử dụng các kỹ thuật khai phá dữ liệu để trích xuất thông tin liên quan (khái niệm, mẫu, xu hướng)" },
            { "id": "4", "text": "Ứng dụng thông tin đó (vd: phát hiện từ ngữ buộc tội trong kế toán pháp y)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quá trình 2 bước: 1. Áp đặt cấu trúc lên văn bản, 2. Sử dụng kỹ thuật khai phá để trích xuất thông tin, sau đó là ứng dụng."
    },
    # 9. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ thích hợp liên quan đến ngôn ngữ lập trình cho kế toán viên:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Sự thành thạo các công cụ lập trình mã nguồn mở (open-source) phổ biến cho AI, chẳng hạn như <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>, sẽ cho phép các kế toán viên tùy chỉnh các ứng dụng AI.",
        "words": [
            { "id": "w1", "text": "Python" },
            { "id": "w2", "text": "R" },
            { "id": "w3", "text": "HTML" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Python và R là 2 ngôn ngữ phổ biến nhất được khuyên học cho Data Science và AI."
    },
    # 10. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Sự kiện thị trường 'Sự cố chớp nhoáng' (flash crash) ngày 6 tháng 5 năm 2010 đã làm giảm 1000 điểm Dow Jones trong vài phút được cho là do đâu?",
        "options": [
            { "id": "a", "text": "Do sự sụp đổ của một ngân hàng ảo trên Metaverse" },
            { "id": "b", "text": "Do giao dịch thuật toán tần suất cao (Algorithmic trading) gây thao túng và mất ổn định thị trường" },
            { "id": "c", "text": "Do rò rỉ dữ liệu của Equifax" },
            { "id": "d", "text": "Do một chatbot AI tư vấn sai cho khách hàng" }
        ],
        "correctAnswer": "b",
        "explanation": "Giao dịch thuật toán tần suất cao đã kích hoạt đợt bán tháo tự động dây chuyền, gây ra flash crash."
    },
    # 11. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Trong trường hợp của Ngân hàng HDFC, việc sử dụng học máy để chấm điểm tín dụng đã làm dấy lên vấn đề đạo đức nào lớn nhất?",
        "options": [
            { "id": "a", "text": "Quyền riêng tư dữ liệu" },
            { "id": "b", "text": "Thao túng thị trường" },
            { "id": "c", "text": "Sự thiên vị (biases) dẫn đến phân biệt đối xử trong các lựa chọn cho vay" },
            { "id": "d", "text": "Mất việc làm của nhân viên ngân hàng" }
        ],
        "correctAnswer": "c",
        "explanation": "Nghiên cứu chỉ ra rằng các đánh giá của thuật toán AI chấm điểm tín dụng đôi khi bị thiên vị, gây ra sự phân biệt đối xử khi cấp khoản vay."
    },
    # 12. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép tên các doanh nghiệp/tổ chức với vấn đề hoặc công nghệ cốt lõi mà họ gặp phải (trong Case Study):",
        "left": [
            { "id": "l1", "text": "Ngân hàng ICICI" },
            { "id": "l2", "text": "Paytm" },
            { "id": "l3", "text": "Aditya Birla Capital" }
        ],
        "right": [
            { "id": "r1", "text": "Sử dụng chatbot AI (iPal) làm dấy lên các lo ngại về quyền riêng tư và bảo mật thông tin khách hàng" },
            { "id": "r2", "text": "Cung cấp nền tảng giao dịch thuật toán (Algorithmic trading) gây lo ngại về tính công bằng và thao túng thị trường" },
            { "id": "r3", "text": "Sử dụng NLP để tư vấn đầu tư cá nhân hóa, đồng thời đối mặt với nhu cầu bảo vệ dữ liệu tài chính nhạy cảm" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "ICICI liên quan đến chatbot iPal. Paytm liên quan giao dịch thuật toán. Aditya Birla liên quan tư vấn đầu tư bằng NLP."
    },
    # 13. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp theo thứ tự mức độ can thiệp vào ngôn ngữ tự nhiên từ thấp đến cao (từ đọc dữ liệu thô đến tạo ra phản hồi):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Dữ liệu văn bản phi cấu trúc (Unstructured Text Data)" },
            { "id": "2", "text": "Phân tích ngữ nghĩa và khai phá văn bản (Text mining)" },
            { "id": "3", "text": "Hiểu ngôn ngữ tự nhiên (NLU) - Máy hiểu ý định" },
            { "id": "4", "text": "Tạo ngôn ngữ tự nhiên (NLG) - Máy tự động phát sinh câu trả lời" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quy trình bắt đầu từ văn bản thô -> Trích xuất dữ liệu cơ bản -> Hiểu ngữ nghĩa chuyên sâu (NLU) -> Sinh ra văn bản phản hồi mới (NLG)."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ vào chỗ trống liên quan đến rủi ro của AI Tạo sinh trong tài chính:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Sự phát triển nhanh chóng của AI thường vượt qua khả năng của nhà quản lý trong việc thiết lập <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, dẫn đến những khoảng trống trong tuân thủ. Hơn nữa, việc tự động hóa có thể dẫn đến <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> và bất bình đẳng kinh tế.",
        "words": [
            { "id": "w1", "text": "khuôn khổ pháp lý (legal frameworks)" },
            { "id": "w2", "text": "mất việc làm (job displacement)" },
            { "id": "w3", "text": "thuật toán" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Tài liệu nhắc đến 2 rủi ro: sự chậm trễ của luật pháp (Regulatory Compliance gap) và mất việc làm (Job displacement) do tự động hóa."
    },
    # 15. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Để xử lý dữ liệu có cấu trúc (structured data) trong một hệ thống ERP nhằm phát hiện gian lận giao dịch, kế toán viên nên sử dụng công nghệ nào sau đây là trực tiếp nhất?",
        "options": [
            { "id": "a", "text": "Khai phá văn bản (Text Mining)" },
            { "id": "b", "text": "Khai phá dữ liệu (Data Mining)" },
            { "id": "c", "text": "Thực tế ảo (VR)" },
            { "id": "d", "text": "Tạo ngôn ngữ tự nhiên (NLG)" }
        ],
        "correctAnswer": "b",
        "explanation": "Khai phá dữ liệu (Data Mining) rất phù hợp cho dữ liệu có cấu trúc từ hệ thống ERP/Sổ cái chung để tìm kiếm các mẫu và ngoại lai."
    },
    # 16. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công nghệ AI với một ứng dụng thực tiễn trong kế toán/tài chính:",
        "left": [
            { "id": "l1", "text": "Học sâu (Deep Learning)" },
            { "id": "l2", "text": "Khai phá văn bản (Text mining)" },
            { "id": "l3", "text": "RPA (Tự động hóa robot)" }
        ],
        "right": [
            { "id": "r1", "text": "Tái tạo lại các tài liệu quét kém chất lượng bằng nhận dạng quang học (như EY đang làm)" },
            { "id": "r2", "text": "Tìm kiếm từ ngữ mang tính buộc tội trong hàng ngàn email để phục vụ kiểm toán pháp y" },
            { "id": "r3", "text": "Tự động đăng nhập vào phần mềm và đối chiếu sao kê ngân hàng hàng ngày" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "DL chuyên xử lý ảnh/nhận dạng. Text mining xử lý văn bản/email. RPA xử lý thao tác tự động trên giao diện."
    },
    # 17. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Theo báo cáo, công cụ lập trình nào giúp thao tác trực tiếp với cơ sở dữ liệu rất hữu ích cho các ứng dụng AI?",
        "options": [
            { "id": "a", "text": "HTML và CSS" },
            { "id": "b", "text": "SQL và NoSQL" },
            { "id": "c", "text": "Photoshop" },
            { "id": "d", "text": "Excel VBA" }
        ],
        "correctAnswer": "b",
        "explanation": "Tài liệu ghi rõ: Các công cụ khác, chẳng hạn như SQL và NoSQL, sẽ hữu ích cho việc truy xuất, chỉnh sửa và thao tác dữ liệu để sử dụng cho ứng dụng AI."
    },
    # 18. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp quá trình tích hợp API của Google Prediction vào một hệ thống phần mềm doanh nghiệp:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Phần mềm doanh nghiệp thu thập dữ liệu giao dịch" },
            { "id": "2", "text": "Gửi dữ liệu thông qua API (người đưa tin kỹ thuật số) lên đám mây" },
            { "id": "3", "text": "Google Prediction API sử dụng Học máy để phân tích và đưa ra dự đoán" },
            { "id": "4", "text": "API trả kết quả phân tích về lại phần mềm doanh nghiệp để kế toán viên xem" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "API hoạt động như một cầu nối nhận dữ liệu, gửi tới service xử lý, và trả kết quả về."
    },
    # 19. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ vào chỗ trống liên quan đến việc lập hồ sơ khách hàng (Customer profiling):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Các tổ chức tài chính sử dụng AI để lập hồ sơ khách hàng nhằm mục đích tiếp thị nhắm mục tiêu. Tuy nhiên, các nhà bán lẻ có thể lạm dụng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để xác định những người tiêu dùng yếu thế, từ đó lợi dụng lỗ hổng tài chính của họ bằng các phương thức bán hàng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "phân tích dự đoán (predictive analytics)" },
            { "id": "w2", "text": "hung hăng (aggressive)" },
            { "id": "w3", "text": "bảo vệ môi trường" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Việc lạm dụng predictive analytics để đưa ra các đề xuất bán hàng hung hăng là một rủi ro đạo đức lớn."
    },
    # 20. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Vụ vi phạm dữ liệu của Equifax năm 2017 là một ví dụ điển hình cảnh báo rủi ro gì trong việc áp dụng AI vào tài chính?",
        "options": [
            { "id": "a", "text": "AI không thể hoạt động trên điện thoại di động" },
            { "id": "b", "text": "Nguy cơ về bảo mật và quyền riêng tư dữ liệu (Data Privacy) khi thu thập lượng lớn thông tin cá nhân" },
            { "id": "c", "text": "Chi phí điện năng quá cao để chạy mô hình AI" },
            { "id": "d", "text": "Sự thiên vị trong cấp tín dụng" }
        ],
        "correctAnswer": "b",
        "explanation": "Equifax là case study về Data Privacy, nơi hàng triệu dữ liệu bị lộ, nhấn mạnh tầm quan trọng của an ninh mạng."
    },
    # 21. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các khái niệm/hiện tượng trong AI Đạo đức với ý nghĩa thực tiễn của nó:",
        "left": [
            { "id": "l1", "text": "Thiên kiến thuật toán (Biases)" },
            { "id": "l2", "text": "Tính không rõ ràng về trách nhiệm (Accountability opacity)" },
            { "id": "l3", "text": "Bảo vệ người tiêu dùng (Consumer protection)" }
        ],
        "right": [
            { "id": "r1", "text": "Rủi ro khi hệ thống AI từ chối khoản vay dựa trên dữ liệu lịch sử mang tính phân biệt đối xử" },
            { "id": "r2", "text": "Khó khăn trong việc xác định ai (lập trình viên, ngân hàng hay AI) chịu trách nhiệm khi AI gây ra thiệt hại" },
            { "id": "r3", "text": "Ngăn chặn các thủ thuật tiếp thị và bán hàng lợi dụng lỗ hổng tâm lý/tài chính của khách hàng" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Biases = thiên vị phân biệt đối xử. Opacity = hộp đen/khó quy trách nhiệm. Protection = bảo vệ khách hàng khỏi bị thao túng."
    },
    # 22. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Theo giáo sư Aldhizer (2017), kỹ thuật Trích xuất Khái niệm (Concept Extraction) dùng trong kiểm toán pháp y chủ yếu để làm gì?",
        "options": [
            { "id": "a", "text": "Trích xuất số liệu bảng cân đối kế toán từ file Excel" },
            { "id": "b", "text": "Xác định các từ ngữ hoặc đoạn văn mang tính buộc tội (incriminating words) từ email và mạng xã hội" },
            { "id": "c", "text": "Khởi tạo hợp đồng thông minh trên Blockchain" },
            { "id": "d", "text": "Chấm điểm tín dụng cho doanh nghiệp" }
        ],
        "correctAnswer": "b",
        "explanation": "Concept extraction (một phần của text mining) được dùng trong pháp y kế toán để tìm từ ngữ buộc tội từ email, tin nhắn..."
    },
    # 23. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ vào chỗ trống liên quan đến học sâu:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Mạng nơ-ron nhân tạo (ANNs) được lấy cảm hứng từ <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> của con người, phân tích khối lượng dữ liệu lớn để <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "mạng nơ-ron sinh học" },
            { "id": "w2", "text": "tự học (self-learn)" },
            { "id": "w3", "text": "chiếc máy tính" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "ANN lấy cảm hứng từ cấu trúc não người (nơ-ron sinh học) để cho phép máy tính tự học từ dữ liệu."
    },
    # 24. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp quy trình giải quyết vấn đề bằng AI theo mô hình đề xuất để đảm bảo tính đạo đức:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thiết kế hệ thống AI và thu thập dữ liệu đại diện, tránh thiên vị (bias)" },
            { "id": "2", "text": "Triển khai thuật toán với sự minh bạch (transparency) và khả năng giải thích (explainability)" },
            { "id": "3", "text": "Áp dụng vào thực tế (như chấm điểm tín dụng) với sự giám sát liên tục (constant monitoring)" },
            { "id": "4", "text": "Thực hiện kiểm toán định kỳ (frequent audits) bởi bên thứ ba hoặc cơ quan quản lý" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Phát triển AI đạo đức cần: Thu thập dữ liệu sạch -> Thiết kế minh bạch -> Giám sát liên tục -> Kiểm toán định kỳ."
    },
    # 25. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Ứng dụng nào sau đây là kết quả của NLG (Tạo ngôn ngữ tự nhiên)?",
        "options": [
            { "id": "a", "text": "Siri ghi nhận giọng nói của người dùng thành văn bản" },
            { "id": "b", "text": "Máy tính đọc một hóa đơn PDF và lấy ra số tiền" },
            { "id": "c", "text": "Hệ thống tự động chuyển biểu đồ doanh thu thành một đoạn văn bản tóm tắt tình hình tài chính cho sếp đọc" },
            { "id": "d", "text": "Tìm kiếm các khoản vay rủi ro trong cơ sở dữ liệu SQL" }
        ],
        "correctAnswer": "c",
        "explanation": "NLG có thể chuyển đổi các hình ảnh hóa dữ liệu như biểu đồ thành mô tả bằng lời nói/văn bản mà con người đọc được."
    },
    # 26. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công cụ / ứng dụng với lĩnh vực tương ứng của chúng:",
        "left": [
            { "id": "l1", "text": "Python, R" },
            { "id": "l2", "text": "Google Prediction, BigML, Anaconda" },
            { "id": "l3", "text": "ACL, IDEA" }
        ],
        "right": [
            { "id": "r1", "text": "Ngôn ngữ lập trình mã nguồn mở tốt nhất cho khoa học dữ liệu" },
            { "id": "r2", "text": "Các dịch vụ nền tảng hoặc API hỗ trợ triển khai Học máy (ML)" },
            { "id": "r3", "text": "Phần mềm phân tích dữ liệu kiểm toán chuyên nghiệp truyền thống" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Python/R là ngôn ngữ lập trình; Google/BigML cung cấp API/Nền tảng ML; ACL/IDEA là phần mềm kiểm toán."
    },
    # 27. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Theo tài liệu, tại sao các ngân hàng và công ty tài chính cần hợp lực với các cơ quan quản lý trong việc sử dụng AI?",
        "options": [
            { "id": "a", "text": "Để tăng lợi nhuận và thao túng thị trường dễ hơn" },
            { "id": "b", "text": "Để bảo vệ tính toàn vẹn của thị trường, bảo vệ quyền lợi người tiêu dùng và đảm bảo tuân thủ pháp luật" },
            { "id": "c", "text": "Để độc quyền công nghệ AI" },
            { "id": "d", "text": "Để ngừng sử dụng AI và quay về làm thủ công" }
        ],
        "correctAnswer": "b",
        "explanation": "Sự hợp lực là để tận dụng AI trong khi vẫn bảo vệ sự toàn vẹn, đạo đức và tuân thủ quy định."
    },
    # 28. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ vào chỗ trống về Xử lý ngôn ngữ tự nhiên (NLP) trong kế toán:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Tiềm năng của NLP trong kế toán rất lớn. Nó được sử dụng để phân tích các văn bản liên quan đến hiệu quả tài chính và sự tuân thủ quy định. Các ứng dụng của NLP bao gồm phân tích <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, phân loại văn bản, và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> văn bản.",
        "words": [
            { "id": "w1", "text": "ngữ nghĩa (semantics)" },
            { "id": "w2", "text": "tóm tắt (summarization)" },
            { "id": "w3", "text": "chuỗi khối" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "NLP trong kế toán giúp phân tích ngữ nghĩa, phân loại và tóm tắt các tài liệu, hợp đồng, báo cáo."
    },
    # 29. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Quy trình ứng dụng Học sâu (Deep Learning) vào hệ thống tự động theo nghiên cứu:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập khối lượng lớn dữ liệu đầu vào (hình ảnh, giọng nói, tài liệu quét)" },
            { "id": "2", "text": "Dữ liệu được đưa qua các lớp của Mạng nơ-ron nhân tạo (ANNs)" },
            { "id": "3", "text": "Thuật toán tự khám phá ra các mô hình (patterns) mà không cần con người lập trình quy tắc tĩnh" },
            { "id": "4", "text": "Đưa ra dự đoán hoặc nhận dạng chính xác (vd: phát hiện hóa đơn giả)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "DL dựa vào việc đẩy dữ liệu qua mạng ANN để máy tự học cấu trúc (tự khám phá pattern) và đưa ra kết quả."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Hệ thống AI tài chính yêu cầu quyền truy cập vào lượng lớn dữ liệu (hồ sơ giao dịch, điểm tín dụng). Điều này đặt ra yêu cầu CẤP BÁCH nào nhất về mặt đạo đức/pháp luật?",
        "options": [
            { "id": "a", "text": "Yêu cầu phải sử dụng bộ xử lý TPU" },
            { "id": "b", "text": "Yêu cầu thiết lập luật bảo vệ dữ liệu mạnh mẽ để bảo mật quyền riêng tư (Data Privacy)" },
            { "id": "c", "text": "Yêu cầu phải in toàn bộ dữ liệu ra giấy" },
            { "id": "d", "text": "Yêu cầu AI phải tự động giao dịch thay con người" }
        ],
        "correctAnswer": "b",
        "explanation": "Quyền truy cập dữ liệu lớn đi liền với rủi ro bảo mật, đòi hỏi luật bảo vệ dữ liệu (privacy laws) nghiêm ngặt."
    }
]

import os

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day03\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the title and headers
content = content.replace("Bài Tập Trắc Nghiệm Buổi 1", "Bài Tập Trắc Nghiệm Buổi 3")
content = content.replace("Bài Tập Trắc Nghiệm Buổi 2", "Bài Tập Trắc Nghiệm Buổi 3")
content = content.replace("kiến thức của Buổi 1", "kiến thức của Buổi 3")
content = content.replace("kiến thức của Buổi 2", "kiến thức của Buổi 3")
content = content.replace("tài liệu Buổi 1", "tài liệu Buổi 3")
content = content.replace("tài liệu Buổi 2", "tài liệu Buổi 3")

# Replace the questions array
json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 03 quiz updated with 30 new questions.")
