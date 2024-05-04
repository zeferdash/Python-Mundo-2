nome = str(input("Digite seu nome: "))
if nome == "Rafael":
    print("Oloco, que nome bonito da penga")
elif nome == "Samuel" or nome == "Gabriel": # Quando temos if e elif chamamos de estrutura condicional aninhada
    print("É... seu nome não é tão bonito assim =/")
elif nome in "Fatima Samara Camila":
    print("Teu nome é bonito também =D")
print(f"Tenha um bom dia, {nome}")