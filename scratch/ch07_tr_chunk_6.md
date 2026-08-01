7.3  Dữ liệu được khám phá bằng cách tích hợp các mối quan hệ dữ liệu như thế nào?  7-27
7.3  Dữ liệu được khám phá bằng cách tích hợp như thế nào 
Mối quan hệ dữ liệu?
MỤC TIÊU HỌC TẬP ❸
Khám phá dữ liệu bằng cách tích hợp các mối quan hệ nền tảng.
Trong khi các mẫu từ 1 đến 8 khám phá mối quan hệ dữ liệu cơ bản, duy nhất với một
Ngoài ra, việc khám phá dữ liệu thường yêu cầu tích hợp hai hoặc nhiều mối quan hệ dữ liệu. Dữ liệu tích hợp 
các mối quan hệ có thể được biểu diễn bằng một hình ảnh trực quan duy nhất hoặc bằng cách sử dụng các hình ảnh trực quan khác nhau 
như một phần của báo cáo. Xu hướng tổng hợp và phân tích Pareto là hai ví dụ về dữ liệu kết hợp 
mối quan hệ có thể được thể hiện trong một biểu đồ, cả hai đều được thảo luận tiếp theo.
Mẫu khám phá dữ liệu 9: Xu hướng tổng hợp
Mối quan hệ dữ liệu xu hướng tổng hợp hoặc sự thay đổi trong mối quan hệ từng phần với toàn bộ 
thời gian, là mối quan hệ dữ liệu tích hợp thường được phân tích. Một ví dụ là phân tích về 
kết hợp bán hàng của doanh nghiệp thay đổi như thế nào theo thời gian:
• Cơ cấu doanh thu là tỷ lệ tương đối của từng sản phẩm trong tổng doanh thu của doanh nghiệp, nghĩa là 
rằng đó là mối quan hệ một phần với toàn bộ.
• Thay đổi theo thời gian là một chuỗi thời gian.
Chúng tôi khám phá cơ cấu doanh thu của HNA để minh họa mối quan hệ này, nhưng hãy nhớ rằng có 
nhiều ví dụ kinh doanh và kế toán khác về các xu hướng tổng hợp, chẳng hạn như những thay đổi trong 
cấu trúc của một danh mục đầu tư hoặc cách các tài khoản khác nhau trong báo cáo kết quả hoạt động kinh doanh 
thay đổi theo thời gian.
Cấu trúc thăm dò các xu hướng tổng hợp có ba biến và kết hợp 
cấu trúc khám phá của mối quan hệ dữ liệu chuỗi thời gian và mối quan hệ dữ liệu từng phần với toàn bộ 
(Minh họa 7.37).
MINH HỌA 7.37  Khám phá 
Cấu trúc cho xu hướng tổng hợp 
Mối quan hệ dữ liệu
Đơn vị thời gian
Biến
Đơn vị thời gian dùng để
phân tích.
số
Biến
Biến xác định
toàn bộ bị hỏng như thế nào
xuống từng phần.
danh nghĩa
Biến
Biến
được
phân tích
Toàn bộ hoặc
số được
bị phá vỡ.
Cấu trúc thăm dò chuỗi thời gian
Cấu trúc thăm dò toàn bộ

![ILLUSTRATION 7.37](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.37.png)

