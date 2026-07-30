**EX 4.11 (LO 1-4) Kế toán Tài chính | Kế toán Quản trị | Chuẩn bị một Kế hoạch Dự án (Prepare a Project Plan)** Bạn là một nhà phân tích tài chính tại Tiệm làm đẹp Sihrya's. Chủ sở hữu công ty đã yêu cầu bạn thực hiện các phân tích dữ liệu để hiểu về các sản phẩm đóng góp vào khả năng sinh lời của cửa hàng bán lẻ của tiệm. Chủ sở hữu đã cung cấp cho bạn một từ điển dữ liệu (data dictionary), được trình bày ở đây, mô tả dữ liệu mà bạn có thể xem xét sử dụng trong phân tích của mình.

| Nhãn trường (Field Label) | Tên trường trong cơ sở dữ liệu (Field Name in Database) | Mô tả trường (Field Description) |
| --- | --- | --- |
| Số Biên lai (Receipt Number) | ReceiptNo | Số biên lai được gán bởi POS, nhận dạng duy nhất mỗi giao dịch bán hàng. |
| Ngày Bán hàng (Sales Date) | SaleDate | Ngày bán hàng theo POS. |
| Mã Hàng tồn kho (Inventory Code) | InvCode | Số nhận dạng hàng tồn kho duy nhất cho mỗi sản phẩm trong cửa hàng bán lẻ của tiệm. |
| Số lượng Bán ra (Number Sold) | NoSold | Số lượng mặt hàng đã bán. |
| Mô tả Hàng tồn kho (Inventory Description) | InvDesc | Mô tả về mặt hàng tồn kho. |
| Giá Hàng tồn kho (Inventory Price) | InvPrice | Giá bán gộp của mặt hàng tồn kho. |
| Chi phí Hàng tồn kho (Inventory Cost) | InvCost | Chi phí bình quân gia quyền của mặt hàng tồn kho. |

1. Nêu rõ mục tiêu của chủ sở hữu đối với dự án phân tích dữ liệu của bạn.
2. Giả sử câu hỏi phân tích của bạn là nhằm xác định các sản phẩm có lợi nhuận gộp (gross profit) cao nhất. Hãy xác định các trường dữ liệu mà bạn nên đưa vào phân tích của mình. Xác định các lựa chọn phân tích dữ liệu để trả lời câu hỏi phân tích này.
3. Xác định các rủi ro và các lựa chọn kiểm soát liên quan đến câu hỏi phân tích.

**EX 4.12 (LO 1-4) Dữ liệu | Kế toán Quản trị | Chọn một Chiến lược Dữ liệu và Thực hiện Phân tích (Select a Data Strategy and Perform an Analysis)** Bạn là một kế toán quản trị làm việc tại một công ty bán lẻ đồ chăm sóc thú cưng có nhiều địa điểm. Người giám sát của bạn đã yêu cầu bạn so sánh số tiền mua hàng từ mỗi nhà cung cấp trong tháng 12 năm 2024 so với tháng 12 năm 2025. Sau khi thảo luận với người giám sát, bạn đã xác định được những điều sau:
**Mục tiêu:** So sánh tổng mức mua hàng theo nhà cung cấp trong tháng 12 năm 2024 và tháng 12 năm 2025.
**Câu hỏi:** Trong năm 2024 và 2025, công ty đã mua hàng nhiều nhất (tính bằng đô la) từ những nhà cung cấp nào?
**Dữ liệu:** Bạn có quyền truy cập vào các dữ liệu sau.

| Trường dữ liệu (Data Field) | Mô tả (Description) |
| --- | --- |
| PONo | Số Đơn đặt hàng được gán duy nhất. |
| VendorID | Mã nhà cung cấp được gán duy nhất. |
| VendorName | Tên nhà cung cấp. |
| VendorQuality | Đánh giá chất lượng từ 1 - 6, trong đó 1 = kém và 6 = xuất sắc. |
| VendorAddress | Tên đường và địa chỉ gửi thư của bưu điện Hoa Kỳ. |
| VendorCity | Thành phố của địa chỉ gửi thư. |
| VendorState | Bang của địa chỉ gửi thư. |
| VendorZip | Mã zip của địa chỉ gửi thư. |
| VendorPayterms | Các điều khoản thanh toán được đàm phán với nhà cung cấp. |
| PODate | Ngày Đơn đặt hàng. |
| POItemID | Số mặt hàng có thể nhận dạng duy nhất. |
| POItemDescription | Mô tả về mặt hàng. |
| ItemCost | Chi phí của mặt hàng theo các điều khoản được đàm phán với nhà cung cấp. |
| ItemQty | Tổng số lượng mặt hàng đã mua. |

1. Những mục dữ liệu nào bạn sẽ sử dụng trong chiến lược dữ liệu của mình?
2. Thiết kế một chiến lược phân tích để xác định (các) nhà cung cấp mà công ty có số tiền mua hàng cao hơn vào năm 2025 so với năm 2024.
3. Thực hiện phân tích theo chiến lược phân tích của bạn. Xác định các nhà cung cấp mà công ty có số tiền mua hàng cao hơn vào năm 2025 so với năm 2024.

---

**Các Bài tập Tình huống (Problems)**

