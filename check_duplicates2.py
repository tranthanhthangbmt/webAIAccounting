import re
import urllib.parse
with open(r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs\buoi_04.md', 'r', encoding='utf-8') as f:
    text = f.read()

# I need to see the exact text around "Figure 5.4"
idx = text.find('Figure 5.4')
print(text[idx-300:idx+300])
