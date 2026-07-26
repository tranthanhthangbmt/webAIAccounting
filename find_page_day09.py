import fitz
import sys
import os

def find_chapter(pdf_path, search_term1, search_term2=None):
    try:
        doc = fitz.open(pdf_path)
        toc = doc.get_toc()
        print(f"TOC for {os.path.basename(pdf_path)}:")
        found = False
        for item in toc:
            level, title, page = item
            if search_term1.lower() in title.lower():
                print(f"Match 1: Level {level}, Title: '{title}', Page: {page}")
                found = True
            elif search_term2 and search_term2.lower() in title.lower():
                print(f"Match 2: Level {level}, Title: '{title}', Page: {page}")
                found = True
        
        if not found:
            print("Not found in TOC, scanning pages...")
            for i in range(min(50, len(doc))):
                text = doc[i].get_text("text")
                if search_term1.lower() in text.lower():
                    print(f"Match found on page {i+1} for {search_term1}")
        doc.close()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

if __name__ == "__main__":
    pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Artificial_Intelligence_and_Finance_-_Georgios_I_Zekos.pdf"
    pdf2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"
    
    print("Searching PDF 1...")
    find_chapter(pdf1, "Crypto Assets", "Chapter 2")
    
    print("\nSearching PDF 2...")
    find_chapter(pdf2, "Robo-Advisors", "Chapter 6")
