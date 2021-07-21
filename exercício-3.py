import random
"""
A ideia é fazer cadastros de nome baseando em quanto fora doado, sendo que a cada 10R$ o nome é adiconado
na lista do sorteio.
"""
# ---------------| VARIÁVEIS |-----------
lista = ['Ruth','Ruth','Maria','Maria','Maria','Fernando',
         'Fernando','Fernando','Fernando','Fernando']
# -------------| ROTINAS |-------------
def cadastro(nome,valor,lista):
    """
    :param nome: nome a ser cadastrado
    :param valor: o valor doado
    :param lista: nome adcionado a lista
    A variável 'repetir' serve para saber quantas vezes o laço precisará repetir o nome na lista
    para ser equivalente a doação da pessoas a cada 10 R$
    A variável 'a' começa com o valor de 1, porque a repetição se inicia do zero ficando com um
    numero a mais no final
    """
    a = 1
    repetir = valor // 10
    while (a <= repetir):
        lista.append(nome)
        a += 1
# -------------| PROGRAMA PRINCIPAL |-----------
while True:
    """
    Um pequeno menu para o usuário escolher 
    """
    print('Escolha uma opção:')
    print('1 - Cadastrar um nome.')
    print('2 - Sortear um nome. ')
    print('3 - Sair do programa')
    op = int(input('>>:'))
    if op == 1:
        nome = input('Digite o nome para cadastrar:')
        valor = float(input('Digite o valor doado:'))
        cadastro(nome,valor,lista)
    elif op == 2:
        """
        Essa estrutura é igual a do exemplo dado pelo professor
        """
        random.shuffle(lista)
        sorteio = random.choice(lista)
        print('=-'*35)
        print( 'PARABÉNS!!!! \n {} por ter ganhado.'.format(sorteio))
        print('=-' * 35)
    elif op == 3:
        break
    else:
        continue