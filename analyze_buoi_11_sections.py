import re

with open('docs/buoi_11.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    s = line.strip()
    if re.match(r'^(LO\s*2\.\d+|L O\s*2\.\d+|❶|❷|❸|❹|❺|CHƯƠNG\s*2|Tóm tắt|Câu hỏi trắc nghiệm|Câu hỏi ôn tập|Bài tập ngắn gọn|Bài tập|MINH HỌA\s*2\.\d+)', s, re.IGNORECASE) and len(s) < 100:
        print(f"Line {i+1}: {s}")
