import os
import shutil
import urllib.request

output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images\Day_04_TH"
os.makedirs(output_dir, exist_ok=True)

# Copy the generated image
src_bg = r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\ai_accountant_robot_1785262349528.png"
if os.path.exists(src_bg):
    shutil.copy(src_bg, os.path.join(output_dir, "bg_day4_th.png"))

# Download dummy images for placeholders
logos = {
    "chatgpt_persona.png": "https://dummyimage.com/600x400/000080/ffffff.png&text=ChatGPT+Persona+Prompt",
    "cost_allocation.png": "https://dummyimage.com/600x400/107c41/ffffff.png&text=Cost+Allocation+Table",
    "email_drafting.png": "https://dummyimage.com/600x400/800000/ffffff.png&text=AI+Email+Drafting",
    "anomaly_detection.png": "https://dummyimage.com/600x400/333333/ffffff.png&text=Anomaly+Detection+(Red+Flag)"
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
