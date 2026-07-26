# Kế hoạch Xây dựng Slide Bài giảng Buổi 9

## 1. Thông tin chung
- **Học phần:** Trí tuệ Nhân tạo Ứng dụng trong Kế toán (AI in Accounting)
- **Buổi học:** Buổi 9
- **Chủ đề chính:** AI trong Tài chính Cá nhân và Thị trường Tài sản Số (Crypto Assets, DeFi \& Robo-Advisors)
- **Tài liệu nguồn:** `docs/buoi_09.md` (Chương 2 \& Chương 6)
- **Tài liệu bổ trợ:** `TaiLieu/script/audioScript_Day09.txt`
- **Số lượng Slide dự kiến:** ~45 slides
- **Thời lượng:** 3 tiết (135 phút)
- **Kiến trúc:** Beamer LaTeX, Aspect Ratio 16:9, Theme Madrid, tiếng Việt (T5 encoding).

## 2. Mục tiêu Bài giảng
1. Nắm bắt sự đứt gãy kiến tạo của nền kinh tế: Chuyển dịch từ tổ chức tài chính tập trung (CeFi) sang Tài chính phi tập trung (DeFi).
2. Hiểu rõ cơ chế tự thực thi của Hợp đồng thông minh (Smart Contracts) thông qua ẩn dụ "Mảnh ghép Lego tiền tệ" và "Máy bán hàng tự động".
3. Phân tích bài toán định giá Tài sản Kỹ thuật số (NFTs) làm tài sản thế chấp và cơ chế thanh lý tàn khốc không có Margin Call.
4. Lật tẩy các chiêu trò Rửa tiền bằng NFT qua Giao dịch tự chéo (Wash Trading) và cách AI dùng "Thuật toán gom cụm" để truy vết dòng tiền bẩn.
5. Đánh giá tính kinh tế và rủi ro tâm lý - hệ thống của Robo-Advisors. Nhận thức rõ trọng trách kiểm toán thuật toán trong tương lai.

## 3. Tích hợp Ẩn dụ từ Audio Script
Slide sẽ lồng ghép các câu chuyện/ẩn dụ thực tế nhằm mang lại sự sinh động cho bài giảng:
- **Ngân hàng vô hình:** Kiểm toán một ngân hàng mà kho tiền là chuỗi mã lệnh nguồn mở, tài sản thế chấp là bức tranh ảo (NFT), nhân viên là một thuật toán vô cảm.
- **Mảnh ghép Lego tiền tệ (DeFi):** Khác với nhà hàng có bồi bàn tận răng (Ngân hàng truyền thống), DeFi là căn bếp mà khách tự lắp ráp nguyên liệu mà không cần xin phép.
- **Máy bán hàng tự động:** Hợp đồng thông minh. Không cần nộp hồ sơ chứng minh thu nhập. Điều kiện A xảy ra $\rightarrow$ B được thực thi.
- **Thế chấp bằng vé số:** Đưa tài sản biến động (NFT) làm tài sản thế chấp. Oracle báo sụt giá $\rightarrow$ Không có ân hạn, bán tháo ngay lập tức.
- **Wash Trading (Rửa tiền NFT):** Mua lại bức tranh ảo tự vẽ bằng tiền bẩn với giá trên trời (1 triệu USD) để hợp pháp hóa dòng tiền.
- **Thuật toán Gom cụm (Clustering):** AI rà quét mạng lưới tìm ra Ví A và Ví B cố tình che giấu nhưng có chung nguồn cấp vốn.
- **Điểm mù Tâm lý:** Nhà đầu tư KHÔNG có "hội chứng sợ thuật toán". Mù quáng tin tưởng hộp đen miễn là danh mục màu xanh. Khi lỗ thì đổ tại kinh tế vĩ mô.
- **Thiên nga đen:** Hàng triệu Robo-Advisors đồng loạt kích hoạt lệnh bán tháo (hút cạn thanh khoản) vì học chung một tập dữ liệu.

## 4. Cấu trúc chi tiết (3 Tiết học - ~45 Slides)

