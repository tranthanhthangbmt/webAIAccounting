import os
import shutil
import urllib.request

output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images\Day_01_TH"
os.makedirs(output_dir, exist_ok=True)

# Copy the generated image
src_bg = r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\ai_accounting_background_1785259781999.png"
if os.path.exists(src_bg):
    shutil.copy(src_bg, os.path.join(output_dir, "bg_tech.png"))

# Download dummy images for logos
logos = {
    "chatgpt_logo.png": "https://dummyimage.com/400x400/10a37f/ffffff.png&text=ChatGPT",
    "quickbooks_logo.png": "https://dummyimage.com/400x400/2ca01c/ffffff.png&text=QuickBooks",
    "xero_logo.png": "https://dummyimage.com/400x400/13b5ea/ffffff.png&text=Xero",
    "tableau_logo.png": "https://dummyimage.com/400x400/e97627/ffffff.png&text=Tableau",
    "aws_logo.png": "https://dummyimage.com/400x400/ff9900/ffffff.png&text=AWS",
    "ibm_watson_logo.png": "https://dummyimage.com/400x400/0f62fe/ffffff.png&text=IBM+Watson",
    "error_reduction.png": "https://dummyimage.com/600x400/ff3333/ffffff.png&text=Error+Reduction+Chart",
    "cafe_ai.png": "https://dummyimage.com/600x400/8b4513/ffffff.png&text=Cafe+AI+Case+Study",
    "architecture_ai.png": "https://dummyimage.com/600x400/808080/ffffff.png&text=Architecture+Firm+AI",
    "global_ai.png": "https://dummyimage.com/600x400/000080/ffffff.png&text=GlobalTech+Enterprise",
    "puzzle_skills.png": "https://dummyimage.com/600x400/008080/ffffff.png&text=5+Core+Skills+Puzzle",
    "prompt_screenshot.png": "https://dummyimage.com/800x400/333333/ffffff.png&text=ChatGPT+Prompt+Screenshot"
}

for name, url in logos.items():
    try:
        path = os.path.join(output_dir, name)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
