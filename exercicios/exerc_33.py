# Exercício 33

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero  = int(input('Digite o segundo número: '))
terceiro_numero = int(input('Digite o terceiro número: '))

if primeiro_numero >= segundo_numero:
    if primeiro_numero >= terceiro_numero:
        maior = primeiro_numero
    if segundo_numero >= terceiro_numero:
        menor = terceiro_numero
    else:
        menor = segundo_numero

if segundo_numero >= primeiro_numero:
    if segundo_numero >= terceiro_numero:
        maior = segundo_numero
    if primeiro_numero >= terceiro_numero:
        menor = terceiro_numero
    else:
        menor = primeiro_numero

if terceiro_numero >= segundo_numero:
    if terceiro_numero >= primeiro_numero:
        maior = terceiro_numero
    if segundo_numero >= primeiro_numero:
        menor = primeiro_numero
    else:
        menor = segundo_numero

print('O maior dentre esse números é {} e o menor é {}'.format(maior, menor))
