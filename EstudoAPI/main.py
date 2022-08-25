#BIBLIOTECAS IMPORTADAS
import requests
import json
#O JSON É IMPORTANTE PARA TROCA DE INFORMAÇÕES

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

#TEM QUE "MANDAR" SAIR DO FORMATO JSON E VIM PARA O PYTHON. TRANSFORMAR PRO FORMATO PYTHON
cotacoes = cotacoes.json()
cota_dolar = cotacoes['USDBRL']['bid'] #PEGANDO SOMENTE UMA COTAÇÃO
print(cota_dolar)
#AQUI PERCEBE-SE QUE VAI PRINTAR UM DICIONARIO

