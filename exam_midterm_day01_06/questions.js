// Ngân hàng 180 câu hỏi trắc nghiệm Buổi 1 - 6 (AI trong Kế toán & Tài chính)
const EXAM_BANK = [
  {
    "id": 1,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Dễ",
    "question": "Sắp xếp các sự kiện lịch sử về công nghệ kế toán theo thứ tự thời gian từ cũ nhất (trên) đến mới nhất (dưới):\n  (1) Sử dụng bàn tính (Hơn 2000 năm trước)\n  (2) Mua máy tính chuyên dụng cho mục đích kế toán (1955)\n  (3) Sự ra đời của bảng tính điện tử - Spreadsheets (Những năm 1980)\n  (4) Ứng dụng Trí tuệ nhân tạo (Hiện tại và Tương lai)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Công nghệ kế toán tiến hóa từ bàn tính (cũ nhất), đến việc dùng máy tính sơ khai (1955), sau đó là bảng tính điện tử (1980) và hiện tại là AI."
  },
  {
    "id": 2,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Dễ",
    "question": "Theo Klaus Schwab (Diễn đàn Kinh tế Thế giới), AI là một trong những công nghệ then chốt thúc đẩy cuộc cách mạng nào?",
    "options": {
      "A": "Cách mạng Công nghiệp lần thứ nhất",
      "B": "Cách mạng Công nghiệp lần thứ hai",
      "C": "Cách mạng Công nghiệp lần thứ ba",
      "D": "Cách mạng Công nghiệp lần thứ tư"
    },
    "correct": "D",
    "explanation": "Klaus Schwab mô tả kỷ nguyên chuyển đổi số hiện nay, với sự hội tụ của dữ liệu lớn, IoT và AI là Cuộc Cách mạng Công nghiệp Lần thứ tư."
  },
  {
    "id": 3,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Ghép các công ty kiểm toán/kế toán (Big4) với các ứng dụng AI thực tế của họ:\nCột 1:\n  (1) EY\n  (2) Deloitte\n  (3) KPMG\nCột 2:\n  (a) Sử dụng công cụ Argus để trích xuất thông tin kế toán từ hợp đồng\n  (b) Sử dụng thuật toán học máy của IBM để hỗ trợ tuân thủ IFRS 16\n  (c) Dùng máy bay không người lái (drones) tích hợp AI để kiểm kê hàng tồn kho\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-b, 2-a, 3-c",
      "B": "1-a, 2-b, 3-c",
      "C": "1-a, 2-c, 3-b",
      "D": "1-c, 2-a, 3-b"
    },
    "correct": "D",
    "explanation": "EY dùng drones để kiểm kê. Deloitte dùng công cụ Argus đọc hợp đồng. KPMG dùng AI của IBM cho việc tuân thủ chuẩn mực thuê tài sản IFRS 16."
  },
  {
    "id": 4,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Điền các thuật ngữ tương ứng vào chỗ trống để hoàn thành định nghĩa:\n\"___(1)___ tập trung vào một nhiệm vụ cụ thể (như nhận dạng giọng nói, chơi cờ). Trong khi đó, mục tiêu của ___(2)___ là tạo ra máy móc có khả năng thực hiện tất cả các nhiệm vụ nhận thức phức tạp của não bộ con người.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) Trí tuệ nhân tạo tổng quát (AGI) ; (2) Trí tuệ nhân tạo hẹp (ANI)",
      "B": "(1) Trí tuệ nhân tạo hẹp (ANI) ; (2) Trí tuệ nhân tạo tổng quát (AGI)",
      "C": "(1) Học máy (Machine Learning) ; (2) Học máy (Machine Learning)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "ANI (AI hẹp/yếu) chỉ tập trung giải quyết một nhiệm vụ cụ thể rất tốt. AGI (AI tổng quát/mạnh) hướng tới năng lực nhận thức linh hoạt như con người."
  },
  {
    "id": 5,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Khó",
    "question": "Đâu là điểm khác biệt cốt lõi giữa Khai phá dữ liệu (Data Mining) và Học máy (Machine Learning) theo chuyên gia Bernard Marr?",
    "options": {
      "A": "Khai phá dữ liệu tìm mô hình đã có trong dữ liệu lịch sử, còn Học máy cố gắng dự đoán kết quả tương lai dựa trên dữ liệu.",
      "B": "Khai phá dữ liệu hoàn toàn tự động, trong khi Học máy cần sự can thiệp của con người xuyên suốt quá trình.",
      "C": "Khai phá dữ liệu là một lĩnh vực phụ của AI, còn Học máy thì độc lập với AI.",
      "D": "Khai phá dữ liệu chỉ dùng dữ liệu phi cấu trúc, còn Học máy dùng dữ liệu có cấu trúc."
    },
    "correct": "A",
    "explanation": "Khai phá dữ liệu tìm kiếm mô hình đã tồn tại trong tập dữ liệu lịch sử. Học máy tự học từ tập huấn luyện để đưa ra dự đoán cho tương lai."
  },
  {
    "id": 6,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Khó",
    "question": "Ghép nối các loại hình Học máy (Machine Learning) với định nghĩa chính xác nhất:\nCột 1:\n  (1) Học có giám sát (Supervised)\n  (2) Học không giám sát (Unsupervised)\n  (3) Học bán giám sát (Semi-supervised)\n  (4) Học tăng cường (Reinforcement)\nCột 2:\n  (a) Dùng dữ liệu đầu vào CHƯA được gắn nhãn để tìm ra các xu hướng, cụm (clusters)\n  (b) Kết hợp sử dụng cả dữ liệu ĐÃ được gắn nhãn và CHƯA được gắn nhãn\n  (c) Học từ tập dữ liệu ĐÃ được gắn nhãn (biết trước đầu vào X dẫn đến đầu ra Y)\n  (d) Thuật toán tự huấn luyện thông qua thử và sai (nhận phần thưởng hoặc bị phạt)\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-d, 2-b, 3-a, 4-c",
      "B": "1-a, 2-b, 3-d, 4-c",
      "C": "1-c, 2-a, 3-b, 4-d",
      "D": "1-a, 2-c, 3-b, 4-d"
    },
    "correct": "C",
    "explanation": "Có giám sát = Có nhãn sẵn; Không giám sát = Không nhãn; Bán giám sát = Dùng cả 2 loại; Tăng cường = Thử và sai (Thưởng/Phạt)."
  },
  {
    "id": 7,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Dễ",
    "question": "Hội nghị Trí tuệ nhân tạo (AI) đầu tiên được tổ chức vào năm 1956 tại trường đại học nào?",
    "options": {
      "A": "Đại học Harvard",
      "B": "Đại học Stanford",
      "C": "Đại học Dartmouth",
      "D": "Viện Công nghệ Massachusetts (MIT)"
    },
    "correct": "C",
    "explanation": "Lĩnh vực AI được thiết lập như một chuyên ngành học thuật và nghiên cứu khi hội nghị AI đầu tiên được tổ chức tại Đại học Dartmouth vào năm 1956."
  },
  {
    "id": 8,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Dễ",
    "question": "Sắp xếp các mốc lịch sử của AI và Công nghệ từ cũ nhất đến mới nhất:\n  (1) Mô hình nơ-ron nhân tạo đầu tiên do McCulloch và Pitts đề xuất (1943)\n  (2) Hội nghị AI đầu tiên tại Đại học Dartmouth (1956)\n  (3) Hệ chuyên gia (Expert Systems) ra đời (Những năm 1970)\n  (4) Phần mềm bảng tính điện tử phổ biến trong kế toán (Những năm 1980)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (4) ➔ (3)",
      "D": "(1) ➔ (2) ➔ (3) ➔ (4)"
    },
    "correct": "D",
    "explanation": "1943: Mô hình nơ-ron; 1956: Dartmouth; Những năm 1970: Hệ chuyên gia; Những năm 1980: Bảng tính điện tử."
  },
  {
    "id": 9,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Trong kế toán quản trị, trí tuệ nhân tạo (AI) thường được sử dụng để thực hiện công việc gì?",
    "options": {
      "A": "Chỉ phát hiện giao dịch gian lận trong kiểm toán",
      "B": "Tự động mã hóa bút toán kế toán, dự báo doanh thu và phân tích dữ liệu phi cấu trúc",
      "C": "Thay thế hoàn toàn giám đốc tài chính (CFO)",
      "D": "Khai thuế thủ công cho khách hàng"
    },
    "correct": "B",
    "explanation": "Trong kế toán quản trị, AI được sử dụng để tự động mã hóa các bút toán kế toán, dự báo doanh thu và phân tích các dữ liệu phi cấu trúc như hợp đồng, email."
  },
  {
    "id": 10,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Dễ",
    "question": "Hoàn thành định nghĩa sau về API:\n\"Giao diện lập trình ứng dụng (API) là một tập hợp các chức năng hoặc quy tắc tạo điều kiện cho giao tiếp giữa các ___(1)___, ___(2)___ và thiết bị.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) cơ sở dữ liệu ; (2) ứng dụng",
      "B": "(1) thuật toán ; (2) thuật toán",
      "C": "Phương án điền từ khác 3",
      "D": "(1) ứng dụng ; (2) cơ sở dữ liệu"
    },
    "correct": "D",
    "explanation": "API là tập hợp các quy tắc tạo điều kiện giao tiếp giữa ứng dụng, cơ sở dữ liệu và thiết bị, hoạt động như các 'sứ giả kỹ thuật số'."
  },
  {
    "id": 11,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ / khái niệm với ví dụ thực tiễn tương ứng:\nCột 1:\n  (1) Hiểu ngôn ngữ tự nhiên (NLU)\n  (2) Tạo ngôn ngữ tự nhiên (NLG)\n  (3) API (Giao diện lập trình ứng dụng)\nCột 2:\n  (a) Siri nhận diện và hiểu câu hỏi 'Thời tiết hôm nay thế nào?'\n  (b) Siri trả lời lại bằng giọng nói: 'Hôm nay trời quang, nhiệt độ 28 độ'\n  (c) Khách hàng mua vé xem phim qua Fandango bằng cách đăng nhập tài khoản Facebook\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "NLU giúp máy hiểu câu hỏi. NLG giúp máy phát ra câu trả lời bằng ngôn ngữ tự nhiên. API giúp Fandango kết nối với Facebook để đăng nhập."
  },
  {
    "id": 12,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Dễ",
    "question": "Ứng dụng nào của Apple sử dụng phương pháp không cần lập trình truyền thống (no-code/low-code) để phát triển mô hình Học máy?",
    "options": {
      "A": "Kubeflow",
      "B": "Create ML",
      "C": "CNTK",
      "D": "Anaconda"
    },
    "correct": "B",
    "explanation": "Ứng dụng 'Create ML' của Apple cho phép người dùng phát triển và đào tạo các mô hình ML bằng phương pháp kéo-thả (no-code/low-code)."
  },
  {
    "id": 13,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Sắp xếp các khái niệm AI từ phổ quát nhất (rộng nhất) đến chuyên biệt nhất (nhỏ nhất):\n  (1) Trí tuệ nhân tạo (AI - Artificial Intelligence)\n  (2) Học máy (ML - Machine Learning)\n  (3) Học sâu (DL - Deep Learning)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3)",
      "B": "(3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3)",
      "D": "(1) ➔ (3) ➔ (2)"
    },
    "correct": "A",
    "explanation": "Học sâu (DL) là một tập hợp con của Học máy (ML). Học máy lại là một tập hợp con của Trí tuệ nhân tạo (AI)."
  },
  {
    "id": 14,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Khó",
    "question": "Theo Xavier Amatriain, nhận định nào sau đây là ĐÚNG về mối quan hệ giữa Khai phá dữ liệu (Data Mining) và Trí tuệ nhân tạo (AI)?",
    "options": {
      "A": "Khai phá dữ liệu là một tập hợp con (sub-field) của AI.",
      "B": "Khai phá dữ liệu giao thoa với AI nhưng KHÔNG được coi là một lĩnh vực phụ của AI.",
      "C": "AI là một lĩnh vực phụ của Khai phá dữ liệu.",
      "D": "Khai phá dữ liệu và AI hoàn toàn không có sự liên quan nào."
    },
    "correct": "B",
    "explanation": "Khai phá dữ liệu giao thoa với AI nhưng không được coi là lĩnh vực phụ. Khai phá dữ liệu có thể sử dụng học máy (một phần của AI) nhưng cũng sử dụng các kỹ thuật khác ngoài học máy."
  },
  {
    "id": 15,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ nền tảng mã thấp/không mã (low-code/no-code) với nhà phát triển tương ứng:\nCột 1:\n  (1) Create ML\n  (2) Kubeflow\n  (3) CNTK (Cognitive Toolkit)\nCột 2:\n  (a) Apple\n  (b) Google\n  (c) Microsoft\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "Create ML do Apple phát triển. Kubeflow hỗ trợ trên nền tảng AI của Google. CNTK do Microsoft phát triển cho nền tảng Azure."
  },
  {
    "id": 16,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Điền từ thích hợp vào định nghĩa của Học sâu (Deep Learning):\n\"Học sâu là một tập hợp con của học máy sử dụng ___(1)___ để khám phá các mô hình từ dữ liệu. Các mô hình này thường được tăng tốc bởi ___(2)___, một mạch tích hợp chuyên dụng do Google phát triển.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) Bộ xử lý tensor (TPU) ; (2) Mạng nơ-ron nhân tạo (ANN)",
      "B": "(1) Mạng nơ-ron nhân tạo (ANN) ; (2) Bộ xử lý tensor (TPU)",
      "C": "(1) Khai phá dữ liệu ; (2) Lô-gic mờ (Fuzzy logic)",
      "D": "(1) Lô-gic mờ (Fuzzy logic) ; (2) Khai phá dữ liệu"
    },
    "correct": "B",
    "explanation": "Học sâu sử dụng mạng nơ-ron nhân tạo (ANN) lấy cảm hứng từ bộ não người và thường được tăng tốc xử lý bởi bộ xử lý tensor (TPU)."
  },
  {
    "id": 17,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Trong bối cảnh hệ chuyên gia (Expert Systems), hệ thống nào sử dụng các thuật ngữ không mang tính nhị phân (0 hoặc 1) để đối phó với sự thiếu chính xác và mơ hồ?",
    "options": {
      "A": "Hệ chuyên gia dựa trên quy tắc (Rules-based)",
      "B": "Hệ chuyên gia dựa trên lô-gic mờ (Fuzzy-based)",
      "C": "Mạng nơ-ron nhân tạo (ANN)",
      "D": "Xử lý ngôn ngữ tự nhiên (NLP)"
    },
    "correct": "B",
    "explanation": "Lô-gic mờ (fuzzy logic) hữu ích trong các tình huống liên quan đến sự thiếu chính xác và mơ hồ, nơi các điều kiện không thể phân định rõ ràng 0 hoặc 1 (đúng/sai tuyệt đối)."
  },
  {
    "id": 18,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Khó",
    "question": "Sắp xếp quy trình Khai phá văn bản (Text Mining) theo thứ tự thực hiện:\n  (1) Thu thập các nguồn dữ liệu văn bản phi cấu trúc (hợp đồng, email, PDF...)\n  (2) Áp đặt cấu trúc (structure) lên các nguồn dữ liệu văn bản phi cấu trúc này\n  (3) Sử dụng các kỹ thuật khai phá dữ liệu để trích xuất thông tin có liên quan\n  (4) Khám phá các mô hình, xu hướng và chủ đề từ thông tin trích xuất\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "B",
    "explanation": "Quá trình bắt đầu từ thu thập dữ liệu phi cấu trúc -> áp đặt cấu trúc cho nó -> sử dụng khai phá dữ liệu -> cuối cùng khám phá xu hướng/mô hình."
  },
  {
    "id": 19,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Khó",
    "question": "Ghép các công cụ / ứng dụng với phương thức tiếp cận AI của chúng:\nCột 1:\n  (1) Khai phá văn bản (Text Mining)\n  (2) Lập luận máy (Machine Reasoning)\n  (3) Phân tích cụm (Cluster Analysis)\nCột 2:\n  (a) Sử dụng NLP để trích xuất ý nghĩa từ dữ liệu văn bản\n  (b) Thao tác đại số đối với kiến thức đã thu nhận để suy luận diễn dịch/quy nạp\n  (c) Nhóm dữ liệu không gắn nhãn lại với nhau dựa trên điểm tương đồng (Học không giám sát)\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "Khai phá văn bản sử dụng NLP. Lập luận máy dùng suy luận tự động. Phân tích cụm là phương pháp điển hình của học không giám sát."
  },
  {
    "id": 20,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Dễ",
    "question": "Công nghệ RPA (Robotic Process Automation) phù hợp nhất với loại tác vụ nào?",
    "options": {
      "A": "Các tác vụ đòi hỏi sự tư duy sáng tạo nghệ thuật",
      "B": "Các tác vụ có khối lượng lớn, lặp đi lặp lại và theo quy tắc rõ ràng",
      "C": "Các quyết định chiến lược cấp hội đồng quản trị",
      "D": "Sáng tác nhạc và vẽ tranh"
    },
    "correct": "B",
    "explanation": "RPA rất phù hợp với các tác vụ có khối lượng lớn và lặp đi lặp lại (như đối chiếu ngân hàng, xử lý hóa đơn) thường do con người thực hiện trước đây."
  },
  {
    "id": 21,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Khó",
    "question": "Điền từ vào chỗ trống về Lập luận máy (Machine Reasoning):\n\"Các hệ thống Lập luận máy sử dụng kỹ thuật suy luận tự động để bắt chước con người, chẳng hạn như ___(1)___ (deduction) và ___(2)___ (induction).\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) quy nạp ; (2) diễn dịch",
      "B": "(1) dự đoán ; (2) dự đoán",
      "C": "(1) diễn dịch ; (2) quy nạp",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "C",
    "explanation": "Lập luận máy sử dụng kỹ thuật suy luận tự động như diễn dịch (từ cái chung suy ra cái riêng) và quy nạp (từ số liệu cụ thể khái quát thành cái chung)."
  },
  {
    "id": 22,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Trong ví dụ về Học có giám sát (Supervised Learning), biến đầu vào (X) và biến đầu ra (Y) được mô tả như thế nào khi dự đoán nợ xấu?",
    "options": {
      "A": "X là tuổi nợ của khách hàng, Y là số tiền nợ khó đòi đã xóa sổ",
      "B": "X là số lượng nhân viên, Y là doanh thu của công ty",
      "C": "X là dữ liệu không dán nhãn, Y là các cụm khách hàng",
      "D": "X là mức độ gian lận, Y là tên khách hàng"
    },
    "correct": "A",
    "explanation": "Trong bài, mô hình học có giám sát dùng dữ liệu lịch sử: X (đầu vào) là tuổi nợ của khách hàng, Y (đầu ra) là số tiền phải thu khó đòi bị xóa sổ."
  },
  {
    "id": 23,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình hoạt động của thuật toán Học Tăng cường (Reinforcement Learning):\n  (1) Tác nhân (agent) thực hiện một hành động (thử và sai) trong môi trường\n  (2) Nhận được phần thưởng (reward) nếu đúng, hoặc hình phạt (penalty) nếu sai\n  (3) Thuật toán học hỏi từ kết quả để điều chỉnh hành vi\n  (4) Tối đa hóa phần thưởng và giảm thiểu hình phạt trong tương lai\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "C",
    "explanation": "Học tăng cường diễn ra qua quá trình tác nhân thực hiện thử và sai -> nhận thưởng/phạt -> học hỏi -> tối đa hóa phần thưởng ở các lần sau."
  },
  {
    "id": 24,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Dễ",
    "question": "Ghép các thuật ngữ viết tắt trong AI với nghĩa tiếng Việt của nó:\nCột 1:\n  (1) NLP\n  (2) RPA\n  (3) IoT\nCột 2:\n  (a) Xử lý ngôn ngữ tự nhiên\n  (b) Tự động hóa quy trình bằng robot\n  (c) Internet vạn vật\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-a, 2-b, 3-c",
      "B": "1-c, 2-b, 3-a",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "A",
    "explanation": "NLP: Natural Language Processing. RPA: Robotic Process Automation. IoT: Internet of Things."
  },
  {
    "id": 25,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Khó",
    "question": "Theo nghiên cứu của Sophia Sun (2019), Học sâu (Deep Learning) vượt trội hơn Học máy (ML) cổ điển trong điều kiện nào?",
    "options": {
      "A": "Khi tập dữ liệu cực kỳ nhỏ và chỉ có vài biến số",
      "B": "Khi khối lượng dữ liệu và số lượng biến (variables) rất lớn",
      "C": "Khi dữ liệu hoàn toàn có cấu trúc (bảng tính SQL)",
      "D": "Khi không có sự xuất hiện của dữ liệu bán cấu trúc hay phi cấu trúc"
    },
    "correct": "B",
    "explanation": "Hiệu suất dự đoán của mô hình DL vượt trội hơn ML cổ điển khi khối lượng dữ liệu lớn và số lượng biến (variables) nhiều."
  },
  {
    "id": 26,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống để hoàn thành định nghĩa về AI của Siegel (2003):\n\"Để máy móc thực hiện được các tác vụ phức tạp tốt bằng hoặc hơn con người, chúng phải có khả năng ___(1)___, ___(2)___, học hỏi và giao tiếp.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) lập luận ; (2) cảm nhận",
      "B": "(1) bay lượn ; (2) bay lượn",
      "C": "Phương án điền từ khác 3",
      "D": "(1) cảm nhận ; (2) lập luận"
    },
    "correct": "D",
    "explanation": "Theo Siegel et al. (2003), máy móc phải có khả năng cảm nhận (perceive), lập luận (reason), học hỏi (learn) và giao tiếp (communicate)."
  },
  {
    "id": 27,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Bệnh viện Đa khoa Tampa ở Florida đã sử dụng AI trong đại dịch Covid-19 với mục đích gì?",
    "options": {
      "A": "Chẩn đoán bệnh nhân qua email",
      "B": "Quét nhiệt khuôn mặt để phát hiện các triệu chứng tiềm ẩn (sốt, mồ hôi, đổi màu da)",
      "C": "Tính toán chi phí khám bệnh tự động",
      "D": "Robot phẫu thuật từ xa"
    },
    "correct": "B",
    "explanation": "Bệnh viện Tampa triển khai AI thực hiện quét nhiệt khuôn mặt người vào tòa nhà để phát hiện triệu chứng virus như sốt, đổi màu da."
  },
  {
    "id": 28,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Dễ",
    "question": "Quy trình xử lý một lệnh thoại của Siri (ứng dụng của AI và NLP) diễn ra theo thứ tự nào?\n  (1) Người dùng nói: 'Thời tiết hôm nay thế nào?'\n  (2) NLU (Hiểu ngôn ngữ tự nhiên) giúp máy tính phân tích và hiểu yêu cầu\n  (3) Máy tính truy xuất dữ liệu thời tiết qua API Internet\n  (4) NLG (Tạo ngôn ngữ tự nhiên) chuyển dữ liệu thành câu trả lời bằng giọng nói\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (4) ➔ (3)",
      "D": "(1) ➔ (2) ➔ (3) ➔ (4)"
    },
    "correct": "D",
    "explanation": "Người dùng ra lệnh -> Máy hiểu lệnh (NLU) -> Máy lấy thông tin -> Máy trả lời lại bằng ngôn ngữ tự nhiên (NLG)."
  },
  {
    "id": 29,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Ghép các công cụ lập trình AI với đặc điểm của chúng:\nCột 1:\n  (1) Python và R\n  (2) SQL và NoSQL\n  (3) UiPath và BluePrism\nCột 2:\n  (a) Ngôn ngữ mã nguồn mở phổ biến nhất để xây dựng và tùy chỉnh ứng dụng AI/ML\n  (b) Công cụ truy xuất, chỉnh sửa và thao tác với cơ sở dữ liệu\n  (c) Các nền tảng phần mềm phổ biến cho Tự động hóa quy trình bằng robot (RPA)\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-a, 2-b, 3-c",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "B",
    "explanation": "Python/R mạnh về AI/ML. SQL/NoSQL mạnh về xử lý cơ sở dữ liệu. UiPath/BluePrism là phần mềm RPA."
  },
  {
    "id": 30,
    "session": "Buổi 1: What Accountants Need to Know",
    "difficulty": "Trung bình",
    "question": "Việc sử dụng thuật toán máy tính (như Amazon, Netflix) để đề xuất phim hoặc sản phẩm dựa trên lịch sử mua sắm của bạn là một ứng dụng phổ biến của lĩnh vực nào?",
    "options": {
      "A": "Học máy (Machine Learning)",
      "B": "Khai phá văn bản (Text Mining)",
      "C": "Lập luận máy (Machine Reasoning)",
      "D": "Tự động hóa quy trình (RPA)"
    },
    "correct": "A",
    "explanation": "Hệ thống đề xuất (recommendation engines) của Amazon hay Netflix là ví dụ kinh điển của Học máy (ML), học từ dữ liệu quá khứ để dự đoán sở thích tương lai."
  },
  {
    "id": 31,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Dễ",
    "question": "Satoshi Nakamoto đã tạo ra Bitcoin dựa trên niềm tin rằng internet cần một loại tiền tệ có tính chất gì?",
    "options": {
      "A": "Tập trung và được quản lý bởi ngân hàng trung ương",
      "B": "Phi tập trung, bảo vệ bằng mật mã và trao đổi ngang hàng",
      "C": "Được hậu thuẫn bởi vàng hoặc bạc",
      "D": "Chỉ sử dụng để thanh toán cho các dịch vụ phần mềm"
    },
    "correct": "B",
    "explanation": "Nakamoto tin rằng internet cần một loại tiền tệ phi tập trung (decentralized), được bảo vệ bằng mật mã (cryptography) và thuận lợi cho trao đổi ngang hàng (peer-to-peer exchange)."
  },
  {
    "id": 32,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Dễ",
    "question": "Sắp xếp các khái niệm sau từ cấp độ rộng nhất (bao quát nhất) đến cấp độ hẹp nhất (chuyên biệt nhất) trong khoa học máy tính:\n  (1) Trí tuệ nhân tạo (AI)\n  (2) Học máy (Machine Learning)\n  (3) Học sâu (Deep Learning)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(3) ➔ (2) ➔ (1)",
      "B": "(1) ➔ (2) ➔ (3)",
      "C": "(2) ➔ (1) ➔ (3)",
      "D": "(1) ➔ (3) ➔ (2)"
    },
    "correct": "B",
    "explanation": "Học sâu (Deep Learning) là một dạng đặc biệt của Học máy (Machine Learning), và Học máy là một nhánh của Trí tuệ nhân tạo (AI)."
  },
  {
    "id": 33,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Ghép các loại tiền mã hóa với đặc điểm nổi bật của chúng:\nCột 1:\n  (1) Bitcoin\n  (2) Ethereum\n  (3) Zcash\nCột 2:\n  (a) Nền tảng phần mềm phi tập trung cho phép chạy Hợp đồng thông minh (Smart Contracts)\n  (b) Tiền mã hóa đầu tiên, dựa trên mô hình ngang hàng (P2P), không phụ thuộc tổ chức phát hành\n  (c) Cung cấp tính năng an toàn hơn thông qua các giao dịch được che chắn (shielded transactions)\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-a, 3-b",
      "B": "1-a, 2-c, 3-b",
      "C": "1-a, 2-b, 3-c",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "D",
    "explanation": "Bitcoin là tiền mã hóa tiên phong. Ethereum nổi bật với Hợp đồng thông minh. Zcash tập trung vào quyền riêng tư bằng các giao dịch được che chắn."
  },
  {
    "id": 34,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Hoàn thành nhận định về sự khác biệt giữa AI, ML và Khoa học Dữ liệu:\n\"___(1)___ và ___(2)___ không cấu thành nên một nhánh của khoa học dữ liệu. Thay vào đó, ___(3)___ sử dụng chúng như một bộ công cụ thống kê để giải quyết các vấn đề từ dữ liệu.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) Khoa học Dữ liệu ; (2) Học máy (ML) ; (3) Trí tuệ nhân tạo (AI)",
      "B": "(1) Trí tuệ nhân tạo (AI) ; (2) Học máy (ML) ; (3) Khoa học Dữ liệu",
      "C": "(1) Tự động hóa (RPA) ; (2) Tự động hóa (RPA) ; (3) Tự động hóa (RPA)",
      "D": "(1) Học máy (ML) ; (2) Khoa học Dữ liệu ; (3) Trí tuệ nhân tạo (AI)"
    },
    "correct": "B",
    "explanation": "AI và ML là các công cụ mà Khoa học Dữ liệu sử dụng. Khoa học Dữ liệu là quy trình rộng hơn bao gồm thu thập, phân tích, trực quan hóa và mô hình hóa."
  },
  {
    "id": 35,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Khó",
    "question": "Quan điểm của Tòa án Tối cao Tây Ban Nha (2019) về bản chất pháp lý của Bitcoin là gì?",
    "options": {
      "A": "Bitcoin được công nhận là một loại tiền tệ hợp pháp (legal tender)",
      "B": "Bitcoin bị từ chối công nhận là tiền hợp pháp nhưng được coi là 'tài sản vô hình' (incorporeal asset)",
      "C": "Bitcoin bị cấm hoàn toàn trong các giao dịch thương mại",
      "D": "Bitcoin được coi là một dạng chứng khoán phái sinh (derivative security)"
    },
    "correct": "B",
    "explanation": "Bản án của Tòa án Tối cao Tây Ban Nha ngày 20/06/2019 đã từ chối công nhận Bitcoin là tiền tệ hợp pháp (money) mà coi nó là một tài sản vô hình."
  },
  {
    "id": 36,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Dễ",
    "question": "Ba trụ cột chuyên môn (theo biểu đồ Venn) tạo nên một Nhà khoa học dữ liệu (Data Scientist) là gì?",
    "options": {
      "A": "Thống kê/Toán học, Khoa học máy tính, và Chuyên môn ngành (Domain expertise)",
      "B": "Tài chính kế toán, Nhân sự, và Marketing",
      "C": "Lập trình web, Thiết kế đồ họa, và Quản trị kinh doanh",
      "D": "Trí tuệ nhân tạo, Khai phá văn bản, và Lập luận máy"
    },
    "correct": "A",
    "explanation": "Khoa học dữ liệu là lĩnh vực liên ngành sử dụng Thống kê/Toán học, Khoa học máy tính và Chuyên môn trong lĩnh vực cụ thể."
  },
  {
    "id": 37,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Ghép nối các khái niệm trong Vũ trụ ảo (Metaverse) với ý nghĩa của chúng:\nCột 1:\n  (1) Vũ trụ ảo mã hóa (Crypto-metaverse)\n  (2) Giao dịch thuật toán (Algorithmic trading)\n  (3) Tài chính phi tập trung (DeFi) trong Metaverse\nCột 2:\n  (a) Sự tích hợp mạnh mẽ giữa công nghệ chuỗi khối và tiền mã hóa vào các môi trường ảo\n  (b) Thực hiện giao dịch tự động trên thị trường nhờ các thuật toán AI\n  (c) Cho phép người dùng đi vay, cho vay và kiếm lợi nhuận ngay trong thế giới ảo mà không cần ngân hàng truyền thống\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "Metaverse sử dụng Crypto (blockchain/coin) làm nền tảng kinh tế. AI hỗ trợ giao dịch thuật toán tự động. DeFi giúp giao dịch tài chính không cần trung gian."
  },
  {
    "id": 38,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Khó",
    "question": "Quy trình ứng dụng NFT (được tạo bởi AI) làm tài sản thế chấp trong hệ sinh thái DeFi diễn ra theo trình tự nào?\n  (1) AI sáng tạo hoặc hợp tác với nghệ sĩ để tạo ra tác phẩm nghệ thuật số\n  (2) Tác phẩm nghệ thuật số được mã hóa (tokenized) thành một NFT trên chuỗi khối\n  (3) Người dùng mang NFT này thế chấp (collateral) vào một nền tảng DeFi\n  (4) Người dùng nhận được khoản vay (bằng crypto) mà không cần phải bán đứt NFT\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (4) ➔ (3)",
      "D": "(1) ➔ (2) ➔ (3) ➔ (4)"
    },
    "correct": "D",
    "explanation": "Đầu tiên tạo tác phẩm (bằng AI) -> Mã hóa thành NFT -> Thế chấp trên DeFi -> Nhận khoản vay. Đây là ứng dụng thanh khoản mới cho NFT."
  },
  {
    "id": 39,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Dễ",
    "question": "Điền từ thích hợp để hoàn thành khái niệm về sự kết hợp giữa Chuỗi khối và AI:\n\"___(1)___ cung cấp tính minh bạch, bảo mật và hồ sơ giao dịch không thể sửa đổi. Trong khi đó, ___(2)___ đóng góp vào việc phân tích dự đoán và tự động hóa theo thời gian thực.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) Trí tuệ nhân tạo (AI) ; (2) Công nghệ Chuỗi khối (Blockchain)",
      "B": "(1) Dữ liệu lớn (Big Data) ; (2) Dữ liệu lớn (Big Data)",
      "C": "(1) Công nghệ Chuỗi khối (Blockchain) ; (2) Trí tuệ nhân tạo (AI)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "C",
    "explanation": "Blockchain bảo đảm dữ liệu an toàn và bất biến, còn AI dùng dữ liệu đó để phân tích và đưa ra quyết định dự đoán."
  },
  {
    "id": 40,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "CBDC (Central Bank Digital Currency) là gì?",
    "options": {
      "A": "Đồng tiền ảo do một nhóm lập trình viên ẩn danh tạo ra",
      "B": "Tiền kỹ thuật số được phát hành và kiểm soát bởi ngân hàng trung ương của một quốc gia",
      "C": "Một thuật toán khai phá dữ liệu trên thị trường chứng khoán",
      "D": "Hệ thống máy chủ đám mây của các ngân hàng thương mại"
    },
    "correct": "B",
    "explanation": "CBDC (Central Bank Digital Currency) là nỗ lực của các chính phủ bước vào cuộc chơi tài sản kỹ thuật số nhằm phát hành tiền kỹ thuật số mang tính quốc gia."
  },
  {
    "id": 41,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Khó",
    "question": "Theo quan điểm của Tổng biện lý (Advocate General), lý do chính khiến Bitcoin KHÔNG được coi là 'Tiền' là gì?",
    "options": {
      "A": "Vì nó chỉ được sử dụng ở Châu Âu",
      "B": "Vì nó không thực hiện đủ 3 chức năng: phương tiện trao đổi, công cụ lưu trữ giá trị, và đơn vị kế toán, đồng thời không được thực thể trung tâm nào hậu thuẫn",
      "C": "Vì giá trị vốn hóa của nó còn quá thấp (dưới 1 triệu Euro)",
      "D": "Vì nó sử dụng công nghệ chuỗi khối quá phức tạp"
    },
    "correct": "B",
    "explanation": "Tổng biện lý cho rằng Bitcoin chậm chạp, tốn kém, không đảm bảo chuyển đổi ra tiền mặt và không có sự quản lý/hậu thuẫn từ cơ quan công quyền, nên không thực hiện đủ chức năng của tiền."
  },
  {
    "id": 42,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Sự khác biệt giữa Nhà khoa học dữ liệu và Nhà phân tích kinh doanh/dữ liệu:\nCột 1:\n  (1) Nhà phân tích kinh doanh (Business Analyst)\n  (2) Nhà khoa học dữ liệu (Data Scientist)\nCột 2:\n  (a) Sử dụng chuyên môn ngành và phân tích để tạo insight, ít tập trung vào lập trình mô hình học máy\n  (b) Vai trò rộng hơn, bao gồm lập trình, phân tích thống kê và xây dựng mô hình học máy (Machine Learning)\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-a, 2-b",
      "B": "1-b, 2-a",
      "C": "Phương án ghép cặp khác 2",
      "D": "Phương án ghép cặp khác 3"
    },
    "correct": "A",
    "explanation": "Business Analyst tập trung vào business insight. Data Scientist có kỹ năng lập trình và toán học cao hơn để xây dựng các mô hình dự đoán (ML/AI)."
  },
  {
    "id": 43,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Dễ",
    "question": "Quá trình một Nhà khoa học dữ liệu giải quyết vấn đề bằng Học máy diễn ra theo các bước chung nào?\n  (1) Thu thập dữ liệu (Data collection)\n  (2) Xử lý và làm sạch dữ liệu (Data processing)\n  (3) Xây dựng mô hình Học máy (Modeling)\n  (4) Đưa ra các dự đoán và trực quan hóa kết quả\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Quy trình tiêu chuẩn: Thu thập -> Tiền xử lý (làm sạch) -> Xây dựng mô hình -> Dự đoán/Đánh giá."
  },
  {
    "id": 44,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Khó",
    "question": "Điền từ vào chỗ trống liên quan đến rủi ro không gian mạng của Metaverse:\n\"Sự xuất hiện của vũ trụ ảo làm tăng bề mặt tấn công cho các đối tượng độc hại bằng cách tạo ra nhiều điểm xâm nhập hơn cho ___(1)___ và các vụ ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) rò rỉ dữ liệu (data breaches) ; (2) phần mềm độc hại (malware)",
      "B": "(1) tiền ảo (virtual money) ; (2) tiền ảo (virtual money)",
      "C": "Phương án điền từ khác 3",
      "D": "(1) phần mềm độc hại (malware) ; (2) rò rỉ dữ liệu (data breaches)"
    },
    "correct": "D",
    "explanation": "Quá trình số hóa và tích hợp Metaverse mang lại rủi ro lớn về an ninh mạng như malware và rò rỉ dữ liệu do tăng số lượng điểm xâm nhập."
  },
  {
    "id": 45,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Hợp đồng thông minh (Smart Contracts) hoạt động trên công nghệ nào?",
    "options": {
      "A": "Dữ liệu lớn (Big Data)",
      "B": "Chuỗi khối (Blockchain)",
      "C": "Máy chủ ngân hàng tập trung",
      "D": "Các hệ thống ERP truyền thống"
    },
    "correct": "B",
    "explanation": "Hợp đồng thông minh là các đoạn mã chạy trên nền tảng Chuỗi khối (Blockchain) như Ethereum, tự động thực thi các thỏa thuận mà không cần bên trung gian."
  },
  {
    "id": 46,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Sự kết hợp giữa Chuỗi khối và AI mang lại lợi ích gì trong tài chính?\nCột 1:\n  (1) Tính minh bạch từ Chuỗi khối\n  (2) Khả năng phân tích của AI\n  (3) Cố vấn rô-bốt (Robo-advisors)\nCột 2:\n  (a) Đảm bảo tất cả các bên có quyền truy cập vào một phiên bản thống nhất của sự thật (bất biến)\n  (b) Chủ động xác định các mối đe dọa tiềm ẩn (như gian lận) theo thời gian thực\n  (c) Đưa ra các đề xuất đầu tư được cá nhân hóa dựa trên phân tích dự đoán\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-a, 2-b, 3-c",
      "B": "1-c, 2-b, 3-a",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "A",
    "explanation": "Blockchain bảo đảm dữ liệu. AI xử lý phân tích và phát hiện rủi ro. Cố vấn rô-bốt kết hợp AI để tự động hóa tư vấn đầu tư."
  },
  {
    "id": 47,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Tại sao một số người cho rằng Bitcoin cần có các trung gian tài chính để phát triển thành một loại tiền tệ ổn định?",
    "options": {
      "A": "Vì Blockchain không đủ bảo mật để lưu trữ Bitcoin",
      "B": "Vì cần trung gian để cho phép 'khám phá giá' (price discovery) và tạo quỹ hoán đổi danh mục (ETFs)",
      "C": "Vì chính phủ yêu cầu mọi người dân phải gửi Bitcoin vào ngân hàng",
      "D": "Vì Bitcoin có chi phí giao dịch quá đắt nếu không qua ngân hàng"
    },
    "correct": "B",
    "explanation": "John O. McGinnis lập luận rằng Bitcoin cần các cơ chế tài chính như ETF và sự 'khám phá giá' (do trung gian thực hiện) để có chiều sâu thị trường và ổn định hơn, dù nó được sinh ra để chống lại trung gian."
  },
  {
    "id": 48,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình AI hỗ trợ quản lý thị trường NFT:\n  (1) Thu thập dữ liệu xu hướng thị trường và sở thích của người mua\n  (2) AI phân tích dữ liệu bằng các thuật toán tiên tiến\n  (3) Đề xuất các tác phẩm nghệ thuật NFT phù hợp cho người mua tiềm năng\n  (4) Đồng thời AI quét để phát hiện các vi phạm bản quyền hoặc bản sao (duplicates)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "B",
    "explanation": "AI vừa đóng vai trò như hệ thống đề xuất (tương tự Amazon/Netflix) cho NFT, vừa đóng vai trò kiểm duyệt (xác thực tính nguyên bản) trên thị trường."
  },
  {
    "id": 49,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Điền từ vào định nghĩa về Ngân hàng ảo:\n\"Ngân hàng ảo (virtual banking) khác biệt so với ngân hàng điện tử (electronic banking) ở chỗ nó không phụ thuộc vào bất kỳ ___(1)___ nào. Chúng cung cấp quy trình mở tài khoản nhanh chóng và tuân thủ các yêu cầu ___(2)___ thông qua công nghệ kỹ thuật số.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) cơ sở hạ tầng vật lý (phòng giao dịch) ; (2) KYC (Nhận biết khách hàng)",
      "B": "(1) KYC (Nhận biết khách hàng) ; (2) cơ sở hạ tầng vật lý (phòng giao dịch)",
      "C": "(1) thị trường chứng khoán ; (2) thị trường chứng khoán",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "A",
    "explanation": "Ngân hàng ảo hoạt động 100% online không cần chi nhánh vật lý, và sử dụng e-KYC để định danh khách hàng."
  },
  {
    "id": 50,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Dễ",
    "question": "Nhận định nào sau đây là ĐÚNG về Dữ liệu lớn (Big Data)?",
    "options": {
      "A": "Dữ liệu lớn là một nhánh nhỏ của Khoa học dữ liệu.",
      "B": "Dữ liệu lớn là lượng dữ liệu rất lớn mà các công cụ cơ sở dữ liệu truyền thống không thể quản lý và phân tích được.",
      "C": "Dữ liệu lớn chỉ chứa dữ liệu ở dạng văn bản (text).",
      "D": "Chỉ các tập đoàn công nghệ mới được phép sở hữu Dữ liệu lớn."
    },
    "correct": "B",
    "explanation": "Big Data có khối lượng, tốc độ, độ đa dạng... vượt qua khả năng của các hệ thống cơ sở dữ liệu quan hệ truyền thống."
  },
  {
    "id": 51,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Khó",
    "question": "Ghép các quy định / chính sách với mục đích của nó trong hệ thống tài chính & blockchain:\nCột 1:\n  (1) AML (Anti-Money Laundering)\n  (2) KYC (Know Your Customer)\n  (3) GDPR (Quy định chung về Bảo vệ Dữ liệu)\nCột 2:\n  (a) Quy định chống rửa tiền, ngăn chặn việc hợp pháp hóa nguồn tiền bất hợp pháp\n  (b) Quy trình xác minh danh tính và đánh giá rủi ro của khách hàng\n  (c) Luật bảo vệ quyền riêng tư và dữ liệu cá nhân (điển hình tại Châu Âu)\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-a, 2-b, 3-c",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "B",
    "explanation": "Các mô hình phát hiện gian lận dựa trên Blockchain/AI phải tuân thủ nghiêm ngặt AML, KYC và GDPR để đảm bảo minh bạch và tính pháp lý."
  },
  {
    "id": 52,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Khó",
    "question": "Theo Michael Conklin, việc các doanh nghiệp đầu tư và chấp nhận tiền mã hóa như một phương thức thanh toán có thể vi phạm điều gì?",
    "options": {
      "A": "Luật chống độc quyền của Hoa Kỳ",
      "B": "Lý thuyết các bên liên quan (stakeholder theory) của đạo đức doanh nghiệp",
      "C": "Luật bảo vệ môi trường do việc đào coin tiêu tốn nhiều năng lượng",
      "D": "Công ước Geneva về tiền tệ quốc tế"
    },
    "correct": "B",
    "explanation": "Conklin cho rằng do tính biến động cao và các rủi ro khác, việc doanh nghiệp đầu tư tiền mã hóa là vi phạm lý thuyết các bên liên quan (bảo vệ lợi ích của cổ đông, nhân viên...) trong đạo đức doanh nghiệp."
  },
  {
    "id": 53,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Dễ",
    "question": "Điền từ thích hợp nói về sự sáng tạo của AI và NFT:\n\"Sự đổi mới xuất hiện khi triển khai các ý tưởng mới. Nếu ___(1)___ tự chủ tạo ra các tác phẩm nghệ thuật, điều này gây ra các tranh cãi liên quan đến quyền tác giả (authorship) và ___(2)___ khi mã hóa thành NFT.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) Trí tuệ nhân tạo (AI) ; (2) bản quyền (copyright)",
      "B": "(1) bản quyền (copyright) ; (2) Trí tuệ nhân tạo (AI)",
      "C": "(1) thế chấp (collateral) ; (2) thế chấp (collateral)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "A",
    "explanation": "Khi AI tạo ra nghệ thuật, việc xác định ai sở hữu 'bản quyền' và 'quyền tác giả' trở nên phức tạp, nhất là khi chúng được thương mại hóa qua NFT."
  },
  {
    "id": 54,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Khó",
    "question": "Sắp xếp quá trình tiến hóa của tiền tệ theo lịch sử (từ cũ đến mới) dựa trên tài liệu đọc:\n  (1) Tiền kim loại / Tiền xu (Specie extraction)\n  (2) Tiền giấy và sự quản lý cung tiền bằng chính sách tiền tệ của Ngân hàng trung ương\n  (3) Chuyển tiền điện tử (Electronic money/banking)\n  (4) Tiền mã hóa phi tập trung (Cryptocurrencies) và Tiền kỹ thuật số của NHTW (CBDC)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (4) ➔ (3)",
      "D": "(1) ➔ (2) ➔ (3) ➔ (4)"
    },
    "correct": "D",
    "explanation": "Lịch sử tiền tệ: Kim loại -> Giấy do Nhà nước quản lý -> Tiền điện tử (thẻ/app) -> Crypto (phi tập trung) và CBDC."
  },
  {
    "id": 55,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Điều gì là RÀO CẢN lớn nhất đối với sự đổi mới có trách nhiệm trong hệ sinh thái tiền mã hóa hiện nay?",
    "options": {
      "A": "Tốc độ internet quá chậm",
      "B": "Thiếu sự chắc chắn về mặt pháp lý (Legal uncertainty)",
      "C": "Không có đủ máy tính để đào coin",
      "D": "Sự phản đối của các nhà đầu tư bán lẻ"
    },
    "correct": "B",
    "explanation": "Tài liệu nêu rõ: Việc thiếu sự chắc chắn về mặt pháp lý là một 'rào cản khổng lồ' đối với sự đổi mới có trách nhiệm trong hệ sinh thái tiền mã hóa."
  },
  {
    "id": 56,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ với tính năng cốt lõi của chúng trong tài chính ảo:\nCột 1:\n  (1) Thực tế tăng cường (AR) / Thực tế ảo (VR)\n  (2) DeFi (Tài chính phi tập trung)\n  (3) NFTs (Non-Fungible Tokens)\nCột 2:\n  (a) Vật chất hóa không gian hiển thị và tương tác của Vũ trụ ảo (Metaverse)\n  (b) Cung cấp dịch vụ vay, cho vay không cần qua trung gian ngân hàng\n  (c) Đại diện chứng nhận tính sở hữu độc nhất cho các tài sản kỹ thuật số hoặc nghệ thuật\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-a, 2-b, 3-c",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "C",
    "explanation": "AR/VR tạo ra môi trường ảo (Metaverse). DeFi thay thế chức năng ngân hàng truyền thống. NFT đảm bảo tính độc nhất của tài sản kỹ thuật số."
  },
  {
    "id": 57,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Dễ",
    "question": "Tính năng nào KHÔNG phải là đặc điểm của công nghệ Chuỗi khối (Blockchain)?",
    "options": {
      "A": "Phi tập trung (Decentralized)",
      "B": "Bảo mật bằng mật mã (Cryptographically secured)",
      "C": "Dữ liệu có thể dễ dàng bị chỉnh sửa bởi bất kỳ ai",
      "D": "Sổ cái công khai phân tán (Distributed public ledger)"
    },
    "correct": "C",
    "explanation": "Đặc trưng lớn nhất của Blockchain là tính bất biến; một khi dữ liệu được ghi lại, nó KHÔNG bị ảnh hưởng bởi việc sửa đổi."
  },
  {
    "id": 58,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống về đặc tính của học sâu (Deep learning):\n\"Các thuật toán học máy đôi khi gặp hạn chế vì hiệu suất phụ thuộc vào cách dữ liệu được chuẩn bị. ___(1)___ giải quyết vấn đề này bằng cách tự mình trích xuất thông tin, giúp cho việc học của máy tính trở nên mạnh mẽ, linh hoạt và ___(2)___ hơn.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) trừu tượng (abstract) ; (2) Học sâu (Deep Learning)",
      "B": "(1) Học sâu (Deep Learning) ; (2) trừu tượng (abstract)",
      "C": "(1) Cơ sở dữ liệu (Database) ; (2) Cơ sở dữ liệu (Database)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "Deep Learning tự động trích xuất các đặc trưng (features) từ dữ liệu thô, giúp quá trình nhận diện linh hoạt và trừu tượng hơn ML truyền thống."
  },
  {
    "id": 59,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Trình tự tích hợp tài sản vật lý vào nền kinh tế kỹ thuật số DeFi:\n  (1) Xác định tài sản thế giới thực (bất động sản, hàng xa xỉ)\n  (2) Mã hóa (Tokenize) chứng thư sở hữu của tài sản thành NFT\n  (3) Đưa NFT lên giao dịch hoặc làm tài sản thế chấp trong hệ sinh thái DeFi\n  (4) Tăng cường tính thanh khoản và mở rộng cơ hội đầu tư cho tài sản đó\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Mã hóa tài sản thực (RWA - Real World Assets) bắt đầu từ việc chọn tài sản -> biến thành NFT -> thế chấp trên DeFi -> tạo thanh khoản."
  },
  {
    "id": 60,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "difficulty": "Trung bình",
    "question": "Việc sử dụng thuật toán (ví dụ GNN) để phát hiện gian lận tài chính trong Blockchain/AI cần đáp ứng điều kiện tiên quyết nào?",
    "options": {
      "A": "Phải có nguồn dữ liệu bí mật từ hacker",
      "B": "Phải minh bạch, có thể kiểm toán được và tuân thủ các quy định về AML, KYC, GDPR",
      "C": "Chỉ hoạt động được với Bitcoin, không dùng cho các coin khác",
      "D": "Hệ thống phải tự động đóng băng tài khoản mà không cần con người xem xét"
    },
    "correct": "B",
    "explanation": "Các mô hình phát hiện gian lận dựa trên GNN phải tuân thủ các quy định về AML, KYC và GDPR; điều này có nghĩa là hệ thống phải minh bạch và có thể kiểm toán."
  },
  {
    "id": 61,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Dễ",
    "question": "Mạng nơ-ron nhân tạo (ANNs) thường được sử dụng cho mục đích gì?",
    "options": {
      "A": "Phân tích báo cáo tài chính thủ công",
      "B": "Nhận dạng mẫu (pattern recognition) như nhận dạng khuôn mặt và giọng nói",
      "C": "In ấn tài liệu",
      "D": "Chỉ dùng để gửi email tự động"
    },
    "correct": "B",
    "explanation": "ANNs thường được sử dụng cho nhận dạng mẫu như nhận dạng khuôn mặt trong hình ảnh và video, nhận dạng giọng nói, mạng xã hội, v.v."
  },
  {
    "id": 62,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Dễ",
    "question": "Sắp xếp quá trình hoạt động của Xử lý Ngôn ngữ Tự nhiên (NLP) khi Siri trả lời câu hỏi về thời tiết:\n  (1) Người dùng đặt câu hỏi: 'Này Siri, thời tiết thế nào?'\n  (2) NLU (Hiểu ngôn ngữ tự nhiên) giúp Siri hiểu yêu cầu của người dùng\n  (3) Siri tìm kiếm thông tin thời tiết trên Internet\n  (4) NLG (Tạo ngôn ngữ tự nhiên) chuyển dữ liệu thời tiết thành câu trả lời bằng giọng nói để phản hồi người dùng\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "B",
    "explanation": "NLP gồm hai phần: NLU (để máy tính hiểu người) và NLG (để máy tính nói lại cho người hiểu)."
  },
  {
    "id": 63,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Ghép nối các khái niệm về xử lý dữ liệu và ngôn ngữ với định nghĩa của chúng:\nCột 1:\n  (1) NLU (Hiểu ngôn ngữ tự nhiên)\n  (2) NLG (Tạo ngôn ngữ tự nhiên)\n  (3) Text mining (Khai phá văn bản)\nCột 2:\n  (a) Cho phép máy tính hiểu các hướng dẫn được cung cấp bằng ngôn ngữ của con người\n  (b) Chuyển đổi dữ liệu và kết quả thành mô tả bằng lời nói mà con người có thể hiểu được\n  (c) Trích xuất thông tin từ các nguồn văn bản phi cấu trúc (email, pdf) để khám phá mẫu/chủ đề\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "NLU là máy hiểu người, NLG là máy giao tiếp với người, Text mining là trích xuất insight từ tài liệu văn bản."
  },
  {
    "id": 64,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Điền từ thích hợp nói về sự khác biệt giữa Khai phá dữ liệu và Học máy (theo Bernard Marr):\n\"Khai phá dữ liệu tìm kiếm các mẫu đã tồn tại trong ___(1)___, trong khi học máy cố gắng dự đoán các kết quả trong tương lai. Khai phá dữ liệu dựa vào sự can thiệp của ___(2)___ trong suốt quá trình, trong khi phần lớn quá trình học tập với học máy là tự động.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) con người ; (2) dữ liệu lịch sử (historical data)",
      "B": "(1) dữ liệu lịch sử (historical data) ; (2) con người",
      "C": "(1) thuật toán ; (2) thuật toán",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "Khai phá dữ liệu phân tích dữ liệu lịch sử và cần nhiều sự can thiệp phân tích của con người hơn học máy tự động."
  },
  {
    "id": 65,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Khó",
    "question": "Nhà nghiên cứu Sophia Sun (2019) đã thúc đẩy việc sử dụng học sâu (DL) trong kiểm toán vào 2 lĩnh vực chính nào?",
    "options": {
      "A": "Kiểm kê kho bãi và tính lương",
      "B": "Xác định thông tin (từ dữ liệu văn bản, hình ảnh, âm thanh) và hỗ trợ đánh giá (ra quyết định)",
      "C": "Thiết kế website và quảng cáo trên mạng xã hội",
      "D": "Tự động hóa hoàn toàn việc sa thải nhân viên"
    },
    "correct": "B",
    "explanation": "Sun (2019) thúc đẩy việc sử dụng học sâu để hỗ trợ ra quyết định kiểm toán trong hai lĩnh vực chính: xác định thông tin và hỗ trợ đánh giá."
  },
  {
    "id": 66,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Dễ",
    "question": "RPA (Tự động hóa quy trình bằng robot) rất phù hợp với loại công việc nào?",
    "options": {
      "A": "Các công việc mang tính sáng tạo cao, thay đổi liên tục",
      "B": "Các tác vụ có khối lượng lớn, lặp đi lặp lại thường do con người thực hiện (vd: đối chiếu ngân hàng, xử lý hóa đơn)",
      "C": "Các công việc cần sự đồng cảm và thấu hiểu tâm lý khách hàng",
      "D": "Khám phá các mô hình dữ liệu chưa từng được biết đến"
    },
    "correct": "B",
    "explanation": "RPA là một ứng dụng phần mềm tự động hóa các quy trình kinh doanh bằng cách lặp lại các hành động của con người, rất phù hợp cho các tác vụ lặp đi lặp lại."
  },
  {
    "id": 67,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Ghép các công cụ / nền tảng với chức năng / đặc điểm của chúng:\nCột 1:\n  (1) TPU (Bộ xử lý tensor)\n  (2) API (Giao diện lập trình ứng dụng)\n  (3) UiPath, Automation Anywhere\nCột 2:\n  (a) Mạch chuyên dụng do Google phát triển để tăng tốc độ xử lý cho ứng dụng AI/ML\n  (b) Đóng vai trò như 'người đưa tin', cho phép các phần mềm và nền tảng khác nhau giao tiếp với nhau\n  (c) Các nhà cung cấp phần mềm hàng đầu trong lĩnh vực tự động hóa RPA\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "TPU tăng tốc AI. API kết nối phần mềm. UiPath là phần mềm RPA phổ biến."
  },
  {
    "id": 68,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Khó",
    "question": "Sắp xếp quy trình khai phá văn bản (Text mining) được mô tả trong tài liệu:\n  (1) Thu thập các nguồn văn bản phi cấu trúc (ví dụ: hợp đồng, email, bài đăng MXH)\n  (2) Áp đặt cấu trúc (structure) lên các nguồn dữ liệu văn bản phi cấu trúc này\n  (3) Sử dụng các kỹ thuật khai phá dữ liệu để trích xuất thông tin liên quan (khái niệm, mẫu, xu hướng)\n  (4) Ứng dụng thông tin đó (vd: phát hiện từ ngữ buộc tội trong kế toán pháp y)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (4) ➔ (3)",
      "D": "(1) ➔ (2) ➔ (3) ➔ (4)"
    },
    "correct": "D",
    "explanation": "Quá trình 2 bước: 1. Áp đặt cấu trúc lên văn bản, 2. Sử dụng kỹ thuật khai phá để trích xuất thông tin, sau đó là ứng dụng."
  },
  {
    "id": 69,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Dễ",
    "question": "Điền từ thích hợp liên quan đến ngôn ngữ lập trình cho kế toán viên:\n\"Sự thành thạo các công cụ lập trình mã nguồn mở (open-source) phổ biến cho AI, chẳng hạn như ___(1)___ và ___(2)___, sẽ cho phép các kế toán viên tùy chỉnh các ứng dụng AI.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) R ; (2) Python",
      "B": "(1) HTML ; (2) HTML",
      "C": "(1) Python ; (2) R",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "C",
    "explanation": "Python và R là 2 ngôn ngữ phổ biến nhất được khuyên học cho Data Science và AI."
  },
  {
    "id": 70,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Sự kiện thị trường 'Sự cố chớp nhoáng' (flash crash) ngày 6 tháng 5 năm 2010 đã làm giảm 1000 điểm Dow Jones trong vài phút được cho là do đâu?",
    "options": {
      "A": "Do sự sụp đổ của một ngân hàng ảo trên Metaverse",
      "B": "Do giao dịch thuật toán tần suất cao (Algorithmic trading) gây thao túng và mất ổn định thị trường",
      "C": "Do rò rỉ dữ liệu của Equifax",
      "D": "Do một chatbot AI tư vấn sai cho khách hàng"
    },
    "correct": "B",
    "explanation": "Giao dịch thuật toán tần suất cao đã kích hoạt đợt bán tháo tự động dây chuyền, gây ra flash crash."
  },
  {
    "id": 71,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Khó",
    "question": "Trong trường hợp của Ngân hàng HDFC, việc sử dụng học máy để chấm điểm tín dụng đã làm dấy lên vấn đề đạo đức nào lớn nhất?",
    "options": {
      "A": "Quyền riêng tư dữ liệu",
      "B": "Thao túng thị trường",
      "C": "Sự thiên vị (biases) dẫn đến phân biệt đối xử trong các lựa chọn cho vay",
      "D": "Mất việc làm của nhân viên ngân hàng"
    },
    "correct": "C",
    "explanation": "Nghiên cứu chỉ ra rằng các đánh giá của thuật toán AI chấm điểm tín dụng đôi khi bị thiên vị, gây ra sự phân biệt đối xử khi cấp khoản vay."
  },
  {
    "id": 72,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Ghép tên các doanh nghiệp/tổ chức với vấn đề hoặc công nghệ cốt lõi mà họ gặp phải (trong Case Study):\nCột 1:\n  (1) Ngân hàng ICICI\n  (2) Paytm\n  (3) Aditya Birla Capital\nCột 2:\n  (a) Sử dụng chatbot AI (iPal) làm dấy lên các lo ngại về quyền riêng tư và bảo mật thông tin khách hàng\n  (b) Cung cấp nền tảng giao dịch thuật toán (Algorithmic trading) gây lo ngại về tính công bằng và thao túng thị trường\n  (c) Sử dụng NLP để tư vấn đầu tư cá nhân hóa, đồng thời đối mặt với nhu cầu bảo vệ dữ liệu tài chính nhạy cảm\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-a, 2-b, 3-c",
      "B": "1-c, 2-b, 3-a",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "A",
    "explanation": "ICICI liên quan đến chatbot iPal. Paytm liên quan giao dịch thuật toán. Aditya Birla liên quan tư vấn đầu tư bằng NLP."
  },
  {
    "id": 73,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Dễ",
    "question": "Sắp xếp theo thứ tự mức độ can thiệp vào ngôn ngữ tự nhiên từ thấp đến cao (từ đọc dữ liệu thô đến tạo ra phản hồi):\n  (1) Dữ liệu văn bản phi cấu trúc (Unstructured Text Data)\n  (2) Phân tích ngữ nghĩa và khai phá văn bản (Text mining)\n  (3) Hiểu ngôn ngữ tự nhiên (NLU) - Máy hiểu ý định\n  (4) Tạo ngôn ngữ tự nhiên (NLG) - Máy tự động phát sinh câu trả lời\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Quy trình bắt đầu từ văn bản thô -> Trích xuất dữ liệu cơ bản -> Hiểu ngữ nghĩa chuyên sâu (NLU) -> Sinh ra văn bản phản hồi mới (NLG)."
  },
  {
    "id": 74,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Khó",
    "question": "Điền từ vào chỗ trống liên quan đến rủi ro của AI Tạo sinh trong tài chính:\n\"Sự phát triển nhanh chóng của AI thường vượt qua khả năng của nhà quản lý trong việc thiết lập ___(1)___, dẫn đến những khoảng trống trong tuân thủ. Hơn nữa, việc tự động hóa có thể dẫn đến ___(2)___ và bất bình đẳng kinh tế.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) mất việc làm (job displacement) ; (2) khuôn khổ pháp lý (legal frameworks)",
      "B": "(1) thuật toán ; (2) thuật toán",
      "C": "Phương án điền từ khác 3",
      "D": "(1) khuôn khổ pháp lý (legal frameworks) ; (2) mất việc làm (job displacement)"
    },
    "correct": "D",
    "explanation": "Tài liệu nhắc đến 2 rủi ro: sự chậm trễ của luật pháp (Regulatory Compliance gap) và mất việc làm (Job displacement) do tự động hóa."
  },
  {
    "id": 75,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Để xử lý dữ liệu có cấu trúc (structured data) trong một hệ thống ERP nhằm phát hiện gian lận giao dịch, kế toán viên nên sử dụng công nghệ nào sau đây là trực tiếp nhất?",
    "options": {
      "A": "Khai phá văn bản (Text Mining)",
      "B": "Khai phá dữ liệu (Data Mining)",
      "C": "Thực tế ảo (VR)",
      "D": "Tạo ngôn ngữ tự nhiên (NLG)"
    },
    "correct": "B",
    "explanation": "Khai phá dữ liệu (Data Mining) rất phù hợp cho dữ liệu có cấu trúc từ hệ thống ERP/Sổ cái chung để tìm kiếm các mẫu và ngoại lai."
  },
  {
    "id": 76,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ AI với một ứng dụng thực tiễn trong kế toán/tài chính:\nCột 1:\n  (1) Học sâu (Deep Learning)\n  (2) Khai phá văn bản (Text mining)\n  (3) RPA (Tự động hóa robot)\nCột 2:\n  (a) Tái tạo lại các tài liệu quét kém chất lượng bằng nhận dạng quang học (như EY đang làm)\n  (b) Tìm kiếm từ ngữ mang tính buộc tội trong hàng ngàn email để phục vụ kiểm toán pháp y\n  (c) Tự động đăng nhập vào phần mềm và đối chiếu sao kê ngân hàng hàng ngày\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-a, 2-b, 3-c",
      "B": "1-c, 2-b, 3-a",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "A",
    "explanation": "DL chuyên xử lý ảnh/nhận dạng. Text mining xử lý văn bản/email. RPA xử lý thao tác tự động trên giao diện."
  },
  {
    "id": 77,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Theo báo cáo, công cụ lập trình nào giúp thao tác trực tiếp với cơ sở dữ liệu rất hữu ích cho các ứng dụng AI?",
    "options": {
      "A": "HTML và CSS",
      "B": "SQL và NoSQL",
      "C": "Photoshop",
      "D": "Excel VBA"
    },
    "correct": "B",
    "explanation": "Tài liệu ghi rõ: Các công cụ khác, chẳng hạn như SQL và NoSQL, sẽ hữu ích cho việc truy xuất, chỉnh sửa và thao tác dữ liệu để sử dụng cho ứng dụng AI."
  },
  {
    "id": 78,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình tích hợp API của Google Prediction vào một hệ thống phần mềm doanh nghiệp:\n  (1) Phần mềm doanh nghiệp thu thập dữ liệu giao dịch\n  (2) Gửi dữ liệu thông qua API (người đưa tin kỹ thuật số) lên đám mây\n  (3) Google Prediction API sử dụng Học máy để phân tích và đưa ra dự đoán\n  (4) API trả kết quả phân tích về lại phần mềm doanh nghiệp để kế toán viên xem\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "B",
    "explanation": "API hoạt động như một cầu nối nhận dữ liệu, gửi tới service xử lý, và trả kết quả về."
  },
  {
    "id": 79,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống liên quan đến việc lập hồ sơ khách hàng (Customer profiling):\n\"Các tổ chức tài chính sử dụng AI để lập hồ sơ khách hàng nhằm mục đích tiếp thị nhắm mục tiêu. Tuy nhiên, các nhà bán lẻ có thể lạm dụng ___(1)___ để xác định những người tiêu dùng yếu thế, từ đó lợi dụng lỗ hổng tài chính của họ bằng các phương thức bán hàng ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) phân tích dự đoán (predictive analytics) ; (2) hung hăng (aggressive)",
      "B": "(1) hung hăng (aggressive) ; (2) phân tích dự đoán (predictive analytics)",
      "C": "(1) bảo vệ môi trường ; (2) bảo vệ môi trường",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "A",
    "explanation": "Việc lạm dụng predictive analytics để đưa ra các đề xuất bán hàng hung hăng là một rủi ro đạo đức lớn."
  },
  {
    "id": 80,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Dễ",
    "question": "Vụ vi phạm dữ liệu của Equifax năm 2017 là một ví dụ điển hình cảnh báo rủi ro gì trong việc áp dụng AI vào tài chính?",
    "options": {
      "A": "AI không thể hoạt động trên điện thoại di động",
      "B": "Nguy cơ về bảo mật và quyền riêng tư dữ liệu (Data Privacy) khi thu thập lượng lớn thông tin cá nhân",
      "C": "Chi phí điện năng quá cao để chạy mô hình AI",
      "D": "Sự thiên vị trong cấp tín dụng"
    },
    "correct": "B",
    "explanation": "Equifax là case study về Data Privacy, nơi hàng triệu dữ liệu bị lộ, nhấn mạnh tầm quan trọng của an ninh mạng."
  },
  {
    "id": 81,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Khó",
    "question": "Ghép các khái niệm/hiện tượng trong AI Đạo đức với ý nghĩa thực tiễn của nó:\nCột 1:\n  (1) Thiên kiến thuật toán (Biases)\n  (2) Tính không rõ ràng về trách nhiệm (Accountability opacity)\n  (3) Bảo vệ người tiêu dùng (Consumer protection)\nCột 2:\n  (a) Rủi ro khi hệ thống AI từ chối khoản vay dựa trên dữ liệu lịch sử mang tính phân biệt đối xử\n  (b) Khó khăn trong việc xác định ai (lập trình viên, ngân hàng hay AI) chịu trách nhiệm khi AI gây ra thiệt hại\n  (c) Ngăn chặn các thủ thuật tiếp thị và bán hàng lợi dụng lỗ hổng tâm lý/tài chính của khách hàng\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-a, 2-b, 3-c",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "B",
    "explanation": "Biases = thiên vị phân biệt đối xử. Opacity = hộp đen/khó quy trách nhiệm. Protection = bảo vệ khách hàng khỏi bị thao túng."
  },
  {
    "id": 82,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Khó",
    "question": "Theo giáo sư Aldhizer (2017), kỹ thuật Trích xuất Khái niệm (Concept Extraction) dùng trong kiểm toán pháp y chủ yếu để làm gì?",
    "options": {
      "A": "Trích xuất số liệu bảng cân đối kế toán từ file Excel",
      "B": "Xác định các từ ngữ hoặc đoạn văn mang tính buộc tội (incriminating words) từ email và mạng xã hội",
      "C": "Khởi tạo hợp đồng thông minh trên Blockchain",
      "D": "Chấm điểm tín dụng cho doanh nghiệp"
    },
    "correct": "B",
    "explanation": "Concept extraction (một phần của text mining) được dùng trong pháp y kế toán để tìm từ ngữ buộc tội từ email, tin nhắn..."
  },
  {
    "id": 83,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Dễ",
    "question": "Điền từ vào chỗ trống liên quan đến học sâu:\n\"Mạng nơ-ron nhân tạo (ANNs) được lấy cảm hứng từ ___(1)___ của con người, phân tích khối lượng dữ liệu lớn để ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) mạng nơ-ron sinh học ; (2) tự học (self-learn)",
      "B": "(1) tự học (self-learn) ; (2) mạng nơ-ron sinh học",
      "C": "(1) chiếc máy tính ; (2) chiếc máy tính",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "A",
    "explanation": "ANN lấy cảm hứng từ cấu trúc não người (nơ-ron sinh học) để cho phép máy tính tự học từ dữ liệu."
  },
  {
    "id": 84,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Khó",
    "question": "Sắp xếp quy trình giải quyết vấn đề bằng AI theo mô hình đề xuất để đảm bảo tính đạo đức:\n  (1) Thiết kế hệ thống AI và thu thập dữ liệu đại diện, tránh thiên vị (bias)\n  (2) Triển khai thuật toán với sự minh bạch (transparency) và khả năng giải thích (explainability)\n  (3) Áp dụng vào thực tế (như chấm điểm tín dụng) với sự giám sát liên tục (constant monitoring)\n  (4) Thực hiện kiểm toán định kỳ (frequent audits) bởi bên thứ ba hoặc cơ quan quản lý\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (4) ➔ (3)",
      "D": "(1) ➔ (2) ➔ (3) ➔ (4)"
    },
    "correct": "D",
    "explanation": "Phát triển AI đạo đức cần: Thu thập dữ liệu sạch -> Thiết kế minh bạch -> Giám sát liên tục -> Kiểm toán định kỳ."
  },
  {
    "id": 85,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Ứng dụng nào sau đây là kết quả của NLG (Tạo ngôn ngữ tự nhiên)?",
    "options": {
      "A": "Siri ghi nhận giọng nói của người dùng thành văn bản",
      "B": "Máy tính đọc một hóa đơn PDF và lấy ra số tiền",
      "C": "Hệ thống tự động chuyển biểu đồ doanh thu thành một đoạn văn bản tóm tắt tình hình tài chính cho sếp đọc",
      "D": "Tìm kiếm các khoản vay rủi ro trong cơ sở dữ liệu SQL"
    },
    "correct": "C",
    "explanation": "NLG có thể chuyển đổi các hình ảnh hóa dữ liệu như biểu đồ thành mô tả bằng lời nói/văn bản mà con người đọc được."
  },
  {
    "id": 86,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Ghép các công cụ / ứng dụng với lĩnh vực tương ứng của chúng:\nCột 1:\n  (1) Python, R\n  (2) Google Prediction, BigML, Anaconda\n  (3) ACL, IDEA\nCột 2:\n  (a) Ngôn ngữ lập trình mã nguồn mở tốt nhất cho khoa học dữ liệu\n  (b) Các dịch vụ nền tảng hoặc API hỗ trợ triển khai Học máy (ML)\n  (c) Phần mềm phân tích dữ liệu kiểm toán chuyên nghiệp truyền thống\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-a, 2-b, 3-c",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "C",
    "explanation": "Python/R là ngôn ngữ lập trình; Google/BigML cung cấp API/Nền tảng ML; ACL/IDEA là phần mềm kiểm toán."
  },
  {
    "id": 87,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Dễ",
    "question": "Theo tài liệu, tại sao các ngân hàng và công ty tài chính cần hợp lực với các cơ quan quản lý trong việc sử dụng AI?",
    "options": {
      "A": "Để tăng lợi nhuận và thao túng thị trường dễ hơn",
      "B": "Để bảo vệ tính toàn vẹn của thị trường, bảo vệ quyền lợi người tiêu dùng và đảm bảo tuân thủ pháp luật",
      "C": "Để độc quyền công nghệ AI",
      "D": "Để ngừng sử dụng AI và quay về làm thủ công"
    },
    "correct": "B",
    "explanation": "Sự hợp lực là để tận dụng AI trong khi vẫn bảo vệ sự toàn vẹn, đạo đức và tuân thủ quy định."
  },
  {
    "id": 88,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống về Xử lý ngôn ngữ tự nhiên (NLP) trong kế toán:\n\"Tiềm năng của NLP trong kế toán rất lớn. Nó được sử dụng để phân tích các văn bản liên quan đến hiệu quả tài chính và sự tuân thủ quy định. Các ứng dụng của NLP bao gồm phân tích ___(1)___, phân loại văn bản, và ___(2)___ văn bản.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) tóm tắt (summarization) ; (2) ngữ nghĩa (semantics)",
      "B": "(1) ngữ nghĩa (semantics) ; (2) tóm tắt (summarization)",
      "C": "(1) chuỗi khối ; (2) chuỗi khối",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "NLP trong kế toán giúp phân tích ngữ nghĩa, phân loại và tóm tắt các tài liệu, hợp đồng, báo cáo."
  },
  {
    "id": 89,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Quy trình ứng dụng Học sâu (Deep Learning) vào hệ thống tự động theo nghiên cứu:\n  (1) Thu thập khối lượng lớn dữ liệu đầu vào (hình ảnh, giọng nói, tài liệu quét)\n  (2) Dữ liệu được đưa qua các lớp của Mạng nơ-ron nhân tạo (ANNs)\n  (3) Thuật toán tự khám phá ra các mô hình (patterns) mà không cần con người lập trình quy tắc tĩnh\n  (4) Đưa ra dự đoán hoặc nhận dạng chính xác (vd: phát hiện hóa đơn giả)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "DL dựa vào việc đẩy dữ liệu qua mạng ANN để máy tự học cấu trúc (tự khám phá pattern) và đưa ra kết quả."
  },
  {
    "id": 90,
    "session": "Buổi 3: Python for Finance & Data Science",
    "difficulty": "Trung bình",
    "question": "Hệ thống AI tài chính yêu cầu quyền truy cập vào lượng lớn dữ liệu (hồ sơ giao dịch, điểm tín dụng). Điều này đặt ra yêu cầu CẤP BÁCH nào nhất về mặt đạo đức/pháp luật?",
    "options": {
      "A": "Yêu cầu phải sử dụng bộ xử lý TPU",
      "B": "Yêu cầu thiết lập luật bảo vệ dữ liệu mạnh mẽ để bảo mật quyền riêng tư (Data Privacy)",
      "C": "Yêu cầu phải in toàn bộ dữ liệu ra giấy",
      "D": "Yêu cầu AI phải tự động giao dịch thay con người"
    },
    "correct": "B",
    "explanation": "Quyền truy cập dữ liệu lớn đi liền với rủi ro bảo mật, đòi hỏi luật bảo vệ dữ liệu (privacy laws) nghiêm ngặt."
  },
  {
    "id": 91,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Dễ",
    "question": "Khái niệm STP trong tiếp thị là viết tắt của các từ nào?",
    "options": {
      "A": "Segmentation, Targeting, Positioning",
      "B": "Sales, Technology, Pricing strategies",
      "C": "Systems, Tracking, Performance measures",
      "D": "Standardization, Trading, Profitability"
    },
    "correct": "A",
    "explanation": "STP là viết tắt của Phân khúc (Segmentation), Nhắm mục tiêu (Targeting), Định vị (Positioning)."
  },
  {
    "id": 92,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Trong học không giám sát (unsupervised learning), tại sao chúng ta sử dụng thuật toán phân cụm?",
    "options": {
      "A": "Để tính toán lợi nhuận và doanh thu",
      "B": "Để huấn luyện mô hình dự báo phá sản",
      "C": "Do dữ liệu không có nhãn kết quả (unlabeled)",
      "D": "Do cần một phương pháp hồi quy tuyến tính"
    },
    "correct": "C",
    "explanation": "Phân cụm được sử dụng trong học không giám sát vì dữ liệu không có nhãn (unlabeled data)."
  },
  {
    "id": 93,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Dễ",
    "question": "Ghép các khái niệm phân khúc với định nghĩa tương ứng:\nCột 1:\n  (1) Phân khúc động (Dynamic Segmentation)\n  (2) Vi phân khúc (Microsegments)\n  (3) Tiếp thị đại chúng (Mass marketing)\nCột 2:\n  (a) Liên tục cập nhật phân khúc vì sở thích khách hàng luôn thay đổi\n  (b) Phân khúc siêu nhỏ hướng tới cá nhân hóa (hyperpersonalization)\n  (c) Giả định tất cả khách hàng đều giống nhau và gửi chung một thông điệp\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "Dynamic = cập nhật liên tục. Micro = cá nhân hóa siêu nhỏ. Mass = đại trà."
  },
  {
    "id": 94,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Sắp xếp các bước cơ bản của thuật toán k-Means:\n  (1) Xác định số lượng cụm (k)\n  (2) Khởi tạo ngẫu nhiên các trung tâm cụm (centroids)\n  (3) Gán mỗi điểm dữ liệu cho trung tâm cụm gần nhất\n  (4) Tính toán lại trung tâm và lặp lại cho đến khi hội tụ\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (4) ➔ (3)",
      "D": "(1) ➔ (2) ➔ (3) ➔ (4)"
    },
    "correct": "D",
    "explanation": "Quy trình k-Means: Chọn k -> Khởi tạo -> Gán điểm -> Cập nhật trung tâm (lặp lại)."
  },
  {
    "id": 95,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Điền từ thích hợp so sánh giữa k-Means và k-Medoid:\n\"Thay vì sử dụng giá trị trung bình như k-Means, k-Medoid sử dụng một ___(1)___ làm trung tâm. Điều này giúp thuật toán chống ___(2)___ tốt hơn k-Means.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) nhiễu ngoại lai (outliers) ; (2) điểm dữ liệu thực tế (medoid)",
      "B": "(1) giá trị giả định ; (2) giá trị giả định",
      "C": "(1) điểm dữ liệu thực tế (medoid) ; (2) nhiễu ngoại lai (outliers)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "C",
    "explanation": "k-Medoid lấy một điểm thực tế làm tâm, giúp nó bền vững hơn trước các giá trị ngoại lai (outliers)."
  },
  {
    "id": 96,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Khó",
    "question": "Lệnh `scale(df, center = TRUE, scale = TRUE)` trong R nhằm mục đích gì?",
    "options": {
      "A": "Chuyển dữ liệu thành dạng số nguyên (integer)",
      "B": "Lọc các giá trị trống (NA) ra khỏi dữ liệu",
      "C": "Vẽ biểu đồ các trung tâm cụm ngẫu nhiên",
      "D": "Chuyển đổi các biến về cùng thang đo (điểm Z)"
    },
    "correct": "D",
    "explanation": "Căn giữa và chia tỷ lệ giúp chuyển giá trị về điểm Z, khắc phục sự khác biệt thang đo giữa các biến."
  },
  {
    "id": 97,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Dễ",
    "question": "Đa cộng tuyến (Multicollinearity) xảy ra khi nào trong mô hình dự báo?",
    "options": {
      "A": "Khi tất cả các biến đều độc lập với nhau",
      "B": "Khi có nhiều biến độc lập tương quan mạnh",
      "C": "Khi dữ liệu bị thiếu hụt",
      "D": "Khi không thể xác định được biến phụ thuộc"
    },
    "correct": "B",
    "explanation": "Đa cộng tuyến (Multicollinearity) xảy ra khi có sự tương quan mạnh giữa nhiều biến độc lập."
  },
  {
    "id": 98,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Khó",
    "question": "Ghép nối các tham số trong R với chức năng của chúng:\nCột 1:\n  (1) centers trong kmeans()\n  (2) nstart trong kmeans()\n  (3) repel = TRUE trong fviz_cluster()\nCột 2:\n  (a) Chỉ định số lượng cụm cần phân chia\n  (b) Đặt số lượng điểm khởi tạo ngẫu nhiên ban đầu\n  (c) Ngăn các nhãn của điểm dữ liệu đè lên nhau trên biểu đồ\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-a, 2-b, 3-c",
      "B": "1-c, 2-b, 3-a",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "A",
    "explanation": "centers = k (số cụm); nstart = số lần lặp random ban đầu; repel=TRUE = tránh text overlap."
  },
  {
    "id": 99,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống về mô hình hồi quy:\n\"Để khắc phục Đa cộng tuyến và tự động loại bỏ biến không cần thiết, người ta dùng Hồi quy ___(1)___, tiêu biểu là mô hình ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) LASSO ; (2) có phạt (Penalized)",
      "B": "(1) tuyến tính (Linear) ; (2) tuyến tính (Linear)",
      "C": "(1) có phạt (Penalized) ; (2) LASSO",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "C",
    "explanation": "Hồi quy có phạt (Penalized regression), đặc biệt là LASSO, giúp lựa chọn đặc trưng và giải quyết đa cộng tuyến."
  },
  {
    "id": 100,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Khó",
    "question": "Sắp xếp các bước đánh giá sức khỏe tài chính bằng LASSO:\n  (1) Thu thập dữ liệu các chỉ số tài chính (ratios) của các công ty (cả phá sản và không phá sản)\n  (2) Kiểm tra sự tương quan (Biểu đồ tương quan) và VIF\n  (3) Chạy mô hình LASSO để tự động loại bỏ các biến có đa cộng tuyến (thu gọn hệ số về 0)\n  (4) Đánh giá khả năng dự đoán của mô hình bằng đường cong AUC ROC\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "B",
    "explanation": "Quy trình: Chuẩn bị dữ liệu -> Kiểm tra tương quan -> Huấn luyện LASSO (lọc biến) -> Đánh giá (AUC ROC)."
  },
  {
    "id": 101,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Đường cong AUC ROC biểu diễn mối quan hệ giữa hai yếu tố nào?",
    "options": {
      "A": "Dương tính giả (X) và Dương tính thật (Y)",
      "B": "Khoảng cách Euclide (X) và Tâm cụm (Y)",
      "C": "Chi phí (X) và Doanh thu (Y)",
      "D": "Thời gian mua sắm (X) và Số tiền chi tiêu (Y)"
    },
    "correct": "A",
    "explanation": "AUC ROC biểu diễn False Positives (trục x) và True Positives (trục y)."
  },
  {
    "id": 102,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Dễ",
    "question": "Thuật ngữ 'Vốn cổ phần tư nhân' (Private equity) trong tài liệu thường đầu tư vào dạng doanh nghiệp nào?",
    "options": {
      "A": "Chỉ đầu tư vào tập đoàn công nghệ",
      "B": "Doanh nghiệp có tiềm năng lớn nhưng đang khó khăn tài chính",
      "C": "Chỉ đầu tư vào ngân hàng trung ương",
      "D": "Doanh nghiệp hoàn toàn không có khoản nợ nào"
    },
    "correct": "B",
    "explanation": "Công ty cổ phần tư nhân đầu tư vào doanh nghiệp có tiềm năng chưa hiện thực hóa nhưng đang gặp khó khăn (nợ cao)."
  },
  {
    "id": 103,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Ghép các công thức chỉ số tài chính (Financial Ratios) với tên của chúng:\nCột 1:\n  (1) Current Ratio (Tỷ lệ thanh toán hiện hành)\n  (2) Debt-Equity Ratio (Tỷ lệ nợ trên vốn CSH)\n  (3) Operating Ratio (Tỷ lệ hoạt động)\nCột 2:\n  (a) Tài sản lưu động / Nợ ngắn hạn\n  (b) Giá trị sổ sách của vốn chủ sở hữu / Tổng nợ phải trả\n  (c) Tổng chi phí / Tổng doanh thu\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-a, 2-b, 3-c",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "B",
    "explanation": "Dựa vào công thức trong mục 10.5.1 và bộ dữ liệu."
  },
  {
    "id": 104,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Khó",
    "question": "Điền từ liên quan đến cách hoạt động của glmnet (mô hình LASSO):\n\"Mô hình LASSO đã thu hẹp các tham số beta của một số biến về ___(1)___, do đó giúp ___(2)___ từ 16 biến ban đầu xuống số lượng ít hơn.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) lựa chọn đặc trưng (feature selection) ; (2) 0 (không)",
      "B": "(1) gia tăng (increase) ; (2) gia tăng (increase)",
      "C": "Phương án điền từ khác 3",
      "D": "(1) 0 (không) ; (2) lựa chọn đặc trưng (feature selection)"
    },
    "correct": "D",
    "explanation": "LASSO giải quyết đa cộng tuyến bằng cách đẩy hệ số của các biến kém quan trọng về 0, giúp chọn lọc đặc trưng."
  },
  {
    "id": 105,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Thứ tự xử lý dữ liệu trước khi phân cụm (Cluster Analysis):\n  (1) Đọc dữ liệu thô (vd: số tiền, thời gian mua sắm)\n  (2) Trừ giá trị trung bình (center = TRUE)\n  (3) Chia cho độ lệch chuẩn (scale = TRUE)\n  (4) Sử dụng dữ liệu điểm Z (Z-scores) để chạy k-Means\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "C",
    "explanation": "Quy trình: Đọc dữ liệu -> Căn giữa (trừ mean) -> Chia tỷ lệ (chia std dev) -> Chạy phân cụm."
  },
  {
    "id": 106,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Điều kiện cần thiết của dữ liệu khi truyền vào hàm glmnet() để chạy LASSO trong R là gì?",
    "options": {
      "A": "Dữ liệu phải có định dạng văn bản (text)",
      "B": "Dữ liệu phải ở dạng ma trận (matrix)",
      "C": "Dữ liệu phải là danh sách liên kết",
      "D": "Dữ liệu không được chứa số thập phân"
    },
    "correct": "B",
    "explanation": "Tài liệu ghi rõ: Vì đối với glmnet, dữ liệu phải ở dạng ma trận, chúng ta chuyển đổi nó thành một ma trận..."
  },
  {
    "id": 107,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Dễ",
    "question": "Ghép các bộ phận/tổ chức với vai trò sử dụng Dự báo sức khỏe tài chính:\nCột 1:\n  (1) Người cho vay (Ngân hàng)\n  (2) Ban quản lý (Doanh nghiệp)\n  (3) Nhà đầu tư (Cổ phần tư nhân)\nCột 2:\n  (a) Quyết định có nên cấp tín dụng hay không\n  (b) Lập kế hoạch chiến lược và phân bổ nguồn lực nội bộ\n  (c) Mua lại các doanh nghiệp nợ cao nhưng có tiềm năng\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-a, 2-b, 3-c",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "B",
    "explanation": "Ngân hàng -> cấp tín dụng. Ban quản lý -> chiến lược. Nhà đầu tư -> mua lại công ty."
  },
  {
    "id": 108,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Khó",
    "question": "Hệ quả của Đa cộng tuyến đối với một mô hình dự báo là gì?",
    "options": {
      "A": "Mô hình sẽ không thể tính toán được",
      "B": "Nó làm tăng tốc độ xử lý dữ liệu",
      "C": "Dẫn đến các ước tính không đáng tin cậy cho từng hệ số dự báo",
      "D": "Làm cho biểu đồ ROC AUC luôn đạt 1.0"
    },
    "correct": "C",
    "explanation": "Đa cộng tuyến không làm hỏng toàn bộ mô hình nhưng làm hệ số của từng biến trở nên không chính xác, thiếu tin cậy."
  },
  {
    "id": 109,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Dễ",
    "question": "Điền từ liên quan đến sự tương đồng trong phân cụm:\n\"Nếu hai khách hàng ở gần nhau trong ___(1)___, họ sẽ có nhiều điểm tương đồng và do đó nên được nhóm vào cùng một ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) không gian đặc trưng (feature space) ; (2) cụm (cluster)",
      "B": "(1) cụm (cluster) ; (2) không gian đặc trưng (feature space)",
      "C": "(1) vũ trụ song song ; (2) vũ trụ song song",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "A",
    "explanation": "Khoảng cách trong feature space càng nhỏ, sự tương đồng càng cao, do đó được xếp chung vào 1 cluster."
  },
  {
    "id": 110,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Nhãn kết quả (label) dự đoán trong mô hình sức khỏe tài chính của Ngân hàng Altra là gì?",
    "options": {
      "A": "Doanh nghiệp có thuộc cụm 1 hay cụm 2 không",
      "B": "Doanh nghiệp có lợi nhuận cao nhất thị trường",
      "C": "Khách hàng có ở lại lâu không",
      "D": "Doanh nghiệp có phá sản hay không"
    },
    "correct": "D",
    "explanation": "Nhãn để đánh giá là liệu một doanh nghiệp có bị phá sản hay không (sẽ phá sản = 0, không phá sản = 1)."
  },
  {
    "id": 111,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Dễ",
    "question": "Thứ tự các khái niệm từ mức độ tổng quát đến cá nhân hóa trong Marketing:\n  (1) Tiếp thị đại chúng (Mass marketing - coi mọi người như 1)\n  (2) Phân khúc thị trường (Segmentation - chia nhóm lớn)\n  (3) Vi phân khúc (Microsegments - nhóm rất nhỏ)\n  (4) Siêu cá nhân hóa (Hyperpersonalization - duy nhất từng người)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Đại chúng -> Phân khúc -> Vi phân khúc -> Cá nhân hóa."
  },
  {
    "id": 112,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Khó",
    "question": "Ghép chức năng của các hàm trong R khi vẽ và đo lường mô hình:\nCột 1:\n  (1) fviz_cluster()\n  (2) predict(..., type='response')\n  (3) performance(pred, 'auc')\nCột 2:\n  (a) Trực quan hóa kết quả phân cụm (k-Means)\n  (b) Đưa ra dự đoán phá sản cho dữ liệu mới\n  (c) Tính toán diện tích dưới đường cong ROC để đánh giá mô hình\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-a, 2-b, 3-c",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "C",
    "explanation": "fviz_cluster vẽ cụm. predict lấy xác suất/phản hồi. performance tính AUC."
  },
  {
    "id": 113,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Trong đánh giá mô hình bằng ROC, giá trị AUC (Area Under Curve) như thế nào thì được coi là tốt?",
    "options": {
      "A": "Bằng 0",
      "B": "Càng thấp càng tốt",
      "C": "Chính xác là 0.5",
      "D": "Các giá trị cao hơn cho thấy dự đoán tốt hơn"
    },
    "correct": "D",
    "explanation": "Các giá trị AUC cao hơn cho thấy khả năng phân loại, dự đoán của mô hình tốt hơn."
  },
  {
    "id": 114,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Điền từ liên quan đến VIF (Variance Inflation Factor):\n\"Chúng ta có thể kiểm tra ___(1)___ (multicollinearity) bằng cách sử dụng ___(2)___ cho từng biến dự báo.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) VIF ; (2) đa cộng tuyến",
      "B": "(1) đa cộng tuyến ; (2) VIF",
      "C": "(1) cây quyết định ; (2) cây quyết định",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "VIF được dùng để đánh giá mức độ đa cộng tuyến của các biến dự báo."
  },
  {
    "id": 115,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình phân khúc khách hàng theo cơ sở dữ liệu (Data-Driven Segmentation):\n  (1) Giới thiệu sản phẩm qua các mẫu nhỏ\n  (2) Theo dõi hành vi mua hàng thực tế của khách hàng (dữ liệu bán hàng)\n  (3) Phân tích cụm (Clustering) trên dữ liệu thu thập được\n  (4) Tinh chỉnh lại sản phẩm và chiến lược nhắm mục tiêu (Vòng phản hồi)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Dựa trên data-driven: tung mẫu -> theo dõi hành vi -> phân tích -> vòng lặp tinh chỉnh."
  },
  {
    "id": 116,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Dễ",
    "question": "Ví dụ về Vi phân khúc (Microsegmenting) mà Amazon áp dụng là gì?",
    "options": {
      "A": "Gửi coupon giảm giá rau củ cho mọi người ở Phoenix",
      "B": "Không đưa ra bất kỳ gợi ý nào",
      "C": "Đề xuất sản phẩm rất cụ thể dựa trên hành vi mua hàng trong quá khứ của cá nhân",
      "D": "Chỉ đề xuất sản phẩm dựa vào độ tuổi"
    },
    "correct": "C",
    "explanation": "Amazon tạo microsegments để đề xuất các sản phẩm rất cụ thể cho từng khách hàng."
  },
  {
    "id": 117,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Ghép ý nghĩa của các thông số/câu lệnh khi thực hành R (Phân khúc bằng k-Means):\nCột 1:\n  (1) set.seed(12345)\n  (2) center = TRUE\n  (3) scale = TRUE\nCột 2:\n  (a) Thiết lập giá trị gieo mầm để có thể tái tạo (reproduce) lại kết quả y hệt\n  (b) Trừ giá trị trung bình của biến khỏi các giá trị\n  (c) Chia dữ liệu cho độ lệch chuẩn để đồng bộ thang đo\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "seed = cố định random; center = trừ mean; scale = chia std dev."
  },
  {
    "id": 118,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Khó",
    "question": "Điền từ vào chỗ trống liên quan đến báo cáo tài chính:\n\"Bộ phận tài chính cung cấp cái nhìn hồi tố thông qua bảng cân đối kế toán, báo cáo ___(1)___, và báo cáo lưu chuyển tiền tệ. Họ cũng cung cấp cái nhìn hướng tới tương lai qua các dự báo và lập kế hoạch ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) kịch bản (scenario planning) ; (2) kết quả hoạt động kinh doanh",
      "B": "(1) kết quả hoạt động kinh doanh ; (2) kịch bản (scenario planning)",
      "C": "(1) viễn cảnh ; (2) viễn cảnh",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "Báo cáo kết quả hoạt động kinh doanh là 1 trong 3 báo cáo chính. Lập kế hoạch kịch bản là phương pháp dự báo tương lai."
  },
  {
    "id": 119,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Dễ",
    "question": "Sắp xếp theo thứ tự ưu tiên của việc phân khúc thị trường truyền thống đến tự động hóa AI:\n  (1) Nhắm mục tiêu theo nhân khẩu học chung (Demographics cơ bản)\n  (2) Sử dụng yếu tố tâm lý học và lối sống (Psychographics)\n  (3) Áp dụng học máy (k-Means) để phân cụm dựa trên dữ liệu mua sắm\n  (4) Siêu cá nhân hóa tự động bằng AI (Hyperpersonalization)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Sự phát triển của segmentation từ tĩnh (nhân khẩu, tâm lý) đến tự động bằng Machine Learning và AI siêu cá nhân hóa."
  },
  {
    "id": 120,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "difficulty": "Trung bình",
    "question": "Nhược điểm của k-Means dẫn đến việc ra đời k-Medoid là gì?",
    "options": {
      "A": "Dễ bị ảnh hưởng mạnh bởi nhiễu (outliers) do dùng giá trị trung bình",
      "B": "Không thể chạy trên dữ liệu lớn",
      "C": "Chỉ hỗ trợ phân khúc theo độ tuổi",
      "D": "Bắt buộc dữ liệu phải có nhãn kết quả (labeled)"
    },
    "correct": "A",
    "explanation": "k-Means dùng trung bình nên dễ bị nhiễu kéo lệch. k-Medoid dùng điểm thực tế làm tâm nên chống nhiễu tốt hơn."
  },
  {
    "id": 121,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Dễ",
    "question": "Thuật ngữ 'Ra quyết định dưới sự không chắc chắn' (Decision-Making Under Uncertainty) có nghĩa là gì?",
    "options": {
      "A": "Quyết định được đưa ra khi thiếu thông tin hoặc thông tin chỉ có sẵn ở dạng xác suất",
      "B": "Quyết định đưa ra khi bạn đã biết chắc chắn 100% về tương lai",
      "C": "Quyết định được thực hiện bởi máy tính một cách tự động",
      "D": "Việc từ chối đưa ra bất kỳ hành động nào do thiếu thông tin"
    },
    "correct": "A",
    "explanation": "Ra quyết định dưới sự không chắc chắn xảy ra khi bạn thiếu thông tin đầy đủ và chỉ có thể dựa vào xác suất thành công."
  },
  {
    "id": 122,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Hiệu ứng 'Cái roi da' (Bullwhip effect) trong chuỗi cung ứng mô tả hiện tượng nào?",
    "options": {
      "A": "Việc giảm giá sản phẩm để chống lại đối thủ cạnh tranh mới",
      "B": "Lỗi phần mềm gây chậm trễ cho toàn bộ hệ thống logistic",
      "C": "Sự thay đổi nhỏ về nhu cầu bị đánh giá quá cao, dẫn đến dư thừa cung",
      "D": "Sự khan hiếm hàng hóa do thiên tai hoặc dịch bệnh"
    },
    "correct": "C",
    "explanation": "Hiệu ứng cái roi da xảy ra khi những tín hiệu nhu cầu nhỏ lẻ bị phóng đại dọc theo chuỗi cung ứng, dẫn đến tích trữ quá mức hoặc dư thừa nguồn cung."
  },
  {
    "id": 123,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Dễ",
    "question": "Ghép các khái niệm của Cây quyết định (Decision Tree) với định nghĩa của chúng:\nCột 1:\n  (1) Nút gốc (Root node)\n  (2) Độ vẩn đục Gini (Gini impurity)\n  (3) Nút lá (Leaf node)\nCột 2:\n  (a) Điểm bắt đầu của cây, biến phân loại tốt nhất được chọn đầu tiên\n  (b) Chỉ số để đo lường mức độ hỗn tạp của dữ liệu, càng thấp càng tốt\n  (c) Kết quả dự đoán cuối cùng của nhánh (vd: Có/Không bị chậm giao)\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "Root node là nút cao nhất. Gini đo mức độ phân loại tốt hay xấu. Leaf node là kết quả cuối cùng."
  },
  {
    "id": 124,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Sắp xếp các bước cơ bản trong quá trình Phát triển Sản phẩm Mới:\n  (1) Hình thành và sàng lọc ý tưởng (Idea Generation & Screening)\n  (2) Phát triển khái niệm và phân tích kinh doanh (Concept & Business Analysis)\n  (3) Thiết kế và phát triển nguyên mẫu sản phẩm\n  (4) Thử nghiệm thị trường (Test Marketing) và Thương mại hóa (Commercialization)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (4) ➔ (3)",
      "D": "(1) ➔ (2) ➔ (3) ➔ (4)"
    },
    "correct": "D",
    "explanation": "Quy trình tiêu chuẩn: Lên ý tưởng -> Phân tích tính khả thi kinh doanh -> Chế tạo sản phẩm -> Thử nghiệm và tung ra thị trường."
  },
  {
    "id": 125,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Điền từ liên quan đến sự mất cân bằng dữ liệu (Imbalance) và cách xử lý:\n\"Khi số lượng sản phẩm giao đúng hạn quá lớn so với sản phẩm bị chậm giao, mô hình có thể bị thiên vị. Kỹ thuật ___(1)___ (lấy mẫu giảm) giúp cân bằng dữ liệu, qua đó làm tăng ___(2)___ (khả năng nhận diện sản phẩm bị chậm giao).\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) độ nhạy (sensitivity) ; (2) downsampling",
      "B": "(1) tính đồng nhất ; (2) tính đồng nhất",
      "C": "(1) downsampling ; (2) độ nhạy (sensitivity)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "C",
    "explanation": "Downsampling giảm lượng mẫu của lớp đa số, giúp mô hình tập trung học cách nhận diện lớp thiểu số (tăng độ nhạy)."
  },
  {
    "id": 126,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Khó",
    "question": "Đặc điểm chính của thuật toán Rừng ngẫu nhiên (Random Forest) là gì?",
    "options": {
      "A": "Kết hợp nhiều cây quyết định bằng kỹ thuật Bagging (bootstrap aggregation) để giảm phương sai",
      "B": "Chỉ sử dụng một cây quyết định duy nhất để dự đoán",
      "C": "Là thuật toán dựa trên hồi quy tuyến tính cổ điển",
      "D": "Chỉ phù hợp với dữ liệu không có nhãn kết quả"
    },
    "correct": "A",
    "explanation": "Random Forest tạo ra nhiều cây (forest) bằng cách lấy mẫu có hoàn lại (Bagging) và kết hợp chúng để ra kết quả ổn định hơn."
  },
  {
    "id": 127,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Dễ",
    "question": "Trong ví dụ ở chương 14, Nintendo Switch thành công nhờ yếu tố nào?",
    "options": {
      "A": "Chỉ có thể chơi khi kết nối với tivi (console) ở nhà",
      "B": "Thiết kế linh hoạt cho phép chơi cả cầm tay và qua bảng điều khiển",
      "C": "Mức giá cao hơn đáng kể so với các đối thủ",
      "D": "Phát hành miễn phí cho tất cả người dùng"
    },
    "correct": "B",
    "explanation": "Thiết kế của nó cho phép chơi trò chơi cầm tay và bảng điều khiển (console) thu hút được lượng lớn người dùng."
  },
  {
    "id": 128,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Khó",
    "question": "Ghép các thông số của Ma trận nhầm lẫn (Confusion Matrix) với cách tính:\nCột 1:\n  (1) Độ nhạy (Sensitivity)\n  (2) Độ đặc hiệu (Specificity)\n  (3) Dương tính thật (True Positive)\nCột 2:\n  (a) Tỷ lệ mô hình nhận diện chính xác lớp thiểu số (vd: bị chậm giao)\n  (b) Tỷ lệ mô hình nhận diện chính xác lớp đa số (vd: không bị chậm giao)\n  (c) Số lượng các trường hợp thực tế CÓ và mô hình dự đoán CÓ\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-a, 2-b, 3-c",
      "B": "1-c, 2-b, 3-a",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "A",
    "explanation": "Sensitivity (True Positive Rate) = đoán trúng lớp thiểu số. Specificity (True Negative Rate) = đoán trúng lớp đa số."
  },
  {
    "id": 129,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Điền từ về các bài kiểm định trong Thử nghiệm A/B (A/B Testing):\n\"Để so sánh giá trị trung bình của ba mức độ khó (Low, Medium, High) trong thiết kế nguyên mẫu game, chúng ta sử dụng kiểm định ___(1)___. Nếu phương sai không bằng nhau, ta dùng ___(2)___ để thay thế.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) Welch's ANOVA ; (2) F (ANOVA)",
      "B": "(1) chi bình phương (chi-square) ; (2) chi bình phương (chi-square)",
      "C": "(1) F (ANOVA) ; (2) Welch's ANOVA",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "C",
    "explanation": "Kiểm định F (ANOVA) dùng cho >=3 nhóm. Welch's ANOVA dùng khi giả định về phương sai bằng nhau bị vi phạm."
  },
  {
    "id": 130,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Khó",
    "question": "Trình tự tính toán Chỉ số Gini (Gini Impurity) cho nút gốc (Root node) trên một biến dự báo:\n  (1) Tính tỷ lệ kết quả (Có/Không) cho từng nhóm của biến dự báo (vd: Dự báo cao/Thấp)\n  (2) Tính độ vẩn đục (Impurity) của từng nhóm: 1 - P(Có)^2 - P(Không)^2\n  (3) Tính trung bình có trọng số (weighted average) của các chỉ số Impurity này\n  (4) So sánh kết quả với các biến dự báo khác, biến có Gini thấp nhất sẽ làm nút gốc\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "B",
    "explanation": "Tỷ lệ từng nhóm -> Impurity từng nhóm -> Trọng số tổng thể -> Chọn biến có Gini bé nhất."
  },
  {
    "id": 131,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Sự tự chọn (Self-selection) trong thử nghiệm A/B dẫn đến vấn đề gì?",
    "options": {
      "A": "Nó làm tăng tính ngẫu nhiên của thử nghiệm",
      "B": "Nó phá vỡ tính ngẫu nhiên hóa (randomization)",
      "C": "Nó giúp hệ thống ghi nhận dữ liệu nhanh hơn",
      "D": "Nó loại bỏ nhu cầu phải có biến kết quả"
    },
    "correct": "B",
    "explanation": "Tự chọn xảy ra khi người tham gia được tự chọn nhóm, phá vỡ tính ngẫu nhiên và làm lệch kết quả thử nghiệm."
  },
  {
    "id": 132,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Dễ",
    "question": "Chỉ số Gini impurity càng thấp thì có ý nghĩa gì trong cây quyết định?",
    "options": {
      "A": "Nút đó có khả năng phân loại dữ liệu càng tốt",
      "B": "Dữ liệu tại nút đó càng hỗn tạp và lẫn lộn",
      "C": "Chỉ số này không phản ánh chất lượng phân loại",
      "D": "Mô hình đã bị tính sai và cần phải chạy lại"
    },
    "correct": "A",
    "explanation": "Gini impurity thấp nghĩa là dữ liệu ít bị lẫn lộn, do đó có khả năng phân loại, chia rẽ nhóm càng tốt."
  },
  {
    "id": 133,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Ghép các loại bài kiểm định trong phân tích A/B với mục đích sử dụng:\nCột 1:\n  (1) Levene's test\n  (2) Shapiro-Wilk test\n  (3) Games-Howell post hoc test\nCột 2:\n  (a) Kiểm tra tính đồng nhất của phương sai (Equal variance)\n  (b) Kiểm tra tính phân phối chuẩn (Normality)\n  (c) Xác định chính xác cặp nhóm nào khác biệt nhau sau khi ANOVA có ý nghĩa\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-a, 2-b, 3-c",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "B",
    "explanation": "Levene = Phương sai; Shapiro = Chuẩn hóa; Games-Howell = Bài test hậu hoc khi phương sai khác nhau."
  },
  {
    "id": 134,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Khó",
    "question": "Điền từ liên quan đến sự kết hợp (Ensemble) trong Random Forest:\n\"Quá trình lấy mẫu có hoàn lại từ tập dữ liệu gốc để xây dựng nhiều cây quyết định khác nhau được gọi là ___(1)___. Random Forest sử dụng kỹ thuật này để giảm ___(2)___ của mô hình so với việc chỉ dùng 1 cây đơn lẻ.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) hiện tượng quá khớp (overfitting) và phương sai ; (2) Bagging (bootstrap aggregation)",
      "B": "(1) chính xác (accuracy) ; (2) chính xác (accuracy)",
      "C": "Phương án điền từ khác 3",
      "D": "(1) Bagging (bootstrap aggregation) ; (2) hiện tượng quá khớp (overfitting) và phương sai"
    },
    "correct": "D",
    "explanation": "Bagging giúp tạo ra rừng các cây đa dạng, giảm phương sai và nguy cơ overfitting so với cây quyết định đơn lẻ."
  },
  {
    "id": 135,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Sắp xếp các bước thực hiện kiểm định thử nghiệm A/B với >=3 nhóm:\n  (1) Thu thập dữ liệu từ các nguyên mẫu đã được phân bổ ngẫu nhiên\n  (2) Kiểm tra giả định về phân phối chuẩn và phương sai đồng nhất\n  (3) Chạy kiểm định Welch's ANOVA (nếu phương sai không đồng nhất)\n  (4) Chạy kiểm định hậu hoc (Post-hoc test) để xem cặp nguyên mẫu nào thực sự khác biệt\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "C",
    "explanation": "Data -> Check assumptions -> Chạy ANOVA -> Post-hoc test để xác định rõ sự khác biệt."
  },
  {
    "id": 136,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Đặc điểm nào KHÔNG ĐÚNG khi nói về kỹ thuật Bagging (bootstrap aggregation)?",
    "options": {
      "A": "Nó bao gồm việc lấy mẫu mà không có sự hoàn lại (without replacement)",
      "B": "Nó kết hợp kết quả từ nhiều mô hình nhỏ lẻ để ra quyết định chung",
      "C": "Nó giúp xây dựng các cây quyết định đa dạng",
      "D": "Random forest là một ứng dụng phổ biến của Bagging"
    },
    "correct": "A",
    "explanation": "Bagging (Bootstrap aggregation) YÊU CẦU lấy mẫu CÓ hoàn lại (with replacement), do đó câu A là sai."
  },
  {
    "id": 137,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Dễ",
    "question": "Ghép các quyết định kinh doanh với các sự không chắc chắn (uncertainty) tương ứng (Theo ví dụ Hãng hàng không):\nCột 1:\n  (1) Quyết định Hành động (Giảm giá)\n  (2) Quyết định Không hành động (Giữ nguyên giá)\nCột 2:\n  (a) Có thể làm xói mòn lợi nhuận và gây ra cuộc chiến giá cả\n  (b) Có thể bị cổ đông coi là không sẵn lòng thích ứng với thị trường\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-b, 2-a",
      "B": "1-a, 2-b",
      "C": "Phương án ghép cặp khác 2",
      "D": "Phương án ghép cặp khác 3"
    },
    "correct": "B",
    "explanation": "Hành động giảm giá -> rủi ro chiến tranh giá cả. Không làm gì -> rủi ro mất khách và bị coi là bảo thủ."
  },
  {
    "id": 138,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Khó",
    "question": "Nếu trong một mô hình dự báo, tỷ lệ Accuracy và giá trị AUC đều rất cao, nhưng Sensitivity (Độ nhạy) lại rất thấp, điều này phản ánh vấn đề gì?",
    "options": {
      "A": "Mô hình đã bị phân bổ ngẫu nhiên sai cách",
      "B": "Mô hình hoàn toàn mất khả năng chạy dự báo",
      "C": "Mô hình gặp vấn đề do dữ liệu bị mất cân bằng (class imbalance) nghiêm trọng",
      "D": "Mô hình dự báo quá tốt đến mức không cần điều chỉnh thêm"
    },
    "correct": "C",
    "explanation": "Khi dữ liệu cực kỳ lệch (imbalance), mô hình có thể chỉ chọn dự báo lớp đa số (đạt Accuracy cao) nhưng hoàn toàn thất bại trong việc nhận diện lớp thiểu số (Sensitivity thấp)."
  },
  {
    "id": 139,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Dễ",
    "question": "Điền từ về Thử nghiệm Nguyên mẫu Trò chơi:\n\"Để tránh việc người chơi tự chọn nhóm theo sở thích màu sắc hay độ khó, GameV phải áp dụng ___(1)___ để phân bổ người chơi. Nhờ đó, bất kỳ sự khác biệt nào về thời gian chơi cũng có thể tự tin gán cho ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) sự ngẫu nhiên hóa (randomization) ; (2) mức độ khó (nguyên mẫu)",
      "B": "(1) mức độ khó (nguyên mẫu) ; (2) sự ngẫu nhiên hóa (randomization)",
      "C": "(1) thiên vị (bias) ; (2) thiên vị (bias)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "A",
    "explanation": "Phân bổ ngẫu nhiên giúp cô lập nguyên nhân, khẳng định sự khác biệt là do mức độ khó chứ không do yếu tố nhiễu ngoài."
  },
  {
    "id": 140,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Trong thử nghiệm A/B, Giả thuyết Không (Null Hypothesis) biểu thị điều gì?",
    "options": {
      "A": "Sự can thiệp (intervention) đã gây ra sự khác biệt",
      "B": "Có sự khác biệt đáng kể giữa các nhóm với nhau",
      "C": "Không có sự khác biệt đáng kể giữa các nhóm, kết quả chỉ là do ngẫu nhiên",
      "D": "Thiết kế của nguyên mẫu A ưu việt hơn hẳn nguyên mẫu B"
    },
    "correct": "C",
    "explanation": "Giả thuyết Không (Null Hypothesis) luôn giả định rằng không có sự khác biệt thực sự, và mọi biến động đều do sai số ngẫu nhiên."
  },
  {
    "id": 141,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Dễ",
    "question": "Thứ tự lý tưởng khi xử lý tình trạng mất cân bằng dữ liệu trong Random Forest:\n  (1) Phân chia dữ liệu thành tập huấn luyện (Train) và tập kiểm tra (Test)\n  (2) Thực hiện giảm mẫu (downsampling) trên tập huấn luyện\n  (3) Huấn luyện mô hình Random Forest trên dữ liệu đã cân bằng\n  (4) Dự đoán trên tập kiểm tra và tính toán Ma trận nhầm lẫn (Confusion Matrix)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Tách data -> Cân bằng tập train -> Huấn luyện -> Dự đoán và Đánh giá."
  },
  {
    "id": 142,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Khó",
    "question": "Ghép số lượng nhóm cần thiết (Groups) với thiết kế thử nghiệm A/B tương ứng:\nCột 1:\n  (1) 1 yếu tố có 2 cấp độ (levels)\n  (2) 1 yếu tố có 3 cấp độ (levels)\n  (3) 3 yếu tố, mỗi yếu tố có 2 cấp độ (levels)\nCột 2:\n  (a) Cần 2 nhóm (ví dụ: Nút Đỏ vs Nút Xanh)\n  (b) Cần 3 nhóm (ví dụ: Độ khó Low, Med, High)\n  (c) Cần 8 nhóm (2 * 2 * 2 = 8)\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-a, 2-b, 3-c",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "C",
    "explanation": "Số lượng nhóm phụ thuộc vào tổ hợp của số lượng yếu tố và số cấp độ."
  },
  {
    "id": 143,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Mục đích chính của một thử nghiệm A/B (A/B testing) là gì?",
    "options": {
      "A": "Để xác định hiệu quả của một sự can thiệp (intervention) thông qua quan hệ nhân quả",
      "B": "Để tăng mức giá bán của tất cả sản phẩm hiện có",
      "C": "Để giảm thiểu thời gian vận chuyển của chuỗi cung ứng",
      "D": "Để phát hiện mối tương quan giữa các biến mà không cần kiểm soát"
    },
    "correct": "A",
    "explanation": "A/B testing là một thử nghiệm nhân quả (causal testing) nhằm so sánh hiệu quả thực sự của một sự can thiệp so với đối chứng."
  },
  {
    "id": 144,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Điền từ về các kết quả dự báo trong bảng nhầm lẫn:\n\"Nếu độ đặc hiệu (specificity) của mô hình thấp, chúng ta sẽ kết thúc bằng việc đặt hàng ___(1)___ những sản phẩm ít có khả năng bị chậm giao, tức là rơi vào trường hợp ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) dương tính giả (False Positive) ; (2) quá mức (overordering)",
      "B": "(1) quá mức (overordering) ; (2) dương tính giả (False Positive)",
      "C": "(1) âm tính thật (True Negative) ; (2) âm tính thật (True Negative)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "Specificity thấp nghĩa là đoán nhầm hàng Không chậm thành Có chậm (False Positive), dẫn tới tích trữ quá mức."
  },
  {
    "id": 145,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Sắp xếp theo logic của Quá trình tinh chỉnh Siêu tham số (Hyperparameter Tuning):\n  (1) Thiết lập danh sách các siêu tham số cần thử nghiệm (vd: mtry, min_n)\n  (2) Sử dụng kiểm chứng chéo k-fold (k-fold Cross Validation) để chạy thử\n  (3) Đánh giá mô hình dựa trên số đo AUC ROC cho từng tổ hợp\n  (4) Chọn tổ hợp siêu tham số tốt nhất (vd: select_best) để hoàn thiện mô hình\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Grid search -> k-fold CV -> Đánh giá các Fold -> Chọn Best hyperparameter."
  },
  {
    "id": 146,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Dễ",
    "question": "Trong bài kiểm định F, việc biến kết quả (outcome variable) có bản chất là liên tục (continuous) mang ý nghĩa gì?",
    "options": {
      "A": "Ví dụ như thời gian chơi game, có thể đo lường bằng các giá trị số chi tiết thay vì Có/Không",
      "B": "Biến kết quả chỉ có hai giá trị (Có hoặc Không, 1 hoặc 0)",
      "C": "Biến kết quả không thể được sử dụng trong Thử nghiệm A/B",
      "D": "Biến kết quả chỉ mang giá trị phân loại như 'Màu xanh', 'Màu đỏ'"
    },
    "correct": "A",
    "explanation": "Biến liên tục có thể mang giá trị số mở rộng (ví dụ thời gian: 1.5 giờ, 2.3 giờ...). Việc này phù hợp với các kiểm định như F-test/ANOVA."
  },
  {
    "id": 147,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Ghép các ví dụ phát triển sản phẩm với loại hình đổi mới của chúng:\nCột 1:\n  (1) Chase Sapphire Reserve\n  (2) Nintendo Switch\n  (3) Ứng dụng theo dõi sức khỏe số\nCột 2:\n  (a) Sản phẩm dịch vụ tài chính có chương trình điểm thưởng lớn\n  (b) Phần cứng vật lý tích hợp cách chơi đa dạng (cầm tay/console)\n  (c) Sản phẩm tồn tại hoàn toàn trên web, không có hiện diện vật lý\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "Chase = Tài chính. Nintendo = Phần cứng. Ứng dụng = Sản phẩm ảo/web."
  },
  {
    "id": 148,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Khó",
    "question": "Điền từ về hậu quả khi một doanh nghiệp phản ứng chậm với thị trường:\n\"Bằng cách không điều chỉnh theo động lực thị trường đang thay đổi, doanh nghiệp có khả năng ___(1)___ mà người mới tham gia có thể khai thác, dẫn đến việc họ nhận ra quá muộn và không thể ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) phục hồi vị thế của mình ; (2) mất đi các cơ hội",
      "B": "(1) mất đi các cơ hội ; (2) phục hồi vị thế của mình",
      "C": "(1) phá sản ngay lập tức ; (2) phá sản ngay lập tức",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "Việc giữ nguyên hiện trạng mang rủi ro bỏ lỡ cơ hội, khiến đối thủ cạnh tranh giá rẻ chiếm mất thị phần."
  },
  {
    "id": 149,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Dễ",
    "question": "Sắp xếp theo thứ tự ưu tiên của Cây quyết định từ trên xuống:\n  (1) Tính Gini Impurity cho tất cả các biến dự báo\n  (2) Chọn biến có Gini Impurity thấp nhất làm Nút gốc (Root Node)\n  (3) Tiếp tục phân chia các nhánh bên dưới để giảm mức độ hỗn tạp\n  (4) Hoàn thành và tạo ra Nút lá (Leaf Node) để dự đoán\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Tính Gini -> Xác định root node -> Tạo nhánh -> Tạo nút lá."
  },
  {
    "id": 150,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "difficulty": "Trung bình",
    "question": "Khẳng định nào đúng khi so sánh kiểm định quan hệ tương quan và thử nghiệm A/B?",
    "options": {
      "A": "Thử nghiệm A/B cho phép xác định rõ mối quan hệ nguyên nhân - kết quả (nhân quả)",
      "B": "Thử nghiệm tương quan luôn mang lại độ chính xác cao hơn thử nghiệm A/B",
      "C": "Thử nghiệm A/B không thể dùng để kiểm tra tính năng phần mềm mới",
      "D": "Cả hai đều không yêu cầu phân bổ ngẫu nhiên người tham gia"
    },
    "correct": "A",
    "explanation": "Thử nghiệm A/B là thử nghiệm can thiệp ngẫu nhiên (Causal Testing), giúp tìm ra quan hệ nhân quả (ví dụ: do nút màu đỏ mà lượng click tăng)."
  },
  {
    "id": 151,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Dễ",
    "question": "Ứng dụng AI giúp Kế toán Điều tra chuyển đổi từ mô hình phản ứng hậu kiểm sang mô hình nào?",
    "options": {
      "A": "Phòng ngừa chủ động (Proactive Prevention)",
      "B": "Kiểm toán truyền thống dựa trên sổ sách giấy tờ",
      "C": "Hệ thống chuyên gia lập trình quy tắc thủ công",
      "D": "Lập báo cáo tài chính nội bộ thủ công hàng quý"
    },
    "correct": "A",
    "explanation": "AI giúp chuyển từ kiểm tra sau khi sự cố xảy ra sang phòng ngừa chủ động và theo thời gian thực."
  },
  {
    "id": 152,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Đâu là điểm yếu lớn nhất của phương pháp chọn mẫu thống kê truyền thống trong phát hiện gian lận?",
    "options": {
      "A": "Cần quá nhiều phần mềm máy tính hiện đại để chạy",
      "B": "Nó bỏ lọt các giao dịch gian lận nằm ngoài mẫu kiểm toán",
      "C": "Nó phân tích 100% giao dịch khiến kế toán viên mệt mỏi",
      "D": "Hệ thống tự động đưa ra quá nhiều cảnh báo giả"
    },
    "correct": "B",
    "explanation": "Chọn mẫu thống kê thường chỉ kiểm tra 5-10% dữ liệu, kẻ gian lận dễ dàng lách qua bằng cách chia nhỏ giao dịch (Smurfing)."
  },
  {
    "id": 153,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Dễ",
    "question": "Ghép các công nghệ AI với tính năng chính trong phát hiện gian lận:\nCột 1:\n  (1) Xử lý Ngôn ngữ Tự nhiên (NLP)\n  (2) Phân tích Mạng lưới (Graph Analysis)\n  (3) Học không giám sát (Unsupervised ML)\nCột 2:\n  (a) Đọc hiểu email, hợp đồng và biên bản họp\n  (b) Trực quan hóa quan hệ giữa các tài khoản, IP, công ty sân sau\n  (c) Tự động gom cụm, tìm điểm ngoại lai mà không cần gán nhãn\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "NLP đọc văn bản. Graph vẽ sơ đồ mạng lưới quan hệ. Unsupervised ML tìm điểm bất thường từ dữ liệu thô."
  },
  {
    "id": 154,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Sắp xếp theo Lộ trình 7 Bước Triển khai AI trong Kế toán (4 bước đầu):\n  (1) Đánh giá chiến lược và xác định nút thắt cổ chai\n  (2) Chọn lựa công cụ AI phù hợp quy mô doanh nghiệp\n  (3) Đào tạo nhân sự kỹ năng AI, xóa bỏ tâm lý e ngại\n  (4) Triển khai thí điểm (Pilot) trên tác vụ lặp đi lặp lại\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (4) ➔ (3)",
      "D": "(1) ➔ (2) ➔ (3) ➔ (4)"
    },
    "correct": "D",
    "explanation": "Lộ trình: Đánh giá chiến lược -> Chọn công cụ -> Đào tạo nhân lực -> Triển khai Pilot."
  },
  {
    "id": 155,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Điền từ vào khái niệm phân tích dữ liệu gian lận:\n\"Thay vì kiểm tra hậu kỳ (sau khi kết thúc kỳ kế toán), hệ thống AI phân tích toàn phần 100% dữ liệu theo ___(1)___, giúp phát hiện và ngăn chặn giao dịch bất thường nhằm giảm thiểu ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) cảnh báo giả (false positives) ; (2) thời gian thực (real-time)",
      "B": "(1) chu kỳ hàng năm ; (2) chu kỳ hàng năm",
      "C": "(1) thời gian thực (real-time) ; (2) cảnh báo giả (false positives)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "C",
    "explanation": "Real-time anomaly detection giúp cảnh báo ngay khi giao dịch xảy ra, đồng thời AI học cách giảm bớt cảnh báo giả (false positives)."
  },
  {
    "id": 156,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Khó",
    "question": "Hiện tượng 'ảo giác' (Hallucination) trong AI Tạo sinh (GenAI) mang lại rủi ro gì lớn nhất cho ngành kế toán?",
    "options": {
      "A": "AI sinh ra thông tin, trích dẫn hoặc số liệu tài chính không có thật",
      "B": "Nó làm máy tính của kế toán viên tiêu thụ quá nhiều điện năng",
      "C": "Không thể kết nối với mạng nội bộ của doanh nghiệp",
      "D": "Luôn dự báo lạm phát sai lệch do lỗi phần cứng"
    },
    "correct": "A",
    "explanation": "Ảo giác của GenAI là hiện tượng nó tự bịa ra thông tin sai lệch trông có vẻ hợp lý, rất nguy hiểm nếu áp dụng vào BCTC."
  },
  {
    "id": 157,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Dễ",
    "question": "Mô hình Học máy nào phù hợp nhất để nhận diện các chiêu thức gian lận ĐÃ BIẾT từ dữ liệu lịch sử?",
    "options": {
      "A": "Học không giám sát (Unsupervised Learning)",
      "B": "Học có giám sát (Supervised Learning)",
      "C": "Hệ thống lưu trữ đám mây phân tán",
      "D": "Thuật toán K-Means Clustering"
    },
    "correct": "B",
    "explanation": "Học có giám sát dùng dữ liệu đã gán nhãn ('gian lận' / 'hợp lệ') để nhận diện lại các hành vi gian lận đã biết."
  },
  {
    "id": 158,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Khó",
    "question": "Ghép các thuật ngữ kỹ thuật dữ liệu tài chính với đặc điểm của chúng:\nCột 1:\n  (1) Underfitting (Độ lệch cao)\n  (2) Overfitting (Phương sai cao)\n  (3) Bias vs. Variance Tradeoff\nCột 2:\n  (a) Mô hình quá đơn giản, không học được quy luật dữ liệu\n  (b) Mô hình quá phức tạp, học vẹt cả nhiễu của dữ liệu huấn luyện\n  (c) Quá trình tìm điểm cân bằng tối ưu giữa hai lỗi sai số trên\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-a, 2-b, 3-c",
      "B": "1-c, 2-b, 3-a",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "A",
    "explanation": "Underfitting là Bias cao. Overfitting là Variance cao. Điểm cân bằng là Tradeoff."
  },
  {
    "id": 159,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Điền từ liên quan đến quá trình huấn luyện Học máy (Modeling Process):\n\"Để đánh giá mô hình, tập dữ liệu được chia làm hai phần: Tập ___(1)___ (thường chiếm 80%) để mô hình học quy luật và Tập ___(2)___ (thường 20%) dùng để đánh giá hiệu suất khách quan.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) kiểm tra (Test set) ; (2) huấn luyện (Training set)",
      "B": "(1) ngoại lai (Outliers) ; (2) ngoại lai (Outliers)",
      "C": "(1) huấn luyện (Training set) ; (2) kiểm tra (Test set)",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "C",
    "explanation": "Data luôn được chia Train (để học) và Test (để kiểm chứng)."
  },
  {
    "id": 160,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Khó",
    "question": "Sắp xếp Vòng đời Dự án Khoa học Dữ liệu trong Kiểm tra Gian lận (Data Science Lifecycle):\n  (1) Hiểu bài toán nghiệp vụ (Xác định mục tiêu chống gian lận)\n  (2) Đánh giá, làm sạch & Chuẩn bị dữ liệu (Data Preparation)\n  (3) Mô hình hóa (Modeling) & Đánh giá hiệu suất thuật toán\n  (4) Triển khai hệ thống (Deployment) vào giám sát thực tế\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "B",
    "explanation": "Theo hình 6.4: Business Understanding -> Data Prep -> Modeling & Evaluation -> Deployment."
  },
  {
    "id": 161,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Trong Case Study 4, cơ quan nhà nước đã phát hiện 'Thông đồng đấu thầu' (Bid-rigging) thông qua thuật toán nào?",
    "options": {
      "A": "Hồi quy tuyến tính đơn giản trên bảng tính Excel",
      "B": "Phân tích bất thường kết hợp phân tích mạng lưới (Graph Analytics)",
      "C": "Mạng nơ-ron nhân tạo thế hệ đầu từ thập niên 90",
      "D": "Học có giám sát dùng dữ liệu gian lận ngân hàng"
    },
    "correct": "B",
    "explanation": "AI phân tích bất thường và Graph Analytics theo dõi lịch sử nộp thầu của các công ty có liên quan (sân sau)."
  },
  {
    "id": 162,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Dễ",
    "question": "Theo báo cáo, công nghệ Trí tuệ Nhân tạo đang tác động đến ngành Kế toán - Kiểm toán như thế nào?",
    "options": {
      "A": "Loại bỏ hoàn toàn sự can thiệp và kiểm soát của con người",
      "B": "Thay thế phán đoán nghề nghiệp của kiểm toán viên",
      "C": "Tự động kiểm tra 100% dữ liệu, chuyển hướng sang kiểm toán liên tục",
      "D": "Làm chậm quá trình phát hành báo cáo tài chính cuối năm"
    },
    "correct": "C",
    "explanation": "AI tự động kiểm tra 100% dữ liệu giúp kiểm toán viên chuyển từ lấy mẫu sang Kiểm toán liên tục (Continuous Auditing)."
  },
  {
    "id": 163,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Ghép các cấp độ AI với định nghĩa trong Kế toán (Theo biểu đồ Venn):\nCột 1:\n  (1) Trí tuệ nhân tạo (AI)\n  (2) Học máy (ML)\n  (3) Học sâu (Deep Learning)\nCột 2:\n  (a) Khái niệm rộng nhất về máy tính mô phỏng trí thông minh con người\n  (b) Máy tính sử dụng thuật toán thống kê để tự học từ dữ liệu tài chính\n  (c) Phân nhánh nâng cao dùng mạng nơ-ron nhiều lớp (nhận diện hình ảnh/chữ viết)\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-a, 2-b, 3-c",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "B",
    "explanation": "AI là tập lớn nhất. ML là tập con của AI. DL là tập con của ML chuyên xử lý phức tạp bằng mạng nơ-ron."
  },
  {
    "id": 164,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Khó",
    "question": "Điền từ về hệ thống phát hiện gian lận tiền lương (Payroll Fraud):\n\"Trong Case Study Tập đoàn Đa quốc gia, AI sử dụng kỹ thuật phân cụm ___(1)___ để đối chiếu chéo thông tin ngân hàng và mã số thuế, qua đó phát hiện các tài khoản ___(2)___ do quản lý chi nhánh cấu kết tạo ra.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) nhân viên ma (ghost employees) ; (2) không giám sát (Unsupervised)",
      "B": "(1) đám mây phân tán ; (2) đám mây phân tán",
      "C": "Phương án điền từ khác 3",
      "D": "(1) không giám sát (Unsupervised) ; (2) nhân viên ma (ghost employees)"
    },
    "correct": "D",
    "explanation": "Sử dụng Unsupervised Learning để tìm các 'ghost employees' không có thật nhằm bòn rút tiền lương."
  },
  {
    "id": 165,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình Phát triển Hệ thống Big Data (Tech Stack):\n  (1) Hệ thống ghi nhận dữ liệu từ các giao dịch thô (Data Sources)\n  (2) Hệ thống truyền tải sự kiện trực tuyến (Ví dụ: Apache Kafka)\n  (3) Hệ thống lưu trữ phân tán và xử lý đám mây (Hadoop/Spark)\n  (4) Giao diện trực quan hóa dữ liệu cho Kế toán viên (Tableau/Power BI)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "B": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "C": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "C",
    "explanation": "Tech stack flow: Nguồn dữ liệu -> Streaming/Kafka -> Data Lake/Hadoop -> Visualization BI tools."
  },
  {
    "id": 166,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Trong kinh tế vĩ mô, Ngân hàng Trung ương sử dụng AI để cảnh báo hiện tượng 'Rút tiền ồ ạt' (Bank Run) như thế nào?",
    "options": {
      "A": "Từ chối mọi yêu cầu rút tiền của khách hàng cá nhân",
      "B": "Phân tích tự động các chỉ số thanh khoản, dòng tiền gửi và tỷ lệ nợ xấu",
      "C": "Xóa bỏ các hồ sơ vay vốn có rủi ro cao một cách thủ công",
      "D": "Chỉ dựa vào các tin đồn vô căn cứ trên báo chí truyền thông"
    },
    "correct": "B",
    "explanation": "AI quét hàng vạn chỉ tiêu báo cáo tuân thủ từ các ngân hàng để phát hiện sớm sụt giảm thanh khoản, ngăn chặn Bank Run."
  },
  {
    "id": 167,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Dễ",
    "question": "Ghép các ứng dụng GenAI với lĩnh vực Kế toán cụ thể:\nCột 1:\n  (1) Kế toán Tài chính\n  (2) Kế toán Quản trị\n  (3) Tư vấn Thuế\nCột 2:\n  (a) Tự động phân loại hóa đơn (OCR) và hạch toán\n  (b) Dự báo dòng tiền (Cash Flow) và phân tích phương sai\n  (c) Rà soát luật thuế, chuẩn bị tờ khai tối ưu hóa chi phí\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-a, 2-b, 3-c",
      "C": "1-b, 2-c, 3-a",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "B",
    "explanation": "Tài chính -> hạch toán. Quản trị -> dự báo tương lai. Thuế -> chuẩn bị tờ khai."
  },
  {
    "id": 168,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Khó",
    "question": "Việc sử dụng công nghệ AI 'hộp đen' (Black-box) trong kiểm toán gặp trở ngại pháp lý gì lớn nhất?",
    "options": {
      "A": "Không thể giải thích cho cơ quan pháp luật lý do AI đưa ra kết luận",
      "B": "Chi phí quá rẻ khiến hệ thống mất đi sự uy tín",
      "C": "Hộp đen không thể đọc được dữ liệu phi cấu trúc",
      "D": "Chỉ hoạt động được trên các máy tính siêu phân luồng"
    },
    "correct": "A",
    "explanation": "Black-box AI khó giải thích quy trình ra quyết định, gây khó khăn khi cần trình bày căn cứ khởi tố trước Tòa án."
  },
  {
    "id": 169,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Dễ",
    "question": "Điền từ liên quan đến sự giám sát của con người đối với AI:\n\"Mặc dù AI có thể tự động hóa hàng loạt quy trình kế toán, nguyên tắc ___(1)___ yêu cầu Kế toán viên phải luôn luôn kiểm duyệt và duy trì sự kiểm soát cuối cùng, kết hợp với ___(2)___ để ra quyết định.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) Human-in-the-loop ; (2) phán đoán nghề nghiệp",
      "B": "(1) phán đoán nghề nghiệp ; (2) Human-in-the-loop",
      "C": "(1) làm sạch dữ liệu ; (2) làm sạch dữ liệu",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "A",
    "explanation": "Nguyên tắc 'Người dùng trong vòng lặp' (Human-in-the-loop) nhấn mạnh vai trò quyết định cuối cùng vẫn thuộc về chuyên gia."
  },
  {
    "id": 170,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Trong Case Study 3 (Bảo hiểm), AI kết hợp NLP với Computer Vision để giải quyết vấn đề gì?",
    "options": {
      "A": "Xác định xem nhân viên bảo hiểm có đi làm đúng giờ hay không",
      "B": "Đọc báo cáo giám định và phân tích ảnh hiện trường để tìm dấu hiệu chỉnh sửa",
      "C": "Phân tích giá cổ phiếu của các công ty bảo hiểm trên sàn chứng khoán",
      "D": "In hóa đơn bồi thường ra giấy một cách tự động"
    },
    "correct": "B",
    "explanation": "NLP đọc văn bản giám định và Computer Vision phân tích hình ảnh xem ảnh tai nạn có bị photoshop cắt ghép hay không."
  },
  {
    "id": 171,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Dễ",
    "question": "Sắp xếp mức độ phức tạp từ thấp đến cao trong 3 trụ cột kỹ năng Kế toán viên hiện đại (Venn Diagram):\n  (1) Kiến thức chuyên môn Kế toán / Tài chính cốt lõi\n  (2) Sử dụng công cụ tính toán Thống kê và Excel trung cấp\n  (3) Viết truy vấn SQL, Python để xử lý Dữ liệu lớn (Big Data)\n  (4) Xây dựng và huấn luyện mô hình Học máy (Machine Learning)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Từ kiến thức kế toán nền tảng -> Thống kê Excel -> SQL/Python Big data -> ML modeling."
  },
  {
    "id": 172,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Khó",
    "question": "Ghép các Khung Kỹ năng Cần thiết trong thời đại AI (Bảng 2.2) với mức độ quan trọng:\nCột 1:\n  (1) Tư duy phản biện & Thẩm định (Kiểm chứng sai lệch)\n  (2) Kỹ thuật Prompt & Giao tiếp AI (SPARKS)\n  (3) Đạo đức & Tuân thủ Pháp lý (GDPR)\nCột 2:\n  (a) Quan trọng nhất, bắt buộc để chặn ảo giác AI trước khi duyệt\n  (b) Kỹ năng cốt lõi giúp điều khiển và ra lệnh chính xác cho ChatGPT\n  (c) Rất cao, đảm bảo không vi phạm bảo mật dữ liệu khách hàng\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-a, 2-b, 3-c",
      "D": "1-b, 2-a, 3-c"
    },
    "correct": "C",
    "explanation": "Phản biện là quan trọng nhất để tránh báo cáo sai. Prompt là công cụ giao tiếp hằng ngày. Tuân thủ GDPR bảo vệ quyền riêng tư."
  },
  {
    "id": 173,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Khái niệm 'Giải thích mô hình' (Explainable AI - XAI) có ý nghĩa gì trong kiểm toán?",
    "options": {
      "A": "Mô hình giúp người dùng biết được lý do tại sao AI lại ra kết luận gian lận",
      "B": "Mô hình có thể tự động thuyết trình bằng giọng nói qua loa",
      "C": "Mô hình giấu kín thuật toán để bảo mật 100% trước đối thủ",
      "D": "AI không cần giải thích gì vì kết quả của nó luôn luôn đúng"
    },
    "correct": "A",
    "explanation": "Explainable AI (XAI) giúp mở 'hộp đen', làm rõ cách AI suy luận để có thể giải trình trước Tòa án hoặc cấp quản lý."
  },
  {
    "id": 174,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Điền từ về rủi ro của AI Tạo sinh (GenAI):\n\"Trong chính sách bảo mật doanh nghiệp, nhân viên kế toán tuyệt đối bị cấm đưa các số liệu tài chính ___(1)___ lên các công cụ AI công cộng (như ChatGPT bản miễn phí) để tránh rò rỉ ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) sở hữu trí tuệ và bí mật kinh doanh ; (2) mật (confidential)",
      "B": "(1) mật (confidential) ; (2) sở hữu trí tuệ và bí mật kinh doanh",
      "C": "(1) đã công bố công khai ; (2) đã công bố công khai",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "Dữ liệu mật bị đưa lên AI công cộng có nguy cơ bị dùng làm dữ liệu huấn luyện, gây rò rỉ bí mật."
  },
  {
    "id": 175,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Trình tự khám phá bất thường trong Mua sắm công (Tackling bid-rigging):\n  (1) Tập hợp hàng nghìn hồ sơ nộp thầu lịch sử\n  (2) Sử dụng Graph Analytics vẽ bản đồ quan hệ (IP, email, cổ đông)\n  (3) Phát hiện tần suất thắng thầu luân phiên và mức giá sát nút dự toán\n  (4) Kết luận mạng lưới thông đồng thầu (collusion) và khởi tố\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Lấy hồ sơ -> Vẽ sơ đồ quan hệ -> Nhận diện mẫu luân phiên -> Kết luận có thông đồng."
  },
  {
    "id": 176,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Dễ",
    "question": "Quá trình EDA (Exploratory Data Analysis) trong học máy dùng để làm gì?",
    "options": {
      "A": "Đóng gói phần mềm để bán cho khách hàng",
      "B": "Thăm dò, vẽ biểu đồ để phát hiện giá trị ngoại lai trước khi huấn luyện",
      "C": "Thay thế nhân viên kế toán quản trị trong việc viết báo cáo",
      "D": "Chỉ dùng để cài đặt mật khẩu cho cơ sở dữ liệu"
    },
    "correct": "B",
    "explanation": "Khám phá dữ liệu (EDA) là bước chuẩn bị, vẽ biểu đồ để hiểu rõ phân phối dữ liệu, tìm lỗi/ngoại lai trước khi đưa vào ML."
  },
  {
    "id": 177,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ thập niên với đặc trưng phân tích gian lận:\nCột 1:\n  (1) Thập niên 1980s (Hệ thống chuyên gia)\n  (2) Thập niên 2000s (Học máy tiên tiến)\n  (3) Thập niên 2020s (AI Tạo sinh)\nCột 2:\n  (a) Chỉ chạy quy tắc tĩnh (If-Then), không thể tự học\n  (b) Chấm điểm rủi ro tự động nhưng thường rơi vào dạng hộp đen khó giải thích\n  (c) Có thể đọc hiểu biên bản cuộc họp và tự động viết báo cáo điều tra\nPhương án ghép cặp đúng là:",
    "options": {
      "A": "1-c, 2-b, 3-a",
      "B": "1-b, 2-c, 3-a",
      "C": "1-b, 2-a, 3-c",
      "D": "1-a, 2-b, 3-c"
    },
    "correct": "D",
    "explanation": "80s: Rule-based. 2000s: Machine Learning black-boxes. 2020s: LLMs, GenAI NLP."
  },
  {
    "id": 178,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Khó",
    "question": "Điền từ về các thuật toán trong Case Study 4:\n\"Để phát hiện nhóm công ty 'sân sau' thông đồng thổi phồng giá trúng thầu để nhận ___(1)___, cơ quan quản lý đã áp dụng hệ thống phát hiện ___(2)___.\"\nChọn cụm từ đúng tương ứng với các vị trí điền khuyết:",
    "options": {
      "A": "(1) bất thường (Anomaly Detection) ; (2) tiền hoa hồng (kickbacks)",
      "B": "(1) tiền hoa hồng (kickbacks) ; (2) bất thường (Anomaly Detection)",
      "C": "(1) nhân viên ma ; (2) nhân viên ma",
      "D": "Phương án điền từ khác 3"
    },
    "correct": "B",
    "explanation": "Bid-riggers thổi giá lên 25-40% để nhận kickbacks. Anomaly Detection (AI) phát hiện quy luật này."
  },
  {
    "id": 179,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Dễ",
    "question": "Trình tự kỹ thuật tạo Biến Mục Tiêu (Target Creation) trong giám sát gian lận:\n  (1) Ghi nhận mọi giao dịch chuyển tiền trong quá khứ\n  (2) Đánh dấu (Label) các giao dịch sạch là số 0\n  (3) Đánh dấu các giao dịch gian lận/vỡ nợ là số 1\n  (4) Nạp tập dữ liệu 0 và 1 này vào mô hình Học có giám sát (Supervised ML)\nThứ tự sắp xếp đúng là:",
    "options": {
      "A": "(1) ➔ (2) ➔ (3) ➔ (4)",
      "B": "(4) ➔ (3) ➔ (2) ➔ (1)",
      "C": "(2) ➔ (1) ➔ (3) ➔ (4)",
      "D": "(1) ➔ (2) ➔ (4) ➔ (3)"
    },
    "correct": "A",
    "explanation": "Thu thập data -> Đánh nhãn 0 (hợp lệ) -> Đánh nhãn 1 (gian lận) -> Train supervised ML."
  },
  {
    "id": 180,
    "session": "Buổi 6: Machine Learning for Finance",
    "difficulty": "Trung bình",
    "question": "Trong Kinh tế học Phát triển (Development Economics), AI và dữ liệu viễn thông được dùng để làm gì?",
    "options": {
      "A": "Theo dõi nội dung tin nhắn cá nhân của người dân",
      "B": "Lập bản đồ nghèo đói (Poverty Mapping) để phân bổ phúc lợi minh bạch",
      "C": "Chặn hoàn toàn các kết nối 5G ở khu vực nông thôn",
      "D": "Điều chỉnh lãi suất ngân hàng thương mại hàng tuần"
    },
    "correct": "B",
    "explanation": "Dữ liệu vệ sinh dịch tễ, viễn thông và điện năng tiêu thụ giúp AI vẽ bản đồ nghèo đói để chính phủ hỗ trợ đúng người yếu thế."
  }
];
