# Biến và hàm js

> Legado sử dụng [Rhino v1.8.0](https://github.com/mozilla/rhino) làm engine JavaScript để thuận tiện cho [gọi các class và method Java](https://m.jb51.net/article/92138.htm), xem [bảng tương thích ECMAScript](https://mozilla.github.io/rhino/compat/engines.html)

> [Rhino runtime](https://github.com/mozilla/rhino/blob/master/rhino/src/main/java/org/mozilla/javascript/ScriptRuntime.java) lazy load nhập class và method Java

| Hàm khởi tạo | Hàm                       | Đối tượng               | Gọi class                                                                                                                                 | Mô tả ngắn gọn                            |
| ------------ | ------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| JavaImporter | importClass importPackage |                         | [ImporterTopLevel](https://github.com/mozilla/rhino/blob/master/rhino/src/main/java/org/mozilla/javascript/ImporterTopLevel.java)         | 导入 Java 类到 JavaScript                 |
|              | getClass                  | Packages java javax ... | [NativeJavaTopPackage](https://github.com/mozilla/rhino/blob/master/rhino/src/main/java/org/mozilla/javascript/NativeJavaTopPackage.java) | Nhập mặc định class Java trong JavaScript |
| JavaAdapter  |                           |                         | [JavaAdapter](https://github.com/mozilla/rhino/blob/master/rhino/src/main/java//org/mozilla/javascript/JavaAdapter.java)                  | Kế thừa class Java                        |

> Chú ý biến `java` trỏ tới đã bị Legado sửa đổi, nếu muốn gọi gói dưới `java.*`, vui lòng sử dụng `Packages.java.*`

> Trong quy tắc nguồn sách sử dụng `@js` `<js>` `{{}}` có thể sử dụng JavaScript gọi một số class và method tích hợp của Legado

> Chú ý vì lý do bảo mật, Legado sẽ chặn một số lời gọi class java, xem [RhinoClassShutter](https://github.com/gedoor/legado/blob/master/modules/rhino/src/main/java/com/script/rhino/RhinoClassShutter.kt)

> Các quy tắc nguồn sách khác nhau hỗ trợ gọi các class và method Java khác nhau

> Chú ý sử dụng `const` khai báo biến không hỗ trợ block scope, sử dụng trong vòng lặp sẽ có vấn đề giá trị không thay đổi, vui lòng đổi thành khai báo `var`

| Tên biến       | Gọi class                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| java           | Class hiện tại                                                                                                                      |
| baseUrl        | url hiện tại,String                                                                                                                 |
| result         | Kết quả bước trước                                                                                                                  |
| book           | [Class sách](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/data/entities/Book.kt)                    |
| rssArticle     | [Article 类](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/data/entities/RssArticle.kt)              |
| chapter        | [Class chương](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/data/entities/BookChapter.kt)           |
| source         | [Class nguồn sách cơ bản](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/data/entities/BaseSource.kt) |
| cookie         | [Class thao tác cookie](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/http/CookieStore.kt)      |
| cache          | [Class thao tác cache](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/CacheManager.kt)           |
| title          | Tiêu đề chương hiện tại String                                                                                                      |
| src            | Mã nguồn trả về từ request                                                                                                          |
| nextChapterUrl | url chương tiếp theo                                                                                                                |

## Các method một phần có thể sử dụng của đối tượng class hiện tại

### [RssJsExtensions](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/ui/rss/read/RssJsExtensions.kt)

> Chỉ có thể sử dụng trong quy tắc `shouldOverrideUrlLoading` của nguồn đăng ký  
> Nguồn đăng ký thêm chặn url chuyển hướng, js, trả về true để chặn, biến js url, có thể mở url thông qua js  
> Quy tắc chặn chuyển hướng url không thể thực hiện thao tác tốn thời gian
> 例子https://github.com/gedoor/legado/discussions/3259

- Gọi tìm kiếm Legado

```js
java.searchBook(bookName: String)
```

- Thêm vào giá sách

```js
java.addBook(bookUrl: String)
```

### [AnalyzeUrl](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/model/analyzeRule/AnalyzeUrl.kt) 部分函数

> Gọi trong js thông qua java., chỉ có hiệu lực trong quy tắc `Kiểm tra đăng nhập JS`

```js
initUrl() //Phân tích lại url, có thể dùng cho kiểm tra đăng nhập js sau khi đăng nhập phân tích lại url và truy cập lại
getHeaderMap().putAll(source.getHeaderMap(true)) //Thiết lập lại header đăng nhập
getStrResponse( jsStr: String? = null, sourceRegex: String? = null) //Trả về kết quả truy cập, loại văn bản, sau khi nguồn sách đăng nhập lại có thể gọi method này để trả về kết quả lại
getResponse(): Response //Trả về kết quả truy cập, engine đọc mạng sử dụng cái này, gọi đăng nhập sau đó gọi method này có thể truy cập lại, tham khảo kiểm tra đăng nhập Aliyun
```

### [AnalyzeRule](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/model/analyzeRule/AnalyzeRule.kt) 部分函数

- Lấy văn bản/danh sách văn bản
  > `mContent` Mã nguồn chờ phân tích, mặc định là trang hiện tại  
  > `isUrl` Đánh dấu liên kết, mặc định là `false`

```js
java.getString(ruleStr: String?, mContent: Any? = null, isUrl: Boolean = false)
java.getStringList(ruleStr: String?, mContent: Any? = null, isUrl: Boolean = false)
```

- Thiết lập nội dung phân tích

```js
java.setContent(content: Any?, baseUrl: String? = null):
```

- Lấy Element/Danh sách Element

> Nếu muốn thay đổi mã nguồn phân tích, vui lòng sử dụng `java.setContent` trước

```js
java.getElement(ruleStr: String)
java.getElements(ruleStr: String)
```

- Tìm lại sách/Lấy lại url mục lục

> Chỉ có thể sử dụng trước khi làm mới mục lục, một số nguồn sách địa chỉ sách và url mục lục sẽ thay đổi

```js
java.reGetBook();
java.refreshTocUrl();
```

- Lưu trữ và lấy biến

```js
java.get(key);
java.put(key, value);
```

### [js 扩展类](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/JsExtensions.kt) 部分函数

- Phân tích liên kết[JsURL](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/utils/JsURL.kt)

```js
java.toURL(url): JsURL
java.toURL(url, baseUrl): JsURL
```

- Lấy SystemWebView User-Agent

```js
java.getWebViewUA(): String
```

- Request mạng

```js
java.ajax(urlStr): String
java.ajaxAll(urlList: Array<String>): Array<StrResponse>
//Trả về StrResponse method body() code() message() headers() raw() toString()
java.connect(urlStr): StrResponse

java.post(url: String, body: String, headerMap: Map<String, String>): Connection.Response

java.get(url: String, headerMap: Map<String, String>): Connection.Response

java.head(url: String, headerMap: Map<String, String>): Connection.Response

* Sử dụng webView truy cập mạng
* @param html Trực tiếp sử dụng webView load html, nếu html rỗng thì truy cập trực tiếp url
* @param url Html nếu có đường dẫn tương đối resource không truyền url sẽ không truy cập được
* @param js Câu lệnh js dùng để lấy giá trị trả về, không có thì trả về toàn bộ mã nguồn
* @return Trả về nội dung js lấy được
java.webView(html: String?, url: String?, js: String?): String?

* Sử dụng webView lấy url chuyển hướng
java.webViewGetOverrideUrl(html: String?, url: String?, js: String?, overrideUrlRegex: String): String?

* Sử dụng webView lấy url resource
java.webViewGetSource(html: String?, url: String?, js: String?, sourceRegex: String): String?

* Sử dụng browser tích hợp mở liên kết, có thể dùng để lấy mã xác minh thủ công xác minh website chống crawl
* @param url Liên kết cần mở
* @param title Tiêu đề browser
java.startBrowser(url: String, title: String)

* Sử dụng browser tích hợp mở liên kết, và chờ kết quả webpage .body() lấy nội dung webpage
java.startBrowserAwait(url: String, title: String, refetchAfterSuccess: Boolean? = true): StrResponse
```

- Debug

```js
java.log(msg)
java.logType(var)
```

- Lấy mã xác minh do người dùng nhập

```js
java.getVerificationCode(imageUrl);
```

- Popup thông báo

```js
java.longToast(msg: Any?)
java.toast(msg: Any?)
```

- Đọc file JavaScript từ mạng (do java.cacheFile thực hiện), local, nhập vào context thủ công `eval(String(...))`

```js
java.importScript(url);
//Đường dẫn tương đối hỗ trợ android/data/{package}/cache
java.importScript(relativePath);
java.importScript(absolutePath);
```

- Cache file mạng

```js
Lấy
java.cacheFile(url)
java.cacheFile(url,saveTime)
Thực hiện nội dung
eval(String(java.cacheFile(url)))
Làm cache mất hiệu lực
cache.delete(java.md5Encode16(url))
```

- 获取网络压缩文件里面指定路径的数据 \*可替换 Zip Rar 7Z

```js
java.get*StringContent(url: String, path: String): String

java.get*StringContent(url: String, path: String, charsetName: String): String

java.get*ByteArrayContent(url: String, path: String): ByteArray?

```

- URI 编码

```js
java.encodeURI(str: String) //默认enc="UTF-8"
java.encodeURI(str: String, enc: String)
```

- base64
  > flags 参数可省略，默认 Base64.NO_WRAP，查看[flags 参数说明](https://blog.csdn.net/zcmain/article/details/97051870)

```js
java.base64Decode(str: String)
java.base64Decode(str: String, charset: String)
java.base64DecodeToByteArray(str: String, flags: Int)
java.base64Encode(str: String, flags: Int)
```

- ByteArray

```js
Str转Bytes
java.strToBytes(str: String)
java.strToBytes(str: String, charset: String)
Bytes转Str
java.bytesToStr(bytes: ByteArray)
java.bytesToStr(bytes: ByteArray, charset: String)
```

- Hex

```js
HexString 解码为字节数组
java.hexDecodeToByteArray(hex: String)
hexString 解码为utf8String
java.hexDecodeToString(hex: String)
utf8 编码为hexString
java.hexEncodeToString(utf8: String)
```

- 标识 id

```js
java.randomUUID();
java.androidId();
```

- 繁简转换

```js
将文本转换为简体
java.t2s(text: String): String
将文本转换为繁体
java.s2t(text: String): String
```

- 时间格式化

```js
java.timeFormatUTC(time: Long, format: String, sh: Int): String?
java.timeFormat(time: Long): String
```

- html 格式化

```js
java.htmlFormat(str: String): String
```

- 文件
  > 所有对于文件的读写删操作都是相对路径,只能操作阅读缓存/android/data/{package}/cache/内的文件

```js
//文件下载 url用于生成文件名，返回文件路径
downloadFile(url: String): String
//文件解压,zipPath为压缩文件路径，返回解压路径
unArchiveFile(zipPath: String): String
unzipFile(zipPath: String): String
unrarFile(zipPath: String): String
un7zFile(zipPath: String): String
//文件夹内所有文件读取
getTxtInFolder(unzipPath: String): String
//读取文本文件
readTxtFile(path: String): String
//删除文件
deleteFile(path: String)
```

### [js 加解密类](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/JsEncodeUtils.kt) 部分函数

> 提供在 JavaScript 环境中快捷调用 crypto 算法的函数，由[hutool-crypto](https://www.hutool.cn/docs/#/crypto/概述)实现  
> 由于兼容性问题，hutool-crypto 当前版本为 5.8.22

> 注意：如果输入的参数不是 Utf8String 可先调用`java.hexDecodeToByteArray java.base64DecodeToByteArray`转成 ByteArray

- 对称加密
  > 输入参数 key iv 支持 ByteArray|**Utf8String**

```js
// 创建Cipher
java.createSymmetricCrypto(transformation, key, iv);
```

> 解密加密参数 data 支持 ByteArray|Base64String|HexString|InputStream

```js
//解密为ByteArray String
cipher.decrypt(data);
cipher.decryptStr(data);
//加密为ByteArray Base64字符 HEX字符
cipher.encrypt(data);
cipher.encryptBase64(data);
cipher.encryptHex(data);
```

- 非对称加密
  > 输入参数 key 支持 ByteArray|**Utf8String**

```js
//创建cipher
java
  .createAsymmetricCrypto(transformation)
  //设置密钥
  .setPublicKey(key)
  .setPrivateKey(key);
```

> 解密加密参数 data 支持 ByteArray|Base64String|HexString|InputStream

```js
//解密为ByteArray String
cipher.decrypt(data,  usePublicKey: Boolean? = true
)
cipher.decryptStr(data, usePublicKey: Boolean? = true
)
//加密为ByteArray Base64字符 HEX字符
cipher.encrypt(data,  usePublicKey: Boolean? = true
)
cipher.encryptBase64(data,  usePublicKey: Boolean? = true
)
cipher.encryptHex(data,  usePublicKey: Boolean? = true
)
```

- 签名
  > 输入参数 key 支持 ByteArray|**Utf8String**

```js
//创建Sign
java
  .createSign(algorithm)
  //设置密钥
  .setPublicKey(key)
  .setPrivateKey(key);
```

> 签名参数 data 支持 ByteArray|inputStream|String

```js
//签名输出 ByteArray HexString
sign.sign(data);
sign.signHex(data);
```

- 摘要

```js
java.digestHex(data: String, algorithm: String,): String?

java.digestBase64Str(data: String, algorithm: String,): String?
```

- md5

```js
java.md5Encode(str);
java.md5Encode16(str);
```

- HMac

```js
java.HMacHex(data: String, algorithm: String, key: String): String

java.HMacBase64(data: String, algorithm: String, key: String): String
```

## Thuộc tính có thể sử dụng của đối tượng book

### Thuộc tính

> Cách sử dụng: Trong js hoặc {{}} sử dụng book.thuộc tính để lấy. Ví dụ thêm vào sau nội dung chính ##{{book.name+"正文卷"+title}} có thể lọc bỏ tên sách+正文卷+tên chương (như 我是大明星正文卷第二章我爸是豪门总裁) loại ký tự này.

```js
bookUrl // Địa chỉ trang chi tiết(nguồn sách local lưu trữ đường dẫn file đầy đủ)
tocUrl // Địa chỉ trang mục lục (toc=table of Contents)
origin // URL nguồn sách(mặc định BookType.local)
originName //Tên nguồn sách or Tên file sách local
name // Tên sách(nguồn sách lấy)
author // Tên tác giả(nguồn sách lấy)
kind // Thông tin phân loại(nguồn sách lấy)
customTag // Thông tin phân loại(người dùng sửa)
coverUrl // URL bìa(nguồn sách lấy)
customCoverUrl // URL bìa(người dùng sửa)
intro // Nội dung giới thiệu(nguồn sách lấy)
customIntro // Nội dung giới thiệu(người dùng sửa)
charset // Tên bộ ký tự tùy chỉnh(chỉ áp dụng cho sách local)
type // 0:text 1:audio
group // 自定义分组索引号
latestChapterTitle // Tiêu đề chương mới nhất
latestChapterTime // Thời gian cập nhật tiêu đề chương mới nhất
lastCheckTime // Thời gian cập nhật thông tin sách gần đây nhất
lastCheckCount // Số lượng chương mới phát hiện gần đây nhất
totalChapterNum // Tổng số mục lục sách
durChapterTitle // Tên chương hiện tại
durChapterIndex // Index chương hiện tại
durChapterPos // Tiến độ đọc hiện tại(vị trí index ký tự đầu dòng)
durChapterTime // Thời gian đọc sách gần đây nhất(thời gian mở nội dung chính)
canUpdate // Làm mới giá sách khi cập nhật thông tin sách
order // Sắp xếp thủ công
originOrder //Sắp xếp nguồn sách
variable // Thông tin biến sách tùy chỉnh(dùng cho quy tắc nguồn sách tìm kiếm thông tin sách)
```

## chapter 对象的部分可用属性

> 使用方法: 在 js 中或{{}}中使用 chapter.属性的方式即可获取.如在正文内容后加上 ##{{chapter.title+chapter.index}} 可以净化 章节标题+序号(如 第二章 天仙下凡 2) 这一类的字符.

```js
url; // 章节地址
title; // 章节标题
baseUrl; //用来拼接相对url
bookUrl; // 书籍地址
index; // 章节序号
resourceUrl; // 音频真实URL
tag; //
start; // 章节起始位置
end; // 章节终止位置
variable; //变量
```

## source 对象的部分可用函数

- 获取书源 url

```js
source.getKey();
```

- 书源变量存取

```js
source.setVariable(variable: String?)
source.getVariable()
```

- 登录头操作

```js
获取登录头
source.getLoginHeader()
获取登录头某一键值
source.getLoginHeaderMap().get(key: String)
保存登录头
source.putLoginHeader(header: String)
清除登录头
source.removeLoginHeader()
```

- 用户登录信息操作
  > 使用`登录UI`规则，并成功登录，阅读自动加密保存登录 UI 规则中除 type 为 button 的信息

```js
login函数获取登录信息
source.getLoginInfo()
login函数获取登录信息键值
source.getLoginInfoMap().get(key: String)
清除登录信息
source.removeLoginInfo()
```

## cookie 对象的部分可用函数

```js
获取全部cookie;
cookie.getCookie(url);
获取cookie某一键值;
cookie.getKey(url, key);
设置cookie;
cookie.setCookie(url, cookie);
替换cookie;
cookie.replaceCookie(url, cookie);
删除cookie;
cookie.removeCookie(url);
```

## cache 对象的部分可用函数

> saveTime 单位:秒，可省略  
> 保存至数据库和缓存文件(50M)，保存的内容较大时请使用`getFile putFile`

```js
保存
cache.put(key: String, value: String, saveTime: Int)
读取数据库
cache.get(key: String): String?
删除
cache.delete(key: String)
缓存文件内容
cache.putFile(key: String, value: String, saveTime: Int)
读取文件内容
cache.getFile(key: String): String?
保存到内存
cache.putMemory(key: String, value: Any)
读取内存
cache.getFromMemory(key: String): Any?
删除内存
cache.deleteMemory(key: String)
```

## 跳转外部链接/应用函数

```js
// 跳转外部链接，传入http链接或者scheme跳转到浏览器或其他应用
java.openUrl(url:String)
// 指定mimeType，可以跳转指定类型应用，例如（video/*）
java.openUrl(url:String,mimeType:String)
```
