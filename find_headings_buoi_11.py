import re

with open('docs/buoi_11.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    s = line.strip()
    # Let's find lines that look like headings or LOs
    if (s.startswith('#') or 'LO 2.' in s or s.startswith('2-') or 'Tóm tắt' in s or 'Bài tập' in s or 'Câu hỏi' in s or 'Kỹ năng' in s) and len(s) < 80:
        print(f"Line {i+1}: {s}")
