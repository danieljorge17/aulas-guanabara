# Exercício 50

soma = 0

for i in range(0, 6):
    entrada = int(input('Insira um número: '))
    if not (entrada % 2):
        soma = soma + entrada

print(soma)
