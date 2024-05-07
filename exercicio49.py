# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input("Gostaria de saber a tabuada de qual número? "))
print(f"Segue abaixo a tabuada do número {n}:")
for item in range(1, 11):
    print(f"{n}x{item} = {item * n}")