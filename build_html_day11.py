import os
import glob
import markdown

def read_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def build_html():
    # Gather chunks
    chunks_en = sorted(glob.glob(r"chunk11A_*.txt"))
    chunks_en = [c for c in chunks_en if not c.endswith('_vi.txt')]
    
    en_text = ""
    vi_text = ""
    
    # Custom sorting function for filenames like chunk11A_10.txt
    def get_chunk_num(filename):
        try:
            return int(filename.split('_')[-1].split('.')[0])
        except:
            return 0
            
    chunks_en.sort(key=get_chunk_num)
    
    for c in chunks_en:
        en_text += read_file(c) + "\n\n"
        vi_text += read_file(c.replace(".txt", "_vi.txt")) + "\n\n"

    # Convert to Markdown
    en_html = markdown.markdown(en_text, extensions=['fenced_code', 'tables'])
    vi_html = markdown.markdown(vi_text, extensions=['fenced_code', 'tables'])
    
    # HTML template with tabs
    template = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buổi 11 - Thực hành Nền tảng Dữ liệu Kế toán</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f9;
        }}
        h1, h2, h3 {{
            color: #333;
        }}
        .tab {{
            overflow: hidden;
            border: 1px solid #ccc;
            background-color: #f1f1f1;
            margin-bottom: 20px;
        }}
        .tab button {{
            background-color: inherit;
            float: left;
            border: none;
            outline: none;
            cursor: pointer;
            padding: 14px 16px;
            transition: 0.3s;
            font-size: 17px;
        }}
        .tab button:hover {{
            background-color: #ddd;
        }}
        .tab button.active {{
            background-color: #ccc;
        }}
        .tabcontent {{
            display: none;
            padding: 20px;
            border: 1px solid #ccc;
            border-top: none;
            background-color: white;
        }}
        .placeholder {{
            background-color: #e2e3e5;
            padding: 10px;
            border: 1px dashed #6c757d;
            text-align: center;
            margin: 10px 0;
            color: #6c757d;
            font-weight: bold;
        }}
    </style>
</head>
<body>

    <h1>Buổi 11: Thực hành Nền tảng Dữ liệu Kế toán</h1>

    <div class="tab">
        <button class="tablinks active" onclick="openTab(event, 'Vietnamese')">Tiếng Việt</button>
        <button class="tablinks" onclick="openTab(event, 'English')">English</button>
    </div>

    <div id="Vietnamese" class="tabcontent" style="display:block;">
        {vi_html.replace('<!-- IMAGE_PLACEHOLDER: ', '<div class="placeholder">📸 Image: ').replace(' -->', '</div>')}
    </div>

    <div id="English" class="tabcontent">
        {en_html.replace('<!-- IMAGE_PLACEHOLDER: ', '<div class="placeholder">📸 Image: ').replace(' -->', '</div>')}
    </div>

    <script>
        function openTab(evt, tabName) {{
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {{
                tabcontent[i].style.display = "none";
            }}
            tablinks = document.getElementsByClassName("tablinks");
            for (i = 0; i < tablinks.length; i++) {{
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }}
            document.getElementById(tabName).style.display = "block";
            evt.currentTarget.className += " active";
        }}
    </script>

</body>
</html>
"""

    with open("Buoi_11.html", "w", encoding="utf-8") as f:
        f.write(template)
        
    print("Buoi_11.html generated successfully!")

if __name__ == "__main__":
    build_html()
