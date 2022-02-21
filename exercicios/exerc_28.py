# Exercício 28

import random

numero_aleatorio = random.randrange(0,6)

numero_escolhido = int(input('Digite um número palpite entre 0 e 5: '))

if numero_aleatorio == numero_escolhido:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou!')
    print('O número certo era {}'.format(numero_aleatorio))
