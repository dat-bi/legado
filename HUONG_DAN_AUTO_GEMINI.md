# 🤖 Hướng dẫn sử dụng Auto Gemini Translator

## 🎯 Tổng quan

Tool tự động này sẽ sử dụng Gemini API để dịch **tất cả 117 batches** từ tiếng Trung sang tiếng Việt mà không cần copy-paste thủ công!

## 🔧 Cài đặt nhanh

### Cách 1: Sử dụng script tự động (Khuyến nghị)
```bash
setup_auto_translator.bat
```

### Cách 2: Cài đặt thủ công
```bash
# 1. Cài đặt dependencies
pip install requests

# 2. Lấy API key từ https://aistudio.google.com/app/apikey
```

## 🚀 Sử dụng

### Bước 0: Kiểm tra models có sẵn
```bash
python check_gemini_models.py --api-key YOUR_API_KEY
```

### Test thử với 3 batches đầu tiên
```bash
python auto_gemini_translator.py --api-key YOUR_API_KEY --test
```

### Dịch tất cả 117 batches
```bash
python auto_gemini_translator.py --api-key YOUR_API_KEY
```

### Sử dụng model cụ thể
```bash
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-1.5-pro
```

### Dịch từ batch cụ thể
```bash
# Dịch batch 1-20
python auto_gemini_translator.py --api-key YOUR_API_KEY --start 1 --end 20

# Dịch batch 50-117
python auto_gemini_translator.py --api-key YOUR_API_KEY --start 50 --end 117
```

### Tùy chỉnh tốc độ (tránh rate limit)
```bash
# Chờ 5 giây giữa các request
python auto_gemini_translator.py --api-key YOUR_API_KEY --delay 5.0
```

## 🎯 Tính năng chính

- ✅ **Tự động xử lý** 117 Vietnamese prompt files
- ✅ **Gọi Gemini API** với error handling thông minh
- ✅ **Kiểm tra chất lượng** bản dịch tự động
- ✅ **Xử lý rate limiting** với auto retry
- ✅ **Theo dõi tiến độ** real-time
- ✅ **Recovery mode** cho các batch bị lỗi

## 📊 Kết quả mong đợi

| Thông số | Giá trị |
|----------|---------|
| **Tổng batches** | 117 batches |
| **Entries per batch** | 50 entries |
| **Tổng entries** | 5,838 Chinese→Vietnamese |
| **Thời gian dự kiến** | 3-5 giờ |
| **Tỷ lệ thành công** | >95% |
| **Chi phí** | Rất thấp (~$2-5) |

## 📁 Files được tạo ra

Sau khi chạy tool, bạn sẽ có:
- `vietnamese_translated_batch_001.csv` đến `vietnamese_translated_batch_117.csv`
- Mỗi file chứa 50 bản dịch hoàn chỉnh

## 🔄 Hoàn thiện quy trình

### 1. Gộp tất cả bản dịch
```bash
python batch_splitter.py merge vietnamese_translated_batch_*.csv --output final_vietnamese.csv
```

### 2. Import vào dự án
```bash
python chinese_text_extractor.py import --input final_vietnamese.csv --format csv
```

### 3. Kiểm tra kết quả
```bash
python chinese_text_extractor.py validate
```

## 📝 Ví dụ thực tế

