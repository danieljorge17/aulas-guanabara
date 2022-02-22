# Exercício 37

numero = int(input('Digite um número inteiro: '))

print('[1] Binário, [2] Octal, [3] Hexadecimal')
base = str(input('Para qual base você deseja converter o número? '))

if base == '1':
    numero_bin = format(numero, 'b')
    print('O número escolhido na base binária é representado como: {}'.format(numero_bin))
elif base == '2':
    numero_oct = format(numero, 'o')
    print('O número escolhido na base octal é representado como: {}'.format(numero_oct))
elif base == '3':
    numero_hex = format(numero, 'x')
    print('O número escolhido na base hexadecimal é representado como: {}'.format(numero_hex))
else:
    print('Infelizmente não foi inserido um valor válido!')
