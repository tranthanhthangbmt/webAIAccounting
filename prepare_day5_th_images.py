import os
import urllib.request
import json

base_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images\Day_05"
os.makedirs(base_dir, exist_ok=True)

images_to_download = {
    "bg_day5_th.png": "https://placehold.co/1920x1080/2ecc71/ffffff.png?text=Day+05+TH:+Excel+and+AI+for+Anomaly+Detection",
    "excel_conditional_formatting.png": "https://placehold.co/800x600/3498db/ffffff.png?text=Excel+Conditional+Formatting",
    "chatgpt_excel_prompt.png": "https://placehold.co/800x600/9b59b6/ffffff.png?text=ChatGPT+Prompt+for+Excel",
    "excel_analyze_data.png": "https://placehold.co/800x600/e67e22/ffffff.png?text=Excel+Analyze+Data+Feature",
    "red_flags_table.png": "https://placehold.co/800x600/e74c3c/ffffff.png?text=Red+Flags+Table+Report"
}

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
urllib.request.install_opener(opener)

for filename, url in images_to_download.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        try:
            urllib.request.urlretrieve(url, filepath)
            print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
