import PyPDF2
import re
import json

pdf_path = "d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/textbookForPractice/Ch_05_Analysis_ Data Preparation.pdf"

with open(pdf_path, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

# Clean up text a bit
text = re.sub(r'\n+', ' ', text)

results = {}

# Find all ILLUSTRATION, BE, EX, PAC in chapter 5
patterns = [
    r'(ILLUSTRATION 5\.\d+[A-Z]?)(.*?)(?=ILLUSTRATION|BE 5|EX 5|PAC 5|$)',
    r'(BE 5\.\d+)(.*?)(?=ILLUSTRATION|BE 5|EX 5|PAC 5|$)',
    r'(EX 5\.\d+)(.*?)(?=ILLUSTRATION|BE 5|EX 5|PAC 5|$)',
    r'(PAC 5\.\d+)(.*?)(?=ILLUSTRATION|BE 5|EX 5|PAC 5|$)'
]

for pat in patterns:
    matches = re.findall(pat, text, re.IGNORECASE)
    for match in matches:
        title = match[0].upper()
        content = match[1].strip()[:500]
        if title not in results:
            results[title] = content

output_path = "d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter05/pdf_context_ch05.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(results)} items from PDF.")
