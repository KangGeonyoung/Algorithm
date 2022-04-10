cycle = 0
N = int(input())
tempN = N

while True :
    cycle += 1

    a = tempN // 10
    b = tempN % 10
    c = a + b
    d = c % 10
    newN = b*10 + d
    tempN = newN

    if N == newN :
        break
print(cycle)