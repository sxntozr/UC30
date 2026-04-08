n = int(input())
r = int(input())
p = int(input())

total = n
infectados_hoje = n
dias = 0

while total < p:
    novos = infectados_hoje * r
    total += novos
    infectados_hoje = novos
    dias += 1

print(dias)