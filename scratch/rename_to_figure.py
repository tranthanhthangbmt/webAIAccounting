import os
import csv
import re
import sys

def rename_to_figure(target_dir):
    csv_path = os.path.join(target_dir, "rename_mapping.csv")
    if not os.path.exists(csv_path):
        print(f"Mapping file not found: {csv_path}")
        return
        
    success_count = 0
    error_count = 0
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            original = row.get("Original_File")
            extracted = row.get("Extracted_Text")
            
            if not original or not extracted:
                continue
                
            orig_path = os.path.join(target_dir, original)
            if not os.path.exists(orig_path):
                print(f"File not found: {original}, skipping.")
                error_count += 1
                continue
                
            # Find the x.x pattern (e.g., 1.8, 1.10, 1.20)
            match = re.search(r'\d+\.\d+', extracted)
            if match:
                code = match.group(0)
                new_name = f"Figure {code}.png"
                new_path = os.path.join(target_dir, new_name)
                
                # Deduplicate if needed
                counter = 1
                while os.path.exists(new_path) and orig_path != new_path:
                    new_name = f"Figure {code}_{counter}.png"
                    new_path = os.path.join(target_dir, new_name)
                    counter += 1
                    
                try:
                    if orig_path != new_path:
                        os.rename(orig_path, new_path)
                        print(f"Renamed: {original} -> {new_name}")
                        success_count += 1
                except Exception as e:
                    print(f"Failed to rename {original}: {e}")
                    error_count += 1
            else:
                print(f"Could not find code x.x in: '{extracted}' for {original}")
                
    print(f"\nDone! Renamed {success_count} files. Errors: {error_count}")

if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "TaiLieu", "textbookForPractice", "Figures")
    target = os.path.join(base_dir, "Ch_01")
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
        
    if os.path.exists(target):
        rename_to_figure(target)
    else:
        print(f"Directory not found: {target}")
