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
        
        updated = False
        
        # Format 1: <div class="tab" onclick="openTab('vi-tab', this)">Tiếng Việt (Bản dịch)</div>
        if '<div class="tab" onclick="openTab(\'vi-tab\', this)">Tiếng Việt (Bản dịch)</div>' in content:
            if 'slide-tab' not in content:
                content = content.replace(
                    '<div class="tab" onclick="openTab(\'vi-tab\', this)">Tiếng Việt (Bản dịch)</div>',
                    '<div class="tab" onclick="openTab(\'vi-tab\', this)">Tiếng Việt (Bản dịch)</div>\n        <div class="tab" onclick="openTab(\'slide-tab\', this)">Slide Bài Giảng</div>'
                )
                
                slide_content = f'''    <div id="slide-tab" class="content">
        <iframe src="TaiLieu/slideAIAcc/Slide_AIAcc_Day{day}.pdf" width="100%" height="800px" style="border: none;"></iframe>
    </div>

    <script>'''
                content = content.replace('    <script>', slide_content)
                updated = True

        # Format 2: <button class="tab" onclick="openTab('vi-tab', this)">Tiếng Việt (Bản dịch)</button>
        elif '<button class="tab" onclick="openTab(\'vi-tab\', this)">Tiếng Việt (Bản dịch)</button>' in content:
            if 'slide-tab' not in content:
                content = content.replace(
                    '<button class="tab" onclick="openTab(\'vi-tab\', this)">Tiếng Việt (Bản dịch)</button>',
                    '<button class="tab" onclick="openTab(\'vi-tab\', this)">Tiếng Việt (Bản dịch)</button>\n        <button class="tab" onclick="openTab(\'slide-tab\', this)">Slide Bài Giảng</button>'
                )
                
                # The content container is `<div id="vi-tab" class="content-area"></div>`
                slide_content = f'''<div id="vi-tab" class="content-area"></div>
      <div id="slide-tab" class="content-area">
          <iframe src="TaiLieu/slideAIAcc/Slide_AIAcc_Day{day}.pdf" width="100%" height="800px" style="border: none;"></iframe>
      </div>'''
                content = content.replace('<div id="vi-tab" class="content-area"></div>', slide_content)
                updated = True

        # Format 3: <button class="tablinks" onclick="openTab(event, 'English')">English</button>
        elif '<button class="tablinks" onclick="openTab(event, \'English\')">English</button>' in content:
            if 'Slide Bài Giảng' not in content:
                content = content.replace(
                    '<button class="tablinks" onclick="openTab(event, \'English\')">English</button>',
                    '<button class="tablinks" onclick="openTab(event, \'English\')">English</button>\n        <button class="tablinks" onclick="openTab(event, \'Slide\')">Slide Bài Giảng</button>'
                )
                
                slide_content = f'''    <div id="Slide" class="tabcontent">
        <iframe src="TaiLieu/slideAIAcc/Slide_AIAcc_Day{day}.pdf" width="100%" height="800px" style="border: none;"></iframe>
    </div>

    <script>'''
                content = content.replace('    <script>', slide_content)
                updated = True
        
        if updated:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Updated {f} for Day {day}')
        else:
            print(f'{f} already up-to-date or unknown format.')

if __name__ == '__main__':
    update_html_files()
