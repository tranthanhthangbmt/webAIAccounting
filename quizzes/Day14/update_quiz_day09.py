import re
import json
import os

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Mục đích chính của Toàn cầu hóa tài chính (Financial Globalization) là gì?",
        "options": [
            { "id": "a", "text": "Hội nhập thị trường tài chính trong nước và quốc tế" },
            { "id": "b", "text": "Ngăn chặn các nhà đầu tư nước ngoài mua cổ phiếu" },
            { "id": "c", "text": "Xóa bỏ hoàn toàn các loại tiền tệ của các quốc gia" },
            { "id": "d", "text": "Chỉ phát triển thị trường nội địa bằng tiền mặt thật" }
        ],
        "correctAnswer": "a",
        "explanation": "Toàn cầu hóa tài chính là sự hội nhập ngày càng tăng của thị trường tài chính trong nước và quốc tế."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Tính năng bất biến (Immutability) của công nghệ Blockchain mang lại lợi ích gì?",
        "options": [
            { "id": "a", "text": "Từ chối mọi sửa đổi bất hợp pháp đối với giao dịch" },
            { "id": "b", "text": "Cho phép thay đổi lịch sử để sửa lỗi một cách dễ dàng" },
            { "id": "c", "text": "Tăng cường tốc độ xử lý dữ liệu lên gấp hàng trăm lần" },
            { "id": "d", "text": "Xóa toàn bộ các giao dịch cũ để giải phóng bộ nhớ lưu" }
        ],
        "correctAnswer": "a",
        "explanation": "Blockchain tạo ra một sổ cái bất biến, nơi dữ liệu giao dịch đã ghi không thể bị thay đổi."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các thuật ngữ liên quan đến tiền điện tử và tài chính phi tập trung:",
        "left": [
            { "id": "l1", "text": "DeFi" },
            { "id": "l2", "text": "CBDC" },
            { "id": "l3", "text": "Smart Contract" }
        ],
        "right": [
            { "id": "r1", "text": "Tài chính phi tập trung" },
            { "id": "r2", "text": "Tiền kỹ thuật số của Ngân hàng Trung ương" },
            { "id": "r3", "text": "Hợp đồng thông minh tự động thực thi" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "DeFi: Decentralized Finance; CBDC: Central Bank Digital Currency; Smart Contract: Hợp đồng thông minh."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp thứ tự các mức độ từ truyền thống đến phi tập trung trong dịch vụ tài chính:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Ngân hàng thương mại truyền thống giao dịch bằng tiền giấy" },
            { "id": "2", "text": "Dịch vụ tài chính trực tuyến, ngân hàng số (Fintech)" },
            { "id": "3", "text": "Sử dụng tiền điện tử trên sàn giao dịch tập trung (CeFi)" },
            { "id": "4", "text": "Tài chính phi tập trung hoàn toàn bằng Hợp đồng thông minh (DeFi)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quá trình số hóa diễn ra từ ngân hàng truyền thống (tiền giấy) -> Fintech (ngân hàng số) -> CeFi -> DeFi (không có trung gian)."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về tác động của số hóa đối với nền kinh tế:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Số hóa tạo cơ hội cho các sản phẩm và dịch vụ mới, do đó không chỉ nâng cao hiệu quả của luồng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> mà còn theo dõi và nhận biết <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "hàng tồn kho" },
            { "id": "w2", "text": "khách hàng" },
            { "id": "w3", "text": "giám đốc điều hành" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Số hóa giúp tối ưu hóa hàng tồn kho (chuỗi cung ứng) và nhận diện/chăm sóc khách hàng (CRM)."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Trong không gian DeFi (Tài chính phi tập trung), vì sao các khoản vay thường yêu cầu thế chấp quá mức (over-collateralization)?",
        "options": [
            { "id": "a", "text": "Bù đắp rủi ro do tính ẩn danh và tiền điện tử biến động" },
            { "id": "b", "text": "Để ngân hàng trung ương có thể thu thuế một cách dễ dàng" },
            { "id": "c", "text": "Khuyến khích người vay mua thêm nhiều tài sản vật chất" },
            { "id": "d", "text": "Giúp sàn giao dịch thu được phí hoa hồng cao hơn rất nhiều" }
        ],
        "correctAnswer": "a",
        "explanation": "Trong DeFi, người vay ẩn danh nên không thể đánh giá rủi ro tín dụng (như chấm điểm tín dụng), do đó phải dùng thế chấp quá mức để bù đắp rủi ro biến động giá tiền điện tử."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Tập trung hóa (Centralization) trong hệ thống tài chính có đặc điểm gì?",
        "options": [
            { "id": "a", "text": "Sổ cái tập trung ghi lại tất cả dữ liệu giao dịch" },
            { "id": "b", "text": "Tất cả người dùng đều có quyền biểu quyết ngang nhau" },
            { "id": "c", "text": "Dữ liệu được lưu trữ ngẫu nhiên trên máy tính cá nhân" },
            { "id": "d", "text": "Không có bất kỳ sự can thiệp của chính phủ hay pháp luật" }
        ],
        "correctAnswer": "a",
        "explanation": "Tập trung hóa đặc trưng bởi một tổ chức/cơ quan trung ương kiểm soát sổ cái và quyết định."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các khái niệm tài chính tiền mã hóa với rủi ro tương ứng:",
        "left": [
            { "id": "l1", "text": "Oracles trong DeFi" },
            { "id": "l2", "text": "Smart Contract" },
            { "id": "l3", "text": "Tiền điện tử (như Bitcoin)" }
        ],
        "right": [
            { "id": "r1", "text": "Rủi ro nhà cung cấp bên thứ 3 cấp sai thông tin thị trường" },
            { "id": "r2", "text": "Rủi ro xuất hiện lỗ hổng lập trình khiến quỹ bị tin tặc bòn rút" },
            { "id": "r3", "text": "Tính biến động giá cả rất cao, cản trở việc trở thành tiền tệ" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Oracle cung cấp dữ liệu ngoài chuỗi nên có rủi ro tin giả; Hợp đồng thông minh rủi ro code; Tiền điện tử rủi ro biến động giá."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về Cố vấn Robot (Robo-Advisors):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Robo-advisors cung cấp dịch vụ quản lý danh mục đầu tư bằng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> tự động, với chi phí <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> so với cố vấn con người truyền thống.",
        "words": [
            { "id": "w1", "text": "thuật toán" },
            { "id": "w2", "text": "thấp hơn" },
            { "id": "w3", "text": "cao hơn rất nhiều" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Robo-advisors sử dụng thuật toán để phân bổ tài sản với chi phí thấp."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp trình tự hoạt động của một Hợp đồng thông minh (Smart Contract) trong DeFi:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Lập trình viên viết mã điều kiện (VD: Nếu giá > X thì bán)" },
            { "id": "2", "text": "Triển khai đoạn mã đó lên mạng lưới Blockchain (VD: Ethereum)" },
            { "id": "3", "text": "Oracle cung cấp dữ liệu giá từ bên ngoài vào Blockchain" },
            { "id": "4", "text": "Hợp đồng thông minh tự động thực thi khi điều kiện thỏa mãn" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Viết mã -> Đưa lên Blockchain -> Nhận dữ liệu (Oracle) -> Tự động kích hoạt thực thi."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Stablecoin được tạo ra nhằm giải quyết vấn đề gì của tiền điện tử?",
        "options": [
            { "id": "a", "text": "Giảm thiểu tính biến động giá cả quá lớn" },
            { "id": "b", "text": "Tăng tốc độ khai thác Bitcoin lên nhiều lần" },
            { "id": "c", "text": "Thay thế hoàn toàn mạng lưới Internet hiện tại" },
            { "id": "d", "text": "Ngăn chặn chính phủ phát hành tiền pháp định" }
        ],
        "correctAnswer": "a",
        "explanation": "Stablecoin được gắn giá trị với một tài sản ổn định (như USD) để khắc phục tính biến động lớn của tiền điện tử."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "CBDC (Central Bank Digital Currency) là gì?",
        "options": [
            { "id": "a", "text": "Tiền kỹ thuật số do Ngân hàng Trung ương phát hành" },
            { "id": "b", "text": "Một loại thẻ tín dụng mới dành riêng cho sinh viên" },
            { "id": "c", "text": "Tên gọi khác của Bitcoin tại thị trường chứng khoán" },
            { "id": "d", "text": "Công cụ chỉ để vay vốn mua nhà của các ngân hàng" }
        ],
        "correctAnswer": "a",
        "explanation": "CBDC là tiền kỹ thuật số chính thức được phát hành và kiểm soát bởi Ngân hàng Trung ương của một quốc gia."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công nghệ / khái niệm với vai trò tương ứng:",
        "left": [
            { "id": "l1", "text": "Điện toán đám mây (Cloud Computing)" },
            { "id": "l2", "text": "Stablecoin" },
            { "id": "l3", "text": "Giao dịch nội gián (Insider Trading)" }
        ],
        "right": [
            { "id": "r1", "text": "Cung cấp hạ tầng số tập trung cho phép lưu trữ và xử lý lớn" },
            { "id": "r2", "text": "Đồng tiền điện tử neo giá trị vào tài sản thực tế" },
            { "id": "r3", "text": "Hành vi giao dịch bất hợp pháp dựa trên thông tin chưa công bố" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Cloud lưu trữ/xử lý; Stablecoin neo giá; Giao dịch nội gián dùng thông tin riêng tư trục lợi."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về sự khác biệt giữa CeFi và DeFi:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong CeFi, niềm tin được xây dựng dựa trên danh tiếng của <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Ngược lại, trong DeFi, niềm tin được tạo ra nhờ tính minh bạch và thuật toán của <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "tổ chức trung gian" },
            { "id": "w2", "text": "công nghệ blockchain" },
            { "id": "w3", "text": "hệ thống kiểm toán" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "CeFi dựa vào người trung gian (như ngân hàng, sàn giao dịch). DeFi dựa vào mã nguồn và Blockchain (trustless)."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp quá trình phát triển của tiền tệ:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Hệ thống hàng đổi hàng và tiền kim loại quý (Vàng, bạc)" },
            { "id": "2", "text": "Tiền pháp định (Fiat) do chính phủ in ấn bằng tiền giấy" },
            { "id": "3", "text": "Hệ thống thanh toán kỹ thuật số và thẻ ngân hàng" },
            { "id": "4", "text": "Tiền điện tử phi tập trung và Tiền kỹ thuật số Ngân hàng Trung ương (CBDC)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Sự phát triển từ tiền hàng hóa -> Tiền pháp định giấy -> Thanh toán điện tử -> Tiền mã hóa & CBDC."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Tiền kỹ thuật số CBDC giúp ngân hàng trung ương đạt được mục tiêu nào?",
        "options": [
            { "id": "a", "text": "Duy trì ổn định tài chính và giới hạn tiền ảo tư nhân" },
            { "id": "b", "text": "Giúp người dùng dễ dàng ẩn danh khi mua hàng hóa" },
            { "id": "c", "text": "Loại bỏ hoàn toàn công nghệ trí tuệ nhân tạo (AI)" },
            { "id": "d", "text": "Từ bỏ trách nhiệm quản lý lạm phát của quốc gia đó" }
        ],
        "correctAnswer": "a",
        "explanation": "CBDC giúp ngân hàng trung ương giữ vai trò phát hành tiền, đảm bảo an toàn tài chính, hạn chế sự thống trị của tiền ảo tư nhân."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các mô hình hệ thống với đặc trưng:",
        "left": [
            { "id": "l1", "text": "Tập trung (Centralized)" },
            { "id": "l2", "text": "Phi tập trung (Decentralized)" }
        ],
        "right": [
            { "id": "r1", "text": "Dữ liệu và quyết định nằm trong tay một tổ chức duy nhất" },
            { "id": "r2", "text": "Quyền lực phân tán, giao dịch ngang hàng (P2P)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2" },
        "explanation": "Tập trung là 1 trung tâm quyền lực; Phi tập trung là mạng lưới ngang hàng P2P không có trung gian."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Tại sao AI được kỳ vọng có thể giảm thiểu giao dịch nội gián trong quá trình M&A xuyên biên giới?",
        "options": [
            { "id": "a", "text": "AI phát hiện hành vi bất thường và ngăn chặn kịp thời" },
            { "id": "b", "text": "AI sẽ trực tiếp tiến hành thu hồi tiền của người vi phạm" },
            { "id": "c", "text": "AI hoàn toàn tự động thực hiện mọi giao dịch nội gián" },
            { "id": "d", "text": "AI buộc mọi nhà đầu tư phải nộp thêm thuế thu nhập" }
        ],
        "correctAnswer": "a",
        "explanation": "AI có khả năng phát hiện các luồng tiền, hành vi giao dịch chứng khoán bất thường (mua gom trước khi công bố thông tin)."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ về rủi ro của DeFi:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Bất chấp tính ưu việt, DeFi vẫn đối mặt với rủi ro <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> cao của tiền mã hóa và sự không chắc chắn về <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> do thiếu kiểm tra nhận diện khách hàng KYC.",
        "words": [
            { "id": "w1", "text": "biến động (volatility)" },
            { "id": "w2", "text": "pháp lý, quy định" },
            { "id": "w3", "text": "máy chủ trung tâm" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "DeFi có rủi ro về độ biến động lớn và các vấn đề quy định (chưa tuân thủ KYC/AML)."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Số hóa (Digitalization) đem lại lợi thế kinh tế theo quy mô như thế nào cho các tập đoàn công nghệ lớn?",
        "options": [
            { "id": "a", "text": "Chi phí cố định cao nhưng chi phí cận biên giảm dần" },
            { "id": "b", "text": "Cả chi phí cố định và chi phí cận biên đều tăng cao" },
            { "id": "c", "text": "Không cần đầu tư vốn mà vẫn có lợi nhuận tối đa" },
            { "id": "d", "text": "Chỉ các tập đoàn có nhiều nhân sự mới có lợi nhuận" }
        ],
        "correctAnswer": "a",
        "explanation": "Số hóa (như phát triển phần mềm) tốn chi phí cố định tạo ra ban đầu, nhưng việc phân phối sản phẩm số tốn rất ít chi phí cận biên."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp sự tham gia của Robo-Advisor trong quản lý tài sản:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Khảo sát mức độ chấp nhận rủi ro của khách hàng" },
            { "id": "2", "text": "Thuật toán gợi ý danh mục đầu tư phù hợp (ETF, cổ phiếu)" },
            { "id": "3", "text": "Khách hàng đồng ý và nộp tiền vào hệ thống" },
            { "id": "4", "text": "Hệ thống tự động tái cân bằng danh mục theo thời gian" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Đánh giá rủi ro -> Gợi ý danh mục -> Đầu tư tiền -> Tự động tái cân bằng."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các công nghệ / tổ chức với vai trò quản trị:",
        "left": [
            { "id": "l1", "text": "Thuật toán Đồng thuận (Consensus)" },
            { "id": "l2", "text": "Ngân hàng Trung ương" },
            { "id": "l3", "text": "Cơ quan Quản lý (SEC)" }
        ],
        "right": [
            { "id": "r1", "text": "Duy trì tính nhất quán của mạng lưới Blockchain phi tập trung" },
            { "id": "r2", "text": "Quản lý lạm phát và phát hành tiền tệ hợp pháp (như CBDC)" },
            { "id": "r3", "text": "Điều tra, trừng phạt các hành vi giao dịch nội gián phi pháp" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Consensus trong blockchain thay thế tổ chức trung ương; Ngân hàng phát hành tiền; SEC quản lý thị trường chứng khoán."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Tính minh bạch (Transparency) của chuỗi khối (Blockchain) cũng dẫn đến lo ngại gì?",
        "options": [
            { "id": "a", "text": "Vi phạm quyền riêng tư khi dữ liệu giao dịch bị lộ" },
            { "id": "b", "text": "Chi phí mua điện thoại thông minh trở nên đắt đỏ hơn" },
            { "id": "c", "text": "Các nhân viên ngân hàng sẽ không biết sử dụng máy tính" },
            { "id": "d", "text": "Các tập đoàn đóng cửa toàn bộ nhà máy sản xuất giấy" }
        ],
        "correctAnswer": "a",
        "explanation": "Mọi giao dịch trên Blockchain public đều có thể được xem bởi bất kỳ ai, dẫn đến rủi ro lộ quyền riêng tư tài chính."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về tác động của Fintech:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Fintech tạo ra nền tảng phân phối dịch vụ tài chính <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Nó làm tăng tính <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> trong ngành, buộc các ngân hàng truyền thống phải chuyển đổi số.",
        "words": [
            { "id": "w1", "text": "nhanh chóng, thuận tiện" },
            { "id": "w2", "text": "cạnh tranh khốc liệt" },
            { "id": "w3", "text": "kiểm duyệt gắt gao" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Fintech giúp dịch vụ nhanh chóng hơn và làm tăng tính cạnh tranh trong ngành tài chính."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp mức độ phức tạp trong bảo lãnh phát hành khoản vay:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Đánh giá thủ công sổ sách chứng từ bằng giấy" },
            { "id": "2", "text": "Sử dụng điểm tín dụng truyền thống (FICO score)" },
            { "id": "3", "text": "Thu thập dữ liệu lớn (Big Data) từ mạng xã hội" },
            { "id": "4", "text": "Mô hình AI tự động duyệt khoản vay trong thời gian thực" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Từ thủ công -> Mô hình điểm số -> Big Data -> AI Real-time."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Dịch vụ P2P (Peer-to-Peer) trong tài chính phi tập trung là gì?",
        "options": [
            { "id": "a", "text": "Giao dịch ngang hàng trực tiếp không qua trung gian" },
            { "id": "b", "text": "Quy trình nộp thuế tiêu thụ đặc biệt cho nhà nước" },
            { "id": "c", "text": "Hệ thống xếp hạng mức độ uy tín của các ngân hàng" },
            { "id": "d", "text": "Gửi tin nhắn sms quảng cáo bất động sản tự động" }
        ],
        "correctAnswer": "a",
        "explanation": "P2P (Ngang hàng) là giao dịch trực tiếp giữa 2 cá nhân/thực thể mà không cần có bên thứ 3."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công cụ kỹ thuật số với chức năng chính:",
        "left": [
            { "id": "l1", "text": "AI (Trí tuệ nhân tạo)" },
            { "id": "l2", "text": "Blockchain" },
            { "id": "l3", "text": "Robo-Advisors" }
        ],
        "right": [
            { "id": "r1", "text": "Phân tích khối lượng dữ liệu khổng lồ để phát hiện mẫu" },
            { "id": "r2", "text": "Cung cấp sổ cái phi tập trung an toàn, không thể sửa đổi" },
            { "id": "r3", "text": "Tư vấn đầu tư tài chính tự động bằng thuật toán được lập sẵn" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "AI phân tích dữ liệu; Blockchain lưu trữ an toàn; Robo-Advisors hỗ trợ đầu tư."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về tác động của Tài sản vô hình (Intangible assets):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong nền kinh tế số, các đầu vào vô hình như <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và dữ liệu đóng vai trò quyết định, giúp các công ty công nghệ tạo ra giá trị khác biệt và giành lấy <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> mạnh mẽ trên thị trường.",
        "words": [
            { "id": "w1", "text": "phần mềm" },
            { "id": "w2", "text": "lợi thế cạnh tranh" },
            { "id": "w3", "text": "nhà xưởng vật lý" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Tài sản vô hình như phần mềm, dữ liệu, thuật toán giúp công ty có lợi thế cạnh tranh rất lớn so với tài sản vật lý."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp cấu trúc từ tập trung đến phi tập trung của dữ liệu người dùng:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Hồ sơ lưu trữ trên giấy tại chi nhánh ngân hàng" },
            { "id": "2", "text": "Lưu trữ máy chủ nội bộ tập trung của một ngân hàng" },
            { "id": "3", "text": "Điện toán đám mây với sự kiểm soát của nhà cung cấp dịch vụ" },
            { "id": "4", "text": "Lưu trữ phân tán trên mạng Blockchain (Không ai toàn quyền)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Lưu trữ giấy -> Máy chủ riêng -> Đám mây (tập trung) -> Blockchain (phi tập trung)."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Tiềm năng quan trọng nhất của Tài chính toàn diện (Financial Inclusion) là gì?",
        "options": [
            { "id": "a", "text": "Giúp người dân thu nhập thấp tiếp cận dịch vụ tài chính" },
            { "id": "b", "text": "Tăng phí giao dịch tại tất cả các quốc gia trên thế giới" },
            { "id": "c", "text": "Bắt buộc mọi người đều phải đầu tư vào tiền điện tử" },
            { "id": "d", "text": "Loại bỏ hoàn toàn tiền giấy trong vòng 1 tháng" }
        ],
        "correctAnswer": "a",
        "explanation": "Tài chính toàn diện nhằm cung cấp quyền tiếp cận dịch vụ ngân hàng, tín dụng, thanh toán cho mọi tầng lớp, đặc biệt là người nghèo."
    }
]

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day09\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Bài Tập Trắc Nghiệm Buổi 8", "Bài Tập Trắc Nghiệm Buổi 9")
content = content.replace("kiến thức của Buổi 8", "kiến thức của Buổi 9")
content = content.replace("tài liệu Buổi 8", "tài liệu Buổi 9")

json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 09 quiz updated with 30 new questions.")
