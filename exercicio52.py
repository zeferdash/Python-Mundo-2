# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input("Digite um número: "))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print("\033[34m", end="") # Pinta os números em que "n" é divisivel.
        total += 1
    else:
        print("\033[m", end="")
    print(f"{c}", end=" ")

print(f"\n\033[mO número {n} foi divisivel {total} vez(es)", end="")

if total == 2:
    print(" e por isso ele é primo")
else:
    print(" e por isso ele não é primo")
