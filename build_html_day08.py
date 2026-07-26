import os

dir_path = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting'

# Load English chunks
en_content = ""
for i in range(1, 6):
    try:
        with open(os.path.join(dir_path, f'chunk8A_{i}.txt'), 'r', encoding='utf-8') as f:
            en_content += f.read() + "\n\n"
    except FileNotFoundError:
        pass

for i in range(1, 3):
    try:
        with open(os.path.join(dir_path, f'chunk8B_{i}.txt'), 'r', encoding='utf-8') as f:
            en_content += f.read() + "\n\n"
    except FileNotFoundError:
        pass

# Load Vietnamese chunks
vi_content = ""
for i in range(1, 6):
    try:
        with open(os.path.join(dir_path, f'chunk8A_{i}_vi.txt'), 'r', encoding='utf-8') as f:
            vi_content += f.read() + "\n\n"
    except FileNotFoundError:
        pass

for i in range(1, 3):
    try:
        with open(os.path.join(dir_path, f'chunk8B_{i}_vi.txt'), 'r', encoding='utf-8') as f:
            vi_content += f.read() + "\n\n"
    except FileNotFoundError:
        pass

# Escape backticks and backslashes for JS template literal
en_content = en_content.replace('\\', '\\\\').replace('`', '\\`')
vi_content = vi_content.replace('\\', '\\\\').replace('`', '\\`')

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tài liệu Buổi 8 - AI Accounting</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }}
        .container {{
            max-width: 1000px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        .tab-container {{
            display: flex;
            margin-bottom: 20px;
            border-bottom: 2px solid #ccc;
        }}
        .tab {{
            padding: 10px 20px;
            cursor: pointer;
            border: none;
            background: none;
            font-size: 16px;
            font-weight: bold;
            color: #555;
            outline: none;
        }}
        .tab:hover {{
            color: #000;
        }}
        .tab.active {{
            color: #007bff;
            border-bottom: 2px solid #007bff;
            margin-bottom: -2px;
        }}
        .content-area {{
            display: none;
        }}
        .content-area.active {{
            display: block;
        }}
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 15px 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        table, th, td {{
            border: 1px solid #ccc;
        }}
        th, td {{
            padding: 10px;
            text-align: left;
        }}
        th {{
            background-color: #f9f9f9;
        }}
    </style>
</head>
<body>

<div class="container">
    <h1 style="text-align: center; color: #333;">Tài liệu Buổi 8: Credit Scoring & AI Algorithmic Trading</h1>
    
    <div class="tab-container">
        <button class="tab active" onclick="openTab('en-tab', this)">English (Bản gốc)</button>
        <button class="tab" onclick="openTab('vi-tab', this)">Tiếng Việt (Bản dịch)</button>
    </div>

    <div id="en-tab" class="content-area active"></div>
    <div id="vi-tab" class="content-area"></div>
</div>

<script>
    // Raw Markdown contents
    const enMarkdown = `{en_content}`;
    const viMarkdown = `{vi_content}`;

    // Render Markdown to HTML
    document.getElementById('en-tab').innerHTML = marked.parse(enMarkdown);
    document.getElementById('vi-tab').innerHTML = marked.parse(viMarkdown);

    // Tab switching logic
    function openTab(tabId, element) {{
        const contents = document.querySelectorAll('.content-area');
        contents.forEach(content => content.classList.remove('active'));

        const tabs = document.querySelectorAll('.tab');
        tabs.forEach(tab => tab.classList.remove('active'));

        document.getElementById(tabId).classList.add('active');
        element.classList.add('active');
    }}
</script>

</body>
</html>
"""

with open(os.path.join(dir_path, 'Buoi_08.html'), 'w', encoding='utf-8') as f:
    f.write(html_template)
print("Successfully created Buoi_08.html")
