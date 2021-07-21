"""
Propostar do exercício era criar um e-mail a partir 
da primeira letra do nome, concatenar com o sobrenome e o RU
com o domínio '@algoritmos.com.br"
"""


# variável para criar lista
nome = []
dominio = '@algoritmos.com.br'
# ------| ROTINAS |--------
def email():# função pra criar o e-mail
    nome.append(input('Digite seu nome:'))
    snome = (input('Digite seu sobrenome:'))
    num = (input('Digite os dois últimos digitos do seu RU:'))
    # concatenação da primeira letra do nome com o sobrenome com o RU
    nome1 = nome[0][0] + snome
    res =('Sr. {} {} , seu e-mail é {}{}{}'.format(nome[0],snome,nome1,num,dominio))
    return res
# ---| PROGRAMA PRINCIPAL |------------
print('Cadastrar e-mail')
a = email()
# imprime os retorno da função
print(a)