# verify_textbook_mapping.py
import os

pdf_mapping = {
    "docs/buoi_01.md": [
        "Buoi_01_Chương 1_What Accountants Need to Know (Phần Introduction & History of AI).pdf"
    ],
    "docs/buoi_02.md": [
        "Buoi_02A_Chương 1 (AI and Finance_Mục 1.2, 1.6, 1.7, 1.15) 2. Các phần về Big Data và Blockchain.pdf",
        "Buoi_02B_Phần Big Data & Blockchain.pdf"
    ],
    "docs/buoi_03.md": [
        "Buoi_03A_Chương 1 (Machine Reasoning, ML, DL, NLP).pdf",
        "Buoi_03B_2. Chương 15 (Ethics and Laws_ Governing Generative AI’s Role...).pdf"
    ],
    "docs/buoi_04.md": [
        "Buoi_04A_Chương 5 (Market Segmentation...).pdf",
        "Buoi_04B_Chương 10 (Forecasting Financial Health...).pdf"
    ],
    "docs/buoi_05.md": [
        "Buoi_05A_Chương 12 (Managing Decision Uncertainty).pdf",
        "Buoi_05B_Chương 14 (New Product Development).pdf"
    ],
    "docs/buoi_06.md": [
        "Buoi_06A_Chương 5 (Case study 4_ Tackling public sector corruption).pdf",
        "Buoi_06B_2. Chương 1 (Preserving financial stability).pdf"
    ],
    "docs/buoi_07.md": [
        "Buoi_07A_Chương 9 (Automating Internal Controls).pdf",
        "Buoi_07B_Chương 12 (Intelligent Automation of Fraud Detection).pdf"
    ],
    "docs/buoi_08.md": [
        "Buoi_08A_Chương 6 (Credit Scoring, Algorithmic Trading)2. Phần AI Algorithmic Trading.pdf",
        "Buoi_08B_Chuong_4_AI_Market_Manipulation_new.pdf"
    ],
    "docs/buoi_09.md": [
        "Buoi_09A_Chương 2 (AI, Crypto Assets, and Financial Markets).pdf",
        "Buoi_9B_Chương 6 (Mục Robo-Advisors).pdf"
    ],
    "docs/buoi_11.md": [
        "Buoi_11_Chương 2 (Foundational Data Analysis Skills).pdf"
    ],
    "docs/buoi_12.md": [
        "Buoi_12A_Chương 1 (Generative AI in Accounting).pdf",
        "Buoi_12B_Chương 12 (Web-Enhanced ChatGPT).pdf"
    ],
    "docs/buoi_13.md": [
        "Buoi_13A_Chương 6 (Turbocharging Financial Analysis).pdf",
        "Buoi_13B_Chương 3 & 4 (Planning Data Strategies).pdf"
    ],
    "docs/buoi_14.md": [
        "Buoi_14A_Chương 7 (Data Exploration).pdf",
        "Buoi_14B_Chương 9 (Communicating Results).pdf"
    ]
}

textbook_dir = "textbook"
all_ok = True

for doc, pdfs in pdf_mapping.items():
    for pdf in pdfs:
        path = os.path.join(textbook_dir, pdf)
        if not os.path.exists(path):
            print(f"ERROR: Missing file for {doc} -> {path}")
            all_ok = False
        else:
            print(f"OK: {doc} -> {pdf}")

if all_ok:
    print("\nSUCCESS! All 23 PDF files mapped across 13 buoi exist in textbook/ directory!")
