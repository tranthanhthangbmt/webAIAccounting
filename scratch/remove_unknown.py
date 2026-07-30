import os
import glob
import sys

def remove_unknown(target_dir):
    files = glob.glob(os.path.join(target_dir, "Unknown_*"))
    if not files:
        print("No files starting with 'Unknown_' found.")
        return
        
    for f in files:
        base = os.path.basename(f)
        new_base = base.replace("Unknown_", "", 1)
        new_f = os.path.join(target_dir, new_base)
        
        # Handle duplicates safely
        name, ext = os.path.splitext(new_base)
        counter = 1
        while os.path.exists(new_f):
            new_f = os.path.join(target_dir, f"{name}_{counter}{ext}")
            counter += 1
            
        try:
            os.rename(f, new_f)
            print(f"Renamed: {base} -> {os.path.basename(new_f)}")
        except Exception as e:
            print(f"Failed to rename {base}: {e}")

if __name__ == "__main__":
    d = r"TaiLieu\textbookForPractice\Figures\Ch_02"
    remove_unknown(d)
