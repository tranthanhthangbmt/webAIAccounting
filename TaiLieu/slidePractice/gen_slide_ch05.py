import os
import glob

CH_NUM = 5
CH_TITLE = "Chuẩn bị Dữ liệu"
CH_SUBTITLE = "Analysis: Data Preparation"

out_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slidePractice\Slide_Practice_Ch05.tex"
img_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\textbookForPractice\Figures\Ch_05"

# Escape special characters for latex
def escape_latex(text):
    return text.replace('_', r'\_').replace('&', r'\&').replace('%', r'\%')

# Get all images
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

\title[Thực hành - Chương """ + f"{CH_NUM:02d}" + r"""]{""" + CH_TITLE + r"""}
\subtitle{""" + CH_SUBTITLE + r"""}
\author[Giảng viên]{Trí tuệ Nhân tạo cho Kế toán (AI in Accounting)}
\institute[Đại học]{Khoa Kế toán - Kiểm toán}
\date{Bài giảng Thực hành """ + f"{CH_NUM:02d}" + r"""}

\begin{document}

% Slide 1: Title
\begin{frame}
    \titlepage
\end{frame}

% Slide 2: Mục tiêu
\begin{frame}{Tổng quan Chương (Chapter Preview)}
    \begin{itemize}
        \item \textbf{Mục tiêu:} Giới thiệu và thực hành các khái niệm trọng tâm của Chương """ + f"{CH_NUM:02d}" + r""".
        \item \textbf{Nội dung chính:} Tham khảo chi tiết trong giáo trình và tóm tắt kế hoạch.
        \item Các slide tiếp theo sẽ minh họa chi tiết các khái niệm, quy trình và bài tập thực hành.
    \end{itemize}
\end{frame}

"""

# Add single images
for img in single_images:
    title = escape_latex(os.path.splitext(img)[0])
    img_path = f"../textbookForPractice/Figures/Ch_{CH_NUM:02d}/{img}"
    latex_content += r"""
\begin{frame}{""" + title + r"""}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{" """[0:1] + img_path + r""""}
        \caption{""" + title + r"""}
    \end{figure}
\end{frame}
"""

# Add double images (2 per slide)
for i in range(0, len(double_images), 2):
    img1 = double_images[i]
    title1 = escape_latex(os.path.splitext(img1)[0])
    path1 = f"../textbookForPractice/Figures/Ch_{CH_NUM:02d}/{img1}"
    
    if i + 1 < len(double_images):
        img2 = double_images[i+1]
        title2 = escape_latex(os.path.splitext(img2)[0])
        path2 = f"../textbookForPractice/Figures/Ch_{CH_NUM:02d}/{img2}"
        
        frame_title = f"{title1} \\& {title2}"
        latex_content += r"""
\begin{frame}{""" + frame_title + r"""}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \begin{figure}[h]
                \centering
                \includegraphics[width=\textwidth,height=0.7\textheight,keepaspectratio]{" """[0:1] + path1 + r""""}
                \caption{""" + title1 + r"""}
            \end{figure}
        \end{column}
        \begin{column}{0.5\textwidth}
            \begin{figure}[h]
                \centering
                \includegraphics[width=\textwidth,height=0.7\textheight,keepaspectratio]{" """[0:1] + path2 + r""""}
                \caption{""" + title2 + r"""}
            \end{figure}
        \end{column}
    \end{columns}
\end{frame}
"""
    else:
        frame_title = f"{title1}"
        latex_content += r"""
\begin{frame}{""" + frame_title + r"""}
    \begin{figure}[h]
        \centering
        \includegraphics[height=0.75\textheight,keepaspectratio]{" """[0:1] + path1 + r""""}
        \caption{""" + title1 + r"""}
    \end{figure}
\end{frame}
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
    
print(f"Created Slide_Practice_Ch{CH_NUM:02d}.tex successfully.")
