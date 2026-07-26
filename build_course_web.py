import os
import glob
import shutil
import re

WEB_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting"
EBOOKS_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks"

PDFS_DIR = os.path.join(WEB_DIR, "pdfs")
DOCS_DIR = os.path.join(WEB_DIR, "docs")

os.makedirs(PDFS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

print("Copying PDFs...")
# Copy PDFs to web folder (we only copy those we know we need to save space, or just all of them)
needed_pdfs = [
    "Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf",
    "_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Scott_Dell_Mfon_Akpan.pdf",
    "_OceanofPDF.com_Data_and_Analytics_in_Accounting_-_Ann_C_Dzuranin.pdf",
    "Machine Learning in Accounting_ - PhD, Ethan Blake.pdf",
    "_OceanofPDF.com_Algorithmic_Discrimination_and_Ethical_-_Muharrem_Kilic.pdf"
]

for pdf in needed_pdfs:
    src = os.path.join(EBOOKS_DIR, pdf)
    dst = os.path.join(PDFS_DIR, pdf)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)
        print(f"Copied: {pdf}")

# Lesson definition mapping
lessons = {
    "02": {
        "title": "Buổi 2: AI and Blockchain in Finance",
        "prefixes": ["chunkA", "chunkB"], # Special for day 2 since it was chunkA1, chunkB1, etc.
        "pdf": "Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf"
    },
    "03": {
        "title": "Buổi 3: Python for Finance & Data Science",
        "prefixes": ["chunk3A_", "chunk3B_"],
        "pdf": "Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf"
    },
    "04": {
        "title": "Buổi 4: Algorithms and AI Concepts",
        "prefixes": ["chunk4A_", "chunk4B_"],
        "pdf": "Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf"
    },
    "05": {
        "title": "Buổi 5: Data Analysis and Financial Modeling",
        "prefixes": ["chunk5A_", "chunk5B_"],
        "pdf": "Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf"
    },
    "06": {
        "title": "Buổi 6: Machine Learning for Finance",
        "prefixes": ["chunk6A_", "chunk6B_"],
        "pdf": "Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf"
    },
    "07": {
        "title": "Buổi 7: Deep Learning and Neural Networks",
        "prefixes": ["chunk7A_", "chunk7B_"],
        "pdf": "Cory Ng, John Alarcon - Artificial Intelligence in Accounting Practical Applications (2020) - libgen.li.pdf"
    },
    "08": {
        "title": "Buổi 8: Trí tuệ nhân tạo (AI) trong Kế toán",
        "prefixes": ["chunk8A_", "chunk8B_"],
        "pdf": "_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Scott_Dell_Mfon_Akpan.pdf"
    },
    "09": {
        "title": "Buổi 9: Đạo đức kinh doanh và An toàn AI",
        "prefixes": ["chunk9A_", "chunk9B_"],
        "pdf": "_OceanofPDF.com_Algorithmic_Discrimination_and_Ethical_-_Muharrem_Kilic.pdf"
    },
    "11": {
        "title": "Buổi 11: Chuẩn mực đạo đức Kế toán toàn cầu",
        "prefixes": ["chunk11A_"],
        "pdf": "_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Scott_Dell_Mfon_Akpan.pdf"
    },
    "12": {
        "title": "Buổi 12: Thực hành AI nhận thức và AI tạo sinh",
        "prefixes": ["chunk12A_"],
        "pdf": "_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Scott_Dell_Mfon_Akpan.pdf"
    },
    "13": {
        "title": "Buổi 13: Kỹ thuật Prompt & Khởi động Phân tích dữ liệu (SPARKS)",
        "prefixes": ["chunk13A_", "chunk13B_"],
        "pdf": "_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Scott_Dell_Mfon_Akpan.pdf"
    },
    "14": {
        "title": "Buổi 14: Phân tích Dữ liệu Chuyên sâu",
        "prefixes": ["chunk14A_", "chunk14B_"],
        "pdf": "_OceanofPDF.com_Data_and_Analytics_in_Accounting_-_Ann_C_Dzuranin.pdf"
    },
}

def get_sort_key(filename):
    basename = os.path.basename(filename)
    parts = basename.split('_')
    prefix = parts[0]
    try:
        if len(parts) > 1:
            num = int(parts[1].split('.')[0])
        else:
            # Special case for chunkA2_vi.txt -> chunkA2
            num_str = re.search(r'\d+', prefix)
            num = int(num_str.group()) if num_str else 0
    except:
        num = 0
    return (prefix, num)

print("Building markdown pages...")
for day, info in lessons.items():
    title = info['title']
    pdf_filename = info['pdf']
    prefixes = info['prefixes']
    
    # Gather chunks
    vi_chunks = []
    for prefix in prefixes:
        # Match e.g. chunk12A_1_vi.txt
        if day == "02":
             # chunkA1_1_vi.txt, chunkA2_vi.txt
             vi_chunks.extend(glob.glob(os.path.join(WEB_DIR, f"{prefix}*_vi.txt")))
        else:
             vi_chunks.extend(glob.glob(os.path.join(WEB_DIR, f"{prefix}*_vi.txt")))
             
    # Unique and sort
    vi_chunks = list(set(vi_chunks))
    vi_chunks.sort(key=get_sort_key)
    
    # Read content
    vi_text = ""
    for file in vi_chunks:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                vi_text += f.read() + "\n\n"
        except Exception as e:
            print(f"Error reading {file}: {e}")
            
    # Process image placeholders for markdown visual styling
    vi_text = vi_text.replace('<!-- IMAGE_PLACEHOLDER: ', '> 📸 **Hình ảnh**: ').replace(' -->', '')
    
    # Generate Markdown
    md_path = os.path.join(DOCS_DIR, f"buoi_{day}.md")
    
    md_content = f"""# {title}

<!-- tabs:start -->

#### ** 🇬🇧 Tiếng Anh (Bản gốc PDF) **

> Trình duyệt của bạn sẽ hiển thị nội dung PDF gốc ở dưới đây.

<object data="pdfs/{pdf_filename}" type="application/pdf" class="pdf-container">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="pdfs/{pdf_filename}" target="_blank">Nhấn vào đây để tải tài liệu PDF</a>.</p>
</object>

#### ** 🇻🇳 Tiếng Việt (Bản dịch) **

{vi_text}

<!-- tabs:end -->
"""
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"Generated {md_path} with {len(vi_chunks)} chunks.")

print("All done!")