### Tiết 1: Sự Đứt gãy Kiến tạo \& Tài chính Phi tập trung - DeFi (Slide 04 - 17)
- **Slide 04 - 06:** Đặt vấn đề: Kiểm toán một Ngân hàng Vô hình (Kho tiền là mã lệnh, tài sản là pixel, nhân viên là thuật toán). Sự đứt gãy kiến tạo của dòng tiền toàn cầu.
- **Slide 07 - 09:** Tài chính Phi tập trung (DeFi): Loại bỏ hoàn toàn người trung gian. Ẩn dụ Căn bếp tự lắp ráp nguyên liệu thay vì Nhà hàng có người phục vụ.
- **Slide 10 - 12:** Mảnh ghép Lego Tiền tệ: Các giao thức vay \& cho vay xếp chồng lên nhau mà không cần xin phép. Không cần chứng minh thu nhập!
- **Slide 13 - 15:** Hợp đồng Thông minh (Smart Contracts): Cỗ máy bán hàng tự động không thể bị phá vỡ (A xảy ra $\rightarrow$ B thực thi).
- **Slide 16 - 17:** Dấu hỏi về Định giá trong không gian phi tập trung. Đưa NFTs và Metaverse vào phương trình.

### Tiết 2: Tài sản Kỹ thuật số, Thanh lý Tàn khốc \& Rửa tiền (Slide 18 - 32)
- **Slide 18 - 20:** Định giá Bức tranh Ảo: Khái niệm Sở hữu qua nguyên tắc khan hiếm. Ý vs. Pháp định nghĩa NFT. Thế chấp bằng "một sấp vé số".
- **Slide 21 - 23:** Cơ chế Thanh lý Khắt khe: Không có "Margin Call" trễ vài ngày như ngân hàng. Oracle báo giá giảm $\rightarrow$ Tước quyền, bán tháo ngay lập tức!
- **Slide 24 - 26:** Lầm tưởng về Blockchain: "Bán ẩn danh" chứ không phải ẩn danh tuyệt đối (Sổ cái công khai nhưng không có nhãn dán tên thật).
- **Slide 27 - 29:** Nghệ thuật Rửa tiền hoàn hảo: Giao dịch tự chéo (Wash Trading). Tiền bẩn mua bức tranh 1 triệu USD do chính mình tạo ra để biến thành "Doanh thu Hợp pháp".
- **Slide 30 - 32:** Ma thuật Đánh bại Ma thuật: Dùng AI chống tội phạm. Thuật toán Gom cụm (Clustering) truy vết liên kết ẩn giữa các Ví ảo trên On-chain \& Dữ liệu mạng xã hội (Discord, Telegram).

### Tiết 3: Robo-Advisors, Tâm lý Hành vi \& Tương lai Kiểm toán (Slide 33 - 45)
- **Slide 33 - 35:** Kỷ nguyên Robo-Advisors: Lý thuyết Danh mục Đầu tư hiện đại. Quản lý hàng triệu tài khoản, chi phí biên bằng 0. Kỷ luật, lạnh lùng, không hoảng loạn.
- **Slide 36 - 38:** Tâm lý Hành vi Đầu tư: Phá vỡ Lầm tưởng "Hội chứng sợ thuật toán". Nhà đầu tư chỉ quan tâm danh mục màu xanh! Điểm mù nhận thức khi máy móc thua lỗ.
- **Slide 39 - 41:** Rủi ro Hệ thống \& Sự kiện Thiên nga Đen: Hàng triệu hộp đen học cùng tập dữ liệu. Phản ứng đám đông của thuật toán $\rightarrow$ Hút cạn thanh khoản không có bộ đệm cảm xúc.
- **Slide 42 - 43:** Câu hỏi mở về Pháp lý: Thuật toán gây thiệt hại triệu đô, ai sẽ đền bù? (Lập trình viên, Sàn giao dịch hay Nhà đầu tư?).
- **Slide 44:** Tương lai của Nghề Kiểm toán: Không chỉ soát xét giấy tờ mà là kiểm toán hợp đồng thông minh, định giá tài sản ảo.
- **Slide 45:** Tổng kết \& Q/A.

## 5. Lộ trình Triển khai
1. Nhận phản hồi/phê duyệt từ User cho kế hoạch này.
2. Viết file `build_beamer_day09.py` tạo mã LaTeX với ~45 Slides.
3. Thực thi kịch bản và biên dịch PDF.
4. Kiểm thử kết quả, cập nhật Walkthrough.
