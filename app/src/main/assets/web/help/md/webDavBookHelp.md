# Hướng dẫn sử dụng sách WebDav vắn tắt

> Trang trợ giúp này sẽ bật lên lần đầu vào, lần sau sẽ không xuất hiện nữa, nếu muốn xem, vui lòng nhấp góc trên bên phải "**⁝**" > Trợ giúp để xem trang này.

Mặc dù Legado chủ yếu là công cụ để đọc tiểu thuyết trực tuyến, nhưng để tiện lợi cho bạn đọc, cũng cung cấp một số hỗ trợ đơn giản cho việc đọc sách cục bộ (epub, txt)

Nhưng một khó khăn của việc đọc sách cục bộ là làm thế nào để đồng bộ tiến độ đọc và sách trên nhiều thiết bị, nếu đổi thiết bị thì sách cục bộ trên thiết bị cũ cũng phải nhập lại bằng tay, không thêm tiện lợi lắm.

Bản thân Legado không có máy chủ riêng, không có khả năng lưu trữ trên máy chủ như Duokan, WeChat Reading, nhưng Legado hỗ trợ sao lưu WebDav, vậy chúng ta cũng có thể tận dụng WebDav để đồng bộ sách.

### Điều kiện tiên quyết

1. Cấu hình vị trí lưu trữ sách (vị trí lưu trữ tải sách WebDav): Lần lượt nhấp Của tôi/Cài đặt khác/Vị trí lưu trữ sách, chọn vị trí lưu sách.

2. Cấu hình sao lưu WebDav (vị trí lưu sách WebDav): Của tôi/Sao lưu và khôi phục/Cài đặt WebDav. Ở đây cần cấu hình địa chỉ máy chủ, tài khoản, mật khẩu của sao lưu WebDav. Phương án cấu hình chi tiết không nói chi tiết ở đây, vui lòng xem bài viết này: [Đăng ký và cấu hình Jianguoyun · Yuque (yuque.com)](https://www.yuque.com/legado/wiki/fkx510) hoặc nhấp nút trợ giúp ở góc trên bên phải của trang đó để xem phương pháp cấu hình.

### Tải sách lên WebDav

Sau khi cấu hình xong WebDav, vào trang sách WebDav từ giao diện chính không có sách nào hiển thị, điều này rất bình thường vì trên máy chủ WebDav của chúng ta chưa có sách nào.

Hiện tại có ba cách để tải sách lên WebDav:

1. App tải sách cục bộ đã nhập.

   Nhấn giữ sách cục bộ đã nhập vào chi tiết sách > góc trên bên phải "**⁝**" tìm **Tải lên WebDav**, nhấp, chờ vài giây là có thể tải thành công.

2. App tải sách mạng đã cache.

   Giao diện chính góc trên bên phải nhấp cài đặt thêm > nhấp cache/xuất, ở trang này góc trên bên phải "**⁝**" tìm **Xuất đến WebDav** và đánh dấu. Thì khi xuất sách sẽ tự động tải một bản lên máy chủ WebDav.

3. Sử dụng client Jianguoyun/client dịch vụ WebDav tự xây để tải lên.

   Đối với đa số người dùng, tải lên qua App là đủ, nhưng một số người dùng có thể có số lượng sách khá lớn, chúng tôi không đề xuất bạn tải từng cuốn một qua App, cách tốt hơn là sử dụng client của dịch vụ WebDav bạn sử dụng để tải hàng loạt.

   Giả sử chúng ta sử dụng dịch vụ WebDav của Jianguoyun, vào [trang web chính thức Jianguoyun](https://www.jianguoyun.com/d/home#/), tải và cài đặt client tương ứng cho nền tảng, tìm thư mục legado/books, đây là nơi lưu trữ sách, bạn có thể tải hàng loạt sách vào thư mục này.

**Dù sử dụng cách nào ở trên để tải sách, để đảm bảo tải lên chính xác, tốt nhất sau khi tải sách bạn nên vào trang sách WebDav kiểm tra xem có thấy sách đã tải lên không.**

### Tải sách WebDav về cục bộ

Khác với nhiều cách tải lên, cách tải sách về cục bộ khá đơn giản.

Trong **trang sách WebDav** duyệt sách đã tải lên, tìm sách muốn tải, nhấp nút **Thêm vào kệ sách**, phần mềm sẽ tự động tải sách đó về cục bộ và thêm vào kệ sách.

### Lưu ý

- Nếu sử dụng dịch vụ WebDav của Jianguoyun, hạn ngạch lưu lượng miễn phí đủ cho việc đồng bộ cài đặt App và **ít sách**. Nhưng nếu là người dùng thường xuyên cần tải lên/tải xuống sách thì lưu lượng có thể không đủ, vui lòng chú ý lượng sử dụng cá nhân, tránh vượt quá hạn ngạch ảnh hưởng đồng bộ cài đặt App.

### Câu hỏi thường gặp

- Vào **trang sách WebDav** hiển thị "Lỗi lấy sách WebDav webDav chưa cấu hình".

  > Điều này là do chưa cấu hình dịch vụ đồng bộ WebDav, theo phương pháp cấu hình đồng bộ Webdav được đề cập trong điều kiện tiên quyết ở trên để cấu hình là được.

- Sách cục bộ thiết bị A tải lên có thể thấy trên thiết bị B không, có thể tự động thêm vào kệ sách không?

  > Nếu thiết bị A và thiết bị B cấu hình cùng dịch vụ WebDav, thì B ở **trang sách WebDav** sẽ thấy sách A tải lên. Nhưng không thể trực tiếp thấy sách đó trên kệ sách, điều này có thể sau này sẽ nghĩ phương án để làm, hiện tại phải tự mình ở **trang sách WebDav** tìm sách đó nhấp thủ công **Thêm vào kệ sách** để nhập.

- Tiến độ đọc/bookmark của sách cục bộ có đồng bộ không?

  > Có thể đồng bộ.
