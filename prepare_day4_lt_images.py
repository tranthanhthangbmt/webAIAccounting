import os
import shutil
import urllib.request

output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images\Day_04"
os.makedirs(output_dir, exist_ok=True)

# Copy the generated image
src_bg = r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\ai_bookkeeping_brain_1785262025039.png"
if os.path.exists(src_bg):
    shutil.copy(src_bg, os.path.join(output_dir, "bg_day4.png"))

# Download dummy images for placeholders
logos = {
    "accounting_cycle.png": "https://dummyimage.com/600x400/333333/ffffff.png&text=The+Accounting+Cycle",
    "journal_entry.png": "https://dummyimage.com/600x400/000080/ffffff.png&text=AI+Journal+Entry",
    "bank_recon.png": "https://dummyimage.com/600x400/107c41/ffffff.png&text=Bank+Reconciliation",
    "fraud_triangle.png": "https://dummyimage.com/600x400/800000/ffffff.png&text=The+Fraud+Triangle",
    "internal_controls.png": "https://dummyimage.com/600x400/000000/ffffff.png&text=Internal+Controls"
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
