# Exercício 52

entrada = int(input('Digite um número: '))
eh_primo = True

for i in range(2, entrada):
    if not (entrada % i):
        print('O número {} não é primo'.format(entrada))
        eh_primo = False
        break

if eh_primo:
    print('O número {} é primo'.format(entrada))
