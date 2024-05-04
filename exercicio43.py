print("Bem vindo ao calculador de IMC - Indice de Massa Corporal, preencha os dados a seguir:")
print("-" * 100)
peso = float(input("Digite seu peso: "))
altura = float(input("E qual seria sua altura?: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do peso {:.2f}".format(imc))
elif imc <= 25:
    print("Peso ideal {:.2f}".format(imc))
elif imc <= 30:
    print("Sobrepeso {:.2f}".format(imc))
elif imc <= 40:
    print("Obesidade {:.2f}".format(imc))
else:
    print("Obesidade Morbida {:.2f}".format(imc))