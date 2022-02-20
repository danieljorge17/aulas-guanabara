# Exercício 17

from math import sqrt, pow

cateto_adjacente = float(input('Digite comprimento do cateto adjacente: '))
cateto_oposto = float(input('Digite comprimento do cateto oposto: '))

hipotenusa = sqrt(pow(cateto_adjacente, 2)+ pow(cateto_oposto,2))

print('O comprimento da hipotenusa é {:.3f}'.format(hipotenusa))
