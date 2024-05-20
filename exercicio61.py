# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiroTermo = int(input("Digite o primeiro termo da Progressão Aritmética: "))
razao = int(input("Agora digite a razao da PA: "))
termo = primeiroTermo
cont = 1
total = 0
maisTermos = 10
while maisTermos != 0:
    total+= maisTermos
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        cont += 1
    print("Pausa")
    maisTermos = int(input("Deseja ver mais quantos termos? "))
print("Fim")
