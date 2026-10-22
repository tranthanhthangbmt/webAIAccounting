import os
import re
from urllib.parse import unquote

day02_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day02_Extra"
papers_dir = os.path.join(day02_dir, "papers")

html_files = [os.path.join(day02_dir, "index.html")] + [
    os.path.join(papers_dir, f) for f in os.listdir(papers_dir) if f.endswith(".html")
]

total_checked = 0
missing_count = 0

for hf in sorted(html_files):
    dir_name = os.path.dirname(hf)
    rel_hf = os.path.relpath(hf, day02_dir)
    with open(hf, "r", encoding="utf-8") as f:
        html = f.read()

    links = re.findall(r'(?:href|src)=["\']([^#"\']+)["\']', html)
    print(f"\n--- Checking {rel_hf} ({len(links)} links/srcs) ---")
    for link in links:
        if link.startswith(("http", "mailto:", "data:", "javascript:")):
            continue
        clean_link = unquote(link)
        target = os.path.normpath(os.path.join(dir_name, clean_link))
        total_checked += 1
        if not os.path.exists(target):
            print(f"  [MISSING] {link} -> {target}")
            missing_count += 1
        else:
            if any(k in link for k in ["P0", "P1", "P2", "P3", "P4"]):
                print(f"  [SLIDE OK] {link} ({os.path.getsize(target):,} bytes)")

print(f"\n==========================================")
print(f"Total links verified: {total_checked}")
print(f"Total missing: {missing_count}")
if missing_count == 0:
    print("STATUS: ALL LINKS & SLIDES ARE PERFECT!")
print(f"==========================================")

