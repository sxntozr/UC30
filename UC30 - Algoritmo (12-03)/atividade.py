def calcular(valor1, valor2):
    soma = valor1 + valor2
    produto = valor1 * valor2

    return soma, produto

resultadoSoma, resultadoProduto = calcular(5, 5)
print(f"Resultado da soma: {resultadoSoma}, {resultadoProduto}")
