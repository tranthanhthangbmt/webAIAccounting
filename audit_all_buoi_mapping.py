# audit_all_buoi_mapping.py
# Audit the mapping between Syllabus (DE CUONG TRI TUE NHAN TAO- 2025.docx),
# textbook/ PDF files, and docs/buoi_XX.md Vietnamese tab titles/content.

import docx
import os
import re

# 1. Extract syllabus topics from DE CUONG docx
doc = docx.Document('d:\\DongAUniversity\\TÀI LIỆU DẠY HỌC_2024-2025\\Môn TTNT cho kế toán_2026\\DE CUONG TRI TUE NHAN TAO- 2025.docx')
tbl = doc.tables[5]

syllabus = {}
for r_idx in range(1, len(tbl.rows)):
    row = tbl.rows[r_idx]
    c0 = row.cells[0].text.strip().replace('\n', ' ')
    c1 = row.cells[1].text.strip().replace('\n', ' ')
    if c0.isdigit():
        syllabus[int(c0)] = c1

# 2. Extract PDF files mapped in textbook/ for each buoi
import glob
pdf_files = sorted(glob.glob('textbook/Buoi_*.pdf'))
buoi_pdfs = {}
for p in pdf_files:
    fname = os.path.basename(p)
    # Extract buoi number (e.g. Buoi_01 -> 1, Buoi_02A -> 2)
    m = re.match(r'Buoi_0*(\d+)', fname, re.IGNORECASE)
    if m:
        b_num = int(m.group(1))
        buoi_pdfs.setdefault(b_num, []).append(fname)

# 3. Check docs/buoi_XX.md Vietnamese tab titles and headings
for b_num in sorted(syllabus.keys()):
    if b_num == 10:  # Midterm exam
        continue
    md_file = f'docs/buoi_{b_num:02d}.md'
    print(f"===============================================================")
    print(f"📌 BUỔI {b_num}")
    print(f"📖 ĐỀ CƯƠNG (Syllabus):")
    print(f"   -> {syllabus.get(b_num, 'N/A')[:130]}...")
    print(f"📂 FILE PDF TRONG TEXTBOOK ({len(buoi_pdfs.get(b_num, []))} file):")
    for f in buoi_pdfs.get(b_num, []):
        print(f"   -> {f}")
    
    if os.path.exists(md_file):
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Find main H1 title at top of file
        main_title = "N/A"
        for line in lines[:10]:
            if line.strip().startswith('# ') and '**' not in line:
                main_title = line.strip()
                break
        # Find headings inside Vietnamese tab (after #### ** 🇻🇳 Tiếng Việt)
        vi_headings = []
        in_vi_tab = False
        for line in lines:
            if '🇻🇳 Tiếng Việt' in line:
                in_vi_tab = True
                continue
            if in_vi_tab and line.strip().startswith('#') and '**' not in line:
                vi_headings.append(line.strip())
        print(f"📝 TAB TIẾNG VIỆT (docs/buoi_{b_num:02d}.md):")
        print(f"   -> Tiêu đề trang: {main_title}")
        print(f"   -> Các đề mục chính Tiếng Việt ({len(vi_headings)} đề mục):")
        for h in vi_headings[:4]:
            print(f"      • {h}")
    else:
        print(f"❌ KHÔNG TÌM THẤY FILE {md_file}")

