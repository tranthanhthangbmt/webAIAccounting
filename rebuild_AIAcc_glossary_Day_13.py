import re
import os

glossary_file = 'depPlan/AIAcc_glossaryDay_13.md'
target_file = 'docs/buoi_13.md'

print(f"Bắt đầu xử lý file: {glossary_file}")

with open(glossary_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Dọn dẹp [cite: ...]
content = re.sub(r'(?:\\\\)*[ \t]*\[cite: \d+\]', '', content)

# 2. Xóa các heading cũ và các dải ***
content = re.sub(r'^###\s+.*$', '', content, flags=re.MULTILINE)
content = re.sub(r'^\*\*\*$', '', content, flags=re.MULTILINE)

# 3. Chuyển đổi các bullet point thành details độc lập (exclusive accordion)
# Format của bullet: *   **Tiêu đề:** Nội dung
parts = re.split(r'^[\*\-]\s+\*\*(.*?)\*\*:?\s*', content, flags=re.MULTILINE)

new_content = parts[0].strip()
if new_content:
    new_content += "\n\n"

for i in range(1, len(parts), 2):
    title = parts[i].strip().rstrip(':')
    body = parts[i+1].strip()
    
    # Khối details sử dụng attribute name="glossary" để tạo exclusive accordion (chỉ mở 1 cái)
    # Và dùng onclick để cuộn mượt mà lên đầu khối đó
    block = f"""<details name="glossary" onclick="setTimeout(() => this.scrollIntoView({{behavior: 'smooth', block: 'start'}}), 150)">
<summary><b style="font-size:1.2em">{title}</b></summary>
<br>

{body}

</details>"""
    new_content += block + "\n\n"

content = new_content

# 4. Xử lý ảnh (đề phòng có ảnh Markdown)
content = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" />\n<span style="display: block; color: #333; font-style: italic; text-align: center; margin-top: 5px; margin-bottom: 15px;"><b>\1</b></span>', content)

# 5. Xử lý toán học KaTeX
content = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', content, flags=re.DOTALL)
content = re.sub(r'\\\((.*?)\\\)', r'$\1$', content, flags=re.DOTALL)

tab_content = f"#### ** 📚 Thuật ngữ & Khái niệm **\n\n{content}\n\n"

print(f"Bắt đầu tiêm vào file: {target_file}")
with open(target_file, 'r', encoding='utf-8') as f:
    target_content = f.read()

# Xóa tab cũ nếu tồn tại
pattern_old_tab = r'#### \*\* 📚 Thuật ngữ & Khái niệm \*\*.*?#### \*\* 🇬🇧 Tiếng Anh \*\*'
if re.search(pattern_old_tab, target_content, flags=re.DOTALL):
    target_content = re.sub(pattern_old_tab, '#### ** 🇬🇧 Tiếng Anh **', target_content, flags=re.DOTALL)
    print("Đã xóa Tab Thuật ngữ cũ.")

# Tiêm tab mới
if '#### ** 🇬🇧 Tiếng Anh **' in target_content:
    target_content = target_content.replace('#### ** 🇬🇧 Tiếng Anh **', tab_content + '#### ** 🇬🇧 Tiếng Anh **')
    print("Đã tiêm Tab Thuật ngữ mới thành công.")
else:
    target_content += '\n' + tab_content
    print("Không tìm thấy Tab Tiếng Anh, đã chèn vào cuối file.")

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(target_content)

print("Hoàn tất!")
