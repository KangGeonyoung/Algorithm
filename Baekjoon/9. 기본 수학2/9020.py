import math

T = int(input())
num = [0] * T

# 테스트케이스 만큼 input 입력 받기
for i in range(T) :
    num[i] = int(input())

# 범위 내 소수 리스트를 return하는 함수(에라토스테네스의 체)
def prime_list(num) :
    m = int(num ** 0.5)
    che = [True] * num

    for i in range(2, m + 1) :
        if che[i] == True :
            for j in range(i + i, num, i) :
                che[j] = False

    return [i for i in range(2, num) if che[i] == True]

# 1-10000 범위 내에서 소수 찾기
primeList = prime_list(10000)

# 테스트케이스 만큼 반복
for i in range(T) :
    result = []
    result.clear()
    
    # 입력 받은 num의 절반까지만 검사
    for j in primeList:
        # 절반만 검사
        if j > int(num[i]/2) :
            continue
        # 입력 받은 num에서 j를 뺀 수를 소수인지 검사
        if primeList.count(num[i] - j) == 0 :
            continue
        else :
            result.append(j)

    # (소수 + 소수)가 한 쌍밖에 나오지 않았다면 바로 출력
    if len(result) == 1 :
        print(f"{result[0]} {num[i] - result[0]}")
    # 한 쌍 이상이라면 마지막 값을 출력
    else :
        lastValue = result.pop()
        print(f"{lastValue} {num[i] - lastValue}")