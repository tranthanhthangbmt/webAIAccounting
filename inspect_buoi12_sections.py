# inspect_buoi12_sections.py
with open('docs/buoi_12.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, l in enumerate(lines):
    s = l.strip()
    if any(keyword in s for keyword in ['Đổi mới AI', 'Lợi ích', 'Yêu cầu', 'Quan trọng để', 'Triển khai AI', 'Tóm tắt', 'Đọc thêm', 'Hỏi đáp', 'Những đổi mới của GPT', 'Những thách thức', 'Nghiên cứu điển hình', 'Xu hướng và dự đoán', 'Chuẩn bị cho một']):
        print(f"Line {i+1}: {s}")
