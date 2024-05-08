""" Após terminar meu código perguntei pra IA como ela faria pra ter uma nocao do que fizemos diferente e se aprendia algo novo com ela.
No fim o código IF da IA é bem mais simples que o meu e funciona de forma parecida, só faltando algumas implementacoes pra caso a pessoa digite algo diferente de M/F, coisa que eu
inclui no meu código.
"""
soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
mulheres_menos_20 = 0

for i in range(4):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    sexo = input(f"Digite o sexo da {i+1}ª pessoa (M/F): ").upper()

    soma_idades += idade

    if sexo == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    elif sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idades / 4

print(f"\nA média de idade do grupo é de {media_idade} anos.")
print(f"O homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos.")
print(f"Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos.")