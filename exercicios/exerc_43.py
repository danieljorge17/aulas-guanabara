# Exercício 43

peso    = float(input('Digite o seu peso: '))
altura  = float(input('Digite a sua altura: '))

imc = peso / altura ** 2

if imc > 40:
    print('Você está em obesidade mórbida')
elif imc >= 30:
    print('Você está em obesidade')
elif imc >= 25:
    print('Você está em sobrepeso')
elif imc >= 18.5:
    print('Você está em peso ideal')
else:
    print('Você está abaixo do peso')
