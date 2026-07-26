# merge_tabs_buoi08_to_14.py
# Fix extra tabs in docs/buoi_08.md to docs/buoi_14.md by converting any non-tab #### heading to ### (Level 3 heading)

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
            if stripped.startswith('#### '):
                if 'Tiếng Anh (Bản gốc' not in stripped and 'Tiếng Việt (Bản dịch' not in stripped:
                    # Convert #### to ###
                    line = '### ' + stripped[5:] + '\n'
                    changed += 1
            new_lines.append(line)
        
        if changed > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"Updated {filepath}: converted {changed} extra #### headings to ### (merged into 1 Vietnamese tab).")
        else:
            print(f"Checked {filepath}: already has exactly 2 tabs (0 extra #### headings).")
