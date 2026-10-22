# -*- coding: utf-8 -*-
"""
Builder for the Master Portals:
1. Day02_Extra/papers/index.html (Dedicated Scientific Papers Hub)
2. Day02_Extra/index.html (Master Day 02 Extra Portal matching Day01_Extra)
"""

import os

BASE_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day02_Extra"
PAPERS_DIR = os.path.join(BASE_DIR, "papers")

def build_papers_hub():
    html = """<!DOCTYPE html>
<html lang="vi">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>Thư Viện Bài Báo Khoa Học & Nghiên Cứu Đỉnh Cao — Học Sâu (Deep Learning) Trong Kế Toán & Kiểm Toán (UDA)</title>
  <meta name="description"
    content="Cổng nghiên cứu học thuật toàn văn tiếng Việt chuyên sâu về Học Sâu (Deep Learning) trong Kế toán & Kiểm toán: Phát hiện gian lận BCTC, Dự báo kiệt quệ tài chính, Mô hình ngôn ngữ FinBERT và Kiểm toán sổ cái bằng Deep Autoencoders." />

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

    /* Container */
    .container {
      max-width: 1360px;
      margin: 0 auto;
      padding: 2.5rem 1.75rem 6rem;
    }

    /* Navigation Breadcrumb / Top Bar */
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
      align-items: center;
      gap: 0.75rem;
    }

    .nav-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 600;
      transition: all 0.2s ease;
    }

    .nav-btn:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-1px);
    }

    /* Hero Section */
    .hero {
      text-align: center;
      margin-bottom: 3.5rem;
      position: relative;
    }

    .hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 1rem;
      border-radius: 9999px;
      background: rgba(59, 130, 246, 0.12);
      border: 1px solid rgba(59, 130, 246, 0.3);
      color: #60a5fa;
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1.25rem;
    }

    .hero-title {
      font-family: 'Outfit', sans-serif;
      font-size: clamp(2.2rem, 4.5vw, 3.4rem);
      font-weight: 800;
      line-height: 1.18;
      letter-spacing: -0.025em;
      margin-bottom: 1.25rem;
    }

    .gradient-text {
      background: linear-gradient(135deg, #60a5fa 0%, #c084fc 50%, #22d3ee 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-desc {
      max-width: 860px;
      margin: 0 auto 2.5rem;
      color: var(--text-muted);
      font-size: 1.1rem;
      line-height: 1.75;
    }

    /* Stats Bar */
    .stats-bar {
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      flex-wrap: wrap;
      margin-bottom: 3rem;
    }

    .stat-pill {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      padding: 0.75rem 1.4rem;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-card);
      backdrop-filter: blur(12px);
    }

    .stat-icon {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .stat-num {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.2rem;
      color: var(--text-main);
      line-height: 1.1;
    }

    .stat-label {
      font-size: 0.8rem;
      color: var(--text-dim);
      font-weight: 500;
    }

    /* Toolbar: Filters & Search */
    .toolbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1.25rem;
      margin-bottom: 2.5rem;
      flex-wrap: wrap;
    }

    .filter-pills {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .filter-btn {
      padding: 0.55rem 1.15rem;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .filter-btn:hover {
      background: rgba(255, 255, 255, 0.08);
      color: #fff;
    }

    .filter-btn.active {
      background: var(--primary-gradient);
      color: #fff;
      border-color: transparent;
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35);
    }

    .search-box {
      position: relative;
      min-width: 280px;
      flex-grow: 1;
      max-width: 400px;
    }

    .search-input {
      width: 100%;
      padding: 0.65rem 1rem 0.65rem 2.6rem;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      font-size: 0.9rem;
      font-family: inherit;
      outline: none;
      transition: all 0.2s ease;
    }

    .search-input:focus {
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--primary);
      box-shadow: 0 0 12px rgba(59, 130, 246, 0.3);
    }

    .search-icon {
      position: absolute;
      left: 0.9rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      pointer-events: none;
    }

    /* Video & Paper Grid */
    .papers-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
      gap: 2rem;
    }

    @media (max-width: 768px) {
      .papers-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Paper Card */
    .paper-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-card);
      backdrop-filter: blur(12px);
      display: flex;
      flex-direction: column;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }

    .paper-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--shadow-hover);
      border-color: var(--border-glow);
      background: var(--bg-card-hover);
    }

    /* Card Thumbnail / Header Preview */
    .card-thumb-wrapper {
      position: relative;
      height: 220px;
      background: #0f172a;
      overflow: hidden;
      cursor: pointer;
    }

    .card-thumb-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      transition: transform 0.4s ease;
      filter: brightness(0.9);
    }

    .paper-card:hover .card-thumb-img {
      transform: scale(1.04);
      filter: brightness(1);
    }

    .thumb-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0, 0, 0, 0.1) 0%, rgba(11, 15, 25, 0.85) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: opacity 0.25s ease;
    }

    .read-btn-circle {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      background: var(--primary-gradient);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      box-shadow: 0 4px 18px rgba(59, 130, 246, 0.5);
      transition: transform 0.25s ease;
    }

    .paper-card:hover .read-btn-circle {
      transform: scale(1.1);
    }

    .thumb-badge {
      position: absolute;
      top: 1rem;
      left: 1rem;
      padding: 0.35rem 0.85rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      background: rgba(11, 15, 25, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid;
    }

    .thumb-journal-badge {
      position: absolute;
      top: 1rem;
      right: 1rem;
      padding: 0.35rem 0.85rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      background: rgba(11, 15, 25, 0.85);
      color: #e2e8f0;
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-subtle);
    }

    /* Card Body */
    .card-body {
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .card-header-meta {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      margin-bottom: 0.85rem;
    }

    .topic-category {
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .card-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.32rem;
      font-weight: 700;
      color: #fff;
      text-decoration: none;
      line-height: 1.35;
      margin-bottom: 0.75rem;
      transition: color 0.2s ease;
    }

    .card-title:hover {
      color: var(--accent-cyan);
    }

    .card-title-en {
      font-size: 0.88rem;
      color: var(--text-dim);
      font-style: italic;
      margin-bottom: 1rem;
      line-height: 1.4;
    }

    .card-desc {
      color: var(--text-muted);
      font-size: 0.92rem;
      line-height: 1.65;
      margin-bottom: 1.25rem;
      flex-grow: 1;
    }

    /* Tags */
    .card-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
      margin-bottom: 1.5rem;
      padding-top: 0.85rem;
      border-top: 1px solid var(--border-subtle);
    }

    .tag-item {
      font-size: 0.75rem;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      padding: 0.25rem 0.6rem;
      border-radius: 4px;
      font-weight: 500;
    }

    /* Actions */
    .card-actions {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 0.75rem;
    }

    .btn-read-main {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      background: var(--primary-gradient);
      color: #fff;
      font-weight: 600;
      font-size: 0.92rem;
      padding: 0.75rem 1.25rem;
      border-radius: var(--radius-sm);
      text-decoration: none;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35);
      transition: all 0.25s ease;
      font-family: inherit;
    }

    .btn-read-main:hover {
      box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
      transform: translateY(-2px);
    }

    .btn-secondary-group {
      display: flex;
      gap: 0.4rem;
    }

    .btn-icon-sub {
      width: 44px;
      height: 44px;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
    }

    .btn-icon-sub:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
      border-color: rgba(255, 255, 255, 0.25);
      transform: translateY(-2px);
    }

    /* Modal / Theatre Viewer */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(8px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .modal-backdrop.active {
      display: flex;
      opacity: 1;
    }

    .modal-window {
      width: 95vw;
      max-width: 1400px;
      height: 94vh;
      background: #0f172a;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    }

    .modal-header {
      padding: 0.85rem 1.5rem;
      background: #1e293b;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .modal-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: #f8fafc;
      font-family: 'Outfit', sans-serif;
    }

    .modal-ctrls {
      display: flex;
      gap: 0.6rem;
    }

    .modal-ctrl-btn {
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      color: #fff;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.15);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      text-decoration: none;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .modal-ctrl-btn:hover {
      background: rgba(255, 255, 255, 0.18);
    }

    .modal-close-btn {
      background: rgba(244, 63, 94, 0.2);
      border-color: rgba(244, 63, 94, 0.4);
      color: #fda4af;
    }

    .modal-close-btn:hover {
      background: rgba(244, 63, 94, 0.4);
      color: #fff;
    }

    .modal-iframe-wrap {
      flex-grow: 1;
      width: 100%;
      height: calc(100vh - 65px);
      background: #000;
      position: relative;
    }

    .modal-iframe {
      width: 100%;
      height: 100%;
      border: none;
      display: block;
    }

    /* Footer */
    .site-footer {
      margin-top: 5rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border-subtle);
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
      transition: color 0.2s ease;
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
      <a href="../index.html" class="brand-badge" title="Quay về Trang chủ Chuyên đề Day 02">
        <div class="brand-logo-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path>
            <path d="M6 6h10"></path>
            <path d="M6 10h10"></path>
          </svg>
        </div>
        <span>ĐẠI HỌC ĐÔNG Á • KHOA KẾ TOÁN & KIỂM TOÁN</span>
      </a>

      <div class="nav-actions">
        <a href="../../Day01_Extra/Videos/index.html" class="nav-btn" title="Xem thư viện Day 01 Extra">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
          Day 01 Extra (Học Máy)
        </a>
        <a href="../index.html" class="nav-btn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
          </svg>
          Chuyên đề Day 02 Extra
        </a>
        <a href="../../index.html" class="nav-btn">
          Trang chủ Môn học
        </a>
      </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-tag">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
        </svg>
        CỔNG HỌC THUẬT & NGHIÊN CỨU THỰC CHỨNG (DAY 02 EXTRA)
      </div>

      <h1 class="hero-title">
        Thư Viện Bài Báo Khoa Học <br />
        <span class="gradient-text">Học Sâu Trong Kế Toán & Kiểm Toán</span>
      </h1>

      <p class="hero-desc">
        Hệ thống 4 công trình nghiên cứu khoa học đỉnh cao quốc tế (Journal of Accounting Research, Contemporary Accounting Research, Elsevier Procedia và DFKI/PwC). Dịch thuật học thuật toàn văn sang tiếng Việt, tích hợp biểu đồ phân tích, dữ liệu thực nghiệm và giải pháp cho kiểm toán viên hiện đại.
      </p>

      <!-- Stats Bar -->
      <div class="stats-bar">
        <div class="stat-pill">
          <div class="stat-icon" style="background: rgba(59, 130, 246, 0.15); color: #60a5fa;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path>
              <path d="M6 6h10"></path>
              <path d="M6 10h10"></path>
            </svg>
          </div>
          <div class="stat-text">
            <div class="stat-num">04 Công Trình</div>
            <div class="stat-label">Nghiên Cứu Đỉnh Cao</div>
          </div>
        </div>

        <div class="stat-pill">
          <div class="stat-icon" style="background: rgba(16, 185, 129, 0.15); color: #34d399;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
              <line x1="3" x2="21" y1="9" y2="9"></line>
              <line x1="9" x2="9" y1="21" y2="9"></line>
            </svg>
          </div>
          <div class="stat-text">
            <div class="stat-num">81+ Trang</div>
            <div class="stat-label">Học Thuật Toàn Văn</div>
          </div>
        </div>

        <div class="stat-pill">
          <div class="stat-icon" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
          </div>
          <div class="stat-text">
            <div class="stat-num">100% Tiếng Việt</div>
            <div class="stat-label">Chuẩn Mực Kế Toán</div>
          </div>
        </div>

        <div class="stat-pill">
          <div class="stat-icon" style="background: rgba(139, 92, 246, 0.15); color: #a78bfa;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 2v20"></path>
              <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
            </svg>
          </div>
          <div class="stat-text">
            <div class="stat-num">JAR • CAR • PwC</div>
            <div class="stat-label">Hạng Nhất Học Thuật</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Toolbar: Filter Pills & Search -->
    <div class="toolbar">
      <div class="filter-pills" id="filter-pills">
        <button class="filter-btn active" data-category="all">Tất cả bài báo (4)</button>
        <button class="filter-btn" data-category="fraud">Gian lận BCTC (Bài 1)</button>
        <button class="filter-btn" data-category="distress">Kiệt quệ Tài chính (Bài 2)</button>
        <button class="filter-btn" data-category="nlp">FinBERT NLP (Bài 3)</button>
        <button class="filter-btn" data-category="audit">Autoencoder Sổ cái (Bài 4)</button>
      </div>

      <div class="search-box">
        <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
          stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <path d="m21 21-4.3-4.3"></path>
        </svg>
        <input type="text" id="search-input" class="search-input" placeholder="Tìm theo tên bài, tác giả, phương pháp..." />
      </div>
    </div>

    <!-- Papers Grid -->
    <div class="papers-grid" id="papers-grid">

      <!-- CARD 1: Fraud Detection with Raw Accounting Numbers -->
      <article class="paper-card" data-category="fraud" data-keywords="gian lận kế toán raw accounting variables số liệu thô aaers sec li yu zhang ke jar acml bp-svm balancedcascade easyensemble">
        <div class="card-thumb-wrapper" onclick="openReaderModal('paper_1_Detecting_Accounting_Fraud_tiengviet.html', 'Bài 1: Phát Hiện Gian Lận Kế Toán Bằng Biến Số BCTC Thô')">
          <img class="card-thumb-img" src="figures_paper1/fig_p4_1.jpeg" alt="Paper 1 Thumbnail" loading="lazy" />
          <div class="thumb-overlay">
            <div class="read-btn-circle" title="Đọc bài báo toàn văn">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
              </svg>
            </div>
          </div>
          <span class="thumb-badge" style="border-color: rgba(59, 130, 246, 0.4); color: #60a5fa;">Bài Báo 1</span>
          <span class="thumb-journal-badge">JAR & ACML Landmark</span>
        </div>

        <div class="card-body">
          <div class="card-header-meta">
            <span class="topic-category" style="color: #60a5fa;">Gian Lận BCTC & Học Máy</span>
          </div>

          <a href="paper_1_Detecting_Accounting_Fraud_tiengviet.html" class="card-title">
            1. Phát Hiện Gian Lận Kế Toán Bằng Tiếp Cận Học Máy & Dữ Liệu BCTC Thô
          </a>
          <div class="card-title-en">Detecting Accounting Frauds in Publicly Traded U.S. Firms via a Machine Learning Approach</div>

          <p class="card-desc">
            Công trình đột phá của Li, Yu, Zhang, Ke (mở rộng trên JAR 2020): Chứng minh việc dùng 24 biến kế toán thô vượt trội hoàn toàn so với việc dùng các tỷ số tài chính chọn lọc thủ công (Dechow F-score, Beneish M-score). Giải quyết mất cân bằng lớp cực đoan (0,7% gian lận) qua Biased-Penalty SVM và BalancedCascade đạt Balanced Accuracy 77,53%.
          </p>

          <div class="card-tags">
            <span class="tag-item">24 Biến BCTC Thô</span>
            <span class="tag-item">AAERs 90.172 Năm-Công Ty</span>
            <span class="tag-item">Biased-Penalty SVM</span>
            <span class="tag-item">BalancedCascade</span>
          </div>

          <div class="card-actions">
            <button class="btn-read-main" onclick="openReaderModal('paper_1_Detecting_Accounting_Fraud_tiengviet.html', '1. Phát Hiện Gian Lận Kế Toán Bằng Tiếp Cận Học Máy & Dữ Liệu BCTC Thô')">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
              </svg>
              Đọc Toàn Văn
            </button>
            <div class="btn-secondary-group">
              <a href="paper_1_Detecting_Accounting_Fraud_tiengviet.html" target="_blank" class="btn-icon-sub" title="Mở trang đọc Tab riêng (Full View)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
              </a>
              <a href="paper 1_Detecting Accounting Fraud in Publicly Traded U.S. Firms via a Machine Learning Approach.pdf" target="_blank" class="btn-icon-sub" title="Tải PDF Gốc Tiếng Anh">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                  <polyline points="14 2 14 8 20 8"></polyline>
                </svg>
              </a>
              <a href="paper_1_Detecting_Accounting_Fraud_tiengviet.md" target="_blank" class="btn-icon-sub" title="Xem Markdown (.md)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="4 7 4 4 20 4 20 7"></polyline>
                  <line x1="9" y1="20" x2="15" y2="20"></line>
                  <line x1="12" y1="4" x2="12" y2="20"></line>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </article>

      <!-- CARD 2: Financial Distress Prediction with Deep Learning -->
      <article class="paper-card" data-category="distress" data-keywords="kiệt quệ tài chính financial distress phá sản special treatment st sun elsevier 2024 procedia deep learning 23 chỉ số">
        <div class="card-thumb-wrapper" onclick="openReaderModal('paper_2_Financial_Distress_Prediction_tiengviet.html', 'Bài 2: Dự Báo Kiệt Quệ Tài Chính Bằng Mô Hình Học Sâu')">
          <img class="card-thumb-img" src="figures_paper2/fig1_model_arch_cropped.png" alt="Paper 2 Thumbnail" loading="lazy" />
          <div class="thumb-overlay">
            <div class="read-btn-circle" title="Đọc bài báo toàn văn">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
              </svg>
            </div>
          </div>
          <span class="thumb-badge" style="border-color: rgba(16, 185, 129, 0.4); color: #34d399;">Bài Báo 2</span>
          <span class="thumb-journal-badge">Elsevier Procedia 2024</span>
        </div>

        <div class="card-body">
          <div class="card-header-meta">
            <span class="topic-category" style="color: #34d399;">Kiệt Quệ Tài Chính & Học Sâu</span>
          </div>

          <a href="paper_2_Financial_Distress_Prediction_tiengviet.html" class="card-title">
            2. Dự Báo Kiệt Quệ Tài Chính Doanh Nghiệp Dựa Trên Mô Hình Học Sâu
          </a>
          <div class="card-title-en">Financial Distress and Earnings Prediction using Deep Learning</div>

          <p class="card-desc">
            Nghiên cứu thực nghiệm của Sun (2024) trên 465 công ty niêm yết bị cảnh báo đặc biệt (ST) và 2.325 công ty đối chứng: Xây dựng hệ thống 23 chỉ số tài chính toàn diện, ứng dụng mô hình Deep Learning 4 tầng ẩn Encoder đạt độ chính xác cảnh báo sớm trước 3 năm lên tới 82,00% đối với công ty kiệt quệ, vượt trội hơn Logistic Regression (71,00%).
          </p>

          <div class="card-tags">
            <span class="tag-item">Học Sâu 4 Tầng Ẩn</span>
            <span class="tag-item">23 Chỉ Số Tài Chính</span>
            <span class="tag-item">Cảnh Báo Trước 3 Năm (T-3)</span>
            <span class="tag-item">Độ Chính Xác 82,00%</span>
          </div>

          <div class="card-actions">
            <button class="btn-read-main" onclick="openReaderModal('paper_2_Financial_Distress_Prediction_tiengviet.html', '2. Dự Báo Kiệt Quệ Tài Chính Doanh Nghiệp Dựa Trên Mô Hình Học Sâu')">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
              </svg>
              Đọc Toàn Văn
            </button>
            <div class="btn-secondary-group">
              <a href="paper_2_Financial_Distress_Prediction_tiengviet.html" target="_blank" class="btn-icon-sub" title="Mở trang đọc Tab riêng (Full View)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
              </a>
              <a href="paper 2_Financial Distress and Earnings Prediction using Deep Learning.pdf" target="_blank" class="btn-icon-sub" title="Tải PDF Gốc Tiếng Anh">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                  <polyline points="14 2 14 8 20 8"></polyline>
                </svg>
              </a>
              <a href="paper_2_Financial_Distress_Prediction_tiengviet.md" target="_blank" class="btn-icon-sub" title="Xem Markdown (.md)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="4 7 4 4 20 4 20 7"></polyline>
                  <line x1="9" y1="20" x2="15" y2="20"></line>
                  <line x1="12" y1="4" x2="12" y2="20"></line>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </article>

      <!-- CARD 3: FinBERT Large Language Model -->
      <article class="paper-card" data-category="nlp" data-keywords="finbert nlp ngôn ngữ lớn transformer huang car 2023 contemporary accounting research sentiment esg loughran mcdonald thuyết minh bctc">
        <div class="card-thumb-wrapper" onclick="openReaderModal('paper_3_FinBERT_Large_Language_Model_tiengviet.html', 'Bài 3: FinBERT — Mô Hình Ngôn Ngữ Lớn Cho Văn Bản Tài Chính')">
          <img class="card-thumb-img" src="figures_paper3/fig4_finbert_attention_weights.png" alt="Paper 3 Thumbnail" loading="lazy" />
          <div class="thumb-overlay">
            <div class="read-btn-circle" title="Đọc bài báo toàn văn">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
              </svg>
            </div>
          </div>
          <span class="thumb-badge" style="border-color: rgba(245, 158, 11, 0.4); color: #fbbf24;">Bài Báo 3</span>
          <span class="thumb-journal-badge">CAR (FT50) Landmark</span>
        </div>

        <div class="card-body">
          <div class="card-header-meta">
            <span class="topic-category" style="color: #fbbf24;">Mô Hình Ngôn Ngữ Lớn & NLP</span>
          </div>

          <a href="paper_3_FinBERT_Large_Language_Model_tiengviet.html" class="card-title">
            3. FinBERT: Mô Hình Ngôn Ngữ Lớn Trích Xuất Thông Tin Từ Văn Bản Kế Toán
          </a>
          <div class="card-title-en">FinBERT: A Large Language Model for Extracting Information from Financial Text</div>

          <p class="card-desc">
            Công trình kinh điển của Huang, Wang, Yang (CAR, 2023): Xây dựng mô hình ngôn ngữ lớn FinBERT hiểu sâu sắc ngữ cảnh văn bản kế toán và thuyết minh BCTC. Vượt trội hoàn toàn từ điển Loughran-McDonald (Accuracy 88,2% vs 62,1%), đạt 89,5% trong phân loại ESG và giải thích biến động giá cổ phiếu vượt trội hơn 18% đến 40%.
          </p>

          <div class="card-tags">
            <span class="tag-item">FinBERT Pretraining</span>
            <span class="tag-item">Self-Attention Mechanism</span>
            <span class="tag-item">Phân Loại ESG 89,5%</span>
            <span class="tag-item">Đọc Hiểu Thuyết Minh BCTC</span>
          </div>

          <div class="card-actions">
            <button class="btn-read-main" onclick="openReaderModal('paper_3_FinBERT_Large_Language_Model_tiengviet.html', '3. FinBERT: Mô Hình Ngôn Ngữ Lớn Trích Xuất Thông Tin Từ Văn Bản Kế Toán')">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
              </svg>
              Đọc Toàn Văn
            </button>
            <div class="btn-secondary-group">
              <a href="paper_3_FinBERT_Large_Language_Model_tiengviet.html" target="_blank" class="btn-icon-sub" title="Mở trang đọc Tab riêng (Full View)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
              </a>
              <a href="paper 3_FinBERT_A Large Language Model for Extracting Information from Financial Text.pdf" target="_blank" class="btn-icon-sub" title="Tải PDF Gốc Tiếng Anh">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                  <polyline points="14 2 14 8 20 8"></polyline>
                </svg>
              </a>
              <a href="paper_3_FinBERT_Large_Language_Model_tiengviet.md" target="_blank" class="btn-icon-sub" title="Xem Markdown (.md)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="4 7 4 4 20 4 20 7"></polyline>
                  <line x1="9" y1="20" x2="15" y2="20"></line>
                  <line x1="12" y1="4" x2="12" y2="20"></line>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </article>

      <!-- CARD 4: Deep Autoencoder Anomaly Detection in SAP ERP -->
      <article class="paper-card" data-category="audit" data-keywords="autoencoder bất thường kiểm toán sổ cái general ledger sap erp schreyer pwc dfki reconstruction error sai số tái tạo jet">
        <div class="card-thumb-wrapper" onclick="openReaderModal('paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.html', 'Bài 4: Phát Hiện Bất Thường Sổ Cái Bằng Deep Autoencoder (PwC)')">
          <img class="card-thumb-img" src="figures_paper4/fig2_autoencoder_arch_cropped.png" alt="Paper 4 Thumbnail" loading="lazy" />
          <div class="thumb-overlay">
            <div class="read-btn-circle" title="Đọc bài báo toàn văn">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
              </svg>
            </div>
          </div>
          <span class="thumb-badge" style="border-color: rgba(139, 92, 246, 0.4); color: #a78bfa;">Bài Báo 4</span>
          <span class="thumb-journal-badge">PwC & DFKI Landmark</span>
        </div>

        <div class="card-body">
          <div class="card-header-meta">
            <span class="topic-category" style="color: #a78bfa;">Kiểm Toán Sổ Cái & Autoencoder</span>
          </div>

          <a href="paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.html" class="card-title">
            4. Phát Hiện Bất Thường Trong Dữ Liệu Kế Toán Bằng Deep Autoencoder
          </a>
          <div class="card-title-en">Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoder Networks</div>

          <p class="card-desc">
            Công trình nghiên cứu đột phá hợp tác giữa Trung tâm AI Đức (DFKI) và Hãng kiểm toán PwC: Tự động hóa thủ tục kiểm tra bút toán (Journal Entry Testing) trên hàng triệu giao dịch SAP ERP. Tận dụng sai số tái tạo của mạng Autoencoder 9 tầng ẩn để bắt bất thường ngữ cảnh, giảm 97,5% cảnh báo giả so với phương pháp truyền thống.
          </p>

          <div class="card-tags">
            <span class="tag-item">SAP ERP Sổ Cái</span>
            <span class="tag-item">Reconstruction Error</span>
            <span class="tag-item">Kiểm Toán 100% Bút Toán</span>
            <span class="tag-item">Giảm 97,5% Báo Động Giả</span>
          </div>

          <div class="card-actions">
            <button class="btn-read-main" onclick="openReaderModal('paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.html', '4. Phát Hiện Bất Thường Trong Dữ Liệu Kế Toán Bằng Deep Autoencoder')">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
              </svg>
              Đọc Toàn Văn
            </button>
            <div class="btn-secondary-group">
              <a href="paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.html" target="_blank" class="btn-icon-sub" title="Mở trang đọc Tab riêng (Full View)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
              </a>
              <a href="paper 4_Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoder Networks.pdf" target="_blank" class="btn-icon-sub" title="Tải PDF Gốc Tiếng Anh">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                  <polyline points="14 2 14 8 20 8"></polyline>
                </svg>
              </a>
              <a href="paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.md" target="_blank" class="btn-icon-sub" title="Xem Markdown (.md)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="4 7 4 4 20 4 20 7"></polyline>
                  <line x1="9" y1="20" x2="15" y2="20"></line>
                  <line x1="12" y1="4" x2="12" y2="20"></line>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </article>

    </div>

    <!-- Empty search state -->
    <div class="empty-state" id="empty-state" style="display: none; text-align: center; padding: 4rem 1rem;">
      <div style="font-size: 3rem; margin-bottom: 1rem; opacity: 0.6;">🔍</div>
      <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem;">Không tìm thấy bài báo phù hợp</h3>
      <p style="color: var(--text-muted);">Vui lòng thử lại với từ khóa khác (ví dụ: gian lận, finbert, autoencoder, kiệt quệ...)</p>
    </div>

    <!-- Footer -->
    <footer class="site-footer">
      <div class="footer-links">
        <a href="../index.html" class="footer-link">Trang chủ Day 02 Extra</a>
        <a href="../../Day01_Extra/Videos/index.html" class="footer-link">Thư viện Video Day 01 Extra</a>
        <a href="../../index.html" class="footer-link">Cổng thông tin Môn học AI Kế toán</a>
      </div>
      <p>Khoa Kế toán & Kiểm toán — Trường Đại học Đông Á (UDA)</p>
      <p style="margin-top: 0.35rem; font-size: 0.8rem; color: var(--text-dim);">Chương trình Đào tạo Tiên tiến Kế toán Số & Trí Tuệ Nhân Tạo (2026)</p>
    </footer>

  </div>

  <!-- Modal / Theatre Viewer -->
  <div class="modal-backdrop" id="reader-modal" onclick="closeReaderModal(event)">
    <div class="modal-window" onclick="event.stopPropagation()">
      <div class="modal-header">
        <div class="modal-title" id="modal-title">Đọc Bài Báo Học Thuật</div>
        <div class="modal-ctrls">
          <a href="#" id="modal-full-tab" target="_blank" class="modal-ctrl-btn" title="Mở tab riêng">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
              <polyline points="15 3 21 3 21 9"></polyline>
            </svg>
            Tab Riêng
          </a>
          <button class="modal-ctrl-btn modal-close-btn" onclick="closeReaderModal()">
            ✕ Đóng
          </button>
        </div>
      </div>
      <div class="modal-iframe-wrap">
        <iframe src="" class="modal-iframe" id="reader-iframe"></iframe>
      </div>
    </div>
  </div>

  <script>
    // Modal Reader Logic
    const modal = document.getElementById('reader-modal');
    const iframe = document.getElementById('reader-iframe');
    const modalTitle = document.getElementById('modal-title');
    const modalFullTab = document.getElementById('modal-full-tab');

    function openReaderModal(url, title) {
      modalTitle.textContent = title;
      modalFullTab.href = url;
      iframe.src = url;
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeReaderModal(e) {
      if (!e || e.target === modal || e.target.classList.contains('modal-close-btn')) {
        modal.classList.remove('active');
        iframe.src = '';
        document.body.style.overflow = '';
      }
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeReaderModal();
      }
    });

    // Filter & Search Logic
    const filterBtns = document.querySelectorAll('.filter-btn');
    const searchInput = document.getElementById('search-input');
    const cards = document.querySelectorAll('.paper-card');
    const emptyState = document.getElementById('empty-state');

    let currentCategory = 'all';
    let searchQuery = '';

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentCategory = btn.getAttribute('data-category');
        applyFilters();
      });
    });

    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      applyFilters();
    });

    function applyFilters() {
      let visibleCount = 0;
      cards.forEach(card => {
        const cat = card.getAttribute('data-category');
        const keywords = card.getAttribute('data-keywords') || '';
        const title = card.querySelector('.card-title').textContent.toLowerCase();
        const desc = card.querySelector('.card-desc').textContent.toLowerCase();

        const matchCat = (currentCategory === 'all' || cat === currentCategory);
        const matchSearch = (!searchQuery || title.includes(searchQuery) || desc.includes(searchQuery) || keywords.includes(searchQuery));

        if (matchCat && matchSearch) {
          card.style.display = 'flex';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  </script>

</body>

</html>
"""
    hub_path = os.path.join(PAPERS_DIR, "index.html")
    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Papers Hub: {hub_path}")

