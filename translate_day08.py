import os
import glob
from deep_translator import GoogleTranslator

def translate_file(input_path):
    output_path = input_path.replace('.txt', '_vi.txt')
    print(f"Translating {input_path} -> {output_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split by double newline to preserve paragraph structure
    paragraphs = text.split("\n\n")
    translator = GoogleTranslator(source='en', target='vi')
    translated_paragraphs = []
    
    for p in paragraphs:
        if not p.strip():
            translated_paragraphs.append(p)
            continue
            
        # Google Translate API has a 5000 char limit
        # If a paragraph is too long (very rare), we need to split it
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

chunks = glob.glob(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\chunk8A_*.txt")
chunks.extend(glob.glob(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\chunk8B_*.txt"))
chunks = [c for c in chunks if not c.endswith('_vi.txt')]
chunks.sort()

for chunk in chunks:
    translate_file(chunk)

print("All chunks translated!")
