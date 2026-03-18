def classificar_numero(numero): 

    if numero > 0:
        print("Ele é um número positivo.")
    elif numero < 0:
        print("Ele é um número negativo.")
    else:
        print("Seu número é zero.")

print(classificar_numero(10))