# Exercício 40

nota_um   = float(input('Qual foi sua primeira nota? '))
nota_dois = float(input('Qual foi sua segunda nota? '))

if (nota_um + nota_dois)/2 >= 7.0:
    print('Você está aprovado')
elif (nota_um + nota_dois)/2 >= 5.0:
    print('Você está de recuperação')
else:
    print('Você está reprovado')
