import re

filepath = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the old plugin definition at the bottom
pattern_old_plugin = r'// Docsify plugin to sync player with current chapter and optimize PDF for mobile.*?\n\s*\}\);\s*\}\s*\);\s*'
content = re.sub(pattern_old_plugin, '', content, flags=re.DOTALL)

# 2. Define the new plugin right after window.$docsify = { ... }
plugin_code = """
    window.$docsify.plugins = [
      function (hook, vm) {
        hook.doneEach(function () {
          // 1. Mobile PDF Viewer Support with Google Docs Viewer
          const isMobile = window.innerWidth <= 768 || /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
          if (isMobile) {
            // Dùng setTimeout để đảm bảo docsify-tabs đã render xong thẻ object
            setTimeout(() => {
              document.querySelectorAll('.pdf-container, object[type="application/pdf"]').forEach(function(obj) {
                let src = obj.getAttribute('data') || obj.getAttribute('src');
                if (src && src.includes('.pdf')) {
                  src = src.split('#')[0]; // Remove hash
                  let absoluteUrl = src;
                  if (!src.startsWith('http')) {
                    let baseUrl = window.location.origin + window.location.pathname;
                    baseUrl = baseUrl.replace(/index\\.html$/, '');
                    if (!baseUrl.endsWith('/')) baseUrl += '/';
                    absoluteUrl = baseUrl + src;
                  }
                  
                  // Create wrapper
                  const wrapper = document.createElement('div');
                  wrapper.style.width = '100vw';
                  wrapper.style.marginLeft = '-5px'; // offset docsify padding
                  
                  // Create Fullscreen Button
                  const btn = document.createElement('a');
                  btn.href = src;
                  btn.target = '_blank';
                  btn.innerHTML = '📖 Mở Đọc Toàn Màn Hình';
                  btn.style.display = 'block';
                  btn.style.textAlign = 'center';
                  btn.style.background = 'var(--theme-color, #1a73e8)';
                  btn.style.color = '#fff';
                  btn.style.padding = '12px';
                  btn.style.borderRadius = '8px';
                  btn.style.marginBottom = '15px';
                  btn.style.textDecoration = 'none';
                  btn.style.fontWeight = 'bold';
                  btn.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
                  wrapper.appendChild(btn);

                  // Create Google Docs Viewer Iframe
                  let viewerUrl = 'https://docs.google.com/viewer?url=' + encodeURIComponent(absoluteUrl) + '&embedded=true';
                  let newIframe = document.createElement('iframe');
                  newIframe.src = viewerUrl;
                  newIframe.className = obj.className;
                  newIframe.style.width = '100%';
                  newIframe.style.height = '85vh';
                  newIframe.style.border = 'none';
                  newIframe.style.borderRadius = '10px';
                  wrapper.appendChild(newIframe);
                  
                  obj.parentNode.replaceChild(wrapper, obj);
                }
              });
            }, 300); // 300ms delay to let tabs render
          }

          // 2. Sync APlayer with Chapter
          let hash = window.location.hash;
          if (hash.includes('buoi_')) {
            let match = hash.match(/buoi_(\\d+)/);
            if (match && match[1] && typeof dayToIndex !== 'undefined' && typeof ap !== 'undefined') {
              let dayNum = parseInt(match[1]);
              let chapterIndex = dayToIndex[dayNum];
              if (chapterIndex !== undefined) {
                if (ap.list.index !== chapterIndex) {
                  ap.list.switch(chapterIndex);
                }
              }
            }
          }
        });
      }
    ];
"""

# We insert the plugin code just before the first </script> tag
# Since window.$docsify is defined in the first script tag.
first_script_end = content.find("</script>")
if first_script_end != -1:
    content = content[:first_script_end] + plugin_code + "\n  " + content[first_script_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
