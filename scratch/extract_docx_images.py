import os
import glob
import zipfile
import re
import shutil

source_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2"
images_base_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images"

def process_docx_files():
    docx_files = glob.glob(os.path.join(source_dir, "Day_*.docx"))
    
    for docx_path in docx_files:
        filename = os.path.basename(docx_path)
        
        # Regex to find Day_XX and optionally _TH
        match = re.search(r"^(Day_\d+(?:-\d+)?)(_TH)?", filename)
        if not match:
            print(f"Skipping {filename}, doesn't match Day_XX pattern.")
            continue
            
        day_part = match.group(1) # e.g., Day_01 or Day_13-15
        th_part = match.group(2) # e.g., _TH or None
        
        # Format the folder name. E.g., Day_01 or Day_01_TH
        folder_name = day_part
        if th_part:
            folder_name += th_part
            
        # Standardize folder name to not have underscore after Day if that's what we want?
        # The user's existing folders are Day_02, Day_02_TH, etc. We'll stick to Day_XX.
        target_dir = os.path.join(images_base_dir, folder_name.replace("Day_", "Day"))
        # Actually existing ones are Day_02, so we keep Day_02
        target_dir = os.path.join(images_base_dir, folder_name)
        
        # In the past the user requested "images/Day09". Let's standardize to DayXX without underscore if it's Day09, 
        # but let's check existing. Existing has Day_02. So Day_XX is fine.
        
        # Check if already processed (e.g. folder exists and has files starting with docx_)
        if os.path.exists(target_dir):
            existing_files = glob.glob(os.path.join(target_dir, "docx_img_*.*"))
            if len(existing_files) > 0:
                print(f"Skipping {filename}, already processed in {target_dir}")
                continue
        else:
            os.makedirs(target_dir, exist_ok=True)
            
        print(f"Processing {filename} -> {target_dir}")
        
        # Extract images
        try:
            with zipfile.ZipFile(docx_path, 'r') as zip_ref:
                media_files = [f for f in zip_ref.namelist() if f.startswith('word/media/')]
                
                if not media_files:
                    print(f"  No images found in {filename}")
                    continue
                    
                for idx, media_file in enumerate(media_files):
                    # extract the file
                    extracted_path = zip_ref.extract(media_file, target_dir)
                    
                    # rename it to a flat structure
                    ext = os.path.splitext(media_file)[1]
                    new_name = f"docx_img_{idx+1}{ext}"
                    new_path = os.path.join(target_dir, new_name)
                    
                    # move and rename
                    if os.path.exists(new_path):
                        os.remove(new_path)
                    shutil.move(extracted_path, new_path)
                    
                # clean up word/media folder
                word_dir = os.path.join(target_dir, 'word')
                if os.path.exists(word_dir):
                    shutil.rmtree(word_dir)
                    
            print(f"  Extracted {len(media_files)} images.")
        except Exception as e:
            print(f"  Error processing {filename}: {e}")

if __name__ == "__main__":
    process_docx_files()
