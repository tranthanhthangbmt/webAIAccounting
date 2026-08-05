import os

docs_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\docs"

for i in range(1, 11):
    ch_str = f"{i:02d}"
    file_path = os.path.join(docs_dir, f"practice_ch{ch_str}.md")
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if we already added it
    if "🎬 Video" in content or "🎦 Slide Bài Giảng" in content:
        print(f"Tabs already exist in {file_path}")
        continue
        
    addition = f"""
#### ** 🎬 Video **

<iframe src="videoPractice/Chapter{ch_str}/index.html" style="width: 100%; aspect-ratio: 16/9; max-height: 75vh; border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);"></iframe>

#### ** 🎦 Slide Bài Giảng **

<object data="TaiLieu/slidePractice/Slide_Practice_Ch{ch_str}.pdf#view=FitH" type="application/pdf" class="pdf-container" width="100%" height="800px">
    <p>Trình duyệt của bạn không hỗ trợ xem PDF nhúng. <a href="TaiLieu/slidePractice/Slide_Practice_Ch{ch_str}.pdf#view=FitH" target="_blank">Nhấn vào đây để tải Slide Bài Giảng</a>.</p>
</object>
<p style="text-align: right;"><a href="TaiLieu/slidePractice/Slide_Practice_Ch{ch_str}.pdf#view=FitH" target="_blank" style="font-weight: bold; color: #0056b3;">📥 Tải về Slide Bài Giảng (PDF)</a></p>

<!-- tabs:end -->"""
    
    # Replace <!-- tabs:end -->
    new_content = content.replace("<!-- tabs:end -->", addition)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Updated {file_path}")
