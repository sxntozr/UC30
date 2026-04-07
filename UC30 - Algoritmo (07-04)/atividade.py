import random

numero = random.randint(1, 100)
tentativas = 0

while True:
    numero1 = int(input("Tente adivinhar o número: "))
    tentativas += 1

    if numero1 < numero:
        print("Maior")
    elif numero1 > numero:
        print("Menor")
    else:
        print(f"Acertou! Você precisou de {tentativas} tentativas")
        break