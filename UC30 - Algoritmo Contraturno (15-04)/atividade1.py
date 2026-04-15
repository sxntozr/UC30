def media_notas():

    lista_notas = []

    try:
        for i in range(3):

            nota = float(input(f"Nota {i+1}: "))
            lista_notas.append(nota)

        media = sum(lista_notas) / len(lista_notas)
        print(f"Média: {media:.2f}")

    except ValueError:
        print("Notas devem ser números!")
    except ZeroDivisionError:
        print("Sem notas!")

media_notas()