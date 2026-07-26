import os, glob
for path in sorted(glob.glob('docs/buoi_*.md')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    trang_count = content.count('--- Trang ')
    print(f"{path}: {trang_count} '--- Trang ' markers, length {len(content)}")
