import re, json
import codecs

with open('Buoi_01.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the start of the string: `const viMarkdown = "`
# And the end of the script tag, then parse it safely.
start_idx = content.find('const viMarkdown = "')
if start_idx != -1:
    # Start right at the opening quote
    str_content = content[start_idx + 19:]
    # Find the closing quote that is followed by a semicolon and possibly whitespace/script tag
    end_idx = str_content.rfind('";')
    if end_idx != -1:
        valid_json_str = str_content[:end_idx+1]
        try:
            vi_markdown = json.loads(valid_json_str)
            print('Extracted successfully, length:', len(vi_markdown))
            print('Contains Figure 1.2?', 'Figure 1.2' in vi_markdown)
            
            with codecs.open('docs/buoi_01.md', 'w', encoding='utf-8') as f:
                template = """# Buổi 1: What Accountants Need to Know\n\n<!-- tabs:start -->\n\n#### ** 🇬🇧 Tiếng Anh (Bản gốc PDF) **\n\n> Trình duyệt của bạn sẽ hiển thị nội dung PDF gốc ở dưới đây.\n\n<object data="pdfs/Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf" type="application/pdf" class="pdf-container">\n    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="pdfs/Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf" target="_blank">Nhấn vào đây để tải tài liệu PDF</a>.</p>\n</object>\n\n#### ** 🇻🇳 Tiếng Việt (Bản dịch) **\n\n"""
                f.write(template)
                f.write(vi_markdown)
                f.write("\n\n<!-- tabs:end -->\n")
                
            print("Updated docs/buoi_01.md")
        except Exception as e:
            print('JSON Error:', e)
            print('Ends with:', valid_json_str[-50:])
    else:
        print('Could not find end of string')
else:
    print('Could not find start of string')
