# -*- coding: utf-8 -*-
"""
Builder script to generate Vietnamese translations (.md and .html)
and interactive web portals for Day 02 Extra Papers in Accounting & Auditing.
"""

import os
import sys

BASE_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day02_Extra"
PAPERS_DIR = os.path.join(BASE_DIR, "papers")

def get_html_template(title, title_en, authors, journal, doi, badge, sidebar_links, content_html, active_paper_idx=1):
    return f"""<!DOCTYPE html>
<html lang="vi">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>{title} — Bản Dịch Học Thuật Tiếng Việt (UDA)</title>
  <meta name="description" content="Bản dịch tiếng Việt học thuật toàn văn công trình nghiên cứu: {title_en} ({authors}). Tích hợp biểu đồ, ma trận dữ liệu và phân tích nghiệp vụ kế toán kiểm toán chuyên sâu." />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400&family=Outfit:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-body: #f8fafc;
      --bg-surface: #ffffff;
      --bg-sidebar: #0f172a;
      --sidebar-text: #e2e8f0;
      --sidebar-muted: #94a3b8;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --primary: #2563eb;
      --primary-light: #eff6ff;
      --primary-border: #bfdbfe;
      --accent: #0ea5e9;
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --border-color: #e2e8f0;
      --code-bg: #1e293b;
      --code-text: #f1f5f9;
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
      --content-font-size: 1.05rem;
      --line-height: 1.85;
      --radius-md: 12px;
      --radius-sm: 8px;
    }}

    [data-theme="dark"] {{
      --bg-body: #0b0f19;
      --bg-surface: #131b2e;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --primary: #3b82f6;
      --primary-light: rgba(59, 130, 246, 0.15);
      --primary-border: rgba(59, 130, 246, 0.35);
      --border-color: #1e293b;
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 10px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 12px 24px rgba(0, 0, 0, 0.5);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: var(--line-height);
      font-size: var(--content-font-size);
      display: flex;
      min-height: 100vh;
      transition: background-color 0.25s ease, color 0.25s ease;
    }}

    /* Reading Progress Bar */
    #progress-bar {{
      position: fixed;
      top: 0;
      left: 0;
      height: 4px;
      background: linear-gradient(90deg, #2563eb, #38bdf8, #8b5cf6);
      width: 0%;
      z-index: 9999;
      transition: width 0.1s linear;
    }}

    /* Sidebar Navigation */
    .sidebar {{
      width: 330px;
      background-color: var(--bg-sidebar);
      color: var(--sidebar-text);
      height: 100vh;
      position: sticky;
      top: 0;
      overflow-y: auto;
      flex-shrink: 0;
      border-right: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      flex-direction: column;
      z-index: 100;
    }}

    .sidebar-header {{
      padding: 1.5rem 1.25rem 1rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}

    .sidebar-title {{
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #38bdf8;
      margin-bottom: 0.4rem;
    }}

    .sidebar-subtitle {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      line-height: 1.35;
      font-family: 'Outfit', sans-serif;
    }}

    .sidebar-author {{
      font-size: 0.8rem;
      color: var(--sidebar-muted);
      margin-top: 0.35rem;
    }}

    .sidebar-nav {{
      padding: 1rem 0.75rem 2.5rem;
      flex-grow: 1;
    }}

    .nav-group-title {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #64748b;
      padding: 0.85rem 0.65rem 0.35rem;
    }}

    .sidebar-link {{
      display: block;
      padding: 0.5rem 0.75rem;
      font-size: 0.88rem;
      color: var(--sidebar-muted);
      text-decoration: none;
      border-radius: var(--radius-sm);
      transition: all 0.15s ease;
      line-height: 1.4;
      margin-bottom: 2px;
    }}

    .sidebar-link:hover {{
      color: #ffffff;
      background-color: rgba(255, 255, 255, 0.08);
      transform: translateX(3px);
    }}

    .sidebar-link.active {{
      color: #ffffff;
      background-color: var(--primary);
      font-weight: 600;
    }}

    .sidebar-link.sub-link {{
      padding-left: 1.6rem;
      font-size: 0.83rem;
    }}

    /* Main Content Wrapper */
    .main-wrapper {{
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
    }}

    /* Top Floating Utility Bar */
    .top-bar {{
      position: sticky;
      top: 0;
      background-color: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      padding: 0.75rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 90;
      box-shadow: var(--shadow-sm);
      backdrop-filter: blur(10px);
    }}

    .top-bar-left {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}

    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 600;
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      transition: all 0.2s;
    }}

    .back-btn:hover {{
      color: var(--primary);
      border-color: var(--primary-border);
      background: var(--primary-light);
    }}

    .top-bar-right {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .util-btn {{
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      width: 36px;
      height: 36px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-family: inherit;
      font-size: 0.85rem;
      font-weight: 700;
      transition: all 0.2s;
    }}

    .util-btn:hover {{
      color: var(--text-main);
      border-color: var(--primary);
    }}

    /* Article Paper Layout */
    .article-container {{
      max-width: 980px;
      width: 100%;
      margin: 1.5rem auto 4rem;
      padding: 3rem 2.75rem 6rem;
      background: var(--bg-surface);
      box-shadow: var(--shadow-sm);
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
    }}

    @media (max-width: 1024px) {{
      .sidebar {{
        display: none;
      }}
      .article-container {{
        padding: 2rem 1.25rem 4rem;
        margin-top: 0;
        border-radius: 0;
        border: none;
      }}
    }}

    /* Document Header */
    .paper-header {{
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 2rem;
      margin-bottom: 2.5rem;
      text-align: center;
    }}

    .paper-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 0.9rem;
      border-radius: 9999px;
      background: var(--primary-light);
      border: 1px solid var(--primary-border);
      color: var(--primary);
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 1.25rem;
    }}

    .paper-title {{
      font-family: 'Outfit', sans-serif;
      font-size: clamp(1.85rem, 3.5vw, 2.6rem);
      font-weight: 800;
      line-height: 1.25;
      color: var(--text-main);
      margin-bottom: 1rem;
      letter-spacing: -0.02em;
    }}

    .paper-title-en {{
      font-size: 1.15rem;
      color: var(--text-muted);
      font-weight: 500;
      font-style: italic;
      margin-bottom: 1.5rem;
      line-height: 1.45;
    }}

    .paper-meta-grid {{
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      flex-wrap: wrap;
      font-size: 0.9rem;
      color: var(--text-muted);
      background: var(--bg-body);
      padding: 1rem 1.5rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      margin-top: 1.25rem;
      text-align: left;
    }}

    .meta-item strong {{
      color: var(--text-main);
    }}

    /* Abstract Block */
    .abstract-box {{
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.04) 0%, rgba(14, 165, 233, 0.04) 100%);
      border-left: 4px solid var(--primary);
      padding: 1.75rem 2rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-bottom: 3rem;
      border-top: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }}

    .abstract-heading {{
      font-size: 1.15rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--primary);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-family: 'Outfit', sans-serif;
    }}

    .abstract-text {{
      font-family: 'Merriweather', serif;
      font-size: 1.02rem;
      line-height: 1.85;
      color: var(--text-main);
      text-align: justify;
    }}

    .keywords-box {{
      margin-top: 1rem;
      font-size: 0.9rem;
      color: var(--text-muted);
    }}

    .keywords-box strong {{
      color: var(--primary);
    }}

    /* Academic Typography */
    h2.section-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.7rem;
      font-weight: 800;
      color: var(--text-main);
      margin-top: 3.5rem;
      margin-bottom: 1.25rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--border-color);
      display: flex;
      align-items: center;
      gap: 0.75rem;
      scroll-margin-top: 80px;
    }}

    h2.section-title .section-number {{
      background: var(--primary);
      color: #fff;
      font-size: 1rem;
      padding: 0.2rem 0.65rem;
      border-radius: 6px;
      font-weight: 700;
    }}

    h3.sub-section-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--text-main);
      margin-top: 2.25rem;
      margin-bottom: 0.85rem;
      scroll-margin-top: 80px;
    }}

    h4.tertiary-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary);
      margin-top: 1.5rem;
      margin-bottom: 0.6rem;
      scroll-margin-top: 80px;
    }}

    p {{
      margin-bottom: 1.35rem;
      text-align: justify;
    }}

    ul, ol {{
      margin-left: 1.75rem;
      margin-bottom: 1.5rem;
    }}

    li {{
      margin-bottom: 0.5rem;
    }}

    strong {{
      color: var(--text-main);
      font-weight: 700;
    }}

    /* Callout & Alerts */
    .callout {{
      padding: 1.25rem 1.5rem;
      border-radius: var(--radius-sm);
      margin: 1.75rem 0;
      border-left: 4px solid;
      background: var(--bg-body);
      border-top: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }}

    .callout-info {{
      border-left-color: var(--primary);
      background: var(--primary-light);
    }}

    .callout-warning {{
      border-left-color: var(--warning);
      background: rgba(245, 158, 11, 0.08);
    }}

    .callout-success {{
      border-left-color: var(--success);
      background: rgba(16, 185, 129, 0.08);
    }}

    .callout-title {{
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    /* Figure Card */
    .figure-wrapper {{
      margin: 2.5rem 0;
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      text-align: center;
    }}

    .figure-header {{
      padding: 0.75rem 1.25rem;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
    }}

    .figure-badge {{
      background: var(--primary-light);
      color: var(--primary);
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      font-weight: 700;
      font-size: 0.8rem;
    }}

    .figure-img-container {{
      padding: 1.5rem;
      background: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
    }}

    .figure-img {{
      max-width: 100%;
      height: auto;
      border-radius: 4px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
      transition: transform 0.25s ease;
      cursor: zoom-in;
    }}

    .figure-img:hover {{
      transform: scale(1.02);
    }}

    .figure-caption {{
      padding: 1rem 1.5rem;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-color);
      font-size: 0.92rem;
      color: var(--text-muted);
      text-align: center;
      line-height: 1.6;
    }}

    .figure-caption strong {{
      color: var(--text-main);
    }}

    /* Academic Data Tables */
    .table-container {{
      overflow-x: auto;
      margin: 2rem 0;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
    }}

    table.academic-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
      text-align: left;
    }}

    table.academic-table th {{
      background: var(--primary);
      color: #ffffff;
      padding: 0.85rem 1rem;
      font-weight: 700;
      letter-spacing: 0.02em;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }}

    table.academic-table td {{
      padding: 0.75rem 1rem;
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--text-main);
    }}

    table.academic-table tr:nth-child(even) td {{
      background: var(--bg-body);
    }}

    table.academic-table tr:hover td {{
      background: var(--primary-light);
    }}

    /* Math Formula Block */
    .formula-box {{
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      margin: 1.5rem 0;
      text-align: center;
      font-family: 'Fira Code', monospace;
      font-size: 1.05rem;
      color: var(--text-main);
      overflow-x: auto;
    }}

    /* Code Blocks */
    .code-wrapper {{
      margin: 1.75rem 0;
      border-radius: var(--radius-sm);
      overflow: hidden;
      border: 1px solid #334155;
      background: var(--code-bg);
      box-shadow: var(--shadow-md);
    }}

    .code-header {{
      background: #0f172a;
      padding: 0.5rem 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #94a3b8;
      font-size: 0.8rem;
      font-family: 'Fira Code', monospace;
      border-bottom: 1px solid #1e293b;
    }}

    pre code {{
      display: block;
      padding: 1.25rem 1.5rem;
      font-family: 'Fira Code', monospace;
      font-size: 0.88rem;
      line-height: 1.6;
      color: var(--code-text);
      overflow-x: auto;
      white-space: pre;
    }}

    /* References List */
    .references-list {{
      list-style-type: none;
      margin-left: 0;
    }}

    .references-list li {{
      padding-left: 2rem;
      text-indent: -2rem;
      margin-bottom: 1rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    .references-list li strong {{
      color: var(--text-main);
    }}

    /* Footer */
    .article-footer {{
      border-top: 2px solid var(--border-color);
      padding-top: 2.5rem;
      margin-top: 4rem;
      text-align: center;
      font-size: 0.88rem;
      color: var(--text-muted);
    }}

    .footer-nav-buttons {{
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }}

    .footer-nav-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.75rem 1.25rem;
      border-radius: var(--radius-sm);
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      transition: all 0.2s ease;
    }}

    .footer-nav-btn:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary);
      transform: translateY(-2px);
    }}

    /* Print Styles */
    @media print {{
      .sidebar, .top-bar, #progress-bar, .footer-nav-buttons {{
        display: none !important;
      }}
      .article-container {{
        box-shadow: none;
        border: none;
        padding: 0;
        margin: 0;
        max-width: 100%;
      }}
      body {{
        background: #fff;
        color: #000;
        font-size: 11pt;
      }}
    }}
  </style>
</head>

<body>

  <!-- Reading Progress Bar -->
  <div id="progress-bar"></div>

  <!-- Sidebar Navigation -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-title">Bản Dịch Học Thuật Tiếng Việt (UDA)</div>
      <div class="sidebar-subtitle">{badge}</div>
      <div class="sidebar-author">{authors}</div>
    </div>

    <nav class="sidebar-nav">
      <div class="nav-group-title">Nội Dung Bài Báo</div>
      {sidebar_links}
      
      <div class="nav-group-title">Danh Mục Bài Báo Day 02</div>
      <a href="paper_1_Detecting_Accounting_Fraud_tiengviet.html" class="sidebar-link {'active' if active_paper_idx==1 else ''}">Bài 1: Gian Lận BCTC (JAR/ACML)</a>
      <a href="paper_2_Financial_Distress_Prediction_tiengviet.html" class="sidebar-link {'active' if active_paper_idx==2 else ''}">Bài 2: Kiệt Quệ Tài Chính (Elsevier)</a>
      <a href="paper_3_FinBERT_Large_Language_Model_tiengviet.html" class="sidebar-link {'active' if active_paper_idx==3 else ''}">Bài 3: FinBERT NLP (CAR)</a>
      <a href="paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.html" class="sidebar-link {'active' if active_paper_idx==4 else ''}">Bài 4: Autoencoder Sổ Cái (DFKI/PwC)</a>
      
      <div class="nav-group-title">Slide & Tài Liệu Gốc</div>
      <a href="{get_slide_filename(active_paper_idx)}" target="_blank" class="sidebar-link" style="color: #c084fc; font-weight: 700;">📊 Tải Slide P{active_paper_idx} (PDF)</a>
      <a href="{get_pdf_filename(active_paper_idx)}" target="_blank" class="sidebar-link">📄 Tải PDF Gốc Tiếng Anh</a>
      <a href="index.html" class="sidebar-link">📚 Thư Viện Bài Báo Day 02</a>
      <a href="../index.html" class="sidebar-link">🏠 Cổng Chuyên Đề Day 02</a>
    </nav>
  </aside>

  <!-- Main Wrapper -->
  <div class="main-wrapper">

    <!-- Top Utility Bar -->
    <header class="top-bar">
      <div class="top-bar-left">
        <a href="index.html" class="back-btn" title="Quay về Danh mục Thư viện Bài báo Day 02">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
          Thư Viện Bài Báo
        </a>
        <a href="../index.html" class="back-btn" title="Quay về Trang chủ Chuyên đề Day 02 Extra">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
          </svg>
          Day 02 Extra
        </a>
        <a href="{get_slide_filename(active_paper_idx)}" target="_blank" class="back-btn" style="color: #8b5cf6; border-color: rgba(139, 92, 246, 0.4); background: rgba(139, 92, 246, 0.08);" title="Tải Slide bài giảng P{active_paper_idx} (PDF)">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
            <line x1="8" y1="21" x2="16" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
          </svg>
          Slide Bài Giảng P{active_paper_idx} (PDF)
        </a>
        <a href="{get_pdf_filename(active_paper_idx)}" target="_blank" class="back-btn" style="color: var(--primary);" title="Mở file PDF gốc">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
          </svg>
          PDF Gốc
        </a>
      </div>

      <div class="top-bar-right">
        <button class="util-btn" onclick="toggleTheme()" title="Chuyển chế độ Sáng/Tối">🌓</button>
        <button class="util-btn" onclick="adjustFontSize(-1)" title="Giảm cỡ chữ">A-</button>
        <button class="util-btn" onclick="adjustFontSize(1)" title="Tăng cỡ chữ">A+</button>
        <button class="util-btn" onclick="window.print()" title="In hoặc Xuất PDF">🖨️</button>
      </div>
    </header>

    <!-- Article Container -->
    <main class="article-container">

      <!-- Paper Header -->
      <header class="paper-header">
        <div class="paper-badge">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
          </svg>
          {badge}
        </div>
        <h1 class="paper-title">{title}</h1>
        <div class="paper-title-en">{title_en}</div>

        <div class="paper-meta-grid">
          <div class="meta-item"><strong>Tác giả:</strong> {authors}</div>
          <div class="meta-item"><strong>Xuất bản:</strong> {journal}</div>
          <div class="meta-item"><strong>Định danh:</strong> {doi}</div>
          <div class="meta-item"><strong>Slide Bài Giảng:</strong> <a href="{get_slide_filename(active_paper_idx)}" target="_blank" style="color: #8b5cf6; font-weight: 700; text-decoration: underline;">Tải Slide P{active_paper_idx} ({get_slide_title(active_paper_idx)}) (PDF)</a></div>
        </div>
      </header>

      <!-- Main Body Content -->
      {content_html}

      <!-- Article Footer -->
      <footer class="article-footer">
        <div class="footer-nav-buttons">
          {get_footer_nav(active_paper_idx)}
        </div>
        <p>Khoa Kế toán & Kiểm toán — Trường Đại học Đông Á (UDA)</p>
        <p style="margin-top: 0.35rem; font-size: 0.8rem; color: var(--text-muted);">Tài liệu phục vụ giảng dạy và nghiên cứu học phần Trí Tuệ Nhân Tạo Trong Kế Toán & Kiểm Toán (2026)</p>
      </footer>

    </main>

  </div>

  <script>
    // Reading Progress Bar
    window.addEventListener('scroll', () => {{
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progress-bar').style.width = scrolled + '%';
    }});

    // Theme Switcher (Dark / Light)
    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme');
      const target = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', target);
      localStorage.setItem('doc_theme', target);
    }}

    // Initialize Theme
    const savedTheme = localStorage.getItem('doc_theme');
    if (savedTheme) {{
      document.documentElement.setAttribute('data-theme', savedTheme);
    }} else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {{
      document.documentElement.setAttribute('data-theme', 'dark');
    }}

    // Font Size Adjustment
    let currentFontSizeRem = 1.05;
    function adjustFontSize(delta) {{
      currentFontSizeRem = Math.max(0.85, Math.min(1.35, currentFontSizeRem + delta * 0.05));
      document.documentElement.style.setProperty('--content-font-size', currentFontSizeRem + 'rem');
    }}

    // Active Sidebar Link Spy
    const sections = document.querySelectorAll('section[id], div[id]');
    const navLinks = document.querySelectorAll('.sidebar-link');

    window.addEventListener('scroll', () => {{
      let currentSectionId = '';
      sections.forEach(sec => {{
        const top = sec.offsetTop - 120;
        if (window.pageYOffset >= top) {{
          currentSectionId = sec.getAttribute('id');
        }}
      }});

      navLinks.forEach(link => {{
        if (link.getAttribute('href') && link.getAttribute('href').startsWith('#')) {{
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + currentSectionId) {{
            link.classList.add('active');
          }}
        }}
      }});
    }});
  </script>

</body>

</html>
"""

