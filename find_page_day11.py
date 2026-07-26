import fitz
import os

def find_chapter(pdf_path, search_term1):
    try:
        doc = fitz.open(pdf_path)
        toc = doc.get_toc()
        print(f"TOC for {os.path.basename(pdf_path)}:")
        found = False
        for item in toc:
            level, title, page = item
            if search_term1.lower() in title.lower() or "chapter 2" in title.lower():
                print(f"Match: Level {level}, Title: '{title}', Page: {page}")
                found = True
            elif "chapter 3" in title.lower():
                print(f"Match: Level {level}, Title: '{title}', Page: {page}")
        
        if not found:
            print("Not found in TOC, scanning pages...")
            for i in range(min(150, len(doc))):
                text = doc[i].get_text("text")
                if search_term1.lower() in text.lower():
                    print(f"Match found on page {i+1} for {search_term1}")
        doc.close()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

if __name__ == "__main__":
    pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Data_and_Analytics_in_Accounting_-_Ann_C_Dzuranin.pdf"
    
    print("Searching PDF for Chapter 2...")
    find_chapter(pdf1, "Foundational Data Analysis Skills")
