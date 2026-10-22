import os
import re

papers_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day02_Extra\papers"
for hf in sorted(os.listdir(papers_dir)):
    if not hf.endswith(".html"):
        continue
    p = os.path.join(papers_dir, hf)
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()
    
    srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    for s in srcs:
        if s.startswith(("http", "data:")):
            continue
        target = os.path.normpath(os.path.join(papers_dir, s))
        exists = os.path.exists(target)
        status = "OK" if exists else "MISSING"
        print(f"[{status}] {hf} -> {s}")

print("Validation completed.")
