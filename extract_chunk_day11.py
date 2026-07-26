import fitz
import os

def extract_and_chunk(pdf_path, start_page, end_page, output_prefix, chunk_size=15000):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        # 0-indexed logic: Page 68 is index 67
        for i in range(start_page - 1, min(end_page - 1, len(doc))):
            text += doc[i].get_text("text") + "\n"
        
        doc.close()
        
        full_output = f"buoi11A_text_utf8.txt"
        with open(full_output, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extracted {len(text)} characters to {full_output}")
        
        # Chunking
        total_length = len(text)
        num_chunks = (total_length // chunk_size) + 1
        
        start = 0
        for i in range(1, num_chunks + 1):
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
    pdf1 = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\ebooks\_OceanofPDF.com_Data_and_Analytics_in_Accounting_-_Ann_C_Dzuranin.pdf"
    
    # Extracting pages 68 to 138 from PDF 1
    extract_and_chunk(pdf1, 68, 138, "chunk11A", chunk_size=15000)
