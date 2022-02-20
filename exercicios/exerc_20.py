# Exercício 20

import random

nome_primeiro_aluno = input('Digite o nome do primeiro aluno: ')
nome_segundo_aluno = input('Digite o nome do segundo aluno: ')
nome_terceiro_aluno = input('Digite o nome do terceiro aluno: ')
nome_quarto_aluno = input('Digite o nome do quarto aluno: ')

ordem_de_apresentacao = [nome_primeiro_aluno, nome_segundo_aluno, nome_terceiro_aluno, nome_quarto_aluno]

random.shuffle(ordem_de_apresentacao)

print('A ordem de apresentação dos alunos é {}'.format(ordem_de_apresentacao))
