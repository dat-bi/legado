#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vietnamese Prompt Generator for Legado Translation
Tạo các prompt file dành riêng cho dịch sang tiếng Việt
"""

import os
import glob
from pathlib import Path

def create_vietnamese_prompts():
    """Tạo prompt files tiếng Việt từ các batch có sẵn"""
    
    vietnamese_prompt_template = """Dịch các chuỗi ứng dụng Legado này từ tiếng Trung sang tiếng Việt:

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
- Giữ nguyên các placeholder như %s, %d, \\n
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
- 刷新 = Làm mới
- 缓存 = Bộ nhớ đệm
- 主题 = Giao diện
- 界面 = Giao diện
- 管理 = Quản lý
- 编辑 = Chỉnh sửa
- 删除 = Xóa
- 添加 = Thêm
- 分享 = Chia sẻ
- 下载 = Tải về
- 更新 = Cập nhật
- 目录 = Mục lục
- 章节 = Chương
- 页面 = Trang
- 字体 = Phông chữ
- 亮度 = Độ sáng
- 背景 = Nền
- 颜色 = Màu sắc

**PHONG CÁCH DỊCH**:
- Ngôn ngữ giao diện mobile (ngắn gọn, rõ ràng)
- Thân thiện, không quá kỹ thuật
- Theo chuẩn Android bằng tiếng Việt
- Text nút bấm ngắn (dưới 20 ký tự)
- Menu items mô tả nhưng súc tích

Dữ liệu CSV cần dịch:
"""

    # Tìm tất cả batch files
    batch_files = sorted(glob.glob('batch_*.csv'))
    
    if not batch_files:
        print("Không tìm thấy batch files. Hãy chạy batch_splitter.py trước.")
        return
    
    created_count = 0
    
    for batch_file in batch_files:
        # Đọc nội dung batch file
        try:
            with open(batch_file, 'r', encoding='utf-8') as f:
                csv_content = f.read()
            
            # Tạo tên file prompt tiếng Việt
            batch_name = Path(batch_file).stem  # batch_001, batch_002, etc.
            vietnamese_prompt_file = f'vietnamese_prompt_{batch_name}.txt'
            
            # Tạo file prompt
            with open(vietnamese_prompt_file, 'w', encoding='utf-8') as f:
                f.write(vietnamese_prompt_template + csv_content)
            
            print(f'✓ Tạo thành công: {vietnamese_prompt_file}')
            created_count += 1
            
        except Exception as e:
            print(f'Lỗi khi xử lý {batch_file}: {e}')
    
    print(f'\n🎉 Hoàn thành! Đã tạo {created_count} prompt files tiếng Việt')
    print(f'📁 Sử dụng các file vietnamese_prompt_*.txt với AI model của bạn')
    print(f'💡 Sau khi dịch, lưu kết quả thành vietnamese_translated_batch_*.csv')

def show_usage_example():
    """Hiển thị ví dụ sử dụng"""
    
    print("""
🇻🇳 HƯỚNG DẪN SỬ DỤNG PROMPT TIẾNG VIỆT

1. Tạo prompt files (đã hoàn thành):
   ✓ vietnamese_prompt_batch_001.txt đến vietnamese_prompt_batch_117.txt

2. Sử dụng với Gemini/ChatGPT/Claude:
   - Mở file vietnamese_prompt_batch_001.txt
   - Copy toàn bộ nội dung
   - Paste vào AI model
   - Lưu phản hồi thành vietnamese_translated_batch_001.csv

3. Lặp lại cho tất cả batches

4. Gộp tất cả bản dịch:
   python batch_splitter.py merge vietnamese_translated_batch_*.csv --output final_vietnamese.csv

5. Áp dụng vào dự án:
   python chinese_text_extractor.py import --input final_vietnamese.csv --format csv

🎯 VÍ DỤ PROMPT CHO GEMINI:
════════════════════════════════════════════════════════════════
Copy nội dung từ vietnamese_prompt_batch_001.txt và paste vào Gemini.

Gemini sẽ trả về CSV với cột translation đã được điền bằng tiếng Việt.

🔄 QUY TRÌNH NHANH:
1. Batch 001 → Gemini → Lưu thành vietnamese_translated_batch_001.csv
2. Batch 002 → Gemini → Lưu thành vietnamese_translated_batch_002.csv
3. ... tiếp tục cho 117 batches
4. Gộp tất cả → Import vào dự án

Dự kiến: ~3-4 giờ để dịch hoàn chỉnh 5,838 entries sang tiếng Việt!
""")

if __name__ == '__main__':
    print("🇻🇳 Tạo prompt files dịch sang tiếng Việt cho Legado")
    print("=" * 60)
    
    # Tạo prompt files
    create_vietnamese_prompts()
    
    # Hiển thị hướng dẫn
    show_usage_example()