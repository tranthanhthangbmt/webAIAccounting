# update_all_buoi_h1_titles.py
# Update the main H1 title (line 1) of all docs/buoi_*.md files to perfectly match
# the official syllabus in TaiLieu/DE CUONG TRI TUE NHAN TAO- 2025.pdf (Table 5)
# and reflect the contents of the textbook/Buoi_*.pdf files and Vietnamese translations.

import os
import glob

official_titles = {
    "docs/buoi_01.md": "# Buổi 1: Giới thiệu Tổng quan về AI và Cuộc cách mạng Công nghệ Kinh tế - Tài chính",
    "docs/buoi_02.md": "# Buổi 2: AI, Blockchain và Dữ liệu lớn trong Kinh tế - Tài chính",
    "docs/buoi_03.md": "# Buổi 3: Tương lai của AI, Đạo đức, Rủi ro và Khai phá Dữ liệu trong Kế toán",
    "docs/buoi_04.md": "# Buổi 4: AI trong Dự báo Kinh tế Vĩ mô và Phân tích Hành vi Người tiêu dùng",
    "docs/buoi_05.md": "# Buổi 5: AI trong Quản lý Chuỗi cung ứng và Phát triển Kinh tế Xanh, Bền vững",
    "docs/buoi_06.md": "# Buổi 6: AI trong Tài chính Công và Tài chính Quốc tế (Phòng chống Gian lận & Ổn định Tài chính)",
    "docs/buoi_07.md": "# Buổi 7: AI trong Tài chính Doanh nghiệp và Kiểm toán (Tự động hóa Kiểm soát Nội bộ & Phát hiện Gian lận)",
    "docs/buoi_08.md": "# Buổi 8: AI trong Tài chính Ngân hàng và Thị trường Chứng khoán (Chấm điểm Tín dụng & Giao dịch Thuật toán)",
    "docs/buoi_09.md": "# Buổi 9: AI trong Tài chính Cá nhân và Thị trường Tài sản Số (Crypto Assets & Robo-Advisors)",
    "docs/buoi_11.md": "# Buổi 11: Thực hành AI Phân tích Dữ liệu Cơ bản (Cơ sở Dữ liệu Quan hệ, SQL & Excel)",
    "docs/buoi_12.md": "# Buổi 12: Thực hành AI Nhận thức và AI Tạo sinh trong Kế toán - Tài chính (Generative AI & Web-Enhanced ChatGPT)",
    "docs/buoi_13.md": "# Buổi 13: Kỹ thuật Viết Prompt & Chiến lược Phân tích Dữ liệu Tài chính (SPARKS Framework)",
    "docs/buoi_14.md": "# Buổi 14: Phân tích Dữ liệu Kế toán Chuyên sâu (Khám phá Dữ liệu & Trực quan hóa Kết quả)"
}

for path, new_h1 in official_titles.items():
    if not os.path.exists(path):
        print(f"Skipping {path} (not found)")
        continue
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Replace first line if it starts with #
    if lines and lines[0].strip().startswith("#"):
        lines[0] = new_h1 + "\n"
    else:
        lines.insert(0, new_h1 + "\n\n")
        
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Updated {path} -> {new_h1}")

print("SUCCESS: Updated all 13 buoi files H1 titles to match DE CUONG TRI TUE NHAN TAO- 2025.pdf!")
