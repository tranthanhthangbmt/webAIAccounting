with open('docs/buoi_11.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    s = line.strip()
    if s.startswith('<div') or s.startswith('<img') or s.startswith('</div') or s.startswith('<!--'):
        print(f"Line {i+1}: {s}")
