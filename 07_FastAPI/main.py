from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import null

# BaseModel coloca todos os campos da class como required só deixa opcional aquieles que tem valor default


class Produto(BaseModel):
    id: int
    nome: str
    preco: float = 0
    em_ofeta: bool = False


app = FastAPI()

produtos = [
    Produto(id=1, nome="Produto1", preco=563.02, em_ofeta=True),
    Produto(id=2, nome="Produto2", preco=1233.02),
    Produto(id=3, nome="Produto3", preco=44444.01, em_ofeta=True),
    Produto(id=4, nome="Produto4", preco=5555.0),
    Produto(id=5, nome="Produto5", preco=4651.03, em_ofeta=True),
]


@app.get('/')
async def index():
    return ("Retornou", "Correto")


@app.get('/produtos')
async def buscar_todos_produtos():
    return produtos


@app.get('/produtos/{id}')
async def buscar_produtos(id: int = null):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


@app.put('/produtos/{id}')
async def atualiza_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto
            return {"msg": "Produto Atualizado", "produto": prod}
    return {"msg": "Produto não encontrado"}
