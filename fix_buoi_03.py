import re

with open(r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs\buoi_03.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove injected Figure 1.2 images
text = re.sub(r'\n<div style="text-align: center; margin: 20px auto;">\n\s*<img src="\.\./Figures/Buoi_01/Figure 1\.2[^>]+>\n\s*<div[^>]+>.*?</div>\n</div>\n', '', text)
text = re.sub(r'\n<div style="text-align: center; margin: 20px auto;">\n\s*<img src="\.\./Figures/Buoi_01/Figure%201\.2[^>]+>\n\s*<div[^>]+>.*?</div>\n</div>\n', '', text)
text = re.sub(r'<img src="\.\./Figures/Buoi_01/Figure 1\.2[^>]+>\n(?:<div[^>]+>.*?</div>\n)?', '', text)
text = re.sub(r'<img src="\.\./Figures/Buoi_01/Figure%201\.2[^>]+>\n(?:<div[^>]+>.*?</div>\n)?', '', text)

# 2. Inject Figure 15.1
html_15_1 = '\n<div style="text-align: center; margin: 20px auto;">\n    <img src="../Figures/Buoi_03B/image1.jpeg" alt="Figure 15.1 AI Ethics and Regulation in Finance" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">\n    <div style="color: #666; font-style: italic; font-size: 0.9em;">Figure 15.1 AI Ethics and Regulation in Finance</div>\n</div>\n'
text = re.sub(r'> 📸 \*\*Hình ảnh\*\*: Figure 15\.1.*', html_15_1, text)

with open(r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs\buoi_03.md', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed buoi_03.md')
