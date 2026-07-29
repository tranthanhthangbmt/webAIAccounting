---
theme: "default"
title: "Day 12 LT: Đạo đức và Pháp lý khi ứng dụng AI"
author: "Giảng viên"
date: "2026"
---

# BUỔI 12: ĐẠO ĐỨC KẾ TOÁN VÀ PHÁP LÝ KHI ỨNG DỤNG AI

## Năng lực đạt được sau buổi học
- **Nhận thức Rủi ro:** Nhận diện được các rủi ro về bảo mật dữ liệu, thiên kiến thuật toán (bias) và trách nhiệm pháp lý khi sử dụng AI trong kế toán - kiểm toán.
- **Tuân thủ Đạo đức:** Ứng dụng các khuôn khổ đạo đức (như FAT: Fair, Accountable, Transparent) để đánh giá và lựa chọn công cụ AI phù hợp với chuẩn mực nghề nghiệp.
- **Kiểm soát Trách nhiệm:** Nắm vững nguyên tắc "Con người làm chủ" (Human Oversight), biết cách kiểm chứng quyết định của AI thay vì phụ thuộc hoàn toàn.
- **Tuân thủ Pháp lý:** Hiểu được sự tương tác giữa AI và luật pháp (như Luật Bảo vệ Dữ liệu Cá nhân), đặc biệt là quy định về trách nhiệm giải trình.

## Nội dung chương trình
1. Bảo mật Dữ liệu và Quyền Riêng tư (Data Privacy).
2. Thiên kiến Thuật toán và Sự Công bằng (Algorithmic Bias).
3. Tính Minh bạch và Khả năng Giải thích (Explainability).
4. Trách nhiệm Giải trình và Nghĩa vụ Pháp lý (Liability).
5. Sự Tương tác giữa AI và Quy định Pháp lý (Legal Regulations).
6. Khung Đạo đức FAT (Fair, Accountable, Transparent) trong Kế toán.

---

# PHẦN 1: BẢO MẬT DỮ LIỆU VÀ QUYỀN RIÊNG TƯ (DATA PRIVACY)

## 1.1 Tầm quan trọng của Bảo mật Dữ liệu
- AI định hình lại lĩnh vực kế toán, nhưng cũng mang theo những thách thức lớn về đạo đức.
- Kế toán viên nắm giữ dữ liệu tài chính nhạy cảm của doanh nghiệp và khách hàng.
- Khi cấp dữ liệu này cho AI (ví dụ: ChatGPT), nguy cơ rò rỉ thông tin là cực kỳ lớn.

## 1.2 Nguyên tắc Bảo mật khi dùng AI
- **Ẩn danh hóa dữ liệu (Anonymization):** Xóa tên công ty, số tài khoản, mã số thuế trước khi đưa vào AI.
- Tuân thủ các quy định bảo vệ dữ liệu hiện hành (ví dụ: GDPR, Luật An ninh mạng, Nghị định Bảo vệ Dữ liệu Cá nhân).
- Thiết lập các biện pháp an toàn mạnh mẽ để ngăn chặn truy cập trái phép.

## 1.3 Sự đồng ý của Khách hàng (Informed Consent)
- Khách hàng có quyền biết dữ liệu của họ đang được xử lý bởi AI.
- Kế toán viên phải xin phép và được sự đồng ý rõ ràng từ khách hàng.
- Cần thiết lập các chính sách minh bạch về việc thu thập, lưu trữ và sử dụng dữ liệu.

## 1.4 Quản lý vòng đời dữ liệu
- Dữ liệu đưa vào AI được lưu trữ ở đâu? Trên server của OpenAI hay máy chủ nội bộ?
- Xác định rõ thời hạn lưu trữ và chính sách tiêu hủy dữ liệu khi kết thúc dự án.
- Không sử dụng các mô hình AI công khai để huấn luyện dữ liệu nội bộ của công ty.

## 1.5 Rủi ro từ nhà cung cấp bên thứ ba
- Các phần mềm kế toán tích hợp AI thường do bên thứ ba cung cấp.
- Cần đánh giá kỹ lưỡng các điều khoản dịch vụ (Terms of Service) về quyền sở hữu dữ liệu.
- Đảm bảo rằng nhà cung cấp không bán hoặc sử dụng trái phép dữ liệu tài chính của bạn.

## 1.6 Xây dựng Môi trường AI an toàn (Secure AI)
- Đối với các tập đoàn lớn, nên triển khai AI trên môi trường Private Cloud hoặc On-Premise.
- Giới hạn quyền truy cập AI theo vai trò (Role-based access).
- Ghi nhật ký (Log) toàn bộ các câu lệnh (Prompts) liên quan đến dữ liệu nhạy cảm.

