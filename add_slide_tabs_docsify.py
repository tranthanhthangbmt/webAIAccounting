import os
import glob
import re

def update_docs_files():
    md_files = glob.glob('docs/buoi_*.md')
    for f in md_files:
        match = re.search(r'buoi_(\d+)\.md', f)
        if not match: continue
        day = match.group(1)
        
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if '🎦 Slide Bài Giảng' in content:
            print(f'{f} already has slide tab.')
            continue
            
        slide_tab = f'''#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slideAIAcc/Slide_AIAcc_Day{day}.pdf" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day{day}.pdf" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day{day}.pdf" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

<!-- tabs:end -->'''

        if '<!-- tabs:end -->' in content:
            content = content.replace('<!-- tabs:end -->', slide_tab)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Updated {f} for Day {day}')
        else:
            print(f'{f} does NOT have <!-- tabs:end -->, skipping.')

if __name__ == '__main__':
    update_docs_files()
