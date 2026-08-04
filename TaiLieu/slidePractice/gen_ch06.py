import os
import re

# We will generate slide_data_ch06.py directly by interleaving text and images.
chapter_title = "Mô hình hóa Thông tin"
chapter_subtitle = "Analysis: Information Modeling"

normal_slides = [
    {
        "type": "title_slide"
    },
    {
        "type": "normal",
        "title": "Góc nhìn Chuyên gia (Professional Insight)",
        "content": r"""\begin{itemize}
    \item \textbf{Mô hình hóa Thông tin:} Không chỉ đơn giản là việc liên kết các bảng dữ liệu, mà là nghệ thuật cấu trúc hóa dữ liệu để trả lời chính xác các câu hỏi kinh doanh.
    \item \textbf{Khả năng mở rộng (Scalability):} Một mô hình dữ liệu tốt (ví dụ: Star Schema) cho phép báo cáo chạy nhanh hơn, dễ bảo trì hơn và hạn chế rủi ro sai lệch dữ liệu.
    \item \textbf{Tư duy Hệ thống:} Kế toán viên hiện đại cần tư duy giống như một Data Architect để xây dựng nền tảng vững chắc cho mọi phân tích phía sau.
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Lộ trình Chương (Chapter Roadmap)",
        "content": r"""\begin{itemize}
    \item \textbf{LO 6.1:} Khái niệm Nền tảng của Mô hình hóa Thông tin.
    \item \textbf{LO 6.2:} Áp dụng Các Thuật toán Mô hình hóa Thông tin (7 Mẫu cơ bản).
    \item \textbf{LO 6.3:} Sáu Mẫu Mô hình hóa cho Cấu trúc Dữ liệu Kế toán (Star Schema).
\end{itemize}"""
    },
    
    # LO 6.1
    {
        "type": "normal",
        "title": "6.1 Mô hình hóa Thông tin là gì?",
        "content": r"""\begin{itemize}
    \item \textbf{Định nghĩa:} Là quá trình cấu trúc và sắp xếp lại dữ liệu thô thành thông tin có ý nghĩa thông qua các thuật toán và mối quan hệ giữa các bảng.
    \item \textbf{Quy trình Mô hình hóa (The Information Modeling Process):} Chuyển từ Dữ liệu (Data) $\rightarrow$ Thuật toán (Algorithms) $\rightarrow$ Thông tin (Information).
    \item \textbf{Mục tiêu:} Đảm bảo tính toàn vẹn, tính nhất quán và dễ dàng truy xuất thông tin phục vụ cho Bảng điều khiển (Dashboards) và Báo cáo.
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Thuật toán và Phương pháp tiếp cận",
        "content": r"""\begin{itemize}
    \item \textbf{Thuật toán (Algorithms):} Là tập hợp các quy tắc tính toán (ví dụ: Tính biên lợi nhuận = Doanh thu - Giá vốn).
    \item \textbf{Phương pháp tiếp cận có cấu trúc (Structured Approach):} 
    \begin{itemize}
        \item Hiểu rõ yêu cầu đầu ra (Output).
        \item Xác định dữ liệu đầu vào (Input).
        \item Xây dựng các bước xử lý logic (Processing).
    \end{itemize}
\end{itemize}"""
    },
    
    # LO 6.2
    {
        "type": "normal",
        "title": "6.2 Bảy Mẫu Thuật toán Mô hình hóa Thông tin",
        "content": r"""\begin{itemize}
    \item \textbf{Mẫu 1 - Tính toán Cơ bản:} Cộng, trừ, nhân, chia (ví dụ: Tổng Doanh thu).
    \item \textbf{Mẫu 2 - Logic và Điều kiện (Logic/Conditional):} Hàm IF, CASE WHEN (ví dụ: Phân loại Nợ xấu nếu quá hạn 90 ngày).
    \item \textbf{Mẫu 3 - Xử lý Văn bản (Text):} Nối chuỗi, tách chuỗi, làm sạch văn bản (ví dụ: Tách Mã Vùng từ Số Điện thoại).
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Các Mẫu Thuật toán tiếp theo",
        "content": r"""\begin{itemize}
    \item \textbf{Mẫu 4 - Thời gian (Date/Time):} Trích xuất Tháng, Năm, Quý (ví dụ: Doanh thu theo Quý).
    \item \textbf{Mẫu 5 - Hàm Tài chính (Financial):} Tính PV, FV, NPV, IRR.
    \item \textbf{Mẫu 6 - Tỷ suất (Ratios):} Tính ROA, ROE, Current Ratio.
    \item \textbf{Mẫu 7 - Hàm Phức hợp (Complex/Nested):} Kết hợp nhiều hàm với nhau.
\end{itemize}"""
    },
    
    # LO 6.3
    {
        "type": "normal",
        "title": "6.3 Sáu Mẫu Cấu trúc Dữ liệu Kế toán",
        "content": r"""\begin{itemize}
    \item \textbf{Mẫu 1 - Hệ thống Tài khoản (Chart of Accounts):} Bảng danh mục cốt lõi của mọi hệ thống kế toán.
    \item \textbf{Mẫu 2 - Dữ liệu Giao dịch (Transactions):} Bảng Fact chứa các bút toán nhật ký (Sổ cái).
    \item \textbf{Mẫu 3 - Danh mục Thực thể (Entity/Master Data):} Khách hàng, Nhà cung cấp, Sản phẩm, Nhân viên.
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Cấu trúc Dữ liệu (Tiếp theo)",
        "content": r"""\begin{itemize}
    \item \textbf{Mẫu 4 - Ngân sách so với Thực tế (Budget vs Actual):} Kết nối bảng kế hoạch và bảng thực tế để phân tích chênh lệch (Variance Analysis).
    \item \textbf{Mẫu 5 - Bảng Thời gian (Time Dimension):} Cực kỳ quan trọng để phân tích xu hướng (Time Intelligence) trong Power BI / Tableau.
    \item \textbf{Mẫu 6 - Sổ cái và Sổ chi tiết (General \& Subsidiary Ledgers):} Mối quan hệ 1-N (One-to-Many) giữa Sổ cái tổng hợp và các Sổ chi tiết (Phải thu, Phải trả, Hàng tồn kho).
\end{itemize}"""
    }
]

