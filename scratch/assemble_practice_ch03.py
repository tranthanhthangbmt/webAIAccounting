import os

def assemble():
    output_file = 'docs/practice_ch03.md'
    chunks = [
        'scratch/ch03_tr_chunk_1.md',
        'scratch/ch03_tr_chunk_2.md',
        'scratch/ch03_tr_chunk_3.md',
        'scratch/ch03_tr_chunk_4.md',
        'scratch/ch03_tr_chunk_5.md',
        'scratch/ch03_tr_chunk_6.md',
        'scratch/ch03_tr_chunk_7.md',
        'scratch/ch03_tr_chunk_8.md',
        'scratch/ch03_tr_chunk_9.md',
        'scratch/ch03_tr_chunk_10.md',
    ]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('# Chương 3: Động lực và Mục tiêu cho Phân tích Dữ liệu (Motivations and Objectives for Data Analysis)\n\n')
        outfile.write('<!-- tabs:start -->\n')
        outfile.write('#### **Tiếng Việt**\n\n')

        for chunk_path in chunks:
            if os.path.exists(chunk_path):
                with open(chunk_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    outfile.write('\n\n')
            else:
                print(f"Warning: {chunk_path} not found.")
        
        outfile.write('#### **English**\n')
        outfile.write('<iframe src="TaiLieu/textbookForPractice/Ch_03_Motivations%20and%20Objectives%20for%20Data%20Analysis.pdf" width="100%" height="800px"></iframe>\n\n')
        outfile.write('<!-- tabs:end -->\n')

if __name__ == '__main__':
    assemble()
    print("Assembled docs/practice_ch03.md")
