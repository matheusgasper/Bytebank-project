"""
Exercícios Seção 07 Parte 1

1 - Faça um programa que possua um vetor denominado A que armazene 6 numeros inteiros.
O programa deve executar os seguintes passos:
(a) Atribua os seguinte valores a esse vetor: 1,0,5,-2,-5,7.
(b) Armazene em uma variavel a soma entre os valores das posições A[0], A[1] e A[5] do vetor e
mostre na tela esta soma.
(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.
listaA = []
print(listaA)
listaA.append(1)
listaA.append(0)
listaA.append(5)
listaA.append(-2)
listaA.append(-5)
listaA.append(7)
print(listaA)

soma = listaA[0] + listaA[1] + listaA[5]
print(soma)

listaA.insert(4, 100)
print(listaA)
------------------------------------------------------------------------------------------------------------
3 - Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado dos componentes deste
vetor, armazenando o resultado em outro vetor. Os conjuntos tem 10 elementos cada. Imprimir todos.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))
num6 = int(input("Digite um número: "))
num7 = int(input("Digite um número: "))
num8 = int(input("Digite um número: "))
num9 = int(input("Digite um número: "))
num10 = int(input("Digite um número: "))

listaA = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

quad1 = num1 ** 2
quad2 = num2 ** 2
quad3 = num3 ** 2
quad4 = num4 ** 2
quad5 = num5 ** 2
quad6 = num6 ** 2
quad7 = num7 ** 2
quad8 = num8 ** 2
quad9 = num9 ** 2
quad10 = num10 ** 2

listaB = [quad1, quad2, quad3, quad4, quad5, quad6, quad7, quad8, quad9, quad10]

print(listaA)
print(listaB)
--------------------------------------------------------------------------------------------------------------------
4 - Faça um programa que leia um vetor de 8 posições e em seguida leia também dois valores X e Y quaisquer
correspondentes a duas posiçoes do vetor. Ao final seu programa deverá escreve a soma dos valores encontrados
nas respectivas posições X e Y.
lista = [3, 6, 9, 12, 15, 18, 21, 24]

pos1 = int(input('Digite um valor: '))
pos2 = int(input('Digite um valor: '))

soma = lista[pos1] + lista[pos2]

print(lista)
print(soma)
----------------------------------------------------------------------------------------------------------------------
24 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno e o segundo
representando a sua altura. Encontre o aluno mais baixo e o mais alto. Mostre o nome do aluno mais baixo e do
mais alto juntamente com suas alturas.

alunos = {'Pedro': '1.69', 'João': '1.75', 'Eduardo': '1.92','Carlos': '1.82', 'Éder': '1.74',
          'Otávio': '1.95','Marcos': '1.80','Bruno': '1.71','Felipe': '1.89','Luciano': '1.72'}

alunos = {'Pedro': '1.69', 'João': '1.75', 'Eduardo': '1.92','Carlos': '1.82', 'Éder': '1.74',
          'Otávio': '1.95','Marcos': '1.80','Bruno': '1.71','Felipe': '1.89','Luciano': '1.72'}


alturaMax = max(alunos.values())
alturaMin = min(alunos.values())

for chave, valor in alunos.items():
    if valor == alturaMax:
        print(f"O aluno mais alto da sala é o {chave}, e mede {valor}.")
    elif valor == alturaMin:
        print(f"O aluno mais baixo da sala é o {chave} e mede {valor}.")
---------------------------------------------------------------------------------------------------------------------
34 - Faça um programa para ler 10 numeros diferentes a serem armazendados em um vetor. Os dados deverão ser
armazenados no vetor na ordem que forem sendo lidos, sendo que caso o usuario digite um numero que ja foi digitado
o programa devera pedir para ele digitar outro numero. Cada valor digitado pelo usuario deve ser pesquisado no vetor,
verificando se ele existe entre os numeros que ja foram fornecidos. Exibir na tela o vetor final que foi digitado.
vetor = []
quantidade = 0

while quantidade < 10:
    valor = int(input("Informe um Numero :"))
    if valor not in vetor:
        vetor.append(valor)
        quantidade = quantidade + 1
    else:
        print("numero ja repetido insira outro valor : ")

print(f"valor no vetor {vetor}")
--------------------------------------------------------------------------------------------------------------------
30 - Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os 2
vetores anteriorers, ou seja, que contém apenas os numeros que estao em ambos os vetores. Nao deve conter numeros
repetidos.
cont = 1
vetor1 = []
vetor2 = []

while cont <= 5:
    valores_vetor1 = int(input(f'Valor {cont}: '))
    valores_vetor2 = int(input(f'Valor {cont}: '))
    vetor1.append(valores_vetor1)
    vetor2.append(valores_vetor2)
    cont = cont + 1

print(vetor1)
print(vetor2)
print(set(vetor1).intersection(vetor2))
--------------------------------------------------------------------------------------------------------------------
21 - Faça um programa que receba do usuário dois vetores, A e B, com 10 numeros inteiros cada. Crie um novo
vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C.
quantidade = 1
vetorA = []
vetorB = []
vetorC = []

while quantidade <= 10:
    valores_vetorA = int(input(f'Valor {quantidade}: '))
    valores_vetorB = int(input(f'Valor {quantidade}: '))
    vetorA.append(valores_vetorA)
    vetorB.append(valores_vetorB)
    quantidade = quantidade + 1

print(vetorA)
print(vetorB)

for iA in vetorA:
    valor_A = iA
    for iB in vetorB:
        valor_B = iB
        if vetorA.index(iA) == vetorB.index(iB):
            valor_C = iA - iB
            vetorC.append(valor_C)
print(f'Vetor C (Vetor A - Vetor B: {vetorC}')

valores_vetorC = valores_vetorA - valores_vetorB
----------------------------------------------------------------------------------------------------------------------
Exercícios Seção 07 Parte 2

1 - Leia uma matriz 4x4, conte e escreva quantos valores maiores que 10 ela possui.
matriz = [[1, 25, 2, 8], [23, 5, 3, 14], [10, 0, 1, 9], [7, 8, 9, 4]]
n = 10
for elemento in matriz:
    print(matriz.count(elemento))
**TERMINAR**
--------------------------------------------------------------------------------------------------------------------
2 - Declare uma matriz 5x5. Preencha com 1 a diagonal principal e om 0 os demais elementos. Escreva ao final a matriz
obtida.

matriz = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

for linha in range(0, 5):
    for coluna in range(0, 5):
        print(f"[{matriz[linha][coluna]:^6}]", end='')
    print()
---------------------------------------------------------------------------------------------------------------------
4 - Leia uma matriz 4x4, imprima a matriz e retorne a localização (linha e coluna) do maior valor.
from random import uniform

matriz4x43 = [[int(uniform(-1.0, 1.0) * 100) for numero in range(1, 5)] for matriz in range(1, 5)]
print(matriz4x43)
maiorvalor = int()
linhamaior = list()
colunamaior = int()
for matriz in matriz4x43:
    for numero in matriz:
        if numero > maiorvalor:
            maiorvalor = numero
            linhamaior = matriz
            colunamaior = matriz.index(numero)
print(f'O maior valor da matriz é {maiorvalor} e encontra-se na posição [{matriz4x43.index(linhamaior)}][{colunamaior}]')
-------------------------------------------------------------------------------------------------------------------------
5 - Leia uma matriz 5x5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final,
escrever a localização (linha e coluna).

from random import uniform
matriz5x5 = [[int(uniform(-1.0, 1.0) * 100) for numero in range(1, 6)] for matriz in range(1, 6)]
print(matriz5x5)
valorX = int(input('Digite um valor: '))
linha = list()
coluna = int()
for matriz in matriz5x5:
    for numero in matriz:
        if numero == valorX:
            valorX = numero
            linha = matriz
            coluna = matriz.index(numero)
            print(f'O valor digitado {valorX} encontra-se na posição [{matriz5x5.index(linha)}][{coluna}]')
------------------------------------------------------------------------------------------------------------------------
15 - Leia uma matriz 5x10 que se refere as respostas de 10 questoes de multipla escolha, referentes a 5 alunos.
Leia tambem um vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou d. Seu programa
deverá comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo
a pontuação correspondendte a cada aluno.

import random

matriz = list()
gabarito = ('a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b')
respostas = list()
resultado = list()

for l in range(5):
    linha = []
    for c in range(10):
        linha.append(random.choice('abcd'))
    matriz.append(linha)
print('Gabarito:')
print('  a    b    c    d    a    b    c    d    a    b')
print('-x' * 30)
print('Matriz das notas. Aluno x Resposta')
for l in range(5):
    for c in range(10):
        print(f'{matriz[l][c]:^5}', end='')
    print()
for l in range(len(matriz)):
    for c in range(10):
        if matriz[l][c] == gabarito[c]:
            respostas.append(1)
        else:
            respostas.append(0)
    resultado.append(list(respostas))
    respostas.clear()
for i in range(5):
    nota = resultado[i].count(1)
    print(f'O aluno {i + 1} acertou {nota} e errou {10 - nota} questões')
----------------------------------------------------------------------------------------------------------------------
19 - Este programa lê o número de matrícula, a média das provas e a média dos trabalhos de 5 alunos, e exibe
a nota final (média aritmética \das provas e dos trabalhos) o aluno que tirou a maior nota, e a média das notas finais.
info_alunos = ('Matrícula', 'MédiaP', 'MédiaT')  # vetor para facilitar na hora do input

M = [[int(input(f'{info_alunos[i]}: ')) for i in range(3)] for _ in range(5)]  # preenchendo a matriz

for dados in M:  # inserindo a coluna das notas finais
    nota = (M[M.index(dados)][1] + M[M.index(dados)][2]) / 2  # média das notas de cada aluno
    dados.append(nota)

for linha in M:
    print(linha)

notas = [M[i][3] for i in range(5)]  # criando um vetor da última coluna
mat_maior_nota = M[notas.index(max(notas))][0]  # pegando a linha e a coluna da maior nota
media_notas = round(sum(notas) / 5, 3)  # média entre todas as notas

print(f'\nMatrícula do aluno de maior nota: {mat_maior_nota}'
      f'\nMédia das notas {media_notas}')
------------------------------------------------------------------------------------------------------------------------
"""


