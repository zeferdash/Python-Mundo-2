n = int(input("Digite um valor: "))
contador = soma = 0

while n != 999:
    soma += n
    contador += 1
    n = int(input("Digite um valor: "))
print(f"{contador} numeros foram digitados.")
print(f"Soma dos valores: {soma}")