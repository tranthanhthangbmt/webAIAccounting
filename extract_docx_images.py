import os
import zipfile

docx_files = [
    r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2\Day_01_Accounting Information Systems - Chapter 1_Accounting Information Systems_An Overview.docx",
    r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2\Day_01_Artificial Intelligence in Accounting_Practical Applications - Chapter 1_What Accountants Need to Know.docx"
]

output_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slideAIAcc_v2\images\Day_01"
os.makedirs(output_dir, exist_ok=True)

img_count = 1
for docx in docx_files:
    if os.path.exists(docx):
        with zipfile.ZipFile(docx, 'r') as archive:
            for item in archive.namelist():
                if item.startswith('word/media/'):
                    archive.extract(item, output_dir)
                    # rename extracted file for simplicity
                    old_path = os.path.join(output_dir, item)
                    ext = os.path.splitext(item)[1]
                    new_path = os.path.join(output_dir, f"img_{img_count}{ext}")
                    os.rename(old_path, new_path)
                    img_count += 1

print(f"Extracted {img_count - 1} images to {output_dir}")
