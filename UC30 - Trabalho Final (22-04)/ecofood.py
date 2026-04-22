alimentos = []


def cadastrar():
   nome = input("\nDigite seu nome: ")
   email = input("Digite seu email: ")
   senha = input("Digite uma senha: ")
   print("Cadastro realizado!")


def entrar():
   email = input("\nDigite seu email: ")
   senha = input("Digite sua senha: ")
   print("Login realizado!")


def menu_alimentos():
   while True:
       print(
           "\n=== MENU ECOFOOD ==="
           "\n[1] - Cadastrar alimento"
           "\n[2] - Ver alimentos"
           "\n[0] - Sair"
       )


       opcao = input("\nEscolha: ")


       if opcao == "1":
           print("=== Cadastrar Alimento ===")
           nome = input("Nome do alimento: ")
           validade = input("Validade: ")
           local = input("Local de retirada: ")


           alimentos.append({
               "nome": nome,
               "validade": validade,
               "local": local
           })


           print("\nAlimento cadastrado!")


       elif opcao == "2":
           if not alimentos:
               print("\nNenhum alimento cadastrado.")
           else:
                   print(f" {nome} | {validade} | {local}")


       elif opcao == "0":
           print("Saindo do menu alimentos...")
           break


       else:
           print("Opção inválida!")




print("=== EcoFood ===")


while True:
   print(
       "\n[1] - Cadastrar"
       "\n[2] - Entrar"
       "\n[0] - Sair"
   )


   opcao = input("\nSelecione uma opção: ")


   if opcao == "1":
       cadastrar()
       menu_alimentos()


   elif opcao == "2":
       entrar()
       menu_alimentos()


   elif opcao == "0":
       print("Saindo...")
       break


   else:
       print("Opção inválida!")