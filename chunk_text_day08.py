import os

def chunk_text(filepath, prefix, chunk_size=15000):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = []
    current_chunk = ""
    # split by paragraphs to avoid breaking sentences
    paragraphs = text.split("\n\n")
    
    for p in paragraphs:
        if len(current_chunk) + len(p) > chunk_size and len(current_chunk) > 0:
            chunks.append(current_chunk)
            current_chunk = p + "\n\n"
        else:
            current_chunk += p + "\n\n"
            
    if current_chunk:
        chunks.append(current_chunk)

    for i, c in enumerate(chunks):
        out_name = f"{prefix}_{i+1}.txt"
        with open(out_name, "w", encoding="utf-8") as out:
            out.write(c)
        print(f"Created {out_name} with {len(c)} characters.")

chunk_text(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\buoi8A_text_utf8.txt", r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\chunk8A")
chunk_text(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\buoi8B_text_utf8.txt", r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\chunk8B")
