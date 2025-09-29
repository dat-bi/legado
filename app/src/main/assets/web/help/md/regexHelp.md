# Học biểu thức chính quy

- [Khớp cơ bản]
- [Ký tự meta]
  - [Dấu chấm tiếng Anh]
  - [Tập ký tự]
    - [Tập ký tự phủ định]
  - [Lặp lại]
    - [Dấu sao]
    - [Dấu cộng]
    - [Dấu hỏi]
  - [Ngoặc nhọn]
  - [Nhóm ký tự]
  - [Cấu trúc phân nhánh]
  - [Escape ký tự đặc biệt]
  - [Ký tự định vị]
    - [Ký hiệu chèn]
    - [Ký hiệu đô la]
- [Tập ký tự viết tắt]
- [Assertion]
  - [Positive lookahead assertion]
  - [Negative lookahead assertion]
  - [Positive lookbehind assertion]
  - [Negative lookbehind assertion]
- [Cờ đánh dấu]
  - [Không phân biệt hoa thường]
  - [Tìm kiếm toàn cục]
  - [Khớp đa dòng]
- [Biểu thức chính quy thường dùng]

## 1. Khớp cơ bản

Biểu thức chính quy chỉ là mẫu mà chúng ta sử dụng để kiểm tra chữ cái và số trong văn bản. Ví dụ biểu thức chính quy `cat`, biểu thị: chữ cái `c` theo sau là một chữ cái `a`, rồi theo sau là một chữ cái `t`.<pre>"cat" => The <a href="#learn-regex"><strong>cat</strong></a> sat on the mat</pre>

Biểu thức chính quy `123` sẽ khớp với chuỗi "123". Việc khớp biểu thức chính quy được thực hiện bằng cách so sánh từng ký tự trong biểu thức chính quy với từng ký tự trong chuỗi cần khớp.
Biểu thức chính quy thường phân biệt hoa thường, do đó biểu thức chính quy `Cat` không khớp với chuỗi "cat".<pre>"Cat" => The cat sat on the <a href="#learn-regex"><strong>Cat</strong></a></pre>

## 2. Ký tự meta

Ký tự meta là các thành phần cơ bản của biểu thức chính quy. Ký tự meta ở đây không có nghĩa thông thường mà được hiểu theo một nghĩa đặc biệt nào đó. Một số ký tự meta có nghĩa đặc biệt khi được viết trong dấu ngoặc vuông.
Các ký tự meta như sau:

| Ký tự meta | Mô tả                                                                                                                                                  |
| :--------: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|     .      | Khớp bất kỳ ký tự nào ngoại trừ ký tự xuống dòng.                                                                                                      |
|    [ ]     | Lớp ký tự, khớp bất kỳ ký tự nào chứa trong dấu ngoặc vuông.                                                                                           |
|    [^ ]    | Lớp ký tự phủ định. Khớp bất kỳ ký tự nào không chứa trong dấu ngoặc vuông                                                                             |
|     \*     | Khớp biểu thức con trước đó không lần hoặc nhiều lần                                                                                                   |
|     +      | Khớp biểu thức con trước đó một lần hoặc nhiều lần                                                                                                     |
|     ?      | Khớp biểu thức con trước đó không lần hoặc một lần, hoặc chỉ định một bộ giới hạn không tham lam.                                                      |
|   {n,m}    | Ngoặc nhọn, khớp ký tự trước ít nhất n lần, nhưng không quá m lần.                                                                                     |
|   (xyz)    | Nhóm ký tự, khớp ký tự xyz theo thứ tự chính xác.                                                                                                      |
|   &#124;   | Cấu trúc phân nhánh, khớp ký tự trước hoặc sau ký hiệu.                                                                                                |
|   &#92;    | Ký tự escape, nó có thể khôi phục ý nghĩa gốc của ký tự meta, cho phép bạn khớp ký tự đã được đặt trước <code>[ ] ( ) { } . \* + ? ^ $ \ &#124;</code> |
|     ^      | Khớp đầu dòng                                                                                                                                          |
|     $      | Khớp cuối dòng                                                                                                                                         |

## 2.1 Dấu chấm tiếng Anh

