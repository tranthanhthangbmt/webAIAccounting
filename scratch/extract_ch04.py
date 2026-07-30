import fitz  # PyMuPDF

pdf_path = r'TaiLieu\textbookForPractice\Ch_04_Planning Data and.pdf'
out_path = r'scratch\ch04_raw.txt'

doc = fitz.open(pdf_path)
text = ""
for page in doc:
    text += f"--- PAGE {page.number + 1} ---\n"
    text += page.get_text()

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(text)
