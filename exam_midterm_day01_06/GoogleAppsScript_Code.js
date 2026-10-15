/**
 * ====================================================================
 * MÃ GOOGLE APPS SCRIPT: LƯU KẾT QUẢ BÀI KIỂM TRA VÀO GOOGLE SHEET
 * Học phần: Trí tuệ nhân tạo (AI) trong Kế toán & Tài chính
 * ====================================================================
 * 
 * HƯỚNG DẪN CÀI ĐẶT NHANH (MẤT 2 PHÚT):
 * --------------------------------------------------------------------
 * 1. Mở một trang tính Google Sheet mới (tại sheets.google.com).
 * 2. Đặt tên trang tính, ví dụ: "KẾT QUẢ THI GIỮA KỲ AI KẾ TOÁN".
 * 3. Trên thanh menu, chọn: Tiện ích mở rộng (Extensions) -> Apps Script.
 * 4. Xóa toàn bộ mã mặc định (myFunction), dán toàn bộ đoạn mã bên dưới vào.
 * 5. Bấm vào nút "Triển khai" (Deploy) màu xanh ở góc trên bên phải:
 *    -> Chọn "Tùy chọn triển khai mới" (New deployment).
 *    -> Chọn loại: "Ứng dụng web" (Web App - hình quả địa cầu).
 *    -> Mô tả: "Lưu điểm thi Giữa kỳ".
 *    -> Thực thi dưới dạng (Execute as): "Tôi" (Me).
 *    -> Ai có quyền truy cập (Who has access): "Bất kỳ ai" (Anyone) - RẤT QUAN TRỌNG!
 * 6. Bấm nút "Triển khai":
 *    -> Nếu Google yêu cầu cấp quyền, bấm "Ủy quyền truy cập" -> Chọn tài khoản Google của thầy/cô -> Bấm "Advanced" (Nâng cao) -> Bấm "Go to ... (unsafe)" -> Bấm "Allow" (Cho phép).
 * 7. URL ứng dụng web đang hoạt động:
 *    -> URL: https://script.google.com/macros/s/AKfycby2cPdyEuXF8Hyda1yiqgF5zFo3Ya5qhMjua2YUkyzcFZ-GdhFRGT19WgjhEgqmi-ziAA/exec
 *    -> Deployment ID: AKfycby2cPdyEuXF8Hyda1yiqgF5zFo3Ya5qhMjua2YUkyzcFZ-GdhFRGT19WgjhEgqmi-ziAA
 */

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(15000); // Tránh xung đột ghi dữ liệu khi nhiều sinh viên nộp bài cùng lúc

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getActiveSheet();

    // Tự động tạo dòng tiêu đề nếu trang tính còn mới
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "Thời gian nộp", 
        "Họ và tên sinh viên", 
        "Mã sinh viên (MSSV)", 
        "Lớp sinh hoạt", 
        "Điểm (Thang 10)", 
        "Số câu đúng", 
        "Tổng số câu", 
        "Thời gian làm bài", 
        "Tỷ lệ đúng"
      ]);
      
      // Định dạng dòng tiêu đề đẹp mắt
      var headerRange = sheet.getRange(1, 1, 1, 9);
      headerRange.setFontWeight("bold");
      headerRange.setBackground("#1a73e8");
      headerRange.setFontColor("#ffffff");
      headerRange.setHorizontalAlignment("center");
      sheet.setFrozenRows(1);
    }

    // Đọc dữ liệu gửi từ bài thi
    var data = JSON.parse(e.postData.contents);

    var row = [
      data.submitTime || Utilities.formatDate(new Date(), "GMT+7", "dd/MM/yyyy HH:mm:ss"),
      data.fullName || "Chưa có tên",
      data.studentId || "Chưa có MSSV",
      data.className || "Chưa có lớp",
      data.score10 !== undefined ? Number(data.score10) : 0,
      data.correctCount !== undefined ? Number(data.correctCount) : 0,
      data.totalQuestions || 60,
      data.timeSpent || "",
      data.summaryText || ""
    ];

    sheet.appendRow(row);
    
    // Căn giữa cột điểm, MSSV, lớp
    var lastRow = sheet.getLastRow();
    sheet.getRange(lastRow, 1).setHorizontalAlignment("center");
    sheet.getRange(lastRow, 3).setHorizontalAlignment("center");
    sheet.getRange(lastRow, 4).setHorizontalAlignment("center");
    sheet.getRange(lastRow, 5).setHorizontalAlignment("center").setFontWeight("bold");
    sheet.getRange(lastRow, 6, 1, 4).setHorizontalAlignment("center");

    return ContentService.createTextOutput(JSON.stringify({ "status": "success", "message": "Đã lưu điểm thành công!" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ "status": "error", "message": err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);

  } finally {
    lock.releaseLock();
  }
}

function doGet(e) {
  return ContentService.createTextOutput("Hệ thống Web App chấm điểm AI trong Kế toán & Tài chính đang hoạt động bình thường!");
}
