# Giải thích chi tiết biểu thức đường dẫn xpath

_Lưu ý: Tất cả code trong bài viết này đã được xác minh qua Chrome (phiên bản 123.0.6312.86)_

> Tài liệu XPath định nghĩa 13 trục (axes) khác nhau.  
> Trục biểu thị mối quan hệ với phần tử và được sử dụng để xác định vị trí các phần tử trên cây phần tử tương đối với phần tử đó.

- `namespace`（không hỗ trợ）
- `attribute` thuộc tính của phần tử. Có thể viết tắt là `@`
- `self` biểu thị bản thân phần tử. Có thể viết tắt là `.`
- `parent` phần tử cha của phần tử hiện tại. Có thể viết tắt là `..`
- `child` phần tử con của phần tử hiện tại.
- `ancestor` tất cả tổ tiên trực tiếp của phần tử hiện tại.
- `ancestor-or-self` phần tử hiện tại và tất cả tổ tiên trực tiếp của nó.
- `descendant` tất cả phần tử con đệ quy của phần tử hiện tại.
- `descendant-or-self` phần tử hiện tại và tất cả phần tử con đệ quy của nó.
- `following` tất cả phần tử xuất hiện sau phần tử hiện tại. Bỏ qua cấp độ phần tử, nhưng không bao gồm hậu duệ trực tiếp.
- `following-sibling` tất cả phần tử cùng cấp xuất hiện sau phần tử hiện tại.
- `preceding` tất cả phần tử xuất hiện trước phần tử hiện tại. Bỏ qua cấp độ phần tử, nhưng không bao gồm tổ tiên trực tiếp.
- `preceding-sibling` tất cả phần tử cùng cấp xuất hiện trước phần tử hiện tại.

```js
// Cách dùng trục-> tên_trục::biểu_thức
// Ví dụ:
> $x('//body/ancestor-or-self::*')
< [body, html]
```

#### 1. Định dạng cơ bản của biểu thức xpath

> xpath chọn phần tử thông qua "biểu thức đường dẫn" (Path Expression).  
> Về hình thức, "biểu thức đường dẫn" rất giống với hệ thống file truyền thống.

```txt
# Dấu "/" làm dấu phân cách bên trong đường dẫn.
# Cùng một phần tử có hai cách viết: đường dẫn tuyệt đối và đường dẫn tương đối.
# Đường dẫn tuyệt đối phải bắt đầu bằng "/", theo sau là phần tử gốc, ví dụ /step/step/...
# Đường dẫn tương đối là các cách viết khác ngoài đường dẫn tuyệt đối, ví dụ step/step, tức là không dùng "/" ở đầu.
# "." biểu thị phần tử hiện tại.
# ".." biểu thị phần tử cha của phần tử hiện tại
```

### 2. Quy tắc cơ bản để chọn phần tử

```txt
- "/": biểu thị chọn phần tử gốc
- "//": biểu thị chọn phần tử nào đó ở vị trí bất kỳ
- nodename: biểu thị chọn phần tử có tên chỉ định
- "@": biểu thị chọn một thuộc tính nào đó
```

### 3. Ví dụ chọn phần tử

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>标题</title>
    <meta property=author" content="作者" />
  </head>
  <body>
    <div>
      <title lang="eng">Harry Potter</title>
      <p>29.39</p>
      <p>usd</p>
    </div>
    <div>
      <title lang="cn">Cpp高级编程</title>
      <p>39.95</p>
      <p>rmb</p>
    </div>
    <div id="list">
      <dl>
        <dd><a href="/1">一</a></dd>
        <dd><a href="/2">二</a></dd>
        <dd><a href="/3">三</a></dd>
      </dl>
    </div>
  </body>
