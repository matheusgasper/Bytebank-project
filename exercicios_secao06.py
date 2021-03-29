"""
Exercícios Seção 06

2 - Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar a
estrutura de repetição for, a segunda while, e a terceira do while.

for numeros in range(3):
    for num in range(1, 101):
        print(num)
-----------------------------------------------------------------------------------------------------------
4 - Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000,
imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).
for numero in range(0, 100001, 1000):
    print(numero)

print('Sai do loop')
------------------------------------------------------------------------------------------------------------
8 - Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor lido.
num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
num3 = int(input('Digite o 3º valor: '))
num4 = int(input('Digite o 4º valor: '))
num5 = int(input('Digite o 5º valor: '))
num6 = int(input('Digite o 6º valor: '))
num7 = int(input('Digite o 7º valor: '))
num8 = int(input('Digite o 8º valor: '))
num9 = int(input('Digite o 9º valor: '))
num10 = int(input('Digite o 10º valor: '))

# Exemplo 1 com lista
lista = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
print(min(lista))
print(max(lista))

# Exemplo 2 sem lista
print(min(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10))
print(max(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10))
----------------------------------------------------------------------------------------------------------
18 - Escreva um algoritmo que leia certa quantidade de numeros e imprima o maior deles e quantas
vezes o maior numero foi lido. A quantidade de numeros a serem lidos deve ser fornecida pelo usuario.
from collections import Counter

num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
num3 = int(input('Digite o 3º valor: '))
num4 = int(input('Digite o 4º valor: '))
num5 = int(input('Digite o 5º valor: '))

lista = [num1, num2, num3, num4, num5]
print(max(lista))

vezes_lido = Counter(lista)

print(max(vezes_lido.most_common()))
------------------------------------------------------------------------------------------------------------
32 - Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saida
o numero de cada dado e a relação entre eles (>,<,=) de cada lançamento.
jogada = int(input('Digite quantas vezes quer lançar os dados: '))

from random import randint

for d1 in range(1, jogada + 1):
    print('Dado 1')
    print(randint(1, 7))

print('------------------------------')

for d2 in range(1,jogada + 1):
    print('Dado 2')
    print(randint(1, 7))
-------------------------------------------------------------------------------------------------------------
60 - Faça um programa que leia varios numeros, calcule e mostre:
(a) A soma dos numeros digitados
(b) A quantidade de numeros digitados
(c) A média dos numeros digitados
(d) O maior numero digitado
(e) O menor numero digitado
(f) A media dos numeros pares

from collections import Counter

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
num4 = int(input('Digite o 4º número: '))
num5 = int(input('Digite o 5º número: '))

lista = [num1, num2, num3, num4, num5]

a = num1 + num2 + num3 + num4 + num5
b = Counter(lista)
c = a / 5

print(f'A soma dos números é {a} ')
print(b)
print(f'A média dos numeros digitados é {c} ')
print(max(lista))
print(min(lista))
-------------------------------------------------------------------------------------------
46 - Faça um programa que gera um numero aleatorio de 1 a 1000. O usuario deve tentar acertar
qual numero foi gerado, a cada tentativa o programa deverá informar se o chute é menor ou maior
que o numero gerado. O programa acaba quando o usuario acerta o numero gerado. O programa deve
informar em quantas tentativas o numero foi descoberto.

from random import randint

def jogo():
    for n in range(1):
        numero = randint(1, 5)
        chute = int(input('Qual o número gerado? '))
        if chute == numero:
            print('Parabéns, você acertou!!!')
            break
        elif chute > numero:
            print('O seu chute é maior do que o numero gerado')
            jogo()
        elif chute < numero:
            print('O seu chute é menor do que o numero gerado')
            jogo()

print(jogo())
-----------------------------------------------------------------------------------------------------------------
"""






