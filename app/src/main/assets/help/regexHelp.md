# Đang thì biểu đạt thức học tập

- [ Cơ bản phối hợp ]
- [ Chữ nguyên phù ]
- [ Tiếng Anh dấu chấm tròn ]
- [ Ký tự tụ tập ]
- [ Phủ định ký tự tụ tập ]
- [ Lặp lại ]
- [ Dấu sao ]
- [ Dấu cộng ]
- [ Dấu chấm hỏi ]
- [ Hoa dấu móc ]
- [ Ký tự tổ ]
- [ Chi nhánh kết cấu ]
- [ Chuyển nghĩa đặc thù ký tự ]
- [ Định vị phù ]
- [ Cắm vào ký hiệu ]
- [ Đẹp Nguyên Phù hào ]
- [ Viết chữ giản thể ký tự tụ tập ]
- [ Khẳng định ]
- [ Đang hướng đi trước khẳng định ]
- [ Phụ hướng đi trước khẳng định ]
- [ Đang hướng phía sau đi khẳng định ]
- [ Phụ hướng phía sau đi khẳng định ]
- [ Tiêu ký ]
- [ Không phân biệt chữ hoa hay thường ]
- [ Toàn cục lùng tìm ]
- [ Nhiều đi phối hợp ]
- [ Thường dùng đang thì biểu đạt thức ]
## 1. Cơ bản phối hợp

Đang thì biểu đạt thức chỉ là chúng ta dùng tại văn bản bên trong kiểm tra chữ cái cùng với con số hình thức. Tỷ như đang thì biểu đạt thức `cat`, biểu thị: Chữ cái `c` Đằng sau đi theo một chữ cái `a`, lại đằng sau đi theo một chữ cái `t`."cat" => The cat sat on the mat

Đang thì biểu đạt thức `123` Sẽ phối hợp ký tự xuyên "123". Thông qua đem đang thì biểu đạt thức bên trong mỗi cái ký tự từng cái cùng muốn phối hợp ký tự xuyên bên trong mỗi cái ký tự tiến hành so sánh, để hoàn thành đang thì phối hợp.

Đang thì biểu đạt thức bình thường phân chia chữ hoa hay thường, bởi vậy đang thì biểu đạt thức `Cat` Cùng ký tự xuyên "cat" Không phối hợp."Cat" => The cat sat on the Cat

## 2. Chữ nguyên phù

Chữ nguyên phù là đang thì biểu đạt thức cơ bản tạo thành nguyên tố. Chữ nguyên phù ở đây cùng nó bình thường biểu đạt ý tứ không giống nhau, mà là lấy một loại đặc thù nào đó hàm nghĩa đi giải thích. Có chút chữ nguyên phù viết tại dấu móc bên trong thời điểm có đặc thù hàm nghĩa.

Chữ nguyên phù như sau:
| Chữ nguyên phù | Miêu tả |
|:----:|----|
|.| Phối hợp trừ đổi đi phù bên ngoài tùy ý ký tự.|
|[ ]| Ký tự loại, phối hợp dấu móc bên trong bao hàm tùy ý ký tự.|
|[^ ]| Phủ định ký tự loại. Phối hợp dấu móc bên trong không bao hàm tùy ý ký tự |
|*| Phối hợp trước mặt tử biểu đạt thức linh lần hoặc nhiều lần |
|+| Phối hợp trước mặt tử biểu đạt thức một lần hoặc nhiều lần |
|?| Phối hợp trước mặt tử biểu đạt thức linh lần hoặc một lần, hoặc chỉ rõ một cái không phải tham lam hạn định phù.|
|{n,m}| Hoa dấu móc, phối hợp phía trước ký tự ít nhất n lần, nhưng mà không cao hơn m lần.|
|(xyz)| Ký tự tổ, dựa theo xác thực trình tự phối hợp ký tự xyz.|
||| Chi nhánh kết cấu, phối hợp ký hiệu trước đây ký tự hoặc phía sau ký tự.|
|\| Chuyển nghĩa phù, nó có thể trả lại như cũ chữ nguyên phù lúc đầu hàm nghĩa, cho phép ngươi phối hợp giữ lại ký tự [ ] ( ) { } . * + ? ^ $ \ ||
|^| Phối hợp làm được bắt đầu |
|$| Phối hợp làm được kết thúc |
## 2.1 tiếng Anh dấu chấm tròn

