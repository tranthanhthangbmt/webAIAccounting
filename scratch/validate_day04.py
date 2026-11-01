import os
import re

base_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day04_Extra"

files_to_check = [
    os.path.join(base_dir, "index.html"),
    os.path.join(base_dir, "papers", "index.html"),
    os.path.join(base_dir, "papers", "paper_1_Is_It_All_Hype_ChatGPT_Accounting_tiengviet.html"),
    os.path.join(base_dir, "papers", "paper_1_Is_It_All_Hype_ChatGPT_Accounting_tiengviet.md"),
    os.path.join(base_dir, "papers", "paper_2_AuditCopilot_LLM_Fraud_Detection_tiengviet.html"),
    os.path.join(base_dir, "papers", "paper_2_AuditCopilot_LLM_Fraud_Detection_tiengviet.md"),
    os.path.join(base_dir, "slides", "thumbnails", "P1_cover.png"),
    os.path.join(base_dir, "slides", "thumbnails", "P2_cover.png"),
    os.path.join(base_dir, "slides", "thumbnails", "P3_cover.png"),
    os.path.join(base_dir, "videos", "P1_lý thuyết_Generative_AI_trong_Kế_toán_và_Kiểm_toán", "index.html"),
    os.path.join(base_dir, "videos", "P2_is it all hype_ChatGPT_in_Accounting", "index.html"),
    os.path.join(base_dir, "videos", "P3_AuditCopilot_for_Audit_Fraud_Detection", "index.html")
]

print("=== Checking Day04_Extra Core Files ===")
all_ok = True
for f in files_to_check:
    exists = os.path.exists(f)
    size = os.path.getsize(f) if exists else 0
    rel = os.path.relpath(f, base_dir)
    status = "OK" if exists and size > 0 else "MISSING / EMPTY"
    if not (exists and size > 0):
        all_ok = False
    print(f"[{status}] {rel} ({size:,} bytes)")

# Check slide images count
print("\n=== Checking Slide Images (15 per deck) ===")
for folder in ["P1_lý thuyết_Generative_AI_trong_Kế_toán_và_Kiểm_toán", "P2_is it all hype_ChatGPT_in_Accounting", "P3_AuditCopilot_for_Audit_Fraud_Detection"]:
    img_dir = os.path.join(base_dir, "videos", folder, "images")
    if os.path.exists(img_dir):
        imgs = [i for i in os.listdir(img_dir) if i.endswith(".png")]
        print(f"  {folder}: {len(imgs)} images")
    else:
        print(f"  {folder}: Images directory missing!")
        all_ok = False

print("\nAll files verified successfully!" if all_ok else "\nSome files need attention!")

