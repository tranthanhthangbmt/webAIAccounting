# Kế hoạch chi tiết Slide Bài giảng AI cho Kế toán - Buổi 13 (45 Slides)

## Thông tin chung
- **Chủ đề:** Kỹ thuật Viết Prompt, Khung tư duy SPARKS & Chiến lược Dữ liệu (4 Trụ cột Phân tích)
- **Thời lượng:** 135 Phút / 3 Tiết
- **Đối tượng:** Sinh viên chuyên ngành Kế toán - Kiểm toán
- **Mục tiêu:** 
  - Nắm vững 4 trụ cột phân tích dữ liệu qua lăng kính trận đấu thể thao.
  - Làm chủ Kỹ thuật Prompt (Prompt Engineering) cho nghiệp vụ Kế toán - Tài chính.
  - Áp dụng Khung tư duy SPARKS vào các bài toán thực tế (Accounts Payable).
  - Nhận diện "Bãi mìn rủi ro": Bảo mật, Hộp đen (Black Box) và Vấn đề Đạo đức của AI.

---

## Cấu trúc chi tiết (45 Slides)

### Phần 1: Khởi động \& Sự dịch chuyển vĩ đại (5 Slides)
1. **Title Slide:** Kỹ thuật Prompt \& Chiến lược Phân tích Dữ liệu Tài chính (SPARKS Framework).
2. **Mục tiêu Bài học:** 4 Trụ cột dữ liệu, Prompt Engineering, Khung SPARKS, Đạo đức AI.
3. **Agenda:** Các nội dung chính của buổi học.
4. **Sự dịch chuyển vĩ đại:** Từ việc cặm cụi ghi chép lịch sử đến việc sử dụng dữ liệu để "kiến tạo tương lai".
5. **Kính viễn vọng Tiên đoán:** Ẩn dụ của Wayne R. Landsman - "AI đã biến phân tích tài chính từ một chiếc gương chiếu hậu thành một chiếc kính viễn vọng dự đoán mạnh mẽ".

### Phần 2: Chiến lược Dữ liệu \& 4 Trụ cột Phân tích (10 Slides)
6. **Nguyên lý Sinh tồn:** "Rác đầu vào = Rác đầu ra" (Garbage in, Garbage out). Nếu không có Data Strategy, mọi công cụ AI đều vô nghĩa.
7. **Ẩn dụ Trận đấu Thể thao:** Hãy coi hệ thống kế toán doanh nghiệp như một trận đấu thể thao khắc nghiệt.
8. **Trụ cột 1 - Phân tích Mô tả (Descriptive):** "Chuyện gì đã xảy ra?".
9. **Nhìn lên bảng điểm điện tử:** Chỉ cho ta biết tỷ số (Tổng doanh thu, Lợi nhuận quý), nhưng không cho biết tại sao đội nhà lại thua. Nền tảng bắt buộc.
10. **Trụ cột 2 - Phân tích Chẩn đoán (Diagnostic):** "Tại sao điều đó lại xảy ra?".
11. **Băng ghi hình quay chậm:** Xem lại từng pha bóng để tìm "thủ phạm". Lợi nhuận giảm không phải do doanh thu, mà do chi phí bảo trì máy móc đột ngột tăng vọt.
12. **Trụ cột 3 - Phân tích Dự báo (Predictive):** "Chuyện gì sẽ xảy ra?".
13. **Chạy kịch bản tương lai:** Dùng mô hình toán học (Hồi quy) thay vì linh cảm. Ví dụ Supercooters: Nếu chi phí bảo hành tăng 10% thì doanh thu 2026 sẽ ra sao?
14. **Trụ cột 4 - Phân tích Đề xuất (Prescriptive):** "Chúng ta nên làm gì?".
15. **Bản đồ Chiến lược:** Đỉnh cao của phân tích (What-If analysis). Trả lời thẳng câu hỏi: "Nên sản xuất bao nhiêu xe mỗi loại để tối đa hóa biên lợi nhuận đóng góp?".

