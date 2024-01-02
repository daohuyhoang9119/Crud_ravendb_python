import datetime
from typing import Optional

from fastapi import FastAPI
from pyravendb.store.document_store import DocumentStore
from src.models import Book

app = FastAPI(title="Booking")
server = "http://127.0.0.1:8080"  
# http://26.57.247.94:8080
store = None


@app.on_event("startup")
async def on_startup():
    global store
    store = DocumentStore(urls=[server], database="booking")
    store.initialize()

@app.get("/books")
async def get_list_books():
    with store.open_session() as session:
        return list(session.query(object_type=Book))
    

@app.post("/books",status_code = 201)
async def add_book(title:str, author: str, published_year: datetime.datetime):
    with store.open_session() as session:
        new_book = Book(title, author, published_year)
        session.store(new_book)
        session.save_changes()


@app.delete("/books")
async def remove_book(title:str, author:str):
    with store.open_session() as session:
        query = session.query_index("Book")
        query = query.where_equals("title",title).and_also().where_equals("author",author)
        book = query.firstOrDefault()
        if book:
            session.advanced.clear()
            session.delete(book)
            session.save_changes()
            return {"message": f"Book '{title}' by '{author}' deleted successfully"}
        else:
            return {"message": f"Book '{title}' by '{author}' not found"}

# @app.get("/romaneios/")
# async def romaneios(numero_romaneio: Optional[int] = None):
#     with store.open_session() as session:
#         if numero_romaneio is None:
#             query_result = list(session.query(object_type=Romaneio))
#         else:
#             query_result = list(session.query(object_type=Romaneio).where(numero=numero_romaneio))
#         return query_result


# @app.post("/romaneios/", status_code=201)
# async def romaneio(numero: int, data_hora_carga: datetime.datetime, nome_destinatario: str, endereco: str, cidade: str,
#                    uf: str, nome_transportadora, nome_motorista, placa):
#     with store.open_session() as session:
#         romaneio = Romaneio(numero, data_hora_carga, destinatario=Destinatario(nome_destinatario, endereco, cidade, uf),
#                      transportador=Transportador(nome_transportadora, nome_motorista, placa), itens=[], updates=[])
#         session.store(romaneio)
#         session.save_changes()
#         return romaneio


# @app.post("/romaneios/{numero_romaneio}/adiciona_item/{qt_item}/{descricao}")
# async def romaneios(numero_romaneio: int, qt_item: int, descricao: str):
#     with store.open_session() as session:
#         romaneio = list(session.query(object_type=Romaneio).where(numero=numero_romaneio))[0]
#         romaneio.itens.append(Item(qt_volume=qt_item, descricao=descricao))
#         session.store(romaneio)
#         session.save_changes()
#         return romaneio
