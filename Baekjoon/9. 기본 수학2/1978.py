N = int(input())
numList = list(map(int, input().split()))
result = 0

# 테스트케이스 만큼 반복
for i in range(N) :
    count = 0
    # 1부터 해당 수까지 반복문
    for j in range(1, numList[i] + 1) :
        if numList[i] % j == 0 :
            count += 1
        if count > 2 :
            break
    
    if count == 2 :
        result += 1

print(result)