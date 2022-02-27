# Exercício 51

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print('Os 10 primeiros termos dessa PA são:')

for i in range(0, 10):
    print(primeiro_termo)
    primeiro_termo = primeiro_termo + razao
