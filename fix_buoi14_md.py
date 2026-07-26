import re

def main():
    with open('docs/buoi_14.md', 'r', encoding='utf-8') as file:
        content = file.read()

    # Add <!-- tabs:start --> if missing
    if '<!-- tabs:start -->' not in content:
        content = content.replace('#### ** 🇬🇧 Tiếng Anh (Bản gốc PDF) **', '<!-- tabs:start -->\n\n#### ** 🇬🇧 Tiếng Anh (Bản gốc PDF) **')

    # Add the slide tab at the end if missing
    if '🎦 Slide Bài Giảng' not in content:
        slide_tab = '''

#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slideAIAcc/Slide_AIAcc_Day14.pdf" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day14.pdf" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slideAIAcc/Slide_AIAcc_Day14.pdf" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

<!-- tabs:end -->
'''
        content += slide_tab

    with open('docs/buoi_14.md', 'w', encoding='utf-8') as file:
        file.write(content)
    print('Fixed docs/buoi_14.md')

if __name__ == '__main__':
    main()
