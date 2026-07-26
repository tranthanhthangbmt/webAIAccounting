import fitz

pdf1_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"
pdf2_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Fintech_-_Pranay_Gupta.pdf"

def print_toc(pdf_path, search_term=""):
    try:
        doc = fitz.open(pdf_path)
        toc = doc.get_toc()
        import os
        filename = os.path.basename(pdf_path)
        print(f"--- TOC for {filename} ---")
        found = False
        for item in toc:
            level, title, page = item
            if search_term.lower() in title.lower():
                print(f"Level {level}: {title} (Page {page})")
                found = True
        
        if not found and not search_term:
            for item in toc[:50]:
                print(item)
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

print_toc(pdf1_path, "Chapter 6")
print_toc(pdf1_path, "Credit Scoring")
print_toc(pdf1_path, "Algorithmic")

print_toc(pdf2_path, "Algorithmic")
print_toc(pdf2_path, "Trading")
