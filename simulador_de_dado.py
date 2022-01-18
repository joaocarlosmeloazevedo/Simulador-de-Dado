# 1 - Simulador de dado que permite gerar um valor aleatório entre 1 e 6
# 2 - Permitir que o Usuário rode o script quantas vezes quiser.

from random import randint
import time

escolha_sim = ["SIM", "S"]
escolha_nao = ["NAO", "N"]
def menu():
    print("Bem vindo ao programa de simulador de dados!\nRode o número que você quiser!")

    escolha_usuario = input("Deseja utilizar o nosso programa?\n ***DIGITE \"SIM\" ou \"NAO\"***\n").upper()
    if escolha_usuario in escolha_sim:
        submenu()
    else:
        exit()

def submenu():
    jogar_novamente = "SIM"
    while jogar_novamente in escolha_sim:
        print("ATENÇÃO!")
        i = 3
        while i > 0:
            print("O resultado do seu dado será mostrado em... ", i)
            time.sleep(1)
            i -= 1
        time.sleep(2)
        dado = randint(1, 6)
        print("Seu resultado é: ", dado)

        jogar_novamente = input("Deseja jogar novamente?\n***DIGITE \"SIM\" ou \"NAO\"***\n").upper()

menu()

