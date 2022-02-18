#Exercício 14

var_01 = float(input('Por quantos dias o carro foi alugado? '))

var_02 = float(input('Por quantos Km o carro rodou? '))

print('O valor do aluguel do carro é R$ {:.2f}'.format((var_01*60)+(var_02*0.15)))
