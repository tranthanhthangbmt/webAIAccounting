import re
import os

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'
for md_filename in os.listdir(docs_dir):
    if not md_filename.endswith('.md'): continue
    md_path = os.path.join(docs_dir, md_filename)
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    images = re.findall(r'<img src="(.*?)"', text)
    if not images: continue
    
    # Check for duplicates by normalizing `%20` to space
    normalized_images = [img.replace('%20', ' ') for img in images]
    duplicates = set([x for x in normalized_images if normalized_images.count(x) > 1])
    if duplicates:
        print(f'{md_filename} has duplicates: {duplicates}')
