# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
dataAtual = datetime.datetime.now()
maioridade = 0
menoridade = 0
for c in range(1, 8):
    anoNascimento = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
    if dataAtual.year - anoNascimento >= 21:
        maioridade+= 1
    else:
        menoridade+= 1
print(f"Ao todo temos {maioridade} pessoas maiores de idade e {menoridade} que ainda são menores de idade.")
