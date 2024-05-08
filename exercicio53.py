"""Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

# Forma 1, sem conter o FOR
frase = input("Digite uma frase qualquer: ").upper().replace(" ","")
if frase == frase[::-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")


# Forma 2, contendo o FOR
frase2 = input("Digite uma frase qualquer novamente: ").upper().strip()
palavras = frase2.split() # Transformando a frase2 em strings separadas palavra por palavra
palavrasUnificadas = "".join(palavras) # Unificando a variavel palavras com "" (campo em branco e sem espaco) para que fique uma unica string unificada
inverso = ""
for letra in range(len(palavrasUnificadas) - 1, -1, -1 ):
    inverso += palavrasUnificadas[letra]
print(f"O inverso de {palavrasUnificadas} é {inverso}")
if inverso == palavrasUnificadas:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")