Dấu chấm tiếng Anh `.` là ví dụ đơn giản nhất của ký tự meta. Ký tự meta `.` có thể khớp với bất kỳ ký tự đơn nào. Nó không khớp với ký tự xuống dòng và ký tự dòng mới. Ví dụ biểu thức chính quy `.ar`, biểu thị: bất kỳ ký tự nào theo sau là một chữ cái `a`,
rồi theo sau là một chữ cái `r`.<pre>".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.</pre>

## 2.2 Tập ký tự

Tập ký tự còn được gọi là lớp ký tự. Dấu ngoặc vuông được sử dụng để chỉ định tập ký tự. Sử dụng dấu gạch ngang trong tập ký tự để chỉ định phạm vi ký tự. Thứ tự của phạm vi ký tự trong dấu ngoặc vuông không quan trọng.
Ví dụ biểu thức chính quy `[Tt]he`, biểu thị: chữ cái `T` hoa hoặc chữ cái `t` thường, theo sau là chữ cái `h`, rồi theo sau là chữ cái `e`.<pre>"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.</pre>

Tuy nhiên, dấu chấm tiếng Anh trong tập ký tự biểu thị nghĩa đen của nó. Biểu thức chính quy `ar[.]`, biểu thị chữ cái thường `a`, theo sau là một chữ cái `r`, rồi theo sau là một ký tự dấu chấm tiếng Anh `.`.<pre>"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a></pre>

### 2.2.1 Tập ký tự phủ định

Nói chung ký tự chèn `^` biểu thị sự bắt đầu của một chuỗi, nhưng khi nó xuất hiện trong dấu ngoặc vuông, nó sẽ phủ định tập ký tự. Ví dụ biểu thức chính quy `[^c]ar`, biểu thị: bất kỳ ký tự nào ngoại trừ chữ cái `c`, theo sau là ký tự `a`,
rồi theo sau là một chữ cái `r`.<pre>"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.</pre>

## 2.3 Lặp lại

Các ký tự meta sau `+`, `*` hoặc `?` được sử dụng để chỉ định một mẫu con có thể xuất hiện bao nhiêu lần. Các ký tự meta này có tác dụng khác nhau trong các tình huống khác nhau.

### 2.3.1 Dấu sao

Ký hiệu `*` biểu thị khớp với quy tắc khớp trước đó không lần hoặc nhiều lần. Biểu thức chính quy `a*` biểu thị chữ cái thường `a` có thể lặp lại không lần hoặc nhiều lần. Nhưng nếu nó xuất hiện sau tập ký tự hoặc lớp ký tự, nó biểu thị sự lặp lại của toàn bộ tập ký tự.
Ví dụ biểu thức chính quy `[a-z]*`, biểu thị: một dòng có thể chứa bất kỳ số lượng chữ cái thường nào.<pre>"[a-z]\*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.</pre>

Ký hiệu `*` có thể được sử dụng với ký hiệu meta `.` để khớp với bất kỳ chuỗi ký tự nào `.*`. Ký hiệu `*` có thể được sử dụng với ký tự khoảng trắng `\s` để khớp với một chuỗi các ký tự khoảng trắng.
Ví dụ biểu thức chính quy `\s*cat\s*`, biểu thị: không hoặc nhiều ký tự khoảng trắng, theo sau là chữ cái thường `c`, rồi theo sau là chữ cái thường `a`, rồi rồi theo sau là chữ cái thường `t`, theo sau là không hoặc nhiều ký tự khoảng trắng.<pre>"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex"><strong>cat</strong></a>.</pre>

### 2.3.2 Dấu cộng

Ký hiệu `+` khớp với ký tự trước đó một lần hoặc nhiều lần. Ví dụ biểu thức chính quy `c.+t`, biểu thị: một chữ cái thường `c`, theo sau là bất kỳ số lượng ký tự nào, theo sau là chữ cái thường `t`.<pre>"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.</pre>

### 2.3.3 Dấu hỏi

Trong biểu thức chính quy, ký tự meta `?` được sử dụng để biểu thị ký tự trước đó là tùy chọn. Ký hiệu này khớp với ký tự trước đó không lần hoặc một lần.
Ví dụ biểu thức chính quy `[T]?he`, biểu thị: chữ cái hoa `T` tùy chọn, theo sau là chữ cái thường `h`, theo sau là chữ cái thường `e`.<pre>"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.</pre><pre>"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.</pre>

