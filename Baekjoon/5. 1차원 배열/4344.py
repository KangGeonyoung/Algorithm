C = int(input())
Class = [0] * C
avg = [0] * C
result = [0] * C

for i in range(C) :
    Class[i] = list(map(int, input().split()))

for i in range(C) :
    total = 0
    for j in range(1, len(Class[i])) :
        total += Class[i][j]
    avg[i] = total / Class[i][0]

for i in range(C) :
    total = 0
    for j in range(Class[i][0]) :
        if avg[i] < Class[i][j+1] :
            total += 1
    result[i] = float(total / Class[i][0] * 100)

for i in range(C) :
    print(f"{round(result[i], 3):.3f}%")