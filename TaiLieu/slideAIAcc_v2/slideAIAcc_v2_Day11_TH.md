---
theme: "default"
title: "Day 11 TH: Kỹ thuật Tóm tắt Văn bản Phức tạp với AI"
author: "Giảng viên"
date: "2026"
---

# BUỔI 11 THỰC HÀNH: SỬ DỤNG AI ĐỂ TÓM TẮT VÀ TRÍCH XUẤT DỮ LIỆU TỪ VĂN BẢN PHÁP LUẬT

## Năng lực đạt được sau buổi học
- **Kỹ năng Prompting:** Thành thạo việc xây dựng câu lệnh (Prompt) để tóm tắt các văn bản pháp luật phức tạp, dài dòng (Luật, Thông tư, Nghị định).
- **Kỹ năng Trích xuất:** Biết cách yêu cầu AI trích xuất chính xác các điều kiện cụ thể (ví dụ: điều kiện được khấu trừ thuế, quy định về hóa đơn).
- **Tư duy Phản biện:** Rèn luyện khả năng kiểm chứng chéo (cross-check) thông tin do AI cung cấp với văn bản gốc để phát hiện "ảo giác" (hallucinations).
- **Tự động hóa công việc:** Tiết kiệm thời gian tra cứu và áp dụng văn bản pháp luật vào xử lý tình huống kế toán thực tế.

## Nội dung chương trình
1. Giới thiệu Kỹ thuật Tóm tắt Văn bản Phức tạp với AI
2. Thực hành 1: Tóm tắt nhanh văn bản Thông tư dài
3. Thực hành 2: Trích xuất Điều kiện Khấu trừ Thuế
4. Kỹ thuật Tinh chỉnh Prompt (Refining Prompts)
5. Bài tập Thực hành Độc lập (Sinh viên tự làm)
6. Kiểm chứng Thông tin & Quản trị Rủi ro
7. Tổng kết & Đánh giá

---

# PHẦN 1: GIỚI THIỆU KỸ THUẬT TÓM TẮT VĂN BẢN PHỨC TẠP VỚI AI

## 1.1 Vấn đề của Văn bản Pháp luật Thuế
- Văn bản pháp luật (như Luật Quản lý Thuế, Thông tư 200) thường có hàng trăm trang.
- Ngôn ngữ mang tính hàn lâm, pháp lý, gây khó khăn cho việc đọc hiểu nhanh.
- Một quy định có thể nằm rải rác ở nhiều điều khoản, chương mục khác nhau.

## 1.2 Giải pháp từ Trí tuệ Nhân tạo (AI)
- AI như ChatGPT có khả năng Xử lý Ngôn ngữ Tự nhiên (NLP) cực mạnh.
- "Đọc" một tài liệu 50 trang chỉ trong vài giây.
- Khả năng cô đọng thông tin cốt lõi mà không làm mất đi ý nghĩa pháp lý gốc.

## 1.3 Cơ chế Tóm tắt của AI (Summarization)
- AI không chỉ "cắt xén" câu chữ, mà nó hiểu cấu trúc ngữ nghĩa (Semantic Understanding).
- Tóm tắt có thể theo 2 dạng: Extractive (Trích xuất nguyên văn) hoặc Abstractive (Diễn đạt lại).
- Trong kế toán thuế, chúng ta ưu tiên kết hợp cả 2: Diễn đạt lại cho dễ hiểu nhưng phải trích xuất đúng các điều kiện pháp lý.

## 1.4 Lợi ích khi dùng AI tóm tắt văn bản
- Rút ngắn 90% thời gian nghiên cứu luật.
- Dễ dàng truyền đạt quy định thuế phức tạp cho Ban Giám đốc (những người không chuyên về kế toán).
- Tránh bỏ sót các quy định "ẩn" trong văn bản dài.

---

# PHẦN 2: THỰC HÀNH 1 - TÓM TẮT NHANH VĂN BẢN THÔNG TƯ DÀI

