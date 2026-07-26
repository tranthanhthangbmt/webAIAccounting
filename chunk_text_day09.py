import os

def chunk_text(input_file, chunk_prefix, chunk_size=15000):
    if not os.path.exists(input_file):
        print(f"File {input_file} not found.")
        return
        
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
        
    total_length = len(text)
    print(f"Total length of {input_file}: {total_length} characters")
    
    num_chunks = (total_length // chunk_size) + 1
    
    start = 0
    for i in range(1, num_chunks + 1):
        end = start + chunk_size
        if end > total_length:
            end = total_length
        else:
            # find the nearest newline to avoid cutting in the middle of a sentence
            nearest_newline = text.rfind("\n", start, end)
            if nearest_newline != -1:
                end = nearest_newline + 1
                
        chunk = text[start:end]
        output_file = f"{chunk_prefix}_{i}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(chunk)
            
        print(f"Created {output_file} ({len(chunk)} chars)")
        start = end

if __name__ == "__main__":
    chunk_text("buoi9A_text_utf8.txt", "chunk9A", chunk_size=15000)
    chunk_text("buoi9B_text_utf8.txt", "chunk9B", chunk_size=15000)
