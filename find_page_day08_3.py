import fitz

pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"
pdf2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Fintech_-_Pranay_Gupta.pdf"

# The TOC page numbers might be printed page numbers, let's add the offset.
# For Generative AI, page 410 is printed page 410. The actual index could be different.
doc1 = fitz.open(pdf1)
# Find the actual page index for printed page 410
for i in range(400, 435):
    text = doc1[i].get_text()
    if "Credit Scoring and Risk Management" in text and "Algorithmic Trading" in text:
        print(f"Book 1: Found section at actual index {i}")
        # print(text[:500])

doc2 = fitz.open(pdf2)
for i in range(365, 395):
    text = doc2[i].get_text()
    if "AI Algorithmic Trading" in text:
        print(f"Book 2: Found section at actual index {i}")
