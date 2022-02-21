# Exercício 29

velocidade = float(input('Qual a velocidade do carro em km/h? '))

if velocidade > 80.0:
    print('Você foi multado por excesso de velocidade!')
    print('O valor da multa é R${:.2f}'.format((velocidade - 80.0) * 7.0))
