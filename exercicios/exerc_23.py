# Exercício 23

numero_int = int(input('Digite um número de 0 a 9999: '))

numero_float = float(numero_int/10000)

numero_int_trunc = int((numero_float%1)*10000)

numero_str = str(numero_int_trunc)

numero_str = (4 - len(numero_str)) * '0' + numero_str

print('Unidades: {}'.format(numero_str[3]))

print('Dezenas:  {}'.format(numero_str[2]))

print('Centenas: {}'.format(numero_str[1]))

print('Milhares: {}'.format(numero_str[0]))
