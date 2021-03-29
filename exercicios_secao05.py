"""
Exercícios Seção 05

1 - Faça um programa que receba dois números e mostre qual deles é o maior.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O número maior é {num1}')
else:
    print(f'O número maior é o {num2}')
-----------------------------------------------------------------------------------------------------
2 - Leia um numero, se esse numero for positivo, calcule a raiz quadrada do numero, se o numero for
negativo, mostre a mensagem dizendo que o numero é invalido.

numero = int(input('Digite um número: '))
if numero > 0 :
    raiz = numero ** 2
    print(f'Número positivo! Sua raiz quadrada é {raiz}')
else:
    print('O número digitado é inválido(negativo), digite um numero positivo!')
--------------------------------------------------------------------------------------------------------
5 - Receba um numero inteiro e verifique se este numero é par ou impar.

numero = int(input('Digite um número: '))

if numero % 2:
    print(f'O número {numero} é impar.')
else:
    print(f'O número {numero} é par.')
--------------------------------------------------------------------------------------------------------
8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e exiba na tela
a média destas notas. Uma nota valida deve ser um valor entre 0.0 e 10.0, onde caso a nota nao possua um
valor valido, este fato deve ser informado ao usuario e o programa termina.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if  nota1 >= 0 and nota1 <= 10:
    if nota2 >= 0 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f'A média das notas é: {media}')
    else:
         print('Informe duas notas válidas.')
else:
    print('Informe duas notas válidas.')
---------------------------------------------------------------------------------------------------------
9 - Leia o salario de um trabalhador e o valor da prestação de um emprestimo. Se a
prestação for maior que 20% do salario imprima: Emprestimo nao concedido, caso contrario imprima: Emprestimo
concedido.

salario = float(input('Digite seu salário: '))
prestacao = float(input('Digite o valor da prestação: '))
# calculando 20% do salario
porcent = (20 * salario) / 100
if prestacao > porcent:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')
------------------------------------------------------------------------------------------------------------
18 - Faça um programa que mostre ao usuário um menu com 4 opções de operações matematicas. O usuario
escolhe uma das opções e o seu programa entao pede dois valores numericos e realiza a operação, mostrando
o resultado e saindo.

print('Calculadora - Escolha uma operação \n'
      '1 - Adição \n'
      '2 - Subtração \n'
      '3 - Multiplicação \n'
      '4 - Divisão')

operacao = int(input('Opção escolhida: '))
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if operacao == 1:
    resultado = valor1 + valor2
    print(f'A soma dos valores é: {resultado}')
elif operacao == 2:
    resultado = valor1 - valor2
    print(f'A subtração dos valores é: {resultado}')
elif operacao == 3:
    resultado = valor1 * valor2
    print(f'A multiplicação dos valores é: {resultado}')
elif operacao == 4:
    resultado = valor1 / valor2
    print(f'A divisão dos valores é: {resultado}')
-----------------------------------------------------------------------------------------------------------
22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições são: Ter pelo menos 65 anos, ou ter trabalhado pelo menos 30 anos ou ter pelo menos
60 anos e trabalhado pelo menos 25 anos.

idade = int(input('Digite sua idade: '))
temp_serv = int(input('Digite o tempo de serviço em anos: '))

if idade >= 65 or temp_serv >= 30:
    print('Aposentadoria permitida.')

elif idade >= 60 and temp_serv >= 25:
    print('Aposentadoria permitida.')
else:
    print('Aposentadoria negada.')
--------------------------------------------------------------------------------------------------------------
29 - Faça uma prova de matematica para crianças que estao aprendendo a somar numeros inteiros menores do que
100. Escolha numeros aleatorios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde
a e b são os numeros aleatorios. Peça a resposta.

from random import randint

print('Qual o resultado da soma dos valores abaixo?')
valor1 = (randint(1, 100))
print(valor1)
valor2 = (randint(1, 100))
print(valor2)
resp1 = valor1 + valor2
resposta1 = int(input('Resposta: '))
if resposta1 == resp1:
    print(f'{resp1}. Parabéns, você acertou!')
    acerto1 = 1
else:
    print(f'{resp1}. Poxa, não foi dessa vez...')
    erro1 = 1
print('---------------------------------------------')
print('Qual o resultado da soma dos valores abaixo?')
valor3 = (randint(1, 100))
print(valor3)
valor4 = (randint(1, 100))
print(valor4)
resp2 = valor3 + valor4
resposta2 = int(input('Resposta: '))
if resposta2 == resp2:
    print(f'{resp2}. Parabéns, você acertou!')
    acerto2 = 1
else:
    print(f'{resp2}. Poxa, não foi dessa vez...')
    erro2 = 1
print('---------------------------------------------')
print('Qual o resultado da soma dos valores abaixo?')
valor5 = (randint(1, 100))
print(valor5)
valor6 = (randint(1, 100))
print(valor6)
resp3 = valor5 + valor6
resposta3 = int(input('Resposta: '))
if resposta3 == resp3:
    print(f'{resp3}. Parabéns, você acertou!')
    acerto3 = 1
else:
    print(f'{resp3}. Poxa, não foi dessa vez...')
    erro3 = 1
print('---------------------------------------------')
-----------------------------------------------------------------------------------------------------
26 - Leia a distancia em Km e a quantidade de litros de gasolina consumidos por um carro em um
percurso, calcule o consumo km/l e escreva uma mensagem de acordo com a tabela.

distancia = int(input('Digite a distância em km/h: '))
litros = int(input('Digite a quantidade de litros consumidos: '))

consumo = distancia / litros

if consumo < 8:
    print('Venda o carro!')
elif consumo >= 8 <= 12:
    print('Econômico!')
elif consumo > 14:
    print('Super econômico!')
------------------------------------------------------------------------------------------------------
"""















