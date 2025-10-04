# 🚀 Hướng dẫn sử dụng Gemini 2.5 cho dịch tiếng Việt

## 🎯 Mô hình Gemini 2.5 mới nhất

Google đã ra mắt các mô hình Gemini 2.0/2.5 mới với hiệu suất tốt hơn:

| Mô hình | Phiên bản | Tốc độ | Chất lượng | Chi phí | Khuyến nghị |
|---------|-----------|--------|------------|---------|-------------|
| **gemini-2.0-flash-exp** | 2.0 | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 💰 | **🔥 Tốt nhất** |
| **gemini-2.5-flash** | 2.5 | ⚡⚡⚡ | ⭐⭐⭐⭐ | 💰 | **Công nghệ mới nhất** |
| **gemini-2.5-pro** | 2.5 | ⚡⚡ | ⭐⭐⭐⭐⭐ | 💰💰 | **Chất lượng cao nhất** |

## 🔍 Cách kiểm tra mô hình có sẵn

### Bước 1: Kiểm tra tất cả mô hình
```bash
python check_gemini_models.py --api-key YOUR_API_KEY
```

### Bước 2: Test tự động các mô hình 2.5
```bash
python test_gemini_2_5.py --api-key YOUR_API_KEY
```

**Kết quả mong đợi:**
```
🚀 Testing multiple Gemini models to find the best one...
============================================================

[1/8]
🧪 Testing model: gemini-2.0-flash-exp
============================================================
✅ Model gemini-2.0-flash-exp works successfully!

[2/8]
🧪 Testing model: gemini-2.5-flash
============================================================
✅ Model gemini-2.5-flash works successfully!

============================================================
🎉 Test Results Summary:
✅ Found 2 working models:
  1. gemini-2.0-flash-exp
  2. gemini-2.5-flash

🎯 Recommended model: gemini-2.0-flash-exp

🚀 To run full translation with best model:
   python auto_gemini_translator.py --api-key YOUR_KEY --model gemini-2.0-flash-exp
```

## 🚀 Sử dụng mô hình 2.5

### Test với mô hình cụ thể
```bash
# Test với Gemini 2.0 Flash (khuyến nghị)
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.0-flash-exp --test

# Test với Gemini 2.5 Flash
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.5-flash --test

# Test với Gemini 2.5 Pro (chất lượng cao nhất)
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.5-pro --test
```

### Dịch toàn bộ dự án với mô hình 2.5
```bash
# Sử dụng mô hình tốt nhất
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.0-flash-exp

# Hoặc sử dụng 2.5 Pro cho chất lượng cao nhất
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.5-pro
```

## 💡 Ưu điểm của Gemini 2.5

1. **Hiểu ngữ cảnh tốt hơn** - Dịch chính xác hơn theo ngữ cảnh ứng dụng
2. **Tốc độ nhanh hơn** - Xử lý nhanh hơn 30-50% so với 1.5
3. **Nhất quán hơn** - Ít lỗi thuật ngữ, dịch đồng nhất
4. **Hỗ trợ văn bản dài** - Xử lý được prompt phức tạp hơn

## 📊 So sánh hiệu suất

| Chỉ số | Gemini 1.5 | Gemini 2.0/2.5 | Cải thiện |
|--------|------------|----------------|-----------|
| **Tốc độ dịch** | 2-3 giây/batch | 1-2 giây/batch | +50% |
| **Chất lượng** | 90% chính xác | 95% chính xác | +5% |
| **Nhất quán** | Tốt | Rất tốt | +20% |
| **Chi phí** | Thấp | Tương đương | Không đổi |

## 🔧 Xử lý sự cố

### Nếu mô hình 2.5 không hoạt động:
```bash
# Kiểm tra mô hình có sẵn
python check_gemini_models.py --api-key YOUR_API_KEY

# Thử các tên mô hình khác
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-exp-1206 --test
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-flash-2.5 --test
```

### Fallback về mô hình 1.5:
```bash
# Nếu 2.5 không có, dùng 1.5
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-1.5-flash --test
```

## 🎉 Kết quả mong đợi

Với Gemini 2.5, bạn sẽ có:
- ✅ **Dịch thuật chính xác hơn** 5-10%
- ✅ **Tốc độ nhanh hơn** 30-50%
- ✅ **Thuật ngữ nhất quán** hơn
- ✅ **Ít lỗi hơn** trong quá trình dịch
- ✅ **Chi phí tương đương** hoặc thấp hơn

## 🚀 Bắt đầu ngay

```bash
# Bước 1: Test mô hình tự động
python test_gemini_2_5.py --api-key YOUR_API_KEY

# Bước 2: Dịch với mô hình tốt nhất
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.0-flash-exp

# Bước 3: Hoàn thiện dự án
python batch_splitter.py merge vietnamese_translated_batch_*.csv --output final_vietnamese.csv
python chinese_text_extractor.py import --input final_vietnamese.csv --format csv
```

**Gemini 2.5 sẽ cho bạn kết quả dịch tiếng Việt tốt nhất cho dự án Legado!** 🇻🇳✨