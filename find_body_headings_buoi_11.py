with open('docs/buoi_11.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    s = line.strip()
    if ('LO 2.1' in s or 'LO 2.2' in s or 'LO 2.3' in s or 'LO 2.4' in s or 'LO 2.5' in s or 'TÓM TẮT' in s or 'Tóm tắt' in s or 'Câu hỏi trắc nghiệm' in s or 'Câu hỏi ôn tập' in s or 'Bài tập ngắn gọn' in s or s == 'Bài tập') and len(s) < 120:
        print(f"Line {i+1}: {s}")
