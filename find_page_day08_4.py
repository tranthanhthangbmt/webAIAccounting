import fitz
import sys

pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"
pdf2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Fintech_-_Pranay_Gupta.pdf"

doc1 = fitz.open(pdf1)
for i in range(100, 150):
    text = doc1[i].get_text()
    if "Deep Diving into Financial Frauds" in text:
        print(f"Book 1: Chapter 6 starts at actual index {i}")
        break

doc2 = fitz.open(pdf2)
for i in range(350, 450):
    text = doc2[i].get_text()
    if "AI Algorithmic Trading" in text:
        print(f"Book 2: AI Algorithmic Trading starts at actual index {i}")
        break
