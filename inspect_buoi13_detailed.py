# inspect_buoi13_detailed.py
with open('docs/buoi_13.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
print("Total lines:", len(lines))

# Find lines that are short, uppercase, or look like major headings
for i, l in enumerate(lines):
    s = l.strip()
    if len(s) > 0 and len(s) < 60:
        if s in ['6', '13', '3', '4'] or 'Chương' in s or 'Kỹ thuật' in s or 'SPARKS' in s or 'Phân tích' in s and len(s) < 40 or 'Prompt' in s:
            print(f"Line {i+1}: {s}")
