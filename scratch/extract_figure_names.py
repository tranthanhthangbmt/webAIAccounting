import os
import glob
import re
import csv
import sys

try:
    import easyocr
except ImportError:
    print("Please install easyocr: pip install easyocr")
    sys.exit(1)

def sanitize_filename(name):
    """Remove invalid characters for Windows filenames."""
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r'\s+', " ", name)
    name = name.strip()
    return name

def extract_figure_name(text_list):
    """
    Attempt to find a figure name in the list of OCR text fragments.
    Looks for keywords like Figure, Exhibit, Table.
    """
    full_text = " ".join(text_list)
    match = re.search(r'(Figure|Exhibit|Table|FIGURE|EXHIBIT|TABLE)\s*\d+[\.\-]?\d*\s*[:\-]?\s*([A-Za-z0-9\s]+)', full_text, re.IGNORECASE)
    
    if match:
        extracted = match.group(0)
        if len(extracted) > 60:
            extracted = extracted[:60] + "..."
        return extracted
        
    if text_list:
        fallback = text_list[0]
        if len(fallback) > 30:
            fallback = fallback[:30]
        return f"Unknown_{fallback}"
        
    return "Unknown_Figure"

def process_directory(target_dir):
    print(f"Initializing EasyOCR for English...")
    reader = easyocr.Reader(['en'], gpu=False)
    
    image_files = glob.glob(os.path.join(target_dir, "*.png"))
    image_files.extend(glob.glob(os.path.join(target_dir, "*.jpg")))
    
    if not image_files:
        print(f"No images found in {target_dir}")
        return

    csv_path = os.path.join(target_dir, "rename_mapping.csv")
    results = []
    
    print(f"Found {len(image_files)} images. Starting OCR process...")
    for idx, img_path in enumerate(image_files):
        filename = os.path.basename(img_path)
        
        # Skip files that have already been named (don't start with 'page_')
        if not filename.startswith("page_"):
            print(f"[{idx+1}/{len(image_files)}] Skipping already named file: {filename}")
            continue
            
        print(f"[{idx+1}/{len(image_files)}] Processing {filename}...")
        
        try:
            result = reader.readtext(img_path, detail=0)
            extracted = extract_figure_name(result)
            proposed_name = sanitize_filename(extracted) + os.path.splitext(filename)[1]
            
            results.append({
                "Original_File": filename,
                "Extracted_Text": extracted,
                "Proposed_Filename": proposed_name
            })
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            results.append({
                "Original_File": filename,
                "Extracted_Text": "ERROR",
                "Proposed_Filename": filename
            })

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Original_File", "Extracted_Text", "Proposed_Filename"])
        writer.writeheader()
        writer.writerows(results)
        
    print(f"\nDone! Please review the mapping file at:\n{csv_path}")

if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "TaiLieu", "textbookForPractice", "Figures")
    target = os.path.join(base_dir, "Ch_01")
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
        
    if os.path.exists(target):
        process_directory(target)
    else:
        print(f"Directory not found: {target}")
