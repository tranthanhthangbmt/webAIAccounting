# Kế hoạch chi tiết Slide Bài giảng AI cho Kế toán - Buổi 14 (45 Slides)

## Thông tin chung
- **Chủ đề:** Phân tích Dữ liệu Chuyên sâu: Khám phá Dữ liệu (EDA) \& Nghệ thuật Truyền đạt Kết quả (Data Storytelling).
- **Thời lượng:** 135 Phút / 3 Tiết
- **Đối tượng:** Sinh viên chuyên ngành Kế toán - Kiểm toán
- **Mục tiêu:** 
  - Phân biệt rõ ranh giới giữa "Báo cáo" (Reporting) và "Khám phá" (Exploration).
  - Làm chủ 5 mô hình thăm dò dữ liệu kế toán và kỹ thuật PivotTable.
  - Vận dụng mô hình Kim tự tháp Freytag để kể chuyện bằng số liệu.
  - Hiểu về Tâm lý học thị giác (Gestalt) trong thiết kế Bảng điều khiển (Dashboards).
  - Nhận diện các "Bẫy biểu đồ" vi phạm đạo đức và kiểm duyệt rủi ro AI tự động.

---

## Cấu trúc chi tiết (45 Slides)

### Phần 1: Báo cáo vs. Khám phá (Reporting vs. Exploration) (8 Slides)
1. **Title Slide:** Khám phá Dữ liệu \& Nghệ thuật Truyền đạt Kết quả (Buổi 14 - Buổi cuối).
2. **Mục tiêu Bài học:** EDA, Data Storytelling, Gestalt Principles, Ethical Charting.
3. **Agenda:** Các nội dung chính của buổi học.
4. **Bối cảnh kỷ nguyên số:** Doanh nghiệp bị nhấn chìm trong Big Data. Dữ liệu thô tự nó bị "câm", nếu không khai thác thì nó chỉ gây nhiễu loạn.
5. **Báo cáo (Reporting) là gì?** Thu thập và trình bày quá khứ. Nó mang tính "tĩnh", chỉ trả lời câu hỏi "Cái gì?". (Ví dụ: Đọc hóa đơn siêu thị xem hôm nay tiêu bao nhiêu tiền).
6. **Khám phá (Exploration) là gì?** Đào sâu để tìm Insight (sự thấu hiểu). Nó mang tính "động", trả lời câu hỏi "Tại sao?" và "Như thế nào?". 
7. **Ví dụ Khám phá:** Gom hàng chục hóa đơn lại và phát hiện quy luật tương quan: "Trời nóng > 30 độ C thì lượng mua kem tăng vọt".
8. **Quyền năng của Khám phá:** Não người không thể tự thấy tương quan từ 10,000 dòng Excel. Chúng ta cần công cụ như PivotTable (Kéo - Thả - Xoay chiều dữ liệu) để tìm các góc khuất.

### Phần 2: 5 Mô hình Mối quan hệ Dữ liệu (Data Exploration Patterns) (10 Slides)
9. **Tại sao cần Mô hình Thăm dò?** Định hướng cho kế toán viên biết mình đang tìm kiếm điều gì trong mớ bòng bong dữ liệu.
10. **Pattern 1: So sánh Danh nghĩa (Nominal Comparison).** So sánh các hạng mục không có thứ tự (Ví dụ: So sánh chi phí tiếp thị giữa 3 chi nhánh Hà Nội, Đà Nẵng, TP.HCM).
11. **Pattern 2: Phân phối (Distribution).** Xem tần suất xuất hiện của dữ liệu (Box Plot).
12. **Ứng dụng Tìm Ngoại lai (Outliers):** Những hóa đơn vọt ra ngoài khoảng phân phối trung bình chính là dấu hiệu của sai sót hoặc gian lận khai khống.
13. **Pattern 3: Sai lệch (Deviation).** So sánh thực tế (Actual) với mức tham chiếu (Budget).
14. **Phân tích Phương sai Ngân sách (Variance Analysis).** Favorable (Thuận lợi) vs. Unfavorable (Bất lợi). Ví dụ Case Study xe Happy Colors: Dòng Tatra giảm -10.45%.
15. **Pattern 4: Xếp hạng (Ranking).** Sắp xếp từ cao xuống thấp để tìm trọng tâm.
16. **Quy tắc Pareto 80/20:** Tìm ra 20% khách hàng mang lại 80% lợi nhuận, hoặc 5 dòng sản phẩm lỗi nhiều nhất.
17. **Pattern 5: Phần-trên-Tổng thể (Part-to-Whole).** Hiển thị cơ cấu (Stacked Bar, Treemap).
18. **Lưu ý với Part-to-Whole:** Phân tích cơ cấu nguồn vốn, sự chuyển dịch doanh thu của các thương hiệu.

