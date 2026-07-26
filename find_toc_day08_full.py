import fitz

pdf1_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"

def print_full_toc(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        toc = doc.get_toc()
        import os
        filename = os.path.basename(pdf_path)
        print(f"--- Full TOC for {filename} ---")
        for item in toc:
            print(item)
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

print_full_toc(pdf1_path)
