@echo off
chcp 65001 >nul
title Khởi động Website AI trong Kế toán - Đại học Đông Á
echo ========================================================
echo   ĐẠI HỌC ĐÔNG Á - KHOA KẾ TOÁN & KIỂM TOÁN
echo   HỆ THỐNG WEBSITE MÔN HỌC TRÍ TUỆ NHÂN TẠO CHO KẾ TOÁN
echo ========================================================
echo.
echo Đang khởi động máy chủ cục bộ (Local Server) tại cổng 8000...
echo.
echo [1] Trang chủ môn học:             http://localhost:8000 (Mật khẩu: UDA)
echo [2] Cổng Chuyên đề Day 03 Extra:   http://localhost:8000/video/Day03_Extra/index.html
echo [3] Thư viện Bài báo Day 03:      http://localhost:8000/video/Day03_Extra/papers/index.html
echo [4] Cổng Chuyên đề Day 02 Extra:   http://localhost:8000/video/Day02_Extra/index.html
echo [5] Thư viện Bài báo Day 02:      http://localhost:8000/video/Day02_Extra/papers/index.html
echo [6] Cổng Video Day 01 Extra:       http://localhost:8000/video/Day01_Extra/Videos/index.html
echo.
echo Đang tự động mở trình duyệt...
echo (Giữ cửa sổ này mở trong khi duyệt web, bấm Ctrl+C hoặc đóng cửa sổ khi muốn dừng)
echo ========================================================

start "" "http://localhost:8000/video/Day03_Extra/index.html"
python -m http.server 8000
pause
