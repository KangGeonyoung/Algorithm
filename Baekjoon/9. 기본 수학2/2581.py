M = int(input())
N = int(input())

outputCnt = 0
firstOutput = 0
sum = 0

# M~N 숫자까지 반복
for i in range(M, N+1) :
    count = 0
    # 1부터 해당 수까지 반복문
    for j in range(1, i + 1) :
        if i % j == 0 :
            count += 1
        if count > 2 :
            break
    
    # 소수를 찾았을 경우
    if count == 2 :
        outputCnt += 1
        sum += i

        # 범위 안에서 첫 번 째 소수를 찾았을 경우
        if outputCnt == 1 :
            firstOutput = i
if outputCnt > 0 :
    print(sum)
    print(firstOutput)
else :
    print("-1")