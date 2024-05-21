"""Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8"""
n = int(input("Quantos termos voce deseja ver? "))
t1 = 0
t2 = 1
contador = 3
print(f"{t1} -> {t2} -> ", end="")
while contador <= n:
    t3 = t1 + t2
    print(f"{t3} -> ", end="")
    contador += 1
    t1 = t2
    t2 = t3
print("Fim")