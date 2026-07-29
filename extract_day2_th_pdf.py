import fitz
import os

pdfs = [
    r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2\Day_02_TH_Blog_Power-Query.pdf",
    r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2\Day_02_TH_Data and Analytics in Accounting - Apply It 2.1 & 2.2 (Các bài tập thực hành thao tác dữ liệu cơ bản).pdf",
    r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2\Day_02_TH_Power Query M Language.pdf"
]

all_text = ""
for pdf_path in pdfs:
    if os.path.exists(pdf_path):
        all_text += f"\n\n--- CONTENT FROM {os.path.basename(pdf_path)} ---\n\n"
        with fitz.open(pdf_path) as doc:
            for page in doc:
                all_text += page.get_text()
    else:
        print(f"File not found: {pdf_path}")

out_path = r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\scratch\day2_th_text.txt"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"Successfully extracted text to {out_path}")
