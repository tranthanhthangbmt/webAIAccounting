import os
import re
import random
import glob

output_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter03/script_chapter03.txt'
titles_path = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting/videoPractice/Chapter03/titles_ch03.txt'
chunk_dir = 'd:/DongAUniversity/TÀI LIỆU DẠY HỌC_2024-2025/Môn TTNT cho kế toán_2026/webAIAccounting'

# 1. Load all vi.txt files
vi_files = glob.glob(os.path.join(chunk_dir, '*vi.txt'))
all_vi_lines = []
for f in vi_files:
    with open(f, 'r', encoding='utf-8') as file:
        all_vi_lines.extend(file.readlines())

def find_snippet(keyword):
    # Try to find the exact keyword in the text
    for i, line in enumerate(all_vi_lines):
        if keyword.lower() in line.lower():
            # grab the next few lines
            snippet = ""
            for j in range(i, min(i+15, len(all_vi_lines))):
                snippet += all_vi_lines[j].strip() + " "
            
            # truncate to 400 chars for double detail
            snippet = snippet.replace(line.strip(), '').strip()
            if not snippet:
                # if empty, grab the line itself
                snippet = line.strip()
                
            # clean up
            snippet = re.sub(r'\s+', ' ', snippet)
            if len(snippet) > 400:
                snippet = snippet[:400].rsplit(' ', 1)[0] + '...'
            return snippet
    return ""

text = """KỊCH BẢN BÀI GIẢNG THỰC HÀNH CHƯƠNG 3
Động lực và Mục tiêu Phân tích Dữ liệu

=========================================
Người 1 (Giảng viên): Hướng dẫn, phân tích các động lực kinh doanh và case study.
Người 2 (Sinh viên): Tương tác, đặt câu hỏi thực tế. (Xưng hô "thầy")
=========================================

Slide 1: TRANG BÌA
Người 1: Chào mừng các em đến với Chương 3. Hôm nay chúng ta sẽ đi sâu vào cách biến dữ liệu thô thành những quyết định chiến lược và giá trị thực tiễn. Trọng tâm của chúng ta là học cách xác định đúng "Động lực" và "Mục tiêu" trước khi bắt tay vào phân tích bất kỳ tập dữ liệu nào.
Người 2: Dạ em chào thầy. Em rất tò mò làm sao để biết mình nên bắt đầu phân tích từ đâu khi đối mặt với một đống dữ liệu khổng lồ, đặc biệt là trong môi trường doanh nghiệp phức tạp hiện nay ạ?

Slide 2: GÓC NHÌN CHUYÊN GIA
Người 1: Câu hỏi của em chính là cốt lõi của vấn đề! Các chuyên gia phân tích dữ liệu hàng đầu luôn khuyên rằng: "Đừng bao giờ lao vào tính toán hay vẽ biểu đồ khi chưa thực sự hiểu sếp hoặc khách hàng cần gì". Chúng ta phải luôn bắt đầu bằng một câu hỏi kinh doanh cụ thể, có thể đo lường được và mang tính định hướng rõ ràng.
Người 2: Vâng, em hiểu rồi ạ. Giống như trước khi xây nhà thì phải có bản thiết kế kỹ lưỡng trước vậy. Nếu không xác định đúng mục tiêu ngay từ đầu, mọi công sức xử lý dữ liệu sau này đều có thể đổ sông đổ biển.

Slide 3: LỘ TRÌNH CHƯƠNG
Người 1: Chính xác! Hôm nay chúng ta sẽ đi qua 6 phần chính rất hệ thống. Bắt đầu từ việc định hình câu hỏi phân tích nhờ vào động lực thực tế của doanh nghiệp, cho đến việc thiết lập 4 loại câu hỏi then chốt: Câu hỏi Mô tả (Chuyện gì đã xảy ra?), Chẩn đoán (Tại sao lại xảy ra?), Dự đoán (Điều gì sẽ xảy ra tiếp theo?) và Đề xuất (Chúng ta nên làm gì?).

Slide 4: 3.1 ĐỘNG LỰC ĐỊNH HÌNH CÂU HỎI PHÂN TÍCH NHƯ THẾ NÀO?
Người 1: Trước tiên, hãy hiểu "Động lực" là gì. Động lực chính là những tác nhân từ bên trong nội bộ công ty hoặc từ bên ngoài như sự thay đổi của thị trường, áp lực từ đối thủ cạnh tranh... thôi thúc công ty phải hành động ngay lập tức để thích ứng hoặc phát triển. Nó tạo ra một nhu cầu bức thiết phải phân tích dữ liệu.
Người 2: Chẳng hạn như việc doanh thu đột ngột giảm mạnh trong quý vừa qua, hay việc bị đối thủ cướp mất tệp khách hàng thân thiết, đó chính là những động lực buộc ban giám đốc phải tìm hiểu dữ liệu phải không thầy?

Slide 5: MỤC TIÊU RÕ RÀNG
Người 1: Hoàn toàn đúng! Và từ động lực bức thiết đó, chúng ta sẽ thiết lập "Mục tiêu" (Objective). Mục tiêu ở đây là thứ ta muốn đạt được một cách cụ thể để giải quyết triệt để cái động lực kia. Động lực là lý do bắt đầu, còn Mục tiêu là đích đến của toàn bộ quá trình phân tích.
Người 2: Nghĩa là nếu động lực của công ty là "doanh số bán hàng giảm sút", thì mục tiêu đặt ra cho bộ phận phân tích sẽ phải là "tìm ra chính xác nguyên nhân gây giảm doanh số và đề xuất chiến lược cụ thể nhằm tăng doanh số lên 10% trong quý tới", đúng không ạ?

Slide 6: XÁC ĐỊNH MỤC TIÊU
Người 1: Chuẩn không cần chỉnh! Mục tiêu phải thật cụ thể, đo lường được và khả thi (theo tiêu chí SMART). Càng mơ hồ chung chung, em càng dễ bị "ngợp" và đi lạc trong mớ dữ liệu khổng lồ. Việc xác định đúng mục tiêu sẽ giúp giới hạn phạm vi thu thập dữ liệu và chọn lọc đúng công cụ phân tích.
Người 2: Dạ vâng, em sẽ ghi nhớ nguyên tắc tối quan trọng này. Rõ ràng là không thể bắt tay vào làm nếu chưa biết mình đang đi tìm kiếm điều gì.

Slide 7: KẾT NỐI ĐỘNG LỰC VỚI MỤC TIÊU
Người 1: Khi động lực rõ ràng, mục tiêu sẽ tự động trở nên sắc bén. Chúng kết nối trực tiếp với nhau tạo thành một mũi tên định hướng cho việc chọn phương pháp phân tích. Sự thống nhất giữa động lực kinh doanh và mục tiêu kỹ thuật chính là chìa khóa thành công của bất kỳ dự án dữ liệu nào.
Người 2: Việc xác định động lực và mục tiêu đúng đắn thực sự đóng vai trò như một chiếc la bàn trong quá trình phân tích dữ liệu, giúp chúng ta luôn đi đúng hướng và mang lại giá trị thực cho doanh nghiệp ạ.
"""