## 2.4 Ngoặc nhọn

Trong biểu thức chính quy, ngoặc nhọn (còn được gọi là bộ định lượng ?) được sử dụng để chỉ định số lần một ký tự hoặc một nhóm ký tự có thể lặp lại. Ví dụ biểu thức chính quy `[0-9]{2,3}`, biểu thị: khớp ít nhất 2 chữ số nhưng không quá 3 chữ số (ký tự trong khoảng 0 đến 9).<pre>"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.</pre>

Chúng ta có thể bỏ qua số thứ hai. Ví dụ biểu thức chính quy `[0-9]{2,}`, biểu thị: khớp 2 hoặc nhiều chữ số hơn. Nếu chúng ta cũng xóa dấu phẩy, biểu thức chính quy `[0-9]{2}`, biểu thị: khớp chính xác 2 chữ số.<pre>"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.</pre><pre>"[0-9]{2}" => The number was 9.<a href="#learn-regex"><strong>99</strong></a><a href="#learn-regex"><strong>97</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.</pre>

## 2.5 Nhóm ký tự

Nhóm ký tự là một nhóm các mẫu con được viết trong dấu ngoặc tròn `(...)`. Như chúng ta đã thảo luận trong biểu thức chính quy, nếu chúng ta đặt một bộ định lượng sau một ký tự, nó sẽ lặp lại ký tự trước đó.
Tuy nhiên, nếu chúng ta đặt bộ định lượng sau một nhóm ký tự, nó sẽ lặp lại toàn bộ nhóm ký tự.
Ví dụ biểu thức chính quy `(ab)*` biểu thị khớp với không hoặc nhiều chuỗi "ab". Chúng ta cũng có thể sử dụng ký tự meta `|` trong nhóm ký tự. Ví dụ biểu thức chính quy `(c|g|p)ar`, biểu thị: chữ cái thường `c`, `g` hoặc `p` theo sau là chữ cái `a`, theo sau là chữ cái `r`.<pre>"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.</pre>

## 2.6 Cấu trúc phân nhánh

Trong biểu thức chính quy, thanh dọc `|` được sử dụng để định nghĩa cấu trúc phân nhánh, cấu trúc phân nhánh giống như điều kiện giữa nhiều biểu thức. Bây giờ bạn có thể nghĩ rằng tập ký tự và cấu trúc phân nhánh hoạt động theo cách giống nhau.
Nhưng sự khác biệt lớn giữa tập ký tự và cấu trúc phân nhánh là tập ký tự chỉ hoạt động ở cấp độ ký tự, trong khi cấu trúc phân nhánh vẫn có thể được sử dụng ở cấp độ biểu thức.
Ví dụ biểu thức chính quy `(T|t)he|car`, biểu thị: chữ cái hoa `T` hoặc chữ cái thường `t`, theo sau là chữ cái thường `h`, theo sau là chữ cái thường `e` hoặc chữ cái thường `c`, theo sau là chữ cái thường `a`, theo sau là chữ cái thường `r`.<pre>"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.</pre>

## 2.7 Escape ký tự đặc biệt

