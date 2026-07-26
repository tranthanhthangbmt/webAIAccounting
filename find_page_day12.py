import fitz
import os

def find_chapter(pdf_path, search_terms):
    try:
        doc = fitz.open(pdf_path)
        toc = doc.get_toc()
        print(f"TOC for {os.path.basename(pdf_path)}:")
        
        for term in search_terms:
            print(f"\nSearching for '{term}':")
            for item in toc:
                level, title, page = item
                if term.lower() in title.lower():
                    print(f"Match: Level {level}, Title: '{title}', Page: {page}")
        doc.close()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

if __name__ == "__main__":
    pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Scott_Dell_Mfon_Akpan.pdf"
    
    print("Searching PDF for chapters...")
    find_chapter(pdf1, ["Generative AI in Accounting", "Web-Enhanced ChatGPT", "Chapter 1", "Chapter 2", "Chapter 12", "Chapter 13"])