</html>
```

```js
// Ví dụ 1
> $x('/') // Chọn phần tử gốc, trả về mảng chứa phần tử được chọn.
< [document]
// Ví dụ 2
> $x('/html') // Chọn tất cả phần tử con html dưới phần tử gốc, đây là cách viết đường dẫn tuyệt đối.
< [html]
// Ví dụ 3
> $x('html/head/meta') // Chọn tất cả phần tử meta dưới phần tử head, đây là cách viết đường dẫn tương đối.
< [meta, meta]  // <meta charset="utf-8">, <meta property="author" content="作者">
// Ví dụ 4
> $x('//p') // Chọn tất cả phần tử p, không quan tâm chúng ở đâu
< [p, p, p, p] // <p>29.39</p>, <p>usd</p>, <p>39.95</p>, <p>rmb</p>
// Ví dụ 5
> $x('html/body//a') // Chọn tất cả phần tử a dưới phần tử body
< [a, a, a] // <a href="/1">一</a>, <a href="/2">二</a>, <a href="/3">三</a>
// Ví dụ 6
> $x('//@lang') // Chọn tất cả thuộc tính có tên lang.
< [lang, lang] // lang="eng", lang="cn"
> $x('html/head/meta/@content') // Chọn thuộc tính content của tất cả phần tử meta dưới phần tử head.
< [content] // content="作者"
// Ví dụ 7
> $x('//meta/..') // Chọn phần tử cha của tất cả phần tử meta. (Kết quả giống nhau chỉ trả về một)
< [head] // <head>...</head>
```

### 4. Điều kiện vị từ xpath (Predicate)

> Cái gọi là "điều kiện vị từ", chính là điều kiện bổ sung cho biểu thức đường dẫn.  
> Tất cả điều kiện bổ sung, đều viết trong dấu ngoặc vuông `[]`, dùng để lọc phần tử thêm nữa.
> Chỉ những phần tử có kết quả biểu thức trong ngoặc vuông là true mới được chọn.

```js
// Ví dụ 8
> $x('html/head/meta[1]') //  Chọn phần tử meta đầu tiên dưới phần tử head
< [meta] // <meta charset="utf-8">
> $x('//p[1]') // Chọn phần tử p đầu tiên dưới tất cả phần tử
< [p, p] // <p>29.39</p>, <p>39.95</p>
// Ví dụ 9
> $x('html/head/meta[last()]') // Chọn phần tử meta cuối cùng dưới phần tử head
< [meta] // <meta property="author" content="作者">
// Ví dụ 10
> $x('html/head/meta[last()-1]') // Chọn phần tử meta thứ hai từ cuối dưới phần tử head
< [meta] // <meta charset="utf-8">
// Ví dụ 11
> $x('html/head/meta[position()>1]') // Chọn tất cả phần tử meta dưới phần tử head ngoại trừ phần tử đầu tiên
< [meta] // <meta property="author" content="作者">
// Ví dụ 12
> $x('//title[@lang]') // Chọn tất cả phần tử title có thuộc tính lang.
< [title, title] // <title lang="eng">Harry Potter</title>, <title lang="cn">Cpp高级编程</title>
// Ví dụ 13
> $x('//title[@lang="eng"]') // Chọn tất cả phần tử title có giá trị thuộc tính lang bằng "eng".
< [title] // <title lang="eng">Harry Potter</title>
// Ví dụ 14
> $x('/html/body/div[dl]') // Chọn phần tử con div của body, và div được chọn phải có phần tử con dl.
< [div] // <div id="list"><dl id="list">...</dl></div>
// Ví dụ 15
> $x('/html/body/div[p>35.00]') // Chọn phần tử con div của body, và giá trị phần tử con p của div được chọn phải lớn hơn 35.00.
< [div] // <div><title lang="cn">Cpp高级编程</title><p>39.95</p><p>rmb</p></div>
> $x('/html/body/div[p="rmb"]') // Chọn phần tử con div của body, và giá trị phần tử con p của div được chọn phải bằng "rmb".
< [div] // <div><title lang="cn">Cpp高级编程</title><p>39.95</p><p>rmb</p></div>
// Ví dụ 16
> $x('/html/body/div[p="rmb"]/title') // Trong tập kết quả ví dụ 14, chọn phần tử con title.
< [title] // <title lang="cn">Cpp高级编程</title>
// Ví dụ 17
> $x('/html/body/div/p[.>35.00]') // Chọn phần tử con p của "/html/body/div" có giá trị lớn hơn 35.00.
< [p] // <p>39.95</p>
```

### 5. Ký tự đại diện

- `\*` biểu thị khớp với bất kỳ phần tử nào.
- `@\*` biểu thị khớp với bất kỳ tên thuộc tính nào.

```js
// Ví dụ 18
> $x('//*') // Chọn tất cả phần tử, kết quả trả về theo thứ tự đệ quy
< [html, head, meta, title, meta, body, div, title, p, p, div, title, p, p, div, dl, dd, a, dd, a, dd, a]
// Ví dụ 19
> $x('/*/*') // Chọn tất cả phần tử tầng thứ hai
< [head, body] // <head>...</head>, <body>...</body>
// Ví dụ 20
> $x('//dl[@id="list"]/*') // Chọn tất cả phần tử con của phần tử dl có id="list".
< [dd, dd, dd] // <dd><a href="/1">一</a></dd>, <dd><a href="/2">二</a></dd>, <dd><a href="/3">三</a></dd>
// Ví dụ 21
> $x('//title[@*]') // Chọn tất cả phần tử title có thuộc tính.
< [title, title] // <title lang="eng">Harry Potter</title>, <title lang="cn">Cpp高级编程</title>
```

### 6. Chọn nhiều đường dẫn

- Dùng `|` để gộp kết quả chọn của nhiều biểu thức.

```js
// Ví dụ 22
> $x('//title | //a') // Chọn tất cả phần tử title và a.
< [title, title, title, a, a, a]

