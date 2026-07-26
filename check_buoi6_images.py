# check_buoi6_images.py
import glob, re

for fn in glob.glob('**/*6*.*', recursive=True):
    if fn.endswith('.html') or fn.endswith('.md') or fn.endswith('.txt'):
        try:
            with open(fn, 'r', encoding='utf-8') as f:
                c = f.read()
            imgs = re.findall(r'(!\[.*?\]\(.*?\)|IMAGE_PLACEHOLDER:.*|src=[\"\'].*?[\"\'])', c)
            if imgs:
                print(fn, '->', len(imgs), 'imgs:', imgs[:3])
        except Exception as e:
            pass
