# Exercício 53

frase = str(input('Digite um número: ')).strip()
frase_sem_espacos = ''.join(frase.split())
frase_invertida = ''

for i in range(len(frase_sem_espacos), 0, -1):
    frase_invertida = frase_invertida + frase_sem_espacos[i-1]

if frase_invertida == frase_sem_espacos:
    print('A frase inserida é um palíndromo')
else:
    print('A frase inserida não é um palíndromo')
