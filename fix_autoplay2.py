import os
import glob

base_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video"

html_files = glob.glob(os.path.join(base_dir, "Day*", "index.html"))

old_script = """    /* ================= VISIBILITY CHANGER (Ngừng phát khi chuyển tab) ================= */
    const ro = new ResizeObserver(entries => {
      for (let entry of entries) {
        if (entry.contentRect.width === 0 || entry.contentRect.height === 0) {
          if (typeof slideAudio !== 'undefined' && slideAudio && !slideAudio.paused) slideAudio.pause();
          if (typeof videoElement !== 'undefined' && videoElement && !videoElement.paused) videoElement.pause();
        }
      }
    });
    ro.observe(document.body);"""

new_script = """    /* ================= VISIBILITY CHANGER (Ngừng phát khi chuyển tab) ================= */
    function checkVisibility() {
      if (window.innerWidth === 0 || window.innerHeight === 0) return false;
      try {
        if (window.frameElement) {
          let el = window.frameElement;
          while (el && el !== window.parent.document.body) {
             const style = window.parent.getComputedStyle(el);
             if (style.display === 'none' || style.opacity === '0' || style.visibility === 'hidden') {
                 return false;
             }
             el = el.parentElement;
          }
        }
      } catch (e) {
        // Bỏ qua lỗi cross-origin
      }
      return true;
    }

    setInterval(() => {
      if (!checkVisibility()) {
        if (typeof slideAudio !== 'undefined' && slideAudio && !slideAudio.paused) {
            slideAudio.pause();
            playPauseBtn.innerHTML = '▶️';
            cancelAnimationFrame(scrollAnimationId);
        }
        if (typeof videoElement !== 'undefined' && videoElement && !videoElement.paused) {
            videoElement.pause();
        }
      }
    }, 500);"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_script in content:
        content = content.replace(old_script, new_script)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced in: {file_path}")
    elif new_script in content:
        print(f"Already updated: {file_path}")
    else:
        print(f"Old script NOT FOUND in: {file_path}")
