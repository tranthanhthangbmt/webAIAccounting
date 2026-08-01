import os
import glob
import re

base_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting"
scratch_dir = os.path.join(base_dir, "scratch")
docs_dir = os.path.join(base_dir, "docs")
output_md = os.path.join(docs_dir, "practice_ch05.md")

# Ensure ordering of chunks
chunks = glob.glob(os.path.join(scratch_dir, "ch05_tr_chunk_*.md"))
chunks.sort(key=lambda x: int(re.search(r'ch05_tr_chunk_(\d+)', x).group(1)))

final_content = """<!-- tabs:start -->
#### **Tiếng Việt**

# Chương 5: Phân tích: Chuẩn bị Dữ liệu (Analysis: Data Preparation)

"""

for chunk_path in chunks:
    with open(chunk_path, 'r', encoding='utf-8') as f:
        final_content += f.read() + "\n\n---\n\n"

final_content += """
#### **English**
<iframe src="TaiLieu/textbookForPractice/Ch_05_Analysis_%20Data%20Preparation.pdf" width="100%" height="800px"></iframe>
<!-- tabs:end -->
"""

with open(output_md, 'w', encoding='utf-8') as f:
    f.write(final_content)

print(f"Assembled successfully to {output_md}")
