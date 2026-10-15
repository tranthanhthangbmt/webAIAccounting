import os
import json
import copy
from export_all_quizzes import extract_all_questions

def build_exam():
    output_dir = "exam_midterm_day01_06"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Trích xuất 180 câu hỏi Buổi 1-6
    print("Trích xuất câu hỏi từ Buổi 1 đến Buổi 6...")
    all_qs = extract_all_questions()
    target_sessions = ["Day01", "Day02", "Day03", "Day04", "Day05", "Day06"]
    
    filtered_qs = []
    stt = 1
    for q in all_qs:
        if q["session_key"] in target_sessions:
            q_clean = {
                "id": stt,
                "session": q["session_name"],
                "difficulty": q["difficulty"],
                "question": q["question"],
                "options": q["options"], # {"A": "...", "B": "...", "C": "...", "D": "..."}
                "correct": q["correct"], # "A", "B", "C", or "D"
                "explanation": q["explanation"]
            }
            filtered_qs.append(q_clean)
            stt += 1
            
    print(f"Tổng số câu hỏi trong ngân hàng: {len(filtered_qs)}")
    
    # 2. Xuất file questions.js
    questions_js_path = os.path.join(output_dir, "questions.js")
    with open(questions_js_path, "w", encoding="utf-8") as f:
        f.write("// Ngân hàng 180 câu hỏi trắc nghiệm Buổi 1 - 6 (AI trong Kế toán & Tài chính)\n")
        f.write("const EXAM_BANK = " + json.dumps(filtered_qs, ensure_ascii=False, indent=2) + ";\n")
    print(f"Đã tạo: {questions_js_path}")
    
    # 3. Tạo index.html (Ứng dụng thi trực tuyến đỉnh cao)
    index_html_content = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài Kiểm Tra Giữa Kỳ: AI trong Kế toán & Tài chính (Buổi 1-6)</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --primary: #1a73e8;
            --primary-dark: #1557b0;
            --primary-light: #e8f0fe;
            --success: #2e7d32;
            --success-light: #e8f5e9;
            --warning: #f57c00;
            --warning-light: #fff3e0;
            --danger: #d32f2f;
            --danger-light: #ffebee;
            --text-main: #202124;
            --text-muted: #5f6368;
            --bg-body: #f8f9fa;
            --card-bg: #ffffff;
            --border-color: #dadce0;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
            --shadow-lg: 0 8px 24px rgba(0,0,0,0.12);
            --radius-md: 10px;
            --radius-lg: 16px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        body {
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.6;
            min-height: 100vh;
        }

        /* ===== MÀN HÌNH BẮT ĐẦU (START SCREEN) ===== */
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
            color: var(--primary-dark);
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
            color: var(--text-main);
            margin-bottom: 8px;
            font-weight: 700;
        }

        .start-card .subtitle {
            color: var(--text-muted);
            font-size: 14px;
            margin-bottom: 24px;
        }

        .exam-rules {
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 16px 20px;
            margin-bottom: 24px;
        }

        .exam-rules-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            text-align: center;
        }

        .rule-item {
            padding: 8px;
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
            color: var(--text-main);
        }

        .rule-item .lbl {
            font-size: 12px;
            color: var(--text-muted);
        }

        .form-group {
            margin-bottom: 16px;
        }

        .form-group label {
            display: block;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 6px;
            color: var(--text-main);
        }

        .form-group label span {
            color: var(--danger);
        }

        .form-control {
            width: 100%;
            padding: 12px 14px;
            border: 1.5px solid var(--border-color);
            border-radius: 8px;
            font-size: 14px;
            transition: all 0.2s;
            background: #ffffff;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(26, 115, 232, 0.15);
        }

        .btn-start {
            width: 100%;
            background: var(--primary);
            color: #ffffff;
            border: none;
            padding: 14px 20px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            margin-top: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .btn-start:hover {
            background: var(--primary-dark);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(26, 115, 232, 0.3);
        }

        /* ===== THANH ĐIỀU HƯỚNG CỐ ĐỊNH TRÊN ĐẦU (TOPBAR) ===== */
        .topbar {
            position: sticky;
            top: 0;
            left: 0;
            right: 0;
            background: #ffffff;
            border-bottom: 1px solid var(--border-color);
            padding: 12px 24px;
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-sm);
        }

        .topbar-info {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .student-pill {
            display: flex;
            align-items: center;
            gap: 8px;
            background: #f1f3f4;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            color: var(--text-main);
        }

        .timer-box {
            display: flex;
            align-items: center;
            gap: 10px;
            background: #eef2ff;
            border: 1px solid #c7d2fe;
            color: #3730a3;
            padding: 6px 16px;
            border-radius: 30px;
            font-size: 18px;
            font-weight: 700;
            letter-spacing: 0.5px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            transition: all 0.3s;
        }

        .timer-box.urgent {
            background: var(--danger-light);
            border-color: var(--danger);
            color: var(--danger);
            animation: pulse 1s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.03); }
            100% { transform: scale(1); }
        }

        .btn-submit-exam {
            background: var(--success);
            color: white;
            border: none;
            padding: 9px 20px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }

        .btn-submit-exam:hover {
            background: #1b5e20;
            box-shadow: 0 4px 10px rgba(46, 125, 50, 0.3);
        }

        /* ===== BỐ CỤC CHÍNH (MAIN LAYOUT) ===== */
        .exam-container {
            max-width: 1300px;
            margin: 24px auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 1fr 340px;
            gap: 24px;
            align-items: start;
        }

        /* CỘT DANH SÁCH CÂU HỎI */
        .questions-column {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .question-card {
            background: var(--card-bg);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            padding: 24px;
            box-shadow: var(--shadow-sm);
            transition: border-color 0.2s, box-shadow 0.2s;
            position: relative;
        }

        .question-card:hover {
            box-shadow: var(--shadow-md);
        }

        .question-card.flagged {
            border-left: 5px solid var(--warning);
        }

        .q-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px dashed #e2e8f0;
        }

        .q-number-badge {
            background: var(--primary);
            color: #ffffff;
            font-weight: 700;
            font-size: 13px;
            padding: 4px 12px;
            border-radius: 6px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .q-tag {
            font-size: 12px;
            color: var(--text-muted);
            background: #f1f5f9;
            padding: 4px 10px;
            border-radius: 4px;
            font-weight: 500;
        }

        .btn-flag {
            background: none;
            border: 1px solid var(--border-color);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12px;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .btn-flag.active {
            background: var(--warning-light);
            border-color: var(--warning);
            color: var(--warning);
            font-weight: 600;
        }

        .q-content {
            font-size: 15px;
            font-weight: 500;
            color: var(--text-main);
            margin-bottom: 18px;
            white-space: pre-line;
            line-height: 1.6;
        }

        /* LỰA CHỌN A, B, C, D */
        .options-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .option-item {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            padding: 12px 16px;
            border: 1.5px solid var(--border-color);
            border-radius: 8px;
            background: #ffffff;
            cursor: pointer;
            transition: all 0.2s;
            user-select: none;
        }

        .option-item:hover {
            border-color: #93c5fd;
            background: #f8fafc;
        }

        .option-item.selected {
            border-color: var(--primary);
            background: #f0f7ff;
            box-shadow: 0 0 0 1px var(--primary);
        }

        .opt-radio {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            border: 2px solid #cbd5e1;
            margin-top: 2px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }

        .option-item.selected .opt-radio {
            border-color: var(--primary);
            background: var(--primary);
        }

        .option-item.selected .opt-radio::after {
            content: '';
            width: 8px;
            height: 8px;
            background: #ffffff;
            border-radius: 50%;
        }

        .opt-text {
            font-size: 14px;
            color: #334155;
            line-height: 1.5;
        }

        .opt-letter {
            font-weight: 700;
            color: var(--text-main);
            margin-right: 4px;
        }

        /* CỘT ĐIỀU HƯỚNG CÂU HỎI (QUESTION PALETTE) */
        .palette-column {
            position: sticky;
            top: 80px;
            background: var(--card-bg);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
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
            max-height: 380px;
            overflow-y: auto;
            padding-right: 4px;
            margin-bottom: 16px;
        }

        .palette-btn {
            aspect-ratio: 1;
            border: 1px solid var(--border-color);
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
            outline: 2px solid #000000;
            outline-offset: 1px;
        }

        /* ===== MÀN HÌNH KẾT QUẢ (RESULT SCREEN) ===== */
        .result-card {
            background: #ffffff;
            border-radius: var(--radius-lg);
            max-width: 750px;
            width: 100%;
            margin: 40px auto;
            padding: 40px;
            box-shadow: var(--shadow-lg);
            text-align: center;
            display: none;
        }

        .score-circle {
            width: 130px;
            height: 130px;
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
            font-size: 38px;
            font-weight: 800;
            line-height: 1;
        }

        .score-max {
            font-size: 14px;
            opacity: 0.85;
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
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 12px 8px;
        }

        .res-item .val {
            font-size: 18px;
            font-weight: 700;
            color: var(--text-main);
        }

        .res-item .lbl {
            font-size: 12px;
            color: var(--text-muted);
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

        .sync-error {
            background: var(--danger-light);
            color: var(--danger);
            border: 1px solid #fecaca;
        }

        .result-actions {
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .btn-action {
            padding: 11px 22px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            border: none;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }

        .btn-review {
            background: #f1f5f9;
            color: #334155;
            border: 1px solid var(--border-color);
        }

        .btn-review:hover {
            background: #e2e8f0;
        }

        .btn-download-cert {
            background: var(--primary);
            color: #ffffff;
        }

        .btn-download-cert:hover {
            background: var(--primary-dark);
        }

        /* LỜI GIẢI CHI TIẾT KHI XEM LẠI */
        .review-explanation {
            margin-top: 14px;
            padding: 12px 16px;
            background: #fffbeb;
            border-left: 4px solid #f59e0b;
            border-radius: 4px;
            font-size: 13px;
            color: #78350f;
            display: none;
        }

        .review-mode .review-explanation {
            display: block;
        }

        .review-mode .option-item.correct-ans {
            background: #dcfce7 !important;
            border-color: #22c55e !important;
        }

        .review-mode .option-item.wrong-selected {
            background: #fee2e2 !important;
            border-color: #ef4444 !important;
        }

        @media (max-width: 900px) {
            .exam-container {
                grid-template-columns: 1fr;
            }
            .palette-column {
                display: none; /* Mobile mode drawer */
            }
            .topbar {
                padding: 10px 16px;
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
            <div class="topbar-info">
                <div class="student-pill">
                    <i class="fa-solid fa-user-graduate" style="color: var(--primary);"></i>
                    <span id="topStudentName">Thí sinh</span>
                    <span style="opacity: 0.5;">|</span>
                    <span id="topStudentId">MSSV</span>
                    <span style="opacity: 0.5;">|</span>
                    <span id="topClassName">Lớp</span>
                </div>
            </div>

            <!-- Đồng hồ 70 phút -->
            <div id="timerBox" class="timer-box">
                <i class="fa-regular fa-clock"></i>
                <span id="timerText">70:00</span>
            </div>

            <div>
                <button type="button" class="btn-submit-exam" onclick="confirmSubmitExam()">
                    <i class="fa-solid fa-cloud-arrow-up"></i> Nộp bài
                </button>
            </div>
        </header>

        <!-- Khung làm bài chính -->
        <main class="exam-container">
            <!-- Cột trái: 60 câu hỏi -->
            <div class="questions-column" id="questionsContainer">
                <!-- Javascript sẽ tự động render 60 câu hỏi tại đây -->
            </div>

            <!-- Cột phải: Bảng số câu hỏi (Question Palette) -->
            <aside class="palette-column">
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

                <div style="text-align: center; margin-top: 10px;">
                    <button type="button" class="btn-submit-exam" style="width: 100%; justify-content: center;" onclick="confirmSubmitExam()">
                        <i class="fa-solid fa-check"></i> Hoàn thành & Nộp bài
                    </button>
                </div>
            </aside>
        </main>
    </div>

    <!-- 3. MÀN HÌNH KẾT QUẢ (RESULT CARD) -->
    <div id="resultModal" class="modal-overlay" style="display: none;">
        <div class="result-card" id="resultCard" style="display: block;">
            <span class="exam-header-badge" style="background: #e0f2fe; color: #0369a1;">
                <i class="fa-solid fa-award"></i> KẾT QUẢ BÀI KIỂM TRA GIỮA KỲ
            </span>
            <h2 id="resStudentInfo" style="margin: 10px 0 6px 0; font-size: 22px;">Nguyễn Văn A - 22KT0123</h2>
            <p style="color: var(--text-muted); font-size: 13px;" id="resClassInfo">Lớp: AI22-KT | Môn: AI trong Kế toán & Tài chính</p>

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
                    <div class="val" id="resWrong" style="color: var(--danger);">0</div>
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
                <button type="button" class="btn-action" style="background: #16a34a; color: white;" onclick="retakeExam()">
                    <i class="fa-solid fa-rotate-right"></i> Làm lại bài thi (Bốc đề mới)
                </button>
                <button type="button" class="btn-action btn-review" onclick="toggleReviewMode()">
                    <i class="fa-solid fa-eye"></i> Xem lại bài làm & Lời giải
                </button>
                <button type="button" class="btn-action btn-download-cert" onclick="downloadResultSlip()">
                    <i class="fa-solid fa-file-arrow-down"></i> Tải chứng nhận điểm (.txt)
                </button>
            </div>
        </div>
    </div>

    <!-- Tải ngân hàng câu hỏi -->
    <script src="questions.js"></script>

    <script>
        // CẤU HÌNH THI
        const TOTAL_QUESTIONS = 60;
        const EXAM_DURATION_MINUTES = 70;
        const DEFAULT_SHEET_URL = "https://script.google.com/macros/s/AKfycby2cPdyEuXF8Hyda1yiqgF5zFo3Ya5qhMjua2YUkyzcFZ-GdhFRGT19WgjhEgqmi-ziAA/exec";

        let studentInfo = {};
        let selectedQuestions = [];
        let userAnswers = {}; // { qIdx: 'A' }
        let flaggedQuestions = new Set();
        let remainingSeconds = EXAM_DURATION_MINUTES * 60;
        let timerInterval = null;
        let examStartTime = null;
        let examEndTime = null;
        let isSubmitted = false;

        // Lưu/đọc cấu hình từ localStorage
        window.addEventListener('DOMContentLoaded', () => {
            const savedUrl = localStorage.getItem('exam_sheet_url');
            if (savedUrl) {
                document.getElementById('sheetUrl').value = savedUrl;
            }
        });

        // BẮT ĐẦU BÀI THI
        function startExam(e) {
            e.preventDefault();
            const fullName = document.getElementById('fullName').value.trim();
            const studentId = document.getElementById('studentId').value.trim();
            const className = document.getElementById('className').value.trim();
            const sheetUrl = document.getElementById('sheetUrl').value.trim();

            if (!fullName || !studentId || !className) {
                alert("Vui lòng điền đầy đủ Họ tên, MSSV và Lớp!");
                return;
            }

            studentInfo = { fullName, studentId, className, sheetUrl };
            if (sheetUrl) {
                localStorage.setItem('exam_sheet_url', sheetUrl);
            }

            // Cập nhật thông tin lên thanh Topbar
            document.getElementById('topStudentName').textContent = fullName;
            document.getElementById('topStudentId').textContent = studentId;
            document.getElementById('topClassName').textContent = className;

            // Bốc ngẫu nhiên 60 câu hỏi từ 180 câu trong ngân hàng
            selectedQuestions = pickRandomQuestions(EXAM_BANK, TOTAL_QUESTIONS);

            // Ẩn modal bắt đầu, hiện màn hình làm bài
            document.getElementById('startModal').style.display = 'none';
            document.getElementById('examApp').style.display = 'block';

            // Khởi tạo giao diện
            renderQuestions();
            renderPalette();
            startTimer();
            examStartTime = new Date();
        }

        // THUẬT TOÁN BỐC NGẪU NHIÊN VÀ XÁO TRỘN ĐÁP ÁN (Fisher-Yates)
        function pickRandomQuestions(bank, count) {
            const shuffled = [...bank].sort(() => 0.5 - Math.random());
            const picked = shuffled.slice(0, count);

            // Xáo trộn thứ tự các đáp án bên trong từng câu
            return picked.map((q, idx) => {
                const optKeys = ["A", "B", "C", "D"];
                const originalOptions = [
                    { key: "A", text: q.options.A, isCorrect: q.correct === "A" },
                    { key: "B", text: q.options.B, isCorrect: q.correct === "B" },
                    { key: "C", text: q.options.C, isCorrect: q.correct === "C" },
                    { key: "D", text: q.options.D, isCorrect: q.correct === "D" }
                ].sort(() => 0.5 - Math.random());

                const newOptions = {};
                let newCorrect = "A";

                originalOptions.forEach((opt, oIdx) => {
                    const newKey = optKeys[oIdx];
                    newOptions[newKey] = opt.text;
                    if (opt.isCorrect) {
                        newCorrect = newKey;
                    }
                });

                return {
                    examIndex: idx + 1,
                    originalId: q.id,
                    session: q.session,
                    difficulty: q.difficulty,
                    question: q.question,
                    options: newOptions,
                    correct: newCorrect,
                    explanation: q.explanation
                };
            });
        }

        // RENDER DANH SÁCH 60 CÂU HỎI
        function renderQuestions() {
            const container = document.getElementById('questionsContainer');
            container.innerHTML = '';

            selectedQuestions.forEach((q, idx) => {
                const card = document.createElement('div');
                card.className = 'question-card';
                card.id = `qCard_${idx}`;

                let optionsHtml = '';
                ["A", "B", "C", "D"].forEach(letter => {
                    const text = q.options[letter];
                    optionsHtml += `
                        <div class="option-item" id="opt_${idx}_${letter}" onclick="selectOption(${idx}, '${letter}')">
                            <div class="opt-radio"></div>
                            <div class="opt-text"><span class="opt-letter">${letter}.</span> ${escapeHtml(text)}</div>
                        </div>
                    `;
                });

                card.innerHTML = `
                    <div class="q-header">
                        <span class="q-number-badge"><i class="fa-solid fa-circle-question"></i> Câu ${idx + 1} / ${TOTAL_QUESTIONS}</span>
                        <div style="display: flex; gap: 8px; align-items: center;">
                            <span class="q-tag"><i class="fa-solid fa-bookmark"></i> ${escapeHtml(q.session.split(':')[0])}</span>
                            <button type="button" class="btn-flag" id="flagBtn_${idx}" onclick="toggleFlag(${idx})">
                                <i class="fa-regular fa-flag"></i> Đánh dấu
                            </button>
                        </div>
                    </div>
                    <div class="q-content">${escapeHtml(q.question)}</div>
                    <div class="options-list">
                        ${optionsHtml}
                    </div>
                    <div class="review-explanation" id="exp_${idx}">
                        <strong><i class="fa-solid fa-lightbulb"></i> Giải thích chi tiết (Đáp án đúng: ${q.correct}):</strong><br>
                        ${escapeHtml(q.explanation || 'Không có giải thích chi tiết.')}
                    </div>
                `;

                container.appendChild(card);
            });
        }

        // RENDER BẢNG ĐIỀU HƯỚNG CÂU HỎI (QUESTION PALETTE)
        function renderPalette() {
            const grid = document.getElementById('paletteGrid');
            grid.innerHTML = '';

            for (let i = 0; i < TOTAL_QUESTIONS; i++) {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'palette-btn';
                btn.id = `paletteBtn_${i}`;
                btn.textContent = i + 1;
                btn.onclick = () => scrollToQuestion(i);
                grid.appendChild(btn);
            }
        }

        // CHỌN PHƯƠNG ÁN
        function selectOption(qIdx, letter) {
            if (isSubmitted) return;

            userAnswers[qIdx] = letter;

            // Cập nhật giao diện lựa chọn
            ["A", "B", "C", "D"].forEach(l => {
                const el = document.getElementById(`opt_${qIdx}_${l}`);
                if (el) {
                    if (l === letter) el.classList.add('selected');
                    else el.classList.remove('selected');
                }
            });

            // Cập nhật bảng câu hỏi
            const pBtn = document.getElementById(`paletteBtn_${qIdx}`);
            if (pBtn) pBtn.classList.add('answered');

            updateStats();
        }

        // ĐÁNH DẤU XEM LẠI
        function toggleFlag(qIdx) {
            const card = document.getElementById(`qCard_${qIdx}`);
            const btn = document.getElementById(`flagBtn_${qIdx}`);
            const pBtn = document.getElementById(`paletteBtn_${qIdx}`);

            if (flaggedQuestions.has(qIdx)) {
                flaggedQuestions.delete(qIdx);
                card.classList.remove('flagged');
                btn.classList.remove('active');
                btn.innerHTML = '<i class="fa-regular fa-flag"></i> Đánh dấu';
                pBtn.classList.remove('flagged');
            } else {
                flaggedQuestions.add(qIdx);
                card.classList.add('flagged');
                btn.classList.add('active');
                btn.innerHTML = '<i class="fa-solid fa-flag"></i> Đã đánh dấu';
                pBtn.classList.add('flagged');
            }

            updateStats();
        }

        // CUỘN ĐẾN CÂU HỎI
        function scrollToQuestion(qIdx) {
            const card = document.getElementById(`qCard_${qIdx}`);
            if (card) {
                card.scrollIntoView({ behavior: 'smooth', block: 'center' });
                // Hiệu ứng nhấp nháy nhẹ
                card.style.borderColor = '#1a73e8';
                setTimeout(() => { card.style.borderColor = ''; }, 1000);
            }
        }

        // CẬP NHẬT THỐNG KÊ TIẾN ĐỘ
        function updateStats() {
            const answeredCount = Object.keys(userAnswers).length;
            const unansweredCount = TOTAL_QUESTIONS - answeredCount;
            const flaggedCount = flaggedQuestions.size;

            document.getElementById('statAns').textContent = answeredCount;
            document.getElementById('statUnans').textContent = unansweredCount;
            document.getElementById('statFlag').textContent = flaggedCount;
            document.getElementById('answeredCountBadge').textContent = `${answeredCount}/${TOTAL_QUESTIONS}`;
        }

        // BỘ ĐẾM THỜI GIAN 60 PHÚT
        function startTimer() {
            const timerBox = document.getElementById('timerBox');
            const timerText = document.getElementById('timerText');

            timerInterval = setInterval(() => {
                remainingSeconds--;

                const mins = Math.floor(remainingSeconds / 60);
                const secs = remainingSeconds % 60;
                timerText.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

                // Cảnh báo khi còn dưới 5 phút
                if (remainingSeconds <= 300) {
                    timerBox.classList.add('urgent');
                }

                // Hết giờ -> Tự động nộp bài
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

            const answeredCount = Object.keys(userAnswers).length;
            const unansweredCount = TOTAL_QUESTIONS - answeredCount;

            let msg = `Bạn đã hoàn thành ${answeredCount}/${TOTAL_QUESTIONS} câu hỏi.\n`;
            if (unansweredCount > 0) {
                msg += `⚠️ CẢNH BÁO: Còn ${unansweredCount} câu hỏi CHƯA LÀM!\n\n`;
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

            // Tính điểm
            let correctCount = 0;
            const detailsList = [];

            selectedQuestions.forEach((q, idx) => {
                const userChoice = userAnswers[idx] || "Chưa chọn";
                const isCorrect = (userChoice === q.correct);
                if (isCorrect) correctCount++;

                detailsList.push({
                    qIndex: idx + 1,
                    userChoice,
                    correctAnswer: q.correct,
                    isCorrect
                });
            });

            const score10 = Number(((correctCount / TOTAL_QUESTIONS) * 10).toFixed(2));
            const wrongCount = TOTAL_QUESTIONS - correctCount;
            const percent = Math.round((correctCount / TOTAL_QUESTIONS) * 10).toFixed(0) + "%";

            // Thời gian làm bài
            const timeDiffSec = Math.floor((examEndTime - examStartTime) / 1000);
            const spentMins = Math.floor(timeDiffSec / 60);
            const spentSecs = timeDiffSec % 60;
            const timeSpentText = `${spentMins} phút ${spentSecs} giây`;

            // Hiển thị kết quả lên giao diện
            document.getElementById('resStudentInfo').textContent = `${studentInfo.fullName} - ${studentInfo.studentId}`;
            document.getElementById('resClassInfo').textContent = `Lớp: ${studentInfo.className} | Ngày nộp: ${examEndTime.toLocaleString('vi-VN')}`;
            document.getElementById('resScore10').textContent = score10.toFixed(1);
            document.getElementById('resCorrect').textContent = `${correctCount}/${TOTAL_QUESTIONS}`;
            document.getElementById('resWrong').textContent = wrongCount;
            document.getElementById('resPercent').textContent = `${((correctCount/TOTAL_QUESTIONS)*100).toFixed(1)}%`;
            document.getElementById('resTimeSpent').textContent = `${spentMins}p ${spentSecs}s`;

            // Hiện modal kết quả
            document.getElementById('resultModal').style.display = 'flex';

            // Gửi dữ liệu về Google Sheet (nếu có cấu hình)
            sendToGoogleSheet({
                fullName: studentInfo.fullName,
                studentId: studentInfo.studentId,
                className: studentInfo.className,
                score10: score10,
                correctCount: correctCount,
                totalQuestions: TOTAL_QUESTIONS,
                timeSpent: timeSpentText,
                submitTime: examEndTime.toLocaleString('vi-VN'),
                summaryText: `${correctCount}/${TOTAL_QUESTIONS} câu đúng`
            });
        }

        // ĐỒNG BỘ KẾT QUẢ VỀ GOOGLE SHEET (APPS SCRIPT)
        function sendToGoogleSheet(payload) {
            const statusEl = document.getElementById('syncStatus');
            const targetUrl = studentInfo.sheetUrl || DEFAULT_SHEET_URL;

            if (!targetUrl || targetUrl.includes('example')) {
                statusEl.className = 'sync-status sync-success';
                statusEl.innerHTML = '<i class="fa-solid fa-circle-check"></i> Đã hoàn thành chấm thi và lưu trữ an toàn!';
                return;
            }

            statusEl.className = 'sync-status sync-loading';
            statusEl.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Đang đồng bộ kết quả lên Google Sheet...';

            // Sử dụng POST request (mode no-cors để gửi dữ liệu mượt mà, không bị chặn CORS)
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
                console.error("Lỗi gửi Google Sheet:", err);
                statusEl.className = 'sync-status sync-error';
                statusEl.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Không thể kết nối Google Sheet. Vui lòng bấm "Tải chứng nhận điểm" bên dưới để lưu phiếu nộp bài.';
            });
        }

        // CHẾ ĐỘ XEM LẠI BÀI THI & LỜI GIẢI
        function toggleReviewMode() {
            document.getElementById('resultModal').style.display = 'none';
            document.body.classList.add('review-mode');

            // Đổi màu các đáp án đúng/sai
            selectedQuestions.forEach((q, idx) => {
                const userChoice = userAnswers[idx];
                const correctChoice = q.correct;

                // Tô xanh đáp án đúng
                const correctEl = document.getElementById(`opt_${idx}_${correctChoice}`);
                if (correctEl) correctEl.classList.add('correct-ans');

                // Nếu chọn sai, tô đỏ đáp án đã chọn
                if (userChoice && userChoice !== correctChoice) {
                    const wrongEl = document.getElementById(`opt_${idx}_${userChoice}`);
                    if (wrongEl) wrongEl.classList.add('wrong-selected');
                }
            });

            // Cuộn lên câu 1
            window.scrollTo({ top: 0, behavior: 'smooth' });

            // Cập nhật nút nộp bài thành nút làm lại đề mới
            const submitBtn = document.querySelector('.btn-submit-exam');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fa-solid fa-rotate-right"></i> Làm lại đề mới';
                submitBtn.style.background = '#16a34a';
                submitBtn.onclick = retakeExam;
            }
        }

        // LÀM LẠI BÀI THI (BỐC ĐỀ MỚI - KHÔNG GIỚI HẠN SỐ LẦN)
        function retakeExam() {
            if (!confirm("Hệ thống sẽ bốc ngẫu nhiên một đề thi 60 câu hoàn toàn mới từ ngân hàng câu hỏi. Bạn có muốn bắt đầu làm lại ngay không?")) {
                return;
            }

            isSubmitted = false;
            userAnswers = {};
            flaggedQuestions.clear();
            remainingSeconds = EXAM_DURATION_MINUTES * 60;
            if (timerInterval) clearInterval(timerInterval);
            document.body.classList.remove('review-mode');

            // Reset nút nộp bài
            const submitBtn = document.querySelector('.btn-submit-exam');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fa-solid fa-cloud-arrow-up"></i> Nộp bài';
                submitBtn.style.background = '';
                submitBtn.onclick = confirmSubmitExam;
            }

            // Bốc ngẫu nhiên 60 câu mới
            selectedQuestions = pickRandomQuestions(EXAM_BANK, TOTAL_QUESTIONS);

            // Ẩn modal kết quả
            document.getElementById('resultModal').style.display = 'none';
            document.getElementById('examApp').style.display = 'block';

            // Reset Timer display
            const mins = Math.floor(remainingSeconds / 60);
            const secs = remainingSeconds % 60;
            document.getElementById('timerText').textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
            document.getElementById('timerBox').classList.remove('urgent');

            // Render lại giao diện
            renderQuestions();
            renderPalette();
            updateStats();
            startTimer();
            examStartTime = new Date();

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // TẢI PHIẾU CHỨNG NHẬN ĐIỂM (.TXT)
        function downloadResultSlip() {
            const correctCount = Object.keys(userAnswers).filter(k => userAnswers[k] === selectedQuestions[k].correct).length;
            const score10 = ((correctCount / TOTAL_QUESTIONS) * 10).toFixed(2);

            let lines = [
                "=========================================================",
                "     KHOA KẾ TOÁN - TÀI CHÍNH | ĐẠI HỌC ĐÔNG Á",
                "       PHIẾU KẾT QUẢ BÀI KIỂM TRA GIỮA KỲ",
                "  Học phần: Trí tuệ nhân tạo (AI) trong Kế toán & Tài chính",
                "=========================================================",
                "",
                `Họ và tên thí sinh : ${studentInfo.fullName}`,
                `Mã số sinh viên    : ${studentInfo.studentId}`,
                `Lớp sinh hoạt      : ${studentInfo.className}`,
                `Thời gian nộp bài  : ${examEndTime ? examEndTime.toLocaleString('vi-VN') : ''}`,
                "---------------------------------------------------------",
                `ĐIỂM SỐ (THANG 10) : ${score10} / 10.0`,
                `Số câu trả lời đúng: ${correctCount} / ${TOTAL_QUESTIONS} câu`,
                `Tỷ lệ chính xác    : ${((correctCount / TOTAL_QUESTIONS) * 100).toFixed(1)}%`,
                "=========================================================",
                "",
                "CHI TIẾT ĐÁP ÁN BÀI LÀM:"
            ];

            selectedQuestions.forEach((q, idx) => {
                const userChoice = userAnswers[idx] || "Chưa chọn";
                const isCorrect = (userChoice === q.correct);
                lines.push(`Câu ${String(idx + 1).padStart(2, '0')}: Bạn chọn [${userChoice}] | Đáp án đúng: [${q.correct}] -> ${isCorrect ? 'ĐÚNG (+)' : 'SAI (-)'}`);
            });

            const content = lines.join("\\r\\n");
            const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `KetQua_KiemTra_${studentInfo.studentId}_${studentInfo.fullName.replace(/\\s+/g, '_')}.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        function escapeHtml(text) {
            if (!text) return "";
            return String(text)
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }
    </script>
</body>
</html>
'''
    index_html_path = os.path.join(output_dir, "index.html")
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(index_html_content)
    print(f"Đã tạo giao diện thi: {index_html_path}")

if __name__ == "__main__":
    build_exam()