Tiếng Anh dấu chấm tròn `.` Là chữ nguyên phù ví dụ đơn giản nhất. Chữ nguyên phù `.` Có thể phối hợp tùy ý một cái ký tự. Nó sẽ không phối hợp đổi đi phù cùng mới làm được ký tự. Tỷ như đang thì biểu đạt thức `.ar`, biểu thị: Tùy ý ký tự đằng sau đi theo một chữ cái `a`,

Lại đằng sau đi theo một chữ cái `r`.".ar" => The car parked in the garage.
## 2.2 ký tự tụ tập

Ký tự tụ tập cũng xưng là ký tự loại. Dấu móc bị dùng chỉ định ký tự tụ tập. Sử dụng ký tự tụ tập bên trong liền ký tự chỉ định ký tự phạm vi. Dấu móc bên trong ký tự phạm vi trình tự cũng không trọng yếu.

Tỷ như đang thì biểu đạt thức `[Tt]he`, biểu thị: Viết kép `T` Hoặc viết chữ đơn `t` , gót chữ cái `h`, lại gót chữ cái `e`."[Tt]he" => The car parked in the garage.

Nhưng mà, ký tự tập trung tiếng Anh dấu chấm tròn biểu thị nó mặt chữ hàm nghĩa. Đang thì biểu đạt thức `ar[.]`, biểu thị viết chữ đơn chữ cái `a`, đằng sau đi theo một chữ cái `r`, lại đằng sau đi theo một cái tiếng Anh dấu chấm tròn `.` Ký tự."ar[.]" => A garage is a good place to park a car.
### 2.2.1 phủ định ký tự tụ tập

Nói như vậy cắm vào ký tự `^` Biểu thị một cái ký tự chuỗi bắt đầu, nhưng mà khi nó tại dấu móc bên trong lúc xuất hiện, nó sẽ hủy bỏ ký tự tụ tập. Tỷ như đang thì biểu đạt thức `[^c]ar`, biểu thị: Ngoại trừ chữ cái `c` Bên ngoài tùy ý ký tự, đằng sau đi theo ký tự `a`,

Lại đằng sau đi theo một chữ cái `r`."[^c]ar" => The car parked in the garage.
## 2.3 lặp lại

Phía dưới chữ nguyên phù `+`, `*` Hoặc `?` Dùng chỉ định tử hình thức có thể xuất hiện bao nhiêu lần. Những thứ này chữ nguyên phù tại khác biệt tình huống ở dưới tác dụng khác biệt.
### 2.3.1 dấu sao

Nên ký hiệu `*` Biểu thị phải phù hợp một cái phối hợp quy tắc linh lần hoặc nhiều lần. Đang thì biểu đạt thức `a*` Biểu thị viết chữ đơn chữ cái `a` Có thể lặp lại linh lần hoặc nhiều lần. Nhưng mà nếu như nó xuất hiện tại ký tự tụ tập hoặc ký tự loại sau đó, nó biểu thị toàn bộ ký tự tụ tập lặp lại.

Tỷ như đang thì biểu đạt thức `[a-z]*`, biểu thị: Một nhóm bên trong có thể bao hàm tùy ý số lượng viết chữ đơn chữ cái."[a-z]*" => The car parked in the garage #21.

Nên `*` Ký hiệu có thể cùng Nguyên Phù hào `.` Dùng tại cùng một chỗ, dùng để phối hợp tùy ý ký tự xuyên `.*`. Nên `*` Ký hiệu có thể cùng khoảng trắng phù `\s` Cùng một chỗ sử dụng, dùng để phối hợp một chuỗi khoảng trắng ký tự.

Tỷ như đang thì biểu đạt thức `\s*cat\s*`, biểu thị: Linh cái hoặc nhiều cái khoảng trắng, đằng sau cùng viết chữ đơn chữ cái `c`, lại đằng sau cùng viết chữ đơn chữ cái `a`, lại lại đằng sau cùng viết chữ đơn chữ cái `t`, đằng sau lại cùng linh cái hoặc nhiều cái khoảng trắng."\s*cat\s*" => The fat cat sat on the cat.
### 2.3.2 dấu cộng

Nên ký hiệu `+` Phải phù hợp một cái ký tự một lần hoặc nhiều lần. Tỷ như đang thì biểu đạt thức `c.+t`, biểu thị: Một cái viết chữ đơn chữ cái `c`, gót tùy ý số lượng ký tự, gót viết chữ đơn chữ cái `t`."c.+t" => The fat cat sat on the mat.
### 2.3.3 dấu chấm hỏi

Tại đang thì biểu đạt thức bên trong, chữ nguyên phù `?` Dùng để biểu thị phía trước một cái ký tự là có thể chọn . Nên ký hiệu phối hợp phía trước một cái ký tự linh lần hoặc một lần.

