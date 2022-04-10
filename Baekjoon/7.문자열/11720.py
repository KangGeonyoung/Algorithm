N = int(input())
num = int(input())
digit = [0] * N

for i in range(N) :
    digit[i] = num % 10
    num = num // 10

total = 0

for i in range(N) :
    total += digit[i]

print(total)