### Chạy test mode trước
```bash
C:\Users\Admin\Downloads\legado> python auto_gemini_translator.py --api-key AIza... --test

🧪 Test mode: Processing only first 3 batches
🚀 Starting automated Vietnamese translation
📁 Processing batches 1 to 3
📊 Total batches: 3
⏱ Delay between requests: 2.0 seconds
============================================================

[1/3] ----------------------------------------
📝 Processing vietnamese_prompt_batch_001...
  Expected entries: 50
  Calling Gemini API (attempt 1/3)...
  ✓ API call successful
  ✓ Saved: vietnamese_translated_batch_001.csv
  ⏱ Waiting 2.0 seconds before next batch...

[2/3] ----------------------------------------
📝 Processing vietnamese_prompt_batch_002...
  Expected entries: 50
  Calling Gemini API (attempt 1/3)...
  ✓ API call successful
  ✓ Saved: vietnamese_translated_batch_002.csv
  ⏱ Waiting 2.0 seconds before next batch...

[3/3] ----------------------------------------
📝 Processing vietnamese_prompt_batch_003...
  Expected entries: 50
  Calling Gemini API (attempt 1/3)...
  ✓ API call successful
  ✓ Saved: vietnamese_translated_batch_003.csv

============================================================
🎉 Translation completed!
✅ Successfully translated: 3 batches
❌ Failed batches: 0
⏱ Total time: 0.5 minutes

🔄 Next steps:
1. Review translated files: vietnamese_translated_batch_*.csv
2. Merge all translations:
   python batch_splitter.py merge vietnamese_translated_batch_*.csv --output final_vietnamese.csv
3. Import to project:
   python chinese_text_extractor.py import --input final_vietnamese.csv --format csv
```

### Chạy full translation
```bash
C:\Users\Admin\Downloads\legado> python auto_gemini_translator.py --api-key AIza...

🚀 Starting automated Vietnamese translation
📁 Processing batches 1 to 117
📊 Total batches: 117
⏱ Delay between requests: 2.0 seconds
============================================================

[1/117] ----------------------------------------
📝 Processing vietnamese_prompt_batch_001...
✅ Successfully translated: 1 batches
...
[117/117] ----------------------------------------
📝 Processing vietnamese_prompt_batch_117...
✅ Successfully translated: 117 batches

============================================================
🎉 Translation completed!
✅ Successfully translated: 117 batches
❌ Failed batches: 0
⏱ Total time: 245.3 minutes
```

## 🛡️ Tính năng an toàn

- **Smart retry**: Tự động thử lại khi gặp lỗi
- **Rate limit protection**: Tránh spam API
- **CSV validation**: Kiểm tra chất lượng dịch thuật
- **Progress tracking**: Biết được đang ở đâu
- **Resume capability**: Có thể tiếp tục từ batch bất kỳ

## 🔧 Xử lý sự cố

### Lỗi model không tìm thấy:
```bash
# Kiểm tra models có sẵn trước
python check_gemini_models.py --api-key YOUR_API_KEY

# Sử dụng model được hỗ trợ
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-1.5-flash
```

### Lỗi rate limit
```bash
# Tăng delay giữa các request
python auto_gemini_translator.py --api-key YOUR_API_KEY --delay 10.0
```

### Một số batch bị lỗi
```bash
# Re-run những batch cụ thể
python auto_gemini_translator.py --api-key YOUR_API_KEY --start 45 --end 50
```

### API key không hợp lệ
- Kiểm tra lại API key đã copy đúng chưa
- Vào [Google AI Studio](https://aistudio.google.com/app/apikey) tạo key mới
- Đảm bảo account có quyền sử dụng Gemini API

## 💡 Tips hay

1. **Luôn test trước**: Chạy `--test` mode trước khi dịch tất cả
2. **Monitor tiến độ**: Tool hiển thị real-time progress
3. **Kiểm tra chất lượng**: Review vài file đầu tiên
4. **Resume từ lỗi**: Có thể restart từ batch bất kỳ
5. **Tối ưu chi phí**: Dùng `--delay` để kiểm soát tần suất API

## 🎉 Kết quả cuối cùng

Sau khi hoàn thành, bạn sẽ có:
- ✅ Ứng dụng Legado hoàn toàn tiếng Việt
- ✅ 5,838 text entries được dịch chính xác
- ✅ Thuật ngữ nhất quán trong toàn bộ app
- ✅ UI thân thiện với người dùng Việt Nam

**Tool này sẽ tiết kiệm cho bạn hàng giờ copy-paste thủ công!** 🚀

### Bắt đầu ngay:
```bash
python auto_gemini_translator.py --api-key YOUR_API_KEY --test
```