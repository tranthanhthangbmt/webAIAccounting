import re

def find_los():
    with open('scratch/ch02_raw.txt', encoding='utf-8') as f:
        text = f.read()
    pages = text.split('--- PAGE ')
    
    keywords = [r'LEARNING OBJECTIVE', r'Chapter Review']
    
    for i, p in enumerate(pages):
        if i < 2: continue
        for kw in keywords:
            if re.search(kw, p[:2000], re.I):
                print(f"Page {i}: Match found for {kw}")

if __name__ == "__main__":
    find_los()
