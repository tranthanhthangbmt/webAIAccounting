import re
with open(r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs\buoi_04.md', 'r', encoding='utf-8') as f:
    text = f.read()
blocks = re.findall(r'<div style="text-align: center.*?</div', text, flags=re.DOTALL)
for i, b in enumerate(blocks[:4]):
    print(i, b)
