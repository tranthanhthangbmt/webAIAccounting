import re

with open('docs/buoi_09.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    s = line.strip()
    if re.match(r'^(2|7|8|9|10|11|12)(\.\d+)+', s) or s.startswith('Chương') or s.startswith('CHƯƠNG') or s.startswith('2 ') or s.startswith('7 ') or 'TÓM TẮT' in s.upper() or 'TÀI LIỆU THAM KHẢO' in s.upper() or 'DOI:' in s:
        print(f"Line {i+1}: {s}")
