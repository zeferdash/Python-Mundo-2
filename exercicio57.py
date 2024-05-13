# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input("Por favor, informe seu sexo: [M/F]: ").upper().strip()[0]
while sexo not in "MmFf":
    sexo = input("Dados inválidos, favor escolher M ou F: ").upper().strip()[0]
print(f"Sexo {sexo} registrado com sucesso!")