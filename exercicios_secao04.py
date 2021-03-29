"""
Exercícios Seção 04

1 - Faça um programa que leia um número inteiro e o imprima.
numero = int(input('Digite um número: '))
print(numero)
---------------------------------------------------------------------------------------------------
3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

result = num1 + num2 + num3
print(f' A soma dos três números digitados é {result}')
-------------------------------------------------------------------------------------------------------
6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
(Fórmula de conversão é: F = C* * (9.0/5.0) + 32.0.
tempC = float(input('Digite a temperatura em graus Celsius: '))
conv = tempC * (9.0 / 5.0) + 32.0
print(f'A temperatura em graus Celsius digitada foi convertida em {conv} graus Fahrenheit')
--------------------------------------------------------------------------------------------------------------
10 - Leia uma velocidade em km/h e apresente-a convertida em m/s. A fórmula é: M = K/3.6, sendo K a velocidade
em km/h e M em m/s.
k = float(input('Digite uma velocidade em km/h: '))
m = k / 3.6
print(f'A velocidade em km/h digitada foi convertida em {m} m/s.')
--------------------------------------------------------------------------------------------------------
28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três
valores lidos.
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

quadrado_valor1 = valor1 ** 2
quadrado_valor2 = valor2 ** 2
quadrado_valor3 = valor3 ** 2

soma_quadrados = quadrado_valor1 + quadrado_valor2 + quadrado_valor3
print(f'A soma dos quadrados dos três valores digitados é {soma_quadrados}')
--------------------------------------------------------------------------------------------------------
31 - Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print(f'O antecessor do número digitado é {antecessor}; e o sucessor é {sucessor}')
-------------------------------------------------------------------------------------------------------
32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
numero = int(input('Digite um número: '))
dobro = numero * 2  
triplo = numero * 3 
suce_triplo = triplo + 1 
ant_dobro = dobro - 1 
result = suce_triplo + ant_dobro 
print(f'A soma do sucessor de seu triplo com o antecessor de seu dobro é {result}')
---------------------------------------------------------------------------------------------------------
46 - Faça um programa que leia um número inteiro positivo de tres digitos.
Gere outro numero formado pelos digitos invertidos do numero lido. Ex: 123 -> 321.
numeroLido = input(' Digite um número de três digitos: ')
print(f'O número invertido gerado é: {numeroLido[2], numeroLido[1], numeroLido[0]}')
----------------------------------------------------------------------------------------------------------
47 = Leia um numero de 4 digitos e imprima 1 digito por linha.
numero = input('Digite um número de 4 digitos: ')
print(numero[0])
print(numero[1])
print(numero[2])
print(numero[3])
"""











