# -*- coding: utf-8 -*-
import os
import re

base = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day03_Extra"
papers = os.path.join(base, "papers")

html_files = [
    os.path.join(base, "index.html"),
    os.path.join(papers, "index.html"),
    os.path.join(papers, "paper_1_InvoiceOCR_Deep_Learning_Recognition_tiengviet.html"),
    os.path.join(papers, "paper_2_Automated_Invoice_LLM_OCR_tiengviet.html"),
    os.path.join(papers, "paper_3_Fake_Invoices_Receipts_GenAI_tiengviet.html"),
    os.path.join(papers, "paper_4_AI_Drone_BigData_Auditing_tiengviet.html")
]

broken = 0
for hf in html_files:
    dir_path = os.path.dirname(hf)
    with open(hf, "r", encoding="utf-8") as f:
        html = f.read()

    # check img src
    img_srcs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', html)
    for src in img_srcs:
        if src.startswith("http") or src.startswith("data:"):
            continue
        full_p = os.path.normpath(os.path.join(dir_path, src))
        if not os.path.exists(full_p):
            print(f"BROKEN IMG in {os.path.basename(hf)}: {src} -> {full_p}")
            broken += 1

    # check local a href
    hrefs = re.findall(r'<a[^>]+href=[\'"]([^\'"]+)[\'"]', html)
    for href in hrefs:
        if href.startswith("http") or href.startswith("#") or href.startswith("javascript:"):
            continue
        pure_href = href.split("#")[0]
        if not pure_href:
            continue
        full_p = os.path.normpath(os.path.join(dir_path, pure_href))
        if not os.path.exists(full_p):
            print(f"BROKEN LINK in {os.path.basename(hf)}: {href} -> {full_p}")
            broken += 1

    # check iframe src
    iframes = re.findall(r'<iframe[^>]+src=[\'"]([^\'"]+)[\'"]', html)
    for ifr in iframes:
        if ifr.startswith("http") or ifr.startswith("#") or ifr.startswith("javascript:"):
            continue
        pure_ifr = ifr.split("#")[0]
        full_p = os.path.normpath(os.path.join(dir_path, pure_ifr))
        if not os.path.exists(full_p):
            print(f"BROKEN IFRAME in {os.path.basename(hf)}: {ifr} -> {full_p}")
            broken += 1

if broken == 0:
    print("ALL IMAGES, SLIDES, AND LOCAL LINKS VALIDATED 100% PERFECTLY!")
else:
    print(f"Found {broken} broken items.")
