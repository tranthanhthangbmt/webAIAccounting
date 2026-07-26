import os

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'
md_path = os.path.join(docs_dir, 'buoi_02.md')
with open(md_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if '<img src="../Figures/Buoi_' in line: continue
    if '<div style="text-align: center; margin: 20px auto;">' in line: continue
    if '<div style="color: #666; font-style: italic; font-size: 0.9em;">' in line: continue
    if line.strip() == '</div>' or line.strip() == '</div': continue
    new_lines.append(line)

with open(md_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Cleaned up buoi_02.md')
