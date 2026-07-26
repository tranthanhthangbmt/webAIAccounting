import re

with open('docs/buoi_09.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    s = line.strip()
    if len(s) > 0 and len(s) < 100 and (re.match(r'^(\d+)(\.\d+)*\s+[A-ZÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬEÉÈẺẼẸÊẾỀỂỄỆIÍÌỈĨỊOÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢUÚÙỦŨỤƯỨỪỬỮỰYÝỲỶỸỴĐa-zA-Z]', s) or 'CHƯƠNG' in s.upper() or 'TÓM TẮT' in s.upper() or 'TÀI LIỆU THAM KHẢO' in s.upper() or 'DOI:' in s or '--- Trang' in s):
        print(f"Line {i+1}: {s}")
