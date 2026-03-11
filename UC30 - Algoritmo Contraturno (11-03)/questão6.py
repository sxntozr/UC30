idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Você é Infantil")
elif idade >= 12:
    print("Você é Juvenil.")
elif idade >= 18:
    print("Você é adulto.")
else:
    print("Você é senior.")