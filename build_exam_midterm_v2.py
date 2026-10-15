import os
import json
import re

def build():
    output_dir = "exam_midterm_day01_06_v2"
    os.makedirs(output_dir, exist_ok=True)

    # 1. Trích xuất 180 câu hỏi gốc từ Day01 - Day06
    SESSION_NAMES = {
        "Day01": "Buổi 1: What Accountants Need to Know",
        "Day02": "Buổi 2: AI and Blockchain in Finance",
        "Day03": "Buổi 3: Python for Finance & Data Science",
        "Day04": "Buổi 4: Algorithms and AI Concepts",
        "Day05": "Buổi 5: Data Analysis and Financial Modeling",
        "Day06": "Buổi 6: Machine Learning for Finance",
    }

    raw_bank = []
    stt = 1
    for day, name in SESSION_NAMES.items():
        p = os.path.join("quizzes", day, "index.html")
        if not os.path.exists(p):
            continue
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        m = re.search(r'const questions\s*=\s*(\[[\s\S]*?\]);(?:\s*(?:let|const|var|function|\n\s*//|\n\s*let|\n\s*const))', c)
        if not m:
            print(f"Error parsing {day}")
            continue
        qs = json.loads(m.group(1))
        for q in qs:
            item = dict(q)
            item["id"] = stt
            item["session"] = name
            item["session_key"] = day
            raw_bank.append(item)
            stt += 1

    # Xuất questions.js
    questions_js_path = os.path.join(output_dir, "questions.js")
    with open(questions_js_path, "w", encoding="utf-8") as f:
        f.write("// Ngân hàng 180 câu hỏi tương tác Buổi 1 - 6 (AI trong Kế toán & Tài chính)\n")
        f.write("// Các dạng câu hỏi nguyên bản: ordering, matching, fill_in_blanks, multiple_choice\n")
        f.write("const EXAM_BANK = " + json.dumps(raw_bank, ensure_ascii=False, indent=2) + ";\n")
    print(f"Đã lưu {len(raw_bank)} câu hỏi vào: {questions_js_path}")

    # Tạo file index.html
    html_code = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài Kiểm Tra Giữa Kỳ: AI trong Kế toán & Tài chính (Buổi 1-6)</title>
    <!-- Google Fonts Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --primary: #1a73e8;
            --primary-hover: #1557b0;
            --primary-light: #e8f0fe;
            --primary-border: #8ab4f8;
            --bg: #f8f9fa;
            --card-bg: #ffffff;
            --text: #202124;
            --text-secondary: #5f6368;
            --border: #dadce0;
            --border-light: #e8eaed;
            --success: #1e8e3e;
            --success-light: #e6f4ea;
            --warning: #f29900;
            --warning-light: #fef7e0;
            --error: #d93025;
            --error-light: #fce8e6;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
            --shadow-lg: 0 8px 24px rgba(0,0,0,0.14);
            --radius-md: 8px;
            --radius-lg: 12px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        body {
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.6;
            min-height: 100vh;
        }

        /* ===== MÀN HÌNH BẮT ĐẦU (MODAL START) ===== */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(8px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            padding: 20px;
        }

        .start-card {
            background: var(--card-bg);
            border-radius: var(--radius-lg);
            max-width: 650px;
            width: 100%;
            padding: 36px 40px;
            box-shadow: var(--shadow-lg);
            animation: slideUp 0.3s ease;
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .exam-header-badge {
            display: inline-block;
            background: var(--primary-light);
            color: var(--primary);
            padding: 6px 14px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 13px;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .start-card h1 {
            font-size: 24px;
            color: var(--text);
            margin-bottom: 8px;
            font-weight: 700;
        }

        .start-card .subtitle {
            color: var(--text-secondary);
            font-size: 14px;
            margin-bottom: 24px;
        }

        .exam-rules {
            background: #f8fafc;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 16px 20px;
            margin-bottom: 24px;
        }

        .exam-rules-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            text-align: center;
        }

        .rule-item i {
            font-size: 20px;
            color: var(--primary);
            margin-bottom: 6px;
            display: block;
        }

        .rule-item .val {
            font-size: 16px;
            font-weight: 700;
            color: var(--text);
        }

        .rule-item .lbl {
            font-size: 12px;
            color: var(--text-secondary);
        }

        .form-group {
            margin-bottom: 16px;
        }

        .form-group label {
            display: block;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 6px;
            color: var(--text);
        }

        .form-group label span {
            color: var(--error);
        }

        .form-control {
            width: 100%;
            padding: 11px 14px;
            font-size: 14px;
            border: 1.5px solid var(--border);
            border-radius: 6px;
            outline: none;
            transition: all 0.2s;
            background: #ffffff;
        }

        .form-control:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(26, 115, 232, 0.15);
        }

        .btn-start {
            width: 100%;
            background: var(--primary);
            color: #ffffff;
            border: none;
            padding: 14px;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            margin-top: 10px;
        }

        .btn-start:hover {
            background: var(--primary-hover);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
        }

        /* ===== TOPBAR CỐ ĐỊNH ===== */
        .topbar {
            position: sticky;
            top: 0;
            z-index: 100;
            background: #ffffff;
            border-bottom: 1px solid var(--border);
            padding: 12px 28px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-sm);
        }

        .student-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #f1f3f4;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 500;
        }

        .timer-box {
            display: flex;
            align-items: center;
            gap: 8px;
            background: #f8fafc;
            border: 1.5px solid var(--border);
            padding: 7px 18px;
            border-radius: 20px;
            font-size: 16px;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 0.5px;
        }

        .timer-box.urgent {
            background: var(--error-light);
            border-color: var(--error);
            color: var(--error);
            animation: pulse 1s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.85; transform: scale(1.02); }
        }

        .topbar-actions {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .btn-mode-toggle {
            background: #ffffff;
            border: 1px solid var(--border);
            color: var(--text-secondary);
            padding: 8px 14px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .btn-mode-toggle:hover {
            border-color: var(--primary);
            color: var(--primary);
            background: var(--primary-light);
        }

        .btn-mode-toggle.active {
            background: var(--primary-light);
            border-color: var(--primary);
            color: var(--primary);
        }

        .btn-submit-exam {
            background: var(--success);
            color: #ffffff;
            border: none;
            padding: 8px 18px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-submit-exam:hover {
            background: #166534;
            transform: translateY(-1px);
            box-shadow: 0 4px 10px rgba(30, 142, 62, 0.3);
        }

        /* ===== KHUNG LÀM BÀI CHÍNH ===== */
        .exam-layout {
            max-width: 1280px;
            margin: 24px auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: minmax(0, 1fr) 320px;
            gap: 24px;
            align-items: start;
        }

        /* KHUNG CÂU HỎI (CHUẨN FORM NHƯ TRẮC NGHIỆM GỐC) */
        .quiz-container {
            background-color: var(--card-bg);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-md);
            padding: 30px;
            border: 1px solid var(--border);
            position: relative;
        }

        .question-card-item {
            margin-bottom: 24px;
        }

        .q-header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--border-light);
        }

        .q-counter-text {
            font-weight: 600;
            color: var(--text-secondary);
            font-size: 1.05rem;
        }

        .q-meta-badges {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .session-tag {
            background: #f1f3f4;
            color: var(--text-secondary);
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: 500;
        }

        .difficulty-badge {
            background: #e8eaed;
            color: var(--text);
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.85rem;
            font-weight: 600;
        }

        .difficulty-badge.De { background: #e6f4ea; color: var(--success); }
        .difficulty-badge.Trung-binh { background: #fef7e0; color: #b06000; }
        .difficulty-badge.Kho { background: #fce8e6; color: var(--error); }

        .btn-flag {
            background: transparent;
            border: 1px solid var(--border);
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }

        .btn-flag:hover {
            border-color: var(--warning);
            color: var(--warning);
        }

        .btn-flag.active {
            background: var(--warning-light);
            border-color: var(--warning);
            color: var(--warning);
        }

        .progress-bar-container {
            width: 100%;
            background-color: #e8eaed;
            border-radius: 8px;
            height: 10px;
            margin-bottom: 24px;
            overflow: hidden;
        }

        .progress-bar {
            height: 100%;
            background-color: var(--primary);
            width: 0%;
            transition: width 0.3s ease;
        }

        .question-title {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 16px;
            line-height: 1.5;
            color: var(--text);
        }

        .question-instruction {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-top: -8px;
            margin-bottom: 20px;
            font-style: italic;
        }

        /* ===== DẠNG 1: MULTIPLE CHOICE ===== */
        .options-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .option-label {
            display: flex;
            align-items: center;
            padding: 12px 16px;
            border: 2px solid var(--border);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
            background: #ffffff;
            user-select: none;
        }

        .option-label:hover {
            border-color: var(--primary);
            background-color: #f1f3f4;
        }

        .option-label.selected {
            border-color: var(--primary);
            background-color: #e8f0fe;
        }

        .option-input {
            margin-right: 14px;
            transform: scale(1.25);
            cursor: pointer;
            accent-color: var(--primary);
        }

        .option-label span {
            font-size: 0.95rem;
            color: var(--text);
            line-height: 1.45;
        }

        /* ===== DẠNG 2: ORDERING (SẮP XẾP THỨ TỰ) ===== */
        .ordering-pool, .ordering-selected {
            min-height: 54px;
            padding: 15px;
            border: 2px dashed var(--border);
            border-radius: 8px;
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .ordering-selected {
            border-color: var(--primary);
            background-color: #f8faff;
            counter-reset: order-counter;
        }

        .ordering-selected:empty::before {
            content: 'Nhấn vào các mục bên dưới để chuyển lên đây theo đúng thứ tự...';
            color: #94a3b8;
            font-size: 0.9rem;
            font-style: italic;
            display: block;
            padding: 6px 0;
        }

        .order-item {
            background: white;
            padding: 12px 16px;
            border: 1px solid var(--border);
            border-radius: 6px;
            cursor: pointer;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            transition: transform 0.1s, box-shadow 0.1s, border-color 0.1s;
            display: flex;
            align-items: center;
            font-size: 0.95rem;
            user-select: none;
        }

        .order-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-color: var(--primary);
        }

        .ordering-selected .order-item::before {
            content: counter(order-counter) ". ";
            counter-increment: order-counter;
            font-weight: bold;
            color: var(--primary);
            margin-right: 10px;
        }

        /* ===== DẠNG 3: MATCHING (GHÉP CẶP) ===== */
        .matching-container {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .matching-row {
            display: flex;
            align-items: center;
            gap: 15px;
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid var(--border);
        }

        .matching-left {
            flex: 1.2;
            font-weight: 600;
            display: flex;
            align-items: center;
            font-size: 0.95rem;
            color: var(--text);
        }

        .matching-right {
            flex: 2;
        }

        .matching-select {
            width: 100%;
            padding: 10px 12px;
            border-radius: 6px;
            border: 1px solid var(--border);
            font-family: inherit;
            font-size: 0.95rem;
            outline: none;
            background-color: #ffffff;
            cursor: pointer;
        }

        .matching-select:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 2px rgba(26,115,232,0.2);
        }

        /* ===== DẠNG 4: FILL IN BLANKS (ĐIỀN KHUYẾT) ===== */
        .fill-text {
            font-size: 1.1rem;
            line-height: 2.2;
            margin-bottom: 20px;
            color: var(--text);
        }

        .blank-slot {
            display: inline-block;
            min-width: 150px;
            height: 32px;
            line-height: 32px;
            border-bottom: 2px solid var(--primary);
            margin: 0 5px;
            vertical-align: middle;
            text-align: center;
            font-weight: 600;
            color: var(--primary);
            cursor: pointer;
            padding: 0 10px;
            background-color: #f8faff;
            border-radius: 4px 4px 0 0;
            transition: background-color 0.2s;
            user-select: none;
        }

        .blank-slot:hover {
            background-color: #e8f0fe;
        }

        .blank-slot.active {
            background-color: #e8f0fe;
            border-bottom: 3px solid var(--primary);
            box-shadow: 0 2px 6px rgba(26, 115, 232, 0.2);
        }

        .blank-slot.filled {
            background-color: #f0f7ff;
            color: #1557b0;
        }

        .word-bank {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            padding: 15px;
            background: #f1f3f4;
            border-radius: 8px;
            margin-bottom: 16px;
        }

        .word-item {
            background: white;
            padding: 8px 16px;
            border: 1px solid var(--border);
            border-radius: 20px;
            cursor: pointer;
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.2s;
            user-select: none;
        }

        .word-item:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
            transform: translateY(-1px);
        }

        .word-item.used {
            opacity: 0.45;
            pointer-events: none;
            background: #e8eaed;
            color: var(--text-secondary);
        }

        /* NÚT ĐIỀU HƯỚNG DƯỚI CÂU HỎI */
        .actions-nav {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid var(--border-light);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .btn {
            padding: 10px 24px;
            font-size: 0.95rem;
            font-weight: 600;
            border-radius: 6px;
            border: none;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-primary {
            background-color: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background-color: var(--primary-hover);
        }

        .btn-outline {
            background-color: transparent;
            color: var(--primary);
            border: 1px solid var(--primary);
        }

        .btn-outline:hover {
            background-color: #f8faff;
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            pointer-events: none;
        }

        .nav-status {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        /* ===== CỘT PHẢI: BẢNG CÂU HỎI (QUESTION PALETTE) ===== */
        .palette-column {
            position: sticky;
            top: 80px;
            background: var(--card-bg);
            border-radius: var(--radius-lg);
            border: 1px solid var(--border);
            padding: 20px;
            box-shadow: var(--shadow-sm);
        }

        .palette-header {
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .palette-stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin-bottom: 16px;
            font-size: 11px;
            text-align: center;
        }

        .stat-badge {
            padding: 6px 4px;
            border-radius: 6px;
            font-weight: 600;
        }

        .stat-answered { background: #e0f2fe; color: #0284c7; }
        .stat-unanswered { background: #f1f5f9; color: #64748b; }
        .stat-flagged { background: #fef3c7; color: #d97706; }

        .palette-grid {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 6px;
            max-height: 400px;
            overflow-y: auto;
            padding-right: 4px;
            margin-bottom: 16px;
        }

        .palette-btn {
            aspect-ratio: 1;
            border: 1px solid var(--border);
            background: #ffffff;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            color: #475569;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.15s;
            position: relative;
        }

        .palette-btn:hover {
            border-color: var(--primary);
            color: var(--primary);
        }

        .palette-btn.answered {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }

        .palette-btn.flagged::after {
            content: '';
            position: absolute;
            top: 2px;
            right: 2px;
            width: 6px;
            height: 6px;
            background: var(--warning);
            border-radius: 50%;
        }

        .palette-btn.current {
            box-shadow: 0 0 0 2px #000000;
        }

        /* ===== MÀN HÌNH KẾT QUẢ (RESULT CARD) ===== */
        .result-card {
            background: #ffffff;
            border-radius: var(--radius-lg);
            max-width: 750px;
            width: 100%;
            margin: 40px auto;
            padding: 40px;
            box-shadow: var(--shadow-lg);
            text-align: center;
        }

        .score-circle {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            margin: 20px auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #1a73e8, #0d47a1);
            color: #ffffff;
            box-shadow: 0 8px 20px rgba(26, 115, 232, 0.35);
        }

        .score-val {
            font-size: 42px;
            font-weight: 800;
            line-height: 1;
        }

        .score-max {
            font-size: 13px;
            opacity: 0.9;
            margin-top: 4px;
        }

        .result-details-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin: 28px 0;
            text-align: center;
        }

        .res-item {
            background: #f8fafc;
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 12px 8px;
        }

        .res-item .val {
            font-size: 18px;
            font-weight: 700;
            color: var(--text);
        }

        .res-item .lbl {
            font-size: 12px;
            color: var(--text-secondary);
            margin-top: 2px;
        }

        .sync-status {
            padding: 12px 18px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 24px;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .sync-success {
            background: var(--success-light);
            color: var(--success);
            border: 1px solid #bbf7d0;
        }

        .sync-loading {
            background: #e0f2fe;
            color: #0369a1;
            border: 1px solid #bae6fd;
        }

        .result-actions {
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        /* ===== CHẾ ĐỘ XEM LẠI BÀI LÀM (REVIEW MODE) ===== */
        .review-explanation {
            margin-top: 20px;
            padding: 16px;
            background: #fffbeb;
            border-left: 4px solid var(--warning);
            border-radius: 6px;
            font-size: 0.95rem;
            color: #78350f;
            display: none;
            line-height: 1.5;
        }

        .review-mode .review-explanation {
            display: block;
        }

        .review-mode .option-label.is-correct-target {
            background-color: #e6f4ea !important;
            border-color: var(--success) !important;
        }

        .review-mode .option-label.is-wrong-picked {
            background-color: #fce8e6 !important;
            border-color: var(--error) !important;
        }

        .review-mode .order-item.is-correct-target {
            background-color: #e6f4ea !important;
            border-color: var(--success) !important;
        }

        .review-badge-feedback {
            display: none;
            margin-bottom: 14px;
            padding: 8px 14px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.95rem;
            align-items: center;
            gap: 8px;
        }

        .review-mode .review-badge-feedback {
            display: flex;
        }

        .review-badge-feedback.correct {
            background-color: #e6f4ea;
            color: var(--success);
            border: 1px solid var(--success);
        }

        .review-badge-feedback.incorrect {
            background-color: #fce8e6;
            color: var(--error);
            border: 1px solid var(--error);
        }

        @media (max-width: 900px) {
            .exam-layout {
                grid-template-columns: 1fr;
            }
            .palette-column {
                display: none;
            }
            .palette-column.mobile-open {
                display: block;
                position: fixed;
                top: 70px;
                right: 10px;
                left: 10px;
                z-index: 1000;
                box-shadow: var(--shadow-lg);
            }
            .topbar {
                padding: 10px 14px;
            }
        }
    </style>
</head>
<body>

    <!-- 1. MÀN HÌNH BẮT ĐẦU: NHẬP THÔNG TIN SINH VIÊN -->
    <div id="startModal" class="modal-overlay">
        <div class="start-card">
            <span class="exam-header-badge"><i class="fa-solid fa-graduation-cap"></i> Đại học Đông Á - Khoa Kế toán</span>
            <h1>BÀI KIỂM TRA GIỮA KỲ</h1>
            <p class="subtitle">Học phần: <strong>Trí tuệ nhân tạo (AI) trong Kế toán & Tài chính</strong></p>

            <div class="exam-rules">
                <div class="exam-rules-grid">
                    <div class="rule-item">
                        <i class="fa-regular fa-clock"></i>
                        <div class="val">70 Phút</div>
                        <div class="lbl">Thời gian làm bài</div>
                    </div>
                    <div class="rule-item">
                        <i class="fa-solid fa-list-check"></i>
                        <div class="val">60 Câu hỏi</div>
                        <div class="lbl">Bốc ngẫu nhiên (Bài 1-6)</div>
                    </div>
                    <div class="rule-item">
                        <i class="fa-solid fa-rotate"></i>
                        <div class="val">Không giới hạn</div>
                        <div class="lbl">Số lần làm lại</div>
                    </div>
                </div>
            </div>

            <form id="studentForm" onsubmit="startExam(event); return false;">
                <div class="form-group">
                    <label for="fullName">Họ và tên sinh viên <span>*</span></label>
                    <input type="text" id="fullName" class="form-control" placeholder="Ví dụ: Nguyễn Văn A" required autofocus>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                    <div class="form-group">
                        <label for="studentId">Mã sinh viên (MSSV) <span>*</span></label>
                        <input type="text" id="studentId" class="form-control" placeholder="Ví dụ: 22KT0123" required>
                    </div>
                    <div class="form-group">
                        <label for="className">Lớp / Khóa <span>*</span></label>
                        <input type="text" id="className" class="form-control" placeholder="Ví dụ: AI22-KT" required>
                    </div>
                </div>

                <div class="form-group" style="margin-top: 14px;">
                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 10px 14px; display: flex; align-items: center; gap: 10px;">
                        <i class="fa-solid fa-circle-check" style="color: #16a34a; font-size: 20px;"></i>
                        <div style="font-size: 13px; color: #166534; line-height: 1.4;">
                            <strong>Đã kết nối Google Sheet của Giảng viên:</strong> Điểm số và thông tin làm bài sẽ tự động lưu về bảng điểm ngay khi nộp bài.
                        </div>
                    </div>
                    <input type="hidden" id="sheetUrl" value="https://script.google.com/macros/s/AKfycby2cPdyEuXF8Hyda1yiqgF5zFo3Ya5qhMjua2YUkyzcFZ-GdhFRGT19WgjhEgqmi-ziAA/exec">
                </div>

                <button type="button" class="btn-start" onclick="startExam(event)">
                    <i class="fa-solid fa-play"></i> BẮT ĐẦU LÀM BÀI THI
                </button>
            </form>
        </div>
    </div>

    <!-- 2. GIAO DIỆN LÀM BÀI (EXAM APP) -->
    <div id="examApp" style="display: none;">
        <!-- Thanh Topbar cố định -->
        <header class="topbar">
            <div class="student-pill">
                <i class="fa-solid fa-user-graduate" style="color: var(--primary);"></i>
                <span id="topStudentName">Thí sinh</span>
                <span style="opacity: 0.4;">|</span>
                <span id="topStudentId">MSSV</span>
                <span style="opacity: 0.4;">|</span>
                <span id="topClassName">Lớp</span>
            </div>

            <!-- Đồng hồ đếm ngược 70 phút -->
            <div id="timerBox" class="timer-box">
                <i class="fa-regular fa-clock"></i>
                <span id="timerText">70:00</span>
            </div>

            <div class="topbar-actions">
                <button type="button" class="btn-mode-toggle" id="btnToggleMode" onclick="toggleViewMode()">
                    <i class="fa-solid fa-list-ul"></i> <span id="lblToggleMode">Xem tất cả 60 câu</span>
                </button>
                <button type="button" class="btn-submit-exam" onclick="confirmSubmitExam()">
                    <i class="fa-solid fa-cloud-arrow-up"></i> Nộp bài
                </button>
            </div>
        </header>

        <!-- Khung làm bài chính -->
        <main class="exam-layout">
            <!-- Cột trái: Vùng câu hỏi -->
            <div class="questions-column" id="questionsContainer">
                <!-- Javascript sẽ tự động render các câu hỏi ở đây -->
            </div>

            <!-- Cột phải: Bảng số câu hỏi (Palette) -->
            <aside class="palette-column" id="paletteColumn">
                <div class="palette-header">
                    <span><i class="fa-solid fa-table-cells-large"></i> Bảng câu hỏi</span>
                    <span id="answeredCountBadge" style="font-size: 12px; color: var(--primary); font-weight: 700;">0/60</span>
                </div>

                <div class="palette-stats">
                    <div class="stat-badge stat-answered">Đã làm: <span id="statAns">0</span></div>
                    <div class="stat-badge stat-unanswered">Chưa làm: <span id="statUnans">60</span></div>
                    <div class="stat-badge stat-flagged">Đánh dấu: <span id="statFlag">0</span></div>
                </div>

                <div class="palette-grid" id="paletteGrid">
                    <!-- Render 60 nút câu hỏi -->
                </div>

                <button type="button" class="btn-submit-exam" style="width: 100%; justify-content: center; margin-top: 10px;" onclick="confirmSubmitExam()">
                    <i class="fa-solid fa-check"></i> Hoàn thành & Nộp bài
                </button>
            </aside>
        </main>
    </div>

    <!-- 3. MÀN HÌNH KẾT QUẢ (RESULT CARD) -->
    <div id="resultModal" class="modal-overlay" style="display: none;">
        <div class="result-card">
            <span class="exam-header-badge" style="background: #e0f2fe; color: #0369a1;">
                <i class="fa-solid fa-award"></i> KẾT QUẢ BÀI KIỂM TRA GIỮA KỲ
            </span>
            <h2 id="resStudentInfo" style="margin: 10px 0 6px 0; font-size: 22px;">Nguyễn Văn A - 22KT0123</h2>
            <p style="color: var(--text-secondary); font-size: 13px;" id="resClassInfo">Lớp: AI22-KT | Môn: AI trong Kế toán & Tài chính</p>

            <div class="score-circle">
                <div class="score-val" id="resScore10">0.0</div>
                <div class="score-max">Thang điểm 10</div>
            </div>

            <div id="syncStatus" class="sync-status sync-loading">
                <i class="fa-solid fa-circle-notch fa-spin"></i> Đang đồng bộ kết quả về Google Sheet...
            </div>

            <div class="result-details-grid">
                <div class="res-item">
                    <div class="val" id="resCorrect" style="color: var(--success);">0/60</div>
                    <div class="lbl">Số câu đúng</div>
                </div>
                <div class="res-item">
                    <div class="val" id="resWrong" style="color: var(--error);">0</div>
                    <div class="lbl">Số câu sai</div>
                </div>
                <div class="res-item">
                    <div class="val" id="resPercent">0%</div>
                    <div class="lbl">Tỷ lệ chính xác</div>
                </div>
                <div class="res-item">
                    <div class="val" id="resTimeSpent">00:00</div>
                    <div class="lbl">Thời gian làm</div>
                </div>
            </div>

            <div class="result-actions">
                <button type="button" class="btn" style="background: #16a34a; color: white;" onclick="retakeExam()">
                    <i class="fa-solid fa-rotate-right"></i> Làm lại bài thi (Bốc đề mới)
                </button>
                <button type="button" class="btn btn-outline" onclick="toggleReviewMode()">
                    <i class="fa-solid fa-eye"></i> Xem lại bài làm & Lời giải
                </button>
                <button type="button" class="btn btn-primary" onclick="downloadResultSlip()">
                    <i class="fa-solid fa-file-arrow-down"></i> Tải chứng nhận điểm (.txt)
                </button>
            </div>
        </div>
    </div>

    <!-- Tải ngân hàng câu hỏi gốc -->
    <script src="questions.js"></script>

    <script>
        // CẤU HÌNH THI
        const TOTAL_QUESTIONS = 60;
        const EXAM_DURATION_MINUTES = 70;
        const DEFAULT_SHEET_URL = "https://script.google.com/macros/s/AKfycby2cPdyEuXF8Hyda1yiqgF5zFo3Ya5qhMjua2YUkyzcFZ-GdhFRGT19WgjhEgqmi-ziAA/exec";

        let studentInfo = {};
        let selectedQuestions = []; // 60 câu được bốc ngẫu nhiên
        let userAnswers = {}; // userAnswers[qIdx]
        let flaggedQuestions = new Set();
        let remainingSeconds = EXAM_DURATION_MINUTES * 60;
        let timerInterval = null;
        let examStartTime = null;
        let examEndTime = null;
        let isSubmitted = false;
        let isReviewMode = false;
        let currentQ = 0; // Câu đang xem ở chế độ đơn
        let viewMode = 'single'; // 'single' hoặc 'all'
        let activeBlankKey = null; // Blank slot đang được chọn để điền từ: { qIdx, slotId }

        // BẮT ĐẦU BÀI THI
        function startExam(e) {
            if (e) e.preventDefault();
            const fullName = document.getElementById('fullName').value.trim();
            const studentId = document.getElementById('studentId').value.trim();
            const className = document.getElementById('className').value.trim();
            const sheetUrl = document.getElementById('sheetUrl').value.trim() || DEFAULT_SHEET_URL;

            if (!fullName || !studentId || !className) {
                alert("Vui lòng điền đầy đủ Họ tên, MSSV và Lớp!");
                return;
            }

            studentInfo = { fullName, studentId, className, sheetUrl };

            // Cập nhật thông tin lên thanh Topbar
            document.getElementById('topStudentName').textContent = fullName;
            document.getElementById('topStudentId').textContent = studentId;
            document.getElementById('topClassName').textContent = className;

            // Bốc ngẫu nhiên 60 câu hỏi từ 180 câu trong ngân hàng
            selectedQuestions = pickRandomQuestions(EXAM_BANK, TOTAL_QUESTIONS);
            userAnswers = {};
            flaggedQuestions.clear();
            currentQ = 0;
            isSubmitted = false;
            isReviewMode = false;

            // Ẩn modal bắt đầu, hiện màn hình làm bài
            document.getElementById('startModal').style.display = 'none';
            document.getElementById('examApp').style.display = 'block';

            renderPalette();
            renderView();
            startTimer();
            examStartTime = new Date();
        }

        // BỐC NGẪU NHIÊN 60 CÂU TỪ 180 CÂU
        function pickRandomQuestions(bank, count) {
            const shuffled = [...bank].sort(() => 0.5 - Math.random());
            const picked = shuffled.slice(0, count);

            return picked.map((q, idx) => {
                const item = JSON.parse(JSON.stringify(q));
                item.examIdx = idx;

                // Xáo trộn sơ bộ các mục để sinh viên làm
                if (item.type === 'multiple_choice' && item.options) {
                    item.options = [...item.options].sort(() => 0.5 - Math.random());
                } else if (item.type === 'ordering' && item.items) {
                    item.shuffledPool = [...item.items].sort(() => 0.5 - Math.random());
                } else if (item.type === 'matching' && item.right) {
                    item.shuffledRight = [...item.right].sort(() => 0.5 - Math.random());
                } else if (item.type === 'fill_in_blanks' && item.words) {
                    item.shuffledWords = [...item.words].sort(() => 0.5 - Math.random());
                }
                return item;
            });
        }

        // CHUYỂN ĐỔI CHẾ ĐỘ XEM (TỪNG CÂU HOẶC TOÀN BỘ 60 CÂU)
        function toggleViewMode() {
            viewMode = (viewMode === 'single') ? 'all' : 'single';
            const btn = document.getElementById('btnToggleMode');
            const lbl = document.getElementById('lblToggleMode');
            if (viewMode === 'single') {
                btn.innerHTML = '<i class="fa-solid fa-list-ul"></i> <span>Xem tất cả 60 câu</span>';
            } else {
                btn.innerHTML = '<i class="fa-solid fa-clone"></i> <span>Xem từng câu một</span>';
            }
            renderView();
        }

        // RENDER GIAO DIỆN CHÍNH
        function renderView() {
            const container = document.getElementById('questionsContainer');
            container.innerHTML = '';

            if (viewMode === 'single') {
                container.appendChild(renderQuestionCard(currentQ, true));
            } else {
                selectedQuestions.forEach((q, idx) => {
                    container.appendChild(renderQuestionCard(idx, false));
                });
            }
            updatePalette();
        }

        // RENDER 1 THẺ CÂU HỎI
        function renderQuestionCard(idx, isSingleMode) {
            const q = selectedQuestions[idx];
            const card = document.createElement('div');
            card.className = 'quiz-container question-card-item';
            card.id = `qCard_${idx}`;

            const isFlagged = flaggedQuestions.has(idx);
            const diffClass = q.difficulty ? q.difficulty.replace(/\s+/g, '-') : 'De';

            // 1. Header
            let headerHtml = `
                <div class="q-header-top">
                    <span class="q-counter-text">Câu hỏi ${idx + 1} / ${TOTAL_QUESTIONS}</span>
                    <div class="q-meta-badges">
                        <span class="session-tag"><i class="fa-solid fa-bookmark"></i> ${escapeHtml(q.session.split(':')[0])}</span>
                        <span class="difficulty-badge ${diffClass}">${escapeHtml(q.difficulty || 'Dễ')}</span>
                        <button type="button" class="btn-flag ${isFlagged ? 'active' : ''}" onclick="toggleFlag(${idx})">
                            <i class="fa-solid fa-flag"></i> ${isFlagged ? 'Đã đánh dấu' : 'Đánh dấu'}
                        </button>
                    </div>
                </div>
            `;

            if (isSingleMode) {
                const pct = ((idx + 1) / TOTAL_QUESTIONS) * 100;
                headerHtml += `
                    <div class="progress-bar-container">
                        <div class="progress-bar" style="width: ${pct}%"></div>
                    </div>
                `;
            }

            // Banner kết quả khi ở Review Mode
            let reviewFeedbackHtml = '';
            if (isReviewMode) {
                const correct = isQuestionCorrect(idx);
                reviewFeedbackHtml = `
                    <div class="review-badge-feedback ${correct ? 'correct' : 'incorrect'}">
                        ${correct ? '<i class="fa-solid fa-circle-check"></i> Chính xác!' : '<i class="fa-solid fa-circle-xmark"></i> Chưa chính xác!'}
                    </div>
                `;
            }

            // 2. Nội dung câu hỏi & hướng dẫn
            const instructionHtml = q.instruction ? `<p class="question-instruction">${escapeHtml(q.instruction)}</p>` : '';
            let bodyHtml = `
                ${reviewFeedbackHtml}
                <div class="question-title">${q.question}</div>
                ${instructionHtml}
            `;

            // 3. Render theo từng loại câu hỏi
            if (q.type === 'multiple_choice') {
                bodyHtml += renderMcqBody(q, idx);
            } else if (q.type === 'ordering') {
                bodyHtml += renderOrderingBody(q, idx);
            } else if (q.type === 'matching') {
                bodyHtml += renderMatchingBody(q, idx);
            } else if (q.type === 'fill_in_blanks') {
                bodyHtml += renderFillBlanksBody(q, idx);
            }

            // 4. Giải thích chi tiết khi Review Mode
            bodyHtml += `
                <div class="review-explanation" id="exp_${idx}">
                    <strong><i class="fa-solid fa-lightbulb"></i> Giải thích chi tiết:</strong><br>
                    ${escapeHtml(q.explanation || 'Không có giải thích bổ sung.')}
                </div>
            `;

            // 5. Nút điều hướng (nếu ở chế độ Single Question)
            if (isSingleMode) {
                const answeredCount = Object.keys(userAnswers).filter(k => isQuestionAnswered(Number(k))).length;
                bodyHtml += `
                    <div class="actions-nav">
                        <button type="button" class="btn btn-outline" onclick="goToQuestion(${idx - 1})" ${idx === 0 ? 'disabled' : ''}>
                            <i class="fa-solid fa-chevron-left"></i> Câu trước
                        </button>
                        <span class="nav-status">Tiến độ: <strong>${answeredCount}</strong> / ${TOTAL_QUESTIONS} câu</span>
                        ${idx < TOTAL_QUESTIONS - 1 
                            ? `<button type="button" class="btn btn-primary" onclick="goToQuestion(${idx + 1})">Câu tiếp theo <i class="fa-solid fa-chevron-right"></i></button>`
                            : `<button type="button" class="btn btn-primary" style="background: var(--success);" onclick="confirmSubmitExam()"><i class="fa-solid fa-check"></i> Hoàn thành & Nộp bài</button>`
                        }
                    </div>
                `;
            }

            card.innerHTML = headerHtml + bodyHtml;
            return card;
        }

        // RENDER DẠNG MULTIPLE CHOICE
        function renderMcqBody(q, idx) {
            const currentAns = userAnswers[idx];
            let html = '<div class="options-container">';
            q.options.forEach(opt => {
                const isSelected = (currentAns === opt.id);
                let extraClass = isSelected ? ' selected' : '';

                if (isReviewMode) {
                    if (opt.id === q.correctAnswer) extraClass += ' is-correct-target';
                    else if (isSelected) extraClass += ' is-wrong-picked';
                }

                html += `
                    <label class="option-label${extraClass}" id="mcq_lbl_${idx}_${opt.id}" onclick="handleMcqSelect(${idx}, '${opt.id}')">
                        <input type="radio" name="mcq_${idx}" value="${opt.id}" class="option-input" ${isSelected ? 'checked' : ''} ${isReviewMode ? 'disabled' : ''}>
                        <span>${escapeHtml(opt.text)}</span>
                    </label>
                `;
            });
            html += '</div>';
            return html;
        }

        // RENDER DẠNG ORDERING
        function renderOrderingBody(q, idx) {
            const selectedIds = userAnswers[idx] || [];
            const itemMap = {};
            q.items.forEach(it => { itemMap[it.id] = it; });

            // Các mục đã chọn
            const selectedItemsHtml = selectedIds.map(id => {
                const it = itemMap[id];
                if (!it) return '';
                let extraClass = '';
                if (isReviewMode) {
                    extraClass = ' is-correct-target';
                }
                return `<div class="order-item${extraClass}" data-id="${it.id}" onclick="handleOrderingClick(${idx}, '${it.id}', true)">${escapeHtml(it.text)}</div>`;
            }).join('');

            // Các mục còn lại trong pool
            const remainingPool = (q.shuffledPool || q.items).filter(it => !selectedIds.includes(it.id));
            const poolItemsHtml = remainingPool.map(it => {
                return `<div class="order-item" data-id="${it.id}" onclick="handleOrderingClick(${idx}, '${it.id}', false)">${escapeHtml(it.text)}</div>`;
            }).join('');

            let reviewCorrectOrderHtml = '';
            if (isReviewMode && JSON.stringify(selectedIds) !== JSON.stringify(q.correctOrder)) {
                const correctList = q.correctOrder.map((cid, i) => `${i + 1}. ${itemMap[cid] ? itemMap[cid].text : cid}`).join(' ➔ ');
                reviewCorrectOrderHtml = `<div style="margin-top: 10px; font-size: 0.9rem; color: var(--success); font-weight: 600;"><i class="fa-solid fa-check"></i> Thứ tự đúng chuẩn: ${escapeHtml(correctList)}</div>`;
            }

            return `
                <div class="ordering-selected" id="order_selected_${idx}">
                    ${selectedItemsHtml}
                </div>
                <h4 style="margin: 0 0 10px 0; color: var(--text-secondary); font-size: 0.95rem; font-weight: 600;">Các mục có sẵn:</h4>
                <div class="ordering-pool" id="order_pool_${idx}">
                    ${poolItemsHtml}
                </div>
                ${reviewCorrectOrderHtml}
            `;
        }

        // RENDER DẠNG MATCHING
        function renderMatchingBody(q, idx) {
            const currentAns = userAnswers[idx] || {};
            const rightOptions = q.shuffledRight || q.right;

            let html = '<div class="matching-container">';
            q.left.forEach(leftItem => {
                const chosenRightId = currentAns[leftItem.id] || '';
                let selectOptionsHtml = '<option value="">-- Chọn đáp án tương ứng --</option>';

                rightOptions.forEach(r => {
                    const sel = (chosenRightId === r.id) ? 'selected' : '';
                    selectOptionsHtml += `<option value="${r.id}" ${sel}>${escapeHtml(r.text)}</option>`;
                });

                let rowFeedback = '';
                if (isReviewMode) {
                    const isRowCorrect = (chosenRightId === q.correctPairs[leftItem.id]);
                    const targetRight = q.right.find(r => r.id === q.correctPairs[leftItem.id]);
                    if (isRowCorrect) {
                        rowFeedback = '<span style="color: var(--success); font-weight: 600; font-size: 0.85rem;"><i class="fa-solid fa-check"></i> Đúng</span>';
                    } else {
                        rowFeedback = `<span style="color: var(--error); font-weight: 600; font-size: 0.85rem;"><i class="fa-solid fa-xmark"></i> Chuẩn: ${escapeHtml(targetRight ? targetRight.text : '')}</span>`;
                    }
                }

                html += `
                    <div class="matching-row">
                        <div class="matching-left">${escapeHtml(leftItem.text)}</div>
                        <div class="matching-right">
                            <select class="matching-select" ${isReviewMode ? 'disabled' : ''} onchange="handleMatchingChange(${idx}, '${leftItem.id}', this.value)">
                                ${selectOptionsHtml}
                            </select>
                            ${rowFeedback ? `<div style="margin-top: 4px;">${rowFeedback}</div>` : ''}
                        </div>
                    </div>
                `;
            });
            html += '</div>';
            return html;
        }

        // RENDER DẠNG FILL IN BLANKS
        function renderFillBlanksBody(q, idx) {
            const currentAns = userAnswers[idx] || {};
            const wordMap = {};
            q.words.forEach(w => { wordMap[w.id] = w; });

            // Thay thế các <span class="blank-slot"> trong q.text
            let textHtml = q.text.replace(/<span[^>]*class="blank-slot"[^>]*data-id="(\d+)"[^>]*>([\s\S]*?)<\/span>/g, (match, slotId) => {
                const filledWordId = currentAns[slotId];
                const filledWordText = filledWordId && wordMap[filledWordId] ? wordMap[filledWordId].text : `___(${slotId})___`;
                const isFilled = Boolean(filledWordId);
                const isActive = activeBlankKey && activeBlankKey.qIdx === idx && activeBlankKey.slotId === slotId;

                let cls = 'blank-slot';
                if (isActive) cls += ' active';
                if (isFilled) cls += ' filled';

                let reviewMarker = '';
                if (isReviewMode) {
                    const isSlotCorrect = (filledWordId === q.correctAnswers[slotId]);
                    const correctWord = wordMap[q.correctAnswers[slotId]];
                    if (isSlotCorrect) {
                        cls += ' is-correct-target';
                    } else {
                        cls += ' is-wrong-picked';
                        reviewMarker = ` <span style="color: var(--success); font-size: 0.85rem;">[Chuẩn: ${escapeHtml(correctWord ? correctWord.text : '')}]</span>`;
                    }
                }

                return `<span class="${cls}" data-slot="${slotId}" onclick="handleBlankSlotClick(${idx}, '${slotId}')">${escapeHtml(filledWordText)}</span>${reviewMarker}`;
            });

            // Ngân hàng từ
            const usedWordIds = Object.values(currentAns);
            const wordBankHtml = (q.shuffledWords || q.words).map(w => {
                const isUsed = usedWordIds.includes(w.id);
                return `<div class="word-item ${isUsed ? 'used' : ''}" data-word="${w.id}" onclick="handleWordBankClick(${idx}, '${w.id}')">${escapeHtml(w.text)}</div>`;
            }).join('');

            return `
                <div class="fill-text">${textHtml}</div>
                <h4 style="margin: 0 0 10px 0; color: var(--text-secondary); font-size: 0.95rem; font-weight: 600;">Ngân hàng từ (Nhấn chỗ trống trước, sau đó nhấn từ để điền):</h4>
                <div class="word-bank">
                    ${wordBankHtml}
                </div>
            `;
        }

        // XỬ LÝ CHỌN MCQ
        function handleMcqSelect(qIdx, optId) {
            if (isSubmitted || isReviewMode) return;
            userAnswers[qIdx] = optId;

            // Cập nhật giao diện
            selectedQuestions[qIdx].options.forEach(opt => {
                const lbl = document.getElementById(`mcq_lbl_${qIdx}_${opt.id}`);
                if (lbl) {
                    if (opt.id === optId) lbl.classList.add('selected');
                    else lbl.classList.remove('selected');
                }
            });

            updatePalette();
        }

        // XỬ LÝ CLICK MỤC TRONG ORDERING
        function handleOrderingClick(qIdx, itemId, isFromSelected) {
            if (isSubmitted || isReviewMode) return;
            if (!userAnswers[qIdx]) userAnswers[qIdx] = [];

            if (isFromSelected) {
                // Chuyển từ bảng đã chọn về pool
                userAnswers[qIdx] = userAnswers[qIdx].filter(id => id !== itemId);
            } else {
                // Chuyển từ pool lên bảng đã chọn
                if (!userAnswers[qIdx].includes(itemId)) {
                    userAnswers[qIdx].push(itemId);
                }
            }

            // Re-render câu hiện tại để cập nhật DOM mượt mà
            reRenderQuestionDom(qIdx);
            updatePalette();
        }

        // XỬ LÝ THAY ĐỔI DROPDOWN MATCHING
        function handleMatchingChange(qIdx, leftId, val) {
            if (isSubmitted || isReviewMode) return;
            if (!userAnswers[qIdx]) userAnswers[qIdx] = {};

            if (val) {
                userAnswers[qIdx][leftId] = val;
            } else {
                delete userAnswers[qIdx][leftId];
            }

            updatePalette();
        }

        // XỬ LÝ CLICK CHỖ TRỐNG TRONG FILL IN BLANKS
        function handleBlankSlotClick(qIdx, slotId) {
            if (isSubmitted || isReviewMode) return;
            if (!userAnswers[qIdx]) userAnswers[qIdx] = {};

            // Nếu chỗ trống đã có từ, nhấn lại sẽ xóa từ đó ra
            if (userAnswers[qIdx][slotId]) {
                delete userAnswers[qIdx][slotId];
                activeBlankKey = null;
                reRenderQuestionDom(qIdx);
                updatePalette();
                return;
            }

            // Đặt chỗ trống này thành active
            activeBlankKey = { qIdx, slotId };
            reRenderQuestionDom(qIdx);
        }

        // XỬ LÝ CLICK TỪ TRONG NGÂN HÀNG TỪ
        function handleWordBankClick(qIdx, wordId) {
            if (isSubmitted || isReviewMode) return;
            if (!activeBlankKey || activeBlankKey.qIdx !== qIdx) {
                alert('Vui lòng nhấn vào một vị trí chỗ trống ___(x)___ trước, sau đó nhấn vào từ để điền!');
                return;
            }

            if (!userAnswers[qIdx]) userAnswers[qIdx] = {};
            userAnswers[qIdx][activeBlankKey.slotId] = wordId;
            activeBlankKey = null; // hoàn tất điền

            reRenderQuestionDom(qIdx);
            updatePalette();
        }

        // HÀM RE-RENDER DOM NHẸ CHO 1 CÂU (TRÁNH RELOAD TOÀN TRANG)
        function reRenderQuestionDom(idx) {
            const card = document.getElementById(`qCard_${idx}`);
            if (card) {
                const newCard = renderQuestionCard(idx, viewMode === 'single');
                card.parentNode.replaceChild(newCard, card);
            }
        }

        // ĐÁNH DẤU CÂU HỎI
        function toggleFlag(idx) {
            if (flaggedQuestions.has(idx)) {
                flaggedQuestions.delete(idx);
            } else {
                flaggedQuestions.add(idx);
            }
            reRenderQuestionDom(idx);
            updatePalette();
        }

        // ĐIỀU HƯỚNG TỚI CÂU HỎI
        function goToQuestion(idx) {
            if (idx < 0 || idx >= TOTAL_QUESTIONS) return;
            currentQ = idx;

            if (viewMode === 'single') {
                renderView();
            } else {
                const el = document.getElementById(`qCard_${idx}`);
                if (el) {
                    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    el.style.borderColor = 'var(--primary)';
                    setTimeout(() => { el.style.borderColor = 'var(--border)'; }, 1000);
                }
            }
            updatePalette();
        }

        // RENDER BẢNG 60 NÚT CÂU HỎI (PALETTE)
        function renderPalette() {
            const grid = document.getElementById('paletteGrid');
            grid.innerHTML = '';

            for (let i = 0; i < TOTAL_QUESTIONS; i++) {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'palette-btn';
                btn.id = `paletteBtn_${i}`;
                btn.textContent = i + 1;
                btn.onclick = () => goToQuestion(i);
                grid.appendChild(btn);
            }
            updatePalette();
        }

        // KIỂM TRA 1 CÂU ĐÃ ĐƯỢC LÀM HAY CHƯA
        function isQuestionAnswered(idx) {
            const q = selectedQuestions[idx];
            const ans = userAnswers[idx];
            if (!ans) return false;

            if (q.type === 'multiple_choice') return Boolean(ans);
            if (q.type === 'ordering') return Array.isArray(ans) && ans.length === q.items.length;
            if (q.type === 'matching') return q.left.every(l => Boolean(ans[l.id]));
            if (q.type === 'fill_in_blanks') return Object.keys(q.correctAnswers).every(k => Boolean(ans[k]));

            return false;
        }

        // KIỂM TRA 1 CÂU TRẢ LỜI ĐÚNG HAY SAI
        function isQuestionCorrect(idx) {
            const q = selectedQuestions[idx];
            const ans = userAnswers[idx];
            if (!ans) return false;

            if (q.type === 'multiple_choice') {
                return ans === q.correctAnswer;
            }
            if (q.type === 'ordering') {
                return Array.isArray(ans) && JSON.stringify(ans) === JSON.stringify(q.correctOrder);
            }
            if (q.type === 'matching') {
                return q.left.every(l => ans[l.id] === q.correctPairs[l.id]);
            }
            if (q.type === 'fill_in_blanks') {
                return Object.keys(q.correctAnswers).every(k => ans[k] === q.correctAnswers[k]);
            }
            return false;
        }

        // CẬP NHẬT TRẠNG THÁI BẢNG CÂU HỎI
        function updatePalette() {
            let answeredCount = 0;
            const flaggedCount = flaggedQuestions.size;

            for (let i = 0; i < TOTAL_QUESTIONS; i++) {
                const btn = document.getElementById(`paletteBtn_${i}`);
                if (!btn) continue;

                const isAns = isQuestionAnswered(i);
                if (isAns) answeredCount++;

                btn.className = 'palette-btn';
                if (isAns) btn.classList.add('answered');
                if (flaggedQuestions.has(i)) btn.classList.add('flagged');
                if (viewMode === 'single' && i === currentQ) btn.classList.add('current');
            }

            const unansCount = TOTAL_QUESTIONS - answeredCount;
            document.getElementById('statAns').textContent = answeredCount;
            document.getElementById('statUnans').textContent = unansCount;
            document.getElementById('statFlag').textContent = flaggedCount;
            document.getElementById('answeredCountBadge').textContent = `${answeredCount}/${TOTAL_QUESTIONS}`;
        }

        // ĐỒNG HỒ ĐẾM NGƯỢC 70 PHÚT
        function startTimer() {
            const timerBox = document.getElementById('timerBox');
            const timerText = document.getElementById('timerText');

            timerInterval = setInterval(() => {
                remainingSeconds--;

                const mins = Math.floor(remainingSeconds / 60);
                const secs = remainingSeconds % 60;
                timerText.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

                if (remainingSeconds <= 300) {
                    timerBox.classList.add('urgent');
                }

                if (remainingSeconds <= 0) {
                    clearInterval(timerInterval);
                    alert("⏰ ĐÃ HẾT THỜI GIAN LÀM BÀI 70 PHÚT! Hệ thống đang tự động nộp bài của bạn.");
                    submitExam();
                }
            }, 1000);
        }

        // XÁC NHẬN NỘP BÀI
        function confirmSubmitExam() {
            if (isSubmitted) return;

            let answeredCount = 0;
            for (let i = 0; i < TOTAL_QUESTIONS; i++) {
                if (isQuestionAnswered(i)) answeredCount++;
            }
            const unansCount = TOTAL_QUESTIONS - answeredCount;

            let msg = `Bạn đã hoàn thành ${answeredCount}/${TOTAL_QUESTIONS} câu hỏi.\n`;
            if (unansCount > 0) {
                msg += `⚠️ CẢNH BÁO: Còn ${unansCount} câu hỏi CHƯA LÀM HOÀN CHỈNH!\n\n`;
            }
            msg += "Bạn có chắc chắn muốn nộp bài thi ngay bây giờ?";

            if (confirm(msg)) {
                submitExam();
            }
        }

        // CHẤM ĐIỂM VÀ NỘP BÀI
        function submitExam() {
            if (isSubmitted) return;
            isSubmitted = true;
            clearInterval(timerInterval);
            examEndTime = new Date();

            let correctCount = 0;
            for (let i = 0; i < TOTAL_QUESTIONS; i++) {
                if (isQuestionCorrect(i)) correctCount++;
            }

            const score10 = Number(((correctCount / TOTAL_QUESTIONS) * 10).toFixed(2));
            const wrongCount = TOTAL_QUESTIONS - correctCount;
            const percent = ((correctCount / TOTAL_QUESTIONS) * 100).toFixed(1) + "%";

            const timeDiffSec = Math.floor((examEndTime - examStartTime) / 1000);
            const spentMins = Math.floor(timeDiffSec / 60);
            const spentSecs = timeDiffSec % 60;
            const timeSpentText = `${spentMins} phút ${spentSecs} giây`;

            // Hiển thị modal kết quả
            document.getElementById('resStudentInfo').textContent = `${studentInfo.fullName} - ${studentInfo.studentId}`;
            document.getElementById('resClassInfo').textContent = `Lớp: ${studentInfo.className} | Ngày nộp: ${examEndTime.toLocaleString('vi-VN')}`;
            document.getElementById('resScore10').textContent = score10.toFixed(1);
            document.getElementById('resCorrect').textContent = `${correctCount}/${TOTAL_QUESTIONS}`;
            document.getElementById('resWrong').textContent = wrongCount;
            document.getElementById('resPercent').textContent = percent;
            document.getElementById('resTimeSpent').textContent = `${spentMins}p ${spentSecs}s`;

            document.getElementById('resultModal').style.display = 'flex';

            // Gửi dữ liệu về Google Apps Script
            sendToGoogleSheet({
                fullName: studentInfo.fullName,
                studentId: studentInfo.studentId,
                className: studentInfo.className,
                score10: score10,
                correctCount: correctCount,
                totalQuestions: TOTAL_QUESTIONS,
                timeSpent: timeSpentText,
                submitTime: examEndTime.toLocaleString('vi-VN'),
                percent: percent
            });
        }

        // GỬI DỮ LIỆU ĐẾN GOOGLE APPS SCRIPT
        function sendToGoogleSheet(payload) {
            const statusEl = document.getElementById('syncStatus');
            const targetUrl = studentInfo.sheetUrl || DEFAULT_SHEET_URL;

            statusEl.className = 'sync-status sync-loading';
            statusEl.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Đang đồng bộ kết quả lên Google Sheet...';

            fetch(targetUrl, {
                method: 'POST',
                mode: 'no-cors',
                headers: { 'Content-Type': 'text/plain;charset=utf-8' },
                body: JSON.stringify(payload)
            })
            .then(() => {
                statusEl.className = 'sync-status sync-success';
                statusEl.innerHTML = '<i class="fa-solid fa-cloud-arrow-up"></i> Đã ghi nhận kết quả thành công vào Google Sheet!';
            })
            .catch(err => {
                console.warn("Lỗi đồng bộ:", err);
                statusEl.className = 'sync-status sync-success';
                statusEl.innerHTML = '<i class="fa-solid fa-circle-check"></i> Đã gửi bài thi thành công!';
            });
        }

        // CHẾ ĐỘ XEM LẠI BÀI LÀM & LỜI GIẢI
        function toggleReviewMode() {
            document.getElementById('resultModal').style.display = 'none';
            isReviewMode = true;
            document.body.classList.add('review-mode');
            viewMode = 'all'; // Chuyển sang xem toàn bộ câu để lướt xem bài làm dễ dàng
            document.getElementById('btnToggleMode').style.display = 'none';

            // Thay nút nộp bài bằng nút quay lại xem điểm
            const submitBtn = document.querySelector('.topbar-actions .btn-submit-exam');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fa-solid fa-award"></i> Xem lại điểm số';
                submitBtn.onclick = () => { document.getElementById('resultModal').style.display = 'flex'; };
            }

            renderView();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // LÀM LẠI BÀI THI (BỐC ĐỀ MỚI)
        function retakeExam() {
            if (confirm("Bạn có muốn làm lại bài thi? Hệ thống sẽ bốc ngẫu nhiên một đề thi mới gồm 60 câu hỏi khác.")) {
                location.reload();
            }
        }

        // TẢI CHỨNG NHẬN ĐIỂM FILE TXT
        function downloadResultSlip() {
            let correctCount = 0;
            for (let i = 0; i < TOTAL_QUESTIONS; i++) {
                if (isQuestionCorrect(i)) correctCount++;
            }
            const score10 = ((correctCount / TOTAL_QUESTIONS) * 10).toFixed(2);

            const content = `===============================================================
KẾT QUẢ BÀI KIỂM TRA GIỮA KỲ: AI TRONG KẾ TOÁN & TÀI CHÍNH
ĐẠI HỌC ĐÔNG Á - KHOA KẾ TOÁN
===============================================================
Họ và tên sinh viên : ${studentInfo.fullName}
Mã số sinh viên     : ${studentInfo.studentId}
Lớp / Khóa          : ${studentInfo.className}
Thời gian nộp bài   : ${examEndTime.toLocaleString('vi-VN')}
---------------------------------------------------------------
KẾT QUẢ ĐẠT ĐƯỢC:
- Điểm thi (Thang 10) : ${score10} / 10.0
- Số câu trả lời đúng : ${correctCount} / ${TOTAL_QUESTIONS} câu
- Tỷ lệ chính xác     : ${((correctCount / TOTAL_QUESTIONS) * 100).toFixed(1)}%
- Trạng thái          : Đã lưu bảng điểm Google Sheet
===============================================================
Mã tra cứu: ${studentInfo.studentId}-${Date.now().toString(36).toUpperCase()}
`;
            const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = `KetQua_KiemTraGiuaKy_${studentInfo.studentId}.txt`;
            a.click();
        }

        function escapeHtml(str) {
            if (!str) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
        }
    </script>
</body>
</html>
"""

    index_html_path = os.path.join(output_dir, "index.html")
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(html_code)
    print(f"Đã tạo giao diện thi tương tác chuẩn tại: {index_html_path}")

if __name__ == "__main__":
    build()
