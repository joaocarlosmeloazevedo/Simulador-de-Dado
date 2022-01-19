# 1 - Simulador de dado que permite gerar um valor aleatório entre 1 e 6
# 2 - Permitir que o Usuário rode o script quantas vezes quiser.

from random import randint
from ssl import RAND_pseudo_bytes
import time

escolha_sim = ["SIM", "S"]
escolha_nao = ["NAO", "N"]
def menu():
    print("Bem vindo ao programa de simulador de dados!\nRode o número que você quiser!\nOu jogue contra seus amigos!")

    escolha_usuario = input("Deseja utilizar o nosso programa?\n ***DIGITE \"SIM\" ou \"NAO\"***\n").upper()
    if escolha_usuario in escolha_sim:
        submenu()
    else:
        exit()

def submenu():
    jogar_novamente = "SIM"

    while jogar_novamente in escolha_sim or jogar_novamente == "V":
        user_choice = int(input(("Escolha o seu modo jogo:\n1 - RODE UM DADO!\n2 - Modo VS.")))
        if user_choice == 1:
            while jogar_novamente in escolha_sim or jogar_novamente != "V":
                print("\nATENÇÃO!\n")
                i = 3

                while i > 0:
                    print("O resultado do seu dado será mostrado em... ", i)
                    time.sleep(1)
                    i -= 1
                time.sleep(2)
                dado = randint(1, 6)
                print("Seu resultado é: ", dado)

                
        
        if user_choice == 2:

            dado_1 = 0
            dado_2 = 0
            points_1 = 0
            points_2 = 0

            
            nomes_iguais = False
            player_1 = str
            player_2 = str

            while nomes_iguais == False:
                print("JOGADOR 1, digite seu nome: ")
                player_1 = input("").upper()

                print("JOGADOR 2, digite seu nome: ")
                player_2 = input("").upper()

                if player_1 == player_2:
                    print("Escolham nomes diferentes.")
                    
                else:
                    nomes_iguais = True

            while jogar_novamente in escolha_sim or jogar_novamente != "V":
                print("OS DADOS SERÃO GERADOS AUTOMATICAMENTE!!!\n")
                time.sleep(1)
                print("AI ESTÃO OS RESULTADOS!")
                time.sleep(2)

                dado_1 = randint(1, 6)
                dado_2 = randint(1, 6)
                print("Dado do(a)", player_1, "deu ", dado_1, "!!")
                time.sleep(3)
                print("Dado do(a)", player_2, "deu ", dado_2, "!!")
                
                if dado_1 == dado_2:
                    time.sleep(3)
                    print("EMPATE!")
                    
                
                elif dado_1 > dado_2:
                    time.sleep(3)
                    print("O vencedor foi ", player_1)
                    points_1 += 1 
                else:
                    time.sleep(3)
                    print("O vencedor foi", player_2)
                    points_2 += 1 
                
                print("PLACAR:\n",player_1, " ", points_1, "\n ", player_2, " ", points_2)
                jogar_novamente = input("Deseja jogar novamente?\n***DIGITE \"SIM\" ou \"NAO\"***\nDeseja voltar ao menu?\n***DIGITE \"V\"***\n""").upper()




menu()

