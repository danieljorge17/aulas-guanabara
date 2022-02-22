# Exercício 35

primeiro_numero = float(input('Digite o valor do primeiro lado '))
segundo_numero  = float(input('Digite o valor do segundo lado '))
terceiro_numero = float(input('Digite o valor do terceiro lado '))

if primeiro_numero >= segundo_numero:
    if primeiro_numero >= terceiro_numero:
        maior = primeiro_numero
    if segundo_numero >= terceiro_numero:
        medio = segundo_numero
        menor = terceiro_numero
    else:
        medio = terceiro_numero
        menor = segundo_numero

if segundo_numero >= primeiro_numero:
    if segundo_numero >= terceiro_numero:
        maior = segundo_numero
    if primeiro_numero >= terceiro_numero:
        medio = primeiro_numero
        menor = terceiro_numero
    else:
        medio = terceiro_numero
        menor = primeiro_numero

if terceiro_numero >= segundo_numero:
    if terceiro_numero >= primeiro_numero:
        maior = terceiro_numero
    if segundo_numero >= primeiro_numero:
        medio = segundo_numero
        menor = primeiro_numero
    else:
        medio = primeiro_numero
        menor = segundo_numero

if menor + medio > maior:
    print('Estes valores podem sim formar um triângulo')
else:
    print('Estes valores não podem formar um triângulo')
