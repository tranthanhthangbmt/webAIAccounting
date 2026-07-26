# reformat_buoi_07.py
# Reformat docs/buoi_07.md to have a hierarchical, clean structure matching Buoi 1-6

import re

with open('docs/buoi_07.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Clean up stray OceanofPDF lines
text = re.sub(r'^\s*OceanofPDF\.com\s*$', '', text, flags=re.MULTILINE)

# 2. Replace Chapter 9 and first section
text = text.replace(
    "CHƯƠNG 9\nĐánh giá Kiểm soát Nội bộ Tự động (Automating Internal Controls Assessment)",
    "# 1. Đánh giá Kiểm soát Nội bộ Tự động (Automating Internal Controls Assessment)\n\n## 1.1 Giới thiệu và Bối cảnh Thực tiễn (Introduction and Practical Context)"
)

# 3. Replace uppercase headings in Chapter 9
text = text.replace(
    "TỰ ĐỘNG HÓA ĐÁNH GIÁ KIỂM SOÁT NỘI BỘ (AUTOMATING INTERNAL CONTROLS ASSESSMENT)",
    "## 1.2 Tự động hóa Đánh giá Kiểm soát Nội bộ (Automating Internal Controls Assessment)"
)
text = text.replace(
    "MÔI TRƯỜNG KIỂM SOÁT TỰ ĐỘNG (AUTOMATED CONTROL ENVIRONMENT)",
    "## 1.3 Môi trường Kiểm soát Tự động (Automated Control Environment)"
)
text = text.replace(
    "ĐÁNH GIÁ RỦI RO TỰ ĐỘNG (AUTOMATED RISK ASSESSMENT)",
    "## 1.4 Đánh giá Rủi ro Tự động (Automated Risk Assessment)"
)
text = text.replace(
    "\nCÁC HOẠT ĐỘNG KIỂM SOÁT (CONTROL ACTIVITIES)\n",
    "\n## 1.5 Các Hoạt động Kiểm soát Tự động (Control Activities)\n"
)
text = text.replace(
    "\nGIÁM SÁT TỰ ĐỘNG (AUTOMATED MONITORING)\n",
    "\n## 1.6 Giám sát Tự động (Automated Monitoring)\n"
)
text = text.replace(
    "\nTHÔNG TIN VÀ TRUYỀN THÔNG (INFORMATION AND COMMUNICATIONS)\n",
    "\n## 1.7 Thông tin và Truyền thông (Information and Communications)\n"
)
text = text.replace(
    "\nRỦI RO KIỂM SOÁT VÀ CÁC BƯỚC TIẾP THEO (CONTROL RISK AND NEXT STEPS)\n",
    "\n## 1.8 Rủi ro Kiểm soát và Các Bước Tiếp theo (Control Risk and Next Steps)\n"
)

# Replace first reference heading
text = text.replace(
    "\nTÀI LIỆU THAM KHẢO (REFERENCES)\n",
    "\n## 1.9 Tài liệu Tham khảo (References - Chương 9)\n",
    1
)

# 4. Replace Chapter 12 and first section
text = text.replace(
    "CHƯƠNG 12\nTự động hóa Thông minh trong Phát hiện Gian lận (Intelligent Automation of Fraud Detection)",
    "# 2. Tự động hóa Thông minh trong Phát hiện Gian lận (Intelligent Automation of Fraud Detection)\n\n## 2.1 Khái niệm và Vai trò của Phát hiện Gian lận Thông minh (IFFDI Introduction)"
)

text = text.replace(
    "\nPHÁT HIỆN GIAN LẬN (DETECTING FRAUD)\n",
    "\n## 2.2 Phát hiện Gian lận và Cây Gian lận (Detecting Fraud and The Fraud Tree)\n"
)
text = text.replace(
    "\nCÁC YẾU TỐ CỦA GIAN LẬN (ELEMENTS OF FRAUD)\n",
    "\n## 2.3 Các Yếu tố của Gian lận và Tam giác Gian lận (Elements of Fraud)\n"
)
text = text.replace(
    "\nPHÁT HIỆN GIAN LẬN ĐẶC THÙ THEO LĨNH VỰC (DOMAIN-SPECIFIC FRAUD DETECTION)\n",
    "\n## 2.4 Phát hiện Gian lận Đặc thù theo Lĩnh vực (Domain-Specific Fraud Detection)\n"
)
text = text.replace(
    "\nSTOPSCAM\n",
    "\n## 2.5 Mô hình STOPSCAM trong Phát hiện Gian lận (STOPSCAM Framework)\n"
)

# Format STOPSCAM items as bullet points
text = text.replace("\nChiến lược (Strategy)\n", "\n- **S - Chiến lược (Strategy)**: ")
text = text.replace("\nCác giao dịch (Transactions)\n", "\n- **T - Các giao dịch (Transactions)**: ")
text = text.replace("\nCác hoạt động (Operations)\n", "\n- **O - Các hoạt động (Operations)**: ")
text = text.replace("\nCác quy trình (Processes)\n", "\n- **P - Các quy trình (Processes)**: ")
text = text.replace("\nBáo cáo/Tuyên bố (Statements)\n", "\n- **S - Báo cáo/Tuyên bố (Statements)**: ")
text = text.replace("\nVăn hóa (Culture)\n", "\n- **C - Văn hóa (Culture)**: ")
text = text.replace("\nThái độ (Attitude)\n", "\n- **A - Thái độ (Attitude)**: ")
text = text.replace("\nMô hình (Model)\n", "\n- **M - Mô hình (Model)**: ")

text = text.replace(
    "\nCÁC CÔNG NGHỆ VÀ MÔ HÌNH (TECHNOLOGIES AND MODELS)\n",
    "\n## 2.6 Các Công nghệ và Mô hình AI trong Phát hiện Gian lận (Technologies and Models)\n"
)
text = text.replace(
    "\nCÁCH TIẾP CẬN CỦA CHÚNG TÔI (OUR APPROACH)\n",
    "\n## 2.7 Cách tiếp cận Thực tiễn của Chúng tôi (Our Approach)\n"
)

# Replace second reference heading
text = text.replace(
    "\nTÀI LIỆU THAM KHẢO (REFERENCES)\n",
    "\n## 2.8 Tài liệu Tham khảo (References - Chương 12)\n"
)

# 5. Fix figure captions for the 3 figures
text = text.replace(
    '<div style="color: #666; font-style: italic; font-size: 0.9em;">FIGURE 9.1 Automation of Internal Controls Evaluation</div>',
    '<div style="color: #666; font-style: italic; font-size: 0.9em;">Hình 9.1: Tự động hóa Đánh giá Kiểm soát Nội bộ (FIGURE 9.1 Automation of Internal Controls Evaluation)</div>'
)
text = text.replace(
    '<div style="color: #666; font-style: italic; font-size: 0.9em;">FIGURE 9.2 Automated Environment Evaluation</div>',
    '<div style="color: #666; font-style: italic; font-size: 0.9em;">Hình 9.2: Đánh giá Môi trường Kiểm soát Tự động (FIGURE 9.2 Automated Environment Evaluation)</div>'
)
text = text.replace(
    '<div style="color: #666; font-style: italic; font-size: 0.9em;">FIGURE 12.1 The Fraud Tree</div>',
    '<div style="color: #666; font-style: italic; font-size: 0.9em;">Hình 12.1: Cây Gian lận ACFE (FIGURE 12.1 The Fraud Tree)</div>'
)

# Clean up any triple or more blank lines
text = re.sub(r'\n{3,}', '\n\n', text)

with open('docs/buoi_07.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully reformatted docs/buoi_07.md!")
