# 🇻🇳 HƯỚNG DẪN DỊCH TIẾNG VIỆT HOÀN CHỈNH CHO LEGADO

## ✅ Tình trạng hiện tại

Tool đã sẵn sàng! Đã tìm thấy **5,838 text tiếng Trung** và tạo **117 prompt files tiếng Việt** cho Gemini AI.

## 📁 Các file có sẵn

- ✅ `vietnamese_prompt_batch_001.txt` đến `vietnamese_prompt_batch_117.txt` - Sẵn sàng cho Gemini
- ✅ Tất cả tools và tài liệu đã được tạo
- ✅ Từ điển thuật ngữ chuẩn đã được tích hợp

## 🚀 CÁCH SỬ DỤNG GEMINI AI CHO DỊCH TIẾNG VIỆT

### Bước 1: Mở prompt đầu tiên
1. Mở file `vietnamese_prompt_batch_001.txt` 
2. **Copy toàn bộ nội dung** (Ctrl+A, Ctrl+C)
3. Vào [Gemini AI](https://gemini.google.com)
4. **Paste prompt** (Ctrl+V)
5. Nhấn Enter và đợi Gemini phản hồi

### Bước 2: Lưu kết quả từ Gemini
1. Gemini sẽ trả về CSV với bản dịch tiếng Việt
2. **Copy toàn bộ CSV response** từ Gemini
3. Tạo file mới tên `vietnamese_translated_batch_001.csv`
4. **Paste và save** CSV response

### Bước 3: Lặp lại cho tất cả batches
- `vietnamese_prompt_batch_002.txt` → Lưu thành `vietnamese_translated_batch_002.csv`
- `vietnamese_prompt_batch_003.txt` → Lưu thành `vietnamese_translated_batch_003.csv`
- ... tiếp tục cho tất cả 117 batches

### Bước 4: Gộp tất cả bản dịch
```bash
python batch_splitter.py merge vietnamese_translated_batch_*.csv --output final_vietnamese.csv
```

### Bước 5: Áp dụng vào dự án
```bash
python chinese_text_extractor.py import --input final_vietnamese.csv --format csv
```

## 💡 VÍ DỤ CUỘC TRÒ CHUYỆN VỚI GEMINI

**Bạn paste vào Gemini:**
```
Dịch các chuỗi ứng dụng Legado này từ tiếng Trung sang tiếng Việt:

**DỰ ÁN**: Legado - Ứng dụng đọc sách Android mã nguồn mở
**BỐI CẢNH**: Ứng dụng đọc sách với các tính năng:
- Quản lý nguồn sách
- Giao diện đọc tùy chỉnh
- Text-to-Speech (TTS)
- Nhập/Xuất dữ liệu
- Dịch vụ web

**YÊU CẦU DỊCH**:
- Tiếng Việt tự nhiên, thân thiện với người dùng mobile
- Giữ định dạng CSV hoàn toàn giống nhau
- Chỉ điền cột "translation"
- Giữ nguyên các placeholder như %s, %d, \n
- Sử dụng thuật ngữ nhất quán

**TỪ VỰNG CHUẨN**:
- 阅读 = Đọc sách
- 书源 = Nguồn sách
- 书架 = Kệ sách
- 朗读 = Đọc to / TTS
- 搜索 = Tìm kiếm
- 设置 = Cài đặt
- 导入 = Nhập
- 导出 = Xuất
- 备份 = Sao lưu
- 恢复 = Khôi phục

Dữ liệu CSV cần dịch:
id,type,file_path,line_number,string_name,original_text,translation,context,notes
1,xml_string,app\src\main\res\values-zh\strings.xml,3,app_name,阅读,,String resource: app_name,Chinese parts: 阅读
2,xml_string,app\src\main\res\values-zh\strings.xml,46,bookshelf,书架,,String resource: bookshelf,Chinese parts: 书架
... (50 entries total)
```

**Gemini sẽ trả về:**
```csv
id,type,file_path,line_number,string_name,original_text,translation,context,notes
1,xml_string,app\src\main\res\values-zh\strings.xml,3,app_name,阅读,Đọc sách,String resource: app_name,Chinese parts: 阅读
2,xml_string,app\src\main\res\values-zh\strings.xml,46,bookshelf,书架,Kệ sách,String resource: bookshelf,Chinese parts: 书架
... (tất cả entries với bản dịch tiếng Việt)
```

## ⚡ MẸO HIỆU QUẢ

### 1. Làm theo phiên
- Làm 10-20 batches mỗi phiên để tránh mệt mỏi
- Nghỉ giải lao để duy trì chất lượng dịch

### 2. Kiểm tra vài batch đầu
Trước khi làm hết 117 batches:
1. Hoàn thành batches 1-3
2. Gộp và test:
   ```bash
   python batch_splitter.py merge vietnamese_translated_batch_001.csv vietnamese_translated_batch_002.csv vietnamese_translated_batch_003.csv --output test_vietnamese.csv
   python chinese_text_extractor.py import --input test_vietnamese.csv --format csv
   ```
3. Nếu chất lượng tốt, tiếp tục với các batches còn lại

### 3. Các lệnh kiểm soát chất lượng
Nếu Gemini dịch không nhất quán, thêm vào prompt:
```
KIỂM TRA TÍNH NHẤT QUÁN: Đảm bảo các thuật ngữ này luôn được dịch giống nhau:
- 阅读 = "Đọc sách" (ngữ cảnh ứng dụng)
- 书源 = "Nguồn sách" 
- 设置 = "Cài đặt"
- 朗读 = "Đọc to"
- 搜索 = "Tìm kiếm"
```

## 🔧 XỬ LÝ SỰ CỐ

### Nếu Gemini trả về sai định dạng:
**Nói:** "Vui lòng trả về đúng định dạng CSV với tất cả cột nguyên vẹn, chỉ điền cột translation."

### Nếu bản dịch không nhất quán:
**Nói:** "Vui lòng đảm bảo 书源 luôn được dịch là 'Nguồn sách' và 设置 là 'Cài đặt'. Điều chỉnh lại cho nhất quán."

### Nếu Gemini dừng giữa chừng:
**Nói:** "Vui lòng tiếp tục với các entries còn lại của CSV."

## 📊 TỪNG BƯỚC CHI TIẾT

### Chuẩn bị (đã hoàn thành)
```bash
# Đã tạo sẵn tất cả files cần thiết
✓ 117 vietnamese_prompt_batch_*.txt files
✓ Từ điển thuật ngữ tích hợp trong mỗi prompt
✓ Hướng dẫn rõ ràng cho AI
```

### Thực hiện dịch
```bash
# 1. Mở vietnamese_prompt_batch_001.txt
# 2. Copy → Paste vào Gemini
# 3. Lưu response thành vietnamese_translated_batch_001.csv
# 4. Lặp lại cho 117 batches
```

### Hoàn thiện
```bash
# Gộp tất cả
python batch_splitter.py merge vietnamese_translated_batch_*.csv --output final_vietnamese.csv

# Import vào dự án
python chinese_text_extractor.py import --input final_vietnamese.csv --format csv

# Kiểm tra kết quả
python chinese_text_extractor.py validate
```

## 🎯 TỪ ĐIỂN THUẬT NGỮ CHUẨN

| Tiếng Trung | Tiếng Việt | Ngữ cảnh |
|-------------|------------|----------|
| 阅读 | Đọc sách | Tên app / Tính năng chính |
| 书源 | Nguồn sách | Quản lý sources |
| 书架 | Kệ sách | Thư viện cá nhân |
| 朗读 | Đọc to | Tính năng TTS |
| 搜索 | Tìm kiếm | Chức năng search |
| 设置 | Cài đặt | Settings menu |
| 导入 | Nhập | Import function |
| 导出 | Xuất | Export function |
| 备份 | Sao lưu | Backup |
| 恢复 | Khôi phục | Restore |
| 主题 | Giao diện | Theme/UI |
| 缓存 | Bộ nhớ đệm | Cache |
| 管理 | Quản lý | Management |
| 编辑 | Chỉnh sửa | Edit |
| 删除 | Xóa | Delete |
| 添加 | Thêm | Add |
| 分享 | Chia sẻ | Share |
| 下载 | Tải về | Download |
| 更新 | Cập nhật | Update |
| 目录 | Mục lục | Table of contents |
| 章节 | Chương | Chapter |

## 📈 THỐNG KÊ DỰ KIẾN

- **Tổng entries**: 5,838
- **Số batches**: 117 (50 entries/batch)
- **Thời gian dự kiến**: 3-4 giờ
- **Chất lượng**: Cao (nhờ context và từ điển thuật ngữ)

## 🏆 KẾT QUẢ MONG ĐỢI

Sau khi hoàn thành, bạn sẽ có:
- ✅ Ứng dụng Legado hoàn toàn tiếng Việt
- ✅ Thuật ngữ nhất quán trong toàn bộ app
- ✅ Giao diện thân thiện với người dùng Việt Nam
- ✅ Tất cả tính năng được dịch chính xác

**Sẵn sàng để dịch 5,838 entries sang tiếng Việt!** 🇻🇳

Bắt đầu với: Mở `vietnamese_prompt_batch_001.txt` → Copy → Paste vào Gemini!