# Exercício 34

salario = float(input('Digite o valor do seu salário: '))

if salario <= 1250.00:
    salario = salario * 1.15
else:
    salario = salario * 1.1

print('Com o aumento o seu salário passa a ser R${:.2f}'.format(salario))
