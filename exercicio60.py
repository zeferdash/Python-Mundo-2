"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

"""
from math import factorial
n = int(input("Digite o número voce deseja saber o fatorial: "))
c = n
fatorial = factorial(n)
print(f"Calculando {n}! = ", end="")
while c > 0:
    print(f"{c}", end="")
    if c > 1:
        print(f" x ", end="")
    else:
        print(" = ", end="")
    c-= 1
print(fatorial)