# Exercício 54

from datetime import datetime, time

dia_de_hoje = datetime.today().day
mes_de_hoje = datetime.today().month
ano_de_hoje = datetime.today().year

pessoas_adultas = 0

for i in range(0,2):
    data_de_nascimento = str(input('Digite a data de nascimento da pessoa (Ex: DD/MM/AAAA): '))

    dia_de_nascimento = int(data_de_nascimento[0:2])
    mes_de_nascimento = int(data_de_nascimento[3:5])
    ano_de_nascimento = int(data_de_nascimento[6:])

    if not (ano_de_hoje - ano_de_nascimento <= 20):
        if ano_de_hoje - ano_de_nascimento > 21:
            pessoas_adultas += 1
        elif ano_de_hoje - ano_de_nascimento == 21:
            if mes_de_hoje >= mes_de_nascimento:
                if dia_de_hoje >= dia_de_nascimento:
                    pessoas_adultas += 1

print('O número de adutos é igual a {}'. format(pessoas_adultas))
