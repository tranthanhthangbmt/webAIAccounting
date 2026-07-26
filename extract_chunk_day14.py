import fitz
import os

def extract_and_chunk(pdf_path, ranges, output_prefix, chunk_size=15000):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        
        for start_page, end_page in ranges:
            # 0-indexed logic
            for i in range(start_page - 1, min(end_page - 1, len(doc))):
                text += doc[i].get_text("text") + "\n"
        
        doc.close()
        
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
    pdf2 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Data_and_Analytics_in_Accounting_-_Ann_C_Dzuranin.pdf"
    
    print("Extracting from PDF 2 (Chapter 7)...")
    extract_and_chunk(pdf2, [(406, 468)], "chunk14A", chunk_size=15000)

    print("\nExtracting from PDF 2 (Chapter 9)...")
    extract_and_chunk(pdf2, [(532, 594)], "chunk14B", chunk_size=15000)
