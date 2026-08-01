import fitz  # PyMuPDF
import os
import re

pdf_path = r'TaiLieu\textbookForPractice\Ch_10_Recent Data and Analyses Developments in Accounting.pdf'
out_path = r'scratch\ch10_raw.txt'

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

    print("Learning Objectives:")
    for match in sorted(set(re.findall(r'LO 10\.\d+', text))):
        print(match)

    print("\nExercise sections:")
    for match in set(re.findall(r'Brief Exercises|Exercises|Professional Application Cases|Multiple Choice|Chapter Review', text, re.IGNORECASE)):
        print(match)

    print("\nTitle peek:")
    print("\n".join(text.split('\n')[:20]))
