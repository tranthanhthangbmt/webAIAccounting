import os

def chunk_file():
    raw_path = r"scratch\ch03_raw.txt"
    if not os.path.exists(raw_path):
        print(f"File not found: {raw_path}")
        return

    with open(raw_path, "r", encoding="utf-8") as f:
        content = f.read()

    pages = content.split("--- PAGE ")
    # pages[0] is empty, pages[1] is page 1

    chunks = {
        1: pages[1:10],
        2: pages[10:15],
        3: pages[15:18],
        4: pages[18:26],
        5: pages[26:31],
        6: pages[31:37],
        7: pages[37:46],
        8: pages[46:55],
        9: pages[55:60],
        10: pages[60:65]
    }

    for chunk_id, chunk_pages in chunks.items():
        if not chunk_pages:
            continue
        out_path = f"scratch\\ch03_chunk_{chunk_id}.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            for page in chunk_pages:
                f.write("--- PAGE " + page)
        print(f"Created {out_path} with {len(chunk_pages)} pages.")

if __name__ == "__main__":
    chunk_file()
