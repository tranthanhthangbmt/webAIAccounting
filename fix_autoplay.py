import os
import glob
import re

base_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video"

html_files = glob.glob(os.path.join(base_dir, "Day*", "index.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "let isInitialLoad = true;" in content:
        print(f"Already fixed: {file_path}")
        continue
    
    # 1. Add isInitialLoad
    content = content.replace("const AUD_EXT = '.mp3';", "const AUD_EXT = '.mp3';\n    let isInitialLoad = true;")
    
    # 2. Modify autoplay logic
    old_logic = """        // 4. Phát audio & Auto-scroll
        try {
          await slideAudio.play();
          startAutoScrollIfNeeded();
        } catch (err) {"""
    
    new_logic = """        // 4. Phát audio & Auto-scroll
        try {
          if (isInitialLoad) {
            isInitialLoad = false;
            playPauseBtn.innerHTML = '▶️';
          } else {
            await slideAudio.play();
            startAutoScrollIfNeeded();
          }
        } catch (err) {"""
    
    content = content.replace(old_logic, new_logic)
    
    # 3. Add ResizeObserver before window.addEventListener('load'
    old_init = "    /* ================= INIT ================= */"
    
    new_init = """    /* ================= VISIBILITY CHANGER (Ngừng phát khi chuyển tab) ================= */
    const ro = new ResizeObserver(entries => {
      for (let entry of entries) {
        if (entry.contentRect.width === 0 || entry.contentRect.height === 0) {
          if (typeof slideAudio !== 'undefined' && slideAudio && !slideAudio.paused) slideAudio.pause();
          if (typeof videoElement !== 'undefined' && videoElement && !videoElement.paused) videoElement.pause();
        }
      }
    });
    ro.observe(document.body);

    /* ================= INIT ================= */"""
    
    content = content.replace(old_init, new_init)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed: {file_path}")
