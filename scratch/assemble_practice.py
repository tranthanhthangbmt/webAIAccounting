import re
import os

raw_text_path = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\scratch\ch01_raw.txt'
with open(raw_text_path, 'r', encoding='utf-8') as f:
    raw_text = f.read()

# For Chunks 1-5
lo1_start = raw_text.find("CHAPTER 1\nData and Analytics")
lo2_start = raw_text.find("1.2 What are the Stages of the Data Analysis")
lo3_start = raw_text.find("1.3 What is a Data Analytics Mindset?")
lo4_start = raw_text.find("1.4 How is a Data Analytics Mindset Applied?")
review_start = raw_text.find("Chapter Review and Practice")

en_chunk1 = raw_text[lo1_start:lo2_start] if lo1_start != -1 and lo2_start != -1 else ""
en_chunk2_3 = raw_text[lo2_start:lo3_start] if lo2_start != -1 and lo3_start != -1 else ""
en_chunk4 = raw_text[lo3_start:lo4_start] if lo3_start != -1 and lo4_start != -1 else ""
en_chunk5 = raw_text[lo4_start:review_start] if lo4_start != -1 and review_start != -1 else ""

# For Chunks 6-10, read from ch01_chunk_27_43.txt
prac_path = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\scratch\ch01_chunk_27_43.txt'
with open(prac_path, 'r', encoding='utf-8') as f:
    prac_lines = f.readlines()

en_chunk6 = "".join(prac_lines[0:315])
en_chunk7 = "".join(prac_lines[315:520])
en_chunk8 = "".join(prac_lines[520:619]) + "".join(prac_lines[644:662])
en_chunk9 = "".join(prac_lines[619:644]) + "".join(prac_lines[662:847])
en_chunk10 = "".join(prac_lines[847:])

def get_vi_text(chunk_id):
    path = f'd:\\DongAUniversity\\TÀI LIỆU DẠY HỌC_2024-2025\\Môn TTNT cho kế toán_2026\\webAIAccounting\\scratch\\ch01_tr_chunk_{chunk_id}.md'
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'#### \*\*Tiếng Việt\*\*(.*?)(?=#### \*\*English\*\*)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

vi_chunk1 = get_vi_text(1)
vi_chunk2 = get_vi_text(2)
vi_chunk3 = get_vi_text(3)
vi_chunk2_3 = vi_chunk2 + "\n\n" + vi_chunk3
vi_chunk4 = get_vi_text(4)
vi_chunk5 = get_vi_text(5)
vi_chunk6 = get_vi_text(6)
vi_chunk7 = get_vi_text(7)
vi_chunk8 = get_vi_text(8)
vi_chunk9 = get_vi_text(9)
vi_chunk10 = get_vi_text(10)

# Concatenate all Vietnamese chunks
vi_all = "\n\n".join(filter(None, [
    vi_chunk1, vi_chunk2_3, vi_chunk4, vi_chunk5,
    vi_chunk6, vi_chunk7, vi_chunk8, vi_chunk9, vi_chunk10
]))

# Create the single dual-tab layout at the top
pdf_path = "../TaiLieu/textbookForPractice/Ch_01_Data and Analytics in the Accounting Profession.pdf"
en_embed = f'<object data="{pdf_path}" type="application/pdf" width="100%" height="800px"><p>Trình duyệt của bạn không hỗ trợ xem PDF trực tiếp. Vui lòng tải xuống tệp PDF tại <a href="{pdf_path}">đây</a>.</p></object>'

final_md = "# Chapter 1: Data and Analytics in the Accounting Profession\n\n"
final_md += "<!-- tabs:start -->\n"
final_md += "#### **Tiếng Việt**\n\n"
final_md += vi_all + "\n\n"
final_md += "#### **English**\n\n"
final_md += en_embed + "\n\n"
final_md += "<!-- tabs:end -->\n"

out_path = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs\practice_ch01.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(final_md)

print("Assembled docs/practice_ch01.md successfully with single top tab.")
