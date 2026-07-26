import os
import glob
import zipfile
import shutil

textbook_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook"
figures_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\Figures"

if not os.path.exists(figures_dir):
    os.makedirs(figures_dir)

docx_files = glob.glob(os.path.join(textbook_dir, "*.docx"))

for docx_path in docx_files:
    filename = os.path.basename(docx_path)
    # Extract the Buoi prefix, e.g., "Buoi_01", "Buoi_02A", "Buoi_9B"
    prefix = filename.split('_')[0]
    # Sometimes it's Buoi_01, so we also get the second part if the first is "Buoi"
    parts = filename.split('_')
    if len(parts) >= 2 and parts[0] == "Buoi":
        prefix = "Buoi_" + parts[1]
    
    out_dir = os.path.join(figures_dir, prefix)
    
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        # Find all files in word/media/
        media_files = [f for f in zip_ref.namelist() if f.startswith("word/media/")]
        if not media_files:
            continue
            
        print(f"Extracting {len(media_files)} images from {filename} to {prefix}/")
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
            
        for mf in media_files:
            # Get the image name
            img_name = os.path.basename(mf)
            if not img_name:
                continue
                
            out_path = os.path.join(out_dir, img_name)
            
            # Read from zip and write to file
            with zip_ref.open(mf) as source, open(out_path, "wb") as target:
                shutil.copyfileobj(source, target)

print("Done extracting images!")
