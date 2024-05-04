from datetime import date
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print("Categoria: MIRIM")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JÚNIOR")
elif idade <= 25:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")