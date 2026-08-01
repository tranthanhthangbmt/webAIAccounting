import re

with open('docs/practice_ch05.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
new_lines = []

for line in lines:
    # Remove page numbers at the end of headers (e.g. ## 5.1 Lập hồ sơ... 5-3)
    line = re.sub(r' \s*5-\d+$', '', line)
    line = re.sub(r'\s+5-\d+$', '', line)
    
    # Remove "Chương Lộ trình 5-1" if it starts a paragraph
    if line.startswith('Chương Lộ trình 5-'):
        line = re.sub(r'^Chương Lộ trình 5-\d+\s*', '', line)
        
    # Remove random 5-x page numbers
    line = re.sub(r'\b5-\d+\b', '', line)

    # Clean up "Cái nhìn sâu sắc chuyên nghiệp:" -> make it bold
    if line.startswith('Cái nhìn sâu sắc chuyên nghiệp:'):
        line = '**' + line[:31] + '**' + line[31:]
        
    # Clean up "MỤC TIÊU HỌC TẬP" list if it got split awkwardly
    if line == 'hồ sơ dữ liệu.':
        if len(new_lines) > 0 and 'Giải thích quy trình' in new_lines[-1]:
            new_lines[-1] = new_lines[-1] + ' ' + line
            continue

    new_lines.append(line)

with open('docs/practice_ch05.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Final cleanup applied.")
