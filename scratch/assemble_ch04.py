import os

output_file = "docs/practice_ch04.md"

header = """# Chương 4: Lập kế hoạch Dữ liệu và Chiến lược Phân tích (Planning Data and Analysis Strategies)

<!-- tabs:start -->
#### **Tiếng Việt**

"""

footer = """
#### **English**

<embed src="../TaiLieu/textbookForPractice/Ch_04_Planning Data and.pdf" type="application/pdf" width="100%" height="800px" />

<!-- tabs:end -->
"""

with open(output_file, "w", encoding="utf-8") as out_f:
    out_f.write(header)
    for i in range(1, 11):
        chunk_file = f"scratch/ch04_tr_chunk_{i}.md"
        if os.path.exists(chunk_file):
            with open(chunk_file, "r", encoding="utf-8") as in_f:
                out_f.write(in_f.read() + "\n\n")
        else:
            print(f"Warning: {chunk_file} not found.")
    out_f.write(footer)

print(f"Successfully assembled {output_file}")
