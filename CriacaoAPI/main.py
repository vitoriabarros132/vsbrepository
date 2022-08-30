from datetime import datetime
from enum import Enum
from fastapi import FastAPI


# CRIAÇÃO DA CLASSE ENUM
class Modelo(str, Enum):
    data = datetime.today().strftime('%d-%m-%Y')
    hora = datetime.today().strftime('%H:%M:%S')


# CRIANDO UMA INSTÂNCIA PARA A CLASSE FASTAPI, CRIANDO O APP
app = FastAPI()


# CRIAÇÃO DE ROTA/ENDPOINT
@app.get('/')  # GET -> PEGAR INFO
def home():  # HOMEPAGE
    return "Homepage :)"


@app.get('/data')
def data():
    return Modelo.data


@app.get('/hora')
def hora():
    return Modelo.hora


'''
APÓS ISSO, EXECUTAR O SERVIDOR PELO TERMINAL COM O COMANDO
uvicorn main:app --reload
PARA O SERVIDOR RODAR NO PC, UTILIZA-SE O UVICORN (SERVIDOR LOCAL)
>>uvicorn (nome do arquivo sem o .py): [executar o app] --reload (qualquer alteração, já joga na api)<<


PARA ACESSAR A RESPOSTA, BASTA ACESSAR 
http://127.0.0.1:8000  -> VAI PARA O ARQUIVO EM JSON
http://127.0.0.1:8000/docs -> VAI PARA O Swagger UI
http://127.0.0.1:8000/redoc -> DOCUMENTAÇÃO ALTERNATIVA PELO ReDoc
'''