def get_pdf_filename(idx):
    mapping = {
        1: "paper 1_Detecting Accounting Fraud in Publicly Traded U.S. Firms via a Machine Learning Approach.pdf",
        2: "paper 2_Financial Distress and Earnings Prediction using Deep Learning.pdf",
        3: "paper 3_FinBERT_A Large Language Model for Extracting Information from Financial Text.pdf",
        4: "paper 4_Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoder Networks.pdf"
    }
    return mapping.get(idx, "")

def get_slide_filename(idx):
    mapping = {
        1: "../P1_Học_Sâu_Trong_Kế_Toán.pdf",
        2: "../P2_Deep_Learning_in_Accounting_and_Finance.pdf",
        3: "../P3_FinBERT_in_Accounting.pdf",
        4: "../P4_Deep_Learning_in_Accounting_and_Auditing.pdf"
    }
    return mapping.get(idx, "")

def get_slide_title(idx):
    mapping = {
        1: "P1: Học Sâu Trong Kế Toán & Phát Hiện Gian Lận",
        2: "P2: Deep Learning in Accounting & Finance",
        3: "P3: FinBERT in Accounting",
        4: "P4: Deep Learning in Accounting & Auditing"
    }
    return mapping.get(idx, "")

def get_footer_nav(idx):
    navs = []
    if idx > 1:
        prev_map = {
            2: ("paper_1_Detecting_Accounting_Fraud_tiengviet.html", "← Bài 1: Gian Lận BCTC (JAR)"),
            3: ("paper_2_Financial_Distress_Prediction_tiengviet.html", "← Bài 2: Kiệt Quệ Tài Chính (Elsevier)"),
            4: ("paper_3_FinBERT_Large_Language_Model_tiengviet.html", "← Bài 3: FinBERT NLP (CAR)")
        }
        url, text = prev_map[idx]
        navs.append(f'<a href="{url}" class="footer-nav-btn">{text}</a>')
    else:
        navs.append('<a href="index.html" class="footer-nav-btn">← Thư Viện Bài Báo</a>')
        
    if idx < 4:
        next_map = {
            1: ("paper_2_Financial_Distress_Prediction_tiengviet.html", "Bài 2: Kiệt Quệ Tài Chính (Elsevier) →"),
            2: ("paper_3_FinBERT_Large_Language_Model_tiengviet.html", "Bài 3: FinBERT NLP (CAR) →"),
            3: ("paper_4_Deep_Autoencoder_Anomaly_Detection_tiengviet.html", "Bài 4: Autoencoder Sổ Cái (DFKI/PwC) →")
        }
        url, text = next_map[idx]
        navs.append(f'<a href="{url}" class="footer-nav-btn">{text}</a>')
    else:
        navs.append('<a href="index.html" class="footer-nav-btn">Quay về Trang Chủ Thư Viện →</a>')
        
    return "\n".join(navs)

print("Base helper loaded.")

