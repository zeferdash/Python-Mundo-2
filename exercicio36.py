print("\033[032mBem vindo ao aprovador de empréstimos bancários, preencha os dados a seguir:")
valorCasa = float(input("Digite o valor da casa que deseja comprar: "))
salario = float(input("Agora nos diga qual o seu salário atual: "))
anos = int(input("Em quantos anos voce deseja efetuar o pagamento da casa?: "))
parcelas = valorCasa / (anos * 12)
parcelaMaxima = salario * 0.30
if parcelas > parcelaMaxima:
    print(f"Seu empréstimo foi negado pois o valor das parcelas ultrapassa o valor de 30% do seu salário (R${parcelaMaxima:.2f}) e o valor mínimo necessário das parcelas seria de R${parcelas:.2f}!")
else:
    print(f"Seu empréstimo foi aprovado e o valor das parcelas será de R${parcelas:.2f}")