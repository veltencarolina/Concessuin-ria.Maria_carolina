#======================= ESTOQUES =========================#
# trabaio
Aluguel_carros = [
    ("onix", "chevrolet", 76318.00),
    ("corolla", "toyota", 10701.5),
    ("hb20", "hyundai", 53446.00),
    ("cronos", "fiat", 59131.00),
    ("jetta", "volkswagen", 21094.7)
]

Comprar_carro = [
    ("onix", "chevrolet", 76318),
    ("corolla", "toyota", 10015),
    ("hb20", "hyundai", 53446),
    ("cronos", "fiat", 59131),
    ("jetta", "volkswagen", 210947)
]

#======================= CADASTRO =========================#

cliente = {
    "nome": input("Insira o seu nome: ").strip(),
    "telefone": input("Insira o seu número de telefone: ").strip(),
    "saldoinicial": float(input("Informe o seu saldo: ").strip().replace(",", "."))
}

#======================= VENDA DE CARRO ===================#

def venda_carro():
    Modelo = input("Modelo de carro: ").strip().lower()
    Marca = input("Marca do carro: ").strip().lower()

    Carros = [
        ("onix", "chevrolet", 76318),
        ("corolla", "toyota", 107015),
        ("hb20", "hyundai", 53446),
        ("cronos", "fiat", 59131),
        ("jetta", "volkswagen", 210947)
    ]

    Valor_carro = 0.0
    encontrado = False

    for Carro in Carros:
        if Modelo == Carro[0] and Marca == Carro[1]:
            Valor_carro = Carro[2] * 0.88   # empresa paga 88%
            encontrado = True
            break

    if not encontrado:
        print("Modelo/Marca não encontrado. Operação cancelada.")
        return

    RespostaCliente = input(
        f"Valor da venda: R$ {Valor_carro:.2f}. Continuar negociação? (1 - sim / 2 - não): "
    ).strip()

    if RespostaCliente == '1':
        cliente["saldoinicial"] = cliente["saldoinicial"] + Valor_carro
        print("Venda realizada. Dados do cliente:")
        print(cliente)

        Comprar_carro.append((Modelo, Marca, Valor_carro / 0.88))
    else:
        print("Operação cancelada...")


#======================= ALUGUEL ===========================#

def aluguel_carro():
    Modelo_aluguel = input("Insira um modelo desejado: ").strip().lower()
    Marca_aluguel = input("Insira a marca: ").strip().lower()

    encontrado = False

    for Veiculo in Aluguel_carros:
        if Modelo_aluguel == Veiculo[0] and Marca_aluguel == Veiculo[1]:
            encontrado = True

            while True:
                NumerosDias = input("Quantidade de dias: ").strip()
                try:
                    NumerosDias = int(NumerosDias)
                    if NumerosDias > 0:
                        break
                except:
                    print("Número inválido!")

            Locacao_final = NumerosDias * 77
            break

    if not encontrado:
        print("Modelo não disponível.")
        return

    RespostaAluguel = input(
        f"Valor final: R$ {Locacao_final:.2f}. Continuar? (1 - sim / 2 - não): "
    ).strip()

    if RespostaAluguel == '1':

        if cliente["saldoinicial"] >= Locacao_final:
            cliente["saldoinicial"] -= Locacao_final
            print("Transação aceita!")
            print(f"Saldo restante: R$ {cliente['saldoinicial']:.2f}")

            # remover carro alugado
            for i, v in enumerate(Aluguel_carros):
                if v[0] == Modelo_aluguel and v[1] == Marca_aluguel:
                    Aluguel_carros.pop(i)
                    break
        else:
            print("Saldo insuficiente!")
    else:
        print("Operação cancelada...")


#======================= COMPRA DE CARRO ===================#

def compra_carro():
    Modelo_comprar = input("Modelo desejado: ").strip().lower()
    Marca_comprar = input("Marca desejada: ").strip().lower()

    Comprar_carro_local = [
        ("onix", "chevrolet", 76318),
        ("corolla", "toyota", 107015),
        ("hb20", "hyundai", 53446),
        ("cronos", "fiat", 59131),
        ("jetta", "volkswagen", 210947)
    ]

    Valor_comprar = None
    encontrado = False

    for Carro in Comprar_carro_local:
        if Modelo_comprar == Carro[0] and Marca_comprar == Carro[1]:
            Valor_comprar = Carro[2] * 1.25  # +25%
            encontrado = True
            break

    if not encontrado:
        print("Modelo não disponível.")
        return

    Retornocliente = input(
        f"Valor final: R$ {Valor_comprar:.2f}. Continuar? (1 - sim / 2 - não): "
    ).strip()

    if Retornocliente == '1':

        if cliente["saldoinicial"] >= Valor_comprar:
            cliente["saldoinicial"] -= Valor_comprar
            print("Compra realizada!")
            print(f"Saldo restante: R$ {cliente['saldoinicial']:.2f}")

            for i, c in enumerate(Comprar_carro):
                if c[0] == Modelo_comprar and c[1] == Marca_comprar:
                    Comprar_carro.pop(i)
                    break
        else:
            print("Saldo insuficiente!")
    else:
        print("Operação cancelada...")


#======================= MENU ==============================#

def menu():
    while True:
        print("\n=========== BEM VINDO ===========")
        print("1 - Venda carro")
        print("2 - Aluguel carro")
        print("3 - Compra carro")
        print("4 - Ver saldo e sair")

        opcao = input("Escolha: ").strip()

        match opcao:
            case "1":
                venda_carro()
            case "2":
                aluguel_carro()
            case "3":
                compra_carro()
            case "4":
                print(f"\nSaldo atual: R$ {cliente['saldoinicial']:.2f}")
                break
            case _:
                print("Opção inválida.")


#======================= EXECUTAR ===========================#

if __name__ == "__main__":
    menu()
