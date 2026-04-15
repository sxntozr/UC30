def soma_segura(a, b):
    try:
        return a + b
    except TypeError:
        print("Entrada Inválida")
        return 0

soma_segura(10, 12)
soma_segura("a", 2)

def divisao(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Não divida por zero!"
    
divisao()