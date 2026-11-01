# Update Day03_Extra index.html to add Day 04 Extra
p = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day03_Extra\index.html"
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

old_str = '<a href="../Day02_Extra/index.html" class="nav-btn">'
new_str = '<a href="../Day04_Extra/index.html" class="nav-btn" style="border-color: rgba(139, 92, 246, 0.4); color: #c084fc;">\n          Day 04 Extra (AI Tạo Sinh)\n        </a>\n        <a href="../Day02_Extra/index.html" class="nav-btn">'

if old_str in text:
    text = text.replace(old_str, new_str, 1)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)
    print("Updated Day03_Extra/index.html successfully")
else:
    print("Target not found in Day03_Extra/index.html")

