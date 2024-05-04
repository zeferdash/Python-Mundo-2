import datetime
anoNascimento = int(input("Digite seu ano de nascimento: "))
idadeAlistamento = 18;
idade =  datetime.datetime.now().year - anoNascimento
print(f"Quem nasceu em {anoNascimento} tem {idade} anos atualmente.")
if idade < idadeAlistamento:
    print(f"Voce ainda nao tem idade suficiente para estar efetuando o alistamento obrigatório, lhe faltam {idadeAlistamento - idade} anos.")
elif idade == idadeAlistamento:
    print("Voce está na idade exata para o efetuamento do alistamento obrigatório.")
else:
    print("Provavelmente voce ja efetuou o alistamento obrigatório.")