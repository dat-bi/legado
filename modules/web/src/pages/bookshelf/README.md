# Web cho “Legado 3.0” (đã đóng gói trong Legado 3.0, không thể đặt IP)

Chương trình này là web đi kèm cho “Legado 3.0”. Hãy đảm bảo điện thoại và máy tính ở cùng một mạng LAN, sau đó bật dịch vụ web trên điện thoại.

~~在线地址 http://alanskycn.gitee.io/vip/reader/~~

## Triển khai

Phát triển bằng Vue3

## Tính năng

- Lưu trữ cục bộ lịch sử đọc và cài đặt
- Chuyển đổi chủ đề đọc
- Chế độ ban đêm
- Điều chỉnh cỡ chữ
- Điều chỉnh phông chữ
- Điều chỉnh độ rộng vùng đọc

## Cách sử dụng

```shell
pnpm install
# cài đặt phụ thuộc dự án
pnpm dev
# chạy chế độ phát triển
pnpm build
# đóng gói sản phẩm
pnpm lint:fix
# định dạng mã nguồn
```

- Khi debug có thể sửa địa chỉ trong `.env.development` để kết nối tới dịch vụ trên điện thoại
