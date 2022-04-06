T = int(input())
case = [0] * T
result = [0] * T

for i in range(T) :
    case[i] = input().split()

for i in range(T) :
    case[i][1] = list(case[i][1])

for i in range(T) :
    output = ""
    # word의 digit 만큼 반복
    for j in range(len(case[i][1])) :
        # 반복 횟수 만큼 반복
        for k in range(int(case[i][0])) :
            output += case[i][1][j]
    result[i] = output

for i in range(T) :
    print(result[i])