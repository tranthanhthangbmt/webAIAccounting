# update_all_english_tabs.py
# Update the English tab of all buoi_*.md files to reference the exact textbook/ PDF files (1 or 2 files per buoi)

import os

pdf_info = {
    "docs/buoi_01.md": [
        {
            "title": "Chương 1: What Accountants Need to Know (Introduction & History of AI)",
            "file": "Buoi_01_Chương 1_What Accountants Need to Know (Phần Introduction & History of AI).pdf"
        }
    ],
    "docs/buoi_02.md": [
        {
            "title": "Chương 1: AI and Finance (Mục 1.2, 1.6, 1.7, 1.15)",
            "file": "Buoi_02A_Chương 1 (AI and Finance_Mục 1.2, 1.6, 1.7, 1.15) 2. Các phần về Big Data và Blockchain.pdf"
        },
        {
            "title": "Chuyên đề: Big Data & Blockchain trong Tài chính - Kế toán",
            "file": "Buoi_02B_Phần Big Data & Blockchain.pdf"
        }
    ],
    "docs/buoi_03.md": [
        {
            "title": "Chương 1: Machine Reasoning, Machine Learning, DL & NLP",
            "file": "Buoi_03A_Chương 1 (Machine Reasoning, ML, DL, NLP).pdf"
        },
        {
            "title": "Chương 15: Ethics and Laws Governing Generative AI’s Role",
            "file": "Buoi_03B_2. Chương 15 (Ethics and Laws_ Governing Generative AI’s Role...).pdf"
        }
    ],
    "docs/buoi_04.md": [
        {
            "title": "Chương 5: Market Segmentation & AI Customer Analysis",
            "file": "Buoi_04A_Chương 5 (Market Segmentation...).pdf"
        },
        {
            "title": "Chương 10: Forecasting Financial Health with AI",
            "file": "Buoi_04B_Chương 10 (Forecasting Financial Health...).pdf"
        }
    ],
    "docs/buoi_05.md": [
        {
            "title": "Chương 12: Managing Decision Uncertainty",
            "file": "Buoi_05A_Chương 12 (Managing Decision Uncertainty).pdf"
        },
        {
            "title": "Chương 14: New Product Development & Financial Planning",
            "file": "Buoi_05B_Chương 14 (New Product Development).pdf"
        }
    ],
    "docs/buoi_06.md": [
        {
            "title": "Chương 5 (Case Study 4): Tackling Public Sector Corruption",
            "file": "Buoi_06A_Chương 5 (Case study 4_ Tackling public sector corruption).pdf"
        },
        {
            "title": "Chương 1: Preserving Financial Stability in the Public Sector",
            "file": "Buoi_06B_2. Chương 1 (Preserving financial stability).pdf"
        }
    ],
    "docs/buoi_07.md": [
        {
            "title": "Chương 9: Automating Internal Controls",
            "file": "Buoi_07A_Chương 9 (Automating Internal Controls).pdf"
        },
        {
            "title": "Chương 12: Intelligent Automation of Fraud Detection",
            "file": "Buoi_07B_Chương 12 (Intelligent Automation of Fraud Detection).pdf"
        }
    ],
    "docs/buoi_08.md": [
        {
            "title": "Chương 6: Credit Scoring & AI Algorithmic Trading",
            "file": "Buoi_08A_Chương 6 (Credit Scoring, Algorithmic Trading)2. Phần AI Algorithmic Trading.pdf"
        },
        {
            "title": "Chương 4: AI & Market Manipulation",
            "file": "Buoi_08B_Chuong_4_AI_Market_Manipulation_new.pdf"
        }
    ],
    "docs/buoi_09.md": [
        {
            "title": "Chương 2: AI, Crypto Assets, and Financial Markets",
            "file": "Buoi_09A_Chương 2 (AI, Crypto Assets, and Financial Markets).pdf"
        },
        {
            "title": "Chương 6: Robo-Advisors in Financial Services",
            "file": "Buoi_9B_Chương 6 (Mục Robo-Advisors).pdf"
        }
    ],
    "docs/buoi_11.md": [
        {
            "title": "Chương 2: Foundational Data Analysis Skills (Ann C. Dzuranin)",
            "file": "Buoi_11_Chương 2 (Foundational Data Analysis Skills).pdf"
        }
    ],
    "docs/buoi_12.md": [
        {
            "title": "Chương 1: Generative AI in Accounting (Scott Dell)",
            "file": "Buoi_12A_Chương 1 (Generative AI in Accounting).pdf"
        },
        {
            "title": "Chương 12: Web-Enhanced ChatGPT & Custom GPTs",
            "file": "Buoi_12B_Chương 12 (Web-Enhanced ChatGPT).pdf"
        }
    ],
    "docs/buoi_13.md": [
        {
            "title": "Chương 6: Turbocharging Financial Analysis (Scott Dell)",
            "file": "Buoi_13A_Chương 6 (Turbocharging Financial Analysis).pdf"
        },
        {
            "title": "Chương 3 & 4: Planning Data Strategies & SPARKS Framework",
            "file": "Buoi_13B_Chương 3 & 4 (Planning Data Strategies).pdf"
        }
    ],
    "docs/buoi_14.md": [
        {
            "title": "Chương 7: Data Exploration (Ann C. Dzuranin)",
            "file": "Buoi_14A_Chương 7 (Data Exploration).pdf"
        },
        {
            "title": "Chương 9: Communicating & Visualizing Results (Ann C. Dzuranin)",
            "file": "Buoi_14B_Chương 9 (Communicating Results).pdf"
        }
    ]
}

