import re

filepath = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the Google Docs Viewer block with the native object block
pattern = r'// Create Google Docs Viewer Iframe.*?obj\.parentNode\.replaceChild\(wrapper, obj\);'

replacement = """// Keep native object but move it inside wrapper
                  let newObj = obj.cloneNode(true);
                  newObj.style.width = '100%';
                  newObj.style.height = '85vh';
                  wrapper.appendChild(newObj);
                  
                  obj.parentNode.replaceChild(wrapper, obj);"""

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html to remove buggy Google Docs Viewer and keep the Mở Đọc button")
