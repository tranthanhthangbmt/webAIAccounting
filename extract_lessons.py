import os
import glob
import re

docs_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs"
files = sorted(glob.glob(os.path.join(docs_dir, "buoi_*.md")))

output = ""

for file in files:
    basename = os.path.basename(file)
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Heading
    heading_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    heading = heading_match.group(1).strip() if heading_match else "N/A"
    
    # 2. Vietnamese Tab Content
    # We look for "Tiếng Việt" and take the content until the next tab or EOF
    vi_tab_match = re.search(r'Tiếng Việt\s*\*\*\s*(.*?)(?=\n#### \*\*|\n<!-- tabs:|\Z)', content, re.DOTALL)
    vi_content = vi_tab_match.group(1).strip() if vi_tab_match else "N/A"
    # Truncate vi_content for the report if it's too long
    vi_summary = vi_content[:200] + "..." if len(vi_content) > 200 else vi_content
    vi_summary = vi_summary.replace('\n', ' ')

    # 3. Slide link
    slide_match = re.search(r'<object data="(.*?)"', content)
    slide_link = slide_match.group(1) if slide_match else "N/A"
    
    output += f"--- {basename} ---\n"
    output += f"Heading: {heading}\n"
    output += f"Slide: {slide_link}\n"
    output += f"VN Content: {vi_summary}\n\n"

with open('scratch_analysis.txt', 'w', encoding='utf-8') as f:
    f.write(output)
print("Analysis complete")
