T = int(input())
H = [0] * T
W = [0] * T
N = [0] * T

line = [0] * T
floor = [0] * T
result = [0] * T

for i in range(T) :
    H[i], W[i], N[i] = map(int, input().split())

for i in range(T) :
    line[i] = N[i] // H[i]
    floor[i] = N[i] % H[i]

    # 제일 위 층일 경우 floor가 0이 나오기 때문에 따로 처리해줘야 함.
    if floor[i] == 0 :
        result[i] = H[i] * 100 + line[i]
    else :
        result[i] = floor[i] * 100 + line[i] + 1

for i in range(T) :
    print(result[i])