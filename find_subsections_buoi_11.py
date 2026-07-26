import re

with open('docs/buoi_11.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    s = line.strip()
    if s in [
        "Cơ sở dữ liệu quan hệ",
        "Kết nối các bảng chính xác và ngoại hối",
        "Truy vấn SQL và trích xuất dữ liệu",
        "Áp dụng các hàm cơ bản của Excel",
        "Phân tích giao dịch bán hàng với các hàm Excel",
        "Minh họa cách xoay bảng sắp xếp và lọc dữ liệu.",
        "Sử dụng Bảng tổng hợp",
        "Lọc bảng tổng hợp",
        "Xác định mang tính mô tả các biện pháp được sử dụng để thực hiện dữ liệu phân tích.",
        "Biện pháp vị trí",
        "Biện pháp phân tán",
        "Số đo hình dạng",
        "Phân tích tương quan",
        "Sử dụng thống kê mô tả để Kiểm toán chi phí bảo hành",
        "Tóm tắt cách trực quan hóa dữ liệu khám phá và giải thích dữ liệu.",
        "Trực quan hóa dữ liệu",
        "TÓM TẮT",
        "Câu hỏi trắc nghiệm",
        "Câu hỏi ôn tập",
        "Bài tập ngắn gọn",
        "Bài tập"
    ] or re.match(r'^(LO\s*2\.\d+|L O\s*2\.\d+|❶|❷|❸|❹|❺)', s):
        print(f"Line {i+1}: {s}")
