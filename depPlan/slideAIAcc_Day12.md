# Kế hoạch chi tiết Slide Bài giảng AI cho Kế toán - Buổi 12 (45 Slides)

## Thông tin chung
- **Chủ đề:** Thực hành AI Nhận thức và AI Tạo sinh trong Kế toán - Tài chính (Generative AI & Web-Enhanced ChatGPT)
- **Thời lượng:** 135 Phút / 3 Tiết
- **Đối tượng:** Sinh viên chuyên ngành Kế toán - Kiểm toán
- **Mục tiêu:** 
  - Hiểu rõ sự dịch chuyển từ Kế toán ghi chép (nhìn kính chiếu hậu) sang Kế toán dự báo chiến lược (hệ thống GPS).
  - Phân biệt cơ chế hoạt động của phần mềm cũ (từ khóa) và GenAI (ngữ nghĩa).
  - Nắm bắt hiện tượng "Ảo giác AI" (Hallucination) và vai trò của tư duy phản biện.
  - Sử dụng và triển khai GPT Store / Custom GPTs (RAG) vào công việc thực tế an toàn.
  - Áp dụng nguyên tắc "Human-in-the-loop" và bảo mật dữ liệu Enterprise.

---

## Cấu trúc chi tiết (44 - 45 Slides)

### Phần 1: Khởi động & Sự dịch chuyển cốt lõi (5 Slides)
1. **Title Slide:** AI Nhận thức và AI Tạo sinh trong Kế toán - Từ Kế toán truyền thống đến Cố vấn Chiến lược.
2. **Mục tiêu Bài học:** GenAI, Custom GPTs, RAG, Bảo mật & Kiểm toán liên tục.
3. **Agenda:** Các nội dung chính của buổi học.
4. **Ẩn dụ chiếc Ô tô (Kế toán truyền thống):** Lái xe 120km/h với kính chắn gió bịt kín, chỉ nhìn chằm chằm vào gương chiếu hậu (Báo cáo quá khứ). Rủi ro cao, thụ động.
5. **Cuộc lột xác với GenAI:** Gỡ màn che, lắp hệ thống GPS định vị và dự báo rủi ro theo thời gian thực. "Máy tính sơ khai" tiến hóa thành "Mô hình tạo sinh" hiểu ngôn ngữ.

### Phần 2: Cơ chế khác biệt của AI & Machine Learning (8 Slides)
6. **Case Study: Global Tech Enterprises:** Quản lý tài chính đa quốc gia, luật thuế đan chéo, hàng tỷ giao dịch.
7. **Phần mềm cũ (Từ khóa):** Dò tìm Keyword (Keyword matching), sai một chữ là báo lỗi, đòi hỏi con người can thiệp liên tục.
8. **GenAI (Mạng Neuron sâu):** Phân tích ngữ nghĩa, "hiểu mục đích" của luật thuế y hệt chuyên gia lão làng. Tự động hóa tuân thủ.
9. **Từ Dọn dẹp quá khứ đến Phân tích dự báo:** Không chờ đến cuối quý để hốt hoảng vì dòng tiền âm.
10. **Predictive Analytics:** AI mô hình hóa biến động tỷ giá, cảnh báo thiếu hụt thanh khoản trước hàng tháng.
11. **Sự giải phóng nhân lực:** Cắt giảm việc nhập liệu chân tay, chuyển hướng sang trả lời các câu hỏi sống còn của doanh nghiệp.
12. **Kỹ năng sinh tồn mới - Data Literacy:** Kế toán viên có cần học viết code Python? Không, nhưng phải hiểu cách dữ liệu đầu vào biến thành đầu ra.
13. **Năng lực diễn giải:** Dịch các dashboard chỉ số thành những câu chuyện kinh doanh (Data Storytelling) để Ban giám đốc chốt phương án.

### Phần 3: Tư duy phản biện & Ảo giác AI (8 Slides)
14. **Nghịch lý niềm tin:** Máy tính không biết nói dối, tại sao không thể tin AI 100%?
15. **Bản chất của LLMs:** AI dự đoán từ tiếp theo dựa trên xác suất lịch sử, không có nhận thức kinh doanh thực tế.
16. **Căn bệnh "Ảo giác AI" (Hallucination):** Tự tin đưa ra kết luận sai bét, bịa chuyện thuyết phục do dữ liệu cũ hoặc thiên kiến.
17. **Ẩn dụ "Cậu Chuyên viên Sơ cấp":** AI là Junior Analyst siêu phàm, quét 10.000 công ty trong 1 giây nhưng thiếu nhạy bén thương trường.
18. **Báo động đỏ mù quáng:** AI chặn hạn mức tín dụng của đối tác vì biến động ngắn hạn, bỏ qua kế hoạch sáp nhập nửa năm trước.
19. **Ẩn dụ "Bếp trưởng và Phụ bếp":** AI là phụ bếp sơ chế cực nhanh; Kế toán viên là Bếp trưởng nêm nếm và kiểm soát chất lượng món ăn.
20. **Tư duy Phản biện:** Yếu tố chốt hạ để đối chiếu đề xuất của AI với thực tế thị trường.
21. **Trách nhiệm giải trình (Accountability):** Rốt cuộc, người đặt bút ký duyệt mới là người chịu trách nhiệm trước pháp luật, không phải thuật toán.

