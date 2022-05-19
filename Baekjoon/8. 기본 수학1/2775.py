# PyPy3로 제출하면 시간초과가 발생하지 않고 정답처리 됨.
T = int(input())
k = [0] * T
n = [0] * T
result = [0] * T

for i in range(T) :
    k[i] = int(input())
    n[i] = int(input())

def contract(k, n) :

    if k == 0 :
        return n
    
    if n == 1 :
        return n

    return contract(k, n-1) + contract(k-1, n)

for i in range(T) :
    result[i] = contract(k[i], n[i])

for i in range(T) :
    print(result[i])