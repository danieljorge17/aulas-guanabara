# Exercício 55

maior = 0
menor = -1

for i in range(0,5):
    peso = float(input('Digite o peso da pessoa: '))

    if peso > maior:
        maior = peso

    if peso < menor or menor == -1:
        menor = peso

print('O mais pesado possui {} kilos e o mais leve {} kilos'. format(maior, menor))
