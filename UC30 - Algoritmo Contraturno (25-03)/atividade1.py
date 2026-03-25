def calculadora():
    print("Resuma Estatístico")

    num1 = float(input("Digite a primeira nota: "))
    num2 = float(input("Digite a segundo nota: "))
    num3 = float(input("Digite a terceira nota: "))

    soma = num1 + num2 + num3
    media = soma / 3
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)

    print(f"Soma: {soma}")
    print(f"Média: {media}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")

calculadora()