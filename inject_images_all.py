import os
import re

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'
fig_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\Figures'

# Collect all available images and their relative paths
available_images = {} 

for subdir in os.listdir(fig_dir):
    if not subdir.startswith('Buoi_0') and not subdir.startswith('Buoi_1'):
        continue
        
    subdir_path = os.path.join(fig_dir, subdir)
    if os.path.isdir(subdir_path):
        for img in os.listdir(subdir_path):
            id_match = re.match(r'(Figure \d+\.\d+|Table \d+\.\d+|Hình \d+\.\d+|Bảng \d+\.\d+)', img, re.IGNORECASE)
            if id_match:
                identifier = id_match.group(1).lower()
                available_images[identifier] = f"Figures/{subdir}/{img}"

def inject_all_md():
    for md_filename in os.listdir(docs_dir):
        if not md_filename.endswith('.md'): continue
        if not (md_filename.startswith('buoi_0') and '01' <= md_filename[5:7] <= '07'):
            continue
            
        md_path = os.path.join(docs_dir, md_filename)
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def replacer(match):
            caption = match.group(1).strip()
            id_match = re.match(r'(Figure \d+\.\d+|Table \d+\.\d+|Hình \d+\.\d+|Bảng \d+\.\d+)', caption, re.IGNORECASE)
            
            if id_match:
                identifier = id_match.group(1).lower()
                if identifier in available_images:
                    img_path = available_images[identifier]
                    print(f"[{md_filename}] Matched {identifier} -> {img_path}")
                    # Using HTML img tag is robust against spaces and parentheses in the filename.
                    return f'<img src="../{img_path}" alt="{caption}" style="max-width:100%; border-radius:8px; display:block; margin: 20px auto;">'
                else:
                    print(f"[{md_filename}] WARNING: Image for '{identifier}' not found in Figures/")
            
            return match.group(0)
            
        # First try to replace markdown tags that might be broken:
        # e.g. ![caption](../Figures/...)
        def md_replacer(match):
            caption = match.group(1)
            path = match.group(2)
            # if it's already an HTML tag or already processed, ignore
            return f'<img src="{path}" alt="{caption}" style="max-width:100%; border-radius:8px; display:block; margin: 20px auto;">'

        # Safely replace markdown images with HTML tags (matches until .PNG or .png)
        new_content = re.sub(r'!\[(.*?)\]\(((?:(?:\.\./)?Figures/)(?:.*?)(?:\.PNG|\.png|\.jpg|\.jpeg))\)', md_replacer, content)
            
        new_content = re.sub(r'> 📸 \*\*Hình ảnh\*\*:(.*?)(?=\n|$)', replacer, new_content)
        new_content = re.sub(r'<!-- IMAGE_PLACEHOLDER:(.*?)-->', replacer, new_content)
        
        if new_content != content:
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {md_filename}\n")
        else:
            print(f"No changes made to {md_filename}\n")

print("Processing markdown files...")
inject_all_md()
