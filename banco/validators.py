import re
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

# def cnpj_valido(numero_do_cnpj):
#     cnpj = CNPJ()
#     return cnpj.validate(numero_do_cnpj)

def nome_valido(nome):
    return nome.isalpha()