### Phần 3: Nghệ thuật Kể chuyện bằng Dữ liệu (Data Storytelling) (10 Slides)
19. **Năng lực Dữ liệu (Data Literacy):** Có Insight mới chỉ là nửa chặng đường. Quăng một bảng Excel chi chít số lên máy chiếu sẽ khiến cả phòng ngáp dài. Phải "bán" được Insight đó!
20. **3 Cột trụ của Câu chuyện Dữ liệu:** Data (Sự thật) + Narrative (Cốt truyện/Bối cảnh) + Visuals (Hình ảnh).
21. **Tại sao lại cần Hình ảnh?** Não người xử lý hình ảnh nhanh hơn văn bản 60.000 lần. Thông tin dễ nhớ hơn 22% khi kể bằng hình.
22. **Cấu trúc Kịch bản Shakespeare (Freytag's Pyramid):** Mượn nghệ thuật sân khấu để báo cáo tài chính không hề làm mất đi tính chuyên nghiệp, mà giúp não bộ sếp tiếp nhận tốt nhất.
23. **Giai đoạn 1: Mở đầu (Bối cảnh).** Trình bày bức tranh chung (Ví dụ: Chi phí vật tư toàn công ty đột ngột tăng 15%).
24. **Giai đoạn 2: Thắt nút.** Tung manh mối (Sự gia tăng này chỉ tập trung vào duy nhất một nhà cung cấp mới).
25. **Giai đoạn 3: Cao trào (Climax).** Đập bằng chứng quyết định (Chiếu biểu đồ thời gian: Giờ phê duyệt hóa đơn trùng khớp từng phút với giao dịch chuyển khoản cá nhân của Kế toán mua hàng - Gian lận Kickback!).
26. **Giai đoạn 4: Mở nút.** Giải thích quá trình điều tra.
27. **Giai đoạn 5: Giải quyết.** Đề xuất quy trình kiểm soát nội bộ mới (Action).
28. **Sức mạnh của Narrative:** Một đống số liệu khô khan bỗng hóa thành một cuộc điều tra phá án cực kỳ cuốn hút.

### Phần 4: Thiết kế Biểu đồ \& Tâm lý học Thị giác (Gestalt Principles) (9 Slides)
29. **Cây Quyết định Chọn Biểu đồ (Decision Tree):** Chọn sai biểu đồ giống như kể chuyện ma mà bật nhạc tấu hài. Xu hướng -> Dùng Line Chart; Cấu trúc -> Stacked Bar; Phân bổ -> Scatter Plot.
30. **Tâm lý học Thị giác (Gestalt):** Quy luật Sự gần gũi (Proximity). Những điểm nằm gần nhau tự động bị não gộp thành 1 nhóm, không cần vẽ vòng tròn dán nhãn.
31. **Quy luật Điểm nhấn (Focal Point):** Cách "thôi miên" sự chú ý của người xem.
32. **Ví dụ Điểm nhấn:** Biểu đồ doanh số các nước. Đừng tô màu sặc sỡ cầu vồng! Tô xám nhạt tất cả, và chỉ tô Đỏ đậm duy nhất cho quốc gia đang lỗ nặng. Mọi sự chú ý sẽ bị hút vào đó.
33. **Thiết kế Dashboards:** Bảng điều khiển ô tô không chớp nháy loạn xạ. Nó chỉ sáng đèn Đỏ "Check Engine" khi có sự cố. Dashboard tài chính cũng phải giảm thiểu sự lộn xộn (Clutter).
34. **Thuộc tính tiền chú ý (Preattentive attributes):** Kích thước (thể hiện quy mô) và Màu sắc (thể hiện tính chất).
35. **Lưu ý Nhân văn về Màu sắc:** Cấm kỵ dùng cặp Đỏ - Xanh lá cây! Khoảng 8% nam giới mắc chứng mù màu sẽ không thể phân biệt đâu là lãi, đâu là lỗ.
36. **Mô hình đọc chữ Z và F:** Mắt luôn bắt đầu từ góc trên cùng bên trái. Do đó, KPI cốt lõi nhất luôn phải nằm ở vị trí "Vàng" này.
37. **Nguyên tắc 5 Giây:** Dashboard thành công là khi sếp nhìn 5 giây phải biết ngay công ty đang tốt hay xấu, bộ phận nào đang gặp vấn đề.

### Phần 5: Những Cú Lừa Thị Giác \& Đạo đức Nghề nghiệp (8 Slides)
38. **Bẫy 1: Cắt xén trục tung (Omitting the baseline).** Cắt trục Y bắt đầu từ 90 thay vì 0. Sự sụt giảm rất nhỏ trông như một cú lao dốc thảm khốc. Bóp méo tỷ lệ!
39. **Bẫy 2: Đi ngược quy ước (Going against conventions).** Vẽ biểu đồ cột chi phí nhưng quy định "Cột càng dài là chi phí càng thấp". Đánh lừa não bộ trầm trọng.
40. **Bẫy 3: Trích xuất có chọn lọc (Cherry-picking).** Chỉ khoe số tổng 2 năm tăng trưởng, cố tình giấu biểu đồ từng tháng đang chồi sụt rủi ro. Giấu lỗ, khoe lãi.
41. **Bẫy 4: Dùng sai biểu đồ (Using the wrong graph).** Dùng Pie Chart để so sánh sự biến động doanh thu qua các năm. (Mắt người cực kém trong việc so sánh sự biến thiên diện tích).
42. **Ranh giới Đạo đức:** Vi phạm do thiếu kỹ năng hay cố ý thao túng? Hậu quả cuối cùng luôn là Sự mất niềm tin (Trust). Trong tài chính, mất niềm tin là mất tất cả.
43. **Rủi ro AI Tự động hóa:** Nếu giao cho Generative AI tự vẽ Dashboard, nó có thể tự cắt xén trục Y chỉ vì "trông cho nó kịch tính và đẹp mắt" mà không hiểu bối cảnh đạo đức kinh doanh.
44. **Lời khuyên chốt hạ:** Kế toán viên tương lai không chỉ là người vẽ biểu đồ. Bạn phải là người "Kiểm duyệt tư duy của máy móc", bảo vệ tính trung thực và khách quan của dữ liệu!
45. **Tổng kết \& Kết thúc học phần:** Ôn tập 3 thông điệp chính: Khám phá để tìm Insight - Kể chuyện để thuyết phục - Dùng hình ảnh chuẩn mực để bảo vệ sự trung thực. Cảm ơn sinh viên!
