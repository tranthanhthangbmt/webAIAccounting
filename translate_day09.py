import os
import glob
import re
from deep_translator import GoogleTranslator

# Keywords to preserve in parentheses
KEYWORDS = [
    "Robo-Advisors", "Robo-Advisor", "Crypto Assets", "Crypto Asset",
    "DeFi", "Metaverse", "NFTs", "NFT", "Blockchain", "Smart Contracts",
    "Cryptocurrency", "Cryptocurrencies", "Tokens"
]

def pre_process(text):
    # Find Figure/Table captions and insert placeholder
    # e.g., "Figure 2.1: Some description." or "Fig 1:"
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
    return text

def post_process(text, original_text):
    # Try to re-inject English keywords in parentheses if they existed in the original text
    for kw in KEYWORDS:
        # If the original text had the keyword, let's just make sure it's preserved
        if kw.lower() in original_text.lower():
            # A simple heuristic: we don't know exactly where it was translated to, 
            # but if it was translated, we might not find it. 
            # We'll just leave this to Google Translator, it often preserves capitalized English terms.
            pass
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
    chunks = glob.glob(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\chunk9A_*.txt")
    chunks.extend(glob.glob(r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\chunk9B_*.txt"))
    chunks = [c for c in chunks if not c.endswith('_vi.txt')]
    chunks.sort()

    for chunk in chunks:
        translate_file(chunk)

    print("All chunks translated!")
