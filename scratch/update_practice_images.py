import os
import re
import glob

base_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting"
scratch_dir = os.path.join(base_dir, "scratch")
figures_dir = os.path.join(base_dir, "TaiLieu", "textbookForPractice", "Figures")

# Get all images
images_by_id = {}
for ch in [1, 2, 3, 4, 5, 6]:
    ch_str = f"Ch_{ch:02d}"
    ch_dir = os.path.join(figures_dir, ch_str)
    if not os.path.isdir(ch_dir):
        continue
    for img in os.listdir(ch_dir):
        if img.lower().endswith(".png") or img.lower().endswith(".jpg"):
            basename = os.path.splitext(img)[0]
            
            # Group e.g. "BE 1.1", "BE 1.1_1" under "BE 1.1"
            match = re.match(r'^(.*?(?:\d+\.\d+[A-Z]*))(?:_\d+)?$', basename)
            if match:
                identifier = match.group(1).strip()
            else:
                identifier = basename.strip()
                
            if identifier not in images_by_id:
                images_by_id[identifier] = []
            
            # Use forward slashes for markdown
            rel_path = f"../TaiLieu/textbookForPractice/Figures/{ch_str}/{img}".replace(" ", "%20")
            images_by_id[identifier].append((basename, rel_path))

# Sort the lists so that base image comes first, then _1, _2
for k in images_by_id:
    images_by_id[k].sort()

print(f"Found {len(images_by_id)} unique identifiers.")

def process_chunk_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    for identifier, imgs in images_by_id.items():
        if identifier == 'rename_mapping': continue
        
        # Build the Markdown string for this identifier's images
        img_md = "\n"
        for basename, rel_path in imgs:
            img_md += f"![{basename}]({rel_path})\n"
        img_md += "\n"

        # Check if any of these exact image links already exist in the content
        # If so, we assume it's already injected
        # To be safe, we check if the FIRST image is already in the content
        first_rel_path = imgs[0][1]
        if first_rel_path in content:
            continue
            
        # Also check if an older `page_...png` image is there for this identifier.
        # Often the identifier is followed by an image tag. 
        # We can find where the identifier appears in text (like `**BE 1.1`)
        translated_id = identifier
        if identifier.startswith("ILLUSTRATION"):
            translated_id = identifier.replace("ILLUSTRATION", "MINH HỌA")
        elif identifier.startswith("Apply It"):
            translated_id = identifier.replace("Apply It", "Áp dụng nó")
            
        esc_id = re.escape(identifier)
        esc_trans_id = re.escape(translated_id)
        
        parts = content.split('\n\n')
        for i, part in enumerate(parts):
            if re.search(r'\b' + esc_id + r'\b', part, re.IGNORECASE) or (esc_trans_id != esc_id and re.search(r'\b' + esc_trans_id + r'\b', part, re.IGNORECASE)):
                if i + 1 < len(parts) and ('![BE ' in parts[i+1] or '![ILLUSTRATION ' in parts[i+1] or 'page_' in parts[i+1] or ('![' in parts[i+1] and 'TaiLieu/textbookForPractice' in parts[i+1])):
                    if 'TaiLieu/textbookForPractice/Figures' in parts[i+1]:
                        if not first_rel_path in parts[i+1]:
                            parts[i+1] = img_md.strip()
                            break
                else:
                    if '**' + identifier in part or '**' + translated_id in part or '### ' + identifier in part or '### ' + translated_id in part or part.startswith('**' + identifier) or part.startswith('**' + translated_id):
                        parts.insert(i+1, img_md.strip())
                        break
                    elif 'ILLUSTRATION' in identifier or 'Figure' in identifier or 'Apply It' in identifier:
                        parts.insert(i+1, img_md.strip())
                        break

        new_content = '\n\n'.join(parts)
        if new_content != content:
            content = new_content

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

# Process all tr_chunk files for Ch_01, Ch_02, Ch_03, etc.
for ch in [1, 2, 3, 4, 5, 6]:
    pattern = os.path.join(scratch_dir, f"ch{ch:02d}_tr_chunk_*.md")
    for filepath in glob.glob(pattern):
        process_chunk_file(filepath)

print("Done processing chunk files.")
