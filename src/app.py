from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from pyravendb.store.document_store import DocumentStore
from src.models import  Cthd, Hoadon, Khachhang, Nhanvien, Sanpham

app = FastAPI(title="Quan ly ban hang ⭐")
server = "http://26.57.247.94:8080"  
store = None


@app.on_event("startup")
async def on_startup():
    global store
    store = DocumentStore(urls=[server], database="QUANLYBANHANG")
    store.initialize()

#-----------NHANVIEN-------------------
        
@app.get("/employees")
async def get_list_employees():
    with store.open_session() as session:
        return list(session.query(object_type=Nhanvien))
    
@app.post("/employees",status_code = 201)
async def add_employee(hoten:str, manv: str, sdt: str):
    with store.open_session() as session:
        new_employee = Nhanvien(manv = manv,hoten = hoten, sdt = sdt)
        session.store(new_employee, key=manv)
        session.save_changes()

@app.put("/employees")
async def update_employee(employee_id,hoten,sdt):
    with store.open_session() as session:
        employee = list(session.query(object_type=Nhanvien).where_equals("manv", employee_id))[0] 
        print('emp: ',employee)
        if employee:
            employee.hoten = hoten
            employee.sdt = sdt
            session.save_changes()
            return {"message": f"employee have id:'{employee_id}' update successfully 👏"}
        else: 
            return {"message": f"employee have id:'{employee_id}' not found"}



@app.delete("/employees")
async def remove_employee(employee_id:str):
    with store.open_session() as session:
        employee = list(session.query(object_type=Nhanvien).where_equals("manv", employee_id) )
        if employee[0]:
            session.delete(employee[0])
            session.save_changes()
            return {"message": f"employee have id:'{employee_id}' deleted successfully"}
        else:
            return {"message": f"employee have id:'{employee_id}' not found"}
        

#-----------SANPHAM-------------------
        
@app.get("/products")
async def get_list_products():
    with store.open_session() as session:
        return list(session.query(object_type=Sanpham))
    
@app.post("/products",status_code = 201)
async def add_product( masp: str, tensp:str ,dvt: str, nuocsx: str, gia: float):
    with store.open_session() as session:
        new_product = Sanpham(masp = masp,tensp = tensp, dvt = dvt,nuocsx = nuocsx, gia = gia)
        session.store(new_product, key=masp)
        session.save_changes()

@app.delete("/products")
async def remove_product(masp: str):
    with store.open_session() as session:
        product = list(session.query(object_type=Sanpham).where_equals("masp", masp) )
        if product[0]:
            session.delete(product[0])
            session.save_changes()
            return {"message": f"product have id:'{masp}' deleted successfully"}
        else:
            return {"message": f"product have id:'{masp}' not found"}


        
#-----------CUSTOMERS-------------------
@app.get("/customers")
async def get_list_customers():
    with store.open_session() as session:
        return list(session.query(object_type=Khachhang))
    
@app.post("/customers",status_code = 201)
async def add_customer(makh: str, hoten:str ,sdt: str, diachi: str ,tongtien: float):
    with store.open_session() as session:
        new_customer = Khachhang(makh = makh, hoten = hoten, sdt = sdt,diachi = diachi,tongtien = tongtien )
        session.store(new_customer, key=makh)
        session.save_changes()


@app.delete("/customers")
async def remove_customer(makh: str):
    with store.open_session() as session:
        customer = list(session.query(object_type=Khachhang).where_equals("makh", makh) )
        if customer[0]:
            session.delete(customer[0])
            session.save_changes()
            return {"message": f"customer have id:'{makh}' deleted successfully"}
        else:
            return {"message": f"customer have id:'{makh}' not found"}




#---------HOADON--------------
@app.get("/orders")
async def get_list_orders():
    with store.open_session() as session:
        return list(session.query(object_type=Hoadon))
    
@app.post("/orders",status_code = 201)
async def add_order(sohd: str, makh: str, nghd: str, manv: str ,trigia: float):
    with store.open_session() as session:
        new_order = Hoadon(sohd = sohd ,makh = makh, nghd = nghd, manv = manv, trigia = trigia )
        session.store(new_order, key=sohd)
        session.save_changes()



@app.delete("/orders")
async def remove_order(sohd: str):
    with store.open_session() as session:
        order = list(session.query(object_type=Hoadon).where_equals("sohd", sohd) )
        if order[0]:
            session.delete(order[0])
            session.save_changes()
            return {"message": f"order have id:'{sohd}' deleted successfully"}
        else:
            return {"message": f"order have id:'{sohd}' not found"}



#---------CTHD--------------
@app.get("/order-detail")
async def get_list_orders():
    with store.open_session() as session:
        return list(session.query(object_type=Cthd))
    
@app.post("/order-detail",status_code = 201)
async def add_order_details(sohd: str, masp: str, sl: int):
    with store.open_session() as session:
        new_order_detail = Cthd(sohd = sohd ,masp = masp, sl = sl)
        session.store(new_order_detail)
        session.save_changes()


