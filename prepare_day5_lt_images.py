import os
import shutil
import urllib.request

output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images\Day_05"
os.makedirs(output_dir, exist_ok=True)

# Copy the generated image
src_bg = r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\forensic_ai_background_1785286903067.png"
if os.path.exists(src_bg):
    shutil.copy(src_bg, os.path.join(output_dir, "bg_day5_lt.png"))

# Download dummy images for placeholders
logos = {
    "fraud_stats.png": "https://dummyimage.com/600x400/800000/ffffff.png&text=Fraud+Statistics+Chart",
    "outlier_vs_noise.png": "https://dummyimage.com/600x400/333333/ffffff.png&text=Outlier+vs+Noise+Graph",
    "global_vs_local.png": "https://dummyimage.com/600x400/107c41/ffffff.png&text=Global+vs+Local+Outliers",
    "lof_intuition.png": "https://dummyimage.com/600x400/000080/ffffff.png&text=LOF+Cabin+in+Valley+Example",
    "smurfing_diagram.png": "https://dummyimage.com/600x400/b30000/ffffff.png&text=Smurfing+Transactions+Diagram"
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
