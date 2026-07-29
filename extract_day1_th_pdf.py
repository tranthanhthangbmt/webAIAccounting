import fitz

pdf_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\textbook_Chapters_v2\Day_01_TH_ChatGPT and AI for Accountants - Chapter 1_Generative Artificial Intelligence (GAI) in Accounting (Phần hướng dẫn cơ bản về Prompt).pdf"
output_path = r"C:\Users\thanh\.gemini\antigravity-ide\brain\7344b980-59cf-4269-9c32-fbe7e2e661c0\scratch\day1_th_text.txt"

text = ""
try:
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text() + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Extracted successfully.")
except Exception as e:
    print(f"Error: {e}")