Biểu thức chính quy sử dụng dấu gạch chéo ngược `\` để escape ký tự tiếp theo. Điều này sẽ cho phép bạn sử dụng các ký tự được bảo lưu làm ký tự khớp `{ } [ ] / \ + * . $ ^ | ?`. Thêm `\` trước ký tự đặc biệt, bạn có thể sử dụng nó làm ký tự khớp.
Ví dụ biểu thức chính quy `.` được sử dụng để khớp với bất kỳ ký tự nào ngoại trừ ký tự xuống dòng. Bây giờ để khớp ký tự `.` trong chuỗi đầu vào, biểu thức chính quy `(f|c|m)at\.?`, biểu thị: chữ cái thường `f`, `c` hoặc `m` theo sau là chữ cái thường `a`, theo sau là chữ cái thường `t`, theo sau là ký tự `.` tùy chọn.<pre>"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a></pre>

## 2.8 Ký tự định vị

Trong biểu thức chính quy, để kiểm tra ký hiệu khớp có phải là ký hiệu bắt đầu hay ký hiệu kết thúc không, chúng ta sử dụng ký tự định vị.
Ký tự định vị có hai loại: loại thứ nhất là `^` kiểm tra ký tự khớp có phải là ký tự đầu tiên của chuỗi đầu vào không, loại thứ hai là `$`, nó kiểm tra ký tự khớp có phải là ký tự cuối cùng của chuỗi đầu vào không.

### 2.8.1 Ký hiệu chèn

Ký hiệu chèn `^` được sử dụng để kiểm tra ký tự khớp có phải là ký tự đầu tiên của chuỗi đầu vào không. Nếu chúng ta sử dụng biểu thức chính quy `^a` (để kiểm tra a là ký hiệu bắt đầu) khớp với chuỗi `abc`, nó sẽ khớp với `a`.
Nhưng nếu chúng ta sử dụng biểu thức chính quy `^b`, nó sẽ không khớp với bất cứ thứ gì, vì trong chuỗi `abc`, "b" không phải là ký tự bắt đầu.
Hãy xem một biểu thức chính quy khác `^(T|t)he`, điều này biểu thị: chữ cái hoa `T` hoặc chữ cái thường `t` là ký hiệu bắt đầu của chuỗi đầu vào, theo sau là chữ cái thường `h`, theo sau là chữ cái thường `e`.<pre>"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.</pre><pre>"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.</pre>

### 2.8.2 Ký hiệu đô la

Ký hiệu đô la `$` được sử dụng để kiểm tra ký tự khớp có phải là ký tự cuối cùng của chuỗi đầu vào không. Ví dụ biểu thức chính quy `(at\.)$`, biểu thị: chữ cái thường `a`, theo sau là chữ cái thường `t`, theo sau là một ký tự `.`, và bộ khớp này phải ở cuối chuỗi.<pre>"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a></pre><pre>"(at\.)$" => The fat cat sat on the m<a href="#learn-regex"><strong>at.</strong></a></pre>

## 3. Tập ký tự viết tắt

Biểu thức chính quy cung cấp các viết tắt cho các tập ký tự thường dùng và các biểu thức chính quy thường dùng. Các tập ký tự viết tắt như sau:

| Viết tắt | Mô tả                                                |
| :------: | ---------------------------------------------------- |
|    .     | Khớp với bất kỳ ký tự nào ngoại trừ ký tự xuống dòng |
|    \w    | Khớp với tất cả ký tự chữ cái và số: `[a-zA-Z0-9_]`  |
|    \W    | Khớp với ký tự không phải chữ cái và số: `[^\w]`     |
|    \d    | Khớp với chữ số: `[0-9]`                             |
|    \D    | Khớp với ký tự không phải chữ số: `[^\d]`            |
|    \s    | Khớp với ký tự khoảng trắng: `[\t\n\f\r\p{Z}]`       |
|    \S    | Khớp với ký tự không phải khoảng trắng: `[^\s]`      |

## 4. Assertion

Assertion hướng sau và assertion hướng trước đôi khi được gọi là assertion, chúng là loại đặc biệt của **_nhóm không bắt_** (được sử dụng để khớp mẫu, nhưng không được bao gồm trong danh sách khớp). Khi chúng ta có mẫu này trước hoặc sau một mẫu cụ thể, chúng ta sẽ ưu tiên sử dụng assertion.
Ví dụ, chúng ta muốn lấy tất cả các số có tiền tố `$` trong chuỗi đầu vào `$4.44 and $10.88`. Chúng ta có thể sử dụng biểu thức chính quy này `(?<=\$)[0-9\.]*`, biểu thị: lấy tất cả các số chứa ký tự `.` và có tiền tố là `$`.
Sau đây là các assertion được sử dụng trong biểu thức chính quy:

| Ký hiệu | Mô tả                         |
| :-----: | ----------------------------- |
|   ?=    | Positive lookahead assertion  |
|   ?!    | Negative lookahead assertion  |
|   ?<=   | Positive lookbehind assertion |
|   ?<!   | Negative lookbehind assertion |

### 4.1 Positive lookahead assertion

Positive lookahead assertion cho rằng phần đầu tiên của biểu thức phải là biểu thức assertion hướng trước. Kết quả khớp trả về chỉ chứa văn bản khớp với biểu thức phần đầu tiên.
Để định nghĩa một positive lookahead assertion trong một cặp ngoặc, dấu hỏi và dấu bằng được sử dụng như sau `(?=...)`. Biểu thức assertion hướng trước được viết sau dấu bằng trong ngoặc.
Ví dụ biểu thức chính quy `(T|t)he(?=\sfat)`, biểu thị: khớp chữ cái hoa `T` hoặc chữ cái thường `t`, theo sau là chữ cái `h`, theo sau là chữ cái `e`.
Trong ngoặc, chúng ta đã định nghĩa positive lookahead assertion, nó sẽ hướng dẫn engine biểu thức chính quy khớp `The` hoặc `the` theo sau là `fat`.<pre>"(T|t)he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.</pre>

### 4.2 Negative lookahead assertion

Khi chúng ta cần lấy nội dung không khớp với biểu thức từ chuỗi đầu vào, chúng ta sử dụng negative lookahead assertion. Định nghĩa negative lookahead assertion giống như định nghĩa positive lookahead assertion,
chỉ khác là thay vì dấu bằng `=`, chúng ta sử dụng ký hiệu phủ định `!`, ví dụ `(?!...)`.
Hãy xem biểu thức chính quy sau `(T|t)he(?!\sfat)`, biểu thị: lấy tất cả `The` hoặc `the` từ chuỗi đầu vào và không khớp với `fat` trước đó có thêm một ký tự khoảng trắng.<pre>"(T|t)he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.</pre>

### 4.3 Positive lookbehind assertion

Positive lookbehind assertion được sử dụng để lấy tất cả nội dung khớp trước một mẫu cụ thể. Positive lookbehind assertion được biểu thị bằng `(?<=...)`. Ví dụ biểu thức chính quy `(?<=(T|t)he\s)(fat|mat)`, biểu thị: lấy tất cả các từ `fat` và `mat` sau từ `The` hoặc `the` từ chuỗi đầu vào.<pre>"(?<=(T|t)he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.</pre>

### 4.4 Negative lookbehind assertion

Negative lookbehind assertion được sử dụng để lấy tất cả nội dung khớp không ở trước một mẫu cụ thể. Negative lookbehind assertion được biểu thị bằng `(?<!...)`. Ví dụ biểu thức chính quy `(?<!(T|t)he\s)(cat)`, biểu thị: lấy tất cả từ `cat` không ở sau `The` hoặc `the` trong chuỗi đầu vào.<pre>"(?&lt;!(T|t)he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.</pre>

## 5. Cờ đánh dấu

Cờ đánh dấu cũng được gọi là bộ sửa đổi, vì nó sửa đổi đầu ra của biểu thức chính quy. Các cờ này có thể được sử dụng theo bất kỳ thứ tự hoặc tổ hợp nào và là một phần của biểu thức chính quy.

| Cờ đánh dấu | Mô tả                                                                  |
| :---------: | ---------------------------------------------------------------------- |
|      i      | Không phân biệt hoa thường: Đặt khớp thành không phân biệt hoa thường. |
|      g      | Tìm kiếm toàn cục: Tìm kiếm tất cả khớp trong toàn bộ chuỗi đầu vào.   |
|      m      | Khớp đa dòng: Sẽ khớp mỗi dòng của chuỗi đầu vào.                      |

- **Chữ số**: `\d+$`
- **Tên người dùng**: `^[\w\d_.]{4,16}$`
- **Ký tự chữ và số**: `^[a-zA-Z0-9]*$`
- **Ký tự chữ và số có khoảng trắng**: `^[a-zA-Z0-9 ]*$`
- **Chữ cái thường**: `[a-z]+$`
- **Chữ cái hoa**: `[A-Z]+$`
- **URL**: `^(((http|https|ftp):\/\/)?([[a-zA-Z0-9]\-\.])+(\.)([[a-zA-Z0-9]]){2,4}([[a-zA-Z0-9]\/+=%&_\.~?\-]*))*$`
- **Ngày (MM/DD/YYYY)**: `^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$`
- **Ngày (YYYY/MM/DD)**: `^(19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$`
- **Cầu cập nhật cầu chia sẻ cảm ơn**: `[\(（【].*?[求更谢乐发推].*?[】）\)]`
- **Tìm chương mới nhất**: `您可以.*?查找最新章节`
- **ps/PS**: `(?i)ps\b.*`
- **Thẻ Html**: `<[^>]+?>`
