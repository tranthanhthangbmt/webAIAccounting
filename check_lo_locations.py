with open('docs/buoi_11.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx in [122, 658, 937, 1400, 1768, 2500, 3650, 4241]:
    print(f"=== AROUND LINE {idx} ===")
    for i in range(max(0, idx-5), min(len(lines), idx+6)):
        print(f"{i+1}: {lines[i].strip()}")
