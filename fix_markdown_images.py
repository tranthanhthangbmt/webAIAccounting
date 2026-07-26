import os
import re

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'

def replacer(match):
    caption = match.group(1)
    path = match.group(2)
    # Return HTML tag for the image, prepending ../ so docsify root is reached correctly
    return f'<img src="../{path}" alt="{caption}">'

for md_filename in os.listdir(docs_dir):
    if not md_filename.endswith('.md'): continue
    md_path = os.path.join(docs_dir, md_filename)
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Match ![caption](Figures/...(.PNG|.png|.jpg|.jpeg))
    # This greedy matching until the file extension avoids breaking on parentheses inside the filename.
    new_content = re.sub(r'!\[(.*?)\]\((Figures/.*?(?:\.PNG|\.png|\.jpg|\.jpeg))\)', replacer, content)
    
    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Replaced markdown images with HTML in {md_filename}')
