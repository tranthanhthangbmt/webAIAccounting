import os
import glob
import subprocess
import re

directory = "TaiLieu/slideAIAcc_v2"
md_files = glob.glob(os.path.join(directory, "*.md"))

# Filter to Days 02-09
target_files = []
for f in md_files:
    basename = os.path.basename(f)
    if re.search(r'Day0?[23456789]_(LT|TH)\.md', basename, re.IGNORECASE):
        target_files.append(f)

for md_file in target_files:
    basename = os.path.basename(md_file)
    tex_basename = basename.replace('slideAIAcc_v2_', 'Slide_AIAcc_v2_').replace('.md', '.tex')
    tex_basename = re.sub(r'Day(\d)_', r'Day0\1_', tex_basename)
    
    tex_file = os.path.join(directory, tex_basename)
    
    print(f"Converting {md_file} to {tex_file}...")
    subprocess.run(["python", "scratch/md2tex_v2.py", md_file, tex_file], check=True)
    
    print(f"Compiling {tex_file}...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_basename], cwd=directory)
    subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_basename], cwd=directory)