## 1.7 Khung Đạo đức Trí tuệ Nhân tạo
- Sử dụng AI không chỉ là vấn đề công nghệ mà là vấn đề đạo đức nghề nghiệp.
- Mọi quyết định giao cho AI xử lý dữ liệu phải đặt tính toàn vẹn (Integrity) lên hàng đầu.
- "Bảo mật không phải là rào cản, mà là nền tảng của niềm tin".

---

# PHẦN 2: THIÊN KIẾN THUẬT TOÁN (ALGORITHMIC BIAS)

## 2.1 Thiên kiến Thuật toán là gì?
- Thuật toán AI có thể vô tình đưa ra các kết quả sai lệch, dẫn đến sự phân biệt đối xử (Algorithmic Discrimination).
- Ví dụ: Một hệ thống AI chấm điểm tín dụng có thể tự động từ chối khoản vay của các doanh nghiệp thuộc một khu vực địa lý cụ thể do dữ liệu huấn luyện thiên lệch.

## 2.2 Nguồn gốc của Thiên kiến
- AI học từ dữ liệu lịch sử (Historical Data).
- Nếu dữ liệu lịch sử chứa đựng sự thiên vị của con người, AI sẽ khuếch đại sự thiên vị đó.
- Thiên kiến còn xuất phát từ người lập trình (lựa chọn thuật toán, cách gán nhãn dữ liệu).

## 2.3 Các loại Thiên kiến trong Kế toán & Tài chính
- **Thiên kiến Lấy mẫu (Sampling Bias):** Dữ liệu không đại diện cho toàn bộ đối tượng.
- **Thiên kiến Nhận thức (Cognitive Bias):** Mặc định tin rằng AI luôn đúng (Automation Bias).
- **Thiên kiến Thống kê:** Độ lệch chuẩn so với giá trị thực tế của quần thể.

## 2.4 Quá trình Phát triển AI và Thiên kiến
![Quá trình Phát triển AI](images/Day_12/docx_img_1.png)
- Rủi ro thiên kiến có thể xuất hiện ở mọi giai đoạn: Từ việc chuẩn bị mẫu, phát triển thuật toán, đến khi giao cho người dùng cuối.

## 2.5 Hậu quả của Thiên kiến AI
- Tạo ra các quyết định bất công (unfair) trong tuyển dụng, đánh giá hiệu suất, hoặc cấp tín dụng.
- Vi phạm các nguyên tắc nhân quyền và bình đẳng.
- Gây mất uy tín nghiêm trọng cho doanh nghiệp kế toán - kiểm toán sử dụng AI.

## 2.6 Cách giảm thiểu Thiên kiến (Mitigation)
- Liên tục kiểm toán (Audit) và giám sát các mô hình AI.
- Đảm bảo tính đa dạng (Diversity) của các nguồn dữ liệu đầu vào.
- Thiết lập cơ chế cảnh báo sớm khi phát hiện AI đưa ra các kết quả có tính phân biệt đối xử.

## 2.7 Đầu tư vào AI Trách nhiệm (Responsible AI)
- Các CEO coi việc giảm thiểu thiên kiến là chiến lược cốt lõi trong năm 2021 và các năm tiếp theo.
- Responsible AI không chỉ là đạo đức mà là một lợi thế cạnh tranh bền vững.

---

# PHẦN 3: TÍNH MINH BẠCH VÀ KHẢ NĂNG GIẢI THÍCH (EXPLAINABILITY)

## 3.1 Vấn đề "Hộp đen" của AI (Black Box)
- Nhiều hệ thống AI phức tạp (như Deep Learning) hoạt động như một "hộp đen".
- Kế toán viên nhận được kết quả nhưng không thể biết AI đã suy luận như thế nào để ra kết quả đó.
- Điều này đi ngược lại nguyên tắc rõ ràng và minh bạch trong kế toán.

## 3.2 Khả năng Giải thích (Explainability) là gì?
- Là khả năng của hệ thống AI trong việc cung cấp lý do cho một quyết định cụ thể.
- Giúp người dùng hiểu được logic đằng sau các con số AI tạo ra (Ví dụ: Tại sao AI lại dự báo doanh thu giảm 10%?).

## 3.3 Tầm quan trọng của Tính Minh bạch
- Tăng cường trách nhiệm giải trình (Accountability).
- Giúp các bên liên quan (Stakeholders) như cơ quan thuế, kiểm toán viên độc lập tin tưởng vào báo cáo tài chính.
- Là yêu cầu bắt buộc trong nhiều khung pháp lý hiện hành.

