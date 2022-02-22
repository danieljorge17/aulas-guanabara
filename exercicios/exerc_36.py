# Exercício 36

valor_da_casa = float(input('Qual o valor da casa? '))

salario = float(input('Qual o seu salário? '))

anos = int(input('Em quantos anos você quer pagar essa casa? '))

valor_prestacao = valor_da_casa/anos/12

if valor_prestacao > salario * 0.3:
    print('Infelizmente você não tem condições de pagar por essa casa')
else:
    print('Muito bem, o valor da prestação fica de {:.2f}'.format(valor_prestacao))
