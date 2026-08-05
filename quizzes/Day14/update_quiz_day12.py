import re
import json
import os

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Trí tuệ nhân tạo sáng tạo (Generative AI - GAI) trong kế toán đại diện cho điều gì?",
        "options": [
            { "id": "a", "text": "Sự thay đổi mô hình xử lý, phân tích dữ liệu tài chính" },
            { "id": "b", "text": "Việc cấm hoàn toàn kế toán viên làm báo cáo thủ công" },
            { "id": "c", "text": "Hệ thống tự động in toàn bộ hóa đơn ra giấy A4" },
            { "id": "d", "text": "Máy móc vật lý thay thế 100% nhân sự văn phòng" }
        ],
        "correctAnswer": "a",
        "explanation": "GAI không chỉ là công cụ mà còn là sự thay đổi mô hình (paradigm shift) trong cách kế toán xử lý và phân tích dữ liệu."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Điều kiện tiên quyết nào KHÔNG phải là công cụ công nghệ nhưng lại rất quan trọng để tiếp cận AI?",
        "options": [
            { "id": "a", "text": "Sự tò mò trí tuệ (Intellectual Curiosity)" },
            { "id": "b", "text": "Phần mềm chống vi-rút bản quyền rất đắt" },
            { "id": "c", "text": "Máy quét tài liệu siêu tốc chuyên nghiệp" },
            { "id": "d", "text": "Một trung tâm dữ liệu khổng lồ cá nhân" }
        ],
        "correctAnswer": "a",
        "explanation": "Sự tò mò trí tuệ là nền tảng tư duy, giúp người dùng sẵn sàng khám phá và thử nghiệm phương thức mới với AI."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các công cụ phần mềm với chức năng chính của chúng khi kết hợp AI:",
        "left": [
            { "id": "l1", "text": "QuickBooks Online" },
            { "id": "l2", "text": "Tableau" },
            { "id": "l3", "text": "IBM Cognos Analytics" }
        ],
        "right": [
            { "id": "r1", "text": "Xử lý, tự động hóa sổ sách, phân loại chi phí" },
            { "id": "r2", "text": "Trực quan hóa dữ liệu bằng các biểu đồ dễ hiểu" },
            { "id": "r3", "text": "Thực hiện phân tích dự đoán và lập kế hoạch" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "QuickBooks cho sổ sách; Tableau để trực quan hóa; IBM Cognos mạnh về phân tích dự đoán."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp lộ trình chiến lược triển khai AI vào phòng kế toán doanh nghiệp:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Đánh giá quy trình hiện tại và lập kế hoạch chiến lược" },
            { "id": "2", "text": "Lựa chọn công cụ AI phù hợp với nhu cầu doanh nghiệp" },
            { "id": "3", "text": "Đào tạo nhân viên và triển khai áp dụng theo từng giai đoạn" },
            { "id": "4", "text": "Giám sát hiệu suất, thu thập phản hồi và cải tiến liên tục" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Đánh giá -> Lựa chọn công cụ -> Đào tạo & Triển khai -> Giám sát và Cải tiến."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về vai trò của AI trong phân tích dự đoán:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "AI phân tích các mẫu dữ liệu <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để dự đoán các kịch bản tài chính trong <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "lịch sử" },
            { "id": "w2", "text": "tương lai" },
            { "id": "w3", "text": "phi thực tế" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Phân tích dự đoán sử dụng dữ liệu quá khứ (lịch sử) để dự đoán xu hướng tương lai."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Sự khác biệt chính của Custom GPTs so với công cụ ChatGPT thông thường là gì?",
        "options": [
            { "id": "a", "text": "Có thể tích hợp dữ liệu, hướng dẫn nghiệp vụ và API riêng" },
            { "id": "b", "text": "Luôn luôn phản hồi nhanh hơn gấp 10 lần bản gốc" },
            { "id": "c", "text": "Chỉ hoạt động được trên các máy tính Apple Macbook" },
            { "id": "d", "text": "Yêu cầu người dùng phải tự viết toàn bộ mã nguồn" }
        ],
        "correctAnswer": "a",
        "explanation": "Custom GPTs cho phép người dùng tùy chỉnh sâu bằng cách nạp dữ liệu riêng, cài đặt hướng dẫn cụ thể và kết nối API/Actions."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Thuật ngữ 'Data Literacy' (Hiểu biết về dữ liệu) nghĩa là gì?",
        "options": [
            { "id": "a", "text": "Khả năng đọc, quản lý và giao tiếp qua dữ liệu" },
            { "id": "b", "text": "Chỉ đọc được mã nhị phân của các hệ thống" },
            { "id": "c", "text": "Viết được ngôn ngữ lập trình Python thuần thục" },
            { "id": "d", "text": "Tốc độ gõ phím và nhập số liệu thật nhanh chóng" }
        ],
        "correctAnswer": "a",
        "explanation": "Data Literacy là khả năng đọc, hiểu, quản lý và giao tiếp hiệu quả với dữ liệu."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các công ty (Case studies) với thách thức và giải pháp AI của họ:",
        "left": [
            { "id": "l1", "text": "Brewed Awakenings (Doanh nghiệp nhỏ)" },
            { "id": "l2", "text": "Cityscape Consulting (Công ty tư vấn)" },
            { "id": "l3", "text": "GlobalTech Enterprises (Tập đoàn đa quốc gia)" }
        ],
        "right": [
            { "id": "r1", "text": "Theo dõi chi phí tự động qua QuickBooks" },
            { "id": "r2", "text": "Quản lý ngân sách dự án phức tạp bằng Xero" },
            { "id": "r3", "text": "Quản lý luật thuế đa dạng bằng IBM Watson" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Brewed Awakenings dùng QuickBooks; Cityscape dùng Xero; GlobalTech dùng IBM Watson."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về hiện tượng ảo giác AI:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Mặc dù GPT rất thông minh, hiện tượng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (hallucination) vẫn có thể xảy ra, do đó kế toán viên luôn phải dùng tư duy chuyên môn để <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> thông tin.",
        "words": [
            { "id": "w1", "text": "ảo giác" },
            { "id": "w2", "text": "kiểm chứng" },
            { "id": "w3", "text": "tin tưởng" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Ảo giác (Hallucination) là khi AI bịa ra thông tin sai lệch nhưng diễn đạt rất tự tin. Cần phải kiểm chứng (verify)."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp các bước GPT tùy chỉnh thực hiện khi có kết nối API (Actions):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Người dùng đưa ra yêu cầu bằng ngôn ngữ tự nhiên" },
            { "id": "2", "text": "GPT nhận diện ý định và chuẩn bị tham số gọi API" },
            { "id": "3", "text": "GPT gửi truy vấn đến hệ thống cơ sở dữ liệu bên ngoài" },
            { "id": "4", "text": "GPT nhận kết quả trả về, tóm tắt và phản hồi người dùng" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Nhận lệnh -> Xử lý tham số -> Gọi API ngoài -> Trả kết quả cho người dùng."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Lợi ích lớn nhất của việc GAI tự động hóa các phép tính phức tạp (như khấu hao, ước tính thuế) là gì?",
        "options": [
            { "id": "a", "text": "Nâng cao tốc độ, độ chính xác và giảm thiểu sai sót" },
            { "id": "b", "text": "Giúp ngân sách công ty không phải đóng thuế thu nhập" },
            { "id": "c", "text": "Xóa bỏ hoàn toàn quy định về kiểm toán doanh nghiệp" },
            { "id": "d", "text": "Khiến việc đào tạo kế toán viên mới trở nên vô dụng" }
        ],
        "correctAnswer": "a",
        "explanation": "AI thực hiện phép tính với tốc độ cao và ít sai sót hơn con người, giúp tăng tính tuân thủ."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "GPT Store (Cửa hàng GPT) mang lại tiện ích gì cho cộng đồng người dùng?",
        "options": [
            { "id": "a", "text": "Cung cấp hàng ngàn GPT tùy chỉnh để khám phá và sử dụng" },
            { "id": "b", "text": "Là nơi mua bán thiết bị điện tử, phần cứng siêu máy tính" },
            { "id": "c", "text": "Cho phép tải các game di động hoàn toàn miễn phí" },
            { "id": "d", "text": "Chuyên phân phối các tài liệu mật của chính phủ các nước" }
        ],
        "correctAnswer": "a",
        "explanation": "GPT Store giống như App Store nhưng dành cho các Custom GPTs được cộng đồng xây dựng."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các kỹ năng cần thiết với ý nghĩa của nó đối với kế toán viên thời đại AI:",
        "left": [
            { "id": "l1", "text": "Data Literacy (Hiểu dữ liệu)" },
            { "id": "l2", "text": "Critical Thinking (Tư duy phê phán)" },
            { "id": "l3", "text": "Continuous Learning (Học tập liên tục)" }
        ],
        "right": [
            { "id": "r1", "text": "Nền tảng để điều hướng các nền tảng phân tích tài chính" },
            { "id": "r2", "text": "Chìa khóa để đánh giá tính xác thực của thông tin từ AI" },
            { "id": "r3", "text": "Bắt kịp tốc độ cải tiến công nghệ và quy định nghề nghiệp" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Data Literacy để làm việc với dữ liệu; Critical thinking để thẩm định AI; Continuous learning để không bị tụt hậu."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về rủi ro của Custom GPTs:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Khi tải lên các tài liệu tài chính nhạy cảm vào GPT, tổ chức phải đối mặt với thách thức lớn về <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và đảm bảo không xảy ra sự cố <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> thông tin.",
        "words": [
            { "id": "w1", "text": "quyền riêng tư" },
            { "id": "w2", "text": "rò rỉ" },
            { "id": "w3", "text": "biến động giá" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Quyền riêng tư (Privacy) và rò rỉ dữ liệu (Data leakage) là 2 rủi ro hàng đầu khi đưa tài liệu mật vào AI."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Các bước cơ bản để tạo một Custom GPT riêng trong ChatGPT:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Mở tab Explore và chọn 'Create a GPT'" },
            { "id": "2", "text": "Nhập hướng dẫn (Instructions) chi tiết về vai trò của GPT" },
            { "id": "3", "text": "Tải lên các tệp dữ liệu kiến thức bổ sung (Knowledge files)" },
            { "id": "4", "text": "Lưu và tùy chọn quyền chia sẻ (Chỉ mình tôi, Mọi người...)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Tạo mới -> Cấp lệnh hướng dẫn -> Nạp tài liệu tri thức -> Xuất bản (Save)."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Tính năng Actions trong Custom GPTs cho phép nó làm gì?",
        "options": [
            { "id": "a", "text": "Kết nối và tương tác với các hệ thống phần mềm bên ngoài" },
            { "id": "b", "text": "Hoạt động mà không cần kết nối mạng internet" },
            { "id": "c", "text": "Tự động tắt nguồn máy tính khi xong công việc" },
            { "id": "d", "text": "Viết mã độc để tấn công máy chủ của ngân hàng" }
        ],
        "correctAnswer": "a",
        "explanation": "Actions sử dụng API để kết nối với cơ sở dữ liệu hoặc hệ thống SaaS bên ngoài."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các ứng dụng của AI với bộ phận hoặc nghiệp vụ tương ứng:",
        "left": [
            { "id": "l1", "text": "Tự động phân loại chi phí" },
            { "id": "l2", "text": "Trợ lý hỗ trợ khách hàng 24/7" },
            { "id": "l3", "text": "Phân tích dự báo dòng tiền" }
        ],
        "right": [
            { "id": "r1", "text": "Nghiệp vụ hạch toán, kế toán sổ sách" },
            { "id": "r2", "text": "Chăm sóc khách hàng và tư vấn dịch vụ" },
            { "id": "r3", "text": "Quản trị tài chính chiến lược" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Phân loại chi phí thuộc hạch toán; Hỗ trợ 24/7 thuộc CSKH; Dự báo thuộc quản trị chiến lược."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Tại sao việc áp dụng AI theo từng giai đoạn (phased integration) lại được khuyến khích?",
        "options": [
            { "id": "a", "text": "Tránh làm gián đoạn hệ thống và giúp nhân viên dễ thích nghi" },
            { "id": "b", "text": "Vì các công cụ AI không thể xử lý dữ liệu cùng một lúc" },
            { "id": "c", "text": "Để chi phí bản quyền phần mềm rẻ hơn đáng kể mỗi năm" },
            { "id": "d", "text": "Tránh việc cơ quan thuế phát hiện doanh nghiệp gian lận" }
        ],
        "correctAnswer": "a",
        "explanation": "Tích hợp từng giai đoạn giảm thiểu rủi ro gián đoạn quy trình kinh doanh và cho phép người dùng có thời gian học hỏi."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ về tác động của AI đối với lỗi con người:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Việc tự động hóa các phép tính giúp giảm đáng kể <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, qua đó đảm bảo tính <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> trong báo cáo tài chính.",
        "words": [
            { "id": "w1", "text": "lỗi thủ công" },
            { "id": "w2", "text": "chính xác" },
            { "id": "w3", "text": "sáng tạo" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "AI giảm lỗi nhập liệu thủ công (human errors) để tăng độ chính xác."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Hỗ trợ đa phương tiện nâng cao của Custom GPTs mang lại lợi ích gì?",
        "options": [
            { "id": "a", "text": "Đọc file PDF, phân tích Excel và xử lý hình ảnh cùng lúc" },
            { "id": "b", "text": "Chỉ phát nhạc nền khi người dùng đọc báo cáo tài chính" },
            { "id": "c", "text": "Cho phép thay đổi phông chữ của toàn bộ hệ điều hành" },
            { "id": "d", "text": "Tự động thiết kế văn phòng ảo 3D cho các kiểm toán viên" }
        ],
        "correctAnswer": "a",
        "explanation": "Khả năng Multimodal của GPT-4 cho phép xử lý đồng thời văn bản, hình ảnh, file PDF và bảng tính Excel."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Trình tự thao tác với GPT Trợ lý Kế toán để trích xuất hóa đơn:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Tải file ảnh hoặc PDF hóa đơn lên khung chat của GPT" },
            { "id": "2", "text": "Viết prompt: 'Hãy trích xuất tên công ty, mã số thuế, tổng tiền'" },
            { "id": "3", "text": "GPT xử lý hình ảnh và hiển thị kết quả bằng bảng" },
            { "id": "4", "text": "Người dùng sao chép bảng kết quả vào phần mềm kế toán" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Upload file -> Ra lệnh prompt -> Chờ AI xử lý -> Sao chép dữ liệu hoàn thiện."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các công cụ bảo mật, quản trị dữ liệu với ứng dụng của chúng trong AI:",
        "left": [
            { "id": "l1", "text": "Mã hóa dữ liệu (Encryption)" },
            { "id": "l2", "text": "Tuân thủ GDPR / CCPA" },
            { "id": "l3", "text": "Quản lý truy cập (Access Control)" }
        ],
        "right": [
            { "id": "r1", "text": "Bảo vệ an toàn cho dữ liệu trong lúc truyền tải và lưu trữ" },
            { "id": "r2", "text": "Đảm bảo quyền riêng tư và quyền lợi dữ liệu hợp pháp" },
            { "id": "r3", "text": "Chỉ cấp quyền cho nhân sự được phân quyền trong hệ thống" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Mã hóa bảo vệ dữ liệu vật lý; GDPR quy định luật quyền riêng tư; Access control bảo vệ người dùng."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong giáo dục nội bộ, một Custom GPT (Tutor GPT) có thể giúp gì cho nhân sự mới?",
        "options": [
            { "id": "a", "text": "Giải thích chi tiết các chuẩn mực kế toán một cách dễ hiểu" },
            { "id": "b", "text": "Chấm công và trừ lương tự động nếu nhân viên đến muộn" },
            { "id": "c", "text": "Thay thế nhân sự quản lý cấp cao ra quyết định đuổi việc" },
            { "id": "d", "text": "Mua hộ thức ăn nhanh và cà phê trong giờ nghỉ giải lao" }
        ],
        "correctAnswer": "a",
        "explanation": "Tutor GPT hoạt động như gia sư ảo, hỗ trợ nhân sự mới tra cứu và hiểu các nghiệp vụ kế toán phức tạp."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về sự chuyển dịch trong ngành kế toán:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Lĩnh vực kế toán đang chứng kiến một cuộc cách mạng mang tính <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> nhờ AI. Các nhiệm vụ <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> và lặp đi lặp lại đang dần được tự động hóa.",
        "words": [
            { "id": "w1", "text": "biến đổi" },
            { "id": "w2", "text": "thủ công" },
            { "id": "w3", "text": "vui nhộn" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Kế toán chuyển đổi từ các quy trình thủ công sang tự động hóa thông minh."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp cấp độ tương tác từ đơn giản đến phức tạp khi sử dụng ChatGPT:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Hỏi đáp kiến thức chung bằng phiên bản ChatGPT mặc định" },
            { "id": "2", "text": "Viết prompt có cấu trúc và đính kèm file dữ liệu PDF" },
            { "id": "3", "text": "Sử dụng Custom GPT được huấn luyện sẵn dữ liệu nội bộ" },
            { "id": "4", "text": "Cấu hình Custom GPT tích hợp API gọi lệnh ra bên ngoài" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Trò chuyện bình thường -> Dùng prompt dài/file -> Dùng Custom GPT -> Custom GPT + API."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Điều nào sau đây là hệ quả của việc AI giúp 'tự động hóa sổ sách'?",
        "options": [
            { "id": "a", "text": "Kế toán viên có nhiều thời gian hơn để tư vấn chiến lược" },
            { "id": "b", "text": "Người làm kế toán sẽ không còn bất kỳ công việc nào" },
            { "id": "c", "text": "Thuế thu nhập doanh nghiệp sẽ tự động giảm đi 50%" },
            { "id": "d", "text": "Mọi giấy tờ bằng giấy sẽ biến mất trong vòng một tuần" }
        ],
        "correctAnswer": "a",
        "explanation": "Giảm bớt gánh nặng sổ sách giúp kế toán viên chuyển hướng sang các nhiệm vụ phân tích tài chính giá trị cao."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công cụ lưu trữ/phân tích với đặc trưng hỗ trợ AI:",
        "left": [
            { "id": "l1", "text": "Cloud Storage (AWS/Azure)" },
            { "id": "l2", "text": "Data Visualization (Tableau)" },
            { "id": "l3", "text": "Predictive Analytics" }
        ],
        "right": [
            { "id": "r1", "text": "Mang lại khả năng mở rộng an toàn chứa dữ liệu lớn" },
            { "id": "r2", "text": "Biến dữ liệu phức tạp thành biểu đồ dễ hiểu, có thể hành động" },
            { "id": "r3", "text": "Phân tích mẫu dữ liệu để dự báo rủi ro tương lai" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Cloud lưu trữ lớn; Tableau vẽ biểu đồ; Predictive Analytics dự báo tương lai."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về sự tùy biến của Custom GPTs:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Sự khác biệt lớn nhất của Custom GPTs so với plugin cũ là khả năng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> chuyên sâu, cho phép kết hợp các <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> nội bộ của từng tổ chức.",
        "words": [
            { "id": "w1", "text": "tùy biến" },
            { "id": "w2", "text": "quy trình" },
            { "id": "w3", "text": "linh kiện" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Custom GPTs mạnh ở tùy biến (customization) và nạp được quy trình (workflows) nội bộ."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Trình tự thích ứng với AI của một cá nhân kế toán:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Nhận thức về sự xuất hiện và xu hướng của công nghệ AI" },
            { "id": "2", "text": "Bắt đầu học các khái niệm cơ bản (Data Literacy)" },
            { "id": "3", "text": "Thử nghiệm sử dụng ChatGPT vào công việc thường ngày" },
            { "id": "4", "text": "Ứng dụng AI phân tích tài chính sâu và ra quyết định" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Nhận thức -> Học căn bản -> Thử nghiệm công cụ -> Trở thành chuyên gia ứng dụng."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Đâu là quan điểm đúng đắn nhất về việc AI sẽ 'lấy đi việc làm' của kế toán viên?",
        "options": [
            { "id": "a", "text": "AI thay thế nhiệm vụ thủ công, không thay thế hoàn toàn nghề kế toán" },
            { "id": "b", "text": "Chắc chắn 100% tất cả kế toán viên sẽ thất nghiệp trong năm tới" },
            { "id": "c", "text": "AI không thể làm bất cứ việc gì liên quan đến toán học và số liệu" },
            { "id": "d", "text": "AI chỉ làm mất việc của nhân sự làm marketing và quảng cáo" }
        ],
        "correctAnswer": "a",
        "explanation": "AI thay thế công việc nhập liệu lặp đi lặp lại, nâng cao vai trò của kế toán viên lên mức cố vấn chiến lược, chứ không diệt vong nghề này."
    }
]

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day12\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace day specific titles
content = content.replace("Bài Tập Trắc Nghiệm Buổi 11", "Bài Tập Trắc Nghiệm Buổi 12")
content = content.replace("kiến thức của Buổi 11", "kiến thức của Buổi 12")
content = content.replace("tài liệu Buổi 11", "tài liệu Buổi 12")

json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 12 quiz updated with 30 new questions.")