## 3.4 Yêu cầu về Tài liệu hóa (Documentation)
- Cần lưu trữ đầy đủ tài liệu về nguồn dữ liệu đã dùng để huấn luyện AI.
- Ghi chú lại các bước tiền xử lý dữ liệu (Pre-processing).
- Mô tả rõ kiến trúc mô hình AI được sử dụng.

## 3.5 Khung gỡ lỗi Hộp đen (XAI)
- Kỹ thuật XAI (Explainable AI) đang được phát triển để dịch các thuật toán phức tạp sang ngôn ngữ con người có thể hiểu.
- Các công cụ như LIME hoặc SHAP giúp xác định đặc trưng (feature) nào ảnh hưởng nhiều nhất đến quyết định của AI.

## 3.6 Đạo đức trong việc Từ chối AI
- Kế toán viên có quyền (và nghĩa vụ) từ chối sử dụng kết quả của AI nếu hệ thống đó không thể giải thích được cách nó hoạt động trong các tác vụ trọng yếu.

---

# PHẦN 4: TRÁCH NHIỆM GIẢI TRÌNH VÀ NGHĨA VỤ PHÁP LÝ (LIABILITY)

## 4.1 Ai là người chịu trách nhiệm?
- Khi AI đưa ra một tính toán sai dẫn đến phạt thuế, ai sẽ chịu trách nhiệm?
- Phần mềm AI? Công ty lập trình AI? Hay Kế toán viên?
- Theo pháp luật hiện hành, **Kế toán viên (người sử dụng)** luôn là người chịu trách nhiệm cuối cùng.

## 4.2 Giới hạn của AI (Limitations)
- AI không có tư cách pháp nhân (Legal Personality).
- Nó chỉ là công cụ hỗ trợ, không thể chịu trách nhiệm hình sự hay dân sự.
- Do đó, Kế toán viên phải hiểu rõ rủi ro và giới hạn của hệ thống AI mình đang dùng.

## 4.3 Trách nhiệm của Nhà phát triển phần mềm
- Dù kế toán viên chịu trách nhiệm pháp lý với khách hàng, nhà phát triển phần mềm vẫn có trách nhiệm liên đới nếu phần mềm có lỗi nghiêm trọng (Willful or negligent responsibility).
- Các hợp đồng sử dụng phần mềm AI thường có điều khoản giới hạn trách nhiệm (Limitation of Liability).

## 4.4 Quy trình Đánh giá Rủi ro
- Trước khi ứng dụng AI vào quy trình lõi, cần có bước đánh giá rủi ro toàn diện.
- Xác định những quyết định nào do AI tự động thực hiện (Automated Decision-Making - ADM).
- Tham vấn chuyên gia pháp lý về các rủi ro có thể phát sinh.

## 4.5 AI và Hệ quả Hình sự
- Việc sử dụng AI để gian lận sổ sách hoặc thao túng báo cáo tài chính vẫn bị truy cứu trách nhiệm hình sự đối với con người.
- Luật pháp ngày càng chú ý đến "Meta-surveillance" (Giám sát siêu dữ liệu) để phát hiện tội phạm kinh tế qua AI.

## 4.6 Bảo hiểm Trách nhiệm Nghề nghiệp
- Sự xuất hiện của AI đòi hỏi các công ty kế toán phải cập nhật lại chính sách Bảo hiểm Trách nhiệm Nghề nghiệp.
- Cần đảm bảo các sai sót do AI (nếu xảy ra) vẫn nằm trong phạm vi được bảo hiểm.

---

# PHẦN 5: VAI TRÒ CỦA CON NGƯỜI (HUMAN OVERSIGHT)

## 5.1 Con người làm chủ (Human-in-the-Loop)
- AI sinh ra để tự động hóa, nhưng không phải để tự trị hoàn toàn (Autonomous).
- Sự can thiệp và giám sát của con người là bắt buộc trong kế toán.
- Kế toán viên phải áp dụng Đánh giá Nghề nghiệp (Professional Judgment).

## 5.2 Kiểm chứng Kết quả AI (Validation)
- Đừng bao giờ tin tưởng tuyệt đối vào kết quả đầu ra của AI.
- Phải có quy trình đối chiếu, kiểm tra chéo (Cross-checking) các dữ liệu quan trọng.
- Sẵn sàng can thiệp hoặc ghi đè (override) quyết định của AI khi phát hiện dấu hiệu sai lệch.

