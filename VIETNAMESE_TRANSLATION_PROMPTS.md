# 🇻🇳 Hướng dẫn dịch từ tiếng Trung sang tiếng Việt cho Legado

## 🤖 Sử dụng AI (Gemini, ChatGPT, Claude) để dịch sang tiếng Việt

## 📋 Chuẩn bị

1. **Tạo batch nhỏ** (50-100 entries mỗi lần để có kết quả tốt nhất):
```bash
# Đã tạo sẵn 117 batch files và prompt files
# Sử dụng ai_prompt_batch_*.txt có sẵn nhưng thay đổi yêu cầu dịch sang tiếng Việt
```

## 🎯 Prompt tối ưu cho AI dịch sang tiếng Việt

### Cho Gemini/ChatGPT/Claude:

```
Tôi cần bạn dịch văn bản tiếng Trung sang tiếng Việt cho ứng dụng đọc sách Android tên "Legado". Đây là ứng dụng đọc sách chuyên nghiệp với các tính năng như nguồn sách, giao diện đọc, TTS, v.v.

**BỐI CẢNH**: Legado là ứng dụng đọc sách Android mã nguồn mở hỗ trợ:
- Nhiều nguồn sách và định dạng
- Giao diện đọc có thể tùy chỉnh
- Chức năng đọc văn bản thành giọng nói (TTS)
- Quản lý sách và thư viện
- Dịch vụ web và nhập/xuất dữ liệu

**YÊU CẦU DỊCH THUẬT**:
1. Dịch sang tiếng Việt tự nhiên, thân thiện với người dùng
2. Giữ thuật ngữ kỹ thuật nhất quán (ví dụ: "书源" = "Nguồn sách")
3. Tuân theo quy ước giao diện Android bằng tiếng Việt
4. Xem xét ngữ cảnh được cung cấp cho mỗi chuỗi
5. Giữ nguyên các placeholder định dạng như %s, %d

**ĐỊNH DẠNG ĐẦU VÀO**: CSV với các cột: id, type, file_path, line_number, string_name, original_text, translation, context, notes

**NHIỆM VỤ CỦA BẠN**: Điền vào cột "translation" với bản dịch tiếng Việt chính xác.

Dữ liệu cần dịch:

[DÁN DỮ LIỆU CSV VÀO ĐÂY]

**ĐẦU RA**: Trả về CSV hoàn chỉnh với bản dịch được điền vào cột "translation".
```

### 🔥 Prompt cụ thể cho từng batch:

```
Dịch batch ứng dụng Legado này từ tiếng Trung sang tiếng Việt:

**DỰ ÁN**: Legado - Ứng dụng đọc sách Android mã nguồn mở
**NHIỆM VỤ**: Dịch chuỗi giao diện tiếng Trung sang tiếng Việt
**YÊU CẦU**: 
- Tiếng Việt tự nhiên cho người dùng ứng dụng di động
- Thuật ngữ nhất quán
- Giữ nguyên %s, %d, \n
- Tuân theo hướng dẫn Android Material Design

**TỪ VỰNG CHUNG THAM KHẢO**:
- 阅读 = Đọc sách / Đọc
- 书源 = Nguồn sách
- 书架 = Kệ sách
- 朗读 = Đọc to / TTS
- 搜索 = Tìm kiếm
- 设置 = Cài đặt
- 导入 = Nhập
- 导出 = Xuất
- 备份 = Sao lưu
- 恢复 = Khôi phục
- 主题 = Giao diện / Theme
- 缓存 = Bộ nhớ đệm

Dữ liệu CSV:
```

### 📱 Prompt có ngữ cảnh:

```
Bạn đang dịch chuỗi giao diện cho "Legado", một ứng dụng đọc sách Android phổ biến.

**BỐI CẢNH TÍNH NĂNG ỨNG DỤNG**:
- Quản lý thư viện sách
- Hỗ trợ nhiều nguồn sách
- Giao diện đọc có thể tùy chỉnh
- TTS (Text-to-Speech - Đọc văn bản thành giọng nói)
- Chỉnh sửa sách trên web
- Chức năng nhập/xuất

**PHONG CÁCH DỊCH**:
- Ngôn ngữ giao diện ứng dụng di động (ngắn gọn, rõ ràng)
- Theo thuật ngữ Android Material Design bằng tiếng Việt
- Thân thiện với người dùng, không quá kỹ thuật
- Nhất quán với các ứng dụng trên Google Play Store

**HƯỚNG DẪN ĐẶC BIỆT**:
- "阅读" trong ngữ cảnh tên ứng dụng = "Legado" hoặc "Đọc sách"
- "书源" = "Nguồn sách" (không phải "Nguồn gốc sách")
- "朗读" = "Đọc to" hoặc "TTS" tùy ngữ cảnh
- Giữ text nút bấm ngắn (dưới 20 ký tự khi có thể)
- Mục menu nên mô tả nhưng ngắn gọn

Vui lòng dịch dữ liệu CSV này:
```

## 🛠️ Câu lệnh xử lý batch tự động

### 1. Tạo prompt file cho tiếng Việt từ batch có sẵn:

