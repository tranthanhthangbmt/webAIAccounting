import os

input_file = r"scratch\ch02_raw.txt"

# Defined page ranges for each chunk based on LOs
chunks_def = [
    ("Chunk 1 (LO 2.1)", 1, 9),
    ("Chunk 2 (LO 2.2)", 9, 14),
    ("Chunk 3 (LO 2.3)", 14, 26),
    ("Chunk 4 (LO 2.4)", 26, 41),
    ("Chunk 5 (LO 2.5)", 41, 49),
    ("Chunk 6 (Chapter Review)", 49, 56),
    ("Chunk 7 (Multiple Choice)", 56, 58),
    ("Chunk 8 (Brief Exercises)", 58, 61),
    ("Chunk 9 (Exercises)", 61, 66),
    ("Chunk 10 (Problems)", 66, 71)
]

def chunk_text():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pages = content.split("\n--- PAGE ")
    # pages[0] is empty, pages[1] is page 1 etc
    
    for title, start, end in chunks_def:
        chunk_text = ""
        # Get pages from start to end-1
        for i in range(start, min(end, len(pages))):
            chunk_text += "\n--- PAGE " + pages[i]
            
        out_name = f"scratch/ch02_chunk_{start}_{end}.txt"
        with open(out_name, "w", encoding="utf-8") as out_f:
            out_f.write(chunk_text.strip())
        print(f"Created {out_name} with {len(chunk_text)} chars")

if __name__ == "__main__":
    chunk_text()
