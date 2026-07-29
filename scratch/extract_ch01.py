import fitz
import os

pdf_path = r"TaiLieu\textbookForPractice\Ch_01_Data and Analytics in the Accounting Profession.pdf"
out_path = r"scratch\ch01_raw.txt"

def extract_text():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return
        
    doc = fitz.open(pdf_path)
    with open(out_path, "w", encoding="utf-8") as f:
        for i, page in enumerate(doc):
            text = page.get_text()
            f.write(f"\n--- PAGE {i+1} ---\n")
            f.write(text)
            
    print(f"Extracted {doc.page_count} pages to {out_path}")

if __name__ == "__main__":
    extract_text()
