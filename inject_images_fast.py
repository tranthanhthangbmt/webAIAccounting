import os
import re
import urllib.parse

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
    if md_filename in ['buoi_01.md', 'buoi_03.md']: continue

    md_path = os.path.join(docs_dir, md_filename)
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    injected_images = set()
    for identifier, info in available_images.items():
        if info['filename'] in content or urllib.parse.quote(info['filename']) in content:
            injected_images.add(identifier)

    lines = content.split('\n')
    new_lines = []
    changed = False

    for line in lines:
        if '> 📸 **Hình ảnh**' in line or '<!-- IMAGE_PLACEHOLDER' in line:
            # Check if it matches any available image
            matched_id = None
            for identifier in available_images:
                pattern = rf'(?:Hình|Bảng|Figure|Table|Minh họa|Illustration)\s*{identifier}\b'
                if re.search(pattern, line, re.IGNORECASE):
                    matched_id = identifier
                    break
            
            if matched_id:
                info = available_images[matched_id]
                html = f'\n<div style="text-align: center; margin: 20px auto;">\n    <img src="../{info["path"]}" alt="{info["caption"]}" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">\n    <div style="color: #666; font-style: italic; font-size: 0.9em;">{info["caption"]}</div>\n</div>\n'
                new_lines.append(html)
                injected_images.add(matched_id)
                changed = True
                continue # skip adding original line
            else:
                new_lines.append(line)
                continue

        # For normal lines, just append line
        new_lines.append(line)
        
        # Check if we should inject after this line
        if '<img' in line: continue
        
        for identifier in available_images:
            if identifier in injected_images: continue
            
            if f"Hình {identifier}" in line or f"Figure {identifier}" in line or f"Bảng {identifier}" in line or f"Table {identifier}" in line or f"Minh họa {identifier}" in line or f"MINH HỌA {identifier}" in line or f"ILLUSTRATION {identifier}" in line:
                info = available_images[identifier]
                html = f'\n<div style="text-align: center; margin: 20px auto;">\n    <img src="../{info["path"]}" alt="{info["caption"]}" style="max-width:100%; border-radius:8px; display:block; margin: 0 auto 10px;">\n    <div style="color: #666; font-style: italic; font-size: 0.9em;">{info["caption"]}</div>\n</div>\n'
                new_lines.append(html)
                injected_images.add(identifier)
                changed = True

    if changed:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f'Injected images into {md_filename}')
