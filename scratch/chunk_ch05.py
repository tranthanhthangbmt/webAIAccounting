import re

raw_file = r'scratch\ch05_raw.txt'

with open(raw_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Split by pages
pages = re.split(r'--- PAGE \d+ ---\n', text)
pages = [p for p in pages if p.strip()]

num_pages = len(pages)
chunks = 12
pages_per_chunk = num_pages // chunks
remainder = num_pages % chunks

current_page = 0
for i in range(1, chunks + 1):
    take = pages_per_chunk + (1 if i <= remainder else 0)
    chunk_pages = pages[current_page:current_page+take]
    current_page += take
    
    out_file = rf'scratch\ch05_chunk_{i}.txt'
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(chunk_pages))
    
    print(f"Wrote {take} pages to {out_file}")
