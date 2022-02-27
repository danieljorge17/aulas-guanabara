# Exercício 56

nomes  = []
idades = []
sexos  = []

idade_homem_mais_velho = -1

mulheres_maiores = 0

for i in range(0,4):
    nomes.append(str(input('Digite o nome da pessoa {}: '.format(i))).strip())
    idades.append(int(input('Digite a idade da pessoa {}: '.format(i))))
    sexos.append(str(input('Digite o sexo da pessoa {} (f/m): '.format(i))).lower().strip())

    if sexos[i] == 'm' and (idade_homem_mais_velho < idades[i] or idade_homem_mais_velho == -1) :
        idade_homem_mais_velho = idades[i]
        nome_homem_mais_velho = nomes[i]
    
    if sexos[i] == 'f' and idades[i] < 21:
        mulheres_maiores += 1

print('A média das idades é {:.2f}'.format(sum(idades)/4))
print('O nome do homem mais velho é {}'.format(nome_homem_mais_velho))
print('O número de mulheres com menos de 21 anos é {}'.format(mulheres_maiores))
