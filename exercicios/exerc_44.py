# Exercício 44

valor = float(input('Qual o valor do produto? '))

print('[0] À vista em dinheiro, [1] À vista no cartão, [2] 2x no cartão, [3] 3x no cartão, [4] 4x e assim por diante')

forma_de_pagamento  = int(input('Qual a forma de pagamento? '))

if forma_de_pagamento >= 3:
    valor = valor * 1.2
elif forma_de_pagamento == 2:
    valor = valor
elif forma_de_pagamento == 1:
    valor = valor * 0.95
elif forma_de_pagamento == 0:
    valor = valor * 0.90
else:
    print('Forma de pagamento inválida')

print('O valor final do produto é R${:.2f}'.format(valor))
