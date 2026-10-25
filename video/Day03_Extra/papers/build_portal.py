# -*- coding: utf-8 -*-
"""
Builder for Day 03 Extra Portals:
1. video/Day03_Extra/papers/index.html (Dedicated Scientific Papers Hub)
2. video/Day03_Extra/index.html (Master Day 03 Extra Portal with Interactive Slide Viewer)
"""

import os

BASE_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day03_Extra"
PAPERS_DIR = os.path.join(BASE_DIR, "papers")

def build_papers_hub():
    html = """<!DOCTYPE html>
<html lang="vi">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>Thư Viện Bài Báo Khoa Học & Nghiên Cứu Đỉnh Cao — Thị Giác Máy Tính & Siêu Tự Động Hóa Trong Kế Toán & Kiểm Toán (UDA)</title>
  <meta name="description"
    content="Cổng nghiên cứu học thuật toàn văn tiếng Việt chuyên sâu về Thị giác máy tính (Computer Vision), Xử lý chứng từ thông minh (IDP), Siêu tự động hóa (AI-RPA), Bắt hóa đơn giả mạo Gen-AI và Kiểm toán Drone + Dữ liệu lớn." />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap"
    rel="stylesheet">

  <style>
    :root {
      --bg-dark: #0b0f19;
      --bg-card: rgba(18, 26, 44, 0.75);
      --bg-card-hover: rgba(26, 38, 64, 0.95);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-glow: rgba(59, 130, 246, 0.5);
      --primary: #3b82f6;
      --primary-gradient: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
      --accent-cyan: #06b6d4;
      --accent-violet: #8b5cf6;
      --accent-amber: #f59e0b;
      --accent-emerald: #10b981;
      --accent-rose: #f43f5e;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.5), 0 0 1px 1px rgba(255, 255, 255, 0.05);
      --shadow-hover: 0 20px 40px -15px rgba(59, 130, 246, 0.3), 0 0 20px rgba(59, 130, 246, 0.15);
      --radius-lg: 20px;
      --radius-md: 14px;
      --radius-sm: 8px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      overflow-x: hidden;
      line-height: 1.6;
      background-image:
        radial-gradient(circle at 15% 15%, rgba(59, 130, 246, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 85% 25%, rgba(139, 92, 246, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 50% 80%, rgba(6, 182, 212, 0.1) 0%, transparent 50%);
      background-attachment: fixed;
    }

    .container {
      max-width: 1360px;
      margin: 0 auto;
      padding: 2.5rem 1.75rem 6rem;
    }

    .top-nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2.5rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--border-subtle);
    }

    .brand-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 700;
      font-size: 0.95rem;
      letter-spacing: 0.03em;
      color: #e2e8f0;
      text-decoration: none;
    }

    .brand-logo-icon {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: var(--primary-gradient);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
    }

    .nav-actions {
      display: flex;
      gap: 0.75rem;
      align-items: center;
      flex-wrap: wrap;
    }

    .nav-btn {
      padding: 0.55rem 1rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 600;
      transition: all 0.2s;
    }

    .nav-btn:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.2);
    }

    .nav-btn.primary {
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }

    .hero {
      text-align: center;
      padding: 2rem 1rem 3.5rem;
      max-width: 950px;
      margin: 0 auto;
    }

    .hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 1rem;
      border-radius: 9999px;
      background: rgba(59, 130, 246, 0.12);
      border: 1px solid rgba(59, 130, 246, 0.35);
      color: #60a5fa;
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 1.25rem;
    }

    .hero-title {
      font-family: 'Outfit', sans-serif;
      font-size: clamp(2.2rem, 5vw, 3.4rem);
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 1.25rem;
      letter-spacing: -0.02em;
    }

    .gradient-text {
      background: linear-gradient(135deg, #60a5fa 0%, #c084fc 50%, #22d3ee 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-desc {
      font-size: 1.15rem;
      color: var(--text-muted);
      line-height: 1.7;
      margin-bottom: 2rem;
    }

    .stats-bar {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.25rem;
      margin-bottom: 4rem;
    }

    .stat-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.25rem 1.5rem;
      backdrop-filter: blur(12px);
      text-align: center;
    }

    .stat-value {
      font-family: 'Outfit', sans-serif;
      font-size: 2rem;
      font-weight: 800;
      color: #38bdf8;
      margin-bottom: 0.25rem;
    }

    .stat-label {
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    .section-heading {
      font-family: 'Outfit', sans-serif;
      font-size: 1.65rem;
      font-weight: 700;
      margin-bottom: 1.75rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      color: #f1f5f9;
    }

    .section-heading-icon {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: rgba(59, 130, 246, 0.15);
      border: 1px solid rgba(59, 130, 246, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #60a5fa;
    }

    .papers-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 2rem;
      margin-bottom: 4.5rem;
    }

    @media (max-width: 640px) {
      .papers-grid {
        grid-template-columns: 1fr;
      }
    }

    .paper-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 2.25rem;
      backdrop-filter: blur(16px);
      box-shadow: var(--shadow-card);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }

    .paper-card:hover {
      transform: translateY(-6px);
      background: var(--bg-card-hover);
      border-color: var(--border-glow);
      box-shadow: var(--shadow-hover);
    }

    .paper-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--primary-gradient);
      opacity: 0.8;
    }

    .paper-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin-bottom: 1.25rem;
      align-self: flex-start;
    }

    .badge-p1 {
      background: rgba(59, 130, 246, 0.15);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.3);
    }

    .badge-p2 {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .badge-p3 {
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .badge-p4 {
      background: rgba(244, 63, 94, 0.15);
      color: #fda4af;
      border: 1px solid rgba(244, 63, 94, 0.3);
    }

    .paper-card-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
      margin-bottom: 0.6rem;
    }

    .paper-card-title-en {
      font-size: 0.88rem;
      color: var(--text-muted);
      font-style: italic;
      margin-bottom: 1.25rem;
      line-height: 1.4;
    }

    .paper-card-meta {
      font-size: 0.84rem;
      color: var(--text-dim);
      margin-bottom: 1.25rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border-subtle);
    }

    .paper-card-desc {
      font-size: 0.94rem;
      color: #cbd5e1;
      line-height: 1.65;
      margin-bottom: 1.75rem;
      flex-grow: 1;
    }

    .paper-card-actions {
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      margin-top: auto;
    }

    .btn-read {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.75rem 1.25rem;
      border-radius: var(--radius-sm);
      background: var(--primary-gradient);
      color: #fff;
      font-weight: 700;
      font-size: 0.92rem;
      text-decoration: none;
      transition: all 0.2s;
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35);
    }

    .btn-read:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
    }

    .btn-sub-actions {
      display: flex;
      gap: 0.65rem;
    }

    .btn-sub {
      flex: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      padding: 0.55rem 0.85rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
    }

    .btn-sub:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.2);
    }

    .matrix-container {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-bottom: 4.5rem;
      backdrop-filter: blur(12px);
      overflow-x: auto;
    }

    .matrix-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 800px;
    }

    .matrix-table th {
      text-align: left;
      padding: 1rem;
      border-bottom: 2px solid var(--border-subtle);
      color: #38bdf8;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.78rem;
      letter-spacing: 0.05em;
    }

    .matrix-table td {
      padding: 1rem;
      border-bottom: 1px solid var(--border-subtle);
      color: #e2e8f0;
      vertical-align: top;
    }

    .matrix-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }

    .site-footer {
      border-top: 1px solid var(--border-subtle);
      padding-top: 2.5rem;
      text-align: center;
      color: var(--text-dim);
      font-size: 0.88rem;
    }

    .footer-links {
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }

    .footer-link {
      color: var(--text-muted);
      text-decoration: none;
    }

    .footer-link:hover {
      color: #fff;
    }
  </style>
</head>

<body>

  <div class="container">

    <!-- Top Navigation -->
    <header class="top-nav">
      <a href="../index.html" class="brand-badge">
        <div class="brand-logo-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path>
          </svg>
        </div>
        <span>ĐẠI HỌC ĐÔNG Á • KHOA KẾ TOÁN & KIỂM TOÁN</span>
      </a>

      <div class="nav-actions">
        <a href="../index.html" class="nav-btn primary">
          🚀 Cổng Day 03 Extra
        </a>
        <a href="../../Day02_Extra/papers/index.html" class="nav-btn">
          Day 02 Extra (Học Sâu)
        </a>
        <a href="../../Day01_Extra/Videos/index.html" class="nav-btn">
          Day 01 Extra (Học Máy)
        </a>
        <a href="../../../index.html" class="nav-btn">
          Trang chủ Môn học
        </a>
      </div>
    </header>

    <!-- Hero -->
    <section class="hero">
      <div class="hero-tag">
        THỰC CHỨNG KHOA HỌC QUỐC TẾ (2025 – 2026)
      </div>

      <h1 class="hero-title">
        Thư Viện Bài Báo Khoa Học & Nghiên Cứu Đỉnh Cao <br />
        <span class="gradient-text">Thị Giác Máy Tính & Siêu Tự Động Hóa Trong Kế Toán</span>
      </h1>

      <p class="hero-desc">
        Hệ thống 4 công trình nghiên cứu khoa học thực chứng quốc tế hàng đầu (Springer Nature, arXiv, BMVC, MDPI) được dịch toàn văn tiếng Việt học thuật, tích hợp biểu đồ phân tích và câu hỏi tranh biện nghiệp vụ kế toán kiểm toán chuyên sâu.
      </p>
    </section>

    <!-- Stats Bar -->
    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-value">4 CÔNG TRÌNH</div>
        <div class="stat-label">Xuất bản mới nhất (2025–2026)</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">6.349+</div>
        <div class="stat-label">Hóa đơn thực tế thử nghiệm</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">100%</div>
        <div class="stat-label">Kiểm toán toàn bộ quần thể (Full-Population)</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">&lt; 1 PHÚT</div>
        <div class="stat-label">Chu kỳ bóc tách hóa đơn & đối chiếu 3 bên</div>
      </div>
    </div>

    <!-- 4 Papers Grid -->
    <h2 class="section-heading">
      <div class="section-heading-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
          <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
        </svg>
      </div>
      Danh Mục 4 Công Trình Nghiên Cứu Toàn Văn Tiếng Việt
    </h2>

    <div class="papers-grid">

      <!-- Paper 1 -->
      <div class="paper-card">
        <span class="paper-badge badge-p1">Paper 1 • Springer Nature (2026)</span>
        <h3 class="paper-card-title">1. InvoiceOCR: Quy Trình Nhận Dạng Hóa Đơn Tự Động Bằng Học Sâu</h3>
        <div class="paper-card-title-en">InvoiceOCR: Deep learning based automatic invoice recognition process</div>
        <div class="paper-card-meta">
          <strong>Tác giả:</strong> Chao Wang, Jian Zhang, Yu Yu (State Grid IT Group, Beijing) <br />
          <strong>Tạp chí:</strong> Discover Artificial Intelligence (Springer Nature) — Tập 6, Bài số 636
        </div>
        <p class="paper-card-desc">
          Đột phá bóc tách hóa đơn bị chụp nghiêng, nhăn, mờ trên 6.349 hóa đơn thực tế. Kết hợp thuật toán Differentiable Binarization (DB) và mạng CRNN + CTC với Hậu xử lý kiểm chứng đại số kế toán, đạt F-measure 96,8% và độ chính xác trích xuất trường đạt 98,92%.
        </p>
        <div class="paper-card-actions">
          <a href="paper_1_InvoiceOCR_Deep_Learning_Recognition_tiengviet.html" class="btn-read">
            📖 Đọc Toàn Văn Tiếng Việt &rarr;
          </a>
          <div class="btn-sub-actions">
            <a href="../videos/P2_paper_1_Computer_Vision_in_Accounting/index.html" target="_blank" class="btn-sub" style="color: #c084fc; border-color: rgba(168, 85, 247, 0.4); background: rgba(168, 85, 247, 0.1);">
              🎬 Video P2
            </a>
            <a href="../slides/P2_paper_1_Computer_Vision_in_Accounting.pdf" target="_blank" class="btn-sub">
              📊 Slide P2 (PDF)
            </a>
            <a href="paper 1_InvoiceOCR_Deep learning based automatic invoice recognition process.pdf" target="_blank" class="btn-sub">
              📥 Bản Gốc (PDF)
            </a>
          </div>
        </div>
      </div>

      <!-- Paper 2 -->
      <div class="paper-card">
        <span class="paper-badge badge-p2">Paper 2 • Multimodal Document AI (2026)</span>
        <h3 class="paper-card-title">2. Bóc Tách Hóa Đơn Tự Động Bằng Mô Hình Ngôn Ngữ Lớn (LLM) & OCR</h3>
        <div class="paper-card-title-en">Automated Invoice Data Extraction: Using LLM and OCR</div>
        <div class="paper-card-meta">
          <strong>Tác giả:</strong> Khushi Khanchandani, Advait Thakur et al. (Somaiya University) <br />
          <strong>Nguồn:</strong> Cornell University arXiv (cs.CV) & Framework Siêu tự động hóa LUT University
        </div>
        <p class="paper-card-desc">
          Thế hệ AI Đa phương thức tiếp theo: Kết hợp OCR và LLM có kiểm soát schema để bóc tách các hóa đơn hoàn toàn phi cấu trúc (Unseen Layouts) với F1 95,4%. Tích hợp quy trình Đối chiếu 3 bên (3-Way Matching) giúp giảm chu kỳ thanh toán hóa đơn từ 9,15 ngày xuống dưới 1 phút.
        </p>
        <div class="paper-card-actions">
          <a href="paper_2_Automated_Invoice_LLM_OCR_tiengviet.html" class="btn-read">
            📖 Đọc Toàn Văn Tiếng Việt &rarr;
          </a>
          <div class="btn-sub-actions">
            <a href="../videos/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán/index.html" target="_blank" class="btn-sub" style="color: #34d399; border-color: rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.1);">
              🎬 Video P3
            </a>
            <a href="../slides/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán.pdf" target="_blank" class="btn-sub">
              📊 Slide P3 (PDF)
            </a>
            <a href="paper_2_Automated Invoice Data Extraction_Using LLM and OCR.pdf" target="_blank" class="btn-sub">
              📥 Bản Gốc (PDF)
            </a>
          </div>
        </div>
      </div>

      <!-- Paper 3 -->
      <div class="paper-card">
        <span class="paper-badge badge-p3">Paper 3 • BMVC Landmark (2025/2026)</span>
        <h3 class="paper-card-title">3. Hóa Đơn & Biên Lai Giả Mạo: Thị Giác Máy Tính Bắt Gian Lận Thời Gen-AI</h3>
        <div class="paper-card-title-en">Fake Invoices and Receipts in Accounting: Impacts and Mitigation in the Age of gen-AI</div>
        <div class="paper-card-meta">
          <strong>Tác giả:</strong> Philip Thornton, Lamyaa Aljuaid et al. (Newcastle University & Sage PLC) <br />
          <strong>Hội thảo:</strong> British Machine Vision Conference (BMVC Workshops - MAAAI / SRBS)
        </div>
        <p class="paper-card-desc">
          Công trình phối hợp giữa đại học và tập đoàn phần mềm kế toán Sage: Phân tích hiểm họa làm giả hóa đơn tinh vi bằng AI tạo sinh (Photoshop inpainting, Diffusion models) và xây dựng bộ lọc Pháp y hình ảnh số (Error Level Analysis - ELA và Wavelet) để phát hiện con số bị chỉnh sửa.
        </p>
        <div class="paper-card-actions">
          <a href="paper_3_Fake_Invoices_Receipts_GenAI_tiengviet.html" class="btn-read">
            📖 Đọc Toàn Văn Tiếng Việt &rarr;
          </a>
          <div class="btn-sub-actions">
            <a href="../videos/P4_paper_3_AI_in_Accounting_and_Auditing/index.html" target="_blank" class="btn-sub" style="color: #fbbf24; border-color: rgba(245, 158, 11, 0.4); background: rgba(245, 158, 11, 0.1);">
              🎬 Video P4
            </a>
            <a href="../slides/P4_paper_3_AI_in_Accounting_and_Auditing.pdf" target="_blank" class="btn-sub">
              📊 Slide P4 (PDF)
            </a>
            <a href="paper_3_Fake Invoices and Receipts in Accounting_Impacts and Mitigation in the Age of Gen-AI.pdf" target="_blank" class="btn-sub">
              📥 Bản Gốc (PDF)
            </a>
          </div>
        </div>
      </div>

      <!-- Paper 4 -->
      <div class="paper-card">
        <span class="paper-badge badge-p4">Paper 4 • MDPI Landmark (2025)</span>
        <h3 class="paper-card-title">4. Drone Tích Hợp AI & Dữ Liệu Lớn Trong Kiểm Toán Hiện Trường</h3>
        <div class="paper-card-title-en">The Impact of AI-Integrated Drone Technology and Big Data on External Auditing Performance</div>
        <div class="paper-card-meta">
          <strong>Tác giả:</strong> Abdulaziz H. J. Alhazmi, Sardar Islam, Maria Prokofieva (Victoria University) <br />
          <strong>Tạp chí:</strong> Accounting and Auditing (MDPI Open Access) — Tập 1, Số 3, Bài số 8
        </div>
        <p class="paper-card-desc">
          Cuộc cách mạng kiểm toán số: Drone tự hành tích hợp LiDAR 3D và thuật toán YOLO kiểm kê 100% hàng tồn kho (kho than, quặng, pallet, nông sản) thay cho chọn mẫu 5% truyền thống. Nâng cao tính liêm chính bằng chứng theo ISA 501, cắt giảm 95% thời gian và giảm 85% phát thải khí nhà kính.
        </p>
        <div class="paper-card-actions">
          <a href="paper_4_AI_Drone_BigData_Auditing_tiengviet.html" class="btn-read">
            📖 Đọc Toàn Văn Tiếng Việt &rarr;
          </a>
          <div class="btn-sub-actions">
            <a href="../videos/P5_paper_4_The_Digital_Audit_Revolution/index.html" target="_blank" class="btn-sub" style="color: #fda4af; border-color: rgba(244, 63, 94, 0.4); background: rgba(244, 63, 94, 0.1);">
              🎬 Video P5
            </a>
            <a href="../slides/P5_paper_4_The_Digital_Audit_Revolution.pdf" target="_blank" class="btn-sub">
              📊 Slide P5 (PDF)
            </a>
            <a href="paper_4_The Impact of AI-Integrated Drone Technology and Big Data on External Auditing Performance.pdf" target="_blank" class="btn-sub">
              📥 Bản Gốc (PDF)
            </a>
          </div>
        </div>
      </div>

    </div>

    <!-- Comparative Matrix Table -->
    <h2 class="section-heading">
      <div class="section-heading-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
          <line x1="3" y1="9" x2="21" y2="9"></line>
          <line x1="9" y1="21" x2="9" y2="9"></line>
        </svg>
      </div>
      Ma Trận Đối Chiếu Phương Pháp Luận & Đóng Góp Học Thuật
    </h2>

    <div class="matrix-container">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>Bài Báo</th>
            <th>Trọng Tâm Nghiệp Vụ</th>
            <th>Công Nghệ AI Cốt Lõi</th>
            <th>Bộ Dữ Liệu Thực Nghiệm</th>
            <th>Độ Chính Xác / Hiệu Năng</th>
            <th>Slide & Video Tương Ứng</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bài 1 (Springer)</strong></td>
            <td>Kế toán Phải trả (AP), số hóa hóa đơn scan & chụp di động</td>
            <td>Differentiable Binarization (DB) + CRNN (CTC) + Skew Correction</td>
            <td>6.349 ảnh hóa đơn doanh nghiệp thực tế</td>
            <td>F-measure 96,81%, trích xuất trường đạt 98,92%</td>
            <td>
              <a href="../slides/P2_paper_1_Computer_Vision_in_Accounting.pdf" target="_blank" style="color: #60a5fa; font-weight: 600;">Slide P2</a> • 
              <a href="../videos/P2_paper_1_Computer_Vision_in_Accounting/index.html" target="_blank" style="color: #c084fc; font-weight: 700;">🎬 Video P2</a>
            </td>
          </tr>
          <tr>
            <td><strong>Bài 2 (arXiv/LUT)</strong></td>
            <td>Hóa đơn phi cấu trúc & Đối chiếu 3 bên (3-Way Matching)</td>
            <td>Multimodal Document AI + LLMs (Few-shot Prompting) + AI-RPA</td>
            <td>Tập hóa đơn mua hàng đa mẫu biểu toàn cầu</td>
            <td>F1-score 95,4% trên mẫu mới, giảm chu kỳ còn &lt; 1 phút</td>
            <td>
              <a href="../slides/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán.pdf" target="_blank" style="color: #34d399; font-weight: 600;">Slide P3</a> • 
              <a href="../videos/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán/index.html" target="_blank" style="color: #34d399; font-weight: 700;">🎬 Video P3</a>
            </td>
          </tr>
          <tr>
            <td><strong>Bài 3 (BMVC/Sage)</strong></td>
            <td>Kiểm soát nội bộ, bắt gian lận thanh toán công tác T&E</td>
            <td>Error Level Analysis (ELA) + Biến đổi Wavelet + Deep CNN Forensics</td>
            <td>Bộ dữ liệu biên lai thật và biên lai tạo bởi Gen-AI / Inpainting</td>
            <td>Phát hiện chính xác vùng sửa số tiền với AUC 96,2%</td>
            <td>
              <a href="../slides/P4_paper_3_AI_in_Accounting_and_Auditing.pdf" target="_blank" style="color: #fbbf24; font-weight: 600;">Slide P4</a> • 
              <a href="../videos/P4_paper_3_AI_in_Accounting_and_Auditing/index.html" target="_blank" style="color: #fbbf24; font-weight: 700;">🎬 Video P4</a>
            </td>
          </tr>
          <tr>
            <td><strong>Bài 4 (MDPI)</strong></td>
            <td>Kiểm toán độc lập (ISA 501), kiểm kê kho bãi, mỏ quặng, tài sản cố định</td>
            <td>Drone tự hành + Cảm biến LiDAR 3D + YOLO Object Detection + Big Data</td>
            <td>Cơ sở dữ liệu Web of Science 2015–2025 & thực tế Big 4</td>
            <td>Kiểm toán 100% quần thể, đo thể tích sai số &lt; 1%</td>
            <td>
              <a href="../slides/P5_paper_4_The_Digital_Audit_Revolution.pdf" target="_blank" style="color: #fda4af; font-weight: 600;">Slide P5</a> • 
              <a href="../videos/P5_paper_4_The_Digital_Audit_Revolution/index.html" target="_blank" style="color: #fda4af; font-weight: 700;">🎬 Video P5</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Footer -->
    <footer class="site-footer">
      <div class="footer-links">
        <a href="../index.html" class="footer-link">Cổng Chuyên Đề Day 03 Extra</a>
        <a href="../../Day02_Extra/papers/index.html" class="footer-link">Thư viện Bài báo Day 02 Extra</a>
        <a href="../../Day01_Extra/Videos/index.html" class="footer-link">Thư viện Video Day 01 Extra</a>
        <a href="../../../index.html" class="footer-link">Trang chủ Môn học</a>
      </div>
      <p>© 2026 Khoa Kế toán & Kiểm toán — Trường Đại học Đông Á (UDA). Tài liệu học thuật phục vụ giảng dạy môn Trí Tuệ Nhân Tạo Trong Kế Toán & Kiểm Toán.</p>
    </footer>

  </div>

</body>

</html>
"""
    out_path = os.path.join(PAPERS_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built Day03 Papers Hub: {out_path}")

def build_master_portal():
    html = """<!DOCTYPE html>
<html lang="vi">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>Chuyên Đề Nâng Cao: Thị Giác Máy Tính (Computer Vision) & Siêu Tự Động Hóa Trong Kế Toán — Đại học Đông Á</title>
  <meta name="description"
    content="Cổng chuyên đề nâng cao Day 03 Extra: Thị giác máy tính (Computer Vision), Xử lý chứng từ thông minh (IDP), Siêu tự động hóa (AI-RPA), Trình chiếu Slide P1 - P5 tương tác trực quan và Thư viện 4 bài báo khoa học đỉnh cao." />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap"
    rel="stylesheet">

  <style>
    :root {
      --bg-dark: #0b0f19;
      --bg-card: rgba(18, 26, 44, 0.75);
      --bg-card-hover: rgba(26, 38, 64, 0.95);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-glow: rgba(59, 130, 246, 0.5);
      --primary: #3b82f6;
      --primary-gradient: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
      --accent-cyan: #06b6d4;
      --accent-violet: #8b5cf6;
      --accent-amber: #f59e0b;
      --accent-emerald: #10b981;
      --accent-rose: #f43f5e;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.5), 0 0 1px 1px rgba(255, 255, 255, 0.05);
      --shadow-hover: 0 20px 40px -15px rgba(59, 130, 246, 0.3), 0 0 20px rgba(59, 130, 246, 0.15);
      --radius-lg: 20px;
      --radius-md: 14px;
      --radius-sm: 8px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      overflow-x: hidden;
      line-height: 1.6;
      background-image:
        radial-gradient(circle at 15% 15%, rgba(59, 130, 246, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 85% 25%, rgba(139, 92, 246, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 50% 80%, rgba(6, 182, 212, 0.1) 0%, transparent 50%);
      background-attachment: fixed;
    }

    .container {
      max-width: 1360px;
      margin: 0 auto;
      padding: 2.5rem 1.75rem 6rem;
    }

    .top-nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2.5rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--border-subtle);
    }

    .brand-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 700;
      font-size: 0.95rem;
      letter-spacing: 0.03em;
      color: #e2e8f0;
      text-decoration: none;
    }

    .brand-logo-icon {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: var(--primary-gradient);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
    }

    .nav-actions {
      display: flex;
      gap: 0.75rem;
      align-items: center;
      flex-wrap: wrap;
    }

    .nav-btn {
      padding: 0.55rem 1rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 600;
      transition: all 0.2s;
    }

    .nav-btn:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.2);
    }

    .hero {
      text-align: center;
      padding: 2.5rem 1rem 3.5rem;
      max-width: 980px;
      margin: 0 auto;
    }

    .hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 1rem;
      border-radius: 9999px;
      background: rgba(59, 130, 246, 0.12);
      border: 1px solid rgba(59, 130, 246, 0.35);
      color: #60a5fa;
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 1.25rem;
    }

    .hero-title {
      font-family: 'Outfit', sans-serif;
      font-size: clamp(2.3rem, 5vw, 3.5rem);
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 1.25rem;
      letter-spacing: -0.02em;
    }

    .gradient-text {
      background: linear-gradient(135deg, #60a5fa 0%, #c084fc 50%, #22d3ee 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-desc {
      font-size: 1.15rem;
      color: var(--text-muted);
      line-height: 1.7;
    }

    /* Feature Banner */
    .feature-banner {
      background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%);
      border: 1px solid rgba(59, 130, 246, 0.35);
      border-radius: var(--radius-lg);
      padding: 2rem 2.5rem;
      margin-bottom: 4rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 2rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
      flex-wrap: wrap;
    }

    .banner-text h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.45rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.4rem;
    }

    .banner-text p {
      color: var(--text-muted);
      font-size: 0.95rem;
      max-width: 680px;
    }

    .banner-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.85rem 1.5rem;
      border-radius: var(--radius-sm);
      background: var(--primary-gradient);
      color: #fff;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      transition: all 0.2s;
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
      white-space: nowrap;
    }

    .banner-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
    }

    /* Interactive Slide Viewer */
    .slide-viewer-box {
      background: var(--bg-card);
      border: 1px solid var(--border-glow);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-bottom: 4.5rem;
      backdrop-filter: blur(16px);
      box-shadow: var(--shadow-hover);
    }

    .viewer-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .viewer-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .slide-tabs {
      display: flex;
      gap: 0.5rem;
      overflow-x: auto;
      padding-bottom: 0.5rem;
      margin-bottom: 1.5rem;
      border-bottom: 1px solid var(--border-subtle);
    }

    .slide-tab {
      padding: 0.65rem 1.15rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      white-space: nowrap;
    }

    .slide-tab:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.08);
    }

    .slide-tab.active {
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
      font-weight: 700;
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }

    .slide-frame-container {
      position: relative;
      width: 100%;
      height: 650px;
      border-radius: var(--radius-md);
      overflow: hidden;
      background: #000;
      border: 1px solid var(--border-subtle);
    }

    .slide-frame {
      width: 100%;
      height: 100%;
      border: none;
    }

    .slide-controls-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1.25rem;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .slide-info-text {
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    .slide-action-btns {
      display: flex;
      gap: 0.75rem;
    }

    .slide-btn {
      padding: 0.55rem 1.1rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      color: #e2e8f0;
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }

    .slide-btn:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.12);
      border-color: var(--primary);
    }

    /* Grid Layouts */
    .section-heading {
      font-family: 'Outfit', sans-serif;
      font-size: 1.65rem;
      font-weight: 700;
      margin-bottom: 1.75rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      color: #f1f5f9;
    }

    .section-heading-icon {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: rgba(59, 130, 246, 0.15);
      border: 1px solid rgba(59, 130, 246, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #60a5fa;
    }

    .modules-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      gap: 1.75rem;
      margin-bottom: 4.5rem;
    }

    @media (max-width: 640px) {
      .modules-grid {
        grid-template-columns: 1fr;
      }
    }

    .module-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      backdrop-filter: blur(12px);
      transition: all 0.25s;
      display: flex;
      flex-direction: column;
    }

    .module-card:hover {
      transform: translateY(-4px);
      background: var(--bg-card-hover);
      border-color: rgba(255, 255, 255, 0.18);
      box-shadow: 0 14px 28px rgba(0, 0, 0, 0.4);
    }

    .module-thumb {
      width: 100%;
      height: 200px;
      border-radius: var(--radius-sm);
      overflow: hidden;
      margin-bottom: 1.25rem;
      background: #000;
      border: 1px solid var(--border-subtle);
    }

    .module-thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s;
    }

    .module-card:hover .module-thumb img {
      transform: scale(1.03);
    }

    .module-badge {
      display: inline-flex;
      align-items: center;
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-bottom: 0.85rem;
      align-self: flex-start;
    }

    .module-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.2rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.6rem;
      line-height: 1.4;
    }

    .module-desc {
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 1.25rem;
      flex-grow: 1;
    }

    .module-link {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      color: #60a5fa;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.88rem;
      transition: gap 0.2s;
    }

    .module-link:hover {
      gap: 0.65rem;
      color: #93c5fd;
    }

    .site-footer {
      border-top: 1px solid var(--border-subtle);
      padding-top: 2.5rem;
      text-align: center;
      color: var(--text-dim);
      font-size: 0.88rem;
    }

    .footer-links {
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }

    .footer-link {
      color: var(--text-muted);
      text-decoration: none;
    }

    .footer-link:hover {
      color: #fff;
    }
  </style>
</head>

<body>

  <div class="container">

    <!-- Top Navigation -->
    <header class="top-nav">
      <a href="../../index.html" class="brand-badge">
        <div class="brand-logo-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path>
          </svg>
        </div>
        <span>ĐẠI HỌC ĐÔNG Á • KHOA KẾ TOÁN & KIỂM TOÁN</span>
      </a>

      <div class="nav-actions">
        <a href="../Day02_Extra/index.html" class="nav-btn">
          Day 02 Extra (Học Sâu)
        </a>
        <a href="../Day01_Extra/Videos/index.html" class="nav-btn">
          Day 01 Extra (Học Máy)
        </a>
        <a href="../../index.html" class="nav-btn">
          Trang chủ Môn học
        </a>
      </div>
    </header>

    <!-- Hero -->
    <section class="hero">
      <div class="hero-tag">
        CHUYÊN ĐỀ BÀI GIẢNG & NGHIÊN CỨU THỰC CHỨNG (DAY 03 EXTRA)
      </div>

      <h1 class="hero-title">
        Chuyên Đề Nâng Cao <br />
        <span class="gradient-text">Thị Giác Máy Tính & Siêu Tự Động Hóa Trong Kế Toán</span>
      </h1>

      <p class="hero-desc">
        Hệ thống tài liệu sư phạm toàn diện: Tích hợp trình chiếu trực quan 5 bộ Slide bài giảng P1–P5 độ nét cao, giáo án seminar 70 phút và Thư viện 4 công trình nghiên cứu khoa học thực chứng quốc tế đỉnh cao dịch toàn văn tiếng Việt.
      </p>
    </section>

    <!-- Feature Banner: Papers Hub -->
    <div class="feature-banner">
      <div class="banner-text">
        <h3>📚 Thư Viện 4 Bài Báo Khoa Học Quốc Tế Đỉnh Cao (2025–2026)</h3>
        <p>Bản dịch tiếng Việt học thuật toàn văn các nghiên cứu từ Springer Nature, Cornell arXiv, Kỷ yếu BMVC Anh Quốc / Sage PLC và MDPI Accounting and Auditing.</p>
      </div>
      <a href="papers/index.html" class="banner-btn">
        <span>Khám Phá Thư Viện Bài Báo</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <line x1="5" y1="12" x2="19" y2="12"></line>
          <polyline points="12 5 19 12 12 19"></polyline>
        </svg>
      </a>
    </div>

    <!-- Interactive Slide Viewer Box -->
    <div class="slide-viewer-box" id="slide-viewer-section">
      <div class="viewer-header">
        <h2 class="viewer-title">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
            <line x1="8" y1="21" x2="16" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
          </svg>
          Trình Chiếu Slide Bài Giảng Trực Quan (Slide Viewer)
        </h2>
        <span style="font-size: 0.85rem; color: #38bdf8; font-weight: 600;">Xem trực tiếp trên web • Không cần tải về</span>
      </div>

      <!-- Slide Tabs -->
      <div class="slide-tabs">
        <button class="slide-tab active" onclick="loadSlide('slides/P1_[Theory]_AI_in_Accounting_and_Auditing.pdf', 'Slide P1: Lý Thuyết Nền Tảng AI Trong Kế Toán & Kiểm Toán', 'Lý thuyết nhập môn: Từ OCR truyền thống đến Multimodal Document AI, Siêu tự động hóa IDP + AI-RPA và Kiểm toán Drone.', 1)">
          P1: Lý Thuyết Tổng Quan
        </button>
        <button class="slide-tab" onclick="loadSlide('slides/P2_paper_1_Computer_Vision_in_Accounting.pdf', 'Slide P2: Computer Vision in Accounting (Tương ứng Bài báo 1 - InvoiceOCR)', 'Chuyên sâu Bài báo 1: Pipeline xử lý 6.349 hóa đơn bằng thuật toán DB + CRNN và kiểm chứng đại số kế toán.', 2)">
          P2: Tương Ứng Bài 1 (InvoiceOCR)
        </button>
        <button class="slide-tab" onclick="loadSlide('slides/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán.pdf', 'Slide P3: AI Trong Kế Toán & Kiểm Toán (Tương ứng Bài báo 2 - LLM + OCR)', 'Chuyên sâu Bài báo 2: Kết hợp OCR và Mô hình ngôn ngữ lớn LLM bóc tách hóa đơn không theo mẫu và Đối chiếu 3 bên (3-Way Matching).', 3)">
          P3: Tương Ứng Bài 2 (LLM + OCR)
        </button>
        <button class="slide-tab" onclick="loadSlide('slides/P4_paper_3_AI_in_Accounting_and_Auditing.pdf', 'Slide P4: Bắt Hóa Đơn Giả Mạo Gen-AI (Tương ứng Bài báo 3)', 'Chuyên sâu Bài báo 3: Pháp y hình ảnh số (Error Level Analysis - ELA & Wavelet) bắt hóa đơn giả mạo do AI tạo sinh.', 4)">
          P4: Tương Ứng Bài 3 (Fake Invoices)
        </button>
        <button class="slide-tab" onclick="loadSlide('slides/P5_paper_4_The_Digital_Audit_Revolution.pdf', 'Slide P5: The Digital Audit Revolution (Tương ứng Bài báo 4 - Drone AI)', 'Chuyên sâu Bài báo 4: Kiểm toán hàng tồn kho 100% bằng Drone LiDAR 3D, YOLO Object Detection và Big Data theo chuẩn mực ISA 501.', 5)">
          P5: Tương Ứng Bài 4 (Drone Audit)
        </button>
      </div>

      <!-- Embedded Iframe -->
      <div class="slide-frame-container">
        <iframe id="active-slide-frame" src="slides/P1_[Theory]_AI_in_Accounting_and_Auditing.pdf" class="slide-frame" title="Slide Viewer"></iframe>
      </div>

      <!-- Slide Controls Bar -->
      <div class="slide-controls-bar">
        <div>
          <h4 id="slide-title-display" style="color: #fff; font-size: 1rem; margin-bottom: 0.2rem;">Slide P1: Lý Thuyết Nền Tảng AI Trong Kế Toán & Kiểm Toán</h4>
          <p id="slide-desc-display" class="slide-info-text">Lý thuyết nhập môn: Từ OCR truyền thống đến Multimodal Document AI, Siêu tự động hóa IDP + AI-RPA và Kiểm toán Drone.</p>
        </div>
        <div class="slide-action-btns">
          <a id="slide-download-link" href="slides/P1_[Theory]_AI_in_Accounting_and_Auditing.pdf" target="_blank" class="slide-btn" style="background: rgba(59, 130, 246, 0.2); border-color: rgba(59, 130, 246, 0.4); color: #60a5fa;">
            📥 Tải File PDF Về Máy
          </a>
          <a id="slide-paper-link" href="papers/index.html" class="slide-btn">
            📖 Đọc Bài Báo Tương Ứng &rarr;
          </a>
          <a id="slide-video-link" href="videos/P1_[Theory]_AI_in_Accounting_and_Auditing/index.html" target="_blank" class="slide-btn" style="background: rgba(249, 115, 22, 0.2); border-color: rgba(249, 115, 22, 0.45); color: #fb923c; font-weight: 700;">
            🎬 Xem Video Giảng (P1) &rarr;
          </a>
          <button onclick="toggleFullScreen()" class="slide-btn" title="Toàn màn hình">
            ⛶ Toàn Màn Hình
          </button>
        </div>
      </div>
    </div>

    <!-- Section 1: Bộ 5 Slide Bài Giảng Chuyên Đề P1 - P5 -->
    <h2 class="section-heading">
      <div class="section-heading-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
          <line x1="8" y1="21" x2="16" y2="21"></line>
          <line x1="12" y1="17" x2="12" y2="21"></line>
        </svg>
      </div>
      Bộ 5 Slide Bài Giảng Chuyên Đề (P1 – P5) Độ Nét Cao
    </h2>

    <div class="modules-grid">

      <!-- Slide P1 -->
      <div class="module-card">
        <div class="module-thumb">
          <img src="slides/thumbnails/P1_cover.png" alt="Slide P1 Cover" />
        </div>
        <span class="module-badge" style="background: rgba(59, 130, 246, 0.15); color: #60a5fa;">Slide P1 • Lý Thuyết Tổng Quan</span>
        <h3 class="module-title">P1: AI in Accounting and Auditing</h3>
        <p class="module-desc">
          Slide định hướng nhập môn: Sự tiến hóa từ OCR cổ điển đến Document AI đa phương thức, Siêu tự động hóa Kế toán Phải trả (AP) và Kiểm toán hiện trường bằng Drone.
        </p>
        <div style="display: flex; gap: 0.6rem; flex-wrap: wrap; margin-top: auto;">
          <a href="javascript:void(0)" onclick="loadSlideAndScroll('slides/P1_[Theory]_AI_in_Accounting_and_Auditing.pdf', 'Slide P1: Lý Thuyết Nền Tảng AI Trong Kế Toán & Kiểm Toán', 'Lý thuyết nhập môn: Từ OCR truyền thống đến Multimodal Document AI, Siêu tự động hóa IDP + AI-RPA và Kiểm toán Drone.', 1)" class="module-link" style="color: #60a5fa; font-weight: 700;">
            ▶ Xem Online &rarr;
          </a>
          <a href="slides/P1_[Theory]_AI_in_Accounting_and_Auditing.pdf" target="_blank" class="module-link" style="color: var(--text-muted);">
            📊 Tải PDF &rarr;
          </a>
          <a href="videos/P1_[Theory]_AI_in_Accounting_and_Auditing/index.html" target="_blank" class="module-link" style="color: #fb923c; font-weight: 700; background: rgba(249, 115, 22, 0.15); padding: 0.25rem 0.65rem; border-radius: 6px; border: 1px solid rgba(249, 115, 22, 0.35);">
            🎬 Xem Video &rarr;
          </a>
        </div>
      </div>

      <!-- Slide P2 -->
      <div class="module-card">
        <div class="module-thumb">
          <img src="slides/thumbnails/P2_cover.png" alt="Slide P2 Cover" />
        </div>
        <span class="module-badge" style="background: rgba(139, 92, 246, 0.15); color: #c084fc;">Slide P2 • Tương Ứng Bài Báo 1</span>
        <h3 class="module-title">P2: Computer Vision in Accounting (InvoiceOCR)</h3>
        <p class="module-desc">
          Slide bài giảng chuyên sâu tương ứng Bài báo 1 (Springer Nature): Pipeline nhận dạng 6.349 hóa đơn chụp nghiêng/nhiễu qua mạng DB + CRNN và kiểm tra chéo đại số kế toán.
        </p>
        <div style="display: flex; gap: 0.6rem; flex-wrap: wrap; margin-top: auto;">
          <a href="javascript:void(0)" onclick="loadSlideAndScroll('slides/P2_paper_1_Computer_Vision_in_Accounting.pdf', 'Slide P2: Computer Vision in Accounting (Tương ứng Bài báo 1 - InvoiceOCR)', 'Chuyên sâu Bài báo 1: Pipeline xử lý 6.349 hóa đơn bằng thuật toán DB + CRNN và kiểm chứng đại số kế toán.', 2)" class="module-link" style="color: #c084fc; font-weight: 700;">
            ▶ Xem Online &rarr;
          </a>
          <a href="papers/paper_1_InvoiceOCR_Deep_Learning_Recognition_tiengviet.html" class="module-link">
            📖 Đọc Bài Báo 1 &rarr;
          </a>
          <a href="videos/P2_paper_1_Computer_Vision_in_Accounting/index.html" target="_blank" class="module-link" style="color: #c084fc; font-weight: 700; background: rgba(168, 85, 247, 0.15); padding: 0.25rem 0.65rem; border-radius: 6px; border: 1px solid rgba(168, 85, 247, 0.35);">
            🎬 Xem Video &rarr;
          </a>
        </div>
      </div>

      <!-- Slide P3 -->
      <div class="module-card">
        <div class="module-thumb">
          <img src="slides/thumbnails/P3_cover.png" alt="Slide P3 Cover" />
        </div>
        <span class="module-badge" style="background: rgba(16, 185, 129, 0.15); color: #34d399;">Slide P3 • Tương Ứng Bài Báo 2</span>
        <h3 class="module-title">P3: AI Trong Kế Toán & Kiểm Toán (LLM + OCR)</h3>
        <p class="module-desc">
          Slide bài giảng chuyên sâu tương ứng Bài báo 2 (arXiv & LUT): Kết hợp OCR và Mô hình ngôn ngữ lớn LLM để trích xuất hóa đơn phi mẫu biểu và tự động hóa Đối chiếu 3 bên (3-Way Matching).
        </p>
        <div style="display: flex; gap: 0.6rem; flex-wrap: wrap; margin-top: auto;">
          <a href="javascript:void(0)" onclick="loadSlideAndScroll('slides/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán.pdf', 'Slide P3: AI Trong Kế Toán & Kiểm Toán (Tương ứng Bài báo 2 - LLM + OCR)', 'Chuyên sâu Bài báo 2: Kết hợp OCR và Mô hình ngôn ngữ lớn LLM bóc tách hóa đơn không theo mẫu và Đối chiếu 3 bên (3-Way Matching).', 3)" class="module-link" style="color: #34d399; font-weight: 700;">
            ▶ Xem Online &rarr;
          </a>
          <a href="papers/paper_2_Automated_Invoice_LLM_OCR_tiengviet.html" class="module-link">
            📖 Đọc Bài Báo 2 &rarr;
          </a>
          <a href="videos/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán/index.html" target="_blank" class="module-link" style="color: #34d399; font-weight: 700; background: rgba(16, 185, 129, 0.15); padding: 0.25rem 0.65rem; border-radius: 6px; border: 1px solid rgba(16, 185, 129, 0.35);">
            🎬 Xem Video &rarr;
          </a>
        </div>
      </div>

      <!-- Slide P4 -->
      <div class="module-card">
        <div class="module-thumb">
          <img src="slides/thumbnails/P4_cover.png" alt="Slide P4 Cover" />
        </div>
        <span class="module-badge" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24;">Slide P4 • Tương Ứng Bài Báo 3</span>
        <h3 class="module-title">P4: AI in Accounting & Auditing (Fake Invoices)</h3>
        <p class="module-desc">
          Slide bài giảng tương ứng Bài báo 3 (BMVC & Sage): Pháp y hình ảnh số (Error Level Analysis - ELA & Wavelet) bắt hóa đơn, biên lai chi phí công tác bị chỉnh sửa bằng Gen-AI.
        </p>
        <div style="display: flex; gap: 0.6rem; flex-wrap: wrap; margin-top: auto;">
          <a href="javascript:void(0)" onclick="loadSlideAndScroll('slides/P4_paper_3_AI_in_Accounting_and_Auditing.pdf', 'Slide P4: Bắt Hóa Đơn Giả Mạo Gen-AI (Tương ứng Bài báo 3)', 'Chuyên sâu Bài báo 3: Pháp y hình ảnh số (Error Level Analysis - ELA & Wavelet) bắt hóa đơn giả mạo do AI tạo sinh.', 4)" class="module-link" style="color: #fbbf24; font-weight: 700;">
            ▶ Xem Online &rarr;
          </a>
          <a href="papers/paper_3_Fake_Invoices_Receipts_GenAI_tiengviet.html" class="module-link">
            📖 Đọc Bài Báo 3 &rarr;
          </a>
          <a href="videos/P4_paper_3_AI_in_Accounting_and_Auditing/index.html" target="_blank" class="module-link" style="color: #fbbf24; font-weight: 700; background: rgba(245, 158, 11, 0.15); padding: 0.25rem 0.65rem; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.35);">
            🎬 Xem Video &rarr;
          </a>
        </div>
      </div>

      <!-- Slide P5 -->
      <div class="module-card">
        <div class="module-thumb">
          <img src="slides/thumbnails/P5_cover.png" alt="Slide P5 Cover" />
        </div>
        <span class="module-badge" style="background: rgba(244, 63, 94, 0.15); color: #fda4af;">Slide P5 • Tương Ứng Bài Báo 4</span>
        <h3 class="module-title">P5: The Digital Audit Revolution (AI-Drone)</h3>
        <p class="module-desc">
          Slide bài giảng tương ứng Bài báo 4 (MDPI): Kiểm toán 100% hàng tồn kho hiện trường bằng Drone LiDAR 3D, mô hình YOLO và Big Data Analytics đáp ứng chuẩn mực ISA 501.
        </p>
        <div style="display: flex; gap: 0.6rem; flex-wrap: wrap; margin-top: auto;">
          <a href="javascript:void(0)" onclick="loadSlideAndScroll('slides/P5_paper_4_The_Digital_Audit_Revolution.pdf', 'Slide P5: The Digital Audit Revolution (Tương ứng Bài báo 4 - Drone AI)', 'Chuyên sâu Bài báo 4: Kiểm toán hàng tồn kho 100% bằng Drone LiDAR 3D, YOLO Object Detection và Big Data theo chuẩn mực ISA 501.', 5)" class="module-link" style="color: #fda4af; font-weight: 700;">
            ▶ Xem Online &rarr;
          </a>
          <a href="papers/paper_4_AI_Drone_BigData_Auditing_tiengviet.html" class="module-link">
            📖 Đọc Bài Báo 4 &rarr;
          </a>
          <a href="videos/P5_paper_4_The_Digital_Audit_Revolution/index.html" target="_blank" class="module-link" style="color: #fda4af; font-weight: 700; background: rgba(244, 63, 94, 0.15); padding: 0.25rem 0.65rem; border-radius: 6px; border: 1px solid rgba(244, 63, 94, 0.35);">
            🎬 Xem Video &rarr;
          </a>
        </div>
      </div>

      <!-- Card Giáo Án 70 Phút -->
      <div class="module-card">
        <div class="module-thumb" style="display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, rgba(6, 182, 212, 0.2) 0%, rgba(59, 130, 246, 0.2) 100%);">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#22d3ee" stroke-width="1.8">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
          </svg>
        </div>
        <span class="module-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee;">Giáo Án Sư Phạm</span>
        <h3 class="module-title">Kế Hoạch Giảng Dạy & Tranh Biện 70 Phút</h3>
        <p class="module-desc">
          Kịch bản sư phạm 4 bước: Giải phẫu thuật toán InvoiceOCR (15 phút) $\rightarrow$ Thảo luận nhóm bắt hóa đơn giả mạo (25 phút) $\rightarrow$ Phân tích Case Study Drone kiểm toán (15 phút) $\rightarrow$ Live Demo bóc tách hóa đơn GTGT Việt Nam (15 phút).
        </p>
        <a href="conternt day03_papers.txt" target="_blank" class="module-link" style="color: #22d3ee; font-weight: 700;">
          📄 Xem Chi Tiết Kịch Bản Giảng Dạy &rarr;
        </a>
      </div>

    </div>

    <!-- Section 2: 4 Công Trình Nghiên Cứu -->
    <h2 class="section-heading">
      <div class="section-heading-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path>
        </svg>
      </div>
      4 Bài Báo Khoa Học Quốc Tế Dịch Toàn Văn Tiếng Việt
    </h2>

    <div class="modules-grid">

      <!-- Paper 1 -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(59, 130, 246, 0.15); color: #60a5fa;">Springer Nature (2026)</span>
        <h3 class="module-title">1. InvoiceOCR: Quy Trình Nhận Dạng Hóa Đơn Tự Động</h3>
        <p class="module-desc">
          Chao Wang et al.: Mô hình DB + CRNN và kiểm tra chéo số học trên 6.349 hóa đơn thực tế, bóc tách chính xác 98,92% các trường tài chính trọng yếu.
        </p>
        <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: auto;">
          <a href="papers/paper_1_InvoiceOCR_Deep_Learning_Recognition_tiengviet.html" class="module-link">
            📖 Đọc Bản Dịch Web Tiếng Việt &rarr;
          </a>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <a href="slides/P2_paper_1_Computer_Vision_in_Accounting.pdf" target="_blank" class="module-link" style="color: #c084fc; font-weight: 600;">
              📊 Slide P2 (PDF) &rarr;
            </a>
            <a href="videos/P2_paper_1_Computer_Vision_in_Accounting/index.html" target="_blank" class="module-link" style="color: #fb923c; font-weight: 700;">
              🎬 Video P2 &rarr;
            </a>
          </div>
        </div>
      </div>

      <!-- Paper 2 -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(16, 185, 129, 0.15); color: #34d399;">arXiv cs.CV (2026)</span>
        <h3 class="module-title">2. Bóc Tách Hóa Đơn Bằng Mô Hình Ngôn Ngữ Lớn (LLM) & OCR</h3>
        <p class="module-desc">
          Khanchandani et al.: Kết hợp OCR và LLM có kiểm soát schema bóc tách hóa đơn phi mẫu biểu và Đối chiếu 3 bên, rút ngắn chu kỳ thanh toán từ 9 ngày xuống &lt; 1 phút.
        </p>
        <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: auto;">
          <a href="papers/paper_2_Automated_Invoice_LLM_OCR_tiengviet.html" class="module-link">
            📖 Đọc Bản Dịch Web Tiếng Việt &rarr;
          </a>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <a href="slides/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán.pdf" target="_blank" class="module-link" style="color: #34d399; font-weight: 600;">
              📊 Slide P3 (PDF) &rarr;
            </a>
            <a href="videos/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán/index.html" target="_blank" class="module-link" style="color: #fb923c; font-weight: 700;">
              🎬 Video P3 &rarr;
            </a>
          </div>
        </div>
      </div>

      <!-- Paper 3 -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24;">BMVC & Sage PLC (2025/2026)</span>
        <h3 class="module-title">3. Bắt Hóa Đơn & Biên Lai Giả Mạo Trong Kỷ Nguyên Gen-AI</h3>
        <p class="module-desc">
          Thornton et al. (Newcastle University & Sage PLC): Pháp y hình ảnh số (Error Level Analysis - ELA) phát hiện gian lận thanh toán công tác bằng AI tạo sinh.
        </p>
        <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: auto;">
          <a href="papers/paper_3_Fake_Invoices_Receipts_GenAI_tiengviet.html" class="module-link">
            📖 Đọc Bản Dịch Web Tiếng Việt &rarr;
          </a>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <a href="slides/P4_paper_3_AI_in_Accounting_and_Auditing.pdf" target="_blank" class="module-link" style="color: #fbbf24; font-weight: 600;">
              📊 Slide P4 (PDF) &rarr;
            </a>
            <a href="videos/P4_paper_3_AI_in_Accounting_and_Auditing/index.html" target="_blank" class="module-link" style="color: #fb923c; font-weight: 700;">
              🎬 Video P4 &rarr;
            </a>
          </div>
        </div>
      </div>

      <!-- Paper 4 -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(244, 63, 94, 0.15); color: #fda4af;">MDPI Open Access (2025)</span>
        <h3 class="module-title">4. Drone Tích Hợp AI & Dữ Liệu Lớn Trong Kiểm Toán Hiện Trường</h3>
        <p class="module-desc">
          Alhazmi et al. (Victoria University): Đột phá kiểm toán 100% hàng tồn kho bằng Drone LiDAR 3D và YOLO theo ISA 501, cắt giảm 95% thời gian và giảm 85% phát thải carbon.
        </p>
        <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: auto;">
          <a href="papers/paper_4_AI_Drone_BigData_Auditing_tiengviet.html" class="module-link">
            📖 Đọc Bản Dịch Web Tiếng Việt &rarr;
          </a>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <a href="slides/P5_paper_4_The_Digital_Audit_Revolution.pdf" target="_blank" class="module-link" style="color: #fda4af; font-weight: 600;">
              📊 Slide P5 (PDF) &rarr;
            </a>
            <a href="videos/P5_paper_4_The_Digital_Audit_Revolution/index.html" target="_blank" class="module-link" style="color: #fb923c; font-weight: 700;">
              🎬 Video P5 &rarr;
            </a>
          </div>
        </div>
      </div>

    </div>

    <!-- Footer -->
    <footer class="site-footer">
      <div class="footer-links">
        <a href="papers/index.html" class="footer-link">Thư viện 4 Bài báo Day 03 Extra</a>
        <a href="../Day02_Extra/index.html" class="footer-link">Cổng Chuyên đề Day 02 Extra</a>
        <a href="../Day01_Extra/Videos/index.html" class="footer-link">Thư viện Video Day 01 Extra</a>
        <a href="../../index.html" class="footer-link">Trang chủ Môn học</a>
      </div>
      <p>© 2026 Khoa Kế toán & Kiểm toán — Trường Đại học Đông Á (UDA). Hệ thống bài giảng và nghiên cứu thực chứng môn Trí Tuệ Nhân Tạo Trong Kế Toán.</p>
    </footer>

  </div>

  <script>
    const slidePaperMapping = {
      1: "papers/index.html",
      2: "papers/paper_1_InvoiceOCR_Deep_Learning_Recognition_tiengviet.html",
      3: "papers/paper_2_Automated_Invoice_LLM_OCR_tiengviet.html",
      4: "papers/paper_3_Fake_Invoices_Receipts_GenAI_tiengviet.html",
      5: "papers/paper_4_AI_Drone_BigData_Auditing_tiengviet.html"
    };

    const slideVideoMapping = {
      1: { url: "videos/P1_[Theory]_AI_in_Accounting_and_Auditing/index.html", label: "🎬 Xem Video Giảng (P1) &rarr;" },
      2: { url: "videos/P2_paper_1_Computer_Vision_in_Accounting/index.html", label: "🎬 Xem Video Giảng (P2) &rarr;" },
      3: { url: "videos/P3_paper 2_AI_Trong_Kế_Toán_Và_Kiểm_Toán/index.html", label: "🎬 Xem Video Giảng (P3) &rarr;" },
      4: { url: "videos/P4_paper_3_AI_in_Accounting_and_Auditing/index.html", label: "🎬 Xem Video Giảng (P4) &rarr;" },
      5: { url: "videos/P5_paper_4_The_Digital_Audit_Revolution/index.html", label: "🎬 Xem Video Giảng (P5) &rarr;" }
    };

    function loadSlide(pdfPath, title, desc, idx) {
      document.getElementById('active-slide-frame').src = pdfPath;
      document.getElementById('slide-title-display').innerText = title;
      document.getElementById('slide-desc-display').innerText = desc;
      document.getElementById('slide-download-link').href = pdfPath;
      document.getElementById('slide-paper-link').href = slidePaperMapping[idx] || "papers/index.html";

      const videoInfo = slideVideoMapping[idx] || slideVideoMapping[1];
      const videoBtn = document.getElementById('slide-video-link');
      if (videoBtn) {
        videoBtn.href = videoInfo.url;
        videoBtn.innerHTML = videoInfo.label;
      }

      const tabs = document.querySelectorAll('.slide-tab');
      tabs.forEach((tab, index) => {
        if (index === idx - 1) {
          tab.classList.add('active');
        } else {
          tab.classList.remove('active');
        }
      });
    }

    function loadSlideAndScroll(pdfPath, title, desc, idx) {
      loadSlide(pdfPath, title, desc, idx);
      const section = document.getElementById('slide-viewer-section');
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
      }
    }

    function toggleFullScreen() {
      const elem = document.getElementById('active-slide-frame');
      if (elem.requestFullscreen) {
        elem.requestFullscreen();
      } else if (elem.webkitRequestFullscreen) {
        elem.webkitRequestFullscreen();
      } else if (elem.msRequestFullscreen) {
        elem.msRequestFullscreen();
      }
    }
  </script>

</body>

</html>
"""
    out_path = os.path.join(BASE_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built Day03 Master Portal: {out_path}")

if __name__ == "__main__":
    build_papers_hub()
    build_master_portal()
