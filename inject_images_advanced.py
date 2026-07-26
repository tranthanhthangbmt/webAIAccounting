import os
import re

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'
fig_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\Figures'

available_images = {}
for subdir in os.listdir(fig_dir):
    if not subdir.startswith('Buoi_'): continue
    subdir_path = os.path.join(fig_dir, subdir)
    if os.path.isdir(subdir_path):
        for img in os.listdir(subdir_path):
            id_match = re.search(r'(Figure|Table|Hình|Bảng|Illustration)\s*(\d+\.\d+)', img, re.IGNORECASE)
            if id_match:
                identifier = id_match.group(2)
                available_images[identifier] = {
                    'filename': img,
                    'path': f"Figures/{subdir}/{img}",
                    'caption': img.rsplit('.', 1)[0]
                }

for md_filename in os.listdir(docs_dir):
    if not md_filename.endswith('.md'): continue
    md_path = os.path.join(docs_dir, md_filename)
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    for identifier, info in available_images.items():
        if info['filename'] in content or info['path'] in content:
            continue
            
        # 1. Try to replace `> 📸 **Hình ảnh**: ...`
        placeholder_pattern = rf'> 📸 \*\*Hình ảnh\*\*:.*?(?:Hình|Bảng|Figure|Table|Minh họa|Illustration)\s*{identifier}.*?(?=\n|$)'
        html = f'\n<div style="text-align: center; margin: 20px auto;">\n    <img src="../{info["path"]}" alt="{info["caption"]}" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">\n    <div style="color: #666; font-style: italic; font-size: 0.9em;">{info["caption"]}</div>\n</div>\n'
        
        match = re.search(placeholder_pattern, content, re.IGNORECASE)
        if match:
            content = re.sub(placeholder_pattern, html, content, count=1, flags=re.IGNORECASE)
            continue
            
        # 2. Try to replace `<!-- IMAGE_PLACEHOLDER: ... -->`
        placeholder_pattern2 = rf'<!-- IMAGE_PLACEHOLDER:.*?(?:Hình|Bảng|Figure|Table|Minh họa|Illustration)\s*{identifier}.*?-->'
        match2 = re.search(placeholder_pattern2, content, re.IGNORECASE)
        if match2:
            content = re.sub(placeholder_pattern2, html, content, count=1, flags=re.IGNORECASE)
            continue
            
        # 3. Append after text mention
        text_pattern = rf'^(.*?(?:Hình|Bảng|Figure|Table|Minh họa|Illustration)\s*{identifier}.*)$'
        match3 = re.search(text_pattern, content, re.IGNORECASE | re.MULTILINE)
        if match3:
            html_replace = f'\\1\n{html}'
            content = re.sub(text_pattern, html_replace, content, count=1, flags=re.IGNORECASE | re.MULTILINE)

    if content != original_content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Injected images into {md_filename}')
