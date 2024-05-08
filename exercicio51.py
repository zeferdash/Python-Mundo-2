# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiroTermo = int(input("Digite o primeiro termo da Progressão Aritmética: "))
razao = int(input("Agora digite a razao da PA: "))
decimo = primeiroTermo + (10 - 1) * razao
for item in range(primeiroTermo, decimo, razao):
    print(item, end=" -> ")
print("Fim")