# 숫자의 자리수를 정렬
N = list(map(int, input()))
sortN = sorted(N, reverse=True)

for i in range(len(sortN)) :
    print(sortN[i], end="")