7-28  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
Trực quan hóa
Một số hình ảnh trực quan, tất cả đều dựa trên cấu trúc thăm dò được hiển thị trong Hình minh họa 7.37, 
có thể khám phá các xu hướng tổng hợp. Trong Hình minh họa 7.38, biểu đồ vùng xếp chồng được sử dụng để khám phá 
những thay đổi trong cơ cấu doanh số bán hàng của HNA.
MINH HỌA 7.38  Khám phá 
Những thay đổi trong cơ cấu doanh số bán hàng của HNA với 
Biểu đồ vùng xếp chồng
Năm
0
500.000
1.000.000
1.500.000
2.000.000
2021
2022
2023
2024
2025
Đơn vị đã bán
Biểu đồ khu vực xếp chồng hiển thị các thay đổi
trong cơ cấu doanh số bán hàng của HNA: 2021‒2025
438.424
446.870
544.880
290.695
174.884
178.652
87.784
442,106
567.998
316.593
177.853
179.252
98.890
673.000
563.873
334.996
172.980
186.042
110.988
736.294
664.526
350.096
158.831
172.419
142.972
551.868
311.306
213.893
181.442
1.774.263
1.723.765
1.782.692
2.041.879
2.225.138
hiệp định
dân sự
CR-V
Odyssey
Phi công
Đường sườn núi
MINH HỌA 7.39  Power BI 
Định nghĩa biểu đồ vùng xếp chồng
Trục
Năm
Giá trị
Đơn vị đã bán
Đơn vị thời gian
Biến
Đơn vị thời gian dùng để
phân tích.
Biến xác định
toàn bộ bị hỏng như thế nào
xuống từng phần.
danh nghĩa
Biến
số
Biến
Biến
được
đã phân tích.
Toàn bộ hoặc
số được
bị phá vỡ.
Truyền thuyết
người mẫu
Cấu trúc thăm dò chuỗi thời gian
Cấu trúc thăm dò toàn bộ
Hình minh họa 7.39 cho thấy cách xây dựng biểu đồ này với Power BI.

![ILLUSTRATION 7.39](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.39.png)

7.3  Dữ liệu được khám phá bằng cách tích hợp các mối quan hệ dữ liệu như thế nào?  7-29
Có một số điều cần lưu ý về Hình minh họa 7.38:
• Phần trên cho thấy tổng số đơn vị đã bán (biến số) đã thay đổi như thế nào trong thời gian 
Giai đoạn 2021–2025 (biến đơn vị thời gian).
• Mỗi năm, tổng số đơn vị bán ra (biến số) được chia theo mẫu (danh nghĩa-
biến đầu vào).
• Các dải ngang cho biết thị phần của từng mẫu xe đã thay đổi như thế nào trong giai đoạn 2021–2025 
thời kỳ (xu hướng tổng hợp).
• Mặc dù các nhãn dữ liệu rất hữu ích nhưng các cột xếp chồng lên nhau gây khó khăn cho việc hiểu
chịu được những thay đổi chính xác cho hầu hết các mô hình.
Biểu đồ cột xếp chồng 100% (Minh họa 7.40) sử dụng cùng một dữ liệu được tạo trong Power BI 
theo cùng một cách.
MINH HỌA 7.40  Khám phá 
Cơ cấu doanh số bán hàng của HNA đạt 100% 
Biểu đồ cột xếp chồng
100%
60%
80%
17,55%
10,23%
4,36%
12,06%
31,10%
40%
20%
2021
2022
Đơn vị đã bán
Biểu đồ cột xếp chồng 100% hiển thị các thay đổi trong
Cơ cấu doanh số bán hàng của HNA: 2021‒2025
Năm
0%
2023
2024
2025
hiệp định
dân sự
CR-V
Odyssey
Phi công
Đường sườn núi
24,71%
16,86%
10,36%
5,09%
10,15%
31,61%
25,92%
17,76%
10,06%
5,55%
9,98%
31,86%
24,80%
16,41%
8,47%
9,11%
5,44%
32,96%
27,62%
15,73%
7,14%
7,75%
6,43%
33,09%
29,86%
Mặc dù các nhãn dữ liệu trong biểu đồ xếp chồng 100% được hiển thị trong Hình minh họa 7.40 chính xác hơn, 
biểu đồ này không còn hiển thị xu hướng chung nữa.
Khám phá và hiểu biết sâu sắc
Xu hướng tổng hợp có thể được khám phá cho bất kỳ sự kết hợp nào của các biện pháp (biến số), 
thứ nguyên (biến danh nghĩa) và đơn vị thời gian bằng cách kéo và thả.
Biểu đồ vùng xếp chồng trong Hình minh họa 7.38 tích hợp ba thông tin chi tiết:
• Nó nêu bật những thay đổi về số lượng căn bán được trong giai đoạn 2021–2025 (thời gian 
loạt). Biểu đồ đường trong Hình minh họa 7.32 thể hiện cùng một xu hướng chung và cả hai biểu đồ đều 
cung cấp thông tin chi tiết tương tự: doanh số bán thiết bị của HNA có xu hướng tăng lên bắt đầu từ năm 2023.
• Nó cho thấy mỗi mô hình đóng góp bao nhiêu vào tổng số hàng năm (một phần so với toàn bộ). Vào năm 2025, 
mẫu xe Civic là mẫu xe bán chạy nhất, tiếp theo là mẫu Accord.
• Nhãn dữ liệu và vùng bóng mờ cho biết liệu các mô hình đã trở nên nhập khẩu nhiều hay ít
kiến trong cơ cấu doanh số bán hàng trong giai đoạn 2021–2025 (xu hướng tổng hợp). mô hình Accord 
ngày càng trở nên quan trọng trong khi mô hình Odyssey trở nên ít quan trọng hơn.
So sánh những thông tin này với thông tin chi tiết từ biểu đồ cột xếp chồng 100%:
• Nó không thể hiện xu hướng chung.
• Nó cho thấy tỷ trọng chính xác mà mỗi mô hình đóng góp vào tổng số hàng năm (một phần so với toàn bộ). 33,09% 
trong số ô tô bán ra vào năm 2025 là Civic và 29,86% số ô tô bán ra trong cùng năm là Accord.

