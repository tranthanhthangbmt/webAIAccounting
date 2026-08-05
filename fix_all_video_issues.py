import os
import glob
import re
import time

base_dir = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting"
video_files = glob.glob(os.path.join(base_dir, "video", "Day*", "index.html"))
practice_files = glob.glob(os.path.join(base_dir, "videoPractice", "Chapter*", "index.html"))

all_html_files = video_files + practice_files

for file_path in all_html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Add isInitialLoad if not present
    if "let isInitialLoad = true;" not in content:
        content = content.replace("const AUD_EXT = '.mp3';", "const AUD_EXT = '.mp3';\n    let isInitialLoad = true;")
        modified = True

    # 2. Modify showSlide logic if old logic exists
    old_logic_audio = """        // 4. Phát audio & Auto-scroll
        try {
          await slideAudio.play();
          startAutoScrollIfNeeded();
        } catch (err) {"""
    
    new_logic_audio = """        // 4. Phát audio & Auto-scroll
        try {
          if (isInitialLoad) {
            isInitialLoad = false;
            playPauseBtn.innerHTML = '▶️';
          } else {
            await slideAudio.play();
            startAutoScrollIfNeeded();
          }
        } catch (err) {"""
    
    if old_logic_audio in content:
        content = content.replace(old_logic_audio, new_logic_audio)
        modified = True

    # 3. Handle visibility changer
    old_visibility1 = """    /* ================= INIT ================= */"""
    old_visibility2 = """    /* ================= VISIBILITY CHANGER (Ngừng phát khi chuyển tab) ================= */"""

    visibility_script = """    /* ================= VISIBILITY CHANGER (Ngừng phát khi chuyển tab) ================= */
    function checkVisibility() {
        try {
            if (window.parent && window.parent.document) {
                const iframes = window.parent.document.querySelectorAll('iframe');
                let myIframe = null;
                for (let i = 0; i < iframes.length; i++) {
                    if (iframes[i].contentWindow === window) {
                        myIframe = iframes[i];
                        break;
                    }
                }
                if (myIframe) {
                    let el = myIframe;
                    while (el && el !== window.parent.document.body) {
                        const style = window.parent.getComputedStyle(el);
                        if (style.display === 'none' || style.opacity === '0' || style.visibility === 'hidden') {
                            return false;
                        }
                        el = el.parentElement;
                    }
                }
            }
        } catch (e) {}
        return true;
    }

    setInterval(() => {
      if (!checkVisibility()) {
        if (typeof slideAudio !== 'undefined' && slideAudio && !slideAudio.paused) {
            slideAudio.pause();
            playPauseBtn.innerHTML = '▶️';
            if (typeof scrollAnimationId !== 'undefined') cancelAnimationFrame(scrollAnimationId);
        }
        if (typeof videoElement !== 'undefined' && videoElement && !videoElement.paused) {
            videoElement.pause();
        }
      }
    }, 500);

    /* ================= INIT ================= */"""

    if "function checkVisibility()" not in content:
        if old_visibility2 in content:
            # Replace the old ResizeObserver or first version of interval
            content = re.sub(r'    /\* ================= VISIBILITY CHANGER.*?/\* ================= INIT ================= \*/', visibility_script, content, flags=re.DOTALL)
            modified = True
        elif old_visibility1 in content:
            content = content.replace(old_visibility1, visibility_script)
            modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {file_path}")

# Now update docs/*.md to add a cache-buster to iframe URLs
timestamp = str(int(time.time()))

md_files = glob.glob(os.path.join(base_dir, "docs", "*.md"))
for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    def replace_src(match):
        url = match.group(1)
        if '?' in url:
            url = re.sub(r'\?v=\d+', f'?v={timestamp}', url)
            if '?v=' not in url:
                url = url + f"&v={timestamp}"
        else:
            url = f"{url}?v={timestamp}"
        return f'src="{url}"'
        
    new_md_content = re.sub(r'src="([^"]+index\.html[^"]*)"', replace_src, md_content)
    
    if new_md_content != md_content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(new_md_content)
        print(f"Cache-busted: {md_file}")

print("Done fixing autoplay and cache.")
