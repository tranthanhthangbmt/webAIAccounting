import PyPDF2
import re
import json

pdf_path = "d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/TaiLieu/textbookForPractice/Ch_03_Motivations and Objectives for Data Analysis.pdf"

with open(pdf_path, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

# Clean up text a bit
text = re.sub(r'\n+', ' ', text)

results = {}

# Find all ILLUSTRATION, BE, EX, PAC in chapter 3
patterns = [
    r'(ILLUSTRATION 3\.\d+)(.*?)(?=ILLUSTRATION|BE 3|EX 3|PAC 3|$)',
    r'(BE 3\.\d+)(.*?)(?=ILLUSTRATION|BE 3|EX 3|PAC 3|$)',
    r'(EX 3\.\d+)(.*?)(?=ILLUSTRATION|BE 3|EX 3|PAC 3|$)',
    r'(PAC 3\.\d+)(.*?)(?=ILLUSTRATION|BE 3|EX 3|PAC 3|$)'
]

for pat in patterns:
    matches = re.findall(pat, text, re.IGNORECASE)
    for match in matches:
        title = match[0].upper()
        content = match[1].strip()[:500] # Get first 500 characters
        if title not in results:
            results[title] = content

output_path = "d:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter03/pdf_context.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(results)} items from PDF.")
