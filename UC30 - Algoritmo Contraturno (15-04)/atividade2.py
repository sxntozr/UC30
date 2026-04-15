def total_compra():
    try:
        preço1 = float(input("Digite o preço do primeiro produto: "))
        preço2 = float(input("Digite o preço do segundo produto: "))

        total = preço1 + preço2

        print(f"Total da compra: R$ {total:.2f}")

    except ValueError:
        print("Erro: os preços devem ser números!")

total_compra()