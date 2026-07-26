# inspect_buoi12.py
with open('docs/buoi_12.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- Potential headings in Chapter 1 (Lines 15-530) ---")
for i, l in enumerate(lines[:530]):
    s = l.strip()
    if len(s) > 0 and len(s) < 60 and not s.endswith('.') and not s.endswith(',') and not s.startswith('-') and not s.startswith('“') and not s.startswith('–'):
        print(f"Line {i+1}: {s}")

print("\n--- Potential headings in Chapter 12 (Lines 531-923) ---")
for i, l in enumerate(lines[530:]):
    s = l.strip()
    if len(s) > 0 and len(s) < 60 and not s.endswith('.') and not s.endswith(',') and not s.startswith('-') and not s.startswith('“') and not s.startswith('–'):
        print(f"Line {530+i+1}: {s}")
