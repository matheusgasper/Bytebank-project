import random

print("**************************************")
print("--- Bem vindo ao jogo dos penaltis ---")
print("**************************************")

canto_goleiro = ["esquerdo","direito"]
defesa = random.choice(canto_goleiro)
total_de_tentativas = 5
gols = 0

for rodada in range(1,total_de_tentativas + 1):
    print("Chute {} de {}".format(rodada, total_de_tentativas))
    print("     \\(☻)                                                                       ")
    print("       ||\\                                       ┏━━━━━━━━━━━━━━━━━━━━━┓-------")
    print("       ||                                        ┃           ☻        ┃ |_|_|_|\"")
    print("    \_/  \                                       ┃         //||\\       ┃ |_|_|_|_\"")
    print("       ⬤  \                                      ┃         ╭/ \╮       ┃ |_|_|_|_|\"")
    chute = input("Qual canto ('esquerdo ou direito')? ")


    if (chute == defesa):
        print("DEFENDEEEEU!!! ✖✖✖")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃    ✋⬤   ✋           ┃")
        print("┃    \\(☻)||           ┃")
        print("┃     ╰╰ \\╯╯           ┃")
        print("┃         \╲            ┃")
        print("┃          ╲_╲_         ┃")

    else:
        if(chute == "esquerdo"):
           print("GOOOOOOLL!!!")
           print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
           print("┃                ✋     ✋    ┃")
           print("┃                ||(☹)//     ┃")
           print("┃  ⬤             ╰╰// ╯╯     ┃")
           print("┃                 //         ┃")
           print("┃              _/_/          ┃")
           gols += 1
           print("Gols: {}".format(gols))

      #  elif(chute == "direito"):
        else:
            print("GOOOOOOLL!!!")
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃   ✋     ✋                ┃")
            print("┃    \\(☹)||                ┃")
            print("┃     ╰╰ \\╯╯           ⬤   ┃")
            print("┃         \╲                ┃")
            print("┃          ╲_╲_             ┃")
            gols += 1
            print("Gols: {}".format(gols))

print("Fim do jogo")








