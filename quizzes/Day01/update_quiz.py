import re
import json

questions = [
    # 1. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp các sự kiện lịch sử về công nghệ kế toán theo thứ tự thời gian từ cũ nhất (trên) đến mới nhất (dưới):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Sử dụng bàn tính (Hơn 2000 năm trước)" },
            { "id": "2", "text": "Mua máy tính chuyên dụng cho mục đích kế toán (1955)" },
            { "id": "3", "text": "Sự ra đời của bảng tính điện tử - Spreadsheets (Những năm 1980)" },
            { "id": "4", "text": "Ứng dụng Trí tuệ nhân tạo (Hiện tại và Tương lai)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Công nghệ kế toán tiến hóa từ bàn tính (cũ nhất), đến việc dùng máy tính sơ khai (1955), sau đó là bảng tính điện tử (1980) và hiện tại là AI."
    },
    # 2. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Theo Klaus Schwab (Diễn đàn Kinh tế Thế giới), AI là một trong những công nghệ then chốt thúc đẩy cuộc cách mạng nào?",
        "options": [
            { "id": "a", "text": "Cách mạng Công nghiệp lần thứ nhất" },
            { "id": "b", "text": "Cách mạng Công nghiệp lần thứ hai" },
            { "id": "c", "text": "Cách mạng Công nghiệp lần thứ ba" },
            { "id": "d", "text": "Cách mạng Công nghiệp lần thứ tư" }
        ],
        "correctAnswer": "d",
        "explanation": "Klaus Schwab mô tả kỷ nguyên chuyển đổi số hiện nay, với sự hội tụ của dữ liệu lớn, IoT và AI là Cuộc Cách mạng Công nghiệp Lần thứ tư."
    },
    # 3. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công ty kiểm toán/kế toán (Big4) với các ứng dụng AI thực tế của họ:",
        "left": [
            { "id": "l1", "text": "EY" },
            { "id": "l2", "text": "Deloitte" },
            { "id": "l3", "text": "KPMG" }
        ],
        "right": [
            { "id": "r1", "text": "Sử dụng công cụ Argus để trích xuất thông tin kế toán từ hợp đồng" },
            { "id": "r2", "text": "Sử dụng thuật toán học máy của IBM để hỗ trợ tuân thủ IFRS 16" },
            { "id": "r3", "text": "Dùng máy bay không người lái (drones) tích hợp AI để kiểm kê hàng tồn kho" }
        ],
        "correctPairs": { "l1": "r3", "l2": "r1", "l3": "r2" },
        "explanation": "EY dùng drones để kiểm kê. Deloitte dùng công cụ Argus đọc hợp đồng. KPMG dùng AI của IBM cho việc tuân thủ chuẩn mực thuê tài sản IFRS 16."
    },
    # 4. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền các thuật ngữ tương ứng vào chỗ trống để hoàn thành định nghĩa:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "<span class=\"blank-slot\" data-id=\"1\">___(1)___</span> tập trung vào một nhiệm vụ cụ thể (như nhận dạng giọng nói, chơi cờ). Trong khi đó, mục tiêu của <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> là tạo ra máy móc có khả năng thực hiện tất cả các nhiệm vụ nhận thức phức tạp của não bộ con người.",
        "words": [
            { "id": "w1", "text": "Trí tuệ nhân tạo hẹp (ANI)" },
            { "id": "w2", "text": "Trí tuệ nhân tạo tổng quát (AGI)" },
            { "id": "w3", "text": "Học máy (Machine Learning)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "ANI (AI hẹp/yếu) chỉ tập trung giải quyết một nhiệm vụ cụ thể rất tốt. AGI (AI tổng quát/mạnh) hướng tới năng lực nhận thức linh hoạt như con người."
    },
    # 5. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Đâu là điểm khác biệt cốt lõi giữa Khai phá dữ liệu (Data Mining) và Học máy (Machine Learning) theo chuyên gia Bernard Marr?",
        "options": [
            { "id": "a", "text": "Khai phá dữ liệu tìm mô hình đã có trong dữ liệu lịch sử, còn Học máy cố gắng dự đoán kết quả tương lai dựa trên dữ liệu." },
            { "id": "b", "text": "Khai phá dữ liệu hoàn toàn tự động, trong khi Học máy cần sự can thiệp của con người xuyên suốt quá trình." },
            { "id": "c", "text": "Khai phá dữ liệu là một lĩnh vực phụ của AI, còn Học máy thì độc lập với AI." },
            { "id": "d", "text": "Khai phá dữ liệu chỉ dùng dữ liệu phi cấu trúc, còn Học máy dùng dữ liệu có cấu trúc." }
        ],
        "correctAnswer": "a",
        "explanation": "Khai phá dữ liệu tìm kiếm mô hình đã tồn tại trong tập dữ liệu lịch sử. Học máy tự học từ tập huấn luyện để đưa ra dự đoán cho tương lai."
    },
    # 6. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép nối các loại hình Học máy (Machine Learning) với định nghĩa chính xác nhất:",
        "left": [
            { "id": "l1", "text": "Học có giám sát (Supervised)" },
            { "id": "l2", "text": "Học không giám sát (Unsupervised)" },
            { "id": "l3", "text": "Học bán giám sát (Semi-supervised)" },
            { "id": "l4", "text": "Học tăng cường (Reinforcement)" }
        ],
        "right": [
            { "id": "r1", "text": "Dùng dữ liệu đầu vào CHƯA được gắn nhãn để tìm ra các xu hướng, cụm (clusters)" },
            { "id": "r2", "text": "Kết hợp sử dụng cả dữ liệu ĐÃ được gắn nhãn và CHƯA được gắn nhãn" },
            { "id": "r3", "text": "Học từ tập dữ liệu ĐÃ được gắn nhãn (biết trước đầu vào X dẫn đến đầu ra Y)" },
            { "id": "r4", "text": "Thuật toán tự huấn luyện thông qua thử và sai (nhận phần thưởng hoặc bị phạt)" }
        ],
        "correctPairs": { "l1": "r3", "l2": "r1", "l3": "r2", "l4": "r4" },
        "explanation": "Có giám sát = Có nhãn sẵn; Không giám sát = Không nhãn; Bán giám sát = Dùng cả 2 loại; Tăng cường = Thử và sai (Thưởng/Phạt)."
    },
    
    # NEW QUESTIONS 7-30
    
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Hội nghị Trí tuệ nhân tạo (AI) đầu tiên được tổ chức vào năm 1956 tại trường đại học nào?",
        "options": [
            { "id": "a", "text": "Đại học Harvard" },
            { "id": "b", "text": "Đại học Stanford" },
            { "id": "c", "text": "Đại học Dartmouth" },
            { "id": "d", "text": "Viện Công nghệ Massachusetts (MIT)" }
        ],
        "correctAnswer": "c",
        "explanation": "Lĩnh vực AI được thiết lập như một chuyên ngành học thuật và nghiên cứu khi hội nghị AI đầu tiên được tổ chức tại Đại học Dartmouth vào năm 1956."
    },
    # 8. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp các mốc lịch sử của AI và Công nghệ từ cũ nhất đến mới nhất:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Mô hình nơ-ron nhân tạo đầu tiên do McCulloch và Pitts đề xuất (1943)" },
            { "id": "2", "text": "Hội nghị AI đầu tiên tại Đại học Dartmouth (1956)" },
            { "id": "3", "text": "Hệ chuyên gia (Expert Systems) ra đời (Những năm 1970)" },
            { "id": "4", "text": "Phần mềm bảng tính điện tử phổ biến trong kế toán (Những năm 1980)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "1943: Mô hình nơ-ron; 1956: Dartmouth; Những năm 1970: Hệ chuyên gia; Những năm 1980: Bảng tính điện tử."
    },
    # 9. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong kế toán quản trị, trí tuệ nhân tạo (AI) thường được sử dụng để thực hiện công việc gì?",
        "options": [
            { "id": "a", "text": "Chỉ phát hiện giao dịch gian lận trong kiểm toán" },
            { "id": "b", "text": "Tự động mã hóa bút toán kế toán, dự báo doanh thu và phân tích dữ liệu phi cấu trúc" },
            { "id": "c", "text": "Thay thế hoàn toàn giám đốc tài chính (CFO)" },
            { "id": "d", "text": "Khai thuế thủ công cho khách hàng" }
        ],
        "correctAnswer": "b",
        "explanation": "Trong kế toán quản trị, AI được sử dụng để tự động mã hóa các bút toán kế toán, dự báo doanh thu và phân tích các dữ liệu phi cấu trúc như hợp đồng, email."
    },
    # 10. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Hoàn thành định nghĩa sau về API:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Giao diện lập trình ứng dụng (API) là một tập hợp các chức năng hoặc quy tắc tạo điều kiện cho giao tiếp giữa các <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> và thiết bị.",
        "words": [
            { "id": "w1", "text": "ứng dụng" },
            { "id": "w2", "text": "cơ sở dữ liệu" },
            { "id": "w3", "text": "thuật toán" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "API là tập hợp các quy tắc tạo điều kiện giao tiếp giữa ứng dụng, cơ sở dữ liệu và thiết bị, hoạt động như các 'sứ giả kỹ thuật số'."
    },
    # 11. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công nghệ / khái niệm với ví dụ thực tiễn tương ứng:",
        "left": [
            { "id": "l1", "text": "Hiểu ngôn ngữ tự nhiên (NLU)" },
            { "id": "l2", "text": "Tạo ngôn ngữ tự nhiên (NLG)" },
            { "id": "l3", "text": "API (Giao diện lập trình ứng dụng)" }
        ],
        "right": [
            { "id": "r1", "text": "Siri nhận diện và hiểu câu hỏi 'Thời tiết hôm nay thế nào?'" },
            { "id": "r2", "text": "Siri trả lời lại bằng giọng nói: 'Hôm nay trời quang, nhiệt độ 28 độ'" },
            { "id": "r3", "text": "Khách hàng mua vé xem phim qua Fandango bằng cách đăng nhập tài khoản Facebook" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "NLU giúp máy hiểu câu hỏi. NLG giúp máy phát ra câu trả lời bằng ngôn ngữ tự nhiên. API giúp Fandango kết nối với Facebook để đăng nhập."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Ứng dụng nào của Apple sử dụng phương pháp không cần lập trình truyền thống (no-code/low-code) để phát triển mô hình Học máy?",
        "options": [
            { "id": "a", "text": "Kubeflow" },
            { "id": "b", "text": "Create ML" },
            { "id": "c", "text": "CNTK" },
            { "id": "d", "text": "Anaconda" }
        ],
        "correctAnswer": "b",
        "explanation": "Ứng dụng 'Create ML' của Apple cho phép người dùng phát triển và đào tạo các mô hình ML bằng phương pháp kéo-thả (no-code/low-code)."
    },
    # 13. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp các khái niệm AI từ phổ quát nhất (rộng nhất) đến chuyên biệt nhất (nhỏ nhất):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Trí tuệ nhân tạo (AI - Artificial Intelligence)" },
            { "id": "2", "text": "Học máy (ML - Machine Learning)" },
            { "id": "3", "text": "Học sâu (DL - Deep Learning)" }
        ],
        "correctOrder": ["1", "2", "3"],
        "explanation": "Học sâu (DL) là một tập hợp con của Học máy (ML). Học máy lại là một tập hợp con của Trí tuệ nhân tạo (AI)."
    },
    # 14. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Theo Xavier Amatriain, nhận định nào sau đây là ĐÚNG về mối quan hệ giữa Khai phá dữ liệu (Data Mining) và Trí tuệ nhân tạo (AI)?",
        "options": [
            { "id": "a", "text": "Khai phá dữ liệu là một tập hợp con (sub-field) của AI." },
            { "id": "b", "text": "Khai phá dữ liệu giao thoa với AI nhưng KHÔNG được coi là một lĩnh vực phụ của AI." },
            { "id": "c", "text": "AI là một lĩnh vực phụ của Khai phá dữ liệu." },
            { "id": "d", "text": "Khai phá dữ liệu và AI hoàn toàn không có sự liên quan nào." }
        ],
        "correctAnswer": "b",
        "explanation": "Khai phá dữ liệu giao thoa với AI nhưng không được coi là lĩnh vực phụ. Khai phá dữ liệu có thể sử dụng học máy (một phần của AI) nhưng cũng sử dụng các kỹ thuật khác ngoài học máy."
    },
    # 15. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công nghệ nền tảng mã thấp/không mã (low-code/no-code) với nhà phát triển tương ứng:",
        "left": [
            { "id": "l1", "text": "Create ML" },
            { "id": "l2", "text": "Kubeflow" },
            { "id": "l3", "text": "CNTK (Cognitive Toolkit)" }
        ],
        "right": [
            { "id": "r1", "text": "Apple" },
            { "id": "r2", "text": "Google" },
            { "id": "r3", "text": "Microsoft" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Create ML do Apple phát triển. Kubeflow hỗ trợ trên nền tảng AI của Google. CNTK do Microsoft phát triển cho nền tảng Azure."
    },
    # 16. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ thích hợp vào định nghĩa của Học sâu (Deep Learning):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Học sâu là một tập hợp con của học máy sử dụng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để khám phá các mô hình từ dữ liệu. Các mô hình này thường được tăng tốc bởi <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>, một mạch tích hợp chuyên dụng do Google phát triển.",
        "words": [
            { "id": "w1", "text": "Mạng nơ-ron nhân tạo (ANN)" },
            { "id": "w2", "text": "Bộ xử lý tensor (TPU)" },
            { "id": "w3", "text": "Khai phá dữ liệu" },
            { "id": "w4", "text": "Lô-gic mờ (Fuzzy logic)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Học sâu sử dụng mạng nơ-ron nhân tạo (ANN) lấy cảm hứng từ bộ não người và thường được tăng tốc xử lý bởi bộ xử lý tensor (TPU)."
    },
    # 17. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong bối cảnh hệ chuyên gia (Expert Systems), hệ thống nào sử dụng các thuật ngữ không mang tính nhị phân (0 hoặc 1) để đối phó với sự thiếu chính xác và mơ hồ?",
        "options": [
            { "id": "a", "text": "Hệ chuyên gia dựa trên quy tắc (Rules-based)" },
            { "id": "b", "text": "Hệ chuyên gia dựa trên lô-gic mờ (Fuzzy-based)" },
            { "id": "c", "text": "Mạng nơ-ron nhân tạo (ANN)" },
            { "id": "d", "text": "Xử lý ngôn ngữ tự nhiên (NLP)" }
        ],
        "correctAnswer": "b",
        "explanation": "Lô-gic mờ (fuzzy logic) hữu ích trong các tình huống liên quan đến sự thiếu chính xác và mơ hồ, nơi các điều kiện không thể phân định rõ ràng 0 hoặc 1 (đúng/sai tuyệt đối)."
    },
    # 18. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp quy trình Khai phá văn bản (Text Mining) theo thứ tự thực hiện:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập các nguồn dữ liệu văn bản phi cấu trúc (hợp đồng, email, PDF...)" },
            { "id": "2", "text": "Áp đặt cấu trúc (structure) lên các nguồn dữ liệu văn bản phi cấu trúc này" },
            { "id": "3", "text": "Sử dụng các kỹ thuật khai phá dữ liệu để trích xuất thông tin có liên quan" },
            { "id": "4", "text": "Khám phá các mô hình, xu hướng và chủ đề từ thông tin trích xuất" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quá trình bắt đầu từ thu thập dữ liệu phi cấu trúc -> áp đặt cấu trúc cho nó -> sử dụng khai phá dữ liệu -> cuối cùng khám phá xu hướng/mô hình."
    },
    # 19. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các công cụ / ứng dụng với phương thức tiếp cận AI của chúng:",
        "left": [
            { "id": "l1", "text": "Khai phá văn bản (Text Mining)" },
            { "id": "l2", "text": "Lập luận máy (Machine Reasoning)" },
            { "id": "l3", "text": "Phân tích cụm (Cluster Analysis)" }
        ],
        "right": [
            { "id": "r1", "text": "Sử dụng NLP để trích xuất ý nghĩa từ dữ liệu văn bản" },
            { "id": "r2", "text": "Thao tác đại số đối với kiến thức đã thu nhận để suy luận diễn dịch/quy nạp" },
            { "id": "r3", "text": "Nhóm dữ liệu không gắn nhãn lại với nhau dựa trên điểm tương đồng (Học không giám sát)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Khai phá văn bản sử dụng NLP. Lập luận máy dùng suy luận tự động. Phân tích cụm là phương pháp điển hình của học không giám sát."
    },
    # 20. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Công nghệ RPA (Robotic Process Automation) phù hợp nhất với loại tác vụ nào?",
        "options": [
            { "id": "a", "text": "Các tác vụ đòi hỏi sự tư duy sáng tạo nghệ thuật" },
            { "id": "b", "text": "Các tác vụ có khối lượng lớn, lặp đi lặp lại và theo quy tắc rõ ràng" },
            { "id": "c", "text": "Các quyết định chiến lược cấp hội đồng quản trị" },
            { "id": "d", "text": "Sáng tác nhạc và vẽ tranh" }
        ],
        "correctAnswer": "b",
        "explanation": "RPA rất phù hợp với các tác vụ có khối lượng lớn và lặp đi lặp lại (như đối chiếu ngân hàng, xử lý hóa đơn) thường do con người thực hiện trước đây."
    },
    # 21. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ vào chỗ trống về Lập luận máy (Machine Reasoning):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Các hệ thống Lập luận máy sử dụng kỹ thuật suy luận tự động để bắt chước con người, chẳng hạn như <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (deduction) và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> (induction).",
        "words": [
            { "id": "w1", "text": "diễn dịch" },
            { "id": "w2", "text": "quy nạp" },
            { "id": "w3", "text": "dự đoán" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Lập luận máy sử dụng kỹ thuật suy luận tự động như diễn dịch (từ cái chung suy ra cái riêng) và quy nạp (từ số liệu cụ thể khái quát thành cái chung)."
    },
    # 22. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong ví dụ về Học có giám sát (Supervised Learning), biến đầu vào (X) và biến đầu ra (Y) được mô tả như thế nào khi dự đoán nợ xấu?",
        "options": [
            { "id": "a", "text": "X là tuổi nợ của khách hàng, Y là số tiền nợ khó đòi đã xóa sổ" },
            { "id": "b", "text": "X là số lượng nhân viên, Y là doanh thu của công ty" },
            { "id": "c", "text": "X là dữ liệu không dán nhãn, Y là các cụm khách hàng" },
            { "id": "d", "text": "X là mức độ gian lận, Y là tên khách hàng" }
        ],
        "correctAnswer": "a",
        "explanation": "Trong bài, mô hình học có giám sát dùng dữ liệu lịch sử: X (đầu vào) là tuổi nợ của khách hàng, Y (đầu ra) là số tiền phải thu khó đòi bị xóa sổ."
    },
    # 23. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp quá trình hoạt động của thuật toán Học Tăng cường (Reinforcement Learning):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Tác nhân (agent) thực hiện một hành động (thử và sai) trong môi trường" },
            { "id": "2", "text": "Nhận được phần thưởng (reward) nếu đúng, hoặc hình phạt (penalty) nếu sai" },
            { "id": "3", "text": "Thuật toán học hỏi từ kết quả để điều chỉnh hành vi" },
            { "id": "4", "text": "Tối đa hóa phần thưởng và giảm thiểu hình phạt trong tương lai" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Học tăng cường diễn ra qua quá trình tác nhân thực hiện thử và sai -> nhận thưởng/phạt -> học hỏi -> tối đa hóa phần thưởng ở các lần sau."
    },
    # 24. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các thuật ngữ viết tắt trong AI với nghĩa tiếng Việt của nó:",
        "left": [
            { "id": "l1", "text": "NLP" },
            { "id": "l2", "text": "RPA" },
            { "id": "l3", "text": "IoT" }
        ],
        "right": [
            { "id": "r1", "text": "Xử lý ngôn ngữ tự nhiên" },
            { "id": "r2", "text": "Tự động hóa quy trình bằng robot" },
            { "id": "r3", "text": "Internet vạn vật" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "NLP: Natural Language Processing. RPA: Robotic Process Automation. IoT: Internet of Things."
    },
    # 25. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Theo nghiên cứu của Sophia Sun (2019), Học sâu (Deep Learning) vượt trội hơn Học máy (ML) cổ điển trong điều kiện nào?",
        "options": [
            { "id": "a", "text": "Khi tập dữ liệu cực kỳ nhỏ và chỉ có vài biến số" },
            { "id": "b", "text": "Khi khối lượng dữ liệu và số lượng biến (variables) rất lớn" },
            { "id": "c", "text": "Khi dữ liệu hoàn toàn có cấu trúc (bảng tính SQL)" },
            { "id": "d", "text": "Khi không có sự xuất hiện của dữ liệu bán cấu trúc hay phi cấu trúc" }
        ],
        "correctAnswer": "b",
        "explanation": "Hiệu suất dự đoán của mô hình DL vượt trội hơn ML cổ điển khi khối lượng dữ liệu lớn và số lượng biến (variables) nhiều."
    },
    # 26. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ vào chỗ trống để hoàn thành định nghĩa về AI của Siegel (2003):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Để máy móc thực hiện được các tác vụ phức tạp tốt bằng hoặc hơn con người, chúng phải có khả năng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>, học hỏi và giao tiếp.",
        "words": [
            { "id": "w1", "text": "cảm nhận" },
            { "id": "w2", "text": "lập luận" },
            { "id": "w3", "text": "bay lượn" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Theo Siegel et al. (2003), máy móc phải có khả năng cảm nhận (perceive), lập luận (reason), học hỏi (learn) và giao tiếp (communicate)."
    },
    # 27. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Bệnh viện Đa khoa Tampa ở Florida đã sử dụng AI trong đại dịch Covid-19 với mục đích gì?",
        "options": [
            { "id": "a", "text": "Chẩn đoán bệnh nhân qua email" },
            { "id": "b", "text": "Quét nhiệt khuôn mặt để phát hiện các triệu chứng tiềm ẩn (sốt, mồ hôi, đổi màu da)" },
            { "id": "c", "text": "Tính toán chi phí khám bệnh tự động" },
            { "id": "d", "text": "Robot phẫu thuật từ xa" }
        ],
        "correctAnswer": "b",
        "explanation": "Bệnh viện Tampa triển khai AI thực hiện quét nhiệt khuôn mặt người vào tòa nhà để phát hiện triệu chứng virus như sốt, đổi màu da."
    },
    # 28. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Quy trình xử lý một lệnh thoại của Siri (ứng dụng của AI và NLP) diễn ra theo thứ tự nào?",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Người dùng nói: 'Thời tiết hôm nay thế nào?'" },
            { "id": "2", "text": "NLU (Hiểu ngôn ngữ tự nhiên) giúp máy tính phân tích và hiểu yêu cầu" },
            { "id": "3", "text": "Máy tính truy xuất dữ liệu thời tiết qua API Internet" },
            { "id": "4", "text": "NLG (Tạo ngôn ngữ tự nhiên) chuyển dữ liệu thành câu trả lời bằng giọng nói" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Người dùng ra lệnh -> Máy hiểu lệnh (NLU) -> Máy lấy thông tin -> Máy trả lời lại bằng ngôn ngữ tự nhiên (NLG)."
    },
    # 29. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công cụ lập trình AI với đặc điểm của chúng:",
        "left": [
            { "id": "l1", "text": "Python và R" },
            { "id": "l2", "text": "SQL và NoSQL" },
            { "id": "l3", "text": "UiPath và BluePrism" }
        ],
        "right": [
            { "id": "r1", "text": "Ngôn ngữ mã nguồn mở phổ biến nhất để xây dựng và tùy chỉnh ứng dụng AI/ML" },
            { "id": "r2", "text": "Công cụ truy xuất, chỉnh sửa và thao tác với cơ sở dữ liệu" },
            { "id": "r3", "text": "Các nền tảng phần mềm phổ biến cho Tự động hóa quy trình bằng robot (RPA)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Python/R mạnh về AI/ML. SQL/NoSQL mạnh về xử lý cơ sở dữ liệu. UiPath/BluePrism là phần mềm RPA."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Việc sử dụng thuật toán máy tính (như Amazon, Netflix) để đề xuất phim hoặc sản phẩm dựa trên lịch sử mua sắm của bạn là một ứng dụng phổ biến của lĩnh vực nào?",
        "options": [
            { "id": "a", "text": "Học máy (Machine Learning)" },
            { "id": "b", "text": "Khai phá văn bản (Text Mining)" },
            { "id": "c", "text": "Lập luận máy (Machine Reasoning)" },
            { "id": "d", "text": "Tự động hóa quy trình (RPA)" }
        ],
        "correctAnswer": "a",
        "explanation": "Hệ thống đề xuất (recommendation engines) của Amazon hay Netflix là ví dụ kinh điển của Học máy (ML), học từ dữ liệu quá khứ để dự đoán sở thích tương lai."
    }
]

file_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day01\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the questions array
# We need to find `const questions = [` and replace everything until `];` (inclusive)
# Let's use a regex to replace it
import re

json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"

pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

# update question counter logic because there are now 30 questions
# We also need to change the final message if score is 30/30
# The javascript code uses `score === questions.length` so it will automatically adapt.

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully added 24 new questions. Total 30 questions.")
