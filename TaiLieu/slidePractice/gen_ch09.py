import os
import re

def exact_sort_key(name):
    parts = re.findall(r'\d+', name)
    return [int(p) for p in parts]

def generate_ch09_data():
    img_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\textbookForPractice\Figures\Ch_09"
    out_file = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\TaiLieu\slidePractice\slide_data_ch09.py"

    all_images = []
    if os.path.exists(img_dir):
        for f in os.listdir(img_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                all_images.append(f)

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

    content_slides = [
        {
            "type": "title_slide"
        },
        {
            "type": "normal",
            "title": "Chương 9: Trình bày Kết quả Phân tích Dữ liệu",
            "content": r"""\begin{itemize}
    \item \textbf{Mục tiêu:} Xây dựng năng lực phân tích dữ liệu và trình bày kết quả cho kế toán viên.
    \item \textbf{Tầm quan trọng:} Đóng vai trò là cầu nối giữa dữ liệu kỹ thuật và quyết định chiến lược.
    \item \textbf{Lộ trình:} Từ định nghĩa câu chuyện dữ liệu đến tạo trực quan hóa và nhận diện các biểu đồ gây hiểu lầm.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "9.1 Kể Chuyện Bằng Dữ Liệu",
            "content": r"""\begin{itemize}
    \item \textbf{Câu chuyện dữ liệu (Data Story) là gì?} Là sự giao thoa giữa dữ liệu, hình ảnh trực quan, và tường thuật logic.
    \item \textbf{Mục đích:} Giúp chuyển hóa những bảng số liệu khô khan thành các insight có thể hành động.
    \item Không chỉ là vẽ biểu đồ, mà là việc trả lời câu hỏi: \textit{"Dữ liệu này có ý nghĩa gì đối với công ty?"}
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Phát triển Năng lực Dữ liệu",
            "content": r"""\begin{itemize}
    \item \textbf{Data Literacy:} Khả năng đọc, làm việc, phân tích và tranh luận bằng dữ liệu.
    \item \textbf{Vai trò của Kế toán:} Là chuyên gia am hiểu hoạt động tài chính, kế toán viên ở vị thế lý tưởng nhất để trở thành "người kể chuyện" bằng dữ liệu cho Ban Giám đốc.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Kỹ thuật Xây dựng Câu chuyện",
            "content": r"""\begin{itemize}
    \item \textbf{Bối cảnh (Context):} Dữ liệu này được thu thập khi nào? Nó phản ánh xu hướng gì?
    \item \textbf{Giao tiếp hiệu quả (Communicate Effectively):} Hãy trình bày rõ ràng thông điệp, đừng bắt khán giả phải tự tìm câu trả lời trong dữ liệu.
    \item Xác định cấu trúc cốt truyện: Bắt đầu bằng thực trạng, chỉ ra nút thắt (vấn đề) và đề xuất giải pháp.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "9.2 Quy Trình Tạo Trực Quan Hóa",
            "content": r"""\begin{itemize}
    \item Trực quan hóa dữ liệu hiệu quả cần một quy trình tuần tự.
    \item \textbf{Quy trình 3 bước cốt lõi:}
    \begin{enumerate}
        \item Xác minh Dữ liệu (Verify the Data)
        \item Thấu hiểu Khán giả (Consider the Audience)
        \item Xác định Mục tiêu (Define the Objective)
    \end{enumerate}
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Bước 1 & 2: Xác minh & Thấu hiểu Khán giả",
            "content": r"""\begin{itemize}
    \item \textbf{Xác minh Dữ liệu:} Đảm bảo tính chính xác, đầy đủ và hợp lệ. Dữ liệu sai sẽ dẫn đến biểu đồ sai (Garbage In, Garbage Out).
    \item \textbf{Thấu hiểu Khán giả:} Ai sẽ xem biểu đồ này? Họ có kiến thức chuyên môn về tài chính hay không? Mức độ chi tiết họ cần là bao nhiêu?
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Bước 3: Xác định Mục tiêu (Define the Objective)",
            "content": r"""\begin{itemize}
    \item \textbf{Mục tiêu:} Biểu đồ nhằm mục đích so sánh, chỉ ra xu hướng, hay hiển thị tỷ trọng?
    \item \textbf{Lựa chọn biểu đồ (Chart selection):} Phải chọn đúng biểu đồ phù hợp với mục tiêu.
    \begin{itemize}
        \item \textit{Ví dụ:} So sánh giữa các mục thì dùng Bar Chart. Xem xu hướng theo thời gian thì dùng Line Chart.
    \end{itemize}
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "9.3 Đặc Điểm Trực Quan Hóa Hiệu Quả",
            "content": r"""\begin{itemize}
    \item \textbf{Hiệu quả là gì?} Là khả năng truyền tải thông điệp nhanh nhất và ít gây nhầm lẫn nhất.
    \item \textbf{Nhận thức Thị giác (Visual Perception):} Não bộ con người được tối ưu hóa để xử lý hình ảnh và màu sắc thay vì các con số dạng văn bản.
    \item Chìa khóa: Khai thác sức mạnh của hệ thống thị giác để hướng sự chú ý của người xem.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Các Thuộc tính Tiền-chú-ý (Preattentive Attributes)",
            "content": r"""\begin{itemize}
    \item \textbf{Định nghĩa:} Các đặc điểm mà não bộ xử lý vô thức trước cả khi ta tập trung suy nghĩ.
    \item \textbf{Màu sắc (Color):} Sử dụng màu đỏ để nhấn mạnh sự bất thường hoặc thua lỗ.
    \item \textbf{Kích thước \& Hình dạng (Size \& Shape):} Dùng điểm lớn hơn hoặc đường nét đậm hơn để nhấn mạnh dữ liệu quan trọng nhất.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Tối Giản Hóa và Tránh Lộn Xộn",
            "content": r"""\begin{itemize}
    \item \textbf{Avoid Clutter:} Tránh sự rối rắm không cần thiết.
    \item \textbf{Chartjunk:} Các thành phần trang trí không mang lại giá trị thông tin (VD: Hiệu ứng 3D, lưới nền quá đậm, màu sắc sặc sỡ không cần thiết).
    \item Tối giản hóa giúp thông điệp chính nổi bật (Nguyên lý Tỷ lệ Dữ liệu/Mực in - Data-ink ratio).
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "9.4 Nhận Diện Trực Quan Hóa Gây Hiểu Lầm",
            "content": r"""\begin{itemize}
    \item Dữ liệu có thể không biết nói dối, nhưng biểu đồ thì có thể (Misleading Data Visualizations).
    \item Việc thiết kế sai nguyên tắc có thể bóp méo góc nhìn của người xem.
    \item Kế toán viên cần tinh ý nhận diện những cạm bẫy thiết kế phổ biến.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Lỗi 1: Bỏ qua đường cơ sở (Omitting Baseline)",
            "content": r"""\begin{itemize}
    \item Đối với biểu đồ cột (Bar chart), trục Y \textbf{bắt buộc} phải bắt đầu từ số 0.
    \item \textbf{Hậu quả:} Nếu trục Y bị cắt xén, một sự chênh lệch nhỏ sẽ bị khuếch đại thành một sự thay đổi khổng lồ.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Lỗi 2: Thao Túng Trục Y",
            "content": r"""\begin{itemize}
    \item \textbf{Đảo ngược trục (Inverted Y-axis):} Gây cảm giác lầm tưởng rằng số liệu đang tăng trong khi thực tế đang giảm.
    \item \textbf{Chia tỷ lệ không đều (Uneven scaling):} Trục tọa độ giãn cách không đều làm đường xu hướng bị biến dạng.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Lỗi 3: Đi Ngược Quy Ước Thiết Kế",
            "content": r"""\begin{itemize}
    \item \textbf{Going Against Conventions:} Con người có các quy ước ngầm về màu sắc và không gian.
    \item \textit{Ví dụ:} Màu Đỏ thường mang ý nghĩa tiêu cực/lỗ, màu Xanh mang ý nghĩa tích cực/lãi. Dùng ngược lại sẽ gây nhầm lẫn trầm trọng.
    \item Trên/Phải thường mang ý nghĩa cao hơn/tăng lên. Dưới/Trái là giảm.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Lỗi 4: Chọn Lọc Dữ Liệu & Dùng Sai Biểu Đồ",
            "content": r"""\begin{itemize}
    \item \textbf{Cherry-picking:} Chỉ chọn hiển thị khoảng thời gian dữ liệu có lợi để che giấu bức tranh tổng thể.
    \item \textbf{Wrong Graph:} Dùng sai biểu đồ, ví dụ dùng Pie Chart (Biểu đồ tròn) cho dữ liệu tổng không bằng 100\%, hoặc dùng quá nhiều lát cắt.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "9.5 Thiết Kế Bài Thuyết Trình Tương Tác",
            "content": r"""\begin{itemize}
    \item Việc báo cáo bằng file tĩnh truyền thống (PDF, Excel) đang dần nhường chỗ cho các báo cáo tương tác.
    \item \textbf{Interactive Dashboards:} Người dùng có thể click, filter (lọc) và drill-down (đi sâu) để xem dữ liệu theo ý muốn.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Kinh Nghiệm Thuyết Trình Trực Tiếp",
            "content": r"""\begin{itemize}
    \item \textbf{Best Practices for Live Presentations:}
    \item Không đưa quá nhiều chữ lên slide (khán giả sẽ đọc chữ thay vì nghe bạn nói).
    \item Sử dụng biểu đồ để hỗ trợ lập luận. Giải thích rõ các trục tung/hoành trước khi phân tích xu hướng.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Case Study: Báo Cáo Kế Toán Trực Quan",
            "content": r"""\begin{itemize}
    \item Ứng dụng xây dựng Dashboard trong các cơ quan nhà nước, thư viện công cộng (VD: Madison Public Library) và doanh nghiệp.
    \item Cho phép Ban Giám đốc nhìn được bức tranh thu-chi và phân bổ ngân sách real-time.
\end{itemize}"""
        },
        {
            "type": "normal",
            "title": "Tổng Kết Chương",
            "content": r"""\begin{itemize}
    \item \textbf{Tóm tắt LO 9.1 - LO 9.5:} Kỹ năng phân tích dữ liệu không chỉ nằm ở việc xử lý kỹ thuật, mà quan trọng nhất là \textbf{truyền đạt (communicate)} được giá trị của dữ liệu.
    \item Trực quan hóa đúng cách giúp tối ưu hóa ra quyết định.
\end{itemize}"""
        }
    ]

    # Interleave logic
    final_slides = []
    
    # 1. Distribute content slides
    img_per_content = len(image_slides) // len(content_slides) if content_slides else 0
    extra_imgs = len(image_slides) % len(content_slides) if content_slides else 0
    
    img_idx = 0
    for i, c_slide in enumerate(content_slides):
        final_slides.append(c_slide)
        count = img_per_content + (1 if i < extra_imgs else 0)
        for _ in range(count):
            if img_idx < len(image_slides):
                final_slides.append(image_slides[img_idx])
                img_idx += 1
                
    # Append any remaining images
    while img_idx < len(image_slides):
        final_slides.append(image_slides[img_idx])
        img_idx += 1
        
    # 2. Append all BE/EX/PAC and other non-illustration images
    final_slides.extend(be_ex_pac_slides)
    final_slides.extend(be_ex_pac_final)

    # Generate Python code string
    py_code = 'chapter_title = "CHƯƠNG 9"\n'
    py_code += 'chapter_subtitle = "Trình bày Kết quả Phân tích Dữ liệu"\n'
    py_code += 'slides = [\n'
    for slide in final_slides:
        py_code += '    {\n'
        for k, v in slide.items():
            if k == "content":
                py_code += f'        "{k}": r"""{v}""",\n'
            else:
                py_code += f'        "{k}": "{v}",\n'
        py_code += '    },\n'
    py_code += ']\n'

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(py_code)
    print("Done generating slide_data_ch09.py")

if __name__ == "__main__":
    generate_ch09_data()
