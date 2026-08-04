import os

chapters = {
    3: ("Động lực và Mục tiêu Phân tích Dữ liệu", "Motivations and Objectives for Data Analysis"),
    4: ("Lập Kế hoạch Dữ liệu và Chiến lược Phân tích", "Planning Data and Analysis Strategies"),
    5: ("Chuẩn bị Dữ liệu", "Analysis: Data Preparation"),
    6: ("Mô hình hóa Thông tin", "Analysis: Information Modeling"),
    7: ("Khám phá Dữ liệu", "Analysis: Data Exploration"),
    8: ("Diễn giải Kết quả Phân tích Dữ liệu", "Interpreting Data Analysis Results"),
    9: ("Trình bày Kết quả Phân tích Dữ liệu", "Communicating Data Analysis Results"),
    10: ("Các Xu hướng Dữ liệu và Phân tích Mới nhất", "Recent Data and Analyses Developments")
}

for ch, (title, subtitle) in chapters.items():
    ch_str = f"{ch:02d}"
    out_path = fr"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slidePractice\Slide_Practice_Ch{ch_str}.tex"
    img_dir = fr"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\textbookForPractice\Figures\Ch_{ch_str}"
    
    script_content = f'''import os

CH_NUM = {ch}
CH_TITLE = "{title}"
CH_SUBTITLE = "{subtitle}"

out_path = r"{out_path}"
img_dir = r"{img_dir}"

def escape_latex(text):
    return text.replace('_', r'\_').replace('&', r'\&').replace('%', r'\%')

images = []
if os.path.exists(img_dir):
    for f in os.listdir(img_dir):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            images.append(f)
            
images.sort()

single_images = []
double_images = []

for img in images:
    prefix = img.split(' ')[0].upper()
    if prefix in ['BE', 'EX', 'PAC', 'PR', 'ERD']:
        double_images.append(img)
    else:
        single_images.append(img)

latex_content = r"""\\documentclass[aspectratio=169,12pt]{{beamer}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T5]{{fontenc}}
\\usepackage[vietnamese]{{babel}}
\\usepackage{{lmodern}}
\\usepackage{{graphicx}}
\\usepackage{{booktabs}}
\\usepackage{{tabularx}}
\\usepackage{{multicol}}
\\usepackage{{tikz}}
\\usepackage{{xcolor}}

\\usetheme{{Madrid}}
\\usefonttheme{{professionalfonts}}

% --- Custom Colors & Settings ---
\\definecolor{{UBrandBlue}}{{RGB}}{{0, 71, 155}}
\\definecolor{{UBrandGold}}{{RGB}}{{255, 184, 28}}
\\setbeamercolor{{palette primary}}{{bg=UBrandBlue,fg=white}}
\\setbeamercolor{{palette secondary}}{{bg=UBrandGold,fg=black}}
\\setbeamercolor{{palette tertiary}}{{bg=UBrandBlue!80!black,fg=white}}
\\setbeamercolor{{title}}{{bg=UBrandBlue,fg=white}}
\\setbeamercolor{{item}}{{fg=UBrandBlue}}

\\title[Thực hành - Chương {ch_str}]{{""" + CH_TITLE + r"""}}
\\subtitle{{""" + CH_SUBTITLE + r"""}}
\\author[Giảng viên]{{Trí tuệ Nhân tạo cho Kế toán (AI in Accounting)}}
\\institute[Đại học]{{Khoa Kế toán - Kiểm toán}}
\\date{{Bài giảng Thực hành {ch_str}}}

\\begin{{document}}

% Slide 1: Title
\\begin{{frame}}
    \\titlepage
\\end{{frame}}

% Slide 2: Mục tiêu
\\begin{{frame}}{{Tổng quan Chương (Chapter Preview)}}
    \\begin{{itemize}}
        \\item \\textbf{{Mục tiêu:}} Giới thiệu và thực hành các khái niệm trọng tâm của Chương {ch_str}.
        \\item \\textbf{{Nội dung chính:}} Tham khảo chi tiết trong giáo trình và tóm tắt kế hoạch.
        \\item Các slide tiếp theo sẽ minh họa chi tiết các khái niệm, quy trình và bài tập thực hành.
    \\end{{itemize}}
\\end{{frame}}

"""

for img in single_images:
    title_escaped = escape_latex(os.path.splitext(img)[0])
    img_path = f"../textbookForPractice/Figures/Ch_{ch_str}/{img}"
    latex_content += f"""
\\begin{{frame}}{{{{title_escaped}}}}
    \\begin{{figure}}[h]
        \\centering
        \\includegraphics[height=0.75\\textheight,keepaspectratio]{{{img_path}}}
        \\caption{{{{title_escaped}}}}
    \\end{{figure}}
\\end{{frame}}
"""

for i in range(0, len(double_images), 2):
    img1 = double_images[i]
    title1 = escape_latex(os.path.splitext(img1)[0])
    path1 = f"../textbookForPractice/Figures/Ch_{ch_str}/{{img1}}"
    
    if i + 1 < len(double_images):
        img2 = double_images[i+1]
        title2 = escape_latex(os.path.splitext(img2)[0])
        path2 = f"../textbookForPractice/Figures/Ch_{ch_str}/{{img2}}"
        
        frame_title = f"{{title1}} \\& {{title2}}"
        frame_title = f"{title1} \\& {title2}"
        latex_content += f"""
\\begin{{frame}}{{{frame_title}}}
    \\begin{{columns}}
        \\begin{{column}}{{0.5\\textwidth}}
            \\begin{{figure}}[h]
                \\centering
                \\includegraphics[width=\\textwidth,height=0.7\\textheight,keepaspectratio]{{{path1}}}
                \\caption{{{title1}}}
            \\end{{figure}}
        \\end{{column}}
        \\begin{{column}}{{0.5\\textwidth}}
            \\begin{{figure}}[h]
                \\centering
                \\includegraphics[width=\\textwidth,height=0.7\\textheight,keepaspectratio]{{{path2}}}
                \\caption{{{title2}}}
            \\end{{figure}}
        \\end{{column}}
    \\end{{columns}}
\\end{{frame}}
"""
    else:
        frame_title = title1
        latex_content += f"""
\\begin{{frame}}{{{frame_title}}}
    \\begin{{figure}}[h]
        \\centering
        \\includegraphics[height=0.75\\textheight,keepaspectratio]{{{path1}}}
        \\caption{{{title1}}}
    \\end{{figure}}
\\end{{frame}}
"""

latex_content += r"""
\begin{frame}{Kết thúc}
    \begin{center}
        \Huge \textbf{Hỏi \& Đáp} \\
        \vspace{1cm}
        \Large Cảm ơn các bạn đã lắng nghe!
    \end{center}
\end{frame}

\end{document}
"""

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(latex_content)
    
print(f"Created Slide_Practice_Ch{ch_str}.tex successfully.")
'''
    script_path = fr"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slidePractice\gen_slide_ch{ch_str}.py"
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script_content)

print("Generated all gen scripts.")