# Fetch images
img_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\textbookForPractice\Figures\Ch_06"
all_images = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Sort correctly
def exact_sort_key(x):
    name = os.path.splitext(x)[0]
    parts = re.findall(r'\d+', name)
    return [int(p) for p in parts]

all_images = sorted(all_images, key=exact_sort_key)

image_slides = []
be_ex_pac_slides = []

for img in all_images:
    title = os.path.splitext(img)[0].replace('&', ' & ')
    if img.startswith("ILLUSTRATION"):
        image_slides.append({
            "type": "image",
            "title": title,
            "image": img
        })
    elif img.startswith("Apply It") or img.startswith("DTunes") or img.startswith("LO") or img.startswith("Fig"):
        be_ex_pac_slides.append({
            "type": "image",
            "title": title,
            "image": img
        })

# Be Ex Pac double images
be_imgs = [img for img in all_images if img.startswith("BE ")]
ex_imgs = [img for img in all_images if img.startswith("EX ")]
pac_imgs = [img for img in all_images if img.startswith("PAC ")]

be_ex_pac_final = []

# Title slides for sections
be_ex_pac_final.append({
    "type": "normal",
    "title": "Bài tập Ngắn (Brief Exercises)",
    "content": r"""\begin{center}
    \Huge \textbf{Phần Bài tập Ngắn} \\
    \vspace{0.5cm}
    \Large Brief Exercises (BE)
\end{center}"""
})
for i in range(0, len(be_imgs), 2):
    if i+1 < len(be_imgs):
        title = f"{os.path.splitext(be_imgs[i])[0]} & {os.path.splitext(be_imgs[i+1])[0]}"
        be_ex_pac_final.append({
            "type": "double_image",
            "title": title,
            "image1": be_imgs[i],
            "image2": be_imgs[i+1]
        })
    else:
        be_ex_pac_final.append({
            "type": "image",
            "title": os.path.splitext(be_imgs[i])[0],
            "image": be_imgs[i]
        })

