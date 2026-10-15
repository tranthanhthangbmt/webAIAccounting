// Ngân hàng 180 câu hỏi tương tác Buổi 1 - 6 (AI trong Kế toán & Tài chính)
// Các dạng câu hỏi nguyên bản: ordering, matching, fill_in_blanks, multiple_choice
const EXAM_BANK = [
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Sắp xếp các sự kiện lịch sử về công nghệ kế toán theo thứ tự thời gian từ cũ nhất (trên) đến mới nhất (dưới):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Sử dụng bàn tính (Hơn 2000 năm trước)"
      },
      {
        "id": "2",
        "text": "Mua máy tính chuyên dụng cho mục đích kế toán (1955)"
      },
      {
        "id": "3",
        "text": "Sự ra đời của bảng tính điện tử - Spreadsheets (Những năm 1980)"
      },
      {
        "id": "4",
        "text": "Ứng dụng Trí tuệ nhân tạo (Hiện tại và Tương lai)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Công nghệ kế toán tiến hóa từ bàn tính (cũ nhất), đến việc dùng máy tính sơ khai (1955), sau đó là bảng tính điện tử (1980) và hiện tại là AI.",
    "id": 1,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Theo Klaus Schwab (Diễn đàn Kinh tế Thế giới), AI là một trong những công nghệ then chốt thúc đẩy cuộc cách mạng nào?",
    "options": [
      {
        "id": "a",
        "text": "Cách mạng Công nghiệp lần thứ nhất"
      },
      {
        "id": "b",
        "text": "Cách mạng Công nghiệp lần thứ hai"
      },
      {
        "id": "c",
        "text": "Cách mạng Công nghiệp lần thứ ba"
      },
      {
        "id": "d",
        "text": "Cách mạng Công nghiệp lần thứ tư"
      }
    ],
    "correctAnswer": "d",
    "explanation": "Klaus Schwab mô tả kỷ nguyên chuyển đổi số hiện nay, với sự hội tụ của dữ liệu lớn, IoT và AI là Cuộc Cách mạng Công nghiệp Lần thứ tư.",
    "id": 2,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công ty kiểm toán/kế toán (Big4) với các ứng dụng AI thực tế của họ:",
    "left": [
      {
        "id": "l1",
        "text": "EY"
      },
      {
        "id": "l2",
        "text": "Deloitte"
      },
      {
        "id": "l3",
        "text": "KPMG"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Sử dụng công cụ Argus để trích xuất thông tin kế toán từ hợp đồng"
      },
      {
        "id": "r2",
        "text": "Sử dụng thuật toán học máy của IBM để hỗ trợ tuân thủ IFRS 16"
      },
      {
        "id": "r3",
        "text": "Dùng máy bay không người lái (drones) tích hợp AI để kiểm kê hàng tồn kho"
      }
    ],
    "correctPairs": {
      "l1": "r3",
      "l2": "r1",
      "l3": "r2"
    },
    "explanation": "EY dùng drones để kiểm kê. Deloitte dùng công cụ Argus đọc hợp đồng. KPMG dùng AI của IBM cho việc tuân thủ chuẩn mực thuê tài sản IFRS 16.",
    "id": 3,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền các thuật ngữ tương ứng vào chỗ trống để hoàn thành định nghĩa:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "<span class=\"blank-slot\" data-id=\"1\">___(1)___</span> tập trung vào một nhiệm vụ cụ thể (như nhận dạng giọng nói, chơi cờ). Trong khi đó, mục tiêu của <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> là tạo ra máy móc có khả năng thực hiện tất cả các nhiệm vụ nhận thức phức tạp của não bộ con người.",
    "words": [
      {
        "id": "w1",
        "text": "Trí tuệ nhân tạo hẹp (ANI)"
      },
      {
        "id": "w2",
        "text": "Trí tuệ nhân tạo tổng quát (AGI)"
      },
      {
        "id": "w3",
        "text": "Học máy (Machine Learning)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "ANI (AI hẹp/yếu) chỉ tập trung giải quyết một nhiệm vụ cụ thể rất tốt. AGI (AI tổng quát/mạnh) hướng tới năng lực nhận thức linh hoạt như con người.",
    "id": 4,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Đâu là điểm khác biệt cốt lõi giữa Khai phá dữ liệu (Data Mining) và Học máy (Machine Learning) theo chuyên gia Bernard Marr?",
    "options": [
      {
        "id": "a",
        "text": "Khai phá dữ liệu tìm mô hình đã có trong dữ liệu lịch sử, còn Học máy cố gắng dự đoán kết quả tương lai dựa trên dữ liệu."
      },
      {
        "id": "b",
        "text": "Khai phá dữ liệu hoàn toàn tự động, trong khi Học máy cần sự can thiệp của con người xuyên suốt quá trình."
      },
      {
        "id": "c",
        "text": "Khai phá dữ liệu là một lĩnh vực phụ của AI, còn Học máy thì độc lập với AI."
      },
      {
        "id": "d",
        "text": "Khai phá dữ liệu chỉ dùng dữ liệu phi cấu trúc, còn Học máy dùng dữ liệu có cấu trúc."
      }
    ],
    "correctAnswer": "a",
    "explanation": "Khai phá dữ liệu tìm kiếm mô hình đã tồn tại trong tập dữ liệu lịch sử. Học máy tự học từ tập huấn luyện để đưa ra dự đoán cho tương lai.",
    "id": 5,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép nối các loại hình Học máy (Machine Learning) với định nghĩa chính xác nhất:",
    "left": [
      {
        "id": "l1",
        "text": "Học có giám sát (Supervised)"
      },
      {
        "id": "l2",
        "text": "Học không giám sát (Unsupervised)"
      },
      {
        "id": "l3",
        "text": "Học bán giám sát (Semi-supervised)"
      },
      {
        "id": "l4",
        "text": "Học tăng cường (Reinforcement)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Dùng dữ liệu đầu vào CHƯA được gắn nhãn để tìm ra các xu hướng, cụm (clusters)"
      },
      {
        "id": "r2",
        "text": "Kết hợp sử dụng cả dữ liệu ĐÃ được gắn nhãn và CHƯA được gắn nhãn"
      },
      {
        "id": "r3",
        "text": "Học từ tập dữ liệu ĐÃ được gắn nhãn (biết trước đầu vào X dẫn đến đầu ra Y)"
      },
      {
        "id": "r4",
        "text": "Thuật toán tự huấn luyện thông qua thử và sai (nhận phần thưởng hoặc bị phạt)"
      }
    ],
    "correctPairs": {
      "l1": "r3",
      "l2": "r1",
      "l3": "r2",
      "l4": "r4"
    },
    "explanation": "Có giám sát = Có nhãn sẵn; Không giám sát = Không nhãn; Bán giám sát = Dùng cả 2 loại; Tăng cường = Thử và sai (Thưởng/Phạt).",
    "id": 6,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Hội nghị Trí tuệ nhân tạo (AI) đầu tiên được tổ chức vào năm 1956 tại trường đại học nào?",
    "options": [
      {
        "id": "a",
        "text": "Đại học Harvard"
      },
      {
        "id": "b",
        "text": "Đại học Stanford"
      },
      {
        "id": "c",
        "text": "Đại học Dartmouth"
      },
      {
        "id": "d",
        "text": "Viện Công nghệ Massachusetts (MIT)"
      }
    ],
    "correctAnswer": "c",
    "explanation": "Lĩnh vực AI được thiết lập như một chuyên ngành học thuật và nghiên cứu khi hội nghị AI đầu tiên được tổ chức tại Đại học Dartmouth vào năm 1956.",
    "id": 7,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Sắp xếp các mốc lịch sử của AI và Công nghệ từ cũ nhất đến mới nhất:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Mô hình nơ-ron nhân tạo đầu tiên do McCulloch và Pitts đề xuất (1943)"
      },
      {
        "id": "2",
        "text": "Hội nghị AI đầu tiên tại Đại học Dartmouth (1956)"
      },
      {
        "id": "3",
        "text": "Hệ chuyên gia (Expert Systems) ra đời (Những năm 1970)"
      },
      {
        "id": "4",
        "text": "Phần mềm bảng tính điện tử phổ biến trong kế toán (Những năm 1980)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "1943: Mô hình nơ-ron; 1956: Dartmouth; Những năm 1970: Hệ chuyên gia; Những năm 1980: Bảng tính điện tử.",
    "id": 8,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong kế toán quản trị, trí tuệ nhân tạo (AI) thường được sử dụng để thực hiện công việc gì?",
    "options": [
      {
        "id": "a",
        "text": "Chỉ phát hiện giao dịch gian lận trong kiểm toán"
      },
      {
        "id": "b",
        "text": "Tự động mã hóa bút toán kế toán, dự báo doanh thu và phân tích dữ liệu phi cấu trúc"
      },
      {
        "id": "c",
        "text": "Thay thế hoàn toàn giám đốc tài chính (CFO)"
      },
      {
        "id": "d",
        "text": "Khai thuế thủ công cho khách hàng"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Trong kế toán quản trị, AI được sử dụng để tự động mã hóa các bút toán kế toán, dự báo doanh thu và phân tích các dữ liệu phi cấu trúc như hợp đồng, email.",
    "id": 9,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Dễ",
    "question": "Hoàn thành định nghĩa sau về API:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Giao diện lập trình ứng dụng (API) là một tập hợp các chức năng hoặc quy tắc tạo điều kiện cho giao tiếp giữa các <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> và thiết bị.",
    "words": [
      {
        "id": "w1",
        "text": "ứng dụng"
      },
      {
        "id": "w2",
        "text": "cơ sở dữ liệu"
      },
      {
        "id": "w3",
        "text": "thuật toán"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "API là tập hợp các quy tắc tạo điều kiện giao tiếp giữa ứng dụng, cơ sở dữ liệu và thiết bị, hoạt động như các 'sứ giả kỹ thuật số'.",
    "id": 10,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ / khái niệm với ví dụ thực tiễn tương ứng:",
    "left": [
      {
        "id": "l1",
        "text": "Hiểu ngôn ngữ tự nhiên (NLU)"
      },
      {
        "id": "l2",
        "text": "Tạo ngôn ngữ tự nhiên (NLG)"
      },
      {
        "id": "l3",
        "text": "API (Giao diện lập trình ứng dụng)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Siri nhận diện và hiểu câu hỏi 'Thời tiết hôm nay thế nào?'"
      },
      {
        "id": "r2",
        "text": "Siri trả lời lại bằng giọng nói: 'Hôm nay trời quang, nhiệt độ 28 độ'"
      },
      {
        "id": "r3",
        "text": "Khách hàng mua vé xem phim qua Fandango bằng cách đăng nhập tài khoản Facebook"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "NLU giúp máy hiểu câu hỏi. NLG giúp máy phát ra câu trả lời bằng ngôn ngữ tự nhiên. API giúp Fandango kết nối với Facebook để đăng nhập.",
    "id": 11,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Ứng dụng nào của Apple sử dụng phương pháp không cần lập trình truyền thống (no-code/low-code) để phát triển mô hình Học máy?",
    "options": [
      {
        "id": "a",
        "text": "Kubeflow"
      },
      {
        "id": "b",
        "text": "Create ML"
      },
      {
        "id": "c",
        "text": "CNTK"
      },
      {
        "id": "d",
        "text": "Anaconda"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Ứng dụng 'Create ML' của Apple cho phép người dùng phát triển và đào tạo các mô hình ML bằng phương pháp kéo-thả (no-code/low-code).",
    "id": 12,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp các khái niệm AI từ phổ quát nhất (rộng nhất) đến chuyên biệt nhất (nhỏ nhất):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Trí tuệ nhân tạo (AI - Artificial Intelligence)"
      },
      {
        "id": "2",
        "text": "Học máy (ML - Machine Learning)"
      },
      {
        "id": "3",
        "text": "Học sâu (DL - Deep Learning)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3"
    ],
    "explanation": "Học sâu (DL) là một tập hợp con của Học máy (ML). Học máy lại là một tập hợp con của Trí tuệ nhân tạo (AI).",
    "id": 13,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Theo Xavier Amatriain, nhận định nào sau đây là ĐÚNG về mối quan hệ giữa Khai phá dữ liệu (Data Mining) và Trí tuệ nhân tạo (AI)?",
    "options": [
      {
        "id": "a",
        "text": "Khai phá dữ liệu là một tập hợp con (sub-field) của AI."
      },
      {
        "id": "b",
        "text": "Khai phá dữ liệu giao thoa với AI nhưng KHÔNG được coi là một lĩnh vực phụ của AI."
      },
      {
        "id": "c",
        "text": "AI là một lĩnh vực phụ của Khai phá dữ liệu."
      },
      {
        "id": "d",
        "text": "Khai phá dữ liệu và AI hoàn toàn không có sự liên quan nào."
      }
    ],
    "correctAnswer": "b",
    "explanation": "Khai phá dữ liệu giao thoa với AI nhưng không được coi là lĩnh vực phụ. Khai phá dữ liệu có thể sử dụng học máy (một phần của AI) nhưng cũng sử dụng các kỹ thuật khác ngoài học máy.",
    "id": 14,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ nền tảng mã thấp/không mã (low-code/no-code) với nhà phát triển tương ứng:",
    "left": [
      {
        "id": "l1",
        "text": "Create ML"
      },
      {
        "id": "l2",
        "text": "Kubeflow"
      },
      {
        "id": "l3",
        "text": "CNTK (Cognitive Toolkit)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Apple"
      },
      {
        "id": "r2",
        "text": "Google"
      },
      {
        "id": "r3",
        "text": "Microsoft"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Create ML do Apple phát triển. Kubeflow hỗ trợ trên nền tảng AI của Google. CNTK do Microsoft phát triển cho nền tảng Azure.",
    "id": 15,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ thích hợp vào định nghĩa của Học sâu (Deep Learning):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Học sâu là một tập hợp con của học máy sử dụng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để khám phá các mô hình từ dữ liệu. Các mô hình này thường được tăng tốc bởi <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>, một mạch tích hợp chuyên dụng do Google phát triển.",
    "words": [
      {
        "id": "w1",
        "text": "Mạng nơ-ron nhân tạo (ANN)"
      },
      {
        "id": "w2",
        "text": "Bộ xử lý tensor (TPU)"
      },
      {
        "id": "w3",
        "text": "Khai phá dữ liệu"
      },
      {
        "id": "w4",
        "text": "Lô-gic mờ (Fuzzy logic)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Học sâu sử dụng mạng nơ-ron nhân tạo (ANN) lấy cảm hứng từ bộ não người và thường được tăng tốc xử lý bởi bộ xử lý tensor (TPU).",
    "id": 16,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong bối cảnh hệ chuyên gia (Expert Systems), hệ thống nào sử dụng các thuật ngữ không mang tính nhị phân (0 hoặc 1) để đối phó với sự thiếu chính xác và mơ hồ?",
    "options": [
      {
        "id": "a",
        "text": "Hệ chuyên gia dựa trên quy tắc (Rules-based)"
      },
      {
        "id": "b",
        "text": "Hệ chuyên gia dựa trên lô-gic mờ (Fuzzy-based)"
      },
      {
        "id": "c",
        "text": "Mạng nơ-ron nhân tạo (ANN)"
      },
      {
        "id": "d",
        "text": "Xử lý ngôn ngữ tự nhiên (NLP)"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Lô-gic mờ (fuzzy logic) hữu ích trong các tình huống liên quan đến sự thiếu chính xác và mơ hồ, nơi các điều kiện không thể phân định rõ ràng 0 hoặc 1 (đúng/sai tuyệt đối).",
    "id": 17,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "ordering",
    "difficulty": "Khó",
    "question": "Sắp xếp quy trình Khai phá văn bản (Text Mining) theo thứ tự thực hiện:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Thu thập các nguồn dữ liệu văn bản phi cấu trúc (hợp đồng, email, PDF...)"
      },
      {
        "id": "2",
        "text": "Áp đặt cấu trúc (structure) lên các nguồn dữ liệu văn bản phi cấu trúc này"
      },
      {
        "id": "3",
        "text": "Sử dụng các kỹ thuật khai phá dữ liệu để trích xuất thông tin có liên quan"
      },
      {
        "id": "4",
        "text": "Khám phá các mô hình, xu hướng và chủ đề từ thông tin trích xuất"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Quá trình bắt đầu từ thu thập dữ liệu phi cấu trúc -> áp đặt cấu trúc cho nó -> sử dụng khai phá dữ liệu -> cuối cùng khám phá xu hướng/mô hình.",
    "id": 18,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép các công cụ / ứng dụng với phương thức tiếp cận AI của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "Khai phá văn bản (Text Mining)"
      },
      {
        "id": "l2",
        "text": "Lập luận máy (Machine Reasoning)"
      },
      {
        "id": "l3",
        "text": "Phân tích cụm (Cluster Analysis)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Sử dụng NLP để trích xuất ý nghĩa từ dữ liệu văn bản"
      },
      {
        "id": "r2",
        "text": "Thao tác đại số đối với kiến thức đã thu nhận để suy luận diễn dịch/quy nạp"
      },
      {
        "id": "r3",
        "text": "Nhóm dữ liệu không gắn nhãn lại với nhau dựa trên điểm tương đồng (Học không giám sát)"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Khai phá văn bản sử dụng NLP. Lập luận máy dùng suy luận tự động. Phân tích cụm là phương pháp điển hình của học không giám sát.",
    "id": 19,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Công nghệ RPA (Robotic Process Automation) phù hợp nhất với loại tác vụ nào?",
    "options": [
      {
        "id": "a",
        "text": "Các tác vụ đòi hỏi sự tư duy sáng tạo nghệ thuật"
      },
      {
        "id": "b",
        "text": "Các tác vụ có khối lượng lớn, lặp đi lặp lại và theo quy tắc rõ ràng"
      },
      {
        "id": "c",
        "text": "Các quyết định chiến lược cấp hội đồng quản trị"
      },
      {
        "id": "d",
        "text": "Sáng tác nhạc và vẽ tranh"
      }
    ],
    "correctAnswer": "b",
    "explanation": "RPA rất phù hợp với các tác vụ có khối lượng lớn và lặp đi lặp lại (như đối chiếu ngân hàng, xử lý hóa đơn) thường do con người thực hiện trước đây.",
    "id": 20,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Khó",
    "question": "Điền từ vào chỗ trống về Lập luận máy (Machine Reasoning):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Các hệ thống Lập luận máy sử dụng kỹ thuật suy luận tự động để bắt chước con người, chẳng hạn như <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (deduction) và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> (induction).",
    "words": [
      {
        "id": "w1",
        "text": "diễn dịch"
      },
      {
        "id": "w2",
        "text": "quy nạp"
      },
      {
        "id": "w3",
        "text": "dự đoán"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Lập luận máy sử dụng kỹ thuật suy luận tự động như diễn dịch (từ cái chung suy ra cái riêng) và quy nạp (từ số liệu cụ thể khái quát thành cái chung).",
    "id": 21,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong ví dụ về Học có giám sát (Supervised Learning), biến đầu vào (X) và biến đầu ra (Y) được mô tả như thế nào khi dự đoán nợ xấu?",
    "options": [
      {
        "id": "a",
        "text": "X là tuổi nợ của khách hàng, Y là số tiền nợ khó đòi đã xóa sổ"
      },
      {
        "id": "b",
        "text": "X là số lượng nhân viên, Y là doanh thu của công ty"
      },
      {
        "id": "c",
        "text": "X là dữ liệu không dán nhãn, Y là các cụm khách hàng"
      },
      {
        "id": "d",
        "text": "X là mức độ gian lận, Y là tên khách hàng"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Trong bài, mô hình học có giám sát dùng dữ liệu lịch sử: X (đầu vào) là tuổi nợ của khách hàng, Y (đầu ra) là số tiền phải thu khó đòi bị xóa sổ.",
    "id": 22,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình hoạt động của thuật toán Học Tăng cường (Reinforcement Learning):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Tác nhân (agent) thực hiện một hành động (thử và sai) trong môi trường"
      },
      {
        "id": "2",
        "text": "Nhận được phần thưởng (reward) nếu đúng, hoặc hình phạt (penalty) nếu sai"
      },
      {
        "id": "3",
        "text": "Thuật toán học hỏi từ kết quả để điều chỉnh hành vi"
      },
      {
        "id": "4",
        "text": "Tối đa hóa phần thưởng và giảm thiểu hình phạt trong tương lai"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Học tăng cường diễn ra qua quá trình tác nhân thực hiện thử và sai -> nhận thưởng/phạt -> học hỏi -> tối đa hóa phần thưởng ở các lần sau.",
    "id": 23,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "matching",
    "difficulty": "Dễ",
    "question": "Ghép các thuật ngữ viết tắt trong AI với nghĩa tiếng Việt của nó:",
    "left": [
      {
        "id": "l1",
        "text": "NLP"
      },
      {
        "id": "l2",
        "text": "RPA"
      },
      {
        "id": "l3",
        "text": "IoT"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Xử lý ngôn ngữ tự nhiên"
      },
      {
        "id": "r2",
        "text": "Tự động hóa quy trình bằng robot"
      },
      {
        "id": "r3",
        "text": "Internet vạn vật"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "NLP: Natural Language Processing. RPA: Robotic Process Automation. IoT: Internet of Things.",
    "id": 24,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Theo nghiên cứu của Sophia Sun (2019), Học sâu (Deep Learning) vượt trội hơn Học máy (ML) cổ điển trong điều kiện nào?",
    "options": [
      {
        "id": "a",
        "text": "Khi tập dữ liệu cực kỳ nhỏ và chỉ có vài biến số"
      },
      {
        "id": "b",
        "text": "Khi khối lượng dữ liệu và số lượng biến (variables) rất lớn"
      },
      {
        "id": "c",
        "text": "Khi dữ liệu hoàn toàn có cấu trúc (bảng tính SQL)"
      },
      {
        "id": "d",
        "text": "Khi không có sự xuất hiện của dữ liệu bán cấu trúc hay phi cấu trúc"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Hiệu suất dự đoán của mô hình DL vượt trội hơn ML cổ điển khi khối lượng dữ liệu lớn và số lượng biến (variables) nhiều.",
    "id": 25,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống để hoàn thành định nghĩa về AI của Siegel (2003):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Để máy móc thực hiện được các tác vụ phức tạp tốt bằng hoặc hơn con người, chúng phải có khả năng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>, học hỏi và giao tiếp.",
    "words": [
      {
        "id": "w1",
        "text": "cảm nhận"
      },
      {
        "id": "w2",
        "text": "lập luận"
      },
      {
        "id": "w3",
        "text": "bay lượn"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Theo Siegel et al. (2003), máy móc phải có khả năng cảm nhận (perceive), lập luận (reason), học hỏi (learn) và giao tiếp (communicate).",
    "id": 26,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Bệnh viện Đa khoa Tampa ở Florida đã sử dụng AI trong đại dịch Covid-19 với mục đích gì?",
    "options": [
      {
        "id": "a",
        "text": "Chẩn đoán bệnh nhân qua email"
      },
      {
        "id": "b",
        "text": "Quét nhiệt khuôn mặt để phát hiện các triệu chứng tiềm ẩn (sốt, mồ hôi, đổi màu da)"
      },
      {
        "id": "c",
        "text": "Tính toán chi phí khám bệnh tự động"
      },
      {
        "id": "d",
        "text": "Robot phẫu thuật từ xa"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Bệnh viện Tampa triển khai AI thực hiện quét nhiệt khuôn mặt người vào tòa nhà để phát hiện triệu chứng virus như sốt, đổi màu da.",
    "id": 27,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Quy trình xử lý một lệnh thoại của Siri (ứng dụng của AI và NLP) diễn ra theo thứ tự nào?",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Người dùng nói: 'Thời tiết hôm nay thế nào?'"
      },
      {
        "id": "2",
        "text": "NLU (Hiểu ngôn ngữ tự nhiên) giúp máy tính phân tích và hiểu yêu cầu"
      },
      {
        "id": "3",
        "text": "Máy tính truy xuất dữ liệu thời tiết qua API Internet"
      },
      {
        "id": "4",
        "text": "NLG (Tạo ngôn ngữ tự nhiên) chuyển dữ liệu thành câu trả lời bằng giọng nói"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Người dùng ra lệnh -> Máy hiểu lệnh (NLU) -> Máy lấy thông tin -> Máy trả lời lại bằng ngôn ngữ tự nhiên (NLG).",
    "id": 28,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công cụ lập trình AI với đặc điểm của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "Python và R"
      },
      {
        "id": "l2",
        "text": "SQL và NoSQL"
      },
      {
        "id": "l3",
        "text": "UiPath và BluePrism"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Ngôn ngữ mã nguồn mở phổ biến nhất để xây dựng và tùy chỉnh ứng dụng AI/ML"
      },
      {
        "id": "r2",
        "text": "Công cụ truy xuất, chỉnh sửa và thao tác với cơ sở dữ liệu"
      },
      {
        "id": "r3",
        "text": "Các nền tảng phần mềm phổ biến cho Tự động hóa quy trình bằng robot (RPA)"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Python/R mạnh về AI/ML. SQL/NoSQL mạnh về xử lý cơ sở dữ liệu. UiPath/BluePrism là phần mềm RPA.",
    "id": 29,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Việc sử dụng thuật toán máy tính (như Amazon, Netflix) để đề xuất phim hoặc sản phẩm dựa trên lịch sử mua sắm của bạn là một ứng dụng phổ biến của lĩnh vực nào?",
    "options": [
      {
        "id": "a",
        "text": "Học máy (Machine Learning)"
      },
      {
        "id": "b",
        "text": "Khai phá văn bản (Text Mining)"
      },
      {
        "id": "c",
        "text": "Lập luận máy (Machine Reasoning)"
      },
      {
        "id": "d",
        "text": "Tự động hóa quy trình (RPA)"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Hệ thống đề xuất (recommendation engines) của Amazon hay Netflix là ví dụ kinh điển của Học máy (ML), học từ dữ liệu quá khứ để dự đoán sở thích tương lai.",
    "id": 30,
    "session": "Buổi 1: What Accountants Need to Know",
    "session_key": "Day01"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Satoshi Nakamoto đã tạo ra Bitcoin dựa trên niềm tin rằng internet cần một loại tiền tệ có tính chất gì?",
    "options": [
      {
        "id": "a",
        "text": "Tập trung và được quản lý bởi ngân hàng trung ương"
      },
      {
        "id": "b",
        "text": "Phi tập trung, bảo vệ bằng mật mã và trao đổi ngang hàng"
      },
      {
        "id": "c",
        "text": "Được hậu thuẫn bởi vàng hoặc bạc"
      },
      {
        "id": "d",
        "text": "Chỉ sử dụng để thanh toán cho các dịch vụ phần mềm"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Nakamoto tin rằng internet cần một loại tiền tệ phi tập trung (decentralized), được bảo vệ bằng mật mã (cryptography) và thuận lợi cho trao đổi ngang hàng (peer-to-peer exchange).",
    "id": 31,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Sắp xếp các khái niệm sau từ cấp độ rộng nhất (bao quát nhất) đến cấp độ hẹp nhất (chuyên biệt nhất) trong khoa học máy tính:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Trí tuệ nhân tạo (AI)"
      },
      {
        "id": "2",
        "text": "Học máy (Machine Learning)"
      },
      {
        "id": "3",
        "text": "Học sâu (Deep Learning)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3"
    ],
    "explanation": "Học sâu (Deep Learning) là một dạng đặc biệt của Học máy (Machine Learning), và Học máy là một nhánh của Trí tuệ nhân tạo (AI).",
    "id": 32,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các loại tiền mã hóa với đặc điểm nổi bật của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "Bitcoin"
      },
      {
        "id": "l2",
        "text": "Ethereum"
      },
      {
        "id": "l3",
        "text": "Zcash"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Nền tảng phần mềm phi tập trung cho phép chạy Hợp đồng thông minh (Smart Contracts)"
      },
      {
        "id": "r2",
        "text": "Tiền mã hóa đầu tiên, dựa trên mô hình ngang hàng (P2P), không phụ thuộc tổ chức phát hành"
      },
      {
        "id": "r3",
        "text": "Cung cấp tính năng an toàn hơn thông qua các giao dịch được che chắn (shielded transactions)"
      }
    ],
    "correctPairs": {
      "l1": "r2",
      "l2": "r1",
      "l3": "r3"
    },
    "explanation": "Bitcoin là tiền mã hóa tiên phong. Ethereum nổi bật với Hợp đồng thông minh. Zcash tập trung vào quyền riêng tư bằng các giao dịch được che chắn.",
    "id": 33,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Hoàn thành nhận định về sự khác biệt giữa AI, ML và Khoa học Dữ liệu:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "<span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> không cấu thành nên một nhánh của khoa học dữ liệu. Thay vào đó, <span class=\"blank-slot\" data-id=\"3\">___(3)___</span> sử dụng chúng như một bộ công cụ thống kê để giải quyết các vấn đề từ dữ liệu.",
    "words": [
      {
        "id": "w1",
        "text": "Trí tuệ nhân tạo (AI)"
      },
      {
        "id": "w2",
        "text": "Học máy (ML)"
      },
      {
        "id": "w3",
        "text": "Khoa học Dữ liệu"
      },
      {
        "id": "w4",
        "text": "Tự động hóa (RPA)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2",
      "3": "w3"
    },
    "explanation": "AI và ML là các công cụ mà Khoa học Dữ liệu sử dụng. Khoa học Dữ liệu là quy trình rộng hơn bao gồm thu thập, phân tích, trực quan hóa và mô hình hóa.",
    "id": 34,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Quan điểm của Tòa án Tối cao Tây Ban Nha (2019) về bản chất pháp lý của Bitcoin là gì?",
    "options": [
      {
        "id": "a",
        "text": "Bitcoin được công nhận là một loại tiền tệ hợp pháp (legal tender)"
      },
      {
        "id": "b",
        "text": "Bitcoin bị từ chối công nhận là tiền hợp pháp nhưng được coi là 'tài sản vô hình' (incorporeal asset)"
      },
      {
        "id": "c",
        "text": "Bitcoin bị cấm hoàn toàn trong các giao dịch thương mại"
      },
      {
        "id": "d",
        "text": "Bitcoin được coi là một dạng chứng khoán phái sinh (derivative security)"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Bản án của Tòa án Tối cao Tây Ban Nha ngày 20/06/2019 đã từ chối công nhận Bitcoin là tiền tệ hợp pháp (money) mà coi nó là một tài sản vô hình.",
    "id": 35,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Ba trụ cột chuyên môn (theo biểu đồ Venn) tạo nên một Nhà khoa học dữ liệu (Data Scientist) là gì?",
    "options": [
      {
        "id": "a",
        "text": "Thống kê/Toán học, Khoa học máy tính, và Chuyên môn ngành (Domain expertise)"
      },
      {
        "id": "b",
        "text": "Tài chính kế toán, Nhân sự, và Marketing"
      },
      {
        "id": "c",
        "text": "Lập trình web, Thiết kế đồ họa, và Quản trị kinh doanh"
      },
      {
        "id": "d",
        "text": "Trí tuệ nhân tạo, Khai phá văn bản, và Lập luận máy"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Khoa học dữ liệu là lĩnh vực liên ngành sử dụng Thống kê/Toán học, Khoa học máy tính và Chuyên môn trong lĩnh vực cụ thể.",
    "id": 36,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép nối các khái niệm trong Vũ trụ ảo (Metaverse) với ý nghĩa của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "Vũ trụ ảo mã hóa (Crypto-metaverse)"
      },
      {
        "id": "l2",
        "text": "Giao dịch thuật toán (Algorithmic trading)"
      },
      {
        "id": "l3",
        "text": "Tài chính phi tập trung (DeFi) trong Metaverse"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Sự tích hợp mạnh mẽ giữa công nghệ chuỗi khối và tiền mã hóa vào các môi trường ảo"
      },
      {
        "id": "r2",
        "text": "Thực hiện giao dịch tự động trên thị trường nhờ các thuật toán AI"
      },
      {
        "id": "r3",
        "text": "Cho phép người dùng đi vay, cho vay và kiếm lợi nhuận ngay trong thế giới ảo mà không cần ngân hàng truyền thống"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Metaverse sử dụng Crypto (blockchain/coin) làm nền tảng kinh tế. AI hỗ trợ giao dịch thuật toán tự động. DeFi giúp giao dịch tài chính không cần trung gian.",
    "id": 37,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "ordering",
    "difficulty": "Khó",
    "question": "Quy trình ứng dụng NFT (được tạo bởi AI) làm tài sản thế chấp trong hệ sinh thái DeFi diễn ra theo trình tự nào?",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "AI sáng tạo hoặc hợp tác với nghệ sĩ để tạo ra tác phẩm nghệ thuật số"
      },
      {
        "id": "2",
        "text": "Tác phẩm nghệ thuật số được mã hóa (tokenized) thành một NFT trên chuỗi khối"
      },
      {
        "id": "3",
        "text": "Người dùng mang NFT này thế chấp (collateral) vào một nền tảng DeFi"
      },
      {
        "id": "4",
        "text": "Người dùng nhận được khoản vay (bằng crypto) mà không cần phải bán đứt NFT"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Đầu tiên tạo tác phẩm (bằng AI) -> Mã hóa thành NFT -> Thế chấp trên DeFi -> Nhận khoản vay. Đây là ứng dụng thanh khoản mới cho NFT.",
    "id": 38,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Dễ",
    "question": "Điền từ thích hợp để hoàn thành khái niệm về sự kết hợp giữa Chuỗi khối và AI:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "<span class=\"blank-slot\" data-id=\"1\">___(1)___</span> cung cấp tính minh bạch, bảo mật và hồ sơ giao dịch không thể sửa đổi. Trong khi đó, <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> đóng góp vào việc phân tích dự đoán và tự động hóa theo thời gian thực.",
    "words": [
      {
        "id": "w1",
        "text": "Công nghệ Chuỗi khối (Blockchain)"
      },
      {
        "id": "w2",
        "text": "Trí tuệ nhân tạo (AI)"
      },
      {
        "id": "w3",
        "text": "Dữ liệu lớn (Big Data)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Blockchain bảo đảm dữ liệu an toàn và bất biến, còn AI dùng dữ liệu đó để phân tích và đưa ra quyết định dự đoán.",
    "id": 39,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "CBDC (Central Bank Digital Currency) là gì?",
    "options": [
      {
        "id": "a",
        "text": "Đồng tiền ảo do một nhóm lập trình viên ẩn danh tạo ra"
      },
      {
        "id": "b",
        "text": "Tiền kỹ thuật số được phát hành và kiểm soát bởi ngân hàng trung ương của một quốc gia"
      },
      {
        "id": "c",
        "text": "Một thuật toán khai phá dữ liệu trên thị trường chứng khoán"
      },
      {
        "id": "d",
        "text": "Hệ thống máy chủ đám mây của các ngân hàng thương mại"
      }
    ],
    "correctAnswer": "b",
    "explanation": "CBDC (Central Bank Digital Currency) là nỗ lực của các chính phủ bước vào cuộc chơi tài sản kỹ thuật số nhằm phát hành tiền kỹ thuật số mang tính quốc gia.",
    "id": 40,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Theo quan điểm của Tổng biện lý (Advocate General), lý do chính khiến Bitcoin KHÔNG được coi là 'Tiền' là gì?",
    "options": [
      {
        "id": "a",
        "text": "Vì nó chỉ được sử dụng ở Châu Âu"
      },
      {
        "id": "b",
        "text": "Vì nó không thực hiện đủ 3 chức năng: phương tiện trao đổi, công cụ lưu trữ giá trị, và đơn vị kế toán, đồng thời không được thực thể trung tâm nào hậu thuẫn"
      },
      {
        "id": "c",
        "text": "Vì giá trị vốn hóa của nó còn quá thấp (dưới 1 triệu Euro)"
      },
      {
        "id": "d",
        "text": "Vì nó sử dụng công nghệ chuỗi khối quá phức tạp"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Tổng biện lý cho rằng Bitcoin chậm chạp, tốn kém, không đảm bảo chuyển đổi ra tiền mặt và không có sự quản lý/hậu thuẫn từ cơ quan công quyền, nên không thực hiện đủ chức năng của tiền.",
    "id": 41,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Sự khác biệt giữa Nhà khoa học dữ liệu và Nhà phân tích kinh doanh/dữ liệu:",
    "left": [
      {
        "id": "l1",
        "text": "Nhà phân tích kinh doanh (Business Analyst)"
      },
      {
        "id": "l2",
        "text": "Nhà khoa học dữ liệu (Data Scientist)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Sử dụng chuyên môn ngành và phân tích để tạo insight, ít tập trung vào lập trình mô hình học máy"
      },
      {
        "id": "r2",
        "text": "Vai trò rộng hơn, bao gồm lập trình, phân tích thống kê và xây dựng mô hình học máy (Machine Learning)"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2"
    },
    "explanation": "Business Analyst tập trung vào business insight. Data Scientist có kỹ năng lập trình và toán học cao hơn để xây dựng các mô hình dự đoán (ML/AI).",
    "id": 42,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Quá trình một Nhà khoa học dữ liệu giải quyết vấn đề bằng Học máy diễn ra theo các bước chung nào?",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Thu thập dữ liệu (Data collection)"
      },
      {
        "id": "2",
        "text": "Xử lý và làm sạch dữ liệu (Data processing)"
      },
      {
        "id": "3",
        "text": "Xây dựng mô hình Học máy (Modeling)"
      },
      {
        "id": "4",
        "text": "Đưa ra các dự đoán và trực quan hóa kết quả"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Quy trình tiêu chuẩn: Thu thập -> Tiền xử lý (làm sạch) -> Xây dựng mô hình -> Dự đoán/Đánh giá.",
    "id": 43,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Khó",
    "question": "Điền từ vào chỗ trống liên quan đến rủi ro không gian mạng của Metaverse:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Sự xuất hiện của vũ trụ ảo làm tăng bề mặt tấn công cho các đối tượng độc hại bằng cách tạo ra nhiều điểm xâm nhập hơn cho <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và các vụ <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "phần mềm độc hại (malware)"
      },
      {
        "id": "w2",
        "text": "rò rỉ dữ liệu (data breaches)"
      },
      {
        "id": "w3",
        "text": "tiền ảo (virtual money)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Quá trình số hóa và tích hợp Metaverse mang lại rủi ro lớn về an ninh mạng như malware và rò rỉ dữ liệu do tăng số lượng điểm xâm nhập.",
    "id": 44,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Hợp đồng thông minh (Smart Contracts) hoạt động trên công nghệ nào?",
    "options": [
      {
        "id": "a",
        "text": "Dữ liệu lớn (Big Data)"
      },
      {
        "id": "b",
        "text": "Chuỗi khối (Blockchain)"
      },
      {
        "id": "c",
        "text": "Máy chủ ngân hàng tập trung"
      },
      {
        "id": "d",
        "text": "Các hệ thống ERP truyền thống"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Hợp đồng thông minh là các đoạn mã chạy trên nền tảng Chuỗi khối (Blockchain) như Ethereum, tự động thực thi các thỏa thuận mà không cần bên trung gian.",
    "id": 45,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Sự kết hợp giữa Chuỗi khối và AI mang lại lợi ích gì trong tài chính?",
    "left": [
      {
        "id": "l1",
        "text": "Tính minh bạch từ Chuỗi khối"
      },
      {
        "id": "l2",
        "text": "Khả năng phân tích của AI"
      },
      {
        "id": "l3",
        "text": "Cố vấn rô-bốt (Robo-advisors)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Đảm bảo tất cả các bên có quyền truy cập vào một phiên bản thống nhất của sự thật (bất biến)"
      },
      {
        "id": "r2",
        "text": "Chủ động xác định các mối đe dọa tiềm ẩn (như gian lận) theo thời gian thực"
      },
      {
        "id": "r3",
        "text": "Đưa ra các đề xuất đầu tư được cá nhân hóa dựa trên phân tích dự đoán"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Blockchain bảo đảm dữ liệu. AI xử lý phân tích và phát hiện rủi ro. Cố vấn rô-bốt kết hợp AI để tự động hóa tư vấn đầu tư.",
    "id": 46,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Tại sao một số người cho rằng Bitcoin cần có các trung gian tài chính để phát triển thành một loại tiền tệ ổn định?",
    "options": [
      {
        "id": "a",
        "text": "Vì Blockchain không đủ bảo mật để lưu trữ Bitcoin"
      },
      {
        "id": "b",
        "text": "Vì cần trung gian để cho phép 'khám phá giá' (price discovery) và tạo quỹ hoán đổi danh mục (ETFs)"
      },
      {
        "id": "c",
        "text": "Vì chính phủ yêu cầu mọi người dân phải gửi Bitcoin vào ngân hàng"
      },
      {
        "id": "d",
        "text": "Vì Bitcoin có chi phí giao dịch quá đắt nếu không qua ngân hàng"
      }
    ],
    "correctAnswer": "b",
    "explanation": "John O. McGinnis lập luận rằng Bitcoin cần các cơ chế tài chính như ETF và sự 'khám phá giá' (do trung gian thực hiện) để có chiều sâu thị trường và ổn định hơn, dù nó được sinh ra để chống lại trung gian.",
    "id": 47,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình AI hỗ trợ quản lý thị trường NFT:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Thu thập dữ liệu xu hướng thị trường và sở thích của người mua"
      },
      {
        "id": "2",
        "text": "AI phân tích dữ liệu bằng các thuật toán tiên tiến"
      },
      {
        "id": "3",
        "text": "Đề xuất các tác phẩm nghệ thuật NFT phù hợp cho người mua tiềm năng"
      },
      {
        "id": "4",
        "text": "Đồng thời AI quét để phát hiện các vi phạm bản quyền hoặc bản sao (duplicates)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "AI vừa đóng vai trò như hệ thống đề xuất (tương tự Amazon/Netflix) cho NFT, vừa đóng vai trò kiểm duyệt (xác thực tính nguyên bản) trên thị trường.",
    "id": 48,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ vào định nghĩa về Ngân hàng ảo:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Ngân hàng ảo (virtual banking) khác biệt so với ngân hàng điện tử (electronic banking) ở chỗ nó không phụ thuộc vào bất kỳ <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> nào. Chúng cung cấp quy trình mở tài khoản nhanh chóng và tuân thủ các yêu cầu <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> thông qua công nghệ kỹ thuật số.",
    "words": [
      {
        "id": "w1",
        "text": "cơ sở hạ tầng vật lý (phòng giao dịch)"
      },
      {
        "id": "w2",
        "text": "KYC (Nhận biết khách hàng)"
      },
      {
        "id": "w3",
        "text": "thị trường chứng khoán"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Ngân hàng ảo hoạt động 100% online không cần chi nhánh vật lý, và sử dụng e-KYC để định danh khách hàng.",
    "id": 49,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Nhận định nào sau đây là ĐÚNG về Dữ liệu lớn (Big Data)?",
    "options": [
      {
        "id": "a",
        "text": "Dữ liệu lớn là một nhánh nhỏ của Khoa học dữ liệu."
      },
      {
        "id": "b",
        "text": "Dữ liệu lớn là lượng dữ liệu rất lớn mà các công cụ cơ sở dữ liệu truyền thống không thể quản lý và phân tích được."
      },
      {
        "id": "c",
        "text": "Dữ liệu lớn chỉ chứa dữ liệu ở dạng văn bản (text)."
      },
      {
        "id": "d",
        "text": "Chỉ các tập đoàn công nghệ mới được phép sở hữu Dữ liệu lớn."
      }
    ],
    "correctAnswer": "b",
    "explanation": "Big Data có khối lượng, tốc độ, độ đa dạng... vượt qua khả năng của các hệ thống cơ sở dữ liệu quan hệ truyền thống.",
    "id": 50,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép các quy định / chính sách với mục đích của nó trong hệ thống tài chính & blockchain:",
    "left": [
      {
        "id": "l1",
        "text": "AML (Anti-Money Laundering)"
      },
      {
        "id": "l2",
        "text": "KYC (Know Your Customer)"
      },
      {
        "id": "l3",
        "text": "GDPR (Quy định chung về Bảo vệ Dữ liệu)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Quy định chống rửa tiền, ngăn chặn việc hợp pháp hóa nguồn tiền bất hợp pháp"
      },
      {
        "id": "r2",
        "text": "Quy trình xác minh danh tính và đánh giá rủi ro của khách hàng"
      },
      {
        "id": "r3",
        "text": "Luật bảo vệ quyền riêng tư và dữ liệu cá nhân (điển hình tại Châu Âu)"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Các mô hình phát hiện gian lận dựa trên Blockchain/AI phải tuân thủ nghiêm ngặt AML, KYC và GDPR để đảm bảo minh bạch và tính pháp lý.",
    "id": 51,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Theo Michael Conklin, việc các doanh nghiệp đầu tư và chấp nhận tiền mã hóa như một phương thức thanh toán có thể vi phạm điều gì?",
    "options": [
      {
        "id": "a",
        "text": "Luật chống độc quyền của Hoa Kỳ"
      },
      {
        "id": "b",
        "text": "Lý thuyết các bên liên quan (stakeholder theory) của đạo đức doanh nghiệp"
      },
      {
        "id": "c",
        "text": "Luật bảo vệ môi trường do việc đào coin tiêu tốn nhiều năng lượng"
      },
      {
        "id": "d",
        "text": "Công ước Geneva về tiền tệ quốc tế"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Conklin cho rằng do tính biến động cao và các rủi ro khác, việc doanh nghiệp đầu tư tiền mã hóa là vi phạm lý thuyết các bên liên quan (bảo vệ lợi ích của cổ đông, nhân viên...) trong đạo đức doanh nghiệp.",
    "id": 52,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Dễ",
    "question": "Điền từ thích hợp nói về sự sáng tạo của AI và NFT:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Sự đổi mới xuất hiện khi triển khai các ý tưởng mới. Nếu <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> tự chủ tạo ra các tác phẩm nghệ thuật, điều này gây ra các tranh cãi liên quan đến quyền tác giả (authorship) và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> khi mã hóa thành NFT.",
    "words": [
      {
        "id": "w1",
        "text": "Trí tuệ nhân tạo (AI)"
      },
      {
        "id": "w2",
        "text": "bản quyền (copyright)"
      },
      {
        "id": "w3",
        "text": "thế chấp (collateral)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Khi AI tạo ra nghệ thuật, việc xác định ai sở hữu 'bản quyền' và 'quyền tác giả' trở nên phức tạp, nhất là khi chúng được thương mại hóa qua NFT.",
    "id": 53,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "ordering",
    "difficulty": "Khó",
    "question": "Sắp xếp quá trình tiến hóa của tiền tệ theo lịch sử (từ cũ đến mới) dựa trên tài liệu đọc:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Tiền kim loại / Tiền xu (Specie extraction)"
      },
      {
        "id": "2",
        "text": "Tiền giấy và sự quản lý cung tiền bằng chính sách tiền tệ của Ngân hàng trung ương"
      },
      {
        "id": "3",
        "text": "Chuyển tiền điện tử (Electronic money/banking)"
      },
      {
        "id": "4",
        "text": "Tiền mã hóa phi tập trung (Cryptocurrencies) và Tiền kỹ thuật số của NHTW (CBDC)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Lịch sử tiền tệ: Kim loại -> Giấy do Nhà nước quản lý -> Tiền điện tử (thẻ/app) -> Crypto (phi tập trung) và CBDC.",
    "id": 54,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Điều gì là RÀO CẢN lớn nhất đối với sự đổi mới có trách nhiệm trong hệ sinh thái tiền mã hóa hiện nay?",
    "options": [
      {
        "id": "a",
        "text": "Tốc độ internet quá chậm"
      },
      {
        "id": "b",
        "text": "Thiếu sự chắc chắn về mặt pháp lý (Legal uncertainty)"
      },
      {
        "id": "c",
        "text": "Không có đủ máy tính để đào coin"
      },
      {
        "id": "d",
        "text": "Sự phản đối của các nhà đầu tư bán lẻ"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Tài liệu nêu rõ: Việc thiếu sự chắc chắn về mặt pháp lý là một 'rào cản khổng lồ' đối với sự đổi mới có trách nhiệm trong hệ sinh thái tiền mã hóa.",
    "id": 55,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ với tính năng cốt lõi của chúng trong tài chính ảo:",
    "left": [
      {
        "id": "l1",
        "text": "Thực tế tăng cường (AR) / Thực tế ảo (VR)"
      },
      {
        "id": "l2",
        "text": "DeFi (Tài chính phi tập trung)"
      },
      {
        "id": "l3",
        "text": "NFTs (Non-Fungible Tokens)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Vật chất hóa không gian hiển thị và tương tác của Vũ trụ ảo (Metaverse)"
      },
      {
        "id": "r2",
        "text": "Cung cấp dịch vụ vay, cho vay không cần qua trung gian ngân hàng"
      },
      {
        "id": "r3",
        "text": "Đại diện chứng nhận tính sở hữu độc nhất cho các tài sản kỹ thuật số hoặc nghệ thuật"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "AR/VR tạo ra môi trường ảo (Metaverse). DeFi thay thế chức năng ngân hàng truyền thống. NFT đảm bảo tính độc nhất của tài sản kỹ thuật số.",
    "id": 56,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Tính năng nào KHÔNG phải là đặc điểm của công nghệ Chuỗi khối (Blockchain)?",
    "options": [
      {
        "id": "a",
        "text": "Phi tập trung (Decentralized)"
      },
      {
        "id": "b",
        "text": "Bảo mật bằng mật mã (Cryptographically secured)"
      },
      {
        "id": "c",
        "text": "Dữ liệu có thể dễ dàng bị chỉnh sửa bởi bất kỳ ai"
      },
      {
        "id": "d",
        "text": "Sổ cái công khai phân tán (Distributed public ledger)"
      }
    ],
    "correctAnswer": "c",
    "explanation": "Đặc trưng lớn nhất của Blockchain là tính bất biến; một khi dữ liệu được ghi lại, nó KHÔNG bị ảnh hưởng bởi việc sửa đổi.",
    "id": 57,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống về đặc tính của học sâu (Deep learning):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Các thuật toán học máy đôi khi gặp hạn chế vì hiệu suất phụ thuộc vào cách dữ liệu được chuẩn bị. <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> giải quyết vấn đề này bằng cách tự mình trích xuất thông tin, giúp cho việc học của máy tính trở nên mạnh mẽ, linh hoạt và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> hơn.",
    "words": [
      {
        "id": "w1",
        "text": "Học sâu (Deep Learning)"
      },
      {
        "id": "w2",
        "text": "trừu tượng (abstract)"
      },
      {
        "id": "w3",
        "text": "Cơ sở dữ liệu (Database)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Deep Learning tự động trích xuất các đặc trưng (features) từ dữ liệu thô, giúp quá trình nhận diện linh hoạt và trừu tượng hơn ML truyền thống.",
    "id": 58,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Trình tự tích hợp tài sản vật lý vào nền kinh tế kỹ thuật số DeFi:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Xác định tài sản thế giới thực (bất động sản, hàng xa xỉ)"
      },
      {
        "id": "2",
        "text": "Mã hóa (Tokenize) chứng thư sở hữu của tài sản thành NFT"
      },
      {
        "id": "3",
        "text": "Đưa NFT lên giao dịch hoặc làm tài sản thế chấp trong hệ sinh thái DeFi"
      },
      {
        "id": "4",
        "text": "Tăng cường tính thanh khoản và mở rộng cơ hội đầu tư cho tài sản đó"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Mã hóa tài sản thực (RWA - Real World Assets) bắt đầu từ việc chọn tài sản -> biến thành NFT -> thế chấp trên DeFi -> tạo thanh khoản.",
    "id": 59,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Việc sử dụng thuật toán (ví dụ GNN) để phát hiện gian lận tài chính trong Blockchain/AI cần đáp ứng điều kiện tiên quyết nào?",
    "options": [
      {
        "id": "a",
        "text": "Phải có nguồn dữ liệu bí mật từ hacker"
      },
      {
        "id": "b",
        "text": "Phải minh bạch, có thể kiểm toán được và tuân thủ các quy định về AML, KYC, GDPR"
      },
      {
        "id": "c",
        "text": "Chỉ hoạt động được với Bitcoin, không dùng cho các coin khác"
      },
      {
        "id": "d",
        "text": "Hệ thống phải tự động đóng băng tài khoản mà không cần con người xem xét"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Các mô hình phát hiện gian lận dựa trên GNN phải tuân thủ các quy định về AML, KYC và GDPR; điều này có nghĩa là hệ thống phải minh bạch và có thể kiểm toán.",
    "id": 60,
    "session": "Buổi 2: AI and Blockchain in Finance",
    "session_key": "Day02"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Mạng nơ-ron nhân tạo (ANNs) thường được sử dụng cho mục đích gì?",
    "options": [
      {
        "id": "a",
        "text": "Phân tích báo cáo tài chính thủ công"
      },
      {
        "id": "b",
        "text": "Nhận dạng mẫu (pattern recognition) như nhận dạng khuôn mặt và giọng nói"
      },
      {
        "id": "c",
        "text": "In ấn tài liệu"
      },
      {
        "id": "d",
        "text": "Chỉ dùng để gửi email tự động"
      }
    ],
    "correctAnswer": "b",
    "explanation": "ANNs thường được sử dụng cho nhận dạng mẫu như nhận dạng khuôn mặt trong hình ảnh và video, nhận dạng giọng nói, mạng xã hội, v.v.",
    "id": 61,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Sắp xếp quá trình hoạt động của Xử lý Ngôn ngữ Tự nhiên (NLP) khi Siri trả lời câu hỏi về thời tiết:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Người dùng đặt câu hỏi: 'Này Siri, thời tiết thế nào?'"
      },
      {
        "id": "2",
        "text": "NLU (Hiểu ngôn ngữ tự nhiên) giúp Siri hiểu yêu cầu của người dùng"
      },
      {
        "id": "3",
        "text": "Siri tìm kiếm thông tin thời tiết trên Internet"
      },
      {
        "id": "4",
        "text": "NLG (Tạo ngôn ngữ tự nhiên) chuyển dữ liệu thời tiết thành câu trả lời bằng giọng nói để phản hồi người dùng"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "NLP gồm hai phần: NLU (để máy tính hiểu người) và NLG (để máy tính nói lại cho người hiểu).",
    "id": 62,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép nối các khái niệm về xử lý dữ liệu và ngôn ngữ với định nghĩa của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "NLU (Hiểu ngôn ngữ tự nhiên)"
      },
      {
        "id": "l2",
        "text": "NLG (Tạo ngôn ngữ tự nhiên)"
      },
      {
        "id": "l3",
        "text": "Text mining (Khai phá văn bản)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Cho phép máy tính hiểu các hướng dẫn được cung cấp bằng ngôn ngữ của con người"
      },
      {
        "id": "r2",
        "text": "Chuyển đổi dữ liệu và kết quả thành mô tả bằng lời nói mà con người có thể hiểu được"
      },
      {
        "id": "r3",
        "text": "Trích xuất thông tin từ các nguồn văn bản phi cấu trúc (email, pdf) để khám phá mẫu/chủ đề"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "NLU là máy hiểu người, NLG là máy giao tiếp với người, Text mining là trích xuất insight từ tài liệu văn bản.",
    "id": 63,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ thích hợp nói về sự khác biệt giữa Khai phá dữ liệu và Học máy (theo Bernard Marr):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Khai phá dữ liệu tìm kiếm các mẫu đã tồn tại trong <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, trong khi học máy cố gắng dự đoán các kết quả trong tương lai. Khai phá dữ liệu dựa vào sự can thiệp của <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> trong suốt quá trình, trong khi phần lớn quá trình học tập với học máy là tự động.",
    "words": [
      {
        "id": "w1",
        "text": "dữ liệu lịch sử (historical data)"
      },
      {
        "id": "w2",
        "text": "con người"
      },
      {
        "id": "w3",
        "text": "thuật toán"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Khai phá dữ liệu phân tích dữ liệu lịch sử và cần nhiều sự can thiệp phân tích của con người hơn học máy tự động.",
    "id": 64,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Nhà nghiên cứu Sophia Sun (2019) đã thúc đẩy việc sử dụng học sâu (DL) trong kiểm toán vào 2 lĩnh vực chính nào?",
    "options": [
      {
        "id": "a",
        "text": "Kiểm kê kho bãi và tính lương"
      },
      {
        "id": "b",
        "text": "Xác định thông tin (từ dữ liệu văn bản, hình ảnh, âm thanh) và hỗ trợ đánh giá (ra quyết định)"
      },
      {
        "id": "c",
        "text": "Thiết kế website và quảng cáo trên mạng xã hội"
      },
      {
        "id": "d",
        "text": "Tự động hóa hoàn toàn việc sa thải nhân viên"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Sun (2019) thúc đẩy việc sử dụng học sâu để hỗ trợ ra quyết định kiểm toán trong hai lĩnh vực chính: xác định thông tin và hỗ trợ đánh giá.",
    "id": 65,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "RPA (Tự động hóa quy trình bằng robot) rất phù hợp với loại công việc nào?",
    "options": [
      {
        "id": "a",
        "text": "Các công việc mang tính sáng tạo cao, thay đổi liên tục"
      },
      {
        "id": "b",
        "text": "Các tác vụ có khối lượng lớn, lặp đi lặp lại thường do con người thực hiện (vd: đối chiếu ngân hàng, xử lý hóa đơn)"
      },
      {
        "id": "c",
        "text": "Các công việc cần sự đồng cảm và thấu hiểu tâm lý khách hàng"
      },
      {
        "id": "d",
        "text": "Khám phá các mô hình dữ liệu chưa từng được biết đến"
      }
    ],
    "correctAnswer": "b",
    "explanation": "RPA là một ứng dụng phần mềm tự động hóa các quy trình kinh doanh bằng cách lặp lại các hành động của con người, rất phù hợp cho các tác vụ lặp đi lặp lại.",
    "id": 66,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công cụ / nền tảng với chức năng / đặc điểm của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "TPU (Bộ xử lý tensor)"
      },
      {
        "id": "l2",
        "text": "API (Giao diện lập trình ứng dụng)"
      },
      {
        "id": "l3",
        "text": "UiPath, Automation Anywhere"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Mạch chuyên dụng do Google phát triển để tăng tốc độ xử lý cho ứng dụng AI/ML"
      },
      {
        "id": "r2",
        "text": "Đóng vai trò như 'người đưa tin', cho phép các phần mềm và nền tảng khác nhau giao tiếp với nhau"
      },
      {
        "id": "r3",
        "text": "Các nhà cung cấp phần mềm hàng đầu trong lĩnh vực tự động hóa RPA"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "TPU tăng tốc AI. API kết nối phần mềm. UiPath là phần mềm RPA phổ biến.",
    "id": 67,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "ordering",
    "difficulty": "Khó",
    "question": "Sắp xếp quy trình khai phá văn bản (Text mining) được mô tả trong tài liệu:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Thu thập các nguồn văn bản phi cấu trúc (ví dụ: hợp đồng, email, bài đăng MXH)"
      },
      {
        "id": "2",
        "text": "Áp đặt cấu trúc (structure) lên các nguồn dữ liệu văn bản phi cấu trúc này"
      },
      {
        "id": "3",
        "text": "Sử dụng các kỹ thuật khai phá dữ liệu để trích xuất thông tin liên quan (khái niệm, mẫu, xu hướng)"
      },
      {
        "id": "4",
        "text": "Ứng dụng thông tin đó (vd: phát hiện từ ngữ buộc tội trong kế toán pháp y)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Quá trình 2 bước: 1. Áp đặt cấu trúc lên văn bản, 2. Sử dụng kỹ thuật khai phá để trích xuất thông tin, sau đó là ứng dụng.",
    "id": 68,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Dễ",
    "question": "Điền từ thích hợp liên quan đến ngôn ngữ lập trình cho kế toán viên:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Sự thành thạo các công cụ lập trình mã nguồn mở (open-source) phổ biến cho AI, chẳng hạn như <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>, sẽ cho phép các kế toán viên tùy chỉnh các ứng dụng AI.",
    "words": [
      {
        "id": "w1",
        "text": "Python"
      },
      {
        "id": "w2",
        "text": "R"
      },
      {
        "id": "w3",
        "text": "HTML"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Python và R là 2 ngôn ngữ phổ biến nhất được khuyên học cho Data Science và AI.",
    "id": 69,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Sự kiện thị trường 'Sự cố chớp nhoáng' (flash crash) ngày 6 tháng 5 năm 2010 đã làm giảm 1000 điểm Dow Jones trong vài phút được cho là do đâu?",
    "options": [
      {
        "id": "a",
        "text": "Do sự sụp đổ của một ngân hàng ảo trên Metaverse"
      },
      {
        "id": "b",
        "text": "Do giao dịch thuật toán tần suất cao (Algorithmic trading) gây thao túng và mất ổn định thị trường"
      },
      {
        "id": "c",
        "text": "Do rò rỉ dữ liệu của Equifax"
      },
      {
        "id": "d",
        "text": "Do một chatbot AI tư vấn sai cho khách hàng"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Giao dịch thuật toán tần suất cao đã kích hoạt đợt bán tháo tự động dây chuyền, gây ra flash crash.",
    "id": 70,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Trong trường hợp của Ngân hàng HDFC, việc sử dụng học máy để chấm điểm tín dụng đã làm dấy lên vấn đề đạo đức nào lớn nhất?",
    "options": [
      {
        "id": "a",
        "text": "Quyền riêng tư dữ liệu"
      },
      {
        "id": "b",
        "text": "Thao túng thị trường"
      },
      {
        "id": "c",
        "text": "Sự thiên vị (biases) dẫn đến phân biệt đối xử trong các lựa chọn cho vay"
      },
      {
        "id": "d",
        "text": "Mất việc làm của nhân viên ngân hàng"
      }
    ],
    "correctAnswer": "c",
    "explanation": "Nghiên cứu chỉ ra rằng các đánh giá của thuật toán AI chấm điểm tín dụng đôi khi bị thiên vị, gây ra sự phân biệt đối xử khi cấp khoản vay.",
    "id": 71,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép tên các doanh nghiệp/tổ chức với vấn đề hoặc công nghệ cốt lõi mà họ gặp phải (trong Case Study):",
    "left": [
      {
        "id": "l1",
        "text": "Ngân hàng ICICI"
      },
      {
        "id": "l2",
        "text": "Paytm"
      },
      {
        "id": "l3",
        "text": "Aditya Birla Capital"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Sử dụng chatbot AI (iPal) làm dấy lên các lo ngại về quyền riêng tư và bảo mật thông tin khách hàng"
      },
      {
        "id": "r2",
        "text": "Cung cấp nền tảng giao dịch thuật toán (Algorithmic trading) gây lo ngại về tính công bằng và thao túng thị trường"
      },
      {
        "id": "r3",
        "text": "Sử dụng NLP để tư vấn đầu tư cá nhân hóa, đồng thời đối mặt với nhu cầu bảo vệ dữ liệu tài chính nhạy cảm"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "ICICI liên quan đến chatbot iPal. Paytm liên quan giao dịch thuật toán. Aditya Birla liên quan tư vấn đầu tư bằng NLP.",
    "id": 72,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Sắp xếp theo thứ tự mức độ can thiệp vào ngôn ngữ tự nhiên từ thấp đến cao (từ đọc dữ liệu thô đến tạo ra phản hồi):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Dữ liệu văn bản phi cấu trúc (Unstructured Text Data)"
      },
      {
        "id": "2",
        "text": "Phân tích ngữ nghĩa và khai phá văn bản (Text mining)"
      },
      {
        "id": "3",
        "text": "Hiểu ngôn ngữ tự nhiên (NLU) - Máy hiểu ý định"
      },
      {
        "id": "4",
        "text": "Tạo ngôn ngữ tự nhiên (NLG) - Máy tự động phát sinh câu trả lời"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Quy trình bắt đầu từ văn bản thô -> Trích xuất dữ liệu cơ bản -> Hiểu ngữ nghĩa chuyên sâu (NLU) -> Sinh ra văn bản phản hồi mới (NLG).",
    "id": 73,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Khó",
    "question": "Điền từ vào chỗ trống liên quan đến rủi ro của AI Tạo sinh trong tài chính:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Sự phát triển nhanh chóng của AI thường vượt qua khả năng của nhà quản lý trong việc thiết lập <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, dẫn đến những khoảng trống trong tuân thủ. Hơn nữa, việc tự động hóa có thể dẫn đến <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> và bất bình đẳng kinh tế.",
    "words": [
      {
        "id": "w1",
        "text": "khuôn khổ pháp lý (legal frameworks)"
      },
      {
        "id": "w2",
        "text": "mất việc làm (job displacement)"
      },
      {
        "id": "w3",
        "text": "thuật toán"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Tài liệu nhắc đến 2 rủi ro: sự chậm trễ của luật pháp (Regulatory Compliance gap) và mất việc làm (Job displacement) do tự động hóa.",
    "id": 74,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Để xử lý dữ liệu có cấu trúc (structured data) trong một hệ thống ERP nhằm phát hiện gian lận giao dịch, kế toán viên nên sử dụng công nghệ nào sau đây là trực tiếp nhất?",
    "options": [
      {
        "id": "a",
        "text": "Khai phá văn bản (Text Mining)"
      },
      {
        "id": "b",
        "text": "Khai phá dữ liệu (Data Mining)"
      },
      {
        "id": "c",
        "text": "Thực tế ảo (VR)"
      },
      {
        "id": "d",
        "text": "Tạo ngôn ngữ tự nhiên (NLG)"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Khai phá dữ liệu (Data Mining) rất phù hợp cho dữ liệu có cấu trúc từ hệ thống ERP/Sổ cái chung để tìm kiếm các mẫu và ngoại lai.",
    "id": 75,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ AI với một ứng dụng thực tiễn trong kế toán/tài chính:",
    "left": [
      {
        "id": "l1",
        "text": "Học sâu (Deep Learning)"
      },
      {
        "id": "l2",
        "text": "Khai phá văn bản (Text mining)"
      },
      {
        "id": "l3",
        "text": "RPA (Tự động hóa robot)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Tái tạo lại các tài liệu quét kém chất lượng bằng nhận dạng quang học (như EY đang làm)"
      },
      {
        "id": "r2",
        "text": "Tìm kiếm từ ngữ mang tính buộc tội trong hàng ngàn email để phục vụ kiểm toán pháp y"
      },
      {
        "id": "r3",
        "text": "Tự động đăng nhập vào phần mềm và đối chiếu sao kê ngân hàng hàng ngày"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "DL chuyên xử lý ảnh/nhận dạng. Text mining xử lý văn bản/email. RPA xử lý thao tác tự động trên giao diện.",
    "id": 76,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Theo báo cáo, công cụ lập trình nào giúp thao tác trực tiếp với cơ sở dữ liệu rất hữu ích cho các ứng dụng AI?",
    "options": [
      {
        "id": "a",
        "text": "HTML và CSS"
      },
      {
        "id": "b",
        "text": "SQL và NoSQL"
      },
      {
        "id": "c",
        "text": "Photoshop"
      },
      {
        "id": "d",
        "text": "Excel VBA"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Tài liệu ghi rõ: Các công cụ khác, chẳng hạn như SQL và NoSQL, sẽ hữu ích cho việc truy xuất, chỉnh sửa và thao tác dữ liệu để sử dụng cho ứng dụng AI.",
    "id": 77,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình tích hợp API của Google Prediction vào một hệ thống phần mềm doanh nghiệp:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Phần mềm doanh nghiệp thu thập dữ liệu giao dịch"
      },
      {
        "id": "2",
        "text": "Gửi dữ liệu thông qua API (người đưa tin kỹ thuật số) lên đám mây"
      },
      {
        "id": "3",
        "text": "Google Prediction API sử dụng Học máy để phân tích và đưa ra dự đoán"
      },
      {
        "id": "4",
        "text": "API trả kết quả phân tích về lại phần mềm doanh nghiệp để kế toán viên xem"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "API hoạt động như một cầu nối nhận dữ liệu, gửi tới service xử lý, và trả kết quả về.",
    "id": 78,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống liên quan đến việc lập hồ sơ khách hàng (Customer profiling):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Các tổ chức tài chính sử dụng AI để lập hồ sơ khách hàng nhằm mục đích tiếp thị nhắm mục tiêu. Tuy nhiên, các nhà bán lẻ có thể lạm dụng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để xác định những người tiêu dùng yếu thế, từ đó lợi dụng lỗ hổng tài chính của họ bằng các phương thức bán hàng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "phân tích dự đoán (predictive analytics)"
      },
      {
        "id": "w2",
        "text": "hung hăng (aggressive)"
      },
      {
        "id": "w3",
        "text": "bảo vệ môi trường"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Việc lạm dụng predictive analytics để đưa ra các đề xuất bán hàng hung hăng là một rủi ro đạo đức lớn.",
    "id": 79,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Vụ vi phạm dữ liệu của Equifax năm 2017 là một ví dụ điển hình cảnh báo rủi ro gì trong việc áp dụng AI vào tài chính?",
    "options": [
      {
        "id": "a",
        "text": "AI không thể hoạt động trên điện thoại di động"
      },
      {
        "id": "b",
        "text": "Nguy cơ về bảo mật và quyền riêng tư dữ liệu (Data Privacy) khi thu thập lượng lớn thông tin cá nhân"
      },
      {
        "id": "c",
        "text": "Chi phí điện năng quá cao để chạy mô hình AI"
      },
      {
        "id": "d",
        "text": "Sự thiên vị trong cấp tín dụng"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Equifax là case study về Data Privacy, nơi hàng triệu dữ liệu bị lộ, nhấn mạnh tầm quan trọng của an ninh mạng.",
    "id": 80,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép các khái niệm/hiện tượng trong AI Đạo đức với ý nghĩa thực tiễn của nó:",
    "left": [
      {
        "id": "l1",
        "text": "Thiên kiến thuật toán (Biases)"
      },
      {
        "id": "l2",
        "text": "Tính không rõ ràng về trách nhiệm (Accountability opacity)"
      },
      {
        "id": "l3",
        "text": "Bảo vệ người tiêu dùng (Consumer protection)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Rủi ro khi hệ thống AI từ chối khoản vay dựa trên dữ liệu lịch sử mang tính phân biệt đối xử"
      },
      {
        "id": "r2",
        "text": "Khó khăn trong việc xác định ai (lập trình viên, ngân hàng hay AI) chịu trách nhiệm khi AI gây ra thiệt hại"
      },
      {
        "id": "r3",
        "text": "Ngăn chặn các thủ thuật tiếp thị và bán hàng lợi dụng lỗ hổng tâm lý/tài chính của khách hàng"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Biases = thiên vị phân biệt đối xử. Opacity = hộp đen/khó quy trách nhiệm. Protection = bảo vệ khách hàng khỏi bị thao túng.",
    "id": 81,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Theo giáo sư Aldhizer (2017), kỹ thuật Trích xuất Khái niệm (Concept Extraction) dùng trong kiểm toán pháp y chủ yếu để làm gì?",
    "options": [
      {
        "id": "a",
        "text": "Trích xuất số liệu bảng cân đối kế toán từ file Excel"
      },
      {
        "id": "b",
        "text": "Xác định các từ ngữ hoặc đoạn văn mang tính buộc tội (incriminating words) từ email và mạng xã hội"
      },
      {
        "id": "c",
        "text": "Khởi tạo hợp đồng thông minh trên Blockchain"
      },
      {
        "id": "d",
        "text": "Chấm điểm tín dụng cho doanh nghiệp"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Concept extraction (một phần của text mining) được dùng trong pháp y kế toán để tìm từ ngữ buộc tội từ email, tin nhắn...",
    "id": 82,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Dễ",
    "question": "Điền từ vào chỗ trống liên quan đến học sâu:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Mạng nơ-ron nhân tạo (ANNs) được lấy cảm hứng từ <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> của con người, phân tích khối lượng dữ liệu lớn để <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "mạng nơ-ron sinh học"
      },
      {
        "id": "w2",
        "text": "tự học (self-learn)"
      },
      {
        "id": "w3",
        "text": "chiếc máy tính"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "ANN lấy cảm hứng từ cấu trúc não người (nơ-ron sinh học) để cho phép máy tính tự học từ dữ liệu.",
    "id": 83,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "ordering",
    "difficulty": "Khó",
    "question": "Sắp xếp quy trình giải quyết vấn đề bằng AI theo mô hình đề xuất để đảm bảo tính đạo đức:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Thiết kế hệ thống AI và thu thập dữ liệu đại diện, tránh thiên vị (bias)"
      },
      {
        "id": "2",
        "text": "Triển khai thuật toán với sự minh bạch (transparency) và khả năng giải thích (explainability)"
      },
      {
        "id": "3",
        "text": "Áp dụng vào thực tế (như chấm điểm tín dụng) với sự giám sát liên tục (constant monitoring)"
      },
      {
        "id": "4",
        "text": "Thực hiện kiểm toán định kỳ (frequent audits) bởi bên thứ ba hoặc cơ quan quản lý"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Phát triển AI đạo đức cần: Thu thập dữ liệu sạch -> Thiết kế minh bạch -> Giám sát liên tục -> Kiểm toán định kỳ.",
    "id": 84,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Ứng dụng nào sau đây là kết quả của NLG (Tạo ngôn ngữ tự nhiên)?",
    "options": [
      {
        "id": "a",
        "text": "Siri ghi nhận giọng nói của người dùng thành văn bản"
      },
      {
        "id": "b",
        "text": "Máy tính đọc một hóa đơn PDF và lấy ra số tiền"
      },
      {
        "id": "c",
        "text": "Hệ thống tự động chuyển biểu đồ doanh thu thành một đoạn văn bản tóm tắt tình hình tài chính cho sếp đọc"
      },
      {
        "id": "d",
        "text": "Tìm kiếm các khoản vay rủi ro trong cơ sở dữ liệu SQL"
      }
    ],
    "correctAnswer": "c",
    "explanation": "NLG có thể chuyển đổi các hình ảnh hóa dữ liệu như biểu đồ thành mô tả bằng lời nói/văn bản mà con người đọc được.",
    "id": 85,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công cụ / ứng dụng với lĩnh vực tương ứng của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "Python, R"
      },
      {
        "id": "l2",
        "text": "Google Prediction, BigML, Anaconda"
      },
      {
        "id": "l3",
        "text": "ACL, IDEA"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Ngôn ngữ lập trình mã nguồn mở tốt nhất cho khoa học dữ liệu"
      },
      {
        "id": "r2",
        "text": "Các dịch vụ nền tảng hoặc API hỗ trợ triển khai Học máy (ML)"
      },
      {
        "id": "r3",
        "text": "Phần mềm phân tích dữ liệu kiểm toán chuyên nghiệp truyền thống"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Python/R là ngôn ngữ lập trình; Google/BigML cung cấp API/Nền tảng ML; ACL/IDEA là phần mềm kiểm toán.",
    "id": 86,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Theo tài liệu, tại sao các ngân hàng và công ty tài chính cần hợp lực với các cơ quan quản lý trong việc sử dụng AI?",
    "options": [
      {
        "id": "a",
        "text": "Để tăng lợi nhuận và thao túng thị trường dễ hơn"
      },
      {
        "id": "b",
        "text": "Để bảo vệ tính toàn vẹn của thị trường, bảo vệ quyền lợi người tiêu dùng và đảm bảo tuân thủ pháp luật"
      },
      {
        "id": "c",
        "text": "Để độc quyền công nghệ AI"
      },
      {
        "id": "d",
        "text": "Để ngừng sử dụng AI và quay về làm thủ công"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Sự hợp lực là để tận dụng AI trong khi vẫn bảo vệ sự toàn vẹn, đạo đức và tuân thủ quy định.",
    "id": 87,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống về Xử lý ngôn ngữ tự nhiên (NLP) trong kế toán:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Tiềm năng của NLP trong kế toán rất lớn. Nó được sử dụng để phân tích các văn bản liên quan đến hiệu quả tài chính và sự tuân thủ quy định. Các ứng dụng của NLP bao gồm phân tích <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, phân loại văn bản, và <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> văn bản.",
    "words": [
      {
        "id": "w1",
        "text": "ngữ nghĩa (semantics)"
      },
      {
        "id": "w2",
        "text": "tóm tắt (summarization)"
      },
      {
        "id": "w3",
        "text": "chuỗi khối"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "NLP trong kế toán giúp phân tích ngữ nghĩa, phân loại và tóm tắt các tài liệu, hợp đồng, báo cáo.",
    "id": 88,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Quy trình ứng dụng Học sâu (Deep Learning) vào hệ thống tự động theo nghiên cứu:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Thu thập khối lượng lớn dữ liệu đầu vào (hình ảnh, giọng nói, tài liệu quét)"
      },
      {
        "id": "2",
        "text": "Dữ liệu được đưa qua các lớp của Mạng nơ-ron nhân tạo (ANNs)"
      },
      {
        "id": "3",
        "text": "Thuật toán tự khám phá ra các mô hình (patterns) mà không cần con người lập trình quy tắc tĩnh"
      },
      {
        "id": "4",
        "text": "Đưa ra dự đoán hoặc nhận dạng chính xác (vd: phát hiện hóa đơn giả)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "DL dựa vào việc đẩy dữ liệu qua mạng ANN để máy tự học cấu trúc (tự khám phá pattern) và đưa ra kết quả.",
    "id": 89,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Hệ thống AI tài chính yêu cầu quyền truy cập vào lượng lớn dữ liệu (hồ sơ giao dịch, điểm tín dụng). Điều này đặt ra yêu cầu CẤP BÁCH nào nhất về mặt đạo đức/pháp luật?",
    "options": [
      {
        "id": "a",
        "text": "Yêu cầu phải sử dụng bộ xử lý TPU"
      },
      {
        "id": "b",
        "text": "Yêu cầu thiết lập luật bảo vệ dữ liệu mạnh mẽ để bảo mật quyền riêng tư (Data Privacy)"
      },
      {
        "id": "c",
        "text": "Yêu cầu phải in toàn bộ dữ liệu ra giấy"
      },
      {
        "id": "d",
        "text": "Yêu cầu AI phải tự động giao dịch thay con người"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Quyền truy cập dữ liệu lớn đi liền với rủi ro bảo mật, đòi hỏi luật bảo vệ dữ liệu (privacy laws) nghiêm ngặt.",
    "id": 90,
    "session": "Buổi 3: Python for Finance & Data Science",
    "session_key": "Day03"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Khái niệm STP trong tiếp thị là viết tắt của các từ nào?",
    "options": [
      {
        "id": "a",
        "text": "Segmentation, Targeting, Positioning"
      },
      {
        "id": "b",
        "text": "Sales, Technology, Pricing strategies"
      },
      {
        "id": "c",
        "text": "Systems, Tracking, Performance measures"
      },
      {
        "id": "d",
        "text": "Standardization, Trading, Profitability"
      }
    ],
    "correctAnswer": "a",
    "explanation": "STP là viết tắt của Phân khúc (Segmentation), Nhắm mục tiêu (Targeting), Định vị (Positioning).",
    "id": 91,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong học không giám sát (unsupervised learning), tại sao chúng ta sử dụng thuật toán phân cụm?",
    "options": [
      {
        "id": "a",
        "text": "Để tính toán lợi nhuận và doanh thu"
      },
      {
        "id": "b",
        "text": "Để huấn luyện mô hình dự báo phá sản"
      },
      {
        "id": "c",
        "text": "Do dữ liệu không có nhãn kết quả (unlabeled)"
      },
      {
        "id": "d",
        "text": "Do cần một phương pháp hồi quy tuyến tính"
      }
    ],
    "correctAnswer": "c",
    "explanation": "Phân cụm được sử dụng trong học không giám sát vì dữ liệu không có nhãn (unlabeled data).",
    "id": 92,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "matching",
    "difficulty": "Dễ",
    "question": "Ghép các khái niệm phân khúc với định nghĩa tương ứng:",
    "left": [
      {
        "id": "l1",
        "text": "Phân khúc động (Dynamic Segmentation)"
      },
      {
        "id": "l2",
        "text": "Vi phân khúc (Microsegments)"
      },
      {
        "id": "l3",
        "text": "Tiếp thị đại chúng (Mass marketing)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Liên tục cập nhật phân khúc vì sở thích khách hàng luôn thay đổi"
      },
      {
        "id": "r2",
        "text": "Phân khúc siêu nhỏ hướng tới cá nhân hóa (hyperpersonalization)"
      },
      {
        "id": "r3",
        "text": "Giả định tất cả khách hàng đều giống nhau và gửi chung một thông điệp"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Dynamic = cập nhật liên tục. Micro = cá nhân hóa siêu nhỏ. Mass = đại trà.",
    "id": 93,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp các bước cơ bản của thuật toán k-Means:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Xác định số lượng cụm (k)"
      },
      {
        "id": "2",
        "text": "Khởi tạo ngẫu nhiên các trung tâm cụm (centroids)"
      },
      {
        "id": "3",
        "text": "Gán mỗi điểm dữ liệu cho trung tâm cụm gần nhất"
      },
      {
        "id": "4",
        "text": "Tính toán lại trung tâm và lặp lại cho đến khi hội tụ"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Quy trình k-Means: Chọn k -> Khởi tạo -> Gán điểm -> Cập nhật trung tâm (lặp lại).",
    "id": 94,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ thích hợp so sánh giữa k-Means và k-Medoid:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Thay vì sử dụng giá trị trung bình như k-Means, k-Medoid sử dụng một <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> làm trung tâm. Điều này giúp thuật toán chống <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> tốt hơn k-Means.",
    "words": [
      {
        "id": "w1",
        "text": "điểm dữ liệu thực tế (medoid)"
      },
      {
        "id": "w2",
        "text": "nhiễu ngoại lai (outliers)"
      },
      {
        "id": "w3",
        "text": "giá trị giả định"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "k-Medoid lấy một điểm thực tế làm tâm, giúp nó bền vững hơn trước các giá trị ngoại lai (outliers).",
    "id": 95,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Lệnh `scale(df, center = TRUE, scale = TRUE)` trong R nhằm mục đích gì?",
    "options": [
      {
        "id": "a",
        "text": "Chuyển dữ liệu thành dạng số nguyên (integer)"
      },
      {
        "id": "b",
        "text": "Lọc các giá trị trống (NA) ra khỏi dữ liệu"
      },
      {
        "id": "c",
        "text": "Vẽ biểu đồ các trung tâm cụm ngẫu nhiên"
      },
      {
        "id": "d",
        "text": "Chuyển đổi các biến về cùng thang đo (điểm Z)"
      }
    ],
    "correctAnswer": "d",
    "explanation": "Căn giữa và chia tỷ lệ giúp chuyển giá trị về điểm Z, khắc phục sự khác biệt thang đo giữa các biến.",
    "id": 96,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Đa cộng tuyến (Multicollinearity) xảy ra khi nào trong mô hình dự báo?",
    "options": [
      {
        "id": "a",
        "text": "Khi tất cả các biến đều độc lập với nhau"
      },
      {
        "id": "b",
        "text": "Khi có nhiều biến độc lập tương quan mạnh"
      },
      {
        "id": "c",
        "text": "Khi dữ liệu bị thiếu hụt"
      },
      {
        "id": "d",
        "text": "Khi không thể xác định được biến phụ thuộc"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Đa cộng tuyến (Multicollinearity) xảy ra khi có sự tương quan mạnh giữa nhiều biến độc lập.",
    "id": 97,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép nối các tham số trong R với chức năng của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "centers trong kmeans()"
      },
      {
        "id": "l2",
        "text": "nstart trong kmeans()"
      },
      {
        "id": "l3",
        "text": "repel = TRUE trong fviz_cluster()"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Chỉ định số lượng cụm cần phân chia"
      },
      {
        "id": "r2",
        "text": "Đặt số lượng điểm khởi tạo ngẫu nhiên ban đầu"
      },
      {
        "id": "r3",
        "text": "Ngăn các nhãn của điểm dữ liệu đè lên nhau trên biểu đồ"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "centers = k (số cụm); nstart = số lần lặp random ban đầu; repel=TRUE = tránh text overlap.",
    "id": 98,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ vào chỗ trống về mô hình hồi quy:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Để khắc phục Đa cộng tuyến và tự động loại bỏ biến không cần thiết, người ta dùng Hồi quy <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, tiêu biểu là mô hình <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "có phạt (Penalized)"
      },
      {
        "id": "w2",
        "text": "LASSO"
      },
      {
        "id": "w3",
        "text": "tuyến tính (Linear)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Hồi quy có phạt (Penalized regression), đặc biệt là LASSO, giúp lựa chọn đặc trưng và giải quyết đa cộng tuyến.",
    "id": 99,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "ordering",
    "difficulty": "Khó",
    "question": "Sắp xếp các bước đánh giá sức khỏe tài chính bằng LASSO:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Thu thập dữ liệu các chỉ số tài chính (ratios) của các công ty (cả phá sản và không phá sản)"
      },
      {
        "id": "2",
        "text": "Kiểm tra sự tương quan (Biểu đồ tương quan) và VIF"
      },
      {
        "id": "3",
        "text": "Chạy mô hình LASSO để tự động loại bỏ các biến có đa cộng tuyến (thu gọn hệ số về 0)"
      },
      {
        "id": "4",
        "text": "Đánh giá khả năng dự đoán của mô hình bằng đường cong AUC ROC"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Quy trình: Chuẩn bị dữ liệu -> Kiểm tra tương quan -> Huấn luyện LASSO (lọc biến) -> Đánh giá (AUC ROC).",
    "id": 100,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Đường cong AUC ROC biểu diễn mối quan hệ giữa hai yếu tố nào?",
    "options": [
      {
        "id": "a",
        "text": "Dương tính giả (X) và Dương tính thật (Y)"
      },
      {
        "id": "b",
        "text": "Khoảng cách Euclide (X) và Tâm cụm (Y)"
      },
      {
        "id": "c",
        "text": "Chi phí (X) và Doanh thu (Y)"
      },
      {
        "id": "d",
        "text": "Thời gian mua sắm (X) và Số tiền chi tiêu (Y)"
      }
    ],
    "correctAnswer": "a",
    "explanation": "AUC ROC biểu diễn False Positives (trục x) và True Positives (trục y).",
    "id": 101,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Thuật ngữ 'Vốn cổ phần tư nhân' (Private equity) trong tài liệu thường đầu tư vào dạng doanh nghiệp nào?",
    "options": [
      {
        "id": "a",
        "text": "Chỉ đầu tư vào tập đoàn công nghệ"
      },
      {
        "id": "b",
        "text": "Doanh nghiệp có tiềm năng lớn nhưng đang khó khăn tài chính"
      },
      {
        "id": "c",
        "text": "Chỉ đầu tư vào ngân hàng trung ương"
      },
      {
        "id": "d",
        "text": "Doanh nghiệp hoàn toàn không có khoản nợ nào"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Công ty cổ phần tư nhân đầu tư vào doanh nghiệp có tiềm năng chưa hiện thực hóa nhưng đang gặp khó khăn (nợ cao).",
    "id": 102,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công thức chỉ số tài chính (Financial Ratios) với tên của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "Current Ratio (Tỷ lệ thanh toán hiện hành)"
      },
      {
        "id": "l2",
        "text": "Debt-Equity Ratio (Tỷ lệ nợ trên vốn CSH)"
      },
      {
        "id": "l3",
        "text": "Operating Ratio (Tỷ lệ hoạt động)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Tài sản lưu động / Nợ ngắn hạn"
      },
      {
        "id": "r2",
        "text": "Giá trị sổ sách của vốn chủ sở hữu / Tổng nợ phải trả"
      },
      {
        "id": "r3",
        "text": "Tổng chi phí / Tổng doanh thu"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Dựa vào công thức trong mục 10.5.1 và bộ dữ liệu.",
    "id": 103,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Khó",
    "question": "Điền từ liên quan đến cách hoạt động của glmnet (mô hình LASSO):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Mô hình LASSO đã thu hẹp các tham số beta của một số biến về <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, do đó giúp <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> từ 16 biến ban đầu xuống số lượng ít hơn.",
    "words": [
      {
        "id": "w1",
        "text": "0 (không)"
      },
      {
        "id": "w2",
        "text": "lựa chọn đặc trưng (feature selection)"
      },
      {
        "id": "w3",
        "text": "gia tăng (increase)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "LASSO giải quyết đa cộng tuyến bằng cách đẩy hệ số của các biến kém quan trọng về 0, giúp chọn lọc đặc trưng.",
    "id": 104,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Thứ tự xử lý dữ liệu trước khi phân cụm (Cluster Analysis):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Đọc dữ liệu thô (vd: số tiền, thời gian mua sắm)"
      },
      {
        "id": "2",
        "text": "Trừ giá trị trung bình (center = TRUE)"
      },
      {
        "id": "3",
        "text": "Chia cho độ lệch chuẩn (scale = TRUE)"
      },
      {
        "id": "4",
        "text": "Sử dụng dữ liệu điểm Z (Z-scores) để chạy k-Means"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Quy trình: Đọc dữ liệu -> Căn giữa (trừ mean) -> Chia tỷ lệ (chia std dev) -> Chạy phân cụm.",
    "id": 105,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Điều kiện cần thiết của dữ liệu khi truyền vào hàm glmnet() để chạy LASSO trong R là gì?",
    "options": [
      {
        "id": "a",
        "text": "Dữ liệu phải có định dạng văn bản (text)"
      },
      {
        "id": "b",
        "text": "Dữ liệu phải ở dạng ma trận (matrix)"
      },
      {
        "id": "c",
        "text": "Dữ liệu phải là danh sách liên kết"
      },
      {
        "id": "d",
        "text": "Dữ liệu không được chứa số thập phân"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Tài liệu ghi rõ: Vì đối với glmnet, dữ liệu phải ở dạng ma trận, chúng ta chuyển đổi nó thành một ma trận...",
    "id": 106,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "matching",
    "difficulty": "Dễ",
    "question": "Ghép các bộ phận/tổ chức với vai trò sử dụng Dự báo sức khỏe tài chính:",
    "left": [
      {
        "id": "l1",
        "text": "Người cho vay (Ngân hàng)"
      },
      {
        "id": "l2",
        "text": "Ban quản lý (Doanh nghiệp)"
      },
      {
        "id": "l3",
        "text": "Nhà đầu tư (Cổ phần tư nhân)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Quyết định có nên cấp tín dụng hay không"
      },
      {
        "id": "r2",
        "text": "Lập kế hoạch chiến lược và phân bổ nguồn lực nội bộ"
      },
      {
        "id": "r3",
        "text": "Mua lại các doanh nghiệp nợ cao nhưng có tiềm năng"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Ngân hàng -> cấp tín dụng. Ban quản lý -> chiến lược. Nhà đầu tư -> mua lại công ty.",
    "id": 107,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Hệ quả của Đa cộng tuyến đối với một mô hình dự báo là gì?",
    "options": [
      {
        "id": "a",
        "text": "Mô hình sẽ không thể tính toán được"
      },
      {
        "id": "b",
        "text": "Nó làm tăng tốc độ xử lý dữ liệu"
      },
      {
        "id": "c",
        "text": "Dẫn đến các ước tính không đáng tin cậy cho từng hệ số dự báo"
      },
      {
        "id": "d",
        "text": "Làm cho biểu đồ ROC AUC luôn đạt 1.0"
      }
    ],
    "correctAnswer": "c",
    "explanation": "Đa cộng tuyến không làm hỏng toàn bộ mô hình nhưng làm hệ số của từng biến trở nên không chính xác, thiếu tin cậy.",
    "id": 108,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Dễ",
    "question": "Điền từ liên quan đến sự tương đồng trong phân cụm:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Nếu hai khách hàng ở gần nhau trong <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, họ sẽ có nhiều điểm tương đồng và do đó nên được nhóm vào cùng một <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "không gian đặc trưng (feature space)"
      },
      {
        "id": "w2",
        "text": "cụm (cluster)"
      },
      {
        "id": "w3",
        "text": "vũ trụ song song"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Khoảng cách trong feature space càng nhỏ, sự tương đồng càng cao, do đó được xếp chung vào 1 cluster.",
    "id": 109,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Nhãn kết quả (label) dự đoán trong mô hình sức khỏe tài chính của Ngân hàng Altra là gì?",
    "options": [
      {
        "id": "a",
        "text": "Doanh nghiệp có thuộc cụm 1 hay cụm 2 không"
      },
      {
        "id": "b",
        "text": "Doanh nghiệp có lợi nhuận cao nhất thị trường"
      },
      {
        "id": "c",
        "text": "Khách hàng có ở lại lâu không"
      },
      {
        "id": "d",
        "text": "Doanh nghiệp có phá sản hay không"
      }
    ],
    "correctAnswer": "d",
    "explanation": "Nhãn để đánh giá là liệu một doanh nghiệp có bị phá sản hay không (sẽ phá sản = 0, không phá sản = 1).",
    "id": 110,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Thứ tự các khái niệm từ mức độ tổng quát đến cá nhân hóa trong Marketing:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Tiếp thị đại chúng (Mass marketing - coi mọi người như 1)"
      },
      {
        "id": "2",
        "text": "Phân khúc thị trường (Segmentation - chia nhóm lớn)"
      },
      {
        "id": "3",
        "text": "Vi phân khúc (Microsegments - nhóm rất nhỏ)"
      },
      {
        "id": "4",
        "text": "Siêu cá nhân hóa (Hyperpersonalization - duy nhất từng người)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Đại chúng -> Phân khúc -> Vi phân khúc -> Cá nhân hóa.",
    "id": 111,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép chức năng của các hàm trong R khi vẽ và đo lường mô hình:",
    "left": [
      {
        "id": "l1",
        "text": "fviz_cluster()"
      },
      {
        "id": "l2",
        "text": "predict(..., type='response')"
      },
      {
        "id": "l3",
        "text": "performance(pred, 'auc')"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Trực quan hóa kết quả phân cụm (k-Means)"
      },
      {
        "id": "r2",
        "text": "Đưa ra dự đoán phá sản cho dữ liệu mới"
      },
      {
        "id": "r3",
        "text": "Tính toán diện tích dưới đường cong ROC để đánh giá mô hình"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "fviz_cluster vẽ cụm. predict lấy xác suất/phản hồi. performance tính AUC.",
    "id": 112,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong đánh giá mô hình bằng ROC, giá trị AUC (Area Under Curve) như thế nào thì được coi là tốt?",
    "options": [
      {
        "id": "a",
        "text": "Bằng 0"
      },
      {
        "id": "b",
        "text": "Càng thấp càng tốt"
      },
      {
        "id": "c",
        "text": "Chính xác là 0.5"
      },
      {
        "id": "d",
        "text": "Các giá trị cao hơn cho thấy dự đoán tốt hơn"
      }
    ],
    "correctAnswer": "d",
    "explanation": "Các giá trị AUC cao hơn cho thấy khả năng phân loại, dự đoán của mô hình tốt hơn.",
    "id": 113,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ liên quan đến VIF (Variance Inflation Factor):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Chúng ta có thể kiểm tra <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (multicollinearity) bằng cách sử dụng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> cho từng biến dự báo.",
    "words": [
      {
        "id": "w1",
        "text": "đa cộng tuyến"
      },
      {
        "id": "w2",
        "text": "VIF"
      },
      {
        "id": "w3",
        "text": "cây quyết định"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "VIF được dùng để đánh giá mức độ đa cộng tuyến của các biến dự báo.",
    "id": 114,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình phân khúc khách hàng theo cơ sở dữ liệu (Data-Driven Segmentation):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Giới thiệu sản phẩm qua các mẫu nhỏ"
      },
      {
        "id": "2",
        "text": "Theo dõi hành vi mua hàng thực tế của khách hàng (dữ liệu bán hàng)"
      },
      {
        "id": "3",
        "text": "Phân tích cụm (Clustering) trên dữ liệu thu thập được"
      },
      {
        "id": "4",
        "text": "Tinh chỉnh lại sản phẩm và chiến lược nhắm mục tiêu (Vòng phản hồi)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Dựa trên data-driven: tung mẫu -> theo dõi hành vi -> phân tích -> vòng lặp tinh chỉnh.",
    "id": 115,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Ví dụ về Vi phân khúc (Microsegmenting) mà Amazon áp dụng là gì?",
    "options": [
      {
        "id": "a",
        "text": "Gửi coupon giảm giá rau củ cho mọi người ở Phoenix"
      },
      {
        "id": "b",
        "text": "Không đưa ra bất kỳ gợi ý nào"
      },
      {
        "id": "c",
        "text": "Đề xuất sản phẩm rất cụ thể dựa trên hành vi mua hàng trong quá khứ của cá nhân"
      },
      {
        "id": "d",
        "text": "Chỉ đề xuất sản phẩm dựa vào độ tuổi"
      }
    ],
    "correctAnswer": "c",
    "explanation": "Amazon tạo microsegments để đề xuất các sản phẩm rất cụ thể cho từng khách hàng.",
    "id": 116,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép ý nghĩa của các thông số/câu lệnh khi thực hành R (Phân khúc bằng k-Means):",
    "left": [
      {
        "id": "l1",
        "text": "set.seed(12345)"
      },
      {
        "id": "l2",
        "text": "center = TRUE"
      },
      {
        "id": "l3",
        "text": "scale = TRUE"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Thiết lập giá trị gieo mầm để có thể tái tạo (reproduce) lại kết quả y hệt"
      },
      {
        "id": "r2",
        "text": "Trừ giá trị trung bình của biến khỏi các giá trị"
      },
      {
        "id": "r3",
        "text": "Chia dữ liệu cho độ lệch chuẩn để đồng bộ thang đo"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "seed = cố định random; center = trừ mean; scale = chia std dev.",
    "id": 117,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Khó",
    "question": "Điền từ vào chỗ trống liên quan đến báo cáo tài chính:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Bộ phận tài chính cung cấp cái nhìn hồi tố thông qua bảng cân đối kế toán, báo cáo <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, và báo cáo lưu chuyển tiền tệ. Họ cũng cung cấp cái nhìn hướng tới tương lai qua các dự báo và lập kế hoạch <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "kết quả hoạt động kinh doanh"
      },
      {
        "id": "w2",
        "text": "kịch bản (scenario planning)"
      },
      {
        "id": "w3",
        "text": "viễn cảnh"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Báo cáo kết quả hoạt động kinh doanh là 1 trong 3 báo cáo chính. Lập kế hoạch kịch bản là phương pháp dự báo tương lai.",
    "id": 118,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Sắp xếp theo thứ tự ưu tiên của việc phân khúc thị trường truyền thống đến tự động hóa AI:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Nhắm mục tiêu theo nhân khẩu học chung (Demographics cơ bản)"
      },
      {
        "id": "2",
        "text": "Sử dụng yếu tố tâm lý học và lối sống (Psychographics)"
      },
      {
        "id": "3",
        "text": "Áp dụng học máy (k-Means) để phân cụm dựa trên dữ liệu mua sắm"
      },
      {
        "id": "4",
        "text": "Siêu cá nhân hóa tự động bằng AI (Hyperpersonalization)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Sự phát triển của segmentation từ tĩnh (nhân khẩu, tâm lý) đến tự động bằng Machine Learning và AI siêu cá nhân hóa.",
    "id": 119,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Nhược điểm của k-Means dẫn đến việc ra đời k-Medoid là gì?",
    "options": [
      {
        "id": "a",
        "text": "Dễ bị ảnh hưởng mạnh bởi nhiễu (outliers) do dùng giá trị trung bình"
      },
      {
        "id": "b",
        "text": "Không thể chạy trên dữ liệu lớn"
      },
      {
        "id": "c",
        "text": "Chỉ hỗ trợ phân khúc theo độ tuổi"
      },
      {
        "id": "d",
        "text": "Bắt buộc dữ liệu phải có nhãn kết quả (labeled)"
      }
    ],
    "correctAnswer": "a",
    "explanation": "k-Means dùng trung bình nên dễ bị nhiễu kéo lệch. k-Medoid dùng điểm thực tế làm tâm nên chống nhiễu tốt hơn.",
    "id": 120,
    "session": "Buổi 4: Algorithms and AI Concepts",
    "session_key": "Day04"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Thuật ngữ 'Ra quyết định dưới sự không chắc chắn' (Decision-Making Under Uncertainty) có nghĩa là gì?",
    "options": [
      {
        "id": "a",
        "text": "Quyết định được đưa ra khi thiếu thông tin hoặc thông tin chỉ có sẵn ở dạng xác suất"
      },
      {
        "id": "b",
        "text": "Quyết định đưa ra khi bạn đã biết chắc chắn 100% về tương lai"
      },
      {
        "id": "c",
        "text": "Quyết định được thực hiện bởi máy tính một cách tự động"
      },
      {
        "id": "d",
        "text": "Việc từ chối đưa ra bất kỳ hành động nào do thiếu thông tin"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Ra quyết định dưới sự không chắc chắn xảy ra khi bạn thiếu thông tin đầy đủ và chỉ có thể dựa vào xác suất thành công.",
    "id": 121,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Hiệu ứng 'Cái roi da' (Bullwhip effect) trong chuỗi cung ứng mô tả hiện tượng nào?",
    "options": [
      {
        "id": "a",
        "text": "Việc giảm giá sản phẩm để chống lại đối thủ cạnh tranh mới"
      },
      {
        "id": "b",
        "text": "Lỗi phần mềm gây chậm trễ cho toàn bộ hệ thống logistic"
      },
      {
        "id": "c",
        "text": "Sự thay đổi nhỏ về nhu cầu bị đánh giá quá cao, dẫn đến dư thừa cung"
      },
      {
        "id": "d",
        "text": "Sự khan hiếm hàng hóa do thiên tai hoặc dịch bệnh"
      }
    ],
    "correctAnswer": "c",
    "explanation": "Hiệu ứng cái roi da xảy ra khi những tín hiệu nhu cầu nhỏ lẻ bị phóng đại dọc theo chuỗi cung ứng, dẫn đến tích trữ quá mức hoặc dư thừa nguồn cung.",
    "id": 122,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "matching",
    "difficulty": "Dễ",
    "question": "Ghép các khái niệm của Cây quyết định (Decision Tree) với định nghĩa của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "Nút gốc (Root node)"
      },
      {
        "id": "l2",
        "text": "Độ vẩn đục Gini (Gini impurity)"
      },
      {
        "id": "l3",
        "text": "Nút lá (Leaf node)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Điểm bắt đầu của cây, biến phân loại tốt nhất được chọn đầu tiên"
      },
      {
        "id": "r2",
        "text": "Chỉ số để đo lường mức độ hỗn tạp của dữ liệu, càng thấp càng tốt"
      },
      {
        "id": "r3",
        "text": "Kết quả dự đoán cuối cùng của nhánh (vd: Có/Không bị chậm giao)"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Root node là nút cao nhất. Gini đo mức độ phân loại tốt hay xấu. Leaf node là kết quả cuối cùng.",
    "id": 123,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp các bước cơ bản trong quá trình Phát triển Sản phẩm Mới:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Hình thành và sàng lọc ý tưởng (Idea Generation & Screening)"
      },
      {
        "id": "2",
        "text": "Phát triển khái niệm và phân tích kinh doanh (Concept & Business Analysis)"
      },
      {
        "id": "3",
        "text": "Thiết kế và phát triển nguyên mẫu sản phẩm"
      },
      {
        "id": "4",
        "text": "Thử nghiệm thị trường (Test Marketing) và Thương mại hóa (Commercialization)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Quy trình tiêu chuẩn: Lên ý tưởng -> Phân tích tính khả thi kinh doanh -> Chế tạo sản phẩm -> Thử nghiệm và tung ra thị trường.",
    "id": 124,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ liên quan đến sự mất cân bằng dữ liệu (Imbalance) và cách xử lý:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Khi số lượng sản phẩm giao đúng hạn quá lớn so với sản phẩm bị chậm giao, mô hình có thể bị thiên vị. Kỹ thuật <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (lấy mẫu giảm) giúp cân bằng dữ liệu, qua đó làm tăng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> (khả năng nhận diện sản phẩm bị chậm giao).",
    "words": [
      {
        "id": "w1",
        "text": "downsampling"
      },
      {
        "id": "w2",
        "text": "độ nhạy (sensitivity)"
      },
      {
        "id": "w3",
        "text": "tính đồng nhất"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Downsampling giảm lượng mẫu của lớp đa số, giúp mô hình tập trung học cách nhận diện lớp thiểu số (tăng độ nhạy).",
    "id": 125,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Đặc điểm chính của thuật toán Rừng ngẫu nhiên (Random Forest) là gì?",
    "options": [
      {
        "id": "a",
        "text": "Kết hợp nhiều cây quyết định bằng kỹ thuật Bagging (bootstrap aggregation) để giảm phương sai"
      },
      {
        "id": "b",
        "text": "Chỉ sử dụng một cây quyết định duy nhất để dự đoán"
      },
      {
        "id": "c",
        "text": "Là thuật toán dựa trên hồi quy tuyến tính cổ điển"
      },
      {
        "id": "d",
        "text": "Chỉ phù hợp với dữ liệu không có nhãn kết quả"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Random Forest tạo ra nhiều cây (forest) bằng cách lấy mẫu có hoàn lại (Bagging) và kết hợp chúng để ra kết quả ổn định hơn.",
    "id": 126,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Trong ví dụ ở chương 14, Nintendo Switch thành công nhờ yếu tố nào?",
    "options": [
      {
        "id": "a",
        "text": "Chỉ có thể chơi khi kết nối với tivi (console) ở nhà"
      },
      {
        "id": "b",
        "text": "Thiết kế linh hoạt cho phép chơi cả cầm tay và qua bảng điều khiển"
      },
      {
        "id": "c",
        "text": "Mức giá cao hơn đáng kể so với các đối thủ"
      },
      {
        "id": "d",
        "text": "Phát hành miễn phí cho tất cả người dùng"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Thiết kế của nó cho phép chơi trò chơi cầm tay và bảng điều khiển (console) thu hút được lượng lớn người dùng.",
    "id": 127,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép các thông số của Ma trận nhầm lẫn (Confusion Matrix) với cách tính:",
    "left": [
      {
        "id": "l1",
        "text": "Độ nhạy (Sensitivity)"
      },
      {
        "id": "l2",
        "text": "Độ đặc hiệu (Specificity)"
      },
      {
        "id": "l3",
        "text": "Dương tính thật (True Positive)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Tỷ lệ mô hình nhận diện chính xác lớp thiểu số (vd: bị chậm giao)"
      },
      {
        "id": "r2",
        "text": "Tỷ lệ mô hình nhận diện chính xác lớp đa số (vd: không bị chậm giao)"
      },
      {
        "id": "r3",
        "text": "Số lượng các trường hợp thực tế CÓ và mô hình dự đoán CÓ"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Sensitivity (True Positive Rate) = đoán trúng lớp thiểu số. Specificity (True Negative Rate) = đoán trúng lớp đa số.",
    "id": 128,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ về các bài kiểm định trong Thử nghiệm A/B (A/B Testing):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Để so sánh giá trị trung bình của ba mức độ khó (Low, Medium, High) trong thiết kế nguyên mẫu game, chúng ta sử dụng kiểm định <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Nếu phương sai không bằng nhau, ta dùng <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> để thay thế.",
    "words": [
      {
        "id": "w1",
        "text": "F (ANOVA)"
      },
      {
        "id": "w2",
        "text": "Welch's ANOVA"
      },
      {
        "id": "w3",
        "text": "chi bình phương (chi-square)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Kiểm định F (ANOVA) dùng cho >=3 nhóm. Welch's ANOVA dùng khi giả định về phương sai bằng nhau bị vi phạm.",
    "id": 129,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "ordering",
    "difficulty": "Khó",
    "question": "Trình tự tính toán Chỉ số Gini (Gini Impurity) cho nút gốc (Root node) trên một biến dự báo:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Tính tỷ lệ kết quả (Có/Không) cho từng nhóm của biến dự báo (vd: Dự báo cao/Thấp)"
      },
      {
        "id": "2",
        "text": "Tính độ vẩn đục (Impurity) của từng nhóm: 1 - P(Có)^2 - P(Không)^2"
      },
      {
        "id": "3",
        "text": "Tính trung bình có trọng số (weighted average) của các chỉ số Impurity này"
      },
      {
        "id": "4",
        "text": "So sánh kết quả với các biến dự báo khác, biến có Gini thấp nhất sẽ làm nút gốc"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Tỷ lệ từng nhóm -> Impurity từng nhóm -> Trọng số tổng thể -> Chọn biến có Gini bé nhất.",
    "id": 130,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Sự tự chọn (Self-selection) trong thử nghiệm A/B dẫn đến vấn đề gì?",
    "options": [
      {
        "id": "a",
        "text": "Nó làm tăng tính ngẫu nhiên của thử nghiệm"
      },
      {
        "id": "b",
        "text": "Nó phá vỡ tính ngẫu nhiên hóa (randomization)"
      },
      {
        "id": "c",
        "text": "Nó giúp hệ thống ghi nhận dữ liệu nhanh hơn"
      },
      {
        "id": "d",
        "text": "Nó loại bỏ nhu cầu phải có biến kết quả"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Tự chọn xảy ra khi người tham gia được tự chọn nhóm, phá vỡ tính ngẫu nhiên và làm lệch kết quả thử nghiệm.",
    "id": 131,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Chỉ số Gini impurity càng thấp thì có ý nghĩa gì trong cây quyết định?",
    "options": [
      {
        "id": "a",
        "text": "Nút đó có khả năng phân loại dữ liệu càng tốt"
      },
      {
        "id": "b",
        "text": "Dữ liệu tại nút đó càng hỗn tạp và lẫn lộn"
      },
      {
        "id": "c",
        "text": "Chỉ số này không phản ánh chất lượng phân loại"
      },
      {
        "id": "d",
        "text": "Mô hình đã bị tính sai và cần phải chạy lại"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Gini impurity thấp nghĩa là dữ liệu ít bị lẫn lộn, do đó có khả năng phân loại, chia rẽ nhóm càng tốt.",
    "id": 132,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các loại bài kiểm định trong phân tích A/B với mục đích sử dụng:",
    "left": [
      {
        "id": "l1",
        "text": "Levene's test"
      },
      {
        "id": "l2",
        "text": "Shapiro-Wilk test"
      },
      {
        "id": "l3",
        "text": "Games-Howell post hoc test"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Kiểm tra tính đồng nhất của phương sai (Equal variance)"
      },
      {
        "id": "r2",
        "text": "Kiểm tra tính phân phối chuẩn (Normality)"
      },
      {
        "id": "r3",
        "text": "Xác định chính xác cặp nhóm nào khác biệt nhau sau khi ANOVA có ý nghĩa"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Levene = Phương sai; Shapiro = Chuẩn hóa; Games-Howell = Bài test hậu hoc khi phương sai khác nhau.",
    "id": 133,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Khó",
    "question": "Điền từ liên quan đến sự kết hợp (Ensemble) trong Random Forest:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Quá trình lấy mẫu có hoàn lại từ tập dữ liệu gốc để xây dựng nhiều cây quyết định khác nhau được gọi là <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>. Random Forest sử dụng kỹ thuật này để giảm <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> của mô hình so với việc chỉ dùng 1 cây đơn lẻ.",
    "words": [
      {
        "id": "w1",
        "text": "Bagging (bootstrap aggregation)"
      },
      {
        "id": "w2",
        "text": "hiện tượng quá khớp (overfitting) và phương sai"
      },
      {
        "id": "w3",
        "text": "chính xác (accuracy)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Bagging giúp tạo ra rừng các cây đa dạng, giảm phương sai và nguy cơ overfitting so với cây quyết định đơn lẻ.",
    "id": 134,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp các bước thực hiện kiểm định thử nghiệm A/B với >=3 nhóm:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Thu thập dữ liệu từ các nguyên mẫu đã được phân bổ ngẫu nhiên"
      },
      {
        "id": "2",
        "text": "Kiểm tra giả định về phân phối chuẩn và phương sai đồng nhất"
      },
      {
        "id": "3",
        "text": "Chạy kiểm định Welch's ANOVA (nếu phương sai không đồng nhất)"
      },
      {
        "id": "4",
        "text": "Chạy kiểm định hậu hoc (Post-hoc test) để xem cặp nguyên mẫu nào thực sự khác biệt"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Data -> Check assumptions -> Chạy ANOVA -> Post-hoc test để xác định rõ sự khác biệt.",
    "id": 135,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Đặc điểm nào KHÔNG ĐÚNG khi nói về kỹ thuật Bagging (bootstrap aggregation)?",
    "options": [
      {
        "id": "a",
        "text": "Nó bao gồm việc lấy mẫu mà không có sự hoàn lại (without replacement)"
      },
      {
        "id": "b",
        "text": "Nó kết hợp kết quả từ nhiều mô hình nhỏ lẻ để ra quyết định chung"
      },
      {
        "id": "c",
        "text": "Nó giúp xây dựng các cây quyết định đa dạng"
      },
      {
        "id": "d",
        "text": "Random forest là một ứng dụng phổ biến của Bagging"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Bagging (Bootstrap aggregation) YÊU CẦU lấy mẫu CÓ hoàn lại (with replacement), do đó câu A là sai.",
    "id": 136,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "matching",
    "difficulty": "Dễ",
    "question": "Ghép các quyết định kinh doanh với các sự không chắc chắn (uncertainty) tương ứng (Theo ví dụ Hãng hàng không):",
    "left": [
      {
        "id": "l1",
        "text": "Quyết định Hành động (Giảm giá)"
      },
      {
        "id": "l2",
        "text": "Quyết định Không hành động (Giữ nguyên giá)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Có thể làm xói mòn lợi nhuận và gây ra cuộc chiến giá cả"
      },
      {
        "id": "r2",
        "text": "Có thể bị cổ đông coi là không sẵn lòng thích ứng với thị trường"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2"
    },
    "explanation": "Hành động giảm giá -> rủi ro chiến tranh giá cả. Không làm gì -> rủi ro mất khách và bị coi là bảo thủ.",
    "id": 137,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Nếu trong một mô hình dự báo, tỷ lệ Accuracy và giá trị AUC đều rất cao, nhưng Sensitivity (Độ nhạy) lại rất thấp, điều này phản ánh vấn đề gì?",
    "options": [
      {
        "id": "a",
        "text": "Mô hình đã bị phân bổ ngẫu nhiên sai cách"
      },
      {
        "id": "b",
        "text": "Mô hình hoàn toàn mất khả năng chạy dự báo"
      },
      {
        "id": "c",
        "text": "Mô hình gặp vấn đề do dữ liệu bị mất cân bằng (class imbalance) nghiêm trọng"
      },
      {
        "id": "d",
        "text": "Mô hình dự báo quá tốt đến mức không cần điều chỉnh thêm"
      }
    ],
    "correctAnswer": "c",
    "explanation": "Khi dữ liệu cực kỳ lệch (imbalance), mô hình có thể chỉ chọn dự báo lớp đa số (đạt Accuracy cao) nhưng hoàn toàn thất bại trong việc nhận diện lớp thiểu số (Sensitivity thấp).",
    "id": 138,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Dễ",
    "question": "Điền từ về Thử nghiệm Nguyên mẫu Trò chơi:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Để tránh việc người chơi tự chọn nhóm theo sở thích màu sắc hay độ khó, GameV phải áp dụng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để phân bổ người chơi. Nhờ đó, bất kỳ sự khác biệt nào về thời gian chơi cũng có thể tự tin gán cho <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "sự ngẫu nhiên hóa (randomization)"
      },
      {
        "id": "w2",
        "text": "mức độ khó (nguyên mẫu)"
      },
      {
        "id": "w3",
        "text": "thiên vị (bias)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Phân bổ ngẫu nhiên giúp cô lập nguyên nhân, khẳng định sự khác biệt là do mức độ khó chứ không do yếu tố nhiễu ngoài.",
    "id": 139,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong thử nghiệm A/B, Giả thuyết Không (Null Hypothesis) biểu thị điều gì?",
    "options": [
      {
        "id": "a",
        "text": "Sự can thiệp (intervention) đã gây ra sự khác biệt"
      },
      {
        "id": "b",
        "text": "Có sự khác biệt đáng kể giữa các nhóm với nhau"
      },
      {
        "id": "c",
        "text": "Không có sự khác biệt đáng kể giữa các nhóm, kết quả chỉ là do ngẫu nhiên"
      },
      {
        "id": "d",
        "text": "Thiết kế của nguyên mẫu A ưu việt hơn hẳn nguyên mẫu B"
      }
    ],
    "correctAnswer": "c",
    "explanation": "Giả thuyết Không (Null Hypothesis) luôn giả định rằng không có sự khác biệt thực sự, và mọi biến động đều do sai số ngẫu nhiên.",
    "id": 140,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Thứ tự lý tưởng khi xử lý tình trạng mất cân bằng dữ liệu trong Random Forest:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Phân chia dữ liệu thành tập huấn luyện (Train) và tập kiểm tra (Test)"
      },
      {
        "id": "2",
        "text": "Thực hiện giảm mẫu (downsampling) trên tập huấn luyện"
      },
      {
        "id": "3",
        "text": "Huấn luyện mô hình Random Forest trên dữ liệu đã cân bằng"
      },
      {
        "id": "4",
        "text": "Dự đoán trên tập kiểm tra và tính toán Ma trận nhầm lẫn (Confusion Matrix)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Tách data -> Cân bằng tập train -> Huấn luyện -> Dự đoán và Đánh giá.",
    "id": 141,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép số lượng nhóm cần thiết (Groups) với thiết kế thử nghiệm A/B tương ứng:",
    "left": [
      {
        "id": "l1",
        "text": "1 yếu tố có 2 cấp độ (levels)"
      },
      {
        "id": "l2",
        "text": "1 yếu tố có 3 cấp độ (levels)"
      },
      {
        "id": "l3",
        "text": "3 yếu tố, mỗi yếu tố có 2 cấp độ (levels)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Cần 2 nhóm (ví dụ: Nút Đỏ vs Nút Xanh)"
      },
      {
        "id": "r2",
        "text": "Cần 3 nhóm (ví dụ: Độ khó Low, Med, High)"
      },
      {
        "id": "r3",
        "text": "Cần 8 nhóm (2 * 2 * 2 = 8)"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Số lượng nhóm phụ thuộc vào tổ hợp của số lượng yếu tố và số cấp độ.",
    "id": 142,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Mục đích chính của một thử nghiệm A/B (A/B testing) là gì?",
    "options": [
      {
        "id": "a",
        "text": "Để xác định hiệu quả của một sự can thiệp (intervention) thông qua quan hệ nhân quả"
      },
      {
        "id": "b",
        "text": "Để tăng mức giá bán của tất cả sản phẩm hiện có"
      },
      {
        "id": "c",
        "text": "Để giảm thiểu thời gian vận chuyển của chuỗi cung ứng"
      },
      {
        "id": "d",
        "text": "Để phát hiện mối tương quan giữa các biến mà không cần kiểm soát"
      }
    ],
    "correctAnswer": "a",
    "explanation": "A/B testing là một thử nghiệm nhân quả (causal testing) nhằm so sánh hiệu quả thực sự của một sự can thiệp so với đối chứng.",
    "id": 143,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ về các kết quả dự báo trong bảng nhầm lẫn:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Nếu độ đặc hiệu (specificity) của mô hình thấp, chúng ta sẽ kết thúc bằng việc đặt hàng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> những sản phẩm ít có khả năng bị chậm giao, tức là rơi vào trường hợp <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "quá mức (overordering)"
      },
      {
        "id": "w2",
        "text": "dương tính giả (False Positive)"
      },
      {
        "id": "w3",
        "text": "âm tính thật (True Negative)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Specificity thấp nghĩa là đoán nhầm hàng Không chậm thành Có chậm (False Positive), dẫn tới tích trữ quá mức.",
    "id": 144,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp theo logic của Quá trình tinh chỉnh Siêu tham số (Hyperparameter Tuning):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Thiết lập danh sách các siêu tham số cần thử nghiệm (vd: mtry, min_n)"
      },
      {
        "id": "2",
        "text": "Sử dụng kiểm chứng chéo k-fold (k-fold Cross Validation) để chạy thử"
      },
      {
        "id": "3",
        "text": "Đánh giá mô hình dựa trên số đo AUC ROC cho từng tổ hợp"
      },
      {
        "id": "4",
        "text": "Chọn tổ hợp siêu tham số tốt nhất (vd: select_best) để hoàn thiện mô hình"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Grid search -> k-fold CV -> Đánh giá các Fold -> Chọn Best hyperparameter.",
    "id": 145,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Trong bài kiểm định F, việc biến kết quả (outcome variable) có bản chất là liên tục (continuous) mang ý nghĩa gì?",
    "options": [
      {
        "id": "a",
        "text": "Ví dụ như thời gian chơi game, có thể đo lường bằng các giá trị số chi tiết thay vì Có/Không"
      },
      {
        "id": "b",
        "text": "Biến kết quả chỉ có hai giá trị (Có hoặc Không, 1 hoặc 0)"
      },
      {
        "id": "c",
        "text": "Biến kết quả không thể được sử dụng trong Thử nghiệm A/B"
      },
      {
        "id": "d",
        "text": "Biến kết quả chỉ mang giá trị phân loại như 'Màu xanh', 'Màu đỏ'"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Biến liên tục có thể mang giá trị số mở rộng (ví dụ thời gian: 1.5 giờ, 2.3 giờ...). Việc này phù hợp với các kiểm định như F-test/ANOVA.",
    "id": 146,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các ví dụ phát triển sản phẩm với loại hình đổi mới của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "Chase Sapphire Reserve"
      },
      {
        "id": "l2",
        "text": "Nintendo Switch"
      },
      {
        "id": "l3",
        "text": "Ứng dụng theo dõi sức khỏe số"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Sản phẩm dịch vụ tài chính có chương trình điểm thưởng lớn"
      },
      {
        "id": "r2",
        "text": "Phần cứng vật lý tích hợp cách chơi đa dạng (cầm tay/console)"
      },
      {
        "id": "r3",
        "text": "Sản phẩm tồn tại hoàn toàn trên web, không có hiện diện vật lý"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Chase = Tài chính. Nintendo = Phần cứng. Ứng dụng = Sản phẩm ảo/web.",
    "id": 147,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Khó",
    "question": "Điền từ về hậu quả khi một doanh nghiệp phản ứng chậm với thị trường:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Bằng cách không điều chỉnh theo động lực thị trường đang thay đổi, doanh nghiệp có khả năng <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> mà người mới tham gia có thể khai thác, dẫn đến việc họ nhận ra quá muộn và không thể <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "mất đi các cơ hội"
      },
      {
        "id": "w2",
        "text": "phục hồi vị thế của mình"
      },
      {
        "id": "w3",
        "text": "phá sản ngay lập tức"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Việc giữ nguyên hiện trạng mang rủi ro bỏ lỡ cơ hội, khiến đối thủ cạnh tranh giá rẻ chiếm mất thị phần.",
    "id": 148,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Sắp xếp theo thứ tự ưu tiên của Cây quyết định từ trên xuống:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Tính Gini Impurity cho tất cả các biến dự báo"
      },
      {
        "id": "2",
        "text": "Chọn biến có Gini Impurity thấp nhất làm Nút gốc (Root Node)"
      },
      {
        "id": "3",
        "text": "Tiếp tục phân chia các nhánh bên dưới để giảm mức độ hỗn tạp"
      },
      {
        "id": "4",
        "text": "Hoàn thành và tạo ra Nút lá (Leaf Node) để dự đoán"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Tính Gini -> Xác định root node -> Tạo nhánh -> Tạo nút lá.",
    "id": 149,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Khẳng định nào đúng khi so sánh kiểm định quan hệ tương quan và thử nghiệm A/B?",
    "options": [
      {
        "id": "a",
        "text": "Thử nghiệm A/B cho phép xác định rõ mối quan hệ nguyên nhân - kết quả (nhân quả)"
      },
      {
        "id": "b",
        "text": "Thử nghiệm tương quan luôn mang lại độ chính xác cao hơn thử nghiệm A/B"
      },
      {
        "id": "c",
        "text": "Thử nghiệm A/B không thể dùng để kiểm tra tính năng phần mềm mới"
      },
      {
        "id": "d",
        "text": "Cả hai đều không yêu cầu phân bổ ngẫu nhiên người tham gia"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Thử nghiệm A/B là thử nghiệm can thiệp ngẫu nhiên (Causal Testing), giúp tìm ra quan hệ nhân quả (ví dụ: do nút màu đỏ mà lượng click tăng).",
    "id": 150,
    "session": "Buổi 5: Data Analysis and Financial Modeling",
    "session_key": "Day05"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Ứng dụng AI giúp Kế toán Điều tra chuyển đổi từ mô hình phản ứng hậu kiểm sang mô hình nào?",
    "options": [
      {
        "id": "a",
        "text": "Phòng ngừa chủ động (Proactive Prevention)"
      },
      {
        "id": "b",
        "text": "Kiểm toán truyền thống dựa trên sổ sách giấy tờ"
      },
      {
        "id": "c",
        "text": "Hệ thống chuyên gia lập trình quy tắc thủ công"
      },
      {
        "id": "d",
        "text": "Lập báo cáo tài chính nội bộ thủ công hàng quý"
      }
    ],
    "correctAnswer": "a",
    "explanation": "AI giúp chuyển từ kiểm tra sau khi sự cố xảy ra sang phòng ngừa chủ động và theo thời gian thực.",
    "id": 151,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Đâu là điểm yếu lớn nhất của phương pháp chọn mẫu thống kê truyền thống trong phát hiện gian lận?",
    "options": [
      {
        "id": "a",
        "text": "Cần quá nhiều phần mềm máy tính hiện đại để chạy"
      },
      {
        "id": "b",
        "text": "Nó bỏ lọt các giao dịch gian lận nằm ngoài mẫu kiểm toán"
      },
      {
        "id": "c",
        "text": "Nó phân tích 100% giao dịch khiến kế toán viên mệt mỏi"
      },
      {
        "id": "d",
        "text": "Hệ thống tự động đưa ra quá nhiều cảnh báo giả"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Chọn mẫu thống kê thường chỉ kiểm tra 5-10% dữ liệu, kẻ gian lận dễ dàng lách qua bằng cách chia nhỏ giao dịch (Smurfing).",
    "id": 152,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "matching",
    "difficulty": "Dễ",
    "question": "Ghép các công nghệ AI với tính năng chính trong phát hiện gian lận:",
    "left": [
      {
        "id": "l1",
        "text": "Xử lý Ngôn ngữ Tự nhiên (NLP)"
      },
      {
        "id": "l2",
        "text": "Phân tích Mạng lưới (Graph Analysis)"
      },
      {
        "id": "l3",
        "text": "Học không giám sát (Unsupervised ML)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Đọc hiểu email, hợp đồng và biên bản họp"
      },
      {
        "id": "r2",
        "text": "Trực quan hóa quan hệ giữa các tài khoản, IP, công ty sân sau"
      },
      {
        "id": "r3",
        "text": "Tự động gom cụm, tìm điểm ngoại lai mà không cần gán nhãn"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "NLP đọc văn bản. Graph vẽ sơ đồ mạng lưới quan hệ. Unsupervised ML tìm điểm bất thường từ dữ liệu thô.",
    "id": 153,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp theo Lộ trình 7 Bước Triển khai AI trong Kế toán (4 bước đầu):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Đánh giá chiến lược và xác định nút thắt cổ chai"
      },
      {
        "id": "2",
        "text": "Chọn lựa công cụ AI phù hợp quy mô doanh nghiệp"
      },
      {
        "id": "3",
        "text": "Đào tạo nhân sự kỹ năng AI, xóa bỏ tâm lý e ngại"
      },
      {
        "id": "4",
        "text": "Triển khai thí điểm (Pilot) trên tác vụ lặp đi lặp lại"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Lộ trình: Đánh giá chiến lược -> Chọn công cụ -> Đào tạo nhân lực -> Triển khai Pilot.",
    "id": 154,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ vào khái niệm phân tích dữ liệu gian lận:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Thay vì kiểm tra hậu kỳ (sau khi kết thúc kỳ kế toán), hệ thống AI phân tích toàn phần 100% dữ liệu theo <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, giúp phát hiện và ngăn chặn giao dịch bất thường nhằm giảm thiểu <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "thời gian thực (real-time)"
      },
      {
        "id": "w2",
        "text": "cảnh báo giả (false positives)"
      },
      {
        "id": "w3",
        "text": "chu kỳ hàng năm"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Real-time anomaly detection giúp cảnh báo ngay khi giao dịch xảy ra, đồng thời AI học cách giảm bớt cảnh báo giả (false positives).",
    "id": 155,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Hiện tượng 'ảo giác' (Hallucination) trong AI Tạo sinh (GenAI) mang lại rủi ro gì lớn nhất cho ngành kế toán?",
    "options": [
      {
        "id": "a",
        "text": "AI sinh ra thông tin, trích dẫn hoặc số liệu tài chính không có thật"
      },
      {
        "id": "b",
        "text": "Nó làm máy tính của kế toán viên tiêu thụ quá nhiều điện năng"
      },
      {
        "id": "c",
        "text": "Không thể kết nối với mạng nội bộ của doanh nghiệp"
      },
      {
        "id": "d",
        "text": "Luôn dự báo lạm phát sai lệch do lỗi phần cứng"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Ảo giác của GenAI là hiện tượng nó tự bịa ra thông tin sai lệch trông có vẻ hợp lý, rất nguy hiểm nếu áp dụng vào BCTC.",
    "id": 156,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Mô hình Học máy nào phù hợp nhất để nhận diện các chiêu thức gian lận ĐÃ BIẾT từ dữ liệu lịch sử?",
    "options": [
      {
        "id": "a",
        "text": "Học không giám sát (Unsupervised Learning)"
      },
      {
        "id": "b",
        "text": "Học có giám sát (Supervised Learning)"
      },
      {
        "id": "c",
        "text": "Hệ thống lưu trữ đám mây phân tán"
      },
      {
        "id": "d",
        "text": "Thuật toán K-Means Clustering"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Học có giám sát dùng dữ liệu đã gán nhãn ('gian lận' / 'hợp lệ') để nhận diện lại các hành vi gian lận đã biết.",
    "id": 157,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép các thuật ngữ kỹ thuật dữ liệu tài chính với đặc điểm của chúng:",
    "left": [
      {
        "id": "l1",
        "text": "Underfitting (Độ lệch cao)"
      },
      {
        "id": "l2",
        "text": "Overfitting (Phương sai cao)"
      },
      {
        "id": "l3",
        "text": "Bias vs. Variance Tradeoff"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Mô hình quá đơn giản, không học được quy luật dữ liệu"
      },
      {
        "id": "r2",
        "text": "Mô hình quá phức tạp, học vẹt cả nhiễu của dữ liệu huấn luyện"
      },
      {
        "id": "r3",
        "text": "Quá trình tìm điểm cân bằng tối ưu giữa hai lỗi sai số trên"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Underfitting là Bias cao. Overfitting là Variance cao. Điểm cân bằng là Tradeoff.",
    "id": 158,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ liên quan đến quá trình huấn luyện Học máy (Modeling Process):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Để đánh giá mô hình, tập dữ liệu được chia làm hai phần: Tập <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> (thường chiếm 80%) để mô hình học quy luật và Tập <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> (thường 20%) dùng để đánh giá hiệu suất khách quan.",
    "words": [
      {
        "id": "w1",
        "text": "huấn luyện (Training set)"
      },
      {
        "id": "w2",
        "text": "kiểm tra (Test set)"
      },
      {
        "id": "w3",
        "text": "ngoại lai (Outliers)"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Data luôn được chia Train (để học) và Test (để kiểm chứng).",
    "id": 159,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "ordering",
    "difficulty": "Khó",
    "question": "Sắp xếp Vòng đời Dự án Khoa học Dữ liệu trong Kiểm tra Gian lận (Data Science Lifecycle):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Hiểu bài toán nghiệp vụ (Xác định mục tiêu chống gian lận)"
      },
      {
        "id": "2",
        "text": "Đánh giá, làm sạch & Chuẩn bị dữ liệu (Data Preparation)"
      },
      {
        "id": "3",
        "text": "Mô hình hóa (Modeling) & Đánh giá hiệu suất thuật toán"
      },
      {
        "id": "4",
        "text": "Triển khai hệ thống (Deployment) vào giám sát thực tế"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Theo hình 6.4: Business Understanding -> Data Prep -> Modeling & Evaluation -> Deployment.",
    "id": 160,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong Case Study 4, cơ quan nhà nước đã phát hiện 'Thông đồng đấu thầu' (Bid-rigging) thông qua thuật toán nào?",
    "options": [
      {
        "id": "a",
        "text": "Hồi quy tuyến tính đơn giản trên bảng tính Excel"
      },
      {
        "id": "b",
        "text": "Phân tích bất thường kết hợp phân tích mạng lưới (Graph Analytics)"
      },
      {
        "id": "c",
        "text": "Mạng nơ-ron nhân tạo thế hệ đầu từ thập niên 90"
      },
      {
        "id": "d",
        "text": "Học có giám sát dùng dữ liệu gian lận ngân hàng"
      }
    ],
    "correctAnswer": "b",
    "explanation": "AI phân tích bất thường và Graph Analytics theo dõi lịch sử nộp thầu của các công ty có liên quan (sân sau).",
    "id": 161,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Theo báo cáo, công nghệ Trí tuệ Nhân tạo đang tác động đến ngành Kế toán - Kiểm toán như thế nào?",
    "options": [
      {
        "id": "a",
        "text": "Loại bỏ hoàn toàn sự can thiệp và kiểm soát của con người"
      },
      {
        "id": "b",
        "text": "Thay thế phán đoán nghề nghiệp của kiểm toán viên"
      },
      {
        "id": "c",
        "text": "Tự động kiểm tra 100% dữ liệu, chuyển hướng sang kiểm toán liên tục"
      },
      {
        "id": "d",
        "text": "Làm chậm quá trình phát hành báo cáo tài chính cuối năm"
      }
    ],
    "correctAnswer": "c",
    "explanation": "AI tự động kiểm tra 100% dữ liệu giúp kiểm toán viên chuyển từ lấy mẫu sang Kiểm toán liên tục (Continuous Auditing).",
    "id": 162,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các cấp độ AI với định nghĩa trong Kế toán (Theo biểu đồ Venn):",
    "left": [
      {
        "id": "l1",
        "text": "Trí tuệ nhân tạo (AI)"
      },
      {
        "id": "l2",
        "text": "Học máy (ML)"
      },
      {
        "id": "l3",
        "text": "Học sâu (Deep Learning)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Khái niệm rộng nhất về máy tính mô phỏng trí thông minh con người"
      },
      {
        "id": "r2",
        "text": "Máy tính sử dụng thuật toán thống kê để tự học từ dữ liệu tài chính"
      },
      {
        "id": "r3",
        "text": "Phân nhánh nâng cao dùng mạng nơ-ron nhiều lớp (nhận diện hình ảnh/chữ viết)"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "AI là tập lớn nhất. ML là tập con của AI. DL là tập con của ML chuyên xử lý phức tạp bằng mạng nơ-ron.",
    "id": 163,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Khó",
    "question": "Điền từ về hệ thống phát hiện gian lận tiền lương (Payroll Fraud):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Trong Case Study Tập đoàn Đa quốc gia, AI sử dụng kỹ thuật phân cụm <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> để đối chiếu chéo thông tin ngân hàng và mã số thuế, qua đó phát hiện các tài khoản <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> do quản lý chi nhánh cấu kết tạo ra.",
    "words": [
      {
        "id": "w1",
        "text": "không giám sát (Unsupervised)"
      },
      {
        "id": "w2",
        "text": "nhân viên ma (ghost employees)"
      },
      {
        "id": "w3",
        "text": "đám mây phân tán"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Sử dụng Unsupervised Learning để tìm các 'ghost employees' không có thật nhằm bòn rút tiền lương.",
    "id": 164,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Sắp xếp quá trình Phát triển Hệ thống Big Data (Tech Stack):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Hệ thống ghi nhận dữ liệu từ các giao dịch thô (Data Sources)"
      },
      {
        "id": "2",
        "text": "Hệ thống truyền tải sự kiện trực tuyến (Ví dụ: Apache Kafka)"
      },
      {
        "id": "3",
        "text": "Hệ thống lưu trữ phân tán và xử lý đám mây (Hadoop/Spark)"
      },
      {
        "id": "4",
        "text": "Giao diện trực quan hóa dữ liệu cho Kế toán viên (Tableau/Power BI)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Tech stack flow: Nguồn dữ liệu -> Streaming/Kafka -> Data Lake/Hadoop -> Visualization BI tools.",
    "id": 165,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong kinh tế vĩ mô, Ngân hàng Trung ương sử dụng AI để cảnh báo hiện tượng 'Rút tiền ồ ạt' (Bank Run) như thế nào?",
    "options": [
      {
        "id": "a",
        "text": "Từ chối mọi yêu cầu rút tiền của khách hàng cá nhân"
      },
      {
        "id": "b",
        "text": "Phân tích tự động các chỉ số thanh khoản, dòng tiền gửi và tỷ lệ nợ xấu"
      },
      {
        "id": "c",
        "text": "Xóa bỏ các hồ sơ vay vốn có rủi ro cao một cách thủ công"
      },
      {
        "id": "d",
        "text": "Chỉ dựa vào các tin đồn vô căn cứ trên báo chí truyền thông"
      }
    ],
    "correctAnswer": "b",
    "explanation": "AI quét hàng vạn chỉ tiêu báo cáo tuân thủ từ các ngân hàng để phát hiện sớm sụt giảm thanh khoản, ngăn chặn Bank Run.",
    "id": 166,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "matching",
    "difficulty": "Dễ",
    "question": "Ghép các ứng dụng GenAI với lĩnh vực Kế toán cụ thể:",
    "left": [
      {
        "id": "l1",
        "text": "Kế toán Tài chính"
      },
      {
        "id": "l2",
        "text": "Kế toán Quản trị"
      },
      {
        "id": "l3",
        "text": "Tư vấn Thuế"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Tự động phân loại hóa đơn (OCR) và hạch toán"
      },
      {
        "id": "r2",
        "text": "Dự báo dòng tiền (Cash Flow) và phân tích phương sai"
      },
      {
        "id": "r3",
        "text": "Rà soát luật thuế, chuẩn bị tờ khai tối ưu hóa chi phí"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Tài chính -> hạch toán. Quản trị -> dự báo tương lai. Thuế -> chuẩn bị tờ khai.",
    "id": 167,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Khó",
    "question": "Việc sử dụng công nghệ AI 'hộp đen' (Black-box) trong kiểm toán gặp trở ngại pháp lý gì lớn nhất?",
    "options": [
      {
        "id": "a",
        "text": "Không thể giải thích cho cơ quan pháp luật lý do AI đưa ra kết luận"
      },
      {
        "id": "b",
        "text": "Chi phí quá rẻ khiến hệ thống mất đi sự uy tín"
      },
      {
        "id": "c",
        "text": "Hộp đen không thể đọc được dữ liệu phi cấu trúc"
      },
      {
        "id": "d",
        "text": "Chỉ hoạt động được trên các máy tính siêu phân luồng"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Black-box AI khó giải thích quy trình ra quyết định, gây khó khăn khi cần trình bày căn cứ khởi tố trước Tòa án.",
    "id": 168,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Dễ",
    "question": "Điền từ liên quan đến sự giám sát của con người đối với AI:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Mặc dù AI có thể tự động hóa hàng loạt quy trình kế toán, nguyên tắc <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> yêu cầu Kế toán viên phải luôn luôn kiểm duyệt và duy trì sự kiểm soát cuối cùng, kết hợp với <span class=\"blank-slot\" data-id=\"2\">___(2)___</span> để ra quyết định.",
    "words": [
      {
        "id": "w1",
        "text": "Human-in-the-loop"
      },
      {
        "id": "w2",
        "text": "phán đoán nghề nghiệp"
      },
      {
        "id": "w3",
        "text": "làm sạch dữ liệu"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Nguyên tắc 'Người dùng trong vòng lặp' (Human-in-the-loop) nhấn mạnh vai trò quyết định cuối cùng vẫn thuộc về chuyên gia.",
    "id": 169,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong Case Study 3 (Bảo hiểm), AI kết hợp NLP với Computer Vision để giải quyết vấn đề gì?",
    "options": [
      {
        "id": "a",
        "text": "Xác định xem nhân viên bảo hiểm có đi làm đúng giờ hay không"
      },
      {
        "id": "b",
        "text": "Đọc báo cáo giám định và phân tích ảnh hiện trường để tìm dấu hiệu chỉnh sửa"
      },
      {
        "id": "c",
        "text": "Phân tích giá cổ phiếu của các công ty bảo hiểm trên sàn chứng khoán"
      },
      {
        "id": "d",
        "text": "In hóa đơn bồi thường ra giấy một cách tự động"
      }
    ],
    "correctAnswer": "b",
    "explanation": "NLP đọc văn bản giám định và Computer Vision phân tích hình ảnh xem ảnh tai nạn có bị photoshop cắt ghép hay không.",
    "id": 170,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Sắp xếp mức độ phức tạp từ thấp đến cao trong 3 trụ cột kỹ năng Kế toán viên hiện đại (Venn Diagram):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Kiến thức chuyên môn Kế toán / Tài chính cốt lõi"
      },
      {
        "id": "2",
        "text": "Sử dụng công cụ tính toán Thống kê và Excel trung cấp"
      },
      {
        "id": "3",
        "text": "Viết truy vấn SQL, Python để xử lý Dữ liệu lớn (Big Data)"
      },
      {
        "id": "4",
        "text": "Xây dựng và huấn luyện mô hình Học máy (Machine Learning)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Từ kiến thức kế toán nền tảng -> Thống kê Excel -> SQL/Python Big data -> ML modeling.",
    "id": 171,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "matching",
    "difficulty": "Khó",
    "question": "Ghép các Khung Kỹ năng Cần thiết trong thời đại AI (Bảng 2.2) với mức độ quan trọng:",
    "left": [
      {
        "id": "l1",
        "text": "Tư duy phản biện & Thẩm định (Kiểm chứng sai lệch)"
      },
      {
        "id": "l2",
        "text": "Kỹ thuật Prompt & Giao tiếp AI (SPARKS)"
      },
      {
        "id": "l3",
        "text": "Đạo đức & Tuân thủ Pháp lý (GDPR)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Quan trọng nhất, bắt buộc để chặn ảo giác AI trước khi duyệt"
      },
      {
        "id": "r2",
        "text": "Kỹ năng cốt lõi giúp điều khiển và ra lệnh chính xác cho ChatGPT"
      },
      {
        "id": "r3",
        "text": "Rất cao, đảm bảo không vi phạm bảo mật dữ liệu khách hàng"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "Phản biện là quan trọng nhất để tránh báo cáo sai. Prompt là công cụ giao tiếp hằng ngày. Tuân thủ GDPR bảo vệ quyền riêng tư.",
    "id": 172,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Khái niệm 'Giải thích mô hình' (Explainable AI - XAI) có ý nghĩa gì trong kiểm toán?",
    "options": [
      {
        "id": "a",
        "text": "Mô hình giúp người dùng biết được lý do tại sao AI lại ra kết luận gian lận"
      },
      {
        "id": "b",
        "text": "Mô hình có thể tự động thuyết trình bằng giọng nói qua loa"
      },
      {
        "id": "c",
        "text": "Mô hình giấu kín thuật toán để bảo mật 100% trước đối thủ"
      },
      {
        "id": "d",
        "text": "AI không cần giải thích gì vì kết quả của nó luôn luôn đúng"
      }
    ],
    "correctAnswer": "a",
    "explanation": "Explainable AI (XAI) giúp mở 'hộp đen', làm rõ cách AI suy luận để có thể giải trình trước Tòa án hoặc cấp quản lý.",
    "id": 173,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Trung bình",
    "question": "Điền từ về rủi ro của AI Tạo sinh (GenAI):",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Trong chính sách bảo mật doanh nghiệp, nhân viên kế toán tuyệt đối bị cấm đưa các số liệu tài chính <span class=\"blank-slot\" data-id=\"1\">___(1)___</span> lên các công cụ AI công cộng (như ChatGPT bản miễn phí) để tránh rò rỉ <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "mật (confidential)"
      },
      {
        "id": "w2",
        "text": "sở hữu trí tuệ và bí mật kinh doanh"
      },
      {
        "id": "w3",
        "text": "đã công bố công khai"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Dữ liệu mật bị đưa lên AI công cộng có nguy cơ bị dùng làm dữ liệu huấn luyện, gây rò rỉ bí mật.",
    "id": 174,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "ordering",
    "difficulty": "Trung bình",
    "question": "Trình tự khám phá bất thường trong Mua sắm công (Tackling bid-rigging):",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Tập hợp hàng nghìn hồ sơ nộp thầu lịch sử"
      },
      {
        "id": "2",
        "text": "Sử dụng Graph Analytics vẽ bản đồ quan hệ (IP, email, cổ đông)"
      },
      {
        "id": "3",
        "text": "Phát hiện tần suất thắng thầu luân phiên và mức giá sát nút dự toán"
      },
      {
        "id": "4",
        "text": "Kết luận mạng lưới thông đồng thầu (collusion) và khởi tố"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Lấy hồ sơ -> Vẽ sơ đồ quan hệ -> Nhận diện mẫu luân phiên -> Kết luận có thông đồng.",
    "id": 175,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Dễ",
    "question": "Quá trình EDA (Exploratory Data Analysis) trong học máy dùng để làm gì?",
    "options": [
      {
        "id": "a",
        "text": "Đóng gói phần mềm để bán cho khách hàng"
      },
      {
        "id": "b",
        "text": "Thăm dò, vẽ biểu đồ để phát hiện giá trị ngoại lai trước khi huấn luyện"
      },
      {
        "id": "c",
        "text": "Thay thế nhân viên kế toán quản trị trong việc viết báo cáo"
      },
      {
        "id": "d",
        "text": "Chỉ dùng để cài đặt mật khẩu cho cơ sở dữ liệu"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Khám phá dữ liệu (EDA) là bước chuẩn bị, vẽ biểu đồ để hiểu rõ phân phối dữ liệu, tìm lỗi/ngoại lai trước khi đưa vào ML.",
    "id": 176,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "matching",
    "difficulty": "Trung bình",
    "question": "Ghép các công nghệ thập niên với đặc trưng phân tích gian lận:",
    "left": [
      {
        "id": "l1",
        "text": "Thập niên 1980s (Hệ thống chuyên gia)"
      },
      {
        "id": "l2",
        "text": "Thập niên 2000s (Học máy tiên tiến)"
      },
      {
        "id": "l3",
        "text": "Thập niên 2020s (AI Tạo sinh)"
      }
    ],
    "right": [
      {
        "id": "r1",
        "text": "Chỉ chạy quy tắc tĩnh (If-Then), không thể tự học"
      },
      {
        "id": "r2",
        "text": "Chấm điểm rủi ro tự động nhưng thường rơi vào dạng hộp đen khó giải thích"
      },
      {
        "id": "r3",
        "text": "Có thể đọc hiểu biên bản cuộc họp và tự động viết báo cáo điều tra"
      }
    ],
    "correctPairs": {
      "l1": "r1",
      "l2": "r2",
      "l3": "r3"
    },
    "explanation": "80s: Rule-based. 2000s: Machine Learning black-boxes. 2020s: LLMs, GenAI NLP.",
    "id": 177,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "fill_in_blanks",
    "difficulty": "Khó",
    "question": "Điền từ về các thuật toán trong Case Study 4:",
    "instruction": "(Nhấn vào chỗ trống, sau đó nhấn vào từ bên dưới để điền)",
    "text": "Để phát hiện nhóm công ty 'sân sau' thông đồng thổi phồng giá trúng thầu để nhận <span class=\"blank-slot\" data-id=\"1\">___(1)___</span>, cơ quan quản lý đã áp dụng hệ thống phát hiện <span class=\"blank-slot\" data-id=\"2\">___(2)___</span>.",
    "words": [
      {
        "id": "w1",
        "text": "tiền hoa hồng (kickbacks)"
      },
      {
        "id": "w2",
        "text": "bất thường (Anomaly Detection)"
      },
      {
        "id": "w3",
        "text": "nhân viên ma"
      }
    ],
    "correctAnswers": {
      "1": "w1",
      "2": "w2"
    },
    "explanation": "Bid-riggers thổi giá lên 25-40% để nhận kickbacks. Anomaly Detection (AI) phát hiện quy luật này.",
    "id": 178,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "ordering",
    "difficulty": "Dễ",
    "question": "Trình tự kỹ thuật tạo Biến Mục Tiêu (Target Creation) trong giám sát gian lận:",
    "instruction": "(Nhấn vào từng mục ở danh sách bên dưới để chuyển lên bảng đã chọn)",
    "items": [
      {
        "id": "1",
        "text": "Ghi nhận mọi giao dịch chuyển tiền trong quá khứ"
      },
      {
        "id": "2",
        "text": "Đánh dấu (Label) các giao dịch sạch là số 0"
      },
      {
        "id": "3",
        "text": "Đánh dấu các giao dịch gian lận/vỡ nợ là số 1"
      },
      {
        "id": "4",
        "text": "Nạp tập dữ liệu 0 và 1 này vào mô hình Học có giám sát (Supervised ML)"
      }
    ],
    "correctOrder": [
      "1",
      "2",
      "3",
      "4"
    ],
    "explanation": "Thu thập data -> Đánh nhãn 0 (hợp lệ) -> Đánh nhãn 1 (gian lận) -> Train supervised ML.",
    "id": 179,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  },
  {
    "type": "multiple_choice",
    "difficulty": "Trung bình",
    "question": "Trong Kinh tế học Phát triển (Development Economics), AI và dữ liệu viễn thông được dùng để làm gì?",
    "options": [
      {
        "id": "a",
        "text": "Theo dõi nội dung tin nhắn cá nhân của người dân"
      },
      {
        "id": "b",
        "text": "Lập bản đồ nghèo đói (Poverty Mapping) để phân bổ phúc lợi minh bạch"
      },
      {
        "id": "c",
        "text": "Chặn hoàn toàn các kết nối 5G ở khu vực nông thôn"
      },
      {
        "id": "d",
        "text": "Điều chỉnh lãi suất ngân hàng thương mại hàng tuần"
      }
    ],
    "correctAnswer": "b",
    "explanation": "Dữ liệu vệ sinh dịch tễ, viễn thông và điện năng tiêu thụ giúp AI vẽ bản đồ nghèo đói để chính phủ hỗ trợ đúng người yếu thế.",
    "id": 180,
    "session": "Buổi 6: Machine Learning for Finance",
    "session_key": "Day06"
  }
];
