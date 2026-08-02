import glob
import re

for f in glob.glob('docs/buoi_*.md'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We replace the specific iframe height style with a responsive one
    content = re.sub(
        r'<iframe src="video/Day(\d+)/index\.html" width="100%" height="800px" style="border: none;"></iframe>',
        r'<iframe src="video/Day\1/index.html" style="width: 100%; aspect-ratio: 16/9; max-height: 75vh; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>',
        content
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
