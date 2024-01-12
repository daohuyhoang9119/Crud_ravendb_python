# Project Title

Small application for CRUD API

## Team member

- Đào Huy Hoàng - 19521528
- Lê Minh Chánh - 21520596
- Trần Thị Kim Anh - 21520596
- Lê Thị Lệ Trúc - 21521882

## Target

- Understand RavenDB
- Know how to add/remove/update data in RavenDB
- Know how to connect RavenDB with Python
- Know how to use FastAPI, Uvicorn, PyravenDB

## Steps

- Install RavenDB
- Setup http link
- Install libraries in project
  http://localhost:8081/docs

------- QUERRY--------
Show danh sách các quốc gia và số lượng sản phẩm của quốc gia đó

```bash
    from Orders
    group by Company
    where count() > 0
    order by count() as long desc
    select count(), Company
```

Tìm khách hàng có địa chỉ bắt đầu bằng số 90

```bash
    from "Khachhangs"
    where startsWith(diachi, '90')

```

Sử dụng switch-case

```bash
declare function localizedResults(c) {
    switch(c.nuocsx)
    {
        case "TRUNGQUOC":
            return { TrungQuoc: c.gia };
        case "SINGAPORE":
            return { Singapore: c.gia};
        case "VIETNAM":
            return { VietNam: c.gia};
        default:
            return { Des: 'nothing' };
    }
}
from 'Sanphams' as s
select localizedResults(s)
```