```

### 7. Hàm xpath

> Tham số của hàm xpath có thể là chuỗi tĩnh hoặc biểu thức, và hàm có thể gọi lồng nhau.  
> Chỉ số của xpath đều bắt đầu từ 1, không phải từ 0.

```js
// boolean(expression) Chuyển đổi kết quả chọn của biểu thức thành giá trị boolean.
> $x('boolean(//title)')
< true
// number([object]) Chuyển đổi kết quả chọn của biểu thức thành số. (Nội dung phần tử HTML mặc định đều là chuỗi)
> $x('number(//p[1])')
< 29.39
// round(decimal) Chuyển đổi tham số số thành số nguyên và làm tròn.
> $x('round(//p[1])')
< 29
// ceiling(number) Chuyển đổi tham số số thành số nguyên và làm tròn lên. ceiling(5.2)=6
> $x('ceiling(//p[1])') // Chỉ sử dụng phần tử đầu tiên khớp với biểu thức
< 30
// floor(number) Chuyển đổi tham số số thành số nguyên và làm tròn xuống. floor(5.8)=5
> $x('floor(//p[1])')
< 29
// concat( string1, string2 [,stringn]* ) Nối chuỗi, tham số là chuỗi tĩnh hoặc biểu thức
> $x('concat("cost:", //p[1], //p[2])') // Chỉ sử dụng phần tử đầu tiên khớp với biểu thức
< 'cost:29.39usd'
// contains(haystack, needle) Kiểm tra haystack có chứa needle không, trả về boolean
> $x('contains(//p[1], "29.39")') // Chỉ sử dụng phần tử đầu tiên khớp với biểu thức
< true
> $x('//title[contains(., "Harry")]') // Chọn phần tử title có nội dung chứa "Harry".
< [title] // <title lang="eng">Harry Potter</title>
// count( node-set ) Đếm số lượng phần tử được chọn bởi biểu thức.
> $x('count(//p)')
< 4
// id(expression) Chọn phần tử theo thuộc tính id, nếu tham số là biểu thức, sẽ lấy kết quả biểu thức làm id để truy vấn.
> $x('id(//dl/@id)') // Tương đương với $x('id("list")')
< [dl#list] // <dl id="list">...</dl>
// last() Trả về số lượng thành viên của tập hợp phần tử cùng cấp khớp với biểu thức đường dẫn hiện tại.
> $x('//p[last()]')
< [p, p] // <p>usd</p>, <p>rmb</p>
// name([node-set]) Trả về tên phần tử có namespace của thành viên đầu tiên trong tập chọn của biểu thức, trong HTML tương đương với local-name([node-set]).
// local-name([node-set]) Trả về tên phần tử cục bộ của thành viên đầu tiên trong tập chọn của biểu thức.
> $x('local-name(//*[@id])') //
< 'dl'
// namespace-uri([node-set]) Lấy URI namespace của node đầu tiên trong tập node được chọn.
> $x('namespace-uri(//div)')
< 'http://www.w3.org/1999/xhtml' // HTML thường trả về giá trị cố định này
// normalize-space([string]) Loại bỏ khoảng trắng đầu cuối trong nội dung văn bản và thay thế khoảng trắng liên tiếp bên trong bằng một khoảng trắng đơn
> $x('normalize-space("  test    string   ")')
< 'test string'
// not(expression) Trả về giá trị boolean nghịch đảo của biểu thức.
> $x('//title[not(@lang)]')
< [title] // <title>标题</title>
// position() Trả về vị trí của phần tử được chọn trong tập hợp phần tử cùng cấp khớp với biểu thức đường dẫn.
> $x('//meta[position()=2]')
< [meta] // <meta property=author" content="作者" />
// starts-with(haystack, needle) Kiểm tra chuỗi haystack có bắt đầu bằng chuỗi needle khác không.
> $x('//title[starts-with(., "Cpp")]')
< [title] // <title lang="cn">Cpp高级编程</title]
// string([object]) Chuyển đổi tham số đã cho thành chuỗi
> $x('string(//p)')
< '29.39'
// string-length([string]) Trả về số lượng ký tự của chuỗi đã cho
> $x('string-length(string(//p))')
< 5
// substring(string, start[, length]) Cắt chuỗi
> $x('substring(string(//p), 1, 3)')
< '29.'
// substring-after(haystack, needle) Trả về chuỗi sau needle đầu tiên trong chuỗi haystack.
> $x('substring-after(string(//p), ".")')
< '39'
// substring-before(haystack, needle) Trả về chuỗi trước needle đầu tiên trong chuỗi haystack.
> $x('substring-before(string(//p), ".")')
< '29'
// sum([node-set]) Tính tổng số của tập hợp đã cho. Nếu tồn tại số không phải số trong tập hợp đã cho, trả về NaN
> $x('sum(//p[1])')
< 69.34
// translate(string, "abc", "XYZ") Thay thế lần lượt a, b, c xuất hiện trong string bằng X, Y, Z ở vị trí tương ứng.
// Nếu ký tự trong tham số thứ ba ít hơn tham số thứ hai, thì ký tự tương ứng trong tham số đầu tiên sẽ bị xóa.
> $x('translate("aabbcc112233", "ac2", "V8")')
< 'VVbb881133'
// true() Biểu thị giá trị boolean true trong hàm
// false() Biểu thị giá trị boolean false trong hàm
```
