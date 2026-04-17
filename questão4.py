peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

def academia_dados(peso, altura):
    try:
        imc = peso / (altura * altura)

        if imc < 18.5:
            print(f"Seu IMC é: {imc} e você é Magro.")
        elif imc <= 24.9:
            print(f"Seu IMC é: {imc} e você é Normal.")
        else:
            print(f"Seu IMC é: {imc} e você está Acima do peso.")

    except ZeroDivisionError:
        print("Entrada inválida! Digite apenas números acima de 0.")

academia_dados(peso, altura)