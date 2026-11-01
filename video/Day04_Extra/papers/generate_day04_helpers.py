# -*- coding: utf-8 -*-
"""
Builder script to generate Vietnamese translations (.md and .html)
and interactive web portals for Day 04 Extra Papers in Accounting & Auditing.
Topic: Generative AI, Large Language Models (LLMs), Prompt Engineering (CoT, ToT, Few-Shot, ReAct),
Double-Entry Bookkeeping Anomaly Detection (AuditCopilot), and Accounting Exam Performance.
"""

import os

BASE_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day04_Extra"
PAPERS_DIR = os.path.join(BASE_DIR, "papers")
SLIDES_DIR = os.path.join(BASE_DIR, "slides")
VIDEOS_DIR = os.path.join(BASE_DIR, "videos")

def get_html_template(title, title_en, authors, journal, doi, badge, content_html, active_paper_idx=1):
    active_1 = 'active' if active_paper_idx == 1 else ''
    active_2 = 'active' if active_paper_idx == 2 else ''
    return f"""<!DOCTYPE html>
<html lang="vi">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>{title} — Bản Dịch Học Thuật Toàn Văn Tiếng Việt (UDA)</title>
  <meta name="description" content="Bản dịch tiếng Việt học thuật toàn văn công trình nghiên cứu: {title_en} ({authors}). Tích hợp số liệu thực nghiệm, chuỗi tư duy CoT/ToT và phân tích nghiệp vụ kế toán kiểm toán chuyên sâu." />

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
      --accent-violet: #8b5cf6;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
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
      --code-bg: #090d16;
      --code-text: #e2e8f0;
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 10px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.5);
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
      line-height: 1.6;
      display: flex;
      min-height: 100vh;
      transition: background-color 0.3s ease, color 0.3s ease;
    }}

    /* Sidebar Navigation */
    .sidebar {{
      width: 320px;
      background: var(--bg-sidebar);
      color: var(--sidebar-text);
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      z-index: 100;
      overflow-y: auto;
      border-right: 1px solid rgba(255, 255, 255, 0.08);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .sidebar-header {{
      padding: 24px 20px 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}

    .sidebar-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: #fff;
    }}

    .brand-logo {{
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.1rem;
      color: #fff;
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }}

    .brand-info h1 {{
      font-size: 0.95rem;
      font-weight: 700;
      line-height: 1.2;
      color: #fff;
    }}

    .brand-info span {{
      font-size: 0.75rem;
      color: var(--sidebar-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .sidebar-nav {{
      padding: 16px 12px;
      flex: 1;
    }}

    .nav-group-title {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--sidebar-muted);
      padding: 8px 12px 6px;
      margin-top: 12px;
    }}

    .nav-item {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 12px;
      border-radius: var(--radius-sm);
      color: #cbd5e1;
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 500;
      transition: all 0.2s;
      margin-bottom: 2px;
    }}

    .nav-item:hover {{
      background: rgba(255, 255, 255, 0.06);
      color: #fff;
    }}

    .nav-item.active {{
      background: linear-gradient(135deg, rgba(59, 130, 246, 0.25) 0%, rgba(139, 92, 246, 0.25) 100%);
      color: #93c5fd;
      font-weight: 600;
      border-left: 3px solid #3b82f6;
    }}

    .nav-badge {{
      margin-left: auto;
      font-size: 0.7rem;
      padding: 2px 7px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.1);
      color: var(--sidebar-muted);
    }}

    .nav-item.active .nav-badge {{
      background: rgba(59, 130, 246, 0.4);
      color: #fff;
    }}

    /* Main Content Wrapper */
    .main-wrapper {{
      margin-left: 320px;
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
    }}

    /* Top Sticky Bar */
    .topbar {{
      height: 64px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 90;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 32px;
      box-shadow: var(--shadow-sm);
    }}

    .topbar-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .mobile-menu-btn {{
      display: none;
      background: none;
      border: none;
      font-size: 1.4rem;
      color: var(--text-main);
      cursor: pointer;
      padding: 6px;
    }}

    .breadcrumb {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .breadcrumb a {{
      color: var(--primary);
      text-decoration: none;
      font-weight: 500;
    }}

    .topbar-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s;
      border: 1px solid transparent;
    }}

    .btn-secondary {{
      background: var(--bg-body);
      border-color: var(--border-color);
      color: var(--text-main);
    }}

    .btn-secondary:hover {{
      background: var(--primary-light);
      border-color: var(--primary-border);
      color: var(--primary);
    }}

    .btn-primary {{
      background: var(--primary);
      color: #fff;
    }}

    .btn-primary:hover {{
      opacity: 0.9;
      transform: translateY(-1px);
    }}

    .theme-toggle {{
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.1rem;
      transition: all 0.2s;
    }}

    .theme-toggle:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}

    /* Article Container */
    .article-container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 40px 32px 80px;
      width: 100%;
    }}

    .paper-header {{
      margin-bottom: 36px;
      padding-bottom: 28px;
      border-bottom: 1px solid var(--border-color);
    }}

    .paper-badge {{
      display: inline-block;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%);
      color: var(--primary);
      border: 1px solid var(--primary-border);
      margin-bottom: 16px;
    }}

    .paper-title-vi {{
      font-family: 'Outfit', sans-serif;
      font-size: 2.1rem;
      font-weight: 800;
      line-height: 1.25;
      color: var(--text-main);
      margin-bottom: 12px;
    }}

    .paper-title-en {{
      font-size: 1.1rem;
      font-style: italic;
      color: var(--text-muted);
      margin-bottom: 20px;
      line-height: 1.4;
    }}

    .paper-meta {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 12px;
      font-size: 0.85rem;
      box-shadow: var(--shadow-sm);
    }}

    .meta-item {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .meta-label {{
      font-weight: 700;
      color: var(--text-muted);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .meta-value {{
      color: var(--text-main);
      font-weight: 500;
    }}

    /* Academic Prose Styling */
    .paper-content {{
      font-family: 'Merriweather', Georgia, serif;
      font-size: var(--content-font-size);
      line-height: var(--line-height);
      color: var(--text-main);
    }}

    .paper-content p {{
      margin-bottom: 1.5rem;
      text-align: justify;
    }}

    .paper-content h2 {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.55rem;
      font-weight: 700;
      color: var(--text-main);
      margin: 44px 0 18px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--primary-light);
      position: relative;
    }}

    .paper-content h2::after {{
      content: '';
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 60px;
      height: 2px;
      background: var(--primary);
    }}

    .paper-content h3 {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-main);
      margin: 30px 0 14px;
    }}

    .paper-content h4 {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary);
      margin: 22px 0 10px;
    }}

    .paper-content ul, .paper-content ol {{
      margin: 0 0 1.5rem 1.8rem;
    }}

    .paper-content li {{
      margin-bottom: 0.5rem;
    }}

    .paper-content blockquote {{
      margin: 24px 0;
      padding: 18px 24px;
      background: var(--bg-surface);
      border-left: 4px solid var(--primary);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      font-style: italic;
      box-shadow: var(--shadow-sm);
    }}

    .paper-content table {{
      width: 100%;
      border-collapse: collapse;
      margin: 28px 0;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.88rem;
      background: var(--bg-surface);
      border-radius: var(--radius-sm);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }}

    .paper-content th {{
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 700;
      text-align: left;
      padding: 12px 16px;
      border-bottom: 2px solid var(--primary-border);
    }}

    .paper-content td {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-color);
      vertical-align: top;
    }}

    .paper-content tr:hover td {{
      background: rgba(59, 130, 246, 0.03);
    }}

    .callout {{
      margin: 24px 0;
      padding: 18px 22px;
      border-radius: var(--radius-md);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.95rem;
      display: flex;
      gap: 14px;
      box-shadow: var(--shadow-sm);
    }}

    .callout-info {{
      background: rgba(59, 130, 246, 0.08);
      border-left: 4px solid var(--primary);
      color: var(--text-main);
    }}

    .callout-success {{
      background: rgba(16, 185, 129, 0.08);
      border-left: 4px solid var(--accent-emerald);
      color: var(--text-main);
    }}

    .callout-warning {{
      background: rgba(245, 158, 11, 0.08);
      border-left: 4px solid var(--accent-amber);
      color: var(--text-main);
    }}

    .callout-danger {{
      background: rgba(244, 63, 94, 0.08);
      border-left: 4px solid var(--accent-rose);
      color: var(--text-main);
    }}

    .callout-icon {{
      font-size: 1.3rem;
      line-height: 1;
    }}

    .figure-box {{
      margin: 32px 0;
      padding: 16px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      text-align: center;
      box-shadow: var(--shadow-sm);
    }}

    .figure-box img {{
      max-width: 100%;
      height: auto;
      border-radius: var(--radius-sm);
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}

    .figure-caption {{
      margin-top: 12px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.85rem;
      color: var(--text-muted);
      font-style: italic;
    }}

    /* Footer Navigation */
    .article-footer {{
      margin-top: 50px;
      padding-top: 30px;
      border-top: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    /* Responsive */
    @media (max-width: 1024px) {{
      .sidebar {{
        transform: translateX(-100%);
      }}
      .sidebar.open {{
        transform: translateX(0);
      }}
      .main-wrapper {{
        margin-left: 0;
      }}
      .mobile-menu-btn {{
        display: block;
      }}
    }}
  </style>
</head>

<body>
  <!-- Sidebar -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <a href="../index.html" class="sidebar-brand">
        <div class="brand-logo">UDA</div>
        <div class="brand-info">
          <h1>Đại Học Đông Á</h1>
          <span>Day 04 Extra • Khoa Học LLM</span>
        </div>
      </a>
    </div>

    <nav class="sidebar-nav">
      <div class="nav-group-title">Cổng Chuyên Đề</div>
      <a href="../index.html" class="nav-item">
        <span>🏠</span>
        <span>Cổng Tổng Hợp Day 04 Extra</span>
      </a>
      <a href="index.html" class="nav-item">
        <span>📚</span>
        <span>Thư Viện Bài Báo Khoa Học</span>
      </a>

      <div class="nav-group-title">2 Bài Báo Khoa Học (2024–2025)</div>
      <a href="paper_1_Is_It_All_Hype_ChatGPT_Accounting_tiengviet.html" class="nav-item {active_1}">
        <span>📄</span>
        <span>Bài 1: Is It All Hype? (Eulerich 2024)</span>
        <span class="nav-badge">RAST '24</span>
      </a>
      <a href="paper_2_AuditCopilot_LLM_Fraud_Detection_tiengviet.html" class="nav-item {active_2}">
        <span>📄</span>
        <span>Bài 2: AuditCopilot (DFKI 2025)</span>
        <span class="nav-badge">DFKI '25</span>
      </a>

      <div class="nav-group-title">Bộ 3 Slide Bài Giảng Trực Quan</div>
      <a href="../index.html#slide-viewer-section" class="nav-item">
        <span>📊</span>
        <span>Slide P1: Lý Thuyết Generative AI</span>
        <span class="nav-badge">15 trang</span>
      </a>
      <a href="../index.html#slide-viewer-section" class="nav-item">
        <span>📊</span>
        <span>Slide P2: Is It All Hype? (Eulerich)</span>
        <span class="nav-badge">15 trang</span>
      </a>
      <a href="../index.html#slide-viewer-section" class="nav-item">
        <span>📊</span>
        <span>Slide P3: AuditCopilot (DFKI)</span>
        <span class="nav-badge">15 trang</span>
      </a>

      <div class="nav-group-title">Video & Kịch Bản Giảng Dạy</div>
      <a href="../videos/P1_lý thuyết_Generative_AI_trong_Kế_toán_và_Kiểm_toán/index.html" class="nav-item">
        <span>🎬</span>
        <span>Trình Phát Video P1 (Lý Thuyết)</span>
      </a>
      <a href="../videos/P2_is it all hype_ChatGPT_in_Accounting/index.html" class="nav-item">
        <span>🎬</span>
        <span>Trình Phát Video P2 (Is It All Hype)</span>
      </a>
      <a href="../videos/P3_AuditCopilot_for_Audit_Fraud_Detection/index.html" class="nav-item">
        <span>🎬</span>
        <span>Trình Phát Video P3 (AuditCopilot)</span>
      </a>
    </nav>
  </aside>

  <!-- Main Content -->
  <div class="main-wrapper">
    <header class="topbar">
      <div class="topbar-left">
        <button class="mobile-menu-btn" id="mobileMenuBtn">☰</button>
        <div class="breadcrumb">
          <a href="../../../index.html">Trang chủ</a>
          <span>›</span>
          <a href="../index.html">Day 04 Extra</a>
          <span>›</span>
          <a href="index.html">Bài Báo Khoa Học</a>
          <span>›</span>
          <span>Bài {active_paper_idx}</span>
        </div>
      </div>

      <div class="topbar-actions">
        <button class="theme-toggle" id="themeToggle" title="Đổi giao diện Sáng / Tối">🌙</button>
        <a href="../index.html" class="btn btn-secondary">🏠 Cổng Day 04</a>
        <a href="index.html" class="btn btn-primary">📚 Thư Viện Bài Báo</a>
      </div>
    </header>

    <article class="article-container">
      <div class="paper-header">
        <span class="paper-badge">{badge}</span>
        <h1 class="paper-title-vi">{title}</h1>
        <div class="paper-title-en">{title_en}</div>
        <div class="paper-meta">
          <div class="meta-item">
            <span class="meta-label">Nhóm Tác Giả:</span>
            <span class="meta-value">{authors}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">Công Bố Tại:</span>
            <span class="meta-value">{journal}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">Định Danh / Bản Quyền:</span>
            <span class="meta-value">{doi}</span>
          </div>
        </div>
      </div>

      <div class="paper-content">
        {content_html}
      </div>

      <div class="article-footer">
        <a href="index.html" class="btn btn-secondary">← Về Danh Mục Bài Báo</a>
        <a href="../index.html#slide-viewer-section" class="btn btn-primary">Xem Slide Bài Giảng Liên Quan →</a>
      </div>
    </article>
  </div>

  <script>
    // Theme toggle
    const themeToggle = document.getElementById('themeToggle');
    const root = document.documentElement;
    let isDark = localStorage.getItem('day04_theme') === 'dark';
    
    function updateTheme() {{
      if (isDark) {{
        root.setAttribute('data-theme', 'dark');
        themeToggle.textContent = '☀️';
      }} else {{
        root.removeAttribute('data-theme');
        themeToggle.textContent = '🌙';
      }}
      localStorage.setItem('day04_theme', isDark ? 'dark' : 'light');
    }}
    updateTheme();

    themeToggle.addEventListener('click', () => {{
      isDark = !isDark;
      updateTheme();
    }});

    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const sidebar = document.getElementById('sidebar');
    mobileMenuBtn.addEventListener('click', () => {{
      sidebar.classList.toggle('open');
    }});
  </script>
</body>
</html>"""

