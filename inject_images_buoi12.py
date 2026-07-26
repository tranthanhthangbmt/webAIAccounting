import os
import re

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'
fig_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\Figures'

def inject_images(md_filename, fig_subdir):
    md_path = os.path.join(docs_dir, md_filename)
    fig_path = os.path.join(fig_dir, fig_subdir)
    
    if not os.path.exists(md_path) or not os.path.exists(fig_path):
        print(f'Skipping {md_filename} because file or folder missing.')
        return
        
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    images = os.listdir(fig_path)
    
    # We find all lines like: > 📸 **Hình ảnh**: Figure 6.2: Data scientist Venn diagram
    # or <!-- IMAGE_PLACEHOLDER: Figure 1.1 Relationship between AI, ML, and DL. -->
    
    def replacer(match):
        caption = match.group(1).strip()
        # Find the identifier, e.g. "Figure 6.2" or "Table 6.1"
        id_match = re.match(r'(Figure \d+\.\d+|Table \d+\.\d+|Hình \d+\.\d+|Bảng \d+\.\d+)', caption, re.IGNORECASE)
        
        if id_match:
            identifier = id_match.group(1).lower()
            # Find matching image in the folder
            for img in images:
                if img.lower().startswith(identifier):
                    print(f"Matched {caption} with {img}")
                    return f"![{caption}](Figures/{fig_subdir}/{img})"
            print(f"WARNING: Could not find image for {caption}")
        else:
            print(f"WARNING: Could not extract identifier from {caption}")
            
        return match.group(0) # Do not replace if not found
        
    new_content = re.sub(r'> 📸 \*\*Hình ảnh\*\*:(.*?)(?=\n|$)', replacer, content)
    new_content = re.sub(r'<!-- IMAGE_PLACEHOLDER:(.*?)-->', replacer, new_content)
    
    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {md_filename}")
    else:
        print(f"No changes made to {md_filename}")

print("Processing Buoi 1...")
inject_images('buoi_01.md', 'Buoi_01')

print("\nProcessing Buoi 2...")
inject_images('buoi_02.md', 'Buoi_02B')
