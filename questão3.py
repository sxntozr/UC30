valores = []

while True:
    valor = float(input("Digite o valor do produto: "))
    valores.append(valor)

    total = sum(valores)

    if valor == 0:
        break 

print(f"Total da compra: R$ {total:.2f}")
