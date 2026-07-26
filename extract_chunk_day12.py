import fitz
import os

def extract_and_chunk(pdf_path, ranges, output_prefix, chunk_size=15000):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        
        # 0-indexed logic: Page 36 is index 35
        for start_page, end_page in ranges:
            for i in range(start_page - 1, min(end_page - 1, len(doc))):
                text += doc[i].get_text("text") + "\n"
        
        doc.close()
        
        full_output = f"buoi12A_text_utf8.txt"
        with open(full_output, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extracted {len(text)} characters to {full_output}")
        
        # Chunking
        total_length = len(text)
        num_chunks = (total_length // chunk_size) + 1
        
        start = 0
        for i in range(1, num_chunks + 1):
            if start >= total_length:
                break
                
            end = start + chunk_size
            if end > total_length:
                end = total_length
            else:
                nearest_newline = text.rfind("\n", start, end)
                if nearest_newline != -1:
                    end = nearest_newline + 1
                    
            chunk = text[start:end]
            output_file = f"{output_prefix}_{i}.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(chunk)
                
            print(f"Created {output_file} ({len(chunk)} chars)")
            start = end
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_ChatGPT_and_AI_for_Accountants_-_Scott_Dell_Mfon_Akpan.pdf"
    
    # Extracting Chapter 1 (36 to 50) and Chapter 12 (225 to 236)
    ranges = [(36, 50), (225, 236)]
    extract_and_chunk(pdf1, ranges, "chunk12A", chunk_size=15000)
