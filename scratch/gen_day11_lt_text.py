import docx
import os

files = [
    'textbook_Chapters_v2/Day_11_Accounting AI - Chapter 9_AI-Based Tax Planning and Compliance.docx',
    'textbook_Chapters_v2/Day_11_Luật Quản lý thuế, Thông tư 200.docx'
]

with open('scratch/day11_lt_text.txt', 'w', encoding='utf-8') as f:
    for file in files:
        f.write(f'--- File: {file} ---\n')
        try:
            doc = docx.Document(file)
            for para in doc.paragraphs:
                f.write(para.text + '\n')
        except Exception as e:
            f.write(f'Error reading {file}: {e}\n')
print("Done")
