n = int(input())
result = [0] * n

for i in range(n) :
    a, b = map(int, input().split())
    result[i] = a + b

for i in range(n) :
    print(result[i])