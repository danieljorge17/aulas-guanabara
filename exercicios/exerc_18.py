# Exercício 18

from math import tan, sin, cos, radians

entrada = radians(float(input('Digite o ângulo em graus: ')))

print('O valor do seno desse ângulo é {:.3f}'.format(sin(entrada)))
print('O valor do cosseno desse ângulo é {:.3f}'.format(cos(entrada)))
print('O valor da tangente desse ângulo é {:.3f}'.format(tan(entrada)))