## 2.1 Chuẩn bị Dữ liệu (Dataset)
- Chúng ta sẽ sử dụng một đoạn trích từ **Thông tư 78/2014/TT-BTC** (hoặc Thông tư 96 sửa đổi) về Thuế TNDN.
- Giảng viên đã chuẩn bị sẵn file text cho đoạn văn bản này.
- **Yêu cầu:** Mở file text và Copy toàn bộ nội dung.

## 2.2 Công thức Prompt Tóm tắt Cơ bản
- Đừng chỉ nói: "Hãy tóm tắt đoạn này."
- Hãy dùng cấu trúc: **[Vai trò] + [Hành động] + [Định dạng đầu ra] + [Dữ liệu đầu vào]**
- Ví dụ: "Đóng vai chuyên gia tư vấn thuế, hãy tóm tắt văn bản sau bằng các gạch đầu dòng ngắn gọn."

## 2.3 Viết Prompt Thực tế
- **Prompt:** "Tôi là một kế toán viên mới ra trường. Dưới đây là đoạn quy định về các khoản chi phí không được trừ khi tính thuế TNDN. Hãy tóm tắt lại bằng ngôn ngữ dễ hiểu nhất, chia làm 3 ý chính. [Dán văn bản vào đây]"
- Hãy thử chạy Prompt này trên ChatGPT hoặc Copilot.

## 2.4 Phân tích Kết quả
- Bạn thấy kết quả của AI thế nào? Dễ hiểu hơn bản gốc chứ?
- Chú ý xem AI có chia đúng 3 ý chính như bạn yêu cầu không.
- Nếu kết quả còn quá dài, hãy yêu cầu AI: "Hãy làm cho nó ngắn hơn nữa, tối đa 100 chữ."

## 2.5 Kỹ thuật "Format Instructions" (Chỉ định Định dạng)
- Bạn có thể yêu cầu AI xuất kết quả dưới dạng Bảng (Table).
- **Prompt:** "Hãy chuyển đoạn tóm tắt vừa rồi thành một bảng gồm 2 cột: Cột 1 là 'Loại Chi phí', Cột 2 là 'Giải thích ngắn gọn'."
- Việc dùng bảng giúp thông tin trực quan và dễ tra cứu hơn rất nhiều.

---

# PHẦN 3: THỰC HÀNH 2 - TRÍCH XUẤT ĐIỀU KIỆN KHẤU TRỪ THUẾ

## 3.1 Trích xuất Dữ liệu (Data Extraction) là gì?
- Thay vì tóm tắt toàn bộ, bạn chỉ muốn "moi" ra một mẩu thông tin cụ thể từ một mớ bòng bong.
- Ví dụ: Trong 10 trang quy định, tôi chỉ muốn biết "Điều kiện để được khấu trừ thuế GTGT đầu vào là gì?"

## 3.2 Tình huống Thực tế
- Doanh nghiệp bạn vừa mua một xe ô tô 9 chỗ ngồi trị giá 2 tỷ đồng.
- Kế toán trưởng yêu cầu bạn kiểm tra xem phần thuế GTGT của xe này có được khấu trừ toàn bộ không.

## 3.3 Viết Prompt Trích xuất
- **Prompt:** "Dựa trên quy định của Luật Thuế GTGT hiện hành tại Việt Nam, hãy cho tôi biết: Điều kiện khấu trừ thuế GTGT đầu vào đối với ô tô chở người từ 9 chỗ ngồi trở xuống là gì? Mức khống chế là bao nhiêu? Hãy trích dẫn cơ sở pháp lý."

## 3.4 Kỹ thuật Ràng buộc Context (Ngữ cảnh)
- Để tránh AI trả lời sai (hallucination) dựa trên luật của Mỹ hay nước khác, bạn phải ép ngữ cảnh.
- Cụm từ: *"Dựa trên quy định của Luật Thuế GTGT hiện hành tại Việt Nam"* là cực kỳ quan trọng.
- Hoặc an toàn hơn: Copy đoạn văn bản luật tiếng Việt dán vào và nói *"Chỉ dựa vào đoạn văn bản dưới đây, hãy..."*

