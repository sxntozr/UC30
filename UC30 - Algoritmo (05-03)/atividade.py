import random

numeros = [10, 20, 30, 20, 40, 20, 50]
print("Lista oficial: ", numeros)

print("Qt. de Elementos: ", len(numeros))

print("Quantas vezes o número 20 aparece: ", numeros.count(20))

print("30 está na lista? ", 30 in numeros)
print("100 está na lista? ", 100 in numeros)

# ----------------------------------------------------------------

numeros2 = [91,34, 67, 15, 82]
print("Lista oficial: ", numeros2)

numeros2.sort()
print("Após sort(): ", numeros2)

numeros2.sort(reverse=True)
print("Após sort(): ", numeros2)

# ----------------------------------------------------------------

numeros3 = [80, 7, 10, 9, 19]
print("Lista oficial: ", numeros3)

random.shuffle(numeros3)
print("Embaralhar: ", numeros3)

# ----------------------------------------------------------------

numeros4 = [1, 6, 4, 3, 2, 5]
print("Lista oficial: ", numeros4)

numeros4.sort()
print("Após sort(): ", numeros4)

numeros4.sort(reverse=True)
print("Após sort(): ", numeros4)

random.shuffle(numeros4)
print("Embaralhar: ", numeros4)