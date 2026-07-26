import fitz

pdf1_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"

doc = fitz.open(pdf1_path)
for i in range(8, 13):
    text = doc[i].get_text()
    print(f"--- Page {i} ---")
    print(text[:2000])
