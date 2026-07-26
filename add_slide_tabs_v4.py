import os
import glob
import re

def update_html_files():
    html_files = ['Buoi_02.html', 'Buoi_03.html', 'Buoi_04.html', 'Buoi_12.html', 'Buoi_13.html', 'Buoi_14.html']
    for f in html_files:
        if not os.path.exists(f): continue
        match = re.search(r'Buoi_(\d+)\.html', f)
        if not match: continue
        day = match.group(1)
        
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if 'slide-content' in content or 'Slide Bài Giảng' in content:
            print(f'{f} already has slide tab.')
            continue
            
        # Add the tab button
        content = re.sub(
            r'(<div class="tab"[^>]*onclick="switchTab\(\'[^\']+\'\)"[^>]*>.*?</div>\s*)(</div>)',
            r'\1<div class="tab" onclick="switchTab(\'slide\')">Slide Bài Giảng</div>\n    \2',
            content, count=1
        )
        
        # Add the tab content right before <script>
        slide_content = f'''    <div id="slide-content" class="content">
        <iframe src="TaiLieu/slideAIAcc/Slide_AIAcc_Day{day}.pdf" width="100%" height="800px" style="border: none;"></iframe>
    </div>

    <script>'''
        content = content.replace('    <script>', slide_content)
        
        # Update the switchTab function
        new_switchTab = '''        function switchTab(lang) {
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.content').forEach(content => content.classList.remove('active'));

            if (lang === 'en') {
                document.querySelector('.tab[onclick*="switchTab(\\'en\\')"]').classList.add('active');
                document.getElementById('en-content').classList.add('active');
            } else if (lang === 'vi') {
                document.querySelector('.tab[onclick*="switchTab(\\'vi\\')"]').classList.add('active');
                document.getElementById('vi-content').classList.add('active');
            } else if (lang === 'slide') {
                document.querySelector('.tab[onclick*="switchTab(\\'slide\\')"]').classList.add('active');
                document.getElementById('slide-content').classList.add('active');
            }
        }'''
        
        content = re.sub(r'        function switchTab\(lang\) \{.*?\n        \}', new_switchTab, content, flags=re.DOTALL)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f} for Day {day}')

if __name__ == '__main__':
    update_html_files()
