import re
import json

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Khái niệm STP trong tiếp thị là viết tắt của các từ nào?",
        "options": [
            { "id": "a", "text": "Segmentation, Targeting, Positioning" },
            { "id": "b", "text": "Sales, Technology, Pricing strategies" },
            { "id": "c", "text": "Systems, Tracking, Performance measures" },
            { "id": "d", "text": "Standardization, Trading, Profitability" }
        ],
        "correctAnswer": "a",
        "explanation": "STP là viết tắt của Phân khúc (Segmentation), Nhắm mục tiêu (Targeting), Định vị (Positioning)."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong học không giám sát (unsupervised learning), tại sao chúng ta sử dụng thuật toán phân cụm?",
        "options": [
            { "id": "a", "text": "Để tính toán lợi nhuận và doanh thu" },
            { "id": "b", "text": "Để huấn luyện mô hình dự báo phá sản" },
            { "id": "c", "text": "Do dữ liệu không có nhãn kết quả (unlabeled)" },
            { "id": "d", "text": "Do cần một phương pháp hồi quy tuyến tính" }
        ],
        "correctAnswer": "c",
        "explanation": "Phân cụm được sử dụng trong học không giám sát vì dữ liệu không có nhãn (unlabeled data)."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các khái niệm phân khúc với định nghĩa tương ứng:",
        "left": [
            { "id": "l1", "text": "Phân khúc động (Dynamic Segmentation)" },
            { "id": "l2", "text": "Vi phân khúc (Microsegments)" },
            { "id": "l3", "text": "Tiếp thị đại chúng (Mass marketing)" }
        ],
        "right": [
            { "id": "r1", "text": "Liên tục cập nhật phân khúc vì sở thích khách hàng luôn thay đổi" },
            { "id": "r2", "text": "Phân khúc siêu nhỏ hướng tới cá nhân hóa (hyperpersonalization)" },
            { "id": "r3", "text": "Giả định tất cả khách hàng đều giống nhau và gửi chung một thông điệp" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Dynamic = cập nhật liên tục. Micro = cá nhân hóa siêu nhỏ. Mass = đại trà."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp các bước cơ bản của thuật toán k-Means:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Xác định số lượng cụm (k)" },
            { "id": "2", "text": "Khởi tạo ngẫu nhiên các trung tâm cụm (centroids)" },
            { "id": "3", "text": "Gán mỗi điểm dữ liệu cho trung tâm cụm gần nhất" },
            { "id": "4", "text": "Tính toán lại trung tâm và lặp lại cho đến khi hội tụ" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quy trình k-Means: Chọn k -> Khởi tạo -> Gán điểm -> Cập nhật trung tâm (lặp lại)."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ thích hợp so sánh giữa k-Means và k-Medoid:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Thay vì sử dụng giá trị trung bình như k-Means, k-Medoid sử dụng một <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> làm trung tâm. Điều này giúp thuật toán chống <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> tốt hơn k-Means.",
        "words": [
            { "id": "w1", "text": "điểm dữ liệu thực tế (medoid)" },
            { "id": "w2", "text": "nhiễu ngoại lai (outliers)" },
            { "id": "w3", "text": "giá trị giả định" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "k-Medoid lấy một điểm thực tế làm tâm, giúp nó bền vững hơn trước các giá trị ngoại lai (outliers)."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Lệnh `scale(df, center = TRUE, scale = TRUE)` trong R nhằm mục đích gì?",
        "options": [
            { "id": "a", "text": "Chuyển dữ liệu thành dạng số nguyên (integer)" },
            { "id": "b", "text": "Lọc các giá trị trống (NA) ra khỏi dữ liệu" },
            { "id": "c", "text": "Vẽ biểu đồ các trung tâm cụm ngẫu nhiên" },
            { "id": "d", "text": "Chuyển đổi các biến về cùng thang đo (điểm Z)" }
        ],
        "correctAnswer": "d",
        "explanation": "Căn giữa và chia tỷ lệ giúp chuyển giá trị về điểm Z, khắc phục sự khác biệt thang đo giữa các biến."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Đa cộng tuyến (Multicollinearity) xảy ra khi nào trong mô hình dự báo?",
        "options": [
            { "id": "a", "text": "Khi tất cả các biến đều độc lập với nhau" },
            { "id": "b", "text": "Khi có nhiều biến độc lập tương quan mạnh" },
            { "id": "c", "text": "Khi dữ liệu bị thiếu hụt" },
            { "id": "d", "text": "Khi không thể xác định được biến phụ thuộc" }
        ],
        "correctAnswer": "b",
        "explanation": "Đa cộng tuyến (Multicollinearity) xảy ra khi có sự tương quan mạnh giữa nhiều biến độc lập."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép nối các tham số trong R với chức năng của chúng:",
        "left": [
            { "id": "l1", "text": "centers trong kmeans()" },
            { "id": "l2", "text": "nstart trong kmeans()" },
            { "id": "l3", "text": "repel = TRUE trong fviz_cluster()" }
        ],
        "right": [
            { "id": "r1", "text": "Chỉ định số lượng cụm cần phân chia" },
            { "id": "r2", "text": "Đặt số lượng điểm khởi tạo ngẫu nhiên ban đầu" },
            { "id": "r3", "text": "Ngăn các nhãn của điểm dữ liệu đè lên nhau trên biểu đồ" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "centers = k (số cụm); nstart = số lần lặp random ban đầu; repel=TRUE = tránh text overlap."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ vào chỗ trống về mô hình hồi quy:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Để khắc phục Đa cộng tuyến và tự động loại bỏ biến không cần thiết, người ta dùng Hồi quy <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, tiêu biểu là mô hình <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "có phạt (Penalized)" },
            { "id": "w2", "text": "LASSO" },
            { "id": "w3", "text": "tuyến tính (Linear)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Hồi quy có phạt (Penalized regression), đặc biệt là LASSO, giúp lựa chọn đặc trưng và giải quyết đa cộng tuyến."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp các bước đánh giá sức khỏe tài chính bằng LASSO:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập dữ liệu các chỉ số tài chính (ratios) của các công ty (cả phá sản và không phá sản)" },
            { "id": "2", "text": "Kiểm tra sự tương quan (Biểu đồ tương quan) và VIF" },
            { "id": "3", "text": "Chạy mô hình LASSO để tự động loại bỏ các biến có đa cộng tuyến (thu gọn hệ số về 0)" },
            { "id": "4", "text": "Đánh giá khả năng dự đoán của mô hình bằng đường cong AUC ROC" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quy trình: Chuẩn bị dữ liệu -> Kiểm tra tương quan -> Huấn luyện LASSO (lọc biến) -> Đánh giá (AUC ROC)."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Đường cong AUC ROC biểu diễn mối quan hệ giữa hai yếu tố nào?",
        "options": [
            { "id": "a", "text": "Dương tính giả (X) và Dương tính thật (Y)" },
            { "id": "b", "text": "Khoảng cách Euclide (X) và Tâm cụm (Y)" },
            { "id": "c", "text": "Chi phí (X) và Doanh thu (Y)" },
            { "id": "d", "text": "Thời gian mua sắm (X) và Số tiền chi tiêu (Y)" }
        ],
        "correctAnswer": "a",
        "explanation": "AUC ROC biểu diễn False Positives (trục x) và True Positives (trục y)."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Thuật ngữ 'Vốn cổ phần tư nhân' (Private equity) trong tài liệu thường đầu tư vào dạng doanh nghiệp nào?",
        "options": [
            { "id": "a", "text": "Chỉ đầu tư vào tập đoàn công nghệ" },
            { "id": "b", "text": "Doanh nghiệp có tiềm năng lớn nhưng đang khó khăn tài chính" },
            { "id": "c", "text": "Chỉ đầu tư vào ngân hàng trung ương" },
            { "id": "d", "text": "Doanh nghiệp hoàn toàn không có khoản nợ nào" }
        ],
        "correctAnswer": "b",
        "explanation": "Công ty cổ phần tư nhân đầu tư vào doanh nghiệp có tiềm năng chưa hiện thực hóa nhưng đang gặp khó khăn (nợ cao)."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các công thức chỉ số tài chính (Financial Ratios) với tên của chúng:",
        "left": [
            { "id": "l1", "text": "Current Ratio (Tỷ lệ thanh toán hiện hành)" },
            { "id": "l2", "text": "Debt-Equity Ratio (Tỷ lệ nợ trên vốn CSH)" },
            { "id": "l3", "text": "Operating Ratio (Tỷ lệ hoạt động)" }
        ],
        "right": [
            { "id": "r1", "text": "Tài sản lưu động / Nợ ngắn hạn" },
            { "id": "r2", "text": "Giá trị sổ sách của vốn chủ sở hữu / Tổng nợ phải trả" },
            { "id": "r3", "text": "Tổng chi phí / Tổng doanh thu" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Dựa vào công thức trong mục 10.5.1 và bộ dữ liệu."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ liên quan đến cách hoạt động của glmnet (mô hình LASSO):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Mô hình LASSO đã thu hẹp các tham số beta của một số biến về <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, do đó giúp <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> từ 16 biến ban đầu xuống số lượng ít hơn.",
        "words": [
            { "id": "w1", "text": "0 (không)" },
            { "id": "w2", "text": "lựa chọn đặc trưng (feature selection)" },
            { "id": "w3", "text": "gia tăng (increase)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "LASSO giải quyết đa cộng tuyến bằng cách đẩy hệ số của các biến kém quan trọng về 0, giúp chọn lọc đặc trưng."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Thứ tự xử lý dữ liệu trước khi phân cụm (Cluster Analysis):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Đọc dữ liệu thô (vd: số tiền, thời gian mua sắm)" },
            { "id": "2", "text": "Trừ giá trị trung bình (center = TRUE)" },
            { "id": "3", "text": "Chia cho độ lệch chuẩn (scale = TRUE)" },
            { "id": "4", "text": "Sử dụng dữ liệu điểm Z (Z-scores) để chạy k-Means" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quy trình: Đọc dữ liệu -> Căn giữa (trừ mean) -> Chia tỷ lệ (chia std dev) -> Chạy phân cụm."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Điều kiện cần thiết của dữ liệu khi truyền vào hàm glmnet() để chạy LASSO trong R là gì?",
        "options": [
            { "id": "a", "text": "Dữ liệu phải có định dạng văn bản (text)" },
            { "id": "b", "text": "Dữ liệu phải ở dạng ma trận (matrix)" },
            { "id": "c", "text": "Dữ liệu phải là danh sách liên kết" },
            { "id": "d", "text": "Dữ liệu không được chứa số thập phân" }
        ],
        "correctAnswer": "b",
        "explanation": "Tài liệu ghi rõ: Vì đối với glmnet, dữ liệu phải ở dạng ma trận, chúng ta chuyển đổi nó thành một ma trận..."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các bộ phận/tổ chức với vai trò sử dụng Dự báo sức khỏe tài chính:",
        "left": [
            { "id": "l1", "text": "Người cho vay (Ngân hàng)" },
            { "id": "l2", "text": "Ban quản lý (Doanh nghiệp)" },
            { "id": "l3", "text": "Nhà đầu tư (Cổ phần tư nhân)" }
        ],
        "right": [
            { "id": "r1", "text": "Quyết định có nên cấp tín dụng hay không" },
            { "id": "r2", "text": "Lập kế hoạch chiến lược và phân bổ nguồn lực nội bộ" },
            { "id": "r3", "text": "Mua lại các doanh nghiệp nợ cao nhưng có tiềm năng" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Ngân hàng -> cấp tín dụng. Ban quản lý -> chiến lược. Nhà đầu tư -> mua lại công ty."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Hệ quả của Đa cộng tuyến đối với một mô hình dự báo là gì?",
        "options": [
            { "id": "a", "text": "Mô hình sẽ không thể tính toán được" },
            { "id": "b", "text": "Nó làm tăng tốc độ xử lý dữ liệu" },
            { "id": "c", "text": "Dẫn đến các ước tính không đáng tin cậy cho từng hệ số dự báo" },
            { "id": "d", "text": "Làm cho biểu đồ ROC AUC luôn đạt 1.0" }
        ],
        "correctAnswer": "c",
        "explanation": "Đa cộng tuyến không làm hỏng toàn bộ mô hình nhưng làm hệ số của từng biến trở nên không chính xác, thiếu tin cậy."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ liên quan đến sự tương đồng trong phân cụm:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Nếu hai khách hàng ở gần nhau trong <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, họ sẽ có nhiều điểm tương đồng và do đó nên được nhóm vào cùng một <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "không gian đặc trưng (feature space)" },
            { "id": "w2", "text": "cụm (cluster)" },
            { "id": "w3", "text": "vũ trụ song song" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Khoảng cách trong feature space càng nhỏ, sự tương đồng càng cao, do đó được xếp chung vào 1 cluster."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Nhãn kết quả (label) dự đoán trong mô hình sức khỏe tài chính của Ngân hàng Altra là gì?",
        "options": [
            { "id": "a", "text": "Doanh nghiệp có thuộc cụm 1 hay cụm 2 không" },
            { "id": "b", "text": "Doanh nghiệp có lợi nhuận cao nhất thị trường" },
            { "id": "c", "text": "Khách hàng có ở lại lâu không" },
            { "id": "d", "text": "Doanh nghiệp có phá sản hay không" }
        ],
        "correctAnswer": "d",
        "explanation": "Nhãn để đánh giá là liệu một doanh nghiệp có bị phá sản hay không (sẽ phá sản = 0, không phá sản = 1)."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Thứ tự các khái niệm từ mức độ tổng quát đến cá nhân hóa trong Marketing:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Tiếp thị đại chúng (Mass marketing - coi mọi người như 1)" },
            { "id": "2", "text": "Phân khúc thị trường (Segmentation - chia nhóm lớn)" },
            { "id": "3", "text": "Vi phân khúc (Microsegments - nhóm rất nhỏ)" },
            { "id": "4", "text": "Siêu cá nhân hóa (Hyperpersonalization - duy nhất từng người)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Đại chúng -> Phân khúc -> Vi phân khúc -> Cá nhân hóa."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép chức năng của các hàm trong R khi vẽ và đo lường mô hình:",
        "left": [
            { "id": "l1", "text": "fviz_cluster()" },
            { "id": "l2", "text": "predict(..., type='response')" },
            { "id": "l3", "text": "performance(pred, 'auc')" }
        ],
        "right": [
            { "id": "r1", "text": "Trực quan hóa kết quả phân cụm (k-Means)" },
            { "id": "r2", "text": "Đưa ra dự đoán phá sản cho dữ liệu mới" },
            { "id": "r3", "text": "Tính toán diện tích dưới đường cong ROC để đánh giá mô hình" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "fviz_cluster vẽ cụm. predict lấy xác suất/phản hồi. performance tính AUC."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong đánh giá mô hình bằng ROC, giá trị AUC (Area Under Curve) như thế nào thì được coi là tốt?",
        "options": [
            { "id": "a", "text": "Bằng 0" },
            { "id": "b", "text": "Càng thấp càng tốt" },
            { "id": "c", "text": "Chính xác là 0.5" },
            { "id": "d", "text": "Các giá trị cao hơn cho thấy dự đoán tốt hơn" }
        ],
        "correctAnswer": "d",
        "explanation": "Các giá trị AUC cao hơn cho thấy khả năng phân loại, dự đoán của mô hình tốt hơn."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ liên quan đến VIF (Variance Inflation Factor):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Chúng ta có thể kiểm tra <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (multicollinearity) bằng cách sử dụng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> cho từng biến dự báo.",
        "words": [
            { "id": "w1", "text": "đa cộng tuyến" },
            { "id": "w2", "text": "VIF" },
            { "id": "w3", "text": "cây quyết định" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "VIF được dùng để đánh giá mức độ đa cộng tuyến của các biến dự báo."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp quá trình phân khúc khách hàng theo cơ sở dữ liệu (Data-Driven Segmentation):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Giới thiệu sản phẩm qua các mẫu nhỏ" },
            { "id": "2", "text": "Theo dõi hành vi mua hàng thực tế của khách hàng (dữ liệu bán hàng)" },
            { "id": "3", "text": "Phân tích cụm (Clustering) trên dữ liệu thu thập được" },
            { "id": "4", "text": "Tinh chỉnh lại sản phẩm và chiến lược nhắm mục tiêu (Vòng phản hồi)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Dựa trên data-driven: tung mẫu -> theo dõi hành vi -> phân tích -> vòng lặp tinh chỉnh."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Ví dụ về Vi phân khúc (Microsegmenting) mà Amazon áp dụng là gì?",
        "options": [
            { "id": "a", "text": "Gửi coupon giảm giá rau củ cho mọi người ở Phoenix" },
            { "id": "b", "text": "Không đưa ra bất kỳ gợi ý nào" },
            { "id": "c", "text": "Đề xuất sản phẩm rất cụ thể dựa trên hành vi mua hàng trong quá khứ của cá nhân" },
            { "id": "d", "text": "Chỉ đề xuất sản phẩm dựa vào độ tuổi" }
        ],
        "correctAnswer": "c",
        "explanation": "Amazon tạo microsegments để đề xuất các sản phẩm rất cụ thể cho từng khách hàng."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép ý nghĩa của các thông số/câu lệnh khi thực hành R (Phân khúc bằng k-Means):",
        "left": [
            { "id": "l1", "text": "set.seed(12345)" },
            { "id": "l2", "text": "center = TRUE" },
            { "id": "l3", "text": "scale = TRUE" }
        ],
        "right": [
            { "id": "r1", "text": "Thiết lập giá trị gieo mầm để có thể tái tạo (reproduce) lại kết quả y hệt" },
            { "id": "r2", "text": "Trừ giá trị trung bình của biến khỏi các giá trị" },
            { "id": "r3", "text": "Chia dữ liệu cho độ lệch chuẩn để đồng bộ thang đo" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "seed = cố định random; center = trừ mean; scale = chia std dev."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ vào chỗ trống liên quan đến báo cáo tài chính:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Bộ phận tài chính cung cấp cái nhìn hồi tố thông qua bảng cân đối kế toán, báo cáo <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, và báo cáo lưu chuyển tiền tệ. Họ cũng cung cấp cái nhìn hướng tới tương lai qua các dự báo và lập kế hoạch <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "kết quả hoạt động kinh doanh" },
            { "id": "w2", "text": "kịch bản (scenario planning)" },
            { "id": "w3", "text": "viễn cảnh" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Báo cáo kết quả hoạt động kinh doanh là 1 trong 3 báo cáo chính. Lập kế hoạch kịch bản là phương pháp dự báo tương lai."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp theo thứ tự ưu tiên của việc phân khúc thị trường truyền thống đến tự động hóa AI:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Nhắm mục tiêu theo nhân khẩu học chung (Demographics cơ bản)" },
            { "id": "2", "text": "Sử dụng yếu tố tâm lý học và lối sống (Psychographics)" },
            { "id": "3", "text": "Áp dụng học máy (k-Means) để phân cụm dựa trên dữ liệu mua sắm" },
            { "id": "4", "text": "Siêu cá nhân hóa tự động bằng AI (Hyperpersonalization)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Sự phát triển của segmentation từ tĩnh (nhân khẩu, tâm lý) đến tự động bằng Machine Learning và AI siêu cá nhân hóa."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Nhược điểm của k-Means dẫn đến việc ra đời k-Medoid là gì?",
        "options": [
            { "id": "a", "text": "Dễ bị ảnh hưởng mạnh bởi nhiễu (outliers) do dùng giá trị trung bình" },
            { "id": "b", "text": "Không thể chạy trên dữ liệu lớn" },
            { "id": "c", "text": "Chỉ hỗ trợ phân khúc theo độ tuổi" },
            { "id": "d", "text": "Bắt buộc dữ liệu phải có nhãn kết quả (labeled)" }
        ],
        "correctAnswer": "a",
        "explanation": "k-Means dùng trung bình nên dễ bị nhiễu kéo lệch. k-Medoid dùng điểm thực tế làm tâm nên chống nhiễu tốt hơn."
    }
]

import os

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day04\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the title and headers
content = content.replace("Bài Tập Trắc Nghiệm Buổi 1", "Bài Tập Trắc Nghiệm Buổi 4")
content = content.replace("kiến thức của Buổi 1", "kiến thức của Buổi 4")
content = content.replace("tài liệu Buổi 1", "tài liệu Buổi 4")

# Replace the questions array
json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 04 quiz updated with 30 new questions.")
