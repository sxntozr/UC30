P = int(input())
D = int(input())
B = int(input())

total = P + 2*D + 3*B

if total >= 150:
    print()
elif total >= 120:
    print("D")
elif total >= 100:
    print("P")
else:
    print("N")