![ILLUSTRATION 7.40](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.40.png)

7-30  CHƯƠNG 7  Phân tích: Khám phá dữ liệu
• Được biểu thị dưới dạng phần trăm, nó cho thấy thị phần của một mẫu xe trong cơ cấu doanh số bán hàng đã thay đổi như thế nào 
trong giai đoạn 2021–2025. Thị phần của mẫu xe Accord đã tăng từ 31,1% vào năm 2021 lên 
33,09% vào năm 2025.
Việc áp dụng mô hình xu hướng tổng hợp cũng có thể cung cấp thông tin chi tiết cho doanh nghiệp khám phá cách thức 
sự đóng góp của các khu vực khác nhau (biến danh nghĩa) vào doanh thu (biến số) 
đã thay đổi trong 5 năm qua (biến đơn vị thời gian). Một mô hình xu hướng tổng hợp cũng có thể 
cho thấy tầm quan trọng tương đối của các tài khoản khác nhau trong báo cáo kết quả hoạt động kinh doanh đã thay đổi như thế nào 
trong một thời kỳ cụ thể. Đây là sự kết hợp giữa chiều dọc (từng phần) và chiều ngang (thời gian). 
loạt) phân tích báo cáo tài chính.
Mẫu khám phá dữ liệu 10: Phân tích Pareto
Phân tích Pareto (Minh họa 7.41) xác định tầm quan trọng của các danh mục khác nhau, trong đó 
là so sánh danh nghĩa, xếp hạng chúng và cho thấy mỗi thứ, dựa trên thứ hạng đó, đóng góp như thế nào 
theo tỷ lệ phần trăm tích lũy (một phần trên toàn bộ).
Biến số đó
quyết định sự đóng góp
theo tỷ lệ phần trăm tích lũy.
Biến số được sử dụng
để so sánh và xếp hạng
biến danh nghĩa.
số
Biến:
tích lũy
Giá trị
số
Biến:
Giá trị
danh nghĩa
Biến
Những danh mục nào đang được
đã phân tích.
MINH HỌA 7.41  Cấu trúc thăm dò để phân tích Pareto
Trực quan hóa
Biểu đồ Pareto trực quan hóa sự kết hợp của các mối quan hệ được hiển thị trong cấu trúc khám phá.
ture. Một số công cụ, như Excel, cung cấp biểu đồ Pareto. Chúng cũng có thể được tạo dưới dạng dòng và cột 
biểu đồ, được hỗ trợ bởi hầu hết các công cụ. ( Data How To 7.2. chỉ ra cách tạo Pareto 
biểu đồ bằng cả Power BI và Excel.)
Ở đây, biểu đồ đường và cột được tạo bằng Excel. Hình minh họa 7.42 (A) cho thấy một 
PivotTable được tạo từ tập dữ liệu Bán hàng đơn vị HNA. Nó chứa các mô hình, đơn vị khác nhau 
được bán cho mỗi mẫu và số lượng tích lũy được bán cho mỗi mẫu. Các mô hình được xếp theo thứ tự giảm dần 
(xếp hạng) dựa trên số lượng sản phẩm đã bán. Về mô hình thăm dò:
• Mô hình đại diện cho biến danh nghĩa.
• Tổng số sản phẩm đã bán đại diện cho biến số (giá trị).
• Phần trăm tích lũy thể hiện giá trị số (giá trị tích lũy).
Làm cách nào để

