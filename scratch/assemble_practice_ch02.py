import os

def main():
    base_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting'
    scratch_dir = os.path.join(base_dir, 'scratch')
    out_path = os.path.join(base_dir, 'docs', 'practice_ch02.md')
    
    vi_all = []
    
    # Read chunks 1 to 10
    for i in range(1, 11):
        chunk_path = os.path.join(scratch_dir, f'ch02_tr_chunk_{i}.md')
        if os.path.exists(chunk_path):
            with open(chunk_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                vi_all.append(content)
        else:
            print(f"Warning: {chunk_path} not found.")

    vi_combined = "\n\n".join(vi_all)
    
    pdf_path = "../TaiLieu/textbookForPractice/Ch_02_Foundational Data Analysis Skills.pdf"
    en_embed = f'<object data="{pdf_path}" type="application/pdf" width="100%" height="800px"><p>Trình duyệt của bạn không hỗ trợ xem PDF trực tiếp. Vui lòng tải xuống tệp PDF tại <a href="{pdf_path}">đây</a>.</p></object>'
    
    final_md = "# Chương 2: Các Kỹ năng Phân tích Dữ liệu Nền tảng (Foundational Data Analysis Skills)\n\n"
    final_md += "<!-- tabs:start -->\n"
    final_md += "#### **Tiếng Việt**\n\n"
    final_md += vi_combined + "\n\n"
    final_md += "#### **English**\n\n"
    final_md += en_embed + "\n\n"
    final_md += "<!-- tabs:end -->\n"
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_md)
        
    print(f"Assembled successfully to {out_path}")

if __name__ == '__main__':
    main()
