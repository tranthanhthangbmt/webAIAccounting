import os

input_file = r"scratch\ch01_raw.txt"

# Defined page ranges for each chunk based on LOs
chunks_def = [
    ("Chunk 1 (LO 1-1)", 1, 5),
    ("Chunk 2 (LO 1-2)", 5, 8),
    ("Chunk 3 (LO 1-3)", 8, 15),
    ("Chunk 4 (LO 1-4)", 15, 19),
    ("Chunk 5 (LO 1-5)", 19, 22),
    ("Chunk 6 (LO 1-6 & Summary)", 22, 27),
    ("Chunk 7 (End Materials)", 27, 43)
]

def chunk_text():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pages = content.split("--- PAGE ")
    # pages[0] is empty, pages[1] is page 1 etc
    
    for title, start, end in chunks_def:
        chunk_text = ""
        # Get pages from start to end-1 (or adjust depending on how split works)
        # Assuming end page is exclusive or inclusive? Let's make it inclusive.
        # Actually end-1 because the next LO starts on the 'end' page. Let's just include the pages and we will translate manually.
        for i in range(start, min(end + 1, len(pages))):
            chunk_text += "--- PAGE " + pages[i]
            
        out_name = f"scratch/ch01_chunk_{start}_{end}.txt"
        with open(out_name, "w", encoding="utf-8") as out_f:
            out_f.write(chunk_text)
        print(f"Created {out_name} with {len(chunk_text)} chars")

if __name__ == "__main__":
    chunk_text()
