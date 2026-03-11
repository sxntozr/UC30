notas = {}

notas["nome"] = input("Qual seu nome: ")
notas["nota1"] = int(input("Nota 1º Prova: "))
notas["nota2"] = int(input("Nota 2º Prova: "))

media = (notas["nota1"] + notas["nota2"]) / 2

notas["media"] = media

if notas["media"] >= 7:
     print(f"Você foi aprovado. Sua média foi de {media}")
elif notas["media"] >= 5:
     print("Você está de recuperação!")
else:
    print("Você foi reprovado!")