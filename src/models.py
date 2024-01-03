from typing import List

class Nhanvien:
    def __init__(self, manv, hoten, sdt):
        self.manv = manv
        self.hoten = hoten
        self.sdt = sdt
        

class Khachhang:
    def __init__(self, makh, hoten, diachi, sdt, tongtien):
        self.makh = makh
        self.hoten = hoten
        self.sdt = sdt
        self.diachi = diachi
        self.tongtien = tongtien


class Sanpham:
    def __init__(self, masp, tensp, dvt, nuocsx, gia):
        self.masp = masp
        self.tensp = tensp
        self.dvt = dvt
        self.nuocsx = nuocsx
        self.gia = gia


class Hoadon:
    def __init__(self, sohd, nghd, makh, manv, trigia):
        self.sohd = sohd
        self.nghd = nghd
        self.makh = makh
        self.manv = manv
        self.trigia = trigia

class Cthd:
    def __init__(self, sohd, masp, sl):
        self.sohd = sohd
        self.masp = masp
        self.sl = sl

