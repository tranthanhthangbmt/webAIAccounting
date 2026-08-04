import os
import importlib
import sys

def escape_latex(text):
    if text is None:
        return ""
    # Only escape things that aren't already formatted LaTeX. 
    # But wait, our titles might have & which needs escaping, but content will be raw LaTeX.
    # So we only use this for titles.
    return text.replace('_', r'\_').replace('&', r'\&').replace('%', r'\%')

def build_chapter(ch_num):
    ch_str = f"{ch_num:02d}"
    
    try:
        module = importlib.import_module(f"slide_data_ch{ch_str}")
        chapter_title = module.chapter_title
        chapter_subtitle = module.chapter_subtitle
        slides_data = module.slides
        
        # Ensure title_slide is first, and "Intro" slides immediately follow
        title_slides = [s for s in slides_data if s.get("type") == "title_slide"]
        intro_slides = [s for s in slides_data if str(s.get("title", "")).startswith("Intro ")]
        
        if not title_slides:
            title_slides = [{"type": "title_slide"}]
            
        other_slides = [s for s in slides_data if s.get("type") != "title_slide" and not str(s.get("title", "")).startswith("Intro ")]
        
        slides_data = title_slides + intro_slides + other_slides
    except ImportError:
        print(f"Error: Could not find slide_data_ch{ch_str}.py")
        return

    out_path = fr"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slidePractice\Slide_Practice_Ch{ch_str}.tex"
    img_dir = fr"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\textbookForPractice\Figures\Ch_{ch_str}"
    
    # Get all images in directory
    all_images = []
    if os.path.exists(img_dir):
        for f in os.listdir(img_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                all_images.append(f)
    all_images.sort()
    
    used_images = set()

    latex_content = r"""\documentclass[aspectratio=169,12pt]{beamer}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage{lmodern}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{multicol}
\usepackage{tikz}
\usepackage{xcolor}

\usetheme{Madrid}
\usefonttheme{professionalfonts}

% --- Custom Colors & Settings ---
\definecolor{UBrandBlue}{RGB}{0, 71, 155}
\definecolor{UBrandGold}{RGB}{255, 184, 28}
\setbeamercolor{palette primary}{bg=UBrandBlue,fg=white}
\setbeamercolor{palette secondary}{bg=UBrandGold,fg=black}
\setbeamercolor{palette tertiary}{bg=UBrandBlue!80!black,fg=white}
\setbeamercolor{title}{bg=UBrandBlue,fg=white}
\setbeamercolor{item}{fg=UBrandBlue}

"""

    latex_content += f"""
\\title[Thực hành - Chương {ch_str}]{{{chapter_title}}}
\\subtitle{{{chapter_subtitle}}}
\\author[Giảng viên]{{Trí tuệ Nhân tạo cho Kế toán (AI in Accounting)}}
\\institute[Đại học]{{Khoa Kế toán - Kiểm toán}}
\\date{{Bài giảng Thực hành {ch_str}}}

\\begin{{document}}
"""

    for slide in slides_data:
        stype = slide.get("type", "normal")
        title = slide.get("title", "")
        content = slide.get("content", "")
        
        if stype == "title_slide":
            latex_content += r"""
\begin{frame}
    \titlepage
\end{frame}
"""
        elif stype == "normal":
            latex_content += f"""
\\begin{{frame}}{{{escape_latex(title)}}}
{content}
\\end{{frame}}
"""
        elif stype == "image":
            img = slide.get("image")
            if img: used_images.add(img)
            img_path = f"../textbookForPractice/Figures/Ch_{ch_str}/{img}" if img else ""
            
            latex_content += f"""
\\begin{{frame}}{{{escape_latex(title)}}}
"""
            if content:
                latex_content += f"""
    \\begin{{columns}}
        \\begin{{column}}{{0.45\\textwidth}}
{content}
        \\end{{column}}
        \\begin{{column}}{{0.55\\textwidth}}
            \\begin{{figure}}[h]
                \\centering
                \\includegraphics[width=\\textwidth,height=0.75\\textheight,keepaspectratio]{{{img_path}}}
            \\end{{figure}}
        \\end{{column}}
    \\end{{columns}}
"""
            else:
                latex_content += f"""
    \\begin{{figure}}[h]
        \\centering
        \\includegraphics[width=0.95\\textwidth,height=0.75\\textheight,keepaspectratio]{{{img_path}}}
    \\end{{figure}}
"""
            latex_content += "\\end{frame}\n"
            
        elif stype == "double_image":
            img1 = slide.get("image1")
            img2 = slide.get("image2")
            if img1: used_images.add(img1)
            if img2: used_images.add(img2)
            
            path1 = f"../textbookForPractice/Figures/Ch_{ch_str}/{img1}" if img1 else ""
            path2 = f"../textbookForPractice/Figures/Ch_{ch_str}/{img2}" if img2 else ""
            
            latex_content += f"""
\\begin{{frame}}{{{escape_latex(title)}}}
    \\begin{{columns}}
        \\begin{{column}}{{0.5\\textwidth}}
            \\begin{{figure}}[h]
                \\centering
                \\includegraphics[width=\\textwidth,height=0.7\\textheight,keepaspectratio]{{{path1}}}
            \\end{{figure}}
        \\end{{column}}
        \\begin{{column}}{{0.5\\textwidth}}
            \\begin{{figure}}[h]
                \\centering
                \\includegraphics[width=\\textwidth,height=0.7\\textheight,keepaspectratio]{{{path2}}}
            \\end{{figure}}
        \\end{{column}}
    \\end{{columns}}
\\end{{frame}}
"""

    # Generate slides for remaining images
    remaining_images = [img for img in all_images if img not in used_images]
    single_images = []
    double_images = []
    
    for img in remaining_images:
        prefix = img.split(' ')[0].upper()
        if prefix in ['BE', 'EX', 'PAC', 'PR', 'ERD']:
            double_images.append(img)
        else:
            single_images.append(img)

    for img in single_images:
        title_escaped = escape_latex(os.path.splitext(img)[0])
        img_path = f"../textbookForPractice/Figures/Ch_{ch_str}/{img}"
        latex_content += f"""
\\begin{{frame}}{{{title_escaped}}}
    \\begin{{figure}}[h]
        \\centering
        \\includegraphics[width=0.95\\textwidth,height=0.75\\textheight,keepaspectratio]{{{img_path}}}
    \\end{{figure}}
\\end{{frame}}
"""

    for i in range(0, len(double_images), 2):
        img1 = double_images[i]
        title1 = escape_latex(os.path.splitext(img1)[0])
        path1 = f"../textbookForPractice/Figures/Ch_{ch_str}/{img1}"
        
        if i + 1 < len(double_images):
            img2 = double_images[i+1]
            title2 = escape_latex(os.path.splitext(img2)[0])
            path2 = f"../textbookForPractice/Figures/Ch_{ch_str}/{img2}"
            
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
        \\includegraphics[width=0.95\\textwidth,height=0.75\\textheight,keepaspectratio]{{{path1}}}
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
    print(f"Generated {out_path} with {len(slides_data)} defined slides and {len(remaining_images)} auto-generated image slides.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        build_chapter(int(sys.argv[1]))
    else:
        for i in range(3, 11):
            build_chapter(i)
