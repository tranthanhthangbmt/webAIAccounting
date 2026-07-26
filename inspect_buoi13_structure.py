# inspect_buoi13_structure.py
with open('docs/buoi_13.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Total lines in docs/buoi_13.md:", len(lines))
print("\n--- Key lines (short lines, numbers, 'Chương', 'Bảng', 'Table', 'SPARKS') ---")
for i, l in enumerate(lines):
    s = l.strip()
    if len(s) > 0 and (len(s) < 55 or 'Chương' in s or 'chương' in s[:15] or 'Bảng' in s or 'bảng' in s[:10] or 'SPARKS' in s or 'sparks' in s or s.isupper() and len(s) < 70):
        if not s.startswith('“') and not s.startswith('–') and not s.startswith('-') and not s.endswith(',') and not s.endswith('.'):
            print(f"Line {i+1}: {s}")
