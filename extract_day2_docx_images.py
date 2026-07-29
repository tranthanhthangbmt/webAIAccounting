import os
import zipfile

docx_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2\Day_02_Data and Analytics in Accounting - Chapter 2_Foundational Data Analysis Skills.docx"

output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images\Day_02"
os.makedirs(output_dir, exist_ok=True)

img_count = 1
if os.path.exists(docx_path):
    with zipfile.ZipFile(docx_path, 'r') as archive:
        for item in archive.namelist():
            if item.startswith('word/media/'):
                archive.extract(item, output_dir)
                old_path = os.path.join(output_dir, item)
                ext = os.path.splitext(item)[1]
                new_path = os.path.join(output_dir, f"img_lt_{img_count}{ext}")
                os.rename(old_path, new_path)
                img_count += 1
print(f"Extracted {img_count - 1} images to {output_dir}")