**PR 4.1 (LO 1- 4) Dữ liệu | Kiểm toán | Kế toán Quản trị | Hoàn thành Kế hoạch Dự án (Complete Project Plan)** Bạn làm việc trong nhóm kiểm toán nội bộ của tổ chức mình và người giám sát của bạn đã yêu cầu bạn phân tích dữ liệu về thẻ p-card. Mục tiêu của phân tích là để hiểu được việc chi tiêu qua thẻ p-card trong năm hiện tại. Các câu hỏi liên quan đến mục tiêu bao gồm:
- Ba nhà cung cấp nào mà công ty chi nhiều tiền nhất bằng thẻ p-card?
- Nhân viên nào chi số tiền cao nhất bằng thẻ p-card?
Xem xét dữ liệu và hoàn thành biểu đồ để lập hồ sơ các lựa chọn chiến lược dữ liệu và phân tích của bạn.

| Mục tiêu và Các Câu hỏi (Objective and Questions) | Các Chiến lược Dữ liệu và Phân tích (Data and Analysis Strategies) | Các Rủi ro (Risks) | Các Kiểm soát (Controls) |
| --- | --- | --- | --- |
| **Mục tiêu:** Hiểu việc chi tiêu thẻ p-card trong năm hiện tại.<br>**Các Câu hỏi:**<br>• Ba nhà cung cấp nào mà Công ty chi nhiều tiền nhất bằng thẻ p-card?<br>• Nhân viên nào chi số tiền cao nhất bằng thẻ p-card? | **Dữ liệu:** Sử dụng dữ liệu được cung cấp trong tệp Excel.<br>**Phân tích:** Sử dụng Excel để tạo PivotTable cho phép phân nhóm dữ liệu chi tiêu p-card theo nhà cung cấp và sắp xếp theo nhà cung cấp có mức chi tiêu cao nhất.<br>Sử dụng Excel để tạo PivotTable nhằm phân nhóm số tiền chi tiêu p-card theo nhân viên và sắp xếp theo số tiền cao nhất theo từng nhân viên. | 1. Dữ liệu:<br>2. Phân tích: | 3. Dữ liệu:<br>4. Phân tích: |

5. Thực hiện các phân tích được đề xuất trong biểu đồ. Tóm tắt kết quả của bạn.

**PR 4.2 (LO 1, 2, 3) Dữ liệu | Kế toán Tài chính | Kế toán Quản trị | Hoàn thành Bước 2 và 3 của Kế hoạch Dự án và Thực hiện Phân tích (Complete Steps 2 and 3 of a Project Plan and Perform Analysis).** Bạn là một nhà phân tích tài chính tại Tiệm làm đẹp Sihrya's. Chủ sở hữu đã yêu cầu bạn thực hiện các phân tích dữ liệu để hiểu về các sản phẩm đóng góp vào khả năng sinh lời của cửa hàng bán lẻ của tiệm. Chủ sở hữu đã đưa cho bạn một từ điển dữ liệu (data dictionary), được trình bày ở đây, mô tả dữ liệu mà bạn có thể xem xét sử dụng trong phân tích của mình.

| Nhãn trường (Field Label) | Tên trường trong cơ sở dữ liệu (Field Name in Database) | Mô tả trường (Field Description) |
| --- | --- | --- |
| Số Biên lai (Receipt Number) | ReceiptNo | Số biên lai được gán bởi POS, nhận dạng duy nhất mỗi giao dịch bán hàng. |
| Ngày Bán hàng (Sales Date) | SaleDate | Ngày bán hàng theo POS. |
| Mã Hàng tồn kho (Inventory Code) | InvCode | Số nhận dạng hàng tồn kho duy nhất cho mỗi sản phẩm trong cửa hàng bán lẻ của tiệm. |
| Số lượng Bán ra (Number Sold) | NoSold | Số lượng mặt hàng đã bán. |
| Mô tả Hàng tồn kho (Inventory Description) | InvDesc | Mô tả về mặt hàng tồn kho. |
| Giá Hàng tồn kho (Inventory Price) | InvPrice | Giá bán gộp của mặt hàng tồn kho. |
| Chi phí Hàng tồn kho (Inventory Cost) | InvCost | Chi phí bình quân gia quyền của mặt hàng tồn kho. |

Giả sử mục tiêu phân tích của bạn là xác định các sản phẩm đóng góp nhiều nhất vào khả năng sinh lời của cửa hàng bán lẻ của tiệm. Các câu hỏi cụ thể của bạn là: Những sản phẩm nào có số lượng bán ra cao nhất? Những sản phẩm nào có biên lợi nhuận gộp dương (positive gross profit margin)? Hãy sử dụng thông tin được cung cấp để trả lời các câu hỏi sau:
1. Xác định các trường dữ liệu cần đưa vào chiến lược dữ liệu của bạn.
2. Xác định một chiến lược dữ liệu có thể được sử dụng để trả lời các câu hỏi mục tiêu.
3. Xác định một chiến lược phân tích có thể được sử dụng để trả lời các câu hỏi mục tiêu.
4. Xem xét dữ liệu được cung cấp để thực hiện phân tích. Sau khi thực hiện phân tích, hãy xác định hai sản phẩm hàng đầu đóng góp vào khả năng sinh lời của tiệm.
