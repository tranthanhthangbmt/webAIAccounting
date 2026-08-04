import os
import re
import importlib.util

# 1. Load gen_ch05.py as a module
spec = importlib.util.spec_from_file_location("gen_ch05", "gen_ch05.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

slides = module.slides

# 2. Extract Normal Slides and Image Slides
normal_slides = []
image_slides = []
be_ex_pac_slides = []

for slide in slides:
    if slide["type"] == "title_slide":
        normal_slides.append(slide)
    elif slide["type"] == "normal":
        if "Bài tập Ngắn" in slide["title"] or "Bài tập (Exercises)" in slide["title"] or "Tình Huống Ứng Dụng" in slide["title"]:
            be_ex_pac_slides.append(slide)
        elif "Tóm tắt Mục tiêu" in slide["title"]:
            be_ex_pac_slides.append(slide)
        else:
            normal_slides.append(slide)
    elif slide["type"] == "image":
        if "ILLUSTRATION" in slide["title"]:
            image_slides.append(slide)
        else:
            be_ex_pac_slides.append(slide)
    elif slide["type"] == "double_image":
        be_ex_pac_slides.append(slide)

# 3. Group normal slides by section
sections = []
current_section = []
for slide in normal_slides:
    if slide.get("title", "").startswith("5."):
        if current_section:
            sections.append(current_section)
        current_section = [slide]
    else:
        current_section.append(slide)
if current_section:
    sections.append(current_section)

print(f"Number of sections: {len(sections)}")

# 4. Group images by section
lo_sections = sections[1:]
images_per_lo = len(image_slides) // len(lo_sections)
image_chunks = [image_slides[i:i + images_per_lo] for i in range(0, len(image_slides), images_per_lo)]
if len(image_chunks) > len(lo_sections):
    image_chunks[-2].extend(image_chunks[-1])
    image_chunks.pop()

print(f"Number of image chunks: {len(image_chunks)}")

# 5. Interleave
new_slides = []
new_slides.extend(sections[0])

for i, lo_section in enumerate(lo_sections):
    chunk_images = image_chunks[i] if i < len(image_chunks) else []
    images_per_text = len(chunk_images) // len(lo_section)
    remainder = len(chunk_images) % len(lo_section)
    
    img_idx = 0
    for j, text_slide in enumerate(lo_section):
        new_slides.append(text_slide)
        count = images_per_text + (1 if j < remainder else 0)
        for _ in range(count):
            if img_idx < len(chunk_images):
                new_slides.append(chunk_images[img_idx])
                img_idx += 1

new_slides.extend(be_ex_pac_slides)

# 6. Write out slide_data_ch05.py
out_path = "slide_data_ch05.py"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(f'chapter_title = {repr(module.chapter_title)}\n')
    f.write(f'chapter_subtitle = {repr(module.chapter_subtitle)}\n\n')
    f.write('slides = [\n')
    
    for slide in new_slides:
        f.write('    {\n')
        for k, v in slide.items():
            if k == "content":
                f.write(f'        "{k}": r"""{v}""",\n')
            else:
                f.write(f'        "{k}": "{v}",\n')
        f.write('    },\n')
    f.write(']\n')

print("Wrote slide_data_ch05.py successfully.")
