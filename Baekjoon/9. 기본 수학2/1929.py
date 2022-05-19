M, N = map(int, input().split())

# 에라토스테네스의 체 
def prime_list(n) :
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)

    for i in range(2, m + 1) :
        if sieve[i] == True :
            for j in range(i + i, n + 1, i) :
                sieve[j] = False

    return [i for i in range(M, n + 1) if sieve[i] == True]

# 1이 result에 들어갔을 때 삭제해주는 코드 부분
result = prime_list(N)
if result.count(1) > 0 :
    result.remove(1)

# 결과 출력 과정
for i in range(len(result)) :
    print(result[i])