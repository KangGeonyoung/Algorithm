# 0 입력 시 입력 종료
nList = []
n = int(input())
while n!= 0 :
    nList.append(n)
    n = int(input())

# 에라토스테네스의 체 
def prime_list(n) :
    sieve = [True] * (2 * n + 1)
    m = int(2 * n ** 0.5)

    for i in range(2, m + 1) :
        if sieve[i] == True :
            for j in range(i + i, 2 * n + 1, i) :
                sieve[j] = False

    return [i for i in range(n, 2 * n + 1) if sieve[i] == True]

# 테스트케이스 만큼 반복
for i in range(len(nList)) :
    result = []
    result = prime_list(nList[i])
    
    # n보다 큰 범위이기 때문에 result 속에서 n을 지워주자
    if result.count(nList[i]) > 0 :
        result.remove(nList[i])

    print(len(result))
