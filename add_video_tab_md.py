import glob
import re
import os

md_files = glob.glob('docs/buoi_*.md')
for filepath in md_files:
    # get the day number
    match = re.search(r'buoi_(\d+)\.md', filepath)
    if not match: continue
    day_num = match.group(1)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already inserted Video tab
    if '#### ** 🎬 Video **' in content:
        continue
    
    video_tab = f"#### ** 🎬 Video **\n\n<iframe src=\"video/Day{day_num}/index.html\" width=\"100%\" height=\"800px\" style=\"border: none;\"></iframe>\n\n"
    
    # Insert right before #### ** 🎦 Slide Bài Giảng **
    new_content = re.sub(
        r'(#### \*\* 🎦 Slide Bài Giảng \*\*)',
        video_tab + r'\1',
        content,
        count=1
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {filepath}")
