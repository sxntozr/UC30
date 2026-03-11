compra = input("Digite o valor da compra: ")

if compra < 100:
    print("Compra sem desconto!")
elif compra >= 100:
    desconto1 = compra * 0.05
    print("")