Tỷ như đang thì biểu đạt thức `[T]?he`, biểu thị: Có thể chọn viết kép chữ cái `T`, đằng sau cùng viết chữ đơn chữ cái `h`, gót viết chữ đơn chữ cái `e`."[T]he" => The car is parked in the garage."[T]?he" => The car is parked in the garage.
## 2.4 hoa dấu móc

Tại đang thì biểu đạt thức bên trong hoa dấu móc ( Cũng được xưng là lượng từ ?) dùng chỉ định ký tự hoặc một tổ ký tự có thể tái diễn số lần. Tỷ như đang thì biểu đạt thức `[0-9]{2,3}`, biểu thị: Phối hợp ít nhất 2 chữ số chữ nhưng không cao hơn 3 vị (0 đến 9 phạm vi bên trong ký tự )."[0-9]{2,3}" => The number was 9.9997 but we rounded it off to 10.0.

Chúng ta có thể tỉnh lược con số thứ hai. Tỷ như đang thì biểu đạt thức `[0-9]{2,}`, biểu thị: Phối hợp 2 cái hoặc càng nhiều hơn con số. Nếu như chúng ta cũng xóa bỏ dấu phẩy, thì đang thì biểu đạt thức `[0-9]{2}`, biểu thị: Phối hợp vừa vặn vì 2 con số con số."[0-9]{2,}" => The number was 9.9997 but we rounded it off to 10.0."[0-9]{2}" => The number was 9.9997 but we rounded it off to 10.0.
## 2.5 ký tự tổ

Ký tự tổ là một tổ viết tại tròn trong dấu ngoặc tử hình thức `(...)`. Chính như chúng ta tại đang thì biểu đạt thức bên trong thảo luận như thế, nếu như chúng ta đem một cái lượng từ đặt ở một cái ký tự sau đó, nó sẽ lặp lại phía trước một cái ký tự.

Nhưng mà, nếu như chúng ta đem lượng từ đặt ở một cái ký tự tổ sau đó, nó sẽ lặp lại toàn bộ ký tự tổ.

Tỷ như đang thì biểu đạt thức `(ab)*` Biểu thị phối hợp linh cái hoặc nhiều cái ký tự xuyên "ab". Chúng ta còn có thể tại ký tự tổ bên trong sử dụng chữ nguyên phù `|`. Tỷ như đang thì biểu đạt thức `(c|g|p)ar`, biểu thị: Viết chữ đơn chữ cái `c`, `g` Hoặc `p` Đằng sau cùng chữ cái `a`, gót chữ cái `r`."(c|g|p)ar" => The car is parked in the garage.
## 2.6 chi nhánh kết cấu

Tại đang thì biểu đạt thức bên trong thẳng đứng đầu `|` Dùng để định nghĩa chi nhánh kết cấu, chi nhánh kết cấu giống như nhiều cái biểu đạt thức ở giữa điều kiện. Hiện tại có thể cho rằng cái này ký tự tụ tập cùng chi nhánh cơ quan phương thức làm việc một dạng.

Nhưng mà ký tự tụ tập cùng chi nhánh kết cấu cực lớn khác nhau là ký tự tụ tập chỉ ở ký tự trên cấp bậc có tác dụng, nhưng mà chi nhánh kết cấu đang biểu đạt thức trên cấp bậc vẫn như cũ có thể sử dụng.

Tỷ như đang thì biểu đạt thức `(T|t)he|car`, biểu thị: Viết kép chữ cái `T` Hoặc viết chữ đơn chữ cái `t`, đằng sau cùng viết chữ đơn chữ cái `h`, gót viết chữ đơn chữ cái `e` Hoặc viết chữ đơn chữ cái `c`, gót viết chữ đơn chữ cái `a`, gót viết chữ đơn chữ cái `r`."(T|t)he|car" => The car is parked in the garage.
## 2.7 chuyển nghĩa đặc thù ký tự

