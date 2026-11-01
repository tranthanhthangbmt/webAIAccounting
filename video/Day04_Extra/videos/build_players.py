# -*- coding: utf-8 -*-
"""
Builder for Day 04 Extra Video Players:
P1: Lý thuyết Generative AI trong Kế toán & Kiểm toán
P2: Is it all hype? ChatGPT in Accounting (Eulerich 2024)
P3: AuditCopilot for Audit Fraud Detection (DFKI 2025)
"""

import os
import re
import json

BASE_DIR = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day04_Extra"
VIDEOS_DIR = os.path.join(BASE_DIR, "videos")

def parse_script(script_path):
    if not os.path.exists(script_path):
        return {}
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()
    slides = {}
    pattern = r"Slide\s+(\d+):\s*(.*?)(?=(?:Slide\s+\d+:|$))"
    matches = re.findall(pattern, content, re.DOTALL)
    for num, text in matches:
        slides[int(num)] = text.strip()
    return slides

def build_player(part_folder, part_title, part_code):
    folder_path = os.path.join(VIDEOS_DIR, part_folder)
    script_path = os.path.join(folder_path, "script.txt")
    scripts_dict = parse_script(script_path)

    # Convert scripts dict to formatted JSON string
    scripts_json = json.dumps(scripts_dict, ensure_ascii=False)

    player_html = f"""<!DOCTYPE html>
<html lang="vi">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport"
    content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>{part_title} — Trình Phát Bài Giảng UDA</title>
  <style>
    :root {{
      --bar-bg: rgba(11, 15, 25, 0.85);
      --bar-fg: #ffffff;
      --accent: #3b82f6;
      --ok: #10b981;
      --border-subtle: rgba(255, 255, 255, 0.12);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      height: 100%;
      background: #000;
      overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}

    .player-container {{
      background: #0b0f19;
      width: 100vw;
      height: 100dvh;
      display: flex;
      flex-direction: column;
      position: relative;
    }}

    /* Top Bar */
    .top-bar {{
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 52px;
      background: linear-gradient(180deg, rgba(0,0,0,0.8) 0%, transparent 100%);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      z-index: 20;
      color: #fff;
    }}

    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-subtle);
      color: #fff;
      padding: 6px 12px;
      border-radius: 6px;
      text-decoration: none;
      font-size: 0.82rem;
      font-weight: 600;
      transition: all 0.2s;
    }}

    .back-btn:hover {{
      background: var(--accent);
    }}

    .part-title-tag {{
      font-size: 0.88rem;
      font-weight: 700;
      color: #e2e8f0;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 60%;
    }}

    /* Slide Viewer */
    .slide-viewer {{
      flex: 1;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: auto;
      background: #000;
    }}

    .slide-img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      box-shadow: 0 0 30px rgba(0,0,0,0.8);
      transition: opacity 0.2s;
    }}

    /* Bottom Control Bar */
    .controls-bar {{
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 12px 20px;
      background: linear-gradient(0deg, rgba(0,0,0,0.85) 0%, transparent 100%);
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 20;
      color: #fff;
    }}

    .ctrl-group-left, .ctrl-group-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .ctrl-group-center {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .ctrl-btn {{
      color: #fff;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid var(--border-subtle);
      border-radius: 50%;
      width: 42px;
      height: 42px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      cursor: pointer;
      transition: all 0.2s;
      backdrop-filter: blur(6px);
    }}

    .ctrl-btn:hover {{
      background: rgba(255, 255, 255, 0.25);
      transform: scale(1.05);
    }}

    .ctrl-btn:disabled {{
      opacity: 0.3;
      cursor: not-allowed;
      transform: none;
    }}

    .play-btn {{
      background: var(--ok);
      border-color: transparent;
      width: 48px;
      height: 48px;
      font-size: 1.3rem;
    }}

    .play-btn:hover {{
      background: #059669;
    }}

    .slide-counter {{
      font-weight: 700;
      font-size: 0.95rem;
      min-width: 70px;
      text-align: center;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
    }}

    .btn-pill {{
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid var(--border-subtle);
      color: #fff;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-pill:hover {{
      background: var(--accent);
    }}

    /* Transcript Drawer */
    .transcript-drawer {{
      position: absolute;
      bottom: 74px;
      right: 20px;
      width: min(520px, calc(100vw - 40px));
      max-height: 55vh;
      background: rgba(18, 26, 44, 0.95);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.6);
      backdrop-filter: blur(16px);
      z-index: 30;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transform: translateY(20px);
      opacity: 0;
      visibility: hidden;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .transcript-drawer.open {{
      transform: translateY(0);
      opacity: 1;
      visibility: visible;
    }}

    .drawer-header {{
      padding: 12px 16px;
      background: rgba(0,0,0,0.3);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-weight: 700;
      font-size: 0.88rem;
      color: #93c5fd;
    }}

    .drawer-close {{
      background: none;
      border: none;
      color: #94a3b8;
      font-size: 1.2rem;
      cursor: pointer;
    }}

    .drawer-body {{
      padding: 16px;
      overflow-y: auto;
      font-size: 0.92rem;
      line-height: 1.65;
      color: #cbd5e1;
      white-space: pre-wrap;
    }}

    .drawer-body strong {{
      color: #60a5fa;
    }}

    /* Loading Spinner */
    .spinner-overlay {{
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 25;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.2s;
    }}

    .spinner-overlay.active {{
      opacity: 1;
      visibility: visible;
    }}

    .spinner {{
      width: 40px;
      height: 40px;
      border: 3px solid rgba(255,255,255,0.2);
      border-top-color: var(--accent);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }}

    @keyframes spin {{
      to {{ transform: rotate(360deg); }}
    }}
  </style>
</head>

<body>
  <div class="player-container" id="playerContainer">
    <!-- Top Bar -->
    <div class="top-bar">
      <a href="../../index.html" class="back-btn">
        <span>←</span>
        <span>Về Cổng Day 04</span>
      </a>
      <div class="part-title-tag">{part_code}: {part_title}</div>
      <button class="btn-pill" id="toggleTranscriptBtn">
        <span>📝</span>
        <span>Kịch Bản Lời Thoại</span>
      </button>
    </div>

    <!-- Slide Viewer -->
    <div class="slide-viewer" id="slideViewer">
      <img id="slideImg" class="slide-img" src="images/slide-1.png" alt="Slide" />
      <div class="spinner-overlay" id="spinner">
        <div class="spinner"></div>
      </div>
    </div>

    <!-- Transcript Drawer -->
    <div class="transcript-drawer" id="transcriptDrawer">
      <div class="drawer-header">
        <span id="drawerTitle">Kịch bản Lời thoại Slide 1</span>
        <button class="drawer-close" id="drawerCloseBtn">✕</button>
      </div>
      <div class="drawer-body" id="drawerBody">
        Đang tải kịch bản...
      </div>
    </div>

    <!-- Controls Bar -->
    <div class="controls-bar">
      <div class="ctrl-group-left">
        <button class="btn-pill" id="pdfLinkBtn" onclick="window.open('../../slides/{part_folder}.pdf', '_blank')">
          <span>📄</span>
          <span>Xem PDF</span>
        </button>
      </div>

      <div class="ctrl-group-center">
        <button class="ctrl-btn" id="prevBtn" title="Slide Trước">❮</button>
        <button class="ctrl-btn play-btn" id="playBtn" title="Tự động phát">▶</button>
        <button class="ctrl-btn" id="nextBtn" title="Slide Tiếp">❯</button>
        <div class="slide-counter" id="slideCounter">1 / 15</div>
      </div>

      <div class="ctrl-group-right">
        <button class="ctrl-btn" id="fullscreenBtn" title="Toàn Màn Hình">⛶</button>
      </div>
    </div>
  </div>

  <audio id="slideAudio" preload="auto"></audio>

  <script>
    const TOTAL_SLIDES = 15;
    const scriptsData = {scripts_json};

    let currentIndex = 1;
    let isPlaying = false;
    let autoPlayTimer = null;

    const slideImg = document.getElementById('slideImg');
    const slideAudio = document.getElementById('slideAudio');
    const slideCounter = document.getElementById('slideCounter');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const playBtn = document.getElementById('playBtn');
    const spinner = document.getElementById('spinner');
    const transcriptDrawer = document.getElementById('transcriptDrawer');
    const drawerTitle = document.getElementById('drawerTitle');
    const drawerBody = document.getElementById('drawerBody');
    const toggleTranscriptBtn = document.getElementById('toggleTranscriptBtn');
    const drawerCloseBtn = document.getElementById('drawerCloseBtn');
    const fullscreenBtn = document.getElementById('fullscreenBtn');

    function updateTranscript(index) {{
      drawerTitle.textContent = `Kịch bản Lời thoại — Slide ${{index}} / ${{TOTAL_SLIDES}}`;
      const text = scriptsData[index] || "Chưa có kịch bản cho slide này.";
      // Format Người 1 and Người 2 bold
      const formatted = text
        .replace(/(Người 1:)/g, "<strong>$1</strong>")
        .replace(/(Người 2:)/g, "<strong>$2</strong>");
      drawerBody.innerHTML = formatted;
    }}

    function showSlide(index) {{
      if (index < 1) index = 1;
      if (index > TOTAL_SLIDES) index = TOTAL_SLIDES;
      currentIndex = index;

      slideCounter.textContent = `${{index}} / ${{TOTAL_SLIDES}}`;
      prevBtn.disabled = (index === 1);
      nextBtn.disabled = (index === TOTAL_SLIDES);

      // Show spinner briefly
      spinner.classList.add('active');

      // Update image
      const newImg = new Image();
      newImg.src = `images/slide-${{index}}.png`;
      newImg.onload = () => {{
        slideImg.src = newImg.src;
        spinner.classList.remove('active');
      }};
      newImg.onerror = () => {{
        spinner.classList.remove('active');
      }};

      // Update transcript
      updateTranscript(index);

      // Try audio
      slideAudio.pause();
      clearTimeout(autoPlayTimer);

      const audioSrc = `audio/slide_${{index}}.mp3`;
      slideAudio.src = audioSrc;

      slideAudio.oncanplaythrough = () => {{
        if (isPlaying) slideAudio.play();
      }};

      slideAudio.onerror = () => {{
        // Audio not found, use fallback timer if playing
        if (isPlaying) {{
          autoPlayTimer = setTimeout(() => {{
            if (currentIndex < TOTAL_SLIDES) {{
              showSlide(currentIndex + 1);
            }} else {{
              stopPlayback();
            }}
          }}, 12000); // 12 seconds per slide fallback
        }}
      }};

      slideAudio.onended = () => {{
        if (isPlaying) {{
          if (currentIndex < TOTAL_SLIDES) {{
            showSlide(currentIndex + 1);
          }} else {{
            stopPlayback();
          }}
        }}
      }};
    }}

    function startPlayback() {{
      isPlaying = true;
      playBtn.textContent = '⏸';
      playBtn.style.background = '#eab308';
      slideAudio.play().catch(() => {{
        // Autoplay fallback timer
        clearTimeout(autoPlayTimer);
        autoPlayTimer = setTimeout(() => {{
          if (currentIndex < TOTAL_SLIDES) {{
            showSlide(currentIndex + 1);
          }} else {{
            stopPlayback();
          }}
        }}, 12000);
      }});
    }}

    function stopPlayback() {{
      isPlaying = false;
      playBtn.textContent = '▶';
      playBtn.style.background = 'var(--ok)';
      slideAudio.pause();
      clearTimeout(autoPlayTimer);
    }}

    playBtn.addEventListener('click', () => {{
      if (isPlaying) stopPlayback();
      else startPlayback();
    }});

    prevBtn.addEventListener('click', () => {{
      if (currentIndex > 1) showSlide(currentIndex - 1);
    }});

    nextBtn.addEventListener('click', () => {{
      if (currentIndex < TOTAL_SLIDES) showSlide(currentIndex + 1);
    }});

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowLeft') {{
        if (currentIndex > 1) showSlide(currentIndex - 1);
      }} else if (e.key === 'ArrowRight') {{
        if (currentIndex < TOTAL_SLIDES) showSlide(currentIndex + 1);
      }} else if (e.key === ' ') {{
        e.preventDefault();
        playBtn.click();
      }}
    }});

    // Transcript toggle
    toggleTranscriptBtn.addEventListener('click', () => {{
      transcriptDrawer.classList.toggle('open');
    }});

    drawerCloseBtn.addEventListener('click', () => {{
      transcriptDrawer.classList.remove('open');
    }});

    // Fullscreen toggle
    fullscreenBtn.addEventListener('click', () => {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(() => {{}});
      }} else {{
        document.exitFullscreen().catch(() => {{}});
      }}
    }});

    // Initial load
    showSlide(1);
  </script>
</body>
</html>"""

    out_file = os.path.join(folder_path, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(player_html)
    print(f"Generated player for {part_code}: {out_file} ({len(player_html)} bytes)")

def build_all():
    decks = [
        ("P1_lý thuyết_Generative_AI_trong_Kế_toán_và_Kiểm_toán", "Lý thuyết Generative AI trong Kế toán & Kiểm toán", "P1"),
        ("P2_is it all hype_ChatGPT_in_Accounting", "Is it all hype? ChatGPT in Accounting (Eulerich 2024)", "P2"),
        ("P3_AuditCopilot_for_Audit_Fraud_Detection", "AuditCopilot for Audit Fraud Detection (DFKI 2025)", "P3")
    ]
    for folder, title, code in decks:
        build_player(folder, title, code)

if __name__ == "__main__":
    build_all()

