import re
import os

header_part = """<!-- tabs:start -->
#### **Tiếng Việt**

# Chương 9: Truyền đạt Kết quả Phân tích Dữ liệu (Communicating Data Analysis Results)
"""

footer_part = """
#### **English**
<iframe src="TaiLieu/textbookForPractice/Ch_09_Interpreting%20Data%20Analysis%20Results.pdf" width="100%" height="800px"></iframe>
<!-- tabs:end -->
"""

all_lines = []
for i in range(1, 13):  # 12 chunks
    chunk_file = f"scratch/ch09_tr_chunk_{i}.md"
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
    if re.match(r'^9-\d+.*$', s) or re.match(r'^\d+-9.*$', s):
        continue
    if s in ['C H A PT E R 9', 'C H A P T ER 9', 'Truyền đạt dữ liệu', 'Kết quả phân tích', 'Truyền đạt Kết quả Phân tích Dữ liệu', 'Communicating Data Analysis Results', 'Communicating Data', 'Analysis Results']:
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
    
    # Custom post-processing for Ch09 formatting
    text_para = re.sub(r'C H A P T ÉP 9.*Xem trước chương\s*', '**Xem trước chương**\n\n', text_para)
    text_para = re.sub(r'Lộ trình chương\s*', '\n\n**Lộ trình chương**\n\n', text_para)
    text_para = re.sub(r'Cái nhìn sâu sắc chuyên nghiệp:', '\n\n**Cái nhìn sâu sắc chuyên nghiệp:**', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ➊', '\n\n**MỤC TIÊU HỌC TẬP ➊**\n\n', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ❷', '\n\n**MỤC TIÊU HỌC TẬP ❷**\n\n', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ❸', '\n\n**MỤC TIÊU HỌC TẬP ❸**\n\n', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ❹', '\n\n**MỤC TIÊU HỌC TẬP ❹**\n\n', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ❺', '\n\n**MỤC TIÊU HỌC TẬP ❺**\n\n', text_para)
    text_para = re.sub(r'9\.1 (\w+.*)', r'\n\n## 9.1 \1\n\n', text_para)
    text_para = re.sub(r'9\.2 (\w+.*)', r'\n\n## 9.2 \1\n\n', text_para)
    text_para = re.sub(r'9\.3 (\w+.*)', r'\n\n## 9.3 \1\n\n', text_para)
    text_para = re.sub(r'9\.4 (\w+.*)', r'\n\n## 9.4 \1\n\n', text_para)
    text_para = re.sub(r'9\.5 (\w+.*)', r'\n\n## 9.5 \1\n\n', text_para)
    text_para = re.sub(r'\) LO 9\.1', ')\n\n**LO 9.1** ', text_para)
    text_para = re.sub(r'\) LO 9\.2', ')\n\n**LO 9.2** ', text_para)
    text_para = re.sub(r'\) LO 9\.3', ')\n\n**LO 9.3** ', text_para)
    text_para = re.sub(r'\) LO 9\.4', ')\n\n**LO 9.4** ', text_para)
    text_para = re.sub(r'\) LO 9\.5', ')\n\n**LO 9.5** ', text_para)
    text_para = re.sub(r'Wiley\.\s+## 9\.1', 'Wiley.\n\n## 9.1', text_para)
    
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

    # Identify images (e.g., ![ILLUSTRATION 9.1](...))
    if s.startswith('![') and ']' in s and '(' in s and ')' in s:
        flush_para()
        formatted_blocks.append(s)
        i += 1
        continue

    # Major Sections
    m = re.match(r'^(9\.[1-9])\s*(.*)', s)
    if m and not s.lower().startswith('9.x'):
        flush_para()
        formatted_blocks.append(f"## {s}")
        i += 1
        continue

    # Subsections like LO 9.x
    if re.match(r'^LO\s*9\.\d+.*', s, re.IGNORECASE):
        flush_para()
        formatted_blocks.append(f"**{s}**")
        i += 1
        continue

    # Captions and Exercises
    if re.match(r'^(MINH HỌA|BE|EX|PR|PAC|FIG|Apply It|Intro|Madison public library)\s*9\.\d+.*', s, re.IGNORECASE):
        flush_para()
        # Collect full exercise text if it's long
        ex_text = s
        i += 1
        while i < len(cleaned_lines) and cleaned_lines[i] and not re.match(r'^(MINH HỌA|BE|EX|PR|PAC|FIG|Apply It|Intro|Madison public library)\s*9\.\d+.*', cleaned_lines[i], re.IGNORECASE):
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

with open('docs/practice_ch09.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_md))

print(f"Assembled docs/practice_ch09.md with {len(formatted_blocks)} blocks.")
