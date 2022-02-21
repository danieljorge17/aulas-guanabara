# Exercício 32

ano = input('Digite o ano: ')

if (ano[len(ano) - 1] + ano[len(ano) - 2]) == '00':
    if int(ano)%400:
        print('O ano não é bissexto')
    else:
        print('O ano é bissexto')
elif int(ano)%4:
    print('O ano não é bissexto')
else:
    print('O ano é bissexto')
