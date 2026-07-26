import codecs
import os

# List of chunks in order
en_chunks = [
    "chunk3A_1.txt", "chunk3A_2.txt",
    "chunk3B_1.txt", "chunk3B_2.txt", "chunk3B_3.txt"
]

vi_chunks = [
    "chunk3A_1_vi.txt", "chunk3A_2_vi.txt",
    "chunk3B_1_vi.txt", "chunk3B_2_vi.txt", "chunk3B_3_vi.txt"
]

# Read English text
en_text = ""
for file in en_chunks:
    try:
        if os.path.exists(file):
            with codecs.open(file, 'r', 'utf-8') as f:
                en_text += f.read() + "\n\n"
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Read Vietnamese text
vi_text = ""
for file in vi_chunks:
    try:
        if os.path.exists(file):
            with codecs.open(file, 'r', 'utf-8') as f:
                vi_text += f.read() + "\n\n"
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Escape backticks and backslashes for JS string literal
en_text_js = en_text.replace('\\', '\\\\').replace('`', '\\`')
vi_text_js = vi_text.replace('\\', '\\\\').replace('`', '\\`')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buổi 3 - Đạo đức, rủi ro của AI & Học máy</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }}
        .tabs {{ display: flex; border-bottom: 2px solid #ccc; margin-bottom: 20px; position: sticky; top: 0; background: white; z-index: 100; padding-top: 10px; }}
        .tab {{ padding: 10px 20px; cursor: pointer; background: #f1f1f1; border: 1px solid #ccc; border-bottom: none; margin-right: 5px; border-radius: 5px 5px 0 0; }}
        .tab.active {{ background: #fff; border-top: 3px solid #007bff; font-weight: bold; }}
        .content {{ display: none; }}
        .content.active {{ display: block; }}
        .en-text {{ white-space: pre-wrap; font-family: 'Courier New', Courier, monospace; background: #f9f9f9; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
        .vi-text {{ margin-top: 20px; }}
        img {{ max-width: 100%; height: auto; display: block; margin: 20px auto; }}
        blockquote {{ border-left: 5px solid #ccc; padding-left: 15px; font-style: italic; color: #555; background: #f9f9f9; padding: 10px; margin: 20px 0; }}
    </style>
</head>
<body>

    <h1>Buổi 3: Đạo đức, rủi ro của AI & Các khái niệm cơ bản (ML, DL)</h1>

    <div class="tabs">
        <div class="tab active" onclick="switchTab('en')">Tiếng Anh</div>
        <div class="tab" onclick="switchTab('vi')">Tiếng Việt</div>
    </div>

    <div id="en-content" class="content active">
        <div class="en-text">{en_text_js}</div>
    </div>

    <div id="vi-content" class="content">
        <div id="vi-markdown" class="vi-text"></div>
    </div>

    <script>
        const viMarkdown = `{vi_text_js}`;
        
        document.getElementById('vi-markdown').innerHTML = marked.parse(viMarkdown);

        function switchTab(lang) {{
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.content').forEach(content => content.classList.remove('active'));

            if (lang === 'en') {{
                document.querySelectorAll('.tab')[0].classList.add('active');
                document.getElementById('en-content').classList.add('active');
            }} else {{
                document.querySelectorAll('.tab')[1].classList.add('active');
                document.getElementById('vi-content').classList.add('active');
            }}
        }}
    </script>

</body>
</html>
"""

with codecs.open("Buoi_03.html", "w", "utf-8") as f:
    f.write(html_content)

print("Generated Buoi_03.html successfully.")
