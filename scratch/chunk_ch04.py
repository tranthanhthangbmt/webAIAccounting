def chunk_text():
    with open('scratch/ch04_raw.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunks = [
        (1, 667),
        (668, 1022),
        (1023, 1546),
        (1547, 2074),
        (2075, 3155),
        (3156, 3358),
        (3359, 3633),
        (3634, 3795),
        (3796, 3955),
        (3956, len(lines))
    ]

    for i, (start, end) in enumerate(chunks):
        chunk_lines = lines[start-1:end]
        with open(f'scratch/ch04_chunk_{i+1}.txt', 'w', encoding='utf-8') as out:
            out.writelines(chunk_lines)

if __name__ == '__main__':
    chunk_text()
    print("Chunked into 10 files.")
