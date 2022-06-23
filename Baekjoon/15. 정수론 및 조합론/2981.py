import sys

N = int(sys.stdin.readline())
num = list()
result = list()

for i in range(N) :
    num.append(int(sys.stdin.readline()))

Min = min(num)

# M 범위
for i in range(2, Min+1) :
    state = 1
    # 한 줄씩 검사
    for j in range(len(num)) :
        if j+1 == len(num) :
            break

        if num[j] % i != num[j+1] % i :
            state = 0
            break
    
    if state == 1 :
        result.append(i)

for i in range(len(result)) :
    print(result[i], end=' ')

print(result)