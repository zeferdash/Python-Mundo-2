#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(0, 50+1, 2): # Primeira alternativa que tive em mente que seria a mais básica de todas porém inclui o número 0.
    print(c, end = " ")

print()

for c in range(1, 50+1): # Segunda alternativa que tive em mente, mais linhas de código porém nao possui o 0.
    if c % 2 == 0:
        print(c, end = " ")

print()

for c in range(2, 50+1, 2): # Terceira alternativa que tive em mente que sinceramente não sei nem pq não pensei nela primeiro
    print(c, end = " ")