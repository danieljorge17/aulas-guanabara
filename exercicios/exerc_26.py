# Exercício 26

frase = input('Digite uma frase: ')

print('A frase possui a letra "a" {} vezes'.format(frase.lower().count('a')))

print('A primeira aparição da letra "a" é na posição {}'.format(frase.lower().find('a')))

print('A ultima aparição da letra "a" é na posição {}'.format(frase.lower().rfind('a')))
