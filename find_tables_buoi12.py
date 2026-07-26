# find_tables_buoi12.py
with open('docs/buoi_12.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'Bảng' in l or 'bảng' in l or 'Table' in l:
        print(f"Line {i+1}: {l.strip()}")
