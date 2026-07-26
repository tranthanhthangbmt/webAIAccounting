import os
import glob
import re

def inject_audio_player():
    audio_files = glob.glob('audio/AIAcc_Day_*.m4a')
    audio_map = {}
    for af in audio_files:
        # Extract day number
        match = re.search(r'AIAcc_Day_(\d+)_', af)
        if match:
            day = match.group(1)
            audio_map[day] = af.replace('\\', '/')

    md_files = glob.glob('docs/buoi_*.md')
    for f in md_files:
        match = re.search(r'buoi_(\d+)\.md', f)
        if not match: continue
        day = match.group(1)

        if day not in audio_map:
            print(f'No audio found for Day {day}, skipping {f}')
            continue
            
        audio_path = audio_map[day]

        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()

        if '🎧 Nghe Bài Giảng' in content:
            print(f'{f} already has audio player, skipping.')
            continue

        audio_html = f'''
<div style="margin: 20px 0; padding: 15px; background-color: #f8f9fa; border-left: 4px solid #0056b3; border-radius: 4px;">
    <h4 style="margin-top: 0;">🎧 Nghe Bài Giảng (Audio)</h4>
    <audio controls style="width: 100%;">
        <source src="{audio_path}" type="audio/mp4">
        Trình duyệt của bạn không hỗ trợ thẻ audio.
    </audio>
</div>
'''
        # Inject right after the first H1 header
        content = re.sub(
            r'^(# Buổi \d+:.*?)\n',
            r'\1\n' + audio_html,
            content,
            count=1,
            flags=re.MULTILINE
        )

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Injected audio into {f} for Day {day}')

if __name__ == '__main__':
    inject_audio_player()
