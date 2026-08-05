import re
import json
import os

questions = [
    # 1. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Trong cơ sở dữ liệu quan hệ, bảng (table) bao gồm các thành phần nào?",
        "options": [
            { "id": "a", "text": "Hàng (bản ghi) và Cột (thuộc tính)" },
            { "id": "b", "text": "Các video quảng cáo trên mạng" },
            { "id": "c", "text": "Chỉ có các thư mục hình ảnh số" },
            { "id": "d", "text": "Tin nhắn của tất cả khách hàng" }
        ],
        "correctAnswer": "a",
        "explanation": "Bảng trong cơ sở dữ liệu quan hệ bao gồm các hàng (đại diện cho bản ghi) và cột (phản ánh các thuộc tính)."
    },
    # 2. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Đặc điểm quan trọng nhất của Khóa chính (Primary Key) trong một bảng dữ liệu là gì?",
        "options": [
            { "id": "a", "text": "Phải có một giá trị duy nhất cho mỗi hàng" },
            { "id": "b", "text": "Cho phép nhiều hàng có cùng một mã số" },
            { "id": "c", "text": "Luôn luôn chứa các giá trị null hoặc rỗng" },
            { "id": "d", "text": "Chỉ được phép sử dụng chữ cái in hoa" }
        ],
        "correctAnswer": "a",
        "explanation": "Khóa chính là cột phải có một giá trị duy nhất để định danh cho mỗi hàng trong bảng."
    },
    # 3. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép các loại phép nối (Join) SQL với mô tả kết quả của chúng:",
        "left": [
            { "id": "l1", "text": "Inner Join" },
            { "id": "l2", "text": "Left Join" },
            { "id": "l3", "text": "Full Join" }
        ],
        "right": [
            { "id": "r1", "text": "Chỉ lấy các hàng có giá trị khớp ở cả 2 bảng" },
            { "id": "r2", "text": "Lấy tất cả các hàng từ bảng bên trái" },
            { "id": "r3", "text": "Trả về tất cả bản ghi từ cả 2 bảng" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Inner Join chỉ lấy điểm giao. Left Join lấy toàn bộ bên trái. Full Join lấy tất cả."
    },
    # 4. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Sắp xếp trình tự logic để kết nối 2 bảng dữ liệu và thực hiện tính toán:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Xác định các trường (cột) dữ liệu cần lấy từ 2 bảng" },
            { "id": "2", "text": "Xác định cột chung (khóa chính và khóa ngoại)" },
            { "id": "3", "text": "Sử dụng SQL Join để nối 2 bảng thông qua cột chung" },
            { "id": "4", "text": "Thực hiện tính toán trên bảng kết quả vừa được nối" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Xác định nhu cầu -> Tìm cột chung -> Join -> Tính toán."
    },
    # 5. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về khái niệm Khóa ngoại:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Khóa ngoại (Foreign Key) là một cột chứa dữ liệu giống như khóa <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> của một bảng khác. Nó được sử dụng để tạo <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> giữa các bảng.",
        "words": [
            { "id": "w1", "text": "chính" },
            { "id": "w2", "text": "mối quan hệ" },
            { "id": "w3", "text": "kẻ hở bảo mật" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Khóa ngoại liên kết với khóa chính của bảng khác để tạo mối quan hệ (relationship)."
    },
    # 6. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Trong phép nối (Join), khi nào xuất hiện giá trị null trong bảng kết quả?",
        "options": [
            { "id": "a", "text": "Khi không có hàng phù hợp ở bảng được ghép" },
            { "id": "b", "text": "Mỗi khi thực hiện bất kỳ lệnh Inner Join nào" },
            { "id": "c", "text": "Khi hai khóa chính hoàn toàn trùng khớp nhau" },
            { "id": "d", "text": "Do người dùng nhập sai mật khẩu vào phần mềm" }
        ],
        "correctAnswer": "a",
        "explanation": "Giá trị null (hoặc thiếu) xuất hiện (trong Left/Right/Full Join) khi một bảng không có bản ghi khớp với bảng kia."
    },
    # 7. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Microsoft Excel PivotTable thường được sử dụng để làm gì?",
        "options": [
            { "id": "a", "text": "Tóm tắt lượng lớn dữ liệu thành một báo cáo ngắn gọn" },
            { "id": "b", "text": "Thay thế hoàn toàn ngôn ngữ lập trình Python" },
            { "id": "c", "text": "Thiết kế đồ họa hoạt hình 3D cho trò chơi trực tuyến" },
            { "id": "d", "text": "Đọc định dạng video 4K để tính toán băng thông" }
        ],
        "correctAnswer": "a",
        "explanation": "PivotTable là công cụ mạnh mẽ trong Excel dùng để tổng hợp, xoay (pivot), lọc và tính toán dữ liệu lớn."
    },
    # 8. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép các phép đo thống kê (Statistical measures) với phân loại của chúng:",
        "left": [
            { "id": "l1", "text": "Mean (Trung bình), Median (Trung vị)" },
            { "id": "l2", "text": "Variance (Phương sai), Range (Khoảng)" },
            { "id": "l3", "text": "Skewness (Độ lệch), Kurtosis (Độ nhọn)" }
        ],
        "right": [
            { "id": "r1", "text": "Thước đo vị trí (Measures of location)" },
            { "id": "r2", "text": "Thước đo độ phân tán (Measures of dispersion)" },
            { "id": "r3", "text": "Thước đo hình dạng (Measures of shape)" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Vị trí cho biết trung tâm dữ liệu; Phân tán cho biết độ trải rộng; Hình dạng cho biết hình thái phân phối."
    },
    # 9. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về giá trị P-value trong thống kê:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "P-value được sử dụng để kiểm định giả thuyết. Nếu P-value nhỏ hơn mức ý nghĩa (thường là <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>), ta có thể bác bỏ giả thuyết <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "0.05" },
            { "id": "w2", "text": "không (null hypothesis)" },
            { "id": "w3", "text": "95%" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Mức ý nghĩa chuẩn thường là 0.05 (5%). P-value < 0.05 nghĩa là bác bỏ giả thuyết không."
    },
    # 10. Ordering - Hard
    {
        "type": "ordering",
        "difficulty": "Khó",
        "question": "Sắp xếp quá trình phân tích số liệu thống kê mô tả từ tập dữ liệu thô:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Làm sạch và lọc các bản ghi không hợp lệ hoặc rỗng" },
            { "id": "2", "text": "Tính toán các thước đo trung tâm (Mean, Median)" },
            { "id": "3", "text": "Đánh giá mức độ phân tán (Độ lệch chuẩn, Khoảng)" },
            { "id": "4", "text": "Phân tích hệ số tương quan giữa các biến số" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Làm sạch -> Hiểu xu hướng trung tâm -> Phân tích sự biến động -> Phân tích tương quan."
    },
    # 11. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Hệ số tương quan (Correlation coefficient) nằm trong khoảng giá trị nào?",
        "options": [
            { "id": "a", "text": "Từ -1 đến +1" },
            { "id": "b", "text": "Luôn lớn hơn 100" },
            { "id": "c", "text": "Từ 0 đến vô cực" },
            { "id": "d", "text": "Chỉ bằng 0 hoặc 1" }
        ],
        "correctAnswer": "a",
        "explanation": "Hệ số tương quan r luôn nằm trong khoảng [-1, 1]."
    },
    # 12. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "SQL (Structured Query Language) là ngôn ngữ được dùng để làm gì?",
        "options": [
            { "id": "a", "text": "Truy vấn và thao tác trên cơ sở dữ liệu" },
            { "id": "b", "text": "Tạo ra các trò chơi điện tử thực tế ảo" },
            { "id": "c", "text": "Định dạng kiểu chữ và màu sắc website" },
            { "id": "d", "text": "Kiểm soát phần cứng của bo mạch chủ" }
        ],
        "correctAnswer": "a",
        "explanation": "SQL là ngôn ngữ chuẩn để quản lý và truy vấn dữ liệu trong các hệ quản trị CSDL quan hệ."
    },
    # 13. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các loại biểu đồ với mục đích sử dụng tốt nhất của chúng:",
        "left": [
            { "id": "l1", "text": "Bar chart (Biểu đồ cột)" },
            { "id": "l2", "text": "Scatter plot (Biểu đồ phân tán)" },
            { "id": "l3", "text": "Line chart (Biểu đồ đường)" }
        ],
        "right": [
            { "id": "r1", "text": "So sánh các giá trị giữa các danh mục khác nhau" },
            { "id": "r2", "text": "Hiển thị mối quan hệ (tương quan) giữa hai biến số" },
            { "id": "r3", "text": "Theo dõi xu hướng của dữ liệu thay đổi theo thời gian" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Cột: so sánh; Phân tán: tương quan; Đường: xu hướng thời gian."
    },
    # 14. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về tính chất của phân phối chuẩn:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Trong phân phối chuẩn (Normal distribution), đường cong có hình <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và đối xứng, trong đó giá trị Mean, Median và Mode đều <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "quả chuông" },
            { "id": "w2", "text": "bằng nhau" },
            { "id": "w3", "text": "lệch dương" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Phân phối chuẩn có hình quả chuông (bell-shaped) và Mean = Median = Mode."
    },
    # 15. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Trình tự thao tác tạo Pivot Table trong Excel:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Đảm bảo dữ liệu nguồn có tiêu đề cột đầy đủ" },
            { "id": "2", "text": "Bôi đen vùng dữ liệu hoặc chọn một ô trong bảng" },
            { "id": "3", "text": "Vào thẻ Insert -> Chọn PivotTable" },
            { "id": "4", "text": "Kéo thả các trường vào vùng Rows, Columns, Values" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Kiểm tra data -> Chọn vùng -> Insert PivotTable -> Thiết lập Layout (kéo thả)."
    },
    # 16. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Nếu dữ liệu có giá trị ngoại lai (outliers) quá lớn, thước đo nào sau đây phản ánh xu hướng trung tâm tốt nhất?",
        "options": [
            { "id": "a", "text": "Trung vị (Median) vì nó ít bị nhiễu" },
            { "id": "b", "text": "Trung bình (Mean) vì nó bao gồm tất cả" },
            { "id": "c", "text": "Độ lệch chuẩn vì nó luôn lớn hơn không" },
            { "id": "d", "text": "Khoảng (Range) vì nó tính cả lớn và nhỏ" }
        ],
        "correctAnswer": "a",
        "explanation": "Trung vị (Median) không bị ảnh hưởng mạnh bởi các giá trị quá lớn hoặc quá nhỏ (outliers) như Mean."
    },
    # 17. Matching - Easy
    {
        "type": "matching",
        "difficulty": "Dễ",
        "question": "Ghép chức năng của các vùng trong Pivot Table (Excel):",
        "left": [
            { "id": "l1", "text": "Rows" },
            { "id": "l2", "text": "Values" },
            { "id": "l3", "text": "Filters" }
        ],
        "right": [
            { "id": "r1", "text": "Nhóm dữ liệu theo các hàng ngang" },
            { "id": "r2", "text": "Thực hiện phép tính (Sum, Count, Average)" },
            { "id": "r3", "text": "Lọc toàn bộ bảng theo một điều kiện cụ thể" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Rows: Hiển thị dòng; Values: Tính toán; Filters: Bộ lọc báo cáo."
    },
    # 18. MCQ - Hard
    {
        "type": "multiple_choice",
        "difficulty": "Khó",
        "question": "Độ lệch chuẩn (Standard Deviation) đo lường điều gì trong tập dữ liệu?",
        "options": [
            { "id": "a", "text": "Mức độ phân tán của các điểm dữ liệu quanh giá trị Mean" },
            { "id": "b", "text": "Sự khác biệt giữa tổng chi phí và tổng doanh thu thực tế" },
            { "id": "c", "text": "Giá trị thường xuyên xuất hiện nhất trong bảng dữ liệu" },
            { "id": "d", "text": "Chênh lệch lớn nhất và nhỏ nhất của tập hợp các biến số" }
        ],
        "correctAnswer": "a",
        "explanation": "Độ lệch chuẩn đo lường sự phân tán trung bình của dữ liệu so với giá trị trung bình (Mean)."
    },
    # 19. Fill-in-the-blank - Easy
    {
        "type": "fill_in_blanks",
        "difficulty": "Dễ",
        "question": "Điền từ về Right Join:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Right Join sẽ trả về tất cả bản ghi từ bảng bên <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và các bản ghi trùng khớp từ bảng bên <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "phải" },
            { "id": "w2", "text": "trái" },
            { "id": "w3", "text": "trên" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Right Join ưu tiên lấy toàn bộ dữ liệu của bảng bên phải."
    },
    # 20. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Trong thống kê, biểu đồ Hộp (Box plot) đặc biệt hữu ích khi muốn quan sát điều gì?",
        "options": [
            { "id": "a", "text": "Sự phân tán dữ liệu và các giá trị ngoại lai (outliers)" },
            { "id": "b", "text": "Số lượng bản ghi chính xác theo từng mốc thời gian" },
            { "id": "c", "text": "Tổng doanh thu bán hàng của doanh nghiệp theo năm" },
            { "id": "d", "text": "Tên và địa chỉ chi tiết của từng khách hàng cá nhân" }
        ],
        "correctAnswer": "a",
        "explanation": "Box plot hiển thị tứ phân vị, dải phân tán và dễ dàng phát hiện các giá trị ngoại lai."
    },
    # 21. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Sắp xếp độ phức tạp của các loại Join (từ ít dữ liệu nhất đến nhiều dữ liệu nhất trong trường hợp thông thường):",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Inner Join (Chỉ lấy điểm giao 2 bảng)" },
            { "id": "2", "text": "Left Join / Right Join (Lấy điểm giao + 1 bảng đầy đủ)" },
            { "id": "3", "text": "Full Join (Lấy tất cả của cả 2 bảng)" }
        ],
        "correctOrder": ["1", "2", "3"],
        "explanation": "Inner Join thường có số dòng nhỏ nhất. Full Join chứa toàn bộ dữ liệu."
    },
    # 22. Matching - Hard
    {
        "type": "matching",
        "difficulty": "Khó",
        "question": "Ghép thuật ngữ SQL với hành động tương ứng:",
        "left": [
            { "id": "l1", "text": "SELECT" },
            { "id": "l2", "text": "FROM" },
            { "id": "l3", "text": "WHERE" }
        ],
        "right": [
            { "id": "r1", "text": "Chỉ định các cột cần lấy dữ liệu" },
            { "id": "r2", "text": "Chỉ định bảng nguồn chứa dữ liệu" },
            { "id": "r3", "text": "Áp dụng điều kiện lọc cho các hàng" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Cấu trúc cơ bản: SELECT (cột) FROM (bảng) WHERE (điều kiện)."
    },
    # 23. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Khi hai biến số có Hệ số tương quan r = -0.9, điều đó mang ý nghĩa gì?",
        "options": [
            { "id": "a", "text": "Tương quan nghịch rất mạnh, biến này tăng thì biến kia giảm" },
            { "id": "b", "text": "Hai biến số này hoàn toàn không có bất kỳ liên hệ gì" },
            { "id": "c", "text": "Tương quan thuận rất mạnh, hai biến cùng tăng cùng lúc" },
            { "id": "d", "text": "Lỗi dữ liệu vì hệ số không bao giờ có số âm được" }
        ],
        "correctAnswer": "a",
        "explanation": "r = -0.9 là tương quan âm (nghịch) và rất mạnh (gần -1)."
    },
    # 24. Fill-in-the-blank - Medium
    {
        "type": "fill_in_blanks",
        "difficulty": "Trung bình",
        "question": "Điền từ về Khóa chính:",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Mỗi bảng chỉ có thể có <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> khóa chính và các giá trị của nó không bao giờ được phép <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "một" },
            { "id": "w2", "text": "null (rỗng)" },
            { "id": "w3", "text": "trùng lặp hoàn toàn" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Mỗi bảng có 1 khóa chính, và giá trị không được phép null hoặc trùng lặp (duy nhất)."
    },
    # 25. Ordering - Medium
    {
        "type": "ordering",
        "difficulty": "Trung bình",
        "question": "Các bước cơ bản để tính lợi nhuận ròng từ bảng dữ liệu đơn hàng thô:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Gộp dữ liệu đơn hàng và chi phí theo mã sản phẩm" },
            { "id": "2", "text": "Tính tổng doanh thu và tổng chi phí của từng món" },
            { "id": "3", "text": "Lấy tổng doanh thu trừ đi tổng chi phí để ra lợi nhuận" },
            { "id": "4", "text": "Sắp xếp theo lợi nhuận giảm dần để tìm sản phẩm tốt nhất" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Gộp dữ liệu -> Tính doanh thu/chi phí -> Trừ ra lợi nhuận -> Sắp xếp phân tích."
    },
    # 26. MCQ - Easy
    {
        "type": "multiple_choice",
        "difficulty": "Dễ",
        "question": "Tính năng VLOOKUP trong Excel thường dùng để làm gì?",
        "options": [
            { "id": "a", "text": "Tìm kiếm một giá trị ở cột đầu tiên và trả về dữ liệu tương ứng" },
            { "id": "b", "text": "Thiết kế các hiệu ứng ảnh động cho biểu đồ hình tròn" },
            { "id": "c", "text": "Xóa toàn bộ các dòng trống trong bảng dữ liệu lớn" },
            { "id": "d", "text": "Gửi email báo cáo hàng ngày một cách tự động hóa" }
        ],
        "correctAnswer": "a",
        "explanation": "VLOOKUP (Vertical Lookup) dùng để tra cứu giá trị theo chiều dọc trong một bảng."
    },
    # 27. Matching - Medium
    {
        "type": "matching",
        "difficulty": "Trung bình",
        "question": "Ghép các phép đo với khái niệm tương ứng:",
        "left": [
            { "id": "l1", "text": "Mean" },
            { "id": "l2", "text": "Median" },
            { "id": "l3", "text": "Mode" }
        ],
        "right": [
            { "id": "r1", "text": "Giá trị trung bình cộng của toàn bộ các quan sát" },
            { "id": "r2", "text": "Giá trị đứng ở vị trí chính giữa khi sắp xếp dãy số" },
            { "id": "r3", "text": "Giá trị xuất hiện với tần suất nhiều nhất trong tập" }
        ],
        "correctPairs": { "l1": "r1", "l2": "r2", "l3": "r3" },
        "explanation": "Mean: trung bình cộng; Median: trung vị; Mode: yếu vị (xuất hiện nhiều nhất)."
    },
    # 28. Fill-in-the-blank - Hard
    {
        "type": "fill_in_blanks",
        "difficulty": "Khó",
        "question": "Điền từ về độ nhọn của đường phân phối (Kurtosis):",
        "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
        "text": "Kurtosis đo lường độ <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> của phân phối. Phân phối chuẩn có độ nhọn bằng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
        "words": [
            { "id": "w1", "text": "nhọn hoặc phẳng" },
            { "id": "w2", "text": "không (0)" },
            { "id": "w3", "text": "trăm phần trăm" }
        ],
        "correctAnswers": { "1": "w1", "2": "w2" },
        "explanation": "Kurtosis biểu thị mức độ nhọn/bẹt của đỉnh. Phân phối chuẩn chuẩn hóa (excess kurtosis) bằng 0."
    },
    # 29. Ordering - Easy
    {
        "type": "ordering",
        "difficulty": "Dễ",
        "question": "Trình tự quy trình làm việc với dữ liệu cơ bản:",
        "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
        "items": [
            { "id": "1", "text": "Thu thập và trích xuất dữ liệu từ Database (SQL)" },
            { "id": "2", "text": "Làm sạch và xử lý dữ liệu thô bằng các công cụ" },
            { "id": "3", "text": "Tính toán thống kê và phân tích mô tả bằng Excel" },
            { "id": "4", "text": "Trực quan hóa thành biểu đồ để viết báo cáo cuối" }
        ],
        "correctOrder": ["1", "2", "3", "4"],
        "explanation": "Thu thập -> Làm sạch -> Phân tích -> Trực quan hóa."
    },
    # 30. MCQ - Medium
    {
        "type": "multiple_choice",
        "difficulty": "Trung bình",
        "question": "Khi làm việc với các tập dữ liệu cực kỳ lớn (Big Data), nhược điểm của Microsoft Excel là gì?",
        "options": [
            { "id": "a", "text": "Giới hạn số dòng và hiệu suất chậm khi xử lý file lớn" },
            { "id": "b", "text": "Không có khả năng vẽ bất kỳ loại biểu đồ nào cả" },
            { "id": "c", "text": "Không thể tính được giá trị trung bình cộng (Mean)" },
            { "id": "d", "text": "Luôn luôn xóa dữ liệu cũ mỗi khi tắt máy tính đi" }
        ],
        "correctAnswer": "a",
        "explanation": "Excel có giới hạn khoảng 1 triệu dòng và trở nên rất chậm chạp, hay treo khi file quá nặng, không phù hợp cho Big Data khổng lồ."
    }
]

index_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\quizzes\Day11\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace day specific titles
content = content.replace("Bài Tập Trắc Nghiệm Buổi 9", "Bài Tập Trắc Nghiệm Buổi 11")
content = content.replace("kiến thức của Buổi 9", "kiến thức của Buổi 11")
content = content.replace("tài liệu Buổi 9", "tài liệu Buổi 11")

json_str = json.dumps(questions, indent=4, ensure_ascii=False)
js_array_str = f"const questions = {json_str};"
pattern = re.compile(r"const questions = \[.*?\];", re.DOTALL)
new_content = pattern.sub(js_array_str, content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Day 11 quiz updated with 30 new questions.")
