import fitz

def extract_pages(pdf_path, start_page, end_page, output_file):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        # fitz pages are 0-indexed, so page N is doc[N-1] if N is 1-indexed.
        # But our previous output "Match found on page 152" means index 151.
        for i in range(start_page - 1, min(end_page, len(doc))):
            text += doc[i].get_text("text") + "\n"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extracted {len(text)} characters to {output_file}")
        doc.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Artificial_Intelligence_and_Finance_-_Georgios_I_Zekos.pdf"
    pdf2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"
    
    # Extracting pages 91 to 140 from PDF 1
    extract_pages(pdf1, 91, 140, "buoi9A_text_utf8.txt")
    
    # Extracting pages 150 to 155 from PDF 2
    extract_pages(pdf2, 150, 155, "buoi9B_text_utf8.txt")
