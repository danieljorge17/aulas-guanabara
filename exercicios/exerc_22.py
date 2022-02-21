# Exercício 22

nome_completo = input('Digite seu nome completo: ')

print('O seu nome com somente maiúsculas é {}'.format(nome_completo.upper()))

print('O seu nome com somente minúsculas é {}'.format(nome_completo.lower()))

print('O seu nome contém {} letras'.format(len(nome_completo) - nome_completo.count(' ')))

print('O seu primeiro nome é {}'.format(nome_completo.split()[0]))
