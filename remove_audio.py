import os
import re

directory = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs"

# Pattern to match the audio block
# We use re.DOTALL to match across newlines
pattern = re.compile(r'<div style="margin: 20px 0; padding: 15px; background-color: #f8f9fa; border-left: 4px solid #0056b3; border-radius: 4px;">\s*<h4 style="margin-top: 0;">🎧 Nghe Bài Giảng \(Audio\)</h4>\s*<audio controls style="width: 100%;">\s*<source src="audio/[^"]+" type="audio/mp4">\s*Trình duyệt của bạn không hỗ trợ thẻ audio.\s*</audio>\s*</div>\n*', re.DOTALL)

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub('', content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
