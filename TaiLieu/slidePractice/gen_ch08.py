import os
import re

# Generate slide_data_ch08.py by interleaving text and images.
chapter_title = "Diễn giải Kết quả Phân tích Dữ liệu"
chapter_subtitle = "Interpreting Data Analysis Results"

normal_slides = [
    {
        "type": "title_slide"
    },
    {
        "type": "normal",
        "title": "Góc nhìn Chuyên gia (Professional Insight)",
        "content": r"""\begin{itemize}
    \item \textbf{Câu hỏi cốt lõi:} "Liệu kết quả phân tích này có hợp lý không?" (Do the Analysis Results Make Sense?)
    \item \textbf{Trách nhiệm của Kế toán viên:} Kế toán không chỉ tạo ra báo cáo mà còn phải \textit{diễn giải} ý nghĩa của những con số đó để tư vấn cho Ban Lãnh đạo.
    \item \textbf{Tư duy phản biện (Critical Thinking):} Đừng bao giờ tin tưởng tuyệt đối vào kết quả đầu ra của một thuật toán hay AI mà không có sự đánh giá, kiểm chứng từ con người.
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Lộ trình Chương (Chapter Roadmap)",
        "content": r"""\begin{itemize}
    \item \textbf{LO 8.1:} Phân biệt Khám phá và Diễn giải.
    \item \textbf{LO 8.2:} Áp dụng Tư duy Phản biện trong Diễn giải (SPARK-S).
    \item \textbf{LO 8.3:} Đánh giá Sự phù hợp của Kết quả.
    \item \textbf{LO 8.4:} Đánh giá Phân tích Mô tả và Chẩn đoán.
    \item \textbf{LO 8.5:} Đánh giá Phân tích Dự đoán và Đề xuất.
\end{itemize}"""
    },
    
    # LO 8.1
    {
        "type": "normal",
        "title": "8.1 Rút ra kết luận từ Phân tích dữ liệu",
        "content": r"""\begin{itemize}
    \item \textbf{Khám phá (Exploration):} Trả lời câu hỏi "Tôi đang nhìn thấy gì?" Mục tiêu là \textit{hiểu dữ liệu} (Understanding the data).
    \item \textbf{Diễn giải (Interpretation):} Trả lời câu hỏi "Điều này có ý nghĩa gì đối với doanh nghiệp?" Mục tiêu là \textit{hiểu kết quả phân tích} (Understanding the analysis).
    \item \textbf{Quá trình Diễn giải:} Đòi hỏi sự kết hợp giữa kiến thức chuyên môn kế toán, hiểu biết về bối cảnh kinh doanh và các nguyên tắc thống kê.
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Từ Trực quan hóa đến Diễn giải",
        "content": r"""\begin{itemize}
    \item \textbf{Ví dụ:} Một biểu đồ doanh thu đang đi xuống.
    \item \textbf{Khám phá:} Phát hiện ra doanh thu tháng 10 giảm 15\% so với tháng 9.
    \item \textbf{Diễn giải:} Nguyên nhân là do gián đoạn chuỗi cung ứng hoặc thay đổi chính sách tín dụng? Hậu quả là dòng tiền tháng 11 sẽ bị thiếu hụt.
\end{itemize}"""
    },
    
    # LO 8.2
    {
        "type": "normal",
        "title": "8.2 Ứng dụng Tư duy Phản biện (SPARK-S)",
        "content": r"""\begin{itemize}
    \item Tư duy phản biện giúp chúng ta không bị dẫn dắt bởi những dữ liệu sai lệch hoặc thiên kiến. Khung \textbf{SPARK-S}:
    \begin{itemize}
        \item \textbf{S - Stakeholders:} Ai bị ảnh hưởng bởi kết quả này?
        \item \textbf{P - Purpose:} Mục đích ban đầu của việc phân tích là gì?
        \item \textbf{A - Alternatives:} Có cách giải thích nào khác cho hiện tượng này không?
    \end{itemize}
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Tư duy Phản biện (Tiếp theo)",
        "content": r"""\begin{itemize}
    \item \textbf{Khung SPARK-S (Tiếp):}
    \begin{itemize}
        \item \textbf{R - Risks \& Biases:} Phân tích này có gặp phải thiên kiến xác nhận (Confirmation Bias) hay rủi ro dữ liệu sai không?
        \item \textbf{K - Knowledge:} Chúng ta cần thêm thông tin gì để kết luận chắc chắn hơn?
        \item \textbf{S - Self-reflection:} Đánh giá lại bản thân trong quá trình phân tích.
    \end{itemize}
\end{itemize}"""
    },
    
    # LO 8.3
    {
        "type": "normal",
        "title": "8.3 Đánh giá Sự phù hợp của Kết quả",
        "content": r"""\begin{itemize}
    \item \textbf{Câu hỏi chính:} Kết quả thu được có thực sự \textit{trả lời được câu hỏi kinh doanh} ban đầu không?
    \item \textbf{Đánh giá Dữ liệu (Data):} Dữ liệu có đủ sạch, đủ lớn và đại diện cho vấn đề không?
    \item \textbf{Đánh giá Phương pháp (Methods):} Mô hình thống kê hoặc biểu đồ được chọn có phù hợp với loại dữ liệu không?
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Kiểm tra và Bổ sung thông tin",
        "content": r"""\begin{itemize}
    \item \textbf{Kiểm tra Kết quả (Examine Results):} Các con số có ý nghĩa thực tế không? (Ví dụ: Tỷ suất lợi nhuận 500\% có thể là do lỗi dữ liệu hơn là thực tế).
    \item \textbf{Xác định thông tin cần thêm:} Có cần bổ sung dữ liệu phi tài chính (Non-financial data) để giải thích cho dữ liệu tài chính không?
\end{itemize}"""
    },
    
    # LO 8.4
    {
        "type": "normal",
        "title": "8.4 Đánh giá Phân tích Mô tả và Chẩn đoán",
        "content": r"""\begin{itemize}
    \item \textbf{Tính Hợp lệ (Validity):} Đo lường đúng thứ cần đo.
    \item \textbf{Độ Tin cậy (Reliability):} Tính nhất quán của kết quả khi lặp lại phân tích.
    \item \textbf{Phân tích Mô tả (Descriptive):} Đánh giá tính chính xác của các chỉ số tóm tắt (Tổng, Trung bình, Max, Min).
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Đánh giá Phân tích Chẩn đoán",
        "content": r"""\begin{itemize}
    \item \textbf{Phân tích Chẩn đoán (Diagnostic):} Giải thích "Tại sao điều đó xảy ra?"
    \item \textbf{Nhận diện Điểm dị biệt (Outliers):} Sử dụng biểu đồ phân tán (Scatterplot) hoặc Box-plot để tìm các giao dịch bất thường trong Kiểm toán.
    \item \textbf{Lưu ý:} Không phải Outlier nào cũng là gian lận, có thể do sai sót nhập liệu.
\end{itemize}"""
    },

    # LO 8.5
    {
        "type": "normal",
        "title": "8.5 Đánh giá Phân tích Dự đoán và Đề xuất",
        "content": r"""\begin{itemize}
    \item \textbf{Phân tích Dự đoán (Predictive):} Sử dụng mô hình (như Hồi quy - Regression) để dự báo tương lai.
    \item \textbf{Đánh giá Mô hình:}
    \begin{itemize}
        \item Hệ số $R^2$ có đủ cao không?
        \item Mối quan hệ có ý nghĩa thống kê (p-value < 0.05) không?
        \item Cẩn thận với "Tương quan không có nghĩa là Nhân quả" (Correlation vs. Causation).
    \end{itemize}
\end{itemize}"""
    },
    {
        "type": "normal",
        "title": "Đánh giá Phân tích Đề xuất",
        "content": r"""\begin{itemize}
    \item \textbf{Phân tích Đề xuất (Prescriptive):} Tối ưu hóa các nguồn lực để đạt kết quả tốt nhất.
    \item \textbf{Đánh giá Khả năng Thực thi:} Đề xuất của AI có khả thi trong điều kiện ngân sách và chính sách của công ty không?
    \item \textbf{Kết luận:} Con người luôn là chốt chặn cuối cùng trong quá trình ra quyết định tài chính.
\end{itemize}"""
    }
]

# Fetch images
img_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\textbookForPractice\Figures\Ch_08"
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
    elif not (img.startswith("BE ") or img.startswith("EX ") or img.startswith("PAC ")):
        # Apply It, PR, ERD, Ortho Inc, Infor, LO...
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

if be_imgs:
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

if ex_imgs:
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

if be_ex_pac_slides:
    be_ex_pac_final.append({
        "type": "normal",
        "title": "Trường hợp và Bổ trợ",
        "content": r"""\begin{center}
        \Huge \textbf{Tình huống Bổ trợ \& Dữ liệu} \\
        \vspace{0.5cm}
        \Large PR, ERD, Info
    \end{center}"""
    })
    be_ex_pac_final.extend(be_ex_pac_slides)

# Group normal slides by section
sections = []
current_section = []
for slide in normal_slides:
    if slide.get("title", "").startswith("8."):
        if current_section:
            sections.append(current_section)
        current_section = [slide]
    else:
        current_section.append(slide)
if current_section:
    sections.append(current_section)

# Sections: 0 (intro), 1 (LO 8.1), 2 (LO 8.2), 3 (LO 8.3), 4 (LO 8.4), 5 (LO 8.5)
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

# Write out slide_data_ch08.py
out_path = "slide_data_ch08.py"
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

print("Wrote slide_data_ch08.py successfully.")
