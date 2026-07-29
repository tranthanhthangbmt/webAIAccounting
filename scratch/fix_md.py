import os
import glob
import re

directory = "TaiLieu/slideAIAcc_v2"
md_files = glob.glob(os.path.join(directory, "*.md"))

def fix_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Convert `## PHẦN...` to `# PHẦN...`
    content = re.sub(r'^##\s+(PHẦN\s+\d+.*)$', r'# \1', content, flags=re.MULTILINE)
    
    # 2. Convert `**SLIDE X: Title**` to `## Title`
    content = re.sub(r'^\*\*SLIDE\s+\d+:\s*(.*?)\*\*$', r'## \1', content, flags=re.MULTILINE)
    
    # 3. Convert `* **Slide X:** Title` to `## Title`
    content = re.sub(r'^\*\s*\*\*Slide\s+\d+:\*\*\s*(.*?)$', r'## \1', content, flags=re.MULTILINE)
    
    # 4. Handle edge cases where they missed SLIDE X and just wrote **Năng lực đạt được sau buổi học:**
    content = re.sub(r'^\*\*Năng lực đạt được sau buổi học:\*\*\s*$', r'## Năng lực đạt được sau buổi học', content, flags=re.MULTILINE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in md_files:
    basename = os.path.basename(filepath)
    print(f"Fixing {basename}...")
    fix_markdown(filepath)
