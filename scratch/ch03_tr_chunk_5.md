hiệu quả hơn và đưa ra các quyết định về chi phí/lợi nhuận. Mô hình tối ưu hóa phổ biến nhất được sử dụng trong kế toán là tối ưu hóa tuyến tính. Trong tối ưu hóa tuyến tính, mô hình bao gồm:
- **Các biến quyết định (Decision variables):** Các giá trị chưa biết mà mô hình tìm cách xác định.
- **Hàm mục tiêu (Objective function):** Phương trình toán học mô tả mục tiêu đầu ra cần giảm thiểu hoặc tối đa hóa.
- **Các ràng buộc (Constraints):** Các giới hạn, yêu cầu, hoặc các hạn chế khác phải được áp dụng cho bất kỳ giải pháp nào, chẳng hạn như các ràng buộc về nhu cầu, vật liệu hoặc lao động.

Đầu ra từ một mô hình tối ưu hóa tuyến tính sẽ hiển thị giải pháp tối ưu.

Ban quản lý của Super Scooters đã quyết định tiếp tục sản xuất cả hai mẫu Celeritas và Kicks trong ít nhất một năm nữa. Họ muốn biết nên sản xuất bao nhiêu đơn vị của mỗi mẫu để tối đa hóa số dư đảm phí (contribution margin). Họ đã dự báo nhu cầu cho mỗi mẫu:
- Captain: 18.000 chiếc.
- Celeritas: 10.000 chiếc.
- Kicks: 7.000 chiếc.
- Lazer: 24.000 chiếc.

Vì muốn tránh lượng hàng tồn kho dư thừa, họ không muốn sản xuất nhiều hơn mức họ dự kiến bán được. Ngoài ra cũng có một giới hạn về số giờ máy (machine hours) có sẵn trong năm.

Hình minh họa 3.24 cho thấy thông tin cần thiết để tạo một mô hình tối ưu hóa cho Super Scooters.

![ILLUSTRATION 3.24](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.24.png)

Chương trình tối ưu hóa tuyến tính sẽ sử dụng dữ liệu này để giải quyết số lượng tối ưu của mỗi mẫu cần được sản xuất, trong đó số dư đảm phí (hàm mục tiêu) được tối đa hóa tùy thuộc vào các ràng buộc. Lưu ý rằng chúng ta đã bắt đầu với một con số 1 tùy ý trong các ô số lượng đơn vị được sản xuất. Con số này cũng có thể là số 0 khi bắt đầu; tuy nhiên, việc sử dụng số 1 giúp chúng ta có thể xác nhận các công thức. Tính năng tối ưu hóa tuyến tính có sẵn trong Microsoft Excel Solver có thể minh họa cách hoạt động của các mô hình tối ưu hóa. Chương trình Solver được truy cập thông qua tab Data trên thanh công cụ ribbon (Hình minh họa 3.25).

![ILLUSTRATION 3.25](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.25.png)

Nhấp vào Solver sẽ mở ra một hộp thoại để nhập ô hàm mục tiêu, ô biến quyết định và tạo bất kỳ ràng buộc nào có liên quan. Hình minh họa 3.26 là hộp thoại Solver được sử dụng để tạo chương trình tối ưu hóa cho Super Scooters.

![ILLUSTRATION 3.26](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.26.png)

Khi tất cả các ràng buộc đã được nhập vào, hãy đánh dấu vào ô để đảm bảo kết quả của Solver không bị âm (chúng ta không thể "hủy sản xuất" một sản phẩm) và chọn Phương pháp giải (Solving Method) là Simplex LP, vì đây là một tối ưu hóa tuyến tính. Nhấp vào Solve sẽ tạo ra hộp thoại như trong Hình minh họa 3.27.

![ILLUSTRATION 3.27](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.27.png)

Hộp thoại này cho thấy Solver đã tìm thấy một giải pháp tối ưu thỏa mãn các ràng buộc. Lựa chọn mặc định là Keep Solver Solution (Giữ giải pháp của Solver). Nếu nút (radio button) này được chọn, bảng tính sẽ phản ánh số tiền mới của biến quyết định và số dư đảm phí tối ưu (Hình minh họa 3.28). Ngoài ra còn có sự lựa chọn để tạo ra ba báo cáo. Chọn báo cáo Answer (Câu trả lời) và nhấp OK.

![ILLUSTRATION 3.28](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.28.png)

Hình minh họa 3.29 là báo cáo Answer. Phần đầu tiên của báo cáo cho thấy giá trị ban đầu của hàm mục tiêu và sau đó là giá trị cuối cùng khi đạt được giải pháp tối ưu. Trong trường hợp này, sản lượng tối ưu sẽ là 18.000 xe tay ga Captain, 5.520 xe Celeritas, 7.000 xe Kicks, và 24.000 xe Lazer.

![ILLUSTRATION 3.29](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.29.png)

Phần giữa của báo cáo (Các ô Biến - Variable Cells) cho thấy giá trị cuối cùng của các biến quyết định (Hình minh họa 3.30). Nó cho thấy số lượng xe tay ga mỗi mẫu mà Super Scooters nên bán để đạt được mức số dư đảm phí tối đa.

![ILLUSTRATION 3.30](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.30.png)

