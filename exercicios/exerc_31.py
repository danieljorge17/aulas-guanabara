# Exercício 31

distancia = float(input('Digite a distância até o destino: '))

if distancia < 200.0:
    print('O valor da passagem é R$ {:.2f}'.format(distancia*0.5))
else:
    print('O valor da passagem é R$ {:.2f}'.format(distancia*0.45))