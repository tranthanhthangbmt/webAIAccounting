import os
import glob
import re
from deep_translator import GoogleTranslator

# Keywords to preserve in parentheses
KEYWORDS = [
    "Accounting", "Analytics", "SQL", "Excel", "Data Preparation", "Data",
    "Data Exploration", "Extract", "Transform", "Load", "ETL", "Tableau", "Alteryx"
]

def translate_file(input_path):
    output_path = input_path.replace('.txt', '.md').replace('ch05_chunk_', 'ch05_tr_chunk_')
    print(f"Translating {input_path} -> {output_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    paragraphs = text.split("\n\n")
    translator = GoogleTranslator(source='en', target='vi')
    translated_paragraphs = []
    
    for p in paragraphs:
        p = p.strip()
        if not p:
            translated_paragraphs.append("")
            continue
            
        if p.startswith("--- PAGE"):
            continue
            
        # Optional: formatting adjustments
        # We will keep it simple and just translate
        
        if len(p) > 4900:
            sentences = p.split('. ')
            temp_p = ""
            for s in sentences:
                if s.strip():
                    try:
                        trans_s = translator.translate(s)
                        temp_p += trans_s + ". "
                    except Exception as e:
                        print("Error translating sentence:", e)
                        temp_p += s + ". "
            translated_paragraphs.append(temp_p)
        else:
            try:
                trans = translator.translate(p)
                translated_paragraphs.append(trans)
            except Exception as e:
                print(f"Error translating paragraph of length {len(p)}: {e}")
                translated_paragraphs.append(p)
                
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(translated_paragraphs))
    print(f"Saved {output_path}")

if __name__ == "__main__":
    chunks = glob.glob(r"scratch\ch05_chunk_*.txt")
    chunks.sort(key=lambda x: int(re.search(r'ch05_chunk_(\d+)', x).group(1)))

    for chunk in chunks:
        translate_file(chunk)

    print("All chunks translated!")
