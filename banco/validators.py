import re
from validate_docbr import CPF, CNPJ

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def cnpj_valido(numero_do_cnpj):
    cnpj = CNPJ()
    return cnpj.validate(numero_do_cnpj)

def nome_valido(nome):
    return nome.isalpha()

