#Exercício 04

var_01 = input('Insira algo: ')

print('O tipo do que você digitou é {}'.format(type(var_01)))

if var_01.isalpha():
    print('O que você digitou é alfabético')
# Uma string alfabética é uma string que contém apenas as letras
# presentes no alfabeto. Espaços, números e  símbolos não são 
# permitidos. Nota: 'ª' e 'º' são considerados alfabéticos
# para esse método.

if var_01.isalnum():
    print('O que você digitou é alfanumérico')
# Uma string alfanumérica é uma string que contém apenas as
# letras presentes no alfabeto e números de 0 a 9. Espaços e
# símbolos são não permitidos. Nota: 'ª' e 'º' são considerados
# alfabéticos para esse método.

if var_01.isupper():
    print('O que você digitou está tudo em maiúsculo')
# Nota: 'ª' e 'º' são considerados caracteres minúsculos para
# esse método.

if var_01.islower():
    print('O que você digitou está tudo em minúsculo')
# Nota: 'ª' e 'º' são considerados caracteres minúsculos para
# esse método.
    
if var_01.isnumeric():
    print('O que você digitou está tudo em numérico')

if var_01.isdigit():
    print('O que você digitou são apenas dígitos')

if var_01.isdecimal():
    print('O que você digitou é um número decimal')

if var_01.isascii():
    print('O que você digitou está presente na tabela ASCII')

if var_01.isidentifier():
    print('O que você digitou é um identificador')
# Identificador é uma string que contém apenas letras, números
# ou underlines e não podendo começar com um número ou conter
# espaços.

if var_01.isprintable():
    print('Todos os caracteres você digitou são imprimíveis')
# Alguns caracteres não são imprimíveis. Exemplo: '\n'.

if var_01.isspace():
    print('Todos os caracteres são espaços')

if var_01.istitle():
    print('O que você digitou é um título')
# Título são strings que contém palavras começadas em maíusculo
# e o resto dos caracteres da palavra em minúsculo. São ignorados
# símbolos não alfabéticos. Nota: 'ª' e 'º' são considerados
# caracteres minúsculos para esse método.
