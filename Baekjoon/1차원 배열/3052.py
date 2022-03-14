num = [0] * 10
r = [0] * 10
result = 10

for i in range(10) :
    num[i] = int(input())
    r[i] = num[i] % 42

for i in range(10) :
    for j in range(i+1, 10) :
        if r[i] == r[j] :
            result -= 1
            break

print(result)