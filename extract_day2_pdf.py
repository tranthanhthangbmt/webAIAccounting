import fitz
import os

pdf_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2\Day_02_Data and Analytics in Accounting - Chapter 2_Foundational Data Analysis Skills.pdf"

if os.path.exists(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    
    with open(r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\scratch\day2_lt_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully extracted Day 2 LT PDF.")
else:
    print(f"File not found: {pdf_path}")
