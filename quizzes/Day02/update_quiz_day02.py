import re
import json

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Satoshi Nakamoto đã tạo ra Bitcoin dựa trên niềm tin rằng internet cần một loại tiền tệ có tính chất gì?",
        "options": [
            { "id": "a", "text": "Tập trung và được quản lý bởi ngân hàng trung ương" },
            { "id": "b", "text": "Phi tập trung, bảo vệ bằng mật mã và trao đổi ngang hàng" },
            { "id": "c", "text": "Được hậu thuẫn bởi vàng hoặc bạc" },
            { "id": "d", "text": "Chỉ sử dụng để thanh toán cho các dịch vụ phần mềm" }
        ],
        "correctAnswer": "b",
        "explanation": "Nakamoto tin rằng internet cần một loại tiền tệ phi tập trung (decentralized), được bảo vệ bằng mật mã (cryptography) và thuận lợi cho trao đổi ngang hàng (peer-to-peer exchange)."
    },
    # 2. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp các khái niệm sau từ cấp độ rộng nhất (bao quát nhất) đến cấp độ hẹp nhất (chuyên biệt nhất) trong khoa học máy tính:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Trí tuệ nhân tạo (AI)" },
            { "id": "2", "text": "Học máy (Machine Learning)" },
            { "id": "3", "text": "Học sâu (Deep Learning)" }
        ],
        "correctOrder": ["1", "2", "3"],
        "explanation": "Học sâu (Deep Learning) là một dạng đặc biệt của Học máy (Machine Learning), và Học máy là một nhánh của Trí tuệ nhân tạo (AI)."
    },
    # 3. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các loại tiền mã hóa với đặc điểm nổi bật của chúng:",
        "left": [
            { "id": "l1", "text": "Bitcoin" },
            { "id": "l2", "text": "Ethereum" },
            { "id": "l3", "text": "Zcash" }
        ],
        "right": [
            { "id": "r1", "text": "Nền tảng phần mềm phi tập trung cho phép chạy Hợp đồng thông minh (Smart Contracts)" },
            { "id": "r2", "text": "Tiền mã hóa đầu tiên, dựa trên mô hình ngang hàng (P2P), không phụ thuộc tổ chức phát hành" },
            { "id": "r3", "text": "Cung cấp tính năng an toàn hơn thông qua các giao dịch được che chắn (shielded transactions)" }
        ],
        "correctPairs": { "l1": "r2", "l2": "r1", "l3": "r3" },
        "explanation": "Bitcoin là tiền mã hóa tiên phong. Ethereum nổi bật với Hợp đồng thông minh. Zcash tập trung vào quyền riêng tư bằng các giao dịch được che chắn."
    },
    # 4. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Hoàn thành nhận định về sự khác biệt giữa AI, ML và Khoa học Dữ liệu:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "<span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> không cấu thành nên một nhánh của khoa học dữ liệu. Thay vào đó, <span class=\"blank-slot\" data-id=\"3\">___(3)___</span> sử dụng chúng như một bộ công cụ thống kê để giải quyết các vấn đề từ dữ liệu.",
        "words": [
            { "id": "w1", "text": "Trí tuệ nhân tạo (AI)" },
            { "id": "w2", "text": "Học máy (ML)" },
            { "id": "w3", "text": "Khoa học Dữ liệu" },
            { "id": "w4", "text": "Tự động hóa (RPA)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2", "3": "w3" },
        "explanation": "AI và ML là các công cụ mà Khoa học Dữ liệu sử dụng. Khoa học Dữ liệu là quy trình rộng hơn bao gồm thu thập, phân tích, trực quan hóa và mô hình hóa."
    },
    # 5. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Quan điểm của Tòa án Tối cao Tây Ban Nha (2019) về bản chất pháp lý của Bitcoin là gì?",
        "options": [
            { "id": "a", "text": "Bitcoin được công nhận là một loại tiền tệ hợp pháp (legal tender)" },
            { "id": "b", "text": "Bitcoin bị từ chối công nhận là tiền hợp pháp nhưng được coi là 'tài sản vô hình' (incorporeal asset)" },
            { "id": "c", "text": "Bitcoin bị cấm hoàn toàn trong các giao dịch thương mại" },
            { "id": "d", "text": "Bitcoin được coi là một dạng chứng khoán phái sinh (derivative security)" }
        ],
        "correctAnswer": "b",
        "explanation": "Bản án của Tòa án Tối cao Tây Ban Nha ngày 20/06/2019 đã từ chối công nhận Bitcoin là tiền tệ hợp pháp (money) mà coi nó là một tài sản vô hình."
    },
    # 6. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Ba trụ cột chuyên môn (theo biểu đồ Venn) tạo nên một Nhà khoa học dữ liệu (Data Scientist) là gì?",
        "options": [
            { "id": "a", "text": "Thống kê/Toán học, Khoa học máy tính, và Chuyên môn ngành (Domain expertise)" },
            { "id": "b", "text": "Tài chính kế toán, Nhân sự, và Marketing" },
            { "id": "c", "text": "Lập trình web, Thiết kế đồ họa, và Quản trị kinh doanh" },
            { "id": "d", "text": "Trí tuệ nhân tạo, Khai phá văn bản, và Lập luận máy" }
        ],
        "correctAnswer": "a",
        "explanation": "Khoa học dữ liệu là lĩnh vực liên ngành sử dụng Thống kê/Toán học, Khoa học máy tính và Chuyên môn trong lĩnh vực cụ thể."
    },
    # 7. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép nối các khái niệm trong Vũ trụ ảo (Metaverse) với ý nghĩa của chúng:",
        "left": [
            { "id": "l1", "text": "Vũ trụ ảo mã hóa (Crypto-metaverse)" },
            { "id": "l2", "text": "Giao dịch thuật toán (Algorithmic trading)" },
            { "id": "l3", "text": "Tài chính phi tập trung (DeFi) trong Metaverse" }
        ],
        "right": [
            { "id": "r1", "text": "Sự tích hợp mạnh mẽ giữa công nghệ chuỗi khối và tiền mã hóa vào các môi trường ảo" },
            { "id": "r2", "text": "Thực hiện giao dịch tự động trên thị trường nhờ các thuật toán AI" },
            { "id": "r3", "text": "Cho phép người dùng đi vay, cho vay và kiếm lợi nhuận ngay trong thế giới ảo mà không cần ngân hàng truyền thống" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Metaverse sử dụng Crypto (blockchain/coin) làm nền tảng kinh tế. AI hỗ trợ giao dịch thuật toán tự động. DeFi giúp giao dịch tài chính không cần trung gian."
    },
    # 8. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Quy trình ứng dụng NFT (được tạo bởi AI) làm tài sản thế chấp trong hệ sinh thái DeFi diễn ra theo trình tự nào?",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "AI sáng tạo hoặc hợp tác với nghệ sĩ để tạo ra tác phẩm nghệ thuật số" },
            { "id": "2", "text": "Tác phẩm nghệ thuật số được mã hóa (tokenized) thành một NFT trên chuỗi khối" },
            { "id": "3", "text": "Người dùng mang NFT này thế chấp (collateral) vào một nền tảng DeFi" },
            { "id": "4", "text": "Người dùng nhận được khoản vay (bằng crypto) mà không cần phải bán đứt NFT" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Đầu tiên tạo tác phẩm (bằng AI) -> Mã hóa thành NFT -> Thế chấp trên DeFi -> Nhận khoản vay. Đây là ứng dụng thanh khoản mới cho NFT."
    },
    # 9. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ thích hợp để hoàn thành khái niệm về sự kết hợp giữa Chuỗi khối và AI:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "<span class=\"blank-slot\" data-id=\"1\">___(1)___</span> cung cấp tính minh bạch, bảo mật và hồ sơ giao dịch không thể sửa đổi. Trong khi đó, <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> đóng góp vào việc phân tích dự đoán và tự động hóa theo thời gian thực.",
        "words": [
            { "id": "w1", "text": "Công nghệ Chuỗi khối (Blockchain)" },
            { "id": "w2", "text": "Trí tuệ nhân tạo (AI)" },
            { "id": "w3", "text": "Dữ liệu lớn (Big Data)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Blockchain bảo đảm dữ liệu an toàn và bất biến, còn AI dùng dữ liệu đó để phân tích và đưa ra quyết định dự đoán."
    },
    # 10. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "CBDC (Central Bank Digital Currency) là gì?",
        "options": [
            { "id": "a", "text": "Đồng tiền ảo do một nhóm lập trình viên ẩn danh tạo ra" },
            { "id": "b", "text": "Tiền kỹ thuật số được phát hành và kiểm soát bởi ngân hàng trung ương của một quốc gia" },
            { "id": "c", "text": "Một thuật toán khai phá dữ liệu trên thị trường chứng khoán" },
            { "id": "d", "text": "Hệ thống máy chủ đám mây của các ngân hàng thương mại" }
        ],
        "correctAnswer": "b",
        "explanation": "CBDC (Central Bank Digital Currency) là nỗ lực của các chính phủ bước vào cuộc chơi tài sản kỹ thuật số nhằm phát hành tiền kỹ thuật số mang tính quốc gia."
    },
    # 11. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Theo quan điểm của Tổng biện lý (Advocate General), lý do chính khiến Bitcoin KHÔNG được coi là 'Tiền' là gì?",
        "options": [
            { "id": "a", "text": "Vì nó chỉ được sử dụng ở Châu Âu" },
            { "id": "b", "text": "Vì nó không thực hiện đủ 3 chức năng: phương tiện trao đổi, công cụ lưu trữ giá trị, và đơn vị kế toán, đồng thời không được thực thể trung tâm nào hậu thuẫn" },
            { "id": "c", "text": "Vì giá trị vốn hóa của nó còn quá thấp (dưới 1 triệu Euro)" },
            { "id": "d", "text": "Vì nó sử dụng công nghệ chuỗi khối quá phức tạp" }
        ],
        "correctAnswer": "b",
        "explanation": "Tổng biện lý cho rằng Bitcoin chậm chạp, tốn kém, không đảm bảo chuyển đổi ra tiền mặt và không có sự quản lý/hậu thuẫn từ cơ quan công quyền, nên không thực hiện đủ chức năng của tiền."
    },
    # 12. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Sự khác biệt giữa Nhà khoa học dữ liệu và Nhà phân tích kinh doanh/dữ liệu:",
        "left": [
            { "id": "l1", "text": "Nhà phân tích kinh doanh (Business Analyst)" },
            { "id": "l2", "text": "Nhà khoa học dữ liệu (Data Scientist)" }
        ],
        "right": [
            { "id": "r1", "text": "Sử dụng chuyên môn ngành và phân tích để tạo insight, ít tập trung vào lập trình mô hình học máy" },
            { "id": "r2", "text": "Vai trò rộng hơn, bao gồm lập trình, phân tích thống kê và xây dựng mô hình học máy (Machine Learning)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2" },
        "explanation": "Business Analyst tập trung vào business insight. Data Scientist có kỹ năng lập trình và toán học cao hơn để xây dựng các mô hình dự đoán (ML/AI)."
    },
    # 13. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Quá trình một Nhà khoa học dữ liệu giải quyết vấn đề bằng Học máy diễn ra theo các bước chung nào?",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập dữ liệu (Data collection)" },
            { "id": "2", "text": "Xử lý và làm sạch dữ liệu (Data processing)" },
            { "id": "3", "text": "Xây dựng mô hình Học máy (Modeling)" },
            { "id": "4", "text": "Đưa ra các dự đoán và trực quan hóa kết quả" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quy trình tiêu chuẩn: Thu thập -> Tiền xử lý (làm sạch) -> Xây dựng mô hình -> Dự đoán/Đánh giá."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ vào chỗ trống liên quan đến rủi ro không gian mạng của Metaverse:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Sự xuất hiện của vũ trụ ảo làm tăng bề mặt tấn công cho các đối tượng độc hại bằng cách tạo ra nhiều điểm xâm nhập hơn cho <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và các vụ <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "phần mềm độc hại (malware)" },
            { "id": "w2", "text": "rò rỉ dữ liệu (data breaches)" },
            { "id": "w3", "text": "tiền ảo (virtual money)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Quá trình số hóa và tích hợp Metaverse mang lại rủi ro lớn về an ninh mạng như malware và rò rỉ dữ liệu do tăng số lượng điểm xâm nhập."
    },
    # 15. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Hợp đồng thông minh (Smart Contracts) hoạt động trên công nghệ nào?",
        "options": [
            { "id": "a", "text": "Dữ liệu lớn (Big Data)" },
            { "id": "b", "text": "Chuỗi khối (Blockchain)" },
            { "id": "c", "text": "Máy chủ ngân hàng tập trung" },
            { "id": "d", "text": "Các hệ thống ERP truyền thống" }
        ],
        "correctAnswer": "b",
        "explanation": "Hợp đồng thông minh là các đoạn mã chạy trên nền tảng Chuỗi khối (Blockchain) như Ethereum, tự động thực thi các thỏa thuận mà không cần bên trung gian."
    },
    # 16. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Sự kết hợp giữa Chuỗi khối và AI mang lại lợi ích gì trong tài chính?",
        "left": [
            { "id": "l1", "text": "Tính minh bạch từ Chuỗi khối" },
            { "id": "l2", "text": "Khả năng phân tích của AI" },
            { "id": "l3", "text": "Cố vấn rô-bốt (Robo-advisors)" }
        ],
        "right": [
            { "id": "r1", "text": "Đảm bảo tất cả các bên có quyền truy cập vào một phiên bản thống nhất của sự thật (bất biến)" },
            { "id": "r2", "text": "Chủ động xác định các mối đe dọa tiềm ẩn (như gian lận) theo thời gian thực" },
            { "id": "r3", "text": "Đưa ra các đề xuất đầu tư được cá nhân hóa dựa trên phân tích dự đoán" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Blockchain bảo đảm dữ liệu. AI xử lý phân tích và phát hiện rủi ro. Cố vấn rô-bốt kết hợp AI để tự động hóa tư vấn đầu tư."
    },
    # 17. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Tại sao một số người cho rằng Bitcoin cần có các trung gian tài chính để phát triển thành một loại tiền tệ ổn định?",
        "options": [
            { "id": "a", "text": "Vì Blockchain không đủ bảo mật để lưu trữ Bitcoin" },
            { "id": "b", "text": "Vì cần trung gian để cho phép 'khám phá giá' (price discovery) và tạo quỹ hoán đổi danh mục (ETFs)" },
            { "id": "c", "text": "Vì chính phủ yêu cầu mọi người dân phải gửi Bitcoin vào ngân hàng" },
            { "id": "d", "text": "Vì Bitcoin có chi phí giao dịch quá đắt nếu không qua ngân hàng" }
        ],
        "correctAnswer": "b",
        "explanation": "John O. McGinnis lập luận rằng Bitcoin cần các cơ chế tài chính như ETF và sự 'khám phá giá' (do trung gian thực hiện) để có chiều sâu thị trường và ổn định hơn, dù nó được sinh ra để chống lại trung gian."
    },
    # 18. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp quá trình AI hỗ trợ quản lý thị trường NFT:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập dữ liệu xu hướng thị trường và sở thích của người mua" },
            { "id": "2", "text": "AI phân tích dữ liệu bằng các thuật toán tiên tiến" },
            { "id": "3", "text": "Đề xuất các tác phẩm nghệ thuật NFT phù hợp cho người mua tiềm năng" },
            { "id": "4", "text": "Đồng thời AI quét để phát hiện các vi phạm bản quyền hoặc bản sao (duplicates)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "AI vừa đóng vai trò như hệ thống đề xuất (tương tự Amazon/Netflix) cho NFT, vừa đóng vai trò kiểm duyệt (xác thực tính nguyên bản) trên thị trường."
    },
    # 19. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ vào định nghĩa về Ngân hàng ảo:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Ngân hàng ảo (virtual banking) khác biệt so với ngân hàng điện tử (electronic banking) ở chỗ nó không phụ thuộc vào bất kỳ <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> nào. Chúng cung cấp quy trình mở tài khoản nhanh chóng và tuân thủ các yêu cầu <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> thông qua công nghệ kỹ thuật số.",
        "words": [
            { "id": "w1", "text": "cơ sở hạ tầng vật lý (phòng giao dịch)" },
            { "id": "w2", "text": "KYC (Nhận biết khách hàng)" },
            { "id": "w3", "text": "thị trường chứng khoán" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Ngân hàng ảo hoạt động 100% online không cần chi nhánh vật lý, và sử dụng e-KYC để định danh khách hàng."
    },
    # 20. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Nhận định nào sau đây là ĐÚNG về Dữ liệu lớn (Big Data)?",
        "options": [
            { "id": "a", "text": "Dữ liệu lớn là một nhánh nhỏ của Khoa học dữ liệu." },
            { "id": "b", "text": "Dữ liệu lớn là lượng dữ liệu rất lớn mà các công cụ cơ sở dữ liệu truyền thống không thể quản lý và phân tích được." },
            { "id": "c", "text": "Dữ liệu lớn chỉ chứa dữ liệu ở dạng văn bản (text)." },
            { "id": "d", "text": "Chỉ các tập đoàn công nghệ mới được phép sở hữu Dữ liệu lớn." }
        ],
        "correctAnswer": "b",
        "explanation": "Big Data có khối lượng, tốc độ, độ đa dạng... vượt qua khả năng của các hệ thống cơ sở dữ liệu quan hệ truyền thống."
    },
    # 21. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các quy định / chính sách với mục đích của nó trong hệ thống tài chính & blockchain:",
        "left": [
            { "id": "l1", "text": "AML (Anti-Money Laundering)" },
            { "id": "l2", "text": "KYC (Know Your Customer)" },
            { "id": "l3", "text": "GDPR (Quy định chung về Bảo vệ Dữ liệu)" }
        ],
        "right": [
            { "id": "r1", "text": "Quy định chống rửa tiền, ngăn chặn việc hợp pháp hóa nguồn tiền bất hợp pháp" },
            { "id": "r2", "text": "Quy trình xác minh danh tính và đánh giá rủi ro của khách hàng" },
            { "id": "r3", "text": "Luật bảo vệ quyền riêng tư và dữ liệu cá nhân (điển hình tại Châu Âu)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Các mô hình phát hiện gian lận dựa trên Blockchain/AI phải tuân thủ nghiêm ngặt AML, KYC và GDPR để đảm bảo minh bạch và tính pháp lý."
    },
    # 22. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Theo Michael Conklin, việc các doanh nghiệp đầu tư và chấp nhận tiền mã hóa như một phương thức thanh toán có thể vi phạm điều gì?",
        "options": [
            { "id": "a", "text": "Luật chống độc quyền của Hoa Kỳ" },
            { "id": "b", "text": "Lý thuyết các bên liên quan (stakeholder theory) của đạo đức doanh nghiệp" },
            { "id": "c", "text": "Luật bảo vệ môi trường do việc đào coin tiêu tốn nhiều năng lượng" },
            { "id": "d", "text": "Công ước Geneva về tiền tệ quốc tế" }
        ],
        "correctAnswer": "b",
        "explanation": "Conklin cho rằng do tính biến động cao và các rủi ro khác, việc doanh nghiệp đầu tư tiền mã hóa là vi phạm lý thuyết các bên liên quan (bảo vệ lợi ích của cổ đông, nhân viên...) trong đạo đức doanh nghiệp."
    },
    # 23. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ thích hợp nói về sự sáng tạo của AI và NFT:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Sự đổi mới xuất hiện khi triển khai các ý tưởng mới. Nếu <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> tự chủ tạo ra các tác phẩm nghệ thuật, điều này gây ra các tranh cãi liên quan đến quyền tác giả (authorship) và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> khi mã hóa thành NFT.",
        "words": [
            { "id": "w1", "text": "Trí tuệ nhân tạo (AI)" },
            { "id": "w2", "text": "bản quyền (copyright)" },
            { "id": "w3", "text": "thế chấp (collateral)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Khi AI tạo ra nghệ thuật, việc xác định ai sở hữu 'bản quyền' và 'quyền tác giả' trở nên phức tạp, nhất là khi chúng được thương mại hóa qua NFT."
    },
    # 24. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp quá trình tiến hóa của tiền tệ theo lịch sử (từ cũ đến mới) dựa trên tài liệu đọc:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Tiền kim loại / Tiền xu (Specie extraction)" },
            { "id": "2", "text": "Tiền giấy và sự quản lý cung tiền bằng chính sách tiền tệ của Ngân hàng trung ương" },
            { "id": "3", "text": "Chuyển tiền điện tử (Electronic money/banking)" },
            { "id": "4", "text": "Tiền mã hóa phi tập trung (Cryptocurrencies) và Tiền kỹ thuật số của NHTW (CBDC)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Lịch sử tiền tệ: Kim loại -> Giấy do Nhà nước quản lý -> Tiền điện tử (thẻ/app) -> Crypto (phi tập trung) và CBDC."
    },
    # 25. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Điều gì là RÀO CẢN lớn nhất đối với sự đổi mới có trách nhiệm trong hệ sinh thái tiền mã hóa hiện nay?",
        "options": [
            { "id": "a", "text": "Tốc độ internet quá chậm" },
            { "id": "b", "text": "Thiếu sự chắc chắn về mặt pháp lý (Legal uncertainty)" },
            { "id": "c", "text": "Không có đủ máy tính để đào coin" },
            { "id": "d", "text": "Sự phản đối của các nhà đầu tư bán lẻ" }
        ],
        "correctAnswer": "b",
        "explanation": "Tài liệu nêu rõ: Việc thiếu sự chắc chắn về mặt pháp lý là một 'rào cản khổng lồ' đối với sự đổi mới có trách nhiệm trong hệ sinh thái tiền mã hóa."
    },
    # 26. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công nghệ với tính năng cốt lõi của chúng trong tài chính ảo:",
        "left": [
            { "id": "l1", "text": "Thực tế tăng cường (AR) / Thực tế ảo (VR)" },
            { "id": "l2", "text": "DeFi (Tài chính phi tập trung)" },
            { "id": "l3", "text": "NFTs (Non-Fungible Tokens)" }
        ],
        "right": [
            { "id": "r1", "text": "Vật chất hóa không gian hiển thị và tương tác của Vũ trụ ảo (Metaverse)" },
            { "id": "r2", "text": "Cung cấp dịch vụ vay, cho vay không cần qua trung gian ngân hàng" },
            { "id": "r3", "text": "Đại diện chứng nhận tính sở hữu độc nhất cho các tài sản kỹ thuật số hoặc nghệ thuật" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "AR/VR tạo ra môi trường ảo (Metaverse). DeFi thay thế chức năng ngân hàng truyền thống. NFT đảm bảo tính độc nhất của tài sản kỹ thuật số."
    },
    # 27. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Tính năng nào KHÔNG phải là đặc điểm của công nghệ Chuỗi khối (Blockchain)?",
        "options": [
            { "id": "a", "text": "Phi tập trung (Decentralized)" },
            { "id": "b", "text": "Bảo mật bằng mật mã (Cryptographically secured)" },
            { "id": "c", "text": "Dữ liệu có thể dễ dàng bị chỉnh sửa bởi bất kỳ ai" },
            { "id": "d", "text": "Sổ cái công khai phân tán (Distributed public ledger)" }
        ],
        "correctAnswer": "c",
        "explanation": "Đặc trưng lớn nhất của Blockchain là tính bất biến; một khi dữ liệu được ghi lại, nó KHÔNG bị ảnh hưởng bởi việc sửa đổi."
    },
    # 28. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ vào chỗ trống về đặc tính của học sâu (Deep learning):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Các thuật toán học máy đôi khi gặp hạn chế vì hiệu suất phụ thuộc vào cách dữ liệu được chuẩn bị. <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> giải quyết vấn đề này bằng cách tự mình trích xuất thông tin, giúp cho việc học của máy tính trở nên mạnh mẽ, linh hoạt và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> hơn.",
        "words": [
            { "id": "w1", "text": "Học sâu (Deep Learning)" },
            { "id": "w2", "text": "trừu tượng (abstract)" },
            { "id": "w3", "text": "Cơ sở dữ liệu (Database)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Deep Learning tự động trích xuất các đặc trưng (features) từ dữ liệu thô, giúp quá trình nhận diện linh hoạt và trừu tượng hơn ML truyền thống."
    },
    # 29. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Trình tự tích hợp tài sản vật lý vào nền kinh tế kỹ thuật số DeFi:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Xác định tài sản thế giới thực (bất động sản, hàng xa xỉ)" },
            { "id": "2", "text": "Mã hóa (Tokenize) chứng thư sở hữu của tài sản thành NFT" },
            { "id": "3", "text": "Đưa NFT lên giao dịch hoặc làm tài sản thế chấp trong hệ sinh thái DeFi" },
            { "id": "4", "text": "Tăng cường tính thanh khoản và mở rộng cơ hội đầu tư cho tài sản đó" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Mã hóa tài sản thực (RWA - Real World Assets) bắt đầu từ việc chọn tài sản -> biến thành NFT -> thế chấp trên DeFi -> tạo thanh khoản."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Việc sử dụng thuật toán (ví dụ GNN) để phát hiện gian lận tài chính trong Blockchain/AI cần đáp ứng điều kiện tiên quyết nào?",
        "options": [
            { "id": "a", "text": "Phải có nguồn dữ liệu bí mật từ hacker" },
            { "id": "b", "text": "Phải minh bạch, có thể kiểm toán được và tuân thủ các quy định về AML, KYC, GDPR" },
            { "id": "c", "text": "Chỉ hoạt động được với Bitcoin, không dùng cho các coin khác" },
            { "id": "d", "text": "Hệ thống phải tự động đóng băng tài khoản mà không cần con người xem xét" }
        ],
        "correctAnswer": "b",
        "explanation": "Các mô hình phát hiện gian lận dựa trên GNN phải tuân thủ các quy định về AML, KYC và GDPR; điều này có nghĩa là hệ thống phải minh bạch và có thể kiểm toán."
    }
]

import os

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day02\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the title and headers
content = content.replace("Bài Tập Trắc Nghiệm Buổi 1", "Bài Tập Trắc Nghiệm Buổi 2")
content = content.replace("kiến thức của Buổi 1", "kiến thức của Buổi 2")
content = content.replace("tài liệu Buổi 1", "tài liệu Buổi 2")

# Replace the questions array
json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 02 quiz updated with 30 new questions.")
