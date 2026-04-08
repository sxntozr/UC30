p = int(input())
d = int(input())
b = int(input())

total = p + 2*d + 3*b

if total >= 150:
    print("B")
elif total >= 120:
    print("D")
elif total >= 100:
    print("P")
else:
    print("N")