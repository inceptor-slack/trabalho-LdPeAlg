"""
Proposta do exercício era gerar um conceito de nota a partir da entrada da nota
"""

entrada = int(input('Deseja inserir uma nota: 0-Não 1-Sim:'))# entrada da condição do laço
while entrada == 1:# condição do laço
# ------------| ENTRADA DE DADOS DO ALUNO |-------------
    nome = input('Digite o nome do aluno:')
    nota = float(input(('Digite a nota final:')))
# ------------| CONDIÇÕES PARA CONCEITO |----------------
    if nota <= 2.9:
        conceito = 'E'
        print('O aluno(a) {} tirou a nota {} e se enquadra no conceito {}'.format(nome,nota,conceito))
    elif nota >=3.0 and nota <=4.9:
        conceito = 'D'
        print('O aluno(a) {} tirou a nota {} e se enquadra no conceito {}'.format(nome,nota,conceito))
    elif nota >= 5.0 and nota <=5.9:
        conceito = 'C'
        print('O aluno(a) {} tirou a nota {} e se enquadra no conceito {}'.format(nome,nota,conceito))
    elif nota >= 7.0 and nota <= 8.9:
        conceito = 'B'
        print('O aluno(a) {} tirou a nota {} e se enquadra no conceito {}'.format(nome,nota,conceito))
    else:
        conceito = 'A'
        print('O aluno(a) {} tirou a nota {} e se enquadra no conceito {}'.format(nome,nota,conceito))
# ---------| CONDIÇÃO PARA REPETIÇÃO |---------
    entrada = int(input('Deseja inserir dados: 0-Não 1-Sim:'))