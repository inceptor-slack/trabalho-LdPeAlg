from operator import itemgetter
"""
Modifacar os dicionarios da lista
"""

# ---------| VARIÁVEIS |-------

lista = [{'codigo':1,'estoque':23,'minimo':56},
         {'codigo':5,'estoque':75,'minimo':50},
         {'codigo':20,'estoque':35,'minimo':20}]

# ---------| ROTINAS |--------
def addItem():
    cadastro = {}
    print('+','-'*33,'+')
    print('| Digite o código do produto:       ')
    cadastro['codigo'] = int(input('>>:'))
    print('| Digite a quantidade para estoque do produto:  ')
    cadastro['estoque'] = int(input('>>:'))
    print('| Qual quantidade mínima para estoque do produto:')
    cadastro['minimo'] = int(input('>>:'))
    print('+','-'*33,'+')
    lista.append(cadastro)
    return cadastro

def modItem(opm):
    opm-= 1
    print('Digite o código do produto:')
    codigo = int(input('>>:'))
    print('Digite a quantidade para estoque do produto')
    estoque = int(input('>>:'))
    print('Qual quantidade mínima para estoque do produto:')
    minimo = int(input('>>:'))
    lista[opm]['codigo'] = codigo
    lista[opm]['estoque'] = estoque
    lista[opm]['minimo'] = minimo
    return codigo, estoque, minimo

while True:
    print('+','-'*33,'+')
    print('| Qual a opção que deseja escolher: |')
    print('| 1 - Cadastrar um novo produto     |')
    print('| 2 - Modificar um item             |')
    print('| 3 - Ver estoque                   |')
    print('| 4 - Sair do programa              |')
    op = int(input('>>:'))
    print('+','-'*33,'+')
    if op == 1:
        a = addItem()
        if a != {'codigo': 0, 'estoque': 0, 'minimo': 0}:
            continue
        else:
            break
    elif op == 2:
        listaOrdem = sorted(lista, key=itemgetter('codigo'))
        for listas in listaOrdem:
            print(listas)
        print('Qual linha quer modificar:')
        opm = int(input('>>:'))
        a = modItem(opm)
        if a != (0,0,0):
            continue
        else:
            break
    elif op == 3:
        listaOrdem = sorted(lista, key=itemgetter('codigo'))
        for listas in listaOrdem:
                print(listas)
        continue
    elif op == 4:
        print('Encerrando o programa.')
        break
    elif op == 0:
        break
    else:
        continue