import re
import os

with open('docs/practice_ch05.md', 'r', encoding='utf-8') as f:
    text = f.read()

header_marker = "# Chương 5: Phân tích: Chuẩn bị Dữ liệu (Analysis: Data Preparation)"
footer_marker = "#### **English**"

if header_marker not in text or footer_marker not in text:
    print("Could not find markers")
    exit(1)

header_idx = text.find(header_marker) + len(header_marker)
footer_idx = text.find(footer_marker)

header_part = text[:header_idx]
body_part = text[header_idx:footer_idx]
footer_part = text[footer_idx:]

lines = body_part.split('\n')
cleaned_lines = []
for line in lines:
    s = line.strip()
    if not s:
        cleaned_lines.append('')
        continue
    # Remove OCR page numbers and headers
    if re.match(r'^5-\d+.*$', s):
        continue
    if s in ['C H A PT E R 5', 'Phân tích: Dữ liệu', 'Chuẩn bị']:
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
    if text_para:
        formatted_blocks.append(text_para)
    current_para = []

i = 0
while i < len(cleaned_lines):
    s = cleaned_lines[i]
    if not s:
        flush_para()
        i += 1
        continue

    # Identify images (e.g., ![ILLUSTRATION 5.1](...))
    if s.startswith('![') and ']' in s and '(' in s and ')' in s:
        flush_para()
        formatted_blocks.append(s)
        i += 1
        continue

    # Major Sections
    m = re.match(r'^(5\.[1-9])\s*(.*)', s)
    if m and not s.lower().startswith('5.x'):
        flush_para()
        formatted_blocks.append(f"## {s}")
        i += 1
        continue

    # Subsections like LO 5.x
    if re.match(r'^LO\s*5\.\d+.*', s, re.IGNORECASE):
        flush_para()
        formatted_blocks.append(f"### **{s}**")
        i += 1
        continue

    # Captions and Exercises
    if re.match(r'^(MINH HỌA|BE|EX|PR|PAC)\s*5\.\d+.*', s, re.IGNORECASE):
        flush_para()
        # Collect full exercise text if it's long
        ex_text = s
        i += 1
        while i < len(cleaned_lines) and cleaned_lines[i] and not re.match(r'^(MINH HỌA|BE|EX|PR|PAC)\s*5\.\d+.*', cleaned_lines[i], re.IGNORECASE):
            ex_text += " " + cleaned_lines[i]
            i += 1
        ex_text = re.sub(r'\s+', ' ', ex_text)
        formatted_blocks.append(f"#### **{ex_text}**")
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
        formatted_blocks.append(f"{num_text}")
        continue

    current_para.append(s)
    i += 1

flush_para()

final_md = [header_part.strip(), ""]
for block in formatted_blocks:
    final_md.append(block)
    final_md.append("")
final_md.append(footer_part.strip())

with open('docs/practice_ch05.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_md))

print(f"Reformatted docs/practice_ch05.md with {len(formatted_blocks)} blocks.")
