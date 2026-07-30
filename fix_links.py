import glob
import re

for filepath in glob.glob('docs/*.md'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(
        r'<a href="Datasets/([^"]+)" download target="_blank"><strong>([^<]+)</strong></a>',
        r'<a href="TaiLieu/Datasets/\1" download target="_blank"><strong>\2</strong></a>',
        content
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filepath}')
