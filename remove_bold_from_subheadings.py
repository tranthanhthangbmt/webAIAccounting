# remove_bold_from_subheadings.py
# Fix extra tabs in docs/buoi_08.md, buoi_09.md, buoi_11.md by removing ** from subheadings or converting to bold paragraphs

import glob

files = sorted(glob.glob('docs/buoi_*.md'))

for filepath in files:
    session_num = int(filepath.split('_')[1].split('.')[0])
    if session_num >= 8:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        changed = 0
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('#') and '**' in stripped:
                if 'Tiếng Anh (Bản gốc' not in stripped and 'Tiếng Việt (Bản dịch' not in stripped:
                    # If it's buoi 8 or buoi 9, convert these specific list intros to bold paragraphs (remove ### and **)
                    if session_num in [8, 9] and ('Các loại gian lận' in stripped or 'Các thuộc tính' in stripped or 'Các ứng dụng' in stripped or 'Các chiến lược' in stripped):
                        # Remove heading markers but keep **
                        new_text = stripped.lstrip('#').strip()
                        line = new_text + '\n'
                        changed += 1
                    else:
                        # Otherwise remove ** from the heading
                        new_text = stripped.replace('**', '')
                        line = new_text + '\n'
                        changed += 1
            new_lines.append(line)
        
        if changed > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"Updated {filepath}: cleaned {changed} headings that triggered docsify-tabs.")
        else:
            print(f"Checked {filepath}: already clean (0 extra tab triggers).")
