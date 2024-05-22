"""Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

resposta = "S"
soma = quantidade = media = maior = menor = 0
while resposta in "S":
    n = int(input("Digite um valor: "))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
media = soma / quantidade
print(f"Voce digitou {quantidade} números e a média deles foi {media}")
print(f"O maior numero foi {maior} e o menor numero foi {menor}")

