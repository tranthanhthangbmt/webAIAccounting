import os
import glob
import re

def update_html_files():
    html_files = glob.glob('Buoi_*.html')
    for f in html_files:
        match = re.search(r'Buoi_(\d+)\.html', f)
        if not match: continue
        day = match.group(1)
        
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if 'slide-tab' in content:
            print(f'{f} already has slide-tab.')
            continue
            
        # 1. Add tab button
        pattern1 = r'(<div class="tab" onclick="openTab\(\'vi-tab\', this\)">Tiếng Việt \(Bản dịch\)</div>\s*</div>)'
        replacement1 = r'<div class="tab" onclick="openTab(\'vi-tab\', this)">Tiếng Việt (Bản dịch)</div>\n        <div class="tab" onclick="openTab(\'slide-tab\', this)">Slide Bài Giảng</div>\n    </div>'
        content = re.sub(pattern1, replacement1, content)
        
        # 2. Add tab content before <script>
        slide_content = f'''    <div id="slide-tab" class="content">
        <iframe src="TaiLieu/slideAIAcc/Slide_AIAcc_Day{day}.pdf" width="100%" height="800px" style="border: none;"></iframe>
    </div>

    <script>'''
        content = content.replace('    <script>', slide_content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f} for Day {day}')

if __name__ == '__main__':
    update_html_files()
