# Exercício 44

from random import randrange

print('[0] Pedra, [1] Papel, [2] Tesoura')

escolha_maquina = randrange(0,3)

escolha_humano = int(input('Escolha dentre as opções? '))

print('A máquina escolheu {}'.format(escolha_maquina))

if escolha_humano == escolha_maquina:
    print('Empatados')
elif escolha_humano - 1 == escolha_maquina or (escolha_humano == 0 and escolha_maquina == 2):
    print('Você ganhou')
else:
    print('Você perdeu')
