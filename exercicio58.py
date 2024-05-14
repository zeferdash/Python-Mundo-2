from random import randint
from time import sleep

print("Vou pensar em um número aleatório de 0 a 10...")
sleep(3)
aleatorio = randint(0, 10)
chute = int(input("Pronto! Em qual número voce acha que pensei? "))
palpite = 1
while chute != aleatorio:
    if chute > aleatorio or chute < aleatorio:
        print("Nada disso, eu pensei em um número de 0 a 10 e nao nesse valor que voce colocou.")
    chute = int(input("Infelizmente voce errou =/, tente novamente: "))
    palpite += 1
print(f"Finalmente depois de {palpite} palpites voce acertouuu, eu tinha pensado no número {aleatorio}")
