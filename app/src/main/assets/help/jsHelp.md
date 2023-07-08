# js lượng biến đổi cùng hàm số

Sách nguyên quy tắc bên trong sử dụng js có thể phỏng vấn phía dưới lượng biến đổi
> java lượng biến đổi - Trước mắt loại
> baseUrl lượng biến đổi - Trước mắt url,String
> result lượng biến đổi - Bên trên một bước kết quả
> book lượng biến đổi -[ Sách loại ](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/data/entities/Book.kt)> chapter lượng biến đổi -[ Trước mắt mục lục loại ](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/data/entities/BookChapter.kt)> source lượng biến đổi -[ Cơ sở sách nguyên loại ](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/data/entities/BaseSource.kt)> cookie lượng biến đổi -[cookie thao tác loại ](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/http/CookieStore.kt)> cache lượng biến đổi -[ Cache thao tác loại ](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/CacheManager.kt)> title lượng biến đổi - Trước mắt tiêu đề,String
> src nội dung, nguyên mã
> nextChapterUrl lượng biến đổi Chương sau tiết url
## Trước mắt loại đối tượng có thể sử dụng bộ phận phương pháp
### [AnalyzeUrl](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/model/analyzeRule/AnalyzeUrl.kt) bộ phận hàm số
> js bên trong thông qua java. Điều động, chỉ ở ` Đăng lục kiểm tra JS` Quy tắc bên trong hữu hiệu
```
initUrl() // một lần nữa phân tích url, có thể dùng tại đăng lục kiểm trắc js đăng lục sau một lần nữa phân tích url một lần nữa phỏng vấn

getHeaderMap().putAll(source.getHeaderMap(true)) // thiết trí cái mới đăng lục đầu

getStrResponse( jsStr: String? null, sourceRegex: String? null) // trở về phỏng vấn kết quả, văn bản loại hình, sách nguyên nội bộ một lần nữa đăng lục sau có thể thuyên chuyển này phương pháp một lần nữa trở về kết quả

getResponse(): Response // trở về phỏng vấn kết quả, internet đọc chậm động cơ áp dụng chính là cái này, điều động đăng lục sau tại điều động phương pháp kia có thể một lần nữa phỏng vấn, tham khảo A Lí mây đăng lục kiểm trắc
```### [AnalyzeRule](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/model/analyzeRule/AnalyzeRule.kt) bộ phận hàm số
* Thu hoạch văn bản / văn bản danh sách
> `mContent` Chờ phân tích mật mã gốc, thừa nhận làm trước mắt giao diện
> `isUrl` Kết nối tiêu chí, thừa nhận làm `false````
java.getString(ruleStr: String?, mContent: Any? null, isUrl: Boolean false)
java.getStringList(ruleStr: String?, mContent: Any? null, isUrl: Boolean false)```* Thiết trí phân tích nội dung
```
java.setContent(content: Any?, baseUrl: String? null):```* Thu hoạch Element/Element danh sách
> Nếu như phải cải biến phân tích mật mã gốc, thỉnh sử dụng trước `java.setContent````
java.getElement(ruleStr: String)
java.getElements(ruleStr: String)```* Một lần nữa lùng tìm sách / một lần nữa thu hoạch mục lục url
> Có thể tại đổi mới mục lục phía trước sử dụng, có chút sách nguyên sách địa chỉ cùng mục lục url sẽ thành
```
java.reGetBook()
java.refreshTocUrl()```* Lượng biến đổi tồn lấy
```
java.get(key)
java.put(key, value)```### [js mở rộng loại ](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/JsExtensions.kt) bộ phận hàm số
* Internet thỉnh cầu
```
java.ajax(urlStr): String

java.ajaxAll(urlList: Array): Array
// trở về Response phương pháp body() code() message() header() raw() toString()
java.connect(urlStr): StrResponse

java.post(url: String, body: String, headerMap: Map): Connection.Response

java.get(url: String, headerMap: Map): Connection.Response

java.head(url: String, headerMap: Map): Connection.Response
* Sử dụng webView phỏng vấn internet
* @param html trực tiếp dùng webView ghi vào html, nếu như html vì khoảng không trực tiếp phỏng vấn url
* @param url html bên trong nếu có tương đối đường tắt tài nguyên không truyền vào url phỏng vấn không được
* @param js dùng để lấy trở về giá trị js câu nói, không có liền trở về toàn bộ mật mã gốc
* @return trở về js lấy được nội dung

java.webView(html: String?, url: String?, js: String?): String
* Sử dụng nội trí trình duyệt mở ra kết nối, có thể dùng ở thu hoạch nghiệm chứng mã Thủ động nghiệm chứng website phòng bò
* @param url muốn mở ra kết nối
* @param title trình duyệt tiêu đề

java.startBrowser(url: String, title: String)* Sử dụng nội trí trình duyệt mở ra kết nối, đồng thời chờ đợi website kết quả .body() thu hoạch website nội dung

java.startBrowserAwait(url: String, title: String): StrResponse
```* Điều chỉnh thử
```
java.log(msg)
java.logType(var)```* Thu hoạch người sử dụng truyền vào nghiệm chứng mã
```
java.getVerificationCode(imageUrl)```* Pop-up nhắc nhở
```
java.longToast(msg: Any?)
java.toast(msg: Any?)```* Từ internet ( Từ java.cacheFile thực hiện ), bản địa đọc đến JavaScript văn kiện, dẫn vào trên dưới văn thỉnh thủ động `eval(String(...))````
java.importScript(url)// tương đối đường đi ủng hộ android/data/{package}/cache

java.importScript(relativePath)
java.importScript(absolutePath)```* Cache internet văn kiện
```
Thu hoạch

java.cacheFile(url)
java.cacheFile(url,saveTime)
Thi hành nội dung

eval(String(java.cacheFile(url)))
Xóa bỏ cache văn kiện

cache.delete(java.md5Encode16(url))```* Thu hoạch internet áp súc trong văn kiện mặt chỉ định đường tắt số liệu * Có thể thay đổi Zip Rar 7Z
```
java.get*StringContent(url: String, path: String): String

java.get*StringContent(url: String, path: String, charsetName: String): String

java.get*ByteArrayContent(url: String, path: String): ByteArray?```* base64
> flags tham số có thể tiết kiệm hơi, ngầm thừa nhận Base64.NO_WRAP, xem xét [flags tham số chứng minh ](https://blog.csdn.net/zcmain/article/details/97051870)```
java.base64Decode(str: String)
java.base64Decode(str: String, charset: String)
java.base64DecodeToByteArray(str: String, flags: Int)
java.base64Encode(str: String, flags: Int)```* ByteArray
```
Str chuyển Bytes

java.strToBytes(str: String)
java.strToBytes(str: String, charset: String)
Bytes chuyển Str

java.bytesToStr(bytes: ByteArray)
java.bytesToStr(bytes: ByteArray, charset: String)```* Hex
```
HexString giải mã vì tự tiết mấy tổ

java.hexDecodeToByteArray(hex: String)
hexString giải mã vì utf8String

java.hexDecodeToString(hex: String)
utf8 mã hóa vì hexString

java.hexEncodeToString(utf8: String)```* Tiêu chí id
```
java.randomUUID()
java.androidId()```* Phồn giản chuyển đổi
```
Đem văn bản chuyển đổi thành giản thể

java.t2s(text: String): String

Đem văn bản chuyển đổi thành phồn thể

java.s2t(text: String): String
```* Văn kiện
> Tất cả đối với văn kiện đọc viết xóa thao tác đều là tương đối đường đi, chỉ có thể thao tác đọc cache /android/data/{package}/cache/ bên trong văn kiện
```// dưới văn kiện tái url dùng tạo ra văn kiện tên, trở về văn kiện đường đi

downloadFile(url: String): String
// văn kiện bớt áp lực,zipPath vì áp súc văn kiện đường đi, trở về bớt áp lực đường đi

unArchiveFile(zipPath: String): String

unzipFile(zipPath: String): String

unrarFile(zipPath: String): String

un7zFile(zipPath: String): String
// cặp văn kiện bên trong tất cả văn kiện đọc đến

getTxtInFolder(unzipPath: String): String
// đọc đến văn bản văn kiện

readTxtFile(path: String): String
// xóa bỏ văn kiện

deleteFile(path: String)```### [js thêm giải mã loại ](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/JsEncodeUtils.kt) bộ phận hàm số
> Cung cấp tại JavaScript trong hoàn cảnh mau lẹ điều động crypto phép tính hàm số, từ [hutool-crypto](https://www.hutool.cn/docs/#/crypto/ tường thuật tóm lược ) thực hiện
> Khác không có tăng thêm phép tính nhưng tại JavaScript bên trong sử dụng `JavaImporter`[ Điều động ](https://m.jb51.net/article/92138.htm)Java, ví dụ có thể tham khảo ` Đọc chậm động cơ - A Lí mây giọng nói `> Chú ý: Nếu như truyền vào tham số không phải Utf8String có thể trước tiên điều động `java.hexDecodeToByteArray java.base64DecodeToByteArray` Chuyển thành ByteArray
* Đối xứng mã hóa
> Đưa vào tham số key iv ủng hộ ByteArray|**Utf8String**```// sáng tạo Cipher

java.createSymmetricCrypto(transformation, key, iv)```> Giải mã mã hóa tham số data ủng hộ ByteArray|Base64String|HexString|InputStream
```// giải mã vì ByteArray String

cipher.decrypt(data)
cipher.decryptStr(data)// mã hóa vì ByteArray Base64 ký tự HEX ký tự

cipher.encrypt(data)
cipher.encryptBase64(data)
cipher.encryptHex(data)```* Không đối với xưng mã hóa
> Đưa vào tham số key ủng hộ ByteArray|**Utf8String**```// sáng tạo cipher

java.createAsymmetricCrypto(transformation)// thiết trí chìa khóa bí mật
.setPublicKey(key).setPrivateKey(key)```> Giải mã mã hóa tham số data ủng hộ ByteArray|Base64String|HexString|InputStream
```// giải mã vì ByteArray String

cipher.decrypt(data, usePublicKey: Boolean? true
)
cipher.decryptStr(data, usePublicKey: Boolean? true
)// mã hóa vì ByteArray Base64 ký tự HEX ký tự

cipher.encrypt(data, usePublicKey: Boolean? true
)
cipher.encryptBase64(data, usePublicKey: Boolean? true
)
cipher.encryptHex(data, usePublicKey: Boolean? true
)```* Ký tên
> Đưa vào tham số key ủng hộ ByteArray|**Utf8String**```// sáng tạo Sign

java.createSign(algorithm)// thiết trí chìa khóa bí mật
.setPublicKey(key).setPrivateKey(key)```> Ký tên tham số data ủng hộ ByteArray|inputStream|String
```// ký tên thu phát ByteArray HexString

sign.sign(data)
sign.signHex(data)```* Trích yếu
```
java.digestHex(data: String, algorithm: String,): String?
java.digestBase64Str(data: String, algorithm: String,): String?```* md5
```
java.md5Encode(str)
java.md5Encode16(str)```* HMac
```
java.HMacHex(data: String, algorithm: String, key: String): String

java.HMacBase64(data: String, algorithm: String, key: String): String
```## book đối tượng có thể dùng thuộc tính
### Thuộc tính
> Phương pháp sử dụng: Tại js bên trong hoặc {{}} Bên trong sử dụng book. Thuộc tính phương thức liền có thể thu hoạch. Như tại nội dung sau tăng thêm ##{{book.name+" Cuốn "+title}} Có thể tịnh hóa Tên sách + Cuốn + Tên chương xưng ( Như Ta là đại minh tinh cuốn Chương 02: cha ta là hào môn tổng giám đốc ) loại này ký tự.```
bookUrl // tường tình trang Url( Bản địa sách nguyên tồn trữ hoàn chỉnh văn kiện đường đi )
tocUrl // trang mục lục Url (toc=table of Contents)
origin // sách nguyên URL( Ngầm thừa nhận BookType.local)
originName // sách nguyên tên or bản địa sách văn kiện tên

name // sách tên ( Sách nguyên thu hoạch )
author // tên tác giả xưng ( Sách nguyên thu hoạch )
kind // phân loại tin tức ( Sách nguyên thu hoạch )
customTag // phân loại tin tức ( Người sử dụng sửa chữa )
coverUrl // trang bìa Url( Sách nguyên thu hoạch )
customCoverUrl // trang bìa Url( Người sử dụng sửa chữa )
intro // giới thiệu vắn tắt nội dung ( Sách nguyên thu hoạch )
customIntro // giới thiệu vắn tắt nội dung ( Người sử dụng sửa chữa )
charset // tự định nghĩa ký tự tụ tập tên ( Vẻn vẹn thích hợp với bản địa sách )
type // 0:text 1:audio

group // tự định nghĩa phân tổ hướng dẫn tra cứu hào

latestChapterTitle // chương mới nhất tiêu đề

latestChapterTime // chương mới nhất tiêu đề thời gian đổi mới

lastCheckTime // lần gần đây nhất càng sách mới tịch tin tức thời gian

lastCheckCount // lần gần đây nhất phát hiện chương tiết mới số lượng

totalChapterNum // sách mục lục tổng số

durChapterTitle // trước mắt tên chương xưng

durChapterIndex // trước mắt chương tiết hướng dẫn tra cứu

durChapterPos // trước mắt đọc tiến độ ( Bài hàng chữ phù hướng dẫn tra cứu vị trí )
durChapterTime // lần gần đây nhất đọc sách thời gian ( Mở ra thời gian )
canUpdate // đổi mới giá sách lúc càng sách mới tịch tin tức

order // thủ động sắp xếp

originOrder // sách nguyên sắp xếp

variable // tự định nghĩa sách lượng biến đổi tin tức ( Dùng sách nguyên quy tắc kiểm tra sách tin tức )```## chapter đối tượng bộ phận có thể dùng thuộc tính
> Phương pháp sử dụng: Tại js bên trong hoặc {{}} Bên trong sử dụng chapter. Thuộc tính phương thức liền có thể thu hoạch. Như tại nội dung sau tăng thêm ##{{chapter.title+chapter.index}} Có thể tịnh hóa Chương tiết tiêu đề + Số thứ tự ( Như Chương 02: Thiên tiên hạ phàm 2) loại này ký tự.```
url // chương tiết địa chỉ

title // chương tiết tiêu đề

baseUrl // dùng để ghép lại tương đối url

bookUrl // sách địa chỉ

index // chương tiết số thứ tự

resourceUrl // âm tần chân thực URL

tag //
start // chương tiết mở đầu vị trí

end // chương tiết kết thúc vị trí

variable // lượng biến đổi
```## source đối tượng bộ phận có thể dùng hàm số
* Thu hoạch sách nguyên url
```
source.getKey()```* Sách nguyên lượng biến đổi tồn lấy
```
source.setVariable(variable: String?)
source.getVariable()```* Đăng lục đầu thao tác
```
source.getLoginHeader()
source.getLoginHeaderMap().get(key: String)
source.putLoginHeader(header: String)
source.removeLoginHeader()```* Người sử dụng đăng lục tin tức thao tác
> Sử dụng ` Đăng lục UI` Quy tắc, đồng thời thành công đăng lục, đọc tự động mã hóa bảo tồn đăng lục UI quy tắc bên trong trừ type vì button tin tức
```
source.getLoginInfo()
source.getLoginInfoMap().get(key: String)
source.removeLoginInfo()```## cookie đối tượng bộ phận có thể dùng hàm số
```
Thu hoạch toàn bộ cookie

cookie.getCookie(url)
Thu hoạch cookie một khóa giá trị

cookie.getKey(url,key)
Xóa bỏ cookie

cookie.removeCookie(url)```## cache đối tượng bộ phận có thể dùng hàm số
> saveTime đơn vị: Giây, có thể tiết kiệm hơi
> Bảo tồn đến kho số liệu hòa hoãn tồn văn kiện (50M), bảo tồn nội dung khá lớn lúc xin sử dụng `getFile putFile````
Bảo tồn

cache.put(key: String, value: Any , saveTime: Int)
Đọc đến kho số liệu

cache.get(key: String): String?
Xóa bỏ

cache.delete(key: String)
Cache văn kiện nội dung

cache.putFile(key: String, value: String, saveTime: Int)
Đọc đến văn kiện nội dung

cache.getFile(key: String): String?
Bảo tồn đến bộ nhớ

cache.deleteMemory(key: String)
cache.getFromMemory(key: String): Any?
cache.putMemory(key: String, value: Any)```