import re
import json
import os

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Sự khác biệt chính giữa Khám phá dữ liệu (EDA) và Phân tích kiểm định (Confirmatory Analysis) là gì?",
        "options": [
            { "id": "a", "text": "EDA mang tính tự do, linh hoạt tìm kiếm cấu trúc tiềm ẩn" },
            { "id": "b", "text": "Phân tích kiểm định không bao giờ dùng công thức toán" },
            { "id": "c", "text": "EDA bắt buộc phải có một giả thuyết kiên cố từ trước" },
            { "id": "d", "text": "Phân tích kiểm định chỉ được dùng trong marketing" }
        ],
        "correctAnswer": "a",
        "explanation": "EDA trả lời 'Dữ liệu đang cho thấy điều gì' (tự do thăm dò), trong khi Phân tích kiểm định trả lời 'Giả thuyết có đúng không'."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong quy trình 4 bước Khám phá dữ liệu, bước đầu tiên Kế toán viên cần làm là gì?",
        "options": [
            { "id": "a", "text": "Xác định câu hỏi định hướng dựa trên mục tiêu" },
            { "id": "b", "text": "Tự động gửi báo cáo ngay cho Hội đồng Quản trị" },
            { "id": "c", "text": "Xóa toàn bộ dữ liệu lịch sử để lấy chỗ trống" },
            { "id": "d", "text": "Nhờ AI vẽ tất cả các biểu đồ có thể có" }
        ],
        "correctAnswer": "a",
        "explanation": "Bước 1 là 'Identify Questions' - Xác định câu hỏi định hướng (Ví dụ: Chi nhánh nào chi phí cao nhất?)."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các vùng cấu trúc của PivotTable với chức năng của chúng:",
        "left": [
            { "id": "l1", "text": "Rows & Columns" },
            { "id": "l2", "text": "Values" },
            { "id": "l3", "text": "Filters" }
        ],
        "right": [
            { "id": "r1", "text": "Vùng đặt trường danh mục để tạo phân nhóm" },
            { "id": "r2", "text": "Vùng thực hiện tính toán (SUM, AVERAGE, COUNT)" },
            { "id": "r3", "text": "Vùng lọc toàn bộ bảng theo một điều kiện cụ thể" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Rows/Columns dùng để phân nhóm; Values dùng để tính toán; Filters dùng để lọc."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp 4 bước Khám phá Dữ liệu Kế toán theo thứ tự chuẩn xác:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Bước 1: Xác định Câu hỏi (Identify Questions)" },
            { "id": "2", "text": "Bước 2: Nhận diện Mối quan hệ Dữ liệu" },
            { "id": "3", "text": "Bước 3: Khám phá Mối quan hệ Dữ liệu (Dùng PivotTable)" },
            { "id": "4", "text": "Bước 4: Tạo ra Hiểu biết Sâu sắc (Generate Insights)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Hỏi -> Nhận diện biến số -> Dùng PivotTable để khám phá -> Tổng hợp thành Insight."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về tầm quan trọng của EDA đối với kiểm toán viên:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Khám phá dữ liệu (EDA) giúp phát hiện sớm sai sót hoặc giao dịch <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Từ đó, kiểm toán viên có thể định hướng chọn mẫu vào những khu vực có <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> cao thay vì kiểm tra dàn trải.",
        "words": [
            { "id": "w1", "text": "bất thường" },
            { "id": "w2", "text": "rủi ro" },
            { "id": "w3", "text": "khuyến mãi" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "EDA phát hiện các giao dịch bất thường (outliers/gian lận) giúp tập trung vào các khu vực rủi ro cao (High-risk areas)."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Kỹ thuật 'Calculated Fields' trong PivotTable được dùng để làm gì?",
        "options": [
            { "id": "a", "text": "Tạo cột tính toán mới theo công thức tự định nghĩa" },
            { "id": "b", "text": "Chỉ dùng để đổi màu sắc của các ô trong bảng" },
            { "id": "c", "text": "Xóa các dòng dữ liệu bị lỗi trống (NULL) đi" },
            { "id": "d", "text": "In tự động toàn bộ báo cáo ra giấy A4" }
        ],
        "correctAnswer": "a",
        "explanation": "Calculated Fields cho phép viết công thức (VD: = Profit / Sales) trực tiếp ngay bên trong PivotTable."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Kỹ thuật 'Show Values As' trong PivotTable giúp kế toán viên làm gì?",
        "options": [
            { "id": "a", "text": "Chuyển số tuyệt đối thành tỷ lệ phần trăm (%)" },
            { "id": "b", "text": "Mã hóa toàn bộ số liệu để bảo vệ quyền riêng tư" },
            { "id": "c", "text": "Tắt hiển thị màn hình Excel để tiết kiệm điện" },
            { "id": "d", "text": "Xóa bỏ các con số thập phân trên bảng tính" }
        ],
        "correctAnswer": "a",
        "explanation": "Show Values As (như % of Grand Total) dùng để chuyển số tuyệt đối thành tỷ trọng (Vertical Analysis)."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép 3 mô hình Khám phá Dữ liệu với biểu đồ được khuyên dùng:",
        "left": [
            { "id": "l1", "text": "Phân phối (Distribution)" },
            { "id": "l2", "text": "Sai lệch (Deviation)" },
            { "id": "l3", "text": "Phần-trên-Tổng thể (Part-to-Whole)" }
        ],
        "right": [
            { "id": "r1", "text": "Biểu đồ tần suất (Histogram) / Box Plot" },
            { "id": "r2", "text": "Variance Bar Chart / Bullet Chart" },
            { "id": "r3", "text": "Stacked Column Chart / Treemap" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Phân phối dùng Histogram; Sai lệch dùng Variance chart; Phần-tổng thể dùng Stacked Column/Treemap."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về phân tích phương sai (Variance Analysis):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong kế toán quản trị, phương sai <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (Favorable) xảy ra khi doanh thu thực tế lớn hơn ngân sách. Ngược lại, phương sai <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> (Unfavorable) xảy ra khi chi phí thực tế vượt mức kế hoạch.",
        "words": [
            { "id": "w1", "text": "thuận lợi" },
            { "id": "w2", "text": "không thuận lợi" },
            { "id": "w3", "text": "trung bình" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Doanh thu > Ngân sách là Thuận lợi (Favorable); Chi phí > Ngân sách là Không thuận lợi (Unfavorable)."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp quá trình tính Phương sai (Variance) trong Kế toán quản trị:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Xác định số liệu Doanh thu/Chi phí Thực tế (Actual)" },
            { "id": "2", "text": "Xác định số liệu Ngân sách tương ứng (Budget)" },
            { "id": "3", "text": "Lấy Thực tế trừ đi Ngân sách (Actual - Budget)" },
            { "id": "4", "text": "Đánh giá kết quả là Favorable (F) hay Unfavorable (U)" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Thu thập Thực tế -> Thu thập Ngân sách -> Trừ để tìm Phương sai -> Gắn nhãn F hoặc U."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Theo mô hình So sánh danh nghĩa (Nominal Comparison), biểu đồ nào là thích hợp nhất?",
        "options": [
            { "id": "a", "text": "Biểu đồ cột dọc (Column Chart) hoặc thanh ngang" },
            { "id": "b", "text": "Biểu đồ phân tán (Scatter Plot) dày đặc" },
            { "id": "c", "text": "Bản đồ nhiệt độ màu sắc (Heatmap)" },
            { "id": "d", "text": "Biểu đồ hộp (Box Plot) râu trên dưới" }
        ],
        "correctAnswer": "a",
        "explanation": "Nominal Comparison so sánh các danh mục độc lập, do đó biểu đồ cột (Column/Bar Chart) là trực quan nhất."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Trong Data Exploration Patterns, Xếp hạng (Ranking) giúp làm gì?",
        "options": [
            { "id": "a", "text": "Xác định nhóm Top/Bottom theo nguyên lý Pareto 80/20" },
            { "id": "b", "text": "Chỉ để nhìn xem công ty nào có logo đẹp nhất" },
            { "id": "c", "text": "Tính tổng các khoản nợ phải trả cuối kỳ" },
            { "id": "d", "text": "Tìm ngày nghỉ lễ dài nhất trong năm tài chính" }
        ],
        "correctAnswer": "a",
        "explanation": "Xếp hạng giúp tìm ra Top khách hàng hoặc rủi ro (áp dụng quy tắc 80/20)."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các biến cố với nhãn phương sai (Variance) tương ứng:",
        "left": [
            { "id": "l1", "text": "Doanh thu bán xe vượt kế hoạch 8%" },
            { "id": "l2", "text": "Chi phí nguyên vật liệu tăng vượt định mức" },
            { "id": "l3", "text": "Doanh số xe bán tải sụt giảm 10%" }
        ],
        "right": [
            { "id": "r1", "text": "Favorable Variance (F)" },
            { "id": "r2", "text": "Unfavorable Variance (U)" },
            { "id": "r3", "text": "Critical Unfavorable (Cần kiểm toán khẩn cấp)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Doanh thu vượt kế hoạch = F; Chi phí vượt định mức = U; Doanh số sụt giảm nặng = Critical U."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về biểu đồ phân phối để tìm gian lận:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Khi vẽ biểu đồ Box Plot, các giao dịch tài chính nằm xa ngoài vùng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (Whiskers) được coi là giá trị <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> (Outliers), tiềm ẩn rủi ro gian lận khai khống.",
        "words": [
            { "id": "w1", "text": "râu" },
            { "id": "w2", "text": "ngoại lai" },
            { "id": "w3", "text": "cột" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Biểu đồ hộp (Box Plot) có các đường râu (Whiskers). Giá trị nằm ngoài râu gọi là ngoại lai (Outliers)."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Trình tự thực hiện tích hợp Python (AI-Enhanced) trong EDA theo giáo trình:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Import các thư viện pandas, seaborn, matplotlib" },
            { "id": "2", "text": "Tải tập dữ liệu lớn bằng lệnh pd.read_csv()" },
            { "id": "3", "text": "Xử lý làm sạch và kiểm tra thông tin dữ liệu (df.info)" },
            { "id": "4", "text": "Vẽ biểu đồ phân phối hoặc phân tán tự động" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Khai báo thư viện -> Load dữ liệu -> Làm sạch -> Vẽ biểu đồ."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong Data Storytelling, tại sao nên thay thế biểu đồ tròn (Pie Chart) bằng Stacked Bar Chart hoặc Treemap?",
        "options": [
            { "id": "a", "text": "Vì biểu đồ tròn kém chính xác khi có quá nhiều hạng mục" },
            { "id": "b", "text": "Vì biểu đồ tròn luôn làm máy tính bị chậm đáng kể" },
            { "id": "c", "text": "Vì Treemap có màu sắc nổi bật hợp với in trắng đen" },
            { "id": "d", "text": "Vì không có phần mềm kế toán nào hỗ trợ biểu đồ tròn" }
        ],
        "correctAnswer": "a",
        "explanation": "Pie Chart rất khó nhìn nếu có nhiều thành phần (trên 5). Stacked Bar hay Treemap thể hiện cấu trúc tổng thể tốt hơn."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép kỹ thuật PivotTable với tác dụng tương ứng:",
        "left": [
            { "id": "l1", "text": "Date Grouping" },
            { "id": "l2", "text": "Running Total in" },
            { "id": "l3", "text": "Slicers" }
        ],
        "right": [
            { "id": "r1", "text": "Tự động gom nhóm ngày tháng thành Quý, Năm" },
            { "id": "r2", "text": "Cộng dồn số liệu qua từng giai đoạn thời gian" },
            { "id": "r3", "text": "Tạo nút bấm lọc trực quan trên bảng điều khiển" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Date Grouping gom nhóm thời gian; Running Total cộng dồn; Slicers làm nút lọc nhanh."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Khi tập dữ liệu tài chính vượt quá 1 triệu dòng (vượt giới hạn Excel), giải pháp được khuyên dùng là gì?",
        "options": [
            { "id": "a", "text": "Dùng ngôn ngữ Python (Pandas) và AI để phân tích" },
            { "id": "b", "text": "Chia nhỏ file Excel thành hàng ngàn file nhỏ lẻ" },
            { "id": "c", "text": "Xóa bớt 50% dữ liệu đi để phần mềm chạy mượt" },
            { "id": "d", "text": "Dùng máy tính tay Casio để cộng dồn thủ công" }
        ],
        "correctAnswer": "a",
        "explanation": "Excel có giới hạn khoảng 1.04 triệu dòng. Dữ liệu Big Data cần dùng Python (Pandas) hoặc công cụ BI."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ về truyền đạt kết quả (Data Storytelling):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Mục tiêu của Data Storytelling là chuyển hóa phát hiện phức tạp thành một <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> có sức thuyết phục, hỗ trợ <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> đưa ra quyết định hành động.",
        "words": [
            { "id": "w1", "text": "câu chuyện" },
            { "id": "w2", "text": "Ban điều hành" },
            { "id": "w3", "text": "khách hàng" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Data Storytelling là kể 'câu chuyện' dữ liệu cho 'Ban điều hành' (C-Suite) hiểu."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Từ điển Dữ liệu (Data Dictionary) đóng vai trò gì trước khi Khám phá dữ liệu?",
        "options": [
            { "id": "a", "text": "Chuẩn hóa và giải thích ý nghĩa các cột dữ liệu" },
            { "id": "b", "text": "Tự động dịch báo cáo tài chính sang tiếng Anh" },
            { "id": "c", "text": "Mã hóa bảo mật toàn bộ máy tính của công ty" },
            { "id": "d", "text": "Xóa toàn bộ những lỗi chính tả trong văn bản" }
        ],
        "correctAnswer": "a",
        "explanation": "Data Dictionary giúp giải thích ý nghĩa (metadata) và kiểu dữ liệu của các trường (fields)."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Các bước cơ bản để thiết lập một PivotTable:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Chọn bảng dữ liệu thô (Raw Data)" },
            { "id": "2", "text": "Nhấn Insert > PivotTable trên thanh công cụ" },
            { "id": "3", "text": "Kéo trường phân loại (ví dụ Brand) vào Rows" },
            { "id": "4", "text": "Kéo trường số liệu (ví dụ Sales) vào Values" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Bôi đen dữ liệu -> Insert Pivot -> Chọn Row -> Chọn Value tính toán."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép tên trường dữ liệu trong Happy Colors Data Dictionary với kiểu/dữ liệu tương ứng:",
        "left": [
            { "id": "l1", "text": "Units_Sold_Actual" },
            { "id": "l2", "text": "Model" },
            { "id": "l3", "text": "Gross_Sales_Actual" }
        ],
        "right": [
            { "id": "r1", "text": "Số nguyên (Số lượng xe thực tế bán ra)" },
            { "id": "r2", "text": "Văn bản (Dòng sản phẩm xe cụ thể)" },
            { "id": "r3", "text": "Tiền tệ (Tổng doanh thu gộp thực tế)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Units = Số nguyên; Model = Tên xe (Văn bản); Sales = Tiền tệ (Tiền)."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Mô hình Phần-trên-Tổng thể (Part-to-Whole) thường được ứng dụng phân tích báo cáo nào?",
        "options": [
            { "id": "a", "text": "Phân tích cơ cấu tài sản trên Bảng Cân đối kế toán" },
            { "id": "b", "text": "Đếm số lượng nhân viên đi làm trễ trong tháng" },
            { "id": "c", "text": "Tính tổng số giờ làm thêm của đội IT bảo trì" },
            { "id": "d", "text": "Ghi chép lịch sử phiên bản của hệ điều hành" }
        ],
        "correctAnswer": "a",
        "explanation": "Phân tích cơ cấu tài sản (ngắn hạn/dài hạn) chiếm bao nhiêu % tổng tài sản là điển hình của Part-to-Whole."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về Khám phá dữ liệu (EDA):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Việc Khám phá Dữ liệu (EDA) là quá trình kiểm tra, <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và trực quan hóa ban đầu nhằm phát hiện <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> tiềm ẩn của dữ liệu trước khi xây dựng mô hình dự báo.",
        "words": [
            { "id": "w1", "text": "tóm tắt" },
            { "id": "w2", "text": "cấu trúc" },
            { "id": "w3", "text": "sai lầm" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "EDA là quá trình 'tóm tắt' (summarize) dữ liệu để tìm 'cấu trúc' (structure/patterns)."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp quá trình giải quyết 'Unfavorable Variance' (Phương sai không thuận lợi):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Phát hiện chi phí thực tế cao hơn ngân sách" },
            { "id": "2", "text": "Đánh dấu là Unfavorable Variance (U)" },
            { "id": "3", "text": "Drill-down chi tiết giao dịch để tìm nguyên nhân gốc" },
            { "id": "4", "text": "Trình bày báo cáo và đề xuất khắc phục cho Ban quản trị" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Thấy chi phí vượt mức -> Dán nhãn U -> Phân tích sâu nguyên nhân (Drill-down) -> Báo cáo giải pháp."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Một PivotTable chuẩn mực có bao nhiêu vùng cấu trúc cốt lõi?",
        "options": [
            { "id": "a", "text": "4 vùng (Fields, Rows/Columns, Values, Filters)" },
            { "id": "b", "text": "1 vùng duy nhất để nhập toàn bộ mọi thứ" },
            { "id": "c", "text": "10 vùng nằm rải rác trên giao diện Excel" },
            { "id": "d", "text": "Không có vùng nào, dữ liệu bay lơ lửng" }
        ],
        "correctAnswer": "a",
        "explanation": "PivotTable gồm 4 vùng: Fields List, Columns/Rows, Values, Filters."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các loại biểu đồ truyền đạt kết quả với lỗi thiết kế thường gặp:",
        "left": [
            { "id": "l1", "text": "Pie Chart (Biểu đồ tròn)" },
            { "id": "l2", "text": "Bar Chart 3D (Cột 3D)" },
            { "id": "l3", "text": "Line Chart trục Y bị cắt ngắn" }
        ],
        "right": [
            { "id": "r1", "text": "Có quá nhiều lát cắt (hơn 5) gây khó đọc" },
            { "id": "r2", "text": "Hiệu ứng phối cảnh làm lệch cảm nhận tỷ lệ" },
            { "id": "r3", "text": "Phóng đại sự chênh lệch nhỏ (Misleading Axis)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Biểu đồ tròn có lỗi quá nhiều góc cắt; 3D gây biến dạng tỷ lệ; Trục Y cắt ngắn gây phóng đại sai lệch (misleading)."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về kỹ thuật Value Grouping trong PivotTable:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Kỹ thuật Value Grouping gom nhóm số liệu <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> thành các dải (Bins/Ranges), rất hữu ích khi phân tích phân loại hóa đơn hoặc phân tích <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> nợ phải thu (Aging Schedule).",
        "words": [
            { "id": "w1", "text": "liên tục" },
            { "id": "w2", "text": "tuổi" },
            { "id": "w3", "text": "gián đoạn" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Value Grouping gom số liệu liên tục (continuous) thành dải (ví dụ 1-30 ngày, 31-60 ngày) để lập Báo cáo Tuổi nợ (Aging)."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Trình tự kể một câu chuyện dữ liệu tài chính (Data Storytelling):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Bắt đầu với Bối cảnh: Giới thiệu mục tiêu của báo cáo" },
            { "id": "2", "text": "Trình bày Dữ liệu bằng biểu đồ trực quan, đơn giản" },
            { "id": "3", "text": "Phân tích Insight: Giải thích tại sao có con số này" },
            { "id": "4", "text": "Đưa Lời kêu gọi Hành động (Call-to-action) cho Ban GĐ" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Bối cảnh (Context) -> Dữ liệu trực quan (Visuals) -> Giải thích Insight -> Kêu gọi hành động."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Kế toán viên hiện đại (Business Data Analyst) đóng vai trò gì sau khi đã phân tích dữ liệu?",
        "options": [
            { "id": "a", "text": "Truyền đạt Insights để tư vấn chiến lược cho CFO" },
            { "id": "b", "text": "Trở về viết tay từng dòng sổ nhật ký chung" },
            { "id": "c", "text": "Đứng làm lễ tân tiếp đón khách hàng đến giao dịch" },
            { "id": "d", "text": "Xóa toàn bộ các tệp dữ liệu máy tính để bảo mật" }
        ],
        "correctAnswer": "a",
        "explanation": "Phân tích dữ liệu không chỉ dừng ở tính toán, mà đích đến cuối cùng là dùng Insight để tư vấn quản trị."
    }
]

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day14\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace day specific titles
content = content.replace("Bài Tập Trắc Nghiệm Buổi 13", "Bài Tập Trắc Nghiệm Buổi 14")
content = content.replace("kiến thức của Buổi 13", "kiến thức của Buổi 14")
content = content.replace("tài liệu Buổi 13", "tài liệu Buổi 14")

json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 14 quiz updated with 30 new questions.")
