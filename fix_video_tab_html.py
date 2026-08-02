import os
import re
import glob

html_files = glob.glob('Buoi_*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix the incorrectly escaped quotes in openTab
    content = content.replace("openTab(\\'video-tab\\', this)", "openTab('video-tab', this)")
    content = content.replace("openTab(\\'vi-tab\\', this)", "openTab('vi-tab', this)")
    content = content.replace("openTab(\\'slide-tab\\', this)", "openTab('slide-tab', this)")
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Fixed {f}')
