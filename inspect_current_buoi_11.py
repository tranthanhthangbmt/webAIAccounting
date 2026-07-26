with open('docs/buoi_11.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines[:100]):
    print(f"{i+1}: {line}")
