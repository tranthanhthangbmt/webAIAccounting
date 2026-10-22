# FINBERT: MÔ HÌNH NGÔN NGỮ LỚN ĐẶC THÙ TÀI CHÍNH ĐỂ TRÍCH XUẤT THÔNG TIN TỪ VĂN BẢN KẾ TOÁN
*(FinBERT: A Large Language Model for Extracting Information from Financial Text)*

- **Tác giả:** Allen H. Huang (HKUST), Hui Wang (Đại học Nhân Dân Trung Hoa), Yi Yang (HKUST)
- **Tạp chí xuất bản:** Contemporary Accounting Research (CAR) — Tạp chí Kế toán Hàng đầu Thế giới (FT50)
- **Định danh DOI:** [10.1111/1911-3846.12832](https://doi.org/10.1111/1911-3846.12832)
- **Ngữ liệu thực nghiệm:** 10.000 câu gán nhãn thủ công từ báo cáo phân tích, hàng triệu văn bản 10-K, 10-Q, và bản ghi các cuộc họp hội nghị báo cáo lợi nhuận (Earnings Conference Calls)

---

## TÓM TẮT NGHIÊN CỨU (ABSTRACT)

Chúng tôi phát triển **FinBERT**, một mô hình ngôn ngữ lớn (*Large Language Model - LLM*) tiên tiến được huấn luyện thích nghi chuyên biệt cho lĩnh vực tài chính - kế toán. Chúng tôi chứng minh rằng FinBERT tích hợp sâu sắc tri thức tài chính và có khả năng tóm tắt, nắm bắt ngữ cảnh trong các văn bản tài chính vượt trội hơn hẳn các phương pháp trước đây. Sử dụng mẫu dữ liệu gồm 10.000 câu được các nhà nghiên cứu gán nhãn thủ công từ các báo cáo phân tích tài chính, chúng tôi ghi nhận FinBERT **vượt trội áp đảo so với Từ điển Loughran & McDonald (LM)** và các thuật toán học máy phổ biến khác, bao gồm Naïve Bayes, Support Vector Machine (SVM), Random Forest, Convolutional Neural Network (CNN) và Long Short-Term Memory (LSTM) trong bài toán phân loại sắc thái (*sentiment classification*).

FinBERT đặc biệt xuất sắc trong việc nhận diện sắc thái tích cực hoặc tiêu cực của các câu mà các thuật toán khác thường gán nhãn sai thành "Trung tính" (*Neutral*), nhờ vào cơ chế chú ý ngữ cảnh (*contextual attention*). Lợi thế của FinBERT so với mô hình BERT gốc của Google đặc biệt rõ nét khi kích thước mẫu huấn luyện nhỏ và trong các văn bản chứa các thuật ngữ tài chính hiếm gặp trong ngôn ngữ thông thường. FinBERT cũng vượt trội trong việc tự động nhận diện các thảo luận liên quan đến **Môi trường, Xã hội và Quản trị (ESG)**. Cuối cùng, chúng tôi chứng minh rằng các phương pháp truyền thống đã **đánh giá thấp tính hữu ích thông tin (*textual informativeness*)** của các cuộc họp hội nghị báo cáo lợi nhuận ít nhất **18%** so với FinBERT.

**Từ khóa:** Học sâu (Deep Learning); Mô hình ngôn ngữ lớn (LLM); FinBERT; Transfer Learning; Khả năng giải trình; Phân loại sắc thái; ESG; Thuyết minh BCTC.

---

## 1. MỞ ĐẦU & TẦM QUAN TRỌNG CỦA DỮ LIỆU VĂN BẢN KẾ TOÁN

Hơn 80% thông tin công bố của các doanh nghiệp tồn tại dưới dạng **văn bản phi cấu trúc (*unstructured text*)**:
- Thuyết minh Báo cáo Tài chính (Footnotes).
- Báo cáo Thảo luận và Phân tích của Ban Giám đốc (MD&A trong Báo cáo 10-K, 10-Q).
- Biên bản họp hội nghị công bố kết quả kinh doanh định kỳ (*Earnings Conference Calls*).
- Báo cáo phân tích của các chuyên viên phân tích tài chính (*Analyst Reports*).

Khi doanh nghiệp gặp khó khăn tài chính hoặc có hành vi thao túng sổ sách (*Earnings Management*), các con số trên bảng cân đối kế toán chỉ phản ánh một phần. Ban lãnh đạo thường sử dụng ngôn từ vòng vo, thuật ngữ mơ hồ hoặc giọng điệu đánh lạc hướng trong phần Thuyết minh và Báo cáo thường niên để che giấu rủi ro.

### Điểm Yếu Chí Mạng Của Các Phương Pháp Phân Tích Văn Bản Truyền Thống:
1. **Phương pháp đếm từ điển (như Từ điển Loughran-McDonald - LM):** Coi văn bản là "túi từ" (*Bag-of-Words*), chỉ đơn thuần đếm số từ thuộc danh sách từ tích cực hoặc tiêu cực. Phương pháp này hoàn toàn mù tịt trước ngữ cảnh phủ định (ví dụ: không phân biệt được giữa *"Khoản nợ xấu không còn là rủi ro"* và *"Khoản nợ có nguy cơ trở thành rủi ro"*).
2. **Hiện tượng đa nghĩa trong tài chính (*Financial Polysemy*):** Các từ ngữ trong tài chính mang ý nghĩa rất khác với đời thường. Ví dụ: từ *"share"* (thường là chia sẻ, tài chính là cổ phần), *"liability"* (thường là gánh nặng, tài chính là nợ phải trả), *"depreciation"* (thường là sự coi thường, tài chính là khấu hao tài sản).

---

## 2. QUÁ TRÌNH HUẤN LUYỆN TRƯỚC (PRETRAINING) & CƠ CHẾ SELF-ATTENTION CỦA FinBERT

FinBERT được xây dựng trên kiến trúc **Transformer (Bộ biến đổi)** gồm 12 tầng mã hóa (*Encoder layers*), 768 chiều ẩn và 12 đầu chú ý đa tầng (*Self-Attention Heads*).

### Quá trình Pretraining chuyên biệt:
- **Ngữ liệu tài chính khổng lồ:** FinBERT được huấn luyện tiếp tục (*Continual Pretraining*) trên 2,5 triệu đoạn văn bản từ Báo cáo thường niên 10-K, Báo cáo quý 10-Q của các công ty niêm yết tại Mỹ, cùng các bản ghi họp hội nghị báo cáo lợi nhuận và tin tức tài chính.
- **Học biểu diễn từ chuyên ngành:** Cơ chế Masked Language Model (MLM) giúp mạng nơ-ron học sâu hiểu sâu sắc ngữ cảnh của các thuật ngữ kế toán kiểm toán phức tạp.

![Hình 4: Trọng số chú ý Self-Attention của FinBERT](figures_paper3/fig4_finbert_attention_weights.png)
*Hình 4: Trực quan hóa trọng số Self-Attention của FinBERT. Mô hình tự động tập trung sự chú ý vào các cụm từ thể hiện cốt lõi sức khỏe tài chính và rủi ro hoạt động.*

---

## 3. THỰC NGHIỆM 1: PHÂN LOẠI SẮC THÁI CÂU (SENTIMENT CLASSIFICATION)

Nghiên cứu sử dụng mẫu chuẩn gồm **10.000 câu** được các chuyên gia tài chính gán nhãn thủ công cẩn trọng (3.577 câu tích cực, 4.586 câu trung tính, 1.837 câu tiêu cực). Đơn vị phân tích là **cấp độ câu (*sentence level*)** vì câu là đơn vị ngôn ngữ tự nhiên nhỏ nhất truyền tải trọn vẹn một quan điểm đánh giá.

### Bảng 1: So sánh hiệu năng phân loại sắc thái trên mẫu kiểm thử (1.000 câu độc lập):

| Thuật Toán / Mô Hình NLP | Accuracy (%) (Độ chính xác) | Precision (%) (Độ chuẩn xác) | Recall (%) (Độ bao phủ) | F1-Score (%) | Recall Tích Cực (%) | Recall Trung Tính (%) | Recall Tiêu Cực (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FinBERT (Đề xuất)** | **88,2%** | **87,2%** | **88,5%** | **87,8%** | **88,5%** | **87,3%** | **89,7%** |
| BERT (Google gốc) | 85,0% | 83,6% | 85,1% | 84,2% | 86,3% | 84,1% | 84,8% |
| LSTM (Mạng chuỗi thời gian) | 76,3% | 74,8% | 72,5% | 73,3% | 79,3% | 82,1% | 56,0% |
| CNN (Mạng tích chập) | 75,1% | 74,4% | 71,4% | 72,5% | 73,5% | 83,6% | 57,1% |
| Naïve Bayes (NB) | 73,6% | 71,8% | 70,7% | 71,1% | 75,4% | 78,4% | 58,2% |
| Support Vector Machine (SVM) | 72,6% | 71,0% | 68,8% | 69,6% | 68,7% | 82,8% | 54,9% |
| Random Forest (RF) | 71,9% | 75,4% | 64,8% | 66,8% | 70,7% | 86,9% | 37,0% |
| **Từ điển Loughran & McDonald (LM)** | **62,1%** | **64,4%** | **58,0%** | **58,1%** | **40,2%** | **84,3%** | **49,5%** |

### 🔍 Điểm Nhấn Đột Phá Của FinBERT:
1. **FinBERT đạt F1-score 87,8%**, vượt trội hoàn toàn so với Từ điển LM (chỉ đạt F1 58,1%).
2. **Khắc phục điểm yếu "Bỏ lọt tiêu cực":** Từ điển LM chỉ bắt được 49,5% câu tiêu cực, Random Forest chỉ bắt được 37,0%. Trong khi đó, **FinBERT đạt độ nhạy bắt câu tiêu cực lên tới 89,7%** (nhận diện chính xác 165/184 câu tiêu cực). Điều này vô cùng quý giá đối với kiểm toán viên nhằm phát hiện các cảnh báo rủi ro ngầm.

![Hình 1: Độ chính xác theo quy mô mẫu huấn luyện](figures_paper3/fig1_sample_size_accuracy.png)
*Hình 1: Độ chính xác của các mô hình khi giảm quy mô mẫu huấn luyện từ 100% xuống 10%. FinBERT duy trì độ chính xác 81,3% ngay cả khi chỉ có 10% mẫu (cao hơn cả LSTM huấn luyện trên 100% mẫu).*

![Hình 2: Hiệu ứng xáo trộn từ lên các thuật toán](figures_paper3/fig2_word_randomization.png)
*Hình 2: Thử nghiệm xáo trộn ngẫu nhiên thứ tự từ (Word Randomization). Hiệu năng của FinBERT sụt giảm mạnh nhất, chứng minh mô hình thực sự dựa vào cấu trúc ngữ pháp và chuỗi ngữ cảnh chứ không học vẹt từ khóa.*

---

## 4. THỰC NGHIỆM 2: PHÂN LOẠI THẢO LUẬN MÔI TRƯỜNG, XÃ HỘI & QUẢN TRỊ (ESG)

Các yêu cầu công bố thông tin phi tài chính về ESG đang trở thành chuẩn mực kiểm toán bắt buộc toàn cầu (theo IFRS S1 và IFRS S2). Tác giả tiến hành thử nghiệm phân loại các câu thành 4 lớp: Môi trường (E), Xã hội (S), Quản trị (G), và Phi ESG:

| Thuật Toán NLP | Accuracy Toàn Diện (%) | Precision (%) | F1-Score (%) | Recall Môi Trường (E) (%) | Recall Xã Hội (S) (%) | Recall Quản Trị (G) (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FinBERT** | **89,5%** | **90,0%** | **89,6%** | **90,0%** | **90,0%** | **92,0%** |
| BERT (Gốc) | 87,0% | 87,0% | 86,9% | 96,0% | 86,0% | 86,0% |
| LSTM | 86,0% | 86,1% | 86,0% | 90,0% | 82,0% | 86,0% |
| CNN | 82,0% | 82,2% | 81,9% | 86,0% | 70,0% | 88,0% |
| Naïve Bayes | 80,0% | 80,1% | 80,0% | 78,0% | 76,0% | 88,0% |
| Random Forest | 78,0% | 79,9% | 78,3% | 72,0% | 84,0% | 78,0% |
| Support Vector Machine | 75,0% | 75,3% | 75,0% | 78,0% | 66,0% | 74,0% |

FinBERT đạt độ chính xác **89,5%**, hỗ trợ kiểm toán viên thẩm định tính xác thực của các cam kết giảm phát thải, quản trị nhân sự và kiểm soát nội bộ, ngăn chặn hành vi "tẩy xanh" (*greenwashing*).

---

## 5. THỰC NGHIỆM 3: KIỂM CHỨNG BẰNG PHẢN ỨNG THỊ TRƯỜNG VỐN (MARKET REACTION)

Để loại trừ định kiến chủ quan của người gán nhãn, nghiên cứu kiểm định xem sắc thái văn bản trích xuất bởi FinBERT có giải thích được **Lợi nhuận bất thường tích lũy (Cumulative Abnormal Returns - CAR)** của giá cổ phiếu trong cửa sổ 3 ngày quanh sự kiện họp báo cáo lợi nhuận hay không (Bảng 7 bài báo gốc).

Hồi quy kiểm toán:
$$ \text{CAR} = \alpha + \beta_1 \cdot \text{Tone} + \beta_2 \cdot \text{Earn} + \beta_3 \cdot \text{UE} + \beta_4 \cdot \text{Accruals} + \dots + \varepsilon $$

- Hệ số của `Tone` trích xuất từ FinBERT: **$eta = 0.907$ ($t = 20.35, p < 0.001$)**, cao hơn nhiều so với `Tone` từ từ điển LM ($eta = 0.640, t = 14.89$) và LSTM ($eta = 0.743, t = 17.93$).
- **Kết luận:** Các phương pháp truyền thống đánh giá thấp mức độ truyền tải thông tin của văn bản kế toán ít nhất **18% đến 40%** so với FinBERT. Thị trường thực sự phản ứng nhạy bén với ngữ cảnh mà FinBERT nắm bắt được.

---

## 6. ĐÚC KẾT CHO NGHỀ NGHIỆP KIỂM TOÁN & KẾ TOÁN

> [!TIP]
> **Ứng dụng đột phá cho Kiểm toán số:**
> - **Đọc hiểu Thuyết minh BCTC tự động:** Thay vì đọc thủ công hàng trăm trang thuyết minh, kiểm toán viên có thể dùng FinBERT để quét toàn bộ báo cáo trong vài giây, tự động gắn cờ các đoạn văn bản có sắc thái tiêu cực hoặc cấu trúc ngữ nghĩa bất thường.
> - **Rà soát hợp đồng theo chuẩn IFRS 16 (Thuê tài sản):** Tự động bóc tách các điều khoản cam kết thuê, quyền chọn gia hạn, lãi suất chiết khấu ẩn trong các hợp đồng kinh tế.
> - **Kiểm toán báo cáo bền vững ESG:** Thẩm tra tự động các tuyên bố về trách nhiệm xã hội và môi trường của doanh nghiệp đối chiếu với bằng chứng hoạt động thực tế.

---

## 7. TÀI LIỆU THAM KHẢO CHÍNH (REFERENCES)

1. **Huang, A. H., Wang, H., & Yang, Y. (2023).** FinBERT: A large language model for extracting information from financial text. *Contemporary Accounting Research*, 40(2), 806–841.
2. **Loughran, T., & McDonald, B. (2011).** When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. *The Journal of Finance*, 66(1), 35–65.
3. **Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019).** BERT: Pre-training of deep bidirectional transformers for language understanding. *NAACL-HLT 2019*, 4171–4186.
4. **Li, F. (2010).** The information content of forward-looking statements in corporate filings. *Journal of Accounting Research*, 48(5), 1049–1102.
