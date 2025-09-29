# Trợ giúp quy tắc nguồn

- [Hướng dẫn quy tắc đọc 3.0(Legado)](https://mgz0227.github.io/The-tutorial-of-Legado/)
- [Tài liệu trợ giúp nguồn sách](https://mgz0227.github.io/The-tutorial-of-Legado/Rule/source.html)
- [Tài liệu trợ giúp nguồn đăng ký](https://mgz0227.github.io/The-tutorial-of-Legado/Rule/rss.html)
- Bàn phím hỗ trợ ❓ có thể chèn mẫu tham số URL, mở trợ giúp, hướng dẫn js, hướng dẫn regex, chọn file
- Ký hiệu quy tắc, {{......}} khi sử dụng quy tắc bên trong phải có ký hiệu quy tắc rõ ràng, không có ký hiệu quy tắc sẽ được thực thi như js

```
@@ Quy tắc mặc định, có thể bỏ qua khi viết trực tiếp@@
@XPath: quy tắc xpath, khi viết trực tiếp bắt đầu bằng // có thể bỏ qua @XPath
@Json: quy tắc json, khi viết trực tiếp bắt đầu bằng $. có thể bỏ qua @Json
: quy tắc regex, không thể bỏ qua, chỉ có thể sử dụng trong danh sách sách và danh sách mục lục
```

- jsLib
  > Chèn JavaScript vào engine RhinoJs, hỗ trợ hai định dạng, có thể thực hiện [chia sẻ hàm](https://github.com/gedoor/legado/wiki/JavaScript%E5%87%BD%E6%95%B0%E5%85%B1%E7%94%A8)

> `JavaScript Code` điền trực tiếp đoạn JavaScript  
> `{"example":"https://www.example.com/js/example.js", ...}` tự động tái sử dụng file js đã tải

> Lưu ý hàm được định nghĩa tại đây có thể được nhiều thread gọi đồng thời, biến toàn cục trong hàm sẽ được chia sẻ sử dụng, việc sửa đổi chúng có thể gây ra vấn đề cạnh tranh

- Tỷ lệ đồng thời
  > Giới hạn đồng thời, đơn vị ms, có thể điền hai định dạng

> `1000` khoảng cách truy cập 1s  
> `20/60000` số lần truy cập trong 60s là 20

- Loại nguồn sách: File
  > Đối với các website tương tự như Zhi Xuan Cáng Thư cung cấp tải file tích hợp, có thể lấy link file trong quy tắc URL tải của chi tiết nguồn sách

> Thông qua việc cắt đường link tải hoặc header phản hồi file để lấy thông tin file, khi thất bại sẽ tự động ghép `tên sách` `tác giả` và trường `type` của `UrlOption` của link tải

> Bộ nhớ cache giải nén file nén sẽ tự động dọn dẹp sau lần khởi động tiếp theo, không chiếm thêm không gian

- CookieJar

  > Khi bật sẽ tự động lưu giá trị Set-Cookie trong header trả về mỗi lần, phù hợp cho các website cần session như ảnh mã xác nhận

- Giao diện đăng nhập
  > Không sử dụng webView tích hợp sẵn để đăng nhập website, cần sử dụng quy tắc `URL đăng nhập` để thực hiện logic đăng nhập, có thể sử dụng `JS kiểm tra đăng nhập` để kiểm tra kết quả đăng nhập  
  > Thay đổi quan trọng phiên bản 20221113: Nút hỗ trợ gọi hàm trong quy tắc `URL đăng nhập`, phải thực hiện hàm `login`

```
Ví dụ điền quy tắc
[
    {
        "name": "telephone",
        "type": "text"
    },
    {
        "name": "password",
        "type": "password"
    },
    {
        "name": "đăng ký",
        "type": "button",
        "action": "http://www.yooike.com/xiaoshuo/#/register?title=%E6%B3%A8%E5%86%8C"
    },
    {
        "name": "lấy mã xác nhận",
        "type": "button",
        "action": "getVerificationCode()",
        "style": {
            "layout_flexGrow": 0,
            "layout_flexShrink": 1,
            "layout_alignSelf": "auto",
            "layout_flexBasisPercent": -1,
            "layout_wrapBefore": false
        }
    }
]
```

- URL đăng nhập
  > Có thể điền link đăng nhập hoặc thực hiện JavaScript logic đăng nhập cho giao diện đăng nhập

```
Ví dụ điền
function login() {
    java.log("Đăng nhập mô phỏng yêu cầu");
    java.log(source.getLoginInfoMap());
}
function getVerificationCode() {
    java.log("Đăng nhập UI nút: Lấy số điện thoại "+result.get("telephone"))
}

Nút đăng nhập hàm lấy thông tin đăng nhập
result.get("telephone")
hàm login lấy thông tin đăng nhập
source.getLoginInfo()
source.getLoginInfoMap().get("telephone")
phương thức liên quan đăng nhập source, có thể gọi thông qua source. trong js, có thể tham khảo đăng nhập giọng nói Ali Cloud
login()
getHeaderMap(hasLoginHeader: Boolean = false)
getLoginHeader(): String?
getLoginHeaderMap(): Map<String, String>?
putLoginHeader(header: String)
removeLoginHeader()
setVariable(variable: String?)
getVariable(): String?
Hàm liên quan AnalyzeUrl, gọi thông qua java. trong js
initUrl() //phân tích lại url, có thể dùng cho js kiểm tra đăng nhập sau khi đăng nhập để phân tích lại url và truy cập lại
getHeaderMap().putAll(source.getHeaderMap(true)) //thiết lập lại header đăng nhập
getStrResponse( jsStr: String? = null, sourceRegex: String? = null) //trả về kết quả truy cập, kiểu văn bản, nguồn sách bên trong đăng nhập lại sau có thể gọi phương thức này để trả về kết quả lại
getResponse(): Response //trả về kết quả truy cập, engine đọc web sử dụng cái này, gọi đăng nhập sau rồi gọi phương thức này có thể truy cập lại, tham khảo kiểm tra đăng nhập Ali Cloud
```

- Định dạng url khám phá

```json
[
  {
    "title": "xxx",
    "url": "",
    "style": {
      "layout_flexGrow": 0,
      "layout_flexShrink": 1,
      "layout_alignSelf": "auto",
      "layout_flexBasisPercent": -1,
      "layout_wrapBefore": false
    }
  }
]
```

- Header yêu cầu, hỗ trợ thiết lập proxy http, proxy socks4 socks5
  > Lưu ý key của header yêu cầu phân biệt hoa thường  
  > Định dạng đúng User-Agent Referer  
  > Định dạng sai user-agent referer

```
proxy socks5
{
  "proxy":"socks5://127.0.0.1:1080"
}
proxy http
{
  "proxy":"http://127.0.0.1:1080"
}
hỗ trợ xác thực máy chủ proxy http
{
  "proxy":"http://127.0.0.1:1080@tên người dùng@mật khẩu"
}
Lưu ý: những header yêu cầu này không có ý nghĩa, sẽ bị bỏ qua
```

- url thêm tham số js, thực thi khi phân tích url, có thể xử lý url khi truy cập url, ví dụ

```
https://www.baidu.com,{"js":"java.headerMap.put('xxx', 'yyy')"}
https://www.baidu.com,{"js":"java.url=java.url+'yyyy'"}
```

- Thêm phương thức js, dùng cho chặn chuyển hướng
  - `java.get(urlStr: String, headers: Map<String, String>)`
  - `java.post(urlStr: String, body: String, headers: Map<String, String>)`
- Đối với nguồn chuyển hướng tìm kiếm, có thể sử dụng phương thức này để lấy url sau chuyển hướng

```
(()=>{
  if(page==1){
    let url='https://www.yooread.net/e/search/index.php,'+JSON.stringify({
    "method":"POST",
    "body":"show=title&tempid=1&keyboard="+key
    });
    return source.put('surl',String(java.connect(url).raw().request().url()));
  } else {
    return source.get('surl')+'&page='+(page-1)
  }
})()
hoặc
(()=>{
  let base='https://www.yooread.net/e/search/';
  if(page==1){
    let url=base+'index.php';
    let body='show=title&tempid=1&keyboard='+key;
    return base+source.put('surl',java.post(url,body,{}).header("Location"));
  } else {
    return base+source.get('surl')+'&page='+(page-1);
  }
})()
```

- Link hình ảnh hỗ trợ sửa đổi headers

```
let options = {
"headers": {"User-Agent": "xxxx","Referrer":baseUrl,"Cookie":"aaa=vbbb;"}
};
'<img src="'+src+","+JSON.stringify(options)+'">'
```

- Sử dụng phân tích font chữ
  > Cách sử dụng, dùng trong quy tắc thay thế nội dung chính, nguyên lý dựa trên dữ liệu glyph của font f1 để tìm trong f2 mã tương ứng với glyph

```
<js>
(function(){
  var b64=String(src).match(/ttf;base64,([^\)]+)/);
  if(b64){
    var f1 = java.queryTTF(b64[1]);
    var f2 = java.queryTTF("https://alanskycn.gitee.io/teachme/assets/font/Source Han Sans CN Regular.ttf");
    // return java.replaceFont(result, f1, f2);
    return java.replaceFont(result, f1, f2, true); // lọc bỏ glyph không tồn tại trong f1
  }
  return result;
})()
</js>
```

- Thao tác mua

> Có thể điền trực tiếp link hoặc JavaScript, nếu kết quả thực thi là link mạng sẽ tự động mở trình duyệt, js trả về true tự động làm mới mục lục và chương hiện tại

- Giải mã hình ảnh
  > Áp dụng cho trường hợp hình ảnh cần giải mã thứ hai, điền trực tiếp JavaScript, trả về `ByteArray` sau giải mã  
  > Giải thích một số biến: java (chỉ hỗ trợ [lớp mở rộng js](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/JsExtensions.kt)), result là `ByteArray` của hình ảnh cần giải mã, src là link hình ảnh

```js
java.createSymmetricCrypto("AES/CBC/PKCS5Padding", key, iv).decrypt(result);
```

```js
function decodeImage(data, key) {
  var input = new Packages.java.io.ByteArrayInputStream(data);
  var out = new Packages.java.io.ByteArrayOutputStream();
  var byte;
  while ((byte = input.read()) != -1) {
    out.write(byte ^ key);
  }
  return out.toByteArray();
}

decodeImage(result, key);
```

- Giải mã bìa
  > Giống giải mã hình ảnh, trong đó result là `inputStream` của bìa cần giải mã

```js
java.createSymmetricCrypto("AES/CBC/PKCS5Padding", key, iv).decrypt(result);
```

```js
function decodeImage(data, key) {
  var out = new Packages.java.io.ByteArrayOutputStream();
  var byte;
  while ((byte = data.read()) != -1) {
    out.write(byte ^ key);
  }
  return out.toByteArray();
}

decodeImage(result, key);
```
