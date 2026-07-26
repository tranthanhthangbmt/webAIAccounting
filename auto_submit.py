import pyautogui
import time
import sys

print("Đang chạy Auto-Submit cho Antigravity. Nhấn Ctrl+C để dừng...")

while True:
    try:
        # Tìm nút Submit trên màn hình (độ chính xác 80% để tránh sai số hiển thị)
        # Nút "1. Yes, allow this time" thường đã là mặc định, nên chỉ cần click Submit.
        location = pyautogui.locateCenterOnScreen('submit_btn.png', confidence=0.8)
        
        if location:
            pyautogui.click(location)
            print("Đã tự động nhấn Submit!")
            time.sleep(3) # Đợi 3 giây sau khi click để tránh click đúp
            
    except pyautogui.ImageNotFoundException:
        pass # Không tìm thấy nút thì bỏ qua
    except KeyboardInterrupt:
        print("\nĐã dừng script.")
        sys.exit()
        
    time.sleep(1) # Quét lại mỗi giây