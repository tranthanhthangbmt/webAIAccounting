import os
import urllib.request

output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images\Day_01_TH"
os.makedirs(output_dir, exist_ok=True)

images = {
    "chatgpt_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/512px-ChatGPT_logo.svg.png",
    "quickbooks_logo.png": "https://upload.wikimedia.org/wikipedia/en/thumb/2/23/QuickBooks_logo.svg/512px-QuickBooks_logo.svg.png",
    "aws_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/512px-Amazon_Web_Services_Logo.svg.png",
    "ibm_watson_logo.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/IBM_logo.svg/512px-IBM_logo.svg.png",
    "ai_concept.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Artificial_Intelligence_Concept.jpg/640px-Artificial_Intelligence_Concept.jpg",
    "tech_bg.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Node.js_logo.svg/512px-Node.js_logo.svg.png" # simple fallback
}

for name, url in images.items():
    try:
        path = os.path.join(output_dir, name)
        # Using a User-Agent to avoid 403 Forbidden on some wikimedia requests
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
