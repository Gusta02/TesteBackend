import re
from urllib.robotparser import RequestRate
import requests
from validate_docbr import CPF, CNPJ

def cpf_cnpj_valido(numero_do_cpf_cnpj):

    if len(numero_do_cpf_cnpj) == 11:
        cpf = CPF()
        resultado = cpf.validate(numero_do_cpf_cnpj)
    elif len(numero_do_cpf_cnpj) == 14:
        cnpj = CNPJ()
        resultado = cnpj.validate(numero_do_cpf_cnpj)
    else:
        resultado = False

    return resultado

def nome_valido(nome):
    return nome.isalpha()

def numero_conta(conta):
    if conta == int:
        resposta = True
    else:
        resposta = False
    return resposta

def permissao_user(id):
    tipoUser = requests.get(f'http://127.0.0.1:8000/Usuario/{id}/Tipo/')
    if tipoUser['Usuario'] == True:
        resposta = False
    else:
        resposta = True
    return resposta

def Valida_valorTransferencia(idUser, valorTransferencia):
    saldo = requests.get(f"http://127.0.0.1:8000/SaldoBancario/{idUser}/Saldo/")

    if saldo['saldo_total'] >= valorTransferencia:
        resposta = True
    else:
        resposta = False
    return resposta

def valida_api():
    autenticacao = requests.get('https://run.mocky.io/v3/d02168c6-d88d-4ff2-aac6-9e9eb3425e31')
    if autenticacao['authorization'] == True:
        resposta = True
    else:
        resposta = False
    return resposta



 