with open(titles_path, 'r', encoding='utf-8') as f:
    titles = f.read().splitlines()

titles.append('Slide 123: KẾT THÚC')

teacher_ill_templates = [
    'Chúng ta cùng phân tích thật kỹ {title} nhé. Trọng tâm cốt lõi của hình ảnh này được mô tả chi tiết như sau: "{snippet}". Các em hãy lưu ý cách áp dụng những thông tin này vào bối cảnh thực tế của doanh nghiệp để thấy rõ sự liên kết giữa lý thuyết và thực hành.',
    'Các em hãy dành chút thời gian quan sát cẩn thận minh họa ở {title} trên slide. Nội dung trong hình đề cập đến một khía cạnh rất quan trọng: "{snippet}". Đây là một tình huống rất sát với thực tế quản trị doanh nghiệp, đòi hỏi chúng ta phải có cái nhìn hệ thống.',
    'Slide tiếp theo mang đến một ví dụ thực tế rất sinh động qua {title}. Cụ thể, tài liệu phân tích rằng: "{snippet}". Việc phân tích mổ xẻ kỹ càng từng chi tiết trong hình này sẽ giúp các em hiểu sâu hơn về bản chất của vấn đề và cách vận dụng các công cụ phân tích.',
    'Nhìn vào {title}, chúng ta có thể rút ra những bài học chiến lược nào? Văn bản mô tả đi kèm ghi rõ: "{snippet}". Đây là một điểm cực kỳ đáng chú ý mà các chuyên gia phân tích dữ liệu thường xuyên gặp phải trong quá trình làm việc thực tế.',
    'Mời các em tập trung quan sát {title}. Điểm cốt lõi và bài học lớn nhất ở đây là: "{snippet}". Hãy thử đặt mình vào vị trí của người ra quyết định trong tình huống này, các em sẽ thấy việc hiểu rõ dữ liệu quan trọng đến mức nào.'
]

