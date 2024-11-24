from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from typing import List, Optional

app = FastAPI()

# Modelo para os dados do cliente
class Cliente(BaseModel):
    id: int
    nome: str
    idade: int
    sexo: str
    email: str

# Função para carregar os dados do arquivo JSON
def carregar_clientes() -> List[Cliente]:
    with open('clientes.json', 'r') as f:
        return json.load(f)

@app.get('/clientes', response_model=List[Cliente])
def buscar_clientes(nome: Optional[str] = None):
    clientes = carregar_clientes()
    
    if nome:
        # Filtra clientes pelo nome
        clientes_filtrados = [cliente for cliente in clientes if nome.lower() in cliente['nome'].lower()]
        if not clientes_filtrados:  # Se não encontrar clientes
            raise HTTPException(status_code=404, detail="Cliente não encontrado.")
        return clientes_filtrados
    
    return clientes

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)