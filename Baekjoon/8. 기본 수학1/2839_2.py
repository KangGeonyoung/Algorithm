N = int(input())
result = []

for i in range(0, N//3 + 1) :
    threeKg = i
    newN = N - 3*i
    if newN % 5 == 0 :
        fiveKg = newN // 5
        result.append(threeKg + fiveKg)

if len(result) == 0 :
    print(-1)
else :
    print(min(result))