## 3.5 Phân tích Kết quả của AI
- AI sẽ trả lời: Mức khống chế khấu trừ thuế GTGT đối với ô tô từ 9 chỗ trở xuống là 1,6 tỷ đồng (trừ trường hợp kinh doanh vận tải).
- Hãy kiểm tra xem AI có trích dẫn đúng tên văn bản không (Ví dụ: Khoản 3 Điều 14 Thông tư 219/2013/TT-BTC).

---

# PHẦN 4: KỸ THUẬT TINH CHỈNH PROMPT (REFINING PROMPTS)

## 4.1 Tại sao cần tinh chỉnh?
- Hiếm khi bạn nhận được câu trả lời hoàn hảo ngay ở Prompt đầu tiên.
- AI cần sự tương tác qua lại (Conversational AI).
- Tinh chỉnh giúp AI đi đúng hướng và đáp ứng chính xác nhu cầu chuyên môn sâu của bạn.

## 4.2 Kỹ thuật "Hỏi sâu hơn" (Drill-down)
- Khi AI đưa ra danh sách các điều kiện, nếu có điều kiện nào bạn chưa hiểu, hãy hỏi tiếp.
- **Prompt:** "Ở điều kiện số 2 bạn vừa nêu (phải có chứng từ thanh toán không dùng tiền mặt), xin hãy giải thích rõ thế nào là thanh toán không dùng tiền mặt? Có bao gồm bù trừ công nợ không?"

## 4.3 Kỹ thuật Yêu cầu Ví dụ (Ask for Examples)
- Luật thuế thường rất trừu tượng. Ví dụ là cách tốt nhất để hiểu.
- **Prompt:** "Hãy đưa ra một ví dụ bằng số liệu cụ thể về cách tính mức khấu trừ thuế GTGT đối với ô tô trị giá 2 tỷ mà bạn vừa đề cập ở trên."
- AI sẽ tự động đóng vai và lập một bài toán nhỏ để bạn hiểu.

## 4.4 Kỹ thuật So sánh (Comparison)
- Kế toán thường hay nhầm lẫn giữa các quy định.
- **Prompt:** "Hãy lập bảng so sánh sự khác nhau về điều kiện khấu trừ thuế giữa Thuế GTGT đầu vào và Thuế TNDN đối với khoản chi phí công tác phí cho nhân viên."
- AI cực kỳ giỏi trong việc gom nhóm và so sánh các đặc điểm.

---

# PHẦN 5: BÀI TẬP THỰC HÀNH ĐỘC LẬP

## 5.1 Đề bài cho Sinh viên
- Giảng viên chia lớp thành các nhóm nhỏ 2-3 người.
- **Tài liệu:** Một đoạn văn bản dài 3 trang trích từ Thông tư hướng dẫn về Thuế Thu nhập Cá nhân (TNCN) đối với các khoản phụ cấp, trợ cấp.
- **Nhiệm vụ:** Trong thời gian 15 phút, sử dụng AI để giải quyết 3 yêu cầu.

## 5.2 Yêu cầu 1: Tóm tắt
- Viết một Prompt yêu cầu AI tóm tắt 3 trang tài liệu trên thành đúng 1 đoạn văn (tối đa 150 chữ).
- Đoạn văn phải tóm lược được tinh thần chính: Khoản phụ cấp nào chịu thuế, khoản nào không.

## 5.3 Yêu cầu 2: Trích xuất Bảng dữ liệu
- Viết Prompt yêu cầu AI trích xuất tất cả các khoản phụ cấp được nhắc đến trong văn bản.
- Trình bày dưới dạng Bảng với 3 cột: STT, Tên Khoản Phụ cấp, Tình trạng (Chịu thuế / Miễn thuế).

## 5.4 Yêu cầu 3: Tư vấn Tình huống
- Giả định công ty A trợ cấp tiền ăn trưa cho nhân viên là 1.000.000 VNĐ/tháng bằng tiền mặt.
- Hãy dùng AI để kiểm tra xem khoản này có bị tính vào Thu nhập chịu thuế TNCN không, dựa vào chính văn bản vừa cung cấp.

