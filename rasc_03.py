# Rascunhos 03 - Brincando com a função print

var_01 = 'qualquer'

print('Uma frase {}'.format(var_01))

print('Uma frase {:>12}'.format(var_01))

print('Uma frase {:^12}'.format(var_01))

print('Uma frase {:<12}'.format(var_01))

print('Uma frase {:.^12}'.format(var_01))

print('Uma frase {: ^12}'.format(var_01))

print('Uma frase {:-^12}'.format(var_01))

print('Uma frase {:\^12}'.format(var_01))

var_02 = '!'

print('Uma frase {0}{1}'.format(var_01, var_02))

print('Uma frase {1}{0}'.format(var_01, var_02))

print('Uma frase {var_01}{var_02}'.format(var_01 = var_01, var_02 = var_02))

print('Uma frase {var_1}{var_2}'.format(var_1 = var_01, var_2 = var_02))

print('Uma frase {var_1}{var_2}'.format(var_2 = var_01, var_1 = var_02))

print('Uma frase {}'.format(var_01), end = var_02)

print('Uma frase {}'.format(var_01), end = var_02 + '\n')
