# Exercício 19

import random

nome_primeiro_aluno = input('Digite o nome do primeiro aluno: ')
nome_segundo_aluno = input('Digite o nome do segundo aluno: ')
nome_terceiro_aluno = input('Digite o nome do terceiro aluno: ')
nome_quarto_aluno = input('Digite o nome do quarto aluno: ')

aluno_selecionado = random.choice((nome_primeiro_aluno, nome_segundo_aluno, nome_terceiro_aluno, nome_quarto_aluno))

print('O aluno selecionado é {}'.format(aluno_selecionado))
