import re
with open(r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs\buoi_05.md', 'r', encoding='utf-8') as f:
    text = f.read()
print(re.findall(r'<img src="(.*?)"', text))
