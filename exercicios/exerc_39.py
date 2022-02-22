# Exercício 39

from datetime import date

ano_atual = date.today().year

ano_de_nascimento = int(input('Qual seu ano de nascimento? '))

if ano_atual - ano_de_nascimento == 18:
    print('Você precisa se alistar ainda esse ano')
elif ano_atual - ano_de_nascimento < 18:
    print('Você só precisa se alistar em {} anos'.format(18 - ano_atual + ano_de_nascimento))
else:
    print('Já passou {} anos do seu prazo de alistamento'.format(ano_atual - ano_de_nascimento - 18))
