import os
import re
import glob

html_files = glob.glob('Buoi_*.html')
for f in html_files:
    match = re.search(r'Buoi_(\d+)\.html', f)
    if not match: continue
    day_num = match.group(1)
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'id="video-tab"' in content:
        print(f'Already has Video tab: {f}')
        continue
    
    # 1. Add the tab button
    # Find: <div class="tab" onclick="openTab('vi-tab', this)">Tiếng Việt</div>
    # Replace: <div class="tab" onclick="openTab('vi-tab', this)">Tiếng Việt</div>\n        <div class="tab" onclick="openTab('video-tab', this)">Video</div>
    # Be careful with escaped quotes like \'vi-tab\' vs 'vi-tab'
    
    tab_pattern = r'(<div class="tab" onclick="openTab\(\\\'?vi-tab\\\'?, this\)">Tiếng Việt</div>)'
    tab_replacement = r'\1\n        <div class="tab" onclick="openTab(\'video-tab\', this)">Video</div>'
    content = re.sub(tab_pattern, tab_replacement, content)
    
    # 2. Add the tab content
    # Find: <div id="vi-tab" class="content">...</div>
    # Actually just add it before <div id="slide-tab"
    
    content_pattern = r'(<div id="slide-tab" class="content">)'
    content_replacement = f'<div id="video-tab" class="content">\n        <iframe src="video/Day{day_num}/index.html" width="100%" height="800px" style="border: none;"></iframe>\n    </div>\n\n    \\1'
    content = re.sub(content_pattern, content_replacement, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated {f}')
