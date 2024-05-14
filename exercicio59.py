n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
opcao = 0
while opcao != 5:
    opcao = int(input("Qual opcao voce deseja? "))
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma dos valores é {soma}")
        print("-=" * 30)
    elif opcao == 2:
        razao = n1 * n2
        print(f"A multiplicacao dos valores deu {razao}")
        print("-=" * 30)
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior valor é o {n1}")
            print("-=" * 30)
        else:
            print(f"O maior valor é o {n2}")
            print("-=" * 30)
    elif opcao == 4:
        print("Digite abaixo os novos valores desejados")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print("-=" * 30)
    elif opcao == 5:
        print("O programa será encerrado.")
    else:
        print("Opcao invalida.")