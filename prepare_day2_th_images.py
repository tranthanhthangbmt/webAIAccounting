import os
import shutil
import urllib.request

output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images\Day_02_TH"
os.makedirs(output_dir, exist_ok=True)

# Copy the generated image
src_bg = r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\power_query_background_1785260797785.png"
if os.path.exists(src_bg):
    shutil.copy(src_bg, os.path.join(output_dir, "bg_pq.png"))

# Download dummy images for placeholders
logos = {
    "get_data.png": "https://dummyimage.com/600x400/107c41/ffffff.png&text=Excel+Get+Data+Button",
    "pq_interface.png": "https://dummyimage.com/600x400/222222/ffffff.png&text=Power+Query+Interface",
    "applied_steps.png": "https://dummyimage.com/600x400/333333/ffffff.png&text=Applied+Steps+Pane",
    "append_queries.png": "https://dummyimage.com/600x400/000080/ffffff.png&text=Append+Queries+Lego",
    "merge_queries.png": "https://dummyimage.com/600x400/800080/ffffff.png&text=Merge+Queries+Lock",
    "super_scooters.png": "https://dummyimage.com/600x400/666666/ffffff.png&text=Super+Scooters+Database"
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
