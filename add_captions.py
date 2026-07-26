import os
import re

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'

def replacer(match):
    src = match.group(1)
    alt = match.group(2)
    return f'''<div style="text-align: center; margin: 20px auto;">
    <img src="{src}" alt="{alt}" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">
    <div style="color: #666; font-style: italic; font-size: 0.9em;">{alt}</div>
</div>'''

for md_filename in os.listdir(docs_dir):
    if not md_filename.endswith('.md'): continue
    md_path = os.path.join(docs_dir, md_filename)
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Match the exact img tags we generated earlier
    new_content = re.sub(r'<img src="(.*?)" alt="(.*?)" style=".*?">', replacer, content)
    
    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Added captions to images in {md_filename}')
