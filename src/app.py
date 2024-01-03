from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from pyravendb.store.document_store import DocumentStore
from src.models import  Khachhang, Nhanvien, Sanpham

app = FastAPI(title="Booking")
server = "http://127.0.0.1:8080"  
# http://26.57.247.94:8080
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

@app.delete("/employees")
async def remove_employee(employee_id:str):
    with store.open_session() as session:
        query = session.query_index("Nhanvien")
        query = query.where_equals("manv",employee_id)
        employee = query.firstOrDefault()
        if employee:
            session.advanced.clear()
            session.delete(employee)
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
        session.store(new_product)
        session.save_changes()

@app.delete("/products")
async def remove_product(product_id:str):
    with store.open_session() as session:
        query = session.query_index("Sanpham")
        query = query.where_equals("masp",product_id)
        product = query.firstOrDefault()
        if product:
            session.advanced.clear()
            session.delete(product)
            session.save_changes()
            return {"message": f"product have id:'{product_id}' deleted successfully"}
        else:
            return {"message": f"product have id:'{product_id}' not found"}
        

        
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