Cuối cùng, phần cuối của báo cáo cho thấy mức độ sử dụng các ràng buộc trong giải pháp tối ưu (Hình minh họa 3.31). Cột Status (Trạng thái) chỉ ra liệu ràng buộc có bị ràng buộc chặt (binding) hay không bị ràng buộc (not binding). Nói cách khác, việc sản xuất thêm là không thể nếu không có sự gia tăng trong mức giới hạn của ràng buộc đó. Số lượng hiển thị trong cột Slack đại diện cho số lượng của ràng buộc còn lại sau giải pháp tối ưu.

![ILLUSTRATION 3.31](../TaiLieu/textbookForPractice/Figures/Ch_03/ILLUSTRATION%203.31.png)

Vì số giờ máy là có hạn, mô hình tối ưu đưa ra cách tốt nhất để sử dụng những giờ đó nhằm tối đa hóa số dư đảm phí là sản xuất tất cả những gì Super Scooters có thể bán cho các mẫu Captain, Kicks và Lazer và sản xuất ít hơn 4.480 chiếc so với nhu cầu của mẫu Celeritas. Bất kỳ sự kết hợp nào khác sẽ dẫn đến số dư đảm phí thấp hơn so với mô hình tối ưu.

#### Phân tích What-if (What-if Analyses)

Một mô hình bảng tính đánh giá những thay đổi và các tổ hợp cụ thể của các đầu vào và giả định của mô hình được gọi là phân tích what-if. Phân tích what-if là một cách dễ dàng để thay đổi các giá trị trong bảng tính và tính toán lại các đầu ra. Microsoft Excel có ba công cụ được tích hợp trong tab Data ở dưới mục What-if Analyses. Hai trong số các công cụ này – Scenario Manager (Quản lý kịch bản) và Goal Seek (Tìm kiếm mục tiêu) – là những công cụ hữu ích để tạo điều kiện cho các phân tích what-if. Chúng ta sẽ thảo luận về từng công cụ trong một chương sau, nhưng đây là một lời giải thích ngắn gọn:
- **Scenario Manager** trong Excel cho phép thay đổi hoặc thay thế các giá trị đầu vào cho nhiều ô (tối đa 32). Do đó, kết quả của các giá trị đầu vào hoặc các kịch bản khác nhau có thể được xem xét cùng một lúc.
- **Goal Seek** được sử dụng khi kết quả mong muốn đã được biết trước nhưng giá trị đầu vào để đạt được kết quả đó thì chưa. Goal Seek bị giới hạn vì nó chỉ có thể sử dụng một biến đầu vào. Nếu phân tích đang được thực hiện yêu cầu nhiều hơn một biến thay đổi, thì một mô hình tối ưu hóa sử dụng Excel Solver là cần thiết. Ví dụ, mô hình tối ưu hóa của Super Scooters có nhiều hơn một biến vì cần phải xem xét các ràng buộc về nhu cầu và số giờ máy.

---

### Ứng dụng 3.5 (Apply It 3.5)
**Đề xuất Tổ hợp Bán hàng Tối ưu (Prescribe Optimal Sales Mix)**

> **Data** **Kế toán Quản trị (Managerial Accounting)** Bạn là một kế toán viên quản trị cho Best Bakes Bakery và được yêu cầu chuẩn bị một bản phân tích để xác định tổ hợp sản phẩm (mix of products) tối ưu nhằm tối đa hóa lợi nhuận. Bạn đã được cung cấp các giao dịch bán hàng cho các năm 2022–2025. Bên cạnh dữ liệu bán hàng trước đó, bạn biết rằng có một số ràng buộc về nguồn lực (chẳng hạn như vật tư hoặc giờ lao động) nên được đưa vào phân tích.

**Yêu cầu:**
1. Mục tiêu của phân tích là gì?
2. Phát triển ba câu hỏi phù hợp với mục tiêu.
3. Bạn sẽ sử dụng những phân tích nào để trả lời ba câu hỏi này?

**GIẢI PHÁP (SOLUTION)**
1. Mục tiêu là xác định tổ hợp bán hàng (sales mix) tối ưu của các sản phẩm dựa trên các nguồn lực có sẵn.
2. Ba câu hỏi:
   - Các ràng buộc về nguồn lực nào nên được đưa vào quyết định?
   - Yêu cầu về nguồn lực cho mỗi sản phẩm là gì?
   - Lợi nhuận dự kiến cho mỗi sản phẩm là bao nhiêu?
3. Tối ưu hóa tuyến tính có thể được sử dụng để xác định sự kết hợp tốt nhất của các sản phẩm để đạt được lợi nhuận tối đa.

---

## 3.6 Động lực và Mục tiêu Phân tích Dữ liệu trong Thực tiễn Nghề nghiệp là gì?

**MỤC TIÊU HỌC TẬP 6 (LEARNING OBJECTIVE 6)**
**Mô tả các động lực và mục tiêu cho phân tích dữ liệu trong thực tiễn nghề nghiệp.**

Trong khi các phương pháp phân tích – mô tả, chẩn đoán, dự đoán và đề xuất – là giống nhau trên các lĩnh vực kế toán, mục tiêu của dự án và những gì thúc đẩy chúng có thể khác nhau do có nhiều mục đích và các bên liên quan khác nhau. Trong kiểm toán, các bên liên quan phần lớn là từ bên ngoài (ví dụ: các cổ đông, các cơ quan quản lý), trong khi các bên liên quan trong kế toán quản trị chủ yếu là từ nội bộ (ví dụ: ban quản lý, nhân viên). Quan điểm của họ giúp xác định mục tiêu và phát triển các câu hỏi tốt.