be_ex_pac_final.append({
    "type": "normal",
    "title": "Bài tập (Exercises)",
    "content": r"""\begin{center}
    \Huge \textbf{Phần Bài tập} \\
    \vspace{0.5cm}
    \Large Exercises (EX)
\end{center}"""
})
for i in range(0, len(ex_imgs), 2):
    if i+1 < len(ex_imgs):
        title = f"{os.path.splitext(ex_imgs[i])[0]} & {os.path.splitext(ex_imgs[i+1])[0]}"
        be_ex_pac_final.append({
            "type": "double_image",
            "title": title,
            "image1": ex_imgs[i],
            "image2": ex_imgs[i+1]
        })
    else:
        be_ex_pac_final.append({
            "type": "image",
            "title": os.path.splitext(ex_imgs[i])[0],
            "image": ex_imgs[i]
        })

be_ex_pac_final.append({
    "type": "normal",
    "title": "Tình huống Ứng dụng (PAC)",
    "content": r"""\begin{center}
    \Huge \textbf{Tình huống Ứng dụng Chuyên môn} \\
    \vspace{0.5cm}
    \Large Professional Application Cases (PAC)
\end{center}"""
})
for i in range(0, len(pac_imgs), 2):
    if i+1 < len(pac_imgs):
        title = f"{os.path.splitext(pac_imgs[i])[0]} & {os.path.splitext(pac_imgs[i+1])[0]}"
        be_ex_pac_final.append({
            "type": "double_image",
            "title": title,
            "image1": pac_imgs[i],
            "image2": pac_imgs[i+1]
        })
    else:
        be_ex_pac_final.append({
            "type": "image",
            "title": os.path.splitext(pac_imgs[i])[0],
            "image": pac_imgs[i]
        })

be_ex_pac_final.extend(be_ex_pac_slides)

# Group normal slides by section
sections = []
current_section = []
for slide in normal_slides:
    if slide.get("title", "").startswith("6."):
        if current_section:
            sections.append(current_section)
        current_section = [slide]
    else:
        current_section.append(slide)
if current_section:
    sections.append(current_section)

# Sections: 0 (intro), 1 (LO 6.1), 2 (LO 6.2), 3 (LO 6.3)
lo_sections = sections[1:]
images_per_lo = len(image_slides) // len(lo_sections)
image_chunks = [image_slides[i:i + images_per_lo] for i in range(0, len(image_slides), images_per_lo)]
if len(image_chunks) > len(lo_sections):
    image_chunks[-2].extend(image_chunks[-1])
    image_chunks.pop()

new_slides = []
new_slides.extend(sections[0])

for i, lo_section in enumerate(lo_sections):
    chunk_images = image_chunks[i] if i < len(image_chunks) else []
    images_per_text = len(chunk_images) // len(lo_section)
    remainder = len(chunk_images) % len(lo_section)
    
    img_idx = 0
    for j, text_slide in enumerate(lo_section):
        new_slides.append(text_slide)
        count = images_per_text + (1 if j < remainder else 0)
        for _ in range(count):
            if img_idx < len(chunk_images):
                new_slides.append(chunk_images[img_idx])
                img_idx += 1

new_slides.extend(be_ex_pac_final)

# Write out slide_data_ch06.py
out_path = "slide_data_ch06.py"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(f'chapter_title = {repr(chapter_title)}\n')
    f.write(f'chapter_subtitle = {repr(chapter_subtitle)}\n\n')
    f.write('slides = [\n')
    
    for slide in new_slides:
        f.write('    {\n')
        for k, v in slide.items():
            if k == "content":
                f.write(f'        "{k}": r"""{v}""",\n')
            else:
                f.write(f'        "{k}": "{v}",\n')
        f.write('    },\n')
    f.write(']\n')

print("Wrote slide_data_ch06.py successfully.")
