# THỰC TIỄN ỨNG DỤNG HỌC MÁY TRONG KẾ TOÁN VÀ KIỂM TOÁN
*(Machine Learning Practices in Accounting and Auditing)*

- **Tác giả:** Chetanpal Singh (Holmesglen Institute, Úc), Rahul Thakkar (Học viện Công nghệ Victoria - VIT, Úc), Rashikala Weerawarna (Holmesglen Institute), Vimal B Patel (Navsari Agricultural University, Ấn Độ)
- **Tạp chí xuất bản:** *International Journal of Science and Research Archive* (IJSRA, 2023), 10(01), 131–162
- **DOI:** [10.30574/ijsra.2023.10.1.0720](https://doi.org/10.30574/ijsra.2023.10.1.0720)
- **Mở rộng thực tiễn:** Khảo sát thực chứng của Fedyk et al. (*Review of Accounting Studies - RAST*)

---

## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

Trong kỷ nguyên công nghệ hiện nay, các ứng dụng Học máy (*Machine Learning - ML*) đang trở nên phổ biến từng ngày. Công trình nghiên cứu này cung cấp thông tin toàn diện về hiệu quả của các kỹ thuật ML trong quy trình kế toán cũng như kiểm toán. Để thu được các kết quả khách quan, nhiều thư viện ML mạnh mẽ trên nền tảng Python đã được khai thác triệt để, bao gồm Seaborn, Matplotlib, NumPy, Statsmodels và Scikit-learn. 

Trong phần mở đầu, mục đích và các mục tiêu nghiên cứu cụ thể được xác lập nhằm định hướng toàn bộ quy trình phân tích. Một mô hình học máy Hồi quy Logistic (*Logistic Regression Machine Learning Model*) hoàn chỉnh được xây dựng và kiểm thử từng bước trên bộ dữ liệu tài chính thực nghiệm 25 biến. Các nguồn tài liệu học thuật được phân tích sâu sắc trong phần tổng quan y văn, giúp người đọc nắm bắt đa chiều bối cảnh thực tiễn và nhận diện rõ vai trò của các thuật toán ML trong tự động hóa rà soát hợp đồng (Argus), kiểm tra toàn diện nhật ký chứng từ (Halo), cũng như vượt qua các rào cản về tâm lý thiên lệch nhận thức của kiểm toán viên.

**Từ khóa:** Machine Learning; Algorithm; Accounting; Auditing; Artificial Neural Network; Logistic Regression; VIF; Confusion Matrix; Class Imbalance.

---

## 1. MỞ ĐẦU & ĐỘNG LỰC NGHIÊN CỨU (INTRODUCTION)

Hãng nghiên cứu công nghệ hàng đầu thế giới **Gartner Inc.** khẳng định rằng: Để duy trì lợi thế cạnh tranh sống còn, các doanh nghiệp bắt buộc phải phân tích sâu sắc cách thức các công nghệ then chốt đang định hình lại toàn bộ hoạt động vận hành của mình. Doanh nghiệp sẽ đối mặt với rủi ro tụt hậu và bị đào thải nếu không chủ động khảo sát và áp dụng những công nghệ này. Học máy (Machine Learning) là một ví dụ tiêu biểu cho công nghệ chiến lược sử dụng trí tuệ nhân tạo.

**PricewaterhouseCoopers (PwC)** đã chính thức công nhận tầm quan trọng của các học phần học máy nâng cao trong chương trình đào tạo kế toán bậc đại học, khẳng định rằng học máy là một kỹ năng AI cốt lõi mà bất kỳ kế toán viên và kiểm toán viên chuyên nghiệp nào trong kỷ nguyên số cũng bắt buộc phải thành thạo.

---

## 2. TỔNG QUAN LÝ THUYẾT & ỨNG DỤNG THỰC TẾ

### 2.1 Các Ứng Dụng Đột Phá Tại Các Hãng Kiểm Toán Lớn
1. **Hệ thống Argus (Deloitte):** Tự động đọc và bóc tách các văn bản pháp lý phức tạp như hợp đồng thuê tài sản, công cụ tài chính phái sinh và hợp đồng bán hàng. Thuật toán tự động phân loại hợp đồng thuê tài chính (*Capital Lease*) vs thuê hoạt động (*Operating Lease*) và cảnh báo các điều khoản dị thường.
2. **Hệ thống Halo (PwC):** Rà soát 100% các bút toán nhật ký chứng từ (*Journal Entries*) thay vì chỉ chọn mẫu ngẫu nhiên. Tự động phát hiện các bút toán bất thường: chứa từ khóa nhạy cảm, hạch toán vào ban đêm/ngày nghỉ, thực hiện bởi tài khoản trái thẩm quyền, hoặc các giao dịch chia nhỏ cố tình lách hạn mức phê duyệt.

### 2.2 Bốn Thiên Lệch Tâm Lý Của Kiểm Toán Viên Khi Làm Việc Với AI
1. **Thiên lệch xác nhận (Confirmation Bias):** Chỉ tìm kiếm các thông tin củng cố niềm tin chủ quan có sẵn.
2. **Thiên lệch sẵn có (Availability Bias):** Ra quyết định dựa trên sự kiện vừa xảy ra gần nhất.
3. **Thiên lệch quá tự tin (Overconfidence Bias):** Tin tưởng mù quáng vào kết quả của máy móc mà không rà soát lại dữ liệu đầu vào.
4. **Thiên lệch neo thông tin (Anchoring Bias):** Bị "neo" vào số liệu phân tích do phần mềm của khách hàng cung cấp.

---

## 3. THỰC NGHIỆM PIPELINE HỌC MÁY TRÊN PYTHON

Nghiên cứu tiến hành thực nghiệm trên bộ dữ liệu **Default of Credit Card Clients Dataset** gồm 25 thuộc tính tài chính:

- `default.payment.next.month`: Biến mục tiêu (1 = Vỡ nợ kỳ tới, 0 = Thanh toán đúng hạn).
- `LIMIT_BAL`: Hạn mức tín dụng cấp cho khách hàng.
- `EDUCATION`, `MARRIAGE`, `AGE`: Trình độ học vấn, tình trạng hôn nhân và độ tuổi.
- `PAY_0` đến `PAY_6`: Lịch sử trả nợ 6 tháng qua (-1 = đúng hạn, 1 = trễ 1 tháng,...).
- `BILL_AMT1` đến `BILL_AMT6`: Số dư hóa đơn sao kê qua 6 kỳ liên tiếp.
- `PAY_AMT1` đến `PAY_AMT6`: Số tiền thanh toán thực tế qua 6 kỳ.

### Các Bước Thực Nghiệm Kỹ Thuật:
1. **Khám phá dữ liệu (EDA):** Dùng `seaborn` và `matplotlib` vẽ Countplot, Boxplot để đánh giá phân bố nợ xấu theo nhóm nhân khẩu học.
2. **Làm sạch ngoại lệ (Outliers):** Lọc bỏ 1% giá trị biên cực đoan của hạn mức tín dụng và số tiền hóa đơn để triệt tiêu nhiễu.
3. **Kiểm định đa cộng tuyến VIF:** Giữ lại các biến có $VIF < 5$, loại bỏ các biến có $VIF \ge 5$ gây sai lệch dấu hồi quy.
4. **Chọn biến Wald Chi-Square:** Xác định top các biến có đóng góp thống kê lớn nhất vào xác suất vỡ nợ (nổi bật là `PAY_0` và `LIMIT_BAL`).
5. **Huấn luyện mô hình Logistic Regression:** Thực thi song song qua `statsmodels.Logit` và `sklearn.linear_model.LogisticRegression`.
6. **Đánh giá hiệu năng:**
   - Accuracy: **81.0%**
   - Specificity (Lớp 0): **97.0%**
   - Sensitivity / Recall (Lớp 1): **24.0%** (Rủi ro: Bỏ sót 76% trường hợp vỡ nợ!)
7. **Xử lý mất cân bằng lớp (Class Imbalance):** Cân bằng lại mẫu dữ liệu, nâng cao độ nhạy Recall của lớp rủi ro lên mức cảnh báo tin cậy.

---

## 4. GÓC NHÌN THỰC CHỨNG RAST (FEDYK ET AL.)

Khảo sát thực chứng quy mô lớn của Fedyk et al. (*Review of Accounting Studies*) mang lại 3 thông điệp lớn:
1. **Thâm nhập thực tế:** ML tại các hãng kiểm toán hiện chủ yếu phục vụ tiền kiểm toán và tự động hóa tác vụ cơ bản. Ý kiến kiểm toán cuối cùng vẫn đòi hỏi phán đoán con người.
2. **Mô hình Human-in-the-loop:** ML đóng vai trò trợ lý sàng lọc rủi ro, giúp kiểm toán viên tập trung 80% thời gian vào 20% các rủi ro phức tạp nhất.
3. **Không ỷ lại công nghệ:** Kiểm toán viên thế hệ mới phải duy trì năng lực tư duy phản biện độc lập để không bị phụ thuộc vào thuật toán hộp đen.
