import fitz
import os

pdf_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2"
pdfs = [
    "Day_01_Accounting Information Systems - Chapter 1_Accounting Information Systems_An Overview.pdf",
    "Day_01_Artificial Intelligence in Accounting_Practical Applications - Chapter 1_What Accountants Need to Know.pdf",
    "Day_01_ChatGPT and AI for Accountants - Chapter 15_The Future is Now – Integrating AI into Accounting.pdf"
]

out_file = r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\scratch\day1_text.txt"

# Ensure directory exists
os.makedirs(os.path.dirname(out_file), exist_ok=True)

with open(out_file, "w", encoding="utf-8") as f:
    for pdf_name in pdfs:
        full_path = os.path.join(pdf_dir, pdf_name)
        f.write(f"\n{'='*50}\n--- CONTENT FROM: {pdf_name} ---\n{'='*50}\n\n")
        try:
            doc = fitz.open(full_path)
            for page in doc:
                f.write(page.get_text())
                f.write("\n")
        except Exception as e:
            f.write(f"Error reading {pdf_name}: {e}\n")