## 5.5 Chấm điểm & Trình bày
- Các nhóm báo cáo lại Câu lệnh (Prompt) mình đã dùng.
- Nhóm nào có Prompt hay nhất, ra kết quả chính xác và định dạng đẹp nhất (bảng biểu rõ ràng) sẽ đạt điểm cao.
- Chia sẻ bài học rút ra khi giao tiếp với AI.

---

# PHẦN 6: KIỂM CHỨNG THÔNG TIN & QUẢN TRỊ RỦI RO

## 6.1 Mối nguy hiểm của AI trong Pháp lý
- AI có xu hướng muốn "làm hài lòng" người dùng.
- Nếu không biết câu trả lời, AI có thể tự sáng tác ra một điều luật (Hallucination).
- Trong ngành Kế toán - Thuế, sai 1 con số luật có thể dẫn đến hậu quả tài chính nặng nề.

## 6.2 Nguyên tắc Không Tin Tưởng Tuyệt Đối (Zero Trust)
- Bất cứ thông tin luật nào AI xuất ra, phải coi đó là **bản nháp** hoặc **gợi ý**.
- KHÔNG BAO GIỜ mang nguyên văn kết quả của AI đưa vào hồ sơ quyết toán thuế hay tư vấn cho Giám đốc mà chưa kiểm chứng.
- "Trust, but Verify" (Tin tưởng, nhưng phải xác minh).

## 6.3 Cách thức Kiểm chứng Chéo (Cross-checking)
- Khi AI nói "Theo Điều 4, Thông tư 96/2015/TT-BTC...", bạn hãy mở đúng văn bản đó trên trang web của Thư viện Pháp luật hoặc Cổng thông tin Bộ Tài chính để đọc lại.
- Dùng chức năng `Ctrl + F` trong file gốc để tìm các từ khóa mà AI đã trích xuất.
- Đảm bảo AI không bỏ sót các trường hợp ngoại lệ (Exceptions) rất hay có trong luật thuế.

## 6.4 Tự động hóa an toàn
- Hãy mớm sẵn dữ liệu (Feeding Data): Copy nội dung luật chuẩn từ file PDF/Word của bạn và đưa cho AI, thay vì để AI tự lục lọi trên internet.
- Điều này giới hạn sự "sáng tạo" của AI và buộc nó bám sát vào cơ sở pháp lý chính thống của doanh nghiệp.

---

# PHẦN 7: TỔNG KẾT & ĐÁNH GIÁ

## 7.1 Những gì chúng ta đã đạt được hôm nay?
- Biết cách sử dụng AI (ChatGPT) như một công cụ đắc lực để xử lý văn bản pháp luật dày đặc.
- Nắm vững 3 kỹ thuật cốt lõi: Tóm tắt (Summarization), Trích xuất (Extraction), và Tinh chỉnh (Refining).
- Hiểu được ranh giới giữa việc dùng AI để tăng năng suất và rủi ro đạo đức nghề nghiệp khi tin tưởng mù quáng vào AI.

## 7.2 Lời khuyên cho Kế toán viên tương lai
- AI sẽ không thay thế kế toán viên.
- Người kế toán viên biết dùng AI sẽ thay thế người không biết dùng.
- Hãy rèn luyện kỹ năng đặt câu hỏi (Prompting) mỗi ngày, từ những việc nhỏ nhất.

## 7.3 Giải đáp Thắc mắc (Q&A)
- Học viên chia sẻ khó khăn khi sử dụng các công cụ AI trong buổi học hôm nay.
- Giảng viên giải đáp và hướng dẫn khắc phục các lỗi cơ bản khi Prompting.

## CẢM ƠN CÁC BẠN ĐÃ LẮNG NGHE!
- Kết thúc Buổi 11 Thực hành.
- Chúc các bạn làm chủ AI và nâng cao hiệu suất làm việc!
