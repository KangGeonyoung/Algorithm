N = int(input())
case = [0] * N
grade = [0] * N

for i in range(N) :
    case[i] = list(input())

for i in range(N) :
    unit = 0
    for j in range(len(case[i])) :
        if case[i][j] == 'O' :
            unit += 1
            grade[i] += unit
        else :
            unit = 0

for i in range(N) :
    print(grade[i])