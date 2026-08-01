import re
import os

header_part = """<!-- tabs:start -->
#### **Tiếng Việt**

# Chương 7: Phân tích: Khám phá Dữ liệu (Analysis: Data Exploration)
"""

footer_part = """
#### **English**
<iframe src="TaiLieu/textbookForPractice/Ch_07_Analysis_Data%20Exploration.pdf" width="100%" height="800px"></iframe>
<!-- tabs:end -->
"""

all_lines = []
for i in range(1, 13):  # 12 chunks
    chunk_file = f"scratch/ch07_tr_chunk_{i}.md"
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
    if re.match(r'^7-\d+.*$', s) or re.match(r'^\d+-7.*$', s):
        continue
    if s in ['C H A PT E R 7', 'Phân tích: Khám phá', 'Dữ liệu', 'Analysis: Data Exploration', 'Analysis: Data', 'Exploration']:
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
    
    # Custom post-processing for Ch07 formatting
    text_para = re.sub(r'C H A P T ÉP 7.*Xem trước chương\s*', '**Xem trước chương**\n\n', text_para)
    text_para = re.sub(r'Lộ trình chương\s*', '\n\n**Lộ trình chương**\n\n', text_para)
    text_para = re.sub(r'Cái nhìn sâu sắc chuyên nghiệp:', '\n\n**Cái nhìn sâu sắc chuyên nghiệp:**', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ➊', '\n\n**MỤC TIÊU HỌC TẬP ➊**\n\n', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ❷', '\n\n**MỤC TIÊU HỌC TẬP ❷**\n\n', text_para)
    text_para = re.sub(r'MỤC TIÊU HỌC TẬP ❸', '\n\n**MỤC TIÊU HỌC TẬP ❸**\n\n', text_para)
    text_para = re.sub(r'7\.1 Khám phá dữ liệu là gì\?', '\n\n## 7.1 Khám phá dữ liệu là gì?\n\n', text_para)
    text_para = re.sub(r'7\.2 Khám phá dữ liệu.*', '\n\n## 7.2 Khám phá các mối quan hệ dữ liệu cơ bản thông qua trực quan hóa\n\n', text_para)
    text_para = re.sub(r'7\.3 Khám phá dữ liệu bằng cách.*', '\n\n## 7.3 Khám phá dữ liệu bằng cách tích hợp các mối quan hệ cơ bản\n\n', text_para)
    text_para = re.sub(r'\) LO 7\.1', ')\n\n**LO 7.1** ', text_para)
    text_para = re.sub(r'\) LO 7\.2', ')\n\n**LO 7.2** ', text_para)
    text_para = re.sub(r'\) LO 7\.3', ')\n\n**LO 7.3** ', text_para)
    text_para = re.sub(r'Wiley\.\s+## 7\.1', 'Wiley.\n\n## 7.1', text_para)
    
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

    # Identify images (e.g., ![ILLUSTRATION 7.1](...))
    if s.startswith('![') and ']' in s and '(' in s and ')' in s:
        flush_para()
        formatted_blocks.append(s)
        i += 1
        continue

    # Major Sections
    m = re.match(r'^(7\.[1-9])\s*(.*)', s)
    if m and not s.lower().startswith('7.x'):
        flush_para()
        formatted_blocks.append(f"## {s}")
        i += 1
        continue

    # Subsections like LO 7.x
    if re.match(r'^LO\s*7\.\d+.*', s, re.IGNORECASE):
        flush_para()
        formatted_blocks.append(f"**{s}**")
        i += 1
        continue

    # Captions and Exercises
    if re.match(r'^(MINH HỌA|BE|EX|PR|PAC|FIG|Apply It)\s*7\.\d+.*', s, re.IGNORECASE):
        flush_para()
        # Collect full exercise text if it's long
        ex_text = s
        i += 1
        while i < len(cleaned_lines) and cleaned_lines[i] and not re.match(r'^(MINH HỌA|BE|EX|PR|PAC|FIG|Apply It)\s*7\.\d+.*', cleaned_lines[i], re.IGNORECASE):
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

# Second pass: Image injection
def inject_images(text):
    import os
    img_dir = "TaiLieu/textbookForPractice/Figures/Ch_07"
    if not os.path.exists(img_dir):
        return text
        
    images = os.listdir(img_dir)
    images.sort(key=len, reverse=True) # Sort to match longer names first
    
    for img in images:
        if not img.endswith('.png'): continue
        name_no_ext = img[:-4]
        # Look for the bold tag containing this name
        pattern = r'\*\*(MINH HỌA|EX|BE|Apply It)\s*' + re.escape(name_no_ext.split(' ')[-1] if len(name_no_ext.split(' ')) > 1 else name_no_ext) + r'(.*?)\*\*'
        # It's tricky to inject precisely if the translation changes the name. Let's just do a simple replacement if the exact name appears.
        # Often the translation keeps 'EX 7.3' intact.
    return text

# We will let the update script handle the images better later, or just do it here if possible. 
# Actually, the user's `update_practice_images.py` usually handles image injection. I will write a script for it.

with open('docs/practice_ch07.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_md))

print(f"Assembled docs/practice_ch07.md with {len(formatted_blocks)} blocks.")
