from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint (0,2)
print('''Suas opcoes: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input("E ai, qual vai ser sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
print("-=" * 20)
print(f"Computador jogou: {itens[computador]}")
print(f"Voce jogou: {itens[jogador]}")
print("-=" * 20)
if computador == 0:
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Jogador Venceu")
    elif jogador == 2:
        print("jogador Perdeu")
    else:
        print("Jogada inválida")
elif computador == 1:
    if jogador == 0:
        print("Jogador Perdeu")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Jogador Venceu")
    else:
        print("Jogada inválida")
elif computador == 2:
    if jogador == 0:
        print("Jogador Venceu")
    elif jogador == 1:
        print("Jogador Perdeu")
    elif jogador == 2:
        print("Empate")
    else:
        print("Jogada inválida")