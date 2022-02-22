# Exercício 41

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Em que ano você nasceu? '))

if ano_atual - ano_nascimento > 25:
    print('Você está na categoria Master')
elif ano_atual - ano_nascimento >= 19:
    print('Você está na categoria Sênior')
elif ano_atual - ano_nascimento >= 14:
    print('Você está na categoria Junior')
elif ano_atual - ano_nascimento >= 9:
    print('Você está na categoria Infantil')
else:
    print('Você está na categoria Mirim')
