import os
import csv
import sys
import shutil

def rename_files(target_dir):
    csv_path = os.path.join(target_dir, "rename_mapping.csv")
    if not os.path.exists(csv_path):
        print(f"Mapping file not found: {csv_path}")
        print("Please run extract_figure_names.py first.")
        return
        
    success_count = 0
    error_count = 0
    
    # Track used names to prevent overwriting
    used_names = set()
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            original = row.get("Original_File")
            proposed = row.get("Proposed_Filename")
            
            if not original or not proposed:
                continue
                
            orig_path = os.path.join(target_dir, original)
            if not os.path.exists(orig_path):
                print(f"File not found: {original}, skipping.")
                error_count += 1
                continue
                
            # Handle duplicates
            base_name, ext = os.path.splitext(proposed)
            new_name = proposed
            counter = 1
            while new_name.lower() in used_names or os.path.exists(os.path.join(target_dir, new_name)):
                if new_name == original:
                    break # Same file, no need to deduplicate against itself
                new_name = f"{base_name}_{counter}{ext}"
                counter += 1
                
            used_names.add(new_name.lower())
            
            if new_name == original:
                print(f"Keeping original name: {original}")
                continue
                
            new_path = os.path.join(target_dir, new_name)
            
            try:
                os.rename(orig_path, new_path)
                print(f"Renamed: {original} -> {new_name}")
                success_count += 1
            except Exception as e:
                print(f"Failed to rename {original}: {e}")
                error_count += 1
                
    print(f"\nDone! Renamed {success_count} files. Errors: {error_count}")

if __name__ == "__main__":
    # Default to Ch_01 if no argument provided
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "TaiLieu", "textbookForPractice", "Figures")
    target = os.path.join(base_dir, "Ch_01")
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
        
    if os.path.exists(target):
        rename_files(target)
    else:
        print(f"Directory not found: {target}")