## 5.3 Tránh sự Phụ thuộc Mù quáng (Automation Bias)
- Căn bệnh nguy hiểm nhất: "Máy tính nói thế nên chắc là đúng".
- Rèn luyện tư duy hoài nghi nghề nghiệp (Professional Skepticism).
- Nếu AI đưa ra một kết quả mâu thuẫn với kinh nghiệm kế toán, hãy dừng lại và điều tra.

## 5.4 Sự Tiến hóa của Năng lực (Continuous Learning)
- AI tiến hóa, Kế toán viên cũng phải tiến hóa.
- Cập nhật liên tục các kiến thức mới về AI, phương pháp tốt nhất (Best Practices) và hướng dẫn đạo đức.
- Tham gia các khóa đào tạo thường xuyên để không bị công nghệ bỏ lại phía sau.

## 5.5 Giao tiếp với Các bên liên quan (Stakeholder Engagement)
- Khởi xướng các cuộc thảo luận mở và minh bạch về AI trong tổ chức.
- Cùng Ban Lãnh đạo xây dựng Bộ quy tắc Ứng xử (Code of Conduct) về AI nội bộ.
- Truyền thông rõ ràng rủi ro và lợi ích cho toàn bộ nhân viên.

---

# PHẦN 6: SỰ TƯƠNG TÁC GIỮA AI VÀ PHÁP LÝ (LEGAL REGULATIONS)

## 6.1 Khung Đạo đức FAT
![Chiến lược AI Trách nhiệm](images/Day_12/docx_img_2.jpeg)
- Cộng đồng quốc tế đang thúc đẩy hệ thống AI dựa trên nguyên tắc **FAT**: Fair (Công bằng), Accountable (Trách nhiệm), Transparent (Minh bạch).

## 6.2 Vai trò của Dữ liệu Cá nhân (Data Protection)
- Quy định Bảo vệ Dữ liệu (như GDPR của Châu Âu) coi quyền bảo vệ dữ liệu cá nhân là Quyền Con người cơ bản (Fundamental Human Right).
- Kế toán viên vi phạm quy định này (ví dụ: đưa dữ liệu lương nhân viên lên ChatGPT) sẽ phải chịu phạt rất nặng.

## 6.3 Luật chống Phân biệt Đối xử
- Luật pháp cấm mọi hình thức phân biệt đối xử dựa trên thuật toán.
- Một phần mềm đánh giá tín dụng nếu loại bỏ khách hàng chỉ vì độ tuổi, giới tính sẽ bị coi là vi phạm pháp luật.

## 6.4 AI trong việc Thực thi Pháp luật (Predictive Policing)
- Công an và Cơ quan Thuế cũng đang dùng AI để "dự báo tội phạm" và "dự báo trốn thuế".
- Dữ liệu lịch sử sẽ giúp AI quét và đánh dấu rủi ro (Risk Profiling) đối với doanh nghiệp của bạn.
- Hiểu về AI giúp bạn chuẩn bị tốt hơn trước các đợt thanh tra thuế tự động.

## 6.5 Thay đổi Cấu trúc Việc làm
- AI Automation ảnh hưởng trực tiếp đến luật lao động.
- Nhiều doanh nghiệp sẽ sử dụng thuật toán AI để giám sát, đánh giá KPI và thậm chí là sa thải nhân viên.
- Quyền lợi xã hội và quyền cơ bản của con người trong thời đại số cần được quan tâm.

## 6.6 Tương lai của Luật AI (AI Law)
- Các quốc gia đang ráo riết ban hành các bộ Luật AI (ví dụ: EU AI Act).
- AI trong tài chính - kế toán sẽ bị xếp vào nhóm "Rủi ro cao" (High Risk), đòi hỏi phải kiểm định cực kỳ gắt gao trước khi sử dụng.
- Đón đầu các xu hướng pháp lý này là chìa khóa để tồn tại và phát triển.

---

# KẾT LUẬN

## 7.1 Lời kết Buổi 12
- Ứng dụng AI là một sức mạnh to lớn, và "Sức mạnh càng lớn, trách nhiệm càng cao".
- Đạo đức nghề nghiệp không thay đổi, chỉ là cách chúng ta áp dụng nó trong môi trường máy móc cần sự tinh tế hơn.
- Hãy là những kế toán viên dẫn đầu công nghệ, nhưng không bao giờ đánh mất sự chính trực (Integrity) của mình.

## CẢM ƠN CÁC BẠN ĐÃ LẮNG NGHE!
- Kết thúc phần Lý thuyết Day 12.
- Chuẩn bị cho phần Thực hành: Xác định thiên kiến và xử lý rủi ro bảo mật với các công cụ AI cụ thể!
