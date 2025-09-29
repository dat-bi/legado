# API của [Legado](/app/src/main/java/io/legado/app/api/controller)

## Cấu hình cho [Web](/app/src/main/java/io/legado/app/web/)

Bạn cần kích hoạt "Dịch vụ Web" trong cài đặt trước.

## Sử dụng

### Web

Các hướng dẫn dưới đây giả sử bạn thực hiện trên máy cục bộ và cổng mở là 1234.  
Nếu bạn muốn truy cập [Legado]() từ máy tính từ xa, hãy thay thế `127.0.0.1` bằng IP điện thoại.

#### Thêm một nguồn sách

Nội dung BODY yêu cầu là chuỗi `JSON`,  
Định dạng tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/BookSource.kt)

```
URL = http://127.0.0.1:1234/saveBookSource
Method = POST
```

#### Thêm nhiều nguồn sách hoặc nguồn đăng ký

Nội dung BODY yêu cầu là chuỗi `JSON`,  
Định dạng tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/BookSource.kt), **là định dạng mảng**.

```
URL = http://127.0.0.1:1234/saveBookSources
URL = http://127.0.0.1:1234/saveRssSources
Method = POST
```

#### Lấy nguồn sách

```
URL = http://127.0.0.1:1234/getBookSource?url=xxx
URL = http://127.0.0.1:1234/getRssSource?url=xxx
Method = GET
```

#### Lấy tất cả nguồn sách hoặc nguồn đăng ký

```
URL = http://127.0.0.1:1234/getBookSources
URL = http://127.0.0.1:1234/getRssSources
Method = GET
```

#### Xóa nhiều nguồn sách hoặc nguồn đăng ký

Nội dung BODY yêu cầu là chuỗi `JSON`,  
Định dạng tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/BookSource.kt), **là định dạng mảng**.

```
URL = http://127.0.0.1:1234/deleteBookSources
URL = http://127.0.0.1:1234/deleteRssSources
Method = POST
```

#### Gỡ lỗi nguồn

key là từ khóa tìm kiếm nguồn sách, tag là liên kết nguồn

```
URL = ws://127.0.0.1:1235/bookSourceDebug
URL = ws://127.0.0.1:1235/rssSourceDebug
Message = { key: [String], tag: [String] }
```

#### Lấy quy tắc thay thế

```
URL = http://127.0.0.1:1234/getReplaceRules
Method = GET
```

#### Quản lý quy tắc thay thế

Nội dung BODY yêu cầu là chuỗi `JSON`,  
Quy tắc thay thế tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/ReplaceRule.kt)。

##### Xóa

```
URL = http://127.0.0.1:1234/deleteReplaceRule
Method = POST
Body = [ReplaceRule]
```

##### Thêm

```
URL = http://127.0.0.1:1234/saveReplaceRule
Method = POST
Body = [ReplaceRule]
```

##### Kiểm tra

Trả về kết quả thay thế văn bản test

```
URL = http://127.0.0.1:1234/testReplaceRule
Method = POST
Body = { rule: [ReplaceRule], text: [String] }
```

#### Tìm kiếm sách trực tuyến

Nếu muốn lấy mục lục nội dung của sách tương ứng, vui lòng **thêm sách** trước để kích hoạt bộ nhớ đệm, nếu sau khi đọc thử quyết định không thêm vào sách, vui lòng **xóa sách**

```
URL = ws://127.0.0.1:1235/searchBook
Message = { key: [String] }
```

#### Thêm sách

Nội dung BODY yêu cầu là chuỗi `JSON`,  
Định dạng tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/Book.kt)。

```
URL = http://127.0.0.1:1234/saveBook
Method = POST
```

#### Xóa sách

```
URL = http://127.0.0.1:1234/deleteBook
Method = POST
```

#### Lấy tất cả sách

```
URL = http://127.0.0.1:1234/getBookshelf
Method = GET
```

Lấy tất cả sách trong APP。

#### Lấy danh sách chương sách

```
URL = http://127.0.0.1:1234/getChapterList?url=xxx
Method = GET
```

