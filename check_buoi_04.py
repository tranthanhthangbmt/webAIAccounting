import re
import os

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'
with open(os.path.join(docs_dir, 'buoi_04.md'), 'r', encoding='utf-8') as f:
    text = f.read()

images = re.findall(r'<img src="(.*?)"', text)
for i, img in enumerate(images):
    print(i, img)