student_ill_templates = [
    'Dạ, ví dụ minh họa này làm em thấy rõ hơn hẳn những lý thuyết trừu tượng vừa học. Nó giúp em hình dung được quy trình thực tế sẽ diễn ra như thế nào ạ.',
    'Vâng thưa thầy, hình ảnh và diễn giải này giải thích rất trực quan, dễ hiểu. Việc có số liệu và tình huống cụ thể giúp em nắm bắt vấn đề nhanh chóng hơn rất nhiều.',
    'Dạ, kết hợp lý thuyết với một minh họa thực tế mang tính ứng dụng cao thế này rất hiệu quả ạ. Em có thể thấy rõ vai trò của từng bước phân tích trong bức tranh tổng thể.',
    'Em đã nắm vững được ý chính và thông điệp cốt lõi của phần này rồi thưa thầy. Các chi tiết trong hình thực sự bổ trợ rất tốt cho việc hiểu sâu lý thuyết.',
    'Dạ, nhờ minh họa chi tiết này mà các khái niệm vốn khô khan lại trở nên gần gũi và dễ áp dụng hơn rất nhiều ạ. Em sẽ ghi chú lại cẩn thận tình huống này.'
]

teacher_ex_templates = [
    'Bây giờ, để rèn luyện kỹ năng thực chiến, chúng ta cùng xem xét bài tập {title}. Đề bài đặt ra một tình huống đầy thách thức: "{snippet}". Các em hãy thử suy nghĩ một cách đa chiều xem chúng ta nên tiếp cận và giải quyết vấn đề này theo phương pháp nào là tối ưu nhất.',
    'Đến phần thực hành thực tế với {title}. Dữ kiện trọng tâm của bài toán cung cấp: "{snippet}". Các em hãy vận dụng toàn bộ những phương pháp luận vừa học để xác định chính xác yêu cầu, sau đó lên kế hoạch phân tích từng bước một nhé.',
    'Chúng ta cùng thử sức với thử thách trong {title} xem sao. Yêu cầu chi tiết của bài toán là: "{snippet}". Hãy cứ bám sát vào khung phân tích chuẩn mực mà chúng ta đã thống nhất, đừng quên phân loại dữ liệu cẩn thận trước khi xử lý.'
]

student_ex_templates = [
    'Em sẽ bám sát vào các thông tin cốt lõi trong đề bài này, tiến hành phân loại rành mạch từng biến số và áp dụng ngay mô hình phù hợp để giải quyết bài toán ạ.',
    'Dạ vâng, em đang cẩn thận gạch dưới các từ khóa quan trọng và lập dàn ý các bước cần làm để tìm ra hướng giải quyết chính xác nhất thưa thầy.',
    'Bài tập này rất sát với thực tiễn doanh nghiệp ạ. Em sẽ lập tức áp dụng quy trình phân tích từ việc xác định mục tiêu đến lựa chọn công cụ để đưa ra lời giải hoàn chỉnh.'
]

