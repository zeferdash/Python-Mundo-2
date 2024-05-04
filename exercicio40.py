n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2)/ 2
if media < 5.0:
    print("Voce foi reprovado!")
elif media >= 5.0 and media <= 6.9:
    print("Voce esta em recuperacao!")
else:
    print("Voce foi aprovado!")