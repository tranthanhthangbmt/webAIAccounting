import fitz  # PyMuPDF
import os

pdf_path = r'TaiLieu\textbookForPractice\Ch_05_Analysis_ Data Preparation.pdf'
out_path = r'scratch\ch05_raw.txt'

if not os.path.exists(pdf_path):
    print(f"File not found: {pdf_path}")
else:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += f"--- PAGE {page.number + 1} ---\n"
        text += page.get_text()

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Extracted {len(doc)} pages to {out_path}")