for i in range(7, len(titles)):
    if ': ' in titles[i]:
        slide_title = titles[i].split(': ', 1)[1]
    else:
        slide_title = titles[i]
        
    text += f'\nSlide {i+1}: {slide_title.upper()}\n'
    
    # Keyword extraction
    keyword = slide_title
    nice_title = slide_title
    if 'ILLUSTRATION' in slide_title:
        nice_title = slide_title.replace('ILLUSTRATION', 'Minh họa')
        keyword = nice_title
    
    if '&' in keyword:
        keyword = keyword.split('&')[0].strip()
        
    if '_' in keyword:
        keyword = keyword.split('_')[0].strip()
        
    snippet = ""
    if 'ILLUSTRATION' in slide_title or 'BE ' in slide_title or 'EX ' in slide_title or 'PAC ' in slide_title or 'Case' in slide_title:
        snippet = find_snippet(keyword)
    
    if 'ILLUSTRATION' in slide_title:
        if snippet:
            t_template = random.choice(teacher_ill_templates)
            s_template = random.choice(student_ill_templates)
            text += f'Người 1: {t_template.format(title=nice_title, snippet=snippet)}\n'
            text += f'Người 2: {s_template}\n'
        else:
            text += f'Người 1: Chuyển sang phần {nice_title}, các em chú ý quan sát thật cẩn thận từng chi tiết, từng con số và biểu đồ trên màn hình nhé. Mỗi một dữ kiện nhỏ đều có thể ẩn chứa những thông tin vô giá cho quá trình ra quyết định của doanh nghiệp.\n'
            text += 'Người 2: Dạ vâng thưa thầy, em đang phóng to để phân tích kỹ từng thành phần cấu trúc của hình ảnh này ạ.\n'
            
    elif 'BE ' in slide_title or 'EX ' in slide_title or 'PAC ' in slide_title or 'Case' in slide_title:
        if snippet:
            t_template = random.choice(teacher_ex_templates)
            s_template = random.choice(student_ex_templates)
            text += f'Người 1: {t_template.format(title=slide_title, snippet=snippet)}\n'
            text += f'Người 2: {s_template}\n'
        else:
            text += f'Người 1: Chúng ta cùng bước vào phần thực hành chuyên sâu với {slide_title}. Các em hãy vận dụng toàn diện hệ thống kiến thức vừa học để nhận diện vấn đề và đề xuất phương án giải quyết triệt để nhé.\n'
            text += 'Người 2: Vâng ạ, em sẽ đọc thật kỹ yêu cầu của đề bài, bóc tách từng lớp thông tin và phân tích các từ khóa chính xác trước khi lên phương án thưa thầy.\n'
            
    elif i+1 == 123:
        text += 'Người 1: Phù! Một chương học thực sự đồ sộ và vô cùng quan trọng với 123 slides đã chính thức hoàn thành. Qua chương này, các em đã nắm vững được linh hồn của nghệ thuật phân tích dữ liệu: Mọi thứ phải luôn bắt đầu từ việc thấu hiểu sâu sắc Động lực kinh doanh và xác định đúng Mục tiêu cốt lõi! Thiếu đi những điều này, mọi kỹ năng lập trình hay sử dụng công cụ đều trở nên vô nghĩa.\n'
        text += 'Người 2: Dạ vâng, hôm nay khối lượng kiến thức tuy dài và nhiều thách thức nhưng em thấy cấu trúc bài giảng rất liền mạch, logic và mang tính hệ thống cao. Những ví dụ thực tế đã giúp em kết nối được lý thuyết với công việc của một chuyên gia phân tích. Em chân thành cảm ơn thầy! Hẹn gặp lại thầy và mọi người ở những chương học hấp dẫn tiếp theo ạ!\n'
    else:
        # Avoid robotic normal slide text too
        normal_teacher = [
            f'Người 1: Đi sâu vào nội dung "{slide_title}", chúng ta cần đặc biệt lưu ý và phân tích kỹ lưỡng những điểm cốt lõi sau đây. Việc hiểu thấu đáo khái niệm này sẽ là nền tảng vững chắc cho việc thiết kế các mô hình phân tích phức tạp hơn ở giai đoạn sau.',
            f'Người 1: Khi bước sang phần "{slide_title}", thầy muốn nhấn mạnh rằng đây là một khái niệm mang tính ứng dụng cực kỳ cao, rất hay xuất hiện trong các bài toán tối ưu hóa thực tế của doanh nghiệp. Các em hãy ghi chú lại cẩn thận nhé.',
            f'Người 1: Tiếp tục với phần "{slide_title}", các em hãy cố gắng xâu chuỗi một cách logic với những nguyên lý chúng ta đã học ở các phần trước. Tính liên kết chặt chẽ giữa các khái niệm chính là chìa khóa để làm chủ bức tranh toàn cảnh về dữ liệu.'
        ]
        normal_student = [
            'Người 2: Vâng, em đang cẩn thận ghi chú lại các ý chính này vào sổ tay cũng như các trường hợp ngoại lệ cần lưu ý rồi thưa thầy. Quả thực phần này đòi hỏi sự tập trung cao độ.',
            'Người 2: Dạ, em đang theo dõi sát sao từng bước trong tiến trình bài giảng ạ. Càng học sâu vào chi tiết, em càng thấy được sự thú vị và logic chặt chẽ của bộ môn này.',
            'Người 2: Vâng thưa thầy, phần lý thuyết này được trình bày rất logic, hệ thống và dễ tiếp thu. Việc kết hợp với các ví dụ thực tiễn ngay từ đầu giúp em không bị bỡ ngỡ ạ.'
        ]
        text += f'{random.choice(normal_teacher)}\n'
        text += f'{random.choice(normal_student)}\n'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Generated natural script_chapter03.txt successfully with more detailed context!")
