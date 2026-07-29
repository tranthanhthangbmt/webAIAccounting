import fitz
import os

pdf_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2\Day_05_Business Analytics_Solving Business Problems - Chapter 11_Forensic Accounting Using Outlier Detection.pdf"

all_text = ""
if os.path.exists(pdf_path):
    with fitz.open(pdf_path) as doc:
        for page in doc:
            all_text += page.get_text()
else:
    all_text += "FILE NOT FOUND"

out_path = r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\scratch\day5_lt_text.txt"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"Successfully extracted text to {out_path}")
