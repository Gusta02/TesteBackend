import requests
from requests.auth import HTTPBasicAuth

def transferencia(idDestino, idOrigem, valor_transferido):
    # Destinatario
    contaDestino = requests.get(f"http://127.0.0.1:8000/Banco/Contabancaria/{idDestino}/", auth=HTTPBasicAuth('gusta', '1234'))
    dataDestino = contaDestino.json()
    idContaDestino = dataDestino[0]['id']
    
    saldoAtualDestinatario = dataDestino[0]['saldo']

    saldoFinalDestinatario = float(saldoAtualDestinatario) + float(valor_transferido)

    jsonDestino = {**dataDestino[0], 'saldo':saldoFinalDestinatario}
    
    atualizandoContaDestino = requests.put(f"http://127.0.0.1:8000/contaBancaria/{idContaDestino}/", data = jsonDestino, auth=HTTPBasicAuth('gusta', '1234'))
  
    # Origem

    contaOrigem = requests.get(f"http://127.0.0.1:8000/Banco/Contabancaria/{idOrigem}/", auth=HTTPBasicAuth('gusta', '1234'))
    dataOrigem = contaOrigem.json()
    idContaOrigem = dataOrigem[0]['id']
    
    saldoAtualOrigem = dataOrigem[0]['saldo']

    saldofinalOrigem = float(saldoAtualOrigem) - float(valor_transferido)

    jsonOrigem = {**dataOrigem[0], 'saldo':saldofinalOrigem}


    atualizandoContaOrigem = requests.put(f"http://127.0.0.1:8000/contaBancaria/{idContaOrigem}/", data = jsonOrigem, auth=HTTPBasicAuth('gusta', '1234'))
    