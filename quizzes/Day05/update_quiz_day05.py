import re
import json

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Thuật ngữ 'Ra quyết định dưới sự không chắc chắn' (Decision-Making Under Uncertainty) có nghĩa là gì?",
        "options": [
            { "id": "a", "text": "Quyết định được đưa ra khi thiếu thông tin hoặc thông tin chỉ có sẵn ở dạng xác suất" },
            { "id": "b", "text": "Quyết định đưa ra khi bạn đã biết chắc chắn 100% về tương lai" },
            { "id": "c", "text": "Quyết định được thực hiện bởi máy tính một cách tự động" },
            { "id": "d", "text": "Việc từ chối đưa ra bất kỳ hành động nào do thiếu thông tin" }
        ],
        "correctAnswer": "a",
        "explanation": "Ra quyết định dưới sự không chắc chắn xảy ra khi bạn thiếu thông tin đầy đủ và chỉ có thể dựa vào xác suất thành công."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Hiệu ứng 'Cái roi da' (Bullwhip effect) trong chuỗi cung ứng mô tả hiện tượng nào?",
        "options": [
            { "id": "a", "text": "Việc giảm giá sản phẩm để chống lại đối thủ cạnh tranh mới" },
            { "id": "b", "text": "Lỗi phần mềm gây chậm trễ cho toàn bộ hệ thống logistic" },
            { "id": "c", "text": "Sự thay đổi nhỏ về nhu cầu bị đánh giá quá cao, dẫn đến dư thừa cung" },
            { "id": "d", "text": "Sự khan hiếm hàng hóa do thiên tai hoặc dịch bệnh" }
        ],
        "correctAnswer": "c",
        "explanation": "Hiệu ứng cái roi da xảy ra khi những tín hiệu nhu cầu nhỏ lẻ bị phóng đại dọc theo chuỗi cung ứng, dẫn đến tích trữ quá mức hoặc dư thừa nguồn cung."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các khái niệm của Cây quyết định (Decision Tree) với định nghĩa của chúng:",
        "left": [
            { "id": "l1", "text": "Nút gốc (Root node)" },
            { "id": "l2", "text": "Độ vẩn đục Gini (Gini impurity)" },
            { "id": "l3", "text": "Nút lá (Leaf node)" }
        ],
        "right": [
            { "id": "r1", "text": "Điểm bắt đầu của cây, biến phân loại tốt nhất được chọn đầu tiên" },
            { "id": "r2", "text": "Chỉ số để đo lường mức độ hỗn tạp của dữ liệu, càng thấp càng tốt" },
            { "id": "r3", "text": "Kết quả dự đoán cuối cùng của nhánh (vd: Có/Không bị chậm giao)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Root node là nút cao nhất. Gini đo mức độ phân loại tốt hay xấu. Leaf node là kết quả cuối cùng."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp các bước cơ bản trong quá trình Phát triển Sản phẩm Mới:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Hình thành và sàng lọc ý tưởng (Idea Generation & Screening)" },
            { "id": "2", "text": "Phát triển khái niệm và phân tích kinh doanh (Concept & Business Analysis)" },
            { "id": "3", "text": "Thiết kế và phát triển nguyên mẫu sản phẩm" },
            { "id": "4", "text": "Thử nghiệm thị trường (Test Marketing) và Thương mại hóa (Commercialization)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Quy trình tiêu chuẩn: Lên ý tưởng -> Phân tích tính khả thi kinh doanh -> Chế tạo sản phẩm -> Thử nghiệm và tung ra thị trường."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ liên quan đến sự mất cân bằng dữ liệu (Imbalance) và cách xử lý:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Khi số lượng sản phẩm giao đúng hạn quá lớn so với sản phẩm bị chậm giao, mô hình có thể bị thiên vị. Kỹ thuật <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (lấy mẫu giảm) giúp cân bằng dữ liệu, qua đó làm tăng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> (khả năng nhận diện sản phẩm bị chậm giao).",
        "words": [
            { "id": "w1", "text": "downsampling" },
            { "id": "w2", "text": "độ nhạy (sensitivity)" },
            { "id": "w3", "text": "tính đồng nhất" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Downsampling giảm lượng mẫu của lớp đa số, giúp mô hình tập trung học cách nhận diện lớp thiểu số (tăng độ nhạy)."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Đặc điểm chính của thuật toán Rừng ngẫu nhiên (Random Forest) là gì?",
        "options": [
            { "id": "a", "text": "Kết hợp nhiều cây quyết định bằng kỹ thuật Bagging (bootstrap aggregation) để giảm phương sai" },
            { "id": "b", "text": "Chỉ sử dụng một cây quyết định duy nhất để dự đoán" },
            { "id": "c", "text": "Là thuật toán dựa trên hồi quy tuyến tính cổ điển" },
            { "id": "d", "text": "Chỉ phù hợp với dữ liệu không có nhãn kết quả" }
        ],
        "correctAnswer": "a",
        "explanation": "Random Forest tạo ra nhiều cây (forest) bằng cách lấy mẫu có hoàn lại (Bagging) và kết hợp chúng để ra kết quả ổn định hơn."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Trong ví dụ ở chương 14, Nintendo Switch thành công nhờ yếu tố nào?",
        "options": [
            { "id": "a", "text": "Chỉ có thể chơi khi kết nối với tivi (console) ở nhà" },
            { "id": "b", "text": "Thiết kế linh hoạt cho phép chơi cả cầm tay và qua bảng điều khiển" },
            { "id": "c", "text": "Mức giá cao hơn đáng kể so với các đối thủ" },
            { "id": "d", "text": "Phát hành miễn phí cho tất cả người dùng" }
        ],
        "correctAnswer": "b",
        "explanation": "Thiết kế của nó cho phép chơi trò chơi cầm tay và bảng điều khiển (console) thu hút được lượng lớn người dùng."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các thông số của Ma trận nhầm lẫn (Confusion Matrix) với cách tính:",
        "left": [
            { "id": "l1", "text": "Độ nhạy (Sensitivity)" },
            { "id": "l2", "text": "Độ đặc hiệu (Specificity)" },
            { "id": "l3", "text": "Dương tính thật (True Positive)" }
        ],
        "right": [
            { "id": "r1", "text": "Tỷ lệ mô hình nhận diện chính xác lớp thiểu số (vd: bị chậm giao)" },
            { "id": "r2", "text": "Tỷ lệ mô hình nhận diện chính xác lớp đa số (vd: không bị chậm giao)" },
            { "id": "r3", "text": "Số lượng các trường hợp thực tế CÓ và mô hình dự đoán CÓ" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Sensitivity (True Positive Rate) = đoán trúng lớp thiểu số. Specificity (True Negative Rate) = đoán trúng lớp đa số."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về các bài kiểm định trong Thử nghiệm A/B (A/B Testing):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Để so sánh giá trị trung bình của ba mức độ khó (Low, Medium, High) trong thiết kế nguyên mẫu game, chúng ta sử dụng kiểm định <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Nếu phương sai không bằng nhau, ta dùng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> để thay thế.",
        "words": [
            { "id": "w1", "text": "F (ANOVA)" },
            { "id": "w2", "text": "Welch's ANOVA" },
            { "id": "w3", "text": "chi bình phương (chi-square)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Kiểm định F (ANOVA) dùng cho >=3 nhóm. Welch's ANOVA dùng khi giả định về phương sai bằng nhau bị vi phạm."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Trình tự tính toán Chỉ số Gini (Gini Impurity) cho nút gốc (Root node) trên một biến dự báo:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Tính tỷ lệ kết quả (Có/Không) cho từng nhóm của biến dự báo (vd: Dự báo cao/Thấp)" },
            { "id": "2", "text": "Tính độ vẩn đục (Impurity) của từng nhóm: 1 - P(Có)^2 - P(Không)^2" },
            { "id": "3", "text": "Tính trung bình có trọng số (weighted average) của các chỉ số Impurity này" },
            { "id": "4", "text": "So sánh kết quả với các biến dự báo khác, biến có Gini thấp nhất sẽ làm nút gốc" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Tỷ lệ từng nhóm -> Impurity từng nhóm -> Trọng số tổng thể -> Chọn biến có Gini bé nhất."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Sự tự chọn (Self-selection) trong thử nghiệm A/B dẫn đến vấn đề gì?",
        "options": [
            { "id": "a", "text": "Nó làm tăng tính ngẫu nhiên của thử nghiệm" },
            { "id": "b", "text": "Nó phá vỡ tính ngẫu nhiên hóa (randomization)" },
            { "id": "c", "text": "Nó giúp hệ thống ghi nhận dữ liệu nhanh hơn" },
            { "id": "d", "text": "Nó loại bỏ nhu cầu phải có biến kết quả" }
        ],
        "correctAnswer": "b",
        "explanation": "Tự chọn xảy ra khi người tham gia được tự chọn nhóm, phá vỡ tính ngẫu nhiên và làm lệch kết quả thử nghiệm."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Chỉ số Gini impurity càng thấp thì có ý nghĩa gì trong cây quyết định?",
        "options": [
            { "id": "a", "text": "Nút đó có khả năng phân loại dữ liệu càng tốt" },
            { "id": "b", "text": "Dữ liệu tại nút đó càng hỗn tạp và lẫn lộn" },
            { "id": "c", "text": "Chỉ số này không phản ánh chất lượng phân loại" },
            { "id": "d", "text": "Mô hình đã bị tính sai và cần phải chạy lại" }
        ],
        "correctAnswer": "a",
        "explanation": "Gini impurity thấp nghĩa là dữ liệu ít bị lẫn lộn, do đó có khả năng phân loại, chia rẽ nhóm càng tốt."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các loại bài kiểm định trong phân tích A/B với mục đích sử dụng:",
        "left": [
            { "id": "l1", "text": "Levene's test" },
            { "id": "l2", "text": "Shapiro-Wilk test" },
            { "id": "l3", "text": "Games-Howell post hoc test" }
        ],
        "right": [
            { "id": "r1", "text": "Kiểm tra tính đồng nhất của phương sai (Equal variance)" },
            { "id": "r2", "text": "Kiểm tra tính phân phối chuẩn (Normality)" },
            { "id": "r3", "text": "Xác định chính xác cặp nhóm nào khác biệt nhau sau khi ANOVA có ý nghĩa" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Levene = Phương sai; Shapiro = Chuẩn hóa; Games-Howell = Bài test hậu hoc khi phương sai khác nhau."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ liên quan đến sự kết hợp (Ensemble) trong Random Forest:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Quá trình lấy mẫu có hoàn lại từ tập dữ liệu gốc để xây dựng nhiều cây quyết định khác nhau được gọi là <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Random Forest sử dụng kỹ thuật này để giảm <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> của mô hình so với việc chỉ dùng 1 cây đơn lẻ.",
        "words": [
            { "id": "w1", "text": "Bagging (bootstrap aggregation)" },
            { "id": "w2", "text": "hiện tượng quá khớp (overfitting) và phương sai" },
            { "id": "w3", "text": "chính xác (accuracy)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Bagging giúp tạo ra rừng các cây đa dạng, giảm phương sai và nguy cơ overfitting so với cây quyết định đơn lẻ."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp các bước thực hiện kiểm định thử nghiệm A/B với >=3 nhóm:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập dữ liệu từ các nguyên mẫu đã được phân bổ ngẫu nhiên" },
            { "id": "2", "text": "Kiểm tra giả định về phân phối chuẩn và phương sai đồng nhất" },
            { "id": "3", "text": "Chạy kiểm định Welch's ANOVA (nếu phương sai không đồng nhất)" },
            { "id": "4", "text": "Chạy kiểm định hậu hoc (Post-hoc test) để xem cặp nguyên mẫu nào thực sự khác biệt" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Data -> Check assumptions -> Chạy ANOVA -> Post-hoc test để xác định rõ sự khác biệt."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Đặc điểm nào KHÔNG ĐÚNG khi nói về kỹ thuật Bagging (bootstrap aggregation)?",
        "options": [
            { "id": "a", "text": "Nó bao gồm việc lấy mẫu mà không có sự hoàn lại (without replacement)" },
            { "id": "b", "text": "Nó kết hợp kết quả từ nhiều mô hình nhỏ lẻ để ra quyết định chung" },
            { "id": "c", "text": "Nó giúp xây dựng các cây quyết định đa dạng" },
            { "id": "d", "text": "Random forest là một ứng dụng phổ biến của Bagging" }
        ],
        "correctAnswer": "a",
        "explanation": "Bagging (Bootstrap aggregation) YÊU CẦU lấy mẫu CÓ hoàn lại (with replacement), do đó câu A là sai."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các quyết định kinh doanh với các sự không chắc chắn (uncertainty) tương ứng (Theo ví dụ Hãng hàng không):",
        "left": [
            { "id": "l1", "text": "Quyết định Hành động (Giảm giá)" },
            { "id": "l2", "text": "Quyết định Không hành động (Giữ nguyên giá)" }
        ],
        "right": [
            { "id": "r1", "text": "Có thể làm xói mòn lợi nhuận và gây ra cuộc chiến giá cả" },
            { "id": "r2", "text": "Có thể bị cổ đông coi là không sẵn lòng thích ứng với thị trường" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2" },
        "explanation": "Hành động giảm giá -> rủi ro chiến tranh giá cả. Không làm gì -> rủi ro mất khách và bị coi là bảo thủ."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Nếu trong một mô hình dự báo, tỷ lệ Accuracy và giá trị AUC đều rất cao, nhưng Sensitivity (Độ nhạy) lại rất thấp, điều này phản ánh vấn đề gì?",
        "options": [
            { "id": "a", "text": "Mô hình đã bị phân bổ ngẫu nhiên sai cách" },
            { "id": "b", "text": "Mô hình hoàn toàn mất khả năng chạy dự báo" },
            { "id": "c", "text": "Mô hình gặp vấn đề do dữ liệu bị mất cân bằng (class imbalance) nghiêm trọng" },
            { "id": "d", "text": "Mô hình dự báo quá tốt đến mức không cần điều chỉnh thêm" }
        ],
        "correctAnswer": "c",
        "explanation": "Khi dữ liệu cực kỳ lệch (imbalance), mô hình có thể chỉ chọn dự báo lớp đa số (đạt Accuracy cao) nhưng hoàn toàn thất bại trong việc nhận diện lớp thiểu số (Sensitivity thấp)."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ về Thử nghiệm Nguyên mẫu Trò chơi:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Để tránh việc người chơi tự chọn nhóm theo sở thích màu sắc hay độ khó, GameV phải áp dụng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để phân bổ người chơi. Nhờ đó, bất kỳ sự khác biệt nào về thời gian chơi cũng có thể tự tin gán cho <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "sự ngẫu nhiên hóa (randomization)" },
            { "id": "w2", "text": "mức độ khó (nguyên mẫu)" },
            { "id": "w3", "text": "thiên vị (bias)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Phân bổ ngẫu nhiên giúp cô lập nguyên nhân, khẳng định sự khác biệt là do mức độ khó chứ không do yếu tố nhiễu ngoài."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong thử nghiệm A/B, Giả thuyết Không (Null Hypothesis) biểu thị điều gì?",
        "options": [
            { "id": "a", "text": "Sự can thiệp (intervention) đã gây ra sự khác biệt" },
            { "id": "b", "text": "Có sự khác biệt đáng kể giữa các nhóm với nhau" },
            { "id": "c", "text": "Không có sự khác biệt đáng kể giữa các nhóm, kết quả chỉ là do ngẫu nhiên" },
            { "id": "d", "text": "Thiết kế của nguyên mẫu A ưu việt hơn hẳn nguyên mẫu B" }
        ],
        "correctAnswer": "c",
        "explanation": "Giả thuyết Không (Null Hypothesis) luôn giả định rằng không có sự khác biệt thực sự, và mọi biến động đều do sai số ngẫu nhiên."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Thứ tự lý tưởng khi xử lý tình trạng mất cân bằng dữ liệu trong Random Forest:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Phân chia dữ liệu thành tập huấn luyện (Train) và tập kiểm tra (Test)" },
            { "id": "2", "text": "Thực hiện giảm mẫu (downsampling) trên tập huấn luyện" },
            { "id": "3", "text": "Huấn luyện mô hình Random Forest trên dữ liệu đã cân bằng" },
            { "id": "4", "text": "Dự đoán trên tập kiểm tra và tính toán Ma trận nhầm lẫn (Confusion Matrix)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Tách data -> Cân bằng tập train -> Huấn luyện -> Dự đoán và Đánh giá."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép số lượng nhóm cần thiết (Groups) với thiết kế thử nghiệm A/B tương ứng:",
        "left": [
            { "id": "l1", "text": "1 yếu tố có 2 cấp độ (levels)" },
            { "id": "l2", "text": "1 yếu tố có 3 cấp độ (levels)" },
            { "id": "l3", "text": "3 yếu tố, mỗi yếu tố có 2 cấp độ (levels)" }
        ],
        "right": [
            { "id": "r1", "text": "Cần 2 nhóm (ví dụ: Nút Đỏ vs Nút Xanh)" },
            { "id": "r2", "text": "Cần 3 nhóm (ví dụ: Độ khó Low, Med, High)" },
            { "id": "r3", "text": "Cần 8 nhóm (2 * 2 * 2 = 8)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Số lượng nhóm phụ thuộc vào tổ hợp của số lượng yếu tố và số cấp độ."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Mục đích chính của một thử nghiệm A/B (A/B testing) là gì?",
        "options": [
            { "id": "a", "text": "Để xác định hiệu quả của một sự can thiệp (intervention) thông qua quan hệ nhân quả" },
            { "id": "b", "text": "Để tăng mức giá bán của tất cả sản phẩm hiện có" },
            { "id": "c", "text": "Để giảm thiểu thời gian vận chuyển của chuỗi cung ứng" },
            { "id": "d", "text": "Để phát hiện mối tương quan giữa các biến mà không cần kiểm soát" }
        ],
        "correctAnswer": "a",
        "explanation": "A/B testing là một thử nghiệm nhân quả (causal testing) nhằm so sánh hiệu quả thực sự của một sự can thiệp so với đối chứng."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về các kết quả dự báo trong bảng nhầm lẫn:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Nếu độ đặc hiệu (specificity) của mô hình thấp, chúng ta sẽ kết thúc bằng việc đặt hàng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> những sản phẩm ít có khả năng bị chậm giao, tức là rơi vào trường hợp <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "quá mức (overordering)" },
            { "id": "w2", "text": "dương tính giả (False Positive)" },
            { "id": "w3", "text": "âm tính thật (True Negative)" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Specificity thấp nghĩa là đoán nhầm hàng Không chậm thành Có chậm (False Positive), dẫn tới tích trữ quá mức."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp theo logic của Quá trình tinh chỉnh Siêu tham số (Hyperparameter Tuning):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thiết lập danh sách các siêu tham số cần thử nghiệm (vd: mtry, min_n)" },
            { "id": "2", "text": "Sử dụng kiểm chứng chéo k-fold (k-fold Cross Validation) để chạy thử" },
            { "id": "3", "text": "Đánh giá mô hình dựa trên số đo AUC ROC cho từng tổ hợp" },
            { "id": "4", "text": "Chọn tổ hợp siêu tham số tốt nhất (vd: select_best) để hoàn thiện mô hình" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Grid search -> k-fold CV -> Đánh giá các Fold -> Chọn Best hyperparameter."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Trong bài kiểm định F, việc biến kết quả (outcome variable) có bản chất là liên tục (continuous) mang ý nghĩa gì?",
        "options": [
            { "id": "a", "text": "Ví dụ như thời gian chơi game, có thể đo lường bằng các giá trị số chi tiết thay vì Có/Không" },
            { "id": "b", "text": "Biến kết quả chỉ có hai giá trị (Có hoặc Không, 1 hoặc 0)" },
            { "id": "c", "text": "Biến kết quả không thể được sử dụng trong Thử nghiệm A/B" },
            { "id": "d", "text": "Biến kết quả chỉ mang giá trị phân loại như 'Màu xanh', 'Màu đỏ'" }
        ],
        "correctAnswer": "a",
        "explanation": "Biến liên tục có thể mang giá trị số mở rộng (ví dụ thời gian: 1.5 giờ, 2.3 giờ...). Việc này phù hợp với các kiểm định như F-test/ANOVA."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các ví dụ phát triển sản phẩm với loại hình đổi mới của chúng:",
        "left": [
            { "id": "l1", "text": "Chase Sapphire Reserve" },
            { "id": "l2", "text": "Nintendo Switch" },
            { "id": "l3", "text": "Ứng dụng theo dõi sức khỏe số" }
        ],
        "right": [
            { "id": "r1", "text": "Sản phẩm dịch vụ tài chính có chương trình điểm thưởng lớn" },
            { "id": "r2", "text": "Phần cứng vật lý tích hợp cách chơi đa dạng (cầm tay/console)" },
            { "id": "r3", "text": "Sản phẩm tồn tại hoàn toàn trên web, không có hiện diện vật lý" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Chase = Tài chính. Nintendo = Phần cứng. Ứng dụng = Sản phẩm ảo/web."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về hậu quả khi một doanh nghiệp phản ứng chậm với thị trường:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Bằng cách không điều chỉnh theo động lực thị trường đang thay đổi, doanh nghiệp có khả năng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> mà người mới tham gia có thể khai thác, dẫn đến việc họ nhận ra quá muộn và không thể <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "mất đi các cơ hội" },
            { "id": "w2", "text": "phục hồi vị thế của mình" },
            { "id": "w3", "text": "phá sản ngay lập tức" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Việc giữ nguyên hiện trạng mang rủi ro bỏ lỡ cơ hội, khiến đối thủ cạnh tranh giá rẻ chiếm mất thị phần."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp theo thứ tự ưu tiên của Cây quyết định từ trên xuống:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Tính Gini Impurity cho tất cả các biến dự báo" },
            { "id": "2", "text": "Chọn biến có Gini Impurity thấp nhất làm Nút gốc (Root Node)" },
            { "id": "3", "text": "Tiếp tục phân chia các nhánh bên dưới để giảm mức độ hỗn tạp" },
            { "id": "4", "text": "Hoàn thành và tạo ra Nút lá (Leaf Node) để dự đoán" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Tính Gini -> Xác định root node -> Tạo nhánh -> Tạo nút lá."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Khẳng định nào đúng khi so sánh kiểm định quan hệ tương quan và thử nghiệm A/B?",
        "options": [
            { "id": "a", "text": "Thử nghiệm A/B cho phép xác định rõ mối quan hệ nguyên nhân - kết quả (nhân quả)" },
            { "id": "b", "text": "Thử nghiệm tương quan luôn mang lại độ chính xác cao hơn thử nghiệm A/B" },
            { "id": "c", "text": "Thử nghiệm A/B không thể dùng để kiểm tra tính năng phần mềm mới" },
            { "id": "d", "text": "Cả hai đều không yêu cầu phân bổ ngẫu nhiên người tham gia" }
        ],
        "correctAnswer": "a",
        "explanation": "Thử nghiệm A/B là thử nghiệm can thiệp ngẫu nhiên (Causal Testing), giúp tìm ra quan hệ nhân quả (ví dụ: do nút màu đỏ mà lượng click tăng)."
    }
]

import os

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day05\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the title and headers
content = content.replace("Bài Tập Trắc Nghiệm Buổi 1", "Bài Tập Trắc Nghiệm Buổi 5")
content = content.replace("kiến thức của Buổi 1", "kiến thức của Buổi 5")
content = content.replace("tài liệu Buổi 1", "tài liệu Buổi 5")

# Replace the questions array
json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 05 quiz updated with 30 new questions.")