### Phần 3: Kỹ năng Sinh tồn: Kỹ thuật Viết Prompt (10 Slides)
16. **Prompt Engineering là gì?** Nghệ thuật và khoa học thiết kế lệnh đầu vào. Giao tiếp với AI sao cho hiệu quả nhất.
17. **Cơ chế xác suất của LLM:** AI không tự "nghĩ", nó dự đoán ngữ cảnh. Không có bối cảnh = Câu trả lời rác.
18. **Nguyên tắc 1 - Chỉ định vai trò (Role-based):** Không hỏi chung chung. "Hãy đóng vai Kế toán trưởng 15 năm kinh nghiệm chuẩn mực IFRS..."
19. **Nguyên tắc 2 - Cung cấp bối cảnh (Context \& Clarity):** Gắn liền với loại hình doanh nghiệp, mục tiêu và định dạng dữ liệu đầu vào.
20. **Nguyên tắc 3 - Tư duy theo bước (Chain-of-Thought):** Yêu cầu AI "re-check" từng bước tính toán (ví dụ: phân bổ chi phí, thuế TNDN hoãn lại) trước khi chốt kết quả.
21. **Thực chiến 1: Phân tích Báo cáo Tài chính.** Yêu cầu AI tính hệ số thanh toán hiện hành, nhanh và đưa ra 3 gạch đầu dòng nhận xét chiến lược.
22. **Thực chiến 2: Rà soát Hóa đơn \& Thuế GTGT.** Phát hiện rủi ro và các khoản mục bất thường.
23. **Thực chiến 3: Thư tư vấn Khách hàng.** Soạn thảo thư chuyên nghiệp báo cáo kiểm toán nội bộ.
24. **Sai lầm chết người 1 \& 2:** Prompt quá chung chung; Nhắm mắt tin tưởng khả năng làm Toán (cộng trừ nhân chia) của LLM mà không kiểm chứng.
25. **Sai lầm chết người 3:** Lộ lọt dữ liệu. Đưa tên thật, mã số thuế bí mật của khách hàng lên AI công cộng.

### Phần 4: Khởi động Dự án với Khung Tư duy SPARKS (10 Slides)
26. **Giới thiệu SPARKS Framework:** Phương pháp luận chuẩn hóa của Richardson dành riêng cho Phân tích dữ liệu Kế toán.
27. **S - State the Question:** Đặt câu hỏi cốt lõi (Ví dụ: Tại sao chi phí mua hàng Quý 4 tăng đột biến?).
28. **P - Partition the Data:** Trích xuất, làm sạch và chia nhỏ dữ liệu từ hệ thống ERP/AIS.
29. **A - Analyze the Data:** Thực hiện phân tích (Áp dụng 1 trong 4 trụ cột đã học).
30. **R - Refine the Analysis:** Tinh chỉnh, kiểm tra giá trị ngoại lai (Outliers - lỗi đánh máy dư số 0), loại bỏ nhiễu.
31. **K - Communicate the Insights:** Truyền đạt qua Dashboards (Biểu đồ, báo cáo quản trị) để lãnh đạo ra quyết định.
32. **S - Stop and Reflect:** Dừng lại \& Suy ngẫm. Trả lời trọn vẹn câu hỏi ban đầu chưa?
33. **Thực hành SPARKS - Bài toán Accounts Payable (AP):** Giới thiệu Từ điển Dữ liệu mua hàng (InvoiceNo, VendorID, QualityRating...).
34. **Case Study 1: Tìm hóa đơn bất thường:** Sử dụng Scatter Plot (Biểu đồ phân tán) giữa Ngày hóa đơn và Số tiền để phát hiện gian lận.
35. **Case Study 2: Chất lượng Nhà cung cấp:** Phân tích điểm QualityRating theo thời gian để loại bỏ đối tác kém.

### Phần 5: Bãi mìn Rủi ro - Bảo mật, Hộp đen \& Đạo đức AI (10 Slides)
36. **Động cơ Siêu tốc vs. Bãi mìn Rủi ro:** Bơm AI vào hệ thống dữ liệu giống như lắp động cơ phản lực, nhưng cũng mở ra vô vàn rủi ro.
37. **Vấn đề Bảo mật (Security):** Vụ rò rỉ Equifax 2017 (hàng triệu người bị phơi bày dữ liệu do quản lý kém) vs. Global Tech (Chuẩn GDPR, mã hóa bọc trong pháo đài).
38. **Hiện tượng Hộp đen (Black Box):** Máy tính ra quyết định cực nhanh nhưng không giải thích được lý do (Ví dụ: Giao dịch thuật toán tần suất cao HFT).
39. **Sự mù mờ của AI:** Gây lo ngại cho thị trường chứng khoán và cơ quan kiểm toán vì không thể "Truy vết" tư duy của máy.
40. **Vấn đề Đạo đức \& Sự thiên lệch (Bias):** Sự va chạm giữa công nghệ và triết học.
41. **Cỗ máy tàn nhẫn:** AI có thể mù quáng đổ hàng tỷ đô vào nhiên liệu hóa thạch hoặc vũ khí chỉ để "Tối đa hóa lợi nhuận" theo hàm mục tiêu, phớt lờ đạo đức môi trường.
42. **Giải pháp cốt lõi:** Lỗi không nằm ở mã code, lỗi nằm ở người thiết lập. Yêu cầu giám sát liên tục (Continuous Monitoring).
43. **Cái "Phanh Khẩn Cấp" của Con người:** Dù AI có thông minh đến mấy, Kế toán trưởng vẫn phải là người giữ quyền chốt hạ cuối cùng.
44. **Giá trị không thể thay thế:** Kỹ năng toán học của AI có thể vượt con người, nhưng Trực giác đạo đức và Sự thấu cảm triết học thì không một dòng code nào lập trình được.
45. **Tổng kết \& Q\&A:** Vai trò mới của Kế toán viên: Trở thành Strategic Advisor (Cố vấn chiến lược).
