nome = input("Digite o nome completo do aluno: ")
matricula = input("Digite o número da matricula: ")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota:: "))

nota = (nota1 + nota2) / 2

print(nome)
print(matricula)
print(f"A média foi de {nota}")