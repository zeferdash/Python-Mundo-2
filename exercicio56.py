# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
maisVelho = 0
menosDe20 = 0
somaIdades = 0
homemMaisVelho = ""

for pessoa in range(4):
    nome = input(f"Digite o nome da {pessoa+1}ª pessoa: ").strip()
    idade = int(input(f"Digite a idade da {pessoa+1}ª pessoa: "))
    genero = input(f"Digite o sexo da {pessoa+1}ª pessoa com H para Homem e M para Mulher: ").strip().upper()
    somaIdades += idade
    print()

    if pessoa == 1 and genero[0] == "H":
        maisVelho = idade
        homemMaisVelho = nome

    if genero[0] == "H" and idade > maisVelho:
        maisVelho = idade
        homemMaisVelho = nome

    if genero[0] == "M" and idade < 20:
        menosDe20 += 1

mediaIdade = somaIdades / 4
print(f"A média de idade do grupo é {mediaIdade} anos, o nome do homem mais velho é {homemMaisVelho}, {maisVelho} anos e {menosDe20} mulheres tem menos que 20 anos.")
