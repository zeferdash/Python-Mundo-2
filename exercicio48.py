# Exercício Python 48: Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
valores_multiplos_de_3 = []
for n in range(1, 501, 2):
    if n % 3 == 0:
        contador += 1
        soma += n
        valores_multiplos_de_3.append(n)
print(f"A soma de todos os {contador} valores multiplos de 3 solicitados é {soma}")
print(f"E os 83 valores são: {valores_multiplos_de_3}")
