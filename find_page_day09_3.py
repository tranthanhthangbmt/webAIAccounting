import fitz

def search_text_in_pdf(pdf_path, search_term, max_pages=300):
    try:
        doc = fitz.open(pdf_path)
        for i in range(min(max_pages, len(doc))):
            text = doc[i].get_text("text")
            if search_term.lower() in text.lower():
                print(f"Match found on page {i+1} for '{search_term}'")
                # print a snippet
                idx = text.lower().find(search_term.lower())
                print(text[max(0, idx-50):min(len(text), idx+100)])
                print("-" * 40)
        doc.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Artificial_Intelligence_and_Finance_-_Georgios_I_Zekos.pdf"
    pdf2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"
    
    print("Searching PDF 1 for 'Chapter 3'...")
    search_text_in_pdf(pdf1, "Chapter 3", max_pages=300)
    
    print("\nSearching PDF 2 for 'Robo-Advisors'...")
    search_text_in_pdf(pdf2, "Robo-Advisors", max_pages=300)
    
    print("\nSearching PDF 2 for 'Chapter 6'...")
    search_text_in_pdf(pdf2, "Chapter 6", max_pages=300)