Đang thì biểu đạt thức bên trong sử dụng phản liếc đòn khiêng `\` Tới chuyển nghĩa cái tiếp theo ký tự. Cái này đem cho phép ngươi sử dụng giữ lại ký tự tới xem như phối hợp ký tự `{ } [ ] / \ + * . $ ^ | ?`. Tại đặc thù ký tự phía trước thêm `\`, liền có thể sử dụng nó tới làm phối hợp ký tự.

Tỷ như đang thì biểu đạt thức `.` Là dùng để phối hợp ngoại trừ đổi đi phù bên ngoài tùy ý ký tự. Bây giờ muốn tại đưa vào ký tự xuyên bên trong phối hợp `.` Ký tự, đang thì biểu đạt thức `(f|c|m)at\.?`, biểu thị: Viết chữ đơn chữ cái `f`, `c` Hoặc `m` Gót viết chữ đơn chữ cái `a`, gót viết chữ đơn chữ cái `t`, gót có thể chọn `.` Ký tự."(f|c|m)at\.?" => The fat cat sat on the mat.
## 2.8 định vị phù

Tại đang thì biểu đạt thức bên trong, vì kiểm tra phối hợp ký hiệu có phải là hay không mở đầu ký hiệu hoặc phần cuối ký hiệu, chúng ta sử dụng định vị phù.

Định vị phù có hai loại loại hình: Loại thứ nhất loại hình là `^` Kiểm tra phối hợp ký tự có phải là hay không mở đầu ký tự, loại thứ hai loại hình là `$`, nó kiểm tra phối hợp ký tự có phải là hay không đưa vào ký tự chuỗi cái cuối cùng ký tự.
### 2.8.1 cắm vào ký hiệu

Cắm vào ký hiệu `^` Ký hiệu dùng kiểm tra phối hợp ký tự có phải là hay không đưa vào ký tự chuỗi thứ nhất ký tự. Nếu như chúng ta sử dụng đang thì biểu đạt thức `^a` ( Nếu như a là mở đầu ký hiệu ) phối hợp ký tự xuyên `abc`, nó sẽ phối hợp đến `a`.

Nhưng mà nếu như chúng ta sử dụng đang thì biểu đạt thức `^b`, nó là phối hợp không đến bất luận cái gì đồ vật , bởi vì tại ký tự xuyên `abc` Bên trong "b" Không phải mở đầu ký tự.

Để chúng ta đến xem một cái khác đang thì biểu đạt thức `^(T|t)he`, cái này biểu thị: Viết kép chữ cái `T` Hoặc viết chữ đơn chữ cái `t` Là đưa vào ký tự chuỗi mở đầu ký hiệu, đằng sau đi theo viết chữ đơn chữ cái `h`, gót viết chữ đơn chữ cái `e`."(T|t)he" => The car is parked in the garage."^(T|t)he" => The car is parked in the garage.
### 2.8.2 đẹp Nguyên Phù hào

USD `$` Ký hiệu dùng kiểm tra phối hợp ký tự có phải là hay không đưa vào ký tự chuỗi cái cuối cùng ký tự. Tỷ như đang thì biểu đạt thức `(at\.)$`, biểu thị: Viết chữ đơn chữ cái `a`, gót viết chữ đơn chữ cái `t`, gót một cái `.` Ký tự, lại cái này phối hợp khí nhất định phải là ký tự chuỗi phần cuối."(at\.)" => The fat cat. sat. on the mat."(at\.)$" => The fat cat sat on the mat.
## 3. Viết chữ giản thể ký tự tụ tập

Đang thì biểu đạt thức vì thường dùng ký tự tụ tập cùng thường dùng đang thì biểu đạt thức cung cấp viết chữ giản thể. Viết chữ giản thể ký tự tụ tập như sau:
| Viết chữ giản thể | Miêu tả |
|:----:|----|
|.| Phối hợp trừ đổi đi phù bên ngoài tùy ý ký tự |
|\w| Phối hợp tất cả chữ cái cùng với con số ký tự: `[a-zA-Z0-9_]`|
|\W| Phối hợp không phải chữ cái cùng với con số ký tự: `[^\w]`|
|\d| Phối hợp con số: `[0-9]`|
|\D| Phối hợp không phải con số: `[^\d]`|
|\s| Phối hợp khoảng trắng phù: `[\t\n\f\r\p{Z}]`|
|\S| Phối hợp không phải khoảng trắng phù: `[^\s]`|
## 4. Khẳng định

Làm sau khẳng định cùng đi trước khẳng định có đôi khi được xưng là khẳng định, bọn chúng là đặc thù loại hình *** Không phải bắt được tổ *** ( Dùng phối hợp hình thức, nhưng không bao gồm tại phối hợp trong danh sách ). Coi chúng ta tại một loại đặc biệt hình thức phía trước hoặc sau đó có loại mô thức này lúc, sẽ ưu tiên sử dụng khẳng định.

Tỷ như chúng ta nghĩ thu hoạch đưa vào ký tự xuyên `$4.44 and $10.88` Bên trong mang theo tiền tố `$` tất cả con số. Chúng ta có thể sử dụng cái này đang thì biểu đạt thức `(?<=\$)[0-9\.]*`, biểu thị: Thu hoạch bao hàm `.` Ký tự lại tiền tố vì `$` tất cả con số.

Phía dưới là đang thì biểu đạt thức bên trong sử dụng khẳng định:
| Ký hiệu | Miêu tả |
|:----:|----|
|?=| Đang hướng đi trước khẳng định |
|?!| Phụ hướng đi trước khẳng định |
|?<=| Đang hướng phía sau đi khẳng định |
|?"(T|t)he(?=\sfat)" => The fat cat sat on the mat.
### 4.2 phụ hướng đi trước khẳng định

Coi chúng ta cần từ đưa vào ký tự xuyên bên trong thu hoạch không phối hợp biểu đạt thức nội dung lúc, sử dụng phụ hướng đi trước khẳng định. Phụ hướng đi trước khẳng định định nghĩa cùng chúng ta định nghĩa đang hướng đi trước khẳng định một dạng,

Khác biệt duy nhất có phải hay không ngang bằng `=`, chúng ta sử dụng phủ định ký hiệu `!`, tỷ như `(?!...)`.

Chúng ta đến xem phía dưới đang thì biểu đạt thức `(T|t)he(?!\sfat)`, biểu thị: Từ đưa vào ký tự xuyên bên trong thu hoạch toàn bộ `The` Hoặc `the` Lại không phối hợp `fat` Phía trước tăng thêm một cái khoảng trắng ký tự."(T|t)he(?!\sfat)" => The fat cat sat on the mat.
### 4.3 đang hướng phía sau đi khẳng định

Đang hướng phía sau đi khẳng định là dùng thu hoạch tại đặc biệt hình thức trước đây tất cả phối hợp nội dung. Đang hướng phía sau đi khẳng định biểu thị vì `(?<=...)`. Tỷ như đang thì biểu đạt thức `(?<=(T|t)he\s)(fat|mat)`, biểu thị: Từ đưa vào ký tự xuyên bên trong thu hoạch tại từ đơn `The` Hoặc `the` Sau đó tất cả `fat` Cùng `mat` Từ đơn."(?<=(T|t)he\s)(fat|mat)" => The fat cat sat on the mat.
### 4.4 phụ hướng phía sau đi khẳng định

Phụ hướng phía sau đi khẳng định là dùng thu hoạch không tại đặc biệt hình thức trước đây tất cả phối hợp nội dung. Phụ hướng phía sau đi khẳng định biểu thị vì `(?"(? The cat sat on cat.
## 5. Tiêu ký

Tiêu ký cũng xưng là tân trang phù, bởi vì nó sẽ sửa chữa đang thì biểu đạt thức thu phát. Những thứ này tiêu chí có thể lấy tùy ý trình tự hoặc tổ hợp sử dụng, hơn nữa là đang thì biểu đạt thức một bộ phận.
| Tiêu ký | Miêu tả |
|:----:|----|
|i| Không phân biệt chữ hoa hay thường: Đem phối hợp thiết trí vì không phân biệt chữ hoa hay thường.|
|g| Toàn cục lùng tìm: Lùng tìm toàn bộ đưa vào ký tự xuyên bên trong tất cả phối hợp.|
|m| Nhiều đi phối hợp: Sẽ phối hợp đưa vào ký tự xuyên mỗi một đi.|
* ** Con số **: `\d+$`
* ** Người sử dụng tên **: `^[\w\d_.]{4,16}$`
* ** Chữ cái con số ký tự **: `^[a-zA-Z0-9]*$`
* ** Mang khoảng trắng chữ cái con số ký tự **: `^[a-zA-Z0-9 ]*$`
* ** Viết chữ đơn chữ cái **: `[a-z]+$`
* ** Viết kép chữ cái **: `[A-Z]+$`
* ** Địa chỉ Internet **: `^(((http|https|ftp):\/\/)?([[a-zA-Z0-9]\-\.])+(\.)([[a-zA-Z0-9]]){2,4}([[a-zA-Z0-9]\/+=%&_\.~?\-]*))*$`
* ** Ngày (MM/DD/YYYY)**: `^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$`
* ** Ngày (YYYY/MM/DD)**: `^(19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$`
* ** Cầu càng cầu phát gửi tới lời cảm ơn **: `[\((【].*?[ Cầu càng tạ nhạc phát đẩy ].*?[】)\)]`
* ** Tra tìm chương mới nhất **: ` Ngài có thể.*? Tra tìm chương mới nhất `
* **ps/PS**: `(?i)ps\b.*`
* **Html nhãn hiệu **: `<[^>]+?>`