![ILLUSTRATION 7.42](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.42.png)

7.3  Dữ liệu được khám phá bằng cách tích hợp các mối quan hệ dữ liệu như thế nào?  7-31
Khám phá và hiểu biết sâu sắc
Biểu đồ Pareto giúp xác định xem có một nhóm nhỏ mô hình nào tạo ra doanh thu cao nhất hay không. 
Trong trường hợp này, các mẫu xe Accord, Civic và CR-V cùng nhau tạo ra hơn 75% doanh số bán hàng, 
trong khi ba mô hình còn lại tạo ra ít hơn 25%.
Phân tích Pareto có nhiều ứng dụng trong kinh doanh và kế toán:
• Xác định những khiếu nại quan trọng nhất của khách hàng. Nếu một nhóm nhỏ các vấn đề gây ra 
hầu hết các khiếu nại, việc loại bỏ những vấn đề này có thể tác động tích cực đến sự hài lòng của khách hàng.
• Nêu rõ các loại chi phí chính cho một dự án cụ thể.
• Xác định những nhân viên tạo ra nhiều khách hàng mới nhất.
• Minh họa nhóm cổ phiếu nào trong danh mục đầu tư chịu trách nhiệm cho phần lớn sự tăng trưởng của nó.
Báo cáo sử dụng nhiều hình ảnh trực quan
Các mối quan hệ dữ liệu thường được tích hợp bằng cách sử dụng nhiều hình ảnh trực quan như một phần của báo cáo. Hầu hết 
mang tính tương tác, những hình ảnh trực quan này mang lại cơ hội khám phá vô tận. Một báo cáo liên quan
mối quan hệ từng phần và chuỗi thời gian khám phá các xu hướng không chỉ cho tổng thể mà còn 
cũng như đối với từng bộ phận riêng lẻ. Một ví dụ nâng cao hơn, với nhiều tính năng tương tác 
hình dung đại diện cho các mối quan hệ khác nhau, có thể minh họa điều này.
Trực quan hóa
Hình minh họa 7.43 là Báo cáo tương tác HNA, tích hợp các mối quan hệ dữ liệu với 
nhiều trực quan hóa.
Tổng cộng
Odyssey
CR-V
hiệp định
Đường sườn núi
Phi công
dân sự
3.074.040
2.555.799
1.603.686
898.441
897.807
517.964
9.547.737
người mẫu
Tổng số đơn vị đã bán
32,20%
58,97%
75,76%
85,17%
94,58%
100,00%
Phần Trăm Tích Lũy
(A) Bảng Pivot
(B): Biểu đồ đường và cột
2.500.000
2.000.000
3.000.000
3.500.000
1.000.000
500.000
1.500.000
0
80,00%
60,00%
100,00%
20,00%
40,00%
0,00%
hiệp định
CR-V
dân sự
Odyssey
Pilot Ridgeline
Tổng số căn đã bán
Phần Trăm Tích Lũy
MINH HỌA 7.42  Khám phá doanh số bán hàng của HNA bằng phân tích Pareto
Hình minh họa 7.42 (B) là biểu đồ đường và cột được tạo từ PivotTable. Cùng 
trục x là các mẫu khác nhau được xếp hạng dựa trên tổng số đơn vị đã bán. Chúng là những món đồ 
đang được phân tích. Dòng biểu thị số lượng đơn vị tích lũy được bán. Trục y thứ hai 
đã được thêm vào để nhấn mạnh rằng dòng này được biểu thị dưới dạng phần trăm. Một điểm trên đường 
cho thấy các mô hình bên trái đóng góp tích lũy như thế nào vào tổng doanh số bán hàng, như 
một tỷ lệ phần trăm.

![ILLUSTRATION 7.43](../TaiLieu/textbookForPractice/Figures/Ch_07/ILLUSTRATION%207.43.png)