def build_day02_master_index():
    # Day02_Extra/index.html - The master portal for Day 02 Extra
    html = """<!DOCTYPE html>
<html lang="vi">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>Chuyên Đề Nâng Cao: Học Sâu (Deep Learning) Trong Kế Toán & Kiểm Toán — Đại học Đông Á</title>
  <meta name="description"
    content="Cổng chuyên đề nâng cao Day 02 Extra: Học Sâu (Deep Learning) trong Kế toán & Kiểm toán. Tích hợp Slide bài giảng lý thuyết, giáo trình chi tiết và Thư viện 4 bài báo khoa học quốc tế đỉnh cao dịch toàn văn tiếng Việt." />

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
      align-items: center;
      gap: 0.75rem;
    }

    .nav-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 600;
      transition: all 0.2s ease;
    }

    .nav-btn:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
      transform: translateY(-1px);
    }

    /* Hero Section */
    .hero {
      text-align: center;
      margin-bottom: 3.5rem;
    }

    .hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 1rem;
      border-radius: 9999px;
      background: rgba(139, 92, 246, 0.15);
      border: 1px solid rgba(139, 92, 246, 0.35);
      color: #c084fc;
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1.25rem;
    }

    .hero-title {
      font-family: 'Outfit', sans-serif;
      font-size: clamp(2.2rem, 4.5vw, 3.5rem);
      font-weight: 800;
      line-height: 1.18;
      letter-spacing: -0.025em;
      margin-bottom: 1.25rem;
    }

    .gradient-text {
      background: linear-gradient(135deg, #a78bfa 0%, #38bdf8 50%, #34d399 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-desc {
      max-width: 860px;
      margin: 0 auto 2.5rem;
      color: var(--text-muted);
      font-size: 1.1rem;
      line-height: 1.75;
    }

    /* Featured Banner */
    .feature-banner {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.18) 0%, rgba(139, 92, 246, 0.18) 100%);
      border: 1px solid rgba(139, 92, 246, 0.35);
      border-radius: var(--radius-lg);
      padding: 2.25rem 2.5rem;
      margin-bottom: 3.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 2rem;
      flex-wrap: wrap;
      box-shadow: 0 15px 35px -10px rgba(139, 92, 246, 0.25);
    }

    .banner-text h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.6rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.5rem;
    }

    .banner-text p {
      color: #cbd5e1;
      font-size: 1rem;
      max-width: 700px;
      line-height: 1.6;
    }

    .banner-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.85rem 1.75rem;
      border-radius: var(--radius-md);
      background: var(--primary-gradient);
      color: #fff;
      font-weight: 700;
      font-size: 1rem;
      text-decoration: none;
      box-shadow: 0 4px 18px rgba(59, 130, 246, 0.4);
      transition: all 0.25s ease;
    }

    .banner-btn:hover {
      box-shadow: 0 8px 25px rgba(59, 130, 246, 0.6);
      transform: translateY(-2px);
    }

    /* Sections */
    .section-heading {
      font-family: 'Outfit', sans-serif;
      font-size: 1.75rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 1.75rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .section-heading-icon {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: rgba(59, 130, 246, 0.15);
      color: #60a5fa;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .modules-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 1.75rem;
      margin-bottom: 4rem;
    }

    .module-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.75rem;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      transition: all 0.25s ease;
    }

    .module-card:hover {
      transform: translateY(-4px);
      border-color: var(--border-glow);
      background: var(--bg-card-hover);
    }

    .module-badge {
      display: inline-block;
      align-self: flex-start;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.25rem 0.65rem;
      border-radius: 4px;
      margin-bottom: 1rem;
    }

    .module-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.65rem;
      text-decoration: none;
    }

    .module-desc {
      color: var(--text-muted);
      font-size: 0.92rem;
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

    /* Footer */
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
        CHUYÊN ĐỀ BÀI GIẢNG & NGHIÊN CỨU THỰC CHỨNG (DAY 02 EXTRA)
      </div>

      <h1 class="hero-title">
        Chuyên Đề Nâng Cao <br />
        <span class="gradient-text">Học Sâu Trong Kế Toán & Kiểm Toán</span>
      </h1>

      <p class="hero-desc">
        Hệ thống tài liệu sư phạm toàn diện từ giáo trình lý thuyết 100 phút, slide bài giảng độ nét cao đến 4 công trình nghiên cứu khoa học thực chứng quốc tế đỉnh cao dịch toàn văn tiếng Việt.
      </p>
    </section>

    <!-- Feature Banner: Papers Hub -->
    <div class="feature-banner">
      <div class="banner-text">
        <h3>📚 Thư Viện 4 Bài Báo Khoa Học Quốc Tế Đỉnh Cao</h3>
        <p>Bản dịch tiếng Việt học thuật toàn văn các nghiên cứu từ Journal of Accounting Research (JAR), Contemporary Accounting Research (CAR), Elsevier Procedia và DFKI/PwC.</p>
      </div>
      <a href="papers/index.html" class="banner-btn">
        <span>Khám Phá Thư Viện Bài Báo</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <line x1="5" y1="12" x2="19" y2="12"></line>
          <polyline points="12 5 19 12 12 19"></polyline>
        </svg>
      </a>
    </div>

    <!-- Section 1: Giáo Trình & Lý Thuyết -->
    <h2 class="section-heading">
      <div class="section-heading-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
          <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
        </svg>
      </div>
      Tài Liệu Lý Thuyết & Giáo Án Chuyên Sâu
    </h2>

    <div class="modules-grid">
      <!-- Card: Giáo Án 100 Phút -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(59, 130, 246, 0.15); color: #60a5fa;">Giáo Án Sư Phạm</span>
        <h3 class="module-title">Giáo Án Chi Tiết 100 Phút: Học Sâu Trong Kế Toán</h3>
        <p class="module-desc">
          Kế hoạch bài giảng sư phạm Chain of Thought và Tree of Thought: Từ điểm nghẽn của ML truyền thống đến DNN, CNN đọc hóa đơn, LSTM dự báo dòng tiền, FinBERT và Deep Autoencoder bắt gian lận sổ cái.
        </p>
        <a href="deepleanring_for_accounting.txt" target="_blank" class="module-link">
          Xem Toàn Văn Giáo Án (Text) &rarr;
        </a>
      </div>

      <!-- Card: Slide Lý Thuyết PDF -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(139, 92, 246, 0.15); color: #a78bfa;">Slide Bài Giảng</span>
        <h3 class="module-title">Slide Lý Thuyết Học Sâu Trong Kế Toán (PDF)</h3>
        <p class="module-desc">
          Bộ slide bài giảng chuẩn mực trực quan hóa kiến trúc mạng nơ-ron sâu, giải thuật tối ưu hóa Backpropagation và ứng dụng kiểm toán số.
        </p>
        <a href="Lý Thuyết Học Sâu Trong Kế Toán.pdf" target="_blank" class="module-link">
          Tải Slide Bài Giảng PDF &rarr;
        </a>
      </div>

      <!-- Card: Slide Part 1 -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(16, 185, 129, 0.15); color: #34d399;">Slide Thực Chiến</span>
        <h3 class="module-title">P1: Deep Learning in Accounting & Finance</h3>
        <p class="module-desc">
          Slide bài giảng chuyên sâu Part 1 về các ứng dụng học sâu trong tự động hóa kế toán, xử lý ngôn ngữ tự nhiên và kiểm soát nội bộ.
        </p>
        <a href="P1_Deep_Learning_in_Accounting.pdf" target="_blank" class="module-link">
          Tải Slide Part 1 PDF &rarr;
        </a>
      </div>
    </div>

    <!-- Section 2: 4 Công Trình Nghiên Cứu -->
    <h2 class="section-heading">
      <div class="section-heading-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="2" y1="12" x2="22" y2="12"></line>
        </svg>
      </div>
      4 Bài Báo Khoa Học Quốc Tế Dịch Toàn Văn Tiếng Việt
    </h2>

    <div class="modules-grid">
      <!-- Paper 1 -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(59, 130, 246, 0.15); color: #60a5fa;">JAR / ACML Landmark</span>
        <h3 class="module-title">1. Phát Hiện Gian Lận BCTC Bằng Biến Số Kế Toán Thô</h3>
        <p class="module-desc">
          Li, Yu, Zhang, Ke: Đột phá dùng 24 biến BCTC thô thay cho tỷ số tài chính, giải quyết mất cân bằng lớp cực đoan 0,7% qua BP-SVM và BalancedCascade đạt BAC 77,53%.
        </p>
        <a href="papers/paper_1_Detecting_Accounting_Fraud_tiengviet.html" class="module-link">
          Đọc Bản Dịch Web Tiếng Việt &rarr;
        </a>
      </div>

      <!-- Paper 2 -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(16, 185, 129, 0.15); color: #34d399;">Elsevier Procedia 2024</span>
        <h3 class="module-title">2. Dự Báo Kiệt Quệ Tài Chính Bằng Mô Hình Học Sâu</h3>
        <p class="module-desc">
          Sun: Mạng học sâu 4 tầng Encoder trên 2.790 công ty niêm yết, đạt độ chính xác cảnh báo sớm trước 3 năm lên tới 82,00% đối với công ty kiệt quệ tài chính.
        </p>
        <a href="papers/paper_2_Financial_Distress_Prediction_tiengviet.html" class="module-link">
          Đọc Bản Dịch Web Tiếng Việt &rarr;
        </a>
      </div>

      <!-- Paper 3 -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24;">CAR (FT50) Landmark</span>
        <h3 class="module-title">3. FinBERT: Mô Hình Ngôn Ngữ Lớn Cho Văn Bản Kế Toán</h3>
        <p class="module-desc">
          Huang, Wang, Yang: Mô hình BERT tài chính hiểu sâu sắc Thuyết minh BCTC, đạt F1 87,8% phân loại sắc thái câu và 89,5% phân loại ESG, vượt trội hơn từ điển LM 18% - 40%.
        </p>
        <a href="papers/paper_3_FinBERT_Large_Language_Model_tiengviet.html" class="module-link">
          Đọc Bản Dịch Web Tiếng Việt &rarr;
        </a>
      </div>

      <!-- Paper 4 -->
      <div class="module-card">
        <span class="module-badge" style="background: rgba(139, 92, 246, 0.15); color: #a78bfa;">PwC & DFKI Landmark</span>
        <h3 class="module-title">4. Phát Hiện Bất Thường Sổ Cái Bằng Deep Autoencoder</h3>
        <p class="module-desc">
          Schreyer, Sattarov, PwC: Ứng dụng sai số tái tạo của mạng Autoencoder 9 tầng ẩn kiểm tra 100% bút toán SAP ERP, giảm 97,5% cảnh báo giả cho kiểm toán viên.
        </p>
        <a href="papers/paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.html" class="module-link">
          Đọc Bản Dịch Web Tiếng Việt &rarr;
        </a>
      </div>
    </div>

    <!-- Footer -->
    <footer class="site-footer">
      <div class="footer-links">
        <a href="papers/index.html" class="footer-link">Thư viện Bài báo Day 02 Extra</a>
        <a href="../Day01_Extra/Videos/index.html" class="footer-link">Thư viện Video Day 01 Extra</a>
        <a href="../../index.html" class="footer-link">Cổng thông tin Môn học AI Kế toán</a>
      </div>
      <p>Khoa Kế toán & Kiểm toán — Trường Đại học Đông Á (UDA)</p>
      <p style="margin-top: 0.35rem; font-size: 0.8rem; color: var(--text-dim);">Chương trình Đào tạo Tiên tiến Kế toán Số & Trí Tuệ Nhân Tạo (2026)</p>
    </footer>

  </div>

</body>

</html>
"""
    master_path = os.path.join(BASE_DIR, "index.html")
    with open(master_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Master Day02 Extra Index: {master_path}")

if __name__ == "__main__":
    build_papers_hub()
    build_day02_master_index()