### Phần 4: Kỷ nguyên Cá nhân hóa với Cửa hàng GPT (GPT Store) (8 Slides)
22. **Giới hạn của việc tìm kiếm:** "Mọi người ghét tìm kiếm" (Sam Altman). Trích xuất con số thuế nhanh chóng không cần lặn ngụp trong phần mềm.
23. **Sự kiện Dân chủ hóa AI:** Từ việc thuê đội ngũ kỹ sư đắt đỏ đến việc tự làm Kiến trúc sư AI bằng ngôn ngữ tự nhiên.
24. **GPT Store vs. App Store:** App Store tải ứng dụng thụ động (máy tính). GPT Store tải về "những bộ não kỹ thuật số" đã được huấn luyện nghiệp vụ.
25. **Custom GPTs trong Kế toán:** Trợ lý thuế quốc tế, Chuyên viên CSKH 24/7, Nhà phân tích rủi ro. 
26. **Xây dựng Custom GPT:** Nạp sổ tay kế toán, quy chế nội bộ, lịch sử giao dịch độc quyền vào hệ thống.
27. **Cơ chế RAG (Retrieval-Augmented Generation):** Không "chém gió" bừa. AI phải đối chiếu tài liệu nội bộ (Retriever) rồi mới đưa ra câu trả lời (Generation).
28. **Sức mạnh của Context Window:** Cửa sổ ngữ cảnh khổng lồ, duy trì bối cảnh xuyên suốt phiên làm việc phức tạp.
29. **Hiệu suất thực tế:** Custom GPT tự động quét sạch báo cáo thu chi hàng tháng để tìm khoản tiêu sai quy chế. Chi phí giảm sập sàn.

### Phần 5: Bảo mật dữ liệu & Quản trị Rủi ro (8 Slides)
30. **Gắn não AI vào tủy sống doanh nghiệp:** Thách thức về chất lượng GPT Store (thượng vàng hạ cám) và ảo giác (hallucination).
31. **Vấn đề sinh tử - Bảo mật (Data Privacy):** Dữ liệu tài chính là chiến lược kinh doanh, là tính mạng của tổ chức (Tuân thủ GDPR, CCPA).
32. **Rủi ro rò rỉ chiến lược:** Ném kế hoạch sáp nhập, báo cáo thu chi cho AI -> Vô tình làm mồi huấn luyện -> Công ty đối thủ khai thác được.
33. **Trách nhiệm pháp lý:** "Sếp đi tù" nếu vi phạm nguyên tắc bảo mật thông tin khách hàng và tài chính.
34. **Giải pháp AI Enterprise (Bản Doanh nghiệp):** Cam kết pháp lý, chuẩn SOC 2. Dữ liệu bị cô lập hoàn toàn trong "bong bóng".
35. **Zero Data Retention:** Đảm bảo không lấy dữ liệu nội bộ để huấn luyện ngược cho AI công cộng.
36. **Kiểm toán Hệ thống nội bộ:** Mã hóa dữ liệu nhạy cảm trước khi nạp vào AI, quét lỗ hổng liên tục.
37. **Quy tắc vàng: Human-in-the-loop (HITL):** Không bao giờ để máy tự làm 100%. Luôn có con người phân quyền kiểm duyệt cuối cùng trước khi đồng tiền được chuyển đi.

### Phần 6: Tương lai Kiểm toán liên tục & Tổng kết (7 Slides)
38. **Cẩm nang sinh tồn:** Nắm bắt AI ngay lúc này không còn là viễn cảnh tương lai, mà là lợi thế cạnh tranh sống còn.
39. **Sự lột xác của nghề kế toán:** Rời bỏ việc sao chép quá khứ, nâng cấp thành Đối tác kinh doanh (Business Partner).
40. **Tương lai: Kiểm toán liên tục (Continuous Auditing):** Từ kiểm toán theo chu kỳ (quý, năm) sang bắt lỗi Real-time (Thời gian thực).
41. **Bắt lỗi tại 1/1000 giây:** Tự động già soát giao dịch ngay khi bấm nút. Hệ thống tài chính tự chữa lành (Self-healing).
42. **Ngăn chặn đại án:** Bóp nghẹt gian lận từ trong trứng nước, trước khi dòng tiền bẩn kịp nhảy khỏi tài khoản.
43. **Tổng kết buổi học:** GenAI, RAG, Ảo giác AI, Quản trị bảo mật dữ liệu.
44. **Q\&A:** Thảo luận, hỏi đáp với sinh viên.
