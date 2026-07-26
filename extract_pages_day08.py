import fitz
import re
import os

pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\Generative Artificial Intelligence in Finance_ Large Language Models, Interfaces, and Industry Us...{Pethuru Raj Chelliah}(2025){107913862} libgen.li.pdf"
pdf2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Fintech_-_Pranay_Gupta.pdf"
output1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\buoi8A_text_utf8.txt"
output2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\buoi8B_text_utf8.txt"

def extract_and_clean(doc, start_idx, end_idx):
    text = ""
    for i in range(start_idx, end_idx):
        page = doc[i]
        # remove headers/footers if possible, but let's just extract all for now
        t = page.get_text()
        text += f"\n\n--- Page {i+1} ---\n\n" + t
    return text

doc1 = fitz.open(pdf1)
text1 = extract_and_clean(doc1, 123, 147) # Chapter 6
with open(output1, "w", encoding="utf-8") as f:
    f.write(text1)
print(f"Extracted {len(text1)} chars to {output1}")

doc2 = fitz.open(pdf2)
# AI Algorithmic Trading starts at index 364.
# Let's extract until we hit another big section or just extract 15 pages.
# Actually, the TOC showed:
# Level 4: Case Study: QCP Capital and Trading Cryptoassets (Page 282)
# Level 4: AI Algorithmic Trading (Page 365)
# There are no other Level 4s after 365. Let's just extract 364 to 380 and we can review.
text2 = extract_and_clean(doc2, 364, 380)
with open(output2, "w", encoding="utf-8") as f:
    f.write(text2)
print(f"Extracted {len(text2)} chars to {output2}")
