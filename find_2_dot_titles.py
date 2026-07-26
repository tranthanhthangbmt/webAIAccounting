with open('docs/buoi_11.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    s = line.strip()
    if ('2.1' in s or '2.2' in s or '2.3' in s or '2.4' in s or '2.5' in s or 'MỤC TIÊU BÀI HỌC' in s) and not 'MINH HỌA' in s and not 'LO 2.' in s:
        print(f"Line {i+1}: {s}")
