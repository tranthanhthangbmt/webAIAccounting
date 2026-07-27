import os

directory1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs"
directory2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting"

def replace_in_files(dir_path, ext):
    for filename in os.listdir(dir_path):
        if filename.endswith(ext):
            filepath = os.path.join(dir_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace('Tiếng Anh (Bản gốc PDF)', 'Tiếng Anh')
            new_content = new_content.replace('Tiếng Việt (Bản dịch)', 'Tiếng Việt')
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")

replace_in_files(directory1, ".md")
replace_in_files(directory2, ".html")
