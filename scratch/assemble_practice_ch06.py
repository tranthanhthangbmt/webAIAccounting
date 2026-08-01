import re
import os

header_part = """<!-- tabs:start -->
#### **Tiếng Việt**

# Chương 6: Phân tích: Mô hình Thông tin (Analysis: Information Modeling)
"""

footer_part = """
#### **English**
<iframe src="TaiLieu/textbookForPractice/Ch_06_Analysis_Data%20Preparation.pdf" width="100%" height="800px"></iframe>
<!-- tabs:end -->
"""

all_lines = []
for i in range(1, 12):  # 11 chunks
    chunk_file = f"scratch/ch06_tr_chunk_{i}.md"
    if os.path.exists(chunk_file):
        with open(chunk_file, "r", encoding="utf-8") as in_f:
            lines = in_f.read().split('\n')
            all_lines.extend(lines)

cleaned_lines = []
for line in all_lines:
    s = line.strip()
    if not s:
        cleaned_lines.append('')
        continue
    # Remove OCR page numbers and headers
    if re.match(r'^6-\d+.*$', s):
        continue
    if s in ['C H A PT E R 6', 'Phân tích: Thông tin', 'Mô hình hóa', 'Analysis: Information Modeling']:
        continue
    if s == 'OceanofPDF.com':
        continue
    if s == '---':
        continue
    
    # Strip any existing markdown headers that we might re-add
    if s.startswith('##'):
        s = s.lstrip('#').strip()
        
    cleaned_lines.append(s)

formatted_blocks = []
current_para = []

def flush_para():
    global current_para
    if not current_para:
        return
    text_para = ' '.join(current_para).strip()
    text_para = re.sub(r'\s+', ' ', text_para)
    
    # Custom post-processing for Ch06 formatting
    text_para = re.sub(r'C H A P T ÉP 6 Làm người mẫu Xem trước chương\s*', '**Xem trước chương**\n\n', text_para)
    text_para = re.sub(r'Lộ trình chương\s*', '\n\n**Lộ trình chương**\n\n', text_para)
    text_para = re.sub(r'Cái nhìn sâu sắc chuyên nghiệp:', '\n\n**Cái nhìn sâu sắc chuyên nghiệp:**', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ➊', '\n\n**MỤC TIÊU HỌC TẬP ➊**\n\n', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ❷', '\n\n**MỤC TIÊU HỌC TẬP ❷**\n\n', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ❸', '\n\n**MỤC TIÊU HỌC TẬP ❸**\n\n', text_para)
    text_para = re.sub(r'6\.1 Mô hình thông tin là gì\?', '\n\n## 6.1 Mô hình thông tin là gì?\n\n', text_para)
    text_para = re.sub(r'6\.2 Những mẫu nào triển khai thuật toán mô hình hóa thông tin\?', '\n\n## 6.2 Những mẫu nào triển khai thuật toán mô hình hóa thông tin?\n\n', text_para)
    text_para = re.sub(r'6\.2 Thông tin triển khai mẫu nào Thuật toán mô hình hóa\?', '\n\n## 6.2 Những mẫu nào triển khai thuật toán mô hình hóa thông tin?\n\n', text_para)
    text_para = re.sub(r'6\.3 Các cấu trúc chung của mô hình thông tin là gì\?', '\n\n## 6.3 Các cấu trúc chung của mô hình thông tin là gì?\n\n', text_para)
    text_para = re.sub(r'6\.3 Cấu trúc dữ liệu chung nào Mô hình thông tin\?', '\n\n## 6.3 Các cấu trúc chung của mô hình thông tin là gì?\n\n', text_para)
    text_para = re.sub(r'\) LO 6\.2', ')\n\n**LO 6.2** ', text_para)
    text_para = re.sub(r'\) LO 6\.3', ')\n\n**LO 6.3** ', text_para)
    text_para = re.sub(r'\) LO 6\.4', ')\n\n**LO 6.4** ', text_para)
    text_para = re.sub(r'Wiley\.\s+## 6\.1', 'Wiley.\n\n## 6.1', text_para)
    
    if text_para.strip():
        # Split again by newlines if we introduced any to keep block structure clean
        for sub in text_para.split('\n\n'):
            if sub.strip():
                formatted_blocks.append(sub.strip())
    current_para = []

i = 0
while i < len(cleaned_lines):
    s = cleaned_lines[i]
    if not s:
        flush_para()
        i += 1
        continue

    # Identify images (e.g., ![ILLUSTRATION 6.1](...))
    if s.startswith('![') and ']' in s and '(' in s and ')' in s:
        flush_para()
        formatted_blocks.append(s)
        i += 1
        continue

    # Major Sections
    m = re.match(r'^(6\.[1-9])\s*(.*)', s)
    if m and not s.lower().startswith('6.x'):
        flush_para()
        formatted_blocks.append(f"## {s}")
        i += 1
        continue

    # Subsections like LO 6.x
    if re.match(r'^LO\s*6\.\d+.*', s, re.IGNORECASE):
        flush_para()
        formatted_blocks.append(f"**{s}**")
        i += 1
        continue

    # Captions and Exercises
    if re.match(r'^(MINH HỌA|BE|EX|PR|PAC|FIG)\s*6\.\d+.*', s, re.IGNORECASE):
        flush_para()
        # Collect full exercise text if it's long
        ex_text = s
        i += 1
        while i < len(cleaned_lines) and cleaned_lines[i] and not re.match(r'^(MINH HỌA|BE|EX|PR|PAC|FIG)\s*6\.\d+.*', cleaned_lines[i], re.IGNORECASE):
            ex_text += " " + cleaned_lines[i]
            i += 1
        ex_text = re.sub(r'\s+', ' ', ex_text)
        formatted_blocks.append(f"**{ex_text}**")
        continue

    # Bullets
    if s.startswith('• ') or s.startswith('- '):
        flush_para()
        bullet_text = s[2:].strip()
        i += 1
        while i < len(cleaned_lines) and cleaned_lines[i] and not cleaned_lines[i].startswith('• ') and not cleaned_lines[i].startswith('- '):
            bullet_text += " " + cleaned_lines[i]
            i += 1
        bullet_text = re.sub(r'\s+', ' ', bullet_text)
        formatted_blocks.append(f"- {bullet_text}")
        continue
    
    # Numbered lists like 1. ..., 2. ...
    if re.match(r'^\d+\.\s+.*', s):
        flush_para()
        num_text = s
        i += 1
        while i < len(cleaned_lines) and cleaned_lines[i] and not re.match(r'^\d+\.\s+.*', cleaned_lines[i]) and not cleaned_lines[i].startswith('• '):
            num_text += " " + cleaned_lines[i]
            i += 1
        num_text = re.sub(r'\s+', ' ', num_text)
        # Force a proper markdown numbered list
        num_match = re.match(r'^(\d+)\.\s+(.*)', num_text)
        if num_match:
            formatted_blocks.append(f"{num_match.group(1)}. {num_match.group(2)}")
        else:
            formatted_blocks.append(f"{num_text}")
        continue
        
    # MỤC TIÊU HỌC TẬP highlighting
    if s.startswith("MỤC TIÊU HỌC TẬP"):
        flush_para()
        formatted_blocks.append(f"**{s}**")
        i += 1
        continue

    current_para.append(s)
    i += 1

flush_para()

final_md = [header_part.strip(), ""]
for block in formatted_blocks:
    final_md.append(block)
    final_md.append("")
final_md.append(footer_part.strip())

with open('docs/practice_ch06.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_md))

print(f"Assembled docs/practice_ch06.md with {len(formatted_blocks)} blocks.")
