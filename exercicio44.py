# Solicita ao usuário que insira o preço do produto
preco = float(input("Digite o preço das compras: "))

# Solicita ao usuário que escolha a condição de pagamento
print("Escolha a condição de pagamento:")
print("1 - À vista dinheiro/cheque (10% de desconto)")
print("2 - À vista no cartão (5% de desconto)")
print("3 - Em até 2x no cartão (preço normal)")
print("4 - 3x ou mais no cartão (20% de juros)")
opcao = int(input("Digite o número da opção desejada: "))

# Calcula o valor a ser pago com base na condição de pagamento escolhida
if opcao == 1:
    total = preco - (preco * 10/100)  # 10% de desconto
elif opcao == 2:
    total = preco - (preco * 5/100)  # 5% de desconto
elif opcao == 3:
    total = preco  # Preço normal
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totpar = int(input("Quantas parcelas? "))
    parcela = total / totpar
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(totpar, parcela))
else:
    print("Opção inválida.")
    exit()

# Imprime o valor a ser pago
print("Valor a ser pago: R${:.2f}" .format(total))
