import os

def read_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def main():
    # Read English chunks
    en_content = ""
    en_content += read_file("chunk6A_1.txt") + "\n\n"
    en_content += read_file("chunk6B_1.txt") + "\n\n"

    # Read Vietnamese chunks
    vi_content = ""
    vi_content += read_file("chunk6A_1_vi.txt") + "\n\n"
    vi_content += read_file("chunk6B_1_vi.txt") + "\n\n"

    # Escape backticks and backslashes for JS string literal
    en_content_js = en_content.replace('\\', '\\\\').replace('`', '\\`')
    vi_content_js = vi_content.replace('\\', '\\\\').replace('`', '\\`')

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tài liệu Buổi 6 - AI Accounting</title>
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
    <h1 style="text-align: center; color: #333;">Tài liệu Buổi 6: AI trong tài chính công và quốc tế</h1>
    
    <div class="tab-container">
        <button class="tab active" onclick="openTab('en-tab', this)">English (Bản gốc)</button>
        <button class="tab" onclick="openTab('vi-tab', this)">Tiếng Việt (Bản dịch)</button>
    </div>

    <div id="en-tab" class="content-area active"></div>
    <div id="vi-tab" class="content-area"></div>
</div>

<script>
    // Raw Markdown contents
    const enMarkdown = `{en_content_js}`;
    const viMarkdown = `{vi_content_js}`;

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
</html>"""

    with open('Buoi_06.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Successfully created Buoi_06.html")

if __name__ == "__main__":
    main()
