import re
import codecs

with open('Buoi_01.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract viMarkdown variable
match = re.search(r'const viMarkdown = (.*?);', content, re.DOTALL)
if match:
    # The string might be wrapped in double quotes
    vi_markdown_str = match.group(1).strip()
    
    # Remove surrounding quotes
    if vi_markdown_str.startswith('"') and vi_markdown_str.endswith('"'):
        vi_markdown_str = vi_markdown_str[1:-1]
    elif vi_markdown_str.startswith('`') and vi_markdown_str.endswith('`'):
        vi_markdown_str = vi_markdown_str[1:-1]
    
    # Unescape unicode and newlines
    # The string inside HTML has \n and \uXXXX
    vi_text = codecs.decode(vi_markdown_str, 'unicode_escape')
    
    pdf_filename = 'Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf'
    
    # Process image placeholders
    vi_text = vi_text.replace('<!-- IMAGE_PLACEHOLDER: ', '> 📸 **Hình ảnh**: ').replace(' -->', '')
    
    md_content = f"""# Buổi 1: What Accountants Need to Know

<!-- tabs:start -->

#### ** 🇬🇧 Tiếng Anh (Bản gốc PDF) **

> Trình duyệt của bạn sẽ hiển thị nội dung PDF gốc ở dưới đây.

<object data="pdfs/{pdf_filename}" type="application/pdf" class="pdf-container">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="pdfs/{pdf_filename}" target="_blank">Nhấn vào đây để tải tài liệu PDF</a>.</p>
</object>

#### ** 🇻🇳 Tiếng Việt (Bản dịch) **

{vi_text}

<!-- tabs:end -->
"""
    with open('docs/buoi_01.md', 'w', encoding='utf-8') as out_f:
        out_f.write(md_content)
    print('Created docs/buoi_01.md successfully!')
else:
    print('Could not find viMarkdown variable in Buoi_01.html')
