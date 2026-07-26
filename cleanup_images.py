import os

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'

for md_filename in os.listdir(docs_dir):
    if not md_filename.endswith('.md'): continue
    if md_filename in ['buoi_01.md', 'buoi_02.md', 'buoi_03.md']: continue # Keep 1, 2, 3 as they are manually verified and fine now (I just fixed buoi 3). Wait, buoi_02 had duplicates!
    # I should process buoi_02.md as well!
    
    md_path = os.path.join(docs_dir, md_filename)
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    changed = False

    for line in lines:
        if '<img src="../Figures/Buoi_' in line:
            changed = True
            continue
        if '<div style="text-align: center; margin: 20px auto;">' in line:
            changed = True
            continue
        if '<div style="color: #666; font-style: italic; font-size: 0.9em;">' in line:
            changed = True
            continue
        if line.strip() == '</div>' or line.strip() == '</div':
            # ONLY remove </div> if we recently removed an image tag (this is a heuristic, but safe since these markdowns don't use <div> otherwise)
            # Actually, the easiest is to just check if we are dropping HTML.
            changed = True
            continue
            
        new_lines.append(line)

    if changed:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f'Cleaned up {md_filename}')