Lấy danh sách chương của sách được chỉ định。

#### Lấy nội dung sách

```
URL = http://127.0.0.1:1234/getBookContent?url=xxx&index=1
Method = GET
```

Lấy nội dung văn bản chương `index` của sách được chỉ định。

#### Lấy ảnh bìa

```
URL = http://127.0.0.1:1234/cover?path=xxxxx
Method = GET
```

#### Lấy hình ảnh nội dung

```
URL = http://127.0.0.1:1234/image?url=${bookUrl}&path=${picUrl}&width=${width}
Method = GET
```

#### Lưu tiến độ sách

Nội dung BODY yêu cầu là chuỗi `JSON`,  
Định dạng tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/BookProgress.kt)。

```
URL = http://127.0.0.1:1234/saveBookProgress
Method = POST
```

### [Content Provider](/app/src/main/java/io/legado/app/api/ReaderProvider.kt)

- Cần khai báo quyền `io.legado.READ_WRITE`
- `providerHost` là `đói gói.readerProvider`, ví dụ `io.legado.app.release.readerProvider`, địa chỉ các gói khác nhau khác nhau, để tránh xung đột cài đặt thất bại
- Các `providerHost` xuất hiện dưới đây vui lòng tự thay thế

#### Thêm một nguồn sách hoặc nguồn đăng ký

Tạo `ContentValues` với `Key="json"`, nội dung là chuỗi `JSON`,  
Định dạng tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/BookSource.kt)

```
URL = content://providerHost/bookSource/insert
URL = content://providerHost/rssSource/insert
Method = insert
```

#### Thêm nhiều nguồn sách hoặc nguồn đăng ký

Tạo `ContentValues` với `Key="json"`, nội dung là chuỗi `JSON`,  
Định dạng tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/BookSource.kt), **là định dạng mảng**。

```
URL = content://providerHost/bookSources/insert
URL = content://providerHost/rssSources/insert
Method = insert
```

#### Lấy nguồn sách hoặc nguồn đăng ký

Lấy thông tin nguồn sách tương ứng với URL được chỉ định。  
Dùng `Cursor.getString(0)` để lấy kết quả trả về。

```
URL = content://providerHost/bookSource/query?url=xxx
URL = content://providerHost/rssSource/query?url=xxx
Method = query
```

#### Lấy tất cả nguồn sách hoặc nguồn đăng ký

Lấy tất cả nguồn đăng ký trong APP。  
Dùng `Cursor.getString(0)` để lấy kết quả trả về。

```
URL = content://providerHost/bookSources/query
URL = content://providerHost/rssSources/query
Method = query
```

#### Xóa nhiều nguồn sách hoặc nguồn đăng ký

Tạo `ContentValues` với `Key="json"`, nội dung là chuỗi `JSON`,  
Định dạng tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/BookSource.kt), **là định dạng mảng**。

```
URL = content://providerHost/bookSources/delete
URL = content://providerHost/rssSources/delete
Method = delete
```

#### Thêm sách

Tạo `ContentValues` với `Key="json"`, nội dung là chuỗi `JSON`,  
Định dạng tham khảo [file này](/app/src/main/java/io/legado/app/data/entities/Book.kt)。

```
URL = content://providerHost/book/insert
Method = insert
```

#### Lấy tất cả sách

Lấy tất cả sách trong APP。  
Dùng `Cursor.getString(0)` để lấy kết quả trả về。

```
URL = content://providerHost/books/query
Method = query
```

#### Lấy danh sách chương sách

Lấy danh sách chương của sách được chỉ định。  
Dùng `Cursor.getString(0)` để lấy kết quả trả về。

```
URL = content://providerHost/book/chapter/query?url=xxx
Method = query
```

#### Lấy nội dung sách

Lấy nội dung văn bản chương `index` của sách được chỉ định。  
Dùng `Cursor.getString(0)` để lấy kết quả trả về。

```
URL = content://providerHost/book/content/query?url=xxx&index=1
Method = query
```

#### Lấy ảnh bìa

```
URL = content://providerHost/book/cover/query?path=xxxx
Method = query
```
