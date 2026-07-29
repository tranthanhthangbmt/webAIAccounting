import sys, re

def escape_tex(text):
    text = text.replace(r'\&', '&')
    text = text.replace(r'\_', '_')
    text = text.replace(r'\%', '%')
    text = text.replace('&', r'\&')
    text = text.replace('_', r'\_')
    text = text.replace('%', r'\%')
    # handle **bold** -> \textbf{bold}
    text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
    # handle images: ![alt](path)
    text = re.sub(r'!\[.*?\]\((.*?)\)', r'\\begin{center}\\includegraphics[width=0.7\\textwidth,height=0.6\\textheight,keepaspectratio]{\1}\\end{center}', text)
    return text

def convert(md_file, tex_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tex_content = []
    
    # Extract title from the first `# ` header if available
    title = "Trí tuệ Nhân tạo cho Kế toán"
    subtitle = "Bài Giảng"
    for line in lines:
        if line.startswith('# '):
            subtitle = line[2:].strip()
            break

    title_tex = escape_tex(title)
    subtitle_tex = escape_tex(subtitle)

    tex_content.append(r'''\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}
\usecolortheme{default}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{booktabs}

\setbeamertemplate{caption}[numbered]
\renewcommand{\figurename}{Hình}

\title[''' + title_tex + r''']{Trí tuệ Nhân tạo cho Kế toán \\ \vspace{0.3cm} \Large ''' + subtitle_tex + r'''}
\author{Đại học Đông Á}
\date{\today}

\begin{document}

% SLIDE 1
\begin{frame}
    \titlepage
\end{frame}

% SLIDE 2
\begin{frame}{Nội dung Bài học}
    \tableofcontents
\end{frame}

''')

    in_slide = False
    slide_items = []
    
    def flush_slide():
        if in_slide:
            has_items = any(item.startswith('- ') for item in slide_items)
            if has_items:
                itemizing = False
                for item in slide_items:
                    if item.startswith('- '):
                        if not itemizing:
                            tex_content.append(r'    \begin{itemize}')
                            itemizing = True
                        tex_content.append(r'        \item ' + escape_tex(item[2:]))
                    elif item.startswith('!['):
                        if itemizing:
                            tex_content.append(r'    \end{itemize}')
                            itemizing = False
                        tex_content.append(r'    ' + escape_tex(item))
                    else:
                        if itemizing:
                            tex_content.append(r'        ' + escape_tex(item))
                        else:
                            tex_content.append(r'    ' + escape_tex(item) + r'\\')
                if itemizing:
                    tex_content.append(r'    \end{itemize}')
            else:
                for item in slide_items:
                    tex_content.append(r'    ' + escape_tex(item) + r'\\')
            tex_content.append(r'\end{frame}' + '\n\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith('---') or line.startswith('theme:') or line.startswith('title:') or line.startswith('author:') or line.startswith('date:'):
            continue

        if line.startswith('# '):
            flush_slide()
            in_slide = False
            sec_title = line[2:]
            tex_content.append(r'\section{' + escape_tex(sec_title) + '}')
            tex_content.append('\n')
        elif line.startswith('## '):
            flush_slide()
            in_slide = True
            slide_items = []
            slide_title = line[3:]
            tex_content.append(r'\begin{frame}{' + escape_tex(slide_title) + '}')
        elif in_slide:
            slide_items.append(line)

    flush_slide()

    tex_content.append(r'\end{document}')

    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(tex_content))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        convert(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python md2tex_v2.py input.md output.tex")
