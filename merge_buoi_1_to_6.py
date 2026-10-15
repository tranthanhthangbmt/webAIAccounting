import os
import copy
from export_all_quizzes import (
    extract_all_questions,
    export_to_word_docx,
    export_to_excel,
    export_to_moodle_aiken,
    export_to_quizizz_template
)

def main():
    output_dir = "NganHangCauHoi_TracNghiem"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Đang trích xuất câu hỏi từ Buổi 1 đến Buổi 6...")
    all_qs = extract_all_questions()
    
    target_sessions = ["Day01", "Day02", "Day03", "Day04", "Day05", "Day06"]
    
    filtered_qs = []
    stt = 1
    for q in all_qs:
        if q["session_key"] in target_sessions:
            q_copy = copy.deepcopy(q)
            q_copy["global_stt"] = stt
            filtered_qs.append(q_copy)
            stt += 1
            
    print(f"Tổng số câu hỏi được gộp: {len(filtered_qs)} câu (Buổi 1 - 6)")
    
    # 1. File Word đề thi gộp Buổi 1 - 6 (Chuẩn Azota / MS Forms)
    docx_path = os.path.join(output_dir, "De_Thi_Trac_Nghiem_Buoi_1_den_6.docx")
    export_to_word_docx(
        filtered_qs, 
        docx_path, 
        title="ĐỀ KIỂM TRA TRẮC NGHIỆM AI TRONG KẾ TOÁN (BUỔI 1 - BUỔI 6)"
    )
    
    # 2. File Excel gộp Buổi 1 - 6
    xlsx_path = os.path.join(output_dir, "De_Thi_Trac_Nghiem_Buoi_1_den_6.xlsx")
    export_to_excel(filtered_qs, xlsx_path)
    
    # 3. File Aiken (Moodle/Canvas)
    aiken_path = os.path.join(output_dir, "De_Thi_Trac_Nghiem_Buoi_1_den_6_Aiken.txt")
    export_to_moodle_aiken(filtered_qs, aiken_path)
    
    # 4. File Quizizz Template
    quizizz_path = os.path.join(output_dir, "Quizizz_Template_Buoi_1_den_6.xlsx")
    export_to_quizizz_template(filtered_qs, quizizz_path)
    
    print("\nHOÀN TẤT GỘP ĐỀ THI BUỔI 1 ĐẾN BUỔI 6!")

if __name__ == "__main__":
    main()
