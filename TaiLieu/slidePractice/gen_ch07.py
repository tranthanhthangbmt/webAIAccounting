import os
import re

# Generate slide_data_ch07.py by interleaving text and images.
chapter_title = "Khám phá Dữ liệu"
chapter_subtitle = "Analysis: Data Exploration"

normal_slides = [
    {
        "type": "title_slide"
    },
    {
        "type": "normal",
        "title": "Góc nhìn Chuyên gia (Professional Insight)",
        "content": r"""\begin{itemize}
    \item \textbf{Tầm quan trọng:} Khám phá dữ liệu là bước đầu tiên để "làm quen" với dữ liệu. Kế toán viên cần hiểu rõ dữ liệu của mình trước khi đưa ra bất kỳ kết luận hay báo cáo nào.
    \item \textbf{Trực giác Kế toán:} Kết hợp kinh nghiệm thực tiễn và kỹ năng phân tích để phát hiện ra các điểm bất thường, xu hướng hoặc insight tiềm ẩn.
    \item \textbf{Kể chuyện bằng dữ liệu (Data Storytelling):} Một biểu đồ trực quan tốt có giá trị hơn hàng ngàn con số trong bảng tính phức tạp.
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Lộ trình Chương (Chapter Roadmap)",
        "content": r"""\begin{itemize}
    \item \textbf{LO 7.1:} Quy trình Khám phá Dữ liệu.
    \item \textbf{LO 7.2:} Khám phá Mối quan hệ Nền tảng qua 8 Mẫu Trực quan hóa.
    \item \textbf{LO 7.3:} Khám phá Dữ liệu bằng cách Tích hợp Mối quan hệ (Dashboards).
\end{itemize}"""
    },
    
    # LO 7.1
    {
        "type": "normal",
        "title": "7.1 Khám phá Dữ liệu (Data Exploration) là gì?",
        "content": r"""\begin{itemize}
    \item \textbf{Định nghĩa:} Là quá trình phân tích dữ liệu ban đầu bằng các công cụ trực quan và thống kê để hiểu rõ đặc điểm, phát hiện xu hướng và kiểm tra các giả định.
    \item \textbf{Sự khác biệt:}
    \begin{itemize}
        \item \textbf{Khám phá (Exploration):} Tự do tìm kiếm insight (cho chính bạn).
        \item \textbf{Diễn giải (Interpretation):} Hiểu ý nghĩa của insight.
        \item \textbf{Báo cáo (Reporting):} Trình bày insight cho người khác (Management/Stakeholders).
    \end{itemize}
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Quy trình Khám phá Dữ liệu",
        "content": r"""\begin{itemize}
    \item \textbf{Bước 1: Xác định Mục tiêu (Identify Objectives):} Bạn đang tìm kiếm điều gì?
    \item \textbf{Bước 2: Lựa chọn Biến (Select Variables):} Dữ liệu nào cần thiết?
    \item \textbf{Bước 3: Khám phá Trực quan (Visual Exploration):} Sử dụng biểu đồ.
    \item \textbf{Bước 4: Đánh giá \& Tinh chỉnh (Evaluate \& Refine):} Biểu đồ có ý nghĩa không? Có cần thay đổi không?
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Công cụ Khám phá Dữ liệu",
        "content": r"""\begin{itemize}
    \item \textbf{PivotTables trong Excel:} Công cụ cơ bản, nhanh chóng và phổ biến nhất để nhóm, tóm tắt và lọc dữ liệu.
    \item \textbf{Đa nền tảng (Across Tools):} Các công cụ BI hiện đại (Power BI, Tableau) cung cấp khả năng trực quan hóa mạnh mẽ hơn, hỗ trợ tương tác và xử lý dữ liệu lớn (Big Data).
    \item \textbf{Mục tiêu cốt lõi:} Tìm ra các \textit{Insights} ẩn giấu đằng sau những con số tài chính khô khan.
\end{itemize}"""
    },
    
    # LO 7.2
    {
        "type": "normal",
        "title": "7.2 Mối quan hệ Nền tảng qua Trực quan hóa",
        "content": r"""\begin{itemize}
    \item \textbf{Mục đích:} Giúp não bộ con người nhanh chóng nhận diện quy luật (Pattern Recognition).
    \item \textbf{8 Mẫu Mối quan hệ Nền tảng (Eight Patterns):}
    \begin{enumerate}
        \item Phần-Toàn thể (Part-To-Whole)
        \item So sánh Cường độ (Magnitude)
        \item Chuỗi Thời gian (Time Series)
        \item Phân phối (Distribution)
        \item ... và 4 mẫu nâng cao khác.
    \end{enumerate}
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Phân tích Các Mẫu Cơ bản",
        "content": r"""\begin{itemize}
    \item \textbf{Phần-Toàn thể (Part-To-Whole):} Biểu đồ tròn (Pie), Biểu đồ vành khăn (Donut), Treemap. Cho thấy tỷ trọng đóng góp (Ví dụ: Tỷ trọng doanh thu theo từng sản phẩm).
    \item \textbf{Cường độ (Magnitude):} Biểu đồ cột (Bar/Column). Dùng để so sánh trực diện kích thước, quy mô giữa các hạng mục.
    \item \textbf{Chuỗi Thời gian (Time Series):} Biểu đồ đường (Line). Thể hiện xu hướng biến động qua thời gian (Tháng, Quý, Năm).
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Phân tích Các Mẫu Nâng cao",
        "content": r"""\begin{itemize}
    \item \textbf{Phân phối (Distribution):} Biểu đồ Histogram, Box-plot. Đánh giá sự phân tán của dữ liệu và phát hiện ngoại lai (Outliers).
    \item \textbf{Tương quan (Correlation):} Biểu đồ phân tán (Scatter plot). Kiểm tra mối liên hệ giữa hai biến (Ví dụ: Chi phí quảng cáo và Doanh thu).
    \item \textbf{Không gian/Địa lý (Spatial):} Bản đồ (Map). Hiển thị dữ liệu theo vị trí địa lý (Ví dụ: Doanh số theo Tỉnh/Thành phố).
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Nguyên tắc Thiết kế Biểu đồ",
        "content": r"""\begin{itemize}
    \item \textbf{Giữ sự đơn giản (Keep it Simple):} Tránh lạm dụng 3D, bóng đổ hoặc màu sắc lòe loẹt gây xao nhãng (Chartjunk).
    \item \textbf{Rõ ràng (Clarity):} Trục tọa độ, nhãn dữ liệu (Data labels), và tiêu đề phải dễ đọc và mang tính mô tả.
    \item \textbf{Sử dụng Màu sắc có chủ ý:} Dùng màu đỏ cho sự giảm sút/rủi ro, màu xanh cho sự tăng trưởng.
\end{itemize}"""
    },
    
    # LO 7.3
    {
        "type": "normal",
        "title": "7.3 Khám phá Dữ liệu Đa chiều (Tích hợp)",
        "content": r"""\begin{itemize}
    \item \textbf{Tích hợp Mối quan hệ:} Sử dụng kết hợp nhiều loại biểu đồ để có cái nhìn toàn diện hơn (Holistic view).
    \item \textbf{Hai mẫu trong một (Single Visualization):}
    \begin{itemize}
        \item Biểu đồ Đa trục (Dual-axis): So sánh hai chỉ số có thang đo khác nhau trên cùng một biểu đồ (ví dụ: Doanh thu - Cột, Tỷ suất LN - Đường).
        \item Biểu đồ Bong bóng (Bubble chart): Thể hiện 3 biến dữ liệu (Trục X, Trục Y, Độ lớn bong bóng).
    \end{itemize}
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Bảng điều khiển (Dashboards)",
        "content": r"""\begin{itemize}
    \item \textbf{Dashboard là gì?} Là giao diện trực quan tổng hợp nhiều biểu đồ, chỉ số quan trọng (KPIs) trên cùng một màn hình.
    \item \textbf{Tính Tương tác (Interactivity):} Người dùng có thể click, lọc (Slicers), khoan sâu (Drill-down) để khám phá chi tiết (Ví dụ: Từ doanh thu Tổng Công ty khoan xuống từng Chi nhánh).
    \item \textbf{Giá trị Kế toán:} Giúp Ban Lãnh đạo ra quyết định nhanh chóng, dựa trên dữ liệu (Data-driven decision making).
\end{itemize}"""
    }
]

# Fetch images
img_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\textbookForPractice\Figures\Ch_07"
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
    elif img.startswith("Apply It") or img.startswith("Info") or img.startswith("LO") or img.startswith("NoTable"):
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

if pac_imgs:
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
    if slide.get("title", "").startswith("7."):
        if current_section:
            sections.append(current_section)
        current_section = [slide]
    else:
        current_section.append(slide)
if current_section:
    sections.append(current_section)

# Sections: 0 (intro), 1 (LO 7.1), 2 (LO 7.2), 3 (LO 7.3)
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

# Write out slide_data_ch07.py
out_path = "slide_data_ch07.py"
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

print("Wrote slide_data_ch07.py successfully.")