```python
# Tạo script Python để tạo prompt tiếng Việt
python -c "
import glob

vietnamese_prompt_template = '''Dịch các chuỗi ứng dụng Legado này từ tiếng Trung sang tiếng Việt:

**DỰ ÁN**: Legado - Ứng dụng đọc sách Android
**BỐI CẢNH**: Ứng dụng đọc sách mã nguồn mở với nguồn sách, TTS, giao diện

**YÊU CẦU**:
- Tiếng Việt tự nhiên, thân thiện
- Giữ định dạng CSV y hệt
- Chỉ điền cột translation
- Giữ nguyên %s, %d, \\n
- Thuật ngữ nhất quán

**TỪ VỰNG CHUNG**:
- 阅读 = Đọc sách
- 书源 = Nguồn sách  
- 书架 = Kệ sách
- 朗读 = Đọc to
- 设置 = Cài đặt
- 搜索 = Tìm kiếm
- 备份 = Sao lưu
- 恢复 = Khôi phục
- 导入 = Nhập
- 导出 = Xuất

Dữ liệu CSV:
'''

# Tạo prompt tiếng Việt cho từng batch
for i in range(1, 118):  # 117 batches
    batch_file = f'batch_{i:03d}.csv'
    try:
        with open(batch_file, 'r', encoding='utf-8') as f:
            csv_content = f.read()
        
        with open(f'vietnamese_prompt_batch_{i:03d}.txt', 'w', encoding='utf-8') as f:
            f.write(vietnamese_prompt_template + csv_content)
        
        print(f'Created vietnamese_prompt_batch_{i:03d}.txt')
    except FileNotFoundError:
        continue
"
```

## 🎨 Ví dụ dịch tham khảo

```csv
id,original_text,vietnamese_translation,context
1,阅读,Đọc sách,Tên ứng dụng
2,书架,Kệ sách,Tab chính
3,搜索,Tìm kiếm,Nút hành động
4,设置,Cài đặt,Mục menu
5,朗读,Đọc to,Tính năng TTS
6,书源管理,Quản lý nguồn sách,Mục menu
7,主题设置,Cài đặt giao diện,Danh mục cài đặt
8,备份与恢复,Sao lưu & Khôi phục,Phần cài đặt
9,离线缓存,Bộ nhớ đệm offline,Tính năng tải về
10,替换净化,Thay thế văn bản,Lọc nội dung
```

## 🔄 Quy trình dịch với AI

### Bước 1: Tạo prompt tiếng Việt
```bash
# Chạy script Python ở trên để tạo vietnamese_prompt_batch_*.txt
```

### Bước 2: Sử dụng với Gemini
Sao chép prompt đã tối ưu ở trên và dán dữ liệu CSV của bạn.

### Bước 3: Lưu bản dịch từ AI
```bash
# Lưu phản hồi AI thành vietnamese_translated_batch_001.csv
```

### Bước 4: Lặp lại cho batch tiếp theo

### Bước 5: Gộp tất cả bản dịch
```bash
python batch_splitter.py merge vietnamese_translated_batch_*.csv --output final_vietnamese_translation.csv
```

## 🎯 Mẹo chất lượng cho dịch tiếng Việt

1. **Cung cấp ngữ cảnh**: Luôn đề cập đây là giao diện ứng dụng Android
2. **Sử dụng batch**: 50-100 entries mỗi lần để có chất lượng tốt nhất
3. **Cụ thể hóa**: Đề cập tính năng của Legado (e-book, TTS, v.v.)
4. **Xem lại thuật ngữ chung**: Đảm bảo nhất quán giữa các batch
5. **Kiểm tra định dạng**: Xác minh cấu trúc CSV được duy trì
6. **Test nhập**: Luôn test batch nhỏ trước

## 🚀 Câu lệnh nhanh cho các AI model khác nhau

### Cho Gemini:
```
Dịch các chuỗi ứng dụng Legado này từ tiếng Trung sang tiếng Việt. Giữ định dạng CSV, điền cột translation:

[DÁN DỮ LIỆU CSV]
```

### Cho ChatGPT:
```
Tôi cần bản dịch tiếng Việt cho các chuỗi giao diện tiếng Trung từ ứng dụng Legado Android. Giữ định dạng CSV và cung cấp bản dịch tự nhiên, thân thiện:

[DÁN DỮ LIỆU CSV]
```

### Cho Claude:
```
Vui lòng dịch các chuỗi tiếng Trung này cho ứng dụng đọc sách Legado Android sang tiếng Việt. Trả về CSV với bản dịch tiếng Việt trong cột translation:

[DÁN DỮ LIỆU CSV]
```

## ⚡ Mẹo Pro

1. **Bắt đầu với batch nhỏ** (20-30 entries) để test chất lượng
2. **Lưu prompt thành công** hoạt động tốt cho AI model của bạn
3. **Tạo từ điển thuật ngữ** từ những bản dịch tốt
4. **Sử dụng cột context** để hướng dẫn quyết định dịch thuật
5. **Kiểm tra kỹ thuật ngữ** và nhãn nút

Phương pháp này sẽ cho bạn bản dịch tiếng Việt chất lượng cao, nhất quán cho toàn bộ dự án Legado! 🎉