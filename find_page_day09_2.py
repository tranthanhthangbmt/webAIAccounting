import fitz
import sys
import os

def find_chapter(pdf_path, search_term1):
    try:
        doc = fitz.open(pdf_path)
        toc = doc.get_toc()
        print(f"TOC for {os.path.basename(pdf_path)}:")
        for item in toc:
            level, title, page = item
            if search_term1.lower() in title.lower():
                print(f"Match: Level {level}, Title: '{title}', Page: {page}")
        
        doc.close()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

if __name__ == "__main__":
    pdf2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"
    
    print("\nSearching PDF 2...")
    find_chapter(pdf2, "Robo")
    print("\nSearching PDF 2 for Chapter 6...")
    find_chapter(pdf2, "6")