def generate_english_tab_content(pdf_list):
    lines = []
    lines.append("#### ** 🇬🇧 Tiếng Anh (Bản gốc PDF) **\n")
    if len(pdf_list) == 1:
        item = pdf_list[0]
        lines.append("> Trình duyệt của bạn sẽ hiển thị nội dung PDF bài học gốc từ tài liệu giáo trình (`textbook/`) ở bên dưới.\n")
        lines.append(f"### 📄 {item['title']}\n")
        lines.append(f'<object data="textbook/{item["file"]}" type="application/pdf" class="pdf-container" width="100%" height="800px">')
        lines.append(f'    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/{item["file"]}" target="_blank">Nhấn vào đây để tải tài liệu PDF gốc</a>.</p>')
        lines.append('</object>')
        lines.append(f'<p style="text-align: right;"><a href="textbook/{item["file"]}" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về tài liệu PDF (Bản gốc tiếng Anh)</a></p>\n')
    else:
        lines.append("> Buổi học này bao gồm **2 tài liệu PDF gốc** từ giáo trình học phần (`textbook/`). Trình duyệt của bạn sẽ hiển thị nội dung từng tài liệu ở bên dưới.\n")
        for idx, item in enumerate(pdf_list):
            if idx > 0:
                lines.append("---\n")
            lines.append(f"### 📄 Tài liệu PDF {idx+1}: {item['title']}\n")
            lines.append(f'<object data="textbook/{item["file"]}" type="application/pdf" class="pdf-container" width="100%" height="800px">')
            lines.append(f'    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="textbook/{item["file"]}" target="_blank">Nhấn vào đây để tải tài liệu PDF {idx+1}</a>.</p>')
            lines.append('</object>')
            lines.append(f'<p style="text-align: right;"><a href="textbook/{item["file"]}" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Tài liệu {idx+1} (PDF)</a></p>\n')
    return "\n".join(lines) + "\n\n"

for filepath, pdfs in pdf_info.items():
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    eng_marker = "#### ** 🇬🇧 Tiếng Anh (Bản gốc PDF) **"
    viet_marker = "#### ** 🇻🇳 Tiếng Việt (Bản dịch) **"
    
    if eng_marker not in content or viet_marker not in content:
        print(f"WARNING: Could not find markers in {filepath}")
        continue
    
    part1 = content.split(eng_marker)[0]
    part2 = content.split(viet_marker)[1]
    
    new_eng_section = generate_english_tab_content(pdfs)
    
    new_content = part1 + new_eng_section + viet_marker + part2
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"UPDATED {filepath}: configured {len(pdfs)} PDF textbook file(s) in English tab!")

print("\nAll 13 buoi files updated successfully with clean newlines!")
