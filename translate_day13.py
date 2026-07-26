import os
import glob
import re
from deep_translator import GoogleTranslator

# Keywords to preserve in parentheses
KEYWORDS = [
    "SPARKS", "Prompt", "Prompts", "Prompting", "Data Strategies", "Financial Analysis",
    "Data Analytics", "ChatGPT", "Generative AI", "AI", "Machine Learning", "Data",
    "Data Exploration", "Data Storytelling"
]

def pre_process(text):
    # Find Figure/Table captions and insert placeholder
    pattern = re.compile(r'(Figure\s+\d+[\.\d]*\s*:.*?)(?=\n|$)', re.IGNORECASE)
    def repl(m):
        caption = m.group(1)
        return f"\n\n<!-- IMAGE_PLACEHOLDER: [{caption}] -->\n\n{caption}"
    
    text = pattern.sub(repl, text)
    
    pattern2 = re.compile(r'(Table\s+\d+[\.\d]*\s*:.*?)(?=\n|$)', re.IGNORECASE)
    def repl2(m):
        caption = m.group(1)
        return f"\n\n<!-- IMAGE_PLACEHOLDER: [{caption}] -->\n\n{caption}"
    
    text = pattern2.sub(repl2, text)
    
    pattern3 = re.compile(r'(Exhibit\s+\d+[\.\d]*\s*:.*?)(?=\n|$)', re.IGNORECASE)
    def repl3(m):
        caption = m.group(1)
        return f"\n\n<!-- IMAGE_PLACEHOLDER: [{caption}] -->\n\n{caption}"
    
    text = pattern3.sub(repl3, text)
    
    return text

def translate_file(input_path):
    output_path = input_path.replace('.txt', '_vi.txt')
    print(f"Translating {input_path} -> {output_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    text = pre_process(text)

    # Split by double newline to preserve paragraph structure
    paragraphs = text.split("\n\n")
    translator = GoogleTranslator(source='en', target='vi')
    translated_paragraphs = []
    
    for p in paragraphs:
        p = p.strip()
        if not p:
            translated_paragraphs.append("")
            continue
            
        if p.startswith("<!-- IMAGE_PLACEHOLDER:"):
            translated_paragraphs.append(p)
            continue
            
        # Google Translate API has a 5000 char limit
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
    chunks = glob.glob(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\chunk13A_*.txt")
    chunks += glob.glob(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\chunk13B_*.txt")
    chunks = [c for c in chunks if not c.endswith('_vi.txt')]
    
    # Custom sort to ensure we process A1, A2... B1, B2... in order
    def get_sort_key(filename):
        # Extract '13A' or '13B' and the number
        basename = os.path.basename(filename)
        # e.g., chunk13A_1.txt
        parts = basename.split('_')
        prefix = parts[0] # chunk13A
        try:
            num = int(parts[1].split('.')[0])
        except:
            num = 0
        return (prefix, num)
        
    chunks.sort(key=get_sort_key)

    for chunk in chunks:
        translate_file(chunk)

    print("All chunks translated!")
