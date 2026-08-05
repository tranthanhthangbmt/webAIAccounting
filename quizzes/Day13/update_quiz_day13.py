import re
import json
import os

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Trong bối cảnh kế toán tài chính, quá trình phân tích với sự trợ giúp của AI đã chuyển đổi từ 'gương chiếu hậu' thành gì?",
        "options": [
            { "id": "a", "text": "Một chiếc kính viễn vọng tiên đoán" },
            { "id": "b", "text": "Một cuốn sổ ghi chép kế toán tay dày đặc" },
            { "id": "c", "text": "Một hệ thống in ấn chứng từ thuế giấy" },
            { "id": "d", "text": "Một màn hình máy tính đen trắng cũ" }
        ],
        "correctAnswer": "a",
        "explanation": "Wayne R. Landsman mô tả AI biến quá trình phân tích từ 'gương chiếu hậu' (chỉ nhìn dữ liệu lịch sử) thành 'kính viễn vọng tiên đoán'."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong dự báo dòng tiền, trí tuệ nhân tạo (AI) đột phá thế nào so với phương pháp truyền thống?",
        "options": [
            { "id": "a", "text": "Phân tích đa biến thời gian thực" },
            { "id": "b", "text": "Dựa trên phương pháp trung bình cộng giản đơn" },
            { "id": "c", "text": "Phỏng đoán thủ công bằng cảm tính của CEO" },
            { "id": "d", "text": "Chỉ dựa vào sổ quỹ tiền mặt hàng ngày" }
        ],
        "correctAnswer": "a",
        "explanation": "Thay vì dựa trên trung bình cộng, AI sử dụng mô hình học máy phân tích dữ liệu đa biến thời gian thực."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các công cụ AI trong dự báo tài chính với ứng dụng của chúng:",
        "left": [
            { "id": "l1", "text": "Mô hình dự đoán (Predictive Models)" },
            { "id": "l2", "text": "Phân tích tình cảm (Sentiment Analysis)" },
            { "id": "l3", "text": "Trực quan hóa tự động" }
        ],
        "right": [
            { "id": "r1", "text": "Dự báo doanh thu và chi phí bằng Machine Learning" },
            { "id": "r2", "text": "Đánh giá xu hướng tâm lý thị trường qua tin tức" },
            { "id": "r3", "text": "Chuyển số liệu phức tạp thành bảng điều khiển (Dashboards)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Mô hình dự đoán dùng học máy; Phân tích tình cảm quét tin tức; Trực quan hóa tạo Dashboard."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp thứ tự các bước trong khung tư duy SPARKS theo thứ tự đúng:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "S - State the Question (Xác định câu hỏi)" },
            { "id": "2", "text": "P - Partition the Data (Phân chia dữ liệu)" },
            { "id": "3", "text": "A - Analyze the Data (Thực hiện phân tích)" },
            { "id": "4", "text": "R - Refine the Analysis (Tinh chỉnh phân tích)" },
            { "id": "5", "text": "K - Communicate (Truyền đạt thông tin)" }
        ],
        "correctOrder": ["1", "2", "3", "4", "5"],
        "explanation": "Quy trình SPARKS: State -> Partition -> Analyze -> Refine -> Communicate -> Stop."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về kỹ thuật Viết Prompt:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong Prompt Engineering, việc chỉ định <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (ví dụ: 'Hãy đóng vai một Kế toán trưởng...') giúp LLM thiết lập giọng văn và độ sâu kỹ thuật chuẩn xác. Ngoài ra, cần cung cấp <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> rõ ràng để AI xử lý đúng hướng.",
        "words": [
            { "id": "w1", "text": "vai trò" },
            { "id": "w2", "text": "bối cảnh" },
            { "id": "w3", "text": "bạn bè" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Role-based Prompting gán vai trò chuyên môn (Role), đồng thời cần có bối cảnh (Context)."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Tại sao kỹ thuật 'Phân chia tác vụ theo bước' (Chain-of-Thought) lại quan trọng khi dùng AI giải bài toán kế toán?",
        "options": [
            { "id": "a", "text": "Buộc AI tự re-check từng bước tính toán, giảm lỗi số học" },
            { "id": "b", "text": "Làm cho AI mất thời gian hơn để người dùng có thể nghỉ ngơi" },
            { "id": "c", "text": "Chỉ dùng để kiểm tra ngữ pháp tiếng Anh của máy tính" },
            { "id": "d", "text": "Giúp AI tự động gọi điện báo cáo cho cơ quan quản lý" }
        ],
        "correctAnswer": "a",
        "explanation": "Chain-of-Thought (Step-by-step) yêu cầu AI suy luận từng bước, giúp phát hiện lỗi logic và cải thiện độ chính xác tính toán."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Mức độ phân tích nào trả lời cho câu hỏi 'Chuyện gì đã xảy ra?'",
        "options": [
            { "id": "a", "text": "Phân tích Mô tả (Descriptive Analytics)" },
            { "id": "b", "text": "Phân tích Đề xuất (Prescriptive Analytics)" },
            { "id": "c", "text": "Phân tích Dự đoán (Predictive Analytics)" },
            { "id": "d", "text": "Phân tích Viễn tưởng (Sci-fi Analytics)" }
        ],
        "correctAnswer": "a",
        "explanation": "Phân tích mô tả (Descriptive) nhìn lại quá khứ để trả lời câu hỏi 'Chuyện gì đã xảy ra'."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép 4 mức độ phân tích với kỹ thuật kế toán thường dùng:",
        "left": [
            { "id": "l1", "text": "Mô tả (Descriptive)" },
            { "id": "l2", "text": "Chẩn đoán (Diagnostic)" },
            { "id": "l3", "text": "Đề xuất (Prescriptive)" }
        ],
        "right": [
            { "id": "r1", "text": "Bảng tổng hợp (Pivot Tables), tính tổng (Sum)" },
            { "id": "r2", "text": "Biểu đồ phân tán (Scatter), Phân tích phương sai" },
            { "id": "r3", "text": "Phân tích giả định (What-If), Tối ưu hóa mô hình" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Mô tả dùng Pivot Table; Chẩn đoán dùng phân tích phương sai để tìm nguyên nhân; Đề xuất dùng What-If để ra quyết định."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về các bước trong SPARKS:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Chữ K trong SPARKS đại diện cho <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (Communicate), nghĩa là sử dụng biểu đồ, Dashboard để truyền tải phát hiện đến <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "truyền đạt" },
            { "id": "w2", "text": "ban giám đốc" },
            { "id": "w3", "text": "khách du lịch" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Communicate là truyền đạt thông tin (Insights) đến các bên liên quan, đặc biệt là Ban Giám đốc."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Thứ tự tiến hành bài tập phân tích 'Giao dịch Hóa đơn bất thường' bằng SPARKS:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "S - Đặt câu hỏi: Có hóa đơn mua hàng giá trị bất thường không?" },
            { "id": "2", "text": "P - Trích xuất trường InvoiceDate, InvoiceAmount từ CSDL" },
            { "id": "3", "text": "A - Vẽ biểu đồ phân tán (Scatter Plot) để phân tích chẩn đoán" },
            { "id": "4", "text": "R - Kiểm tra các điểm giá trị ngoại lai (Outliers)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Hỏi -> Chọn dữ liệu -> Vẽ biểu đồ -> Tinh chỉnh kiểm tra ngoại lai."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trường dữ liệu 'QualityRating' trong AP Data Dictionary có ý nghĩa gì?",
        "options": [
            { "id": "a", "text": "Điểm đánh giá chất lượng của bộ phận nhận hàng" },
            { "id": "b", "text": "Số lượng sản phẩm bị nhà cung cấp thu hồi" },
            { "id": "c", "text": "Mức chiết khấu cho thanh toán trước hạn" },
            { "id": "d", "text": "Thuế suất GTGT tính cho đơn hàng nhập khẩu" }
        ],
        "correctAnswer": "a",
        "explanation": "QualityRating là thang điểm đánh giá chất lượng hàng hóa nhận được."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Nghiên cứu điển hình (Case study) trong ngành bán lẻ sử dụng AI để làm gì?",
        "options": [
            { "id": "a", "text": "Dự báo nhu cầu hàng tồn kho theo mùa vụ" },
            { "id": "b", "text": "Chế tạo ra sản phẩm mới trong siêu thị" },
            { "id": "c", "text": "Tính lương của nhân viên thu ngân nhanh hơn" },
            { "id": "d", "text": "Trang trí lại mặt tiền cửa hàng cho đẹp" }
        ],
        "correctAnswer": "a",
        "explanation": "Ngành bán lẻ dùng AI để dự báo nhu cầu hàng tồn kho, giảm 25% chi phí lưu kho."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các bước trong SPARKS với hành động tương ứng:",
        "left": [
            { "id": "l1", "text": "State the Question (Xác định câu hỏi)" },
            { "id": "l2", "text": "Partition the Data (Phân chia dữ liệu)" },
            { "id": "l3", "text": "Refine the Analysis (Tinh chỉnh)" }
        ],
        "right": [
            { "id": "r1", "text": "Tìm ra vấn đề tài chính cốt lõi cần giải quyết" },
            { "id": "r2", "text": "Làm sạch, loại bỏ sai lệch và chọn lọc biến số" },
            { "id": "r3", "text": "Kiểm tra tính hợp lệ của giả định, rà soát rủi ro" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "State là đặt câu hỏi; Partition là làm sạch/lọc dữ liệu; Refine là kiểm tra/rà soát kết quả phân tích."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về các cấp độ phân tích:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Phân tích <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (Predictive) giúp trả lời 'Điều gì có khả năng sẽ xảy ra?' thông qua các công cụ như <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>, trong khi Phân tích Đề xuất trả lời 'Chúng ta nên làm gì?'.",
        "words": [
            { "id": "w1", "text": "Dự đoán" },
            { "id": "w2", "text": "Hồi quy tuyến tính" },
            { "id": "w3", "text": "Đánh thuế GTGT" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Dự đoán (Predictive) sử dụng công cụ như Hồi quy tuyến tính (Linear Regression) hay Machine Learning."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Các bước trong quy trình phân tích Quy mô Mua hàng theo Quốc gia bằng SPARKS:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "S - Hỏi kim ngạch mua hàng phân bổ giữa các quốc gia thế nào?" },
            { "id": "2", "text": "P - Trích xuất bảng dữ liệu có trường ShipLocation, InvoiceAmount" },
            { "id": "3", "text": "A - Kéo thả Pivot Table để tính SUM(InvoiceAmount) theo vị trí" },
            { "id": "4", "text": "K - Tạo biểu đồ tròn (Pie Chart) báo cáo tổng chi phí toàn cầu" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Câu hỏi -> Lọc bảng -> Pivot Table -> Vẽ biểu đồ."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong kỹ thuật viết Prompt, vì sao KHÔNG nên đưa thông tin như tên thật, mã số thuế thực tế của khách hàng vào công cụ AI?",
        "options": [
            { "id": "a", "text": "Vì rủi ro vi phạm bảo mật dữ liệu nhạy cảm" },
            { "id": "b", "text": "Vì AI không thể đọc được các con số mã số thuế" },
            { "id": "c", "text": "Vì làm AI bị chậm tốc độ xử lý mạng internet" },
            { "id": "d", "text": "Vì chính phủ cấm sử dụng AI trong toàn quốc" }
        ],
        "correctAnswer": "a",
        "explanation": "Đưa PII (Personally Identifiable Information) hoặc dữ liệu mật lên nền tảng công cộng tiềm ẩn nguy cơ rò rỉ dữ liệu (data breach)."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các trường dữ liệu AP với ý nghĩa thực tế:",
        "left": [
            { "id": "l1", "text": "InvoiceAmount" },
            { "id": "l2", "text": "VendorName" },
            { "id": "l3", "text": "PaymentTerms" }
        ],
        "right": [
            { "id": "r1", "text": "Tổng số tiền phải trả cho hóa đơn" },
            { "id": "r2", "text": "Tên đầy đủ của đơn vị cung cấp" },
            { "id": "r3", "text": "Điều khoản tín dụng thương mại (ví dụ Net 30)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "InvoiceAmount = Số tiền hóa đơn; VendorName = Tên nhà cung cấp; PaymentTerms = Điều kiện thanh toán."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Trong ví dụ 'Phân tích Rủi ro tín dụng', AI đem lại lợi ích gì so với việc đánh giá bằng các chỉ số tĩnh?",
        "options": [
            { "id": "a", "text": "Phân tích liên tục hành vi thanh toán thời gian thực" },
            { "id": "b", "text": "Cho phép khách hàng vay nợ không cần phải thế chấp" },
            { "id": "c", "text": "Bỏ qua toàn bộ thủ tục pháp lý của hợp đồng vay vốn" },
            { "id": "d", "text": "Phê duyệt mọi khoản vay mà không xét tín dụng" }
        ],
        "correctAnswer": "a",
        "explanation": "AI vượt trội nhờ việc giám sát liên tục tín hiệu thị trường và hành vi để tự động cảnh báo sớm."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ về các bước viết Prompt:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Tránh các prompt quá <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Nên chia nhỏ bài toán bằng cách yêu cầu AI giải quyết <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> để tính chính xác nhất.",
        "words": [
            { "id": "w1", "text": "chung chung" },
            { "id": "w2", "text": "từng bước" },
            { "id": "w3", "text": "khó tính" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Prompt cần cụ thể, không chung chung. Và nên dùng Chain-of-thought (từng bước)."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Bước chữ 'S' cuối cùng trong SPARKS (Stop and Reflect) có ý nghĩa gì?",
        "options": [
            { "id": "a", "text": "Đánh giá lại xem thông tin đã trả lời trọn vẹn câu hỏi chưa" },
            { "id": "b", "text": "Dừng mọi công việc để chuẩn bị nghỉ phép hàng năm" },
            { "id": "c", "text": "Buộc máy chủ cơ sở dữ liệu ngắt kết nối mạng ngay lập tức" },
            { "id": "d", "text": "Yêu cầu hủy bỏ mọi phân tích và bắt đầu lại từ đầu" }
        ],
        "correctAnswer": "a",
        "explanation": "Stop and Reflect là lúc nhìn lại toàn bộ quá trình xem insight đã giải quyết được vấn đề kinh doanh gốc hay chưa."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp cấu trúc Prompt hoàn chỉnh để phân tích Báo cáo Tài chính:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Đóng vai một chuyên gia phân tích tài chính cao cấp" },
            { "id": "2", "text": "Đây là bảng số liệu tài chính của Công ty A trong quý 3" },
            { "id": "3", "text": "Hãy tính toán các chỉ số thanh khoản (hiện hành, nhanh)" },
            { "id": "4", "text": "Đưa ra nhận xét chiến lược ngắn gọn trong 3 gạch đầu dòng" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Gán Role -> Cung cấp Context/Data -> Ra lệnh tính toán -> Yêu cầu định dạng đầu ra."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các bài tập thực hành SPARKS với loại biểu đồ/công cụ thể hiện:",
        "left": [
            { "id": "l1", "text": "Tìm giá trị bất thường (Outliers) của Hóa đơn" },
            { "id": "l2", "text": "Đánh giá chất lượng của Top Nhà cung cấp" },
            { "id": "l3", "text": "Quy mô mua hàng toàn cầu phân bổ theo khu vực" }
        ],
        "right": [
            { "id": "r1", "text": "Biểu đồ phân tán (Scatter Plot) với trục giá và ngày" },
            { "id": "r2", "text": "Biểu đồ cột (Bar Chart) xếp hạng điểm trung bình" },
            { "id": "r3", "text": "Biểu đồ tròn (Pie Chart) thể hiện tỷ trọng phần trăm" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Outliers dùng Scatter plot; Top xếp hạng dùng Bar chart; Tỷ trọng phân bổ dùng Pie chart."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Đâu là kỹ thuật kế toán đại diện cho 'Phân tích Đề xuất' (Prescriptive Analytics)?",
        "options": [
            { "id": "a", "text": "Phân tích giả định (What-If Analysis) và tối ưu hóa" },
            { "id": "b", "text": "Dùng hàm SUM để tính tổng chi phí phát sinh" },
            { "id": "c", "text": "Kẻ bảng đối chiếu phương sai thủ công trên giấy" },
            { "id": "d", "text": "Vẽ biểu đồ phân tán tìm sự cố giao hàng chậm" }
        ],
        "correctAnswer": "a",
        "explanation": "What-If Analysis là đặc trưng của Prescriptive Analytics để đưa ra quyết định 'nên làm gì'."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về Dự báo thị trường Bất động sản (Case Study):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Sử dụng mô hình <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> đa biến AI để theo dõi lãi suất ngân hàng và dòng tiền thuê, giúp ban lãnh đạo ra quyết định <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> an toàn hơn.",
        "words": [
            { "id": "w1", "text": "hồi quy" },
            { "id": "w2", "text": "giải ngân" },
            { "id": "w3", "text": "thơ ca" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Dùng Hồi quy (Regression) đa biến để dự báo, từ đó quyết định giải ngân (hoặc thoái vốn)."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Các bước để rà soát Hóa đơn và Thuế GTGT bằng Prompt:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Yêu cầu: 'Đóng vai chuyên viên kiểm soát thuế'" },
            { "id": "2", "text": "Cung cấp danh sách các giao dịch mua hàng thô" },
            { "id": "3", "text": "Yêu cầu: 'Lập bảng đối chiếu phát hiện khoản rủi ro GTGT'" },
            { "id": "4", "text": "Định dạng kết quả: 'Trích dẫn lý do pháp lý ở cột cuối'" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Gán role -> Cấp dữ liệu -> Giao task -> Ấn định kết quả."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Chữ 'A' trong SPARKS framework đại diện cho hành động gì?",
        "options": [
            { "id": "a", "text": "Analyze the Data (Thực hiện phân tích dữ liệu)" },
            { "id": "b", "text": "Ask the AI (Hỏi Trí tuệ nhân tạo bất cứ gì)" },
            { "id": "c", "text": "Archive the Document (Lưu trữ tài liệu kế toán)" },
            { "id": "d", "text": "Approve the Budget (Phê duyệt ngân sách quý)" }
        ],
        "correctAnswer": "a",
        "explanation": "A = Analyze (Phân tích). Áp dụng các kỹ thuật mô tả, chẩn đoán, dự đoán, đề xuất."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các cấp độ phân tích với ví dụ thực tiễn trong Kế toán:",
        "left": [
            { "id": "l1", "text": "Descriptive (Mô tả)" },
            { "id": "l2", "text": "Diagnostic (Chẩn đoán)" },
            { "id": "l3", "text": "Predictive (Dự đoán)" }
        ],
        "right": [
            { "id": "r1", "text": "Tính tổng chi phí mua hàng theo nhà cung cấp năm 2022" },
            { "id": "r2", "text": "Tìm nguyên nhân tỷ lệ hàng lỗi tăng cao vào tháng 8" },
            { "id": "r3", "text": "Dự báo số dư công nợ phải trả (AP) trong 2 quý tới" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Mô tả tính tổng; Chẩn đoán tìm nguyên nhân; Dự đoán dự báo AP tương lai."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về rủi ro mô hình phân tích:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong bước Refine (R), kế toán viên cần rà soát rủi ro, kiểm tra tính hợp lệ của các <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> tài chính và tinh chỉnh <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> để đạt độ chính xác cao hơn.",
        "words": [
            { "id": "w1", "text": "giả định" },
            { "id": "w2", "text": "mô hình" },
            { "id": "w3", "text": "báo giá" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Cần rà soát các giả định (assumptions) và tinh chỉnh mô hình (model) trong bước Refine."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Trình tự thực hiện bài tập 'Phân tích chất lượng nhà cung cấp':",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Xác định câu hỏi: Nhà cung cấp nào có chất lượng kém nhất?" },
            { "id": "2", "text": "Lọc dữ liệu VendorName, QualityRating từ hệ thống" },
            { "id": "3", "text": "Tính trung bình điểm chất lượng và xếp hạng" },
            { "id": "4", "text": "Đề xuất danh sách nhà cung cấp cần thay thế lên GĐ" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Đặt câu hỏi -> Lấy dữ liệu -> Tính toán -> Đưa đề xuất."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong trường hợp nào Kế toán viên đang thực hiện 'Phân tích Chẩn đoán' (Diagnostic)?",
        "options": [
            { "id": "a", "text": "Đối chiếu phương sai để tìm hiểu tại sao chi phí lại vượt ngân sách" },
            { "id": "b", "text": "In bảng cân đối kế toán ra giấy và nộp cho cục thuế" },
            { "id": "c", "text": "Ước tính doanh thu 5 năm tới bằng trí tuệ nhân tạo" },
            { "id": "d", "text": "Lấy tổng số tiền chia đều cho 12 tháng kế toán" }
        ],
        "correctAnswer": "a",
        "explanation": "Diagnostic Analytics trả lời câu hỏi 'Tại sao' (Tìm nguyên nhân chi phí vượt ngân sách qua phân tích phương sai)."
    }
]

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day13\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace day specific titles
content = content.replace("Bài Tập Trắc Nghiệm Buổi 12", "Bài Tập Trắc Nghiệm Buổi 13")
content = content.replace("kiến thức của Buổi 12", "kiến thức của Buổi 13")
content = content.replace("tài liệu Buổi 12", "tài liệu Buổi 13")

json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 13 quiz updated with 30 new questions.")
