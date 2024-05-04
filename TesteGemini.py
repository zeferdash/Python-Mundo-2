def calcular_valor_final(preco_normal):
    """
    Calcula o valor final do produto, valor das parcelas e detalhamento do pagamento com base no preço normal e na forma de pagamento escolhida pelo usuário.

    Args:
      preco_normal: O preço normal do produto (float).

    Returns:
      Um dicionário contendo:
        * 'valor_final': O valor final do produto (float).
        * 'valor_parcela': O valor de cada parcela (float).
        * 'detalhes': Uma string com o detalhamento do pagamento.
    """

    print("\nOpções de pagamento:")
    print("1. À vista dinheiro/cheque (10% de desconto)")
    print("2. À vista no cartão (5% de desconto)")
    print("3. Em até 2x no cartão (preço normal)")
    print("4. 3x ou mais no cartão (20% de juros)")

    while True:
        try:
            forma_pagamento = int(input("Digite o número da forma de pagamento escolhida: "))
            if 1 <= forma_pagamento <= 4:
                break
            else:
                print("Forma de pagamento inválida. Por favor, digite um número entre 1 e 4.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    if forma_pagamento == 1:
        desconto = preco_normal * 0.1
        valor_final = preco_normal - desconto
        valor_parcela = valor_final
        detalhes = f"""
    Pagamento à vista dinheiro/cheque:
      Preço normal: R${preco_normal:.2f}
      Desconto: 10%
      Valor final: R${valor_final:.2f}
    """
    elif forma_pagamento == 2:
        desconto = preco_normal * 0.05
        valor_final = preco_normal - desconto
        valor_parcela = valor_final
        detalhes = f"""
    Pagamento à vista no cartão:
      Preço normal: R${preco_normal:.2f}
      Desconto: 5%
      Valor final: R${valor_final:.2f}
    """
    elif forma_pagamento == 3:
        valor_final = preco_normal
        valor_parcela = valor_final / 2
        detalhes = f"""
    Pagamento em até 2x no cartão:
      Preço normal: R${preco_normal:.2f}
      Valor por parcela: R${valor_parcela:.2f}
      Total de parcelas: 2
    """
    elif forma_pagamento == 4:
        while True:
            try:
                numero_parcelas = int(input("Digite o número de parcelas (3x ou mais): "))
                if numero_parcelas >= 3:
                    break
                else:
                    print("Número de parcelas inválido. Digite um número igual ou superior a 3.")
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

        juros_por_parcela = preco_normal * 0.2 / numero_parcelas
        valor_final = preco_normal + (juros_por_parcela * numero_parcelas)
        valor_parcela = valor_final / numero_parcelas
        detalhes = f"""
    Pagamento em {numero_parcelas}x no cartão:
      Preço normal: R${preco_normal:.2f}
      Juros: 20%
      Valor por parcela: R${valor_parcela:.2f}
      Total de parcelas: {numero_parcelas}
    """

    return {
        'valor_final': valor_final,
        'valor_parcela': valor_parcela,
        'detalhes': detalhes
    }

# Exemplo de uso
preco_normal = float(input("Digite o preço normal do produto: "))

resultado = calcular_valor_final(preco_normal)

print(resultado['detalhes'])
print(f"O valor final do produto ficará de R${resultado['valor_final']:.2f}.")
