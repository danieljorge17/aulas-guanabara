# Exercício 27

nome_completo = input('Digite um nome completo: ')

print('O primeiro nome é {}'.format(nome_completo.split()[0]))

print('O último nome é {}'.format(nome_completo.split()[len(nome_completo.split()) - 1]))
