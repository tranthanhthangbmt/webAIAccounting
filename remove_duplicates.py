import re
import os
import urllib.parse

docs_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs'

# The block looks exactly like this, where whitespace might vary slightly:
block_pattern = re.compile(
    r'\n?<div style="text-align: center; margin: 20px auto;">\n\s*<img src="(.*?)" alt=".*?" style=".*?>\n\s*<div style=".*?">.*?</div>\n</div>\n?',
    re.IGNORECASE
)

for md_filename in os.listdir(docs_dir):
    if not md_filename.endswith('.md'): continue
    md_path = os.path.join(docs_dir, md_filename)
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    seen_images = set()

    def replace_block(match):
        src = match.group(1)
        normalized_src = urllib.parse.unquote(src) # normalize `%20` back to space
        if normalized_src in seen_images:
            return '' # remove duplicate
        else:
            seen_images.add(normalized_src)
            return match.group(0) # keep the first one

    new_content = block_pattern.sub(replace_block, content)

    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Removed duplicates from {md_filename}')
