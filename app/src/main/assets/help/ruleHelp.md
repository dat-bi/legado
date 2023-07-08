# Nguyên quy tắc trợ giúp

* [ Sách nguyên trợ giúp văn kiện ](https://alanskycn.gitee.io/teachme/Rule/source.html)
* [ Đặt mua nguyên trợ giúp văn kiện ](https://alanskycn.gitee.io/teachme/Rule/rss.html)
* Phụ trợ bàn phím ❓ Bên trong có thể cắm vào URL tham số mô bản, mở ra trợ giúp,js giáo trình, đang thì giáo trình, lựa chọn văn kiện

* Quy tắc tiêu chí, {{......}} Bên trong sử dụng quy tắc nhất thiết phải có rõ ràng quy tắc tiêu chí, không có quy tắc tiêu chí coi như js thi hành

```
@@ Ngầm thừa nhận quy tắc, trực tiếp viết lúc có thể tỉnh lược @@
@XPath: xpath quy tắc, trực tiếp viết lúc lấy // mở đầu có thể tiết kiệm hơi @XPath

@Json: json quy tắc, trực tiếp viết lúc lấy $. Mở đầu có thể tiết kiệm hơi @Json

: regex quy tắc, không thể tỉnh lược, chỉ có thể dùng tại sách danh sách cùng mục lục danh sách

```
* jsLib

> Rót vào JavaScript đến RhinoJs động cơ bên trong, ủng hộ hai loại cách thức, có thể thực hiện [ Hàm số dùng chung ](https://github.com/gedoor/legado/wiki/JavaScript%E5%87%BD%E6%95%B0%E5%85%B1%E7%94%A8)
> `JavaScript Code` Trực tiếp điền JavaScript đoạn ngắn

> `{"example":"https://www.example.com/js/example.js", ...}` Tự động phục dùng đã tải xuống js văn kiện

* Đồng phát tỷ lệ

> Đồng phát hạn chế, đơn vị ms, có thể điền hai loại cách thức

> `1000` Phỏng vấn khoảng cách 1s

> `20/60000` 60s bên trong phỏng vấn số lần 20

* Sách nguyên loại hình: Văn kiện

> Đối với giống biết hiên tàng thư cung cấp văn kiện chỉnh hợp tải xuống website, có thể tại sách nguyên tình hình rõ ràng download URL quy tắc thu hoạch văn kiện kết nối

> Thông qua lấy ra download kết nối hoặc văn kiện hưởng ứng đầu lĩnh thu hoạch văn kiện tin tức, thu hoạch thất bại sẽ tự động ghép lại ` Tên sách ` ` Tác giả ` Cùng download liên tiếp `UrlOption` `type` Chữ đoạn

> Áp súc văn kiện bớt áp lực cache sẽ ở lần sau sau khi khởi động tự động thanh lý, sẽ không chiếm dùng ngoài định mức không gian

* CookieJar

> Khải dụng sau sẽ tự động bảo tồn mỗi lần trở về trong đầu Set-Cookie bên trong giá trị, thích hợp với nghiệm chứng mã hình ảnh một loại cần session website

* Đăng lục UI

> Không sử dụng nội trí webView đăng lục website, cần sử dụng ` Đăng lục URL` Quy tắc thực hiện đăng lục lôgic, có thể sử dụng ` Đăng lục kiểm tra JS` Kiểm tra đăng lục kết quả

> Phiên bản 20221113 trọng yếu sửa đổi: Cái nút ủng hộ điều động ` Đăng lục URL` Trong quy tắc mặt hàm số, nhất thiết phải thực hiện `login` Hàm số

```

Quy tắc điền làm mẫu

[
{

name: "telephone",

type: "text"
},
{

name: "password",

type: "password"
},
{

name: " Đăng ký ",

type: "button",

action: "http://www.yooike.com/xiaoshuo/#/register?title=%E6%B3%A8%E5%86%8C"
},
{

name: " Thu hoạch nghiệm chứng mã ",

type: "button",

action: "getVerificationCode()"
}
]
```
* Đăng lục URL

> Có thể điền đăng lục kết nối hoặc thực hiện đăng lục UI đăng lục lôgic JavaScript

```

Làm mẫu điền

function login() {

java.log(" Mô phỏng đăng lục thỉnh cầu ");

java.log(source.getLoginInfoMap());
}

function getVerificationCode() {

java.log(" Đăng lục UI cái nút: Thu hoạch tới điện thoại di động dãy số "+result.get("telephone"))
}

Đăng lục cái nút hàm số thu hoạch đăng lục tin tức

result.get("telephone")

login hàm số thu hoạch đăng lục tin tức

source.getLoginInfo()

source.getLoginInfoMap().get("telephone")

source đăng lục liên quan phương pháp, nhưng tại js bên trong thông qua source. Điều động, có thể tham khảo A Lí mây giọng nói đăng lục

login()

getHeaderMap(hasLoginHeader: Boolean false)

getLoginHeader(): String?

getLoginHeaderMap(): Map?

putLoginHeader(header: String)

removeLoginHeader()

setVariable(variable: String?)

getVariable(): String?

AnalyzeUrl liên quan hàm số,js bên trong thông qua java. Điều động

initUrl() // một lần nữa phân tích url, có thể dùng tại đăng lục kiểm trắc js đăng lục sau một lần nữa phân tích url một lần nữa phỏng vấn

getHeaderMap().putAll(source.getHeaderMap(true)) // thiết trí cái mới đăng lục đầu

getStrResponse( jsStr: String? null, sourceRegex: String? null) // trở về phỏng vấn kết quả, văn bản loại hình, sách nguyên nội bộ một lần nữa đăng lục sau có thể thuyên chuyển này phương pháp một lần nữa trở về kết quả

getResponse(): Response // trở về phỏng vấn kết quả, internet đọc chậm động cơ áp dụng chính là cái này, điều động đăng lục sau tại điều động phương pháp kia có thể một lần nữa phỏng vấn, tham khảo A Lí mây đăng lục kiểm trắc

```
* Phát hiện url cách thức

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
* Thỉnh cầu đầu, ủng hộ http đại diện,socks4 socks5 đại diện thiết trí

```

socks5 đại diện

{
"proxy":"socks5://127.0.0.1:1080"
}

http đại diện

{
"proxy":"http://127.0.0.1:1080"
}

Ủng hộ đại diện server nghiệm chứng

{
"proxy":"socks5://127.0.0.1:1080@ Người sử dụng tên @ Mật mã "
}

Chú ý: Những thứ này thỉnh cầu đầu là không có ý nghĩa , sẽ bị bỏ qua

```
* url tăng thêm js tham số, phân tích url lúc thi hành, nhưng tại phỏng vấn url lúc xử lý url, lệ

```

https://www.baidu.com,{"js":"java.headerMap.put('xxx', 'yyy')"}

https://www.baidu.com,{"js":"java.url=java.url+'yyyy'"}
```
* Tăng thêm js phương pháp, dùng bình định lại hướng chặn lại

* `java.get(urlStr: String, headers: Map)`
* `java.post(urlStr: String, body: String, headers: Map)`
* Đối với lùng tìm bình định lại hướng nguyên, có thể sử dụng này phương pháp thu được bình định lại về phía sau url

```
(()=>{

if(page==1){

let url='https://www.yooread.net/e/search/index.php,'+JSON.stringify({
"method":"POST",
"body":"show=title&tempid=1&keyboard="+key

});

return java.put('surl',String(java.connect(url).raw().request().url()));
} else {

return java.get('surl')+'&page='+(page-1)
}
})()

Hoặc

(()=>{

let base='https://www.yooread.net/e/search/';

if(page==1){

let url=base+'index.php';

let body='show=title&tempid=1&keyboard='+key;

return base+java.put('surl',java.post(url,body,{}).header("Location"));
} else {

return base+java.get('surl')+'&page='+(page-1);
}
})()
```
* Hình ảnh kết nối ủng hộ sửa chữa headers

```

let options {
"headers": {"User-Agent": "xxxx","Referrer":baseUrl,"Cookie":"aaa=vbbb;"}
};
''
```
* Kiểu chữ phân tích sử dụng

> Phương pháp sử dụng, tại thay thế quy tắc bên trong sử dụng, nguyên lý căn cứ vào f1 kiểu chữ hình chữ số liệu đến f2 bên trong tra tìm hình chữ đối ứng mã hóa

```
(function(){

var b64=String(src).match(/ttf;base64,([^\)]+)/);

if(b64){

var f1 java.queryBase64TTF(b64[1]);

var f2 java.queryTTF("https://alanskycn.gitee.io/teachme/assets/font/Source Han Sans CN Regular.ttf");

return java.replaceFont(result, f1, f2);
}

return result;
})()
```
* Mua sắm thao tác

> Có thể trực tiếp điền kết nối hoặc JavaScript, nếu như thi hành kết quả là internet kết nối sẽ tự động mở ra trình duyệt,js trở về true tự động đổi mới mục lục cùng trước mắt chương tiết

* Hình ảnh giải mã

> Thích hợp với hình ảnh cần lần thứ hai giải mã tình huống, trực tiếp điền JavaScript, trở về giải mã sau `ByteArray`
> Bộ phận lượng biến đổi chứng minh: java( Vẻn vẹn ủng hộ [js mở rộng loại ](https://github.com/gedoor/legado/blob/master/app/src/main/java/io/legado/app/help/JsExtensions.kt)), result vì chờ giải mã hình ảnh `ByteArray`, src vì hình ảnh kết nối

* Trang bìa giải mã

> Cùng hình ảnh giải mã Trong đó result vì chờ giải mã trang bìa `inputStream`
