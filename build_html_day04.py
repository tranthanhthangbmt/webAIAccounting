import os

def build_html():
    en_content = ""
    for i in range(1, 4):
        try:
            with open(f"chunk4A_{i}.txt", "r", encoding="utf-8") as f:
                en_content += f.read() + "\n\n"
        except FileNotFoundError:
            pass
    for i in range(1, 5):
        try:
            with open(f"chunk4B_{i}.txt", "r", encoding="utf-8") as f:
                en_content += f.read() + "\n\n"
        except FileNotFoundError:
            pass

    vi_content = ""
    for i in range(1, 4):
        try:
            with open(f"chunk4A_{i}_vi.txt", "r", encoding="utf-8") as f:
                vi_content += f.read() + "\n\n"
        except FileNotFoundError:
            pass
    for i in range(1, 5):
        try:
            with open(f"chunk4B_{i}_vi.txt", "r", encoding="utf-8") as f:
                vi_content += f.read() + "\n\n"
        except FileNotFoundError:
            pass

    en_content_escaped = en_content.replace('`', '\\`')
    vi_content_escaped = vi_content.replace('`', '\\`')

    html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buổi 4: Tài liệu song ngữ - Trí tuệ nhân tạo cho Kế toán</title>
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
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        .tabs {{
            display: flex;
            cursor: pointer;
            border-bottom: 1px solid #ccc;
        }}
        .tab {{
            padding: 10px 20px;
            background-color: #e0e0e0;
            border: 1px solid #ccc;
            border-bottom: none;
            margin-right: 5px;
        }}
        .tab.active {{
            background-color: #fff;
            font-weight: bold;
        }}
        .tab-content {{
            display: none;
            padding: 20px 0;
        }}
        .tab-content.active {{
            display: block;
        }}
        h1, h2, h3 {{
            color: #333;
        }}
        pre {{
            background-color: #f8f8f8;
            padding: 10px;
            border: 1px solid #ddd;
            overflow-x: auto;
        }}
        code {{
            font-family: Consolas, monospace;
        }}
        .image-placeholder {{
            background-color: #eee;
            border: 1px dashed #999;
            text-align: center;
            padding: 20px;
            margin: 10px 0;
            color: #666;
        }}
    </style>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
</head>
<body>
    <div class="container">
        <h1>Buổi 4: Tài liệu song ngữ - Trí tuệ nhân tạo cho Kế toán</h1>
        <div class="tabs">
            <div class="tab active" onclick="openTab(event, 'English')">English</div>
            <div class="tab" onclick="openTab(event, 'Vietnamese')">Tiếng Việt</div>
        </div>

        <div id="English" class="tab-content active">
            <div id="en-markdown"></div>
        </div>

        <div id="Vietnamese" class="tab-content">
            <div id="vi-markdown"></div>
        </div>
    </div>

    <script>
        function openTab(evt, tabName) {{
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tab-content");
            for (i = 0; i < tabcontent.length; i++) {{
                tabcontent[i].style.display = "none";
                tabcontent[i].classList.remove("active");
            }}
            tablinks = document.getElementsByClassName("tab");
            for (i = 0; i < tablinks.length; i++) {{
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }}
            document.getElementById(tabName).style.display = "block";
            document.getElementById(tabName).classList.add("active");
            evt.currentTarget.className += " active";
        }}

        // Format placeholders
        const formatPlaceholders = (text) => {{
            return text.replace(/<!-- IMAGE_PLACEHOLDER: (.*?) -->/g, '<div class="image-placeholder">[Hình ảnh: $1 sẽ được chèn vào đây]</div>');
        }};

        // Render Markdown
        const enContent = `{en_content_escaped}`;
        const viContent = `{vi_content_escaped}`;

        document.getElementById('en-markdown').innerHTML = marked.parse(formatPlaceholders(enContent));
        document.getElementById('vi-markdown').innerHTML = marked.parse(formatPlaceholders(viContent));
    </script>
</body>
</html>
"""

    with open("Buoi_04.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Created Buoi_04.html successfully!")

if __name__ == "__main__":
    build_html()
