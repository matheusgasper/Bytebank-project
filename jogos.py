import forca
import adivinhacao
import Jogo_penaltis

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação (3) Penaltis")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()
elif (jogo == 3):
    print("Jogando Penaltis")
    Jogo_penaltis.jogar()
