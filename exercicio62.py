# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input("Digite o primeiro termo da Progressão Aritmética: "))
razao = int(input("Agora digite a razao da PA: "))
termo = primeiroTermo
cont = 1
maisTermos = 1
while maisTermos != 0:
    while cont <= 10:
        print(f"{termo} -> ", end="")
termo += razao
cont += 1
print("Pausa")
