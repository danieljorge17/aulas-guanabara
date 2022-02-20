# Exercício 16

var_01 = float(input('Digite um número: '))

#print('A parte inteira desse número é {:.0f}'.format(var_01))

# Ou

#import math

#print('A parte inteira desse número é {:.0f}'.format(math.trunc(var_01)))

# Ou

from math import trunc

print('A parte inteira desse número é {:.0f}'.format(trunc(var_01)))
